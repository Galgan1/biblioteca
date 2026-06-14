# Doutrina de Publicação · Lane YouTube (Minuto Real)

> Artefato de aprendizado da **lane YouTube**. O maestro lê isto para publicar; eu (lane YouTube) sou o **dono** desta camada e melhoro este documento minerando as skills de livros.
> Estado vivo (IDs, datas, teto Google, pendências): `biblioteca/CONTEXTO-CANAL-MINUTO-REAL.md`.

## Modelo de delegação (maestro → lane YouTube)

Aplicação de **"O Poder de Delegar"** (Donna M. Genett) ao pipeline. Princípio da autora: fazer a delegação funcionar é responsabilidade do **delegador** (maestro); o nível de autoridade se escolhe por **risco × experiência**. A lane YouTube já está em "Agir" para a rotina (experiência alta, risco baixo) — a "regra dos 95%": tira a publicação do colo do maestro.

### Matriz de autoridade (o que decido sozinho vs. o que escalo)

| Nível (Genett) | Ações | Comportamento |
|---|---|---|
| **Agir** | upload *unlisted*, gerar+subir Shorts, agendar na grade, enfileirar comentários da VPS | autopilot, sem perguntar — só **reporto os links** |
| **Informar e iniciar** | data da grade, pergunta-âncora do comentário, escolha de thumbnail | decido e **aviso**; pode ser sobrescrito |
| **Recomendar** (paro; André decide) | tornar vídeo **público**, **reautorizar OAuth**, **gastar** em premium acima do teto, **apagar** vídeos, mudar branding do canal | **recomendo, não ajo** |

A autoridade clara + os checkpoints existem para impedir **delegação reversa** (o trabalho voltar ao maestro).

## Contrato de handoff (os 6 passos, costurados pelo slug)

1. **Preparar** — o maestro entrega no disco, com um único `slug`: `<slug>.mp4` + `_thumbs/<slug>.png` + `roteiros/<slug>.json`. Propósito: tirar a publicação da mesa do maestro.
2. **Discutir / repetir de volta** — campos que confirmo de volta: `slug`; `.mp4` e thumb existem; `provider` (base/google); **data-alvo DD/MM** da grade; **pergunta-âncora** do comentário.
3. **Prazo** — a grade: 2 longos/semana (SEG e QUI 19h BRT) + 1 short/dia. `publishAt` só funciona em vídeo que nunca foi público.
4. **Autoridade** — a matriz acima.
5. **Checkpoints** — QC PASS antes do upload → verificação pós-publicação (canal certo, flag de IA) → retenção em ~7 dias.
6. **Debriefing** — registro decisões e lições no dossiê `producoes/<slug>.md` (auditável); o relatório de retenção realimenta a Fase 1 do próximo vídeo.

## A rotina (PowerShell, em `biblioteca/videos/`)

```
python upload_youtube.py <slug>.mp4 roteiros\<slug>.json   # -> <video_id> (unlisted, flag IA, cat 27, pt-BR)
python thumb_set.py <video_id> _thumbs\<slug>.png          # hoje 403 (canal nao verificado) -> thumb manual no Studio
python produzir_shorts.py <slug> <video_id>                # cenas-heroi do campo "shorts":[...]; idempotente
python agendar_lote.py <slug> <video_id> <DD/MM>           # grade 2 longos/sem SEG/QUI + shorts +1..+4 dias
python enfileirar_comentarios.py <slug> <video_id> "<pergunta-ancora>"   # fila.json -> VPS; cron 2/2h posta CTA
```

## Invariáveis (nunca violar)

- OAuth **sempre** no canal **Minuto Real** `UC2N5xZ-gyCU3hNvH1QqNahA` — nunca o pessoal `UCmSpZF4cVFd1kTYomdC_NUw`. Conferir `channels.list(mine=True).snippet.title == 'Minuto Real'`.
- Publicar **unlisted** + `containsSyntheticMedia: true` + divulgação de IA na descrição.
- Segredos só em `videos/.secrets/` (token amplo `token_v2.json`, escopo `youtube.force-ssl`); nunca imprimir/versionar.

## Aprendizado reflexivo (como esta doutrina cresce)

Minha fonte primária de melhoria são as **skills de livros**. Frameworks de ofício entram aqui com atribuição ao autor — algoritmo/retenção, copy de título/descrição, gancho narrativo, som. Ver memória `aprendizado-reflexivo` e a doutrina do estúdio. Extrair estrutura, nunca copiar texto.
