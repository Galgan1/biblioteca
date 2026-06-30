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
 "intro": "Em 1894 a bola chegou debaixo do braço de um filho da elite, vinda da Inglaterra — esporte de sócio branco, de luva e diploma. Virou a coisa mais brasileira que existe no dia em que o negro, o mulato e o pobre pularam a cerca e ganharam. Mário Filho, em 'O Negro no Futebol Brasileiro', conta esse momento: foi quando a várzea invadiu o gramado nobre que o jogo deixou de ser cópia e aprendeu a gingar. Daí nasceram tudo — o drible que o mundo copia, o tri de Pelé, e as duas feridas que não fecham, o Maracanazo e o 7 a 1. A história do futebol brasileiro é o próprio Brasil se olhando no espelho — e nem sempre gostando do que vê.",
 "description": "A história do futebol brasileiro da casaca à camisa amarela, lida pelo maior clássico do tema: 'O Negro no Futebol Brasileiro', de Mário Filho. Charles Miller e a origem de elite (1894); a barreira racial e o 'pó de arroz'; a ruptura do Vasco (1923), que escalou pobre e foi campeão; Friedenreich e Leônidas; a profissionalização (1933) que derrubou o último muro; a invenção da ginga; o Maracanazo (1950) e o 'complexo de vira-lata' de Nelson Rodrigues; o tri de Pelé e Garrincha (1958/62/70); a beleza que perdeu em 1982; o tetra e o penta (1994/2002); o 7 a 1 de 2014; e o debate sobre o mito da democracia racial — o futebol como arena da nossa questão de raça, não como sua cura.",
 "hook": "O craque precisava empoar o rosto para jogar. Isso é futebol brasileiro.",
 "story_promise": "O PÓ DE ARROZ QUE O BRASIL ESCONDE",
 "story_lessons": [
   "A ginga brasileira nasceu da exclusão racial, não do talento natural.",
   "O Vasco de 1923 foi campeão sem precisar de um único jogador branco.",
   "O 7 a 1 de 2014 revelou o mesmo Brasil que o Maracanazo de 1950.",
 ],
 "tags": ["História", "Futebol", "Brasil", "Cultura"],
 "progress": "10 Capítulos",
 "cover": "assets/futebol-brasileiro-cover.png",
 "overview_cards": [
   {"ic":"fork","t":"De Esporte de Elite a Paixão Nacional","b":"A bola entrou pela porta da frente, com a aristocracia — clube branco, sócio rico, 'inglês de imitação'. Só virou <strong>brasileira</strong> quando o povo escuro e pobre entrou pela várzea, pulou a cerca e <strong>ganhou</strong>. Para Mário Filho, é aí, e não em 1894, que o nosso futebol de fato nasce.","tip":"<strong>Chave de leitura:</strong> o jogo brasileiro nasceu do encontro racial — não apesar dele, mas por causa dele.","wide":True},
   {"ic":"spark","t":"A Invenção da Ginga","b":"Junte a técnica do inglês ao corpo do morro — a malandragem, a capoeira, o samba na cintura — e dá nisto: <strong>drible, finta, improviso</strong>. Galeano chamou de futebol-arte: a beleza como fim, não só a vitória como desculpa.","tip":"<strong>Assinatura:</strong> é o único jeito de jogar que o mundo inteiro reconhece de olhos fechados e chama de 'brasileiro'."},
   {"ic":"wave","t":"A Glória e a Ferida, o Espelho do País","b":"O Maracanazo (1950) e o 7 a 1 (2014) são luto nacional; o tri de Pelé (1958/62/70) e o penta (2002), delírio coletivo. Em campo, o Brasil <strong>se vê inteiro</strong> — o gênio e o fracasso, a festa e a vergonha.","tip":"<strong>Modelo mental:</strong> o futebol não é fuga da realidade brasileira. É essa realidade em estado concentrado, com mais luz e mais sombra."},
 ],
}

CHAPTERS = [
 {"slug":"ch01-origem-aristocratica","sub":"CAPÍTULO 1: A Origem Aristocrática (1894)",
  "intro":"O futebol não nasceu popular no Brasil. Em 1894, Charles Miller desembarcou da Inglaterra com duas bolas e um livro de regras debaixo do braço e o apresentou a uma elite branca e abastada. Por décadas, foi marca de distinção: clube de sócio, não paixão de rua. A bola, aqui, começou como casaca.",
  "cards":[
      {"ic":"flag","t":"O Esporte de Casaca","emph":"Casaca","b":"Charles Miller desembarca em 1894 com a bola na bagagem, e o jogo estreia no Brasil como diversão de cavalheiro. Nessas primeiras décadas, a grama nobre só aceita <strong>o sócio branco, de boas famílias e diploma inglês</strong> — futebol é, antes de paixão, um sobrenome.","tip":"<strong>Marco:</strong> o esporte entra pela porta da frente da elite. A paixão de rua viria depois, e contra a vontade dela."},
      {"ic":"mask","t":"A Trincheira do Amadorismo","emph":"Amadorismo","b":"Proibir pagamento por jogar parecia defesa do 'amor puro à camisa'. Era filtro de classe: <strong>só joga de graça quem não precisa do dinheiro</strong>. A regra do amadorismo, tão nobre no discurso, deixava o operário e o negro de fora — sem ofender ninguém.","tip":"<strong>Sinal de alerta:</strong> desconfie da regra 'neutra' que, por acaso, só atrapalha sempre os mesmos. O muro mais firme é o que não parece muro.","warn":True},
      {"ic":"key","t":"O Fogo da Várzea","emph":"Várzea","b":"Enquanto a taça brilhava entre madames no jardim do clube, o talento se forjava no campo de terra do subúrbio, descalço, ao sol. <strong>Foi a exclusão que criou a várzea — e a várzea criou o craque</strong> que a elite não queria e não pôde, depois, ignorar.","tip":"<strong>Modelo mental:</strong> o novo costuma nascer na margem que o centro despreza. Quem é barrado da festa acaba inventando a sua própria."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 1",
  "lessons":["O futebol chegou ao Brasil em 1894, importado por uma elite branca.","No começo era marca de distinção social, não paixão popular.","O amadorismo funcionava como filtro de classe — e seria o primeiro muro a cair."]},

 {"slug":"ch02-barreira-racial","sub":"CAPÍTULO 2: A Barreira Racial e o 'Pó de Arroz'",
  "intro":"Para entrar no futebol de elite, o jogador de pele escura precisava parecer branco. A lenda do 'pó de arroz' resume a época: a inclusão até existia, mas sob a condição do embranquecimento. É o conflito que Mário Filho põe no centro do livro — e da nossa história.",
  "cards":[
      {"ic":"mask","t":"O Pó de Arroz","emph":"Pó de Arroz","b":"Conta-se que o mulato do Fluminense empoava o rosto antes de entrar em campo, para clarear a pele e ser tolerado — daí a torcida tricolor virar 'pó de arroz'. <strong>Para ser aceito, o talento tinha de pedir desculpa pela própria cor</strong>. A inclusão vinha com fatura, e a fatura era a identidade do jogador.","tip":"<strong>Armadilha:</strong> celebrar a entrada do negro no futebol e esquecer o preço que ele pagou para entrar é contar metade da história — a metade confortável.","warn":True},
      {"ic":"gap","t":"Dois Futebóis","emph":"Dois Futebóis","b":"De um lado, o futebol oficial: liga branca, amadora, anotada nos jornais. Do outro, o futebol da várzea: negro, operário, jogado no campo de terra e ignorado pela elite. <strong>Eram dois países dentro do mesmo país, separados pela cor e pela carteira</strong> — e jogando, sem saber, a mesma partida.","tip":"<strong>Prática:</strong> o talento que se forja na margem aprende, na raça, soluções que o manual do centro nunca ensina. A criatividade mora onde falta tudo."},
      {"ic":"lens","t":"O Espelho de Mário Filho","emph":"Mário Filho","b":"Mário Filho fez do futebol uma forma de contar o Brasil: narrou a entrada do negro em campo como epopeia, não como nota de rodapé. <strong>Para ele, o gol da várzea valia uma página de história nacional</strong> — porque era ali, e não nos discursos, que o país de fato se misturava.","tip":"<strong>Regra:</strong> não leia o futebol brasileiro pelo manual tático do estrangeiro. Leia a arquibancada — é nela que está escrita a alma mestiça do país."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 2",
  "lessons":["A inclusão inicial vinha com a condição do embranquecimento ('pó de arroz').","Havia dois futebóis: o de elite (oficial) e o de várzea (popular).","Para Mário Filho, furar essa barreira é o ato fundador do futebol brasileiro."]},

 {"slug":"ch03-ruptura-vasco","sub":"CAPÍTULO 3: A Ruptura — o Vasco da Gama (1923)",
  "intro":"Em 1923 o Vasco da Gama escalou negros, mulatos e operários e foi campeão carioca logo na estreia na primeira divisão. A elite reagiu criando uma liga separada, com regras feitas para barrar o jogador pobre. O Vasco resistiu. O talento popular furou o muro — e não voltou atrás.",
  "cards":[
      {"ic":"mountain","t":"A Estreia que Virou Título","emph":"Estreia","b":"Sustentado pela colônia portuguesa, o Vasco subiu à primeira divisão com um time de negros, mulatos e operários — e foi <strong>campeão carioca logo na estreia, em 1923</strong>. Dentro das quatro linhas, o pulmão do pobre derrubou o currículo da elite. O placar não mente nem tem cor de pele.","tip":"<strong>Marco:</strong> não foi discurso, foi vitória. O Vasco provou no campo o que o salão se recusava a admitir: o povo jogava melhor."},
      {"ic":"sword","t":"As Regras 'Neutras'","emph":"Regras","b":"Derrotada na bola, a elite revidou na burocracia: criou uma liga (a AMEA) que exigia comprovante de emprego e prova de alfabetização. <strong>Eram regras 'neutras' desenhadas para trancar fora o jogador negro e analfabeto</strong> sem precisar dizer o nome do preconceito.","tip":"<strong>Sinal de alerta:</strong> quando não se pode vencer no mérito, muda-se a regra. A exigência 'técnica' é, muitas vezes, a discriminação de gravata.","warn":True},
      {"ic":"key","t":"O 'Não' que Mudou Tudo","emph":"O 'Não'","b":"O Vasco podia ter cedido para ser aceito. Recusou: bancou seus jogadores e enfrentou o cerco. <strong>Foi esse 'não' que tornou a inclusão irreversível</strong> — depois dele, não havia mais como devolver o povo para fora do gramado.","tip":"<strong>Modelo mental:</strong> portas fechadas só caem quando alguém se recusa a bater de leve. A história vira na hora em que o excluído para de pedir licença."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 3",
  "lessons":["O Vasco foi campeão de 1923 com um time de negros, mulatos e operários.","A elite reagiu com regras 'neutras' criadas para excluir o jogador pobre.","A resistência do Vasco tornou a inclusão irreversível."]},

 {"slug":"ch04-friedenreich","sub":"CAPÍTULO 4: Friedenreich, o Primeiro Craque Mestiço",
  "intro":"Antes de Pelé, houve Friedenreich. Filho de pai alemão e mãe negra, 'El Tigre' foi o maior craque do Brasil das primeiras décadas — e carregava no próprio corpo, mestiço e de olhos verdes, a contradição racial do país inteiro.",
  "cards":[
      {"ic":"spark","t":"El Tigre e o Gol de 1919","emph":"El Tigre","b":"Friedenreich fez o gol que deu ao Brasil o título sul-americano de <strong>1919</strong>, sobre o Uruguai, e foi o maior artilheiro da sua geração. <strong>Foi o primeiro craque a transformar o talento da margem em glória da nação</strong> — o sinal de que o futebol brasileiro tinha encontrado o próprio jeito de vencer.","tip":"<strong>Regra:</strong> o número (gols, títulos) é o que entra no livro; mas o que ficou foi a forma — a primeira assinatura de drible brasileiro num ídolo de massa."},
      {"ic":"mask","t":"A Dor no Vestiário","emph":"Vestiário","b":"Mulato de olhos verdes, Friedenreich alisava o cabelo crespo no vestiário antes de entrar em campo — pequeno gesto que dizia tudo. <strong>O maior craque do país precisava, todo dia, negociar com a própria cor para ser aceito</strong>. A glória era pública; o constrangimento, particular.","tip":"<strong>Armadilha:</strong> idolatrar o craque e apagar o preço racial que ele pagou é polir a estátua e esconder a corrente. O ídolo carregava o conflito do país no próprio espelho.","warn":True},
      {"ic":"constellation","t":"O Drible Nasce Aqui","emph":"Drible","b":"O futebol de compasso reto, importado, esbarrava no corpo de El Tigre: ginga, finta, mudança de direção. <strong>Antes de virar estilo nacional com Pelé e Garrincha, o drible brasileiro já balançava nas pernas de Friedenreich</strong> — a semente da arte que o mundo copiaria.","tip":"<strong>Como aplicar:</strong> a genialidade brota do desvio, não da linha reta. O passo de lado que confunde o zagueiro é a mesma malandragem que o Brasil traria do samba para o campo."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 4",
  "lessons":["Friedenreich foi o maior craque brasileiro antes de Pelé (gol do título de 1919).","Mestiço, encarnava a contradição racial do país dentro do próprio ídolo.","Nele já nasce o drible como assinatura do futebol brasileiro."]},

 {"slug":"ch05-profissionalizacao","sub":"CAPÍTULO 5: A Profissionalização (1933) e Leônidas (1938)",
  "intro":"Em 1933 o futebol brasileiro se tornou profissional — pagar para jogar derrubou o último muro do amadorismo de elite. Agora o talento podia vir de qualquer lugar. E veio: Leônidas, o Diamante Negro, brilhou na Copa de 1938.",
  "cards":[
      {"ic":"key","t":"O Salário que Abriu a Porta","emph":"Salário","b":"Quando, em 1933, pagar para jogar virou regra, ruiu o último muro do amadorismo de elite — aquele que só deixava jogar quem não precisava do dinheiro. <strong>O profissionalismo democratizou o acesso: agora o talento podia vir do morro, da fábrica, de qualquer lugar — e veio</strong>. Cinco anos depois, na Copa de 1938, <strong>Leônidas da Silva, o Diamante Negro</strong>, foi artilheiro do mundial e virou o primeiro ídolo negro de massa do país. A prova, em campo internacional, de que o futebol brasileiro tinha enfim encontrado a própria voz."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 5",
  "lessons":["Em 1933 o futebol vira profissional e o acesso se democratiza.","Leônidas, o Diamante Negro, foi artilheiro da Copa de 1938.","O talento popular chega ao topo e o Brasil começa a criar estilo próprio."]},

 {"slug":"ch06-futebol-arte","sub":"CAPÍTULO 6: O Futebol-Arte — a Ginga",
  "intro":"Do encontro entre a técnica importada e o corpo popular — a malandragem, a capoeira, o samba — nasce o estilo brasileiro: drible curto, finta, improviso. Galeano o chama de futebol-arte: a beleza como fim, não só a vitória como meio.",
  "cards":[
      {"ic":"spark","t":"A Ginga","emph":"Ginga","b":"O traço brasileiro: <strong>drible, finta e improviso</strong>, um jeito de jogar que herda o gingado da capoeira e o suingue do samba. Outros povos jogam para ganhar; o brasileiro joga também para <strong>se expressar</strong> — o gol é frase, não só placar.","tip":"<strong>Identidade:</strong> o mundo aprendeu a reconhecer o 'jogo brasileiro' de longe, pela ginga, como se reconhece um sotaque.","wide":True},
      {"ic":"leaf","t":"Beleza como Fim","emph":"Beleza como Fim","b":"Para Galeano, o <strong>futebol-arte</strong> se opõe ao futebol-resultado: jogar bonito tem valor próprio, mesmo quando não vence. A torcida brasileira ama o gol de placa tanto quanto a taça.","tip":"<strong>Valor cultural:</strong> a estética do jogo vira patrimônio nacional."},
      {"ic":"link","t":"Mestiçagem em Campo","emph":"Mestiçagem","b":"O estilo é <strong>mestiço</strong> por definição — soma de heranças africanas, europeias e indígenas traduzidas em movimento. Gilberto Freyre leu nisso a 'cara' do Brasil.","tip":"<strong>Atribua:</strong> a leitura 'dionisíaca/mestiça' é de Freyre — fundadora e hoje debatida."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 6",
  "lessons":["A ginga (drible, finta, improviso) é a assinatura do futebol brasileiro.","Para Galeano, o futebol-arte valoriza a beleza, não só o resultado.","O estilo é mestiço — Freyre o leu como expressão da própria identidade nacional."]},

 {"slug":"ch07-maracanazo","sub":"CAPÍTULO 7: O Maracanazo (1950) e o 'Complexo de Vira-Lata'",
  "intro":"Sede da Copa, favorito, em casa, o Brasil só precisava de um empate na decisão. Perdeu para o Uruguai por 2 a 1 no Maracanã lotado. O trauma foi tão fundo que Nelson Rodrigues batizou a ferida nacional: o complexo de vira-lata.",
  "cards":[
      {"ic":"wave","t":"A Tragédia de 1950","emph":"1950","b":"Diante de quase 200 mil pessoas, o Brasil saiu na frente e <strong>perdeu de virada para o Uruguai, 2 a 1</strong>, o <strong>Maracanazo</strong>. O silêncio do estádio virou símbolo de uma nação em choque.","tip":"<strong>Trauma fundador:</strong> a derrota em casa marca o futebol brasileiro para sempre.","wide":True},
      {"ic":"mask","t":"O Complexo de Vira-Lata","emph":"Vira-Lata","b":"<strong>Nelson Rodrigues</strong> cunhou a expressão: o brasileiro que se sente <strong>inferior</strong> diante do resto do mundo. A ferida de 1950 virou diagnóstico de um país.","tip":"<strong>Atribua:</strong> 'complexo de vira-lata' é de Nelson Rodrigues, após 1950."},
      {"ic":"spark","t":"A Ferida como Combustível","emph":"Combustível","b":"O trauma não paralisou — virou <strong>fome de redenção</strong>. A dor de 1950 ficou guardada como brasa e preparou o terreno para a explosão de 1958. O Brasil precisou perder em casa para, oito anos depois, ganhar no mundo.","tip":"<strong>Arco:</strong> não há redenção sem queda. A taça de 58 só pesa porque o silêncio de 50 pesou primeiro."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 7",
  "lessons":["Em 1950 o Brasil perdeu o título em casa para o Uruguai (2 a 1), o Maracanazo.","Nelson Rodrigues batizou o trauma de 'complexo de vira-lata'.","A ferida virou combustível para a redenção de 1958."]},

 {"slug":"ch08-tri-pele","sub":"CAPÍTULO 8: A Glória — 1958, 1962, 1970",
  "intro":"O vira-lata virou campeão do mundo. Em três Copas, o Brasil conquistou o tricampeonato com Pelé e Garrincha e coroou, em 1970, um dos melhores times de todos os tempos. O 'país do futebol' nasce aqui.",
  "cards":[
      {"ic":"mountain","t":"1958 e 1962 — o Bi","emph":"o Bi","b":"<strong>1958 (Suécia):</strong> primeiro título, 5 a 2 na final sobre os donos da casa; surge <strong>Pelé</strong>, aos 17 anos, ao lado de <strong>Garrincha</strong>. <strong>1962 (Chile):</strong> bicampeão, 3 a 1 na final; com Pelé lesionado, Garrincha carrega o time.","tip":"<strong>Redenção:</strong> oito anos depois do Maracanazo, o Brasil é campeão do mundo.","wide":True},
      {"ic":"spark","t":"1970 — o Time Perfeito","emph":"Time Perfeito","b":"<strong>Tricampeão</strong> no México, 4 a 1 sobre a Itália, campanha perfeita. <strong>Pelé, Tostão, Gérson, Jairzinho, Rivelino e Carlos Alberto</strong> — o gol coletivo da final é eleito por muitos o melhor de todos os tempos.","tip":"<strong>Auge:</strong> o futebol-arte e o resultado, finalmente, na mesma equipe."},
      {"ic":"constellation","t":"O 'País do Futebol'","emph":"País do Futebol","b":"Com o tri, o Brasil ganha de vez a taça Jules Rimet e a <strong>identidade mundial</strong> de melhor do mundo no esporte. O futebol vira religião nacional.","tip":"<strong>Significado:</strong> a vitória esportiva vira projeto de autoestima de um povo."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 8",
  "lessons":["1958 e 1962: o bicampeonato com Pelé e Garrincha redime o trauma de 1950.","1970: o tri no México, com o time de 70 eleito por muitos o melhor de sempre.","Com o tri, o Brasil firma a identidade de 'país do futebol'."]},

 {"slug":"ch09-1982-tetra-penta","sub":"CAPÍTULO 9: 1982, o Tetra e o Penta",
  "intro":"O futebol brasileiro vive a beleza que perde (1982) e a maturidade que vence (1994 e 2002). Da arte de Telê Santana ao pragmatismo de 94 e ao brilho de Ronaldo em 2002, o Brasil chega às cinco estrelas.",
  "cards":[
      {"ic":"leaf","t":"1982 — a Beleza que Perdeu","emph":"Beleza que Perdeu","b":"O time de <strong>Telê Santana</strong> — <strong>Sócrates, Zico, Falcão, Cerezo</strong> — encantou o mundo, mas caiu para a Itália de Paolo Rossi (3 a 2). Virou o símbolo eterno de que jogar bonito nem sempre vence — e por isso é amado.","tip":"<strong>Paradoxo:</strong> a derrota mais querida da história do futebol brasileiro.","wide":True},
      {"ic":"key","t":"1994 — o Tetra","emph":"Tetra","b":"Nos <strong>Estados Unidos</strong>, o Brasil é <strong>tetracampeão</strong> nos pênaltis sobre a Itália após 0 a 0. O pragmatismo de <strong>Romário e Bebeto</strong> exorciza, 44 anos depois, o fantasma de 1950.","tip":"<strong>Cura:</strong> a vitória que fecha a ferida aberta no Maracanã."},
      {"ic":"spark","t":"2002 — o Penta","emph":"Penta","b":"Na <strong>Coreia/Japão</strong>, <strong>pentacampeão</strong>, 2 a 0 sobre a Alemanha, dois gols de <strong>Ronaldo</strong>, com Rivaldo e Ronaldinho. O Brasil chega a cinco estrelas, recordista mundial.","tip":"<strong>Marca:</strong> nenhuma seleção ganhou mais Copas do que o Brasil."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 9",
  "lessons":["1982: o time mais belo perdeu — e virou símbolo do futebol-arte.","1994: o tetra nos pênaltis sobre a Itália exorciza o fantasma de 1950.","2002: o penta com Ronaldo torna o Brasil o maior campeão mundial."]},

 {"slug":"ch10-7x1-legado","sub":"CAPÍTULO 10: O 7 a 1, o Legado e o Debate",
  "intro":"Em 2014, em casa de novo, o Brasil sofreu o avesso de 1950. O 7 a 1 fechou um arco e reabriu uma ferida. E, no fundo de toda a história, fica um debate: o futebol incluiu — mas terá curado o racismo? Mário Filho dizia que sim; hoje a tese é contestada.",
  "cards":[
      {"ic":"wave","t":"2014 — o Mineiraço","emph":"Mineiraço","b":"Na semifinal da Copa em casa, o Brasil foi goleado pela <strong>Alemanha por 7 a 1</strong>, sem o lesionado Neymar. O avesso de 1950, em escala digital — e, como ele, um espelho do país em crise consigo mesmo.","tip":"<strong>Eco:</strong> 64 anos depois, outra tragédia em casa marca uma geração.","wide":True},
      {"ic":"lens","t":"O Mito da Democracia Racial","emph":"Democracia Racial","b":"Freyre leu no futebol a prova de uma <strong>'democracia racial'</strong>. A crítica atual responde: a inclusão no gramado <strong>conviveu com o racismo</strong> — do 'pó de arroz' aos casos de injúria racial nas arquibancadas no século XXI.","tip":"<strong>Honestidade:</strong> o futebol foi arena da disputa racial, não a sua solução."},
      {"ic":"constellation","t":"O Futebol como Brasil","emph":"como Brasil","b":"De Charles Miller a Neymar, o futebol é onde o Brasil <strong>se vê inteiro</strong>: a inclusão e o preconceito, o gênio e a tragédia, a festa e a ferida.","tip":"<strong>Síntese:</strong> entender o futebol brasileiro é entender o Brasil."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 10",
  "lessons":["Em 2014 o 7 a 1 para a Alemanha repetiu, ampliado, o trauma de 1950.","A tese da 'democracia racial' (Freyre) é hoje contestada: o racismo persistiu.","O futebol é o espelho mais concentrado do Brasil — glória e ferida juntas."]},
]
