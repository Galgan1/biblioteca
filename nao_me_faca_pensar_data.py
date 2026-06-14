# -*- coding: utf-8 -*-
"""Conteúdo (pt-BR) das páginas da biblioteca para 'Não Me Faça Pensar'
(Steve Krug — Don't Make Me Think: A Common Sense Approach to Web Usability).
Frameworks canônicos: a 1ª Lei de Krug ('não me faça pensar' / auto-evidência);
como realmente usamos a web (escanear, satisficing/satisfazer, muddling
through/se virar); design para escaneabilidade (billboard design 101 —
convenções, hierarquia visual, áreas claras, clicável óbvio, eliminar ruído);
'omita as palavras desnecessárias' (corte metade, depois metade do resto;
happy talk); navegação persistente (Site ID, seções, 'você está aqui', busca);
o teste do tronco (trunk test); a página inicial e o mito da home perfeita;
o mito do usuário médio e o teste de usabilidade barato (3 usuários, uma manhã
por mês, pensar em voz alta); a reserva de boa vontade (reservoir of goodwill);
acessibilidade e design para celular. Base: síntese dos frameworks amplamente
documentados — não reproduz o texto."""

BOOK = {
 "title": "Não Me Faça Pensar",
 "author": "Steve Krug",
 "header_light": "NÃO ME",
 "header_bold": "FAÇA PENSAR",
 "subtitle": "VISÃO GERAL · USABILIDADE E O BOM SENSO NA WEB",
 "intro": "E se a regra de ouro da usabilidade coubesse numa frase? Steve Krug a resume assim: 'Não me faça pensar'. Uma página, um botão, um link — tudo deve ser auto-evidente, óbvio sem esforço. Porque as pessoas não leem, escaneiam; não escolhem a melhor opção, pegam a primeira razoável; não entendem o sistema, se viram. Não Me Faça Pensar é o bom senso aplicado ao design digital — e a prova de que boa usabilidade se descobre testando, não discutindo.",
 "description": "O clássico mais influente da usabilidade web, de Steve Krug. Em vez de um manual técnico, é um guia de bom senso: reduza a carga cognitiva, aproveite as convenções, deixe óbvio o que é clicável, corte as palavras desnecessárias e dê ao usuário uma navegação que sempre responde 'onde estou?' e 'como volto?'. Krug demole o mito do 'usuário médio' e da home perfeita, e mostra como um teste de usabilidade barato — três pessoas, uma manhã por mês — resolve discussões com evidência. No centro de tudo, a reserva de boa vontade do usuário: cada atrito a esvazia, cada cortesia a reabastece.",
 "tags": ["Usabilidade", "UX", "Web"],
 "progress": "10 Capítulos Completos",
 "cover": "assets/nao-me-faca-pensar-cover.png",
 "overview_cards": [
   {"ic":"bulb","t":"A 1ª Lei: \"Não Me Faça Pensar\"","b":"A regra-mestra da usabilidade: cada página deve ser <strong>auto-evidente</strong> — óbvia sem deliberação. Todo <strong>'ponto de interrogação' na cabeça</strong> do usuário ('isto é clicável?', 'onde estou?') é um imposto sobre a atenção. A escala: auto-evidente (ideal) > autoexplicativo (aceitável) > confuso (inaceitável).","tip":"<strong>Como aplicar:</strong> olhe cada tela e pergunte 'isto gera alguma dúvida?'. Cada dúvida é um defeito a eliminar.","wide":True},
   {"ic":"eye","t":"Como REALMENTE Usamos a Web","b":"Projetamos para um leitor ideal que não existe. Na prática: <strong>escaneamos</strong> (não lemos), <strong>satisfazemos</strong> (pegamos a primeira opção razoável, não a melhor — <em>satisficing</em>) e <strong>nos viramos</strong> (usamos sem entender o sistema — <em>muddling through</em>).","tip":"<strong>Modelo mental:</strong> a página é um outdoor lido de relance, a 100 km/h. Destaque a ação certa e torne tudo à prova de erro.","wide":True},
   {"ic":"target","t":"Teste Barato, e a Boa Vontade","b":"Não existe 'usuário médio': resolva discussões testando — <strong>3 usuários, uma manhã por mês</strong>, pensando em voz alta. E lembre da <strong>reserva de boa vontade</strong>: cada atrito esvazia a paciência do usuário; cada cortesia a reabastece.","tip":"<strong>Regra:</strong> pare de discutir 'o que o usuário faria' — uma manhã de teste vale mais que semanas de opinião."},
 ],
}

CHAPTERS = [
 {"slug":"ch01-nao-me-faca-pensar","sub":"CAPÍTULO 1: Não Me Faça Pensar (a 1ª Lei)",
  "intro":"A primeira lei da usabilidade de Steve Krug: 'Não me faça pensar'. Cada página, botão ou link deve ser auto-evidente — óbvio, exigindo o mínimo de esforço cognitivo. Quando o usuário precisa parar para descobrir como algo funciona, você já o perdeu um pouco.",
  "cards":[
   {"ic":"bulb","t":"A 1ª Lei de Krug","b":"A página deve ser <strong>auto-evidente</strong>: o usuário 'entende' sem deliberar. Cada elemento que provoca um <strong>ponto de interrogação na cabeça</strong> ('isto é clicável?', 'começo por onde?') cobra um pequeno imposto de atenção. A meta é tornar o uso óbvio, não esperto.","tip":"<strong>Como aplicar:</strong> revise cada tela perguntando 'isto gera alguma dúvida?'. Cada dúvida é um ponto a corrigir.","wide":True},
   {"ic":"scale","t":"Auto-evidente > Autoexplicativo > Confuso","b":"Mire no <strong>auto-evidente</strong> (captado à primeira vista). Aceite o <strong>autoexplicativo</strong> (exige um pouco de pensamento, mas a explicação está ali) só quando for inevitável, em telas complexas. <strong>Confuso / precisa de instrução</strong> é inaceitável.","tip":"<strong>Modelo mental:</strong> a página é um outdoor passando a 100 km/h — precisa ser 'pega' num relance."},
   {"ic":"gap","t":"Nomes Criativos no Lugar de Rótulos Óbvios","b":"Chamar 'Vagas' de 'Jobs!' ou 'Produtos' de 'Soluções' força o usuário a <strong>decodificar</strong>. Nomes de marketing 'fofos' geram interrogações; rótulos comuns são entendidos sem pensar.","tip":"<strong>Sinal de alerta:</strong> se um rótulo exige tradução mental, ele falha na 1ª Lei. Prefira o óbvio ao criativo.","warn":True},
  ],
  "lessons_title":"Lições-Chave: A 1ª Lei",
  "lessons":["Mire o auto-evidente: cada ponto de interrogação na cabeça do usuário é um defeito.","Use rótulos comuns e óbvios, não nomes criativos que exijam decodificação.","Minimizar a carga cognitiva é o objetivo número um de toda a interface."]},

 {"slug":"ch02-como-usamos-a-web","sub":"CAPÍTULO 2: Como Realmente Usamos a Web",
  "intro":"Projetamos pensando num usuário racional e atento que lê a página e escolhe a melhor opção. A realidade é o oposto: o usuário escaneia, se satisfaz com a primeira opção razoável e se vira sem entender como as coisas funcionam. Bom design parte desses três fatos.",
  "cards":[
   {"ic":"eye","t":"Não Lemos — Escaneamos","b":"O olho <strong>varre a página</strong> buscando palavras-âncora que combinem com o objetivo, em vez de ler frase a frase. Otimizar para o 'leitor cuidadoso' que para e pondera é desenhar para alguém que não existe.","tip":"<strong>Como aplicar:</strong> use hierarquia visual e palavras-chave que 'saltem' — desenhe para quem bate o olho, não para quem lê tudo.","wide":True},
   {"ic":"fork","t":"Satisficing (Satisfazer)","b":"Em vez da melhor opção, o usuário pega <strong>a primeira que parece servir</strong> (termo de Herbert Simon: <em>satisfy</em> + <em>suffice</em>). Procurar a ótima custa esforço, errar tem baixo custo (basta voltar) e adivinhar é até divertido.","tip":"<strong>Regra:</strong> faça a opção certa ser a mais saliente — o usuário vai clicar na primeira razoável, não na melhor escondida."},
   {"ic":"wave","t":"Muddling Through (Se Virar)","b":"O usuário <strong>usa sem entender o modelo</strong> do sistema; se funciona 'mais ou menos', ele segue e nunca descobre o jeito 'certo'. Contar que ele 'vá descobrir navegando' é apostar contra o comportamento real.","tip":"<strong>Cuidado:</strong> interfaces que quebram quando o usuário improvisa punem exatamente o jeito como as pessoas agem.","warn":True},
  ],
  "lessons_title":"Lições-Chave: Como Usamos a Web",
  "lessons":["Projete para quem escaneia, satisfaz e se vira — não para o leitor ideal.","Como o usuário pega a primeira opção razoável, faça a opção certa ser a mais saliente.","Como ele 'se vira', torne a interface à prova de erro e fácil de desfazer."]},

 {"slug":"ch03-design-escaneabilidade","sub":"CAPÍTULO 3: Design para Escaneabilidade (Billboard 101)",
  "intro":"Se o usuário escaneia, a página precisa ser construída para ser escaneada — o que Krug chama de billboard design 101: aproveitar convenções, criar hierarquia visual clara, dividir a página em áreas óbvias, deixar evidente o que é clicável e eliminar o ruído.",
  "cards":[
   {"ic":"layers","t":"Os 5 Movimentos do Billboard 101","b":"Desenhe a página como um outdoor: <strong>1) aproveite convenções</strong> (logo no topo-esquerda, carrinho à direita); <strong>2) crie hierarquia visual</strong> (importante = proeminente, relacionado = agrupado); <strong>3) divida em áreas claras</strong>; <strong>4) deixe óbvio o que é clicável</strong>; <strong>5) elimine o ruído</strong>.","tip":"<strong>Como aplicar:</strong> faça a aparência refletir a estrutura — o olho deve 'ler' a organização antes de ler as palavras.","wide":True},
   {"ic":"book","t":"Convenções > Inovação","b":"Padrões consagrados são processados <strong>sem esforço</strong> porque já foram aprendidos em mil outros sites. Inove apenas quando tiver certeza de que a nova forma é claramente melhor e tão óbvia quanto a convenção.","tip":"<strong>Modelo mental:</strong> convenções são vocabulário compartilhado — economizam o 'pensar' do usuário."},
   {"ic":"spark","t":"Eliminar o Ruído (Noise)","b":"Banners, animações e cores que competem entre si <strong>afogam o conteúdo</strong>. Há três tipos de ruído: barulho de fundo, bagunça e tagarelice visual. Cada elemento extra rouba atenção do que importa.","tip":"<strong>Cuidado:</strong> hierarquia plana (tudo do mesmo tamanho/peso) deixa o usuário sem saber por onde começar.","warn":True},
  ],
  "lessons_title":"Lições-Chave: Escaneabilidade",
  "lessons":["Use convenções; só inove quando a alternativa for claramente superior e tão óbvia.","Faça a aparência refletir a estrutura: importante = proeminente, relacionado = agrupado.","Deixe o clicável obviamente clicável e elimine sem dó o ruído visual."]},

 {"slug":"ch04-omita-palavras","sub":"CAPÍTULO 4: Omita as Palavras Desnecessárias",
  "intro":"A terceira lei de Krug: 'Omita as palavras desnecessárias' — corte metade das palavras de cada página, depois corte a metade do que sobrou. Texto enxuto reduz o ruído, destaca o conteúdo útil e encurta as páginas, fazendo o usuário pensar (e rolar) menos.",
  "cards":[
   {"ic":"steps","t":"A 3ª Lei: Corte pela Metade, Duas Vezes","b":"Adaptando Strunk & White à web: <strong>'livre-se de metade das palavras de cada página, depois livre-se de metade do que sobrou'</strong>. A maioria das páginas suporta esse corte sem perda de informação — só de ruído.","tip":"<strong>Como aplicar:</strong> seja um editor implacável; cada palavra deve justificar a própria presença ou sair.","wide":True},
   {"ic":"bubble","t":"Mate o Happy Talk","b":"O <strong>'blá-blá feliz'</strong> de boas-vindas e auto-promoção ('Bem-vindo ao nosso site! É um prazer recebê-lo...') não diz nada útil e ocupa o espaço nobre. É ruído puro: corte por inteiro.","tip":"<strong>Regra:</strong> se o texto não ajuda o usuário a agir, ele é candidato a corte."},
   {"ic":"gap","t":"Instruções São um Sintoma","b":"A maioria das instruções é <strong>ignorada</strong>. Em vez de explicar, torne as coisas tão óbvias que dispensem instrução; o que sobrar, reduza ao mínimo essencial, junto do ponto de uso.","tip":"<strong>Cuidado:</strong> precisar de instrução longa costuma significar que o design não está óbvio o bastante.","warn":True},
  ],
  "lessons_title":"Lições-Chave: Omitir Palavras",
  "lessons":["Corte metade das palavras, depois metade do que restou.","Elimine todo happy talk e a maioria das instruções.","Texto enxuto é menos ruído, mais destaque ao essencial e páginas mais curtas."]},

 {"slug":"ch05-navegacao-persistente","sub":"CAPÍTULO 5: Navegação Persistente",
  "intro":"Na web não há 'sensação de lugar' física; a navegação substitui as paredes e placas do mundo real. Ela precisa estar presente em toda página (persistente) e responder de imediato às perguntas tácitas: onde estou, o que tem aqui, como busco, como volto ao início.",
  "cards":[
   {"ic":"pin","t":"O \"Billboard de Navegação\"","b":"O núcleo que se repete em todas as páginas: <strong>Site ID</strong> (logo no topo, clicável, leva à home), <strong>Seções</strong> (navegação primária), <strong>'Você está aqui'</strong> (destaque da seção atual), <strong>Busca</strong> (caixa simples, sempre no mesmo lugar) e atalhos/utilitários.","tip":"<strong>Como aplicar:</strong> repita exatamente o mesmo núcleo de navegação em toda página, na mesma posição.","wide":True},
   {"ic":"pin","t":"Sempre Marque \"Você Está Aqui\"","b":"O usuário <strong>não chega pela home</strong> — entra fundo, por links do Google. Por isso precisa se localizar de qualquer ponto. O marcador 'você está aqui' (a seção atual destacada) e os breadcrumbs respondem 'onde estou?'.","tip":"<strong>Modelo mental:</strong> pense nas placas de um shopping — 'Você está aqui', mapa sempre no mesmo lugar."},
   {"ic":"link","t":"O Logo Leva à Home","b":"Convenção universal: clicar no <strong>Site ID volta ao começo</strong>. Navegação que muda de página para página, ou busca escondida atrás de filtros, desorienta e viola o satisficing.","tip":"<strong>Cuidado:</strong> navegação inconsistente entre páginas quebra a persistência e perde o usuário.","warn":True},
  ],
  "lessons_title":"Lições-Chave: Navegação Persistente",
  "lessons":["Repita a navegação central em toda página (ID, seções, 'você está aqui', busca, home).","Sempre marque 'você está aqui' — o usuário entra por qualquer porta.","O logo no topo leva à home; a busca é simples e fica sempre no mesmo lugar."]},

 {"slug":"ch06-teste-do-tronco","sub":"CAPÍTULO 6: O Teste do Tronco (Trunk Test)",
  "intro":"O teste do tronco é um diagnóstico rápido da navegação: imagine que você foi vendado, jogado no porta-malas (o 'tronco' do carro) e largado numa página qualquer e profunda do site. Ao 'abrir os olhos', você deve responder, sem pânico, às perguntas básicas de localização.",
  "cards":[
   {"ic":"lens","t":"As 6 Perguntas do Trunk Test","b":"Pegue uma página interna qualquer, isolada do contexto, e responda de relance: <strong>1)</strong> que site é este? (Site ID) <strong>2)</strong> em que página estou? (título) <strong>3)</strong> quais as seções principais? <strong>4)</strong> quais minhas opções neste nível? <strong>5)</strong> onde estou na hierarquia? ('você está aqui') <strong>6)</strong> como faço uma busca?","tip":"<strong>Como aplicar:</strong> abra uma página profunda fora de contexto e cheque os 6 itens em segundos — um veredito barato e honesto.","wide":True},
   {"ic":"key","t":"Cada Página É uma Porta de Entrada","b":"A maioria dos usuários <strong>não entra pela home</strong>: chega fundo, via busca e links. Logo, toda página deve <strong>se sustentar sozinha</strong> e responder às perguntas-âncora sem depender do caminho percorrido.","tip":"<strong>Modelo mental:</strong> não desenhe a jornada 'desde a home'; desenhe cada página como uma entrada autônoma."},
   {"ic":"gap","t":"Páginas Internas Sem Título","b":"Sem um <strong>título claro e proeminente</strong> (que bata com o link clicado e com o item destacado na navegação), o usuário não sabe onde está nem como subir um nível — falha imediata no trunk test.","tip":"<strong>Cuidado:</strong> navegação que só faz sentido se você 'veio da home' perde quem chega pelo meio.","warn":True},
  ],
  "lessons_title":"Lições-Chave: O Teste do Tronco",
  "lessons":["Aplique o trunk test a páginas internas profundas, fora de contexto.","Toda página deve responder sozinha: que site, que página, seções, opções, onde estou, como busco.","O usuário entra 'pelo meio' — cada página é uma porta de entrada autônoma."]},

 {"slug":"ch07-pagina-inicial","sub":"CAPÍTULO 7: A Página Inicial (Home)",
  "intro":"A home carrega expectativas impossíveis — todos querem espaço nela, e ela deve comunicar identidade, missão, hierarquia, e ainda oferecer atalhos e busca. O erro é tentar agradar a todos. A home tem uma missão central: dizer, em segundos, o que é o site e por que vale a pena.",
  "cards":[
   {"ic":"target","t":"Vença o \"Big Honkin' Question\"","b":"Nunca deixe o visitante sem resposta para <strong>'o que é este site?'</strong>. No espaço nobre (visível sem rolar), entregue uma <strong>tagline / proposta de valor</strong> concreta — 'o que é isto e por que eu deveria me importar?' — não happy talk genérico.","tip":"<strong>Como aplicar:</strong> troque 'Inovação que transforma' por algo concreto: 'Software de agendamento para clínicas — menos faltas, mais consultas'.","wide":True},
   {"ic":"scale","t":"As Tarefas que a Home Equilibra","b":"A home precisa cumprir, ao mesmo tempo: <strong>identidade e missão</strong>, <strong>hierarquia do site</strong> (as seções), <strong>busca</strong>, <strong>conteúdo em destaque/atalhos</strong> e <strong>registro/login</strong>. Nem tudo cabe no espaço nobre — priorize por trade-off.","tip":"<strong>Modelo mental:</strong> a home é a fachada e a vitrine da loja: num relance, diz o que vende e convida a entrar."},
   {"ic":"mask","t":"O Mito da Home Perfeita","b":"Tentar encaixar <strong>todas as prioridades de todos os stakeholders</strong> transforma a home num mural de banners que não diz o que o site é. A 'home perfeita' que agrada a todos resulta em ruído e mensagem diluída.","tip":"<strong>Cuidado:</strong> cada departamento 'pendurando' seu banner é o caminho mais curto para uma home que não comunica nada.","warn":True},
  ],
  "lessons_title":"Lições-Chave: A Página Inicial",
  "lessons":["A home deve responder 'o que é isto e por que me importar?' no espaço nobre, com uma frase de valor.","Não persiga a home perfeita que agrada a todos — priorize a missão central e faça trade-offs.","Troque happy talk e murais de banners por identidade, valor, seções e busca."]},

 {"slug":"ch08-teste-de-usabilidade","sub":"CAPÍTULO 8: Teste de Usabilidade Barato",
  "intro":"Debates de equipe sobre design são intermináveis porque cada um projeta para si mesmo e invoca 'o usuário médio' — que não existe. A saída é parar de discutir e testar: um teste de usabilidade barato, simples e frequente resolve as discussões com evidência, não com opinião.",
  "cards":[
   {"ic":"target","t":"A Fórmula do Teste Barato","b":"<strong>Quantos:</strong> ~3 usuários por rodada (já revelam os problemas mais sérios). <strong>Quando:</strong> comece cedo e teste sempre — <strong>'uma manhã por mês'</strong>. <strong>Como:</strong> dê tarefas reais, peça para <strong>pensar em voz alta</strong> (<em>think aloud</em>) e observe sem ajudar nem guiar.","tip":"<strong>Como aplicar:</strong> faça o debrief no mesmo dia e conserte só os problemas mais sérios primeiro — resista a consertar tudo.","wide":True},
   {"ic":"gap","t":"O Mito do \"Usuário Médio\"","b":"Não há usuário típico: 'todos os usuários da web são únicos e todo uso é basicamente imprevisível'. Invocar o <strong>'usuário médio'</strong> para vencer uma discussão é apoiar-se numa figura inexistente.","tip":"<strong>Sinal de alerta:</strong> quando alguém diz 'o usuário médio vai entender', é hora de testar, não de debater.","warn":True},
   {"ic":"lens","t":"Testar para Achar, não para Provar","b":"O objetivo <strong>não é estatística científica</strong> — é encontrar e corrigir problemas. Teste qualitativo, faça-você-mesmo: <strong>pouco e frequente vence muito e raro</strong>. Cada rodada troca horas de opinião por minutos de evidência.","tip":"<strong>Modelo mental:</strong> testar é acender a luz — você para de tropeçar no que não via."},
  ],
  "lessons_title":"Lições-Chave: Teste de Usabilidade",
  "lessons":["Não existe usuário médio — não vença discussões invocando-o; teste.","Teste cedo e sempre: ~3 usuários, uma manhã por mês, pensando em voz alta.","Observe sem guiar, faça o debrief no dia e conserte primeiro só os problemas mais sérios."]},

 {"slug":"ch09-boa-vontade","sub":"CAPÍTULO 9: A Reserva de Boa Vontade",
  "intro":"Todo usuário chega com uma reserva de boa vontade (reservoir of goodwill) — uma paciência limitada. Cada atrito, obstáculo ou desrespeito drena o reservatório; cada cortesia e facilidade o reabastece. Esvaziado, o usuário vai embora, mesmo que o site 'funcione'.",
  "cards":[
   {"ic":"scale","t":"A Paciência É um Tanque Finito","b":"A boa vontade começa cheia (em grau variável) e se esvazia com cada frustração. O perigoso é a <strong>soma de pequenos atritos</strong> — cada um 'pequeno demais para reclamar' — que vaza o tanque até o usuário desistir <strong>sem avisar</strong>.","tip":"<strong>Como aplicar:</strong> a cada exigência, pergunte 'isto enche ou esvazia o tanque?'. Trate o usuário como convidado.","wide":True},
   {"ic":"sword","t":"O Que ESVAZIA o Reservatório","b":"Drenam a boa vontade: <strong>esconder o que o usuário quer</strong> (preço, contato, suporte); <strong>puni-lo por não fazer 'do seu jeito'</strong> (rejeitar telefone com parênteses); <strong>pedir dados desnecessários</strong>; empurrar para ele um trabalho que é seu; e a aparência amadora.","tip":"<strong>Cuidado:</strong> esconder o preço para 'capturar o lead' esvazia o tanque na hora.","warn":True},
   {"ic":"leaf","t":"O Que REABASTECE","b":"Recompõem a paciência: <strong>dizer claramente o que ele quer saber</strong> (frete, prazo, disponibilidade); <strong>poupar passos</strong> e não pedir o que você não precisa; <strong>antecipar dúvidas</strong> (ajuda no ponto de uso); e caprichar nos detalhes e na cortesia.","tip":"<strong>Modelo mental:</strong> hospitalidade reabastece; rispidez drena. Trate o usuário como você gostaria de ser tratado."},
  ],
  "lessons_title":"Lições-Chave: A Boa Vontade",
  "lessons":["Trate a paciência do usuário como reserva finita: cada atrito drena, cada cortesia reabastece.","Não esconda o que ele quer, não peça o desnecessário, não empurre seu trabalho para ele.","Antecipe dúvidas, poupe passos e capriche nos detalhes — pequenas cortesias somam muito."]},

 {"slug":"ch10-acessibilidade-mobile","sub":"CAPÍTULO 10: Acessibilidade e Mobile",
  "intro":"Usabilidade inclui todos os usuários e todos os contextos. Acessibilidade não é caridade nem só conformidade legal — é fazer o site funcionar para pessoas com deficiência, o que quase sempre melhora a experiência de todos. E, no celular, a 1ª Lei vale em dobro.",
  "cards":[
   {"ic":"key","t":"Acessibilidade É Usabilidade Estendida","b":"Corrigir os problemas mais comuns costuma ser <strong>barato e beneficia a todos</strong> ('a maré que sobe levanta todos os barcos'): <strong>alt text</strong> em imagens informativas, <strong>rótulos</strong> em formulários, <strong>contraste e fonte</strong> legíveis, <strong>navegação por teclado</strong> e ordem semântica.","tip":"<strong>Como aplicar:</strong> nunca transmita informação só por cor (ex.: 'campos em vermelho são obrigatórios') — exclui daltônicos.","wide":True},
   {"ic":"wave","t":"Mobile É o Stress Test da 1ª Lei","b":"Celular <strong>não é desktop encolhido</strong>: tela menor, dedo grosso, atenção dividida. Priorize o essencial, use <strong>alvos de toque grandes e espaçados</strong> e exija ainda menos pensamento. Se passa no mobile distraído, passa em qualquer contexto.","tip":"<strong>Modelo mental:</strong> a acessibilidade é como a rampa de calçada — feita para cadeirantes, ajuda carrinhos, malas e todo mundo."},
   {"ic":"clock","t":"Usabilidade × Aprendabilidade (Learnability)","b":"Interfaces mobile escondem comandos atrás de gestos e ícones. Vale sacrificar um pouco de usabilidade imediata se o usuário <strong>aprende rápido</strong> — mas não exagere no obscuro: gesto crítico sem nenhuma pista tem learnability zero.","tip":"<strong>Cuidado:</strong> esconder ações importantes atrás de ícones ambíguos faz ninguém adivinhar como agir.","warn":True},
  ],
  "lessons_title":"Lições-Chave: Acessibilidade e Mobile",
  "lessons":["Acessibilidade é usabilidade para todos — comece pelo barato e de alto impacto (alt, rótulos, contraste, teclado).","Nunca transmita informação só por cor; garanta estrutura semântica e navegação por teclado.","Mobile não é desktop encolhido: priorize o essencial, use alvos de toque grandes e exija menos pensamento."]},
]
