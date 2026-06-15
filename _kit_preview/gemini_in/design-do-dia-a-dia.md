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

# LIVRO PARA APROFUNDAR: O Design do Dia a Dia — Don Norman

**Subtítulo:** VISÃO GERAL · OS PRINCÍPIOS DO DESIGN CENTRADO NO HUMANO
**Ideia central:** Por que algumas portas a gente empurra quando deveria puxar, e sai com a sensação de ser burro? Don Norman responde: a culpa é do design, não do usuário. Nesta obra fundadora da UX, ele mostra que objetos bem projetados comunicam sozinhos o que se pode fazer e o que cada coisa significa — e nos dá o vocabulário para enxergar (e consertar) o mau design em tudo à nossa volta.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-psicopatologia` — CAPÍTULO 1: A Psicopatologia das Coisas do Dia a Dia
- `ch02-affordances-significantes-mapeamento` — CAPÍTULO 2: Affordances, Significantes, Mapeamento e Feedback
- `ch03-psicologia-das-acoes` — CAPÍTULO 3: A Psicologia das Ações do Dia a Dia
- `ch04-conhecimento-cabeca-mundo` — CAPÍTULO 4: Conhecimento na Cabeça e no Mundo
- `ch05-restricoes-descoberta` — CAPÍTULO 5: Restrições, Descobribilidade e Feedback
- `ch06-funcoes-de-forca` — CAPÍTULO 6: Funções de Força — Tornar Difícil o Erro Grave
- `ch07-erro-humano-mau-design` — CAPÍTULO 7: Erro Humano? Não, Mau Design
- `ch08-design-a-prova-de-erro` — CAPÍTULO 8: Design à Prova de Erro
- `ch09-design-centrado-no-humano` — CAPÍTULO 9: Design Centrado no Humano e Design Thinking
- `ch10-design-no-mundo-dos-negocios` — CAPÍTULO 10: Design no Mundo dos Negócios

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-psicopatologia": {
  "cards": [
   {
    "ic": "key",
    "t": "A Culpa é do Design, Não do Usuário",
    "b": "O princípio fundador. Se as pessoas erram sistematicamente num objeto, o objeto está mal projetado — não as pessoas mal preparadas. Troque <strong>'por que erraram?'</strong> por <strong>'o que no design induziu o erro?'</strong>.",
    "tip": "<strong>Como aplicar:</strong> nunca encerre a análise em 'erro humano'; é onde a investigação deveria começar, no design."
   },
   {
    "ic": "eye",
    "t": "Descobribilidade e Compreensão",
    "b": "Dois testes de todo objeto. <strong>Descobribilidade</strong>: dá para descobrir quais ações são possíveis e como executá-las? <strong>Compreensão</strong>: o que tudo isso significa, como devo usar? Um bom produto torna o que se pode fazer <strong>visível</strong>.",
    "tip": "<strong>Modelo mental:</strong> o objeto é um comunicador — deve 'dizer' o que faz sem palavras."
   },
   {
    "ic": "gap",
    "t": "As \"Portas Norman\"",
    "b": "O exemplo-ícone do mau design: a porta cujo design <strong>'mente'</strong> sobre como operá-la — você puxa quando deveria empurrar. Se a porta precisa de uma placa 'EMPURRE', o design já falhou. A solução é um significante físico: barra para puxar, placa para empurrar.",
    "tip": "<strong>Sinal de alerta:</strong> se a operação básica exige etiqueta ou manual, o design está errado."
   }
  ]
 },
 "ch02-affordances-significantes-mapeamento": {
  "cards": [
   {
    "ic": "target",
    "t": "Affordances × Significantes",
    "b": "<strong>Affordance</strong> é a relação entre o objeto e quem usa, que determina o que é possível fazer (uma cadeira oferece sentar). <strong>Significante</strong> é o sinal perceptível que indica <strong>onde e como agir</strong>. A affordance existe; o significante a anuncia — e é ele que o designer mais controla.",
    "tip": "<strong>Como aplicar:</strong> não basta a ação ser possível; torne-a visível com um significante claro (seta, barra, rótulo)."
   },
   {
    "ic": "link",
    "t": "Mapeamento Natural",
    "b": "É a correspondência entre controles e seus efeitos. O <strong>mapeamento natural</strong> usa analogias espaciais/culturais para ser entendido na hora — como controles do fogão dispostos igual às bocas, dispensando etiquetas.",
    "tip": "<strong>Como aplicar:</strong> quando houver correspondência espacial óbvia, espelhe-a no layout dos controles."
   },
   {
    "ic": "wave",
    "t": "Feedback Imediato",
    "b": "Informação instantânea e informativa sobre o resultado de uma ação. Sem feedback, o usuário fica inseguro e <strong>repete a ação</strong> (às vezes disparando duas vezes). Mas feedback em excesso vira ruído e é ignorado.",
    "tip": "<strong>Cuidado:</strong> nem ausente, nem excessivo — calibre a prioridade do que o produto comunica."
   }
  ]
 },
 "ch03-psicologia-das-acoes": {
  "cards": [
   {
    "ic": "steps",
    "t": "Os 7 Estágios da Ação",
    "b": "O ciclo completo de uma ação, útil para diagnosticar onde a interface falha: <strong>Objetivo → Plano → Especificar → Executar → Perceber → Interpretar → Comparar</strong> com o objetivo. Localize em qual estágio o usuário trava.",
    "tip": "<strong>Como aplicar:</strong> use os 7 estágios como checklist de diagnóstico de qualquer interface."
   },
   {
    "ic": "gap",
    "t": "Os Dois Golfos",
    "b": "O <strong>Golfo da Execução</strong> ('como eu faço?') é a distância entre intenção e ação — estreitado por significantes, mapeamento e restrições. O <strong>Golfo da Avaliação</strong> ('o que aconteceu? deu certo?') é a distância entre o estado do sistema e o entendimento — estreitado por feedback e bom modelo conceitual.",
    "tip": "<strong>Modelo mental:</strong> o trabalho do designer é construir pontes sobre os dois golfos."
   },
   {
    "ic": "lens",
    "t": "Os 3 Níveis de Processamento",
    "b": "O design afeta a pessoa em três camadas: o <strong>visceral</strong> (reação imediata, estética, instinto), o <strong>comportamental</strong> (uso, expectativa, controle) e o <strong>reflexivo</strong> (significado, memória, autoimagem).",
    "tip": "<strong>Como aplicar:</strong> projete para os três — primeira impressão, facilidade de uso e o significado que fica."
   }
  ]
 },
 "ch04-conhecimento-cabeca-mundo": {
  "cards": [
   {
    "ic": "book",
    "t": "Conhecimento no Mundo × na Cabeça",
    "b": "<strong>No mundo</strong>: informação visível no objeto (rótulos, formatos, posições) — fácil de usar, dispensa decorar. <strong>Na cabeça</strong>: memorizada — eficiente, mas frágil e exige aprendizado. Distinguimos moedas no bolso sem saber desenhá-las: o objeto carrega o que precisamos.",
    "tip": "<strong>Como aplicar:</strong> sempre que exigir memória, pergunte 'posso deixar isto visível no objeto?'."
   },
   {
    "ic": "bulb",
    "t": "Modelo Conceitual × Modelo Mental",
    "b": "O <strong>modelo conceitual</strong> é a explicação simplificada de como o objeto funciona, que o design comunica. O <strong>modelo mental</strong> é o que o usuário constrói na cabeça. Quando os dois divergem, surgem os erros (ex.: 'girar o termostato no máximo aquece mais rápido').",
    "tip": "<strong>Modelo mental:</strong> erros nascem quando o que o usuário acredita não bate com como a coisa realmente funciona."
   },
   {
    "ic": "eye",
    "t": "A Imagem do Sistema",
    "b": "O designer não fala direto com o usuário: ele só se comunica pela <strong>imagem do sistema</strong> — tudo que o usuário consegue ver e perceber do produto. Se o modelo conceitual não está visível no produto, ele <strong>não existe</strong> para o usuário.",
    "tip": "<strong>Como aplicar:</strong> torne o modelo conceitual visível na própria interface; é o único canal que você tem."
   }
  ]
 },
 "ch05-restricoes-descoberta": {
  "cards": [
   {
    "ic": "scale",
    "t": "As 4 Restrições",
    "b": "O quarteto que orienta a ação. <strong>Físicas</strong>: a geometria impede o caminho errado (a tomada que só encaixa numa orientação). <strong>Culturais</strong>: convenções aprendidas (vermelho = parar). <strong>Semânticas</strong>: o significado da situação restringe (o vidro vai na frente). <strong>Lógicas</strong>: o raciocínio elimina alternativas (sobrou uma peça e um buraco — é ali).",
    "tip": "<strong>Como aplicar:</strong> combine as quatro para que a única ação possível seja a correta."
   },
   {
    "ic": "link",
    "t": "Convenções e Padronização",
    "b": "Quando não há mapeamento natural, <strong>padronize</strong> (pedais, teclado QWERTY). A convenção vira conhecimento cultural compartilhado e reduz o que cada um precisa aprender do zero.",
    "tip": "<strong>Regra:</strong> sem analogia espacial óbvia, a próxima melhor coisa é a uniformidade."
   },
   {
    "ic": "wave",
    "t": "O Som como Confirmação",
    "b": "Ruídos naturais (o clique da fechadura, o zíper) funcionam como <strong>feedback e significantes</strong>: confirmam que a ação aconteceu. Silenciar mal um produto remove esse sinal e gera insegurança.",
    "tip": "<strong>Cuidado:</strong> ao 'limpar' os sons de um produto, você pode estar removendo feedback essencial."
   }
  ]
 },
 "ch06-funcoes-de-forca": {
  "cards": [
   {
    "ic": "sword",
    "t": "Funções de Força: os 3 tipos",
    "b": "Restrições que interrompem a operação a menos que o passo certo seja cumprido. <strong>Interlock</strong>: força uma ordem (o micro-ondas não liga de porta aberta). <strong>Lock-in</strong>: impede encerrar cedo ('salvar antes de sair?'). <strong>Lock-out</strong>: bloqueia zona perigosa (escada barrada no térreo).",
    "tip": "<strong>Como aplicar:</strong> use quando o custo do erro for alto — escolha o tipo pela natureza do risco."
   },
   {
    "ic": "constellation",
    "t": "Poka-yoke (À Prova de Erro)",
    "b": "Princípio da qualidade japonesa: projetar para que a montagem ou operação errada seja <strong>fisicamente impossível</strong>. Pinos assimétricos, encaixes únicos, contadores de peças — dispositivos simples que eliminam classes inteiras de erro.",
    "tip": "<strong>Regra:</strong> o melhor controle de erro é a impossibilidade física de errar."
   },
   {
    "ic": "bubble",
    "t": "Aviso Não Basta para o Grave",
    "b": "Para erros sérios e irreversíveis, confiar só em avisos ('cuidado!') é fraco — o usuário se distrai, especialmente sob estresse. O erro grave precisa ser <strong>bloqueado</strong>, não advertido.",
    "tip": "<strong>Cuidado:</strong> funções de força no lugar errado viram burocracia e são burladas — anulando também a proteção real."
   }
  ]
 },
 "ch07-erro-humano-mau-design": {
  "cards": [
   {
    "ic": "pivot",
    "t": "Deslizes × Enganos",
    "b": "A distinção mestre. <strong>Deslize (slip)</strong>: o objetivo está certo, mas a ação sai errada — por desatenção, em tarefas automáticas. <strong>Engano (mistake)</strong>: a ação é executada certa, mas o objetivo ou plano estava errado — falha de decisão ou de modelo mental.",
    "tip": "<strong>Como aplicar:</strong> pergunte 'objetivo certo ou errado?'. Certo + ação ruim = deslize; errado de origem = engano."
   },
   {
    "ic": "target",
    "t": "Remédios Distintos por Tipo",
    "b": "Deslizes pedem <strong>feedback, restrições, undo e funções de força</strong> (proteger a execução). Enganos pedem <strong>melhor modelo conceitual e informação</strong> (corrigir a decisão). Tratar os dois igual não funciona.",
    "tip": "<strong>Modelo mental:</strong> deslize é falha de execução; engano é falha de planejamento — remédios diferentes."
   },
   {
    "ic": "mask",
    "t": "Mode Error e a Raiz Sistêmica",
    "b": "O <strong>deslize de modo (mode error)</strong>: o sistema está num modo e o usuário pensa que está noutro — clássico de interfaces com modos invisíveis. Erros raramente têm causa única: em vez de 'quem errou?', pergunte <strong>'por que o sistema permitiu o erro?'</strong>.",
    "tip": "<strong>Cuidado:</strong> punir o operador e encerrar a análise garante que o erro se repita com a próxima pessoa."
   }
  ]
 },
 "ch08-design-a-prova-de-erro": {
  "cards": [
   {
    "ic": "steps",
    "t": "A Hierarquia da Defesa",
    "b": "Quatro camadas, nesta ordem: <strong>Prevenir</strong> (restrições e funções de força), <strong>tornar visível</strong> (bom feedback para perceber o erro logo), <strong>tornar reversível</strong> (undo barato) e <strong>confirmar</strong> — só o irreversível.",
    "tip": "<strong>Como aplicar:</strong> errar deve ser barato; se o erro custa caro, projete reversibilidade ou trava."
   },
   {
    "ic": "spark",
    "t": "O Poder do Desfazer (Undo)",
    "b": "A defesa mais poderosa contra deslizes: torna o erro inofensivo. Excluir um e-mail deve <strong>mover para a lixeira</strong> (reversível) com um discreto 'Desfazer', em vez de apagar com um pop-up 'Tem certeza?' que todos clicam no automático.",
    "tip": "<strong>Regra:</strong> reserve confirmações pesadas para o irreversível; para o resto, ofereça undo."
   },
   {
    "ic": "bubble",
    "t": "Mensagem de Erro como Ajuda",
    "b": "A mensagem deve explicar o problema <strong>e como corrigi-lo</strong>, em linguagem humana — nunca apenas acusar ('Erro 0x8007'). Idealmente, permita corrigir ali mesmo.",
    "tip": "<strong>Cuidado:</strong> confirmar tudo gera cegueira de confirmação — o usuário clica 'sim' até no irreversível."
   }
  ]
 },
 "ch09-design-centrado-no-humano": {
  "cards": [
   {
    "ic": "leaf",
    "t": "Design Centrado no Humano (HCD)",
    "b": "Filosofia que coloca as necessidades, capacidades e comportamento das pessoas em primeiro lugar — e adapta o design a elas, não o contrário. O processo: <strong>Observar → Idear → Prototipar → Testar</strong>, em ciclos rápidos e baratos.",
    "tip": "<strong>Como aplicar:</strong> prototipe para aprender; falhe cedo e barato. O protótipo é uma pergunta, não um produto."
   },
   {
    "ic": "mountain",
    "t": "O Duplo Diamante",
    "b": "Dois ciclos de divergir-convergir. <strong>Diamante 1</strong>: encontrar o problema certo (explorar, depois definir). <strong>Diamante 2</strong>: encontrar a solução certa (idear, depois entregar). Resolver bem o problema errado é inútil — use os '5 porquês' para chegar à causa-raiz.",
    "tip": "<strong>Modelo mental:</strong> antes de 'como resolvo?', pergunte 'qual é o problema real?'."
   },
   {
    "ic": "lens",
    "t": "Observe, Não Pergunte",
    "b": "Pesquisa observacional no contexto real revela necessidades que as pessoas não verbalizam. <strong>Comportamento real vence opinião declarada</strong>: não confie só no que dizem, observe o que fazem.",
    "tip": "<strong>Cuidado:</strong> pular direto para a solução e empilhar funções (featuritis) é projetar para o problema aparente, não o real."
   }
  ]
 },
 "ch10-design-no-mundo-dos-negocios": {
  "cards": [
   {
    "ic": "scale",
    "t": "As Forças que Distorcem o Design",
    "b": "Bom design é também <strong>negociação</strong> com prazo, orçamento, marketing, concorrência e legados — não busca da perfeição isolada. É isso que explica por que produtos 'óbvios' saem ruins.",
    "tip": "<strong>Modelo mental:</strong> pense no design como negociação de restrições, não como perfeição num vácuo."
   },
   {
    "ic": "spiral",
    "t": "Featuritis (Creeping Featurism)",
    "b": "A tendência de adicionar funções a cada versão — cada uma defensável, o conjunto insustentável. Mais funções vendem na vitrine, mas <strong>degradam o uso</strong>.",
    "tip": "<strong>Cuidado:</strong> não empilhe funções para 'vencer na lista de especificações'; cada uma cobra um preço em usabilidade."
   },
   {
    "ic": "clock",
    "t": "Incremental × Radical e os Legados",
    "b": "A inovação <strong>incremental</strong> melhora o que existe (a maioria, e mais segura); a <strong>radical</strong> cria categorias novas (rara, arriscada, lenta de aceitar). A tecnologia muda, as pessoas não tanto — e padrões/legados (o QWERTY) persistem por coordenação social, não por serem ótimos.",
    "tip": "<strong>Como aplicar:</strong> aposte no incremental como regra e trate o radical como aposta de longo prazo."
   }
  ]
 }
}
```
