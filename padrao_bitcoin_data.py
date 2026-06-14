# -*- coding: utf-8 -*-
"""Conteúdo (pt-BR) das páginas da biblioteca para 'O Padrão Bitcoin'
(Saifedean Ammous). Termos canônicos: vendabilidade, estoque/fluxo, moeda
forte/fraca, preferência temporal, moeda sonante, prova de trabalho.

Padrão de densidade (jun/2026): >=6 cards densos e fiéis por capítulo —
'insight real + composição elegante'. Fonte: skill ammous-padrao-bitcoin."""

BOOK = {
 "title": "O Padrão Bitcoin",
 "author": "Saifedean Ammous",
 "header_light": "O PADRÃO",
 "header_bold": "BITCOIN",
 "subtitle": "VISÃO GERAL · DINHEIRO FORTE E A HISTÓRIA DO DINHEIRO",
 "intro": "Para entender o Bitcoin, é preciso primeiro entender o dinheiro. Ammous percorre toda a história monetária — do escambo às conchas, do ouro ao fiat — para extrair a lei que governa todo dinheiro: vence o que é mais difícil de produzir. A régua é a razão estoque/fluxo, e a tese é que o Bitcoin, com oferta absolutamente fixa, é o dinheiro mais forte já inventado.",
 "description": "Para entender o Bitcoin, entenda o dinheiro. Ammous usa a história monetária e a escola austríaca para mostrar por que o dinheiro forte (alta razão estoque/fluxo) preserva poupança e civilização — e por que o Bitcoin seria o mais forte já criado.",
 "tags": ["Economia", "Dinheiro", "Bitcoin"],
 "progress": "10 Capítulos Completos",
 "cover": "assets/padrao-bitcoin-cover.png",
 "overview_cards": [
   {"ic":"scale","t":"A Régua: Estoque / Fluxo","b":"A força de uma moeda = razão entre o <strong>estoque</strong> (tudo já produzido) e o <strong>fluxo</strong> (a produção nova). Razão <strong>alta</strong> = moeda forte (mantém valor); razão <strong>baixa</strong> = moeda fraca (destrói a poupança).","tip":"<strong>Como aplicar:</strong> antes de poupar em algo, pergunte: se virar reserva popular, fica fácil produzir mais?","wide":True},
   {"ic":"target","t":"Vendabilidade","b":"O dinheiro emerge porque é o bem mais <strong>vendável</strong> — o que se revende com a menor perda de valor. Três faces: escala, espaço e tempo — e a vendabilidade <strong>no tempo</strong> é a decisiva.","tip":"<strong>Modelo mental:</strong> o melhor dinheiro é o que melhor atravessa o tempo sem perder valor."},
   {"ic":"clock","t":"A Armadilha da Moeda Fraca","b":"Tudo que vira reserva de valor atrai produção extra. Se essa produção é fácil, ela <strong>afunda o valor e expropria quem poupou</strong>. Por isso todo bom dinheiro é <strong>caro de produzir</strong>.","tip":"<strong>Modelo mental:</strong> ser caro de produzir é virtude monetária, não defeito.","warn":True},
   {"ic":"steps","t":"Dinheiro e Civilização","b":"Dinheiro que guarda valor permite <strong>baixa preferência temporal</strong>: poupar, investir e construir para o longo prazo. Dinheiro que apodrece empurra para o consumo imediato e a dívida.","tip":"<strong>Lição:</strong> a qualidade do dinheiro molda a poupança, a cultura e a civilização."},
   {"ic":"spiral","t":"Bitcoin = Escassez Absoluta","b":"Primeira moeda com oferta <strong>fixa (21 milhões)</strong>, garantida por prova de trabalho e descentralização. Os <strong>halvings</strong> cortam o fluxo pela metade a cada ~4 anos — a razão estoque/fluxo só sobe, superando o ouro.","tip":"<strong>Chave:</strong> pela 1ª vez, demanda crescente NÃO produz oferta crescente."},
   {"ic":"key","t":"O Caso de Uso","b":"Para Ammous, o Bitcoin é <strong>reserva de valor soberana</strong> e camada de liquidação final — 'ouro digital', não meio de pagamento de varejo.","tip":"<strong>Cuidado:</strong> tratá-lo como investimento que 'só sobe' ou como dinheiro de troco leva a erro.","warn":True},
 ],
}

CHAPTERS = [
 {"slug":"ch01-dinheiro-vendabilidade","sub":"CAPÍTULO 1: Dinheiro e Vendabilidade",
  "intro":"Dinheiro é o bem que a sociedade adota livremente como meio de troca para resolver o problema da coincidência de desejos. Ele emerge porque é o mais vendável.",
  "cards":[
   {"ic":"target","t":"Vendabilidade (Carl Menger)","b":"A facilidade de vender um bem com a <strong>menor perda de valor</strong>. Três faces: <strong>escala</strong> (divisível), <strong>espaço</strong> (transportável) e <strong>tempo</strong> (mantém valor) — esta é a decisiva.","tip":"<strong>Como aplicar:</strong> o melhor dinheiro é o mais vendável no tempo.","wide":True},
   {"ic":"fork","t":"O Problema do Escambo","b":"A troca direta falha por falta de coincidência: <strong>em escala</strong> (o sapato não compra a casa em pedaços), <strong>no tempo</strong> (o perecível não acumula até o durável) e <strong>no espaço</strong> (a casa não se transporta).","tip":"<strong>Saída:</strong> a troca indireta — adquirir um bem intermediário que todos aceitam (dinheiro)."},
   {"ic":"book","t":"As Duas Funções","b":"<strong>Meio de troca</strong> (a função-mãe: comprar não para consumir, mas para trocar depois) e <strong>reserva de valor</strong> (transportar poder de compra ao futuro).","tip":"<strong>Cuidado:</strong> dinheiro ≠ investimento — investimento dá ganho, tem risco e é menos líquido."},
   {"ic":"scale","t":"Unidade de Conta","b":"A terceira função <strong>emerge das duas primeiras</strong>: quando um bem vira meio de troca, todos os preços passam a ser medidos nele. Não há unidade de conta sem antes ser o bem mais vendável.","tip":"<strong>Modelo mental:</strong> o dinheiro é a régua dos preços — e só vira régua quem já é o mais líquido."},
   {"ic":"eye","t":"O Dinheiro Não é Inventado","b":"Menger mostrou que o dinheiro <strong>emerge espontaneamente do mercado</strong>: cada um aceita o bem mais fácil de revender, e a convergência elege um só. O Estado reconhece o dinheiro — não o cria.","tip":"<strong>Lição:</strong> bom dinheiro é descoberto por milhões de escolhas, não decretado."},
   {"ic":"wave","t":"O Prêmio de Liquidez","b":"O bem mais vendável ganha um <strong>valor extra</strong> só por ser aceito por todos — demanda monetária acima do uso prático. Foi assim que o ouro valeu muito mais que sua utilidade industrial.","tip":"<strong>Cuidado:</strong> esse prêmio evapora se a oferta do bem fica fácil de aumentar.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 1",
  "lessons":["Dinheiro resolve a coincidência de desejos via troca indireta.","Vendabilidade (escala, espaço, tempo) elege o dinheiro — e o tempo é decisivo.","As três funções (troca, reserva, conta) emergem nessa ordem.","O mercado, não o Estado, descobre o melhor dinheiro."]},

 {"slug":"ch02-estoque-fluxo","sub":"CAPÍTULO 2: Estoque, Fluxo e a Moeda Forte",
  "intro":"A força de uma moeda mede-se pela razão entre estoque e fluxo. É a régua que governa todo o livro.",
  "cards":[
   {"ic":"scale","t":"Estoque / Fluxo","b":"<strong>Estoque</strong> = tudo já produzido (menos o consumido). <strong>Fluxo</strong> = a produção nova de um período. Razão <strong>alta</strong> = nem um grande aumento de produção move o total = o valor resiste.","tip":"<strong>Regra:</strong> mede-se a força pela oferta FUTURA (o fluxo), não pela foto atual.","wide":True},
   {"ic":"clock","t":"A Armadilha da Moeda Fraca","b":"Tudo que vira reserva atrai produção; se a produção é fácil, ela <strong>expropria quem poupou</strong>. Corolário: todo dinheiro que dura é <strong>caro de produzir</strong>.","tip":"<strong>Sinal de alerta:</strong> oferta fácil de inflar = riqueza fácil de evaporar.","warn":True},
   {"ic":"target","t":"A Régua na Prática","b":"O ouro nunca teve a oferta crescendo mais que ~<strong>1,5% ao ano</strong> — por isso resiste como nenhum outro. A prata cresce mais rápido; bens de consumo têm a oferta acompanhando a demanda quase 1:1.","tip":"<strong>Modelo mental:</strong> estoque/fluxo alto = 'mesmo todo mundo cavando, mal move o total'."},
   {"ic":"steps","t":"Seleção Natural Monetária","b":"Numa competição entre reservas de valor, quem produz a moeda barato dilui todos os outros. Sobrevive a que <strong>ninguém consegue inflar</strong> — a de maior estoque/fluxo.","tip":"<strong>Como aplicar:</strong> antes de poupar em algo, pergunte 'quão fácil é fabricar mais disto?'."},
   {"ic":"key","t":"Moeda Sonante","b":"A moeda forte <strong>emerge pela escolha livre do mercado</strong> e seu valor é determinado pelo mercado, não pelo decreto. A competição sempre tende ao dinheiro mais forte.","tip":"<strong>Modelo mental:</strong> o fluxo é o inimigo do poupador."},
   {"ic":"wrench","t":"A Lei de Gresham","b":"Quando o Estado força as duas a valerem igual (curso legal), a <strong>moeda fraca expulsa a forte de circulação</strong>: gasta-se a ruim e entesoura-se a boa.","tip":"<strong>Cuidado:</strong> isso só acontece sob decreto — no mercado livre, a forte vence.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 2",
  "lessons":["Mede-se a força pela razão estoque/fluxo, não pela oferta atual.","A armadilha: o que é fácil de produzir destrói quem o usa como reserva.","O ouro reinou por ter o menor crescimento de oferta (~1,5%/ano).","No mercado livre a moeda forte vence; sob decreto, a fraca expulsa a forte (Gresham)."]},

 {"slug":"ch03-moedas-primitivas","sub":"CAPÍTULO 3: Moedas Primitivas",
  "intro":"Cada bem foi dinheiro enquanto era escasso — e colapsou quando a tecnologia tornou sua oferta fácil. A razão estoque/fluxo aplicada à história real.",
  "cards":[
   {"ic":"mountain","t":"Pedras de Yap e Conchas","b":"As pedras de Rai foram dinheiro por séculos porque eram dificílimas de obter — até alguém com ferramentas modernas produzi-las em massa. Conchas: dinheiro enquanto raras; a importação em massa destruiu seu valor.","tip":"<strong>Lição:</strong> a escassez de hoje não garante a de amanhã.","wide":True},
   {"ic":"wave","t":"A Regra da Oferta Súbita","b":"Um meio monetário sobrevive enquanto o fluxo é pequeno; quando um avanço dispara a oferta, o bem <strong>perde o status de dinheiro</strong>.","tip":"<strong>Modelo mental:</strong> a tecnologia é a juíza silenciosa do dinheiro."},
   {"ic":"eye","t":"Transferência de Riqueza","b":"Em toda moeda primitiva, quem conseguia <strong>produzir o bem barato</strong> trocava-o por bens reais de quem poupava nele — expropriando-os.","tip":"<strong>Cuidado:</strong> dinheiro fraco é um mecanismo silencioso de transferência de riqueza.","warn":True},
   {"ic":"link","t":"As Contas de Vidro da África","b":"Europeus produziam contas de vidro <strong>baratíssimas</strong> e as trocavam por ouro, marfim e pessoas escravizadas. Para os africanos eram raras (dinheiro forte); para os europeus, triviais — uma das maiores expropriações da história.","tip":"<strong>Lição:</strong> quem tem o dinheiro mais difícil drena a riqueza de quem tem o mais fácil."},
   {"ic":"sword","t":"Dinheiro Difícil Conquista o Fácil","b":"Repetidamente, sociedades com moeda mais forte <strong>subjugaram</strong> as de moeda mais fraca — economicamente e militarmente. A dureza monetária foi vantagem civilizacional.","tip":"<strong>Modelo mental:</strong> a escolha do dinheiro não é técnica — é questão de sobrevivência."},
   {"ic":"clock","t":"O Padrão se Repete","b":"Gado, sal, contas, conchas, metais: cada um reinou e caiu pela <strong>mesma causa única</strong> — a oferta deixou de ser difícil.","tip":"<strong>Como aplicar:</strong> ao avaliar qualquer 'novo dinheiro', olhe o que acontece com a oferta quando a demanda sobe."},
  ],
  "lessons_title":"Lições-Chave do Capítulo 3",
  "lessons":["Toda moeda primitiva caiu pela mesma causa: a oferta deixou de ser difícil.","A escassez é relativa à tecnologia — e a tecnologia muda.","Dinheiro fraco transfere riqueza para quem o produz (as contas de vidro).","Sociedades de dinheiro forte historicamente dominaram as de dinheiro fraco."]},

 {"slug":"ch04-metais-monetarios","sub":"CAPÍTULO 4: Os Metais Monetários",
  "intro":"O ouro venceu porque tinha a maior razão estoque/fluxo: é indestrutível (o estoque só cresce) e sua produção anual é mínima.",
  "cards":[
   {"ic":"target","t":"Por que o Ouro Venceu","b":"<strong>Indestrutibilidade</strong> → quase todo ouro já garimpado ainda existe (estoque cumulativo). <strong>Produção mínima</strong> → fluxo ínfimo frente ao estoque. Resultado: a maior razão estoque/fluxo = o melhor reserva de valor.","tip":"<strong>Lição:</strong> o ouro venceu por durar, não por brilhar.","wide":True},
   {"ic":"scale","t":"A Derrota da Prata","b":"A prata teve seu papel (mais divisível para o dia a dia), mas sua oferta cresce mais rápido e ela <strong>oxida e se consome</strong>. Quando foi desmonetizada, quem poupava nela empobreceu.","tip":"<strong>Modelo mental:</strong> entre dois metais, vence o de menor crescimento de oferta."},
   {"ic":"steps","t":"O Padrão-Ouro Clássico","b":"De ~1871 a 1914: com o ouro como âncora, os preços eram estáveis no longo prazo, a poupança valia e o capital se acumulava — a 'Belle Époque' de inovação, livre-comércio e baixa preferência temporal.","tip":"<strong>Como aplicar:</strong> dinheiro forte como base da prosperidade duradoura."},
   {"ic":"wrench","t":"A Âncora Disciplina o Estado","b":"Sob o ouro, déficits causavam <strong>saída de ouro</strong> e forçavam o ajuste automático. O governo não podia gastar além do que arrecadava sem sentir o freio.","tip":"<strong>Lição:</strong> o ouro impunha honestidade fiscal sem precisar de promessa política."},
   {"ic":"gap","t":"O Calcanhar de Aquiles","b":"O ouro é pesado e difícil de transportar/verificar — o que forçou a <strong>centralização em cofres de bancos</strong>. E foi essa centralização que abriu a porta para o Estado confiscá-lo.","tip":"<strong>Sinal de alerta:</strong> resolver a fraqueza do peso centralizando foi o pecado original.","warn":True},
   {"ic":"book","t":"Papel Lastreado: a Brecha","b":"As notas 'resgatáveis em ouro' eram convenientes — mas permitiram emitir <strong>mais papel do que havia metal</strong>. A conveniência preparou o terreno para romper a âncora.","tip":"<strong>Cuidado:</strong> toda camada de abstração sobre o dinheiro forte é uma chance de inflá-lo.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 4",
  "lessons":["O ouro venceu pela maior razão estoque/fluxo (indestrutível + produção mínima).","O padrão-ouro clássico (1871–1914) foi era de poupança sólida e progresso.","A âncora do ouro disciplinava governos automaticamente.","A fraqueza física (peso) forçou a centralização — a brecha do fiat."]},

 {"slug":"ch05-dinheiro-governamental","sub":"CAPÍTULO 5: O Dinheiro Governamental",
  "intro":"O fiat nasceu quando os Estados romperam a âncora do ouro para financiar guerras e gastos. Sem freio de escassez, a inflação virou confisco silencioso da poupança.",
  "cards":[
   {"ic":"wrench","t":"A Captura do Ouro","b":"Como o ouro estava em cofres centrais, bastou suspender a conversibilidade e <strong>emitir papel além das reservas</strong>. A Primeira Guerra é o marco: os países abandonaram o padrão-ouro para imprimir e financiar o conflito.","tip":"<strong>Modelo mental:</strong> quando a régua é elástica, a estabilidade vira promessa política.","wide":True},
   {"ic":"clock","t":"Inflação como Imposto Invisível","b":"Emitir moeda nova transfere poder de compra de quem poupa para <strong>quem recebe o dinheiro novo primeiro</strong> (o Estado e os próximos da fonte). É o <strong>Efeito Cantillon</strong> — tributação sem voto.","tip":"<strong>Cuidado:</strong> inflação é transferência, não geração de riqueza.","warn":True},
   {"ic":"gap","t":"1971: o Fim da Âncora","b":"Bretton Woods atou as moedas ao dólar e o dólar ao ouro. Em 1971, Nixon 'suspendeu temporariamente' a conversão — e a suspensão <strong>nunca acabou</strong>. Desde então, o mundo vive sob fiat puro.","tip":"<strong>Lição:</strong> 'temporário' em política monetária costuma significar permanente."},
   {"ic":"book","t":"Curso Legal","b":"Imposição estatal de que a moeda seja aceita — o <strong>oposto da moeda sonante</strong>, que o mercado escolhe. Ser obrigatório denuncia que o mercado não a escolheria.","tip":"<strong>Sinal de alerta:</strong> 'um pouco de inflação é saudável' = normalização do confisco gradual."},
   {"ic":"spiral","t":"O Fim do Jogo: Hiperinflação","b":"Sem limite físico, a tentação de imprimir não tem freio. Weimar, Zimbábue, Venezuela: quando a confiança quebra, a moeda <strong>colapsa por completo</strong> e a poupança de gerações evapora.","tip":"<strong>Cuidado:</strong> toda hiperinflação começou como 'só um pouco' de emissão.","warn":True},
   {"ic":"eye","t":"O Calote Silencioso","b":"Governos preferem inflar a dar calote honesto: a dívida é paga em moeda que <strong>vale cada vez menos</strong>. O credor recebe o número, não o valor.","tip":"<strong>Modelo mental:</strong> a inflação é um default que não precisa ser declarado."},
  ],
  "lessons_title":"Lições-Chave do Capítulo 5",
  "lessons":["O fiat nasceu para financiar gastos (sobretudo guerra) sem o freio do ouro.","1971 selou a era do fiat puro — a 'suspensão temporária' virou permanente.","Sem âncora, a oferta vira política e a inflação confisca a poupança.","Curso legal, Efeito Cantillon e hiperinflação mostram quem ganha e quem paga."]},

 {"slug":"ch06-preferencia-temporal","sub":"CAPÍTULO 6: Dinheiro e Preferência Temporal",
  "intro":"A qualidade do dinheiro molda como a sociedade valoriza o futuro. Dinheiro que guarda valor permite poupar e construir; dinheiro que apodrece empurra para o consumo imediato.",
  "cards":[
   {"ic":"clock","t":"Preferência Temporal","b":"Quanto se valoriza o presente sobre o futuro. <strong>Baixa</strong> = paciência, poupança, planejamento; <strong>alta</strong> = impaciência, consumo imediato, dívida. O dinheiro forte recompensa adiar; o fraco pune.","tip":"<strong>Como aplicar:</strong> o dinheiro é um sinal de paciência — molda a cultura, não só os preços.","wide":True},
   {"ic":"steps","t":"A Escada da Civilização","b":"Baixa preferência temporal → <strong>poupança</strong> → acúmulo de <strong>capital</strong> → mais produtividade → tempo livre para ciência, arte e família. O dinheiro forte estaria na base.","tip":"<strong>Modelo mental:</strong> civilizações de dinheiro forte fazem obras para durar séculos."},
   {"ic":"key","t":"Poupar é Plantar","b":"Guardar valor com segurança é o que permite <strong>investir no eu futuro</strong>: estudo, saúde, ferramentas, negócios. A poupança é a semente de todo capital.","tip":"<strong>Lição:</strong> sem reserva de valor confiável, ninguém tem motivo para adiar a gratificação."},
   {"ic":"mountain","t":"A Arte que Dura","b":"Ammous liga o dinheiro forte às catedrais, à Renascença e à arte feita <strong>para durar séculos</strong>. Sob fiat, a produção tende ao descartável e ao imediato.","tip":"<strong>Modelo mental:</strong> o horizonte de tempo de uma cultura aparece no que ela constrói."},
   {"ic":"eye","t":"A Cultura do Imediato","b":"Inflação reeduca a sociedade para <strong>gastar e se endividar</strong> — o consumo financiado por dívida é o futuro pagando o presente, não riqueza nova.","tip":"<strong>Cuidado:</strong> você compete com o seu eu futuro; dinheiro que apodrece o expropria.","warn":True},
   {"ic":"target","t":"O Juro Nasce da Poupança","b":"Quando muita gente poupa (baixa preferência temporal), os juros caem <strong>naturalmente</strong> e há capital barato para projetos longos. É o oposto de baixar o juro por decreto (cap. 7).","tip":"<strong>Lição:</strong> juro saudável é fruto de poupança real, não de impressora."},
  ],
  "lessons_title":"Lições-Chave do Capítulo 6",
  "lessons":["Boa reserva de valor → baixa preferência temporal → poupança e civilização.","Inflação reeduca a sociedade para a impaciência e a dívida.","Capital, arte e cultura duradoura acumulam-se sobre dinheiro forte.","Juro saudável nasce da poupança real, não do decreto."]},

 {"slug":"ch07-ciclos-economicos","sub":"CAPÍTULO 7: O Sistema de Informação do Capitalismo",
  "intro":"Os juros de livre mercado coordenam poupança e investimento. Quando o Estado infla a moeda e força juros baixos, corrompe esse sinal — e nasce o ciclo de bolha e estouro.",
  "cards":[
   {"ic":"target","t":"Juros como Sinal","b":"A taxa de juros comunica <strong>quanta poupança real existe</strong> para investir. Juro alto = poupe mais antes; juro baixo = há recursos para projetos longos. Baixá-lo por decreto é <strong>mentir ao mercado</strong>.","tip":"<strong>Modelo mental:</strong> juro é um preço — mexer nele à força cega a economia.","wide":True},
   {"ic":"spiral","t":"Boom → Bust","b":"Crédito fácil gera um <strong>boom</strong> de investimentos insustentáveis; quando se revela que a poupança real não existe, vem o <strong>bust</strong> — a correção que liquida os erros.","tip":"<strong>Lição:</strong> a recessão não é a doença; é a cura.","warn":True},
   {"ic":"book","t":"A Teoria Austríaca","b":"Mises e Hayek (Nobel de 1974) mostraram que o ciclo nasce da <strong>expansão artificial do crédito</strong>, não de um defeito do mercado. O dinheiro fácil é a causa, não o remédio.","tip":"<strong>Como aplicar:</strong> ao ouvir 'falha de mercado', pergunte quem manipulou o juro antes."},
   {"ic":"wrench","t":"Capital Mal Alocado","b":"Com juro falso, projetos que só parecem lucrativos a essa taxa atraem capital, trabalho e recursos. O bust <strong>revela o desperdício</strong> — fábricas, imóveis e empresas que não deviam existir.","tip":"<strong>Modelo mental:</strong> o estrago se faz no boom; o bust apenas o expõe."},
   {"ic":"eye","t":"Quem Paga o Boom","b":"O crédito novo não é poupança — é dinheiro criado. Ele transfere recursos para <strong>quem o recebe primeiro</strong> e deixa a conta (inflação e crise) para o resto.","tip":"<strong>Cuidado:</strong> crescimento por dívida barata é riqueza emprestada do futuro.","warn":True},
   {"ic":"clock","t":"O Erro do Estímulo","b":"Tratar a recessão como o inimigo a combater com <strong>mais estímulo</strong> apenas semeia o próximo ciclo, maior. A 'cura' vira a causa.","tip":"<strong>Cuidado:</strong> PIB inflado por dívida não é riqueza real."},
  ],
  "lessons_title":"Lições-Chave do Capítulo 7",
  "lessons":["Juros coordenam poupança e investimento; o Estado os distorce ao inflar.","Crédito barato gera boom de mau investimento; o bust é a correção.","A teoria austríaca (Mises/Hayek): o ciclo vem do dinheiro fácil, não do mercado.","Estímulo sobre estímulo só adia e amplia a crise seguinte."]},

 {"slug":"ch08-dinheiro-solido-liberdade","sub":"CAPÍTULO 8: Dinheiro Sólido e Liberdade",
  "intro":"Há relação direta entre a qualidade do dinheiro e o tamanho do Estado e da guerra. Dinheiro forte limita o poder; dinheiro fraco o solta.",
  "cards":[
   {"ic":"scale","t":"Dinheiro Forte = Freio ao Poder","b":"Sob o padrão-ouro, o Estado só gasta o que <strong>arrecada ou toma emprestado abertamente</strong> — e o povo sente o custo, o que gera resistência. O fiat remove esse freio: gasta-se e guerreia-se sem aprovação direta.","tip":"<strong>Modelo mental:</strong> quem controla a régua do valor, controla a sociedade.","wide":True},
   {"ic":"steps","t":"O Crescimento do Leviatã","b":"Foi sob o fiat que o Estado <strong>explodiu de tamanho</strong> no séc. XX. Sem o limite do ouro, programas e burocracias crescem financiados pela impressora, não pelo consentimento do contribuinte.","tip":"<strong>Lição:</strong> o tamanho do governo acompanha a elasticidade do dinheiro."},
   {"ic":"sword","t":"Guerra e Fiat","b":"A escala industrial das guerras do séc. XX só foi possível porque os Estados podiam <strong>imprimir</strong>. O ouro as teria abreviado — a diferença entre uma guerra de meses e uma de anos.","tip":"<strong>Cuidado:</strong> a guerra total é financiada pela inflação, não pelo imposto declarado.","warn":True},
   {"ic":"eye","t":"Inflação e Desigualdade","b":"O dinheiro novo chega primeiro a bancos e aos próximos do poder (Efeito Cantillon), que compram ativos <strong>antes dos preços subirem</strong>. O assalariado recebe por último — concentração de riqueza embutida.","tip":"<strong>Modelo mental:</strong> nem toda desigualdade é de mercado; parte é desenhada pela emissão.","warn":True},
   {"ic":"key","t":"Poupança é Liberdade Estocada","b":"Poder guardar valor com segurança permite <strong>dizer não, esperar, escolher</strong>. Quando a poupança apodrece, o indivíduo perde independência e fica mais dependente do Estado e do crédito.","tip":"<strong>Como aplicar:</strong> destruir a reserva de valor é destruir a soberania do indivíduo."},
   {"ic":"book","t":"O Mecenas e o Estado","b":"Sob dinheiro forte, ciência e arte eram bancadas por <strong>poupança e mecenato privado</strong>. Sob fiat, passam a depender de subsídio estatal — e da agenda de quem o concede.","tip":"<strong>Lição:</strong> quem financia a cultura molda a cultura."},
  ],
  "lessons_title":"Lições-Chave do Capítulo 8",
  "lessons":["Dinheiro forte limita o Estado; dinheiro fraco o solta para gastar e guerrear.","O fiat permitiu o crescimento do Estado e a guerra total do séc. XX.","A emissão concentra riqueza (Cantillon) — desigualdade desenhada.","Poupança segura é uma forma concreta de liberdade individual."]},

 {"slug":"ch09-bitcoin-dinheiro-digital","sub":"CAPÍTULO 9: O Dinheiro Digital (Bitcoin)",
  "intro":"O Bitcoin é a primeira moeda com escassez absolutamente fixa — no máximo 21 milhões — garantida por matemática, prova de trabalho e descentralização.",
  "cards":[
   {"ic":"spiral","t":"Escassez Absoluta (21 milhões)","b":"A oferta total é <strong>fixa por código</strong>; nenhum governo, banco ou maioria pode emitir mais. O oposto do fiat, cuja oferta é, por definição, ilimitada.","tip":"<strong>Chave:</strong> pela 1ª vez, a oferta é perfeitamente inelástica à demanda.","wide":True},
   {"ic":"layers","t":"Prova de Trabalho + Dificuldade Ajustável","b":"Mineradores gastam <strong>energia real</strong> para validar e emitir — o 'custo de produção' que protege a moeda. E a <strong>dificuldade se ajusta</strong>: se mais poder entra, a emissão segue o cronograma — a oferta NÃO acelera.","tip":"<strong>Modelo mental:</strong> a armadilha da moeda fraca foi tornada impossível por design."},
   {"ic":"clock","t":"O Cronograma dos Halvings","b":"A emissão cai pela metade a cada ~4 anos (210.000 blocos), até a última fração de moeda por volta de <strong>2140</strong>. O fluxo só encolhe — a razão estoque/fluxo só sobe, ultrapassando o ouro.","tip":"<strong>Lição:</strong> a política monetária do Bitcoin é conhecida até o último satoshi."},
   {"ic":"link","t":"Descentralização","b":"A rede é mantida por <strong>milhares de nós independentes</strong>; alterar a oferta exigiria consenso impossível. Não há ponto único para o Estado capturar — a falha do ouro centralizado, resolvida.","tip":"<strong>Lição:</strong> confiança substituída por verificação — você audita, não confia."},
   {"ic":"key","t":"Autocustódia = Soberania","b":"Quem detém as <strong>chaves privadas</strong> detém o dinheiro, sem depender de banco ou custodiante. É a posse direta que o ouro físico prometia, sem o peso nem o cofre.","tip":"<strong>Cuidado:</strong> 'not your keys, not your coins' — em corretora, você tem uma promessa, não o ativo."},
   {"ic":"eye","t":"Resistência à Censura","b":"Transações e saldos <strong>não podem ser bloqueados ou confiscados</strong> por decreto enquanto você controla as chaves. É dinheiro que não pede permissão.","tip":"<strong>Modelo mental:</strong> o que não pode ser apreendido não pode ser usado como alavanca contra você."},
  ],
  "lessons_title":"Lições-Chave do Capítulo 9",
  "lessons":["Oferta fixa (21 milhões) por prova de trabalho e descentralização.","A dificuldade ajustável torna a armadilha da moeda fraca impossível.","Os halvings fazem a razão estoque/fluxo só crescer — superando o ouro.","Autocustódia e resistência à censura devolvem a soberania ao indivíduo."]},

 {"slug":"ch10-para-que-serve-bitcoin","sub":"CAPÍTULO 10: Para Que Serve o Bitcoin",
  "intro":"O valor do Bitcoin, para Ammous, está em ser reserva de valor soberana e camada de liquidação final — não dinheiro de varejo para o dia a dia.",
  "cards":[
   {"ic":"target","t":"Reserva de Valor Soberana","b":"Um ativo que ninguém pode <strong>confiscar, inflar ou congelar</strong> — poupança fora do alcance de qualquer Estado ou banco. É o caso de uso primário do livro.","tip":"<strong>Como aplicar:</strong> pense em ouro digital — o concorrente é a reserva de valor, não o meio de pagamento.","wide":True},
   {"ic":"layers","t":"Camada de Liquidação","b":"Cada transação na base é cara e definitiva — como a liquidação entre bancos centrais. A <strong>escala vem de camadas superiores</strong> (rápidas, baratas), não de inchar a base.","tip":"<strong>Modelo mental:</strong> a base resolve confiança; as camadas resolvem velocidade."},
   {"ic":"key","t":"Poupança de Longo Prazo","b":"O uso realista para o indivíduo é <strong>guardar</strong>, não negociar: estocar poder de compra por anos, imune à inflação. O comportamento certo é o do poupador paciente, não do especulador.","tip":"<strong>Lição:</strong> baixa preferência temporal aplicada — comprar para deter, não para girar."},
   {"ic":"link","t":"Ativo ao Portador, Sem Contraparte","b":"Diferente de um depósito ou título, o Bitcoin <strong>não é dívida de ninguém</strong>: não há banco que possa quebrar, congelar ou não honrar. Você detém o ativo, não a promessa de alguém.","tip":"<strong>Modelo mental:</strong> sem contraparte = sem o risco de o outro lado falhar."},
   {"ic":"wave","t":"Volatilidade = Preço da Adoção","b":"Como ativo monetário jovem em monetização, oscila muito — é o <strong>custo de ser cedo</strong>, e tende a diminuir conforme cresce e se torna líquido.","tip":"<strong>Cuidado:</strong> só arrisque o que aguenta a volatilidade; o horizonte é de anos, não de semanas.","warn":True},
   {"ic":"eye","t":"O que o Bitcoin NÃO é","b":"Não é investimento 'que só sobe', não é dinheiro barato de varejo, não é isento de risco. <strong>Tratá-lo como qualquer dessas coisas leva a erro.</strong>","tip":"<strong>Cuidado:</strong> confundir reserva de valor com varejo (ou com retorno garantido) é a porta da especulação ingênua.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 10",
  "lessons":["Os usos centrais são reserva de valor soberana e liquidação final.","É ativo ao portador, sem risco de contraparte — você detém, não confia.","A escala vem de camadas; a base existe para garantir escassez e finalidade.","Volatilidade é o preço da adoção precoce — comportamento de poupador, não de especulador."]},
]
