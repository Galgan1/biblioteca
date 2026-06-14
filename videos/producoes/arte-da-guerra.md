# Dossiê de Produção · A Arte da Guerra (Sun Tzu)

**Status:** v4 PUBLICADA (unlisted) — https://youtu.be/zLqdMHJ-k8A · título "O tratado de guerra que manda você NÃO lutar | A Arte da Guerra, Sun Tzu" · flag de mídia sintética enviada · local 4:53, 43,4 MB, QC PASS
**A apagar pelo Showrunner no Studio:** v1 jF54mM0g2Ps · v2 ezngaUm8MHc
**v4 (2026-06-12):** gancho reescrito via McKee/story-screenwriting (Proposta A — paradoxo; cena 1 = 28,8s); flag `containsSyntheticMedia` adicionada ao upload; divulgação de IA na descrição. Proposta B reprovada no fact-check (Boju 506 a.C. foi batalha decisiva; Sun Tzu ausente do Zuo Zhuan) — corrigida como B-v2 no histórico da conversa, não usada. Pendentes (opcionais): pontes entre cenas, reescrita da cena 9, metáfora do falcão (cena 7).
**Publicado:** versão ANTIGA no ar (unlisted) https://youtu.be/ezngaUm8MHc (sem movimento Veo) — versão atual NÃO publicada
**Custo real:** ~US$ 6,50 (12 imagens Imagen ≈ 0,48 + 5 clipes Veo fast ≈ 6,00 + TTS centavos)

## Histórico de decisões
- Estilo aprovado pelo Showrunner: cinema épico âmbar/carvão, voz Iapetus 0.96, acento #d8a64a
- v1: edge-tts (jF54mM0g2Ps) → v2: Iapetus + Imagen + Ken Burns (ezngaUm8MHc) → v3: + 5 cenas Veo (local)
- Cenas animadas: 0 (abertura/push-in), 5 (névoa), 7 (água), 9 (dragão), 12 (pôr do sol)

## Revisão do estúdio (2026-06-11) — achados

### Conferência técnica (Editores Assistentes) — PASS
- 4:38 total; 13/13 cenas; cenas entre 18,1–25,2s (dentro de 12–30s); áudio AAC presente
- Movimento real verificado nas 5 cenas Veo (diff luminância início/ápice: 24,8 / 14,9 / 6,8 / 9,7 / 9,5 — todos > 3)

### Editor Chefe — ACHADOS (médios)
1. **Gancho fraco (cena 1):** abre com aula de história ("Há mais de dois mil anos...") em vez do problema do espectador. Padrão do estúdio: 3s para o espectador sentir que é sobre a vida dele.
2. **Pontes paratáticas:** cenas começam "do zero" ("Para Sun Tzu...", "Esta é a máxima...") — faltam pontes causais e loops de promessa ("a próxima é a mais perigosa").
3. Clímax razoável (cenas 10–11 fortes), final com peso ✓.
   *Decisão: corrigível no roteiro v2 por ~centavos (regerar TTS de 2–3 cenas + rebuild de caches). Ou aceitar para este vídeo e aplicar no próximo.*

### Editor Chefe (2ª passada, sessão fria 2026-06-11) — achados adicionais
4. **[CRÍTICO] Cena 9 ("Conheça o terreno") é recapitulação disfarçada** — repete cenas 3 e 4, sem motion, frase final conclusiva (sinaliza fim). Maior buraco de retenção do vídeo. Recomendação: reescrever com os 6 tipos de terreno + consequências, ou fundir com a cena 4.
5. **Cena 7: metáfora verbal ≠ visual** — narração diz "notas de uma melodia", imagem mostra falcão em mergulho. Unificar (preferir o falcão no texto).
6. **Cena 4: lista abstrata** dos 5 fatores sem exemplo concreto — ancorar em batalha real ou pergunta retórica.
7. **Cena 12 → 13 sem ponte de antecipação** — adicionar gancho ("tudo afunda se o líder cometer um destes erros...").

### VFX / Colorista / Som — PASS
- Palíndromo invisível (água: frames pré/pós-reversão idênticos a olho)
- Contact sheet coeso: paleta âmbar/carvão consistente nas 13 cenas (cena 4 "tochas" é a mais quente, dentro da paleta)
- Mix: mean -21,3 dB, max -5,6 dB (sem clipping; trilha sob a voz ✓)

### Jurídico — ACHADOS (1 bloqueante)
1. **[BLOQUEANTE] Flag de mídia sintética ausente no upload**: `upload_youtube.py` não seta a declaração de conteúdo gerado/alterado por IA exigida pela política do YouTube para visual+voz sintéticos realistas. Adicionar antes do próximo upload.
2. Descrição não menciona produção com IA — adicionar 1 linha.
3. Versão desatualizada no ar; antiga v1 (jF54mM0g2Ps) ainda não apagada pelo Showrunner.
4. `.secrets/` fora de versionamento ✓ · unlisted-first ✓ · assets 100% gerados ✓

### Ideação/Empacotamento (retroativo) — ACHADO (alto impacto, custo zero)
- Título atual "A Arte da Guerra, de Sun Tzu — Resumo em 5 minutos" é descritivo, CTR-fraco.
- Sem thumbnail custom (YouTube escolhe frame) — maior alavanca de CTR não usada.
- Finalistas propostos ao Showrunner (ver relatório da revisão na conversa de 2026-06-11).

### Cientista de Dados — sem dados ainda
- Vídeo unlisted, sem tráfego. Plano de medição pós-publicação: CTR alvo ≥ 4%; queda nos primeiros 30s < 40%; mapear vales da curva → cena; A/B de thumbnail.

### Revisor de Língua Portuguesa (1ª passada, sessão fria 2026-06-12) — v4 publicada
- **Zero bloqueantes** (v4 pode permanecer no ar). 12 itens ⚠️ recomendados para a próxima síntese:
  - **Dois-pontos antes de lista → travessão** (cenas 4, 5, 7, 8, 9): risco do Iapetus colapsar a pausa
  - Período de 32 palavras na cena 7 (quebrar); sujeito elíptico ambíguo (cenas 1, 3); eco "que se deixa X" 3× (cena 11)
  - Testar pronúncia "Sun Tzu" no Iapetus (cenas 1, 12); descrição: "a si e ao inimigo" → "a si mesmo e ao inimigo"
- Aplicar em eventual v5 ou herdar como padrão nos próximos roteiros (regra nova: travessão em vez de dois-pontos em texto para TTS).

## Lições já incorporadas ao estúdio
1. Gancho ≠ contexto histórico → abrir pelo problema do espectador (codificado em desenvolvimento.md)
2. Prompts de motion ambientes/oscilatórios escondem o palíndromo (codificado em producao.md)
3. Empacotamento antes do roteiro — este vídeo foi feito ao contrário; o próximo segue o fluxo do estúdio
