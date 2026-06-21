import json

data = {
  "noites-brancas": {
    "ch01-noite-primeira-encontro": {
      "cards": [
        {"ic": "pin", "t": "O Cais das Ilusões", "emph": "Cais", "b": "A cidade vazia espelha a alma trancada do sonhador. <strong>Ele foge do contato real e caminha pelas ruas criando cenas imaginárias, evitando o atrito vivo com as pessoas.</strong> A geografia fria de São Petersburgo é o retrato físico de quem teme o amor na prática.", "tip": "<strong>Modelo mental:</strong> o isolamento costuma mascarar o pavor de lidar com emoções que não controlamos."},
        {"ic": "clock", "t": "O Tempo Suspenso", "emph": "Suspenso", "b": "A neblina noturna quebra a dureza do mundo operário e oferece uma trégua silenciosa. <strong>A noite branca dissolve a vigilância social e cria um palco provisório para confissões vulneráveis.</strong> O protagonista ganha coragem apenas nesse hiato onde a luz crua do sol não alcança.", "tip": "<strong>Para refletir:</strong> observe como a noite empresta coragem efêmera a quem vive se escondendo de dia."},
        {"ic": "triangle", "t": "Pacto com a Dor", "emph": "Pacto", "b": "A mulher impõe a amizade pura logo no primeiro esbarrão, e ele aceita assinar o contrato na hora. <strong>Ao jurar segurar a paixão para não assustá-la, ele engole uma promessa que vai rasgar seu peito nos dias seguintes.</strong> O acordo provisório contém o veneno da ruína.", "tip": "<strong>Sinal de alerta:</strong> reprimir um sentimento autêntico em nome da conveniência sela a própria desgraça.", "warn": True}
      ]
    },
    "ch02-noite-segunda-o-sonhador": {
      "cards": [
        {"ic": "spiral", "t": "O Homem Submerso", "emph": "Submerso", "b": "Em vez de construir pontes reais, ele coleciona triunfos irreais nos porões do próprio ego. <strong>A imaginação sem lastro na matéria corrói a vontade humana e transforma o indivíduo num parasita da própria mente.</strong> O devaneio crônico cobra a atrofia dos músculos vitais.", "tip": "<strong>Prática:</strong> arranque o planejamento mental excessivo e execute algo palpável, por menor que seja."},
        {"ic": "gap", "t": "O Preço da Imagem", "emph": "Preço", "b": "As batalhas invisíveis sob as cobertas exigem a castração da coragem no mundo tridimensional. <strong>A fuga romântica vicia o sujeito, tornando a sujeira, o suor e a dor das relações reais fardos insuportáveis de carregar.</strong> A imaginação exagerada sabota a matéria.", "tip": "<strong>Regra:</strong> não permita que glórias fantasiosas substituam a necessidade do embate físico do dia a dia."},
        {"ic": "bulb", "t": "A Embrião da Revolta", "emph": "Revolta", "b": "O personagem manso e curvado no banco da praça cultiva o ressentimento por baixo do sorriso amarelo. <strong>Ele transfere a culpa da sua solidão para o mundo cruel, ignorando que trancou a porta pelo lado de dentro.</strong> A passividade esconde sementes letais de rancor.", "tip": "<strong>Sinal de alerta:</strong> culpar a sociedade pela reclusão voluntária é a mentira que protege o covarde.", "warn": True}
      ]
    },
    "ch03-noite-terceira-historia-nastienka": {
      "cards": [
        {"ic": "link", "t": "O Espelho Trincado", "emph": "Espelho", "b": "A dor de Nástienka, alfinetada na barra da saia da avó, cruza o caminho do sonhador também preso no próprio labirinto. <strong>Duas existências paralisadas se encontram não por afinidade pura, mas pela urgência de escapar do sufoco insuportável.</strong> A tristeza procura abrigo na tristeza alheia.", "tip": "<strong>Modelo mental:</strong> reconheça quando uma ligação nasce do desespero idêntico e não de uma escolha livre."},
        {"ic": "key", "t": "A Moeda da Espera", "emph": "Espera", "b": "O inquilino aluga o quarto, rouba o coração da moça e desaparece deixando um relógio marcando um ano vazio. <strong>Ela estaciona o próprio destino na beira da estrada aguardando a salvação que depende exclusivamente de terceiros.</strong> Entregar as chaves da vida é assinar o sofrimento cego.", "tip": "<strong>Como aplicar:</strong> assuma o volante da sua trajetória; a espera passiva consome a juventude sem entregar juros."},
        {"ic": "mask", "t": "A Caridade Egoísta", "emph": "Caridade", "b": "Ele seca as lágrimas dela e entrega bilhetes no correio vestindo a armadura brilhante de herói altruísta. <strong>A caridade aparente funciona como isca sorrateira para prender a moça no seu círculo, tornando-se uma presença vital.</strong> A dor do outro é usada como alavanca emocional.", "tip": "<strong>Para refletir:</strong> avalie com franqueza os favores prestados: eles buscam aliviar a dor ou criar dívidas eternas?"}
      ]
    },
    "ch04-noite-quarta-ilusao-desilusao": {
      "cards": [
        {"ic": "wave", "t": "A Miragem Toca o Chão", "emph": "Miragem", "b": "A frustração brutal do atraso despedaça as regras do jogo e força o amor reprimido a sair das catacumbas. <strong>O silêncio obsequioso morre atropelado pela necessidade animal de afeto, escancarando a paixão inegável que ele tentou trancar.</strong> O papel cede espaço ao sangue quente.", "tip": "<strong>Regra:</strong> nenhum acordo intelectual sobrevive aos abalos sísmicos da carne e da emoção viva."},
        {"ic": "scale", "t": "O Trono Provisório", "emph": "Provisório", "b": "Cansada de esperar o dono do cargo, ela coroa o consolador para tentar tapar o buraco enorme deixado no peito. <strong>Ele senta na cadeira com sorriso rasgado, esquecendo que o posto é uma resposta provisória à dor aguda do abandono alheio.</strong> Erguer a vitória na fuga do outro é insustentável.", "tip": "<strong>Sinal de alerta:</strong> o afeto entregue na hora do luto amoroso cobra faturas altas de arrependimento logo à frente.", "warn": True},
        {"ic": "pivot", "t": "A Névoa se Dissipa", "emph": "Névoa", "b": "A figura do inquilino surge cortando o escuro da rua e rasga a noite de encantos sem pedir licença. <strong>O despertar da ilusão varre o castelo de cartas com um golpe único; o sonho tomba duro ao toque da realidade material concreta.</strong> A matéria não negocia com devaneios.", "tip": "<strong>Modelo mental:</strong> enxergue o fato bruto e físico como a fronteira absoluta onde fantasias encerram a validade."}
      ]
    },
    "ch05-a-manha-o-despertar": {
      "cards": [
        {"ic": "clock", "t": "O Sol Condena", "emph": "Condena", "b": "A manhã derrama luz crua revelando as rachaduras da parede e a palidez infinita do destino solitário que o aguarda. <strong>O sol esfola a alma e crava na testa do sonhador a garantia inegociável de uma velhice cinza sem testemunhas e sem calor.</strong> A trégua mágica acabou, e a conta chegou alta.", "tip": "<strong>Prática:</strong> a luz do sol desmente o brilho da noite; prepare a armadura para o retorno brutal às rotinas feias."},
        {"ic": "leaf", "t": "A Glória de um Minuto", "emph": "Glória", "b": "Ele sorri engolindo a perda gigantesca, agarrando o relâmpago de amor autêntico para tentar aquecer os invernos seguintes. <strong>O estalo microscópico de afeto pleno coroa a biografia de um homem que passaria a eternidade tropeçando num quarto trancado.</strong> Ele não exige o prêmio, ele absorve a centelha.", "tip": "<strong>Para refletir:</strong> instantes de beleza colossal não precisam ser eternos para injetar sentido permanente num peito humano."}
      ]
    }
  }
}

with open("gen_b6.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

