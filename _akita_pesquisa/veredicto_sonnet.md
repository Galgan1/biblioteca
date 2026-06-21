# Veredicto Cross-Model — Verificador: Claude Sonnet 4.6

**Skill auditado:** `~/.claude/skills/akita/SKILL.md`
**Rúbrica:** `_akita_pesquisa/_PLANO.md` (seção RÚBRICA, R1–R4; R5 é sobre git, não aplica ao skill em si)
**Data:** 2026-06-20
**Método:** leitura integral do skill + amostragem independente de 6 notas-fonte + consulta ao D01 como referência cruzada + leitura dos dois CLAUDE.md (constituição).

---

## R1 — Rastreável: PASS

Amostragem independente de 6 tags (escolhidas por risco de invenção, não por comodidade):

| Tag amostrada | Afirmação no skill | Verificado na nota | Resultado |
|---|---|---|---|
| [A11] l.14 | Karpathy verbatim "fully give in to the vibes… forget that the code even exists" + "throwaway weekend projects" | A11 l.12 (tweet verbatim) + l.17 ("It's not too bad for throwaway weekend projects") | **SIM** |
| [A11] l.15 | Willison: "se você revisa, testa e sabe explicar… é desenvolvimento de software" | A11 l.23 (citação verbatim da distinção ingênuo×disciplinado) | **SIM** |
| [A05] l.85–86 | Opus solo vence ~90% do dia a dia; mistura = "otimização prematura"; só 3 casos; Akita NÃO usa modelo-juiz; Verifier cross-model é acréscimo NOSSO | A05 l.9 (Opus solo, 90%), l.33 ("otimização prematura"), l.22–26 (3 exceções), l.44 (verbatim: "Akita testou Planner→Executor unidirecional e não usa um modelo-juiz/reviewer… nosso Verifier cross-model… é um acréscimo nosso") | **SIM** |
| [A12] l.15 | Akita rejeita "vibe coder"; chama de "Engenharia de Software aplicada à IA"/"Agile Vibe Code" | A12 l.12–13 ("ele NÃO se assume 'vibe coder'"), l.33 (citação verbatim "chamei de 'Agile Vibe Code', mas é basicamente 'Engenharia de Software aplicada à IA'") | **SIM** |
| [A12] l.124 | Vídeo podcast = sátira de terceiros; contradiz posição real do Akita | A12 l.6 ("[SECUNDÁRIO]… tom satírico/irônico… NÃO como fala do Akita"), l.47 ("Contradiz o que o Akita realmente afirma") | **SIM** |
| [A01] l.70–72 | Funções 4-20 linhas; arquivos <500 (ideal 200-300); nomes <5 grep hits; "Grep é mais barato que read"; comentários POR QUÊ + proveniência; "Keep your own comments" | A01 l.6 (4-20 linhas / 200-300 / 500); l.8 (<5 grep hits); l.9 (POR QUÊ / issue/SHA); l.10 ("Keep your own comments. Don't strip on refactor."); l.45 ("Grep é mais barato que read") | **SIM** |

**Ressalvas de honestidade (verificação dirigida):**

- **(a) Karpathy "throwaway weekend projects":** skill l.14 cita [A11]. Confirmado em A11 l.17 verbatim. **CORRETA.**
- **(b) Akita NÃO usa modelo-juiz; Verifier = acréscimo NOSSO:** skill l.86 marca com ⚠️ e cita [A05]. Confirmado em A05 l.44 verbatim ("acréscimo nosso, não dele"). **CORRETA e explicitamente demarcada.**
- **(c) Podcast = sátira de terceiros:** skill l.124 cita [A12]. Confirmado em A12 l.6 ("[SECUNDÁRIO]"), l.19 e l.47 (contradiz posição real). A nota ainda avisa que o conteúdo foi reconstruído de resumos por falta de transcrição — o skill não cita o vídeo como fala do Akita. **CORRETA.**

Nenhuma afirmação encontrada sem suporte nas notas. O auditor D01 verificou 53 tags com 53 SIM / 0 PARCIAL / 0 NÃO. Minha amostra independente de 6 confirma o mesmo resultado. **R1 PASS.**

---

## R2 — Enxuto/acionável: PASS

O skill mantém a estrutura de skill: frontmatter YAML + princípio central + 11 pilares (todos em forma de regras operacionais com bullets) + checklist de 8 itens por tarefa + lista de anti-padrões + tabela de fontes. O texto é em pt-BR, imperativo e orientado a ação. Não vira ensaio: não há seções narrativas longas, digressões filosóficas ou prosa explicativa extensa. O tamanho (~128 linhas) é compatível com um skill denso porém navegável.

Uma observação menor: a seção 9 ("Clean Code para agentes") e a seção 10 ("Memória e contexto") têm subtítulos numerados que fogem ligeiramente ao padrão dos pilares 1–8, mas o conteúdo é igualmente acionável (regras com métricas). Não é bloqueante.

**R2 PASS.**

---

## R3 — Coerência com a constituição: PASS

Contratos invioláveis da constituição (CLAUDE.md da biblioteca):

1. **Git — GitGuy only:** o skill é um documento de método de engenharia; não instrui a fazer commit, push ou PR. Nenhum trecho do skill viola este contrato. O pilar 5 menciona CI e commits, mas como prática de engenharia geral — não dá instrução de `git push` ao agente. **Coerente.**

2. **Fontes da verdade (`_data.py`):** o skill não trata do modelo de dados da Biblioteca; não menciona `_data.py`, `books.json` ou derivados. Não há conflito possível. **Coerente.**

3. **Qualidade (verde = exit code):** o skill reforça explicitamente este contrato em l.30 ("Verde = exit code de teste") e no checklist l.94 ("100% verde (exit code) antes de consolidar"). Alinhado com a constituição l.51. **Coerente e reforçador.**

4. **Idioma pt-BR:** o skill inteiro está em pt-BR. Termos técnicos em inglês (TDD, DRY, SRP, CI) são jargão universal inescapável, não violação de idioma. **Coerente.**

5. **Soberania:** o skill menciona ferramentas (ripgrep, BM25, Bubblewrap, edge-tts via [A07]) sem impor dependência de serviço externo pago. O pilar 8 (isolamento/sandbox com Bubblewrap) é explicitamente uma solução local. **Coerente.**

6. **Ponto de atenção — honestidade sobre o Verifier cross-model (l.86):** o skill afirma que nosso `loop-agente` (Verifier cross-model, Opus↔Sonnet) é "acréscimo nosso — não atribua ao Akita". Isso é compatível com a constituição, que adota o loop-agente como camada adicional. **Coerente e transparente.**

Nenhuma contradição com os contratos invioláveis. **R3 PASS.**

---

## R4 — Critérios verificáveis (não conselho vago): PASS

O skill mantém critérios mensuráveis em vez de recomendações vagas:

- "Verde = exit code de teste" (não "código parece correto") — l.30
- "Cobertura: ratio >1:1 em módulos críticos, mínimo ~80% (95%+ em lógica de negócio)" — l.32
- "Funções 4-20 linhas; arquivos <500 (ideal 200-300)" — l.70
- "Nomes <5 grep hits" — l.71
- "CI gate bloqueante: lint → segurança → testes; vermelho bloqueia merge" — l.46
- "Comando único, output parseável, sem setup humano" para testes — l.31
- "Sandbox Bubblewrap: --ro-bind sistema, escrita só em $(pwd), --unshare-all --share-net" — l.63

O checklist (l.91–98) usa perguntas de sim/não verificáveis por exit code ou inspeção direta de artefato. Nenhum critério depende de julgamento subjetivo do agente ("parece certo", "está bom"). **R4 PASS.**

---

## VEREDICTO FINAL: APROVADO

Todos os 4 critérios PASS. Nenhuma afirmação inventada, nenhuma contradição com a constituição, estrutura de skill mantida, critérios verificáveis por exit code. As 3 ressalvas de honestidade críticas (Karpathy "throwaway", Verifier = acréscimo nosso, podcast = sátira) estão corretamente demarcadas e ancoradas nas notas-fonte.

**Ajustes obrigatórios:** nenhum.

**Observações não-bloqueantes (para eventual revisão futura):**
- Seções 9 e 10 usam numeração diferente dos pilares 1–8 (minor inconsistência de estrutura).
- Afirmação #45 (ciclo red-green explícito) é ligeiramente mais específica que a frase exata da nota A01, embora coerente com a doutrina TDD que as notas suportam. Risco de invenção desprezível.
- A nota A11 avisa que a autoria do gist Karpathy "LLM Wiki" não foi verificada por API (HTTP error); o skill não atribui o gist como fonte primária isolada, o que mitiga o risco.
