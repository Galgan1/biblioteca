# -*- coding: utf-8 -*-
"""Conteúdo (pt-BR) das páginas da biblioteca para 'A Psicologia Financeira' (Morgan Housel).
Frameworks: comportamento > matemática, sorte e risco, nunca o bastante, juros compostos,
sobreviver, cauda longa, liberdade, homem no carro, riqueza invisível, poupar/margem, pessimismo/mudança."""

BOOK = {
 "title": "A Psicologia Financeira",
 "author": "Morgan Housel",
 "header_light": "PSICOLOGIA",
 "header_bold": "FINANCEIRA",
 "subtitle": "VISÃO GERAL · COMO VOCÊ AGE IMPORTA MAIS QUE O QUE VOCÊ SABE",
 "intro": "O sucesso com dinheiro não é uma ciência exata — é uma habilidade comportamental. Um gênio que perde o controle das emoções pode quebrar; uma pessoa comum, sem formação financeira, pode enriquecer apenas com paciência, poupança e bom comportamento. Morgan Housel mostra que como você se comporta importa mais do que o que você sabe.",
 "description": "As lições atemporais de Morgan Housel sobre riqueza, ganância e felicidade. Por que o comportamento vence a matemática nas finanças: sorte e risco, o 'nunca o bastante', os juros compostos, sobreviver para deixar o tempo compor, a cauda longa, a liberdade como maior dividendo, a riqueza invisível e a margem de segurança.",
 "tags": ["Finanças", "Comportamento", "Investimento"],
 "progress": "11 Capítulos",
 "cover": "assets/psicologia-financeira-cover.png",
 "overview_cards": [
   {"ic":"scale","t":"Comportamento > Matemática","b":"Finanças são uma <strong>soft skill</strong>, não uma ciência exata. Um gênio que perde o controle das emoções quebra; uma pessoa comum enriquece com <strong>paciência, poupança e bom comportamento</strong>.","tip":"<strong>Como aplicar:</strong> trabalhe a atitude (poupar, sobreviver, ser humilde) antes de escolher ativos.","wide":True},
   {"ic":"clock","t":"Sobreviver + Deixar o Tempo Compor","b":"Ganhar dinheiro pede ousadia; <strong>mantê-lo</strong> pede humildade e medo. A única estratégia infalível é <strong>sobreviver</strong> — ficar no jogo o bastante para os <strong>juros compostos</strong> agirem.","tip":"<strong>Regra:</strong> nunca se exponha à ruína; maximize o tempo no jogo, não o retorno do ano."},
   {"ic":"eye","t":"Riqueza é o que Você Não Vê","b":"<strong>Rico</strong> é a renda de agora; <strong>riqueza</strong> é a renda que você NÃO gastou. O maior dividendo do dinheiro é o <strong>controle do seu tempo</strong> — não as posses.","tip":"<strong>Modelo mental:</strong> meça-se pelo patrimônio guardado, não pelo consumo exibido."},
 ],
}

CHAPTERS = [
 {"slug":"ch01-ninguem-e-doido","sub":"CAPÍTULO 1: Ninguém é Doido",
  "intro":"As pessoas não tomam decisões financeiras malucas — tomam decisões que fazem sentido para elas, dada a história e a geração que viveram. Sucesso com dinheiro é mais comportamento do que conhecimento.",
  "cards":[
   {"ic":"scale","t":"Finanças como Soft Skill","b":"Não é física (regras e fórmulas), é psicologia aplicada — medo, ganância, ego, otimismo. <strong>Como você se comporta importa mais do que o que você sabe.</strong>","tip":"<strong>Como aplicar:</strong> ataque a atitude, não só a planilha.","wide":True},
   {"ic":"lens","t":"Ninguém é Doido","b":"Cada decisão faz sentido para quem a toma, dada sua <strong>experiência única</strong>. Vivemos ~0,00000001% da história econômica e achamos que entendemos o todo.","tip":"<strong>Modelo mental:</strong> pergunte 'que vivência o leva a agir assim?' antes de 'que erro ele cometeu?'."},
   {"ic":"fork","t":"Cada Um Joga um Jogo Diferente","b":"Suas escolhas refletem época, classe e traumas — não uma fórmula universal. Copiar quem tem outro <strong>horizonte, risco e objetivo</strong> leva ao desastre.","tip":"<strong>Cuidado:</strong> não imite quem joga um jogo diferente do seu.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 1",
  "lessons":["Comportamento bate inteligência nas finanças.","Antes de julgar, reconstrua a experiência de quem decide.","Saiba qual jogo você joga — e não copie quem joga outro."]},

 {"slug":"ch02-sorte-e-risco","sub":"CAPÍTULO 2: Sorte & Risco",
  "intro":"Sorte e risco são irmãos: ambos são a realidade de que todo resultado é guiado por forças além do esforço. A sorte é o risco visto pelo lado de fora.",
  "cards":[
   {"ic":"fork","t":"Sorte e Risco São Gêmeos","b":"Nenhum sucesso é só mérito; nenhum fracasso é só erro. <strong>A sorte é o risco visto pelo outro lado.</strong>","tip":"<strong>Como aplicar:</strong> pergunte 'quanto disso foi processo replicável e quanto foi acaso?'.","wide":True},
   {"ic":"constellation","t":"Foque em Padrões, Não em Indivíduos","b":"Casos extremos (o bilionário que largou a faculdade) são exemplos <strong>ruins</strong> — sorte e azar distorcem demais. Estude o <strong>geral</strong>, não o herói.","tip":"<strong>Regra:</strong> não idolatre nem demonize indivíduos; extraia padrões amplos."},
   {"ic":"mask","t":"Humildade nos Dois Lados","b":"Dar crédito demais a si nos acertos e culpa demais ao mundo nos erros distorce o aprendizado. <strong>Bill Gates teve a escola; Kent Evans teve o acidente</strong> — mesmo talento, destinos opostos.","tip":"<strong>Cuidado:</strong> seja humilde nos acertos e gentil consigo nos erros.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 2",
  "lessons":["Trate sorte e risco como duas faces da mesma moeda.","Não idolatre nem condene casos individuais — extraia padrões.","Humildade nos acertos, autocompaixão nos erros."]},

 {"slug":"ch03-nunca-o-bastante","sub":"CAPÍTULO 3: Nunca o Bastante",
  "intro":"A habilidade financeira mais difícil é fazer a meta parar de se mover. Sem um senso de 'o bastante', nenhum ganho satisfaz — e a busca infinita leva a riscar o que se tem por algo de que não se precisa.",
  "cards":[
   {"ic":"target","t":"Mover a Trave","b":"A ambição que cresce <strong>mais rápido que a satisfação</strong> garante insatisfação permanente. O teto da comparação social é inalcançável — sempre há alguém acima.","tip":"<strong>Como aplicar:</strong> defina explicitamente o que é 'o bastante' antes de buscar mais.","wide":True},
   {"ic":"sword","t":"O que Nunca Vale o Risco","b":"Riscar o que você tem (e precisa) por algo de que <strong>não precisa</strong> é insanidade. Reputação, liberdade, família, ser amado e felicidade <strong>não têm preço de recompra</strong>.","tip":"<strong>Sinal de alerta:</strong> dívida e fraude para acelerar ganhos — tinham tudo e quiseram mais.","warn":True},
   {"ic":"bulb","t":"\"Eu Tenho o Bastante\"","b":"Na festa do bilionário, Heller responde a Vonnegut: \"tenho algo que ele nunca terá — <strong>o bastante</strong>.\" Reconhecer o suficiente é a vitória.","tip":"<strong>Regra:</strong> pare de comparar; a corrida do 'mais que o vizinho' não tem linha de chegada."},
  ],
  "lessons_title":"Lições-Chave do Capítulo 3",
  "lessons":["Defina seu 'o bastante' antes que a trave se mova sozinha.","Nunca arrisque o que tem (e precisa) por algo de que não precisa.","Há valores acima de qualquer cifra — não os ponha em jogo."]},

 {"slug":"ch04-juros-compostos","sub":"CAPÍTULO 4: A Confusão dos Juros Compostos",
  "intro":"Os juros compostos são contraintuitivos: o que produz fortunas não é o retorno espetacular, é o retorno bom mantido por muito tempo. Tempo é a alavanca que o cérebro subestima.",
  "cards":[
   {"ic":"spiral","t":"A 8ª Maravilha","b":"Pequenos ganhos repetidos por <strong>décadas</strong> explodem em escala que a intuição linear não prevê. O composto cresce devagar e depois <strong>dispara</strong> — a maior parte vem no fim.","tip":"<strong>Modelo mental:</strong> não-linear — comece cedo e fique muito tempo.","wide":True},
   {"ic":"clock","t":"Tempo > Retorno","b":"Estender o <strong>prazo</strong> bate melhorar o percentual. <strong>~84,2 dos US$ 84,5 bi de Buffett</strong> vieram depois dos 50 anos — o segredo foi investir bem por ~75 anos, não o retorno único.","tip":"<strong>Regra:</strong> maximize o horizonte, não só a taxa."},
   {"ic":"pin","t":"Não Interrompa à Toa","b":"Cada saída antecipada <strong>zera</strong> o efeito composto acumulado. O resultado vem do tempo no mercado, não de acertar o timing.","tip":"<strong>Cuidado:</strong> buscar o 'melhor ano' em vez de muitos anos medianos seguidos.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 4",
  "lessons":["O resultado vem do tempo no mercado, não do timing.","Um retorno bom e durável vence um retorno alto e curto.","Paciência é a maior vantagem competitiva acessível a qualquer um."]},

 {"slug":"ch05-ficar-rico-continuar-rico","sub":"CAPÍTULO 5: Ficar Rico vs. Continuar Rico",
  "intro":"Conquistar dinheiro e mantê-lo exigem habilidades opostas. Ganhar pede ousadia e otimismo; manter pede humildade e medo de perder. A única estratégia que garante o composto é sobreviver.",
  "cards":[
   {"ic":"mountain","t":"Sobrevivência Acima de Tudo","b":"Ficar no jogo por décadas vale mais que qualquer retorno excepcional. <strong>Evite a ruína a todo custo</strong> — nunca seja forçado a vender no fundo.","tip":"<strong>Como aplicar:</strong> seja financeiramente inquebrável — caixa, baixa dívida, folga.","wide":True},
   {"ic":"pivot","t":"Ganhar ≠ Manter","b":"Conquistar pede <strong>ousadia e otimismo</strong>; manter pede <strong>humildade e medo</strong> de perder. Troque de mentalidade depois de conquistar.","tip":"<strong>Modelo mental:</strong> otimista no longo prazo, paranoico no curto (mentalidade haltere)."},
   {"ic":"scale","t":"O Risco de Ruína","b":"Alavancagem excessiva transforma uma queda <strong>temporária</strong> em ruína <strong>permanente</strong>. Jesse Livermore fez fortuna em 1929 e morreu falido — soube ganhar, não manter.","tip":"<strong>Sinal de alerta:</strong> confiar que a coragem que enriqueceu autoriza arriscar tudo.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 5",
  "lessons":["Priorize a sobrevivência: nunca se exponha à ruína.","Mude de ousadia para humildade depois de conquistar.","Tenha folga para não vender no pior momento."]},

 {"slug":"ch06-cauda-longa","sub":"CAPÍTULO 6: Caudas Vencem",
  "intro":"Uma minoria de eventos responde pela maioria dos resultados. Você pode errar a maior parte do tempo e ainda vencer — desde que os poucos acertos (as caudas) sejam grandes o bastante.",
  "cards":[
   {"ic":"wave","t":"Eventos de Cauda (tail events)","b":"Os extremos <strong>raros</strong> dominam o resultado de portfólios, carreiras e negócios. Poucas ações respondem por quase todo o ganho do índice ao longo do tempo.","tip":"<strong>Como aplicar:</strong> avalie o resultado agregado, não a frequência de acertos.","wide":True},
   {"ic":"layers","t":"Errar Muito e Ainda Ganhar","b":"A galeria de <strong>Berggruen</strong>: a maioria das obras perdeu valor, mas um punhado (Picasso, Klee) bastou. Acertar ~1% das compras tornou-o um dos maiores marchands.","tip":"<strong>Regra:</strong> tolere muitos pequenos fracassos — são o custo das poucas caudas enormes."},
   {"ic":"target","t":"O que Mata Não é Errar","b":"O que mata não é errar muito, é <strong>não sobreviver</strong> para acertar a cauda. Vender vencedores cedo e segurar perdedores corta justamente a cauda.","tip":"<strong>Cuidado:</strong> não abandone uma boa estratégia por uma sequência normal de fracassos.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 6",
  "lessons":["Julgue estratégias pelo resultado agregado, não pela taxa de acerto.","Aceite muitos pequenos erros como custo das grandes caudas.","Sobreviva aos fracassos para estar presente nos poucos acertos decisivos."]},

 {"slug":"ch07-liberdade","sub":"CAPÍTULO 7: Liberdade — O Maior Dividendo",
  "intro":"O maior valor que o dinheiro entrega é o controle sobre o próprio tempo. Poder fazer o que quer, quando quer, com quem quer — esse é o dividendo mais alto que a riqueza paga.",
  "cards":[
   {"ic":"key","t":"Controle do Tempo = Riqueza Máxima","b":"Autonomia sobre a agenda <strong>supera qualquer bem material</strong>. O senso de controle sobre a vida prediz felicidade melhor que renda, saúde ou status (Angus Campbell).","tip":"<strong>Como aplicar:</strong> priorize escolhas que ampliem o controle do seu tempo, não só o saldo.","wide":True},
   {"ic":"leaf","t":"Use o Dinheiro para Comprar Tempo","b":"O melhor uso do dinheiro é comprar <strong>autonomia</strong>, não coisas. Reserva = liberdade: a opção de dizer 'não' e de esperar.","tip":"<strong>Modelo mental:</strong> poupança compra a opção de escolher."},
   {"ic":"sword","t":"Renda Alta com Coleira","b":"Ganhar muito <strong>preso à mesa de outro</strong> é riqueza pela metade. Trocar liberdade por status (mais bens, menos controle) é mau negócio.","tip":"<strong>Sinal de alerta:</strong> empregos que maximizam renda e minimizam autonomia.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 7",
  "lessons":["O melhor uso do dinheiro é comprar controle sobre o seu tempo.","Autonomia prediz felicidade melhor que renda absoluta.","Construa reserva para poder dizer 'não' e esperar."]},

 {"slug":"ch08-homem-no-carro","sub":"CAPÍTULO 8: O Paradoxo do Homem no Carro",
  "intro":"Ninguém admira você por suas posses. Quem vê seu carro caro não admira você — projeta a si mesmo dirigindo. Gastamos por um status que o status não entrega.",
  "cards":[
   {"ic":"mask","t":"O Paradoxo do Homem no Carro","b":"Usamos bens para ganhar admiração, mas o observador admira a <strong>coisa</strong> (e a si mesmo), não o dono. Você também não admira o dono do Ferrari — admira o Ferrari.","tip":"<strong>Como aplicar:</strong> pergunte 'compro pelo uso ou pelo olhar dos outros?'.","wide":True},
   {"ic":"bubble","t":"Respeito Vem de Caráter","b":"Humildade, gentileza e empatia rendem <strong>mais admiração</strong> que cavalos-vapor. As pessoas admiram quem as faz sentir bem, não quem exibe bens.","tip":"<strong>Regra:</strong> quer respeito? invista em caráter, não em cifrões."},
   {"ic":"eye","t":"Comprar para a Plateia","b":"Comprar bens caros para conquistar respeito tem efeito <strong>quase nulo</strong>. Não confunda inveja alheia com admiração.","tip":"<strong>Sinal de alerta:</strong> a plateia olha a coisa, não você — e talvez nem esteja olhando.","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 8",
  "lessons":["Bens caros raramente compram a admiração que prometem.","Quer respeito? Invista em humildade e gentileza.","A plateia olha a coisa, não você."]},

 {"slug":"ch09-riqueza-invisivel","sub":"CAPÍTULO 9: Riqueza é o que Você Não Vê",
  "intro":"Rico é a renda alta de agora; riqueza é a renda que você não gastou. A riqueza é, por definição, invisível — são os carros não comprados e os luxos recusados.",
  "cards":[
   {"ic":"eye","t":"Rico vs. Riqueza","b":"<strong>Rico</strong> (rich) financia o consumo; <strong>riqueza</strong> (wealth) é o consumo adiado, convertido em ativos. Você vê o gasto — nunca a conta bancária.","tip":"<strong>Como aplicar:</strong> meça prosperidade pela renda NÃO gasta, não pelo padrão exibido.","wide":True},
   {"ic":"gap","t":"A Riqueza é Escondida","b":"Não dá para 'aprender' riqueza <strong>copiando aparências</strong> — o 'rico aparente' pode estar endividado; o realmente rico parece comum.","tip":"<strong>Cuidado:</strong> tomar quem ostenta como modelo de prosperidade.","warn":True},
   {"ic":"steps","t":"O Teste é Resistir ao Gasto","b":"Construir riqueza é, em essência, <strong>recusar gastos</strong>. Gastar para 'parecer' bem-sucedido destrói a chance de ser.","tip":"<strong>Regra:</strong> a tentação de gastar é o teste; o invisível é o que sobra."},
  ],
  "lessons_title":"Lições-Chave do Capítulo 9",
  "lessons":["Riqueza é renda não gasta — invisível por natureza.","Não confunda gasto visível com prosperidade real.","Construir riqueza é, em essência, recusar gastos."]},

 {"slug":"ch10-poupar-margem","sub":"CAPÍTULO 10: Poupar & Margem de Segurança",
  "intro":"A taxa de poupança está mais sob seu controle que a renda ou o retorno — e depende menos da renda do que do ego. Poupe sem motivo; e planeje sempre com margem de segurança.",
  "cards":[
   {"ic":"leaf","t":"Poupar Sem um Motivo","b":"A poupança não precisa de meta — ela é a <strong>proteção contra o imprevisível</strong>, que é a única certeza. Separe um percentual fixo, com ou sem plano.","tip":"<strong>Como aplicar:</strong> poupe por hábito; não espere um objetivo 'digno' para começar.","wide":True},
   {"ic":"scale","t":"Margem de Segurança","b":"Deixe folga entre o que <strong>pode</strong> acontecer e o que você <strong>precisa</strong> que aconteça. Graham comprava abaixo do valor: errando a estimativa, ainda saía bem.","tip":"<strong>Regra:</strong> planeje para que o plano não precise dar certo."},
   {"ic":"mask","t":"Poupança Depende do Ego","b":"Gastar menos exige <strong>desejar menos status</strong> — provar menos aos outros. Quanto menor o ego, maior a poupança possível.","tip":"<strong>Sinal de alerta:</strong> otimizar tanto o plano que qualquer desvio o quebra (sem folga).","warn":True},
  ],
  "lessons_title":"Lições-Chave do Capítulo 10",
  "lessons":["Poupe por hábito, sem precisar de meta — o imprevisto é certo.","A poupança depende mais do ego (gastar menos) do que da renda.","Sempre embuta margem de segurança: planeje para o plano falhar."]},

 {"slug":"ch11-pessimismo-e-mudanca","sub":"CAPÍTULO 11: Pessimismo, Mudança & Coerência",
  "intro":"O pessimismo soa mais inteligente e captura mais atenção que o otimismo — mas a aposta racional de longo prazo é otimista. E como você vai mudar, evite planos extremos e irreversíveis.",
  "cards":[
   {"ic":"wave","t":"A Sedução do Pessimismo","b":"O medo grita mais alto porque <strong>progresso é lento e ruína é súbita</strong>. Pessimismo parece sabedoria; otimismo parece venda — mas o longo prazo tende a melhorar.","tip":"<strong>Como aplicar:</strong> desconfie do alarme que soa 'esperto demais'.","wide":True},
   {"ic":"pivot","t":"Você Vai Mudar","b":"A <strong>falácia do fim da história</strong>: cada idade acha que é a versão final de si. Subestimamos o quanto vamos mudar de gostos, metas e prioridades.","tip":"<strong>Regra:</strong> evite metas extremas e irreversíveis — deixe espaço para o 'eu futuro' revisar.","warn":True},
   {"ic":"spark","t":"Otimismo Racional","b":"Esperar reveses no <strong>curto prazo</strong> e crescimento no <strong>longo</strong> é a postura coerente. Otimista de longo prazo, realista de curto.","tip":"<strong>Modelo mental:</strong> as duas coisas convivem — paciência com cautela."},
  ],
  "lessons_title":"Lições-Chave do Capítulo 11",
  "lessons":["Desconfie do pessimismo que soa esperto; aposte na melhora de longo prazo.","Você vai mudar — evite metas extremas e irreversíveis.","Seja otimista no longo prazo e cauteloso no curto."]},
]
