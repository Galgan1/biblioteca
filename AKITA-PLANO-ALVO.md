# Plano-Alvo do Projeto — Etapa 0 (retroativa) · base Akita

> O **norte**: onde o projeto chega quando está Akita-correto. Construído sobre `akita.md` (método) + `AKITA-DIAGNOSTICO.md` (estado atual). As etapas 1→7 convergem para cá. É "Etapa 0" porque deveria ter existido na origem; é "retroativa" porque o projeto já roda.

## Norte
O projeto inteiro — **livro→skill → site → redes → Amazon** — operado como engenharia de software séria, não vibe coding: cada mudança é **planejada, testada (verde = exit code), isolada, auditada e governada**. A IA escreve; o humano decide o quê; os testes guardam o portão.

## Arquitetura-alvo por área
- **Livro→skill:** `book-to-skill/` como pipeline canônico (já testado/CI) + **manifest rastreável** (qual PDF → qual skill, quando, com que versão).
- **Site:** **um** gerador canônico (`gerar_livro.py`), **zero** geradores legados; `<slug>_data.py` = fonte da verdade; geração coberta por teste.
- **Redes/pipeline:** orquestrador com `contracts.py` validando antes de gastar API + **`circuit_breaker` aplicado em todos os postadores**; custo rastreado; tudo idempotente.
- **Amazon:** `afiliados.json` = fonte única; links de produto validados (nunca busca).

## Estado-alvo por pilar Akita (definição de "pronto")
| Pilar | Alvo |
|---|---|
| 1 Planejar antes | toda feature nasce de tarefa atômica + critério de aceite |
| 2 **TDD** | suíte cobre o caminho crítico; **verde = exit code**; roda na CI (modelo: `book-to-skill/`) |
| 3 Humano decide o quê / IA o como | matriz de autoridade explícita (mantida) |
| 4 Refatoração | gerador único, sem duplicação, dívida dos legados zerada |
| 5 **CI + small releases** | gate no repo principal (lint + testes + segurança); cada commit production-ready |
| 6 Constituição | `CLAUDE.md` por lane, lido a cada sessão |
| 7 Auditoria | loops **automáticos** (agendados), não manuais |
| 8 Isolamento | `requirements.txt`/venv; circuit_breaker aplicado; segredos fora do working tree |

## Contratos invioláveis (nunca quebrar)
- **Nada entra sem teste verde.**
- `<slug>_data.py` e `afiliados.json` são a **fonte da verdade**.
- Execução só por ponto único idempotente (nada de comando solto).
- **GitGuy** commita; CI verde antes do merge.

## Ponte com o diagnóstico (gap → alvo)
| Hoje (diagnóstico) | Alvo (Etapa 0) | Etapa que leva lá |
|---|---|---|
| TDD/CI FALTAM | suíte + CI obrigatórios | 3, 5 |
| circuit_breaker existe, não aplicado | aplicado em todo postador | 4 |
| ~7 geradores legados | 1 gerador canônico | 7 |
| auditoria manual | loops agendados | 6 |
| segredos no tree / sem venv | isolados + ambiente reproduzível | 4, 5 |
| constituição já forte | manter | 2 |

## Pronto = projeto Akita-correto quando
CI verde é **obrigatória** no repo principal · caminho crítico **testado** · circuit_breaker **aplicado** · geradores **unificados** · auditoria **automática** · segredos **isolados**. Enquanto qualquer um faltar, o projeto ainda é "Akita de forma, não de substância".
