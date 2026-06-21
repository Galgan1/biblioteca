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

# LIVRO PARA APROFUNDAR: Flow — Mihaly Csikszentmihalyi

**Subtítulo:** VISÃO GERAL · A PSICOLOGIA DO ALTO DESEMPENHO E DA FELICIDADE
**Ideia central:** A felicidade não é sorte nem dinheiro: é a qualidade da experiência interior, e pode ser cultivada. Csikszentmihalyi mostra que o melhor momento da vida é o flow — imersão total numa atividade desafiadora que se domina — e ensina a produzi-lo controlando a atenção, transformando trabalho, lazer e até a adversidade em ordem na consciência.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-a-felicidade-revisitada` — CAPÍTULO 1: A Felicidade Revisitada
- `ch02-a-anatomia-da-consciencia` — CAPÍTULO 2: A Anatomia da Consciência
- `ch03-fruicao-e-qualidade-de-vida` — CAPÍTULO 3: Fruição e Qualidade de Vida
- `ch04-as-condicoes-do-flow` — CAPÍTULO 4: As Condições do Flow
- `ch05-o-corpo-em-flow` — CAPÍTULO 5: O Corpo em Flow
- `ch06-o-flow-do-pensamento` — CAPÍTULO 6: O Flow do Pensamento
- `ch07-o-trabalho-como-flow` — CAPÍTULO 7: O Trabalho como Flow
- `ch08-fruir-a-solidao-e-os-outros` — CAPÍTULO 8: Fruir a Solidão e os Outros
- `ch09-driblando-o-caos` — CAPÍTULO 9: Driblando o Caos
- `ch10-a-construcao-do-sentido` — CAPÍTULO 10: A Construção do Sentido

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-a-felicidade-revisitada": {
  "cards": [
   {
    "ic": "leaf",
    "t": "Felicidade Construída",
    "b": "A felicidade <strong>não pode ser perseguida diretamente</strong> — quem a busca de frente, foge dela. Ela é subproduto de estar totalmente envolvido em cada detalhe da vida. Quem controla a vida interior determina a qualidade da própria vida.",
    "tip": "<strong>Modelo mental:</strong> o alvo certo não é 'o que tenho', é como organizo minha atenção e experiência."
   },
   {
    "ic": "mountain",
    "t": "As Raízes do Descontentamento",
    "b": "O universo não foi feito para o conforto humano: entropia, doença, morte. A <strong>frustração é o estado-base</strong>; a ordem (felicidade) precisa ser conquistada contra essa corrente.",
    "tip": "<strong>Para refletir:</strong> o progresso material elevou as expectativas no mesmo ritmo — por isso a satisfação não acompanhou."
   },
   {
    "ic": "book",
    "t": "Os Escudos da Cultura",
    "b": "Religião, mitos e filosofias são <strong>escudos contra o caos</strong>. Funcionam por um tempo, mas quando perdem credibilidade (era secular), a pessoa fica sem proteção e precisa <strong>construir sentido por conta própria</strong>.",
    "tip": "<strong>Modelo mental:</strong> se o escudo herdado rachou, defender-se do caos vira tarefa pessoal."
   }
  ]
 },
 "ch02-a-anatomia-da-consciencia": {
  "cards": [
   {
    "ic": "key",
    "t": "Atenção = Energia Psíquica",
    "b": "A atenção seleciona o que entra na consciência. É <strong>limitada</strong> (~126 bits/s; conversar consome quase metade) — por isso 'investir a atenção' é a decisão mais importante que tomamos.",
    "tip": "<strong>Modelo mental:</strong> trate a atenção como orçamento — onde se gasta define a experiência e o eu."
   },
   {
    "ic": "spiral",
    "t": "Entropia × Negentropia",
    "b": "<strong>Entropia psíquica</strong>: desordem na consciência — medo, raiva, tédio, ansiedade; o estado normal da mente desocupada. <strong>Ordem (flow)</strong>: a energia psíquica fluindo sem esforço para a meta.",
    "tip": "<strong>Para ler qualquer estado mental:</strong> a informação que chega briga com suas metas (sofre) ou serve a elas (flui)?"
   },
   {
    "ic": "layers",
    "t": "O Crescimento do Eu",
    "b": "Cada flow torna o eu mais <strong>complexo</strong>, por dois movimentos: <strong>diferenciação</strong> (tornar-se único) e <strong>integração</strong> (ligar-se a algo maior). O eu complexo combina os dois.",
    "tip": "<strong>Modelo mental:</strong> crescer = ser mais você mesmo E mais conectado ao mundo, ao mesmo tempo."
   }
  ]
 },
 "ch03-fruicao-e-qualidade-de-vida": {
  "cards": [
   {
    "ic": "spark",
    "t": "Prazer × Fruição",
    "b": "<strong>Prazer</strong> satisfaz e restaura a homeostase (comer, dormir), mas não cria nada nem se lembra. <strong>Fruição</strong> (enjoyment) vem de novidade e superação — leva o eu a crescer.",
    "tip": "<strong>Teste:</strong> depois, você se sente igual (prazer) ou maior/mais capaz (fruição)?"
   },
   {
    "ic": "target",
    "t": "Os 8 Elementos do Flow",
    "b": "Desafio ≈ habilidade · concentração total · <strong>metas claras</strong> · <strong>feedback imediato</strong> · envolvimento sem esforço · senso de controle · perda da autoconsciência · distorção do tempo.",
    "tip": "<strong>Como usar:</strong> faltou flow? Veja qual elemento estava ausente — em geral, metas vagas ou sem feedback."
   },
   {
    "ic": "spiral",
    "t": "Experiência Autotélica",
    "b": "Do grego <em>auto</em> (em si) + <em>telos</em> (fim): a atividade vale pela <strong>própria recompensa</strong>, não por ganho externo. É o que transforma esforço em fruição.",
    "tip": "<strong>Selo de qualidade:</strong> a melhor atividade é a que você faria mesmo sem recompensa externa."
   }
  ]
 },
 "ch04-as-condicoes-do-flow": {
  "cards": [
   {
    "ic": "scale",
    "t": "O Canal de Flow",
    "b": "Cruze desafio × habilidade: alto/baixa = <strong>ansiedade</strong>; baixo/alta = <strong>tédio</strong>; baixo/baixa = <strong>apatia</strong> (o pior); <strong>alto/alta = flow</strong>.",
    "tip": "<strong>Diagnóstico:</strong> ansioso? treine a habilidade ou simplifique. Entediado? suba o desafio."
   },
   {
    "ic": "steps",
    "t": "A Espiral de Crescimento",
    "b": "Como o flow exige equilíbrio e ambos os lados sobem com a prática, ele <strong>empurra para desafios cada vez maiores</strong> — daí ser um motor de complexidade do eu. Ficar no mesmo nível entedia.",
    "tip": "<strong>Modelo mental:</strong> flow é alvo móvel — só permanece se você sobe junto com sua habilidade."
   },
   {
    "ic": "person",
    "t": "Personalidade Autotélica",
    "b": "A disposição de quem cria flow <strong>mesmo sem condições externas favoráveis</strong>: define metas próprias, mergulha na ação, presta atenção, frui o aqui-e-agora. É a habilidade central que o livro ensina.",
    "tip": "<strong>Para treinar:</strong> comece definindo metas próprias e dando atenção plena ao que faz."
   }
  ]
 },
 "ch05-o-corpo-em-flow": {
  "cards": [
   {
    "ic": "wave",
    "t": "O Fluxo do Movimento",
    "b": "Esporte e dança dão metas, regras e feedback prontos; o atleta entra em flow ao esticar o corpo até o limite da destreza. <strong>Qualquer ação física rotineira</strong> vira desafio com meta mensurável.",
    "tip": "<strong>Como aplicar:</strong> caminhar vira flow ao virar 'andar X em Y' — meta + atenção transforma qualquer função física."
   },
   {
    "ic": "leaf",
    "t": "O Domínio do Corpo",
    "b": "Tradições como ioga e artes marciais são <strong>'tecnologias de flow'</strong>: controlam consciência e corpo ao mesmo tempo — a ioga como controle disciplinado da energia psíquica via o físico.",
    "tip": "<strong>Para refletir:</strong> o domínio do corpo é também domínio da atenção."
   },
   {
    "ic": "eye",
    "t": "Os Sentidos como Flow",
    "b": "Ver (artes visuais), ouvir (música) e saborear viram fruição quando se aprende a <strong>discriminar e apreciar com atenção treinada</strong>. Não é dom — é habilidade cultivável.",
    "tip": "<strong>Anti-padrão:</strong> consumo passivo (música de fundo, comer no automático) é prazer raso, nunca flow."
   }
  ]
 },
 "ch06-o-flow-do-pensamento": {
  "cards": [
   {
    "ic": "constellation",
    "t": "A Mente como Campo de Flow",
    "b": "Pensar (resolver, criar, especular) reúne metas, regras e feedback <strong>internos</strong>; quando o desafio cognitivo ≈ habilidade mental, surge flow puramente mental — sem nenhum estímulo externo.",
    "tip": "<strong>Modelo mental:</strong> a mente bem ocupada é negentropia em ação."
   },
   {
    "ic": "book",
    "t": "A Memória como Playground",
    "b": "Ter conhecimento de cor (poemas, fatos, padrões) é o que permite o flow do pensamento <strong>em qualquer fila ou insônia</strong>. Quem memorizou tem um parque mental sempre à mão.",
    "tip": "<strong>Anti-padrão:</strong> a mente terceirizada à tela — depender de feed/TV por nunca ter cultivado conteúdo interno."
   },
   {
    "ic": "spark",
    "t": "Pensar por Amor",
    "b": "O <strong>amador</strong> (do latim <em>amare</em>, amar) faz pela fruição, não pela carreira. Ciência, filosofia, escrita feitas por amor são vias puras de flow intelectual.",
    "tip": "<strong>Selo:</strong> a melhor atividade mental é a que você faria sem ganhar nada por ela."
   }
  ]
 },
 "ch07-o-trabalho-como-flow": {
  "cards": [
   {
    "ic": "pivot",
    "t": "O Paradoxo do Trabalho",
    "b": "As pessoas relatam <strong>mais flow no trabalho do que no lazer</strong> — mas dizem preferir o lazer e querer trabalhar menos. Vivem o melhor onde menos querem estar.",
    "tip": "<strong>Alerta:</strong> ao 'querer fugir para o fim de semana', cheque se o lazer é de flow ou só ócio passivo (entropia)."
   },
   {
    "ic": "wrench",
    "t": "O Trabalho Autotélico",
    "b": "Emprego redesenhado para <strong>parecer um jogo</strong>: variedade, desafios apropriados, metas claras, feedback. Até tarefas humildes podem ser refeitas assim (o operário que cronometra e bate o próprio recorde).",
    "tip": "<strong>Como aplicar:</strong> imponha metas pessoais e busque o gesto mais elegante dentro das restrições do cargo."
   },
   {
    "ic": "target",
    "t": "Lazer Ativo × Passivo",
    "b": "Lazer <strong>não é bom por definição</strong>: hobbies, esportes e leitura geram flow; TV e ócio são terreno de entropia. A personalidade autotélica cria flow em qualquer ocupação.",
    "tip": "<strong>Para refletir:</strong> a atitude pesa mais que o cargo — o mesmo emprego entedia um e entusiasma outro."
   }
  ]
 },
 "ch08-fruir-a-solidao-e-os-outros": {
  "cards": [
   {
    "ic": "person",
    "t": "A Solidão como Desafio",
    "b": "Estar só é difícil porque a mente desocupada cai na entropia. Quem cultiva hobbies, leitura e ofícios internos <strong>transforma a solidão em flow</strong> em vez de fugir dela.",
    "tip": "<strong>Teste do eu:</strong> quem não suporta ficar só sem estímulo ainda não domina a própria consciência."
   },
   {
    "ic": "link",
    "t": "Relações que Produzem Flow",
    "b": "Família e amizades geram fruição quando há <strong>metas comuns, feedback mútuo e desafios crescentes</strong> — não com companhia passiva. A relação autotélica combina diferenciação e integração.",
    "tip": "<strong>Regra:</strong> convívio sem meta comum entedia; objetivo partilhado faz crescer."
   },
   {
    "ic": "layers",
    "t": "Diferenciação × Integração",
    "b": "Bons vínculos fazem cada membro <strong>mais único E mais ligado ao todo</strong>, ao mesmo tempo. Integração sem diferenciação sufoca; diferenciação sem integração isola.",
    "tip": "<strong>Modelo mental:</strong> a família boa deixa crescer junto e como indivíduo."
   }
  ]
 },
 "ch09-driblando-o-caos": {
  "cards": [
   {
    "ic": "spiral",
    "t": "Transformar a Adversidade",
    "b": "O sofrimento é a <strong>entropia psíquica em estado máximo</strong>. Quem reformula a situação como desafio (não como catástrofe sem saída) recupera a ordem na consciência — como estruturas dissipativas extraem ordem do caos.",
    "tip": "<strong>Como aplicar:</strong> trate cada golpe como problema com metas possíveis dentro das novas restrições."
   },
   {
    "ic": "target",
    "t": "Olhar para Fora, Não para a Dor",
    "b": "As três condições para driblar o caos: <strong>confiança sem ego</strong>, <strong>atenção voltada ao mundo</strong> (não à própria angústia) e a <strong>busca ativa de novas soluções</strong>.",
    "tip": "<strong>Anti-padrão:</strong> ensimesmar-se na desgraça aprofunda a entropia e fecha as saídas."
   },
   {
    "ic": "mountain",
    "t": "Resiliência Transformativa",
    "b": "Não é só resistir — é <strong>crescer com a adversidade</strong>, usando a energia negativa da crise como combustível para um novo nível de complexidade do eu.",
    "tip": "<strong>Para refletir:</strong> não é o que acontece que decide o sofrimento, mas como a consciência o processa."
   }
  ]
 },
 "ch10-a-construcao-do-sentido": {
  "cards": [
   {
    "ic": "constellation",
    "t": "O Tema de Vida",
    "b": "A <strong>meta superior</strong> que dá direção a tudo — o projeto central em torno do qual se organiza a energia psíquica. Pode ser descoberto (herdado) ou <strong>forjado</strong> (criado autenticamente, e mais robusto na crise).",
    "tip": "<strong>Modelo mental:</strong> o sentido é o tema musical da vida — sem ele, as atividades são notas soltas."
   },
   {
    "ic": "scale",
    "t": "As Três Dimensões do Sentido",
    "b": "<strong>Propósito</strong> (uma meta final que ordena as demais) + <strong>resolução</strong> (esforço determinado) + <strong>harmonia</strong> (ordem interior quando intenção, sentimento e ação se alinham).",
    "tip": "<strong>Roteiro:</strong> escolha a meta-mestra, comprometa-se, e a harmonia interior virá como consequência."
   },
   {
    "ic": "leaf",
    "t": "A Vida como Flow Unificado",
    "b": "Com o tema de vida vivo, cada atividade vira parte de um flow maior — e até o sofrimento ganha lugar no projeto. A felicidade deixa de depender de eventos isolados e vira <strong>condição estável</strong>.",
    "tip": "<strong>Anti-padrão:</strong> colecionar flows e prazeres sem unidade é soma de momentos, não um sentido."
   }
  ]
 }
}
```
