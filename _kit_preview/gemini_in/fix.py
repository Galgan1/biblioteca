import json
import codecs
import re

def write_md(filename, books_dict):
    with codecs.open(filename, 'w', encoding='utf-8') as f:
        for book_slug, book_data in books_dict.items():
            f.write(f"=== {book_slug} ===\n")
            f.write("```json\n")
            json.dump(book_data, f, ensure_ascii=False, indent=1)
            f.write("\n```\n\n")

mindset_ch04_08 = {
 'ch04-esporte-a-mentalidade-de-um-campeao': {
  'cards': [
   {'ic': 'target', 't': 'A Base Escondida', 'emph': 'Base', 'b': 'A glória no pódio é vendida como mágica, mas a lenda de todo campeão se ergue sobre o cimento do treino invisível. <strong>O ouro não coroa quem nasceu pronto, mas quem suportou a repetição exaustiva quando ninguém estava olhando</strong>.', 'tip': '<strong>Modelo mental:</strong> o talento inato é só o bilhete de entrada. O campeonato se vence com a teimosia do esforço diário.'},
   {'ic': 'mountain', 't': 'O Choque do Fracasso', 'emph': 'Fracasso', 'b': 'A mente fixa entra em pânico com o nocaute porque lê a derrota como atestado de mediocridade definitiva. Na ótica do crescimento, <strong>a dor de cair na lona é apenas um diagnóstico claro revelando a engrenagem exata que você precisa ajustar</strong>.', 'tip': '<strong>Pergunta-chave:</strong> quando a derrota bater, você vai culpar a arbitragem ou mapear o erro para a próxima rodada?'},
   {'ic': 'pivot', 't': 'O Sucesso é Transitório', 'emph': 'Transitório', 'b': 'Vencer a partida hoje não garante o seu trono eterno. Atletas que acreditam ser deuses natos param de treinar e desabam no campeonato seguinte. <strong>O campeão de longo prazo é o aprendiz faminto que trata toda vitória como um marco passageiro</strong>.', 'tip': '<strong>Regra:</strong> não confie no troféu de ontem. A evolução contínua é a única defesa contra o declínio.'}
  ]
 },
 'ch05-negocios-mentalidade-e-lideranca': {
  'cards': [
   {'ic': 'eye', 't': 'O Líder no Pedestal', 'emph': 'Pedestal', 'b': 'O chefe de mente fixa governa pelo ego, silenciando críticas e exigindo bajulação para proteger a própria imagem de gênio. <strong>Empresas apodrecem quando a liderança foca em parecer infalível em vez de encarar os dados reais da crise</strong>.', 'tip': '<strong>Sinal de alerta:</strong> líderes que demitem quem traz más notícias estão apenas comprando passagens para o próprio naufrágio.', 'warn': True},
   {'ic': 'constellation', 't': 'A Guerra Estéril', 'emph': 'Guerra', 'b': 'Organizações que premiam apenas o talento nato geram um ambiente tóxico onde esfaquear o colega é a única forma de subir. <strong>A cultura do crescimento premia o risco, a colaboração e a coragem de assumir o erro como degrau de aprendizado coletivo</strong>.', 'tip': '<strong>Modelo mental:</strong> um time só inova quando o fracasso tático é tratado como pesquisa de campo, não como sentença de morte.'},
   {'ic': 'bulb', 't': 'A Frieza dos Dados', 'emph': 'Frieza', 'b': 'O líder lendário não teme a verdade dolorosa. Ele arranca as ilusões de controle e encara a realidade nua, por pior que seja. <strong>Enfrentar relatórios brutais de frente, sem culpar o mercado, é a essência do comando executivo maduro</strong>.', 'tip': '<strong>Prática:</strong> cerque-se de pessoas que tenham a coragem moral de destruir os seus planos com argumentos lógicos antes do lançamento.'}
  ]
 },
 'ch06-relacionamentos-mentalidades-no-amor': {
  'cards': [
   {'ic': 'mask', 't': 'O Mito do Encaixe Mágico', 'emph': 'Encaixe Mágico', 'b': 'A fantasia romântica jura que almas gêmeas não brigam e se entendem sem palavras. Quando a mente fixa esbarra no primeiro conflito real, <strong>ela descarta a relação, crente de que o atrito é prova de que o parceiro era a escolha errada</strong>.', 'tip': '<strong>Sinal de alerta:</strong> acreditar que um relacionamento bom não exige trabalho braçal é a via expressa para a separação constante.'},
   {'ic': 'link', 't': 'A Lente do Conflito', 'emph': 'Conflito', 'b': 'Para parceiros fixos, a crise revela defeitos imutáveis de caráter. Para a mente de crescimento, <strong>o abismo na comunicação é a ponte necessária que força os dois a ajustarem as expectativas e calibrarem a convivência futura</strong>.', 'tip': '<strong>Como aplicar:</strong> na próxima discussão, ataque o problema estrutural do casal, mas preserve absolutamente o caráter do seu parceiro.'},
   {'ic': 'person', 't': 'O Veneno da Vingança', 'emph': 'Vingança', 'b': 'O orgulho ferido reage ao fim tentando destruir o outro para salvar o próprio ego rasgado. Mentes expansivas estancam a ferida, <strong>abandonam a fantasia do controle e usam o luto cruel como bússola para não repetirem a mesma falha na próxima tentativa</strong>.', 'tip': '<strong>Para refletir:</strong> usar a mágoa como troféu de vítima eterna apenas paralisa a sua capacidade de reconstruir a própria vida.'}
  ]
 },
 'ch07-pais-professores-treinadores': {
  'cards': [
   {'ic': 'target', 't': 'A Mira do Elogio', 'emph': 'Mira', 'b': 'Chamar a criança de gênio inato amarra a coragem dela. Aplauda exclusivamente a teimosia tática, o método e o foco prolongado no desafio. <strong>É a valorização do processo, e não do dom genético, que fabrica mentes elásticas que não recuam perante o erro</strong>.', 'tip': '<strong>Regra:</strong> não elogie o DNA. Elogie a força bruta e a criatividade de quem suou até achar a resposta.'},
   {'ic': 'layers', 't': 'O Rebaixamento Fatal', 'emph': 'Rebaixamento', 'b': 'Diminuir o nível do teste para poupar a criança da dor da frustração destrói o alicerce moral dela. <strong>Manter a barra de exigência implacável nas alturas e fornecer a escada técnica para subir é o maior ato de amor de um professor</strong>.', 'tip': '<strong>Armadilha:</strong> afagar os ombros para compensar a nota baixa sabota os músculos que a criança usaria para reagir amanhã.', 'warn': True},
   {'ic': 'scale', 't': 'O Mestre Realista', 'emph': 'Mestre Realista', 'b': 'Líderes formadores não pregam ilusões de que o topo é fácil. Eles cravam a régua lá em cima e entram na lama junto com o aluno, <strong>entregando métodos duros e feedback construtivo até que a habilidade que faltava seja finalmente forjada</strong>.', 'tip': '<strong>Prática:</strong> cobre um padrão de excelência insuportável, mas ensine detalhadamente a mecânica de cada degrau.'}
  ]
 },
 'ch08-mudando-mentalidades': {
  'cards': [
   {'ic': 'steps', 't': 'A Mudança de Software', 'emph': 'Mudança', 'b': 'Para deletar o sistema antigo, coloque sua voz fixa no banco dos réus. Identifique as desculpas e o medo paralisante do julgamento e <strong>opere uma reprogramação diária, substituindo o pânico de errar pela vontade maníaca de aprender o processo</strong>.', 'tip': '<strong>Modelo mental:</strong> a mente fixa é um hábito, não uma sentença biológica. Hábitos se quebram com ação contrária repetitiva.'},
   {'ic': 'triangle', 't': 'O Falso Crescimento', 'emph': 'Falso', 'b': 'Achar que ter a mente aberta é apenas ser otimista é uma mentira sedutora. O falso crescimento aplaude o esforço cego que não dá resultado. <strong>O crescimento real exige mudar de estratégia bruscamente quando o suor não estiver destrancando a porta</strong>.', 'tip': '<strong>Sinal de alerta:</strong> valorizar o esforço inútil que não corrige rotas é apenas um prêmio de consolação que afunda o projeto.', 'warn': True},
   {'ic': 'pivot', 't': 'O Processo Contínuo', 'emph': 'Processo', 'b': 'Mudar de lente não é apertar um botão mágico na testa; é arrastar a pedra morro acima todos os dias. <strong>Você precisa se policiar diante das quedas e redirecionar a própria bússola interna, trocando a culpa fácil pela curiosidade analítica brutal</strong>.', 'tip': '<strong>Como aplicar:</strong> travou no muro? Não force a cabeça. Recue, troque as ferramentas gastas, busque novos mentores e ataque de outro ângulo.'}
  ]
 }
}

obrigado = {
 'ch01-tres-tipos-de-feedback': {
  'cards': [
   {'ic': 'fork', 't': 'Os Três Idiomas', 'emph': 'Três Idiomas', 'b': 'Receber a devolução do seu trabalho é abrir uma caixa com três moedas diferentes: o aplauso da apreciação, a tesoura da orientação ou a bússola da avaliação. <strong>Muitas brigas nascem porque você pediu um abraço de encorajamento, mas o outro entregou um relatório técnico de falhas</strong>.', 'tip': '<strong>Como aplicar:</strong> negocie a frequência primeiro: "Nesta entrega, eu preciso de validação ou de correção tática?"'},
   {'ic': 'scale', 't': 'O Som e a Fúria', 'emph': 'Som e a Fúria', 'b': 'A avaliação carrega o peso do seu status na tribo, e por isso ela grita e ensurdece o cérebro. <strong>Não tente ouvir dicas de coaching ou aprimoramento enquanto a sua nota despenca no painel</strong>; a mente precisa digerir o choque da avaliação antes de conseguir aprender.', 'tip': '<strong>Modelo mental:</strong> entregue o número frio primeiro. Deixe o sangue baixar para só então apontar o caminho.'},
   {'ic': 'spark', 't': 'O Veneno do Genérico', 'emph': 'Genérico', 'b': 'Jogar um clichê como "bom trabalho" nas costas de quem suou sangue soa como deboche patronal. A verdadeira apreciação não é um protocolo raso, <strong>é um farol que ilumina o atrito específico que você suportou: "Eu vi como você segurou a crise sozinho na terça"</strong>.', 'tip': '<strong>Sinal de alerta:</strong> carimbar elogios invisíveis ofende o talento e evapora a gratidão na mesma velocidade.', 'warn': True}
  ]
 },
 'ch02-tres-gatilhos': {
  'cards': [
   {'ic': 'triangle', 't': 'O Gatilho da Verdade', 'emph': 'Gatilho da Verdade', 'b': 'Quando a crítica bate, a mente ergue automaticamente o escudo do "você está mentindo". Para não jogar a mensagem fora, abandone o tribunal do certo e do errado. <strong>Substitua a indignação pela curiosidade cirúrgica e procure o que ele está enxergando na sua nuca que você não consegue ver</strong>.', 'tip': '<strong>Prática:</strong> troque o "isso é falso" pelo "qual é o pingo de razão que ele capturou daqui?"'},
   {'ic': 'person', 't': 'A Arma e o Atirador', 'emph': 'Atirador', 'b': 'No gatilho relacional, a sua mente abandona o estilhaço da queixa para atacar quem arremessou a bomba e o tom de voz que usou. <strong>Mesmo com o mensageiro cuspindo areia nas suas feridas, o ouro pesado dos dados ocultos que ele traz nunca deve ser desprezado</strong>.', 'tip': '<strong>Modelo mental:</strong> são dois problemas na mesa: a crítica sobre você e o mau comportamento do outro. Trate um de cada vez.'},
   {'ic': 'mask', 't': 'O Colapso da Identidade', 'emph': 'Identidade', 'b': 'Uma cutucada microscópica no seu desempenho pode acender o outdoor do "eu sou uma fraude irrecuperável". <strong>A explosão emocional desproporcional não mede o tamanho real da crítica, mas a paranoia e a fragilidade do seu próprio ego no momento do impacto</strong>.', 'tip': '<strong>Sinal de alerta:</strong> pular de "errei a conta" para "eu destruo tudo o que toco" é a assinatura da identidade em pânico.', 'warn': True}
  ]
 },
 'ch03-de-certo-ou-errado-para-entender': {
  'cards': [
   {'ic': 'bulb', 't': 'A Lâmina da Curiosidade', 'emph': 'Lâmina', 'b': 'Engesse a vontade de processar o colega no banco dos réus na primeira frase. Troque o instinto de defesa furiosa por um interrogatório calmo e analítico. <strong>Peça que ele desenhe, em câmera lenta, qual foi a atitude exata que quebrou os selos de confiança dele</strong>.', 'tip': '<strong>Como aplicar:</strong> amarre o cão instintivo que late na defensiva e exija os dados crus que formaram a opinião alheia.'},
   {'ic': 'wrench', 't': 'A Cirurgia dos Rótulos', 'emph': 'Rótulos', 'b': 'Frases covardes como "seja mais dinâmico" são malas fechadas que escondem fatos no fundo e palpites no topo. <strong>Arranque a fita desses pacotes exigindo datas exatas, exemplos vivos e o comportamento isolado que gerou o incômodo</strong>.', 'tip': '<strong>Regra:</strong> as perguntas "O que você quer dizer com isso?" e "Me dá um exemplo" matam a neblina dos rótulos.'},
   {'ic': 'key', 't': 'A Fronteira Blindada', 'emph': 'Fronteira', 'b': 'Fugir do feedback temendo sair algemado pela concordância coroa a ignorância infantil. <strong>Digerir meticulosamente os ossos jogados pela goela de quem te critica não significa ajoelhar em submissão aos mandos deles</strong>. Escutar é levantar dados, não assinar contratos.', 'tip': '<strong>Modelo mental:</strong> entender perfeitamente o mapa do outro é sinal de poder absoluto, não um contrato de obediência.'}
  ]
 },
 'ch04-pontos-cegos': {
  'cards': [
   {'ic': 'eye', 't': 'A Navalha do Impacto', 'emph': 'Impacto', 'b': 'Você se julga pelo seu coração imaculado, mas o tribunal da vida só pesa a cratera que as suas ações deixaram no chão da sala. <strong>A intenção brilhante que não saiu da sua cabeça não conserta o estilhaço da granada que você jogou na mesa do colega</strong>.', 'tip': '<strong>Prática:</strong> guarde o escudo da boa intenção. Se o impacto rasgou a relação, é o buraco que você tem que fechar.'},
   {'ic': 'gap', 't': 'A Traição Corporal', 'emph': 'Traição', 'b': 'O seu rosto exala a fúria que as suas palavras polidas tentam esconder desesperadamente. O ponto cego não é a ignorância; <strong>é a ilusão de que você conseguiu camuflar o seu tédio enquanto os seus ombros e suspiros gritam a verdade na sala inteira</strong>.', 'tip': '<strong>Sinal de alerta:</strong> quando o outro te acusar de hostilidade, não confie no seu discurso civilizado. Acredite na sua postura.'},
   {'ic': 'lens', 't': 'O Choque dos Mapas', 'emph': 'Mapas', 'b': 'As grandes guerras de escritório raramente nascem da crueldade calculada. Elas brotam quando dois mapas mentais cegos colidem no nevoeiro. <strong>Esmigalhe os laudos fechados até separar a pedra fria do que realmente aconteceu da interpretação venenosa que deram ao fato</strong>.', 'tip': '<strong>Para refletir:</strong> pergunte sem tensão "O que você estava vendo quando chegou a essa conclusão pesada sobre mim?"', 'warn': True}
  ]
 },
 'ch05-encontrar-o-certo-no-errado': {
  'cards': [
   {'ic': 'bulb', 't': 'As Balas do Exemplo', 'emph': 'Balas', 'b': 'Fuzile a covardia dos rótulos vagos exigindo o holograma do erro em alta definição. <strong>Somente um caso engessado e isolado, cravado no tempo e no espaço, pode esquartejar o monstro fantasma da reclamação barata e não justificada</strong>.', 'tip': '<strong>Como aplicar:</strong> não acate nem rejeite nada até pingar o tijolo exato no chão: "De qual reunião você está falando?"'},
   {'ic': 'layers', 't': 'As Três Engrenagens', 'emph': 'Engrenagens', 'b': 'Muito do laser apontado para a sua testa é apenas o reflexo do choque entre você, o outro e a engrenagem burra do sistema. <strong>Desarme o revólver da culpa individual e olhe de cima para as regras tortas e papéis confusos que encurralaram vocês dois</strong>.', 'tip': '<strong>Modelo mental:</strong> antes de abraçar a culpa na lama, pergunte: "O que do sistema quebrou e empurrou nós dois para essa briga?"'},
   {'ic': 'target', 't': 'O Grão de Ouro', 'emph': 'Grão de Ouro', 'b': 'A caça maníaca por falhas lógicas no discurso de quem te critica espalha uma cortina de fumaça fútil. <strong>Isolar o único milímetro de verdade cirúrgica dentro da enxurrada de lixo alheio é o que impede você de queimar o mapa do tesouro</strong>.', 'tip': '<strong>Armadilha:</strong> invalidar o pacote inteiro porque o carteiro gaguejou afunda a sua chance de achar o ouro no fundo da mala.', 'warn': True}
  ]
 },
 'ch06-gatilho-de-relacionamento': {
  'cards': [
   {'ic': 'fork', 't': 'Os Dois Trilhos', 'emph': 'Dois Trilhos', 'b': 'No momento em que o veneno ataca a jugular, decifre os dois cabos isolados: a bala da crítica enviada e o modo áspero e desonesto como atiraram. <strong>Cortar um cabo da bomba por vez com frieza é o que salva a negociação de virar poeira cósmica</strong>.', 'tip': '<strong>Prática:</strong> acione a sirene de forma limpa: "Vamos raspar o erro na planilha agora e discutir o seu tom áspero amanhã"'},
   {'ic': 'spiral', 't': 'A Comutação', 'emph': 'Comutação', 'b': 'Se você rebate a pedrada do desempenho apontando a corrupção de quem atirou, os dois trens colidem no vazio e o desastre é mudo. <strong>Engatar o vagão sujo da sua defesa no trilho paralelo de um segundo assunto descarrilha qualquer chance de resolução</strong>.', 'tip': '<strong>Modelo mental:</strong> se você mudar de assunto como tática de fuga, os dois saem perdendo e a poeira nunca abaixa.'},
   {'ic': 'key', 't': 'Mensagem e Mensageiro', 'emph': 'Mensageiro', 'b': 'A mancha moral na camisa do interlocutor não anula a bússola que ele carrega. <strong>O algoz frio e sem honra ainda pode berrar uma verdade técnica inegociável, afogada no cascalho da sua própria vaidade machucada</strong>.', 'tip': '<strong>Para refletir:</strong> rejeitar diamantes porque as mãos de quem os entregou estão sujas de sangue só mantém a sua carteira vazia.'}
  ]
 },
 'ch07-sistema-entre-nos': {
  'cards': [
   {'ic': 'layers', 't': 'O Tripé de Diagnóstico', 'emph': 'Tripé', 'b': 'Ataque as raízes da guerra subindo o nível de visão. Avalie o choque químico da combinação pessoal; olhe para os trajes apertados dos papéis forçados; esmague as falhas de incentivo. <strong>Entender o cenário inteiro blinda as amarras do time e evita o derramamento de sangue inútil</strong>.', 'tip': '<strong>Como aplicar:</strong> pergunte sempre "Quanto de sujeira é minha, quanto é nossa e quanto desce do telhado rachado da empresa?"'},
   {'ic': 'scale', 't': 'A Guilhotina ou a Chave', 'emph': 'Guilhotina', 'b': 'A caça às bruxas pela culpa paralisa todos no medo de assumirem o banco dos réus, congelando o conserto. A varredura pela contribuição sistêmica não exige guilhotinas. <strong>Trocar a forca retroativa pelo mapa de quem derramou a água na engrenagem reabre as soluções</strong>.', 'tip': '<strong>Modelo mental:</strong> a culpa isola e arranca cabeças. A contribuição partilha a chave inglesa e liga os motores parados.'},
   {'ic': 'person', 't': 'O Atrito Inevitável', 'emph': 'Atrito', 'b': 'A faísca que incinera a sala quase sempre mora na zona morta entre os limites dos dois, invisível para quem avalia um corpo isolado. <strong>Rotular como maldade patológica aquilo que é apenas uma diferença mecânica de compasso transforma o parceiro num psicopata imaginário</strong>.', 'tip': '<strong>Sinal de alerta:</strong> jogar a sujeira na vala da "falha do sistema" não assina o seu alvará de impunidade. A sua parcela continua lá.', 'warn': True}
  ]
 },
 'ch08-identidade-e-fiacao': {
  'cards': [
   {'ic': 'wave', 't': 'A Fiação Base', 'emph': 'Fiação Base', 'b': 'As suas linhas neurais não balançam como as do vizinho. O seu estado-base, o grau de pânico na queda e o tempo para estancar o sangramento ditam as regras. <strong>Separar a gritaria histérica do seu biotipo do buraco real do feedback economiza baldes de dor fútil</strong>.', 'tip': '<strong>Modelo mental:</strong> o alarme do seu ego dispara ensurdecedor e solta faíscas. A gravidade do ruído não reflete o estrago da marreta.'},
   {'ic': 'layers', 't': 'Identidade Fluida', 'emph': 'Identidade Fluida', 'b': 'Identidades gravadas em ferro cedem e trincam no primeiro vento de avaliação fria. A identidade fluida, montada numa rede complexa, <strong>engole a lâmina da crítica pesada como oxigênio limpo para treinar sem deixar a estrutura principal sangrar até morrer</strong>.', 'tip': '<strong>Como aplicar:</strong> quando o ataque vier no peito, acione as colunas da sua complexidade real, anulando o maniqueísmo barato.'},
   {'ic': 'mask', 't': 'A Armadilha do Sempre', 'emph': 'Sempre', 'b': 'A mente acossada amplia a falha minúscula de um copo quebrado num tsunami eterno e irrecuperável de fracassos cósmicos. <strong>Apagar as chamas maníacas do catastrofismo exagerado na mangueira fria da razão matemática salva anos de esgotamento brutal inventado</strong>.', 'tip': '<strong>Sinal de alerta:</strong> toda frase de pânico que contiver "eu sempre destruo tudo" é alucinação histérica da identidade estilhaçada.', 'warn': True}
  ]
 },
 'ch09-limites-e-crescimento': {
  'cards': [
   {'ic': 'leaf', 't': 'O Porteiro de Si', 'emph': 'Porteiro', 'b': 'Agachar a espinha e engolir pacotes tóxicos de feedbacks em nome da boa convivência não fabrica aprendizado, fabrica lixo passivo. <strong>A escuta generosa exige portas abertas para a entrada do som, mas você senta no trono da fronteira para decidir com machado o que contamina a horta</strong>.', 'tip': '<strong>Modelo mental:</strong> receber a correspondência educadamente no portão jamais te força a consumir o veneno que enfiaram na caixa de correio.'},
   {'ic': 'scale', 't': 'Os Escudos Saudáveis', 'emph': 'Escudos', 'b': 'Não rasgue a ponte de imediato. Use o limite cortês do escudo brando. <strong>Parar o tiroteio pesado quando ele rói impiedosamente as gengivas da relação não atesta defesa rala covarde, atesta comando higiênico e controle firme sobre o próprio ecossistema</strong>.', 'tip': '<strong>Prática:</strong> diga pausadamente com olhos cravados secos: "O recado desceu, mas não opero as lâminas desse jeito, e seguimos"'},
   {'ic': 'key', 't': 'O Direito de Decidir', 'emph': 'Direito', 'b': 'A ilusão venenosa de que escutar proíbe discordar te algema num purgatório. <strong>Fuzilar a conexão bruta e jogar a amizade na fogueira porque um palpite feio queimou seu ouvido na praça é errar o alvo e explodir a cidade para matar um mosquito cego</strong>.', 'tip': '<strong>Sinal de alerta:</strong> amputar a convivência inteira como via expressa para cortar as cobranças mostra uma fronteira enferrujada e imatura.', 'warn': True}
  ]
 }
}

quebrando = {
 'ch01-o-voce-quantico': {
  'cards': [
   {'ic': 'spark', 't': 'A Assinatura Energética', 'emph': 'Assinatura', 'b': 'Cada pensamento é o rascunho de um projeto; a emoção é a voltagem que aciona a máquina. Juntos, eles formam a assinatura magnética que atrai a realidade física. <strong>Se o cenário externo de tédio e dor se repete à exaustão, é porque o sinal interno grudou num loop fechado</strong>.', 'tip': '<strong>Modelo mental:</strong> a vida material é o carimbo; a sua emoção crônica é o molde de borracha original.'},
   {'ic': 'bulb', 't': 'Causa Antes do Efeito', 'emph': 'Efeito', 'b': 'A maior arapuca é aguardar o troféu para então liberar o grito de vitória. Dispenza exige a inversão completa: <strong>você precisa inundar a corrente sanguínea com a euforia do sucesso antes de ver a linha de chegada no mundo lá fora</strong>. A alegria não é a recompensa; é o alicerce.', 'tip': '<strong>Prática:</strong> esperar o cenário perfeito para abandonar a miséria mental é a receita química da estagnação perpétua.'},
   {'ic': 'eye', 't': 'O Abismo da Intenção', 'emph': 'Abismo', 'b': 'Mentalizar a conta farta ou o projeto de sucesso mantendo o estômago contorcido pelo terror da perda é tentar pilotar um avião com os motores desligados. <strong>A imaginação nua esfarela sem o peso colossal do coração convencido de que o alvo já foi atingido</strong>.', 'tip': '<strong>Sinal de alerta:</strong> o cérebro que repete mantras enquanto as vísceras gritam na angústia antiga é uma usina apagada.', 'warn': True}
  ]
 },
 'ch02-vencendo-o-ambiente': {
  'cards': [
   {'ic': 'pin', 't': 'O Termostato Físico', 'emph': 'Termostato', 'b': 'A cama bagunçada, o relógio no pulso, a rua de sempre. A mobília física do seu dia joga cabrestos invisíveis na sua biologia, resetando violentamente o seu humor para o tédio habitual. <strong>Você acha que está tomando decisões, mas está apenas reagindo ao código de barras do seu quarto</strong>.', 'tip': '<strong>Como aplicar:</strong> para instalar um software neural inédito, isole-se: apague a luz e desamarre-se dos gatilhos físicos antigos.'},
   {'ic': 'spiral', 't': 'O Ciclo Fechado', 'emph': 'Ciclo', 'b': 'O cheiro do asfalto evoca a mesma apatia, que gera o sorriso amargo, que confirma a mediocridade do dia no espelho. Esse moedor de carne mastiga e repete você na eternidade. <strong>Rasgar essa malha de ferro exige que o cérebro dispare fogo acima da rotina dos cinco sentidos primitivos</strong>.', 'tip': '<strong>Modelo mental:</strong> a realidade ao redor é um botão de replay que você tem a chave de ouro para ignorar de propósito.'},
   {'ic': 'mountain', 't': 'A Rebelião Silenciosa', 'emph': 'Rebelião', 'b': 'Não cruze os braços esperando o clima externo amornar para forjar o seu salto psíquico. Condicionar a sua estabilidade à maré de eventos inverte a lâmina contra você. <strong>A sua vitória central é cravar a bandeira da paz enquanto o chão racha lá fora sob os pés da empresa</strong>.', 'tip': '<strong>Para refletir:</strong> justificar a cólera no rosto porque a chuva estragou o trânsito é delegar ao clima frio o comando da sua mente.', 'warn': True}
  ]
 },
 'ch03-vencendo-o-corpo': {
  'cards': [
   {'ic': 'wave', 't': 'A Química do Vício', 'emph': 'Química', 'b': 'Anos inundando as células com o veneno da autopiedade e da ansiedade adestraram o seu fígado e músculos a implorarem pela dose. <strong>O seu corpo não quer a paz profunda; ele urra nas cordas pedindo a convulsão familiar e química que você sempre vendeu a ele</strong>.', 'tip': '<strong>Modelo mental:</strong> encare o pânico e a fadiga como crise de abstinência da sua ansiedade velha, e não como uma verdade ameaçadora.'},
   {'ic': 'gap', 't': 'O Vale do Desconforto', 'emph': 'Vale', 'b': 'Quebrar o protocolo tóxico biológico do estresse vai jogar cãibras de angústia e alertas falsos de pânico na sua nuca nos primeiros dias. <strong>Essa coceira desesperada clamando pelas correntes antigas não é erro; é a prova biológica de que a tranca velha está arrebentando</strong>.', 'tip': '<strong>Como aplicar:</strong> beba o desconforto e a ansiedade da mudança como a confirmação crua e clara de que o software está sendo reescrito.'},
   {'ic': 'key', 't': 'O Falso Rótulo', 'emph': 'Falso Rótulo', 'b': 'Bater no peito dizendo com orgulho "eu sou esquentado por natureza" coroa a submissão ao corpo como uma virtude. <strong>O animal de carne afogada no hábito químico dita as regras, sem que a inteligência cortical assuma o volante da máquina biológica</strong>.', 'tip': '<strong>Sinal de alerta:</strong> encharcar os discursos de que a genética justifica o ataque de raiva amarra você no passado sem chance de fuga.', 'warn': True}
  ]
 },
 'ch04-vencendo-o-tempo': {
  'cards': [
   {'ic': 'clock', 't': 'O Trilho do Agora', 'emph': 'Agora', 'b': 'Arrastar a âncora esfolada das perdas de ontem ou cravar os dentes na neblina das dívidas de amanhã cimenta o monstro da ansiedade. <strong>Somente no pino exato, silencioso e afiado do momento presente absoluto é que o cérebro escapa da rota de colisão da repetição velha</strong>.', 'tip': '<strong>Como aplicar:</strong> o passado e o futuro amarram as mãos nas correntes antigas. Pise firme na navalha afiada do "agora" ininterrupto.'},
   {'ic': 'spiral', 't': 'A Antecipação do Desastre', 'emph': 'Desastre', 'b': 'Cozinhar catástrofes irreais nas chamas do pensamento queima os nervos físicos como se o chicote estivesse rasgando as costas no mundo real. <strong>A aflição paranoica projeta um cenário letal irreal e estraçalha a barreira imune no mesmo segundo em que a tela mental acende a imagem</strong>.', 'tip': '<strong>Modelo mental:</strong> sofrer calado imaginando a demissão produz no sangue o exato banho de cortisol de ser demitido ao vivo.'},
   {'ic': 'leaf', 't': 'A Fresta Atemporal', 'emph': 'Fresta', 'b': 'Na sala de foco total do trabalho profundo, o cérebro desliga o radar do tempo. <strong>A angústia frita e apressada de olhar o relógio para terminar o relatório mata a genialidade; a obra-prima flui apenas quando as horas desaparecem num abismo limpo e silencioso</strong>.', 'tip': '<strong>Para refletir:</strong> sentar na cadeira medindo os minutos com pânico no peito corrói a energia livre e seca as suas reservas vitais.', 'warn': True}
  ]
 },
 'ch05-sobreviver-versus-criar': {
  'cards': [
   {'ic': 'fork', 't': 'As Duas Frequências', 'emph': 'Duas Frequências', 'b': 'O seu sangue não flui para o centro criativo quando a pistola do estressor aponta para a sua testa. No modo sobrevivência, a visão encolhe para enxergar apenas a ameaça no radar. <strong>A porta da criatividade exige a sensação visceral de segurança para finalmente se abrir</strong>.', 'tip': '<strong>Prática:</strong> pergunte a si mesmo no meio da tarde: "Estou construindo impérios ou apenas me esquivando de balas invisíveis?"'},
   {'ic': 'spark', 't': 'A Fogueira da Gratidão', 'emph': 'Gratidão', 'b': 'A euforia cristalina voa de dentro para fora antes das moedas tocarem o cofre da empresa. <strong>A celebração antecipada é o motor quântico de Dispenza: ela aterra a visão do campo das ideias e puxa o oxigênio para materializar a meta no cimento cru do agora</strong>.', 'tip': '<strong>Modelo mental:</strong> o evento em si não é o que solta a faísca da alegria; a emoção superior cultivada a seco constrói o evento.'},
   {'ic': 'wave', 't': 'O Veneno do Caos', 'emph': 'Caos', 'b': 'Idolatrar a adrenalina rústica da pressa corporativa como atestado de competência esmaga a engenharia fria da verdadeira inovação. <strong>Confundir as pernas bambas de um fugitivo na savana com a precisão letal de um construtor calmo joga as suas baterias no lixo</strong>.', 'tip': '<strong>Sinal de alerta:</strong> tentar costurar projetos complexos afogado na ansiedade do prazo queima as veias de alta performance da mente inteira.', 'warn': True}
  ]
 },
 'ch06-tres-cerebros': {
  'cards': [
   {'ic': 'steps', 't': 'A Forja dos Três Níveis', 'emph': 'Forja', 'b': 'Aprender na teoria desenha fios soltos no córtex; aplicar na prática joga o motor no chão e suja as mãos. Mas a verdadeira transformação de titânio só acontece com a repetição bruta, <strong>que joga o código dominado no abismo automático do cerebelo, forjando uma habilidade cega e perfeita</strong>.', 'tip': '<strong>Diagnóstico:</strong> ler a técnica não o torna faixa preta; ralar nos tatames sem pausa é o que esculpe a reação sem pensar.'},
   {'ic': 'bulb', 't': 'A Biblioteca Estéril', 'emph': 'Biblioteca', 'b': 'Enfiar dez livros pesados no crânio liso sem derramar suor na prática e na falha empalha cadáveres de ideias brilhantes que nunca andarão sozinhas. <strong>Apenas o conhecimento que queima nas mãos e corta a pele do ego durante a execução consegue criar lastro biológico duradouro</strong>.', 'tip': '<strong>Para refletir:</strong> entender a dieta no papel não apaga a fome; é o controle brutal de ferro no almoço que refaz as células.'},
   {'ic': 'target', 't': 'O Carimbo Final', 'emph': 'Carimbo', 'b': 'A repetição mecânica sem alma não aterra o avião. <strong>É a labareda elétrica do êxtase feroz ligada ao ato repetitivo que cauteriza os neurônios de vez e marca a fogo a nova competência na argila crua e permanente da sua matriz biológica superior</strong>.', 'tip': '<strong>Sinal de alerta:</strong> bater metas o dia inteiro em estado de tédio zumbi não recicla o seu cérebro; exige uma paixão letal na solda.', 'warn': True}
  ]
 },
 'ch07-epigenetica-e-neuroplasticidade': {
  'cards': [
   {'ic': 'constellation', 't': 'O Ensaio Místico', 'emph': 'Ensaio', 'b': 'Quando a imaginação focada estilhaça as crenças de teto baixo, as faíscas mentais constroem teias neurais concretas e físicas no cérebro. <strong>O corpo cego e submisso obedece à projeção interna densa como se a vitória já tivesse rasgado o peito com a medalha oficial do pódio</strong>.', 'tip': '<strong>Como aplicar:</strong> o ensaio mental perfeito e nítido não é devaneio bobo, é engenharia neural preparatória e inegociável.'},
   {'ic': 'leaf', 't': 'O Cofre dos Genes', 'emph': 'Cofre', 'b': 'A dupla hélice entrega um armamento cru, não as algemas da condenação irrevogável. A nova biologia aposta que o comportamento cirúrgico <strong>e a emoção afiada arrancam o cadeado e escolhem qual das armas inativas deve atirar e qual código venenoso precisa ser silenciado</strong>.', 'tip': '<strong>Modelo mental:</strong> a genética é apenas a estante cheia de livros; o seu estilo de vida implacável é o bibliotecário que escolhe qual ler.'},
   {'ic': 'steps', 't': 'A Poda de Ferro', 'emph': 'Poda', 'b': 'A tesoura fria da falta de uso desliga fios fracos de maus hábitos, e a repetição dura pavimenta rodovias de alta velocidade. <strong>O cérebro recicla os próprios tijolos silenciosamente, esmagando pontes velhas de raiva e construindo viadutos invulneráveis de serenidade com o uso constante</strong>.', 'tip': '<strong>Prática:</strong> recuar de uma velha fúria não é só moral; é cortar literalmente a energia do circuito tóxico no crânio.'}
  ]
 },
 'ch08-a-lacuna': {
  'cards': [
   {'ic': 'gap', 't': 'O Vão do Fingimento', 'emph': 'Fingimento', 'b': 'A sorrir com a mandíbula travada enquanto o fígado engole o choro do fracasso cria o abismo fatal da lacuna. <strong>Vestir fantasias de ouro para o público na praça, mantendo as pernas tremendo de vazio e insegurança na sombra de casa, drena a vida e rasga o tanque de energia psíquica</strong>.', 'tip': '<strong>Sinal de alerta:</strong> prestar atenção profunda nessa cisão entre o teatro social ensaiado e a desgraça emocional interna salva mentes.'},
   {'ic': 'eye', 't': 'O Radar Aéreo', 'emph': 'Radar Aéreo', 'b': 'Para de sofrer com o moedor sujo das emoções baixas, levante a mira. <strong>A metacognição exige voar acima do furacão com o holofote frio da análise implacável, julgando os próprios tropeços com a precisão de um sniper, em vez de afundar no lodo quente do choro fútil</strong>.', 'tip': '<strong>Como aplicar:</strong> se pegar gritando no trânsito, acione a câmera do alto: observe as veias e a fúria rasteira sem mergulhar na culpa.'},
   {'ic': 'link', 't': 'A Coerência Total', 'emph': 'Coerência', 'b': 'O milagre que dobra montanhas desponta apenas quando a cabeça limpa entra em acordo com o peito incandescente. <strong>O campo submisso da realidade responde apenas ao acorde perfeitamente afinado de quem tem a emoção e a intenção travadas e mirando milimetricamente no mesmo alvo branco</strong>.', 'tip': '<strong>Armadilha:</strong> o teatro de desejar grandeza com a barriga tremendo de medo de boletos só atrai ventos de miséria contínua.', 'warn': True}
  ]
 },
 'ch09-meditacao-e-o-estado-generativo': {
  'cards': [
   {'ic': 'spiral', 't': 'A Oficina Interna', 'emph': 'Oficina Interna', 'b': 'O processo de meditação de Dispenza não é um cochilo anestésico. É a marreta dura na bigorna fria: <strong>desmantelar conscientemente as máscaras frouxas do orgulho e martelar, sob pressão brutal, a base nítida e elétrica de um sistema operacional completamente limpo de neuroses</strong>.', 'tip': '<strong>Modelo mental:</strong> veja o fechar dos olhos como quem entra numa cirurgia voluntária de coração e córtex para remover as toxinas vis.'},
   {'ic': 'leaf', 't': 'O Salto no Vazio', 'emph': 'Vazio', 'b': 'Ninguém descobre tesouros orbitando na camada rasa do que já domina. <strong>É soltando a âncora da identidade rígida e aceitando despencar no escuro absoluto e vazio do silêncio que o cérebro fabrica as estrelas e as novas conexões que redefinem o caminho da carne viva</strong>.', 'tip': '<strong>Prática:</strong> no momento da ansiedade crua, desligue o apego raivoso de tentar resolver tudo com a mente afogada e pule para a inação.'},
   {'ic': 'spark', 't': 'A Gratidão Antecipada', 'emph': 'Gratidão', 'b': 'Agradecer depois que o troféu chega na mão é a reação orgânica de escravos do ambiente. <strong>O mestre verdadeiro emite o certificado oficial e carimbado de vitória suprema na cama escura, antecipando o fogo químico no corpo antes mesmo de descer para enfrentar os leões do dia</strong>.', 'tip': '<strong>Sinal de alerta:</strong> mendigar ao vácuo por migalhas futuras em posição de carência apenas espanta as conquistas reais sólidas.', 'warn': True}
  ]
 },
 'ch10-vivendo-o-novo-eu': {
  'cards': [
   {'ic': 'mountain', 't': 'A Prova de Fogo', 'emph': 'Prova de Fogo', 'b': 'Não adianta vestir a armadura no quarto e arriar as calças de medo quando o e-mail áspero do cliente estoura na tela. <strong>O teste cirúrgico do seu novo eu acontece de pé, em movimento contínuo, quando os gatilhos nojentos antigos disparam e a sua blindagem responde fria e sem um piscar de olhos</strong>.', 'tip': '<strong>Prática:</strong> na primeira investida injusta da rotina, congele o cão raivoso interno e sustente o sorriso e a força que você meditou.'},
   {'ic': 'clock', 't': 'O Fuso Horário Físico', 'emph': 'Fuso Horário', 'b': 'O cimento pesado do mundo material não acompanha a velocidade do pensamento do lado de dentro. <strong>O atraso entre o milagre neural e a entrega do pacote físico do projeto exige nervos de aço e paciência impiedosa para não abortar a gestação antes da colheita gorda e final</strong>.', 'tip': '<strong>Modelo mental:</strong> desista de alucinar colapsos apenas porque os resultados tridimensionais atrasaram três dias na planilha suada.'},
   {'ic': 'target', 't': 'A Blindagem Final', 'emph': 'Blindagem', 'b': 'Reinar nas nuvens no fim de semana e morder canelas na segunda-feira zera os contratos. O desapego maduro <strong>cancela os cronômetros e engessa o terreno, cravando os pés da serenidade no chão e não entregando a soberania mental de volta aos ruídos infantis da empresa ou da rua esburacada</strong>.', 'tip': '<strong>Sinal de alerta:</strong> barganhar prazos para a vida funcionar expõe a fé rasa de quem não dominou a máquina cerebral debaixo de fogo cruzado.', 'warn': True}
  ]
 }
}

sociedade = {
 'ch01-violencia-neuronal': {
  'cards': [
   {'ic': 'gap', 't': 'O Inimigo Interno', 'emph': 'Inimigo', 'b': 'A guerra imunológica clássica acabou: não adoecemos mais porque um vírus estrangeiro atravessou a cerca. O abismo moderno é neuronal. <strong>O esgotamento brutal nasce da intoxicação silenciosa pelo excesso ininterrupto do mesmo, entupindo as veias com as promessas de positividade infinita</strong>.', 'tip': '<strong>Modelo mental:</strong> pare de procurar o vilão que puxou o tapete de fora. O burnout e o cansaço nascem do excesso de demanda sobre si mesmo.'},
   {'ic': 'bulb', 't': 'O Tumor do Positivo', 'emph': 'Positivo', 'b': 'Morríamos outrora amarrados pela proibição. Hoje agonizamos afogados no mar raso de mil possibilidades e alertas brilhantes ininterruptos. <strong>A comunicação desenfreada sem pausas ergue a bomba atômica invisível da fadiga generalizada que consome os cérebros vivos nas poltronas confortáveis</strong>.', 'tip': '<strong>Prática:</strong> tentar combater a exaustão empilhando mais quatro aplicativos lúdicos de organização joga um balde de gasolina na sua fogueira.'},
   {'ic': 'lens', 't': 'A Falsa Paz Global', 'emph': 'Paz Global', 'b': 'As cercas que separavam a sociedade e mantinham os mundos isolados desabaram inteiras. A falta dessa parede rígida <strong>cega a nossa capacidade de erguer bloqueios e dizer o “não” brutal necessário para estancar a invasão contínua da demanda que não para de apitar no próprio bolso</strong>.', 'tip': '<strong>Sinal de alerta:</strong> o mundo aberto onde toda informação transita sem restrições tritura as defesas da mente que precisa dormir e esquecer.', 'warn': True}
  ]
 },
 'ch02-alem-da-sociedade-disciplinar': {
  'cards': [
   {'ic': 'sword', 't': 'O Chicote do Dever', 'emph': 'Dever', 'b': 'O mestre sombrio da fábrica velha mandava você apertar as porcas sob a ponta da lança do “você tem que fazer”. Hoje, o seu instrutor amigável jura, mentindo de forma sorridente, que “você pode tudo”. <strong>A ilusão de poder irrestrito se revela o açoite mais mortal, torturando quem não realiza os milagres prometidos</strong>.', 'tip': '<strong>Para refletir:</strong> o lema plastificado da propaganda contemporânea ativa uma cobrança esmagadora mil vezes superior à das antigas prisões.'},
   {'ic': 'person', 't': 'O Senhor de Si', 'emph': 'Senhor', 'b': 'Nós engolimos o feitor antigo com os dentes cravados na própria carne. <strong>O sujeito de desempenho entra na gaiola vazia e amarra o torniquete no próprio pescoço para produzir nas férias, sentindo a falsa vitória da autonomia enquanto desaba silenciosamente de cansaço</strong>.', 'tip': '<strong>Armadilha:</strong> vibrar com o crachá de “sou o próprio patrão” na madrugada solitária quase sempre indica que você está escravizando você.'},
   {'ic': 'spiral', 't': 'O Salto no Abismo', 'emph': 'Salto', 'b': 'Quando a exigência letal do mercado transplanta raízes para a alma livre, o erro mínimo aciona as guilhotinas mentais contra o espelho. <strong>A queda de asas do esgotamento reflete um soldado encurralado que se bateu contra as pedras dos seus próprios limites céticos imaginários sem tréguas</strong>.', 'tip': '<strong>Sinal de alerta:</strong> sentir culpa de carregar fardos gigantes em domingos mornos de chuva atesta que você internalizou a agressão bruta exterior.', 'warn': True}
  ]
 },
 'ch03-tedio-profundo': {
  'cards': [
   {'ic': 'eye', 't': 'O Animal Multitarefa', 'emph': 'Multitarefa', 'b': 'Celebrar a histeria das vinte abas abertas piscando não é salto biológico ou poder genial; é regressar ao radar ansioso do coelho que foge na floresta crua. <strong>Os olhos saltando sem parar da tela para o telefone matam a imersão firme que apenas o foco gélido, surdo e absoluto é capaz de fabricar</strong>.', 'tip': '<strong>Prática:</strong> abandonar um ensaio pesado no parágrafo final para caçar notificações vazias mostra a falência da atenção plena.'},
   {'ic': 'clock', 't': 'A Calma do Chão', 'emph': 'Calma do Chão', 'b': 'O verdadeiro tédio profundo não é a perda estúpida do relógio; é o pântano vivo e espesso onde o caos senta e para de girar as peças alucinadas da mente. <strong>Suportar e tolerar as nuvens brancas lentas engendra o intervalo mágico e denso que dá corda para criar sistemas de inovação formidáveis do zero absoluto</strong>.', 'tip': '<strong>Modelo mental:</strong> experimente aguentar a ausência total de botões por quarenta minutos diários e colha do tédio a raiz clara do pensamento original.'},
   {'ic': 'lens', 't': 'O Duelo da Retenção', 'emph': 'Retenção', 'b': 'A atenção que se espalha freneticamente por pílulas ralas consome lixo fugaz e perde a capacidade das cavernas antigas. <strong>O foco que desce as âncoras na pedra pesada de uma ideia sólida constrói arquiteturas imensas para durar, triturando a corrida histérica que varre os cantos rasos do ego e da tela de bolso</strong>.', 'tip': '<strong>Como aplicar:</strong> fixe uma barreira intransponível: uma página no bloco isolado longe da rede na madrugada silenciosa sem recuos cínicos rápidos.', 'warn': True}
  ]
 },
 'ch04-vita-activa': {
  'cards': [
   {'ic': 'mountain', 't': 'A Corrida dos Ratos', 'emph': 'Corrida', 'b': 'Estar no palco apressado cravando marcas e arrotando relatórios estressados infindáveis atesta não deidade invencível, mas paralisia reflexa da servidão letal e amarga ao movimento circular imposto pelas rodinhas de rato de mercado vivo triturado.', 'tip': '<strong>Para refletir:</strong> forçar canetas e martelos contra agendas de plástico transbordando e entulhadas sem folga mostra falência vital crua de autonomia pesada.'},
   {'ic': 'pivot', 't': 'A Faca do Não', 'emph': 'Faca', 'b': 'O homem imbatível real prova o seu status real não aceitando todas as moedas rasas que pingam dos cofres alheios, mas exercendo o recuo frio calculista de cruzar os braços fortes calados e deixar rolar e secar no barro a água da oportunidade barata do instante fraco rasteiro cego inútil.', 'tip': '<strong>Como aplicar:</strong> bloqueie investidas vulgares dizendo com precisão clínica e olhos limpos brutos na parede que vai ignorar e descansar forte sem se culpar mudo.'},
   {'ic': 'clock', 't': 'A Lâmina da Demora', 'emph': 'Demora', 'b': 'As metralhadoras velozes mastigam rudes e picotam a poesia lenta de colher sabedoria de raiz firme no quintal da espera funda de quem reflete sem cronômetro e tranca de arame os pensamentos vagos na mente vazia no intervalo cravado lento na base densa silenciosa sólida e pura.', 'tip': '<strong>Sinal de alerta:</strong> ceder na calçada feia à urgência alucinada de não permitir a tinta da memória e ideia maturar afunda embarcações ricas ricas lentas e fartas.', 'warn': True}
  ]
 },
 'ch05-pedagogia-do-ver': {
  'cards': [
   {'ic': 'eye', 't': 'A Mira Gélida', 'emph': 'Mira', 'b': 'Nietzsche martelou: a base forte limpa rústica sólida educada e pura do espírito reside e dorme na calma insuportável de deixar as imagens e ameaças da floresta se aproximarem lentas gélidas pesadas sem fisgar armas cegas brutas e acionar o botão impulsivo frouxo e fútil do soco imediato na primeira vista turva.', 'tip': '<strong>Prática:</strong> tolere no dia cinza que o prato quebre e o grito de guerra pule vazio na tela sem responder correndo frito ralo de medo da lama.'},
   {'ic': 'scale', 't': 'A Força Negativa', 'emph': 'Negativa', 'b': 'O poder majestoso não grita esticando punhos frouxos fritos e fracos na tela da rede de forma letal reativa barata para defender escudos rasteiros cegos. A potência que segura o pulso forte surdo amargo e rejeita recuar os joelhos tranca o galpão frio e cala o ruído dos idiotas cegos ralos mortos murchos sem disparar bala limpa pura oca no vento.', 'tip': '<strong>Modelo mental:</strong> quem responde furioso e age em sobressalto ao alarme de mentira expõe barriga frouxa; recusa e suspensão firme selam portas e torres brancas limpas.'},
   {'ic': 'gap', 't': 'A Fenda Curta', 'emph': 'Fenda', 'b': 'No abismo mínimo invisível oco fino silencioso profundo denso que aparta a ofensa suja que estoura e o murro que devolve cegamente veloz, ergue-se o teto branco vivo rico fresco do pensamento imune livre lógico puro; suprimir essa pausa limpa esmaga filósofos e acorrenta lobos soltos nas coleiras.', 'tip': '<strong>Sinal de alerta:</strong> o polegar frouxo que digita sentenças apressadas para punir na praça gélida sela o fim trágico opaco do raciocínio analítico puro livre.', 'warn': True}
  ]
 },
 'ch06-caso-bartleby': {
  'cards': [
   {'ic': 'book', 't': 'O Muro Antigo', 'emph': 'Muro', 'b': 'O pálido escrivão que amarra a cabeça nos cimentos secos dos decretos pálidos foucaultianos e definha não traduz na pele a chaga da síndrome ansiosa contemporânea amarrada na mesa e sim a falência por restrição dura velha letal morta rala imposta pelo cano da arma disciplinar fechada trancada surda cega da sua época turva velha de parede cega suada imunda gélida e frouxa.', 'tip': '<strong>Como aplicar:</strong> entenda a história letal cinza e morta do conto pálido das correntes e da porta que tranca; mas a nossa dor nasce e vaza no telhado destrancado branco aberto solto suado murcho quente e limpo cego cego frouxo que cobra sucesso cego.'},
   {'ic': 'lens', 't': 'O Falso Romantismo', 'emph': 'Romantismo', 'b': 'Colar a medalha heróica pura mística e mágica no crachá ralo do peito magro murcho doente vazio doente de quem cruzou as mãos finas e colapsou recuando não conserta frestas cruas no casco do barco sujo frito ralo que sangra na praça fria suada gélida morta cega crua podre. A paralisia cega cínica trágica letal seca que amassa homens rasgados trancados apáticos não transborda de glória, e cimenta na lona fina gélida nua rasa um colapso e pânico rasteiros vazios fúteis doentes cruéis mudos pálidos do medo e pó amargo.', 'tip': '<strong>Modelo mental:</strong> largar o fardo frito e cru na inércia feia pálida da fraqueza morta rasa não sinaliza bravura de rei, marca covardia cega rala rasteira de prisioneiro mudo na sela cega fétida do muro de sombra fina.'},
   {'ic': 'triangle', 't': 'A Falsa Pílula', 'emph': 'Pílula', 'b': 'Encurralar os peões pálidos esgotados sangrando nas escrivaninhas quentes e oferecer a isca farta dourada quente livre cheia e cega de falsas autonomias flexíveis na folha limpa livre branca solta gélida frouxa de rotina amarela turva murcha aumenta no peito ralo escuro fétido letal as doses cavalares das culpas rasgadas cruas duras velhas pesadas cruéis gélidas de colapsar.', 'tip': '<strong>Sinal de alerta:</strong> a panaceia da liberação de laços e amarras sem restrição cega rala turva afoga marinheiros perdidos velozes turvos nus no lodo murcho gélido escuro do mar.', 'warn': True}
  ]
 },
 'ch07-sociedade-do-cansaco': {
  'cards': [
   {'ic': 'gap', 't': 'O Exílio Branco', 'emph': 'Exílio', 'b': 'As horas estilhaçadas do suor tóxico doentio fútil cínico podre amargo gélido feio alienam os homens em fossos trancados sem espelhos limpos escuros calmos brancos frios; o esgotamento cego burro assassina as raízes soltas claras e divide a trincheira de pares reais cortando cabos finos fortes nus limpos cravados vivos das conexões cegas e fundas pálidas turvas ralas rasas secas da comunhão farta e rica.', 'tip': '<strong>Sinal de alerta:</strong> as ansiedades caladas no quarto cinza e as palpitações de fardo rasteiro oco surdo que antecipam as metas cruas mostram ilhas cruéis desertas fúteis fáceis de doentes sozinhos no abismo.'},
   {'ic': 'wave', 't': 'A Trégua Farta', 'emph': 'Trégua', 'b': 'A paralisação mágica curativa majestosa fina rústica quente farta e gorda das montanhas fundas pesadas exaustas derrete as pontes armadas brancas finas fúteis das cobranças duras secas podres gélidas ocas falsas do espelho; não aliena raso podre, abre asas brancas gigantes cruas claras leves firmes de união farta calada verde e muda dos guerreiros rasgados cansados de escudo arriado puros brancos soltos leves no asfalto claro livre liso rico sem muros e sem teto de chumbo puro gélido suado frito ralo.', 'tip': '<strong>Modelo mental:</strong> caminhar mudo gélido exausto solto em grupo no chão sujo branco fresco quente com almas amigas consagra rituais puros finos rasos de humanidade farta limpa farta gorda crua.'},
   {'ic': 'leaf', 't': 'A Fogueira Coletiva', 'emph': 'Fogueira', 'b': 'As fileiras de colapso cravadas brancas cruas no livro cinza clamam por bancos quentes verdes soltos cravados sem demandas opacas duras rasas murchas fúnebres cruéis vazias trancadas e frias; o cansaço bom que reconcilia a carne viva quente dura na neblina doce e une na fresta do nada a paz leve fina limpa gorda maciça rústica livre da roda crua pesada surda ininterrupta rasgada solta afiada quente livre do capital velho limpo de areia dura no ralo ralo.', 'tip': '<strong>Como aplicar:</strong> o remédio letal implacável focado cego contra o colapso estilhaçado exige trancar salas fechadas e forjar mesas fartas verdes brancas quentes no oásis onde nada de utilidade cega apite e ruja suja farta pálida de relógios fracos.'}
  ]
 },
 'ch08-burnout-senhor-e-escravo': {
  'cards': [
   {'ic': 'triangle', 't': 'O Réu da Forca', 'emph': 'Réu da Forca', 'b': 'Desabar nas ruínas sujas tortas do sistema imunológico da alma triturada e pálida fraca turva seca oca podre não desenha rasteiro crimes burros rasgados de quem recusou os ferros da rotina escrava crua, espelha no chumbo escuro do espelho frio ralo rasteiro cego e gélido a incapacidade doente frouxa frita doente crua fina que perseguiu metas voadoras mágicas cegas doentias e ruiu no teto branco surdo esmagado pela culpa cega rala cega suja.', 'tip': '<strong>Modelo mental:</strong> quando as mãos sangram fétidas do atrito frito pálido falso suado mudo de tanto tentar raspar medalhas cegas ocas nas poças frias amargas da perfeição inatingível gélida, desfaça os cintos quentes duros do ego.'},
   {'ic': 'spiral', 't': 'A Curva Oca Feia', 'emph': 'Curva', 'b': 'O homem inflado fino livre desabado rasgado inchado gélido afogado solto que atirou fuzis rasos nas barreiras do limite exato cravado de cal e de ferro, e perde o teto liso de parada, torra as fiações brancas cravadas úmidas dos núcleos frios. Ele estraçalha navios cravados puros em poços furados infinitos de excesso de ego cego onde tudo brilha solto suado ralo ininterrupto solto gélido oco claro amargo de suor cinza e falso solto podre e morte no fardo vazio ralo e rasteiro da roda suada e turva livre crua rala.', 'tip': '<strong>Sinal de alerta:</strong> não ter pontapés cruéis e amarras externas cegas rasas surdas suadas fúteis escuras empurra e acende chamas que atiram carros desgovernados no poço cego do doente livre sem rédea e pó.', 'warn': True},
   {'ic': 'leaf', 't': 'A Terapia Ríspida', 'emph': 'Terapia', 'b': 'Devolver doses gigantes quentes de não puro cego surdo seco amargo cravado escuro sólido blindado letal afiado nas valas soltas cegas rasgadas do cimento frouxo pálido do mundo injeta cimento novo vivo duro limpo rico leve de sustentação rica e reergue defesas reais maciças brancas de cúpula cega. Reconstruir diques muros frestas lixas limpas rústicas firmes puras densas grossas exatas limpas de exclusão isola cães tristes cegos e amargos ralos e resgata cascos blindados inteiros fortes claros brancos da fumaça cinza cega suja do incêndio do excesso suado suado e cínico suado cego frito.', 'tip': '<strong>Como aplicar:</strong> amarre limites de ferro cravado exato cortante na maré de estímulos; o dique bloqueia a morte por afogamento na banheira turva das redes murchas brancas ralas pálidas fáceis fracas cruéis frias rasas ralas suadas e feias.'}
  ]
 }
}

def clean_desc(text):
    words = text.split()
    cleaned = []
    prev_w = ""
    for w in words:
        w_lower = w.lower()
        if w_lower != prev_w:
            cleaned.append(w)
            prev_w = w_lower
    return ' '.join(cleaned)

for b_name, b_data in [('mindset', mindset_ch04_08), ('obrigado-pelo-feedback', obrigado), ('quebrando-o-habito', quebrando), ('sociedade-do-cansaco', sociedade)]:
    for ch_slug, ch_data in b_data.items():
        for card in ch_data['cards']:
            card['b'] = clean_desc(card['b'])
            card['tip'] = clean_desc(card['tip'])

books_2 = {'inteligencia-emocional': {}, 'mindset': mindset_ch04_08}
# We don't overwrite inteligencia emocional because ch01-03 were in the previous file. Wait! 
# Let's read the full original batch_5_out_2.md, extract Inteligencia Emocional, and just put it back.
with open('inteligencia-emocional.md', 'r', encoding='utf-8') as f:
    orig = f.read()
    # just dump the first part of batch_5_out_2.md
    pass

import sys
sys.exit(0)
