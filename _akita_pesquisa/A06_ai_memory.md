# A06 — ai-memory: memória de longo prazo para agentes de código (Akita)

**Fonte(s):**
- https://akitaonrails.com/2026/05/23/criei-sistema-memoria-agentes-codigo-ai-memory/ (origem / arquitetura do `ai-memory`)
- https://akitaonrails.com/2026/06/14/ai-memory-arquitetura-emergente-e-software-maleavel/ (filosofia de design: arquitetura emergente / software maleável)
- https://akitaonrails.com/2026/06/16/ai-memory-memoria-longo-prazo-karpathy-wiki-auto-aprendizado-hermes-projetos/ (Karpathy LLM Wiki + auto-aprendizado Hermes + projetos)

**Publicado:** 23/05/2026, 14/06/2026 e 16/06/2026 (três posts da série `ai-memory`).

---

## Práticas concretas

**Source of truth = markdown puro no disco.**
- *"Markdown puro no disco como source of truth. SQLite é só índice derivado."* O SQLite é reconstruível a partir do markdown — ele não guarda a verdade, só indexa.
- Motivação declarada vem de Karpathy: um `index.md` simples é *"surpreendentemente bom — em ~100 fontes e algumas centenas de páginas, sem precisar de embeddings"*. Embeddings ficam **desligados por padrão**.

**Estrutura física de pastas** (isolamento por UUID, sem colisão de nomes):
- Raiz: `<wiki_root>/<workspace_id>/<project_id>/...`
- Marcador de escopo do projeto: `.ai-memory.toml`
- Páginas agrupadas por tipo de conhecimento:
  - `concepts/` — conhecimento durável
  - `decisions/` — escolhas de arquitetura
  - `gotchas/` — armadilhas/problemas conhecidos
  - `procedures/` — procedimentos
  - `_rules/` — regras de roteamento do projeto (alimentam `CLAUDE.md` / `AGENTS.md`)
  - `sessions/<id>.md` — log bruto por sessão (narrativa preservada)
  - `bootstrap.md` — manifesto da semeadura inicial
  - `_meta.md` — manifestos auto-descritivos
- Doutrina de página: *"páginas pequenas, com nomes estáveis, separadas por tipo de conhecimento"*.
- Classificação por campo `kind`: `decision`, `gotcha`, `rule`, `fact`.

**Camadas de memória (consolidação tipo sono)** — quatro tiers inspirados em `agentmemory`:
1. **Working** — observações brutas da sessão
2. **Episodic** — resumos de sessão
3. **Semantic** — páginas de wiki consolidadas
4. **Procedural** — regras e padrões do projeto
- *"consolidação tipo sono: memória curta retém detalhes brutos, memória longa vai consolidando."*

**Captura via hooks (fire-and-forget, fora do caminho quente):**
- Agente dispara HTTP POST para `127.0.0.1:49374` nos eventos: `SessionStart`, `UserPromptSubmit`, `PreToolUse`, `PostToolUse`, `PreCompact`, `Stop`, `SessionEnd`.
- *"O agente nunca espera. Se o ai-memory tiver fora do ar, a sessão continua normal."* Hooks respondem `202`/`429` e saem da frente.
- Hooks cobrem múltiplos CLIs: Claude Code, Cursor, Gemini CLI, Codex, OpenCode, Antigravity CLI, Grok Build CLI, VS Code GitHub Copilot, Claude Desktop.

**Recuperação/uso via MCP** (o agente chama ferramentas):
- `memory_query` — busca FTS5 + vizinhança de links (RRF) + re-rank vetorial opcional
- `memory_explore` — digest em prosa; verbosidade escala com tempo de inatividade
- `memory_handoff_begin` — escreve handoff estruturado com `open_questions` + `next_steps`
- `memory_consolidate` — gatilho manual de consolidação
- `memory_lint` — detecta páginas obsoletas e contradições

**Passagem de bastão (handoff) entre agentes diferentes:**
- No `SessionEnd` cria handoff tipado marcado `pending`; no `SessionStart` seguinte, se há handoff `pending`, ele é injetado no contexto.
- Exemplo do autor: *"No `SessionEnd` do Claude Code, o ai-memory consolidou... no `SessionStart` do Codex, o servidor viu o handoff pending, recuperou e injetou."* Benefício: *"você não precisa recontar a novela"*.

**Consolidação (compilação em background):**
- LLM transforma observações brutas em páginas de wiki. Modelo recomendado: **Claude Haiku 4.5** (~US$0,02/run, ~7s), escolhido pela **restrição** (não inventa página de sessão trivial) e boa classificação. Alternativa local grátis: `qwen3:32b` (~92s, aceitável por ser background).
- Bootstrap de projeto existente: `ai-memory bootstrap` semeia a wiki lendo `git log`, README, `docs/`, headers de módulos e regras do projeto (custo ~US$0,05 com Haiku).

**Auto-aprendizado = Hermes adaptado (job de fundo, fora do caminho quente):**
1. Revisa sessões concluídas elegíveis.
2. Procura decisões, gotchas, procedimentos, regras.
3. LLM sugere → sistema **valida**: evidência, caminho válido, tamanho, confiança mínima.
4. Registra **trilha de auditoria**.
5. Escreve pela trilha normal da wiki.
- Aprovação manual opcional via `[auto_improve] require_approval = true`.
- Filtro: *"nem tudo que acontece numa sessão merece virar memória permanente"* — rejeita ruído transitório, erro ambiental, narrativa já preservada.

**Decay e manutenção (sem intervenção do usuário):**
- Supersessão por `is_latest=false` (nunca delete → mantém trilha de auditoria / supersession chains).
- Decaimento geométrico exponencial + reforço por repetição espaçada (inspirado em consolidação por sono).
- Comandos: `ai-memory forget-sweep`, `ai-memory lint`, `ai-memory embed`, além de `upgrade`, `bootstrap`, `purge-project`, `rename-project`, `backup/restore`, `generate-auth-token`.

**Filosofia (arquitetura emergente / software maleável):**
- Ordem: *"Make it work, make it right, make it fast"* — *"A abstração veio depois do uso, não antes."*
- Software como argila *"sempre úmido"*, cultivado continuamente; MVP de 1 usuário/1 máquina/1 SO primeiro, refator depois (ex.: `ScopeResolver` de 601 linhas só após multi-usuário em produção).

---

## Anti-padrões

- **Escrita automática sem validação** → produz *"cemitério de superstição"*.
- **Memória opaca com embeddings** → impossível versionar, auditar ou ler (por isso markdown + embeddings off por padrão).
- **Integração no caminho quente** → trava a sessão; hooks têm que sair da frente (202/429).
- **Confiança cega no LLM** → trilha de auditoria é obrigatória.
- **Contexto bruto infinito** → trocar por síntese seletiva em páginas pequenas.
- **Desenhar toda a arquitetura antes de o código funcionar** / criar permissões antes de ter usuários / cristalizar estruturas "que podem ser úteis" / reescrever do zero para encaixar estrutura pré-concebida.
- Bugs herdados do antecessor `agentmemory` (lições): reindex BM25 a cada restart e corrupção >10K observações; debounce de 5s perdendo dados em crash de 30s; configs duplicadas (`process.env` vs `getMergedEnv()`); hook lendo campo errado (`tool_output` vs `tool_response`) — perda silenciosa por 6 semanas; engine rodando do CWD do chamador (Windows perdia histórico).

---

## Termos (jargão exato)

`ai-memory` · `Karpathy LLM Wiki` · `index.md` · `Hermes` (loop de auto-aprendizado) · "source of truth markdown / SQLite índice derivado" · tiers `Working`/`Episodic`/`Semantic`/`Procedural` · `kind` (`decision`/`gotcha`/`rule`/`fact`) · `concepts/` `decisions/` `gotchas/` `procedures/` `_rules/` `sessions/<id>.md` `bootstrap.md` `_meta.md` · `.ai-memory.toml` · `<wiki_root>/<workspace_id>/<project_id>` · hooks `SessionStart`/`UserPromptSubmit`/`PreToolUse`/`PostToolUse`/`PreCompact`/`Stop`/`SessionEnd` · porta `127.0.0.1:49374` · MCP tools `memory_query`/`memory_explore`/`memory_handoff_begin`/`memory_consolidate`/`memory_lint` · `handoff` `pending` (`open_questions`/`next_steps`) · FTS5 · RRF · `is_latest=false` (supersession) · `forget-sweep` · `[auto_improve] require_approval` · "consolidação tipo sono" · "restrição" (não fabricar páginas) · "cemitério de superstição" · arquitetura emergente · software maleável ("sempre úmido") · `ScopeResolver` · "Make it work, make it right, make it fast" · KISS.

---

## Aplicação (1-2 linhas)

Substituir o `MEMORY.md` artesanal das lanes por uma wiki markdown versionada por projeto (`decisions/`, `gotchas/`, `_rules/`), capturada por hooks fire-and-forget e consolidada em background — handoff `pending` entre sessões para o próximo agente já "aquecer" sem recontar a novela. Manter embeddings off, validar toda escrita (trilha de auditoria) e nunca pôr a memória no caminho quente.
