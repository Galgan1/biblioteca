# -*- coding: utf-8 -*-
"""Conteúdo (pt-BR) das páginas da biblioteca para 'Hábitos Atômicos' (James Clear).
Frameworks: 1%/sistemas, identidade, loop do hábito, as 4 leis, regra dos 2 minutos."""

BOOK = {
 "title": "Hábitos Atômicos",
 "author": "James Clear",
 "header_light": "HÁBITOS",
 "header_bold": "ATÔMICOS",
 "subtitle": "VISÃO GERAL · O 1% QUE, REPETIDO, REFAZ UMA VIDA",
 "intro": "Esqueça a virada épica. A mudança que dura não chega num salto — vem em frações de 1%, tão pequenas que você duvida que valham, até o dia em que o composto estoura na sua frente. Você não sobe ao nível das suas metas; cai ao nível dos seus sistemas. E nenhuma das quatro leis pega de verdade enquanto a alavanca mais funda não virar: não 'quero ter este resultado', mas 'sou o tipo de pessoa que faz isto'. Cada repetição é um voto. James Clear não promete motivação — entrega a engenharia.",
 "description": "O sistema de James Clear para construir bons hábitos e desmontar os ruins, peça por peça. O 1% que compõe, os sistemas que vencem as metas, a identidade como camada mais profunda, o loop em quatro estágios — deixa, desejo, resposta, recompensa — e as quatro leis que destravam cada um: torne óbvio, atraente, fácil e satisfatório (e a inversa para largar). No chão da prática: empilhamento de hábitos, a regra dos 2 minutos, o desenho do ambiente, o rastreador e o 'nunca falhe duas vezes'.",
 "hook": "Sua força de vontade não falha — seu sistema falha.",
 "story_promise": "1% melhor por dia = 37x em 1 ano",
 "story_lessons": [
   "Metas dizem onde ir. Sistemas te levam lá.",
   "Aja como a pessoa que você quer ser — já.",
   "Facilite o bom hábito, dificulte o ruim.",
 ],
 "tags": ["Hábitos", "Produtividade", "Autodesenvolvimento"],
 "progress": "8 Capítulos",
 "cover": "assets/habitos-atomicos-cover.png",
 "overview_cards": [
   {"ic":"steps","t":"As Quatro Leis da Mudança","b":"O loop tem quatro estágios; cada lei é a alavanca de um deles (e a inversa larga o mau hábito):","list":[
     "<strong>1ª — Torne Óbvio</strong>: ponha a deixa à vista.",
     "<strong>2ª — Torne Atraente</strong>: faça o desejo querer.",
     "<strong>3ª — Torne Fácil</strong>: corte o atrito da resposta.",
     "<strong>4ª — Torne Satisfatório</strong>: feche o loop com recompensa.",
   ],"tip":"<strong>Como aplicar:</strong> para largar um mau hábito, vire cada lei do avesso — invisível, sem graça, difícil, insatisfatório.","wide":True},
   {"ic":"layers","t":"Mudança por Identidade","b":"Três camadas — <strong>resultados</strong> (o que obtenho) → <strong>processos</strong> (o que faço) → <strong>identidade</strong> (o que creio ser). Quase todo mundo muda de fora para dentro; o que dura faz o contrário.","tip":"<strong>Modelo mental:</strong> a meta não é ler um livro, é virar leitor — e cada hábito é um voto nessa pessoa."},
   {"ic":"spark","t":"O 1% e os Sistemas","b":"<strong>1% melhor por dia</strong> compõe ~37× num ano; 1% pior some no zero. E <strong>sistemas &gt; metas</strong>: a meta aponta o norte, mas é o sistema diário que move o pé.","tip":"<strong>Regra:</strong> não se apaixone pela meta — apaixone-se pelo processo, e a meta cai como subproduto."},
 ],
}

# Infografico de Instagram (Diretor de Design) — arquetipo FLUXO (gerar_infografico.py)
FLUXO = {
 "kicker": "O LOOP DO HÁBITO EM 4 LEIS",
 "steps": [
   {"n":"1","ic":"eye","lbl":"Deixa","law":"1ª Lei · Torne Óbvio",
    "sub":"O gatilho do ambiente que dispara o comportamento. Deixe-o à vista."},
   {"n":"2","ic":"spark","lbl":"Desejo","law":"2ª Lei · Torne Atraente",
    "sub":"A expectativa da recompensa que motiva. Agrupe-o com algo prazeroso."},
   {"n":"3","ic":"leaf","lbl":"Resposta","law":"3ª Lei · Torne Fácil",
    "sub":"A ação em si. Reduza o atrito: comece na versão de <strong>2 minutos</strong>."},
   {"n":"4","ic":"key","lbl":"Recompensa","law":"4ª Lei · Torne Satisfatório",
    "sub":"O prazer que ensina o cérebro a repetir. Feche o loop com satisfação imediata.","gold":True},
 ],
 "na_pratica": "Empilhe UM novo hábito num que já existe — “depois de [rotina], "
               "vou [hábito]” — na versão de <strong>2 minutos</strong>.",
}

# Infografico de Instagram (Diretor de Design) — arquetipo NUMEROS (gerar_infografico.py)
NUMEROS = {
 "kicker": "O LIVRO EM NÚMEROS", "tag": "DADOS",
 "stats": [
   {"ic":"spark","num":"37","unit":"×","star":True,"lbl":"em um ano",
    "ctx":"Melhorar <b>1% por dia</b> compõe ~37 vezes em 12 meses. 1% pior tende a zero."},
   {"ic":"clock","pre":"≤","num":"2","unit":"min","lbl":"a regra de começar",
    "ctx":"Todo hábito novo começa numa versão de <b>2 minutos</b>. Domine a arte de aparecer."},
   {"ic":"layers","num":"3","lbl":"níveis de mudança",
    "ctx":"Resultados → processos → <b>identidade</b>. O durável muda de dentro para fora."},
 ],
 "viz": {"type":"curve","title":"Os juros compostos do comportamento","note":"1% ao dia &rarr; <b>37&times;</b> / ano"},
 "foot": {"ic":"spark","text":"Esqueça a meta: projete o <strong>sistema diário</strong>. "
          "Comece pela versão de 2 minutos e deixe o 1% compor."},
}

# Infografico de Instagram (Diretor de Design) — arquetipo ANATOMIA (anel/ciclo)
ANATOMIA = {
 "eyebrow": "Anatomia · Hábitos Atômicos",
 "h1": '<span class="lt">Anatomia</span> de um hábito',
 "sub": "Todo hábito gira num ciclo de quatro estágios — e cada um tem uma Lei "
        "que o cria (ou, invertida, o quebra).",
 "hub": {"l1": "O LOOP", "l2": "DO HÁBITO", "note": "O MOTOR DE TODO HÁBITO"},
 "nodes": [
   {"ic":"eye","law":"1ª Lei · Torne Óbvio","lbl":"A Deixa",
    "exp":"O gatilho que <b>dispara</b> o hábito. À vista p/ criar; invisível p/ largar."},
   {"ic":"spark","law":"2ª Lei · Torne Atraente","lbl":"O Desejo",
    "exp":"A <b>antecipação</b> da recompensa — é ela que motiva, não a ação."},
   {"ic":"steps","law":"3ª Lei · Torne Fácil","lbl":"A Resposta",
    "exp":"O hábito feito. Vence o <b>menor atrito</b> — frequência &gt; intensidade."},
   {"ic":"key","law":"4ª Lei · Torne Satisfatório","lbl":"A Recompensa",
    "exp":"O prazer <b>imediato</b> fecha o loop e ensina o cérebro a repetir."},
 ],
 "practice": {"kicker":"Na prática · a regra dos 2 minutos","ic":"clock",
   "text":"Comece pela versão <b>≤ 2 minutos</b> do hábito (“ler” = 1 página). "
          "Domine a arte de aparecer; escale depois."},
}

CHAPTERS = [
 {"slug":"ch01-1porcento-sistemas","sub":"CAPÍTULO 1: O 1% e os Sistemas",
  "intro":"O resultado que impressiona quase nunca veio do dia que impressiona. Veio de centenas de dias comuns, melhoras de 1% que pareciam não fazer diferença — até fazerem toda. E quem decide se você chega lá não é a meta pendurada na parede; é o sistema que você repete sem ninguém ver.",
  "cards":[
      {"ic":"spark","t":"O Cálculo Que Ninguém Faz — e Que Decide Quem Evolui","emph":"Juros Compostos","b":"1% melhor por dia parece nada. Mas compõe <strong>37× em um ano</strong>. 1% pior vai ao zero. Você não está parado por falta de esforço — está indo na direção errada em incrementos invisíveis.","tip":"<strong>Modelo mental:</strong> não avalie pelo ponto de hoje — avalie pela inclinação da curva. O 1% diário é imperceptível na semana e decisivo na década."},
      {"ic":"pivot","t":"Campeão e Perdedor Querem Exatamente a Mesma Coisa","emph":"Sistemas > Metas","b":"Nas Olimpíadas, todos querem o ouro. <strong>A meta é idêntica para todos.</strong> O que separa o pódio do resto não é desejo — é a rotina que cada um repete. \"Você não sobe ao nível das suas metas — cai ao nível dos seus sistemas.\"","tip":"<strong>Como aplicar:</strong> pare de otimizar a meta; otimize o sistema que a produz. O placar cuida de si quando a máquina funciona."},
      {"ic":"clock","t":"A Maioria Desiste Exatamente Quando Ia Funcionar","emph":"Potencial Latente","b":"O gelo não muda de -4° a -1°. Parece estagnação. <strong>De repente derrete tudo de uma vez.</strong> A maioria abandona o hábito no vale da decepção — a 1 grau do ponto de virada. Isso não é fracasso: é espera mal-calibrada.","tip":"<strong>Cuidado:</strong> o gelo acumula calor invisível durante horas e derrete em segundos. Você saiu de cena antes do zero grau.","warn":True},
    ],
  "lessons_title":"Lições-Chave do Capítulo 1",
  "lessons":["O sistema diário é o produto; a meta é só o endereço.","1% ao dia compõe dos dois lados — você escolhe agora a direção da curva.","Qual desses é você: ainda no vale esperando o gelo derreter, ou saiu no -1° achando que era fracasso?"]},

 {"slug":"ch02-identidade","sub":"CAPÍTULO 2: Hábitos e Identidade",
  "intro":"Por que tanta gente desiste de um hábito que 'devia' manter? Porque mira o resultado, não a pessoa. A mudança que cola não brota do que você quer ter — brota de quem você acredita ser. E essa crença não se decreta: ela se prova, hábito por hábito.",
  "cards":[
      {"ic":"layers","t":"O Erro que Te Mantém no Loop","emph":"Três Níveis","b":"Você não falha no hábito por falta de força de vontade. Falha porque começou pela camada errada. Resultados → processos → identidade: 99% das pessoas tentam mudar de fora pra dentro. Dura só o que muda de dentro pra fora.","tip":"<strong>Como aplicar:</strong> antes de montar qualquer plano, responda: que tipo de pessoa já viveria assim? Comece sendo ela — o resultado vem depois.","wide":True},
      {"ic":"key","t":"Você Vota em Quem Está se Tornando","emph":"Voto","b":"Cada ação pequena é uma cédula: calçar o tênis = 'sou corredor'. Ler 1 página = 'sou leitor'. A meta não é correr 42 km — é ser o tipo de pessoa que corre. Não precisa de unanimidade, só de maioria.","tip":"<strong>Regra prática:</strong> não pergunte 'vou conseguir?'. Pergunte 'o que um corredor faria agora?' — e faça isso, mesmo que por só 2 minutos."},
      {"ic":"mask","t":"Quando a Identidade Vira Jaula","emph":"Aprisiona","b":"'Sou desorganizado.' 'Sou péssimo com dinheiro.' 'Sou ansioso.' Cada vez que você repete isso, está votando contra si mesmo. Em 2 anos de repetição, a crença vira destino — não por fatalidade, mas por profecia.","tip":"<strong>Sinal de alerta:</strong> qual dessas frases você carrega há mais de 1 ano — 'sou desorganizado', 'sou ansioso' ou 'sou péssimo com dinheiro'? Escreve nos comentários.","warn":True},
    ],
  "lessons_title":"Lições-Chave do Capítulo 2",
  "lessons":["Não comece pela meta. Comece pela identidade: 'que tipo de pessoa faria isso?' — depois aja como ela.","Hábito é voto. Cada ação pequena é uma cédula em quem você está virando. Não precisa ganhar por unanimidade.","As frases que você repete sobre si mesmo constroem ou aprisionam. Segure sua identidade com a mão leve."]},

 {"slug":"ch03-loop-do-habito","sub":"CAPÍTULO 3: O Loop do Hábito",
  "intro":"Antes de consertar um hábito, é preciso enxergar suas peças. Todo comportamento que se repete roda no mesmo ciclo de quatro estágios — e quando você sabe onde ele trava, descobre por que a força de vontade sozinha quase nunca resolve.",
  "cards":[
      {"ic":"spiral","t":"O Erro que Mata Todo Hábito Novo","emph":"Quatro Estágios","b":"Você ataca a ação. O cérebro controla 4 estágios. Existe um loop invisível — Deixa → Desejo → Resposta → Recompensa — que dispara antes de você raciocinar. Mudar só a força de vontade é consertar 1 peça de um motor de 4 cilindros. O hábito quebra porque você mexe na parte errada.","tip":"<strong>Diagnóstico rápido:</strong> hábito que não pega — qual estágio falhou? A deixa é óbvia? O desejo é forte? A ação é fácil? A recompensa é imediata? Um deles é o culpado.","wide":True},
      {"ic":"target","t":"Você Nunca Quer o Hábito","emph":"Não Deseja o Hábito","b":"Ninguém quer escovar os dentes. Quer a boca limpa. O fumante não anseia pelo cigarro — anseia pelo alívio que ele entrega em 3 minutos. O desejo é sempre por uma <strong>mudança de estado</strong>, nunca pela ação em si.","tip":"<strong>Alavanca:</strong> troque a recompensa que o cérebro espera e o desejo muda junto. É mais fácil substituir o prêmio do que brigar com o impulso."},
      {"ic":"gap","t":"Força de Vontade Só Controla 1 de 4","emph":"A Alavanca Que Você Está Ignorando","b":"O loop tem duas metades: <strong>problema</strong> (deixa + desejo) e <strong>solução</strong> (resposta + recompensa). A força de vontade mora só na resposta — 1 dos 4 estágios. Culpá-la por tudo é jogar um jogo com 4 peças usando só uma mão.","tip":"<strong>Qual desses é você?</strong> A) Sabe que quer mudar, mas não aguenta o impulso. B) Nunca sente vontade de começar. A resposta revela exatamente onde seu loop emperra — comenta aí."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 3",
  "lessons":["Hábito que não pega trava em um dos 4 estágios. Ache qual — e use a alavanca certa, não mais força de vontade.","Você nunca deseja o hábito. Deseja a sensação que ele entrega. Mude a recompensa e o desejo muda junto.","Força de vontade controla só 1 de 4 estágios do loop. Atacar só ela é jogar 75% do jogo no escuro."]},

 {"slug":"ch04-lei1-obvio","sub":"CAPÍTULO 4: 1ª Lei — Torne Óbvio",
  "intro":"Boa parte do que você faz não é decisão — é resposta automática a uma deixa do ambiente. Você não escolhe acender o cigarro; vê o maço e a mão vai. A primeira lei trabalha aí, no gatilho: deixe à vista o que ajuda e some com o que atrapalha.",
  "cards":[
      {"ic":"eye","t":"Por Que Força de Vontade Não Funciona","emph":"Pontuação e Intenção","b":"Pessoas disciplinadas não resistem mais à tentação — elas simplesmente se expõem menos a ela. Quem muda o ambiente uma vez vence quem força a barra todo dia. A deixa dispara o hábito antes de você pensar.","tip":"<strong>Virada prática:</strong> 'vou ler mais' dura 3 dias. 'Vou ler depois do café, com o livro em cima da cafeteira' dispara sozinho — hora e lugar duplicam a chance de acontecer."},
      {"ic":"link","t":"Empilhamento de Hábitos","emph":"Empilhamento","b":"Você não precisa de alarme nem de anotação. Só de um hábito que já existe. Fórmula: '<strong>depois de [o que já faço], vou [novo hábito]</strong>'. A rotina antiga vira o gatilho da nova — você pega carona na inércia.","tip":"<strong>Exemplo concreto:</strong> 'depois de passar o café, leio uma página.' O café já acontece todo dia. O livro não precisa de força — precisa de ancoragem."},
      {"ic":"pin","t":"Torne Invisível o Que Te Derruba","emph":"Ambiente Vence a Vontade","b":"Não é falta de disciplina — é excesso de exposição. Quem guarda o celular no quarto de outra pessoa dorme mais cedo. Quem tira o biscoito da bancada come menos. Remover a deixa é mais eficaz do que resistir.","tip":"<strong>Qual desses é você:</strong> tenta resistir todo dia ou já mudou o ambiente uma vez só? Escreve nos comentários — a resposta diz tudo sobre seus hábitos."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 4",
  "lessons":["'Vou meditar' é um desejo. 'Vou meditar às 7h na cadeira da sala' é um contrato com você mesmo.","O hábito não dispara quando você lembra — dispara quando a deixa aparece. Mude o ambiente, não a memória.","Tirar o gatilho do campo de visão vale mais do que qualquer resolução de virada de ano."]},

 {"slug":"ch05-lei2-atraente","sub":"CAPÍTULO 5: 2ª Lei — Torne Atraente",
  "intro":"O que move você não é a recompensa — é a expectativa dela. A dopamina dispara na antecipação, antes de o prazer chegar. Por isso a segunda lei não muda o hábito, muda como ele se parece aos seus olhos: quanto mais atraente a oportunidade, mais o cérebro quer agir.",
  "cards":[
      {"ic":"spark","t":"Agrupamento de Tentação","emph":"Agrupamento de Tentação","b":"Amarre algo que você <strong>precisa</strong> fazer a algo que você <strong>quer</strong> fazer: 'só assisto à série enquanto pedalo'. O desejo já forte empresta sua força ao hábito ainda fraco — um puxa o outro pela mão.","tip":"<strong>Como aplicar:</strong> coloque o prazer como recompensa imediata da tarefa chata. O hábito necessário passa a vir embrulhado em algo que você já adora."},
      {"ic":"bubble","t":"As Normas do Grupo","emph":"Normas do Grupo","b":"Nada é mais atraente que se encaixar. Imitamos três tribos: os <strong>próximos</strong> (família, amigos), os <strong>muitos</strong> (o que a maioria faz) e os <strong>poderosos</strong> (quem tem status). O hábito que custa sozinho fica fácil quando vira o comportamento normal da sua turma.","tip":"<strong>Regra:</strong> entre num grupo onde o seu hábito desejado já é o padrão e a sua versão de hoje é respeitada. Pertencer vence a lógica — escolha a cultura, não só a meta.","wide":True},
      {"ic":"bulb","t":"Reformule a Mente","emph":"Reformule","b":"O mesmo ato muda de cor conforme a palavra. Troque '<strong>tenho que</strong>' por '<strong>tenho a chance de</strong>': não 'preciso treinar', mas 'posso ficar mais forte'. Você não está alterando o hábito — está mudando o sentimento que a deixa desperta.","tip":"<strong>Modelo mental:</strong> o pico de prazer vem na expectativa, não na entrega. Quem aprende a antecipar a recompensa certa já ganhou metade da batalha."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 5",
  "lessons":["Embrulhe o hábito necessário num prazer imediato (agrupamento de tentação).","Mude de tribo: escolha o grupo onde o hábito desejado já é o normal.","Reformule a fala interna — 'tenho a chance de', não 'tenho que'."]},

 {"slug":"ch06-lei3-facil","sub":"CAPÍTULO 6: 3ª Lei — Torne Fácil",
  "intro":"O que constrói um hábito não é o tempo que você dedica num dia, mas o número de vezes que repete. E você repete o que é fácil. A terceira lei não pede mais disciplina — pede menos atrito: torne a boa ação tão simples que não fazê-la dê mais trabalho.",
  "cards":[
      {"ic":"leaf","t":"A Lei do Menor Esforço","emph":"Menor Esforço","b":"O cérebro é um economizador de energia: entre dois caminhos, pega sempre o de <strong>menor atrito</strong>. Então não lute contra essa preguiça — use-a. Reduza os passos do bom hábito e multiplique os do mau, e deixe o ambiente decidir por você.","tip":"<strong>Como aplicar:</strong> menos atrito no bom (deixe o tênis na porta), mais atrito no mau (tire a bateria do controle). Cada segundo a menos vira uma repetição a mais."},
      {"ic":"clock","t":"A Regra dos 2 Minutos","emph":"2 Minutos","b":"Encolha todo hábito novo até caber em <strong>dois minutos</strong>: 'ler' vira ler uma página, 'treinar' vira calçar o tênis, 'meditar' vira respirar uma vez. Parece ridículo de pequeno — e é esse o ponto. Primeiro você domina a <strong>arte de aparecer</strong>; o tamanho vem depois.","tip":"<strong>Regra:</strong> padronize antes de otimizar. Um hábito precisa existir antes de poder crescer — e ele só cresce se for fácil demais para falhar.","wide":True},
      {"ic":"steps","t":"Compromisso e Automação","emph":"Automação","b":"A melhor decisão é a que você toma uma vez e nunca mais. Os <strong>dispositivos de compromisso</strong> travam o bom comportamento no futuro: débito automático para a poupança, app deletado do celular. Um esforço hoje compra meses do hábito certo no piloto automático.","tip":"<strong>Modelo mental:</strong> o obstáculo raramente é continuar — é começar. Engenheie o início para ser quase automático e a inércia trabalha a seu favor."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 6",
  "lessons":["Corte o atrito do bom hábito a quase zero e empilhe atrito no mau.","Comece na versão de 2 minutos: domine aparecer antes de pensar em escalar.","Use compromissos e automação para travar o bom comportamento de antemão."]},

 {"slug":"ch07-lei4-satisfatorio","sub":"CAPÍTULO 7: 4ª Lei — Torne Satisfatório",
  "intro":"O que se sente bem na hora, repete-se; o que dói agora e recompensa só lá na frente, abandona-se. Eis a armadilha do bom hábito: o preço vem hoje e o prêmio vem tarde. A quarta lei resolve isso fabricando uma satisfação que chegue no fim de cada repetição.",
  "cards":[
      {"ic":"key","t":"Recompensa Imediata","emph":"Imediata","b":"O cérebro é cego para o longo prazo: a tentação de agora vence a saúde de daqui a dez anos. Por isso, pendure uma <strong>pequena gratificação</strong> no fim do hábito — mas escolha uma que <strong>combine com a identidade</strong> que você quer (nada de recompensar a corrida com um doce que apaga a corrida).","tip":"<strong>Como aplicar:</strong> dê ao bom hábito um fechamento prazeroso imediato. Sem um motivo para sorrir agora, ele morre de tédio antes de o resultado aparecer."},
      {"ic":"steps","t":"O Rastreador de Hábitos","emph":"Rastreador","b":"Riscar o dia como 'feito' é uma recompensa por si só: visual, concreta, satisfatória. A corrente de marcas cresce e você não vai querer ser quem a quebra — '<strong>não quebre a corrente</strong>'. O que se mede e se vê progredir tende a se manter.","tip":"<strong>Regra:</strong> a própria sequência vira o prêmio e o jogo. Cada X no calendário é mais um voto, agora visível, na sua nova identidade."},
      {"ic":"target","t":"Nunca Falhe Duas Vezes","emph":"Duas Vezes","b":"Faltar um dia não desfaz nada — é acidente. O perigo é o segundo dia: <strong>duas faltas seguidas</strong> já não são tropeço, são o começo de um novo hábito (ruim). O profissional também erra; ele só recompõe mais rápido.","tip":"<strong>Sinal de alerta:</strong> 'já estraguei tudo, desisto' é a armadilha do tudo-ou-nada. Meio esforço num dia ruim vale infinitamente mais que zero. A regra é simples: nunca duas vezes.","warn":True},
    ],
  "lessons_title":"Lições-Chave do Capítulo 7",
  "lessons":["Dê ao hábito uma recompensa imediata que combine com a identidade desejada.","Use um rastreador e proteja a corrente: 'não quebre a sequência'.","Falhou? Volte no dia seguinte — nunca duas faltas em sequência."]},

 {"slug":"ch08-avancado","sub":"CAPÍTULO 8: Avançado — Manter e Dominar",
  "intro":"As quatro leis fazem o hábito nascer; mantê-lo vivo e em crescimento é outro ofício. Aqui está o que separa quem usa o sistema por um mês de quem o usa por uma vida: escolher o jogo certo, dosar a dificuldade e não deixar o automático virar cegueira.",
  "cards":[
      {"ic":"mountain","t":"O Jogo Certo + Cachinhos Dourados","emph":"Jogo Certo","b":"Genes e talentos inclinam o tabuleiro a seu favor em alguns jogos e contra em outros — então escolha a quadra onde sua natureza compete bem. E mantenha o desafio na <strong>Regra de Cachinhos Dourados</strong>: nem fácil demais (tédio), nem impossível (frustração), mas bem <strong>no limite</strong> da sua capacidade.","tip":"<strong>Como aplicar:</strong> calibre a dificuldade para empurrar você um pouco além do confortável. É nessa fronteira que a motivação fica no pico.","wide":True},
      {"ic":"eye","t":"O Lado Sombrio dos Hábitos","emph":"Lado Sombrio","b":"Toda virtude do hábito é também seu risco: ao ficar automático, ele para de exigir atenção — e você repete sem melhorar, estacionado num <strong>platô</strong>. A saída é hábito <strong>mais</strong> prática deliberada: deixe o básico no automático e gaste a atenção liberada na próxima fronteira.","tip":"<strong>Cuidado:</strong> piloto automático sem revisão não é maestria, é estagnação disfarçada de constância.","warn":True},
      {"ic":"pivot","t":"Revisão e Reflexão","emph":"Revisão e Reflexão","b":"Pare de vez em quando para olhar o sistema de fora: o hábito ainda serve ao objetivo? a identidade ainda cabe em você? A revisão evita seguir firme na direção errada. E há um sinal final: <strong>apaixonar-se pelo tédio</strong> é o que separa o profissional do amador.","tip":"<strong>Regra:</strong> o amador só aparece quando sente vontade; o profissional aparece mesmo nos dias sem brilho, sem novidade, sem aplauso."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 8",
  "lessons":["Escolha o jogo onde sua natureza favorece e mantenha o desafio no limite (Cachinhos Dourados).","Hábito + prática deliberada é o que atravessa o platô da automaticidade.","Revise o sistema de tempos em tempos e aprenda a aparecer mesmo no tédio."]},
]
