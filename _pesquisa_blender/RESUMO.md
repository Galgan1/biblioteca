# Blender — Onde se inspirar/baixar + o que aprendi (síntese)

> Pesquisa cross-model (6 subagentes Sonnet → juiz Opus severo, corte ≥8). Todas as 6 entregas aprovadas em 2 ciclos. Detalhe em `R1`–`R6`. Estado: 19/jun/2026.

## Conexão BlenderMCP (estado real)
- **Poly Haven** — ✅ ligado e testado ao vivo (CC0, sem chave). Tool: `download_polyhaven_asset(asset_id, asset_type, resolution, file_format)`. Prova: HDRI `kloppenheim_06_puresky` aplicado ao mundo da cena da rua.
- **Sketchfab** — ✅ habilitado, ⚠️ falta **API key grátis** (`blendermcp_sketchfab_api_key` vazio). Conta Sketchfab → Settings → Password & API → API Token → colar no campo "API Key" do painel. Tools: `search_sketchfab_models(query, categories, count, downloadable)` e `download_sketchfab_model(uid, target_size)` — **a tool NÃO filtra licença; conferir CC/CC0 manualmente**.
- Hyper3D/Hunyuan — dispensados pelo usuário.

## ASSETS grátis (baixar e usar)
**Modelos 3D** — TOP comercial-seguro: **Poly Haven** (CC0, MCP), **BlenderKit** (free tier, add-on nativo), **Sketchfab** (CC, MCP, checar licença/modelo). Também: BlendSwap (CC), Blender Studio demo files (CC-BY, atribuição), Fab/Megascans (Fab Standard; ~1.500 grátis curados), Khronos glTF samples. Evitar p/ produção: Objaverse.

**HDRIs · texturas · materiais** — **Poly Haven** (CC0, MCP, até 16K), **ambientCG** (CC0), **3DTextures.me** (CC0 em 1K), **TextureCan** (CC0), **BlenderKit** (RF+CC0). Proprietário-grátis (sem redistribuir): Poliigon free, ShareTextures. *HDRI Haven/Texture Haven → migraram p/ Poly Haven; cc0textures → ambientCG.*
Combo rápido p/ iluminar: `kloppenheim_06_puresky` (exterior) / `dancing_hall` (interior), 2K, 1 chamada.

## INSPIRAÇÃO (postar/estudar — NÃO baixar p/ usar)
TOP 3: **ArtStation**, **Blender Artists ("Finished Projects") + BlenderNation**, **80.lv** (única que explica o *processo*). Também: **Sketchfab Staff Picks/Masters** (orbita o modelo, estuda topologia), **r/blender** (curadoria por votos + autores explicam), **Behance** (product viz). CGSociety/CGTalk: encerrada (jan/2024).

## APRENDER / COMUNIDADE
- **Do zero:** Blender Manual + Blender Studio Fundamentals (LTS) → donut do **Blender Guru** → **Grant Abbitt**, **CG Cookie**, **CG Boost**.
- **Avançado:** Josh Gambrell (hard-surface), Ducky 3D (procedural/motion), CGMatter/Default Cube (Geometry Nodes), Curtis Holt (Python/add-ons), Ian Hubert (VFX "lazy tutorials"), Polygon Runway (ilustração 3D).
- **Dúvida/comunidade:** Blender Artists, r/blender, Blender Stack Exchange, Discord oficial.

## OFÍCIO destilado (skill `blender` + correlatas) → ação
1. **Render/cor:** Cycles + **OptiX** (ordem: `compute_device_type`→`get_devices()`→habilitar→`device='GPU'`), denoise OptiX, **AgX** como view transform.
2. **Material:** Principled BSDF 4.x — nomes certos (`Specular IOR Level`, `Coat Weight/Roughness`); alpha por nó.
3. **Luz:** HDRI único p/ coesão cromática; truque `Light Path → Is Camera Ray` (fundo limpo, reflexo do HDRI); 3 pontos nomeados (key/fill/rim); **temperatura de cor = intenção narrativa**.
4. **Câmera:** ~85mm, sensor 36mm, DoF calibrado; **`rotation_euler` explícito — nunca `TRACK_TO` no headless** (tela vazia 2×). Progressão wide→médio→detalhe espelha a emoção.
5. **Composição/clareza (Krug/Norman):** hierarquia por contraste de valor + DoF; silhueta legível; fundo que serve, não compete; regra dos terços via posição de câmera.
6. **Narrativa visual (Poética/McKee/Chion):** mimese = coerência interna; peripécia = virada de luz no mesmo espaço; reconhecimento = o detalhe do "reveal" já plantado antes; catarse = clímax num eixo só (eleos OU phobos); **render só se aprova com a trilha** (Chion: valor acrescentado).
7. **Pipeline (gotchas):** Blender 5.x sem `action.fcurves` (usar layers/channelbags); build sem FFMPEG → render PNG + juntar no ffmpeg; ops precisam de contexto; `from_pydata` seguro no headless; **câmera animada NÃO pode atravessar mesh** (interior fechado = frame preto) → validar a TRAJETÓRIA inteira contra os bounding boxes, nunca 1 frame só; QC: frame preto = PNG de tamanho constante << mediana.

## Arquivos
`R1_modelos.md` · `R2_hdri_texturas.md` · `R3_inspiracao.md` · `R4_comunidades.md` · `R5_skill_blender.md` · `R6_skills_correlatas.md` · `PLANO.md`
