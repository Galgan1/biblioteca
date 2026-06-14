# -*- coding: utf-8 -*-
"""Conteúdo (pt-BR) das páginas da biblioteca para 'As 48 Leis do Poder' (Robert Greene).
Agrupamento temático próprio das 48 leis, em chave DEFENSIVA (reconhecer para não ser peão).
Não reproduz o texto nem a lista integral — síntese atribuída a Greene."""

BOOK = {
 "title": "As 48 Leis do Poder",
 "author": "Robert Greene",
 "header_light": "AS 48 LEIS",
 "header_bold": "DO PODER",
 "subtitle": "VISÃO GERAL · O JOGO SOCIAL DO PODER (LEITURA DEFENSIVA)",
 "intro": "O poder é um jogo social com regras atemporais. Robert Greene destila séculos de história em 48 leis de tom amoral — descreve o poder como ele é, não como deveria ser. Aqui a leitura é defensiva: reconhecer as táticas (no chefe, no falso amigo, no vendedor) para não virar peão.",
 "description": "O compêndio de Robert Greene sobre a dinâmica do poder, destilado de três mil anos de história. Apresentado em agrupamento temático e em chave defensiva: proteger a reputação, dominar as aparências, criar dependência, a tática da indireção, sedução e timing, a defesa contra manipulação e a lei suprema de ser informe.",
 "tags": ["Poder", "Estratégia", "Psicologia"],
 "progress": "8 Capítulos",
 "cover": "assets/48-leis-do-poder-cover.png",
 "overview_cards": [
   {"ic":"scale","t":"Os 7 Eixos das 48 Leis","b":"A síntese temática do livro:","list":[
     "<strong>Proteja o mestre e a reputação</strong> (1, 5, 2).",
     "<strong>Domine as aparências</strong> (3, 4, 6, 7).",
     "<strong>Controle e dependência</strong> (11, 8, 9).",
     "<strong>Tática e indireção</strong> (15, 33, 21, 13).",
     "<strong>Sedução, audácia e timing</strong> (32, 28, 35, 25).",
     "<strong>Defesa</strong> (10, 19, 20, 40) e <strong>a lei suprema</strong> (48, 34).",
   ],"tip":"<strong>Chave do acervo:</strong> leitura DEFENSIVA — reconhecer a tática para não ser vítima, não para virar vilão.","wide":True},
   {"ic":"mask","t":"As Três Leis-Mestras","b":"<strong>Reputação</strong> (Lei 5) é o ativo central; <strong>dissimulação</strong> (3 e 4) — o poder vive na incerteza; <strong>ser informe</strong> (48) — padrão fixo é alvo, adaptar-se é blindagem.","tip":"<strong>Modelo mental:</strong> intenção exposta é arma entregue."},
   {"ic":"eye","t":"A Pergunta Defensiva","b":"Para cada jogada, pergunte — <strong>\"quem está aplicando isto em mim?\"</strong>. O elogio com pedido (isca, Lei 8), o presente súbito (Lei 40), o bajulador que te faz baixar a guarda.","tip":"<strong>Cuidado:</strong> recusar-se a ver o jogo não te protege — te torna peão.","warn":True},
 ],
}

CHAPTERS = [
 {"slug":"ch01-natureza-do-poder","sub":"CAPÍTULO 1: A Natureza do Poder",
  "intro":"Poder não é força bruta — é influência social, indireta e sutil. Quem se recusa a entender o jogo não permanece puro; permanece peão. A lente certa é diagnóstica.",
  "cards":[
   {"ic":"scale","t":"O Poder é um Jogo Social","b":"Regras atemporais, observadas em séculos de história e na <strong>sociedade de corte</strong>. O cortesão de Versalhes vence pela aparência e pelo cálculo, não pelo confronto.","tip":"<strong>Modelo mental:</strong> toda interação tem uma camada de poder — mesmo as amigáveis."},
   {"ic":"mask","t":"Tom Amoral","b":"Greene descreve o poder como ele <strong>é</strong>, não como deveria ser. É controverso — pode ser lido como manual de manipulação. Cabe ao leitor o <strong>discernimento ético</strong>.","tip":"<strong>Regra do acervo:</strong> use como lente, não como cartilha de vilania."},
   {"ic":"eye","t":"A Ingenuidade é Vulnerabilidade","b":"Ignorar o jogo é entregá-lo ao outro. A leitura defensiva — \"<strong>quem aplica isto em mim?</strong>\" — é o uso sábio das 48 leis.","tip":"<strong>Sinal de alerta:</strong> achar que \"não jogar\" protege protege menos que reconhecer o jogo.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 1",
  "lessons":["Trate poder como jogo social a ser lido, não negado.","Use as leis como diagnóstico — reconhecer para se defender.","O tom é amoral; o discernimento é seu."]},

 {"slug":"ch02-mestre-reputacao","sub":"CAPÍTULO 2: Proteja o Mestre e a Reputação",
  "intro":"A primeira arena do poder é a percepção dos outros — sobretudo de quem está acima de você. Ofuscar o superior e descuidar da reputação afundam mais gente que a incompetência.",
  "cards":[
   {"ic":"scale","t":"Lei 5 — A Reputação é Tudo","b":"Ela decide como você é lido <strong>antes de abrir a boca</strong>. Forte, intimida; arranhada, convida ataque. Defenda a sua como capital — construída devagar, perdida rápido.","tip":"<strong>Como aplicar:</strong> guarde a reputação como ativo central."},
   {"ic":"mask","t":"Lei 1 — Nunca Ofusque o Mestre","b":"Faça quem está acima sentir-se superior. Brilho excessivo sem tato gera <strong>inveja e retaliação</strong> — o talentoso que corrige o chefe em público colhe sabotagem.","tip":"<strong>Regra:</strong> deixe o crédito subir; sua ascensão deixa de ameaçar.","warn":True},
   {"ic":"link","t":"Lei 2 — Amigos e Inimigos","b":"Cuidado com amigos (o acomodado pode invejar); saiba <strong>usar inimigos</strong> — o ex-rival conquistado é leal por prova. Avalie pelo interesse, não só pelo afeto.","tip":"<strong>Cuidado:</strong> confiança cega por afeto ignora o interesse em jogo."},
  ],
  "lessons_title":"Lições-Chave do Capítulo 2",
  "lessons":["Guarde a reputação como ativo central.","Valorize o mestre; deixe o crédito subir.","Avalie amigos pelo interesse, não só pelo afeto."]},

 {"slug":"ch03-aparencias-atencao","sub":"CAPÍTULO 3: Domine as Aparências e a Atenção",
  "intro":"No jogo do poder, o que parece pesa mais que o que é. Controlar o que você revela — e capturar a atenção — é meia batalha vencida.",
  "cards":[
   {"ic":"mask","t":"Leis 3 e 4 — Dissimule e Diga Menos","b":"Intenção exposta é <strong>arma entregue</strong>; mantenha o outro no escuro e ele reage tarde. E o silêncio sugere poder — quanto mais você fala, mais comum e vulnerável parece.","tip":"<strong>Como aplicar:</strong> numa negociação, quem fala menos faz o outro preencher o silêncio com concessões.","wide":True},
   {"ic":"eye","t":"Lei 6 — Corteje a Atenção","b":"Ser notado e comentado importa — a <strong>invisibilidade é a morte social</strong>. A controvérsia que faz falar pode valer mais que o elogio morno.","tip":"<strong>Modelo mental:</strong> atenção é moeda."},
   {"ic":"spark","t":"Lei 7 — Leve o Crédito","b":"Faça os outros trabalharem, mas a <strong>eficiência aparente</strong> é o que fica na memória. Mostre o efeito, esconda o esforço (e a intenção).","tip":"<strong>Defesa:</strong> perceba quando alguém está levando o crédito do SEU trabalho."},
  ],
  "lessons_title":"Lições-Chave do Capítulo 3",
  "lessons":["Revele intenções a conta-gotas.","Fale menos; deixe o silêncio trabalhar.","Gerencie atenção e crédito ativamente."]},

 {"slug":"ch04-controle-dependencia","sub":"CAPÍTULO 4: Controle e Dependência",
  "intro":"Poder durável é poder de que os outros precisam. Tornar-se necessário — e fazer o jogo vir até você — vale mais que qualquer demonstração de força.",
  "cards":[
   {"ic":"link","t":"Lei 11 — Faça-os Dependerem de Você","b":"Quando sua falta dói, sua posição fica intocável. <strong>Indispensabilidade é segurança</strong> — seja o nó que, removido, derruba a estrutura.","tip":"<strong>Como aplicar:</strong> construa dependência, não favores avulsos (o favor se esquece; a necessidade fica)."},
   {"ic":"target","t":"Lei 8 — Faça-os Vir Até Você","b":"Quem força o adversário a agir <strong>controla o terreno</strong>. A paciência vira ataque; use uma isca e deixe o outro se mover primeiro.","tip":"<strong>Defesa:</strong> desconfie quando algo é bom demais para te atrair — pode ser isca."},
   {"ic":"spark","t":"Lei 9 — Vença por Ações","b":"Discussão gera ressentimento; o <strong>fato consumado</strong> convence sem inimizade. Prove com o resultado — ninguém discute com o fato.","tip":"<strong>Regra:</strong> vencer a discussão e perder a pessoa é derrota disfarçada."},
  ],
  "lessons_title":"Lições-Chave do Capítulo 4",
  "lessons":["Torne-se necessário; construa dependência ética.","Faça o outro vir até você.","Convença por ações, não por debate."]},

 {"slug":"ch05-tatica-indirecao","sub":"CAPÍTULO 5: Tática e Indireção",
  "intro":"O confronto frontal é caro e arriscado. As táticas de poder operam pelo flanco: explorar fraquezas, mascarar força e fazer o outro baixar a guarda.",
  "cards":[
   {"ic":"lens","t":"Lei 33 — O Ponto Fraco","b":"Todo alvo tem um \"<strong>polegar</strong>\" — uma insegurança, vaidade ou necessidade. Encontrá-lo é achar a alavanca. A vaidade de alguém costuma ser a porta de entrada.","tip":"<strong>Defesa:</strong> conheça o SEU ponto fraco antes que explorem por você."},
   {"ic":"mask","t":"Leis 21 e 22 — Tolo e Rendição","b":"<strong>Finja-se mais tolo</strong> que o alvo — o subestimado tem campo livre. E a <strong>tática da rendição</strong>: ceder na hora certa transforma fraqueza aparente em vantagem.","tip":"<strong>Modelo mental:</strong> parecer inofensivo é uma forma de poder."},
   {"ic":"key","t":"Lei 13 — Apele ao Interesse Próprio","b":"Ao pedir ajuda, fale do <strong>ganho do outro</strong> — nunca da gratidão ou de favores passados. O sim vem fácil quando atende a quem decide.","tip":"<strong>Como aplicar:</strong> mostre a vantagem do aliado, não a sua necessidade."},
  ],
  "lessons_title":"Lições-Chave do Capítulo 5",
  "lessons":["Ao pedir, fale do interesse do outro.","Leia o ponto fraco antes de agir.","Não deixe disputas pela metade (Lei 15)."]},

 {"slug":"ch06-seducao-audacia-timing","sub":"CAPÍTULO 6: Sedução, Audácia e Timing",
  "intro":"Poder também se conquista atraindo — pela imaginação dos outros, pela audácia que impõe respeito e pelo senso de momento que separa o golpe certo do precipitado.",
  "cards":[
   {"ic":"spark","t":"Lei 32 — Jogue com as Fantasias","b":"A verdade é dura; quem oferece o <strong>sonho</strong> atrai multidões. O desejo move mais que a estatística.","tip":"<strong>Como aplicar:</strong> ofereça uma visão, não só dados. (Defesa: desconfie de quem só vende sonho.)"},
   {"ic":"mountain","t":"Lei 28 — Aja com Audácia","b":"A hesitação contamina; o gesto ousado convence pela própria convicção. <strong>Audácia gera autoridade</strong>; meia audácia é o pior dos mundos.","tip":"<strong>Regra:</strong> aja com audácia plena ou não aja."},
   {"ic":"clock","t":"Leis 35 e 25 — Timing e Recriar-se","b":"<strong>Domine o timing</strong> — o mesmo gesto, cedo ou tarde demais, fracassa. E <strong>recrie-se</strong>: forje a própria imagem antes que imponham uma a você.","tip":"<strong>Modelo mental:</strong> o timing é metade da tática."},
  ],
  "lessons_title":"Lições-Chave do Capítulo 6",
  "lessons":["Ofereça uma visão, não só dados.","Aja com audácia plena ou não aja.","Trabalhe o timing tanto quanto a tática."]},

 {"slug":"ch07-defesa","sub":"CAPÍTULO 7: O Lado Defensivo",
  "intro":"O uso ético das 48 leis é defensivo: reconhecer as táticas aplicadas em você. Boa parte das leis ensina a se proteger de pessoas tóxicas, presentes interesseiros e compromissos que aprisionam.",
  "cards":[
   {"ic":"eye","t":"Lei 10 — Evite os Azarados","b":"Estados emocionais e padrões de fracasso são <strong>contagiosos</strong>. Você absorve o padrão de quem te cerca — escolha o círculo com cuidado.","tip":"<strong>Cuidado:</strong> a convivência que rebaixa contamina sem você notar.","warn":True},
   {"ic":"mask","t":"Lei 40 — Despreze o que é Grátis","b":"Toda dádiva tem um <strong>preço oculto</strong>; o \"presente\" cria dívida e controle. A generosidade súbita costuma cobrar depois.","tip":"<strong>Defesa:</strong> agradeça sem ficar refém da reciprocidade.","warn":True},
   {"ic":"key","t":"Leis 19 e 20 — Saiba com Quem Lida","b":"Não ofenda a pessoa errada (alguns nunca esquecem). E <strong>não se comprometa cedo demais</strong> — independência preserva opções e valor.","tip":"<strong>Regra:</strong> quem não deve, não é dono de ninguém — nem refém."},
  ],
  "lessons_title":"Lições-Chave do Capítulo 7",
  "lessons":["Escolha o círculo — o padrão é contagioso.","Desconfie do grátis; toda dádiva cobra.","Preserve independência e opções."]},

 {"slug":"ch08-lei-suprema","sub":"CAPÍTULO 8: A Lei Suprema — Seja Informe",
  "intro":"A lei que fecha o livro é a mais profunda: adaptabilidade. O que tem forma fixa é previsível, e o previsível é atacável. O poder duradouro flui como água.",
  "cards":[
   {"ic":"wave","t":"Lei 48 — Assuma a Forma da Água","b":"Não se prenda a um único método ou identidade rígida; <strong>mude conforme o terreno</strong> e ninguém te encurrala. Padrão previsível é alvo; adaptar-se é blindagem.","tip":"<strong>Como aplicar:</strong> varie a resposta — quem é lido é manipulado.","wide":True},
   {"ic":"mountain","t":"Lei 34 — Porte-se como Rei","b":"A postura <strong>molda como o mundo te trata</strong> — a profecia da autoimagem projetada. O porte antecede o reconhecimento.","tip":"<strong>Cuidado:</strong> informe ≠ sem caráter; é flexibilidade tática sobre valores firmes."},
   {"ic":"scale","t":"A Régua Ética","b":"As leis são uma <strong>lente</strong> do jogo social. Usá-las como manual de vilania corrói a própria reputação (Lei 5) e fabrica inimigos. O poder ético serve quem entende o jogo sem perder a alma.","tip":"<strong>Regra final:</strong> reconhecer a tática (como na ponerologia) desarma o poder dela."},
  ],
  "lessons_title":"Lições-Chave do Capítulo 8",
  "lessons":["Não se prenda a um método único; adapte-se ao terreno.","A postura projeta o status.","Use as leis como lente ética, não como cartilha de vilania."]},
]
