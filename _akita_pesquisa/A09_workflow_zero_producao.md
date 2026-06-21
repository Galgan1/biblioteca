# A09 — Workflow real: do zero à produção (Vibe Code / FrankMD)

**Fonte(s):**
1. https://akitaonrails.com/2026/02/16/vibe-code-do-zero-a-producao-em-6-dias-the-m-akita-chronicles/ (projeto "M.", 6 dias, do zero à produção)
2. https://akitaonrails.com/2026/02/01/vibe-code-fiz-um-editor-de-markdown-do-zero-com-claude-code-frankmd-part-1/ (FrankMD parte 1 — definição do problema e stack)
3. https://akitaonrails.com/2026/02/01/vibe-code-fiz-um-editor-de-markdown-do-zero-com-claude-code-frankmd-parte-2/ (FrankMD parte 2 — diário ponta a ponta)

**Publicado:** 01/02/2026 (FrankMD, partes 1 e 2) e 16/02/2026 (M. Chronicles).

> Os dois casos descrevem o MESMO método em escalas diferentes: FrankMD = 1 app web (~30h em 3 dias, 137 PRs); M. = sistema multi-componente (6 dias, ~200 commits). Onde números divergem, ambos estão anotados.

---

## Sequência de passos (workflow)

Sequência ponta a ponta, destilada dos dois diários:

1. **Definir a dor antes de codar.** Ele parte de um problema concreto e pessoal (FrankMD nasce do incômodo com Obsidian/LazyVim para escrever posts; M. de uma necessidade de pipeline). A ideia é conceituada num **documento público** (M.) antes de qualquer linha.
2. **Decisões técnicas mínimas (stack upfront).** Escolhe a stack rápido e a justifica: FrankMD = **Ruby on Rails 8 + Tailwind**, filesystem (sem banco), sem autenticação — "para refrescar a skill". Critério declarado: *"este editor deve ter apenas as funcionalidades SUFICIENTES"* (rejeita feature creep).
3. **FASE 1 — Prototipagem rápida.** Vai até "**já funciona**" o mais rápido possível. FrankMD: ~**1,5h / 10 commits** = editor mínimo funcional com tema dark e preview. M.: dias 1–2 = features core até ponto funcional (~50 commits).
4. **FASE 2 — Acúmulo de features.** Empilha funcionalidades em sequência priorizada (FrankMD: cheat-sheet → code blocks → temas → fontes → zoom → typewriter → fuzzy finder → search/regex → YouTube embed → upload de imagem → Docker). ~**4h / 34 commits**. Aqui o "já funciona" vira armadilha: tudo se acumula num arquivo só.
5. **FASE 3+ — Refactor contínuo (gatilho = dor / arquivo gigante).** Quando um arquivo incha (CSS de 1.000+ linhas; JS de 4–5 mil linhas num único arquivo) ele dispara um **grande refactor**: "Refactor to RESTful Architecture", quebra do `application.css` monolítico, mega-refactor de JS em múltiplos controllers. Refatora "**componentes inteiros quando os testes indicam necessidade**".
6. **Testes acompanham cada funcionalidade (TDD real).** Regra: *"toda funcionalidade deve vir acompanhada de testes unitários. Toda correção de bug precisa de testes de regressão."* Pequenas funcionalidades → abstração correta → **teste imediato**. Cobertura final: ~70% (FrankMD), 100% / 1:1 (M.).
7. **Pequenos commits descritivos + branch master só com verde.** Claude separa tarefas em **múltiplos commits** com descrições precisas; a `master` só recebe commits com **testes aprovados** (em M., critério de "**150 PRs aprovados**", não "já funciona"). Permite **reversão segura em qualquer ponto**.
8. **Code review / QC humano recorrente.** Ao longo do projeto checa explicitamente: **memory leaks** (2–3x), buracos de segurança óbvios, e **dead code** pós-refatoração. Em M.: múltiplas revisões de segurança com **Claude Code E Codex** (não confia em revisão única).
9. **Interromper quando o agente desvia.** Quando Claude muda paradigma sem avisar (ex.: trocar lógica server-side ↔ client-side), ele corta com *"ow, por que?"*. Assistência humana constante — "batendo o olho".
10. **Não reinventar a roda.** Quando bate num inferno de edge cases (o "Syntax Highlight Hell", 3h+ de brigas), decide *"Chega. Estou reinventando a roda."* e troca por biblioteca consagrada (**CodeMirror**, ~6.000 linhas trocadas). Frase: *"Grandes refactorings, especialmente se você preparou uma boa suíte de testes automatizados, vão bastante bem com LLMs."*
11. **Performance é pedida, não automática.** Só depois de funcionar pede otimização. Bugs achados: `setTimeout` sem `clearTimeout`, auto-save a cada tecla, preview atualizando fechado. Frase: *"LLMs não vão fazer o código mais performático logo de cara; você precisa pedir como!"*
12. **Deploy em produção + validação ponta a ponta.** Em M.: deploy na **sexta-feira** (dias 3–5), depois dias 6–7 = primeira execução completa real (newsletter, blog, podcast, upload Spotify, e-mails). Segurança de produção: Cloudflare, AES-256, zero tracking, LGPD. FrankMD: modo duplo — wrapper CLI (`fed .`) para diretório local + opção self-hosted via Docker.

**Distribuição de tempo (FrankMD, ~30h / 3 dias):** 1,5h protótipo → 4h features (fim do dia 1) → ~8h refactor grande (entra no dia 2) → ~15h de pausa (febre/repouso) → 14h finais (dia 3: CodeMirror, bugs, performance) → versão ~1.0 no domingo. **(M.):** dia 1–2 planejar/prototipar, dia 3–5 testar/refatorar/segurança/deploy, dia 6–7 validar em produção.

---

## Práticas concretas

- **Pair programming com o agente:** *"trate o Claude Code como um programador esforçado que comete erros"*; o humano assume os papéis de **gerente, Tech Lead e QA**.
- **TDD rigoroso:** feature ⇒ teste unitário; bugfix ⇒ teste de regressão. Verde de teste é o critério de pronto, não "a IA achou que funciona".
- **CI/CD com gate:** `master` só com commits/PRs aprovados (testes verdes); reversão segura em qualquer ponto.
- **Small commits, mensagens precisas:** *"pelo menos uma coisa que as LLMs fazem bem é documentar o histórico do que foi modificado naquele commit"* — ele recomenda **ler os commits** para entender o projeto.
- **Refatoração contínua disparada por sintoma** (arquivo de 1.000+/4.000+ linhas, "estagiário", "castelo de cartas"): consolidar domínios, RESTful, quebrar monólitos de CSS/JS.
- **Suíte de testes habilita refactor grande com LLM** (a citação do passo 10).
- **QC humano periódico:** caçar memory leaks, dead code e falhas de segurança.
- **Múltiplos revisores de IA** para segurança (Claude Code + Codex).
- **i18n com LLM:** extrair strings → traduzir; *"LLMs brilham"* em linguagem natural, superior ao Google Tradutor.
- **Convenções upfront:** insight de que deveria ter criado um `CLAUDE.MD` / `CONTRIBUTING.MD` com convenções de código **antes** de começar.
- **Bisect assistido:** Claude oferece testar **commit-por-commit** (equivalente manual ao `git bisect`) para localizar a introdução de um bug.

## Anti-padrões (o que ele evita / critica)

- **"Já funciona" como critério de pronto** → acumula tudo num arquivo único, vira "castelo de cartas".
- **Pular a fase de testes.**
- **`git add .` indiscriminado** (em vez de commits separados e descritos).
- **Confiar em revisão única de segurança.**
- **Deixar o agente rodar solo sem verificação humana** → "funciona" mas com arquivos gigantes, sem testes, código desastroso.
- **Reinventar a roda** quando já existe biblioteca madura (CodeMirror).
- **Não comunicar mudança de paradigma:** o agente troca server↔client sem avisar — tem que ser interrompido.
- **Esperar performance "de graça"** sem pedir.
- **Tracking/cookies desnecessários** (M.).
- **Rebranding cedo demais** (FrankMD só renomeou "WebNotes"→"FrankMD" depois de maduro).
- **Comprimir 30h em 3 dias:** ele mesmo diz que o correto seriam **~5 dias**.
- **O "jeito podre que todo vibe coder amador faz"** (a antítese explícita do método).

## Termos / jargões (exatos)

- **Vibe Code / Vibe Coding** — desenvolvimento assistido por IA.
- **Senior Agile Vibe Coder** — a metodologia "que realmente funciona" (oposta ao amador).
- **Developer 10x** — *"finalmente sinto que chegamos ao elusivo Developer 10x. Basta que você seja sênior primeiro."*
- **Extreme Programming (XP)** — framework que garante qualidade com IA.
- **Spec Driven Development** — citado como "menos importante que a qualidade da descrição".
- **User Stories** — formato irrelevante; o conteúdo é tudo.
- **Pair programming**; papéis **gerente / Tech Lead / QA**.
- **TDD**, **testes de regressão**, **edge cases**, **dead code** (código morto), **memory leaks** / leaks de memória.
- **Refactor** / "Refactor to RESTful Architecture", **RESTful resources**, **HTTP verbs (PATCH/DELETE)**.
- **I18n** (internacionalização).
- **CodeMirror** (biblioteca que substituiu o textarea custom).
- **git bisect** (manual / assistido), **small commits**, **branch master**.
- **"já funciona"**, **"castelo de cartas"**, **"estagiário"** (qualidade do 1º jato do agente), **"lag"**.
- **6 a 7 vezes mais rápido** (vs. ~200h solo estimadas).
- Métricas: **Tokei** (contagem de linhas), **137 PRs / 130+ commits / ~18 mil → 33 mil linhas / ~70% cobertura** (FrankMD); **~200 commits, 150 PRs aprovados, 100% cobertura** (M.).

## Aplicação (1–2 linhas)

No nosso projeto: prototipar até "já funciona" é só a Fase 1 — o pronto exige **teste verde + refactor de monólito + QC humano (leaks/segurança/dead code)** antes de produção; e refactor grande só é seguro com **suíte de testes** já no lugar. Reforça a constituição (TDD real, small commits, GitGuy como único a commitar) e justifica criar convenções `CLAUDE.MD` upfront em cada lane.
