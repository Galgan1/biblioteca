/**
 * biblioteca-pdf — serviço de geração de PDF premium (A4) da Biblioteca.
 *
 * Rotas:
 *   GET /pdf/:book/visao-geral.pdf     → PDF da página de visão geral do livro
 *   GET /pdf/:book/livro-completo.pdf  → capa + visão geral + todos os capítulos
 *   GET /pdf/:book/:page.pdf           → PDF de uma página de capítulo
 *   GET /health
 *
 * Estratégia: on-demand com cache em disco. A chave do cache embute mtime/size
 * dos arquivos-fonte (+ style.css/psicodelia.css + VERSION); mudou a página,
 * o PDF é regenerado no próximo pedido.
 *
 * Env: PORT (3008) · SITE_ROOT (/var/www/andregalgani/biblioteca) ·
 *      CHROME (/usr/bin/google-chrome)
 */
const path = require('path');
const fs = require('fs');
const fsp = fs.promises;
const crypto = require('crypto');
const express = require('express');
const puppeteer = require('puppeteer-core');
const QRCode = require('qrcode');
const { PDFDocument } = require('pdf-lib');
const makeAuth = require('./auth');                 // login multiusuário + papéis
const instagram = require('./instagram');           // publicação IG via Graph API
const publishAssets = require('./publish_assets');  // mídia + legenda do post

const PORT = Number(process.env.PORT) || 3008;
const SITE_ROOT = process.env.SITE_ROOT || '/var/www/andregalgani/biblioteca';
const CHROME = process.env.CHROME || '/usr/bin/google-chrome';
const CACHE_DIR = path.join(__dirname, 'cache');
const VERSION = 11; // suba para invalidar todo o cache após mudar o layout

// ----------------------------------------------------------- paywall (Pix)
// DESLIGADO por enquanto (downloads gratuitos enquanto os PDFs amadurecem).
// Para religar: PAYWALL = true aqui E no script-livro.js do site (+ cópias).
const PAYWALL = false;
// Pix estático (Bipa). Liberação atual: por confiança — o token é emitido ao
// clicar "já paguei". Quando houver PSP com webhook, mover a emissão do token
// para o handler do webhook e nada mais muda.
const PIX_CODE = process.env.PIX_CODE ||
  '00020126580014br.gov.bcb.pix013686af0c5d-f4f7-4141-ace0-86aed1f591d252040000530398654042.005802BR5917ANDRE NUNES GOMES6014Belo Horizonte62290525d9CUWsBOiNownzZVoV3DI5HeI6304BBD4';
const PIX_AMOUNT = process.env.PIX_AMOUNT || 'R$ 2,00';
const TOKEN_TTL_MS = 1000 * 60 * 90; // 90 min

// segredo persistente (sobrevive a restarts → links emitidos continuam válidos)
const SECRET_FILE = path.join(__dirname, 'secret.key');
let SECRET = process.env.PDF_SECRET || '';
if (!SECRET) {
  try { SECRET = fs.readFileSync(SECRET_FILE, 'utf8').trim(); } catch {}
  if (!SECRET) {
    SECRET = crypto.randomBytes(32).toString('hex');
    fs.writeFileSync(SECRET_FILE, SECRET, { mode: 0o600 });
  }
}

function signToken(book, page, exp) {
  return crypto.createHmac('sha256', SECRET).update(`${book}.${page}.${exp}`).digest('hex');
}
function makeToken(book, page) {
  const exp = Date.now() + TOKEN_TTL_MS;
  return `${exp}.${signToken(book, page, exp)}`;
}
function checkToken(book, page, token) {
  if (!token) return false;
  const [expStr, sig] = String(token).split('.');
  const exp = Number(expStr);
  if (!exp || !sig || exp < Date.now()) return false;
  const good = signToken(book, page, exp);
  return sig.length === good.length && crypto.timingSafeEqual(Buffer.from(sig), Buffer.from(good));
}

const GREEN = '#0f7a4d';
const SLUG_RE = /^[a-z0-9-]+$/;

fs.mkdirSync(CACHE_DIR, { recursive: true });

// ------------------------------------------------------------ estatísticas
// Visitas (geral e por livro, via beacon do script.js) e downloads por
// arquivo (contados na própria rota do PDF). Agregados por dia em stats.json.
// Visitante único = hash truncado de ip+user-agent+dia — nenhum IP em claro.
const STATS_FILE = path.join(__dirname, 'stats.json');
let STATS = { days: {} };
try { STATS = JSON.parse(fs.readFileSync(STATS_FILE, 'utf8')); } catch {}
if (!STATS || typeof STATS.days !== 'object') STATS = { days: {} };

let statsTimer = null;
function saveStatsSoon() {
  if (statsTimer) return;
  statsTimer = setTimeout(() => {
    statsTimer = null;
    fsp.writeFile(STATS_FILE, JSON.stringify(STATS)).catch(() => {});
  }, 5000);
}
function saveStatsNow() { try { fs.writeFileSync(STATS_FILE, JSON.stringify(STATS)); } catch {} }
// votos (joinha/desjoinha) — agregados globais por livro em votes.json.
// O voto do visitante fica no localStorage do navegador; o cliente manda a
// transição (from->to) e o servidor ajusta as contagens. Honor-system (como o stats).
const VOTES_FILE = path.join(__dirname, 'votes.json');
let VOTES = {};
try { VOTES = JSON.parse(fs.readFileSync(VOTES_FILE, 'utf8')); } catch {}
if (!VOTES || typeof VOTES !== 'object') VOTES = {};
let votesTimer = null;
function saveVotesSoon() {
  if (votesTimer) return;
  votesTimer = setTimeout(() => { votesTimer = null; fsp.writeFile(VOTES_FILE, JSON.stringify(VOTES)).catch(() => {}); }, 3000);
}
function saveVotesNow() { try { fs.writeFileSync(VOTES_FILE, JSON.stringify(VOTES)); } catch {} }
function getVotes(book) { const v = VOTES[book] || {}; return { up: v.up || 0, down: v.down || 0 }; }
function applyVote(book, from, to) {
  const v = getVotes(book);
  if (from === 'up') v.up = Math.max(0, v.up - 1);
  if (from === 'down') v.down = Math.max(0, v.down - 1);
  if (to === 'up') v.up += 1;
  if (to === 'down') v.down += 1;
  VOTES[book] = v;
  saveVotesSoon();
  return v;
}

process.on('SIGINT', () => { saveStatsNow(); saveVotesNow(); process.exit(0); });
process.on('SIGTERM', () => { saveStatsNow(); saveVotesNow(); process.exit(0); });

const BOT_RE = /bot|crawl|spider|slurp|facebookexternalhit|preview|curl|wget|python|headless|lighthouse/i;
const dayKey = () => new Date().toISOString().slice(0, 10);
function dayData() {
  const d = dayKey();
  if (!STATS.days[d]) STATS.days[d] = { views: 0, visitors: [], books: {}, downloads: {} };
  return STATS.days[d];
}
function visitorHash(req) {
  const ua = req.headers['user-agent'] || '';
  return crypto.createHash('sha256').update(`${req.ip}|${ua}|${dayKey()}`).digest('hex').slice(0, 16);
}
function countHit(req, book) {
  if (BOT_RE.test(req.headers['user-agent'] || '')) return;
  const d = dayData();
  d.views += 1;
  const h = visitorHash(req);
  if (!d.visitors.includes(h)) d.visitors.push(h);
  d.books[book] = (d.books[book] || 0) + 1;
  saveStatsSoon();
}
function countDownload(req, book, page) {
  if (BOT_RE.test(req.headers['user-agent'] || '')) return;
  const d = dayData();
  const k = `${book}/${page}`;
  d.downloads[k] = (d.downloads[k] || 0) + 1;
  saveStatsSoon();
}

// resumo agregado: geral por período + por livro + downloads por arquivo
function statsSummary() {
  const today = dayKey();
  const cut = (n) => new Date(Date.now() - (n - 1) * 864e5).toISOString().slice(0, 10);
  const d7 = cut(7), d30 = cut(30);
  const out = {
    geral: {
      hoje: { visitas: 0, visitantes: 0 },
      dias7: { visitas: 0, visitantes: 0 },
      dias30: { visitas: 0, visitantes: 0 },
      total: { visitas: 0, visitantes: 0 },
    },
    livros: {},
    downloads: {},
    desde: today,
  };
  const days = Object.keys(STATS.days).sort();
  if (days.length) out.desde = days[0];
  for (const d of days) {
    const x = STATS.days[d];
    const u = (x.visitors || []).length;
    const add = (g) => { g.visitas += x.views || 0; g.visitantes += u; };
    add(out.geral.total);
    if (d >= d30) add(out.geral.dias30);
    if (d >= d7) add(out.geral.dias7);
    if (d === today) add(out.geral.hoje);
    for (const [slug, n] of Object.entries(x.books || {})) {
      const e = out.livros[slug] || (out.livros[slug] = { dias30: 0, total: 0 });
      e.total += n; if (d >= d30) e.dias30 += n;
    }
    for (const [k, n] of Object.entries(x.downloads || {})) {
      const e = out.downloads[k] || (out.downloads[k] = { dias30: 0, total: 0 });
      e.total += n; if (d >= d30) e.dias30 += n;
    }
  }
  return out;
}

function statsPage(s) {
  let titles = {};
  try {
    titles = Object.fromEntries(JSON.parse(fs.readFileSync(path.join(SITE_ROOT, 'books.json'), 'utf8'))
      .map((b) => [b.id, b.title]));
  } catch {}
  const name = (slug) => slug === '_estante' ? 'Estante (página inicial)' : (titles[slug] || slug);
  const byTotal = (obj) => Object.entries(obj).sort((a, b) => b[1].total - a[1].total);
  const rows = (obj, label) => byTotal(obj)
    .map(([k, v]) => `<tr><td>${label(k)}</td><td>${v.dias30}</td><td>${v.total}</td></tr>`)
    .join('') || '<tr><td colspan="3" class="vazio">sem registros ainda</td></tr>';
  const g = s.geral;
  return `<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>Estatísticas · Biblioteca</title>
<style>
  body { font-family: 'Hanken Grotesk', system-ui, sans-serif; max-width: 880px;
         margin: 2rem auto; padding: 0 1rem; color: #1a1a1a; background: #fcfdfc; }
  h1 { text-transform: uppercase; font-weight: 800; }
  h1 .light { color: ${GREEN}; }
  h2 { text-transform: uppercase; font-size: 0.95rem; letter-spacing: 0.04em;
       background: ${GREEN}; color: #fff; display: inline-block;
       padding: 0.25rem 0.8rem; border-radius: 999px; margin: 1.6rem 0 0.5rem; }
  table { border-collapse: collapse; width: 100%; }
  th, td { text-align: left; padding: 0.4rem 0.6rem; border-bottom: 1px dashed ${GREEN}; }
  th { text-transform: uppercase; font-size: 0.72rem; letter-spacing: 0.05em; color: #555; }
  td:nth-child(n+2), th:nth-child(n+2) { text-align: right; width: 7.5rem; }
  .vazio { color: #888; font-style: italic; }
  .nota { color: #555; font-size: 0.8rem; margin-top: 1.6rem; }
</style></head><body>
<h1><span class="light">Biblioteca</span> · Estatísticas</h1>
<h2>Visitas — geral</h2>
<table><tr><th>Período</th><th>Visitas</th><th>Visitantes</th></tr>
<tr><td>Hoje</td><td>${g.hoje.visitas}</td><td>${g.hoje.visitantes}</td></tr>
<tr><td>Últimos 7 dias</td><td>${g.dias7.visitas}</td><td>${g.dias7.visitantes}</td></tr>
<tr><td>Últimos 30 dias</td><td>${g.dias30.visitas}</td><td>${g.dias30.visitantes}</td></tr>
<tr><td>Total (desde ${s.desde})</td><td>${g.total.visitas}</td><td>${g.total.visitantes}</td></tr></table>
<h2>Visitas — por livro</h2>
<table><tr><th>Livro</th><th>30 dias</th><th>Total</th></tr>${rows(s.livros, name)}</table>
<h2>Downloads — por arquivo</h2>
<table><tr><th>Arquivo (livro/página)</th><th>30 dias</th><th>Total</th></tr>${rows(s.downloads, (k) => k)}</table>
<p class="nota">Visitantes = únicos por dia (hash anônimo de IP + navegador; somados entre dias).
Robôs e crawlers são ignorados. JSON bruto em <a href="stats.json" style="color:${GREEN}">stats.json</a>.</p>
</body></html>`;
}

// ---------------------------------------------------------------- browser
let browserPromise = null;
function getBrowser() {
  if (!browserPromise) {
    browserPromise = puppeteer
      .launch({
        executablePath: CHROME,
        headless: true,
        args: ['--no-sandbox', '--disable-dev-shm-usage', '--disable-gpu', '--hide-scrollbars'],
      })
      .then((b) => {
        b.on('disconnected', () => { browserPromise = null; });
        return b;
      })
      .catch((e) => { browserPromise = null; throw e; });
  }
  return browserPromise;
}

// fila: uma renderização por vez (limita memória do Chromium)
let queue = Promise.resolve();
function enqueue(job) {
  const run = queue.then(job, job);
  queue = run.catch(() => {});
  return run;
}

// ---------------------------------------------------------------- helpers
function readBooks() {
  try {
    return JSON.parse(fs.readFileSync(path.join(SITE_ROOT, 'books.json'), 'utf8'));
  } catch { return []; }
}

function bookMeta(book) {
  const b = readBooks().find((x) => x.id === book);
  return { title: b ? b.title : book, author: b ? b.author : '' };
}

function bookFull(book) {
  const b = readBooks().find((x) => x.id === book) || {};
  return { title: b.title || book, author: b.author || '', description: b.description || '', tags: b.tags || [] };
}

const escHtml = (v) => String(v).replace(/&/g, '&amp;').replace(/</g, '&lt;');

// Rodapé fino do PDF: assinatura discreta (QR p/ a página online + 1 linha de CTA).
// NÃO é mais "preenchedor" — o preenchimento das páginas curtas agora é feito com
// escala de fonte + ritmo (ar) no adaptiveFit. Toda página ganha esta assinatura.
async function buildFooter(book) {
  const meta = bookFull(book);
  const qr = await QRCode.toDataURL(`https://www.andregalgani.com.br/biblioteca/${book}.html`, { width: 168, margin: 1 });
  return `<aside class="pdf-footer">
    <img class="pdf-footer-qr" src="${qr}" alt="Abrir na Biblioteca">
    <div class="pdf-footer-txt">
      <strong>${escHtml(meta.title)}</strong> · resumo completo, capítulo a capítulo, em <span class="pdf-footer-cta">andregalgani.com.br/biblioteca</span><br>
      Gostou? Leia o livro na íntegra — o link de compra está na página online.
    </div>
  </aside>`;
}

async function statSig(file) {
  const st = await fsp.stat(file);
  return `${st.mtimeMs}:${st.size}`;
}

async function cacheKey(book, page, sources) {
  const parts = [`v${VERSION}`];
  for (const f of sources) parts.push(await statSig(f));
  for (const extra of ['assets/style.css', 'assets/psicodelia.css']) {
    try { parts.push(await statSig(path.join(SITE_ROOT, extra))); } catch {}
  }
  const hash = crypto.createHash('sha1').update(parts.join('|')).digest('hex').slice(0, 16);
  return `${book}--${page}--${hash}.pdf`;
}

async function cleanStale(book, page, keep) {
  const prefix = `${book}--${page}--`;
  let names = [];
  try { names = await fsp.readdir(CACHE_DIR); } catch { return; }
  for (const n of names) {
    if (n.startsWith(prefix) && n !== keep) fsp.unlink(path.join(CACHE_DIR, n)).catch(() => {});
  }
}

function extract(html, re, fallback = '') {
  const m = html.match(re);
  return m ? m[0] : fallback;
}

function textOf(html, re) {
  const m = html.match(re);
  return m ? m[1].replace(/<[^>]+>/g, '').replace(/\s+/g, ' ').trim() : '';
}

// CSS injetado na hora da impressão (não faz parte do site).
// Filosofia: cheat sheet de verdade — muita informação em pouco espaço.
// A fonte-base cai (o leitor de PDF dá zoom) e os cards empacotam em 2 colunas.
const PRINT_CSS = `
  .skip-link, .back-link, .chapter-nav, .footer, .pdf-actions, .amazon-cta,
  nav[aria-label="Navegação principal"], nav[aria-label="Navegação Voltar"] { display: none !important; }
  .animate-entrance { animation: none !important; opacity: 1 !important; transform: none !important; }

  /* corpo ~8pt: denso, mas confortável sem zoom */
  html { font-size: 11px; }
  .page { max-width: 100% !important; padding: 0 !important; }
  p, li { orphans: 2; widows: 2; }
  .card-body, .card-tip, .card-details-inner p, .content-list li, .lessons-list li {
    -webkit-hyphens: auto; hyphens: auto;
  }

  /* cabeçalho compacto */
  .header { margin: 0 0 0.8rem !important; padding: 0 0 0.6rem !important; }
  .header-title { font-size: 1.7rem !important; margin-bottom: 0.15rem !important; }
  .header-subtitle { font-size: 0.92rem !important; margin-bottom: 0.1rem !important; }
  .header-credit { font-size: 0.82rem !important; margin-bottom: 0.25rem !important; }
  .header-intro { font-size: 0.94rem !important; line-height: 1.4 !important; margin: 0.25rem auto 0 !important; max-width: 92% !important; }

  /* cards empacotados em 2 colunas (preenchimento vertical = denso) */
  .grid { display: block !important; columns: 2; column-gap: 1rem; margin-bottom: 0 !important; }
  .card {
    break-inside: avoid; page-break-inside: avoid;
    display: flex; margin: 0 0 1rem !important; padding: 0.75rem !important; gap: 0.55rem !important;
  }
  .card-icon { width: 22px !important; height: 22px !important; }
  .card-title { font-size: 0.85rem !important; padding: 0.2rem 0.6rem !important; margin-bottom: 0.35rem !important; border-radius: 6px !important; line-height: 1.2 !important; }
  .card-body { font-size: 0.94rem !important; line-height: 1.38 !important; margin-bottom: 0.3rem !important; }
  .card-tip { font-size: 0.86rem !important; line-height: 1.35 !important; margin-top: 0.25rem !important; }
  .card-details { display: block !important; }
  .card-details-inner p, .card-details-inner h3 { font-size: 0.88rem !important; margin: 0.22rem 0 !important; line-height: 1.35 !important; }
  blockquote { font-size: 0.88rem !important; margin: 0.3rem 0 !important; padding-left: 0.65rem !important; line-height: 1.35 !important; }
  .content-list { font-size: 0.9rem !important; margin: 0.25rem 0 0.25rem 1.05rem !important; }
  .content-list li, .lessons-list li { margin-bottom: 0.2rem !important; line-height: 1.35 !important; }

  /* Lições entram no fluxo das colunas (reparentadas no render) — viram um "card" largo */
  .lessons { break-inside: avoid; page-break-inside: avoid; padding: 0.75rem !important; margin: 0 0 1rem !important; }
  .lessons-title { font-size: 0.85rem !important; padding: 0.2rem 0.6rem !important; margin-bottom: 0.4rem !important; }
  .lessons-list { font-size: 0.9rem !important; margin-left: 1.05rem !important; }

  /* componentes largos */
  .cycle-flow { gap: 0.4rem !important; margin: 0.4rem 0 !important; }
  .cycle-step { padding: 0.45rem !important; flex-basis: 110px !important; }
  .cycle-desc { font-size: 0.78rem !important; }
  .data-table { font-size: 0.84rem !important; }
  .data-table th, .data-table td { padding: 0.3rem 0.4rem !important; }
  .chapter-list .chapter-link { padding: 0.28rem 0.5rem !important; font-size: 0.9rem !important; min-height: 0 !important; }

  /* rodapé fino do PDF — assinatura discreta (QR + CTA), não enchimento */
  .pdf-footer { display: flex; align-items: center; gap: 0.7rem; margin-top: 1.1rem;
                padding-top: 0.7rem; border-top: 2px dashed var(--green);
                break-inside: avoid; page-break-inside: avoid; }
  .pdf-footer-qr { width: 46px; height: 46px; flex: 0 0 auto; border: 1px solid var(--green); border-radius: 4px; }
  .pdf-footer-txt { font-size: 0.8rem; line-height: 1.4; color: var(--gray-dark); }
  .pdf-footer-txt strong { font-family: var(--font-display); color: var(--green-dark); }
  .pdf-footer-cta { color: var(--green-dark); font-weight: 700; }
`;

// Na hora do render: (1) remove a pele psicodélica (o PDF é sempre o padrão
// verde premium; a skin psy é intencional só no site); (2) as Lições deixam de
// ser faixa de largura total e entram no fluxo das colunas.
const REFLOW_JS = `
  document.querySelectorAll('link[href*="psicodelia"]').forEach((l) => l.remove());
  document.body.classList.remove('psy');
  document.querySelectorAll('.grid').forEach((grid) => {
    const scope = grid.parentElement;
    if (!scope) return;
    scope.querySelectorAll(':scope > .lessons, :scope > section.lessons').forEach((l) => grid.appendChild(l));
  });
`;

// --------------------------------------------------- tuning aprendido
// O refinador (local, offline) grava aqui a melhor configuração por livro/tipo
// de página. Ausência do arquivo (ou de uma entrada) = comportamento padrão do
// adaptiveFit. Produção NÃO muda enquanto não houver tuned.json.
const TUNED_FILE = path.join(__dirname, 'refinador', 'tuned.json');
function loadTuned() {
  try { return JSON.parse(fs.readFileSync(TUNED_FILE, 'utf8')); } catch { return {}; }
}
let TUNED = loadTuned();
function pageKind(page) {
  if (page === 'livro-completo') return 'livro-completo';
  if (page === 'visao-geral') return 'visao-geral';
  return 'capitulo';
}
// precedência (mais específico ganha): default global → tipo global →
// default do livro → tipo do livro → página exata.
function tuneFor(book, page) {
  const kind = pageKind(page);
  const gd = TUNED._default || {};
  const bd = TUNED[book] || {};
  return {
    ...(gd._default || {}),
    ...(gd[kind] || {}),
    ...(bd._default || {}),
    ...(bd[kind] || {}),
    ...(bd[page] || {}),
  };
}

function headerTemplate(title, subtitle) {
  const esc = (s) => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;');
  return `
  <div style="width:100%; font-family: Helvetica, Arial, sans-serif; font-size:8px; color:#666;
              padding:0 9mm 4px; display:flex; justify-content:space-between; align-items:flex-end;
              border-bottom:2px solid ${GREEN};">
    <span style="font-weight:bold; letter-spacing:.06em; text-transform:uppercase;">${esc(title)}</span>
    <span style="letter-spacing:.04em;">${esc(subtitle)}</span>
  </div>`;
}

function footerTemplate(author) {
  const esc = (s) => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;');
  const year = new Date().getFullYear();
  return `
  <div style="width:100%; font-family: Helvetica, Arial, sans-serif; font-size:8px; color:#666;
              padding:4px 9mm 0; display:flex; justify-content:space-between; border-top:1px solid #ccc;">
    <span>© ${year} andregalgani.com.br/biblioteca${author ? ' &nbsp;·&nbsp; ' + esc(author) : ''}</span>
    <span>Página <span class="pageNumber"></span> de <span class="totalPages"></span></span>
  </div>`;
}

const PDF_OPTS = {
  format: 'A4',
  printBackground: true,
  displayHeaderFooter: true,
  tagged: true,   // PDF acessível
  outline: true,  // marcadores (sumário) a partir dos títulos
  margin: { top: '15mm', bottom: '13mm', left: '9mm', right: '9mm' },
};

// metadados de infoproduto carimbados no arquivo final
async function stampMetadata(pdfBytes, { title, subtitle, author }) {
  try {
    const doc = await PDFDocument.load(pdfBytes, { updateMetadata: false });
    doc.setTitle(subtitle ? `${title} — ${subtitle}` : title);
    doc.setAuthor(author || 'André Galgani');
    doc.setSubject(`Cheat sheet do livro "${title}" · Biblioteca André Galgani`);
    doc.setKeywords(['cheat sheet', 'resumo', title, author || ''].filter(Boolean));
    doc.setCreator('andregalgani.com.br/biblioteca');
    doc.setProducer('biblioteca-pdf');
    doc.setCreationDate(new Date());
    doc.setModificationDate(new Date());
    return Buffer.from(await doc.save());
  } catch (e) {
    console.error('[meta]', e.message);
    return pdfBytes; // metadado nunca derruba a geração
  }
}

// Ajuste adaptativo v9 — NORTE: cada página = cheia de CONTEÚDO REAL e bonita.
// O preenchimento NÃO usa mais bloco-ficha/QR (virou rodapé fino e fixo). Ordem
// de uma página curta: (1) escala de fonte generosa até ~94% (teto premium);
// (2) "ritmo": distribui o residual como AR entre os cards (respiro elegante),
// nunca como anúncio. Multipágina: mata-viúva. Roda no contexto da página.
function adaptiveFit(cfg) {
  const t = cfg.tune || {};
  const T = t.pageH || 1010; // altura útil aproximada de uma página A4 (px CSS)
  const el = document.querySelector('.page');
  if (!el) return { mode: 'skip' };
  const setFS = (px) => { document.documentElement.style.fontSize = px + 'px'; };
  const H = () => el.offsetHeight;

  // rodapé fino sempre presente (assinatura, não enchimento) — fica por último
  if (cfg.footer) {
    const holder = document.createElement('div');
    holder.innerHTML = cfg.footer;
    if (holder.firstElementChild) el.appendChild(holder.firstElementChild);
  }

  let fs = 11;
  setFS(fs);
  let h = H();

  if (h > T) { // multipágina: evitar última página quase vazia (mata-viúva)
    const pages = Math.ceil(h / T);
    const lastFrac = h / T - (pages - 1);
    if (pages > 1 && lastFrac < (t.widowFrac || 0.30)) {
      const fs2 = Math.max(10, (11 * ((pages - 1) * T)) / h * 0.99);
      setFS(fs2);
      if (H() > (pages - 1) * T) { setFS(11); } else { fs = fs2; }
    }
    h = H();
    return { mode: 'multi', fs: +fs.toFixed(2), pagesEst: Math.ceil(h / T), lastFill: +((h / T) % 1 || 1).toFixed(2) };
  }

  // página única — (1) fonte generosa até o alvo de preenchimento, teto premium
  const cap = t.maxFs || 15.5;
  const target = T * (t.fillTarget || 0.94);
  for (let i = 0; i < 4; i++) {
    fs = Math.min(cap, Math.max(11, (fs * target) / h));
    setFS(fs); h = H();
    if (h > T) { fs *= 0.97; setFS(fs); h = H(); }
    if (h >= T * 0.9 && h <= T) break;
  }
  // garante caber antes do ritmo
  let g = 0;
  while (H() > T && fs > 10 && g++ < 6) { fs *= 0.97; setFS(fs); }
  h = H();

  // (2) ritmo elegante — o residual vira AR entre os cards (não bloco-anúncio):
  // cresce sobretudo a margem entre cards e o espaço do cabeçalho; padding e
  // entrelinha sobem pouco (cap) para não inchar os cards. Tudo tunável.
  let rhythm = 1;
  if ((T - h) / T > 0.05) {
    const padCap = t.padCap || 1.4, lhCap = t.lhCap || 1.16, marginMul = t.marginMul || 1.0;
    const st = document.createElement('style');
    document.head.appendChild(st);
    const apply = (m) => {
      const pad = Math.min(m, padCap), lh = Math.min(m, lhCap);
      st.textContent =
        '.card,.lessons{margin-bottom:' + (marginMul * m).toFixed(2) + 'rem!important;' +
        'padding:' + (0.75 * pad).toFixed(2) + 'rem!important}' +
        '.header{margin-bottom:' + (0.8 * m).toFixed(2) + 'rem!important}' +
        '.header-intro{margin-top:' + (0.25 * m).toFixed(2) + 'rem!important}' +
        '.card-body,.card-tip,.content-list li,.lessons-list li{line-height:' + (1.38 * lh).toFixed(3) + '!important}';
    };
    let r = Math.min(t.rhythmCap || 1.9, (T * (t.rhythmFillTarget || 0.965)) / h);
    while (r > 1.03) { apply(r); h = H(); if (h <= T) break; r -= 0.06; }
    if (H() > T) { st.textContent = ''; h = H(); }
    rhythm = +r.toFixed(2);
  }

  return { mode: 'single', fs: +fs.toFixed(2), fill: +(h / T).toFixed(3), rhythm };
}

async function renderUrlToPdf(url, { title, subtitle, author, footer, maxFs, tune }) {
  const browser = await getBrowser();
  const page = await browser.newPage();
  try {
    await page.emulateMediaFeatures([{ name: 'prefers-color-scheme', value: 'light' }]);
    await page.goto(url, { waitUntil: 'networkidle0', timeout: 60000 });
    await page.emulateMediaType('print');
    await page.addStyleTag({ content: PRINT_CSS });
    await page.evaluate(REFLOW_JS);
    await page.evaluateHandle('document.fonts.ready');
    await page.setViewport({ width: 725, height: 1050 }); // largura útil do A4 p/ medição fiel
    const diag = await page.evaluate(adaptiveFit, {
      footer: footer || '',
      tune: { maxFs: maxFs || 15.5, ...(tune || {}) },
    });
    const buffer = await page.pdf({
      ...PDF_OPTS,
      headerTemplate: headerTemplate(title, subtitle),
      footerTemplate: footerTemplate(author),
    });
    return { buffer, diag };
  } finally {
    await page.close().catch(() => {});
  }
}

async function renderHtmlToPdf(html, opts) {
  const browser = await getBrowser();
  const page = await browser.newPage();
  try {
    await page.emulateMediaFeatures([{ name: 'prefers-color-scheme', value: 'light' }]);
    await page.setContent(html, { waitUntil: 'networkidle0', timeout: 120000 });
    await page.emulateMediaType('print');
    await page.addStyleTag({ content: PRINT_CSS });
    await page.evaluate(REFLOW_JS);
    await page.evaluateHandle('document.fonts.ready');
    return await page.pdf({
      ...PDF_OPTS,
      headerTemplate: headerTemplate(opts.title, opts.subtitle),
      footerTemplate: footerTemplate(opts.author),
    });
  } finally {
    await page.close().catch(() => {});
  }
}

// ------------------------------------------------------- livro completo
async function buildBookHtml(book, baseUrl) {
  const overviewFile = path.join(SITE_ROOT, `${book}.html`);
  const overview = await fsp.readFile(overviewFile, 'utf8');

  // ordem dos capítulos = ordem dos links na visão geral
  const hrefs = [...overview.matchAll(/href="([^"]+\.html)"[^>]*class="chapter-link"/g)]
    .map((m) => m[1])
    .filter((h) => h.startsWith(`${book}/`));

  const sources = [overviewFile];
  const sections = [];

  const grab = (html) => {
    const header = extract(html, /<header class="header[\s\S]*?<\/header>/);
    const main = extract(html, /<main id="conteudo"[\s\S]*?<\/main>/)
      .replace(/<main /, '<div class="pdf-main" ')
      .replace(/<\/main>/, '</div>');
    return header + '\n' + main;
  };

  sections.push(`<section class="pdf-sec">${grab(overview)}</section>`);
  for (const href of hrefs) {
    const file = path.join(SITE_ROOT, href);
    sources.push(file);
    const html = await fsp.readFile(file, 'utf8');
    sections.push(`<section class="pdf-sec">${grab(html)}</section>`);
  }

  const { title, author } = bookMeta(book);
  const cover = `
  <section class="pdf-cover">
    <div class="pdf-cover-frame">
      <p class="pdf-cover-author">${author}</p>
      <h1 class="pdf-cover-title">${title}</h1>
      <div class="pdf-cover-rule"></div>
      <p class="pdf-cover-sub">Cheat sheets do livro · andregalgani.com.br/biblioteca</p>
    </div>
  </section>`;

  const html = `<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<base href="${baseUrl}/">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;500;700;800&family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,600;0,7..72,700;1,7..72,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
<style>
  /* documento transitório de impressão — não faz parte do site */
  .pdf-sec { page-break-before: always; }
  .pdf-cover { page-break-after: always; display: flex; align-items: center; justify-content: center;
               min-height: 240mm; }
  .pdf-cover-frame { border: 3px dashed var(--green); border-radius: 8px; padding: 28mm 16mm;
                     text-align: center; width: 100%; }
  .pdf-cover-author { font-family: var(--font-display); font-weight: 800; letter-spacing: .18em;
                      text-transform: uppercase; color: var(--green-dark); font-size: 1rem; }
  .pdf-cover-title { font-family: var(--font-display); font-weight: 800; text-transform: uppercase;
                     color: var(--green); font-size: 3rem; line-height: 1.05; margin: 1.2rem 0; }
  .pdf-cover-rule { width: 72px; height: 5px; background: var(--green); margin: 0 auto 1.2rem;
                    border-radius: 3px; }
  .pdf-cover-sub { font-family: var(--font-display); font-weight: 700; letter-spacing: .08em;
                   text-transform: uppercase; color: var(--gray-dark); font-size: .8rem; }
</style>
</head>
<body>
<div class="page">
${cover}
${sections.join('\n')}
</div>
</body>
</html>`;

  return { html, sources, title, author };
}

// ---------------------------------------------------------------- app
const app = express();
app.set('trust proxy', 'loopback'); // IP real via X-Forwarded-For do nginx
app.use(express.json());
app.use('/site', express.static(SITE_ROOT));      // legado (testes antigos)
app.use('/biblioteca', express.static(SITE_ROOT)); // espelho fiel da produção
app.get('/health', (_req, res) => res.json({ ok: true, version: VERSION, paywall: PAYWALL }));

const pdf = express.Router();
app.use('/pdf', pdf);            // produção (nginx faz proxy de /biblioteca/pdf/ → /pdf/)
app.use('/biblioteca/pdf', pdf); // espelho local sem nginx

// login/usuários (mesmas montagens do pdf → /pdf/auth/* e /biblioteca/pdf/auth/*)
const auth = makeAuth(SECRET);
app.use('/pdf', auth.router);
app.use('/biblioteca/pdf', auth.router);

// ------------------------------------------------------------- estatísticas
// beacon de visita (sendBeacon do script.js): ?book=<slug> ou ?book=_estante
pdf.post('/hit', (req, res) => {
  const book = String(req.query.book || '');
  if (book !== '_estante' && !SLUG_RE.test(book)) return res.status(400).end();
  countHit(req, book);
  res.status(204).end();
});
pdf.get('/stats.json', (_req, res) => res.json(statsSummary()));
pdf.get('/stats', (_req, res) => res.type('html').send(statsPage(statsSummary())));

// votos: joinha/desjoinha por livro — ranking global da estante
pdf.get('/votes', (_req, res) => res.json(VOTES));
pdf.post('/vote', (req, res) => {
  const q = req.query || {};
  const book = String(q.book || '');
  const from = String(q.from || 'none');
  const to = String(q.to || 'none');
  const ok = v => v === 'up' || v === 'down' || v === 'none';
  if (!SLUG_RE.test(book) || !ok(from) || !ok(to)) return res.status(400).json({ error: 'parâmetros inválidos' });
  if (BOT_RE.test(req.headers['user-agent'] || '')) return res.json(getVotes(book));
  res.json(applyVote(book, from, to));
});

// ----- Kit de Divulgação: assets de redes on-demand (gera-ou-serve-cache) -----
// Cada formato = um template HTML servido estaticamente, renderizado pelo mesmo
// Chrome dos PDFs e cacheado em disco. 1º pedido gera; os próximos servem o
// cache. 'capa'/'og' já são estáticos (gerados antes) — só servidos.
const KIT_TPL = {
  'citacao-feed':  { tpl: 'quote.html',       w: 1080, h: 1350 },
  'citacao-story': { tpl: 'quote-story.html', w: 1080, h: 1920 },
  'ideia':         { tpl: 'ideia.html',       w: 1080, h: 1080 },
  'capa-story':    { tpl: 'capa-story.html',  w: 1080, h: 1920 },
  'mapa':          { tpl: 'mapa.html',        w: 1080, h: 1350 },
  'thumb':         { tpl: 'thumb.html',       w: 1280, h: 720  },
};

// Auto-fit das peças do Kit. ESPELHA gerar_dados_kit._FIT_JS (o fit do caminho
// --proof, em Playwright) — mantenha os dois em sincronia: a produção tem de bater
// com a prova. Encolhe título que estoura a largura (.head h1/.ed-title/.thumb h1)
// e o corpo .fitv (ex.: o mapa) que estoura a altura. Não toca no que já cabe.
//
// ATENÇÃO: o Puppeteer (≠ Playwright) NÃO invoca uma string em forma de função —
// só AVALIA a expressão. Por isso o call site embrulha isto num IIFE; sem o IIFE a
// função só seria criada e o fit nunca rodaria (era o motivo de não estar aplicando).
const KIT_FIT = `() => {
  for (const el of document.querySelectorAll('.head h1, .ed-title, .thumb h1')) {
    const box = el.parentElement, cs = getComputedStyle(box);
    const avail = box.clientWidth - parseFloat(cs.paddingLeft) - parseFloat(cs.paddingRight);
    let fs = parseFloat(getComputedStyle(el).fontSize), g = 0;
    while (el.scrollWidth > avail && fs > 40 && g < 120){ fs -= 3; el.style.fontSize = fs+'px'; g++; }
  }
  for (const el of document.querySelectorAll('.fitv')) {
    let fs = parseFloat(getComputedStyle(el).fontSize), g = 0;
    while (el.scrollHeight > el.clientHeight + 1 && fs > 24 && g < 60){ fs -= 1; el.style.fontSize = fs+'px'; g++; }
  }
}`;
const KIT_STATIC = { 'capa': (b) => `${b}-capa.png`, 'og': (b) => `${b}-og.png` };

async function renderKitAsset(book, fmt, ext = 'png') {
  const spec = KIT_TPL[fmt];
  const type = ext === 'jpg' ? 'jpeg' : 'png';  // IG exige JPEG; PNG p/ download
  const tplFile = path.join(SITE_ROOT, 'assets', 'kit', '_tpl', book, spec.tpl);
  const st = await fsp.stat(tplFile);
  const hash = crypto.createHash('sha1')
    .update(`kit|v${VERSION}|${book}|${fmt}|${st.mtimeMs}|${st.size}`).digest('hex').slice(0, 16);
  const cacheFile = path.join(CACHE_DIR, `kit-${book}-${fmt}-${hash}.${ext}`);
  try { return { buffer: await fsp.readFile(cacheFile), cached: true }; } catch {}
  const url = `http://127.0.0.1:${PORT}/biblioteca/assets/kit/_tpl/${book}/${spec.tpl}`;
  const browser = await getBrowser();
  const page = await browser.newPage();
  try {
    await page.setViewport({ width: spec.w, height: spec.h, deviceScaleFactor: 2 });
    await page.goto(url, { waitUntil: 'networkidle0', timeout: 60000 });
    await page.evaluateHandle('document.fonts.ready');
    await page.evaluate(`(${KIT_FIT})()`);  // IIFE: Puppeteer avalia a string, não invoca a função (ver KIT_FIT)
    const el = await page.$('.slide, .story, .thumb');
    const shot = type === 'jpeg' ? { type: 'jpeg', quality: 90 } : { type: 'png' };
    const buffer = await (el || page).screenshot(shot);
    fsp.writeFile(cacheFile, buffer).catch(() => {});
    return { buffer, cached: false };
  } finally { await page.close().catch(() => {}); }
}

pdf.get('/asset/:book/:fmt.png', async (req, res) => {
  const book = String(req.params.book);
  const fmt = String(req.params.fmt);
  if (!SLUG_RE.test(book)) return res.status(400).send('inválido');
  try {
    if (KIT_TPL[fmt]) {
      const { buffer, cached } = await enqueue(() => renderKitAsset(book, fmt));
      res.setHeader('Content-Type', 'image/png');
      res.setHeader('X-Kit-Cache', cached ? 'hit' : 'miss');
      res.setHeader('Cache-Control', 'public, max-age=300');
      return res.end(buffer);
    }
    if (KIT_STATIC[fmt]) {
      const f = path.join(SITE_ROOT, 'assets', KIT_STATIC[fmt](book));
      await fsp.access(f);
      res.setHeader('X-Kit-Cache', 'static');
      return res.sendFile(f);
    }
    return res.status(404).send('formato desconhecido');
  } catch (err) {
    if (err.code === 'ENOENT') return res.status(404).send('não encontrado');
    console.error('[kit-asset]', err.message);
    res.status(500).send('erro ao gerar asset');
  }
});

// variante JPEG (Instagram exige JPEG p/ image/story; só os formatos de template)
pdf.get('/asset/:book/:fmt.jpg', async (req, res) => {
  const book = String(req.params.book);
  const fmt = String(req.params.fmt);
  if (!SLUG_RE.test(book)) return res.status(400).send('inválido');
  if (!KIT_TPL[fmt]) return res.status(404).send('formato sem jpg');
  try {
    const { buffer, cached } = await enqueue(() => renderKitAsset(book, fmt, 'jpg'));
    res.setHeader('Content-Type', 'image/jpeg');
    res.setHeader('X-Kit-Cache', cached ? 'hit' : 'miss');
    res.setHeader('Cache-Control', 'public, max-age=300');
    return res.end(buffer);
  } catch (err) {
    if (err.code === 'ENOENT') return res.status(404).send('não encontrado');
    console.error('[kit-asset-jpg]', err.message);
    res.status(500).send('erro ao gerar asset');
  }
});

// ----- Kit de Divulgação: CARROSSEL por capítulo, on-demand (gera no 1º clique) -----
// O conteúdo dos slides (HTML) é emitido localmente por gerar_dados_carrossel.py
// (mesmos construtores do gerar_carrossel → zero deriva) em assets/kit/<livro>/slides.json.
// Aqui montamos CSS + slides, renderizamos no mesmo Chrome dos PDFs (png + webp),
// armazenamos em assets/kit/<livro>/caps/<cap>/ e devolvemos o manifesto. Idempotente.
const CRC_TABLE = (() => {
  const t = new Array(256);
  for (let n = 0; n < 256; n++) {
    let c = n;
    for (let k = 0; k < 8; k++) c = (c & 1) ? (0xEDB88320 ^ (c >>> 1)) : (c >>> 1);
    t[n] = c >>> 0;
  }
  return t;
})();
function crc32(buf) {
  let c = 0xFFFFFFFF;
  for (let i = 0; i < buf.length; i++) c = CRC_TABLE[(c ^ buf[i]) & 0xFF] ^ (c >>> 8);
  return (c ^ 0xFFFFFFFF) >>> 0;
}
function zipStore(entries) {
  // ZIP método "store" (sem compressão) — PNG já é comprimido. Sem dependências.
  const locals = [], central = [];
  let offset = 0;
  for (const e of entries) {
    const name = Buffer.from(e.name, 'utf8');
    const crc = crc32(e.data);
    const lh = Buffer.alloc(30);
    lh.writeUInt32LE(0x04034b50, 0); lh.writeUInt16LE(20, 4); lh.writeUInt16LE(0, 6);
    lh.writeUInt16LE(0, 8); lh.writeUInt16LE(0, 10); lh.writeUInt16LE(0, 12);
    lh.writeUInt32LE(crc, 14); lh.writeUInt32LE(e.data.length, 18); lh.writeUInt32LE(e.data.length, 22);
    lh.writeUInt16LE(name.length, 26); lh.writeUInt16LE(0, 28);
    locals.push(lh, name, e.data);
    const ch = Buffer.alloc(46);
    ch.writeUInt32LE(0x02014b50, 0); ch.writeUInt16LE(20, 4); ch.writeUInt16LE(20, 6); ch.writeUInt16LE(0, 8);
    ch.writeUInt16LE(0, 10); ch.writeUInt16LE(0, 12); ch.writeUInt16LE(0, 14);
    ch.writeUInt32LE(crc, 16); ch.writeUInt32LE(e.data.length, 20); ch.writeUInt32LE(e.data.length, 24);
    ch.writeUInt16LE(name.length, 28); ch.writeUInt16LE(0, 30); ch.writeUInt16LE(0, 32);
    ch.writeUInt16LE(0, 34); ch.writeUInt16LE(0, 36); ch.writeUInt32LE(0, 38); ch.writeUInt32LE(offset, 42);
    central.push(ch, name);
    offset += lh.length + name.length + e.data.length;
  }
  const cdStart = offset;
  const cdSize = central.reduce((s, b) => s + b.length, 0);
  const eocd = Buffer.alloc(22);
  eocd.writeUInt32LE(0x06054b50, 0); eocd.writeUInt16LE(0, 4); eocd.writeUInt16LE(0, 6);
  eocd.writeUInt16LE(entries.length, 8); eocd.writeUInt16LE(entries.length, 10);
  eocd.writeUInt32LE(cdSize, 12); eocd.writeUInt32LE(cdStart, 16); eocd.writeUInt16LE(0, 20);
  return Buffer.concat([...locals, ...central, eocd]);
}
const CAROUSEL_SHRINK = `() => {
  for (const el of document.querySelectorAll('.cover h1, .st h1')) {
    const box = el.parentElement, cs = getComputedStyle(box);
    const avail = box.clientWidth - parseFloat(cs.paddingLeft) - parseFloat(cs.paddingRight);
    let fs = parseFloat(getComputedStyle(el).fontSize), guard = 0;
    while (el.getBoundingClientRect().width > avail && fs > 50 && guard < 120) { fs -= 3; el.style.fontSize = fs + 'px'; guard++; }
  }
  const SHRINK = '.ed-title,.ed-body,.ed-tip .tipbody,.phrase,.cta .big,.cta .row p,.cta .save,.card-title,.card-body,.card-tip';
  for (const slide of document.querySelectorAll('.slide, .story')) {
    const padB = parseFloat(getComputedStyle(slide).paddingBottom) || 110;
    const safe = slide.getBoundingClientRect().bottom - Math.max(padB, 40);
    const maxBottom = () => {
      let m = 0;
      for (const el of slide.querySelectorAll(SHRINK)) { const r = el.getBoundingClientRect(); if (r.height > 0) m = Math.max(m, r.bottom); }
      return m;
    };
    let g = 0;
    while (maxBottom() > safe && g < 300) {
      let changed = false;
      for (const el of slide.querySelectorAll(SHRINK)) {
        const fs = parseFloat(getComputedStyle(el).fontSize);
        if (fs > 22) { el.style.fontSize = (fs - 1) + 'px'; changed = true; }
      }
      if (!changed) break;
      g++;
    }
  }
}`;
async function renderCarousel(book, cap) {
  const outDir = path.join(SITE_ROOT, 'assets', 'kit', book, 'caps', cap);
  const mfPath = path.join(outDir, 'manifest.json');
  try { return { manifest: JSON.parse(await fsp.readFile(mfPath, 'utf8')), cached: true }; } catch {}
  const slidesFile = path.join(SITE_ROOT, 'assets', 'kit', book, 'slides.json');
  const data = JSON.parse(await fsp.readFile(slidesFile, 'utf8'));
  const slidesHtml = (data.chapters || {})[cap];
  if (!Array.isArray(slidesHtml) || !slidesHtml.length) { const e = new Error('cap'); e.code = 'ENOENT'; throw e; }
  const css = await fsp.readFile(path.join(SITE_ROOT, 'assets', 'kit', '_carousel.css'), 'utf8');
  const html = `<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>${css}</style></head><body>${slidesHtml.join('')}</body></html>`;
  await fsp.mkdir(outDir, { recursive: true });
  const browser = await getBrowser();
  const page = await browser.newPage();
  const pngEntries = [];
  const slides = [], view = [];
  try {
    await page.setViewport({ width: 1080, height: 1350, deviceScaleFactor: 2 });
    await page.setContent(html, { waitUntil: 'networkidle0', timeout: 60000 });
    await page.evaluateHandle('document.fonts.ready');
    await new Promise(r => setTimeout(r, 500));
    await page.evaluate(`(${CAROUSEL_SHRINK})()`);  // IIFE: Puppeteer avalia a string, nao invoca a funcao (igual KIT_FIT)
    const els = await page.$$('.slide');
    for (let i = 0; i < els.length; i++) {
      const n = String(i + 1).padStart(2, '0');
      const png = await els[i].screenshot({ type: 'png' });
      const webp = await els[i].screenshot({ type: 'webp', quality: 72 });
      const jpg = await els[i].screenshot({ type: 'jpeg', quality: 90 }); // p/ Instagram
      await fsp.writeFile(path.join(outDir, n + '.png'), png);
      await fsp.writeFile(path.join(outDir, n + '.webp'), webp);
      await fsp.writeFile(path.join(outDir, n + '.jpg'), jpg);
      pngEntries.push({ name: `${book}-${cap}-${n}.png`, data: png });
      slides.push(`assets/kit/${book}/caps/${cap}/${n}.png`);
      view.push(`assets/kit/${book}/caps/${cap}/${n}.webp`);
    }
  } finally { await page.close().catch(() => {}); }
  await fsp.writeFile(path.join(outDir, 'carrossel.zip'), zipStore(pngEntries));
  const manifest = { book, chapter: cap, count: slides.length, slides, view, zip: `assets/kit/${book}/caps/${cap}/carrossel.zip` };
  await fsp.writeFile(mfPath, JSON.stringify(manifest, null, 2));
  return { manifest, cached: false };
}
pdf.get('/carrossel/:book/:cap.json', async (req, res) => {
  const book = String(req.params.book), cap = String(req.params.cap);
  if (!SLUG_RE.test(book) || !SLUG_RE.test(cap)) return res.status(400).json({ error: 'inválido' });
  try {
    const { manifest, cached } = await enqueue(() => renderCarousel(book, cap));
    res.setHeader('X-Kit-Cache', cached ? 'hit' : 'miss');
    res.setHeader('Cache-Control', 'public, max-age=60');
    return res.json(manifest);
  } catch (err) {
    if (err.code === 'ENOENT') return res.status(404).json({ error: 'capítulo sem carrossel' });
    console.error('[kit-carrossel]', err.message);
    res.status(500).json({ error: 'erro ao gerar carrossel' });
  }
});

// ----- ADMIN: disparo de publicação no Instagram (a partir da VPS) -----
// Protegido por requireAdmin. IG_DRYRUN=1 monta o contêiner mas NÃO publica.
pdf.get('/admin/instagram/options', auth.requireAdmin, (req, res) => {
  const book = String(req.query.book || '');
  if (!SLUG_RE.test(book)) return res.status(400).json({ error: 'inválido' });
  try {
    const o = publishAssets.optionsFor(book);
    // adapta {types, options:{tipo:[...]}} → [{type, selectors:[...]}] (forma da UI)
    const options = o.types.map((t) => ({ type: t, selectors: o.options[t] }));
    res.json({ book, options, captionPreview: o.captionPreview });
  } catch (err) {
    res.status(404).json({ error: err.message });
  }
});

// cota diária de publicação do IG (p/ a UI avisar "restam X posts hoje")
pdf.get('/admin/instagram/limit', auth.requireAdmin, async (req, res) => {
  try {
    res.json(await instagram.publishingLimit());
  } catch (err) {
    // falha ao consultar não deve travar a UI — devolve nulos (fail-open)
    res.json({ used: null, total: null, remaining: null, error: err.message });
  }
});

pdf.post('/admin/instagram/publish', auth.requireAdmin, async (req, res) => {
  const { book, type, selector, caption, confirm } = req.body || {};
  if (!SLUG_RE.test(String(book || ''))) return res.status(400).json({ error: 'livro inválido' });
  if (!confirm) return res.status(400).json({ error: 'confirmação ausente' });
  const dryRun = String(process.env.IG_DRYRUN || '') === '1';
  try {
    let media, cap;
    if (type === 'carrossel') {
      // gera os slides (png+webp+jpg) e monta as URLs JPEG públicas do manifesto
      const { manifest } = await enqueue(() => renderCarousel(book, String(selector)));
      media = manifest.slides.map((s) => `${publishAssets.PUB}/biblioteca/${s.replace(/\.png$/, '.jpg')}`);
      cap = caption !== undefined ? caption : publishAssets.captionFor(book);
    } else {
      const r = publishAssets.resolve(book, type, selector); // valida selector
      media = r.media;
      cap = caption !== undefined ? caption : r.caption;
      // pré-aquece o JPEG p/ o IG buscar sem timeout (feed/story)
      if (type === 'feed' || type === 'story') {
        await enqueue(() => renderKitAsset(book, String(selector), 'jpg'));
      }
    }
    let result;
    if (type === 'feed') result = await instagram.publishImage(media[0], cap, { dryRun });
    else if (type === 'story') result = await instagram.publishStory(media[0], { dryRun });
    else if (type === 'carrossel') result = await instagram.publishCarousel(media, cap, { dryRun });
    else if (type === 'reels') result = await instagram.publishReel(media[0], cap, { dryRun });
    else return res.status(400).json({ error: 'tipo inválido' });
    res.json({ ok: true, dryRun, mediaId: result.id || result.containerId, permalink: result.permalink || null });
  } catch (err) {
    console.error('[ig-publish]', err.message);
    res.status(500).json({ error: err.message });
  }
});

// ----- refinador (DEV, só com REFINADOR=1): render fresco, sem cache, com -----
// um `tune` ad-hoc. Devolve o PDF cru + o diagnóstico do fit no header X-Fit-Diag.
// Em produção o env não está setado, então estas rotas nem existem.
if (process.env.REFINADOR === '1') {
  pdf.get('/_refinar/:book/:page', async (req, res) => {
    const { book, page } = req.params;
    if (!SLUG_RE.test(book) || !SLUG_RE.test(page)) return res.status(400).send('inválido');
    let tune = {};
    try { if (req.query.tune) tune = JSON.parse(req.query.tune); } catch {}
    try {
      const meta = bookMeta(book);
      let out;
      if (page === 'livro-completo') {
        const built = await buildBookHtml(book, `http://127.0.0.1:${PORT}/site`);
        const buffer = await enqueue(() => renderHtmlToPdf(built.html,
          { title: meta.title, subtitle: 'Resumo completo', author: meta.author }));
        out = { buffer, diag: { mode: 'book' } };
      } else {
        const isOverview = page === 'visao-geral';
        const file = isOverview ? path.join(SITE_ROOT, `${book}.html`)
                                : path.join(SITE_ROOT, book, `${page}.html`);
        await fsp.access(file);
        const url = isOverview ? `http://127.0.0.1:${PORT}/site/${book}.html`
                               : `http://127.0.0.1:${PORT}/site/${book}/${page}.html`;
        const html = await fsp.readFile(file, 'utf8');
        const subtitle = textOf(html, /<p class="header-subtitle">([\s\S]*?)<\/p>/)
                         || (isOverview ? 'Visão geral' : page);
        const footer = await buildFooter(book);
        out = await enqueue(() => renderUrlToPdf(url,
          { title: meta.title, subtitle, author: meta.author, footer, maxFs: tune.maxFs || 15.5, tune }));
      }
      res.setHeader('X-Fit-Diag', JSON.stringify(out.diag || {}));
      res.setHeader('Content-Type', 'application/pdf');
      res.end(out.buffer);
    } catch (err) {
      if (err.code === 'ENOENT') return res.status(404).send('não encontrada');
      console.error('[refinar]', err.message);
      res.status(500).send('erro');
    }
  });
  // recarrega o tuned.json em memória (o refinador chama após gravar)
  pdf.post('/_reload-tuned', (_req, res) => {
    TUNED = loadTuned();
    res.json({ ok: true, livros: Object.keys(TUNED) });
  });
  console.log('[refinador] rotas DEV ativas: GET /pdf/_refinar/:book/:page  ·  POST /pdf/_reload-tuned');
}

// ----- paywall: dados do Pix, QR e emissão de token -----
pdf.get('/pix-info', (_req, res) => {
  res.json({ code: PIX_CODE, amount: PIX_AMOUNT, ttlMin: TOKEN_TTL_MS / 60000 });
});

let qrCache = null;
pdf.get('/pix-qr.png', async (_req, res) => {
  try {
    if (!qrCache) {
      qrCache = await QRCode.toBuffer(PIX_CODE, { width: 480, margin: 2, errorCorrectionLevel: 'M' });
    }
    res.setHeader('Content-Type', 'image/png');
    res.setHeader('Cache-Control', 'public, max-age=86400');
    res.end(qrCache);
  } catch (e) {
    console.error('[qr]', e.message);
    res.status(500).send('erro ao gerar QR');
  }
});

pdf.post('/token', (req, res) => {
  const { book, page } = req.body || {};
  if (!SLUG_RE.test(String(book)) || !SLUG_RE.test(String(page))) {
    return res.status(400).json({ error: 'parâmetros inválidos' });
  }
  // Emissão por confiança (Pix estático não tem confirmação automática).
  // Com PSP + webhook, esta emissão passa a acontecer só após o pagamento.
  console.log(`[token] ${book}/${page} ip=${req.headers['x-real-ip'] || req.ip}`);
  res.json({ t: makeToken(book, page) });
});

const GATE_HTML = (back) => `<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">
<title>Download protegido · Biblioteca</title></head>
<body style="font-family:sans-serif;max-width:560px;margin:4rem auto;text-align:center;line-height:1.6">
<h1 style="color:#0f7a4d">Download protegido</h1>
<p>Este PDF é liberado na página do capítulo, pelo botão <strong>Baixar em PDF</strong> (contribuição via Pix).</p>
<p><a href="${back}" style="color:#0f7a4d;font-weight:bold">Ir para a página do livro →</a></p>
</body></html>`;

pdf.get('/:book/:page.pdf', async (req, res) => {
  const { book, page } = req.params;
  if (!SLUG_RE.test(book) || !SLUG_RE.test(page)) return res.status(400).send('parâmetros inválidos');

  if (PAYWALL && !checkToken(book, page, req.query.t)) {
    return res.status(403).type('html').send(GATE_HTML(`/biblioteca/${book}.html`));
  }

  try {
    const meta = bookMeta(book);
    let sources, make, makeSafe;

    if (page === 'livro-completo') {
      const overviewFile = path.join(SITE_ROOT, `${book}.html`);
      await fsp.access(overviewFile);
      make = async () => {
        const built = await buildBookHtml(book, `http://127.0.0.1:${PORT}/site`);
        const buffer = await renderHtmlToPdf(built.html, { title: meta.title, subtitle: 'Resumo completo', author: meta.author });
        return { buffer, diag: { mode: 'book' } };
      };
      const built = await buildBookHtml(book, `http://127.0.0.1:${PORT}/site`);
      sources = built.sources;
    } else {
      const isOverview = page === 'visao-geral';
      const file = isOverview ? path.join(SITE_ROOT, `${book}.html`) : path.join(SITE_ROOT, book, `${page}.html`);
      await fsp.access(file);
      sources = [file];
      const url = isOverview
        ? `http://127.0.0.1:${PORT}/site/${book}.html`
        : `http://127.0.0.1:${PORT}/site/${book}/${page}.html`;
      const html = await fsp.readFile(file, 'utf8');
      const subtitle = textOf(html, /<p class="header-subtitle">([\s\S]*?)<\/p>/) || (isOverview ? 'Visão geral' : page);
      const footer = await buildFooter(book);
      const base = { title: meta.title, subtitle, author: meta.author };
      const tune = tuneFor(book, page);
      make = () => renderUrlToPdf(url, { ...base, footer, maxFs: 15.5, tune });
      // fallback conservador: densidade padrão (garante 1 página quando o fit vazar)
      makeSafe = () => renderUrlToPdf(url, { ...base, footer, maxFs: 11 });
    }

    const key = await cacheKey(book, page, sources);
    const cached = path.join(CACHE_DIR, key);

    if (!fs.existsSync(cached)) {
      let { buffer: raw, diag } = await enqueue(make);
      if (diag && diag.mode === 'single' && makeSafe) {
        // trava: se o ajuste fino vazou para uma 2ª página, re-renderiza conservador
        diag.pages = (await PDFDocument.load(raw)).getPageCount();
        if (diag.pages > 1) {
          ({ buffer: raw, diag } = await enqueue(makeSafe));
          diag = { ...diag, retried: true, pages: (await PDFDocument.load(raw)).getPageCount() };
        }
      }
      console.log(`[fit] ${book}/${page} ${JSON.stringify(diag || {})}`);
      const pageHtml = page === 'livro-completo' ? '' : await fsp.readFile(sources[0], 'utf8');
      const subtitle = page === 'livro-completo'
        ? 'Resumo completo'
        : textOf(pageHtml, /<p class="header-subtitle">([\s\S]*?)<\/p>/) || page;
      const pdf = await stampMetadata(raw, { title: meta.title, subtitle, author: meta.author });
      await fsp.writeFile(cached, pdf);
      cleanStale(book, page, key);
    }

    countDownload(req, book, page);
    res.setHeader('Content-Type', 'application/pdf');
    res.setHeader('Content-Disposition', `inline; filename="${book}-${page}.pdf"`);
    res.setHeader('Cache-Control', 'public, max-age=300');
    fs.createReadStream(cached).pipe(res);
  } catch (err) {
    if (err.code === 'ENOENT') return res.status(404).send('página não encontrada');
    console.error(`[pdf] ${book}/${page}:`, err.message);
    res.status(500).send('erro ao gerar o PDF');
  }
});

app.listen(PORT, '127.0.0.1', () => {
  console.log(`biblioteca-pdf na porta ${PORT} · site: ${SITE_ROOT} · chrome: ${CHROME}`);
});
