# Playbook Premium — Facebook (Página "Minuto Real")

> **Canal Minuto Real** · resumos de livros · pt-BR · divulgação de IA obrigatória
> Página FB `1225638803958838` (vinculada a @minutoreal1701) · custo de produção **zero** (reusa os assets do Instagram)
> Framework de base: **Marketing 4.0** (Kotler/Kartajaya/Setiawan) — 5 As · Fator-F · Zona O · 4 Cs · PAR/BAR.
> Irmão do `videos/PLANO-INSTAGRAM.md`. Última atualização: 2026-06-15

---

## 0. Premissa central — como o algoritmo do FB realmente trata o que postamos

Tudo aqui parte de uma realidade que não negociamos com o feed:

- **Post com link externo é rebaixado** — e link de **YouTube** (concorrente direto do Reels/Watch) é o mais punido de todos. Um post-link entrega o **pior alcance** da plataforma.
- **O FB empurra Reels** para brigar com o TikTok. Reel nativo é hoje a **superfície de maior alcance orgânico** da Página — de longe.
- **Conteúdo que mantém a pessoa na plataforma vence**: vídeo nativo e carrossel nativo (mídia hospedada na própria Página) > qualquer post-link.
- **Tática premium (a regra de ouro deste playbook):**
  > Post **nativo** (Reel / vídeo / carrossel) com **legenda SEM link no corpo** + o link (YouTube/site) no **PRIMEIRO COMENTÁRIO**.

Em linguagem de Kotler: deixamos a **Zona O** (others' opinion / comunidade) e a **própria experiência** carregarem a descoberta. O algoritmo só nos dá alcance se entregarmos retenção — e retenção é o que o Reel nativo faz. O link no comentário continua servindo a **Ação** (descida ao YouTube/acervo) sem pagar o pedágio de alcance do post-link.

---

## 1. Diagnóstico do estado atual (e por que está errado)

**Hoje, na prática:** a Página posta basicamente **post-link do vídeo longo do YouTube** (é o que o `facebook_post.py` faz por padrão: `/{page}/feed` com `link=youtu.be/...`). É **manual**, **um formato só**, e **sem medição**.

| Sintoma atual | Por que está errado (lente Kotler / algoritmo) |
|---|---|
| Só post-link do YouTube | É o formato **mais rebaixado** do FB; e link de concorrente é o pior. Estamos publicando exatamente o que o feed mais pune. |
| Formato único | Não cobre os 5 As — só tenta a **Ação** direto, pulando **Assimilação** e **Atração**. Sem alcance no topo, ninguém chega na Ação. |
| Manual | Sem cadência ⇒ sem o ritmo que o algoritmo recompensa; e rouba tempo que deveria ser zero (os assets já existem). |
| Sem medição | Não dá pra calcular **PAR/BAR** nem saber qual gancho funciona. Otimização vira achismo. |

**Resumo:** estamos investindo 100% no formato de pior alcance, ignorando o de melhor alcance (Reels), sem dado nenhum. Os scripts premium **já existem** (`facebook_reels.py`, `facebook_carrossel.py`, `facebook_comment.py`) — falta **virar a chave de doutrina** de "post-link" para "nativo + link no comentário".

---

## 2. O play premium — reaproveitar 100% dos assets do Instagram (custo zero)

Nada se produz a mais para o Facebook. Cada peça do FB é o **mesmo arquivo** já feito para o IG/YouTube, costurado pelo `slug`:

| Ativo já produzido | Fonte / caminho | Vira no Facebook | Script |
|---|---|---|---|
| **Shorts 9:16** | `videos/_shorts/<slug>_NN.mp4` | **Reel nativo** (maior alcance) | `facebook_reels.py <slug>` |
| **Carrossel verde** | `videos/_carrossel/<slug>_overview/NN.png` | **Carrossel de fotos nativo** | `facebook_carrossel.py <slug>` |
| **Vídeo longo (~5 min)** | `videos/<slug>.mp4` | **Vídeo nativo** na Página (não post-link) | (subir nativo; link do YT no comentário) |
| **Citação / frase-bomba** | `roteiros/<slug>.json` (`cenas[].titulo/narracao`) | Card de citação (imagem nativa) | reusa pipeline do IG |
| **Link YouTube + acervo** | `youtu.be/<id>` + `…/biblioteca` | **1º comentário-CTA** | `facebook_comment.py <post_id> --video <id>` |

**O fluxo de cada publicação (sempre 2 passos):**
```
1) Postar NATIVO, legenda SEM link    -> facebook_reels.py / facebook_carrossel.py   -> devolve post_id
2) Comentar o link em 1º lugar        -> facebook_comment.py <post_id> --video <video_id>
```
Os scripts são **idempotentes** (estado em `_shorts/<slug>_fbreels_state.json` etc.) e têm `--dry-run`. O `facebook_post.py` (post-link) fica **só para exceção** (ex.: um anúncio puro de texto), nunca como rotina.

---

## 3. Mix de formatos e cadência semanal (wave-sync com YouTube/IG)

A grade orbita o YouTube — **longos QUA e QUI, 19h BRT** (`canal-state.json`). O FB **aquece** com nativo; o longo **converte**. Horários em BRT, deslocados ~1h dos do IG para não competir com a própria audiência.

| Dia | Formato FB (nativo) | Fonte | Horário | Fase (5 As) | Link no 1º comentário |
|---|---|---|---|---|---|
| **SEG** | 🎬 Reel | corte do livro novo da semana | 13h | Assimilação | YouTube (canal) |
| **TER** | 🟩 Carrossel | cheat sheet do livro da semana | 12h | Atração + Arguição | acervo (cheat sheet/PDF) |
| **QUA** | 🎬 Reel | 2º corte do livro · esquenta o longo das 19h | 13h | Assimilação | YouTube (longo das 19h) |
| **QUA 19h** | 🎬 Vídeo nativo OU Reel-teaser | longo da semana | 19h | Ação | YouTube (longo) + acervo |
| **QUI** | 🟩 Carrossel | 2º livro da semana | 12h | Arguição | acervo |
| **QUI 19h** | 🎬 Vídeo nativo OU Reel-teaser | 2º longo | 19h | Ação | YouTube (longo) |
| **SEX** | 💬 Citação | frase-bomba do roteiro | 18h | Apologia | "marca quem precisa" (sem link) |
| **SÁB** | 🎬 Reel | corte de acervo (livro antigo) | 11h | Assimilação | YouTube |
| **DOM** | 🟩 Carrossel ou 💬 Citação | acervo | 17h | Arguição/Apologia | acervo / sem link |

**Ritmo:** ~3 Reels (alcance/Assimilação) · 2 Carrosséis (salvamento/Arguição) · 1–2 Citações (compartilhamento/Apologia) · vídeo nativo nos dias de longo. **Reel é o carro-chefe.** A onda FB→IG→YouTube empurra views/inscrições para o longo na quarta e quinta à noite.

---

## 4. Regras de copy (legenda + comentário)

A legenda do **post nativo** nunca leva link. O link vai **sempre** no 1º comentário.

1. **Hook nos primeiros ~125 caracteres** — é o que aparece antes do "Ver mais". Tensão ou promessa, não título. Ex.: *"Você não está viciado em prazer. Está fugindo da dor."*
2. **Valor primeiro** — 2–4 linhas entregando a ideia destilada. O FB premia quem **fica lendo**; entregue antes de pedir.
3. **CTA sem link no corpo** — para o link, aponte para o comentário: *"Link aqui nos comentários 👇"*. (É exatamente o que `facebook_comment.py` posta.)
4. **Divulgação de IA (obrigatória):** *"Narração e arte por IA."*
5. **Hashtags de nicho — 3 a 5, nunca 30.** Fixas: `#livros #resumodelivro #leitura` + 1–2 do tema (ex.: `#dopamina #habitos`). No fim da legenda.
6. **1 post = 1 CTA.** Reel/vídeo → YouTube; carrossel → acervo; citação → "marca quem precisa" (Apologia, sem link).

**1º comentário-CTA (padrão `facebook_comment.py`):** "O link tá aqui 👇" + 🎬 YouTube (se houver `video_id`) + 📚 acervo (`…/biblioteca`) + convite a curtir a Página. O `attachment_url` gera o card de preview **no comentário**, não no post — o alcance fica protegido.

---

## 5. KPIs — o que medir e como liga aos 5 As / BAR

Nunca otimizar por *like*. As métricas dão a **PAR** (consciência → ação) e a **BAR** (consciência → apologia), que é a métrica-mestra da era conectada.

| KPI (Insights da Página) | Formato dono | Fase (5 As) | O que diz |
|---|---|---|---|
| **Alcance de Reels / contas não seguidoras** | 🎬 Reel | Assimilação | topo do funil; o motor de descoberta do FB |
| **Retenção / tempo de vídeo** | Reel + vídeo nativo | Atração | se o gancho "gruda" (entra no PAR) |
| **Compartilhamentos** | 💬 Citação | **Apologia → BAR** | Fator-F em ação (Friends/Fans empurrando) |
| **Salvamentos** | 🟩 Carrossel | Arguição | conteúdo de referência |
| **Cliques no link do 1º comentário** | CTA | **Ação → PAR** | quantos descem ao YouTube/acervo |
| **Seguidores/curtidas da Página** | todos | Atração acumulada | base que recebe alcance recorrente |

**Como ler:** o **gargalo entre duas fases** mostra onde investir. Muito alcance e pouco clique no comentário ⇒ o gargalo é Assimilação→Ação (melhorar o CTA do comentário ou o teaser). Pouco compartilhamento ⇒ BAR baixa ⇒ reforçar Citações e o Fator-F (pedir "marca quem precisa"). **Norte:** o sucesso não é seguidor, é **apologia (BAR)** — empurrar de "vi" para "compartilhei / cliquei".

---

## 6. Roadmap de implementação (por prioridade)

| Prioridade | Ação | Verificação |
|---|---|---|
| **1 — Reels nativo** | Rodar `facebook_reels.py <slug>` para os livros âncora; aposentar o post-link como rotina. | Reels publicados; alcance ≫ que post-link. |
| **2 — Link no 1º comentário** | Após cada post nativo, `facebook_comment.py <post_id> --video <video_id>`. | Comentário-CTA presente; preview no comentário, não no post. |
| **3 — Carrossel nativo** | `facebook_carrossel.py <slug> --variante overview` nos dias de Arguição. | Carrossel de fotos nativo (não link); salvamentos. |
| **4 — Vídeo longo nativo** | Subir o `<slug>.mp4` como vídeo nativo na QUA/QUI 19h; link do YT no comentário. | Vídeo nativo na Página; clique no comentário. |
| **5 — Cadência automatizada** | Encaixar os 2 passos (postar nativo → comentar) na onda do maestro, costurado pelo slug, junto da grade do IG/YouTube. | Publicação coordenada sem ação manual. |
| **6 — Medição quinzenal** | Coletar os KPIs da Seção 5 (Insights) a cada 2 semanas; identificar o gargalo de fase e **dobrar no que funciona**. | Relatório de PAR/BAR; backlog alimentado pelos ganchos vencedores. |

**Invariáveis:** sempre **nativo + link no comentário** (nunca link no corpo na rotina); divulgação de IA em toda legenda; 3–5 hashtags; segredos só em `videos/.secrets/` (`facebook_page_token.txt`, `facebook_page_id.txt`) — nunca imprimir/versionar.
