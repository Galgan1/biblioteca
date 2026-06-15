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

# LIVRO PARA APROFUNDAR: O Alquimista — Paulo Coelho

**Subtítulo:** VISÃO GERAL · A FÁBULA DA LENDA PESSOAL
**Ideia central:** Santiago, jovem pastor andaluz, larga o rebanho para seguir um sonho repetido: um tesouro escondido nas Pirâmides do Egito. Atravessa o mar, é roubado, trabalha, ama Fátima e aprende com dois mestres — Melquisedeque e o Alquimista — a ler a Linguagem do Mundo. No fim, descobre que o tesouro estava no ponto de partida. Uma fábula sobre seguir o próprio destino: a Lenda Pessoal.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-prologo-narciso` — MOVIMENTO 1: Prólogo — Narciso e o lago
- `ch02-o-sonho-e-melquisedeque` — MOVIMENTO 2: O sonho e Melquisedeque
- `ch03-tanger-e-o-roubo` — MOVIMENTO 3: Tânger e o roubo
- `ch04-a-loja-de-cristais` — MOVIMENTO 4: A loja de cristais
- `ch05-o-ingles-e-a-alquimia` — MOVIMENTO 5: O inglês e a alquimia
- `ch06-o-oasis-e-fatima` — MOVIMENTO 6: O oásis e Fátima
- `ch07-o-alquimista` — MOVIMENTO 7: O Alquimista
- `ch08-o-deserto-e-o-vento` — MOVIMENTO 8: O deserto e o vento
- `ch09-o-tesouro` — MOVIMENTO 9: As Pirâmides e o tesouro

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-prologo-narciso": {
  "cards": [
   {
    "ic": "wave",
    "t": "O Lago que Chorava",
    "b": "No mito recontado, o lago não lamenta a morte de Narciso: chora porque perdeu o espelho onde via a <strong>própria</strong> beleza. Cada um buscava no outro a imagem de si.",
    "tip": "<strong>Como ler:</strong> trate a história como alegoria — o tesouro, o deserto e os sinais figuram verdades interiores."
   },
   {
    "ic": "eye",
    "t": "Buscar o Mundo é Buscar-se",
    "b": "O olhar funciona como espelho: a gente procura no mundo o reflexo do que carrega dentro. O prólogo antecipa a tese — a jornada externa revela o interior.",
    "tip": "<strong>Para refletir:</strong> o reflexo só aparece quando há o que refletir; a travessia é que revela quem se é."
   }
  ]
 },
 "ch02-o-sonho-e-melquisedeque": {
  "cards": [
   {
    "ic": "spark",
    "t": "A Lenda Pessoal",
    "b": "Melquisedeque revela: todos nascem com uma Lenda Pessoal — o que sempre quiseram realizar. Saber a sua é ganhar a <strong>obrigação</strong> de cumpri-la; ignorá-la passa a ser escolha, não ignorância.",
    "tip": "<strong>Como aplicar:</strong> resgate o sonho nítido da juventude, antes de o medo entrar."
   },
   {
    "ic": "constellation",
    "t": "O Universo Conspira",
    "b": "\"Quando você quer alguma coisa, todo o universo conspira para que você realize seu desejo.\" O desejo verdadeiro vem da <strong>Alma do Mundo</strong> e mobiliza o mundo a favor.",
    "tip": "<strong>Modelo mental:</strong> querer com todo o coração é a condição — não o capricho passageiro."
   },
   {
    "ic": "fork",
    "t": "Urim e Tumim",
    "b": "O rei entrega duas pedras (preta = sim, branca = não): muleta para ler sinais quando não se sabe interpretar sozinho. Ensina a recorrer a elas só na dúvida extrema.",
    "tip": "<strong>Para refletir:</strong> o sinal externo é apoio temporário; a meta é ler a Linguagem do Mundo com o próprio coração."
   }
  ]
 },
 "ch03-tanger-e-o-roubo": {
  "cards": [
   {
    "ic": "mountain",
    "t": "A Prova Após o Começo Fácil",
    "b": "Acabada a sorte de principiante, o mundo testa a decisão. O revés <strong>não anula</strong> o acerto de ter partido — é parte do caminho, não sinal de erro.",
    "tip": "<strong>Modelo mental:</strong> depois do impulso fácil do início, prepare-se para as provas."
   },
   {
    "ic": "fork",
    "t": "Reescolher a Interpretação",
    "b": "Diante dos mesmos fatos, Santiago vê duas histórias: <strong>vítima</strong> (que desiste) ou <strong>aventureiro</strong> (que recomeça). Os fatos são neutros; a leitura decide o rumo.",
    "tip": "<strong>Para refletir:</strong> 'fui roubado' e 'estou atrás de um tesouro' descrevem a mesma cena — você escolhe qual viver."
   }
  ]
 },
 "ch04-a-loja-de-cristais": {
  "cards": [
   {
    "ic": "book",
    "t": "Maktub — Está Escrito",
    "b": "O mercador ensina: <em>Maktub</em>, \"está escrito\". Há um destino traçado, mas cabe a cada um <strong>caminhá-lo</strong>. Não é fatalismo passivo — é confiança que dispensa a ansiedade, não o esforço.",
    "tip": "<strong>Modelo mental:</strong> aja com fé de que o caminho existe; o que se larga é o medo, não a ação."
   },
   {
    "ic": "masks",
    "t": "O Sonho que Nunca se Vive",
    "b": "O mercador sonha a vida toda em ir a Meca — e nunca vai, com medo de ficar sem motivo para viver depois. Há quem prefira o sonho à realização: uma forma sutil de <strong>abandonar a Lenda</strong>.",
    "tip": "<strong>Para refletir:</strong> adiar o sonho 'para quando der' indefinidamente = você virou o mercador."
   },
   {
    "ic": "target",
    "t": "O Conforto como Tentação",
    "b": "Prosperando, Santiago junta o suficiente para voltar ao rebanho. O dinheiro e o conforto são a tentação de <strong>trocar a Lenda pela segurança</strong> e desistir no meio.",
    "tip": "<strong>Modelo mental:</strong> 'já tenho o bastante para voltar' é o canto da sereia que encerra a jornada cedo demais."
   }
  ]
 },
 "ch05-o-ingles-e-a-alquimia": {
  "cards": [
   {
    "ic": "leaf",
    "t": "Alquimia como Alegoria",
    "b": "Transformar chumbo em ouro = <strong>purificar a si mesmo</strong> até realizar a própria Lenda. A Pedra Filosofal e o Elixir da Vida são símbolos: a transmutação exterior espelha a interior.",
    "tip": "<strong>Modelo mental:</strong> a verdadeira Obra-Prima é a pessoa que se torna quem veio ser."
   },
   {
    "ic": "layers",
    "t": "A Alma do Mundo",
    "b": "Tudo na Terra é uma só matéria, escrita pela mesma Mão. Existe uma <strong>Linguagem do Mundo</strong> — universal, sem palavras — por trás de todas as coisas. Quem ama e busca seu destino se conecta a ela.",
    "tip": "<strong>Para refletir:</strong> entender que tudo é uma só coisa é o começo de falar a Linguagem do Mundo."
   },
   {
    "ic": "lens",
    "t": "Livros × Experiência",
    "b": "O inglês carrega anos de leitura mas ainda não viveu a verdade; Santiago aprende olhando o deserto e os homens. Os dois caminhos são <strong>complementares</strong> — viver o que se sabe é o que falta ao erudito.",
    "tip": "<strong>Modelo mental:</strong> acumular conhecimento sem aplicar = a mala de livros do inglês."
   }
  ]
 },
 "ch06-o-oasis-e-fatima": {
  "cards": [
   {
    "ic": "link",
    "t": "O Amor que Não Aprisiona",
    "b": "Fátima, a mulher do deserto, ama Santiago e por isso o <strong>deixa partir</strong>: \"se eu faço parte do seu sonho, você há de voltar um dia\". O amor verdadeiro é parte da Lenda, não desculpa para desistir dela.",
    "tip": "<strong>Para refletir:</strong> usar o amor como motivo para abandonar o sonho corrói o próprio amor."
   },
   {
    "ic": "eye",
    "t": "Ler os Agouros",
    "b": "Vendo dois gaviões rasgarem o céu, Santiago intui um exército invadindo o oásis — e avisa os chefes, arriscando a vida. A <strong>Linguagem do Mundo</strong> se lê nos sinais e se traduz em ação.",
    "tip": "<strong>Modelo mental:</strong> o sinal pede decisão e risco — não é horóscopo passivo."
   },
   {
    "ic": "target",
    "t": "O Refúgio como Tentação",
    "b": "Ficar para sempre no oásis, com Fátima, encerraria a jornada a meio caminho. Os refúgios são <strong>tentações de parar no meio</strong> — o conforto pode adiar a Lenda para sempre.",
    "tip": "<strong>Para refletir:</strong> a paz fácil do oásis é doce — e por isso perigosa para quem ainda tem caminho."
   }
  ]
 },
 "ch07-o-alquimista": {
  "cards": [
   {
    "ic": "spiral",
    "t": "Escutar o Coração",
    "b": "O coração teme sofrer e às vezes trai — mas é por ele que se fala com a Alma do Mundo. <strong>Ouça-o</strong>, inclusive os medos: ouvido, ele para de pregar peças e vira aliado.",
    "tip": "<strong>Modelo mental:</strong> não cale o coração; escute o medo sem obedecer a ele."
   },
   {
    "ic": "scale",
    "t": "O Medo de Sofrer",
    "b": "O maior obstáculo à Lenda não são os perigos — é o <strong>medo de sofrer</strong>. \"Nenhum coração jamais sofreu quando foi atrás de seus sonhos\", pois cada momento da busca é um encontro com o sagrado.",
    "tip": "<strong>Para refletir:</strong> o medo de sofrer dói mais do que o sofrimento real."
   },
   {
    "ic": "clock",
    "t": "Viver o Presente",
    "b": "A vida é vivida no agora; quem vive o presente é feliz e vê o deserto como vida, não ameaça. A felicidade está na <strong>travessia</strong>, não só na chegada.",
    "tip": "<strong>Modelo mental:</strong> quem só pensa no tesouro perde a vida que é o caminho."
   }
  ]
 },
 "ch08-o-deserto-e-o-vento": {
  "cards": [
   {
    "ic": "wave",
    "t": "Conversar com os Elementos",
    "b": "Sem saber como virar vento, Santiago dialoga com o deserto, o vento e o sol — cada um o remetendo adiante até a <strong>Mão que escreveu tudo</strong>. Mergulhando nessa unidade, ele move o simum e levanta a tempestade.",
    "tip": "<strong>Modelo mental:</strong> tudo é a mesma matéria; entender essa unidade é falar a Linguagem do Mundo."
   },
   {
    "ic": "spark",
    "t": "O Amor que Transforma",
    "b": "Cada elemento confessa não saber sozinho o que é transformar — só o <strong>amor</strong> (a Alma do Mundo) transmuta. Foi o amor que converteu o chumbo em ouro nos alquimistas; é ele o motor da verdadeira alquimia.",
    "tip": "<strong>Para refletir:</strong> a força que muda o mundo não é técnica, é amor."
   },
   {
    "ic": "mountain",
    "t": "A Prova Suprema",
    "b": "A Lenda Pessoal cobra uma <strong>provação final</strong>, em que se prova tudo o que se aprendeu. Vencida pela fé em ação (Maktub), abre-se o que parecia impossível — e o caminho às Pirâmides fica livre.",
    "tip": "<strong>Modelo mental:</strong> a maior prova vem perto do fim — é nela que a jornada inteira se confirma."
   }
  ]
 },
 "ch09-o-tesouro": {
  "cards": [
   {
    "ic": "key",
    "t": "O Tesouro no Começo",
    "b": "O ouro estava sob o mesmo sicômoro onde Santiago sonhou pela primeira vez. Mas só se torna <strong>visível depois</strong> de toda a travessia — é o caminho que dá olhos para ver o que já estava perto.",
    "tip": "<strong>Modelo mental:</strong> o que se busca longe costuma estar perto; só a jornada nos faz enxergá-lo."
   },
   {
    "ic": "steps",
    "t": "O Caminho é a Recompensa",
    "b": "A jornada transformou Santiago; sem ela, ele jamais teria olhos para ver (ou direito de receber) o tesouro. O <strong>bandido</strong> também sonhou — mas não foi, e por isso nada terá.",
    "tip": "<strong>Para refletir:</strong> sonhar não basta; quem não vai atrás da Lenda fica sem nada."
   },
   {
    "ic": "link",
    "t": "O Amor que Espera",
    "b": "Fátima, parte da Lenda, permanece à espera. No vento, Santiago sente o beijo dela e sabe que pode ir buscá-la: o tesouro <strong>material e o afetivo</strong> se reconciliam no fim.",
    "tip": "<strong>Modelo mental:</strong> a Lenda realizada reúne tudo — propósito, transformação e amor."
   }
  ]
 }
}
```
