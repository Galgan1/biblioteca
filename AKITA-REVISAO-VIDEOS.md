# Revisão Akita — lane `videos/` (Criador de Vídeos) · 2026-06-20

> Revisão-DELTA sobre `AKITA-DIAGNOSTICO.md` (17/jun). Gerada por **7 subagentes de auditoria (Sonnet, 1 por pilar) + síntese (Opus)** — cross-model, via `loop-agente`. Escopo: `videos/` = 71 `.py` / ~10,5k linhas.

## Veredito geral
A lane saiu do "Akita de **forma**" e já é **Akita de substância na FUNDAÇÃO**: `python testar.py` = **182 testes VERDE** (hermético, ponto único), CI ativa, `contracts/circuit_breaker/cost_tracker/pipeline_state` existem, segredos isolados, orquestrador idempotente. **Mas a conformidade ainda é parcial** — 5 gaps concentrados. O mais grave: **código novo (a stack de som desta sessão) entrou SEM teste**, violando "nada entra sem teste verde".

## Rúbrica (PASS/FAIL por pilar)
| Pilar | Veredito | Evidência-chave |
|---|---|---|
| 1 Planejar antes | PASS (parcial) | tarefas atômicas; falta critério de aceite escrito p/ módulos novos |
| 2 **TDD** | **PARCIAL→FAIL** | testar.py verde (182), mas `dsp/marca_sonora/efeitos_transicao/youtube_pos/sincronizar` SEM teste (funções puras, testáveis) |
| 3 Humano decide o quê | PASS | matriz de autoridade em `PUBLICACAO-YOUTUBE.md` |
| 4 **Refatoração/DRY** | **FAIL** | `_token/_page_id/_post` FB copiados 4–5×; `_refresh/_get/_user_id` IG 2×; `HASHTAGS_BASE` 6×; sem `facebook_base/ig_base`; postadores ignoram `net.py` |
| 5 **CI + ambiente** | **FAIL** | CI só roda unittest (ruff configurado em pyproject mas NÃO ligado; sem segurança); **`requirements.txt` runtime AUSENTE** (7 deps core não declaradas) |
| 6 Constituição | PARCIAL | módulos novos em `ESTUDIO-AGENTES.md`, não no `CLAUDE.md`; 3D/cost_tracker/breaker sem contrato de interface |
| 7 Auditoria automática | PARCIAL | VPS cron (`ig_runner_vps` */15) ✅; LOCAL `auditoria.bat` existe mas **NÃO agendado** |
| 8 Isolamento | PASS (ressalvas) | segredos isolados ✅; `tokens.py` (nome ambíguo, sem segredo); `gerar_video` roda fora do orquestrador |
| 9 **Clean code** | **PARCIAL→FAIL** | `gerar_video.py` 689 + `instagram_post.py` 524 (>500); 4 colisões de nome (`caption_for` ×3); indentação 10 níveis em instagram_post; 29 `def main` |

## Resiliência aplicada (pilares 4/8 — detalhe)
- **COM** breaker/cost: `imagen.py`, `veo.py`, `tts_gcloud.py`, `upload_youtube.py` ✅
- **SEM** proteção: **`falgen.py`** (Flux+Kling, o cliente mais caro — zero breaker/retry/cost), ElevenLabs em `gerar_video.py`, e TODOS os postadores (tiktok/instagram/facebook) usam `urllib` cru, ignorando `net.py`.
- `contracts.load_roteiro` está em `try/except` que **só avisa** — valida mas não bloqueia (roteiro inválido gasta API antes de falhar).

## Backlog priorizado (rumo à conformidade)
| Ordem | Gap | Ação atômica | Risco | Gate (verde=exit) |
|---|---|---|---|---|
| 1 | env não reproduzível | `videos/requirements.txt` (7 deps) + ligar no `ci.yml` | nulo | `pip install` limpo |
| 2 | **som novo sem teste** | `test_dsp/test_marca_sonora/test_efeitos_transicao/test_youtube_pos/test_sincronizar` (funções puras) | baixo | `testar.py` verde |
| 3 | CI incompleta | step `ruff check` + `pip-audit` no `ci.yml` | baixo | CI verde |
| 4 | falgen/contracts | breaker+retry+cost em `falgen`; `contracts` vira guarda (fora do try) | baixo | teste novo |
| 5 | DRY postadores | extrair `facebook_base.py` + `ig_base.py`; rotear via `net.py` — **só DEPOIS de cobrir com teste** | ALTO | `test_facebook_base` antes |
| 6 | arquivos >500 | dividir `gerar_video`(→ `_video_slides`/`_video_tts`) e `instagram_post`(→ `ig_carousel`) | médio | `testar.py` verde |
| 7 | nomes colidentes | renomear `caption_for/post_reel/postar_reels` por plataforma | baixo | `testar.py` verde |
| 8 | constituição/auditoria | contratos dos módulos novos no `CLAUDE.md`; agendar `auditoria.bat` (schtasks) | nulo | — |

## Pronto = lane Akita-conforme quando
`testar.py` cobre **todo módulo de produção não-trivial** · CI roda **lint+segurança+testes** com **env reproduzível** · `falgen` e postadores protegidos por **breaker** · **zero duplicação** de auth entre postadores · **nenhum arquivo >500 linhas** · auditoria local **agendada**. Enquanto qualquer um faltar, a lane é "Akita de forma, não de substância plena".

> Execução em modo `loop-agente`: tarefas atômicas, uma por vez, cada uma com TDD (verde = exit code de `testar.py`). Refatores de risco (ordem 5–6) exigem teste-rede ANTES. Commit é da lane **GitGuy** (não desta sessão).

## Progresso — execução loop-agente (2026-06-20, mesma sessão)
- ✅ **#1 env:** `videos/requirements.txt` criado (7 deps de runtime declaradas).
- ✅ **#2 testes:** `test_dsp` (10) + `test_marca_sonora` (21) + `test_efeitos_transicao` (23) + `test_youtube_pos` (39) + `test_sincronizar` (40) → **`testar.py` 182 → 315 VERDE**. 4 escritos por subagentes (Sonnet, auto-verificados); gate unificado por Opus. Fecha a violação "código novo sem teste".
- ✅ **#3 (parte):** `ci.yml` agora instala `requirements.txt` (rodava sem numpy → teria quebrado). **Gate ruff/segurança DEFERIDO** por contrato do `pyproject.toml` ("reformat em massa = 1 commit único do GitGuy; master nunca nasce vermelha"); **35 issues reais F/B** (13 imports não-usados, 7 raise-sem-from, 6 zip-sem-strict, 7 f-string-vazia, 2 outros) logados p/ esse commit.
- Achados menores (NÃO-bugs): `build_chapters` aceita 1º cap em ≤0.5s como "0:00" (tolerância); `marca_sonora` s03/s06 têm pico bruto 2.0–2.5 antes do `_norm` (normalizado antes do disco — inofensivo).
- ✅ **postadores cobertos:** `test_tiktok_post` (19) + `test_facebook_post` (28) + `test_instagram_post` (35) → **`testar.py` 315 → 397 VERDE**. Fixou `caption_for`/`_afiliado_block`/`_token`/`_page_id`/`_post`/`HASHTAGS_BASE`; **confirmado IDÊNTICO** na família FB → a extração DRY (#5) agora tem **rede de teste** = segura.
- ⏸️ **GATEADOS (decisão humana — Akita pilar 3 / doutrina do projeto):** #5 DRY (`facebook_base`/`ig_base`) — agora **DESBLOQUEADO** (testes prontos), aguardando go; #4 contracts-vira-guarda (muda comportamento de erro — verificar roteiros antes); #6 dividir `gerar_video`(689)/`instagram_post`(524); #8 `schtasks` (config persistente do host); reformat ruff em massa (lane do GitGuy). `falgen`-breaker é seguro mas baixo valor (provider dormente).

## Finalização — `/akita /loop-agente` (2026-06-20, 2ª rodada, fan-out disjunto)
Onda 1 (4 subagentes, arquivos disjuntos) + Onda 2 (2 subagentes) + doc. `testar.py` **180 → 446 VERDE** (exit 0). Cada onda com gate unificado + revisão de diff (Opus).
- ✅ **#4/#5 DRY (pilar 4 FAIL→PASS):** `facebook_base.py` + `ig_base.py` extraídos; `_token/_page_id/_post` (FB) e `refresh/token/user_id` (IG) agora em UM lugar (era 5×/2× → 1×). FB completado na onda 2 (delegação + mock re-apontado p/ `facebook_base`).
- ✅ **Resiliência (pilar 8):** `falgen` (Flux+Kling, o cliente mais caro) ganhou `@retry`+`@circuit_breaker`+`record_cost` (+10 testes); `contracts.load_roteiro` virou **guarda dura** nos callers (22/22 roteiros validados ANTES; +3 testes).
- ✅ **#6 clean-code (pilar 9 file-size FAIL→PASS):** `gerar_video.py` 689→**454** (extraiu `_video_tts.py`+`_video_audio.py`, +30 testes); `instagram_post.py` **498** (<500 pós-dedup → split dispensado).
- ✅ **Constituição (pilar 6):** contratos dos módulos novos gravados no `CLAUDE.md` (auth única, resiliência, guarda, som procedural).
- ⏸️ **Resta (fora do meu alcance por contrato):** (a) gate `ruff`+`pip-audit` na CI = **reformat em massa do GitGuy** (35 bugs F/B logados); (b) agendar `auditoria.bat` local = **schtasks (config persistente do host)** — comando pronto, aguarda OK do André; (c) nomes namespaced (`caption_for`×3) = resíduo menor (não é o caso egrégio do §9).
- 🐞 **Bug pré-existente achado (flagado p/ fix próprio):** `_video_audio.sintetiza_ambiente` estoura com `dur<11s` (slice `out[:fi]`, `fi=4·SR`). Nunca dispara em produção (trilha é do vídeo inteiro), mas é landmine.
