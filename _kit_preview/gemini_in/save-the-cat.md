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

# LIVRO PARA APROFUNDAR: Save the Cat! — Blake Snyder

**Subtítulo:** VISÃO GERAL · O MÉTODO DE ESTRUTURA DE HISTÓRIAS
**Ideia central:** Blake Snyder destilou décadas de roteiro de Hollywood num sistema prático e brutalmente claro: venda a ideia numa frase (logline), descubra o tipo de transformação que você está contando (os 10 gêneros), bata as 15 batidas da estrutura (a beat sheet), arme a história inteira no Quadro antes de escrever e diagnostique o que trava pelo nome do defeito. Não é fórmula — é a gramática que o público já tem no ouvido.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-logline` — CAPÍTULO 1: O Que É Isso? — A Logline
- `ch02-generos` — CAPÍTULO 2: O Mesmo, Só Que Diferente — Os 10 Gêneros
- `ch03-heroi` — CAPÍTULO 3: É Sobre Um Cara Que… — O Herói
- `ch04-beat-sheet` — CAPÍTULO 4: Vamos Marcar as Batidas — A Beat Sheet
- `ch05-o-quadro` — CAPÍTULO 5: Construindo a Fera Perfeita — O Quadro
- `ch06-leis-fisica-roteiro` — CAPÍTULO 6: As Leis Imutáveis da Física do Roteiro
- `ch07-diagnostico` — CAPÍTULO 7: O Que Há de Errado? — Diagnóstico
- `ch08-fade-in-final` — CAPÍTULO 8: Fade In Final — Vender e Persistir

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-logline": {
  "cards": [
   {
    "ic": "target",
    "t": "Os 4 Ingredientes",
    "b": "<strong>Ironia</strong> (tensão na premissa), <strong>imagem mental</strong> completa do filme, <strong>público e custo</strong> implícitos e <strong>título</strong> que diz o que é. A ironia é o gancho.",
    "tip": "<strong>Como aplicar:</strong> sem tensão interna, é sinopse, não logline."
   },
   {
    "ic": "eye",
    "t": "O Teste do Estranho",
    "b": "Conte a logline para quem não te deve gentileza. Se os olhos não acendem, <strong>volte para a prancheta</strong> — antes de gastar meses de roteiro.",
    "tip": "<strong>Modelo mental:</strong> venda o ingresso antes de construir o cinema."
   },
   {
    "ic": "gap",
    "t": "Onde Falha",
    "b": "\"Quando eu terminar você entende\" — se precisa do roteiro para explicar, a <strong>premissa falhou</strong>. Empilhar enredo não substitui uma tensão única e clara.",
    "tip": "<strong>Cuidado:</strong> apaixonar-se cedo demais pula o teste que evita o desastre."
   }
  ]
 },
 "ch02-generos": {
  "cards": [
   {
    "ic": "book",
    "t": "Transformação, Não Cenário",
    "b": "Um filme no espaço pode ser terror (Monstro na Casa), sobrevivência (Cara com um Problema) ou Institucionalizado. O que define o gênero é <strong>o tipo de mudança contada</strong>.",
    "tip": "<strong>Como aplicar:</strong> ache a família da sua história e estude os irmãos dela."
   },
   {
    "ic": "layers",
    "t": "As 10 Famílias",
    "b": "Monstro na Casa, Velocino de Ouro, Lâmpada Mágica, Cara com um Problema, Ritos de Passagem, Amor de Camaradas, Por Que Foi Feito?, Triunfo do Tolo, Institucionalizado, Super-Herói.",
    "tip": "<strong>Modelo mental:</strong> cada família tem regras que o público conhece de cor."
   },
   {
    "ic": "key",
    "t": "\"O Mesmo, Só Que Diferente\"",
    "b": "Honre a expectativa do gênero; <strong>surpreenda na execução</strong>. O esqueleto é emprestado; a torção é o seu trabalho.",
    "tip": "<strong>Cuidado:</strong> \"meu filme não se parece com nada\" costuma significar \"não estudei com o que ele se parece\"."
   }
  ]
 },
 "ch03-heroi": {
  "cards": [
   {
    "ic": "target",
    "t": "Herói a Serviço da Ideia",
    "b": "Escolha o protagonista que <strong>maximiza o conflito</strong>, tem o <strong>arco mais longo</strong> (parte do ponto mais distante da lição) e é <strong>abraçável</strong> (o público se vê nele).",
    "tip": "<strong>Como aplicar:</strong> se outro personagem serve melhor à premissa, troque — dói menos que um filme morno."
   },
   {
    "ic": "spiral",
    "t": "É Primal?",
    "b": "Toda motivação que funciona é primal — sobreviver, proteger os seus, fome, amor, medo da morte. Se um <strong>homem das cavernas</strong> não entenderia o que está em jogo, as estacas são fracas.",
    "tip": "<strong>Modelo mental:</strong> traduza o abstrato (carreira) no primal (família)."
   },
   {
    "ic": "eye",
    "t": "Herói Passivo",
    "b": "As coisas acontecem <strong>a</strong> ele, não <strong>por causa</strong> dele. Quem conduz é protagonista; quem assiste é figurante caro.",
    "tip": "<strong>Cuidado:</strong> herói passivo é o primeiro defeito que a reescrita procura."
   }
  ]
 },
 "ch04-beat-sheet": {
  "cards": [
   {
    "ic": "clock",
    "t": "As 15 Batidas",
    "b": "Imagem de Abertura, Tema Declarado, Apresentação, <strong>Catalisador</strong>, Debate, Virada p/ Ato 2, História B, <strong>Diversão e Jogos</strong>, <strong>Ponto Médio</strong>, Vilões Fecham o Cerco, <strong>Tudo Está Perdido</strong>, Noite Escura da Alma, Virada p/ Ato 3, Final, Imagem Final.",
    "tip": "<strong>Chave:</strong> estrutura é forma, não fórmula — o soneto tem 14 versos e ninguém chama Camões de preguiçoso."
   },
   {
    "ic": "spiral",
    "t": "Promessa da Premissa",
    "b": "<strong>Diversão e Jogos</strong> é onde a logline é paga — as cenas pelas quais o público comprou o ingresso. O <strong>Ponto Médio</strong> é falsa vitória/derrota; <strong>Tudo Está Perdido</strong> traz o \"cheiro de morte\".",
    "tip": "<strong>Como aplicar:</strong> se o miolo não paga a premissa, o filme vira outro filme."
   },
   {
    "ic": "scale",
    "t": "As Duas Regras",
    "b": "<strong>Espelho:</strong> Imagem de Abertura e Final são o antes/depois — se iguais, não houve filme. <strong>Decisão:</strong> as viradas de ato são escolhas do herói, não empurrões.",
    "tip": "<strong>Cuidado:</strong> Ato 3 resolvido por terceiros não fecha o arco (deus ex machina)."
   }
  ]
 },
 "ch05-o-quadro": {
  "cards": [
   {
    "ic": "layers",
    "t": "4 Fileiras, ~40 Cartões",
    "b": "Ato 1 · Ato 2-A (até o Ponto Médio) · Ato 2-B · Ato 3 — ~10 cartões por fileira. Dividir o Ato 2 pelo Ponto Médio <strong>mata o miolo infinito</strong>.",
    "tip": "<strong>Como aplicar:</strong> fileira que incha denuncia história desequilibrada antes do rascunho."
   },
   {
    "ic": "target",
    "t": "Anatomia do Cartão",
    "b": "Cada cena registra o <strong>conflito</strong> (>< quem quer o quê contra quem) e a <strong>carga emocional</strong> (+/− — entra num estado, sai noutro).",
    "tip": "<strong>Modelo mental:</strong> cena sem conflito ou sem mudança de carga é informação fantasiada."
   },
   {
    "ic": "wrench",
    "t": "Erre no Papelão",
    "b": "Escrever é a etapa cara; planejar é a barata. Todo problema resolvido no Quadro custa <strong>1%</strong> do que custaria na página.",
    "tip": "<strong>Cuidado:</strong> pular para o rascunho \"porque a inspiração veio\" mata o filme na página 60."
   }
  ]
 },
 "ch06-leis-fisica-roteiro": {
  "cards": [
   {
    "ic": "key",
    "t": "Save the Cat",
    "b": "Cedo, o herói faz algo <strong>genuinamente simpático</strong> — ajuda alguém, mostra coragem ou humor sob pressão. É o gesto que dá ao público uma razão para torcer, sobretudo se o herói tem falhas.",
    "tip": "<strong>Como aplicar:</strong> simpatia ≠ bondade; basta um humano por quem valha torcer."
   },
   {
    "ic": "wave",
    "t": "Pope in the Pool",
    "b": "Quando a exposição é inevitável, <strong>esconda-a sob algo divertido</strong> de assistir. O público engole o necessário sem sentir o gosto.",
    "tip": "<strong>Modelo mental:</strong> exposição é dívida; pague-a sem cobrar tédio."
   },
   {
    "ic": "spiral",
    "t": "Double Mumbo Jumbo",
    "b": "O público aceita <strong>uma</strong> licença de magia por história, não duas. Um homem vira lobo, tudo bem; vira lobo <strong>e</strong> recebe alienígenas — perdeu a plateia. (E todos mudam, menos o vilão.)",
    "tip": "<strong>Cuidado:</strong> somar sistemas fantásticos não é riqueza, é furo de credibilidade."
   }
  ]
 },
 "ch07-diagnostico": {
  "cards": [
   {
    "ic": "target",
    "t": "O Checklist",
    "b": "Herói conduz (não passivo)? Dramatiza em vez de <strong>falar o enredo</strong>? <strong>Vilão forte</strong> e escalando? Estacas primais? Todos têm arco (menos o vilão)? Dá pra dizer o tema numa frase?",
    "tip": "<strong>Como aplicar:</strong> trate a causa estrutural, não o sintoma de diálogo."
   },
   {
    "ic": "sword",
    "t": "Herói Tão Grande Quanto o Vilão",
    "b": "O herói só é tão grande quanto o obstáculo. Para crescê-lo, <strong>engrandeça o adversário</strong> — \"make the bad guy badder\", escalando a cada ato.",
    "tip": "<strong>Modelo mental:</strong> vilão fraco = filme sem tensão."
   },
   {
    "ic": "eye",
    "t": "Sintoma vs. Causa",
    "b": "\"O segundo ato arrasta\" é sintoma; a causa pode ser herói passivo, vilão fraco ou Diversão e Jogos fora da premissa.",
    "tip": "<strong>Cuidado:</strong> polir frases de uma cena que não deveria existir é maquiar osso quebrado."
   }
  ]
 },
 "ch08-fade-in-final": {
  "cards": [
   {
    "ic": "target",
    "t": "Título + Pôster + Pitch",
    "b": "Se você imagina o <strong>pôster</strong> e o <strong>título diz o que é</strong>, a premissa é clara. No pitch: comece pelo gênero, entregue a logline com ironia, ancore com comparáveis (<strong>\"é X encontra Y\"</strong>) e pare.",
    "tip": "<strong>Como aplicar:</strong> se não cabe no pôster, não cabe na cabeça do público."
   },
   {
    "ic": "steps",
    "t": "Disciplina de Carreira",
    "b": "Escrever sempre, ter <strong>várias loglines no bolso</strong>, ouvir notas sem ego e tratar rejeição como dado, não veredito.",
    "tip": "<strong>Modelo mental:</strong> a diferença entre quem publica e quem não publica raramente é talento — é persistência informada."
   },
   {
    "ic": "eye",
    "t": "Pitch-Enredo",
    "b": "Contar o filme cena a cena em vez de <strong>vender a tensão central</strong> perde o ouvinte no segundo ato.",
    "tip": "<strong>Cuidado:</strong> defender em vez de ouvir notas mata a reescrita e a relação."
   }
  ]
 }
}
```
