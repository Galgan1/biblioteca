# -*- coding: utf-8 -*-
"""Conteúdo (pt-BR) das páginas da biblioteca para 'A História do Futebol Brasileiro'.
Entrada TEMÁTICA inspirada no melhor livro do assunto — Mário Filho, 'O Negro no Futebol
Brasileiro' (1947, pref. Gilberto Freyre) — enriquecida com Alex Bellos ('Futebol: The
Brazilian Way of Life') e Eduardo Galeano ('Futebol ao Sol e à Sombra'), e com fatos
verificados (Charles Miller 1894; Friedenreich 1919; Vasco 1923; profissionalização 1933;
Leônidas 1938; Maracanazo 1950; tri 58/62/70; 1982; tetra 94; penta 02; 7x1 em 2014).
Base: síntese atribuída + fatos checados — não reproduz o texto das obras."""

BOOK = {
 "title": "A História do Futebol Brasileiro",
 "author": "Mário Filho e clássicos do tema",
 "header_light": "A HISTÓRIA DO",
 "header_bold": "FUTEBOL BRASILEIRO",
 "subtitle": "VISÃO GERAL · COMO UM ESPORTE DE ELITE VIROU A ALMA DO BRASIL",
 "intro": "O futebol chegou ao Brasil em 1894 como passatempo de uma elite branca e europeizada — e virou a coisa mais brasileira que existe. O clássico de Mário Filho, 'O Negro no Futebol Brasileiro', conta como: foi quando o negro, o mulato e o pobre furaram a barreira e venceram que o jogo deixou de ser cópia e ganhou ginga, drible e alma. Desse encontro nasceram o futebol-arte, a glória do tri de Pelé e os traumas do Maracanazo e do 7 a 1. A história do futebol brasileiro é o próprio Brasil aprendendo a se olhar no espelho.",
 "description": "A história do futebol brasileiro, da origem aristocrática (Charles Miller, 1894) à era das cinco estrelas — inspirada no maior clássico do tema, 'O Negro no Futebol Brasileiro' de Mário Filho. A barreira racial e o 'pó de arroz', a ruptura do Vasco (1923), Friedenreich e Leônidas, a profissionalização (1933), a invenção do futebol-arte, o Maracanazo (1950) e o 'complexo de vira-lata', o tri de Pelé e Garrincha (1958/62/70), a beleza que perdeu em 1982, o tetra e o penta (1994/2002), o 7 a 1 de 2014 e o debate sobre o mito da democracia racial.",
 "tags": ["História", "Futebol", "Brasil", "Cultura"],
 "progress": "10 Capítulos Completos",
 "cover": "assets/futebol-brasileiro-cover.png",
 "overview_cards": [
   {"ic":"fork","t":"De Esporte de Elite a Paixão Nacional","b":"O futebol entrou pela porta da aristocracia (clubes brancos, ingleses de imitação) e só virou <strong>brasileiro</strong> quando o talento popular — negro, mulato, operário — invadiu o campo e <strong>venceu</strong>. Mário Filho narra essa virada como o ato de fundação do nosso futebol.","tip":"<strong>Chave de leitura:</strong> o jogo brasileiro nasceu do encontro racial — não apesar dele.","wide":True},
   {"ic":"spark","t":"A Invenção do Futebol-Arte","b":"Da técnica importada somada ao repertório popular (a malandragem, a capoeira, o samba no corpo) nasce a <strong>ginga</strong>: drible, finta, improviso. Galeano chama de futebol-arte — beleza como fim, não só a vitória como meio.","tip":"<strong>Assinatura:</strong> é o estilo que o mundo inteiro passou a reconhecer como 'brasileiro'."},
   {"ic":"wave","t":"Glória e Trauma, o Espelho do País","b":"O Maracanazo (1950) e o 7 a 1 (2014) são feridas nacionais; o tri de Pelé (1958/62/70) e o penta (2002) são auges. O futebol é onde o Brasil <strong>se vê inteiro</strong>.","tip":"<strong>Modelo mental:</strong> não é fuga da realidade brasileira — é a sua forma mais concentrada."},
 ],
}

CHAPTERS = [
 {"slug":"ch01-origem-aristocratica","sub":"CAPÍTULO 1: A Origem Aristocrática (1894)",
  "intro":"O futebol não nasceu popular no Brasil. Charles Miller voltou da Inglaterra em 1894 com duas bolas e um livro de regras e o apresentou a uma elite branca e abastada. Por décadas, foi marca de distinção social — clube fechado, não paixão de rua.",
  "cards":[
   {"ic":"flag","t":"Charles Miller Traz o Jogo","b":"Filho de pai escocês e mãe brasileira, <strong>Charles Miller</strong> voltou a São Paulo em <strong>1894</strong> com duas bolas, chuteiras, bomba de ar e um livro de regras. Organizou a <strong>primeira partida oficial</strong> do país em 14 de abril de 1895, na Várzea do Carmo.","tip":"<strong>Marco:</strong> o futebol entra pelo trilho inglês — funcionários da São Paulo Railway e do gás.","wide":True},
   {"ic":"mask","t":"Esporte de Distinção","b":"Nos primeiros anos o futebol 'oficial' é <strong>amador, branco e de elite</strong>. Jogar era exibir status — pertencer a um clube de sócios ricos, vestir-se 'à inglesa'. O povo jogava nas várzeas, fora das ligas.","tip":"<strong>Cuidado com o mito:</strong> a paixão nacional não é a origem — é a conquista que veio depois."},
   {"ic":"key","t":"O Amadorismo como Filtro","b":"Exigir que ninguém recebesse para jogar era, na prática, um <strong>filtro de classe</strong>: só jogava quem podia se dar ao luxo de não ser pago. O muro do amadorismo guardava o jogo para os ricos.","tip":"<strong>Antecipe o conflito:</strong> derrubar esse muro será o motor de toda a história seguinte.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 1",
  "lessons":["O futebol chegou ao Brasil em 1894, importado por uma elite branca.","No começo era marca de distinção social, não paixão popular.","O amadorismo funcionava como filtro de classe — e seria o muro a cair."]},

 {"slug":"ch02-barreira-racial","sub":"CAPÍTULO 2: A Barreira Racial e o 'Pó de Arroz'",
  "intro":"Para entrar no futebol de elite, o jogador de pele escura precisava parecer branco. A lenda do 'pó de arroz' resume a época: a inclusão existia, mas sob a condição do embranquecimento. É o conflito central que Mário Filho narra.",
  "cards":[
   {"ic":"mask","t":"O 'Pó de Arroz'","b":"Conta a lenda que o mulato <strong>Carlos Alberto</strong>, do Fluminense, <strong>empoava o rosto</strong> para clarear a pele e ser aceito — daí o apelido 'pó de arroz' da torcida tricolor. O corpo do jogador virou o palco do preconceito.","tip":"<strong>Símbolo:</strong> para ser tolerado, o talento negro tinha de se disfarçar de branco.","wide":True},
   {"ic":"gap","t":"Dois Futebóis Paralelos","b":"De um lado, as <strong>ligas de elite</strong> (brancas, amadoras); de outro, o <strong>futebol de várzea</strong>, onde negros e operários jogavam com craque de sobra, longe dos holofotes oficiais.","tip":"<strong>Tensão:</strong> o talento estava do lado de fora — pressionando para entrar."},
   {"ic":"lens","t":"A Tese de Mário Filho","b":"Para o autor, a história do nosso futebol <strong>é</strong> a história dessa barreira sendo furada. O jogo só vira brasileiro quando o excluído entra — e ganha.","tip":"<strong>Atribua sempre:</strong> 'segundo Mário Filho' — é a tese do livro, não um fato neutro.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 2",
  "lessons":["A inclusão inicial vinha com a condição do embranquecimento ('pó de arroz').","Havia dois futebóis: o de elite (oficial) e o de várzea (popular).","Para Mário Filho, furar essa barreira é o ato fundador do futebol brasileiro."]},

 {"slug":"ch03-ruptura-vasco","sub":"CAPÍTULO 3: A Ruptura — o Vasco da Gama (1923)",
  "intro":"Em 1923 o Vasco escalou negros, mulatos e operários e foi campeão carioca logo na estreia na primeira divisão. A elite reagiu com regras feitas para barrar o jogador pobre — e o Vasco resistiu. O talento popular furou o muro e não voltou atrás.",
  "cards":[
   {"ic":"mountain","t":"O Título de 1923","b":"Sustentado pela colônia portuguesa, o <strong>Vasco</strong> montou um time de <strong>negros, mulatos e trabalhadores</strong> e venceu o Campeonato Carioca de 1923 na primeira tentativa. A prova em campo de que o talento não tinha cor nem classe.","tip":"<strong>Virada:</strong> pela primeira vez, o excluído ganha dentro do sistema oficial.","wide":True},
   {"ic":"sword","t":"A Reação da Elite (AMEA)","b":"Os clubes de elite criaram uma liga separada com exigências — comprovante de <strong>emprego</strong>, prova de <strong>alfabetização</strong> — desenhadas para excluir o jogador pobre e negro disfarçando o preconceito de 'critério'.","tip":"<strong>Reconheça o padrão:</strong> a regra 'neutra' como instrumento de exclusão.","warn":True},
   {"ic":"key","t":"A Resistência","b":"O Vasco se recusou a dispensar seus jogadores. A pressão pela inclusão tornou-se <strong>irreversível</strong> — o futebol brasileiro já tinha mudado de dono.","tip":"<strong>Lição:</strong> conquistas sociais avançam quando alguém se recusa a recuar."},
  ],
  "lessons_title":"Lições-Chave do Capítulo 3",
  "lessons":["O Vasco foi campeão de 1923 com um time de negros, mulatos e operários.","A elite reagiu com regras 'neutras' criadas para excluir o jogador pobre.","A resistência do Vasco tornou a inclusão irreversível."]},

 {"slug":"ch04-friedenreich","sub":"CAPÍTULO 4: Friedenreich, o Primeiro Craque Mestiço",
  "intro":"Antes de Pelé, houve Friedenreich. Filho de pai alemão e mãe negra, 'El Tigre' foi o maior craque do Brasil das primeiras décadas — e carregava no próprio corpo a contradição racial do país.",
  "cards":[
   {"ic":"spark","t":"O Gol de 1919","b":"<strong>Arthur Friedenreich</strong> marcou o gol do título sul-americano de <strong>1919</strong> sobre o Uruguai. Considerado o <strong>maior craque brasileiro antes da era Pelé</strong>, foi o primeiro ídolo a unir técnica de elite e origem popular.","tip":"<strong>Pioneiro:</strong> a ponte entre o futebol importado e o futebol-arte por vir.","wide":True},
   {"ic":"mask","t":"O Corpo do Conflito","b":"Mulato de olhos verdes, <strong>alisava o cabelo</strong> no vestiário antes de entrar em campo. O maior ídolo do país encarnava a mesma tensão racial que a sociedade tentava esconder.","tip":"<strong>Leitura:</strong> o ídolo não escapa do preconceito — ele o carrega à vista de todos.","warn":True},
   {"ic":"constellation","t":"A Semente do Estilo","b":"Em Friedenreich já aparece o <strong>drible</strong> como linguagem — o gosto pela jogada de efeito que, décadas depois, definiria o Brasil no mundo.","tip":"<strong>Continuidade:</strong> de Fried a Garrincha e Pelé, a mesma assinatura."},
  ],
  "lessons_title":"Lições-Chave do Capítulo 4",
  "lessons":["Friedenreich foi o maior craque brasileiro antes de Pelé (gol do título de 1919).","Mestiço, encarnava a contradição racial do país dentro do próprio ídolo.","Nele já nasce o drible como assinatura do futebol brasileiro."]},

 {"slug":"ch05-profissionalizacao","sub":"CAPÍTULO 5: A Profissionalização (1933) e Leônidas (1938)",
  "intro":"Em 1933 o futebol brasileiro se tornou profissional — pagar para jogar derrubou o último muro do amadorismo de elite. Agora o talento podia vir de qualquer lugar. E veio: Leônidas, o Diamante Negro, brilhou na Copa de 1938.",
  "cards":[
   {"ic":"key","t":"O Fim do Amadorismo","b":"A <strong>profissionalização de 1933</strong> derrubou o filtro de classe: quem joga, recebe. O acesso ao futebol de ponta se <strong>democratiza</strong>, e a era dos grandes craques populares começa.","tip":"<strong>Marco:</strong> o talento, não a origem, passa a decidir quem joga.","wide":True},
   {"ic":"spark","t":"Leônidas, o Diamante Negro","b":"Associado à <strong>bicicleta</strong>, <strong>Leônidas da Silva</strong> foi artilheiro da <strong>Copa de 1938</strong> (França), onde o Brasil ficou em 3º. Primeiro ídolo negro de massa do país.","tip":"<strong>Prova mundial:</strong> em campo internacional, o futebol brasileiro mostra voz própria."},
   {"ic":"steps","t":"Talento Popular no Topo","b":"Com o muro derrubado, o repertório das várzeas chega à seleção. O futebol deixa de imitar a Europa e começa a <strong>inventar a si mesmo</strong>.","tip":"<strong>Transição:</strong> daqui ao futebol-arte é um passo."},
  ],
  "lessons_title":"Lições-Chave do Capítulo 5",
  "lessons":["Em 1933 o futebol vira profissional e o acesso se democratiza.","Leônidas, o Diamante Negro, foi artilheiro da Copa de 1938.","O talento popular chega ao topo e o Brasil começa a criar estilo próprio."]},

 {"slug":"ch06-futebol-arte","sub":"CAPÍTULO 6: O Futebol-Arte — a Ginga",
  "intro":"Do encontro entre a técnica importada e o corpo popular — a malandragem, a capoeira, o samba — nasce o estilo brasileiro: drible curto, finta, improviso. Galeano o chama de futebol-arte: a beleza como fim, não só a vitória como meio.",
  "cards":[
   {"ic":"spark","t":"A Ginga","b":"O traço brasileiro: <strong>drible, finta e improviso</strong>, um jeito de jogar que herda o gingado da capoeira e o suingue do samba. Não é só eficiência — é <strong>expressão</strong>.","tip":"<strong>Identidade:</strong> o mundo aprende a reconhecer o 'jogo brasileiro' pela ginga.","wide":True},
   {"ic":"leaf","t":"Beleza como Fim","b":"Para Galeano, o <strong>futebol-arte</strong> se opõe ao futebol-resultado: jogar bonito tem valor próprio, mesmo quando não vence. A torcida brasileira ama o gol de placa tanto quanto a taça.","tip":"<strong>Valor cultural:</strong> a estética do jogo vira patrimônio nacional."},
   {"ic":"link","t":"Mestiçagem em Campo","b":"O estilo é <strong>mestiço</strong> por definição — soma de heranças africanas, europeias e indígenas traduzidas em movimento. Gilberto Freyre leu nisso a 'cara' do Brasil.","tip":"<strong>Atribua:</strong> a leitura 'dionisíaca/mestiça' é de Freyre — fundadora e hoje debatida."},
  ],
  "lessons_title":"Lições-Chave do Capítulo 6",
  "lessons":["A ginga (drible, finta, improviso) é a assinatura do futebol brasileiro.","Para Galeano, o futebol-arte valoriza a beleza, não só o resultado.","O estilo é mestiço — Freyre o leu como expressão da própria identidade nacional."]},

 {"slug":"ch07-maracanazo","sub":"CAPÍTULO 7: O Maracanazo (1950) e o 'Complexo de Vira-Lata'",
  "intro":"Sede da Copa, favorito, em casa, o Brasil só precisava de um empate na decisão. Perdeu para o Uruguai por 2 a 1 no Maracanã lotado. O trauma foi tão fundo que Nelson Rodrigues batizou a ferida nacional: o complexo de vira-lata.",
  "cards":[
   {"ic":"wave","t":"A Tragédia de 1950","b":"Diante de quase 200 mil pessoas, o Brasil saiu na frente e <strong>perdeu de virada para o Uruguai, 2 a 1</strong>, o <strong>Maracanazo</strong>. O silêncio do estádio virou símbolo de uma nação em choque.","tip":"<strong>Trauma fundador:</strong> a derrota em casa marca o futebol brasileiro para sempre.","wide":True},
   {"ic":"mask","t":"O Complexo de Vira-Lata","b":"<strong>Nelson Rodrigues</strong> cunhou a expressão: o brasileiro que se sente <strong>inferior</strong> diante do resto do mundo. A ferida de 1950 virou diagnóstico de um país.","tip":"<strong>Atribua:</strong> 'complexo de vira-lata' é de Nelson Rodrigues, após 1950."},
   {"ic":"spark","t":"A Ferida como Combustível","b":"O trauma não paralisou — virou <strong>fome de redenção</strong>. A dor de 1950 prepara o terreno para a explosão de 1958.","tip":"<strong>Arco:</strong> toda grande redenção começa numa grande queda."},
  ],
  "lessons_title":"Lições-Chave do Capítulo 7",
  "lessons":["Em 1950 o Brasil perdeu o título em casa para o Uruguai (2 a 1), o Maracanazo.","Nelson Rodrigues batizou o trauma de 'complexo de vira-lata'.","A ferida virou combustível para a redenção de 1958."]},

 {"slug":"ch08-tri-pele","sub":"CAPÍTULO 8: A Glória — 1958, 1962, 1970",
  "intro":"O vira-lata virou campeão do mundo. Em três Copas, o Brasil conquistou o tricampeonato com Pelé e Garrincha e coroou, em 1970, um dos melhores times de todos os tempos. O 'país do futebol' nasce aqui.",
  "cards":[
   {"ic":"mountain","t":"1958 e 1962 — o Bi","b":"<strong>1958 (Suécia):</strong> primeiro título, 5 a 2 na final sobre os donos da casa; surge <strong>Pelé</strong>, aos 17 anos, ao lado de <strong>Garrincha</strong>. <strong>1962 (Chile):</strong> bicampeão, 3 a 1 na final; com Pelé lesionado, Garrincha carrega o time.","tip":"<strong>Redenção:</strong> oito anos depois do Maracanazo, o Brasil é campeão do mundo.","wide":True},
   {"ic":"spark","t":"1970 — o Time Perfeito","b":"<strong>Tricampeão</strong> no México, 4 a 1 sobre a Itália, campanha perfeita. <strong>Pelé, Tostão, Gérson, Jairzinho, Rivelino e Carlos Alberto</strong> — o gol coletivo da final é eleito por muitos o melhor de todos os tempos.","tip":"<strong>Auge:</strong> o futebol-arte e o resultado, finalmente, na mesma equipe."},
   {"ic":"constellation","t":"O 'País do Futebol'","b":"Com o tri, o Brasil ganha de vez a taça Jules Rimet e a <strong>identidade mundial</strong> de melhor do mundo no esporte. O futebol vira religião nacional.","tip":"<strong>Significado:</strong> a vitória esportiva vira projeto de autoestima de um povo."},
  ],
  "lessons_title":"Lições-Chave do Capítulo 8",
  "lessons":["1958 e 1962: o bicampeonato com Pelé e Garrincha redime o trauma de 1950.","1970: o tri no México, com o time de 70 eleito por muitos o melhor de sempre.","Com o tri, o Brasil firma a identidade de 'país do futebol'."]},

 {"slug":"ch09-1982-tetra-penta","sub":"CAPÍTULO 9: 1982, o Tetra e o Penta",
  "intro":"O futebol brasileiro vive a beleza que perde (1982) e a maturidade que vence (1994 e 2002). Da arte de Telê Santana ao pragmatismo de 94 e ao brilho de Ronaldo em 2002, o Brasil chega às cinco estrelas.",
  "cards":[
   {"ic":"leaf","t":"1982 — a Beleza que Perdeu","b":"O time de <strong>Telê Santana</strong> — <strong>Sócrates, Zico, Falcão, Cerezo</strong> — encantou o mundo, mas caiu para a Itália de Paolo Rossi (3 a 2). Virou o símbolo eterno de que jogar bonito nem sempre vence — e por isso é amado.","tip":"<strong>Paradoxo:</strong> a derrota mais querida da história do futebol brasileiro.","wide":True},
   {"ic":"key","t":"1994 — o Tetra","b":"Nos <strong>Estados Unidos</strong>, o Brasil é <strong>tetracampeão</strong> nos pênaltis sobre a Itália após 0 a 0. O pragmatismo de <strong>Romário e Bebeto</strong> exorciza, 44 anos depois, o fantasma de 1950.","tip":"<strong>Cura:</strong> a vitória que fecha a ferida aberta no Maracanã."},
   {"ic":"spark","t":"2002 — o Penta","b":"Na <strong>Coreia/Japão</strong>, <strong>pentacampeão</strong>, 2 a 0 sobre a Alemanha, dois gols de <strong>Ronaldo</strong>, com Rivaldo e Ronaldinho. O Brasil chega a cinco estrelas, recordista mundial.","tip":"<strong>Marca:</strong> nenhuma seleção ganhou mais Copas do que o Brasil."},
  ],
  "lessons_title":"Lições-Chave do Capítulo 9",
  "lessons":["1982: o time mais belo perdeu — e virou símbolo do futebol-arte.","1994: o tetra nos pênaltis sobre a Itália exorciza o fantasma de 1950.","2002: o penta com Ronaldo torna o Brasil o maior campeão mundial."]},

 {"slug":"ch10-7x1-legado","sub":"CAPÍTULO 10: O 7 a 1, o Legado e o Debate",
  "intro":"Em 2014, em casa de novo, o Brasil sofreu o avesso de 1950. O 7 a 1 fechou um arco e reabriu uma ferida. E, no fundo de toda a história, fica um debate: o futebol incluiu — mas terá curado o racismo? Mário Filho dizia que sim; hoje a tese é contestada.",
  "cards":[
   {"ic":"wave","t":"2014 — o Mineiraço","b":"Na semifinal da Copa em casa, o Brasil foi goleado pela <strong>Alemanha por 7 a 1</strong>, sem o lesionado Neymar. O avesso de 1950, em escala digital — e, como ele, um espelho do país em crise consigo mesmo.","tip":"<strong>Eco:</strong> 64 anos depois, outra tragédia em casa marca uma geração.","wide":True},
   {"ic":"lens","t":"O Mito da Democracia Racial","b":"Freyre leu no futebol a prova de uma <strong>'democracia racial'</strong>. A crítica atual responde: a inclusão no gramado <strong>conviveu com o racismo</strong> — do 'pó de arroz' aos casos de injúria racial nas arquibancadas no século XXI.","tip":"<strong>Honestidade:</strong> o futebol foi arena da disputa racial, não a sua solução.","warn":True},
   {"ic":"constellation","t":"O Futebol como Brasil","b":"De Charles Miller a Neymar, o futebol é onde o Brasil <strong>se vê inteiro</strong>: a inclusão e o preconceito, o gênio e a tragédia, a festa e a ferida.","tip":"<strong>Síntese:</strong> entender o futebol brasileiro é entender o Brasil."},
  ],
  "lessons_title":"Lições-Chave do Capítulo 10",
  "lessons":["Em 2014 o 7 a 1 para a Alemanha repetiu, ampliado, o trauma de 1950.","A tese da 'democracia racial' (Freyre) é hoje contestada: o racismo persistiu.","O futebol é o espelho mais concentrado do Brasil — glória e ferida juntas."]},
]
