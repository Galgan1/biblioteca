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

# LIVRO PARA APROFUNDAR: O Gene Egoísta — Richard Dawkins

**Subtítulo:** VISÃO GERAL · A EVOLUÇÃO VISTA DO PONTO DE VISTA DO GENE
**Ideia central:** A unidade fundamental da seleção natural não é a espécie, o grupo nem o indivíduo: é o gene. Os organismos são 'máquinas de sobrevivência' — veículos descartáveis construídos pelos genes para propagar suas cópias. O 'egoísmo' é uma metáfora técnica (maximizar cópias, não intenção), e dele emergem tanto o conflito quanto o altruísmo: parentes ajudam parentes porque compartilham genes, e a cooperação floresce onde os encontros se repetem. Dawkins fecha cunhando o meme, o segundo replicador — a unidade da evolução cultural.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-o-gene-como-unidade` — CAPÍTULO 1: O Gene Como Unidade da Seleção
- `ch02-parentesco-e-altruismo` — CAPÍTULO 2: Parentesco, Altruísmo e a Regra de Hamilton
- `ch03-estrategias-estaveis` — CAPÍTULO 3: Estratégias Estáveis e Cooperação
- `ch04-memes-e-alcance` — CAPÍTULO 4: Memes e o Longo Alcance do Gene

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-o-gene-como-unidade": {
  "cards": [
   {
    "ic": "spiral",
    "t": "Replicador × Veículo",
    "b": "O <strong>replicador</strong> (o gene) é a informação copiada que persiste por gerações; o <strong>veículo</strong> (o organismo) é a máquina mortal que o abriga e propaga. O corpo morre; o gene é potencialmente <em>imortal</em>.",
    "tip": "<strong>Como aplicar:</strong> ao explicar uma adaptação, separe o que é replicador (persiste e é copiado) do que é veículo (efêmero)."
   },
   {
    "ic": "layers",
    "t": "Máquina de Sobrevivência",
    "b": "Todo organismo é um robô construído pelos genes para abrigá-los. 'Eles nos criaram, corpo e mente.' Os genes não controlam em tempo real — <strong>programam</strong> estratégias que o cérebro executa sozinho.",
    "tip": "<strong>Modelo mental:</strong> gene = programador; animal = programa rodando, autônomo na execução mas com objetivos herdados."
   },
   {
    "ic": "leaf",
    "t": "Os Três Trunfos do Replicador",
    "b": "O replicador bem-sucedido maximiza <strong>longevidade</strong> (durar), <strong>fecundidade</strong> (copiar muito) e <strong>fidelidade</strong> (copiar com precisão). A vida começou com uma molécula que, por acaso, fazia cópias de si no caldo primordial.",
    "tip": "<strong>Para refletir:</strong> evolução é, no fundo, 'sobrevivência dos estáveis' — quem persiste, prevalece."
   },
   {
    "ic": "scale",
    "t": "A Falácia do 'Bem da Espécie'",
    "b": "Animais não agem 'para preservar a espécie' — a <strong>seleção de grupo</strong> é instável: um mutante egoísta invade e domina o grupo altruísta. A seleção atua muito abaixo: no gene.",
    "tip": "<strong>Regra:</strong> ao ouvir 'isso evoluiu para o bem da espécie', desconfie e reformule no nível do gene."
   }
  ]
 },
 "ch02-parentesco-e-altruismo": {
  "cards": [
   {
    "ic": "link",
    "t": "Seleção de Parentesco",
    "b": "Genes de altruísmo dirigido a <strong>parentes</strong> se espalham porque os parentes tendem a carregar os mesmos genes. O laço de sangue não importa por si — importa o <strong>gene compartilhado</strong> que ele sinaliza.",
    "tip": "<strong>Modelo mental:</strong> trate parentes como bancos parciais dos seus genes — ajudar um irmão é 'investir meio você mesmo'."
   },
   {
    "ic": "target",
    "t": "A Regra de Hamilton (rB > C)",
    "b": "Um gesto altruísta evolui quando <strong>r × B > C</strong>: <em>r</em> = grau de parentesco, <em>B</em> = benefício ao receptor, <em>C</em> = custo ao doador. Haldane: 'eu morreria por dois irmãos ou oito primos'.",
    "tip": "<strong>Como aplicar:</strong> estime r, B e C — se o produto rB excede C, o altruísmo tende a se fixar."
   },
   {
    "ic": "fork",
    "t": "O Grau de Parentesco (r)",
    "b": "r é a probabilidade de o parente carregar o mesmo gene: <strong>½</strong> para irmãos e pais–filhos, <strong>¼</strong> para tios e avós, <strong>⅛</strong> para primos, <strong>1</strong> para gêmeos idênticos. O cuidado se gradua pela proximidade.",
    "tip": "<strong>Para refletir:</strong> r é uma probabilidade genética, não um sentimento — por isso o altruísmo é desigual entre parentes e estranhos."
   },
   {
    "ic": "person",
    "t": "O Conflito Dentro do Laço",
    "b": "Como o parentesco é parcial (r<1), os interesses divergem mesmo entre quem se ama: <strong>pais × filhos</strong> (cada filho quer mais que a parte justa), <strong>machos × fêmeas</strong> (quem investe mais é mais 'explorável'). O laço é cooperação <em>e</em> conflito.",
    "tip": "<strong>Modelo mental:</strong> o choro do filhote pode ser sinal honesto OU manipulação para extrair mais investimento."
   }
  ]
 },
 "ch03-estrategias-estaveis": {
  "cards": [
   {
    "ic": "scale",
    "t": "Estratégia Evolutivamente Estável (EEE)",
    "b": "Uma estratégia que, adotada pela maioria, <strong>não pode ser invadida</strong> por nenhuma alternativa rara. É um <strong>equilíbrio</strong>, não um ótimo coletivo — pode ser ruim para todos e ainda assim estável.",
    "tip": "<strong>Teste:</strong> imagine a população toda numa estratégia + um mutante raro; se resiste à invasão, é EEE."
   },
   {
    "ic": "sword",
    "t": "Falcão × Pomba",
    "b": "'Falcão' sempre luta; 'Pomba' exibe e recua. Nenhum é EEE puro — a população estabiliza numa <strong>mistura</strong> dos dois. Mostra por que o mundo animal não é nem todo agressivo nem todo pacífico.",
    "tip": "<strong>Modelo mental:</strong> pense em comportamento social como jogo — o que compensa depende do que os outros fazem."
   },
   {
    "ic": "wave",
    "t": "Altruísmo Recíproco",
    "b": "Cooperação entre <strong>não-parentes</strong> evolui quando os encontros se repetem e há memória: 'você coça minhas costas, eu coço as suas'. Exige reencontro, reconhecimento e detecção de trapaceiro.",
    "tip": "<strong>Regra:</strong> sem repetição nem memória, a traição é estável — não conte com cooperação espontânea."
   },
   {
    "ic": "steps",
    "t": "Olho por Olho: Os Bonzinhos em 1º",
    "b": "No torneio de Axelrod (dilema do prisioneiro iterado), vence <strong>Olho por Olho</strong>: gentil (não trai primeiro), retaliador (pune na hora), perdoador (volta a cooperar) e claro. Em relações repetidas, a gentileza condicional é a estratégia robusta.",
    "tip": "<strong>Como aplicar:</strong> maximize o ganho mútuo, não a diferença para o rival — a inveja piora seu resultado."
   }
  ]
 },
 "ch04-memes-e-alcance": {
  "cards": [
   {
    "ic": "constellation",
    "t": "O Meme",
    "b": "<strong>Termo cunhado neste livro:</strong> a unidade de transmissão cultural (ideia, melodia, moda, crença) que se replica de cérebro a cérebro por imitação, sujeita à sua própria seleção. Memes competem por <strong>atenção e memória</strong>.",
    "tip": "<strong>Modelo mental:</strong> pense em ideias como organismos competindo por mentes — vence quem se copia melhor, não quem é verdadeiro."
   },
   {
    "ic": "eye",
    "t": "Complexo de Memes (Memeplex)",
    "b": "Memes que se reforçam e se propagam <strong>em conjunto</strong> — como doutrinas e ideologias. Um memeplex pode ser <strong>parasitário</strong>, espalhando-se mesmo contra o interesse de quem o carrega.",
    "tip": "<strong>Para refletir:</strong> 'bom para o meme' ≠ 'bom para você', assim como 'bom para o gene' ≠ 'bom para o indivíduo'."
   },
   {
    "ic": "key",
    "t": "O Fenótipo Estendido",
    "b": "Os efeitos de um gene <strong>não param na pele</strong>: a represa do castor, o ninho do pássaro, a teia da aranha e até a <strong>manipulação do hospedeiro</strong> por um parasita são fenótipos do gene, agindo no mundo exterior. O gene alcança longe.",
    "tip": "<strong>Modelo mental:</strong> apague a 'pele' como limite causal — o alcance do gene vai até onde chegam seus efeitos."
   },
   {
    "ic": "spark",
    "t": "A Rebelião Contra os Genes",
    "b": "Somos a única espécie capaz de <strong>prever</strong> e <strong>resistir</strong> à lógica dos genes (e dos memes) egoístas. Podemos cultivar altruísmo genuíno e cooperação deliberada. 'Temos o poder de nos voltar contra nossos criadores.'",
    "tip": "<strong>Lembrete do autor:</strong> descrever como a seleção opera NÃO é endossá-la como ética — cuidado com a falácia naturalista."
   }
  ]
 }
}
```
