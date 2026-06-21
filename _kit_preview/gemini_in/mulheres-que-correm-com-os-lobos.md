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

# LIVRO PARA APROFUNDAR: Mulheres que Correm com os Lobos — Clarissa Pinkola Estés

**Subtítulo:** VISÃO GERAL · CONTOS, ARQUÉTIPOS E A PSIQUE SELVAGEM
**Ideia central:** Dentro de toda mulher vive a Mulher Selvagem — a natureza instintiva, criativa e sábia soterrada pela domesticação cultural. Clarissa Pinkola Estés lê contos de fada como mapas da alma feminina, mostrando como recuperar o instinto, a voz e a vitalidade que a vida amorteceu.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-la-loba-mulher-selvagem` — CAPÍTULO 1: La Loba e a Mulher Selvagem
- `ch02-barba-azul-predador-interno` — CAPÍTULO 2: Barba Azul e o Predador da Psique
- `ch03-vasalisa-intuicao` — CAPÍTULO 3: Vasalisa e a Recuperação da Intuição
- `ch04-mulher-esqueleto-vida-morte-vida` — CAPÍTULO 4: A Mulher Esqueleto — Vida-Morte-Vida no Amor
- `ch05-patinho-feio-exilio-pertencimento` — CAPÍTULO 5: O Patinho Feio — Exílio e Pertencimento
- `ch06-sapatinhos-vermelhos-vicio` — CAPÍTULO 6: Os Sapatinhos Vermelhos — A Alma Capturada
- `ch07-manawee-cortejo-alma-dupla` — CAPÍTULO 7: Manawee e o Cortejo da Alma Dupla
- `ch08-donzela-manca-descida-renovacao` — CAPÍTULO 8: A Donzela Manca — Descida e Renovação
- `ch09-lar-subterraneo-voz-propria` — CAPÍTULO 9: O Lar Subterrâneo e a Voz Própria

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-la-loba-mulher-selvagem": {
  "cards": [
   {
    "ic": "spark",
    "t": "Juntar os Ossos",
    "b": "Reunir o que foi disperso: as partes <strong>indestrutíveis de si</strong> que a vida amorteceu. O canto sobre os ossos (a criatividade, a voz) é o que as reanima. La Loba é a guardiã que sabe que nada de essencial se perde.",
    "tip": "<strong>Como aplicar:</strong> quando se sentir fragmentada, pergunte — o que em mim é indestrutível e só precisa ser reunido?"
   },
   {
    "ic": "leaf",
    "t": "O Selvagem como Natural",
    "b": "Selvagem significa <strong>natural e não domado</strong>, não descontrolado. A Mulher Selvagem é o instinto que discerne, não que se descontrola. Domesticação é o processo que ensina a abafar esse instinto em troca de aceitação.",
    "tip": "<strong>Sinal de alerta:</strong> confundir instinto com impulsividade. O instinto saudável discerne — ele não se lança às cegas."
   },
   {
    "ic": "wave",
    "t": "O Rio Sob o Rio",
    "b": "<em>Río abajo río</em>: há sempre uma <strong>corrente instintiva subterrânea</strong> correndo sob a vida cotidiana. Quando a superfície seca, a corrente funda ainda corre. Ouvir os sonhos, o corpo e as atrações/repulsas é afinar o ouvido para ela.",
    "tip": "<strong>Modelo mental:</strong> aridez e cansaço são sinais de que você perdeu contato com a corrente subterrânea — não de que ela sumiu."
   }
  ]
 },
 "ch02-barba-azul-predador-interno": {
  "cards": [
   {
    "ic": "eye",
    "t": "O Predador se Revela pelo que Proíbe",
    "b": "O perigo interno se disfarça de encanto e se denuncia pelo que <strong>proíbe você de ver</strong>. A chave proibida (a curiosidade) é função de sobrevivência da alma, não um pecado. Abrir a porta revela a verdade.",
    "tip": "<strong>Como aplicar:</strong> diante de algo brilhante demais, pergunte — o que há atrás da porta que me pedem para não abrir?"
   },
   {
    "ic": "spark",
    "t": "A Chave que Sangra",
    "b": "Uma vez que você <strong>viu a verdade, não há como desfazê-la</strong>. O saber é irreversível — a chave manda sangue de um lado quando some do outro. Tentar 'limpar a chave' (negar o que foi visto) é a armadilha.",
    "tip": "<strong>Sinal de alerta:</strong> racionalizar sinais de alarme ('ele não quis dizer isso', 'estou exagerando') é tentar lavar a chave."
   },
   {
    "ic": "person",
    "t": "Nomear e Mobilizar",
    "b": "Ver a verdade não basta: é preciso <strong>nomear o predador</strong> e mobilizar os 'irmãos' (forças ativas, aliados, limites firmes). A paralisia diante do predador é ceder o jogo.",
    "tip": "<strong>Como aplicar:</strong> depois de ver, nomeie e aja — não negocie de volta para a cegueira."
   }
  ]
 },
 "ch03-vasalisa-intuicao": {
  "cards": [
   {
    "ic": "bulb",
    "t": "A Boneca que Sabe",
    "b": "A intuição é o <strong>saber do corpo antes da mente</strong>. 'Pergunte à boneca' e sinta a resposta no corpo (alívio vs. aperto) antes de racionalizar. Alimente-a: silêncio, sono, atenção. Intuição faminta emudece.",
    "tip": "<strong>Como aplicar:</strong> diante de uma decisão, faça a pergunta e sinta a resposta no corpo antes de pensar."
   },
   {
    "ic": "mountain",
    "t": "A Baba Yagá como Iniciadora",
    "b": "A bruxa feroz não destrói gratuitamente: ela <strong>inicia</strong>. Situações aterrorizantes que testam (as tarefas impossíveis) são provas que separam o que importa do que não importa — e entregam a luz ao final.",
    "tip": "<strong>Modelo mental:</strong> aceite ir à cabana da Baba Yagá — fuja e você fica no escuro; cumpra as tarefas e conquista a luz própria."
   },
   {
    "ic": "key",
    "t": "O Fogo que Queima o que Sabota",
    "b": "A luz conquistada (o crânio com olhos de fogo) <strong>incinera o que diminui e sabota</strong>. Recuperar o fogo interno não é agressão: é discernimento que queima naturalmente o que não pertence ao seu círculo.",
    "tip": "<strong>Sinal de alerta:</strong> pedir fogo emprestado para sempre (depender da luz dos outros) é recusar a própria iniciação."
   }
  ]
 },
 "ch04-mulher-esqueleto-vida-morte-vida": {
  "cards": [
   {
    "ic": "spiral",
    "t": "Desembaraçar os Ossos",
    "b": "O trabalho paciente de <strong>organizar o medo e enfrentar o que assusta no amor</strong>. Quem foge remando da Mulher Esqueleto ela acompanha enredada — só quem para e desembaraça os ossos um a um liberta o ciclo.",
    "tip": "<strong>Como aplicar:</strong> quando uma fase do vínculo 'morre', desembarace um medo por vez — em vez de remar para longe."
   },
   {
    "ic": "wave",
    "t": "A Lágrima que Alimenta",
    "b": "A vulnerabilidade autêntica — <strong>deixar-se sentir</strong> — é o que alimenta e revive a relação. A lágrima do pescador é o que dá de beber à Mulher Esqueleto e a faz cantar carne de volta ao corpo.",
    "tip": "<strong>Modelo mental:</strong> a vulnerabilidade verdadeira não é fraqueza — é o alimento do amor."
   },
   {
    "ic": "masks",
    "t": "A Dama Morte como Parceira",
    "b": "A Dama Morte/Vida não veio destruir o amor: veio <strong>iniciá-lo nos ciclos</strong>. Querer só a 'vida' (prazer, novidade) e recusar a 'morte' (perdas, transformação) esteriliza a relação.",
    "tip": "<strong>Sinal de alerta:</strong> recomeços eternos (fugir toda vez que a 'morte' aparece) condenam a não aprofundar nenhum vínculo."
   }
  ]
 },
 "ch05-patinho-feio-exilio-pertencimento": {
  "cards": [
   {
    "ic": "gap",
    "t": "O Ninho Errado",
    "b": "Sentir-se cronicamente 'errada' costuma ser sinal de <strong>ninho errado, não de defeito</strong>. O talento e a sensibilidade incomuns que o grupo de origem trata como falha são, para a própria espécie, o traço de reconhecimento.",
    "tip": "<strong>Como aplicar:</strong> antes de concluir que há algo errado com você, considere a hipótese do ninho errado."
   },
   {
    "ic": "person",
    "t": "O Exílio como Bússola",
    "b": "O exílio não é sentença: é uma bússola que aponta para a <strong>própria espécie</strong>. 'Sobreviver ao inverno' (a resistência tenaz no período mais duro) é parte obrigatória da travessia, não fracasso.",
    "tip": "<strong>Modelo mental:</strong> o exílio empurra — não se instale permanentemente no congelamento."
   },
   {
    "ic": "eye",
    "t": "O Reflexo que Reconhece",
    "b": "Pertencimento verdadeiro é onde você se vê <strong>sem precisar se deformar</strong>. Os cisnes acolhem não porque o patinho mudou — mas porque o espelho finalmente mostra o que ele sempre foi.",
    "tip": "<strong>Como aplicar:</strong> procure ativamente os cisnes — ambientes e pessoas em cujo reflexo você se reconhece."
   }
  ]
 },
 "ch06-sapatinhos-vermelhos-vicio": {
  "cards": [
   {
    "ic": "spark",
    "t": "Os Sapatinhos Artesanais",
    "b": "A vida criativa genuína — ainda que pobre, ainda que simples — é o <strong>valor selvagem original</strong>. Quando ele é roubado ou negociado por 'vida decente e estéril', abre-se um vazio que nenhum substituto consegue preencher.",
    "tip": "<strong>Modelo mental:</strong> pergunte — que sapatinhos artesanais foram queimados? Qual vida autêntica o substituto está tampando?"
   },
   {
    "ic": "mask",
    "t": "A Dança que Não Para",
    "b": "Os sapatos enfeitiçados prometem preencher o vazio mas <strong>escravizam</strong>: a compulsão começa como alívio e vira cárcere. O encanto barato cobra a liberdade como preço.",
    "tip": "<strong>Sinal de alerta:</strong> desconfie do que brilha na vitrine e promete ser exatamente o que faltava — ele pode colar aos pés."
   },
   {
    "ic": "leaf",
    "t": "Curar a Fonte, Não o Sintoma",
    "b": "Combater só o comportamento compulsivo sem restaurar a <strong>alegria selvagem original</strong> é tratar o sintoma e deixar a causa. Reacender a vida criativa real esvazia o poder do substituto melhor que a força de vontade.",
    "tip": "<strong>Como aplicar:</strong> identifique e reacenda o que foi roubado; a compulsão perde potência quando a fonte é restaurada."
   }
  ]
 },
 "ch07-manawee-cortejo-alma-dupla": {
  "cards": [
   {
    "ic": "link",
    "t": "Os Dois Nomes Secretos",
    "b": "Toda pessoa tem uma dimensão visível e uma <strong>secreta/selvagem</strong>; amar é conhecer e honrar ambas. Honrar só a metade conveniente e ignorar a outra é amar pela metade.",
    "tip": "<strong>Como aplicar:</strong> para conhecer alguém a fundo, descubra os dois nomes — a face social e a natureza selvagem."
   },
   {
    "ic": "target",
    "t": "As Iscas do Caminho",
    "b": "O instinto <strong>sabe os nomes</strong>, mas perde-os cada vez que para para uma isca (preguiça, gratificação imediata, distração brilhante). A constância é o que entrega o resultado — não a esperteza.",
    "tip": "<strong>Sinal de alerta:</strong> quando o instinto 'perder o nome' no caminho, volte e refaça o trajeto em vez de desistir."
   },
   {
    "ic": "person",
    "t": "Persistência Humilde",
    "b": "Conquista-se a alma dupla pela <strong>constância repetida e tenaz</strong>, não por uma investida de força. Amar como prática — ir, perder, voltar — é o padrão de quem por fim entrega os dois nomes intactos.",
    "tip": "<strong>Modelo mental:</strong> recuse as iscas durante a missão — fidelidade ao objetivo supera gratificação imediata."
   }
  ]
 },
 "ch08-donzela-manca-descida-renovacao": {
  "cards": [
   {
    "ic": "mountain",
    "t": "A Descida como Caminho",
    "b": "Perda de identidade, escuridão e errância são <strong>parte da individuação</strong>, não desvios. A nekyia (descida ao inconsciente) é necessária — forçar uma saída rápida aborta a transformação que está incubando no escuro.",
    "tip": "<strong>Modelo mental:</strong> quando 'as mãos forem cortadas', reconheça que entrou numa fase de descida — deixe a floresta fazer seu trabalho."
   },
   {
    "ic": "clock",
    "t": "Tempos Estéreis como Incubação",
    "b": "A transformação acontece <strong>fora de vista</strong>. Períodos longos e aparentemente improdutivos são incubação da alma, não fracasso. As mãos crescem no escuro, no tempo próprio, não no cronograma da urgência.",
    "tip": "<strong>Como aplicar:</strong> trate o período estéril como gestação — não force a saída antes de as mãos renascerem."
   },
   {
    "ic": "leaf",
    "t": "As Mãos que Renascem",
    "b": "A capacidade renovada <strong>nasce da travessia e da própria ação</strong> — não de um resgate externo. A renovação é orgânica e conquistada: mais madura e autêntica do que a inocência inicial que foi perdida.",
    "tip": "<strong>Sinal de alerta:</strong> esperar ser resgatada de fora prolonga a estéril permanência na floresta."
   }
  ]
 },
 "ch09-lar-subterraneo-voz-propria": {
  "cards": [
   {
    "ic": "wave",
    "t": "Vestir a Pele Antes de Secar",
    "b": "Os sinais de 'pele seca' (exaustão, perda de brilho, irritação, vazio) avisam que faz tempo que você não mergulha no lar interior. O retorno ao si é <strong>manutenção preventiva</strong>, não luxo nem emergência.",
    "tip": "<strong>Como aplicar:</strong> programe regressos regulares à solidão fértil antes de ressecar — não espere o colapso para buscar o mar."
   },
   {
    "ic": "spiral",
    "t": "O Ciclo Saudável",
    "b": "Mergulhar para se reabastecer e <strong>voltar renovada</strong> — ir e retornar. O objetivo não é escapar do mundo, mas sustentar a vida nele. Usar o 'lar subterrâneo' como desculpa para nunca retornar é confundir cura com fuga.",
    "tip": "<strong>Modelo mental:</strong> o ciclo saudável é ida e volta — recarregar para sustentar, não desaparecer."
   },
   {
    "ic": "spark",
    "t": "A Voz Própria como Respiração",
    "b": "Criar, nomear, falar a verdade no próprio tom é a <strong>respiração da alma selvagem</strong>. O silenciamento — por medo, vergonha ou domesticação — a asfixia. Não espere permissão: criar é respirar.",
    "tip": "<strong>Como aplicar:</strong> quando se sentir morta por dentro, pergunte — onde minha voz foi silenciada? Devolva-a a um campo de cada vez."
   }
  ]
 }
}
```
