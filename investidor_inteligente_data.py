# -*- coding: utf-8 -*-
"""Conteúdo (pt-BR) de 'O Investidor Inteligente' (Benjamin Graham)."""

BOOK = {
 "title": "O Investidor Inteligente",
 "author": "Benjamin Graham",
 "header_light": "O INVESTIDOR",
 "header_bold": "INTELIGENTE",
 "subtitle": "VISÃO GERAL · A BÍBLIA DO VALUE INVESTING",
 "intro": "O 'investidor inteligente' não é o mais esperto — é o mais paciente e disciplinado. Graham mostra que o maior inimigo do investidor é ele mesmo, e que duas palavras resumem tudo: margem de segurança. A alegoria do Sr. Mercado, a distinção preço × valor e as regras para o defensivo e o empreendedor compõem o manual definitivo.",
 "description": "A bíblia do value investing de Benjamin Graham. Investidor vs. especulador, a alegoria do Sr. Mercado, a margem de segurança, o investidor defensivo (50/50 e dollar-cost averaging), o empreendedor e as net-nets, preço vs. valor, inflação, temperamento e os critérios quantitativos de seleção de ações.",
 "tags": ["Value Investing", "Finanças", "Bolsa de Valores"],
 "progress": "10 Capítulos",
 "cover": "assets/investidor-inteligente-cover.png",
 "overview_cards": [
   {"ic":"scale","t":"Margem de Segurança","b":"O conceito central de todo o livro. Compre sempre com <strong>desconto substancial sobre o valor intrínseco</strong>, deixando folga para você estar errado. Analogia clássica: construa a ponte para 30 toneladas e dirija o caminhão de 10.","tip":"<strong>Como aplicar:</strong> pense primeiro em não perder; o ganho vem como consequência da disciplina."},
   {"ic":"person","t":"O Sr. Mercado","b":"O mercado é um <strong>sócio maníaco-depressivo</strong> que bate à sua porta todo dia oferecendo um preço. Você nunca é obrigado a aceitar. Ele está lá para <strong>servir, não para guiar</strong> — use a volatilidade como oportunidade, não como sinal de alarme.","tip":"<strong>Regra:</strong> compre no pânico do Sr. Mercado; ignore ou venda na euforia.","wide":True},
   {"ic":"fork","t":"Defensivo × Empreendedor","b":"Dois perfis coerentes: o <strong>defensivo</strong> busca tranquilidade com carteira 50/50 a 75/25 e regras mecânicas; o <strong>empreendedor</strong> dedica tempo para caçar pechinchas e net-nets. O erro é o meio-termo sem disciplina.","tip":"<strong>Modelo mental:</strong> se não tiver tempo e método para ser ativo, seja definitivamente passivo."},
 ],
}

CHAPTERS = [
 {"slug":"ch01-investidor-vs-especulador","sub":"CAPÍTULO 1: Investimento vs. Especulação",
  "intro":"Graham define investimento como uma operação que, após análise séria, promete segurança do principal e retorno adequado. Tudo que não atende a esses três pilares é especulação. Saber em qual jogo você está é a primeira decisão inteligente.",
  "cards":[
   {"ic":"scale","t":"A Definição Tríplice","b":"<strong>Investimento</strong> = análise minuciosa + segurança do principal + retorno adequado. Faltando qualquer um dos três pilares, é <strong>especulação</strong> — consciente ou não.","tip":"<strong>Como aplicar:</strong> antes de qualquer aplicação, classifique-a pelos três pilares — se faltar um, admita que está especulando."},
   {"ic":"fork","t":"Defensivo × Empreendedor","b":"Dois perfis, duas estratégias coerentes. O <strong>defensivo</strong> busca tranquilidade e ausência de erros graves; o <strong>empreendedor</strong> dedica tempo e método para superar a média. O erro é o meio-termo sem disciplina.","tip":"<strong>Regra:</strong> escolha um perfil e seja coerente — o amador que tenta ser ativo sem método destrói valor."},
   {"ic":"gap","t":"Especulação Inteligente vs. Burra","b":"Especular pode ser legítimo — desde que <strong>consciente, isolado e dimensionado</strong>. A conta separada de especulação preserva o capital de investimento. O erro fatal é especular acreditando estar investindo.","tip":"<strong>Sinal de alerta:</strong> misturar o capital de longo prazo com apostas de curto prazo na mesma conta.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 1",
  "lessons":["Defina seu jogo: investidor ou especulador — e seja coerente com ele.","Investir exige os três pilares; sem eles, admita que está especulando.","Se for especular, isole o capital e limite o tamanho."]},

 {"slug":"ch02-inflacao","sub":"CAPÍTULO 2: O Investidor e a Inflação",
  "intro":"O inimigo silencioso do investidor não é a queda do mercado, mas a inflação, que corrói o poder de compra do dinheiro parado. O retorno 'adequado' precisa ser medido em termos reais.",
  "cards":[
   {"ic":"wave","t":"Retorno Real vs. Nominal","b":"O que importa é o ganho <strong>acima da inflação</strong>, não o número de cotação. Ganhar 6% com inflação de 8% é perder 2% de poder de compra ao ano — uma perda real, mesmo que o saldo suba nominalmente.","tip":"<strong>Como aplicar:</strong> ao avaliar qualquer rendimento, sempre subtraia a inflação esperada."},
   {"ic":"triangle","t":"Ações como Hedge Imperfeito","b":"Empresas reajustam preços e lucros, oferecendo proteção <strong>parcial</strong> contra inflação — útil, mas não garantida em todo cenário. Títulos sofrem com inflação alta; ações sofrem em deflação/recessão.","tip":"<strong>Modelo mental:</strong> trate a inflação como um cenário a defender, não a prever — prepare a carteira para conviver com ela."},
   {"ic":"layers","t":"Diversificação Defensiva","b":"Ter ações <strong>e</strong> renda fixa defende contra cenários opostos — nenhuma alocação única ganha em todos os ambientes. Mesmo o defensivo precisa de parcela permanente em ações.","tip":"<strong>Cuidado:</strong> manter todo o patrimônio em caixa/renda fixa em ambiente inflacionário é uma perda lenta garantida.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 2",
  "lessons":["Meça todo retorno em termos reais, descontando a inflação.","Ações oferecem proteção parcial — útil, mas não garantida.","Equilibrar ações e renda fixa defende contra cenários opostos."]},

 {"slug":"ch03-historico-do-mercado","sub":"CAPÍTULO 3: Um Século de História do Mercado",
  "intro":"A história mostra que o mercado alterna euforia e pânico em ciclos, e que preços altos embutem retornos futuros baixos. Estudar o passado serve para calibrar expectativas, não para prever o próximo movimento.",
  "cards":[
   {"ic":"clock","t":"O Preço Pago Define o Retorno","b":"Quanto mais caro o mercado hoje, menor o retorno esperado e maior o risco. Os múltiplos (preço/lucro ajustado) são a bússola de expectativa — não uma bola de cristal, mas o dado mais confiável disponível.","tip":"<strong>Como aplicar:</strong> quando o mercado estiver em múltiplos históricos altos, reduza expectativas e reforce cautela."},
   {"ic":"spiral","t":"Reversão à Média","b":"Extremos de valuation tendem a se corrigir. O que sobe demais costuma voltar; o que cai demais também. A euforia 'desta vez é diferente' marcou quase todos os topos históricos.","tip":"<strong>Modelo mental:</strong> use a história como bússola de expectativa, não como bola de cristal — ela ensina padrões, não datas."},
   {"ic":"wave","t":"Ajuste a Alocação ao Ciclo","b":"Variar entre ~50% e ~75% em ações conforme o mercado esteja caro ou barato — mas sempre <strong>dentro de limites disciplinados</strong>. Comprar mais justamente quando está mais caro (FOMO) é o erro mais comum.","tip":"<strong>Sinal de alerta:</strong> quando todos estão eufóricos, mais cautela — não mais coragem.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 3",
  "lessons":["O preço pago hoje determina, em grande parte, o retorno de amanhã.","Extremos de valuation revertem; humildade vence a euforia.","Ajuste a alocação ao ciclo, mas sempre dentro de limites disciplinados."]},

 {"slug":"ch04-investidor-defensivo","sub":"CAPÍTULO 4: A Carteira do Investidor Defensivo",
  "intro":"O investidor defensivo busca tranquilidade e ausência de erros graves, não desempenho máximo. A solução é uma carteira simples, equilibrada, com regras mecânicas que removem a emoção da decisão.",
  "cards":[
   {"ic":"scale","t":"A Faixa 50/50 a 75/25","b":"Nunca menos de 25% nem mais de 75% em ações; o ponto neutro é <strong>50/50</strong>. Quando o mercado empurrar a proporção para fora da faixa, rebalanceie — essa mecânica <strong>vende caro e compra barato</strong> no automático.","tip":"<strong>Como aplicar:</strong> regras > previsões — o defensivo terceiriza a decisão para um sistema, não para o palpite."},
   {"ic":"clock","t":"Dollar-Cost Averaging","b":"Investir um valor fixo em intervalos fixos (aportes regulares) compra mais cotas quando barato e menos quando caro — neutraliza o timing e <strong>disciplina sem força de vontade</strong>. Abandone os aportes justamente nas quedas e perde o que é mais valioso.","tip":"<strong>Regra:</strong> defina valor e periodicidade e cumpra-os independente do humor do mercado."},
   {"ic":"key","t":"Blue Chips e Simplicidade","b":"Empresas grandes, conservadoramente financiadas, com longo histórico de lucros e dividendos. <strong>Simplicidade como estratégia</strong>: menos decisões discricionárias = menos erros emocionais.","tip":"<strong>Modelo mental:</strong> concentrar em poucas ou em modismos sem histórico é o oposto do que o defensivo deve fazer."},
  ],
  "lessons_title":"Lições-Chave do Capítulo 4",
  "lessons":["Mantenha de 25% a 75% em ações, com 50/50 como neutro, e rebalanceie.","Use aportes regulares (dollar-cost averaging) para vencer o timing.","Escolha blue chips e prefira simplicidade a complexidade."]},

 {"slug":"ch05-investidor-empreendedor","sub":"CAPÍTULO 5: A Carteira do Investidor Empreendedor",
  "intro":"O investidor empreendedor está disposto a dedicar tempo e esforço para superar a média. Graham adverte: só vale a pena com disciplina real — esforço sem método destrói valor, e pode ser pior que a estratégia passiva.",
  "cards":[
   {"ic":"lens","t":"Caça às Pechinchas","b":"Comprar ativos cotados <strong>bem abaixo do valor intrínseco/contábil</strong> — empresas sólidas em desgraça temporária ou negligenciadas pelo mercado. O coração da estratégia ativa é comprar o dólar por cinquenta centavos.","tip":"<strong>Como aplicar:</strong> quando você pode analisar a fundo e o mercado precifica mal por pessimismo ou desatenção."},
   {"ic":"gap","t":"Net-Nets (NCAV)","b":"Ações negociadas abaixo do <strong>ativo circulante líquido</strong> (capital de giro menos todo o passivo) oferecem margem extrema — você recebe o negócio 'de graça'. Exigem <strong>cesta diversificada</strong>: são frágeis individualmente.","tip":"<strong>Cuidado:</strong> concentrar numa única net-net é o erro — são situações de risco; só funcionam em cesta.","warn":True},
   {"ic":"target","t":"Esforço com Método","b":"Ser 'ativo' no sentido de girar a carteira, pagar corretagem e seguir manchetes <strong>não é</strong> investimento empreendedor. Atividade sem disciplina destrói valor; sem método, o empreendedor é pior que o defensivo.","tip":"<strong>Regra:</strong> só seja ativo se tiver disciplina e método comprovados; senão, seja definitivamente defensivo."},
  ],
  "lessons_title":"Lições-Chave do Capítulo 5",
  "lessons":["Só seja ativo se tiver disciplina e método; senão, seja defensivo.","Busque pechinchas e net-nets, com ampla diversificação.","Esforço sem critério é pior que a estratégia passiva."]},

 {"slug":"ch06-preco-vs-valor","sub":"CAPÍTULO 6: Preço vs. Valor",
  "intro":"A distinção fundadora do value investing: preço é o que você paga; valor é o que você recebe. O mercado cota preços o tempo todo, mas o valor intrínseco de um negócio muda muito mais devagar. Investir bem é explorar a diferença entre os dois.",
  "cards":[
   {"ic":"scale","t":"Preço ≠ Valor","b":"<strong>Preço</strong> = cotação de mercado, volátil e emocional. <strong>Valor</strong> = estimativa fundamentada do que o negócio vale. Nunca os confunda — o erro de confundir preço subindo com valor aumentando é o mais caro do investidor.","tip":"<strong>Como aplicar:</strong> se preço << valor, compre; se preço >> valor, evite ou venda; no meio, abstenha-se."},
   {"ic":"wave","t":"Votação × Balança","b":"No <strong>curto prazo</strong> o mercado é uma máquina de votação (popularidade, emoção); no <strong>longo prazo</strong>, é uma balança (pesa o valor real). Tenha paciência para a balança agir.","tip":"<strong>Modelo mental:</strong> o esquecido com desconto é preferível ao querido sobreprecificado."},
   {"ic":"lens","t":"Faixas, não Precisão","b":"Estime valor por <strong>faixas amplas</strong>, não por números exatos ilusórios. Graham desconfia do qualitativo excessivo — números (lucros, dívida, ativos) ancoram; qualidade refina.","tip":"<strong>Cuidado:</strong> comprar pelo 'momentum' da popularidade (votação), não pelo fundamento (peso), é especulação.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 6",
  "lessons":["Preço e valor são coisas distintas; lucre com a divergência.","No curto prazo prevalece a emoção; no longo, o fundamento.","Estime valor por faixas amplas, não por números exatos ilusórios."]},

 {"slug":"ch07-sr-mercado","sub":"CAPÍTULO 7: A Alegoria do Sr. Mercado",
  "intro":"Graham personifica o mercado como o Sr. Mercado: um sócio maníaco-depressivo que aparece todo dia oferecendo um preço. Você nunca é obrigado a aceitar. A genialidade é usá-lo, não obedecê-lo.",
  "cards":[
   {"ic":"person","t":"Servo, Não Guia","b":"O Sr. Mercado está a seu serviço com cotações diárias — explore suas extravagâncias, não as siga. Aja quando o preço for <strong>absurdamente baixo</strong> (compre) ou alto (venda/ignore); nos demais dias, ignore-o.","tip":"<strong>Regra:</strong> quando ele entra em pânico, faça compras; quando eufórico, fique cético."},
   {"ic":"spark","t":"Volatilidade = Oportunidade","b":"A oscilação só prejudica quem deixa o Sr. Mercado <strong>ditar</strong> suas decisões. Para o disciplinado, ela cria pechinchas — compra-se mais caro no topo e mais barato no fundo sem nenhuma análise extra.","tip":"<strong>Modelo mental:</strong> sua riqueza real depende do negócio, não da cotação de hoje."},
   {"ic":"mask","t":"Imunidade Emocional","b":"Tratar a cotação diária como medida de quanto você é rico ou sábio é deixar o humor do Sr. Mercado contaminar sua avaliação. <strong>Vender no pânico e comprar na euforia</strong> é o ciclo que destrói patrimônio.","tip":"<strong>Sinal de alerta:</strong> sentir urgência de 'fazer algo' com a carteira toda vez que o mercado oscila.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 7",
  "lessons":["O Sr. Mercado oferece preços, não verdades — você escolhe quando agir.","Use a volatilidade a seu favor: compre no pânico, ignore a euforia.","Sua riqueza real depende do negócio, não da cotação de hoje."]},

 {"slug":"ch08-margem-de-seguranca","sub":"CAPÍTULO 8: A Margem de Segurança",
  "intro":"Se Graham tivesse que resumir o investimento inteligente a duas palavras, seriam MARGEM DE SEGURANÇA: comprar com desconto suficiente sobre o valor intrínseco para que erros de estimativa ou imprevistos não levem à perda permanente.",
  "cards":[
   {"ic":"scale","t":"O Conceito Central","b":"A margem de segurança é a diferença entre o valor intrínseco estimado e o preço pago. Quanto maior o desconto, maior a proteção. Só compre quando o preço estiver <strong>bem abaixo do valor</strong>, deixando folga para você estar errado.","tip":"<strong>Como aplicar:</strong> se você estima o valor em R$ 100/ação, não compre a R$ 95 — espere R$ 60 ou R$ 70."},
   {"ic":"key","t":"Proteção contra o Erro","b":"A margem existe <strong>porque</strong> o futuro é incerto e suas estimativas são imperfeitas. Protege contra <strong>perda permanente</strong> — não evita a volatilidade. Construa a ponte para 30 toneladas e dirija o caminhão de 10.","tip":"<strong>Modelo mental:</strong> pense primeiro em não perder; o ganho vem como consequência da disciplina."},
   {"ic":"layers","t":"Margem + Diversificação","b":"Mesmo com margem, espalhe o risco. Algumas teses falharão — a margem + diversificação garantem o resultado do conjunto. Concentrar tudo numa tese, mesmo com margem ampla, é dispensar o seguro contra o imprevisto.","tip":"<strong>Cuidado:</strong> confiar tanto na própria análise a ponto de dispensar a margem ou a diversificação.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 8",
  "lessons":["Nunca compre sem margem de segurança — é o filtro central de Graham.","A margem protege contra seus próprios erros, não contra a volatilidade.","Combine margem com diversificação: ambas absorvem o imprevisível."]},

 {"slug":"ch09-temperamento-e-disciplina","sub":"CAPÍTULO 9: Temperamento e Disciplina",
  "intro":"Para Graham, o sucesso no investimento depende muito mais do temperamento do que do intelecto. O maior inimigo do investidor é ele mesmo — e proteger-se das próprias reações emocionais vale mais que qualquer análise sofisticada.",
  "cards":[
   {"ic":"mountain","t":"Caráter > QI","b":"O principal inimigo do investidor é <strong>ele mesmo</strong>. Dois investidores com o mesmo conhecimento e a mesma carteira: na queda, um vende em pânico e cristaliza a perda; o outro compra mais e segue o plano. A diferença não foi inteligência — foi <strong>temperamento</strong>.","tip":"<strong>Como aplicar:</strong> tenha regras escritas e siga-as — a disciplina substitui a força de vontade no momento da pressão."},
   {"ic":"clock","t":"Não Prever, Proteger","b":"A meta não é antecipar movimentos do mercado — é garantir que você não tome decisões autodestrutivas. <strong>Proteja-se da sua própria burrice</strong>: desenhe o sistema para o seu pior momento emocional.","tip":"<strong>Modelo mental:</strong> sentir necessidade de 'fazer algo' sempre, em vez de esperar a oportunidade, é o sintoma do problema."},
   {"ic":"key","t":"Paciência como Vantagem","b":"O investidor pode esperar indefinidamente pela pechincha certa, sem pressão de 'fazer algo'. Abandonar as regras justamente quando elas mais protegem (no pânico ou na euforia) desfaz anos de disciplina.","tip":"<strong>Regra:</strong> regras escritas e paciência são as armas centrais — o investidor inteligente é paciente, não genial."},
  ],
  "lessons_title":"Lições-Chave do Capítulo 9",
  "lessons":["Temperamento vence QI: o inimigo é o próprio comportamento.","Não tente prever o mercado; proteja-se das suas reações emocionais.","Regras escritas e paciência são as armas centrais do investidor inteligente."]},

 {"slug":"ch10-analise-de-empresas","sub":"CAPÍTULO 10: Análise e Seleção de Ações",
  "intro":"Para estimar o valor intrínseco e encontrar a margem de segurança, Graham propõe critérios quantitativos, conservadores e verificáveis. A análise busca solidez e desconto, não a empresa mais empolgante.",
  "cards":[
   {"ic":"lens","t":"Filtro Qualidade + Preço","b":"Critérios do defensivo: tamanho adequado, posição financeira forte (ativo circulante folgado, baixa dívida), histórico de lucros <strong>estável</strong>, dividendos contínuos, crescimento moderado e <strong>múltiplos baixos</strong>. Solidez verificável bate narrativa empolgante.","tip":"<strong>Como aplicar:</strong> compre solidez com desconto — fundamentos verificáveis sempre."},
   {"ic":"scale","t":"P/L e P/VPA com Tetos","b":"Pagar pouco em relação aos lucros (P/L baixo) <strong>e</strong> ao patrimônio (P/VPA baixo) limita o sobrepreço. Graham combina os dois — uma empresa pode ter P/L razoável mas P/VPA elevado, o que sinaliza risco.","tip":"<strong>Modelo mental:</strong> os números são o piso; a margem nasce de pagar pouco por eles."},
   {"ic":"key","t":"Solidez Financeira","b":"Lucros que cobrem juros com folga e ativos que cobrem passivos sustentam a 'segurança do principal'. <strong>Ignorar a dívida e a liquidez</strong> é o erro que leva à empresa frágil que quebra justamente quando você mais precisava que não quebrasse.","tip":"<strong>Sinal de alerta:</strong> confiar em lucros de um único ano em vez do histórico de longo prazo.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 10",
  "lessons":["Selecione por solidez financeira, histórico estável e múltiplos baixos.","Combine P/L e P/VPA moderados para limitar o sobrepreço.","Lucros que cobrem a dívida com folga sustentam a segurança do principal."]},
]
