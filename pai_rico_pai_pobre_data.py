# -*- coding: utf-8 -*-
"""Conteúdo (pt-BR) das páginas da biblioteca para 'Pai Rico, Pai Pobre' (Robert T. Kiyosaki).
Frameworks: dois pais, os ricos não trabalham por dinheiro (medo/ganância, corrida dos ratos),
ativo vs. passivo (regra nº1, fluxo de caixa), cuide do seu negócio (coluna de ativos),
impostos e corporações, inventar dinheiro (inteligência financeira/risco calculado),
trabalhe para aprender, os 5 obstáculos, pague-se primeiro, como começar.
Base: síntese dos frameworks amplamente documentados — não reproduz o texto."""

BOOK = {
 "title": "Pai Rico, Pai Pobre",
 "author": "Robert T. Kiyosaki",
 "header_light": "PAI RICO,",
 "header_bold": "PAI POBRE",
 "subtitle": "VISÃO GERAL · O QUE OS RICOS ENSINAM AOS FILHOS",
 "intro": "Dois homens criaram Kiyosaki, e cada um lhe deu um conselho. O Pai Pobre — professor de PhD — dizia 'estude para arranjar um bom emprego'. O Pai Rico — que largou a escola na 8ª série e ficou milionário — dizia 'estude para que o dinheiro trabalhe para você'. Os dois ganhavam bem; só um morreu rico. A escola te treina para ser o melhor funcionário possível e nunca te conta o segredo mais simples do jogo: <em>os ricos não trabalham por dinheiro — eles compram ativos, e os ativos é que trabalham</em>.",
 "description": "O livro de finanças mais vendido da história, e o que mais irrita quem ama diploma. Kiyosaki desmonta a promessa da escola — boas notas, bom emprego, segurança — e a chama de armadilha: a corrida dos ratos, em que cada aumento de salário só compra uma gaiola mais cara. Contra isso, uma única regra que dá nome ao jogo: ativo põe dinheiro no seu bolso, passivo tira. Dos dois pais à coluna de ativos, das corporações que driblam o imposto ao pague-se primeiro, é um manual para parar de trabalhar por dinheiro e fazê-lo trabalhar por você.",
 "hook": "Você trabalha por dinheiro a vida toda. Os ricos fazem o contrário.",
 "story_promise": "ATIVO VS. PASSIVO: SAIA DA CORRIDA",
 "story_lessons": [
   "Ativo põe dinheiro no bolso. Passivo tira. Só isso.",
   "A escola te treina pra ser o melhor funcionário.",
   "Pague-se primeiro — antes de pagar qualquer conta.",
 ],
 "tags": ["Finanças", "Educação Financeira", "Mentalidade"],
 "progress": "10 Capítulos",
 "cover": "assets/pai-rico-pai-pobre-cover.png",
 "overview_cards": [
   {"ic":"scale","t":"Ativo vs. Passivo — a Regra nº1","b":"Toda a riqueza cabe numa frase de criança: <strong>ativo põe dinheiro no seu bolso; passivo tira</strong>. Os ricos passam a vida comprando ativos; a classe média compra passivos convencida de que são ativos — e por isso corre a vida inteira sem sair do lugar.","tip":"<strong>Como aplicar:</strong> antes de assinar qualquer cheque, pergunte 'isto vai me trazer dinheiro todo mês, ou me tirar?'.","wide":True},
   {"ic":"steps","t":"Faça o Dinheiro Trabalhar por Você","b":"O pobre e a classe média <strong>trabalham por dinheiro</strong> a vida inteira; o rico aprende cedo a fazer o <strong>dinheiro trabalhar por ele</strong>. O segredo não é ganhar mais — é montar uma coluna de ativos que, um dia, paga as contas no seu lugar enquanto você dorme.","tip":"<strong>Regra:</strong> cada aumento vai para comprar ativos, não para subir o padrão de vida. Padrão de vida é passivo disfarçado de recompensa."},
   {"ic":"key","t":"Pague-se Primeiro","b":"Quase todo mundo paga as contas, os credores, o governo — e investe o que sobra (quase nunca sobra). Inverta: <strong>separe para os ativos antes de qualquer boleto</strong>. A pressão de ainda dever não te afunda; vira o combustível que te força a gerar mais renda.","tip":"<strong>Modelo mental:</strong> a primeira conta do mês tem o seu nome. Pagar-se por último é o hábito que mantém a pessoa pobre."},
 ],
}

# Infografico de Instagram (Diretor de Design) — arquetipo COMPARA (gerar_infografico.py)
COMPARA = {
 "kicker": "PAI RICO, PAI POBRE · KIYOSAKI",
 "title": 'Pai <span class="hi">pobre</span> × pai <span class="hi">rico</span>',
 "left": {
   "ic": "spiral", "tag": "Pai pobre", "label": "Trabalha por dinheiro",
   "items": [
     'Diz <b>"não posso pagar"</b> — a frase que fecha a mente',
     "Compra <b>passivos</b> achando que são ativos (tiram do bolso)",
     "Sobe o padrão a cada aumento: a <b>corrida dos ratos</b>",
     "Ganha → é taxado → gasta o que <b>sobra</b>",
   ],
 },
 "right": {
   "ic": "mountain", "tag": "Pai rico", "label": "Faz o dinheiro trabalhar",
   "items": [
     'Pergunta <b>"como posso pagar?"</b> — ativa a solução',
     "Compra <b>ativos</b> que põem dinheiro no bolso todo mês",
     "<b>Paga-se primeiro</b>: investe antes de pagar contas",
     "Trabalha para <b>aprender</b>, não pelo salário",
   ],
 },
 "verdict_ic": "scale",
 "verdict": 'A Regra nº1: antes de comprar, pergunte <b>"isto traz ou leva '
            'dinheiro?"</b>. Só é ativo o que gera fluxo de caixa entrante.',
}

CHAPTERS = [
 {"slug":"ch01-dois-pais","sub":"CAPÍTULO 1: A Parábola dos Dois Pais",
  "intro":"Duas vozes disputaram a cabeça do autor menino, e elas se contradiziam em tudo. O Pai Pobre, professor, dizia 'o amor ao dinheiro é a raiz de todo mal'; o Pai Rico respondia 'a falta de dinheiro é que é a raiz de todo mal'. Um valorizava o diploma e o emprego seguro; o outro, ativos e fluxo de caixa. A primeira lição do livro é desconfortável: nota alta na escola não compra nota alta na vida — inteligência acadêmica e inteligência financeira são duas matérias diferentes, e só uma é cobrada na prova final.",
  "cards":[
      {"ic":"fork","t":"Os Dois Pais","emph":"Dois Pais","b":"Dois homens, dois mapas do mundo. O Pai Pobre repetia 'não posso pagar' e morria de medo da falência; o Pai Rico largou a escola na 8ª série e foi <strong>aprender a fazer o dinheiro trabalhar para ele</strong>. Os dois trabalhavam duro — mas trabalho duro num mapa errado só leva você mais rápido ao lugar errado.","tip":"<strong>Prática:</strong> repare em qual das duas vozes fala na sua cabeça quando aparece uma oportunidade. A escolha do mapa decide o destino."},
      {"ic":"lens","t":"Acadêmico ≠ Financeiro","emph":"Acadêmico ≠ Financeiro","b":"O sistema te promete que boas notas garantem uma vida garantida — e é aí que mente. <strong>Existe gente diplomada e quebrada, e gente sem diploma e milionária</strong>: a diferença não está no boletim, está em saber ler um demonstrativo de fluxo de caixa. A escola forma excelentes funcionários e péssimos donos.","tip":"<strong>Cuidado:</strong> ninguém te ensina dinheiro na escola justamente porque ela foi desenhada para formar quem trabalha por dinheiro, não quem o comanda.","warn":True},
      {"ic":"bulb","t":"\"Como Posso Pagar?\"","emph":"Como Posso Pagar?","b":"'Não posso pagar' é uma frase que fecha a mente: o cérebro ouve, concorda e desliga. Trocar por 'como eu posso pagar isto?' faz o oposto — <strong>obriga a cabeça a procurar uma saída em vez de aceitar a derrota</strong>. Uma é a afirmação do pobre; a outra, o exercício mental do rico.","tip":"<strong>Modelo mental:</strong> a primeira frase é uma porta trancada; a segunda é uma pergunta que sua mente não consegue deixar sem resposta."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 1",
  "lessons":["Examine de quem você herdou as suas crenças sobre dinheiro — e se essa pessoa é, de fato, rica.","Troque 'não posso pagar' por 'como posso pagar?' e force o cérebro a trabalhar.","Diploma e salário alto não bastam: o que decide a vida financeira é a inteligência financeira."]},

 {"slug":"ch02-nao-trabalhar-por-dinheiro","sub":"CAPÍTULO 2 (Lição 1): Os Ricos Não Trabalham por Dinheiro",
  "intro":"A primeira lição que o Pai Rico ensinou foi a mais difícil de engolir: os ricos não trabalham por dinheiro. O pobre e a classe média trabalham por dinheiro; o rico trabalha para aprender, e deixa o dinheiro trabalhar por ele. O que prende a maioria na roda não é a falta de salário — são duas emoções gêmeas, medo e desejo, que empurram para o emprego e depois gastam o salário antes mesmo de ele esfriar na conta.",
  "cards":[
      {"ic":"spiral","t":"A Corrida dos Ratos","emph":"Corrida dos Ratos","b":"Acordar, trabalhar, pagar conta, repetir: essa é a roda. A armadilha é que ela parece progresso — <strong>cada aumento de salário vem acompanhado de um carro maior, uma casa maior, uma conta maior</strong>, e a renda sobe junto com as despesas sem nunca abrir distância. Você corre cada vez mais rápido e continua exatamente no mesmo lugar.","tip":"<strong>Sinal de alerta:</strong> se a sua reação a um aumento é trocar de carro ou de bairro, você não saiu da corrida — só pôs a roda para girar mais depressa."},
      {"ic":"wave","t":"Medo e Ganância","emph":"Medo e Ganância","b":"São os dois motores escondidos por trás de quase toda decisão de dinheiro. O medo de não ter empurra a pessoa para o trabalho; o desejo do que o dinheiro compra faz ela torrar tudo no fim do mês. <strong>Acreditando que está sendo racional, ela na verdade obedece à emoção</strong> — e quem obedece à emoção é dirigido por quem entende dela.","tip":"<strong>Como aplicar:</strong> não tente eliminar o medo e o desejo (não dá). Aprenda a vê-los agindo e a decidir com a cabeça fria, sem pânico de perder nem afobação de ostentar."},
      {"ic":"target","t":"Trabalhe para Aprender","emph":"Aprender","b":"A maioria entra num emprego perguntando 'quanto paga?'. O futuro rico entra perguntando 'o que eu vou aprender aqui?'. <strong>O salário acaba no fim do mês; a habilidade que você decodificou no negócio fica para a vida toda</strong> — e é ela, não o contracheque, que constrói patrimônio.","tip":"<strong>Regra de ouro:</strong> não deixe o medo te paralisar diante de um trabalho que paga pouco mas ensina muito. Conhecimento composto rende mais que juros."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 2",
  "lessons":["O pobre e a classe média trabalham por dinheiro; o rico trabalha para aprender e faz o dinheiro trabalhar por ele.","Medo e desejo sustentam a corrida dos ratos — reconheça a emoção antes de decidir.","Mais salário sem mudar de mentalidade não liberta: só acelera a corrida."]},

 {"slug":"ch03-ativo-passivo","sub":"CAPÍTULO 3 (Lição 2): Alfabetização Financeira — Ativo vs. Passivo",
  "intro":"Se houvesse uma única regra para ficar rico, seria esta — e é tão simples que dá raiva: conheça a diferença entre ativo e passivo, e gaste a vida comprando ativos. Kiyosaki define de propósito com palavras de criança, porque é onde quase todo adulto se perde. A diferença entre o rico e a classe média não está em quanto ganham, mas em onde o dinheiro vai parar depois que entra.",
  "cards":[
      {"ic":"scale","t":"Ativo vs. Passivo (a Regra nº1)","emph":"Ativo vs. Passivo","b":"Esqueça as definições do contador. A do Pai Rico cabe num cartão: <strong>ativo é o que põe dinheiro no seu bolso; passivo é o que tira</strong>. Não importa o nome bonito que deram à coisa nem o que o vendedor jura — o que decide é a direção em que o dinheiro corre depois que você compra.","tip":"<strong>Como aplicar:</strong> o luxo que só dá despesa não é 'um pequeno investimento'. É um passivo, por mais charmoso que seja o seu nome."},
      {"ic":"steps","t":"O Padrão de Fluxo de Caixa","emph":"Fluxo de Caixa","b":"O pobre gasta tudo o que entra. A classe média compra passivos jurando que são ativos — a casa maior, o carro do ano, a TV nova. O rico faz outra coisa: <strong>usa a renda para comprar ativos, e deixa os ativos pagarem os passivos</strong>. Três rendas iguais, três destinos opostos — tudo decidido pelo caminho que o dinheiro toma.","tip":"<strong>Modelo mental:</strong> pare de olhar o preço da etiqueta. Aprenda a desenhar para onde o dinheiro vai depois da compra — esse é o mapa que importa."},
      {"ic":"gap","t":"A Casa Não É um Ativo","emph":"Casa Não É um Ativo","b":"Aqui Kiyosaki comete a heresia que o tornou famoso e odiado: a sua casa própria não é um ativo. <strong>Ela tira dinheiro do seu bolso todo mês — prestação, IPTU, condomínio, manutenção</strong> —, logo, pela regra nº1, é um passivo. Pode ser o passivo dos seus sonhos; mas confundi-lo com investimento é o erro nº1 da classe média.","tip":"<strong>Sinal de alerta:</strong> jogar toda a sua poupança na entrada de uma casa grande pode adiar por décadas o dia em que você começa a comprar ativos de verdade.","warn":True},
    ],
  "lessons_title":"Lições-Chave do Capítulo 3",
  "lessons":["Ativo põe dinheiro no bolso; passivo tira — toda a riqueza começa em saber separar os dois.","O rico compra ativos; a classe média compra passivos achando que são ativos.","Para Kiyosaki, a própria casa própria é um passivo, não um ativo — tese deliberadamente provocadora."]},

 {"slug":"ch04-cuide-do-seu-negocio","sub":"CAPÍTULO 4 (Lição 3): Cuide do Seu Próprio Negócio",
  "intro":"Há uma diferença entre a sua profissão e o seu negócio, e quase ninguém percebe. A sua profissão é o emprego que paga as contas — mas esse emprego é o negócio do seu patrão, não o seu. O seu negócio é a sua coluna de ativos. Kiyosaki não manda largar o trabalho: manda manter o emprego e, com a renda dele, começar a comprar ativos de verdade, em vez de gastar a vida fazendo o sonho de outra pessoa crescer.",
  "cards":[
      {"ic":"layers","t":"Emprego ≠ Negócio","emph":"Emprego ≠ Negócio","b":"Quando você trabalha por salário, você está cuidando do negócio do seu patrão — fazendo a empresa <strong>dele</strong> valer mais. A virada é mental: continue no emprego, mas trate-o como a fonte de capital para construir <strong>a sua própria coluna de ativos do lado de fora</strong>. Funcionário fiel constrói patrimônio alheio; é preciso decidir também construir o seu.","tip":"<strong>Como aplicar:</strong> o emprego paga as contas de hoje; o que você faz com a sobra decide se haverá liberdade amanhã."},
      {"ic":"leaf","t":"Construa a Coluna de Ativos","emph":"Coluna de Ativos","b":"Ativos de verdade são poucos e conhecidos: negócios que rodam sem você, ações, imóveis que geram aluguel, títulos, royalties. Eles trabalham sem reclamar, sem dormir e sem pedir aumento. <strong>Comece pequeno e mantenha os passivos baixos</strong> — uma coluna de ativos cresce por reinvestimento, não por mágica.","tip":"<strong>Prática:</strong> cada real que deixa de virar bobagem e vira ativo é uma semente que, plantada cedo, paga as suas despesas no futuro."},
      {"ic":"sword","t":"Luxos por Último","emph":"Luxos por Último","b":"O pobre compra o brinquedo a crédito; a classe média faz o mesmo e chama de 'eu mereço'. O rico inverte a ordem: <strong>primeiro constrói o ativo, e só compra o luxo com a renda que esse ativo gera</strong>. O carro do ano não é proibido — proibido é pagá-lo com o salário em vez de com o que os seus ativos produzem.","tip":"<strong>Modelo mental:</strong> deixe o seu dinheiro comprar primeiro a galinha; o ovo do luxo vem depois, pago pela galinha, não por você."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 4",
  "lessons":["Distinga a sua profissão (o negócio do patrão) do seu negócio (a sua coluna de ativos).","Use a renda do emprego para comprar ativos e mantenha os passivos baixos.","Compre luxos com a renda dos ativos, não com o salário — primeiro a galinha, depois o ovo."]},

 {"slug":"ch05-impostos-corporacoes","sub":"CAPÍTULO 5 (Lição 4): Impostos & o Poder das Corporações",
  "intro":"Esta é a lição que mais incomoda: os ricos pagam, proporcionalmente, menos imposto que a classe média — e fazem isso dentro da lei. A arma é o conhecimento. A corporação é um escudo legal que vira de cabeça para baixo a ordem do dinheiro: o assalariado ganha, é taxado e gasta o que sobra; a corporação ganha, gasta as despesas e só então é taxada sobre o que restou. A diferença não é trapaça — é saber ler o livro de regras que todos têm acesso e quase ninguém estuda.",
  "cards":[
      {"ic":"layers","t":"A História dos Impostos","emph":"História dos Impostos","b":"O imposto nasceu como um Robin Hood — cobrar dos ricos para dar aos pobres. Mas o apetite do governo cresceu, e a conta acabou caindo justamente sobre quem aplaudiu: a classe média assalariada. <strong>O sistema tributa com mais força quem ganha salário e dá mais brechas a quem opera por corporação</strong> — e isso não é segredo, está na lei.","tip":"<strong>Sinal de alerta:</strong> quem confia que 'bater ponto' garante segurança é exatamente quem mais paga e menos reclama."},
      {"ic":"scale","t":"Ganhar, Gastar, Ser Taxado","emph":"Ganhar–Gastar–Taxar","b":"Repare na ordem das palavras, porque ela vale fortunas. O assalariado <strong>ganha → é taxado → gasta o que sobra</strong>. A empresa do rico <strong>ganha → gasta nas despesas legítimas → é taxada só sobre o que restou</strong>. Mesma renda, sequência invertida, resultado completamente diferente no fim do ano.","tip":"<strong>Como aplicar:</strong> a estrutura jurídica (a pessoa jurídica) não é luxo de milionário — é a ferramenta que muda a ordem em que o imposto te alcança."},
      {"ic":"book","t":"Conhecimento, Não Trapaça","emph":"Conhecimento","b":"Usar corporações para pagar menos imposto não é sonegar — é jogar pelas regras que o próprio sistema escreveu. <strong>O rico contrata os melhores advogados e contadores e usa a lei a seu favor</strong>; a fraude amadora (esconder dinheiro, omitir renda) é o caminho do tolo, que ainda por cima acaba na cadeia.","tip":"<strong>Regra:</strong> as quatro inteligências que protegem o patrimônio são contabilidade, investimento, mercados e a lei. Não saber é o que custa caro."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 5",
  "lessons":["A corporação inverte a ordem: gasta antes de ser taxada; o indivíduo é taxado antes de gastar.","Domine as quatro inteligências financeiras: contabilidade, investimento, mercados e a lei.","O conhecimento (não a trapaça) é a vantagem legal dos ricos — usar a lei, não burlá-la."]},

 {"slug":"ch06-inventar-dinheiro","sub":"CAPÍTULO 6 (Lição 5): Os Ricos Inventam Dinheiro",
  "intro":"'Eu não tenho dinheiro para investir' é a desculpa preferida de quem nunca vai investir. Kiyosaki responde que a riqueza não vem do dinheiro inicial, e sim da inteligência financeira — a mente treinada inventa dinheiro onde os outros só veem falta dele. O que separa os dois grupos não é a conta bancária; é a coragem de assumir risco calculado em vez de fugir dele. O ativo mais poderoso que existe não está na carteira: é a sua própria cabeça.",
  "cards":[
      {"ic":"spark","t":"A Mente Inventa Dinheiro","emph":"Inventa Dinheiro","b":"Dinheiro não é um bolo de tamanho fixo que alguém esconde — é fabricado por quem enxerga uma oportunidade e a transforma em negócio. <strong>O verdadeiro obstáculo à riqueza não é o saldo zerado, é o medo paralisante diante do risco</strong>. Treine o olho, e o mundo se enche de oportunidades que os outros simplesmente não veem.","tip":"<strong>Prática:</strong> a oportunidade aparece para a mente preparada. Estude o jogo antes de precisar dele — não depois que ela passou."},
      {"ic":"mountain","t":"Risco Calculado","emph":"Risco Calculado","b":"Deixar tudo na poupança parece prudente, mas a longo prazo é a aposta mais arriscada de todas: a inflação corrói em silêncio. Risco calculado não é apostar às cegas — é <strong>entrar bem informado, com a matemática feita antes do salto</strong>. Aprender a perder pouco no começo é o que ensina a ganhar muito depois.","tip":"<strong>Modelo mental:</strong> quem só joga para não perder perde devagar, por fora, para a inflação. Evitar o risco é, ele próprio, o maior dos riscos."},
      {"ic":"pivot","t":"Os Dois Tipos de Investidor","emph":"Dois Tipos de Investidor","b":"Existe quem compra pacotes prontos na prateleira do banco — fundos, planos, produtos embalados por outros. E existe quem <strong>monta o próprio investimento do zero: encontra a oportunidade, junta as peças e cria valor que não existia</strong>. O primeiro aceita a margem que sobra; o segundo fica com a margem inteira.","tip":"<strong>Como aplicar:</strong> antes de comprar o que o gerente oferece, pergunte se você não poderia montar você mesmo o negócio que está por trás daquilo."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 6",
  "lessons":["É a inteligência financeira, não o capital inicial, que cria a riqueza.","Risco calculado (com estudo) vence a fuga do risco — evitá-lo é o maior risco de todos.","Seja o investidor que monta o próprio negócio, não só o que compra pacotes prontos."]},

 {"slug":"ch07-trabalhe-para-aprender","sub":"CAPÍTULO 7 (Lição 6): Trabalhe para Aprender, Não pelo Dinheiro",
  "intro":"O Pai Pobre dizia 'estude bastante para conseguir uma boa empresa onde trabalhar'. O Pai Rico dizia 'estude bastante para encontrar uma boa empresa para comprar'. A lição é escolher o trabalho pelo que ele te ensina, não pelo que ele te paga. Habilidades amplas — vendas, marketing, comunicação, gestão de pessoas — libertam; a especialização estreita prende você ao emprego, porque quanto mais especialista, mais difícil é viver fora daquela função.",
  "cards":[
      {"ic":"book","t":"Cada Emprego é uma Escola","emph":"Emprego é uma Escola","b":"Pare de ver o emprego só como fonte de salário e passe a vê-lo como escola paga. <strong>A pergunta certa não é 'quanto eu ganho aqui?', mas 'o que eu vou aprender aqui que vale para o resto da vida?'</strong>. Um trabalho que paga pouco mas ensina uma habilidade rara pode valer mais que um salário alto que te ensina nada.","tip":"<strong>Prática:</strong> aceite, de vez em quando, ganhar menos para aprender mais. Habilidade composta rende juros pela vida toda; salário acaba todo mês."},
      {"ic":"link","t":"Habilidades Amplas > Especialização","emph":"Habilidades Amplas","b":"Quem passa dez anos aperfeiçoando uma única função vira refém dela. O futuro dono precisa do oposto: <strong>saber um pouco de muita coisa — números, pessoas, vendas, sistemas</strong>. O especialista é caro e substituível; o generalista que entende como as partes se encaixam é quem senta na cadeira do dono.","tip":"<strong>Regra:</strong> não se afunde tanto numa especialidade que esqueça de aprender como o negócio inteiro funciona."},
      {"ic":"target","t":"Saber Vender é a Habilidade nº1","emph":"Saber Vender","b":"A melhor ideia do mundo morre na gaveta se ninguém souber vendê-la. Vender não é empurrar produto — <strong>é a arte de comunicar e convencer, e ela está por trás de toda renda própria</strong>. Kiyosaki é direto: há autores 'mais vendidos', não 'que escrevem melhor'. O que faz a diferença é quem sabe vender.","tip":"<strong>Sinal de alerta:</strong> quem se recusa a treinar comunicação e vendas entrega a vitória, de bandeja, para o medíocre carismático que treinou."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 7",
  "lessons":["Escolha o trabalho pelo que ele ensina, não só pelo que ele paga.","Priorize habilidades amplas: vendas, marketing, comunicação e gestão de pessoas.","Saber vender e comunicar é a competência mais decisiva para gerar renda própria."]},

 {"slug":"ch08-cinco-obstaculos","sub":"CAPÍTULO 8: Os 5 Obstáculos",
  "intro":"Você pode entender tudo de ativo e passivo e mesmo assim continuar pobre. Entre saber e fazer há cinco obstáculos, e todos moram dentro de você: medo, cinismo, preguiça, maus hábitos e arrogância. Não são falta de oportunidade nem de dinheiro — são as desculpas internas que travam quem já tem o mapa na mão. Reconhecer cada uma pelo nome é o primeiro passo para deixar de obedecer a ela.",
  "cards":[
      {"ic":"wave","t":"Medo & Cinismo","emph":"Medo & Cinismo","b":"Sentir medo de perder dinheiro é normal — todo rico já perdeu. O erro é deixar o medo decidir por você. Ao lado dele vem o cinismo: <strong>o 'e se der errado?' repetido até paralisar, muitas vezes na voz de quem nunca arriscou nada</strong>. Os palpites pessimistas dos outros são o som do próprio medo deles.","tip":"<strong>Como aplicar:</strong> ouça a crítica que tem base e ignore o pânico sem fundamento. Quem não tem pele em risco também não tem voto na sua decisão."},
      {"ic":"clock","t":"Preguiça & Maus Hábitos","emph":"Preguiça & Maus Hábitos","b":"A preguiça moderna se disfarça de ocupação: 'estou cansado demais, ocupado demais para pensar em dinheiro'. E o pior dos maus hábitos é financeiro — <strong>pagar todos os outros primeiro e a si mesmo por último</strong>, quando deveria ser o contrário. O antídoto, dizia o Pai Rico, é uma dose saudável de ganância: um desejo forte o bastante para vencer a inércia.","tip":"<strong>Regra:</strong> 'estou ocupado demais' costuma ser preguiça com roupa de gente séria. Reserve tempo para cuidar dos ativos antes que o dia acabe sem isso."},
      {"ic":"mask","t":"Arrogância (ego + ignorância)","emph":"Arrogância","b":"Arrogância é ego mais ignorância: achar que sabe o que não sabe e investir mesmo assim. <strong>Aquilo que você ignora sobre dinheiro é exatamente o que te faz perdê-lo</strong> — e o ego impede de admitir o buraco. Quem despreza o conselho de quem entende, achando-se esperto demais, costuma pagar caro pela lição.","tip":"<strong>Sinal de alerta:</strong> quando você se pegar pensando 'eu não preciso aprender isso', desconfie — é provavelmente o ponto exato onde está perdendo dinheiro.","warn":True},
    ],
  "lessons_title":"Lições-Chave do Capítulo 8",
  "lessons":["Os cinco obstáculos são internos: medo, cinismo, preguiça, maus hábitos e arrogância.","Não fuja do medo e da perda — gerencie-os e comece cedo, porque todo rico já perdeu.","Pague-se primeiro e tenha a humildade de admitir o que ainda não sabe."]},

 {"slug":"ch09-pague-se-primeiro","sub":"CAPÍTULO 9: Pague-se Primeiro & Hábitos",
  "intro":"Quase todo mundo paga primeiro o aluguel, o cartão, o governo — e investe o que sobrar (e nunca sobra). 'Pague-se primeiro' inverte a ordem: separe o dinheiro dos seus ativos antes de qualquer conta. Parece imprudente, e é justamente esse o truque — a pressão de ainda ter contas a pagar acende a criatividade e a energia para buscar mais renda, em vez de deixar a folga apagar o impulso. No fundo, é um exercício de autodisciplina, o mais difícil e o mais decisivo de todos os hábitos.",
  "cards":[
      {"ic":"key","t":"Pague-se Primeiro","emph":"Pague-se Primeiro","b":"Investir não é o que se faz com a sobra — é a primeira coisa que se faz com a renda. <strong>Quando o dinheiro entra, uma parte vai para os ativos antes de qualquer boleto</strong>. A maioria faz o contrário e por isso nunca investe: pagar-se por último é o hábito silencioso que mantém a pessoa na corrida dos ratos a vida inteira.","tip":"<strong>Prática:</strong> automatize o aporte para sair da conta no mesmo dia do salário. O que não passa pela sua mão não passa pela sua tentação."},
      {"ic":"spark","t":"A Pressão como Combustível","emph":"Pressão","b":"Tirar dinheiro dos ativos para cobrir uma conta é desistir do jogo. O Pai Rico fazia o oposto: <strong>deixava a pressão das contas pendentes bater, porque é o desconforto que obriga o cérebro a inventar uma nova fonte de renda</strong>. A folga relaxa; o aperto, bem usado, cria. A disciplina nasce da necessidade, não do conforto.","tip":"<strong>Modelo mental:</strong> não sacrifique o ativo para apagar o incêndio. Use o incêndio como motivo para ganhar mais — não como desculpa para gastar a poupança."},
      {"ic":"steps","t":"Autodisciplina","emph":"Autodisciplina","b":"De nada vale conhecer a regra nº1 se você não tiver a disciplina de cumpri-la todo mês. <strong>Controlar o próprio impulso de gastar é o que separa quem aplica o livro de quem só o lê e concorda</strong>. Sem domínio de si, alta renda só significa altas dívidas — a folha de pagamento maior costuma vir com a fatura maior.","tip":"<strong>Sinal de alerta:</strong> falhar em se pagar primeiro no dia 1 de cada mês não é culpa do mercado nem do salário. É falta de disciplina — e essa é a única que você controla."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 9",
  "lessons":["Invista primeiro, pague as contas depois — a primeira conta do mês tem o seu nome.","Use a pressão das contas pendentes para gerar mais renda, nunca para sacar dos ativos.","Autodisciplina é o hábito que separa quem aplica o livro de quem apenas concorda com ele."]},

 {"slug":"ch10-comecar","sub":"CAPÍTULO 10: Como Começar",
  "intro":"Saber tudo isso e não fazer nada é onde a maioria para. O capítulo final é o empurrão: gatilhos práticos para acender a inteligência financeira e dar o primeiro passo de verdade. A diferença entre quem terminou este livro e mudou de vida e quem só o achou interessante não é talento nem sorte — é a ação. Conhecimento sem ação é só entretenimento.",
  "cards":[
      {"ic":"mountain","t":"Uma Razão Maior que a Realidade","emph":"Razão Maior","b":"Antes de aprender o como, você precisa de um porquê forte o bastante para aguentar o tranco. <strong>Um motivo morno desiste na primeira dificuldade; um motivo profundo te tira da cama</strong>. Para Kiyosaki, o melhor combustível mistura o desejo de algo (liberdade, viajar) com o pavor de algo (depender dos outros na velhice, obedecer a um chefe a vida inteira).","tip":"<strong>Como aplicar:</strong> escreva, sem enfeite, a verdadeira razão pela qual você quer dinheiro. Sem esse porquê na parede, qualquer técnica cai na primeira semana."},
      {"ic":"constellation","t":"O Poder das Companhias","emph":"Companhias","b":"Cada real e cada hora que você gasta é um voto no futuro que está construindo. E você pensa na média de quem te cerca: <strong>fuja do círculo dos que só reclamam de dinheiro e aproxime-se de quem já joga o jogo</strong>. Escolha amigos pelo que eles sabem, não pelo tamanho da conta — e aprenda com quem ganha e com quem perde.","tip":"<strong>Modelo mental:</strong> o nível das conversas à sua volta puxa o seu próprio nível para cima ou para baixo. Escolha a mesa em que você se senta."},
      {"ic":"steps","t":"Comece Pequeno, mas Comece","emph":"Comece","b":"Ler mil livros e nunca aplicar é a forma mais sofisticada de não fazer nada. <strong>Comece com pouco, com um ativo real, e aprenda fazendo</strong> — o medo de verdade ensina o que nenhum curso ensina. Não espere ter muito dinheiro para começar; comece para um dia ter muito dinheiro.","tip":"<strong>Sinal de alerta:</strong> 'preciso estudar mais antes' costuma ser medo disfarçado de prudência. A teoria infinita é o esconderijo preferido de quem nunca dá o primeiro passo.","warn":True},
    ],
  "lessons_title":"Lições-Chave do Capítulo 10",
  "lessons":["Tenha um 'porquê' forte — é ele que sustenta a disciplina quando a motivação cai.","Cerque-se de quem já joga o jogo e invista primeiro na sua própria educação financeira.","Aja: comece pequeno, com um ativo real, em vez de acumular teoria para sempre."]},
]
