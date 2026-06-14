# -*- coding: utf-8 -*-
"""Conteúdo (pt-BR) das páginas da biblioteca para a linguística textual de
Beaugrande & Dressler (Introduction to Text Linguistics) + os mecanismos de
coesão de Halliday & Hasan. Os 7 critérios de textualidade e as 5 coesões."""

BOOK = {
 "title": "Coesão e Coerência",
 "author": "Beaugrande, Dressler & Halliday",
 "header_light": "COESÃO E",
 "header_bold": "COERÊNCIA",
 "subtitle": "VISÃO GERAL · OS 7 CRITÉRIOS DA TEXTUALIDADE",
 "intro": "O que faz de um conjunto de frases um texto? Beaugrande & Dressler respondem com sete critérios de textualidade — e Halliday & Hasan detalham os cinco mecanismos que amarram a superfície. Um texto não é frase grande: é uma ocorrência comunicativa que precisa se conectar (coesão), fazer sentido (coerência) e funcionar numa situação real. É a régua para diagnosticar por que um texto não fecha.",
 "description": "A linguística textual de Beaugrande & Dressler (os 7 critérios de textualidade) e os 5 mecanismos de coesão de Halliday & Hasan: coesão, coerência, intencionalidade, aceitabilidade, informatividade, situacionalidade e intertextualidade.",
 "tags": ["Língua", "Texto", "Redação"],
 "progress": "9 Capítulos",
 "cover": "assets/coesao-coerencia-cover.png",
 "overview_cards": [
   {"ic":"layers","t":"Os 7 Critérios de Textualidade","b":"Um texto só é texto se cumpre sete critérios — <strong>coesão</strong> e <strong>coerência</strong> (no texto) + <strong>intencionalidade, aceitabilidade, informatividade, situacionalidade e intertextualidade</strong> (no uso). Falhou um, não fecha.","tip":"<strong>Como aplicar:</strong> quando um texto 'não soa como texto', pergunte qual dos sete falhou.","wide":True},
   {"ic":"link","t":"Coesão = superfície · Coerência = sentido","b":"A <strong>coesão</strong> liga as palavras visíveis (pronomes, conectores, repetições); a <strong>coerência</strong> liga as ideias na mente do leitor. Pode haver uma sem a outra.","tip":"<strong>Chave:</strong> a coerência é a prova final — acima da gramática."},
   {"ic":"key","t":"Os 5 Mecanismos de Coesão","b":"<strong>Referência</strong> (ele, este), <strong>substituição</strong> (outro), <strong>elipse</strong> (omitir o recuperável), <strong>conjunção</strong> (mas, porque) e <strong>coesão lexical</strong> (sinônimo, campo semântico).","tip":"<strong>Modelo mental:</strong> o pronome ambíguo é o defeito nº 1."},
 ],
}

CHAPTERS = [
 {"slug":"ch01-textualidade","sub":"CAPÍTULO 1: O Que É Um Texto — Os 7 Critérios",
  "intro":"Texto não é frase grande nem amontoado de orações — é uma ocorrência comunicativa que só conta como texto se cumpre sete critérios de textualidade.",
  "cards":[
   {"ic":"layers","t":"Os 7 critérios","b":"<strong>Coesão</strong> (superfície) e <strong>coerência</strong> (sentido) são centrados no texto; <strong>intencionalidade, aceitabilidade, informatividade, situacionalidade e intertextualidade</strong> são centrados no uso.","tip":"<strong>Como aplicar:</strong> cada critério é uma condição — a falha de um compromete o todo.","wide":True},
   {"ic":"bubble","t":"Ocorrência comunicativa","b":"O texto <strong>acontece numa situação real</strong>, com alguém querendo dizer algo a alguém. Avalie-o pela comunicação que realiza, não pela gramática isolada.","tip":"<strong>Modelo mental:</strong> texto é evento, não objeto."},
   {"ic":"gap","t":"Gramática ≠ textualidade","b":"Frases corretas e <strong>desconexas</strong> não fazem um texto. Avaliar o texto fora da situação mede só metade.","tip":"<strong>Cuidado:</strong> não busque perfeição nos sete — eles se equilibram.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 1",
  "lessons":["Texto é ocorrência comunicativa, não frase grande.","7 critérios: coesão e coerência (no texto) + 5 centrados no uso.","Quando um texto não fecha, diagnostique qual critério falhou."]},

 {"slug":"ch02-coesao-referencia","sub":"CAPÍTULO 2: Coesão I — Referência, Substituição, Elipse",
  "intro":"Os três primeiros mecanismos de coesão funcionam por economia e retomada — apontar, encurtar ou omitir em vez de repetir.",
  "cards":[
   {"ic":"link","t":"Referência","b":"Uma forma que <strong>aponta</strong> para outro elemento em vez de nomeá-lo de novo — pronomes, demonstrativos, artigos. <strong>Anafórica</strong> (aponta para trás) ou <strong>catafórica</strong> (para frente).","tip":"<strong>Como aplicar:</strong> todo pronome é uma promessa de antecedente claro.","wide":True},
   {"ic":"pivot","t":"Substituição e elipse","b":"<strong>Substituição</strong> troca um item por forma curta ('outra'); <strong>elipse</strong> omite o recuperável ('Eu [quero]') — a substituição por zero.","tip":"<strong>Modelo mental:</strong> só funcionam se o leitor reconstrói sem esforço."},
   {"ic":"gap","t":"Pronome ambíguo","b":"'João disse a Pedro que <strong>ele</strong> errou' — quem? A ambiguidade referencial é o defeito de coesão <strong>mais comum</strong>.","tip":"<strong>Cuidado:</strong> referência distante demais faz o leitor perder o fio.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 2",
  "lessons":["Referência aponta; substituição troca por forma curta; elipse omite o recuperável.","A cadeia referencial mantém o assunto vivo; pronome ambíguo é o defeito nº 1.","Retomar economiza — só enquanto o leitor recupera o referente."]},

 {"slug":"ch03-coesao-conjuncao-lexical","sub":"CAPÍTULO 3: Coesão II — Conjunção e Coesão Lexical",
  "intro":"Os outros dois mecanismos amarram por relação lógica (conjunção) e por escolha de palavras (coesão lexical).",
  "cards":[
   {"ic":"steps","t":"Conjunção (conectores)","b":"As expressões que <strong>sinalizam a relação</strong> — aditiva (e), adversativa (mas), causal (porque), temporal (então), conclusiva (portanto). O conectivo é a placa de trânsito do raciocínio.","tip":"<strong>Como aplicar:</strong> o conectivo é a seta do raciocínio — confirma, contradiz ou conclui.","wide":True},
   {"ic":"constellation","t":"Coesão lexical","b":"Amarração pelo vocabulário — <strong>reiteração</strong> (repetir, sinônimo, hiperônimo) e <strong>colocação</strong> (palavras do mesmo <strong>campo semântico</strong> que coocorrem).","tip":"<strong>Modelo mental:</strong> as palavras de um texto devem 'se conhecer'."},
   {"ic":"gap","t":"Conectivo errado ou demais","b":"'mas' onde a relação é causal, ou 'portanto' sem premissa, <strong>desorienta</strong>. Excesso de 'aí/então/daí' vira ruído.","tip":"<strong>Cuidado:</strong> trocar de campo semântico sem transição faz o texto 'pular de assunto'.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 3",
  "lessons":["Conjunção sinaliza a relação (aditiva, adversativa, causal, temporal, conclusiva).","Coesão lexical amarra por reiteração e colocação (campo semântico).","Conectivo errado ou em excesso desorienta tanto quanto a falta dele."]},

 {"slug":"ch04-coerencia","sub":"CAPÍTULO 4: Coerência — A Continuidade de Sentidos",
  "intro":"Se a coesão amarra a superfície, a coerência amarra o sentido — a continuidade que faz o leitor construir um mundo textual estável.",
  "cards":[
   {"ic":"constellation","t":"Mundo textual e inferência","b":"A coerência é a <strong>estabilidade</strong> dos conceitos que o texto ativa na mente — sem contradições nem buracos. Muito dela é construído por <strong>inferência</strong>, não escrito.","tip":"<strong>Como aplicar:</strong> a coerência mora na cabeça do leitor; o texto dá as pistas.","wide":True},
   {"ic":"layers","t":"Esquemas, frames e scripts","b":"Estruturas de conhecimento (o 'roteiro do restaurante') que o texto <strong>evoca</strong> e o leitor usa — economia: não é preciso explicar o óbvio.","tip":"<strong>Modelo mental:</strong> sentido é uma rede, não uma fila."},
   {"ic":"gap","t":"Salto lógico e contradição","b":"Pular uma etapa que o leitor <strong>não infere</strong> abre um buraco; afirmar o que choca com o mundo textual gera ruído.","tip":"<strong>Cuidado:</strong> coeso e incoerente existe — a coerência é a prova final.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 4",
  "lessons":["Coerência é a continuidade de sentidos — a estabilidade do mundo textual.","É coconstruída por inferência, usando esquemas do leitor.","Coesão não garante coerência; o sentido é a prova final."]},

 {"slug":"ch05-intencionalidade-aceitabilidade","sub":"CAPÍTULO 5: Intencionalidade e Aceitabilidade",
  "intro":"Os critérios centrados nas pessoas: a intenção do produtor e a aceitação do receptor. Texto é um pacto entre os dois.",
  "cards":[
   {"ic":"target","t":"Intencionalidade","b":"A intenção do produtor de que aquilo <strong>conte como texto</strong> coeso e coerente e sirva a um plano — informar, persuadir, emocionar. O texto é instrumento de um objetivo.","tip":"<strong>Como aplicar:</strong> texto sem propósito visível é abandonado.","wide":True},
   {"ic":"bubble","t":"Aceitabilidade","b":"A disposição do receptor de <strong>cooperar</strong> — preencher lacunas, tolerar pequenas falhas — desde que perceba relevância e utilidade.","tip":"<strong>Modelo mental:</strong> texto é cooperação, não transmissão."},
   {"ic":"gap","t":"Ignorar o destinatário","b":"Escrever para si, não para quem recebe, derruba a aceitabilidade. Abusar da cooperação (defeitos demais) faz o leitor <strong>parar de colaborar</strong>.","tip":"<strong>Cuidado:</strong> a mesma mensagem muda de forma conforme quem recebe.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 5",
  "lessons":["Intencionalidade: o produtor quer um texto com propósito.","Aceitabilidade: o receptor coopera se vê relevância e utilidade.","Texto é pacto cooperativo — calibre-o para quem vai aceitar."]},

 {"slug":"ch06-informatividade","sub":"CAPÍTULO 6: Informatividade",
  "intro":"Um texto equilibra o esperado e o inesperado. Pouca informatividade entedia; muita exige esforço demais.",
  "cards":[
   {"ic":"scale","t":"As três ordens","b":"<strong>1ª ordem</strong> — trivial, entedia. <strong>2ª ordem</strong> — o equilíbrio ideal, informa sem sobrecarregar. <strong>3ª ordem</strong> — inesperado a ponto de exigir grande esforço (arriscado).","tip":"<strong>Como aplicar:</strong> mire a 2ª ordem; o tédio e o caos são vizinhos do fracasso.","wide":True},
   {"ic":"spark","t":"Surpresa motivada","b":"A quebra de expectativa funciona quando o leitor <strong>encontra a razão</strong> dela. Surpreenda, mas dê a chave.","tip":"<strong>Modelo mental:</strong> o esperado garante compreensão; o novo garante interesse."},
   {"ic":"gap","t":"Óbvio ou denso demais","b":"Dizer o que o público já sabe (1ª) faz pular; empilhar novidade sem âncora (3ª) faz <strong>se perder</strong>.","tip":"<strong>Cuidado:</strong> densidade plana, sem picos, não cria interesse.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 6",
  "lessons":["Informatividade equilibra esperado e novo; o alvo é a 2ª ordem.","1ª ordem entedia; 3ª ordem não motivada afasta.","Surpresa funciona quando é motivada — o leitor acha a razão."]},

 {"slug":"ch07-situacionalidade","sub":"CAPÍTULO 7: Situacionalidade",
  "intro":"Nenhum texto existe no vácuo. A situacionalidade é a relevância do texto para a situação em que ocorre.",
  "cards":[
   {"ic":"pin","t":"O contexto é metade do texto","b":"Os fatores que tornam o texto <strong>relevante</strong> ao contexto. O contexto carrega sentido que as palavras não precisam repetir e define o que pode ficar implícito.","tip":"<strong>Como aplicar:</strong> 'Cuidado, degrau' é texto completo na situação — fora dela, fragmento.","wide":True},
   {"ic":"pivot","t":"Monitorar vs. gerenciar","b":"O texto pode só <strong>descrever</strong> a situação (monitorar) ou <strong>agir para mudá-la</strong> (gerenciar — uma ordem, um pedido, uma persuasão).","tip":"<strong>Modelo mental:</strong> texto certo, lugar errado, é texto errado."},
   {"ic":"gap","t":"Ignorar o suporte","b":"Escrever para o YouTube como se fosse ensaio acadêmico é <strong>desajuste de situação</strong>. Repetir o que o contexto já diz é ruído.","tip":"<strong>Cuidado:</strong> texto irrelevante à situação falha mesmo sendo coeso e coerente.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 7",
  "lessons":["Situacionalidade é a relevância do texto para o contexto.","O contexto carrega sentido e exige adequação ao canal.","Texto irrelevante à situação falha mesmo coeso e coerente."]},

 {"slug":"ch08-intertextualidade","sub":"CAPÍTULO 8: Intertextualidade",
  "intro":"Todo texto se apoia em outros. Entendemos um texto novo porque já vimos textos parecidos.",
  "cards":[
   {"ic":"link","t":"O texto depende de textos","b":"Os fatores que fazem o uso de um texto depender do <strong>conhecimento de outros</strong>. Nenhum texto começa do zero — herda formas e expectativas.","tip":"<strong>Como aplicar:</strong> aludir ao que o público conhece economiza; ao obscuro, quebra a ponte.","wide":True},
   {"ic":"book","t":"Gêneros = contrato prévio","b":"Reconhecer o gênero (notícia, receita, resumo) <strong>ativa expectativas</strong> que guiam produtor e receptor — intertextualidade institucionalizada.","tip":"<strong>Modelo mental:</strong> o gênero é metade da compreensão antes da 1ª palavra."},
   {"ic":"gap","t":"Clichê e alusão obscura","b":"Repetir fórmulas sem perceber gera previsibilidade (1ª ordem); referir um texto que o público não conhece <strong>não forma a ponte</strong>.","tip":"<strong>Cuidado:</strong> quebrar o gênero pode encantar (surpresa motivada) ou frustrar.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 8",
  "lessons":["Intertextualidade: o texto depende do conhecimento de outros textos.","O gênero é intertextualidade institucionalizada — ativa expectativas.","Aludir ao conhecido economiza; ao obscuro, quebra a ponte."]},

 {"slug":"ch09-principios-regulativos","sub":"CAPÍTULO 9: Os Princípios Regulativos",
  "intro":"Os critérios dizem o que faz um texto ser texto; os princípios regulativos dizem como produzi-lo bem.",
  "cards":[
   {"ic":"scale","t":"Eficiência × Efetividade → Adequação","b":"<strong>Eficiência</strong> = mínimo esforço (mas, só, entedia). <strong>Efetividade</strong> = forte impressão (mas, só, cansa). <strong>Adequação</strong> = o equilíbrio calibrado à situação.","tip":"<strong>Como aplicar:</strong> eficiência poupa; efetividade marca; adequação decide.","wide":True},
   {"ic":"pivot","t":"Otimizar, não maximizar","b":"Não se <strong>maximiza</strong> um critério — otimiza-se o conjunto. Maximizar um sempre custa outro.","tip":"<strong>Modelo mental:</strong> o alvo é o ponto ótimo, não o extremo."},
   {"ic":"gap","t":"Só fluência ou só impacto","b":"100% eficiente = fluente e <strong>esquecível</strong>; 100% efetivo = impactante e <strong>exaustivo</strong>. Os dois extremos falham.","tip":"<strong>Cuidado:</strong> o equilíbrio certo muda com gênero, canal e público.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 9",
  "lessons":["Três princípios: eficiência (esforço), efetividade (impacto), adequação (equilíbrio).","Fluência e impacto se opõem; a adequação arbitra conforme a situação.","Otimize o conjunto dos critérios — nunca maximize um só."]},
]
