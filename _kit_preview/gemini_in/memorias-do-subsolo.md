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

# LIVRO PARA APROFUNDAR: Memórias do Subsolo — Fiódor Dostoiévski

**Subtítulo:** VISÃO GERAL · A LIBERDADE COMO DOENÇA E COMO DIGNIDADE
**Ideia central:** Um funcionário aposentado, amargo e hiperconsciente, escreve do seu 'subsolo'. Na Parte 1 ataca o racionalismo e defende o livre-arbítrio (o '2+2=5'); na Parte 2 prova, em episódios humilhantes, ser incapaz de agir e de amar. A obra que abriu o caminho para o existencialismo.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-o-homem-do-subsolo` — CAPÍTULO 1: O Homem do Subsolo — O Anti-Herói
- `ch02-hiperconsciencia-paralisia` — CAPÍTULO 2: A Hiperconsciência que Paralisa
- `ch03-palacio-de-cristal-2x2` — CAPÍTULO 3: O Palácio de Cristal e o 2+2=4
- `ch04-livre-arbitrio-capricho` — CAPÍTULO 4: O Livre-Arbítrio e o Capricho
- `ch05-parte-2-jantar-humilhacao` — CAPÍTULO 5 (Parte 2): O Jantar e a Humilhação
- `ch06-liza-incapacidade-de-amar` — CAPÍTULO 6: Liza — A Redenção Oferecida e Negada
- `ch07-narrador-estrutura-duas-partes` — CAPÍTULO 7: O Narrador e a Estrutura em Duas Partes
- `ch08-legado-existencialismo-simbolos` — CAPÍTULO 8: Legado, Existencialismo e Símbolos

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-o-homem-do-subsolo": {
  "cards": [
   {
    "ic": "gap",
    "t": "O Subsolo como Estado da Alma",
    "b": "O subsolo (подполье) é o <strong>isolamento da consciência hipertrofiada</strong>: o narrador se retira dos homens, os observa com desprezo e ainda assim os precisa para existir. Sem plateia, o monólogo não faz sentido — ele escreve para 'os senhores' imaginários.",
    "tip": "<strong>Para o leitor:</strong> o subsolo não é orgulho saudável nem introversão produtiva — é o isolamento que se alimenta do que odeia."
   },
   {
    "ic": "mask",
    "t": "O Anti-Herói sem Ação",
    "b": "O herói clássico age; o anti-herói é <strong>definido pela impotência</strong>. O narrador do subsolo não executa nada de significativo — sua 'grandeza' é o ressentimento elaborado e o projeto de ações que nunca realiza. Dostoiévski cunha o anti-herói moderno pela primeira vez na literatura.",
    "tip": "<strong>Modelo mental:</strong> o ressentimento é a rebeldia do impotente — a elaboração de por que o mundo está errado e de por que eu não o mudo."
   },
   {
    "ic": "spiral",
    "t": "Prazer no Sofrimento",
    "b": "O narrador tira um prazer <strong>doentio da própria humilhação</strong>: a dor o faz sentir-se vivo e moralmente superior ('ao menos eu sofro conscientemente'). É a inversão perversa do masoquismo — não sexualizado, mas filosófico: sofrer com consciência é preferível a viver na estupidez feliz.",
    "tip": "<strong>Como aplicar:</strong> identifique quando o 'sofrimento consciente' serve para evitar a mudança real — 'sofrer bem' pode ser fuga do crescimento."
   }
  ]
 },
 "ch02-hiperconsciencia-paralisia": {
  "cards": [
   {
    "ic": "spiral",
    "t": "Consciência como Doença",
    "b": "A <strong>hiperconsciência</strong> que o narrador possui não é virtude: cada impulso analisado até a raiz perde a força de se realizar. O homem que 'pensa demais' não age — e Dostoiévski mostra que isso não é sabedoria, é paralisia.",
    "tip": "<strong>Modelo mental:</strong> existe um ponto em que a autoanálise impede a ação — a consciência que tudo dissolve não produz nem bondade nem mudança."
   },
   {
    "ic": "mountain",
    "t": "O Homem 'Espontâneo' × O Hiperconsciente",
    "b": "O narrador inveja e despreza o homem 'de ação direta' — aquele que age sem examinar demais. O espontâneo é chamado de burro, mas <strong>ele ao menos vive</strong>. O hiperconsciente é mais inteligente e mais morto — a inteligência que paralisa é pior que a 'burrice' que age.",
    "tip": "<strong>Para o leitor:</strong> Dostoiévski não romantiza nem um nem outro — mas o subsolo mostra que a inteligência que não se converte em ação vira tormento."
   },
   {
    "ic": "eye",
    "t": "O Prazer Invertido da Dor",
    "b": "O narrador encontra satisfação peculiar em <strong>analisar sua própria humilhação</strong>: 'Sofrer é vantagem!' A dor consciente lhe parece superior à satisfação inconsciente — e isso o aprisiona no ciclo: a dor é confortável demais para ser abandonada.",
    "tip": "<strong>Como aplicar:</strong> quando o sofrimento passa a ter função de identidade ('sou o que sofre conscientemente'), ele resiste à cura."
   }
  ]
 },
 "ch03-palacio-de-cristal-2x2": {
  "cards": [
   {
    "ic": "triangle",
    "t": "O Palácio de Cristal — Prisão Dourada",
    "b": "A utopia racional é atacada como <strong>aniquilação da liberdade</strong>: num mundo onde tudo está resolvido e calculado, não há o que contestar nem escolher. A perfeição racional é descrita como morte da liberdade — a prisão mais elegante possível.",
    "tip": "<strong>Modelo mental:</strong> questione qualquer sistema que prometa eliminar toda incerteza — a segurança absoluta tem sempre um preço que envolve liberdade."
   },
   {
    "ic": "spark",
    "t": "2+2=5 — Manifesto do Livre-Arbítrio",
    "b": "O narrador não defende que '2+2=5' seja verdade matemática: defende o <strong>direito de discordar da verdade imposta</strong>. Contra o determinismo que trata o homem como 'tecla de piano', o capricho livre — mesmo contra o próprio interesse — é o que prova a humanidade.",
    "tip": "<strong>Para o leitor:</strong> '2+2=5' é a raiz filosófica do existencialismo — a liberdade antes da essência, a vontade antes da razão."
   },
   {
    "ic": "sword",
    "t": "O Muro de Pedra",
    "b": "As leis da natureza são o '<strong>muro de pedra</strong>' que o racionalista aceita com reverência e o subsolo recusa aceitar — não porque possa derrubá-lo, mas porque a recusa é o único gesto de liberdade disponível. Bater a cabeça no muro é humano; reverenciá-lo como destino é abdicação.",
    "tip": "<strong>Como aplicar:</strong> diferencie limites reais (que se respeitam) de limites arbitrários impostos por sistemas — a distinção exige discernimento, não rebeldia indiscriminada."
   }
  ]
 },
 "ch04-livre-arbitrio-capricho": {
  "cards": [
   {
    "ic": "key",
    "t": "A Vontade — Acima do Interesse",
    "b": "O subsolo inverte a premissa utilitarista: o <strong>bem supremo não é a felicidade</strong>, é a liberdade de querer. Qualquer sistema que garanta o bem-estar suprimindo a escolha suprime o que faz o homem humano — o capricho indócil, a vontade que não se deixa prever.",
    "tip": "<strong>Modelo mental:</strong> a raiz do existencialismo está aqui — a liberdade antes da essência, a vontade antes do interesse calculado."
   },
   {
    "ic": "person",
    "t": "A Tecla de Piano — Contra o Determinismo",
    "b": "O racionalismo trata o homem como '<strong>tecla de piano</strong>': dadas as condições, a nota é prevista. O subsolo recusa: age de propósito <strong>contra o próprio interesse</strong> para provar que é livre, não determinado. Mesmo que essa prova custe sofrimento.",
    "tip": "<strong>Para o leitor:</strong> Dostoiévski não romantiza a autossabotagem — ele a diagnostica como prova desesperada de liberdade num mundo que nega a agência."
   },
   {
    "ic": "fork",
    "t": "Agir Contra Si — O Paradoxo",
    "b": "O narrador afirma: prefiro agir contra o meu bem apenas para provar que posso. É o paradoxo da liberdade: <strong>a autossabotagem como afirmação de humanidade</strong>. Dostoiévski viu isso como raiz de muito sofrimento moderno — a liberdade exercida contra si mesmo por falta de outro campo.",
    "tip": "<strong>Como aplicar:</strong> quando agir contra o próprio interesse é padrão, pergunte se é exercício de liberdade ou aprisionamento disfarçado de rebeldia."
   }
  ]
 },
 "ch05-parte-2-jantar-humilhacao": {
  "cards": [
   {
    "ic": "wave",
    "t": "A Teoria Vira Biografia",
    "b": "A estrutura da obra é argumento: a Parte 1 (monólogo filosófico) é testada pela Parte 2 (biografia). O narrador que teorizou a liberdade e o capricho <strong>fracassa em praticá-los</strong>: não age — reage, e mal. A ideia não se sustenta quando encarnada.",
    "tip": "<strong>Modelo mental:</strong> qualquer sistema filosófico deve ser medido pelas consequências quando vivido — não pelo que parece coerente em teoria."
   },
   {
    "ic": "mask",
    "t": "Zvérkov — A Inveja que se Disfarça de Desprezo",
    "b": "O narrador diz desprezar Zvérkov — belo, rico, popular — mas o motor real é a <strong>inveja</strong>. O desprezo é a defesa do ressentido que não admite querer o que o outro tem. Dostoiévski expõe o mecanismo com precisão clínica: desprezo por fora, inveja por dentro.",
    "tip": "<strong>Para o leitor:</strong> o ressentimento (inveja disfarçada de superioridade moral) é uma das psicologias mais precisamente descritas em toda a literatura."
   },
   {
    "ic": "gap",
    "t": "Buscar a Humilhação",
    "b": "O narrador <strong>procura</strong> a humilhação: persegue o grupo ao bordel após o jantar, exige reconhecimento de quem não o quer dar. A dor da humilhação é preferível ao vazio da ausência — ao menos no humilhamento ele existe para os olhos dos outros.",
    "tip": "<strong>Como aplicar:</strong> quando alguém parece 'atrair' o sofrimento social, pergunte se a presença dolorosa não é preferível à invisibilidade — o padrão tem lógica interna."
   }
  ]
 },
 "ch06-liza-incapacidade-de-amar": {
  "cards": [
   {
    "ic": "mask",
    "t": "O Discurso-Arma",
    "b": "O narrador usa <strong>palavras verdadeiras como arma</strong>: o discurso sobre a degradação de Liza é sincero em conteúdo, mas motivado pelo despeito e pelo desejo de dominar. É possível dizer a verdade por razões completamente erradas — e ainda ferir com ela.",
    "tip": "<strong>Modelo mental:</strong> a sinceridade do conteúdo não garante a bondade da intenção — as 'palavras verdadeiras' podem ser usadas para dominar."
   },
   {
    "ic": "gap",
    "t": "Incapacidade de Amar — A Defesa",
    "b": "Quando Liza aparece com compaixão real, o narrador <strong>a ataca</strong>: confessa que falou por despeito, humilha-a, paga-a como prostituta. O afeto o desarma — ele não suporta ser amado, porque amar exige igualdade que o subsolo nunca pode aceitar.",
    "tip": "<strong>Para o leitor:</strong> a crueldade aqui não é maldade gratuita — é a defesa desesperada de quem não tolera a exposição que o amor exige."
   },
   {
    "ic": "leaf",
    "t": "Liza — A Superior Moral",
    "b": "Liza percebe a infelicidade do narrador e <strong>o abraça com pena</strong>. Ao partir, deixa o dinheiro sobre a mesa sem palavra. A 'caída' é a superior moral: sua compaixão real mede a falência total dele. A inversão do clichê romântico (o herói salva a prostituta) é a tese de Dostoiévski.",
    "tip": "<strong>Como aplicar:</strong> frequentemente quem está em posição de 'precisar de ajuda' tem mais clareza moral do que quem se propõe a 'ajudar' — o poder corrompe a percepção."
   }
  ]
 },
 "ch07-narrador-estrutura-duas-partes": {
  "cards": [
   {
    "ic": "eye",
    "t": "Narrador Não Confiável — O Pioneiro",
    "b": "O narrador se contradiz, muda de posição, mente e logo revela a mentira. É um dos primeiros <strong>narradores não confiáveis</strong> sistemáticos da literatura moderna. A instabilidade não é erro do texto — é o retrato de uma mente que não consegue ser coerente consigo mesma.",
    "tip": "<strong>Modelo mental:</strong> em narradores não confiáveis, as contradições são os dados mais importantes — revele o que o narrador está tentando esconder."
   },
   {
    "ic": "layers",
    "t": "A Estrutura em Duas Partes",
    "b": "Parte 1 (monólogo filosófico do narrador velho) → Parte 2 (narrativa da juventude): a <strong>teoria se testa na vida</strong>. Lidas em paralelo, mostram que o filósofo do livre-arbítrio é prisioneiro do padrão que denuncia. A forma é o argumento mais eficaz da obra.",
    "tip": "<strong>Para o leitor:</strong> leia as duas partes em diálogo — cada afirmação da Parte 1 tem seu contra-exemplo na Parte 2."
   },
   {
    "ic": "gap",
    "t": "A Antinarrativa — Sem Redenção",
    "b": "A obra termina sem resolução: o narrador <strong>interrompe o relato</strong>, cercado pela moldura irônica do autor. Não há redenção, não há aprendizado, não há progressão — a antinarrativa é intencional: o subsolo não cresce, fecha-se sobre si mesmo.",
    "tip": "<strong>Como aplicar:</strong> a ausência de arco redentor é uma escolha estética que comunica: o subsolo é uma condição que se perpetua, não um problema a ser resolvido por narrativa."
   }
  ]
 },
 "ch08-legado-existencialismo-simbolos": {
  "cards": [
   {
    "ic": "spark",
    "t": "Raiz do Existencialismo",
    "b": "A liberdade antes da essência, a angústia da consciência, a vontade que precede a razão — tudo que Sartre e Camus desenvolverão está prefigurado aqui. Dostoiévski cunha o <strong>existencialismo literário</strong> antes de ele ter nome filosófico.",
    "tip": "<strong>Modelo mental:</strong> Memórias do Subsolo é o texto que conecta o realismo russo ao existencialismo europeu — leia-o como ponte, não como ilha."
   },
   {
    "ic": "link",
    "t": "Ponte na Obra de Dostoiévski",
    "b": "O homem do subsolo <strong>prefigura</strong> Raskólnikov (a teoria que se destrói na vida), Ivan Karamázov (o racionalismo que enlouquece) e o Grande Inquisidor (a liberdade como fardo insuportável). A novela é o laboratório onde os personagens maiores são esboçados.",
    "tip": "<strong>Para o leitor:</strong> releia Memórias do Subsolo após Crime e Castigo e Os Irmãos Karamázov — as conexões retroativas multiplicam o sentido."
   },
   {
    "ic": "eye",
    "t": "Os Símbolos — O Mapa",
    "b": "<strong>Subsolo</strong> (consciência hipertrofiada isolada) · <strong>Palácio de cristal</strong> (utopia racional = prisão) · <strong>Muro de pedra</strong> (necessidade que a liberdade recusa) · <strong>Tecla de piano</strong> (o homem determinado) · <strong>2×2=5</strong> (capricho = dignidade) · <strong>Neve molhada</strong> (Petersburgo degradada).",
    "tip": "<strong>Como aplicar:</strong> cada símbolo é argumento condensado — em vez de ler a novela como história, leia-a como filosofia em forma de imagem."
   }
  ]
 }
}
```
