# -*- coding: utf-8 -*-
"""Conteúdo (pt-BR) das páginas da biblioteca para 'Save the Cat!' de Blake
Snyder. Método de estrutura de histórias: logline, 10 gêneros, beat sheet de
15 beats (BS2), o Quadro, as leis da física do roteiro, diagnóstico."""

BOOK = {
 "title": "Save the Cat!",
 "author": "Blake Snyder",
 "header_light": "SAVE THE",
 "header_bold": "CAT!",
 "subtitle": "VISÃO GERAL · O MÉTODO DE ESTRUTURA DE HISTÓRIAS",
 "intro": "Blake Snyder destilou décadas de roteiro de Hollywood num sistema prático e brutalmente claro: venda a ideia numa frase (logline), descubra o tipo de transformação que você está contando (os 10 gêneros), bata as 15 batidas da estrutura (a beat sheet), arme a história inteira no Quadro antes de escrever e diagnostique o que trava pelo nome do defeito. Não é fórmula — é a gramática que o público já tem no ouvido.",
 "description": "O método prático de Blake Snyder para estruturar histórias: logline com ironia, os 10 gêneros de transformação, a beat sheet de 15 beats, o Quadro de 40 cartões, as leis da física do roteiro e um checklist de diagnóstico.",
 "tags": ["Roteiro", "Narrativa", "Ofício"],
 "progress": "8 Capítulos",
 "cover": "assets/save-the-cat-cover.png",
 "overview_cards": [
   {"ic":"target","t":"A Logline — \"o que é isso?\"","b":"Antes da primeira cena, uma frase que vende: com <strong>ironia</strong> (tensão na própria premissa), <strong>imagem mental</strong> do filme inteiro, <strong>público/tom</strong> implícitos e <strong>título matador</strong>. Se não fisga em um minuto, o roteiro não conserta.","tip":"<strong>Como aplicar:</strong> teste a logline com estranhos — os olhos deles são o veredito.","wide":True},
   {"ic":"book","t":"Os 10 Gêneros","b":"Gênero não é cenário; é o <strong>tipo de transformação</strong>: Monstro na Casa, Velocino de Ouro, Lâmpada Mágica, Cara com um Problema, Ritos de Passagem, Amor de Camaradas, Por Que Foi Feito?, Triunfo do Tolo, Institucionalizado, Super-Herói.","tip":"<strong>Modelo mental:</strong> identifique a família, estude os clássicos, entregue o familiar com uma torção."},
   {"ic":"clock","t":"A Beat Sheet — 15 Beats","b":"O mapa de toda história, da <strong>Imagem de Abertura</strong> à <strong>Imagem Final</strong> (espelhos), passando por Catalisador, Diversão e Jogos, Ponto Médio, Tudo Está Perdido e Final.","tip":"<strong>Chave:</strong> estrutura é forma, não fórmula — o público sente quando falta uma batida."},
 ],
}

CHAPTERS = [
 {"slug":"ch01-logline","sub":"CAPÍTULO 1: O Que É Isso? — A Logline",
  "intro":"Se a premissa não cabe numa frase que faz alguém querer ver, o problema está na ideia — e nenhum roteiro brilhante salva uma ideia que não vende.",
  "cards":[
      {"ic":"target","t":"A Fórmula da Logline","emph":"Logline","b":"Uma logline não é um resumo burocrático, é um soco comercial. Ela exige ironia na premissa, uma imagem mental cristalina de quem é o herói e um título que venda o problema. <strong>Se a sua frase não tiver um gancho de tensão inerente, você escreveu uma sinopse inofensiva e sem brilho.</strong>","tip":"<strong>Como aplicar:</strong> o herói e o desafio precisam ser opostos cômicos ou trágicos; o contraste é o motor da ironia."},
      {"ic":"eye","t":"O Teste do Estranho","emph":"Teste","b":"Jogue a sua premissa no colo de alguém que não lhe deve lealdade. Se os olhos do ouvinte não acenderem de curiosidade na hora, enterre a ideia. <strong>O pior erro de um criador é investir meses cavando um túnel que ninguém quer cruzar.</strong>","tip":"<strong>Modelo mental:</strong> teste a bilheteria da sua história antes de digitar a primeira cena no computador."},
      {"ic":"gap","t":"O Defeito da Explicação","emph":"Explicação","b":"Se você precisa de cinco minutos de preâmbulo para que a sua ideia central faça sentido, o seu projeto nasceu morto. <strong>Empilhar detalhes de mundo não salva a ausência de um conflito nuclear forte e evidente.</strong> O público compra o conflito, não o cenário.","tip":"<strong>Cuidado:</strong> apaixonar-se pela ideia muito cedo blinda o autor das críticas e pavimenta o caminho do desastre.","warn":True},
    ],
  "lessons_title":"Lições-Chave do Capítulo 1",
  "lessons":["Uma frase com ironia, imagem, público e título — antes da primeira cena.","Teste com estranhos; os olhos deles decidem.","Ideia que não vende em um minuto não melhora com 110 páginas."]},

 {"slug":"ch02-generos","sub":"CAPÍTULO 2: O Mesmo, Só Que Diferente — Os 10 Gêneros",
  "intro":"O público quer o conforto do familiar e a surpresa do novo ao mesmo tempo. A resposta é classificar pela transformação, não pelo cenário.",
  "cards":[
      {"ic":"book","t":"O Gênero É a Mudança","emph":"Mudança","b":"Colocar naves e alienígenas não cria um filme de ficção científica, apenas enfeita o palco. O que dita o gênero narrativo é a mecânica da transformação do protagonista. <strong>A sua história é definida pela ferida que o herói cura, não pelas roupas que ele veste na cena.</strong>","tip":"<strong>Como aplicar:</strong> olhe para a espinha dorsal do enredo; descubra a qual família ele pertence e obedeça ao formato dela."},
      {"ic":"layers","t":"As Dez Famílias Ocultas","emph":"Famílias Ocultas","b":"Existem apenas dez caixas essenciais em Hollywood: do 'Monstro na Casa' até o 'Triunfo do Tolo'. <strong>Toda vez que você foge das regras de uma dessas famílias para tentar inventar a roda, a sua narrativa engasga.</strong> O espectador possui a gramática desses dez formatos embutida na memória.","tip":"<strong>Modelo mental:</strong> aceite os clichês estruturais; o seu trabalho é inovar apenas nos detalhes da pintura externa."},
      {"ic":"key","t":"A Promessa do Mesmo","emph":"Promessa do Mesmo","b":"O pacto de venda exige que você honre a familiaridade do gênero enquanto golpeia o espectador com reviravoltas na execução. <strong>Quando um autor diz orgulhoso que sua obra não se parece com nada do mercado, ele geralmente está confessando que errou na fundação estrutural.</strong>","tip":"<strong>Como aplicar:</strong> entregue o esqueleto que o público espera de forma inconsciente, mas coloque uma pele que ele nunca viu antes."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 2",
  "lessons":["Gênero é o tipo de transformação, não o cenário.","Identifique a família, estude os clássicos, honre o esqueleto.","Entregue o familiar com uma torção — nunca só um dos dois."]},

 {"slug":"ch03-heroi","sub":"CAPÍTULO 3: É Sobre Um Cara Que… — O Herói",
  "intro":"O herói não é sagrado: é a peça que melhor serve à ideia. O certo amplifica a logline; o errado a desperdiça.",
  "cards":[
      {"ic":"target","t":"O Herói Ideal do Enredo","emph":"Herói Ideal","b":"O protagonista correto não é o seu favorito, mas aquele que mais sofre na premissa. Ele deve iniciar a jornada no extremo oposto da lição final. <strong>Se um coadjuvante tem mais a perder ou uma curva de aprendizado maior, promova-o a herói e demita o atual.</strong>","tip":"<strong>Como aplicar:</strong> o arco do protagonista dita a potência do enredo. Maximize a imperfeição inicial para alavancar a glória final."},
      {"ic":"spiral","t":"A Estaca Primal","emph":"Primal","b":"Qualquer motivação filosófica é fraca se não ancorar no instinto biológico primário: proteger a vida, buscar abrigo, salvar a prole ou aplacar a fome. <strong>Se um homem das cavernas não pudesse chorar pela angústia do seu herói, a audiência de hoje também dormirá no cinema.</strong>","tip":"<strong>Modelo mental:</strong> traduza problemas intelectuais, como perder o emprego, em dores primais: incapacidade de alimentar a própria família."},
      {"ic":"eye","t":"A Falha do Herói Passivo","emph":"Herói Passivo","b":"Personagens passivos são figurantes com falas exageradas. O protagonista verdadeiro toma as rédeas e empurra a história pelo pescoço em cada virada de ato. <strong>Se o seu herói apenas apanha do acaso e é resgatado por terceiros, a narrativa murcha e o filme fracassa vergonhosamente.</strong>","tip":"<strong>Cuidado:</strong> diagnostique o seu texto: o herói tomou a decisão de entrar no conflito ou foi arrastado pela orelha?"},
    ],
  "lessons_title":"Lições-Chave do Capítulo 3",
  "lessons":["Escolha o herói que maximiza conflito, arco e identificação.","Toda motivação que funciona é primal.","Herói conduz; se só reage do início ao fim, o roteiro tem dono errado."]},

 {"slug":"ch04-beat-sheet","sub":"CAPÍTULO 4: Vamos Marcar as Batidas — A Beat Sheet",
  "intro":"Toda história que funciona percorre 15 batidas reconhecíveis. A beat sheet é a gramática que o público já tem no ouvido.",
  "cards":[
      {"ic":"clock","t":"A Mecânica das Batidas","emph":"Mecânica","b":"O formato de 15 batidas não é um engessamento criativo, é a espinha dorsal biológica do contar histórias. Do 'Catalisador' ao 'Tudo Está Perdido', os compassos ditam o ritmo correto do respiro narrativo. <strong>A estrutura rígida liberta a imaginação de ficar patinando no vazio do tédio narrativo longo.</strong>","tip":"<strong>Modelo mental:</strong> grandes sonetos obedecem a métricas fixas. Use o gabarito das batidas como guia e não como amarra."},
      {"ic":"spiral","t":"Pague a Promessa da Capa","emph":"Promessa da Capa","b":"A fase de 'Diversão e Jogos' é a entrega do produto: é nela que ocorrem as cenas que venderam o trailer e o pôster. <strong>Se a miolo da obra ignorar o absurdo cômico ou tenso da premissa original, o público sentirá que sofreu um golpe imperdoável de propaganda enganosa.</strong>","tip":"<strong>Como aplicar:</strong> o segundo ato precisa transpirar a promessa do título a cada página."},
      {"ic":"scale","t":"A Lupa do Espelho","emph":"Espelho","b":"As imagens de abertura e encerramento precisam atestar de forma muda e visual a mudança abissal na vida do herói. <strong>Se as duas pontas do rolo de filme apresentarem o protagonista respirando do mesmo jeito e com os mesmos problemas, a história rodou em falso no asfalto.</strong>","tip":"<strong>Regra:</strong> não feche uma jornada sem cobrar o recibo visual de que a alma daquele sujeito derreteu e foi forjada de novo."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 4",
  "lessons":["15 batidas, 3 atos, posições aproximadas — gramática, não algema.","Diversão e Jogos paga a promessa da premissa.","Abertura e Final são espelhos: a transformação tem que ser visível."]},

 {"slug":"ch05-o-quadro","sub":"CAPÍTULO 5: Construindo a Fera Perfeita — O Quadro",
  "intro":"Entre a beat sheet e o rascunho existe o Quadro: a história inteira visível de uma vez, onde mover uma cena custa um alfinete, não uma semana.",
  "cards":[
      {"ic":"layers","t":"O Quadro de Cortiça","emph":"Quadro","b":"O caos da escrita amansa quando você crava cerca de quarenta cartões em quatro fileiras lógicas. Dividir o Ato 2 exatamente no meio aniquila aquele deserto exaustivo e sem rumo do miolo da obra. <strong>Se uma das fileiras do seu quadro inchar demais, o filme está manco e o desequilíbrio estrutural é certo.</strong>","tip":"<strong>Como aplicar:</strong> olhe as fileiras de longe. Uma barriga física de cartões aponta um ato barrigudo no roteiro."},
      {"ic":"target","t":"A Carga de Toda Cena","emph":"Carga","b":"Uma cena sem um ringue de boxe ou sem alteração de valor polar (+/-) é lixo informativo. Cada trecho exige embate claro e mudança emocional da entrada para a saída da porta. <strong>Se o personagem entra alegre e sai alegre após conversar sobre o enredo, rasgue a folha e jogue no lixo.</strong>","tip":"<strong>Regra:</strong> crave um sinal de mais e um de menos em cada cartão. A emoção deve girar no final da página, sem exceções."},
      {"ic":"wrench","t":"Erre no Papelão Barato","emph":"Papelão","b":"Planejar no quadro custa centavos; reescrever cinquenta páginas digitadas custa sangue. Todo buraco narrativo coberto na fase dos cartões de cortiça salva meses de angústia. <strong>Pular as trincheiras do planejamento sob a desculpa de surfe na intuição artística garante um acidente de trem no ato final.</strong>","tip":"<strong>Cuidado:</strong> a inspiração cega que o faz pular o quadro o forçará a chorar sangue quando a trama desmoronar sem conserto."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 5",
  "lessons":["4 fileiras, ~40 cartões, a história inteira visível antes da 1ª página.","Cada cartão: conflito (><) e mudança emocional (+/−).","Erre no papelão, não no roteiro."]},

 {"slug":"ch06-leis-fisica-roteiro","sub":"CAPÍTULO 6: As Leis Imutáveis da Física do Roteiro",
  "intro":"Um punhado de regras práticas que, quando obedecidas, ninguém nota; quando violadas, a história cai e ninguém sabe por quê.",
  "cards":[
      {"ic":"key","t":"O Ato de Salvar o Gato","emph":"Salvar o Gato","b":"Apresente um gesto inaugural no qual o protagonista aja com decência genuína. Pode ser humor estoico sob tortura ou ajuda a um miserável, mas tem que ser imediato. <strong>O espectador precisa encontrar um núcleo nobre no herói rapidamente para ancorar a própria torcida, principalmente se o sujeito for um canalha no geral.</strong>","tip":"<strong>Como aplicar:</strong> o herói pode ser um assassino de aluguel frio; mas faça-o salvar o cachorro na página dois."},
      {"ic":"wave","t":"O Papa na Piscina","emph":"Papa","b":"Toda história carrega fardos pesados de informações contextuais entediantes que não podem ser puladas. A solução não é ditar regras para a plateia. <strong>Enterre as explicações chatas por baixo de uma ação hilária, sexy ou violenta que cative a retina enquanto a audição trabalha calada.</strong>","tip":"<strong>Modelo mental:</strong> informação técnica sem adereço de conflito imediato é remédio amargo que ninguém engole."},
      {"ic":"spiral","t":"A Dose de Absurdo","emph":"Dose de Absurdo","b":"A plateia suspende a descrença de forma leal para um milagre único por bilhete comprado. <strong>Introduzir um protagonista que é ressuscitado e, depois, revelar que ele foi mordido por vampiros espaciais é rasgar a paciência e a lealdade da audiência de uma tacada só.</strong> Duplo milagre afunda a verossimilhança.","tip":"<strong>Regra:</strong> não empilhe magias independentes. O universo da sua obra só aceita uma mentira fundadora; o resto segue física estrita."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 6",
  "lessons":["Salve o gato cedo: compre a simpatia antes de cobrar paciência.","Esconda exposição sob ação; gaste só uma licença de magia.","Todos mudam, menos o vilão; e a ameaça tem que ser iminente."]},

 {"slug":"ch07-diagnostico","sub":"CAPÍTULO 7: O Que Há de Errado? — Diagnóstico",
  "intro":"Reescrever é diagnóstico, não \"mexer no texto até soar melhor\". Saber o nome do problema é metade da cura.",
  "cards":[
      {"ic":"target","t":"O Diagnóstico Frio","emph":"Diagnóstico","b":"Quando a leitura perde o encanto, o defeito nunca é um diálogo infeliz isolado. O abismo sempre nasce na fundação: heróis frouxos, vilões mornos, riscos falsos ou temas sem consistência moral palpável. <strong>Audite a planta baixa da estrutura; a falha está nas pilastras de aço, não na tintura da parede superficial.</strong>","tip":"<strong>Como aplicar:</strong> faça a pergunta impiedosa: \"meu herói escolheu apanhar ou apenas escorregou no acaso?\""},
      {"ic":"sword","t":"O Vilão Faz o Herói","emph":"Vilão","b":"O limite do esplendor do protagonista é ditado pela muralha de terror erguida pelo vilão. Um arqui-inimigo fraco engessa e castra o engrandecimento de quem tenta derrotá-lo. <strong>Para salvar um arco que parece raso e sem graça, amplifique a ruindade do antagonista e dobre a carga penal a cada novo encontro.</strong>","tip":"<strong>Modelo mental:</strong> a vitória do bem só arranca aplausos se o mal parecia realmente indestrutível e perfeitamente racional."},
      {"ic":"eye","t":"Não Pode os Sintomas Falsos","emph":"Sintomas","b":"Reescrever diálogos elegantes para consertar o marasmo do segundo ato é apenas colocar perfume pesado em material morto. <strong>A barriga narrativa não se trata com polimento de parágrafos; ela pede a faca da cirurgia bruta para arrancar passagens inteiras que não carregam a premissa de forma verdadeira.</strong>","tip":"<strong>Cuidado:</strong> pare de arrumar a pontuação de cenas inteiras que deveriam, na verdade, ser incendiadas sem dó."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 7",
  "lessons":["Reescrita é diagnóstico: nomeie o mal antes de tratá-lo.","Herói passivo, falar o enredo e vilão fraco são os suspeitos de sempre.","Para crescer o herói, engrandeça o vilão e torne as estacas primais."]},

 {"slug":"ch08-fade-in-final","sub":"CAPÍTULO 8: Fade In Final — Vender e Persistir",
  "intro":"Roteiro pronto é o começo da parte em que ele precisa ser vendido — e o autor, sobreviver à carreira.",
  "cards":[
      {"ic":"target","t":"O Teste do Pôster","emph":"Pôster","b":"A ideia só atinge a maturidade letal se couber numa imagem nítida com um título que venda e prometa a confusão por si só. <strong>Se a embalagem central do produto não explodir no escuro, não existe esforço artístico no recheio que vá resgatar a atenção e a carteira de ninguém nas ruas rápidas da cidade.</strong>","tip":"<strong>Como aplicar:</strong> construa a ponte comercial comparando de forma seca a sua obra a dois pilares do mercado. \"É X misturado com Y\" resolve e situa o leitor."},
      {"ic":"steps","t":"O Ofício Frio da Escrita","emph":"Ofício Frio","b":"Não há glória no amadorismo ofendido. O roteirista blindado possui bolsos forrados de novas premissas prontas para o disparo e recolhe críticas humilhantes sem misturar com o valor moral da sua pessoa. <strong>Rejeição bruta não é epitáfio criativo, é puramente um sintoma métrico de um mercado surdo ajustando as próprias contas da sua máquina caótica e insaciável.</strong>","tip":"<strong>Modelo mental:</strong> escreva continuamente e encare o descarte alheio apenas como pesquisa de terreno e não como veredito pessoal."},
      {"ic":"eye","t":"Venda o Gancho, Não as Cenas","emph":"Gancho","b":"Em prospecções agressivas, despejar relatórios minuciosos sobre enredos labirínticos atordoa e sepulta a vontade do ouvinte impaciente de forma irreversível e sem perdão. <strong>Você ganha os corações comercializando a espinha tensionada aguda e cortante do problema irresolvível central, deixando que o silêncio grite pelo desfecho genial oculto que ele vai pagar para descobrir se assinar embaixo do que ouviu ali.</strong>","tip":"<strong>Regra:</strong> não confunda a arte da defesa de pitch com o resumo maçante das minúcias de roteiro. Ancore as dores centrais cegas no estômago deles e cale."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 8",
  "lessons":["Título + pôster + logline são o teste final de clareza.","Pitch com gênero, ironia e comps; pare antes de cansar.","Carreira é persistência informada: muitas loglines, ouvir notas."]},
]
