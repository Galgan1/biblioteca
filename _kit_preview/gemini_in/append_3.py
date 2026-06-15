import sys

content = """
=== mundo-de-sofia ===
```json
{
  "ch01-espanto-e-a-moldura": {
    "cards": [
      {
        "ic": "eye",
        "t": "O Coelho na Cartola",
        "emph": "Coelho na Cartola",
        "b": "Imagine o cosmos como um truque de mágica. Nascemos na ponta fina dos pelos do coelho, maravilhados e tontos. Mas a rotina pesa e nós <strong>escorregamos preguiçosamente para o fundo da pelagem</strong>, onde é quente e seguro. O verdadeiro filósofo é aquele que escala o pelo de volta para encarar o ilusionista nos olhos.",
        "tip": "<strong>Como aplicar:</strong> trate a rotina como um sedativo. Se você não se espanta mais com o fato de estar vivo, já adormeceu no fundo do pelo."
      },
      {
        "ic": "bulb",
        "t": "Perguntas Valem Mais que Respostas",
        "emph": "Perguntas",
        "b": "O mercado vende soluções enlatadas, mas a filosofia é a arte subversiva de <strong>arrombar as fechaduras do óbvio</strong>. Fazer a pergunta certa, sentindo o assombro infantil diante da resposta que foge, é o exercício máximo de quem recusa o rebanho.",
        "tip": "<strong>Modelo mental:</strong> respostas finais matam a curiosidade. O combustível de uma mente afiada é a pergunta que ainda dói."
      },
      {
        "ic": "bubble",
        "t": "Mito × Razão",
        "emph": "Razão",
        "b": "O berço do pensamento ocidental balançou no exato momento em que alguém parou de culpar a fúria dos deuses pelo trovão e <strong>exigiu uma explicação física e lógica</strong>. O desencantamento não empobreceu o mundo; ele nos deu a chave mestra para dominar a matéria.",
        "tip": "<strong>Regra:</strong> sempre que você justifica um problema com 'é assim que a banda toca', você acabou de ajoelhar no altar do mito."
      }
    ]
  },
  "ch02-pre-socraticos": {
    "cards": [
      {
        "ic": "wave",
        "t": "Tudo Flui × Nada Muda",
        "emph": "Flui × Muda",
        "b": "Heráclito decreta o terror do panta rhei: <strong>o rio é outro e você também</strong>. Parmênides grita o oposto: os sentidos mentem, o Ser é de cimento. É a batalha eterna entre confiar no caos daquilo que os seus olhos veem ou na arquitetura de aço que só a sua mente constrói.",
        "tip": "<strong>Modelo mental:</strong> toda a história do pensamento (e do seu próprio cérebro) é a guerra fria entre o que muda hoje e o que permanece sempre."
      },
      {
        "ic": "layers",
        "t": "A Busca pela Physis",
        "emph": "Physis",
        "b": "De Tales a Anaximandro, a audácia suprema foi buscar <strong>o tijolo único que levanta o prédio inteiro do universo</strong>. Não se apegue ao erro deles (achar que tudo era água ou ar), admire a revolução do método: a crença de que o infinito pode ser explicado por um fio racional.",
        "tip": "<strong>Como aplicar:</strong> diante de um problema complexo no trabalho, escave freneticamente até isolar a 'physis' — o princípio raiz que origina todo o caos."
      },
      {
        "ic": "link",
        "t": "Demócrito e os Átomos",
        "emph": "Átomos",
        "b": "O ancestral letal do método científico rasgou os céus poéticos: nada de deuses, apenas blocos eternos, invisíveis e de lego infinito que se <strong>chocam no escuro e formam galáxias e pessoas</strong>. É a brutalidade de explicar o milagre complexo pela simples matemática da matéria.",
        "tip": "<strong>Para refletir:</strong> a ciência moderna inteira é o triunfo do ceticismo atômico de Demócrito. Ele quebrou o feitiço."
      }
    ]
  },
  "ch03-socrates-platao-aristoteles": {
    "cards": [
      {
        "ic": "bubble",
        "t": "A Maiêutica Socrática",
        "emph": "Maiêutica",
        "b": "O gênio de Atenas não dava aulas; ele implodia a ignorância fazendo a pergunta exata. A maiêutica é o parto forçado da mente: <strong>fazer o outro vomitar a contradição</strong> que ele escondia de si mesmo. O primeiro pilar é confessar que não sabe nada. O ego inflado é o cemitério da sabedoria.",
        "tip": "<strong>Prática:</strong> em uma discussão difícil, esconda o martelo das afirmações. Use a navalha das perguntas até a defesa do outro desmoronar."
      },
      {
        "ic": "mountain",
        "t": "O Mundo das Ideias",
        "emph": "Mundo das Ideias",
        "b": "A Caverna de Platão é o pesadelo eterno da humanidade. Vivemos tateando sombras na parede, aplaudindo o teatro de ilusões, enquanto as <strong>Formas puras e cortantes queimam no sol do lado de fora</strong>. O papel do pensador não é o de guru, é o do cara que te arrasta para a luz cegante.",
        "tip": "<strong>Sinal de alerta:</strong> o que você toma por verdade inegociável é, com frequência, só o reflexo distorcido de um consenso social que alguém inventou.",
        "warn": true
      },
      {
        "ic": "lens",
        "t": "Aristóteles — A Forma nas Coisas",
        "emph": "Forma nas Coisas",
        "b": "Aristóteles agarra Platão pelos ombros e o joga na lama da realidade física. A beleza não flutua num céu abstrato; ela <strong>mora dentro da matéria que você toca e cheira</strong>. O conhecimento começa suando frio na trincheira dos cinco sentidos, classificando o mundo como ele é.",
        "tip": "<strong>Modelo mental:</strong> se você sofre demais com o 'ideal', aplique Aristóteles. A perfeição não está num rascunho de gaveta, mas no objeto pronto na mesa."
      }
    ]
  },
  "ch04-helenismo-e-idade-media": {
    "cards": [
      {
        "ic": "leaf",
        "t": "Filosofia como Arte de Viver",
        "emph": "Arte de Viver",
        "b": "Quando o mundo grego desmoronou, a filosofia deixou de ser ciência estelar e virou caixa de primeiros socorros. O estoico blinda a mente contra o que não controla; o epicurista <strong>caça ferozmente a ausência de dor</strong>. Era o pensamento transformado em torniquete existencial.",
        "tip": "<strong>Como aplicar:</strong> o estoicismo de Epicteto é pragmatismo sangrento: separe com precisão cirúrgica a sua atitude mental do lixo que acontece lá fora."
      },
      {
        "ic": "scale",
        "t": "Agostinho × Tomás — Fé e Razão",
        "emph": "Fé e Razão",
        "b": "Os dois titãs que costuraram Atenas e Jerusalém. Agostinho pegou o Idealismo de Platão e o batizou nas águas divinas; Tomás de Aquino puxou a biologia de Aristóteles e <strong>provou a existência de Deus no compasso matemático da razão</strong>. A Idade Média não dormiu; ela engajou o intelecto numa fusão nuclear.",
        "tip": "<strong>Para refletir:</strong> não despreze a Idade Média como um abismo escuro. Ela foi a bigorna onde a herança greco-romana foi forjada para não morrer."
      },
      {
        "ic": "spiral",
        "t": "Neoplatonismo — A Emanação do Uno",
        "emph": "Emanação",
        "b": "Plotino cria um abismo cósmico onde o Ser Supremo (o Uno) transborda luz sem fim, e a nossa matéria crua é apenas a sombra fria onde a luz não chegou. É uma mística brutal: <strong>retornar ao centro apagando as ilusões da carne</strong>. Um eco que explodirá no Romantismo séculos depois.",
        "tip": "<strong>Modelo mental:</strong> veja a busca por sentido espiritual como uma escalada desesperada para sair da beirada fria da sombra e correr para o sol central."
      }
    ]
  },
  "ch05-renascenca-descartes": {
    "cards": [
      {
        "ic": "bulb",
        "t": "A Dúvida Metódica",
        "emph": "Dúvida Metódica",
        "b": "Descartes passa a retroescavadeira na própria mente. Ele recusa todas as tradições e certezas e duvida ativamente dos sentidos e da vigília para <strong>derrubar qualquer parede que trema</strong>. Ele não quer o caos; ele destrói a metrópole inteira para encontrar a única pedra de granito que resiste a explosões.",
        "tip": "<strong>Prática:</strong> quer achar a verdade sobre um projeto? Descarte impiedosamente tudo que foi aceito 'porque sim' e veja o que fica de pé."
      },
      {
        "ic": "spark",
        "t": "'Penso, Logo Existo'",
        "emph": "Penso, Logo Existo",
        "b": "O choque elétrico que inaugurou o homem moderno: o <em>Cogito</em>. Mesmo que um gênio maligno me engane em tudo, o fato de que estou aqui angustiado e pensando <strong>prova irrefutavelmente o meu Ser</strong>. A bússola do mundo sai das estrelas celestes e passa a girar dentro do crânio humano.",
        "tip": "<strong>Regra:</strong> o 'eu' virou o centro gravitacional. Você só legitima a realidade externa a partir do momento em que a sua consciência a atesta."
      },
      {
        "ic": "gap",
        "t": "O Problema do Dualismo",
        "emph": "Dualismo",
        "b": "O fantasma na máquina. Descartes espreme o universo em dois baldes incompatíveis: a <em>res cogitans</em> (espírito sem massa) e a <em>res extensa</em> (matéria cega). A herança que ele deixou é o <strong>nó cego definitivo</strong>: se alma e carne são matérias de dimensões alienígenas, como uma move a outra?",
        "tip": "<strong>Sinal de alerta:</strong> até hoje tratamos a mente e o corpo como se fossem inquilinos inimigos na mesma casa — esse é o preço do corte de Descartes."
      }
    ]
  },
  "ch06-spinoza-empiristas": {
    "cards": [
      {
        "ic": "leaf",
        "t": "Deus sive Natura",
        "emph": "Deus sive Natura",
        "b": "O panteísmo vulcânico de Spinoza aniquila o dualismo e decreta: Deus e a Natureza são a mesma <strong>massa divina e imensurável</strong>. Nós não moramos em um mundo criado por um relojoeiro ausente; nós somos os modos e as ondulações desse próprio Deus vibrando. Tudo está amarrado.",
        "tip": "<strong>Modelo mental:</strong> olhe para a realidade <em>sub specie aeternitatis</em>. Seus problemas perdem a força quando você os vê na escala gelada da eternidade."
      },
      {
        "ic": "eye",
        "t": "A Tabula Rasa e o Esse Est Percipi",
        "emph": "Tabula Rasa",
        "b": "Locke zera o jogo dizendo que nascemos uma folha em branco, rabiscada pelas mãos cruéis da experiência. Mas é Berkeley quem torce a maçaneta da loucura lógica: <strong>existir é apenas ser percebido na mente de alguém</strong>. A matéria densa evapora; somos apenas ideias pulsando no ar.",
        "tip": "<strong>Como aplicar:</strong> o 'ser percebido' antecipa a Matrix e a simulação de Sofia. Sua realidade sólida depende sempre de um espectador."
      },
      {
        "ic": "lens",
        "t": "Hume Dissolve a Causalidade",
        "emph": "Causalidade",
        "b": "O cético brutal que esmagou a ciência e obrigou Kant a levantar da cama. Hume afirma que você nunca viu a 'causa e efeito'; você apenas viu uma bola bater na outra e <strong>condicionou a sua mente a esperar a mesma coisa de novo</strong>. O hábito não é prova de lei universal.",
        "tip": "<strong>Pergunta-chave:</strong> o que você chama de 'regra inquebrável' não seria apenas o seu vício mental em prever repetições confortáveis?",
        "warn": true
      }
    ]
  },
  "ch07-kant": {
    "cards": [
      {
        "ic": "lens",
        "t": "Os Óculos da Mente",
        "emph": "Óculos da Mente",
        "b": "Kant costura o buraco deixado pelos empiristas e racionalistas. O espaço, o tempo e a causa não flutuam soltos pelo espaço sideral; eles são os <strong>óculos permanentes colados no seu crânio</strong>. Você nunca verá o mundo sem essas lentes, logo, a sua ciência é exata, mas restrita ao que o vidro alcança.",
        "tip": "<strong>Modelo mental:</strong> não lute para ver a realidade sem o seu cérebro. Aceite o equipamento que tem e maximize o uso do software interno."
      },
      {
        "ic": "gap",
        "t": "Fenômeno × Coisa-em-Si",
        "emph": "Fenômeno × Coisa-em-Si",
        "b": "A fronteira inquebrável. O mundo como nos aparece (fenômeno) é o parque de diversões da ciência. A Coisa-em-Si (a realidade nua por trás da tela) é o <strong>abismo escuro e trancado a sete chaves</strong>. Kant não diz que estamos sonhando, mas exige respeito pela cortina de ferro que limita o nosso olho.",
        "tip": "<strong>Sinal de alerta:</strong> alegar que descobriu a verdade metafísica absoluta é a maior arrogância punida pelo tribunal kantiano."
      },
      {
        "ic": "scale",
        "t": "O Imperativo Categórico",
        "emph": "Imperativo Categórico",
        "b": "A ética de Kant não negocia com Deus e nem calcula o lucro das ações. A regra máxima surge do próprio software da razão humana: aja apenas de um modo que <strong>você toleraria que virasse a lei para todos os vivos da Terra</strong>. O ser humano é o destino final, nunca o trampolim do seu ego.",
        "tip": "<strong>Prática:</strong> antes de puxar o tapete, pergunte: 'se isso fosse lei mundial hoje, a humanidade sobreviveria amanhã?' Se a resposta é não, não o faça."
      }
    ]
  },
  "ch08-hegel-kierkegaard-marx-freud": {
    "cards": [
      {
        "ic": "spiral",
        "t": "A Dialética de Hegel",
        "emph": "Dialética",
        "b": "A verdade não é uma rocha gelada num museu; ela é um <strong>rio de sangue e história</strong>. Uma tese domina, engorda e sofre o golpe brutal da sua antítese. O cadáver dos dois vira o adubo para uma síntese superior. O Espírito do mundo avança assim, engolindo os confrontos e subindo a montanha.",
        "tip": "<strong>Como aplicar:</strong> não tente destruir o argumento do rival por inteiro. A evolução exige que você quebre a tese dele e absorva a parte que funciona."
      },
      {
        "ic": "person",
        "t": "Kierkegaard — O Indivíduo Concreto",
        "emph": "Indivíduo Concreto",
        "b": "O soco na cara do sistema abstrato de Hegel. Kierkegaard grita que focar no 'Espírito do mundo' é esquecer <strong>o pobre infeliz que sua, sangra e tem que escolher como viver agora</strong>. O existencialismo nasce aqui: o seu dever de agarrar a vida e dar um salto no escuro, rumo à fé irracional e viva.",
        "tip": "<strong>Modelo mental:</strong> chega de teorias cósmicas de poltrona. A angústia da escolha diária é a única sala de aula que importa."
      },
      {
        "ic": "triangle",
        "t": "Os Três Mestres da Suspeita",
        "emph": "Mestres da Suspeita",
        "b": "A trinca de ferro que fuzilou o rei-sol da razão: Darwin, rasgando o mito da criação pura; Marx, provando que o tal idealismo era escravo do bolso e do pão; e Freud, detonando que o homem <strong>nem sequer manda na própria sala de estar mental</strong>. Eles inauguraram a era do olho clínico e da desconfiança.",
        "tip": "<strong>Regra:</strong> sempre interrogue a 'nobreza' das ideias. Há sempre um macaco biológico, um saldo bancário ou um desejo enjaulado operando a máquina."
      }
    ]
  },
  "ch09-sartre-virada-meta": {
    "cards": [
      {
        "ic": "key",
        "t": "'Condenados a ser Livres'",
        "emph": "Condenados",
        "b": "A bomba-relógio de Sartre aniquila a natureza humana. O homem é atirado no chão cru do universo e <strong>tem que inventar o próprio sentido suando sangue nas escolhas</strong>. Essa liberdade infinita não é festa; é a fonte da nossa angústia suprema, porque apaga qualquer chance de culpar a genética ou a deusa da sorte.",
        "tip": "<strong>Sinal de alerta:</strong> o termo 'má-fé' define o momento exato em que você aponta para a cadeira e culpa a vida pelas escolhas que você assinou.",
        "warn": true
      },
      {
        "ic": "constellation",
        "t": "A Virada Meta",
        "emph": "Virada Meta",
        "b": "A rasteira genial do livro. Quando Sofia e Alberto acordam como meros personagens do teclado de um Major onipotente, todo o caldo filosófico ferve junto. Eles executam o grito final do existencialismo: lutar cegamente para <strong>quebrar o destino escrito nas páginas e assumir o roteiro à força</strong>.",
        "tip": "<strong>Modelo mental:</strong> imagine quantas camadas de roteiros sociais, corporativos e mentais estão escrevendo as suas falas hoje. Salte fora do papel."
      },
      {
        "ic": "eye",
        "t": "O Cosmos e o Espanto Final",
        "emph": "Espanto Final",
        "b": "A aula finaliza onde tudo nasceu. Nossos ossos e olhos são as sobras carbonizadas de constelações mortas; a humanidade é o pedaço de universo que <strong>ganhou olhos para se encantar e sentir pavor diante do próprio espelho</strong>. A ciência entregou as chaves do carro, mas a estupefação do existir jamais sumirá.",
        "tip": "<strong>Para refletir:</strong> se lembrar que você é o resíduo fumegante de uma supernova não te faz levantar da cama em choque, nada mais fará."
      }
    ]
  }
}
```

=== pai-rico-pai-pobre ===
```json
{
  "ch01-dois-pais": {
    "cards": [
      {
        "ic": "fork",
        "t": "Os Dois Pais",
        "emph": "Dois Pais",
        "b": "É a escolha entre jogar na segurança medíocre ou aprender o código do sistema. O Pai Pobre adora diplomas e tem pavor da falência; o Pai Rico largou o quadro negro para <strong>dobrar a espinha dorsal do dinheiro e forçá-lo a trabalhar sem folga</strong>. É o contraste letal entre ganhar salário e gerar riqueza.",
        "tip": "<strong>Prática:</strong> audite sua mente agora. Você está operando com o software do medo do contracheque ou com o radar da oportunidade invisível?"
      },
      {
        "ic": "lens",
        "t": "Acadêmico ≠ Financeiro",
        "emph": "Acadêmico ≠ Financeiro",
        "b": "O maior golpe do sistema educacional é convencer você de que um boletim com notas altas garante imunidade ao desastre na conta bancária. Ser uma estrela acadêmica com um salário inflado é inútil se a sua <strong>analfabetização financeira sangra cada centavo num passivo disfarçado</strong>.",
        "tip": "<strong>Cuidado:</strong> pare de aceitar ordens financeiras de especialistas teóricos que nunca pisaram no lado ensanguentado da trincheira do mercado.",
        "warn": true
      },
      {
        "ic": "bulb",
        "t": "\"Como Posso Pagar?\"",
        "emph": "Como Posso Pagar?",
        "b": "O 'eu não posso comprar' é a droga que anestesia o cérebro; ele tranca as portas e permite que a mente durma. A virada violenta é forçar a engrenagem com 'como eu posso comprar isso?'. Essa simples engenharia verbal <strong>chicoteia a criatividade e obriga a mente a fabricar uma rota de fuga</strong>.",
        "tip": "<strong>Modelo mental:</strong> a negação decreta a morte da imaginação. A pergunta joga oxigênio na fogueira da solução de problemas."
      }
    ]
  },
  "ch02-nao-trabalhar-por-dinheiro": {
    "cards": [
      {
        "ic": "spiral",
        "t": "A Corrida dos Ratos",
        "emph": "Corrida dos Ratos",
        "b": "O manicômio do contracheque, onde acordar, bater cartão e pagar boleto forma a roda do hamster perfeita. A piada cruel é que a cada promoção, você adquire uma gaiola mais cara; a receita salta e <strong>as despesas sangram exatamente na mesma proporção para sustentar o cenário</strong>.",
        "tip": "<strong>Sinal de alerta:</strong> se você comemora um aumento trocando imediatamente de carro ou mudando de bairro, a roda de metal acabou de girar mais rápido."
      },
      {
        "ic": "wave",
        "t": "Medo e Ganância",
        "emph": "Medo e Ganância",
        "b": "Os dois motores invisíveis que pilotam o cérebro das massas. O chicote frio do medo do aluguel empurra o sujeito para o escritório, e a ganância por brinquedos cintilantes rouba o dinheiro dele na sexta-feira. <strong>Você trabalha escravizado pela emoção pura</strong>, achando que está usando a lógica.",
        "tip": "<strong>Como aplicar:</strong> corte a injeção dessas duas drogas. Avalie friamente onde colocar a nota de dinheiro, sem pânico de perder e sem fissura de ostentar."
      },
      {
        "ic": "target",
        "t": "Trabalhe para Aprender",
        "emph": "Aprender",
        "b": "O rebanho entra na empresa de joelhos perguntando 'qual é a escala e o salário?'. O investidor de elite entra pelo mesmo saguão e mapeia: 'quais habilidades brutais eu posso roubar dessa operação?'. O medo não deve paralisá-lo, deve <strong>dar fome de comer as regras inteiras do jogo</strong>.",
        "tip": "<strong>Regra de ouro:</strong> o dinheiro da carteira assinada acaba no mês que vem; a mecânica do negócio que você decodificou pagará a conta para o resto da vida."
      }
    ]
  },
  "ch03-ativo-passivo": {
    "cards": [
      {
        "ic": "scale",
        "t": "Ativo vs. Passivo (a Regra nº1)",
        "emph": "Ativo vs. Passivo",
        "b": "A guilhotina financeira: ativo injeta fluxo constante de sangue no seu caixa; passivo enfia a mão no seu bolso e leva o sangue embora. Não interessa o brilho ou o que o corretor sussurra; <strong>antes de assinar o cheque, exija saber de que lado da trincheira aquele objeto vai lutar</strong>.",
        "tip": "<strong>Como aplicar:</strong> o luxo que não gera lucro não é 'meu pequeno investimento', é apenas um pedágio caro para o próprio ego."
      },
      {
        "ic": "steps",
        "t": "O Padrão de Fluxo de Caixa",
        "emph": "Fluxo de Caixa",
        "b": "O pobre pega o contracheque e queima na vala da sobrevivência. A classe média comete suicídio lento comprando bugigangas caríssimas jurando que são patrimônio. A elite <strong>redireciona a mangueira da renda exclusivamente para os ativos</strong>, construindo um exército autônomo que caça dinheiro 24 horas.",
        "tip": "<strong>Modelo mental:</strong> pare de ler etiquetas de preço. Aprenda a ler os vetores invisíveis do fluxo de caixa que cruzam o papel."
      },
      {
        "ic": "gap",
        "t": "A Casa Não É um Ativo",
        "emph": "Casa Não É um Ativo",
        "b": "A heresia suprema de Kiyosaki que fuzila o dogma americano: a sua casa própria adorável chupa IPTU, arranca taxas de manutenção e devora juros de prestação. <strong>Se drena o fluxo do caixa em vez de enchê-lo, é um passivo de concreto armado</strong>, independentemente do que diga o seu avô.",
        "tip": "<strong>Sinal de alerta:</strong> afundar 100% da sua munição na parede de tijolos do seu teto trava brutalmente a montagem do seu portfólio guerreiro.",
        "warn": true
      }
    ]
  },
  "ch04-cuide-do-seu-negocio": {
    "cards": [
      {
        "ic": "layers",
        "t": "Emprego ≠ Negócio",
        "emph": "Emprego ≠ Negócio",
        "b": "A sua rotina massacrante na corporação garante a picanha do seu patrão; isso é a sua profissão, não a sua mina de ouro. A jogada mestra é bater o ponto para garantir a gasolina do mês, mas <strong>dedicar a noite implacavelmente para erguer o castelo da sua própria coluna de ativos</strong>.",
        "tip": "<strong>Como aplicar:</strong> o turno do dia paga a sua sobrevivência; o turno da madrugada empilha os ativos que vão comprar a sua alforria."
      },
      {
        "ic": "leaf",
        "t": "Construa a Coluna de Ativos",
        "emph": "Coluna de Ativos",
        "b": "Empilhe soldados de papel que não dormem, não fazem greve e valorizam no escuro: ações explosivas, imóveis que sangram aluguel e royalties que pingam sem aviso. A lei é militar — inicie com um esquadrão minúsculo, e <strong>estrangule qualquer chance de um passivo inútil inflar no começo</strong>.",
        "tip": "<strong>Prática:</strong> cada cédula poupada num vício banal é a semente pronta de um pequeno tanque de guerra que vai lutar pela sua fortuna."
      },
      {
        "ic": "sword",
        "t": "Luxos por Último",
        "emph": "Luxos por Último",
        "b": "O pobre antecipa o brinquedo, torrando o crédito que não tem. A classe média finge ser rica comprando fumaça. Os titãs <strong>compram carros e joias exclusivamente com o sangue derramado pelo exército de ativos</strong>. O prêmio é o suco da vitória do sistema, e não o suor do próprio salário.",
        "tip": "<strong>Modelo mental:</strong> o cordão de ouro não é proibido. Proibido é ser pago pelo salário; ele deve ser a sobra gorda do ativo que você construiu."
      }
    ]
  },
  "ch05-impostos-corporacoes": {
    "cards": [
      {
        "ic": "layers",
        "t": "A História dos Impostos",
        "emph": "História dos Impostos",
        "b": "O Robin Hood do estado cobrou imposto dos milionários com a promessa de dar aos pobres; mas a fome do leviatã acordou e logo engoliu a garganta da classe média que batia palmas. <strong>O estado pune quem produz salário e alivia o chicote de quem orquestra corporações blindadas</strong>.",
        "tip": "<strong>Sinal de alerta:</strong> a moral da lenda é que a classe média pagará a conta do baile enquanto acreditar que bater ponto garante a segurança."
      },
      {
        "ic": "scale",
        "t": "O Jogo da Classe Média vs. Rico",
        "emph": "Classe Média vs. Rico",
        "b": "A classe média trabalha, o governo suga a primeira fatia do bolo e ela tenta sobreviver com as migalhas finais. O rico vira a mesa: <strong>a corporação dele arrecada tudo, torra legalmente nas despesas operacionais pesadas e oferece ao governo apenas o que sobra</strong> no osso das tributações.",
        "tip": "<strong>Como aplicar:</strong> a corporação e o CNPJ não são estruturas teóricas, são as escotilhas de sobrevivência na selva tributária. Use o escudo de aço."
      },
      {
        "ic": "book",
        "t": "Conhecimento, Não Trapaça",
        "emph": "Conhecimento",
        "b": "O uso brutal da pessoa jurídica não é um assalto à mão armada; é usar a própria engenharia do livro de regras do sistema para levantar trincheiras. <strong>É a maestria jurídica que desvia o imposto legalmente, e não a burrice suicida de esconder dinheiro embaixo do colchão</strong>.",
        "tip": "<strong>Regra:</strong> não caia na tentação da fraude amadora. Contrate a melhor inteligência tributária e vença usando exatamente a gramática deles."
      }
    ]
  },
  "ch06-inventar-dinheiro": {
    "cards": [
      {
        "ic": "spark",
        "t": "Inteligência Financeira Inventa Dinheiro",
        "emph": "Inventa Dinheiro",
        "b": "O dinheiro não é um recurso finito escondido num cofre; ele é fabricado no vácuo pela mente treinada que conecta a solução ao problema alheio. <strong>A maior âncora da pobreza não é a conta zerada, é a covardia patológica diante do risco</strong> e a paralisia perante a página em branco da oportunidade.",
        "tip": "<strong>Prática:</strong> treine o olho clínico. O mercado está cheio de fortunas ocultas esperando que a ignorância dos outros bata na genialidade da sua percepção."
      },
      {
        "ic": "mountain",
        "t": "Risco Calculado",
        "emph": "Risco Calculado",
        "b": "Esconder o dinheiro na poupança com pavor da chuva é a aposta mais radioativa a longo prazo. Risco não é pular da ponte de olhos vendados; é a <strong>ciência fria de entrar na arena blindado com informações táticas</strong>. Aprender a apanhar logo no início é arrancar o dente do medo.",
        "tip": "<strong>Modelo mental:</strong> quem joga sempre para não perder termina na lona esmagado pela inflação. O risco calculado é a única matemática da riqueza."
      },
      {
        "ic": "pivot",
        "t": "Os Dois Tipos de Investidor",
        "emph": "Dois Tipos de Investidor",
        "b": "Existe a ovelha dócil que compra pacotes mastigados na prateleira do banco. E existe o predador alfa, que encontra o terreno destruído, arranja o cimento, agrupa as ferramentas e <strong>monta o esqueleto do próprio golias do zero, criando um valor que não existia</strong> no planeta ontem de manhã.",
        "tip": "<strong>Como aplicar:</strong> recuse o menu degustação. Aprenda a montar o prato juntando as peças no mercado primário e engula as margens que os preguiçosos largam."
      }
    ]
  },
  "ch07-trabalhe-para-aprender": {
    "cards": [
      {
        "ic": "book",
        "t": "Cada Emprego é uma Escola",
        "emph": "Emprego é uma Escola",
        "b": "Um contracheque não deve ser a sua ração de sobrevivência, deve ser a bolsa que financia os seus estudos nas entranhas da corporação. Mergulhe no moedor de carne empresarial e <strong>trate cada rotina como um módulo letal para roubar o <em>know-how</em></strong> antes que o departamento demita você.",
        "tip": "<strong>Prática:</strong> troque de setor voluntariamente. Trocar salário alto por um treinamento prático insano constrói o armamento que te blindará na guerra final."
      },
      {
        "ic": "link",
        "t": "Habilidades Amplas > Especialização",
        "emph": "Habilidades Amplas",
        "b": "Ficar dez anos virando a mesma engrenagem cria a síndrome do macaco adestrado. Você precisa ser um lobo híbrido: entender da matemática dos lucros, do controle de pânico da equipe e da arte sutil do convencimento. <strong>O hiper-especialista treme no vento; o generalista faminto assume a cadeira do chefe</strong>.",
        "tip": "<strong>Regra:</strong> não mergulhe tanto no poço de uma função que esqueça de ler o manual que pilota a fábrica inteira."
      },
      {
        "ic": "target",
        "t": "Saber Vender é a Habilidade nº1",
        "emph": "Saber Vender",
        "b": "Um projeto absurdamente revolucionário sem uma voz capaz de empurrá-lo goela abaixo do investidor é apenas poesia murcha de gaveta. Vender não é pedir esmola, <strong>é o dom de dominar o ar ao redor e transferir a convicção do seu sangue para a cabeça da outra pessoa</strong>. O medo da rejeição é a guilhotina do sucesso.",
        "tip": "<strong>Sinal de alerta:</strong> se você recusa treinar a sua oratória e a sua capacidade de venda, preparou a mesa perfeita para que um medíocre carismático leve a melhor."
      }
    ]
  },
  "ch08-cinco-obstaculos": {
    "cards": [
      {
        "ic": "wave",
        "t": "Medo & Cinismo",
        "emph": "Medo & Cinismo",
        "b": "O terror frio de assinar um cheque arriscado é natural, o crime é deixá-lo sequestrar o volante da ação. O cinismo agudo é a praga que faz os medrosos bancarem os <strong>profetas do apocalipse, caçando o fio de cabelo no omelete para justificar a paralisia do sofá</strong>. Trate o ruído deles como lixo.",
        "tip": "<strong>Como aplicar:</strong> os 'amigos cautelosos' são o departamento de marketing do fracasso. Abafe os gritos de quem não tem pele em risco."
      },
      {
        "ic": "clock",
        "t": "Preguiça & Maus Hábitos",
        "emph": "Preguiça & Maus Hábitos",
        "b": "A camuflagem perfeita da preguiça moderna é o culto da agenda entupida: trabalhar dezoito horas cavando o próprio buraco sem focar no pilar que sustenta o cofre. O pecado capital da rotina não é acordar tarde, é <strong>bancar o bom moço e liquidar o próprio aporte antes de sobrar algo no final do mês</strong>.",
        "tip": "<strong>Regra:</strong> o conforto frito de uma rotina lotada impede você de estancar o sangramento invisível do seu caixa de ativos."
      },
      {
        "ic": "mask",
        "t": "Arrogância (ego + ignorância)",
        "emph": "Arrogância",
        "b": "Usar o canudo de ouro e o ego gigantesco para disfarçar a completa indigência sobre relatórios contábeis. A fórmula é letal: <strong>o excesso de confiança apoiado sobre o nada resulta num meteoro rasgando a sua conta em pedaços</strong>. Quem acha que o mercado tem pena, amanhece pobre e orgulhoso no asfalto.",
        "tip": "<strong>Sinal de alerta:</strong> fechar os ouvidos para um consultor e investir achando que o gênio é infalível é pedir para entregar o castelo ao inimigo.",
        "warn": true
      }
    ]
  },
  "ch09-pague-se-primeiro": {
    "cards": [
      {
        "ic": "key",
        "t": "Pague-se Primeiro",
        "emph": "Pague-se Primeiro",
        "b": "Não trate o seu investimento como gorjeta da sobra. Ele é o primeiro abutre que voa na carcaça do salário antes de todo mundo; os bancos e boletos são a segunda divisão. <strong>Imponha a si mesmo o tributo inegociável na linha de frente</strong>, rasgando o sangue da prioridade para a sua milícia de papéis valorizados.",
        "tip": "<strong>Prática:</strong> o aporte não se discute; ele cai direto e programado da conta base como um raio no dia em que o chefe aperta o botão do TED."
      },
      {
        "ic": "spark",
        "t": "A Pressão como Combustível",
        "emph": "Pressão",
        "b": "Roubar dos próprios ativos para salvar o jantar cancela o jogo inteiro. Deixe o desespero do aluguel pendente bater no peito: é essa <strong>fome cortante e esse desconforto bruto que acionarão as manivelas de emergência do seu cérebro, obrigando-o a inventar um novo canal de dinheiro vivo</strong> na madrugada.",
        "tip": "<strong>Modelo mental:</strong> use as dívidas para apertar o seu pescoço taticamente; a genialidade nunca acordou descansando num colchão quentinho."
      },
      {
        "ic": "steps",
        "t": "Autodisciplina",
        "emph": "Autodisciplina",
        "b": "Sem o chicote interno batendo na própria espinha todo santo dia, o livro mais brilhante do mundo afunda no tédio. Dominar o ego fraco e domesticar o impulso infantil de queimar caixa são <strong>os fatores ditatoriais mais selvagens entre os vencedores implacáveis e o resto da sala ruidosa</strong>.",
        "tip": "<strong>Sinal de alerta:</strong> falhar na blindagem pessoal no dia 1 de cada mês não anula o mercado, anula você."
      }
    ]
  },
  "ch10-comecar": {
    "cards": [
      {
        "ic": "mountain",
        "t": "Uma Razão Maior que a Realidade",
        "emph": "Razão Maior",
        "b": "Um porquê pálido gera o recuo na primeira trincheira suja de sangue. O motor não avança pelo glamour do dólar; avança porque o terror agudo de <strong>terminar dependendo da compaixão e engolir as ordens alheias com o joelho em terra na velhice queima mais forte do que a preguiça letárgica do presente</strong>.",
        "tip": "<strong>Como aplicar:</strong> arranque o verniz das palavras e anote a ira bruta e inegociável que faz você levantar dessa cadeira."
      },
      {
        "ic": "constellation",
        "t": "Poder da Escolha & da Associação",
        "emph": "Associação",
        "b": "Cada dez centavos e cada cinco minutos torrados formam a cédula de votação do seu futuro cimentado ou triturado. Expurque a praga de reclamões do seu perímetro e <strong>alugue um espaço VIP no círculo invisível onde tubarões debatem fortunas, porque o pensamento se arrasta em manada e você imita de quem foge ou caça</strong>.",
        "tip": "<strong>Modelo mental:</strong> o nível do jogo é puxado pelo adversário e pelo aliado do lado; a mediocridade ao redor rebaixa o cérebro rapidamente à temperatura morna local."
      },
      {
        "ic": "steps",
        "t": "Comece Pequeno, mas Comece",
        "emph": "Comece",
        "b": "Devorar biblioteca sobre mercado e estagiar em planilhas teóricas acaba na mais covarde masturbação acadêmica. Arrume um troco ridículo, compre a primeira pedra microscópica e acione o risco real: <strong>o suor do medo vivo fará pelas suas conexões cerebrais aquilo que duas mil horas de MBA enlatado não ousaram fazer</strong>.",
        "tip": "<strong>Sinal de alerta:</strong> não se afogue no mar da paralisia pelo excesso da teoria inútil. Puxe o gatilho; pule e entenda a gravidade só após a queda inicial.",
        "warn": true
      }
    ]
  }
}
```
"""

with open(r"C:\Users\User\.gemini\antigravity\scratch\biblioteca\_kit_preview\gemini_in\batch_7_out.md", "a", encoding="utf-8") as f:
    f.write(content + "\n")
