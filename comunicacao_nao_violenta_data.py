# -*- coding: utf-8 -*-
"""Conteúdo (pt-BR) das páginas da biblioteca para 'Comunicação Não-Violenta'
(Marshall B. Rosenberg — Nonviolent Communication).
Framework canônico: os 4 componentes (Observação, Sentimento, Necessidade, Pedido);
observação ≠ avaliação; sentimento ≠ pseudo-sentimento; necessidades universais;
pedido ≠ exigência; receber com empatia (os 4 modos); auto-empatia; os 4 passos da
raiva; girafa × chacal; gratidão CNV; força protetora × punitiva.
Base: síntese dos frameworks amplamente documentados — não reproduz o texto."""

BOOK = {
 "title": "Comunicação Não-Violenta",
 "author": "Marshall B. Rosenberg",
 "header_light": "COMUNICAÇÃO",
 "header_bold": "NÃO-VIOLENTA",
 "subtitle": "VISÃO GERAL · A LINGUAGEM DA EMPATIA",
 "intro": "Um método para falar e ouvir de um jeito que reconecta as pessoas à compaixão — mesmo no conflito. Tudo cabe em quatro passos: observar sem julgar, nomear o sentimento, encontrar a necessidade por trás dele e fazer um pedido claro. Rosenberg chama de 'girafa' (o animal terrestre de maior coração) a linguagem que conecta, e de 'chacal' a que julga, exige e pune.",
 "description": "O clássico de Marshall Rosenberg que ensina a transformar conflito em conexão. Pela estrutura dos quatro componentes — observação, sentimento, necessidade e pedido — mostra como sair da linguagem que julga e exige (o 'chacal') para a que escuta e enriquece a vida (a 'girafa'): distinguir observação de avaliação, sentimento de interpretação, pedido de exigência, receber com empatia e traduzir a própria raiva.",
 "tags": ["Comunicação", "Empatia", "Relacionamentos"],
 "progress": "11 Capítulos",
 "cover": "assets/comunicacao-nao-violenta-cover.png",
 "overview_cards": [
   {"ic":"steps","t":"Os 4 Componentes (OSNP)","b":"O coração do método — a mesma estrutura para <strong>se expressar</strong> e para <strong>ouvir</strong>:","list":[
     "<strong>1. Observação</strong> — o fato, sem avaliação (como uma câmera veria).",
     "<strong>2. Sentimento</strong> — a emoção real que o fato desperta.",
     "<strong>3. Necessidade</strong> — a necessidade universal por trás do sentimento.",
     "<strong>4. Pedido</strong> — uma ação concreta, positiva e que aceita o 'não'.",
   ],"tip":"<strong>Como aplicar:</strong> 'Quando ___ (fato), sinto ___, porque preciso de ___. Você toparia ___?'","wide":True},
   {"ic":"mask","t":"Girafa × Chacal","b":"Duas linguagens. O <strong>chacal</strong> julga, rotula, exige e pune; a <strong>girafa</strong> observa, sente, identifica a necessidade e pede. Toda crítica ou ataque é a <strong>expressão trágica de uma necessidade não atendida</strong> — o tradutor universal da CNV.","tip":"<strong>Modelo mental:</strong> pergunte sempre 'que necessidade está gritando por baixo destas palavras?'","wide":True},
   {"ic":"scale","t":"Pedido × Exigência","b":"A diferença não está nas palavras, e sim no que acontece com o <strong>'não'</strong>. Se a recusa gera culpa, punição ou retirada de afeto, virou <strong>exigência</strong>. Pedido de verdade deixa o 'não' em aberto.","tip":"<strong>Teste do não:</strong> se você pune a recusa, não era pedido."},
 ],
}

CHAPTERS = [
 {"slug":"ch01-coracao-da-cnv","sub":"CAPÍTULO 1: O Coração da CNV",
  "intro":"A CNV reconecta as pessoas à compaixão natural organizando a conversa em torno de quatro componentes — observação, sentimento, necessidade e pedido — usados tanto para falar quanto para escutar.",
  "cards":[
      {"ic":"steps","t":"Toda a CNV Cabe em Quatro Passos","emph":"Quatro Passos","b":"Rosenberg não pede que você fique gentil — pede que organize a fala numa ordem fixa: observar o fato sem julgar, nomear o que isso desperta em você, achar a necessidade por baixo e fazer um pedido concreto. <strong>Quando a conversa descarrila, é a esse trilho que se volta</strong>: o que observo, o que sinto, do que preciso, o que peço.","tip":"<strong>Como aplicar:</strong> “Quando ___ (fato), sinto ___, porque preciso de ___. Você toparia ___?”"},
      {"ic":"link","t":"A Mesma Gramática nas Duas Direções","emph":"Duas Direções","b":"Os quatro passos não servem só para você se expor — servem para ler o outro por dentro. Numa direção você diz o que vive em si com honestidade; na outra, escuta o que vive no outro com empatia. <strong>É uma língua de mão dupla: fala-se e ouve-se com a mesma estrutura</strong> — e a escuta costuma ser a metade mais esquecida.","tip":"<strong>Modelo mental:</strong> antes de responder, pergunte qual dos dois lados a conversa pede agora — expressar ou receber."},
      {"ic":"mask","t":"A Linguagem da Girafa e a do Chacal","emph":"Girafa","b":"Rosenberg batiza duas falas. O chacal julga, rotula, exige e pune; a girafa — o animal terrestre de maior coração — observa, sente, nomeia a necessidade e pede. São hábitos, aprendíveis e desaprendíveis. <strong>Mas recitar as quatro frases sem presença soa falso</strong> — o que faz funcionar é a intenção de conectar, não o roteiro.","tip":"<strong>Cuidado:</strong> CNV usada para conseguir o que se quer vira chacal de fantasia — a meta é conexão, não vitória.","warn":True},
    ],
  "lessons_title":"Lições-Chave do Capítulo 1",
  "lessons":["Toda a CNV cabe em 4 passos: observação, sentimento, necessidade, pedido.","Os mesmos passos servem para falar e para ouvir.","A meta é conexão e compaixão — não vencer nem manipular."]},

 {"slug":"ch02-comunicacao-que-bloqueia","sub":"CAPÍTULO 2: A Comunicação que Bloqueia a Compaixão",
  "intro":"Antes de aprender a CNV é preciso reconhecer a 'comunicação alienante da vida' — hábitos de linguagem que desconectam, transferem culpa e disparam a defensiva.",
  "cards":[
      {"ic":"fork","t":"Os Quatro Bloqueadores da Compaixão","emph":"Bloqueadores","b":"Antes de aprender a girafa, é preciso flagrar a fala que desconecta. São quatro hábitos: o julgamento moralizador que rotula quem discorda; a comparação que mede gente contra um ideal; a negação da escolha (“tive de”); e a exigência que ameaça com culpa. <strong>Todos desviam a atenção do que cada um precisa para quem está “certo”.</strong>","tip":"<strong>Como aplicar:</strong> pegue-se usando qualquer um dos quatro e reescreva a frase em observação, sentimento, necessidade e pedido."},
      {"ic":"key","t":"De “Tenho de” para “Escolho”","emph":"“Escolho”","b":"A linguagem que nega a escolha apaga você da própria vida: “tenho de”, “devo”, “sou obrigado” entregam o comando a uma força lá fora. Quase tudo o que dizemos ser obrigação é, no fundo, uma escolha com um motivo. <strong>Troque “tenho de” por “escolho ___ porque quero ___” e a responsabilidade volta para as suas mãos.</strong>","tip":"<strong>Modelo mental:</strong> ninguém te obriga a quase nada — você escolhe, a partir de uma necessidade que vale a pena nomear."},
      {"ic":"sword","t":"A Semente da Violência é o “Merecer”","emph":"“Merecer”","b":"Pensar que alguém “merece” sofrer é, para Rosenberg, a raiz psicológica de toda violência — da bronca em casa à guerra. O julgamento de caráter (“ele é egoísta”) é sempre uma necessidade sua que não foi dita em voz alta, embrulhada em veredito. <strong>Por baixo de “ele é um grosso” mora um “eu precisava de respeito”.</strong>","tip":"<strong>Cuidado:</strong> “sinto que você é injusto” não é sentimento — é julgamento fantasiado de emoção.","warn":True},
    ],
  "lessons_title":"Lições-Chave do Capítulo 2",
  "lessons":["A linguagem que julga e exige é aprendida — e desaprendível.","'Tenho de' mascara escolhas; recupere a responsabilidade dizendo 'escolho porque'.","Pensar em quem 'merece' punição é a semente da violência."]},

 {"slug":"ch03-observar-sem-avaliar","sub":"CAPÍTULO 3: Observar sem Avaliar",
  "intro":"O primeiro componente é observar sem misturar avaliação: descrever o que aconteceu de forma específica e factual, sem rótulos de certo/errado ou sempre/nunca.",
  "cards":[
      {"ic":"eye","t":"O Que a Câmera Teria Gravado","emph":"Câmera","b":"O primeiro passo parece simples e é o mais traído: descrever só o fato, sem o veredito grudado nele. Observação é o que uma câmera registraria, ancorado em tempo e lugar — “ontem você chegou vinte minutos depois”. <strong>Misture fato e juízo na mesma frase e o fato some atrás da crítica</strong> — e o outro só ouve o ataque.","tip":"<strong>Como aplicar:</strong> antes de falar, pergunte “o que uma câmera teria gravado aqui?” — e diga só isso primeiro."},
      {"ic":"gap","t":"Troque o Rótulo Fixo pelo Fato Datado","emph":"Datado","b":"“Ele é preguiçoso” é uma sentença de prisão perpétua: trava a pessoa num traço que não muda. “Esta semana ele não entregou o relatório” é um fato com data, que abre porta para conversa. A linguagem estática condena; a de processo descreve. <strong>“Sempre” e “nunca” soam como acusação e convidam o outro direto para a defensiva.</strong>","tip":"<strong>Sinal de alerta:</strong> ao ouvir (ou dizer) “sempre” e “nunca”, suspeite — quase certamente é avaliação disfarçada de fato.","warn":True},
      {"ic":"lens","t":"A Forma Mais Alta de Inteligência","emph":"Inteligência","b":"Rosenberg recorre a Krishnamurti: observar sem avaliar é a forma mais elevada de inteligência humana — e é raríssima, porque o cérebro classifica antes de perceber. Separar o que aconteceu do que aquilo significa é disciplina, não frieza. <strong>Só o fato limpo abre o diálogo; o veredito o fecha antes de começar.</strong>","tip":"<strong>Modelo mental:</strong> “gasta demais” é juízo; “este mês gastou R$ 600 acima do orçado” é o fato que dá para conversar."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 3",
  "lessons":["Comece pelo fato observável; o juízo afasta o ouvinte.","Ancore observações em tempo e contexto — fuja de 'sempre/nunca'.","Rótulo de caráter é avaliação; ação datada é observação."]},

 {"slug":"ch04-identificar-sentimentos","sub":"CAPÍTULO 4: Identificar e Expressar Sentimentos",
  "intro":"O segundo componente é nomear o sentimento real — distinguindo emoções genuínas dos 'pseudo-sentimentos', que são interpretações sobre o que o outro fez, disfarçadas de emoção.",
  "cards":[
      {"ic":"mask","t":"O Pseudo-Sentimento é Acusação Disfarçada","emph":"Pseudo-Sentimento","b":"“Sinto-me ignorado, manipulado, rejeitado” parecem emoções, mas descrevem o que você acha que o outro fez — são julgamentos vestidos de sentimento. O teste é cru: se “sinto-me X” vira “acho que você me ___”, não era emoção. <strong>Sob cada pseudo-sentimento mora uma emoção real — mágoa, medo, solidão — e uma necessidade.</strong>","tip":"<strong>Como aplicar:</strong> ache a emoção verdadeira sob a acusação; “ignorado” costuma ser “sozinho e triste” pedindo conexão."},
      {"ic":"bubble","t":"Cuidado com o “Sinto Que…”","emph":"“Sinto Que…”","b":"Quase toda vez que “sinto” vem seguido de “que”, “como se” ou um pronome, o que vem depois é pensamento, não emoção: “sinto que isso é errado”, “sinto como se você não ligasse”. A palavrinha entrega o disfarce. <strong>Emoção é medo, alegria, tristeza, alívio — interpretação é “usado”, “desrespeitado”, “traído”.</strong>","tip":"<strong>Sinal de alerta:</strong> “me sinto pressionado” é veredito sobre o outro; “me sinto ansioso” é o que de fato se passa em você.","warn":True},
      {"ic":"book","t":"Sem Vocabulário, Ninguém te Entende","emph":"Vocabulário","b":"Viver entre “tô bem” e “tô mal” é falar do mundo interior em duas cores só. Nomear com precisão — frustrado, apreensivo, aliviado, grato — é pré-requisito da CNV, não enfeite. Expor o sentimento real deixa você vulnerável e, por isso, costuma desarmar o conflito. <strong>Quem não nomeia o que sente não tem como ser compreendido.</strong>","tip":"<strong>Modelo mental:</strong> a emoção é uma placa que aponta a necessidade; quanto mais exata a palavra, mais clara a direção."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 4",
  "lessons":["Nem toda frase com 'eu me sinto' expressa um sentimento — muitas escondem julgamento.","Atrás de todo pseudo-sentimento há uma emoção real e uma necessidade.","Ampliar o vocabulário de sentimentos é pré-requisito da CNV."]},

 {"slug":"ch05-necessidades","sub":"CAPÍTULO 5: Assumir a Responsabilidade pelos Sentimentos",
  "intro":"O terceiro componente liga cada sentimento a uma necessidade universal. A causa do que sentimos é a necessidade — não o ato do outro; reconhecer isso é assumir a responsabilidade pela própria vida emocional.",
  "cards":[
      {"ic":"target","t":"A Necessidade é a Causa, o Outro é o Estímulo","emph":"Causa","b":"“Você me faz sentir isso” é a frase que entrega o seu poder de bandeja. O ato do outro é só o estímulo; a causa do que você sente é uma necessidade sua — atendida, vem o agradável; frustrada, vem a dor. <strong>Diga “sinto X porque preciso de Z”, nunca “porque você fez Y”</strong>: a primeira versão devolve sua vida emocional às suas mãos.","tip":"<strong>Como aplicar:</strong> depois de nomear o sentimento, pergunte “que necessidade minha está por trás disto?” antes de qualquer acusação."},
      {"ic":"layers","t":"Os Quatro Modos de Receber uma Farpa","emph":"Quatro Modos","b":"Diante de uma mensagem dura, há quatro lugares para levar a atenção: culpar a si (engolir o chacal, vem a culpa), culpar o outro (revidar, vem a briga), sentir as próprias necessidades (auto-empatia) ou sentir as do outro (empatia). <strong>A CNV vive nos dois últimos — e qual você escolhe é o ponto de virada da conversa.</strong>","tip":"<strong>Regra:</strong> a escolha não é automática; respire e decida conscientemente para onde a atenção vai antes de reagir."},
      {"ic":"fork","t":"Não Confunda Necessidade com Estratégia","emph":"Estratégia","b":"A necessidade é abstrata e universal — conexão, segurança, respeito — e não exige pessoa ou ato específico. A estratégia é só um dos meios de atendê-la. A briga nasce de confundir as duas: discute-se “me ligue todo dia” em vez de “preciso de conexão”. <strong>Cravar uma única solução fecha portas que a necessidade deixaria abertas.</strong>","tip":"<strong>Modelo mental:</strong> ache a necessidade primeiro; muitas estratégias diferentes podem servir à mesma, e isso destrava o acordo."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 5",
  "lessons":["A necessidade — não o outro — é a causa real do sentimento.","Diante de uma mensagem dura, escolha onde colocar a atenção (os 4 modos).","Necessidade não é estratégia: ache a necessidade antes de defender uma solução."]},

 {"slug":"ch06-pedidos","sub":"CAPÍTULO 6: Pedir o que Enriquece a Vida",
  "intro":"O quarto componente é o pedido: uma ação concreta, positiva e acionável que atenda à necessidade — e que aceita o 'não' sem punição. Pedido difere de exigência pela liberdade de recusa.",
  "cards":[
      {"ic":"scale","t":"O Pedido se Revela no “Não”","emph":"“Não”","b":"A diferença entre pedido e exigência não está nas palavras nem no tom doce — está no que você faz quando ouve “não”. Se a recusa gera culpa, castigo, silêncio ou só uma cara feia, aquilo nunca foi pedido: era exigência embrulhada em gentileza. <strong>Pedido de verdade deixa o “não” em aberto, sem cobrar pedágio pela recusa.</strong>","tip":"<strong>Como aplicar:</strong> peça com leveza, mas observe sua própria reação ao “não” — é ela que denuncia o que você fez de fato.","warn":True},
      {"ic":"target","t":"Positivo, Concreto e no Presente","emph":"Concreto","b":"“Pare de me ignorar” diz o que evitar e deixa o outro sem saber o que fazer; “quero trinta minutos de conversa sem celular hoje” entrega uma ação possível agora. Bom pedido diz o que fazer, não o que parar, e descreve algo observável. <strong>“Seja mais carinhoso” é vago demais para virar ação — ninguém sabe por onde começar.</strong>","tip":"<strong>Regra:</strong> se o pedido não cabe num gesto que dá para filmar hoje, ele ainda é vago demais para ser atendido."},
      {"ic":"link","t":"Peça o Reflexo de Volta","emph":"Reflexo","b":"Em mensagens que importam, peça que o outro repita o que entendeu — e como se sente com aquilo. Não para testá-lo, mas para flagrar o ruído antes que vire conflito. Enquadre como cuidado seu: “pra eu ter certeza de que me expressei bem”. <strong>Confirmar o que chegou previne metade das brigas, que nascem de mensagens pela metade.</strong>","tip":"<strong>Como aplicar:</strong> peça o reflexo (“o que você ouviu?”) e a honestidade (“como você se sente com isto?”) lado a lado."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 6",
  "lessons":["Pedido é positivo, concreto, no presente — e aceita o 'não'.","No instante em que o 'não' é punido, o pedido virou exigência.","Peça o reflexo: confirmar o entendimento previne metade dos conflitos."]},

 {"slug":"ch07-receber-com-empatia","sub":"CAPÍTULO 7: Receber com Empatia",
  "intro":"A CNV não é só falar: é ouvir. Receber com empatia é oferecer presença plena ao que o outro observa, sente, precisa e pede — sem aconselhar, consertar ou contar a própria história.",
  "cards":[
      {"ic":"wave","t":"Empatia é Presença, não Conserto","emph":"Presença","b":"Diante da dor do outro, o impulso é resolver — e é justo aí que se perde a conexão. Empatia é esvaziar a mente dos pré-julgamentos e ficar inteiro com quem está na sua frente, sem agenda de consertar. <strong>Antes de qualquer solução, a presença cura mais que o conselho</strong> — escute, e só se ajudar devolva sentimento e necessidade.","tip":"<strong>Modelo mental:</strong> “não faça algo, fique aí” — pergunte-se se a pessoa quer solução ou só quer ser ouvida."},
      {"ic":"gap","t":"Os Bloqueadores que Parecem Ajuda","emph":"Parecem Ajuda","b":"Há frases bem-intencionadas que cortam a conexão pela raiz: aconselhar (“o que você devia fazer…”), consolar (“vai passar”), competir (“comigo foi pior”), educar, corrigir, interrogar. Todas tiram o foco da pessoa e o jogam de volta em você. <strong>Mesmo cheias de boa intenção, elas invalidam o que o outro sente.</strong>","tip":"<strong>Cuidado:</strong> “relaxa, semana que vem melhora” não acolhe — apaga o que a pessoa está sentindo agora.","warn":True},
      {"ic":"bubble","t":"Reflita em Pergunta, não em Rótulo","emph":"Pergunta","b":"Devolver o que você ouviu como afirmação fecha (“você está com medo.”); devolver como pergunta abre (“você está com medo de…?”). A pergunta convida o outro a corrigir ou confirmar, em vez de receber um diagnóstico pronto. <strong>Sinal de empatia suficiente: a tensão no corpo do outro afrouxa, ou ele para de falar.</strong>","tip":"<strong>Como aplicar:</strong> reflita sentimento mais necessidade — “você está frustrado porque queria ter sido consultado?”."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 7",
  "lessons":["Empatia é presença, não conserto — não faça algo, fique aí.","Reflita sentimento + necessidade em forma de pergunta.","Conselho, consolo e 'comigo foi pior' bloqueiam a empatia, mesmo bem-intencionados."]},

 {"slug":"ch08-poder-da-empatia","sub":"CAPÍTULO 8: O Poder da Empatia",
  "intro":"A empatia tem poder de cura, desarma a hostilidade e permite até dizer 'não' sem romper a conexão. Ouvir a necessidade por trás de qualquer mensagem — inclusive um ataque — muda a dinâmica do conflito.",
  "cards":[
      {"ic":"shield","t":"Empatia Primeiro, Defesa Depois","emph":"Primeiro","b":"Quando a crítica aterrissa em você, o corpo já prepara a defesa — e contra-argumentar antes do outro se sentir ouvido só escala a briga. A ordem é o segredo: escute até a pessoa sentir que foi compreendida e só então apresente o seu lado. <strong>Quem se sente ouvido finalmente consegue ouvir; a sequência invertida acende o pavio.</strong>","tip":"<strong>Como aplicar:</strong> em conflito, segure o impulso de explicar; a sua vez chega — e chega melhor — depois da empatia."},
      {"ic":"key","t":"O Ataque é um “Obrigado” Mal-Embrulhado","emph":"Mal-Embrulhado","b":"Por trás de toda agressão grita uma necessidade não atendida. O cliente que xinga, o parceiro que acusa — ambos pedem algo, da pior forma. Quem revida responde à embalagem; quem escuta a necessidade muda o jogo. <strong>Ao se sentir reconhecida, a raiva do outro costuma baixar sozinha — e só então a solução cabe na conversa.</strong>","tip":"<strong>Modelo mental:</strong> traduza o chacal do outro em sentimento mais necessidade — “você esperava que já estivesse resolvido?”."},
      {"ic":"scale","t":"Dizer “Não” é Dizer “Sim” a uma Necessidade","emph":"“Não”","b":"O “não” seco fere e o “não” afogado em desculpas alimenta a sensação de rejeição. O “não” empático faz outra coisa: nomeia a necessidade que ele protege. “Vou dizer não a isto porque preciso de descanso” recusa sem romper o vínculo. <strong>Todo “não” honesto é, no fundo, um “sim” a algo que importa para você.</strong>","tip":"<strong>Cuidado:</strong> recusar sem dizer o que você protege deixa o outro só com a rejeição, sem a razão por trás dela.","warn":True},
    ],
  "lessons_title":"Lições-Chave do Capítulo 8",
  "lessons":["Atrás de todo ataque há uma necessidade — escute-a antes de revidar.","Empatia antes da autodefesa: quem se sente ouvido passa a ouvir.","Um 'não' pode ser empático quando nomeia o 'sim' (a necessidade) que protege."]},

 {"slug":"ch09-auto-empatia","sub":"CAPÍTULO 9: Conexão Compassiva Consigo Mesmo",
  "intro":"A CNV mais importante é a interior. Antes de dar empatia, é preciso dar a si mesmo: observar, sentir, identificar a necessidade e fazer um pedido a si — em vez de se afogar em autorrecriminação (o 'chacal interno').",
  "cards":[
      {"ic":"spiral","t":"Não se Dá Empatia de Tanque Vazio","emph":"Tanque Vazio","b":"A CNV mais importante é a que você dirige a si mesmo. Antes de acolher alguém, aplique os quatro passos por dentro: o que observo em mim, o que sinto, de que preciso, o que peço a mim. <strong>Quem chega esgotado a uma conversa difícil derrama a própria reatividade no outro</strong> — uma auto-empatia relâmpago evita o transbordo.","tip":"<strong>Como aplicar:</strong> antes de ajudar alguém em crise, faça os quatro passos consigo — só assim a presença que você oferece é limpa."},
      {"ic":"pivot","t":"Traduza Cada “Deveria”","emph":"“Deveria”","b":"A tirania do “eu deveria ter…” é só o chacal voltado para dentro: pune sem atender necessidade nenhuma e gera culpa, não mudança. Cada “deveria” esconde algo de que você precisava. Troque “deveria ter feito X” por “queria ter feito X porque preciso de ___”. <strong>“Como pude ser tão burro” paralisa; a necessidade nomeada liberta.</strong>","tip":"<strong>Sinal de alerta:</strong> autocrítica em forma de xingamento é chacal mal traduzido — por baixo dela há uma necessidade pedindo atenção.","warn":True},
      {"ic":"leaf","t":"Luto e Autoperdão no Lugar da Culpa","emph":"Autoperdão","b":"Errar pede duas coisas, e nenhuma é culpa. O luto CNV é sentir a dor ligada à necessidade que seu erro não atendeu; o autoperdão é acolher a necessidade que você buscava atender ao agir como agiu. <strong>Energia limpa nasce da necessidade que a ação serve, não da vergonha</strong> — quem age por culpa ou medo carrega resistência junto.","tip":"<strong>Modelo mental:</strong> a necessidade (“valorizo cuidado nas relações”) substitui o veredito (“sou uma pessoa horrível”)."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 9",
  "lessons":["Auto-empatia primeiro: não se dá empatia de um tanque vazio.","Todo 'deveria' esconde uma necessidade — traduza em vez de se punir.","Luto e autoperdão CNV substituem a culpa pela conexão com a necessidade."]},

 {"slug":"ch10-raiva","sub":"CAPÍTULO 10: Expressar Plenamente a Raiva",
  "intro":"A raiva não é causada pelo outro, mas pelos julgamentos que fazemos ('ele não deveria…'). Ela é um alarme valioso: aponta uma necessidade não atendida. Expressá-la plenamente é traduzi-la, não despejá-la nem engoli-la.",
  "cards":[
      {"ic":"steps","t":"Os Quatro Passos da Raiva","emph":"Quatro Passos","b":"A raiva é uma luz piscando no painel: informação valiosa, péssima como volante. Quando ela sobe: pare e respire; veja o julgamento que a alimenta (“ele não deveria…”); conecte-se à necessidade por trás dele; e só então expresse sentimento e necessidade. <strong>Os quatro passos convertem a explosão em informação que dá para usar.</strong>","tip":"<strong>Como aplicar:</strong> o passo 1 é não fazer nada e não falar — é o respiro que separa a reação da resposta."},
      {"ic":"target","t":"O Outro Acende, o Julgamento Causa","emph":"Julgamento","b":"“Você me deixa com raiva” é mentira conveniente: o ato do outro só acende o pavio. A causa é o pensamento que você cola em cima — “ele é um aproveitador” — somado à necessidade que ficou de fora. <strong>Diga “estou com raiva porque preciso de ___”, nunca “porque você fez ___”</strong> — e o controle volta para você.","tip":"<strong>Modelo mental:</strong> a raiva é um presente embrulhado — por dentro está a necessidade que mais importa agora."},
      {"ic":"fork","t":"Nem Despejar, nem Reprimir: Traduzir","emph":"Traduzir","b":"Há dois becos sem saída. Despejar (“a culpa é toda sua!”) alivia por três segundos e arrasa a conexão; reprimir engole tudo e fermenta em ressentimento e chacal interno. A CNV abre um terceiro caminho — traduzir a raiva em sentimento e necessidade. <strong>E quase sempre, sob a raiva, mora algo mais frágil: medo, mágoa ou solidão.</strong>","tip":"<strong>Cuidado:</strong> a raiva despejada parece força, mas é a saída que mais custa caro à relação depois.","warn":True},
    ],
  "lessons_title":"Lições-Chave do Capítulo 10",
  "lessons":["O outro é o estímulo; o julgamento é a causa da raiva.","Os 4 passos: parar, ver o julgamento, achar a necessidade, expressá-la.","Há um terceiro caminho entre despejar e reprimir: traduzir a raiva em necessidade."]},

 {"slug":"ch11-gratidao-e-poder-protetor","sub":"CAPÍTULO 11: Gratidão e o Uso Protetor da Força",
  "intro":"A CNV também muda como elogiamos e como agimos quando o diálogo não é possível. A gratidão celebra sem julgar; e quando não dá tempo de dialogar, usa-se a força protetora — nunca a punitiva.",
  "cards":[
      {"ic":"spark","t":"Até o Elogio Pode Ser Julgamento","emph":"Julgamento","b":"“Você é incrível” soa generoso, mas coloca você no banco do juiz, emitindo um veredito de cima. A gratidão CNV troca o rótulo por três partes: o que a pessoa fez (observação), como você se sentiu (sentimento) e que necessidade sua aquilo atendeu. <strong>Assim você celebra a conexão, em vez de avaliar quem está na sua frente.</strong>","tip":"<strong>Como aplicar:</strong> receba gratidão sem falsa modéstia nem ego inflado — é só uma necessidade que foi atendida."},
      {"ic":"shield","t":"Força Protetora ou Força Punitiva","emph":"Protetora","b":"Quando não há tempo de dialogar e há risco real, usa-se a força — mas a fronteira é a intenção. A protetora segura a criança que corre para a rua sem julgá-la, supondo que o dano vem de ignorância. A punitiva quer fazer o outro sofrer, apostando no “merecimento”. <strong>Antes de agir, pergunte: estou protegendo ou punindo?</strong>","tip":"<strong>Regra:</strong> a mesma mão que protege pode punir — só a intenção por trás do gesto decide qual das duas é."},
      {"ic":"sword","t":"O Custo Oculto da Punição","emph":"Custo Oculto","b":"Castigar “para o outro aprender” entrega obediência por medo, nunca cooperação — e vai corroendo a boa vontade que sustentava a relação. A força punitiva nasce das perguntas fatais: o que quero que ele faça, e por que motivo quero que faça. <strong>Veja o ato prejudicial como ignorância da CNV, não como maldade que merece troco.</strong>","tip":"<strong>Cuidado:</strong> a punição produz ressentimento e resistência, não a mudança que você imaginava estar ensinando.","warn":True},
    ],
  "lessons_title":"Lições-Chave do Capítulo 11",
  "lessons":["Gratidão CNV celebra com observação + sentimento + necessidade — não com rótulos.","Receba gratidão sem falsa modéstia nem ego: é só uma necessidade atendida.","Use a força para proteger, nunca para punir — a punição custa a boa vontade."]},
]
