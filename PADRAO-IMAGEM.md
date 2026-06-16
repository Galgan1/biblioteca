# Bíblia do Padrão de Imagem — Minuto Real / Biblioteca

> **A regra única de como TODA imagem que produzimos deve parecer.** Premium, cinematográfica, coerente. Uma peça nossa deve ser reconhecível em 0,5 segundo no feed — antes de o olho ler uma palavra.

| | |
|---|---|
| **Versão** | 1.0 |
| **Data** | 2026-06-16 |
| **Dono** | Diretor de Design (lane de unificação da rede, nomeada 14/jun/2026) |
| **Fonte única de cor/fonte** | [`marca.py`](marca.py) |
| **Guardrail** | [`check_marca.py`](check_marca.py) — rode `python check_marca.py` |
| **Geradores** | [`gerar_infografico.py`](gerar_infografico.py), [`gerar_carrossel.py`](gerar_carrossel.py), [`gerar_dados_kit.py`](gerar_dados_kit.py), [`videos/imagen.py`](videos/imagen.py) |

**Como ler esta bíblia.** Toda peça é construída em **duas camadas**: a **PELE UNIVERSAL** (a atmosfera que toda peça veste — cor, tipografia, acabamento) e o **LAYOUT POR TIPO** (o esqueleto de cada formato). As seções **01–02** e **07–08** descrevem a pele; **03–06** descrevem os layouts; **00** e **09** são a doutrina e a governança que costuram tudo. Quando um valor desta bíblia divergir do código, **o código vence** — e a bíblia é corrigida.

---

## Sumário

| # | Seção | Camada |
|---|---|---|
| **00** | Norte & Filosofia | doutrina |
| **01** | Paleta & Cor | pele |
| **02** | Tipografia | pele |
| **03** | Anatomia da Peça (DNA do Layout) | layout |
| **04** | O Objeto Fotorrealista | layout · o coração |
| **05** | Molde de Prompt | layout |
| **06** | Catálogo por Tipo de Peça | layout |
| **07** | Acabamento Cinematográfico | pele |
| **08** | Legibilidade & Acessibilidade | pele |
| **09** | Governança, Checklist & Guardrail | governança |

---

## 00. Norte & Filosofia

> *A bíblia do padrão de imagem da rede Minuto Real / Biblioteca. Esta é a seção que abre o documento — o manifesto. As nove seções seguintes detalham o "como"; esta estabelece o "porquê" e a doutrina que governa todas as outras.*

### Por que este documento existe

Produzimos imagens para 92+ livros, em quatro frentes (feed e carrossel do Instagram, Stories, thumbnail do YouTube) e em ritmo de esteira. Sem uma regra única, cada peça vira uma decisão nova: outro verde, outra fonte, outro jeito de tratar o acento. O resultado seria um acervo que *parece* de marcas diferentes — e marca que não se reconhece não constrói equity.

A meta deste documento é uma só, e é mensurável: **uma peça nossa deve ser reconhecível em 0,5 segundo no feed**, antes de o olho ler uma palavra. O leitor passa o polegar, bate o olho, e *sabe* que é Minuto Real — pela cor, pela atmosfera, pelo acabamento. Essa coerência é o que separa um catálogo premium de uma pilha de posts.

A bíblia existe para tornar isso **automático e repetível**. Ela não é um moodboard inspiracional; é a fonte de verdade que alinha o gerador (`gerar_infografico.py`, `gerar_carrossel.py`), os tokens (`marca.py`) e o guardrail (`check_marca.py`). Quando a regra está escrita, a máquina executa e o humano só aprova.

### A alma que copiamos — e o arco-íris que não copiamos

A referência viva são os **infográficos densos de catálogo**: o "Guia rápido: fusíveis do carro", o "Tipos de fita e quando usar cada uma". O que admiramos neles não é o assunto — é a **densidade elegante**: muita informação organizada numa única imagem, sem virar bagunça. O DNA desse gênero é claro:

1. **Cabeçalho/título forte** que ancora a peça.
2. Uma **grade de itens**, cada um com um **objeto renderizado de verdade** (a "coisa", fotorrealista).
3. **Rótulo + descrição curta** por item.
4. Um bloco prático — **ícone + "USO:"**.
5. Um **rodapé de aviso** ("DICA" / "IMPORTANTE").
6. **Acabamento cinematográfico**: luz, profundidade, grão, vinheta.

Essa é a **alma**. Para nós, o "objeto" deixa de ser um fusível e passa a ser um **objeto-símbolo do livro**: coroa = poder, correntes = dependência, prisma = tática. Mas a estrutura — cabeçalho, grade, descrição, USO, rodapé, acabamento — é exatamente a que copiamos.

**O que NÃO copiamos é a paleta arco-íris.** As referências usam uma cor por categoria — vermelho, azul, amarelo, verde, tudo junto. Isso é morte para a marca: vira ruído, e nada se reconhece. Vestimos a mesma alma na **nossa** roupa:

> **Verde (hue 152) lidera. Um único ouro (hue 83, `#d8a64a`) é o acento. Mais nada.**

E a regra que sustenta isso: **a cor nunca é o único sinal.** Toda distinção vem acompanhada de ícone, forma ou rótulo — nunca só de matiz. É o que nos deixa monocromáticos *e* legíveis ao mesmo tempo (e acessíveis a quem não distingue cores).

### O modelo de 2 camadas — a espinha de toda a bíblia

Esta é a ideia central que organiza tudo o que vem depois. Toda peça da rede é construída em **duas camadas independentes**:

#### (A) PELE UNIVERSAL — o que toda peça veste

A **atmosfera comum**: a paleta (verde-mãe + ouro), a tipografia (Hanken Grotesk + Literata), o fundo escuro-papel (`#08080c`), a moldura tracejada verde, a grade de pontos, o número-fantasma e o acabamento cinematográfico (luz, profundidade, grão, vinheta).

A pele é o que faz **um carrossel e uma thumbnail parecerem irmãos**, mesmo tendo layouts completamente diferentes. É a camada do reconhecimento de 0,5 s. Ela é constante, governada por `marca.py`, e **não negociável** entre formatos. No código, ela vive no `BASE_CSS` compartilhado e nos tokens de marca.

#### (B) LAYOUT POR TIPO — a estrutura sob a pele

Por baixo da pele, cada formato tem sua **própria arquitetura**: a grade de itens da LISTA, a linha do tempo do FLUXO, as duas colunas do COMPARA, os números-herói do NUMEROS, os callouts da ANATOMIA — e, fora dos infográficos, o ritmo de slides do carrossel ou a hierarquia de uma thumbnail.

O layout é o **esqueleto que muda** conforme a informação a transmitir. No código, cada arquétipo é renderizado numa **página isolada** (`BASE_CSS` + só o CSS daquele tipo), de modo que **não há vazamento de estilo** entre formatos — a pele é compartilhada, o esqueleto é local.

#### Por que separar assim

A separação é o que nos dá **coerência e variedade ao mesmo tempo**. A pele garante que tudo pertença à mesma família; o layout garante que cada formato resolva bem seu trabalho. Trocar a cor-mãe é mexer em **uma** camada (a pele, em um arquivo) e propagar para 92 livros. Criar um formato novo é desenhar **um** esqueleto novo sob a pele que já existe. As seções desta bíblia mapeiam direto nessas duas camadas: 01–02 e 07–08 descrevem a **pele**; 03–06 descrevem os **layouts**; 00 e 09 são a doutrina e a governança que costuram as duas.

### Os princípios de marca

| Princípio | O que significa na prática |
|---|---|
| **Premium** | Nada de aparência "feita por IA" ou template genérico. Cada peça tem acabamento de catálogo editorial. |
| **Cinematográfico** | Luz, profundidade, grão e vinheta. A imagem tem *atmosfera*, não é flat design. |
| **Denso, mas legível** | Muita informação numa imagem — como as referências — sem nunca sacrificar a leitura. Densidade é a meta; ilegibilidade é o erro. |
| **Verde lidera** | O verde-mãe (hue 152) é a identidade. Domina a peça; o resto se subordina. |
| **Objeto > ícone** | O alvo é o **objeto fotorrealista** por conceito, não o ícone de linha. O ícone é a etapa intermediária; o objeto renderizado é a alma. |
| **Mono, não arco-íris** | Uma cor-mãe + um acento. Categorias se distinguem por ícone/forma/rótulo, jamais por uma paleta multicor. |
| **A cor nunca é o único sinal** | Acessibilidade e clareza: todo sinal de cor vem dobrado com forma, ícone ou texto. |
| **Gera-uma-vez + cache** | O objeto fotorrealista é caro de gerar. Gera-se uma vez por conceito, tinge-se na nossa cor e guarda-se. O custo é pago uma vez; o ativo se reusa. |

### A promessa visual da rede Minuto Real

Quando alguém vê uma peça nossa, a promessa entregue é:

- **"Isto é sério."** O acabamento premium sinaliza que o conteúdo por baixo também é cuidado — destilamos grandes livros com respeito.
- **"Isto é a Biblioteca."** O verde e o ouro são reconhecidos antes da leitura. A marca chega antes da palavra.
- **"Vou aprender algo aqui."** A densidade elegante promete substância, não enchimento — uma imagem que recompensa o tempo de leitura.

Toda decisão visual nesta bíblia serve a essas três promessas. Quando uma escolha não as serve, a escolha está errada.

### Os Mandamentos

1. **Verde lidera; ouro é o único acento.** Sem terceira cor de marca.
2. **A alma do catálogo, nunca o arco-íris.** Copiamos a densidade; rejeitamos a paleta multicor.
3. **A cor nunca é o único sinal.** Todo sinal de cor anda acompanhado de ícone, forma ou rótulo.
4. **Objeto fotorrealista vence ícone de linha.** O ícone é a ponte; o objeto-símbolo é o destino.
5. **Denso, mas sempre legível.** Densidade é virtude; ilegibilidade é falha.
6. **A pele é universal; o layout é por tipo.** Uma atmosfera para todos; um esqueleto para cada formato.
7. **`marca.py` é a fonte única de verdade.** Cor e fonte se leem dos tokens — nunca se hardcodam na peça.
8. **Gera uma vez, reusa sempre.** O objeto caro é cacheado; o pipeline é local e barato.

---

## 01. Paleta & Cor

A referência canônica de cor do padrão Minuto Real / Biblioteca. **Fonte de verdade:** `marca.py` (dicionário `TOKENS`) e a doutrina escrita no topo desse arquivo. Nada aqui é inventado — todo HEX e OKLCH abaixo foi confirmado em `marca.py`; toda razão de contraste foi medida por `check_marca.py`. Se um valor divergir do código, o código vence. **Não crie tokens novos.**

### A paleta DARK (canvas escuro — o padrão de toda peça de rede/vídeo)

Cada token de `marca.py` carrega três valores: `(oklch claro, oklch escuro, hex p/ Pillow no canvas escuro)`. Para o canvas escuro usamos o **índice [1] (OKLCH escuro)** no CSS e o **índice [2] (HEX)** no Pillow.

| Token (`marca.py`) | Papel / uso | OKLCH (escuro, índice [1]) | HEX (Pillow, índice [2]) |
|---|---|---|---|
| `papel` | Fundo do canvas — o "papel" escuro de tudo | `oklch(16% 0.01 152)` | `#08080c` |
| `tinta` | Texto principal (corpo, títulos) | `oklch(95% 0.01 152)` | `#f2f2f5` |
| `tinta-fraca` | Texto secundário, legendas, rótulos fracos | `oklch(72% 0.01 152)` | `#9aa0a2` |
| `verde` | **Cor-mãe.** UI, ícones de linha, traço tracejado, rótulos | `oklch(70% 0.13 152)` | `#3faf76` |
| `verde-deep` | Verde profundo — hierarquia/realce dentro do verde | `oklch(76% 0.11 152)` | `#5cc28a` |
| `verde-soft` | Verde menta — texto sobre fundo, brilhos suaves | `oklch(28% 0.04 152)` | `#a9e6c4` |
| `ouro` | **Acento único.** Destaque, CTA, "estrela", selo premium | `oklch(76% 0.105 83)` | `#d8a64a` |
| `ouro-soft` | Ouro suave — gradiente/halo do ouro, estado secundário | `oklch(86% 0.075 83)` | `#ecca8c` |
| `alerta` | **Só avisos.** Rodapé "IMPORTANTE", caução, perigo | `oklch(72% 0.16 30)` | `#e8744f` |

> O canvas escuro é o padrão. O modo claro (índice [0] do mesmo token) existe só para o site, com o ouro real fixo em **`#d8a64a`** — a âncora de marca.

### A doutrina (decidida em 14/jun/2026 — está escrita no topo de `marca.py`)

Três frases governam toda decisão de cor:

1. **Verde (hue 152) é a cor-mãe e lidera.** É a identidade da Biblioteca. O verde aparece no traço tracejado, nos ícones de linha, nos rótulos, na UI. Quando você está em dúvida sobre que cor usar, a resposta padrão é **verde**.
2. **UM ouro (hue 83) é o único acento premium.** Ancorado no âmbar **`#d8a64a`**, que já carrega o *equity* visual do YouTube do canal. Não há um segundo acento. Não existe "azul de apoio", "roxo de seção", nem nada disso. Ouro é a única voz que pode interromper o verde.
3. **Alerta (hue ~30, `#e8744f`) é exceção rara.** Existe só para o registro de aviso ("IMPORTANTE", caução, perigo). Não é decoração; é semântica.

A âncora **`#d8a64a`** é tão central que `check_marca.py` proíbe hardcodá-la nos geradores: o código deve sempre puxar `marca.hex_of("ouro")`. Isso garante que mudar a marca seja mudar **um** valor, em **um** arquivo.

### Proporção de cor (o "orçamento" cromático de uma peça)

A peça é predominantemente escura e verde; o ouro é um tempero, não um ingrediente.

| Faixa | Papel | Onde |
|---|---|---|
| **~70%** | Neutros escuros (`papel`, `tinta`, `tinta-fraca`) | Fundo, corpo de texto, grades, respiro |
| **~20–25%** | Verde (`verde`, `verde-deep`, `verde-soft`) | Traço, ícones, rótulos, hierarquia, brilhos |
| **< ~10%** | Ouro (`ouro`, `ouro-soft`) | **Só** o ponto de destaque: CTA, a "estrela" da grade, o selo premium |
| **Raríssimo** | Alerta (`alerta`) | Só o registro de aviso, quando ele de fato existir |

Regra prática: **um único ouro por peça** na maioria dos casos. Se há ouro em três lugares, ele deixou de ser destaque e virou ruído — escolha o um que mais importa e devolva os outros ao verde.

### Rejeição explícita do arco-íris

As referências de "alma" que copiamos (guias de fusível, tipos de fita) muitas vezes pintam **cada coluna/categoria de uma cor diferente**. **Nós não fazemos isso.** Copiamos a *organização* densa e elegante daquelas peças — a ALMA — **não** a paleta arco-íris.

- ❌ Categoria A em azul, B em roxo, C em laranja, D em rosa.
- ✅ Todas as categorias na mesma família verde/escura; **a categoria se distingue por ícone + rótulo + objeto fotorrealista**, nunca por matiz.

A cor não é o eixo de categorização. O eixo é o **ícone de linha**, o **rótulo de texto** e o **objeto**. A cor só carrega hierarquia (verde lidera, ouro destaca) e semântica (alerta avisa).

### "A cor nunca é o único sinal"

Acessibilidade não é opcional. Quem é daltônico ou está num celular sob sol forte não pode depender do matiz. Por isso **toda informação carregada por cor é sempre pareada com um segundo sinal**:

- Verde de destaque → **+ ícone + rótulo**.
- Ouro de "estrela/CTA" → **+ ícone/selo + texto** ("o melhor", "comece aqui").
- Alerta vermelho-terra → **+ a palavra "IMPORTANTE" + ícone de aviso**.

Se você apagasse toda a cor da peça e a transformasse em escala de cinza, ela ainda deveria ser **legível e navegável**. Esse é o teste.

### Cor sobre o objeto fotorrealista

Cada item da grade tem um objeto fotorrealista (detalhe nas seções 04 e 07). Princípio cromático aqui: **o objeto deve pertencer ao mundo verde da marca** — tratado como tinta de marca / duotone verde, não como foto de banco de imagem colorida e crua. O objeto não pode reintroduzir o arco-íris pela porta dos fundos. *(O "como" — duotone, grade, sombra, iluminação — fica nas seções 04/07.)*

### Contraste (medido por `check_marca.py`, canvas escuro)

O texto e os acentos passam WCAG com folga. Estes números saem do relatório de contraste embutido em `check_marca.py` (`contrast_report`):

| Par | Razão | Mínimo WCAG | Veredito |
|---|---|---|---|
| Texto (`tinta` `#f2f2f5`) sobre fundo (`papel` `#08080c`) | **17.9:1** | 4.5 | AA folgado |
| Verde (`#3faf76`) sobre fundo | **7.2:1** | 3.0 | AA ok |
| Ouro (`#d8a64a`) sobre fundo | **9.0:1** | 3.0 | AA ok |
| Texto escuro sobre pílula verde | **7.2:1** | 4.5 | AA ok |

O mesmo guardrail roda um relatório paralelo para o **modo claro do site** (`contrast_report_light`), confirmando texto/verde/ouro sobre o papel claro. Sempre que mexer em cor, rode `python check_marca.py` — ele falha se algum gerador hardcodar uma cor antiga proibida e reporta o contraste atualizado.

### Cores PROIBIDAS (o guardrail rejeita)

`check_marca.py` mantém uma lista `FORBIDDEN` de valores antigos que **não podem** voltar a aparecer:

- `#d8a64a` **hardcoded** → use `marca.hex_of("ouro")` (o valor é certo, o hardcode é o erro).
- `oklch(84% 0.115 92)` → ouro antigo (hue 92) → use o ouro de marca (hue **83**).
- `oklch(75% 0.16 38)` → alerta antigo (hue 38) → use alerta de marca (hue **30**).
- `oklch(73% 0.15 152)` → verde antigo (L73) → use verde de marca (**L70**).
- Fontes `ariblk.ttf` / `arial.ttf` / `georgia.ttf` hardcoded → use `marca.font(...)`.

### Faça / Não faça

| ✅ Faça | ❌ Não faça |
|---|---|
| Deixe o verde (hue 152) liderar a peça inteira | Pintar cada categoria/coluna de uma cor diferente (arco-íris) |
| Use o ouro `#d8a64a` em **um** ponto de destaque (< ~10%) | Espalhar ouro por toda a peça até ele virar ruído |
| Reserve o alerta `#e8744f` só para "IMPORTANTE"/aviso | Usar vermelho-terra como decoração ou acento estético |
| Pareie sempre cor + ícone + rótulo | Distinguir itens **só** pela cor |
| Puxe a cor de `marca.py` (`hex_of`, `css_root`) | Hardcodar HEX/OKLCH nos geradores |
| Trate o objeto como duotone no mundo verde | Colar foto colorida crua que reintroduz o arco-íris |
| Rodar `python check_marca.py` ao mexer em cor | Inventar um segundo acento ("azul de apoio", "roxo de seção") |

---

## 02. Tipografia

> A tipografia é a **voz** da marca. Duas famílias, papéis fixos, pesos disciplinados. Quando o leitor bate o olho numa peça do Minuto Real, é a tipografia — antes da cor — que diz "isto é nosso". Esta seção é a lei. Os valores são reais: lidos de `marca.py` (contrato de fontes) e do `BASE_CSS`/`ARCH_CSS` em `gerar_infografico.py` (tamanhos e pesos de fato renderizados no canvas 1080×1350).

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

### Caixa-alta, tracking e quebra de linha

**CAIXA-ALTA** (`text-transform:uppercase`) é a assinatura dos títulos, rótulos, kickers e watermark. Nunca digite o texto já em maiúsculas no `_data.py` — deixe o CSS fazer o `uppercase` (preserva acentuação correta em pt-BR e mantém o controle no token).

**Tracking (`letter-spacing`):**
- Títulos-herói: **negativo** (`-.018em` a `-.022em`) — letras pesadas e grandes pedem aperto para virar bloco sólido.
- Números-herói: bem negativo (`-.04em`).
- Kickers, badges, watermark: **positivo e generoso** (`.12em` a `.26em`) — texto pequeno em caixa-alta precisa de ar entre as letras para respirar e parecer "etiqueta de catálogo".

**Quebra de linha:** todo título usa `text-wrap:balance` (linhas equilibradas, sem órfã solta); corpo e descrição usam `text-wrap:pretty`. Não force `<br>` manual nos títulos — confie no balance + auto-fit.

**Itálico:** só na Literata, só em citação. Itálico em Hanken é **proibido** — descaracteriza a voz grotesca.

### O título-herói premium

É o efeito das referências do usuário. Receita real (está no `BASE_CSS`/`ARCH_CSS`), sem exagero:

1. **Peso e caixa:** Hanken **Black 900**, `text-transform:uppercase`, tracking negativo. O título é um bloco, não uma linha de texto.
2. **Duas tintas na mesma frase:** a parte-chave em verde (`.lt` → `var(--green)`) e o resto em tinta clara (`.bd` → `var(--ink)`). Vem direto do `_data.py` (`header_light` + `header_bold`). Isso cria foco sem mudar de fonte.
3. **Brilho verde sutil (o "glow"):** `text-shadow: 0 0 50px oklch(72% 0.14 152 / .38)` aplicado **só na parte verde** (`.lt`). É um halo difuso (raio ~50px, opacidade ~.38), não um contorno. Faz a palavra-chave "acender" sobre o fundo escuro — cinematográfico, nunca neon.
4. **Textura/grão na letra:** o grão vem do `.slide::before` (pontos radiais sutis) por baixo, e o efeito de "letra vazada com textura" aparece no **ghost** (`.ghost`): Black 900, `color:transparent` + `-webkit-text-stroke:2px oklch(... / .09)`, com máscara radial. É a letra-fantasma gigante atrás do conteúdo (o "→", "VS", "%"). Use-o como camada de profundidade — **um por peça**, nunca competindo com o herói.
5. **Capitular (Literata):** para abrir uma ideia em tom editorial, troque a primeira letra de um bloco por uma **capitular em Literata** (serif, ~2–3 linhas de altura, verde ou ouro). Reserve para citações e aberturas — é o único lugar onde a serif lidera.

Discrição é a regra: **um** glow (na palavra-chave), **um** ghost, **uma** capitular por peça. Empilhar os três no mesmo elemento vira ruído.

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

---

## 03. Anatomia da Peça (DNA do Layout)

Toda peça do Minuto Real é a mesma **planta baixa** vestida em conteúdos diferentes. Quem lê de relance precisa reconhecer "isto é nosso" em 200 ms — antes de ler uma palavra. Esse reconhecimento mora na **estrutura**, não no texto: cinco zonas empilhadas de cima para baixo, sempre na mesma ordem, sempre com o mesmo respiro.

Os valores aqui são os **reais** de `gerar_infografico.py` (canvas `.slide` 1080×1350, padding `70px 76px 50px`). Quando um arquétipo diverge, está anotado.

### As cinco zonas (de cima para baixo)

```
┌──────────────────────────────────────────────┐  ← moldura tracejada (inset 38px)
│  ┌────────────────────────────────────────┐  │
│  │ 1 · TOPO    [▣ Minuto Real]   [01/03] │  │  ← brandmark + badge/paginação
│  │ ────────────────────────────────────── │  │
│  │ 2 · CABEÇALHO   TÍTULO-HERÓI            │  │  ← h1 uppercase + promessa
│  │     promessa / subtítulo curto          │  │
│  │     - - - - - - - - - - - - régua - - - │  │  ← régua tracejada verde
│  │                                          │  │
│  │ 3 · CORPO        ▣  RÓTULO      [chip]  │  │
│  │     a GRADE      └─ descrição curta      │  │  ← itens (catálogo OU "com fios")
│  │     de itens     ▣  RÓTULO      [chip]  │  │
│  │                  └─ descrição curta      │  │
│  │                                          │  │
│  │ 4 · RODAPÉ  [◆] DICA: aviso final…      │  │  ← barra de aviso (ícone + selo)
│  │ 5 · ASSINATURA      @minutoreal1701      │  │  ← handle / domínio
│  └────────────────────────────────────────┘  │
└──────────────────────────────────────────────┘
        ⌗ número-fantasma atrás de tudo (z-0)
```

#### 1 · TOPO — identidade + paginação
A primeira linha **sempre** carrega o `brandmark`: selo verde de raio `12px` (42×42px, fundo `--green`, ícone `book` na cor `--on-green`) seguido de "Minuto**Real**" — onde "Real" vai em `--green`, peso 900, uppercase, `letter-spacing:.03em`, `font-size:25px`. À direita, um **badge/pílula** de contexto: borda `1.5px` `--hair`, raio `999px`, `padding:9px 20px`, texto `--green-soft` uppercase com `letter-spacing` largo (ex.: `MAPA DO LIVRO`, `01/03`, `DADOS`). O topo é a única zona presente em **100%** dos arquétipos.

#### 2 · CABEÇALHO — título-herói + promessa + régua
- **Título-herói (`h1`):** `font-size:78px`, `line-height:.92`, peso 900, **uppercase**, `letter-spacing:-.022em`, `text-wrap:balance`. Padrão de duas cores: parte clara (`header_light`) em `--green` com glow (`text-shadow`), parte forte (`header_bold`) em `--ink`. (Os outros arquétipos abaixam o h1: fluxo 74px, numeros 76px, anatomia 60px, compara 54px.)
- **Promessa/subtítulo:** `font-size:30px`, `line-height:1.24`, `--muted`, peso 600, `max-width:880px`. É a primeira frase do livro/capítulo — concreta, nunca um slogan vago.
- **Régua tracejada:** `border-top:2px dashed var(--green)` com `opacity:.55`. Fecha o cabeçalho e abre o corpo. É a costura visual da marca.

#### 3 · CORPO — a GRADE de itens
O coração da peça. Duas variantes principais:

**(a) CATÁLOGO em coluna / N-colunas** — cada item é uma **célula** com quatro sub-elementos fixos:

| Sub-elemento | Papel | Valores reais (arquétipo LISTA) |
|---|---|---|
| **selo + objeto** | o ícone/objeto-símbolo do conceito | selo 84×84px, raio `22px`, borda `2px --hair`, glow interno; SVG 46px |
| **rótulo** | o nome do conceito, curto e forte | `.lbl` peso 900, uppercase, `text-wrap:balance` |
| **descrição** | uma frase que explica o conceito | `.sub` `--muted`, `line-height:1.26`, peso 500 |
| **chip / "USO:"** | a marca de uso (nº do capítulo, tag) | `.chip` raio `13px`, peso 900; variante ouro `.au` no último item |

A célula é um `grid` de 3 colunas: `auto 1fr auto` (selo · texto · chip), `column-gap:28px`. Entre itens, um **divisor pontilhado** (`repeating-linear-gradient`, dash 14px / gap 12px). O tom de verde **cicla** `soft → mid → deep` para criar ritmo, e o **último item é sempre ouro** (`--gold`) — o acento premium que fecha a leitura.

**(b) DIAGRAMA "COM FIOS"** (estilo guia de fusíveis) — em vez de uma lista paralela, um **objeto-fonte ligado por um fio/linha a um objeto-alvo** que ele afeta. É a variante usada pelos arquétipos **FLUXO** e **ANATOMIA**:

- **FLUXO** (timeline vertical): cada passo = selo redondo de 108px (número + ícone) ligado ao próximo por um **fio tracejado vertical** (`border-left:2px dashed var(--green)`, `left:53px`, parte do centro do selo). O fio é literalmente o "cabo" que conecta a etapa N à N+1. Passo-chave ganha coroa ouro e o fio vira `--gold`.
- **ANATOMIA** (anel/ciclo): um **hub central** com 4 nós em volta (N, E, S, O, sentido horário), ligados por **arcos com seta** (`marker-end`, `stroke-dasharray`) — o ciclo. Cada nó tem um **conector tracejado** (`stroke-dasharray:2 6`) que vai até um **callout numerado** num dos 4 cantos (rótulo + lei + explicação). É o "com fios" em forma de ciclo: a fonte (nó) puxa um fio até seu rótulo.
- **COMPARA** é o caso especial de **duas colunas X × Y**: grade `1fr 1fr` com um selo "VS" ouro de 84px no cruzamento; lado A = "evite" (verde-deep + ✕), lado B = "faça" (verde + ✓).

A regra que une as duas variantes: **um objeto + um rótulo + uma frase + um conector** (divisor, fio ou arco). Nunca texto solto sem âncora visual.

#### 4 · RODAPÉ — barra de aviso "DICA / IMPORTANTE"
Uma faixa fechada que entrega o **takeaway**: caixa de borda `2px --hair`, raio `22px`, `padding:22px 28px`, fundo em gradiente verde sutil. Dentro: um **ícone em selo** verde (62×62px, raio `17px`, fundo `--green`) + um **kicker** uppercase (`NA PRÁTICA`, `DICA`, peso 900, `letter-spacing:.18em`, cor `--green`) + a frase de fechamento (`--ink`, ~27px). Nos arquétipos com `viz`/`practice` o rodapé pode trocar de moldura (borda tracejada superior em fluxo/numeros), mas o **trio ícone + kicker + frase** é invariável.

#### 5 · ASSINATURA — handle / domínio
A última linha, centralizada e discreta: `@minutoreal1701`, peso 800, uppercase, `letter-spacing` muito largo (`.24em`), `font-size:18px`, cor `--ink-dim`. Em LISTA vem com cauda editorial ("· o livro inteiro em 1 página"). Nunca é destaque — é o carimbo, não a manchete.

### Elementos estruturais de fundo (o "cromo" da marca)

Três camadas vivem **atrás** do conteúdo (z-0) e são o que faz a peça parecer impressa, não um slide de PowerPoint:

| Elemento | CSS real | Função |
|---|---|---|
| **Moldura tracejada** | `.slide::after` · `inset:38px` · `border:2px dashed var(--green)` · `border-radius:32px` · `opacity:.38` | a "borda do bilhete"; emoldura toda a peça |
| **Grade de pontos** | `.slide::before` · `radial-gradient` 1.1px · `background-size:36px 36px` · máscara que some no topo | textura de papel técnico; nunca compete com o texto |
| **Número-fantasma** | `.ghost` · peso 900 · `-webkit-text-stroke:2px` (verde a ~9% opacidade) · `letter-spacing:-.05em` · com máscara radial | um glifo gigante (→, %, VS) atrás do conteúdo, dá profundidade e "assunto" |

> O conteúdo real fica em `.slide > *` com `position:relative; z-index:1` — sempre **acima** das três camadas.

### Ritmo & espaçamento

- **Margem de segurança:** o padding (`~70px` lateral) e a moldura (`inset:38px`) criam uma **zona morta** nas bordas. Nada de texto ou objeto encosta na moldura.
- **Respiro vertical:** o corpo usa `justify-content:space-between` (LISTA) — os itens se distribuem para preencher a altura sem amontoar. A peça **nunca** tem um bloco gordo em cima e vazio embaixo.
- **Alinhamento à grade:** selos, rótulos e chips alinham em colunas verticais consistentes (o `grid` de 3 colunas garante isso). Olho do leitor desce em linha reta.
- **Auto-fit:** um passo de JS (`_FIT_JS`) encolhe o `h1` que estoura a largura (até 40px) e o corpo `.fitv` que estoura a altura (1px por vez). **O layout se adapta ao conteúdo, não o contrário** — mas isso é rede de segurança, não desculpa para texto longo.

### Grids por formato

O arquivo gera nativamente o **feed 4:5**. Os demais formatos reusam o mesmo DNA (zonas + cromo), reescalando a contagem de itens:

| Formato | Dimensões | Proporção | Itens que cabem bem | Observação |
|---|---|---|---|---|
| **Feed** | 1080×1350 | 4:5 | **5–6** itens de catálogo (ou 4 passos de fluxo) | formato nativo de `gerar_infografico.py` (`_even_sample(..., 6)`) |
| **Quadrado** | 1080×1080 | 1:1 | **4** itens | menos altura → corte do corpo; rótulos mais curtos |
| **Story** | 1080×1920 | 9:16 | **6–7** itens, ou 1 conceito gigante | sobra altura → cabeçalho maior + CTA "arrasta"; respeitar zona segura do topo/rodapé (UI do app) |
| **Thumb** | 1280×720 | 16:9 | **1–3** | é cartaz, não catálogo: título-herói domina, no máximo 3 objetos |

Regra geral: **quanto mais largo o formato, menos itens** (a altura é o que comporta a coluna). O número-fantasma e a moldura escalam junto; brandmark e assinatura **nunca** somem.

### Faça / Não faça (composição)

**Faça**
- Mantenha a ordem das 5 zonas. Topo e assinatura são obrigatórios em toda peça.
- Use **um objeto por conceito** e ancore todo texto a uma âncora visual (selo, fio ou arco).
- Deixe a moldura respirar: borda da moldura → conteúdo tem folga de sobra.
- Hierarquia clara por **tamanho e peso**, não só por cor (cor é reforço, nunca o único sinal).
- Feche com o rodapé "DICA/NA PRÁTICA": toda peça entrega um takeaway acionável.
- Reserve o **ouro** para um único acento (último item / verdict / passo-chave).

**Não faça**
- Não lote: mais de 6 itens no feed vira parede de texto — corte ou parta em carrossel.
- Não solte texto sem objeto/conector; não deixe um item "flutuando" fora da grade.
- Não encoste nada na moldura tracejada nem na borda do canvas.
- Não use arco-íris: verde lidera, ouro é o único acento. Sem azul/vermelho decorativos.
- Não confie só na cor para separar "faça/evite" — use também ✓/✕ e posição (COMPARA já faz isso).
- Não deixe o número-fantasma legível a ponto de competir com o conteúdo (fica em ~9% de opacidade, atrás de tudo).
- Não esconda o brandmark nem a assinatura para "ganhar espaço" — são o carimbo da marca.

---

## 04. O Objeto Fotorrealista

> *O coração do padrão. As seções anteriores vestem a peça (paleta, tipografia) e desenham seu esqueleto (anatomia). Esta seção trata da única coisa que hoje nos falta para alcançar a alma das referências: trocar o ícone de linha pelo **objeto renderizado de verdade**. Se a bíblia inteira tivesse de caber numa frase, seria esta — o objeto é o que nos faz premium.*

### O que é um "objeto" no nosso padrão

Nas referências que admiramos — o guia de fusíveis, os tipos de fita — cada item da grade não traz um desenho: traz **a coisa**. O fusível está ali, com seu corpo translúcido, seus terminais de metal, sua etiqueta de amperagem. É renderizado como se tivesse sido fotografado num estúdio de produto. Essa presença física é o que separa um infográfico de catálogo de um slide de PowerPoint.

No nosso padrão, **o "objeto" é a coisa concreta — um objeto-símbolo — que representa um conceito do livro.** Ele ocupa o `seal` (o slot circular ou de canto arredondado de cada item) e **substitui o ícone de linha** que usamos hoje. O ícone de linha foi a etapa intermediária honesta: legível, barato, na marca. Mas é plano e genérico — um ícone de "corrente" parece o ícone de "corrente" de qualquer marca do mundo. O objeto fotorrealista é **nosso**: tem peso, material, luz e atmosfera.

A regra-base é severa e não-negociável:

> **Um objeto por item. Um conceito por objeto. Nada de ícone de linha na mesma peça em que há objeto fotorrealista.**

O objeto é caro de gerar (passa pelo Imagen), então a doutrina de toda a rede se aplica: **gera-se uma vez por conceito, tinge-se na nossa cor, guarda-se em cache.** O custo é pago uma única vez; o ativo se reusa em carrossel, feed, Stories e thumbnail.

### Como escolher o objeto-símbolo de um conceito

Escolher o objeto é a decisão de direção de arte mais importante da peça. Um objeto errado afunda um card inteiro, por mais bem renderizado que esteja. Cinco critérios, em ordem de prioridade:

**1. Concreto vence abstrato.** O objeto tem de ser uma coisa que existe no mundo físico e que se pode segurar, fotografar, iluminar. "Poder" não é objeto; uma **coroa** é. "Dependência" não é objeto; uma **corrente** é. Se o conceito for abstrato, traduza-o para o artefato físico mais próximo — o instrumento, a consequência, o emblema.

**2. Metáfora visual forte e legível em 1 segundo.** O leitor tem de entender o vínculo conceito→objeto sem legenda. A ponte metafórica precisa ser curta. Coroa→poder é uma ponte de um passo. "Ampulheta de mercúrio escorrendo para cima"→adaptabilidade é uma ponte de quatro passos: ninguém atravessa. Prefira a metáfora que o público já carrega.

**3. Consistência de "mundo".** Todos os objetos de **uma mesma peça** devem pertencer à mesma família estética — o mesmo universo material. Se o card 1 é uma coroa barroca de ouro lapidado, o card 2 não pode ser um emoji de cadeado nem um ícone 3D de plástico: tem de ser um objeto do mesmo mundo (um molho de chaves de latão envelhecido, digamos). Mesma "liga" de materiais, mesma época, mesma seriedade.

**4. Tensão e silhueta.** O objeto premium tem uma **silhueta reconhecível** no escuro e uma pitada de drama. Um prisma com um feixe de luz atravessando é mais forte que um prisma parado. Uma corrente parcialmente tensionada diz mais que uma corrente enrolada no chão.

**5. Fuja do clichê fraco.** O clichê forte (coroa = poder) é um atalho útil; o clichê fraco (lâmpada acesa = ideia, aperto de mão = acordo, alvo com flecha = meta) é preguiça que faz a peça parecer banco de imagens grátis. Quando o primeiro objeto que vier à cabeça for um desses, descarte e procure o segundo.

#### Critérios — Faça / Não faça

| Faça | Não faça |
|---|---|
| Traduzir o abstrato para um artefato físico (poder → coroa) | Tentar renderizar a abstração direto ("uma nuvem de poder") |
| Metáfora de 1 passo, que o público já tem | Metáfora cifrada que exige legenda para entender |
| Manter todos os objetos da peça no mesmo mundo material | Misturar coroa barroca com cadeado de emoji no mesmo grid |
| Buscar a silhueta forte e legível no escuro | Objeto chapado, sem volume, que some no fundo `#08080c` |
| Recusar o primeiro clichê fraco e procurar melhor | Lâmpada/aperto-de-mão/alvo-com-flecha como reflexo automático |

### Enquadramento & escala

O objeto entra num slot pequeno e repetido (o `seal`, ~84–110 px na peça final). Para que a grade pareça **uma série** — e não cinco fotos avulsas coladas — o enquadramento tem de ser idêntico item a item.

- **Centralizado.** O objeto vive no centro óptico do quadro, com folga de respiro ao redor. Nunca encostado nas bordas, nunca cortado pelo recorte do slot.
- **Escala consistente.** O objeto preenche aproximadamente a **mesma fração do quadro** em todos os cards (mire ~70–80% da altura útil). Uma coroa que ocupa o quadro inteiro ao lado de uma chave minúscula quebra a série. Escala-se pela presença visual, não pelo tamanho real: uma chave pode ser ampliada e uma coroa recuada para que "pesem" igual.
- **Ângulo e ponto de vista coerentes.** Mesma altura de câmera (de leve acima ou no nível do objeto) e mesma rotação de três-quartos em todos. Não alterne entre vista frontal chapada e vista mergulhada.
- **Fundo escuro ou transparente.** Gere sobre fundo escuro profundo (vizinho do `#08080c`) ou transparente, para compositar limpo no slot. **Nunca** sobre branco, cenário, mesa de madeira ou qualquer ambientação — o objeto é recortado, não uma cena.

### Iluminação

A luz é o que transforma "imagem de objeto" em "fotografia de produto premium". É também o maior vetor de coerência: **mesma direção de luz em todos os objetos da peça.**

- **Luz dramática de produto, não luz de catálogo plano.** Buscamos o claro-escuro de still de cinema, não a iluminação difusa e sem sombra de e-commerce.
- **Key light** definindo o volume a partir de um lado (mantenha o mesmo lado — ex.: superior-esquerdo — em toda a série).
- **Rim light verde** — a assinatura. Uma luz de contorno na cor da marca (verde hue 152) lambendo a borda do objeto pelo lado oposto à key. É o que cola o objeto no nosso universo cromático antes mesmo do pós-processo, e o que dá o brilho de "isto é Minuto Real".
- **Profundidade.** Leve queda de foco / atmosfera ao fundo, para o objeto saltar do escuro. Negro absoluto e chapado mata o premium; queremos o preto com profundidade.
- **Sombra de contato.** Uma sombra curta e ancorada sob o objeto, para que ele **pouse** em algo e não flutue no vácuo. Mesma direção e dureza de sombra em todos os cards.

### Material & textura

O objeto tem de ser **tátil**. O leitor quase sente o peso. Esta é a fronteira entre premium e amador, e ela é binária:

| Queremos | Rejeitamos |
|---|---|
| Hiper-real, fotográfico, microtextura visível (arranhão, poro, reflexo) | Cartoon / ilustração chapada / flat design |
| Metal escovado, vidro com refração, pedra, latão envelhecido, cristal | "3D plástico barato" — render de banco de imagem, sem alma |
| Imperfeição premium (pátina, desgaste fino, reflexo especular) | Superfície perfeita-demais, lisa, sintética, de brinquedo |
| Materiais nobres e coerentes entre si | Material aleatório por card (um de ouro, um de borracha, um de papel) |

O acabamento de material é o que faz o objeto **parecer caro**. Quando em dúvida, vá para o material mais nobre e mais texturizado: vidro lapidado em vez de plástico, latão patinado em vez de aço genérico, plasma com profundidade em vez de bola lisa.

### A "tinta de marca" — fazer todo objeto pertencer ao mundo verde

Este é o passo que separa "cinco imagens bonitas de bancos diferentes" de "uma série da Minuto Real". Objetos gerados livremente vêm com cores próprias — uma coroa dourada, uma corrente cinza, um prisma de arco-íris. Cada um pertence a um mundo cromático diferente, e a grade vira ruído. A tinta de marca **resolve isso em duas frentes**, e as duas são obrigatórias:

**(a) Ancorar a paleta verde já no prompt.** Antes de o objeto existir, pedimos a luz e o ambiente na nossa cor: rim-light verde, fundo escuro-verde, atmosfera fria na faixa do hue 152. O objeto já **nasce** banhado no nosso verde. (O texto exato do prompt é assunto da seção 05 — aqui fica o princípio: a cor da marca entra na geração, não só depois.)

**(b) Pós-processo de tingimento no compositing.** Mesmo nascendo verde, cada objeto chega com matiz ligeiramente diferente. No compositing aplicamos uma camada de unificação — um **duotone / overlay verde** que puxa todos os objetos para a mesma faixa cromática (verde-mãe `#3faf76` nas sombras/meios, mantendo brilho nos realces) — reforçada pelo **rim-light verde** já comentado. O resultado: cinco objetos de origens diferentes que parecem **iluminados pela mesma lâmpada, no mesmo estúdio**.

> **O ouro (`#d8a64a`) entra só como brilho-acento pontual** — uma faísca especular num realce, a borda de um objeto-chave, nunca como cor dominante do objeto e nunca em todos os cards. O ouro pontua; o verde governa. (Princípio da seção 01 aplicado ao objeto.)

#### A tinta de marca — Faça / Não faça

| Faça | Não faça |
|---|---|
| Pedir o verde da marca já na geração (rim-light + atmosfera) | Gerar com cor livre e "arrumar depois" só na pós |
| Unificar os objetos com um duotone/overlay verde no compositing | Deixar cada objeto na sua cor original (vira arco-íris) |
| Usar ouro como faísca especular pontual num único realce | Banhar o objeto inteiro de ouro, ou pôr ouro em todos |
| Manter o verde dominante e o objeto legível sob a tinta | Tingir tão forte que o objeto vira uma silhueta verde chapada |

### Consistência — dentro de uma peça e entre peças

A coerência é a moeda da marca. Vale tanto **horizontalmente** (os objetos de um mesmo carrossel/infográfico entre si) quanto **verticalmente** (os objetos de "48 Leis" contra os de "Hábitos Atômicos").

Quatro eixos têm de bater **sempre**:

1. **Direção de luz.** Mesma key, mesmo lado, mesmo rim-light verde. Um objeto iluminado da esquerda ao lado de um iluminado de cima já denuncia que não são da mesma série.
2. **Liga cromática.** Todos passam pela mesma tinta de marca, na mesma intensidade. O verde tem de ser **o mesmo verde** em toda a peça.
3. **Profundidade e atmosfera.** Mesmo nível de queda de foco, mesma densidade de escuro ao fundo, mesma sombra de contato.
4. **Escala e enquadramento.** Mesma fração do quadro, mesmo ponto de vista (ver "Enquadramento & escala").

Entre peças diferentes, esses quatro eixos são o que faz um leitor reconhecer a Minuto Real antes de ler o título do livro — exatamente a promessa de reconhecimento em 0,5 s da seção 00. Por isso os parâmetros de luz, tinta e enquadramento vivem na receita (cache + marca), não no capricho de cada geração.

### Exemplo de referência — "As 48 Leis do Poder"

Espelha as peças que já geramos. Cada conceito vira um objeto-símbolo concreto, todos no mesmo mundo material e sob a mesma luz verde:

| Conceito do livro | Objeto-símbolo | Material & leitura |
|---|---|---|
| A natureza do poder | Esfera / núcleo de **plasma verde** | Energia contida e instável — o poder como força viva, brilho interno na cor-mãe |
| Proteja o mestre | **Molho de chaves + coroa** | Latão e ouro envelhecidos — acesso e autoridade que se guardam |
| Controle & dependência | **Cabos / correntes de rede** | Metal tensionado, elos entrelaçados — o laço que prende quem depende |
| Tática & indireção | **Prisma com feixe de luz** | Cristal lapidado desviando um feixe verde — a jogada que não vai em linha reta |
| Ser informe / adaptável | **Metal líquido / mercúrio** | Superfície espelhada e móvel — o que não se agarra porque não tem forma fixa |

Note como os cinco objetos pertencem ao mesmo universo: todos sólidos, todos sob a mesma key e o mesmo rim-light verde, todos com a faísca de ouro apenas onde o realce pede. É essa unidade — não a beleza de cada um isolado — que torna a grade premium.

### Faça / Não faça — o objeto fotorrealista

| Faça | Não faça |
|---|---|
| Um objeto fotorreal por card, com respiro ao redor | Empilhar dois objetos ou poluir o card com elementos soltos |
| Manter fotorreal **e** ícones de linha em peças separadas | Misturar objeto fotorrealista com ícone flat na **mesma** peça |
| Tingir todo objeto na liga verde da marca | Deixar um objeto com cor fora da marca (cinza cru, arco-íris) |
| Mesma direção de luz e mesma sombra em toda a série | Cada objeto com sua própria luz e seu próprio ângulo |
| Ouro como faísca pontual num realce | Ouro como cor dominante, ou ausência total do acento |
| Material nobre, tátil, hiper-real | Render de plástico barato, cartoon ou flat |
| Gerar uma vez por conceito e cachear o ativo tingido | Regerar o mesmo objeto a cada peça (caro e inconsistente) |

---

## 05. Molde de Prompt

> *Como gerar o objeto-símbolo já vestido na nossa estética, num prompt só. A seção 04 (Objeto) decide **qual** objeto representa cada conceito — a direção de arte. Esta seção entrega **o template de texto** que manda esse objeto para o Imagen e volta no nosso mundo verde. Os dois andam juntos: 04 escolhe o herói; 05 o fotografa.*

**Arquivo de verdade:** `videos/imagen.py`. A interface real é `gen(prompt, out_png, aspect='16:9')` — ela monta `{'instances':[{'prompt': ...}], 'parameters':{'sampleCount':1,'aspectRatio': aspect}}` contra `imagen-4.0-generate-001` (com fallback `-fast`). **Só existem dois campos que nós controlamos: o `prompt` (texto livre) e o `aspect`.** Não há `seed`, não há `negativePrompt`, não há `guidanceScale` exposto nessa API. Tudo o que queremos — o objeto, a luz, a cor, o que recusar — mora dentro da string `prompt`.

### Por que o prompt é em inglês

O Imagen 4 foi treinado predominantemente em legendas em inglês. **Prompts em inglês rendem objetos mais nítidos, luz mais previsível e menos "deriva" de estilo** do que os mesmos prompts em português. Por isso a regra desta seção:

> **A bíblia é escrita em pt-BR; os PROMPTS de imagem são escritos em inglês.**

O texto que o leitor vê na peça continua em português (ele é desenhado depois, em camada própria — seções 02/03). O inglês fica só na ordem que mandamos ao gerador. E como o template é fixo, ninguém precisa "saber inglês" para operar: troca-se **uma** variável (o objeto) e o resto é colado.

### Negativos sem campo de negativo

A API do Imagen **não tem `negativePrompt` separado** (diferente do Stable Diffusion). O que rejeitamos — texto na imagem, arco-íris, cartoon, multidão de objetos — vai **embutido no fim da string**, em linguagem afirmativa-de-recusa: `no text, no rainbow colors, no cartoon`. Esse rabo de negativos é **parte fixa da assinatura de estilo** e nunca sai. É ele que impede o Imagen de "ajudar" colando uma legenda ou pintando o objeto de sete cores.

### O template reutilizável

Toda peça da rede usa **a mesma string**, trocando só o miolo. As partes:

```
[SUBJECT]                <- a única variável real: o objeto-símbolo da seção 04
[RENDER]                 <- fixo: como renderizar (hero product render)
[PALETTE / LIGHT]        <- fixo: a nossa cor e luz (verde-mãe + 1 ouro + fundo near-black)
[FINISH]                 <- fixo: o acabamento cinematográfico
[FRAMING]                <- fixo: objeto isolado, espaço negativo generoso
[EMBEDDED NEGATIVES]     <- fixo: os negativos de texto / arco-íris / cartoon / multidão
```

E o molde montado, pronto para colar — só o `[SUBJECT]` muda:

```text
[SUBJECT: a single brass key with an ornate crown-shaped bow],
cinematic hyperrealistic product render, single hero object, centered,
dramatic emerald-green key light and rim light (jade #3faf76), one deep
green spill (#5cc28a), set against a deep near-black background (#08080c),
one small warm gold accent highlight (amber #d8a64a) as a single glint,
volumetric light, soft atmospheric haze, subtle film grain, high detail,
shallow depth of field, studio look, object isolated with generous
negative space, dark moody catalog aesthetic,
no text, no letters, no logos, no watermark, no people, no hands,
no rainbow colors, no multicolor, no flat icon, no cartoon, no illustration,
not busy, single object only.
```

**A regra de ouro do molde:** tudo a partir de `cinematic hyperrealistic...` é a **frase de assinatura de estilo** — ela é *idêntica* em todos os objetos do acervo. É o que faz um molho de chaves e uma gota de mercúrio parecerem fotografados no mesmo estúdio. Quem escreve um prompt novo **não reescreve o estilo**; copia o bloco e troca só o `[SUBJECT]`.

### O que muda × o que é fixo

| Parte | Fixo ou variável | Conteúdo |
|---|---|---|
| `[SUBJECT]` | **Variável** | O objeto-símbolo do conceito (vem da seção 04). É a *única* coisa que muda. |
| `[RENDER]` | Fixo | `cinematic hyperrealistic product render, single hero object, centered` |
| `[PALETTE/LIGHT]` | Fixo | Key/rim verde-mãe (`#3faf76`) + spill verde-deep (`#5cc28a`) + fundo `#08080c` + **um** glint ouro (`#d8a64a`) |
| `[FINISH]` | Fixo | `volumetric light, subtle film grain, high detail, shallow depth of field` |
| `[FRAMING]` | Fixo | `object isolated with generous negative space` |
| `[NEGATIVES]` | Fixo | `no text … no rainbow colors … no cartoon … single object only` |

Os HEX no prompt **espelham** `marca.py` (`#3faf76` verde, `#5cc28a` verde-deep, `#08080c` papel, `#d8a64a` ouro) — eles guiam o Imagen, mas **não substituem o tingimento de marca** no acabamento (seção 07). O objeto nasce verde por causa da luz, e ainda passa pelo duotone depois. Cinto e suspensório.

### Aspect ratio por uso

O `aspect` é o segundo (e último) parâmetro. Passe o formato certo direto no `gen`:

| Uso | Aspect | Chamada |
|---|---|---|
| **Slot de card** (objeto isolado p/ a grade do infográfico) | `1:1` | `gen(prompt, out, aspect='1:1')` |
| **Feed Instagram** (peça vertical) | `4:5` | `gen(prompt, out, aspect='4:5')` |
| **Story / Reels** | `9:16` | `gen(prompt, out, aspect='9:16')` |
| **Thumbnail YouTube / capa larga** | `16:9` | `gen(prompt, out, aspect='16:9')` *(default)* |

**Regra prática:** o objeto-herói da grade quase sempre é gerado em **`1:1`** (slot quadrado, recortável), porque é a peça que mais se reusa entre formatos. O `16:9` é só para a arte de capa/thumbnail onde o objeto ocupa a cena inteira. Quando em dúvida, gere `1:1` — sobra moldura para encaixar em qualquer layout.

### Consistência entre objetos (o "mesmo mundo")

92+ livros, dezenas de objetos. O que faz todos parecerem do mesmo acervo:

1. **Mesma frase de estilo, byte a byte.** Não "melhore" a assinatura de um objeto para o outro. Se mudar a luz num, mude em todos — ou nenhum. O estilo é constante; o objeto é a variável.
2. **Gere em lote.** Rode todos os objetos de um livro (ou de um agrupamento das 48 Leis) **na mesma sessão**, com a mesma string de estilo, para que a luz e o grão "casem". Lotes separados em dias diferentes derivam.
3. **Mesma luz, mesma direção.** Key verde sempre vindo do mesmo lado, rim verde marcando a silhueta, fundo sempre `#08080c`. É a iluminação que costura objetos diferentes numa família.
4. **Sobre seeds e variações:** essa API **não expõe seed** — não dá para "fixar" um resultado. A consequência prática: gere **2–3 amostras** por objeto (rode o `gen` mais de uma vez no mesmo prompt) e **escolha a melhor à mão**. A reprodutibilidade vem do *cache* — depois de aprovado, o objeto é guardado e reusado (doutrina "gera uma vez, reusa sempre" da seção 00), não regenerado.

### Os 5 prompts prontos — objetos das 48 Leis do Poder

Espelham a direção de arte da seção 04 (cada conceito → seu objeto-símbolo). Já trazem a assinatura de estilo verde completa. Gere em `1:1` para a grade; troque o `aspect` se for capa.

**(1) Núcleo de plasma verde — a natureza do poder**

```text
A single glowing orb of emerald-green plasma energy, a contained core of
swirling green light with crackling filaments, floating, centered,
cinematic hyperrealistic product render, single hero object,
dramatic emerald-green key light and rim light (jade #3faf76), deep green
inner glow (#5cc28a), set against a deep near-black background (#08080c),
one small warm gold glint (amber #d8a64a) at the very center,
volumetric light, soft atmospheric haze, subtle film grain, high detail,
shallow depth of field, object isolated with generous negative space,
dark moody catalog aesthetic,
no text, no logos, no people, no rainbow colors, no multicolor,
no flat icon, no cartoon, not busy, single object only.
```

**(2) Molho de chaves de latão com coroa — proteja o mestre / a reputação**

```text
A single bunch of ornate antique brass keys tied together, one key with a
crown-shaped bow, hanging, centered, cinematic hyperrealistic product render,
single hero object, dramatic emerald-green key light and rim light
(jade #3faf76), deep green spill (#5cc28a), set against a deep near-black
background (#08080c), one small warm gold highlight (amber #d8a64a) glinting
off the crown, volumetric light, subtle film grain, high detail,
shallow depth of field, object isolated with generous negative space,
dark moody catalog aesthetic,
no text, no logos, no people, no hands, no rainbow colors, no multicolor,
no flat icon, no cartoon, not busy, single object only.
```

**(3) Emaranhado de cabos / correntes de rede — controle & dependência**

```text
A single dense tangle of dark metal chains and braided cables knotted into
one cluster, centered, cinematic hyperrealistic product render,
single hero object, dramatic emerald-green key light and rim light
(jade #3faf76), deep green rim (#5cc28a) tracing the links,
set against a deep near-black background (#08080c), one small warm gold
glint (amber #d8a64a) on a single link, volumetric light, subtle film grain,
high detail, shallow depth of field, object isolated with generous negative
space, dark moody catalog aesthetic,
no text, no logos, no people, no rainbow colors, no multicolor,
no flat icon, no cartoon, not busy, single object only.
```

**(4) Prisma de vidro com feixe de luz — tática & indireção**

```text
A single clear glass triangular prism bending a thin beam of light,
the refracted beam staying within green and gold tones, centered,
cinematic hyperrealistic product render, single hero object,
dramatic emerald-green key light and rim light (jade #3faf76), deep green
caustics (#5cc28a) cast on the surface, set against a deep near-black
background (#08080c), one small warm gold streak (amber #d8a64a) inside the
refracted beam, volumetric light, subtle film grain, high detail,
shallow depth of field, object isolated with generous negative space,
dark moody catalog aesthetic,
no text, no logos, no people, no rainbow spectrum, no multicolor,
no flat icon, no cartoon, not busy, single object only.
```

> *Atenção neste: um prisma "quer" virar arco-íris. Por isso os negativos `no rainbow spectrum, no multicolor` são reforçados e o feixe é amarrado a "green and gold tones" no SUBJECT. Sem isso, o Imagen pinta o espectro inteiro e quebra a marca.*

**(5) Gota de metal líquido / mercúrio — ser informe & adaptável**

```text
A single droplet of liquid metal mercury mid-morph, a shape-shifting blob of
reflective chrome catching green light, centered, cinematic hyperrealistic
product render, single hero object, dramatic emerald-green key light and rim
light (jade #3faf76), deep green reflections (#5cc28a) on the chrome surface,
set against a deep near-black background (#08080c), one small warm gold
reflection (amber #d8a64a) on the metal, volumetric light, subtle film grain,
high detail, shallow depth of field, object isolated with generous negative
space, dark moody catalog aesthetic,
no text, no logos, no people, no rainbow colors, no multicolor,
no flat icon, no cartoon, not busy, single object only.
```

### Dica de ouro: o acento sem virar arco-íris

O ouro (`#d8a64a`) é o tempero — **um ponto de brilho quente, não a peça inteira** (seção 01, "< ~10%"). Como pedir isso ao Imagen sem ele dourar tudo:

- Peça o ouro como **um evento único e pequeno**: `one small warm gold glint / highlight / reflection`, sempre no singular, sempre com `one small`.
- **Ancore o ouro num ponto físico** do objeto ("on the crown", "at the very center", "on a single link"). Ouro flutuante vira névoa dourada e domina a cena.
- **Nunca** escreva `golden object`, `gold and green`, nem liste o ouro como cor co-protagonista. Ele é um *glint*, não um banho.
- Se o objeto sair dourado demais, **não tire o ouro do prompt** — mova-o para um ponto menor (`a single glint on the edge`) e reforce `dominant green tones`.

A hierarquia no prompt espelha a da peça: **verde domina (key + rim + spill), ouro é um único reflexo.** Escrito nessa ordem, o Imagen respeita a proporção.

### Faça / Não faça (de prompt)

| ✅ Faça | ❌ Não faça |
|---|---|
| Manter a assinatura de estilo **idêntica** em todos os objetos | "Melhorar" o estilo de um objeto para o outro (derruba a consistência) |
| Trocar **só** o `[SUBJECT]`; colar o resto | Reescrever luz/cor/acabamento a cada prompt |
| Sempre embutir os negativos de **texto** (`no text, no letters, no logos`) | Deixar o Imagen colar legenda/marca-d'água por conta própria |
| Sempre embutir negativos de **arco-íris** (`no rainbow colors, no multicolor`) | Esquecer o anti-arco-íris (o Imagen adora colorir, sobretudo em prismas/plasma) |
| Pedir **um** objeto-herói (`single hero object, single object only`) | Pedir vários objetos / uma cena cheia (`not busy` existe por isto) |
| Fundo sempre `deep near-black background (#08080c)` | Fundo claro, branco ou colorido (quebra o mundo escuro da marca) |
| Ouro como `one small ... glint`, ancorado num ponto | `golden`, `gold and green`, ouro como cor co-protagonista |
| Gerar em `1:1` para o slot de card; `aspect` certo por uso | Gerar tudo em `16:9` e recortar torto depois |
| Gerar 2–3 amostras e escolher à mão (sem seed nesta API) | Esperar reprodutibilidade exata de uma só geração |
| Vestir o verde no SUBJECT **e** confiar no duotone da seção 07 | Achar que o prompt sozinho garante a cor — ele guia, o acabamento fecha |

---

## 06. Catálogo por Tipo de Peça

> *O inventário da rede, peça por peça. Cada formato resolve um trabalho diferente — mas todos vestem a **mesma pele** (a paleta de **01**, a tipografia de **02**, a anatomia genérica de **03**, o objeto fotorrealista de **04** e o acabamento de **07**). Aqui descrevemos só o que **muda** de um tipo para o outro: o layout, o papel, e onde entra o objeto. Nada de reescrever a pele — ela é referenciada, não duplicada.*

**Fonte de verdade desta seção:** `gerar_infografico.py` (arquétipos + dimensões), `gerar_carrossel.py` (carrossel, stories, citação) e `gerar_dados_kit.py` (peças do kit: `ASSET_META` / `ASSET_ORDER`). Toda dimensão abaixo foi lida desses arquivos. Se um valor divergir do código, o código vence.

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

### 06.3 — Stories 9:16 (1080×1920 · vertical)

De `gerar_carrossel.py` (`STORY_CSS`). Mesma pele, formato vertical, com **zona segura**: o conteúdo vive no miolo (`padding: 300px 100px`) deixando topo/rodapé (~290px) livres para a UI do Instagram. Wordmark fixo no topo, CTA-pill verde no rodapé.

| Frame | Peça | Papel | Objeto |
|---|---|---|---|
| `capa-story` | **Capa (story)** | Anúncio vertical do livro: eyebrow "novo · resumo da semana" + título-herói (158px) + gancho "N ideias que ficam" + tap "toque no link da bio" | Numeral-fantasma `N` grande ao fundo; objeto-símbolo do livro como na capa do carrossel |
| `citacao-story` | **Citação (story)** | A mesma frase-bomba do carrossel, layout vertical (aspa 300px + frase 88px + atribuição) | Objeto sutil ao fundo (aspa-fantasma); tipografia soberana |

- **Como veste o padrão:** é literalmente a **mesma pele** do carrossel, re-encaixada no 9:16. O título usa o mesmo `header_light`/`header_bold` verde/claro; o gancho numérico usa o **ouro**.
- **Observação:** existe ainda um `_story_cta` (frame "tudo em 1 toque": Acervo / YouTube / Amazon) usado pelo fluxo `--stories`; o kit publica `capa-story` e `citacao-story` como peças.

### 06.4 — Capa / Thumbnail do YouTube (1280×720 · 16:9)

De `gerar_dados_kit.py` (`THUMB_CSS`, `_thumb_fragment`). **16:9 (1280×720)** — alto contraste, legível em miniatura.

- **Papel:** a thumbnail do vídeo-resumo. Wordmark + eyebrow "o livro em ~5 min" + título-herói gigante (118px) + rodapé com o **número de ideias** em ouro (96px) + "ideias que ficam com você".
- **Como veste o padrão:** mesma pele (gradientes em camadas, moldura tracejada, numeral-fantasma gigante de 520px ao fundo), recortada para o 16:9. Verde lidera o título (`.lt`), o **ouro** carrega o número de ideias — o único acento.
- **Objeto fotorrealista:** **SIM — o objeto-símbolo do livro**, grande, no estilo de capa (ver **04**). O brief pede o título tratado como **3D em vidro/prata** sobre **textura (carbono/circuito)** + número de ideias + objeto-símbolo. O CSS atual entrega a base on-brand (numeral-fantasma + título-herói + número-ouro); o tratamento 3D/textura é a camada de **acabamento (07)** aplicada por cima, sem trocar a paleta.
- **Destaque:** é a peça de **maior contraste** (precisa ler em miniatura no feed do YouTube) — números e título maiores, respiro menor. Legibilidade em escala reduzida é a prova (ver **08**).

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

### 06.6 — CTA "Gostou? Tem mais"

Slide final do carrossel (`_cta` em `gerar_carrossel.py`), 4:5. O brief o descreve como **painel premium skeuomórfico** com botão verde "SALVE", knobs/LED.

- **Papel:** fechar o carrossel convertendo a atenção em ação: 3 destinos (acervo/cheat sheet + PDF, YouTube ~5 min, seguir @minutoreal1701) + botão **"Salve para revisar"**.
- **Estrutura atual:** título "Gostou? **tem mais.**" (verde) → 3 linhas (ícone em selo + frase, com a palavra-chave em verde-soft) → botão **save** verde (pílula, ícone bookmark) → handle → numeral-fantasma `+` ao fundo.
- **Como manter na paleta (skeuomorfismo on-brand):** o tratamento "painel premium / knobs / LED" do brief é **acabamento (07)** aplicado sobre esta estrutura — e tem de respeitar **01**: o botão "SALVE" é **verde** (`--green` sobre `--on-green`), os LEDs/realces "acesos" usam **verde-soft** (não um vermelho/azul de painel), e o **único ouro** vai no detalhe de destaque (selo premium), nunca espalhado pelos knobs. Skeuomorfismo sim; arco-íris de equipamento eletrônico, não. A cor nunca é o único sinal: cada destino tem ícone + rótulo, não só matiz.
- **Observação:** o Stories tem seu próprio CTA (`_story_cta`, "tudo em 1 toque", os 3 destinos verticais) — mesmo papel, formato 9:16.

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

### Nota de coerência

Todos os tipos acima compartilham a **PELE UNIVERSAL** — a paleta de **01**, a tipografia de **02**, a anatomia genérica de **03**, o objeto fotorrealista de **04** e o acabamento de **07**. Só o **layout** muda de um tipo para outro: a grade da LISTA, a linha do tempo do FLUXO, as colunas do COMPARA, os números do NUMEROS, o anel da ANATOMIA, o ritmo de slides do carrossel, a verticalidade do Story, o alto contraste da thumbnail. No código isso é garantido por **páginas isoladas** (`BASE_CSS`/pele compartilhada + só o CSS do tipo), de modo que não há vazamento de estilo. Por isso uma thumbnail 16:9 e um card de citação 4:5 **parecem irmãos** mesmo tendo esqueletos completamente diferentes: a pele os reconhece como família; o layout deixa cada um resolver bem o seu trabalho.

---

## 07. Acabamento Cinematográfico

A camada de *finish*. É o que separa uma peça **premium** de uma peça que parece feita às pressas — e quase nada disso é o conteúdo: é atmosfera, profundidade, grão e brilho controlado. **Fonte de verdade:** o `BASE_CSS` de `gerar_infografico.py` e o de `gerar_carrossel.py`. Todo valor abaixo foi confirmado no código; se algo divergir, o código vence. A regra que rege a seção inteira é uma só: **mão leve**. Premium é sutileza e controle. Glow estourado, grão grosseiro e sombra dura são a assinatura do amador.

### A pilha de acabamento (a "assinatura" recorrente)

Toda peça da rede carrega a mesma pilha de finish, construída em camadas sobre o `.slide`. Essas quatro coisas, juntas, são a **assinatura visual** que faz qualquer peça ser reconhecida como Minuto Real à distância:

1. **Fundo em camadas** — radial-glows verdes + gradiente escuro + vinheta nos cantos.
2. **Grade de pontos** (36px) com máscara radial — `.slide::before`.
3. **Moldura tracejada verde** (inset 38px, raio 32px, opacity .38) — `.slide::after`.
4. **Número-fantasma** — stroke verde translúcido com máscara radial — `.ghost`.

Nenhuma delas grita. Todas trabalham no fundo, abaixo do conteúdo (`z-index:0`), deixando o texto e o objeto no `z-index:1`. Vamos por partes.

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

### 6 · Tratamento do objeto no compositing (fazer o objeto "sentar" na cena)

O objeto fotorrealista (capa, item da grade — detalhe na seção 04) precisa **pertencer** à atmosfera verde, não parecer colado por cima. Três tratamentos o assentam na cena:

| Tratamento | O que faz | Como (mesma família dos selos) |
|---|---|---|
| **Sombra de contato** | Ancora o objeto no plano — ele "toca" o fundo | `box-shadow` deslocada para baixo (ex.: `0 14px 40px oklch(60% .14 152 / .3)`, como nos cards do carrossel) |
| **Rim-light / glow verde** | Borda do objeto pega a luz verde da cena | `drop-shadow(0 0 ~12px verde)` + glow ambiente radial fraco |
| **Realce de topo** | Reflexo de 1px na aresta superior, simula luz vindo de cima | `inset 0 1px 0 oklch(90% .1 152 / .12)` |

O objeto é tratado como **duotone no mundo verde** (ver seção 01): a iluminação de cena que incide sobre ele é verde, a sombra que ele projeta é verde-escura. Assim ele não reintroduz o arco-íris — ele é da paleta. *(O duotone/grade do objeto em si é assunto da 04; aqui é só o tratamento de borda e o assentamento na cena.)*

**Faça:** sombra de contato (deslocada) + rim-light verde (radial) + realce de topo de 1px. **Não faça:** objeto sem sombra (flutuando) ou com sombra dura preta (recortado, falso).

### 7 · Scrims / overlays (texto sobre objeto ou imagem)

Quando texto **cai sobre** o objeto ou uma imagem, a legibilidade não pode depender da sorte do pixel embaixo. A solução cinematográfica é o **scrim**: um gradiente escuro **entre** a imagem e o texto, que garante o contraste.

O princípio (introduzido aqui; a seção **08** aprofunda a leitura): um `linear-gradient` de transparente → escuro, do lado onde o texto se assenta, abaixado **sob** o texto e **sobre** a imagem. A própria vinheta do `.slide` (camada 3 do fundo) já é um scrim de borda — escurece os cantos, que é justo onde rótulos e marca-d'água costumam ficar (`.wm`, `@minutoreal1701`). Para texto sobre objeto, replique a lógica localmente: um gradiente escuro verde-quase-preto na base do bloco de texto.

A regra de ouro do scrim é a mesma de tudo aqui: **escuro o suficiente para o texto passar WCAG, leve o suficiente para a imagem ainda respirar.** O scrim não pode virar uma tarja preta opaca que mata o objeto. *(Os limiares de contraste e os casos difíceis ficam na 08.)*

**Faça:** scrim em gradiente sob todo texto que pousa sobre imagem. **Não faça:** texto cru sobre objeto torcendo para o fundo ajudar; nem tarja preta sólida que apaga a foto.

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

---

## 08. Legibilidade & Acessibilidade

A lente do **leitor**. As seções anteriores definem o que a peça *é* (cor, tipo, anatomia, objeto); esta define o que o leitor *consegue ler* — rolando o feed no celular, sob sol, daltônico, em 0,5 segundo. Duas vozes governam aqui: **Don Norman** (*O Design do Dia a Dia* — a culpa é do design, não do usuário) e **Steve Krug** (*Não Me Faça Pensar* — auto-evidência acima de tudo). Densidade é a alma do padrão; legibilidade é o que impede a densidade de virar ruído.

**Fonte de verdade desta seção:** as razões de contraste vêm de `check_marca.py` (`contrast_report` / `ratio`); os tamanhos de fonte, de `gerar_infografico.py` (canvas `1080×1350`). Nada aqui é estimado.

### Contraste WCAG — os limiares que o repo cobra

`check_marca.py` embute um relatório de contraste (`contrast_report`) que mede pares-chave no canvas escuro contra dois mínimos WCAG — e o site roda o mesmo no modo claro (`contrast_report_light`). Os **limiares que o código usa**:

- **Texto ≥ 4.5:1** (corpo e título — WCAG AA para texto normal).
- **Verde/ouro como cor de UI ≥ 3.0:1** (borda, ícone de linha, traço, rótulo — WCAG AA para componente/UI e texto grande).

Medições reais do nosso canvas escuro (`papel #08080c`):

| Par (papel `#08080c` ao fundo) | Razão | Mínimo no código | Veredito |
|---|---|---|---|
| Texto `tinta` `#f2f2f5` sobre fundo | **17.9:1** | 4.5 | passa folgado |
| Verde `#3faf76` sobre fundo | **7.2:1** | 3.0 | AA ok |
| Ouro `#d8a64a` sobre fundo | **9.0:1** | 3.0 | AA ok |
| Texto escuro (`papel`) sobre pílula verde | **7.2:1** | 4.5 | AA ok |

O texto principal passa com folga gigante (17.9:1) — é o piso confortável de todo corpo de texto. **A armadilha não é o branco sobre escuro; é o verde como texto.** O verde `#3faf76` mede 7.2:1 e é ótimo para *UI* (traço, ícone, rótulo curto, um título-palavra), mas:

> **Regra:** texto crítico de leitura longa (frase de promessa, subtítulo descritivo, aviso) **nunca** em verde médio sobre fundo escuro. Corpo longo é sempre `tinta` (`#f2f2f5`, 17.9:1). Verde é tinta de *etiqueta*, não de *parágrafo*. O verde-soft (`#a9e6c4`) só aparece em rótulo/badge curto, jamais numa linha corrida.

Sempre que mexer em cor de texto, rode `python check_marca.py` — ele reporta o contraste atualizado e falha se um gerador hardcodar uma cor antiga.

### Texto sobre imagem / objeto — sempre com proteção por baixo

Cada item da grade carrega um objeto fotorrealista (seções 04/07). Objeto tem áreas claras e escuras; texto solto sobre uma área clara vira ilegível e quebra os 17.9:1 que tanto cuidamos.

> **Regra prática:** **nenhum texto** repousa diretamente sobre o objeto. Todo texto sobre imagem ganha uma das três proteções, nesta ordem de preferência:
> 1. **Caixa/pílula** com fundo `papel` (ou escuro translúcido `oklch(16% 0.01 152 / .7)` ou mais opaco) — o padrão para rótulo e chip.
> 2. **Gradiente escuro** (scrim) subindo da base do objeto, quando o texto fica sobreposto à foto.
> 3. **Faixa de respiro escura** separando objeto e texto, quando dá para não sobrepor.

O objeto e o texto ocupam **zonas distintas** sempre que possível (texto na coluna, objeto no selo) — a sobreposição é a exceção, e a exceção pede scrim. Nunca confie no acaso de "essa foto é escura o bastante".

| ✅ Faça | ❌ Não faça |
|---|---|
| Rótulo numa pílula `papel` sobre o objeto | Texto branco solto sobre a parte clara de um objeto |
| Scrim escuro na base antes de qualquer legenda | "Essa imagem é escura, deve dar" — sem medir |
| Objeto no selo, texto na coluna (zonas separadas) | Título atravessando o meio da foto sem proteção |

### O teste do "billboard" (Krug) — a ideia em 0,5 segundo

Krug: uma página tem que comunicar como um *outdoor* — você passa de carro e pega a mensagem num relance. No feed é literal: o dedo rola, a peça tem **meio segundo** para entregar a ideia principal. Quem faz o trabalho pesado nesse meio segundo são **o título e o objeto** — não a grade densa, que é o prêmio para quem parou.

- **Título** = a promessa, em caixa-alta, peso 900, ~78px. Lê-se antes de tudo.
- **Objeto/selo da estrela** = a âncora visual que diz "do que isto trata".
- A grade densa de itens é a **recompensa de quem parou**, não a isca. Ela não precisa ser lida em 0,5s; o título e o objeto sim.

**Teste:** mostre a peça por meio segundo (ou reduza a miniatura ao tamanho de um polegar). Se a pessoa não souber dizer o tema, o título está fraco, pequeno ou competindo com ruído. Conserte o título/objeto antes de qualquer detalhe da grade.

### "Omita as palavras desnecessárias" (Krug)

A metade das palavras de uma peça pode sair sem perda; depois, metade de novo. Rótulo é etiqueta, não frase. Densidade não é *mais texto* — é mais *itens legíveis*, e isso exige texto curto por item.

| ❌ Antes (palavroso) | ✅ Depois (billboard) |
|---|---|
| "Lei nº 1 — Nunca ofusque o seu mestre, sempre faça com que aqueles acima de você se sintam confortavelmente superiores a você" | "1 · Nunca ofusque o mestre" |
| "Este é um princípio fundamental que você deve aplicar no seu dia a dia para obter melhores resultados" | "Aplique hoje" |
| "Clique aqui para saber mais sobre o conteúdo completo deste livro" | "Leia o resumo" |
| "Aviso importante: tenha cuidado ao aplicar esta tática" | "IMPORTANTE: use com cautela" |

Regra de bolso: **rótulo (`lbl`) cabe numa linha**; o descritivo (`sub`) é uma frase enxuta de apoio, não um parágrafo. Se um item precisa de parágrafo, ele não é item de grade — é outra peça.

### Ordem de leitura inequívoca

O leitor não deve *escolher* por onde começar. A hierarquia visual decide por ele (Krug: "deixe óbvio o que é mais importante"). O padrão do canvas `1080×1350` impõe um percurso único:

```
TÍTULO (topo, ~78px, 900)
   ↓
PROMESSA / subtítulo (uma linha, ~30px)
   ↓
ITENS da grade  — de cima para baixo, e dentro de cada linha esq → dir
   (selo/ícone → rótulo → chip de valor)
   ↓
RODAPÉ / aviso (registro final)
   ↓
marca-d'água (assinatura, menor de tudo)
```

Tamanho, peso e posição constroem essa escada. O título é o maior; o aviso e a marca-d'água, os menores. **Nada de dois elementos disputando o "primeiro olhar".** Se há dois títulos do mesmo tamanho, não há título.

### "A cor nunca é o único sinal" (Norman / daltonismo)

~8% dos homens têm alguma forma de daltonismo; somem o sol no celular e o matiz fica ainda menos confiável. Norman: a informação não pode depender de um só canal sensorial. **Toda categoria ou estado é sinalizado por pelo menos dois canais além da cor:** ícone de linha **+** rótulo de texto **+** posição.

- A estrela/CTA não é "a dourada" — é a que tem **selo + a palavra** ("comece aqui", "o melhor") **+** está na posição de honra.
- O aviso não é "a vermelha" — é a que diz **"IMPORTANTE" + ícone de aviso** no rodapé.
- Categorias não se distinguem por matiz (rejeitamos o arco-íris da seção 01) — distinguem-se por **ícone + rótulo + objeto**.

**Teste do cinza:** converta a peça para escala de cinza. Se ainda dá para navegar e entender quem é a estrela e quem é o aviso, está certo. Se a peça "desmonta" em cinza, a cor estava carregando informação sozinha — corrija.

### Tamanho mínimo legível — feed e miniatura

Valores reais do canvas `1080×1350` de `gerar_infografico.py`, com o piso prático para o feed mobile:

| Elemento | px no canvas 1080 | Papel |
|---|---|---|
| Título `h1` | **~78px** | Lê-se na miniatura; o billboard |
| Promessa / subtítulo | **~30px** | Uma linha; limiar do confortável |
| Linha da grade (`rows`) | **~40px** base | Corpo dos itens |
| Sub-descrição (`sub`) | **~26px** (`.65em`) | **Piso de leitura.** Abaixo disto, não desça |
| Chip / badge | **~20–21px** | Rótulo curtíssimo, caixa-alta |
| Marca-d'água | **~18px** | Assinatura; não carrega informação crítica |

> **Pisos práticos no canvas 1080:** texto que o leitor **precisa ler** ≥ **~26px**; nada informativo abaixo de **~18px** (esse patamar é só assinatura/marca-d'água, nunca conteúdo). Caixa-alta come legibilidade — rótulo em caps pede um corpo um pouco maior e *letter-spacing* (o padrão já aplica).

**A miniatura é outro produto.** Reduzida a thumbnail (e ainda mais a 16:9 do YouTube), só o **título** sobrevive. Regra da thumb:

- **Texto grande, pouquíssimo.** 3–5 palavras no máximo; o resto é objeto.
- Nunca dependa do `sub` de 26px na miniatura — ele some.
- Teste encolhendo a peça ao tamanho de um polegar: se o tema não aparece, o título não está grande/curto o bastante para a thumb.

### Densidade × respiro — quando cortar um item

A alma do padrão é a grade densa de catálogo. Mas denso **não é apertado**: precisa de ar entre linhas, margem interna, e o traço tracejado para respirar. O padrão do canvas reserva *padding* generoso (`70px 76px`) e a moldura tracejada recuada (`inset 38px`) — esse respiro é intocável.

**Quando cortar:** se para caber mais um item você precisa (a) reduzir o `sub` abaixo de ~26px, (b) comer o respiro entre linhas, ou (c) espremer o título — **corte o item**. Menos itens legíveis batem mais itens ilegíveis, sempre. Krug: o objetivo é que o leitor *entenda*, não que você *caiba tudo*.

- Grade confortável: tipicamente **5–7 linhas** no `1080×1350` sem sufocar.
- Passou disso e o `sub` encolheu? Promova os melhores itens, mande o resto para uma segunda peça (carrossel) ou para a página do site.

### Mini-checklist de legibilidade

1. **Texto crítico em `tinta` `#f2f2f5`** (17.9:1) — nunca corpo longo em verde médio.
2. **Nenhum texto sobre objeto sem scrim/caixa/gradiente** por baixo.
3. **Billboard:** título + objeto entregam a ideia em ~0,5s (teste do polegar).
4. **Palavras desnecessárias omitidas:** rótulo numa linha, zero parágrafo na grade.
5. **Ordem de leitura única:** título → itens (cima→baixo, esq→dir) → aviso → marca.
6. **Teste do cinza passa:** categoria/estado legíveis sem depender de matiz (ícone + rótulo + posição).
7. **Pisos de px respeitados:** texto informativo ≥ ~26px; nada legível abaixo de ~18px.
8. **Miniatura legível:** só o título grande sobrevive; 3–5 palavras, muito objeto.

---

## 09. Governança, Checklist & Guardrail

> *Padrão sem governança é só opinião bonita. Esta seção fecha a bíblia: transforma tudo o que veio antes (00–08) em **regra viva** — um checklist que se marca antes de cada peça, uma tabela de pecados capitais, e um **guardrail técnico que falha o build** se a marca derivar. Aqui o belo vira verificável.*

### 09.1 Checklist pré-voo (por peça)

Antes de declarar **qualquer** imagem pronta — carrossel, feed, Story, thumbnail, infográfico — passe esta lista. Marque de verdade. Uma caixa desmarcada é um motivo para não publicar.

**Paleta (seção 01)**
- [ ] Canvas é o **dark da marca**: fundo `#08080c` (papel), texto `#f2f2f5` (tinta).
- [ ] O **verde lidera** — `#3faf76` (verde) é a cor estrutural dominante da peça.
- [ ] O **ouro `#d8a64a` aparece no máximo como 1 acento** (destaque/realce premium), nunca como cor de fundo nem espalhado.
- [ ] O **alerta `#e8744f` só aparece em contexto de aviso/voto** — jamais decorativo.
- [ ] **Sem arco-íris**: nenhuma cor fora da paleta da marca. Categorias NÃO são distinguidas por matizes aleatórios.

**Objeto fotorrealista (seções 04–05)**
- [ ] Há **um objeto fotorrealista por item** (ocupa o slot circular/`seal`), não um ícone de linha.
- [ ] O objeto está **tingido na marca** (banhado no verde/ouro no compositing) — não é um stock cru fora da paleta.
- [ ] **Não há mistura**: nenhuma peça com ícone flat *e* objeto fotorreal lado a lado.
- [ ] Todos os objetos da peça pertencem ao **mesmo "mundo" material** (mesma família estética).

**Tipografia (seção 02)**
- [ ] Título em **Hanken Grotesk Black** (display) — `marca.font('display', s, 'Black')`, nunca fonte de sistema.
- [ ] Corpo/editorial em **Literata** (serif) onde a anatomia pede.
- [ ] Nenhuma `arial.ttf` / `ariblk.ttf` / `georgia.ttf` hardcodada — tudo via `marca.font(...)`.

**Anatomia & acabamento (seções 03, 07)**
- [ ] **Moldura + grão + grade de pontos** presentes (a textura premium do canvas).
- [ ] **Glow contido** — sem brilho estourado/clipado em volta do objeto.
- [ ] Hierarquia da grade respeitada (kicker → título → itens → assinatura).

**Legibilidade (seção 08)**
- [ ] Todo texto sobre imagem/objeto tem **scrim** (véu escuro por baixo) garantindo contraste.
- [ ] Cada categoria é sinalizada por **cor + ícone + rótulo** — **nunca só por cor** (acessibilidade; daltônico tem de distinguir).
- [ ] Contraste AA: tinta sobre papel ≥ 4.5:1; verde/ouro sobre papel ≥ 3.0:1 (validado em `check_marca.py`).

**Identidade & formato (seção 00)**
- [ ] Assinatura **@minutoreal1701** presente.
- [ ] **Formato/dimensão corretos** para o destino (feed 1:1, Story/Reel 9:16, thumbnail 16:9).

### 09.2 Faça / Não faça — os pecados capitais

| Faça | Não faça |
|---|---|
| Verde `#3faf76` lidera; ouro `#d8a64a` como **único** acento | **Arco-íris** — uma cor por categoria, paleta de banco de imagens |
| `marca.font('display', s, 'Black')` (Hanken) | **Fonte de sistema** (Arial/Calibri/Georgia hardcodada) |
| Um **objeto fotorrealista** por item, na marca | **Misturar** ícone flat com objeto fotorreal na mesma peça |
| Tingir o objeto na cor da marca no compositing | Objeto **fora da paleta** (stock cru, azul/vermelho aleatório) |
| **Scrim** sob todo texto que cai sobre imagem | Texto **sem scrim** — branco sumindo no claro do objeto |
| Glow sutil, sob controle | **Glow estourado** (halo clipado, "brilho de Word") |
| Sinalizar categoria por **cor + ícone + rótulo** | **Cor como único sinal** (falha para daltônicos) |
| Ler toda cor/fonte de `marca.py` | **Hardcodar** `#d8a64a`, `arial.ttf`, OKLCH antigo |

### 09.3 O guardrail técnico — `check_marca.py`

A marca não depende de boa vontade: ela é **defendida por código**. `marca.py` é a **fonte única de verdade** (toda cor e fonte saem de `TOKENS` e `font()`), e `check_marca.py` é o porteiro que garante que ninguém burlou isso.

**Como rodar (antes de fechar trabalho de imagem):**

```
python check_marca.py
```

Sai com **código ≠ 0 se houver deriva** — pode (e deve) entrar em CI/pré-commit para barrar regressões.

**O que ele faz, em três frentes:**

**(A) `scan_drift()` — caça hardcode.** Varre cada arquivo da lista **`TARGETS`** e procura, linha a linha, qualquer token do dict **`FORBIDDEN`**. Se achar, imprime `DRIFT <arquivo>:<linha> "<token>" — <correção>` e incrementa o contador. Os `TARGETS` hoje:

```
gerar_carrossel.py, gerar_infografico.py, assets/style.css,
videos/gerar_video.py, videos/gerar_thumb.py, videos/gerar_canal_art.py
```

O dict `FORBIDDEN` proíbe, entre outros: `#d8a64a` (ouro hardcoded → use `marca.hex_of("ouro")`), `ariblk.ttf`/`arial.ttf`/`georgia.ttf` (fontes de sistema → `marca.font(...)`), e os **OKLCH antigos** que ficaram para trás na unificação (ex.: `oklch(84% 0.115 92)` ouro h92, `oklch(73% 0.15 152)` verde L73). Achou? **Drift — build falha.**

**(B) Contraste no canvas escuro — `contrast_report()`.** Calcula a razão WCAG dos pares-chave lendo as cores **da própria marca** (`marca.hex_of(...)`): tinta sobre papel (min 4.5), verde sobre papel (min 3.0), ouro sobre papel (min 3.0), texto escuro sobre pílula verde (min 4.5). Cada par sai marcado `AA ok` ou `ABAIXO`.

**(C) Contraste no modo claro do site — `contrast_report_light()`.** Mesmo relatório para o tema claro, convertendo os OKLCH `[0]` de `marca.TOKENS` para sRGB (`oklch_to_srgb`).

**Regra de ouro do guardrail — para QUALQUER novo gerador de imagem:**
1. **Leia cor/fonte de `marca.py`** (`hex_of`, `rgb`, `font`, `css_root`). Zero hardcode.
2. **Entre na lista `TARGETS`** de `check_marca.py`. Um gerador fora dos `TARGETS` é um gerador sem porteiro — é onde a deriva volta a entrar.

> Hoje `gerar_infografico.py` **já está** nos `TARGETS`. Todo gerador futuro de objeto/imagem segue o mesmo caminho.

### 09.4 Fluxo de produção do objeto (gera-uma-vez → cache)

O objeto-por-conceito segue **exatamente** o mesmo espírito dos campos curados que `gerar_infografico.py` já lê (`FLUXO`, `COMPARA`, `NUMEROS`, `ANATOMIA`): é **dado curado no `_data.py` do livro**, não improvisado no gerador.

| Etapa | O quê | Onde |
|---|---|---|
| **1. Curar** | Declarar o objeto-símbolo de cada conceito como **campo no `<slug>_data.py`** (mesmo padrão de `FLUXO`/`COMPARA`) | `<slug>_data.py` |
| **2. Prompt** | Montar o prompt fotorrealista do objeto conforme a **seção 05** | seção 05 |
| **3. Gerar** | Render via **`videos/imagen.py`** (Google Imagen) — passa por `cost_tracker` + `circuit_breaker` | `videos/imagen.py` |
| **4. Tingir** | Aplicar a **tinta de marca** no compositing (verde/ouro), banhar na paleta | compositing |
| **5. Cachear** | Salvar o ativo **versionado em disco** — gera-uma-vez, reusa em tudo | `assets/kit/<slug>/...` |

**Disciplina de custo (Modo Soberano).** O Imagen custa na conta Google do usuário. Por isso: **gera-se uma vez por conceito, tinge-se, e guarda-se em cache versionado**. As peças seguem rodando local/grátis; a IA é a **exceção**, não a rotina. O `circuit_breaker` em `imagen.py` é o freio de mão — se algo dispara, a geração para, não sangra orçamento.

**Onde os assets vivem.** O cache do objeto fica junto dos demais ativos do livro, no padrão já em uso:

```
assets/kit/<slug>/        ← capa-story.png, citacao-feed.png, manifest.json, caps/, thumbs/, [objetos]
```

Como em `gerar_infografico.py`, **a presença do campo no `_data.py` controla a geração** (lá, `if field and not hasattr(data, field): pula`). Sem o campo curado, sem objeto — o gerador degrada com graça, nunca quebra.

### 09.5 Versionamento da bíblia

Esta bíblia é **documento vivo**, não tábua de pedra.

- **Dono:** Diretor de Design (lane de unificação da rede, nomeada 14/jun/2026).
- **Registro:** toda revisão anota **data + versão** no cabeçalho do documento mestre.
- **Processo de mudança:** qualquer alteração de padrão (nova cor, nova fonte, novo arquétipo, mudança no objeto) **passa por aqui** — atualiza-se a seção pertinente **e**, se for cor/fonte, atualiza-se `marca.py` (fonte única) e o `FORBIDDEN`/`TARGETS` de `check_marca.py` no mesmo movimento. Bíblia e guardrail andam juntos: mudar uma sem a outra é criar deriva.
- **Critério de aceite de um padrão novo:** ele só é "lei" quando (a) está escrito nesta bíblia, (b) sai de `marca.py`, e (c) é coberto por `check_marca.py`.

### Regra de ouro da governança

> **Se a cor ou a fonte não saiu de `marca.py` e não passou no `python check_marca.py`, a peça não está pronta — por mais bonita que pareça.**
