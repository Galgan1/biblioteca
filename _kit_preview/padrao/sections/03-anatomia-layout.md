## 03. Anatomia da Peça (DNA do Layout)

Toda peça do Minuto Real é a mesma **planta baixa** vestida em conteúdos diferentes. Quem lê de relance precisa reconhecer "isto é nosso" em 200 ms — antes de ler uma palavra. Esse reconhecimento mora na **estrutura**, não no texto: cinco zonas empilhadas de cima para baixo, sempre na mesma ordem, sempre com o mesmo respiro.

Os valores aqui são os **reais** de `gerar_infografico.py` (canvas `.slide` 1080×1350, padding `70px 76px 50px`). Quando um arquétipo diverge, está anotado.

---

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

---

### Elementos estruturais de fundo (o "cromo" da marca)

Três camadas vivem **atrás** do conteúdo (z-0) e são o que faz a peça parecer impressa, não um slide de PowerPoint:

| Elemento | CSS real | Função |
|---|---|---|
| **Moldura tracejada** | `.slide::after` · `inset:38px` · `border:2px dashed var(--green)` · `border-radius:32px` · `opacity:.38` | a "borda do bilhete"; emoldura toda a peça |
| **Grade de pontos** | `.slide::before` · `radial-gradient` 1.1px · `background-size:36px 36px` · máscara que some no topo | textura de papel técnico; nunca compete com o texto |
| **Número-fantasma** | `.ghost` · peso 900 · `-webkit-text-stroke:2px` (verde a ~9% opacidade) · `letter-spacing:-.05em` · com máscara radial | um glifo gigante (→, %, VS) atrás do conteúdo, dá profundidade e "assunto" |

> O conteúdo real fica em `.slide > *` com `position:relative; z-index:1` — sempre **acima** das três camadas.

---

### Ritmo & espaçamento

- **Margem de segurança:** o padding (`~70px` lateral) e a moldura (`inset:38px`) criam uma **zona morta** nas bordas. Nada de texto ou objeto encosta na moldura.
- **Respiro vertical:** o corpo usa `justify-content:space-between` (LISTA) — os itens se distribuem para preencher a altura sem amontoar. A peça **nunca** tem um bloco gordo em cima e vazio embaixo.
- **Alinhamento à grade:** selos, rótulos e chips alinham em colunas verticais consistentes (o `grid` de 3 colunas garante isso). Olho do leitor desce em linha reta.
- **Auto-fit:** um passo de JS (`_FIT_JS`) encolhe o `h1` que estoura a largura (até 40px) e o corpo `.fitv` que estoura a altura (1px por vez). **O layout se adapta ao conteúdo, não o contrário** — mas isso é rede de segurança, não desculpa para texto longo.

---

### Grids por formato

O arquivo gera nativamente o **feed 4:5**. Os demais formatos reusam o mesmo DNA (zonas + cromo), reescalando a contagem de itens:

| Formato | Dimensões | Proporção | Itens que cabem bem | Observação |
|---|---|---|---|---|
| **Feed** | 1080×1350 | 4:5 | **5–6** itens de catálogo (ou 4 passos de fluxo) | formato nativo de `gerar_infografico.py` (`_even_sample(..., 6)`) |
| **Quadrado** | 1080×1080 | 1:1 | **4** itens | menos altura → corte do corpo; rótulos mais curtos |
| **Story** | 1080×1920 | 9:16 | **6–7** itens, ou 1 conceito gigante | sobra altura → cabeçalho maior + CTA "arrasta"; respeitar zona segura do topo/rodapé (UI do app) |
| **Thumb** | 1280×720 | 16:9 | **1–3** | é cartaz, não catálogo: título-herói domina, no máximo 3 objetos |

Regra geral: **quanto mais largo o formato, menos itens** (a altura é o que comporta a coluna). O número-fantasma e a moldura escalam junto; brandmark e assinatura **nunca** somem.

---

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
