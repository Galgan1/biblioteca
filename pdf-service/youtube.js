/**
 * youtube.js — upload de vídeo para o YouTube via Data API v3 (Node, CommonJS).
 *
 * Porte do videos/upload_youtube.py para o serviço Node. Espelha o estilo de
 * instagram.js (loadX que lê JSON de .secrets, erros ricos, exports no fim).
 *
 * Espelha do Python:
 *   - build_metadata  -> buildMetadata  (mesmo snippet/status, mesmos fallbacks)
 *   - upload          -> publishVideo   (videos.insert part=snippet,status)
 *   - SCOPES force-ssl + refresh de token (a lib renova sozinha; regravamos)
 *   - thumb_set.py    -> setThumbnail   (thumbnails.set)
 *
 * Diferença vs. o Python: aqui o token vem da OAuth2 da google-auth-library, que
 * renova o access_token sozinha a partir do refresh_token; no evento `tokens`
 * regravamos o arquivo no formato Credentials.to_json() (chave `token`).
 *
 * Env:
 *   YT_TOKEN_FILE      caminho do JSON do token (default /opt/biblioteca-pdf/.secrets/youtube_token.json)
 *                      formato igual ao videos/.secrets/token_v2.json:
 *                      { token | access_token, refresh_token, token_uri, client_id, client_secret, scopes }
 *   YT_CLIENT_SECRET   client secret OAuth desktop (default /opt/biblioteca-pdf/.secrets/client_secret.json)
 *                      formato { installed: { client_id, client_secret, redirect_uris, ... } }
 *
 * IMPORTANTE: googleapis e google-auth-library são exigidos por require LAZY,
 * dentro de loadAuth() — assim buildMetadata() (e o teste) rodam sem as libs.
 */
const fs = require('fs');

// força-ssl = escopo amplo (upload + editar/agendar + comentários). Mesmo do Python.
const SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl'];
const DEFAULT_TOKEN_FILE = '/opt/biblioteca-pdf/.secrets/youtube_token.json';
const DEFAULT_CLIENT_SECRET = '/opt/biblioteca-pdf/.secrets/client_secret.json';

// ---------------------------------------------------------------- credenciais
// Lê JSON do disco com mensagem de erro rica (espelha loadToken do instagram.js).
function readJson(file, label) {
  try {
    return JSON.parse(fs.readFileSync(file, 'utf8'));
  } catch (e) {
    throw new Error(`${label} ausente/ilegível em ${file}: ${e.message}`);
  }
}

// Monta o cliente OAuth2 a partir do token + client secret no disco.
// A lib (google-auth-library) renova o access_token sozinha pelo refresh_token;
// no evento `tokens` regravamos o arquivo p/ persistir o access_token novo.
function loadAuth() {
  // require lazy: só aqui as libs são exigidas (buildMetadata roda sem elas).
  const { google } = require('googleapis');

  const tokenFile = process.env.YT_TOKEN_FILE || DEFAULT_TOKEN_FILE;
  const secretFile = process.env.YT_CLIENT_SECRET || DEFAULT_CLIENT_SECRET;

  const tj = readJson(tokenFile, 'token YouTube');
  const cs = readJson(secretFile, 'client secret YouTube');
  const inst = cs.installed || cs.web || cs; // tolera installed/web/raiz

  // client_id/secret: preferem o client_secret.json; caem p/ o do token se faltar.
  const clientId = inst.client_id || tj.client_id;
  const clientSecret = inst.client_secret || tj.client_secret;
  if (!clientId || !clientSecret) {
    throw new Error(`client_id/client_secret ausentes (vistos em ${secretFile} e ${tokenFile})`);
  }
  const redirect = (Array.isArray(inst.redirect_uris) && inst.redirect_uris[0])
    || 'http://localhost';

  const oauth2 = new google.auth.OAuth2(clientId, clientSecret, redirect);

  // token_v2.json (Python) usa `token`; outras fontes usam `access_token`.
  const accessToken = tj.token || tj.access_token;
  if (!tj.refresh_token) {
    throw new Error(`token YouTube sem refresh_token em ${tokenFile} (renovação impossível)`);
  }
  oauth2.setCredentials({
    refresh_token: tj.refresh_token,
    access_token: accessToken,
    token_uri: tj.token_uri,
    scope: (Array.isArray(tj.scopes) ? tj.scopes.join(' ') : tj.scope) || SCOPES.join(' '),
  });

  // Persiste o token renovado no MESMO formato (chave `token`, como o Python).
  oauth2.on('tokens', (tokens) => {
    try {
      const cur = readJson(tokenFile, 'token YouTube');
      if (tokens.access_token) cur.token = tokens.access_token;
      if (tokens.refresh_token) cur.refresh_token = tokens.refresh_token;
      fs.writeFileSync(tokenFile, JSON.stringify(cur, null, 2));
    } catch (e) {
      // best-effort: não derruba o upload se a regravação falhar.
      console.error(`[youtube] aviso: não regravou token em ${tokenFile}: ${e.message}`);
    }
  });

  return google.youtube({ version: 'v3', auth: oauth2 });
}

// ------------------------------------------------------------------- metadados
// Espelha upload_youtube.build_metadata: lê o roteiro e monta snippet/status.
// Fallbacks idênticos (título "<titulo>, de <autor> — Resumo em ~5 min", etc.).
function buildMetadata(roteiroPath) {
  const cfg = readJson(roteiroPath, 'roteiro');
  const yt = cfg.youtube || {};

  const conceitos = (cfg.cenas || [])
    .filter((c) => c.tipo === 'conceito')
    .map((c) => c.titulo)
    .join(' • ');

  const slug = cfg.slug || '';
  const titulo = yt.titulo || `${cfg.titulo}, de ${cfg.autor} — Resumo em ~5 min`;
  const desc = yt.descricao || (
    `Um resumo essencial de "${cfg.titulo}", de ${cfg.autor}.\n\n`
    + `Princípios abordados: ${conceitos}.\n\n`
    + `📚 Biblioteca de André Galgani — https://www.andregalgani.com.br/biblioteca\n\n`
    + `#resumo #livros #${slug.replace(/-/g, '')}`
  );
  const tags = yt.tags || [
    cfg.titulo, cfg.autor, 'resumo de livro',
    'resumo', 'livros', 'audiolivro', 'filosofia',
  ];
  const privacyStatus = yt.privacidade || 'unlisted'; // unlisted = revisar antes de publicar

  return {
    snippet: {
      title: String(titulo).slice(0, 100),
      description: String(desc).slice(0, 5000),
      tags,
      categoryId: '27', // Education
      defaultLanguage: 'pt-BR',
    },
    status: {
      privacyStatus,
      selfDeclaredMadeForKids: false,
      // Divulgação obrigatória (política YouTube): narração/visuais gerados por IA.
      containsSyntheticMedia: true,
    },
  };
}

// ------------------------------------------------------------------- upload
// videos.insert(part=snippet,status). Em dryRun: valida entradas e monta o
// request, mas NÃO chama a API — devolve { dryRun:true, meta }.
async function publishVideo(mp4Path, meta, opts = {}) {
  if (!meta || !meta.snippet || !meta.status) {
    throw new Error('meta inválido: esperava { snippet, status } (use buildMetadata)');
  }
  if (!fs.existsSync(mp4Path)) {
    throw new Error(`vídeo não encontrado em ${mp4Path}`);
  }
  // privacidade: opts.privacy > meta.status.privacyStatus > 'unlisted'.
  const privacyStatus = opts.privacy || meta.status.privacyStatus || 'unlisted';
  const requestBody = {
    snippet: meta.snippet,
    status: { ...meta.status, privacyStatus },
  };

  if (opts.dryRun) {
    return { dryRun: true, meta: { ...meta, status: requestBody.status } };
  }

  const yt = loadAuth();
  const resp = await yt.videos.insert({
    part: 'snippet,status',
    requestBody,
    media: { mimeType: 'video/mp4', body: fs.createReadStream(mp4Path) },
  });
  const id = resp.data.id;
  return { id, url: `https://youtu.be/${id}` };
}

// ------------------------------------------------------------------- thumbnail
// thumbnails.set — espelha videos/thumb_set.py. Requer canal verificado.
async function setThumbnail(videoId, pngPath) {
  if (!fs.existsSync(pngPath)) {
    throw new Error(`thumbnail não encontrada em ${pngPath}`);
  }
  const yt = loadAuth();
  const resp = await yt.thumbnails.set({
    videoId,
    media: { mimeType: 'image/png', body: fs.createReadStream(pngPath) },
  });
  return resp.data;
}

module.exports = {
  loadAuth,
  buildMetadata,
  publishVideo,
  setThumbnail,
};
