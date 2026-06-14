# -*- coding: utf-8 -*-
"""Conteúdo (pt-BR) das páginas da biblioteca para 'Essencialismo: A Disciplinada
Busca por Menos' (Greg McKeown — Essentialism: The Disciplined Pursuit of Less).
Frameworks canônicos: 'menos, porém melhor'; a essência (a escolha, discernir o
vital trivial, o trade-off — 'o que vou renunciar?'); Essencialista vs.
Não-essencialista; o método EXPLORAR (espaço/escapar, observar/ouvir o sinal,
brincar, dormir, critério 90% / seleção extrema) → ELIMINAR (clarear o propósito
essencial, o 'não' gracioso, descomprometer-se / sunk cost, editar, limites) →
EXECUTAR (buffer/folga, remover o gargalo, pequenas vitórias, rotina, foco no
agora/fluxo); a vida do essencialista. Base: síntese dos frameworks amplamente
documentados — não reproduz o texto."""

BOOK = {
 "title": "Essencialismo",
 "author": "Greg McKeown",
 "header_light": "ESSENCIA",
 "header_bold": "LISMO",
 "subtitle": "VISÃO GERAL · A DISCIPLINADA BUSCA POR MENOS",
 "intro": "E se você parasse de perguntar 'como faço tudo?' e passasse a perguntar 'o que é absolutamente essencial?'. Greg McKeown chama isso de Essencialismo: não é gestão de tempo nem fazer mais com menos esforço — é a disciplina sistemática de discernir o vital de poucos do trivial de muitos, eliminar o resto sem culpa e proteger com folga o que importa. O lema: menos, porém melhor.",
 "description": "O manifesto de Greg McKeown contra a vida espalhada e ocupada que não leva a lugar nenhum. Em vez de dizer sim a tudo por pressão, o Essencialista escolhe: assume que todo 'sim' custa um 'não', aplica o critério dos 90% para recusar até o que é bom, e dedica sua energia à única coisa que faz a maior contribuição. Um método em três fases — explorar, eliminar, executar — para reconquistar a clareza, o controle e a alegria do que realmente conta.",
 "tags": ["Produtividade", "Foco", "Prioridades"],
 "progress": "12 Capítulos Completos",
 "cover": "assets/essencialismo-cover.png",
 "overview_cards": [
   {"ic":"scale","t":"A Essência: Escolha · Discernir · Trade-off","b":"Três verdades destravam tudo. <strong>A escolha</strong>: você sempre pode escolher como gastar tempo e energia ('não posso' → 'eu escolho não'). <strong>O discernimento</strong>: quase tudo é ruído, pouquíssimo é sinal — esforço não vira resultado proporcional. <strong>O trade-off</strong>: não dá para ter tudo, então a pergunta certa não é 'como faço as duas?', mas <strong>'o que vou renunciar?'</strong>.","tip":"<strong>Modelo mental:</strong> antes de cada 'sim', nomeie do que você está abrindo mão. Todo 'sim' é um 'não' a outra coisa.","wide":True},
   {"ic":"steps","t":"O Método: Explorar → Eliminar → Executar","b":"<strong>EXPLORAR</strong> (discernir): crie espaço, observe o sinal, durma, brinque e use o <strong>critério 90%</strong>. <strong>ELIMINAR</strong> (cortar): clareie um propósito, diga o 'não' gracioso, descomprometa-se, edite e ponha limites. <strong>EXECUTAR</strong> (facilitar): construa folga (buffer), remova o gargalo e avance por pequenas vitórias e rotina.","tip":"<strong>Como aplicar:</strong> explore mais opções para escolher menos e melhor; depois corte sem dó; só então execute o pouco que resta.","wide":True},
   {"ic":"target","t":"Critério 90% (Seleção Extrema)","b":"A régua que torna tudo prático: avalie cada opção de 0 a 100. Se não chega a <strong>90</strong>, marque <strong>0</strong> e descarte. <strong>'Se não é um claro SIM, é um NÃO.'</strong> Recusar um sólido '8' é o preço de ter espaço para o '10'.","tip":"<strong>Regra:</strong> hesitou? A própria hesitação já costuma ser o 'não'. Acabe com a zona do 'talvez'."},
 ],
}

CHAPTERS = [
 {"slug":"ch01-essencia-escolha","sub":"A ESSÊNCIA: A Escolha",
  "intro":"A base de todo essencialismo é reconquistar o poder de escolher. As opções podem ser tiradas, mas a capacidade de escolher entre elas, não. Quem esquece isso vira reativo — e deixa que os outros e o mais urgente decidam por ele.",
  "cards":[
   {"ic":"fork","t":"O Poder de Escolher","b":"A escolha é uma capacidade inata: 'não posso' quase sempre significa <strong>'eu escolho não'</strong> ou 'escolho outra coisa'. Coisas (opções) se perdem; a ação de escolher, não. Reformule cada 'tenho que' em 'eu escolho [X] porque valorizo [Y]'.","tip":"<strong>Como aplicar:</strong> ao se pegar dizendo 'sou obrigado', troque por 'eu escolho' e nomeie o porquê."},
   {"ic":"gap","t":"A Impotência Aprendida","b":"Ao parar de exercer a escolha, a pessoa passa a agir <strong>como se não a tivesse</strong>: terceiriza a decisão ao mais barulhento e à 'tirania do tudo'. Tratar tudo como obrigatório é abdicar do leme da própria vida.","tip":"<strong>Sinal de alerta:</strong> deixar a pauta da sua vida ser escrita pelo que grita mais alto.","warn":True},
   {"ic":"spark","t":"A Escolha é um Músculo","b":"Ela atrofia quando não usada e fortalece com o exercício de dizer não. Use 'eu escolho não' para sair da posição de vítima para a de <strong>agente</strong> — comece nas decisões pequenas para ter força nas grandes.","tip":"<strong>Modelo mental:</strong> a escolha não é algo que você tem; é algo que você faz — e treina."},
  ],
  "lessons_title":"Lições-Chave: A Escolha",
  "lessons":["Você sempre pode escolher como gastar tempo e energia — não terceirize isso.","Troque todo 'tenho que' por 'eu escolho', e nomeie o porquê.","Trate a escolha como músculo: exercite-a no pequeno para usá-la no grande."]},

 {"slug":"ch02-essencia-discernir","sub":"A ESSÊNCIA: Discernir o Vital Trivial",
  "intro":"Quase tudo é ruído e pouquíssimo é sinal. O Essencialista investe tempo para distinguir o vital de poucos do trivial de muitos — porque mais esforço, passado certo ponto, não vira mais resultado.",
  "cards":[
   {"ic":"layers","t":"O Vital de Poucos × o Trivial de Muitos","b":"A maioria das opções contribui pouco; uma minoria contribui quase tudo. A meta não é fazer mais coisas bem — é achar <strong>a coisa certa que rende muito mais</strong>. Pela lei do poder (Pareto), ~20% do esforço gera ~80% do resultado.","tip":"<strong>Como aplicar:</strong> em qualquer lista, ache as 1–3 opções de retorno desproporcional e despriorize o resto.","wide":True},
   {"ic":"eye","t":"Sinal × Ruído","b":"Sinal é o que faz a maior contribuição; ruído é o resto que só disputa atenção. Quando tudo parece igualmente importante, <strong>suspeite</strong>: importância uniforme costuma ser falta de discernimento.","tip":"<strong>Regra:</strong> não meça esforço; meça contribuição. Movimento não é progresso."},
   {"ic":"target","t":"O Retorno Desproporcional","b":"A relação entre esforço e resultado <strong>não é linear</strong>. Garimpe muito cascalho para achar a pepita — concentre-se onde o retorno é desproporcional, em vez de pulverizar energia uniformemente.","tip":"<strong>Modelo mental:</strong> pense como editor/garimpeiro — pouca coisa vale ouro; o resto é cascalho."},
  ],
  "lessons_title":"Lições-Chave: Discernir",
  "lessons":["Quase tudo é trivial; pouquíssimo é vital — separe o sinal do ruído.","Mais esforço nem sempre dá mais resultado; busque o retorno desproporcional.","Se tudo parece importante, falta discernimento — não falta tempo."]},

 {"slug":"ch03-essencia-tradeoff","sub":"A ESSÊNCIA: O Trade-off",
  "intro":"Não dá para ter tudo nem fazer tudo. A pergunta do Não-essencialista é 'como faço as duas coisas?'; a do Essencialista é 'o que vou renunciar?'. Assumir o trade-off de propósito é o que transforma escolha em estratégia.",
  "cards":[
   {"ic":"fork","t":"\"O Que Vou Renunciar?\"","b":"Todo caminho tem custo; fingir que não tem só faz outra pessoa (ou o acaso) escolher por você. Troque 'como faço tudo?' — uma armadilha — por <strong>'do que estou abrindo mão?'</strong>, que é acionável. Cada 'sim' é um 'não' a tudo que poderia ocupar aquele tempo.","tip":"<strong>Como aplicar:</strong> antes de aceitar qualquer compromisso, escreva explicitamente o que ele exclui.","wide":True},
   {"ic":"scale","t":"O Trade-off Consciente como Estratégia","b":"Marcas e pessoas que escolhem <strong>deliberadamente o que NÃO farão</strong> ganham foco e força. Estratégia é exatamente o conjunto de coisas que você decidiu não fazer.","tip":"<strong>Modelo mental:</strong> pense como estrategista — defina o que recusar antes de definir o que fazer."},
   {"ic":"mountain","t":"\"Qual Problema Eu Quero?\"","b":"Todo caminho tem dores; não existe a opção sem custo. Em vez de buscar a ausência ilusória de dor, escolha conscientemente <strong>a dor que vale a pena</strong>. Negar o trade-off é a fonte das agendas lotadas e da mediocridade dispersa.","tip":"<strong>Cuidado:</strong> tentar 'encaixar tudo' na agenda é negar o trade-off — e diluir o essencial.","warn":True},
  ],
  "lessons_title":"Lições-Chave: O Trade-off",
  "lessons":["Não dá para fazer tudo: a pergunta certa é 'o que vou renunciar?'.","Estratégia é escolher de propósito o que você NÃO vai fazer.","Todo 'sim' tem um custo de oportunidade — torne-o explícito."]},

 {"slug":"ch04-explorar-espaco","sub":"EXPLORAR: Espaço para Pensar e Escapar",
  "intro":"Para discernir o vital trivial é preciso, paradoxalmente, criar espaço — escapar da rotina e do ruído para conseguir pensar. Sem folga mental, você só reage; não escolhe.",
  "cards":[
   {"ic":"leaf","t":"Escapar para Explorar","b":"Reserve tempo deliberado, isolado das demandas, para pensar e enxergar o todo. Não é fuga do trabalho — agendar o 'pensar' é <strong>parte do trabalho</strong>. Bloqueie um período (de 2 horas a um retiro) sem telas nem agenda, levando só a pergunta essencial.","tip":"<strong>Como aplicar:</strong> trate o tempo de pensar como uma reunião inegociável e proteja-o."},
   {"ic":"bubble","t":"Folga Mental: o Estúdio da Mente","b":"A banda livre da mente é o que permite ver conexões e prioridades que o excesso esconde. Ideias essenciais não surgem na correria — precisam de <strong>uma sala vazia</strong>.","tip":"<strong>Modelo mental:</strong> sem espaço, o cérebro não consegue separar sinal de ruído."},
   {"ic":"clock","t":"O Paradoxo do Ocupado","b":"Quem mais precisa parar para pensar é justamente quem se sente <strong>sem tempo</strong> para isso. Hiperconexão e disponibilidade 100% do tempo matam a reflexão — e disfarçam ocupação de produtividade.","tip":"<strong>Cuidado:</strong> sentir-se 'ocupado demais para pensar' é o sinal de que você precisa parar.","warn":True},
  ],
  "lessons_title":"Lições-Chave: Espaço",
  "lessons":["Agende, de propósito, tempo só para pensar — e proteja-o.","Folga mental é a condição para separar o sinal do ruído.","Quando achar que não tem tempo para parar, é exatamente a hora de parar."]},

 {"slug":"ch05-explorar-observar","sub":"EXPLORAR: Observar e Ouvir o que Importa",
  "intro":"Explorar bem é saber observar e escutar o sinal dentro do excesso de informação. O Essencialista vira 'jornalista da própria vida': busca o lide, a essência — não cada detalhe.",
  "cards":[
   {"ic":"lens","t":"O Jornalista da Própria Vida","b":"Enxergue os fatos com distância, procurando a <strong>'manchete'</strong> — o que de fato importa naquele projeto, reunião ou tema. Pergunte 'qual é a história aqui? qual é o lide?' e ignore o detalhe que não muda a manchete.","tip":"<strong>Como aplicar:</strong> seja repórter, não estenógrafo — discerna o que vira notícia em vez de registrar tudo.","wide":True},
   {"ic":"eye","t":"Caçar o Sinal, não o Ruído","b":"O ruído costuma ser barulhento; o sinal, discreto. Reagir ao mais alto ou mais recente garante perder o essencial. Treine a <strong>escuta ativa do não-óbvio</strong>: o que não está sendo dito, o que destoa do padrão.","tip":"<strong>Regra:</strong> tentar absorver tudo igualmente é a forma mais segura de perder o que importa."},
   {"ic":"link","t":"Conectar os Pontos","b":"O valor está em <strong>ligar fragmentos numa visão</strong>, não em colecionar fragmentos. A manchete é o 20% que explica os 80% de uma situação.","tip":"<strong>Modelo mental:</strong> privilegie conectar pontos sobre acumular dados."},
  ],
  "lessons_title":"Lições-Chave: Observar",
  "lessons":["Em qualquer fluxo de informação, pergunte 'qual é a manchete?'.","O sinal é discreto; o ruído, barulhento — não confunda volume com importância.","Conectar pontos vale mais do que colecionar dados."]},

 {"slug":"ch06-explorar-brincar-dormir","sub":"EXPLORAR: Brincar e Dormir",
  "intro":"Brincar e dormir não são desperdício de tempo essencial — são investimentos que ampliam a capacidade de explorar, criar e discernir. Proteger o sono é proteger o seu maior ativo: você.",
  "cards":[
   {"ic":"spark","t":"Brincar é um Ativo, não um Custo","b":"A brincadeira — atividade feita pelo prazer dela — traz três benefícios: <strong>amplia opções</strong>, reduz o estresse e estimula as funções cerebrais superiores (criatividade, exploração). Quando a lógica empaca, o lúdico abre portas que o esforço fecha.","tip":"<strong>Como aplicar:</strong> agende lazer/brincadeira real sem objetivo de produtividade — é insumo de criatividade, não luxo.","wide":True},
   {"ic":"leaf","t":"O Sono Protege o Ativo","b":"Dormir bem aumenta foco, criatividade e capacidade de priorizar. Sacrificar o sono <strong>corrói exatamente o que te torna capaz</strong> de fazer o essencial. Trate 7–8 horas como recarga, não como pausa: o ativo recarregado rende mais que o esgotado.","tip":"<strong>Modelo mental:</strong> 8h dormindo podem render mais que mais 8h trabalhando exausto."},
   {"ic":"key","t":"Você é o Ativo","b":"A fonte de toda contribuição é a sua mente e energia: <strong>gerir a si mesmo vem antes</strong> de gerir tarefas. Glorificar a privação de sono confunde sacrifício com produtividade.","tip":"<strong>Cuidado:</strong> cortar primeiro o lazer e o sono é cortar a própria fonte de criatividade.","warn":True},
  ],
  "lessons_title":"Lições-Chave: Brincar e Dormir",
  "lessons":["Brincar amplia opções, reduz estresse e alimenta a criatividade.","O sono é recarga do ativo — protegê-lo é pré-condição de tudo.","Você é o ativo: gerir a si mesmo vem antes de gerir tarefas."]},

 {"slug":"ch07-explorar-criterio90","sub":"EXPLORAR: O Critério 90% (Seleção Extrema)",
  "intro":"A seleção extrema é o coração do método: se uma opção não é um claro 'SIM', é um claro 'NÃO'. Rejeitar o bom é o preço de ter espaço para o excelente.",
  "cards":[
   {"ic":"target","t":"O Critério 90%","b":"Avalie cada opção de 0 a 100 no critério mais importante. Se não chega a <strong>90, registre como 0</strong> e descarte. Aceitar 'oitos' medianos ocupa a capacidade que o '10' exigiria — o custo de aceitar o bom é não ter espaço para o excelente.","tip":"<strong>Como aplicar:</strong> defina o critério decisivo, dê a nota, elimine tudo abaixo de 90. Sem 'talvez'.","wide":True},
   {"ic":"scale","t":"Os Três Critérios","b":"Para passar, a opção precisa cumprir <strong>um critério mínimo</strong> ('é viável?') E <strong>dois ou três critérios ideais extremos</strong> ('é exatamente o que busco?'). Só passa o que satisfaz ambos — decisão por critério, não por emoção ou pressão.","tip":"<strong>Regra:</strong> 'se não é um claro sim, é um não' — elimine a zona cinzenta do 'talvez'."},
   {"ic":"gap","t":"O Custo do \"Sim\" Impulsivo","b":"Dizer sim por culpa, pressão ou medo de perder enche a vida de medianos. O 'talvez' indefinido consome energia e adia a renúncia. A própria <strong>hesitação já costuma ser o 'não'</strong>.","tip":"<strong>Sinal de alerta:</strong> hesitar entre sim e não — na seleção extrema, hesitação é não.","warn":True},
  ],
  "lessons_title":"Lições-Chave: Critério 90%",
  "lessons":["Pontue de 0 a 100; abaixo de 90 vira 0 e se descarta.","Exija um critério mínimo + dois ou três extremos para qualquer 'sim'.","Se não é um claro SIM, é um NÃO — acabe com o 'talvez'."]},

 {"slug":"ch08-eliminar-clarear-nao","sub":"ELIMINAR: Clarear o Propósito e o \"Não\" Gracioso",
  "intro":"Eliminar começa por clareza: um único propósito essencial, concreto e inspirador. Com ele definido, dizer 'não' ao resto deixa de ser rude e passa a ser coerente — e pode ser feito com graça.",
  "cards":[
   {"ic":"target","t":"A Intenção Essencial","b":"Defina um propósito ao mesmo tempo <strong>inspirador e concreto/mensurável</strong> o bastante para guiar decisões. Troque o vago ('ser o melhor', 'fazer a diferença') por uma meta única e verificável que, alcançada, torna o resto desnecessário.","tip":"<strong>Como aplicar:</strong> uma boa intenção essencial responde sozinha a mil pedidos paralelos — é a bússola, não o mapa de tudo.","wide":True},
   {"ic":"mask","t":"O \"Não\" Gracioso","b":"Recuse com firmeza e respeito, <strong>separando a decisão da relação</strong>: você pode negar o pedido sem rejeitar quem pede. Diga não devagar e sim depressa; foque no trade-off ('se eu fizer isto, não farei o essencial'); ofereça respeito, não desculpas intermináveis.","tip":"<strong>Regra:</strong> o desconforto curto de um 'não' agora evita o ressentimento longo de um 'sim' mentiroso."},
   {"ic":"sword","t":"Clareza > Aprovação","b":"Equipes e pessoas sem propósito claro avançam em todas as direções e em nenhuma. Dizer sim só para ser querido troca o <strong>respeito de longo prazo</strong> pela aprovação de curto prazo.","tip":"<strong>Cuidado:</strong> propósito vago ('liderar o mercado') não decide nada — tudo 'cabe' nele.","warn":True},
  ],
  "lessons_title":"Lições-Chave: Clarear e Dizer Não",
  "lessons":["Defina uma intenção essencial concreta E inspiradora (verificável).","Use o propósito como filtro: o que não o serve recebe um 'não'.","Recuse com graça: foque no trade-off e separe a decisão da pessoa."]},

 {"slug":"ch09-eliminar-descomprometer-editar-limites","sub":"ELIMINAR: Descomprometer-se, Editar e Limites",
  "intro":"Eliminar não é só recusar o novo: é largar o que já não serve (vencendo o custo afundado), editar a vida como um editor corta o supérfluo, e instalar limites que protegem o essencial dos avanços alheios.",
  "cards":[
   {"ic":"pivot","t":"Descomprometer-se (Sunk Cost)","b":"O já gasto é irrecuperável; mantê-lo como justificativa é jogar bom tempo atrás do ruim. Quando o único motivo for 'já investi tanto', aplique o <strong>teste zero-based</strong>: 'se eu já não estivesse nisto, quanto investiria HOJE para entrar?'. Pouco? Saia.","tip":"<strong>Como aplicar:</strong> separe a decisão do passado investido — o futuro não deve pagar a conta do que já se foi.","wide":True},
   {"ic":"scale","t":"Editar a Vida","b":"Como um editor faz a um texto: <strong>subtrair, condensar, corrigir e conter</strong>. Eliminar opções não enfraquece o todo — fortalece. A obra (e a vida) melhora tanto pelo que se corta quanto pelo que se mantém.","tip":"<strong>Modelo mental:</strong> pense como editor — menos opções, todo mais forte."},
   {"ic":"key","t":"Limites como Liberdade","b":"Fronteiras são regras claras do que você não aceita. Definidas <strong>de antemão</strong>, dizem 'não' por você e eliminam a renegociação no calor do pedido. Sem limite definido, o tempo dos outros sempre invade o seu.","tip":"<strong>Cuidado:</strong> 'já cheguei até aqui, não posso parar' é a falácia do custo afundado em estado puro.","warn":True},
  ],
  "lessons_title":"Lições-Chave: Descomprometer, Editar, Limites",
  "lessons":["Use o teste zero-based para sair do que se mantém só por inércia.","Edite a vida: cortar opções fortalece o todo.","Limites definidos de antemão dizem 'não' por você e protegem o essencial."]},

 {"slug":"ch10-executar-buffer-gargalo","sub":"EXECUTAR: Buffer (Folga) e o Gargalo",
  "intro":"Executar o essencial sem esforço heroico exige preparar o terreno: criar buffer (folga/margem) para absorver imprevistos e remover o gargalo (a restrição que limita todo o progresso).",
  "cards":[
   {"ic":"layers","t":"Buffer: a Regra dos 50%","b":"Reserva deliberada de tempo e recursos entre o planejado e o real. Contra a <strong>falácia do planejamento</strong> (sempre subestimamos prazos), estime quanto algo vai levar e some <strong>50%</strong>. Deixe espaço entre compromissos e prepare-se para o pior cenário razoável.","tip":"<strong>Como aplicar:</strong> pense na agenda como um cano com folga, não cheio até a borda — sem espaço, qualquer atraso transborda.","wide":True},
   {"ic":"pin","t":"Remover o Gargalo","b":"O gargalo é a restrição mais lenta que trava todo o resto — o sistema só anda na velocidade dela. Em vez de 'empurrar mais forte', <strong>ache e remova a restrição</strong>: 1) clareie a meta; 2) identifique o obstáculo que mais limita; 3) elimine-o antes de somar esforço.","tip":"<strong>Regra:</strong> somar recursos sem tratar a restrição só alimenta um gargalo que continua travando tudo."},
   {"ic":"spiral","t":"Preparação Extrema","b":"Prevenir-se para o <strong>pior cenário razoável</strong> reduz o estresse e protege o essencial. O buffer transforma a surpresa em rotina — em vez de cada imprevisto virar uma crise em cascata.","tip":"<strong>Cuidado:</strong> planejar para o melhor cenário garante atrasos encadeados e correria crônica.","warn":True},
  ],
  "lessons_title":"Lições-Chave: Buffer e Gargalo",
  "lessons":["Some 50% às estimativas e deixe folga entre compromissos.","Antes de somar esforço, ache e remova o gargalo que limita tudo.","Prepare-se para o cenário ruim razoável — o buffer transforma surpresa em rotina."]},

 {"slug":"ch11-executar-progresso-rotina-fluxo","sub":"EXECUTAR: Progresso, Rotina e Fluxo",
  "intro":"O essencial avança não por grandes saltos, mas por pequenas vitórias que compõem progresso, por rotinas que colocam o essencial no piloto automático e pelo foco no agora (fluxo).",
  "cards":[
   {"ic":"steps","t":"Pequenas Vitórias (Progresso)","b":"Nada motiva mais do que sentir que se avança no que importa. Para destravar grandes metas que paralisam, comece <strong>ridiculamente pequeno</strong> e gere uma vitória mínima por dia — o ímpeto se acumula por composição.","tip":"<strong>Como aplicar:</strong> a menor vitória possível hoje vence a maior intenção adiada.","wide":True},
   {"ic":"clock","t":"Rotina: o Essencial Automático","b":"Transforme o comportamento essencial em hábito ancorado num <strong>gatilho/horário fixo</strong>, para não gastar força de vontade a cada vez. Desenhe a rotina para que o difícil vire padrão — quando a disciplina pontual falha, o hábito carrega o essencial.","tip":"<strong>Modelo mental:</strong> gatilho → rotina: um sinal disparador automatiza a ação essencial."},
   {"ic":"wave","t":"Foco no Agora (Fluxo)","b":"Concentre-se na <strong>única coisa importante do momento presente</strong>, em vez de se dispersar no passado ou no futuro. A pergunta que devolve o foco: 'qual é a coisa mais importante agora?'.","tip":"<strong>Cuidado:</strong> esperar o 'grande lance' paralisa, e a multitarefa fragmenta a atenção e mata o fluxo.","warn":True},
  ],
  "lessons_title":"Lições-Chave: Progresso, Rotina e Fluxo",
  "lessons":["Comece ridiculamente pequeno: uma vitória mínima por dia.","Ancore o essencial numa rotina com gatilho — automatize o que importa.","Pergunte 'o que é mais importante agora?' e fique no presente."]},

 {"slug":"ch12-a-vida-do-essencialista","sub":"A VIDA DO ESSENCIALISTA",
  "intro":"O essencialismo não é uma técnica de vez em quando: é uma identidade, um modo de ser. Quando vira essência da pessoa, devolve clareza, controle e alegria — e a sensação de que cada hora foi bem vivida.",
  "cards":[
   {"ic":"constellation","t":"A Essência como Identidade","b":"Pare de 'fazer essencialismo' e passe a <strong>'ser essencialista'</strong>: que cada decisão seja filtrada pela essência por hábito, não por esforço. Quando o que você faz reflete o que valoriza, some o conflito de viver dividido.","tip":"<strong>Como aplicar:</strong> use 'o que é essencial?' como a lente padrão de toda escolha — pequena ou grande.","wide":True},
   {"ic":"spark","t":"Clareza · Controle · Alegria","b":"Viver assim entrega três frutos: <strong>clareza</strong> (você sabe o que importa), <strong>controle</strong> (a vida é sua, não dos outros) e <strong>alegria</strong> (presença no que vale a pena). Priorizar o essencial é o melhor seguro contra o arrependimento.","tip":"<strong>Modelo mental:</strong> pense na vida como obra editada — o que você corta a define tanto quanto o que mantém."},
   {"ic":"book","t":"Vida Ocupada × Vida que Conta","b":"No fim, a diferença é entre uma agenda lotada de tudo e <strong>um punhado de coisas que importaram, feitas bem</strong>. Usar o essencialismo só na crise e recair no caos é voltar a ser Não-essencialista.","tip":"<strong>Cuidado:</strong> até o essencial precisa de trade-off — 'menos' continua sendo a régua.","warn":True},
  ],
  "lessons_title":"Lições-Chave: A Vida do Essencialista",
  "lessons":["Transforme o método em identidade: seja essencialista, não apenas o pratique.","Meça a vida pela contribuição ao essencial, não pelo volume de atividades.","'O que é essencial?' é a pergunta-padrão de toda escolha — e o seguro contra o arrependimento."]},
]
