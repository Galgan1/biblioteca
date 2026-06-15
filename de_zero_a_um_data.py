# -*- coding: utf-8 -*-
"""Conteúdo (pt-BR) de 'De Zero a Um' (Zero to One) de Peter Thiel com Blake Masters."""

BOOK = {
  "title": "De Zero a Um",
  "author": "Peter Thiel com Blake Masters",
  "header_light": "DE ZERO",
  "header_bold": "A UM",
  "subtitle": "VISÃO GERAL · COMO CONSTRUIR O FUTURO",
  "intro": "O futuro valioso não vem de copiar o que existe (ir de 1 a n), mas de criar o que nunca existiu (ir de 0 a 1). Thiel mostra por que o monopólio criativo bate a concorrência, como encontrar o segredo que poucos veem, e quais as 7 perguntas que toda startup precisa acertar.",
  "description": "Ensaio de Peter Thiel (com Blake Masters) sobre startups e inovação: progresso vertical (0→1) × horizontal (1→n), a pergunta contrária, monopólio criativo × concorrência, lei de potência, segredos, fundações, distribuição e as 7 perguntas de toda startup. Manual contrário de como criar o novo.",
  "tags": ["Empreendedorismo", "Inovação", "Estratégia"],
  "progress": "14 Capítulos",
  "cover": "assets/de-zero-a-um-cover.png",
  "overview_cards": [
    {"ic":"spark","t":"Progresso Vertical (0→1)","b":"Há dois tipos de progresso. O <strong>vertical (0→1)</strong> cria o radicalmente novo — é tecnologia. O <strong>horizontal (1→n)</strong> copia o que já funciona — é globalização. O futuro valioso vem de inventar, não de copiar.","tip":"<strong>Modelo mental:</strong> pergunte 'isto cria o que não existia (0→1) ou só replica/escala o existente (1→n)?'.","warn":True},
    {"ic":"lens","t":"A Pergunta Contrária","b":"A bússola do livro: <strong>'Que verdade importante pouquíssimas pessoas concordam com você?'</strong> A boa resposta é impopular mas verdadeira — e aponta o futuro que ninguém vê ainda.","tip":"<strong>Para refletir:</strong> a resposta certa é um <em>segredo</em>; procure-o onde ninguém olha."},
    {"ic":"target","t":"Monopólio × Concorrência","b":"'A concorrência é para perdedores': empresas iguais brigam por margens que vão a zero. O alvo é o <strong>monopólio criativo</strong> — ser tão melhor em algo que ninguém compete de verdade — e <strong>capturar</strong> o valor, não só criá-lo.","tip":"<strong>Para refletir:</strong> companhias aéreas criam valor e não o capturam; o Google captura. Tamanho não é monopólio."},
  ],
}

CHAPTERS = [
  {
    "slug": "ch01-o-desafio-do-futuro",
    "sub": "CAPÍTULO 1: O Desafio do Futuro",
    "intro": "Há dois tipos de progresso: o vertical (0→1), que cria algo radicalmente novo, e o horizontal (1→n), que copia o que já funciona. A próxima onda de empresas valiosas virá de fazer 0→1 — tecnologia, não globalização.",
    "cards": [
      {"ic":"spark","t":"0→1 × 1→n","b":"<strong>Vertical (0→1)</strong> = tecnologia, criar o que não existia. <strong>Horizontal (1→n)</strong> = globalização, copiar e espalhar. O mundo é finito: copiar sem inventar esgota; o futuro precisa do 0→1.","tip":"<strong>Como aplicar:</strong> pergunte 'isto é invenção do novo (0→1) ou cópia melhorada (1→n)?'.","warn":True},
      {"ic":"lens","t":"A Pergunta Contrária","b":"'Que verdade importante <strong>pouquíssimas pessoas concordam com você</strong>?' Boas respostas revelam o futuro que ninguém vê. A resposta certa é impopular — mas verdadeira.","tip":"<strong>Modelo mental:</strong> o que é óbvio para você e estranho para os outros pode ser sua oportunidade."},
      {"ic":"wave","t":"Tecnologia ≠ Globalização","b":"Confundir progresso com globalização é o erro de base. Copiar o que funciona em escala não é criar o futuro — é só 1→n. <strong>Tecnologia, não consenso</strong>, cria valor radicalmente novo.","tip":"<strong>Para refletir:</strong> a startup é o maior grupo que você convence de um plano para um futuro diferente."},
    ],
    "lessons_title": "Lições-Chave do Capítulo 1",
    "lessons": [
      "O futuro valioso vem do progresso vertical (0→1), não da mera globalização (1→n).",
      "A 'pergunta contrária' é a bússola: procure a verdade importante que poucos veem.",
      "Tecnologia, não consenso, é o que cria valor radicalmente novo.",
    ],
  },
  {
    "slug": "ch02-festa-como-em-1999",
    "sub": "CAPÍTULO 2: Festa como em 1999",
    "intro": "A bolha das pontocom deixou quatro 'lições' que estão erradas. As verdades opostas são mais úteis — e, na dúvida, é melhor ser ousado e ter convicção do que seguir o rebanho do mercado.",
    "cards": [
      {"ic":"scale","t":"As 4 Lições Erradas","b":"O crash ensinou o oposto do certo: (1) avançar passo a passo; (2) ser lean/flexível; (3) melhorar sobre o concorrente; (4) focar produto, não vendas. <strong>Lição de consenso = sinal de alerta.</strong>","tip":"<strong>Como aplicar:</strong> para cada dogma pós-bolha, considere a verdade contrária."},
      {"ic":"spark","t":"As 4 Verdades Opostas","b":"(1) Melhor a ousadia que a trivialidade; (2) um plano ruim > nenhum plano; (3) mercados competitivos destroem lucro — fuja; (4) <strong>vendas importam tanto quanto o produto</strong>.","tip":"<strong>Modelo mental:</strong> ousadia com tese é menos arriscada que trivialidade sem direção.","warn":True},
    ],
    "lessons_title": "Lições-Chave do Capítulo 2",
    "lessons": [
      "As quatro lições populares da bolha são, em sua maioria, falsas.",
      "Ousadia com convicção bate trivialidade prudente.",
      "Um plano, mesmo imperfeito, supera a improvisação perpétua.",
    ],
  },
  {
    "slug": "ch03-todas-as-empresas-felizes-sao-diferentes",
    "sub": "CAPÍTULO 3: Todas as Empresas Felizes São Diferentes",
    "intro": "A concorrência perfeita destrói o lucro: empresas iguais brigam por margens que tendem a zero. O alvo de toda startup que cria e captura valor é o oposto — o monopólio (ser tão melhor que ninguém compete de verdade).",
    "cards": [
      {"ic":"target","t":"Monopólio Criativo","b":"<strong>'A concorrência é para perdedores.'</strong> O monopólio aqui não é cartel: é ser radicalmente melhor em algo. É a condição de qualquer negócio duradouro e lucrativo — só sobra lucro para quem escapa da concorrência.","tip":"<strong>Como aplicar:</strong> 'esta empresa é única e dona do seu mercado, ou só mais uma de margens espremidas?'.","warn":True},
      {"ic":"key","t":"Criar × Capturar Valor","b":"Criar valor não basta — é preciso <strong>reter</strong> parte dele. As companhias aéreas criam muito valor e capturam quase nada; o Google cria menos e captura uma fatia imensa. A diferença é monopólio × concorrência.","tip":"<strong>Modelo mental:</strong> separe 'quanto valor gera para o mundo' de 'quanto fica para si'."},
      {"ic":"mask","t":"As Duas Mentiras","b":"O monopolista <strong>finge competir</strong> (para não chamar atenção); o não-monopolista <strong>inventa um nicho próprio</strong> (para parecer único). Suspeite das duas narrativas e leia o mercado por trás delas.","tip":"<strong>Para refletir:</strong> definir o mercado como interseção estreita revela se você é único de verdade."},
    ],
    "lessons_title": "Lições-Chave do Capítulo 3",
    "lessons": [
      "A concorrência é para perdedores; o objetivo é o monopólio criativo.",
      "Criar valor não basta — é preciso capturar valor para sobreviver.",
      "Monopolistas e não-monopolistas mentem em direções opostas sobre seu mercado.",
    ],
  },
  {
    "slug": "ch04-a-ideologia-da-concorrencia",
    "sub": "CAPÍTULO 4: A Ideologia da Concorrência",
    "intro": "A concorrência não é só uma condição econômica: é uma ideologia que distorce o pensamento e nos faz lutar onde não deveríamos. Obcecados pelo rival, copiamos o existente e perdemos a chance de criar o novo.",
    "cards": [
      {"ic":"sword","t":"Concorrência como Ideologia","b":"Somos ensinados a competir, e isso vira hábito mental que nos prende a brigas sem prêmio. A rivalidade leva a <strong>guerras que destroem valor</strong> para os dois lados.","tip":"<strong>Como aplicar:</strong> 'estou lutando por este mercado porque ele vale, ou só porque há alguém para vencer?'.","warn":True},
      {"ic":"fork","t":"Guerra × Lucro","b":"Quanto mais parecidos os rivais, mais feroz e inútil a disputa (eco de Girard: desejamos o que o outro deseja). Às vezes a jogada certa é <strong>não lutar</strong> — recuar ou fundir cria mais valor que vencer.","tip":"<strong>Modelo mental:</strong> par de gêmeos brigando — guerra simbólica que custa mais do que rende."},
    ],
    "lessons_title": "Lições-Chave do Capítulo 4",
    "lessons": [
      "A concorrência é uma ideologia que distorce o foco — leva a copiar, não a criar.",
      "Nem toda batalha vale a pena; às vezes recuar ou fundir cria mais valor.",
      "Quanto mais parecidos os rivais, mais destrutiva e fútil a disputa.",
    ],
  },
  {
    "slug": "ch05-vantagem-do-pioneiro",
    "sub": "CAPÍTULO 5: Vantagem do Pioneiro (Last Mover)",
    "intro": "Um monopólio só vale se durar. O valor de uma empresa está na soma dos fluxos de caixa futuros — por isso a durabilidade vale mais que o crescimento rápido. Quatro forças sustentam o monopólio duradouro.",
    "cards": [
      {"ic":"layers","t":"As 4 Forças de Durabilidade","b":"<strong>Tecnologia proprietária</strong> (~10× melhor, não marginal), <strong>efeitos de rede</strong> (mais usuários = mais valor), <strong>economias de escala</strong> e <strong>marca</strong>. Quanto mais presentes, mais defensável.","tip":"<strong>Como aplicar:</strong> melhoria precisa ser de ordem de grandeza (10×), não de 20%.","warn":True},
      {"ic":"clock","t":"Vantagem do Último (Last Mover)","b":"Melhor que ser o primeiro é fazer o <strong>grande avanço final</strong> e dominar por décadas. O pioneirismo é tática, não objetivo. Valor = soma dos fluxos de caixa futuros → durabilidade > faturamento de hoje.","tip":"<strong>Modelo mental:</strong> árvore que dá fruto por décadas — o valor está nas safras futuras."},
      {"ic":"mountain","t":"Comece Pequeno e Domine","b":"Comece num <strong>mercado pequeno dominável</strong> (fatia grande de um nicho), depois expanda. Monopólio local antes de global — é mais fácil dominar uma interseção estreita.","tip":"<strong>Para refletir:</strong> efeito de rede precisa ser valioso já para os primeiros usuários."},
    ],
    "lessons_title": "Lições-Chave do Capítulo 5",
    "lessons": [
      "O que conta é a durabilidade do monopólio, não o tamanho de hoje.",
      "As 4 forças: tecnologia proprietária (10×), efeitos de rede, escala, marca.",
      "Ser o último a se mover (e ficar) vence ser o primeiro a chegar.",
    ],
  },
  {
    "slug": "ch06-voce-nao-e-um-bilhete-de-loteria",
    "sub": "CAPÍTULO 6: Você Não É um Bilhete de Loteria",
    "intro": "O sucesso é fruto de projeto deliberado, não de sorte. Thiel cruza dois eixos — otimista/pessimista e definido/indefinido. O 0→1 vive no otimismo definido: ter um plano específico e executá-lo.",
    "cards": [
      {"ic":"steps","t":"Definido × Indefinido","b":"Quatro visões de futuro. O <strong>otimista-definido</strong> tem plano e esperança — é o motor do 0→1. O <strong>otimista-indefinido</strong> (Ocidente atual) acredita que melhora, mas sem plano; cultua 'manter opções abertas'.","tip":"<strong>Como aplicar:</strong> há um plano específico (definido) e há esperança (otimista)?","warn":True},
      {"ic":"key","t":"Sorte × Projeto","b":"Tratar o sucesso como loteria desvaloriza o planejamento. Fundadores de 0→1 <strong>recusam a 'sorte'</strong> como explicação. 'Manter as opções abertas' é um custo, não uma virtude — sem compromisso, nada de 0→1 acontece.","tip":"<strong>Para refletir:</strong> o futuro definido prefere quem constrói uma coisa a quem diversifica para tudo."},
    ],
    "lessons_title": "Lições-Chave do Capítulo 6",
    "lessons": [
      "O sucesso é projetado, não sorteado.",
      "O otimismo definido (plano + esperança) é o motor do 0→1.",
      "Trocar plano por flexibilidade leva à estagnação de visão.",
    ],
  },
  {
    "slug": "ch07-siga-o-dinheiro",
    "sub": "CAPÍTULO 7: Siga o Dinheiro",
    "intro": "A lei de potência (power law) governa investimentos e resultados: alguns poucos vencedores superam todos os outros somados. O que mais importa raramente é distribuído por igual — e a diversificação cega é uma armadilha.",
    "cards": [
      {"ic":"spark","t":"Lei de Potência (Power Law)","b":"O melhor investimento de um fundo iguala ou supera <strong>todos os outros juntos</strong>. A distribuição é radicalmente desigual, não normal. Aposte em poucas coisas com potencial de serem enormes — não pulverize.","tip":"<strong>Modelo mental:</strong> uma sequoia gigante entre arbustos — o resultado total é a sequoia.","warn":True},
      {"ic":"target","t":"A Regra do VC","b":"Só invista no que tem potencial de <strong>devolver o fundo inteiro</strong> sozinho. Apostas medianas, mesmo lucrativas, não movem o ponteiro. A diversificação cega dilui justamente o vencedor que define o resultado.","tip":"<strong>Para refletir:</strong> vale para a carreira — poucas apostas grandes batem muitas pequenas."},
    ],
    "lessons_title": "Lições-Chave do Capítulo 7",
    "lessons": [
      "A lei de potência domina: poucos vencedores superam todo o resto.",
      "Só aposte no que pode ser enorme — o resto é ruído.",
      "Aplique a lógica à própria carreira, não só ao capital.",
    ],
  },
  {
    "slug": "ch08-segredos",
    "sub": "CAPÍTULO 8: Segredos",
    "intro": "Todo grande negócio se constrói sobre um segredo — uma verdade importante que ainda poucos conhecem. A crença de que 'não há mais segredos' é justamente o que impede de encontrá-los.",
    "cards": [
      {"ic":"key","t":"Segredos × Mistérios","b":"Entre as verdades fáceis (convencionais) e as impossíveis (mistérios) estão os <strong>segredos</strong>: difíceis, mas descobríveis. São o material de 0→1 — a versão prática da pergunta contrária.","tip":"<strong>Como aplicar:</strong> não confunda mistério (ninguém pode saber) com segredo (difícil, mas alcançável).","warn":True},
      {"ic":"lens","t":"Onde Procurar","b":"Há segredos de <strong>natureza</strong> (o mundo físico) e de <strong>pessoas</strong> (o que escondem ou não sabem de si). Procure em áreas negligenciadas, campos 'resolvidos' ou tabu — o segredo está onde ninguém olha.","tip":"<strong>Para refletir:</strong> o 'fim dos segredos' é o mito que faz a cultura parar de procurá-los."},
    ],
    "lessons_title": "Lições-Chave do Capítulo 8",
    "lessons": [
      "Todo grande negócio nasce de um segredo que poucos conhecem.",
      "Segredos existem (de natureza e de pessoas); a cultura é que parou de procurá-los.",
      "Procure onde ninguém olha — o convencional e o tabu escondem segredos.",
    ],
  },
  {
    "slug": "ch09-fundacoes",
    "sub": "CAPÍTULO 9: Fundações",
    "intro": "Uma startup arruinada na fundação não se conserta depois. A 'Lei de Thiel': uma empresa mal fundada não pode ser corrigida. As decisões iniciais — sócios, propriedade, papéis — definem o destino.",
    "cards": [
      {"ic":"layers","t":"Lei de Thiel","b":"<strong>Uma startup estragada na fundação não pode ser consertada.</strong> Por isso as escolhas do 'dia zero' são as mais importantes: cofundadores com história, expectativas alinhadas antes de começar.","tip":"<strong>Modelo mental:</strong> concreto fresco — molda-se uma vez; depois de curado, não se reforma.","warn":True},
      {"ic":"scale","t":"Propriedade · Posse · Controle","b":"Quem detém o capital (<strong>propriedade</strong>), quem toca o dia a dia (<strong>posse</strong>) e quem governa as decisões (<strong>controle</strong>). O conflito surge quando os três se desencontram — alinhe-os cedo.","tip":"<strong>Como aplicar:</strong> conselho enxuto (idealmente 3); maior = mais difícil decidir."},
      {"ic":"person","t":"Dentro ou Fora","b":"Todo envolvido deve estar <strong>em tempo integral e com capital</strong>, ou de fora — meios-termos (part-time, consultores no núcleo) corroem. Pague pouco em salário e muito em participação para alinhar o longo prazo.","tip":"<strong>Para refletir:</strong> CEO mal pago é bom sinal — prova compromisso com o valor de longo prazo."},
    ],
    "lessons_title": "Lições-Chave do Capítulo 9",
    "lessons": [
      "Uma fundação ruim não se conserta — acerte no começo.",
      "Alinhe propriedade, posse e controle desde o dia zero.",
      "Cofundadores precisam de história e expectativas alinhadas; é dentro ou fora.",
    ],
  },
  {
    "slug": "ch10-a-mecanica-da-mafia",
    "sub": "CAPÍTULO 10: A Mecânica da Máfia",
    "intro": "Uma grande empresa é uma cultura, não só uma estrutura. A 'Máfia do PayPal' virou modelo: contrate pessoas que se gostam de verdade, que partilham uma missão e que formam uma tribo, não um bando de mercenários nem de zelotes.",
    "cards": [
      {"ic":"constellation","t":"A Empresa como Tribo","b":"A melhor startup é uma 'seita leve': vínculo forte, missão compartilhada, identidade própria. <strong>Cultura não é perk</strong> — é quem você contrata e por quê. Recrutar é conspirar para uma missão, não preencher vagas.","tip":"<strong>Como aplicar:</strong> 'por que trabalhar AQUI e não em qualquer lugar que pague igual?'.","warn":True},
      {"ic":"fork","t":"Mercenários × Zelotes","b":"Evite os extremos: nem <strong>mercenários</strong> (só por dinheiro) nem <strong>zelotes</strong> (fanáticos cegos). Busque o meio — comprometidos com a missão e com as pessoas. E dê a cada um uma <strong>responsabilidade única</strong>.","tip":"<strong>Para refletir:</strong> papéis sobrepostos criam guerra interna — a concorrência ideológica dentro de casa."},
    ],
    "lessons_title": "Lições-Chave do Capítulo 10",
    "lessons": [
      "A empresa é uma cultura (tribo com missão), não uma estrutura.",
      "Contrate quem se gosta e partilha a missão; fuja de mercenários e zelotes.",
      "Dê a cada pessoa uma responsabilidade única para matar o conflito interno.",
    ],
  },
  {
    "slug": "ch11-se-voce-construir-eles-virao",
    "sub": "CAPÍTULO 11: Se Você Construir, Eles Virão?",
    "intro": "Distribuição importa tanto quanto o produto. Um ótimo produto sem plano de venda fracassa. 'Se você construir, eles virão' é falso — existe uma lei de potência também na distribuição.",
    "cards": [
      {"ic":"link","t":"A Primazia da Distribuição","b":"Vender e distribuir são tão decisivos quanto construir — e a melhor venda é <strong>invisível</strong> (parece que 'o produto se vendeu'). Trate distribuição como parte do design do negócio, não como detalhe final.","tip":"<strong>Como aplicar:</strong> em geral, UM canal domina — ache-o e foque nele, não disperse.","warn":True},
      {"ic":"scale","t":"CLV × CAC","b":"O valor do cliente (<strong>CLV</strong>) precisa superar com folga o custo de adquiri-lo (<strong>CAC</strong>). O método de venda segue o ticket: venda complexa (deals grandes) → vendedor → publicidade → viral (grátis).","tip":"<strong>Modelo mental:</strong> viral exige coeficiente > 1 — cada usuário traz mais de um novo."},
      {"ic":"gap","t":"A Zona Morta","b":"Há uma 'zona morta' de ticket médio (~US$ 1.000): <strong>caro demais</strong> para vender só com anúncios, <strong>barato demais</strong> para sustentar um vendedor. Preso nela? Suba o ticket ou desça drasticamente.","tip":"<strong>Para refletir:</strong> ficar no meio mata; o CAC come o CLV."},
    ],
    "lessons_title": "Lições-Chave do Capítulo 11",
    "lessons": [
      "Distribuição importa tanto quanto o produto; 'construa e eles virão' é mito.",
      "CLV deve superar o CAC; o método de venda segue o tamanho do ticket.",
      "Cuidado com a zona morta de ticket médio; em geral um único canal domina.",
    ],
  },
  {
    "slug": "ch12-o-homem-e-a-maquina",
    "sub": "CAPÍTULO 12: O Homem e a Máquina",
    "intro": "Computadores são complementos dos humanos, não substitutos. A maior oportunidade não é a IA que substitui pessoas, mas os sistemas que combinam o julgamento humano com a escala da máquina.",
    "cards": [
      {"ic":"link","t":"Complemento × Substituto","b":"A globalização vê o trabalho como competição (máquina × humano); a tecnologia de verdade vê <strong>complementaridade</strong>. Humanos decidem e dão sentido; máquinas processam e escalam. Os melhores produtos juntam os dois.","tip":"<strong>Como aplicar:</strong> pergunte 'como a máquina amplia o humano?', não 'como o substitui?'.","warn":True},
      {"ic":"person","t":"O Centauro","b":"Humano + máquina supera tanto o humano sozinho quanto a máquina sozinha. A máquina <strong>sinaliza</strong> padrões em volumes imensos; o humano <strong>julga</strong> os casos difíceis. Não compita com o computador — faça par com ele.","tip":"<strong>Para refletir:</strong> ganhos reais vêm de máquinas que ajudam pessoas, não de uma superinteligência futura."},
    ],
    "lessons_title": "Lições-Chave do Capítulo 12",
    "lessons": [
      "Computadores complementam humanos; não os substituem (e isso cria mais valor).",
      "Humanos julgam e dão sentido; máquinas escalam e processam.",
      "Os melhores produtos combinam ambos — pense complemento, não competição.",
    ],
  },
  {
    "slug": "ch13-vendo-verde",
    "sub": "CAPÍTULO 13: Vendo Verde",
    "intro": "A bolha das cleantech quebrou porque quase nenhuma empresa respondia às 7 perguntas que toda startup precisa acertar. Boa intenção e mercado quente não bastam — faltava engenharia, monopólio, distribuição e segredo.",
    "cards": [
      {"ic":"target","t":"As 7 Perguntas","b":"<strong>(1) Engenharia</strong> (10×?) · <strong>(2) Timing</strong> (a hora certa?) · <strong>(3) Monopólio</strong> (nicho dominável?) · <strong>(4) Equipe</strong> (os sócios certos?) · <strong>(5) Distribuição</strong> (plano de venda?) · <strong>(6) Durabilidade</strong> (10–20 anos?) · <strong>(7) Segredo</strong> (oportunidade única?).","tip":"<strong>Como aplicar:</strong> é preciso ir bem na MAIORIA — acertar uma ou duas não salva.","warn":True},
      {"ic":"leaf","t":"Setor da Moda ≠ Tese","b":"O 'verde' estava na moda, mas moda <strong>não responde nenhuma das 7 perguntas</strong> — daí a quebra em massa. Painéis 'um pouco melhores' falham na engenharia (não é 10×), no timing, no monopólio e no segredo.","tip":"<strong>Modelo mental:</strong> use as 7 perguntas como raio-X — poucas respostas fortes = bolha."},
    ],
    "lessons_title": "Lições-Chave do Capítulo 13",
    "lessons": [
      "As 7 perguntas (engenharia, timing, monopólio, equipe, distribuição, durabilidade, segredo) são o teste decisivo.",
      "Acertar uma ou duas não basta — é preciso ir bem na maioria.",
      "Setor em alta não responde nenhuma das 7 perguntas; moda não é tese.",
    ],
  },
  {
    "slug": "ch14-o-paradoxo-do-fundador",
    "sub": "CAPÍTULO 14: O Paradoxo do Fundador",
    "intro": "Os fundadores que importam são pessoas extremas e paradoxais — ao mesmo tempo insiders e outsiders, celebrados e demonizados. A sociedade precisa desses singulares porque só eles conseguem o pensamento de 0→1.",
    "cards": [
      {"ic":"person","t":"O Paradoxo do Fundador","b":"Grandes fundadores acumulam traços <strong>opostos em grau extremo</strong> (gênio e ingênuo, querido e odiado, insider e outsider). Não são 'normais' — são outliers. A média não cria 0→1; o novo nasce do extremo.","tip":"<strong>Para refletir:</strong> não tente fabricar um fundador 'equilibrado' — o valor está na excentricidade produtiva.","warn":True},
      {"ic":"spark","t":"Preservar o Pensamento de 0→1","b":"Porque o futuro depende de poucos indivíduos singulares, a tarefa final é <strong>cultivar</strong> (não nivelar) os que veem segredos e criam o novo. O '1' decisivo vem de pessoas excepcionais, não de algoritmos.","tip":"<strong>Modelo mental:</strong> resista à pressão de nivelar tudo à média — o progresso vertical vem do incomum."},
    ],
    "lessons_title": "Lições-Chave do Capítulo 14",
    "lessons": [
      "Grandes fundadores são paradoxais e extremos — outliers, não médias.",
      "A sociedade precisa deles porque o 0→1 vem de poucos indivíduos singulares.",
      "Preservar o pensamento de 0→1 é a tarefa final: cultive o incomum em vez de nivelá-lo.",
    ],
  },
]
