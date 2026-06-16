## 01. Paleta & Cor

A referência canônica de cor do padrão Minuto Real / Biblioteca. **Fonte de verdade:** `marca.py` (dicionário `TOKENS`) e a doutrina escrita no topo desse arquivo. Nada aqui é inventado — todo HEX e OKLCH abaixo foi confirmado em `marca.py`; toda razão de contraste foi medida por `check_marca.py`. Se um valor divergir do código, o código vence. **Não crie tokens novos.**

---

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

---

### A doutrina (decidida em 14/jun/2026 — está escrita no topo de `marca.py`)

Três frases governam toda decisão de cor:

1. **Verde (hue 152) é a cor-mãe e lidera.** É a identidade da Biblioteca. O verde aparece no traço tracejado, nos ícones de linha, nos rótulos, na UI. Quando você está em dúvida sobre que cor usar, a resposta padrão é **verde**.
2. **UM ouro (hue 83) é o único acento premium.** Ancorado no âmbar **`#d8a64a`**, que já carrega o *equity* visual do YouTube do canal. Não há um segundo acento. Não existe "azul de apoio", "roxo de seção", nem nada disso. Ouro é a única voz que pode interromper o verde.
3. **Alerta (hue ~30, `#e8744f`) é exceção rara.** Existe só para o registro de aviso ("IMPORTANTE", caução, perigo). Não é decoração; é semântica.

A âncora **`#d8a64a`** é tão central que `check_marca.py` proíbe hardcodá-la nos geradores: o código deve sempre puxar `marca.hex_of("ouro")`. Isso garante que mudar a marca seja mudar **um** valor, em **um** arquivo.

---

### Proporção de cor (o "orçamento" cromático de uma peça)

A peça é predominantemente escura e verde; o ouro é um tempero, não um ingrediente.

| Faixa | Papel | Onde |
|---|---|---|
| **~70%** | Neutros escuros (`papel`, `tinta`, `tinta-fraca`) | Fundo, corpo de texto, grades, respiro |
| **~20–25%** | Verde (`verde`, `verde-deep`, `verde-soft`) | Traço, ícones, rótulos, hierarquia, brilhos |
| **< ~10%** | Ouro (`ouro`, `ouro-soft`) | **Só** o ponto de destaque: CTA, a "estrela" da grade, o selo premium |
| **Raríssimo** | Alerta (`alerta`) | Só o registro de aviso, quando ele de fato existir |

Regra prática: **um único ouro por peça** na maioria dos casos. Se há ouro em três lugares, ele deixou de ser destaque e virou ruído — escolha o um que mais importa e devolva os outros ao verde.

---

### Rejeição explícita do arco-íris

As referências de "alma" que copiamos (guias de fusível, tipos de fita) muitas vezes pintam **cada coluna/categoria de uma cor diferente**. **Nós não fazemos isso.** Copiamos a *organização* densa e elegante daquelas peças — a ALMA — **não** a paleta arco-íris.

- ❌ Categoria A em azul, B em roxo, C em laranja, D em rosa.
- ✅ Todas as categorias na mesma família verde/escura; **a categoria se distingue por ícone + rótulo + objeto fotorrealista**, nunca por matiz.

A cor não é o eixo de categorização. O eixo é o **ícone de linha**, o **rótulo de texto** e o **objeto**. A cor só carrega hierarquia (verde lidera, ouro destaca) e semântica (alerta avisa).

---

### "A cor nunca é o único sinal"

Acessibilidade não é opcional. Quem é daltônico ou está num celular sob sol forte não pode depender do matiz. Por isso **toda informação carregada por cor é sempre pareada com um segundo sinal**:

- Verde de destaque → **+ ícone + rótulo**.
- Ouro de "estrela/CTA" → **+ ícone/selo + texto** ("o melhor", "comece aqui").
- Alerta vermelho-terra → **+ a palavra "IMPORTANTE" + ícone de aviso**.

Se você apagasse toda a cor da peça e a transformasse em escala de cinza, ela ainda deveria ser **legível e navegável**. Esse é o teste.

---

### Cor sobre o objeto fotorrealista

Cada item da grade tem um objeto fotorrealista (detalhe nas seções 04 e 07). Princípio cromático aqui: **o objeto deve pertencer ao mundo verde da marca** — tratado como tinta de marca / duotone verde, não como foto de banco de imagem colorida e crua. O objeto não pode reintroduzir o arco-íris pela porta dos fundos. *(O "como" — duotone, grade, sombra, iluminação — fica nas seções 04/07.)*

---

### Contraste (medido por `check_marca.py`, canvas escuro)

O texto e os acentos passam WCAG com folga. Estes números saem do relatório de contraste embutido em `check_marca.py` (`contrast_report`):

| Par | Razão | Mínimo WCAG | Veredito |
|---|---|---|---|
| Texto (`tinta` `#f2f2f5`) sobre fundo (`papel` `#08080c`) | **17.9:1** | 4.5 | AA folgado |
| Verde (`#3faf76`) sobre fundo | **7.2:1** | 3.0 | AA ok |
| Ouro (`#d8a64a`) sobre fundo | **9.0:1** | 3.0 | AA ok |
| Texto escuro sobre pílula verde | **7.2:1** | 4.5 | AA ok |

O mesmo guardrail roda um relatório paralelo para o **modo claro do site** (`contrast_report_light`), confirmando texto/verde/ouro sobre o papel claro. Sempre que mexer em cor, rode `python check_marca.py` — ele falha se algum gerador hardcodar uma cor antiga proibida e reporta o contraste atualizado.

---

### Cores PROIBIDAS (o guardrail rejeita)

`check_marca.py` mantém uma lista `FORBIDDEN` de valores antigos que **não podem** voltar a aparecer:

- `#d8a64a` **hardcoded** → use `marca.hex_of("ouro")` (o valor é certo, o hardcode é o erro).
- `oklch(84% 0.115 92)` → ouro antigo (hue 92) → use o ouro de marca (hue **83**).
- `oklch(75% 0.16 38)` → alerta antigo (hue 38) → use alerta de marca (hue **30**).
- `oklch(73% 0.15 152)` → verde antigo (L73) → use verde de marca (**L70**).
- Fontes `ariblk.ttf` / `arial.ttf` / `georgia.ttf` hardcoded → use `marca.font(...)`.

---

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
