# -*- coding: utf-8 -*-
"""Conteúdo (pt-BR) de 'A Lógica do Cisne Negro' (Nassim Nicholas Taleb)."""

BOOK = {
  "title": "A Lógica do Cisne Negro",
  "author": "Nassim Nicholas Taleb",
  "header_light": "CISNE",
  "header_bold": "NEGRO",
  "subtitle": "VISÃO GERAL · O IMPACTO DO ALTAMENTE IMPROVÁVEL",
  "intro": "Um Cisne Negro é o evento raro, de impacto extremo, que depois racionalizamos como se fosse previsível. Taleb mostra que quase tudo que importa na história vem desses eventos — e que nossas ferramentas de previsão (a curva de sino, as narrativas, os modelos de jogo) nos cegam para eles. A saída não é prever melhor, mas tornar-se robusto ao imprevisível.",
  "description": "Ensaio de Nassim Taleb sobre o evento Cisne Negro: raro, de impacto extremo e previsível só em retrospecto. Mediocristão × Extremistão, falácia narrativa, problema da indução (o peru de Russell), evidência silenciosa, falácia lúdica, arrogância epistêmica, a fraude da curva de sino e a robustez (estratégia barbell) diante do imprevisível.",
  "tags": ["Incerteza", "Risco", "Epistemologia"],
  "progress": "8 Capítulos",
  "cover": "assets/cisne-negro-cover.png",
  "overview_cards": [
    {"ic":"wave","t":"O Cisne Negro","b":"Evento que reúne três traços: é uma <strong>surpresa rara</strong> (nada no passado apontava), tem <strong>impacto extremo</strong> e é <strong>racionalizado depois</strong> como se fosse previsível. Quase tudo que importa — crashes, guerras, descobertas — é Cisne Negro.","tip":"<strong>Teste:</strong> foi imprevisto? o impacto foi extremo? estão contando uma história que o faz parecer óbvio só agora? Três 'sim' = Cisne Negro.","warn":True},
    {"ic":"scale","t":"Mediocristão × Extremistão","b":"No <strong>Mediocristão</strong> (peso, altura) nenhum evento isolado move o total e a curva de sino funciona. No <strong>Extremistão</strong> (riqueza, vendas, fama, crashes) um único evento domina tudo — é o lar do Cisne Negro.","tip":"<strong>Modelo mental:</strong> antes de qualquer estatística, pergunte 'um único caso pode ser maior que todo o resto somado?' Se sim, é Extremistão."},
    {"ic":"eye","t":"Evidência Silenciosa","b":"Julgamos pelo que sobrou e está visível, ignorando o <strong>cemitério dos que fracassaram igual</strong>. A história é escrita pelos vencedores — literalmente, na amostra. Por isso confundimos sorte com talento (o 'idiota sortudo').","tip":"<strong>Para refletir:</strong> antes de copiar um vencedor, pergunte 'onde estão os que fizeram o mesmo e quebraram?'"},
  ],
}

CHAPTERS = [
  {
    "slug": "ch01-o-cisne-negro",
    "sub": "CAPÍTULO 1: O que é um Cisne Negro",
    "intro": "Na Europa, 'todo cisne é branco' foi verdade indutiva até acharem cisnes pretos na Austrália — uma única observação destruiu milênios de certeza. O Cisne Negro é o evento raro, de impacto extremo, que o cérebro racionaliza depois como previsível, apagando a surpresa e impedindo o aprendizado.",
    "cards": [
      {"ic":"wave","t":"A Tríade Do Cisne Negro","emph":"Cisne Negro","b":"Ele pousa rasgando tudo com as três garras expostas: uma raridade cega aos radares, uma pancada que esfarela a mesa de xadrez e <strong>uma sensação mentirosa de lógica costurada apenas quando a fumaça sobe</strong>. A História pula movida a esses assombros, enquanto a nossa ciência contábil finge medir águas serenas.","tip":"<strong>Sinal de alerta:</strong> arranque o verniz do “era questão de tempo” — se fosse óbvio e fácil, os profetas estariam milionários.","warn":True},
      {"ic":"spiral","t":"O Peru De Russell","emph":"Peru","b":"A ave recebe a lavagem grossa diária do fazendeiro e a sua certeza no paraíso inquebrável atinge os céus tranquilos. Na véspera do machado, <strong>o momento de maior conforto e gordura do peito escancara o risco letal</strong> batendo de frente. Não ver rastro da morte atrás do pasto verde não cancela o fio do açougueiro.","tip":"<strong>Modelo mental:</strong> ausência cega de prova não atesta, nem de longe, que o perigo fantasma se mudou — a navalha afia no escuro."},
      {"ic":"lens","t":"A Ilusão Retrospectiva","emph":"Retrospectiva","b":"Assim que o meteoro atinge a praça, o nosso cérebro acovardado aplica cimento em tudo e <strong>limpa a sujeira brutal inventando pontes de causas idiotas até a porrada não parecer surpresa</strong>. Engolir essa historinha anestesia a dor profunda da ignorância viva e cega, nos jogando mansos no colo do próximo trauma fatal.","tip":"<strong>Prática:</strong> exija anotar as suas certezas a lápis antes do temporal bater; só a lista molhada esfregará o fracasso do oráculo."},
      {"ic":"book","t":"A Antibiblioteca De Eco","emph":"Antibiblioteca","b":"O gênio italiano estocava montanhas de papel encadernado que nunca abriu porque honrava que <strong>o ouro real e mortal jaz exatamente no vão escuro daquilo que escapou da sua leitura</strong>. A sua parede de folhas não ostenta sabedoria rasa; ela deve escrachar o precipício colossal da sua própria burrice abissal diária.","tip":"<strong>Modelo mental:</strong> a régua que avalia o sujeito perigoso ignora os diplomas da parede e foca na montanha fria do que ele não domina."},
    ],
    "lessons_title": "Lições-Chave do Capítulo 1",
    "lessons": [
      "Um Cisne Negro é raro, de impacto extremo e racionalizado depois como previsível.",
      "O que está fora do seu mapa costuma importar mais do que o que está nele.",
      "Ausência de evidência não é evidência de ausência — o evento decisivo ainda não apareceu na amostra.",
      "A previsibilidade retrospectiva é a armadilha que impede o aprendizado.",
    ],
  },
  {
    "slug": "ch02-arrogancia-epistemica",
    "sub": "CAPÍTULO 2: Arrogância Epistêmica e a Tríade da Opacidade",
    "intro": "Achamos que sabemos mais do que sabemos. Essa arrogância epistêmica cresce com a informação e a especialização, e nos cega para o Cisne Negro. Diante da história, a mente sofre três males — a tríade da opacidade — que a fazem confundir o mapa elegante com o território caótico.",
    "cards": [
      {"ic":"target","t":"A Arrogância Epistêmica","emph":"Arrogância","b":"A gente bota num altar fino a poeira de jornal que decorou de manhã e escarra em cima do vulcão negro incerto. A avalanche inútil de dados <strong>incha a empáfia acadêmica do peito muito mais rápido que melhora a precisão real no jogo cru</strong>. O analista de gravata afunda no barco tão cego quanto a porta de madeira.","tip":"<strong>Armadilha:</strong> jogue fora as desculpas engravatadas e cegas — exija olhar as faturas rasgadas de quem apostou e suou no mercado.","warn":True},
      {"ic":"triangle","t":"A Tríade Da Opacidade","emph":"Opacidade","b":"Enfrentando o triturador imenso de carne humana engolimos três venenos de farmácia: <strong>fingimos sacar as engrenagens ocultas, maquiamos os acidentes mortos de ontem com lógicas fáceis</strong> e adoramos o profeta que cospe sílabas complicadas fingindo saber. O tecido do real cheira a sangue, mas juramos que é de seda.","tip":"<strong>Modelo mental:</strong> na frente das reportagens impecáveis e lisas de domingo, fareje a falácia inventada de longe pra envernizar o caos."},
      {"ic":"layers","t":"A Falha Da Platonicidade","emph":"Platonicidade","b":"Nosso olhar covarde funde os rabiscos coloridos do projeto de papelão com a lama tóxica espirrando dos pneus da calçada. Rejeitamos o sujo e fugimos pros abrigos quentes de equações lisinhas e fáceis. <strong>É bem nas quinas feias e estilhaçadas, onde a teoria de lousa derrete e falha</strong>, que o mal varre fortunas em segundos.","tip":"<strong>Para refletir:</strong> encare o molde polido de cera da teoria e aceite que, no embate franco do suor, as bordas esburacadas vão estourar tudo."},
      {"ic":"eye","t":"Os Cadáveres Despercebidos","emph":"Despercebidos","b":"A multidão histérica carrega nos ombros dourados quem subiu ao pódio, empurrando pra vala as montanhas de esqueletos de sujeitos que deram exatamente o mesmo chute e viraram pó. Apagar o cemitério <strong>transmuta num passe mágico a roleta de pura bobeira cega em suposto dom majestoso</strong> e talento indomável da cartilha corporativa.","tip":"<strong>Regra:</strong> recuse imitar de forma barata os passos do trilionário de palco sem botar na mesa de necrotério a chapa dos afogados silenciados."},
    ],
    "lessons_title": "Lições-Chave do Capítulo 2",
    "lessons": [
      "Quanto mais sabemos, mais confiantes ficamos — não necessariamente mais certos.",
      "A tríade da opacidade: ilusão de entender, distorção retrospectiva, excesso de fé na informação.",
      "Platonicidade é confundir o mapa elegante com o território caótico.",
      "O viés de sobrevivência transforma sorte em 'talento'; procure o contraexemplo, não a confirmação.",
    ],
  },
  {
    "slug": "ch03-falacia-narrativa",
    "sub": "CAPÍTULO 3: A Falácia Narrativa",
    "intro": "A mente não suporta fatos crus: ela tece histórias de causa e efeito para reduzir a complexidade a algo memorável. Essa falácia narrativa dá a ilusão de entender o passado e prever o futuro — e esconde sistematicamente o papel do acaso e do Cisne Negro.",
    "cards": [
      {"ic":"bubble","t":"A Falácia Narrativa","emph":"Narrativa","b":"Nossas entranhas repulsam fios cortados caindo soltos, então nós <strong>enfarpelamos a poça de fatos crus fétidos com uma historinha barata e charmosa do herói vencendo obstáculos</strong>. Costuramos os cordões do destino no vazio só pra poder dormir no colchão de penas no frio da incerteza mortal. A verdade pura dói quieta.","tip":"<strong>Como aplicar:</strong> jogue ácido e esfregue duro nos conectivos lógicos que fingem atar a linha do tempo; veja o castelo murchar sem nexo."},
      {"ic":"fork","t":"O Teste Das Duas Histórias","emph":"Duas Histórias","b":"Quando a pena engravatada justifica que a mesma inflação fantasma serve tanto pra alta rasgada das telas de pregão quanto pro chão caindo oco de medo e de morte, sinta a fraude rolando solta. Uma fábula esticada que <strong>engole sorrindo e justifica as duas metades opostas da batida do pneu</strong> não tem luz de verdade e fede lixo raso.","tip":"<strong>Modelo mental:</strong> puxe a gangorra do noticiário invertendo o resultado final de ponta-cabeça e assista o jornalista escorregar na mesma maionese."},
      {"ic":"steps","t":"Fatos Soltos Antes Do Enredo","emph":"Fatos Soltos","b":"A pupila caça faces de ursos rolando soltas nas nuvens gordas do céu e enxerga ordens mágicas amarradas na parede mofada das finanças diárias onde urra só <strong>uma jaula barulhenta sem grade com baques de pura aleatoriedade de grana</strong>. Engula como remédio amargo e espinhento o número bruto solitário fugindo da crônica doce furada.","tip":"<strong>Prática:</strong> carimbe no caderno as justificativas engomadas cruas de sangue antes da poeira da roleta abaixar, só pra não inventar balela amanhã."},
    ],
    "lessons_title": "Lições-Chave do Capítulo 3",
    "lessons": [
      "A mente troca a verdade crua por histórias compactas — e acredita nelas.",
      "Se a narrativa explicaria igualmente bem o resultado oposto, ela não explica nada.",
      "Reescrevemos a memória para caber num bom enredo.",
      "A narrativa apaga o acaso — e com ele, o Cisne Negro.",
    ],
  },
  {
    "slug": "ch04-mediocristao-extremistao",
    "sub": "CAPÍTULO 4: Mediocristão × Extremistão",
    "intro": "Há dois tipos de aleatoriedade, dois 'países'. No Mediocristão, nenhum evento isolado muda muito o total — a média manda. No Extremistão, um único evento pode dominar tudo — é o reino do escalável e o lar dos Cisnes Negros. Confundir um pelo outro é o erro fatal.",
    "cards": [
      {"ic":"mountain","t":"As Regras Do Mediocristão","emph":"Mediocristão","b":"No cercadinho pacato pesa duro o chumbo da biologia lenta e física pesada: se botar um milhão de formigas comuns na mesma balança cega com o morador da calça mais esgarçada do planeta, <strong>o balofo sozinho jamais empurrará o ponteiro da curva da média da multidão mansa para cima ou pra baixo</strong>. A gaussiana aqui reina serena de berço.","tip":"<strong>Régua:</strong> se puxar para a amostra o sujeito mais anômalo e irreal e ele não sacudir nem arranhar o total do bolo grande, relaxe na poça plana."},
      {"ic":"spark","t":"O Abismo Do Extremistão","emph":"Extremistão","b":"Aqui o sino de gesso quebrou de nojo e os cifrões galopam soltos furando escudos: livros, balas da guerra e telas espelhadas abrem caminho sangrando as contas. Um só jogador bizarro <strong>pode bater de frente estourando sozinho todo o volume restante na máquina e roubar de bobeira a fatia suculenta esmagando a feira limpa inteira</strong>.","tip":"<strong>Sinal de alerta:</strong> prever o furacão de notas fiscais insanas usando régua de escola é engolir a granada achando que chupa morango.","warn":True},
      {"ic":"scale","t":"O Ganho Escalável","emph":"Escalável","b":"O cirurgião cobra suado no osso gasto das costas encurvadas trocando milagres de cama por moedas no relógio mudo. Já o escritor liso de terno solto ou o analista frio de telas pretas voam pesados de bolso <strong>arrastando arrastão de ganhos enormes apertando um mesmo par de teclas numa porrada solitária jogada pelo mundo rasgando a rede oca inteira</strong>.","tip":"<strong>Modelo mental:</strong> divida o asfalto antes do salto: profissões que dependem da pá correndo a areia não multiplicam ouro cego enquanto a lua rola no céu."},
    ],
    "lessons_title": "Lições-Chave do Capítulo 4",
    "lessons": [
      "Mediocristão: nenhum caso isolado move o total; a gaussiana funciona.",
      "Extremistão: um único evento pode dominar tudo; é onde vivem os Cisnes Negros.",
      "Antes de qualquer estatística, identifique em qual 'país' você está.",
      "O escalável concentra ganhos (winner-take-all) e amplia o risco de cauda.",
    ],
  },
  {
    "slug": "ch05-falacia-ludica",
    "sub": "CAPÍTULO 5: A Falácia Lúdica e a Evidência Silenciosa",
    "intro": "Confundimos o risco esterilizado dos jogos (dados, cassino, modelos) com a incerteza da vida real, onde as regras são desconhecidas. Essa falácia lúdica é a base de quase toda matemática de risco mal aplicada. E a evidência silenciosa esconde os fracassos, distorcendo as probabilidades.",
    "cards": [
      {"ic":"target","t":"A Falácia Lúdica","emph":"Lúdica","b":"O feltro verde das mesas de fichas plastificadas respira no tubo limpo ensaiado do dado solto redondo. Na rua esburacada, o monstro cospe caco de vidro cruzando no escuro, <strong>estraçalhando feio de lado a proteção que suas fórmulas arrumaram lendo manual morno que prometia domar as feras mudas e lógicas do bolso</strong>.","tip":"<strong>Sinal de alerta:</strong> as planilhas cravadas recheadas de casas preenchendo zeros redondos mascaram a cova preta esticada lá embaixo do assoalho oco.","warn":True},
      {"ic":"eye","t":"A Evidência Silenciosa","emph":"Silenciosa","b":"A igreja da praia ferve reluzindo as plaquinhas esmaltadas de marinheiros fortes que rezaram alto e o navio boiou em paz na pedra. Debaixo d'água o mar esconde <strong>no esquecimento gordo grosso sujo mudo os pulmões apodrecidos dos trouxas que choraram a mesmíssima prece e afundaram engolindo o barro verde e chumbo denso e mudo</strong>.","tip":"<strong>Modelo mental:</strong> pare na calçada e arranque a tinta fresca do sucesso para desenterrar, com pá cega, as ovelhas chacinadas na mesma tática torta."},
      {"ic":"person","t":"Os Macacos Sortudos","emph":"Sortudos","b":"Se jogar um mar de chimpanzés de óculos escuros apertando botão de ação no breu, dez sairão de laço fino e bota limpa coroando capas de revista de sucesso na faria lima solta. A peneira caótica brutal adora <strong>bater carimbo de rei majestoso de talento insuperável em roletas suadas vulgares que escaparam puramente de raspão rasgado do triturador mudo da lama</strong>.","tip":"<strong>Para refletir:</strong> exija auditar o pátio de sucatas cheirando zinco estourado antes de babar no diploma dourado do sobrevivente sortudo do jogo que deu bom."},
    ],
    "lessons_title": "Lições-Chave do Capítulo 5",
    "lessons": [
      "A vida não é cassino: o que quebra você vem de fora do modelo.",
      "Precisão estatística sobre incerteza real é fingimento perigoso.",
      "A evidência silenciosa esconde os fracassos e infla as probabilidades de sucesso.",
      "Resultado não é prova de habilidade — sorte se disfarça de talento.",
    ],
  },
  {
    "slug": "ch06-limites-da-previsao",
    "sub": "CAPÍTULO 6: Os Limites da Previsão",
    "intro": "Somos péssimos em prever, sobretudo o que mais importa, e pioramos quando nos especializamos. A maior parte do progresso vem de descobertas que ninguém planejou. Em vez de prever, é preciso preparar-se para o imprevisível e maximizar a exposição ao acaso positivo.",
    "cards": [
      {"ic":"lens","t":"O Escândalo Da Previsão","emph":"Previsão","b":"A turba de paletó da academia erra fundo de cara enfiada no lodo na exata mesma batida cega dos pedreiros do balcão de rua, <strong>usando apenas a cortina defumada de jargões pedantes grossos pra varrer do tapete as crateras das apostas furadas estúpidas afundadas no chumbo passado raso</strong>. Ter anel no dedo não blinda o ego do precipício gordo sujo de tinta.","tip":"<strong>Armadilha:</strong> o risco mais agressivo e afiado nunca anda de farol aceso na média limpa da prancheta do figurão de tela de TV.","warn":True},
      {"ic":"key","t":"A Serendipidade Guia","emph":"Serendipidade","b":"As lâmpadas brilhantes que operam miolos de tela escorregaram rindo num tubo de quebra suja que despencou de estante frouxa no canto escuro fedido à sorte limpa gorda de mesa de química tonta solta e livre. Para trancar o horizonte novo em grade de papel plano e cinza você <strong>carece de antecipar o que a ciência ainda engatinha tateando cega sem saber nascer ou sangrar</strong>.","tip":"<strong>Modelo mental:</strong> regue e nutra pesadamente os terrenos férteis para o acidente sem dono rebentar na cara; pare de orquestrar a roleta no milímetro do sino."},
      {"ic":"pivot","t":"A Bricolagem Constante","emph":"Bricolagem","b":"Esqueça esfregar bola cega de cristal barato suja de vidro oco de rua. A colheita furiosa planta tombos minúsculos esfolando só as pontinhas de joelhos pra recolher solto rindo à toa e farto da grama <strong>a montanha esmagadora brutal rara colossal rica solta preta e gorda cega da porrada que enxuga tudo e paga a lona mansa de raspão grosso de bilhete rico na roda do ano inteiro</strong>.","tip":"<strong>Como aplicar:</strong> forre o chão de pequenos furos e armadilhas inofensivas bobas e caia abraçando os presentes raros anômalos gordos do Cisne Bom solto aberto cego limpo."},
    ],
    "lessons_title": "Lições-Chave do Capítulo 6",
    "lessons": [
      "Erramos previsões justamente no que mais importa — e com excesso de confiança.",
      "Especialização aumenta a arrogância, não a acurácia.",
      "As maiores descobertas são acidentais: cultive a serendipidade.",
      "Não tente prever o futuro; posicione-se para sobreviver e lucrar com o imprevisto.",
    ],
  },
  {
    "slug": "ch07-fraude-do-sino",
    "sub": "CAPÍTULO 7: A Curva de Sino, Essa Grande Fraude Intelectual",
    "intro": "A curva de sino é uma ferramenta legítima no Mediocristão e uma fraude intelectual quando aplicada ao Extremistão. Ela faz os eventos extremos parecerem impossíveis — exatamente os Cisnes Negros que dominam o resultado. É o erro embutido em quase toda a finança acadêmica.",
    "cards": [
      {"ic":"wave","t":"A Fraude Da Curva","emph":"Curva","b":"O desenho de sino ensina de lousa chata no sol que as tempestades de pregos finos somem feito pó de asfalto quando andam poucos metros saindo do centro mole fraco da média manca. Porém, a selva do mercado doido <strong>arranca os limites da folha mastigando a probabilidade cega e te esfaqueia com monstros pesados soltos rindo do cálculo amansado morno afogado do doutorzinho raso no poço podre macio e liso sem escudos de couro limpo</strong>.","tip":"<strong>Sinal de alerta:</strong> confie o seu osso limpo ao padrão da curva plana e colha do caixão um soco frio de chumbo quente esburacado letal.","warn":True},
      {"ic":"layers","t":"O Perigo Das Caudas Gordas","emph":"Caudas Gordas","b":"Na terra das calculadoras, o apocalipse distante é mito covarde que não chega de barco na praia frouxa mansa nula da calçada limpa morta chata livre redonda e branca de mesa gorda suja falsa cega na prancheta fria oca sem som de tombo surdo mole livre sujo. <strong>O buraco real escorre sangue de fat tails inchadas de peso estourando a boca do balão sem mandar cartas de pêsames pra ninguém acordar pronto armado cego ou alerta mudo vivo em paz fria de gelo solto e fraco de chumbo branco torto falso no mercado cego de ouro ou fogo</strong>.","tip":"<strong>Regra:</strong> cauda gorda diz de terno cru: o evento mais irreal do caderno de ficção vai, com toda a certeza cega de chumbo frio nulo, pagar a conta e fechar o caixão do mês logo ou cedo."},
      {"ic":"constellation","t":"Os Cisnes Cinza","emph":"Cisnes Cinza","b":"A quebra bizarra esticando perdas num só mergulho rascante era impossível no mapa mudo chato fedendo giz de lousa, mas fumaça preta cruzou e esturricou as velas brancas mansas do rio manso frouxo liso. As fraturas não são obra de zumbi; são apenas <strong>trombadas brutais da matemática cega gigante gorda de fractais sujos escancarando dentes rindo alto de costas do falso abrigo limpo frouxo morno liso afundado nulo na poça barata cega de pano molhado fraco liso plano e murcho sem base reta na roda crua feia grande solta parda viva</strong>.","tip":"<strong>Modelo mental:</strong> se a água que ferve corre e sobe de degrau escalável rasgado grosso de poço negro, não engula o sedativo de cera fria do sino."},
    ],
    "lessons_title": "Lições-Chave do Capítulo 7",
    "lessons": [
      "A gaussiana é válida no Mediocristão e fraudulenta no Extremistão.",
      "Caudas gordas: extremos são mais frequentes e devastadores do que o sino prevê.",
      "Desvio-padrão e 'sigmas' dão falsa segurança em domínios escaláveis.",
      "Em risco financeiro, assuma fat tails por padrão.",
    ],
  },
  {
    "slug": "ch08-robustez-e-barbell",
    "sub": "CAPÍTULO 8: Robustez, Fragilidade e a Estratégia Barbell",
    "intro": "Já que não dá para prever Cisnes Negros, a saída não é prever melhor — é construir robustez. Torne-se imune aos Cisnes Negros negativos (que te quebram) e exposto aos positivos (que te enriquecem). A tática prática é a estratégia barbell, dos halteres.",
    "cards": [
      {"ic":"scale","t":"A Fixação Na Robustez","emph":"Robustez","b":"O corpo frágil escorre no ralo fino rangendo oco frouxo cego quebrado e o sistema robusto sangra os arranhões mas cruza o deserto podre do pior cataclisma negro cego frio em pé firme no chão sujo mudo aguentando sol e chumbo de costas. Desenhe a fortaleza inteira primeiro para <strong>brecar seco o esmagamento mortal bruto pesado gordo afiado no inferno imprevisível cego sem amarras e sem pena da chuva grossa forte amarga antes mesmo de caçar lucros altos na parede estufada limpa fina cega da calçada rica</strong>.","tip":"<strong>Pergunta-chave:</strong> no exato segundo que o meteorito esmagar o teto da praça mole frouxa livre nula cega e plana do mercado inteiro falso e falso e raso, você respira cru limpo frio ou seca?"},
      {"ic":"wrench","t":"A Estratégia Barbell","emph":"Barbell","b":"Ancore quase tudo na blindagem extrema de concreto chato cego duro e burro de segurança maçante nula onde quebra é zero cravado puro e chumbo sujo frio na tumba. E os punhados escassos varra de vez soltos na alavanca pra <strong>explodir rasgando sem medo escancarado de risco brutal insano louco selvagem grosso gordo podre de teto arrombado rico infinito raso de subida quente viva alta rolando a bola solta limpa na cara e dente do capeta rindo oco rico de poeira nula do céu livre solto de asfalto solto falso no fundo escuro mole podre ralo fino mole</strong>.","tip":"<strong>Como aplicar:</strong> desvie seco das águas mornas de risco moderado mudo falso solto mole cego nulo de areia falsa porque esconde armadilhas piores."},
      {"ic":"spark","t":"O Jogo Da Convexidade","emph":"Convexidade","b":"Cace posições em que o impacto brutal afundando cruze uma laje blindada grossa cravada e esbarre sem arrastar sangue na cama forrada chata contada de cimento duro, porém arme tudo de tal forma que <strong>a boca escancarada solta rica da máquina caça-níqueis mastigue teto furado sem freios jorrando a mina preta de ouro grosso em chamas soltas no salão batendo a louça cheia quente de poça de milagre bruto podre gordo no chão afiado do Extremistão rasgado de vento grande subindo o voo alucinado no mercado sujo sem âncora viva morta fraca frouxa lisa sem dor pesada rasa dura de aço nula fria e oca rindo solta da sorte cega gigante preta louca sem fim de teto afundado raso podre frouxo liso e cego do cego de luz limpa clara nula na veia rica cega grossa rasgada gorda do meio forte duro mudo do mundo rasgado falso solto sem asfalto</strong>.","tip":"<strong>Regra:</strong> aposte com um limite de chão bem nítido no osso, mas certifique a rota insana da cabeça subindo foguetes ao céu de cera frouxa."},
    ],
    "lessons_title": "Lições-Chave do Capítulo 8",
    "lessons": [
      "Não preveja Cisnes Negros — torne-se robusto a eles.",
      "Blinde-se contra o Cisne Negro negativo; exponha-se ao positivo.",
      "Barbell: extremo seguro + extremo especulativo, sem meio-termo.",
      "Busque assimetria: perda pequena e limitada, ganho grande e ilimitado.",
    ],
  },
]
