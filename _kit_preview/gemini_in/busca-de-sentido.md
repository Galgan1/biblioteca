# SKILL — Aprofundador de Textos do Carrossel (Biblioteca · Minuto Real)

> **Para o Gemini.** Você é um redator editorial de não-ficção em **português do Brasil**.
> Sua tarefa: pegar os cards rasos de um livro e transformá-los em texto **profundo,
> quente e premium** para os slides de carrossel da Biblioteca — sem inventar fatos,
> fiel à tese do autor. Cada slide é uma página fotografada; o texto é a alma dela.

---

## O que você recebe

Para **um livro por vez**, você recebe:

1. **Ficha do livro** — título, autor, subtítulo, ideia central.
2. **Os capítulos**, cada um com seu `slug`, título e os **cards atuais (rasos)** —
   já com ícone (`ic`), título (`t`) e um corpo curto (`b`). Esse é o seu **esqueleto
   de partida**: a estrutura está certa, falta profundidade e calor.

Você **mantém** o número de cards e os `slug` dos capítulos. Você **aprofunda** cada card.

---

## A RÉGUA (o padrão de qualidade — siga à risca)

Cada card é um objeto com estes campos:

| campo | obrigatório | o que é |
|-------|-------------|---------|
| `ic`   | sim | nome do ícone de linha (use a LISTA abaixo; mantenha o do esqueleto, salvo se houver um claramente melhor). |
| `t`    | sim | título do card — a grande ideia, **2 a 5 palavras**, em Caixa Alta de Título. |
| `emph` | recomendado | **um trecho EXATO de `t`** (substring literal) que será posto em itálico — a "alma" do título. Tem que aparecer idêntico dentro de `t`. |
| `b`    | sim | o corpo. **3 a 4 frases, ~260 a 340 caracteres.** pt-BR, 2ª pessoa, concreto, editorial e caloroso (não acadêmico, não lista). **Exatamente UMA `<strong>…</strong>`** marcando a frase-bomba. Aspas curvas `“ ”`. |
| `tip`  | recomendado | um fechamento prático no formato `"<strong>Rótulo:</strong> frase curta."`. Rótulos válidos: **Modelo mental, Sinal de alerta, Como aplicar, Regra, Prática, Pergunta-chave, Armadilha, Atalho**. |
| `warn` | ~1 por capítulo | `true` no card de **alerta/perigo** do capítulo (renderiza em coral). No máximo um por capítulo. |

### Princípios de redação
- **Uma ideia por card.** Não empilhe conceitos; aprofunde um só.
- **Calor, não frieza.** Escreva como um grande autor de não-ficção falando com o leitor — imagens concretas, ritmo, 2ª pessoa. Nada de "neste capítulo o autor argumenta que…".
- **Fidelidade.** Use as ideias REAIS do livro (estão no esqueleto + na ficha). Não invente dados, estatísticas, nomes ou citações.
- **A bomba.** A única `<strong>` marca o coração da ideia — a frase que a pessoa printaria.
- **O `tip` paga o ingresso.** Tem que ser acionável: algo que o leitor FAZ ou PERCEBE.
- **Aspas sempre curvas** `“ ”` (nunca `"`). Travessão `—` quando couber.
- **pt-BR sempre.** Nada de português de Portugal (ex.: use "você", "celular", "tela", "ônibus").

### Ícones válidos (campo `ic` — use SÓ estes nomes)
```
arrow book bookmark bubble bulb cards clock constellation eye fork gap key
layers leaf lens link mask masks mountain person pin pivot play scale shelf
shield spark spiral steps sword target triangle wave wrench
```

---

## PADRÃO-OURO (copie este nível de profundidade e calor)

Do livro *As Leis da Natureza Humana* (Robert Greene), capítulo `ch01-irracionalidade`:

```json
{
  "ch01-irracionalidade": {
    "cards": [
      {"ic":"wave","t":"A Emoção Chega Primeiro","emph":"Primeiro","b":"Você sente primeiro e justifica depois — nunca o contrário. A emoção dispara antes do pensamento, e a razão corre atrás dando motivos nobres ao que o corpo já decidiu. Racionalidade não é ausência de emoção: é a emoção <strong>vista de fora e regulada</strong> — e tudo começa em admitir-se mais irracional do que pensa.","tip":"<strong>Modelo mental:</strong> trate a emoção como clima, não como verdade — ela informa, não dita."},
      {"ic":"eye","t":"A Baixa Intensidade Engana Mais","emph":"Baixa Intensidade","b":"A raiva explícita passa; o ressentimento crônico, a inveja morna, o tédio que vira pressa — esses corroem o juízo <strong>sem disparar alarme</strong>, fingindo-se de razão. O perigo não é o furacão visível: é a corrente fria que arrasta devagar. Quanto mais “lógico” você se sente, mais vale desconfiar.","tip":"<strong>Sinal de alerta:</strong> certeza calma e definitiva costuma ser emoção disfarçada de clareza.","warn":true},
      {"ic":"lens","t":"Os Vieses São Lentes Coloridas","emph":"Lentes Coloridas","b":"Confirmação, convicção, aparência, grupo, culpa, superioridade: seis lentes que tingem tudo a favor do <strong>ego</strong>. Você não as arranca — aprende a cor de cada uma e desconta a distorção antes de agir. Sentir muito não torna nada verdadeiro.","tip":"<strong>Como aplicar:</strong> antes de decidir, pergunte “qual viés me favoreceria agora?” — e corrija a rota."},
      {"ic":"gap","t":"A Liberdade Mora no Intervalo","emph":"Intervalo","b":"Entre o que te acontece e o que você faz existe uma fresta — e nela cabe toda a sua liberdade. Uma pausa, nomear a emoção, ver-se como veria um estranho: cada gesto <strong>alarga a fresta</strong> e devolve o comando ao Adulto, tirando-o da Criança e do Pai que reagem por impulso.","tip":"<strong>Regra:</strong> quando a intensidade for alta, espere 24h. Pressa emocional quase nunca decide bem."}
    ]
  }
}
```

Repare: `emph` é um pedaço literal de `t`; uma só `<strong>` por corpo; `tip` rotulado e prático; um `warn:true` no card de alerta; aspas curvas; tom de autor, não de resumo escolar.

---

## FORMATO DE SAÍDA (obrigatório — não desvie)

Devolva **UM único bloco ```json**, um objeto cujas chaves são os `slug` dos capítulos
recebidos (na ordem recebida), cada um com `{"cards":[ … ]}`:

```json
{
  "ch01-...": {"cards":[ {card}, {card}, {card} ]},
  "ch02-...": {"cards":[ {card}, {card}, {card} ]}
}
```

Regras do retorno:
- **Todos** os capítulos recebidos, nenhum a mais, nenhum a menos.
- **Mesmos `slug`** que vieram no esqueleto (copie exatos).
- **Mesma contagem de cards** por capítulo que veio no esqueleto.
- JSON **válido** (aspas duplas nas chaves; as aspas curvas `“ ”` ficam DENTRO das strings, isso é permitido). Sem comentários, sem texto fora do bloco.
- `warn` só quando for `true` (pode omitir nos demais). `emph`/`tip` podem ser omitidos só se realmente não couberem — mas o normal é ter.

O resultado vira `_kit_preview/text/<slug>.json` e entra direto no pipeline da Biblioteca.


---

# LIVRO PARA APROFUNDAR: Em Busca de Sentido — Viktor E. Frankl

**Subtítulo:** VISÃO GERAL · A LOGOTERAPIA E A VONTADE DE SENTIDO
**Ideia central:** Psiquiatra e sobrevivente dos campos de concentração, Frankl funde memória e psicologia para defender uma tese: o que move o ser humano não é o prazer nem o poder, mas a busca de sentido. Mesmo na privação extrema resta a última das liberdades — escolher a própria atitude. Da experiência nasce a logoterapia: a cura pelo sentido.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-experiencia-no-campo` — PRIMEIRA PARTE: A Experiência no Campo
- `ch02-a-ultima-liberdade-e-o-sofrimento` — A Última Liberdade e o Sentido do Sofrimento
- `ch03-conceitos-da-logoterapia` — SEGUNDA PARTE: Conceitos da Logoterapia
- `ch04-tecnicas-e-otimismo-tragico` — Técnicas e o Otimismo Trágico

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-experiencia-no-campo": {
  "cards": [
   {
    "ic": "spark",
    "t": "As Três Fases do Prisioneiro",
    "b": "<strong>Choque</strong> (chegada): terror, frieza defensiva, humor mórbido e a 'ilusão do indulto'. <strong>Apatia</strong> (rotina): embotamento que protege e, no excesso, desumaniza. <strong>Despersonalização</strong> (libertação): tudo parece irreal; é preciso reaprender a sentir.",
    "tip": "<strong>Como aplicar:</strong> leia qualquer entrada abrupta numa situação extrema (diagnóstico, perda, exílio) por essas fases — cada uma pede uma resposta interior diferente."
   },
   {
    "ic": "book",
    "t": "Porquê e Como (Nietzsche)",
    "b": "A bússola do livro: <em>'quem tem um porquê para viver suporta quase qualquer como'</em>. No campo, a resistência vinha menos da força física e mais de haver um sentido, uma meta, alguém esperando — um <strong>porquê</strong>.",
    "tip": "<strong>Modelo mental:</strong> antes de perguntar 'como aguentar?', encontre o 'por que / para que aguentar'."
   },
   {
    "ic": "person",
    "t": "Amor, Beleza e Humor",
    "b": "Privado do mundo exterior, o homem aprofunda a <strong>vida interior</strong>. A imagem do ser amado sustenta o prisioneiro: salva-se o homem pelo e no amor. A <strong>beleza</strong> (um pôr do sol) e o <strong>humor</strong> (rir do horror) provam a alma viva.",
    "tip": "<strong>Para refletir:</strong> ama-se a essência do outro, presente ou não — o amor dá sentido independentemente da posse."
   }
  ]
 },
 "ch02-a-ultima-liberdade-e-o-sofrimento": {
  "cards": [
   {
    "ic": "scale",
    "t": "A Inversão da Pergunta",
    "b": "Não cabe ao homem perguntar 'qual o sentido da vida?', mas <strong>responder à pergunta que a vida lhe faz</strong>. Somos os interrogados; respondemos agindo na tarefa concreta de cada momento — isso é <strong>responsabilidade</strong>.",
    "tip": "<strong>Como aplicar:</strong> reformule 'qual o sentido de tudo isto?' em 'o que esta situação, agora, me pede para fazer ou ser?'."
   },
   {
    "ic": "mountain",
    "t": "Sofrimento com Sentido",
    "b": "O sofrimento <strong>evitável</strong> deve ser evitado (sofrer por sofrer é masoquismo). Mas o sofrimento <strong>inevitável</strong> carrega um sentido potencial: a atitude digna diante dele transforma a tragédia em conquista interior.",
    "tip": "<strong>Regra:</strong> mude o que pode mudar; dê sentido ao que não pode."
   },
   {
    "ic": "pin",
    "t": "O Sentido é Único e Concreto",
    "b": "O sentido é <strong>descoberto, não inventado</strong> — detecta-se no mundo, fora de si. E é sempre <strong>concreto e único</strong>: muda de pessoa para pessoa e de hora para hora. Não há um 'sentido da vida' genérico.",
    "tip": "<strong>Para refletir:</strong> manter uma meta no futuro (uma tarefa, alguém) sustenta o homem no presente mais duro."
   }
  ]
 },
 "ch03-conceitos-da-logoterapia": {
  "cards": [
   {
    "ic": "constellation",
    "t": "As Três Escolas Vienenses",
    "b": "1ª <strong>Freud</strong> → vontade de prazer. 2ª <strong>Adler</strong> → vontade de poder. 3ª <strong>Frankl</strong> → <strong>vontade de sentido</strong>. A logoterapia cura pela busca de sentido, voltada ao futuro a realizar.",
    "tip": "<strong>Modelo mental:</strong> o homem é <em>autotranscendente</em> — realiza-se ao esquecer-se de si numa causa ou em alguém, não girando em torno do próprio eu."
   },
   {
    "ic": "gap",
    "t": "Vazio Existencial",
    "b": "A frustração da vontade de sentido produz o sentimento de <strong>vazio, tédio e ausência de propósito</strong> — fenômeno de massa do nosso tempo. Manifesta-se no <strong>conformismo</strong> (fazer o que os outros fazem) e no <strong>totalitarismo</strong> (fazer o que mandam).",
    "tip": "<strong>Como aplicar:</strong> leia o tédio crônico como sentido frustrado — pergunte o 'para quê', não só medique o humor."
   },
   {
    "ic": "spiral",
    "t": "Neurose Noogênica · Tensão Sadia",
    "b": "A <strong>neurose noogênica</strong> nasce de conflitos existenciais/espirituais (de <em>noös</em>), não de pulsões — pede logoterapia. E a saúde não é equilíbrio sem tensão: é a <strong>tensão sadia</strong> rumo a uma meta digna. Homeostase plena = vazio.",
    "tip": "<strong>Para refletir:</strong> não precisamos de uma vida sem exigências, mas do esforço por uma meta que valha a pena."
   }
  ]
 },
 "ch04-tecnicas-e-otimismo-tragico": {
  "cards": [
   {
    "ic": "pivot",
    "t": "Intenção Paradoxal",
    "b": "Contra o medo que se autorrealiza (fobia, insônia): o paciente é convidado a <strong>desejar, com humor e exagero, justamente o que teme</strong> ('vou tentar suar o máximo possível'). O <strong>autodistanciamento</strong> e o riso cortam a ansiedade antecipatória.",
    "tip": "<strong>Como aplicar:</strong> ninguém consegue <em>querer</em> de propósito o sintoma com a mesma força com que o teme — o círculo se rompe."
   },
   {
    "ic": "eye",
    "t": "Dereflexão",
    "b": "Contra a <strong>hiperreflexão</strong> (auto-observação que sabota o desempenho): <strong>desviar a atenção de si</strong> para um sentido, uma tarefa ou outra pessoa. O que foge quando perseguido — sono, prazer, felicidade — volta quando deixa de ser alvo.",
    "tip": "<strong>Regra:</strong> felicidade não se persegue, ela sobrevém — como efeito de um sentido realizado."
   },
   {
    "ic": "leaf",
    "t": "Otimismo Trágico",
    "b": "Dizer 'sim' à vida apesar da <strong>tríade trágica</strong> — dor, culpa e morte. Converter cada uma: <strong>dor</strong> em conquista; <strong>culpa</strong> em mudança para melhor; <strong>transitoriedade</strong> em responsabilidade de agir agora.",
    "tip": "<strong>Para refletir:</strong> é otimismo <em>apesar</em> da tragédia, não em negação dela."
   }
  ]
 }
}
```
