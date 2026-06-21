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

# LIVRO PARA APROFUNDAR: Meditações — Marco Aurélio

**Subtítulo:** VISÃO GERAL · O CADERNO ESTOICO DO IMPERADOR-FILÓSOFO
**Ideia central:** Escritas para ninguém ler, as anotações de Marco Aurélio são o manual de campo do estoicismo: como manter a mente reta no comando do maior império do mundo. Tudo gira em torno de uma só pergunta — o que depende de mim? — e de três disciplinas (juízo, desejo e ação) que transformam a teoria em hábito diário.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-debitos-e-licoes` — TEMA 1: Débitos e Lições — a Gratidão como Exercício
- `ch02-dicotomia-do-controle` — TEMA 2: A Dicotomia do Controle — o que Depende de Nós
- `ch03-disciplina-do-assentimento` — TEMA 3: A Disciplina do Assentimento — não é a Coisa, é o Juízo
- `ch04-disciplina-do-desejo-amor-fati` — TEMA 4: A Disciplina do Desejo — Viver Segundo a Natureza e Amar o Destino
- `ch05-disciplina-da-acao-obstaculo` — TEMA 5: A Disciplina da Ação — o Bem Comum e o Obstáculo que Vira Caminho
- `ch06-memento-mori-impermanencia` — TEMA 6: Memento Mori — a Impermanência e a Brevidade da Vida
- `ch07-visao-do-alto-e-pessoas-dificeis` — TEMA 7: A Visão do Alto e o Convívio com Pessoas Difíceis
- `ch08-cosmopolitismo-dever-serenidade` — TEMA 8: Cosmopolitismo, Dever e Serenidade Interior

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-debitos-e-licoes": {
  "cards": [
   {
    "ic": "book",
    "t": "Inventário de Débitos",
    "b": "Nomear quem te formou e a <strong>virtude concreta</strong> que cada um te legou — não elogio vago, mas 'de fulano, aprendi X'. Ancora a identidade no que se recebeu, não no que se conquistou sozinho.",
    "tip": "<strong>Como aplicar:</strong> liste pessoas reais; para cada uma, a qualidade específica que ela te ensinou pelo exemplo."
   },
   {
    "ic": "person",
    "t": "Aprender por Exemplo",
    "b": "Aprende-se virtude <strong>vendo-a praticada</strong>, não só lendo sobre ela. Marco descreve Antonino Pio — brando, constante, trabalhador, indiferente à bajulação — como o sábio estoico encarnado num homem real.",
    "tip": "<strong>Modelo mental:</strong> quer mudar? Descreva em detalhe alguém que já vive a virtude que você busca."
   },
   {
    "ic": "leaf",
    "t": "A Humildade da Dívida",
    "b": "Somos feitos pelos outros: o 'eu' é tecido de heranças. Tomar as próprias virtudes como mérito próprio <strong>ignora quem as semeou</strong>. A gratidão nomeada — não a genérica — é que educa o caráter.",
    "tip": "<strong>Para refletir:</strong> 'sou grato por tudo' não forma ninguém; só a dívida específica ensina."
   }
  ]
 },
 "ch02-dicotomia-do-controle": {
  "cards": [
   {
    "ic": "scale",
    "t": "Depende de Mim × Não Depende",
    "b": "Tudo se divide em duas pilhas. Só a primeira — <strong>juízos e escolhas</strong> — é matéria de virtude e ansiedade legítima. A cada perturbação, classifique antes de reagir: 'isto está sob meu poder de escolha agora?'",
    "tip": "<strong>Como aplicar:</strong> se não está, retire dele toda exigência e expectativa. O resto é emprestado e revogável."
   },
   {
    "ic": "key",
    "t": "A Cidadela Interior",
    "b": "O centro de comando da mente (<em>hēgemonikon</em>) é <strong>inexpugnável</strong> se você não o entregar. Nada externo toca a parte que escolhe — só você pode corrompê-la. O insulto bate na muralha, não em você.",
    "tip": "<strong>Modelo mental:</strong> sob ataque, recolha-se ao refúgio interior; nenhum lugar é mais sereno que a própria alma."
   },
   {
    "ic": "gap",
    "t": "Os Indiferentes",
    "b": "Saúde, riqueza, fama, morte são <strong>indiferentes</strong> (adiaphora): nem bem nem mal em si — úteis, mas não o bem. Ancorar a felicidade neles é construir sobre areia e entregar a paz ao acaso.",
    "tip": "<strong>Para refletir:</strong> use os indiferentes com mão leve; não faça deles o sumo bem."
   }
  ]
 },
 "ch03-disciplina-do-assentimento": {
  "cards": [
   {
    "ic": "lens",
    "t": "Tira o Juízo, Tira o Dano",
    "b": "Entre a impressão e a reação, insira um <strong>filtro de juízo</strong>. Descreva o evento nu, sem adjetivos de valor ('perdi o cargo', não 'é uma catástrofe'). Tira a opinião e tira o 'fui prejudicado'; tira a queixa e tira o prejuízo.",
    "tip": "<strong>Como aplicar:</strong> sempre que algo 'te tira do sério', refaça a frase sem o veredito de valor."
   },
   {
    "ic": "eye",
    "t": "A Definição Física",
    "b": "Desmonte o objeto na sua <strong>matéria crua</strong> para dissolver o fascínio ou o pavor: o vinho é suco de uva fermentado; a púrpura, lã tinta. A auréola cai e o desejo inflado (ou o medo) encolhe.",
    "tip": "<strong>Modelo mental:</strong> um 'raio-X' que mostra a coisa sem a maquiagem do desejo — não é desprezo, é ver sem ilusão."
   },
   {
    "ic": "bulb",
    "t": "O Assentimento é Livre",
    "b": "A impressão (<em>phantasia</em>) se apresenta, mas o <strong>'sim' é seu</strong>. Assentir por reflexo a 'isto é insuportável' é entregar a mente ao automatismo. Você pode recusar a impressão antes de ela virar paixão.",
    "tip": "<strong>Para refletir:</strong> o evento não é o veredito; o juízo é provisório até você examiná-lo."
   }
  ]
 },
 "ch04-disciplina-do-desejo-amor-fati": {
  "cards": [
   {
    "ic": "leaf",
    "t": "Viver Segundo a Natureza",
    "b": "O homem é parte de um <strong>Todo racional</strong>; agir conforme sua natureza (a razão) e a do universo é a única definição de bem. Antes de cada ação: 'isto está de acordo com a razão e com minha natureza de ser social e racional?'",
    "tip": "<strong>Modelo mental:</strong> você é folha de uma árvore-cosmos; o que cai sobre você é seiva da mesma raiz."
   },
   {
    "ic": "spiral",
    "t": "Amor Fati",
    "b": "Aceitar com <strong>alegria, não só resignação</strong>, tudo o que o cosmos entrega — porque cada parte serve ao todo. Troque 'por que comigo?' por 'isto foi tecido para mim; recebo-o'. O que acontece é como o remédio que o médico prescreve.",
    "tip": "<strong>Para refletir:</strong> querer que o real seja diferente é guerrear contra a natureza — derrota garantida."
   },
   {
    "ic": "constellation",
    "t": "Providência ou Átomos",
    "b": "Ou o mundo é <strong>cosmos providente</strong>, ou caos de átomos. Em qualquer hipótese, a postura sábia é a mesma: aceitar o que vem e agir com virtude. A dúvida metafísica não muda o dever ético.",
    "tip": "<strong>Modelo mental:</strong> 'aceita sem soberba, larga sem apego' — o desejo afinado pede o que vem e solta o que vai."
   }
  ]
 },
 "ch05-disciplina-da-acao-obstaculo": {
  "cards": [
   {
    "ic": "link",
    "t": "Membros de um Corpo",
    "b": "Toda ação deve servir à <strong>comunidade racional</strong>: o homem é animal social, parte de um corpo coletivo. O que fere a colmeia fere a abelha; o egoísmo é uma amputação. Aja 'como mão, pé ou pálpebra' — peças que cumprem sua função.",
    "tip": "<strong>Como aplicar:</strong> ao decidir, pergunte 'isto serve ao todo do qual sou membro?'"
   },
   {
    "ic": "mountain",
    "t": "O Obstáculo Vira Ação",
    "b": "O que impede uma via <strong>abre outra</strong>. Como o fogo converte a lenha em chama, a mente reta consome o impedimento e cresce. 'O que impede o trabalho torna-se o trabalho; o que barra o caminho torna-se o caminho.'",
    "tip": "<strong>Modelo mental:</strong> diante de cada bloqueio, pergunte: que virtude — paciência, justiça, engenho — posso exercer agora?"
   },
   {
    "ic": "target",
    "t": "A Cláusula de Reserva",
    "b": "Aja com <strong>empenho total</strong>, mas acrescentando 'se nada o impedir'. Comprometa-se com o esforço (que é seu), não com o resultado (que não depende só de você). Assim você protege a paz sem cair no desleixo.",
    "tip": "<strong>Para refletir:</strong> apegar-se ao resultado é entregar a serenidade ao acaso."
   }
  ]
 },
 "ch06-memento-mori-impermanencia": {
  "cards": [
   {
    "ic": "clock",
    "t": "Memento Mori",
    "b": "A morte é certa, natural e iminente; tê-la diante dos olhos <strong>depura as prioridades</strong> e dissolve a vaidade. 'Faze, dize e pensa cada coisa como quem pode deixar a vida já' — aja como se este ato pudesse ser o último.",
    "tip": "<strong>Como aplicar:</strong> contra a procrastinação e a mesquinhez, lembre-se de que adiar a virtude é apostar num amanhã que pode não vir."
   },
   {
    "ic": "wave",
    "t": "Tudo Flui (Panta Rhei)",
    "b": "A substância do universo é um <strong>rio</strong>: nada é estável — nem o corpo, nem as coisas, nem a fama. Veja cada estado como passageiro; o presente é o único instante real, e ele já está virando passado.",
    "tip": "<strong>Modelo mental:</strong> não se apegue ao que, por natureza, passa — inclusive a você mesmo."
   },
   {
    "ic": "pin",
    "t": "Só se Perde o Presente",
    "b": "Ninguém perde o passado (que já não é) nem o futuro (que ainda não é) — <strong>só o agora</strong>. Logo, longa ou curta, toda vida perde a mesma coisa. A fama póstuma é fumaça: até quem se lembra de você logo morrerá.",
    "tip": "<strong>Para refletir:</strong> viva o presente; é a única posse real, e a única que se pode perder."
   }
  ]
 },
 "ch07-visao-do-alto-e-pessoas-dificeis": {
  "cards": [
   {
    "ic": "eye",
    "t": "A Visão do Alto",
    "b": "Imagine-se contemplando a Terra do alto — multidões, exércitos, festas, mercados, tudo <strong>minúsculo e fugaz</strong>. Amplie a escala no tempo (a eternidade) e no espaço (o cosmos), e vaidades e ofensas perdem o tamanho.",
    "tip": "<strong>Como aplicar:</strong> contra orgulho e ira, veja a si e ao conflito como um ponto na imensidão."
   },
   {
    "ic": "person",
    "t": "O Preparo Matinal",
    "b": "Ao amanhecer, diga: 'encontrarei o ingrato, o arrogante, o invejoso'. E logo desarme: eles erram por <strong>ignorância do bem</strong>; somos feitos para cooperar como pés e mãos; ninguém me fere a menos que eu julgue ter sido ferido.",
    "tip": "<strong>Modelo mental:</strong> a surpresa é metade da irritação — antecipe o atrito para não ser pego por ele."
   },
   {
    "ic": "mask",
    "t": "Não Imitar o Agressor",
    "b": "Quem age mal <strong>não viu o bem</strong> (tese socrática): merece correção e pena, não ódio. Esperar que o invejoso não inveje é como esperar que a figueira não dê figos. A melhor vingança é não te assemelhares a quem te feriu.",
    "tip": "<strong>Para refletir:</strong> devolver o mal é deixar o ofensor vencer duas vezes."
   }
  ]
 },
 "ch08-cosmopolitismo-dever-serenidade": {
  "cards": [
   {
    "ic": "constellation",
    "t": "Cidadão do Mundo",
    "b": "Como ser racional, minha cidade é Roma; como homem, minha cidade é o <strong>universo</strong>. A razão partilhada faz de todos os homens concidadãos. O que é bom para a colmeia é bom para a abelha: sirva ao todo e servirá a si.",
    "tip": "<strong>Modelo mental:</strong> contra o tribalismo e o egoísmo, lembre que não há bem teu separado do bem do conjunto."
   },
   {
    "ic": "steps",
    "t": "O Dever (Kathēkon)",
    "b": "Cumprir a <strong>própria função</strong> — o papel que a natureza e a posição te deram — sem reclamar. Levante-se para o trabalho de homem; faça o que está à sua frente com seriedade, justiça e simplicidade, em vez de fugir da tarefa.",
    "tip": "<strong>Para refletir:</strong> poupar-se do dever é trair a própria função no corpo do mundo."
   },
   {
    "ic": "key",
    "t": "A Serenidade da Alma Simples",
    "b": "A paz não vem de retiros, mas de uma <strong>mente reta</strong>. As pessoas buscam praias e montanhas para escapar; mas não há refúgio mais tranquilo que a própria alma. 'Não percas tempo discutindo o que é um homem bom: sê um.'",
    "tip": "<strong>Como aplicar:</strong> inquieto? Volte-se para dentro, para os princípios verdadeiros — e renove-se ali."
   }
  ]
 }
}
```
