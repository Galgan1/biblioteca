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
 "progress": "8 Capítulos Completos",
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
   {"ic":"target","t":"Os 4 Ingredientes","b":"<strong>Ironia</strong> (tensão na premissa), <strong>imagem mental</strong> completa do filme, <strong>público e custo</strong> implícitos e <strong>título</strong> que diz o que é. A ironia é o gancho.","tip":"<strong>Como aplicar:</strong> sem tensão interna, é sinopse, não logline.","wide":True},
   {"ic":"eye","t":"O Teste do Estranho","b":"Conte a logline para quem não te deve gentileza. Se os olhos não acendem, <strong>volte para a prancheta</strong> — antes de gastar meses de roteiro.","tip":"<strong>Modelo mental:</strong> venda o ingresso antes de construir o cinema."},
   {"ic":"gap","t":"Onde Falha","b":"\"Quando eu terminar você entende\" — se precisa do roteiro para explicar, a <strong>premissa falhou</strong>. Empilhar enredo não substitui uma tensão única e clara.","tip":"<strong>Cuidado:</strong> apaixonar-se cedo demais pula o teste que evita o desastre.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 1",
  "lessons":["Uma frase com ironia, imagem, público e título — antes da primeira cena.","Teste com estranhos; os olhos deles decidem.","Ideia que não vende em um minuto não melhora com 110 páginas."]},

 {"slug":"ch02-generos","sub":"CAPÍTULO 2: O Mesmo, Só Que Diferente — Os 10 Gêneros",
  "intro":"O público quer o conforto do familiar e a surpresa do novo ao mesmo tempo. A resposta é classificar pela transformação, não pelo cenário.",
  "cards":[
   {"ic":"book","t":"Transformação, Não Cenário","b":"Um filme no espaço pode ser terror (Monstro na Casa), sobrevivência (Cara com um Problema) ou Institucionalizado. O que define o gênero é <strong>o tipo de mudança contada</strong>.","tip":"<strong>Como aplicar:</strong> ache a família da sua história e estude os irmãos dela.","wide":True},
   {"ic":"layers","t":"As 10 Famílias","b":"Monstro na Casa, Velocino de Ouro, Lâmpada Mágica, Cara com um Problema, Ritos de Passagem, Amor de Camaradas, Por Que Foi Feito?, Triunfo do Tolo, Institucionalizado, Super-Herói.","tip":"<strong>Modelo mental:</strong> cada família tem regras que o público conhece de cor."},
   {"ic":"key","t":"\"O Mesmo, Só Que Diferente\"","b":"Honre a expectativa do gênero; <strong>surpreenda na execução</strong>. O esqueleto é emprestado; a torção é o seu trabalho.","tip":"<strong>Cuidado:</strong> \"meu filme não se parece com nada\" costuma significar \"não estudei com o que ele se parece\".","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 2",
  "lessons":["Gênero é o tipo de transformação, não o cenário.","Identifique a família, estude os clássicos, honre o esqueleto.","Entregue o familiar com uma torção — nunca só um dos dois."]},

 {"slug":"ch03-heroi","sub":"CAPÍTULO 3: É Sobre Um Cara Que… — O Herói",
  "intro":"O herói não é sagrado: é a peça que melhor serve à ideia. O certo amplifica a logline; o errado a desperdiça.",
  "cards":[
   {"ic":"target","t":"Herói a Serviço da Ideia","b":"Escolha o protagonista que <strong>maximiza o conflito</strong>, tem o <strong>arco mais longo</strong> (parte do ponto mais distante da lição) e é <strong>abraçável</strong> (o público se vê nele).","tip":"<strong>Como aplicar:</strong> se outro personagem serve melhor à premissa, troque — dói menos que um filme morno.","wide":True},
   {"ic":"spiral","t":"É Primal?","b":"Toda motivação que funciona é primal — sobreviver, proteger os seus, fome, amor, medo da morte. Se um <strong>homem das cavernas</strong> não entenderia o que está em jogo, as estacas são fracas.","tip":"<strong>Modelo mental:</strong> traduza o abstrato (carreira) no primal (família)."},
   {"ic":"eye","t":"Herói Passivo","b":"As coisas acontecem <strong>a</strong> ele, não <strong>por causa</strong> dele. Quem conduz é protagonista; quem assiste é figurante caro.","tip":"<strong>Cuidado:</strong> herói passivo é o primeiro defeito que a reescrita procura.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 3",
  "lessons":["Escolha o herói que maximiza conflito, arco e identificação.","Toda motivação que funciona é primal.","Herói conduz; se só reage do início ao fim, o roteiro tem dono errado."]},

 {"slug":"ch04-beat-sheet","sub":"CAPÍTULO 4: Vamos Marcar as Batidas — A Beat Sheet",
  "intro":"Toda história que funciona percorre 15 batidas reconhecíveis. A beat sheet é a gramática que o público já tem no ouvido.",
  "cards":[
   {"ic":"clock","t":"As 15 Batidas","b":"Imagem de Abertura, Tema Declarado, Apresentação, <strong>Catalisador</strong>, Debate, Virada p/ Ato 2, História B, <strong>Diversão e Jogos</strong>, <strong>Ponto Médio</strong>, Vilões Fecham o Cerco, <strong>Tudo Está Perdido</strong>, Noite Escura da Alma, Virada p/ Ato 3, Final, Imagem Final.","tip":"<strong>Chave:</strong> estrutura é forma, não fórmula — o soneto tem 14 versos e ninguém chama Camões de preguiçoso.","wide":True},
   {"ic":"spiral","t":"Promessa da Premissa","b":"<strong>Diversão e Jogos</strong> é onde a logline é paga — as cenas pelas quais o público comprou o ingresso. O <strong>Ponto Médio</strong> é falsa vitória/derrota; <strong>Tudo Está Perdido</strong> traz o \"cheiro de morte\".","tip":"<strong>Como aplicar:</strong> se o miolo não paga a premissa, o filme vira outro filme."},
   {"ic":"scale","t":"As Duas Regras","b":"<strong>Espelho:</strong> Imagem de Abertura e Final são o antes/depois — se iguais, não houve filme. <strong>Decisão:</strong> as viradas de ato são escolhas do herói, não empurrões.","tip":"<strong>Cuidado:</strong> Ato 3 resolvido por terceiros não fecha o arco (deus ex machina).","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 4",
  "lessons":["15 batidas, 3 atos, posições aproximadas — gramática, não algema.","Diversão e Jogos paga a promessa da premissa.","Abertura e Final são espelhos: a transformação tem que ser visível."]},

 {"slug":"ch05-o-quadro","sub":"CAPÍTULO 5: Construindo a Fera Perfeita — O Quadro",
  "intro":"Entre a beat sheet e o rascunho existe o Quadro: a história inteira visível de uma vez, onde mover uma cena custa um alfinete, não uma semana.",
  "cards":[
   {"ic":"layers","t":"4 Fileiras, ~40 Cartões","b":"Ato 1 · Ato 2-A (até o Ponto Médio) · Ato 2-B · Ato 3 — ~10 cartões por fileira. Dividir o Ato 2 pelo Ponto Médio <strong>mata o miolo infinito</strong>.","tip":"<strong>Como aplicar:</strong> fileira que incha denuncia história desequilibrada antes do rascunho.","wide":True},
   {"ic":"target","t":"Anatomia do Cartão","b":"Cada cena registra o <strong>conflito</strong> (>< quem quer o quê contra quem) e a <strong>carga emocional</strong> (+/− — entra num estado, sai noutro).","tip":"<strong>Modelo mental:</strong> cena sem conflito ou sem mudança de carga é informação fantasiada."},
   {"ic":"wrench","t":"Erre no Papelão","b":"Escrever é a etapa cara; planejar é a barata. Todo problema resolvido no Quadro custa <strong>1%</strong> do que custaria na página.","tip":"<strong>Cuidado:</strong> pular para o rascunho \"porque a inspiração veio\" mata o filme na página 60.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 5",
  "lessons":["4 fileiras, ~40 cartões, a história inteira visível antes da 1ª página.","Cada cartão: conflito (><) e mudança emocional (+/−).","Erre no papelão, não no roteiro."]},

 {"slug":"ch06-leis-fisica-roteiro","sub":"CAPÍTULO 6: As Leis Imutáveis da Física do Roteiro",
  "intro":"Um punhado de regras práticas que, quando obedecidas, ninguém nota; quando violadas, a história cai e ninguém sabe por quê.",
  "cards":[
   {"ic":"key","t":"Save the Cat","b":"Cedo, o herói faz algo <strong>genuinamente simpático</strong> — ajuda alguém, mostra coragem ou humor sob pressão. É o gesto que dá ao público uma razão para torcer, sobretudo se o herói tem falhas.","tip":"<strong>Como aplicar:</strong> simpatia ≠ bondade; basta um humano por quem valha torcer.","wide":True},
   {"ic":"wave","t":"Pope in the Pool","b":"Quando a exposição é inevitável, <strong>esconda-a sob algo divertido</strong> de assistir. O público engole o necessário sem sentir o gosto.","tip":"<strong>Modelo mental:</strong> exposição é dívida; pague-a sem cobrar tédio."},
   {"ic":"spiral","t":"Double Mumbo Jumbo","b":"O público aceita <strong>uma</strong> licença de magia por história, não duas. Um homem vira lobo, tudo bem; vira lobo <strong>e</strong> recebe alienígenas — perdeu a plateia. (E todos mudam, menos o vilão.)","tip":"<strong>Cuidado:</strong> somar sistemas fantásticos não é riqueza, é furo de credibilidade.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 6",
  "lessons":["Salve o gato cedo: compre a simpatia antes de cobrar paciência.","Esconda exposição sob ação; gaste só uma licença de magia.","Todos mudam, menos o vilão; e a ameaça tem que ser iminente."]},

 {"slug":"ch07-diagnostico","sub":"CAPÍTULO 7: O Que Há de Errado? — Diagnóstico",
  "intro":"Reescrever é diagnóstico, não \"mexer no texto até soar melhor\". Saber o nome do problema é metade da cura.",
  "cards":[
   {"ic":"target","t":"O Checklist","b":"Herói conduz (não passivo)? Dramatiza em vez de <strong>falar o enredo</strong>? <strong>Vilão forte</strong> e escalando? Estacas primais? Todos têm arco (menos o vilão)? Dá pra dizer o tema numa frase?","tip":"<strong>Como aplicar:</strong> trate a causa estrutural, não o sintoma de diálogo.","wide":True},
   {"ic":"sword","t":"Herói Tão Grande Quanto o Vilão","b":"O herói só é tão grande quanto o obstáculo. Para crescê-lo, <strong>engrandeça o adversário</strong> — \"make the bad guy badder\", escalando a cada ato.","tip":"<strong>Modelo mental:</strong> vilão fraco = filme sem tensão."},
   {"ic":"eye","t":"Sintoma vs. Causa","b":"\"O segundo ato arrasta\" é sintoma; a causa pode ser herói passivo, vilão fraco ou Diversão e Jogos fora da premissa.","tip":"<strong>Cuidado:</strong> polir frases de uma cena que não deveria existir é maquiar osso quebrado.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 7",
  "lessons":["Reescrita é diagnóstico: nomeie o mal antes de tratá-lo.","Herói passivo, falar o enredo e vilão fraco são os suspeitos de sempre.","Para crescer o herói, engrandeça o vilão e torne as estacas primais."]},

 {"slug":"ch08-fade-in-final","sub":"CAPÍTULO 8: Fade In Final — Vender e Persistir",
  "intro":"Roteiro pronto é o começo da parte em que ele precisa ser vendido — e o autor, sobreviver à carreira.",
  "cards":[
   {"ic":"target","t":"Título + Pôster + Pitch","b":"Se você imagina o <strong>pôster</strong> e o <strong>título diz o que é</strong>, a premissa é clara. No pitch: comece pelo gênero, entregue a logline com ironia, ancore com comparáveis (<strong>\"é X encontra Y\"</strong>) e pare.","tip":"<strong>Como aplicar:</strong> se não cabe no pôster, não cabe na cabeça do público.","wide":True},
   {"ic":"steps","t":"Disciplina de Carreira","b":"Escrever sempre, ter <strong>várias loglines no bolso</strong>, ouvir notas sem ego e tratar rejeição como dado, não veredito.","tip":"<strong>Modelo mental:</strong> a diferença entre quem publica e quem não publica raramente é talento — é persistência informada."},
   {"ic":"eye","t":"Pitch-Enredo","b":"Contar o filme cena a cena em vez de <strong>vender a tensão central</strong> perde o ouvinte no segundo ato.","tip":"<strong>Cuidado:</strong> defender em vez de ouvir notas mata a reescrita e a relação.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 8",
  "lessons":["Título + pôster + logline são o teste final de clareza.","Pitch com gênero, ironia e comps; pare antes de cansar.","Carreira é persistência informada: muitas loglines, ouvir notas."]},
]
