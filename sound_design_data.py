# -*- coding: utf-8 -*-
"""Conteúdo (pt-BR) das páginas da biblioteca para 'Sound Design' de David
Sonnenschein. O uso EXPRESSIVO do som: processo, criatividade, acústica,
psicoacústica, música, voz, efeitos e o mapa emocional."""

BOOK = {
 "title": "Sound Design",
 "author": "David Sonnenschein",
 "header_light": "SOUND",
 "header_bold": "DESIGN",
 "subtitle": "VISÃO GERAL · O PODER EXPRESSIVO DO SOM NO CINEMA",
 "intro": "Sonnenschein trata a trilha sonora — voz, música e efeitos — como uma camada de contar história tão poderosa quanto a imagem, e quase sempre subutilizada. O som percorre uma cadeia (vibração → sensação → percepção → emoção), e o ofício é desenhá-la de ponta a ponta: traçar a curva emocional da história e pintá-la com tom, ritmo, intensidade, timbre, espaço e silêncio.",
 "description": "O guia prático e expressivo do sound design por David Sonnenschein: o processo (do roteiro à mixagem), a criação de sons, a acústica e a psicoacústica, música, voz, efeitos e o mapa emocional que faz o som dirigir o que o público sente.",
 "tags": ["Som", "Cinema", "Ofício"],
 "progress": "8 Capítulos Completos",
 "cover": "assets/sound-design-cover.png",
 "overview_cards": [
   {"ic":"layers","t":"As 3 Famílias do Som","b":"Todo áudio se divide em <strong>voz</strong> (o rei — vococentrismo), <strong>música</strong> (que comenta, não ilustra) e <strong>efeitos</strong> (que constroem o mundo). Orquestrar as três sem que briguem é o ofício.","tip":"<strong>Como aplicar:</strong> em cada instante, um elemento manda (em geral a voz); os outros recuam.","wide":True},
   {"ic":"spiral","t":"Da Vibração à Emoção","b":"O som é uma cadeia: <strong>vibração</strong> (física) → <strong>sensação</strong> (ouvido) → <strong>percepção</strong> (cérebro) → <strong>emoção</strong>. Projetar som é desenhar essa cadeia inteira.","tip":"<strong>Modelo mental:</strong> você mixa para o cérebro, não para o medidor."},
   {"ic":"clock","t":"O Mapa Emocional","b":"Trace a curva de emoção da história e faça o som <strong>segui-la</strong> — usando tom, ritmo, intensidade e silêncio como tinta. O som não ilustra a cena: diz ao público o que sentir.","tip":"<strong>Chave:</strong> o clímax muitas vezes É o silêncio."},
 ],
}

CHAPTERS = [
 {"slug":"ch01-processo-sound-design","sub":"CAPÍTULO 1: O Processo do Sound Design",
  "intro":"Sound design não é colar efeitos no fim — é um processo que começa na leitura do roteiro. O som planejado conta história; o improvisado tapa buraco.",
  "cards":[
   {"ic":"eye","t":"Spotting (a leitura sonora)","b":"Percorrer o roteiro perguntando, cena a cena — <strong>o que se ouve aqui, e o que esse som deve fazer pela história?</strong> Mapear voz, música, efeito e silêncio.","tip":"<strong>Como aplicar:</strong> spotting é o storyboard do ouvido.","wide":True},
   {"ic":"target","t":"Intenção por som","b":"Todo som deve responder <strong>por que está aqui?</strong> Som sem função é ruído que rouba a atenção que a história precisa.","tip":"<strong>Modelo mental:</strong> antes de criar, defina a paleta — o vocabulário sonoro do projeto."},
   {"ic":"gap","t":"\"Resolvemos na pós\"","b":"Tratar o áudio como etapa cosmética final <strong>perde oportunidades narrativas</strong> e gera remendos caros.","tip":"<strong>Cuidado:</strong> o som se decide no papel, não na mesa de mixagem.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 1",
  "lessons":["Sound design começa no roteiro (spotting), não na mixagem.","Defina a paleta antes de criar; cada som precisa de intenção.","Mixagem é hierarquia: decidir quem manda em cada instante."]},

 {"slug":"ch02-criatividade-sons","sub":"CAPÍTULO 2: Criatividade e a Invenção de Sons",
  "intro":"O som mais forte raramente é a gravação realista do objeto — é o som inventado que diz o que a cena sente.",
  "cards":[
   {"ic":"spark","t":"Metáfora sonora","b":"Representar uma ideia por um som que <strong>evoca a sensação certa</strong>, não o real (um soco = galho quebrando + sub-grave = dor e peso que o soco real não tem).","tip":"<strong>Como aplicar:</strong> projete a sensação, não a fidelidade ao objeto.","wide":True},
   {"ic":"layers","t":"Camadas","b":"O som final costuma ser uma <strong>mistura</strong> de fontes inesperadas (rugido + tigre + voz humana abafada) — a camada é o que dá assinatura e emoção.","tip":"<strong>Modelo mental:</strong> o som é uma mentira útil — honesta com a emoção."},
   {"ic":"gap","t":"Biblioteca preguiçosa","b":"Pegar o efeito genérico de prateleira para tudo faz o filme <strong>soar como todos os outros</strong>.","tip":"<strong>Cuidado:</strong> literalidade mata a metáfora; um som original vira identidade.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 2",
  "lessons":["Projete a sensação, não a fidelidade ao objeto (metáfora sonora).","O som forte costuma ser camadas de fontes inesperadas.","Um som original e reconhecível vira assinatura do filme."]},

 {"slug":"ch03-vibracao-sensacao","sub":"CAPÍTULO 3: Da Vibração à Sensação",
  "intro":"Antes de emocionar, o som é física. Frequência, intensidade, duração, ritmo e espaço são as alavancas que o designer manipula.",
  "cards":[
   {"ic":"scale","t":"As alavancas físicas","b":"<strong>Grave</strong> = peso, ameaça, intimidade; <strong>agudo</strong> = tensão, alerta. <strong>Intensidade</strong> (contraste) = urgência; <strong>ritmo</strong> = energia; <strong>reverberação</strong> = tamanho do mundo.","tip":"<strong>Como aplicar:</strong> cada propriedade é um botão emocional.","wide":True},
   {"ic":"pivot","t":"O contraste é tudo","b":"Nenhuma propriedade significa em absoluto — significa <strong>em relação</strong>. O grave só pesa depois do agudo; o alto só impacta depois do silêncio.","tip":"<strong>Modelo mental:</strong> o subsônico cria tensão corporal que ninguém percebe."},
   {"ic":"gap","t":"Tudo no mesmo nível","b":"Sem contraste de intensidade/frequência, o ouvido <strong>satura</strong> e nada se destaca.","tip":"<strong>Cuidado:</strong> reverberação que contradiz a cena quebra a imersão.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 3",
  "lessons":["Frequência, intensidade, ritmo e espaço são as alavancas da emoção.","Graves pesam; agudos tensionam; o contraste é o que significa.","O subsônico cria tensão corporal que o público sente sem perceber."]},

 {"slug":"ch04-sensacao-percepcao","sub":"CAPÍTULO 4: Da Sensação à Percepção",
  "intro":"O ouvido capta vibração; o cérebro decide o que significa. Projetar som é projetar para esse cérebro.",
  "cards":[
   {"ic":"lens","t":"Figura e fundo","b":"O cérebro separa o som <strong>principal</strong> (figura) do leito (fundo) e só processa <strong>um fluxo consciente por vez</strong> — em geral a voz. A hierarquia respeita esse limite.","tip":"<strong>Como aplicar:</strong> se dois sons disputam o principal, o público perde os dois.","wide":True},
   {"ic":"wave","t":"Mascaramento","b":"Um som forte <strong>esconde</strong> um fraco próximo em frequência. Use a favor (esconder um corte) ou evite contra (a voz some sob a trilha).","tip":"<strong>Modelo mental:</strong> metade da emoção mora abaixo do consciente."},
   {"ic":"gap","t":"Trilha que mascara a voz","b":"Competir na mesma faixa de frequência da fala = <strong>inteligibilidade perdida</strong> (o defeito nº 1).","tip":"<strong>Cuidado:</strong> saturar a atenção cansa e o público desliga.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 4",
  "lessons":["O cérebro filtra: mascaramento, figura/fundo, atenção seletiva.","Só um fluxo consciente por vez — proteja a figura (a voz).","Metade da emoção mora abaixo do consciente (subsônico, ambiência)."]},

 {"slug":"ch05-musica","sub":"CAPÍTULO 5: A Música",
  "intro":"A música é o atalho mais direto para a emoção — e o mais perigoso, porque vira muleta. É linguagem com gramática própria.",
  "cards":[
   {"ic":"spark","t":"As alavancas musicais","b":"<strong>Melodia</strong> (a linha que se lembra), <strong>harmonia</strong> (maior = alegria; menor = tensão; dissonância = desconforto), <strong>ritmo</strong> (energia), <strong>timbre</strong> (a cor emocional).","tip":"<strong>Como aplicar:</strong> música comenta, não ilustra.","wide":True},
   {"ic":"link","t":"Leitmotiv","b":"Um tema associado a um personagem ou ideia, que <strong>retorna transformado</strong> conforme a história muda. Constrói significado por repetição e variação.","tip":"<strong>Modelo mental:</strong> o público sente o personagem chegar antes de vê-lo."},
   {"ic":"gap","t":"Mickey-mousing","b":"A música sublinhar <strong>cada gesto literalmente</strong> infantiliza e cansa. Trilha onipresente anula o próprio poder.","tip":"<strong>Cuidado:</strong> música não salva cena ruim — o problema é a cena.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 5",
  "lessons":["Melodia, harmonia, ritmo e timbre são alavancas emocionais precisas.","O leitmotiv constrói significado por repetição e variação.","Música comenta (não ilustra) e só impacta com silêncio para contrastar."]},

 {"slug":"ch06-voz-humana","sub":"CAPÍTULO 6: A Voz Humana",
  "intro":"De todos os sons, a voz é a que o cérebro prioriza acima de tudo. Ela é veículo de palavras (o quê) e instrumento expressivo (o como).",
  "cards":[
   {"ic":"key","t":"As camadas da voz","b":"<strong>Conteúdo</strong> (palavras) + <strong>prosódia</strong> (entonação, ritmo, ênfase, pausa) + <strong>grão</strong> (a textura física). A mesma frase muda de sentido pela prosódia.","tip":"<strong>Como aplicar:</strong> pontuação é direção de ator — onde a vírgula cai, a emoção acontece.","wide":True},
   {"ic":"target","t":"Vococentrismo","b":"Na presença de voz, o público a escuta <strong>primeiro</strong>; tudo o mais vira fundo. A mixagem protege a inteligibilidade absoluta.","tip":"<strong>Modelo mental:</strong> a voz é o rei da mixagem; nada disputa com ela."},
   {"ic":"gap","t":"Texto certo, tom errado","b":"O público acredita no <strong>tom antes do conteúdo</strong>; uma fala certa dita com tom errado mente. Leitura plana desliga o ouvinte.","tip":"<strong>Cuidado:</strong> voz coberta por trilha/efeito é o pecado capital do áudio.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 6",
  "lessons":["A voz é conteúdo + prosódia + grão — e a prosódia define o sentido.","Vococentrismo: protege-se a inteligibilidade da voz acima de tudo.","Pontuação e pausa são direção de ator — onde a emoção mora."]},

 {"slug":"ch07-efeitos-paisagem","sub":"CAPÍTULO 7: Efeitos e Paisagem Sonora",
  "intro":"Os efeitos constroem o mundo: dizem onde estamos, o que é real, o que ameaça. A paisagem sonora é um personagem invisível.",
  "cards":[
   {"ic":"layers","t":"As camadas do efeito","b":"<strong>Foley</strong> (passos, roupas — presença física), <strong>hard effects</strong> (porta, tiro), <strong>ambiência/room tone</strong> (o leito do lugar) e <strong>sound design</strong> (os sons inventados).","tip":"<strong>Como aplicar:</strong> sem foley, atores parecem fantasmas.","wide":True},
   {"ic":"lens","t":"Hiper-realismo seletivo","b":"Na vida tudo soa; no cinema, <strong>escolhe-se</strong> o que se ouve. Exagerar UM som (a gota, o relógio) e apagar o resto dirige a atenção.","tip":"<strong>Modelo mental:</strong> a emoção mora no foco, não na soma de tudo."},
   {"ic":"gap","t":"Realismo indiscriminado","b":"Pôr todo som que existiria vira <strong>lama sonora sem foco</strong>; ambiência genérica não dá alma a nenhum lugar.","tip":"<strong>Cuidado:</strong> no cinema o silêncio é uma escolha e o som é curadoria.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 7",
  "lessons":["Foley (presença), hard effects, ambiência (lugar) e sound design (o irreal) são as camadas.","A paisagem sonora é um personagem: define espaço, tempo e clima.","Hiper-realismo seletivo: exagere um som, apague o resto."]},

 {"slug":"ch08-som-imagem-emocao","sub":"CAPÍTULO 8: Som, Imagem e o Mapa Emocional",
  "intro":"O som não acompanha a imagem — funde-se a ela e muda o que ela significa. O método final: traçar a curva emocional e pintá-la.",
  "cards":[
   {"ic":"clock","t":"O mapa emocional","b":"Desenhe a linha de emoção pretendida (calma → tensão → clímax → alívio) e atribua a cada trecho as <strong>alavancas sonoras</strong> que a sustentam.","tip":"<strong>Como aplicar:</strong> projete a curva, depois pinte-a — senão o filme não respira.","wide":True},
   {"ic":"pivot","t":"Empático × anempático","b":"Som <strong>empático</strong> acompanha a emoção; som <strong>anempático</strong> (indiferente — uma valsa alegre numa tragédia) <strong>amplifica</strong> o horror.","tip":"<strong>Modelo mental:</strong> a imagem mostra; o som diz o que sentir. Eles se multiplicam."},
   {"ic":"key","t":"O silêncio como clímax","b":"O ponto mais alto da curva muitas vezes é a <strong>ausência total de som</strong> — o vazio que o público preenche com a própria emoção.","tip":"<strong>Cuidado:</strong> curva plana (mesma densidade o tempo todo) não deixa sentir subidas nem quedas.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 8",
  "lessons":["Trace a curva emocional e pinte-a com tom, ritmo, intensidade, densidade e silêncio.","Empático acompanha; anempático contraria — e a indiferença amplifica.","O clímax muitas vezes é o silêncio; densidade e corte são dramaturgia."]},
]
