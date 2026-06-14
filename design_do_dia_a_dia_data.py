# -*- coding: utf-8 -*-
"""Conteúdo (pt-BR) das páginas da biblioteca para 'O Design do Dia a Dia'
(Don Norman — The Design of Everyday Things). Frameworks canônicos: a culpa é
do design, não do usuário; os 5 princípios fundamentais (affordances /
significantes / mapeamento / feedback / restrições); mapeamento natural;
restrições físicas, culturais, semânticas e lógicas; modelo conceitual ×
modelo mental e a imagem do sistema; o Golfo da Execução e o da Avaliação +
os 7 estágios da ação; conhecimento na cabeça × no mundo; deslizes × enganos
e design à prova de erro; funções de força (poka-yoke, interlock, lock-in,
lock-out); HCD e o Duplo Diamante. Base: síntese dos frameworks amplamente
documentados — não reproduz o texto."""

BOOK = {
 "title": "O Design do Dia a Dia",
 "author": "Don Norman",
 "header_light": "O DESIGN",
 "header_bold": "DO DIA A DIA",
 "subtitle": "VISÃO GERAL · OS PRINCÍPIOS DO DESIGN CENTRADO NO HUMANO",
 "intro": "Por que algumas portas a gente empurra quando deveria puxar, e sai com a sensação de ser burro? Don Norman responde: a culpa é do design, não do usuário. Nesta obra fundadora da UX, ele mostra que objetos bem projetados comunicam sozinhos o que se pode fazer e o que cada coisa significa — e nos dá o vocabulário para enxergar (e consertar) o mau design em tudo à nossa volta.",
 "description": "O clássico que inventou o vocabulário do design centrado no humano. Don Norman explica os cinco princípios que fazem um objeto se explicar sozinho — affordances, significantes, mapeamento, feedback e restrições — e por que 'erro humano' quase sempre é erro de design. Da psicologia da ação (os dois golfos, os sete estágios) ao design à prova de erro (deslizes × enganos, funções de força, poka-yoke), é o manual para projetar coisas que as pessoas conseguem usar sem manual.",
 "tags": ["Design", "UX", "Produtos Digitais"],
 "progress": "10 Capítulos",
 "cover": "assets/design-do-dia-a-dia-cover.png",
 "overview_cards": [
   {"ic":"key","t":"A Culpa é do Design, Não do Usuário","b":"O princípio-mãe da obra. Quando as pessoas erram, se sentem burras ou precisam de manual para o básico, o <strong>objeto está mal projetado</strong> — não as pessoas mal preparadas. 'Erro humano' quase sempre é erro de design. A pergunta certa nunca é 'por que erraram?', mas <strong>'o que no design induziu o erro?'</strong>.","tip":"<strong>Como aplicar:</strong> diante de qualquer falha de uso recorrente, conserte o objeto — não tente 'treinar o usuário a prestar mais atenção'.","wide":True},
   {"ic":"layers","t":"Os 5 Princípios Fundamentais","b":"O checklist de todo bom design. <strong>Affordances</strong>: o que o objeto permite fazer. <strong>Significantes</strong>: sinais que dizem onde e como agir. <strong>Mapeamento</strong>: a relação controle→efeito (o natural espelha a função). <strong>Feedback</strong>: resposta imediata ao que você fez. <strong>Restrições</strong>: limites que guiam ao caminho certo.","tip":"<strong>Modelo mental:</strong> affordance é a possibilidade; significante é o anúncio dela. O designer controla o significante muito mais do que a affordance.","wide":True},
   {"ic":"gap","t":"Os Dois Golfos da Ação","b":"Toda ação cruza dois abismos. O <strong>Golfo da Execução</strong> ('como eu faço isto?') é fechado por significantes, mapeamento e restrições. O <strong>Golfo da Avaliação</strong> ('o que aconteceu? deu certo?') é fechado por feedback e um modelo conceitual claro. A função do designer é construir essas pontes.","tip":"<strong>Como aplicar:</strong> use os 7 estágios da ação para diagnosticar em que ponto exato sua interface trava o usuário."},
 ],
}

CHAPTERS = [
 {"slug":"ch01-psicopatologia","sub":"CAPÍTULO 1: A Psicopatologia das Coisas do Dia a Dia",
  "intro":"Quando um objeto é difícil de usar, a culpa é do design, não da pessoa. Bons objetos comunicam sozinhos o que fazer; objetos ruins exigem manuais, geram erros e fazem o usuário se sentir burro. Este é o ponto de partida de toda a obra.",
  "cards":[
   {"ic":"key","t":"A Culpa é do Design, Não do Usuário","b":"O princípio fundador. Se as pessoas erram sistematicamente num objeto, o objeto está mal projetado — não as pessoas mal preparadas. Troque <strong>'por que erraram?'</strong> por <strong>'o que no design induziu o erro?'</strong>.","tip":"<strong>Como aplicar:</strong> nunca encerre a análise em 'erro humano'; é onde a investigação deveria começar, no design."},
   {"ic":"eye","t":"Descobribilidade e Compreensão","b":"Dois testes de todo objeto. <strong>Descobribilidade</strong>: dá para descobrir quais ações são possíveis e como executá-las? <strong>Compreensão</strong>: o que tudo isso significa, como devo usar? Um bom produto torna o que se pode fazer <strong>visível</strong>.","tip":"<strong>Modelo mental:</strong> o objeto é um comunicador — deve 'dizer' o que faz sem palavras."},
   {"ic":"gap","t":"As \"Portas Norman\"","b":"O exemplo-ícone do mau design: a porta cujo design <strong>'mente'</strong> sobre como operá-la — você puxa quando deveria empurrar. Se a porta precisa de uma placa 'EMPURRE', o design já falhou. A solução é um significante físico: barra para puxar, placa para empurrar.","tip":"<strong>Sinal de alerta:</strong> se a operação básica exige etiqueta ou manual, o design está errado.","warn":True},
  ],
  "lessons_title":"Lições-Chave: A Psicopatologia",
  "lessons":["Dificuldade de uso é defeito de design, não de inteligência do usuário.","Bons produtos são descobríveis (vê-se o que fazer) e compreensíveis (sabe-se o que significa).","Se um objeto precisa de manual para a operação básica, ele está mal projetado."]},

 {"slug":"ch02-affordances-significantes-mapeamento","sub":"CAPÍTULO 2: Affordances, Significantes, Mapeamento e Feedback",
  "intro":"O design comunica por cinco princípios psicológicos: affordances (o que é possível), significantes (onde/como agir), mapeamento (controle→efeito), feedback (o que aconteceu) e restrições (o que não fazer). Aqui ficam os quatro primeiros.",
  "cards":[
   {"ic":"target","t":"Affordances × Significantes","b":"<strong>Affordance</strong> é a relação entre o objeto e quem usa, que determina o que é possível fazer (uma cadeira oferece sentar). <strong>Significante</strong> é o sinal perceptível que indica <strong>onde e como agir</strong>. A affordance existe; o significante a anuncia — e é ele que o designer mais controla.","tip":"<strong>Como aplicar:</strong> não basta a ação ser possível; torne-a visível com um significante claro (seta, barra, rótulo).","wide":True},
   {"ic":"link","t":"Mapeamento Natural","b":"É a correspondência entre controles e seus efeitos. O <strong>mapeamento natural</strong> usa analogias espaciais/culturais para ser entendido na hora — como controles do fogão dispostos igual às bocas, dispensando etiquetas.","tip":"<strong>Como aplicar:</strong> quando houver correspondência espacial óbvia, espelhe-a no layout dos controles."},
   {"ic":"wave","t":"Feedback Imediato","b":"Informação instantânea e informativa sobre o resultado de uma ação. Sem feedback, o usuário fica inseguro e <strong>repete a ação</strong> (às vezes disparando duas vezes). Mas feedback em excesso vira ruído e é ignorado.","tip":"<strong>Cuidado:</strong> nem ausente, nem excessivo — calibre a prioridade do que o produto comunica.","warn":True},
  ],
  "lessons_title":"Lições-Chave: Os Princípios",
  "lessons":["Affordances dizem o que é possível; significantes dizem onde e como — projete os dois.","Mapeamento natural deixa a relação controle→efeito autoevidente.","Todo controle precisa de feedback imediato e informativo — nem ausente, nem excessivo."]},

 {"slug":"ch03-psicologia-das-acoes","sub":"CAPÍTULO 3: A Psicologia das Ações do Dia a Dia",
  "intro":"Toda ação atravessa uma ponte entre o que queremos e o mundo. Quando o design não ajuda a planejar a ação nem a interpretar o resultado, abrem-se dois abismos: o Golfo da Execução e o Golfo da Avaliação.",
  "cards":[
   {"ic":"steps","t":"Os 7 Estágios da Ação","b":"O ciclo completo de uma ação, útil para diagnosticar onde a interface falha: <strong>Objetivo → Plano → Especificar → Executar → Perceber → Interpretar → Comparar</strong> com o objetivo. Localize em qual estágio o usuário trava.","tip":"<strong>Como aplicar:</strong> use os 7 estágios como checklist de diagnóstico de qualquer interface.","wide":True},
   {"ic":"gap","t":"Os Dois Golfos","b":"O <strong>Golfo da Execução</strong> ('como eu faço?') é a distância entre intenção e ação — estreitado por significantes, mapeamento e restrições. O <strong>Golfo da Avaliação</strong> ('o que aconteceu? deu certo?') é a distância entre o estado do sistema e o entendimento — estreitado por feedback e bom modelo conceitual.","tip":"<strong>Modelo mental:</strong> o trabalho do designer é construir pontes sobre os dois golfos."},
   {"ic":"lens","t":"Os 3 Níveis de Processamento","b":"O design afeta a pessoa em três camadas: o <strong>visceral</strong> (reação imediata, estética, instinto), o <strong>comportamental</strong> (uso, expectativa, controle) e o <strong>reflexivo</strong> (significado, memória, autoimagem).","tip":"<strong>Como aplicar:</strong> projete para os três — primeira impressão, facilidade de uso e o significado que fica."},
  ],
  "lessons_title":"Lições-Chave: A Psicologia da Ação",
  "lessons":["Use os 7 estágios para localizar exatamente onde uma interface falha.","Significantes estreitam o golfo da execução; feedback estreita o da avaliação.","Projete para os três níveis: visceral, comportamental e reflexivo."]},

 {"slug":"ch04-conhecimento-cabeca-mundo","sub":"CAPÍTULO 4: Conhecimento na Cabeça e no Mundo",
  "intro":"Não precisamos guardar tudo na memória: o mundo é um repositório de conhecimento. Bons designs colocam conhecimento no mundo — visível no objeto — para não exigir que o usuário memorize.",
  "cards":[
   {"ic":"book","t":"Conhecimento no Mundo × na Cabeça","b":"<strong>No mundo</strong>: informação visível no objeto (rótulos, formatos, posições) — fácil de usar, dispensa decorar. <strong>Na cabeça</strong>: memorizada — eficiente, mas frágil e exige aprendizado. Distinguimos moedas no bolso sem saber desenhá-las: o objeto carrega o que precisamos.","tip":"<strong>Como aplicar:</strong> sempre que exigir memória, pergunte 'posso deixar isto visível no objeto?'.","wide":True},
   {"ic":"bulb","t":"Modelo Conceitual × Modelo Mental","b":"O <strong>modelo conceitual</strong> é a explicação simplificada de como o objeto funciona, que o design comunica. O <strong>modelo mental</strong> é o que o usuário constrói na cabeça. Quando os dois divergem, surgem os erros (ex.: 'girar o termostato no máximo aquece mais rápido').","tip":"<strong>Modelo mental:</strong> erros nascem quando o que o usuário acredita não bate com como a coisa realmente funciona."},
   {"ic":"eye","t":"A Imagem do Sistema","b":"O designer não fala direto com o usuário: ele só se comunica pela <strong>imagem do sistema</strong> — tudo que o usuário consegue ver e perceber do produto. Se o modelo conceitual não está visível no produto, ele <strong>não existe</strong> para o usuário.","tip":"<strong>Como aplicar:</strong> torne o modelo conceitual visível na própria interface; é o único canal que você tem.","warn":True},
  ],
  "lessons_title":"Lições-Chave: O Conhecimento",
  "lessons":["Não force memorização: coloque o conhecimento necessário no próprio objeto.","O designer comunica o modelo conceitual só pela imagem do sistema — torne-a clara.","Erros surgem quando o modelo mental do usuário diverge do modelo conceitual real."]},

 {"slug":"ch05-restricoes-descoberta","sub":"CAPÍTULO 5: Restrições, Descobribilidade e Feedback",
  "intro":"Restrições limitam as ações possíveis e guiam o usuário ao caminho certo sem que ele precise pensar. Reduzem o que há para aprender e tornam o erro difícil ou impossível.",
  "cards":[
   {"ic":"scale","t":"As 4 Restrições","b":"O quarteto que orienta a ação. <strong>Físicas</strong>: a geometria impede o caminho errado (a tomada que só encaixa numa orientação). <strong>Culturais</strong>: convenções aprendidas (vermelho = parar). <strong>Semânticas</strong>: o significado da situação restringe (o vidro vai na frente). <strong>Lógicas</strong>: o raciocínio elimina alternativas (sobrou uma peça e um buraco — é ali).","tip":"<strong>Como aplicar:</strong> combine as quatro para que a única ação possível seja a correta.","wide":True},
   {"ic":"link","t":"Convenções e Padronização","b":"Quando não há mapeamento natural, <strong>padronize</strong> (pedais, teclado QWERTY). A convenção vira conhecimento cultural compartilhado e reduz o que cada um precisa aprender do zero.","tip":"<strong>Regra:</strong> sem analogia espacial óbvia, a próxima melhor coisa é a uniformidade."},
   {"ic":"wave","t":"O Som como Confirmação","b":"Ruídos naturais (o clique da fechadura, o zíper) funcionam como <strong>feedback e significantes</strong>: confirmam que a ação aconteceu. Silenciar mal um produto remove esse sinal e gera insegurança.","tip":"<strong>Cuidado:</strong> ao 'limpar' os sons de um produto, você pode estar removendo feedback essencial.","warn":True},
  ],
  "lessons_title":"Lições-Chave: As Restrições",
  "lessons":["Use as quatro restrições para tornar o caminho certo o único óbvio.","Restrições reduzem o que o usuário precisa aprender e o erro que pode cometer.","Sem mapeamento natural, padronize e respeite convenções estabelecidas."]},

 {"slug":"ch06-funcoes-de-forca","sub":"CAPÍTULO 6: Funções de Força — Tornar Difícil o Erro Grave",
  "intro":"Quando um erro pode ser perigoso ou caro, restrições comuns não bastam: usa-se uma função de força — uma restrição forte que impede a ação seguinte até o passo certo, ou trava o usuário fora de uma ação perigosa.",
  "cards":[
   {"ic":"sword","t":"Funções de Força: os 3 tipos","b":"Restrições que interrompem a operação a menos que o passo certo seja cumprido. <strong>Interlock</strong>: força uma ordem (o micro-ondas não liga de porta aberta). <strong>Lock-in</strong>: impede encerrar cedo ('salvar antes de sair?'). <strong>Lock-out</strong>: bloqueia zona perigosa (escada barrada no térreo).","tip":"<strong>Como aplicar:</strong> use quando o custo do erro for alto — escolha o tipo pela natureza do risco.","wide":True},
   {"ic":"constellation","t":"Poka-yoke (À Prova de Erro)","b":"Princípio da qualidade japonesa: projetar para que a montagem ou operação errada seja <strong>fisicamente impossível</strong>. Pinos assimétricos, encaixes únicos, contadores de peças — dispositivos simples que eliminam classes inteiras de erro.","tip":"<strong>Regra:</strong> o melhor controle de erro é a impossibilidade física de errar."},
   {"ic":"bubble","t":"Aviso Não Basta para o Grave","b":"Para erros sérios e irreversíveis, confiar só em avisos ('cuidado!') é fraco — o usuário se distrai, especialmente sob estresse. O erro grave precisa ser <strong>bloqueado</strong>, não advertido.","tip":"<strong>Cuidado:</strong> funções de força no lugar errado viram burocracia e são burladas — anulando também a proteção real.","warn":True},
  ],
  "lessons_title":"Lições-Chave: Funções de Força",
  "lessons":["Para erros graves, não avise: torne o erro impossível com uma função de força.","Interlock (ordem), lock-in (permanência), lock-out (zona proibida) — escolha pelo risco.","Poka-yoke: o melhor controle de erro é a impossibilidade física de errar."]},

 {"slug":"ch07-erro-humano-mau-design","sub":"CAPÍTULO 7: Erro Humano? Não, Mau Design",
  "intro":"A maioria dos chamados 'erros humanos' são erros de design: o sistema permitiu, induziu ou não preveniu o engano. Há dois tipos fundamentais de erro — deslizes e enganos — e cada um pede um remédio de design diferente.",
  "cards":[
   {"ic":"pivot","t":"Deslizes × Enganos","b":"A distinção mestre. <strong>Deslize (slip)</strong>: o objetivo está certo, mas a ação sai errada — por desatenção, em tarefas automáticas. <strong>Engano (mistake)</strong>: a ação é executada certa, mas o objetivo ou plano estava errado — falha de decisão ou de modelo mental.","tip":"<strong>Como aplicar:</strong> pergunte 'objetivo certo ou errado?'. Certo + ação ruim = deslize; errado de origem = engano.","wide":True},
   {"ic":"target","t":"Remédios Distintos por Tipo","b":"Deslizes pedem <strong>feedback, restrições, undo e funções de força</strong> (proteger a execução). Enganos pedem <strong>melhor modelo conceitual e informação</strong> (corrigir a decisão). Tratar os dois igual não funciona.","tip":"<strong>Modelo mental:</strong> deslize é falha de execução; engano é falha de planejamento — remédios diferentes."},
   {"ic":"mask","t":"Mode Error e a Raiz Sistêmica","b":"O <strong>deslize de modo (mode error)</strong>: o sistema está num modo e o usuário pensa que está noutro — clássico de interfaces com modos invisíveis. Erros raramente têm causa única: em vez de 'quem errou?', pergunte <strong>'por que o sistema permitiu o erro?'</strong>.","tip":"<strong>Cuidado:</strong> punir o operador e encerrar a análise garante que o erro se repita com a próxima pessoa.","warn":True},
  ],
  "lessons_title":"Lições-Chave: Erro Humano",
  "lessons":["Classifique o erro: deslize (objetivo certo, ação errada) ou engano (objetivo errado).","Deslizes pedem feedback e funções de força; enganos pedem melhor modelo conceitual.","Não culpe o usuário: pergunte por que o sistema permitiu o erro e corrija o design."]},

 {"slug":"ch08-design-a-prova-de-erro","sub":"CAPÍTULO 8: Design à Prova de Erro",
  "intro":"Já que pessoas vão errar, o design deve assumir o erro e trabalhar com ele: dificultar o erro grave, facilitar a detecção e tornar a recuperação simples. Errar deve ser barato e reversível.",
  "cards":[
   {"ic":"steps","t":"A Hierarquia da Defesa","b":"Quatro camadas, nesta ordem: <strong>Prevenir</strong> (restrições e funções de força), <strong>tornar visível</strong> (bom feedback para perceber o erro logo), <strong>tornar reversível</strong> (undo barato) e <strong>confirmar</strong> — só o irreversível.","tip":"<strong>Como aplicar:</strong> errar deve ser barato; se o erro custa caro, projete reversibilidade ou trava.","wide":True},
   {"ic":"spark","t":"O Poder do Desfazer (Undo)","b":"A defesa mais poderosa contra deslizes: torna o erro inofensivo. Excluir um e-mail deve <strong>mover para a lixeira</strong> (reversível) com um discreto 'Desfazer', em vez de apagar com um pop-up 'Tem certeza?' que todos clicam no automático.","tip":"<strong>Regra:</strong> reserve confirmações pesadas para o irreversível; para o resto, ofereça undo."},
   {"ic":"bubble","t":"Mensagem de Erro como Ajuda","b":"A mensagem deve explicar o problema <strong>e como corrigi-lo</strong>, em linguagem humana — nunca apenas acusar ('Erro 0x8007'). Idealmente, permita corrigir ali mesmo.","tip":"<strong>Cuidado:</strong> confirmar tudo gera cegueira de confirmação — o usuário clica 'sim' até no irreversível.","warn":True},
  ],
  "lessons_title":"Lições-Chave: À Prova de Erro",
  "lessons":["Assuma que erros vão acontecer: previna o grave, torne tudo visível e reversível.","Reserve confirmações pesadas para o irreversível; para o resto, ofereça desfazer.","Mensagens de erro devem explicar e ajudar a corrigir, nunca apenas acusar."]},

 {"slug":"ch09-design-centrado-no-humano","sub":"CAPÍTULO 9: Design Centrado no Humano e Design Thinking",
  "intro":"O bom design começa resolvendo o problema certo e parte das necessidades reais das pessoas. O Design Centrado no Humano (HCD) é um processo iterativo de observar, idear, prototipar e testar, repetidamente.",
  "cards":[
   {"ic":"leaf","t":"Design Centrado no Humano (HCD)","b":"Filosofia que coloca as necessidades, capacidades e comportamento das pessoas em primeiro lugar — e adapta o design a elas, não o contrário. O processo: <strong>Observar → Idear → Prototipar → Testar</strong>, em ciclos rápidos e baratos.","tip":"<strong>Como aplicar:</strong> prototipe para aprender; falhe cedo e barato. O protótipo é uma pergunta, não um produto.","wide":True},
   {"ic":"mountain","t":"O Duplo Diamante","b":"Dois ciclos de divergir-convergir. <strong>Diamante 1</strong>: encontrar o problema certo (explorar, depois definir). <strong>Diamante 2</strong>: encontrar a solução certa (idear, depois entregar). Resolver bem o problema errado é inútil — use os '5 porquês' para chegar à causa-raiz.","tip":"<strong>Modelo mental:</strong> antes de 'como resolvo?', pergunte 'qual é o problema real?'."},
   {"ic":"lens","t":"Observe, Não Pergunte","b":"Pesquisa observacional no contexto real revela necessidades que as pessoas não verbalizam. <strong>Comportamento real vence opinião declarada</strong>: não confie só no que dizem, observe o que fazem.","tip":"<strong>Cuidado:</strong> pular direto para a solução e empilhar funções (featuritis) é projetar para o problema aparente, não o real.","warn":True},
  ],
  "lessons_title":"Lições-Chave: HCD",
  "lessons":["Resolva o problema certo antes de buscar a solução certa (Duplo Diamante).","HCD é iterativo: observar → idear → prototipar → testar, repetidamente.","Observe o comportamento real das pessoas; não confie só no que elas dizem."]},

 {"slug":"ch10-design-no-mundo-dos-negocios","sub":"CAPÍTULO 10: Design no Mundo dos Negócios",
  "intro":"Na prática, o design ideal colide com prazo, custo, concorrência e política interna. Entender essas forças — e como as tecnologias evoluem e se difundem — separa o bom design teórico do produto que realmente chega às pessoas.",
  "cards":[
   {"ic":"scale","t":"As Forças que Distorcem o Design","b":"Bom design é também <strong>negociação</strong> com prazo, orçamento, marketing, concorrência e legados — não busca da perfeição isolada. É isso que explica por que produtos 'óbvios' saem ruins.","tip":"<strong>Modelo mental:</strong> pense no design como negociação de restrições, não como perfeição num vácuo.","wide":True},
   {"ic":"spiral","t":"Featuritis (Creeping Featurism)","b":"A tendência de adicionar funções a cada versão — cada uma defensável, o conjunto insustentável. Mais funções vendem na vitrine, mas <strong>degradam o uso</strong>.","tip":"<strong>Cuidado:</strong> não empilhe funções para 'vencer na lista de especificações'; cada uma cobra um preço em usabilidade.","warn":True},
   {"ic":"clock","t":"Incremental × Radical e os Legados","b":"A inovação <strong>incremental</strong> melhora o que existe (a maioria, e mais segura); a <strong>radical</strong> cria categorias novas (rara, arriscada, lenta de aceitar). A tecnologia muda, as pessoas não tanto — e padrões/legados (o QWERTY) persistem por coordenação social, não por serem ótimos.","tip":"<strong>Como aplicar:</strong> aposte no incremental como regra e trate o radical como aposta de longo prazo."},
  ],
  "lessons_title":"Lições-Chave: O Mundo dos Negócios",
  "lessons":["Bom design é negociação com prazo, custo, marketing e concorrência.","Resista à featuritis: cada função extra cobra um preço em usabilidade.","Espere inovação majoritariamente incremental; trate a radical como aposta de longo prazo."]},
]
