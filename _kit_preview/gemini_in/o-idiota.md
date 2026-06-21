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

# LIVRO PARA APROFUNDAR: O Idiota — Fiódor Dostoiévski

**Subtítulo:** VISÃO GERAL · A TRAGÉDIA DA BONDADE PURA NO MUNDO REAL
**Ideia central:** Um homem bom de verdade — o príncipe Míchkin, epiléptico e sem malícia — entra na sociedade de Petersburgo movida a dinheiro e vaidade. Ao tentar salvar a todos por compaixão, precipita a ruína de todos. 'A beleza salvará o mundo' fica como pergunta, não como resposta.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-chegada-michkin-sociedade` — CAPÍTULO 1 (Parte I): A Chegada de Míchkin e a Sociedade
- `ch02-noite-nastassia-o-fogo` — CAPÍTULO 2 (Parte I): A Noite de Nastássia e o Fogo
- `ch03-rogojin-faca-holbein` — CAPÍTULO 2 (Parte II): Rogójin, a Faca e o Cristo de Holbein
- `ch04-epilepsia-extase` — CAPÍTULO 4 (Parte II): A Epilepsia e o Êxtase
- `ch05-beleza-salvara-mundo-compaixao` — CAPÍTULO 5 (Parte III): 'A Beleza Salvará o Mundo'
- `ch06-aglaia-nastassia-confronto` — CAPÍTULO 6 (Parte IV): Agláia × Nastássia
- `ch07-casamento-assassinato-desfecho` — CAPÍTULO 7 (Parte IV): O Casamento, o Assassinato e o Desfecho
- `ch08-personagens-sistema` — CAPÍTULO 8: Os Personagens como Sistema
- `ch09-simbolos-estrutura-tese` — CAPÍTULO 9: Símbolos, Estrutura e a Tese da Bondade

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-chegada-michkin-sociedade": {
  "cards": [
   {
    "ic": "person",
    "t": "Candura como Espelho",
    "b": "A transparência de Míchkin <strong>revela</strong> cada personagem pela forma como reage a ela: uns encantados, outros desdenhosos, outros a exploram. A bondade funciona como espelho — o que cada um vê nela diz mais sobre quem olha do que sobre quem é visto.",
    "tip": "<strong>Para o leitor:</strong> observe sua própria reação a Míchkin — o desconforto com a bondade é dado de quem lê, não defeito do personagem."
   },
   {
    "ic": "masks",
    "t": "O Trem — Duplos desde o Início",
    "b": "No vagão, Míchkin e Rogójin se encontram pela primeira vez. O trem é o <strong>prólogo do destino</strong>: os dois são duplos desde o instante zero — compaixão e posse pelo mesmo caminho, para a mesma mulher, para o mesmo colapso.",
    "tip": "<strong>Modelo mental:</strong> em Dostoiévski o primeiro encontro já contém o desfecho — releia o início depois de terminar o livro."
   },
   {
    "ic": "key",
    "t": "O Mundo que o Recebe",
    "b": "Petersburgo opera por <strong>dinheiro, dote e amor-próprio</strong>: Nastássia é 'comprada' (primeiro por Tótski, depois por Rogójin); Gánia a aceitaria por 75 mil rublos. Míchkin é o único que não calcula — e por isso parece idiota. O mundo mede bondade como incompetência.",
    "tip": "<strong>Como aplicar:</strong> questione os ambientes que tratam generosidade como ingenuidade e cálculo como inteligência."
   }
  ]
 },
 "ch02-noite-nastassia-o-fogo": {
  "cards": [
   {
    "ic": "spark",
    "t": "O Fogo dos 100 Mil — Julgamento",
    "b": "Nastássia joga os 100 mil rublos de Rogójin no fogo e oferece o pacote a Gánia: quem tirar sem luvas fica com o dinheiro. É um <strong>tribunal improvisado</strong> — ela que foi 'comprada' agora compra e queima. A beleza ferida decreta seu próprio julgamento.",
    "tip": "<strong>Para o leitor:</strong> o fogo é símbolo de duplo sentido — julgamento da sociedade que precifica gente e, ao mesmo tempo, autodestruição."
   },
   {
    "ic": "wave",
    "t": "Beleza Ferida × Beleza Viva",
    "b": "Nastássia não é apenas vítima: é a <strong>beleza que se autodestrói</strong> porque não aceita ser salva. O orgulho autopunitivo a impede de receber o amor de Míchkin — ela não se permite o caminho de volta à dignidade. Agláia, no contraste, é a beleza que ainda pode viver.",
    "tip": "<strong>Modelo mental:</strong> o orgulho autopunitivo é uma das formas mais difíceis de sofrimento — bloqueia a saída que a pessoa mais precisa."
   },
   {
    "ic": "gap",
    "t": "Compra × Compaixão",
    "b": "Todos calculam o preço de Nastássia; Míchkin a <strong>vê como pessoa</strong>, não como objeto. Mas a piedade dele também a aprisionará — ser amada por pena é difícil de aceitar quando o orgulho está partido. Compaixão e instrumentalização têm efeitos diferentes, mas ambos podem aprisionar.",
    "tip": "<strong>Como aplicar:</strong> quem sofreu instrumentalização profunda pode resistir até ao afeto genuíno — porque aprendeu a desconfiar de toda atenção."
   }
  ]
 },
 "ch03-rogojin-faca-holbein": {
  "cards": [
   {
    "ic": "eye",
    "t": "O Cristo de Holbein — A Dúvida",
    "b": "O quadro de Holbein retrata um Cristo <strong>sem ressurreição visível</strong> — carne deteriorada, sem glória, apenas morte. É o contra-argumento à tese da beleza que salva: e se a bondade não ressuscitar? O quadro debate-se contra a tese do romance durante toda a obra.",
    "tip": "<strong>Para o leitor:</strong> o quadro de Holbein é o único personagem mudo do romance — mas fala mais que muitos."
   },
   {
    "ic": "masks",
    "t": "Rogójin e Míchkin — Os Duplos",
    "b": "Os dois homem estão ligados por irmandade e rivalidade: trocam crucifixos, fazem votos. São as <strong>duas faces do amor por Nastássia</strong> — compaixão (Míchkin) e posse (Rogójin). Quando estão juntos, a tragédia é iminente.",
    "tip": "<strong>Modelo mental:</strong> o duplo em Dostoiévski não é vilão × herói — é a mesma força (amor) em duas formas opostas e igualmente destrutivas."
   },
   {
    "ic": "sword",
    "t": "A Faca — Prenúncio",
    "b": "A faca que Rogójin usa no final aparece antecipada em cenas anteriores — Dostoiévski prepara o leitor com <strong>prenúncios</strong>. A paixão possessiva tem um destino anunciado: o amor que não aceita a perda tende ao domínio e à destruição.",
    "tip": "<strong>Como aplicar:</strong> a paixão que possui — que precisa que o outro seja seu e só seu — contém sua própria catástrofe."
   }
  ]
 },
 "ch04-epilepsia-extase": {
  "cards": [
   {
    "ic": "spark",
    "t": "O Instante Eterno",
    "b": "O êxtase pré-epiléptico é uma experiência de <strong>harmonia absoluta</strong> que Míchkin descreve como valendo uma vida inteira. É a graça inseparável da doença — a lucidez suprema e a 'idiotice' moram no mesmo corpo.",
    "tip": "<strong>Para o leitor:</strong> Dostoiévski viveu a epilepsia — o êxtase que descreve é experiência direta, não invenção literária."
   },
   {
    "ic": "gap",
    "t": "Graça e Doença — Inseparáveis",
    "b": "O <strong>preço do êxtase</strong> é a queda, a confusão posterior, a exposição pública. A visão mais clara de tudo vem acompanhada da vulnerabilidade maior. A graça de Míchkin e sua impotência são o mesmo dom.",
    "tip": "<strong>Modelo mental:</strong> os maiores dons costumam vir com vulnerabilidades correspondentes — a genialidade e a fragilidade raramente se separam."
   },
   {
    "ic": "eye",
    "t": "A Aura como Diagnóstico Moral",
    "b": "A crise epiléptica expõe Míchkin no momento mais <strong>politicamente inoportuno</strong> (o jantar, a sala da família) — a doença faz o que a bondade não consegue: <strong>força a verdade</strong> para fora, quebra a compostura social e revela quem cada um é no momento da crise.",
    "tip": "<strong>Como aplicar:</strong> observe como as pessoas reagem em momentos de crise — crise revela caráter onde a normalidade o esconde."
   }
  ]
 },
 "ch05-beleza-salvara-mundo-compaixao": {
  "cards": [
   {
    "ic": "spark",
    "t": "A Tese — E Sua Ambiguidade",
    "b": "'A beleza salvará o mundo' é ambígua por <strong>design</strong>: não é beleza física, é beleza moral (compaixão, humildade encarnada). Mas o romance encena Nastássia — beleza que destrói — ao mesmo tempo. A frase é programa e pergunta: sob que condições a beleza salva?",
    "tip": "<strong>Para o leitor:</strong> não leia a frase como slogan — o romance a testa sem confirmá-la. A ambiguidade é a tese."
   },
   {
    "ic": "wave",
    "t": "Ippolit — A Revolta Diante da Morte",
    "b": "Ippolit, jovem tuberculoso, lê sua confissão em público e provoca: e se a bondade de Míchkin não servir para nada? E se ele morrer antes de qualquer salvação? É a <strong>objeção da finitude</strong> à compaixão — o Cristo de Holbein em pessoa.",
    "tip": "<strong>Modelo mental:</strong> Ippolit é a voz de quem não tem tempo para a salvação lenta — a urgência da morte torna qualquer resposta insuficiente."
   },
   {
    "ic": "leaf",
    "t": "Compaixão que Alimenta a Autodestruição",
    "b": "A piedade de Míchkin por Nastássia, oferecida sem limites, <strong>alimenta a autodestruição dela</strong> — ela não se permite ser salva, e o amor de Míchkin sem escolha firme confirma que ela não precisa ser. Compaixão sem discernimento pode ser cumplicidade.",
    "tip": "<strong>Como aplicar:</strong> ajudar alguém a se salvar às vezes exige deixar de 'salvar' o que a pessoa já decidiu perder."
   }
  ]
 },
 "ch06-aglaia-nastassia-confronto": {
  "cards": [
   {
    "ic": "scale",
    "t": "A Escolha Impossível — Mas Necessária",
    "b": "Míchkin ama as duas: Nastássia por piedade, Agláia por amor. Recusar a escolha para não ferir ninguém é, na prática, <strong>ferir a ambas mais fundo</strong>. A tragédia não vem da maldade — vem da bondade sem firmeza que não suporta causar dor.",
    "tip": "<strong>Modelo mental:</strong> evitar a escolha não é neutralidade — é uma escolha com consequências, geralmente piores que a decisão direta."
   },
   {
    "ic": "mask",
    "t": "Agláia — Orgulho Que Pode Viver",
    "b": "Agláia é a contraparte de Nastássia: <strong>orgulhosa mas com futuro</strong>. O amor dela por Míchkin é real — e o abandono dele quando ele corre para a 'salvação' de Nastássia a destrói. O orgulho que poderia ter vida não aguenta a piedade do amado por outra.",
    "tip": "<strong>Para o leitor:</strong> a cena do confronto entre as duas mulheres é o momento em que Dostoiévski coloca em evidência que mesmo a 'boa escolha' (Agláia) foi desperdiçada."
   },
   {
    "ic": "gap",
    "t": "A Falha Trágica — Indecisão",
    "b": "A falha trágica de Míchkin não é maldade nem fraqueza de caráter: é a <strong>incapacidade de aceitar que toda escolha exige custo</strong>. Quem ama a todos por compaixão e não aceita ferir ninguém acaba, inevitavelmente, destruindo a todos.",
    "tip": "<strong>Como aplicar:</strong> compaixão que recusa a firmeza da escolha transfere o sofrimento de quem age para todos que esperam — o custo não desaparece, só muda de destinatário."
   }
  ]
 },
 "ch07-casamento-assassinato-desfecho": {
  "cards": [
   {
    "ic": "sword",
    "t": "A Faca — Posse Levada ao Fim",
    "b": "Rogójin mata Nastássia porque não consegue suportar perdê-la para outra vez. A <strong>paixão possessiva levada ao fim</strong> tem um único desfecho: destruir o que ama para que ninguém mais o tenha. O amor que não suporta a liberdade do amado não é amor — é aprisionamento.",
    "tip": "<strong>Modelo mental:</strong> o amor que exige posse total como condição é mais próximo do controle do que do afeto."
   },
   {
    "ic": "mountain",
    "t": "A Vigília ao Lado do Assassino",
    "b": "Míchkin e Rogójin velam juntos o corpo de Nastássia. Os duplos <strong>se reúnem na catástrofe</strong> que precipitaram juntos — compaixão e posse, cada um por sua parte, convergem para o mesmo desfecho. A cena é o ponto mais sombrio e mais honesto da obra.",
    "tip": "<strong>Para o leitor:</strong> a vigília conjunta dos dois homens é a imagem mais poderosa do romance — dois polos opostos unificados no fracasso."
   },
   {
    "ic": "spiral",
    "t": "A Circularidade Trágica",
    "b": "Míchkin retorna ao manicômio suíço — <strong>de onde veio, para onde volta</strong>. A bondade não progrediu no mundo: ela colapsou. A estrutura circular é a tese: o homem bom puro não encontra lugar no mundo real — é destruído pela sua própria incapacidade de firmeza.",
    "tip": "<strong>Modelo mental:</strong> estruturas circulares em literatura anunciam tragédia — o herói retorna ao ponto de partida sem ter conquistado o que prometia."
   }
  ]
 },
 "ch08-personagens-sistema": {
  "cards": [
   {
    "ic": "masks",
    "t": "O Quadrângulo Amoroso",
    "b": "<strong>Míchkin–Nastássia–Rogójin–Agláia</strong> formam o quadrângulo central: compaixão × paixão pelo mesmo objeto; beleza ferida × beleza viva como destinos possíveis; o homem que não escolhe × o homem que só sabe possuir. Cada relação define as outras por contraste.",
    "tip": "<strong>Modelo mental:</strong> em Dostoiévski as relações são sempre triângulos ou quadrângulos — o sentido de cada personagem depende da posição dos outros."
   },
   {
    "ic": "eye",
    "t": "Figuras Crísticas — E Suas Falhas",
    "b": "Míchkin é figura de Cristo na compaixão e na recusa do julgamento — mas é um Cristo que <strong>não redime</strong>. A bondade desarmada, sem a firmeza da escolha, não converte: é manipulada, idolatrada e destroçada pelo mundo que pretendia salvar.",
    "tip": "<strong>Para o leitor:</strong> Dostoiévski mostra que a imagem de Cristo lançada na história moderna encontra resistência que a narrativa evangélica não precisou enfrentar."
   },
   {
    "ic": "gap",
    "t": "Ippolit — A Voz da Revolta",
    "b": "Ippolit confronta Míchkin com a morte iminente e a pergunta: a bondade do príncipe <strong>serve para algo</strong> quando se morre aos dezoito anos? É o contraponto mais duro — a inocência que sofre sem redenção possível, o Cristo de Holbein em carne e osso.",
    "tip": "<strong>Como aplicar:</strong> a pergunta de Ippolit não tem resposta fácil — é a mesma da teodiceia de Ivan Karamázov, mas em versão pessoal e urgente."
   }
  ]
 },
 "ch09-simbolos-estrutura-tese": {
  "cards": [
   {
    "ic": "spiral",
    "t": "Os Símbolos — A Tese em Imagens",
    "b": "<strong>Cristo de Holbein</strong> (bondade sem ressurreição?), <strong>fogo</strong> (julgamento e autodestruição), <strong>faca</strong> (paixão que mata), <strong>aura epiléptica</strong> (graça inseparável da doença), <strong>sanatório suíço</strong> (circularidade trágica). Cada símbolo é argumento — não decoração.",
    "tip": "<strong>Para o leitor:</strong> em Dostoiévski, leia os objetos tanto quanto os diálogos — eles sustentam a tese quando as palavras falham."
   },
   {
    "ic": "layers",
    "t": "A Estrutura em 4 Partes",
    "b": "As quatro partes têm <strong>progressão de catástrofe</strong>: I (chegada/esperança), II (prenúncios), III (teste da tese), IV (a ruína). A circularidade fecha: Míchkin retorna ao manicômio suíço de onde partiu — o mundo não foi transformado, ele foi destruído por ele.",
    "tip": "<strong>Modelo mental:</strong> a estrutura circular trágica é sinal de que a promessa inicial (a bondade salvará) não se cumpriu — o herói paga com o retorno ao ponto zero."
   },
   {
    "ic": "bulb",
    "t": "A Tese Aberta",
    "b": "O romance não responde se 'a beleza salvará o mundo': apresenta o teste e <strong>deixa o leitor com a pergunta</strong>. Míchkin falhou — mas isso prova que a bondade não salva, ou que esta bondade, sem firmeza, foi insuficiente? Dostoiévski recusa o slogan fácil em ambas as direções.",
    "tip": "<strong>Como aplicar:</strong> a maior honestidade de Dostoiévski é não resolver o que não tem solução fácil — a pergunta aberta é respeito pelo leitor."
   }
  ]
 }
}
```
