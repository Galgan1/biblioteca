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

# LIVRO PARA APROFUNDAR: Noites Brancas — Fiódor Dostoiévski

**Subtítulo:** VISÃO GERAL · UM MINUTO INTEIRO DE FELICIDADE
**Ideia central:** Em quatro noites brancas de Petersburgo, um jovem solitário — o Sonhador — encontra Nástienka, que espera por outro homem. Ele a ajuda a reencontrá-lo, perde-a — e abençoa o único minuto de felicidade que teve. Dostoiévski, 1848.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-noite-primeira-encontro` — NOITE PRIMEIRA: O Encontro
- `ch02-noite-segunda-o-sonhador` — NOITE SEGUNDA: A Confissão do Sonhador
- `ch03-noite-terceira-historia-nastienka` — NOITE TERCEIRA: A História de Nástienka
- `ch04-noite-quarta-virada` — NOITE QUARTA: A Virada
- `ch05-a-manha-generosidade` — A MANHÃ: Generosidade no Sofrimento
- `ch06-sonho-realidade-solidao` — CAPÍTULO 6: Sonho × Realidade e a Solidão
- `ch07-estrutura-simbolos-recursos` — CAPÍTULO 7: Estrutura, Símbolos e Recursos

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-noite-primeira-encontro": {
  "cards": [
   {
    "ic": "pin",
    "t": "O Cenário como Estado de Alma",
    "b": "A cidade vazia no verão espelha a solidão interior do Sonhador — ele <strong>dá adeus às casas como a amigos</strong>, prova de que sua vida acontece com coisas, não com pessoas. Petersburgo é personagem.",
    "tip": "<strong>Como ler:</strong> leia o cenário como estado psicológico, não como geografia — a Dostoiévski, o espaço é sempre alma."
   },
   {
    "ic": "clock",
    "t": "O Cronotopo da Noite Branca",
    "b": "O crepúsculo que não anoitece suspende o tempo: <strong>não é dia nem noite, é um entre-lugar onde o devaneio ganha consistência</strong>. O cenário é condição ativa da história, não pano de fundo.",
    "tip": "<strong>Modelo mental:</strong> a noite branca autoriza o irreal — é por isso que o encontro improvável acontece."
   },
   {
    "ic": "triangle",
    "t": "O Pacto como Ironia Trágica",
    "b": "Nástienka aceita conversar desde que ele <strong>não se apaixone</strong>. A regra é a ironia trágica que estrutura tudo — o leitor já sabe que será quebrada, e a queda está marcada desde a primeira noite.",
    "tip": "<strong>Sinal de alerta:</strong> ao prometer não amar, o Sonhador já está perdido."
   }
  ]
 },
 "ch02-noite-segunda-o-sonhador": {
  "cards": [
   {
    "ic": "spiral",
    "t": "O Tipo Literário do Sonhador",
    "b": "O <strong>sonhador (мечтатель)</strong> russo: jovem solitário, anos num quarto enfumaçado, amores e aventuras imaginadas — chegando aos trinta sem ter vivido. Dostoiévski examina o tipo com ternura e ironia ao mesmo tempo.",
    "tip": "<strong>Como ler:</strong> trate o devaneio como vício, não como hobby — o texto mostra o custo, não a poesia da fantasia."
   },
   {
    "ic": "gap",
    "t": "Fantasia: Droga e Prisão",
    "b": "A imaginação dá <strong>prazeres febris</strong> e arrebatadores — mas custa a vida real. 'Aniversários do devaneio' no lugar de memórias verdadeiras. A felicidade intensa do sonho é paga com o isolamento total.",
    "tip": "<strong>Modelo mental:</strong> cada ano de devaneio é mais um fio que prende o Sonhador ao subsolo."
   },
   {
    "ic": "bulb",
    "t": "O Embrião do Subsolo",
    "b": "Aqui está a <strong>semente do anti-herói de Memórias do Subsolo (1864)</strong> — mas o Sonhador ainda é dócil: entrega-se à ilusão em vez de se revoltar contra o mundo. A diferença é apenas de temperatura, não de natureza.",
    "tip": "<strong>Sinal de alerta:</strong> ao confessar-se a Nástienka, o Sonhador sai do devaneio — mas corre o risco de transformá-la em mais um sonho."
   }
  ]
 },
 "ch03-noite-terceira-historia-nastienka": {
  "cards": [
   {
    "ic": "link",
    "t": "Confissões em Espelho",
    "b": "À confissão do Sonhador (vida imaginada) responde a de Nástienka (vida real). <strong>Ambos estão presos, ambos esperam</strong> — ele por um amor projetado, ela por um amor concreto com nome e prazo.",
    "tip": "<strong>Como ler:</strong> fantasia (ele) × realidade (ela) — leia as duas confissões como variações do mesmo aprisionamento."
   },
   {
    "ic": "key",
    "t": "O Alfinete da Avó",
    "b": "A avó cega <strong>prendia o vestido de Nástienka ao seu com um alfinete</strong> para não a perder de vista. Imagem da clausura e da falta de liberdade — aprisionamento físico como metáfora da condição da moça.",
    "tip": "<strong>Modelo mental:</strong> o alfinete é o símbolo mais condensado da obra — uma vida inteira de vigilância reduzida a um objeto."
   },
   {
    "ic": "pivot",
    "t": "O Sonhador Cúmplice da Própria Dor",
    "b": "Nástienka pede que ele leve uma carta ao inquilino. O Sonhador se torna <strong>cúmplice da própria perda</strong> — ajuda a aproximar o rival, movido por generosidade e por amor.",
    "tip": "<strong>Sinal de alerta:</strong> a trama trágica se arma aqui: o amor não correspondido que ainda assim serve o rival."
   }
  ]
 },
 "ch04-noite-quarta-virada": {
  "cards": [
   {
    "ic": "mountain",
    "t": "A Peripécia Total",
    "b": "A maior subida (a declaração correspondida) seguida da maior queda (o retorno do rival) — tudo em poucas páginas. <strong>Ápice e ruína no mesmo minuto.</strong> A crueldade do desfecho está em ter chegado tão perto.",
    "tip": "<strong>Como ler:</strong> meça a queda pela altura — leia o pico como armadilha, não como promessa."
   },
   {
    "ic": "spark",
    "t": "O Instante de Felicidade",
    "b": "A felicidade não é negada de todo — ela acontece, mas dura um instante. O drama não é nunca ter; é <strong>ter por um minuto e perder</strong>. A efemeridade é o tema operante desta noite.",
    "tip": "<strong>Modelo mental:</strong> o minuto real vale mais que anos de devaneio — esse é o paradoxo central da novela."
   },
   {
    "ic": "eye",
    "t": "Não Traição, mas Verdade",
    "b": "Nástienka amou os dois por um momento. Ao correr para o inquilino, ela não engana: ela <strong>descobre, no instante do reencontro, qual era o amor verdadeiro</strong>. Realidade vence devaneio no mesmo segundo.",
    "tip": "<strong>Como ler:</strong> a corrida de Nástienka ao inquilino é reconhecimento, não traição."
   }
  ]
 },
 "ch05-a-manha-generosidade": {
  "cards": [
   {
    "ic": "leaf",
    "t": "Altruísmo Radical",
    "b": "Em vez de maldição, o Sonhador oferece uma bênção: <strong>deseja o bem de Nástienka acima da própria dor</strong>. A generosidade no sofrimento — amar querendo a felicidade do outro, sem posse — é o ápice ético da obra.",
    "tip": "<strong>Como ler:</strong> a renúncia é grandeza, não fraqueza — vitória moral dentro da derrota afetiva."
   },
   {
    "ic": "clock",
    "t": "A Frase-Síntese",
    "b": "\"Meu Deus! Um minuto inteiro de felicidade! Será pouco para a vida inteira de um homem?\" — a tese da obra. <strong>Pese sempre um minuto contra uma vida inteira</strong>: é a pergunta que fica depois de tudo acabar.",
    "tip": "<strong>Modelo mental:</strong> a bênção é sublime e patética ao mesmo tempo — pode ser nobreza da alma ou resignação de quem nunca soube viver."
   },
   {
    "ic": "spiral",
    "t": "Estrutura Circular",
    "b": "A novela começa e termina com o Sonhador <strong>só em seu quarto</strong>. O encontro foi um parêntese de felicidade entre duas solidões — mas o quarto do fim carrega algo que o do começo não tinha: um minuto real.",
    "tip": "<strong>Como ler:</strong> o círculo se fecha, mas o Sonhador volta transformado por uma experiência genuína."
   }
  ]
 },
 "ch06-sonho-realidade-solidao": {
  "cards": [
   {
    "ic": "gap",
    "t": "O Eixo Filosófico",
    "b": "Sonhador (fantasia) × Nástienka (realidade) é o eixo. <strong>O real cobra o preço que o sonho isenta</strong> — mas é justamente esse preço que prova que se viveu. O minuto de dor é a certidão de que, por uma vez, ele saiu do subsolo.",
    "tip": "<strong>Como ler:</strong> não moralize fácil — o texto não diz 'acorde e viva'; diz que viver dói, e ainda assim o minuto valeu."
   },
   {
    "ic": "person",
    "t": "Idealização Romântica",
    "b": "O Sonhador ama um ideal projetado de Nástienka tanto quanto a moça concreta. Dostoiévski usa as <strong>convenções do Romantismo e ao mesmo tempo as examina com distância crítica</strong> — bela e mutiladora.",
    "tip": "<strong>Modelo mental:</strong> a idealização é fonte de felicidade e de miséria — o mesmo movimento que consola adoece."
   },
   {
    "ic": "constellation",
    "t": "Solidão como Diagnóstico Social",
    "b": "A doença de fundo é a <strong>solidão urbana</strong>: estar só na multidão de Petersburgo é o que produz o sonhador. O devaneio é sintoma de um mal social, não só psicológico.",
    "tip": "<strong>Sinal de alerta:</strong> o Sonhador não escolheu a fantasia — foi empurrado a ela pela metrópole indiferente."
   }
  ]
 },
 "ch07-estrutura-simbolos-recursos": {
  "cards": [
   {
    "ic": "steps",
    "t": "Arquitetura 4 + 1",
    "b": "Quatro noites de intimidade crescente + uma manhã de desfecho. <strong>A passagem da noite (crepúsculo onírico) para o dia (luz crua) é a própria curva dramática</strong> — ascensão noturna, queda matinal.",
    "tip": "<strong>Como ler:</strong> leia a divisão por noites como termômetro emocional — cada noite eleva a intimidade; a manhã a desfaz."
   },
   {
    "ic": "layers",
    "t": "Símbolos por Oposição",
    "b": "<strong>Noite branca / manhã</strong> (devaneio / fim) · <strong>quarto encardido / cais</strong> (clausura / limiar) · <strong>alfinete da avó</strong> (aprisionamento) · <strong>Petersburgo vazia</strong> (solidão tornada cidade). A obra inteira trabalha por pares de oposição.",
    "tip": "<strong>Modelo mental:</strong> atenção aos pares simbólicos — todo símbolo tem seu par antitético."
   },
   {
    "ic": "book",
    "t": "'Romance Sentimental' — Sincero e Irônico",
    "b": "O subtítulo é <strong>sincero e irônico ao mesmo tempo</strong>: a obra usa as convenções do Romantismo (a confissão, o amor irrealizado) e as examina com distância crítica. Herança romântica sob lente realista.",
    "tip": "<strong>Como ler:</strong> a confissão é autêntica e literária — o Sonhador é eloquente demais para ser só um homem comum; é também uma construção estética."
   }
  ]
 }
}
```
