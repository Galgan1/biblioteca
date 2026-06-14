# Plano Estratégico — Instagram @minutoreal1701

> **Canal Minuto Real** · resumos de livros · pt-BR · divulgação de IA obrigatória
> Cadência agressiva (~1 post/dia + stories) · conta nova (começando do zero)
> Framework de base: **Marketing 4.0** (Kotler) — jornada dos 5 As + fator-F + marketing de conteúdo.
> Última atualização: 2026-06-13

---

## 1. Posicionamento e Funil

**Quem é a conta:** o atalho diário para a ideia central dos grandes livros. A cada dia, o seguidor leva uma ideia que muda algo — destilada, visual e em 1 minuto. Não é "dica de leitura": é a **ideia já mastigada**, com a fonte aberta para quem quiser ir fundo.

**Promessa de uma linha:** *"A ideia mais importante de um grande livro, todo dia, em pt-BR."*

**O funil (Instagram = topo de descoberta):**

```
INSTAGRAM (descoberta / 5 As)          →  CTA           →  DESTINO (link da bio = hub)
─────────────────────────────────────     ──────────       ──────────────────────────────
🎬 Reels   → ALCANCE   (Assimilação)    →  "vídeo completo" → YouTube (resumo ~5 min)
🟩 Carrossel → SALVAMENTO (Arguição)    →  "guia completo"  → Biblioteca (cheat sheet + PDF)
💬 Citação  → COMPARTILHAMENTO (Apologia) → "marca quem precisa" → comunidade (fator-F)
```

**Mapa para os 5 As do Kotler** (esta é a espinha do plano):

| Fase (Kotler) | Pilar que mais serve | Métrica-alvo |
|---|---|---|
| **Assimilação** (ser visto) | 🎬 Reels (alcance) | Alcance / contas não seguidoras |
| **Atração** (grudar) | 🟩 Carrossel + identidade visual verde | Visitas ao perfil, seguidas |
| **Arguição** (pesquisar/comparar) | 🟩 Carrossel + bio-hub | Cliques no link, salvamentos |
| **Ação** (assistir/baixar/comprar) | CTA → YouTube / Biblioteca / Amazon | Cliques no link, idas ao YouTube |
| **Apologia** (recomendar) | 💬 Citação + stories de comunidade | Compartilhamentos, repost de stories |

A métrica-mestra da era conectada é a **BAR (Taxa de Defesa da Marca)** — por isso priorizamos **salvamento, compartilhamento, cliques e alcance**, nunca like.

---

## 2. Calendário Semanal

Cadência: **1 post de feed/dia, 7 dias**, alternando os 3 pilares; stories todos os dias. Horários em **BRT**. A grade reforça o YouTube (vídeos longos **SEG e QUI, 19h**).

| Dia | Pilar (feed) | Formato | Horário | Função no funil |
|---|---|---|---|---|
| **SEG** | 🎬 Reels | Corte do vídeo-resumo do **livro novo da semana** | 12h | Assimilação + esquenta o longo das 19h |
| **TER** | 🟩 Carrossel | Destilado do cheat sheet (livro da semana) | 11h | Atração + Arguição (motor de SALVAMENTO) |
| **QUA** | 💬 Citação | Frase-bomba do roteiro | 18h | Apologia (motor de COMPARTILHAMENTO) |
| **QUI** | 🎬 Reels | Corte do **2º vídeo da semana** | 12h | Assimilação + esquenta o longo das 19h |
| **SEX** | 🟩 Carrossel | Destilado do 2º livro da semana | 11h | Arguição (SALVAMENTO) |
| **SÁB** | 💬 Citação | Frase de acervo (livro antigo) | 10h | Apologia + reaquece catálogo |
| **DOM** | 🎬 Reels | Corte de acervo (livro antigo) | 17h | Alcance no pico de domingo |

**Ritmo da semana:** 3 Reels (alcance) · 2 Carrosséis (salvamento) · 2 Citações (compartilhamento). A grade orbita o YouTube: **SEG/QUI** o feed entrega Reel ao meio-dia e o longo sai às 19h — Instagram aquece, YouTube converte.

**Stories — 2 a 4 por dia (rotina fixa):**

| Janela | Story |
|---|---|
| Manhã (~9h) | Repost do post do dia + sticker "salva aí" / "arrasta pro lado" |
| Pré-19h (SEG/QUI) | **Contagem regressiva** do vídeo longo + link "lembrar" |
| Pós-19h (SEG/QUI) | Print da abertura do vídeo + link direto pro YouTube |
| Noite (diário) | **Enquete / caixinha** ("já leu X?", "qual o próximo?") → ativação comunitária (4 Cs) |

---

## 3. Cada Pilar → Fonte de Produção

Todos os pilares são **derivados** de assets já produzidos por livro — zero criação manual nova. O slug (ex.: `nacao-dopamina`) costura tudo.

| Pilar | Fonte | Caminho | Como vira post |
|---|---|---|---|
| 🟩 **Carrossel** | cheat sheet do livro | `videos\gerar_carrossel.py` → `videos\_carrossel\<slug>_overview\NN.png` | 5–8 cards verdes destilando capítulos; último card = CTA "guia completo na bio" |
| 🎬 **Reels** | cortes do vídeo-resumo | `videos\_shorts\<slug>_NN.mp4` | corte 9:16 já renderizado; legenda gancho + CTA YouTube |
| 💬 **Citação** | frases do roteiro | `videos\roteiros\<slug>.json` (campo `narracao`/`titulo` das `cenas`) | card de citação com a frase-bomba; CTA "marca quem precisa ler" |

**Notas de produção (para os agentes de código — não é tarefa deste plano):**
- O `gerar_carrossel.py` ainda será criado; já existe precedente em `videos\_carrossel\padrao-bitcoin_overview\` (PNGs `01.png`–`05.png`).
- As frases de citação saem das `cenas[].narracao` / `cenas[].titulo` dos JSONs de roteiro — as melhores são as falas curtas e categóricas (ex.: "Querer não é gostar", "Não há prazer de graça"). Há precedente de seleção em `videos\_shorts\padrao-bitcoin_instagram_captions.md`.
- Reels reaproveitam os arquivos `_NN.mp4` já listados em `roteiros\<slug>.json` no campo `shorts`.
- Publicação via `videos\instagram_post.py` (estado por livro em `<slug>_instagram_state.json`).

---

## 4. Hashtags e Legendas

**Hashtags — 3 a 5 de nicho, nunca 30** (alinhado ao precedente já em uso):
- **Fixas da marca (sempre):** `#livros #resumodelivro #leitura`
- **+1 a 2 do tema do livro:** ex. Nação Dopamina → `#dopamina #habitos`; Padrão Bitcoin → `#bitcoin #padraobitcoin`; Arte da Guerra → `#estrategia #suntzu`.
- Colocar as hashtags **no fim da legenda** (ou no 1º comentário), nunca no gancho.

**Anatomia da legenda:**
1. **Gancho na 1ª linha** (antes do "...mais") — uma frase que para o scroll. Tensão ou promessa, não título. Ex.: *"Você não está viciado em prazer. Está fugindo da dor."*
2. **Corpo curto** — 2 a 4 linhas destilando a ideia.
3. **CTA único e claro** — varia por pilar:
   - Reels → *"Resumo completo de [Livro] no canal Minuto Real — link na bio."*
   - Carrossel → *"Salva pra não esquecer. Guia completo (cheat sheet + PDF) na bio."*
   - Citação → *"Marca quem precisa ler isso."*
4. **Divulgação de IA (obrigatória):** *"🎙 Narração e arte por IA."*
5. **Hashtags** (3–5).

**Regra de ouro:** 1 post = 1 CTA. Não competir destinos na mesma legenda.

---

## 5. Stories — Linha Editorial

- **Repost do feed** (todo dia) — com sticker de ação ("salva", "arrasta", "compartilha").
- **CTA / link** — story dedicado levando ao destino do dia (YouTube / Biblioteca / Amazon).
- **Bastidores** — "como esse resumo foi feito", recorte do roteiro, prévia do próximo livro → marketing humano (dá rosto à marca).
- **Enquetes / caixinha de perguntas** — "qual livro resumir depois?", "já leu X?" → **co-criação** e **ativação comunitária** (4 Cs); alimenta o backlog.
- **Repost de quem nos marcou** — quando aparecer (apologia / fator-F).
- **Contagem regressiva** — SEG e QUI, sticker de countdown para o vídeo das 19h.

---

## 6. Sequência de LARGADA — 2 Semanas

Objetivo: **chegar coeso já no 1º dia**. A conta abre com o feed **já montado** — publicar os 3 primeiros posts juntos (carrossel + citação + reel do mesmo livro âncora) para que o visitante encontre uma grade que "faz sentido" (Atração). Livros âncora escolhidos por apelo amplo e ganchos fortes: **Nação Dopamina** (dor universal: celular/vício), **A Arte da Guerra** (autoridade/estratégia), **Padrão Bitcoin** (curiosidade/polêmica — já tem carrossel pronto).

### Semana 1 — abre com os 3 âncoras

| Dia | Pilar | Livro | Peça |
|---|---|---|---|
| SEG | 🎬 Reels | Nação Dopamina | `_shorts\nacao-dopamina_01.mp4` (gancho do celular-agulha) |
| TER | 🟩 Carrossel | Nação Dopamina | balança prazer-dor → DOPAMINE → autovínculo |
| QUA | 💬 Citação | Nação Dopamina | "Querer não é gostar" |
| QUI | 🎬 Reels | A Arte da Guerra | `_shorts\arte-da-guerra_01.mp4` |
| SEX | 🟩 Carrossel | A Arte da Guerra | os princípios da estratégia |
| SÁB | 💬 Citação | Padrão Bitcoin | "O dinheiro molda como você encara o futuro" |
| DOM | 🎬 Reels | Padrão Bitcoin | `_shorts\padrao-bitcoin_02.mp4` |

### Semana 2 — amplia o leque (acervo + livro novo da grade)

| Dia | Pilar | Livro | Peça |
|---|---|---|---|
| SEG | 🎬 Reels | **Livro novo da semana** (grade YouTube) | corte do longo de seg |
| TER | 🟩 Carrossel | Save the Cat! | a beat sheet em cards |
| QUA | 💬 Citação | Quem Mexeu no Meu Queijo? | "Se você não mudar, pode desaparecer" |
| QUI | 🎬 Reels | **2º livro novo** (grade YouTube) | corte do longo de qui |
| SEX | 🟩 Carrossel | Padrão Bitcoin | reaproveita `_carrossel\padrao-bitcoin_overview` (pronto) |
| SÁB | 💬 Citação | Maquiavel Pedagogo | frase-bomba do roteiro |
| DOM | 🎬 Reels | Jornada do Escritor | corte de acervo |

**Após 2 semanas:** a conta tem ~14 posts, cobre os 3 pilares e ~7 livros, e entra no **ritmo permanente** da grade da Seção 2 (livro novo segue o calendário do YouTube SEG/QUI).

---

## 7. Métricas-Alvo e Revisão

**O que medir (nunca like):**

| Métrica | Pilar dono | Sinal |
|---|---|---|
| **Salvamentos** | 🟩 Carrossel | conteúdo de referência (Arguição) — o motor nº1 do alcance no IG |
| **Compartilhamentos** | 💬 Citação | apologia / fator-F (BAR) |
| **Cliques no link** | CTA / bio-hub | descida no funil (Ação) |
| **Alcance / não-seguidores** | 🎬 Reels | Assimilação |

**Metas de rampa (conta do zero — direcionais, não vaidade):**
- **2 semanas:** identidade visual reconhecível + primeiros salvamentos/compartilhamentos por post; rotina de stories estável.
- **30 dias:** 1+ Reel furando para não-seguidores; taxa de salvamento dos carrosséis subindo; primeiros cliques no link da bio.
- **90 dias:** padrão claro de quais livros/ganchos mais salvam e compartilham → vira insumo do pipeline de produção.

**Cadência de revisão — a cada 2 semanas:**
1. Listar os 3 posts que **mais salvaram** e os 3 que **mais compartilharam**.
2. Identificar o padrão (tema? formato do gancho? livro?).
3. **Dobrar no que funciona** — mais carrosséis/citações no estilo vencedor; alimentar o backlog com os temas que performam.
4. Cortar o que não engaja (formato, horário ou gancho) — sem apego.

**Norte (Kotler):** o sucesso não é seguidor — é a **apologia** (BAR). Toda decisão de conteúdo deve empurrar o seguidor de *"vi"* para *"salvei / compartilhei / cliquei"*.
