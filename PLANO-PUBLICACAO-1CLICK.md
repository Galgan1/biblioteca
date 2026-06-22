# Plano-Alvo — Publicação 1-Clique (site → VPS → 4 superfícies)

> Base Akita (planejar antes de codar; tarefas atômicas; verde = exit code). Norte: do botão no
> site da Biblioteca a YouTube(longo+Shorts) + Instagram(tudo) + Facebook(tudo), **tudo
> processado na VPS**. NÃO é "faça tudo num clique de código" — é decompor e blindar cada elo.

## Objetivo (o QUÊ — humano decide)
Um clique no site (admin) publica um livro/peça em **YouTube** (vídeo longo + Shorts) ·
**Instagram** (Reel + carrossel + stories) · **Facebook** (post-link/nativo). O **disparo** é o
clique; **todo o processamento** (cortes + uploads + chamadas de API) roda **na VPS**, não no PC.

## Restrições (invioláveis — nenhum elo quebra)
- **VPS faz o trabalho; o PC só dispara.** Idempotente: re-clique NÃO duplica.
- **Gates obrigatórios no caminho:** `canal_guard` (YT só Minuto Real, aborta no canal errado) ·
  `verificar_copy` piso duro (pt-PT/link-cru/Amazon-busca/spam) antes de cada legenda ·
  `valida_marca` nos assets visuais. Pular gate = bug.
- **Segredos só em `.secrets/` na VPS** (gitignored; nunca no chat/git).
- **GitGuy commita; o agente não.** Anti-fantasma: nenhum import órfão.
- **Modo soberano:** sem crédito externo, o caminho degrada (render → Ken Burns/edge-tts; juiz de
  copy → só piso duro) — publicar nunca quebra por falta de crédito.
- **pt-BR** sempre; Amazon só `/dp//gp/`; IG = link na BIO (legenda não clicável).

## Método (arquitetura-alvo — reusar o que existe)
```
[site/admin]  --1 clique-->  [endpoint VPS (auth)]  -->  enfileira JOB (manifest/state)
                                                              |
                          [runner VPS: publicar_tudo.py <slug>]  (cron/daemon, idempotente)
                          ├─ YouTube longo   : upload_youtube  (canal_guard, publish_in_min)
                          ├─ YouTube Shorts  : produzir_shorts (corte vertical + upload)
                          ├─ Instagram TUDO  : instagram_post (reel + carousel + story, video_url)
                          └─ Facebook  TUDO  : facebook_post (post-link; nativo a construir)
                          cada etapa: gate de copy/marca → estado (pipeline_state/events.jsonl)
                                                              |
                          [status de volta ao site]  <--  SSE/polling por superfície
```

## O que JÁ existe ✓ vs GAPS
| Peça | Existe | Gap |
|---|---|---|
| Runner na VPS | `ig_runner_vps.py` (cron, fila) | publica só o **eco IG**; falta YT+FB+IG-completo |
| Fila/estado | `sincronizar.py` (manifest), `pipeline_state`, `_shorts/*_state.json` | unificar num job de 4 superfícies |
| Publishers | `upload_youtube`, `instagram_post` (reel/carrossel/story), `facebook_post`, `produzir_shorts` | orquestrá-los num **único `publicar_tudo.py`** |
| Gates | `canal_guard`, `valida_marca`, `verificar_copy` | **plugar no caminho** do orquestrador |
| Disparo no site | Node API de IG + login multiusuário | botão **"Publicar tudo"** + endpoint agregado |
| Segredos na VPS | IG (token/app) | falta **YT `token_v2`** (Minuto Real) + **FB page token** |
| Render na VPS | local hoje (Imagen+3DGS+ElevenLabs) | **decisão**: render soberano na VPS (sem GPU) ou pré-render local |

## Decomposição em tarefas atômicas (cada uma com teste/verde próprio)
- **T0 · Levar pipeline + segredos pra VPS (FUNDAÇÃO).** Hoje só o publisher de IG vive em
  `/opt/minutoreal`. Deploy idempotente do **render soberano** (`gerar_video` + `imagen` +
  `cinegrafista` Ken-Burns + `_video_tts` edge + `mixmaster` + ffmpeg) e dos **publishers**
  (`upload_youtube`/`produzir_shorts`/`facebook_post`) + `.secrets` (YT `token_v2` Minuto Real, FB,
  IG, Imagen). Reusa `deploy_ig_vps.ps1` como base. *Verde:* `import` de cada módulo na VPS + 1
  render Ken-Burns de teste (1 cena) sem OOM.
- **T1 · `publicar_tudo.py` (VPS)** — orquestrador idempotente: `slug` → 4 superfícies, cada uma
  gateada e com estado; pula o que já foi. *Verde:* teste e2e mocando as APIs (roda as 4, 2º run = no-op).
- **T2 · Endpoint de disparo** (Node API VPS) "publicar tudo" + auth admin → cria o job. *Verde:* POST cria job; sem auth → 401.
- **T3 · Botão "Publicar tudo" + status** no site (SSE/polling, precedente viral). *Verde:* clique → job + status por superfície.
- **T4 · Segredos na VPS** — subir `token_v2` (re-auth no **Minuto Real**) + FB page token p/ `.secrets` (chmod 600). *Ação humana (OAuth).* 
- **T5 · Render — HÍBRIDO (DECIDIDO):** a VPS renderiza no soberano **Ken Burns** (ffmpeg puro +
  Imagen API + edge-tts + master) quando o asset não existe; **SEM torch/DepthFlow** (OOM sem swap)
  e **SEM 3DGS** (GPU). O **premium (3DGS/DepthFlow) é renderizado LOCAL** e a VPS **reaproveita** o
  asset pronto. *Rails obrigatórios:* criar **4–8 GB de swap**, `nice`+limite de threads no ffmpeg,
  **fila 1-job** (um render por vez), **guarda de RAM** (adia se livre < teto). *Verde:* render
  Ken-Burns na VPS roda sem derrubar as 8 APIs de produção (RAM/carga sob teto).
- **T6 · Gates no caminho** — chamar `verificar_copy --rapido` por legenda, `valida_marca` nos PNGs, `canal_guard` no YT (já existem; só costurar). *Verde:* legenda ruim/cor fora da marca → job recusa a etapa.
- **T7 · Heartbeat + ALERTA de PC offline (exigência nova).** O PC local manda heartbeat à VPS a
  cada N min (a VPS NÃO alcança o PC atrás de NAT → o PC é cliente). Quando um job pede o **premium**
  e o PC está **offline** (heartbeat velho) OU qualquer etapa **falha**, a VPS **AVISA** o operador
  e **degrada pro soberano Ken Burns** (publica mesmo assim — não trava). **Canal = TELEGRAM
  (decidido)** via `videos/notificar.py` (token+chat_id em `videos/.secrets/telegram_*`). Akita
  pilar 7: erro com contexto + alerta. *Verde:* simular PC offline → o alerta chega E o job conclui
  no soberano. (Sender `notificar.py` + teste = 1ª peça do T7, já construída.)

## Validação (o GOAL — "pronto" =)
Um clique no site → na VPS → o livro entra em **YT(longo+Shorts) + IG(reel+carrossel+story) + FB**,
cada superfície reportando **sucesso/erro**, **idempotente** (re-clique não duplica), **gates
aplicados** (copy/marca/canal), tudo **logado**. Verde mensurável = **teste e2e do `publicar_tudo`
(APIs mocadas)** provando: roda as 4 superfícies · 2ª execução é no-op · legenda reprovada bloqueia
a etapa · canal errado aborta o YT.

## Riscos (decisões abertas)
1. ~~Render na VPS sem GPU~~ **RESOLVIDO → HÍBRIDO (21/jun/2026).** Specs medidas da VPS: **2 vCPU**
   (EPYC 9354P) · **7,8 GB RAM (~4,3 livres)** · **SEM swap** · 74 GB de disco livres · **ffmpeg 7.1.1
   + Python 3.13** · já roda **8 APIs de produção** (cartório/árvore/azul…) + Puppeteer ≈3,5 GB.
   Verdito: **Ken Burns (ffmpeg) cabe** (mesma classe do `biblioteca-pdf` que já roda lá); **DepthFlow/
   torch NÃO** (OOM sem swap → mataria o cartório); **3DGS NÃO** (sem GPU). Rails obrigatórios: swap
   4–8 GB, `nice`, fila 1-job, guarda de RAM. Premium (3DGS) fica local; a VPS reaproveita o asset.
2. **OAuth YT na VPS:** re-auth headless é chato; provável gerar o `token_v2` local (no Minuto Real)
   e **subir** o arquivo pra VPS.
3. **Custo na VPS:** Imagen/ElevenLabs/Claude consomem crédito → teto + modo soberano.
4. **Rate limit / ordem:** publicar 4 superfícies de uma vez — espaçar; YT agendado, redes em eco.
```
```
