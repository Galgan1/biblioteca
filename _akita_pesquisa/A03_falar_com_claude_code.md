# A03 — Como falar com o Claude Code efetivamente (e por que as LLMs "não dão o resultado esperado")

**Fonte:** https://akitaonrails.com/2026/04/15/como-falar-com-o-claude-code-efetivamente/
**Publicado:** 15 de abril de 2026
**Autor:** Fábio Akita (akitaonrails.com)

> Nota de rastreabilidade (R1): tudo abaixo vem do post acima. Citações literais entre aspas.
> Nada foi inventado; onde o post não detalha, está marcado como "não detalhado na fonte".

---

## Práticas concretas

### 1. Estruturar todo pedido em 4 blocos
Akita modela o prompt como **Objetivo · Método · Restrições · Validação**:
- **Objetivo** — o resultado final desejado, claro.
- **Método** — "o jeito que eu quero que seja feito, em linhas gerais".
- **Restrições** — "o que eu não quero" (carrega os pressupostos não-verbalizados).
- **Validação** — "como a gente valida que deu certo".
Ele frisa que **não é template/formalismo**: "só como eu converso com qualquer pessoa que precisa entregar algo pra mim".

### 2. Tratar prompt como conversa iterativa, não one-shot
Os prompts são **iterativos**, não únicos: durante a execução ele segue mandando correção, contexto extra e ajuste em tempo real (modelo Mark I → II → III…, até "Mark LXXXV").

### 3. Planejar antes de codar em etapas separadas e idempotentes
Para tarefa complexa, decompõe em passos **idempotentes**:
- cria diretórios de doc (`docs/`, `docs/scripts/`);
- numera scripts em sequência (`01_walk_and_hash.py`, `02_classify.py`);
- mantém **estado de progresso em SQLite** (não na memória do chat);
- usa **gates humanos** entre fases críticas (ex.: arquivo-flag `docs/.phase4-approved`).
Caso real citado: consolidação de ROMs — 12 TB, ~400 mil arquivos.

### 4. Despejar o conhecimento de domínio que só existe na sua cabeça
Ele entrega ativamente: conhecimento de domínio ("Romset de Neo Geo depende do emulador que vai consumir"), restrições técnicas (Synology/NFS, 10GbE pro NAS), decisões de engenharia prévias (dedupe por **SHA1+tamanho**, não por nome) e o histórico do que "já deu errado". Justificativa: "Esse conhecimento está na minha cabeça e não no código. Se eu não der, ele vai assumir o default mais razoável dele, que pode ser o oposto do que eu preciso."

### 5. Ficar na sala: pair programming contínuo durante a execução
"Eu não saio da sala." Ele monitora ETA/gargalos e intervém em tempo real: pede paralelização ("acho que dá pra paralelizar, tenho CPU sobrando"), injeta contexto esquecido ("Ah, esqueci de te falar que também é importante abordar X") e corrige erro factual ("Não, essa referência aqui está desatualizada"). Ele chama isso de **Agile Vibe Coding**: aplicar técnicas de **XP** (pair programming, test-driven, feedback curto, refactor contínuo) ao prompting.

### 6. Usar o harness (não só o modelo) a seu favor
Por que **Claude Code**, na visão dele — é questão de **harness**, não de modelo:
- **planejamento visível**: mantém a to-do list na tela e quebra a tarefa longa em subtarefas — "Quando ele me diz 'terminei', eu sei que a lista inteira foi executada, porque está bem ali pra eu conferir";
- **execução paralela**: ao interromper com `ESC`, mantém a 1ª tarefa rodando enquanto começa a 2ª (contraste com o Codex, que ele descreve como serial — para a 1ª ao receber nova solicitação).
Ressalva de modelo: "Claude Opus e GPT-5.4 xHigh, pra mim, estão empatadíssimos como modelos."

### 7. Investir esforço no pedido (a regra-mãe)
"A qualidade do que te entregam é diretamente proporcional ao esforço que você colocou em pedir."

---

## Anti-padrões (o que ele diz para NÃO fazer)

- **Achar que o contexto da sua cabeça já está no modelo** — assumir que o pressuposto óbvio pra você é óbvio pra ele.
- **Pedido genérico esperando resultado específico** — "pediu pouco, esperou muito. E quando o resultado veio abaixo, culpou a ferramenta. Nunca a própria pergunta."
- **Omitir as restrições / o "o que eu não quero"** — é onde moram os pressupostos não-verbalizados.
- **Não definir métrica de sucesso** (pular o bloco de Validação).
- **Manter estado de progresso na memória do chat** em vez de externo (SQLite/flags).
- **Esperar o "mágico"** em vez do "terceirizado": "Mágico resolve sem você dizer nada. Terceirizado resolve exatamente o que você pediu, do jeito que você pediu, com as informações que você deu." A LLM é terceirizado.
- **One-shot prompt** como expectativa (nem o Stark acerta a armadura de primeira — 85 iterações / Mark LXXXV).
- Diagnóstico-raiz de por que "as LLMs não dão o resultado esperado": **"Ninguém sabe se comunicar."**

---

## Termos / jargões exatos

- **Agile Vibe Coding** — XP aplicado ao prompting (pair programming, test-driven, feedback curto, refactor contínuo).
- **Spec Driven Development** — citado e criticado por ele como "tratamento de sintoma".
- **Harness** — a infraestrutura/interface (Claude Code, Codex), distinta do modelo.
- **Idempotente** — propriedade exigida dos scripts/etapas.
- **Gates humanos** — pontos de aprovação manual entre fases (ex.: `docs/.phase4-approved`).
- **Default mais razoável** — o que o modelo assume quando você não dá contexto.
- **Mágico vs. Terceirizado** — metáfora do que a LLM é (terceirizado).
- **Stark + Jarvis = Homem de Ferro** — IA executa, humano pensa; **Mark LXXXV** = iteração contínua.
- **42** — a resposta certa pra pergunta errada (Douglas Adams).
- **ESC** — interromper o Claude Code mantendo a tarefa anterior rodando (paralelismo).
- Modelos citados: **Claude Opus**, **GPT-5.4 xHigh** ("empatadíssimos"); harness comparado: **Codex**.

---

## Aplicação (1–2 linhas)
Adotar o gabarito **Objetivo · Método · Restrições · Validação** como forma padrão de prompt no `/akita` e no `/loop-agente` (a "Validação" vira a rúbrica), e exigir estado de progresso externo + gates humanos idempotentes nas tarefas longas — em vez de confiar na memória do chat ou no one-shot.
