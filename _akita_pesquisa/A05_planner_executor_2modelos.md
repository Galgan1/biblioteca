# A05 — Planner + Executor (misturar 2 modelos) / Benchmarks múltiplos modelos

**Fonte(s):**
- https://akitaonrails.com/2026/04/25/llm-benchmarks-vale-a-pena-misturar-2-modelos/
- https://akitaonrails.com/2026/04/18/llm-benchmarks-parte-2-multiplos-modelos/

**Publicado:** 2026-04-18 (Parte 2) e 2026-04-25 (Parte 3 / "vale a pena misturar 2 modelos")

> Veredito central do Akita: **NÃO compensa** misturar "modelo forte planejador + modelo barato executor" no dia a dia. *"Em todas as três rodadas de experimentos que rodei, mistura de 'modelo forte planejador + modelo barato executor' perde pra simplesmente usar Opus 4.7 sozinho."* Recomendação: *"Pra 90% do trabalho de programação do dia a dia, minha recomendação continua: Claude Code + Opus."*

---

## Práticas concretas

1. **O padrão tem nome: `Planner + Executor`** (jargão dele) — um **frontier model** forte planeja a arquitetura/escopo/limites; um modelo mais barato escreve as linhas. Configurado por harness:
   - **Claude Code:** Opus 4.7 (primary) → Sonnet 4.6 / Haiku 4.5 como **sub-agentes** via `.claude/agents/*.md` (usa o **Task tool**).
   - **opencode:** Opus 4.7 → GLM 5.1 ou Qwen 3.6 local (config em JSON).
   - **Codex CLI:** GPT 5.4 xHigh → GPT 5.4 medium/low (agents em TOML).

2. **Quem decide os limites é o que importa, não quem digita.** *"Qwen escreveu as linhas, Opus decidiu os limites, e os limites são a maior parte do que tira isso de B pra A."* / *"Kimi escreveu cada linha, mas as instruções de plano do Opus moldaram o que pedir."* → O valor do planner está em **decision boundaries** e validações, não no volume de código.

3. **Mistura só se paga em 3 exceções estreitas:**
   - **(a) Pipeline amortizada / multi-tenant:** *"se você tá rodando uma pipeline que aplica o mesmo padrão de mudança em muitos projetos similares"* (ex.: refatorar 50 repos, traduzir 700+ posts do blog — tarefas **genuinamente paralelas e desacopladas**). Aí *"Opus orquestrando + Sonnet executando a tradução de cada arquivo teria cortado o custo pela metade."*
   - **(b) Preso ao ecossistema OpenAI:** GPT 5.4 xHigh planner + GPT 5.4 medium executor cai de ~$16 para $1–3 (−80~85%) perdendo só ~3 pontos (97→94).
   - **(c) Quota Anthropic saturada:** Opus planner + Kimi K2.6 executor entrega 95/100 vs 97/100 do Opus solo — troca qualidade por acessibilidade de quota.

4. **Números do custo/benefício (pay-as-you-go):** Opus 4.7 solo = 97/100, ~18 min, ~$4 (baseline). Opus+Kimi **manual** (cross-process) empata em qualidade (97) mas custa ~3× e +22 min → *"Manual orchestration custa 3× mais que solo."* Opus+Kimi **in-process** = 95/100. Em **assinatura mensal**: *"nenhuma configuração multi-agente bate o solo do frontier model. O custo marginal de uma chamada extra é zero."*

5. **Harness importa para custo:** Claude Code custa **5–7×** mais por run que opencode no MESMO modelo, por overhead de cache (6–11M tokens vs ~210K). *"Claude Code custa 5 a 7 vezes mais por run no mesmo modelo."*

## Anti-padrões

- **Multi-agente como default = otimização prematura.** *"Multi-agente em coding agent contínuo é otimização prematura disfarçada."*
- **Achar que delegar acontece sozinho:** *"Em 7 runs, a ferramenta de delegação foi chamada zero vezes."* Nenhum modelo invocou o sub-agente espontaneamente. Em greenfield Rails (código cross-file, acoplado) a delegação isolada não cola; *"Delegação tem custo de coordenação"* — corrigir o plano após erro de execução custa mais que rodar um modelo só.
- **Otimizar orquestração em vez do prompt:** ele recomenda o inverso — *"otimiza prompt em vez de orquestração"*, usando um harness maduro (cita opencode como "o que mais respeita o modelo").

## Termos

`Planner + Executor` · `frontier model` (Opus 4.7, GPT 5.4 xHigh) · `sub-agente` / `Task tool` (Claude Code) · `harness` (Claude Code, opencode, Codex) · `vibe coding` · `greenfield Rails` · `pay-as-you-go` · `Tier A/B/C/D` (escala 0–100) · `orchestration overhead` / "custo de coordenação" · `DNF` (Did Not Finish) · `fallback agent`.
**Modelos citados:** Claude Opus 4.7/4.6, Sonnet 4.6, Haiku 4.5; GPT 5.4 (xHigh/medium/low), GPT 5.5; Kimi K2.6; Qwen 3.6 (Plus / local); GLM 5.1; DeepSeek V4 Pro (incompatível com ai-sdk multi-turn → sem conclusão).

## Aplicação (1–2 linhas)

Confirma o pilar 2 do nosso método: usar Planner→Executor cross-model com parcimônia. **Diferença crítica vs. nosso padrão:** Akita testou Planner→Executor *unidirecional* e **não usa um modelo-juiz/reviewer** (*"Akita não implementou modelo 'judge' ou 'reviewer'"* / *"não descreve cross-model judge/reviewer"*) — nosso `Verifier cross-model` (juiz ≠ autor, Opus↔Sonnet) é um acréscimo nosso, não dele. Doutrina prática: solo Opus para o dia a dia; reservar a mistura para lotes paralelos desacoplados (ex.: gerar peças/traduzir N livros) ou quota saturada.
