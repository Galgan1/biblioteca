# C03 — Constituição: lacunas vs. método Akita atualizado

> Aplicação · Wave 3. Alvo: os dois `CLAUDE.md` (raiz `scratch/` + projeto `biblioteca/`).
> Fonte método: `~/.claude/skills/akita/SKILL.md` (pilares 1–11). Norte: `AKITA-PLANO-ALVO.md`. Estado: `AKITA-DIAGNOSTICO.md`.
> **Natureza:** a constituição é DOC, não código — a verificação é coerência (não-contradição com os 7 contratos invioláveis), não exit code.
> **Proveniência:** referências `[Axx]` apontam para o corpus Akita citado no SKILL.md.

---

## 1. Estado atual (o que os dois CLAUDE.md já cobrem)

O diagnóstico (Etapa 1) classifica o pilar 6 (constituição) como **ATENDE** nas três áreas. Cobertura real hoje:

**Raiz (`scratch/CLAUDE.md`)** — guia comportamental anti-erro de LLM:
- §1 *Think Before Coding* → cobre Akita pilar 1 (planejar antes; explicitar premissas; não escolher em silêncio).
- §2 *Simplicity First* → cobre "código mínimo, nada especulativo" (ressoa pilar 4 / clean code).
- §3 *Surgical Changes* → mudança cirúrgica, casar estilo, não apagar dead code alheio.
- §4 *Goal-Driven Execution* → critério de sucesso verificável + plano por passo (ressoa pilar 2, mas sem amarrar "verde = exit code").
- §5 *Deploy VPS* → SSH/scp para `andregalgani.com.br`.

**Projeto (`biblioteca/CLAUDE.md`)** — constituição operacional da Biblioteca:
- **Modo de trabalho PADRÃO:** Akita + `/loop-agente` (Planner→Executor→Verifier, rúbrica, cross-model Opus↔Sonnet, parada em 5).
- **Git GitGuy-only:** lista explícita do que nunca fazer (commit/push/add+commit/PR) e o porquê (working tree compartilhado).
- **Tabela "o que versionar"** (fonte ✅ vs. runtime ❌).
- **7 Contratos Invioláveis:** (1) git=GitGuy, (2) fontes da verdade `_data.py`/`afiliados.json`/`canal-state.json`, (3) qualidade Akita (teste verde=exit code, ponto único idempotente, na dúvida reprova), (4) gerador canônico único + tokens de marca únicos, (5) distribuição/afiliado (Amazon só `/dp/`·`/gp/`, IG link na bio, FB nativo+1º comentário), (6) pt-BR (pt-PT bloqueante), (7) soberania (local/grátis + rota de fuga edge-tts).

**Conclusão do estado atual:** a *governança* (quem decide, quem commita, fontes da verdade, qualidade=verde, idioma, soberania) está sólida. O que falta é a camada **"como o agente deve escrever e lembrar"** — os achados NOVOS do SKILL.md (pilares 9, 10, 11) ainda não estão na constituição do projeto.

---

## 2. Gap vs. método ATUALIZADO

O método atualizado trouxe três pilares que **não têm âncora** na constituição do projeto. Nenhum contradiz os contratos atuais — são camadas ausentes.

| Achado novo (SKILL.md) | Onde está hoje | Gap |
|---|---|---|
| **Clean code p/ agentes** [A01] (pilar 9): funções 4–20 linhas; arquivos <500 (ideal 200–300); nomes <5 grep hits, proibido `data`/`process`/`handler`/`Manager`/`Service`; comentários POR QUÊ + proveniência ("keep your own comments"); tipos explícitos; early returns ≤2 níveis; erro com contexto; setup idempotente | §2 raiz fala "simplicidade", mas **sem números operacionais** nem regra de nomes/proveniência | **AUSENTE no projeto** — só princípio vago, sem métrica acionável |
| **Memória markdown + grep** [A06][A08] (pilar 10): markdown no disco = fonte da verdade; `MEMORY.md` = índice de ponteiros → topic files; long-context + grep > RAG; embeddings off; auto-aprendizado **com validação** (anti "cemitério de superstição") | Não mencionado em nenhum CLAUDE.md | **AUSENTE** — o projeto já PRATICA (MEMORY.md existe), mas a doutrina não está escrita |
| **Prompt 4-blocos** [A03] (pilar 1): Objetivo · Método · Restrições · Validação; injetar conhecimento de domínio | §1/§4 raiz tocam "planejar" e "critério de sucesso" soltos | **PARCIAL** — falta nomear os 4 blocos como padrão |
| **Ponto único de teste** [A01] (pilar 2): comando único, output parseável, sem setup humano | Contrato 3 cita "ponto único idempotente" p/ EXECUÇÃO | **PARCIAL** — falta dizer que o TESTE também é comando único rodável pelo agente |
| **Isolamento de execução** [A07] (pilar 8): wrapper idempotente, permissões mínimas (negar `rm -rf`/`sudo`/`git push --force`), anti-YOLO (`--dangerously-skip-permissions`) | Contrato 1 (GitGuy) cobre git; sandbox/permissões não | **PARCIAL** — git protegido, resto do host não |
| **Harness > modelo** [A05][A10]: escolher pelo arreio; multi-modelo NÃO é default | `/loop-agente` é cross-model por desenho | **OK por ora** — registrar a honestidade de fonte (juiz cross-model é acréscimo nosso, não do Akita) é nice-to-have, não gap |

Foco do bloco de adições: pilares **9 (clean code), 10 (memória)** e o reforço de **1 (4-blocos)**, **2 (teste=comando único)** e **8 (isolamento/permissões)** — porque o diagnóstico já aponta o resto (TDD/CI/refatoração) para as etapas 3/5/7, não para a constituição.

---

## 3. Bloco de adições proposto (pronto p/ colar)

> **ADIÇÃO** ao final de `biblioteca/CLAUDE.md`, **depois** da seção "Contratos Invioláveis". NÃO altera nem renumera os 7 contratos — acrescenta *normas de ofício* que os concretizam. Imperativo, bullets, orientado a ação (pilar 6: "nenhum LLM faz nada por default — é preciso ESCREVER as regras").

```markdown
## Clean Code para agentes — normas de ofício (Akita pilar 9) [ADIÇÃO]

Otimize o código para a forma como o agente lê e edita. Concretiza o contrato 3 (qualidade).

- **Funções 4–20 linhas. Arquivos < 500 linhas (ideal 200–300)** — deve caber numa tool call sem truncar. Arquivo gigante → extraia responsabilidade (não "depois").
- **Nomes únicos e pesquisáveis: meta < 5 hits de grep.** PROIBIDO `data`, `process`, `handler`, `Manager`, `Service` (~50 matches). Grep é mais barato que read.
- **Comentário = POR QUÊ, não O QUE** + proveniência (issue/SHA/workaround/constraint). **Não apague comentário alheio no refactor** — carrega a intenção da iteração anterior ("keep your own comments").
- **Tipos explícitos** (type hints) = gabarito p/ o agente. **DRY é mais crítico ainda** (o agente atualiza uma cópia e esquece as réplicas).
- **Early returns, ≤ 2 níveis de indentação.** Erro com contexto (valor ofendido + forma esperada). Setup idempotente (`bin/setup` roda em máquina limpa).
- Vale só para código novo/editado por você. NÃO refatore código alheio que não está quebrado (mudança cirúrgica — CLAUDE.md raiz §3).

## Teste = comando único que o agente roda sozinho (Akita pilar 2) [ADIÇÃO]

Concretiza o contrato 3 ("verde = exit code"):
- O teste que define "pronto" é **um comando único** (em README/CLAUDE.md/Makefile), **output parseável**, **sem setup humano** (sem seed manual, credencial secreta ou config ausente).
- **Um bug vira um teste de regressão** antes do fix. Modelo a replicar: `book-to-skill/` (pytest + CI já verdes).

## Memória do agente: markdown + grep, nunca RAG (Akita pilar 10) [ADIÇÃO]

- **Markdown no disco = fonte da verdade.** `MEMORY.md` é índice de ponteiros → topic files curtos sob demanda. Embeddings/RAG ficam OFF: long-context + grep (ripgrep) > vector DB.
- **Não escreva memória sem validar** (evidência/confiança/trilha). Memória sem validação = "cemitério de superstição".
- Toda lane que precisar de fato vivo (ex.: metadados) **invoca a skill** e lê ao vivo — não responde de memória.

## Prompt em 4 blocos (Akita pilar 1) [ADIÇÃO]

Toda tarefa não-trivial nasce com: **Objetivo · Método · Restrições · Validação**, e injeta o conhecimento de domínio que está na sua cabeça (senão o modelo assume o "default mais razoável" e erra). Tarefa atômica, uma por vez.

## Isolamento e permissões mínimas (Akita pilar 8) [ADIÇÃO]

Estende o contrato 1 (git) ao host inteiro:
- Execução por **ponto único idempotente revisável** — nunca comando solto/destrutivo no host.
- **Negar por padrão:** `rm -rf`, `sudo`, `git push --force`. Anti-padrão proibido: **YOLO mode** (`--dangerously-skip-permissions`).
- Segredos **fora do working tree**; ambiente reproduzível (venv/`requirements.txt`) antes de qualquer gate de teste.
```

---

## 4. Checklist de não-contradição (como verificar)

A constituição é doc → verificação = **coerência**, não exit code. Cada item do bloco proposto foi conferido contra os 7 contratos: deve **concretizar** ou **ser neutro**, nunca colidir.

- [x] **Contrato 1 (git=GitGuy):** o bloco "Isolamento" reforça (nega `git push --force`, ponto único) — **não autoriza** o agente a commitar. ✔ coerente.
- [x] **Contrato 2 (fontes da verdade):** "Memória markdown+grep" trata de memória do AGENTE (MEMORY.md), não das fontes de produto (`_data.py`/`afiliados.json`/`canal-state.json`). Não compete nem renomeia fonte. ✔
- [x] **Contrato 3 (qualidade: verde=exit code, ponto único, na dúvida reprova):** "Teste=comando único" e "Clean code" **detalham** o contrato 3; não o afrouxam. "Setup idempotente" alinha com "ponto único idempotente". ✔
- [x] **Contrato 4 (gerador canônico + tokens únicos):** "Clean code" diz para não refatorar código alheio que não quebrou → **protege** o gerador canônico de deriva. Não manda criar novo gerador. ✔
- [x] **Contrato 5 (distribuição/afiliado):** bloco não toca em links/canais. Neutro. ✔
- [x] **Contrato 6 (pt-BR):** todo o bloco está em pt-BR; termos técnicos (grep, RAG) são universais, não pt-PT. ✔
- [x] **Contrato 7 (soberania):** "embeddings/RAG OFF + grep local" **reforça** a soberania (menos dependência de serviço externo). "Isolamento" mantém local/grátis. ✔
- [x] **Modo de trabalho PADRÃO (Akita + /loop-agente):** "Prompt 4-blocos" e "teste=comando único" alimentam o Planner/Verifier; não substituem o loop. ✔
- [x] **CLAUDE.md raiz §3 (mudança cirúrgica):** "Clean code" foi explicitamente limitado a código novo/editado, com nota "não refatore código alheio". Sem colisão com a regra de não-melhorar adjacências. ✔
- [x] **Honestidade de fonte (SKILL.md A05):** o bloco NÃO atribui o juiz cross-model ao Akita; mantém-no como prática do `/loop-agente`. ✔
- [x] **Não-renumeração:** o bloco entra como SEÇÕES novas após "Contratos Invioláveis"; os 7 contratos permanecem com os mesmos números. ✔

**Verificação sugerida (idempotente, opcional):** após colar, rodar `grep -n "Contrato\|contrato\|inviol" biblioteca/CLAUDE.md` e confirmar que continuam **7** contratos numerados 1–7. Critério de aceite = contagem inalterada + nenhum item do checklist acima marcado como colisão.

---

## 5. Risco / colisão

- **Risco baixo — inflação da constituição.** O Akita pede constituição CURTA e imperativa [A01]. O bloco acrescenta 5 seções. Mitigação: cada seção é bullets densos; o detalhe fica na skill `akita`, a constituição só ancora a regra + a referência ao pilar. Se ficar longo, mover "Prompt 4-blocos" para a raiz (`scratch/CLAUDE.md` §1), onde já há "Think Before Coding".
- **Colisão potencial — funções ≤20 linhas vs. código legado.** Os ~7 geradores legados e postadores (token/post triplicado) violam o limite hoje. **Não é contradição** porque a regra vale só para código novo/editado (cláusula explícita no bloco); a dívida legada é tarefa da Etapa 7 (refatoração), não da constituição. Evita que o agente "melhore" tudo de uma vez (viola §3 raiz).
- **Sobreposição com a skill `akita`.** As regras já vivem na skill; duplicá-las na constituição é intencional (pilar 6: a IA lê o CLAUDE.md a cada sessão; a skill é sob demanda). Risco de drift entre os dois → manter a constituição como ponteiro curto + `[Axx]`.
- **Sem risco de quebrar produção:** é documento; nenhuma linha de código de produção muda. A única ação física foi criar este arquivo de pesquisa.
- **Pendência de decisão humana (pilar 3):** este C03 é PROPOSTA. A edição efetiva do `CLAUDE.md` é mudança de produção → fica para o humano aprovar e para o GitGuy versionar. Não editei nenhum CLAUDE.md.
```
