# Plano Premium — Biblioteca

Síntese de auditoria de 10 dimensões (performance, tipografia, espaçamento,
cor/tokens, motion, imagens, acessibilidade, SEO, responsivo, microcopy).
Objetivo: elevar o site de "muito bom" para **premium** — refinado, rápido,
consistente, impecável no detalhe.

> **Princípio que governa o plano:** trabalho premium aqui é **sistêmico**, não
> bespoke. Quase tudo se resolve editando **4 arquivos centrais** (`marca.py`,
> `assets/style.css`, `gerar_livro.py`, `script.js`) **uma vez** e regenerando as
> 100 páginas. Isso é sequencial e quer **uma cabeça só** (consistência = essência
> do premium). O paralelismo real só compensa na **geração de assets** (Fase 5).

---

## Achados confirmados por múltiplos agentes (alta confiança)

| Achado | Quem confirmou |
|---|---|
| 65 MB de PNG, zero WebP — gargalo dominante de velocidade | performance + imagens |
| Dark mode reprova contraste AA (corpo, pílulas ativas, foco) | a11y + cor |
| Capas/cards sem sombra — visual chapado, sem profundidade | imagens + motion + cor |
| OG image em retrato 2:3 (errado p/ 1.91:1) nas 100 páginas | SEO + imagens |
| `marca.py` e `style.css` usam nomes de token divergentes | cor (risco de quebra silenciosa) |
| Escalas de tipo (17 tamanhos) e espaço (15 valores) ad-hoc | tipografia + espaçamento |
| `meta description` do index obsoleta/duplicada | SEO + microcopy |
| `.card-body` sem `max-width` → linhas de 80–90 caracteres | tipografia + espaçamento |
| `animate-entrance`: 7 cards escalonados + 93 simultâneos | performance + motion |

---

## Fase 1 — Fundação: sistema de tokens (sequencial · `marca.py` + `:root` do CSS)

Tudo o resto referencia tokens. Fazer primeiro.

1. **Unificar `marca.py` ↔ `style.css`** (CRÍTICO). 5 tokens com nomes incompatíveis
   (`verde-deep/--green-dark`, `tinta/--black`, `tinta-fraca/--gray-dark`,
   `alerta/--dislike`, `papel/--paper-bg`) e `verde-soft` com **valor** divergente
   (chroma 0.06 vs 0.03). Hoje `marca.css_root()` gera variáveis que o site não
   reconhece → uma regeneração quebra o visual em silêncio. Adotar o vocabulário do
   site (mais semântico) e espelhar em `_CSS_VARMAP`. Cobrir os 9 tokens órfãos
   (`--surface-hover`, `--on-green`, `--footer-bg`, `--border-solid`, etc.).
   *(cor #1, #2, #6, #7)*
2. **Escala tipográfica modular.** Trocar os 17 tamanhos avulsos por ~7 variáveis
   (`--text-xs:0.75 → --text-2xl:2 → --text-display:clamp(...)`, razão ~1.25).
   `0.72/0.75/0.78rem` são indistinguíveis hoje — viram ruído, não hierarquia. *(tipo #2)*
3. **Escala de espaçamento.** `--sp-xs:0.5 … --sp-xl:3rem`. Elimina os 15 valores
   ad-hoc (`0.85` vs `0.95rem`) que dão a sensação de "site um pouco errado". *(espaço #3)*
4. **Tokens de profundidade.** `--surface` (camada de card no dark) e
   `--shadow-card` / `--shadow-card-hover`. Base para Fases 2 e 5. *(cor #3, motion #5)*

---

## Fase 2 — Dark mode + acabamento visual (sequencial · `style.css`)

O lado claro está limpo; **o dark mode é a metade quebrada**. Pura edição de CSS,
maior salto de qualidade percebida por minuto investido.

**Contraste (a11y — corrigir já):**
- `--gray-dark` no dark = 3.25:1 no corpo de texto → subir p/ ~`oklch(82%)`. *(a11y #1)*
- Pílulas/botões ativos: `--on-green` sobre `--green` = 2.91:1 → usar `--on-green`
  claro no dark (ou escurecer `--green`). Idem dislike. *(a11y #2)*
- Foco invisível: `outline` verde sobre fundo escuro = 2.89:1 → outline claro,
  `width:3px`. *(a11y #3)*

**Profundidade & acabamento (o "caro"):**
- `--surface` + `box-shadow` sutil nos `.card` no dark → para de parecer chapado. *(cor #3)*
- Sombra na capa: `.card-cover img { box-shadow }` → 100 capas ganham espessura física. *(imagens #7)*
- Hover do card eleva `-2px` **sem sombra** hoje (parece glitch) → adicionar sombra. *(motion #5)*

**Tipografia (transforma "dashboard" em "editorial"):**
- **Ativar Literata** em `.card-body` / `.header-intro` / lições — hoje a serif só
  aparece em `blockquote`; o par tipográfico não trabalha. *(tipo #1)*
- `line-height` do corpo 1.55 → 1.65–1.7 (leitura, não UI). *(tipo #3)*
- `.card-body { max-width: 68–70ch }` — corta linhas de 80–90 caracteres. *(tipo #4, espaço #7)*
- Reduzir UPPERCASE (12 usos hoje) e remover a regra global `h1–h4 uppercase`
  (perigosa); `letter-spacing: 0.06em` no `.card-title` (hoje apertado a 0.02em). *(tipo #5, #6, #7)*

**Layout & respiração:**
- Container 950 → ~1100px (capas ~30% maiores; estante deixa de parecer thumbnails). *(espaço #1)*
- `gap` da grade 2rem → 1.25rem **e** `.shelf-section` mb → 4rem (move o espaço para
  *entre* seções, não dentro da grade). *(espaço #4)*
- Header: 6rem de vácuo (padding+margin duplicados) → ~4rem. *(espaço #5)*

**Motion:**
- `prefers-reduced-motion`: trocar `duration:0.01ms` por `animation:none` +
  `opacity:1` (hoje pode piscar). *(motion #6)*
- `:active` em voto/chip/toggle (feedback de toque — crítico no mobile). *(motion #2)*
- `<details>` das trilhas anima a seta mas o conteúdo é corte seco → `grid-template-rows
  0fr→1fr`. *(motion #1)*

---

## Fase 3 — Template + regeneração (sequencial · `gerar_livro.py`, `retrofit`, `gerar_seo.py`)

Editar os geradores **uma vez** e regenerar as 100 páginas. Sequencial pela race de
`books.json` + template compartilhado.

**Compartilhamento social (o que se vê ao colar o link):**
- OG image em retrato nas 100 páginas → usar banner 1.91:1 (genérico agora, por-livro
  na Fase 5). *(SEO #1, imagens #1/#2)*
- `twitter:card=summary` → `summary_large_image` nas páginas de livro (hoje só o index). *(SEO #2)*
- `og:type=article` → `book`/`website`. *(SEO #4)*
- `og:title` de capítulo com breadcrumb de 94 chars → versão curta ≤65. *(SEO #5)*
- `Article` JSON-LD sem `datePublished`/`dateModified` (já temos `mtime()`). *(SEO #6)*

**Template (`gerar_livro.py`):**
- `theme-color` hardcoded sem variante dark nas páginas de capítulo → 2 variantes
  como no index (barra do Safari fica branca no dark hoje). *(mobile #3, cor #4)*
- Nav de capítulo sem `aria-label`/`rel` no template (versões no disco têm; uma
  regeneração perde). *(a11y #7)*
- Formato do `progress`: `"9 Capítulos"` vira `"Cheat sheet · 9 cap."`; normalizar o
  one-off `"Resumo Geral"`. *(microcopy #8)*

---

## Fase 4 — Performance, microcopy e a11y de interação (sequencial · `script.js` + `style.css`)

**Performance (velocidade percebida = premium):**
- `<script defer>` (fetch de `books.json` começa mais cedo). *(perf #5)*
- Fontes assíncronas (`preload` + `onload`) — hoje render-blocking. *(perf #4)*
- `width`/`height` nos `<img>` de capa (elimina CLS). *(perf #2)*
- `books-slim.json` sem `description`/`compras`/`tags` (97 KB → ~30 KB) + confirmar
  `gzip` no nginx p/ `application/json`. *(perf #3)*
- `IntersectionObserver` na entrada dos cards + não reanimar em filtro/busca. *(perf #6, motion #3)*

**Microcopy & voz:**
- Erro de carregamento expõe `file://`/"Live Server" em produção → separar dev/prod. *(microcopy #6)*
- `meta description` obsoleta no index → alinhar com a OG. *(microcopy #1, SEO #3)*
- "Acervo · do mais curtido ao menos" (jargão de rede) → "Acervo · mais relevantes". *(microcopy #3)*
- Placeholder inconsistente (`...` vs `…`) → unificar via JS. *(microcopy #2)*
- Estados vazios planos → voz editorial (interpolar a query na busca). *(microcopy #5)*
- "Não curtir" (pt-PT-ish) → rever rótulo; **decisão de produto:** manter o dislike? *(microcopy #7)*

**A11y de interação:**
- Modal Pix: focus trap + restaurar foco ao fechar. *(a11y #4)*
- `card-soon` é `<a>` sem `href` (falsa affordance) → `<div>`. *(a11y #6)*
- `aria-busy` no skeleton durante o load. *(a11y #8)*

**Mobile (maioria do tráfego de conteúdo):**
- Alvos de toque: `.vote-btn` 40→44px; `.trilha-chip` ~22→44px (`min-height` + flex). *(mobile #1, #2)*
- `chapter-nav` empilhar em coluna ≤640px. *(mobile #4)*
- `.search-input { font-size: max(1rem,16px) }` + `touch-action:manipulation` (zoom iOS). *(mobile #7)*

---

## Fase 5 — Assets (PARALELO — onde subagentes ganham de verdade)

Cada arquivo é dono de si → paraleliza limpo. Mas a maioria é **um script em lote**,
não 20 agentes.

1. **WebP das 100 capas** (`cwebp`/Pillow, q≈82) + `<picture>`/`srcset`. ~65 MB → ~18 MB.
   **Um script** resolve. *(perf #1, imagens #5)* — **o item de maior impacto isolado.**
2. **Re-buscar ~8 capas fora do padrão**: quadradas (`48-leis`, `arte-da-seducao`,
   `startup-enxuta`, `maquiavel`), invertida (`mindset`), minúsculas (`o-alquimista`),
   pesada (`futebol-brasileiro` 1.5 MB). *(imagens #2/#3/#6/#8)* — **aqui ~8 itens
   independentes paralelizam.**
3. **OG banners 1200×630 por livro** (fundo de marca + capa + título), via
   `gerar_capa.py`. 100 itens independentes → **bom alvo de paralelismo**. *(SEO #1)*
4. **Redesenhar `og-banner.png`** da home (hoje 94% branco). *(imagens #4)*

---

## Modelo de execução (honesto)

- **Fases 1–4** são ~4 edições centrais + regeneração. **Sequenciais, uma cabeça.**
  20 agentes aqui = race em `style.css`/template + deriva de estilo (o oposto de premium).
- **Fase 5** é o único terreno de paralelismo real: itens 2 e 3 (≈108 assets
  independentes). Itens 1 e 4 são scripts únicos.
- Ordem recomendada: **1 → 2 → 3/4 → 5**, com verificação no preview ao fim de cada fase
  e deploy só depois de validado.

## Decisão tomada

**Trilhas: abertas no desktop, fechadas no mobile (`<768px`).** No celular as
3 linhas de controle empurravam os livros para baixo da dobra; fechar por padrão no
mobile (via JS no load) libera a primeira dobra para o acervo, mantendo sua escolha
no desktop. Entra na Fase 4 (`script.js`), junto dos alvos de toque. *(mobile #8)*
