# N5 — Auditoria de Coerência & Qualidade-de-Doc (Akita)

**Escopo:** `scratch/CLAUDE.md` (raiz) × `scratch/biblioteca/CLAUDE.md` (projeto) × `~/.claude/skills/akita/SKILL.md`.
**Lente:** constituição imperativa, concisa, sem rot (Akita pilar 6: "formato curto, imperativo, bullets, sem prosa filosófica").
**Read-only.** Métrica de tamanho real: `biblioteca/CLAUDE.md` = **134 linhas, 16 seções `##`**, das quais **7 marcadas `[ADIÇÃO]`** + 1 não-marcada que também é adição (vídeo). Skill akita = 128 linhas.

---

## Resumo executivo (≤8 linhas)
1. O projeto-CLAUDE.md **virou ensaio**: 134 linhas, 7 seções `[ADIÇÃO]` que são **paráfrase quase 1:1 da skill akita** (clean-code, memória, 4-blocos, isolamento) — duplicação com alto risco de drift. (sev. ALTA)
2. **Contradição de processo:** a skill diz que multi-modelo/juiz "NÃO é default" e "otimização prematura" [A05]; o CLAUDE.md torna o `/loop-agente` cross-model **obrigatório em toda tarefa não-trivial**. Não está reconciliado no projeto. (sev. ALTA)
3. **Redundância estrutural:** "Modo PADRÃO" + "Contratos Invioláveis" + 7 `[ADIÇÃO]` dizem o mesmo Akita três vezes, em granularidades diferentes. (sev. MÉDIA)
4. As `[ADIÇÃO]` deveriam ser **ponteiros de 1 linha → skill akita**, mantendo só o que é específico-do-projeto (comandos, paths, contratos de formato). Corte estimado: ~134 → ~70 linhas.
5. Boa prática a preservar: o disclaimer de honestidade-de-fonte [A05] e os contratos de formato/módulo (esses SÃO específicos do projeto e devem ficar).

---

## 1. CONTRADIÇÕES

### 1.1 [ALTA] Loop cross-model obrigatório × Akita diz "não é default"
- **Onde:** `biblioteca/CLAUDE.md` §"Modo de trabalho PADRÃO" item 2 (L11) — *"Execução = `/loop-agente`. Não responda/entregue direto... verificação cross-model (juiz ≠ autor: Opus ↔ Sonnet)... sem exceção"* (L13). Versus skill `akita/SKILL.md` §11 (L85-86): *"Multi-modelo (Planner→Executor) NÃO é default... mistura é 'otimização prematura'... o Akita NÃO usa modelo-juiz/reviewer."*
- **Problema:** A constituição impõe como **mandatório e sem exceção** justamente a prática que a skill-fonte classifica como acréscimo opcional / otimização prematura. Um agente que leia os dois recebe ordens opostas sobre quando acionar o juiz cross-model.
- **Nota:** a skill É honesta ao marcar isso como "acréscimo nosso" (L86) — o problema é o CLAUDE.md **omitir** essa ressalva e vender como dogma Akita. O contrato 3 ("na dúvida o verificador reprova", L77) reforça o juiz sem citar que é decisão local, não Akita.
- **Sugestão:** em §Modo PADRÃO item 2, acrescentar 1 frase: *"(o ciclo juiz/cross-model é decisão DESTE projeto, não do Akita — ver akita §11; aplica-se a código de produção, dispensável no resto)"*. Alinha a obrigatoriedade ao escopo real e remove a contradição de origem.

### 1.2 [MÉDIA] "Sem exceção" × "tarefas triviais dispensam"
- **Onde:** `biblioteca/CLAUDE.md` L13: *"Tudo que gera/edita código de produção: Akita + loop, **sem exceção**"* logo após *"Tarefas triviais... dispensam o cerimonial"*. Internamente coerente (o "sem exceção" é só p/ produção), mas a justaposição "dispensam" + "sem exceção" na mesma linha é ambígua.
- **Sugestão:** trocar "sem exceção" por "obrigatório" (o "sem exceção" sugere que anula a frase anterior).

### 1.3 [BAIXA] Idioma do CLAUDE.md raiz × contrato pt-BR
- **Onde:** raiz inteiro está em **inglês**; `biblioteca/CLAUDE.md` contrato 6 (L80) exige *"todo conteúdo em pt-BR (pt-PT é bloqueante)"*.
- **Avaliação:** NÃO é contradição real — o contrato 6 fala de **conteúdo gerado** (livros, peças), não da doc interna. Mas convém 1 nota para o agente não se confundir.
- **Sugestão (opcional):** no contrato 6, especificar "conteúdo *publicado*" para deixar claro que a constituição em si pode ser EN/PT.

### 1.4 [BAIXA] Sandbox Bubblewrap (akita §8) × realidade Windows
- **Onde:** skill akita §8 (L63) prescreve `bwrap`/`--unshare-all`; o projeto roda em **Windows 11 / PowerShell** (sem bwrap). O `biblioteca/CLAUDE.md` §Isolamento (L122-127) adapta corretamente para "ponto único idempotente + deny no settings.local.json" — ou seja, **já reconciliado**. Apenas registro de que a adaptação está certa; não há ação.

---

## 2. INCHAÇO / ROT

### 2.1 [ALTA] Contagem e veredito
- 16 seções `##`. As 8 seções de adição-de-doutrina (7 com tag `[ADIÇÃO]` + "Contratos de módulo — lane de vídeo" L100, que é adição sem tag) ocupam **~L83-133 = ~50 linhas (37% do arquivo)**.
- O Akita §6 (L53) é explícito: constituição = *"formato curto, imperativo, bulletpoints... sem prosa filosófica"*. As `[ADIÇÃO]` violam isso: trazem **justificativa de doutrina** (o "por quê" do Akita), não contrato-de-projeto.

### 2.2 Seções que são prosa-doutrinária (devem virar ponteiro)
Estas **repetem a skill** sem agregar nada específico do projeto:
| Seção (linha) | Veredito | Ação |
|---|---|---|
| Clean Code para agentes (L83-92) | ~90% cópia de akita §9 | → ponteiro: *"Clean code p/ agentes: ver skill akita §9. Específico aqui: arquivos `<500` linhas; gate `python testar.py`."* |
| Memória markdown+grep (L111-116) | ~85% cópia de akita §10 | → ponteiro + manter só o local: `valida_memoria.py` (verde=exit 0) e "invoca skill p/ fato vivo". |
| Prompt em 4 blocos (L118-120) | 100% cópia de akita §1 | → **deletar** ou ponteiro de 1 linha p/ akita §1. Nada de projeto aqui. |
| Isolamento e permissões (L122-127) | ~70% cópia de akita §8 | → manter SÓ o específico (path `.claude/settings.local.json → deny`, "YOLO proibido") como sub-bullet do contrato 1; resto → akita §8. |

### 2.3 Seções que DEVEM ficar (são contrato-de-projeto, não doutrina)
NÃO enxugar — são valor real e específico:
- **Contratos de Formato — Gerador** (L15-39): paths, contagens de slides, classe CSS. Específico, testável. **Manter.**
- **Git — GitGuy** (L41-59): regra de processo única do projeto. **Manter** (mas ver §3.1 — duplica o contrato 1).
- **O que versionar** (L61-69): tabela operacional. **Manter.**
- **Contratos de módulo — lane de vídeo** (L100-109): paths reais de `videos/`. Específico. **Manter** (mas adicionar a tag de seção e considerar mover p/ skill da lane de vídeo se existir).
- **Guardas de máquina: CI + anti-fantasma** (L129-133): comandos reais (`testar.py`, `audita_fantasmas.py`) + a regra-ouro *"passa local ≠ está no git"*. **Manter** — é o gate concreto.

### 2.4 Estimativa de enxugamento
Convertendo as 4 seções de §2.2 em ponteiros: **~50 linhas → ~12**. Arquivo: **134 → ~95 linhas**. Se também fundir Git/GitGuy ao contrato 1 (§3.1): **~80 linhas**. Ganho: doc cabe melhor na janela do agente, menos drift.

---

## 3. DUPLICAÇÃO

### 3.1 [MÉDIA] Git/GitGuy dito duas vezes no MESMO arquivo
- **Onde:** §"Git — REGRA ABSOLUTA" (L41-59, ~18 linhas) **e** "Contratos Invioláveis" contrato 1 (L75): *"Git: só o GitGuy commita/pusha/cria PR (ver seção acima)"*.
- **Avaliação:** o contrato 1 já remete corretamente ("ver seção acima") — não é drift, mas é redundante ter 18 linhas + 1 linha do mesmo tema separadas por 2 seções. A lista de "o que você nunca faz" (L51-55) é o miolo; o resto é justificativa.
- **Sugestão:** encolher §Git para ~6 linhas (regra + lista do-not + 1 linha de por-quê) e deixar o contrato 1 como o ponto canônico.

### 3.2 [ALTA] Doutrina Akita duplicada entre CLAUDE.md e skill (risco de drift)
- **clean-code / memória / 4-blocos / isolamento** aparecem **integralmente nos dois lugares** (não como ponteiro). Exemplos de cópia quase-literal:
  - "Funções 4-20 linhas; arquivos <500 (ideal 200-300)... cabe numa tool call" → CLAUDE.md L87 ≈ akita L70.
  - "nomes <5 grep hits; PROIBIDO `data`,`process`,`handler`,`Manager`,`Service`" → CLAUDE.md L88 ≈ akita L71.
  - "cemitério de superstição" → CLAUDE.md L114 ≈ akita L80.
  - "Objetivo·Método·Restrições·Validação" → CLAUDE.md L120 ≈ akita L24.
- **Risco concreto (o próprio Akita avisa, DRY p/ agente, akita L73):** se um dia o Akita atualizar a skill (ex.: muda "<5 grep hits" → "<3"), o CLAUDE.md fica defasado e o agente recebe dois números. **A constituição replica a regra em vez de apontar para a fonte.**
- **Veredito:** hoje é **cópia integral, não ponteiro** → é exatamente o anti-padrão de DRY que a skill prega. Recomendação: ponteiros.

---

## 4. IMPERATIVO / ACIONÁVEL

### 4.1 [MÉDIA] Prosa filosófica embutida (Akita §6 proíbe)
Trechos que são *justificativa/ensaio*, não regra acionável:
- L57 §Git "Por quê": *"múltiplos agentes editam o mesmo working tree. Commits fora de hora criam estados inconsistentes, enterram trabalho..."* — explicação, não comando. (manter 1 linha, cortar o resto)
- L85: *"Otimize o código para a forma como o agente lê e edita."* — slogan, não testável.
- L113: *"Embeddings/RAG ficam OFF: long-context + grep > vector DB."* — doutrina-Akita, não contrato deste projeto.
- L118-120 (4 blocos): puramente conceitual, zero gancho de projeto.
- **Contraste positivo:** L129-133 (CI/anti-fantasma) e L100-109 (módulos vídeo) são **exemplares**: nomeiam comando, path, contrato verificável. É o tom que o resto deveria ter.

### 4.2 [BAIXA] Boas regras imperativas e testáveis (preservar)
- "Sempre 4 frames" (L21), "≥6 slides" (L26), "≤350 linhas" (L36), "verde = exit code" (L77), "`python testar.py`" (L132): tudo binário/verificável. Este é o padrão-ouro do arquivo.

---

## 5. NAVEGABILIDADE

### 5.1 [MÉDIA] Ordem mistura projeto-específico com doutrina genérica
Ordem atual: Modo PADRÃO → Formato → Git → Versionar → **Contratos Invioláveis** → 7×[ADIÇÃO] → Vídeo → Memória → 4-blocos → Isolamento → Guardas.
- Problema: "Contratos Invioláveis" (a constituição-núcleo, L71-81) fica **no meio**, depois vêm 50 linhas de doutrina genérica `[ADIÇÃO]` e SÓ no fim aparecem os Guardas de máquina (CI), que são o gate mais importante.
- **Sugestão de ordem (núcleo → específico → ponteiros):**
  1. Modo PADRÃO (curto)
  2. **Contratos Invioláveis** (a constituição — primeiro!)
  3. Guardas de máquina (CI + anti-fantasma) — o gate, logo após os contratos
  4. Contratos de Formato + Contratos de módulo vídeo (específicos, testáveis)
  5. O que versionar (tabela)
  6. Git/GitGuy (encolhido)
  7. **Ponteiros para a skill akita** (1 bloco curto cobrindo clean-code/memória/4-blocos/isolamento) — em vez das 4 seções longas.

### 5.2 [BAIXA] Redundância tripla "Modo PADRÃO × Contratos × [ADIÇÃO]"
O Akita aparece em 3 camadas: como *método* (Modo PADRÃO L9), como *contrato 3* (L77), e como *doutrina detalhada* (as `[ADIÇÃO]`). É a mesma ideia ("verde=exit code, TDD, isolamento") repetida em 3 granularidades. Consolidar: Modo PADRÃO = ponteiro p/ skill; Contratos = as 7 regras invioláveis; doutrina detalhada = MORA na skill, não aqui.

---

## Recomendação concreta (1 parágrafo)
Transformar as 4 seções `[ADIÇÃO]` genéricas (Clean Code, Memória, 4-blocos, Isolamento) em **um único bloco de ponteiros** ("Para clean-code/memória/prompt/isolamento, a fonte é a skill `akita` §9/§10/§1/§8; abaixo só o que é específico deste projeto: ..."), preservando apenas os ganchos locais (paths, `valida_memoria.py`, `settings.local.json → deny`, `testar.py`). Reordenar conforme §5.1. Adicionar a ressalva de §1.1 ao Modo PADRÃO. Resultado: ~134 → ~80 linhas, sem perder nenhum contrato verificável e eliminando o risco de drift com a skill.
