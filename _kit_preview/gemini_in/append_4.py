import sys

content = """
=== quem-pensa-enriquece ===
```json
{
  "ch01-o-poder-do-pensamento": {
    "cards": [
      {
        "ic": "lens",
        "t": "O Pensamento é Coisa Tangível",
        "emph": "Tangível",
        "b": "Um pensamento não é uma nuvem de fumaça poética, é um <strong>ímã de chumbo que puxa a matéria física para perto</strong>. Quando acoplado a um propósito violento e à teimosia cega, ele deixa de ser uma ideia no vácuo e se torna um decreto arquitetônico da sua realidade.",
        "tip": "<strong>Modelo mental:</strong> trate as suas ideias como matéria-prima. Se você pensar no lixo, construirá um castelo de lixo."
      },
      {
        "ic": "mask",
        "t": "O \"Não Posso\" como Sentença de Morte",
        "emph": "Sentença de Morte",
        "b": "Cada vez que o seu cérebro sussurra \"é impossível\", ele não está analisando a probabilidade; ele está <strong>assinando o decreto de execução da sua oportunidade</strong>. A limitação não mora na economia ou na gravidade do mercado, mora na covardia do portão que você mesmo trancou na sua mente.",
        "tip": "<strong>Sinal de alerta:</strong> preste atenção na boca: o 'não posso' é o alarme de incêndio de que o cérebro desistiu de procurar a resposta.",
        "warn": true
      },
      {
        "ic": "key",
        "t": "A Oportunidade Entra pela Porta dos Fundos",
        "emph": "Porta dos Fundos",
        "b": "O pote de ouro não chega tocando fanfarra e vestindo smoking. A oportunidade tem a mania cruel de <strong>se disfarçar de tragédia, infortúnio e humilhação completa</strong>. É no meio do caos que o prêmio gordo se esconde de quem não tem estômago para virar a pedra suja.",
        "tip": "<strong>Como aplicar:</strong> na próxima derrota humilhante, engula o choro e vasculhe os destroços: é ali que a semente do equivalente vantajoso está enterrada."
      }
    ]
  },
  "ch02-o-desejo": {
    "cards": [
      {
        "ic": "spark",
        "t": "Desejo Escaldante ≠ Vontade Fraca",
        "emph": "Desejo Escaldante",
        "b": "A diferença entre querer ser rico e exigir o dinheiro é a diferença entre a brisa e o furacão. Uma vontade fraca não acorda cedo e não sobrevive ao primeiro 'não'. Apenas uma <strong>obsessão doentia que queima os botes de fuga</strong> força o universo a ceder a passagem.",
        "tip": "<strong>Regra:</strong> corte as rotas de retirada. Se você puder fugir de volta para o conforto, o seu desejo nunca vai virar um incêndio."
      },
      {
        "ic": "steps",
        "t": "Os 6 Passos para Converter Desejo em Ouro",
        "emph": "6 Passos",
        "b": "Hill não quer poesia, quer contrato: fixe o valor exato, defina o que vai dar em troca, coloque o dia letal, escreva o roteiro, leia isso até engasgar de manhã e de noite. O <strong>ritual converte o desejo vago num comando militar que domina o seu sistema nervoso central</strong>.",
        "tip": "<strong>Prática:</strong> rasgue o 'quero muito dinheiro'. Escreva 'quero R$ 100.000,00 no dia 31 de dezembro vendendo a solução X' e fixe no teto do quarto."
      },
      {
        "ic": "mask",
        "t": "Você Pode Enganar o Fracasso",
        "emph": "Enganar o Fracasso",
        "b": "Quando as pernas tremerem, a sua mente vai sussurrar que você é uma fraude. O desejo escaldante serve exatamente para <strong>intimidar o pessimismo interno e manter a máquina rodando</strong> até que o subconsciente acredite na mentira e a transformem em lucro no caixa.",
        "tip": "<strong>Modelo mental:</strong> a fé cega não é ignorância, é o adubo tático que sustenta o músculo até a realidade decidir se curvar."
      }
    ]
  },
  "ch03-fe-e-autossugestao": {
    "cards": [
      {
        "ic": "bulb",
        "t": "Fé: O Químico Mental",
        "emph": "Químico Mental",
        "b": "A fé não tem relação com banco de igreja. Ela é o elemento químico que <strong>fundido ao desejo transforma um pensamento comum numa ogiva nuclear</strong> capaz de perfurar o subconsciente Infinito. Sem a vibração da crença inabalável, o seu mantra é só um papagaio repetindo palavras mortas.",
        "tip": "<strong>Como aplicar:</strong> pare de recitar metas como um zumbi. Se a emoção brutal não estiver engatada na palavra, a porta do subconsciente continua trancada."
      },
      {
        "ic": "wave",
        "t": "O Perigo da Fé Negativa",
        "emph": "Fé Negativa",
        "b": "O cérebro é um escravo cego: ele obedece à mesma química quer você tenha a crença inabalável no sucesso, quer você tenha pavor do desastre. Quem jura que vai quebrar e vive a emoção do fracasso antecipado, <strong>ordena ao cérebro que construa meticulosamente o abismo</strong>.",
        "tip": "<strong>Sinal de alerta:</strong> o medo crônico é apenas a sua autossugestão orando pela desgraça. Corte a emissão dessa frequência.",
        "warn": true
      },
      {
        "ic": "bubble",
        "t": "Autossugestão Prática",
        "emph": "Autossugestão",
        "b": "O subconsciente só se curva aos comandos misturados com emoção visceral. A autossugestão é a técnica de invadir a sala de máquinas da própria mente e <strong>injetar as ordens de enriquecimento usando a paixão como cavalo de Troia</strong>. O que você repete friamente não vinga.",
        "tip": "<strong>Prática:</strong> feche a porta, visualize o dinheiro na sua mão até o coração bater mais forte e só então faça a sua afirmação."
      }
    ]
  },
  "ch04-conhecimento-especializado": {
    "cards": [
      {
        "ic": "sword",
        "t": "O Conhecimento só é Poder em Ação",
        "emph": "Poder em Ação",
        "b": "Ter uma enciclopédia na cabeça sem uma máquina de execução não vale um centavo no mercado. Conhecimento é poder apenas e <strong>estritamente quando amarrado a um plano brutal de ação para gerar riqueza</strong>. A erudição estática é o troféu dos professores falidos.",
        "tip": "<strong>Modelo mental:</strong> se o seu diploma não está se transformando num serviço que o mercado compra, ele é só uma moldura cara."
      },
      {
        "ic": "link",
        "t": "Compre o Conhecimento dos Outros",
        "emph": "Conhecimento dos Outros",
        "b": "Henry Ford esmagou os advogados no tribunal avisando que apertava um botão e trazia o maior especialista da área à sua mesa. Você não precisa entupir o crânio com cada detalhe técnico da Terra; o <strong>jogo dos deuses é ser o maestro que aluga o cérebro hiper-focado de quem sabe mais</strong>.",
        "tip": "<strong>Regra:</strong> não estude o que você pode comprar. Fazer a gestão de mentes especialistas é a verdadeira especialidade dos trilionários."
      },
      {
        "ic": "steps",
        "t": "Educação Nunca Termina",
        "emph": "Educação",
        "b": "\"Educo\" vem de tirar de dentro, desenvolver. A linha de montagem da escola convenceu a massa de que o estudo morre no dia da formatura. Quem engole a pílula de que \"já sabe tudo\" assina o atestado de óbito; o <strong>rico constrói o império sendo um viciado incurável e vitalício em saber como o jogo novo funciona</strong>.",
        "tip": "<strong>Prática:</strong> se faz um ano que você não devora um conhecimento útil para a sua arena financeira, você já começou a apodrecer no cargo."
      }
    ]
  },
  "ch05-imaginacao": {
    "cards": [
      {
        "ic": "bulb",
        "t": "O Laboratório da Mente",
        "emph": "Laboratório",
        "b": "A oficina onde cada império da Terra foi primeiro desenhado em fumaça antes de se tornar aço. A imaginação não é divagação romântica; é o <strong>espaço de teste onde o intelecto amarra o conhecimento velho e fabrica o dinheiro novo</strong> que mudará a sua conta amanhã.",
        "tip": "<strong>Como aplicar:</strong> não tente inventar a roda do zero. Pegue dois conceitos mortos e bata um de frente com o outro no laboratório mental."
      },
      {
        "ic": "fork",
        "t": "Imaginação Sintética × Criativa",
        "emph": "Sintética × Criativa",
        "b": "A Sintética empilha e recicla ideias velhas em arranjos novos — o <em>feijão com arroz</em> dos lucros do dia a dia. A Criativa é a <strong>antena monstruosa que fura a nuvem e capta inspiração pura direto do infinito</strong>. A primeira se fortalece no uso braçal; a segunda pisca apenas na clareza absoluta e silenciosa do desejo.",
        "tip": "<strong>Modelo mental:</strong> pare de rezar por um milagre criativo. Bote a imaginação sintética para suar organizando as ideias antigas, e a criativa dará as caras."
      },
      {
        "ic": "spark",
        "t": "As Ideias como Dinheiro Vivo",
        "emph": "Ideias",
        "b": "A Coca-Cola nasceu de uma chaleira e de um pedaço de papel que o farmacêutico vendeu por trocados, mas foi a imaginação do comprador que injetou o gás no império. <strong>O capital real não é a nota verde impressa no banco; é a ideia afiada capaz de magnetizar esse dinheiro</strong>.",
        "tip": "<strong>Para refletir:</strong> dinheiro é o que menos falta no mercado. O que falta é a mente audaciosa e estruturada capaz de sequestrá-lo para o próprio cofre."
      }
    ]
  },
  "ch06-planejamento-organizado": {
    "cards": [
      {
        "ic": "layers",
        "t": "A Cristalização do Desejo",
        "emph": "Cristalização",
        "b": "Sonhar não compra tijolos. O planejamento organizado é o <strong>funil de chumbo que força o vapor quente do seu desejo a virar a água pesada do dinheiro real</strong>. Sem o rascunho sujo de um plano para o dia de amanhã, o seu 'Desejo' inteiro não passa de uma farsa psicológica para se sentir bem.",
        "tip": "<strong>Sinal de alerta:</strong> o plano perfeito que nunca arranca perde para o plano imperfeito executado brutalmente numa terça-feira."
      },
      {
        "ic": "wave",
        "t": "Derrota Temporária ≠ Fracasso Absoluto",
        "emph": "Derrota Temporária",
        "b": "Quando o plano ruir com um estouro, a primeira reação do idiota é deitar e chamar de fracasso definitivo. A mente treinada sabe que a explosão é apenas o <strong>recado do mercado de que aquela rota específica estava apodrecida</strong>. Volte à mesa, risque o papel, crie o plano B e levante a cabeça.",
        "tip": "<strong>Regra:</strong> o fracasso só ganha a certidão de óbito permanente se você assinar a desistência. Todo o resto é um dado tático para ajustar a mira.",
        "warn": true
      },
      {
        "ic": "person",
        "t": "Liderança pela Concordância",
        "emph": "Liderança",
        "b": "O modelo do chefe-ditador morreu a pauladas, enterrado por Napoleão e Mussolini. A liderança que arrasta os cérebros do século 20 exige consentimento e simpatia. <strong>Você não empurra as pessoas para a trincheira com chicote; você domina a mente delas fazendo com que desejem lutar a sua guerra</strong>.",
        "tip": "<strong>Como aplicar:</strong> estude incansavelmente os interesses da sua equipe. O mestre junta as fomes individuais na direção do banquete da empresa."
      }
    ]
  },
  "ch07-decisao-e-procrastinacao": {
    "cards": [
      {
        "ic": "clock",
        "t": "O Hábito de Decidir Rápido",
        "emph": "Decidir Rápido",
        "b": "Análises confirmam: quem engorda o banco decide rápido como o raio e <strong>muda de ideia lentamente, quando a pedra se quebra</strong>. O pobre congela na hesitação e altera o plano a cada sopro do vento. A firmeza da decisão é o bisturi que expulsa a procrastinação que estava roendo o seu destino.",
        "tip": "<strong>Prática:</strong> condicione-se a bater o martelo. A indecisão paralisa o fluxo; uma escolha razoável e violenta bate a paralisia do cálculo perfeito."
      },
      {
        "ic": "shield",
        "t": "Feche os Ouvidos",
        "emph": "Feche os Ouvidos",
        "b": "O oxigênio mais farto e barato do mundo é a opinião não solicitada de vizinhos e parentes assustados. Se você abrir o cofre da sua mente para a mediocridade alheia, <strong>eles plantarão as próprias sementes de pavor nas suas entranhas</strong> e liquidarão o seu projeto no ventre.",
        "tip": "<strong>Sinal de alerta:</strong> mantenha a boca trancada sobre os seus planos absolutos. Compartilhe estratégias só com as mentes de elite da sua mesa.",
        "warn": true
      },
      {
        "ic": "mountain",
        "t": "Coragem Desmedida",
        "emph": "Coragem",
        "b": "Assinar a Declaração de Independência americana com a corda da forca balançando ao fundo não foi delírio juvenil; foi a <strong>decisão forjada em titânio de gente disposta a sangrar pela ideia</strong>. A sua meta não pode ser um capricho, precisa valer a pena o risco de ser incinerado pelo caminho.",
        "tip": "<strong>Modelo mental:</strong> quem entra na roda de negociação deixando uma brecha de recuo já perdeu. Assuma o risco inteiro."
      }
    ]
  },
  "ch08-persistencia-e-mastermind": {
    "cards": [
      {
        "ic": "mountain",
        "t": "A Resistência ao Desgaste",
        "emph": "Resistência",
        "b": "O talento morre e o gênio cansa, mas a persistência é o <strong>motor a diesel blindado que engole o fracasso temporário, cospe a fumaça no rosto das críticas e tritura os obstáculos no silêncio da madrugada</strong>. É a vacina que você injeta nas veias do plano para ele não definhar diante dos primeiros 'nãos'.",
        "tip": "<strong>Como aplicar:</strong> não conte o sucesso pelos dias brilhantes. O teste de ouro é a capacidade de fazer a tarefa suja quando a vontade zerou."
      },
      {
        "ic": "link",
        "t": "A Química do Mastermind",
        "emph": "Mastermind",
        "b": "Não é <em>networking</em> de bebedeira. O Mastermind é a fusão de dois ou mais cérebros afiados girando em ressonância obsessiva por um único fim. <strong>A fricção dessas mentes não cria a soma dos indivíduos, mas desperta um \"terceiro cérebro\" invisível e letal</strong>. É a alavanca da potência pura.",
        "tip": "<strong>Prática:</strong> sente na mesa pessoas com fomes parecidas, mas com armas complementares. Uma bala disparada sozinha não vence a guerra."
      },
      {
        "ic": "eye",
        "t": "Afastando a Sombra do Medo",
        "emph": "Sombra do Medo",
        "b": "A persistência triturará o asfalto sob você; a mente de grupo estenderá o trilho na sua frente. E o medo será a ferrugem que corrói os dois se você o aceitar de volta. <strong>A pobreza é uma doença mental atraída por quem vibra na miséria. Defenda o cofre contra a negatividade com fúria psicopata</strong>.",
        "tip": "<strong>Regra:</strong> não existe neutralidade mental. Ou você aduba o foco feroz no dinheiro, ou o mato crescerá empurrando o pavor."
      }
    ]
  }
}
```

=== startup-enxuta ===
```json
{
  "ch01-o-que-e-uma-startup": {
    "cards": [
      {
        "ic": "gap",
        "t": "Incerteza Extrema",
        "emph": "Incerteza Extrema",
        "b": "Uma startup não é uma miniatura da Apple ou da Ford. É uma instituição humana encurralada no inferno de <strong>tentar fabricar um produto novo para um cliente fantasma em um terreno sem mapa</strong>. Planejamento rígido, que salva a megacorporação, é o veneno exato que mata uma startup.",
        "tip": "<strong>Modelo mental:</strong> se você tem certeza de quem vai comprar, não é startup, é apenas um negócio. A startup é desenhada para a cegueira."
      },
      {
        "ic": "layers",
        "t": "O Empreendedorismo é Gestão",
        "emph": "É Gestão",
        "b": "O mito do gênio de moletom que quebra tudo no dormitório mascara o tédio necessário da realidade: a startup exige <strong>um novo manual de contabilidade, medição e rigor gerencial que tolere o caos</strong>, mas que puna severamente o achismo solto de inovadores irresponsáveis.",
        "tip": "<strong>Sinal de alerta:</strong> não use a palavra 'inovação' para mascarar falta de disciplina. O caos criativo não preenche o fluxo de caixa.",
        "warn": true
      },
      {
        "ic": "mountain",
        "t": "O Custo do Fracasso Perfeito",
        "emph": "Fracasso Perfeito",
        "b": "Ficar três anos no porão arquitetando o software intocável, e só depois descobrir que nenhum ser humano na Terra quer usá-lo. O crime maior não é construir o produto torto, <strong>é derreter milhares de horas num planejamento épico que nunca encontrou a navalha letal do mercado real</strong>.",
        "tip": "<strong>Como aplicar:</strong> pare de polir a Ferrari no escuro. Traga o rascunho de barro para a luz e veja se alguém, pelo menos, pisa no freio."
      }
    ]
  },
  "ch02-aprendizado-validado": {
    "cards": [
      {
        "ic": "target",
        "t": "A Única Métrica que Importa",
        "emph": "A Única Métrica",
        "b": "Num ambiente de caos, o dinheiro é colateral e a pesquisa é viciada. O seu único salário na etapa inicial chama-se <strong>aprendizado validado: testar a sua visão doentiamente na carne de clientes reais</strong> e coletar a prova inegável do que eles compram e do que eles ignoram.",
        "tip": "<strong>Modelo mental:</strong> cada centavo gasto sem testar o comportamento prático e mudo do cliente é dinheiro rasgado."
      },
      {
        "ic": "lens",
        "t": "Experimento, Não Enquete",
        "emph": "Experimento",
        "b": "O que o cliente diz no grupo focal é areia movediça; o que ele faz quando a carteira está na mesa é granito puro. <strong>Transforme o próprio produto inicial num sensor que capta as decisões de sangue dos usuários</strong>, não num questionário onde todos mentem tentando ser educados.",
        "tip": "<strong>Prática:</strong> recuse entrevistas rasas. Você quer medir a conversão crua de cliques, botões e cartões de crédito. O silêncio do cartão grita a verdade."
      },
      {
        "ic": "mask",
        "t": "A Farsa do Sucesso sem Método",
        "emph": "Farsa do Sucesso",
        "b": "\"Veja como estamos famosos nos blogs\". Métricas de vaidade são a morfina do empreendedor. Elas inflam o ego no painel de controle, mas <strong>escondem o abismo de que a retenção do produto é miserável e ninguém volta a comprar</strong>. Se não prova causa e efeito no bolso, é cortina de fumaça.",
        "tip": "<strong>Regra:</strong> afaste o veneno da contabilidade que aplaude curtidas e pageviews. O aprendizado validado exige números que custam dor e suor."
      }
    ]
  },
  "ch03-o-ciclo-construir-medir-aprender": {
    "cards": [
      {
        "ic": "spiral",
        "t": "A Engrenagem do Feedback",
        "emph": "Engrenagem do Feedback",
        "b": "A pulsação cardíaca de qualquer startup que recusa a morte: <strong>transformar rapidamente as ideias no código, empurrar para o mercado medir a reação, engolir os dados amargos e decidir se acelera ou se gira o timão para o outro lado</strong>. O ciclo deve ser vicioso e maníaco.",
        "tip": "<strong>Como aplicar:</strong> o cronômetro manda no jogo. Reduza drasticamente o tempo entre ter a ideia maldita na lousa e analisar o choro do cliente."
      },
      {
        "ic": "spark",
        "t": "O Salto de Fé (Leap of Faith)",
        "emph": "Salto de Fé",
        "b": "Escondidas no porão de todo plano de negócios bonito, existem as premissas letais: \"as pessoas querem isso\" e \"elas pagarão tanto\". O gestor implacável mapeia <strong>quais são as hipóteses que, se afundarem, arrastam a empresa inteira para a cova</strong>, e testa isso antes de trocar as cortinas do escritório.",
        "tip": "<strong>Modelo mental:</strong> pare de gastar munição onde você já tem certeza. Identifique a dúvida mais aterrorizante do projeto e vá direto à jugular dela."
      },
      {
        "ic": "fork",
        "t": "O Reverso da Lógica",
        "emph": "Reverso da Lógica",
        "b": "Em vez de trancar a porta, construir tudo, medir o impacto e aprender da pior forma, inverta o vetor. <strong>Decida primeiro qual a prova brutal que você precisa extrair do mundo real e monte o produto mais ridículo e rápido capaz de arrancar esse dado específico</strong> da multidão.",
        "tip": "<strong>Prática:</strong> a pergunta não é 'o que eu vou construir amanhã?'; é 'que conhecimento exato eu preciso que a rua me ensine hoje?'."
      }
    ]
  },
  "ch04-o-produto-minimo-viavel-mvp": {
    "cards": [
      {
        "ic": "sword",
        "t": "MVP: O Desconforto Tático",
        "emph": "Desconforto Tático",
        "b": "O MVP não é um produto defeituoso feito por incompetência; é <strong>uma arapuca tática fabricada de propósito para medir e extrair inteligência máxima gastando a munição mínima</strong>. Se você não sente vergonha da cara que o produto tem quando foi para a rua, você poliu demais e lançou tarde demais.",
        "tip": "<strong>Como aplicar:</strong> remova sem dó qualquer botão, função ou estética que não ajude a testar a principal dúvida de negócio."
      },
      {
        "ic": "play",
        "t": "MVP de Vídeo / Concierge",
        "emph": "Vídeo / Concierge",
        "b": "Dropbox testou se as pessoas queriam pastas mágicas subindo apenas um vídeo falso do produto. A Zappos tirava foto do sapato na vitrine e mandava pelos correios sem ter um depósito de tijolos. <strong>Simule a mágica na superfície e faça o esqueleto sangrar manualmente no fundo</strong> antes de programar o monstro todo.",
        "tip": "<strong>Regra:</strong> não automatize o desconhecido. Fazer o processo brutal de forma braçal com 10 clientes ensina o que você não deveria automatizar para 10.000."
      },
      {
        "ic": "eye",
        "t": "O Risco da Ilusão da Qualidade",
        "emph": "Ilusão da Qualidade",
        "b": "O engenheiro chora abraçado ao código puro e recusa o lançamento para \"não ofender a marca\". É uma histeria suicida: <strong>não existe qualidade num produto glorioso e invisível que nenhum cliente vivo vai usar</strong>. O mercado define o que é útil, não as réguas teóricas da equipe técnica.",
        "tip": "<strong>Sinal de alerta:</strong> o perfeccionismo que bloqueia o contato inicial não é excelência, é terror agudo da rejeição do mercado disfarçado de nobreza técnica.",
        "warn": true
      }
    ]
  },
  "ch05-inovacao-contabil-metricas": {
    "cards": [
      {
        "ic": "scale",
        "t": "Métricas de Vaidade × Métricas Acionáveis",
        "emph": "Métricas Acionáveis",
        "b": "Se a curva no gráfico sobe furiosamente e você não faz ideia de qual botão você apertou para que isso acontecesse, você está abraçado com métricas de vaidade. <strong>Métricas acionáveis revelam causa clara; acessíveis expõem os dados em inglês simples e auditáveis deixam a equipe rasgar o relatório para verificar</strong>.",
        "tip": "<strong>Como aplicar:</strong> o indicador de ouro responde a uma única pergunta nua e crua: 'se eu fizer a ação X amanhã, este número exato vai mudar?'"
      },
      {
        "ic": "fork",
        "t": "Testes A/B: A Guerra dos Dados",
        "emph": "Testes A/B",
        "b": "Pare com as reuniões de achismos. O método científico espanca o ego. Coloque a versão azul e a vermelha na arena simultaneamente e <strong>deixe que a mão do cliente decida quem leva o dinheiro e quem vai para a vala</strong>. O teste A/B arranca a política da empresa e entrega a coroa ao usuário cego.",
        "tip": "<strong>Prática:</strong> o cliente não vota com a boca, vota com o botão. Em qualquer divergência pesada de design, deixe o experimento sangrar na tela dividida."
      },
      {
        "ic": "lens",
        "t": "Coortes: O Raio-X do Motor",
        "emph": "Coortes",
        "b": "A métrica global mascara a retenção porca, cobrindo o lixo com dinheiro de anúncios novos. O raio-X não falha: <strong>acompanhe pequenos esquadrões de clientes mês a mês; se os clientes de janeiro compram menos em março do que o coorte antigo comprava</strong>, você não está voando, você está escondendo o rombo.",
        "tip": "<strong>Modelo mental:</strong> não olhe as compras totais. Divida a audiência na guilhotina mensal; se a retenção não melhorar na nova safra, o produto piorou."
      }
    ]
  },
  "ch06-pivotar-ou-perseverar": {
    "cards": [
      {
        "ic": "pivot",
        "t": "O Pivô: Desistir sem Fraquejar",
        "emph": "Pivô",
        "b": "Pivotar não é gritar fracasso e jogar as chaves do escritório no lago. <strong>É manter o pé esquerdo fincado ferozmente no que você aprendeu com os mortos e girar o canhão noventa graus com a tática ajustada</strong>. É o atalho brutal que evita que a sua startup vire o piloto suicida de um navio furado no deserto.",
        "tip": "<strong>Prática:</strong> pareceu um muro inquebrável por meses seguidos? Troque o alvo (pivô de cliente) ou a pivô de função, mas não morra teimoso na mesma pedra."
      },
      {
        "ic": "mask",
        "t": "O Cemitério dos 'Quase-vivos'",
        "emph": "Quase-vivos",
        "b": "O pesadelo não é queimar a empresa numa explosão catastrófica. O verdadeiro terror é <strong>entrar num estado de zumbi contínuo</strong>, crescendo o suficiente para bancar as pizzas, mas afundado na irrelevância total, consumindo os anos da sua vida e as desculpas sem parar, sem a coragem de girar a rota e sem a piedade de morrer.",
        "tip": "<strong>Sinal de alerta:</strong> o vale dos zumbis é o preço pago pelos fundadores que recusam admitir que as métricas acionáveis decretaram o fim daquele ciclo.",
        "warn": true
      },
      {
        "ic": "sword",
        "t": "A Decisão Letal",
        "emph": "Decisão Letal",
        "b": "A coragem para perseverar quando o universo ri do seu produto, ou o frio no estômago para rasgar a planta e pivotar quando a teoria falhou miseravelmente na rua. <strong>Marque reuniões periódicas sangrentas onde essa é a única pauta da mesa</strong>. Nenhuma métrica fará o giro sozinha sem a mão pesada do capitão.",
        "tip": "<strong>Regra:</strong> as métricas apenas disparam a buzina; a decisão de enfiar o pé no freio ou de capotar o carro precisa do instinto brutal do piloto."
      }
    ]
  },
  "ch07-os-motores-de-crescimento": {
    "cards": [
      {
        "ic": "link",
        "t": "O Motor Viscoso (Sticky)",
        "emph": "Viscoso",
        "b": "O foco de retenção letal das redes sociais e bancos: entrar é legal, sair dá um trabalho desgraçado. A máquina inteira depende que <strong>a velocidade macabra do abandono de usuários (churn) seja rigorosamente inferior à força de aquisição</strong>. Se a porta de trás estiver escancarada, a publicidade não salva.",
        "tip": "<strong>Como aplicar:</strong> o motor viscoso colapsa no churn. Engessar o cliente ao sistema até doer na espinha é mais importante do que focar em convites chamativos."
      },
      {
        "ic": "spark",
        "t": "O Motor Viral",
        "emph": "Viral",
        "b": "Cada cliente que usa o seu projeto infecta um colega de forma invisível. Não é \"boca a boca\" romântico, é <strong>o produto sendo a própria isca durante o uso normal</strong> (ex.: \"enviado do meu iPhone\"). O segredo militar é focar insanamente em fazer o coeficiente viral quebrar a barreira do \"maior do que 1\".",
        "tip": "<strong>Modelo mental:</strong> marketing com motor viral é um veneno letal contra a publicidade paga. Você arranca lucros quando o contágio substitui o custo em vendas."
      },
      {
        "ic": "target",
        "t": "O Motor Pago",
        "emph": "Pago",
        "b": "A matemática sangrenta da guerra fria comercial. Se cada novo guerreiro adquirido te traz US$ 50 ao longo da vida e custou apenas US$ 10 no leilão do Facebook, <strong>você encontrou a máquina de multiplicar o dinheiro</strong>. Gire as peças do produto para reduzir os custos e enfie a lenha no LTV (valor do ciclo de vida) da audiência.",
        "tip": "<strong>Prática:</strong> focar a fúria simultaneamente no custo de aquisição e no preço da esteira. Se a margem empatar, feche as portas antes de acelerar."
      }
    ]
  }
}
```
"""

with open(r"C:\Users\User\.gemini\antigravity\scratch\biblioteca\_kit_preview\gemini_in\batch_7_out.md", "a", encoding="utf-8") as f:
    f.write(content + "\n")
