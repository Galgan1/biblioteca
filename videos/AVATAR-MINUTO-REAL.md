# Avatar do Minuto Real — Persona-Bible + Plano de Criação (HeyGen)

> Investigação Akita (`/loop-agente`, 3 frentes: HeyGen técnico · design de credibilidade · fit de marca). Objetivo: uma figura que **transpareça credibilidade**, coerente com a marca.

## STATUS (21/jun) — ROSTO CRIADO ✅ (grátis, NVIDIA)
- **HeyGen CANCELADO.** Pivot para **NVIDIA NIM (Flux)** — grátis (key `nvapi-`, sem cartão), alinhado à soberania. Ferramenta: `videos/nvidia.py` (`python nvidia.py face`; gerador de imagem grátis reutilizável).
- **Rosto oficial:** `videos/_canal/avatar_narrador.png` — opção **A** (`flux.1-dev`, seed 0). Aprovado na rúbrica (autoridade+calor · preto-e-ouro · anti-uncanny). ⚠️ está **gitignored** → GitGuy deve versionar (brand asset).
- **Talking-head (falar):** DEFERIDO — depois decidir entre **fal Kling Avatar** (pago, foto→lip-sync fácil) e **NVIDIA Audio2Face + Blender** (grátis, 3D, pesado). HeyGen saiu.
- **Onde entra:** capa dos Shorts + intro/outro dos longos (não talking-head o vídeo todo).

## Veredito da persona — "O Narrador do Minuto Real"
A encarnação **visual da voz que o público já ouve** (Iapetus/AntonioNeural — masculina, sóbria). Credibilidade = **competência + calor**, no ponto "connector" de Cialdini (expert que mostra curiosidade, não só autoridade).

- **Quem:** homem brasileiro, **~42–48 anos**, pele neutra a morena clara, cabelo curto bem-cuidado com leve grisalho nas têmporas (autoridade + segurança anti-uncanny), expressão **calma e concentrada** com **micro-sorriso contido** ao introduzir um insight (o calor), **olhar direto** à câmera. Óculos de armação fina = opcional (eleva inteligência percebida).
- **Traje:** camisa/malha fina **escura** (preto/chumbo), **sem gravata, sem blazer claro** — roupa que **some no fundo escuro**; ficam o rosto e os olhos (espelha o que a tipografia já faz no banner).
- **Cenário/luz:** **fundo preto-carbono** (`#08080c`) com **uma luz direcional âmbar/ouro** lateral (Rembrandt, `#d8a64a`) — editorial, premium. **NÃO** estante iluminada nem fundo claro/verde (quebraria a marca preto-e-ouro).
- **Enquadramento/movimento:** **plano busto** (cabeça + ombros), câmera ao nível dos olhos ou 3–5° acima; **movimento contido** (casa com a cadência lenta do Iapetus); `expressiveness: low–medium`.
- **Voz:** a do canal — **Iapetus/AntonioNeural**, passada como **áudio externo** ao HeyGen (preserva a identidade sonora; rosto combina com a voz).
- **Nome:** recomendação = **sem nome próprio** ("O Narrador" / "narração e imagem por IA" nos créditos). Se quiser nome: **Lúcio** (aceno a Sêneca — casa com filosofia/estratégia) ou **Rafael**.
- **Transparência:** declarar "narração e imagem por IA" (a pesquisa de credibilidade mostra que assumir a IA **antes** protege a confiança).
- **Onde aparece:** 1º nos **Shorts** (rosto no frame de capa, escurecido sob o texto) + **intro/outro** dos longos (quadro 3–5s, fade). **Não** talking-head o vídeo inteiro (quebraria a estética cinematográfica).

## Prompt do rosto sintético (pronto p/ Imagen/Flux/Midjourney/HeyGen-prompt)
> Photorealistic editorial portrait of a Brazilian man, ~45 years old, neutral-to-light-brown skin, short well-groomed dark hair with subtle gray at the temples, calm composed concentrated expression with a faint closed-mouth micro-smile, **direct eye contact with camera**, subtle catchlight in the eyes, visible natural skin texture and pores; wearing a dark charcoal fine shirt (no tie, no blazer); **black-carbon background (#08080c)** lit by a single warm amber/gold directional Rembrandt side-light (#d8a64a); bust shot (head and shoulders), eye-level, **mouth very slightly open and relaxed**; soft 45° key light, premium cinematic mood; 4K, frontal, sharp focus on the eyes.
- Requisitos anti-uncanny (HeyGen Photo Avatar): frontal, rosto único, **boca levemente aberta** (evita artefato de dentes), luz uniforme, fundo simples, alta resolução, sem óculos escuros/sombra dura.

## Plano de criação no HeyGen (rota recomendada: Photo Avatar + áudio externo)
1. **Gerar o rosto** (uma vez) com o prompt acima → imagem 1080p+.
2. **Registrar no HeyGen:** `POST /v3/avatars` com `type:"photo"` (ou `type:"prompt"` p/ gerar dentro do HeyGen) → guarda `avatar_id` + `avatar_group_id`.
3. **Por vídeo:** o pipeline gera o áudio (Iapetus/edge) → upload (`audio_asset_id`) ou URL → `POST /v3/videos` com `avatar_id` + `engine:{type:"avatar_iv"}` + `aspect_ratio` + `1080p` → polling `video_id` → baixa o MP4 → monta no pipeline (`ffmpeg`).
- **Pré-requisitos:** plano **Creator US$29/mês** (API + Avatar IV + sem marca d'água) + **API key**. Custo: Avatar IV = 20 créditos/min (200/mês ≈ 10 min). Voz pt-BR própria via áudio externo (sem depender das vozes do HeyGen).
- ⚠️ **REALIDADE DE CRÉDITO (testado 21/jun, key válida):** a conta está no **free** (`remaining_quota: 0` pago; **3 grátis de imagem + 3 de Avatar IV**). Mas a **API exige créditos PAGOS** (`insufficient_credit: requires 'api' credits`) — **os grátis só valem na UI web**. Logo: ou (a) adicionar créditos de API (PAYG dep. mín. US$5, ou Creator) → rodar `heygen_avatar.py generate/group`; ou (b) usar os 3 grátis **na UI web** (você cria, ou eu dirijo o navegador). A ferramenta `heygen_avatar.py` está pronta p/ a rota (a).
- **HeyGen termina no MP4** — upload segue pelo nosso pipeline (`upload_youtube`/`instagram_post`).

## Rúbrica de credibilidade (PASS/FAIL — os juízes verificam o rosto gerado)
1. **Autoridade:** idade/porte/traje/luz de "quem leu os grandes livros" (Cialdini).
2. **Calor:** micro-sorriso contido + olhar direto; não vendedor, não frio.
3. **Fit de marca:** preto-e-ouro, masculino, sóbrio — combina com a voz Iapetus e o banner.
4. **Anti-uncanny:** catchlight nos olhos, textura de pele, boca levemente aberta, movimento contido; sem "olhar morto"/lip-sync quebrado.
5. **Produção:** caminho HeyGen reproduzível + custo conhecido + esta bible escrita.

## Decisão pendente (portão humano — antes de gastar crédito/criar a face do canal)
Persona (gênero/idade/arquétipo) · caminho de acesso ao HeyGen (API key / você na UI / eu no navegador) · fonte da imagem do rosto (HeyGen-prompt / nosso Imagen pago / você fornece) · com ou sem nome.
