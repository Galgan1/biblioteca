# SKILL — Aprofundador de Textos do Carrossel (Biblioteca · Minuto Real)

> **Para o Gemini.** Você é um redator editorial de não-ficção em **português do Brasil**.
> Sua tarefa: pegar os cards rasos de um livro e transformá-los em texto **profundo,
> quente e premium** para os slides de carrossel da Biblioteca — sem inventar fatos,
> fiel à tese do autor. Cada slide é uma página fotografada; o texto é a alma dela.

---

## O que você recebe

Para **um livro por vez**, você recebe:

1. **Ficha do livro** — título, autor, subtítulo, ideia central.
2. **Os capítulos**, cada um com seu `slug`, título e os **cards atuais (rasos)** —
   já com ícone (`ic`), título (`t`) e um corpo curto (`b`). Esse é o seu **esqueleto
   de partida**: a estrutura está certa, falta profundidade e calor.

Você **mantém** o número de cards e os `slug` dos capítulos. Você **aprofunda** cada card.

---

## A RÉGUA (o padrão de qualidade — siga à risca)

Cada card é um objeto com estes campos:

| campo | obrigatório | o que é |
|-------|-------------|---------|
| `ic`   | sim | nome do ícone de linha (use a LISTA abaixo; mantenha o do esqueleto, salvo se houver um claramente melhor). |
| `t`    | sim | título do card — a grande ideia, **2 a 5 palavras**, em Caixa Alta de Título. |
| `emph` | recomendado | **um trecho EXATO de `t`** (substring literal) que será posto em itálico — a "alma" do título. Tem que aparecer idêntico dentro de `t`. |
| `b`    | sim | o corpo. **3 a 4 frases, ~260 a 340 caracteres.** pt-BR, 2ª pessoa, concreto, editorial e caloroso (não acadêmico, não lista). **Exatamente UMA `<strong>…</strong>`** marcando a frase-bomba. Aspas curvas `“ ”`. |
| `tip`  | recomendado | um fechamento prático no formato `"<strong>Rótulo:</strong> frase curta."`. Rótulos válidos: **Modelo mental, Sinal de alerta, Como aplicar, Regra, Prática, Pergunta-chave, Armadilha, Atalho**. |
| `warn` | ~1 por capítulo | `true` no card de **alerta/perigo** do capítulo (renderiza em coral). No máximo um por capítulo. |

### Princípios de redação
- **Uma ideia por card.** Não empilhe conceitos; aprofunde um só.
- **Calor, não frieza.** Escreva como um grande autor de não-ficção falando com o leitor — imagens concretas, ritmo, 2ª pessoa. Nada de "neste capítulo o autor argumenta que…".
- **Fidelidade.** Use as ideias REAIS do livro (estão no esqueleto + na ficha). Não invente dados, estatísticas, nomes ou citações.
- **A bomba.** A única `<strong>` marca o coração da ideia — a frase que a pessoa printaria.
- **O `tip` paga o ingresso.** Tem que ser acionável: algo que o leitor FAZ ou PERCEBE.
- **Aspas sempre curvas** `“ ”` (nunca `"`). Travessão `—` quando couber.
- **pt-BR sempre.** Nada de português de Portugal (ex.: use "você", "celular", "tela", "ônibus").

### Ícones válidos (campo `ic` — use SÓ estes nomes)
```
arrow book bookmark bubble bulb cards clock constellation eye fork gap key
layers leaf lens link mask masks mountain person pin pivot play scale shelf
shield spark spiral steps sword target triangle wave wrench
```

---

## PADRÃO-OURO (copie este nível de profundidade e calor)

Do livro *As Leis da Natureza Humana* (Robert Greene), capítulo `ch01-irracionalidade`:

```json
{
  "ch01-irracionalidade": {
    "cards": [
      {"ic":"wave","t":"A Emoção Chega Primeiro","emph":"Primeiro","b":"Você sente primeiro e justifica depois — nunca o contrário. A emoção dispara antes do pensamento, e a razão corre atrás dando motivos nobres ao que o corpo já decidiu. Racionalidade não é ausência de emoção: é a emoção <strong>vista de fora e regulada</strong> — e tudo começa em admitir-se mais irracional do que pensa.","tip":"<strong>Modelo mental:</strong> trate a emoção como clima, não como verdade — ela informa, não dita."},
      {"ic":"eye","t":"A Baixa Intensidade Engana Mais","emph":"Baixa Intensidade","b":"A raiva explícita passa; o ressentimento crônico, a inveja morna, o tédio que vira pressa — esses corroem o juízo <strong>sem disparar alarme</strong>, fingindo-se de razão. O perigo não é o furacão visível: é a corrente fria que arrasta devagar. Quanto mais “lógico” você se sente, mais vale desconfiar.","tip":"<strong>Sinal de alerta:</strong> certeza calma e definitiva costuma ser emoção disfarçada de clareza.","warn":true},
      {"ic":"lens","t":"Os Vieses São Lentes Coloridas","emph":"Lentes Coloridas","b":"Confirmação, convicção, aparência, grupo, culpa, superioridade: seis lentes que tingem tudo a favor do <strong>ego</strong>. Você não as arranca — aprende a cor de cada uma e desconta a distorção antes de agir. Sentir muito não torna nada verdadeiro.","tip":"<strong>Como aplicar:</strong> antes de decidir, pergunte “qual viés me favoreceria agora?” — e corrija a rota."},
      {"ic":"gap","t":"A Liberdade Mora no Intervalo","emph":"Intervalo","b":"Entre o que te acontece e o que você faz existe uma fresta — e nela cabe toda a sua liberdade. Uma pausa, nomear a emoção, ver-se como veria um estranho: cada gesto <strong>alarga a fresta</strong> e devolve o comando ao Adulto, tirando-o da Criança e do Pai que reagem por impulso.","tip":"<strong>Regra:</strong> quando a intensidade for alta, espere 24h. Pressa emocional quase nunca decide bem."}
    ]
  }
}
```

Repare: `emph` é um pedaço literal de `t`; uma só `<strong>` por corpo; `tip` rotulado e prático; um `warn:true` no card de alerta; aspas curvas; tom de autor, não de resumo escolar.

---

## FORMATO DE SAÍDA (obrigatório — não desvie)

Devolva **UM único bloco ```json**, um objeto cujas chaves são os `slug` dos capítulos
recebidos (na ordem recebida), cada um com `{"cards":[ … ]}`:

```json
{
  "ch01-...": {"cards":[ {card}, {card}, {card} ]},
  "ch02-...": {"cards":[ {card}, {card}, {card} ]}
}
```

Regras do retorno:
- **Todos** os capítulos recebidos, nenhum a mais, nenhum a menos.
- **Mesmos `slug`** que vieram no esqueleto (copie exatos).
- **Mesma contagem de cards** por capítulo que veio no esqueleto.
- JSON **válido** (aspas duplas nas chaves; as aspas curvas `“ ”` ficam DENTRO das strings, isso é permitido). Sem comentários, sem texto fora do bloco.
- `warn` só quando for `true` (pode omitir nos demais). `emph`/`tip` podem ser omitidos só se realmente não couberem — mas o normal é ter.

O resultado vira `_kit_preview/text/<slug>.json` e entra direto no pipeline da Biblioteca.


---

# LIVRO PARA APROFUNDAR: A Insustentável Leveza do Ser — Milan Kundera

**Subtítulo:** VISÃO GERAL · LEVEZA, PESO E O QUE DÁ SENTIDO À VIDA
**Ideia central:** Se vivemos uma vez só — e tudo que acontece acontece pela primeira e única vez —, nossas escolhas têm uma leveza insuportável ou um peso esmagador? Kundera encena essa pergunta em quatro destinos na Praga da invasão soviética de 1968, sem jamais respondê-la.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-leveza-peso-eterno-retorno` — CAPÍTULO 1: Leveza, Peso e o Eterno Retorno
- `ch02-parte1-leveza-e-peso` — CAPÍTULO 2: Parte 1 — Leveza e Peso (Tomáš e Tereza)
- `ch03-parte2-alma-e-corpo` — CAPÍTULO 3: Parte 2 — A Alma e o Corpo (Tereza por dentro)
- `ch04-parte3-palavras-incompreendidas` — CAPÍTULO 4: Parte 3 — Palavras Incompreendidas (Sabina × Franz)
- `ch05-parte4-alma-e-corpo` — CAPÍTULO 5: Parte 4 — A Alma e o Corpo (Tereza, o Regime)
- `ch06-parte5-leveza-e-peso` — CAPÍTULO 6: Parte 5 — Leveza e Peso (Tomáš, Édipo, as Vidraças)
- `ch07-parte6-a-grande-marcha` — CAPÍTULO 7: Parte 6 — A Grande Marcha (O Kitsch)
- `ch08-parte7-o-sorriso-de-karenin` — CAPÍTULO 8: Parte 7 — O Sorriso de Karenin (O Idílio)
- `ch09-narrador-estrutura-simbolos` — CAPÍTULO 9: O Narrador, a Estrutura e os Símbolos

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-leveza-peso-eterno-retorno": {
  "cards": [
   {
    "ic": "scale",
    "t": "O Peso Máximo e a Leveza Real",
    "b": "Se tudo se repetisse infinitamente (eterno retorno de Nietzsche), cada gesto carregaria uma 'carga atroz de responsabilidade' — o <strong>peso máximo</strong>. Mas não há retorno: a história é 'leve como uma pena'. Essa ausência de retorno <strong>torna tudo perdoado de antemão</strong> — e, portanto, leve.",
    "tip": "<strong>Para refletir:</strong> Kundera não acredita no eterno retorno — usa-o como régua para medir o quanto a vida real é leve. O peso máximo imaginário revela, por contraste, a leveza real."
   },
   {
    "ic": "spark",
    "t": "Einmal ist Keinmal",
    "b": "'<strong>Uma vez é nenhuma vez</strong>' — o que acontece só uma vez é como se não tivesse acontecido. Vivemos o <strong>primeiro rascunho já em definitivo</strong>, sem ensaio, sem comparação com a vida que não vivemos. Daí a angústia das escolhas de Tomáš.",
    "tip": "<strong>Modelo mental:</strong> não podemos comparar a vida vivida com a não vivida — qualquer julgamento retrospectivo das próprias escolhas esbarra nesse paradoxo."
   },
   {
    "ic": "fork",
    "t": "O Paradoxo do Título",
    "b": "O título é um <strong>oxímoro programático</strong>: o que é leve deveria ser fácil de suportar — e justamente não é. A leveza do ser é insuportável porque, sem peso, nada importa. O peso esmaga; a leveza esvaziara. <strong>A obra não decide entre os dois polos</strong> — encena-os.",
    "tip": "<strong>Para refletir:</strong> quando foi a última vez que uma decisão 'sem consequências' pesou mais do que esperava — justamente porque parecia leve demais?"
   }
  ]
 },
 "ch02-parte1-leveza-e-peso": {
  "cards": [
   {
    "ic": "constellation",
    "t": "Os Seis Acasos",
    "b": "Tomáš e Tereza só se encontram por uma cadeia de coincidências improváveis — <strong>seis acasos</strong> minúsculos e frágeis como o bater de asas de um pássaro. O que ele tomaria por destino era <strong>pura contingência</strong>. A beleza (um motivo musical no rádio) converte acaso em sentido amoroso.",
    "tip": "<strong>Para refletir:</strong> o que você chama de 'destino' na sua história pessoal seria, como no romance, uma cadeia de acasos que a memória sacraliza?"
   },
   {
    "ic": "leaf",
    "t": "A Compaixão Como Armadilha",
    "b": "Tereza chega doente à casa de Tomáš; sentir o sofrimento dela como próprio (<em>com-paixão</em> = sofrer com) é o que o prende. <strong>O amor de Tomáš não é desejo — é a impossibilidade de não sofrer o sofrimento do outro.</strong> O peso que ele temia entra pela porta da compaixão.",
    "tip": "<strong>Modelo mental:</strong> a compaixão kunderiana não é piedade que olha de cima — é sofrer com, no mesmo plano. É essa simetria de sofrimento que cria o vínculo mais difícil de cortar."
   },
   {
    "ic": "fork",
    "t": "Es Muss Sein?",
    "b": "Tomáš oscila: deve assumir o peso de Tereza ou voltar à leveza? <strong>Sem o eterno retorno, não há como saber qual escolha é a certa</strong> — só viverá uma das opções, sem comparação possível. 'Tem de ser?' é a pergunta que o livro inteiro tenta responder — sem responder.",
    "tip": "<strong>Para refletir:</strong> em uma decisão irreversível que você enfrentou, o que o fez senti-la como 'necessidade' — e quanto disso era, na verdade, contingência que você transformou em fado?"
   }
  ]
 },
 "ch03-parte2-alma-e-corpo": {
  "cards": [
   {
    "ic": "person",
    "t": "O Drama do Dualismo",
    "b": "Tereza quer que seu corpo seja a expressão única e visível de sua alma — mas teme que seja apenas um corpo entre milhões, <strong>intercambiável</strong>. O ciúme em relação às traições de Tomáš ataca exatamente essa ferida: se o sexo 'não tem alma', o corpo é coisa banal — e Tereza não é ninguém.",
    "tip": "<strong>Para refletir:</strong> o ciúme de Tereza é metafísico, não só sentimental — está em jogo se a pessoa é única ou substituível. Em que relações você experimenta essa ansiedade de singularidade?"
   },
   {
    "ic": "eye",
    "t": "O Espelho e a Alma",
    "b": "Tereza diante do espelho, tentando ver a alma por trás do rosto. Por um instante parece vê-la; no seguinte, vê apenas rosto, pele e ossos — <strong>um invólucro intercambiável</strong>. O terror não é de feiura: é de não ser ninguém. É contra esse mundo (o da mãe que negava o pudor) que ela luta.",
    "tip": "<strong>Modelo mental:</strong> a câmera fotográfica será o modo de Tereza agir e se afirmar como sujeito (registrar a invasão soviética) — ver em vez de apenas ser visto."
   },
   {
    "ic": "wave",
    "t": "A Vertigem Kunderiana",
    "b": "Vertigem não é medo de cair — é o <strong>desejo de cair</strong>, a atração pela própria fraqueza, pelo abismo. Tereza sente vertigem diante da força de Tomáš e da própria submissão. É também a forma do amor por alguém que sabe que vai machucá-la.",
    "tip": "<strong>Para refletir:</strong> a forma do romance (repetir a mesma cena por dois pontos de vista) é ela mesma uma tese — a verdade muda conforme a alma que a vive."
   }
  ]
 },
 "ch04-parte3-palavras-incompreendidas": {
  "cards": [
   {
    "ic": "bubble",
    "t": "O Dicionário das Palavras Mal-Entendidas",
    "b": "Para Franz, <strong>fidelidade</strong> é a virtude suprema. Para Sabina, a virtude é a <strong>traição</strong> — sair da fila, romper o estabelecido. Para Franz, as manifestações são a 'vida verdadeira'. Para Sabina, que viveu o desfile obrigatório comunista, são horror. <strong>As mesmas palavras, mundos incompatíveis.</strong>",
    "tip": "<strong>Como aplicar:</strong> em qualquer conflito de relacionamento — amoroso, profissional, familiar — liste as palavras-chave de cada lado e pergunte: 'elas realmente significam o mesmo para os dois?'"
   },
   {
    "ic": "triangle",
    "t": "A Traição Como Valor de Sabina",
    "b": "Sabina trai em cadeia — o pai, o marido, a pátria — e descobre que a <strong>leveza absoluta termina no vazio</strong>: depois de trair tudo, não resta nada para trair. É a demonstração de que a leveza, levada ao extremo, vira o mais insuportável dos fardos. O oposto do peso não salva.",
    "tip": "<strong>Para refletir:</strong> Sabina é a personagem que mais longe leva a filosofia da leveza — e quem paga seu preço. O que acontece quando a liberdade total de não se comprometer com nada é conquistada?"
   },
   {
    "ic": "mask",
    "t": "O Chapéu-Coco — O Sentido Que Se Move",
    "b": "O chapéu preto do avô de Sabina muda de sentido a cada retorno: é jogo erótico, depois identidade, depois memória do passado perdido. O <strong>mesmo objeto, sentidos opostos</strong>. Ensina a ler todo o romance: o sentido é móvel, depende de quem olha e de quando.",
    "tip": "<strong>Modelo mental:</strong> como o chapéu-coco, motivos e símbolos na obra retornam transformados — como temas musicais num desenvolvimento de sonata. Siga-os ao longo do livro."
   }
  ]
 },
 "ch05-parte4-alma-e-corpo": {
  "cards": [
   {
    "ic": "person",
    "t": "A Leveza Não É Transferível",
    "b": "Tereza tenta experimentar o sexo 'leve', separado de sentimento — e fracassa. Em vez de libertação, vem a náusea. <strong>O que liberta um pode aprisionar o outro</strong>; corpo e alma se ligam de modo diferente em cada pessoa. A fenda entre Tomáš e Tereza é existencial, não moral.",
    "tip": "<strong>Para refletir:</strong> a diferença entre Tomáš e Tereza não é que um seja 'melhor' que o outro — é que habitam estruturas existenciais opostas. Nenhuma é ensinável."
   },
   {
    "ic": "eye",
    "t": "Público × Privado Sob Vigilância",
    "b": "Em Praga após 1968, a polícia secreta grava conversas íntimas. <strong>A fronteira entre o quarto e o Estado desaparece</strong>: a intimidade vira prova, a vida privada vira espetáculo de controle. Sob o totalitarismo, não existe vida privada.",
    "tip": "<strong>Modelo mental:</strong> o totalitarismo não invade só a praça pública — invade o quarto. O pessoal é, à força, político. É a versão 'macro' do dualismo corpo × alma (o corpo público capturado pelo regime)."
   },
   {
    "ic": "wave",
    "t": "O Pesadelo da Igualdade Forçada",
    "b": "Tereza tem pesadelos de mulheres nuas marchando uniformizadas — imagens do terror de ser <strong>um corpo entre corpos iguais, sem alma</strong>. É o mundo da mãe e o mundo do totalitarismo fundidos num símbolo. A ameaça existencial e a política têm a mesma forma.",
    "tip": "<strong>Para refletir:</strong> os sonhos de Tereza são o lugar onde o pessoal e o político se fundem — Kundera mostra que o regime não só proíbe liberdades; destrói a singularidade da alma."
   }
  ]
 },
 "ch06-parte5-leveza-e-peso": {
  "cards": [
   {
    "ic": "eye",
    "t": "A Metáfora de Édipo",
    "b": "Édipo não quis matar o pai nem desposar a mãe — mas ao descobrir a verdade, <strong>arrancou os próprios olhos</strong>. Quem diz 'não sabia dos crimes' não está absolvido: a ignorância não desculpa, e a culpa compartilhada pede o mesmo gesto. O regime entende a metáfora literária como <strong>crime político</strong>.",
    "tip": "<strong>Para refletir:</strong> a questão de Kundera via Édipo — 'é suficiente não saber?' — tem aplicação direta a qualquer situação em que alegamos inocência pela ignorância de consequências que deveríamos ter investigado."
   },
   {
    "ic": "spark",
    "t": "A Retratação Recusada",
    "b": "Tomáš recusa assinar a retratação — não por heroísmo ideológico, mas por não suportar <strong>dizer por escrito o contrário do que pensa</strong>. Perde a medicina, vira limpador de vidraças. A fidelidade ao próprio eu pode custar tudo — e não é nem heroísmo nem covardia.",
    "tip": "<strong>Modelo mental:</strong> o gesto de Tomáš não é político — é de integridade mínima. O que você preservaria mesmo ao custo da carreira?"
   },
   {
    "ic": "leaf",
    "t": "A Leveza da Queda",
    "b": "Limpando vidraças, Tomáš sente-se estranhamente <strong>livre</strong>: sem carreira a defender, sem peso a proteger. A perda de status social vira leveza ambígua — simultaneamente alívio e dissolução. Aquilo que chamamos de destino era acaso que a memória sacraliza como <strong>es muss sein</strong>.",
    "tip": "<strong>Para refletir:</strong> Kundera revela que 'tem de ser' era contingência — a necessidade que Tomáš atribuía à profissão tinha raízes tão acidentais quanto os seis acasos que o levaram a Tereza."
   }
  ]
 },
 "ch07-parte6-a-grande-marcha": {
  "cards": [
   {
    "ic": "mask",
    "t": "O Kitsch e a Segunda Lágrima",
    "b": "Kitsch = a recusa da morte, do ridículo, do acaso — o 'biombo que esconde a morte'. Sua fórmula: <strong>a segunda lágrima</strong>. A primeira ('que comovente, as crianças na grama!') é humana. A segunda ('que comovente, comover-me junto com toda a humanidade!') é o kitsch — <strong>a comoção com a própria comoção</strong>.",
    "tip": "<strong>Teste:</strong> na próxima vez que sentir uma emoção 'grande' em público — num desfile, numa causa, numa campanha —, pergunte: estou sentindo pelo objeto da emoção, ou estou me comovendo com minha própria comoção?"
   },
   {
    "ic": "triangle",
    "t": "A Ditadura do Coração",
    "b": "O kitsch exige <strong>unanimidade emocional</strong> e expulsa a dúvida, a ironia, o individual. 'No reino do kitsch totalitário, as respostas são dadas de antemão e excluem qualquer pergunta.' Por isso <strong>todo totalitarismo é kitsch</strong> — e o kitsch totalitário bane tudo que destoa do desfile.",
    "tip": "<strong>Sinal de alerta:</strong> quando um grupo exige que você sinta o que 'todos' sentem, sob pena de exclusão, você está diante da ditadura do coração — seja ela comunista, democrática ou familiar."
   },
   {
    "ic": "wave",
    "t": "O Kitsch É Universal",
    "b": "Há kitsch comunista, fascista, católico e democrático. 'O kitsch é parte da condição humana' — ninguém escapa por inteiro. Até Sabina, que combate o kitsch, tem o seu: a imagem da casa iluminada à noite, a família feliz. <strong>Combatê-lo é tarefa sem fim.</strong>",
    "tip": "<strong>Para refletir:</strong> qual é o kitsch particular que você cultiva — a imagem de realização que 'não pode faltar' na sua vida e que você recusa examinar de perto?"
   }
  ]
 },
 "ch08-parte7-o-sorriso-de-karenin": {
  "cards": [
   {
    "ic": "leaf",
    "t": "O Amor Idílico e o Tempo Circular",
    "b": "O único amor verdadeiramente idílico do livro é o amor por um animal: <strong>sem ciúme, sem futuro a conquistar, sem busca de reciprocidade</strong>. Karenin vive no tempo circular da repetição amada — o paraíso que os humanos perderam ao entrar no tempo linear do progresso e do desejo.",
    "tip": "<strong>Para refletir:</strong> Kundera sugere que talvez seja o único amor pelo qual o homem não merece ser perdoado de tê-lo recebido melhor do que deu. O que seria viver com mais desse tempo circular na vida cotidiana?"
   },
   {
    "ic": "scale",
    "t": "A Leveza Finalmente Habitável",
    "b": "Despojados de tudo (carreira, pátria, juventude), Tomáš e Tereza alcançam uma reconciliação. Tereza descobre que a 'queda' os trouxe à única felicidade possível. <strong>O peso, no fim, foi também o que os salvou.</strong> A leveza e o peso encontram repouso frágil — não vitória de um polo.",
    "tip": "<strong>Modelo mental:</strong> o idílio de Karenin é a leveza redimida — não o vazio de Sabina, mas a paz da repetição amada. A felicidade humilde, fora da Grande Marcha, à beira do fim."
   },
   {
    "ic": "mountain",
    "t": "A Morte Sem Biombo",
    "b": "Karenin tem câncer; Tomáš, o médico, decide sacrificá-lo. Encarar essa morte <strong>sem enfeite, sem segunda lágrima, com simples ternura e dor</strong> é o oposto do kitsch. O idílio só é verdadeiro porque inclui a morte — não a nega. O biombo caiu.",
    "tip": "<strong>Para refletir:</strong> Kundera revela a morte de Tomáš e Tereza antes do fim — para que o foco recaia sobre a felicidade do instante, não sobre o desfecho trágico. O que muda na sua experiência da vida quando você lembra da sua finitude?"
   }
  ]
 },
 "ch09-narrador-estrutura-simbolos": {
  "cards": [
   {
    "ic": "book",
    "t": "O Romance Que Pensa",
    "b": "O narrador-ensaísta não desaparece atrás da história: pensa em voz alta, cita filósofos, <strong>confessa que os personagens são ficção</strong> ('Tomáš nasceu da frase <em>einmal ist keinmal</em>'). Isso desmonta a ilusão realista: o leitor é convidado a pensar, não a se iludir.",
    "tip": "<strong>Como ler:</strong> cada personagem é uma hipótese posta à prova. Tomáš = leveza/'es muss sein'. Tereza = peso/corpo-alma. Sabina = traição/fuga do kitsch. Franz = fidelidade/Grande Marcha."
   },
   {
    "ic": "wave",
    "t": "Composição Musical / Polifonia",
    "b": "Sete partes como sete movimentos — títulos que se repetem em espelho ('Leveza e Peso' 1 e 5; 'A Alma e o Corpo' 2 e 4). <strong>Motivos retornam transformados</strong> como temas musicais: <em>es muss sein</em>, o chapéu-coco, a segunda lágrima, Karenin. Leia o livro como partitura, não como enredo.",
    "tip": "<strong>Como aplicar:</strong> ao reler (ou assistir ao filme), siga os motivos recorrentes — cada retorno do chapéu-coco, de Beethoven ou do espelho carrega sentido novo. O eterno retorno funciona na estrutura da obra."
   },
   {
    "ic": "spiral",
    "t": "A Não-Resolução Como Método",
    "b": "Kundera não resolve a oposição leveza/peso — encarna-a em destinos e a deixa em aberto. O romance, para ele, é o reino da <strong>pergunta e da ambiguidade</strong>, não da resposta. A cronologia é embaralhada de propósito: o 'o que acontece' importa menos que o 'o que significa'.",
    "tip": "<strong>Para refletir:</strong> o que muda na sua leitura quando você sabe desde o início que os protagonistas morrerão num acidente? Kundera queria que o foco fosse a qualidade do instante, não o suspense do desfecho."
   }
  ]
 }
}
```
