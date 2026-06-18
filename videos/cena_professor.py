# -*- coding: utf-8 -*-
"""Cena temática (B): PROFESSOR (billboard recortado) apresentando um LIVRO 3D, num
ambiente de comunidade (HDRI interior CC0). Headless Blender/Cycles, GPU OptiX.

Uso: blender --background --python cena_professor.py -- --prof PROF.png --capa CAPA.png
     --hdri ROOM.exr --out OUT.mp4 [--frames 336 --samples 80 --res 1080x1350]
Vídeo MUDO; o áudio (narração + sonoplastia) é muxado depois pelo pipeline.
"""
import bpy, sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cenario3d as c3   # reusa criar_livro, luz, _set

argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
def arg(f, d=None): return argv[argv.index(f) + 1] if f in argv else d
PROF = arg("--prof"); CAPA = arg("--capa"); HDRI = arg("--hdri"); OUT = arg("--out", "out.mp4")
N = int(arg("--frames", "336")); SAMPLES = int(arg("--samples", "80"))
RX, RY = (int(x) for x in arg("--res", "1080x1350").split("x"))


def limpar():
    bpy.ops.object.select_all(action='SELECT'); bpy.ops.object.delete(use_global=False)
    for b in (bpy.data.meshes, bpy.data.materials, bpy.data.lights, bpy.data.cameras, bpy.data.images):
        for it in list(b):
            try: b.remove(it)
            except Exception: pass


def mundo_room(hdri_path, força=0.7):
    """HDRI interior VISÍVEL (cenário) — ilumina e aparece (desfocado) ao fundo."""
    w = bpy.data.worlds.new("World"); bpy.context.scene.world = w; w.use_nodes = True
    nt = w.node_tree; nt.nodes.clear()
    out = nt.nodes.new('ShaderNodeOutputWorld'); bg = nt.nodes.new('ShaderNodeBackground')
    env = nt.nodes.new('ShaderNodeTexEnvironment'); mp = nt.nodes.new('ShaderNodeMapping'); tc = nt.nodes.new('ShaderNodeTexCoord')
    img = bpy.data.images.load(hdri_path); img.colorspace_settings.name = 'Linear Rec.709'; env.image = img
    bg.inputs['Strength'].default_value = força
    mp.inputs['Rotation'].default_value = (0, 0, math.radians(40))   # gira o quarto p/ um ângulo bom
    nt.links.new(tc.outputs['Generated'], mp.inputs['Vector'])
    nt.links.new(mp.outputs['Vector'], env.inputs['Vector'])
    nt.links.new(env.outputs['Color'], bg.inputs['Color'])
    nt.links.new(bg.outputs['Background'], out.inputs['Surface'])


def chao():
    bpy.ops.mesh.primitive_plane_add(size=20, location=(0, 0, 0))
    o = bpy.context.active_object
    m = bpy.data.materials.new("Chao"); m.use_nodes = True
    b = m.node_tree.nodes.get('Principled BSDF')
    c3._set(b, "Base Color", (0.04, 0.04, 0.05, 1)); c3._set(b, "Roughness", 0.35)   # piso escuro semi-reflexivo
    o.data.materials.append(m)
    return o


def billboard_prof(png, altura=1.72, x=-0.6):
    """Plano recortado (from_pydata, confiável no headless) com o professor — em pé no chão,
    aspecto correto, encarando -Y (a câmera). Alpha do recorte vem do nó Image."""
    img = bpy.data.images.load(png)
    w, h = img.size; hw = altura * (w / h) / 2
    verts = [(x - hw, 0, 0), (x + hw, 0, 0), (x + hw, 0, altura), (x - hw, 0, altura)]
    me = bpy.data.meshes.new("Prof"); me.from_pydata(verts, [], [(0, 1, 2, 3)]); me.update()
    uvl = me.uv_layers.new(name="UVMap")
    for i, uv in enumerate([(0, 0), (1, 0), (1, 1), (0, 1)]):
        uvl.data[i].uv = uv
    o = bpy.data.objects.new("Prof", me); bpy.context.scene.collection.objects.link(o)
    m = bpy.data.materials.new("ProfMat"); m.use_nodes = True
    nt = m.node_tree; nt.nodes.clear()
    out = nt.nodes.new('ShaderNodeOutputMaterial'); bsdf = nt.nodes.new('ShaderNodeBsdfPrincipled')
    tex = nt.nodes.new('ShaderNodeTexImage'); tex.image = img; uvn = nt.nodes.new('ShaderNodeUVMap'); uvn.uv_map = "UVMap"
    c3._set(bsdf, "Roughness", 0.6)
    nt.links.new(uvn.outputs['UV'], tex.inputs['Vector'])
    nt.links.new(tex.outputs['Color'], bsdf.inputs['Base Color'])
    nt.links.new(tex.outputs['Alpha'], bsdf.inputs['Alpha'])
    nt.links.new(bsdf.outputs['BSDF'], out.inputs['Surface'])
    o.data.materials.append(m)
    return o


def main():
    limpar()
    sc = bpy.context.scene
    mundo_room(HDRI, 0.75)
    chao()
    prof = billboard_prof(PROF, altura=1.65, x=-0.62)
    # livro 3D ampliado (presença de "apresentação"), à direita, levemente girado
    livro = c3.criar_livro(CAPA, larg=0.40, esp=0.07, alt=0.58)
    livro.location = (0.62, 0.05, 0.62); livro.rotation_euler = (0, 0, math.radians(-22))
    # luz quente de "estúdio/estúdio de gravação"
    c3.luz("Key", 600, (1.2, -1.6, 2.2), 1.2); c3.luz("Fill", 180, (-1.5, -1.0, 1.4), 1.6)
    # câmera: enquadra os dois, leve dolly-in
    cd = bpy.data.cameras.new("Cam"); cd.lens = 40; cd.sensor_width = 36
    cd.dof.use_dof = True; cd.dof.aperture_fstop = 3.5
    co = bpy.data.objects.new("Cam", cd); sc.collection.objects.link(co); sc.camera = co
    alvo = bpy.data.objects.new("Alvo", None); alvo.location = (0, 0, 0.9); sc.collection.objects.link(alvo)
    cd.dof.focus_object = alvo
    co.rotation_euler = (math.radians(87), 0, 0)           # olha +Y (leve down) — explícito, sem TRACK_TO
    sc.frame_start = 1; sc.frame_end = N
    for fr, y in [(1, -3.35), (N, -2.75)]:                 # dolly-in suave
        co.location = (0.0, y, 1.05); co.keyframe_insert("location", frame=fr)
    # GPU OptiX
    sc.render.engine = 'CYCLES'; sc.cycles.device = 'GPU'
    pr = bpy.context.preferences.addons['cycles'].preferences
    pr.compute_device_type = 'OPTIX'; pr.get_devices()
    for d in pr.devices: d.use = (d.type == 'OPTIX')
    sc.cycles.samples = SAMPLES; sc.cycles.use_adaptive_sampling = True; sc.cycles.adaptive_threshold = 0.01
    sc.cycles.use_denoising = True; sc.cycles.denoiser = 'OPTIX'
    sc.render.resolution_x = RX; sc.render.resolution_y = RY; sc.render.fps = 24
    sc.view_settings.view_transform = 'AgX'
    try: sc.view_settings.look = 'AgX - Medium High Contrast'
    except Exception: pass
    r = sc.render; r.filepath = OUT
    r.image_settings.file_format = 'FFMPEG'; r.ffmpeg.format = 'MPEG4'; r.ffmpeg.codec = 'H264'
    r.ffmpeg.constant_rate_factor = 'HIGH'; r.ffmpeg.audio_codec = 'NONE'
    print("[dbg] prof loc", tuple(round(x,2) for x in prof.location), "dim", tuple(round(x,2) for x in prof.dimensions))
    print("[dbg] livro loc", tuple(round(x,2) for x in livro.location), "dim", tuple(round(x,2) for x in livro.dimensions))
    print("[dbg] cam loc", tuple(round(x,2) for x in co.location), "alvo", tuple(round(x,2) for x in alvo.location))
    print(f"[cena] render {N}f {RX}x{RY} -> {OUT}")
    bpy.ops.render.render(animation=True)
    print("CENA_OK", OUT)


main()
