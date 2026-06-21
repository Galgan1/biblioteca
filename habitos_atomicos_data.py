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
      {"ic":"spark","t":"Os Juros Compostos do Comportamento","emph":"Juros Compostos","b":"<strong>1% melhor a cada dia compõe ~37× num ano</strong>; 1% pior afunda no zero. Hábitos são juros compostos do autodesenvolvimento — e, como dinheiro, rendem devagar e depois de repente.","tip":"<strong>Modelo mental:</strong> não julgue pelo ponto de hoje, julgue pela inclinação da curva. O 1% é invisível num dia e decisivo numa década."},
      {"ic":"pivot","t":"Sistemas > Metas","emph":"Sistemas > Metas","b":"\"Você não sobe ao nível das suas metas — <strong>cai ao nível dos seus sistemas</strong>.\" Vencedor e perdedor querem a mesma coisa; a meta é idêntica. O que separa os dois é a rotina que cada um repete.","tip":"<strong>Como aplicar:</strong> pare de mirar o placar e construa a máquina que o produz. Cuide do processo e o resultado cuida de si."},
      {"ic":"clock","t":"O Platô do Potencial Latente","emph":"Potencial Latente","b":"O progresso se acumula muito antes de aparecer — você atravessa o <strong>vale da decepção</strong> achando que nada anda. É o gelo que não muda nada de -4° a -1° e derrete de uma vez ao cruzar o zero. Persistir é só esperar o ponto de virada.","tip":"<strong>Cuidado:</strong> a maioria desiste exatamente no vale, a um grau de o gelo virar água. Largar perto do limiar é o erro clássico.","warn":True},
    ],
  "lessons_title":"Lições-Chave do Capítulo 1",
  "lessons":["Construa o sistema diário; deixe a meta cair como consequência dele.","O 1% compõe para os dois lados — escolha a direção da curva.","Você ainda está no vale da decepção, não no fracasso: o gelo está prestes a virar água."]},

 {"slug":"ch02-identidade","sub":"CAPÍTULO 2: Hábitos e Identidade",
  "intro":"Por que tanta gente desiste de um hábito que 'devia' manter? Porque mira o resultado, não a pessoa. A mudança que cola não brota do que você quer ter — brota de quem você acredita ser. E essa crença não se decreta: ela se prova, hábito por hábito.",
  "cards":[
      {"ic":"layers","t":"Os Três Níveis","emph":"Três Níveis","b":"Toda mudança mora numa de três camadas: <strong>resultados → processos → identidade</strong>. A maioria parte do resultado ('quero perder peso') e desiste. O que dura parte da identidade ('sou alguém que cuida do corpo') — de dentro para fora.","tip":"<strong>Como aplicar:</strong> não comece perguntando o que quer alcançar; pergunte que tipo de pessoa alcançaria isso — e aja como ela hoje.","wide":True},
      {"ic":"key","t":"Cada Hábito é um Voto","emph":"Voto","b":"Ler uma página é um voto em 'sou leitor'. Calçar o tênis é um voto em 'sou corredor'. A meta nunca foi correr a maratona — é <strong>tornar-se um corredor</strong>. Cada repetição deposita uma prova de quem você está virando.","tip":"<strong>Regra:</strong> você não precisa de unanimidade, precisa de maioria. Vote nas pequenas ações; um voto perdido não anula a eleição."},
      {"ic":"mask","t":"A Identidade que Aprisiona","emph":"Aprisiona","b":"'Sou desorganizado', 'sou péssimo com números', 'sou tímido' — repetida, a frase deixa de descrever e passa a comandar: vira <strong>profecia que se cumpre sozinha</strong>. A mesma força que constrói o hábito bom tranca você no ruim.","tip":"<strong>Sinal de alerta:</strong> segure suas identidades com a mão leve. Quando uma crença sobre si mesmo passa a vetar a mudança, ela já virou jaula.","warn":True},
    ],
  "lessons_title":"Lições-Chave do Capítulo 2",
  "lessons":["Mude de dentro para fora: comece pela identidade, não pelo resultado.","Cada pequena ação é um voto em quem você está se tornando — colete maioria, não perfeição.","Segure as identidades com a mão leve: a crença que define também aprisiona."]},

 {"slug":"ch03-loop-do-habito","sub":"CAPÍTULO 3: O Loop do Hábito",
  "intro":"Antes de consertar um hábito, é preciso enxergar suas peças. Todo comportamento que se repete roda no mesmo ciclo de quatro estágios — e quando você sabe onde ele trava, descobre por que a força de vontade sozinha quase nunca resolve.",
  "cards":[
      {"ic":"spiral","t":"Os Quatro Estágios","emph":"Quatro Estágios","b":"<strong>Deixa → Desejo → Resposta → Recompensa.</strong> A deixa percebe a oportunidade, o desejo dá a motivação, a resposta é a ação, e a recompensa satisfaz — e <strong>ensina</strong> o cérebro que vale a pena fazer de novo. O loop gira, e o hábito se aprende.","tip":"<strong>Como aplicar:</strong> hábito que não pega? Vá estágio por estágio: a deixa é óbvia? o desejo, atraente? a ação, fácil? a recompensa, satisfatória? Um deles falhou.","wide":True},
      {"ic":"target","t":"Você Não Deseja o Hábito","emph":"Não Deseja o Hábito","b":"Ninguém deseja escovar os dentes — deseja a boca limpa. Você nunca quer o hábito em si, quer a <strong>mudança de estado</strong> que ele promete. O fumante não anseia pelo cigarro; anseia pelo alívio que ele entrega.","tip":"<strong>Modelo mental:</strong> o desejo é sempre por sentir-se diferente. Troque a recompensa que o cérebro espera e o desejo muda junto."},
      {"ic":"gap","t":"Problema vs. Solução","emph":"Problema vs. Solução","b":"O loop tem duas metades. Deixa + desejo formam a fase do <strong>problema</strong> (algo precisa mudar); resposta + recompensa, a fase da <strong>solução</strong> (a mudança aconteceu). No fundo, todo hábito é um atalho que o cérebro guarda para resolver o mesmo problema gastando o mínimo de energia.","tip":"<strong>Regra:</strong> não jogue toda a culpa na força de vontade, que mora só na resposta. Puxe a alavanca do estágio onde o hábito de fato emperra."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 3",
  "lessons":["Decomponha o hábito que quer mudar nos quatro estágios e ache onde ele trava.","O que você deseja é a mudança de estado, nunca a ação em si.","Cada estágio tem sua lei: use a alavanca certa em vez de espremer a força de vontade."]},

 {"slug":"ch04-lei1-obvio","sub":"CAPÍTULO 4: 1ª Lei — Torne Óbvio",
  "intro":"Boa parte do que você faz não é decisão — é resposta automática a uma deixa do ambiente. Você não escolhe acender o cigarro; vê o maço e a mão vai. A primeira lei trabalha aí, no gatilho: deixe à vista o que ajuda e some com o que atrapalha.",
  "cards":[
      {"ic":"eye","t":"Pontuação e Intenção","emph":"Pontuação e Intenção","b":"A consciência vem antes da mudança: faça a <strong>pontuação de hábitos</strong> — liste os seus e marque cada um com +, − ou =. Depois amarre o que importa no tempo e no espaço com a <strong>intenção de implementação</strong>: 'vou [hábito] às [hora] em [local]'.","tip":"<strong>Como aplicar:</strong> 'vou meditar' é um desejo; 'vou meditar às 7h na cadeira da sala' é um plano. Dar hora e lugar ao hábito multiplica a chance de ele acontecer."},
      {"ic":"link","t":"Empilhamento de Hábitos","emph":"Empilhamento","b":"O melhor gatilho para um hábito novo é um hábito que você já tem. Encaixe um no outro: '<strong>depois de [hábito atual], vou [novo hábito]</strong>'. A rotina já automática passa a ser a deixa da nova — você pega carona na inércia que já existe.","tip":"<strong>Exemplo:</strong> 'depois de passar o café da manhã, leio uma página.' Sem horário no relógio, sem alarme — a ação anterior é o alarme."},
      {"ic":"pin","t":"O Ambiente Vence a Vontade","emph":"Ambiente Vence a Vontade","b":"Deixe as deixas do bom hábito <strong>na cara</strong> e esconda as do mau. O ambiente está sempre lá; a força de vontade acaba. Some com a tentação e você nem precisa resistir a ela — e dê a cada espaço um único uso, para a mente associar lugar a comportamento.","tip":"<strong>Regra:</strong> a forma mais confiável de largar um mau hábito é tornar a deixa invisível. Não é mais disciplina que falta — é menos exposição."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 4",
  "lessons":["Torne o hábito explícito: escreva a intenção de implementação com hora e lugar.","Empilhe o hábito novo sobre um que já existe e deixe sua deixa à vista.","Desenhe o ambiente a seu favor em vez de torrar força de vontade resistindo a ele."]},

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
