## 06. Catálogo por Tipo de Peça

> *O inventário da rede, peça por peça. Cada formato resolve um trabalho diferente — mas todos vestem a **mesma pele** (a paleta de **01**, a tipografia de **02**, a anatomia genérica de **03**, o objeto fotorrealista de **04** e o acabamento de **07**). Aqui descrevemos só o que **muda** de um tipo para o outro: o layout, o papel, e onde entra o objeto. Nada de reescrever a pele — ela é referenciada, não duplicada.*

**Fonte de verdade desta seção:** `gerar_infografico.py` (arquétipos + dimensões), `gerar_carrossel.py` (carrossel, stories, citação) e `gerar_dados_kit.py` (peças do kit: `ASSET_META` / `ASSET_ORDER`). Toda dimensão abaixo foi lida desses arquivos. Se um valor divergir do código, o código vence.

---

### 06.1 — Infográficos (1080×1350 · 4:5 · Instagram feed)

Os cinco arquétipos densos de `gerar_infografico.py`. Todos saem em **4:5 (1080×1350)**, cada um renderizado numa página isolada (`BASE_CSS` + só o CSS daquele arquétipo) para não haver vazamento de estilo. A **LISTA** é universal (sai de qualquer livro, dos `CHAPTERS`); os outros quatro são **curados** — só saem se o `<slug>_data.py` traz o dict correspondente (`FLUXO`, `COMPARA`, `NUMEROS`, `ANATOMIA`), senão o arquétipo é pulado.

#### LISTA — "Mapa do livro" (universal)

- **Papel:** o livro inteiro em uma página. Um nó por capítulo/lei, com rótulo + primeira frase da introdução do capítulo + chip do número do capítulo. É a peça-base do acervo (rodapé: *"o livro inteiro em 1 página"*).
- **Estrutura:** cabeçalho (badge "Mapa do livro" + título-herói `header_light` verde / `header_bold` claro + promessa) → **grade de ~6 linhas** (amostragem uniforme dos capítulos via `_even_sample`) separadas por divisória tracejada → rodapé "Na prática" (selo verde + dica) → marca d'água `@minutoreal1701`.
- **Objeto fotorrealista:** **SIM — 1 por linha.** Cada linha tem um **selo** (`.row .seal`, 84×84, cantos 22px) que hoje carrega o ícone de linha do card (`ic`). **É exatamente o slot onde o objeto-símbolo do capítulo entra** (ver **04**): a coroa, a corrente, o prisma — um por nó, tingido no mundo verde. A última linha é a **dourada** (`tone == 'gold'`): selo e chip viram ouro — o destaque único da peça.
- **Destaque/observações:** os tons ciclam `soft → mid → deep` dentro do verde (hierarquia **sem** sair do hue 152); só a última linha rompe para ouro. Tem auto-fit de altura (`.fitv`): se a grade estoura, a fonte encolhe até caber. É a mesma LISTA reaproveitada pelo kit como `mapa.html` (ver 06.5).

#### FLUXO — passos / linha do tempo (curado: campo `FLUXO`)

- **Papel:** um processo em etapas numeradas (passo 1 → 2 → 3…), ligadas por uma linha tracejada vertical. Para "como fazer X" em sequência.
- **Estrutura:** topbar (marca + autor) → kicker + título → **coluna de passos**, cada um com selo redondo (108×108) contendo o **número** + ícone, e corpo com lei/rótulo/descrição → rodapé "Na prática · comece hoje".
- **Objeto fotorrealista:** **SIM — 1 por etapa**, no selo redondo de cada passo (`.flow .seal .ic`), abaixo do número-herói. O objeto ilustra a ação daquela etapa.
- **Destaque:** o passo-chave pode ser marcado `gold` (coroa "Passo-chave" + selo/linha em ouro). Numeral-fantasma `→` ao fundo. Um só passo dourado por peça.

#### COMPARA — duas colunas X × Y (curado: campo `COMPARA`)

- **Papel:** confronto de dois caminhos — **evite (lado A)** × **faça (lado B)**. O quadro do "antes/depois", "erro/acerto".
- **Estrutura:** cabeçalho centrado → **moldura de 2 colunas** com um selo **"vs"** dourado no centro → cada coluna tem selo + tag + rótulo + lista de itens → veredito dourado no rodapé ("Na prática").
- **Objeto fotorrealista:** **SIM — 1 por lado** (`.col-seal`, 88×88), com um **carimbo** sobreposto: **✕** (cruz) no lado A e **✓** (check) no lado B. O lado A usa **verde-deep** (o tom mais sóbrio do verde, para "o que evitar"); o lado B usa o **verde** pleno (o recomendado). A diferença entre os lados é **forma + ícone + carimbo**, nunca matiz fora do verde.
- **Destaque:** o único ouro é o disco "vs" central + o veredito — coerente com a regra "um ouro por peça". Numeral-fantasma "VS" ao fundo.

#### NUMEROS — números-herói + mini-viz (curado: campo `NUMEROS`)

- **Papel:** os dados do livro em destaque. Cada estatística é um número gigante (até 104px) com ícone, rótulo e contexto; opcionalmente uma **mini-visualização** on-brand.
- **Estrutura:** topbar + tag → kicker + título + autor → **lista de stats** (ícone + número-herói + rótulo/contexto) → bloco **viz** opcional → rodapé "Na prática".
- **Objeto fotorrealista:** **SIM — o ícone de cada stat** (`.stat .ic`, 80×80) é o slot do objeto; e a **mini-viz** é a "coisa" da peça. A viz tem dois tipos prontos: **`curve`** (curva exponencial verde subindo vs. linha plana cinza, com ponto-ouro no fim — juros compostos / crescimento) e **`bar`** (barra empilhada: fatia pequena em verde-deep × fatia dominante em ouro). Ambas já vêm na paleta da marca — verde + um ouro, nada de arco-íris.
- **Destaque:** a stat-estrela (`star: true`) vira **dourada** (número, ícone e contexto em ouro) — o único realce premium. Numeral-fantasma "%" ao fundo.

#### ANATOMIA — anel de nós com hub central (curado: campo `ANATOMIA`)

- **Papel:** a estrutura interna de um conceito como um **ciclo de 4 nós** (N, E, S, O, sentido horário) em torno de um hub central, com callouts numerados nos quatro cantos. Para sistemas, ciclos, frameworks de 4 partes.
- **Estrutura:** topbar (marca + pílula "Anatomia") → cabeçalho (autor + h1 + sub) → **palco SVG** com o anel, setas em arco entre os nós, conectores tracejados aos callouts e número em disco verde por callout → rodapé "Na prática".
- **Objeto fotorrealista:** **SIM — 1 por nó** (`_an_node`, círculos de raio 58 com o ícone dentro), **mais o hub central** que carrega o nome do conceito. São os quatro objetos-símbolo do framework dispostos no anel.
- **Destaque:** é o arquétipo mais "diagramático" — usa SVG real com `foreignObject` para os callouts. Tudo monocromático verde; o hub central é o âncora semântico.

---

### 06.2 — Carrossel do Instagram (1080×1350 · 4:5 · multi-slide)

De `gerar_carrossel.py`. Um carrossel = o livro em N ideias (ou um capítulo). Sequência: **capa → N slides de conceito → CTA**. Cada slide é 4:5, com a pele completa (fundo em camadas, moldura tracejada, grade de pontos, numeral-fantasma, **indicador de progresso** em dots no rodapé).

#### CAPA (slide 1)

- **Papel:** o anúncio do livro "para o dedo" — para a pessoa parar de rolar. Wordmark forte no topo, título-herói gigante (124px), autor, gancho ("N ideias que ficam") e a affordance **"arrasta"** (pílula verde, perto do polegar).
- **Objeto fotorrealista:** **SIM — o objeto-símbolo do livro, grande e central** (ver **04**). É a única peça onde o objeto vira protagonista de tela cheia, não item de grade. A coroa de *O Príncipe*, o prisma de *48 Leis* — o símbolo que diz de que livro se trata antes da leitura.
- **Destaque:** o gancho numérico usa o **ouro** (`#d8a64a`) — único acento da capa. A swipe-pill verde é a affordance principal (Krug: o que fazer a seguir deve ser óbvio).

#### CARDS DE CONTEÚDO (slides 2…N) — padrão editorial "quente"

- **Papel:** uma ideia por slide, em layout **editorial** (estilo "A Pergunta Defensiva"): numeral-romano em outline (Literata, 300px) + kicker + fonte do capítulo + título serifado + corpo com **capitular** (drop-cap) + caixa de dica/cuidado. O corpo é cortado pelo `_lead` para 1–2 frases escaneáveis (contrato Krug: o slide é billboard, a prosa inteira vive no site).
- **Objeto fotorrealista:** **SIM — vários objetos-cena cinematográficos.** Este é o slide onde o padrão pede **objetos-cena** (não um único símbolo): a cena montada que ilustra a ideia, no acabamento de **07**. O selo de ícone (`.card-icon`, 108×108) é o ponto de ancoragem on-brand.
- **Destaque:** cards de aviso usam a classe `.warn` → o **alerta** (`#e8744f`) substitui o verde **só** ali (ícone shield, "Cuidado"). É a exceção semântica de **01**, não decoração. Auto-fit reduz a fonte do corpo se a caixa estoura.

#### CITAÇÃO (cards `--citacao` / `quote`)

- **Papel:** a frase-bomba do livro, grande. Aspas serifadas gigantes (Literata itálico, 280px), a frase em destaque (66px), atribuição (autor + título) e rodapé "salve esta". As frases são extraídas e pontuadas por `_best_quotes`/`_score` (curtas, com travessão/contraste, sem perguntas).
- **Objeto fotorrealista:** **SUTIL — objeto de fundo.** A citação privilegia a tipografia; o objeto entra **discreto**, ao fundo, sem competir com a frase (aqui o numeral-fantasma é a aspa `"`). O punch da frase (após o último travessão) é realçado em **verde** via `_emph`.
- **Destaque:** é a peça mais tipográfica da rede — serif soberana. Single ou multi-card (com contador `NN/NN`).

---

### 06.3 — Stories 9:16 (1080×1920 · vertical)

De `gerar_carrossel.py` (`STORY_CSS`). Mesma pele, formato vertical, com **zona segura**: o conteúdo vive no miolo (`padding: 300px 100px`) deixando topo/rodapé (~290px) livres para a UI do Instagram. Wordmark fixo no topo, CTA-pill verde no rodapé.

| Frame | Peça | Papel | Objeto |
|---|---|---|---|
| `capa-story` | **Capa (story)** | Anúncio vertical do livro: eyebrow "novo · resumo da semana" + título-herói (158px) + gancho "N ideias que ficam" + tap "toque no link da bio" | Numeral-fantasma `N` grande ao fundo; objeto-símbolo do livro como na capa do carrossel |
| `citacao-story` | **Citação (story)** | A mesma frase-bomba do carrossel, layout vertical (aspa 300px + frase 88px + atribuição) | Objeto sutil ao fundo (aspa-fantasma); tipografia soberana |

- **Como veste o padrão:** é literalmente a **mesma pele** do carrossel, re-encaixada no 9:16. O título usa o mesmo `header_light`/`header_bold` verde/claro; o gancho numérico usa o **ouro**.
- **Observação:** existe ainda um `_story_cta` (frame "tudo em 1 toque": Acervo / YouTube / Amazon) usado pelo fluxo `--stories`; o kit publica `capa-story` e `citacao-story` como peças.

---

### 06.4 — Capa / Thumbnail do YouTube (1280×720 · 16:9)

De `gerar_dados_kit.py` (`THUMB_CSS`, `_thumb_fragment`). **16:9 (1280×720)** — alto contraste, legível em miniatura.

- **Papel:** a thumbnail do vídeo-resumo. Wordmark + eyebrow "o livro em ~5 min" + título-herói gigante (118px) + rodapé com o **número de ideias** em ouro (96px) + "ideias que ficam com você".
- **Como veste o padrão:** mesma pele (gradientes em camadas, moldura tracejada, numeral-fantasma gigante de 520px ao fundo), recortada para o 16:9. Verde lidera o título (`.lt`), o **ouro** carrega o número de ideias — o único acento.
- **Objeto fotorrealista:** **SIM — o objeto-símbolo do livro**, grande, no estilo de capa (ver **04**). O brief pede o título tratado como **3D em vidro/prata** sobre **textura (carbono/circuito)** + número de ideias + objeto-símbolo. O CSS atual entrega a base on-brand (numeral-fantasma + título-herói + número-ouro); o tratamento 3D/textura é a camada de **acabamento (07)** aplicada por cima, sem trocar a paleta.
- **Destaque:** é a peça de **maior contraste** (precisa ler em miniatura no feed do YouTube) — números e título maiores, respiro menor. Legibilidade em escala reduzida é a prova (ver **08**).

---

### 06.5 — Peças do Kit (estáticas, sob demanda)

De `gerar_dados_kit.py` (`ASSET_META` / `ASSET_ORDER`). São os `_tpl` que o `server.js` fotografa sob demanda (png+webp) e cacheia. A ordem de exibição na UI é `ASSET_ORDER = [mapa, ideia, citacao-feed, citacao-story, capa-story, thumb]`, com o carrossel do livro entrando antes, à parte.

#### Ideia-chave (1080×1080 · 1:1 · Instagram feed)

- **Papel:** a carta **mais forte** do livro virada peça de feed quadrada. `_pick_idea` escolhe o card com dica + maior corpo (o mais profundo). Layout editorial: tag "Ideia-chave" + kicker + título (72px) + corpo com **capitular** (118px) + caixa de dica.
- **Objeto fotorrealista:** **SIM — o objeto-símbolo daquela ideia** (ver **04**), na mesma gramática editorial dos cards de conteúdo do carrossel. Reusa o cromo quente de `gerar_carrossel`, então não há deriva.
- **Destaque:** é a peça quadrada (1:1) — única razão de aspecto entre as do kit. Rodapé com a URL do acervo.

#### Citação (feed) (1080×1350 · 4:5)

- **Papel:** a citação no formato de feed 4:5. É **literalmente** o `_quote_card` do carrossel (06.2 → CITAÇÃO) emitido como peça única — zero deriva.
- **Objeto fotorrealista:** **SUTIL — objeto de fundo**, como toda citação (a tipografia serifada lidera).
- **Destaque:** `citacao-story` (06.3) é a irmã vertical 9:16 da mesma frase.

> O kit também emite `mapa.html` (= a **LISTA** de 06.1, 4:5, universal), `capa-story` e `citacao-story` (= 06.3) e `thumb` (= 06.4). Ou seja: **as peças do kit não são formatos novos — são os arquétipos já descritos acima, emitidos como `_tpl` estáticos e cacheados.**

---

### 06.6 — CTA "Gostou? Tem mais"

Slide final do carrossel (`_cta` em `gerar_carrossel.py`), 4:5. O brief o descreve como **painel premium skeuomórfico** com botão verde "SALVE", knobs/LED.

- **Papel:** fechar o carrossel convertendo a atenção em ação: 3 destinos (acervo/cheat sheet + PDF, YouTube ~5 min, seguir @minutoreal1701) + botão **"Salve para revisar"**.
- **Estrutura atual:** título "Gostou? **tem mais.**" (verde) → 3 linhas (ícone em selo + frase, com a palavra-chave em verde-soft) → botão **save** verde (pílula, ícone bookmark) → handle → numeral-fantasma `+` ao fundo.
- **Como manter na paleta (skeuomorfismo on-brand):** o tratamento "painel premium / knobs / LED" do brief é **acabamento (07)** aplicado sobre esta estrutura — e tem de respeitar **01**: o botão "SALVE" é **verde** (`--green` sobre `--on-green`), os LEDs/realces "acesos" usam **verde-soft** (não um vermelho/azul de painel), e o **único ouro** vai no detalhe de destaque (selo premium), nunca espalhado pelos knobs. Skeuomorfismo sim; arco-íris de equipamento eletrônico, não. A cor nunca é o único sinal: cada destino tem ícone + rótulo, não só matiz.
- **Observação:** o Stories tem seu próprio CTA (`_story_cta`, "tudo em 1 toque", os 3 destinos verticais) — mesmo papel, formato 9:16.

---

### Tabela-resumo

| Tipo | Arquivo | Formato | Dimensão | Usa objeto? | Texto principal | Acento |
|---|---|---|---|---|---|---|
| **LISTA / Mapa** | `gerar_infografico.py` · `mapa.html` | 4:5 | 1080×1350 | **Sim** — 1 por capítulo (no selo da linha) | Título-herói + grade de capítulos | Ouro: última linha |
| **FLUXO** | `gerar_infografico.py` | 4:5 | 1080×1350 | **Sim** — 1 por etapa (selo redondo) | Passos numerados | Ouro: passo-chave |
| **COMPARA** | `gerar_infografico.py` | 4:5 | 1080×1350 | **Sim** — 1 por lado (+ ✕/✓) | 2 colunas: evite × faça | Ouro: disco "vs" + veredito |
| **NUMEROS** | `gerar_infografico.py` | 4:5 | 1080×1350 | **Sim** — ícone + mini-viz | Números-herói | Ouro: stat-estrela + viz |
| **ANATOMIA** | `gerar_infografico.py` | 4:5 | 1080×1350 | **Sim** — 1 por nó + hub | Anel de 4 nós + callouts | Verde (hub central) |
| **Carrossel · Capa** | `gerar_carrossel.py` | 4:5 | 1080×1350 | **Sim** — símbolo do livro (grande) | Título-herói + "arrasta" | Ouro: gancho numérico |
| **Carrossel · Conteúdo** | `gerar_carrossel.py` | 4:5 | 1080×1350 | **Sim** — objetos-cena | Editorial: nº romano + ideia | Alerta (só `.warn`) |
| **Carrossel · Citação** | `gerar_carrossel.py` | 4:5 | 1080×1350 | **Sutil** — fundo | Frase-bomba serifada | Verde: punch da frase |
| **Capa (story)** | `gerar_carrossel.py` (`STORY_CSS`) | 9:16 | 1080×1920 | **Sim** — símbolo do livro | Título-herói + tap | Ouro: gancho numérico |
| **Citação (story)** | `gerar_carrossel.py` (`STORY_CSS`) | 9:16 | 1080×1920 | **Sutil** — fundo | Frase-bomba serifada | Verde: punch |
| **Ideia-chave** | `gerar_dados_kit.py` | 1:1 | 1080×1080 | **Sim** — símbolo da ideia | Editorial: título + corpo | Verde lidera |
| **Citação (feed)** | `gerar_dados_kit.py` (= `_quote_card`) | 4:5 | 1080×1350 | **Sutil** — fundo | Frase-bomba serifada | Verde: punch |
| **Thumbnail YouTube** | `gerar_dados_kit.py` (`THUMB_CSS`) | 16:9 | 1280×720 | **Sim** — símbolo do livro | Título-herói + nº de ideias | Ouro: número de ideias |
| **CTA "Tem mais"** | `gerar_carrossel.py` (`_cta`) | 4:5 | 1080×1350 | Opcional | "Gostou? tem mais." + 3 destinos | Verde (botão SALVE) |

---

### Nota de coerência

Todos os tipos acima compartilham a **PELE UNIVERSAL** — a paleta de **01**, a tipografia de **02**, a anatomia genérica de **03**, o objeto fotorrealista de **04** e o acabamento de **07**. Só o **layout** muda de um tipo para outro: a grade da LISTA, a linha do tempo do FLUXO, as colunas do COMPARA, os números do NUMEROS, o anel da ANATOMIA, o ritmo de slides do carrossel, a verticalidade do Story, o alto contraste da thumbnail. No código isso é garantido por **páginas isoladas** (`BASE_CSS`/pele compartilhada + só o CSS do tipo), de modo que não há vazamento de estilo. Por isso uma thumbnail 16:9 e um card de citação 4:5 **parecem irmãos** mesmo tendo esqueletos completamente diferentes: a pele os reconhece como família; o layout deixa cada um resolver bem o seu trabalho. **Esta seção especializa por tipo; quem governa a pele são 01/02/03/07 — referencie-as, não as reescreva.**
