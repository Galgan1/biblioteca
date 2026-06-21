# -*- coding: utf-8 -*-
"""Conteúdo (pt-BR) das páginas da biblioteca para 'A Jornada do Escritor'
(The Writer's Journey) de Christopher Vogler. Estrutura mítica para roteiro:
os 12 estágios da Jornada do Herói e os 8 arquétipos."""

BOOK = {
 "title": "A Jornada do Escritor",
 "author": "Christopher Vogler",
 "header_light": "A JORNADA DO",
 "header_bold": "ESCRITOR",
 "subtitle": "VISÃO GERAL · O MAPA SECRETO DE TODA HISTÓRIA",
 "intro": "Por baixo de cada conto de fogueira, cada filme e cada lenda corre um só rio. Joseph Campbell ouviu mil mitos do mundo inteiro e descobriu que contavam, no fundo, a mesma história. Vogler pegou esse mapa e o devolveu ao escritor como ferramenta de trabalho: doze estágios e oito arquétipos. Não porque a fórmula vende, mas porque a Jornada do Herói é o desenho da única coisa que comove de verdade — alguém que parte do que era para se tornar outro. Quem escreve está sempre recontando esse caminho. A questão é se sabe disso.",
 "description": "A adaptação que Christopher Vogler fez do monomito de Joseph Campbell para o ofício do roteiro: os 12 estágios da Jornada do Herói e os 8 arquétipos vistos como funções psicológicas, não tipos fixos. Uma bússola para escrever — e diagnosticar — qualquer história, do mito épico ao drama mais íntimo. Mapa flexível, jamais receita.",
 "tags": ["Roteiro", "Mito", "Ofício"],
 "progress": "10 Capítulos",
 "cover": "assets/jornada-do-escritor-cover.png",
 "overview_cards": [
   {"ic":"spiral","t":"A Jornada do Herói — 12 Estágios","b":"O mesmo arco em três atos: <strong>Partida</strong> (o herói deixa o Mundo Comum e cruza o Limiar), <strong>Iniciação</strong> (sofre Provas até arrancar a Recompensa) e <strong>Retorno</strong> (volta com o Elixir que faltava). O público nunca leu este mapa, mas reconhece cada curva — porque é a forma da própria vida que muda.","tip":"<strong>Como aplicar:</strong> comprima, reordene, subverta os estágios à vontade. O osso aparece mesmo embaixo de muita carne.","wide":True},
   {"ic":"layers","t":"Os 8 Arquétipos","b":"Não são personagens, são forças que a história convoca: <strong>Herói, Mentor, Guardião do Limiar, Arauto, Camaleão, Sombra, Pícaro, Aliado</strong>. São máscaras — e um mesmo rosto pode trocá-las de cena em cena, conforme o que a trama precisa naquele instante.","tip":"<strong>Modelo mental:</strong> não pergunte 'que personagem ponho aqui?'. Pergunte 'que força esta cena está pedindo?'."},
   {"ic":"key","t":"Morte, Renascimento e Elixir","b":"No fundo da caverna, a <strong>Provação</strong> mata o herói por dentro para que outro renasça. No clímax, a <strong>Ressurreição</strong> cobra a prova de que ele de fato mudou. E no fim ele só está inteiro se voltar com o <strong>Elixir</strong> que cura a casa de onde partiu.","tip":"<strong>Chave:</strong> transformação que não retorna para casa é metade de história. O elixir guardado não cura ninguém."},
 ],
}

CHAPTERS = [
 {"slug":"ch01-monomito-arquetipos","sub":"CAPÍTULO 1: O Monomito e os Arquétipos",
  "intro":"Campbell ouviu os mitos de todos os povos e achou, sob eles, um único enredo. Vogler o entrega ao escritor — e com ele vêm os arquétipos, as forças que toda boa história precisa pôr em jogo.",
  "cards":[
      {"ic":"spiral","t":"A Força do Monomito","emph":"Monomito","b":"Expulso do conforto, o herói desce a um mundo estranho e volta com algo que faltava à sua gente. A roupagem muda — espada, nave, divórcio —, o desenho não. <strong>O monomito comove porque é o retrato de toda transformação que o público já viveu na pele.</strong> O dragão lá fora é sempre o medo aqui dentro.","tip":"<strong>Modelo mental:</strong> o perigo externo da cena é a forma visível do conflito interno do herói. Se um não espelha o outro, a aventura fica oca."},
      {"ic":"layers","t":"A Máscara do Arquétipo","emph":"Máscara","b":"Arquétipo não é crachá fixo, é máscara que se troca conforme a cena exige. O aliado fiel pode vestir a Sombra por três páginas e devolvê-la depois. <strong>É essa troca de máscaras que tira a história do trilho previsível</strong> e mantém o leitor sem saber de que lado cada um joga.","tip":"<strong>Prática:</strong> deixe um personagem assumir a função que ninguém espera dele. O sábio também pode trair; o vilão também pode salvar."},
      {"ic":"eye","t":"O Risco da Forma Rígida","emph":"Forma Rígida","b":"Tratar a jornada como receita de bolo — tantas gramas de cada estágio — sufoca a voz. Corte um beat, inverta dois, faça o herói pular etapas. <strong>O mapa serve para mostrar as curvas da estrada, não para amarrar os pés de quem caminha.</strong> Mito vivo nunca foi cópia.","tip":"<strong>Armadilha:</strong> arquétipo preenchido por obrigação vira clichê de papelão. A função tem de nascer da história, não do checklist.","warn":True},
    ],
  "lessons_title":"Lições-Chave do Capítulo 1",
  "lessons":["O monomito é o mapa universal da transformação, não fórmula de gênero.","Arquétipos são funções; personagens são máscaras que as vestem.","Use a estrutura como bússola flexível, nunca como gabarito fechado."]},

 {"slug":"ch02-mundo-comum-chamado","sub":"CAPÍTULO 2: Mundo Comum e o Chamado à Aventura",
  "intro":"Toda jornada começa no Mundo Comum — o 'antes' que mostra o que falta ao herói. Então o Chamado chega e quebra o equilíbrio de que ninguém queria sair.",
  "cards":[
      {"ic":"book","t":"O Chão do Mundo Comum","emph":"Mundo Comum","b":"Antes da aventura, o tédio. Mostre a rotina, a falta, a ferida que o herói carrega como se fosse normal. <strong>Sem o gosto do café de todo dia, ninguém sente a sede pela estrada.</strong> O 'antes' existe para medir o tamanho da mudança que virá — é a régua de toda a história.","tip":"<strong>Como aplicar:</strong> deixe à mostra, logo de início, o que falta ao herói. É essa falta que o Chamado vem cobrar."},
      {"ic":"wave","t":"O Chamado que Não se Recusa","emph":"Chamado","b":"O Chamado não é sussurro educado: é a porta que se abre e não dá mais para fechar. Uma carta, uma morte, um convite — algo que torna impossível continuar como antes. <strong>O herói pode hesitar, mas o mundo dele já mudou de lugar.</strong> O 'como sempre' acabou na primeira linha do convite.","tip":"<strong>Modelo mental:</strong> chamado que pode ser ignorado sem custo é só sugestão. O verdadeiro fecha a porta de volta ao conforto."},
      {"ic":"target","t":"A Voz do Arauto","emph":"Arauto","b":"O Arauto é quem traz a notícia que vira o jogo e aponta o olhar do herói para o que ele vinha evitando. Pode ser pessoa, telefonema ou reviravolta. <strong>O que ele anuncia é sempre o mesmo recado: a vida de antes não cabe mais.</strong> Ele não resolve nada — só impede que tudo fique igual.","tip":"<strong>Regra:</strong> não demore na vitrine do Mundo Comum. Faça o Arauto entrar cedo, antes que o leitor se acomode no tédio do herói."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 2",
  "lessons":["O Mundo Comum estabelece quem o herói é e o que lhe falta.","O Chamado rompe o equilíbrio e encerra o 'como sempre'.","O Arauto — pessoa, notícia ou evento — traz o Chamado."]},

 {"slug":"ch03-recusa-mentor","sub":"CAPÍTULO 3: Recusa do Chamado e o Encontro com o Mentor",
  "intro":"Entre o Chamado e a aventura há a Recusa — a hesitação que torna humana a coragem. E aí entra o Mentor, que arma o herói e se retira.",
  "cards":[
      {"ic":"clock","t":"A Recusa que Humaniza","emph":"Recusa","b":"O passo atrás, o pretexto, a mão que treme: a Recusa testa se o perigo é de verdade. Herói que aceita o abismo sem piscar não convence ninguém. <strong>Se a decisão não custa medo, a travessia cheira a mentira.</strong> A coragem não é a ausência do tremor — é avançar com ele.","tip":"<strong>Prática:</strong> dê ao herói uma boa razão para recuar antes de aceitar. O leitor precisa sentir o peso do que ele arrisca perder.","warn":True},
      {"ic":"key","t":"O Dom do Mentor","emph":"Mentor","b":"O Mentor entrega o que falta para o primeiro passo: um conselho, um treino, um objeto. Ele encarna o eu superior que o herói ainda não é. <strong>Depois de dar o dom, o sábio precisa sair de cena para não roubar a história.</strong> Gandalf entrega a espada e desaparece na ponte — por isso Frodo cresce.","tip":"<strong>Modelo mental:</strong> o mentor é o farol que mostra o porto de longe; quem pilota a embarcação no temporal é sempre o herói."},
      {"ic":"eye","t":"A Praga do Mentor Onipotente","emph":"Onipotente","b":"O sábio que tudo sabe e tudo pode mata a tensão: se o cajado resolve, para que serve o aprendiz? <strong>O dom do mentor é fagulha, nunca o incêndio inteiro.</strong> Ele aponta o caminho; quem sangra na estrada tem de ser o herói. Tutor que vence as batalhas pelo pupilo escreve a história errada.","tip":"<strong>Armadilha:</strong> mentor que protege demais sufoca o protagonista. A força do herói nasce justamente onde o mentor não pode ir."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 3",
  "lessons":["A Recusa expõe o medo e torna a coragem humana.","O Mentor arma o herói com dom, treino ou conselho — e se retira.","O dom é meio para a ação do herói, nunca substituto dela."]},

 {"slug":"ch04-travessia-limiar","sub":"CAPÍTULO 4: A Travessia do Primeiro Limiar",
  "intro":"O herói se decide e cruza para o Mundo Especial. É o ponto sem retorno que fecha a Partida e abre o Ato 2.",
  "cards":[
      {"ic":"steps","t":"O Ponto Sem Retorno","emph":"Ponto Sem Retorno","b":"O pé no mundo hostil, as regras novas e estranhas, a certeza de que voltar agora seria covardia. A Travessia é o herói dizendo 'sim' com o corpo, não só com a boca. <strong>É o momento em que ele aposta tudo e queima a ponte às costas.</strong> O Ato 1 morre aqui; o que vem não tem volta.","tip":"<strong>Como aplicar:</strong> faça a travessia custar algo. Uma perda concreta no limiar transforma uma decisão em compromisso de verdade."},
      {"ic":"gap","t":"O Guardião do Limiar","emph":"Limiar","b":"Na porta do Mundo Especial há um guarda. Ele não é o vilão final nem carrega o tesouro: está ali para testar quem merece passar. <strong>O Guardião mede o desejo do herói — afasta os mornos e deixa entrar os decididos.</strong> Sua função é filtrar, não matar.","tip":"<strong>Modelo mental:</strong> o guardião aceita ser vencido, contornado ou convertido em aliado. O que ele nunca faz é ocupar o centro da história."},
      {"ic":"eye","t":"A Travessia Sem Custo","emph":"Travessia Sem Custo","b":"Herói empurrado para dentro do Mundo Especial por mãos alheias vira bagagem, não protagonista. Limiar que não cobra nada não significa nada. <strong>Quando a travessia é de graça, o herói entra no Ato 2 morno, e o público entra junto.</strong> Quem não escolheu cruzar não tem o que provar do outro lado.","tip":"<strong>Armadilha:</strong> herói rebocado para a aventura esvazia o clímax lá na frente. O compromisso de agora é o que dará peso ao desfecho.","warn":True},
    ],
  "lessons_title":"Lições-Chave do Capítulo 4",
  "lessons":["A Travessia é o comprometimento que abre o Ato 2.","O Guardião testa o preparo; supere, contorne ou converta.","Idealmente o herói escolhe cruzar, firmando-se como agente."]},

 {"slug":"ch05-provas-aliados-inimigos","sub":"CAPÍTULO 5: Provas, Aliados e Inimigos",
  "intro":"No Mundo Especial, o herói aprende as regras novas, ganha aliados e identifica inimigos — a parte que abre o leque do Ato 2.",
  "cards":[
      {"ic":"target","t":"O Ferro das Provas","emph":"Provas","b":"Pequenos confrontos afiam a lâmina e ensinam ao herói (e ao leitor) como funciona o Mundo Especial. Cada teste eleva a aposta e revela o caráter sob pressão. <strong>As provas preparam o músculo que não pode falhar na Provação.</strong> Não são enchimento — são o treino antes da grande luta.","tip":"<strong>Prática:</strong> que cada conflito do meio ensine algo ou mude alguém. Prova que deixa tudo igual é cena desperdiçada."},
      {"ic":"layers","t":"Aliados e o Espelho Escuro","emph":"Espelho Escuro","b":"Os aliados constroem a confiança; o inimigo dá ao herói o que ele teme virar. A melhor Sombra não é o mais forte — é o que escancara a fraqueza secreta do protagonista. <strong>O grande vilão é o retrato do que o herói poderia se tornar se desistisse de mudar.</strong> Por isso dói tanto encará-lo.","tip":"<strong>Modelo mental:</strong> dê ao antagonista uma lógica que o herói reconheça em si mesmo. A oposição certa é um espelho, não um obstáculo."},
      {"ic":"eye","t":"Conflito Sem Raiz","emph":"Sem Raiz","b":"Briga solta e aliado decorativo afundam o ritmo. Personagem sem função cega a cena; ameaça sem ligação com a ferida central não significa nada. <strong>Cada peça do meio precisa empurrar o herói rumo à Provação.</strong> Se a luta não muda nada por dentro, é só barulho na tela.","tip":"<strong>Armadilha:</strong> ação que não altera o herói por dentro custa tempo do público e dinheiro da produção sem comprar nada.","warn":True},
    ],
  "lessons_title":"Lições-Chave do Capítulo 5",
  "lessons":["Provas treinam o herói e elevam as estacas rumo à Provação.","Aliados e Inimigos definem o time e dão forma à Sombra.","A Sombra mais potente espelha o herói."]},

 {"slug":"ch06-aproximacao-provacao","sub":"CAPÍTULO 6: Aproximação e a Provação",
  "intro":"O herói chega à caverna mais profunda e enfrenta a Provação: a crise central, um encontro com a morte do qual ele renasce outro.",
  "cards":[
      {"ic":"spiral","t":"O Ventre da Baleia","emph":"Ventre","b":"É a noite mais escura da história. No fundo da caverna, diante do que mais teme, o herói toca o fundo do poço. <strong>Ele morre simbolicamente — o velho eu não sobrevive a este lugar — para que outro possa emergir.</strong> A Provação é o centro de gravidade de toda a jornada; tudo cai em direção a ela.","tip":"<strong>Regra:</strong> não há renascimento sem que algo morra antes. Derrube uma certeza, um vínculo ou uma máscara do herói nesta cena."},
      {"ic":"key","t":"O Cheiro de Morte","emph":"Morte","b":"A casca velha do herói se desfaz aqui, e a plateia precisa acreditar que ele pode não voltar. <strong>Só renasce de verdade quem o público teve medo de perder.</strong> Quando o herói prende a respiração no escuro, o leitor prende junto. É esse risco real que dá sentido a cada fagulha jogada lá atrás.","tip":"<strong>Modelo mental:</strong> a profundidade da Provação define o tamanho de tudo o que veio antes. Quanto mais funda a queda, mais alto o renascer."},
      {"ic":"eye","t":"A Morte de Mentira","emph":"Morte de Mentira","b":"Vitória limpa, sem um arranhão, esvazia a caverna. Se ninguém duvidou de que o herói voltaria, o renascimento vira teatro barato. <strong>Sem morte por dentro, a ação por fora é só pirotecnia.</strong> O público perdoa quase tudo, menos a falsa coragem do roteiro que poupa o herói do que importa.","tip":"<strong>Armadilha:</strong> resolver a crise central com uma saída fácil quebra o pacto com o leitor. A morte simbólica é o preço do clímax.","warn":True},
    ],
  "lessons_title":"Lições-Chave do Capítulo 6",
  "lessons":["A Provação é a crise central: morte simbólica e renascimento.","Precisa de risco real e 'cheiro de morte' para emocionar.","A mudança tem que ser interna, não só a vitória externa."]},

 {"slug":"ch07-recompensa","sub":"CAPÍTULO 7: A Recompensa (Apoderar-se da Espada)",
  "intro":"Sobrevivida a Provação, o herói toma a Recompensa. É respiro e festa — e também a ilusão perigosa de que tudo já acabou.",
  "cards":[
      {"ic":"target","t":"A Espada Conquistada","emph":"Espada","b":"O prêmio que a morte validou: o objeto, o saber, o perdão de si mesmo. O herói segura algo que custou caro demais para ser largado. <strong>A Recompensa carrega, gravado, o preço da Provação que ficou para trás.</strong> Espada ganha sem luta é ouro de feira — brilha, mas não corta.","tip":"<strong>Prática:</strong> que o prêmio mostre as marcas do que foi enfrentado. O valor da Recompensa é a memória do que ela custou."},
      {"ic":"clock","t":"O Falso Respiro","emph":"Falso Respiro","b":"Vem a calmaria: o brinde, o beijo, a sensação doce de que terminou. Mas é só o herói tomando fôlego antes da última corrida. <strong>É o silêncio enganoso que prepara o golpe que ainda virá.</strong> Quanto mais confortável a pausa, mais dura a queda que o roteiro guarda para o Ato 3.","tip":"<strong>Modelo mental:</strong> use o alívio para baixar a guarda do público. A maior reviravolta cabe bem no meio da festa."},
      {"ic":"eye","t":"A Festa Sem Fim","emph":"Sem Fim","b":"Demorar na celebração afunda a história. Se o herói se acomoda na vitória, a aventura para — e o mundo que ele jurou salvar fica esperando. <strong>A Recompensa é estação, não destino; quem fica nela trai a própria jornada.</strong> O elixir ainda está longe da gente que precisa dele.","tip":"<strong>Armadilha:</strong> herói que saboreia o prêmio sozinho e esquece o resto perde a simpatia do público. A vitória só vale se for partilhada."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 7",
  "lessons":["A Recompensa é o prêmio conquistado pela Provação.","A falsa paz dá respiro e prepara a virada — não é o fim.","A Recompensa deve revelar a transformação do herói."]},

 {"slug":"ch08-caminho-de-volta","sub":"CAPÍTULO 8: O Caminho de Volta",
  "intro":"Com a Recompensa em mãos, o herói precisa voltar — e o retorno nunca é tranquilo. É a virada que abre o Ato 3.",
  "cards":[
      {"ic":"steps","t":"A Decisão de Voltar","emph":"Voltar","b":"O herói dá as costas ao Mundo Especial e aponta para casa, muitas vezes com as forças que ele feriu correndo atrás. <strong>Voltar não é fuga: é o herói reassumindo a missão, agora sabendo o preço dela.</strong> A perseguição que se acende aqui é a velha vida cobrando o que ele ousou levar.","tip":"<strong>Como aplicar:</strong> dê à volta um motor de urgência — algo ou alguém empurrando o herói para a frente. Retorno sem pressão arrasta o Ato 3."},
      {"ic":"wave","t":"A Última Reviravolta","emph":"Reviravolta","b":"Antes do clímax, uma virada nova aperta o nó: a Sombra ressurge, o plano desmorona, a aposta sobe de novo. <strong>É a faca que o roteiro enfia para garantir que ninguém respire fácil até o fim.</strong> Sem esse choque, o leitor já sente o final chegar e perde o medo de torcer.","tip":"<strong>Prática:</strong> recuse a calmaria fácil no caminho de casa. Solte mais um obstáculo, justo quando tudo parecia resolvido."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 8",
  "lessons":["O Caminho de Volta vira o Ato 3: consequências e perseguição.","O herói se recompromete com a missão, ciente do custo.","A escolha de voltar prova que a transformação se fixou."]},

 {"slug":"ch09-ressurreicao","sub":"CAPÍTULO 9: A Ressurreição",
  "intro":"O clímax: a prova final, mais dura que a Provação, em que o herói encara a morte uma última vez e mostra, em ato, que de fato mudou.",
  "cards":[
      {"ic":"spiral","t":"O Clímax Final","emph":"Clímax","b":"O confronto derradeiro, mais alto que tudo o que veio antes. Aqui a morte volta a bater à porta, e desta vez não há treino que valha. <strong>É a segunda morte e o segundo renascimento — agora à vista de todos, sem rede embaixo.</strong> O que estava em jogo na caverna se decide de vez na luz do clímax.","tip":"<strong>Prática:</strong> faça a aposta da Ressurreição superar a da Provação. O clímax tem de ser o pico, nunca a repetição do que já vimos."},
      {"ic":"target","t":"A Prova da Transformação","emph":"Transformação","b":"Promessa não basta: o herói precisa provar que mudou fazendo, sob pressão máxima, aquilo que era incapaz de fazer no início. <strong>A mudança interna se torna visível num único ato decisivo — a velha falha vencida diante dos nossos olhos.</strong> É o instante em que o público vê, e não apenas ouve, que ele é outro.","tip":"<strong>Regra:</strong> mostre a transformação em ação, não em discurso. Que o herói faça, no clímax, o que jamais teria feito no Mundo Comum."},
      {"ic":"sword","t":"O Salvador de Última Hora","emph":"Salvador","b":"O raio caído do céu, a cavalaria surgida do nada, a sorte que resolve o que o herói não resolveu — tudo isso rouba a catarse que o público pagou para sentir. <strong>Quando uma força externa vence por ele, o herói deixa de merecer o final.</strong> A vitória precisa ter o nome dele, conquistada pelo próprio gesto.","tip":"<strong>Armadilha:</strong> o deus ex machina que liquida o vilão mata junto a honra do herói. O clímax pertence a quem fez a jornada inteira.","warn":True},
    ],
  "lessons_title":"Lições-Chave do Capítulo 9",
  "lessons":["A Ressurreição é o clímax: a prova final, maior que a Provação.","O herói demonstra em ato, sob pressão máxima, que mudou.","Deve ser o próprio herói a vencer — nunca um salvador externo."]},

 {"slug":"ch10-retorno-com-elixir","sub":"CAPÍTULO 10: O Retorno com o Elixir",
  "intro":"A jornada se completa quando o herói volta ao Mundo Comum trazendo o Elixir — algo que beneficia a casa de onde ele partiu.",
  "cards":[
      {"ic":"key","t":"O Elixir que Cura","emph":"Elixir","b":"O herói retorna e despeja sobre a sua gente o que foi buscar: um saber, uma cura, uma liberdade, às vezes um objeto. <strong>O Elixir é a prova de que a descida ao abismo serviu para algo além do próprio herói.</strong> É a sabedoria do mito antigo: você só guarda o tesouro depois de doá-lo.","tip":"<strong>Modelo mental:</strong> o herói merece a coroa porque a partilha. O ganho que fica só com ele não fecha a jornada — só engorda o personagem."},
      {"ic":"spiral","t":"O Círculo que se Fecha","emph":"Círculo","b":"A imagem final ecoa a primeira, e a diferença entre as duas é a história toda. O mesmo lugar, a mesma gente — só que agora curados pelo que o herói trouxe. <strong>O retorno lava a miséria do começo e mostra, sem dizer, o tamanho da mudança.</strong> O Mundo Comum reaparece, e o leitor mede de relance toda a distância percorrida.","tip":"<strong>Prática:</strong> espelhe a cena de abertura no encerramento. A rima visual entre o 'antes' e o 'depois' diz mais que qualquer fala."},
      {"ic":"eye","t":"O Tesouro Guardado","emph":"Tesouro","b":"Terminar com o herói abraçado ao prêmio, sozinho, apaga o sentido de toda a jornada. <strong>Se o palco não mostra a casa curada, a Provação inteira foi sofrimento à toa.</strong> Elixir trancado no cofre não vale o abismo que custou. A catarse do público mora no instante em que o ganho volta para a gente que ficou.","tip":"<strong>Armadilha:</strong> encerrar longe do impacto coletivo encolhe a história. Mostre o que mudou para os outros, não só para o herói.","warn":True},
    ],
  "lessons_title":"Lições-Chave do Capítulo 10",
  "lessons":["O herói retorna transformado e traz um Elixir que beneficia o mundo.","O Elixir compartilhado cura o Mundo Comum e fecha o círculo.","A Imagem Final espelha a inicial — a prova visível da mudança."]},
]
