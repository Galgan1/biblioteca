# N3 — Auditoria: "Contratos de módulo — lane de vídeo (`videos/`)"

**Alvo:** `CLAUDE.md` linhas 100-109 (seção `## Contratos de módulo — lane de vídeo (videos/)`).
**Método:** Akita — verde = exit code / evidência file:line. Read-only. pt-BR.
**Data:** 2026-06-20.

## Veredito por contrato

| # | Contrato (CLAUDE.md) | Veredito | Evidência |
|---|---|---|---|
| 1a | `facebook_base.py` define `token`/`page_id`/`post`, `GRAPH`, `HASHTAGS_BASE` | **CONFERE** | `facebook_base.py:31` GRAPH, `:32` HASHTAGS_BASE, `:38` token, `:48` page_id, `:55` post |
| 1b | `ig_base.py` define `read_token`/`refresh_token`/`read_user_id` | **CONFERE** | `ig_base.py:23` refresh_token, `:58` read_token, `:84` read_user_id |
| 1c | Postadores IMPORTAM da base e NÃO redefinem `_token/_page_id/_post` (só wrapper fino) | **CONFERE** | importam: `facebook_post.py:25-26`, `facebook_comment.py:20`, `facebook_carrossel.py:27`, `facebook_reels.py:31`, `facebook_video.py:36`, `instagram_post.py:35`, `analytics_ig.py:15`. Wrappers finos que só passam o `*_FILE`: `facebook_post.py:37-46`, `instagram_post.py:119-134`, `analytics_ig.py:32-42`. Carrossel/reels/video usam `import as` (sem redefinir) `facebook_carrossel.py:29`, `facebook_reels.py:33` |
| 2 | Resiliência `@retry`+`@circuit_breaker(api=)`+`record_cost(api=)` em `imagen/veo/tts_gcloud/upload_youtube/falgen` | **DRIFT (parcial)** | ver tabela abaixo |
| 3 | Som: existem `dsp.py`, `marca_sonora.py`, `efeitos_transicao.py`, `_video_audio.py`, `_video_tts.py` com `sintetiza_ambiente`/`_to_ssml`/`place_marca` | **CONFERE** | os 5 arquivos existem; `_video_audio.py:13` sintetiza_ambiente, `_video_tts.py:130` _to_ssml + `:151` tts, `efeitos_transicao.py:65` place_marca |
| 4 | `gerar_video.py` orquestrador fino (< 500 linhas) + delega som a `_video_audio`/`_video_tts` | **CONFERE** | `wc -l` = **454** (< 500); delega: `gerar_video.py:15` (`from _video_tts import ...`), `:16` (`from _video_audio import sintetiza_ambiente`) |
| 5 | `contracts.load_roteiro` é guarda dura nos callers `gerar_video`/`upload_youtube` (fora do try/except, só `ImportError` silenciado) | **CONFERE** | `gerar_video.py:298-304` (try só import; `load_roteiro` no `else`, sempre roda), `upload_youtube.py:75-81` (idem). `contracts.py:130` define `load_roteiro` |

### Detalhe do contrato 2 — resiliência por cliente de API

| Módulo | `@retry` | `@circuit_breaker(api=)` | ordem (retry FORA) | `record_cost(api=)` | Veredito |
|---|---|---|---|---|---|
| `imagen.py` | ✅ `:27` | ✅ `:28` | ✅ retry acima | ✅ `:48` | **CONFERE** |
| `tts_gcloud.py` | ✅ `:24` | ✅ `:25` | ✅ retry acima | ✅ `:39` | **CONFERE** |
| `falgen.py` | ✅ `:43`,`:66` | ✅ `:44`,`:67` | ✅ retry acima | ✅ `:60`,`:84` (`_record_cost`) | **CONFERE** |
| `veo.py` | ❌ **ausente** | ✅ `:22` | — (falta retry) | ✅ `:67` | **DRIFT** |
| `upload_youtube.py` | ❌ **ausente** | ✅ `:101` | — (falta retry) | ✅ `:144` | **DRIFT** |

> Nota: `veo.py:14` e `upload_youtube.py` importam o fallback de `retry`, mas a função real (`animate`/`upload`) **não é decorada** com `@retry`. `upload_youtube.py:25` sequer importa `retry` (só `circuit_breaker`).

## DRIFTs encontrados (com severidade)

### D1 — `veo.py`: falta `@retry` em `animate()` · MÉDIA
- **Onde:** `videos/veo.py:22` — só `@circuit_breaker(api='google_veo', ...)`, sem `@retry`.
- **Contrato violado:** linha 105 do CLAUDE.md ("Decore `@retry(...)` (fora) + `@circuit_breaker(api=...)` (dentro) — NESSA ordem … Já vale p/ imagen/veo/tts_gcloud/upload_youtube/falgen").
- **Severidade MÉDIA:** Veo é a API mais cara/lenta (image-to-video); sem retry, um soluço transitório (429/5xx) já abre o breaker e mata a cena. As irmãs (imagen/tts/falgen) têm retry.

### D2 — `upload_youtube.py`: falta `@retry` em `upload()` (e nem importa `retry`) · MÉDIA
- **Onde:** `videos/upload_youtube.py:101` (`@circuit_breaker` sozinho) e `:25` (import só de `circuit_breaker`, sem `retry`).
- **Contrato violado:** linha 105 (mesma do D1).
- **Severidade MÉDIA:** upload é resumable e suscetível a falhas de rede; sem retry, falha transitória derruba a publicação inteira.

### D3 (observação, não bloqueante) — `facebook_insights.py` redefine `_token/_page_id` sem usar `facebook_base` · BAIXA
- **Onde:** `videos/facebook_insights.py:42` (`_token`) e `:49` (`_page_id`) — leitura própria de `.secrets`, NÃO importa `facebook_base` (declara `GRAPH/PAGE_TOKEN_FILE/PAGE_ID_FILE` locais em `:37-39`).
- **Por que NÃO é DRIFT do contrato 1c:** o contrato nomeia os *postadores* (`facebook_*` que escrevem, + `instagram_post`/`analytics_ig`); `facebook_insights.py` é read-only (GET via `net`), não posta, e tem semântica diferente (retorna `None` em vez de `sys.exit`). Fora da letra do contrato.
- **Severidade BAIXA:** é duplicação de leitura de segredo (DRY/pilar 4). Candidato a unificação futura (ler via `facebook_base.token`/`page_id` com variante "soft"), mas o contrato atual não o cobre — corrigir a redação OU o código, decisão do dono da lane.

## Correções sugeridas

**Opção A — alinhar o código ao contrato (preferida; o contrato é o norte):**
1. `veo.py`: adicionar `@retry(max_attempts=2, base_s=3.0)` ACIMA do `@circuit_breaker` em `animate()` (`:22`); garantir `retry` no import real (já tem fallback `:14`). 2 tentativas (não 3) por ser cara/lenta — alinha com os timeouts de 600s.
2. `upload_youtube.py`: importar `retry` (junto de `circuit_breaker` em `:23-26`) e decorar `upload()` (`:101`) com `@retry(max_attempts=2, base_s=3.0)` ACIMA do breaker.
3. Ambas as correções nascem com teste hermético (mock que falha 1x → sucesso no retry), por `videos/tests/` (contrato linha 109).

**Opção B — corrigir a redação do CLAUDE.md (só se houver decisão de NÃO pôr retry em veo/youtube):**
- Linha 105: remover `veo` e `upload_youtube` da lista do `@retry`, deixando só `imagen/tts_gcloud/falgen`; manter `@circuit_breaker`+`record_cost` para os 5. Justificar o porquê (ex.: upload já é resumable; Veo tem polling próprio).

**Para D3 (opcional):** decidir entre (a) `facebook_insights.py` passar a usar `facebook_base` com helper soft, ou (b) a redação do contrato 1c explicitar que só cobre módulos de *escrita*.
