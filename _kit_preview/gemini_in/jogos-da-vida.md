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

# LIVRO PARA APROFUNDAR: Os Jogos da Vida — Eric Berne

**Subtítulo:** VISÃO GERAL · AS TRANSAÇÕES QUE REPETEM A MESMA DOR
**Ideia central:** Eric Berne fundou a Análise Transacional com uma pergunta simples: por que as pessoas repetem os mesmos padrões dolorosos de relacionamento? A resposta: jogos — transações de duplo-fundo com um 'trambique' e um payoff prevísivel que confirma velhas convicções sobre si e o mundo.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-analise-estrutural` — CAPÍTULO 1: Análise Estrutural — Os Estados de Ego
- `ch02-analise-transacional` — CAPÍTULO 2: Análise Transacional — Os Três Tipos
- `ch03-estruturacao-do-tempo` — CAPÍTULO 3: A Estruturação do Tempo e as Carícias
- `ch04-os-jogos` — CAPÍTULO 4: Os Jogos — Definição e Anatomia
- `ch05-jogos-da-vida` — CAPÍTULO 5: Jogos do Dia a Dia
- `ch06-jogos-conjugais-sociais` — CAPÍTULO 6: Jogos Conjugais e Sociais
- `ch07-jogos-do-submundo` — CAPÍTULO 7: Jogos do Submundo — Os Graus Pesados
- `ch08-alem-dos-jogos-autonomia` — CAPÍTULO 8: Além dos Jogos — Roteiros e Autonomia
- `ch09-intimidade-saida` — CAPÍTULO 9: Intimidade — A Saída dos Jogos

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-analise-estrutural": {
  "cards": [
   {
    "ic": "triangle",
    "t": "Pai, Adulto e Criança",
    "b": "<strong>Pai (P)</strong>: copiado de figuras parentais — Crítico ('deveria/sempre/nunca') ou Nutritivo (cuida, protege). <strong>Adulto (A)</strong>: processa fatos do aqui-e-agora, neutro. <strong>Criança (C)</strong>: relíquia da infância — Livre (espontânea) ou Adaptada (obediente/rebelde).",
    "tip": "<strong>Como aplicar:</strong> pense no P-A-C como três fitas gravadas rodando dentro de você; a qualquer instante uma está no alto-falante. Qual está ativa agora?"
   },
   {
    "ic": "lens",
    "t": "Contaminação e Exclusão",
    "b": "<strong>Contaminação</strong>: preconceito do Pai ou medo infantil da Criança infiltrados no julgamento 'racional' do Adulto. <strong>Exclusão</strong>: bloquear um estado (ex.: a pessoa que nunca acessa a Criança Livre — sem espontaneidade nem prazer). Ambas geram sofrimento.",
    "tip": "<strong>Modelo mental:</strong> o Adulto saudável não elimina P e C — ele os administra conscientemente."
   },
   {
    "ic": "bubble",
    "t": "Diagnostique pelo Tom",
    "b": "O diagnóstico rápido usa <strong>tom de voz, vocabulário, postura e contexto histórico</strong>. 'Quantas vezes preciso repetir?' = Pai Crítico. 'Posso confirmar o prazo?' = Adulto. 'Você nunca explica direito!' = Criança Rebelde. Quanto mais critérios convergem, mais firme o diagnóstico.",
    "tip": "<strong>Regra:</strong> 'quem está falando agora?' — essa pergunta diagnóstica muda tudo. Faz-se a si mesmo e ao outro."
   }
  ]
 },
 "ch02-analise-transacional": {
  "cards": [
   {
    "ic": "link",
    "t": "Complementar × Cruzada",
    "b": "<strong>Complementar</strong>: a resposta vem do estado a que o estímulo se dirigiu — vetores paralelos, a comunicação pode prosseguir. <strong>Cruzada</strong>: a resposta parte de um estado inesperado — vetores se cruzam, a comunicação rompe. A maioria das brigas é uma transação cruzada não percebida.",
    "tip": "<strong>Como aplicar:</strong> para desarmar uma briga, cruze de propósito a transação ofensiva — responda pelo Adulto a um ataque Pai→Criança."
   },
   {
    "ic": "eye",
    "t": "Ulterior: O Duplo-Fundo",
    "b": "A transação ulterior opera em <strong>dois níveis simultâneos</strong>: a mensagem social (aberta) e a mensagem psicológica (oculta). <strong>O desfecho é determinado pelo nível psicológico, não pelo social.</strong> É a estrutura de todos os jogos — e a base de todo flerte, toda venda manipulada.",
    "tip": "<strong>Modelo mental:</strong> em vendas e flertes, escute o 'segundo andar' da frase. A mensagem social é a fachada; a psicológica é o convite real."
   },
   {
    "ic": "triangle",
    "t": "Exemplo Clássico (Angular)",
    "b": "Vendedor (social A→A): 'Este modelo é melhor, mas talvez fora do seu orçamento.' Psicológico (A→C): 'Duvido que você possa pagar.' Cliente (C→A): 'É esse que eu quero.' — A <strong>Criança mordeu a isca</strong> do nível psicológico; o social era apenas o disfarce.",
    "tip": "<strong>Sinal de alerta:</strong> quando uma frase parece neutra mas produz uma reação emocional forte, o nível psicológico foi ativado. Procure a mensagem oculta."
   }
  ]
 },
 "ch03-estruturacao-do-tempo": {
  "cards": [
   {
    "ic": "spark",
    "t": "Carícia: A Unidade de Reconhecimento",
    "b": "Uma carícia (stroke) é qualquer ato de reconhecimento — 'eu te vejo'. Pode ser <strong>positiva</strong> (elogio, afeto) ou <strong>negativa</strong> (crítica, briga). <strong>Princípio crítico</strong>: carícia negativa é melhor que nenhuma carícia. É por isso que as pessoas jogam jogos dolorosos — garantem um suprimento confiável de reconhecimento.",
    "tip": "<strong>Como aplicar:</strong> 'que carícia esta pessoa está buscando?' — essa pergunta está por trás de quase todo comportamento social difícil."
   },
   {
    "ic": "steps",
    "t": "As 6 Formas de Estruturar o Tempo",
    "b": "Do menor ao maior risco/recompensa: <strong>(1)</strong> Retraimento · <strong>(2)</strong> Rituais ('bom dia') · <strong>(3)</strong> Passatempos (conversa padrão) · <strong>(4)</strong> Atividades (trabalho) · <strong>(5)</strong> Jogos (muitas carícias, tóxicas) · <strong>(6)</strong> Intimidade (carícias autênticas, maior exposição).",
    "tip": "<strong>Modelo mental:</strong> pense nas 6 formas como escada de risco e recompensa. Quanto mais para cima, mais carícias verdadeiras — e mais vulnerabilidade exigida."
   },
   {
    "ic": "gap",
    "t": "O Passatempo Seleciona o Jogo",
    "b": "Passatempos são conversas semirritualizadas ('filhos', 'trânsito', 'futebol') que parecem inofensivas mas <strong>sondam parceiros</strong> para jogos e relações. Uma conversa de passatempo pode virar jogo se alguém usa para extrair um payoff — pena, superioridade, cumplicidade na queixa.",
    "tip": "<strong>Sinal de alerta:</strong> grupos que só reclamam e nunca agem estão no passatempo/jogo 'Não É Horrível?' — as carícias vêm da queixa, não da solução."
   }
  ]
 },
 "ch04-os-jogos": {
  "cards": [
   {
    "ic": "spiral",
    "t": "A Fórmula J Detalhada",
    "b": "<strong>Isca</strong> (Con): o convite ulterior do iniciador. <strong>Fraqueza</strong> (Gimmick): o ponto vulnerável que aceita a isca. <strong>Resposta</strong>: a sequência de transações. <strong>Virada</strong> (Switch): a troca súbita de papel — o coração do jogo. <strong>Confusão</strong>: desorientação pós-virada. <strong>Recompensa</strong>: o sentimento ruim familiar que cada um colhe.",
    "tip": "<strong>Regra diagnóstica:</strong> se a Fórmula J encaixa, é jogo. Preencha os 6 campos para qualquer padrão que se repete."
   },
   {
    "ic": "key",
    "t": "Por que os Jogos Persistem",
    "b": "Jogos rendem <strong>vantagens reais</strong> em camadas: biológica (carícias), psicológica (defende o equilíbrio, evita ansiedade), social (estrutura o tempo, dá 'assunto'), existencial (confirma a posição de vida e o roteiro). Por isso persistem mesmo sendo tóxicos — eles entregam algo que a pessoa não sabe obter de outra forma.",
    "tip": "<strong>Modelo mental:</strong> o payoff é como uma 'moeda emocional colecionável' — a pessoa junta selos ruins para resgatar o direito de explodir, deprimir ou romper."
   },
   {
    "ic": "target",
    "t": "Antítese: Recuse a Isca",
    "b": "A saída de um jogo é a <strong>antítese</strong>: o lance que recusa o jogo e o desarma. Não é confrontar o jogador — é recusar a fraqueza que o jogo explora. 'Agora te peguei': não forneça a falta esperada. 'Sim, mas': pare de dar conselhos. Atacar o jogador só realimenta o payoff.",
    "tip": "<strong>Como aplicar:</strong> antítese &gt; confronto — recuse o lance específico, mantenha-se no Adulto, e ofereça carícias por vias saudáveis."
   }
  ]
 },
 "ch05-jogos-da-vida": {
  "cards": [
   {
    "ic": "fork",
    "t": "'Se Não Fosse Por Você'",
    "b": "O jogador culpa o parceiro por aquilo que, no fundo, <strong>teme fazer</strong>. Social: 'você me impede de X'. Psicológico: 'eu não quero arriscar, e ainda colho a vantagem de te culpar'. Payoff: confirma 'eu poderia, se não fosse você' sem nunca se expor. A proibição alheia vira álibi.",
    "tip": "<strong>Modelo mental:</strong> quando alguém repete 'eu faria X se não fosse Y', suspeite do INFPV — o Y pode ser um álibi conveniente para evitar o risco real."
   },
   {
    "ic": "masks",
    "t": "'Olha o Que Você Me Fez Fazer'",
    "b": "Ao errar, o jogador <strong>transfere a responsabilidade</strong> para quem o 'interrompeu' ou aconselhou. Função: defender-se de qualquer culpa e manter os outros à distância ('não me perturbem'). O payoff é o ego protegido; o custo, o isolamento crescente.",
    "tip": "<strong>Sinal de alerta:</strong> quando um erro é seguido de 'olha o que você me fez fazer', não aceite a culpa — você está sendo recrutado para o jogo."
   },
   {
    "ic": "wave",
    "t": "'Esquentadinho' (Uproar)",
    "b": "Troca de hostilidades crescentes que termina com os dois em quartos separados — mas o objetivo <strong>não é resolver o conflito</strong>: é evitar a intimidade (especialmente a sexual) sob aparência de briga. A briga é o meio, não o fim. Brigas que sempre estouram na hora da aproximação = Esquentadinho.",
    "tip": "<strong>Como aplicar:</strong> reconheça o padrão (aproximação → briga → separação) e nomeie-o em voz alta — nomear o jogo costuma ser o primeiro passo da antítese."
   }
  ]
 },
 "ch06-jogos-conjugais-sociais": {
  "cards": [
   {
    "ic": "scale",
    "t": "'Tribunal' — Quem Está Certo?",
    "b": "O casal (ou grupo) arrasta a disputa para diante de um <strong>terceiro como juiz</strong>. A pergunta é 'quem está certo?', não 'como resolvemos?'. Antítese: o terceiro recusa o papel de juiz e devolve a responsabilidade ao casal. O jogo perde o árbitro e desmorona.",
    "tip": "<strong>Regra:</strong> quando convidado a arbitrar entre duas pessoas, pergunte 'o que cada um precisa do outro nessa situação?' — em vez de dar o veredicto."
   },
   {
    "ic": "bubble",
    "t": "'Por Que Você Não — Sim, Mas'",
    "b": "Alguém apresenta um problema; os outros oferecem soluções; o iniciador rejeita todas com 'sim, mas...'. O objetivo nunca foi resolver — é provar que <strong>nenhum Pai consegue ajudar</strong>. Payoff: 'ninguém me entende'; os conselheiros ficam frustrados. <strong>Antítese</strong>: não dar conselho — devolver a pergunta.",
    "tip": "<strong>Como aplicar:</strong> recebeu um problema e todas as sugestões foram rejeitadas com 'sim, mas'? Pare. Diga: 'realmente difícil. O que você pretende fazer a respeito?'"
   },
   {
    "ic": "eye",
    "t": "'Encurralado' e 'Defeito'",
    "b": "<strong>Encurralado</strong>: qualquer resposta do parceiro está errada (faça = criticado; não faça = criticado) — duplo vínculo permanente. <strong>Defeito</strong>: o jogador varre o ambiente em busca de uma falha no outro para se sentir superior ('reparou na gravata dele?'). Origem na Criança insegura que precisa rebaixar para subir.",
    "tip": "<strong>Modelo mental:</strong> toda resposta sua é punida = você está Encurralado. Nomeie o duplo vínculo em voz alta — isso quebra o encantamento do jogo."
   }
  ]
 },
 "ch07-jogos-do-submundo": {
  "cards": [
   {
    "ic": "triangle",
    "t": "'Chuta-me' — Autopunição",
    "b": "A pessoa age de modo a <strong>provocar rejeição e punição</strong>, confirmando 'sempre sou rejeitado'. Fórmula J: isca (comportamento provocador) + fraqueza (tendência do outro a punir) → resposta → virada (o outro 'chuta') → confusão → recompensa (posição de vida confirmada). Variante de 3º grau: 'Espancado' — atrai abuso real.",
    "tip": "<strong>Sinal de alerta:</strong> 'azar crônico' que se repete nos mesmos contextos pode ser 'Chuta-me' buscando a punição que confirma o roteiro. Não morda a isca — punir fecha o ciclo."
   },
   {
    "ic": "sword",
    "t": "'Agora Te Peguei' (NIGYSOB)",
    "b": "O jogador <strong>coleciona pequenas ofensas</strong> em silêncio e espera o outro cometer um erro mínimo para descarregar fúria desproporcional 'justificada'. O erro real é só o gatilho esperado — o verdadeiro objetivo é a explosão acumulada. Payoff: descarga de raiva 'com razão' + confirmação de 'não se pode confiar em ninguém'.",
    "tip": "<strong>Como aplicar:</strong> quem coleciona e explora após longa paciência está jogando NIGYSOB. Não forneça o erro esperado — e nomeie o padrão se puder."
   },
   {
    "ic": "mask",
    "t": "'Pata-de-Pau' — O Álibi Vitalício",
    "b": "O jogador usa uma desvantagem real ou alegada como <strong>isenção permanente</strong>: 'o que se pode esperar de alguém com a minha criação?' Troca mudança por pena. A antítese não é negar a dificuldade — é recusar a isenção permanente e devolver a responsabilidade possível.",
    "tip": "<strong>Modelo mental:</strong> a 'pata-de-pau' pode ser real E usada como jogo simultaneamente. Compadeça-se da dificuldade; não conceda a licença de nunca mudar."
   }
  ]
 },
 "ch08-alem-dos-jogos-autonomia": {
  "cards": [
   {
    "ic": "spiral",
    "t": "O Roteiro de Vida",
    "b": "Um plano de vida <strong>inconsciente</strong>, formado na primeira infância sob influência dos pais, que dita o desfecho ('como minha história termina'). Os jogos são as cenas repetidas que mantêm o roteiro em curso. A posição de vida ('eu sempre acabo só') é o que o roteiro sustenta.",
    "tip": "<strong>Pergunta libertadora:</strong> 'que desfecho este jogo está me ajudando a confirmar — e eu ainda quero esse final?' Tornar o padrão consciente é o primeiro passo."
   },
   {
    "ic": "key",
    "t": "As Quatro Posições de Vida",
    "b": "Convicções básicas sobre si e o outro que o roteiro sustenta — formalizadas como: <strong>Eu OK/Não-OK × Você OK/Não-OK</strong>. A posição saudável e a meta é <strong>Eu OK – Você OK</strong>: a base da intimidade real e da cooperação genuína.",
    "tip": "<strong>Modelo mental:</strong> troque de jogo mantendo a posição 'Não-OK' e você muda de cena mas não de roteiro. A mudança real exige a posição existencial, não só o comportamento."
   },
   {
    "ic": "constellation",
    "t": "Autonomia: A Meta",
    "b": "A liberação dos jogos e do roteiro, por três capacidades: <strong>(1) Consciência</strong> — perceber o aqui-e-agora sem o filtro do Pai; <strong>(2) Espontaneidade</strong> — escolher livremente entre P, A e C; <strong>(3) Intimidade</strong> — relação franca, sem jogos nem exploração. É o oposto da deriva do roteiro.",
    "tip": "<strong>Regra:</strong> autonomia não é eliminar P e C — é recuperar a Criança Livre e a consciência adulta para escolher qual estado usar em cada momento."
   }
  ]
 },
 "ch09-intimidade-saida": {
  "cards": [
   {
    "ic": "leaf",
    "t": "Intimidade: Risco e Recompensa",
    "b": "A intimidade oferece o máximo de carícias autênticas — e também o maior grau de <strong>exposição e vulnerabilidade</strong>. Por isso é rara: os jogos existem exatamente porque garantem carícias sem o risco da intimidade real. Escolher a intimidade é escolher o risco de ser visto.",
    "tip": "<strong>Modelo mental:</strong> a intimidade é o destino que todos os capítulos anteriores prepararam. É o que os jogos bloqueiam — e o que a autonomia torna possível."
   },
   {
    "ic": "target",
    "t": "Como Sair de um Jogo",
    "b": "Quatro caminhos: <strong>(1)</strong> não morder a isca — recusar a fraqueza que o jogo explora; <strong>(2)</strong> responder pelo Adulto quando o convite é ulterior; <strong>(3)</strong> recusar a recompensa — não colher o sentimento ruim familiar; <strong>(4)</strong> oferecer/buscar carícias por vias saudáveis. A antítese é sempre específica para cada jogo.",
    "tip": "<strong>Como aplicar:</strong> identifique qual dos 4 caminhos é aplicável ao jogo que você está dentro — e tente o mais simples primeiro."
   },
   {
    "ic": "person",
    "t": "A Posição 'Eu OK – Você OK'",
    "b": "A base da saída definitiva dos jogos é a convicção de que <strong>eu tenho valor e você tem valor</strong> — sem precisar de payoffs que confirmem superioridade, inferioridade ou vitimização. É a posição existencial que torna a intimidade possível e os jogos desnecessários.",
    "tip": "<strong>Regra:</strong> mudar a posição de vida exige mais que intenção — exige experiências repetidas de interação autêntica que reescrevam a convicção básica."
   }
  ]
 }
}
```
