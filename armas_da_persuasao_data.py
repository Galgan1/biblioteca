# -*- coding: utf-8 -*-
"""Conteúdo (pt-BR) das páginas da biblioteca para 'As Armas da Persuasão'
(Robert B. Cialdini). Frameworks: padrões fixos (clique-zumm), contraste, e os 6
princípios da influência (reciprocidade, compromisso/coerência, prova social,
afeição, autoridade, escassez) + a unidade como 7º. Para cada princípio: como
funciona e como se defender. Síntese atribuída — não reproduz o texto."""

BOOK = {
 "title": "As Armas da Persuasão",
 "author": "Robert B. Cialdini",
 "header_light": "AS ARMAS",
 "header_bold": "DA PERSUASÃO",
 "subtitle": "VISÃO GERAL · OS 6 PRINCÍPIOS DA INFLUÊNCIA",
 "intro": "Vivemos cercados de informação demais para analisar tudo, então decidimos por atalhos mentais disparados por um único gatilho. Eles costumam ajudar — mas viram armas nas mãos de quem sabe acioná-los. Cialdini mapeia seis (mais um) gatilhos universais do 'sim' automático: como cada um funciona, como é explorado e, sobretudo, como você se defende.",
 "description": "O clássico de Robert Cialdini sobre a psicologia do consentimento. Os padrões fixos de ação (o 'clique, zumm'), o contraste perceptivo e os 6 princípios universais da influência — reciprocidade, compromisso e coerência, aprovação/prova social, afeição, autoridade e escassez (mais a unidade como 7º). Para cada princípio: como funciona e como se proteger da manipulação.",
 "tags": ["Persuasão", "Influência", "Psicologia"],
 "progress": "8 Capítulos",
 "cover": "assets/armas-da-persuasao-cover.png",
 "overview_cards": [
   {"ic":"target","t":"Os 6 Princípios da Influência","b":"Toda persuasão eficaz aciona um destes gatilhos universais:","list":[
     "<strong>Reciprocidade</strong> — retribuímos o que recebemos.",
     "<strong>Compromisso e Coerência</strong> — agimos conforme o que já assumimos.",
     "<strong>Prova Social</strong> — fazemos o que os outros (parecidos) fazem.",
     "<strong>Afeição</strong> — dizemos sim a quem gostamos.",
     "<strong>Autoridade</strong> — obedecemos a (símbolos de) quem 'sabe'.",
     "<strong>Escassez</strong> — valorizamos o que é raro ou está acabando.",
   ],"tip":"<strong>Como usar:</strong> as edições novas somam a <strong>Unidade</strong> (o 'nós' de grupo) como 7º princípio.","wide":True},
   {"ic":"spark","t":"Clique, Zumm: os atalhos mentais","b":"Como animais com 'fitas gravadas', reagimos em série a <strong>um único traço-gatilho</strong> (preço alto = 'caro é bom'). O atalho é eficiente — e por isso explorável por quem imita o gatilho.","tip":"<strong>Modelo mental:</strong> o gatilho liga a reação inteira sem análise — útil, até ser falsificado."},
   {"ic":"key","t":"A chave é a defesa","b":"A saída não é desligar os atalhos (impossível), e sim <strong>reconhecer quando o gatilho foi fabricado</strong> e resistir ao trapaceiro, não ao atalho.","tip":"<strong>Regra-mãe:</strong> sentir-se ENGANADO (não só persuadido) é a deixa para recusar — sem culpa."},
 ],
}

CHAPTERS = [
 {"slug":"ch01-armas-da-influencia","sub":"CAPÍTULO 1: As Armas da Influência",
  "intro":"Temos informação demais para analisar tudo, então decidimos por atalhos disparados por um traço-gatilho. São úteis — até alguém imitar o gatilho para acionar a reação sem o conteúdo que a justifica.",
  "cards":[
   {"ic":"spark","t":"Padrões Fixos: Clique, Zumm","b":"Como o animal cuja 'fita gravada' toca inteira ao primeiro estímulo, reagimos em série a <strong>um único gatilho-chave</strong>. A heurística <strong>'caro = bom'</strong> é o exemplo: o preço alto liga a qualidade presumida.","tip":"<strong>Como aplicar:</strong> reserve a análise lenta para o que é caro ou irreversível; nesses casos, desligue o atalho."},
   {"ic":"scale","t":"O Contraste Perceptivo","b":"Julgamos cada coisa <strong>em relação à anterior</strong>, não em absoluto. Mostrado o caro primeiro, o seguinte parece barato (terno → suéter; casa cara → 'razoável').","tip":"<strong>Como se defender:</strong> avalie cada preço/oferta em absoluto, isolando-o do que foi mostrado logo antes.","wide":True},
   {"ic":"bulb","t":"Jiu-jítsu da Persuasão","b":"O profissional não empurra de fora — ele <strong>usa uma força que já está em você</strong> (a própria heurística). Por isso parece percepção, não manipulação.","tip":"<strong>Sinal de alerta:</strong> reação rápida e forte a um sinal isolado (preço, uniforme, 'porque...') é a fita tocando.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 1",
  "lessons":["A maioria das decisões usa atalhos; o problema é o gatilho fabricado.","Avalie em absoluto, não pelo contraste com o que veio antes.","Reserve a análise lenta para o que custa caro errar."]},

 {"slug":"ch02-reciprocidade","sub":"CAPÍTULO 2: Reciprocidade",
  "intro":"A regra mais difundida da cultura humana: sentimo-nos obrigados a retribuir o que recebemos. O favor — mesmo não pedido, mesmo pequeno — cria uma dívida que pagamos desproporcionalmente.",
  "cards":[
   {"ic":"link","t":"A Dívida do Favor","b":"Receber gera a <strong>obrigação de retribuir</strong>. Dar primeiro (amostra grátis, brinde, gentileza) aciona a dívida antes do pedido — e, para sair dela, aceitamos a troca desigual.","tip":"<strong>Como se defender:</strong> aceite favores genuínos, mas redefina o truque como truque — a regra não obriga a retribuir um ardil.","wide":True},
   {"ic":"pivot","t":"Rejeição-depois-recuo","b":"Peça muito (será recusado) e <strong>recue</strong> para o que você queria. A sua 'concessão' obriga a uma concessão de volta — e, somada ao contraste, o segundo pedido parece pequeno.","tip":"<strong>Sinal de alerta:</strong> pediram muito e 'cederam' para um pedido menor? É a tática agindo.","warn":True},
   {"ic":"gap","t":"A Troca Desigual","b":"O desconforto de dever pressiona até a <strong>retribuição maior que o recebido</strong>. O 'presente' não é presente — é gatilho plantado.","tip":"<strong>Modelo mental:</strong> pergunte quem deu primeiro e por quê antes de se sentir em dívida."},
  ],
  "lessons_title":"Lições-Chave do Capítulo 2",
  "lessons":["O favor inicial cria a dívida — note quem deu primeiro.","Na 'porta na cara', o recuo é o 'favor' que puxa sua concessão.","Defesa: retribuir não vale para um truque comercial."]},

 {"slug":"ch03-compromisso-coerencia","sub":"CAPÍTULO 3: Compromisso e Coerência",
  "intro":"Depois de assumir uma posição, sentimos forte pressão para agir de modo coerente com ela. Por isso um pequeno compromisso inicial abre a porta para concessões cada vez maiores.",
  "cards":[
   {"ic":"steps","t":"O Pé na Porta","b":"Um <strong>sim trivial</strong> muda a autoimagem e prepara o sim grande ('sou o tipo de pessoa que diz sim a isto'). O pedido cresce em etapas.","tip":"<strong>Como aplicar:</strong> comece por um compromisso pequeno; ele é a alavanca do grande."},
   {"ic":"key","t":"O que Faz o Compromisso 'Pegar'","b":"Vale mais quando é <strong>ativo, público, voluntário e trabalhoso</strong> — porque a pessoa cria as próprias 'pernas' (justificativas) que sustentam a decisão.","tip":"<strong>Como aplicar:</strong> peça o compromisso por escrito e diante de outros — gruda muito mais.","wide":True},
   {"ic":"eye","t":"Lowball (a bola baixa)","b":"Oferecer uma vantagem para gerar a decisão e depois <strong>removê-la</strong>: a decisão persiste porque já criou apoios próprios, mesmo sem o incentivo original.","tip":"<strong>Como se defender:</strong> escute o estômago ('estou sendo coagido?') e o coração ('decidiria assim de novo agora?').","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 3",
  "lessons":["Um sim pequeno, ativo e público predispõe ao grande.","Cuidado com o lowball: a vantagem some, a decisão fica.","Defesa: consulte o estômago e o coração antes de honrar o compromisso."]},

 {"slug":"ch04-aprovacao-social","sub":"CAPÍTULO 4: Aprovação Social",
  "intro":"Determinamos o que é correto descobrindo o que os outros acham correto. O atalho é mais forte sob incerteza (não sei o que fazer) e diante de pessoas semelhantes a mim.",
  "cards":[
   {"ic":"constellation","t":"Prova Social: incerteza + semelhança","b":"'Se muitos fazem, deve estar certo' — e pesa <strong>mais sob incerteza</strong> e diante de pessoas <strong>parecidas comigo</strong>. Daí 'o mais vendido', filas e depoimentos.","tip":"<strong>Como se defender:</strong> muitos errados não fazem um certo — cheque os fatos, não só a manada.","wide":True},
   {"ic":"eye","t":"Ignorância Pluralística","b":"Numa emergência com muitos presentes, cada um lê a calma alheia como 'não é grave' — e <strong>ninguém age</strong> (efeito espectador).","tip":"<strong>Como se defender:</strong> caído na rua? aponte UMA pessoa: 'você, de azul, chame a ambulância'."},
   {"ic":"wave","t":"O Efeito Werther","b":"Ondas de imitação (ex.: suicídios) sobem após ampla cobertura da mídia — a prova social no <strong>extremo trágico</strong>.","tip":"<strong>Sinal de alerta:</strong> desconfie de prova social fabricada (avaliações falsas, plateia paga, números inflados).","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 4",
  "lessons":["A prova social pesa mais sob incerteza e entre semelhantes.","Multidão não é verdade — cheque os fatos.","Em emergência, individualize o pedido de ajuda."]},

 {"slug":"ch05-afeicao","sub":"CAPÍTULO 5: Afeição",
  "intro":"Preferimos dizer sim a quem gostamos — e muitos fatores fazem gostar mais rápido do que percebemos. O perigo é o vínculo afetivo, fabricado de propósito, decidir por nós.",
  "cards":[
   {"ic":"bubble","t":"Os Cinco Fatores da Simpatia","b":"Gostamos mais por: <strong>atratividade</strong> (efeito halo), <strong>semelhança</strong>, <strong>elogios</strong> (mesmo bajulação), <strong>familiaridade/cooperação</strong> e <strong>associação</strong> (ligar-se ao agradável).","tip":"<strong>Como se defender:</strong> ao gostar rápido e demais de quem vende, pergunte por quê e isole a pessoa do negócio.","wide":True},
   {"ic":"link","t":"O Princípio da Associação","b":"Transferimos sentimentos por contiguidade: comida boa, celebridades, 'meu time ganhou'. Por isso o produto vem colado a <strong>beleza, sucesso e esporte</strong>.","tip":"<strong>Modelo mental:</strong> associação é contágio — o que está perto do produto 'cola' nele."},
   {"ic":"mask","t":"O Vendedor 'Amigo'","b":"No método Tupperware, quem vende é uma <strong>amiga</strong> (afeição + reciprocidade + compromisso público). Recusar a oferta vira recusar a amiga.","tip":"<strong>Como se defender:</strong> separe o sentimento pela pessoa da decisão sobre o negócio.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 5",
  "lessons":["Atratividade, semelhança, elogio, familiaridade e associação fazem dizer sim.","Associação transfere sentimentos: cuidado com o que ligam ao produto.","Defesa: isole o negócio da pessoa que vende."]},

 {"slug":"ch06-autoridade","sub":"CAPÍTULO 6: Autoridade",
  "intro":"Somos treinados a obedecer à autoridade legítima — atalho útil, mas que dispara mesmo diante de meros símbolos dela, sem checar a substância por trás.",
  "cards":[
   {"ic":"layers","t":"Os Três Símbolos","b":"Cedemos a <strong>títulos</strong> (Dr., Professor), <strong>roupas</strong> (jaleco, terno, uniforme) e <strong>adereços</strong> (carro de luxo, joias) — sinais de status fáceis de alegar e difíceis de verificar.","tip":"<strong>Como se defender:</strong> pergunte 'esta autoridade é mesmo especialista NISTO?' — ela vale só na área dela.","wide":True},
   {"ic":"eye","t":"Aparência vs. Substância","b":"O gatilho é o <strong>símbolo</strong>, não a competência real — e o símbolo pode ser falsificado. O jaleco não é o médico.","tip":"<strong>Como se defender:</strong> a segunda pergunta — 'quão sincera ela está sendo aqui?' (qual o interesse dela)."},
   {"ic":"gap","t":"O Experimento de Milgram","b":"Pessoas comuns aplicaram (acreditavam) choques crescentes a outra só porque um 'cientista' de jaleco mandava — a maioria foi <strong>até o fim</strong>. A força bruta da obediência ao símbolo.","tip":"<strong>Sinal de alerta:</strong> obedecer a quem só VESTE a autoridade (título alegado, uniforme) é o risco.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 6",
  "lessons":["Reagimos a símbolos (título, roupa, adereço), não à competência real.","A autoridade só vale na sua área específica.","Defesa: 'é mesmo especialista nisto?' e 'quão sincera está sendo aqui?'."]},

 {"slug":"ch07-escassez","sub":"CAPÍTULO 7: Escassez",
  "intro":"Atribuímos mais valor ao que é raro ou está acabando. A perda potencial pesa mais que o ganho — e a sensação de oportunidade fugindo aciona o impulso de agarrar antes de pensar.",
  "cards":[
   {"ic":"clock","t":"Os Três Gatilhos da Escassez","b":"<strong>Quantidade limitada</strong> ('últimas unidades'), <strong>prazo</strong> ('só hoje', contagem regressiva) e <strong>censura/proibição</strong> (o restrito ganha valor). Raro = mais desejável.","tip":"<strong>Como se defender:</strong> raridade muda quanto você QUER, não quanto SERVE — separe 'querer ter' de 'ser útil'.","wide":True},
   {"ic":"spiral","t":"Reatância: o proibido seduz","b":"Quando uma liberdade (de ter/escolher) é ameaçada, <strong>desejamos mais</strong> essa opção (teoria de Brehm). Proibir aumenta o querer; a perda dói mais que o ganho equivalente.","tip":"<strong>Sinal de alerta:</strong> querer algo só porque foi restringido/proibido é a reatância no comando.","warn":True},
   {"ic":"target","t":"Escassez + Competição","b":"'Só resta uma — e outro cliente já vem buscar.' Quantidade limitada somada à <strong>disputa</strong> dispara o pico de impulso de fechar na hora.","tip":"<strong>Como se defender:</strong> a onda de excitação/posse é o ALARME — pare e pergunte 'útil ou só raro?'."},
  ],
  "lessons_title":"Lições-Chave do Capítulo 7",
  "lessons":["Raridade, prazo e proibição inflam o desejo, não o valor de uso.","A perda dói mais que o ganho: a ameaça de perder distorce o juízo.","Defesa: use a própria excitação como gatilho de pausa."]},

 {"slug":"ch08-defesa-e-unidade","sub":"CAPÍTULO 8: Defesa e Unidade",
  "intro":"Os atalhos são necessários — não dá para analisar tudo. A defesa não é abandoná-los, e sim reconhecer quando o gatilho foi falsificado e reagir contra o explorador, não contra o atalho.",
  "cards":[
   {"ic":"lens","t":"Vigilância Seletiva","b":"Na 'era automática', decidimos cada vez mais por gatilho único. A contramedida é a <strong>análise lenta só quando o custo do erro é alto</strong> — não tentar (nem conseguir) examinar tudo.","tip":"<strong>Regra-mãe:</strong> aceite o atalho com gatilho autêntico; resista quando o gatilho é fabricado.","wide":True},
   {"ic":"constellation","t":"Unidade (o 7º princípio)","b":"Mais forte que 'gostar do parecido': o <strong>'nós' compartilhado</strong> — família, lugar, identidade de grupo. Quando o outro é sentido como parte do 'eu coletivo', ele convence sem argumento.","tip":"<strong>Como se defender:</strong> confirme se o 'um de nós' é real ou forjado para baixar sua guarda."},
   {"ic":"key","t":"A Bússola da Defesa","b":"A sensação de ter sido <strong>ENGANADO</strong> — não apenas persuadido — é a deixa para recusar e contra-atacar, sem culpa. Não brigue com o atalho; brigue com o trapaceiro.","tip":"<strong>Resumo dos 6+1:</strong> reciprocidade→não a truque · coerência→estômago+coração · prova social→cheque fatos · afeição→isole o negócio · autoridade→especialista e sincera? · escassez→excitação é pausa · unidade→o 'nós' é real?"},
  ],
  "lessons_title":"Lições-Chave do Capítulo 8",
  "lessons":["A defesa não é desligar os atalhos, é detectar o gatilho falsificado.","Vigilância seletiva: análise lenta onde o erro custa caro.","A Unidade ('um de nós') é o 7º princípio — confirme se é real."]},
]
