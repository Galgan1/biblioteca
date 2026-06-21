# -*- coding: utf-8 -*-
"""Conteúdo (pt-BR) das páginas da biblioteca para 'Rápido e Devagar: Duas Formas de Pensar'
(Daniel Kahneman). Frameworks: Sistema 1 vs. Sistema 2, atenção/esforço, WYSIATI, substituição e
heurísticas, ancoragem, disponibilidade/representatividade, falácia da conjunção (Linda)/regressão,
ilusão de validade, excesso de confiança/pré-mortem, teoria do prospecto, enquadramento/contabilidade
mental, os dois eus (pico-fim).
Base: síntese dos frameworks amplamente documentados — não reproduz o texto."""

BOOK = {
 "title": "Rápido e Devagar: Duas Formas de Pensar",
 "author": "Daniel Kahneman",
 "header_light": "RÁPIDO",
 "header_bold": "E DEVAGAR",
 "subtitle": "VISÃO GERAL · DUAS FORMAS DE PENSAR",
 "intro": "Sua mente tem dois motores. O Sistema 1 é rápido, automático, intuitivo e emocional — ele dirige quase tudo o que você pensa e faz. O Sistema 2 é lento, deliberado, lógico e esforçado — e preguiçoso: costuma assinar embaixo das intuições do Sistema 1 sem conferir. Daniel Kahneman mostra que os atalhos do pensamento rápido produzem erros previsíveis (vieses) — e que pensar melhor começa por saber em qual sistema você está.",
 "description": "O mapa da mente de Daniel Kahneman, vencedor do Nobel de Economia. Os dois sistemas de pensamento (rápido/intuitivo e lento/deliberado), o princípio WYSIATI, as heurísticas e vieses que enganam o julgamento (ancoragem, disponibilidade, representatividade, falácia da conjunção, taxa-base, regressão à média), o excesso de confiança e o pré-mortem, a Teoria do Prospecto (aversão à perda, ponto de referência, enquadramento) e os dois eus — o que experiencia e o que recorda.",
 "tags": ["Psicologia", "Decisão", "Vieses Cognitivos"],
 "progress": "12 Capítulos",
 "cover": "assets/rapido-e-devagar-cover.png",
 "overview_cards": [
   {"ic":"fork","t":"Sistema 1 vs. Sistema 2","b":"O <strong>Sistema 1</strong> é rápido, automático, intuitivo e emocional; o <strong>Sistema 2</strong> é lento, deliberado, lógico — e <strong>preguiçoso</strong>. O S1 dirige quase tudo, e o S2 quase sempre só endossa sem checar.","tip":"<strong>Como aplicar:</strong> antes de decidir, pergunte 'essa resposta veio sozinha (S1) ou exigiu esforço (S2)?'.","wide":True},
   {"ic":"eye","t":"WYSIATI — o que você vê é tudo que há","b":"O Sistema 1 monta a história mais coerente com a informação <strong>disponível</strong> e a trata como toda a verdade, ignorando o que não sabe. <strong>A confiança mede a coerência da história, não a evidência.</strong>","tip":"<strong>Modelo mental:</strong> pergunte sempre 'que informação me falta — e mudaria a conclusão?'."},
   {"ic":"scale","t":"Aversão à Perda","b":"Avaliamos tudo a partir de um <strong>ponto de referência</strong>, e <strong>perder dói cerca de 2× mais do que ganhar agrada</strong>. É a peça central da Teoria do Prospecto.","tip":"<strong>Regra:</strong> não recuse uma aposta favorável só porque a dor da perda grita mais alto."},
 ],
}

CHAPTERS = [
 {"slug":"ch01-os-dois-sistemas","sub":"CAPÍTULO 1: Os Dois Sistemas",
  "intro":"A mente opera em dois modos. O Sistema 1 pensa rápido, automático e intuitivo; o Sistema 2 pensa devagar, com esforço e lógica. A maior parte das decisões — e dos erros — nasce no Sistema 1.",
  "cards":[
      {"ic":"spark","t":"O Piloto Automático Manda","emph":"Piloto Automático","b":"O Sistema 1 trabalha sem você pedir: lê o tom de uma frase, decide se confia numa cara, completa “pão com…” antes que você queira. É rápido, sem esforço, sem sensação de comando — e <strong>gera quase todas as suas impressões, intuições e impulsos do dia</strong>. Você acha que pilota; na maior parte do tempo, só assiste.","tip":"<strong>Modelo mental:</strong> trate a primeira resposta como palpite do S1 — quase sempre útil, às vezes traiçoeira.","wide":True},
      {"ic":"clock","t":"O Sistema 2 Custa Caro","emph":"Custa Caro","b":"Multiplicar 17 por 24, comparar duas apólices, segurar a língua: tudo isso exige o Sistema 2, que aloca atenção, gasta energia e <strong>cansa como um músculo</strong>. Por ser caro, ele é convocado a contragosto — e só quando o S1 trava ou a aposta é alta o bastante para acordá-lo.","tip":"<strong>Regra:</strong> acione o S2 de propósito quando o tema for complexo ou caro errar — ele não vem sozinho."},
      {"ic":"mask","t":"O Supervisor que Só Assina","emph":"Só Assina","b":"O Sistema 2 é o “eu” que você acredita ser — racional, no controle. Mas no dia a dia ele age mais como um <strong>supervisor preguiçoso que carimba o que o S1 entrega</strong>, sem reler. Você sente que decidiu pesando tudo; na verdade a intuição chegou pronta e a razão só assinou embaixo.","tip":"<strong>Cuidado:</strong> acreditar que “decidiu racionalmente” quando o S1 já tinha a resposta e o S2 apenas chancelou.","warn":True},
    ],
  "lessons_title":"Lições-Chave do Capítulo 1",
  "lessons":["Quase tudo o que você pensa e faz começa no Sistema 1.","O Sistema 2 é lento e preguiçoso — por isso os erros do S1 passam.","O primeiro passo para decidir melhor é saber em qual sistema você está."]},

 {"slug":"ch02-atencao-esforco-piloto-automatico","sub":"CAPÍTULO 2: Atenção, Esforço e Piloto Automático",
  "intro":"O Sistema 2 é caro: pensar com esforço consome um recurso limitado, gera fadiga e tende à lei do menor esforço. Por isso a mente delega quase tudo ao Sistema 1 e só 'acorda' o S2 quando obrigada.",
  "cards":[
      {"ic":"leaf","t":"A Lei do Menor Esforço","emph":"Menor Esforço","b":"Entre dois caminhos para o mesmo destino, a mente escolhe sempre o <strong>que dói menos pensar</strong>. Pensar com cuidado é trabalhoso, então a regra padrão é pular a checagem deliberada e aceitar o palpite que já veio. Não é preguiça moral: é economia de um recurso de verdade escasso — a atenção.","tip":"<strong>Como aplicar:</strong> não conte com a força de vontade o dia todo; desenhe o ambiente para precisar menos dela.","wide":True},
      {"ic":"scale","t":"O Mesmo Poço Esgotado","emph":"Mesmo Poço","b":"Autocontrole e raciocínio puxam da <strong>mesma reserva limitada</strong>: gastar num esvazia o outro. Quem resiste a um doce decide pior na sequência; quem decide o dia inteiro cede à tentação à noite. É o esgotamento do ego — e fome, cansaço e multitarefa entregam o volante de volta ao Sistema 1.","tip":"<strong>Regra:</strong> evite decisões importantes com fome, exausto ou fazendo três coisas ao mesmo tempo."},
      {"ic":"eye","t":"O Gorila que Ninguém Vê","emph":"Gorila","b":"No experimento clássico, contando passes de basquete, <strong>metade das pessoas não vê uma figura fantasiada de gorila cruzar a tela</strong> e bater no peito. O foco intenso ilumina um ponto e apaga toda a periferia. Não vemos o óbvio — e, pior, ficamos cegos à própria cegueira.","tip":"<strong>Cuidado:</strong> supor que “estar prestando atenção” garante ver o que importa — o foco sempre cobra periferia.","warn":True},
    ],
  "lessons_title":"Lições-Chave do Capítulo 2",
  "lessons":["Pensar com esforço é caro; a mente economiza por padrão.","Cansaço, fome e multitarefa dão o controle ao Sistema 1.","Desenhe o contexto para depender menos da força de vontade."]},

 {"slug":"ch03-wysiati-coerencia","sub":"CAPÍTULO 3: WYSIATI e a Máquina de Saltar a Conclusões",
  "intro":"O Sistema 1 constrói a história mais coerente possível com a informação disponível e a trata como toda a verdade. WYSIATI: 'o que você vê é tudo que há' — não levamos em conta o que não sabemos.",
  "cards":[
      {"ic":"eye","t":"O que Você Vê é Tudo que Há","emph":"Tudo que Há","b":"O Sistema 1 monta a história mais coerente que consegue com a informação que tem à mão — e a trata como o mundo inteiro. Ele não pergunta o que ficou de fora. Por isso a sua confiança mede a <strong>coerência da história, não a qualidade da evidência</strong>: quanto menos você sabe, mais fácil é a história fechar.","tip":"<strong>Como aplicar:</strong> pergunte “o que falta que eu não estou vendo — e mudaria a conclusão?”.","wide":True},
      {"ic":"link","t":"O Halo que Contamina Tudo","emph":"Halo","b":"As ideias acendem ideias vizinhas em cascata, e uma narrativa fluida vira “verdade” sentida. Uma primeira impressão — um rosto simpático, uma resposta segura — <strong>contamina traços que você nem chegou a observar</strong>. Quem parece confiante no início ganha crédito antecipado em tudo o que disser depois.","tip":"<strong>Modelo mental:</strong> a confiança mede a coerência da história, não a quantidade de evidência por trás dela."},
      {"ic":"bubble","t":"A Ilusão de Verdade por Repetição","emph":"Repetição","b":"O que é fácil de processar — familiar, claro, repetido — parece mais verdadeiro, bom e seguro. A mera <strong>repetição fabrica a sensação de verdade</strong>, mesmo numa frase falsa: ouvi-la três vezes a faz soar certa. Propaganda e boato exploram exatamente essa fluência sem precisar de um único argumento.","tip":"<strong>Cuidado:</strong> tomar a fluência — “soou claro, soou familiar” — como prova de que aquilo é verdade.","warn":True},
    ],
  "lessons_title":"Lições-Chave do Capítulo 3",
  "lessons":["Julgamos com o que está ativado, não com o que é relevante.","Facilidade e repetição forjam sensação de verdade.","Quanto menos você sabe, mais fácil (e errado) é montar uma história coerente."]},

 {"slug":"ch04-substituicao-heuristicas","sub":"CAPÍTULO 4: Substituição e o Mecanismo das Heurísticas",
  "intro":"Diante de uma pergunta difícil, o Sistema 1 a substitui por uma pergunta mais fácil e responde a esta sem perceber a troca. Heurísticas são atalhos úteis que produzem vieses sistemáticos.",
  "cards":[
      {"ic":"pivot","t":"A Troca de Pergunta Silenciosa","emph":"Troca de Pergunta","b":"Diante de uma pergunta difícil — “esse candidato será um bom gestor?” — o Sistema 1 não responde a ela. Ele a <strong>troca por uma fácil e parecida</strong> — “gosto da cara dele?” — e devolve essa resposta como se fosse a outra. A troca é invisível: você sente que respondeu à pergunta real, com pressa e confiança demais.","tip":"<strong>Como aplicar:</strong> isole a pergunta-alvo da pergunta fácil que você de fato respondeu.","wide":True},
      {"ic":"wave","t":"O Afeto Decide e Depois Argumenta","emph":"Afeto","b":"O atalho mais comum é deixar o gostar ou temer guiar o juízo sobre o mundo. Se simpatizo com uma tecnologia, <strong>julgo seus riscos baixos e seus benefícios altos</strong> — sem nenhum dado novo. A conclusão emocional chega primeiro e a mente fabrica os motivos depois, na ordem inversa da que imaginamos.","tip":"<strong>Modelo mental:</strong> o afeto vem antes do argumento — o sentimento entrega a resposta, a razão maquia."},
      {"ic":"target","t":"Gostar Não é o Mesmo que Verdadeiro","emph":"Verdadeiro","b":"O erro no coração da substituição é colar dois mundos diferentes: confundir “<strong>isso me agrada</strong>” com “<strong>isso é provavelmente verdadeiro</strong>”. Uma resposta que escorrega fácil parece certa só por ser fluente. Mas facilidade de sentir não é evidência de nada — é só o S1 entregando o que tinha à mão.","tip":"<strong>Cuidado:</strong> tomar a fluência da resposta como prova de que respondeu à pergunta certa.","warn":True},
    ],
  "lessons_title":"Lições-Chave do Capítulo 4",
  "lessons":["Diante de perguntas difíceis, respondemos a outras mais fáceis sem perceber.","O afeto (gostar/temer) é a heurística mais comum e poderosa.","Para checar um julgamento, separe a pergunta-alvo da que você de fato respondeu."]},

 {"slug":"ch05-ancoragem","sub":"CAPÍTULO 5: Ancoragem",
  "intro":"Ao estimar um valor, um número apresentado antes — mesmo arbitrário e irrelevante — ancora o julgamento e o puxa em sua direção. A ancoragem é um dos vieses mais robustos e mensuráveis.",
  "cards":[
      {"ic":"pin","t":"Toda Estimativa Gravita na Âncora","emph":"Gravita","b":"Antes de estimar qualquer número, o que você viu por último puxa a resposta para perto de si. Kahneman mostrou que <strong>até uma roleta viciada ou dígitos aleatórios deslocam a estimativa</strong> de pessoas — sem nenhuma relação com a pergunta. Em negociação, quem solta o primeiro número desenha o campo onde os dois vão jogar.","tip":"<strong>Como aplicar:</strong> em negociação, abra com a sua âncora — quem fala o primeiro número define o terreno.","wide":True},
      {"ic":"steps","t":"Os Dois Motores da Âncora","emph":"Dois Motores","b":"A âncora prende por dois caminhos ao mesmo tempo: o <strong>ajuste insuficiente</strong> — o S2 parte do número dado e para cedo demais — somado à <strong>ativação seletiva</strong> — o S1 corre buscar só as evidências que combinam com ela. Um deliberado, outro automático, ambos puxando para o mesmo lado.","tip":"<strong>Regra:</strong> ancore conscientemente e desconfie de todo número visto pouco antes de você estimar."},
      {"ic":"sword","t":"Saber é Pouco — Pense o Oposto","emph":"Pense o Oposto","b":"O mais perturbador da ancoragem é que ela age <strong>mesmo quando você sabe que o número é absurdo e irrelevante</strong>. Acreditar que “ignorou” a âncora é cair nela com elegância. A única defesa que funciona não é desprezar — é gastar esforço listando ativamente razões pelas quais ela estaria errada.","tip":"<strong>Cuidado:</strong> deixar a outra parte abrir a negociação sem ter a sua própria âncora pronta.","warn":True},
    ],
  "lessons_title":"Lições-Chave do Capítulo 5",
  "lessons":["Qualquer número visto antes de estimar puxa a estimativa em sua direção.","A ancoragem age mesmo quando você sabe que a âncora é irrelevante.","Defenda-se pensando ativamente o oposto da âncora."]},

 {"slug":"ch06-disponibilidade-representatividade","sub":"CAPÍTULO 6: Disponibilidade e Representatividade",
  "intro":"Estimamos probabilidades por dois atalhos falhos: a disponibilidade (o que vem fácil à mente parece mais frequente) e a representatividade (julgamos pela semelhança ao estereótipo, ignorando a estatística).",
  "cards":[
      {"ic":"wave","t":"O que Lembra Fácil Parece Comum","emph":"Lembra Fácil","b":"Estimamos a frequência de algo pela <strong>facilidade com que exemplos saltam à memória</strong> — não pelos números. Um desastre aéreo recente, vívido e repetido na mídia, faz o avião parecer mais perigoso que o carro, quando é o contrário. O que é fácil de imaginar sequestra o lugar do que é estatisticamente provável.","tip":"<strong>Como aplicar:</strong> avalie o risco pela frequência real, não pela última manchete que te marcou.","wide":True},
      {"ic":"constellation","t":"O Estereótipo no Lugar da Conta","emph":"Estereótipo","b":"A representatividade julga a que categoria algo pertence pela <strong>semelhança com o protótipo na sua cabeça</strong>, ignorando quão comum aquilo realmente é. Alguém tímido e organizado “tem cara” de bibliotecário — e esquecemos que há muito mais agricultores. O perfil grita; a taxa-base fica muda.","tip":"<strong>Regra:</strong> antes de cravar o caso, pergunte “quão comum isso é na população?” — só então ajuste."},
      {"ic":"gap","t":"A Taxa-Base que Some","emph":"Taxa-Base","b":"O pecado por trás dos dois atalhos é o mesmo: <strong>ignorar a frequência de base ao julgar um caso isolado</strong>. “Parece o tipo” não é “é provável”. Sem ancorar primeiro em quão comum algo é na população, qualquer perfil convincente nos leva a apostar contra a estatística e a errar com confiança.","tip":"<strong>Cuidado:</strong> deixar o estereótipo do caso gritar mais alto do que a estatística da população.","warn":True},
    ],
  "lessons_title":"Lições-Chave do Capítulo 6",
  "lessons":["Frequência percebida segue a facilidade de lembrar, não os dados.","Semelhança ao estereótipo nos faz ignorar a estatística de base.","Antes de julgar, ancore na taxa-base — depois ajuste pela evidência."]},

 {"slug":"ch07-linda-regressao","sub":"CAPÍTULO 7: A Falácia da Conjunção (Linda) e a Regressão à Média",
  "intro":"A representatividade gera dois erros clássicos: achar que um cenário detalhado é mais provável que um genérico (Linda) e ignorar que valores extremos voltam à média sem causa nenhuma (regressão).",
  "cards":[
      {"ic":"layers","t":"O Detalhe que Reduz a Chance","emph":"Detalhe","b":"No caso de Linda — descrita como engajada e crítica — quase todos julgam “caixa de banco e feminista” mais provável que só “caixa de banco”. É impossível: <strong>cada detalhe somado só pode estreitar o conjunto, nunca alargá-lo</strong>. P(A e B) jamais supera P(A). A história mais rica convence justamente porque é menos provável.","tip":"<strong>Como aplicar:</strong> entre o cenário cheio de detalhes e o simples, aposte no simples — ele é mais provável.","wide":True},
      {"ic":"spiral","t":"O Extremo Volta Sozinho à Média","emph":"Volta Sozinho","b":"Depois de um resultado extremo — um voo péssimo, uma prova brilhante — o próximo tende a se aproximar da média por puro acaso. Mas a mente <strong>insiste em fabricar uma causa</strong>: “a bronca corrigiu o piloto”, “o elogio amoleceu o aluno”. Punição parece funcionar e elogio parece estragar — quando foi só a estatística respirando.","tip":"<strong>Regra:</strong> antes de explicar uma melhora ou piora, pergunte “não seria só regressão à média?”."},
      {"ic":"mask","t":"Plausível Não é Provável","emph":"Plausível","b":"Uma narrativa rica em detalhes é mais fácil de imaginar, e por isso parece mais provável — mas cada cláusula extra a torna estatisticamente menos provável. A <strong>coerência engana a lógica</strong>: confundimos “consigo visualizar bem” com “tem grande chance de ser verdade”. O vívido vende; o vago acerta.","tip":"<strong>Cuidado:</strong> dar a uma intervenção o crédito por uma melhora que era apenas regressão à média.","warn":True},
    ],
  "lessons_title":"Lições-Chave do Capítulo 7",
  "lessons":["Adicionar detalhes plausíveis aumenta a credibilidade e diminui a probabilidade.","Resultados extremos regridem à média sozinhos — não invente causa.","Desconfie de explicações causais para o que pode ser mero acaso."]},

 {"slug":"ch08-ilusao-validade-intuicao","sub":"CAPÍTULO 8: A Ilusão de Validade e a Intuição de Especialistas",
  "intro":"A confiança que sentimos não mede a precisão de um julgamento — mede a coerência da história. Em ambientes irregulares (bolsa, política), especialistas têm intuições tão válidas quanto adivinhação, com confiança altíssima.",
  "cards":[
      {"ic":"lens","t":"Sentir-se Certo Não é Estar Certo","emph":"Sentir-se Certo","b":"A confiança que você sente mede a coerência da sua história, não a precisão dela. É a ilusão de validade: a <strong>certeza subjetiva sobrevive intacta mesmo quando os dados provam que o julgamento não prevê nada</strong>. Analistas de bolsa seguríssimos acertam como o acaso — e seguem confiantes assim mesmo.","tip":"<strong>Como aplicar:</strong> trate confiança alta em terreno imprevisível como alarme, não como garantia.","wide":True},
      {"ic":"key","t":"Quando a Intuição é Confiável","emph":"Intuição","b":"O palpite de especialista só merece crédito sob duas condições juntas: um <strong>ambiente regular o bastante para ter padrões</strong> e <strong>feedback rápido e claro para aprendê-los</strong>. O bombeiro que sente a casa desabar e o enxadrista têm isso; o previsor de bolsa, não — ali a intuição é adivinhação vestida de experiência.","tip":"<strong>Regra:</strong> sem ambiente regular e feedback de qualidade, não confie na intuição — nem na sua."},
      {"ic":"scale","t":"A Fórmula Vence o Especialista","emph":"Fórmula","b":"Em previsões de ambiente ruidoso, uma <strong>fórmula simples e consistente supera o julgamento clínico do especialista</strong> na maioria dos casos. O motivo é humano demais: a pessoa varia, contradiz a si mesma de um dia para o outro e se deixa levar pela impressão global. A regra é burra, mas não muda de humor.","tip":"<strong>Cuidado:</strong> tratar a confiança de um especialista como se fosse prova do acerto da previsão.","warn":True},
    ],
  "lessons_title":"Lições-Chave do Capítulo 8",
  "lessons":["Confiança é a sensação de coerência, não a medida da precisão.","Intuição só é confiável em ambientes regulares com bom feedback.","Em terreno ruidoso, regras simples e consistentes vencem o julgamento humano."]},

 {"slug":"ch09-excesso-confianca-pre-mortem","sub":"CAPÍTULO 9: Excesso de Confiança, Visão de Fora e o Pré-Mortem",
  "intro":"Subestimamos prazos, custos e riscos porque planejamos pela 'visão de dentro' (otimista) em vez da 'visão de fora' (a estatística de casos parecidos). O excesso de confiança é a mais danosa das ilusões.",
  "cards":[
      {"ic":"lens","t":"Olhe de Fora, Não de Dentro","emph":"de Fora","b":"A falácia do planejamento nasce da visão de dentro: estimamos pelo melhor cenário deste projeto, com seus detalhes animadores, e ignoramos os atrasos típicos. A correção é a <strong>visão de fora — a taxa-base de projetos parecidos que já aconteceram</strong>. Eles estouraram prazo e custo; o seu provavelmente também vai.","tip":"<strong>Como aplicar:</strong> pergunte “como foram os projetos parecidos com este?” antes de confiar na sua estimativa.","wide":True},
      {"ic":"sword","t":"Convide o Fracasso para a Mesa","emph":"o Fracasso","b":"O pré-mortem inverte o roteiro: antes de fechar a decisão, suponha que já se passou um ano e <strong>o projeto fracassou feio — e cada um escreve a história desse desastre</strong>. O exercício legitima a dúvida que o entusiasmo do grupo calava e faz emergir riscos que ninguém ousava nomear em voz alta.","tip":"<strong>Regra:</strong> imaginar o fracasso agora custa barato; descobri-lo depois, no post-mortem, custa caro."},
      {"ic":"mountain","t":"O Otimismo que Esquece o Rival","emph":"Esquece o Rival","b":"Superestimamos nosso controle e nossa habilidade, e <strong>esquecemos que os concorrentes estão fazendo exatamente o mesmo cálculo</strong>. O otimismo coletivo é contagioso e cega: numa sala animada, levantar a mão para duvidar parece deslealdade. Por isso atraso e estouro de orçamento são a regra, não o azar.","tip":"<strong>Cuidado:</strong> silenciar a própria dúvida só porque “a equipe está animada” e ninguém mais reclamou.","warn":True},
    ],
  "lessons_title":"Lições-Chave do Capítulo 9",
  "lessons":["Planejamos pelo melhor caso e por isso quase sempre estouramos prazo e custo.","A visão de fora (taxa-base de projetos parecidos) corrige o otimismo.","Um pré-mortem barato hoje evita um post-mortem caro depois."]},

 {"slug":"ch10-teoria-do-prospecto","sub":"CAPÍTULO 10: Teoria do Prospecto — Aversão à Perda e Ponto de Referência",
  "intro":"Contra a economia clássica, avaliamos resultados como ganhos e perdas em relação a um ponto de referência — e perder dói cerca de duas vezes mais do que ganhar agrada.",
  "cards":[
      {"ic":"scale","t":"Perder Dói o Dobro de Ganhar","emph":"o Dobro","b":"A curva do prazer e a curva da dor não são simétricas: <strong>perder R$ 100 machuca cerca de duas vezes mais do que ganhar R$ 100 agrada</strong>. Essa assimetria explica por que recusamos apostas justas e seguramos ações que despencam — o medo da perda fala sempre mais alto que a vontade do ganho.","tip":"<strong>Como aplicar:</strong> não recuse uma aposta favorável só porque a dor da perda grita mais alto que o ganho.","wide":True},
      {"ic":"pin","t":"Tudo se Mede a Partir de um Ponto","emph":"a Partir de um Ponto","b":"Não julgamos riqueza absoluta — julgamos <strong>mudanças a partir de onde estamos agora</strong>, o ponto de referência. E com sensibilidade decrescente: sair de R$ 100 para R$ 200 sentimos muito; de R$ 1.100 para R$ 1.200, quase nada, embora a quantia seja a mesma. Mude o ponto de partida e o mesmo fato vira ganho ou perda.","tip":"<strong>Modelo mental:</strong> redefina o ponto de referência e a mesma situação se transforma em alívio ou em derrota."},
      {"ic":"key","t":"O que é Meu Vale Mais","emph":"é Meu","b":"Basta possuir algo para passar a valorizá-lo acima do preço de mercado — é o efeito posse, e nasce da aversão à perda: <strong>abrir mão dói como perder</strong>. Some a isso a tendência a superpesar tanto o evento raríssimo quanto a certeza absoluta, e estão explicadas a loteria que compramos e o seguro caro que contratamos.","tip":"<strong>Cuidado:</strong> segurar um investimento ruim só para não “realizar” a perda e ter de admiti-la.","warn":True},
    ],
  "lessons_title":"Lições-Chave do Capítulo 10",
  "lessons":["Avaliamos mudanças a partir de um ponto de referência, não a riqueza final.","Perdas pesam cerca do dobro dos ganhos equivalentes.","Superpesamos a certeza e os eventos raros, distorcendo seguros e loterias."]},

 {"slug":"ch11-enquadramento-contabilidade-mental","sub":"CAPÍTULO 11: Enquadramento, Contabilidade Mental e Econs vs. Humanos",
  "intro":"A mesma informação descrita de formas diferentes produz decisões diferentes — porque o Sistema 1 reage à apresentação, não à substância. Somos Humanos previsivelmente irracionais, não Econs.",
  "cards":[
      {"ic":"lens","t":"A Palavra Decide, Não o Fato","emph":"A Palavra Decide","b":"“Salva 200 de 600” e “deixa 400 morrerem” descrevem o mesmo resultado — e fazem as pessoas escolherem o oposto. “90% magro” vende; “10% de gordura”, não. <strong>A forma de apresentar muda a escolha sem mudar um único fato</strong>, porque o Sistema 1 reage à embalagem, não à substância por dentro dela.","tip":"<strong>Como aplicar:</strong> reenquadre e inverta toda decisão importante — “se fosse descrita como perda, eu decidiria igual?”.","wide":True},
      {"ic":"layers","t":"As Contas Mentais Separadas","emph":"Contas Mentais","b":"Tratamos o dinheiro conforme a “conta” a que o atribuímos — lazer, salário, prêmio — como se R$ 100 valessem coisas diferentes. Isso <strong>viola a fungibilidade</strong> e abre a porta para vender o que sobe cedo demais, segurar o que cai, e cair no custo afundado: insistir num projeto ruim porque já se gastou nele.","tip":"<strong>Regra:</strong> avalie pelo patrimônio e pelo objetivo total, nunca pela conta mental isolada."},
      {"ic":"book","t":"Somos Humanos, Não Econs","emph":"Humanos","b":"A teoria econômica supõe os Econs — agentes frios que sempre maximizam. As pessoas reais são <strong>Humanos: previsivelmente irracionais</strong>, levados por enquadramento, contas mentais e inércia. Daí o poder dos bons defaults: como ninguém recalcula tudo, a opção padrão escolhida por outro acaba decidindo por nós.","tip":"<strong>Cuidado:</strong> persistir num projeto perdido por causa do custo já gasto — “já investi tanto…”.","warn":True},
    ],
  "lessons_title":"Lições-Chave do Capítulo 11",
  "lessons":["A forma de apresentar decide a escolha — reenquadre antes de fechar.","Contas mentais e custo afundado nos fazem violar a lógica econômica.","Somos Humanos previsíveis: bons defaults e arquitetura de escolha mudam resultados."]},

 {"slug":"ch12-os-dois-eus","sub":"CAPÍTULO 12: Os Dois Eus — Experiência vs. Memória",
  "intro":"Há dois 'eus' em conflito: o que experiencia vive cada momento; o que recorda guarda e julga a experiência depois. Decidimos pelo eu que recorda — que distorce sistematicamente o que vivemos.",
  "cards":[
      {"ic":"fork","t":"Quem Vive e Quem Lembra","emph":"Quem Lembra","b":"Há dois “eus” dentro de você: o que experiencia vive cada minuto enquanto ele passa; o que recorda <strong>guarda a história e é quem decide o futuro</strong>. O problema é que decidimos para agradar o eu que lembra — maximizamos a boa lembrança, não a soma real de bem-estar que de fato vivemos.","tip":"<strong>Como aplicar:</strong> decida pensando no eu que vai lembrar, mas viva atento ao eu que está experimentando agora.","wide":True},
      {"ic":"clock","t":"O Pico e o Fim Escrevem Tudo","emph":"o Fim","b":"A memória de um episódio não é a média de tudo: é a média do <strong>momento mais intenso com o momento final</strong>, e a duração quase não conta — a negligência da duração. Um procedimento longo que termina suave é lembrado como melhor que um curto e ruim no fim. O encerramento reescreve a experiência inteira.","tip":"<strong>Regra:</strong> para deixar boa memória, capriche no pico e no final — a duração mal entra na conta."},
      {"ic":"bulb","t":"Nada é Tão Importante Quanto Parece","emph":"Tão Importante","b":"“Nada na vida é tão importante quanto você pensa <strong>enquanto está pensando nisso</strong>.” É a ilusão do foco: ao mirar uma única coisa — um carro novo, mudar de cidade — ela parece capaz de transformar a vida. Mas a atenção se dispersa, a novidade desbota, e o impacto real encolhe muito abaixo do prometido.","tip":"<strong>Cuidado:</strong> escolher experiências pela “história que vou contar” em vez do bem-estar realmente vivido.","warn":True},
    ],
  "lessons_title":"Lições-Chave do Capítulo 12",
  "lessons":["Decidimos pela memória, não pela experiência vivida — e a memória mente.","Pico e final dominam a lembrança; a duração some.","A ilusão do foco superdimensiona o impacto de qualquer coisa em que você pense."]},
]
