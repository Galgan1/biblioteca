# -*- coding: utf-8 -*-
"""Cinegrafista Premium (Blender/bpy) — capa de livro -> LIVRO 3D real girando (turntable).

3D de VERDADE (Cycles): órbita 360 sem buraco, fotorrealista, comercial (renders são
nossos; HDRI Poly Haven = CC0). Headless, GPU OptiX na RTX 5060.

Uso:  blender --background --python cenario3d.py -- --capa CAPA.jpg --hdri STUDIO.exr --out OUT.mp4
Opcionais: --frames 120 --samples 96 --res 1080x1350
"""
import bpy, sys, math, os

# ---- args após '--' ----
argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
def arg(flag, default=None):
    return argv[argv.index(flag) + 1] if flag in argv else default

CAPA = arg("--capa"); HDRI = arg("--hdri"); OUT = arg("--out", "out.mp4")
N = int(arg("--frames", "120")); SAMPLES = int(arg("--samples", "96"))
RES = arg("--res", "1080x1350"); RX, RY = (int(x) for x in RES.split("x"))


def limpar():
    bpy.ops.object.select_all(action='SELECT'); bpy.ops.object.delete(use_global=False)
    for b in (bpy.data.meshes, bpy.data.materials, bpy.data.lights, bpy.data.cameras, bpy.data.images):
        for it in list(b):
            try: b.remove(it)
            except Exception: pass


def _set(bsdf, nome, val):
    for k in (nome, nome.replace(" IOR Level", "")):
        if k in bsdf.inputs:
            bsdf.inputs[k].default_value = val; return


def mat_capa(capa_path):
    m = bpy.data.materials.new("Capa"); m.use_nodes = True
    nt = m.node_tree; nt.nodes.clear()
    out = nt.nodes.new('ShaderNodeOutputMaterial'); bsdf = nt.nodes.new('ShaderNodeBsdfPrincipled')
    tex = nt.nodes.new('ShaderNodeTexImage'); uv = nt.nodes.new('ShaderNodeUVMap')
    img = bpy.data.images.load(capa_path); tex.image = img; uv.uv_map = "UVMap"
    _set(bsdf, "Roughness", 0.45); _set(bsdf, "Specular IOR Level", 0.4); _set(bsdf, "Coat Weight", 0.3)
    nt.links.new(uv.outputs['UV'], tex.inputs['Vector'])
    nt.links.new(tex.outputs['Color'], bsdf.inputs['Base Color'])
    nt.links.new(bsdf.outputs['BSDF'], out.inputs['Surface'])
    return m


def mat_papel():
    m = bpy.data.materials.new("Papel"); m.use_nodes = True
    b = m.node_tree.nodes.get('Principled BSDF') or next((n for n in m.node_tree.nodes if n.type == 'BSDF_PRINCIPLED'), None)
    if b:
        b.inputs['Base Color'].default_value = (0.30, 0.28, 0.25, 1)   # cinza-escuro fosco (verso/lombada/cortes)
        b.inputs['Roughness'].default_value = 0.85
        _set(b, "Specular IOR Level", 0.1)
    print("[dbg] papel BSDF ok:", b is not None)
    return m


def criar_livro(capa_path, larg=0.15, alt=0.22, esp=0.03):
    w, h, t = larg/2, esp/2, alt/2   # w=largura(x)  h=espessura(y)  t=altura(z)
    verts = [(-w,-h,-t),(w,-h,-t),(w,h,-t),(-w,h,-t),(-w,-h,t),(w,-h,t),(w,h,t),(-w,h,t)]
    faces = [(0,1,5,4),(2,3,7,6),(3,0,4,7),(1,2,6,5),(0,3,2,1),(4,5,6,7)]  # frente,trás,esq,dir,baixo,cima
    me = bpy.data.meshes.new("Livro"); me.from_pydata(verts, [], faces); me.update()
    ob = bpy.data.objects.new("Livro", me); bpy.context.scene.collection.objects.link(ob)
    uvl = me.uv_layers.new(name="UVMap")
    capa_uv = [(0,0),(1,0),(1,1),(0,1)]; edge_uv = [(0,0),(0.1,0),(0.1,1),(0,1)]
    per = [capa_uv, [(1,0),(0,0),(0,1),(1,1)], edge_uv, edge_uv, edge_uv, edge_uv]
    i = 0
    for fu in per:
        for u, v in fu:
            uvl.data[i].uv = (u, v); i += 1
    ob.data.materials.append(mat_capa(capa_path))   # idx 0
    ob.data.materials.append(mat_papel())           # idx 1
    for p in me.polygons:
        p.material_index = 0 if p.index == 0 else 1        # só a FRENTE = capa; resto = papel (verso/lombada/cortes)
    # bevel leve nas arestas (real)
    mod = ob.modifiers.new("bevel", 'BEVEL'); mod.width = 0.0025; mod.segments = 3
    for p in me.polygons:
        p.use_smooth = False
    return ob


def mundo_hdri(hdri_path, força=0.6):
    """HDRI ilumina e REFLETE no livro, mas a CÂMERA vê um fundo escuro neutro (look estúdio).
    Truque Light Path 'Is Camera Ray': raio de câmera → fundo escuro; reflexo/iluminação → HDRI."""
    w = bpy.data.worlds.new("World"); bpy.context.scene.world = w; w.use_nodes = True
    nt = w.node_tree; nt.nodes.clear()
    out = nt.nodes.new('ShaderNodeOutputWorld')
    env = nt.nodes.new('ShaderNodeTexEnvironment')
    img = bpy.data.images.load(hdri_path); img.colorspace_settings.name = 'Linear Rec.709'; env.image = img
    bg_env = nt.nodes.new('ShaderNodeBackground'); bg_env.inputs['Strength'].default_value = força
    bg_dark = nt.nodes.new('ShaderNodeBackground')
    bg_dark.inputs['Color'].default_value = (0.012, 0.012, 0.016, 1); bg_dark.inputs['Strength'].default_value = 1.0
    lp = nt.nodes.new('ShaderNodeLightPath'); mix = nt.nodes.new('ShaderNodeMixShader')
    nt.links.new(env.outputs['Color'], bg_env.inputs['Color'])
    nt.links.new(lp.outputs['Is Camera Ray'], mix.inputs['Fac'])
    nt.links.new(bg_env.outputs['Background'], mix.inputs[1])    # fac=0 → HDRI (reflexo/luz)
    nt.links.new(bg_dark.outputs['Background'], mix.inputs[2])   # fac=1 → escuro (câmera)
    nt.links.new(mix.outputs['Shader'], out.inputs['Surface'])


def luz(nome, energia, loc, tam=0.6):
    d = bpy.data.lights.new(nome, 'AREA'); d.energy = energia; d.size = tam
    o = bpy.data.objects.new(nome, d); o.location = loc; bpy.context.scene.collection.objects.link(o)
    c = o.constraints.new('TRACK_TO'); c.track_axis = 'TRACK_NEGATIVE_Z'; c.up_axis = 'UP_Z'
    return o


def camera(alvo):
    cd = bpy.data.cameras.new("Cam"); cd.lens = 50; cd.sensor_width = 36
    cd.dof.use_dof = True; cd.dof.aperture_fstop = 8.0   # blur sutil no fundo, livro nítido
    cd.dof.focus_object = alvo
    co = bpy.data.objects.new("Cam", cd); bpy.context.scene.collection.objects.link(co)
    bpy.context.scene.camera = co
    co.location = (0.0, -0.45, 0.0)
    co.rotation_euler = (math.radians(90), 0, 0)         # olha +Y (a capa), upright
    return co


def turntable(ob, n, amp=50):
    """Sway senoidal ±amp (não 360): a CAPA é a heroína o tempo todo, mostra o 3D/espessura
    e o verso (sem conteúdo) nunca aparece. Loopável (começa e termina em 0)."""
    s = bpy.context.scene; s.frame_start = 1; s.frame_end = n
    a = math.radians(amp)
    for fr, ang in [(1, 0), (n // 4, a), (n // 2, 0), (3 * n // 4, -a), (n, 0)]:
        ob.rotation_euler = (0, 0, ang); ob.keyframe_insert("rotation_euler", frame=fr)
    # interpolação BEZIER (default) = sway suave; sem LINEAR


def gpu():
    s = bpy.context.scene; s.render.engine = 'CYCLES'; s.cycles.device = 'GPU'
    pr = bpy.context.preferences.addons['cycles'].preferences
    pr.compute_device_type = 'OPTIX'; pr.get_devices()          # ordem importa (headless)
    achou = False
    for d in pr.devices:
        d.use = (d.type == 'OPTIX'); achou = achou or d.use
    if not achou:                                               # fallback CUDA
        pr.compute_device_type = 'CUDA'; pr.get_devices()
        for d in pr.devices:
            d.use = (d.type == 'CUDA')
    print("[cenario3d] devices:", [(d.name, d.type, d.use) for d in pr.devices])
    s.cycles.samples = SAMPLES; s.cycles.use_adaptive_sampling = True; s.cycles.adaptive_threshold = 0.01
    s.cycles.use_denoising = True; s.cycles.denoiser = 'OPTIX'


def main():
    limpar()
    livro = criar_livro(CAPA)
    mundo_hdri(HDRI, 0.4)
    luz("Key", 220, (0.6, -0.6, 0.8), 0.7); luz("Fill", 70, (-0.7, -0.3, 0.4), 0.9); luz("Rim", 140, (0, 0.7, 0.7), 0.5)
    camera(livro)
    turntable(livro, N)
    gpu()
    s = bpy.context.scene
    s.render.resolution_x = RX; s.render.resolution_y = RY; s.render.fps = 24
    s.view_settings.view_transform = 'AgX'
    try: s.view_settings.look = 'AgX - Punchy'
    except Exception: pass
    r = s.render; r.filepath = OUT
    r.image_settings.file_format = 'FFMPEG'; r.ffmpeg.format = 'MPEG4'; r.ffmpeg.codec = 'H264'
    r.ffmpeg.constant_rate_factor = 'HIGH'; r.ffmpeg.audio_codec = 'NONE'
    print(f"[cenario3d] render {N}f {RX}x{RY} samples={SAMPLES} -> {OUT}")
    bpy.ops.render.render(animation=True)
    print("CENARIO_OK", OUT)


main()
