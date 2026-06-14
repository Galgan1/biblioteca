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
   {"ic":"spark","t":"Sistema 1 (pensar rápido)","b":"Opera de forma <strong>automática e veloz</strong>, com pouco ou nenhum esforço e nenhuma sensação de controle voluntário. É o piloto automático que gera impressões, intuições e impulsos.","tip":"<strong>Como aplicar:</strong> reconheça que a resposta imediata quase sempre é do S1 — útil, mas falível.","wide":True},
   {"ic":"clock","t":"Sistema 2 (pensar devagar)","b":"Aloca <strong>atenção</strong> às tarefas mentais que exigem esforço — cálculo, comparação, autocontrole. É lento, custoso e <strong>preguiçoso</strong>: tende a endossar o S1 sem checar.","tip":"<strong>Regra:</strong> acione o S2 de propósito quando o tema for complexo ou a aposta for alta."},
   {"ic":"mask","t":"O Supervisor Preguiçoso","b":"O S2 é o 'eu' que você acredita ser, mas o S1 é quem realmente dirige. O S2 costuma <strong>racionalizar</strong> a impressão do S1 em vez de questioná-la.","tip":"<strong>Cuidado:</strong> achar que 'decidiu racionalmente' quando o S1 já entregou a resposta e o S2 só assinou.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 1",
  "lessons":["Quase tudo o que você pensa e faz começa no Sistema 1.","O Sistema 2 é lento e preguiçoso — por isso os erros do S1 passam.","O primeiro passo para decidir melhor é saber em qual sistema você está."]},

 {"slug":"ch02-atencao-esforco-piloto-automatico","sub":"CAPÍTULO 2: Atenção, Esforço e Piloto Automático",
  "intro":"O Sistema 2 é caro: pensar com esforço consome um recurso limitado, gera fadiga e tende à lei do menor esforço. Por isso a mente delega quase tudo ao Sistema 1 e só 'acorda' o S2 quando obrigada.",
  "cards":[
   {"ic":"leaf","t":"Lei do Menor Esforço","b":"Dadas várias formas de chegar ao mesmo objetivo, a mente escolhe a <strong>menos exigente</strong>. Pensar dói — por isso pulamos a checagem deliberada.","tip":"<strong>Como aplicar:</strong> não conte com a força de vontade o dia todo; estruture o ambiente para precisar menos dela.","wide":True},
   {"ic":"scale","t":"Esgotamento do Ego","b":"Autocontrole e pensamento esforçado puxam do <strong>mesmo poço</strong>: usar um esgota o outro. Cansaço, fome e multitarefa entregam o controle ao Sistema 1.","tip":"<strong>Regra:</strong> evite decisões importantes cansado, com fome ou multitarefando."},
   {"ic":"eye","t":"Cegueira por Desatenção","b":"Foco intenso torna invisível o óbvio — o experimento do <strong>gorila invisível</strong>: contando passes, metade não vê uma pessoa fantasiada cruzar a cena. Atenção é finita.","tip":"<strong>Cuidado:</strong> supor que 'prestar atenção' garante ver o relevante — o foco custa periferia.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 2",
  "lessons":["Pensar com esforço é caro; a mente economiza por padrão.","Cansaço, fome e multitarefa dão o controle ao Sistema 1.","Desenhe o contexto para depender menos da força de vontade."]},

 {"slug":"ch03-wysiati-coerencia","sub":"CAPÍTULO 3: WYSIATI e a Máquina de Saltar a Conclusões",
  "intro":"O Sistema 1 constrói a história mais coerente possível com a informação disponível e a trata como toda a verdade. WYSIATI: 'o que você vê é tudo que há' — não levamos em conta o que não sabemos.",
  "cards":[
   {"ic":"eye","t":"WYSIATI","b":"O Sistema 1 julga só pela informação <strong>ativada</strong>, ignorando a ausência de dados. Daí o excesso de confiança: a história coerente <strong>parece</strong> completa.","tip":"<strong>Como aplicar:</strong> pergunte 'o que falta que eu não estou vendo — e como mudaria a conclusão?'.","wide":True},
   {"ic":"link","t":"Coerência & Efeito de Halo","b":"Ideias ativam ideias relacionadas em cascata; uma narrativa fluida vira 'verdade' sentida. Uma primeira impressão (boa ou má) <strong>contamina</strong> traços não observados (halo).","tip":"<strong>Modelo mental:</strong> a confiança mede a coerência da história, não a quantidade de evidência."},
   {"ic":"bubble","t":"Facilidade Cognitiva","b":"O que é fácil de processar — familiar, claro, <strong>repetido</strong> — parece mais verdadeiro, bom e seguro. A mera repetição cria a <strong>ilusão de verdade</strong>.","tip":"<strong>Cuidado:</strong> tomar a fluência (soou claro e familiar) como sinal de verdade.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 3",
  "lessons":["Julgamos com o que está ativado, não com o que é relevante.","Facilidade e repetição forjam sensação de verdade.","Quanto menos você sabe, mais fácil (e errado) é montar uma história coerente."]},

 {"slug":"ch04-substituicao-heuristicas","sub":"CAPÍTULO 4: Substituição e o Mecanismo das Heurísticas",
  "intro":"Diante de uma pergunta difícil, o Sistema 1 a substitui por uma pergunta mais fácil e responde a esta sem perceber a troca. Heurísticas são atalhos úteis que produzem vieses sistemáticos.",
  "cards":[
   {"ic":"pivot","t":"Substituição de Atributo","b":"Troca-se a pergunta difícil (a <strong>alvo</strong>) por uma fácil e relacionada (a <strong>heurística</strong>) — e responde-se a esta. A resposta vem rápida e confiante demais para a dificuldade real.","tip":"<strong>Como aplicar:</strong> isole a pergunta-alvo da pergunta fácil que você realmente respondeu.","wide":True},
   {"ic":"wave","t":"Heurística do Afeto","b":"Deixar o <strong>gostar/temer</strong> guiar crenças sobre o mundo: se gosto de algo, julgo seus riscos baixos e benefícios altos — mesmo sem dados.","tip":"<strong>Modelo mental:</strong> o afeto vem antes do argumento — a conclusão emocional chega primeiro."},
   {"ic":"target","t":"Gostar ≠ Verdadeiro","b":"Confundir '<strong>isso me parece bom/ruim</strong>' com '<strong>isso é provavelmente verdadeiro/seguro</strong>' é o erro central da substituição.","tip":"<strong>Cuidado:</strong> tomar a fluência da resposta como prova de que respondeu à pergunta certa.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 4",
  "lessons":["Diante de perguntas difíceis, respondemos a outras mais fáceis sem perceber.","O afeto (gostar/temer) é a heurística mais comum e poderosa.","Para checar um julgamento, separe a pergunta-alvo da que você de fato respondeu."]},

 {"slug":"ch05-ancoragem","sub":"CAPÍTULO 5: Ancoragem",
  "intro":"Ao estimar um valor, um número apresentado antes — mesmo arbitrário e irrelevante — ancora o julgamento e o puxa em sua direção. A ancoragem é um dos vieses mais robustos e mensuráveis.",
  "cards":[
   {"ic":"pin","t":"Efeito de Ancoragem","b":"Estimativas <strong>gravitam</strong> em torno de qualquer número considerado antes de estimar — até uma roleta viciada ou dígitos aleatórios deslocam a resposta.","tip":"<strong>Como aplicar:</strong> em negociação, abra com a sua âncora — quem fala o primeiro número define o campo.","wide":True},
   {"ic":"steps","t":"Dois Motores da Âncora","b":"<strong>Ajuste insuficiente</strong> (o S2 parte da âncora e para cedo) somado à <strong>ativação seletiva</strong> (o S1 recruta evidências compatíveis com ela).","tip":"<strong>Regra:</strong> ancore conscientemente e desconfie de qualquer número visto antes de estimar."},
   {"ic":"sword","t":"Defesa: Pensar o Oposto","b":"A ancoragem age <strong>mesmo</strong> quando você sabe que a âncora é irrelevante. Achar que 'ignorou' o número absurdo é a armadilha.","tip":"<strong>Cuidado:</strong> deixar a outra parte abrir a negociação sem ter a sua própria âncora pronta.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 5",
  "lessons":["Qualquer número visto antes de estimar puxa a estimativa em sua direção.","A ancoragem age mesmo quando você sabe que a âncora é irrelevante.","Defenda-se pensando ativamente o oposto da âncora."]},

 {"slug":"ch06-disponibilidade-representatividade","sub":"CAPÍTULO 6: Disponibilidade e Representatividade",
  "intro":"Estimamos probabilidades por dois atalhos falhos: a disponibilidade (o que vem fácil à mente parece mais frequente) e a representatividade (julgamos pela semelhança ao estereótipo, ignorando a estatística).",
  "cards":[
   {"ic":"wave","t":"Heurística da Disponibilidade","b":"A <strong>facilidade de lembrar</strong> exemplos vira medida de frequência. Eventos vívidos, recentes ou midiáticos (acidentes de avião) parecem mais prováveis do que são.","tip":"<strong>Como aplicar:</strong> avalie risco pela frequência real, não pela última manchete.","wide":True},
   {"ic":"constellation","t":"Heurística da Representatividade","b":"Julga-se pertinência a uma categoria pela <strong>semelhança ao protótipo</strong>, não pela probabilidade. O pecado: ignorar a <strong>taxa-base</strong> (quão comum algo é).","tip":"<strong>Regra:</strong> antes de julgar um caso, pergunte 'quão comum isso é na população?'."},
   {"ic":"gap","t":"Negligência da Taxa-Base","b":"Ignorar a <strong>frequência de base</strong> ao julgar um caso específico. 'Parece o tipo' ≠ 'é provável' — há muito mais agricultores que bibliotecários.","tip":"<strong>Cuidado:</strong> deixar o estereótipo gritar mais alto que a estatística.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 6",
  "lessons":["Frequência percebida segue a facilidade de lembrar, não os dados.","Semelhança ao estereótipo nos faz ignorar a estatística de base.","Antes de julgar, ancore na taxa-base — depois ajuste pela evidência."]},

 {"slug":"ch07-linda-regressao","sub":"CAPÍTULO 7: A Falácia da Conjunção (Linda) e a Regressão à Média",
  "intro":"A representatividade gera dois erros clássicos: achar que um cenário detalhado é mais provável que um genérico (Linda) e ignorar que valores extremos voltam à média sem causa nenhuma (regressão).",
  "cards":[
   {"ic":"layers","t":"Falácia da Conjunção (Linda)","b":"Julgar 'A e B' mais provável que só 'A' porque a combinação é mais <strong>representativa</strong>. Mas <strong>P(A e B) nunca supera P(A)</strong> — cada detalhe a mais reduz a probabilidade.","tip":"<strong>Como aplicar:</strong> entre o cenário rico e o simples, escolha o simples — ele é mais provável.","wide":True},
   {"ic":"spiral","t":"Regressão à Média","b":"Após um resultado <strong>extremo</strong>, o próximo tende a ficar mais perto da média — por puro acaso. Inventamos causa: 'a bronca funcionou', 'o elogio estragou'.","tip":"<strong>Regra:</strong> antes de explicar uma melhora/piora, pergunte 'não seria só regressão à média?'."},
   {"ic":"mask","t":"Plausível ≠ Provável","b":"Uma história rica em detalhes é mais <strong>convincente</strong> e menos <strong>provável</strong>. A coerência engana a lógica.","tip":"<strong>Cuidado:</strong> dar a uma intervenção o crédito por uma melhora que era estatística.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 7",
  "lessons":["Adicionar detalhes plausíveis aumenta a credibilidade e diminui a probabilidade.","Resultados extremos regridem à média sozinhos — não invente causa.","Desconfie de explicações causais para o que pode ser mero acaso."]},

 {"slug":"ch08-ilusao-validade-intuicao","sub":"CAPÍTULO 8: A Ilusão de Validade e a Intuição de Especialistas",
  "intro":"A confiança que sentimos não mede a precisão de um julgamento — mede a coerência da história. Em ambientes irregulares (bolsa, política), especialistas têm intuições tão válidas quanto adivinhação, com confiança altíssima.",
  "cards":[
   {"ic":"lens","t":"Ilusão de Validade","b":"Confiança subjetiva <strong>descolada</strong> da acurácia objetiva: sentir-se certo não é estar certo. Sobrevive até quando a evidência mostra que o julgamento não prevê nada.","tip":"<strong>Como aplicar:</strong> trate confiança alta em terreno imprevisível como alarme, não garantia.","wide":True},
   {"ic":"key","t":"Quando Confiar na Intuição","b":"A intuição de especialista só vale com (1) <strong>ambiente regular</strong> e (2) <strong>feedback</strong> rápido e claro para aprendê-lo. Bombeiro e enxadrista: sim; analista de bolsa: não.","tip":"<strong>Regra:</strong> sem ambiente regular e feedback de qualidade, não confie na intuição."},
   {"ic":"scale","t":"Fórmulas > Julgamento","b":"Algoritmos simples e <strong>consistentes</strong> superam o julgamento clínico humano na maioria das previsões — humanos discordam até de si mesmos.","tip":"<strong>Cuidado:</strong> tratar a confiança de um especialista como prova de acerto.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 8",
  "lessons":["Confiança é a sensação de coerência, não a medida da precisão.","Intuição só é confiável em ambientes regulares com bom feedback.","Em terreno ruidoso, regras simples e consistentes vencem o julgamento humano."]},

 {"slug":"ch09-excesso-confianca-pre-mortem","sub":"CAPÍTULO 9: Excesso de Confiança, Visão de Fora e o Pré-Mortem",
  "intro":"Subestimamos prazos, custos e riscos porque planejamos pela 'visão de dentro' (otimista) em vez da 'visão de fora' (a estatística de casos parecidos). O excesso de confiança é a mais danosa das ilusões.",
  "cards":[
   {"ic":"lens","t":"Visão de Dentro × Visão de Fora","b":"A <strong>falácia do planejamento</strong>: previmos pelo melhor cenário, ignorando atrasos típicos. A correção é a <strong>visão de fora</strong> — a taxa-base de projetos semelhantes.","tip":"<strong>Como aplicar:</strong> pergunte 'como foram os projetos parecidos com este?' antes de confiar na sua estimativa.","wide":True},
   {"ic":"sword","t":"Pré-Mortem","b":"Antes de decidir, imagine que já se passou um ano e o projeto <strong>fracassou</strong>; cada um escreve a história do desastre. Legitima a dúvida e revela riscos que o entusiasmo escondia.","tip":"<strong>Regra:</strong> convide o fracasso para a mesa antes de começar — é mais barato imaginá-lo agora."},
   {"ic":"mountain","t":"Otimismo & Negligência da Concorrência","b":"Superestimamos o controle e <strong>esquecemos os rivais</strong> fazendo o mesmo. O otimismo de grupo cega — atraso e estouro são a regra, não a exceção.","tip":"<strong>Cuidado:</strong> silenciar a dúvida porque 'a equipe está animada'.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 9",
  "lessons":["Planejamos pelo melhor caso e por isso quase sempre estouramos prazo e custo.","A visão de fora (taxa-base de projetos parecidos) corrige o otimismo.","Um pré-mortem barato hoje evita um post-mortem caro depois."]},

 {"slug":"ch10-teoria-do-prospecto","sub":"CAPÍTULO 10: Teoria do Prospecto — Aversão à Perda e Ponto de Referência",
  "intro":"Contra a economia clássica, avaliamos resultados como ganhos e perdas em relação a um ponto de referência — e perder dói cerca de duas vezes mais do que ganhar agrada.",
  "cards":[
   {"ic":"scale","t":"Aversão à Perda","b":"A curva das perdas é mais íngreme: <strong>perdas pesam ~2× os ganhos</strong> equivalentes. Por isso recusamos apostas justas e seguramos perdedores.","tip":"<strong>Como aplicar:</strong> não recuse uma aposta favorável só porque a dor da perda grita mais alto.","wide":True},
   {"ic":"pin","t":"Ponto de Referência","b":"Julgamos <strong>mudanças</strong> a partir de um status quo, não níveis absolutos — com <strong>sensibilidade decrescente</strong> (R$ 100→200 pesa mais que R$ 1.100→1.200).","tip":"<strong>Modelo mental:</strong> mude o ponto de referência e a mesma situação vira ganho ou perda."},
   {"ic":"key","t":"Efeito Posse & Ponderação de Probabilidades","b":"Valorizamos mais algo só por <strong>possuí-lo</strong> (efeito posse); e <strong>superpesamos</strong> eventos raros e a certeza absoluta (loterias, seguros).","tip":"<strong>Cuidado:</strong> segurar um investimento ruim só para não 'realizar' a perda.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 10",
  "lessons":["Avaliamos mudanças a partir de um ponto de referência, não a riqueza final.","Perdas pesam cerca do dobro dos ganhos equivalentes.","Superpesamos a certeza e os eventos raros, distorcendo seguros e loterias."]},

 {"slug":"ch11-enquadramento-contabilidade-mental","sub":"CAPÍTULO 11: Enquadramento, Contabilidade Mental e Econs vs. Humanos",
  "intro":"A mesma informação descrita de formas diferentes produz decisões diferentes — porque o Sistema 1 reage à apresentação, não à substância. Somos Humanos previsivelmente irracionais, não Econs.",
  "cards":[
   {"ic":"lens","t":"Efeito Enquadramento (Framing)","b":"A forma de apresentar — 'salva 200' vs. 'deixa 400 morrerem', '90% magro' vs. '10% gordura' — <strong>altera a escolha sem mudar os fatos</strong>.","tip":"<strong>Como aplicar:</strong> reenquadre/inverta toda decisão importante antes de fechar.","wide":True},
   {"ic":"layers","t":"Contabilidade Mental","b":"Tratamos dinheiro diferente conforme a 'conta' (lazer, salário, prêmio), violando a <strong>fungibilidade</strong>. Daí o efeito disposição e a armadilha do <strong>custo afundado</strong>.","tip":"<strong>Regra:</strong> avalie pelo patrimônio/objetivo total, não pela conta isolada."},
   {"ic":"book","t":"Econs vs. Humanos","b":"A economia supõe agentes racionais (<strong>Econs</strong>); pessoas reais (<strong>Humanos</strong>) são previsivelmente irracionais — por isso bons <strong>defaults</strong> mudam resultados.","tip":"<strong>Cuidado:</strong> persistir num projeto perdido por causa do custo já gasto ('já investi tanto…').","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 11",
  "lessons":["A forma de apresentar decide a escolha — reenquadre antes de fechar.","Contas mentais e custo afundado nos fazem violar a lógica econômica.","Somos Humanos previsíveis: bons defaults e arquitetura de escolha mudam resultados."]},

 {"slug":"ch12-os-dois-eus","sub":"CAPÍTULO 12: Os Dois Eus — Experiência vs. Memória",
  "intro":"Há dois 'eus' em conflito: o que experiencia vive cada momento; o que recorda guarda e julga a experiência depois. Decidimos pelo eu que recorda — que distorce sistematicamente o que vivemos.",
  "cards":[
   {"ic":"fork","t":"Eu que Experiencia × Eu que Recorda","b":"Um <strong>sente o agora</strong>; o outro <strong>escreve a história</strong> e decide o futuro. Maximizamos a lembrança da experiência, não a soma do bem-estar vivido.","tip":"<strong>Como aplicar:</strong> decida pensando no eu que vai lembrar, mas viva pensando no que está experimentando.","wide":True},
   {"ic":"clock","t":"Regra do Pico-Fim","b":"A memória de um episódio é a média do <strong>momento mais intenso (pico)</strong> com o <strong>final</strong> — e a <strong>duração quase não conta</strong> (negligência da duração).","tip":"<strong>Regra:</strong> para deixar boa memória, capriche no pico e no final, não na duração."},
   {"ic":"bulb","t":"Ilusão do Foco","b":"'Nada na vida é tão importante quanto você pensa <strong>enquanto está pensando nisso</strong>.' Comprar X promete felicidade duradoura — mas a novidade some.","tip":"<strong>Cuidado:</strong> escolher experiências pela 'história que vou contar' em vez do bem-estar vivido.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 12",
  "lessons":["Decidimos pela memória, não pela experiência vivida — e a memória mente.","Pico e final dominam a lembrança; a duração some.","A ilusão do foco superdimensiona o impacto de qualquer coisa em que você pense."]},
]
