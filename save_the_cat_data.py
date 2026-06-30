# -*- coding: utf-8 -*-
"""Conteúdo (pt-BR) das páginas da biblioteca para 'Save the Cat!' de Blake
Snyder. Método de estrutura de histórias: logline, 10 gêneros, beat sheet de
15 beats (BS2), o Quadro, as leis da física do roteiro, diagnóstico."""

BOOK = {
 "title": "Save the Cat!",
 "author": "Blake Snyder",
 "header_light": "SAVE THE",
 "header_bold": "CAT!",
 "subtitle": "VISÃO GERAL · O MANUAL QUE HOLLYWOOD TENTA ESCONDER",
 "intro": "Blake Snyder vendeu roteiros por uma fortuna, levou choque atrás de choque e voltou com a confissão que todo roteirista finge não precisar: história tem regra, e a regra cabe num guardanapo. Venda o filme inteiro numa frase (a logline) antes de escrever uma cena; descubra qual das 10 transformações você está contando; bata as 15 batidas que o público já sabe de cor sem saber que sabe; arme tudo no Quadro, onde mover uma cena custa um alfinete; e, quando emperrar, dê nome ao defeito em vez de chorar. Não é fórmula que mata a arte — é a gramática que liberta. E sim: faça o herói salvar o gato logo na página dois.",
 "description": "O manual de roteiro mais prático e debochado de Hollywood. Blake Snyder entrega o sistema inteiro: a logline com ironia que vende o filme numa frase, os 10 gêneros (que são tipos de transformação, não cenários), a beat sheet de 15 batidas, o Quadro de 40 cartões, as leis da física do roteiro (salve o gato, o papa na piscina, uma só mágica por filme) e o diagnóstico que conserta a história pela planta baixa, não pela tinta da parede.",
 "hook": "Sua história afunda porque falta gramática, não talento.",
 "story_promise": "OS 15 BEATS DE SNYDER",
 "story_lessons": [
   "O herói precisa salvar o gato antes de exigir sua simpatia.",
   "Gênero é o tipo de transformação, não o cenário nem o figurino.",
   "Estrutura firme liberta — quem a evita é quem mais tranca na página.",
 ],
 "tags": ["Roteiro", "Narrativa", "Ofício"],
 "progress": "8 Capítulos",
 "cover": "assets/save-the-cat-cover.png",
 "overview_cards": [
   {"ic":"target","t":"A Logline — \"o que é isso?\"","b":"Antes de uma cena existir, uma frase que vende o filme inteiro: com <strong>ironia</strong> (a tensão já mora na premissa), uma <strong>imagem mental</strong> nítida do que vamos ver, <strong>público e tom</strong> embutidos e um <strong>título matador</strong>. Se ela não acende o olho de um estranho em um minuto, nenhuma página genial vai consertar depois.","tip":"<strong>Como aplicar:</strong> conte a premissa na fila do cinema. Se o desconhecido perguntar 'quando estreia?', você tem um filme. Os olhos dele são o veredito.","wide":True},
   {"ic":"book","t":"Os 10 Gêneros","b":"Pôr nave e alienígena não faz ficção científica — só troca o figurino. Gênero é o <strong>tipo de transformação</strong> que o herói atravessa: Monstro na Casa, Velocino de Ouro, Lâmpada Mágica, Cara com um Problema, Ritos de Passagem, Amor de Camaradas, Por Que Foi Feito?, Triunfo do Tolo, Institucionalizado, Super-Herói. Toda história nova é prima de uma dessas dez.","tip":"<strong>Modelo mental:</strong> ache a família, assista aos parentes ricos, e entregue o familiar com uma torção — é 'o mesmo, só que diferente'."},
   {"ic":"clock","t":"A Beat Sheet — 15 Beats","b":"O esqueleto de toda história que funciona, da <strong>Imagem de Abertura</strong> à <strong>Imagem Final</strong> — espelhos que provam o quanto o herói mudou —, com paradas obrigatórias no Catalisador, na Diversão e Jogos (a promessa da premissa), no Ponto Médio e no Tudo Está Perdido. É um mapa, não uma camisa de força.","tip":"<strong>Chave:</strong> estrutura é forma, não fórmula. O público não sabe nomear as batidas, mas sente na pele quando falta uma."},
 ],
}

CHAPTERS = [
 {"slug":"ch01-logline","sub":"CAPÍTULO 1: O Que É Isso? — A Logline",
  "intro":"A primeira coisa que se vende não é o roteiro: é a frase. Se a sua premissa não cabe numa linha que faz um estranho querer ver, o defeito está na ideia — e não há página brilhante que ressuscite uma ideia que não vende.",
  "cards":[
      {"ic":"target","t":"A Frase Que Vende o Filme","emph":"Logline","b":"Logline não é resumo educado: é o gancho que segura a carteira do estúdio. Precisa de ironia (a tensão já vem embutida na premissa), de uma imagem mental que projete o filme na cabeça de quem ouve e de um título que conte o que é. <strong>Se não há um nó de tensão na própria frase, você não escreveu uma logline — escreveu uma sinopse, e ninguém compra sinopse.</strong>","tip":"<strong>Como aplicar:</strong> ponha herói e desafio em rota de colisão. O contraste cômico ou trágico entre os dois é o motor da ironia."},
      {"ic":"eye","t":"O Teste do Estranho","emph":"Teste","b":"Despeje a premissa no colo de quem não te deve nada. Se o olho não acender na hora, é a ideia avisando que está morta — agradeça e enterre. <strong>O pior pecado do roteirista é passar meses cavando um túnel que ninguém faz questão de atravessar.</strong>","tip":"<strong>Modelo mental:</strong> faça a bilheteria do filme na fila do café, antes da primeira palavra digitada. Sai mais barato."},
      {"ic":"gap","t":"Quem Precisa Explicar, Já Perdeu","emph":"Explicação","b":"Se a sua ideia central só faz sentido depois de cinco minutos de preâmbulo, ela nasceu morta. <strong>Empilhar regras de mundo e mitologia não tapa o buraco de um conflito que não fisga sozinho.</strong> O público compra o problema do herói, não a planta do cenário.","tip":"<strong>Cuidado:</strong> apaixonar-se pela ideia cedo demais cega o autor para as críticas — e cego, ele caminha sorrindo para o precipício.","warn":True},
    ],
  "lessons_title":"Lições-Chave do Capítulo 1",
  "lessons":["Uma frase com ironia, imagem, público e título — antes de existir uma cena.","Teste com estranhos: o olho deles acende, ou a ideia está morta.","Ideia que não vende em um minuto não melhora com 110 páginas."]},

 {"slug":"ch02-generos","sub":"CAPÍTULO 2: O Mesmo, Só Que Diferente — Os 10 Gêneros",
  "intro":"O público quer duas coisas opostas ao mesmo tempo: o conforto de algo que já conhece e o frio na barriga de algo que nunca viu. Snyder resolve o paradoxo num lance: pare de pensar em cenário e pense em transformação.",
  "cards":[
      {"ic":"book","t":"Gênero É a Mudança, Não o Figurino","emph":"Mudança","b":"Encher a tela de nave e alienígena não faz ficção científica — só enfeita o palco. O que define o gênero é a mecânica da virada do protagonista. <strong>A sua história é a ferida que o herói cura, não a roupa que ele veste na cena.</strong>","tip":"<strong>Como aplicar:</strong> ignore o disfarce do enredo e olhe a espinha. Descubra a família a que ele pertence e jogue pelas regras dela."},
      {"ic":"layers","t":"As Dez Caixas de Hollywood","emph":"Dez Caixas","b":"Toda história já contada cabe em dez caixas — do 'Monstro na Casa' ao 'Triunfo do Tolo'. <strong>Cada vez que você foge das regras da sua caixa para 'reinventar a roda', a narrativa engasga e o público não sabe dizer por quê.</strong> Ele tem a gramática desses dez formatos gravada na memória desde criança.","tip":"<strong>Modelo mental:</strong> aceite os clichês da estrutura sem vergonha. A sua originalidade mora na tinta de fora, não na fundação."},
      {"ic":"key","t":"O Mesmo, Só Que Diferente","emph":"Mesmo / Diferente","b":"O contrato com o público pede que você honre a promessa do gênero e, na mesma respirada, o surpreenda na execução. <strong>Quando um autor se gaba de que a obra dele 'não se parece com nada', quase sempre está confessando que errou na fundação.</strong>","tip":"<strong>Como aplicar:</strong> dê o esqueleto que o público espera sem perceber que espera — e vista nele uma pele que ele nunca viu."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 2",
  "lessons":["Gênero é o tipo de transformação, não o cenário nem o figurino.","Ache a família, assista aos parentes, honre o esqueleto.","Entregue o familiar com uma torção — 'não parecer com nada' é confissão de erro."]},

 {"slug":"ch03-heroi","sub":"CAPÍTULO 3: É Sobre Um Cara Que… — O Herói",
  "intro":"O herói não é sagrado: é a peça que melhor serve à logline. O protagonista certo amplifica a ideia; o errado a desperdiça — e você só descobre na sala de montagem, tarde demais.",
  "cards":[
      {"ic":"target","t":"Escolha Quem Mais Tem a Perder","emph":"Herói Ideal","b":"O protagonista certo não é o seu xodó: é o que mais sangra na premissa, o que começa no extremo oposto da lição que vai aprender. <strong>Se um coadjuvante tem mais a perder e uma curva de mudança maior, promova-o a herói e demita o titular sem dó.</strong>","tip":"<strong>Como aplicar:</strong> quanto mais fundo o herói começa, mais alto pode chegar. Maximize a falha inicial para alavancar a glória do final."},
      {"ic":"spiral","t":"É Primal?","emph":"Primal","b":"Toda motivação fina demais é motivação fraca. O que move plateia é instinto de caverna: proteger a cria, fugir da morte, matar a fome, defender o ninho. <strong>Se um homem das cavernas não choraria pela aflição do seu herói, a plateia de hoje vai cochilar do mesmo jeito.</strong>","tip":"<strong>Modelo mental:</strong> traduza o intelectual em visceral. 'Perder o emprego' não emociona; 'não ter como pôr comida no prato dos filhos' emociona."},
      {"ic":"eye","t":"Herói Passivo Mata o Filme","emph":"Herói Passivo","b":"Personagem passivo é figurante com falas longas. O herói de verdade pega as rédeas e empurra a história pelo pescoço a cada virada de ato. <strong>Se o seu protagonista só apanha do acaso e é salvo pelos outros, a história murcha e o filme afunda — e ninguém vai saber explicar a causa.</strong>","tip":"<strong>Cuidado:</strong> faça a pergunta crua a cada ato — o herói decidiu entrar nesta briga, ou foi arrastado pela orelha?"},
    ],
  "lessons_title":"Lições-Chave do Capítulo 3",
  "lessons":["Escolha o herói que maximiza conflito, arco e identificação — não o favorito.","Toda motivação que funciona é primal: comida, abrigo, prole, sobrevivência.","Herói conduz; se ele só reage do início ao fim, o roteiro tem dono errado."]},

 {"slug":"ch04-beat-sheet","sub":"CAPÍTULO 4: Vamos Marcar as Batidas — A Beat Sheet",
  "intro":"Toda história que funciona — não importa o gênero — bate as mesmas 15 batidas, mais ou menos nas mesmas marcas de página. A beat sheet (BS2) é a gramática que o público já tem no ouvido sem nunca ter aberto um livro de roteiro.",
  "cards":[
      {"ic":"clock","t":"As 15 Batidas, da Abertura ao Final","emph":"15 Batidas","b":"As batidas não são camisa de força: são a espinha dorsal do contar histórias. Do Catalisador (o que estraga a vida velha) ao Tudo Está Perdido (o fundo do poço com cheiro de morte), elas ditam quando o filme respira e quando aperta. <strong>A estrutura firme é o que liberta a imaginação de ficar patinando no vazio do segundo ato.</strong>","tip":"<strong>Modelo mental:</strong> o soneto também tem métrica fixa, e nem por isso Shakespeare ficou pobre. Use o gabarito como guia, não como grilhão."},
      {"ic":"spiral","t":"Diversão e Jogos Paga a Promessa","emph":"Promessa","b":"A Diversão e Jogos é onde você entrega o produto que vendeu: as cenas do trailer, a piada do pôster, o motivo pelo qual a pessoa comprou o ingresso. <strong>Se o miolo do filme ignorar o absurdo — cômico ou tenso — da premissa, o público sente que foi vítima de propaganda enganosa, e tem razão.</strong>","tip":"<strong>Como aplicar:</strong> leia o segundo ato perguntando, página a página: cadê a promessa do título? Se sumiu, traga de volta."},
      {"ic":"scale","t":"Abertura e Final São Espelhos","emph":"Espelho","b":"A Imagem de Abertura e a Imagem Final precisam provar, sem uma palavra, o tamanho da mudança no herói. <strong>Se nas duas pontas do filme ele respira do mesmo jeito e carrega os mesmos problemas, a história girou em falso — fez barulho e não saiu do lugar.</strong>","tip":"<strong>Regra:</strong> não feche a jornada sem o recibo visual de que aquela alma foi derretida e forjada de novo."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 4",
  "lessons":["15 batidas, 3 atos, marcas aproximadas de página — gramática, não algema.","Diversão e Jogos é onde você paga a promessa da premissa.","Imagem de Abertura e Final são espelhos: a mudança tem que se ver."]},

 {"slug":"ch05-o-quadro","sub":"CAPÍTULO 5: Construindo a Fera Perfeita — O Quadro",
  "intro":"Entre a beat sheet e o rascunho existe o Quadro: a história inteira pregada na parede, visível de um só golpe de vista — onde mover uma cena custa um alfinete, não uma semana de reescrita.",
  "cards":[
      {"ic":"layers","t":"Quarenta Cartões na Parede","emph":"Quadro","b":"O caos da escrita amansa quando você crava uns quarenta cartões em quatro fileiras: ato 1, as duas metades do ato 2 e o ato 3. Partir o segundo ato no meio mata aquele deserto sem rumo onde tantos roteiros morrem de sede. <strong>Se uma fileira incha mais que as outras, o filme está manco — e dá para ver isso a três metros de distância.</strong>","tip":"<strong>Como aplicar:</strong> afaste-se e olhe as fileiras de longe. Barriga de cartões na parede é barriga de ato no roteiro."},
      {"ic":"target","t":"Toda Cena É um Ringue","emph":"Carga","b":"Cena sem conflito e sem virada de carga (+/−) é informação jogada fora. Cada cartão precisa de um embate (quem quer o quê) e de uma emoção que muda da porta de entrada à de saída. <strong>Se o personagem entra feliz e sai feliz depois de uma conversa explicando o enredo, rasgue o cartão.</strong>","tip":"<strong>Regra:</strong> marque um sinal de mais e um de menos em cada cartão. A polaridade tem que virar até o fim da cena — sem exceção."},
      {"ic":"wrench","t":"Erre no Papelão, Não na Página","emph":"Papelão","b":"Consertar um furo no cartão custa centavos; descobri-lo na página 80 custa sangue e semanas. Todo buraco tapado na fase do Quadro é um colapso evitado lá na frente. <strong>Pular o planejamento em nome da 'intuição artística' é marcar hora com um acidente de trem no terceiro ato.</strong>","tip":"<strong>Cuidado:</strong> a inspiração que te faz pular o Quadro é a mesma que te faz chorar quando a trama desaba sem conserto possível."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 5",
  "lessons":["4 fileiras, ~40 cartões: a história inteira visível antes da 1ª página.","Cada cartão tem conflito (><) e virada de emoção (+/−), ou vai pro lixo.","Erre no papelão barato, nunca na página cara."]},

 {"slug":"ch06-leis-fisica-roteiro","sub":"CAPÍTULO 6: As Leis Imutáveis da Física do Roteiro",
  "intro":"Um punhado de leis tão certas quanto a gravidade. Quando você as obedece, ninguém percebe que existem; quando as quebra, a história cai no chão — e nem você sabe dizer por quê. Começam pela que dá nome ao livro.",
  "cards":[
      {"ic":"key","t":"Salve o Gato","emph":"Salvar o Gato","b":"Logo de cara, faça o protagonista praticar um gesto de decência genuína — ajudar um coitado, fazer piada com classe sob pressão. <strong>O público precisa achar um fiapo de nobreza no herói cedo para decidir torcer por ele — ainda mais se o sujeito for um canalha no resto do filme.</strong> Daí o nome: o assassino de aluguel para tudo para salvar o gato.","tip":"<strong>Como aplicar:</strong> seu herói pode ser frio e mortal — mas ponha-o salvando o cachorro na página dois, e ele é nosso."},
      {"ic":"wave","t":"O Papa na Piscina","emph":"Papa na Piscina","b":"Toda história arrasta fardos de exposição chata que não dá para cortar. A saída não é alinhar a plateia e ditar as regras do mundo. <strong>Enterre a informação seca debaixo de algo que prenda o olho — uma cena engraçada, sexy ou violenta — para o público engolir o remédio sem sentir o gosto.</strong>","tip":"<strong>Modelo mental:</strong> mostre o papa explicando a trama enquanto nada de sunga numa piscina. O olho fica na piscina; a informação entra pela porta dos fundos."},
      {"ic":"spiral","t":"Uma Só Mágica por Filme","emph":"Uma Só Mágica","b":"A plateia te empresta a descrença para um milagre por ingresso — e cobra fidelidade no resto. <strong>Dar ao herói superpoderes e, no segundo ato, revelar que ele também é um fantasma é estourar o contrato de uma só tacada.</strong> Dois milagres independentes afundam a verossimilhança junto com o filme.","tip":"<strong>Regra:</strong> escolha a única mentira que funda o seu universo. A partir dela, tudo obedece à física estrita do mundo real."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 6",
  "lessons":["Salve o gato cedo: compre a simpatia antes de cobrar paciência.","Esconda a exposição sob a ação; gaste uma só licença de magia.","Todos mudam, menos o vilão — e a ameaça tem que ser iminente, não teórica."]},

 {"slug":"ch07-diagnostico","sub":"CAPÍTULO 7: O Que Há de Errado? — Diagnóstico",
  "intro":"Reescrever não é 'mexer no texto até soar melhor' — é diagnóstico médico. Quando a história adoece, a cura começa por dar nome ao mal, e dar nome ao mal já é metade da cura.",
  "cards":[
      {"ic":"target","t":"A Falha Está na Fundação","emph":"Diagnóstico","b":"Quando a leitura perde a graça, o culpado quase nunca é um diálogo infeliz. O buraco mora na fundação: herói frouxo, vilão morno, risco de mentira, tema sem coluna moral. <strong>Vistorie a planta baixa, não o acabamento: o problema está nas vigas de aço, não na cor da parede.</strong>","tip":"<strong>Como aplicar:</strong> faça a pergunta impiedosa de sempre — o herói escolheu entrar na briga, ou só escorregou no acaso?"},
      {"ic":"sword","t":"O Vilão É o Teto do Herói","emph":"Vilão","b":"O tamanho do herói é ditado pela altura da muralha que o vilão ergue. Antagonista fraco engessa qualquer protagonista — não há glória em vencer um capacho. <strong>Quando o arco do herói parece raso, não mexa nele: aumente a maldade do vilão e suba a aposta a cada encontro.</strong>","tip":"<strong>Modelo mental:</strong> o bem só arranca aplauso quando o mal parecia, até a última cena, invencível e perfeitamente racional."},
      {"ic":"eye","t":"Não Trate o Sintoma Errado","emph":"Sintoma","b":"Polir diálogos para curar a barriga do segundo ato é passar perfume caro em material morto. <strong>Barriga narrativa não se trata com retoque de parágrafo — pede o bisturi: arrancar cenas inteiras que não carregam a premissa para frente.</strong>","tip":"<strong>Cuidado:</strong> pare de ajeitar a vírgula de uma cena que, na verdade, deveria ser incendiada sem dó."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 7",
  "lessons":["Reescrita é diagnóstico: nomeie o mal antes de tentar tratá-lo.","Herói passivo, personagem que fala o enredo e vilão fraco são os suspeitos de sempre.","Para crescer o herói, engrandeça o vilão e torne as estacas primais."]},

 {"slug":"ch08-fade-in-final","sub":"CAPÍTULO 8: Fade In Final — Vender e Persistir",
  "intro":"Roteiro pronto não é a linha de chegada — é a largada da parte mais dura: vender o filme e, sobretudo, sobreviver à carreira sem virar pó.",
  "cards":[
      {"ic":"target","t":"O Teste do Pôster","emph":"Pôster","b":"A ideia só está madura quando cabe num pôster: uma imagem nítida e um título que, sozinhos, prometem o filme. <strong>Se a capa não explode na escuridão, não há genialidade no recheio que recupere a atenção — nem a carteira — de quem passou correndo pela frente do cinema.</strong>","tip":"<strong>Como aplicar:</strong> faça a ponte com o que o mercado já conhece. 'É X encontra Y' situa o ouvinte em dois segundos e vende junto."},
      {"ic":"steps","t":"O Ofício, Não o Lampejo","emph":"Ofício","b":"Roteirista profissional não vive de inspiração ofendida: vive de gaveta cheia de loglines prontas para o próximo tiro. <strong>Rejeição não é epitáfio do seu talento — é só o mercado, surdo e ocupado, fazendo as próprias contas.</strong> Separe a nota da página do valor da sua pessoa, ou a carreira te quebra na primeira porta fechada.","tip":"<strong>Modelo mental:</strong> escreva sempre a próxima. Encare cada 'não' como pesquisa de terreno, nunca como veredito sobre quem você é."},
      {"ic":"eye","t":"Venda o Gancho, Não o Enredo","emph":"Gancho","b":"No pitch, despejar cada reviravolta do enredo enterra a curiosidade do ouvinte em vez de acendê-la. <strong>Conquista-se um sim vendendo a espinha tensa do problema central — e deixando o silêncio cobrar o desfecho que ele vai pagar para descobrir.</strong>","tip":"<strong>Regra:</strong> pitch não é sinopse falada. Finque a dor central no estômago do comprador e cale a boca — a curiosidade fecha o negócio."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 8",
  "lessons":["Título + pôster + logline são o teste final de clareza da ideia.","No pitch, dê gênero, ironia e comparações — e pare antes de cansar.","Carreira é persistência informada: muitas loglines, e ouvir as notas sem se ferir."]},
]
