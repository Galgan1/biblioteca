# -*- coding: utf-8 -*-
"""Conteúdo (pt-BR) de 'O Gene Egoísta' (The Selfish Gene) — Richard Dawkins."""

BOOK = {
  "title": "O Gene Egoísta",
  "author": "Richard Dawkins",
  "header_light": "O GENE",
  "header_bold": "EGOÍSTA",
  "subtitle": "VISÃO GERAL · A EVOLUÇÃO VISTA DO PONTO DE VISTA DO GENE",
  "intro": "A unidade fundamental da seleção natural não é a espécie, o grupo nem o indivíduo: é o gene. Os organismos são 'máquinas de sobrevivência' — veículos descartáveis construídos pelos genes para propagar suas cópias. O 'egoísmo' é uma metáfora técnica (maximizar cópias, não intenção), e dele emergem tanto o conflito quanto o altruísmo: parentes ajudam parentes porque compartilham genes, e a cooperação floresce onde os encontros se repetem. Dawkins fecha cunhando o meme, o segundo replicador — a unidade da evolução cultural.",
  "description": "Clássico de divulgação científica de Richard Dawkins (1976). A visão centrada no gene: replicador × veículo, máquinas de sobrevivência, seleção de parentesco e a regra de Hamilton (rB>C), estratégias evolutivamente estáveis (EEE) e teoria dos jogos (falcão × pomba), altruísmo recíproco e o dilema do prisioneiro iterado, e o meme como replicador cultural. Descrever a lógica do gene não é prescrevê-la como ética.",
  "tags": ["Biologia Evolutiva", "Ciência", "Comportamento"],
  "progress": "4 Capítulos",
  "cover": "assets/gene-egoista-cover.png",
  "overview_cards": [
    {"ic":"spiral","t":"A Visão Centrada no Gene","b":"A unidade da seleção não é a espécie nem o indivíduo, e sim o <strong>gene</strong> — o replicador potencialmente imortal. O organismo é só uma <strong>máquina de sobrevivência</strong> (veículo) que os genes constroem para se propagar.","tip":"<strong>Modelo mental:</strong> diante de qualquer comportamento, pergunte 'que gene se beneficia disto?', não 'o que é bom para a espécie?'.","warn":True},
    {"ic":"link","t":"Egoísmo do Gene, Altruísmo do Indivíduo","b":"'Egoísta' descreve o <strong>efeito</strong> (maximizar cópias), não uma intenção. Um gene egoísta pode construir um indivíduo <strong>altruísta</strong> — desde que o gesto favoreça cópias do mesmo gene em parentes (regra de Hamilton: rB>C).","tip":"<strong>Para refletir:</strong> não confunda os níveis — o egoísmo é do gene; o altruísmo pode ser do corpo."},
    {"ic":"constellation","t":"O Meme: o Segundo Replicador","b":"Dawkins <strong>cunha o termo meme</strong>: a unidade da evolução cultural (ideia, melodia, crença) que se copia de cérebro a cérebro por imitação. Vence o meme que melhor se replica — <strong>não</strong> necessariamente o verdadeiro ou útil.","tip":"<strong>Modelo mental:</strong> popularidade mede capacidade de cópia, não veracidade."},
  ],
}

CHAPTERS = [
  {
    "slug": "ch01-o-gene-como-unidade",
    "sub": "CAPÍTULO 1: O Gene Como Unidade da Seleção",
    "intro": "A tese do livro: a evolução faz mais sentido vista do ponto de vista do gene. Os genes que persistem são os bons em fazer cópias de si — e, para isso, constroem corpos: máquinas de sobrevivência temporárias e descartáveis a seu serviço.",
    "cards": [
      {"ic":"spiral","t":"Replicador Contra Veículo","emph":"Replicador","b":"O gene é o replicador mestre: uma informação blindada que atravessa gerações fazendo cópias de si. Você e todos os animais são apenas os veículos mortais, as carcaças provisórias que ele usa para viajar. O corpo é <strong>programado para morrer</strong>; a informação lá dentro luta para ser imortal.","tip":"<strong>Modelo mental:</strong> pare de olhar a evolução como a história dos bichos. É a história da informação persistindo através da morte dos bichos."},
      {"ic":"layers","t":"A Máquina De Sobrevivência","emph":"Máquina","b":"Todo organismo é um robô de carne perfeitamente desenhado para abrigar e proteger seus genes. Eles te criaram de corpo e alma. Porém, os genes não controlam você como titereiros em tempo real; eles <strong>programaram a máquina na largada</strong> e deixaram o seu cérebro executar a estratégia no escuro.","tip":"<strong>Como aplicar:</strong> lembre-se de que os seus desejos mais profundos (açúcar, sexo, status) foram instalados no seu cérebro para servir ao gene, não a você."},
      {"ic":"leaf","t":"Os Trunfos Do Replicador","emph":"Trunfos","b":"O jogo da evolução só premia quem obedece a três regras: durar muito tempo (longevidade), fazer cópias em massa (fecundidade) e errar pouco na cópia (fidelidade). Tudo começou no caos do caldo primordial quando uma única molécula, por puro acidente, <strong>conseguiu clonar a si mesma</strong> e desencadeou a vida.","tip":"<strong>Regra:</strong> na grande roleta da biologia, a lei suprema não é a força, mas a 'sobrevivência dos mais estáveis'."},
      {"ic":"scale","t":"A Ilusão Do Bem Maior","emph":"A Ilusão","b":"Apague da sua cabeça a ideia de que animais se sacrificam 'para preservar a espécie'. Um grupo de altruístas puros é um prato cheio: basta nascer um único mutante egoísta para ele explorar a bondade geral, <strong>multiplicar-se e dominar o grupo inteiro em poucas gerações</strong>. O jogo se decide no nível do gene, não do grupo.","tip":"<strong>Sinal de alerta:</strong> sempre que alguém justificar um instinto natural dizendo 'é para o bem da espécie', saiba que a biologia moderna rejeita essa tese.","warn":True},
    ],
    "lessons_title": "Lições-Chave do Capítulo 1",
    "lessons": [
      "A unidade da seleção é o gene (replicador); o organismo é seu veículo descartável.",
      "Genes programam estratégias antecipadamente; o cérebro as executa em tempo real.",
      "Longevidade, fecundidade e fidelidade definem o sucesso de um replicador.",
      "'Para o bem da espécie' é quase sempre uma explicação errada — a seleção de grupo é instável.",
    ],
  },
  {
    "slug": "ch02-parentesco-e-altruismo",
    "sub": "CAPÍTULO 2: Parentesco, Altruísmo e a Regra de Hamilton",
    "intro": "Se o gene é egoísta, por que existe altruísmo? Porque ajudar um parente propaga cópias dos seus próprios genes em outro corpo. A seleção de parentesco e a regra de Hamilton mostram exatamente quando o sacrifício compensa.",
    "cards": [
      {"ic":"link","t":"A Seleção De Parentesco","emph":"Parentesco","b":"Por que uma mãe morre pelo filho? Não é amor místico, é matemática genética. O instinto de altruísmo entre parentes evoluiu violentamente porque <strong>o beneficiário carrega cópias exatas do mesmo gene egoísta do doador</strong>. Ajudar um irmão a sobreviver é, na prática, ajudar uma cópia de si mesmo.","tip":"<strong>Como aplicar:</strong> os laços de sangue são fortes porque operam como bancos descentralizados para os seus próprios genes."},
      {"ic":"target","t":"A Fria Regra De Hamilton","emph":"Fria Regra","b":"O sacrifício obedece a um cálculo implacável: o altruísmo evolui se o custo para quem doa for menor que o benefício para quem recebe, <strong>multiplicado pela proximidade do parentesco (rB > C)</strong>. A natureza é contadora: ela só paga a conta se o retorno genético for matematicamente positivo.","tip":"<strong>Modelo mental:</strong> como dizia o biólogo Haldane em tom de piada afiada: 'eu daria minha vida para salvar dois irmãos ou oito primos'."},
      {"ic":"fork","t":"A Matemática Do Sangue","emph":"Matemática","b":"O cuidado animal é distribuído como uma aposta probabilística. A chance de carregar o mesmo gene despenca rapidamente: 50% para irmãos, 25% para tios e avós, 12,5% para primos de primeiro grau. É por isso que o altruísmo <strong>seca tão rápido à medida que o parentesco se afasta</strong>.","tip":"<strong>Prática:</strong> compreenda que o nepotismo biológico não é um defeito moral da natureza, é o design lógico da propagação."},
      {"ic":"person","t":"A Guerra Na Família","emph":"Guerra","b":"Como você compartilha só metade dos genes com seu irmão, há 50% de motivo para amar e 50% para competir. Até o útero é um campo de batalha: o feto quer sugar o máximo, a mãe quer poupar recursos para os próximos filhos. Onde o parentesco não é total, <strong>o afeto sempre vem costurado com conflito profundo</strong>.","tip":"<strong>Sinal de alerta:</strong> romantizar a família como um ambiente de paz absoluta ignora o cabo de guerra genético que opera no subsolo das relações.","warn":True},
    ],
    "lessons_title": "Lições-Chave do Capítulo 2",
    "lessons": [
      "Ajudar parentes propaga seus próprios genes — altruísmo a serviço do egoísmo do gene.",
      "Regra de Hamilton: o gesto altruísta se fixa quando rB > C.",
      "r mede quanto de 'você' há no outro: ½ para irmãos, ⅛ para primos.",
      "Como r < 1, há conflito de interesses embutido até nos laços de família.",
    ],
  },
  {
    "slug": "ch03-estrategias-estaveis",
    "sub": "CAPÍTULO 3: Estratégias Estáveis e Cooperação",
    "intro": "Por que os animais raramente lutam até a morte, e como a cooperação surge entre quem não é parente? A teoria dos jogos responde: não pelo bem do grupo, mas porque certas estratégias são estáveis — imbatíveis pelo desvio individual.",
    "cards": [
      {"ic":"scale","t":"O Equilíbrio De Ferro","emph":"Equilíbrio","b":"Uma Estratégia Evolutivamente Estável (EEE) é um padrão que, uma vez adotado pela maioria, <strong>esmaga qualquer comportamento rebelde que tente invadir</strong>. É o ponto de estagnação. Ela não existe para maximizar a felicidade ou a eficiência de todos, mas simplesmente porque resiste à subversão de um mutante espertinho.","tip":"<strong>Modelo mental:</strong> muitos equilíbrios sociais e biológicos são dolorosos para todos, mas continuam existindo porque a primeira pessoa a mudar sempre sai perdendo."},
      {"ic":"sword","t":"Falcão Contra Pomba","emph":"Falcão","b":"Imagine um mundo só de Falcões (lutam até a morte) e Pombas (recuam ao primeiro rugido). Se todos são pacíficos, um Falcão domina tudo; se todos são assassinos, ser Pomba garante a sobrevivência nas margens. A biologia sempre <strong>congela a sociedade numa mistura exata e matemática</strong> dos dois perfis.","tip":"<strong>Como aplicar:</strong> em qualquer ambiente competitivo humano ou animal, não espere a paz total nem a guerra total: o equilíbrio exige as duas posturas."},
      {"ic":"wave","t":"O Altruísmo Recíproco","emph":"Recíproco","b":"Para surgir cooperação entre não-parentes, o cérebro precisou inventar a memória social: 'eu arranho suas costas se você arranhar as minhas'. Mas esse pacto é frágil. Ele só vinga se as partes <strong>souberem que vão se encontrar de novo</strong> e tiverem o poder afiado de identificar e punir quem trapaceia.","tip":"<strong>Regra:</strong> se você não vai ver a pessoa de novo amanhã, o incentivo frio da biologia diz para você trair o acordo hoje. A repetição cria a confiança."},
      {"ic":"steps","t":"Olho Por Olho","emph":"Olho","b":"No longo prazo, a estratégia vencedora para relações contínuas é simples e aterradora: seja um 'Olho por Olho'. Comece cooperando e nunca traia primeiro. Mas, se o outro te golpear, <strong>bata de volta no mesmo segundo, sem piedade</strong>. E então perdoe rápido se ele voltar a cooperar. É a firmeza sem rancor.","tip":"<strong>Sinal de alerta:</strong> ser o bonzinho incondicional atrai a exploração rápida e mortal dos egoístas. A bondade só sobrevive se vier armada.","warn":True},
    ],
    "lessons_title": "Lições-Chave do Capítulo 3",
    "lessons": [
      "EEE é a estratégia imbatível pelo desvio — equilíbrio, não ótimo coletivo.",
      "Populações estabilizam em misturas de estratégias (falcão/pomba), não em tipos puros.",
      "Altruísmo recíproco exige encontros repetidos, reconhecimento e memória.",
      "Em jogos repetidos vence Olho por Olho: gentil, retaliador, perdoador e claro.",
    ],
  },
  {
    "slug": "ch04-memes-e-alcance",
    "sub": "CAPÍTULO 4: Memes e o Longo Alcance do Gene",
    "intro": "Dawkins amplia a tese em duas direções: a evolução ganha um segundo replicador na cultura — o meme; e o alcance do gene não para na pele do corpo que o carrega. Fecho moral: somos a única espécie capaz de se rebelar contra os próprios replicadores.",
    "cards": [
      {"ic":"constellation","t":"O Salto Do Meme","emph":"Meme","b":"A evolução deu um solavanco: agora há um segundo replicador no planeta. O 'meme' é qualquer ideia, melodia, dogma ou fofoca que pula de cérebro em cérebro por pura imitação. Como vírus na sua mente, eles lutam ferozmente por <strong>um segundo da sua atenção e memória</strong> para se propagarem mais longe.","tip":"<strong>Como aplicar:</strong> o valor de uma ideia no mercado dos memes não é ser verdadeira ou boa, é ser pegajosa e impossível de não repassar."},
      {"ic":"eye","t":"O Complexo Memético","emph":"Complexo","b":"As grandes religiões, as modas e as ideologias são memeplexos: exércitos de memes que se aliaram para sobreviver juntos no hospedeiro. E o perigo é brutal: um meme altamente contagioso pode <strong>escravizar a sua vida e forçar você ao sacrifício físico</strong> só para garantir que a ideia continue viva.","tip":"<strong>Sinal de alerta:</strong> uma doutrina sedutora pode ser incrivelmente perigosa para você e, ainda assim, perfeitamente bem-sucedida em se multiplicar no mundo.","warn":True},
      {"ic":"key","t":"O Fenótipo Estendido","emph":"Estendido","b":"Pare de achar que o corpo é o limite do gene. A teia cravada entre duas árvores é uma extensão da aranha; o castor modificando o fluxo de um rio colossal é a mão invisível da genética agindo no ambiente. O poder de manipulação do gene <strong>não para na borda da pele, ele refaz o mundo</strong>.","tip":"<strong>Modelo mental:</strong> veja a tecnologia humana, as barragens e as cidades como o nosso gigantesco fenótipo estendido saltando para fora dos corpos."},
      {"ic":"spark","t":"A Nossa Grande Rebelião","emph":"Rebelião","b":"Somos as únicas máquinas no universo capazes de encarar a verdade sombria dos nossos criadores de código. Porque temos previsão e cultura, podemos <strong>dizer um não estrondoso aos nossos genes e memes egoístas</strong>, escolhendo o altruísmo deliberado e construindo um destino além da biologia crua.","tip":"<strong>Regra:</strong> entender a selva do gene egoísta não é uma licença ética para imitar a selva; é adquirir o mapa para escapar da tirania dela."},
    ],
    "lessons_title": "Lições-Chave do Capítulo 4",
    "lessons": [
      "O meme é o segundo replicador — a unidade da evolução cultural, cunhada neste livro.",
      "O sucesso de um meme depende de sua capacidade de cópia, não de sua verdade ou utilidade.",
      "O fenótipo de um gene inclui seus efeitos fora do corpo (artefatos e manipulação).",
      "Só o humano pode se rebelar contra genes e memes egoístas — descrever a natureza não é prescrevê-la.",
    ],
  },
]
