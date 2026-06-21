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

# LIVRO PARA APROFUNDAR: A Hora da Estrela — Clarice Lispector

**Subtítulo:** VISÃO GERAL · A MORTE COMO ÚNICO PROTAGONISMO
**Ideia central:** Um narrador inventado tenta contar a vida de Macabéa — datilógrafa nordestina pobre, quase sem desejo, invisível para o mundo. O <em>como</em> se narra é o tema. Ela só vira 'estrela' no instante da morte. Último livro de Clarice Lispector, 1977.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-rodrigo-metalinguagem` — CAPÍTULO 1: Rodrigo S.M. e a Metalinguagem
- `ch02-macabea-invisivel` — CAPÍTULO 2: Macabéa, a Anti-Heroína Invisível
- `ch03-pobreza-alteridade` — CAPÍTULO 3: Pobreza, Alteridade e Invisibilidade Social
- `ch04-linguagem-silencio-instante` — CAPÍTULO 4: Linguagem, Silêncio e o Instante
- `ch05-olimpico-gloria-desejo` — CAPÍTULO 5: Olímpico, Glória e o Desejo
- `ch06-madame-carlota-epifania` — CAPÍTULO 6: Madame Carlota e a Falsa Epifania
- `ch07-hora-da-estrela-morte` — CAPÍTULO 7: A Hora da Estrela — a Morte como Ápice
- `ch08-estrutura-simbolos-recursos` — CAPÍTULO 8: Estrutura, Símbolos e Recursos

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-rodrigo-metalinguagem": {
  "cards": [
   {
    "ic": "bubble",
    "t": "O Narrador como Tema",
    "b": "Rodrigo hesita, recua, confessa que inventa e se acusa: \"preciso falar desta nordestina senão me asfixio\". A <strong>demora é estrutural</strong>, não falha — é a forma de aproximar-se de quem quase não tem matéria narrável.",
    "tip": "<strong>Como aplicar:</strong> leia cada interrupção do narrador como dado sobre a impossibilidade de representar o outro."
   },
   {
    "ic": "mask",
    "t": "A Máscara Autoral",
    "b": "Clarice escolhe um narrador masculino para <strong>dramatizar a distância</strong> entre quem escreve e quem é escrito — classe, gênero, experiência. A máscara é o argumento da obra.",
    "tip": "<strong>Modelo mental:</strong> mise en abyme — o livro contém a reflexão sobre o livro que está sendo escrito."
   },
   {
    "ic": "triangle",
    "t": "Narrador Não Confiável",
    "b": "Rodrigo contradiz-se, duvida, declara que vai escrever \"uma história simples\" e que a história \"ainda não começou\". <strong>Não há versão final dos fatos</strong> — há versões possíveis de um narrador confesso.",
    "tip": "<strong>Sinal de alerta:</strong> escrever sobre o miserável é também apropriar-se dele — e o texto sabe disso."
   }
  ]
 },
 "ch02-macabea-invisivel": {
  "cards": [
   {
    "ic": "person",
    "t": "Caracterização por Privação",
    "b": "Macabéa é definida pelo que lhe <strong>falta</strong>, não pelo que tem. \"Ela não sabia que existia, assim como um cachorro não sabe que é cachorro.\" A ausência é o método de construção.",
    "tip": "<strong>Como ler:</strong> não procure profundidade psicológica convencional — a ausência dela é a denúncia."
   },
   {
    "ic": "leaf",
    "t": "Alegrias Miúdas",
    "b": "Um cafezinho, ouvir a Rádio Relógio, um gole de Coca-Cola substituem qualquer enredo de ação. A <strong>banalidade como matéria literária</strong> é o gesto político da obra.",
    "tip": "<strong>Modelo mental:</strong> a 'felicidade' de Macabéa obriga o leitor a confrontar a própria condescendência."
   },
   {
    "ic": "gap",
    "t": "Feliz à Sua Maneira",
    "b": "A pobreza extrema rouba até a capacidade de querer e de se saber — mas Macabéa encontra prazer secreto em coisas mínimas. Isso é <strong>alívio ou a forma mais cruel da alienação?</strong>",
    "tip": "<strong>Sinal de alerta:</strong> a pena fácil é parte do problema que a obra quer desmontar."
   }
  ]
 },
 "ch03-pobreza-alteridade": {
  "cards": [
   {
    "ic": "mountain",
    "t": "O Abismo de Classe",
    "b": "O narrador é culto, urbano, masculino; Macabéa é ignorante, faminta, feminina. O <strong>abismo entre eles é o abismo da sociedade brasileira</strong> — e a obra recusa resolvê-lo.",
    "tip": "<strong>Como ler:</strong> a miséria aqui é existencial, não só econômica — rouba até a capacidade de querer."
   },
   {
    "ic": "constellation",
    "t": "O Narrador Denuncia e Reproduz",
    "b": "Rodrigo fala <em>por</em> Macabéa, sem ela. Clarice — elite intelectual — escreve sobre a pobre que jamais leria o livro. <strong>A contradição é consciente e é parte do argumento.</strong>",
    "tip": "<strong>Modelo mental:</strong> desconfie da própria pena — o texto provoca compaixão e denuncia o conforto de quem se compadece de longe."
   },
   {
    "ic": "link",
    "t": "Migração e Hierarquia",
    "b": "Macabéa e Olímpico migram do Nordeste para o Rio indiferente. <strong>Entre pobres também há hierarquia</strong> — Olímpico despreza Macabéa; Glória, ao roubá-lo, tem mais fartura.",
    "tip": "<strong>Invisibilidade social é uma forma de morte em vida</strong> — e a compaixão fácil é parte do problema."
   }
  ]
 },
 "ch04-linguagem-silencio-instante": {
  "cards": [
   {
    "ic": "wave",
    "t": "Afasia e Excesso",
    "b": "Macabéa colhe palavras do rádio sem entendê-las — linguagem chega a ela como ruído mágico. Rodrigo tem palavras demais e ainda sente que <strong>cada palavra trai a coisa</strong>.",
    "tip": "<strong>Como ler:</strong> o silêncio de Macabéa é mais eloquente que suas falas — leia o que não é dito."
   },
   {
    "ic": "spark",
    "t": "O Instante-Já",
    "b": "Clarice persegue o <strong>presente nu antes do sentido</strong> — o ser que precede a nomeação. A epifania em sua obra raramente consola; ela revela e fere ao mesmo tempo.",
    "tip": "<strong>Modelo mental:</strong> a palavra como fracasso produtivo — Clarice escreve sabendo que a linguagem não basta."
   },
   {
    "ic": "eye",
    "t": "Sintaxe Expressiva",
    "b": "Frases truncadas, pontuação irregular, o \"...sim\" inicial — <strong>a forma da frase é significado</strong>. A música do texto imita a respiração e a hesitação do narrador.",
    "tip": "<strong>Como ler:</strong> leia a pontuação estranha como dado de sentido, não como erro tipográfico."
   }
  ]
 },
 "ch05-olimpico-gloria-desejo": {
  "cards": [
   {
    "ic": "sword",
    "t": "Nomes Irônicos",
    "b": "<strong>Olímpico, Glória, 'de Jesus', Madame Carlota</strong> — grandeza nos nomes, miséria nas vidas. A ironia onomástica é uma das marcas mais visíveis da obra: expectativa nominal × realidade.",
    "tip": "<strong>Como ler:</strong> ao encontrar um nome grandioso, espere o contraste com o que a personagem de fato é."
   },
   {
    "ic": "pivot",
    "t": "O Desejo como Predação",
    "b": "Olímpico quer \"ser deputado\" e \"ficar rico\". Trata Macabéa com impaciência e a troca por Glória, que tem mais <strong>carne e fartura</strong>. Entre pobres, o desejo é instrumental, não romântico.",
    "tip": "<strong>Modelo mental:</strong> Macabéa só quer existir; Olímpico e Glória querem ascender."
   },
   {
    "ic": "triangle",
    "t": "Glória Aciona o Desfecho",
    "b": "Ao 'roubar' Olímpico, Glória sente culpa e empurra Macabéa para a cartomante. <strong>A vilã é quem aciona o mecanismo trágico</strong> — a peripécia vem daí.",
    "tip": "<strong>Sinal de alerta:</strong> o ato de piedade de Glória é a sentença de morte de Macabéa."
   }
  ]
 },
 "ch06-madame-carlota-epifania": {
  "cards": [
   {
    "ic": "bulb",
    "t": "A Esperança como Armadilha",
    "b": "Madame Carlota anuncia riqueza e um noivo estrangeiro loiro. <strong>A única vez que Macabéa deseja o futuro é a véspera de morrer</strong> — a obra desconfia radicalmente de qualquer promessa de redenção.",
    "tip": "<strong>Modelo mental:</strong> leia a peripécia trágica clássica dentro de uma anti-tragédia."
   },
   {
    "ic": "eye",
    "t": "Ironia Trágica",
    "b": "O leitor pressente que a promessa é falsa; Macabéa, não. A informação assimétrica cria uma <strong>tensão insuportável</strong> — sabemos o destino enquanto ela sorri.",
    "tip": "<strong>Como ler:</strong> 'falsa epifania' — a revelação prometida que não se cumpre, ou se cumpre às avessas."
   },
   {
    "ic": "mask",
    "t": "Madame Carlota: Charlatã ou Destino?",
    "b": "Ex-prostituta, devota de Jesus, generosa e grotesca. A obra mantém o <strong>duplo sentido</strong>: instrumento do destino ou ilusionista? A promessa de 'virar gente' é cruel — e é a única ternura que Macabéa recebe.",
    "tip": "<strong>Sinal de alerta:</strong> a 'boa nova' é sentença de morte."
   }
  ]
 },
 "ch07-hora-da-estrela-morte": {
  "cards": [
   {
    "ic": "star",
    "t": "Morte como Protagonismo",
    "b": "Só ao morrer Macabéa se torna o centro — <strong>'a hora da estrela' é o instante em que cada um, como ator, tem sua cena final</strong>. A vida inteira foi uma preparação para esse único momento de presença.",
    "tip": "<strong>Modelo mental:</strong> a morte não é punição; é a coroação paradoxal de quem nunca pôde existir plenamente."
   },
   {
    "ic": "spark",
    "t": "Existência × Essência",
    "b": "Macabéa, que 'não sabia que existia', só É plenamente ao deixar de ser. <strong>O instante final é o único em que existir e ser coincidem</strong> — a obra resolve na morte o que a vida não deu.",
    "tip": "<strong>Como ler:</strong> 'a hora da estrela' = o instante-já supremo de Clarice — a morte como única epifania real."
   },
   {
    "ic": "triangle",
    "t": "O Narrador Morre com Ela",
    "b": "Rodrigo encerra dizendo que também ele vai morrer — e que 'é morango', numa nota de estranha leveza. <strong>A obra se fecha sobre si mesma</strong>: o narrador criado para contar Macabéa desaparece com ela.",
    "tip": "<strong>Ironia do destino:</strong> o estrangeiro loiro e rico chega — como assassino ao volante, não como noivo."
   }
  ]
 },
 "ch08-estrutura-simbolos-recursos": {
  "cards": [
   {
    "ic": "book",
    "t": "O Paratexto é Obra",
    "b": "Dedicatória '(na verdade Clarice Lispector)', <strong>treze títulos alternativos</strong>, o '...sim' inicial — tudo integra o texto. Não pule: eles dão a chave antes de a leitura começar.",
    "tip": "<strong>Como ler:</strong> a lista de títulos (incl. 'A Culpa É Minha', 'Ela Que Se Arranje') já é o argumento da obra."
   },
   {
    "ic": "constellation",
    "t": "Símbolos do Brilho Letal",
    "b": "<strong>Estrela</strong> (protagonismo/morte) · <strong>Mercedes amarelo</strong> (riqueza letal) · <strong>loiro/ouro</strong> (promessa falsa) · <strong>Rádio Relógio</strong> (mundo como ruído) · <strong>capim</strong> (vida humilde). O brilho é sempre ligado à morte.",
    "tip": "<strong>Modelo mental:</strong> quando algo reluz na obra, antecipe a catástrofe — nunca a salvação."
   },
   {
    "ic": "layers",
    "t": "Os Três ao Mesmo Tempo",
    "b": "Romance social + metaficção + poema filosófico. A obra recusa pertencer a um único gênero: <strong>é os três ao mesmo tempo</strong>, e isso é parte do argumento sobre a impossibilidade de reduzir Macabéa a uma só moldura.",
    "tip": "<strong>Cuidado:</strong> forçar A Hora da Estrela num único gênero trai a obra."
   }
  ]
 }
}
```
