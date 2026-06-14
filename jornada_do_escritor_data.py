# -*- coding: utf-8 -*-
"""Conteúdo (pt-BR) das páginas da biblioteca para 'A Jornada do Escritor'
(The Writer's Journey) de Christopher Vogler. Estrutura mítica para roteiro:
os 12 estágios da Jornada do Herói e os 8 arquétipos."""

BOOK = {
 "title": "A Jornada do Escritor",
 "author": "Christopher Vogler",
 "header_light": "A JORNADA DO",
 "header_bold": "ESCRITOR",
 "subtitle": "VISÃO GERAL · A ESTRUTURA MÍTICA PARA ROTEIRISTAS",
 "intro": "Christopher Vogler traduziu o monomito de Joseph Campbell para a linguagem do roteiro. Sob a infinita variedade das histórias, há um único padrão — a Jornada do Herói — porque ele descreve a forma da transformação humana. Vogler organiza esse padrão em 12 estágios e 8 arquétipos, ferramentas para escrever (e diagnosticar) qualquer narrativa, do mito épico ao drama doméstico.",
 "description": "A adaptação de Christopher Vogler do monomito de Campbell para roteiristas: os 12 estágios da Jornada do Herói e os 8 arquétipos como funções psicológicas — uma bússola flexível para a estrutura de qualquer história.",
 "tags": ["Roteiro", "Mito", "Ofício"],
 "progress": "10 Capítulos Completos",
 "cover": "assets/jornada-do-escritor-cover.png",
 "overview_cards": [
   {"ic":"spiral","t":"A Jornada do Herói — 12 Estágios","b":"O padrão universal em três atos: <strong>Partida</strong> (Mundo Comum → Travessia do Limiar), <strong>Iniciação</strong> (Provas → Recompensa) e <strong>Retorno</strong> (Caminho de Volta → Elixir). É bússola flexível, não fórmula rígida.","tip":"<strong>Como aplicar:</strong> comprima, mova ou subverta estágios — o público reconhece o padrão no osso.","wide":True},
   {"ic":"layers","t":"Os 8 Arquétipos","b":"Funções psicológicas, não tipos fixos: <strong>Herói, Mentor, Guardião do Limiar, Arauto, Camaleão, Sombra, Pícaro, Aliado</strong>. Um mesmo personagem pode vestir várias máscaras.","tip":"<strong>Modelo mental:</strong> pergunte que função a cena precisa, não que personagem colocar."},
   {"ic":"key","t":"Morte, Renascimento e Elixir","b":"No centro, a <strong>Provação</strong> mata e ressuscita o herói; no clímax, a <strong>Ressurreição</strong> prova a mudança; no fim, ele volta com o <strong>Elixir</strong> que cura o mundo de onde partiu.","tip":"<strong>Chave:</strong> transformação que não volta para casa é incompleta."},
 ],
}

CHAPTERS = [
 {"slug":"ch01-monomito-arquetipos","sub":"CAPÍTULO 1: O Monomito e os Arquétipos",
  "intro":"Campbell encontrou um único padrão sob todas as histórias; Vogler o traduziu para o roteiro. Junto vêm os arquétipos — funções psicológicas recorrentes.",
  "cards":[
   {"ic":"spiral","t":"O Monomito","b":"Um herói parte do mundo conhecido, atravessa um limiar, enfrenta provações e uma <strong>crise de morte/renascimento</strong>, conquista uma recompensa e retorna transformado, trazendo algo que beneficia os outros.","tip":"<strong>Como aplicar:</strong> o mundo externo da jornada espelha o conflito interno do herói.","wide":True},
   {"ic":"layers","t":"Arquétipo = Função","b":"Cada arquétipo é um <strong>papel que a narrativa precisa</strong> — uma energia psicológica —, não um personagem fixo. Personagens são máscaras que esses arquétipos vestem.","tip":"<strong>Modelo mental:</strong> um personagem pode trocar de máscara ao longo do arco."},
   {"ic":"eye","t":"Bússola, Não Trilho","b":"A estrutura pode ser comprimida, reordenada, repetida ou subvertida sem perder o efeito. Tratá-la como <strong>checklist rígido</strong> mata o orgânico.","tip":"<strong>Cuidado:</strong> arquétipo como estereótipo (\"o velho sábio barbudo\") engessa o elenco.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 1",
  "lessons":["O monomito é o mapa universal da transformação, não fórmula de gênero.","Arquétipos são funções; personagens são máscaras que as vestem.","Use a estrutura como bússola flexível."]},

 {"slug":"ch02-mundo-comum-chamado","sub":"CAPÍTULO 2: Mundo Comum e o Chamado à Aventura",
  "intro":"Toda jornada começa no Mundo Comum — o 'antes', que mostra o que falta ao herói. Então o Chamado rompe o equilíbrio.",
  "cards":[
   {"ic":"book","t":"Mundo Comum","b":"A linha de base contra a qual mediremos a transformação. Mostre a rotina, a falha e a <strong>ferida</strong> que a aventura virá desafiar ou curar.","tip":"<strong>Como aplicar:</strong> você só sente a viagem se viu a casa.","wide":True},
   {"ic":"wave","t":"O Chamado","b":"A perturbação que apresenta o problema ou desafio e <strong>encerra a possibilidade</strong> de seguir como antes. Fecha a porta de trás.","tip":"<strong>Modelo mental:</strong> um evento que o herói pode ignorar sem custo não é chamado, é convite."},
   {"ic":"target","t":"O Arauto","b":"A força que entrega o Chamado — pessoa, notícia ou mudança de circunstância. <strong>Anuncia que a mudança chegou.</strong>","tip":"<strong>Cuidado:</strong> Mundo Comum longo demais faz o público embarcar tarde.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 2",
  "lessons":["O Mundo Comum estabelece quem o herói é e o que lhe falta.","O Chamado rompe o equilíbrio e encerra o 'como sempre'.","O Arauto — pessoa, notícia ou evento — traz o Chamado."]},

 {"slug":"ch03-recusa-mentor","sub":"CAPÍTULO 3: Recusa do Chamado e o Encontro com o Mentor",
  "intro":"Entre o Chamado e a aventura há a Recusa — a hesitação que torna humana a coragem. E entra o Mentor, que arma o herói.",
  "cards":[
   {"ic":"clock","t":"A Recusa","b":"A manifestação do medo: o herói recua, ou alguém alerta do perigo. <strong>Ninguém hesita diante do que é fácil</strong> — a Recusa prova que a aposta é real.","tip":"<strong>Como aplicar:</strong> coragem só existe contra o medo.","wide":True},
   {"ic":"key","t":"O Mentor","b":"A fonte de <strong>sabedoria, treino ou dom</strong> que arma o herói para o limiar. Representa o eu superior — e depois se retira.","tip":"<strong>Modelo mental:</strong> o Mentor abre a porta; quem atravessa é o herói."},
   {"ic":"eye","t":"Mentor Onipotente","b":"Se o Mentor pode resolver, por que o herói? <strong>O dom é meio, não substituto da ação.</strong>","tip":"<strong>Cuidado:</strong> mentor que resolve tudo rouba o arco do protagonista.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 3",
  "lessons":["A Recusa expõe o medo e torna a coragem humana.","O Mentor arma o herói com dom, treino ou conselho — e se retira.","O dom é meio para a ação do herói, nunca substituto dela."]},

 {"slug":"ch04-travessia-limiar","sub":"CAPÍTULO 4: A Travessia do Primeiro Limiar",
  "intro":"O herói se compromete e cruza para o Mundo Especial. É o ponto sem retorno que abre o Ato 2.",
  "cards":[
   {"ic":"steps","t":"O Comprometimento","b":"O herói entra no desconhecido por vontade própria, aceitando suas regras e perigos. Depois do limiar, <strong>o mundo antigo se fecha</strong>.","tip":"<strong>Como aplicar:</strong> cruzar o limiar é assinar o contrato da aventura.","wide":True},
   {"ic":"gap","t":"O Guardião do Limiar","b":"A força que bloqueia a passagem e <strong>testa o comprometimento</strong>. Não é o vilão final — é o filtro de quem não está pronto.","tip":"<strong>Modelo mental:</strong> guardiões não são para derrotar, e sim para passar (vencer, contornar ou converter)."},
   {"ic":"eye","t":"Limiar Morno","b":"Passagem sem peso nem risco <strong>não sinaliza o ponto sem retorno</strong>. E herói sempre empurrado segue passivo no Ato 2.","tip":"<strong>Cuidado:</strong> tratar o Guardião como batalha final gasta o clímax cedo.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 4",
  "lessons":["A Travessia é o comprometimento que abre o Ato 2.","O Guardião testa o preparo; supere, contorne ou converta.","Idealmente o herói escolhe cruzar, firmando-se como agente."]},

 {"slug":"ch05-provas-aliados-inimigos","sub":"CAPÍTULO 5: Provas, Aliados e Inimigos",
  "intro":"No Mundo Especial, o herói aprende as novas regras, ganha aliados e identifica inimigos — a parte expansiva do Ato 2.",
  "cards":[
   {"ic":"target","t":"Provas","b":"Desafios menores que <strong>treinam o herói</strong>, revelam seu caráter e elevam as estacas. São o aquecimento para a Provação.","tip":"<strong>Como aplicar:</strong> o meio do Ato 2 é uma escola; cada prova é uma aula com nota.","wide":True},
   {"ic":"layers","t":"Aliados e a Sombra","b":"O herói descobre em quem confiar (<strong>Aliado</strong>) e quem temer (<strong>Sombra</strong>, a oposição). O Camaleão semeia dúvida; o Pícaro alivia a tensão.","tip":"<strong>Modelo mental:</strong> a melhor Sombra é um espelho — mostra o que o herói poderia se tornar."},
   {"ic":"eye","t":"Provas Avulsas","b":"Desafios que <strong>não escalam nem ensinam</strong> viram enchimento; aliados sem função tornam o time decorativo.","tip":"<strong>Cuidado:</strong> inimigo sem relação com a falha do herói desperdiça o tema.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 5",
  "lessons":["Provas treinam o herói e elevam as estacas rumo à Provação.","Aliados e Inimigos definem o time e dão forma à Sombra.","A Sombra mais potente espelha o herói."]},

 {"slug":"ch06-aproximacao-provacao","sub":"CAPÍTULO 6: Aproximação e a Provação",
  "intro":"O herói chega à caverna mais profunda e enfrenta a Provação: a crise central, um confronto com a morte do qual renasce mudado.",
  "cards":[
   {"ic":"spiral","t":"A Provação","b":"O ponto médio dramático, o confronto supremo. O herói <strong>toca o fundo</strong>, encara seu maior medo e parece morrer — para então renascer. É a fonte da magia da história.","tip":"<strong>Como aplicar:</strong> sem morte, sem ressurreição — algo no herói precisa acabar.","wide":True},
   {"ic":"key","t":"Morte e Renascimento","b":"O herói experimenta uma <strong>morte simbólica</strong> (perda, fracasso, escuridão) e emerge transformado. O público morre e ressuscita com ele.","tip":"<strong>Modelo mental:</strong> a Provação é o centro de gravidade — tudo antes prepara, tudo depois decorre."},
   {"ic":"eye","t":"Provação Sem Risco","b":"Se o público nunca teme a derrota, o <strong>renascimento não emociona</strong>. Vencer fácil esvazia o arco inteiro.","tip":"<strong>Cuidado:</strong> derrotar o inimigo sem nada mudar por dentro é ação sem transformação.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 6",
  "lessons":["A Provação é a crise central: morte simbólica e renascimento.","Precisa de risco real e 'cheiro de morte' para emocionar.","A mudança tem que ser interna, não só a vitória externa."]},

 {"slug":"ch07-recompensa","sub":"CAPÍTULO 7: A Recompensa (Apoderar-se da Espada)",
  "intro":"Sobrevivida a Provação, o herói toma a Recompensa. É respiro e celebração — mas também a falsa sensação de que tudo acabou.",
  "cards":[
   {"ic":"target","t":"Apoderar-se da Espada","b":"O herói toma posse do que buscava — literal (tesouro, arma) ou interno (autoconhecimento, perdão, amor). <strong>Conquista-se algo por ter enfrentado a morte.</strong>","tip":"<strong>Como aplicar:</strong> a espada é ganha, não dada; o que vem fácil não é recompensa.","wide":True},
   {"ic":"clock","t":"A Falsa Paz","b":"A calmaria pós-Provação: celebração, intimidade, vanglória — e a <strong>ilusão de que a história terminou</strong>. O autor usa o respiro para preparar a virada.","tip":"<strong>Modelo mental:</strong> cuidado com o final que parece chegar cedo."},
   {"ic":"eye","t":"Parar na Celebração","b":"Tratar a Recompensa como desfecho deixa a jornada pela metade — <strong>falta o retorno</strong>.","tip":"<strong>Cuidado:</strong> herói que toma o prêmio igual a quem entrou anula a Provação.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 7",
  "lessons":["A Recompensa é o prêmio conquistado pela Provação.","A falsa paz dá respiro e prepara a virada — não é o fim.","A Recompensa deve revelar a transformação do herói."]},

 {"slug":"ch08-caminho-de-volta","sub":"CAPÍTULO 8: O Caminho de Volta",
  "intro":"Com a Recompensa em mãos, o herói precisa voltar — e o retorno não é tranquilo. A virada que abre o Ato 3.",
  "cards":[
   {"ic":"steps","t":"O Caminho de Volta","b":"O herói decide retornar e completar a missão; muitas vezes começa com uma <strong>perseguição</strong> — a Sombra contra-ataca, as escolhas cobram seu preço.","tip":"<strong>Como aplicar:</strong> sair do Mundo Especial é tão difícil quanto entrar.","wide":True},
   {"ic":"key","t":"O Recomprometimento","b":"Depois da falsa paz, o herói <strong>reassume o propósito</strong>, agora ciente do custo. É a 'segunda virada de ato'.","tip":"<strong>Modelo mental:</strong> a escolha de voltar e terminar prova que a transformação pegou."},
   {"ic":"eye","t":"Retorno Sem Atrito","b":"Voltar sem perseguição nem custo <strong>esvazia o terceiro ato</strong>; herói arrastado de volta perde o protagonismo na reta final.","tip":"<strong>Cuidado:</strong> não deixe a história desinflar entre a Recompensa e o clímax.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 8",
  "lessons":["O Caminho de Volta vira o Ato 3: consequências e perseguição.","O herói se recompromete com a missão, ciente do custo.","A escolha de voltar prova que a transformação se fixou."]},

 {"slug":"ch09-ressurreicao","sub":"CAPÍTULO 9: A Ressurreição",
  "intro":"O clímax: a prova final e mais severa, em que o herói enfrenta a morte uma última vez e demonstra, definitivamente, que mudou.",
  "cards":[
   {"ic":"spiral","t":"A Ressurreição","b":"O confronto culminante, <strong>mais alto que a Provação</strong>. O herói é testado com tudo em jogo e renasce purificado, dominando a lição que antes só vislumbrara.","tip":"<strong>Como aplicar:</strong> é o exame final — a Provação foi a aula, aqui ele prova que aprendeu.","wide":True},
   {"ic":"target","t":"A Prova da Mudança","b":"O herói <strong>age como o novo eu sob pressão máxima</strong> — não basta dizer que mudou. Reúne tudo (dom, lições, aliados) num ato final.","tip":"<strong>Modelo mental:</strong> mudança se mostra em ação, sob fogo, não narrada."},
   {"ic":"sword","t":"Resolução por Terceiros","b":"Se outro salva o dia, o herói <strong>não ressuscita</strong> (deus ex machina). E clímax menor que a Provação é anticlímax.","tip":"<strong>Cuidado:</strong> deve ser o próprio herói a vencer o clímax.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 9",
  "lessons":["A Ressurreição é o clímax: a prova final, maior que a Provação.","O herói demonstra em ato, sob pressão máxima, que mudou.","Deve ser o próprio herói a vencer — nunca um salvador externo."]},

 {"slug":"ch10-retorno-com-elixir","sub":"CAPÍTULO 10: O Retorno com o Elixir",
  "intro":"A jornada se completa quando o herói retorna ao Mundo Comum trazendo o Elixir — algo que beneficia o mundo de onde partiu.",
  "cards":[
   {"ic":"key","t":"O Elixir","b":"O herói volta transformado e traz um <strong>benefício para a comunidade</strong>: tesouro, amor, sabedoria, liberdade, cura. Concreto ou intangível.","tip":"<strong>Como aplicar:</strong> a marca da jornada bem-sucedida é que o ganho do herói cura também os outros.","wide":True},
   {"ic":"spiral","t":"O Círculo Fechado","b":"A Imagem do Mundo Comum retorna, agora <strong>curada pela presença do herói mudado</strong> — o 'depois' que dá sentido ao 'antes'. A última imagem responde à primeira.","tip":"<strong>Modelo mental:</strong> transformação que não volta para casa é incompleta."},
   {"ic":"eye","t":"Voltar de Mãos Vazias","b":"Sem Elixir, a aventura <strong>não significou nada</strong> para o mundo; o herói que guarda tudo para si frustra a função social do mito.","tip":"<strong>Cuidado:</strong> terminar no Mundo Especial deixa o público sem catarse.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 10",
  "lessons":["O herói retorna transformado e traz um Elixir que beneficia o mundo.","O Elixir compartilhado cura o Mundo Comum e fecha o círculo.","A Imagem Final espelha a inicial — a prova visível da mudança."]},
]
