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

# LIVRO PARA APROFUNDAR: Mais Esperto que o Diabo — Napoleon Hill

**Subtítulo:** VISÃO GERAL · DERIVA = CONTROLE · DECISÃO = LIBERDADE
**Ideia central:** Hill 'entrevista o Diabo' — alegoria das forças que sabotam a mente — e arranca a confissão: a arma mestra é a DERIVA (viver sem pensar por si). Escrito em 1938, publicado em 2011. ~98% das pessoas derivam; ~2% pensam por si.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-a-entrevista-alegorica` — CAPÍTULO 1: A Entrevista Alegórica com o Diabo
- `ch02-a-deriva` — CAPÍTULO 2: A Deriva (Drifting)
- `ch03-as-armas-do-diabo` — CAPÍTULO 3: As Armas do Diabo
- `ch04-o-hipnotismo-ritmico` — CAPÍTULO 4: O Hipnotismo Rítmico do Hábito
- `ch05-definicao-de-proposito` — CAPÍTULO 5: Definição de Propósito — o Antídoto
- `ch06-mente-dominante-autocontrole` — CAPÍTULO 6: A Mente Dominante e o Autocontrole
- `ch07-o-tempo-e-a-adversidade` — CAPÍTULO 7: O Tempo e a Adversidade
- `ch08-sistemas-que-produzem-derivantes` — CAPÍTULO 8: Os Sistemas que Produzem Derivantes
- `ch09-os-sete-principios-da-libertacao` — CAPÍTULO 9: Os Sete Princípios da Libertação

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-a-entrevista-alegorica": {
  "cards": [
   {
    "ic": "mask",
    "t": "O Diabo como Alegoria",
    "b": "O 'Diabo' não é literal: é <strong>a soma de todo medo, dúvida, procrastinação e hábito negativo</strong> que opera em nós. Personificá-lo o torna combatível — o inimigo sem nome é o mais poderoso.",
    "tip": "<strong>Como aplicar:</strong> quando travar, pergunte 'que tática está me usando agora — medo? procrastinação? dúvida?'"
   },
   {
    "ic": "bulb",
    "t": "O Outro Eu",
    "b": "Hill identifica um 'Outro Eu' — a parte que age com propósito definido — em oposição ao eu que deriva. <strong>Separar a voz da iniciativa da voz do medo</strong> é o primeiro passo para sair do controle.",
    "tip": "<strong>Modelo mental:</strong> o obstáculo ao sucesso raramente é falta de método; é a força interna que impede aplicá-lo."
   },
   {
    "ic": "eye",
    "t": "98% × 2%",
    "b": "~98% das pessoas são controláveis porque derivam. ~2% pensam por si, decidem rápido, persistem. <strong>A linha entre os dois grupos não é talento</strong> — é o hábito de decidir versus o hábito de aceitar passivamente.",
    "tip": "<strong>Sinal de alerta:</strong> saber a fórmula não basta — é preciso desarmar o que impede você de usá-la."
   }
  ]
 },
 "ch02-a-deriva": {
  "cards": [
   {
    "ic": "wave",
    "t": "Deriva: o Barco sem Leme",
    "b": "Deriva = aceitar passivamente o que a vida traz, sem decisão própria. <strong>O Diabo só controla quem consente</strong> — quem deriva. O não-derivante é 'fechado' para ele porque pensa por si e decide.",
    "tip": "<strong>Teste rápido:</strong> 'Eu escolhi isto, ou apenas aceitei?' Se aceitou sem escolher, está derivando."
   },
   {
    "ic": "person",
    "t": "O Não-Derivante",
    "b": "Critérios: <strong>tem propósito definido</strong> · decide rápido e muda devagar · controla a própria mente · aprende com a adversidade. A maioria deriva sem saber — reconhecer o hábito já é meio caminho para sair dele.",
    "tip": "<strong>Modelo mental:</strong> flexibilidade (mudar por nova informação) ≠ deriva (mudar por medo ou pressão)."
   },
   {
    "ic": "clock",
    "t": "A Indecisão como Porta",
    "b": "Quem não decide é decidido pelas circunstâncias. <strong>A indecisão é a porta de entrada da deriva</strong> — e uma vez dentro, o hábito de derivar se aprofunda a cada aceitação passiva.",
    "tip": "<strong>Sinal de alerta:</strong> a deriva confortável — agradável no curto prazo — é por isso a mais perigosa."
   }
  ]
 },
 "ch03-as-armas-do-diabo": {
  "cards": [
   {
    "ic": "sword",
    "t": "Os Seis Medos Básicos",
    "b": "Hill reduz os medos a seis: <strong>pobreza · crítica · doença · perda do amor · velhice · morte</strong>. Rastrear qual está por trás de uma hesitação o torna combatível. O medo da crítica é o mais paralisante para quem cria.",
    "tip": "<strong>Como aplicar:</strong> identifique qual dos 6 está agindo — e decida mesmo assim."
   },
   {
    "ic": "link",
    "t": "A Corrente do Medo",
    "b": "<strong>Medo → dúvida → indecisão → procrastinação</strong>. Cada etapa alimenta a seguinte. Quebre a corrente no <strong>primeiro elo</strong>: reconheça o medo, decida mesmo assim, aja imediatamente.",
    "tip": "<strong>Modelo mental:</strong> procrastinação = deriva no tempo. 'Depois' é o território do Diabo."
   },
   {
    "ic": "clock",
    "t": "Esperar o Medo Passar",
    "b": "<strong>A ação dissolve o medo</strong>, não o contrário. Esperar o medo passar antes de agir é entregar o leme — o Diabo ganha o tempo de que precisa para aprofundar o sulco.",
    "tip": "<strong>Sinal de alerta:</strong> racionalizar a indecisão como 'prudência' é um dos disfarces mais comuns da deriva."
   }
  ]
 },
 "ch04-o-hipnotismo-ritmico": {
  "cards": [
   {
    "ic": "spiral",
    "t": "A Lei Cósmica do Hábito",
    "b": "Pela repetição, um pensamento entra num 'ritmo' e a natureza o adota como padrão fixo. <strong>A lei é neutra</strong>: torna permanente o que você repete, bom ou mau. Não distingue — apenas fixa.",
    "tip": "<strong>Modelo mental:</strong> um sulco na rocha cavado pela água — gota a gota ele se aprofunda até a água correr sozinha."
   },
   {
    "ic": "steps",
    "t": "Instale o Ritmo Novo",
    "b": "Para mudar, <strong>não combata o hábito velho</strong> — instale o ritmo do novo até a natureza assumir. A força de vontade isolada perde para o sulco antigo; um novo sulco mais profundo vence.",
    "tip": "<strong>Como aplicar:</strong> repita deliberadamente o bom hábito até virar automático — o mesmo mecanismo que o Diabo usa para o mau."
   },
   {
    "ic": "clock",
    "t": "Repetição Negligente",
    "b": "Deixar a repetição ao acaso <strong>entrega o ritmo ao Diabo</strong>. A natureza não distingue o que você quer do que você pratica — ela fixa o que você de fato repete, inclusive inconscientemente.",
    "tip": "<strong>Sinal de alerta:</strong> o medo cede uma vez, depois de novo, depois de novo — e em meses entra no ritmo e opera sozinho."
   }
  ]
 },
 "ch05-definicao-de-proposito": {
  "cards": [
   {
    "ic": "target",
    "t": "Um Alvo Único e Claro",
    "b": "Passos: (1) escolha <strong>UM propósito dominante</strong>; (2) escreva-o; (3) crie um plano; (4) aja hoje; (5) repita até virar ritmo. Múltiplos objetivos vagos são deriva disfarçada de ambição.",
    "tip": "<strong>Modelo mental:</strong> o propósito é o leme do barco — não muda a correnteza, mas decide o destino apesar dela."
   },
   {
    "ic": "bulb",
    "t": "A Mente Fechada ao Diabo",
    "b": "\"A natureza abomina o vácuo\": uma <strong>mente sem propósito será preenchida por medos</strong>. A pessoa com propósito definido não tem 'espaço vazio' para o medo e a deriva ocuparem.",
    "tip": "<strong>Como aplicar:</strong> defina o alvo único; o resto é subproduto — ou deriva disfarçada de ambição."
   },
   {
    "ic": "clock",
    "t": "Definir sem Agir",
    "b": "<strong>Propósito sem ação imediata é procrastinação</strong> (Ch 3). Definir e não começar hoje é entregar o impulso ao Diabo — o tempo gasto sem agir aprofunda o sulco da inação.",
    "tip": "<strong>Sinal de alerta:</strong> 'vou começar amanhã' é a forma mais elegante de deriva."
   }
  ]
 },
 "ch06-mente-dominante-autocontrole": {
  "cards": [
   {
    "ic": "key",
    "t": "A Única Coisa Sua",
    "b": "O controle da própria mente é <strong>a única coisa sobre a qual se tem domínio completo</strong> — e é exatamente o que o Diabo quer que se largue. Recuse pensamentos negativos como um porteiro recusa um intruso.",
    "tip": "<strong>Modelo mental:</strong> a mente como uma casa com porta — você decide quem entra. Medo e pessimismo são visitas indesejadas."
   },
   {
    "ic": "person",
    "t": "Reação vs. Resposta",
    "b": "O derivante <strong>reage automaticamente</strong>; o não-derivante escolhe a resposta. A diferença entre os dois é o intervalo — o momento de recusa consciente antes de obedecer ao impulso.",
    "tip": "<strong>Como aplicar:</strong> ao sentir o impulso automático, pausa — 'estou reagindo ou respondendo?'"
   },
   {
    "ic": "constellation",
    "t": "Curar o Ambiente",
    "b": "Companhias, leituras e ambientes moldam a mente por contágio. <strong>Cercar-se de derivantes absorve, imperceptivelmente, a deriva deles.</strong> Escolha deliberadamente o ambiente mental.",
    "tip": "<strong>Sinal de alerta:</strong> terceirizar o estado de espírito (deixar o clima ou o humor alheio ditar o seu) é a forma mais silenciosa de deriva."
   }
  ]
 },
 "ch07-o-tempo-e-a-adversidade": {
  "cards": [
   {
    "ic": "clock",
    "t": "Juros Compostos do Hábito",
    "b": "O tempo <strong>multiplica o que você repete</strong>: aliado de quem decidiu, inimigo de quem deriva. A cada ano de deriva, o hábito fica mais profundo e a saída mais difícil.",
    "tip": "<strong>Modelo mental:</strong> deixar o tempo passar derivando é entregar a composição ao Diabo."
   },
   {
    "ic": "leaf",
    "t": "A Semente de Benefício",
    "b": "Toda adversidade traz a semente de um benefício equivalente — para quem <strong>a procura em vez de derivar no lamento</strong>. O próprio livro nasceu de Hill numa crise — a adversidade forçou o propósito definido.",
    "tip": "<strong>Como aplicar:</strong> diante do fracasso, pergunte 'qual é a semente de benefício aqui?' e plante-a."
   },
   {
    "ic": "bulb",
    "t": "Sabedoria vs. Idade",
    "b": "Sabedoria = conhecimento + tempo + aplicação. O derivante <strong>envelhece sem sabedoria</strong> porque não aprende com a experiência — acumula anos, não lições.",
    "tip": "<strong>Sinal de alerta:</strong> o tempo com propósito gera sabedoria; sem propósito, só gera mais deriva."
   }
  ]
 },
 "ch08-sistemas-que-produzem-derivantes": {
  "cards": [
   {
    "ic": "layers",
    "t": "Fábricas de Hábitos Mentais",
    "b": "Sistemas que premiam conformidade e medo <strong>configuram de fábrica</strong> uma pessoa para derivar. Conformidade premiada treina a aceitação passiva — a matéria-prima da deriva.",
    "tip": "<strong>Como reconhecer:</strong> quando um sistema pede obediência sem entendimento, memorização sem pensamento, medo em vez de propósito."
   },
   {
    "ic": "fork",
    "t": "Educar vs. Condicionar",
    "b": "<strong>Educar</strong> (do latim <em>educere</em>) = extrair pensamento de dentro. <strong>Condicionar</strong> = impor medo e regras de fora. A maioria das instituições condicionam — e treinam, sem querer, a deriva.",
    "tip": "<strong>Modelo mental:</strong> use qualquer sistema para extrair pensamento; não o deixe usá-lo para instalar medo."
   },
   {
    "ic": "person",
    "t": "Atravessar sem Ser Configurado",
    "b": "Não é preciso abandonar os sistemas — é preciso <strong>atravessá-los pensando por si</strong>. O não-derivante usa a instituição sem ser usado por ela; nem obediência cega, nem rebeldia cega.",
    "tip": "<strong>Sinal de alerta:</strong> a rebeldia por reflexo também é deriva — reagir sem decidir ainda é entregar o leme."
   }
  ]
 },
 "ch09-os-sete-principios-da-libertacao": {
  "cards": [
   {
    "ic": "steps",
    "t": "O Cadeado de Sete Pinos",
    "b": "<strong>1. Propósito definido · 2. Autocontrole · 3. Aprender com a adversidade · 4. Controlar associações · 5. Tempo · 6. Harmonia · 7. Cautela.</strong> Funcionam como sistema — falta um pino, o cadeado não abre.",
    "tip": "<strong>Diagnóstico reverso:</strong> ao derivar, pergunte 'qual dos 7 abandonei?'"
   },
   {
    "ic": "target",
    "t": "Harmonia e Cautela",
    "b": "<strong>Harmonia</strong>: alinhar pensamentos, propósito e ambiente para que tudo 'puxe' na mesma direção, sem conflito interno. <strong>Cautela</strong>: pensar o plano antes de agir - não é indecisão, é decisão bem feita.",
    "tip": "<strong>Distinção crítica:</strong> cautela decide depois de pensar; indecisão nunca decide. Não confunda os dois."
   },
   {
    "ic": "constellation",
    "t": "Sistema, Não Menu",
    "b": "Os sete não são opcionais avulsos — cada um protege o outro. Ter propósito mas sem autocontrole, ou autocontrole sem propósito, <strong>mantém a porta do Diabo entreaberta</strong>.",
    "tip": "<strong>Como aplicar:</strong> use os 7 como checklist: qual está faltando agora? Aplique-o antes de insistir no que já tem."
   }
  ]
 }
}
```
