## 07. Acabamento Cinematográfico

A camada de *finish*. É o que separa uma peça **premium** de uma peça que parece feita às pressas — e quase nada disso é o conteúdo: é atmosfera, profundidade, grão e brilho controlado. **Fonte de verdade:** o `BASE_CSS` de `gerar_infografico.py` e o de `gerar_carrossel.py`. Todo valor abaixo foi confirmado no código; se algo divergir, o código vence. A regra que rege a seção inteira é uma só: **mão leve**. Premium é sutileza e controle. Glow estourado, grão grosseiro e sombra dura são a assinatura do amador.

---

### A pilha de acabamento (a "assinatura" recorrente)

Toda peça da rede carrega a mesma pilha de finish, construída em camadas sobre o `.slide`. Essas quatro coisas, juntas, são a **assinatura visual** que faz qualquer peça ser reconhecida como Minuto Real à distância:

1. **Fundo em camadas** — radial-glows verdes + gradiente escuro + vinheta nos cantos.
2. **Grade de pontos** (36px) com máscara radial — `.slide::before`.
3. **Moldura tracejada verde** (inset 38px, raio 32px, opacity .38) — `.slide::after`.
4. **Número-fantasma** — stroke verde translúcido com máscara radial — `.ghost`.

Nenhuma delas grita. Todas trabalham no fundo, abaixo do conteúdo (`z-index:0`), deixando o texto e o objeto no `z-index:1`. Vamos por partes.

---

### 1 · Profundidade em camadas (o fundo nunca é chapado)

Um fundo de cor sólida é a marca registrada do amador. No padrão, o `.slide` empilha **quatro fundos** numa só declaração `background` (lidos de cima para baixo, o último é o mais ao fundo):

```css
.slide{ ... background:
   radial-gradient(135% 95% at 102% 108%, oklch(24% 0.045 152 / .85) 0%, transparent 48%),
   radial-gradient(115% 72% at 50% -12%, oklch(27% 0.05 152) 0%, transparent 60%),
   radial-gradient(150% 125% at 50% 48%, transparent 52%, oklch(5% 0.012 152 / .6) 100%),
   linear-gradient(177deg, var(--bg) 0%, var(--bg2) 100%); }
```

Cada camada tem um papel:

| Camada | Tipo | Papel cinematográfico |
|---|---|---|
| 1 (topo) | radial em `102% 108%` | **Glow verde no canto inferior-direito** — uma luz de cena fora do quadro, quente e fraca (alpha .85, mas verde escuro L24). |
| 2 | radial em `50% -12%` | **Glow verde no topo-centro** — "luz de palco" descendo sobre o título. |
| 3 | radial em `50% 48%` | **Vinheta** — transparente no centro, escurece para `oklch(5% .012 152 / .6)` nas bordas. É o que sela os cantos. |
| 4 (fundo) | linear `177deg` | **Base escura** — `--bg` (`oklch(14.5% .014 152)`) → `--bg2` (`oklch(10.5% .012 152)`), quase preto, levemente esverdeado. |

O segredo é que **os glows são verdes** (hue 152, croma baixíssimo .045–.05) e a vinheta também é verde-quase-preta. O fundo inteiro respira a cor-mãe sem nunca virar "tela verde". A vinheta (camada 3) é o truque clássico de cinema: o olho é atraído para o centro iluminado porque os cantos foram discretamente apagados.

> No carrossel, o Story usa uma variante com a mesma lógica, só remapeada para o quadro 9:16: glow em `100% 104%`, glow de topo em `50% -4%`, vinheta em `50% 50%` fechando a `oklch(5% .012 152 / .62)`. Mesma alma, outro formato.

**Faça:** sempre quatro camadas — dois glows verdes, uma vinheta, uma base em gradiente. **Não faça:** `background:#08080c` sólido (chapado, morto).

---

### 2 · Grão / textura de filme (tira o "digital chapado")

O fundo perfeitamente liso é digital demais. A solução do padrão **não** é um ruído pesado — é uma **grade de pontos finíssima**, tão sutil que o olho lê como textura de papel/filme, não como pontos:

```css
.slide::before{ content:''; position:absolute; inset:0; pointer-events:none;
  background-image:radial-gradient(oklch(78% 0.07 152 / .055) 1.1px, transparent 1.3px);
  background-size:36px 36px; background-position:center;
  -webkit-mask-image:radial-gradient(125% 105% at 50% -5%, #000 50%, transparent 100%); }
```

Os números importam e são **deliberadamente discretos**:

- **Ponto de 1.1px**, fade até 1.3px — minúsculo.
- **Cor verde clara a alpha .055** — quase invisível, só insinua textura.
- **Tile de 36px** — espaçamento largo; não é um *halftone* denso, é um respiro.
- **Máscara radial** centrada no topo (`50% -5%`): a textura é mais forte em cima e **some** nas bordas e embaixo, evitando que ela compita com a moldura.

Esse é o exemplo canônico de mão leve: alpha .055 num ponto de 1px. Se você consegue "ver os pontos" sem procurar, está grosso demais — abaixe o alpha, não suba.

**Faça:** grão fino, alpha < ~.06, mascarado para sumir nas bordas. **Não faça:** ruído de filme grosso, granulado visível, textura que "chia".

---

### 3 · Moldura tracejada verde (assinatura recorrente)

A borda tracejada é o elemento mais reconhecível da marca — vem do tom "cheat sheet verde" do site e atravessa toda peça:

```css
.slide::after{ content:''; position:absolute; inset:38px; border:2px dashed var(--green);
  border-radius:32px; opacity:.38; pointer-events:none;
  box-shadow:inset 0 0 90px oklch(70% 0.13 152 / .05); }
```

Valores exatos: **inset 38px** (a moldura flutua para dentro da borda), **traço 2px dashed verde**, **raio 32px** (cantos generosos), **opacity .38** (presente, nunca gritando). O detalhe premium é o `box-shadow:inset 0 0 90px` num verde a alpha .05 — um **halo interno** levíssimo que faz a moldura "irradiar" para dentro em vez de ser só uma linha seca.

> No Story (carrossel) a moldura usa `inset:208px 60px` — recuada do topo/base para abrir espaço às zonas seguras do formato vertical. O dashed verde e o raio continuam.

**Faça:** moldura tracejada verde, inset ~38px, opacity ~.38, com halo interno suave. **Não faça:** borda sólida grossa, opacity 1.0, cantos retos.

---

### 4 · Número-fantasma (profundidade tipográfica)

O `.ghost` é um número gigante atrás do conteúdo, em **contorno** (só stroke, miolo transparente), que dá profundidade e ancora o olhar:

```css
.slide>.ghost{ position:absolute; font-family:'Hanken Grotesk'; font-weight:900; line-height:.74;
  color:transparent; -webkit-text-stroke:2px oklch(74% 0.09 152 / .09); pointer-events:none;
  letter-spacing:-.05em; z-index:0; overflow:hidden;
  -webkit-mask-image:radial-gradient(120% 120% at 50% 50%, #000 60%, transparent 100%); }
```

A receita: **miolo transparente** (`color:transparent`) + **stroke verde de 2px a alpha .09** — fantasmagórico, não preenchido. A **máscara radial** faz o número se dissolver nas pontas, como se emergisse da própria atmosfera do fundo. Está no `z-index:0`, abaixo de tudo. No carrossel, o número da edição (`.ed-num`) sobe o stroke para alpha .55 e ganha `text-shadow:0 0 70px` verde a .12 — mais presente porque ali ele é protagonista, não fantasma.

**Faça:** número grande em stroke translúcido (alpha ~.09), mascarado nas pontas, atrás do conteúdo. **Não faça:** número preenchido sólido competindo com o texto.

---

### 5 · Brilho / glow verde controlado (mão leve, sempre)

O glow é onde o amador exagera. No padrão ele aparece em **três lugares** e sempre fraco:

**a) Títulos — `text-shadow` verde.** A palavra-chave do título (`.lt`, em verde) ganha um halo:

```css
.head h1 .lt{ color:var(--green); text-shadow:0 0 50px oklch(72% 0.14 152 / .38); }
```

`0 0 50px` é um raio largo e difuso (não uma sombra dura) e o alpha .38 mantém o controle. No FLUXO o raio sobe para `56px`; na capa do carrossel chega a `60px` e no Story a `80px` — quanto maior o tipo, maior o raio, mas sempre alpha < ~.42. **A regra:** glow é raio grande + alpha baixo. Raio pequeno + alpha alto vira borrão sujo.

**b) Selos/ícones — `box-shadow` + `drop-shadow`.** O selo da marca e os selos de linha "irradiam":

```css
.brandmark .seal{ ... box-shadow:0 8px 22px oklch(60% 0.14 152 / .35); }
.row .seal{ ... box-shadow:0 0 34px oklch(70% 0.14 152 / .12), inset 0 1px 0 oklch(90% 0.1 152 / .12); }
.row .seal svg{ ... filter:drop-shadow(0 0 9px oklch(72% 0.14 152 / .4)); }
```

Dois sabores de sombra trabalham juntos: a **sombra de contato** (`0 8px 22px` — deslocada para baixo, ancora o selo no plano) e o **glow ambiente** (`0 0 34px` — radial, faz o selo brilhar). O `inset 0 1px 0` no topo é um **realce de luz** de 1px que simula a borda iluminada por cima. E o `drop-shadow` no SVG faz o próprio ícone emitir luz verde.

**c) Acento ouro — quando o selo é "estrela".** O selo `gold` troca o glow verde por ouro (`oklch(76% .11 83 / .16)`) e o ícone por `drop-shadow(0 0 10px oklch(80% .1 83 / .5))`. Mesma técnica, outra cor — o ouro é o único que pode interromper o verde (ver seção 01).

**Faça:** glow de raio largo, alpha baixo, escalado pelo tamanho do elemento. **Não faça:** `text-shadow:0 0 8px #3faf76` (raio curto + cor cheia = neon barato).

---

### 6 · Tratamento do objeto no compositing (fazer o objeto "sentar" na cena)

O objeto fotorrealista (capa, item da grade — detalhe na seção 04) precisa **pertencer** à atmosfera verde, não parecer colado por cima. Três tratamentos o assentam na cena:

| Tratamento | O que faz | Como (mesma família dos selos) |
|---|---|---|
| **Sombra de contato** | Ancora o objeto no plano — ele "toca" o fundo | `box-shadow` deslocada para baixo (ex.: `0 14px 40px oklch(60% .14 152 / .3)`, como nos cards do carrossel) |
| **Rim-light / glow verde** | Borda do objeto pega a luz verde da cena | `drop-shadow(0 0 ~12px verde)` + glow ambiente radial fraco |
| **Realce de topo** | Reflexo de 1px na aresta superior, simula luz vindo de cima | `inset 0 1px 0 oklch(90% .1 152 / .12)` |

O objeto é tratado como **duotone no mundo verde** (ver seção 01): a iluminação de cena que incide sobre ele é verde, a sombra que ele projeta é verde-escura. Assim ele não reintroduz o arco-íris — ele é da paleta. *(O duotone/grade do objeto em si é assunto da 04; aqui é só o tratamento de borda e o assentamento na cena.)*

**Faça:** sombra de contato (deslocada) + rim-light verde (radial) + realce de topo de 1px. **Não faça:** objeto sem sombra (flutuando) ou com sombra dura preta (recortado, falso).

---

### 7 · Scrims / overlays (texto sobre objeto ou imagem)

Quando texto **cai sobre** o objeto ou uma imagem, a legibilidade não pode depender da sorte do pixel embaixo. A solução cinematográfica é o **scrim**: um gradiente escuro **entre** a imagem e o texto, que garante o contraste.

O princípio (introduzido aqui; a seção **08** aprofunda a leitura): um `linear-gradient` de transparente → escuro, do lado onde o texto se assenta, abaixado **sob** o texto e **sobre** a imagem. A própria vinheta do `.slide` (camada 3 do fundo) já é um scrim de borda — escurece os cantos, que é justo onde rótulos e marca-d'água costumam ficar (`.wm`, `@minutoreal1701`). Para texto sobre objeto, replique a lógica localmente: um gradiente escuro verde-quase-preto na base do bloco de texto.

A regra de ouro do scrim é a mesma de tudo aqui: **escuro o suficiente para o texto passar WCAG, leve o suficiente para a imagem ainda respirar.** O scrim não pode virar uma tarja preta opaca que mata o objeto. *(Os limiares de contraste e os casos difíceis ficam na 08.)*

**Faça:** scrim em gradiente sob todo texto que pousa sobre imagem. **Não faça:** texto cru sobre objeto torcendo para o fundo ajudar; nem tarja preta sólida que apaga a foto.

---

### A filosofia "mão leve"

Todos os valores desta seção apontam para a mesma direção. Junte-os e o padrão fica claro:

| Efeito | Valor real (premium) | O erro de amador |
|---|---|---|
| Grão | ponto 1.1px, alpha **.055** | ruído grosso, alpha alto |
| Moldura | dashed, opacity **.38** | sólida, opacity 1.0 |
| Número-fantasma | stroke alpha **.09** | número preenchido sólido |
| Glow de título | raio **50px**, alpha **.38** | raio 8px, cor cheia (neon) |
| Glow de selo | `0 0 34px`, alpha **.12** | sombra dura preta |
| Vinheta | verde-escuro alpha **.6** | sem vinheta (cantos chapados) |

Repare: **quase nenhum alpha passa de ~.4, e os raios são sempre largos.** Esse é o DNA do premium. O efeito tem que estar lá — a peça sem ele fica pobre — mas você não deve *perceber* cada efeito individualmente. Você percebe o **resultado**: profundidade, atmosfera, "isso parece de catálogo". Se um efeito chama atenção para si mesmo, ele está alto demais. Premium é o acabamento que você sente sem conseguir apontar.

---

### Faça / Não faça (acabamento)

| ✅ Faça | ❌ Não faça |
|---|---|
| Fundo em 4 camadas (2 glows verdes + vinheta + base) | Fundo de cor sólida chapado |
| Grão fino (ponto ~1px, alpha ~.055), mascarado nas bordas | Ruído grosso, granulado visível |
| Moldura tracejada verde, inset 38px, raio 32px, opacity .38 | Borda sólida grossa, cantos retos |
| Número-fantasma em stroke translúcido (alpha ~.09), mascarado | Número preenchido competindo com o texto |
| Glow de raio largo (~50px+) e alpha baixo (< ~.4), escalado pelo tipo | Glow de raio curto + cor cheia (neon barato) |
| Selo/objeto com sombra de contato **+** glow ambiente **+** realce de 1px | Sombra dura preta única (recorte falso) |
| Objeto como duotone verde, rim-light verde, assentado na cena | Objeto colado sem sombra (flutuando) |
| Scrim em gradiente sob texto que pousa sobre imagem | Texto cru sobre foto; ou tarja preta opaca |
| Manter quase todo alpha < ~.4 — controle é a marca do premium | Subir alphas "para aparecer mais" |
| Puxar a cor dos efeitos da paleta verde (hue 152) / ouro (hue 83) | Glow azul/roxo/branco-puro que foge da marca |
