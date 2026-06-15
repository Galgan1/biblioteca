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

# Infografico de Instagram (Diretor de Design) — arquetipo NUMEROS (gerar_infografico.py)
NUMEROS = {
 "kicker": "O LIVRO EM NÚMEROS", "tag": "DADOS",
 "stats": [
   {"ic":"clock","pre":"US$","num":"84,2","unit":"bi","star":True,"lbl":"depois dos 50 anos",
    "ctx":"Dos <b>US$ 84,5 bi</b> de Buffett, quase tudo veio após os 50 — o segredo foi o tempo."},
   {"ic":"spiral","pre":"~","num":"75","unit":"anos","lbl":"no jogo, compondo",
    "ctx":"Buffett investe há <b>~75 anos</b>. Tempo &gt; retorno: maximize o horizonte, não a taxa."},
   {"ic":"wave","pre":"~","num":"1","unit":"%","lbl":"de acertos bastou",
    "ctx":"Berggruen errou quase tudo; <b>~1% das obras</b> fez a fortuna. As caudas vencem."},
 ],
 "viz": {"type":"bar","frac":0.0036,"left":"AT&Eacute; OS 50 ANOS","right":"DOS 50 EM DIANTE",
         "title":"De onde veio a fortuna de Buffett","note":"tempo no jogo &rarr; <b>99,6%</b>"},
 "foot": {"ic":"clock","text":"<strong>Sobreviva e fique no jogo.</strong> Não busque o retorno do ano "
          "— deixe os juros compostos trabalharem por décadas."},
}

CHAPTERS = [
 {"slug":"ch01-ninguem-e-doido","sub":"CAPÍTULO 1: Ninguém é Doido",
  "intro":"As pessoas não tomam decisões financeiras malucas — tomam decisões que fazem sentido para elas, dada a história e a geração que viveram. Sucesso com dinheiro é mais comportamento do que conhecimento.",
  "cards":[
      {"ic":"scale","t":"Finanças São Comportamento, Não Física","emph":"Comportamento","b":"O dinheiro é ensinado como ciência exata — fórmulas, planilhas, taxas — mas é vivido como psicologia: medo, ganância, ego, esperança. Por isso o gênio das contas quebra e a faxineira que poupou por décadas morre milionária. <strong>Como você se comporta importa mais do que o que você sabe.</strong> A planilha está certa; é o operador que treme.","tip":"<strong>Como aplicar:</strong> antes de buscar o ativo perfeito, conserte a atitude — poupar, esperar, não entrar em pânico."},
      {"ic":"lens","t":"Ninguém É Doido","emph":"Doido","b":"Aquilo que parece insano na sua planilha faz todo sentido na vida do outro. Quem cresceu na hiperinflação foge da bolsa; quem nasceu em bull market acha o risco gratuito. Cada um viveu cerca de 0,00000001% da história econômica e acha que entende o todo. <strong>Decisões financeiras não nascem de fórmulas, nascem de cicatrizes.</strong>","tip":"<strong>Modelo mental:</strong> pergunte “que vivência o leva a agir assim?” antes de “que erro ele cometeu?”."},
      {"ic":"fork","t":"Cada Um Joga um Jogo Diferente","emph":"Jogo Diferente","b":"O trader que compra na euforia não é tolo — ele joga o jogo de horas, não o de décadas. O problema nasce quando você copia o lance de quem tem outro horizonte, outro risco e outro objetivo, achando que joga a mesma partida. <strong>Bolhas se formam quando investidores de longo prazo começam a imitar especuladores de curto prazo.</strong>","tip":"<strong>Cuidado:</strong> defina seu jogo — prazo, risco, meta — e nunca importe a tática de quem joga outro.","warn":True},
    ],
  "lessons_title":"Lições-Chave do Capítulo 1",
  "lessons":["Comportamento bate inteligência nas finanças.","Antes de julgar, reconstrua a experiência de quem decide.","Saiba qual jogo você joga — e não copie quem joga outro."]},

 {"slug":"ch02-sorte-e-risco","sub":"CAPÍTULO 2: Sorte & Risco",
  "intro":"Sorte e risco são irmãos: ambos são a realidade de que todo resultado é guiado por forças além do esforço. A sorte é o risco visto pelo lado de fora.",
  "cards":[
      {"ic":"fork","t":"Sorte e Risco São Gêmeos","emph":"Gêmeos","b":"Todo resultado carrega um peso de forças fora do seu controle — e a sorte nada mais é que o risco visto pelo lado de fora. Nenhum sucesso é só mérito, nenhum fracasso é só erro. <strong>A mesma decisão pode enriquecer um e arruinar outro, e a diferença não foi a inteligência: foi o acaso.</strong> Julgar resultado sem descontar o azar engana.","tip":"<strong>Como aplicar:</strong> pergunte “quanto disso foi processo replicável e quanto foi puro acaso?”."},
      {"ic":"constellation","t":"Estude o Padrão, Não o Herói","emph":"Herói","b":"O bilionário que largou a faculdade é o pior professor possível: o caso extremo é onde sorte e azar mais distorcem a lição. Por um Gates há mil que fizeram o mesmo e sumiram — só que esses não dão palestra. <strong>Os exemplos mais inspiradores costumam ser os mais inúteis para copiar.</strong> Aprenda com a regra ampla, não com a exceção luminosa.","tip":"<strong>Regra:</strong> não idolatre nem demonize indivíduos — extraia padrões largos de muitos casos."},
      {"ic":"mask","t":"Bill Gates e o Amigo que Não Voltou","emph":"Bill Gates","b":"Gates estudou numa das únicas escolas do mundo com computador em 1968 — sorte de uma em um milhão. Seu colega Kent Evans, igualmente brilhante, morreu num acidente de montanha antes de se formar — azar de uma em um milhão. Mesmo talento, mesma escola, destinos opostos. <strong>O acaso escreve linhas que o esforço não controla.</strong>","tip":"<strong>Cuidado:</strong> seja humilde nos acertos e gentil consigo nos erros — nem tudo foi sua mão.","warn":True},
    ],
  "lessons_title":"Lições-Chave do Capítulo 2",
  "lessons":["Trate sorte e risco como duas faces da mesma moeda.","Não idolatre nem condene casos individuais — extraia padrões.","Humildade nos acertos, autocompaixão nos erros."]},

 {"slug":"ch03-nunca-o-bastante","sub":"CAPÍTULO 3: Nunca o Bastante",
  "intro":"A habilidade financeira mais difícil é fazer a meta parar de se mover. Sem um senso de 'o bastante', nenhum ganho satisfaz — e a busca infinita leva a riscar o que se tem por algo de que não se precisa.",
  "cards":[
      {"ic":"target","t":"A Trave que Sempre se Move","emph":"se Move","b":"A habilidade financeira mais difícil é fazer a meta parar de fugir. Quando a ambição cresce mais rápido que a satisfação, nenhuma cifra basta — você conquista o número dos sonhos e ele já virou o piso. <strong>O teto da comparação social é inalcançável: sempre haverá alguém mais rico, mais à frente, com um pouco mais.</strong> A corrida não tem linha de chegada.","tip":"<strong>Como aplicar:</strong> escreva, antes de buscar mais, qual é o seu “o bastante” — e pare de comparar.","wide":True},
      {"ic":"sword","t":"O que Nunca Vale o Risco","emph":"Nunca Vale","b":"Arriscar o que você tem e precisa por algo de que não precisa é insanidade matemática — e foi o que derrubou Rajat Gupta e Bernie Madoff, que tinham tudo e quiseram mais. Há ativos sem preço de recompra: reputação, liberdade, família, ser amado, a paz de espírito. <strong>Perdidos esses, nenhum lucro os traz de volta.</strong>","tip":"<strong>Sinal de alerta:</strong> dívida e fraude para acelerar ganhos — quem já tem o bastante e ainda aposta o essencial.","warn":True},
      {"ic":"bulb","t":"“Eu Tenho o Bastante”","emph":"o Bastante","b":"Na festa de um bilionário, Kurt Vonnegut provoca Joseph Heller: o anfitrião ganhou num só dia mais do que o livro de Heller renderá na vida inteira. Heller responde com a frase que resume o capítulo: <strong>“Mas eu tenho algo que ele nunca terá — o bastante.”</strong> Reconhecer o suficiente é a única vitória que a comparação não rouba.","tip":"<strong>Regra:</strong> defina o suficiente como destino, não como etapa — só assim o jogo termina a seu favor."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 3",
  "lessons":["Defina seu 'o bastante' antes que a trave se mova sozinha.","Nunca arrisque o que tem (e precisa) por algo de que não precisa.","Há valores acima de qualquer cifra — não os ponha em jogo."]},

 {"slug":"ch04-juros-compostos","sub":"CAPÍTULO 4: A Confusão dos Juros Compostos",
  "intro":"Os juros compostos são contraintuitivos: o que produz fortunas não é o retorno espetacular, é o retorno bom mantido por muito tempo. Tempo é a alavanca que o cérebro subestima.",
  "cards":[
      {"ic":"spiral","t":"A Oitava Maravilha","emph":"Maravilha","b":"O cérebro pensa em linha reta; os juros compostos andam em curva. Um retorno apenas bom, repetido por décadas, produz uma escala que a intuição se recusa a prever — cresce devagar, devagar, e então dispara. <strong>A maior parte da fortuna não vem do retorno espetacular: vem do retorno mediano que ninguém interrompeu.</strong> O tédio é o motor.","tip":"<strong>Modelo mental:</strong> o composto é não-linear — comece cedo e, acima de tudo, fique muito tempo.","wide":True},
      {"ic":"clock","t":"Tempo Vence Retorno","emph":"Tempo","b":"Buffett não é apenas o melhor investidor — é o mais antigo. Dos seus cerca de US$ 84,5 bilhões, quase US$ 84,2 bilhões chegaram depois dos 50 anos, a maior fatia após os 65. <strong>Se tivesse começado aos 30 e parado aos 60 com os mesmos retornos, seria um desconhecido.</strong> O segredo não foi a taxa anual: foi atravessar ~75 anos sem sair.","tip":"<strong>Regra:</strong> maximize o horizonte, não a taxa — alongar o prazo bate refinar o percentual."},
      {"ic":"pin","t":"Não Interrompa à Toa","emph":"Interrompa","b":"Cada saída antecipada não pausa o composto: reinicia a contagem do zero. O resultado vem do tempo dentro do mercado, não de adivinhar o melhor momento de entrar e sair. Quem persegue o ano perfeito troca uma década de juros silenciosos por uma aposta de timing. <strong>Sair “só desta vez” costuma custar a metade do resultado de uma vida.</strong>","tip":"<strong>Cuidado:</strong> buscar o melhor ano em vez de muitos anos medianos seguidos quebra a mágica do composto.","warn":True},
    ],
  "lessons_title":"Lições-Chave do Capítulo 4",
  "lessons":["O resultado vem do tempo no mercado, não do timing.","Um retorno bom e durável vence um retorno alto e curto.","Paciência é a maior vantagem competitiva acessível a qualquer um."]},

 {"slug":"ch05-ficar-rico-continuar-rico","sub":"CAPÍTULO 5: Ficar Rico vs. Continuar Rico",
  "intro":"Conquistar dinheiro e mantê-lo exigem habilidades opostas. Ganhar pede ousadia e otimismo; manter pede humildade e medo de perder. A única estratégia que garante o composto é sobreviver.",
  "cards":[
      {"ic":"mountain","t":"Sobreviver Acima de Tudo","emph":"Sobreviver","b":"Há mil formas de enriquecer e uma só de garantir o composto: não quebrar. Ficar no jogo por décadas vale mais que qualquer retorno excepcional, porque a ruína apaga tudo o que veio antes — e quem é forçado a vender no fundo nunca volta para a recuperação. <strong>A única vantagem que sempre paga é simplesmente continuar de pé.</strong>","tip":"<strong>Como aplicar:</strong> seja financeiramente inquebrável — caixa, dívida baixa, folga para atravessar o pior.","wide":True},
      {"ic":"pivot","t":"Ganhar e Manter São Opostos","emph":"Opostos","b":"As duas metades da fortuna pedem talentos contrários. Conquistar exige ousadia, otimismo, apostar e se expor. Manter exige o avesso: humildade, frugalidade e o medo saudável de que a sorte pode virar. <strong>A coragem que enriqueceu você é exatamente o que pode arruiná-lo depois.</strong> Vencida a etapa de ganhar, troque a mentalidade.","tip":"<strong>Modelo mental:</strong> otimista no longo prazo, paranoico no curto — a mentalidade haltere que sobrevive."},
      {"ic":"scale","t":"O Trader que Morreu Falido","emph":"Falido","b":"Jesse Livermore foi o maior especulador de sua era e fez fortuna apostando contra a quebra de 1929. Mas a mesma audácia que o fez vencer não sabia parar: continuou alavancando, perdeu tudo e morreu sem nada. <strong>Saber ganhar não é saber manter — e a alavancagem transforma uma queda temporária em ruína permanente.</strong>","tip":"<strong>Sinal de alerta:</strong> confiar que a ousadia que enriqueceu autoriza arriscar o patrimônio inteiro.","warn":True},
    ],
  "lessons_title":"Lições-Chave do Capítulo 5",
  "lessons":["Priorize a sobrevivência: nunca se exponha à ruína.","Mude de ousadia para humildade depois de conquistar.","Tenha folga para não vender no pior momento."]},

 {"slug":"ch06-cauda-longa","sub":"CAPÍTULO 6: Caudas Vencem",
  "intro":"Uma minoria de eventos responde pela maioria dos resultados. Você pode errar a maior parte do tempo e ainda vencer — desde que os poucos acertos (as caudas) sejam grandes o bastante.",
  "cards":[
      {"ic":"wave","t":"As Caudas Decidem Tudo","emph":"Caudas","b":"Numa carteira, numa carreira, num negócio, uma minoria de eventos raros responde por quase todo o resultado. O índice sobe porque uma fração das empresas carrega o peso morto do resto; o ganho da vida cabe em poucos anos. <strong>Você pode estar errado na maior parte do tempo e ainda vencer — desde que as poucas vezes em que acerta sejam enormes.</strong>","tip":"<strong>Como aplicar:</strong> julgue uma estratégia pelo resultado agregado, não pela frequência de acertos.","wide":True},
      {"ic":"layers","t":"Errar Muito e Ainda Ganhar","emph":"Errar Muito","b":"O marchand Heinz Berggruen comprou milhares de obras e a maioria perdeu valor — mas um punhado, Picasso, Klee, Matisse, valorizou tanto que o fez um dos maiores negociantes do mundo. Acertou talvez 1% das compras, e bastou. <strong>O custo das poucas caudas gigantes é tolerar uma multidão de pequenos fracassos.</strong>","tip":"<strong>Regra:</strong> trate cada erro barato como ingresso pago para estar presente no acerto que muda tudo."},
      {"ic":"target","t":"O que Mata Não É Errar","emph":"Mata","b":"O fracasso frequente é normal e previsto; o que de fato arruína é não sobreviver até a cauda chegar. Vender o vencedor cedo demais e segurar o perdedor por orgulho corta justamente o evento que pagaria toda a conta. <strong>Abandonar uma boa estratégia por uma sequência normal de perdas é o erro que não se recupera.</strong>","tip":"<strong>Cuidado:</strong> não troque uma estratégia sólida por uma sequência de fracassos que já estava no roteiro.","warn":True},
    ],
  "lessons_title":"Lições-Chave do Capítulo 6",
  "lessons":["Julgue estratégias pelo resultado agregado, não pela taxa de acerto.","Aceite muitos pequenos erros como custo das grandes caudas.","Sobreviva aos fracassos para estar presente nos poucos acertos decisivos."]},

 {"slug":"ch07-liberdade","sub":"CAPÍTULO 7: Liberdade — O Maior Dividendo",
  "intro":"O maior valor que o dinheiro entrega é o controle sobre o próprio tempo. Poder fazer o que quer, quando quer, com quem quer — esse é o dividendo mais alto que a riqueza paga.",
  "cards":[
      {"ic":"key","t":"Controle do Tempo É a Riqueza Máxima","emph":"Controle do Tempo","b":"O maior dividendo que o dinheiro paga não vem em coisas — vem em manhãs em que você decide o que fazer, quando, com quem e por quanto tempo. O psicólogo Angus Campbell achou que o senso de controle sobre a própria vida prevê felicidade melhor que renda, saúde ou status. <strong>Poder dizer “a agenda é minha” é o luxo mais caro que existe.</strong>","tip":"<strong>Como aplicar:</strong> ao decidir, prefira a opção que amplia o controle do seu tempo, não só o saldo.","wide":True},
      {"ic":"leaf","t":"Compre Autonomia, Não Coisas","emph":"Autonomia","b":"O melhor uso do dinheiro é converter renda em independência: a reserva que permite recusar o trabalho ruim, esperar a oportunidade certa, sair sem pedir permissão. Cada real guardado é uma opção comprada. <strong>Poupança não é renúncia ao prazer — é a compra do direito de escolher.</strong> A liberdade tem preço, e ele se paga adiando o gasto.","tip":"<strong>Modelo mental:</strong> sua reserva mede quantos “nãos” você pode dizer antes de precisar de um “sim”."},
      {"ic":"sword","t":"Renda Alta com Coleira","emph":"Coleira","b":"Desde os anos 1950 a riqueza média se multiplicou, mas a felicidade não acompanhou — em parte porque muitos ganharam mais bens e perderam o controle das próprias horas: jornadas, e-mails fora do expediente, disponibilidade total. <strong>Ganhar muito preso à mesa de outro é riqueza pela metade.</strong> Trocar autonomia por status é mau negócio.","tip":"<strong>Sinal de alerta:</strong> empregos que maximizam a renda e minimizam o controle sobre o seu próprio tempo.","warn":True},
    ],
  "lessons_title":"Lições-Chave do Capítulo 7",
  "lessons":["O melhor uso do dinheiro é comprar controle sobre o seu tempo.","Autonomia prediz felicidade melhor que renda absoluta.","Construa reserva para poder dizer 'não' e esperar."]},

 {"slug":"ch08-homem-no-carro","sub":"CAPÍTULO 8: O Paradoxo do Homem no Carro",
  "intro":"Ninguém admira você por suas posses. Quem vê seu carro caro não admira você — projeta a si mesmo dirigindo. Gastamos por um status que o status não entrega.",
  "cards":[
      {"ic":"mask","t":"O Paradoxo do Homem no Carro","emph":"Homem no Carro","b":"Como manobrista, Housel viu por anos a multidão cobiçar os carros de luxo que ele estacionava — e ninguém, nunca, olhava o motorista. Cada um se imaginava dentro do carro, não admirando o dono. <strong>Quem compra o Ferrari para ser admirado some atrás do próprio objeto de desejo.</strong> Você usa o bem como sinal; o outro vê só o bem.","tip":"<strong>Como aplicar:</strong> pergunte “compro isto pelo uso ou pelo olhar de uma plateia que nem está olhando?”.","wide":True},
      {"ic":"bubble","t":"Respeito Vem do Caráter","emph":"Caráter","b":"A admiração que se busca com cavalos-vapor chega muito mais por humildade, gentileza e empatia. As pessoas se afeiçoam a quem as faz sentir bem, não a quem exibe o relógio. <strong>O respeito que o dinheiro tenta comprar é justamente o que o dinheiro não vende.</strong> Você não admira o dono do carro caro — então por que esperaria o contrário?","tip":"<strong>Regra:</strong> quer ser respeitado? Invista em caráter e atenção ao outro, não em cifrões visíveis."},
      {"ic":"eye","t":"Comprar para a Plateia","emph":"Plateia","b":"Gastar caro para conquistar respeito tem efeito quase nulo — e, pior, costuma render inveja, que é fácil de confundir com admiração. A plateia que você imagina avaliando suas posses está, na verdade, ocupada com as próprias. <strong>O bem comprado para impressionar impressiona menos do que custou, e por muito menos tempo.</strong>","tip":"<strong>Sinal de alerta:</strong> não confunda a inveja alheia com admiração — uma corrói, a outra nem chega.","warn":True},
    ],
  "lessons_title":"Lições-Chave do Capítulo 8",
  "lessons":["Bens caros raramente compram a admiração que prometem.","Quer respeito? Invista em humildade e gentileza.","A plateia olha a coisa, não você."]},

 {"slug":"ch09-riqueza-invisivel","sub":"CAPÍTULO 9: Riqueza é o que Você Não Vê",
  "intro":"Rico é a renda alta de agora; riqueza é a renda que você não gastou. A riqueza é, por definição, invisível — são os carros não comprados e os luxos recusados.",
  "cards":[
      {"ic":"eye","t":"Rico É Renda; Riqueza É o que Sobra","emph":"o que Sobra","b":"Rico é a renda alta de agora — financia o carro novo, o relógio, a viagem. Riqueza é a renda que você decidiu não gastar, convertida em ativos guardados. Uma se vê; a outra, por definição, não. <strong>A riqueza é feita justamente dos carros não comprados e dos luxos recusados.</strong> Você enxerga o gasto do vizinho, nunca a conta bancária dele.","tip":"<strong>Como aplicar:</strong> meça prosperidade pela renda que você NÃO gastou, não pelo padrão que exibe.","wide":True},
      {"ic":"gap","t":"A Riqueza Não Se Copia pela Aparência","emph":"Aparência","b":"Como a riqueza é invisível, não dá para aprendê-la imitando quem parece rico — porque o que parece muitas vezes não é. O homem do carro trocado todo ano e dos relógios pode ter patrimônio mínimo e dívida alta; o realmente rico passa por comum. <strong>Tomar o ostentador como modelo é copiar a fatura, não a fortuna.</strong>","tip":"<strong>Cuidado:</strong> não use quem ostenta como prova de sucesso — a aparência de rico e a riqueza raramente moram juntas.","warn":True},
      {"ic":"steps","t":"O Teste É Resistir ao Gasto","emph":"Resistir","b":"Construir riqueza, no fundo, é um único gesto repetido: dizer não ao gasto que parecia merecido. Cada compra adiada vira patrimônio; cada esforço para “parecer” bem-sucedido destrói a chance de de fato ser. <strong>A tentação visível é o teste; o que sobra invisível é a nota.</strong> Riqueza é a soma de prazeres que você optou por não exibir.","tip":"<strong>Regra:</strong> trate a renda não gasta como o placar real — o consumo é despesa, não troféu."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 9",
  "lessons":["Riqueza é renda não gasta — invisível por natureza.","Não confunda gasto visível com prosperidade real.","Construir riqueza é, em essência, recusar gastos."]},

 {"slug":"ch10-poupar-margem","sub":"CAPÍTULO 10: Poupar & Margem de Segurança",
  "intro":"A taxa de poupança está mais sob seu controle que a renda ou o retorno — e depende menos da renda do que do ego. Poupe sem motivo; e planeje sempre com margem de segurança.",
  "cards":[
      {"ic":"leaf","t":"Poupar Sem um Motivo","emph":"Sem um Motivo","b":"A poupança não precisa de uma meta para começar — esperar o objetivo “digno” é a desculpa que adia tudo. Ela é a proteção contra o imprevisível, e o imprevisível é a única certeza da vida financeira. <strong>Poupar sem destino específico é construir a opção de lidar com o que você ainda nem consegue imaginar.</strong> Guarde um percentual fixo, plano ou não.","tip":"<strong>Como aplicar:</strong> poupe por hábito automático — antes de saber para quê, justamente porque não dá para saber.","wide":True},
      {"ic":"scale","t":"Margem de Segurança","emph":"Margem de Segurança","b":"Benjamin Graham comprava ativos bem abaixo do valor estimado: errando a conta, ainda saía bem. A ideia vale para a vida inteira — deixe folga entre o que pode acontecer e o que você precisa que aconteça. <strong>Planeje para que o plano não precise dar certo.</strong> A folga é o que transforma um erro de cálculo em incidente, não em ruína.","tip":"<strong>Regra:</strong> dimensione tudo para sobreviver ao cenário ruim, não só ao cenário esperado."},
      {"ic":"mask","t":"Poupança Depende do Ego","emph":"Ego","b":"Quanto você poupa depende menos da renda e mais do quanto você precisa provar aos outros. Gastar menos é, no fundo, desejar menos status — e quem se liberta da plateia descobre uma capacidade de poupar que a renda nunca explicou. <strong>O abismo entre o que você ganha e o que gasta é cavado pelo ego, não pelo salário.</strong>","tip":"<strong>Sinal de alerta:</strong> otimizar tanto o plano que não sobra folga — sem ego sob controle, qualquer desvio quebra.","warn":True},
    ],
  "lessons_title":"Lições-Chave do Capítulo 10",
  "lessons":["Poupe por hábito, sem precisar de meta — o imprevisto é certo.","A poupança depende mais do ego (gastar menos) do que da renda.","Sempre embuta margem de segurança: planeje para o plano falhar."]},

 {"slug":"ch11-pessimismo-e-mudanca","sub":"CAPÍTULO 11: Pessimismo, Mudança & Coerência",
  "intro":"O pessimismo soa mais inteligente e captura mais atenção que o otimismo — mas a aposta racional de longo prazo é otimista. E como você vai mudar, evite planos extremos e irreversíveis.",
  "cards":[
      {"ic":"wave","t":"A Sedução do Pessimismo","emph":"Pessimismo","b":"O alarme sempre soa mais inteligente que a esperança, e por um motivo estrutural: o progresso é lento e silencioso, enquanto a ruína é súbita e barulhenta. Por isso o pessimista parece sábio e o otimista parece vendedor ingênuo. <strong>Mas a aposta racional de longo prazo é otimista — o mundo tende a melhorar apesar dos reveses.</strong>","tip":"<strong>Como aplicar:</strong> desconfie do alarme que soa “esperto demais” e pese a tendência histórica de melhora.","wide":True},
      {"ic":"pivot","t":"Você Vai Mudar","emph":"Mudar","b":"A falácia do fim da história: em cada idade a gente acha que chegou à versão final de si mesmo. O jovem jura que nunca mudará de gosto, profissão ou estilo — e aos quarenta mudou todos. <strong>Subestimamos sistematicamente o quanto nossas metas e prioridades vão se transformar.</strong> Amarrar a vida a uma meta extrema é apostar contra o próprio futuro.","tip":"<strong>Regra:</strong> evite metas extremas e irreversíveis — deixe espaço para o “eu futuro” revisar sem punição alta.","warn":True},
      {"ic":"spark","t":"Otimismo Racional","emph":"Racional","b":"As duas posturas convivem e não se contradizem: esperar reveses no curto prazo e crescimento no longo é a coerência que mantém alguém no jogo. O realismo de curto prazo evita a ruína; o otimismo de longo prazo paga o composto. <strong>Otimista de longo prazo, cauteloso de curto — paciência casada com cautela.</strong>","tip":"<strong>Modelo mental:</strong> aposte no longo prazo melhorando, mas blinde o curto prazo contra o golpe que tira você do jogo."},
    ],
  "lessons_title":"Lições-Chave do Capítulo 11",
  "lessons":["Desconfie do pessimismo que soa esperto; aposte na melhora de longo prazo.","Você vai mudar — evite metas extremas e irreversíveis.","Seja otimista no longo prazo e cauteloso no curto."]},
]
