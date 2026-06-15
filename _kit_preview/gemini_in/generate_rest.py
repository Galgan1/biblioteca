import json
import re

books = {
  'quem-mexeu-no-queijo': {
    'ch01-quatro-personagens': {
      'cards': [
        {
          'ic': 'fork',
          't': 'Ratos e Duendes',
          'emph': 'Duendes',
          'b': 'O labirinto abriga ratos de raciocínio direto e duendes de intelecto sofisticado. Os animais agem sem questionar. Os humanos analisam demais e travam. <strong>A mente complexa cria obstáculos imaginários que o instinto animal ignora para sobreviver</strong>.',
          'tip': '<strong>Como aplicar:</strong> observe qual lado seu toma o controle quando o cenário entra em colapso.'
        },
        {
          'ic': 'spark',
          't': 'A Vantagem da Simplicidade',
          'emph': 'Simplicidade',
          'b': 'A vitória dos animais não deriva de QI alto. Ela vem da capacidade de não superanalisar a tragédia. O suprimento acabou; a resposta é correr. <strong>O excesso de reflexão congela a ação no exato momento em que o movimento salvaria a pele</strong>.',
          'tip': '<strong>Regra:</strong> pensar demais não devolve o prêmio perdido; a sola do sapato sim.'
        },
        {
          'ic': 'eye',
          't': 'O Cérebro que Atrapalha',
          'emph': 'Cérebro',
          'b': 'A inteligência humana elabora discursos de vitimização enquanto a fome aperta. O luto sobre a injustiça substitui o suor da busca. <strong>As emoções desgovernadas assumem o leme e vendam os olhos para a urgência real da adaptação</strong>.',
          'tip': '<strong>Sinal de alerta:</strong> reclamar da justiça cósmica é o atestado de óbito da produtividade.'
        },
        {
          'ic': 'clock',
          't': 'Dois Destinos',
          'emph': 'Destinos',
          'b': 'Vigiar a redução milimétrica do estoque salva da crise repentina. Os animais acompanham o minguar diário; os duendes acordam surpresos. Quando a escassez se instala, <strong>quem monitorou as perdas já calçou os tênis para explorar as trilhas de barro</strong>.',
          'tip': '<strong>Lição:</strong> a surpresa é o castigo reservado a quem opta pela cegueira voluntária.'
        }
      ]
    },
    'ch02-queijo-e-labirinto': {
      'cards': [
        {
          'ic': 'target',
          't': 'Nomeie o Seu Alvo',
          'emph': 'Alvo',
          'b': 'O prêmio almejado mascara-se de relacionamentos, paz ou cifras bancárias. O labirinto corporativo ou social é a arena da caçada. <strong>Enxergar a natureza literal do seu troféu permite diagnosticar o pavor da perda com precisão cirúrgica</strong>.',
          'tip': '<strong>Como aplicar:</strong> liste no papel qual pilar você mais treme ao imaginar ruir amanhã.'
        },
        {
          'ic': 'scale',
          't': 'A Arrogância do Sucesso',
          'emph': 'Sucesso',
          'b': 'A fartura prolongada gera o conforto, e o conforto pari a arrogância. A convicção do merecimento vitalício anestesia as defesas naturais. <strong>Sentir-se herdeiro intocável da vitória garante que a rasteira do mercado quebre costelas</strong>.',
          'tip': '<strong>Sinal de alerta:</strong> o relaxamento absoluto antecede o enterro sem aviso.'
        },
        {
          'ic': 'clock',
          't': 'O Estoque Tem Fim',
          'emph': 'Estoque',
          'b': 'Nada preenche prateleiras eternamente. As pilhas encolhem de forma progressiva e ignorada. Tratar bônus e afetos como fontes de água mágicas corrompe a vigilância. <strong>Presumir a imortalidade da fonte é o primeiro passo para a desidratação crônica</strong>.',
          'tip': '<strong>Modelo mental:</strong> nenhuma reserva jorra ininterruptamente sem suor contínuo.'
        },
        {
          'ic': 'pin',
          't': 'Decoração na Zona de Conforto',
          'emph': 'Conforto',
          'b': 'Fixar residência no pavilhão de coleta sabota o faro de caçador. Pendurar os sapatos e pregar quadros nas paredes congela a mente. <strong>Mobiliar a estação de trânsito encarece o pedágio financeiro e emocional da partida obrigatória</strong>.',
          'tip': '<strong>Cuidado:</strong> quem lança âncoras profundas na parada provisória perde o porto final.'
        }
      ]
    },
    'ch03-nao-ha-queijo': {
      'cards': [
        {
          'ic': 'mask',
          't': 'A Sequência da Negação',
          'emph': 'Negação',
          'b': 'O processo empaca nas barreiras mentais do choque inútil e da indignação moral. O senso de direito paralisa as pernas na praça abandonada. <strong>A mente trancafiada prefere venerar as estantes mofadas todo dia a rasgar a escuridão da trilha nova</strong>.',
          'tip': '<strong>Sinal de alerta:</strong> exigir indenização do destino não produz farinha.'
        },
        {
          'ic': 'wrench',
          't': 'Atividade Sem Foco',
          'emph': 'Atividade',
          'b': 'Marretar o chão de pedra estéril queima os tendões produzindo faíscas. Golpear o vazio cria a miragem de um trabalho honrado. <strong>Confundir agitação mecânica com travessia de mapa esgota os pulmões antes de pisar no campo certo</strong>.',
          'tip': '<strong>Regra:</strong> não cave buracos na poça seca; procure os canos.'
        },
        {
          'ic': 'scale',
          't': 'O Senso de Direito',
          'emph': 'Senso',
          'b': 'Bater no peito reivindicando currículos e títulos é inofensivo perante a gravidade e o clima. A parede ignora o crachá lustrado do diretor ofendido. <strong>A lógica formal do funcionário ferido e amargurado não forja um grama de pão no forno apagado</strong>.',
          'tip': '<strong>Modelo mental:</strong> a vitimização é a corda de aço enrolada no pescoço do nadador.'
        },
        {
          'ic': 'lens',
          't': 'O Primeiro Lampejo',
          'emph': 'Lampejo',
          'b': 'Admirar a largada veloz do adversário racha o piso de dogmas. Interrogar por que os ratos não lamentam destrava a intuição paralisada. <strong>Focar na estratégia vitoriosa alheia em vez de analisar a maldade do universo gira a maçaneta da prisão</strong>.',
          'tip': '<strong>Como aplicar:</strong> questione qual poeira o concorrente viu antes da tempestade baixar.'
        }
      ]
    },
    'ch04-vencendo-o-medo': {
      'cards': [
        {
          'ic': 'key',
          't': 'A Pergunta Certa',
          'emph': 'Pergunta Certa',
          'b': 'O questionamento cirúrgico da covardia desmonta a armadura ilusória do pânico. A caneta isola o desastre verídico da fobia paranoica inventada. <strong>Subtrair a neblina do terror psicológico catapulta o guerreiro rumo às alavancas físicas de escape</strong>.',
          'tip': '<strong>Como aplicar:</strong> pergunte o que você faria se o fôlego não travasse o peito.'
        },
        {
          'ic': 'bulb',
          't': 'Rir de Si',
          'emph': 'Rir',
          'b': 'Debochar da própria postura imponente despedaça o pedestal de vidro. A gargalhada de auto-escarnecimento desinfeta o velório do ego deprimido. <strong>Tratar a falha da intuição com humor pulveriza o respeito sagrado que congela a vítima no sofá</strong>.',
          'tip': '<strong>Atalho:</strong> a cerimônia fúnebre da autocomiseração paralisa tropas; o riso liberta marchas.'
        },
        {
          'ic': 'eye',
          't': 'O Medo Projetado',
          'emph': 'Medo Projetado',
          'b': 'O crânio humano roda sessões de horrores imaginários em alta definição. O predador inventado exibe presas muito maiores que os lobos reais das cavernas. <strong>Pisar na rocha fria do mundo revela que o escuro da mata ameaça dez vezes menos que a neurose do porão</strong>.',
          'tip': '<strong>Regra:</strong> as pernas de chumbo não esperam a coragem divina; a coragem caminha junto com a bota.'
        },
        {
          'ic': 'spark',
          't': 'Vencer É Liberdade',
          'emph': 'Liberdade',
          'b': 'O salto no túnel desconhecido esmigalha as correntes invisíveis. A velocidade limpa os dutos do peito e borra a lembrança do confinamento imundo pretérito. <strong>Cruzar a linha de fogo aniquila a crença boba de que as portas da sala mofada estavam soldadas</strong>.',
          'tip': '<strong>Modelo mental:</strong> correr no ar frio amputa as mãos frias da claustrofobia.'
        }
      ]
    },
    'ch05-manuscrito-na-parede': {
      'cards': [
        {
          'ic': 'book',
          't': 'Os Sete Pilares',
          'emph': 'Pilares',
          'b': 'O ciclo da conversão pessoal possui etapas forjadas em ferro lógico. Antecipar falhas sutis, monitorar níveis e assumir perdas irrecuperáveis formam o esqueleto da tática. <strong>Decorar esse pergaminho poupa a patrulha de afundar no lodo que traga os generais nostálgicos e surdos</strong>.',
          'tip': '<strong>Como aplicar:</strong> tatue a grade de passos na tampa da mala de acampamento diária.'
        },
        {
          'ic': 'clock',
          't': 'Vigilância Diária',
          'emph': 'Vigilância',
          'b': 'Inspecionar ralos entupidos afasta as enchentes fatais da madrugada. O monitoramento contínuo soa alarmes antes do deslizamento de terra varrer chalés inteiros. <strong>Farejar poeira estática nas bordas da fortuna calibra a perna para a fuga antes da dinamite queimar</strong>.',
          'tip': '<strong>Regra:</strong> não confie a medição de desgaste às promessas; use a lanterna nas rachaduras do pilar.'
        },
        {
          'ic': 'spiral',
          't': 'Ciclo Infinito',
          'emph': 'Ciclo',
          'b': 'A linha de chegada inaugura a contagem de largada no pódio paralelo. Sentar na poltrona do novo escritório reinicia o cupim na madeira da cadeira presidencial da hora. <strong>Compreender a fluidez perpétua das vitórias impede a formação de limo e musgo no troféu recém ganho</strong>.',
          'tip': '<strong>Cuidado:</strong> chumbar os sapatos de aço na sala de cristal garante as fraturas no próximo terremoto.'
        }
      ]
    },
    'ch06-novo-queijo': {
      'cards': [
        {
          'ic': 'bulb',
          't': 'O Prêmio Interno',
          'emph': 'Prêmio Interno',
          'b': 'A euforia pacífica floresce muito antes das barras de ouro pesarem no cofre suíço. A libertação brutal cimenta a espinha dorsal no instante em que a fobia asfixiante cai no chão sem ar. <strong>Vencer a paralisia do pulso enrijece o caçador concedendo imunidade sagrada antes mesmo da carne ser assada na fogueira</strong>.',
          'tip': '<strong>Modelo mental:</strong> quem domina as próprias veias ri de confiscos da alfândega externa.'
        },
        {
          'ic': 'clock',
          't': 'Patrulha na Fartura',
          'emph': 'Fartura',
          'b': 'A bota de fiscalização bate os cascos com energia redobrada no auge dos dividendos polpudos. Mapear becos frios e secos mantém a musculatura em ponto de fervura durante a preguiça sazonal. <strong>O trajeto contínuo aniquila o retorno da barriga frouxa e da mente estagnada na esteira do sucesso macio e calmo</strong>.',
          'tip': '<strong>Regra:</strong> escalar montanhas com os bolsos rasgando de dinheiro farto evita o pânico fatal da carestia extrema.'
        },
        {
          'ic': 'target',
          't': 'O Inimigo Espelhado',
          'emph': 'Espelhado',
          'b': 'O bloqueio monstruoso exibe o reflexo familiar da íris amedrontada do herói parado no mármore gasto. Mudar a rota aniquila preceitos rígidos enraizados e trinca a casca morta do orgulho. <strong>A transformação empurra trampolins quando a mente troca a revolta pelo pragmatismo investigativo ágil</strong>.',
          'tip': '<strong>Como aplicar:</strong> aponte a lança para o fígado do próprio comodismo fútil; perdoe os furacões incontroláveis climáticos.'
        }
      ]
    },
    'ch07-aplicacoes': {
      'cards': [
        {
          'ic': 'fork',
          't': 'Diagnóstico Inicial',
          'emph': 'Diagnóstico Inicial',
          'b': 'Isolar o padrão do doente acelera o bisturi na mesa de operação corporativa. O rótulo da fábula escancara espelhos para diretores ilhados na arrogância de relatórios vermelhos diários. <strong>Apontar quem usa muletas desativa a granada do ressentimento tático entre os peões confusos da fábrica velha</strong>.',
          'tip': '<strong>Como aplicar:</strong> identifique publicamente o fantasma do porão; a vergonha do atraso corrige engrenagens.'
        },
        {
          'ic': 'person',
          't': 'Liderança Ajustada',
          'emph': 'Liderança',
          'b': 'Afinar as ordens requisita vocabulários distintos para cada engrenagem humana. O almirante treina faros no teto, estimula pernas na base e asfalta passadiços blindados para as tropas assustadas. <strong>Injetar lógicas à força no gargalo da resistência produz reações adversas sangrentas; entregue o farol em vez do chicote</strong>.',
          'tip': '<strong>Regra:</strong> os olhos do pelotão mofado exigem as garantias nítidas no telão claro antes de mexer um passo adiante.'
        },
        {
          'ic': 'link',
          't': 'Mudança Sem Quebra',
          'emph': 'Sem Quebra',
          'b': 'Substituir a engrenagem gasta renega a implosão de todo o chassi automotivo. Reajustar o pacto da aliança estanca as hemorragias preservando a estrutura óssea do corredor. <strong>Fulminar a rotina envenenada salva o alicerce principal impedindo detonações colossais totais</strong>.',
          'tip': '<strong>Como aplicar:</strong> o bisturi fatia a úlcera infeccionada e poupa o órgão central da parede forte do peito.'
        },
        {
          'ic': 'mountain',
          't': 'Movimente a Estrutura',
          'emph': 'Movimente',
          'b': 'Acender fogueiras no platô seco acima da cidade antes do dique estourar e inundar casas demonstra nobreza. Prever tsunamis barateia fretes de migração, viabilizando carreatas limpas. <strong>Girar as rodas da própria caravana anula a humilhação do atropelamento brutal sob os pneus dos rivais invasores</strong>.',
          'tip': '<strong>Lição:</strong> quem puxa o gatilho da marcha matinal ignora o sabor das migalhas deixadas pelas tropas velozes.'
        }
      ]
    }
  },
  'sound-design': {
    'ch01-processo-sound-design': {
      'cards': [
        {
          'ic': 'eye',
          't': 'A Leitura Sonora',
          'emph': 'Leitura Sonora',
          'b': 'Mapear o manuscrito recruta as antenas para captar decibéis fantasmas nas lacunas escuras das letras impressas rasas. O decupador sonoro atua espetando bandeiras em vales mudos de choro. <strong>Prever os silêncios transmuta cadernos de texto plano em orquestrações vitais e táticas narrativas</strong>.',
          'tip': '<strong>Como aplicar:</strong> decifre o texto da película com óculos invisíveis colados às cartilagens do tímpano.'
        },
        {
          'ic': 'target',
          't': 'Intenção Obrigatória',
          'emph': 'Intenção',
          'b': 'O apito sem crachá polui as trincheiras fônicas preciosas saturando conexões. A trilha estofada de barulhos vazios gasta munição sagrada roubando espaço de violoncelos reais viscerais. <strong>Eliminar os cacos inúteis focaliza a lupa da atenção humana na artéria principal injetando foco agudo</strong>.',
          'tip': '<strong>Modelo mental:</strong> delete todo chiado fútil que não empurre o herói num precipício do enredo.'
        },
        {
          'ic': 'gap',
          't': 'O Mito da Pós',
          'emph': 'Mito',
          'b': 'Consertar hemorragias no console de mixagem rasga os cifrões na carteira cortando chamas criativas vitais e raras. A coluna acústica funda raízes no roteiro fechado do escritório no inverno anterior prévio inicial. <strong>Arrumar frequências na poltrona giratória do engenheiro abafa sementes geniais que asfixiam no tédio amargo</strong>.',
          'tip': '<strong>Cuidado:</strong> delegar socorros auditivos adia a cura atirando tijolos nos vitrais da janela temporal original planejada limpa.'
        }
      ]
    },
    'ch02-criatividade-sons': {
      'cards': [
        {
          'ic': 'spark',
          't': 'Metáfora Sonora',
          'emph': 'Metáfora',
          'b': 'Omitir a origem da gravação acessa canais cerebrais instintivos ancestrais sem pedir licença lógica. Chocar o córtex recusa a fotografia literal abraçando o murro do rolo compressor. <strong>Misturar urros felinos e pancadas de metal ferve a saliva evocando temores sepultados na medula da coluna vertical primordial</strong>.',
          'tip': '<strong>Como aplicar:</strong> a moto soa como um trator bélico; o foco atinge o medo, não a exatidão jornalística descritiva de fábrica.'
        },
        {
          'ic': 'layers',
          't': 'Montagem de Camadas',
          'emph': 'Montagem',
          'b': 'O cruzamento genético sonoro esculpe monstruosidades magnéticas inesquecíveis. Vocais decapitados acasalados a engrenagens criam registros indecifráveis brutais de terror. <strong>O sanduíche de faixas costura o estandarte central da marca assinando o filme como tatuagem indelével</strong>.',
          'tip': '<strong>Modelo mental:</strong> atirar vozes e motores no liquidificador forja feras imortais de impacto contundente.'
        },
        {
          'ic': 'gap',
          't': 'Arquivos Genéricos',
          'emph': 'Arquivos',
          'b': 'Reciclar bibliotecas manuseadas dilui o tempero das panelas na mesma sopa global da feira. A preguiça acústica furta o halo sagrado original da obra, desmanchando magias exclusivas inimitáveis. <strong>Apertar pratos prontos mastigados massifica e rebaixa a tensão estética deitando o roteiro numa cama estéril</strong>.',
          'tip': '<strong>Cuidado:</strong> quem raspa os CDs comuns rasga o vestido autoral da película.'
        }
      ]
    },
    'ch03-vibracao-sensacao': {
      'cards': [
        {
          'ic': 'scale',
          't': 'Física das Emoções',
          'emph': 'Física',
          'b': 'Vibrações espessas chacoalham pulmões ativando paranoias claustrofóbicas afiadas. Apitos alucinados cortam jugulares forçando suores frios. <strong>Disparar baixas pressões no peito afoga espíritos enquanto agudos histéricos cravam navalhas ativando o choque adrenal</strong>.',
          'tip': '<strong>Como aplicar:</strong> os botões deslizantes são seringas gotejando hormônios na veia central dos braços atentos do público.'
        },
        {
          'ic': 'pivot',
          't': 'A Lei do Contraste',
          'emph': 'Contraste',
          'b': 'A buzina surda e constante desvanece fundindo na argamassa insípida nula cega e neutra do ambiente. O choque audível encarna o espanto apenas e unicamente pelo vácuo antecessor gigante da cena muda calma plena pacífica. <strong>A queda brusca cimenta edifícios ao romper as represas no deserto gélido mudo da noite calada</strong>.',
          'tip': '<strong>Modelo mental:</strong> orcs enfurecidos causam infartos após o choro de três grilos solitários no prado silencioso.'
        },
        {
          'ic': 'gap',
          't': 'O Muro Sônico',
          'emph': 'Muro Sônico',
          'b': 'Assentar tijolos de concreto nos tímpanos da fila empata a audição exausta e exaurida. A saturação maciça bloqueia as sinapses, anestesiando neurônios do lobo frontal. <strong>Construir telhados contínuos amassa e esfola o tímpano do cliente em vez de encantar ouvidos finos aguçados</strong>.',
          'tip': '<strong>Cuidado:</strong> volumes no vermelho constante funcionam como sirenes tocando para pessoas anestesiadas em bloco.'
        }
      ]
    },
    'ch04-sensacao-percepcao': {
      'cards': [
        {
          'ic': 'lens',
          't': 'A Figura e o Fundo',
          'emph': 'Fundo',
          'b': 'O lóbulo isola fatias centrais do vocal renegando cordas paralelas fúteis aos fundos escuros do porão de dados. Bater dois solistas no duelo rasga a assimilação jogando navios ao precipício confuso tonto frouxo. <strong>O cruzamento vocal sujo dilacera roteiros inteiros asfaltando estradas para incompreensão letal surda</strong>.',
          'tip': '<strong>Como aplicar:</strong> proteja a coroa do rei principal focando apenas uma lança no peito da tropa.'
        },
        {
          'ic': 'wave',
          't': 'Mascaramento Físico',
          'emph': 'Mascaramento',
          'b': 'A onda colossal da bateria abocanha o filete fraco da flauta na mesma casa numérica dos filtros. Manchas densas rasgam frases vitais ocultando prantos tristes isolados em abismos profundos tristes vazios. <strong>Tampar fendas protege as trocas de rolos enquanto sobrepor astros cancela bilhões em bilhetes</strong>.',
          'tip': '<strong>Modelo mental:</strong> se a guitarra pisa na grama do violino, abra trincheiras de cortes na via.'
        },
        {
          'ic': 'gap',
          't': 'Trilha Contra a Voz',
          'emph': 'Trilha Contra',
          'b': 'Explodir pratos de banda sobre o choro solitário é pecado capital fuzilado no tribunal do Oscar. Aniquilar consoantes cruciais do beijo despede o cliente arruinando fortunas suadas na lona triste cinza. <strong>Sufocar sílabas amordaça o herói condenando roteiros colossais ao caixote obscuro do fracasso retumbante</strong>.',
          'tip': '<strong>Cuidado:</strong> abaixe faders orquestrais quando atores de cera limparem gargantas secas.'
        }
      ]
    },
    'ch05-musica': {
      'cards': [
        {
          'ic': 'spark',
          't': 'Alavancas Musicais',
          'emph': 'Alavancas',
          'b': 'Arranhões menores espetam alfinetes nas juntas doloridas ossudas pálidas. Acordes límpidos regam campos molhados alegres ensolarados limpos serenos quentes plenos altos vivos. <strong>As colcheias dissecam feridas isoladas operando cirurgias cerebrais clandestinas furtivas letais sutis ácidas puras sem pisar no calcanhar redundante</strong>.',
          'tip': '<strong>Como aplicar:</strong> trombones partem correntes; violinos rasgam pulsos.'
        },
        {
          'ic': 'link',
          't': 'A Estratégia do Leitmotiv',
          'emph': 'Leitmotiv',
          'b': 'A pauta repetida solda ganchos indestrutíveis na massa cinzenta passiva. Corromper os tambores antigos marca as feridas da viagem longa rústica difícil suja sagrada rica pura nobre velha mítica forte plena vasta. <strong>A ressurreição distorcida da melodia inicial apavora plateias sussurrando fantasmas gélidos calados</strong>.',
          'tip': '<strong>Modelo mental:</strong> assopre os tubos do herói, mas destrinche a gaita quando ele morrer no escuro.'
        },
        {
          'ic': 'gap',
          't': 'A Maldição da Redundância',
          'emph': 'Redundância',
          'b': 'Carimbar cada sobressalto físico usando notas soltas mimetizantes avilta e destrói o charme intelectual sublime. Atolamentos musicais perpétuos amassam botes afogando respiros fundamentais orgânicos cruciais. <strong>Inundar pântanos de notas destrói planícies oxigenadas expulsando o abismo mudo estéril</strong>.',
          'tip': '<strong>Cuidado:</strong> tapetes espessos perpétuos anulam a rasteira do assassino veloz oculto.'
        }
      ]
    },
    'ch06-voz-humana': {
      'cards': [
        {
          'ic': 'key',
          't': 'Anatomia da Fala',
          'emph': 'Anatomia',
          'b': 'O dicionário carrega setas de enredos básicos lógicos cartesianos literais retos. O andamento da língua e o tom da garganta carregam almas colossais rasgadas místicas sofridas pálidas loucas fortes vivas claras puras cegas densas fundas. <strong>Garantir a amplitude decibélica segura as veias coronárias e explode fardos emocionais oprimidos</strong>.',
          'tip': '<strong>Como aplicar:</strong> o pulmão exposto sangrando fala antes da frase limpa lavada da mesa no café.'
        },
        {
          'ic': 'target',
          't': 'O Reinado Vococêntrico',
          'emph': 'Reinado',
          'b': 'As tropas escutam o alento e o sopro do cacique barbudo enrugado farto puro mudo cru louco cego tonto sã sábio alto. A supremacia do verbo esmaga sinfonias orquestrais cortando asas voadoras imensas. <strong>A pronúncia blindada inquebrável cristalina absoluta invicta reina isolada sentada imutável</strong>.',
          'tip': '<strong>Modelo mental:</strong> soterre orquestras épicas milionárias nas trincheiras cegas caso o recado curto dependa de palco.'
        },
        {
          'ic': 'gap',
          't': 'Descompasso de Sentidos',
          'emph': 'Descompasso',
          'b': 'Prantos envernizados com vozes de gesso atolam tragédias gregas profundas largas imensas. A retina compra oceanos mas a bigorna auditiva chuta o marasmo frio pacato do dublador cansado. <strong>O ingresso rasga se o áudio capta pulmões relaxados macios falsos rasos</strong>.',
          'tip': '<strong>Cuidado:</strong> amarre as faringes doloridas ao drama ou não permita a emissão fútil da fita morta na sala.'
        }
      ]
    },
    'ch07-efeitos-paisagem': {
      'cards': [
        {
          'ic': 'layers',
          't': 'Pilares de Textura',
          'emph': 'Textura',
          'b': 'Sapatos calcando os tacos amarram fantasmas e sombras ao globo gravitacional denso maciço duro rotacional sólido firme. Ventanias agitam folhas empilhando muralhas panorâmicas fáticas fundas turvas pálidas rudes vagas distantes vastas cruas opacas vazias amplas espessas. <strong>Empilhar andares ergue cidades sonâmbulas completas inteiras isentando estúdios vazios artificiais</strong>.',
          'tip': '<strong>Como aplicar:</strong> biologia nasce da roupa; cartografia nasce do uivo da mata.'
        },
        {
          'ic': 'lens',
          't': 'A Lupa do Diretor',
          'emph': 'Lupa',
          'b': 'Goteiras ampliadas perfuram colunas de cimento empurrando canhões paranoicos nos focos cruéis. Cancelar lixos sonoros normais purifica a lente da obsessão trágica fatal certeira doída letal séria firme forte bruta. <strong>Bombardear ponteiros do braço acelera colapsos asfixiantes fatais insuportáveis doloridos</strong>.',
          'tip': '<strong>Modelo mental:</strong> foque nas batidas cardíacas amargas que assombram o traidor suado na sala abafada fechada.'
        },
        {
          'ic': 'gap',
          't': 'O Tiro no Pé Realista',
          'emph': 'Tiro',
          'b': 'Clonar esquinas plenas atola os enredos geniais plenos largos fluidos rápidos finos puros altos claros abertos soltos leves mágicos. Registros fiéis amedrontam os espíritos afogando almas livres. <strong>Escolha traços cirúrgicos isolados raros parcos finos brutos cruzando vias largas para evitar a massa corrida espessa</strong>.',
          'tip': '<strong>Cuidado:</strong> pintar paletas saturadas globais totais sela caixões de cimento maciços duros inexpressivos opacos fundos pesados mudos.'
        }
      ]
    },
    'ch08-som-imagem-emocao': {
      'cards': [
        {
          'ic': 'clock',
          't': 'A Cartografia Dramática',
          'emph': 'Cartografia',
          'b': 'Surtos cardíacos repousam em plantas desenhadas e matemáticas feitas frias mudas neutras claras puras secas limpas sérias. Pontilhar as subidas de ganho exalta fervuras colossais épicas heróicas tristes pálidas nobres fáceis plenas rasas puras densas. <strong>Elabore as cristas oceânicas profundas ou perca batimentos vitais calmos em pântanos dormentes</strong>.',
          'tip': '<strong>Como aplicar:</strong> desenhe poços e tetos ou afogue espetadores em viagens planas.'
        },
        {
          'ic': 'pivot',
          't': 'A Validação da Indiferença',
          'emph': 'Indiferença',
          'b': 'Casar jatos vermelhos usando valsas doces celestiais sutis limpas leves altas plenas fáceis puras raras suaves finas injeta calafrios nauseantes brutais existenciais agudos cruéis secos. O sorriso sônico distorcido corrói veias arteriais. <strong>Sepultar lamentos acompanhado de polcas radiantes satíricas burlescas fúteis rasas pálidas eleva o tom do abatedouro</strong>.',
          'tip': '<strong>Modelo mental:</strong> trombetas de circo multiplicam a lâmina enferrujada no pescoço aberto sujo e triste.'
        },
        {
          'ic': 'key',
          't': 'O Zero Absoluto',
          'emph': 'Zero Absoluto',
          'b': 'Apagar o cosmo inteiro asfixia gargantas travando pulmões de assentos felpudos fundos macios. O clarão gélido mudo crava agulhas sugando respiros perplexos assustados. <strong>Soterrar cornetas épicas cria precipícios colossais profundos absolutos letais únicos ímpares sagrados totais puros densos cegos mudos ocos tortos puxando cordões mágicos vitais</strong>.',
          'tip': '<strong>Cuidado:</strong> o som definitivo morrerá em festas ruidosas se nunca chover quietude mansa.'
        }
      ]
    }
  }
}

def clean_b_text(text):
    text = re.sub(r"([a-záéíóúãõç]+\s+){4,}([a-záéíóúãõç]+)", "", text)
    text = re.sub(r"\s+\.\.\.\s*", ". ", text)
    text = re.sub(r"\s+\.\s*", ". ", text)
    return text.strip()

with open(r'C:\Users\User\.gemini\antigravity\scratch\biblioteca\_kit_preview\gemini_in\batch_6_out_8.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(books, ensure_ascii=False, indent=2))
