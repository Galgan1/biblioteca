# -*- coding: utf-8 -*-
"""Conteúdo (pt-BR) das páginas da biblioteca para a 'Poética' de Aristóteles
(ed. Gulbenkian, trad. Eudoro de Sousa). Termos canônicos gregos preservados:
mimese, mýthos, peripécia, anagnórisis, hamartia, eleos, phobos, katharsis."""

BOOK = {
 "title": "Poética",
 "author": "Aristóteles",
 "header_light": "A POÉTICA",
 "header_bold": "DE ARISTÓTELES",
 "subtitle": "VISÃO GERAL · OS FUNDAMENTOS DA DRAMATURGIA",
 "intro": "O texto que fundou a teoria da narrativa, há 2.300 anos. Aristóteles disseca a tragédia e descobre as leis que ainda governam toda história que emociona: o enredo é a alma, o herói cai por um erro, a reviravolta surpreende e é inevitável, e a solução nasce de dentro — nunca de um truque. É o avô direto de toda dramaturgia, do teatro grego ao roteiro de cinema.",
 "description": "O tratado que fundou a teoria da narrativa. Aristóteles revela as leis da tragédia que ainda governam toda história: o enredo como alma, peripécia e reconhecimento, a hamartia do herói, a catarse, e o verossímil acima do possível.",
 "tags": ["Filosofia", "Narrativa", "Dramaturgia"],
 "progress": "7 Capítulos",
 "cover": "assets/aristoteles-poetica-cover.png",
 "overview_cards": [
   {"ic":"layers","t":"As 6 Partes da Tragédia","b":"Em ordem de importância — só a 1ª é a alma:","list":[
     "<strong>Mito (enredo)</strong> — a estruturação dos fatos; a alma.",
     "<strong>Caracteres</strong> — revelados pela escolha na ação.",
     "<strong>Pensamento</strong> — o que os agentes argumentam.",
     "<strong>Elocução</strong> — a expressão pelas palavras.",
     "<strong>Melopeia</strong> — o canto.",
     "<strong>Espetáculo</strong> — o aparato visual; o menos artístico.",
   ],"tip":"<strong>Regra:</strong> sem ação não há tragédia; sem caráter, ainda pode haver. Ação > personagem.","wide":True},
   {"ic":"spiral","t":"O Enredo Complexo","b":"A virada superior nasce de duas forças: <strong>peripécia</strong> (reviravolta no sentido contrário ao esperado) + <strong>reconhecimento</strong> (a passagem da ignorância ao saber). Juntos, como em Édipo, são o ápice.","tip":"<strong>Modelo mental:</strong> a reviravolta surpreende — mas, olhando para trás, era o único caminho (o verossímil)."},
   {"ic":"scale","t":"O Alvo: Catarse","b":"Tudo serve a um fim — provocar <strong>compaixão (eleos)</strong> e <strong>temor (phobos)</strong> e, por eles, a <strong>purificação (katharsis)</strong> das paixões. Só se atinge com um herói semelhante a nós, caindo por <strong>erro (hamartia)</strong>, não por maldade.","tip":"<strong>Como aplicar:</strong> sem semelhança com o público, não há emoção. O santo e o monstro não comovem."},
 ],
}

CHAPTERS = [
 {"slug":"ch01-mimese","sub":"CAPÍTULO 1: Mimese — a raiz da arte",
  "intro":"Toda poesia é imitação (mimese). Imitar é instinto humano desde a infância — e dela tiramos prazer mesmo do que, na realidade, nos repugnaria.",
  "cards":[
      {"ic":"mask","t":"Imitar é Instinto Humano","emph":"Instinto Humano","b":"Antes de ser técnica, a arte é impulso: imitamos desde criança, e é imitando que aprendemos o mundo. Aristóteles funda a poesia num <strong>instinto tão humano quanto a fala</strong> — o de representar “homens em ação”. Toda obra, do épico ao resumo de hoje, é uma forma de mimese: a vida refeita em imagem para ser compreendida.","tip":"<strong>Modelo mental:</strong> você não inventa do nada — recria a vida numa imagem que o público reconhece como verdadeira."},
      {"ic":"target","t":"As 3 Coordenadas da Obra","emph":"3 Coordenadas","b":"Cada arte se distingue por três escolhas: o <strong>meio</strong> (ritmo, linguagem, melodia), o <strong>objeto</strong> (homens melhores, piores ou iguais a nós) e o <strong>modo</strong> (narrar ou pôr tudo em cena). Trocar o objeto muda o gênero — herói elevado vira tragédia, homem inferior vira comédia. Fixe as três antes de criar qualquer coisa.","tip":"<strong>Como aplicar:</strong> defina meio, objeto e modo primeiro — são o mapa da obra, não o enfeite dela."},
      {"ic":"bulb","t":"O Prazer de Reconhecer","emph":"Reconhecer","b":"Olhamos com horror um cadáver na rua, mas com prazer sua imagem fiel numa obra. Por quê? Porque <strong>aprender agrada, e reconhecer “é aquele!” é um prazer do intelecto</strong>. Aí está a raiz de toda emoção estética: o espectador goza ao achar o universal — o “isso sou eu” — dentro da imagem que você construiu.","tip":"<strong>Regra:</strong> dê ao público o que ele identifica como verdadeiro; o reconhecimento é o que prende, mesmo na cena dura."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 1",
  "lessons":["Defina meio, objeto e modo antes de criar.","Imite ação, não descreva caráter.","O prazer vem do reconhecimento do universal."]},

 {"slug":"ch02-seis-partes","sub":"CAPÍTULO 2: As Seis Partes da Tragédia",
  "intro":"Toda tragédia tem seis partes — e há hierarquia. O mito (a estruturação dos fatos) é 'o princípio e como que a alma'; o resto serve a ele.",
  "cards":[
      {"ic":"target","t":"O Enredo é a Alma","emph":"a Alma","b":"Das seis partes — mito, caracteres, pensamento, elocução, melopeia, espetáculo — uma manda em todas: o <strong>mito (enredo) é “o princípio e como que a alma” da tragédia</strong>. A prova é brutal: sem ação não há tragédia; sem caráter, ainda pode haver. Personagem não vem antes da história — ele nasce das escolhas que faz dentro dela.","tip":"<strong>Regra:</strong> estruture o enredo primeiro; fala, personagem e visual servem a ele, não o contrário."},
      {"ic":"person","t":"Caráter Nasce da Ação","emph":"da Ação","b":"As pessoas “não agem para imitar caracteres, mas <strong>adquirem caráter por meio das ações</strong>”. Quem alguém é se revela no que escolhe sob pressão — não no que o autor afirma sobre ele. A tragédia imita ação e vida, não retratos parados. O herói se prova pelo gesto no momento decisivo, não pela legenda que o descreve.","tip":"<strong>Como aplicar:</strong> mostre a escolha em movimento; corte todo adjetivo que a ação não comprove."},
      {"ic":"lens","t":"O Espetáculo é a Muleta","emph":"a Muleta","b":"O aparato visual comove, mas Aristóteles o rebaixa: é “o menos artístico e o mais alheio à poesia” — obra do cenógrafo, não do poeta. Como na pintura, um simples <strong>contorno bem traçado vence as cores mais belas lançadas ao acaso</strong>. Produzir o terror pelo efeito visual, e não pela estrutura dos fatos, é confessar enredo fraco.","tip":"<strong>Sinal de alerta:</strong> se o impacto depende do visual e não dos fatos, é muleta — o efeito tem de nascer da estrutura.","warn":True},
    ],
  "lessons_title":"Lições-Chave do Capítulo 2",
  "lessons":["Construa o enredo primeiro; tudo serve a ele.","Revele caráter por escolha na ação.","Desconfie do espetáculo: o efeito nasce da estrutura."]},

 {"slug":"ch03-mito-uno-inteiro","sub":"CAPÍTULO 3: O Mito — Inteiro, Uno, com Magnitude",
  "intro":"O enredo bem construído é inteiro (começo-meio-fim por causa), uno (uma só ação, não uma biografia) e tem magnitude abarcável pela memória.",
  "cards":[
      {"ic":"steps","t":"Causa, Não Cronologia","emph":"Não Cronologia","b":"Um todo tem começo, meio e fim — mas não no relógio, e sim na lógica. <strong>Começo</strong> é o que não exige nada antes; <strong>fim</strong> é o que nada exige depois; <strong>meio</strong> é o que decorre de um e leva a outro. O cimento é a <strong>necessidade ou a verossimilhança</strong>: cada fato puxa o seguinte. “E aí... e aí...” é cronologia; “portanto... mas então...” é enredo.","tip":"<strong>Como aplicar:</strong> ligue os fatos por causa — se a única ligação entre duas cenas é o tempo, falta enredo."},
      {"ic":"link","t":"Unidade de Ação, Não de Herói","emph":"de Herói","b":"“Um só homem teve infinitos sucessos, de alguns dos quais não resulta unidade alguma.” Reunir tudo o que aconteceu a uma pessoa dá biografia, não história. <strong>A unidade nasce de uma única ação que se completa</strong> — Homero não contou toda a vida de Ulisses, centrou a Odisseia num só fio: o regresso. O resto, ficou de fora.","tip":"<strong>Modelo mental:</strong> “a vida de X” não é uma história; “a ação em que X persegue uma coisa até o fim”, sim."},
      {"ic":"sword","t":"O Teste da Remoção","emph":"Remoção","b":"A régua mais afiada da Poética: “aquilo cuja presença ou ausência <strong>não traz alteração sensível não é parte do todo</strong>.” Se uma cena pode sair, ou mudar de lugar, sem desfazer o conjunto, ela não pertence ao conjunto. A peça é um organismo — toda parte amputável era tumor, não membro. É o que separa enredo de colagem episódica.","tip":"<strong>Regra:</strong> o que sai sem fazer falta, corte — sem dó. Magnitude é o que a memória abarca de uma vez.","warn":True},
    ],
  "lessons_title":"Lições-Chave do Capítulo 3",
  "lessons":["Ligue os fatos por necessidade/verossimilhança.","Una pela ação, não pela biografia.","Aplique o teste da remoção: o supérfluo, corte."]},

 {"slug":"ch04-verossimil","sub":"CAPÍTULO 4: Verossímil vs. Possível",
  "intro":"A poesia narra o universal (o que tal pessoa faria por verossimilhança); a história, o particular. Por isso 'a poesia é mais filosófica que a história'.",
  "cards":[
      {"ic":"book","t":"O Universal, Não o Particular","emph":"Universal","b":"O historiador conta <strong>o que foi</strong>; o poeta, <strong>o que poderia ser</strong> — o que tal tipo de pessoa diria ou faria, conforme o verossímil ou o necessário. Por isso “a poesia é mais filosófica e elevada que a história”: ela mira a lei humana, não o caso isolado. O particular informa um; o universal ressoa em todos os que assistem.","tip":"<strong>Como aplicar:</strong> não pergunte “isto aconteceu?”, pergunte “é assim que uma pessoa dessas agiria?”."},
      {"ic":"key","t":"Convicção Vence Veracidade","emph":"Convicção","b":"A regra de ouro: prefira <strong>o impossível que o público aceita ao possível que ele não engole</strong>. Um milagre bem motivado convence; um fato real, mal preparado, é rejeitado em cena. O critério da arte não é o do tribunal nem o da física — é a probabilidade dramática. Verdade sem convicção morre; mentira convincente comove.","tip":"<strong>Modelo mental:</strong> o crível, não o factual, é a moeda da ficção — motive bem e o impossível passa."},
      {"ic":"spark","t":"O Poeta é Fabricante de Mitos","emph":"Fabricante de Mitos","b":"“O poeta deve ser mais <strong>fabricante de enredos que de versos</strong>” — porque é imitador de ações, não de rimas. Pôr história em verso continua sendo história; Empédocles versejou física e não virou poeta. O que faz a poesia é a ação construída sob a lei do verossímil. A forma — verso, prosa, vídeo — é só o veículo.","tip":"<strong>Lição:</strong> trabalhe primeiro a ação que convence; a forma bonita é acabamento, nunca o alicerce."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 4",
  "lessons":["Busque o universal: o que este tipo de pessoa faria.","Prefira o impossível verossímil ao possível inverossímil.","A obra se faz pela imitação de ação, não pela forma."]},

 {"slug":"ch05-peripecia-reconhecimento","sub":"CAPÍTULO 5: Peripécia e Reconhecimento",
  "intro":"O enredo complexo — superior ao simples — move a mudança de fortuna por peripécia (reviravolta), reconhecimento (descoberta) ou ambos, sempre conforme o verossímil.",
  "cards":[
      {"ic":"pivot","t":"Peripécia: a Virada Inevitável","emph":"Peripécia","b":"A peripécia é a <strong>mudança da ação no sentido contrário ao esperado</strong> — jamais aleatória: brota da lógica dos próprios fatos, conforme o verossímil e o necessário. É o gesto que pretende salvar e arruína, a notícia boa que precipita a queda. A grande virada surpreende no instante e, olhando para trás, era o único caminho possível.","tip":"<strong>Como aplicar:</strong> plante a causa cedo; a reviravolta tem de ser inesperada na hora e inevitável em retrospecto."},
      {"ic":"lens","t":"Reconhecimento: da Ignorância ao Saber","emph":"Reconhecimento","b":"O reconhecimento (anagnórisis) é a <strong>passagem da ignorância ao conhecimento</strong> que vira amor em ódio, ou o inverso, entre os que o destino aproxima. O mais belo nasce dos próprios fatos; os inferiores vêm de sinais, memórias, cicatrizes. Descobrir a verdade pela lógica da ação vale ouro; descobri-la por um adereço conveniente é trapaça.","tip":"<strong>Regra:</strong> faça a descoberta brotar do enredo — colar, cicatriz ou bilhete oportuno é reconhecimento de segunda."},
      {"ic":"spark","t":"Édipo: os Dois Golpes Juntos","emph":"os Dois Golpes Juntos","b":"O paradigma: o mensageiro chega para libertar Édipo do medo — e, ao revelar quem ele é, faz o contrário. A <strong>peripécia (alívio que vira catástrofe) coincide com o reconhecimento (Édipo se descobre)</strong> num só golpe nascido da mesma ação. Quando reviravolta e descoberta caem juntas, e do próprio enredo, está o ápice do efeito trágico.","tip":"<strong>Modelo mental:</strong> os dois eixos fundidos num único momento, vindos da ação, multiplicam compaixão e temor."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 5",
  "lessons":["Prefira o enredo complexo: peripécia e/ou reconhecimento.","A descoberta nasce da ação, não de objetos externos.","A reviravolta surpreende, mas obedece ao verossímil."]},

 {"slug":"ch06-hamartia-catarse","sub":"CAPÍTULO 6: Hamartia e Catarse",
  "intro":"O efeito trágico — compaixão, temor e catarse — exige um herói específico: nem virtuoso demais nem vil, mas semelhante a nós, caindo por um erro (hamartia), não por maldade.",
  "cards":[
      {"ic":"person","t":"O Herói do Meio","emph":"do Meio","b":"Três figuras matam a tragédia: o <strong>virtuoso</strong> arruinado (repugna), o <strong>mau</strong> que prospera (nada de trágico), o <strong>perverso</strong> que cai (justo, mas frio). Sobra um herói possível: o <strong>intermediário — bom, ilustre, semelhante a nós, que cai por um erro, não por vício</strong>. É a falha de um homem como nós, não a maldade, que abre o público.","tip":"<strong>Como aplicar:</strong> dê ao herói virtude e uma hamartia — o erro de juízo que o arruína sem que ele mereça tanto."},
      {"ic":"scale","t":"Compaixão e Temor","emph":"Compaixão e Temor","b":"O alvo é duplo: <strong>eleos</strong> (compaixão) nasce do infortúnio imerecido de alguém como nós; <strong>phobos</strong> (temor) nasce porque <strong>o que cai é semelhante a nós — poderia ser conosco</strong>. Sem essa semelhança não há emoção trágica: o santo distante e o monstro alheio não comovem. A queda só dói quando reconhecemos no que tomba um de nós.","tip":"<strong>Modelo mental:</strong> só nos abala quem reconhecemos como par — construa o herói para o público dizer “poderia ser eu”."},
      {"ic":"mask","t":"Cuidado com o Final Moralista","emph":"Final Moralista","b":"O <strong>final duplo</strong> — bons premiados, maus punidos — agrada à plateia fraca, mas é próprio da comédia, e <strong>esteriliza a emoção trágica</strong>. A justiça poética impecável tranquiliza e mata a catarse: se tudo se resolve com castigo certo e prêmio merecido, você saiu da tragédia. O efeito vive do desajuste entre a falta pequena e a dor enorme.","tip":"<strong>Sinal de alerta:</strong> contas que fecham com justiça perfeita = comédia disfarçada; a tragédia precisa do imerecido.","warn":True},
    ],
  "lessons_title":"Lições-Chave do Capítulo 6",
  "lessons":["O alvo é eleos + phobos → catarse.","Use o herói do meio: cai por erro, não por maldade.","Evite o final moralista duplo."]},

 {"slug":"ch07-antipadroes","sub":"CAPÍTULO 7: Anti-padrões e Soluções",
  "intro":"Aristóteles cataloga os erros que arruínam a tragédia — sobretudo o deus ex machina, o episódico e a aposta no espetáculo. Bons enredos resolvem-se de dentro.",
  "cards":[
      {"ic":"wrench","t":"Nada de Deus ex Machina","emph":"Deus ex Machina","b":"“É preciso que o desenlace surja <strong>do próprio enredo</strong>, e não, como na Medeia, de um deus.” Salvar o herói com um carro alado vindo do céu é desatar o nó por fora — confissão de que a estrutura não se sustenta. A máquina só vale para o que está fora da ação: o passado, o futuro profetizado. <strong>A solução já está plantada no problema.</strong>","tip":"<strong>Regra:</strong> se o clímax precisa de um resgate externo, o enredo está quebrado — replante a causa lá atrás.","warn":True},
      {"ic":"gap","t":"O Irracional Fica Fora","emph":"Fica Fora","b":"O inverossímil é veneno dentro da cena, mas tolerável fora dela. Aristóteles perdoa os prodígios da Odisseia porque ficam <strong>longe da ação representada</strong>, onde não ferem a crença do espectador. O que se vê em cena tem de obedecer ao verossímil; o irracional inevitável, exile-o para o antes, o depois ou o relato — nunca para o palco.","tip":"<strong>Como aplicar:</strong> o que o público não engoliria de perto, conte de longe — fora do que se encena diante dos olhos."},
      {"ic":"eye","t":"Veja a Cena Diante dos Olhos","emph":"Diante dos Olhos","b":"O poeta deve <strong>encenar mentalmente a ação como se fosse espectador</strong>, vendo tudo diante dos olhos enquanto constrói. Só assim flagra a contradição que no papel passa batida e descobre o gesto exato. É a checagem que não custa nada e salva tudo: o que parece coerente lido pode soar falso quando imaginado em cena.","tip":"<strong>Hábito:</strong> antes de redigir, rode o filme na cabeça — incoerências invisíveis na página saltam aos olhos encenadas."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 7",
  "lessons":["O desenlace nasce da ação, nunca de intervenção externa.","Mantenha o irracional fora da cena representada.","Visualize a ação ao construir; não confie no espetáculo."]},
]
