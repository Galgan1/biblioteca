# -*- coding: utf-8 -*-
"""Conteúdo (pt-BR) de 'Sapiens: Uma Breve História da Humanidade' (Yuval Noah Harari)."""

BOOK = {
  "title": "Sapiens",
  "author": "Yuval Noah Harari",
  "header_light": "SAPIENS",
  "header_bold": "UMA BREVE HISTÓRIA",
  "subtitle": "VISÃO GERAL · DE PRIMATA INSIGNIFICANTE A SENHOR DO PLANETA",
  "intro": "Há 100 mil anos, o Homo sapiens era um animal sem importância no meio da savana, mais perto da hiena que do trono. Hoje, manda no planeta e brinca de deus. O que mudou não foi a força, nem o cérebro de um indivíduo: foi a capacidade de inventar histórias — deuses, dinheiro, nações, direitos — e fazer milhões de estranhos acreditarem na mesma ficção. Cooperação em massa em torno de mitos: esta é a arma secreta. Três revoluções escrevem o resto da trama. E a última cena é a mais inquietante: o sapiens prestes a aposentar a seleção natural e desenhar seu próprio sucessor.",
  "description": "Yuval Noah Harari conta a história inteira da nossa espécie sem reverência ao 'progresso'. Três revoluções a movem: a Cognitiva (~70 mil anos) nos deu a ficção; a Agrícola (~12 mil) — 'a maior fraude da história' — multiplicou a espécie e escravizou o indivíduo; a Científica (~500 anos) transformou a ignorância confessada em poder. No meio, dinheiro, império e religião costuram mundos isolados num só. No fim, o capitalismo aposta tudo num futuro maior — e o sapiens, mais poderoso que nunca e nem por isso mais feliz, ensaia trocar a evolução pelo design e virar deus de si mesmo.",
  "tags": ["História", "Antropologia", "Civilização"],
  "progress": "13 Capítulos",
  "cover": "assets/sapiens-cover.png",
  "overview_cards": [
    {"ic":"bulb","t":"Ficção Compartilhada","b":"A superpotência do sapiens não é o polegar nem o cérebro grande: é <strong>contar histórias e fazer milhões acreditarem nelas</strong> — deuses, dinheiro, nações, direitos. Essas ficções criadas e cridas por muitos nos deixam <strong>cooperar com estranhos</strong> sem limite, rompendo o teto de ~150 (número de Dunbar) que prende os outros animais.","tip":"<strong>Modelo mental:</strong> diante de qualquer coisa que mova multidões, pergunte qual é a ficção que a sustenta — e a quem ela serve."},
    {"ic":"layers","t":"As 3 Revoluções","b":"A história inteira cabe em três viradas. <strong>Cognitiva</strong> (~70 mil anos): aprendemos a imaginar o que não existe. <strong>Agrícola</strong> (~12 mil): domesticamos o trigo — ou ele nos domesticou — na 'maior fraude da história'. <strong>Científica</strong> (~500 anos): confessamos a ignorância e o poder humano disparou.","tip":"<strong>Como aplicar:</strong> em toda revolução, separe 'a espécie prosperou' de 'o sujeito comum viveu melhor' — quase nunca é a mesma frase."},
    {"ic":"spiral","t":"Do Natural ao Design","b":"Por 4 bilhões de anos a seleção natural escreveu a vida. Agora, pela primeira vez, uma espécie pega a caneta: <strong>vamos redesenhar a nós mesmos</strong> com bioengenharia, ciborgues e IA. A pergunta sai de 'o que podemos fazer?' e vira a única que importa: <strong>'o que queremos nos tornar?'</strong>.","tip":"<strong>Para refletir:</strong> nunca tivemos tanto poder e tão pouca clareza sobre o que fazer com ele. Deus sem propósito é a definição do perigo.","warn":True},
  ],
}

CHAPTERS = [
  {
    "slug": "ch01-revolucao-cognitiva",
    "sub": "CAPÍTULO 1: A Revolução Cognitiva",
    "intro": "Por que nós, e não os neandertais? Há ~70 mil anos, algo no cérebro do sapiens mudou e nasceu uma linguagem capaz de falar do que jamais existiu — espíritos, leis, futuros imaginários. Foi a fagulha. Com ela vieram as ficções compartilhadas e a cooperação flexível em massa: a única espécie que consegue juntar milhões de estranhos em torno de uma história inventada.",
    "cards": [
      {"ic":"spark","t":"A Árvore do Conhecimento","emph":"Conhecimento","b":"O leão é mais forte, o cavalo é mais rápido, o chimpanzé tem músculos maiores. O sapiens venceu com a língua. <strong>Aprendemos a fofocar sobre quem é confiável e, sobretudo, a falar de coisas que não existem.</strong> Nenhum outro animal jamais convenceu o vizinho a se comportar prometendo recompensa depois da morte.","tip":"<strong>Modelo mental:</strong> fofoca cola dezenas de pessoas; ficção cola milhões. A segunda é que fez a civilização."},
      {"ic":"layers","t":"O Poder da Ficção","emph":"Ficção","b":"Dois chimpanzés desconhecidos jamais farão negócio. <strong>Dois sapiens que nunca se viram fundam uma empresa, lutam pela mesma bandeira ou rezam ao mesmo deus — porque acreditam na mesma ficção.</strong> Deuses, nações e dinheiro não existem fora da nossa cabeça coletiva, e mesmo assim governam o mundo.","tip":"<strong>Como aplicar:</strong> ninguém comanda multidões só com fatos. Comanda com uma história em que valha a pena acreditar."},
      {"ic":"target","t":"A Invasão Fulminante","emph":"Invasão","b":"Não fomos pioneiros gentis. Onde o sapiens chegou, o silêncio veio atrás. <strong>Varremos os neandertais, os denisovanos e metade da megafauna do planeta antes mesmo de inventar a roda.</strong> A maior e mais rápida onda de extinção da história tem nosso nome.","tip":"<strong>Sinal de alerta:</strong> o ecocídio não começou com as fábricas — começou com lanças e fogo, milênios atrás.","warn":True},
    ],
    "lessons_title": "Por Que o Sapiens Venceu",
    "lessons": [
      "A arma decisiva não foi força nem QI individual, foi a imaginação coletiva — contar histórias que muitos creem.",
      "Ficções compartilhadas (deuses, dinheiro, nações) deixam estranhos cooperarem sem se conhecer.",
      "Acima de ~150 pessoas, nenhum grupo se sustenta no olho no olho: precisa de um mito comum.",
      "O que move multidões raramente é a verdade — é a ficção em que se acredita. Poder e verdade quase nunca coincidem.",
    ],
  },
  {
    "slug": "ch02-cacadores-coletores",
    "sub": "CAPÍTULO 2: O Mundo dos Caçadores-Coletores",
    "intro": "Esqueça o homem das cavernas miserável e faminto. Por dezenas de milhares de anos o sapiens viveu de caça e coleta numa 'sociedade da abundância original' — talvez mais saudável, mais variada e com mais tempo livre que o camponês que viria depois. E é a esse mundo, não ao escritório, que o nosso corpo e a nossa mente ainda obedecem.",
    "cards": [
      {"ic":"leaf","t":"A Vida Ancestral","emph":"Vida","b":"Vivemos 99% da nossa história sem cidades, sem patrões, sem trigo. <strong>O cérebro que você carrega para a reunião de hoje foi forjado para fugir de leões e devorar doce sempre que aparecesse, porque o açúcar era raro.</strong> Nossos vícios modernos são instintos antigos sem o cenário antigo.","tip":"<strong>Prática:</strong> a fissura por açúcar, curtidas e status é um software de caçador rodando num mundo que ele não reconhece."},
      {"ic":"scale","t":"A Sociedade Opulenta","emph":"Opulenta","b":"O forrageador trabalhava poucas horas, comia dezenas de espécies e raramente passava fome. <strong>Foi o camponês — não o caçador — quem herdou as jornadas exaustivas, a dieta monótona de cereais e as pragas que vêm de viver grudado em gente e bicho.</strong> A mente do caçador era também uma enciclopédia viva do mundo natural.","tip":"<strong>Para refletir:</strong> cada 'avanço' que veio depois cobrou seu preço no corpo do indivíduo comum."},
    ],
    "lessons_title": "O Mito do Caçador Miserável",
    "lessons": [
      "O caçador-coletor talvez fosse mais saudável, mais bem alimentado e mais folgado que o primeiro agricultor.",
      "Preconceito do progresso: nem toda revolução que engrandece a espécie melhora a vida de quem a vive.",
      "Muito antes das fábricas, o sapiens já era o exterminador-mor: a megafauna sumiu por onde passamos.",
      "Corpo e psique seguem calibrados para a savana — vivemos no século 21 com instintos da Idade da Pedra.",
    ],
  },
  {
    "slug": "ch03-revolucao-agricola",
    "sub": "CAPÍTULO 3: A Revolução Agrícola — A Maior Fraude da História",
    "intro": "Chamamos de Revolução Agrícola o maior salto da humanidade. Harari chama de 'a maior fraude da história'. Há ~12 mil anos começamos a plantar — e a vida do sapiens médio piorou: mais trabalho, comida pior, doenças novas, costas quebradas. A espécie inchou; o indivíduo definhou. E a pergunta que vira tudo de ponta-cabeça: nós domesticamos o trigo, ou o trigo nos domesticou?",
    "cards": [
      {"ic":"layers","t":"A Maior Fraude","emph":"Fraude","b":"A agricultura é um sucesso de evolução e um desastre de bem-estar. <strong>Trocamos a dieta variada do caçador pela papa de trigo, e as horas livres pelo dia inteiro curvado na enxada.</strong> Houve mais gente viva e mais gente infeliz — o ganho da espécie foi pago pelo suor de cada um.","tip":"<strong>Modelo mental:</strong> 'a humanidade progrediu' e 'o sujeito comum viveu melhor' são duas afirmações diferentes — não as confunda."},
      {"ic":"spiral","t":"Quem Domesticou Quem","emph":"Domesticou","b":"O trigo era uma gramínea selvagem qualquer há 10 mil anos. Hoje cobre milhões de quilômetros do globo. <strong>Quem se ajoelhou para arrancar pedras, carregar água e espantar pragas pelo trigo fomos nós.</strong> Pela contabilidade fria do DNA, a planta domou o macaco — e não o contrário.","tip":"<strong>Para refletir:</strong> 'sucesso evolutivo' mede cópias de genes, não felicidade. Os dois podem caminhar em sentidos opostos."},
      {"ic":"key","t":"A Armadilha do Luxo","emph":"Armadilha","b":"Toda conveniência nova vira, em uma geração, necessidade da qual não se abre mão. <strong>O que prometia mais lazer trouxe mais bocas para alimentar e mais trabalho para sustentá-las — sem caminho de volta.</strong> Inventamos a vida fácil e fomos escravizados por ela.","tip":"<strong>Sinal de alerta:</strong> desconfie da tecnologia que jura poupar seu tempo; em pouco tempo é você quem serve a ela.","warn":True},
    ],
    "lessons_title": "A Maior Fraude da História",
    "lessons": [
      "A Revolução Agrícola foi triunfo da espécie e retrocesso do indivíduo médio — mais gente, pior vida.",
      "'Não domesticamos o trigo; o trigo nos domesticou' — virar a lente revela quem serviu a quem.",
      "Armadilha do luxo: todo conforto novo vira necessidade e gera mais trabalho, nunca mais ócio.",
      "Mais comida sustentou mais bocas e prendeu a todos: depois do primeiro campo, não havia retorno.",
    ],
  },
  {
    "slug": "ch04-piramides-escrita-memoria",
    "sub": "CAPÍTULO 4: Pirâmides, Burocracia e Escrita",
    "intro": "O excedente do campo empilhou gente em cidades e reinos — e juntar milhares de estranhos exige um mito poderoso e uma tecnologia improvável. A primeira escrita do mundo não nasceu para cantar deuses nem declarar amor. Nasceu para anotar quantos sacos de cevada cada um devia ao rei. A poesia veio muito depois do imposto.",
    "cards": [
      {"ic":"layers","t":"A Ordem Antes da Pedra","emph":"Ordem","b":"Antes de erguer a pirâmide, o faraó precisou erguer uma crença. <strong>Milhares só arrastam blocos de toneladas se acreditarem que aquele homem é um deus na Terra.</strong> O primeiro tijolo de todo império não é de pedra — é de fé compartilhada.","tip":"<strong>Modelo mental:</strong> por trás de toda obra colossal, procure a história invisível que convenceu as pessoas a carregá-la."},
      {"ic":"book","t":"A Escrita e o Fisco","emph":"Escrita","b":"O cérebro do sapiens é ótimo para reconhecer rostos e péssimo para guardar números. <strong>Quando o império passou a cobrar de milhares de súditos, nenhum tesoureiro deu conta — e veio a escrita, parteira da contabilidade.</strong> Os primeiros textos da humanidade são planilhas de impostos.","tip":"<strong>Prática:</strong> a escrita é a primeira tecnologia a furar o teto biológico da memória humana."},
      {"ic":"cards","t":"A Burocracia","emph":"Burocracia","b":"Para arquivar o mundo, a burocracia teve de recortá-lo em gavetas. <strong>Aprendemos a pensar por categorias, formulários e prateleiras — e a confundir a etiqueta com a coisa.</strong> O arquivo deixou de organizar a realidade e passou a moldá-la.","tip":"<strong>Para refletir:</strong> quando o sistema só enxerga o que cabe na pasta, o que não cabe deixa de existir."},
    ],
    "lessons_title": "O Império de Papel",
    "lessons": [
      "Pirâmides e impérios repousam sobre ordens imaginadas: muitos as sustentam, pouquíssimos as desenham.",
      "A escrita nasceu do fisco, não da arte — sua função inaugural foi contar grãos e impostos.",
      "Escrita e burocracia reprogramam o pensamento em categorias, listas e arquivos.",
      "Toda grande ordem social é um castelo imaginado: de pé enquanto a crença coletiva o sustenta.",
    ],
  },
  {
    "slug": "ch05-ordem-imaginada-hierarquias",
    "sub": "CAPÍTULO 5: A Ordem Imaginada e as Hierarquias",
    "intro": "Nenhuma sociedade grande se segura na honestidade ou no instinto. Ela se segura numa ordem imaginada — um conjunto de regras que só existe porque todos concordam em fingir que existe, mas que sentimos tão real quanto a gravidade. E toda ordem imaginada produz hierarquias que jura serem 'naturais'. Spoiler de Harari: quase nenhuma é.",
    "cards": [
      {"ic":"scale","t":"A Ordem Imaginada","emph":"Ordem Imaginada","b":"Nobres e plebeus, brancos e negros, ricos e pobres: divisões inventadas que parecem leis do cosmos. <strong>A ordem social não está nos seus genes — está na cabeça de milhões que acreditam nela ao mesmo tempo.</strong> É uma ficção poderosa, e quem fica embaixo dela sangra de verdade.","tip":"<strong>Modelo mental:</strong> o 'direito divino do rei' e os 'direitos humanos' brotam da mesma fonte — a imaginação coletiva."},
      {"ic":"eye","t":"Os Três Truques","emph":"Três Truques","b":"A ficção sobrevive porque se disfarça de natureza. <strong>Ela se materializa em muros, prédios e fronteiras; ela molda por dentro o que você deseja; e ela só vive na cabeça de todos ao mesmo tempo.</strong> Por isso não basta um cético — para derrubá-la, é preciso convencer milhões a crer em outra coisa.","tip":"<strong>Como aplicar:</strong> duvidar sozinho não muda o sistema. Ordem imaginada só cai quando a crença coletiva migra."},
      {"ic":"spiral","t":"O Ciclo Vicioso","emph":"Vicioso","b":"Um acaso histórico cria uma lei que exclui um grupo. A exclusão o empobrece. E a pobreza vira a 'prova' de que aquele grupo é mesmo inferior — justificando a próxima lei. <strong>A discriminação fabrica a desigualdade que depois usa como álibi.</strong> A injustiça se alimenta da própria sombra.","tip":"<strong>Sinal de alerta:</strong> quando jurarem que uma hierarquia é 'natural', pergunte sempre quem ganha com essa crença.","warn":True},
    ],
    "lessons_title": "A Hierarquia Que Diz Ser Natureza",
    "lessons": [
      "Toda sociedade em larga escala se apoia numa ordem imaginada que sentimos, equivocadamente, como natural.",
      "Ela se sustenta por 3 truques: encarna no mundo material, molda nossos desejos e é intersubjetiva.",
      "Hierarquias se vendem como 'naturais', mas nascem de acasos e se perpetuam por círculos viciosos.",
      "Igualdade, liberdade e direitos são ficções tão imaginadas quanto as castas — só que ficções melhores.",
    ],
  },
  {
    "slug": "ch06-dinheiro",
    "sub": "CAPÍTULO 6: O Dinheiro",
    "intro": "Cristãos e muçulmanos não concordam sobre Deus. Mas concordam sobre o dólar. O dinheiro é a ficção mais bem-sucedida que o sapiens já inventou — a única crença genuinamente universal, acima de religião, raça e bandeira. Um pedaço de papel ou um número numa tela não valem nada por si. Valem porque você confia que o estranho ali na frente também acredita neles.",
    "cards": [
      {"ic":"key","t":"A Confiança Suprema","emph":"Confiança","b":"A nota na sua carteira é só papel pintado. <strong>Ela vira comida, casa e remédio porque um bilhão de desconhecidos jura, junto com você, que ela vale.</strong> O dinheiro é o sistema de confiança mútua mais eficiente já criado — confiança sem precisar conhecer, gostar ou respeitar ninguém.","tip":"<strong>Modelo mental:</strong> a moeda faz inimigos comerciarem e estranhos cooperarem onde nenhum deus conseguiu."},
      {"ic":"link","t":"O Conversor Universal","emph":"Conversor","b":"O dinheiro traduz qualquer coisa em qualquer coisa. <strong>Terra vira voto, suor vira saúde, lealdade vira preço — tudo passa pelo mesmo câmbio.</strong> É o solvente que dissolveu as fronteiras entre civilizações que nunca tinham se tocado, e as misturou num só mercado.","tip":"<strong>Prática:</strong> o dinheiro não tem moral nem lado — é a tecnologia neutra da conversão total."},
      {"ic":"scale","t":"O Lado Sombrio","emph":"Sombrio","b":"O mesmo solvente que une dissolve o que não tem preço. <strong>Quando tudo vira mercadoria, a vizinhança vira mercado, o favor vira fatura e a comunidade vira clientela.</strong> Ganhamos um mundo que negocia com qualquer um — e perdemos os laços que não cabem numa etiqueta.","tip":"<strong>Para refletir:</strong> o que ganha preço perde o caráter de laço humano que não se compra."},
    ],
    "lessons_title": "A Ficção em Que Todos Creem",
    "lessons": [
      "O dinheiro é a ficção mais universal: a única crença que une cristão, ateu e xamã na mesma mesa.",
      "Seu valor é intersubjetivo — confiança mútua, não ouro nem força física no cofre.",
      "Como conversor e reservatório universal de valor, é o maior unificador da história humana.",
      "O preço da eficiência: ele corrói tudo o que vale precisamente por não ter preço.",
    ],
  },
  {
    "slug": "ch07-imperios",
    "sub": "CAPÍTULO 7: Os Impérios",
    "intro": "'Império' virou xingamento — e nem por isso deixou de ser a forma de governo mais comum e duradoura dos últimos 2.500 anos. Harari faz a provocação desconfortável: o império foi o grande liquidificador da humanidade. Aquela cultura que você chama de 'autêntica', com sua comida, suas leis e sua língua, é quase sempre o caldo deixado por algum conquistador.",
    "cards": [
      {"ic":"layers","t":"O Motor Cultural","emph":"Motor Cultural","b":"O conquistador chega para roubar e, sem querer, funde. <strong>Impõe sua língua, sua lei e seus deuses sobre povos distintos, e do choque nasce uma cultura nova que sobrevive ao próprio império.</strong> A bota do exército é também o pilão que mistura mundos antes isolados.","tip":"<strong>Modelo mental:</strong> impérios são os grandes liquidificadores de idiomas, comidas e crenças do planeta."},
      {"ic":"link","t":"A Herança Imperial","emph":"Herança","b":"O colonizado acaba exigindo justiça nas palavras do colonizador. <strong>Direitos, nações e ideais iluministas viajaram nos mesmos navios que traziam grilhões — e hoje são empunhados contra quem os trouxe.</strong> Não existe volta a uma pureza anterior: ela nunca existiu.","tip":"<strong>Para refletir:</strong> a cultura que herdamos é mestiça por nascimento — filha do conquistador e do conquistado."},
      {"ic":"target","t":"Visão Universalista","emph":"Universalista","b":"Quase todo império se contou uma bela história: levo paz, lei e ciência aos 'bárbaros'. <strong>A retórica do bem universal foi sempre a maquiagem do saque — e, ainda assim, deixou estradas, hospitais e ideias que duraram mais que os tronos.</strong> O saldo é a um tempo sangue e legado.","tip":"<strong>Sinal de alerta:</strong> 'estou aqui para civilizar você' é o disfarce favorito de quem veio pegar o que é seu.","warn":True},
    ],
    "lessons_title": "O Grande Liquidificador",
    "lessons": [
      "O império foi a forma política mais comum e estável da história — e o maior motor de fusão cultural.",
      "Quase toda cultura 'autêntica' de hoje é, em boa parte, herança imperial sincrética.",
      "Até quem combate o império o faz com suas ideias e ferramentas: não há retorno a uma pureza original.",
      "O império é contradição viva: opressão concreta e fábrica de ideais universais ao mesmo tempo.",
    ],
  },
  {
    "slug": "ch08-religioes",
    "sub": "CAPÍTULO 8: As Religiões",
    "intro": "Harari faz uma pergunta que incomoda os dois lados: e se religião não for sobre deuses? Para ele, religião é qualquer sistema de valores fundado numa ordem sobre-humana tida como absoluta e inquestionável. Pela definição, cristianismo e islã entram — mas também o liberalismo, o comunismo, o nacionalismo e o humanismo. Todos têm seus dogmas, seus santos e seus hereges.",
    "cards": [
      {"ic":"mountain","t":"Ordem Sobre-Humana","emph":"Sobre-Humana","b":"Lei feita só por homens, homens podem mudar amanhã. <strong>Por isso o rei amarrou suas regras a um deus: 'não é minha vontade, é a do Céu — quem desobedece, arde'.</strong> Apoiada numa ordem acima dos humanos, a lei vira inquestionável e o império, estável.","tip":"<strong>Modelo mental:</strong> toda ordem que se diz absoluta busca uma âncora fora do alcance da discussão humana."},
      {"ic":"wave","t":"O Rolo Compressor","emph":"Rolo Compressor","b":"As religiões universais não pedem licença na fronteira. <strong>Carregando uma verdade que se julga válida para todos, o missionário atravessa o mundo e dissolve mil cultos locais numa só fé planetária.</strong> Foi assim que tribos isoladas viraram civilizações conectadas.","tip":"<strong>Como aplicar:</strong> o que expande sem freio é a convicção de possuir a verdade que o resto do mundo precisa ouvir."},
      {"ic":"person","t":"As Religiões Modernas","emph":"Religiões","b":"O altar não fechou — só trocou de santo. <strong>O comunismo tem suas escrituras, o liberalismo seus mártires, o nacionalismo seus rituais; todos exigem sacrifício e punem a heresia.</strong> Trocamos o deus do céu pelo Mercado, pela Nação e pela Humanidade — mas continuamos crendo e obedecendo.","tip":"<strong>Para refletir:</strong> aplique a uma ideologia secular o mesmo ceticismo que você aplicaria a uma seita antiga."},
    ],
    "lessons_title": "A Terceira Grande Ficção",
    "lessons": [
      "Religião = sistema de valores ancorado numa ordem sobre-humana absoluta — definição funcional, não teológica.",
      "É a terceira ordem unificadora: empresta ao dinheiro e ao império uma legitimidade que vem 'de cima'.",
      "Religiões universais e missionárias unem ao se declararem verdadeiras para toda a humanidade.",
      "Liberalismo, comunismo, nacionalismo e humanismo também operam como religiões — só que sem deuses.",
    ],
  },
  {
    "slug": "ch09-revolucao-cientifica",
    "sub": "CAPÍTULO 9: A Revolução Científica — A Descoberta da Ignorância",
    "intro": "Como, em apenas 500 anos, o sapiens saiu de barcos a vela para a Lua? O estopim não foi um gênio nem uma máquina — foi uma frase de duas palavras: 'não sei'. A Revolução Científica começa quando a humanidade troca a certeza confortável das tradições — que diziam ter todas as respostas — pela descoberta inquietante da própria ignorância.",
    "cards": [
      {"ic":"lens","t":"O Salto da Dúvida","emph":"Dúvida","b":"Por milênios, sábios consultavam livros antigos certos de que tudo o que importa já fora revelado. <strong>O salto veio quando passamos a desenhar o mapa com manchas brancas e escrever 'aqui não sabemos — vamos descobrir'.</strong> O dogma diz 'a resposta está no passado'; a ciência diz 'a resposta está adiante, e ainda não a temos'.","tip":"<strong>Modelo mental:</strong> o conhecimento dispara no instante em que 'eu não sei' deixa de ser vergonha e vira ponto de partida."},
      {"ic":"target","t":"Os Três Pilares","emph":"Três Pilares","b":"Confessar a ignorância foi só o começo. <strong>A ciência exigiu mais: observar a natureza e traduzi-la em matemática, e depois cobrar resultado — teoria que não vira poder fica na gaveta.</strong> Medir e aplicar transformaram a curiosidade em força bruta sobre o mundo.","tip":"<strong>Prática:</strong> hipótese bonita que não vira resultado serve ao poeta; o engenheiro quer a que faz a ponte ficar de pé."},
      {"ic":"spark","t":"A Forja do Poder","emph":"Poder","b":"A ciência moderna raramente busca a verdade pela verdade. <strong>Ela busca poder — remédios, canhões, motores — e por isso quem paga a pesquisa é quem quer mais lucro, mais terras ou mais armas.</strong> O telescópio e o canhão saíram da mesma oficina, e juntos puseram o Ocidente no topo.","tip":"<strong>Sinal de alerta:</strong> pergunte sempre quem financia a descoberta — o cheque revela que poder ela serve.","warn":True},
    ],
    "lessons_title": "A Descoberta da Ignorância",
    "lessons": [
      "A Revolução Científica é, na raiz, a descoberta da ignorância: trocar o saber fechado pela dúvida que produz.",
      "Três pilares a sustentam: confessar a ignorância, observar e medir (matemática), buscar novos poderes.",
      "Ciência e tecnologia se casam — o lema da era é 'saber é poder', não 'saber é verdade'.",
      "Aqui nasce a fé no progresso ilimitado, que reorganiza economia, política e imaginação do sapiens.",
    ],
  },
  {
    "slug": "ch10-ciencia-imperio-capital",
    "sub": "CAPÍTULO 10: O Casamento Ciência-Império-Capital",
    "intro": "Em 1500, a Europa era um beco atrasado do mundo: a China e o mundo islâmico eram mais ricos e mais avançados. Trezentos anos depois, um punhado de potências europeias mandava no planeta. Por quê? Não pela tecnologia inicial — outros a tinham —, mas por uma mentalidade e uma aliança inéditas. Ciência, império e capital se acasalaram e geraram um motor que se acelerava sozinho.",
    "cards": [
      {"ic":"link","t":"O Triângulo de Ouro","emph":"Triângulo","b":"A conquista do mundo precisou de três cúmplices. <strong>O soldado abre a rota, o cientista diz onde fica o caminho e o banqueiro paga a conta dos dois — e cobra os juros.</strong> Sozinho, cada um fracassa; juntos, repartem o mapa. Não há descoberta inocente: alguém sempre financia, e financia esperando retorno.","tip":"<strong>Modelo mental:</strong> por trás de toda 'pura' descoberta, pergunte quem pagou — e o que essa pessoa queria de volta."},
      {"ic":"lens","t":"A Busca pelo Vazio","emph":"Vazio","b":"O navegador europeu não largou a vela por ter melhores armas — largou por não suportar o espaço em branco no mapa. <strong>Enquanto chineses e otomanos, já satisfeitos, ficavam em casa, o europeu cruzava oceanos sem saber o que havia do outro lado.</strong> A fome do desconhecido valeu mais que o estoque de quem já era rico.","tip":"<strong>Para refletir:</strong> a curiosidade agressiva cria impérios; o comodismo do mais rico os entrega de bandeja."},
      {"ic":"target","t":"A Fatura Sangrenta","emph":"Sangrenta","b":"Os mesmos navios que levavam botânicos e astrônomos traziam, no porão de baixo, gente acorrentada. <strong>O conhecimento que admiramos foi colhido sobre genocídios nas Américas e o tráfico de milhões de africanos.</strong> O saber ocidental não nasceu limpo — nasceu com sangue seco nas páginas.","tip":"<strong>Sinal de alerta:</strong> nenhum salto colossal chega imaculado; a glória de uns quase sempre é paga pela ruína de outros.","warn":True},
    ],
    "lessons_title": "Por Que a Europa Venceu",
    "lessons": [
      "A dominação europeia veio da mentalidade — não de uma superioridade inicial de riqueza ou tecnologia.",
      "Ciência, império e capital formaram um motor de retroalimentação que se autoacelerou.",
      "Cada vértice nutria o seguinte: conhecer → conquistar → lucrar → financiar mais conhecimento.",
      "A fome de explorar o desconhecido valeu mais que o cofre cheio de quem já estava no topo.",
    ],
  },
  {
    "slug": "ch11-capitalismo-credito",
    "sub": "CAPÍTULO 11: O Credo Capitalista — Crédito e o Futuro",
    "intro": "Por trás dos números frios, o capitalismo é uma religião — e seu artigo de fé é o futuro. Acredita-se que o bolo econômico vai crescer para sempre. Dessa crença nasce o crédito: dinheiro que ainda não existe, emprestado contra uma riqueza que ainda não foi produzida. O presente inteiro foi reconstruído sobre a aposta de que o amanhã será maior.",
    "cards": [
      {"ic":"spiral","t":"A Moeda do Futuro","emph":"Futuro","b":"Antes, só se gastava o que já se tinha. <strong>O crédito inverteu a flecha do tempo: pegamos a riqueza de amanhã para construir a estrada de hoje, na fé de que ela se pagará sozinha lá na frente.</strong> É uma profecia que se cumpre — desde que todos continuem acreditando nela.","tip":"<strong>Modelo mental:</strong> o sistema financeiro inteiro repousa numa única promessa psicológica: a de que o futuro será maior."},
      {"ic":"steps","t":"O Vício do Crescimento","emph":"Crescimento","b":"O segredo de Adam Smith: o lucro do rico, reinvestido, gera o trabalho de todos. <strong>Por isso o capitalista não guarda o ganho no cofre — joga de volta na produção, e precisa crescer todo ano só para não desabar.</strong> Acumular virou pecado; reinvestir, virou mandamento. Parar é morrer.","tip":"<strong>Como aplicar:</strong> no credo capitalista, a virtude não é poupar o tesouro — é fazê-lo render sem nunca parar."},
      {"ic":"target","t":"A Cegueira Ética","emph":"Ética","b":"O crescimento eterno tem uma conta que não aparece no balanço. <strong>Florestas, rios e o clima são consumidos como se fossem grátis, porque o estrago não entra na planilha — vira 'externalidade'.</strong> O lucro de hoje é cobrado, com juros, das gerações que nascerão para pagar a fatura.","tip":"<strong>Sinal de alerta:</strong> quando só o saldo bancário conta, o veneno do presente é empurrado para quem ainda não nasceu.","warn":True},
    ],
    "lessons_title": "A Religião do Crescimento",
    "lessons": [
      "O capitalismo é, no fundo, uma fé no futuro: a crença de que a economia pode crescer sem teto.",
      "O crédito é essa fé encarnada — dinheiro emprestado contra uma riqueza que ainda não existe.",
      "Seu mandamento central: reinvestir o lucro na produção, em vez de consumi-lo ou entesourá-lo.",
      "O imperativo de crescer sempre traz prosperidade e crises — e empurra a conta para fora do papel.",
    ],
  },
  {
    "slug": "ch12-felicidade",
    "sub": "CAPÍTULO 12: E Eles Viveram Felizes? — A (In)felicidade do Sapiens",
    "intro": "A história adora contar quanto poder, terra e riqueza acumulamos. Quase nunca pergunta a única coisa que importa para quem vive: o sapiens ficou mais feliz? A resposta provável e desconcertante é não — pelo menos não na proporção do nosso poder. Triplicamos o conforto e mantivemos a mesma angústia. Três lentes ajudam a entender o paradoxo.",
    "cards": [
      {"ic":"wave","t":"O Ajuste Químico","emph":"Químico","b":"A alegria do carro novo evapora em semanas, e você está de novo no mesmo lugar — querendo mais. <strong>A evolução te prendeu numa esteira: o prazer é só uma isca para te fazer correr, e some assim que você alcança a presa.</strong> Felicidade permanente seria péssima para a sobrevivência, então a biologia não deixa você tê-la.","tip":"<strong>Modelo mental:</strong> nenhuma conquista te eleva de patamar; a química te puxa de volta ao mesmo termostato interno."},
      {"ic":"scale","t":"O Abismo da Expectativa","emph":"Expectativa","b":"Felicidade não é o que você tem — é o que você tem dividido pelo que esperava ter. <strong>O camponês medieval dormia feliz com pão e abrigo; o executivo de hoje praguejará por uma conexão de internet lenta.</strong> Cada conforto novo eleva a régua, e a régua sempre corre na frente da vida.","tip":"<strong>Prática:</strong> domar as próprias expectativas rende mais paz do que multiplicar o que se possui."},
      {"ic":"bulb","t":"O Fim do Desejo","emph":"Desejo","b":"E se a raiz do sofrimento não for ter pouco, mas querer? <strong>O budismo aponta para fora da esteira: a paz não vem de saciar o anseio — vem de largá-lo.</strong> Quem persegue cada sensação agradável e foge de cada desagradável vive correndo; quem para de correr atrás, descansa.","tip":"<strong>Para refletir:</strong> a paz verdadeira mora em soltar o anseio por mais, não em empilhar mais um troféu."},
    ],
    "lessons_title": "E Eles Viveram Felizes?",
    "lessons": [
      "Mais poder não trouxe mais felicidade na mesma medida: progresso e bem-estar interior não andam juntos.",
      "A felicidade tem teto bioquímico (esteira hedônica): conquistas dão picos passageiros, não patamares.",
      "Felicidade ≈ realidade ÷ expectativas — e cada conforto novo infla a expectativa que corrói o bem-estar.",
      "Sentido — e, na lente budista, abandonar o anseio — pesa mais que acumular prazeres que evaporam.",
    ],
  },
  {
    "slug": "ch13-fim-do-homo-sapiens",
    "sub": "CAPÍTULO 13: O Fim do Homo Sapiens",
    "intro": "Por 4 bilhões de anos, uma só lei reinou sobre toda a vida: a seleção natural. Agora, pela primeira vez, uma de suas criaturas está prestes a tomar a caneta de suas mãos. Com bioengenharia, ciborgues e inteligência artificial, o sapiens pode redesenhar a si mesmo — e, ao fazê-lo, projetar a espécie que virá depois de nós. O último capítulo da nossa história talvez seja o primeiro de outra.",
    "cards": [
      {"ic":"spiral","t":"O Salto Ciborgue","emph":"Ciborgue","b":"A seleção natural está prestes a ser substituída pelo design inteligente. <strong>Com tesouras genéticas e implantes, deixamos de ser produto da evolução e passamos a ser seu engenheiro — escolhendo a inteligência, a memória, a aparência dos nossos filhos.</strong> O macaco que aprendeu a falar agora aprende a se reprojetar.","tip":"<strong>Modelo mental:</strong> assumir o controle da própria biologia é uma porta de mão única — não há como voltar a ser apenas natureza."},
      {"ic":"layers","t":"Mentes Imortais","emph":"Imortais","b":"Funda-se o circuito de silício à célula viva, e a mente começa a vazar para fora do crânio. <strong>Um pensamento que pode trocar de suporte talvez não precise morrer quando o corpo falhar.</strong> A morte, que sempre foi o muro intransponível, vira para a tecno-ciência apenas mais um problema de engenharia a resolver.","tip":"<strong>Como aplicar:</strong> leis, ética e mercados foram todos desenhados em torno da morte e da carne — e nenhum resistirá intacto à sua queda."},
      {"ic":"fork","t":"Deuses Confusos","emph":"Confusos","b":"Eis o retrato com que Harari fecha o livro: estamos virando deuses sem nunca termos amadurecido. <strong>Ganhamos o poder de criar e destruir vida, mas seguimos guiados pelos mesmos medos, vaidades e ânsias do animal que fomos na savana.</strong> Poder de divindade na mão de quem nem sabe o que quer.","tip":"<strong>Sinal de alerta:</strong> 'Existe algo mais perigoso que deuses insatisfeitos e irresponsáveis, que não sabem o que querem?'","warn":True},
    ],
    "lessons_title": "O Fim do Homo Sapiens?",
    "lessons": [
      "O sapiens está trocando a seleção natural pelo design inteligente — encerrando uma era de bilhões de anos.",
      "Três caminhos podem nos superar e nos suceder: bioengenharia, ciborgues e vida inorgânica (IA).",
      "A pergunta crucial mudou de 'o que podemos fazer?' para 'o que queremos nos tornar?'.",
      "O maior risco é o poder de deus sem a sabedoria de deus: 'deuses insatisfeitos e irresponsáveis'.",
    ],
  },
]
