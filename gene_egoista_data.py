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
      {"ic":"spiral","t":"Replicador × Veículo","b":"O <strong>replicador</strong> (o gene) é a informação copiada que persiste por gerações; o <strong>veículo</strong> (o organismo) é a máquina mortal que o abriga e propaga. O corpo morre; o gene é potencialmente <em>imortal</em>.","tip":"<strong>Como aplicar:</strong> ao explicar uma adaptação, separe o que é replicador (persiste e é copiado) do que é veículo (efêmero).","warn":True},
      {"ic":"layers","t":"Máquina de Sobrevivência","b":"Todo organismo é um robô construído pelos genes para abrigá-los. 'Eles nos criaram, corpo e mente.' Os genes não controlam em tempo real — <strong>programam</strong> estratégias que o cérebro executa sozinho.","tip":"<strong>Modelo mental:</strong> gene = programador; animal = programa rodando, autônomo na execução mas com objetivos herdados."},
      {"ic":"leaf","t":"Os Três Trunfos do Replicador","b":"O replicador bem-sucedido maximiza <strong>longevidade</strong> (durar), <strong>fecundidade</strong> (copiar muito) e <strong>fidelidade</strong> (copiar com precisão). A vida começou com uma molécula que, por acaso, fazia cópias de si no caldo primordial.","tip":"<strong>Para refletir:</strong> evolução é, no fundo, 'sobrevivência dos estáveis' — quem persiste, prevalece."},
      {"ic":"scale","t":"A Falácia do 'Bem da Espécie'","b":"Animais não agem 'para preservar a espécie' — a <strong>seleção de grupo</strong> é instável: um mutante egoísta invade e domina o grupo altruísta. A seleção atua muito abaixo: no gene.","tip":"<strong>Regra:</strong> ao ouvir 'isso evoluiu para o bem da espécie', desconfie e reformule no nível do gene.","warn":True},
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
      {"ic":"link","t":"Seleção de Parentesco","b":"Genes de altruísmo dirigido a <strong>parentes</strong> se espalham porque os parentes tendem a carregar os mesmos genes. O laço de sangue não importa por si — importa o <strong>gene compartilhado</strong> que ele sinaliza.","tip":"<strong>Modelo mental:</strong> trate parentes como bancos parciais dos seus genes — ajudar um irmão é 'investir meio você mesmo'.","warn":True},
      {"ic":"target","t":"A Regra de Hamilton (rB > C)","b":"Um gesto altruísta evolui quando <strong>r × B > C</strong>: <em>r</em> = grau de parentesco, <em>B</em> = benefício ao receptor, <em>C</em> = custo ao doador. Haldane: 'eu morreria por dois irmãos ou oito primos'.","tip":"<strong>Como aplicar:</strong> estime r, B e C — se o produto rB excede C, o altruísmo tende a se fixar."},
      {"ic":"fork","t":"O Grau de Parentesco (r)","b":"r é a probabilidade de o parente carregar o mesmo gene: <strong>½</strong> para irmãos e pais–filhos, <strong>¼</strong> para tios e avós, <strong>⅛</strong> para primos, <strong>1</strong> para gêmeos idênticos. O cuidado se gradua pela proximidade.","tip":"<strong>Para refletir:</strong> r é uma probabilidade genética, não um sentimento — por isso o altruísmo é desigual entre parentes e estranhos."},
      {"ic":"person","t":"O Conflito Dentro do Laço","b":"Como o parentesco é parcial (r<1), os interesses divergem mesmo entre quem se ama: <strong>pais × filhos</strong> (cada filho quer mais que a parte justa), <strong>machos × fêmeas</strong> (quem investe mais é mais 'explorável'). O laço é cooperação <em>e</em> conflito.","tip":"<strong>Modelo mental:</strong> o choro do filhote pode ser sinal honesto OU manipulação para extrair mais investimento."},
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
      {"ic":"scale","t":"Estratégia Evolutivamente Estável (EEE)","b":"Uma estratégia que, adotada pela maioria, <strong>não pode ser invadida</strong> por nenhuma alternativa rara. É um <strong>equilíbrio</strong>, não um ótimo coletivo — pode ser ruim para todos e ainda assim estável.","tip":"<strong>Teste:</strong> imagine a população toda numa estratégia + um mutante raro; se resiste à invasão, é EEE.","warn":True},
      {"ic":"sword","t":"Falcão × Pomba","b":"'Falcão' sempre luta; 'Pomba' exibe e recua. Nenhum é EEE puro — a população estabiliza numa <strong>mistura</strong> dos dois. Mostra por que o mundo animal não é nem todo agressivo nem todo pacífico.","tip":"<strong>Modelo mental:</strong> pense em comportamento social como jogo — o que compensa depende do que os outros fazem."},
      {"ic":"wave","t":"Altruísmo Recíproco","b":"Cooperação entre <strong>não-parentes</strong> evolui quando os encontros se repetem e há memória: 'você coça minhas costas, eu coço as suas'. Exige reencontro, reconhecimento e detecção de trapaceiro.","tip":"<strong>Regra:</strong> sem repetição nem memória, a traição é estável — não conte com cooperação espontânea."},
      {"ic":"steps","t":"Olho por Olho: Os Bonzinhos em 1º","b":"No torneio de Axelrod (dilema do prisioneiro iterado), vence <strong>Olho por Olho</strong>: gentil (não trai primeiro), retaliador (pune na hora), perdoador (volta a cooperar) e claro. Em relações repetidas, a gentileza condicional é a estratégia robusta.","tip":"<strong>Como aplicar:</strong> maximize o ganho mútuo, não a diferença para o rival — a inveja piora seu resultado."},
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
      {"ic":"constellation","t":"O Meme","b":"<strong>Termo cunhado neste livro:</strong> a unidade de transmissão cultural (ideia, melodia, moda, crença) que se replica de cérebro a cérebro por imitação, sujeita à sua própria seleção. Memes competem por <strong>atenção e memória</strong>.","tip":"<strong>Modelo mental:</strong> pense em ideias como organismos competindo por mentes — vence quem se copia melhor, não quem é verdadeiro.","warn":True},
      {"ic":"eye","t":"Complexo de Memes (Memeplex)","b":"Memes que se reforçam e se propagam <strong>em conjunto</strong> — como doutrinas e ideologias. Um memeplex pode ser <strong>parasitário</strong>, espalhando-se mesmo contra o interesse de quem o carrega.","tip":"<strong>Para refletir:</strong> 'bom para o meme' ≠ 'bom para você', assim como 'bom para o gene' ≠ 'bom para o indivíduo'."},
      {"ic":"key","t":"O Fenótipo Estendido","b":"Os efeitos de um gene <strong>não param na pele</strong>: a represa do castor, o ninho do pássaro, a teia da aranha e até a <strong>manipulação do hospedeiro</strong> por um parasita são fenótipos do gene, agindo no mundo exterior. O gene alcança longe.","tip":"<strong>Modelo mental:</strong> apague a 'pele' como limite causal — o alcance do gene vai até onde chegam seus efeitos."},
      {"ic":"spark","t":"A Rebelião Contra os Genes","b":"Somos a única espécie capaz de <strong>prever</strong> e <strong>resistir</strong> à lógica dos genes (e dos memes) egoístas. Podemos cultivar altruísmo genuíno e cooperação deliberada. 'Temos o poder de nos voltar contra nossos criadores.'","tip":"<strong>Lembrete do autor:</strong> descrever como a seleção opera NÃO é endossá-la como ética — cuidado com a falácia naturalista."},
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
