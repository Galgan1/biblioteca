# -*- coding: utf-8 -*-
"""Conteúdo (pt-BR) das páginas da biblioteca para 'A Coragem de Não Agradar'
(Ichiro Kishimi & Fumitake Koga — The Courage to Be Disliked), sobre a psicologia
individual de Alfred Adler. Diálogo Filósofo × Jovem em 5 noites.
Frameworks canônicos: teleologia vs. etiologia ('o trauma não existe'); todo
problema é interpessoal; sentimento × complexo de inferioridade/superioridade;
a separação de tarefas ('de quem é a tarefa?'); o desejo de reconhecimento como
armadilha; relações horizontais (encorajar, não elogiar); sentimento de comunidade
(Gemeinschaftsgefühl); a tríade autoaceitação + confiança + contribuição; o aqui
e agora; a coragem de ser desprezado. Base: frameworks amplamente documentados —
não reproduz o texto."""

BOOK = {
 "title": "A Coragem de Não Agradar",
 "author": "Ichiro Kishimi & Fumitake Koga",
 "header_light": "A CORAGEM DE",
 "header_bold": "NÃO AGRADAR",
 "subtitle": "VISÃO GERAL · A PSICOLOGIA DE ADLER EM DIÁLOGO",
 "intro": "Um diálogo socrático entre um Filósofo e um Jovem cético, ao longo de cinco noites. O Filósofo defende a psicologia de Alfred Adler — quase esquecida ao lado de Freud e Jung. A tese choca: o passado não nos determina, todo problema é de relações interpessoais, e a felicidade é uma escolha de coragem. A coragem de ser livre — e, portanto, de ser desprezado por alguém.",
 "description": "O fenômeno japonês de Kishimi e Koga que popularizou Alfred Adler pelo mundo. Em forma de diálogo, vira do avesso a ideia de que somos reféns do trauma: vivemos por objetivos, não por causas. Ensina a separação de tarefas, a sair da armadilha do reconhecimento e a sustentar a felicidade na tríade autoaceitação, confiança e contribuição — a verdadeira coragem de não agradar.",
 "tags": ["Psicologia", "Adler", "Autoconhecimento"],
 "progress": "9 Capítulos",
 "cover": "assets/coragem-de-nao-agradar-cover.png",
 "overview_cards": [
   {"ic":"fork","t":"Teleologia vs. Etiologia — \"o trauma não existe\"","b":"Freud explica pela <strong>causa</strong> passada ('você é assim por causa de…'); Adler, pelo <strong>objetivo</strong> presente ('você age assim para conseguir algo'). A experiência não determina — nós damos significado a ela. O 'trauma não existe' não nega a dor: nega que ela nos <strong>obrigue</strong> a um destino.","tip":"<strong>Modelo mental:</strong> pergunte 'para quê?', não 'por quê?'. A causa prende; o objetivo liberta.","wide":True},
   {"ic":"scale","t":"A Separação de Tarefas","b":"A chave de quase todo conflito é uma pergunta: <strong>'de quem é a tarefa?'</strong>. Critério: <strong>quem arca com as consequências</strong>. Cuide da sua, não invada a do outro — nem deixe invadirem a sua. O que os outros pensam de você é <strong>tarefa deles</strong>.","tip":"<strong>Como aplicar:</strong> antes de se meter num conflito, identifique o dono da tarefa pelas consequências.","wide":True},
   {"ic":"sword","t":"A Coragem de Ser Desprezado","b":"Viver para satisfazer expectativas alheias é viver a vida dos outros. O desejo de reconhecimento é uma armadilha. A liberdade tem preço: aceitar ser, eventualmente, <strong>malvisto por alguém</strong>. Não buscar ser desprezado — mas não temer sê-lo.","tip":"<strong>Regra:</strong> se ninguém nunca te desaprova, talvez você não esteja vivendo a sua vida."},
   {"ic":"constellation","t":"A Tríade da Felicidade","b":"A coragem se ergue sobre três pilares: <strong>autoaceitação</strong> (aceitar o que não dá), <strong>confiança nos outros</strong> (sem condições) e <strong>contribuição</strong> ('sou útil'). É sentir-se útil — não ser aprovado — que dá valor a si mesmo.","tip":"<strong>Modelo mental:</strong> aceitar-se → confiar → contribuir → sentir-se útil → aceitar-se mais."},
 ],
}

CHAPTERS = [
 {"slug":"ch01-trauma-nao-existe","sub":"PRIMEIRA NOITE: O Trauma Não Existe",
  "intro":"O passado não nos determina. Adler explica a conduta pelo objetivo presente (teleologia), não pela causa passada (etiologia). Por isso o Filósofo provoca: o trauma não existe no sentido de uma causa que nos prende — somos nós que damos significado à experiência.",
  "cards":[
   {"ic":"fork","t":"Teleologia vs. Etiologia","b":"Freud olha a <strong>causa</strong> ('você é assim por causa do que aconteceu') — determinista, fecha o futuro. Adler olha o <strong>objetivo</strong> ('você age assim para um fim atual') — o passado vira matéria-prima, não sentença.","tip":"<strong>Como aplicar:</strong> ao dizer 'não posso por causa de X', troque por 'qual objetivo o \"não posso\" serve?'."},
   {"ic":"key","t":"O Significado da Experiência","b":"A experiência em si não causa o resultado: o que decide é o <strong>significado</strong> que damos a ela. Pessoas com o mesmo passado seguem caminhos opostos — logo, não somos determinados pelo que vivemos.","tip":"<strong>Modelo mental:</strong> os mesmos tijolos constroem prisões ou casas. O passado é matéria, não destino."},
   {"ic":"eye","t":"\"O Trauma Não Existe\"","b":"Não é negar que coisas dolorosas aconteceram — é negar que elas nos <strong>obriguem</strong> a um destino. Por trás de todo 'não posso' mora um objetivo que o 'não posso' protege (evitar risco, ser cuidado, não mudar).","tip":"<strong>Cuidado:</strong> 'não existe' não significa 'não importa' — significa 'não te prende'.","warn":True},
  ],
  "lessons_title":"Lições-Chave da Primeira Noite (I)",
  "lessons":["Não é o que te aconteceu que decide, mas o sentido que você dá.","Por trás de todo 'não posso' há um objetivo que ele protege.","Aceitar a teleologia é assumir que a mudança é possível agora."]},

 {"slug":"ch02-objetivo-e-estilo-de-vida","sub":"PRIMEIRA NOITE: Objetivos, Emoções e Estilo de Vida",
  "intro":"As emoções não nos dominam — nós as fabricamos a serviço de um objetivo. E o que chamamos de 'personalidade' é um estilo de vida que escolhemos, e que por isso pode ser reescolhido. O que falta para mudar não é capacidade: é coragem.",
  "cards":[
   {"ic":"spark","t":"A Emoção é Ferramenta, não Senhor","b":"Raiva, medo e tristeza são <strong>criados</strong> para atingir um fim, não causas que nos arrastam. A mãe que grita com a filha atende a escola com voz calma e volta a gritar: ela <strong>liga e desliga</strong> a raiva conforme o interlocutor.","tip":"<strong>Como aplicar:</strong> ao se sentir 'tomado', pergunte 'o que estou tentando conseguir gritando (ou me calando)?'."},
   {"ic":"pivot","t":"Estilo de Vida (e a Re-escolha)","b":"'Estilo de vida' é o termo de Adler para personalidade/caráter — escolhido por volta dos 10 anos e, por ser escolhido, <strong>re-escolhível agora</strong>. Não é 'eu sou tímido'; é 'eu tenho usado a timidez para…'.","tip":"<strong>Modelo mental:</strong> você não 'tem' um temperamento fixo; você 'usa' um estilo — e pode trocar."},
   {"ic":"sword","t":"A Coragem de Mudar","b":"As pessoas não mudam porque o estilo atual, apesar das queixas, é <strong>conhecido e confortável</strong>; o novo é desconhecido. O obstáculo não é a falta de capacidade — é a falta de coragem de abrir mão do familiar.","tip":"<strong>Cuidado:</strong> a inércia é uma escolha ativa, não ausência de escolha.","warn":True},
  ],
  "lessons_title":"Lições-Chave da Primeira Noite (II)",
  "lessons":["Você fabrica a emoção para um fim; ela não te governa.","'Personalidade' é estilo de vida escolhido — e re-escolhível agora.","O que falta para mudar não é capacidade, é coragem."]},

 {"slug":"ch03-todo-problema-interpessoal","sub":"SEGUNDA NOITE: Todo Problema é Interpessoal",
  "intro":"Não existe sofrimento puramente individual: toda angústia humana — inclusive a inferioridade — nasce das relações com os outros. Sentir-se inferior é saudável; o que adoece é transformar isso em desculpa ou em fachada de superioridade.",
  "cards":[
   {"ic":"link","t":"Todo Problema é Interpessoal","b":"Solidão, ansiedade, vergonha e inferioridade só fazem sentido porque existem <strong>outras pessoas</strong>. Num universo vazio, nenhum desses sofrimentos existiria. Por isso a saída também passa pelas relações.","tip":"<strong>Modelo mental:</strong> não há sofrimento numa ilha deserta — e tampouco há cura sozinho."},
   {"ic":"layers","t":"Sentimento × Complexo","b":"O <strong>sentimento de inferioridade</strong> é subjetivo, universal e saudável (combustível). O <strong>complexo de inferioridade</strong> usa a inferioridade como <strong>álibi</strong> ('se eu não fosse X, conseguiria Y'). Sempre desconfie da estrutura 'A, então não posso B'.","tip":"<strong>Como aplicar:</strong> inferioridade é gasolina, não defeito — o problema é o que você faz com ela.","wide":True},
   {"ic":"mask","t":"Complexo de Superioridade","b":"Fingir-se superior para esconder a inferioridade não enfrentada: gabar-se, exibir poder/conquistas — ou, paradoxalmente, exibir as próprias <strong>desgraças</strong> ('ninguém sofre como eu') para dominar a relação.","tip":"<strong>Sinal de alerta:</strong> quanto mais alguém se gaba (ou ostenta sofrimento), mais insegurança costuma esconder.","warn":True},
   {"ic":"target","t":"Superar a Si Mesmo, não aos Outros","b":"A meta sadia é a busca de superioridade <strong>sobre o eu de ontem</strong>, não sobre os outros. Comparar-se com os outros fabrica inimigos onde poderia haver companheiros.","tip":"<strong>Regra:</strong> a única régua legítima é você mesmo, ontem."},
  ],
  "lessons_title":"Lições-Chave da Segunda Noite (I)",
  "lessons":["Todo problema, no fundo, é de relação — não há angústia numa ilha deserta.","Sentir-se inferior é saudável; usá-lo como desculpa (complexo) é fuga.","Quem se gaba ou exibe a própria desgraça está escondendo inferioridade."]},

 {"slug":"ch04-competicao-e-poder","sub":"SEGUNDA NOITE: Competição e Lutas de Poder",
  "intro":"Quando a vida vira competição, o mundo vira campo de batalha e todos viram inimigos. Sair da competição — e recusar-se a entrar em lutas de poder — transforma os outros de rivais em companheiros.",
  "cards":[
   {"ic":"mountain","t":"A Vida Não é Competição","b":"Basta caminhar para frente, sem comparar-se com ninguém. Quem compete vive medindo a vitória pela derrota alheia e nunca descansa — e converte cada conquista do outro em ferida própria.","tip":"<strong>Modelo mental:</strong> sem competição, o mundo se enche de companheiros em vez de inimigos."},
   {"ic":"sword","t":"Não Entre no Ringue","b":"Quando alguém ataca ou provoca, busca uma <strong>luta de poder</strong> para 'vencer'. A saída adleriana é não entrar no ringue. Mesmo que você 'ganhe' a discussão, a relação perde e a vingança se arma.","tip":"<strong>Como aplicar:</strong> separe 'ter razão' de 'fazer o outro admitir que está errado' — buscar o segundo é entrar na guerra.","warn":True},
   {"ic":"scale","t":"Reconhecer o Erro não é Derrota","b":"Admitir um equívoco, pedir desculpas ou sair de uma briga <strong>não</strong> são 'perder'. Quem precisa vencer toda discussão está preso numa luta de poder — recuar da briga não é recuar da verdade.","tip":"<strong>Regra:</strong> admitir erro é força; a derrota real é ficar refém do orgulho."},
  ],
  "lessons_title":"Lições-Chave da Segunda Noite (II)",
  "lessons":["Saia da competição: a régua é você de ontem, não o outro.","Diante da provocação, recuse a luta de poder — não entre no ringue.","Admitir erro ou desculpar-se é força, não derrota."]},

 {"slug":"ch05-separacao-de-tarefas","sub":"TERCEIRA NOITE: A Separação de Tarefas",
  "intro":"A chave prática para desembaraçar quase todo conflito interpessoal é uma pergunta só: 'de quem é a tarefa?'. Cuide da sua e não invada a do outro — nem deixe que invadam a sua.",
  "cards":[
   {"ic":"scale","t":"\"De Quem é a Tarefa?\"","b":"Antes de agir num conflito, pergunte de quem é a tarefa. Critério decisivo: <strong>quem arca, em última instância, com as consequências</strong>? Esse é o dono. Faça só a sua parte; não invada a do outro; não deixe invadirem a sua.","tip":"<strong>Como aplicar:</strong> quase toda dor interpessoal vem de invadir tarefa alheia ou deixar invadirem a sua.","wide":True},
   {"ic":"leaf","t":"Não Intervir na Tarefa Alheia","b":"Você pode oferecer ajuda quando pedido e deixar claro que está disponível — mas a decisão e a execução pertencem ao <strong>dono</strong>. 'Você pode levar o cavalo à água, mas não pode obrigá-lo a beber.'","tip":"<strong>Cuidado:</strong> separar tarefas não é abandono — é respeitar a fronteira e ajudar quando solicitado.","warn":True},
   {"ic":"key","t":"O Juízo dos Outros é Tarefa Deles","b":"O que os outros pensam de você é <strong>tarefa deles</strong>: você não pode controlá-lo e não precisa carregá-lo. Esta é a base da liberdade — e a porta para a coragem de ser desprezado.","tip":"<strong>Regra:</strong> faça a sua tarefa com retidão; o veredito alheio não é seu fardo."},
  ],
  "lessons_title":"Lições-Chave da Terceira Noite (I)",
  "lessons":["Em todo conflito, pergunte primeiro: 'de quem é a tarefa?'.","O dono é quem arca com as consequências — faça a sua, não invada a alheia.","O que os outros pensam de você é tarefa deles; libere-se desse peso."]},

 {"slug":"ch06-liberdade-e-reconhecimento","sub":"TERCEIRA NOITE: Liberdade e a Coragem de Ser Desprezado",
  "intro":"Buscar reconhecimento é uma armadilha: quem vive para satisfazer expectativas alheias vive a vida dos outros. A liberdade tem um preço — e esse preço é a coragem de ser desprezado por alguém.",
  "cards":[
   {"ic":"gap","t":"O Desejo de Reconhecimento é Armadilha","b":"Querer aprovação leva a moldar-se às expectativas dos outros, abrindo mão da própria vida — e ainda faz você <strong>exigir</strong> que os outros correspondam às suas. Você não nasceu para corresponder à expectativa de ninguém.","tip":"<strong>Sinal de alerta:</strong> decidir pelo 'o que vão achar?' em vez de 'qual é minha tarefa?'.","warn":True},
   {"ic":"sword","t":"A Coragem de Ser Desprezado","b":"Ser livre é aceitar a possibilidade de ser malvisto por alguém. Não <strong>buscar</strong> ser desprezado — mas não <strong>temer</strong> sê-lo. Sem essa coragem, não há liberdade nem felicidade. É daí que vem o título.","tip":"<strong>Modelo mental:</strong> se ninguém nunca te desaprova, talvez você não esteja vivendo a sua vida."},
   {"ic":"lens","t":"A Regra das Dez Pessoas","b":"Por mais íntegro que você seja, de cada dez <strong>uma</strong> vai te desprezar, uma ou duas serão amigas verdadeiras, e o resto é neutro. Focar no desaprovador e tentar convertê-lo sacrifica a própria vida — e ainda falha.","tip":"<strong>Como aplicar:</strong> a aprovação do outro é tarefa dele; não a gerencie. Viva para quem importa."},
  ],
  "lessons_title":"Lições-Chave da Terceira Noite (II)",
  "lessons":["Viver para a aprovação alheia é viver a vida dos outros.","Liberdade tem preço: ser, eventualmente, desprezado — e seguir em frente.","O juízo do outro sobre você é tarefa dele; a sua é viver com retidão."]},

 {"slug":"ch07-relacoes-horizontais","sub":"QUARTA NOITE: Relações Horizontais — Encorajar, Não Elogiar",
  "intro":"Elogio e punição são manipulação vertical (de cima para baixo). Adler propõe relações horizontais — 'diferentes, mas iguais' — e, no lugar do elogio, o encorajamento.",
  "cards":[
   {"ic":"layers","t":"Vertical × Horizontal","b":"A relação <strong>vertical</strong> é hierarquia de valor: alguém julga, premia e pune o outro — gera dependência. A <strong>horizontal</strong> é 'diferentes, mas iguais': ninguém está acima de ninguém em valor, mesmo com papéis distintos.","tip":"<strong>Como aplicar:</strong> trate filho, subordinado ou parceiro como iguais em valor — colabore, não comande de cima.","wide":True},
   {"ic":"bubble","t":"Encorajar, não Elogiar","b":"O elogio ('muito bem!') é um veredito de cima para baixo que cria dependência da aprovação. Em vez dele, <strong>agradeça</strong>: 'obrigado, isso me ajudou'. O foco sai do julgamento e vai para a contribuição entre iguais.","tip":"<strong>Regra:</strong> diga 'obrigado', não 'muito bem'. O agradecimento é horizontal; o elogio, vertical."},
   {"ic":"spark","t":"O Valor Vem de \"Sou Útil\"","b":"A criança que ajuda e ouve 'obrigado, você me ajudou' não aprende a caçar elogio — aprende que <strong>é útil</strong>. E é esse senso de utilidade, não o elogio, que constrói coragem e valor próprio.","tip":"<strong>Cuidado:</strong> encorajar ≠ bajular; reconheça contribuição real, não elogio vazio para controlar.","warn":True},
  ],
  "lessons_title":"Lições-Chave da Quarta Noite (I)",
  "lessons":["Troque relações verticais (premiar/punir) por horizontais ('diferentes, mas iguais').","Em vez de elogiar, encoraje: agradeça e reconheça a contribuição.","O valor próprio nasce de 'sou útil', não de 'fui aprovado'."]},

 {"slug":"ch08-sentimento-de-comunidade","sub":"QUARTA NOITE: O Sentimento de Comunidade",
  "intro":"A bússola de Adler para boas relações é o sentimento de comunidade (Gemeinschaftsgefühl): deslocar o foco do apego a si mesmo para o interesse pelos outros, sentindo-se parte de algo maior.",
  "cards":[
   {"ic":"constellation","t":"Gemeinschaftsgefühl","b":"Sentir os outros como <strong>companheiros</strong> e a si mesmo como <strong>parte</strong> de uma comunidade. É o objetivo final das relações segundo Adler — e onde 'todo problema é interpessoal' encontra a cura: o sofrimento das relações se resolve <strong>nas</strong> relações.","tip":"<strong>Modelo mental:</strong> mude de 'o centro sou eu' para 'sou parte do todo'.","wide":True},
   {"ic":"pivot","t":"Do Apego a Si ao Interesse pelos Outros","b":"Quem vive em 'como me veem? o que ganho?' está preso no eu, e exige que tudo gire em torno de si. A virada: trocar 'o que esta pessoa faz por mim?' por <strong>'o que eu posso dar a esta comunidade?'</strong>.","tip":"<strong>Como aplicar:</strong> você é membro da comunidade, não o seu centro."},
   {"ic":"steps","t":"Escute a Comunidade Maior","b":"Quando um vínculo (emprego, escola, casamento) parece prisão, lembre que é só <strong>uma</strong> comunidade entre muitas. Há sempre uma 'comunidade maior' (a humanidade, a sociedade, o futuro) — ouvi-la devolve a liberdade de discordar, mudar ou sair.","tip":"<strong>Cuidado:</strong> tratar um grupo pequeno como o mundo inteiro é o que sufoca.","warn":True},
  ],
  "lessons_title":"Lições-Chave da Quarta Noite (II)",
  "lessons":["A meta das relações é o sentimento de comunidade: sentir-se parte, ver os outros como companheiros.","Saia do apego a si (o centro) para o interesse pelos outros (a parte do todo).","Quando um grupo aprisiona, escute a comunidade maior — ela devolve a liberdade."]},

 {"slug":"ch09-aqui-e-agora","sub":"QUINTA NOITE: A Tríade e o Viver o Aqui e Agora",
  "intro":"A coragem de ser feliz se sustenta em três pilares — autoaceitação, confiança nos outros e contribuição — e se realiza vivendo intensamente o aqui e agora, não num futuro idealizado.",
  "cards":[
   {"ic":"constellation","t":"A Tríade da Coragem","b":"<strong>Autoaceitação</strong> — aceitar o 'eu que não consegue' (≠ autoafirmação): mude o mutável, aceite o imutável. <strong>Confiança incondicional</strong> — confiar sem garantias (trair é tarefa do outro). <strong>Contribuição</strong> — agir pelo bem da comunidade.","tip":"<strong>Como aplicar:</strong> aceito-me → confio → contribuo → sinto-me útil → aceito-me mais. O ciclo se realimenta.","wide":True},
   {"ic":"spark","t":"O Valor Vem de Contribuir","b":"Contribuir é o que dá o <strong>sentido de valor</strong> ('sou útil para alguém') — a fonte real do valor próprio, não a aprovação. Foque em 'como usar o que tenho', não em 'o que eu tenho'.","tip":"<strong>Regra:</strong> sentir-se útil sustenta a coragem; caçar aprovação a corrói."},
   {"ic":"clock","t":"Viva o Aqui e Agora","b":"A vida não é uma reta rumo a um pico futuro: é uma <strong>série de instantes</strong>, como uma dança. Não existe 'vida em preparação'. Adiar a felicidade para 'quando eu conseguir X' é não viver.","tip":"<strong>Cuidado:</strong> fixar-se no passado (trauma) ou no futuro (metas) escurece o único lugar onde se vive — aqui.","warn":True},
   {"ic":"constellation","t":"A Estrela-Guia","b":"Basta apontar para a estrela-guia da <strong>contribuição aos outros</strong>; enquanto se caminha em sua direção, qualquer instante já é pleno — mesmo sem chegar a lugar nenhum. O sentido da vida é o que você dá a ela.","tip":"<strong>Modelo mental:</strong> dance a vida; não a corra como maratona até a linha de chegada."},
  ],
  "lessons_title":"Lições-Chave da Quinta Noite",
  "lessons":["A coragem se ergue sobre a tríade: aceitar-se, confiar nos outros, contribuir.","Contribuir (sentir-se útil) é a fonte real do valor próprio — não a aprovação.","A vida é série de instantes: viva o aqui e agora, com a contribuição por estrela-guia."]},
]
