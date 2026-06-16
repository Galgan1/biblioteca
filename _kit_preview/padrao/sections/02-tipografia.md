## 02. Tipografia

> A tipografia é a **voz** da marca. Duas famílias, papéis fixos, pesos disciplinados. Quando o leitor bate o olho numa peça do Minuto Real, é a tipografia — antes da cor — que diz "isto é nosso". Esta seção é a lei. Os valores são reais: lidos de `marca.py` (contrato de fontes) e do `BASE_CSS`/`ARCH_CSS` em `gerar_infografico.py` (tamanhos e pesos de fato renderizados no canvas 1080×1350).

---

### As duas famílias — e por que só duas

A marca tem **exatamente duas** famílias. Nada mais entra na arte final.

| Família | Papel (`marca.py`) | Arquivo | O que veste |
|---|---|---|---|
| **Hanken Grotesk** | `display` | `_fonts/HankenGrotesk.ttf` | Títulos-herói, kickers, rótulos, números, UI, chips/badges, "USO:"/"Na prática", watermark. É a **voz que afirma**. |
| **Literata** | `serif` | `_fonts/Literata.ttf` | Citações, capitular (drop cap), trechos em voz de "livro", epígrafes. É a **voz que cita**. |

Ambas são variáveis (`@font-face` declara `font-weight:100 900` — pesos contínuos do Thin ao Black) e embarcadas em base64 no PNG, então **a fonte nunca falha por estar fora da máquina**. No fallback gracioso (`marca.py._FALLBACK`), Hanken cai em `arialbd` e Literata em `georgia` — aceitável só em rascunho local, **proibido na arte final**.

**A regra do papel:**
- **Hanken** é o default de tudo que organiza, classifica, comanda e enumera. Toda a estrutura do infográfico (cabeçalho, grade, rodapé) é Hanken.
- **Literata** entra **só** quando o texto é a *fala do livro*: uma citação literal, uma capitular abrindo um conceito, uma epígrafe. Itálico é exclusivo dela.

Se você está em dúvida sobre qual usar, a resposta é Hanken. Literata é a exceção deliberada.

---

### Pesos — a escala de ênfase

Hanken Grotesk traz nove pesos. Usamos **três faixas**, nunca o arco-íris de pesos:

| Faixa | Pesos | Onde |
|---|---|---|
| **Pesada** | Black (900) | Título-herói, números-herói, rótulos de item (`.lbl`), brandmark, chips. |
| **Forte** | ExtraBold/Bold (700–800) | Kickers, badges, tags, "USO:"/"Na prática", `<strong>` no corpo. |
| **Leve** | Medium/Regular (500) | Descrições (`.sub`, `.ctx`, `.exp`), promessa/subtítulo. |

Tabela de uso (papel → família → peso → caixa):

| Papel na peça | Família | Peso | Caixa |
|---|---|---|---|
| Título-herói (`.head h1`) | Hanken | **Black 900** | CAIXA-ALTA |
| Número-herói (`.stat .num`) | Hanken | **Black 900** | — |
| Rótulo de item (`.lbl`, `.col-label`) | Hanken | **Black 900** | CAIXA-ALTA |
| Kicker / badge / tag | Hanken | ExtraBold 800 | CAIXA-ALTA |
| "Na prática" / "USO:" (`.kick`, `.lab`, `.pk`) | Hanken | Black 900 | CAIXA-ALTA |
| Chip de número (`.chip`) | Hanken | Black 900 | CAIXA-ALTA |
| Brandmark "Minuto**Real**" | Hanken | Black 900 | CAIXA-ALTA |
| Promessa / subtítulo (`.promise`, `.sub`) | Hanken | SemiBold 600 | Frase |
| Descrição de item (`.sub`, `.ctx`, `.exp`) | Hanken | Medium/Regular 500 | Frase |
| Watermark (`.wm`) | Hanken | ExtraBold 800 | CAIXA-ALTA |
| **Citação / capitular** | **Literata** | Regular/Medium | Frase, itálico permitido |

---

### Hierarquia e tamanhos (canvas 1080×1350)

Valores reais do gerador. O título-herói tem **auto-fit**: o `_FIT_JS` reduz a fonte em passos de 3px (piso 40px) até caber na largura — então os números abaixo são o **teto**, não um valor fixo.

| Elemento | Tamanho real | Peso | Notas |
|---|---|---|---|
| **Título-herói `h1`** | 54–78px | 900 | lista **78**, numeros **76**, fluxo **74**, anatomia **60**, compara **54** |
| Número-herói (`.stat .num`) | **104px** | 900 | unidade `.u` 52px, prefixo `.pre` 54px |
| Rótulo de passo (`.flow .lbl`) | **46px** | 900 | maior rótulo de item |
| Linha da LISTA (`.rows`) | **40px** base | — | rótulo e sub escalam em `em` a partir daqui |
| Rótulo de item (`.lbl`) | ~0.97em (~39px) | 900 | CAIXA-ALTA |
| Rótulo de coluna (`.col-label`) | **31px** | 900 | comparativo |
| Promessa / subtítulo (`.promise`) | **30px** | 600 | máx. 880px de largura |
| Descrição "sub" (`.sub`) | ~0.65em (~26px) | 500 | corpo do item, `text-wrap:pretty` |
| Contexto de número (`.ctx`) | **25px** | 500 | |
| Tag / kicker / badge | 18–22px | 800 | CAIXA-ALTA, tracking alto |
| "Na prática" / "USO:" (`.kick`/`.lab`/`.pk`) | 18–23px | 900 | CAIXA-ALTA |
| Brandmark | **25px** | 900 | CAIXA-ALTA |
| Chip de número (`.chip`) | 21px / `.big` 33px | 900 | número em cima, "cap" embaixo |
| Watermark (`.wm`) | 18–20px | 800 | CAIXA-ALTA, tracking 0.24em |

**Leitura do ritmo:** a peça respira numa razão clara — herói ~76px → rótulo ~40px → corpo ~26px → metainfo ~20px. Cada degrau é roughly metade do anterior. Não invente tamanhos intermediários; ancore nos degraus acima.

---

### Caixa-alta, tracking e quebra de linha

**CAIXA-ALTA** (`text-transform:uppercase`) é a assinatura dos títulos, rótulos, kickers e watermark. Nunca digite o texto já em maiúsculas no `_data.py` — deixe o CSS fazer o `uppercase` (preserva acentuação correta em pt-BR e mantém o controle no token).

**Tracking (`letter-spacing`):**
- Títulos-herói: **negativo** (`-.018em` a `-.022em`) — letras pesadas e grandes pedem aperto para virar bloco sólido.
- Números-herói: bem negativo (`-.04em`).
- Kickers, badges, watermark: **positivo e generoso** (`.12em` a `.26em`) — texto pequeno em caixa-alta precisa de ar entre as letras para respirar e parecer "etiqueta de catálogo".

**Quebra de linha:** todo título usa `text-wrap:balance` (linhas equilibradas, sem órfã solta); corpo e descrição usam `text-wrap:pretty`. Não force `<br>` manual nos títulos — confie no balance + auto-fit.

**Itálico:** só na Literata, só em citação. Itálico em Hanken é **proibido** — descaracteriza a voz grotesca.

---

### O título-herói premium

É o efeito das referências do usuário. Receita real (está no `BASE_CSS`/`ARCH_CSS`), sem exagero:

1. **Peso e caixa:** Hanken **Black 900**, `text-transform:uppercase`, tracking negativo. O título é um bloco, não uma linha de texto.
2. **Duas tintas na mesma frase:** a parte-chave em verde (`.lt` → `var(--green)`) e o resto em tinta clara (`.bd` → `var(--ink)`). Vem direto do `_data.py` (`header_light` + `header_bold`). Isso cria foco sem mudar de fonte.
3. **Brilho verde sutil (o "glow"):** `text-shadow: 0 0 50px oklch(72% 0.14 152 / .38)` aplicado **só na parte verde** (`.lt`). É um halo difuso (raio ~50px, opacidade ~.38), não um contorno. Faz a palavra-chave "acender" sobre o fundo escuro — cinematográfico, nunca neon.
4. **Textura/grão na letra:** o grão vem do `.slide::before` (pontos radiais sutis) por baixo, e o efeito de "letra vazada com textura" aparece no **ghost** (`.ghost`): Black 900, `color:transparent` + `-webkit-text-stroke:2px oklch(... / .09)`, com máscara radial. É a letra-fantasma gigante atrás do conteúdo (o "→", "VS", "%"). Use-o como camada de profundidade — **um por peça**, nunca competindo com o herói.
5. **Capitular (Literata):** para abrir uma ideia em tom editorial, troque a primeira letra de um bloco por uma **capitular em Literata** (serif, ~2–3 linhas de altura, verde ou ouro). Reserve para citações e aberturas — é o único lugar onde a serif lidera.

Discrição é a regra: **um** glow (na palavra-chave), **um** ghost, **uma** capitular por peça. Empilhar os três no mesmo elemento vira ruído.

---

### Faça / Não faça

**Faça**
- Use **só Hanken + Literata** na arte final; embarque os `.ttf` (já é automático no `_font_face()`).
- Título sempre **Hanken Black 900, CAIXA-ALTA, tracking negativo**.
- Deixe o `text-transform:uppercase` no CSS fazer a maiúscula (acentos corretos em pt-BR).
- Reserve Literata para a **voz do livro** (citação, capitular, epígrafe) — e o itálico só aqui.
- Confie no `text-wrap:balance` + auto-fit; ancore os tamanhos nos degraus reais (~76 → ~40 → ~26 → ~20px).
- Aplique o glow verde **só na palavra-chave** (`.lt`), com raio ~50px.

**Não faça**
- ❌ Fonte de sistema (Arial/Georgia/Calibri) na arte final — é fallback de rascunho, não padrão.
- ❌ Uma terceira família, nem variantes "parecidas" de Hanken/Literata.
- ❌ Esticar, condensar ou falsificar peso/itálico via CSS (`font-stretch`, oblique sintético) — use os pesos variáveis reais.
- ❌ Itálico em Hanken.
- ❌ Texto digitado já em CAIXA-ALTA no `_data.py` (quebra acento e tira o controle do token).
- ❌ Mais de um glow, ghost ou capitular por peça; nem glow em corpo de texto.
- ❌ Inventar tamanhos fora da escala — sem 60px de corpo nem 90px de herói "para destacar".
