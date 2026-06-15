import sys

content = """
=== garra ===
```json
{
  "ch01-o-que-e-garra": {
    "cards": [
      {
        "ic": "spark",
        "t": "Garra = Paixão + Perseverança",
        "emph": "Paixão + Perseverança",
        "b": "Paixão não é a euforia que dura um fim de semana; é <strong>ancorar-se na mesma direção por anos a fio</strong>. Perseverança é apanhar do tédio, dos platôs e dos fracassos dolorosos, sacudir a poeira e voltar ao trabalho. Quando o fogo cruza com o chumbo, nasce a garra.",
        "tip": "<strong>Modelo mental:</strong> paixão é constância, não calor. Pergunte a si mesmo: 'eu ainda estarei obcecado por isso daqui a cinco anos?'"
      },
      {
        "ic": "target",
        "t": "A Escala de Garra",
        "emph": "Escala de Garra",
        "b": "O teste de fogo que separa amadores de lendas. A pontuação que previu quem suportaria o treinamento brutal de West Point não mediu músculos nem QI de gênio; mediu a capacidade de <strong>não recuar quando a dor aperta</strong>.",
        "tip": "<strong>Prática:</strong> em maratonas de longo prazo, pare de otimizar para ser brilhante. Otimize primeiro para não pedir para sair."
      },
      {
        "ic": "mountain",
        "t": "Maratona, não Sprint",
        "emph": "Maratona",
        "b": "Intensidade é o combustível mais barato e abundante do mundo; qualquer amador tem de sobra. A verdadeira prova de fogo é o <strong>compromisso que se recusa a morrer</strong> quando a empolgação da novidade evapora e só sobra o peso do trabalho repetitivo.",
        "tip": "<strong>Regra:</strong> quem fica na mesa, leva o jogo. A maior parte do sucesso extraordinário é pura resistência obstinada."
      }
    ]
  },
  "ch02-talento-nao-e-destino": {
    "cards": [
      {
        "ic": "lens",
        "t": "Viés Contra o Esforço",
        "emph": "Viés Contra o Esforço",
        "b": "Dizemos em alto e bom som que premiamos quem trabalha duro, mas no escuro da alma humana idolatramos o talento natural. Ocupamos o pedestal com falsos deuses porque <strong>ocultar o suor faz a obra parecer pura mágica</strong> — e a sociedade quer aplaudir o espetáculo, não o treinamento.",
        "tip": "<strong>Sinal de alerta:</strong> não se deixe enganar pela pose de facilidade. Por trás de toda leveza genial, há um oceano de esforço bruto invisível.",
        "warn": true
      },
      {
        "ic": "bulb",
        "t": "O Mito do Gênio",
        "emph": "Mito do Gênio",
        "b": "Rotular um vencedor de 'gênio' é o nosso mecanismo de defesa mais covarde. É a desculpa perfeita que <strong>nos isenta de tentar competir</strong>. Sem as horas de sangue e disciplina, o talento mais espetacular do mundo morre apenas como uma semente não germinada.",
        "tip": "<strong>Modelo mental:</strong> fuja da palavra 'gênio'. Ela apaga as madrugadas em claro e a disciplina militar que constroem a grandeza."
      },
      {
        "ic": "steps",
        "t": "Talento = Velocidade, não Teto",
        "emph": "Velocidade",
        "b": "O talento não define o seu limite máximo de grandeza; ele apenas dita <strong>com que velocidade você arranca na linha de partida</strong>. A linha de chegada, o campeonato e o legado dependem exclusivamente da brutalidade do seu esforço ao longo do percurso.",
        "tip": "<strong>Como aplicar:</strong> olhe para o talento como o carro e para o esforço como o acelerador. Você é quem controla a pressão no pedal."
      }
    ]
  },
  "ch03-as-duas-equacoes-do-esforco": {
    "cards": [
      {
        "ic": "scale",
        "t": "O Esforço Conta Duas Vezes",
        "emph": "Conta Duas Vezes",
        "b": "O talento multiplicado pelo esforço cria a habilidade. Mas a habilidade multiplicada pelo <strong>esforço de novo</strong> cria a realização estrondosa. O talento participa de um lado da equação; o esforço impulsiona tudo, garantindo que o seu trabalho duro renda lucros exponenciais.",
        "tip": "<strong>Regra:</strong> não confie na vantagem inicial. É o esforço somado ao tempo que compõe os verdadeiros juros do sucesso."
      },
      {
        "ic": "layers",
        "t": "Hierarquia de Objetivos",
        "emph": "Hierarquia",
        "b": "Uma pirâmide de ferro: na base, mil táticas descartáveis; no meio, estratégias sólidas; no topo absoluto, a <strong>estrela polar que não muda nunca</strong>. Pessoas com garra brutal submetem todas as pequenas vitórias e derrotas a esse propósito de vida inegociável.",
        "tip": "<strong>Como aplicar:</strong> audite sua vida. Para cada meta diária, faça a pergunta letal: 'isto me aproxima ou me afasta do meu topo?'"
      },
      {
        "ic": "key",
        "t": "Firme no Topo, Flexível Embaixo",
        "emph": "Firme no Topo",
        "b": "Descartar um método falido não é fraqueza, é inteligência tática; mas rasgar o seu sonho de topo no primeiro soco na cara é a definição clássica de covardia. O grande mestre troca a ferramenta sem piscar, mas <strong>jamais recua do alvo principal</strong>.",
        "tip": "<strong>Prática:</strong> mude a rota quando a ponte cair, mas nunca esqueça o continente que você jurou conquistar."
      }
    ]
  },
  "ch04-interesse": {
    "cards": [
      {
        "ic": "spark",
        "t": "O Paradoxo da Paixão",
        "emph": "Paradoxo",
        "b": "A mentira moderna diz que a paixão deve cair do céu como um raio, pronta e perfeita. A verdade é que o interesse é <strong>cozido em fogo brando</strong>; ele só cria raízes e engrossa o tronco depois que você já está afundado até o pescoço na prática e no estudo da coisa.",
        "tip": "<strong>Sinal de alerta:</strong> ficar paralisado esperando a 'paixão da vida' surgir do nada é a receita certeira para morrer amador.",
        "warn": true
      },
      {
        "ic": "lens",
        "t": "Descobrir → Desenvolver → Aprofundar",
        "emph": "Aprofundar",
        "b": "Você passeia para descobrir, engaja para desenvolver e mergulha nas trincheiras para aprofundar. O especialista não se entedia com a repetição; ele encontra no microdetalhe um <strong>fascínio magnético que o novato simplesmente não consegue enxergar</strong>.",
        "tip": "<strong>Modelo mental:</strong> a novidade rasa diverte; a complexidade profunda de um mesmo assunto é o que vicia o verdadeiro mestre."
      },
      {
        "ic": "person",
        "t": "O Papel do Encorajamento",
        "emph": "Encorajamento",
        "b": "Antes do chicote da disciplina entrar em cena, tem que haver o parque de diversões. A liberdade para errar, fuçar e se apaixonar pelo processo é a <strong>faísca indispensável</strong>. Apoiar o início lúdico é garantir que o chumbo da prática dura tenha alicerce emocional.",
        "tip": "<strong>Regra:</strong> comece pela diversão pura. A disciplina espartana precoce mata o interesse antes de ele aprender a respirar."
      }
    ]
  },
  "ch05-pratica-deliberada": {
    "cards": [
      {
        "ic": "target",
        "t": "Os 4 Requisitos da Prática Deliberada",
        "emph": "4 Requisitos",
        "b": "Você atira num alvo que ainda não consegue acertar, foca com uma intensidade quase homicida, apanha do feedback corretivo impiedoso e repete o ciclo ajustando os erros. Não é prazeroso; é uma <strong>máquina de moer ego e fabricar excelência absoluta</strong>.",
        "tip": "<strong>Como aplicar:</strong> caçar o seu ponto fraco até sangrar. Praticar o que você já domina é masturbação mental, não treino."
      },
      {
        "ic": "wave",
        "t": "Prática Deliberada × Flow",
        "emph": "Prática Deliberada",
        "b": "Na prática deliberada, você espreme o cérebro, erra feio e sofre — é o treino na lama. No estado de <em>flow</em>, você executa no palco, voando sem atrito e sem pensar. As duas não competem: <strong>o suor feio de hoje compra a fluidez deslumbrante de amanhã</strong>.",
        "tip": "<strong>Modelo mental:</strong> pare de procurar prazer durante o treinamento. A dor no treino é o preço exato do show de gala na arena."
      },
      {
        "ic": "steps",
        "t": "Vire Hábito",
        "emph": "Hábito",
        "b": "A prática de alta performance dói na alma. Para não depender da frágil força de vontade, você tem que <strong>concretar a prática na mesma hora e no mesmo lugar</strong> todos os dias. O atrito de começar derrete e a repetição cega toma o volante.",
        "tip": "<strong>Prática:</strong> amarre o treino a um gatilho inegociável. A dor da excelência se torna suportável quando vira rotina automatizada."
      }
    ]
  },
  "ch06-proposito-e-esperanca": {
    "cards": [
      {
        "ic": "constellation",
        "t": "Propósito: Servir aos Outros",
        "emph": "Servir",
        "b": "O interesse egocêntrico acende o motor, mas só o propósito cravado no <strong>serviço à humanidade</strong> impede que você abandone o carro no meio do deserto. A diferença brutal entre empilhar tijolos como um condenado e construir uma catedral que desafiará os séculos.",
        "tip": "<strong>Como aplicar:</strong> levante a cabeça do tijolo e encare o vitral. Se o seu suor não melhora a vida de ninguém, ele perderá a graça."
      },
      {
        "ic": "leaf",
        "t": "Esperança = Crescimento + Otimismo",
        "emph": "Crescimento + Otimismo",
        "b": "A esperança da garra despreza a reza passiva. Ela é a convicção violenta de que <strong>'eu posso e vou melhorar essa droga'</strong>. É a fusão da crença de que as habilidades são elásticas com a teimosia de enxergar cada fracasso como um tropeço temporário e isolado.",
        "tip": "<strong>Sinal de alerta:</strong> o pessimismo paralisa a ação. Troque imediatamente o 'eu sou burro' por 'eu ainda não descobri como fazer'."
      },
      {
        "ic": "mountain",
        "t": "Anti-Desamparo: Reescreva o Revés",
        "emph": "Anti-Desamparo",
        "b": "O desamparo aprendido sussurra que o universo o odeia e que lutar é inútil. A resposta com garra rasga essa narrativa: o soco na cara não é um atestado de incompetência divina, mas um <strong>problema específico com uma causa mecânica e resolvível</strong>.",
        "tip": "<strong>Modelo mental:</strong> o fracasso é um dado no painel, não uma tatuagem na testa. Leia a informação, conserte o erro e acelere.",
        "warn": true
      }
    ]
  },
  "ch07-cultivar-de-fora": {
    "cards": [
      {
        "ic": "person",
        "t": "Parenting Sábio: Exigente E Acolhedor",
        "emph": "Exigente E Acolhedor",
        "b": "O líder forjador de garra atua em dois polos simultâneos: ele estica a sua capacidade até rasgar, enquanto oferece um <strong>abrigo emocional inabalável</strong>. A tirania esmaga a alma; a fofura permissiva gera covardia. O crescimento brutal exige o chicote do padrão e o colo do apoio.",
        "tip": "<strong>Regra:</strong> não reduza a barra para facilitar a vida, mas garanta que a pessoa sinta que você está com ela na trincheira."
      },
      {
        "ic": "target",
        "t": "A Regra do Difícil",
        "emph": "Regra do Difícil",
        "b": "O pacto da família Duckworth é lei marcial: escolha uma pedreira para quebrar, estude e treine, mas <strong>não ouse abandonar o barco no meio da tempestade</strong>. A desistência num dia ruim é covardia; sair de cabeça erguida no fim do ciclo, porque tentou tudo, é maturidade.",
        "tip": "<strong>Prática:</strong> tranque a porta de saída. Comprometa-se com uma atividade árdua por seis meses inteiros e corte a opção de desistir antes."
      },
      {
        "ic": "constellation",
        "t": "Cultura de Garra",
        "emph": "Cultura de Garra",
        "b": "A força de vontade individual é uma pilha alcalina fuleira. Se você quer garra de verdade, infiltre-se numa tribo cuja <strong>identidade exala fanatismo por terminar o que começa</strong>. A pressão psicológica do grupo injeta resiliência nas suas veias por puro contágio cultural.",
        "tip": "<strong>Modelo mental:</strong> o seu ambiente é o seu destino. Se a sua matilha é fraca, você vai uivar baixo. Ande com leões."
      }
    ]
  }
}
```

=== irmaos-karamazov ===
```json
{
  "ch01-os-tres-irmaos": {
    "cards": [
      {
        "ic": "layers",
        "t": "Personagens-Tese",
        "emph": "Personagens-Tese",
        "b": "Cada Karamázov caminha como uma <strong>ideia encarnada que sangra e respira</strong>. Dmitri queima na paixão, Ivan congela no ceticismo brilhante, e Aliócha transborda a fé que perdoa. Dostoiévski não escreve panfletos; ele os joga numa arena para provar que uma filosofia só tem valor quando testada pelo caos da vida.",
        "tip": "<strong>Modelo mental:</strong> não procure um porta-voz de ideias prontas. A genialidade da polifonia é dar as armas mais letais para todos os lados."
      },
      {
        "ic": "triangle",
        "t": "Smerdiákov — A Quarta Faceta",
        "emph": "Quarta Faceta",
        "b": "O filho escondido que varre o chão é a ponte letal entre a teoria e a tragédia. Quando Ivan decreta friamente que 'tudo é permitido', <strong>é Smerdiákov quem empunha a arma e esmaga o crânio</strong>. Ele é o retrato pavoroso do que acontece quando a elite tira as travas morais da base.",
        "tip": "<strong>Sinal de alerta:</strong> quem defende a anarquia num sofá de veludo será devorado pelo monstro que criou nas ruas.",
        "warn": true
      },
      {
        "ic": "spiral",
        "t": "O 'Karamázovismo'",
        "emph": "Karamázovismo",
        "b": "Um excesso obsceno de vida, um furacão de sensualidade pura e fúria que não conhece coleira. O karamázovismo é <strong>uma energia vulcânica que ilumina santuários ou incinera cidades inteiras</strong>, dependendo exclusivamente das mãos de quem a domina. É a força bruta antes da forma.",
        "tip": "<strong>Para refletir:</strong> não tente castrar a sua intensidade. O segredo é construir diques de chumbo para que a água gere energia em vez de destruir a vila."
      }
    ]
  },
  "ch02-dmitri-mitia-paixao": {
    "cards": [
      {
        "ic": "sword",
        "t": "Madona × Sodoma",
        "emph": "Madona × Sodoma",
        "b": "O inferno de Dmitri é olhar para dentro e encontrar a lama e o céu habitando o mesmo coração. Ele sente um êxtase genuíno diante da pureza da Madona, mas <strong>se arrasta para os becos imundos de Sodoma sem um pingo de hipocrisia</strong>. A contradição humana em seu estado mais cru e assustador.",
        "tip": "<strong>Prática:</strong> pare de fingir que você é uma nota só. Admitir a podridão interna é o primeiro passo para não ser governado por ela."
      },
      {
        "ic": "scale",
        "t": "A Justiça que Erra",
        "emph": "Justiça",
        "b": "Os tribunais dos homens vestem togas solenes para esmagar a pessoa errada com precisão absoluta. Dmitri é atirado na fogueira por um assassinato que não cometeu. Mas o livro recusa o chororô panfletário: <strong>o moedor de carne da injustiça torna-se o forno que purifica a sua alma</strong>.",
        "tip": "<strong>Modelo mental:</strong> a vida raramente paga a conta certa no momento exato. A grandeza mora em transmutar a pedrada cega em fundação sólida."
      },
      {
        "ic": "leaf",
        "t": "Redenção pelo Sofrimento Aceito",
        "emph": "Sofrimento Aceito",
        "b": "No sonho alucinante do bebê chorando de frio, Dmitri é atravessado pelo raio da culpa universal. Ele não se vitimiza mais. Ao <strong>abraçar a cruz por um crime alheio</strong>, ele aniquila o egoísmo antigo e encontra a redenção divina que a liberdade burguesa jamais lhe daria.",
        "tip": "<strong>Regra:</strong> o ressentimento apodrece a alma; o sofrimento abraçado voluntariamente quebra as correntes do ego."
      }
    ]
  },
  "ch03-ivan-intelecto-rebeliao": {
    "cards": [
      {
        "ic": "bulb",
        "t": "'Devolver o Bilhete'",
        "emph": "Devolver o Bilhete",
        "b": "Ivan não se esconde no ateísmo raso; ele peita Deus. Ele aceita o ingresso do universo, mas, ao ver a etiqueta de preço estampada com o choro de uma única criança torturada, ele <strong>recusa o bilhete com nojo ético</strong>. É o soco no estômago da teologia que te obriga a suar frio.",
        "tip": "<strong>Como aplicar:</strong> não fuja de um argumento devastador só porque ele dói. As convicções de chumbo são forjadas enfrentando a faca no pescoço."
      },
      {
        "ic": "fork",
        "t": "Ideias têm Consequências",
        "emph": "Consequências",
        "b": "O brilhantismo intelectual de Ivan forja o punhal; a mediocridade de Smerdiákov executa o golpe. Dostoiévski esfrega na cara dos pensadores a verdade sangrenta de que o niilismo de salão, quando vaza para a sarjeta, <strong>resulta em cadáveres reais e violência pura</strong>.",
        "tip": "<strong>Sinal de alerta:</strong> você é moralmente cúmplice dos monstros que decidem agir em nome das teorias vazias que você gosta de aplaudir.",
        "warn": true
      },
      {
        "ic": "spiral",
        "t": "Ivan e o Diabo",
        "emph": "Ivan e o Diabo",
        "b": "O demônio que assombra Ivan na febre da madrugada não é um monstro de chifres, mas um cavalheiro medíocre que vomita de volta o próprio niilismo do filósofo. A lógica fria que o justificava <strong>vira uma jaula de loucura</strong>. O cérebro que corta a própria raiz apodrece.",
        "tip": "<strong>Modelo mental:</strong> sustentar uma visão de mundo onde nada importa é um jogo que ninguém aguenta jogar até o fim sem enlouquecer."
      }
    ]
  },
  "ch04-aliocha-fe-compaixao": {
    "cards": [
      {
        "ic": "leaf",
        "t": "Fé Encarnada, Não Argumentada",
        "emph": "Fé Encarnada",
        "b": "Aliócha não puxa a espada retórica para duelar com Ivan; ele entrega o rosto e o <strong>beija nos lábios</strong>. A resposta do romance para o cinismo mais genial da história humana não é um teorema vencedor, mas a presença física, silenciosa e esmagadora do amor em ação.",
        "tip": "<strong>Prática:</strong> às vezes, a resposta certa para uma acusação ácida não é o contra-ataque lógico, mas o silêncio denso de quem permanece ao lado."
      },
      {
        "ic": "person",
        "t": "O Discurso da Pedra",
        "emph": "Discurso da Pedra",
        "b": "No funeral de uma criança, Aliócha não promete a revolução. Ele crava na alma daqueles meninos a ideia de que uma única e radiante lembrança de bondade na infância é o <strong>tijolo de ouro capaz de salvar um homem adulto da barbárie</strong> no futuro. A memória salva a ética.",
        "tip": "<strong>Regra:</strong> construa memórias indestrutíveis de dignidade e amor para as crianças; elas usarão isso como colete salva-vidas na vida adulta."
      },
      {
        "ic": "bubble",
        "t": "Compaixão sem Julgamento",
        "emph": "Compaixão",
        "b": "O abismo de compreensão de Aliócha o impede de levantar o martelo de juiz. Ele olha para o pai devasso, para o irmão assassino em potencial e para a prostituta, e <strong>enxerga a fenda sagrada que ainda respira debaixo da lama</strong>. Ele cura a ferida porque se recusa a atirar a primeira pedra.",
        "tip": "<strong>Modelo mental:</strong> você perde o direito de acessar o interior de uma pessoa no exato instante em que decide pendurar um rótulo moral na testa dela."
      }
    ]
  },
  "ch05-smerdiakov-parricidio": {
    "cards": [
      {
        "ic": "mask",
        "t": "Culpa Difusa",
        "emph": "Culpa Difusa",
        "b": "Smerdiákov ergue o pilão, mas a força gravitacional do assassinato puxa todos os Karamázov. Ivan deu o salvo-conduto filosófico e Dmitri deu a pólvora do ódio explícito. O autor quebra o espelho do individualismo e grita que <strong>o veneno mortal foi fabricado pela família inteira</strong>.",
        "tip": "<strong>Como aplicar:</strong> olhe para os desastres do seu ecossistema corporativo ou familiar: quem puxou o gatilho, quem forneceu a arma e quem olhou para o lado?"
      },
      {
        "ic": "gap",
        "t": "O Executor sem Ideia Própria",
        "emph": "Ideia Própria",
        "b": "Smerdiákov é o vazio assustador de uma mente sem bússola, que engole o manual do 'tudo é permitido' sem sofrer a angústia ética de Ivan. Ele mata com o <strong>pragmatismo limpo e macabro de quem limpa uma vidraça</strong>, provando que o vazio moral na ponta da linha é a pior catástrofe.",
        "tip": "<strong>Sinal de alerta:</strong> o maior perigo não é o intelectual rebelde que sente o peso do que diz, mas o fantoche estúpido que executa a regra ao pé da letra.",
        "warn": true
      },
      {
        "ic": "sword",
        "t": "Parricídio como Símbolo",
        "emph": "Símbolo",
        "b": "Rachar o crânio do velho Fiódor não é só uma briga suja por herança e mulher. É o machado descendo no pescoço do próprio <strong>Deus-Pai e de toda a ordem arquitetônica do universo</strong>. Se você queima a fundação divina, o assassinato se torna apenas uma manobra administrativa.",
        "tip": "<strong>Para refletir:</strong> toda rebelião absoluta contra a autoridade invisível termina cedo ou tarde num banho de sangue visível."
      }
    ]
  },
  "ch06-grande-inquisidor": {
    "cards": [
      {
        "ic": "scale",
        "t": "Liberdade × Pão/Segurança",
        "emph": "Liberdade × Pão",
        "b": "O Inquisidor aprisiona o próprio Cristo sob o argumento de que a humanidade é miserável demais para aguentar a liberdade. Ele oferece o pacto do diabo: <strong>troque a sua consciência por pão quente e segurança absoluta</strong>. A massa assustada vende a alma barato para não ter que pensar.",
        "tip": "<strong>Modelo mental:</strong> cuidado com os salvadores da pátria que oferecem conforto total em troca do seu direito inegociável de decidir e errar."
      },
      {
        "ic": "triangle",
        "t": "As Três Tentações Invertidas",
        "emph": "Três Tentações",
        "b": "Milagre, pão e autoridade esmagadora. O Inquisidor acusa Cristo de ter errado no deserto ao rejeitar as únicas três forças que mantêm o gado humano manso. <strong>Dominar o rebanho pelo estômago, pelo circo mágico e pela tirania do dogma</strong> é o manual perpétuo de todo poder absoluto.",
        "tip": "<strong>Como aplicar:</strong> se uma organização te seduz pelo prato cheio, pelo espetáculo e te proíbe de duvidar, você não encontrou a paz; encontrou a coleira."
      },
      {
        "ic": "leaf",
        "t": "O Beijo — A Resposta sem Palavras",
        "emph": "Beijo",
        "b": "O Inquisidor faz o discurso totalitário mais brilhante da literatura humana. Cristo o escuta em silêncio de pedra, aproxima-se e <strong>beija os lábios murchos do velho genocida</strong>. O choque rompe as grades da lógica; a misericórdia pura aniquila a engenharia do poder sem disparar um tiro.",
        "tip": "<strong>Regra:</strong> não lute na mesma arena que um demagogo usando as palavras dele. O gesto sublime quebra a dialética ao meio."
      }
    ]
  },
  "ch07-zossima-amor-ativo": {
    "cards": [
      {
        "ic": "leaf",
        "t": "Amor Ativo × Amor em Sonho",
        "emph": "Amor Ativo",
        "b": "O amor em sonho exige aplausos, chora na primeira ingratidão e quer salvar o mundo pelo Instagram. O <strong>amor ativo é trabalho sujo e implacável</strong> — é lavar feridas sem plateia, engolir patadas e amar um ser humano insuportável no dia a dia. É a disciplina que transforma a lama em luz.",
        "tip": "<strong>Sinal de alerta:</strong> se você depende de palmas ou gratidão para continuar fazendo o bem, você é apenas um turista moral.",
        "warn": true
      },
      {
        "ic": "link",
        "t": "Responsabilidade Universal",
        "emph": "Responsabilidade Universal",
        "b": "O dogma fulminante de Zóssima crava que <strong>'cada um de nós é culpado por tudo e por todos'</strong>. Não existe isolamento na teia da dor humana. Enquanto alguém sofrer no escuro, o seu dever de resgate está em aberto. A culpa universal não paralisa; ela é a bomba atômica da solidariedade.",
        "tip": "<strong>Modelo mental:</strong> pare de lavar as mãos com o 'eu não tenho nada a ver com isso'. Na contabilidade de Zóssima, toda dívida é nossa."
      },
      {
        "ic": "person",
        "t": "Não Julgar",
        "emph": "Não Julgar",
        "b": "Você não consegue ver a trincheira de sangue invisível na qual o outro está perdendo a guerra, então abaixe a maldita caneta do julgamento. Condenar é o refúgio seguro dos preguiçosos; <strong>acolher exige a força brutal de quem entende que todos estão quebrados</strong>, inclusive quem acolhe.",
        "tip": "<strong>Prática:</strong> quando a língua coçar para emitir uma sentença moral sobre um conhecido, morda-a. Substitua o juiz pelo paramédico."
      }
    ]
  },
  "ch08-teodiceia-sofrimento": {
    "cards": [
      {
        "ic": "scale",
        "t": "A Teodiceia — O Nó Insolúvel",
        "emph": "Nó Insolúvel",
        "b": "O escândalo do bebê torturado é o muro de aço onde toda a teologia barata quebra os dentes. Ivan esfrega o sangue dos inocentes no rosto do céu e não aceita harmonias celestiais como desculpa. <strong>Não tente explicar a dor injusta com panfletos bonitinhos</strong>; é o insulto supremo à vítima.",
        "tip": "<strong>Como aplicar:</strong> quando alguém estiver no inferno de um luto absurdo, cale a boca teológica e chore junto. Explicações só servem para ofender a dor alheia."
      },
      {
        "ic": "key",
        "t": "O Livre-Arbítrio como Preço do Amor",
        "emph": "Preço do Amor",
        "b": "Deus poderia ter criado um relógio de marionetes felizes, mas preferiu um mundo de homens livres. A <strong>liberdade radical é o preço de sangue para que o amor não seja programado</strong>. Sem a navalha da escolha real que permite o assassinato, não haveria o milagre do perdão verdadeiro.",
        "tip": "<strong>Modelo mental:</strong> entenda que o risco monstruoso do mal aberto é a única condição que dá valor real a uma ação de bondade."
      },
      {
        "ic": "bulb",
        "t": "A Réplica Existencial — Não Lógica",
        "emph": "Réplica Existencial",
        "b": "Dostoiévski percebeu que um argumento lógico não devolve a vida de uma criança. Por isso, a resposta do livro ao mal absoluto não é uma equação fria, mas a <strong>trajetória radiante de Aliócha</strong>. O mundo só fica menos intolerável quando alguém decide ser o portador físico da misericórdia.",
        "tip": "<strong>Prática:</strong> pare de tentar ganhar os debates sobre o sofrimento do mundo. A resposta é ser a própria mão que estanca o sangramento."
      }
    ]
  },
  "ch09-julgamento-redencao": {
    "cards": [
      {
        "ic": "scale",
        "t": "A Justiça que Erra o Fato",
        "emph": "Erra o Fato",
        "b": "O promotor discursa como um gênio, as testemunhas são coerentes, a plateia delira — e o veredicto condena um inocente. A guilhotina do júri é obcecada por fatos de superfície e <strong>absolutamente míope para o oceano escuro da alma humana</strong>. O teatro legal é só uma farsa coreografada.",
        "tip": "<strong>Sinal de alerta:</strong> desconfie de veredictos perfeitos construídos apenas com raciocínio lógico externo; a verdade do espírito nunca cabe nos autos.",
        "warn": true
      },
      {
        "ic": "leaf",
        "t": "O Pequenino — A Conversão de Dmitri",
        "emph": "Pequenino",
        "b": "Enquanto os advogados brigam por teses, Dmitri é implodido por dentro pelo choro de um bebê anônimo em um sonho. Ele desperta com as mãos em chamas de gratidão, <strong>abraçando a dor para saldar a dívida da humanidade inteira</strong>. O coração que se esmaga e se rende sempre vencerá a razão.",
        "tip": "<strong>Modelo mental:</strong> uma epifania espiritual genuína quebra as grades da lógica de sobrevivência e faz você aceitar o fardo com um sorriso no rosto."
      },
      {
        "ic": "mountain",
        "t": "A Sibéria como Graça",
        "emph": "Sibéria como Graça",
        "b": "Ir para a Sibéria quebrar pedras por vinte anos seria o inferno de qualquer homem livre, mas para o Dmitri purificado, é o altar da expiação gloriosa. Ele usará as correntes como prova do seu amor e do seu renascimento. <strong>A geada cortante será o bisturi que curará a sua alma de vez</strong>.",
        "tip": "<strong>Regra:</strong> não confunda aceitar estoicamente o fardo de um castigo com o papel frouxo da vítima; é a escolha suprema de usar o fogo para forjar caráter."
      }
    ]
  },
  "ch10-estrutura-simbolos": {
    "cards": [
      {
        "ic": "spiral",
        "t": "O Romance Polifônico",
        "emph": "Romance Polifônico",
        "b": "Esqueça o autor onisciente que dá lições de moral no fundo do palco. Dostoiévski empodera cada um de seus demônios com autonomia soberana. <strong>A verdade não sai da boca de um personagem</strong>; ela faísca do impacto caótico e sangrento do confronto entre eles. É um campo de batalha, não uma cartilha.",
        "tip": "<strong>Prática:</strong> preste atenção na fúria de cada voz isolada. A verdade complexa sobrevive nas cicatrizes dos debates inteiros."
      },
      {
        "ic": "eye",
        "t": "Os Símbolos em Pares",
        "emph": "Pares",
        "b": "Nada em Dostoiévski voa com uma asa só. O beijo libertador de Cristo confronta o fogo tirânico do Inquisidor; o corpo de Zóssima que fede à podridão enfrenta o milagre espiritual. <strong>Os opostos se canibalizam para rasgar as camadas do que é sagrado e do que é mundano</strong>, sem tréguas.",
        "tip": "<strong>Como aplicar:</strong> nunca isole um símbolo ou conceito do livro; pegue o seu oposto na história e veja a faísca que os dois soltam ao bater."
      },
      {
        "ic": "fork",
        "t": "Os Ensaios Encenados",
        "emph": "Ensaios Encenados",
        "b": "Teses filosóficas letais são colocadas dentro da carne e da rotina dos irmãos. Quando Ivan monta seu panfleto brilhante da Rebelião, o livro o faz <strong>engolir e viver a podridão teórica através de um surto psicótico real</strong>. Dostoiévski arrasta as abstrações pelos cabelos até a lama da vida.",
        "tip": "<strong>Modelo mental:</strong> as ideias não flutuam no vácuo; a biografia e os pesadelos de quem as defende são o gabarito final do teste de fogo."
      }
    ]
  }
}
```
"""
with open(r"C:\Users\User\.gemini\antigravity\scratch\biblioteca\_kit_preview\gemini_in\batch_7_out.md", "a", encoding="utf-8") as f:
    f.write(content + "\n")
