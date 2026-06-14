# -*- coding: utf-8 -*-
"""Conteúdo (pt-BR) das páginas da biblioteca para 'Nação Dopamina' de Anna
Lembke. A neurociência do prazer e do vício: a balança prazer-dor, o déficit
de dopamina, o jejum, o autovínculo, a busca pela dor e o equilíbrio."""

BOOK = {
 "title": "Nação Dopamina",
 "author": "Anna Lembke",
 "header_light": "NAÇÃO",
 "header_bold": "DOPAMINA",
 "subtitle": "VISÃO GERAL · PRAZER, DOR E O EQUILÍBRIO",
 "intro": "A psiquiatra Anna Lembke explica por que, num mundo de prazer ilimitado, estamos mais infelizes. A chave é uma balança: prazer e dor moram no mesmo lugar do cérebro e buscam o equilíbrio — todo prazer é pago com dor depois. Do excesso nasce o déficit de dopamina; a cura passa por abstinência, autovínculo e, surpreendentemente, pela busca deliberada da dor.",
 "description": "A neurociência do prazer e do vício, por Anna Lembke: a balança prazer-dor, a dopamina como moeda do vício, o déficit por excesso, o jejum de dopamina (acrônimo DOPAMINE), o autovínculo, a hormese e o caminho do equilíbrio.",
 "tags": ["Psicologia", "Neurociência", "Hábitos"],
 "progress": "9 Capítulos",
 "cover": "assets/nacao-dopamina-cover.png",
 "overview_cards": [
   {"ic":"scale","t":"A Balança Prazer-Dor","b":"O cérebro processa <strong>prazer e dor no mesmo lugar</strong>, em lados opostos de uma balança que busca o nível. Todo pico de prazer é compensado com dor — e o cérebro <strong>passa do ponto</strong>. Não há prazer de graça.","tip":"<strong>Como aplicar:</strong> o baixo depois do alto é física do cérebro, não fraqueza moral.","wide":True},
   {"ic":"spiral","t":"O Déficit de Dopamina","b":"O excesso repetido derruba a dopamina basal (<strong>tolerância</strong>): a balança vive inclinada para a dor, e o mundo perde a cor (<strong>anedonia</strong>). Passa-se a usar para fugir do baixo, não pelo alto.","tip":"<strong>Chave:</strong> quando tudo fica sem graça, suspeite do excesso, não do mundo."},
   {"ic":"key","t":"A Saída — Abstinência e Dor","b":"A cura começa pelo <strong>jejum de dopamina</strong> (~30 dias) + <strong>autovínculo</strong> (barreiras). E inverte-se a lógica: <strong>pressionar a dor</strong> (exercício, frio) faz a balança rebater ao prazer.","tip":"<strong>Modelo mental:</strong> a dor é a porta dos fundos do prazer."},
 ],
}

CHAPTERS = [
 {"slug":"ch01-balanca-prazer-dor","sub":"CAPÍTULO 1: A Balança Prazer-Dor",
  "intro":"O cérebro processa prazer e dor no mesmo lugar, em lados opostos de uma balança que quer ficar nivelada. Todo prazer é cobrado com dor depois.",
  "cards":[
   {"ic":"scale","t":"A balança e a homeostase","b":"Prazer de um lado, dor do outro, no <strong>mesmo circuito</strong>. Após um pico de prazer, o cérebro empurra a balança para a dor com a mesma força — e <strong>passa do ponto</strong>.","tip":"<strong>Como aplicar:</strong> não há almoço grátis — todo prazer é empréstimo pago em dor.","wide":True},
   {"ic":"wave","t":"O baixo após o alto","b":"O déficit que vem depois do prazer (o anticlímax, a fissura, a ressaca) é a balança compensando — e é ele que <strong>pede a próxima dose</strong>.","tip":"<strong>Modelo mental:</strong> o que sobe desce, e passa do nível."},
   {"ic":"gap","t":"Perseguir só o alto","b":"Buscar o pico ignorando a dor garantida que vem na sequência afunda a balança. Tratar a fissura como <strong>falha moral</strong> só aumenta a culpa.","tip":"<strong>Cuidado:</strong> repor o baixo com outra dose afunda a balança ainda mais.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 1",
  "lessons":["Prazer e dor moram no mesmo circuito, em lados opostos de uma balança.","A homeostase compensa todo prazer com dor — e passa do ponto.","O baixo após o alto é física do cérebro, não fraqueza moral."]},

 {"slug":"ch02-dopamina-moeda","sub":"CAPÍTULO 2: Dopamina — A Moeda do Vício",
  "intro":"A dopamina é, antes de tudo, o neurotransmissor da motivação e da busca — e a moeda universal que mede o potencial viciante de algo.",
  "cards":[
   {"ic":"target","t":"Querer, não gostar","b":"A dopamina impulsiona a <strong>perseguição</strong> da recompensa (o desejo), distinta do prazer de consumi-la. O vício sequestra o <strong>querer</strong> mesmo quando o gostar já sumiu.","tip":"<strong>Como aplicar:</strong> o vício é o querer que sobrevive à morte do gostar.","wide":True},
   {"ic":"spark","t":"Velocidade é veneno","b":"Não é só quanto, mas <strong>quão rápido</strong> a dopamina sobe. Picos altos e instantâneos são os mais perigosos. A mesma régua vale para drogas e comportamentos (telas, jogo, compras).","tip":"<strong>Modelo mental:</strong> o perigo está no pico rápido, não só na quantidade."},
   {"ic":"gap","t":"Caçar dopamina direto","b":"Buscar a dopamina diretamente é perseguir o <strong>querer</strong>, que nunca se sacia. Confundi-la com felicidade leva à corrida sem fim.","tip":"<strong>Cuidado:</strong> achar que só drogas viciam ignora que telas disparam a mesma moeda.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 2",
  "lessons":["Dopamina é a moeda do querer e da busca — e a régua do potencial viciante.","Querer e gostar são distintos; o vício é o querer sem o gostar.","Picos altos e rápidos são os mais perigosos — velocidade é veneno."]},

 {"slug":"ch03-deficit-dopamina","sub":"CAPÍTULO 3: O Déficit de Dopamina",
  "intro":"Empurrar a balança para o prazer repetidamente faz o cérebro reduzir a própria dopamina. A balança passa a viver inclinada para a dor.",
  "cards":[
   {"ic":"spiral","t":"Tolerância e gremlins","b":"O uso repetido faz o lado da dor responder mais forte (tolerância). Os <strong>gremlins</strong> se acumulam no lado da dor e a <strong>linha de base afunda</strong>.","tip":"<strong>Como aplicar:</strong> a mesma dose entrega cada vez menos — a tolerância sempre ganha.","wide":True},
   {"ic":"eye","t":"Anedonia","b":"No déficit, <strong>nada dá prazer</strong> — nem o vício. Consome-se já não para sentir o alto, mas para <strong>escapar do baixo</strong>.","tip":"<strong>Modelo mental:</strong> tolerância é o brilho do mundo apagando."},
   {"ic":"gap","t":"Aumentar a dose","b":"Repor o déficit com mais estímulo <strong>afunda a balança ainda mais</strong> — a espiral do vício.","tip":"<strong>Cuidado:</strong> 'nada me dá prazer' às vezes é a balança em déficit pedindo abstinência.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 3",
  "lessons":["O excesso repetido rebaixa a dopamina basal — tolerância e déficit.","Os gremlins se acumulam no lado da dor; o normal vira negativo (anedonia).","O vício madura troca a busca do prazer pela fuga da dor."]},

 {"slug":"ch04-era-da-indulgencia","sub":"CAPÍTULO 4: A Era da Indulgência",
  "intro":"Um cérebro feito para a escassez foi solto num mundo de superabundância de dopamina — e a balança vive inclinada para a dor.",
  "cards":[
   {"ic":"link","t":"Incompatibilidade evolutiva","b":"O aparato que nos fazia perseguir recompensas <strong>raras</strong> agora é bombardeado por recompensas <strong>infinitas</strong>. O design que era vantagem virou armadilha.","tip":"<strong>Como aplicar:</strong> cérebro de escassez, mundo de fartura — o descompasso, não a fraqueza, explica o vício.","wide":True},
   {"ic":"pin","t":"O smartphone-agulha","b":"Lembke chama o celular de <strong>agulha hipodérmica moderna</strong> — dopamina rápida e variável, a qualquer hora. A <strong>recompensa variável</strong> é o padrão mais viciante.","tip":"<strong>Modelo mental:</strong> conveniência é a isca; acesso fácil afunda a balança."},
   {"ic":"gap","t":"A doença da abundância","b":"Depressão e anedonia crescem nos países mais ricos — <strong>por excesso, não por falta</strong>. Buscar a cura em mais consumo afunda a balança.","tip":"<strong>Cuidado:</strong> culpar só a força de vontade ignora que os produtos são desenhados para vencê-la.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 4",
  "lessons":["Um cérebro de escassez vive num mundo de superabundância de dopamina.","O smartphone é a 'agulha' moderna; recompensa variável é o padrão mais viciante.","O excesso, não a falta, gera o mal-estar."]},

 {"slug":"ch05-jejum-de-dopamina","sub":"CAPÍTULO 5: O Jejum de Dopamina",
  "intro":"A cura começa por parar: a abstinência. Em geral ~30 dias para o cérebro renivelar a balança e voltar a sentir prazer nas coisas simples.",
  "cards":[
   {"ic":"clock","t":"A regra dos ~30 dias","b":"É o tempo que o sistema de recompensa leva para se reajustar. Os <strong>primeiros dias são os piores</strong> (a balança ainda na dor); a melhora vem na 2ª metade.","tip":"<strong>Como aplicar:</strong> o objetivo é devolver a sensibilidade ao prazer simples, não zerar a dopamina.","wide":True},
   {"ic":"steps","t":"O acrônimo DOPAMINE","b":"<strong>D</strong>ados · <strong>O</strong>bjetivos · <strong>P</strong>roblemas · <strong>A</strong>bstinência · <strong>M</strong>indfulness · <strong>I</strong>nsight · <strong>N</strong>ext (próximos passos) · <strong>E</strong>xperimento.","tip":"<strong>Modelo mental:</strong> a fissura é uma onda — observe-a sem obedecer; ela passa."},
   {"ic":"gap","t":"Desistir cedo","b":"Abandonar nos primeiros dias é justo quando a balança está <strong>mais na dor</strong> — e confirma o vício. Tentar moderar antes de abstinir reacende o ciclo.","tip":"<strong>Cuidado:</strong> a piora inicial é o reajuste, não uma recaída do problema.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 5",
  "lessons":["A cura começa pela abstinência — ~30 dias para renivelar a balança.","O acrônimo DOPAMINE dá o roteiro do jejum.","Piora antes de melhorar; o alvo é recuperar a sensibilidade ao prazer simples."]},

 {"slug":"ch06-autovinculo","sub":"CAPÍTULO 6: O Autovínculo",
  "intro":"A força de vontade é frágil. O autovínculo cria, com a mente fria, barreiras entre você e o estímulo — para a decisão certa não depender da força de vontade na hora da fissura.",
  "cards":[
   {"ic":"key","t":"Os 3 tipos","b":"<strong>Físico</strong> (distância: app fora do celular, gatilho fora de casa); <strong>cronológico</strong> (janelas de tempo: 'só após as 18h'); <strong>categórico</strong> (abstinência total da categoria).","tip":"<strong>Como aplicar:</strong> decida com a mente fria — erga o muro antes da fissura chegar.","wide":True},
   {"ic":"link","t":"Ulisses e o mastro","b":"Amarrar-se ao mastro antes de ouvir as sereias: <strong>proteger o eu futuro</strong> das escolhas do eu impulsivo. Não é resistir — é não precisar resistir.","tip":"<strong>Modelo mental:</strong> a vontade é fraca; mude o ambiente, não confie na vontade."},
   {"ic":"gap","t":"Barreira fraca","b":"Se contornar é fácil (o app a um toque), <strong>não é autovínculo</strong>. Manter o gatilho à mão 'para testar o autocontrole' é alimentá-lo.","tip":"<strong>Cuidado:</strong> na hora da fissura, a força de vontade quase sempre perde.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 6",
  "lessons":["A força de vontade é frágil; o autovínculo cria barreiras que dispensam a luta.","Três tipos: físico (distância), cronológico (tempo), categórico (abstinência).","Decida com a mente fria — erga o muro antes da fissura."]},

 {"slug":"ch07-busca-pela-dor","sub":"CAPÍTULO 7: A Busca pela Dor",
  "intro":"Se o prazer é pago com dor, a recíproca liberta: pressionar de propósito o lado da dor faz a balança rebater para o prazer — duradouro e sem ressaca.",
  "cards":[
   {"ic":"pivot","t":"Hormese","b":"Doses <strong>pequenas e controladas</strong> de um estressor (dor) ativam a recuperação do corpo, que <strong>passa do ponto para o prazer</strong> — o rebote. O bem-estar vem depois, e dura.","tip":"<strong>Como aplicar:</strong> a dor é a porta dos fundos do prazer — sem ressaca.","wide":True},
   {"ic":"steps","t":"A 'dor boa'","b":"Exercício, banho frio, jejum, sauna, trabalho difícil — desconfortos auto-impostos que rebatem em <strong>energia, foco e humor</strong> e elevam a linha de base.","tip":"<strong>Modelo mental:</strong> desconforto voluntário é antídoto do excesso."},
   {"ic":"gap","t":"Exagerar a dose","b":"Hormese vira <strong>lesão</strong> se o estressor for grande demais. Buscar a dor pela dor (masoquismo) erra o alvo — o objetivo é o rebote saudável.","tip":"<strong>Cuidado:</strong> o ganho vem no rebote; quem desiste durante a dor não colhe o depois.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 7",
  "lessons":["Pressionar de propósito o lado da dor faz a balança rebater ao prazer (hormese).","Exercício, frio e jejum dão prazer duradouro e sem ressaca.","A dose certa é moderada; dor demais é dano, não remédio."]},

 {"slug":"ch08-honestidade-radical","sub":"CAPÍTULO 8: A Honestidade Radical",
  "intro":"A recuperação é relacional. Dizer a verdade — inclusive a inconveniente — regula a dopamina e reconstrói a conexão que o vício corrói.",
  "cards":[
   {"ic":"eye","t":"A verdade como reguladora","b":"Relatar honestamente o que se fez (mesmo o vergonhoso) cria <strong>responsabilização</strong> e ativa circuitos de conexão — ajudando a equilibrar a balança.","tip":"<strong>Como aplicar:</strong> a verdade dói na hora e cura depois; a mentira alivia na hora e adoece depois.","wide":True},
   {"ic":"link","t":"Autoria, não vítima","b":"Contar a própria história com <strong>responsabilidade pelos próprios atos</strong> cura mais do que a narrativa de vítima passiva. A vulnerabilidade honesta restaura o vínculo.","tip":"<strong>Modelo mental:</strong> esconder é estar sozinho — e o isolamento alimenta o vício."},
   {"ic":"gap","t":"A narrativa de vítima","b":"Terceirizar a culpa ('foi tudo culpa de X') mantém a <strong>passividade</strong> que impede a recuperação. Confessar para impressionar não cura.","tip":"<strong>Cuidado:</strong> 'ser brutalmente honesto' com os outros não é desculpa para a crueldade.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 8",
  "lessons":["A honestidade radical regula a dopamina e reconstrói a conexão.","A mentira alivia na hora e adoece depois; a verdade dói e cura.","Autoria dos próprios atos (não a vítima) é o que recupera."]},

 {"slug":"ch09-vergonha-equilibrio","sub":"CAPÍTULO 9: Vergonha Prossocial e o Equilíbrio",
  "intro":"A vergonha pode isolar ou reconectar. E a síntese do livro: a meta não é eliminar o prazer nem só sofrer, mas administrar a balança — o equilíbrio.",
  "cards":[
   {"ic":"pivot","t":"As duas vergonhas","b":"A <strong>destrutiva</strong> diz 'eu sou ruim' → isola, esconde, usa mais. A <strong>prossocial</strong> diz 'fiz algo ruim, mas pertenço a um grupo que me ajuda' → repara e reconecta.","tip":"<strong>Como aplicar:</strong> 'eu fiz algo ruim' cura; 'eu sou ruim' afunda.","wide":True},
   {"ic":"scale","t":"O equilíbrio","b":"A meta final: buscar prazer com <strong>consciência da dor</strong> que ele cobra, e buscar dor com consciência do prazer que devolve. Não abstinência eterna — uma <strong>balança administrada</strong>.","tip":"<strong>Modelo mental:</strong> o alvo é o nível, não o pico."},
   {"ic":"gap","t":"Afogar a vergonha","b":"A vergonha destrutiva <strong>pede o próprio veneno</strong> que a criou. Isolar-se na culpa torna a vergonha destrutiva por padrão.","tip":"<strong>Cuidado:</strong> regras claras + comunidade transformam a vergonha em combustível de mudança.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 9",
  "lessons":["Vergonha destrutiva isola e afunda; prossocial reconecta e repara.","Regras claras + comunidade transformam a vergonha em mudança.","A meta é o equilíbrio da balança — não o pico."]},
]
