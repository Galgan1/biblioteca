# -*- coding: utf-8 -*-
"""Conteúdo (pt-BR) de 'A Lógica do Cisne Negro' (Nassim Nicholas Taleb)."""

BOOK = {
  "title": "A Lógica do Cisne Negro",
  "author": "Nassim Nicholas Taleb",
  "header_light": "CISNE",
  "header_bold": "NEGRO",
  "subtitle": "VISÃO GERAL · O IMPACTO DO ALTAMENTE IMPROVÁVEL",
  "intro": "Um Cisne Negro é o evento raro, de impacto extremo, que depois racionalizamos como se fosse previsível. Taleb mostra que quase tudo que importa na história vem desses eventos — e que nossas ferramentas de previsão (a curva de sino, as narrativas, os modelos de jogo) nos cegam para eles. A saída não é prever melhor, mas tornar-se robusto ao imprevisível.",
  "description": "Ensaio de Nassim Taleb sobre o evento Cisne Negro: raro, de impacto extremo e previsível só em retrospecto. Mediocristão × Extremistão, falácia narrativa, problema da indução (o peru de Russell), evidência silenciosa, falácia lúdica, arrogância epistêmica, a fraude da curva de sino e a robustez (estratégia barbell) diante do imprevisível.",
  "tags": ["Incerteza", "Risco", "Epistemologia"],
  "progress": "8 Capítulos",
  "cover": "assets/cisne-negro-cover.png",
  "overview_cards": [
    {"ic":"wave","t":"O Cisne Negro","b":"Evento que reúne três traços: é uma <strong>surpresa rara</strong> (nada no passado apontava), tem <strong>impacto extremo</strong> e é <strong>racionalizado depois</strong> como se fosse previsível. Quase tudo que importa — crashes, guerras, descobertas — é Cisne Negro.","tip":"<strong>Teste:</strong> foi imprevisto? o impacto foi extremo? estão contando uma história que o faz parecer óbvio só agora? Três 'sim' = Cisne Negro.","warn":True},
    {"ic":"scale","t":"Mediocristão × Extremistão","b":"No <strong>Mediocristão</strong> (peso, altura) nenhum evento isolado move o total e a curva de sino funciona. No <strong>Extremistão</strong> (riqueza, vendas, fama, crashes) um único evento domina tudo — é o lar do Cisne Negro.","tip":"<strong>Modelo mental:</strong> antes de qualquer estatística, pergunte 'um único caso pode ser maior que todo o resto somado?' Se sim, é Extremistão."},
    {"ic":"eye","t":"Evidência Silenciosa","b":"Julgamos pelo que sobrou e está visível, ignorando o <strong>cemitério dos que fracassaram igual</strong>. A história é escrita pelos vencedores — literalmente, na amostra. Por isso confundimos sorte com talento (o 'idiota sortudo').","tip":"<strong>Para refletir:</strong> antes de copiar um vencedor, pergunte 'onde estão os que fizeram o mesmo e quebraram?'"},
  ],
}

CHAPTERS = [
  {
    "slug": "ch01-o-cisne-negro",
    "sub": "CAPÍTULO 1: O que é um Cisne Negro",
    "intro": "Na Europa, 'todo cisne é branco' foi verdade indutiva até acharem cisnes pretos na Austrália — uma única observação destruiu milênios de certeza. O Cisne Negro é o evento raro, de impacto extremo, que o cérebro racionaliza depois como previsível, apagando a surpresa e impedindo o aprendizado.",
    "cards": [
      {"ic":"wave","t":"A Tríade do Cisne Negro","b":"Três traços juntos: <strong>raridade</strong> (fora das expectativas), <strong>impacto extremo</strong> e <strong>previsibilidade retrospectiva</strong> (parece óbvio só depois). É raro, mas decide o jogo — e quase tudo que importa na história entra nessa categoria.","tip":"<strong>Como aplicar:</strong> trate todo 'eu sabia que ia acontecer' como ilusão — se fosse óbvio, alguém teria lucrado antes, com risco real.","warn":True},
      {"ic":"spiral","t":"O Peru de Russell","b":"O peru é alimentado todo dia; a cada refeição sua confiança de que 'cuidam de mim' cresce. No milésimo dia, véspera de Ação de Graças, no auge da certeza, é abatido. O ponto de <strong>máxima certeza estatística</strong> foi o de <strong>máximo risco</strong>.","tip":"<strong>Modelo mental:</strong> ausência de evidência ≠ evidência de ausência. Nunca ter visto algo não prova que não exista."},
      {"ic":"lens","t":"Previsibilidade Retrospectiva","b":"Depois do fato, a mente costura uma narrativa que apaga a surpresa. Isso nos faz confiar de novo e <strong>não aprender que não previmos</strong>. O 'óbvio em retrospecto' é uma ilusão fabricada pela memória.","tip":"<strong>Para refletir:</strong> registre previsões por escrito ANTES; depois compare com a história que você conta. O choque revela o quanto não previu."},
      {"ic":"book","t":"A Antibiblioteca de Eco","b":"Os livros <strong>não lidos</strong> valem mais que os lidos: sabem o que você ignora. A biblioteca é monumento ao desconhecido, não troféu do conhecido. Meça seu saber pela consciência do que falta, não pelo que domina.","tip":"<strong>Modelo mental:</strong> quanto mais você sabe, mais sabe o tamanho do que não sabe — e é de lá que vem o Cisne Negro."},
    ],
    "lessons_title": "Lições-Chave do Capítulo 1",
    "lessons": [
      "Um Cisne Negro é raro, de impacto extremo e racionalizado depois como previsível.",
      "O que está fora do seu mapa costuma importar mais do que o que está nele.",
      "Ausência de evidência não é evidência de ausência — o evento decisivo ainda não apareceu na amostra.",
      "A previsibilidade retrospectiva é a armadilha que impede o aprendizado.",
    ],
  },
  {
    "slug": "ch02-arrogancia-epistemica",
    "sub": "CAPÍTULO 2: Arrogância Epistêmica e a Tríade da Opacidade",
    "intro": "Achamos que sabemos mais do que sabemos. Essa arrogância epistêmica cresce com a informação e a especialização, e nos cega para o Cisne Negro. Diante da história, a mente sofre três males — a tríade da opacidade — que a fazem confundir o mapa elegante com o território caótico.",
    "cards": [
      {"ic":"target","t":"Arrogância Epistêmica","b":"Superestimar o que se sabe e subestimar a incerteza. Mais informação aumenta a <strong>confiança</strong> muito mais que a <strong>acurácia</strong>. O especialista erra quase como o leigo — porém com mais convicção.","tip":"<strong>Como aplicar:</strong> compare a confiança declarada com o histórico real de acertos. Quando divergem, desconfie do confiante.","warn":True},
      {"ic":"triangle","t":"A Tríade da Opacidade","b":"Três doenças da mente diante da história: <strong>(a) ilusão de entender</strong> um mundo mais aleatório do que cremos; <strong>(b) distorção retrospectiva</strong> (só julgamos depois, reescrevendo); <strong>(c) excesso de fé na informação</strong> e nos que 'platonificam'.","tip":"<strong>Modelo mental:</strong> para cada explicação histórica, pergunte se não é só uma história contada de trás para frente."},
      {"ic":"layers","t":"Platonicidade","b":"Confundir o <strong>mapa</strong> com o <strong>território</strong>: preferir formas puras e categorias limpas (triângulos, utopias) à bagunça do real. A 'prega platônica' é onde o modelo quebra — e o Cisne Negro entra justamente ali.","tip":"<strong>Para refletir:</strong> quanto mais elegante e lisa a teoria, mais perigosa a borda onde ela falha."},
      {"ic":"eye","t":"O Idiota Sortudo","b":"Vemos só os vencedores; quem arriscou igual e quebrou some da amostra (a <strong>evidência silenciosa</strong>). Assim, sorte vira 'talento' e acaso vira 'método'. Buscar exemplos que confirmam não prova nada — um contraexemplo derruba.","tip":"<strong>Regra:</strong> procure o contraexemplo que refuta, não os mil casos que confirmam."},
    ],
    "lessons_title": "Lições-Chave do Capítulo 2",
    "lessons": [
      "Quanto mais sabemos, mais confiantes ficamos — não necessariamente mais certos.",
      "A tríade da opacidade: ilusão de entender, distorção retrospectiva, excesso de fé na informação.",
      "Platonicidade é confundir o mapa elegante com o território caótico.",
      "O viés de sobrevivência transforma sorte em 'talento'; procure o contraexemplo, não a confirmação.",
    ],
  },
  {
    "slug": "ch03-falacia-narrativa",
    "sub": "CAPÍTULO 3: A Falácia Narrativa",
    "intro": "A mente não suporta fatos crus: ela tece histórias de causa e efeito para reduzir a complexidade a algo memorável. Essa falácia narrativa dá a ilusão de entender o passado e prever o futuro — e esconde sistematicamente o papel do acaso e do Cisne Negro.",
    "cards": [
      {"ic":"bubble","t":"A Falácia Narrativa","b":"A tendência a impor enredos lineares sobre fatos, preferindo <strong>histórias compactas à verdade bruta</strong>. Toda narrativa adiciona um 'porque' que pode não existir. Lembramos melhor o que tem enredo — e passamos a acreditar nele.","tip":"<strong>Como aplicar:</strong> separe o que aconteceu (fato) do porquê alegado (interpolação).","warn":True},
      {"ic":"fork","t":"O Teste das Duas Histórias","b":"Se uma narrativa convincente explicaria <strong>igualmente bem o resultado oposto</strong>, ela não explica nada. O noticiário usa 'a inflação' para explicar a alta E a queda do mercado — sinal de que a história é decorativa, não causal.","tip":"<strong>Modelo mental:</strong> quanto mais redonda e fluente a explicação, mais ela apagou o acaso."},
      {"ic":"steps","t":"Fatos Antes da Narrativa","b":"O cérebro premia o reconhecimento de padrões mesmo onde só há <strong>ruído</strong>. Em decisão real, prefira a lista crua de fatos à história bem contada — e registre previsões por escrito para flagrar a falácia depois.","tip":"<strong>Para refletir:</strong> pós-racionalizar o sucesso ou o fracasso é montar a cadeia causal só depois de saber o desfecho."},
    ],
    "lessons_title": "Lições-Chave do Capítulo 3",
    "lessons": [
      "A mente troca a verdade crua por histórias compactas — e acredita nelas.",
      "Se a narrativa explicaria igualmente bem o resultado oposto, ela não explica nada.",
      "Reescrevemos a memória para caber num bom enredo.",
      "A narrativa apaga o acaso — e com ele, o Cisne Negro.",
    ],
  },
  {
    "slug": "ch04-mediocristao-extremistao",
    "sub": "CAPÍTULO 4: Mediocristão × Extremistão",
    "intro": "Há dois tipos de aleatoriedade, dois 'países'. No Mediocristão, nenhum evento isolado muda muito o total — a média manda. No Extremistão, um único evento pode dominar tudo — é o reino do escalável e o lar dos Cisnes Negros. Confundir um pelo outro é o erro fatal.",
    "cards": [
      {"ic":"mountain","t":"Mediocristão","b":"Domínio do <strong>não escalável</strong> e da física: adicione a maior amostra possível e a média quase não se move (peso, altura, calorias). Há um teto natural. Aqui a curva de sino funciona e o Cisne Negro é fraco.","tip":"<strong>Régua:</strong> 'o maior caso isolado muda o total?' Se não, é Mediocristão."},
      {"ic":"spark","t":"Extremistão","b":"Domínio do <strong>escalável</strong> (riqueza, vendas, fama, mortes em guerra). Um único caso pode ser maior que todos os outros somados. A média engana, a gaussiana mente — e é aqui que vivem os Cisnes Negros.","tip":"<strong>Régua:</strong> 'um único evento pode ser maior que todo o resto junto?' Se sim, é Extremistão — espere Cisnes Negros.","warn":True},
      {"ic":"scale","t":"Escalável × Não Escalável","b":"O dentista é não escalável (ganho proporcional às horas); o escritor, o ator e o trader são escaláveis (um trabalho atinge milhões — <strong>winner-take-all</strong>). O escalável concentra ganhos e amplia o risco de cauda.","tip":"<strong>Modelo mental:</strong> classifique o 'país' ANTES de usar qualquer estatística — a ferramenta gaussiana só vale no Mediocristão."},
    ],
    "lessons_title": "Lições-Chave do Capítulo 4",
    "lessons": [
      "Mediocristão: nenhum caso isolado move o total; a gaussiana funciona.",
      "Extremistão: um único evento pode dominar tudo; é onde vivem os Cisnes Negros.",
      "Antes de qualquer estatística, identifique em qual 'país' você está.",
      "O escalável concentra ganhos (winner-take-all) e amplia o risco de cauda.",
    ],
  },
  {
    "slug": "ch05-falacia-ludica",
    "sub": "CAPÍTULO 5: A Falácia Lúdica e a Evidência Silenciosa",
    "intro": "Confundimos o risco esterilizado dos jogos (dados, cassino, modelos) com a incerteza da vida real, onde as regras são desconhecidas. Essa falácia lúdica é a base de quase toda matemática de risco mal aplicada. E a evidência silenciosa esconde os fracassos, distorcendo as probabilidades.",
    "cards": [
      {"ic":"target","t":"A Falácia Lúdica","b":"Tratar a incerteza da vida como a de um jogo de azar com probabilidades calculáveis. No cassino você conhece as regras; na vida, não — e <strong>o que te quebra vem de fora do modelo</strong>. Precisão decimal sobre incerteza real é fingimento.","tip":"<strong>Como aplicar:</strong> diante de um modelo de risco, pergunte 'que evento, fora deste modelo, tornaria estes cálculos irrelevantes?'","warn":True},
      {"ic":"eye","t":"Evidência Silenciosa","b":"Julgamos pelo que sobrou, ignorando o <strong>cemitério dos que fracassaram igual</strong>. Cícero: os náufragos que rezaram e se salvaram pintam quadros; os que rezaram e afundaram, não. A história é escrita pelos sobreviventes.","tip":"<strong>Modelo mental:</strong> antes de copiar uma receita de sucesso, reconstrua a amostra completa — incluindo os invisíveis."},
      {"ic":"person","t":"Os Idiotas Sortudos","b":"Entre milhares de gestores, alguns 'ganham do mercado' por puro acaso e viram 'gênios' de palco. O histórico é <strong>artefato de sobrevivência</strong>: resultado não é prova de habilidade. A sorte do Extremistão se disfarça de talento.","tip":"<strong>Para refletir:</strong> o desempenho se mantém quando se conta TODO o universo inicial, não só os sobreviventes?"},
    ],
    "lessons_title": "Lições-Chave do Capítulo 5",
    "lessons": [
      "A vida não é cassino: o que quebra você vem de fora do modelo.",
      "Precisão estatística sobre incerteza real é fingimento perigoso.",
      "A evidência silenciosa esconde os fracassos e infla as probabilidades de sucesso.",
      "Resultado não é prova de habilidade — sorte se disfarça de talento.",
    ],
  },
  {
    "slug": "ch06-limites-da-previsao",
    "sub": "CAPÍTULO 6: Os Limites da Previsão",
    "intro": "Somos péssimos em prever, sobretudo o que mais importa, e pioramos quando nos especializamos. A maior parte do progresso vem de descobertas que ninguém planejou. Em vez de prever, é preciso preparar-se para o imprevisível e maximizar a exposição ao acaso positivo.",
    "cards": [
      {"ic":"lens","t":"O Escândalo da Previsão","b":"Especialistas erram quase tanto quanto leigos no longo prazo — e com <strong>mais confiança</strong>. Mais credenciais aumentam a arrogância, não a acurácia. A previsão de longo prazo do que importa é logicamente impossível.","tip":"<strong>Como aplicar:</strong> peça o histórico de erros do previsor; olhe o intervalo de incerteza, ignore o ponto central.","warn":True},
      {"ic":"key","t":"Serendipidade","b":"Penicilina, internet, laser: grandes descobertas foram <strong>acidentais</strong>. O conhecimento avança mais por acaso explorado do que por planejamento. Para prever o futuro, você teria de prever as descobertas futuras — o que é impossível.","tip":"<strong>Modelo mental:</strong> maximize a exposição ao acaso positivo em vez de apostar num plano único."},
      {"ic":"pivot","t":"Tinkering (Bricolagem)","b":"Avançar por <strong>tentativa e erro barata</strong>, com muitas apostas pequenas, colhendo Cisnes Negros positivos. Troque 'prever o futuro' por 'preparar-se para vários futuros'. Foque em robustez, não em acerto.","tip":"<strong>Para refletir:</strong> planejamento rígido de longo prazo assume um futuro conhecível — e quebra no primeiro Cisne Negro."},
    ],
    "lessons_title": "Lições-Chave do Capítulo 6",
    "lessons": [
      "Erramos previsões justamente no que mais importa — e com excesso de confiança.",
      "Especialização aumenta a arrogância, não a acurácia.",
      "As maiores descobertas são acidentais: cultive a serendipidade.",
      "Não tente prever o futuro; posicione-se para sobreviver e lucrar com o imprevisto.",
    ],
  },
  {
    "slug": "ch07-fraude-do-sino",
    "sub": "CAPÍTULO 7: A Curva de Sino, Essa Grande Fraude Intelectual",
    "intro": "A curva de sino é uma ferramenta legítima no Mediocristão e uma fraude intelectual quando aplicada ao Extremistão. Ela faz os eventos extremos parecerem impossíveis — exatamente os Cisnes Negros que dominam o resultado. É o erro embutido em quase toda a finança acadêmica.",
    "cards": [
      {"ic":"wave","t":"A Fraude do Sino","b":"Na gaussiana, a probabilidade <strong>despenca exponencialmente</strong> à medida que o evento se afasta da média — um desvio de 10 sigmas é 'impossível'. No Extremistão esses desvios acontecem e definem tudo. Usar o sino ali subestima o risco em ordens de magnitude.","tip":"<strong>Como aplicar:</strong> a variável é escalável? Então o sino está mentindo sobre as caudas.","warn":True},
      {"ic":"layers","t":"Caudas Gordas (Fat Tails)","b":"A gaussiana tem <strong>caudas finas</strong> (extremos somem rápido); o Extremistão tem <strong>caudas gordas</strong> (extremos raros, porém devastadores e mais frequentes do que o sino prevê). Desvio-padrão e 'sigmas' dão falsa segurança.","tip":"<strong>Regra:</strong> em domínios sociais e financeiros, assuma fat tails por padrão."},
      {"ic":"constellation","t":"Cisnes Cinza","b":"O crash de 1987 (-22,6% num dia) tinha, pelo sino, probabilidade quase nula — e aconteceu, e voltou (1998, 2008). Modelados por <strong>fractais</strong>, esses extremos viram <strong>cisnes cinza</strong>: raros e grandes, mas não totalmente surpreendentes.","tip":"<strong>Modelo mental:</strong> a curva de sino é mapa de cidade plana usado numa cordilheira — preciso onde foi desenhado, suicida fora dela."},
    ],
    "lessons_title": "Lições-Chave do Capítulo 7",
    "lessons": [
      "A gaussiana é válida no Mediocristão e fraudulenta no Extremistão.",
      "Caudas gordas: extremos são mais frequentes e devastadores do que o sino prevê.",
      "Desvio-padrão e 'sigmas' dão falsa segurança em domínios escaláveis.",
      "Em risco financeiro, assuma fat tails por padrão.",
    ],
  },
  {
    "slug": "ch08-robustez-e-barbell",
    "sub": "CAPÍTULO 8: Robustez, Fragilidade e a Estratégia Barbell",
    "intro": "Já que não dá para prever Cisnes Negros, a saída não é prever melhor — é construir robustez. Torne-se imune aos Cisnes Negros negativos (que te quebram) e exposto aos positivos (que te enriquecem). A tática prática é a estratégia barbell, dos halteres.",
    "cards": [
      {"ic":"scale","t":"Robustez × Fragilidade","b":"O <strong>frágil</strong> é destruído pelo evento extremo; o <strong>robusto</strong> sobrevive a ele. Como o extremo é inevitável e imprevisível, projete carteira, carreira e sistema para resistir ao pior caso desconhecido — antes de otimizar retorno.","tip":"<strong>Como aplicar:</strong> pergunte 'o que me mata se o impensável acontecer?' e elimine essa exposição primeiro.","warn":True},
      {"ic":"wrench","t":"Estratégia Barbell","b":"Combine <strong>extremo conservadorismo</strong> (~85–90% em ativos hiperseguros, perda máxima conhecida e pequena) com <strong>extrema especulação</strong> (~10–15% em apostas de alto retorno e perda limitada). <strong>Esvazie o meio-termo</strong> de risco 'moderado' — que esconde a cauda gorda.","tip":"<strong>Regra:</strong> blindar embaixo, apostar pequeno em cima, esvaziar o meio."},
      {"ic":"spark","t":"Assimetria (Convexidade)","b":"Busque posições com <strong>perda pequena e limitada</strong> e <strong>ganho grande e ilimitado</strong>. Uma aposta de 10% pode multiplicar por 100; o máximo que se perde são os 10%. Os fractais de Mandelbrot modelam o Extremistão melhor que o sino.","tip":"<strong>Para refletir:</strong> o 'risco moderado' é a posição mais perigosa — confiança falsa somada à exposição à cauda."},
    ],
    "lessons_title": "Lições-Chave do Capítulo 8",
    "lessons": [
      "Não preveja Cisnes Negros — torne-se robusto a eles.",
      "Blinde-se contra o Cisne Negro negativo; exponha-se ao positivo.",
      "Barbell: extremo seguro + extremo especulativo, sem meio-termo.",
      "Busque assimetria: perda pequena e limitada, ganho grande e ilimitado.",
    ],
  },
]
