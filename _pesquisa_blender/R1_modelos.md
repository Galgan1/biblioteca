# R1 — Melhores Fontes Gratuitas de Modelos 3D para Blender

> Pesquisa verificada em junho de 2026. Todas as URLs foram confirmadas via WebSearch/WebFetch.
> Foco: modelos mesh/assets (não apenas texturas ou HDRIs).

---

## Tabela Principal

| # | Nome | O que é / Tipo de conteúdo | Licença | Uso comercial? | URL verificada | Formatos | Integra com BlenderMCP? |
|---|------|---------------------------|---------|----------------|----------------|----------|------------------------|
| 1 | **Poly Haven** | Biblioteca CC0 de modelos fotorrealistas (props, móveis, natureza, ferramentas), HDRIs e texturas. +1.700 assets totais; seção de modelos crescendo. | **CC0** (Domínio Público) | Sim, sem restrições. Sem atribuição obrigatória. | [polyhaven.com/models](https://polyhaven.com/models) | .blend, FBX, glTF, USD (até 8K) | **SIM** — `download_polyhaven_asset(asset_id, asset_type="models", resolution="2k")` + `search_polyhaven_assets()`. Funciona via `get_polyhaven_status()` primeiro. Nenhuma API key necessária. |
| 2 | **Sketchfab** | Maior plataforma de visualização/download 3D. Centenas de milhares de modelos sob Creative Commons disponíveis para download. Filtra por licença (CC0, CC-BY, CC-BY-SA etc). | **CC0** (subset) / **CC-BY** / **CC-BY-SA** (maioria) — varia por modelo | CC0 = sim sem restrição. CC-BY = sim com atribuição. CC-BY-NC = não comercial. Filtrar sempre. | [sketchfab.com/features/free-3d-models](https://sketchfab.com/features/free-3d-models) | glTF, GLB, USDZ, OBJ, FBX (via API) | **SIM** — `download_sketchfab_model(uid="...", target_size=1.0)`. **Exige API key gratuita**: criar conta em sketchfab.com → Settings → Password & API → gerar token → inserir no add-on BlenderMCP ("Use assets from Sketchfab" + token). A licença NÃO é filtrada pela tool — verificar manualmente no site. |
| 3 | **BlenderKit** | Biblioteca integrada ao Blender (add-on oficial). +63.000 assets gratuitos (modelos, materiais, HDRIs, cenas). 47% do catálogo total é free. Sem login obrigatório para o plano free. | **CC0** e **Royalty-Free** (ambos permitem comercial) | Sim em ambas. RF proíbe revender o modelo como arquivo avulso, mas permite em produtos (renders, jogos, vídeos). | [blenderkit.com](https://www.blenderkit.com/) | .blend nativo (importação direta no Blender) | **NÃO nativamente** via BlenderMCP, mas o add-on oficial BlenderKit opera dentro do Blender — para automação via MCP usaria execute_blender_code() com a API do BlenderKit. |
| 4 | **BlendSwap** | Comunidade de .blend files compartilhados por artistas Blender. +70.000 arquivos. Foco em Blender nativo. | **CC0**, **CC-BY**, **CC-BY-SA**, **CC-BY-ND**, **CC-BY-NC-SA** — varia por upload | CC0 e CC-BY = sim comercial. CC-BY-NC = não comercial. Filtrar por licença. | [blendswap.com](https://www.blendswap.com/) | .blend exclusivamente | **NÃO** — download manual. Requer conta gratuita. Limite mensal de download. |
| 5 | **Blender Studio / Demo Files** | Assets dos open movies oficiais da Blender Foundation (Cosmos Laundromat, Sprite Fright, Singularity etc). Produção cinematográfica real: personagens rigged, ambientes, shaders complexos. Referência técnica definitiva. | **CC-BY 4.0** (Creative Commons Attribution) | Sim, com atribuição obrigatória ("Blender Foundation / Blender Studio"). Logos e marcas excluídos. | [blender.org/download/demo-files](https://www.blender.org/download/demo-files/) | .blend nativos (assets de produção) | **NÃO** via BlenderMCP — download manual do site. Mas arquivos .blend abrem direto no Blender. |
| 6 | **Fab (ex-Quixel Megascans)** | Marketplace da Epic Games. Seção gratuita: +1.500 Megascans hand-picked + ativos gratuitos rotativos (novos a cada 2 semanas). Fotogrametria profissional. | **Fab Standard License** (proprietária) | Sim — permitido em jogos, animações, VFX, renders, qualquer engine/ferramenta incluindo Blender. Proibido: redistribuir assets isolados, projetos 100% open-source. | [fab.com](https://www.fab.com/) | FBX, OBJ, glTF/GLB, USDZ, formatos nativos UE | **NÃO** via BlenderMCP. Download manual via launcher Epic ou Fab Bridge. Conta gratuita obrigatória. |
| 7 | **CGTrader (seção free)** | Marketplace com +200.000 modelos, subconjunto gratuito significativo. Qualidade variável — buscar por "free" + filtro de licença. | **Royalty-Free** (proprietária CGTrader) | Sim — pode usar em produtos comerciais (jogos, renders, animações) desde que o modelo esteja incorporado. Proibido: redistribuir o arquivo 3D avulso ou imprimir e vender isolado. | [cgtrader.com/free-3d-models](https://www.cgtrader.com/free-3d-models) | OBJ, FBX, 3DS, MAX, C4D, STL, glTF | **NÃO** — download manual. Conta gratuita obrigatória. |
| 8 | **TurboSquid / Free3D** | TurboSquid: +7.800 modelos gratuitos (marca "Free"). Free3D: sub-marca do TurboSquid com acervo adicional. Modelos de estúdios profissionais. | **Royalty-Free TurboSquid** (proprietária) | Sim para uso incorporado em produções. Conteúdo com tag "Editorial" = NÃO comercial. Sem revenda de arquivo avulso. | [turbosquid.com/Search/3D-Models/free](https://www.turbosquid.com/Search/3D-Models/free) / [free3d.com](https://free3d.com/) | .blend, OBJ, FBX, MAX, C4D, glTF | **NÃO** — download manual. Conta TurboSquid gratuita. |
| 9 | **Khronos glTF Sample Assets** | Repositório oficial do Grupo Khronos com modelos de referência para testar o formato glTF 2.0. Toy Car, Damaged Helmet, Sponza, etc. Ideal para testes de pipeline e PBR. | **CC BY 4.0** (maioria) / algumas em **CC0** — checar README de cada modelo | CC-BY = sim comercial com atribuição. Ver licença individual por modelo. | [github.com/KhronosGroup/glTF-Sample-Assets](https://github.com/KhronosGroup/glTF-Sample-Assets) | glTF, GLB, glTF-Binary | **PARCIAL** — glTF importa nativamente no Blender; via BlenderMCP pode-se usar `execute_blender_code()` para importar. |
| 10 | **Objaverse / Objaverse-XL** | Dataset de pesquisa com 800K–10M+ modelos 3D, principalmente de Sketchfab. Uso primário: treinamento de IA e pesquisa. Qualidade inconsistente para produção. | **ODC-By v1.0** (dataset); modelos individuais variam (CC0, CC-BY, etc.) | Depende de cada modelo individual. Como banco de dados de pesquisa, não é adequado para busca curada de assets de produção. | [objaverse.allenai.org](https://objaverse.allenai.org/) | glTF, OBJ, FBX (mix) | **NÃO** — ferramenta de pesquisa/IA, não de produção. |
| 11 | **ambientCG** | PBR materials e modelos de fotogrametria CC0. Mais forte em texturas, mas tem seção de modelos 3D (objetos scaneados). Sem conta, sem registro. | **CC0** (Domínio Público) | Sim, sem restrições, sem atribuição. | [ambientcg.com](https://ambientcg.com/) | glTF, OBJ, FBX (até 8K maps) | **NÃO** nativamente via BlenderMCP — mas integra via Blender Asset Browser (add-on em desenvolvimento). |

---

## Notas Críticas de Licença

### Poly Haven CC0 — mais segura do mercado
Literalmente domínio público. Pode distribuir renders, vender produtos, modificar, redistribuir o próprio asset, sem nem precisar citar. Nenhuma outra fonte paga ou gratuita oferece isso com esta qualidade fotográfica.

### Sketchfab — filtrar SEMPRE a licença
A plataforma mistura CC0, CC-BY, CC-BY-SA, CC-BY-NC e até modelos com licença restritiva. Nunca baixar sem verificar a licença do modelo individual. Para uso comercial seguro: filtrar `license=cc0` ou `license=by`.

### Fab Standard License — atenção: não é CC
É licença proprietária da Epic. Permite uso comercial em qualquer engine, mas proíbe redistribuir os assets isolados e uso em projetos open-source puros. Adequada para vídeos e animações do canal, mas leia o EULA antes de qualquer uso novo.

### BlendSwap — qualidade variável, verificar licença por arquivo
Cada blend tem sua licença definida pelo uploader. Filtrar por CC0 ou CC-BY antes de baixar para uso comercial.

---

## Integração BlenderMCP — Guia Prático

### Poly Haven (nativo, sem API key)
```
# 1. Verificar se está ativo
get_polyhaven_status()

# 2. Buscar modelos (sem parâmetro query; use asset_type + categories)
search_polyhaven_assets(asset_type="models", categories="furniture")

# 3. Baixar e importar na cena atual (file_format válido para modelos: "gltf" ou "fbx")
download_polyhaven_asset(
    asset_id="log_stool",
    asset_type="models",
    resolution="2k",
    file_format="gltf"
)
```

### Sketchfab (exige API key gratuita)
```
# Pré-requisito: conta em sketchfab.com → Settings → Password & API → copiar token
# No add-on BlenderMCP: marcar "Use assets from Sketchfab" + colar token

# Verificar status
get_sketchfab_status()

# Buscar modelos downloadáveis (downloadable=True NÃO garante licença CC —
# a tool não filtra por licença; verificar manualmente no resultado/site Sketchfab)
search_sketchfab_models(
    query="wooden crate",
    downloadable=True
)

# Baixar (UID do modelo; target_size obrigatório: maior dimensão em metros; sem parâmetro format)
download_sketchfab_model(
    uid="abc123...",
    target_size=1.0
)
```

---

## TOP 3 para Uso Comercial Seguro

### 1. Poly Haven — OURO
**Por que é a melhor:** CC0 real (domínio público), sem advogado, sem atribuição, sem restrições de tipo de uso. Qualidade fotorrealista de fotogrametria profissional. Integração nativa e zero-fricção no BlenderMCP: um comando e o modelo aparece na cena. Para renders, vídeos e animações do canal Minuto Real, é o ponto de partida obrigatório.

### 2. BlenderKit (plano free)
**Por que é a segunda:** +63.000 assets, add-on integrado ao Blender, RF e CC0 permitem uso comercial, sem fricção de download manual. A desvantagem é que não integra nativamente ao BlenderMCP (usa o próprio add-on dentro do Blender), mas para fluxo de trabalho com o Blender GUI aberto é imbatível em conveniência.

### 3. Sketchfab (filtro CC-BY / CC0)
**Por que é a terceira:** Variedade incomparável (centenas de milhares de modelos sob Creative Commons), integração nativa via BlenderMCP com `download_sketchfab_model`. A API key gratuita é o único requisito. Risco principal: a tool não filtra por licença — verificar manualmente no site antes de usar.

---

## Fontes que NÃO recomendo para uso comercial desatento

| Fonte | Motivo |
|-------|--------|
| **Objaverse** | Dataset de IA, não curado para produção. Qualidade ruim na maioria. |
| **Free3D/TurboSquid free** | Royalty-free proprietária com restrições pouco claras. Conteúdo "Editorial" é armadilha. |
| **CGTrader free** | Proíbe redistribuição do arquivo — limite para reusar em múltiplos produtos. |

---

## Referências Verificadas

- [Poly Haven — Licença CC0](https://polyhaven.com/license)
- [Poly Haven — Modelos](https://polyhaven.com/models)
- [Sketchfab — Free 3D Models](https://sketchfab.com/features/free-3d-models)
- [Sketchfab — Download API](https://sketchfab.com/developers/download-api)
- [BlenderKit — Licenças](https://www.blenderkit.com/docs/licenses/)
- [BlenderKit — Sobre](https://www.blenderkit.com/about-blenderkit)
- [BlendSwap](https://www.blendswap.com/)
- [Blender Demo Files](https://www.blender.org/download/demo-files/)
- [Blender Studio — Sprite Fright (CC-BY 4.0)](https://studio.blender.org/projects/sprite-fright/)
- [Fab.com — Megascans free](https://www.fab.com/megascans-free)
- [Fab Standard License](https://www.fab.com/eula?lang=en)
- [CGTrader — Free 3D Models](https://www.cgtrader.com/free-3d-models)
- [TurboSquid — Free Models](https://www.turbosquid.com/Search/3D-Models/free)
- [Free3D](https://free3d.com/)
- [Khronos glTF Sample Assets](https://github.com/KhronosGroup/glTF-Sample-Assets)
- [Objaverse](https://objaverse.allenai.org/)
- [ambientCG](https://ambientcg.com/)
- [BlenderMCP — download_polyhaven_asset (Glama)](https://glama.ai/mcp/servers/@Eminemminem/blender-mcp/tools/download_polyhaven_asset)
- [CG Channel — Megascans free até 2024](https://www.cgchannel.com/2024/10/epic-games-has-made-megascans-free-to-all-but-only-until-the-end-of-2024/)
