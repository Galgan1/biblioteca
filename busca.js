/* busca.js — Engine de busca premium da Biblioteca (client-side, sem dependências).
 *
 * Resolve o que a busca antiga não fazia: acento-insensível, tolerante a erro de
 * digitação (fuzzy), multi-termo (AND), multi-campo com peso, ranking por relevância,
 * realce dos termos e sugestão "você quis dizer".
 *
 * É PURA (sem DOM): o script.js cuida da tela. Roda em node para teste:
 *   node busca.js --test
 *
 * API:  Busca.buscar(livros, query) -> [livro + _score], ordenado por relevância
 *       Busca.sugerir(livros, query) -> string | null   (p/ "você quis dizer")
 *       Busca.realcar(texto, query)  -> HTML com <mark> nos trechos casados (escapado)
 */
(function (root) {
  'use strict';

  // --- normalização: minúsculas + sem diacríticos (NFD) ---
  function fold(s) {
    return (s || '').normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase();
  }

  // fold preservando o mapa posição→original (necessário p/ realçar o texto cru)
  function foldMap(s) {
    let folded = '';
    const map = [];
    for (let i = 0; i < s.length; i++) {
      const f = fold(s[i]);
      for (const ch of f) { folded += ch; map.push(i); }
    }
    return { folded, map };
  }

  // distância de Levenshtein com poda (retorna maxD+1 se ultrapassa o teto)
  function lev(a, b, maxD) {
    const la = a.length, lb = b.length;
    if (Math.abs(la - lb) > maxD) return maxD + 1;
    let prev = Array.from({ length: lb + 1 }, (_, i) => i);
    let cur = new Array(lb + 1);
    for (let i = 1; i <= la; i++) {
      cur[0] = i;
      let best = cur[0];
      for (let j = 1; j <= lb; j++) {
        const cost = a[i - 1] === b[j - 1] ? 0 : 1;
        cur[j] = Math.min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + cost);
        if (cur[j] < best) best = cur[j];
      }
      if (best > maxD) return maxD + 1; // toda a linha já passou do teto
      const t = prev; prev = cur; cur = t;
    }
    return prev[lb];
  }

  // teto de erro tolerado por tamanho do termo (curtos exigem exatidão)
  function maxDistFor(tok) {
    if (tok.length <= 3) return 0;
    if (tok.length <= 6) return 1;
    return 2;
  }

  // campos pesquisados e seus pesos (título manda; descrição é desempate)
  const CAMPOS = [
    { key: 'title', peso: 10 },
    { key: 'author', peso: 6 },
    { key: 'tags', peso: 4 },
    { key: 'description', peso: 2 },
  ];

  // pré-computa os campos foldados do livro (memoizado em _idx; invalida se mudar título)
  function indexar(livro) {
    if (livro._idx && livro._idx._t === livro.title) return livro._idx;
    livro._idx = {
      _t: livro.title,
      title: fold(livro.title),
      author: fold(livro.author),
      tags: fold((livro.tags || []).join(' ')),
      description: fold(livro.description || ''),
    };
    return livro._idx;
  }

  // pontua UM termo contra UM campo já foldado; null se não casa
  function pontuar(campo, tok, peso) {
    if (!campo) return null;
    const pos = campo.indexOf(tok);
    if (pos !== -1) {
      // bônus por posição: prefixo do campo > início de palavra > meio
      let bonus = 0.2;
      if (pos === 0) bonus = 1.0;
      else if (campo[pos - 1] === ' ') bonus = 0.6;
      return peso * (1 + bonus);            // match exato
    }
    const md = maxDistFor(tok);
    if (md === 0) return null;
    let melhor = Infinity;
    for (const palavra of campo.split(/\s+/)) {
      if (palavra.length < tok.length - md) continue;
      const d = lev(tok, palavra.slice(0, tok.length + md), md);
      if (d < melhor) melhor = d;
      if (melhor === 0) break;
    }
    if (melhor <= md) return peso * (0.5 - 0.15 * melhor); // fuzzy vale menos
    return null;
  }

  // BUSCA: cada termo (AND) precisa casar em algum campo; soma o melhor por termo
  function buscar(livros, query) {
    const toks = fold(query).split(/\s+/).filter(Boolean);
    if (!toks.length) return livros.slice();
    const out = [];
    for (const livro of livros) {
      const idx = indexar(livro);
      let total = 0, ok = true;
      for (const tok of toks) {
        let melhorTok = 0;
        for (const c of CAMPOS) {
          const s = pontuar(idx[c.key], tok, c.peso);
          if (s !== null && s > melhorTok) melhorTok = s;
        }
        if (melhorTok <= 0) { ok = false; break; }
        total += melhorTok;
      }
      if (ok) out.push(Object.assign({}, livro, { _score: total }));
    }
    out.sort((a, b) => b._score - a._score || a.title.localeCompare(b.title, 'pt'));
    // corte de relevância relativa: não poluir matches fortes com ruído fraco.
    // Ex.: "principe" casa "Príncipe" (forte) e "princípio" na descrição de outro
    // livro (fraco, 40× menor) — só os relevantes ao melhor resultado ficam.
    if (out.length) {
      const piso = out[0]._score * 0.1;
      return out.filter((b) => b._score >= piso);
    }
    return out;
  }

  // SUGESTÃO p/ zero resultados: o título/autor mais próximo da query inteira
  function sugerir(livros, query) {
    const q = fold(query).replace(/\s+/g, ' ').trim();
    if (q.length < 3) return null;
    // tolera MAIS que a busca (que aceita só ≤2): senão a sugestão nunca apareceria —
    // quando o erro é pequeno a busca já acha; a sugestão só vale p/ o erro maior.
    const teto = Math.max(2, Math.ceil(q.length / 3));
    let melhor = null, melhorD = teto + 1;
    for (const livro of livros) {
      for (const cand of [livro.title, livro.author]) {
        const c = fold(cand);
        // compara com o nome inteiro E com cada palavra (casa sobrenome/termo do meio)
        let d = lev(q, c.slice(0, q.length + 2), teto);
        for (const palavra of c.split(/\s+/)) {
          if (Math.abs(palavra.length - q.length) > teto) continue;
          const dp = lev(q, palavra, teto);
          if (dp < d) d = dp;
        }
        if (d < melhorD) { melhorD = d; melhor = cand; }
      }
    }
    return melhorD <= teto ? melhor : null;
  }

  function esc(s) {
    return (s || '').replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  }

  // REALCE: envolve em <mark> os trechos do texto ORIGINAL casados pelos termos (exatos)
  function realcar(texto, query) {
    const toks = fold(query).split(/\s+/).filter(Boolean);
    if (!toks.length) return esc(texto);
    const { folded, map } = foldMap(texto);
    const hit = new Array(texto.length).fill(false);
    for (const tok of toks) {
      let from = 0, pos;
      while ((pos = folded.indexOf(tok, from)) !== -1) {
        for (let k = pos; k < pos + tok.length; k++) hit[map[k]] = true;
        from = pos + tok.length;
      }
    }
    let html = '', i = 0;
    while (i < texto.length) {
      if (hit[i]) {
        let j = i;
        while (j < texto.length && hit[j]) j++;
        html += '<mark>' + esc(texto.slice(i, j)) + '</mark>';
        i = j;
      } else {
        html += esc(texto[i]); i++;
      }
    }
    return html;
  }

  const Busca = { fold, lev, buscar, sugerir, realcar };
  root.Busca = Busca;
  if (typeof module !== 'undefined' && module.exports) module.exports = Busca;
})(typeof self !== 'undefined' ? self : globalThis);

// ---------------------------------------------------------------------------
// Auto-teste (só em node): node busca.js --test
// ---------------------------------------------------------------------------
if (typeof require !== 'undefined' && require.main === module && process.argv.includes('--test')) {
  const B = module.exports;
  const livros = [
    { id: 'arte-da-guerra', title: 'A Arte da Guerra', author: 'Sun Tzu', tags: ['Estratégia', 'Guerra'], description: 'Tratado militar.' },
    { id: 'psicologia-financeira', title: 'A Psicologia Financeira', author: 'Morgan Housel', tags: ['Finanças', 'Comportamento'], description: 'Dinheiro e mente.' },
    { id: 'rapido-e-devagar', title: 'Rápido e Devagar', author: 'Daniel Kahneman', tags: ['Psicologia', 'Decisão'], description: 'Dois sistemas de pensamento.' },
    { id: 'arte-da-seducao', title: 'A Arte da Sedução', author: 'Robert Greene', tags: ['Sedução', 'Poder'], description: 'Estratégias de atração.' },
  ];
  let falhas = 0;
  const ok = (cond, msg) => { if (!cond) { falhas++; console.error('  ✗ ' + msg); } else console.log('  ✓ ' + msg); };
  const ids = (q) => B.buscar(livros, q).map((b) => b.id);

  console.log('acento-insensível:');
  ok(ids('estrategia').includes('arte-da-guerra'), 'estrategia → Estratégia (tag)');
  ok(ids('rapido')[0] === 'rapido-e-devagar', 'rapido → Rápido (título, no topo)');
  console.log('tolerância a erro de digitação (fuzzy):');
  ok(ids('kahnemann').includes('rapido-e-devagar'), 'kahnemann (typo) → Kahneman');
  ok(ids('seducao').includes('arte-da-seducao'), 'seducao → Sedução');
  console.log('multi-termo (AND) + ranking:');
  ok(ids('arte guerra')[0] === 'arte-da-guerra', 'arte guerra → A Arte da Guerra primeiro');
  ok(ids('arte').length === 2, 'arte → as duas "Arte da..."');
  console.log('campos:');
  ok(ids('housel').includes('psicologia-financeira'), 'autor: housel');
  ok(ids('decisao').includes('rapido-e-devagar'), 'tag: decisao');
  console.log('realce (preserva caixa e acento do original):');
  ok(B.realcar('A Arte da Guerra', 'arte') === 'A <mark>Arte</mark> da Guerra', 'realça "Arte" no original');
  ok(B.realcar('Estratégia', 'estrategia') === '<mark>Estratégia</mark>', 'realça com acento');
  console.log('sugestão:');
  ok(B.sugerir(livros, 'kahnemen') === 'Daniel Kahneman', 'você quis dizer Kahneman');
  ok(B.buscar(livros, 'xyzqwk').length === 0, 'lixo → zero resultados');

  console.log(falhas ? `\n${falhas} FALHA(S)` : '\nTODOS OS TESTES PASSARAM');
  process.exit(falhas ? 1 : 0);
}
