# Diagnóstico Akita do Projeto — Etapa 1/7

> Aplicação do método Akita (anti-vibe coding) ao projeto inteiro: livro→skill → site → redes → Amazon.
> Etapa 1 = "planejar antes": mapear o real e medir contra os 8 pilares. Gerado por auditoria de 3 subagentes (Sonnet) + síntese (Opus), cross-model.

## Escopo auditado (componentes reais)
- **Livro→skill:** `book-to-skill/` (subprojeto) + `*_data.py` (fonte autoral) + `publicar_livro.py` + `pdfs/`.
- **Site:** `gerar_livro.py` (gerador canônico), `gerar_seo.py`, `gerar_capa.py`, `books.json`, `*.html`, `assets/`, `script.js` + ~7 geradores legados.
- **Redes/Amazon/pipeline:** `videos/` (`orquestrador.py`, `dag.py`, `pipeline_state.py`, `circuit_breaker.py`, `contracts.py`, `cost_tracker.py`, postadores `facebook_*/instagram_post/tiktok_post`, `coletar_datas.py`), `afiliados/afiliados.json`.

## Matriz dos 8 pilares (dominante por área)

| # | Pilar Akita | livro→skill | site | redes/pipeline |
|---|---|---|---|---|
| 1 | Planejar antes | PARCIAL | PARCIAL | PARCIAL |
| 2 | **TDD real (verde=exit code)** | **FALTA**¹ | **FALTA** | **FALTA** |
| 3 | Humano decide o quê / IA o como | PARCIAL | PARCIAL | **ATENDE** |
| 4 | Refatoração contínua | FALTA | PARCIAL (dívida: 7 geradores) | PARCIAL (token/post triplicado) |
| 5 | **CI + small releases** | **FALTA**¹ | **FALTA** | **FALTA** |
| 6 | Documento-constituição | ATENDE | ATENDE | ATENDE |
| 7 | Loops de auditoria | FALTA | FALTA | PARCIAL (infra existe, manual) |
| 8 | Isolamento de execução | PARCIAL | PARCIAL | PARCIAL (circuit_breaker bom, mas não aplicado) |

¹ **Exceção/ilha de excelência:** o subprojeto `book-to-skill/` JÁ é Akita-correto — pytest (~40 testes), CI de 4 jobs, semver/changelog, `validate_skill.py` no CI, conventional commits. **É o modelo a replicar no resto.**

## GAP Nº1 do projeto
**TDD ausente em todo o código de produção** (site + pipeline + postadores). Hoje a validação é "no olho" (navegador) ou em produção — depois de gastar crédito de API/publicar. É exatamente o pilar nº1 do Akita, e o mesmo diagnóstico do nosso loop-agente. Dois gaps o sustentam: **CI ausente** no repo principal (auto-commits de 30/30min direto na main, sem gate) e **ambiente não-reproduzível** (sem `requirements.txt`/`pyproject.toml`), o que impede qualquer gate de teste rodar.

## Gaps priorizados (todo o projeto)
| Sev | Gap | Evidência |
|---|---|---|
| CRÍTICA | Zero testes automatizados no core (site, orquestrador, postadores) | nenhum `test_*.py` fora de `book-to-skill/` |
| ALTA | Sem CI no repo `Galgan1/biblioteca` (commits direto na main) | CI só existe dentro de `book-to-skill/` |
| ALTA | Sem ambiente reproduzível | sem `requirements.txt`/`pyproject.toml` no pipeline |
| ALTA | `circuit_breaker.py` existe mas **não é aplicado** nos postadores | postadores têm `time.sleep` hard-coded, sem `@retry`/breaker |
| MÉDIA | Dívida: ~7 geradores legados duplicados | `gerar_arte_*`, `gerar_maquiavel_*`, `gerar_psicodelia_*`, etc. |
| MÉDIA | Elo livro→skill não rastreável | só 11 de ~73 livros têm PDF-fonte; sem manifest/log |
| MÉDIA | Auditoria existe mas é manual (sem cron/alerta) | `events.jsonl`, `custos.json`, `coletar_datas.py` disparados à mão |

## Pontos fortes (não mexer)
- **Constituição (pilar 6):** `CLAUDE.md` em 2 níveis + `PUBLICACAO-YOUTUBE.md` + `canal-state.json`. Sólido.
- **Humano decide o quê (pilar 3) no pipeline:** matriz de autoridade, stages `UNMANAGED`, fronteira criativo/mecânico.
- **`book-to-skill/`:** referência Akita interna pronta.

## O que isto destrava (etapas 2→7)
- Etapa 3 (TDD) e 5 (CI) atacam o gap nº1 — **prioridade máxima**.
- Etapa 4 (isolamento) tem base pronta (circuit_breaker) — falta **aplicar**.
- Etapa 7 (refatoração) tem alvo claro (7 geradores legados + token/post triplicado).
- Etapa 2 (constituição) é mais consolidação do que criação (já ATENDE).
