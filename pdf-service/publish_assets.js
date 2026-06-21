'use strict';
// publish_assets.js — mapeia um pedido de publicação (Instagram) para URLs de
// mídia + monta a legenda premium pt-BR. Porta a lógica de legenda do
// videos/instagram_post.py (caption_carousel / caption_for / _afiliado_block /
// _pergunta_ancora / HASHTAGS_BASE) para o serviço Node (CommonJS).
//
// As peças do kit são geradas/hospedadas na VPS e ficam públicas sob
// https://andregalgani.com.br/biblioteca/... — aqui só CONSTRUÍMOS as URLs;
// o integrador é quem produz os arquivos (e os .jpg) nos endpoints de asset.

const fs = require('fs');
const path = require('path');

// Raiz do site — MESMO fallback do server.js (SITE_ROOT || prod). Em dev,
// rode com SITE_ROOT apontando p/ o projeto. books.json, assets/kit e
// assets/reels moram aqui.
const ROOT = process.env.SITE_ROOT || '/var/www/andregalgani/biblioteca';
const BOOKS_JSON = path.join(ROOT, 'books.json');
const KIT_DIR = path.join(ROOT, 'assets', 'kit');
// reels: assets/reels/<book>/ (público em /biblioteca/assets/reels/<book>/)
const REELS_DIR = path.join(ROOT, 'assets', 'reels');

const PUB = 'https://andregalgani.com.br';

// IG premia 3–5 hashtags de nicho (não 30) — doutrina de distribuicao.md
const HASHTAGS_BASE = ['livros', 'resumodelivro', 'leitura'];
// Disclosure obrigatória de afiliado (canal é Associado Amazon, tag andregalgani-20).
const DISCLOSURE = 'Como Associado da Amazon, ganho com compras qualificadas.';

// Conjuntos permitidos de selector por tipo.
const FEED_SELECTORS = ['ideia', 'citacao-feed', 'mapa'];
const STORY_SELECTORS = ['capa-story', 'citacao-story', 'insights-story'];

// ---------------------------------------------------------------------------
// books.json
// ---------------------------------------------------------------------------
function _books() {
  // Lê sem cache para refletir edições no disco (o serviço é de longa duração).
  return JSON.parse(fs.readFileSync(BOOKS_JSON, 'utf8'));
}

function _book(bookId) {
  const book = _books().find((b) => b.id === bookId);
  if (!book) throw new Error(`Livro não encontrado em books.json: "${bookId}"`);
  return book;
}

// ---------------------------------------------------------------------------
// Helpers de legenda (porta do instagram_post.py)
// ---------------------------------------------------------------------------

// Quebra um texto em frases limpas (p/ gancho + 1 linha de valor).
function _frases(texto) {
  return String(texto || '')
    .trim()
    .split(/(?<=[.?!])\s+/)
    .map((s) => s.trim())
    .filter(Boolean);
}

// Pergunta âncora específica e polarizante no final da legenda — leva o leitor a
// comentar (3º sinal de ranking do algoritmo). Roteia por tags; fallback acionável.
function _perguntaAncora(titulo, tags) {
  const ts = (tags || []).map((t) => String(t).toLowerCase());
  const tem = (...palavras) => ts.some((t) => palavras.some((p) => t.includes(p)));
  if (tem('dinheiro', 'financ', 'investimento', 'riqueza', 'capital', 'econom'))
    return 'Qual hábito financeiro deste livro você aplicaria primeiro?';
  if (tem('hábito', 'habit', 'produtividade', 'rotina', 'disciplina'))
    return 'Qual hábito deste livro você tenta mas não consegue manter?';
  if (tem('comunicação', 'persuasão', 'negociação', 'conversa', 'relacionamento'))
    return 'Qual dessas técnicas você vai testar hoje?';
  if (tem('liderança', 'negócio', 'estratégia', 'poder', 'gestão'))
    return 'Qual decisão na sua vida mudaria se você aplicasse isso?';
  if (tem('psicologia', 'mente', 'filosofia', 'comportamento', 'consciência'))
    return 'Qual ideia aqui mais te incomodou — ou mais fez sentido?';
  if (tem('ficção', 'romance', 'literatura', 'narrativa', 'roteiro'))
    return 'Qual personagem ou cena ficou mais na sua cabeça?';
  return `Qual ideia de "${titulo}" você colocaria em prática esta semana?`;
}

// Rodapé das legendas do IG: o IG NÃO torna URL clicável na legenda (só bio e
// Stories), então NÃO colocamos link aqui — só a disclosure. O produto/afiliado
// mora no acervo, alcançado pelo "link na bio".
function _afiliadoBlock() {
  return DISCLOSURE;
}

// Normaliza uma tag em hashtag (só [0-9a-z], sem espaços/acentos).
function _slugTag(t) {
  return String(t)
    .toLowerCase()
    .normalize('NFD')
    .replace(/[̀-ͯ]/g, '') // remove acentos
    .replace(/\s+/g, '')
    .replace(/[^0-9a-z]/g, '');
}

// ---------------------------------------------------------------------------
// captionFor — legenda premium pt-BR a partir de books.json
// ---------------------------------------------------------------------------
// Espelha caption_carousel: gancho (1ª frase da description) + linha de valor +
// "Arrasta para o lado…" + "📌 Salve…" + CTA acervo + YouTube + seguir +
// pergunta âncora + disclosure de afiliado + 3–5 hashtags de nicho das tags.
function captionFor(bookId) {
  const book = _book(bookId);
  const frases = _frases(book.description || '');
  const gancho = frases[0] || book.title;
  const valor = frases.length > 1 && frases[1].length <= 140 ? frases[1] : '';
  const corpo = gancho + (valor ? `\n\n${valor}` : '');

  const tags = (book.tags || []).slice(0, 2).map(_slugTag).filter(Boolean);
  const hs = HASHTAGS_BASE.concat(tags)
    .map((t) => '#' + t)
    .join(' ');
  const ancora = _perguntaAncora(book.title, book.tags || []);

  return (
    `${corpo}\n\n` +
    `Arrasta para o lado: as ideias de "${book.title}", de ${book.author}.\n` +
    `📌 Salve para não perder.\n\n` +
    `📄 O livro em 1 página: cheat sheet + PDF no acervo — link na bio.\n` +
    `🎬 Resumo em vídeo (~5 min) no YouTube.\n\n` +
    `Siga @minutoreal1701 — um grande livro por semana.\n\n` +
    `${ancora}\n\n` +
    `${_afiliadoBlock()}\nNarração e arte por IA.\n\n${hs}`
  );
}

// ---------------------------------------------------------------------------
// Construtores de mídia
// ---------------------------------------------------------------------------

// Carrossel: slides 1..count em /biblioteca/assets/kit/<book>/caps/<cap>/<n>.jpg
// (count é fornecido pelo chamador após a geração dos slides).
function mediaForCarousel(book, cap, count) {
  const n = Number(count);
  if (!Number.isInteger(n) || n < 1) {
    throw new Error(`count inválido para carrossel (${book}/${cap}): ${count}`);
  }
  const media = [];
  for (let i = 1; i <= n; i++) {
    media.push(`${PUB}/biblioteca/assets/kit/${book}/caps/${cap}/${i}.jpg`);
  }
  return media;
}

// ---------------------------------------------------------------------------
// resolve — mapeia (book, type, selector) -> { kind, media, caption }
// ---------------------------------------------------------------------------
function resolve(bookId, type, selector) {
  switch (type) {
    case 'feed': {
      if (!FEED_SELECTORS.includes(selector)) {
        throw new Error(
          `selector inválido para feed: "${selector}" (use ${FEED_SELECTORS.join(', ')})`
        );
      }
      return {
        kind: 'feed',
        media: [`${PUB}/biblioteca/pdf/asset/${bookId}/${selector}.jpg`],
        caption: captionFor(bookId),
      };
    }
    case 'story': {
      if (!STORY_SELECTORS.includes(selector)) {
        throw new Error(
          `selector inválido para story: "${selector}" (use ${STORY_SELECTORS.join(', ')})`
        );
      }
      // Story não leva legenda.
      return {
        kind: 'story',
        media: [`${PUB}/biblioteca/pdf/asset/${bookId}/${selector}.jpg`],
        caption: '',
      };
    }
    case 'carrossel': {
      // selector = 'overview' ou um slug de capítulo. As URLs dos slides são
      // construídas por mediaForCarousel(book, cap, count) — count vem do
      // chamador após a geração. Aqui só validamos o selector.
      const caps = _capsChapters(bookId); // { overview: N, <slug>: N, ... } ou null
      if (caps) {
        if (!Object.prototype.hasOwnProperty.call(caps, selector)) {
          throw new Error(
            `selector de carrossel inválido para "${bookId}": "${selector}" ` +
              `(use ${Object.keys(caps).join(', ')})`
          );
        }
      } else if (selector !== 'overview') {
        // Sem caps.json: só 'overview' é garantido.
        throw new Error(
          `selector de carrossel inválido para "${bookId}": "${selector}" ` +
            `(sem caps.json; use "overview")`
        );
      }
      const count = caps ? caps[selector] : undefined;
      return {
        kind: 'carrossel',
        // Se soubermos o count (de caps.json), já entregamos as URLs prontas;
        // senão, mídia vazia e o chamador usa mediaForCarousel após gerar.
        media: count ? mediaForCarousel(bookId, selector, count) : [],
        caption: captionFor(bookId),
      };
    }
    case 'reels': {
      // selector = nome do arquivo mp4 (validado contra os reels locais, se houver).
      const reels = _reelsFiles(bookId);
      if (reels.length && !reels.includes(selector)) {
        throw new Error(
          `selector inválido para reels: "${selector}" (use ${reels.join(', ')})`
        );
      }
      if (!/\.mp4$/i.test(selector)) {
        throw new Error(`selector de reels deve ser um .mp4: "${selector}"`);
      }
      return {
        kind: 'reels',
        media: [`${PUB}/biblioteca/assets/reels/${bookId}/${selector}`],
        caption: captionFor(bookId),
      };
    }
    default:
      throw new Error(`type desconhecido: "${type}" (use feed, story, carrossel, reels)`);
  }
}

// ---------------------------------------------------------------------------
// Leituras locais do kit (para optionsFor / validação de carrossel)
// ---------------------------------------------------------------------------

// Lê o manifest.json do kit do livro (lança se ausente — é o contrato do kit).
function _manifest(bookId) {
  const p = path.join(KIT_DIR, bookId, 'manifest.json');
  return JSON.parse(fs.readFileSync(p, 'utf8'));
}

// caps.json -> { chapters: { overview: N, <slug>: N } }. Retorna o objeto
// chapters ou null se não existir.
function _capsChapters(bookId) {
  const p = path.join(KIT_DIR, bookId, 'caps.json');
  if (!fs.existsSync(p)) return null;
  try {
    const data = JSON.parse(fs.readFileSync(p, 'utf8'));
    return data && data.chapters ? data.chapters : null;
  } catch {
    return null;
  }
}

// Arquivos .mp4 em assets/reels/<book>/ (vazio se a pasta não existir).
function _reelsFiles(bookId) {
  const dir = path.join(REELS_DIR, bookId);
  if (!fs.existsSync(dir)) return [];
  return fs
    .readdirSync(dir)
    .filter((f) => /\.mp4$/i.test(f))
    .sort();
}

// ---------------------------------------------------------------------------
// optionsFor — opções de UI a partir do manifest do kit
// ---------------------------------------------------------------------------
function optionsFor(bookId) {
  const manifest = _manifest(bookId);
  const ids = new Set((manifest.assets || []).map((a) => a.id));

  const options = {};

  // feed: ideia / citacao-feed / mapa (apenas os presentes no manifest)
  const feed = FEED_SELECTORS.filter((s) => ids.has(s));
  if (feed.length) options.feed = feed;

  // story: capa-story / citacao-story (apenas os presentes no manifest)
  const story = STORY_SELECTORS.filter((s) => ids.has(s));
  if (story.length) options.story = story;

  // carrossel: ['overview'] + slugs de capítulo de caps.json (se houver)
  const caps = _capsChapters(bookId);
  if (caps) {
    // overview primeiro, depois os capítulos na ordem do caps.json (sem duplicar)
    const chapters = Object.keys(caps);
    const ordered = ['overview'].concat(chapters.filter((c) => c !== 'overview'));
    options.carrossel = ordered;
  } else if (ids.has('overview')) {
    options.carrossel = ['overview'];
  }

  // reels: nomes de arquivos mp4 locais (vazio se a pasta não existe)
  const reels = _reelsFiles(bookId);
  if (reels.length) options.reels = reels;

  return {
    book: bookId,
    types: Object.keys(options),
    options,
    captionPreview: captionFor(bookId),
  };
}

module.exports = {
  PUB,
  HASHTAGS_BASE,
  captionFor,
  resolve,
  mediaForCarousel,
  optionsFor,
};
