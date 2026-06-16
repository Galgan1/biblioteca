## 05. Molde de Prompt

> *Como gerar o objeto-símbolo já vestido na nossa estética, num prompt só. A seção 04 (Objeto) decide **qual** objeto representa cada conceito — a direção de arte. Esta seção entrega **o template de texto** que manda esse objeto para o Imagen e volta no nosso mundo verde. Os dois andam juntos: 04 escolhe o herói; 05 o fotografa.*

**Arquivo de verdade:** `videos/imagen.py`. A interface real é `gen(prompt, out_png, aspect='16:9')` — ela monta `{'instances':[{'prompt': ...}], 'parameters':{'sampleCount':1,'aspectRatio': aspect}}` contra `imagen-4.0-generate-001` (com fallback `-fast`). **Só existem dois campos que nós controlamos: o `prompt` (texto livre) e o `aspect`.** Não há `seed`, não há `negativePrompt`, não há `guidanceScale` exposto nessa API. Tudo o que queremos — o objeto, a luz, a cor, o que recusar — mora dentro da string `prompt`.

---

### Por que o prompt é em inglês

O Imagen 4 foi treinado predominantemente em legendas em inglês. **Prompts em inglês rendem objetos mais nítidos, luz mais previsível e menos "deriva" de estilo** do que os mesmos prompts em português. Por isso a regra desta seção:

> **A bíblia é escrita em pt-BR; os PROMPTS de imagem são escritos em inglês.**

O texto que o leitor vê na peça continua em português (ele é desenhado depois, em camada própria — seções 02/03). O inglês fica só na ordem que mandamos ao gerador. E como o template é fixo, ninguém precisa "saber inglês" para operar: troca-se **uma** variável (o objeto) e o resto é colado.

---

### Negativos sem campo de negativo

A API do Imagen **não tem `negativePrompt` separado** (diferente do Stable Diffusion). O que rejeitamos — texto na imagem, arco-íris, cartoon, multidão de objetos — vai **embutido no fim da string**, em linguagem afirmativa-de-recusa: `no text, no rainbow colors, no cartoon`. Esse rabo de negativos é **parte fixa da assinatura de estilo** e nunca sai. É ele que impede o Imagen de "ajudar" colando uma legenda ou pintando o objeto de sete cores.

---

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

---

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

---

### Aspect ratio por uso

O `aspect` é o segundo (e último) parâmetro. Passe o formato certo direto no `gen`:

| Uso | Aspect | Chamada |
|---|---|---|
| **Slot de card** (objeto isolado p/ a grade do infográfico) | `1:1` | `gen(prompt, out, aspect='1:1')` |
| **Feed Instagram** (peça vertical) | `4:5` | `gen(prompt, out, aspect='4:5')` |
| **Story / Reels** | `9:16` | `gen(prompt, out, aspect='9:16')` |
| **Thumbnail YouTube / capa larga** | `16:9` | `gen(prompt, out, aspect='16:9')` *(default)* |

**Regra prática:** o objeto-herói da grade quase sempre é gerado em **`1:1`** (slot quadrado, recortável), porque é a peça que mais se reusa entre formatos. O `16:9` é só para a arte de capa/thumbnail onde o objeto ocupa a cena inteira. Quando em dúvida, gere `1:1` — sobra moldura para encaixar em qualquer layout.

---

### Consistência entre objetos (o "mesmo mundo")

92+ livros, dezenas de objetos. O que faz todos parecerem do mesmo acervo:

1. **Mesma frase de estilo, byte a byte.** Não "melhore" a assinatura de um objeto para o outro. Se mudar a luz num, mude em todos — ou nenhum. O estilo é constante; o objeto é a variável.
2. **Gere em lote.** Rode todos os objetos de um livro (ou de um agrupamento das 48 Leis) **na mesma sessão**, com a mesma string de estilo, para que a luz e o grão "casem". Lotes separados em dias diferentes derivam.
3. **Mesma luz, mesma direção.** Key verde sempre vindo do mesmo lado, rim verde marcando a silhueta, fundo sempre `#08080c`. É a iluminação que costura objetos diferentes numa família.
4. **Sobre seeds e variações:** essa API **não expõe seed** — não dá para "fixar" um resultado. A consequência prática: gere **2–3 amostras** por objeto (rode o `gen` mais de uma vez no mesmo prompt) e **escolha a melhor à mão**. A reprodutibilidade vem do *cache* — depois de aprovado, o objeto é guardado e reusado (doutrina "gera uma vez, reusa sempre" da seção 00), não regenerado.

---

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

---

### Dica de ouro: o acento sem virar arco-íris

O ouro (`#d8a64a`) é o tempero — **um ponto de brilho quente, não a peça inteira** (seção 01, "< ~10%"). Como pedir isso ao Imagen sem ele dourar tudo:

- Peça o ouro como **um evento único e pequeno**: `one small warm gold glint / highlight / reflection`, sempre no singular, sempre com `one small`.
- **Ancore o ouro num ponto físico** do objeto ("on the crown", "at the very center", "on a single link"). Ouro flutuante vira névoa dourada e domina a cena.
- **Nunca** escreva `golden object`, `gold and green`, nem liste o ouro como cor co-protagonista. Ele é um *glint*, não um banho.
- Se o objeto sair dourado demais, **não tire o ouro do prompt** — mova-o para um ponto menor (`a single glint on the edge`) e reforce `dominant green tones`.

A hierarquia no prompt espelha a da peça: **verde domina (key + rim + spill), ouro é um único reflexo.** Escrito nessa ordem, o Imagen respeita a proporção.

---

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
