# -*- coding: utf-8 -*-
"""Conteúdo (pt-BR) de 'Antifrágil: Coisas que se Beneficiam com o Caos' (Nassim Nicholas Taleb)."""

BOOK = {
  "title": "Antifrágil",
  "author": "Nassim Nicholas Taleb",
  "header_light": "ANTI",
  "header_bold": "FRÁGIL",
  "subtitle": "VISÃO GERAL · COISAS QUE SE BENEFICIAM COM O CAOS",
  "intro": "Existe uma categoria sem nome além de 'frágil' e 'robusto': o antifrágil — o que ganha com a desordem, a volatilidade e o estresse, em vez de só resistir. Taleb mostra como detectar fragilidade sem prever o futuro, comprar 'opcionalidade' (ganhos assimétricos) e construir sistemas — corpo, carreira, finanças, instituições — que prosperam no caos.",
  "description": "Ensaio de Nassim Taleb sobre como prosperar na desordem. A tríade frágil/robusto/antifrágil, opcionalidade, a estratégia barbell, via negativa, pele em jogo, o efeito Lindy, hormese, iatrogenia e a crítica à previsão. Quarto volume do Incerto, na linha de 'O Cisne Negro'.",
  "tags": ["Incerteza", "Risco", "Filosofia Prática"],
  "progress": "7 Capítulos",
  "cover": "assets/antifragil-cover.png",
  "overview_cards": [
    {"ic":"scale","t":"A Tríade: Frágil / Robusto / Antifrágil","b":"O <strong>frágil</strong> quebra com o choque; o <strong>robusto</strong> aguenta e volta igual; o <strong>antifrágil</strong> melhora. Resistir não é ganhar — robustez é o piso, antifragilidade é o objetivo.","tip":"<strong>Modelo mental:</strong> diante de qualquer sistema, pergunte 'o que isto faz quando é sacudido?' — piora=frágil, nada muda=robusto, melhora=antifrágil.","warn":True},
    {"ic":"fork","t":"Opcionalidade e a Estratégia Barbell","b":"<strong>Opcionalidade</strong>: ter o direito (não o dever) de aproveitar o que der certo — downside travado, upside aberto. A <strong>barbell</strong> aplica isso: ~90% ultrasseguro + ~10% em apostas pequenas e muito arriscadas, nada no meio 'moderado'.","tip":"<strong>Como aplicar:</strong> prefira posições com pior caso pequeno e fechado e melhor caso aberto — você ganha sem precisar prever."},
    {"ic":"leaf","t":"Via Negativa e Pele em Jogo","b":"<strong>Via negativa</strong>: subtrair o nocivo é mais robusto que adicionar o 'bom' incerto (sabemos melhor o que é errado). <strong>Pele em jogo</strong>: quem decide deve carregar o erro — 'o capitão afunda com o navio'.","tip":"<strong>Para refletir:</strong> antes de agir, pergunte 'o que posso remover?'; antes de confiar num conselho, 'quem paga se der errado?'."},
  ],
}

CHAPTERS = [
  {
    "slug": "ch01-o-antifragil-uma-introducao",
    "sub": "LIVRO 1: O Antifrágil — Uma Introdução",
    "intro": "Há uma terceira categoria, sem nome até Taleb, além de frágil e robusto: o antifrágil, que ganha com a desordem em vez de apenas resistir. A ausência da palavra escondeu uma propriedade fundamental do mundo — e identificá-la muda toda decisão sob incerteza.",
    "cards": [
      {"ic":"scale","t":"A Tríade","b":"<strong>Frágil</strong> quebra com o choque (a espada de Dâmocles); <strong>robusto</strong> aguenta e volta igual (a Fênix); <strong>antifrágil</strong> melhora (a Hidra: corta-se uma cabeça, nascem duas). A volatilidade é veneno para um, indiferente para outro, alimento para o terceiro.","tip":"<strong>Como aplicar:</strong> classifique tudo pela reação ao choque — não pergunte 'isto é bom?', pergunte 'como isto reage à desordem?'.","warn":True},
      {"ic":"leaf","t":"Hormese","b":"O estressor em <strong>pequena dose fortalece</strong>: o músculo cresce sob carga, o osso densifica, o corpo se imuniza com um pouco de veneno (mitridatização). Privar um sistema antifrágil de estressores o <strong>atrofia</strong> — a iatrogenia do conforto.","tip":"<strong>Modelo mental:</strong> pense numa 'resposta a doses' — antifrágil é remédio em dose pequena e veneno em dose enorme."},
      {"ic":"target","t":"Sobrecompensação","b":"O sistema antifrágil não só repara o dano: cria <strong>capacidade extra</strong>, uma reserva para o próximo choque. O estressor é informação — sem ele, o sistema fica cego ao próprio risco e fragiliza em silêncio.","tip":"<strong>Para refletir:</strong> conforto e estabilidade total não trazem segurança; produzem fragilidade oculta que estoura de uma vez."},
    ],
    "lessons_title": "Lições-Chave do Capítulo 1",
    "lessons": [
      "A categoria 'antifrágil' não tinha nome — e o que não tem nome fica invisível à decisão.",
      "Frágil odeia volatilidade; robusto a ignora; antifrágil a deseja, em dose.",
      "Hormese: o estressor certo, na dose certa, fortalece; a privação de estresse atrofia.",
      "Resistir não é ganhar: robustez é o piso, antifragilidade é o objetivo.",
    ],
  },
  {
    "slug": "ch02-modernidade-e-a-negacao-da-antifragilidade",
    "sub": "LIVRO 2: Modernidade e a Negação da Antifragilidade",
    "intro": "A modernidade tenta suprimir a volatilidade — alisar ciclos, estabilizar tudo. Mas privar um sistema antifrágil de sua volatilidade natural não o protege: acumula fragilidade escondida que estoura num único Cisne Negro. A intervenção sem necessidade é o pecado capital do moderno.",
    "cards": [
      {"ic":"wrench","t":"Iatrogenia","b":"'Causado pelo curador': o <strong>dano oculto da intervenção</strong>. O intervencionista vê o ganho visível da ação e ignora o dano invisível e tardio — na medicina, na economia, na política, na criação dos filhos.","tip":"<strong>Regra:</strong> só intervir quando o benefício for grande e claro; no caso leve, pratique a procrastinação racional (deixe o sistema se autocorrigir).","warn":True},
      {"ic":"clock","t":"O Peru de Russell","b":"O peru alimentado todo dia ganha 'confiança' crescente na bondade do dono — até a véspera do Dia de Ação de Graças. <strong>Estabilidade aparente = fragilidade máxima acumulada.</strong> Quanto mais longa a calmaria, maior o risco escondido na cauda.","tip":"<strong>Para refletir:</strong> este sistema está calmo porque é saudável, ou porque está sendo artificialmente segurado?"},
      {"ic":"wave","t":"Volatilidade Suprimida","b":"Apagar todo incêndio pequeno acumula combustível para o incêndio catastrófico; reprimir toda recessão prepara o colapso. O risco <strong>não desaparece — migra para a cauda</strong>, vira raro porém devastador. Sistemas vivos pedem solavancos pequenos e frequentes.","tip":"<strong>Modelo mental:</strong> a Suíça (decisões locais, bottom-up) é robusta; o Estado tecnocrático top-down é frágil."},
    ],
    "lessons_title": "Lições-Chave do Capítulo 2",
    "lessons": [
      "Suprimir a volatilidade não elimina o risco — concentra-o na cauda.",
      "Iatrogenia: o dano invisível do 'curador' que precisava ter ficado quieto.",
      "Sistemas vivos pedem estressores pequenos e frequentes; sem eles, fragilizam.",
      "Procrastinação racional é, às vezes, a decisão mais robusta.",
    ],
  },
  {
    "slug": "ch03-uma-visao-nao-preditiva-do-mundo",
    "sub": "LIVRO 3: Uma Visão Não-Preditiva do Mundo",
    "intro": "Em vez de prever o imprevisível, posicione-se para se beneficiar da assimetria: minimize o dano dos eventos ruins e fique exposto aos bons. Não preveja o evento — gerencie a fragilidade à variação. Quem distingue o frágil do antifrágil não precisa de bola de cristal.",
    "cards": [
      {"ic":"scale","t":"A Assimetria de Sêneca","b":"O estoico Sêneca, riquíssimo, já contava as posses como perdidas: <strong>neutralizado o downside, só sobrava upside</strong>. Antifragilidade = mais upside que downside diante da volatilidade; fragilidade, o inverso. O formato do payoff importa mais que a probabilidade.","tip":"<strong>Como aplicar:</strong> aniquile o downside primeiro — só então o upside é gratuito.","warn":True},
      {"ic":"person","t":"Fat Tony × Dr. John","b":"<strong>Fat Tony</strong> fareja a fragilidade pelo bom senso e pela pele em jogo; <strong>Dr. John</strong> raciocina por modelos frágeis e probabilidades falsas. A sabedoria prática (mêtis) bate o conhecimento acadêmico abstrato no terreno do incerto.","tip":"<strong>Para refletir:</strong> quem tem pele em jogo fareja o que o modelo não vê."},
      {"ic":"eye","t":"Não Prever, Medir Fragilidade","b":"Erramos sistematicamente nas caudas; planejar sobre previsões é construir na areia. Mas a <strong>fragilidade é mensurável e previsível</strong> — o evento, não. Quem não está frágil dispensa o oráculo.","tip":"<strong>Modelo mental:</strong> troque 'qual a probabilidade do evento?' por 'qual o meu payoff se o evento vier?'."},
    ],
    "lessons_title": "Lições-Chave do Capítulo 3",
    "lessons": [
      "Não preveja o evento; meça e neutralize a fragilidade a ele.",
      "Sêneca: elimine o downside e o upside vem de graça — a postura antifrágil.",
      "Fat Tony fareja fragilidade; o acadêmico se perde em modelos — pele em jogo bate teoria.",
      "O formato do payoff (assimetria) decide mais que a probabilidade.",
    ],
  },
  {
    "slug": "ch04-opcionalidade-tecnologia-e-a-inteligencia-da-antifragilidade",
    "sub": "LIVRO 4: Opcionalidade, Tecnologia e a Inteligência da Antifragilidade",
    "intro": "A antifragilidade vem da opcionalidade: ter o direito (não o dever) de aproveitar o que der certo, descartando o que der errado. A opção converte volatilidade em ganho. Por isso a tentativa-e-erro bate o planejamento teórico: o erro é barato, o acerto é ilimitado.",
    "cards": [
      {"ic":"fork","t":"Opcionalidade","b":"Assimetria embutida: <strong>pequeno custo de entrada, downside travado, upside aberto</strong>. 'Você não precisa estar certo com frequência — só quando a recompensa for grande.' A opção dá antifragilidade sem exigir previsão.","tip":"<strong>Como aplicar:</strong> prefira posições com pouco a perder e muito a ganhar; mantenha-se exposto a boas surpresas.","warn":True},
      {"ic":"scale","t":"Estratégia Barbell (Halteres)","b":"Combine dois extremos e evite o meio: <strong>~85–90% extremamente seguro + ~10–15% muito arriscado e pequeno</strong>. Downside travado pelo lado seguro, upside aberto pelo agressivo. O 'moderado' do meio engana — esconde risco de cauda.","tip":"<strong>Para refletir:</strong> pior caso = perder só a fração arriscada; melhor caso = um acerto que paga tudo."},
      {"ic":"spark","t":"Tinkering (Tentativa-e-Erro)","b":"A inovação real nasce de <strong>muitas tentativas baratas</strong>, não de grandes planos (a ilusão 'Soviético-Harvard'). Cada erro é informação de baixo custo; o acerto ocasional paga por todos. A prática precede a teoria.","tip":"<strong>Modelo mental:</strong> erre barato e cedo — mas só se o pior caso for pequeno e conhecido."},
    ],
    "lessons_title": "Lições-Chave do Capítulo 4",
    "lessons": [
      "Opcionalidade = downside travado + upside aberto: ganha-se com a volatilidade sem prever nada.",
      "Barbell: extremos (muito seguro + pouco e muito arriscado), nunca o morno do meio.",
      "Tinkering convexo: erre barato e cedo; o acerto raro paga por todos os erros.",
      "A prática precede a teoria — desconfie do crédito que a academia se atribui.",
    ],
  },
  {
    "slug": "ch05-o-nao-linear-e-o-nao-linear",
    "sub": "LIVRO 5: O Não-Linear e o Não-Linear",
    "intro": "A definição técnica de fragilidade e antifragilidade é geométrica, não emocional: tudo se resume ao formato da resposta — a convexidade. Frágil é curva côncava (acelera o dano); antifrágil é convexa (acelera o ganho). E há um teste prático para detectar fragilidade sem prever nada.",
    "cards": [
      {"ic":"gap","t":"Convexidade × Concavidade","b":"O que importa não é a média do estressor, mas a resposta a <strong>doses crescentes</strong>. <strong>Côncavo (frágil):</strong> o dano cresce mais que proporcionalmente — cair de 10 m machuca muito mais que dez quedas de 1 m. <strong>Convexo (antifrágil):</strong> o ganho cresce mais que proporcionalmente.","tip":"<strong>Como aplicar:</strong> dobre o estressor — se o dano mais que dobra, é frágil; se o ganho mais que dobra, é antifrágil.","warn":True},
      {"ic":"lens","t":"O Efeito de Jensen","b":"Sob não-linearidade, a <strong>média dos resultados ≠ resultado da média</strong>. O frágil sofre da 'média escondida': parece OK na média, mas a variação o destrói. O que mata (ou salva) é a dispersão, não o valor médio.","tip":"<strong>Para refletir:</strong> raciocinar pela média esconde a cauda — e a cauda é onde tudo se decide."},
      {"ic":"layers","t":"O Efeito do Tamanho","b":"A mesma 'quantidade' de estresse fere muito mais se vier <strong>concentrada e rápida</strong>. O grande e concentrado é frágil (um elefante despenca; muitos camundongos, não). Prefira muitos pequenos e independentes a um grande.","tip":"<strong>Modelo mental:</strong> concentração e gigantismo escondem risco de cauda côncava."},
    ],
    "lessons_title": "Lições-Chave do Capítulo 5",
    "lessons": [
      "Fragilidade é côncava (dano acelera); antifragilidade é convexa (ganho acelera).",
      "Sob não-linearidade, a média mente — o que mata é a variação (efeito de Jensen).",
      "Você não precisa prever o evento: meça a aceleração do dano e detecte a fragilidade.",
      "O grande e concentrado é frágil; muitos pequenos e independentes são robustos.",
    ],
  },
  {
    "slug": "ch06-via-negativa",
    "sub": "LIVRO 6: Via Negativa",
    "intro": "Subtrair é mais robusto que adicionar. Sabemos com muito mais segurança o que é errado do que o que é certo. A melhoria mais confiável vem de remover o frágil, o nocivo, o supérfluo — não de acrescentar mais um remédio, mais uma regra, mais uma feature.",
    "cards": [
      {"ic":"leaf","t":"Via Negativa","b":"Agir por <strong>subtração</strong>: o que é mau é mais conhecível que o bom. Recomendação por remoção (parar de fumar, cortar açúcar, eliminar a má dívida) é mais robusta que por adição — porque toda adição carrega iatrogenia oculta.","tip":"<strong>Como aplicar:</strong> antes de adicionar uma solução, pergunte 'o que posso remover para resolver isto?'.","warn":True},
      {"ic":"clock","t":"O Efeito Lindy","b":"Para o <strong>não-perecível</strong> (ideias, livros, tecnologias, instituições), a expectativa de vida futura cresce com a idade já vivida: cada ano sobrevivido prevê mais um. O que durou prova durabilidade — o tempo é o melhor filtro de fragilidade.","tip":"<strong>Regra:</strong> na dúvida, prefira o que já passou no teste do tempo."},
      {"ic":"pivot","t":"Neomania","b":"O vício no <strong>novo pelo novo</strong>: superestimar o recente e descartar o que o tempo já validou. Antídoto: o filtro de Lindy. O moderno confunde novidade com qualidade — e troca o robusto testado pelo frágil da moda.","tip":"<strong>Para refletir:</strong> o novíssimo ainda não passou no teste do tempo; o clássico já passou."},
    ],
    "lessons_title": "Lições-Chave do Capítulo 6",
    "lessons": [
      "Via negativa: subtrair o frágil/nocivo é mais robusto que adicionar o 'bom'.",
      "Lindy: para ideias e tecnologias, o que durou tende a durar — o tempo filtra fragilidade.",
      "Toda adição (regra, remédio, feature) carrega iatrogenia oculta; a remoção, quase nunca.",
      "Combata a neomania: prefira o testado pelo tempo ao novíssimo da moda.",
    ],
  },
  {
    "slug": "ch07-a-etica-da-fragilidade-e-da-antifragilidade",
    "sub": "LIVRO 7: A Ética da Fragilidade e da Antifragilidade",
    "intro": "O grande problema ético da modernidade é a transferência de fragilidade: alguém colhe o upside e empurra o downside para os outros. A correção é uma só — pele em jogo: quem decide deve carregar as consequências do erro.",
    "cards": [
      {"ic":"scale","t":"Pele em Jogo","b":"<strong>Simetria</strong> entre quem decide e quem sofre o resultado: 'todo capitão afunda com seu navio'. Sem pele em jogo, o agente fica antifrágil às custas do sistema — ganha nos bônus, socializa as perdas.","tip":"<strong>Como aplicar:</strong> antes de confiar numa decisão ou conselho, pergunte 'quem paga se isto der errado?'.","warn":True},
      {"ic":"link","t":"Transferência de Fragilidade","b":"Alguns ganham robustez <strong>extraindo-a de outrem</strong>: o banqueiro que lucra no risco e é socorrido na quebra, o 'especialista' sem custo do erro. É roubo de cauda — upside privado, downside coletivo.","tip":"<strong>Para refletir:</strong> incentivos que premiam o ganho e isentam da perda são fábrica de risco transferido."},
      {"ic":"person","t":"O Problema do Agente","b":"Gestores, consultores e burocratas com <strong>opção sem obrigação</strong>: capturam o ganho visível, transferem o risco oculto. O herói antigo (que pagava com a própria vida) é o oposto do agente moderno. A coragem é a única virtude impossível de fingir.","tip":"<strong>Modelo mental:</strong> desconfie de quem opina/decide sem custo; valorize quem arca com o próprio erro."},
    ],
    "lessons_title": "Lições-Chave do Capítulo 7",
    "lessons": [
      "O pecado ético central é transferir fragilidade: ganhar no upside e empurrar o downside aos outros.",
      "Pele em jogo restaura a simetria — quem decide carrega o erro ('o capitão afunda com o navio').",
      "Desconfie de quem opina/decide sem custo do erro; valorize quem paga pelo que prescreve.",
      "A coragem (risco assumido por outros) é a única virtude impossível de fingir.",
    ],
  },
]
