# Contexto do Projeto — Canal "Minuto Real" (YouTube ghost da Biblioteca)

> Documento de handoff. Captura o estado inteiro do projeto para retomada em qualquer ferramenta.
> Gerado em 2026-06-12. ⚠️ NÃO contém chaves/segredos (ficam só em `videos/.secrets/`, nunca anexar).

---

## 1. O que é o projeto

Canal de YouTube **faceless/ghost** que transforma os livros da Biblioteca (cheat sheets em www.andregalgani.com.br/biblioteca) em **vídeos-resumo cinematográficos de ~5 min**, produzidos e publicados de forma automatizada. Nome do canal: **Minuto Real**.

Modelo: cada livro → roteiro de 13 cenas → narração neural + imagens IA + movimento → upload. Estética coesa por vídeo, identidade reconhecível do canal.

**Descrição oficial do canal (YouTube → Sobre):**
> Minuto Real — grandes livros, as ideias que ficam, em minutos.
> Cada vídeo destila uma obra essencial — estratégia, filosofia, psicologia, liderança — num resumo cinematográfico de cerca de cinco minutos. Não é leitura por cima: é a espinha do livro, os conceitos que importam e as frases que sobreviveram ao tempo, com narração sóbria e imagem feita para prender.
> O bastante para dominar uma ideia poderosa hoje — e descobrir quais livros merecem a sua leitura completa.
> 📚 Acervo completo em cheat sheets: www.andregalgani.com.br/biblioteca
> 🎬 Novos resumos toda semana.
> Narração e imagens geradas por inteligência artificial.

**Slogan:** "Grandes livros. As ideias que ficam — em minutos."
**Palavras-chave do canal:** resumo de livros, resumo, livros, filosofia, estratégia, psicologia, autodesenvolvimento, liderança, literatura, conhecimento.

---

## 2. Vídeos publicados (todos unlisted)

| Livro | Versão | Link | Situação |
|---|---|---|---|
| A Arte da Guerra (Sun Tzu) | v1 edge-tts | youtu.be/jF54mM0g2Ps | **apagar** (antiga) |
| A Arte da Guerra | v2 Imagen+KenBurns | youtu.be/ezngaUm8MHc | **apagar** (antiga) |
| A Arte da Guerra | **v4** (gancho McKee + Veo + flag IA) | **youtu.be/zLqdMHJ-k8A** | ✅ versão atual |
| Maquiavel Pedagogo (Pascal Bernardin) | cinema (Imagen+Veo) | **youtu.be/QIYk743VByU** | ✅ publicado |
| Story (Robert McKee) | roteiro pronto, auditado | — | ⏸ não produzido (bloqueio de pagamento) |

**Ações do dono do canal (manuais, no YouTube Studio):** apagar v1/v2 de A Arte da Guerra; tornar vídeos públicos quando quiser; subir thumbnails custom (upload de thumb via API exige verificação extra).

**🚀 CANAL LANÇADO (12/jun):** PÚBLICOS — 2 longos (zLqdMHJ-k8A, QIYk743VByU) + 2 Shorts (BeR1z9GKygs, A3ms3ixqn74), publicados pelo Showrunner no Studio. **6 Shorts AGENDADOS** via publishAt (ficam private até a hora): 16/06 12h fEVIgIFu8og · 17/06 19h sW8KKf3-CoA · 19/06 12h xtrshk9yadA · 23/06 12h ODqa4x0uMTc · 26/06 12h gWa8BL1iZP8 · 27/06 10h eUXaxESkSCo (BRT). Regra aprendida: publishAt SÓ funciona em vídeo que nunca foi público. OAuth re-autorizado com escopo amplo (`youtube.force-ssl`, token_v2.json; antigo preservado). Thumbnail via API segue 403 (verificar canal em youtube.com/verify). Legendas p/ outras redes em `producoes/distribuicao_*.md`.

**Arte do canal pronta (arquivos):** `_canal/avatar.png` (800×800), `_canal/banner.png` (2560×1440). Thumbnails dos longos em `_thumbs/`.

**Limites de API confirmados (precisam ser manuais no Studio):**
- Thumbnail custom → 403 (canal não verificado: youtube.com/verify).
- Descrição/banner do canal → 403 (token tem só escopo `youtube.upload`; branding exige `youtube.force-ssl` = re-autorizar).
- **Avatar do canal → não existe API** (limitação do YouTube; sempre manual).
- Para automatizar descrição+banner no futuro: re-autorizar com escopo amplo (apagar `.secrets/token.json` + consentir de novo). Avatar segue manual de todo jeito.

---

## 3. O Estúdio (skill `estudio-de-producao`)

Estrutura de produção "padrão Hollywood" onde o Claude incorpora papel por papel. **4 fases, 3 gates, + 2 consultores transversais. Modo AUTOPILOT ativo.**

```
FASE 1 DESENVOLVIMENTO → GATE 1 Greenlight
FASE 2 PRODUÇÃO        → GATE 2 Protótipo
FASE 3 PÓS-PRODUÇÃO    → GATE 3 Corte final
FASE 4 DADOS & OPERAÇÕES → publica + analisa → realimenta Fase 1
```

**Papéis:** Showrunner (o André) · Dir. Ideação/Empacotamento · Pesquisadores · Roteirista Chefe · Dir. Arte · Dir. Cena · Dir. Fotografia · Gaffer · Téc. Som · Fixer · Editores Assistentes · Editor Chefe · VFX · Colorista · Designer Som · Jurídico · Cientista de Dados · **Especialista no Algoritmo do YouTube** · **Revisor de Língua Portuguesa**.

**MODO AUTOPILOT (ordem permanente):** ao pedir um vídeo, o estúdio roda tudo de ponta a ponta sem parar nos gates (viram checkpoints internos); orçamento ~US$6,50/vídeo pré-aprovado; publica unlisted; **a única resposta ao Showrunner é o link** (exceto bloqueio irrecuperável).

Arquivos da skill: `~/.claude/skills/estudio-de-producao/SKILL.md` + `references/{desenvolvimento,producao,pos-producao,dados-operacoes,algoritmo-youtube,revisor-portugues}.md` + `scripts/qc_video.py`.

---

## 4. Pipeline técnico (skill `biblioteca-video`)

Diretório: `C:\Users\User\.gemini\antigravity\scratch\biblioteca\videos\`

| Arquivo | Função |
|---|---|
| `gerar_video.py` | Pipeline principal. Seletor de **provider** (google/fal/base). Compõe slides, overlay, Ken Burns, palíndromo de movimento, trilha ambiente sintetizada (numpy), montagem ffmpeg. |
| `imagen.py` | Cliente Google Imagen 4 (imagens). |
| `veo.py` | Cliente Google Veo 3.1 (image-to-video, ~8s). |
| `falgen.py` | Cliente fal.ai (Flux + Kling 3.0). **Pronto, mas conta sem saldo.** |
| `tts_gcloud.py` | Google Cloud TTS Chirp3-HD, voz **Iapetus** (pt-BR), com retry de rede. |
| `upload_youtube.py` | Upload YouTube Data API v3 (OAuth). Já envia `containsSyntheticMedia: true`. |
| `produzir_shorts.py` | **ROTINA**: gera E sobe os Shorts-herói de um vídeo (`<slug> <video_id>`), unlisted, automático. Lê `"shorts":[i,...]` do roteiro. Funciona em cinema e base. |
| `gerar_short.py` | Corta Short vertical 9:16 de uma cena (`gerar_short.py <slug> <idx>`). Reaproveita `_img/`, re-sintetiza áudio via TTS → **R$0**. Saída em `_shorts/`. |
| `gerar_thumb.py` | Gera thumbnail 1280×720 (`gerar_thumb.py <slug> <idx> "TEXTO" "Subtítulo"`). Frame cinematográfico + texto-bomba Arial Black. Saída em `_thumbs/`. |
| `thumb_set.py` | Define thumbnail via API (`thumb_set.py <video_id> <png>`). ⚠️ exige canal verificado p/ thumb custom (youtube.com/verify) — hoje retorna 403, subir manual no Studio. |
| `roteiros/<slug>.json` | Formato do roteiro (ver §6). |
| `producoes/<slug>.md` | Dossiê de cada produção (decisões, lições). |
| `_img/`, `_motion/` | **Cache de assets pagos — nunca regenerar.** |
| `.secrets/` | Chaves de API/OAuth — **nunca versionar/anexar/imprimir.** |

**3 níveis de qualidade** (campo `provider` no roteiro):
- **base** — slides escuros + Ken Burns, sem IA externa → **R$ 0** (coberto pelo plano Anthropic, pois é só código local).
- **google** (premium/cinema) — Imagen 4 + Veo 3.1 → ~US$0,50 (só imagens) a ~US$6,50 (com 5 cenas Veo).
- **fal** — Flux 2 + Kling 3.0 via fal.ai → ~US$2,70, fatura separada do Google.

QC: `python ~/.claude/skills/estudio-de-producao/scripts/qc_video.py <slug>` (duração, cenas 12–30s, movimento real, contact sheet, níveis de áudio).

---

## 5. Skills do projeto (`~/.claude/skills/`)

- **maestro** — ponto de entrada único do pipeline ponta a ponta (livro→skill→biblioteca→vídeo→redes). Híbrido: delega a Etapa 1 (ler o livro) a um subagente e roda as Etapas 2–4 inline lendo a skill destilada. Aponta para `estudio-de-producao/references/workflow-completo.md` (não duplica o "como").
- **estudio-de-producao** — o processo criativo (quem decide o quê).
- **biblioteca-video** — a infraestrutura técnica (como executar).
- **story-screenwriting** — Story de Robert McKee (19 capítulos) = caixa de ferramentas do Roteirista Chefe.
- **maquiavel-pedagogo**, **smith-assertiveness**, e demais skills de livros = matéria-prima dos vídeos.
- **book-to-skill** — converte novos livros em skills.

---

## 6. Regras da casa (padrões acumulados — aplicar em todo roteiro)

1. **Empacotamento antes do roteiro.** Gancho = o problema do espectador, nunca contexto histórico (McKee: Inciting Incident).
2. **Narração ≤ 60 palavras por cena**, `tts_rate: 1.0` (Iapetus fala ~110–120 wpm; acima de 60 a cena passa de 30s e o QC reprova).
3. **Travessão ( — ) no lugar de dois-pontos** em texto para TTS (o sintetizador engole a pausa do `:` e cola a lista).
4. Números **por extenso**; **sem crianças** em imagem (política de geração) — usar salas vazias, objetos, silhuetas adultas.
5. **Teses do autor sempre atribuídas** ("segundo o livro", "Bernardin sustenta"); **fatos verificados** antes de gravar (fact-check). Blindagem jurídica e de credibilidade.
6. **Pontes causais entre cenas** (não lista paratática); **clímax nos últimos 30–40%**; loops de retenção.
7. Prompts de **motion ambientes/oscilatórios** (névoa, tecido, luz) — o palíndromo reverte o clipe; movimento direcional forte denuncia a reversão.
8. Texto **alterna lados** (esquerda/direita) por cena; abertura/encerramento centralizados.
9. Publicação **sempre unlisted**; flag de **mídia sintética** + divulgação de IA na descrição.
10. **Gate do Revisor de Português** antes do TTS e antes do upload; **Especialista de Algoritmo** opina no empacotamento.
11. Cache de asset pago **nunca** é regenerado sem ordem.

Formato do roteiro JSON: campos de topo `slug, titulo, autor, voz, tts_rate, acento, musica, estilo_img, provider, youtube{titulo,descricao,tags,privacidade}` + `cenas[]` com `tipo, kicker, titulo, subtitulo, img, motion, narracao`.

---

## 7. Custos e faturamento (estado atual)

- **Google** — projeto `gen-lang-client-0479315290`, conta de faturamento `01D600-51B5BC-2E333D` (BRL). Cartão funciona (cobrado ~US$13 em junho/2 vídeos). Crédito grátis GCP de R$1.771 **expirou em 18/mai/2026** quase intocado.
- **✅ DESBLOQUEADO (14/jun/2026):** o teto do Google foi liberado — Imagen 4 e Veo 3.1 voltaram a operar (probe ao vivo OK em 14/jun: Iapetus + Imagen; cinema produzido em `futebol-brasileiro` com 5 cenas Veo sem fallback). Se reaparecer o 429 RESOURCE_EXHAUSTED, levantar o teto em https://ai.studio/spend (não é pagamento novo — é um limite auto-configurado).
- **fal.ai** — chave criada e válida, mas **conta sem saldo**; cartão brasileiro recusado no top-up pré-pago. Saídas: cartão internacional virtual (Wise/Nomad/Avenue/C6 Global/Nubank intl) ou abandonar fal.
- **Anthropic** — o plano cobre o Claude (raciocínio/roteiro/direção), **não** gera imagem/vídeo (categoria de produto inexistente na Anthropic). O nível **base** é, na prática, o que o plano "cobre".

---

## 8. Próximos passos

1. **Destravar a produção do Story** — escolher: (A) levantar teto Google em ai.studio/spend [cartão já funciona]; (B) produzir o Story no nível **base** grátis agora; (C) cartão internacional p/ habilitar fal/Kling. Roteiro do Story já pronto e auditado (provider atualmente `google`).
2. Apagar versões antigas de A Arte da Guerra no Studio; tornar públicas as aprovadas; thumbnails custom.
3. **Cientista de Dados** entra ~7 dias após cada publicação com relatório de retenção → realimenta a Fase 1 do próximo vídeo.
4. Backlog de livros prontos na biblioteca (ex.: Keller-Casamento, Smith-Assertividade, Experiência Psicodélica…).
5. Formalizar a identidade do canal "Minuto Real" (arte de canal, banner, padrão de thumbnail).

---

## 9. Lições de produção já incorporadas (não repetir os erros)

- Iapetus rate 1.0 + narração ≤60 palavras evita os múltiplos rebuilds que o Maquiavel Pedagogo sofreu por estourar 30s/cena.
- "Filmes são sobre seus últimos 20 minutos" **não é de McKee** (é Wilder/Lumet) — removido do roteiro do Story no fact-check.
- A Arte da Guerra: Proposta de gancho "B" reprovada no fact-check (Batalha de Boju, 506 a.C., FOI decisiva; Sun Tzu ausente do Zuo Zhuan) — usou-se a Proposta "A" (paradoxo, sem risco factual).
- fal.ai é pré-pago e recusa cartão BR comum; Veo (Google) é nível técnico equivalente à Kling e o pagamento já funciona.


## 🤖 Automação na VPS (sempre ligada — independe do PC)
- **/opt/minutoreal/** na VPS (root@andregalgani.com.br): `comentar_pendentes_vps.py` + `upload_youtube.py` + venv (`/opt/minutoreal/venv`) + `.secrets/` (chmod 600, token_v2.json + client_secret.json, FORA da web).
- **Cron:** `17 */2 * * * /opt/minutoreal/run.sh` — a cada 2h checa quais Shorts agendados ficaram públicos e posta o comentário de CTA. Idempotente (estado em `comentarios_state.json`). **Auto-remove a própria linha do crontab** quando os 6 estiverem comentados. Log em `/opt/minutoreal/comentarios.log`.
- Teste headless OK (12/jun): autentica via refresh token sem navegador.
- Os 6 lembretes session-only do Claude foram REMOVIDOS (a VPS assumiu — sem duplicidade).
- Rodar manualmente se preciso: `ssh root@andregalgani.com.br /opt/minutoreal/run.sh`

**Grade semana 3 agendada (Silêncio):** LONGO A9vOvkLDj0w seg 29/06 19h · Shorts 14rnTJohWVE ter 30/06 12h · O-6kZG-2vZY qua 01/07 19h · EJklw9g3QEU sex 03/07 12h · J97o4aCYU3A sáb 04/07 10h.
**Rotina pós-publicação padronizada (3 passos):** produzir_shorts.py → agendar_lote.py (grade: longo seg 19h + shorts ter/qua/sex/sáb) → enfileirar_comentarios.py (fila da VPS v2: /opt/minutoreal/fila.json, cron 2/2h posta CTA quando o vídeo fica público; longo = pergunta+CTA, short = CTA+link-mãe). CTA falado já na narração (regra).


## ⚠️ LIÇÃO CRÍTICA — Canal correto no OAuth (12/jun)
O canal **Minuto Real** = `UC2N5xZ-gyCU3hNvH1QqNahA`. Existe também o canal PESSOAL **André Galgani** (`UCmSpZF4cVFd1kTYomdC_NUw`) sob a mesma conta Google. **Ao reautorizar o OAuth, SEMPRE escolher "Minuto Real"** — uma vez foi selecionado o pessoal por engano e Silêncio+Quem Mexeu subiram no canal errado (revertido). Conferir sempre: `channels.list(mine=True).snippet.title == 'Minuto Real'`.

## IDs ATUAIS (Minuto Real, pós-reversão)
- **Save the Cat (gap-fill 13/jun, PÚBLICO):** longo `WAHhiIW6Wjc` (público sáb 13/06) · shorts CORRIGIDOS (áudio com respiro de entrada) `QVKAObJqcQg`(público 13/06) `3sXdnZ3avHU`(14/06 10h) `9E0napGqpnY`(15/06 12h) `1wUlNH-otWE`(16/06 10h). Shorts antigos (arranque de áudio defeituoso) desativados/unlisted: 56yJnmAOnqc, xBApYdm-QOg, 14P0Wj7CQRw, rwouqYl7veQ. Comentários reapontados.
- **Jornada do Escritor (gap-fill 13/jun):** longo `Eb4LTgfF65o` (dom 14/06 19h). Shorts ainda não produzidos.
- **Nação Dopamina (gap-fill 13/jun):** longo `dzPz77iqffs` (seg 15/06 19h). Shorts ainda não produzidos.
- **Silêncio:** longo 3X5s-p2LH9c (seg 29/06 19h) · shorts LAlSS3Gkbgk(30/06) XbR5IfLl190(01/07) zSyLcgLWBwo(03/07) JPYYyEVZVlU(04/07)
- **Quem Mexeu:** longo JDmuaZ9hA_U (seg 06/07 19h) · shorts ynwCFDI8Vl4(07/07) fnzyThF7fic(08/07) VijxfJZj-vQ(10/07) vvlVJxGaG98(11/07)
- **Padrão Bitcoin (PREMIUM Imagen+Veo, 12/jun):** longo ur9LHfpKUCY (seg 13/07 19h · thumb própria · 10/11 cenas Veo cinema, 1 Ken Burns por quota Veo diária) · shorts iXQOU8uVCJs(ter 14/07) OuIMtbDcxUk(qua 15/07) seCJSaOZOpk(sex 17/07). **PENDENTE:** 4º short cena 8 NÃO subiu (YouTube `uploadLimitExceeded` — cota diária). Amanhã: `produzir_shorts.py padrao-bitcoin ur9LHfpKUCY` (sobe só a cena 8, idempotente) → `agendar_lote.py padrao-bitcoin ur9LHfpKUCY 13/07` (encaixa no slot sáb 18/07) → `enfileirar_comentarios.py padrao-bitcoin ur9LHfpKUCY "..."` (adiciona CTA do 4º short).
### 🎙 Voz com pausas (ajuste 13/jun)
`_to_ssml` no `gerar_video.py` insere pausas SSML (540ms após `?`, 360ms após `.`, 300ms no travessão) — narração ~25% mais longa, mais natural, interrogação com entonação clara. **Os 5 longos base abaixo foram TODOS reconstruídos com a voz nova** (mp4 atuais já são a versão melhorada). O Bitcoin (ur9LHfpKUCY) já estava público-agendado e ficou com a voz antiga (não rebuildado).

### 🎚 Pós-produção desacoplada — stems + Mix & Master (13/jun)
O build agora separa decisões de áudio da mídia cara. `gerar_video.py` exporta `_stems/<slug>/` (`video_mudo.mp4` · `voz.wav` · `trilha.wav` · `efeitos.wav` · `mix.json`) e roda `mixmaster.py`, que monta o master **re-executável em ~5–8s sem re-render**. Pós-edição = editar `_stems/<slug>/mix.json` (`music_gain`, `loudnorm` −14 LUFS, etc.) → `python mixmaster.py <slug>`. Os 6 vídeos da fila foram reconstruídos por esse pipeline (têm stems). Backlog do Sonoplasta (ducking, SFX `efeitos.wav`) agora pluga no `mixmaster`. Detalhes em `estudio-de-producao/references/sonoplastia.md`.

### ✅ GAP-FILL 13–16/jun (≥2 publicações/dia — ordem do Showrunner 13/jun)
Como o canal estava sem nada até 16/jun, 3 longos foram puxados para esta semana (público/agendados) + os 4 shorts do Save the Cat distribuídos:
- **13/06 (sáb):** Save the Cat LONGO `WAHhiIW6Wjc` (PÚBLICO) + short `QVKAObJqcQg` (PÚBLICO).
- **14/06 (dom):** Jornada LONGO `Eb4LTgfF65o` (19h) + STC short `3sXdnZ3avHU` (10h).
- **15/06 (seg):** Nação Dopamina LONGO `dzPz77iqffs` (19h) + STC short `9E0napGqpnY` (12h).
- **16/06 (ter):** short de lançamento `fEVIgIFu8og` (12h, já existia) + STC short `1wUlNH-otWE` (10h).
Comentários CTA enfileirados na VPS. (Save the Cat, Jornada e Nação Dopamina saíram da fila de pendências abaixo.)

### ⚠️ PENDÊNCIAS DE UPLOAD — 4 longos + 1 short (cota diária YouTube)
Todos CONSTRUÍDOS local com voz nova + stems, thumbs em `_thumbs/<slug>.png`, páginas no ar. A cota diária é baixa (~4-6 uploads); a tarefa agendada `minutoreal-finalizar-uploads` sobe com self-healing. Para CADA longo: `upload_youtube.py <slug>.mp4 roteiros/<slug>.json` → `<id>` → `thumb_set.py <id> _thumbs/<slug>.png` (thumb JÁ existe) → `produzir_shorts.py <slug> <id>` → `agendar_lote.py <slug> <id> <DD/MM>` → `enfileirar_comentarios.py <slug> <id> "<pergunta>"`. (Datas refletidas para frente após o gap-fill.)

**Cadência nova (parecer do Especialista de Algoritmo, 13/jun): 2 longos/semana — SEGUNDA e QUINTA 19h — + 1 short/dia.** O `agendar_lote.py` foi reescrito p/ isso (`SLOTS_SHORTS` = +1..+4 dias após o longo, 1/dia; aceita seg E qui). Não empilhar longos no mesmo dia; não publicar longo todo dia (queima o acervo).

| Slug | Agendar 19h | shorts | Pergunta-âncora do comentário |
|---|---|---|---|
| `sound-design` | 20/07 (seg) | [1,3,6,8] | Você presta atenção no som dos filmes — ou ele te manipula sem perceber? 👇 |
| `audiovisao` | 23/07 (qui) | [1,2,4,5] | Qual cena te emocionou mais pelo som do que pela imagem? 👇 |
| `coesao-coerencia` | 27/07 (seg) | [2,3,5,7] | Qual texto te perdeu por falta de coesão ou coerência? 👇 |
| `ponerologia` | 30/07 (qui) | [2,3,6,8] | Quais sinais te ajudam a reconhecer uma manipulação coletiva? 👇 |

+ **4º short do Bitcoin (cena 8)** — `produzir_shorts.py padrao-bitcoin ur9LHfpKUCY` (idempotente, sobe só a cena 8) → `agendar_lote.py padrao-bitcoin ur9LHfpKUCY 13/07` (slot sáb 18/07) → `enfileirar_comentarios.py padrao-bitcoin ur9LHfpKUCY "Você confiaria mais sua poupança ao ouro, ao dinheiro do governo ou ao Bitcoin? 👇"`.
- **Cópias ÓRFÃS no canal pessoal (privadas, neutralizadas):** A9vOvkLDj0w, 14rnTJohWVE, O-6kZG-2vZY, EJklw9g3QEU, J97o4aCYU3A, -qf92lFQ7ms, Bls56mHkGRc, fp5SmbJ46oA, CrIh_N-xwqQ, dokh_4xSpPU → **Showrunner deve APAGAR no Studio do canal pessoal** (não hard-deleto via API por política).
- VPS comment automation: token trocado p/ Minuto Real, fila.json reconstruída (16 itens), estado resetado.
- **TikTok (@minuto_real2):** auto-post construído em `videos/tiktok_post.py` (Content Posting API; `python tiktok_post.py <slug>` = Direct Post · `--draft` = rascunho sem auditoria). Legendas nativas via `caption_for` (salvas em `_shorts/<slug>_tiktok_captions.md`). **Pendente do Showrunner:** app em developers.tiktok.com (Content Posting API + escopo `video.publish`) + auditoria (gargalo de tempo) + OAuth → `access_token` em `.secrets/tiktok_token.txt`. Modo `--draft` (escopo `video.upload`) já funciona sem auditoria assim que houver token. Detalhes em `estudio-de-producao/references/distribuicao.md`.

## OCR (livros-imagem) — instalado 12/jun
Tesseract 5.4 (winget) + por.traineddata em `biblioteca/ocr_data/`. PDF-scan → `python ocr_pdf.py <pdf> <slug>.txt` → book-to-skill. GPU NÃO é necessária (Tesseract CPU é o motor certo p/ livro impresso). Provado ponta a ponta.
