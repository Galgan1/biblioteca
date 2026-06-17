# Instagram — Diagnóstico (Akita · Etapa 1) · Minuto Real

> Estado real de @minutoreal1701 medido contra o `INSTAGRAM-PLANO-ALVO.md`. Grounded no código (`instagram_post.py`, `coletar_datas.py`), `canal-state.json`, assets e `.secrets/`. Etapa 1 = "planejar antes": ver onde estamos antes de executar.

## Matriz gap (frentes do plano-alvo)

| Frente | Estado | Evidência |
|---|---|---|
| **1. Setup/posicionamento** | **PARCIAL** | conta Creator + bio + rótulo IA + foto OK (lane `active`, `ig_id` em canal-state); **link da bio FALTA** (mobile, pendente desde jun) |
| **2a. Reels** | **ATENDE** | `post_reel`/`postar_reels`; 5 livros postados (`_shorts/*_instagram_state.json`) |
| **2b. Carrossel** (campeão de saves) | **PARCIAL** | `post_carousel`+`caption_carousel` existem e assets gerados (1984: overview+9 caps), mas **sem evidência de publicação** (exige `--publish`; sem state de carrossel) |
| **2c. Stories** | **PARCIAL** | `post_story` existe; cadência diária + link sticker **não operacionalizados** |
| **3. Séries-assinatura** | **FALTA** | nada de "1 Livro 1 Ideia"/"Mito×Verdade" definido ou automatizado |
| **4. Cadência** (3–5/sem + stories diário) | **PARCIAL** | posta por livro sob demanda; ritmo semanal + horários BRT não codificados/agendados |
| **5a. Afiliado Amazon** | **ATENDE** | `_amazon_url` só /dp//gp/ (rejeita busca) + `_afiliado_block` + disclosure; hashtags = 3 de nicho |
| **5b. Bio agregador (3 links)** | **FALTA** | sem YouTube/Amazon/newsletter estruturados |
| **5c. ManyChat comment-to-DM** | **FALTA** | nenhum módulo/integração (a jogada de maior conversão do plano) |
| **5d. CTA falado → YouTube** | **PARCIAL** | legenda tem CTA; "CTA falado no Reel + não citar YouTube na legenda" não é regra de produção ainda |
| **6. Medição (saves/sends)** | **FALTA** | coletor puxa conta+mídia, mas **insights gated** por `instagram_manage_insights` (provável ausência, igual ao FB) → a **estrela-guia (sends+saves) não é medível**; sem UTM no link |

## GAP Nº1 — funil e medição (alcançamos, mas não convertemos nem medimos)
Produzimos e postamos Reels, mas faltam as **duas pontas que dão ROI**: (a) a **camada de conversão** — link na bio + agregador + **ManyChat "comente LIVROS"** (12–23% vs 2–4%) + Stories com link sticker; e (b) a **medição da estrela-guia** — sends/saves dependem do escopo `instagram_manage_insights` (ausente). Sem isso, o plano-alvo não fecha o ciclo IG→YouTube→Amazon nem sabe o que funciona.

## Gaps priorizados
| Sev | Gap | Caminho |
|---|---|---|
| ALTA | Link da bio ausente (entrada do funil) | mobile (suas mãos) — agregador com 3 links |
| ALTA | Insights sem permissão → estrela-guia não medível | adicionar `instagram_manage_insights` no token (App Review / re-consent) |
| ALTA | ManyChat comment-to-DM não existe | montar fluxo + palavra-chave "LIVROS" (conta ManyChat) |
| MÉDIA | Carrossel gerado mas subpublicado | publicar os carrosséis (`--publish`) — campeão de saves, custo zero |
| MÉDIA | Séries-assinatura + cadência não operacionalizadas | definir grade semanal + automatizar no orquestrador |
| BAIXA | UTM no link da bio; CTA falado como regra | UTM `?utm_source=instagram`; regra no roteiro |

## Pontos fortes (não mexer)
- **Ferramental cobre os 3 formatos** (Reels/carrossel/Stories) — raro; a base técnica está pronta.
- **Doutrina de afiliado e hashtags já no código** (produto-only, disclosure, 3 de nicho).
- **Secrets de API presentes** (token + refresh + user_id) — publicar funciona.

## O que isto destrava
- A execução do plano-alvo é, na prática: **(1) link/agregador na bio → (2) escopo de insights → (3) ManyChat → (4) publicar carrosséis → (5) séries+cadência.** As 3 primeiras precisam das suas mãos/credenciais; as 2 últimas são código/automação.
