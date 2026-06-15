import json

def get_b3():
    return {
        "ch01-o-desafio-do-futuro": {
            "cards": [
                {"ic": "spark", "t": "O Salto Vertical", "emph": "Vertical", "b": "Copiar o que funciona e espalhar pelo mundo é caminhar na horizontal. <strong>O futuro exige o salto vertical de criar algo do absoluto nada: ir de 0 a 1.</strong> A tecnologia pura, e não a mera cópia em massa, é o que empurra a humanidade para a frente.", "tip": "<strong>Pergunta-chave:</strong> a sua ideia constrói o amanhã ou apenas empacota melhor o que já existe?"},
                {"ic": "lens", "t": "A Pergunta Contrária", "emph": "Pergunta Contrária", "b": "Qual verdade vital você enxerga com clareza, mas quase ninguém concorda? <strong>As teses fáceis já foram espremidas pela concorrência; a oportunidade real veste a roupa do absurdo.</strong> O futuro mora na intersecção entre a sua certeza e a ignorância da maioria.", "tip": "<strong>Modelo mental:</strong> o que é óbvio para você e heresia para os rivais costuma ser a mina de ouro."},
                {"ic": "wave", "t": "Cópia Contra Invenção", "emph": "Invenção", "b": "Confundir avanço humano com a globalização é a cegueira mais cara do mercado. <strong>Multiplicar métodos velhos pelo mundo inteiro só esgotará o planeta mais depressa.</strong> Precisamos de invenções singulares para sustentar as décadas seguintes.", "tip": "<strong>Sinal de alerta:</strong> uma startup que só importa modelos estrangeiros está fadada a competir até sangrar.", "warn": True}
            ]
        },
        "ch02-festa-como-em-1999": {
            "cards": [
                {"ic": "scale", "t": "As Lições do Medo", "emph": "Medo", "b": "Após o estouro da bolha, o mercado abraçou o pensamento miúdo de avançar devagar. <strong>Esses dogmas ensinaram uma geração a pensar pequeno e ter aversão patológica à ousadia.</strong> Quando todos concordam sobre como agir, a mediocridade assume o volante.", "tip": "<strong>Armadilha:</strong> as 'boas práticas' de mercado costumam ser apenas cicatrizes do pânico de crises passadas."},
                {"ic": "spark", "t": "Ousadia Acima da Agilidade", "emph": "Ousadia", "b": "É mil vezes melhor arriscar tudo numa visão grandiosa do que se esconder num pragmatismo envergonhado. <strong>Um plano ruim mas audacioso esmaga qualquer rodada de adaptações ágeis sem direção.</strong> Construa o novo ignorando a concorrência miúda.", "tip": "<strong>Prática:</strong> inverta os clichês modernos para encontrar apostas que os investidores frouxos temem bancar."}
            ]
        },
        "ch03-todas-as-empresas-felizes-sao-diferentes": {
            "cards": [
                {"ic": "target", "t": "A Farsa da Concorrência", "emph": "Concorrência", "b": "Disputar mercado a tapas aniquila as margens e é o esporte de quem não inova. <strong>O sucesso duradouro só aparece quando você é o único dono do nicho, resolvendo algo de um jeito inimitável.</strong> Trata-se da excelência radical que torna o oponente irrelevante.", "tip": "<strong>Regra:</strong> crie um jogo novo onde só exista um competidor competente: você."},
                {"ic": "key", "t": "Criar Não Basta, Capture", "emph": "Capture", "b": "As companhias aéreas transportam a humanidade, mas vivem no vermelho; o Google acumula montanhas de caixa. <strong>Distribuir valor é nobre, mas você precisa de muralhas para reter a riqueza gerada.</strong> Onde a disputa por preços corre solta, o lucro evapora.", "tip": "<strong>Pergunta-chave:</strong> quanto do valor financeiro que o seu produto cria acaba no seu próprio bolso?"},
                {"ic": "mask", "t": "O Teatro do Mercado", "emph": "Teatro", "b": "O gigante monopolista jura sofrer ameaças para despistar reguladores; a padaria jura ser ímpar para inflar o ego. <strong>A economia é um palco de narrativas enviesadas onde a verdade nunca está na vitrine.</strong> Aprenda a rasgar a publicidade alheia.", "tip": "<strong>Sinal de alerta:</strong> empresas que insistem histericamente que não têm concorrentes costumam estar na mira de predadores.", "warn": True}
            ]
        },
        "ch04-a-ideologia-da-concorrencia": {
            "cards": [
                {"ic": "sword", "t": "A Cegueira da Rivalidade", "emph": "Cegueira", "b": "Treinados desde cedo para bater as notas do colega, engessamos o músculo criativo. <strong>A obsessão irracional por destruir o vizinho nos arrasta para batalhas onde o troféu não paga o curativo.</strong> O foco excessivo no rival drena o oxigênio da invenção.", "tip": "<strong>Modelo mental:</strong> pare de olhar pelo retrovisor; o seu inimigo real é o limite do impossível."},
                {"ic": "fork", "t": "Lucro ou Vaidade", "emph": "Vaidade", "b": "Quanto mais as empresas se clonam, mais a vaidade dos fundadores entra em cena e queima caixa. <strong>Em cenários caóticos, a jogada mais antinatural e lucrativa é engolir o ego e fundir operações.</strong> O dinheiro grosso prefere a calmaria do monopólio.", "tip": "<strong>Sinal de alerta:</strong> queimar os tubos para aniquilar um rival minúsculo costuma ser um erro passional.", "warn": True}
            ]
        },
        "ch05-vantagem-do-pioneiro": {
            "cards": [
                {"ic": "layers", "t": "Os Pilares da Defesa", "emph": "Defesa", "b": "Para erguer um império blindado, a sua tecnologia precisa ser matematicamente dez vezes superior. <strong>Melhorias tímidas de vinte por cento são fatiadas pela concorrência; apenas saltos brutais criam o efeito de rede inescapável.</strong>", "tip": "<strong>Prática:</strong> se a demonstração do produto não causar espanto imediato, jogue no lixo e volte à bancada."},
                {"ic": "clock", "t": "A Coroa do Retardatário", "emph": "Retardatário", "b": "Largar na frente só garante o gasto de desbravar a selva com o próprio suor. <strong>O xeque-mate genial consiste em entrar depois, polir o erro dos apressados e reinar no mercado pelas décadas seguintes.</strong> O valor titânico de uma empresa mora no futuro.", "tip": "<strong>Modelo mental:</strong> pioneiros desbravam e quebram as pernas; os últimos a chegar organizam o asfalto e ficam com a fortuna."},
                {"ic": "mountain", "t": "A Genialidade do Nicho", "emph": "Nicho", "b": "Tentar abraçar a população global no dia um é a cartilha clássica para torrar investimento e não entregar nada. <strong>Domine um aquário microscópico, instale uma devoção doentia nos usuários e só então expanda para o oceano.</strong> Nenhum monopólio nasce gigante.", "tip": "<strong>Regra:</strong> mire num alvo tão ridículo e isolado que os predadores maiores achem perda de tempo olhar para ele."}
            ]
        },
        "ch06-voce-nao-e-um-bilhete-de-loteria": {
            "cards": [
                {"ic": "steps", "t": "O Preço de Não Decidir", "emph": "Não Decidir", "b": "A cultura atual odeia planejar o futuro, glorificando a eterna busca por 'manter as opções abertas'. <strong>Esse otimismo vago gera dezenas de caminhos mornos e nenhum resultado de elite.</strong> Quem inventa de verdade finca o pé num plano rígido.", "tip": "<strong>Sinal de alerta:</strong> colecionar caminhos paralelos na carreira é a confissão crua de que você teme definir o destino.", "warn": True},
                {"ic": "key", "t": "Matar o Acaso", "emph": "Acaso", "b": "Justificar o sucesso usando a palavra 'sorte' é o escudo preferido dos invejosos. <strong>Fundadores gigantes encaram a sorte como um parasita e desenham o triunfo com a frieza de um engenheiro civil erguendo pontes.</strong> Assuma o manche da sua vida.", "tip": "<strong>Modelo mental:</strong> trate a sorte como vento aleatório que você corta, e nunca como o motor principal do barco."}
            ]
        },
        "ch07-siga-o-dinheiro": {
            "cards": [
                {"ic": "spark", "t": "A Brutalidade do Gráfico", "emph": "Gráfico", "b": "A economia da tecnologia cospe na curva média e abraça a disparidade monstruosa sem pudor ético. <strong>Uma única tacada colossal vai gerar muito mais lucro do que todos os seus tropeços miúdos somados.</strong> Pulverizar esforços no que é mediano o tira do jogo grande.", "tip": "<strong>Regra:</strong> pare de gastar energia equilibrando bolas moribundas; foque na ideia que pode engolir o setor inteiro."},
                {"ic": "target", "t": "O Filtro do Capital", "emph": "Filtro", "b": "Manter negócios confortáveis só atrai empates contábeis deprimentes. <strong>Se a sua ideia não possui musculatura para devolver sozinha o fundo inteiro de investimento, ela é um peso morto amarrado na perna.</strong> Expulsar o limite linear é pré-requisito básico.", "tip": "<strong>Como aplicar:</strong> duas escolhas extremas e corajosas batem quinhentas concessões feitas pela metade."}
            ]
        },
        "ch08-segredos": {
            "cards": [
                {"ic": "key", "t": "O Tesouro Escondido", "emph": "Escondido", "b": "Chavões já estão precificados pelo mercado, e mistérios insondáveis travam iniciativas. <strong>A riqueza absurda descansa nos segredos ignorados: verdades que requerem curiosidade afiada para virem à luz.</strong> Desistir de procurar o novo é declarar derrota precoce.", "tip": "<strong>Modelo mental:</strong> revire os conceitos que a sociedade jogou no lixo por teimosia ou por arrogância intelectual."},
                {"ic": "lens", "t": "Escavar na Sombra", "emph": "Sombra", "b": "Os buracos negros das oportunidades douradas moram em ideias varridas para debaixo do tapete. <strong>Fundar o amanhã exige que você vista a máscara do herege e faça perguntas que a opinião pública acha inúteis.</strong> Onde os críticos riem, a fortuna esconde a porta.", "tip": "<strong>Prática:</strong> encontre um coro de especialistas gritando 'impossível' e cave fundo justamente debaixo dos pés deles."}
            ]
        },
        "ch09-fundacoes": {
            "cards": [
                {"ic": "layers", "t": "O Cimento do Dia Zero", "emph": "Dia Zero", "b": "Arranjos societários turvos carregam a semente do fim antes da primeira venda. <strong>Sinergia fingida e contratos gentis se transformam num câncer irreversível quando o caixa da startup incha e atrai holofotes.</strong> Seja frio e impiedoso ao definir papéis.", "tip": "<strong>Sinal de alerta:</strong> o abraço entusiasmado na garagem costuma virar briga no tribunal no primeiro milhão faturado.", "warn": True},
                {"ic": "scale", "t": "O Triângulo de Atrito", "emph": "Atrito", "b": "O investidor, o operador e o conselho enxergam galáxias distintas dentro do mesmo projeto. <strong>Quando o lucro imediato cruza espadas com a visão técnica, o negócio sangra energia internamente.</strong> O alinhamento perfeito amordaça o conflito destrutivo.", "tip": "<strong>Regra:</strong> corte os cargos inflados; salas cheias multiplicam a inércia e o pânico corporativo."},
                {"ic": "person", "t": "Sacrifício Alinhado", "emph": "Sacrifício", "b": "Consultores chiques secam o orçamento sem tomar banho de suor. <strong>Salários esmagados recompensados com fatias gordas da empresa filtram os fracos e convertem recrutas em mercenários leais.</strong> Se o líder foge do risco de falir, os soldados debandam rápido.", "tip": "<strong>Modelo mental:</strong> quem não sente no peito o risco da falência provável jamais construirá a solução genial."}
            ]
        },
        "ch10-a-mecanica-da-mafia": {
            "cards": [
                {"ic": "constellation", "t": "A Seita Lucrativa", "emph": "Seita", "b": "Refrigerante grátis e paredes coloridas são adereços que não criam união real. <strong>A startup letal age como um culto focado: fileiras de obcecados alinhados de forma perturbadora para derrubar um problema impossível.</strong> O recrutamento exige apóstolos, não burocratas.", "tip": "<strong>Pergunta-chave:</strong> o que prende as pessoas no seu barco além do salário caindo na conta?"},
                {"ic": "fork", "t": "Poder Sem Choque", "emph": "Choque", "b": "Deixar duas mentes brilhantes dividirem o comando da mesma área é riscar um fósforo na gasolina. <strong>Atribua uma responsabilidade absoluta e inegociável a cada talento e exija que ele foque naquela métrica exata.</strong> Clareza de limites elimina a guerra de egos.", "tip": "<strong>Prática:</strong> sobreposição de tarefas em times geniais gera menos inovação e mais conflitos de vaidade."}
            ]
        },
        "ch11-se-voce-construir-eles-virao": {
            "cards": [
                {"ic": "link", "t": "A Ilusão do Bom Código", "emph": "Ilusão", "b": "A lenda jura que produtos divinos se vendem sozinhos. <strong>Ignorar a malha de distribuição é assinar a sentença de morte silenciosa do invento perfeito, que apodrece numa gaveta por preguiça comercial.</strong> Planejar a venda é tão importante quanto o código.", "tip": "<strong>Regra:</strong> a arte da venda matadora é tão silenciosa e eficaz que o cliente acha que a ideia original foi dele."},
                {"ic": "scale", "t": "A Balança Impiedosa", "emph": "Balança", "b": "O lucro só cresce se o custo de atrair um cliente for ínfimo comparado ao retorno que ele gera. <strong>Quando o valor pago não cobre as despesas de marketing, o negócio se torna uma máquina de queimar dinheiro.</strong> Alinhe a tática ao peso do seu produto.", "tip": "<strong>Modelo mental:</strong> identifique e martele sem piedade o único canal de venda que tritura a concorrência a custo baixo."},
                {"ic": "gap", "t": "A Zona Morta do Caixa", "emph": "Zona Morta", "b": "Cobrar o equivalente a um salário razoável joga você num deserto sádico: caro demais para vendas online massivas, e barato demais para bancar times de vendas presenciais. <strong>Estacionar nessa faixa intermediária sufoca a empresa.</strong> Escale logo ou cave mais fundo.", "tip": "<strong>Sinal de alerta:</strong> o ticket indeciso é o parasita invisível que janta o oxigênio mensal da sua conta bancária.", "warn": True}
            ]
        },
        "ch12-o-homem-e-a-maquina": {
            "cards": [
                {"ic": "person", "t": "Aliados, Não Rivais", "emph": "Aliados", "b": "O pavor coletivo teme que as máquinas roubem empregos, mas o algoritmo apenas despeja força bruta em tarefas repetitivas. <strong>A mente humana sente, fareja a fraude velada e ajusta a mira com instinto que nenhum código possui.</strong> Não dispute, acople-se.", "tip": "<strong>Modelo mental:</strong> quem chutar a inteligência artificial para escanteio perderá feio para quem a usar como exoesqueleto."},
                {"ic": "link", "t": "O Centauro Imbatível", "emph": "Centauro", "b": "Juntar o raciocínio sagaz de um humano com o processamento algorítmico gera uma aliança imbatível. <strong>Deixe o silício devorar montanhas de planilhas e traga para si a caneta que dá a palavra final na zona cinzenta dos negócios.</strong> A simbiose é o futuro real.", "tip": "<strong>Prática:</strong> enxergue o seu computador não como concorrente, mas como um míssil teleguiado à sua disposição."}
            ]
        },
        "ch13-vendo-verde": {
            "cards": [
                {"ic": "target", "t": "O Raio-X Brutal", "emph": "Raio-X", "b": "O sucesso exige responder a sete cravos de sobrevivência: engenharia anômala, timing perfeito, monopólio, time brilhante, venda secreta, durabilidade e segredo revelado. <strong>Ignorar essas frentes e confiar na sorte é cavar a cova com otimismo irresponsável.</strong>", "tip": "<strong>Regra:</strong> não lance foguetes remendados com fita adesiva; a gravidade não perdoa motores fracos no salto."},
                {"ic": "leaf", "t": "O Canto da Sereia", "emph": "Canto da Sereia", "b": "Empresas fundadas apenas em bondade moral, sem lastro de engenharia pesada, fracassam miseravelmente. <strong>Injetar milhões baseando-se em chavões ecológicos sem resolver problemas reais do mercado é assinar recibo de estupidez caridosa.</strong> Boa vontade não ergue impérios.", "tip": "<strong>Sinal de alerta:</strong> causas nobres frequentemente vestem cadáveres industriais para atrair acionistas crédulos.", "warn": True}
            ]
        },
        "ch14-o-paradoxo-do-fundador": {
            "cards": [
                {"ic": "person", "t": "O Fundador Aberrante", "emph": "Aberrante", "b": "Os inovadores que desenham eras inteiras costumam ser figuras exóticas de personalidades intensas. <strong>A corporação tradicional escanteia mentes anômalas para garantir a paz burocrática, asfixiando justamente a mutação genética que traria a mina de ouro.</strong>", "tip": "<strong>Modelo mental:</strong> lixar as arestas cortantes do gênio da equipe só para evitar atritos mata a explosão estelar prometida."},
                {"ic": "spark", "t": "Proteja a Anomalia", "emph": "Anomalia", "b": "O progresso salta degraus nas costas de poucos desajustados teimosos que recusam engolir o consenso da maioria. <strong>Cultive as excentricidades no seu time, pois são os atrevidos que enxergam as alavancas capazes de reescrever as regras do jogo.</strong>", "tip": "<strong>Prática:</strong> uma sociedade doente cassa seus inovadores; a vanguarda constrói plataformas para eles operarem sem amarras."}
            ]
        }
    }
