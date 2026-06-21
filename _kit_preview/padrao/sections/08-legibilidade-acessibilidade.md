## 08. Legibilidade & Acessibilidade

A lente do **leitor**. As seções anteriores definem o que a peça *é* (cor, tipo, anatomia, objeto); esta define o que o leitor *consegue ler* — rolando o feed no celular, sob sol, daltônico, em 0,5 segundo. Duas vozes governam aqui: **Don Norman** (*O Design do Dia a Dia* — a culpa é do design, não do usuário) e **Steve Krug** (*Não Me Faça Pensar* — auto-evidência acima de tudo). Densidade é a alma do padrão; legibilidade é o que impede a densidade de virar ruído.

**Fonte de verdade desta seção:** as razões de contraste vêm de `check_marca.py` (`contrast_report` / `ratio`); os tamanhos de fonte, de `gerar_infografico.py` (canvas `1080×1350`). Nada aqui é estimado.

---

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

---

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

---

### O teste do "billboard" (Krug) — a ideia em 0,5 segundo

Krug: uma página tem que comunicar como um *outdoor* — você passa de carro e pega a mensagem num relance. No feed é literal: o dedo rola, a peça tem **meio segundo** para entregar a ideia principal. Quem faz o trabalho pesado nesse meio segundo são **o título e o objeto** — não a grade densa, que é o prêmio para quem parou.

- **Título** = a promessa, em caixa-alta, peso 900, ~78px. Lê-se antes de tudo.
- **Objeto/selo da estrela** = a âncora visual que diz "do que isto trata".
- A grade densa de itens é a **recompensa de quem parou**, não a isca. Ela não precisa ser lida em 0,5s; o título e o objeto sim.

**Teste:** mostre a peça por meio segundo (ou reduza a miniatura ao tamanho de um polegar). Se a pessoa não souber dizer o tema, o título está fraco, pequeno ou competindo com ruído. Conserte o título/objeto antes de qualquer detalhe da grade.

---

### "Omita as palavras desnecessárias" (Krug)

A metade das palavras de uma peça pode sair sem perda; depois, metade de novo. Rótulo é etiqueta, não frase. Densidade não é *mais texto* — é mais *itens legíveis*, e isso exige texto curto por item.

| ❌ Antes (palavroso) | ✅ Depois (billboard) |
|---|---|
| "Lei nº 1 — Nunca ofusque o seu mestre, sempre faça com que aqueles acima de você se sintam confortavelmente superiores a você" | "1 · Nunca ofusque o mestre" |
| "Este é um princípio fundamental que você deve aplicar no seu dia a dia para obter melhores resultados" | "Aplique hoje" |
| "Clique aqui para saber mais sobre o conteúdo completo deste livro" | "Leia o resumo" |
| "Aviso importante: tenha cuidado ao aplicar esta tática" | "IMPORTANTE: use com cautela" |

Regra de bolso: **rótulo (`lbl`) cabe numa linha**; o descritivo (`sub`) é uma frase enxuta de apoio, não um parágrafo. Se um item precisa de parágrafo, ele não é item de grade — é outra peça.

---

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

---

### "A cor nunca é o único sinal" (Norman / daltonismo)

~8% dos homens têm alguma forma de daltonismo; somem o sol no celular e o matiz fica ainda menos confiável. Norman: a informação não pode depender de um só canal sensorial. **Toda categoria ou estado é sinalizado por pelo menos dois canais além da cor:** ícone de linha **+** rótulo de texto **+** posição.

- A estrela/CTA não é "a dourada" — é a que tem **selo + a palavra** ("comece aqui", "o melhor") **+** está na posição de honra.
- O aviso não é "a vermelha" — é a que diz **"IMPORTANTE" + ícone de aviso** no rodapé.
- Categorias não se distinguem por matiz (rejeitamos o arco-íris da seção 01) — distinguem-se por **ícone + rótulo + objeto**.

**Teste do cinza:** converta a peça para escala de cinza. Se ainda dá para navegar e entender quem é a estrela e quem é o aviso, está certo. Se a peça "desmonta" em cinza, a cor estava carregando informação sozinha — corrija.

---

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

---

### Densidade × respiro — quando cortar um item

A alma do padrão é a grade densa de catálogo. Mas denso **não é apertado**: precisa de ar entre linhas, margem interna, e o traço tracejado para respirar. O padrão do canvas reserva *padding* generoso (`70px 76px`) e a moldura tracejada recuada (`inset 38px`) — esse respiro é intocável.

**Quando cortar:** se para caber mais um item você precisa (a) reduzir o `sub` abaixo de ~26px, (b) comer o respiro entre linhas, ou (c) espremer o título — **corte o item**. Menos itens legíveis batem mais itens ilegíveis, sempre. Krug: o objetivo é que o leitor *entenda*, não que você *caiba tudo*.

- Grade confortável: tipicamente **5–7 linhas** no `1080×1350` sem sufocar.
- Passou disso e o `sub` encolheu? Promova os melhores itens, mande o resto para uma segunda peça (carrossel) ou para a página do site.

---

### Mini-checklist de legibilidade (feche por aqui)

1. **Texto crítico em `tinta` `#f2f2f5`** (17.9:1) — nunca corpo longo em verde médio.
2. **Nenhum texto sobre objeto sem scrim/caixa/gradiente** por baixo.
3. **Billboard:** título + objeto entregam a ideia em ~0,5s (teste do polegar).
4. **Palavras desnecessárias omitidas:** rótulo numa linha, zero parágrafo na grade.
5. **Ordem de leitura única:** título → itens (cima→baixo, esq→dir) → aviso → marca.
6. **Teste do cinza passa:** categoria/estado legíveis sem depender de matiz (ícone + rótulo + posição).
7. **Pisos de px respeitados:** texto informativo ≥ ~26px; nada legível abaixo de ~18px.
8. **Miniatura legível:** só o título grande sobrevive; 3–5 palavras, muito objeto.
