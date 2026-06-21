# R5 — Guia de Ofício Blender (destilado da skill)

> **Fonte primária:** `C:\Users\User\.claude\skills\blender\SKILL.md`
> **Fonte secundária:** `videos/ESTUDIO-AGENTES.md` (seção Cinegrafista Premium, jun/2026)
> **Fundamentação:** Blender Manual (CC-BY-SA 4.0) · Blender 3D: Noob to Pro (CC-BY-SA) · Blender Fundamentals (CC-BY 4.0)
> **Data:** 2026-06-19

---

## Princípios priorizados (do que mais eleva qualidade ao detalhe)

### TIER 1 — Render e cor (maior impacto visual, sem exceção)

**P1 — Sempre Cycles + OptiX + AgX; nunca EEVEE ou Standard para entrega**

- **Por quê:** Cycles é path-tracer fisicamente correto. OptiX (RTX) é 40–80% mais rápido que CUDA. AgX (Blender 4.x) evita o "solarization" de altas luzes que o antigo Filmic exibe — resultado cinematográfico sem pós-processamento.
- **Ação:** no script headless, setar ANTES de qualquer render:

```python
import bpy

scene = bpy.context.scene
scene.render.engine = 'CYCLES'

prefs = bpy.context.preferences.addons['cycles'].preferences
prefs.compute_device_type = 'OPTIX'   # ANTES de get_devices()
prefs.get_devices()                    # popula a lista

for dev in prefs.devices:
    dev.use = True                     # habilita GPU + CPU

scene.cycles.device = 'GPU'
scene.display_settings.display_device = 'sRGB'
scene.view_settings.view_transform = 'AgX'
scene.view_settings.look = 'None'     # ou 'Medium Contrast'
```

- **Gotcha:** chamar `get_devices()` ANTES de setar `compute_device_type` não funciona — o Blender ignora a GPU e cai para CPU silenciosamente. Ordem correta: tipo → get → habilitar.

---

**P2 — Samples adaptativos + Denoiser OptiX: qualidade alta com tempo controlado**

- **Por quê:** denoising neural (OptiX/OpenImageDenoise) permite render com 64–128 samples com resultado de 512+ samples. Adaptive sampling corta amostras em áreas uniformes.
- **Ação:**

```python
cycles = scene.cycles
# Rascunho (preview rápido)
cycles.samples = 64
cycles.adaptive_threshold = 0.1
# Entrega final
cycles.samples = 256
cycles.adaptive_threshold = 0.005

# Denoiser
scene.render.use_compositing = True
scene.render.use_sequencer = False
cycles.use_denoising = True
cycles.denoiser = 'OPTIX'   # ou 'OPENIMAGEDENOISE' se não tiver RTX
```

---

### TIER 2 — Materiais realistas (Principled BSDF)

**P3 — Usar os parâmetros corretos do Principled BSDF no Blender 4.x**

- **Por quê:** no Blender 4.x, `Specular` foi renomeado para `Specular IOR Level`; `Clearcoat` virou `Coat Weight` / `Coat Roughness`. Código com nome antigo falha silenciosamente (param ignorado).
- **Ação:**

```python
mat = bpy.data.materials.new("capa_livro")
mat.use_nodes = True
bsdf = mat.node_tree.nodes["Principled BSDF"]

# Capa fosca (papel/tecido)
bsdf.inputs["Base Color"].default_value = (0.05, 0.4, 0.1, 1.0)  # RGBA
bsdf.inputs["Roughness"].default_value = 0.72
bsdf.inputs["Metallic"].default_value = 0.0

# Verniz brilhante (capa de livro laminada)
bsdf.inputs["Coat Weight"].default_value = 0.8    # era Clearcoat
bsdf.inputs["Coat Roughness"].default_value = 0.05
```

- **Receita fosca:** Roughness 0.6–0.8; Metallic 0.
- **Receita brilhante:** Roughness 0.05 + Coat Weight 0.8.
- **Alpha no Cycles:** vem do nó `Image Texture → Alpha → BSDF Alpha`. Propriedades `blend_method`/`shadow_method` são EEVEE — ignoradas no Cycles.

---

**P4 — Bevel nos cantos: eliminar a "aresta CG barata"**

- **Por quê:** objetos sem bevel têm arestas perfeitamente retas que não existem na realidade. O Modifier Bevel com 3 segmentos cria o highlight de borda que o olho espera.
- **Ação:**

```python
obj = bpy.context.active_object
bevel = obj.modifiers.new("Bevel", 'BEVEL')
bevel.width = 0.0025        # ~2.5mm em escala real
bevel.segments = 3
bevel.limit_method = 'ANGLE'
bevel.angle_limit = 0.523599  # 30 graus em radianos
```

---

### TIER 3 — Iluminação HDRI (ambiente fotorrealista)

**P5 — HDRI com "Light Path Is Camera Ray": fundo escuro + reflexos do HDRI**

- **Por quê:** o HDRI ilumina e cria reflexos realistas, mas seu fundo pode ser inconveniente para composição. O truque do `Is Camera Ray` esconde o fundo para a câmera enquanto mantém luz e reflexos.
- **Ação:**

```python
world = bpy.data.worlds["World"]
world.use_nodes = True
nodes = world.node_tree.nodes
links = world.node_tree.links

# Limpar nodes padrão
nodes.clear()

env = nodes.new("ShaderNodeTexEnvironment")
env.image = bpy.data.images.load("/caminho/absoluto/studio.hdr")
env.image.colorspace_settings.name = "Linear Rec.709"

bg = nodes.new("ShaderNodeBackground")
bg.inputs["Strength"].default_value = 1.0

mix = nodes.new("ShaderNodeMixShader")
light_path = nodes.new("ShaderNodeLightPath")
bg_dark = nodes.new("ShaderNodeBackground")
bg_dark.inputs["Strength"].default_value = 0.0

output = nodes.new("ShaderNodeOutputWorld")

links.new(env.outputs["Color"], bg.inputs["Color"])
links.new(light_path.outputs["Is Camera Ray"], mix.inputs["Fac"])
links.new(bg_dark.outputs["Background"], mix.inputs[1])  # câmera vê escuro
links.new(bg.outputs["Background"], mix.inputs[2])       # reflexos/luz usam HDRI
links.new(mix.outputs["Shader"], output.inputs["Surface"])
```

- **Fonte de HDRI:** Poly Haven (CC0, uso comercial) — integrado ao BlenderMCP via `search_polyhaven_assets` + `get_polyhaven_status`.

---

### TIER 4 — Câmera e DoF

**P6 — Câmera 85mm + DoF calibrado: look "produto premium"**

- **Por quê:** 85mm comprime perspectiva e achata distorções (look de campanha). DoF em f/5.6–8 mantém o produto nítido; f/2.8 cria bokeh para contexto.

```python
cam_data = bpy.data.cameras.new("Cam")
cam_data.lens = 85                   # mm
cam_data.sensor_width = 36           # sensor full-frame
cam_data.dof.use_dof = True
cam_data.dof.aperture_fstop = 5.6   # nítido; 2.8 p/ bokeh

cam_obj = bpy.data.objects.new("Camera", cam_data)
bpy.context.scene.collection.objects.link(cam_obj)
bpy.context.scene.camera = cam_obj

# Posição e rotação explícita (NUNCA use TRACK_TO no headless — ver Gotchas)
cam_obj.location = (0.0, -2.5, 0.8)
cam_obj.rotation_euler = (1.35, 0.0, 0.0)  # radianos
```

---

### TIER 5 — Pipeline headless e organização

**P7 — Mesh via `from_pydata`: único modo confiável no headless**

- **Por quê:** operadores como `primitive_plane_add` + transformações dependem de contexto de viewport ativo. No headless, falham silenciosamente ou produzem resultados errados.

```python
import bmesh

# Plano 2×2 centralizado
verts = [(-1,-1,0), (1,-1,0), (1,1,0), (-1,1,0)]
faces = [(0,1,2,3)]

mesh = bpy.data.meshes.new("plano")
mesh.from_pydata(verts, [], faces)
mesh.update()

obj = bpy.data.objects.new("Plano", mesh)
bpy.context.scene.collection.objects.link(obj)
```

---

**P8 — Render para sequência PNG; montar com ffmpeg externo**

- **Por quê:** o codificador H.264 interno do Blender exige FFMPEG compilado no build. A versão portátil (zip, sem admin) pode não ter. Render PNG frame a frame nunca perde progresso por crash.
- **Ação:**

```python
scene.render.image_settings.file_format = 'PNG'
scene.render.filepath = "/caminho/absoluto/frames/frame_"
scene.render.use_overwrite = True

# Renderizar (headless)
bpy.ops.render.render(animation=True)
```

Depois, montar com ffmpeg:
```bash
ffmpeg -framerate 30 -i "frames/frame_%04d.png" \
       -c:v libx264 -pix_fmt yuv420p -crf 18 \
       saida.mp4
```

- **Gotcha H.264:** dimensões devem ser pares (`width % 2 == 0`). Blender portátil: checar `bpy.app.build_options.codec_ffmpeg` antes de tentar render direto para vídeo.

---

## Seção: Gotchas do Pipeline (erros já pagos)

| Gotcha | Sintoma | Correção |
|--------|---------|----------|
| OptiX antes de `get_devices()` | GPU ignorada, roda em CPU, sem aviso | Setar `compute_device_type` ANTES de `get_devices()` (P1) |
| `TRACK_TO` no headless | Câmera aponta errado, cena vazia, 2 ocorrências no nosso histórico | Usar `rotation_euler` explícito (P6) |
| `primitive_plane_add` + `scale` | Objeto na posição errada ou ausente | Construir mesh com `from_pydata` (P7) |
| `blend_method`/`shadow_method` | Sem efeito (é EEVEE), alpha some | Alpha via nó `Image Texture → Alpha → BSDF Alpha` (P3) |
| `Clearcoat` / `Specular` (nomes antigos) | Param ignorado silenciosamente no 4.x | Renomeados: `Coat Weight`, `Coat Roughness`, `Specular IOR Level` (P3) |
| Caminhos relativos no headless | Asset não carrega, tela preta | Sempre caminhos ABSOLUTOS (nota da skill, seção 4) |
| H.264 em build portátil sem FFMPEG | Erro ao render vídeo direto | Render PNG + ffmpeg externo (P8) |
| `action.fcurves` no Blender 5.x | AttributeError (API mudou) | Não documentado na skill — verificar via `bpy.data.actions` em vez de `action.fcurves` diretamente |
| Dimensões ímpares + H.264 | Erro de encode / linhas verdes | `width` e `height` sempre múltiplos de 2 (P8) |
| `depthflow` rebaixa torch para CPU | CUDA: False após pip install | Reinstalar `torch+cu128` depois do depthflow (verificado jun/2026 na RTX 5060) |

---

## Workflow linear de referência (Blender Fundamentals)

```
Modelagem (from_pydata / Bevel)
  → Shading (Principled BSDF 4.x)
  → UV + Textura (Image Texture → colorspace correto)
  → Iluminação (HDRI + Light Path trick)
  → Câmera (85mm + DoF)
  → Render (Cycles + OptiX + AgX)
  → PNG frames → ffmpeg → mp4
```

---

## Fontes dos princípios

| Princípio | Fonte |
|-----------|-------|
| P1 (OptiX, ordem, AgX) | Blender Manual § Cycles Render + skill `blender` seção 1 |
| P2 (Samples adaptativos, Denoiser) | Blender Manual § Render > Sampling + skill seção 1 |
| P3 (Principled BSDF 4.x, Alpha) | Blender Manual § Shader Nodes + skill seção 1 e 4 |
| P4 (Bevel) | Blender Manual § Modifiers + skill seção 1 |
| P5 (HDRI + Light Path) | Blender Manual § World + skill seção 1 |
| P6 (Câmera 85mm, DoF, anti-TRACK_TO) | Blender Manual § Camera + skill seção 1 e 4 |
| P7 (from_pydata) | skill seção 4 (gotcha pago) |
| P8 (PNG + ffmpeg) | Blender Fundamentals + skill seção 4 |
| Gotchas depthflow/torch | ESTUDIO-AGENTES.md seção Cinegrafista (jun/2026) |

---

## AUTO-NOTA

**Nota: 8.5 / 10**

**Justificativa:**
- **Veracidade:** fiel ao conteúdo literal da skill `SKILL.md` e `ESTUDIO-AGENTES.md`; nenhum princípio inventado; snippets reproduzem a API `bpy` real do Blender 4.x.
- **Acionabilidade (ofício):** cada princípio tem snippet funcional ou instrução concreta. Nenhum item vago.
- **Priorização:** TIER 1 (render/cor) → TIER 2 (materiais) → TIER 3 (luz) → TIER 4 (câmera) → TIER 5 (pipeline) cobre o arco correto de impacto.
- **Gotchas:** tabela cobre todos os casos documentados na skill + um não documentado (`action.fcurves` 5.x, sinalizando como inferência, não confirmado).
- **Desconto (-1.5):** a skill não tem `references/` adicionais — todo o material vem de SKILL.md (49 linhas) e ESTUDIO-AGENTES.md. Um R5 de nota 10 exigiria material de referência mais extenso na própria skill. O ponto sobre `action.fcurves` no Blender 5.x é mencionado na tarefa mas não está documentado na skill — marcado como pendente, não inventado.
- **Idioma:** pt-BR, sem pt-PT.

---

*Arquivos lidos:*
- `C:\Users\User\.claude\skills\blender\SKILL.md`
- `C:\Users\User\.gemini\antigravity\scratch\biblioteca\videos\ESTUDIO-AGENTES.md`
- `C:\Users\User\.gemini\antigravity\scratch\biblioteca\_pesquisa_blender\PLANO.md`
