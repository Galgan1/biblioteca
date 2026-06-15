import sys
import json

content = """=== arte-da-seducao ===
```json
{
  "ch01-seducao-como-poder": {
    "cards": [
      {
        "ic": "spark",
        "t": "Poder por Atração",
        "emph": "Atração",
        "b": "A sedução nunca pressiona; ela desenha um <strong>vácuo irresistível de desejo</strong> que a vítima corre para preencher. É um jogo psicológico onde a paciência e a teatralidade fazem tudo parecer obra do destino, escondendo a trama racional por trás.",
        "tip": "<strong>Modelo mental:</strong> pense como um dramaturgo — a sedução exige um arco narrativo, nunca um avanço bruto."
      },
      {
        "ic": "eye",
        "t": "Foco na Carência do Outro",
        "emph": "Carência",
        "b": "O verdadeiro sedutor silencia o próprio ego para ouvir o que <strong>falta na alma do outro</strong> — a ferida aberta, a fantasia reprimida, o tédio de sempre. É só quando você mapeia essa carência que descobre qual máscara vestir para preenchê-la.",
        "tip": "<strong>Como aplicar:</strong> preste atenção àquilo que a pessoa mais reclama ou idealiza — aí está a fechadura da porta."
      },
      {
        "ic": "mask",
        "t": "A Sedução como Personagem",
        "emph": "Personagem",
        "b": "Você não aplica técnicas: você <strong>encarna uma promessa</strong> viva. A sinceridade crua entedia; o mistério, o drama e a ambiguidade fascinam. Toda resistência inicial da vítima não é um freio, mas a corda que dará tensão ao sim definitivo.",
        "tip": "<strong>Sinal de alerta:</strong> falar demais de si e exibir virtudes rápido é a morte do mistério.",
        "warn": true
      }
    ]
  },
  "ch02-tipos-sedutor-1": {
    "cards": [
      {
        "ic": "wave",
        "t": "Sereia e Libertino",
        "emph": "Sereia e Libertino",
        "b": "A Sereia projeta perigo e sensualidade, prometendo arrancar o outro do tédio seguro. O Libertino oferece um desejo tão incontrolável que faz a vítima <strong>sentir-se a única no mundo</strong>. Ambos vendem a fantasia da paixão devoradora e sem amarras.",
        "tip": "<strong>Prática:</strong> use esses papéis quando o alvo estiver sufocado pela rotina e precisar de intensidade."
      },
      {
        "ic": "constellation",
        "t": "Amante Ideal e Dândi",
        "emph": "Amante Ideal",
        "b": "O Amante Ideal apaga a si mesmo para <strong>refletir o sonho romântico</strong> da vítima, sustentando uma ilusão exaustiva. Já o Dândi transgride os papéis de gênero e as normas sociais, oferecendo o charme proibido da liberdade e da elegância andrógina.",
        "tip": "<strong>Como aplicar:</strong> o Amante Ideal espelha o desejo mais íntimo; o Dândi encanta quebrando as regras."
      },
      {
        "ic": "mask",
        "t": "O Erro de Cada Tipo",
        "emph": "Erro",
        "b": "Toda máscara exige mistério. Uma Sereia transparente vira caricatura vulgar; um Libertino que não sabe atuar vira apenas um predador. O fracasso maior acontece quando você <strong>projeta as suas próprias necessidades</strong> e esquece de ler as ilusões do outro.",
        "tip": "<strong>Sinal de alerta:</strong> impor a sua fantasia em vez de investigar a carência alheia é o carimbo do Anti-Sedutor.",
        "warn": true
      }
    ]
  },
  "ch03-tipos-sedutor-2": {
    "cards": [
      {
        "ic": "leaf",
        "t": "Natural e Coquete",
        "emph": "Natural",
        "b": "O Natural desarma a vítima com uma <strong>vulnerabilidade quase infantil</strong>, oferecendo ternura num mundo duro e cínico. A Coquete joga com o frio e o quente — a promessa adiada cria uma abstinência psicológica que vicia a vítima no jogo infinito da caça.",
        "tip": "<strong>Modelo mental:</strong> o Natural atrai porque não parece uma ameaça; a Coquete domina mantendo você com fome."
      },
      {
        "ic": "person",
        "t": "Encantador e Carismático",
        "emph": "Encantador",
        "b": "O Encantador direciona o foco 100% para você, fazendo-o <strong>sentir-se o centro do universo</strong> sem confrontar seus defeitos. O Carismático exala uma convicção interior quase mística, arrastando seguidores com a promessa inabalável de um sentido maior.",
        "tip": "<strong>Prática:</strong> seja Encantador para desarmar no um a um; seja Carismático para liderar e inspirar multidões."
      },
      {
        "ic": "constellation",
        "t": "A Estrela — Tela de Projeção",
        "emph": "Tela de Projeção",
        "b": "A Estrela não entrega respostas prontas — ela oferece uma <strong>superfície polida e enigmática</strong>. Ela recua e se esvazia para que o público pinte ali suas próprias fantasias. É a distância fabricada e o mistério absoluto que a tornam um ícone insubstituível.",
        "tip": "<strong>Sinal de alerta:</strong> revelar-se demais quebra a tela; a Estrela precisa da ausência para que a projeção aconteça.",
        "warn": true
      }
    ]
  },
  "ch04-anti-sedutor-vitimas": {
    "cards": [
      {
        "ic": "triangle",
        "t": "O Anti-Sedutor",
        "emph": "Anti-Sedutor",
        "b": "A pressa sufocante, o falar apenas de si e a carência desesperada são o <strong>veneno da sedução</strong>. A insegurança exige garantias e aniquila o jogo. Antes de adicionar qualquer artifício, você precisa podar o egoísmo e dar espaço para o outro respirar.",
        "tip": "<strong>Regra:</strong> o desejo morre na certeza absoluta. Plante ambiguidade e deixe que o vácuo trabalhe a seu favor.",
        "warn": true
      },
      {
        "ic": "eye",
        "t": "Ler a Carência da Vítima",
        "emph": "Carência da Vítima",
        "b": "Não tente aplicar a mesma técnica em portas diferentes. A chave é descobrir o que <strong>sangra na vida da pessoa</strong> — o medo do tempo, a rotina esmagadora ou a solidão disfarçada. Casanova não era um só: ele desenhava um personagem sob medida para cada vazio.",
        "tip": "<strong>Como aplicar:</strong> o que a pessoa mais critica no mundo revela exatamente o que ela desesperadamente procura."
      },
      {
        "ic": "person",
        "t": "Reconheça seu Próprio Perfil",
        "emph": "Próprio Perfil",
        "b": "Para nunca ser manipulado às cegas, você deve dissecar o <strong>seu próprio ponto fraco</strong>. Aquela fantasia que você jura odiar costuma esconder o buraco exato por onde um sedutor mestre pode invadir e dominar sua vontade. Conheça a sua fechadura.",
        "tip": "<strong>Pergunta-chave:</strong> qual é a carência que eu não conto para ninguém? É ali que a sua armadura quebra."
      }
    ]
  },
  "ch05-fase1-separar": {
    "cards": [
      {
        "ic": "fork",
        "t": "Aproximação Indireta",
        "emph": "Aproximação Indireta",
        "b": "O predador silencioso nunca anda em linha reta. Surja como um aliado neutro ou um contato casual para <strong>adormecer os alarmes de segurança</strong> do alvo. Ao não demonstrar interesse óbvio, você ganha passe livre para entrar na rotina e plantar a semente da atenção.",
        "tip": "<strong>Como aplicar:</strong> comece por um terceiro assunto em comum e recue antes do esperado. A vítima sentirá necessidade de puxá-lo de volta."
      },
      {
        "ic": "wave",
        "t": "Sinais Ambíguos (Quente e Frio)",
        "emph": "Sinais Ambíguos",
        "b": "Elogie com os olhos e congele com a postura. A contradição proposital bagunça a lógica da vítima, forçando-a a <strong>gastar energia mental decifrando você</strong>. Quem é previsível não ocupa espaço na mente; quem confunde a razão acende o fogo da obsessão.",
        "tip": "<strong>Modelo mental:</strong> misturar presença com um toque de desinteresse faz o outro trabalhar para reconquistar a sua atenção."
      },
      {
        "ic": "gap",
        "t": "Crie a Carência",
        "emph": "Crie a Carência",
        "b": "Faça a pessoa sentir que a vida dela é <strong>pobre e silenciosa demais</strong> sem a sua presença. Você entra como a prova social de um mundo mais brilhante. Quando ela perceber o contraste, o desejo de escapar da própria vida fará todo o trabalho duro por você.",
        "tip": "<strong>Regra:</strong> nunca mire em quem já se sente completo. O alvo perfeito precisa ter uma pequena insatisfação latejante.",
        "warn": true
      }
    ]
  },
  "ch06-fase2-penetrar": {
    "cards": [
      {
        "ic": "bubble",
        "t": "Espelhe e Isole",
        "emph": "Espelhe e Isole",
        "b": "Transforme-se num espelho perfeito dos valores e ritmos dela — um eco raro que <strong>dissolve qualquer defesa</strong>. Então, corte sutilmente as âncoras: afaste-a dos amigos e da velha rotina, puxando-a para o seu mundo fechado onde você é a única bússola.",
        "tip": "<strong>Sinal de alerta:</strong> na vida real, esse isolamento profundo e orquestrado é o alerta vermelho de uma relação abusiva.",
        "warn": true
      },
      {
        "ic": "eye",
        "t": "Insinuação: A Carta de Amor",
        "emph": "Insinuação",
        "b": "Não entregue uma declaração de amor embalada para presente. Use referências, gestos vagos e palavras pela metade, forçando a vítima a <strong>preencher as lacunas com a própria imaginação</strong>. Ela se torna coautora do jogo e amarra o próprio nó sem perceber.",
        "tip": "<strong>Como aplicar:</strong> deixe as entrelinhas gritarem. Quando a pessoa deduz o seu interesse sozinha, o impacto é devastador."
      },
      {
        "ic": "wave",
        "t": "Prazer e Dor — A Montanha-Russa",
        "emph": "Prazer e Dor",
        "b": "O céu constante gera tédio mortal. Você precisa alternar a doçura com um distanciamento cortante ou um leve ciúme calculado. Essa <strong>angústia de perder a recompensa</strong> sequestra o sistema nervoso da vítima, transformando uma atração simples numa dependência química.",
        "tip": "<strong>Modelo mental:</strong> o conforto emocional esfria o romance; a montanha-russa injeta a adrenalina que prende e vicia."
      }
    ]
  },
  "ch07-fase3-precipitar": {
    "cards": [
      {
        "ic": "spark",
        "t": "O Inesperado Reacende",
        "emph": "O Inesperado",
        "b": "Quando o brilho começar a desbotar na rotina, quebre o roteiro brutalmente. Uma viagem sem aviso, uma mudança drástica de humor ou um presente deslocado. A previsibilidade mata a sedução; o <strong>choque repentino devolve o comando</strong> para as suas mãos.",
        "tip": "<strong>Como aplicar:</strong> não avise, faça. O choque tático impede que a vítima se acostume a ter o controle do relacionamento."
      },
      {
        "ic": "gap",
        "t": "Ausência Estratégica",
        "emph": "Ausência Estratégica",
        "b": "No momento em que o interesse dela atingir o ápice, recue. A distância cria um <strong>vácuo desesperador</strong> que ela preencherá idealizando tudo em você. Sufocar com presença destrói o charme; saber a hora de desaparecer é o que torna o seu retorno um troféu.",
        "tip": "<strong>Regra:</strong> não confunda sumiço definitivo com recuo tático. O objetivo não é perder a vítima, é deixá-la faminta.",
        "warn": true
      },
      {
        "ic": "sword",
        "t": "Audácia Cronometrada",
        "emph": "Audácia",
        "b": "Quando a tensão estiver no limite e a vítima apenas hesitar, avance com uma <strong>agressividade fria e sem desculpas</strong>. Pedir permissão nessa hora é letal. A ousadia que corta o ar assume a culpa e empurra a relação para o clímax, libertando o outro de decidir.",
        "tip": "<strong>Como aplicar:</strong> não peça, aja. A liderança audaciosa e oportuna anula qualquer dúvida final que tenha restado."
      }
    ]
  },
  "ch08-fase4-o-tombo": {
    "cards": [
      {
        "ic": "leaf",
        "t": "Regressão e Ilusão",
        "emph": "Regressão e Ilusão",
        "b": "Conduza a vítima a um estado psicológico quase infantil de entrega, criando um porto seguro de ternura e cuidado exclusivo. Quando as barreiras adultas despencam, ela <strong>baixa a guarda completamente</strong> e mergulha na ilusão perfeita que você preparou.",
        "tip": "<strong>Sinal de alerta:</strong> se a pessoa o leva a depender exclusivamente dela, retirando a sua autonomia, o charme virou armadilha.",
        "warn": true
      },
      {
        "ic": "spark",
        "t": "O Golpe Final",
        "emph": "Golpe Final",
        "b": "O teatro inteiro só tem sentido se você souber a hora de fechar as cortinas. Não espere demais para que a tensão evapore, nem tão rápido que soe barato. É um <strong>movimento de pura precisão</strong> que materializa fisicamente todo o delírio construído.",
        "tip": "<strong>Prática:</strong> o encerramento nunca é uma longa conversa justificativa; é um ato físico, decisivo e avassalador."
      },
      {
        "ic": "gap",
        "t": "Evite o Anticlímax",
        "emph": "Anticlímax",
        "b": "O pior veneno da conquista é baixar as armas no dia seguinte. Se a rotina invadir o quarto e a mágica se dissipar, o desencanto trará o arrependimento instantâneo. O verdadeiro mestre <strong>retém um fragmento escuro de mistério</strong> para manter o jogo respirando.",
        "tip": "<strong>Regra:</strong> o relaxamento descuidado é a morte do encanto. Nunca se torne um livro completamente lido."
      }
    ]
  },
  "ch09-lente-analitica": {
    "cards": [
      {
        "ic": "eye",
        "t": "Nomeie a Dinâmica",
        "emph": "Nomeie",
        "b": "Quando você aprende a enxergar a ausência fria de um pretendente ou a distância calculada de um chefe como táticas de manual, a magia evapora. Dar nome à artimanha <strong>rasga o roteiro invisível</strong> e devolve a clareza e a autonomia das suas próprias escolhas.",
        "tip": "<strong>Modelo mental:</strong> entender como a influência é montada transforma você de marionete em espectador consciente."
      },
      {
        "ic": "mask",
        "t": "Marketing, Política e Liderança",
        "emph": "Marketing",
        "b": "O palco não é só a cama. O político Natural, o CEO Carismático e a marca de luxo que exige ser perseguida usam a mesmíssima engenharia do desejo. A sedução é o <strong>motor invisível do poder global</strong>, orquestrando desde compras impensadas até os rumos de um país.",
        "tip": "<strong>Como aplicar:</strong> pergunte-se o que a propaganda promete nas entrelinhas. Que vazio essa marca quer preencher?"
      },
      {
        "ic": "scale",
        "t": "O Uso Ético",
        "emph": "Uso Ético",
        "b": "Estudar a gramática do poder não transforma você num psicopata; transforma-o num ser humano blindado. A linha ética mora em não quebrar a alma alheia para alimentar o próprio ego. Use o mapa para <strong>reconhecer a armadilha e decidir</strong> se quer entrar no jogo ou não.",
        "tip": "<strong>Pergunta-chave:</strong> 'Qual fraqueza minha essa pessoa está iluminando?' Responder a isso é retomar o comando da sua vida.",
        "warn": true
      }
    ]
  }
}
```

=== conversas-cruciais ===
```json
{
  "ch01-conversa-crucial": {
    "cards": [
      {
        "ic": "triangle",
        "t": "As 3 Condições",
        "emph": "3 Condições",
        "b": "Apostas estratosféricas, opiniões que colidem de frente e uma carga emocional à beira do caos. Quando esses três rios se encontram, o cérebro entra em curto. A ironia macabra é que, quanto mais a conversa <strong>define o seu destino</strong>, pior você tende a agir nela.",
        "tip": "<strong>Sinal de alerta:</strong> sinta o corpo — suor frio, estômago travado e voz seca são os bipes de uma conversa crucial."
      },
      {
        "ic": "fork",
        "t": "As 3 Saídas Possíveis",
        "emph": "3 Saídas",
        "b": "Você pode calar e engolir o veneno, explodir e destruir a ponte, ou escolher o caminho estreito do diálogo franco. Apenas a terceira via <strong>salva o resultado sem matar a relação</strong>. O instinto manda atacar ou fugir; o diálogo exige uma escolha racional e consciente.",
        "tip": "<strong>Modelo mental:</strong> pare de escolher entre sinceridade brutal e covardia disfarçada de educação. Abrace a terceira via."
      },
      {
        "ic": "spark",
        "t": "Sequestro Emocional",
        "emph": "Sequestro Emocional",
        "b": "Diante de uma ameaça, seu sangue foge do córtex e irriga as pernas para você correr ou os punhos para bater. É biologia, não falha de caráter. Seu cérebro racional fica <strong>literalmente subnutrido e imbecilizado</strong> exatamente no segundo em que você precisa ser um diplomata.",
        "tip": "<strong>Prática:</strong> quando o sangue ferver, respire e pise no freio emocional antes de abrir a boca.",
        "warn": true
      }
    ]
  },
  "ch02-pool-de-significado": {
    "cards": [
      {
        "ic": "layers",
        "t": "Pool de Significado Comum",
        "emph": "Pool de Significado",
        "b": "Imagine um tanque no centro da mesa onde todos despejam ideias e medos. Um <strong>tanque cheio e compartilhado</strong> gera decisões em que todos acreditam. A violência empurra lixo para dentro dele; o silêncio tranca o fluxo. Ambas as rotas matam o oxigênio da equipe.",
        "tip": "<strong>Como aplicar:</strong> cada ideia exposta sem ataque é um depósito de ouro puro; cada silêncio omisso é um roubo à inteligência do grupo."
      },
      {
        "ic": "bulb",
        "t": "Começar pelo Coração",
        "emph": "Coração",
        "b": "Sob pressão brutal, seu objetivo oculto degrada em segundos: de resolver o problema, você passa a querer esmagar o outro ou salvar o próprio orgulho. Antes de aplicar técnicas brilhantes, você precisa <strong>resetar a própria intenção</strong> e amarrar os demônios do próprio ego.",
        "tip": "<strong>Pergunta-chave:</strong> 'A minha atitude de agora reflete o que eu realmente quero no final dessa história?'."
      },
      {
        "ic": "pivot",
        "t": "Recuse a Escolha do Tolo",
        "emph": "Escolha do Tolo",
        "b": "A armadilha suprema é acreditar na mentira trágica de que você precisa mutilar a amizade para cuspir a verdade. Troque o ou pelo e. O gênio do diálogo não se rende: ele exige descobrir como <strong>falar a dura verdade E manter a conexão intacta</strong>.",
        "tip": "<strong>Regra:</strong> repudie o 'vou ter que ser grosso'. Isso é preguiça mental para fugir de um diálogo maduro.",
        "warn": true
      }
    ]
  },
  "ch04-aprender-a-observar": {
    "cards": [
      {
        "ic": "eye",
        "t": "Visão Dupla: Conteúdo + Condições",
        "emph": "Visão Dupla",
        "b": "O mestre da conversa divide o olho: varre os fatos discutidos e, ao mesmo tempo, lê o termômetro do ar. O sinal vermelho pisca não pela dureza do tema, mas pela <strong>destruição silenciosa da segurança</strong> no olhar do outro. Quando o medo entra, a verdade sai.",
        "tip": "<strong>Modelo mental:</strong> conteúdo não machuca; o que fere as pessoas é a intenção sombria que elas leem nos seus olhos."
      },
      {
        "ic": "mask",
        "t": "Silêncio × Violência em Detalhe",
        "emph": "Silêncio × Violência",
        "b": "O sarcasmo refinado, o mudar de assunto e a omissão calculada são os disfarces finos do silêncio covarde. A rotulagem moralista, o corte agressivo e o deboche são os dentes da violência. Ambos, no fundo, são <strong>gritos de quem está apavorado</strong>, não atos de força.",
        "tip": "<strong>Sinal de alerta:</strong> trate o veneno verbal não como ofensa pessoal, mas como o sintoma claro de alguém que perdeu a segurança.",
        "warn": true
      },
      {
        "ic": "person",
        "t": "Seu Estilo sob Estresse",
        "emph": "Estilo sob Estresse",
        "b": "No caos, você ataca e domina ou foge para a caverna? Não conhecer a sua rota de fuga padrão é assinar um atestado de cegueira tática. Quando a pressão o sequestrar, você será <strong>engolido pelo seu próprio mecanismo de defesa</strong> se não tiver mapeado antes o seu gatilho.",
        "tip": "<strong>Como aplicar:</strong> olhe para a sua última briga feia. Aquela reação horrorosa é o seu piloto automático pedindo correção."
      }
    ]
  },
  "ch05-tornar-seguro": {
    "cards": [
      {
        "ic": "scale",
        "t": "Propósito + Respeito Mútuos",
        "emph": "Propósito + Respeito",
        "b": "Sem o escudo invisível do Propósito (estamos no mesmo barco) e do Respeito (eu o vejo como um igual), a conversa vira trincheira. O respeito é como oxigênio puro: você só repara quando ele some, e quando some, <strong>ninguém consegue respirar ou focar no assunto</strong>.",
        "tip": "<strong>Regra:</strong> travou tudo? Pare o debate técnico e reconstrua o elo do respeito imediato antes de prosseguir."
      },
      {
        "ic": "pivot",
        "t": "Contraste (Não-/Sim-)",
        "emph": "Contraste",
        "b": "É a anestesia antes do corte. Primeiro, você mata a paranoia dizendo com firmeza o que <strong>não pretende fazer</strong>. Depois, com o alvo desarmado, crava o que <strong>realmente quer</strong>. O contraste aterra a fantasia paranoica do interlocutor sem fazê-lo recuar um milímetro dos seus fatos.",
        "tip": "<strong>Como aplicar:</strong> 'Não estou dizendo que você errou de propósito. Estou dizendo que o processo quebrou.' Desarme e avance."
      },
      {
        "ic": "spiral",
        "t": "CRIB — Criar Propósito Mútuo",
        "emph": "Criar Propósito Mútuo",
        "b": "Quando as estratégias entrarem em choque frontal, cave mais fundo até achar a dor original. Comprometa-se a recuar, mapeie a intenção pura escondida atrás da teimosia alheia e <strong>invente uma terceira via</strong> superior. O brainstorming sem o propósito alinhado é só um campo de guerra.",
        "tip": "<strong>Modelo mental:</strong> pare de brigar sobre o 'como' e encontre a ponte escondida sobre o 'para quê'.",
        "warn": true
      }
    ]
  },
  "ch06-dominar-historias": {
    "cards": [
      {
        "ic": "spiral",
        "t": "O Caminho para a Ação",
        "emph": "Caminho para a Ação",
        "b": "Ninguém te irrita; você vê um fato e escreve um <strong>roteiro envenenado na própria cabeça</strong>. Esse filme barato gera a raiva, que dispara o soco ou o grito. Para recuperar o leme da própria alma, você tem que rebobinar a fita da ação brutal até os fatos crus.",
        "tip": "<strong>Sinal de alerta:</strong> o ressentimento mudo nunca é culpa do fato nu, mas do veneno que o seu roteirista interno pingou nele."
      },
      {
        "ic": "mask",
        "t": "As 3 Histórias Espertas",
        "emph": "Histórias Espertas",
        "b": "O ego aterrorizado inventa contos de fadas cínicos: o conto da Vítima pura (escondendo a própria sujeira), o do Vilão diabólico (apagando a humanidade do outro) e o do Impotente amarrado (justificando a inércia). São as grandes <strong>mentiras de absolvição barata</strong> da humanidade.",
        "tip": "<strong>Prática:</strong> quando você se pegar resmungando que 'não há nada a fazer', acenda a luz da honestidade brutal.",
        "warn": true
      },
      {
        "ic": "bulb",
        "t": "Questões Espertas",
        "emph": "Questões Espertas",
        "b": "O antiveneno da Vítima é admitir o próprio papel na bagunça. O exorcismo do Vilão é se forçar a perguntar por que um <strong>ser humano são, lógico e decente</strong> faria aquilo. A cura da Impotência é levantar da cadeira, engolir o vitimismo e fazer o que precisa ser feito.",
        "tip": "<strong>Pergunta-chave:</strong> 'Qual é a minha contribuição invisível para o desastre do qual tanto reclamo?'"
      }
    ]
  },
  "ch07-state": {
    "cards": [
      {
        "ic": "steps",
        "t": "O Método STATE",
        "emph": "STATE",
        "b": "Você despeja os fatos cirúrgicos, conta a sua narrativa de maneira nua, puxa o caminho mental do outro, usa um tom desarmado e empurra todos para o teste da realidade. A genialidade mora no fato de que não é um ataque; é uma <strong>investigação aberta liderada pela sua coragem</strong>.",
        "tip": "<strong>Regra:</strong> inicie pela pedra fria dos fatos. Histórias e opiniões vêm depois de o alicerce estar montado."
      },
      {
        "ic": "bulb",
        "t": "Fatos Primeiro, Conclusão Depois",
        "emph": "Fatos Primeiro",
        "b": "Se você arrombar a porta gritando que o outro é irresponsável, fechou os ouvidos dele antes de começar. Fatos são neutros, frios e irrefutáveis. Ao construir o caso em cima deles, você cria uma <strong>trilha lógica inquebrável</strong> que convida a outra mente a caminhar até a conclusão sozinha.",
        "tip": "<strong>Modelo mental:</strong> jogue os dados na mesa sem adjetivos. O drama afasta, a precisão nua convence.",
        "warn": true
      },
      {
        "ic": "leaf",
        "t": "Confiança + Humildade",
        "emph": "Confiança + Humildade",
        "b": "Falar manso sem ceder a espinha dorsal. É o equilíbrio brutal de quem sustenta uma tese pesada com a maciez de quem diz 'estou apenas concluindo que...'. Baixar a agressividade no tom de voz não diminui o conteúdo da verdade, <strong>apenas impede que ela vire uma granada defensiva</strong>.",
        "tip": "<strong>Como aplicar:</strong> não engula as palavras, apenas amacie o soco. Seja absoluto nos dados e humilde no tom."
      }
    ]
  },
  "ch08-ampp": {
    "cards": [
      {
        "ic": "wave",
        "t": "AMPP — Abrir a Porta",
        "emph": "AMPP",
        "b": "Pergunte ativamente, espelhe o desconforto que vê no rosto dele, parafraseie como se tentasse desesperadamente entender a lógica dele e, só na emergência, <strong>chute um palpite empático</strong> do que ele sente. É um interrogatório amoroso que força a ostra humana a se abrir.",
        "tip": "<strong>Prática:</strong> o espelhamento desarma o orgulho; use frases como 'Você me diz que está bem, mas seu corpo diz o oposto'."
      },
      {
        "ic": "bubble",
        "t": "ABC — Responder sem Brigar",
        "emph": "ABC",
        "b": "Rasgue o hábito infantil de procurar o erro primeiro. Celebre agressivamente a parte com a qual você concorda, construa o tijolo seguinte a partir daí e, só no fim, <strong>coloque a sua visão lado a lado, sem cancelar a do outro</strong>. Vocês brigam pelos 10% porque ignoram os 90%.",
        "tip": "<strong>Regra:</strong> jamais abra a boca com 'mas você está errado'. Comece pescando o pingo de verdade que há do outro lado."
      },
      {
        "ic": "key",
        "t": "Curiosidade Genuína",
        "emph": "Curiosidade Genuína",
        "b": "A técnica de escuta é um teatro patético sem o motor do interesse real. Diante de um ataque espumante de raiva ou de um silêncio tumular, não morda a isca do revide. <strong>Enxergue o pânico escondido</strong> e pergunte a si mesmo: o que quebrou a paz dessa alma?",
        "tip": "<strong>Modelo mental:</strong> raiva é medo vestido com uma armadura. Mire o canhão na fraqueza do medo, não no aço do escudo.",
        "warn": true
      }
    ]
  },
  "ch09-passar-a-acao": {
    "cards": [
      {
        "ic": "fork",
        "t": "Os 4 Métodos de Decisão",
        "emph": "4 Métodos",
        "b": "O comandante decreta, o consultor escuta e decide, o plenário vota a maioria e a equipe de elite sangra até o consenso absoluto. Escolher o processo antes de mergulhar no fogo da ação evita que as pessoas saiam maldizendo que foram <strong>enganadas pela tirania de um falso democrata</strong>.",
        "tip": "<strong>Como aplicar:</strong> reserve o consenso só para dilemas vitais. Usar o consenso para decidir a cor da parede é insanidade coletiva.",
        "warn": true
      },
      {
        "ic": "wrench",
        "t": "WWWF — Feche com Compromisso",
        "emph": "Feche com Compromisso",
        "b": "Uma epifania emocional que não gera um contrato de aço vira lixo esquecido. Defina: quem responde pela tarefa, qual é o osso específico a entregar, o carimbo da data e a hora sagrada de checar o avanço. Um plano não assinado <strong>evapora na fumaça da rotina da próxima segunda-feira</strong>.",
        "tip": "<strong>Sinal de alerta:</strong> conversas cruciais sem a ata rigorosa do 'quem faz o quê e quando' não passam de terapia amadora."
      },
      {
        "ic": "target",
        "t": "Diálogo ≠ Decisão",
        "emph": "Diálogo ≠ Decisão",
        "b": "Encher o reservatório de significados não lhe dá a obra pronta; apenas forja o tijolo. Acatar o delírio de que a equipe toda resolverá os males do mundo é um atestado de falência. A palavra 'nós', quando se trata de responsabilização bruta, <strong>é o exato sinônimo de 'ninguém'</strong>.",
        "tip": "<strong>Regra:</strong> saia do palco abraçado com o time, mas amarre o chicote da cobrança nas costas de um único responsável nomeado."
      }
    ]
  }
}
```
"""

with open(r"C:\Users\User\.gemini\antigravity\scratch\biblioteca\_kit_preview\gemini_in\batch_7_out.md", "w", encoding="utf-8") as f:
    f.write(content + "\n")
