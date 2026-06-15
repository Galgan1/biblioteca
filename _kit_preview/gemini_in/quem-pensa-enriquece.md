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

# LIVRO PARA APROFUNDAR: Quem Pensa, Enriquece — Napoleon Hill

**Subtítulo:** VISÃO GERAL · 13 PRINCÍPIOS PARA TRANSMUTAR DESEJO EM RIQUEZA
**Ideia central:** Pensamentos são coisas. Quando carregados de propósito, desejo ardente e persistência, eles se transmutam em equivalentes financeiros. Napoleon Hill sintetizou 20 anos de estudo dos homens mais ricos da história em 13 princípios — e o mecanismo de todos é sempre o mesmo: emoção mais repetição.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-desejo` — CAPÍTULO 1: Desejo — o Ponto de Partida
- `ch02-fe-autossugestao` — CAPÍTULO 2–3: Fé e Autossugestão
- `ch03-imaginacao-planejamento` — CAPÍTULO 5–6: Imaginação e Planejamento
- `ch04-decisao-persistencia` — CAPÍTULO 7–8: Decisão e Persistência
- `ch05-mastermind` — CAPÍTULO 9: O Poder do Mastermind
- `ch06-subconsciente-cerebro` — CAPÍTULO 10–12: Transmutação, Subconsciente e Cérebro
- `ch07-medos-sexto-sentido` — CAPÍTULO 13: Os 6 Medos e o Sexto Sentido

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-desejo": {
  "cards": [
   {
    "ic": "spark",
    "t": "Os 6 Passos do Desejo",
    "b": "(1) Quantia exata · (2) O que dará em troca · (3) Data definida · (4) Plano + comece já · (5) Declaração escrita · <strong>(6) Leia em voz alta 2× ao dia, vendo e sentindo a posse.</strong>",
    "tip": "<strong>Como aplicar:</strong> o passo 6 é o que grava no subconsciente — nunca o pule."
   },
   {
    "ic": "mountain",
    "t": "Desejo Ardente vs. Desejo Morno",
    "b": "Só o desejo <strong>definido, obsessivo e respaldado por fé</strong> se realiza. \"Quero ficar rico\" (sem quantia, prazo ou plano) é desejo morno — nunca se transmuta.",
    "tip": "<strong>Modelo mental:</strong> pense no desejo como fogo, não como vela — morno se apaga; ardente molda a realidade."
   },
   {
    "ic": "target",
    "t": "Queimar as Pontes",
    "b": "Comprometer-se a ponto de não haver retirada — o estado mental do vencedor. Edwin Barnes chegou maltrapilho à fábrica de Edison sem rota de retorno, e tornou-se sócio.",
    "tip": "<strong>Como aplicar:</strong> elimine o \"Plano B emocional\" — manter rota de fuga enfraquece o desejo."
   }
  ]
 },
 "ch02-fe-autossugestao": {
  "cards": [
   {
    "ic": "eye",
    "t": "Fé Como Estado Induzido",
    "b": "Criada deliberadamente pela <strong>repetição emocional</strong> de uma crença até o subconsciente aceitá-la e agir sobre ela. O subconsciente é solo neutro — cultiva fé ou medo com a mesma lei.",
    "tip": "<strong>Como aplicar:</strong> visualize-se de posse do objetivo com emoção intensa; pensamento frio não atravessa."
   },
   {
    "ic": "bulb",
    "t": "Autossugestão Dirigida",
    "b": "Leia sua declaração de desejo em voz alta, veja e sinta o resultado já realizado, repita manhã e noite. <strong>Emoção + repetição = gravação</strong> no subconsciente — palavras frias não chegam.",
    "tip": "<strong>Regra:</strong> você é o porteiro — se não plantar o positivo, o ambiente planta o medo."
   },
   {
    "ic": "mask",
    "t": "A Fé que Cultiva Medo",
    "b": "Pensamentos de medo, repetidos, também viram \"fé\" — fé no fracasso. O subconsciente não distingue real de vividamente imaginado: <strong>plante a semente escolhida</strong>.",
    "tip": "<strong>Sinal de alerta:</strong> reze ou afirme \"encharcado de medo\" e o subconsciente executa exatamente o medo."
   }
  ]
 },
 "ch03-imaginacao-planejamento": {
  "cards": [
   {
    "ic": "layers",
    "t": "Imaginação Sintética vs. Criativa",
    "b": "<strong>Sintética</strong> = recombinar o existente (a mais usada — fortunas nascem de recombinações, não de invenções inéditas). <strong>Criativa</strong> = captar ideias novas por intuição, alimentada pelo desejo ardente.",
    "tip": "<strong>Modelo mental:</strong> a fórmula da Coca-Cola valeu milhões não pela substância, mas pela imaginação de como levá-la ao mundo."
   },
   {
    "ic": "pivot",
    "t": "Troque o Plano, Não a Meta",
    "b": "\"<strong>Fracasso temporário ≠ derrota permanente.</strong>\" Quando um plano falha, substitua-o — mas mantenha o objetivo fixo. Quem troca o objetivo a cada tropeço, deriva.",
    "tip": "<strong>Como aplicar:</strong> contabilize o fracasso como informação; refaça o plano com o aprendizado."
   },
   {
    "ic": "wrench",
    "t": "Liderança por Consentimento",
    "b": "A única liderança duradoura é a que os liderados aceitam de bom grado. <strong>As 11 qualidades</strong> incluem: fazer mais do que o pago (milha extra), assumir responsabilidade total, cooperação e decisão firme.",
    "tip": "<strong>Sinal de alerta:</strong> liderar pela força ou pelo título gera obediência sem lealdade — insustentável."
   }
  ]
 },
 "ch04-decisao-persistencia": {
  "cards": [
   {
    "ic": "sword",
    "t": "Decidir Rápido, Mudar Devagar",
    "b": "O hábito mental dos vencedores: chegar à <strong>própria decisão, anunciá-la depois</strong> de tomada, mudá-la só com nova informação relevante — nunca por pressão social.",
    "tip": "<strong>Como aplicar:</strong> guarde seus planos e desejos; conte-os pela ação, não pela boca — opinião alheia é matéria-prima da indecisão."
   },
   {
    "ic": "mountain",
    "t": "As 4 Bases da Persistência",
    "b": "(1) <strong>Propósito definido</strong> · (2) <strong>Desejo ardente</strong> · (3) <strong>Autoconfiança</strong> · (4) <strong>Planos definidos</strong>, ainda que imperfeitos. Falta persistência? Diagnóstico: qual das 4 bases está frágil?",
    "tip": "<strong>Modelo mental:</strong> persistência é músculo + hábito — dói no começo, vira automática com a repetição."
   },
   {
    "ic": "gap",
    "t": "A Um Passo do Ouro",
    "b": "R. U. Darby desistiu da mina a <strong>um metro</strong> da veia que renderia milhões. A maioria desiste justamente quando está a um passo do resultado — o último metro é o que paga.",
    "tip": "<strong>Sinal de alerta:</strong> \"fracasso temporário\" é teste, não veredito — o revés inicial é esperado."
   }
  ]
 },
 "ch05-mastermind": {
  "cards": [
   {
    "ic": "link",
    "t": "Mastermind — a Terceira Mente",
    "b": "Mentes harmonizadas formam uma <strong>\"terceira mente\"</strong> invisível. A condição inegociável: <strong>harmonia perfeita</strong> — atrito anula o efeito. \"Nenhuma grande fortuna foi construída por uma só pessoa.\"",
    "tip": "<strong>Como aplicar:</strong> escolha mentes complementares (não cópias suas); defina o objetivo comum; recompense cada membro."
   },
   {
    "ic": "person",
    "t": "As Duas Naturezas do Mastermind",
    "b": "(1) <strong>Econômica</strong> — contar com o conselho e a cooperação de outros. (2) <strong>Psíquica</strong> — a \"terceira mente\" que emerge da harmonia, gerando ideias além do individual.",
    "tip": "<strong>Modelo mental:</strong> o Mastermind é como baterias em série — cada mente soma voltagem; juntas, acendem o que nenhuma sozinha acenderia."
   },
   {
    "ic": "masks",
    "t": "Grupo sem Harmonia não é Mastermind",
    "b": "Inveja, atrito e agendas ocultas anulam o poder — vira só reunião. Reunir gente \"igual a você\" também falha: <strong>o Mastermind precisa de forças complementares</strong>.",
    "tip": "<strong>Sinal de alerta:</strong> se a reunião gera mais atrito que sinergia, reorganize antes de continuar."
   }
  ]
 },
 "ch06-subconsciente-cerebro": {
  "cards": [
   {
    "ic": "wave",
    "t": "Transmutação — Energia para Obra",
    "b": "Redirecionar o impulso sexual do físico para o <strong>criativo e produtivo</strong> multiplica imaginação, coragem e magnetismo. Reprimir destrói; transmutar potencializa. Os 10 estimulantes da mente (desejo, amor, música, Mastermind) elevam a imaginação criativa.",
    "tip": "<strong>Modelo mental:</strong> energia sexual é combustível de alta octanagem — queimado só no físico, move pouco; refinado, move um império."
   },
   {
    "ic": "leaf",
    "t": "O Subconsciente Sempre Ativo",
    "b": "Trabalha 24h; age sobre toda semente — positiva ou negativa. <strong>Plante as 7 emoções positivas</strong> (desejo, fé, amor, entusiasmo, romance, esperança, sexo) e barre as 7 negativas (medo, ciúme, ódio, raiva, ganância, superstição, vingança). Não coexistem.",
    "tip": "<strong>Como aplicar:</strong> antes de enviar qualquer pedido ao subconsciente, ocupe a mente com emoção positiva — expulse o medo primeiro."
   },
   {
    "ic": "constellation",
    "t": "O Cérebro como Rádio",
    "b": "Autossugestão = transmissor; imaginação criativa = receptor; subconsciente = antena. <strong>Mentes em harmonia (Mastermind) captam ideias além da soma individual</strong> — o mecanismo da \"terceira mente\".",
    "tip": "<strong>Modelo mental:</strong> emoção intensa = sintonizar o aparelho na frequência alta; apatia e medo = frequência baixa, sem captação."
   }
  ]
 },
 "ch07-medos-sexto-sentido": {
  "cards": [
   {
    "ic": "triangle",
    "t": "Os 6 Fantasmas do Medo",
    "b": "(1) <strong>Pobreza</strong> (o mais destrutivo) · (2) Crítica · (3) Doença · (4) Perda do amor · (5) Velhice · (6) Morte. São <strong>estados mentais aprendidos</strong> — logo, desaprendíveis por decisão e fé.",
    "tip": "<strong>Como aplicar:</strong> encha a mente de propósito definido e fé; medo é inquilino do vácuo — não deixe vácuo."
   },
   {
    "ic": "spiral",
    "t": "Indecisão → Dúvida → Medo",
    "b": "A trinca que se autoalimenta. Quebre no <strong>primeiro elo</strong>: decida cedo e firme. Conviver com pessimistas e absorver-lhes o medo (\"o 7º mal\") é a suscetibilidade a influências negativas.",
    "tip": "<strong>Sinal de alerta:</strong> se você se cerca de pessimistas, o medo deles vai plantar sugestões negativas no seu subconsciente."
   },
   {
    "ic": "constellation",
    "t": "O Gabinete Invisível de Conselheiros",
    "b": "O método de Hill: reuniões imaginárias com personagens admirados (Emerson, Lincoln, Edison), atribuindo a cada um uma virtude a adquirir. Com o tempo, o canal da <strong>imaginação criativa</strong> — o sexto sentido — se abre.",
    "tip": "<strong>Modelo mental:</strong> o sexto sentido é o mirante no topo da escada — só chega quem subiu os 12 degraus; não há elevador."
   }
  ]
 }
}
```
