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
      {"ic":"key","t":"A Culpa é do Design, Não Sua","emph":"Design","b":"Você esbarra na porta e se sente o tolo da sala. O princípio de ouro desfaz o feitiço: se usuários saudáveis falham de forma consistente ao manusear um objeto, o defeito não está neles. <strong>Troque a caça às bruxas do 'quem errou?' por um raio-X no design que induziu a queda.</strong>","tip":"<strong>Como aplicar:</strong> ao errar, engula a culpa e investigue a máquina. O erro humano é o sintoma, a arquitetura ruim é a doença."},
      {"ic":"eye","t":"Descobrir e Compreender","emph":"Compreender","b":"Todo projeto precisa passar em dois testes ferozes. O primeiro verifica a descobribilidade: é possível bater o olho e ver quais botões apertar? O segundo mede a compreensão: dá para sacar o que o maquinário faz? <strong>Um objeto bem concebido conversa com você no silêncio e grita as suas utilidades.</strong>","tip":"<strong>Modelo mental:</strong> pense nos produtos como guias mudos; se eles não pegam a sua mão e ensinam o caminho, eles falharam."},
      {"ic":"gap","t":"A Síndrome das Portas Norman","emph":"Portas Norman","b":"O retrato máximo da incompetência é uma porta maçica que exibe a alça, mas exige o empurrão. Se a operação mais elementar precisa de uma plaquinha adesiva explicando as regras, a derrota do design já está declarada. <strong>Placas são bengalas para arquiteturas que fracassaram na comunicação básica.</strong>","tip":"<strong>Sinal de alerta:</strong> quando você gasta fita crepe e canetão para etiquetar um painel, não tente embelezar, reprojete.","warn":True},
    ],
  "lessons_title":"Lições-Chave: A Psicopatologia",
  "lessons":["Dificuldade de uso é defeito de design, não de inteligência do usuário.","Bons produtos são descobríveis (vê-se o que fazer) e compreensíveis (sabe-se o que significa).","Se um objeto precisa de manual para a operação básica, ele está mal projetado."]},

 {"slug":"ch02-affordances-significantes-mapeamento","sub":"CAPÍTULO 2: Affordances, Significantes, Mapeamento e Feedback",
  "intro":"O design comunica por cinco princípios psicológicos: affordances (o que é possível), significantes (onde/como agir), mapeamento (controle→efeito), feedback (o que aconteceu) e restrições (o que não fazer). Aqui ficam os quatro primeiros.",
  "cards":[
      {"ic":"target","t":"Affordances e Significantes","emph":"Significantes","b":"A cadeira carrega consigo a affordance, a promessa física de que suporta o seu peso. Porém, sem os significantes — linhas, cores, relevos e barras que acenam —, você não sabe onde exatamente pousar. <strong>A física permite a ação, mas apenas a sinalização afiada garante a execução.</strong>","tip":"<strong>Como aplicar:</strong> em interfaces digitais, não presuma que um quadrado será clicado; encha-o de sombras e molduras que chamem o toque."},
      {"ic":"link","t":"O Mapeamento Natural","emph":"Mapeamento","b":"É a geografia da intuição traduzida no metal. Quando o botão frontal do fogão acende a boca frontal, ele espelha o espaço real e elimina a necessidade de qualquer bula. <strong>Você rouba a familiaridade da natureza para aniquilar o esforço do aprendizado.</strong>","tip":"<strong>Regra:</strong> disponha comandos do mesmo jeito que a ação vai ocorrer no espaço físico — em cima para subir, à direita para avançar."},
      {"ic":"wave","t":"O Retorno Imediato","emph":"Retorno","b":"A falta de feedback mergulha o usuário num breu torturante de dúvidas, fazendo-o esmagar o teclado pela segunda vez. Um bipe curto, um clique, uma cor que pisca. <strong>Mas cuidado: um excesso barulhento de respostas transforma informação crítica em ruído inútil e irritante.</strong>","tip":"<strong>Modelo mental:</strong> entregue o feedback na fração de segundo exata da ação. Atrasos minúsculos geram frustrações monumentais."},
    ],
  "lessons_title":"Lições-Chave: Os Princípios",
  "lessons":["Affordances dizem o que é possível; significantes dizem onde e como — projete os dois.","Mapeamento natural deixa a relação controle→efeito autoevidente.","Todo controle precisa de feedback imediato e informativo — nem ausente, nem excessivo."]},

 {"slug":"ch03-psicologia-das-acoes","sub":"CAPÍTULO 3: A Psicologia das Ações do Dia a Dia",
  "intro":"Toda ação atravessa uma ponte entre o que queremos e o mundo. Quando o design não ajuda a planejar a ação nem a interpretar o resultado, abrem-se dois abismos: o Golfo da Execução e o Golfo da Avaliação.",
  "cards":[
      {"ic":"steps","t":"Os Sete Degraus da Ação","emph":"Degraus","b":"Uma ação nunca é um estalo; é um arco cirúrgico. Começa ao planejar o objetivo, detalhar o movimento, executá-lo e, na volta, observar as mudanças e compará-las com a intenção inicial. <strong>Entenda essas sete fatias e você saberá diagnosticar precisamente em qual pedaço o cliente tropeçou.</strong>","tip":"<strong>Prática:</strong> use a jornada dos 7 degraus como um pente fino rigoroso na hora de auditar as fricções de qualquer produto."},
      {"ic":"gap","t":"A Travessia dos Dois Golfos","emph":"Golfos","b":"De um lado está o Golfo da Execução — o inferno de não saber como fazer a máquina funcionar. Do outro, o Golfo da Avaliação — a cegueira de não entender se a máquina fez o que foi pedido. <strong>O arquiteto genial lança pontes estaiadas sobre ambos, com mapeamento claro na ida e feedback afiado na volta.</strong>","tip":"<strong>Como aplicar:</strong> pergunte ao projeto: \"Como o usuário adivinha a primeira ação?\" e \"Como ele sabe que a ação deu certo?\""},
      {"ic":"lens","t":"A Alma Dividida em Três","emph":"Três","b":"O impacto acontece em três níveis: o instinto visceral que saliva perante a beleza pura, o controle comportamental que se deleita na usabilidade elegante, e a camada reflexiva profunda, a memória gloriosa que afaga a própria autoimagem. <strong>Não foque apenas em um; o projeto de elite seduz em todos eles.</strong>","tip":"<strong>Modelo mental:</strong> a estética ganha a entrada, o uso dita a permanência, o orgulho de dono constrói a devoção duradoura."},
    ],
  "lessons_title":"Lições-Chave: A Psicologia da Ação",
  "lessons":["Use os 7 estágios para localizar exatamente onde uma interface falha.","Significantes estreitam o golfo da execução; feedback estreita o da avaliação.","Projete para os três níveis: visceral, comportamental e reflexivo."]},

 {"slug":"ch04-conhecimento-cabeca-mundo","sub":"CAPÍTULO 4: Conhecimento na Cabeça e no Mundo",
  "intro":"Não precisamos guardar tudo na memória: o mundo é um repositório de conhecimento. Bons designs colocam conhecimento no mundo — visível no objeto — para não exigir que o usuário memorize.",
  "cards":[
      {"ic":"book","t":"Onde Guardar o Conhecimento","emph":"Onde Guardar","b":"Depender puramente da memória é sobrecarregar a cabeça e convidar ao erro sob estresse. A sabedoria do design é <strong>distribuir as pistas, os tamanhos e as formas no próprio ambiente</strong>, permitindo que a geografia indique o caminho sem necessitar de decoreba exaustiva.","tip":"<strong>Como aplicar:</strong> se a interface exigir memorização de códigos difíceis, limpe a tela e deixe as opções óbvias à vista."},
      {"ic":"bulb","t":"O Choque dos Modelos","emph":"Choque","b":"O criador desenha o modelo conceitual de como a engenharia trabalha. O usuário forja o modelo mental no escuro, tentando adivinhar as engrenagens ocultas. <strong>As faíscas destrutivas surgem no exato momento em que essas duas interpretações entram em colapso.</strong>","tip":"<strong>Sinal de alerta:</strong> quando o cliente acredita que apertar dez vezes seguidas acelera a impressora, seu modelo conceitual faliu."},
      {"ic":"eye","t":"A Interface É o Único Embaixador","emph":"Embaixador","b":"O designer está calado, distante, inacessível. A única forma de sussurrar para o usuário é por meio da blindagem visível do aparelho — a imagem do sistema. <strong>Tudo que o projeto quer comunicar precisa estar cravado nas curvas, telas e botões. O que for invisível, simplesmente não existe.</strong>","tip":"<strong>Regra:</strong> não aposte que os manuais em letras miúdas vão preencher os buracos mortos que a interface omitiu."},
    ],
  "lessons_title":"Lições-Chave: O Conhecimento",
  "lessons":["Não force memorização: coloque o conhecimento necessário no próprio objeto.","O designer comunica o modelo conceitual só pela imagem do sistema — torne-a clara.","Erros surgem quando o modelo mental do usuário diverge do modelo conceitual real."]},

 {"slug":"ch05-restricoes-descoberta","sub":"CAPÍTULO 5: Restrições, Descobribilidade e Feedback",
  "intro":"Restrições limitam as ações possíveis e guiam o usuário ao caminho certo sem que ele precise pensar. Reduzem o que há para aprender e tornam o erro difícil ou impossível.",
  "cards":[
      {"ic":"scale","t":"As Quatro Jaulas da Ação","emph":"Quatro Jaulas","b":"Use as restrições físicas para tornar o caminho falso impossível. Imponha barreiras culturais, semânticas e correntes lógicas que gritem a solução óbvia por exclusão. <strong>Em conjunto, essas barricadas estreitam o universo de opções, deixando o acerto como a única avenida possível.</strong>","tip":"<strong>Prática:</strong> amarre as peças de modo assimétrico — crie conexões que só encaixam quando empurradas pelo lado perfeito."},
      {"ic":"link","t":"A Padronização Pacifica","emph":"Padronização","b":"Sempre que faltar uma relação natural imediata, convoque a autoridade da padronização. Ela enraíza convenções globais que, mesmo imperfeitas como o teclado QWERTY, se recusam a morrer. <strong>Um idioma unificado evita o sacrifício de alfabetizar usuários repetidas vezes.</strong>","tip":"<strong>Como aplicar:</strong> fuja da reinvenção da roda; se uma cor, um símbolo ou uma posição já viraram jargão visual global, obedeça."},
      {"ic":"wave","t":"O Assinatura do Som","emph":"Assinatura","b":"O estalo seco da fechadura é um veredito instantâneo; você nem precisa puxar a maçaneta de novo. Esses sons naturais operam simultaneamente como confirmações inquestionáveis e guias invisíveis. <strong>Ao amputar o barulho e silenciar o aparelho por estética, você desorienta as certezas.</strong>","tip":"<strong>Sinal de alerta:</strong> cuidado com o impulso de \"limpar o design\" a ponto de remover os estalos que transmitem seguridade."},
    ],
  "lessons_title":"Lições-Chave: As Restrições",
  "lessons":["Use as quatro restrições para tornar o caminho certo o único óbvio.","Restrições reduzem o que o usuário precisa aprender e o erro que pode cometer.","Sem mapeamento natural, padronize e respeite convenções estabelecidas."]},

 {"slug":"ch06-funcoes-de-forca","sub":"CAPÍTULO 6: Funções de Força — Tornar Difícil o Erro Grave",
  "intro":"Quando um erro pode ser perigoso ou caro, restrições comuns não bastam: usa-se uma função de força — uma restrição forte que impede a ação seguinte até o passo certo, ou trava o usuário fora de uma ação perigosa.",
  "cards":[
      {"ic":"sword","t":"As Travas de Força","emph":"Travas","b":"As funções de força não educam, elas bloqueiam. Elas paralisam a catástrofe, barrando movimentos em zonas críticas, forçando sequências exatas ou impedindo abandono fatal. <strong>Quando a consequência da falha é o fim da linha, não dependa do bom senso, exija a obediência cega.</strong>","tip":"<strong>Modelo mental:</strong> se o erro resulta em hemorragia de dados ou ferimentos físicos graves, construa muros de ferro e não avisos gentis."},
      {"ic":"constellation","t":"A Impossibilidade do Erro","emph":"Impossibilidade","b":"O princípio japonês do poka-yoke crava: projetar contra o deslize humano não é um alerta de cor, mas sim um alicerce físico intransponível. De um pino desencontrado a sensores de contagem, <strong>os mecanismos matam tribos inteiras de acidentes porque simplesmente destroem a chance de errar.</strong>","tip":"<strong>Prática:</strong> em sistemas que custam caro, esforce-se em moldar gabaritos e formatos únicos que não aceitam encaixes espúrios."},
      {"ic":"bubble","t":"Placas Verdes Não Blindam Desastres","emph":"Blindam","b":"Delegar a proteção de operações letais a caixas de diálogo histéricas e adesivos berrantes é transferir o fardo da sua preguiça de engenheiro. Avisos viram parte da paisagem invisível quando a rotina e o estresse corroem a atenção. <strong>Para erros irreparáveis, excomungue os papéis e erga escudos mecânicos.</strong>","tip":"<strong>Armadilha:</strong> o excesso irracional de travas acaba irritando a tripulação, que as desativa, derrubando toda a barreira.","warn":True},
    ],
  "lessons_title":"Lições-Chave: Funções de Força",
  "lessons":["Para erros graves, não avise: torne o erro impossível com uma função de força.","Interlock (ordem), lock-in (permanência), lock-out (zona proibida) — escolha pelo risco.","Poka-yoke: o melhor controle de erro é a impossibilidade física de errar."]},

 {"slug":"ch07-erro-humano-mau-design","sub":"CAPÍTULO 7: Erro Humano? Não, Mau Design",
  "intro":"A maioria dos chamados 'erros humanos' são erros de design: o sistema permitiu, induziu ou não preveniu o engano. Há dois tipos fundamentais de erro — deslizes e enganos — e cada um pede um remédio de design diferente.",
  "cards":[
      {"ic":"pivot","t":"Deslizar Não É Enganar","emph":"Deslizar","b":"Um deslize ocorre na sonolência dos atos automáticos; você mira no branco, mas aperta o botão vizinho, vermelho. O engano, todavia, é uma tragédia tática na raiz; o plano já era letal antes da ação começar. <strong>Diagnosticar a dor exata é a única maneira de dosar o antídoto que resolve a crise.</strong>","tip":"<strong>Como aplicar:</strong> pergunte se o fim pretendido estava correto e a execução tremeu (deslize), ou se a mira já estava entortada desde o princípio (engano)."},
      {"ic":"target","t":"Antídotos Precisos","emph":"Antídotos","b":"Deslizes imploram por atalhos de defesa, feedbacks ruidosos e fáceis estornos; exigem a malha macia de retenção de falhas leves. Enganos, pelo oposto, exigem uma revolução informacional urgente. <strong>Tratar lapsos esporádicos com cartilhas filosóficas pesadas só paralisa os sistemas sem tocar na chaga.</strong>","tip":"<strong>Modelo mental:</strong> defenda a rotina com o Undo (Desfazer), mas reformule a alma do plano conceitual quando houver enganos."},
      {"ic":"mask","t":"A Falha de Modo Escondida","emph":"Falha de Modo","b":"Os lapsos mais obscuros nascem dos \"modos\" fantasmas de uma interface impenetrável. A tela exibe um painel normal, mas uma tecla oculta o reprogramou em background. Onde está o defeito? Não foi quem pilotou, <strong>foi o sistema cego que pavimentou o caminho do erro escondendo o estado verdadeiro da máquina.</strong>","tip":"<strong>Sinal de alerta:</strong> crucificar o erro alheio e engavetar o caso sela a promessa inabalável de que o desastre se repetirá pontualmente."},
    ],
  "lessons_title":"Lições-Chave: Erro Humano",
  "lessons":["Classifique o erro: deslize (objetivo certo, ação errada) ou engano (objetivo errado).","Deslizes pedem feedback e funções de força; enganos pedem melhor modelo conceitual.","Não culpe o usuário: pergunte por que o sistema permitiu o erro e corrija o design."]},

 {"slug":"ch08-design-a-prova-de-erro","sub":"CAPÍTULO 8: Design à Prova de Erro",
  "intro":"Já que pessoas vão errar, o design deve assumir o erro e trabalhar com ele: dificultar o erro grave, facilitar a detecção e tornar a recuperação simples. Errar deve ser barato e reversível.",
  "cards":[
      {"ic":"steps","t":"A Muralha de Quatro Níveis","emph":"Muralha","b":"As defesas formam um paredão robusto. Primeiro, tente barrar com restrições; não funcionou? Então amplie a visibilidade e jorre luz sobre a falha. Terceiro, garanta ferramentas de retorno imediatas (undo barato). E por fim, no último e mais dramático estaleiro, reserve a chave pesada da confirmação solene.","tip":"<strong>Como aplicar:</strong> faça o custo do erro ordinário tender a zero; feche a guarda pesada apenas nos penhascos irreversíveis."},
      {"ic":"spark","t":"O Feitiço do Desfazer","emph":"Desfazer","b":"O pop-up amarelado com \"Tem Certeza?\" é o maior mentiroso da indústria — usuários no piloto automático o pulverizam sem ler. A salvação elegante repousa na maciez do 'Desfazer' discreto na lixeira oculta. <strong>Dê à multidão a liberdade relaxante de tropeçar e apagar o rastro sem o chicote da burocracia.</strong>","tip":"<strong>Regra:</strong> não obrigue a assinatura de termos para jogar coisas no lixo. Apenas ofereça uma cordinha de resgate pelos próximos 30 dias."},
      {"ic":"bubble","t":"O Erro Deve Ser Um Professor","emph":"Professor","b":"Se a mensagem exibe uma cifra diabólica do Windows sem oferecer uma bússola de saída, você não projetou uma ajuda; você vomitou arrogância. <strong>Mensagens brilhantes explicam o desvio com empatia cristalina e oferecem, em seguida, o botão luminoso que repara e recomeça o jogo.</strong>","tip":"<strong>Armadilha:</strong> jargão técnico em alertas esconde falhas de usabilidade e destrói o resquício final de confiança."},
    ],
  "lessons_title":"Lições-Chave: À Prova de Erro",
  "lessons":["Assuma que erros vão acontecer: previna o grave, torne tudo visível e reversível.","Reserve confirmações pesadas para o irreversível; para o resto, ofereça desfazer.","Mensagens de erro devem explicar e ajudar a corrigir, nunca apenas acusar."]},

 {"slug":"ch09-design-centrado-no-humano","sub":"CAPÍTULO 9: Design Centrado no Humano e Design Thinking",
  "intro":"O bom design começa resolvendo o problema certo e parte das necessidades reais das pessoas. O Design Centrado no Humano (HCD) é um processo iterativo de observar, idear, prototipar e testar, repetidamente.",
  "cards":[
      {"ic":"leaf","t":"Centrado na Verdade Humana","emph":"Verdade Humana","b":"Pela força magnética do design moderno, você vira o mestre da gravidade da usabilidade, submetendo engrenagens cruas às demandas caóticas do pulso biológico. O ritual sagrado roda incessantemente pelas fases de investigar, idealizar, rascunhar protótipos de papel e atirá-los contra o teste das trincheiras.","tip":"<strong>Prática:</strong> nunca adote o protótipo como obra acabada; ele é a isca barata jogada para aprender o que não construir."},
      {"ic":"mountain","t":"A Mágica do Duplo Diamante","emph":"Duplo Diamante","b":"Antes de cravar unhas no projeto, mergulhe numa profunda caverna divergente para achar a doença real da máquina; depois, corte o tecido inútil e defina. Só então mergulhe no oceano de curas e reduza-as ao extrato que resolve tudo. <strong>Construir soluções esplêndidas para dores equivocadas é o pior fracasso.</strong>","tip":"<strong>Modelo mental:</strong> pare de curar a caspa antes de questionar por que não investigamos as artérias em entupimento veloz."},
      {"ic":"lens","t":"Esqueça os Questionários, Observe","emph":"Observe","b":"Os números e entrevistas contam uma história açucarada de intenções divinas. Os olhos silenciosos cravados nas rotinas expõem as chagas de uso oculto que as bocas jamais ousam traduzir na sala espelhada. <strong>Em caso de divergência estrondosa, esmague a fala do usuário e creia irrestritamente no suor e nos dedos dele.</strong>","tip":"<strong>Sinal de alerta:</strong> preencher os painéis com featuritis para tratar chagas invisíveis de planilhas resulta numa febre fatal da arquitetura geral."},
    ],
  "lessons_title":"Lições-Chave: HCD",
  "lessons":["Resolva o problema certo antes de buscar a solução certa (Duplo Diamante).","HCD é iterativo: observar → idear → prototipar → testar, repetidamente.","Observe o comportamento real das pessoas; não confie só no que elas dizem."]},

 {"slug":"ch10-design-no-mundo-dos-negocios","sub":"CAPÍTULO 10: Design no Mundo dos Negócios",
  "intro":"Na prática, o design ideal colide com prazo, custo, concorrência e política interna. Entender essas forças — e como as tecnologias evoluem e se difundem — separa o bom design teórico do produto que realmente chega às pessoas.",
  "cards":[
      {"ic":"scale","t":"O Campo Minado das Negociações","emph":"Campo Minado","b":"Uma tela sublime é chumbada pelo trator infernal de orçamentos atrasados, batalhões de marketing estridente e as urgências vulgares da prateleira. O design real, distante da perfeição poética intocada, <strong>reside na coragem de fazer alianças políticas sem sacrificar a alma primária da ideia que resolveu o drama.</strong>","tip":"<strong>Modelo mental:</strong> trate restrições brutais do comércio não como muralhas, mas sim como o molde criativo da forma definitiva."},
      {"ic":"spiral","t":"O Câncer da Featuritis","emph":"Featuritis","b":"Uma atualização atrás da outra se enxerta de funções periféricas, brilhantes na prateleira da loja, mas letais nas veias fluídas do manuseio diário da base de clientes engajados. <strong>Inchar os menus é inflar uma epidemia de esgotamento. Cada pequeno estilhaço de brilho a mais no pacote dilacera a clareza primordial de tudo.</strong>","tip":"<strong>Cuidado:</strong> recusar pedidos fúteis e dizer os temíveis \"nãos\" à chefia é onde você defende o valor monumental e limpo da solução."},
      {"ic":"clock","t":"Inovação Incremental e os Legados","emph":"Incremental","b":"Pequenas lixas sucessivas tornam diamantes suportáveis à maioria avassaladora; porém a revolução radical exige a brutalidade da espera silenciosa das adoções custosas de comportamento íntimo. <strong>Nós mantemos teclados absurdos e botões ilógicos em carros simplesmente pela coordenação enraizada das massas, que não sabem largar um passado conhecido e confortável.</strong>","tip":"<strong>Regra:</strong> construa os tijolos seguros das pequenas revoluções cotidianas, e deixe o abalo sísmico na categoria de investimento incerto lá na frente."},
    ],
  "lessons_title":"Lições-Chave: O Mundo dos Negócios",
  "lessons":["Bom design é negociação com prazo, custo, marketing e concorrência.","Resista à featuritis: cada função extra cobra um preço em usabilidade.","Espere inovação majoritariamente incremental; trate a radical como aposta de longo prazo."]},
]
