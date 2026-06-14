# Dossiê de Produção · O Poder do Silêncio (Eckhart Tolle)

**Status:** PUBLICADO (unlisted, autopilot) — https://youtu.be/A9vOvkLDj0w · 4:48, 6,4 MB
**Skill-fonte:** `poder-do-silencio` (revisada e aprovada — 10 cap., formato book-to-skill consistente; mora em .gemini/config/skills/, não em ~/.claude/skills)

## Decisões em nome do Showrunner
- **Nível BASE (slides escuros + Ken Burns + Iapetus + trilha)** — escolha estética deliberada: cinema (Imagen+Veo) seguia bloqueado pelo teto Google (429 confirmado em 12/jun). Para um livro sobre silêncio/quietude, o minimalismo dark é tematicamente superior, não um downgrade. Custo R$0.
- **Título:** "Quem é você quando os pensamentos param? | O Poder do Silêncio, Eckhart Tolle" (gancho existencial + termo de busca)
- **Acento:** #9bb0c2 (azul-prata sereno, distinto de Arte=âmbar e Maquiavel=azul institucional)
- **CTA novo aplicado:** frase sóbria no encerramento (like + inscrição com motivo) — primeira produção sob a regra.
- Campos `img`/`motion` mantidos no JSON → upgrade para cinema é só flipar `provider: base→google` quando o teto liberar.
- Thumbnail tipográfica pronta em `_thumbs/poder-do-silencio.png` ("SUA MENTE NÃO PARA?") — aplicar quando o canal for verificado (API segue 403).

## Notas técnicas
- QC deu FAIL cosmético: 4 cenas com campo `motion` viram estáticas no base (esperado). Mecânica sã: 4:48, áudio −22 dB mean / −6 dB peak.
- Bug corrigido em gerar_video.py: modo base chamava img_gen=None → guard `and img_gen`.
- Arco McKee: gancho = problema do espectador (mente que não desliga); clímax na cena 11 (fim do sofrimento); pontes causais; ≤60 palavras/cena, rate 1.0, travessões.

## Shorts (4, unlisted, auto via produzir_shorts.py)
cena2 14rnTJohWVE · cena3 O-6kZG-2vZY · cena8 EJklw9g3QEU · cena11 J97o4aCYU3A. Geração+upload automáticos; fundo escuro (base). `"shorts":[2,3,8,11]` no roteiro.

## Reversão de canal (12/jun)
REVERTIDO p/ Minuto Real — novo longo 3X5s-p2LH9c; reagendado. Cópias antigas (canal pessoal André Galgani) neutralizadas/privadas, a apagar no Studio.
