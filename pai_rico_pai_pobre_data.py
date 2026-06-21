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
 "intro": "Robert Kiyosaki cresceu entre dois pais: um instruído, professor e financeiramente conservador (o Pai Pobre), e o pai de um amigo, empreendedor que largou a escola mas dominava o jogo do dinheiro (o Pai Rico). Conselhos opostos, destinos opostos. A lição central: a escola ensina a trabalhar por dinheiro; os ricos aprendem a fazer o dinheiro trabalhar para eles — e isso começa por saber a diferença entre um ativo e um passivo.",
 "description": "O clássico da educação financeira de Robert Kiyosaki. Por que inteligência acadêmica não é inteligência financeira: a parábola dos dois pais, a regra nº1 (ativo vs. passivo e o fluxo de caixa), a corrida dos ratos movida por medo e ganância, construir a coluna de ativos, o poder das corporações e dos impostos, inventar dinheiro com risco calculado, trabalhar para aprender, pagar-se primeiro e vencer os 5 obstáculos à riqueza.",
 "tags": ["Finanças", "Educação Financeira", "Mentalidade"],
 "progress": "10 Capítulos",
 "cover": "assets/pai-rico-pai-pobre-cover.png",
 "overview_cards": [
   {"ic":"scale","t":"Ativo vs. Passivo — a Regra nº1","b":"A alfabetização financeira começa aqui: <strong>ativo põe dinheiro no seu bolso; passivo tira</strong>. Os ricos compram ativos; a classe média compra passivos achando que são ativos.","tip":"<strong>Como aplicar:</strong> antes de comprar, pergunte 'isto traz dinheiro todo mês ou leva?'.","wide":True},
   {"ic":"steps","t":"Faça o Dinheiro Trabalhar por Você","b":"Pobres e classe média <strong>trabalham por dinheiro</strong>; os ricos fazem o <strong>dinheiro trabalhar por eles</strong> — construindo uma coluna de ativos que, um dia, paga as despesas.","tip":"<strong>Regra:</strong> use a renda do trabalho para comprar ativos, não para subir o padrão de vida (passivos)."},
   {"ic":"key","t":"Pague-se Primeiro","b":"Antes de pagar contas, separe para <strong>investir em ativos</strong>. A pressão de ainda dever vira combustível para gerar mais renda — em vez de a folga matar o impulso.","tip":"<strong>Modelo mental:</strong> a primeira conta a pagar é você mesmo."},
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
  "intro":"Duas mentes opostas moldaram o autor: o Pai Pobre (instruído, valoriza emprego e diploma) e o Pai Rico (empreendedor, pensa em ativos). Inteligência acadêmica não é inteligência financeira — a escola não ensina dinheiro.",
  "cards":[
      {"ic":"fork","t":"Os Dois Pais","emph":"Dois Pais","b":"É a escolha entre jogar na segurança medíocre ou aprender o código do sistema. O Pai Pobre adora diplomas e tem pavor da falência; o Pai Rico largou o quadro negro para <strong>dobrar a espinha dorsal do dinheiro e forçá-lo a trabalhar sem folga</strong>. É o contraste letal entre ganhar salário e gerar riqueza.","tip":"<strong>Prática:</strong> audite sua mente agora. Você está operando com o software do medo do contracheque ou com o radar da oportunidade invisível?"},
      {"ic":"lens","t":"Acadêmico ≠ Financeiro","emph":"Acadêmico ≠ Financeiro","b":"O maior golpe do sistema educacional é convencer você de que um boletim com notas altas garante imunidade ao desastre na conta bancária. Ser uma estrela acadêmica com um salário inflado é inútil se a sua <strong>analfabetização financeira sangra cada centavo num passivo disfarçado</strong>.","tip":"<strong>Cuidado:</strong> pare de aceitar ordens financeiras de especialistas teóricos que nunca pisaram no lado ensanguentado da trincheira do mercado.","warn":True},
      {"ic":"bulb","t":"\"Como Posso Pagar?\"","emph":"Como Posso Pagar?","b":"O 'eu não posso comprar' é a droga que anestesia o cérebro; ele tranca as portas e permite que a mente durma. A virada violenta é forçar a engrenagem com 'como eu posso comprar isso?'. Essa simples engenharia verbal <strong>chicoteia a criatividade e obriga a mente a fabricar uma rota de fuga</strong>.","tip":"<strong>Modelo mental:</strong> a negação decreta a morte da imaginação. A pergunta joga oxigênio na fogueira da solução de problemas."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 1",
  "lessons":["Examine de quem vêm suas crenças sobre dinheiro — e se essa pessoa é rica.","Troque 'não posso pagar' por 'como posso pagar?'.","Diploma e renda não bastam; o que decide é a inteligência financeira."]},

 {"slug":"ch02-nao-trabalhar-por-dinheiro","sub":"CAPÍTULO 2 (Lição 1): Os Ricos Não Trabalham por Dinheiro",
  "intro":"Pobres e classe média trabalham por dinheiro; os ricos trabalham para aprender e fazem o dinheiro trabalhar para eles. Duas emoções — medo e ganância — movem a maioria e a prendem na corrida dos ratos.",
  "cards":[
      {"ic":"spiral","t":"A Corrida dos Ratos","emph":"Corrida dos Ratos","b":"O manicômio do contracheque, onde acordar, bater cartão e pagar boleto forma a roda do hamster perfeita. A piada cruel é que a cada promoção, você adquire uma gaiola mais cara; a receita salta e <strong>as despesas sangram exatamente na mesma proporção para sustentar o cenário</strong>.","tip":"<strong>Sinal de alerta:</strong> se você comemora um aumento trocando imediatamente de carro ou mudando de bairro, a roda de metal acabou de girar mais rápido."},
      {"ic":"wave","t":"Medo e Ganância","emph":"Medo e Ganância","b":"Os dois motores invisíveis que pilotam o cérebro das massas. O chicote frio do medo do aluguel empurra o sujeito para o escritório, e a ganância por brinquedos cintilantes rouba o dinheiro dele na sexta-feira. <strong>Você trabalha escravizado pela emoção pura</strong>, achando que está usando a lógica.","tip":"<strong>Como aplicar:</strong> corte a injeção dessas duas drogas. Avalie friamente onde colocar a nota de dinheiro, sem pânico de perder e sem fissura de ostentar."},
      {"ic":"target","t":"Trabalhe para Aprender","emph":"Aprender","b":"O rebanho entra na empresa de joelhos perguntando 'qual é a escala e o salário?'. O investidor de elite entra pelo mesmo saguão e mapeia: 'quais habilidades brutais eu posso roubar dessa operação?'. O medo não deve paralisá-lo, deve <strong>dar fome de comer as regras inteiras do jogo</strong>.","tip":"<strong>Regra de ouro:</strong> o dinheiro da carteira assinada acaba no mês que vem; a mecânica do negócio que você decodificou pagará a conta para o resto da vida."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 2",
  "lessons":["A maioria trabalha por dinheiro; os ricos trabalham para aprender.","Medo e ganância sustentam a corrida dos ratos — reconheça a emoção antes de agir.","Mais salário sem mudar de mentalidade só acelera o ciclo."]},

 {"slug":"ch03-ativo-passivo","sub":"CAPÍTULO 3 (Lição 2): Alfabetização Financeira — Ativo vs. Passivo",
  "intro":"A regra nº1 da riqueza: saber a diferença entre ativo e passivo, e comprar ativos. Os ricos compram ativos; a classe média compra passivos achando que são ativos. A diferença não está na renda, está no que se faz com ela.",
  "cards":[
      {"ic":"scale","t":"Ativo vs. Passivo (a Regra nº1)","emph":"Ativo vs. Passivo","b":"A guilhotina financeira: ativo injeta fluxo constante de sangue no seu caixa; passivo enfia a mão no seu bolso e leva o sangue embora. Não interessa o brilho ou o que o corretor sussurra; <strong>antes de assinar o cheque, exija saber de que lado da trincheira aquele objeto vai lutar</strong>.","tip":"<strong>Como aplicar:</strong> o luxo que não gera lucro não é 'meu pequeno investimento', é apenas um pedágio caro para o próprio ego."},
      {"ic":"steps","t":"O Padrão de Fluxo de Caixa","emph":"Fluxo de Caixa","b":"O pobre pega o contracheque e queima na vala da sobrevivência. A classe média comete suicídio lento comprando bugigangas caríssimas jurando que são patrimônio. A elite <strong>redireciona a mangueira da renda exclusivamente para os ativos</strong>, construindo um exército autônomo que caça dinheiro 24 horas.","tip":"<strong>Modelo mental:</strong> pare de ler etiquetas de preço. Aprenda a ler os vetores invisíveis do fluxo de caixa que cruzam o papel."},
      {"ic":"gap","t":"A Casa Não É um Ativo","emph":"Casa Não É um Ativo","b":"A heresia suprema de Kiyosaki que fuzila o dogma americano: a sua casa própria adorável chupa IPTU, arranca taxas de manutenção e devora juros de prestação. <strong>Se drena o fluxo do caixa em vez de enchê-lo, é um passivo de concreto armado</strong>, independentemente do que diga o seu avô.","tip":"<strong>Sinal de alerta:</strong> afundar 100% da sua munição na parede de tijolos do seu teto trava brutalmente a montagem do seu portfólio guerreiro.","warn":True},
    ],
  "lessons_title":"Lições-Chave do Capítulo 3",
  "lessons":["Ativo põe dinheiro no bolso; passivo tira — saiba qual é qual.","Os ricos compram ativos; a classe média compra passivos achando que são ativos.","Para o autor, a própria casa é um passivo, não um ativo."]},

 {"slug":"ch04-cuide-do-seu-negocio","sub":"CAPÍTULO 4 (Lição 3): Cuide do Seu Próprio Negócio",
  "intro":"Seu negócio não é o seu emprego — o emprego é o negócio do seu patrão. Seu negócio é a sua coluna de ativos. Mantenha o emprego, mas use tempo e dinheiro para construir e comprar ativos reais.",
  "cards":[
      {"ic":"layers","t":"Emprego ≠ Negócio","emph":"Emprego ≠ Negócio","b":"A sua rotina massacrante na corporação garante a picanha do seu patrão; isso é a sua profissão, não a sua mina de ouro. A jogada mestra é bater o ponto para garantir a gasolina do mês, mas <strong>dedicar a noite implacavelmente para erguer o castelo da sua própria coluna de ativos</strong>.","tip":"<strong>Como aplicar:</strong> o turno do dia paga a sua sobrevivência; o turno da madrugada empilha os ativos que vão comprar a sua alforria."},
      {"ic":"leaf","t":"Construa a Coluna de Ativos","emph":"Coluna de Ativos","b":"Empilhe soldados de papel que não dormem, não fazem greve e valorizam no escuro: ações explosivas, imóveis que sangram aluguel e royalties que pingam sem aviso. A lei é militar — inicie com um esquadrão minúsculo, e <strong>estrangule qualquer chance de um passivo inútil inflar no começo</strong>.","tip":"<strong>Prática:</strong> cada cédula poupada num vício banal é a semente pronta de um pequeno tanque de guerra que vai lutar pela sua fortuna."},
      {"ic":"sword","t":"Luxos por Último","emph":"Luxos por Último","b":"O pobre antecipa o brinquedo, torrando o crédito que não tem. A classe média finge ser rica comprando fumaça. Os titãs <strong>compram carros e joias exclusivamente com o sangue derramado pelo exército de ativos</strong>. O prêmio é o suco da vitória do sistema, e não o suor do próprio salário.","tip":"<strong>Modelo mental:</strong> o cordão de ouro não é proibido. Proibido é ser pago pelo salário; ele deve ser a sobra gorda do ativo que você construiu."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 4",
  "lessons":["Distinga sua profissão (negócio do patrão) do seu negócio (sua coluna de ativos).","Use a renda do emprego para comprar ativos; mantenha passivos baixos.","Compre luxos com a renda dos ativos, não com o salário."]},

 {"slug":"ch05-impostos-corporacoes","sub":"CAPÍTULO 5 (Lição 4): Impostos & o Poder das Corporações",
  "intro":"Os ricos usam o conhecimento para se proteger legalmente. A corporação é um escudo que inverte a ordem do imposto: o assalariado ganha, é taxado e gasta o que sobra; a corporação ganha, gasta e é taxada sobre o que sobra.",
  "cards":[
      {"ic":"layers","t":"A História dos Impostos","emph":"História dos Impostos","b":"O Robin Hood do estado cobrou imposto dos milionários com a promessa de dar aos pobres; mas a fome do leviatã acordou e logo engoliu a garganta da classe média que batia palmas. <strong>O estado pune quem produz salário e alivia o chicote de quem orquestra corporações blindadas</strong>.","tip":"<strong>Sinal de alerta:</strong> a moral da lenda é que a classe média pagará a conta do baile enquanto acreditar que bater ponto garante a segurança."},
      {"ic":"scale","t":"O Jogo da Classe Média vs. Rico","emph":"Classe Média vs. Rico","b":"A classe média trabalha, o governo suga a primeira fatia do bolo e ela tenta sobreviver com as migalhas finais. O rico vira a mesa: <strong>a corporação dele arrecada tudo, torra legalmente nas despesas operacionais pesadas e oferece ao governo apenas o que sobra</strong> no osso das tributações.","tip":"<strong>Como aplicar:</strong> a corporação e o CNPJ não são estruturas teóricas, são as escotilhas de sobrevivência na selva tributária. Use o escudo de aço."},
      {"ic":"book","t":"Conhecimento, Não Trapaça","emph":"Conhecimento","b":"O uso brutal da pessoa jurídica não é um assalto à mão armada; é usar a própria engenharia do livro de regras do sistema para levantar trincheiras. <strong>É a maestria jurídica que desvia o imposto legalmente, e não a burrice suicida de esconder dinheiro embaixo do colchão</strong>.","tip":"<strong>Regra:</strong> não caia na tentação da fraude amadora. Contrate a melhor inteligência tributária e vença usando exatamente a gramática deles."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 5",
  "lessons":["Corporação inverte a ordem: gasta antes de ser taxada; o indivíduo é taxado antes de gastar.","Domine as 4 inteligências: contabilidade, investimento, mercados e a lei.","Conhecimento (não trapaça) é a vantagem legal dos ricos."]},

 {"slug":"ch06-inventar-dinheiro","sub":"CAPÍTULO 6 (Lição 5): Os Ricos Inventam Dinheiro",
  "intro":"A riqueza nasce da inteligência financeira, não do dinheiro inicial. Quem entende o jogo cria oportunidades onde outros só veem risco — e assume risco calculado em vez de evitá-lo. O ativo mais poderoso é a mente treinada.",
  "cards":[
      {"ic":"spark","t":"Inteligência Financeira Inventa Dinheiro","emph":"Inventa Dinheiro","b":"O dinheiro não é um recurso finito escondido num cofre; ele é fabricado no vácuo pela mente treinada que conecta a solução ao problema alheio. <strong>A maior âncora da pobreza não é a conta zerada, é a covardia patológica diante do risco</strong> e a paralisia perante a página em branco da oportunidade.","tip":"<strong>Prática:</strong> treine o olho clínico. O mercado está cheio de fortunas ocultas esperando que a ignorância dos outros bata na genialidade da sua percepção."},
      {"ic":"mountain","t":"Risco Calculado","emph":"Risco Calculado","b":"Esconder o dinheiro na poupança com pavor da chuva é a aposta mais radioativa a longo prazo. Risco não é pular da ponte de olhos vendados; é a <strong>ciência fria de entrar na arena blindado com informações táticas</strong>. Aprender a apanhar logo no início é arrancar o dente do medo.","tip":"<strong>Modelo mental:</strong> quem joga sempre para não perder termina na lona esmagado pela inflação. O risco calculado é a única matemática da riqueza."},
      {"ic":"pivot","t":"Os Dois Tipos de Investidor","emph":"Dois Tipos de Investidor","b":"Existe a ovelha dócil que compra pacotes mastigados na prateleira do banco. E existe o predador alfa, que encontra o terreno destruído, arranja o cimento, agrupa as ferramentas e <strong>monta o esqueleto do próprio golias do zero, criando um valor que não existia</strong> no planeta ontem de manhã.","tip":"<strong>Como aplicar:</strong> recuse o menu degustação. Aprenda a montar o prato juntando as peças no mercado primário e engula as margens que os preguiçosos largam."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 6",
  "lessons":["A inteligência financeira, não o capital inicial, cria a riqueza.","Risco calculado (com estudo) vence a evitação do risco.","Seja o investidor que monta o próprio negócio, não só o que compra pacotes."]},

 {"slug":"ch07-trabalhe-para-aprender","sub":"CAPÍTULO 7 (Lição 6): Trabalhe para Aprender, Não pelo Dinheiro",
  "intro":"Escolha o trabalho pelo que você vai aprender, não pelo salário. Habilidades amplas — sobretudo vendas, marketing, comunicação e gestão — libertam; a especialização estreita prende ao emprego.",
  "cards":[
      {"ic":"book","t":"Cada Emprego é uma Escola","emph":"Emprego é uma Escola","b":"Um contracheque não deve ser a sua ração de sobrevivência, deve ser a bolsa que financia os seus estudos nas entranhas da corporação. Mergulhe no moedor de carne empresarial e <strong>trate cada rotina como um módulo letal para roubar o <em>know-how</em></strong> antes que o departamento demita você.","tip":"<strong>Prática:</strong> troque de setor voluntariamente. Trocar salário alto por um treinamento prático insano constrói o armamento que te blindará na guerra final."},
      {"ic":"link","t":"Habilidades Amplas > Especialização","emph":"Habilidades Amplas","b":"Ficar dez anos virando a mesma engrenagem cria a síndrome do macaco adestrado. Você precisa ser um lobo híbrido: entender da matemática dos lucros, do controle de pânico da equipe e da arte sutil do convencimento. <strong>O hiper-especialista treme no vento; o generalista faminto assume a cadeira do chefe</strong>.","tip":"<strong>Regra:</strong> não mergulhe tanto no poço de uma função que esqueça de ler o manual que pilota a fábrica inteira."},
      {"ic":"target","t":"Saber Vender é a Habilidade nº1","emph":"Saber Vender","b":"Um projeto absurdamente revolucionário sem uma voz capaz de empurrá-lo goela abaixo do investidor é apenas poesia murcha de gaveta. Vender não é pedir esmola, <strong>é o dom de dominar o ar ao redor e transferir a convicção do seu sangue para a cabeça da outra pessoa</strong>. O medo da rejeição é a guilhotina do sucesso.","tip":"<strong>Sinal de alerta:</strong> se você recusa treinar a sua oratória e a sua capacidade de venda, preparou a mesa perfeita para que um medíocre carismático leve a melhor."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 7",
  "lessons":["Escolha trabalhos pelo que ensinam, não só pelo que pagam.","Priorize habilidades amplas: vendas, marketing, comunicação e gestão.","Saber vender é a competência mais decisiva para gerar renda própria."]},

 {"slug":"ch08-cinco-obstaculos","sub":"CAPÍTULO 8: Os 5 Obstáculos",
  "intro":"Mesmo financeiramente alfabetizado, cinco coisas impedem a independência: medo, cinismo, preguiça, maus hábitos e arrogância. Reconhecer cada uma é o primeiro passo para superá-la.",
  "cards":[
      {"ic":"wave","t":"Medo & Cinismo","emph":"Medo & Cinismo","b":"O terror frio de assinar um cheque arriscado é natural, o crime é deixá-lo sequestrar o volante da ação. O cinismo agudo é a praga que faz os medrosos bancarem os <strong>profetas do apocalipse, caçando o fio de cabelo no omelete para justificar a paralisia do sofá</strong>. Trate o ruído deles como lixo.","tip":"<strong>Como aplicar:</strong> os 'amigos cautelosos' são o departamento de marketing do fracasso. Abafe os gritos de quem não tem pele em risco."},
      {"ic":"clock","t":"Preguiça & Maus Hábitos","emph":"Preguiça & Maus Hábitos","b":"A camuflagem perfeita da preguiça moderna é o culto da agenda entupida: trabalhar dezoito horas cavando o próprio buraco sem focar no pilar que sustenta o cofre. O pecado capital da rotina não é acordar tarde, é <strong>bancar o bom moço e liquidar o próprio aporte antes de sobrar algo no final do mês</strong>.","tip":"<strong>Regra:</strong> o conforto frito de uma rotina lotada impede você de estancar o sangramento invisível do seu caixa de ativos."},
      {"ic":"mask","t":"Arrogância (ego + ignorância)","emph":"Arrogância","b":"Usar o canudo de ouro e o ego gigantesco para disfarçar a completa indigência sobre relatórios contábeis. A fórmula é letal: <strong>o excesso de confiança apoiado sobre o nada resulta num meteoro rasgando a sua conta em pedaços</strong>. Quem acha que o mercado tem pena, amanhece pobre e orgulhoso no asfalto.","tip":"<strong>Sinal de alerta:</strong> fechar os ouvidos para um consultor e investir achando que o gênio é infalível é pedir para entregar o castelo ao inimigo.","warn":True},
    ],
  "lessons_title":"Lições-Chave do Capítulo 8",
  "lessons":["Os cinco freios são internos: medo, cinismo, preguiça, maus hábitos, arrogância.","Não evite o medo e a perda; gerencie-os e comece cedo.","Pague-se primeiro e admita o que não sabe."]},

 {"slug":"ch09-pague-se-primeiro","sub":"CAPÍTULO 9: Pague-se Primeiro & Hábitos",
  "intro":"Antes de pagar contas e credores, separe dinheiro para investir em ativos. A pressão de ainda dever gera a criatividade e a energia para buscar mais renda — em vez de a folga matar o impulso. É um hábito de autodisciplina, o mais decisivo de todos.",
  "cards":[
      {"ic":"key","t":"Pague-se Primeiro","emph":"Pague-se Primeiro","b":"Não trate o seu investimento como gorjeta da sobra. Ele é o primeiro abutre que voa na carcaça do salário antes de todo mundo; os bancos e boletos são a segunda divisão. <strong>Imponha a si mesmo o tributo inegociável na linha de frente</strong>, rasgando o sangue da prioridade para a sua milícia de papéis valorizados.","tip":"<strong>Prática:</strong> o aporte não se discute; ele cai direto e programado da conta base como um raio no dia em que o chefe aperta o botão do TED."},
      {"ic":"spark","t":"A Pressão como Combustível","emph":"Pressão","b":"Roubar dos próprios ativos para salvar o jantar cancela o jogo inteiro. Deixe o desespero do aluguel pendente bater no peito: é essa <strong>fome cortante e esse desconforto bruto que acionarão as manivelas de emergência do seu cérebro, obrigando-o a inventar um novo canal de dinheiro vivo</strong> na madrugada.","tip":"<strong>Modelo mental:</strong> use as dívidas para apertar o seu pescoço taticamente; a genialidade nunca acordou descansando num colchão quentinho."},
      {"ic":"steps","t":"Autodisciplina","emph":"Autodisciplina","b":"Sem o chicote interno batendo na própria espinha todo santo dia, o livro mais brilhante do mundo afunda no tédio. Dominar o ego fraco e domesticar o impulso infantil de queimar caixa são <strong>os fatores ditatoriais mais selvagens entre os vencedores implacáveis e o resto da sala ruidosa</strong>.","tip":"<strong>Sinal de alerta:</strong> falhar na blindagem pessoal no dia 1 de cada mês não anula o mercado, anula você."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 9",
  "lessons":["Invista primeiro, pague contas depois — a primeira conta é você.","Use a pressão de ter contas pendentes para gerar renda, não para sacar dos ativos.","Autodisciplina é o hábito que separa quem enriquece de quem não enriquece."]},

 {"slug":"ch10-comecar","sub":"CAPÍTULO 10: Como Começar",
  "intro":"Saber não basta — é preciso agir. O capítulo final reúne gatilhos práticos para ativar a inteligência financeira e passos concretos para começar a construir a coluna de ativos hoje.",
  "cards":[
      {"ic":"mountain","t":"Uma Razão Maior que a Realidade","emph":"Razão Maior","b":"Um porquê pálido gera o recuo na primeira trincheira suja de sangue. O motor não avança pelo glamour do dólar; avança porque o terror agudo de <strong>terminar dependendo da compaixão e engolir as ordens alheias com o joelho em terra na velhice queima mais forte do que a preguiça letárgica do presente</strong>.","tip":"<strong>Como aplicar:</strong> arranque o verniz das palavras e anote a ira bruta e inegociável que faz você levantar dessa cadeira."},
      {"ic":"constellation","t":"Poder da Escolha & da Associação","emph":"Associação","b":"Cada dez centavos e cada cinco minutos torrados formam a cédula de votação do seu futuro cimentado ou triturado. Expurque a praga de reclamões do seu perímetro e <strong>alugue um espaço VIP no círculo invisível onde tubarões debatem fortunas, porque o pensamento se arrasta em manada e você imita de quem foge ou caça</strong>.","tip":"<strong>Modelo mental:</strong> o nível do jogo é puxado pelo adversário e pelo aliado do lado; a mediocridade ao redor rebaixa o cérebro rapidamente à temperatura morna local."},
      {"ic":"steps","t":"Comece Pequeno, mas Comece","emph":"Comece","b":"Devorar biblioteca sobre mercado e estagiar em planilhas teóricas acaba na mais covarde masturbação acadêmica. Arrume um troco ridículo, compre a primeira pedra microscópica e acione o risco real: <strong>o suor do medo vivo fará pelas suas conexões cerebrais aquilo que duas mil horas de MBA enlatado não ousaram fazer</strong>.","tip":"<strong>Sinal de alerta:</strong> não se afogue no mar da paralisia pelo excesso da teoria inútil. Puxe o gatilho; pule e entenda a gravidade só após a queda inicial.","warn":True},
    ],
  "lessons_title":"Lições-Chave do Capítulo 10",
  "lessons":["Tenha um 'porquê' forte — ele sustenta a disciplina quando a motivação cai.","Invista primeiro em educação e em boas companhias financeiras.","Aja: comece pequeno, com um ativo real, em vez de só acumular teoria."]},
]
