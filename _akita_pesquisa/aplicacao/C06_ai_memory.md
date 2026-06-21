# C06 — ai-memory: aplicar o padrão Akita ao nosso sistema de memória de agente

**Fontes:** A06 (`_akita_pesquisa/A06_ai_memory.md`), A08 (`_akita_pesquisa/A08_rag_grep_contexto.md`), seção 10 da `~/.claude/skills/akita/SKILL.md`.
**Alvo da análise:** `C:\Users\User\.claude\projects\C--Users-User--gemini-antigravity-scratch-biblioteca\memory\` (1 índice + 50 topic files).
**Premissa-chave:** o A08 é explícito — *"É exatamente o padrão já adotado aqui (MEMORY.md + skills carregadas just-in-time)."* Não estamos longe do alvo; este doc é sobre **incrementos cirúrgicos**, não reescrita.

---

## 1. Nosso estado atual

**Estrutura física (verificada):**
- 1 `MEMORY.md` = índice de ponteiros. 51 linhas, formato `- [Título](arquivo.md) — resumo de ~1 linha`. Carregado por toda sessão (é o que a constituição injeta).
- 50 topic files `.md` **flat** (sem subpastas). Nomes estáveis e legíveis por slug (`gotcha-camera-dentro-de-mesh.md`, `doutrina-metadados-sempre-ao-vivo.md`, `papel-gitguy-versionamento.md`).
- Markdown puro no disco = fonte da verdade. Sem SQLite, sem embeddings, sem vector DB.

**Frontmatter (100% uniforme, 3 campos):**
```yaml
---
name: <slug>
description: <1 frase>
metadata:
  node_type: memory
  type: project | feedback | reference
  originSessionId: <uuid>
---
```
Distribuição de `type:`: **33 project · 14 feedback · 3 reference**. (`node_type: memory` e `originSessionId` em 49/50; `type` em 50/50.)

**Recuperação (lazy retrieval, já no espírito do A08):**
- O `MEMORY.md` carregado dá os ponteiros; o agente lê o topic file inteiro sob demanda (Read), ou faz `grep`/Grep no diretório quando não sabe onde está o fato.
- **Vizinhança de links**: 47/50 arquivos usam wikilinks `[[outro-arquivo]]` no corpo — é um grafo de ligações navegável (equivalente artesanal ao "link neighborhood / RRF" do A06).
- Há também um system-reminder automático de **idade** ("This memory is N days old… verify against current code") — equivale, na prática, a um aviso de decaimento/frescor.

**Manutenção:** existe a skill `anthropic-skills:consolidate-memory` ("merge duplicates, fix stale facts, prune the index") — um passo de consolidação **manual sob demanda**, análogo ao `memory_consolidate`/`memory_lint` do A06, mas disparado por humano, não por hook.

---

## 2. O que JÁ batemos (não mexer — pilar 3 do CLAUDE.md: cirúrgico)

| Princípio Akita (A06/A08) | Nós | Evidência |
|---|---|---|
| Markdown no disco = fonte da verdade | ✅ | 50 `.md`, zero DB |
| Embeddings OFF por default | ✅ | nenhum embedding/vector |
| `MEMORY.md` = índice de ponteiros, não dados | ✅ | 51 linhas, ~1 ponteiro/linha |
| Páginas pequenas, nomes estáveis por slug | ✅ | topic files curtos e legíveis |
| Lazy retrieval (grep/Read sob demanda, não RAG) | ✅ | Grep + Read; sem chunking/cosine |
| Long-context + busca lexical > vector DB | ✅ | A08 cita nós como o exemplo |
| Vizinhança de links (grafo navegável) | ✅ | wikilinks `[[ ]]` em 47/50 |
| Frescor sem re-embedding ("arquivo mudou → próxima query vê") | ✅ | arquivo é a verdade; +aviso de idade |
| Passo de consolidação/lint | ✅ parcial | skill `consolidate-memory` (manual) |

**Conclusão:** batemos a espinha dorsal inteira do A08 e ~metade do A06. Os gaps são todos do A06 (a parte de **tipagem fina, validação e tiers**), nenhum do A08.

---

## 3. Gaps (vs. A06)

**G1 — Tipagem por `kind` grossa demais.** O A06 separa conhecimento em `decision / gotcha / rule / fact` (e pastas `concepts/ decisions/ gotchas/ procedures/ _rules/`). Nós só temos `project / feedback / reference`. Hoje um *gotcha* (`gotcha-camera-dentro-de-mesh`) e uma *doutrina/regra* (`doutrina-metadados-sempre-ao-vivo`) caem ambos em `type: feedback` — perde-se o filtro "me dê só as armadilhas" ou "só as ordens permanentes". A convenção de **nome** já compensa em parte (prefixos `gotcha-`, `doutrina-`, `papel-`, `projeto-`), mas não está no frontmatter (logo, não é grep-ável por campo).

**G2 — Escrita sem validação explícita (risco de "cemitério de superstição").** O A06 exige: LLM sugere → **valida** (evidência, confiança mínima, caminho válido) → **trilha de auditoria** → escreve. Nós escrevemos memória direto. Não há campo de **confiança** nem de **evidência/fonte** no frontmatter (só `originSessionId`, que aponta a sessão mas não a *prova*). Verificado: nenhum arquivo tem `confidence`/`evidence` estruturados.

**G3 — Sem supersessão/decaimento estruturado.** A06: nunca delete, marque `is_latest=false` (supersession chains) + decaimento geométrico. Nós sobrescrevemos/editamos no lugar (a `consolidate-memory` "fix stale facts"), o que **perde a trilha** de o que era verdade antes. O aviso de idade ajuda no frescor, mas não há marca de "este fato substituiu aquele".

**G4 — Tiers ausentes (Working→Episodic→Semantic→Procedural).** Tudo que temos é Semantic (páginas consolidadas) + um pouco de Procedural (as doutrinas/papéis). Não há `sessions/<id>.md` (Working/Episodic = log bruto + resumo por sessão) nem **handoff `pending`** entre sessões. Hoje o handoff entre lanes é manual (docs soltos como `CONTEXTO-CANAL-MINUTO-REAL.md`).

**G5 — Captura/consolidação manual, não fire-and-forget.** A06 captura por hooks (`SessionEnd`, etc.) e consolida em background (Haiku, ~US$0,02). Nós dependemos do agente lembrar de gravar e de alguém rodar `consolidate-memory`. Não é um gap urgente (é mais infra), mas é a diferença entre "memória que se mantém sozinha" e "memória artesanal".

---

## 4. Melhorias propostas (incrementais, respeitando o formato atual)

> Ordenadas por **valor ÷ risco**. Nenhuma joga fora o que existe; todas são aditivas ao frontmatter atual. **Não executadas aqui** (regra dura: só CRIAR este doc).

### M1 — Adicionar `kind` ao frontmatter (cobre G1) · *quick win*
Acrescentar **um campo** dentro de `metadata:` sem remover `type:`:
```yaml
metadata:
  type: feedback        # mantém (compat)
  kind: gotcha          # NOVO: decision | gotcha | rule | fact | concept | procedure
```
Mapa de migração a partir do nome (sem reclassificar à mão): `gotcha-*`→gotcha, `doutrina-*`/`feedback-*`/`padrao-*`→rule, `papel-*`/`projeto-*`→concept, `*-conexao`/`*-setup`→procedure.
**Como verificar:** `grep -rL "kind:" *.md` retorna vazio (cobertura 100%); `grep -rl "kind: gotcha" *.md | wc -l` ≥ 1 e bate com a contagem de arquivos `gotcha-*`. Teste verde = um script `valida_memoria.py` que falha (exit≠0) se algum `.md` não tem `kind` ∈ vocabulário fechado.

### M2 — Campo `evidence` + `confidence` (cobre G2, ataca o "cemitério de superstição") · *alto valor*
Aditivo ao frontmatter:
```yaml
metadata:
  confidence: high       # high | medium | low
  evidence: "videos/tests/test_net.py verde (exit 0); verificado cross-model"
```
Regra (constituição, não código): **memória nova sem `evidence` nasce `confidence: low`** e o leitor é avisado a re-verificar antes de agir. Isso formaliza o que A06 chama de "validar antes de escrever" sem precisar de servidor MCP.
**Como verificar:** lint script: para todo arquivo com `confidence: high`, `evidence:` não pode estar vazio (exit≠0 se violar). Critério de sucesso forte (Akita pilar 4): rodar o lint sobre os 50 arquivos e ele passar depois do backfill.

### M3 — Supersessão por marca, não por sobrescrita (cobre G3) · *médio*
Quando um fato muda, em vez de editar por cima: marcar o antigo `status: superseded` + `superseded_by: <novo-slug>` e criar/atualizar o novo. Mantém a trilha (o A06 nunca deleta). O `MEMORY.md` lista só o `is_latest`.
**Como verificar:** `grep "status: superseded"` sempre tem `superseded_by:` apontando para um arquivo que existe (lint: link quebrado = exit≠0). Conferir que nenhum item `superseded` aparece no `MEMORY.md`.

### M4 — Lint de memória como teste verde (cobre G2+G3, é o que dá "dente" a M1-M3) · *alto valor*
Um `valida_memoria.py` (stdlib, sem dep nova — padrão da etapa 3 da Akita-ização) que checa: (a) todo `.md` tem os campos obrigatórios; (b) `kind`/`type`/`confidence` ∈ vocabulário fechado; (c) wikilinks `[[x]]` apontam para arquivo existente; (d) todo arquivo aparece no `MEMORY.md` e vice-versa (índice e corpo em sincronia); (e) regra M2 (high ⇒ evidence). Plugável no `videos/ci.bat`/`auditoria.bat` que já existem.
**Como verificar:** o próprio script É a verificação — **verde = exit 0** (doutrina Akita). Rodar antes/depois do backfill; CI roda em PR.

### M5 — Convenção de handoff leve (cobre G4 parcial, sem infra de hooks) · *baixo custo*
Um único `_handoff.md` (ou `sessions/_pending.md`) com `open_questions` + `next_steps` que a sessão atualiza ao encerrar trabalho não-trivial e a próxima lê primeiro. É o handoff `pending` do A06 feito à mão — resolve o "não recontar a novela" entre lanes sem servidor.
**Como verificar:** existência + o lint (M4) garante que, se `_handoff.md` existe, tem as duas seções. Teste de aceitação: abrir uma sessão fria numa lane e confirmar que `_handoff.md` + `MEMORY.md` bastam para retomar sem perguntar ao usuário.

### M6 — (NÃO fazer agora) hooks fire-and-forget + consolidação automática (G5)
Registrar como **incremento futuro mapeado**, igual fizemos na Akita-ização (postadores de escrita). Requer servidor local (porta 49374-style) + Haiku em background — é infra, não cabe no formato markdown puro e fere "simplicidade primeiro" enquanto a captura manual funciona. Só construir se a memória começar a apodrecer por esquecimento de gravação.

---

## 5. Risco

- **Baixo no geral:** M1–M3 são **aditivos ao frontmatter** — leitores atuais ignoram campos novos; nada quebra. M4/M5 criam arquivos novos, não tocam memória existente.
- **Backfill dos 50 arquivos (M1/M2):** trabalho de classificação que, se feito por LLM sem validação, é *exatamente* o "cemitério de superstição" que queremos evitar. Mitigação: derivar `kind` do **nome do arquivo** (determinístico, auditável), e `confidence` começar `low` por default — humano promove a `high` só com evidência. **Nunca** o LLM inventar `evidence`.
- **Acoplamento com a constituição:** M2/M3/M5 são *regras*, não só código; só pegam se entrarem no `CLAUDE.md` (como a constituição já fez na etapa 2). Sem isso, viram campos órfãos.
- **Não-regressão:** o `MEMORY.md` é carregado toda sessão — qualquer mudança que o engorde (ex.: pôr `evidence` no índice) viola o limite de ~25 KB do A08. Manter o índice enxuto; campos novos vivem só nos topic files.
- **Escopo (regra dura desta tarefa):** nada disto foi executado. Este doc só descreve; a implementação deve passar pelo `/loop-agente` (Planner→Executor→Verifier) com o lint M4 como rúbrica de verde, e o git é do GitGuy.

---

**Veredito:** já batemos 100% do A08 e a espinha do A06. Os gaps reais são 5, todos de *disciplina de escrita* (tipagem fina, evidência/confiança, supersessão, handoff) — não de infraestrutura. Caminho recomendado: **M1 + M2 + M4** primeiro (kind + evidence/confidence + lint verde), porque dão o maior ganho anti-"cemitério de superstição" com risco mínimo e cabem no formato markdown atual. M3/M5 em seguida; M6 fica como incremento futuro mapeado, como manda a prática Akita.
