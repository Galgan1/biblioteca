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
      {"ic":"layers","t":"Hereditário × Novo × Misto","b":"<strong>Hereditário</strong>: inércia a favor, fácil de manter. <strong>Novo</strong>: toda a dificuldade nasce aqui. <strong>Misto</strong> (território anexado): o mais traiçoeiro — gera esperança e decepção.","tip":"<strong>Modelo mental:</strong> diagnostique o tipo antes de decidir a terapia — a mesma ação que sustenta um arruína o outro."},
      {"ic":"clock","t":"O Tempo como Aliado","b":"A <strong>antiguidade do domínio</strong> apaga a memória das mudanças. Quanto mais o poder dura, mais parece natural. O príncipe hereditário tem menos razões para ofender e por isso é mais amado.","tip":"<strong>Regra:</strong> no hereditário, a inércia trabalha a seu favor — não a rompa sem necessidade."},
      {"ic":"mountain","t":"A Dificuldade do Novo","b":"O principado novo nasce da ambição e gera <strong>novos inimigos</strong>: todos os que se davam bem com a ordem antiga e os tíbios que poderiam se dar bem com a nova. A resistência à mudança é quase sempre mais feroz que o apoio.","tip":"<strong>Sinal de alerta:</strong> ao instaurar uma nova ordem, espere oposição feroz dos antigos beneficiários e apoio morno dos futuros.","warn":True},
    ],
    "lessons_title": "Lições-Chave do Capítulo 1",
    "lessons": ["Classifique o Estado antes de agir: a 'terapia' depende do 'diagnóstico'.", "No hereditário, a inércia e o tempo trabalham por você — não os quebre sem necessidade.", "No novo, prepare-se para a resistência desde o primeiro dia."],
  },
  {
    "slug": "ch02-principados-mistos",
    "sub": "CAPÍTULO 2: Principados Mistos — Conservar o Conquistado",
    "intro": "Manter o território recém-conquistado é a arte de antecipar a desordem enquanto ela ainda é pequena. A decepção dos novos súditos é inevitável — a questão é quando e como contê-la.",
    "cards": [
      {"ic":"eye","t":"Cure o Mal no Broto","b":"'Como a tísica: fácil de curar e difícil de conhecer no início; depois, fácil de conhecer e impossível de curar.' O custo de agir <strong>cresce exponencialmente</strong> com o tempo. <strong>Não existe evitar a guerra — só adiá-la em vantagem do inimigo.</strong>","tip":"<strong>Como aplicar:</strong> aja cedo sobre sinais fracos. O problema pequeno ignorado vira crise sem solução."},
      {"ic":"pin","t":"Resida no Conquistado","b":"Ir morar no território conquistado (ou fundar colônias) permite ver os males nascendo e cortá-los cedo. O governo <strong>à distância</strong> só percebe quando o mal já é incurável. Colônias custam pouco e ofendem poucos; guarnições militares custam caro e ofendem todos.","tip":"<strong>Modelo mental:</strong> presença detecta a desordem; distância a deixa crescer até o ponto sem retorno."},
      {"ic":"spark","t":"Concentre a Dor, Dilua o Prazer","b":"Ofensas devem ser feitas <strong>todas de uma vez</strong>, para serem menos sentidas; benefícios, <strong>aos poucos</strong>, para serem mais saboreados. A memória do mal feito de uma vez se apaga; a do mal repetido se acumula em ódio.","tip":"<strong>Regra:</strong> ao entrar num novo Estado, decida todas as durezas necessárias de uma vez — não as renove dia após dia."},
    ],
    "lessons_title": "Lições-Chave do Capítulo 2",
    "lessons": ["Cure o mal no broto: o custo de agir cresce exponencialmente.", "Resida no conquistado ou plante colônias — a presença detecta a desordem cedo.", "Concentre as durezas num único momento; distribua os benefícios devagar."],
  },
  {
    "slug": "ch03-virtu-e-fortuna",
    "sub": "CAPÍTULO 3: Virtù × Fortuna — As Duas Vias para o Poder",
    "intro": "Há dois caminhos para chegar ao poder: pelo próprio mérito (virtù) ou pelo acaso e favor alheio (fortuna). Quem sobe pela virtù sofre para adquirir mas mantém com facilidade; quem sobe pela fortuna adquire sem esforço e mantém com enorme dificuldade.",
    "cards": [
      {"ic":"mountain","t":"Virtù: A Metade que é Sua","b":"Os grandes fundadores deveram à fortuna apenas <strong>a ocasião</strong> — a matéria a ser moldada. Todo o resto foi virtù. Sem a ocasião, a virtù se desperdiça; sem virtù, a ocasião passa em vão. A virtù não é virtude moral: é eficácia, energia, audácia.","tip":"<strong>Como aplicar:</strong> distinga como você chegou ao poder — por mérito (mantenha o método) ou por sorte (corra para criar raízes)."},
      {"ic":"sword","t":"O Profeta Armado","b":"'Todos os profetas armados venceram; os desarmados se perderam.' A persuasão sem poder de coerção é frágil: os povos são <strong>volúveis</strong>, fáceis de persuadir e difíceis de manter na crença. Quando deixam de crer, é preciso fazê-los crer à força.","tip":"<strong>Modelo mental:</strong> quem implanta uma nova ordem precisa de força para sustentá-la quando a persuasão falhar."},
      {"ic":"clock","t":"Fortuna Pede Raízes Rápidas","b":"Quem sobe pela fortuna deve <strong>lançar raízes depressa</strong> — construir estrutura, alianças e legitimidade que não dependam do favor que o elevou. A fortuna é árbitra de metade; só a virtù garante a outra.","tip":"<strong>Sinal de alerta:</strong> poder obtido por sorte ou favor alheio é frágil enquanto não tiver raízes próprias.","warn":True},
    ],
    "lessons_title": "Lições-Chave do Capítulo 3",
    "lessons": ["Virtù aproveita a ocasião que a fortuna oferece — sem uma, a outra é inútil.", "Subiu pela fortuna? Corra para criar raízes antes que o favor desapareça.", "Quem introduz nova ordem precisa de força para sustentá-la quando a persuasão falhar."],
  },
  {
    "slug": "ch04-armas-proprias",
    "sub": "CAPÍTULO 4: Armas Próprias × Mercenárias e Auxiliares",
    "intro": "Os alicerces do Estado são boas leis e boas armas. Mas sem boas armas não há boas leis — e só as armas próprias são seguras. A competência central do poder não pode ser terceirizada.",
    "cards": [
      {"ic":"sword","t":"Mercenárias: Infiéis e Covardes","b":"Tropas pagas lutam apenas pelo soldo, que não basta para fazê-las morrer por você. <strong>Bravas entre amigos, covardes diante do inimigo</strong> — sem fé nem disciplina real. A Itália de Maquiavel foi humilhada por confiar décadas em condottieri mercenários.","tip":"<strong>Modelo mental:</strong> capacidade comprada cria dependência de quem vende, não vínculo com quem comprou."},
      {"ic":"triangle","t":"Auxiliares: Ainda Piores","b":"Tropas emprestadas por um aliado forte são eficazes — e por isso <strong>mais perigosas</strong>: se perdem, você está perdido com elas; se vencem, você fica refém delas. São 'armas que pesam, apertam ou cortam' em quem as veste.","tip":"<strong>Sinal de alerta:</strong> vencer com força alheia não é sua vitória — é a dívida que você acumula.","warn":True},
      {"ic":"key","t":"A Arma Própria é a Única Segura","b":"'Nenhum principado está seguro sem armas próprias; depende inteiramente da fortuna, sem virtù que o defenda na adversidade.' A guerra é o <strong>core business</strong> do príncipe — o que define a função não pode ser delegado.","tip":"<strong>Como aplicar:</strong> construa competência interna nas áreas que definem o seu poder; nunca delegue o núcleo estratégico."},
    ],
    "lessons_title": "Lições-Chave do Capítulo 4",
    "lessons": ["Funde o poder em forças próprias; mercenários e auxiliares são riscos, não recursos.", "Vença com armas próprias, mesmo imperfeitas — a vitória pelas alheias não é sua.", "A competência central do poder não pode ser delegada a quem não compartilha o seu risco."],
  },
  {
    "slug": "ch05-temido-ou-amado",
    "sub": "CAPÍTULO 5: Temido × Amado — A Verdade Efetiva",
    "intro": "Aqui está o coração realista da obra: Maquiavel rompe com os idealismos e funda a política na realidade dos homens. Quem quer ser bom em tudo, entre tantos que não são, arruína-se.",
    "cards": [
      {"ic":"scale","t":"Temor > Amor (mas jamais Ódio)","b":"Não cabendo ser ambos, <strong>prefira ser temido</strong>: o amor depende dos outros (ingratos), o temor depende de você (medo do castigo). Mas <strong>nunca odiado</strong> — a linha vermelha é não tocar nos bens e na honra dos súditos. 'Os homens esquecem mais depressa a morte do pai que a perda do patrimônio.'","tip":"<strong>Modelo mental:</strong> funde o poder no que está sob seu controle — o temor. O amor depende de quem pode mudar de humor."},
      {"ic":"leaf","t":"A Parcimônia Governa","b":"Aceitar a fama de <strong>avaro</strong> é mais sábio que a de liberal: a liberalidade ostensiva exige sobrecarregar o povo de impostos e gera ódio; a parcimônia governa sem espoliar. Gaste o alheio com largueza; o próprio, com cautela.","tip":"<strong>Como aplicar:</strong> a parcimônia é a virtude que permite manter o Estado sem criar dependência de recursos que acabam."},
      {"ic":"target","t":"A Crueldade Bem Usada","b":"Não temer a fama de cruel quando ela mantém os súditos unidos: poucos <strong>castigos exemplares</strong> são mais piedosos que a clemência que deixa o desgoverno gerar mortes e saques. 'A clemência mal calculada é a maior crueldade.'","tip":"<strong>Regra:</strong> faça-a de uma vez, por necessidade, e não a renove — a dor concentrada se apaga; a difusa acumula ódio."},
    ],
    "lessons_title": "Lições-Chave do Capítulo 5",
    "lessons": ["Prefira ser temido a amado — mas nunca odiado (não toque em bens e honra alheios).", "Aceite a fama de avaro: a parcimônia governa; a prodigalidade espolia.", "A crueldade dosada que mantém a ordem é mais piedosa que a clemência que gera o caos."],
  },
  {
    "slug": "ch06-raposa-e-leao",
    "sub": "CAPÍTULO 6: A Raposa e o Leão",
    "intro": "O capítulo mais célebre: como manter a palavra. A resposta é brutal — quem fez grandes feitos foi quem menos a honrou e soube, com astúcia, confundir os homens. Há dois modos de combater: pelas leis e pela força.",
    "cards": [
      {"ic":"mask","t":"Dois Modos de Combater","b":"O leão não se defende das armadilhas; a raposa, não dos lobos. É preciso ser <strong>raposa para conhecer as ciladas</strong> e <strong>leão para espantar os lobos</strong>. Cada um sozinho é cego — o príncipe alterna os dois conforme o adversário.","tip":"<strong>Modelo mental:</strong> astúcia (raposa) detecta a fraude; força (leão) impede o ataque. Nunca use só um."},
      {"ic":"eye","t":"A Palavra Não É Sagrada","b":"A palavra <strong>não obriga</strong> quando prejudica e quando cessou a razão que a motivou — 'pois os homens, sendo maus, não a guardariam com você'. O príncipe deve ser grande simulador e dissimulador; sempre há razões legítimas para encobrir a quebra.","tip":"<strong>Chave analítica:</strong> serve sobretudo para reconhecer quando um poderoso está sendo 'raposa' — quebrando a palavra sob capa de virtude."},
      {"ic":"person","t":"As Cinco Aparências","b":"Parecer <strong>clemente, fiel, humano, íntegro e religioso</strong> — e até sê-lo. Mas estar pronto a inverter sob necessidade. A maioria julga pela aparência e pelo resultado: 'que vença e mantenha o Estado, e os meios serão julgados honrosos.'","tip":"<strong>Sinal de alerta:</strong> a aparência da virtude vale mais que a virtude num mundo que julga pelos olhos e pelo fim.","warn":True},
    ],
    "lessons_title": "Lições-Chave do Capítulo 6",
    "lessons": ["Combine astúcia (raposa) e força (leão) — nenhuma basta sozinha.", "A palavra não obriga quando prejudica e a razão que a motivou cessou.", "A maioria julga pelo resultado e pela aparência — cultive as cinco qualidades visíveis."],
  },
  {
    "slug": "ch07-evitar-odio-desprezo",
    "sub": "CAPÍTULO 7: Evitar o Ódio e o Desprezo",
    "intro": "O maior perigo vem de dentro: ser odiado ou desprezado pelos súditos. Tudo o que protege de conspirações se resume a uma regra — quem não é odiado nem desprezado raramente é conspirado.",
    "cards": [
      {"ic":"gap","t":"As Duas Coisas a Evitar","b":"<strong>Ódio</strong> (gerado por rapacidade sobre bens e honra alheios) e <strong>desprezo</strong> (gerado por aparecer volúvel, frívolo, pusilânime, irresoluto). Evitar os dois é quase suficiente — quem não é nem um nem outro raramente tem conspiradores.","tip":"<strong>Regra:</strong> mostre grandeza, firmeza e decisão irrevogável; que ninguém pense em ludibriá-lo."},
      {"ic":"person","t":"O Povo é a Maior Fortaleza","b":"O conspirateur anda com medo e a lei contra si; o príncipe tem poder e amigos. Se o povo está do seu lado, conspirar fica <strong>quase impossível</strong>. 'A melhor fortaleza é não ser odiado pelo povo — nenhuma muralha salva quem o povo detesta.'","tip":"<strong>Modelo mental:</strong> o escudo do poder é a opinião popular — base que nenhuma pedra substitui."},
      {"ic":"fork","t":"Delegue o Odioso","b":"As coisas de <strong>favor</strong>, o príncipe faz por si; as de <strong>punição e desagrado</strong>, delega a outros. Colhe a gratidão, terceiriza o rancor. Borgia mandou cortar ao meio o executor Remirro de Orco e o povo ficou 'satisfeito e estupefato' — a crueldade foi atribuída a um terceiro.","tip":"<strong>Como aplicar:</strong> separe os fluxos de crédito e culpa. Faça o bem com seu nome; o mal, com o nome dos outros."},
    ],
    "lessons_title": "Lições-Chave do Capítulo 7",
    "lessons": ["Não seja odiado (não toque em bens e honra) nem desprezado (aja com firmeza).", "A maior fortaleza é o povo do seu lado — nenhuma muralha compensa o ódio popular.", "Faça o favor com seu nome; delegue o odioso a outrem."],
  },
  {
    "slug": "ch08-reputacao-lisonjeiros",
    "sub": "CAPÍTULO 8: Reputação, Ministros e Lisonjeiros",
    "intro": "O poder se mantém também pela reputação e pela qualidade de quem o cerca. A inteligência de um príncipe se mede primeiro pelos homens que escolhe — e o maior risco da corte é o lisonjeiro.",
    "cards": [
      {"ic":"mountain","t":"Reputação por Grandes Feitos","b":"Realizações notáveis e gestos memoráveis impõem admiração. <strong>Tome partido com clareza</strong>: declarar-se franco amigo ou inimigo é sempre mais útil que a neutralidade. 'Quem fica em cima do muro é descartado pelo vencedor e desprezado pelo perdedor.'","tip":"<strong>Regra:</strong> posicione-se — o neutro vira presa de ambos os lados."},
      {"ic":"key","t":"Bons Ministros","b":"O bom ministro pensa mais no <strong>Estado que em si</strong>. Para mantê-lo fiel: honre-o, enriqueça-o e partilhe responsabilidades, para que dependa de você e tema a mudança. 'Os três cérebros': o que entende por si, o que entende o que outros entendem, e o que não entende nem por si.","tip":"<strong>Como aplicar:</strong> a qualidade da equipe é o primeiro sinal da sua própria inteligência — você é julgado por quem escolhe."},
      {"ic":"bubble","t":"Blinde-se dos Lisonjeiros","b":"As cortes estão cheias de lisonjeiros — e os homens se comprazem com as próprias coisas. O remédio: dê a <strong>poucos sábios</strong> a liberdade de dizer a verdade, <strong>só quando perguntados</strong>. Ouça amplo, decida sozinho. 'Bons conselhos nascem da prudência do príncipe, não a prudência dos bons conselhos.'","tip":"<strong>Sinal de alerta:</strong> quem ouve todos sobre tudo perde o respeito; quem não ouve ninguém se arruína.","warn":True},
    ],
    "lessons_title": "Lições-Chave do Capítulo 8",
    "lessons": ["Construa reputação com grandes feitos e posições firmes; nunca seja neutro.", "Escolha bons ministros e prenda-os pela honra e pela dependência ao Estado.", "Blinde-se da lisonja: dê a poucos sábios a liberdade de dizer a verdade — só quando perguntados."],
  },
  {
    "slug": "ch09-fortuna-e-virtu",
    "sub": "CAPÍTULO 9: 'A Fortuna é Mulher' — Virtù e Ocasião",
    "intro": "A pergunta filosófica que organiza toda a obra: quanto do destino cabe à fortuna e quanto à virtù? Maquiavel rejeita o fatalismo — a fortuna é árbitra de metade das ações, mas deixa a outra metade ao nosso governo.",
    "cards": [
      {"ic":"wave","t":"Rio e Diques","b":"A fortuna é um <strong>rio impetuoso</strong>: quando enfurece, arrasa tudo. Mas na calmaria os homens erguem <strong>diques e barreiras</strong> — assim o rio não causa ruína. A fortuna mostra seu poder onde não há virtù preparada para resistir.","tip":"<strong>Modelo mental:</strong> metade é sorte, metade é sua. Construa os diques na calmaria — a crise só revela quem se preparou.","wide":True},
      {"ic":"clock","t":"Adapte-se aos Tempos","b":"Feliz é quem <strong>harmoniza seu modo de agir com a qualidade dos tempos</strong>; infeliz, quem descompassa. O mesmo método dá certo numa época e arruína em outra. O problema: o homem não consegue mudar a própria natureza — por isso a fortuna varia.","tip":"<strong>Como aplicar:</strong> revise periodicamente se o seu método ainda se encaixa nos tempos — a virtù que não muda vira o vício de outrora."},
      {"ic":"spark","t":"A Audácia Vence o Acaso","b":"A fortuna cede mais aos <strong>audaciosos</strong> do que aos cautelosos. 'É melhor ser impetuoso que cauteloso' — desde que os diques estejam de pé. Quem perde o Estado falhou em virtù, não foi traído pela sorte: 'nossa liberdade depende de nós.'","tip":"<strong>Regra:</strong> na incerteza, prefira a audácia à hesitação — mas tendo construído a estrutura de suporte antes."},
    ],
    "lessons_title": "Lições-Chave do Capítulo 9",
    "lessons": ["A fortuna governa metade; a outra metade é sua — recuse o fatalismo.", "Erga diques na calmaria: a previsão prudente contém a ruína da crise.", "Adapte o método aos tempos; na incerteza, a audácia vence a hesitação."],
  },
]
