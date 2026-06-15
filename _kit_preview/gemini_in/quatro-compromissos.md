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

# LIVRO PARA APROFUNDAR: Os Quatro Compromissos — Don Miguel Ruiz

**Subtítulo:** VISÃO GERAL · UM GUIA PRÁTICO PARA A LIBERDADE PESSOAL
**Ideia central:** Da sabedoria tolteca, quatro acordos para reescrever os acordos que você nunca escolheu. Don Miguel Ruiz parte de uma ideia desconcertante: tudo o que você chama de 'eu' foi instalado de fora para dentro — a domesticação. Um Juiz interno condena, uma Vítima sofre, e um Livro da Lei herdado governa o seu sonho. Os quatro acordos são as novas regras que substituem o medo pelo amor e devolvem a liberdade pessoal.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-domesticacao-sonho` — CAPÍTULO 1: A Domesticação e o Sonho do Planeta
- `ch02-impecavel-palavra` — CAPÍTULO 2: Acordo 1 — Seja Impecável com a Palavra
- `ch03-lado-pessoal` — CAPÍTULO 3: Acordo 2 — Não Leve Nada para o Lado Pessoal
- `ch04-conclusoes-precipitadas` — CAPÍTULO 4: Acordo 3 — Não Tire Conclusões Precipitadas
- `ch05-melhor-que-puder` — CAPÍTULO 5: Acordo 4 — Sempre Faça o Melhor que Puder
- `ch06-quebrar-acordos` — CAPÍTULO 6: A Quebra de Acordos Antigos — A Arte da Transformação
- `ch07-liberdade-novo-sonho` — CAPÍTULO 7: O Novo Sonho — A Liberdade Pessoal
- `ch08-quinto-acordo` — CAPÍTULO 8: O Quinto Acordo (obra posterior)

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-domesticacao-sonho": {
  "cards": [
   {
    "ic": "book",
    "t": "O Sonho do Planeta",
    "b": "A realidade humana é um <strong>sonho coletivo</strong> — leis, valores, papéis sociais — que cada cultura sonha junto e transmite. Não é 'o mundo'; é uma interpretação acordada do mundo.",
    "tip": "<strong>Como aplicar:</strong> diante de uma regra social, pergunte 'isto é a realidade ou só o sonho que me ensinaram?'."
   },
   {
    "ic": "layers",
    "t": "A Domesticação do Humano",
    "b": "Como se domestica um animal — com <strong>recompensa e castigo</strong> — somos treinados a adotar o sistema de crenças da família e da sociedade. A criança aceita por medo de não ser amada; depois passa a se autodomesticar.",
    "tip": "<strong>Sinal de alerta:</strong> a pior domesticação é a autodomesticação — você se pune sozinho, mil vezes, pelo mesmo erro."
   },
   {
    "ic": "scale",
    "t": "O Juiz, a Vítima e o Livro da Lei",
    "b": "O <strong>Livro da Lei</strong> guarda todos os acordos herdados; o <strong>Juiz</strong> condena o que desvia; a <strong>Vítima</strong> carrega a culpa e o castigo. É a máquina interna do sofrimento.",
    "tip": "<strong>Modelo mental:</strong> sua mente vira um país com leis que você nunca votou — Juiz é o tribunal, Vítima é o réu, Livro da Lei é a constituição herdada."
   },
   {
    "ic": "eye",
    "t": "Acordo: a Unidade da Vida",
    "b": "Cada crença que você aceitou como verdade é um <strong>acordo</strong>. A vida é a soma dos acordos que faz consigo, com os outros e com a sociedade — e quase nenhum foi examinado.",
    "tip": "<strong>Primeiro filtro:</strong> 'isto é meu acordo ou um acordo herdado?'."
   }
  ]
 },
 "ch02-impecavel-palavra": {
  "cards": [
   {
    "ic": "spark",
    "t": "A Palavra como Magia",
    "b": "A palavra é <strong>força criadora pura</strong> — semente plantada na mente, sua e dos outros. Cada palavra é um feitiço que produz efeito real no sonho.",
    "tip": "<strong>Como aplicar:</strong> antes de falar (e de pensar), pergunte 'esta palavra cria ou destrói?'."
   },
   {
    "ic": "key",
    "t": "Impecabilidade (sem pecado contra si)",
    "b": "'Impecável' vem de <em>sine peccato</em> — <strong>sem pecado</strong>. Pecado, aqui, é tudo que você faz contra si mesmo. Fale com integridade, diga só o que pensa, não use a palavra contra você nem contra ninguém.",
    "tip": "<strong>Regra:</strong> o autoabuso verbal ('sou um fracasso') é o feitiço mais comum — e o mais devastador."
   },
   {
    "ic": "wave",
    "t": "A Fofoca como Veneno",
    "b": "A fofoca é <strong>magia negra</strong>: propaga opinião carregada de medo e ressentimento que infecta quem fala, quem ouve e o alvo. É o vírus mais contagioso da mente humana.",
    "tip": "<strong>Sinal de alerta:</strong> 'só estou comentando' costuma ser veneno emocional disfarçado."
   },
   {
    "ic": "leaf",
    "t": "A Palavra é uma Semente",
    "b": "Uma única frase — 'você é burro', dita a uma criança — pode <strong>germinar e governar uma vida inteira</strong>. Troque o veneno pela semente útil: 'errei e vou corrigir', não 'sou um idiota'.",
    "tip": "<strong>Modelo mental:</strong> o que você semeia na mente vai crescer; plante o que quer colher."
   }
  ]
 },
 "ch03-lado-pessoal": {
  "cards": [
   {
    "ic": "lens",
    "t": "Tudo é Projeção do Outro",
    "b": "O que as pessoas dizem e fazem é <strong>projeção da realidade delas</strong> — do acordo delas com a vida. Mesmo um insulto fala da pessoa que insulta, não de você.",
    "tip": "<strong>Como aplicar:</strong> ao se sentir ofendido, pergunte 'isto é sobre mim ou sobre o sonho dele?'."
   },
   {
    "ic": "mask",
    "t": "Importância Pessoal = Egoísmo",
    "b": "Levar tudo para o lado pessoal é a <strong>expressão máxima do egoísmo</strong>: parte do pressuposto de que 'tudo gira em torno de mim'. Quebrar essa centralidade dissolve a ofensa.",
    "tip": "<strong>Modelo mental:</strong> as opiniões alheias são cartas endereçadas a outra pessoa — chegaram à sua caixa por engano."
   },
   {
    "ic": "scale",
    "t": "Imunidade nos Dois Sentidos",
    "b": "A imunidade vale também para o elogio: <strong>se o elogio te ergue, a crítica te derruba</strong>. 'Você pode me xingar e eu não me sinto pior; pode me elogiar e eu não me sinto melhor' — porque sei o que sou.",
    "tip": "<strong>Regra:</strong> não se vicie em aprovação, ou ficará refém da reprovação."
   },
   {
    "ic": "leaf",
    "t": "Não Coma o Veneno",
    "b": "Quando você 'engole' o que dizem, ingere o <strong>veneno emocional</strong> do outro. Não levar a sério é não comer o veneno — escudo, não muro: mantenha o coração aberto sem absorvê-lo.",
    "tip": "<strong>Atalho:</strong> a imunidade nasce de confiar no que você é, não da opinião externa."
   }
  ]
 },
 "ch04-conclusoes-precipitadas": {
  "cards": [
   {
    "ic": "gap",
    "t": "A Suposição como Veneno",
    "b": "Presumimos o que os outros pensam e sentem, <strong>acreditamos na suposição como se fosse fato</strong> e reagimos a ela — gerando drama a partir de algo que nunca foi verdade.",
    "tip": "<strong>Como aplicar:</strong> sentiu certeza sobre a intenção de alguém? Marque 'isto é fato ou suposição?'."
   },
   {
    "ic": "bubble",
    "t": "A Coragem de Perguntar",
    "b": "O remédio é <strong>fazer perguntas claras e pedir o que se quer</strong>, em vez de adivinhar. Perguntar exige coragem porque expõe a vulnerabilidade — mas elimina o drama na raiz.",
    "tip": "<strong>Regra:</strong> o custo de perguntar é quase sempre menor que o do drama fabricado."
   },
   {
    "ic": "bulb",
    "t": "Ninguém Lê Mente",
    "b": "Supomos que o outro 'deveria saber' o que queremos sem dizermos — e nos magoamos quando ele não adivinha. A mente abomina o vácuo e o <strong>preenche com a pior versão</strong>.",
    "tip": "<strong>Sinal de alerta:</strong> 'ele deveria saber sem eu falar' é expectativa de leitura mental."
   },
   {
    "ic": "link",
    "t": "A Pergunta Dissolve o Drama",
    "b": "Um amigo não responde por horas; a mente inventa 'ele está bravo comigo'. À noite descobre: o celular estava sem bateria. <strong>O sofrimento foi 100% fabricado</strong> — uma pergunta o teria desfeito em dez segundos.",
    "tip": "<strong>Como aplicar:</strong> transforme a suposição em pergunta direta e dê à mente o fato real."
   }
  ]
 },
 "ch05-melhor-que-puder": {
  "cards": [
   {
    "ic": "clock",
    "t": "O Melhor é Variável",
    "b": "Seu 'melhor' não é fixo — varia com saúde, energia, humor, contexto. O melhor de quando você está doente é menor que o de quando está bem; <strong>ambos são, igualmente, o seu melhor</strong>.",
    "tip": "<strong>Como aplicar:</strong> em vez de comparar com um ideal, pergunte 'fiz o melhor que eu podia agora?'."
   },
   {
    "ic": "target",
    "t": "Sem Autojulgamento nem Arrependimento",
    "b": "Quando você sempre faz o seu melhor, <strong>não há base para o Juiz condenar</strong> nem para a Vítima sofrer — não se pode arrepender do que era o seu máximo possível.",
    "tip": "<strong>Sinal de alerta:</strong> 'eu poderia ter feito mais' depois de já ter dado o máximo é autojulgamento sem base."
   },
   {
    "ic": "spark",
    "t": "Faça pela Ação, não pela Recompensa",
    "b": "Fazer o melhor <strong>porque você ama fazer</strong> — não para ser aceito ou premiado — transforma o trabalho de obrigação em expressão de vida. Se você ama o que faz, o fazer já paga.",
    "tip": "<strong>Regra:</strong> a aprovação externa vira bônus, não combustível."
   },
   {
    "ic": "steps",
    "t": "Nem Mais, Nem Menos",
    "b": "Fazer 'mais que o seu melhor' (perfeccionismo) <strong>esgota</strong>; fazer 'menos' <strong>gera culpa</strong>. O ponto é o seu melhor real — num dia ótimo, uma hora flui; num dia difícil, cinco minutos já são o seu melhor.",
    "tip": "<strong>Modelo mental:</strong> pense no 'melhor' como termômetro, não como meta fixa — ele sobe e desce."
   }
  ]
 },
 "ch06-quebrar-acordos": {
  "cards": [
   {
    "ic": "mountain",
    "t": "As Três Maestrias Toltecas",
    "b": "O caminho em três estágios:",
    "tip": "<strong>Como aplicar:</strong> é um mapa de processo — ver, transformar e, então, amar."
   },
   {
    "ic": "sword",
    "t": "O Guerreiro contra o Parasita",
    "b": "O <strong>parasita</strong> (Juiz + Vítima + Livro da Lei) se alimenta do seu veneno emocional. O guerreiro declara guerra a ele com disciplina, pela 'arte do esquecimento' — desinstalar o sonho de medo.",
    "tip": "<strong>Regra:</strong> repetição vence repetição — o acordo antigo foi gravado repetindo; só some repetindo o novo."
   },
   {
    "ic": "pivot",
    "t": "A Iniciação dos Mortos",
    "b": "Viver como se cada momento pudesse ser o último: a <strong>consciência da morte</strong> queima o trivial e revela o essencial. Diante do anjo da morte, fofoca e suposição ficam absurdas.",
    "tip": "<strong>Modelo mental:</strong> use a morte como editora da vida — ela mostra o que realmente importa."
   },
   {
    "ic": "link",
    "t": "Substituir, não só Remover",
    "b": "Cada acordo antigo quebrado precisa ser <strong>trocado por um novo</strong> (os quatro acordos). Removê-lo sem instalar outro deixa o vácuo — e o parasita o reenche de medo.",
    "tip": "<strong>Cuidado:</strong> entender os acordos sem praticá-los não quebra a domesticação."
   }
  ]
 },
 "ch07-liberdade-novo-sonho": {
  "cards": [
   {
    "ic": "leaf",
    "t": "A Liberdade Pessoal",
    "b": "O estado de quem não é mais governado pelo Juiz, pela Vítima nem pelos acordos de medo — <strong>vive segundo a própria verdade</strong>, e não a imagem que tenta projetar.",
    "tip": "<strong>Bússola:</strong> 'esta escolha vem do medo (agradar, defender a imagem) ou do amor (ser quem sou)?'."
   },
   {
    "ic": "spark",
    "t": "Recuperar a Espontaneidade",
    "b": "A criança pequena é livre, espontânea e viva no presente. A liberdade é <strong>voltar a esse estado</strong> — com a sabedoria do adulto. É subtração, não acréscimo: remover os acordos que escondem quem você já é.",
    "tip": "<strong>Modelo mental:</strong> você não precisa adquirir nada novo; precisa desfazer o que foi posto por cima."
   },
   {
    "ic": "constellation",
    "t": "Céu ou Inferno: os Dois Sonhos",
    "b": "Você sempre vive num sonho — o <strong>medo faz dele inferno</strong> (drama, julgamento, controle); o <strong>amor faz dele céu</strong> (paz, alegria). Em qual você vive é resultado direto dos acordos que sustenta.",
    "tip": "<strong>Cuidado:</strong> liberdade não é fazer o que quer por impulso — é viver pela verdade e pelo amor."
   }
  ]
 },
 "ch08-quinto-acordo": {
  "cards": [
   {
    "ic": "lens",
    "t": "Seja Cético, mas Aprenda a Ouvir",
    "b": "Não acredite cegamente — nem em si mesmo, nem em ninguém. Mas <strong>escute de verdade</strong>, para extrair o significado por trás das palavras. O ceticismo filtra a mentira; a escuta capta a intenção útil.",
    "tip": "<strong>Como aplicar:</strong> filtro de dupla camada — duvide do conteúdo literal e, ainda assim, ouça a intenção real."
   },
   {
    "ic": "layers",
    "t": "As Palavras são Símbolos",
    "b": "As palavras são apenas <strong>símbolos de símbolos</strong>; a verdade está atrás delas, não nelas. Por isso o ceticismo: a linguagem distorce — inclusive a sua própria voz interna.",
    "tip": "<strong>Regra:</strong> aplique o ceticismo primeiro às suas 'verdades' internas — muitas são acordos antigos disfarçados."
   },
   {
    "ic": "scale",
    "t": "Ceticismo + Escuta = Discernimento",
    "b": "Ceticismo <strong>sem</strong> escuta vira arrogância fechada; escuta <strong>sem</strong> ceticismo vira credulidade. Juntos, viram discernimento — e completam, não substituem, os quatro acordos.",
    "tip": "<strong>Atalho:</strong> descarte o veneno, fique só com o que for útil e verificável."
   }
  ]
 }
}
```
