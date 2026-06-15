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

# LIVRO PARA APROFUNDAR: Os Irmãos Karamázov — Fiódor Dostoiévski

**Subtítulo:** VISÃO GERAL · FÉ, DÚVIDA E A ALMA HUMANA REPARTIDA
**Ideia central:** Numa pequena cidade russa, três irmãos — paixão (Dmitri), razão (Ivan) e fé (Aliócha) — vivem o parricídio e o julgamento. O romance transforma o crime numa arena onde se debatem Deus, a liberdade, o sofrimento dos inocentes e a redenção pelo amor.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-os-tres-irmaos` — CAPÍTULO 1: Os Três Irmãos — A Alma Repartida
- `ch02-dmitri-mitia-paixao` — CAPÍTULO 2: Dmitri (Mítia) — A Paixão
- `ch03-ivan-intelecto-rebeliao` — CAPÍTULO 3: Ivan — Intelecto, Ateísmo e Rebelião
- `ch04-aliocha-fe-compaixao` — CAPÍTULO 4: Aliócha — Fé, Compaixão e Amor Ativo
- `ch05-smerdiakov-parricidio` — CAPÍTULO 5: Smerdiákov e o Parricídio
- `ch06-grande-inquisidor` — CAPÍTULO 6: A Lenda do Grande Inquisidor
- `ch07-zossima-amor-ativo` — CAPÍTULO 7: O Ancião Zóssima — O Amor Ativo
- `ch08-teodiceia-sofrimento` — CAPÍTULO 8: Teodiceia — O Sofrimento das Crianças
- `ch09-julgamento-redencao` — CAPÍTULO 9: O Julgamento e a Redenção
- `ch10-estrutura-simbolos` — CAPÍTULO 10: Estrutura, Símbolos e Polifonia

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-os-tres-irmaos": {
  "cards": [
   {
    "ic": "layers",
    "t": "Personagens-Tese",
    "b": "Cada irmão <strong>encarna uma posição filosófica</strong>: Dmitri (paixão e o Bem que luta com o Mal no coração do homem), Ivan (a razão que nega harmonia que custa sofrimento inocente), Aliócha (a fé encarnada no amor cotidiano). São teses em carne.",
    "tip": "<strong>Modelo mental:</strong> leia cada discurso como argumento filosófico — a polifonia significa que Dostoiévski dá seus melhores argumentos a todos os lados."
   },
   {
    "ic": "triangle",
    "t": "Smerdiákov — A Quarta Faceta",
    "b": "Filho bastardo e ignorado, Smerdiákov <strong>executa o que Ivan pensa</strong>: o niilismo prático que mata o pai sem remorso. É a prova de que ideias têm consequências — o intelectual que teoriza o 'tudo é permitido' é cúmplice do que o homem sem cultura faz com a teoria.",
    "tip": "<strong>Para o leitor:</strong> quando você sustentar uma ideia, pergunte: que Smerdiákov vai aplicá-la na prática?"
   },
   {
    "ic": "spiral",
    "t": "O 'Karamázovismo'",
    "b": "A família carrega uma força vital excessiva — sensualidade, paixão, sede de vida — que tanto produz grandeza quanto destruição. O <strong>karamázovismo</strong> é a intensidade sem moldura: o mesmo fogo que ilumina pode queimar.",
    "tip": "<strong>Como aplicar:</strong> intensidade sem forma e sem freio moral é a raiz do karamázovismo — identifique o padrão em si mesmo."
   }
  ]
 },
 "ch02-dmitri-mitia-paixao": {
  "cards": [
   {
    "ic": "sword",
    "t": "Madona × Sodoma",
    "b": "Dmitri formula o dilema interno: o homem é capaz de contemplar a Madona (o belo e o puro) e de se afogar em Sodoma (o sensual e o baixo) ao mesmo tempo, sem hipocrisia — porque <strong>ambos são reais nele</strong>.",
    "tip": "<strong>Modelo mental:</strong> a honestidade de Dmitri é admitir a contradição interna em vez de negar uma das faces."
   },
   {
    "ic": "scale",
    "t": "A Justiça que Erra",
    "b": "Dmitri é condenado por um crime que não cometeu — a justiça humana é <strong>cega</strong>: acerta a família certa, erra o culpado. Mas o romance recusa fazer disso um protesto simples: a condenação injusta vira ocasião de graça.",
    "tip": "<strong>Para o leitor:</strong> Dostoiévski não romantiza o erro judiciário — mostra como o sofrimento injusto pode ser aceito e transformado."
   },
   {
    "ic": "leaf",
    "t": "Redenção pelo Sofrimento Aceito",
    "b": "No sonho do 'pequenininho' (a criança que sofre no frio), Dmitri é convertido: a culpa coletiva o alcança, e ele <strong>aceita o sofrimento injusto</strong> como graça. A inocência provada seria alívio; a dor abraçada é redenção.",
    "tip": "<strong>Como aplicar:</strong> a diferença entre sofrimento que destrói e sofrimento que redime está na aceitação — receber em vez de resistir."
   }
  ]
 },
 "ch03-ivan-intelecto-rebeliao": {
  "cards": [
   {
    "ic": "bulb",
    "t": "'Devolver o Bilhete'",
    "b": "Ivan não é ateu simples: <strong>aceita que Deus exista</strong>, mas recusa respeitosamente entrar num mundo cujo preço é a lágrima de uma criança torturada. É protesto ético, não ceticismo frívolo. A honestidade do argumento força o leitor a enfrentá-lo.",
    "tip": "<strong>Para o leitor:</strong> não reduza Ivan a vilão — Dostoiévski lhe dá o melhor argumento possível porque quer testá-lo de verdade."
   },
   {
    "ic": "fork",
    "t": "Ideias têm Consequências",
    "b": "Ivan teoriza o 'tudo é permitido'; Smerdiákov <strong>mata o pai</strong>. A conexão não é acidental: Dostoiévski mostra que o intelectual que remove o fundamento moral é cúmplice das ações que a teoria autoriza, mesmo que não tenha 'pedido'.",
    "tip": "<strong>Modelo mental:</strong> pese as consequências de segunda ordem de qualquer sistema de ideias — quem vai aplicá-las sem os freios que o teórico ainda tem?"
   },
   {
    "ic": "spiral",
    "t": "Ivan e o Diabo",
    "b": "No clímax, Ivan dialoga com o Diabo — que é a <strong>sua própria dúvida personificada</strong>. O niilismo que ele sustentou racionalmente retorna como vozes, alucinações, loucura. A ideia vivida até as últimas consequências destrói quem a pensou.",
    "tip": "<strong>Como aplicar:</strong> o preço de sustentar um sistema que corta a raiz moral é pagos pelo próprio autor da ideia, não só por quem a executa."
   }
  ]
 },
 "ch04-aliocha-fe-compaixao": {
  "cards": [
   {
    "ic": "leaf",
    "t": "Fé Encarnada, Não Argumentada",
    "b": "Aliócha não debat com Ivan: ele <strong>beija</strong> (plágio do gesto de Cristo ao Inquisidor). A fé que Dostoiévski defende não é doutrina vencedora de silogismos — é amor que age, que escuta, que está presente.",
    "tip": "<strong>Modelo mental:</strong> à acusação racional mais poderosa, o romance responde com um gesto de amor — e isso é escolha artística deliberada de Dostoiévski."
   },
   {
    "ic": "person",
    "t": "O Discurso da Pedra",
    "b": "No final, Aliócha reúne as crianças em torno da pedra onde enterraram Iliúcha e fala do poder de uma boa lembrança de infância: ela <strong>ancora moralmente o homem adulto</strong>. O amor cultivado na criança é a semente da ética.",
    "tip": "<strong>Para o leitor:</strong> o Discurso da Pedra é o programa positivo do romance — a contrapartida ativa ao niilismo de Ivan."
   },
   {
    "ic": "bubble",
    "t": "Compaixão sem Julgamento",
    "b": "Aliócha é o único personagem que <strong>não julga</strong> — nem Dmitri (culpado em espírito), nem Ivan (o rebelde), nem Grushenka (a sedutora). Sua compaixão universal não é ingenuidade: é a pedagogia de Zóssima em prática.",
    "tip": "<strong>Como aplicar:</strong> a compaixão sem julgamento não significa ausência de discernimento — significa encontrar o humano antes de decretar o veredicto."
   }
  ]
 },
 "ch05-smerdiakov-parricidio": {
  "cards": [
   {
    "ic": "mask",
    "t": "Culpa Difusa",
    "b": "Smerdiákov executa a mão; mas <strong>Ivan fornece a ideia</strong>, Dmitri o ódio e a oportunidade. O romance recusa a pergunta simples 'quem matou?' — a culpa é compartilhada, simbólica, filosófica. O parricídio é de todos.",
    "tip": "<strong>Modelo mental:</strong> em sistemas complexos, a responsabilidade raramente é de um só agente — rastreie quem forneceu a ideia, o ódio e a oportunidade."
   },
   {
    "ic": "gap",
    "t": "O Executor sem Ideia Própria",
    "b": "Smerdiákov <strong>não tem teoria própria</strong>: usa a de Ivan sem os freios morais que o intelectual ainda mantém. É o niilismo em estado puro — sem angústia, sem remorso, com uma lógica assustadoramente limpa.",
    "tip": "<strong>Para o leitor:</strong> o perigo de uma ideia não está no teórico que a pensa com freios, mas no prático que a aplica sem eles."
   },
   {
    "ic": "sword",
    "t": "Parricídio como Símbolo",
    "b": "Matar o pai é também matar o <strong>Pai (Deus)</strong> e toda autoridade moral transcendente. O romance une o crime doméstico à questão filosófica: sem Deus-Pai como fundamento, o parricídio literal e o moral caminham juntos.",
    "tip": "<strong>Como aplicar:</strong> leia o parricídio em dois níveis — o crime doméstico e a revolta filosófica contra todo fundamento de autoridade."
   }
  ]
 },
 "ch06-grande-inquisidor": {
  "cards": [
   {
    "ic": "scale",
    "t": "Liberdade × Pão/Segurança",
    "b": "O Inquisidor propõe a troca que todo poder autoritário faz: <strong>segurança material e certeza</strong> em lugar da liberdade de consciência. 'Alimenta-os e exige-lhes a virtude': a massa prefere pão a escolha, milagre a fé.",
    "tip": "<strong>Como aplicar:</strong> use o Inquisidor como lente para qualquer poder que cuida das pessoas tirando-lhes a escolha — político, religioso, institucional, tecnológico."
   },
   {
    "ic": "triangle",
    "t": "As Três Tentações Invertidas",
    "b": "As tentações que Cristo recusou no deserto são, para o Inquisidor, as três forças que realmente governam os homens: <strong>pão</strong> (segurança material), <strong>milagre</strong> (a fé que exige prodígio) e <strong>mistério e autoridade</strong> (o poder que dispensa o homem de pensar).",
    "tip": "<strong>Modelo mental:</strong> toda ideologia que entrega pão + milagre + autoridade em troca de obediência repete o esquema do Inquisidor — independente do rótulo."
   },
   {
    "ic": "leaf",
    "t": "O Beijo — A Resposta sem Palavras",
    "b": "Cristo não responde ao discurso do Inquisidor: <strong>beija-o nos lábios</strong>. À dialética do poder, a resposta é o gesto de amor. Aliócha replica da mesma forma a Ivan — o romance ensina que há perguntas cuja resposta não é argumento.",
    "tip": "<strong>Para o leitor:</strong> o silêncio de Cristo é vitória ou rendição? Dostoiévski deixa a pergunta aberta de propósito — a ambiguidade é a tese."
   }
  ]
 },
 "ch07-zossima-amor-ativo": {
  "cards": [
   {
    "ic": "leaf",
    "t": "Amor Ativo × Amor em Sonho",
    "b": "O amor em sonho é espetacular, busca reconhecimento e colapsa diante da ingratidão. O <strong>amor ativo</strong> é concreto, silencioso, duro: serve sem plateia, suporta sem prêmio. Zóssima diz que o amor ativo é trabalho, e o resultado é certeza.",
    "tip": "<strong>Como aplicar:</strong> quando o amor exige reconhecimento para continuar, pergunte se é ativo ou em sonho."
   },
   {
    "ic": "link",
    "t": "Responsabilidade Universal",
    "b": "'<strong>Cada um é responsável por tudo perante todos</strong>': a culpa difusa do parricídio vira, no avesso, uma ética de comunhão. Não há crime 'alheio' — e nenhuma bondade é 'suficiente' enquanto houver sofrimento evitável.",
    "tip": "<strong>Modelo mental:</strong> responsabilidade universal não é culpa paralisante — é o chamado à participação ativa no bem do outro."
   },
   {
    "ic": "person",
    "t": "Não Julgar",
    "b": "O ensinamento central de Zóssima: <strong>não julgue</strong> — porque não conhece a luta interna do outro. Quem julga se fecha; quem acolhe, cura. O starets é a prova encarnada: sua influência cresce pelo amor, não pela autoridade.",
    "tip": "<strong>Para o leitor:</strong> Zóssima não é ingênuo — é perspicaz. Reservar o julgamento é estratégia de quem quer entender antes de decretar."
   }
  ]
 },
 "ch08-teodiceia-sofrimento": {
  "cards": [
   {
    "ic": "scale",
    "t": "A Teodiceia — O Nó Insolúvel",
    "b": "O sofrimento das crianças é o <strong>caso-limite</strong>: inocência absoluta torna toda justificativa teológica intolerável. Ivan não pede uma explicação melhor — recusa a explicação como categoria de resposta ao sofrimento inocente.",
    "tip": "<strong>Para o leitor:</strong> Dostoiévski admite em cartas que temia não conseguir responder a Ivan — a fé do livro é fé apesar da dúvida, não sem ela."
   },
   {
    "ic": "key",
    "t": "O Livre-Arbítrio como Preço do Amor",
    "b": "A resposta existencial do romance: sem liberdade não há mal, mas também não há amor verdadeiro. O <strong>livre-arbítrio é o preço</strong> de um mundo onde o amor seja real — não programado. Deus não é autor do sofrimento; é o que o permite para que o amor exista.",
    "tip": "<strong>Modelo mental:</strong> um mundo sem liberdade seria sem dor — e sem amor. A aposta de Dostoiévski é que o amor vale o risco."
   },
   {
    "ic": "bulb",
    "t": "A Réplica Existencial — Não Lógica",
    "b": "A resposta a Ivan não é um silogismo que vence o dele: é <strong>uma vida</strong> (Zóssima, Aliócha). A fé não explica o sofrimento — redime o sofredor em comunhão. 'Não há resposta para a pergunta de Ivan, só há uma vida que a torna suportável.'",
    "tip": "<strong>Como aplicar:</strong> diante do sofrimento alheio, respostas teóricas costumam magoar — a presença ativa (amor ativo) é o que o romance oferece como resposta."
   }
  ]
 },
 "ch09-julgamento-redencao": {
  "cards": [
   {
    "ic": "scale",
    "t": "A Justiça que Erra o Fato",
    "b": "O julgamento é um espetáculo de retórica que chega à conclusão <strong>errada</strong>: condena quem não matou. A crítica de Dostoiévski à justiça humana não é que ela seja má — é que ela é <strong>limitada</strong>: vê o externo, nunca a alma.",
    "tip": "<strong>Modelo mental:</strong> a justiça humana julga atos; o romance julga intenções e responsabilidades difusas — dimensões que o tribunal não alcança."
   },
   {
    "ic": "leaf",
    "t": "O Pequenino — A Conversão de Dmitri",
    "b": "No sonho do 'pequenininho' (a criança que chora no frio), Dmitri sente pela primeira vez uma <strong>responsabilidade que vai além do seu crime</strong>: a culpa coletiva, o sofrimento inocente, a dívida com todos. A criança que sofre converte onde o argumento falhou.",
    "tip": "<strong>Para o leitor:</strong> a conversão de Dmitri não é intelectual — é emocional e espiritual. Dostoiévski confia mais no coração partido do que na razão convencida."
   },
   {
    "ic": "mountain",
    "t": "A Sibéria como Graça",
    "b": "Dmitri planeja fugir, mas pondera aceitar o <strong>sofrimento injusto</strong> como expiação — não pelo crime que não cometeu, mas pela culpa de espírito que ele carrega. A Sibéria que condena o inocente pode ser a mesma que o redime.",
    "tip": "<strong>Como aplicar:</strong> a aceitação do sofrimento injusto não é resignação passiva — é transformação ativa do que foi imposto em caminho de crescimento."
   }
  ]
 },
 "ch10-estrutura-simbolos": {
  "cards": [
   {
    "ic": "spiral",
    "t": "O Romance Polifônico",
    "b": "Em Dostoiévski nenhuma voz é 'a do autor': cada personagem fala com <strong>autonomia e convicção plena</strong>. A verdade é disputada, não decretada. A 'resposta' do romance é a obra inteira — não um capítulo, não um discurso.",
    "tip": "<strong>Modelo mental:</strong> leia cada discurso como o melhor argumento daquele ponto de vista, não como o que Dostoiévski 'quer que você pense'."
   },
   {
    "ic": "eye",
    "t": "Os Símbolos em Pares",
    "b": "Os símbolos funcionam por <strong>oposição</strong>: beijar a terra (graça/redenção) × o pilão de ferro (violência); o beijo de Cristo × a acusação do Inquisidor; a criança que sofre ('o pequenininho') × a pedra do Discurso (lembrança que ancora). Leia sempre o par, nunca o polo isolado.",
    "tip": "<strong>Para o leitor:</strong> em Dostoiévski cada símbolo positivo tem um negativo correspondente — a tensão entre eles é o significado."
   },
   {
    "ic": "fork",
    "t": "Os Ensaios Encenados",
    "b": "A 'Lenda do Grande Inquisidor', o 'Discurso da Rebelião' de Ivan e os ensinamentos de Zóssima são <strong>ensaios filosóficos dentro do romance</strong>. Dostoiévski os encena como falas de personagens para que nenhum tenha a autoridade do autor — cada um é testado pela vida do personagem que o carrega.",
    "tip": "<strong>Como aplicar:</strong> identifique quando um discurso 'brilhante' é desmentido pela vida do personagem que o pronuncia — esse é o método de Dostoiévski."
   }
  ]
 }
}
```
