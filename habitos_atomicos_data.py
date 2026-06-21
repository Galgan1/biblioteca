# -*- coding: utf-8 -*-
"""Conteúdo (pt-BR) das páginas da biblioteca para 'Hábitos Atômicos' (James Clear).
Frameworks: 1%/sistemas, identidade, loop do hábito, as 4 leis, regra dos 2 minutos."""

BOOK = {
 "title": "Hábitos Atômicos",
 "author": "James Clear",
 "header_light": "HÁBITOS",
 "header_bold": "ATÔMICOS",
 "subtitle": "VISÃO GERAL · PEQUENAS MUDANÇAS, RESULTADOS NOTÁVEIS",
 "intro": "Você não sobe ao nível das suas metas — cai ao nível dos seus sistemas. Um hábito atômico é uma mudança de 1% que, repetida, compõe resultados notáveis. James Clear mostra o loop do hábito, as quatro leis da mudança de comportamento e a alavanca mais profunda de todas: a identidade.",
 "description": "O método prático de James Clear para construir bons hábitos e abandonar os ruins. O 1% melhor por dia, os sistemas acima das metas, a mudança baseada em identidade, o loop do hábito e as quatro leis — tornar óbvio, atraente, fácil e satisfatório — com a regra dos 2 minutos e o rastreador de hábitos.",
 "tags": ["Hábitos", "Produtividade", "Autodesenvolvimento"],
 "progress": "8 Capítulos",
 "cover": "assets/habitos-atomicos-cover.png",
 "overview_cards": [
   {"ic":"steps","t":"As Quatro Leis da Mudança","b":"Uma alavanca para cada estágio do loop (e a inversa para quebrar):","list":[
     "<strong>1ª — Torne Óbvio</strong> (a deixa).",
     "<strong>2ª — Torne Atraente</strong> (o desejo).",
     "<strong>3ª — Torne Fácil</strong> (a resposta).",
     "<strong>4ª — Torne Satisfatório</strong> (a recompensa).",
   ],"tip":"<strong>Como aplicar:</strong> para largar um mau hábito, inverta — invisível, sem graça, difícil, insatisfatório.","wide":True},
   {"ic":"layers","t":"Mudança por Identidade","b":"Três níveis — <strong>resultados</strong> (o que obtenho) → <strong>processos</strong> (o que faço) → <strong>identidade</strong> (o que creio ser). O durável muda de dentro para fora.","tip":"<strong>Modelo mental:</strong> cada hábito é um voto no tipo de pessoa que você quer se tornar."},
   {"ic":"spark","t":"O 1% e os Sistemas","b":"Melhorar <strong>1% ao dia</strong> ≈ 37× no ano. <strong>Sistemas &gt; metas</strong> — metas dão direção, o sistema produz o progresso.","tip":"<strong>Regra:</strong> apaixone-se pelo processo; a meta vem como consequência."},
 ],
}

# Infografico de Instagram (Diretor de Design) — arquetipo FLUXO (gerar_infografico.py)
FLUXO = {
 "kicker": "O LOOP DO HÁBITO EM 4 LEIS",
 "steps": [
   {"n":"1","ic":"eye","lbl":"Deixa","law":"1ª Lei · Torne Óbvio",
    "sub":"O gatilho do ambiente que dispara o comportamento. Deixe-o à vista."},
   {"n":"2","ic":"spark","lbl":"Desejo","law":"2ª Lei · Torne Atraente",
    "sub":"A expectativa da recompensa que motiva. Agrupe-o com algo prazeroso."},
   {"n":"3","ic":"leaf","lbl":"Resposta","law":"3ª Lei · Torne Fácil",
    "sub":"A ação em si. Reduza o atrito: comece na versão de <strong>2 minutos</strong>."},
   {"n":"4","ic":"key","lbl":"Recompensa","law":"4ª Lei · Torne Satisfatório",
    "sub":"O prazer que ensina o cérebro a repetir. Feche o loop com satisfação imediata.","gold":True},
 ],
 "na_pratica": "Empilhe UM novo hábito num que já existe — “depois de [rotina], "
               "vou [hábito]” — na versão de <strong>2 minutos</strong>.",
}

# Infografico de Instagram (Diretor de Design) — arquetipo NUMEROS (gerar_infografico.py)
NUMEROS = {
 "kicker": "O LIVRO EM NÚMEROS", "tag": "DADOS",
 "stats": [
   {"ic":"spark","num":"37","unit":"×","star":True,"lbl":"em um ano",
    "ctx":"Melhorar <b>1% por dia</b> compõe ~37 vezes em 12 meses. 1% pior tende a zero."},
   {"ic":"clock","pre":"≤","num":"2","unit":"min","lbl":"a regra de começar",
    "ctx":"Todo hábito novo começa numa versão de <b>2 minutos</b>. Domine a arte de aparecer."},
   {"ic":"layers","num":"3","lbl":"níveis de mudança",
    "ctx":"Resultados → processos → <b>identidade</b>. O durável muda de dentro para fora."},
 ],
 "viz": {"type":"curve","title":"Os juros compostos do comportamento","note":"1% ao dia &rarr; <b>37&times;</b> / ano"},
 "foot": {"ic":"spark","text":"Esqueça a meta: projete o <strong>sistema diário</strong>. "
          "Comece pela versão de 2 minutos e deixe o 1% compor."},
}

# Infografico de Instagram (Diretor de Design) — arquetipo ANATOMIA (anel/ciclo)
ANATOMIA = {
 "eyebrow": "Anatomia · Hábitos Atômicos",
 "h1": '<span class="lt">Anatomia</span> de um hábito',
 "sub": "Todo hábito gira num ciclo de quatro estágios — e cada um tem uma Lei "
        "que o cria (ou, invertida, o quebra).",
 "hub": {"l1": "O LOOP", "l2": "DO HÁBITO", "note": "O MOTOR DE TODO HÁBITO"},
 "nodes": [
   {"ic":"eye","law":"1ª Lei · Torne Óbvio","lbl":"A Deixa",
    "exp":"O gatilho que <b>dispara</b> o hábito. À vista p/ criar; invisível p/ largar."},
   {"ic":"spark","law":"2ª Lei · Torne Atraente","lbl":"O Desejo",
    "exp":"A <b>antecipação</b> da recompensa — é ela que motiva, não a ação."},
   {"ic":"steps","law":"3ª Lei · Torne Fácil","lbl":"A Resposta",
    "exp":"O hábito feito. Vence o <b>menor atrito</b> — frequência &gt; intensidade."},
   {"ic":"key","law":"4ª Lei · Torne Satisfatório","lbl":"A Recompensa",
    "exp":"O prazer <b>imediato</b> fecha o loop e ensina o cérebro a repetir."},
 ],
 "practice": {"kicker":"Na prática · a regra dos 2 minutos","ic":"clock",
   "text":"Comece pela versão <b>≤ 2 minutos</b> do hábito (“ler” = 1 página). "
          "Domine a arte de aparecer; escale depois."},
}

CHAPTERS = [
 {"slug":"ch01-1porcento-sistemas","sub":"CAPÍTULO 1: O 1% e os Sistemas",
  "intro":"Resultados extraordinários não vêm de uma virada heroica, mas do acúmulo de pequenas melhoras. E o que decide o progresso não é a meta — é o sistema que você repete.",
  "cards":[
      {"ic":"spark","t":"Os Juros Compostos do Comportamento","emph":"Juros Compostos","b":"<strong>1% melhor a cada dia ≈ 37×</strong> em um ano; 1% pior tende a zero. O hábito é a unidade que compõe — para o bem ou para o mal.","tip":"<strong>Modelo mental:</strong> importa a trajetória do 1%, não o ponto de hoje."},
      {"ic":"pivot","t":"Sistemas > Metas","emph":"Sistemas > Metas","b":"\"Você não sobe ao nível das suas metas — <strong>cai ao nível dos seus sistemas</strong>.\" Vencedores e perdedores têm as mesmas metas; o que difere é o sistema diário.","tip":"<strong>Como aplicar:</strong> projete o sistema; deixe a meta ser subproduto."},
      {"ic":"clock","t":"O Platô do Potencial Latente","emph":"Potencial Latente","b":"O progresso fica invisível antes de aparecer — o <strong>vale da decepção</strong>. Como o gelo que só derrete ao cruzar zero grau: persistir é cruzar o platô.","tip":"<strong>Cuidado:</strong> abandonar no vale, às vésperas do platô virar, é o erro mais comum.","warn":True},
    ],
  "lessons_title":"Lições-Chave do Capítulo 1",
  "lessons":["Projete o sistema diário; a meta vem como consequência.","O 1% compõe — para os dois lados.","Persista no vale da decepção: o platô está prestes a virar."]},

 {"slug":"ch02-identidade","sub":"CAPÍTULO 2: Hábitos e Identidade",
  "intro":"A mudança duradoura não começa no resultado, e sim na identidade. Cada hábito é um voto no tipo de pessoa que você quer se tornar.",
  "cards":[
      {"ic":"layers","t":"Os Três Níveis","emph":"Três Níveis","b":"<strong>Resultados → processos → identidade.</strong> A maioria muda de fora para dentro; o durável é de dentro para fora — começa por quem você crê ser.","tip":"<strong>Como aplicar:</strong> decida que tipo de pessoa quer ser e prove com pequenas ações.","wide":True},
      {"ic":"key","t":"Cada Hábito é um Voto","emph":"Voto","b":"Ler uma página é um voto em \"sou um leitor\". A meta não é correr uma maratona — é <strong>tornar-se um corredor</strong>. A prova acumulada reescreve a autoimagem.","tip":"<strong>Regra:</strong> colete votos, não perfeição — não precisa de maioria absoluta."},
      {"ic":"mask","t":"A Identidade que Aprisiona","emph":"Aprisiona","b":"\"Sou desorganizado\", \"sou ruim de número\" — uma identidade rígida vira <strong>profecia autorrealizável</strong>. Segure suas identidades de forma leve.","tip":"<strong>Sinal de alerta:</strong> quando a autoimagem trava a mudança, ela virou jaula.","warn":True},
    ],
  "lessons_title":"Lições-Chave do Capítulo 2",
  "lessons":["Mude de dentro para fora: comece pela identidade.","Cada ação é um voto em quem você se torna.","Segure as identidades de forma leve."]},

 {"slug":"ch03-loop-do-habito","sub":"CAPÍTULO 3: O Loop do Hábito",
  "intro":"Todo hábito segue um ciclo de quatro estágios. Entendê-lo dá o mapa — e para cada estágio há uma lei que cria ou quebra o comportamento.",
  "cards":[
      {"ic":"spiral","t":"Os Quatro Estágios","emph":"Quatro Estágios","b":"<strong>Deixa → Desejo → Resposta → Recompensa.</strong> A deixa dispara, o desejo motiva, a resposta executa, a recompensa satisfaz e <strong>ensina</strong> o cérebro a repetir.","tip":"<strong>Como aplicar:</strong> hábito que não pega? veja qual dos 4 estágios falhou.","wide":True},
      {"ic":"target","t":"Você Não Deseja o Hábito","emph":"Não Deseja o Hábito","b":"Você deseja a <strong>mudança de estado</strong> que ele promete — não a ação em si. O cigarro não é o desejo; o alívio é.","tip":"<strong>Modelo mental:</strong> mude a recompensa esperada e muda o desejo."},
      {"ic":"gap","t":"Problema vs. Solução","emph":"Problema vs. Solução","b":"Deixa + desejo = a fase do <strong>problema</strong>; resposta + recompensa = a <strong>solução</strong>. Hábitos resolvem problemas recorrentes com o mínimo de energia.","tip":"<strong>Regra:</strong> não ataque só a força de vontade (a resposta) — use a lei do estágio certo."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 3",
  "lessons":["Mapeie os 4 estágios do hábito que quer mudar.","O desejo é pela mudança de estado, não pela ação.","Use a lei do estágio certo — não tente vencer tudo na resposta."]},

 {"slug":"ch04-lei1-obvio","sub":"CAPÍTULO 4: 1ª Lei — Torne Óbvio",
  "intro":"Você não decide a maioria dos hábitos — eles disparam por deixas do ambiente. Tornar a deixa óbvia (ou invisível, para o mau hábito) é a primeira alavanca.",
  "cards":[
      {"ic":"eye","t":"Pontuação e Intenção","emph":"Pontuação e Intenção","b":"<strong>Pontuação de hábitos</strong> (liste e marque +/–/=): a consciência vem antes da mudança. <strong>Intenção de implementação</strong> — \"vou [hábito] às [hora] em [local]\".","tip":"<strong>Como aplicar:</strong> datar e localizar o hábito dobra a adesão."},
      {"ic":"link","t":"Empilhamento de Hábitos","emph":"Empilhamento","b":"Ancore o novo num que já existe — \"<strong>depois de [hábito atual], vou [novo hábito]</strong>\". A rotina antiga vira a deixa da nova.","tip":"<strong>Exemplo:</strong> \"depois de fazer o café, leio uma página\"."},
      {"ic":"pin","t":"O Ambiente Vence a Vontade","emph":"Ambiente Vence a Vontade","b":"Deixas do bom hábito <strong>visíveis</strong>; do mau, escondidas. O ambiente é constante; a força de vontade é finita. Cada espaço, um uso.","tip":"<strong>Regra:</strong> para largar um mau hábito, torne a deixa invisível — não resista a ela."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 4",
  "lessons":["Escreva a intenção de implementação do hábito.","Empilhe-o num hábito existente e deixe a deixa à vista.","Engenheire o ambiente em vez de gastar força de vontade."]},

 {"slug":"ch05-lei2-atraente","sub":"CAPÍTULO 5: 2ª Lei — Torne Atraente",
  "intro":"Agimos pelo desejo — a expectativa da recompensa, não a recompensa em si. Quanto mais atraente a oportunidade, mais provável vira hábito.",
  "cards":[
      {"ic":"spark","t":"Agrupamento de Tentação","emph":"Agrupamento de Tentação","b":"Junte algo que você <strong>quer</strong> fazer com algo que <strong>precisa</strong> fazer — \"só vejo a série na esteira\". O desejo de um puxa o outro.","tip":"<strong>Como aplicar:</strong> emparelhe o hábito necessário com um prazer imediato."},
      {"ic":"bubble","t":"As Normas do Grupo","emph":"Normas do Grupo","b":"Copiamos os <strong>próximos</strong> (família/amigos), os <strong>muitos</strong> (a maioria) e os <strong>poderosos</strong> (status). Entre na tribo onde o seu hábito já é o normal.","tip":"<strong>Regra:</strong> pertencimento vence lógica — escolha a cultura, não só o hábito.","wide":True},
      {"ic":"bulb","t":"Reformule a Mente","emph":"Reformule","b":"Troque \"<strong>tenho que</strong>\" por \"<strong>tenho a oportunidade de</strong>\". A associação emocional da deixa muda o desejo.","tip":"<strong>Modelo mental:</strong> o pico de dopamina vem na antecipação, antes da recompensa."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 5",
  "lessons":["Agrupe o hábito necessário com algo prazeroso.","Escolha a tribo onde ele já é normal.","Reformule a linguagem interna: oportunidade, não obrigação."]},

 {"slug":"ch06-lei3-facil","sub":"CAPÍTULO 6: 3ª Lei — Torne Fácil",
  "intro":"O que decide o hábito é a frequência, não o tempo — e a frequência vem da facilidade. Não é sobre intensidade, é sobre aparecer.",
  "cards":[
      {"ic":"leaf","t":"A Lei do Menor Esforço","emph":"Menor Esforço","b":"O cérebro escolhe o caminho de <strong>menor atrito</strong>. Reduza o atrito do bom hábito e aumente o do mau — o ambiente faz o trabalho.","tip":"<strong>Como aplicar:</strong> −atrito no bom, +atrito no mau (tire a bateria do controle)."},
      {"ic":"clock","t":"A Regra dos 2 Minutos","emph":"2 Minutos","b":"Toda nova rotina começa numa versão de <strong>≤ 2 minutos</strong> — \"ler\" = ler uma página; \"treinar\" = calçar o tênis. Domine a <strong>arte de aparecer</strong>; escale depois.","tip":"<strong>Regra:</strong> padronize antes de otimizar — primeiro o hábito existe, depois cresce.","wide":True},
      {"ic":"steps","t":"Compromisso e Automação","emph":"Automação","b":"Decisões únicas que <strong>travam o futuro</strong> — débito automático para poupar, deletar o app. Um esforço hoje, o comportamento certo por meses.","tip":"<strong>Modelo mental:</strong> facilite o começo; a inércia inicial é o maior obstáculo."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 6",
  "lessons":["Reduza o atrito do bom hábito a quase zero.","Comece na versão de 2 minutos; só escale depois.","Automatize e comprometa-se para travar o futuro."]},

 {"slug":"ch07-lei4-satisfatorio","sub":"CAPÍTULO 7: 4ª Lei — Torne Satisfatório",
  "intro":"O que é recompensado de imediato se repete. O problema do bom hábito é que sua recompensa costuma ser tardia — então é preciso fabricar satisfação imediata.",
  "cards":[
      {"ic":"key","t":"Recompensa Imediata","emph":"Imediata","b":"O cérebro prioriza o presente; a recompensa tardia perde para a tentação imediata. Anexe uma <strong>pequena gratificação</strong> ao fim do hábito — coerente com a identidade desejada.","tip":"<strong>Como aplicar:</strong> feche o loop com prazer imediato, senão o bom hábito morre de tédio."},
      {"ic":"steps","t":"O Rastreador de Hábitos","emph":"Rastreador","b":"Marcar \"feito\" é satisfatório e visual — \"<strong>não quebre a corrente</strong>\". O que se mede e se vê progredir, se mantém.","tip":"<strong>Regra:</strong> a própria corrente vira a recompensa e o jogo."},
      {"ic":"target","t":"Nunca Falhe Duas Vezes","emph":"Duas Vezes","b":"Errar uma vez é acidente; <strong>duas seguidas</strong> é o início de um novo (mau) hábito. Recompor rápido vale mais que ser perfeito.","tip":"<strong>Sinal de alerta:</strong> \"já que falhei, desisto\" é a armadilha — só não falhe de novo.","warn":True},
    ],
  "lessons_title":"Lições-Chave do Capítulo 7",
  "lessons":["Dê ao hábito uma recompensa imediata coerente com a identidade.","Use um rastreador; proteja a corrente.","Falhou? Volte já — nunca duas vezes seguidas."]},

 {"slug":"ch08-avancado","sub":"CAPÍTULO 8: Avançado — Manter e Dominar",
  "intro":"Saber as quatro leis não basta; manter exige escolher o jogo certo, calibrar a dificuldade e revisar para não cair no piloto automático cego.",
  "cards":[
      {"ic":"mountain","t":"O Jogo Certo + Cachinhos Dourados","emph":"Jogo Certo","b":"Genes e aptidões inclinam o tabuleiro — jogue onde sua natureza favorece. E a <strong>Regra de Cachinhos Dourados</strong>: motivação no pico quando o desafio está <strong>no limite</strong> da capacidade (nem fácil, nem impossível).","tip":"<strong>Como aplicar:</strong> ajuste a dificuldade ao seu limite para manter o engajamento.","wide":True},
      {"ic":"eye","t":"O Lado Sombrio dos Hábitos","emph":"Lado Sombrio","b":"A automaticidade cria <strong>platôs</strong>: você repete sem melhorar. Hábito + prática deliberada — automatize o básico e direcione a atenção à próxima fronteira.","tip":"<strong>Cuidado:</strong> piloto automático cego para de crescer.","warn":True},
      {"ic":"pivot","t":"Revisão e Reflexão","emph":"Revisão e Reflexão","b":"Revisões periódicas evitam que o hábito siga no automático longe do objetivo e reavaliam a identidade. <strong>Apaixonar-se pelo tédio</strong> é o que separa o profissional do amador.","tip":"<strong>Regra:</strong> o profissional aparece mesmo sem novidade; o amador só com motivação."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 8",
  "lessons":["Jogue onde sua natureza favorece; ajuste o desafio ao limite.","Hábito + prática deliberada cruza o platô da automaticidade.","Revise periodicamente; apaixone-se pelo tédio."]},
]
