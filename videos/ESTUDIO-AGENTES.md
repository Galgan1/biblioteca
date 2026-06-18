# Estúdio de Agentes — Geração de Vídeo (Minuto Real)

> **Akita etapa 0 — plano-alvo.** Desenho da rede de agentes do estúdio de vídeo:
> roster completo (do diretor ao sonoplasta), interconexão ótima e duas modalidades
> (NORMAL / PREMIUM). Fundado em pesquisa de ponta 2025–26 (fontes no fim).
> Este documento é a *constituição* do estúdio (pilar 6 do Akita): contratos antes de código.

---

## 0. Princípio — "estúdio", não "enxame"

A pesquisa dos pipelines de vídeo de ponta converge num ponto que vale repetir antes de tudo:

> *"Um único agente bem desenhado supera um sistema multi-agente em baixa complexidade.
> Não adicione agentes sem necessidade."* — Presenc.ai, 2026

Por isso o estúdio do Minuto Real **NÃO** adota LangGraph/CrewAI/AutoGen como enxame autônomo.
O ótimo, para esta complexidade, é o **padrão Supervisor**: o **Maestro** (que já existe como skill)
é o orquestrador único que chama cada papel na ordem certa, segura os *gates* e decide o próximo passo.

Cada "agente" do estúdio é um **papel com contrato** — não necessariamente uma IA autônoma:

| Tipo de papel | Implementação | Exemplos |
|---|---|---|
| **Determinístico** | script Python puro (sem LLM) | Editor/Montador (ffmpeg), Distribuidor (deploy/upload) |
| **Geração isolada** | 1 chamada de modelo, entrada→saída | Narrador (TTS), Diretor de Arte (imagem), Cinegrafista (vídeo), Compositor (trilha) |
| **Julgamento (LLM)** | decisão/avaliação em linguagem | Roteirista, Diretor, Revisor, QC de conteúdo |

Regra de ouro (pilar Akita "humano decide o quê, IA decide o como"):
**transformação previsível → determinístico; geração/decisão → IA.** Nada de LLM onde um `ffmpeg` resolve.

---

## 1. O roster (do diretor ao sonoplasta)

15 papéis. "Módulo atual" = onde isso já vive no código (a maior parte já existe — isto **formaliza**, não reescreve).

| # | Papel | Responsabilidade | Módulo atual | NORMAL | PREMIUM | "Pronto" (rúbrica binária) |
|---|---|---|---|---|---|---|
| 1 | **Maestro / Showrunner** | orquestra tudo, escolhe modo, segura gates | skill `maestro` | idem | idem | roda a rede ponta-a-ponta sem intervenção fora dos 2 gates |
| 2 | **Pesquisador** | ângulo, palavra-chave, gancho competitivo | *(gap)* skill do livro | LLM + `_data.py` | + dados de tendência | devolve 1 ângulo + 3 ganchos testáveis |
| 3 | **Roteirista** | hook 0–15s, blocos de insight, clímax contraintuitivo, CTA; short = narrative loop | skills storytelling + `_data.py` | LLM (Sonnet) | + loop aberto plantado, virada em 4–4:30 | hook na 1ª frase; ≤52 palavras/cena; short 20–25s |
| 4 | **Diretor** | plano de cenas (shot list): por cena {texto, tratamento visual, tom de voz, som}; ritmo anti-slop | `references/algoritmo-youtube` + `producao` | regras fixas | + roteamento de modelo por cena | toda cena tem os 4 campos; corte varia 3–8s |
| 5 | **Diretor de Arte** | imagens das cenas + slides | `imagen.py`, `make_slide`/`_draw_text` | Imagen 4 Fast ($0,02) + Pillow | Ideogram 3.0 (texto) + Flux (BFL) + **LoRA da marca** | tudo deriva de `marca.py`; seed fixo por família |
| 6 | **Cinegrafista** | still → movimento | `make_clip` (Ken Burns), `make_motion_clip` (Veo/Kling via `veo.py`/`falgen`) | **DepthFlow** parallax 2.5D (local, grátis) + LTX-Video local | Veo 3.1 Fast (base) + Kling 3.0 (rostos) + MiniMax (volume) | sem morphing; câmera motivada, não padrão |
| 7 | **Narrador** | voz por cena, emoção adequada | `tts()` + `_to_ssml()` + rota de fuga | edge-tts `pt-BR-AntonioNeural` (grátis) | **ElevenLabs v3** (1ª opção) → Chirp3-HD (fallback) | pt-BR natural; respiro de entrada ~0,45s; sem pt-PT |
| 8 | **Compositor** | trilha que respira com o tema | `sintetiza_ambiente()` | procedural + Stable Audio (licença limpa) | ElevenLabs Music (única com licença comercial + API limpa) | trilha −18 a −20 dBFS sob a voz |
| 9 | **Sonoplasta** | SFX + transições + marca sonora + DSP + master | `efeitos_transicao.py`, `marca_sonora.py`, `dsp.py` | biblioteca própria + `ffmpeg loudnorm` | + ElevenLabs SFX v2 + DSP cinema | master **−14 LUFS**, True Peak ≤ −1 dBTP |
| 10 | **Editor / Montador** | monta vídeo+áudio+legenda | `gerar_video.py` (ffmpeg), `gerar_short.py` | idem (determinístico) | idem | render sem erro; legenda desde o 1º segundo |
| 11 | **Revisor pt-BR** | QC de língua, pt-PT bloqueante | `references/revisor-portugues` | checagem | idem | zero pt-PT; sem anglicismo solto |
| 12 | **Thumbnailer** | thumb de clique | `gerar_thumb.py`, `thumb_set.py` | Pillow + Imagen 4 Fast | Ideogram 3.0 + A/B (Test & Compare) | 1 foco, ≤3–4 palavras, 1280×760, legível em 100×56 |
| 13 | **QC / Verificador** | rúbrica 4 estágios (técnico/produção/conteúdo/humano) | `doctor.py` + `text_budget.py` | checagem automática | + LLM-judge cross-model | média ≥4/5; **Compliance = bloqueante** |
| 14 | **Compliance / Copyright** | licença de assets, sem personagem protegido, regra de afiliado | *(gap)* | checagem | idem | trilha/SFX com licença; link afiliado só `/dp//gp/` |
| 15 | **Distribuidor / SEO** | título/descrição/tags, publica YT/IG/FB/TikTok | `*_post.py`, `facebook_*.py`, cadence jsons | determinístico | + agendamento (n8n) | metadados completos; link na bio (IG) |

---

## 2. Interconexão ótima (o grafo)

DAG sequencial **com paralelismo no meio e dois gates**. As setas são *handoffs* com contrato
(saída de um = entrada do próximo). O Maestro conduz; nada roda fora de ordem.

```
                       LIVRO/TEMA  (skill do livro = fonte da verdade)
                            │
                     [2 Pesquisador]  → ângulo + ganchos
                            │
                     [3 Roteirista]   → roteiro (hook/blocos/clímax/CTA + short)
                            │
            ╔═══════════════▼═══════════════╗
            ║  ◇ GATE 1 — Roteiro           ║   [11 Revisor pt-BR] + HUMANO aprova
            ╚═══════════════╤═══════════════╝
                            │
                     [4 Diretor]       → shot list: por cena {texto, visual, voz, som}
                            │
        ┌───────────────┬───┴───────────┬────────────────┐   (PARALELO)
        ▼               ▼               ▼                ▼
  [7 Narrador]   [5 Diretor Arte]  [8 Compositor]   [12 Thumbnailer]
   voz/cena       imagens/cena       trilha            thumb
        │               │               │                │
        │        [6 Cinegrafista]       │                │
        │         still → movimento     │                │
        └───────┬───────┴───────┬───────┘                │
                ▼               ▼                          │
            [9 Sonoplasta]  (SFX + marca sonora + DSP + −14 LUFS)
                │                                          │
                ▼                                          │
            [10 Editor/Montador]  (ffmpeg: vídeo+áudio+legenda) ◄──────┘ (thumb anexa)
                │
        ╔═══════▼════════════════════════╗
        ║  ◇ GATE 2 — QC 4 estágios      ║   [13 QC] + [14 Compliance bloqueante] + HUMANO "fresh eyes"
        ╚═══════╤════════════════════════╝
                │
         [15 Distribuidor/SEO]  → YT / IG / FB / TikTok
```

**Paralelismo:** depois da shot list do Diretor, Narrador / Diretor de Arte (→Cinegrafista) / Compositor /
Thumbnailer são independentes e rodam em paralelo; convergem no Sonoplasta → Editor.
**Por que só 2 gates:** a pesquisa é unânime — *pipeline 100% autônomo sem gate humano gera "slop"*.
O humano entra onde decide (aprovar roteiro) e onde cura (revisão final "fresh eyes"). O resto é automático.

---

## 3. As duas modalidades (matriz consolidada)

| Camada | NORMAL (grátis / quase-zero) | PREMIUM (ponta) |
|---|---|---|
| **Roteiro** | Sonnet via skills | Sonnet + pesquisa de gap por livro |
| **Imagem** | Imagen 4 Fast ($0,02) + Pillow | Ideogram 3.0 (texto) + Flux (BFL) + LoRA da marca |
| **Movimento** | DepthFlow parallax 2.5D + LTX-Video (local) | Veo 3.1 Fast + Kling 3.0 (rostos) + MiniMax (volume) |
| **Voz** | edge-tts `AntonioNeural` | ElevenLabs v3 → Chirp3-HD (fallback) |
| **Trilha** | procedural + Stable Audio | ElevenLabs Music |
| **SFX/Master** | biblioteca + `ffmpeg loudnorm` −14 LUFS | ElevenLabs SFX v2 + DSP cinema |
| **Thumb** | Pillow + Imagen 4 Fast | Ideogram 3.0 + A/B |
| **Custo/vídeo 5min** | **~US$0** (só energia) | **~US$25–35** (Veo Fast; *verificar preços*) |

> O maior salto NORMAL→PREMIUM é a **voz** (a pesquisa de áudio é categórica: a narração prende ou
> perde o ouvinte nos primeiros 15s). Trilha/SFX são incrementais. **Sora 2 está descontinuado** —
> não é alvo (atualizar qualquer referência a Sora no `veo.py`).

---

## 4. Contrato anti-slop (constituição — pilar 6)

Regras que **todo** vídeo cumpre, independentemente do modo. Violar = FAIL no Gate 2.

1. Corte/troca de visual a cada **3–8s** (variável, não no beat exato da voz).
2. B-roll de ambiente **antes** do b-roll de conceito (âncora emocional).
3. **Mistura fontes** (imagem IA + slide + stock) — textura uniforme denuncia "tudo IA".
4. Movimento de câmera **motivado**, nunca efeito padrão em 100% das cenas.
5. **Corte no silêncio**, não na palavra (respiro da narração antes da troca).
6. Som ambiente baixo sob a voz (−18 a −20 dBFS); Short sem ambiente soa artificial.
7. Consistência de marca via `marca.py`/`tokens.py` — **fonte única**, sem cor hardcoded
   (deriva de marca é o maior risco de pipeline agêntico).

---

## 5. Gate 2 — rúbrica de QC (4 estágios)

Publica só se média ≥ 4/5 **e** Compliance = OK (bloqueante).

| Estágio | Dimensão | Como | Bloqueia? |
|---|---|---|---|
| 1. Técnico | ≥1080p, sem morphing, áudio sem clip, LUFS correto | `doctor.py` automático | sim se LUFS/clip |
| 2. Produção | ≥4 composições, cortes 3–8s, som ambiente, câmera motivada | checagem + heurística | não (alerta) |
| 3. Conteúdo | gancho ≤3s/≤30s, claims verificáveis, CTA, sem pt-PT | Revisor + LLM-judge cross-model | sim se pt-PT/claim falso |
| 4. Humano | coerência, tom, marca — "fresh eyes" | revisão 2–3 min | sim |
| — | **Compliance** | licença de assets, sem personagem protegido, afiliado `/dp//gp/` | `compliance` | **sempre bloqueante** |

---

## 6. O que já existe × gaps (mapa de implementação)

**Já implementado (formalizar, não reescrever):** Maestro, Roteirista (skills), Diretor de Arte
(`imagen`+Pillow), Cinegrafista (Ken Burns + Veo/Kling), Narrador (`tts`+fuga), Compositor
(`sintetiza_ambiente`), Sonoplasta (`efeitos_transicao`+`marca_sonora`+`dsp`), Editor
(`gerar_video`/`gerar_short`), Revisor pt-BR, Thumbnailer (`gerar_thumb`/`thumb_set`),
Distribuidor (`*_post.py`), QC parcial (`doctor`/`text_budget`).

**Gaps reais (o que a etapa 0 revelou):**
- **Pesquisador** e **Compliance** — papéis sem módulo dedicado hoje.
- **Cinegrafista NORMAL** — falta DepthFlow (hoje só Ken Burns simples) → maior alavanca grátis.
- **Narrador PREMIUM** — opção ElevenLabs v3 (hoje premium = Chirp3-HD apenas).
- **Sonoplasta** — normalização explícita a −14 LUFS (alvo YouTube) no master.
- **QC** — formalizar a rúbrica de 4 estágios como gate de saída (hoje `doctor` cobre só o técnico).
- **Diretor** — shot list explícita com os 4 campos por cena (hoje implícita no `_data.py`).

**Fatia vertical recomendada (1º passo de implementação, pós-aprovação):**
maior valor / menor risco / custo zero → **(a)** Sonoplasta `−14 LUFS` no master +
**(b)** Cinegrafista DepthFlow no NORMAL + **(c)** Gate 2 como `qc.py` (rúbrica executável).
Tudo local, sem crédito de API, testável com TDD antes de mexer em provedores pagos.

> **STATUS (implementado, jun/2026, TDD + cross-model APROVADO):**
> - **(a) FEITO** — `mixmaster.py`: `loudnorm −14 LUFS / TP −1` ligado por padrão; grafo de
>   áudio extraído para `_build_audio_filter` (puro, testado). Tests: `test_mixmaster.py`.
> - **(b) FEITO** — `cinegrafista.py` (decisão `tratamento` + guard `parallax`) + hook
>   **dormente** em `gerar_video.py` (zero regressão sem DepthFlow). Tests: `test_cinegrafista.py`.
> - **(c) FEITO** — `qc.py`: 4 estágios, bloqueantes (resolução/TP/pt-PT/link-busca), exit code;
>   CLI provado (aprova roteiro bom, reprova ruim). Tests: `test_qc.py`. Achado: densidade de
>   narração usa 52 palavras (convenção do projeto), não 35 (que é de slide).
>
> **RODADA DE SUBAGENTES (cada item = 1 executor Sonnet + verificação Opus cross-model):**
> - **Item 1 — Gate QC cravado** ✅ — fim de `gerar_video.py` roda `qc.coletar` e grava o veredicto
>   em `_stems/<slug>/qc.json` (não destrói mídia); ponto único `qc.aprovado(slug)` p/ a publicação.
>   Tests: `test_qc_gate.py`.
> - **Item 2 — DepthFlow FECHADO** ✅ — `pip install depthflow` feito; flags reais da CLI corrigidas
>   (`python -m depthflow … -t … -f …`) + fix de Unicode no Windows; **render real verificado**
>   (mp4 3.0s, ~2,4s cache). ⚠️ instalar depthflow **rebaixou torch p/ CPU** (CUDA: False).
>   Smoke reutilizável: `cinegrafista_smoke.py`. Tests: `test_cinegrafista.py`.
> - **Item 4 — Narrador ElevenLabs** ✅ código — cadeia `eleven→Chirp3-HD→edge-tts` em `tts()`;
>   sem chave cai na fuga (zero rede). Tests: `test_tts_provedor.py`. **PENDENTE p/ uso real:**
>   chave em `.secrets/elevenlabs_key.txt` + autorização de gasto (não houve chamada paga).
>
> **ITEM 3 — Três papéis contratados (Opus executor + Sonnet verificador cross-model 5/5):**
> - **Pesquisador** ✅ — `pesquisador.py`: gera ganchos pelas 5 fórmulas de retenção, pontua
>   (brevidade+curiosidade+pergunta+número) e escolhe o melhor; puro/local. Tests: `test_pesquisador.py`.
> - **Conferente de direitos (Compliance)** ✅ — `compliance.py` é o **lar canônico** das regras
>   (link só `/dp//gp/`, prompt sem IP protegida, trilha licenciada); cravado no gate (`qc.coletar`
>   chama `compliance.auditar`; `qc` reexporta `link_amazon_valido`, sem duplicar nem ciclo). Tests: `test_compliance.py`.
> - **Diretor** ✅ — `diretor.py`: shot list com 4 campos/cena (texto/visual/voz/som), visual reusa
>   `cinegrafista.tratamento`; `revisar_ritmo` avisa cena estática (anti-slop). Tests: `test_diretor.py`.
> Mural: **151 testes verdes** (eram 64 no início desta fase).
>
> **CINEGRAFISTA 3D — 3D Gaussian Splatting local (Opus executor + Sonnet verificador 6/6):**
> - `splatting.py` ✅ seam — `gaussian_disponivel()` (exige torch+CUDA + motor 3DGS), `orbit_poses()`
>   (matemática da órbita de câmera, pura/testada), `splat_clip()` (guard+fallback). Decisão `'gaussian'`
>   adicionada a `cinegrafista.tratamento` (preferida quando disponível; `gaussian_ok` default False =
>   sem regressão). Hook **dormente** em `gerar_video.py`. Tests: `test_splatting.py`. Smoke: `splatting_smoke.py`.
> - **GPU:** RTX 5060 (8 GB, Blackwell). **torch CUDA restaurado** ✅ — `torch 2.11.0+cu128` +
>   `torchvision 0.26.0+cu128` (CUDA True; DepthFlow agora roda na GPU). *(2.12.1 não tem wheel cu128;
>   2.11.0 é a build CUDA original da máquina.)* **PENDENTE p/ render 3DGS real:** instalar motor 3DGS
>   (gsplat) + escrever `splatting_engine` (imagem→Gaussians→render). Bleeding-edge em Blackwell/Windows.
> - **`splatting_engine.py` ESCRITO** ✅ (geometria pura testada; render GPU isolado, ligado a `splat_clip`).
>   gsplat 1.5.3 instalado mas **desabilitado** (sem nvcc/MSVC). Próximo: usuário roda `setup_3dgs_toolchain.bat`
>   como admin (CUDA 12.8 + VS BuildTools) → eu compilo gsplat + `pip install transformers` → smoke na GPU.
> Mural: **166 testes verdes**.
> Mural: **160 testes verdes**.

---

## 7. Fontes (pesquisa 2025–26)

- Vídeo: [fal.ai Veo 3.1](https://fal.ai/models/fal-ai/veo3.1/image-to-video) · [Kling 3.0](https://www.atlascloud.ai/blog/guides/kling-3.0-review-features-pricing-ai-alternatives) · [open-source 2026](https://www.aimagicx.com/blog/open-source-ai-video-models-comparison-2026) · [DepthFlow](https://github.com/BrokenSource/DepthFlow)
- Áudio: [Eleven v3](https://elevenlabs.io/blog/eleven-v3) · [ElevenLabs vs Qwen3 pt-BR (Akita)](https://akitaonrails.com/en/2026/04/09/how-elevenlabs-was-not-killed-by-qwen3-tts/) · [música IA 2026](https://www.digitalapplied.com/blog/ai-music-generation-platforms-suno-udio-elevenlabs-2026) · [LUFS YouTube](https://www.peak-studios.de/en/youtube-audio-richtlinien-streaming-2025/)
- Orquestração: [frameworks 2026](https://presenc.ai/research/multi-agent-orchestration-frameworks-2026) · [stack faceless](https://virvid.ai/blog/ai-faceless-youtube-automation-stack-2026) · [anti-slop](https://greenfroglabs.com/blog/ai-video-quality-avoid-slop-appearance) · [geração→agente](https://genra.ai/blog/ai-video-trends-2026-generation-to-agent-workflows)
- Imagem/roteiro: [Imagen 4 Fast](https://developers.googleblog.com/announcing-imagen-4-fast-and-imagen-4-family-generally-available-in-the-gemini-api/) · [Ideogram 3.0](https://tech-now.io/en/blogs/ideogram-3-0-review-2025-the-ultimate-ai-image-generator-for-text-style-control) · [Flux LoRA](https://fal.ai/models/fal-ai/flux-lora) · [hook 3s](https://virvid.ai/blog/first-3-seconds-hook-faceless-shorts-2026) · [narrative loop](https://virvid.ai/blog/looping-structure-shorts-retention-2026)
