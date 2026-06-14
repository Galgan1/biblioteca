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
 "progress": "7 Capítulos Completos",
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
   {"ic":"mask","t":"As 3 Variáveis da Mimese","b":"Toda arte imita 'homens em ação', diferindo em: <strong>Meio</strong> (ritmo, linguagem, melodia), <strong>Objeto</strong> (homens melhores, piores ou iguais a nós) e <strong>Modo</strong> (narrando ou pondo todos em ação).","tip":"<strong>Como aplicar:</strong> para projetar uma obra, fixe as três coordenadas antes de criar."},
   {"ic":"bulb","t":"O Prazer de Aprender","b":"Contemplamos com prazer a imagem fiel até do que é penoso, <strong>porque aprender agrada</strong> — reconhecer 'ah, é aquele!' é a raiz cognitiva do prazer estético.","tip":"<strong>Modelo mental:</strong> o reconhecimento dá prazer; dê ao público o que ele identifica como verdadeiro."},
   {"ic":"person","t":"Imita-se Ação, não Pessoas","b":"Mesmo num resumo ou documentário, você representa um <strong>fazer</strong>, não descreve um <strong>ser</strong>. A história é imitação de ação e de vida.","tip":"<strong>Regra:</strong> mostre a escolha em movimento, não o atributo parado."},
  ],
  "lessons_title":"Lições-Chave do Capítulo 1",
  "lessons":["Defina meio, objeto e modo antes de criar.","Imite ação, não descreva caráter.","O prazer vem do reconhecimento do universal."]},

 {"slug":"ch02-seis-partes","sub":"CAPÍTULO 2: As Seis Partes da Tragédia",
  "intro":"Toda tragédia tem seis partes — e há hierarquia. O mito (a estruturação dos fatos) é 'o princípio e como que a alma'; o resto serve a ele.",
  "cards":[
   {"ic":"target","t":"O Mito é a Alma","b":"Das seis partes, o <strong>mito (enredo)</strong> é a mais importante: 'os personagens não agem para imitar caracteres, mas <strong>adquirem caracteres por meio das ações</strong>'. A tragédia é imitação de ação e de vida.","tip":"<strong>Como aplicar:</strong> construa o enredo primeiro; personagem, fala e visual servem a ele.","wide":True},
   {"ic":"eye","t":"Espetáculo é o Degrau Mais Baixo","b":"O <strong>espetáculo</strong> (aparato visual) comove, mas é 'o menos artístico e o mais alheio à poesia' — depende do cenógrafo, não do poeta. Produzir o terrível pelo aparato em vez da estrutura é inferior.","tip":"<strong>Sinal de alerta:</strong> confiar o efeito ao visual é muleta — o efeito deve nascer dos fatos.","warn":True},
   {"ic":"lens","t":"O Contorno vale mais que as Cores","b":"Como na pintura: um simples <strong>contorno em branco e preto</strong> (o enredo) agrada mais que as cores mais belas lançadas ao acaso (espetáculo sem estrutura).","tip":"<strong>Lição:</strong> esboço bem desenhado > borrão colorido."},
  ],
  "lessons_title":"Lições-Chave do Capítulo 2",
  "lessons":["Construa o enredo primeiro; tudo serve a ele.","Revele caráter por escolha na ação.","Desconfie do espetáculo: o efeito nasce da estrutura."]},

 {"slug":"ch03-mito-uno-inteiro","sub":"CAPÍTULO 3: O Mito — Inteiro, Uno, com Magnitude",
  "intro":"O enredo bem construído é inteiro (começo-meio-fim por causa), uno (uma só ação, não uma biografia) e tem magnitude abarcável pela memória.",
  "cards":[
   {"ic":"steps","t":"Inteiro: Causa, não Cronologia","b":"<strong>Começo</strong> = o que não segue necessariamente de outra coisa; <strong>fim</strong> = o que sucede por necessidade e nada o segue; <strong>meio</strong> = o que segue algo e é seguido por algo. O cimento é a <strong>necessidade ou a verossimilhança</strong>.","tip":"<strong>Como aplicar:</strong> ligue os fatos por causa, não por 'e aí... e aí... e aí'."},
   {"ic":"link","t":"Unidade de Ação, não de Herói","b":"'Um só homem teve infinitos sucessos, de alguns dos quais não resulta unidade alguma.' A unidade vem da <strong>ação única</strong> — não da biografia do protagonista. Homero centrou a Odisseia em <strong>uma</strong> ação: o regresso.","tip":"<strong>Modelo mental:</strong> 'tudo o que aconteceu a Héracles' não faz uma história; uma ação que se completa, faz."},
   {"ic":"sword","t":"O Teste da Remoção","b":"'Aquilo cuja presença ou ausência não traz alteração sensível <strong>não é parte do todo</strong>.' Se uma cena pode sair ou mudar de lugar sem desfazer o conjunto, ela não pertence ao conjunto.","tip":"<strong>Regra:</strong> o que sai sem fazer falta, corte. É o que separa enredo de biografia.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 3",
  "lessons":["Ligue os fatos por necessidade/verossimilhança.","Una pela ação, não pela biografia.","Aplique o teste da remoção: o supérfluo, corte."]},

 {"slug":"ch04-verossimil","sub":"CAPÍTULO 4: Verossímil vs. Possível",
  "intro":"A poesia narra o universal (o que tal pessoa faria por verossimilhança); a história, o particular. Por isso 'a poesia é mais filosófica que a história'.",
  "cards":[
   {"ic":"book","t":"Universal vs. Particular","b":"O historiador conta <strong>o que foi</strong>; o poeta, <strong>o que poderia ser</strong> — o que tal tipo de pessoa diria ou faria, segundo o verossímil ou o necessário. É isso que faz a poesia 'mais filosófica e elevada'.","tip":"<strong>Como aplicar:</strong> busque o universal — é o que ressoa em todo espectador.","wide":True},
   {"ic":"key","t":"Impossível Verossímil > Possível Inverossímil","b":"A regra de ouro: prefira o <strong>impossível que o público aceita</strong> ao <strong>possível que ele não engole</strong>. Convicção vence veracidade — um milagre motivado convence; um fato real mal motivado, não.","tip":"<strong>Modelo mental:</strong> o critério não é 'isto aconteceu?', mas 'o público acredita que aconteceria?'."},
   {"ic":"spark","t":"Poeta é Fabricante de Mitos","b":"'O poeta deve ser mais <strong>fabricante de enredos</strong> que de versos' — é imitador de ações. Pôr história em verso continua sendo história; o que faz a poesia é a imitação sob a lei do verossímil.","tip":"<strong>Lição:</strong> a forma (verso, prosa, vídeo) é secundária; a ação verossímil é tudo."},
  ],
  "lessons_title":"Lições-Chave do Capítulo 4",
  "lessons":["Busque o universal: o que este tipo de pessoa faria.","Prefira o impossível verossímil ao possível inverossímil.","A obra se faz pela imitação de ação, não pela forma."]},

 {"slug":"ch05-peripecia-reconhecimento","sub":"CAPÍTULO 5: Peripécia e Reconhecimento",
  "intro":"O enredo complexo — superior ao simples — move a mudança de fortuna por peripécia (reviravolta), reconhecimento (descoberta) ou ambos, sempre conforme o verossímil.",
  "cards":[
   {"ic":"pivot","t":"Peripécia","b":"A <strong>mudança da ação no sentido contrário ao esperado</strong> — segundo a verossimilhança e a necessidade. A virada não é aleatória: é o resultado lógico que inverte a expectativa.","tip":"<strong>Como aplicar:</strong> surpreenda, mas conforme o verossímil — o público, olhando para trás, vê que era inevitável."},
   {"ic":"lens","t":"Reconhecimento (Anagnórisis)","b":"A <strong>passagem da ignorância ao conhecimento</strong>. O mais belo nasce da própria ação; inferiores são os por sinais, objetos, cicatrizes. O ápice: <strong>peripécia + reconhecimento juntos</strong> (Édipo).","tip":"<strong>Regra:</strong> a descoberta deve brotar do enredo, nunca de um adereço conveniente.","wide":True},
   {"ic":"spark","t":"Édipo: os Dois Golpes Juntos","b":"O mensageiro vem alegrar Édipo, mas ao revelar quem ele é produz o contrário: a <strong>peripécia</strong> (boa notícia vira catástrofe) coincide com o <strong>reconhecimento</strong> (Édipo descobre sua identidade). O paradigma do enredo complexo.","tip":"<strong>Modelo mental:</strong> os dois golpes nascendo da mesma ação = ápice do efeito trágico."},
  ],
  "lessons_title":"Lições-Chave do Capítulo 5",
  "lessons":["Prefira o enredo complexo: peripécia e/ou reconhecimento.","A descoberta nasce da ação, não de objetos externos.","A reviravolta surpreende, mas obedece ao verossímil."]},

 {"slug":"ch06-hamartia-catarse","sub":"CAPÍTULO 6: Hamartia e Catarse",
  "intro":"O efeito trágico — compaixão, temor e catarse — exige um herói específico: nem virtuoso demais nem vil, mas semelhante a nós, caindo por um erro (hamartia), não por maldade.",
  "cards":[
   {"ic":"person","t":"O Herói do Meio","b":"Evite três figuras: o muito <strong>virtuoso</strong> arruinado (repugna), o <strong>mau</strong> que prospera (nada de trágico), o <strong>perverso</strong> que cai (justo, mas sem compaixão). Resta o <strong>intermediário</strong>: bom, semelhante a nós, que erra.","tip":"<strong>Como aplicar:</strong> o herói cai por <strong>hamartia</strong> (erro de juízo), não por vício — é o que comove.","wide":True},
   {"ic":"scale","t":"Compaixão + Temor","b":"<strong>Eleos</strong> (compaixão) nasce do infortúnio imerecido de um semelhante; <strong>phobos</strong> (temor) nasce porque o que cai é como nós — <em>poderia ser conosco</em>. Sem semelhança, não há emoção trágica.","tip":"<strong>Modelo mental:</strong> só nos comovemos com quem reconhecemos como um de nós."},
   {"ic":"mask","t":"Cuidado com o Final Moralista","b":"O <strong>final duplo</strong> (bons premiados, maus punidos) agrada à plateia fraca, mas é próprio da <strong>comédia</strong> — mata a emoção trágica. A justiça poética perfeita esteriliza.","tip":"<strong>Sinal de alerta:</strong> se tudo se resolve com justiça impecável, você saiu da tragédia.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 6",
  "lessons":["O alvo é eleos + phobos → catarse.","Use o herói do meio: cai por erro, não por maldade.","Evite o final moralista duplo."]},

 {"slug":"ch07-antipadroes","sub":"CAPÍTULO 7: Anti-padrões e Soluções",
  "intro":"Aristóteles cataloga os erros que arruínam a tragédia — sobretudo o deus ex machina, o episódico e a aposta no espetáculo. Bons enredos resolvem-se de dentro.",
  "cards":[
   {"ic":"wrench","t":"Nada de Deus ex Machina","b":"'É preciso que o desenlace surja <strong>do próprio enredo</strong>, e não, como na Medeia, de um deus.' A máquina serve só para o que está <strong>fora</strong> da ação (o antes inacessível, o depois profetizado), nunca para desatar o nó.","tip":"<strong>Regra:</strong> a solução está plantada no problema; recorrer a um deus confessa que a estrutura não se sustenta.","warn":True,"wide":True},
   {"ic":"gap","t":"O Irracional fica Fora","b":"Se houver algo <strong>inverossímil/irracional</strong>, que esteja fora da ação representada — não dentro dela. Aristóteles tolera o irracional na Odisseia porque fica fora da cena.","tip":"<strong>Como aplicar:</strong> exile o irracional inevitável para fora do palco."},
   {"ic":"eye","t":"Veja a Cena Diante dos Olhos","b":"Ao construir e ao redigir, o poeta deve <strong>encenar mentalmente a ação como espectador</strong> — isso flagra contradições invisíveis no papel e revela o gesto certo.","tip":"<strong>Hábito:</strong> visualize antes de escrever; é qualidade de graça."},
  ],
  "lessons_title":"Lições-Chave do Capítulo 7",
  "lessons":["O desenlace nasce da ação, nunca de intervenção externa.","Mantenha o irracional fora da cena representada.","Visualize a ação ao construir; não confie no espetáculo."]},
]
