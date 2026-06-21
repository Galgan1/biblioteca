# Sonoplastia para Engajamento — Estratégia (revisão Akita zero-a-produção · 21/jun/2026)

> `/akita /loop-agente` · juízes = os autores dos livros de sonoplastia (**Sonnenschein** + **Chion**); lente de dopamina = **Lembke** (Nação Dopamina). Forward-looking: **não re-renderiza o catálogo**; soberano (numpy/local); **voz soberana**.

## O achado decisivo
**O Short era VOZ sobre SILÊNCIO.** O `gerar_short.py` só mapeava a voz: a capa de marca (2,4s) abria **muda** e não havia trilha nem efeito nenhum. Em Reels/TikTok/Shorts — onde o **hook de áudio nos primeiros 2s** segura o scroll — isso é a maior perda de engajamento do pipeline. Os 3 autores convergiram exatamente aí.

## Síntese dos 3 autores (os princípios que se reforçam)
- **Chion — temporalização/vetorização:** uma capa estática não faz o tempo correr; sem progressão sonora o espectador percebe duração demais e sai. Todo efeito precisa de **synch point** e de **valor acrescentado** (o som faz a imagem parecer mais forte). A **voz é o acusmêtre** — vococentrismo é física, não conservadorismo.
- **Sonnenschein — emoção pelo contraste:** o impacto só pesa depois do silêncio; a energia vem do **ritmo**, não do volume; o **sub-grave (35–60 Hz)** cria tensão corporal "invisível"; o **envelope** (ataque seco = choque, cauda longa = memória) carrega emoção sozinho; a **assinatura sonora** fideliza o canal.
- **Lembke — dopamina sustentável:** a dopamina é de **antecipação** (o riser que promete vale mais que o hit); **escassez/silêncio** faz o hit aterrissar (hormese); **recompensa variável e espaçada** evita a tolerância; o pico sonoro só é honesto se **coincide com o pico de conteúdo** (senão treina o público a desligar).

**O arco de engajamento sonoro (a estrela-guia):** `HOOK (antecipação) → TENSÃO que vetoriza → ACENTO de síncrese → RECOMPENSA ganha → RESTRIÇÃO/silêncio → SEAM de replay`. Dopamina pelo **arco correto**, não pelo "alto e constante".

## Incremento 1 — IMPLEMENTADO e verde (`_short_audio.py::short_bed`)
Dá ao Short o leito de engajamento que faltava. `python testar.py` → **507 verde** (10 testes novos).
| Camada | Autor | O que faz |
|---|---|---|
| **HOOK** riser na capa (0→2,4s), termina no corte | Lembke (antecipação) + Chion (temporalização) | preenche a abertura muda com uma promessa que **não resolve** → puxa pra frente |
| **ACENTO** knock grave no corte capa→cena | Chion (síncrese) | solda o corte; "snap" de atenção involuntário |
| **LEITO** sub-grave 40–55 Hz pulsante sob a voz | Sonnenschein (tensão invisível) | sentido no corpo, **abaixo da faixa da fala** (voz soberana), gain 0.12 |
| **VETORIZAÇÃO** o leito sobe rumo a ~75% e resolve | Chion (o Short "puxa") | retenção entre os cortes, não só nos cortes |
Mix: `amix normalize=0 + alimiter` no `gerar_short.py` → voz **cheia**, leito por baixo. Tunável por roteiro (`musica_energia`). Testes fixam: hook não-silencioso, corpo << hook (voz soberana), vetorização (RMS sobe), determinismo.

## Rúbrica unificada (PASS/FAIL — os juízes são os autores)
1. **Sonnenschein** — cada efeito serve função emocional (tensão↔liberação, ritmo, contraste de timbre), não é decoração; há **silêncio funcional** e **sub-grave** na construção.
2. **Chion** — cada efeito tem **synch point** e **acrescenta valor**; a voz é soberana (vococentrismo) em toda narração; o arco **vetoriza**.
3. **Lembke** — recompensa por **antecipação + escassez**; espaçada/variável (não constante); o pico sonoro **coincide com o pico de conteúdo** (não predatório).
4. **Engajamento** — cobre hook 0–2s, open loop, pattern interrupt, cue de recompensa, seam de replay, com gatilho por cena.
5. **Produção (Akita)** — código real, `testar.py` verde, parametrizável, forward-looking.

## Roadmap (próximos incrementos — cada um TDD + gateado)
- ✅ **P2 · synch points de conteúdo (IMPLEMENTADO — gate 529):** **tick** brilhante de síncrese no dado/insight via campo `"reveal"` na cena (`True` = meio da narração · número = segundo · substring = estimativa por caractere). `_short_audio._tick` + `gerar_short._reveal_offsets`. Fecha o critério 3 do Lembke (pico sonoro = pico de conteúdo). Falta o **duck/micro-silêncio** antes da frase-chave (Sonnenschein T2) — próximo sub-passo.
- **P1 · levar o ganho ao LONGO:** `sintetiza_ambiente` ganha **curva de energia** (vetorização intra-cena — lacuna nº1 do Chion) + **sub-grave de tensão** (lacuna nº1 do Sonnenschein). Param novo, back-compat (escalar continua valendo).
- **P3 · dopamina anti-tolerância (Lembke):** **reforço variável** (jitter ±0,3–0,6s nos pontos da marca) + **omitir o encerramento em ~1/5** dos vídeos + **resolução adiada** (encerrar em Lá em ~50%, não sempre em Ré) → o cérebro não habitua.
- **P4 · escassez estrutural (Lembke):** **jejum interno** (zona de baixa densidade ~35–55% do vídeo) + **saliência one-shot** (um único acento no insight mais memorável — nunca dois).
- **Guarda de qualidade:** critério 6 da rúbrica (pico sonoro = pico de conteúdo) entra como check antes de exportar — o som nunca promete o que o roteiro não entrega.

## Pronto =
Short com sonoplastia de engajamento ✅ (incremento 1) · trilha longa vetorizando + sub-grave (P1) · synch points de conteúdo (P2) · dopamina espaçada/variável (P3–P4) — **tudo com gate verde, voz soberana e sem re-renderizar o catálogo**. Aprova-se também por **ouvido** (áudio não se aprova só lendo).
