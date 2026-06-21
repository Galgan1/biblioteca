/**
 * instagram.js — publicação no Instagram via Graph API v21 (Node, CommonJS).
 *
 * Porte do videos/instagram_post.py (stdlib urllib) para o serviço Node, usando
 * o `fetch` global (Node 18+). Mesmo fluxo de 2/3 passos da Graph API:
 *   1) criar contêiner de mídia em POST /{uid}/media
 *   2) (carrossel/reel) aguardar o processamento via GET /{id}?fields=status_code
 *   3) publicar em POST /{uid}/media_publish com o creation_id
 * O permalink final vem de GET /{id}?fields=permalink.
 *
 * Diferença vs. o Python: aqui as IMAGENS/VÍDEOS chegam por URL pública
 * (image_url / video_url) — não há upload resumável de bytes. Quem hospeda os
 * JPEG/MP4 (na VPS) é a camada de cima (publish_assets / runner).
 *
 * Env:
 *   IG_TOKEN_FILE  caminho do JSON do token (default /opt/biblioteca-pdf/.secrets/instagram.json)
 *   IG_USER_ID     id numérico da conta IG Business/Creator
 *   IG_APP_ID, IG_APP_SECRET  (opcionais, só para refreshToken() — nunca chamado sozinho)
 *
 * Shape do JSON do token: { access_token, expires_in, _obtained_at }.
 */
const fs = require('fs');

const GRAPH = 'https://graph.facebook.com/v21.0';
const DEFAULT_TOKEN_FILE = '/opt/biblioteca-pdf/.secrets/instagram.json';

// ---------------------------------------------------------------- credenciais
// Lê o access_token do JSON (mantém simples: sem renovação automática — espelha
// o _token() do Python sem o ramo de refresh; refreshToken() existe abaixo mas
// só roda se a camada de cima chamar de propósito).
function loadToken() {
  const file = process.env.IG_TOKEN_FILE || DEFAULT_TOKEN_FILE;
  let tj;
  try {
    tj = JSON.parse(fs.readFileSync(file, 'utf8'));
  } catch (e) {
    throw new Error(`token IG ausente/ilegível em ${file}: ${e.message}`);
  }
  if (!tj.access_token) throw new Error(`token IG sem access_token em ${file}`);
  return tj.access_token;
}

function userId() {
  const uid = process.env.IG_USER_ID;
  if (!uid) throw new Error('IG_USER_ID ausente (id numérico da conta IG Business/Creator)');
  return uid;
}

// ------------------------------------------------------------------- HTTP
// Mensagem de erro rica: superfície o `error.message` que a Graph API devolve
// no corpo (igual ao Python, que carrega o JSON e expõe error.message).
async function graphError(res, label) {
  let body;
  try { body = await res.json(); } catch { body = null; }
  const msg = body && body.error && body.error.message
    ? body.error.message
    : `HTTP ${res.status}`;
  const err = new Error(`Graph API ${label}: ${msg}`);
  err.status = res.status;
  if (body && body.error) err.graph = body.error;
  return err;
}

// GET /{path}?...&access_token=... (espelha _get)
async function graphGet(path, params = {}) {
  const token = loadToken();
  const qs = new URLSearchParams({ ...params, access_token: token });
  const res = await fetch(`${GRAPH}${path}?${qs}`);
  if (!res.ok) throw await graphError(res, `GET ${path}`);
  return res.json();
}

// POST /{path} com corpo urlencoded incluindo access_token (espelha _post)
async function graphPost(path, params = {}) {
  const token = loadToken();
  const body = new URLSearchParams({ ...params, access_token: token });
  const res = await fetch(`${GRAPH}${path}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body,
  });
  if (!res.ok) throw await graphError(res, `POST ${path}`);
  return res.json();
}

// ------------------------------------------------------------------- helpers
// permalink final do post (igual ao _get(id, fields=permalink) implícito).
async function permalinkOf(id) {
  const r = await graphGet(`/${id}`, { fields: 'permalink' });
  return r.permalink || null;
}

// Aguarda o contêiner sair de IN_PROGRESS. status_code: FINISHED | ERROR |
// EXPIRED | IN_PROGRESS. Espelha o laço de polling do Python (sleep entre gets).
// timeoutMs ~120s, intervalo 5s. Aborta em ERROR/EXPIRED.
async function waitFinished(containerId, { timeoutMs = 120000, intervalMs = 5000 } = {}) {
  const deadline = Date.now() + timeoutMs;
  for (;;) {
    const r = await graphGet(`/${containerId}`, { fields: 'status_code' });
    const st = r.status_code;
    if (st === 'FINISHED') return;
    if (st === 'ERROR' || st === 'EXPIRED') {
      throw new Error(`processamento do contêiner ${containerId} falhou: ${st}`);
    }
    if (Date.now() >= deadline) {
      throw new Error(`timeout aguardando processamento do contêiner ${containerId} (status=${st || 'desconhecido'})`);
    }
    await new Promise((r2) => setTimeout(r2, intervalMs));
  }
}

// media_publish + permalink. Em dryRun, NÃO publica: devolve só o contêiner.
async function publishContainer(uid, containerId, opts, extra = {}) {
  if (opts && opts.dryRun) {
    return { dryRun: true, containerId, ...extra };
  }
  const pub = await graphPost(`/${uid}/media_publish`, { creation_id: containerId });
  const id = pub.id;
  const permalink = await permalinkOf(id);
  return { id, permalink };
}

// ------------------------------------------------------------------- API pública

// Foto única no feed: contêiner {image_url, caption} -> media_publish.
async function publishImage(imageUrl, caption, opts = {}) {
  const uid = userId();
  const cont = await graphPost(`/${uid}/media`, { image_url: imageUrl, caption: caption || '' });
  return publishContainer(uid, cont.id, opts);
}

// Story (9:16): contêiner {media_type:STORIES, image_url} — sem caption. Stories
// processam rápido; aqui não fazemos polling (igual ao caminho do Python, que
// tolera status null) — vamos direto ao publish.
async function publishStory(imageUrl, opts = {}) {
  const uid = userId();
  const cont = await graphPost(`/${uid}/media`, { media_type: 'STORIES', image_url: imageUrl });
  return publishContainer(uid, cont.id, opts);
}

// Carrossel: 2..10 filhos {image_url, is_carousel_item} -> pai {CAROUSEL,
// children, caption} -> aguarda processamento -> publica.
async function publishCarousel(imageUrls, caption, opts = {}) {
  const uid = userId();
  if (!Array.isArray(imageUrls) || imageUrls.length < 2 || imageUrls.length > 10) {
    throw new Error(`carrossel precisa de 2 a 10 imagens; recebi ${Array.isArray(imageUrls) ? imageUrls.length : 'não-array'}`);
  }
  // 1) contêineres-filho (um por slide)
  const children = [];
  for (const url of imageUrls) {
    const c = await graphPost(`/${uid}/media`, { image_url: url, is_carousel_item: 'true' });
    children.push(c.id);
  }
  // 2) contêiner CAROUSEL
  const parent = await graphPost(`/${uid}/media`, {
    media_type: 'CAROUSEL',
    children: children.join(','),
    caption: caption || '',
  });
  if (opts && opts.dryRun) {
    return { dryRun: true, containerId: parent.id, children };
  }
  // 3) aguarda processamento e publica
  await waitFinished(parent.id, opts);
  return publishContainer(uid, parent.id, opts, { children });
}

// Reel: contêiner {REELS, video_url, caption, share_to_feed} -> aguarda
// status_code=FINISHED (vídeo demora a processar) -> publica.
async function publishReel(videoUrl, caption, opts = {}) {
  const uid = userId();
  const cont = await graphPost(`/${uid}/media`, {
    media_type: 'REELS',
    video_url: videoUrl,
    caption: caption || '',
    share_to_feed: 'true',
  });
  if (opts && opts.dryRun) {
    return { dryRun: true, containerId: cont.id };
  }
  await waitFinished(cont.id, opts);
  return publishContainer(uid, cont.id, opts);
}

// ------------------------------------------------------------------- refresh
// Troca o token de 60 dias por outro de 60 dias (fb_exchange_token). Espelha o
// _refresh do Python. NÃO é chamado automaticamente — a camada de cima decide.
// Regrava o JSON do token com { access_token, expires_in, _obtained_at }.
async function refreshToken() {
  const appId = process.env.IG_APP_ID;
  const appSecret = process.env.IG_APP_SECRET;
  if (!appId || !appSecret) {
    throw new Error('refreshToken requer IG_APP_ID e IG_APP_SECRET no ambiente');
  }
  const file = process.env.IG_TOKEN_FILE || DEFAULT_TOKEN_FILE;
  const current = loadToken();
  const qs = new URLSearchParams({
    grant_type: 'fb_exchange_token',
    client_id: appId,
    client_secret: appSecret,
    fb_exchange_token: current,
  });
  const res = await fetch(`${GRAPH}/oauth/access_token?${qs}`);
  if (!res.ok) throw await graphError(res, 'GET /oauth/access_token');
  const r = await res.json();
  if (!r.access_token) throw new Error('refreshToken: resposta sem access_token');
  r._obtained_at = Math.floor(Date.now() / 1000);
  fs.writeFileSync(file, JSON.stringify(r, null, 2));
  return r.access_token;
}

// Cota de publicação do IG (janela móvel de 24h). Carrossel/Reel contam como 1.
// Devolve { used, total, remaining }. Erra "para cima" (total 50) se o IG omitir.
async function publishingLimit() {
  const uid = userId();
  const r = await graphGet(`/${uid}/content_publishing_limit`, { fields: 'config,quota_usage' });
  const row = (r && Array.isArray(r.data) && r.data[0]) || {};
  const total = (row.config && Number(row.config.quota_total)) || 50;
  const used = Number(row.quota_usage) || 0;
  return { used: used, total: total, remaining: Math.max(0, total - used) };
}

module.exports = {
  loadToken,
  userId,
  graphGet,
  graphPost,
  publishImage,
  publishStory,
  publishCarousel,
  publishReel,
  publishingLimit,
  refreshToken,
};
