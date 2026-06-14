# MODO SOBERANO — Rota de Fuga (zero crédito de IA externa)

> **Premissa:** se acabar o crédito das IAs/serviços externos (Google Cloud TTS, Imagen, Veo, fal.ai…), **a máquina inteira continua produzindo aqui, de graça.** Esta é a doutrina de continuidade do Minuto Real / Biblioteca. Testado e baqueado em jun/2026.

## 1. O que SEMPRE roda grátis/local (não depende de IA externa)
| Etapa | Como roda | Custo |
|---|---|---|
| **Skill** (livro→skill) | Claude (aqui) + busca web | grátis |
| **Roteiro** | Claude (aqui) | grátis |
| **Biblioteca** (página, PDF, carrossel, capa, deploy) | Python · Pillow · Playwright · scp p/ a VPS própria | grátis |
| **Vídeo base** (slides, trilha, SFX, montagem) | Pillow · numpy · ffmpeg — tudo local | grátis |
| **Publicação** (YouTube · Instagram · Facebook) | APIs gratuitas (só têm **cota/rate-limit**, não custam crédito) | grátis |

**O único fio pago no nível base era a VOZ** — e ela tem substituta local.

## 2. O ÚNICO swap: a voz
- **Padrão (pago):** `"voz": "pt-BR-Chirp3-HD-Iapetus"` — Google Cloud TTS (~centavos/vídeo). Voz-assinatura do canal.
- **FUGA (grátis):** `"voz": "pt-BR-AntonioNeural"` — **edge-tts** (Microsoft, **local, sem chave, sem crédito**). Masculina e sóbria, a mais próxima do Iapetus. Alternativas: `pt-BR-FranciscaNeural` (fem.), `pt-BR-ThalitaMultilingualNeural` (fem.).
- O `gerar_video.py` já roteia: qualquer voz que **não** seja Chirp3/Studio/Neural2/Wavenet → edge-tts automático. **Basta trocar o campo `voz` no roteiro. Zero mudança de código.**
- Mantenha `"provider": "base"` (já não usa Imagen/Veo).

## 3. Auto-fuga baqueada (jun/2026)
O `tts()` do `gerar_video.py` agora é **resiliente**: se o Google Cloud TTS falhar (sem crédito, cota ou 503), ele **tenta 2×** (cobre o 503 transitório) e, persistindo, **cai sozinho na voz grátis `pt-BR-AntonioNeural`** e segue a produção — imprime `[ROTA DE FUGA]` no log. **O render nunca quebra por falta de crédito externo.** Logo, mesmo um roteiro com a voz paga continua produzindo (degradando só a voz) se o crédito acabar no meio.

## 4. O que se perde no modo fuga (aceitável)
- A voz-assinatura **Iapetus** → vira **Antonio** (boa, mas outra identidade).
- O **ritmo premium por SSML** (micro-pausa de vírgula via `<break>`) **não** se aplica ao edge-tts (ele recebe texto puro; as pausas vêm da pontuação natural). Cadência "boa", não "premium".
- Sem **cinema** (Imagen/Veo) — mas o base nunca usou.
- **Idêntico:** slides, trilha enérgica, arco de comoção (SFX), loudnorm −14 LUFS, Shorts, carrossel, agendamento, comentários, eco no Instagram.

## 5. Checklist de produção soberana (por livro, 100% grátis)
1. **Skill** — já existe ou Claude cria (grátis).
2. **Roteiro** `roteiros/<slug>.json` com `"voz":"pt-BR-AntonioNeural"` + `"provider":"base"`.
3. `python gerar_video.py roteiros/<slug>.json` → QC (`loudnorm:true` no `mix.json` se clipar).
4. **Página** — `<slug>_data.py` → `python publicar_livro.py <slug> --deploy`.
5. **Publicar** — `upload_youtube.py` · `produzir_shorts.py` · `agendar_lote.py` · `instagram_post.py`/`facebook_post.py` (grátis; respeitar a cota diária do YouTube ~6 envios/dia).

## 6. Único limite que sobra (não é crédito, é cota)
- **YouTube:** ~6 uploads/dia (1 longo + 4 Shorts = 5). Limite de **taxa**, reseta diário — não custa crédito. Solução: agendar/pacear ~2 livros/dia.
- **Instagram/Facebook:** cota generosa; cadência 1 post/dia já é a regra da lane.

## 7. Status do teste
edge-tts **7.2.8** confirmado neste PC; `pt-BR-AntonioNeural` sintetizou mp3 válido (8,3s). Vozes pt-BR disponíveis: Antonio (M), Francisca (F), Thalita Multilingual (F). **Rota de fuga operacional.**

> **Em uma frase:** enquanto este ambiente (Claude) e a VPS estiverem de pé, o canal produz livro→skill→biblioteca→vídeo→redes **sem gastar um centavo em IA externa** — só trocando a voz para a grátis.
