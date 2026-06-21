# -*- coding: utf-8 -*-
"""Conteúdo (pt-BR) de 'O Príncipe' (Nicolau Maquiavel)."""

BOOK = {
  "title": "O Príncipe",
  "author": "Nicolau Maquiavel",
  "header_light": "O",
  "header_bold": "PRÍNCIPE",
  "subtitle": "VISÃO GERAL · COMO O PODER REALMENTE FUNCIONA",
  "intro": "Maquiavel abandona o 'como deveria ser' e vai direto ao 'como é'. O Príncipe não pergunta se o poder é justo — pergunta como se conquista e se mantém. Um manual de realismo político que fundou a ciência política moderna.",
  "description": "O Príncipe de Maquiavel em cheat sheet: virtù × fortuna, temido vs. amado, raposa e leão, crueldade bem usada, armas próprias, evitar o ódio e o desprezo, lisonjeiros e reputação — os frameworks do poder real.",
  "tags": ["Poder", "Política", "Estratégia"],
  "progress": "9 Capítulos",
  "cover": "assets/o-principe-cover.png",
  "overview_cards": [
    {"ic":"target","t":"A Verdade Efetiva","b":"Maquiavel funda a política na <strong>realidade dos homens</strong>, não no ideal. 'Há tanta distância entre como se vive e como se deveria viver que quem larga o que se faz pelo que se deveria fazer aprende mais a se arruinar.' O realismo é a primeira ferramenta.","tip":"<strong>Modelo mental:</strong> governe os homens como eles são — ingratos, volúveis, interesseiros —, não como você desejaria que fossem."},
    {"ic":"scale","t":"Virtù × Fortuna","b":"A fortuna governa <strong>metade</strong> das ações humanas; a outra metade cabe à virtù — energia, talento, previsão, audácia. Sem virtù, a ocasião passa; sem fortuna, a virtù não tem onde agir.","tip":"<strong>Regra:</strong> erga diques na calmaria. A crise revela quem preparou a resistência e quem não o fez.","wide":True},
    {"ic":"sword","t":"Armas Próprias × Alheias","b":"Todo Estado se sustenta em boas leis e <strong>boas armas próprias</strong>. Mercenários são infiéis; auxiliares, perigosos; só a força própria é segura. Quem terceiriza a competência central fica à mercê do fornecedor.","tip":"<strong>Como aplicar:</strong> nunca delegue o que define o núcleo do seu poder a quem não compartilha o seu risco."},
  ],
}

CHAPTERS = [
  {
    "slug": "ch01-tipos-de-principados",
    "sub": "CAPÍTULO 1: Os Tipos de Principado",
    "intro": "Antes de governar, Maquiavel classifica. Diagnosticar o tipo de Estado é o primeiro ato político: a mesma ação que sustenta um hereditário arruína um novo.",
    "cards": [
      {"ic":"layers","t":"Hereditário × Novo × Misto","emph":"Hereditário","b":"No hereditário, a inércia joga a favor: o povo já se acostumou ao sangue. No novo, nasce a dificuldade: a esperança de melhora os faz pegar em armas. <strong>Já o misto é o mais traiçoeiro</strong> — aqueles que te ajudaram a entrar logo se revoltam por não receberem as terras que você havia prometido.","tip":"<strong>Modelo mental:</strong> diagnostique a origem do seu poder antes de agir — o remédio de um arruína o outro."},
      {"ic":"clock","t":"O Tempo como Aliado","emph":"Tempo","b":"A <strong>antiguidade do domínio</strong> apaga a memória das inovações e as razões das revoltas. Quanto mais tempo o poder dura, mais natural ele parece aos governados. O governante que herda o Estado tem menos motivos e necessidades para ofender — e por isso é mais facilmente amado.","tip":"<strong>Regra:</strong> na estrutura estabelecida, a inércia trabalha por você. Nunca rompa a ordem sem necessidade extrema."},
      {"ic":"mountain","t":"A Dificuldade do Novo","emph":"Dificuldade do Novo","b":"Todo poder recém-fundado nasce da ambição e gera <strong>inimigos automáticos</strong>: todos os que se davam bem com a ordem antiga te odeiam, e os tíbios que poderiam se dar bem com a nova te apoiam frouxamente. A resistência à mudança é sempre muito mais feroz que o entusiasmo por ela.","tip":"<strong>Sinal de alerta:</strong> ao instaurar uma nova ordem, espere fúria dos antigos beneficiários e apoio morno dos futuros.","warn":True},
    ],
    "lessons_title": "Lições-Chave do Capítulo 1",
    "lessons": ["Classifique o Estado antes de agir: a 'terapia' depende do 'diagnóstico'.", "No hereditário, a inércia e o tempo trabalham por você — não os quebre sem necessidade.", "No novo, prepare-se para a resistência desde o primeiro dia."],
  },
  {
    "slug": "ch02-principados-mistos",
    "sub": "CAPÍTULO 2: Principados Mistos — Conservar o Conquistado",
    "intro": "Manter o território recém-conquistado é a arte de antecipar a desordem enquanto ela ainda é pequena. A decepção dos novos súditos é inevitável — a questão é quando e como contê-la.",
    "cards": [
      {"ic":"eye","t":"Cure o Mal no Broto","emph":"Broto","b":"Os problemas de Estado são como a tuberculose: fáceis de curar mas difíceis de diagnosticar no início; fáceis de ver mas <strong>impossíveis de curar</strong> no fim. O custo de enfrentar a ameaça cresce exponencialmente com os dias. Não existe evitar a guerra, apenas adiá-la para a vantagem do inimigo.","tip":"<strong>Como aplicar:</strong> aja brutalmente cedo sobre os sinais fracos. O problema pequeno ignorado vira crise fatal.","warn":True},
      {"ic":"pin","t":"Resida no Conquistado","emph":"Resida","b":"Mudar-se para o território recém-conquistado permite <strong>ver os incêndios nascerem</strong> e apagá-los antes que se espalhem. O governo à distância só percebe a rebelião quando ela já tomou as ruas. Colônias custam quase nada e ofendem apenas os que perdem terras; guarnições esgotam o caixa e ofendem todos.","tip":"<strong>Modelo mental:</strong> a presença física detecta a desordem; a distância a alimenta até o ponto sem retorno."},
      {"ic":"spark","t":"Concentre a Dor, Dilua o Prazer","emph":"Concentre a Dor","b":"Todas as ofensas necessárias devem ser feitas de uma só vez, para machucarem menos e serem logo esquecidas. Já os benefícios devem ser concedidos de forma dosada e contínua, para serem saboreados por mais tempo. <strong>O mal repetido dia após dia acumula um ódio incurável</strong>, gangrenando a tolerância popular.","tip":"<strong>Regra:</strong> ao assumir o comando, execute toda a dureza de imediato. A dor concentrada evapora; a dor difusa gangrena."},
    ],
    "lessons_title": "Lições-Chave do Capítulo 2",
    "lessons": ["Cure o mal no broto: o custo de agir cresce exponencialmente.", "Resida no conquistado ou plante colônias — a presença detecta a desordem cedo.", "Concentre as durezas num único momento; distribua os benefícios devagar."],
  },
  {
    "slug": "ch03-virtu-e-fortuna",
    "sub": "CAPÍTULO 3: Virtù × Fortuna — As Duas Vias para o Poder",
    "intro": "Há dois caminhos para chegar ao poder: pelo próprio mérito (virtù) ou pelo acaso e favor alheio (fortuna). Quem sobe pela virtù sofre para adquirir mas mantém com facilidade; quem sobe pela fortuna adquire sem esforço e mantém com enorme dificuldade.",
    "cards": [
      {"ic":"mountain","t":"Virtù: A Metade que é Sua","emph":"Virtù","b":"Os maiores fundadores de impérios deveram à sorte apenas <strong>a ocasião</strong> — a matéria bruta esperando ser moldada. Todo o resto foi virtù: energia, audácia e eficácia. Sem a ocasião, o talento definha na obscuridade; sem a virtù, a ocasião de ouro escorrega pelas mãos e se perde para sempre.","tip":"<strong>Como aplicar:</strong> distinga a origem do seu sucesso. Se subiu pelo mérito, sustente o método; se foi sorte, crie fundações."},
      {"ic":"sword","t":"O Profeta Armado","emph":"Profeta Armado","b":"Todos os profetas que tinham armas venceram; os desarmados terminaram na cruz ou na fogueira. A persuasão sem poder de coerção é extremamente frágil: as multidões são <strong>naturalmente volúveis</strong>. Quando as palavras não convencerem mais, você precisará da força bruta para mantê-los acreditando.","tip":"<strong>Modelo mental:</strong> quem implanta uma nova ordem precisa de espada para sustentá-la quando o carisma perder o encanto.","warn":True},
      {"ic":"clock","t":"Fortuna Pede Raízes Rápidas","emph":"Raízes Rápidas","b":"Aquele que é catapultado ao topo pelo favor alheio ou por pura sorte deve <strong>lançar raízes desesperadamente</strong>. Construa a estrutura, as alianças e o poderio militar que não dependam de quem o elevou. O poder dado sem esforço tomba no primeiro vento contrário se você não se apressar.","tip":"<strong>Prática:</strong> o favor de um poderoso não é patrimônio — troque-o por poder real e autônomo o mais rápido possível."},
    ],
    "lessons_title": "Lições-Chave do Capítulo 3",
    "lessons": ["Virtù aproveita a ocasião que a fortuna oferece — sem uma, a outra é inútil.", "Subiu pela fortuna? Corra para criar raízes antes que o favor desapareça.", "Quem introduz nova ordem precisa de força para sustentá-la quando a persuasão falhar."],
  },
  {
    "slug": "ch04-armas-proprias",
    "sub": "CAPÍTULO 4: Armas Próprias × Mercenárias e Auxiliares",
    "intro": "Os alicerces do Estado são boas leis e boas armas. Mas sem boas armas não há boas leis — e só as armas próprias são seguras. A competência central do poder não pode ser terceirizada.",
    "cards": [
      {"ic":"sword","t":"Mercenárias: Infiéis e Covardes","emph":"Infiéis","b":"Tropas alugadas lutam apenas pelo salário no fim do mês — o que nunca será motivo suficiente para morrerem por você. São <strong>bravas entre amigos e covardes diante do inimigo</strong>. Sem lealdade ou disciplina real, elas engolem o seu orçamento na paz e te abandonam assim que a guerra aperta.","tip":"<strong>Modelo mental:</strong> capacidade alugada cria dependência crônica de quem vende, não fidelidade a quem comprou."},
      {"ic":"triangle","t":"Auxiliares: Ainda Piores","emph":"Auxiliares","b":"Pedir tropas emprestadas a um aliado poderoso é um erro fatal. Elas podem até ser organizadas e eficazes, mas são <strong>terrivelmente perigosas</strong>: se perdem, você afunda com elas; se vencem, você se torna refém de quem as emprestou. É uma armadura alheia que pesa, sufoca ou te apunhala pelas costas.","tip":"<strong>Sinal de alerta:</strong> vencer usando a força de outro não é vitória sua — é o início da sua submissão a ele.","warn":True},
      {"ic":"key","t":"A Arma Própria é a Única Segura","emph":"Arma Própria","b":"Nenhum governo está seguro sem possuir <strong>tropas próprias</strong>; sem elas, você depende totalmente da sorte e da boa vontade de terceiros. A guerra e a defesa são o negócio central de um príncipe — e aquilo que define a sobrevivência da sua organização jamais pode ser terceirizado.","tip":"<strong>Regra:</strong> construa excelência interna absoluta nas áreas que garantem o seu poder. Nunca delegue o coração da estratégia."},
    ],
    "lessons_title": "Lições-Chave do Capítulo 4",
    "lessons": ["Funde o poder em forças próprias; mercenários e auxiliares são riscos, não recursos.", "Vença com armas próprias, mesmo imperfeitas — a vitória pelas alheias não é sua.", "A competência central do poder não pode ser delegada a quem não compartilha o seu risco."],
  },
  {
    "slug": "ch05-temido-ou-amado",
    "sub": "CAPÍTULO 5: Temido × Amado — A Verdade Efetiva",
    "intro": "Aqui está o coração realista da obra: Maquiavel rompe com os idealismos e funda a política na realidade dos homens. Quem quer ser bom em tudo, entre tantos que não são, arruína-se.",
    "cards": [
      {"ic":"scale","t":"Temor > Amor (mas jamais Ódio)","emph":"Temor","b":"Sendo impossível ter ambos plenamente, <strong>prefira ser temido</strong>. O amor repousa na gratidão de homens interesseiros que te trocam por vantagem; o temor se apoia no medo de castigo, que nunca te abandona. Mas há uma linha vermelha: nunca seja odiado. Para isso, basta não roubar os bens nem as mulheres dos súditos.","tip":"<strong>Modelo mental:</strong> ancore o seu poder no que você controla (o medo) em vez de apostar no humor volátil dos outros (o amor)."},
      {"ic":"leaf","t":"A Parcimônia Governa","emph":"Parcimônia","b":"Abrace a fama de <strong>mão fechada</strong>. O governante que tenta ser generoso para ganhar aplausos logo seca os cofres e se vê obrigado a extorquir o povo com impostos altos — ganhando o ódio de todos. A parcimônia austera garante estabilidade sem precisar saquear o próprio país. Gaste o alheio; o seu, poupe.","tip":"<strong>Como aplicar:</strong> a generosidade ostensiva é um veneno que consome a si mesmo. Seja rigoroso com a caixa para manter a paz."},
      {"ic":"target","t":"A Crueldade Bem Usada","emph":"Crueldade Bem Usada","b":"Um governante não deve temer a fama de cruel quando essa dureza serve para manter os súditos unidos e fiéis. Um punhado de <strong>castigos exemplares</strong> e brutais é muito mais misericordioso do que a fraqueza que permite saques, assassinatos e a desordem total do Estado. A clemência mal calculada derrama rios de sangue.","tip":"<strong>Armadilha:</strong> o excesso de piedade permite o caos que pune a todos. A punição cirúrgica salva o sistema.","warn":True},
    ],
    "lessons_title": "Lições-Chave do Capítulo 5",
    "lessons": ["Prefira ser temido a amado — mas nunca odiado (não toque em bens e honra alheios).", "Aceite a fama de avaro: a parcimônia governa; a prodigalidade espolia.", "A crueldade dosada que mantém a ordem é mais piedosa que a clemência que gera o caos."],
  },
  {
    "slug": "ch06-raposa-e-leao",
    "sub": "CAPÍTULO 6: A Raposa e o Leão",
    "intro": "O capítulo mais célebre: como manter a palavra. A resposta é brutal — quem fez grandes feitos foi quem menos a honrou e soube, com astúcia, confundir os homens. Há dois modos de combater: pelas leis e pela força.",
    "cards": [
      {"ic":"mask","t":"Dois Modos de Combater","emph":"Raposa e Leão","b":"O governante deve ser <strong>raposa para farejar as ciladas e leão para destroçar os lobos</strong>. Apostar em apenas uma natureza é pedir para ser engolido pela primeira crise disfarçada de oportunidade. Na selva do poder, o leão é incapaz de escapar das armadilhas da fraude, e a raposa esconde-se inútil da violência bruta.","tip":"<strong>Modelo mental:</strong> astúcia detecta o ataque furtivo; força bruta massacra o ataque aberto. Domine ambas as marchas."},
      {"ic":"eye","t":"A Palavra Não É Sagrada","emph":"Palavra","b":"Uma promessa <strong>nunca te obriga</strong> quando o cumprimento se volta contra você e quando as razões que a motivaram não existem mais. Os homens são maus e não manteriam a palavra dada a ti — você não tem de mantê-la a eles. Um príncipe inteligente é sempre um grande mestre na arte de simular e dar desculpas brilhantes.","tip":"<strong>Sinal de alerta:</strong> prender-se a uma promessa suicida por 'honra' num jogo onde o adversário não tem nenhuma é estupidez.","warn":True},
      {"ic":"person","t":"As Cinco Aparências","emph":"Aparências","b":"É vital parecer clemente, leal, humano, íntegro e devoto — e, se possível, até sê-lo. Mas você deve estar mentalmente pronto para <strong>inverter para o exato oposto</strong> quando o Estado exigir. A massa engole o que os olhos veem e o que as mãos tocam; se você vencer e mantiver o poder, os meios serão sempre aplaudidos.","tip":"<strong>Regra:</strong> o palco exige a máscara da virtude perfeita. O que sustenta o palco, porém, é a disposição para rasgá-la."},
    ],
    "lessons_title": "Lições-Chave do Capítulo 6",
    "lessons": ["Combine astúcia (raposa) e força (leão) — nenhuma basta sozinha.", "A palavra não obriga quando prejudica e a razão que a motivou cessou.", "A maioria julga pelo resultado e pela aparência — cultive as cinco qualidades visíveis."],
  },
  {
    "slug": "ch07-evitar-odio-desprezo",
    "sub": "CAPÍTULO 7: Evitar o Ódio e o Desprezo",
    "intro": "O maior perigo vem de dentro: ser odiado ou desprezado pelos súditos. Tudo o que protege de conspirações se resume a uma regra — quem não é odiado nem desprezado raramente é conspirado.",
    "cards": [
      {"ic":"gap","t":"As Duas Coisas a Evitar","emph":"Ódio e Desprezo","b":"Sua sobrevivência depende de fugir de dois abismos absolutos: <strong>o ódio público e o desprezo geral</strong>. Roubar bens ou demonstrar covardia frívola sela a sua ruína. Se não for odiado nem desprezado pela massa, quase não enfrentará o fantasma paralisante das conspirações noturnas. Demonstre sempre firmeza de espírito.","tip":"<strong>Regra:</strong> a linha da vida do poder é o respeito. Perdoam-se os erros, nunca a fraqueza escancarada ou o confisco de bens.","warn":True},
      {"ic":"person","t":"O Povo é a Maior Fortaleza","emph":"Maior Fortaleza","b":"O conspirador age tremendo de medo das leis e da punição; o governante tem o Estado, os exércitos e os amigos. Se você tiver <strong>o povo do seu lado</strong>, executar um golpe vira uma missão quase suicida. Nenhuma fortaleza de pedra e aço te salvará no dia em que a população inteira desejar o seu sangue vivo.","tip":"<strong>Modelo mental:</strong> o escudo mais impenetrável de um líder é a aprovação silenciosa das massas. Construa sua base nelas."},
      {"ic":"fork","t":"Delegue o Odioso","emph":"Delegue","b":"No jogo do poder, você distribui os favores com suas próprias mãos iluminadas; <strong>as tarefas de punição você terceiriza a um carrasco</strong>. César Bórgia mandou seu subordinado cortar cabeças e depois o eliminou sumariamente. O povo se acalmou, e toda a culpa do sangue secou junto do defunto culpado.","tip":"<strong>Como aplicar:</strong> centralize os créditos; distribua a lama. O mal necessário jamais deve carregar a sua assinatura."},
    ],
    "lessons_title": "Lições-Chave do Capítulo 7",
    "lessons": ["Não seja odiado (não toque em bens e honra) nem desprezado (aja com firmeza).", "A maior fortaleza é o povo do seu lado — nenhuma muralha compensa o ódio popular.", "Faça o favor com seu nome; delegue o odioso a outrem."],
  },
  {
    "slug": "ch08-reputacao-lisonjeiros",
    "sub": "CAPÍTULO 8: Reputação, Ministros e Lisonjeiros",
    "intro": "O poder se mantém também pela reputação e pela qualidade de quem o cerca. A inteligência de um príncipe se mede primeiro pelos homens que escolhe — e o maior risco da corte é o lisonjeiro.",
    "cards": [
      {"ic":"mountain","t":"Reputação por Grandes Feitos","emph":"Grandes Feitos","b":"Gestos grandiosos e empreitadas colossais cimentam a lenda do governante. O segredo mestre é <strong>tomar partido com total clareza</strong>. Declarar-se um amigo devotado ou um inimigo implacável é sempre mais lucrativo que a neutralidade irresoluta. Quem tenta fugir da briga acaba devorado pelo vencedor e vira escárnio do perdedor.","tip":"<strong>Prática:</strong> posicione-se firmemente em conflitos polarizados. O neutro é a primeira vítima escolhida por todos os lados."},
      {"ic":"key","t":"Bons Ministros","emph":"Bons Ministros","b":"O primeiro diagnóstico da inteligência de um líder é a qualidade da equipe que o cerca. O ministro ideal pensa <strong>mais no Estado que no próprio bolso</strong>. Para blindar a lealdade dele, honre-o, pague muito bem e divida a responsabilidade, fazendo-o temer radicalmente qualquer mudança que ameace você — pois ameaçará a ele.","tip":"<strong>Modelo mental:</strong> o braço direito perfeito precisa que o seu sucesso seja a única garantia absoluta do sucesso dele."},
      {"ic":"bubble","t":"Blinde-se dos Lisonjeiros","emph":"Blinde-se","b":"As cortes estão infectadas de bajuladores profissionais vendendo ilusões para o seu ego. A vacina é <strong>dar a um núcleo diminuto de sábios a permissão para dizer a verdade</strong> — mas apenas quando você perguntar. Ouça profundamente o conselho franco desse grupo fechado e tome a decisão final sozinho, em absoluto silêncio.","tip":"<strong>Sinal de alerta:</strong> líder que escuta todos sobre tudo vira um catavento; quem recusa qualquer crítica marcha cego para o abismo.","warn":True},
    ],
    "lessons_title": "Lições-Chave do Capítulo 8",
    "lessons": ["Construa reputação com grandes feitos e posições firmes; nunca seja neutro.", "Escolha bons ministros e prenda-os pela honra e pela dependência ao Estado.", "Blinde-se da lisonja: dê a poucos sábios a liberdade de dizer a verdade — só quando perguntados."],
  },
  {
    "slug": "ch09-fortuna-e-virtu",
    "sub": "CAPÍTULO 9: 'A Fortuna é Mulher' — Virtù e Ocasião",
    "intro": "A pergunta filosófica que organiza toda a obra: quanto do destino cabe à fortuna e quanto à virtù? Maquiavel rejeita o fatalismo — a fortuna é árbitra de metade das ações, mas deixa a outra metade ao nosso governo.",
    "cards": [
      {"ic":"wave","t":"Rio e Diques","emph":"Rio e Diques","b":"A sorte é como um rio violento: quando transborda, engole planícies e afoga o gado. Mas é no tempo seco que <strong>os homens sábios erguem os diques e as barreiras</strong>. Assim, quando a fúria das águas chegar, o estrago é contido e domado. A fortuna só destrói impiedosamente onde não há defesa de aço preparada a tempo.","tip":"<strong>Modelo mental:</strong> a calamidade é inevitável. Você não controla a tempestade, mas o muro que construiu no sol dita se você sobrevive."},
      {"ic":"clock","t":"Adapte-se aos Tempos","emph":"Adapte-se aos Tempos","b":"Prospera blindado no poder quem <strong>afina seu jeito de governar com a música da época</strong>. O método agressivo que forjou um império hoje pode causar sua ruína sangrenta amanhã. A grande tragédia humana é que é quase impossível desviar de uma natureza que sempre nos deu vitórias — e por não mudarmos, a fortuna nos tritura.","tip":"<strong>Sinal de alerta:</strong> o seu maior sucesso passado é a âncora invisível que te afoga na nova era. Seja veloz e maleável.","warn":True},
      {"ic":"spark","t":"A Audácia Vence o Acaso","emph":"Audácia","b":"Como uma força selvagem e ciumenta, a fortuna é muito mais submissa aos <strong>jovens audaciosos e impetuosos</strong> do que aos velhos cautelosos que calculam eternamente o passo. Na dúvida mortal, 'é melhor ser impetuoso que cauteloso'. Quem é esmagado pelos eventos covardemente, falhou em virtù, nossa glória está em nós.","tip":"<strong>Regra:</strong> o cálculo excessivo paralisa a máquina de ação. Num cenário de névoa incerta, a agressividade controlada é o seu melhor escudo."},
    ],
    "lessons_title": "Lições-Chave do Capítulo 9",
    "lessons": ["A fortuna governa metade; a outra metade é sua — recuse o fatalismo.", "Erga diques na calmaria: a previsão prudente contém a ruína da crise.", "Adapte o método aos tempos; na incerteza, a audácia vence a hesitação."],
  },
]
