# -*- coding: utf-8 -*-
"""Conteúdo (pt-BR) de 'O Mundo de Sofia' (Jostein Gaarder)."""

BOOK = {
  "title": "O Mundo de Sofia",
  "author": "Jostein Gaarder",
  "header_light": "O MUNDO",
  "header_bold": "DE SOFIA",
  "subtitle": "VISÃO GERAL · HISTÓRIA DA FILOSOFIA EM FORMA DE ROMANCE",
  "intro": "Sofia Amundsen, 14 anos, começa a receber cartas misteriosas com duas perguntas: 'Quem é você?' e 'De onde vem o mundo?' O remetente é Alberto Knox, um filósofo que a conduz por toda a história da filosofia ocidental — dos pré-socráticos a Sartre. No caminho, descobrem que são personagens de um livro.",
  "description": "Romance filosófico de Jostein Gaarder que percorre a história da filosofia ocidental: dos pré-socráticos e o espanto originário, passando por Sócrates/Platão/Aristóteles, helenismo, Descartes, empiristas, Kant, Hegel, Marx/Darwin/Freud e Sartre, até a virada meta onde os personagens descobrem que são fictícios.",
  "tags": ["Filosofia", "História", "Educação"],
  "progress": "9 Capítulos",
  "cover": "assets/mundo-de-sofia-cover.png",
  "overview_cards": [
    {"ic":"eye","t":"O Espanto como Ponto de Partida","b":"Filosofar nasce de recusar que o mundo seja óbvio. A criança se espanta; o adulto acostuma-se — vai deslizando para o conforto do pelo do coelho, longe do mágico. <strong>Um bom filósofo nunca perde a capacidade de se admirar.</strong>","tip":"<strong>Como aplicar:</strong> use o espanto como teste — se algo deixou de parecer estranho (a consciência, o tempo, o próprio existir), você parou de filosofar sobre isso."},
    {"ic":"layers","t":"Os Grandes Eixos","b":"Dois eixos estruturam toda a história: <strong>sentidos × razão</strong> (Heráclito × Parmênides, empirismo × racionalismo) e <strong>forma nas Ideias × forma nas coisas</strong> (Platão × Aristóteles). Toda filosofia posterior escolhe um lado — ou sintetiza (Kant).","tip":"<strong>Modelo mental:</strong> ao encontrar qualquer posição filosófica, pergunte — de onde vem o conhecimento (sentido ou razão) e onde está a realidade (Ideias ou coisas)?","wide":True},
    {"ic":"constellation","t":"A Virada Meta","b":"O golpe genial de Gaarder: o curso de filosofia está dentro de uma ficção que pergunta exatamente o que a filosofia pergunta. Sofia e Alberto descobrem que são <strong>personagens de um livro</strong> — e a pergunta 'Quem é você?' torna-se vertiginosa: em que modo qualquer um de nós existe?","tip":"<strong>Modelo mental:</strong> a pergunta inicial retorna no nível mais radical — a própria realidade do sujeito é posta em xeque."},
  ],
}

CHAPTERS = [
  {
    "slug": "ch01-espanto-e-a-moldura",
    "sub": "CAPÍTULO 1: O Espanto e a Moldura",
    "intro": "A filosofia começa com duas perguntas que a maioria não faz porque já se acostumou às respostas: 'Quem é você?' e 'De onde vem o mundo?' Sofia tira um envelope do correio e percebe que não sabe responder de verdade.",
    "cards": [
      {"ic":"eye","t":"O Coelho na Cartola","b":"O universo é o coelho que o mágico tira da cartola. Nós nascemos na <strong>ponta dos pelos finos</strong> (a criança que acha tudo estranho) e vamos deslizando para o conforto do pelo, deixando de ver o truque. Filósofos são os que tentam subir pelos pelos para espiar o mágico nos olhos.","tip":"<strong>Como aplicar:</strong> pense no adulto como alguém que 'afundou no pelo do coelho' — filosofar é voltar a ser criança intelectualmente, sem perder o rigor."},
      {"ic":"bulb","t":"Perguntas Valem Mais que Respostas","b":"Filosofia não é acumular respostas prontas: é a arte de fazer as perguntas e de <strong>não se conformar</strong>. O espanto não é ingenuidade — é o ponto de partida de um pensamento que depois se torna disciplinado.","tip":"<strong>Modelo mental:</strong> use o espanto como teste — se algo deixou de parecer estranho (a consciência, o tempo, o existir), você parou de filosofar sobre isso."},
      {"ic":"bubble","t":"Mito × Razão","b":"A filosofia surge quando se troca a explicação mítica (os deuses fazem chover) pela explicação <strong>natural e racional</strong>. Não é o fim do encantamento — é a recusa de tomar o mundo como óbvio mesmo sem deuses.","tip":"<strong>Como aplicar:</strong> toda vez que você aceita uma explicação 'porque sempre foi assim', está do lado do mito; filosofar é pedir a justificativa."},
    ],
    "lessons_title": "Lições-Chave do Capítulo 1",
    "lessons": ["Filosofar começa antes de qualquer doutrina: começa em recusar que o mundo seja óbvio.", "As perguntas certas valem mais que respostas tranquilizadoras.", "A criança é a filósofa natural; o desafio é manter o espanto na vida adulta."],
  },
  {
    "slug": "ch02-pre-socraticos",
    "sub": "CAPÍTULO 2: Os Pré-socráticos — do Mito ao Logos",
    "intro": "A filosofia ocidental começa quando os gregos da Jônia trocam a explicação mítica por uma racional: de que substância primordial (physis) tudo é feito? O conflito fundador sentidos × razão estrutura tudo o que vem depois.",
    "cards": [
      {"ic":"wave","t":"Tudo Flui × Nada Muda","b":"<strong>Heráclito</strong>: 'panta rhei' — tudo flui, ninguém entra duas vezes no mesmo rio; o logos é a unidade dos opostos. <strong>Parmênides</strong>: o ser é imutável, a mudança é ilusão dos sentidos — só a razão revela o real. O primeiro grande eixo da filosofia.","tip":"<strong>Modelo mental:</strong> Heráclito × Parmênides = confie nos sentidos × confie só na razão. Toda a história posterior oscila entre esses polos."},
      {"ic":"layers","t":"A Busca pela Physis","b":"Tales (água), Anaximandro (o indefinido/ápeiron), Anaxímenes (ar): a ousadia de buscar <strong>um princípio natural unificador</strong> para tudo. Não é adivinhação: é o gesto de explicar o complexo por algo interno à natureza, sem recorrer aos deuses.","tip":"<strong>Como aplicar:</strong> pense em Tales não pelo resultado (água) mas pelo método — uma única pergunta racional para explicar tudo."},
      {"ic":"link","t":"Demócrito e os Átomos","b":"Partículas eternas e indivisíveis (<strong>átomos</strong>) que, combinadas em diferentes arranjos, formam tudo. O primeiro materialismo completo — e o avô do método científico. A ideia de que o complexo se explica por partes simples e mecânicas, sem propósito divino.","tip":"<strong>Modelo mental:</strong> o materialismo de Demócrito é tão antigo quanto a filosofia — a ciência moderna é sua descendente direta."},
    ],
    "lessons_title": "Lições-Chave do Capítulo 2",
    "lessons": ["Filosofia = procurar explicações dentro da natureza, não acima dela.", "O conflito sentidos × razão (Heráclito × Parmênides) estrutura tudo que vem depois.", "A ideia de átomo mostra que o materialismo é tão antigo quanto a filosofia."],
  },
  {
    "slug": "ch03-socrates-platao-aristoteles",
    "sub": "CAPÍTULO 3: Sócrates, Platão e Aristóteles",
    "intro": "O tripé clássico de Atenas: Sócrates inventa o diálogo maiêutico, Platão funda o idealismo (o real são as Ideias eternas), e Aristóteles traz a filosofia 'de volta à terra' com o empirismo e a lógica.",
    "cards": [
      {"ic":"bubble","t":"A Maiêutica Socrática","b":"Sócrates 'parte ideias' pelo diálogo: ele não ensina, faz pensar. 'Só sei que nada sei' — a consciência da própria ignorância é o ponto de partida do conhecimento. <strong>Conhecimento = virtude</strong>; a ignorância é a raiz do mal.","tip":"<strong>Como aplicar:</strong> faça perguntas em vez de dar respostas — a maiêutica revela o que o interlocutor já sabe mas não sabia que sabia."},
      {"ic":"mountain","t":"O Mundo das Ideias","b":"As <strong>Formas</strong> eternas e perfeitas (o Cavalo em si, o Belo em si) existem num mundo à parte; o mundo sensível é cópia imperfeita. A <strong>alegoria da caverna</strong>: prisioneiros tomam sombras por realidade — o filósofo se liberta, vê a luz e volta para libertar os outros.","tip":"<strong>Modelo mental:</strong> use a caverna para qualquer crítica de ilusão — o que tomamos por real pode ser sombra de algo mais verdadeiro."},
      {"ic":"lens","t":"Aristóteles — A Forma nas Coisas","b":"Aristóteles 'traz Platão de volta à terra': a forma está <strong>nas coisas</strong>, não num céu à parte. O conhecimento começa pelos sentidos; a lógica e as quatro causas explicam qualquer fenômeno. A virtude é o <strong>justo meio</strong> entre excessos.","tip":"<strong>Sinal de alerta:</strong> Platão × Aristóteles = o segundo grande eixo — toda a filosofia medieval e moderna escolhe um lado ou tenta síntese."},
    ],
    "lessons_title": "Lições-Chave do Capítulo 3",
    "lessons": ["Sócrates: a verdade nasce do diálogo e da consciência da própria ignorância.", "Platão: existe uma realidade perfeita e racional por trás das aparências.", "Aristóteles: conhecer começa pelos sentidos e pela observação ordenada do mundo."],
  },
  {
    "slug": "ch04-helenismo-e-idade-media",
    "sub": "CAPÍTULO 4: Helenismo e Idade Média",
    "intro": "Depois de Aristóteles, a filosofia vira arte de viver: estoicismo, epicurismo, cinismo, ceticismo. Na Idade Média, ela se funde ao cristianismo — Agostinho cristianiza Platão, Tomás de Aquino cristianiza Aristóteles.",
    "cards": [
      {"ic":"leaf","t":"Filosofia como Arte de Viver","b":"<strong>Estoicos</strong>: viver conforme a razão; aceitar o destino com serenidade. <strong>Epicuristas</strong>: o maior prazer é a ausência de dor (ataraxia) — não a devassidão. <strong>Cínicos</strong>: felicidade na independência dos bens materiais. Helenismo = filosofia-terapia.","tip":"<strong>Como aplicar:</strong> o estoico Epicteto, escravo, distinguia o que depende de nós (o juízo) do que não depende — e só cobrava a si o primeiro."},
      {"ic":"scale","t":"Agostinho × Tomás — Fé e Razão","b":"<strong>Agostinho</strong> (Platão batizado): as Ideias estão na mente de Deus; a fé busca o entendimento. <strong>Tomás de Aquino</strong> (Aristóteles batizado): razão e fé não se contradizem; a razão pode chegar a Deus pelo mundo. Dois modos de conciliar o mesmo eixo.","tip":"<strong>Modelo mental:</strong> a Idade Média não foi 'buraco negro' — foi a ponte que preservou e integrou a herança grega na cultura cristã."},
      {"ic":"spiral","t":"Neoplatonismo — A Emanação do Uno","b":"Plotino: tudo <strong>emana</strong> do Uno como a luz do sol — a matéria é a borda mais escura dessa emanação. O objetivo é retornar ao Uno pelo caminho interior. O misticismo filosófico que influenciará Agostinho e, mais tarde, o Romantismo.","tip":"<strong>Modelo mental:</strong> o neoplatonismo conecta Platão ao misticismo cristão — o Uno de Plotino será depois identificado com Deus."},
    ],
    "lessons_title": "Lições-Chave do Capítulo 4",
    "lessons": ["Filosofia também é técnica de viver bem em meio à incerteza.", "O cristianismo medieval absorve a filosofia grega, não a apaga.", "Fé e razão podem cooperar (Tomás) ou a fé pode primar (Agostinho) — debate que atravessa séculos."],
  },
  {
    "slug": "ch05-renascenca-descartes",
    "sub": "CAPÍTULO 5: Renascença e Descartes",
    "intro": "A Renascença recoloca o homem no centro com o humanismo e o método científico. Descartes inaugura a filosofia moderna: duvidando de tudo, chega à única certeza indubitável — 'penso, logo existo' — e funda o racionalismo.",
    "cards": [
      {"ic":"bulb","t":"A Dúvida Metódica","b":"Descartes decide duvidar de <strong>tudo o que pode ser posto em dúvida</strong> (sentidos, sonho, até a matemática), para encontrar o que resiste. Não é ceticismo: é uma <em>etapa</em> para chegar à certeza — derruba primeiro tudo que pode tremer e vê o que sobra de pé.","tip":"<strong>Como aplicar:</strong> use a dúvida metódica como ferramenta — para achar o que é sólido, derrube primeiro tudo o que pode tremer."},
      {"ic":"spark","t":"'Penso, Logo Existo'","b":"<em>Cogito, ergo sum</em>: mesmo enganado, há um eu que pensa; eis a primeira certeza indubitável. O <strong>ponto de Arquimedes da modernidade</strong> — a filosofia deixa de partir do cosmos e passa a partir do sujeito consciente.","tip":"<strong>Modelo mental:</strong> o cogito é uma virada copernicana — não o mundo me define, sou eu que, ao pensar, certifico que existo."},
      {"ic":"gap","t":"O Problema do Dualismo","b":"Descartes separa duas substâncias: <strong>res cogitans</strong> (pensamento, alma) e <strong>res extensa</strong> (matéria, extensão). Corpo e mente são realidades distintas. Abre o problema filosófico que ocupará toda a modernidade: como e onde interagem?","tip":"<strong>Sinal de alerta:</strong> Descartes ainda precisa de Deus para reconstruir a confiança na realidade externa — o cogito prova que existe, não que o mundo externo é real.","warn":True},
    ],
    "lessons_title": "Lições-Chave do Capítulo 5",
    "lessons": ["A Renascença liberta a investigação da tutela exclusiva da fé e funda a ciência moderna.", "Descartes torna a consciência o ponto de partida seguro da filosofia.", "O dualismo mente/corpo abre um problema que ocupará toda a filosofia seguinte."],
  },
  {
    "slug": "ch06-spinoza-empiristas",
    "sub": "CAPÍTULO 6: Spinoza e os Empiristas",
    "intro": "Contra as ideias inatas de Descartes, os empiristas britânicos: todo conhecimento vem da experiência. Hume dissolve o eu e a causalidade — e 'desperta Kant do sono dogmático'. Spinoza, por sua vez, funde Deus e Natureza.",
    "cards": [
      {"ic":"leaf","t":"Deus sive Natura","b":"Spinoza: 'Deus, ou seja, a Natureza' — uma só substância infinita; tudo é modo dela. Ver as coisas <em>sub specie aeternitatis</em> (do ponto de vista da eternidade). <strong>Panteísmo</strong> que recusa o dualismo cartesiano: não há dois mundos, só um.","tip":"<strong>Modelo mental:</strong> para Spinoza, estudar a natureza é estudar Deus — não há separação entre criador e criatura."},
      {"ic":"eye","t":"A Tabula Rasa e o Esse Est Percipi","b":"<strong>Locke</strong>: a mente nasce folha em branco, a experiência escreve nela. <strong>Berkeley</strong>: 'existir é ser percebido' — só existem espíritos e suas ideias; a matéria como tal não existe fora da percepção. Semente filosófica da virada meta do livro.","tip":"<strong>Como aplicar:</strong> o 'esse est percipi' de Berkeley antecipa a ideia de Sofia existir por ser pensada/escrita pelo major Knag."},
      {"ic":"lens","t":"Hume Dissolve a Causalidade","b":"Não vemos causas — vemos <strong>sucessão de eventos que vira hábito</strong> de esperar B depois de A. Não há 'eu' substancial: só um feixe de percepções. O ceticismo radical de Hume 'acorda Kant do sono dogmático' e força a grande síntese.","tip":"<strong>Sinal de alerta:</strong> antes de afirmar uma conexão necessária, pergunte com Hume — eu a observo ou apenas me acostumei a esperá-la?","warn":True},
    ],
    "lessons_title": "Lições-Chave do Capítulo 6",
    "lessons": ["O conhecimento pode estar todo enraizado na experiência sensível (empirismo).", "Hume dissolve o eu e a causalidade — deixando à razão apenas o hábito.", "Berkeley: 'existir é ser percebido' — semente filosófica da virada meta do livro."],
  },
  {
    "slug": "ch07-kant",
    "sub": "CAPÍTULO 7: Kant — a Grande Síntese",
    "intro": "Kant reconcilia empiristas e racionalistas: o conhecimento tem matéria que vem de fora (sentidos) e forma que vem de nós (estruturas a priori). Nunca conhecemos a coisa-em-si — só o mundo tal como nosso aparato o organiza.",
    "cards": [
      {"ic":"lens","t":"Os Óculos da Mente","b":"<strong>Espaço, tempo e causalidade</strong> são formas a priori da mente — 'óculos' que toda mente humana usa. Não estão 'lá fora' nas coisas: são as lentes pelas quais tudo é percebido. Por isso a ciência é possível (todos usam os mesmos óculos) mas limitada ao fenômeno.","tip":"<strong>Modelo mental:</strong> se você usasse óculos vermelhos colados, veria tudo vermelho e nunca saberia a cor real — espaço, tempo e causa são esses óculos."},
      {"ic":"gap","t":"Fenômeno × Coisa-em-Si","b":"Conhecemos o mundo como ele <strong>nos aparece</strong> (fenômeno), nunca como ele é em si mesmo (Ding an sich — inacessível). Kant não diz que o mundo é ilusão; diz que só temos acesso a ele filtrado pelas nossas estruturas mentais.","tip":"<strong>Sinal de alerta:</strong> a causalidade não é negada como em Hume — ela é garantida, mas como forma do nosso entendimento, não propriedade das coisas em si.","warn":True},
      {"ic":"scale","t":"O Imperativo Categórico","b":"Lei moral interior: '<strong>age só segundo a máxima que possas querer que se torne lei universal</strong>' e 'trata a humanidade sempre como fim, nunca apenas como meio'. A moralidade nasce de dentro, da razão autônoma — não de recompensa nem medo.","tip":"<strong>Como aplicar:</strong> use como teste moral — universalize sua ação ('e se todos fizessem isso?'); se ela se autodestrói ao virar regra geral, é imoral."},
    ],
    "lessons_title": "Lições-Chave do Capítulo 7",
    "lessons": ["Empirismo e racionalismo estavam ambos pela metade — o conhecimento exige experiência e estruturas mentais.", "Há um limite intransponível: a coisa-em-si fica fora do alcance da razão.", "A moralidade nasce de dentro, da razão prática autônoma."],
  },
  {
    "slug": "ch08-hegel-kierkegaard-marx-freud",
    "sub": "CAPÍTULO 8: Hegel, Kierkegaard e os Mestres da Suspeita",
    "intro": "O século XIX: Hegel faz a verdade histórica e processual (dialética); Kierkegaard reage em nome do indivíduo concreto; Marx, Darwin e Freud destronam a velha imagem do homem com três golpes devastadores.",
    "cards": [
      {"ic":"spiral","t":"A Dialética de Hegel","b":"A verdade é <strong>histórica e processual</strong>: tese → antítese → síntese, em ciclo contínuo. O Espírito (Geist) se desdobra na história. Use a dialética para ler conflitos: raramente um lado está totalmente certo — o avanço costuma ser a síntese que conserva o melhor de cada polo.","tip":"<strong>Como aplicar:</strong> diante de um impasse, pergunte — qual seria a síntese que conserva o melhor da tese e da antítese?"},
      {"ic":"person","t":"Kierkegaard — O Indivíduo Concreto","b":"Contra o sistema abstrato de Hegel: importa o <strong>singular que existe, escolhe e sofre</strong>. 'A verdade é subjetividade.' Os três estágios: estético (prazer/instante) → ético (dever, responsabilidade) → religioso (fé, salto). Pai do existencialismo.","tip":"<strong>Modelo mental:</strong> Kierkegaard como antídoto ao excesso de sistema — 'e o indivíduo concreto, que precisa escolher e viver, onde fica?'"},
      {"ic":"triangle","t":"Os Três Mestres da Suspeita","b":"<strong>Marx</strong>: a base econômica determina as ideias (materialismo histórico). <strong>Darwin</strong>: o homem evoluiu, não foi criado. <strong>Freud</strong>: não somos senhores em nossa própria casa (o inconsciente governa). Os três descentram o homem — e tornam mais urgente a pergunta existencialista pela liberdade.","tip":"<strong>Como aplicar:</strong> use a suspeita como método — por trás de uma ideia 'neutra', pergunte a quem serve (Marx), que herança biológica a condiciona (Darwin), que desejo recalcado a move (Freud)."},
    ],
    "lessons_title": "Lições-Chave do Capítulo 8",
    "lessons": ["Hegel: a verdade se realiza na história, por contradições que se superam.", "Kierkegaard: contra todo sistema, o que importa é o indivíduo que existe e decide.", "Marx/Darwin/Freud: três golpes na velha imagem de um homem soberano e consciente."],
  },
  {
    "slug": "ch09-sartre-virada-meta",
    "sub": "CAPÍTULO 9: Sartre, a Virada Meta e o Cosmos",
    "intro": "O fecho filosófico: Sartre — 'a existência precede a essência, estamos condenados a ser livres'. E a genialidade de Gaarder: Sofia descobre que é personagem de um livro. A pergunta 'Quem é você?' retorna no nível mais radical.",
    "cards": [
      {"ic":"key","t":"'Condenados a ser Livres'","b":"Não há natureza humana dada de antemão: primeiro existimos, depois nos definimos pelas <strong>escolhas</strong>. A liberdade é inescapável — até não escolher é uma escolha. Daí a angústia: somos totalmente responsáveis por quem nos tornamos.","tip":"<strong>Sinal de alerta:</strong> 'má-fé' é autoengano — quando diz 'não tive escolha' ou 'é só o meu trabalho', está fugindo de assumir a própria liberdade.","warn":True},
      {"ic":"constellation","t":"A Virada Meta","b":"Sofia e Alberto descobrem que são <strong>personagens de um livro</strong> que o major Knag escreve para a filha Hilde. Realiza o 'esse est percipi' de Berkeley (existir é ser percebido/escrito) e o existencialismo de Sartre (existir = agir por si para além do roteiro). A pergunta 'Quem é você?' torna-se vertiginosa.","tip":"<strong>Modelo mental:</strong> use as camadas (Knag → Sofia; Gaarder → Hilde; você lendo) para pensar — quantas 'molduras' cercam minha sensação de realidade?"},
      {"ic":"eye","t":"O Cosmos e o Espanto Final","b":"O livro fecha onde abriu: no espanto. Somos <strong>poeira de estrelas</strong> — os átomos do nosso corpo foram forjados em estrelas extintas. O ser humano é a parte do cosmos que pergunta sobre o cosmos. A ciência explica o 'como'; o espanto filosófico diante do 'que haja algo' permanece.","tip":"<strong>Como aplicar:</strong> ao perceber a escala do universo e nossa origem estelar, o trivial recupera o caráter de milagre — e o espanto retorna."},
    ],
    "lessons_title": "Lições-Chave do Capítulo 9",
    "lessons": ["Sartre: não há essência prévia — nós nos fazemos pelas escolhas.", "A virada meta transforma a história da filosofia em experiência vivida pelo leitor.", "A maior sabedoria do livro é prática: não perca a capacidade de se admirar com o mundo."],
  },
]
