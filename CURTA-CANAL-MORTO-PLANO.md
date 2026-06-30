# CURTA "CANAL MORTO" — Plano de Produção (fatia vertical Akita)

> **O que é:** a *fatia vertical* da conversa anterior — um curta de **~105s** que exercita a cadeia inteira do ofício (história → diálogo → som → imagem → render → QC) numa unidade atômica e produzível. Prova de pipeline, não publicação de canal.
> **Tema:** abertura de *Neuromancer* (Gibson) — Chiba City, Case decaído, **a prisão da carne** (skill `neuromancer`, ch01).
> **Forma:** **3-hander** — Case dialoga com **Julius Deane** (o fixer) e com **Linda Lee** (a namorada). Diálogo **fora-de-quadro / plano-reação**.
> **Método:** Akita (planejar antes, tarefas atômicas, "pronto" = critério verificável). **Direção/QC = humano. Execução = pipeline.**

> ## ✅ STATUS — EXECUTADO (v1 soberano)
> **No ar:** https://www.andregalgani.com.br/biblioteca/curtas/canal-morto.mp4 (HTTP 200, video/mp4)
> **O que é a v1:** curta de **tipografia/diálogo** noir, **70s**, 1920×1080, **3 vozes reais** (Case/Antonio · Deane/Antonio filtrado · Linda/Francisca), leito de som (chuva + drone 55 Hz). 100% soberano (edge-tts + ffmpeg), **custo zero**.
> **Achado Akita:** o `gerar_video.py` de produção é **mono-voz** (`contracts.RoteiroCfg.voz` única) — não faz diálogo. Por isso a v1 roda por um **montador dedicado** `videos/_curta/build_curta.py` (reusa `_video_tts.tts`, não toca a produção). O "roteiro" vive nele, não num `<slug>.json`.
> **O que a v1 NÃO é (ainda):** o neon fotorrealista do §5 — slides são tipográficos. Upgrade = trocar o fundo por imagens `fal` (pago, opt-in).

---

## 0. Constituição do curta (contratos invioláveis)

1. **COPYRIGHT — não transcrever Gibson.** Texto 100% **original/transformativo** (homenagem aos temas, comentário). A frase do "céu de canal morto" é **evocada com construção própria**, nunca traduzida. ⚠️ *Decisão sua:* publicar ou tratar como demo interna.
2. **pt-BR** (pt-PT é bloqueante — cuidado com voz/tradução).
3. **DIÁLOGO FORA-DE-QUADRO.** Sem boca frontal falando (lip-sync é deferido/pago no pipeline). As vozes carregam a cena; cortamos para **planos-reação** (mãos, nucas, silhuetas, reflexos, neon). Chion: voz acusmática/off. É mais noir **e** produzível hoje.
4. **3 vozes pt-BR distinguíveis (soberano):** Case = edge-tts `AntonioNeural` (limpo); **Deane = Antonio processado** (formant grave + filtro de comunicador no `dsp.py` — diegese: fala por canal sujo); Linda = voz feminina pt-BR (`FranciscaNeural`).
5. **Marca sonora = Ré menor** (consistência com `marca_sonora.py`, motivo Lá→Ré).
6. **Um build por vez** (`_work/` compartilhado → colisão/crash de ffmpeg).
7. **Tema sombrio → imagem por `fal` (flux-2-pro), NÃO NVIDIA** (Flux grátis modera cyberpunk → PNG vazio). `safety_tolerance` alto ANTES de rodar.
8. **Custo:** imagem/movimento pagos → **não disparar render sem teu OK**. Voz, som e fallback são soberanos (grátis).

---

## 1. Logline (Save the Cat — ironia + imagem mental)

> Um ladrão de dados que perdeu o acesso ao paraíso digital vaga por uma noite de neon e chuva em Chiba City atrás de uma cura que ninguém pode vender — até que a mulher que ele ama lhe diz, em voz baixa, qual foi o verdadeiro castigo: trancaram-no dentro do próprio corpo.

**Gênero (Snyder):** *Whydunit* noir / "cara num buraco". **Ação única (Aristóteles):** o reconhecimento (peripécia) de que a carne é a sentença — **entregue por outro personagem** (McKee: a verdade aterrissa pelo conflito, não pela narração).

---

## 2. Beat sheet — ~105 segundos

| t (s) | Beat | Quem | O que carrega |
|---|---|---|---|
| 0:00–0:12 | **Hook / opening image** | Case (VO interno, 1 linha) | céu morto, chuva no neon; "high tech, low life" |
| 0:12–0:48 | **Beat A — a recusa fria** | Case ↔ **Deane** | "ninguém vende a cura"; poder e descarte (capitalismo tardio) |
| 0:48–1:22 | **Beat B — o golpe íntimo** | Case ↔ **Linda** | a carne, o vício, a traição-a-vir; ela nomeia o castigo |
| 1:22–1:45 | **Reconhecimento + button** | Case (VO interno) | "o cárcere é isto que me carrega"; volta pra chuva |

---

## 3. Roteiro — diálogo (pt-BR, ORIGINAL, copyright-safe, fora-de-quadro)

### Cena 1 — Abertura (0:00–0:12)
*(8s de som: chuva + neon + sub-grave da cidade)*
- **CASE** *(VO, interno)* — "Chiba não dorme. E não te deixa esquecer o que você perdeu."

### Cena 2 — Beat A · Case ↔ Deane (0:12–0:48)
*(interior de contrabando: fumaça, mercadoria, mãos enluvadas; Deane só em silhueta/nuca)*
- **DEANE** — "Você queima rápido, cowboy. Triste ver um talento desse jeito."
- **CASE** — "Poupa o sermão, Deane. Me arruma a cura e eu sumo da tua porta."
- **DEANE** — "Cura. Eu vendo o que tem preço: órgão, papel, gente. Voltar a voar não está no estoque."
- **CASE** — "Tudo em Chiba tem preço."
- **DEANE** — "Tudo, menos desfazer o que fizeram com você. Isso, nem eu."

### Cena 3 — Beat B · Case ↔ Linda (0:48–1:22)
*(beco/cápsula, neon; Linda em contraluz/silhueta, reflexos na poça)*
- **LINDA** — "Ainda atrás de uma cura?"
- **CASE** — "Eu já voei, Linda. Sem corpo, sem peso. Puro pensamento dentro da máquina."
- **LINDA** — "E aí te queimaram por dentro. Agora você é igual a mim. Carne. Só carne."
- **CASE** — "Não me conformo."
- **LINDA** — "Ninguém aqui vende o que você quer. Eles te deram o pior castigo que existe."
- **CASE** — "Qual?"
- **LINDA** *(baixo)* — "Te trancaram dentro de você mesmo."

### Cena 4 — Reconhecimento + button (1:22–1:45)
*(silêncio — sub-grave cai; Case se vê no reflexo da poça)*
- **CASE** *(VO, interno)* — "O cárcere nunca foi Chiba." *(beat)* "O cárcere é isto que me carrega."
- *(passos na chuva; o céu segue um canal morto)*
- **CASE** *(VO)* — "E mesmo assim, toda noite, eu volto pra rua. Procurando a porta de volta."

**Regra de fala (prosódia premium):** micro-pausa de vírgula (~150ms), cadência variada; falas curtas, subtexto > exposição. Aprovar **por ouvido**.

---

## 4. Sonoplastia (Sonnenschein + Chion)

**Tese:** o som faz o neon ser *real* (contrato audiovisual). Corpo-cárcere = **baixa frequência**; a matrix perdida = **agudo cristalino**, só em *negativo* (sobe e é cortado = a perda).

- **Vozes (vococentrismo, soberanas):** Case limpo/presente; **Deane** filtrado (canal sujo, interior seco, close); **Linda** com mais ar/reverb (beco + chuva). As 3 sempre acima do leito.
- **Acusmático (Chion):** *shimmer* agudo SEM fonte na fala "puro pensamento dentro da máquina" — a matrix chamando; some na hora.
- **Leito (`_video_audio.sintetiza_ambiente` + `dsp.py`):** chuva + zumbido de neon + sub-grave opressivo; reverb de convolução, saturação, ar; mão leve sob as vozes.
- **Síncrese:** som suturado em cada corte de reação; `efeitos_transicao.py` (arco Fibonacci) na ponte Beat A→B.
- **Batida de comoção:** acúmulo → saturação → **silêncio no clímax** (1:22, "te trancaram dentro de você mesmo" ecoa no vazio). `place_marca` + `marca_sonora.py`.
- **Trilha:** pad esparso em **Ré menor**, motivo Lá→Ré; `energia` baixa (~0.3 — é luto).

---

## 5. Color script + shot list (produzível; sem boca frontal)

**Paleta:** magenta/ciano de neon + âmbar de sódio + pretos profundos + chuva. Mono-tóxico, NÃO arco-íris.

| # | Plano (reação/off, nunca boca frontal) | Imagem | Movimento |
|---|---|---|---|
| 1 | Céu morto sobre telhados de Chiba, chuva | `fal` | DepthFlow |
| 2 | Interior de Deane: fumaça, mercadoria, mãos enluvadas | `fal` | DepthFlow |
| 3 | Case de costas/perfil no balcão; reação | `fal` | Ken Burns |
| 4 | Mão de Case tremendo (deck fantasma) — close | `fal` | fal-wan i2v *(herói)* |
| 5 | Beco de neon; Linda em contraluz/silhueta | `fal` | Ken Burns |
| 6 | Reflexo de Case e Linda na poça/vidro | `fal` | DepthFlow |
| 7 | Olhar de Case (reação a "carne, só carne") | `fal` | DepthFlow |
| 8 | Reflexo na poça — o reconhecimento | `fal` | DepthFlow |
| 9 | Passos na chuva, costas de Case; céu canal morto | `fal` | fal-wan i2v *(herói)* |
| 10 | Cartela final (título + crédito de homenagem) | — | estático |

> Só os planos 4 e 9 ("heróis") usam movimento pago; o resto é soberano. Falha paga → fallback (DepthFlow/Ken Burns); o build nunca quebra por budget.

---

## 6. Pipeline de produção (ferramentas reais — corrigido pós-execução)

**Realidade do `gerar_video.py`:** UMA `voz` por vídeo, cena = uma `narracao` única (`contracts.RoteiroCfg`). **Não há diálogo multi-voz.** Campos extras (`falas`) são ignorados (`extra='allow'`).
- **v1 (feito):** montador soberano `videos/_curta/build_curta.py` — voz por fala via `_video_tts.tts` (edge-tts), Deane filtrado por ffmpeg (formant grave + banda suja), slides PIL, leito `anoisesrc`+`sine`, montagem `concat`+`amix`. Custo zero.
- **Upgrade neon (opt-in, pago):** trocar cada slide PIL por imagem `fal` (flux-2-pro, `safety_tolerance` alto) de fundo; texto/fala por cima. Mesmo montador, só o gerador de fundo muda.
- **Upgrade voz premium:** se o Deane processado não convencer, ElevenLabs com voz pt-BR **verificada** (pago) só p/ ele.

---

## 7. Tarefas atômicas (uma por vez · "pronto" = verificável)

| # | Tarefa | "Pronto" (verde = exit code, onde dá) |
|---|---|---|
| T1 | Escrever `neuromancer-canal-morto.json` (4 cenas, falas §3, 3 falantes) | `publicavel()` exit 0 |
| T2 | **Smoke de voz** — gerar as 3 vozes (Case/Deane proc./Linda) | 3 mp3, vozes distinguíveis por ouvido, sem pt-PT |
| T3 | **Smoke de imagem** — 1 plano `fal` | PNG **>20KB** (não placeholder de moderação) + exit 0 |
| T4 | Build completo (1 por vez; `python … > log 2>&1`) | mp4 ~105s, exit 0, log honesto |
| T5 | QC áudio | LUFS na faixa (cuidado bug −70 falso) · respiro ≥0.45s · mix das vozes legível |
| T6 | Juiz de qualidade (rúbrica §8, juiz Opus, 9=reprovado) | **10/10** ou itera (parada em 5, `/loop-agente`) |
| T7 | *(opcional)* handoff GitGuy / deploy | — |

---

## 8. Rúbrica de aprovação (gate da arte — onde não há exit code)

Juiz independente (≠ autor), só **10/10**:

1. **Fidelidade temática** — carne/cárcere, high-tech-low-life, o céu morto.
2. **Copyright** — zero transcrição de Gibson; tudo original.
3. **pt-BR** — nenhuma deriva pt-PT em nenhuma das 3 vozes.
4. **Diálogo com subtexto** — fala curta, não expositiva; conflito real (Deane = poder; Linda = intimidade).
5. **3 vozes distinguíveis** off-screen, sem boca frontal (lip-sync evitado).
6. **Atmosfera** — neon/chuva "respira"; contrato audiovisual cumprido.
7. **Som em camadas** — sub-grave (carne) × agudo acusmático (matrix) legíveis.
8. **O reconhecimento aterrissa** pela Linda ("trancaram dentro de você mesmo"); silêncio no clímax funciona.
9. **Color script coerente** — mono-tóxico, sem arco-íris.
10. **Button** — fecha com gancho, não corta no vazio.

---

## 9. Riscos / tradeoffs (Akita pilar 1)

- **Copyright** é o maior — decisão sua de publicar vs. demo interna.
- **2 vozes masculinas, 1 voz boa** no edge-tts → Deane diferenciado por processamento (formant + filtro). Se não convencer no ouvido: ElevenLabs com voz pt-BR **verificada** (pago) para o Deane.
- **Moderação** → `fal`, nunca NVIDIA; `safety_tolerance` alto antes.
- **Lip-sync** evitado por design (fora-de-quadro) — não depender da talking-head deferida.
- **`_work/` compartilhado** → um build por vez; matar órfão por **PID específico**.
