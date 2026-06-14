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
   {"ic":"steps","t":"O Processo em 4 Passos","b":"Toda a CNV cabe em quatro componentes, sempre na mesma ordem: <strong>observar</strong> sem avaliar, nomear o <strong>sentimento</strong>, ligar à <strong>necessidade</strong> e fazer um <strong>pedido</strong> concreto e acionável.","tip":"<strong>Como aplicar:</strong> quando a conversa descarrila, volte ao trilho 'o que observo / sinto / preciso / peço'."},
   {"ic":"link","t":"Ida e Volta: Expressar e Receber","b":"Os mesmos quatro passos servem em <strong>dois sentidos</strong>: expressar com honestidade (o que vive em mim) e <strong>receber com empatia</strong> (o que vive no outro).","tip":"<strong>Modelo mental:</strong> a CNV é uma língua de mão dupla — fala-se e escuta-se com a mesma gramática."},
   {"ic":"mask","t":"Girafa × Chacal","b":"<strong>Girafa</strong> (maior coração entre os animais terrestres) é a linguagem que conecta; <strong>chacal</strong> é a que julga, exige e pune. São hábitos de fala — aprendíveis e desaprendíveis.","tip":"<strong>Cuidado:</strong> recitar as quatro frases sem presença soa falso — a intenção de conexão é o que faz funcionar.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 1",
  "lessons":["Toda a CNV cabe em 4 passos: observação, sentimento, necessidade, pedido.","Os mesmos passos servem para falar e para ouvir.","A meta é conexão e compaixão — não vencer nem manipular."]},

 {"slug":"ch02-comunicacao-que-bloqueia","sub":"CAPÍTULO 2: A Comunicação que Bloqueia a Compaixão",
  "intro":"Antes de aprender a CNV é preciso reconhecer a 'comunicação alienante da vida' — hábitos de linguagem que desconectam, transferem culpa e disparam a defensiva.",
  "cards":[
   {"ic":"fork","t":"Os 4 Bloqueadores da Compaixão","b":"Linguagem que nos afasta da empatia — use como <strong>checklist de diagnóstico</strong>:","list":[
     "<strong>Julgamentos moralizadores</strong> — rotular quem discorda como errado ('ele é egoísta').",
     "<strong>Comparações</strong> — medir a si e ao outro contra um ideal.",
     "<strong>Negar a responsabilidade</strong> — 'tive de', 'a regra manda', 'você me obrigou'.",
     "<strong>Exigências</strong> — pedidos que ameaçam com culpa ou punição.",
   ],"tip":"<strong>Como aplicar:</strong> pegue-se usando qualquer um deles e reformule em OSNP.","wide":True},
   {"ic":"key","t":"De 'Tenho de' para 'Escolho'","b":"A linguagem que <strong>nega a escolha</strong> ('tenho de', 'devo') apaga a responsabilidade pessoal. Troque por '<strong>escolho ___ porque quero ___</strong>' e recupere a agência.","tip":"<strong>Modelo mental:</strong> quase tudo o que 'temos de' fazer é, na verdade, uma escolha com um motivo."},
   {"ic":"sword","t":"A Raiz da Violência: 'Merecer'","b":"Pensar que certas pessoas <strong>'merecem'</strong> punição é a semente psicológica da violência. O julgamento de caráter sempre esconde uma <strong>necessidade não dita</strong>.","tip":"<strong>Cuidado:</strong> 'sinto que você é injusto' é julgamento fantasiado de sentimento.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 2",
  "lessons":["A linguagem que julga e exige é aprendida — e desaprendível.","'Tenho de' mascara escolhas; recupere a responsabilidade dizendo 'escolho porque'.","Pensar em quem 'merece' punição é a semente da violência."]},

 {"slug":"ch03-observar-sem-avaliar","sub":"CAPÍTULO 3: Observar sem Avaliar",
  "intro":"O primeiro componente é observar sem misturar avaliação: descrever o que aconteceu de forma específica e factual, sem rótulos de certo/errado ou sempre/nunca.",
  "cards":[
   {"ic":"eye","t":"O Teste da Câmera","b":"Observação é o que uma <strong>câmera registraria</strong>, ancorado em tempo e contexto ('ontem você chegou 20 min depois'). Tudo além disso — rótulo, interpretação, juízo — é <strong>avaliação</strong>.","tip":"<strong>Como aplicar:</strong> antes de falar, pergunte: o que uma câmera teria gravado aqui?"},
   {"ic":"gap","t":"Estático × Processo","b":"Troque o rótulo fixo ('ele é preguiçoso') pela observação <strong>datada</strong> ('esta semana ele não entregou o relatório'). 'Sempre' e 'nunca' soam como crítica e convidam à defesa.","tip":"<strong>Sinal de alerta:</strong> ao ouvir 'sempre/nunca', suspeite de avaliação disfarçada.","warn":True},
   {"ic":"lens","t":"A Forma Suprema de Inteligência","b":"Rosenberg cita Krishnamurti: <strong>observar sem avaliar é a forma mais elevada de inteligência humana</strong>. Misturar fato e juízo na mesma frase faz o fato sumir atrás da crítica.","tip":"<strong>Modelo mental:</strong> separe o fato do veredito — só o fato abre o diálogo."},
  ],
  "lessons_title":"Lições-Chave do Capítulo 3",
  "lessons":["Comece pelo fato observável; o juízo afasta o ouvinte.","Ancore observações em tempo e contexto — fuja de 'sempre/nunca'.","Rótulo de caráter é avaliação; ação datada é observação."]},

 {"slug":"ch04-identificar-sentimentos","sub":"CAPÍTULO 4: Identificar e Expressar Sentimentos",
  "intro":"O segundo componente é nomear o sentimento real — distinguindo emoções genuínas dos 'pseudo-sentimentos', que são interpretações sobre o que o outro fez, disfarçadas de emoção.",
  "cards":[
   {"ic":"mask","t":"Sentimento × Pseudo-sentimento","b":"<strong>Pseudo-sentimento</strong> parece emoção mas descreve a ação atribuída ao outro: 'ignorado', 'manipulado', 'rejeitado', 'pressionado', 'traído'. <strong>Teste:</strong> se 'me sinto X' vira 'acho que <strong>você me</strong> ___', é pseudo-sentimento.","tip":"<strong>Como aplicar:</strong> embaixo de todo pseudo-sentimento há uma emoção real (mágoa, medo, solidão) e uma necessidade.","wide":True},
   {"ic":"bubble","t":"Cuidado com o 'Sinto que…'","b":"'Sinto <strong>que</strong> isso é errado', 'sinto <strong>como se</strong> você não ligasse' — quase sempre introduzem um <strong>pensamento</strong>, não um sentimento. Se vier 'que', 'como se' ou um pronome, desconfie.","tip":"<strong>Sinal de alerta:</strong> 'me sinto pressionado/desrespeitado' são julgamentos sobre o outro, não emoções.","warn":True},
   {"ic":"book","t":"Ampliar o Vocabulário","b":"Sair de 'tô bem / tô mal' para nomear com precisão (frustrado, apreensivo, aliviado, grato, desanimado) é <strong>pré-requisito</strong> para a CNV. Expressar o sentimento real expõe — e, paradoxalmente, resolve.","tip":"<strong>Modelo mental:</strong> quem não nomeia o que sente, não consegue ser entendido."},
  ],
  "lessons_title":"Lições-Chave do Capítulo 4",
  "lessons":["Nem toda frase com 'eu me sinto' expressa um sentimento — muitas escondem julgamento.","Atrás de todo pseudo-sentimento há uma emoção real e uma necessidade.","Ampliar o vocabulário de sentimentos é pré-requisito da CNV."]},

 {"slug":"ch05-necessidades","sub":"CAPÍTULO 5: Assumir a Responsabilidade pelos Sentimentos",
  "intro":"O terceiro componente liga cada sentimento a uma necessidade universal. A causa do que sentimos é a necessidade — não o ato do outro; reconhecer isso é assumir a responsabilidade pela própria vida emocional.",
  "cards":[
   {"ic":"target","t":"A Necessidade é a Causa","b":"Todo sentimento sinaliza uma <strong>necessidade</strong> — agradável quando atendida, desagradável quando não. Diga 'sinto X <strong>porque preciso de Z</strong>', nunca 'sinto X <strong>porque você</strong> fez Y'.","tip":"<strong>Como aplicar:</strong> 'você me faz sentir…' terceiriza a causa e remove a sua agência."},
   {"ic":"layers","t":"Os 4 Modos de Receber","b":"Diante de uma mensagem dura, há quatro escolhas de atenção:","list":[
     "<strong>1. Culpar a si mesmo</strong> — engolir o chacal (culpa, depressão).",
     "<strong>2. Culpar o outro</strong> — atacar, contra-atacar.",
     "<strong>3. Auto-empatia</strong> — sentir os próprios sentimentos/necessidades.",
     "<strong>4. Empatia</strong> — sentir os do outro.",
   ],"tip":"<strong>Regra:</strong> a CNV vive nos modos 3 e 4 — escolha conscientemente onde colocar a atenção.","wide":True},
   {"ic":"fork","t":"Necessidade × Estratégia","b":"A <strong>necessidade</strong> é abstrata e universal (conexão, segurança, respeito); a <strong>estratégia</strong> é o meio específico de atendê-la. Confundi-las gera briga: muitas estratégias servem à mesma necessidade.","tip":"<strong>Modelo mental:</strong> o ato do outro é o <strong>estímulo</strong>; a necessidade é a <strong>causa</strong>."},
  ],
  "lessons_title":"Lições-Chave do Capítulo 5",
  "lessons":["A necessidade — não o outro — é a causa real do sentimento.","Diante de uma mensagem dura, escolha onde colocar a atenção (os 4 modos).","Necessidade não é estratégia: ache a necessidade antes de defender uma solução."]},

 {"slug":"ch06-pedidos","sub":"CAPÍTULO 6: Pedir o que Enriquece a Vida",
  "intro":"O quarto componente é o pedido: uma ação concreta, positiva e acionável que atenda à necessidade — e que aceita o 'não' sem punição. Pedido difere de exigência pela liberdade de recusa.",
  "cards":[
   {"ic":"scale","t":"O Teste do 'Não'","b":"Pedido deixa o 'não' em aberto; <strong>exigência</strong> ameaça com culpa, castigo ou retirada de afeto. Se a recusa do outro provoca punição sua — mesmo só uma cara feia — era exigência.","tip":"<strong>Como aplicar:</strong> peça 'gentilmente', mas observe o que você faz quando ouve 'não'."},
   {"ic":"target","t":"Positivo, Concreto, no Presente","b":"Diga o que <strong>fazer</strong>, não o que parar ('quero 30 min de conversa hoje', não 'pare de me ignorar'). Ação <strong>observável e realizável agora</strong> — 'seja mais carinhoso' é vago demais para virar ação.","tip":"<strong>Regra:</strong> pedido vago não tem como ser atendido — ninguém sabe o que fazer."},
   {"ic":"link","t":"Peça o Reflexo","b":"Em mensagens importantes, peça o <strong>reflexo</strong> ('o que você entendeu?') e a <strong>honestidade</strong> ('como você se sente com isto?'). Confirmar o entendimento previne metade dos conflitos.","tip":"<strong>Como aplicar:</strong> enquadre como checagem sua ('pra eu ter certeza de que me expressei bem'), não teste do outro."},
  ],
  "lessons_title":"Lições-Chave do Capítulo 6",
  "lessons":["Pedido é positivo, concreto, no presente — e aceita o 'não'.","No instante em que o 'não' é punido, o pedido virou exigência.","Peça o reflexo: confirmar o entendimento previne metade dos conflitos."]},

 {"slug":"ch07-receber-com-empatia","sub":"CAPÍTULO 7: Receber com Empatia",
  "intro":"A CNV não é só falar: é ouvir. Receber com empatia é oferecer presença plena ao que o outro observa, sente, precisa e pede — sem aconselhar, consertar ou contar a própria história.",
  "cards":[
   {"ic":"wave","t":"Empatia é Presença, não Conserto","b":"Esvazie a mente de pré-julgamentos e <strong>fique inteiro</strong> com o outro. Antes de qualquer solução, escute os 4 componentes nele e, se ajudar, <strong>reflita</strong> sentimento + necessidade em forma de pergunta.","tip":"<strong>Modelo mental:</strong> 'Não faça algo, fique aí' — a presença cura mais que o conselho."},
   {"ic":"gap","t":"Os Bloqueadores da Empatia","b":"Parecem ajuda, mas cortam a conexão: <strong>aconselhar</strong> ('o que você devia fazer…'), <strong>consolar</strong> ('vai passar'), <strong>competir</strong> ('comigo foi pior'), educar, corrigir, interrogar, contar sua história, encerrar o assunto.","tip":"<strong>Cuidado:</strong> mesmo bem-intencionados, esses bordões invalidam o que a pessoa sente.","warn":True},
   {"ic":"bubble","t":"Refletir em Pergunta","b":"Devolva sentimento + necessidade como <strong>pergunta</strong> ('Você está frustrado porque queria ter sido consultado?'), não como rótulo. Sinal de empatia suficiente: a tensão alivia ou a pessoa para de falar.","tip":"<strong>Como aplicar:</strong> 'Você está com medo de…?' abre espaço; 'Você está com medo.' fecha."},
  ],
  "lessons_title":"Lições-Chave do Capítulo 7",
  "lessons":["Empatia é presença, não conserto — não faça algo, fique aí.","Reflita sentimento + necessidade em forma de pergunta.","Conselho, consolo e 'comigo foi pior' bloqueiam a empatia, mesmo bem-intencionados."]},

 {"slug":"ch08-poder-da-empatia","sub":"CAPÍTULO 8: O Poder da Empatia",
  "intro":"A empatia tem poder de cura, desarma a hostilidade e permite até dizer 'não' sem romper a conexão. Ouvir a necessidade por trás de qualquer mensagem — inclusive um ataque — muda a dinâmica do conflito.",
  "cards":[
   {"ic":"spark","t":"Empatia Antes da Autodefesa","b":"Resista ao impulso de se defender: ouça o outro até ele se sentir <strong>compreendido</strong>, e só então apresente seu lado. A <strong>sequência importa</strong> — quem é ouvido consegue ouvir.","tip":"<strong>Como aplicar:</strong> em conflito, empatia primeiro, defesa depois — o contrário escala."},
   {"ic":"key","t":"O Ataque é um 'Obrigado' Mal-Embrulhado","b":"Por trás de toda agressão há uma <strong>necessidade não atendida</strong>. Escute-a em vez de revidar: ao sentir a necessidade reconhecida, a raiva do outro costuma baixar — e só então a solução cabe.","tip":"<strong>Modelo mental:</strong> traduza o 'chacal' do outro em sentimento + necessidade."},
   {"ic":"scale","t":"Dizer 'Não' com Empatia","b":"Um 'não' empático é um <strong>'sim' a uma necessidade sua</strong>: nomeie a necessidade que o 'não' protege ('vou dizer não a isto porque preciso de descanso').","tip":"<strong>Cuidado:</strong> 'não' seco ou cheio de desculpas alimenta a sensação de rejeição.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 8",
  "lessons":["Atrás de todo ataque há uma necessidade — escute-a antes de revidar.","Empatia antes da autodefesa: quem se sente ouvido passa a ouvir.","Um 'não' pode ser empático quando nomeia o 'sim' (a necessidade) que protege."]},

 {"slug":"ch09-auto-empatia","sub":"CAPÍTULO 9: Conexão Compassiva Consigo Mesmo",
  "intro":"A CNV mais importante é a interior. Antes de dar empatia, é preciso dar a si mesmo: observar, sentir, identificar a necessidade e fazer um pedido a si — em vez de se afogar em autorrecriminação (o 'chacal interno').",
  "cards":[
   {"ic":"spiral","t":"Auto-empatia Primeiro","b":"Aplique os 4 passos a si: o que observo em mim? o que sinto? que necessidade? que pedido faço a mim mesmo? Você <strong>não dá empatia de um tanque vazio</strong> — cuide de si antes de ajudar o outro.","tip":"<strong>Como aplicar:</strong> antes de uma conversa difícil, faça uma auto-empatia relâmpago."},
   {"ic":"pivot","t":"Traduza o 'Deveria'","b":"Cada 'eu deveria ter…' esconde uma <strong>necessidade não atendida</strong>. Troque 'eu deveria ter feito X' por 'eu <strong>queria</strong> ter feito X <strong>porque preciso de ___</strong>'. A autocrítica é só chacal mal traduzido.","tip":"<strong>Sinal de alerta:</strong> 'como pude ser tão burro' paralisa e não atende necessidade nenhuma.","warn":True},
   {"ic":"leaf","t":"Luto e Autoperdão CNV","b":"Lamente o erro conectando-se à <strong>necessidade não atendida</strong> por ele — sem culpa; e perdoe-se acolhendo a <strong>necessidade que você buscava atender</strong> ao agir como agiu. Aja por escolha, não por culpa, dever ou medo.","tip":"<strong>Modelo mental:</strong> energia limpa vem da necessidade que a ação serve, não da vergonha."},
  ],
  "lessons_title":"Lições-Chave do Capítulo 9",
  "lessons":["Auto-empatia primeiro: não se dá empatia de um tanque vazio.","Todo 'deveria' esconde uma necessidade — traduza em vez de se punir.","Luto e autoperdão CNV substituem a culpa pela conexão com a necessidade."]},

 {"slug":"ch10-raiva","sub":"CAPÍTULO 10: Expressar Plenamente a Raiva",
  "intro":"A raiva não é causada pelo outro, mas pelos julgamentos que fazemos ('ele não deveria…'). Ela é um alarme valioso: aponta uma necessidade não atendida. Expressá-la plenamente é traduzi-la, não despejá-la nem engoli-la.",
  "cards":[
   {"ic":"steps","t":"Os 4 Passos da Raiva","b":"No instante em que a raiva sobe:","list":[
     "<strong>1. Pare e respire</strong> — não faça nada, não fale.",
     "<strong>2. Identifique o julgamento</strong> que está gerando a raiva.",
     "<strong>3. Conecte-se à necessidade</strong> por trás do julgamento.",
     "<strong>4. Expresse</strong> o sentimento e a necessidade.",
   ],"tip":"<strong>Como aplicar:</strong> a raiva é a 'luz piscando'; os passos a convertem em informação útil.","wide":True},
   {"ic":"target","t":"Estímulo × Causa","b":"O ato do outro é o <strong>estímulo</strong>; a <strong>causa</strong> é o julgamento que fazemos ('ele é um aproveitador') + a necessidade não atendida. Diga 'estou com raiva <strong>porque preciso de ___</strong>', nunca 'você me deixa com raiva'.","tip":"<strong>Modelo mental:</strong> a raiva é um presente embrulhado — por dentro está a necessidade que mais importa agora."},
   {"ic":"sword","t":"Nem Despejar, nem Reprimir","b":"<strong>Despejar</strong> a raiva ('a culpa é toda sua!') alivia por segundos e destrói a conexão; <strong>reprimir</strong> vira ressentimento e chacal interno. A CNV oferece um <strong>terceiro caminho</strong>: traduzir.","tip":"<strong>Cuidado:</strong> sob a raiva quase sempre há medo, mágoa ou solidão.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 10",
  "lessons":["O outro é o estímulo; o julgamento é a causa da raiva.","Os 4 passos: parar, ver o julgamento, achar a necessidade, expressá-la.","Há um terceiro caminho entre despejar e reprimir: traduzir a raiva em necessidade."]},

 {"slug":"ch11-gratidao-e-poder-protetor","sub":"CAPÍTULO 11: Gratidão e o Uso Protetor da Força",
  "intro":"A CNV também muda como elogiamos e como agimos quando o diálogo não é possível. A gratidão celebra sem julgar; e quando não dá tempo de dialogar, usa-se a força protetora — nunca a punitiva.",
  "cards":[
   {"ic":"spark","t":"Gratidão CNV em 3 Partes","b":"O elogio comum ('você é incrível') ainda é um <strong>julgamento de cima</strong>. A gratidão CNV celebra com: <strong>o que a pessoa fez</strong> (observação) + <strong>como me sinto</strong> (sentimento) + <strong>que necessidade minha foi atendida</strong>.","tip":"<strong>Como aplicar:</strong> receba gratidão sem falsa modéstia nem ego — é só uma necessidade atendida.","wide":True},
   {"ic":"scale","t":"Força Protetora × Punitiva","b":"<strong>Protetora</strong>: usada para proteger a vida/direitos, sem julgar (segurar a criança que corre para a rua). <strong>Punitiva</strong>: para fazer o outro sofrer, baseada em 'merecimento'. A fronteira é a <strong>intenção</strong>.","tip":"<strong>Regra:</strong> pergunte antes de agir: estou protegendo ou punindo?","wide":True},
   {"ic":"sword","t":"O Custo da Punição","b":"A força punitiva produz <strong>obediência por medo</strong>, não cooperação — e corrói a boa vontade. Veja o ato prejudicial do outro como <strong>ignorância da CNV</strong>, não como maldade que 'merece' castigo.","tip":"<strong>Cuidado:</strong> castigar 'para o outro aprender' gera ressentimento, não mudança.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 11",
  "lessons":["Gratidão CNV celebra com observação + sentimento + necessidade — não com rótulos.","Receba gratidão sem falsa modéstia nem ego: é só uma necessidade atendida.","Use a força para proteger, nunca para punir — a punição custa a boa vontade."]},
]
