# Plano — Upgrade do /akita + projeto no "jeito Akita" (2026)

> Planner: Claude Opus 4.8. Execução: loop-agente (Planner→Executor→Verifier cross-model).
> Fonte da verdade = corpus PRÓPRIO do Akita (akitaonrails.com), não o podcast G_8uG1Ot0yo
> (que é comentário do Mano Deyvin *sobre* o Akita). Cada prática DEVE citar a URL de origem.

## GOAL (critério de sucesso, verificável)
1. `/akita` (SKILL.md em ~/.claude/skills/akita) atualizado com o método REAL e atual do Akita,
   **cada regra com fonte citada** (sem prática inventada).
2. Repositório com **plano de adoção concreto e verificável** (gap → mudança → como ficar verde).
3. Aprovado por **juiz cross-model** (Sonnet julga; autor = Opus).

## RÚBRICA (PASS exige TODOS)
- R1 **Rastreável**: toda prática nova no skill aponta para uma fonte (URL Akita). Zero invenção.
- R2 **Enxuto/acionável**: continua um SKILL (pilares + checklist), pt-BR, não um ensaio.
- R3 **Coerente com a constituição**: não contradiz contratos invioláveis do CLAUDE.md
  (GitGuy-only-git, pt-BR, soberania/rota-de-fuga, fonte-da-verdade `_data.py`).
- R4 **Aplicação concreta**: cada proposta diz gap → mudança → verificação (exit code), não conselho vago.
- R5 **Sem git**: tudo no disco; GitGuy versiona depois. Eu não commito/pusho/PR.

## DAG de execução
Wave 1 (12 agentes RESEARCH, paralelo) → escrevem nota em _akita_pesquisa/NN_*.md
Wave 2 (eu, Planner/senior) → síntese: SKILL.md novo + references/fontes
Wave 3 (6 agentes APPLICATION, paralelo) → leem o repo, propõem mudança verificável
Wave 4 (Verifier Sonnet, cross-model) → julga SKILL.md contra R1–R4 → retry (máx 5)

## Roster de agentes (20)
### RESEARCH (12) — cada um: 1 fonte → extrai práticas concretas + cita URL
A01 Clean Code pra Agentes de IA
A02 Software Nunca Está 'Pronto' / One-Shot Prompt é Mito
A03 Como falar com o Claude Code efetivamente (LLMs não dão o resultado)
A04 Boas práticas de projetos open source com LLM — O Mínimo
A05 Planner + Executor (misturar 2 modelos) + Benchmarks Parte 2 (múltiplos modelos)
A06 ai-memory (3 posts: sistema, Karpathy Wiki+Hermes, arquitetura emergente)
A07 AI Agents: Garantindo a Proteção do seu Sistema (isolamento/execução)
A08 RAG Está Morto? Contexto Longo, Grep (como o agente navega o código)
A09 Vibe Code: do Zero à Produção em 6 Dias + FrankMD (workflow real, ponta a ponta)
A10 AI Agents: qual é o melhor / qual LLM é a melhor (tooling landscape)
A11 Karpathy: definição de vibe coding + LLM Wiki (linhagem externa que o Akita usa)
A12 Podcast G_8uG1Ot0yo (tentar resumo) + RANTs (a postura/filosofia dele)

### APPLICATION (6) — cada um: lê o NOSSO repo, propõe mudança verificável
C01 TDD harness: estado dos testes; propor runner + 1º teste de reprodução
C02 CI: propor GitHub Actions/pre-commit (ruff + testes + secret scan) — já há .github/
C03 Constituição: reconciliar CLAUDE.md com "AGENTS.md + prompt logging" do Akita
C04 Isolamento/execução: o "ponto único idempotente" (nada de comando solto)
C05 Refactor/higiene: triagem dos 71 órfãos + 9 geradores legados (do vp100 mapa)
C06 ai-memory: comparar nossa memória (.claude) com Karpathy LLM Wiki do Akita

### SÍNTESE/AUDIT (2)
D01 Source-map: tabela prática→fonte (auditoria de R1)
D02 Rascunho estrutural do SKILL.md novo (eu finalizo)
