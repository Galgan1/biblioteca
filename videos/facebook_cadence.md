# Cadência do Facebook — Minuto Real (wave-sync)

Especificação da **cadência de publicação do Facebook** em sincronia com os
outros canais do Minuto Real. A fonte de verdade é o
[`facebook_cadence.json`](./facebook_cadence.json); este documento explica a
lógica e como o orquestrador deveria consumi-lo depois (sem implementar a
integração — só descrever).

## Contexto

Toda semana entra **1 livro novo**, que já é transformado em:

- **1 vídeo longo** (resumo ~5 min) — vai ao YouTube (grade: longo qua/qui 19h).
- **4 Shorts** (cenas-herói verticais) — `_shorts/<slug>_NN.mp4`.
- **1 carrossel** (mesmas imagens do Instagram).

O Facebook **hoje só posta o link do YouTube** — o que o algoritmo penaliza,
porque tira o usuário da plataforma. Esta cadência corrige isso: o Facebook
passa a **reaproveitar nativamente** o que já foi produzido, sem re-renderizar
nada só para ele.

## Princípios codificados

1. **Nativo primeiro.** Vídeo nativo, Reels e carrossel — formatos que ficam
   dentro do Facebook. Link some do corpo do post.
2. **Link só esporádico e no 1º comentário.** No máximo 1x/semana (no vídeo
   nativo de segunda), e mesmo assim o link vai no **primeiro comentário**,
   nunca no corpo.
3. **Espalhar ao longo da semana.** Um formato por dia, de segunda a sexta —
   nada de despejar tudo de uma vez.
4. **Reaproveitar ativos já produzidos.** Short → Reel, carrossel → carrossel,
   longo → vídeo nativo. O Facebook não gera ativo novo.
5. **Acompanhar a onda do YouTube.** O Reel de quarta sai às 19h, no mesmo
   horário do longo no YouTube, para reforçar o alcance da semana.

## A semana (5–6 slots)

| Dia     | Hora  | Formato       | Ativo reaproveitado            | Link |
|---------|-------|---------------|--------------------------------|------|
| Segunda | 20:00 | Vídeo nativo  | `<slug>.mp4` (longo)           | 1º comentário |
| Terça   | 12:00 | Reel          | `_shorts/<slug>_01.mp4`        | não  |
| Quarta  | 19:00 | Reel          | `_shorts/<slug>_02.mp4`        | não  |
| Quinta  | 12:00 | Carrossel     | `carrossel/<slug>/`            | não  |
| Sexta   | 19:00 | Reel          | `_shorts/<slug>_03.mp4`        | não  |

Cobertura semanal: **1 vídeo nativo do longo + 3 Reels (cenas-herói) + 1
carrossel**. Nenhum post de link no corpo.

> Os números dos Reels (`_01`, `_02`, `_03`) são as **3 primeiras cenas-herói**
> do livro, não os índices brutos de cena. Os arquivos reais em `_shorts/` usam
> o índice de cena (ex.: `padrao-bitcoin_02.mp4`, `_04`, `_05`, `_08`), então o
> orquestrador mapeia "1ª/2ª/3ª cena-herói disponível" para os arquivos
> existentes. O 4º Short pode ficar de reserva (boost ou repost futuro).

## Como o orquestrador deveria consumir (futuro — descrição, não implementação)

1. **Resolver o slug da semana.** Ler o livro corrente em
   `canal-state.json` (`upcoming_schedule[].slug`) e usá-lo para substituir
   `<slug>` em cada `fonte`.
2. **Ancorar a semana.** Tomar a data do longo (qua/qui 19h) como âncora e
   distribuir os slots de FB de segunda a sexta da mesma semana, no fuso
   `America/Sao_Paulo`.
3. **Verificar ativos antes de agendar.** Para cada slot, confirmar que o
   arquivo em `fonte` existe (longo `<slug>.mp4`, Reels mapeados das cenas-herói
   em `_shorts/`, carrossel). Slot sem ativo pronto é **pulado** — nunca trocar
   por link de substituição.
4. **Publicar nativo via Graph API.** Vídeo nativo / Reels via endpoints de
   vídeo da Página; carrossel como álbum de fotos. Reaproveitar o token e o
   `fb_page` já registrados em `canal-state.json`
   (`lanes.instagram.fb_page`).
5. **Aplicar a regra do link.** Só o slot com `link_no_comentario: true`
   (segunda) recebe link — postado como **primeiro comentário** após o vídeo
   subir, não no corpo. CTA da legenda convida ao comentário fixado.
6. **Registrar estado.** Gravar o id do post por peça (padrão já usado nos
   `_shorts/<slug>_facebook_state.json`) para idempotência e para alimentar a
   planilha de metadados.

Tudo isto é **especificação**. A implementação (script de agendamento /
publicação do Facebook que lê este JSON) fica para uma etapa posterior.
