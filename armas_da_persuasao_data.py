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
      {"ic":"spark","t":"Clique, e a Fita Toca Inteira","emph":"a Fita Toca Inteira","b":"Como a perua que aquece qualquer bola de penas que faça “piu-piu”, agimos por fitas gravadas: um único traço-gatilho dispara a reação inteira, sem análise. “Caro é bom”, “todo mundo faz” — o atalho poupa o esforço de pensar. <strong>O problema nunca é o atalho; é quem imita o gatilho e aciona a reação sem o conteúdo que a justificava.</strong>","tip":"<strong>Modelo mental:</strong> o gatilho liga a fita inteira de uma vez — útil até virar falsificável."},
      {"ic":"scale","t":"O Contraste é Invisível","emph":"Invisível","b":"A mente não mede em absoluto — mede em relação ao que veio logo antes. Depois da casa cara, a “razoável” parece pechincha; depois do terno, o suéter caro vira detalhe. <strong>Quem mostra o item caro primeiro não está informando, está calibrando o seu juízo</strong> — e você sente isso como percepção, não como manobra.","tip":"<strong>Como se defender:</strong> avalie cada preço sozinho, isolado do que foi exibido um segundo antes.","wide":True},
      {"ic":"bulb","t":"Jiu-jítsu, Não Empurrão","emph":"Não Empurrão","b":"O persuasor hábil não te empurra de fora — usa uma força que já mora em você, a sua própria heurística, e deixa a gravidade fazer o resto. Por isso a manobra não parece pressão: parece descoberta sua. <strong>Ele gasta pouca energia e some da cena</strong>, enquanto o gatilho plantado trabalha sozinho dentro da sua cabeça.","tip":"<strong>Sinal de alerta:</strong> reação rápida e forte a um sinal isolado — preço, jaleco, “porque…” — é a fita tocando.","warn":True},
    ],
  "lessons_title":"Lições-Chave do Capítulo 1",
  "lessons":["A maioria das decisões usa atalhos; o problema é o gatilho fabricado.","Avalie em absoluto, não pelo contraste com o que veio antes.","Reserve a análise lenta para o que custa caro errar."]},

 {"slug":"ch02-reciprocidade","sub":"CAPÍTULO 2: Reciprocidade",
  "intro":"A regra mais difundida da cultura humana: sentimo-nos obrigados a retribuir o que recebemos. O favor — mesmo não pedido, mesmo pequeno — cria uma dívida que pagamos desproporcionalmente.",
  "cards":[
      {"ic":"link","t":"Toda Dádiva Cria uma Dívida","emph":"uma Dívida","b":"Nenhuma sociedade sobreviveu sem a regra de retribuir — e ela é tão profunda que dispara até com o favor que você não pediu. A amostra grátis, o cafezinho, o brinde plantam um desconforto surdo de “estou devendo”. <strong>Para sair da dívida aceitamos pagar mais do que recebemos</strong> — e é por isso que o “presente” chega antes do pedido.","tip":"<strong>Como se defender:</strong> aceite favores genuínos, mas redefina o ardil como ardil — a regra não obriga a retribuir um truque.","wide":True},
      {"ic":"pivot","t":"A Porta na Cara","emph":"na Cara","b":"Peça muito, ouça o “não” esperado e recue para o pedido menor — o que sempre quis. Seu recuo é lido como concessão, e a regra cobra outra de volta. O escoteiro oferece o ingresso caro, é recusado, emenda “então leva umas barras?” — e você leva chocolate sem gostar. <strong>O segundo pedido parece pequeno só por contraste com o primeiro.</strong>","tip":"<strong>Sinal de alerta:</strong> pediram demais e “cederam” para um pedido menor? É a tática, não generosidade.","warn":True},
      {"ic":"gap","t":"O Presente que Não é Presente","emph":"Não é Presente","b":"A força da reciprocidade está em quem dá primeiro — porque quem dá escolhe o que será trocado e quanto pesará a dívida. O Hare Krishna entrega a flor antes de pedir o donativo: a flor custa centavos e a culpa custa caro. <strong>Quando o “mimo” chega cedo demais, ele raramente é cortesia: é um gancho lançado para fisgar o seu “sim”.</strong>","tip":"<strong>Modelo mental:</strong> antes de se sentir em dívida, pergunte quem deu primeiro — e por quê deu."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 2",
  "lessons":["O favor inicial cria a dívida — note quem deu primeiro.","Na 'porta na cara', o recuo é o 'favor' que puxa sua concessão.","Defesa: retribuir não vale para um truque comercial."]},

 {"slug":"ch03-compromisso-coerencia","sub":"CAPÍTULO 3: Compromisso e Coerência",
  "intro":"Depois de assumir uma posição, sentimos forte pressão para agir de modo coerente com ela. Por isso um pequeno compromisso inicial abre a porta para concessões cada vez maiores.",
  "cards":[
      {"ic":"steps","t":"O Pé na Porta","emph":"na Porta","b":"Um “sim” trivial não custa nada — e é por isso que é a alavanca. O adesivo de “motorista cuidadoso” reescreve quem você acha que é; depois, você cede o jardim ao outdoor enorme e feio, pois já virou “o cidadão engajado”. <strong>O pedido cresce em etapas, e cada passo parece coerente com o anterior</strong> — ninguém recua do que declarou ser.","tip":"<strong>Como aplicar:</strong> repare em qual “sim” pequeno você assinou antes do grande — é a alavanca escondida."},
      {"ic":"key","t":"O que Faz o Compromisso Pegar","emph":"Pegar","b":"Nem todo “sim” gruda igual. O compromisso fixa quando é ativo, público, voluntário e trabalhoso — porque aí a pessoa cria sozinha as próprias “pernas”, que seguram a decisão sem o motivo original. <strong>O que escrevemos de próprio punho e diante dos outros passa a nos governar</strong> — o esforço que custou vira prova de que valeu.","tip":"<strong>Modelo mental:</strong> compromisso por escrito e diante de testemunhas cria âncoras que decidem por você depois.","wide":True},
      {"ic":"eye","t":"A Bola Baixa","emph":"Baixa","b":"Ofereça uma vantagem boa demais, deixe a decisão ser tomada e então remova a vantagem — a decisão fica de pé, porque já criou apoios próprios. É o desconto que “acabou” depois do “sim”, o carro cujo preço sobe na assinatura. <strong>A escolha sobrevive ao incentivo que a gerou, sustentada por razões que você mesmo inventou.</strong>","tip":"<strong>Como se defender:</strong> escute o estômago (“estou sendo coagido?”) e o coração (“decidiria assim de novo, agora?”).","warn":True},
    ],
  "lessons_title":"Lições-Chave do Capítulo 3",
  "lessons":["Um sim pequeno, ativo e público predispõe ao grande.","Cuidado com o lowball: a vantagem some, a decisão fica.","Defesa: consulte o estômago e o coração antes de honrar o compromisso."]},

 {"slug":"ch04-aprovacao-social","sub":"CAPÍTULO 4: Aprovação Social",
  "intro":"Determinamos o que é correto descobrindo o que os outros acham correto. O atalho é mais forte sob incerteza (não sei o que fazer) e diante de pessoas semelhantes a mim.",
  "cards":[
      {"ic":"constellation","t":"Incerteza e Semelhança","emph":"Semelhança","b":"Na dúvida, decidimos o que é certo olhando o que os outros fazem — e o atalho pesa mais quando estamos incertos (não sei agir, então copio) e diante de gente parecida comigo (são como eu, devem saber). <strong>Daí o poder do “mais vendido”, da fila e do depoimento de alguém igual a você</strong>: provam pela quantidade, não pelo mérito.","tip":"<strong>Como se defender:</strong> muitos errados não fazem um certo — cheque os fatos, não o tamanho da manada.","wide":True},
      {"ic":"person","t":"Ninguém Ajuda Porque Ninguém Ajuda","emph":"Ninguém Ajuda","b":"Numa emergência cheia de gente, cada um lê a calma do vizinho como “então não é grave” — e a multidão congela na ignorância pluralística. Quanto mais testemunhas, menos socorro: a responsabilidade se dilui até evaporar. <strong>A fumaça entra na sala e o sujeito sozinho corre; cercado de indiferentes fingidos, fica parado por minutos.</strong>","tip":"<strong>Como se defender:</strong> caído na rua, aponte UMA pessoa — “você, de camisa azul, chame a ambulância”."},
      {"ic":"wave","t":"O Efeito Werther","emph":"Werther","b":"A prova social no extremo trágico: depois da ampla cobertura de um suicídio, ondas de imitação sobem nos dias seguintes — a versão mais sombria de “se outros fizeram, talvez eu também”. É o mesmo mecanismo da fila, só que letal. <strong>A manada arrasta tanto para a compra quanto para o abismo</strong>, e nem sempre o número que a infla é real.","tip":"<strong>Sinal de alerta:</strong> desconfie de prova social fabricada — avaliações falsas, plateia paga, números inflados.","warn":True},
    ],
  "lessons_title":"Lições-Chave do Capítulo 4",
  "lessons":["A prova social pesa mais sob incerteza e entre semelhantes.","Multidão não é verdade — cheque os fatos.","Em emergência, individualize o pedido de ajuda."]},

 {"slug":"ch05-afeicao","sub":"CAPÍTULO 5: Afeição",
  "intro":"Preferimos dizer sim a quem gostamos — e muitos fatores fazem gostar mais rápido do que percebemos. O perigo é o vínculo afetivo, fabricado de propósito, decidir por nós.",
  "cards":[
      {"ic":"bubble","t":"Cinco Atalhos para Gostar","emph":"Gostar","b":"Dizemos sim a quem gostamos — e gostamos por gatilhos rápidos demais para notar: a atratividade (o belo parece bom, é o efeito halo), a semelhança (“também sou de Minas!”), o elogio (até a bajulação funciona), a familiaridade e a associação. <strong>O vendedor não precisa do melhor produto; precisa que você goste dele antes de decidir.</strong>","tip":"<strong>Como se defender:</strong> ao gostar rápido e demais de quem vende, pergunte “por quê?” e isole a pessoa da oferta.","wide":True},
      {"ic":"link","t":"Associação é Contágio","emph":"Contágio","b":"Transferimos sentimento por mera vizinhança: o produto colado à modelo bonita ou ao atleta vencedor herda o brilho do que está ao lado. Por isso o homem do tempo apanha pela chuva que só anunciou — ligamos o mensageiro à mensagem. <strong>O que está perto da coisa “cola” nela, e a publicidade vive de escolher essa companhia.</strong>","tip":"<strong>Modelo mental:</strong> repare no que penduraram ao lado da oferta — beleza, fama, vitória — e desconte o empréstimo de brilho."},
      {"ic":"mask","t":"O Vendedor que é seu Amigo","emph":"seu Amigo","b":"No método Tupperware quem vende é uma amiga, na sua casa, entre amigas — e a oferta vem empilhada sobre reciprocidade e compromisso público. Recusar o produto vira recusar a anfitriã. <strong>Quando o afeto e o negócio se fundem de propósito, dizer “não” ao item parece dizer “não” à pessoa</strong> — e é esse atrito que fecha a venda.","tip":"<strong>Como se defender:</strong> separe o sentimento pela pessoa da decisão sobre o negócio — “gosto dela, mas isto vale o preço?”.","warn":True},
    ],
  "lessons_title":"Lições-Chave do Capítulo 5",
  "lessons":["Atratividade, semelhança, elogio, familiaridade e associação fazem dizer sim.","Associação transfere sentimentos: cuidado com o que ligam ao produto.","Defesa: isole o negócio da pessoa que vende."]},

 {"slug":"ch06-autoridade","sub":"CAPÍTULO 6: Autoridade",
  "intro":"Somos treinados a obedecer à autoridade legítima — atalho útil, mas que dispara mesmo diante de meros símbolos dela, sem checar a substância por trás.",
  "cards":[
      {"ic":"layers","t":"Três Símbolos Bastam","emph":"Símbolos","b":"Somos treinados desde a infância a obedecer a quem sabe — mas o atalho dispara diante de três sinais do saber, não do saber em si: títulos (Dr., Professor), roupas (jaleco, uniforme) e adereços (o carro de luxo). <strong>Todos são fáceis de alegar e difíceis de checar</strong>, e por isso o impostor prefere a casca da autoridade ao seu miolo.","tip":"<strong>Como se defender:</strong> pergunte “esta autoridade é mesmo especialista NISTO?” — ela só vale dentro da área dela.","wide":True},
      {"ic":"eye","t":"O Jaleco Não é o Médico","emph":"Não é o Médico","b":"O gatilho é o símbolo, não a competência real — e o símbolo se falsifica em minutos. O ator que diz “não sou médico, mas faço um na TV” vende remédio com a credibilidade emprestada de um avental. <strong>Cedemos à aparência de saber muito antes de verificar se há saber por baixo</strong> — e quase nunca paramos para conferir.","tip":"<strong>Como se defender:</strong> some uma segunda pergunta — “quão sincera ela está sendo aqui?”, ou seja, qual é o interesse dela."},
      {"ic":"person","t":"Milgram e a Bota da Obediência","emph":"Milgram","b":"Pessoas comuns aplicaram o que criam ser choques cada vez mais fortes em outra só porque um “cientista” de jaleco mandava prosseguir — e a maioria foi até o fim, contra o próprio horror. Não eram monstros: era obediência automática ao símbolo. <strong>A autoridade não precisa forçar; basta vestir-se dela para a vontade alheia se dobrar.</strong>","tip":"<strong>Sinal de alerta:</strong> obedecer a quem só VESTE a autoridade — título alegado, uniforme, jaleco — é onde mora o risco.","warn":True},
    ],
  "lessons_title":"Lições-Chave do Capítulo 6",
  "lessons":["Reagimos a símbolos (título, roupa, adereço), não à competência real.","A autoridade só vale na sua área específica.","Defesa: 'é mesmo especialista nisto?' e 'quão sincera está sendo aqui?'."]},

 {"slug":"ch07-escassez","sub":"CAPÍTULO 7: Escassez",
  "intro":"Atribuímos mais valor ao que é raro ou está acabando. A perda potencial pesa mais que o ganho — e a sensação de oportunidade fugindo aciona o impulso de agarrar antes de pensar.",
  "cards":[
      {"ic":"clock","t":"Três Gatilhos do Raro","emph":"Raro","b":"Damos mais valor ao que escasseia — e o desejo acende por três alavancas: a quantidade limitada (“últimas unidades”), o prazo (“só hoje”, a contagem regressiva) e a censura (o proibido brilha mais). <strong>A raridade não muda o quanto a coisa serve, só o quanto a queremos</strong> — e confundir as duas é metade do trabalho de fechar.","tip":"<strong>Como se defender:</strong> separe “querer ter” de “ser útil” — raridade mexe no desejo, nunca no valor de uso.","wide":True},
      {"ic":"spiral","t":"O Proibido Seduz","emph":"Seduz","b":"Quando a liberdade de ter ou escolher é ameaçada, desejamos ainda mais aquilo que poderíamos perder — é a reatância de Brehm. Perder dói mais do que ganhar agrada, e a ameaça de ficar sem distorce o juízo. <strong>Proibir um livro é o melhor anúncio que ele pode ter</strong>; restringir uma opção é a forma mais limpa de torná-la irresistível.","tip":"<strong>Sinal de alerta:</strong> querer algo só porque foi restringido ou proibido é a reatância assumindo o comando.","warn":True},
      {"ic":"target","t":"Escassez Mais Competição","emph":"Competição","b":"Junte “só resta uma” a “outro cliente já voltou para buscá-la” e o impulso de fechar na hora dispara no pico. A raridade nova vale mais que a antiga, e a disputa vira urgência física — o coração acelera, a posse parece escapar. <strong>Essa onda de excitação é o alarme, não a evidência</strong> de que você precisa do item.","tip":"<strong>Como se defender:</strong> use a própria adrenalina como gatilho de pausa — pare e pergunte “útil, ou só raro?”."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 7",
  "lessons":["Raridade, prazo e proibição inflam o desejo, não o valor de uso.","A perda dói mais que o ganho: a ameaça de perder distorce o juízo.","Defesa: use a própria excitação como gatilho de pausa."]},

 {"slug":"ch08-defesa-e-unidade","sub":"CAPÍTULO 8: Defesa e Unidade",
  "intro":"Os atalhos são necessários — não dá para analisar tudo. A defesa não é abandoná-los, e sim reconhecer quando o gatilho foi falsificado e reagir contra o explorador, não contra o atalho.",
  "cards":[
      {"ic":"lens","t":"Vigilância Seletiva","emph":"Seletiva","b":"Na era da informação demais, decidir por gatilho único deixa de ser preguiça e vira necessidade — analisar tudo paralisaria. A defesa não é desligar os atalhos, e sim reservar o pensamento lento para o que custa caro errar. <strong>Aceite o atalho quando o gatilho é autêntico; resista só quando ele foi fabricado para iludir você.</strong>","tip":"<strong>Regra-mãe:</strong> não tente examinar tudo — mire a análise profunda no que é caro, raro ou irreversível.","wide":True},
      {"ic":"constellation","t":"Unidade: o Sétimo Princípio","emph":"Unidade","b":"Mais fundo que gostar do parecido está o “nós” compartilhado — a família, o lugar, a identidade de grupo. Quando o outro é sentido como parte do seu eu coletivo, ele convence sem argumentar: persuadir vira falar consigo mesmo. <strong>O “um de nós” baixa a guarda antes de qualquer razão entrar em cena</strong> — o gatilho mais difícil de notar.","tip":"<strong>Como se defender:</strong> confirme se o “nós” é real ou foi forjado de propósito para dissolver a sua resistência."},
      {"ic":"key","t":"A Bússola é o “Fui Usado”","emph":"Fui Usado","b":"Persuasão honesta e manipulação usam os mesmos gatilhos; o que as separa é o gatilho ser genuíno ou plantado. Por isso a defesa final não é regra, é sensação: sentir-se enganado — não apenas persuadido — autoriza recusar e contra-atacar, sem culpa. <strong>Não brigue com o atalho, que é bom; brigue com o trapaceiro que o falsificou.</strong>","tip":"<strong>Resumo 6+1:</strong> reciprocidade→não ao truque · coerência→estômago e coração · prova social→cheque os fatos · afeição→isole o negócio · autoridade→especialista e sincera? · escassez→a excitação é pausa · unidade→o “nós” é real?"},
    ],
  "lessons_title":"Lições-Chave do Capítulo 8",
  "lessons":["A defesa não é desligar os atalhos, é detectar o gatilho falsificado.","Vigilância seletiva: análise lenta onde o erro custa caro.","A Unidade ('um de nós') é o 7º princípio — confirme se é real."]},
]
