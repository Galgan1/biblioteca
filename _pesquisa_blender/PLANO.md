# Pesquisa Blender — Plano (loop-agente + Akita)

> Constituição desta tarefa. Estado: em execução (19/jun/2026).

## Tarefa-mãe
1. Conectar o BlenderMCP aos repositórios gratuitos (Poly Haven ✅ ativo / Sketchfab ⚠️ precisa de API key).
2. Mapear ONDE os melhores artistas de Blender postam e baixam inspiração/assets (grátis).
3. Aprender com os livros/skills já "skillizados" na biblioteca (skill `blender` + correlatas) para melhorar o ofício 3D.

## Execução
- **Cross-model:** pesquisadores = `claude-sonnet-4-6`; juiz = `claude-opus-4-8` (oposto ao autor).
- **Parada:** 5 ciclos. Corte: **nota ≥ 8/10** por entrega (juiz severo).
- Saída de cada subagente: arquivo `_pesquisa_blender/R*.md` + resumo + auto-nota.

## RÚBRICA (juiz, /10, corte ≥ 8)
1. **Veracidade [eliminatório]** — fontes reais, URL que resolve, licença correta. Link inventado/licença errada → < 8.
2. **Curadoria** — onde os melhores de fato postam/baixam; não lista de SEO. Separa inspiração de assets; indica nível.
3. **Acionabilidade** — cada item: o que é · licença · como usar; destaca integração com BlenderMCP; próximo passo.
4. **Ofício (R5/R6)** — princípio não-trivial → ação concreta no Blender.
5. **pt-BR, conciso** (pt-PT reprova).

## Subagentes
| # | Foco | Saída |
|---|---|---|
| R1 | Modelos 3D grátis | R1_modelos.md |
| R2 | HDRIs · texturas · materiais | R2_hdri_texturas.md |
| R3 | Inspiração / portfólios | R3_inspiracao.md |
| R4 | Comunidades & aprendizado | R4_comunidades.md |
| R5 | Destilar skill `blender` | R5_skill_blender.md |
| R6 | Destilar skills correlatas | R6_skills_correlatas.md |
