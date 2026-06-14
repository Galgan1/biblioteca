# Dossiê de Produção · Story (Robert McKee)

**Status:** AGUARDANDO CHAVE fal.ai — migração para Kling 3.0 feita. Teto Google bloqueou (429); Showrunner optou por migrar de provedor. Pipeline agora suporta `"provider": "fal"` (Flux 2 + Kling 3.0 via fal.ai, fatura separada do Google, ~US$2,70/vídeo). story-mckee.json já marcado `provider: fal`. Falta o Showrunner: criar conta fal.ai + billing + colar a key em `.secrets/fal_key.txt`. Depois: smoke test (valida ids/args reais) → build → QC → upload → link.
**Código novo:** `falgen.py` (gen/animate, mesma assinatura de imagen/veo); `gerar_video.py` com seletor de provedor + `_clip_dur` (palíndromo auto-detecta 5s Kling vs 8s Veo).
**Pedido do Showrunner:** vídeo do livro Story com verificação do roteiro contra os princípios do próprio autor (máx 3 loops), sem pedir autorização, entregar só o link.

## Decisões em nome do Showrunner
- **Título:** "Por que você não consegue parar de assistir? | Story, Robert McKee" (pergunta universal + termo de busca)
- **Arte:** carvão + âmbar tungstênio + luz prata de projetor (sala de cinema / escrivaninha do escritor), acento #cfa05a
- **5 cenas Veo:** 1 (cinema/projetor), 3 (a fresta), 8 (sombra do dragão), 10 (cortina do palco), 13 (escrivaninha ao amanhecer)
- Narrações ≤60 palavras, rate 1.0, travessões (regras herdadas dos dossiês anteriores)

## Loop de auditoria McKee (exigência do pedido)
- **Loop 1:** roteiro v1 escrito pelo Roteirista com regras do estúdio.
- **Loop 2:** auditoria independente em sessão fria (agente com a skill story-screenwriting). Veredito: APROVADO COM AJUSTES — 6 achados: (1) CRÍTICO cena 2 paratática quebrava o gap do título; (2) MÉDIO título sem fechamento de loop no encerramento; (3) MÉDIO cenas 5–8 em lista sem pontes; (4) MENOR fábula da milípede sem setup; (5) MENOR formulação "filmes são sobre seus últimos 20 minutos" não é de McKee — removida; (6) MENOR clímax e método misturados na cena 10. Aplicados: 1, 2, 3, 5, 6 integralmente; 4 aceito como risco (McKee usa a fábula fria no próprio livro).
- **Loop 3:** verificação final — cadeia causal completa, motivo "fresta" como sistema de imagem (setup cena 2 → payoff cena 13), eco "trinta anos" eliminado, fidelidade ok. **PASS.**

## Lições aplicadas dos dossiês anteriores
≤60 palavras/cena (evitou os 3 rebuilds do maquiavel-pedagogo) · travessão p/ TTS · números por extenso · sem crianças em imagem · flag de mídia sintética no upload
