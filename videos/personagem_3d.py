# -*- coding: utf-8 -*-
"""Personagem 3D PROCEDURAL (Blender/bpy headless) — "o velho louco de cabelo branco".

Escultura estilizada via primitivas + Skin modifier (corpo magro posado) + cabelo de
partículas (selvagem) + cara cartoon (olhos esbugalhados, boca maníaca) + roupa esfarrapada.
Renderiza no NOSSO estúdio (Cycles/OptiX, AgX, HDRI). NÃO é cópia fiel do desenho — é uma
versão 3D estilizada que captura os traços. Reusa cenario3d (gpu/mundo_hdri/luz/_set).

Uso:  blender --background --python personagem_3d.py -- --hdri STUDIO.exr --out PREFIXO
      [--mode stills|turn] [--samples 96] [--res 1080x1350] [--frames 120]
  stills -> PREFIXO_a.png/_b.png/_c.png (3 ângulos, prova de 3D)
  turn   -> PREFIXO.mp4 (turntable 360)
"""
import bpy, sys, os, math, random
from mathutils import Vector
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cenario3d as c3   # gpu, mundo_hdri, luz, _set, limpar

argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
def arg(f, d=None): return argv[argv.index(f) + 1] if f in argv else d
HDRI = arg("--hdri"); OUT = arg("--out", "personagem")
MODE = arg("--mode", "stills"); SAMPLES = int(arg("--samples", "96"))
RX, RY = (int(x) for x in arg("--res", "1080x1350").split("x"))
N = int(arg("--frames", "120"))


# ---------------------------------------------------------------- materiais
def mat(nome, cor, rough=0.6, subsurf=0.0, metal=0.0):
    m = bpy.data.materials.new(nome); m.use_nodes = True
    b = m.node_tree.nodes.get('Principled BSDF')
    b.inputs['Base Color'].default_value = (*cor, 1)
    c3._set(b, "Roughness", rough); c3._set(b, "Metallic", metal)
    if subsurf:
        c3._set(b, "Subsurface Weight", subsurf)
        c3._set(b, "Subsurface Radius", (0.10, 0.04, 0.02))
    return m


SKIN  = lambda: mat("Skin",  (0.46, 0.54, 0.37), 0.55, subsurf=0.18)   # pele pálida doentia (esverdeada)
HAIR  = lambda: mat("Hair",  (0.86, 0.87, 0.90), 0.85)                  # branco-grisalho
SHIRT = lambda: mat("Shirt", (0.30, 0.24, 0.16), 0.95)                  # camisa suja (marrom-terra escuro, contrasta c/ pele)
PANTS = lambda: mat("Pants", (0.26, 0.29, 0.37), 0.95)                  # calça cinza-azulada suja
EYE   = lambda: mat("Eye",   (0.92, 0.92, 0.93), 0.25)                  # esclera
IRIS  = lambda: mat("Iris",  (0.02, 0.02, 0.03), 0.30)                  # pupila escura
MOUTH = lambda: mat("Mouth", (0.10, 0.02, 0.02), 0.50)                  # boca escura
TEETH = lambda: mat("Teeth", (0.82, 0.80, 0.72), 0.40)                  # dentes


# ---------------------------------------------------------------- helpers de forma
def esfera(nome, loc, r, material, escala=(1, 1, 1), segs=24, rings=14):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=segs, ring_count=rings, radius=r, location=loc)
    o = bpy.context.active_object; o.name = nome; o.scale = escala
    for p in o.data.polygons: p.use_smooth = True
    o.data.materials.append(material)
    return o


def caixa(nome, loc, escala, material, rot=(0, 0, 0)):
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=loc)
    o = bpy.context.active_object; o.name = nome; o.scale = escala; o.rotation_euler = rot
    o.data.materials.append(material)
    return o


def figura_skin(nome, verts, edges, radii, root, material, subsurf=2, base_r=0.04):
    """Cria uma malha de 'esqueleto' (verts/edges) e a engorda com o Skin modifier +
    Subsurf -> volume orgânico liso seguindo a pose. radii = {idx: raio} (resto = base_r)."""
    me = bpy.data.meshes.new(nome); me.from_pydata(verts, edges, []); me.update()
    o = bpy.data.objects.new(nome, me); bpy.context.scene.collection.objects.link(o)
    sk = o.modifiers.new("skin", 'SKIN'); sk.use_smooth_shade = True
    sv = me.skin_vertices[0].data
    for i in range(len(verts)):
        r = radii.get(i, base_r); sv[i].radius = (r, r)
    sv[root].use_root = True
    o.modifiers.new("subsurf", 'SUBSURF').levels = subsurf
    o.data.materials.append(material)
    return o


def look_at(cam, alvo):
    d = Vector(alvo) - cam.location
    cam.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler()


# ---------------------------------------------------------------- esqueletos (pose dinâmica)
# eixos: x=esq/dir, y=frente(-)/trás(+), z=cima.  Frente do personagem = -Y. Pose: agachado,
# inclinado p/ frente, um braço erguido (maníaco), passada dinâmica.
def construir_corpo():
    # corpo + membros (UMA malha conectada -> um blob do Skin)
    V = [
        (0.00, 0.02, 0.74),   # 0 pelve (root)
        (0.00,-0.05, 0.95),   # 1 abdômen
        (0.00,-0.10, 1.14),   # 2 peito
        (0.00,-0.11, 1.26),   # 3 pescoço
        # braço esq (erguido/p/ frente — maníaco)
        (0.15,-0.10, 1.16),   # 4 ombro E
        (0.34,-0.22, 1.18),   # 5 cotovelo E
        (0.50,-0.34, 1.30),   # 6 mão E (no alto)
        # braço dir (esticado p/ baixo/fora)
        (-0.15,-0.10,1.16),   # 7 ombro D
        (-0.33,-0.04,0.98),   # 8 cotovelo D
        (-0.46,-0.16,0.82),   # 9 mão D
        # perna esq (frente, joelho dobrado — passada)
        (0.10, 0.02, 0.70),   # 10 quadril E
        (0.15,-0.18, 0.40),   # 11 joelho E
        (0.17,-0.30, 0.06),   # 12 torn. E
        # perna dir (atrás, apoio)
        (-0.10,0.02, 0.70),   # 13 quadril D
        (-0.16,0.12, 0.42),   # 14 joelho D
        (-0.18,0.20, 0.06),   # 15 torn. D
    ]
    V[12] = (0.17, -0.30, 0.045); V[15] = (-0.18, 0.20, 0.045)   # tornozelos no chão
    E = [(0,1),(1,2),(2,3),(2,4),(4,5),(5,6),(2,7),(7,8),(8,9),
         (0,10),(10,11),(11,12),(0,13),(13,14),(14,15)]
    R = {0:0.085, 1:0.078, 2:0.085, 3:0.045,
         4:0.045,5:0.034,6:0.030, 7:0.045,8:0.034,9:0.030,
         10:0.055,11:0.040,12:0.030, 13:0.055,14:0.040,15:0.030}
    corpo = figura_skin("Corpo", V, E, R, root=0, material=SKIN(), subsurf=2, base_r=0.04)
    pele = corpo.data.materials[0]
    esfera("MaoE", (0.50, -0.34, 1.30), 0.055, pele, escala=(0.9, 0.9, 1.0))    # mãos
    esfera("MaoD", (-0.46, -0.16, 0.82), 0.055, pele, escala=(0.9, 0.9, 1.0))
    esfera("PeE", (0.17, -0.37, 0.035), 0.055, pele, escala=(0.7, 1.5, 0.5))    # pés descalços no chão
    esfera("PeD", (-0.18, 0.12, 0.035), 0.055, pele, escala=(0.7, 1.5, 0.5))
    return corpo


def construir_camisa():
    """Camisa = TUBO de tecido aberto (gola em cima, bainha RASGADA embaixo) + Solidify
    (espessura de pano). Lê claramente como roupa (não 'barriga') — cues de gola + bainha torta."""
    random.seed(7)
    Nr = 18
    topo_z, base_z = 0.21, -0.21
    topo_r, base_r = 0.125, 0.175
    V = []
    for i in range(Nr):                                    # gola (mostra o pescoço pelo buraco)
        a = 2 * math.pi * i / Nr
        V.append((topo_r * math.cos(a), topo_r * 0.85 * math.sin(a), topo_z))
    for i in range(Nr):                                    # bainha esfarrapada (z e raio irregulares)
        a = 2 * math.pi * i / Nr
        r = base_r + random.uniform(-0.012, 0.022)
        V.append((r * math.cos(a), r * 0.9 * math.sin(a), base_z + random.uniform(-0.06, 0.02)))
    F = [(i, (i + 1) % Nr, Nr + (i + 1) % Nr, Nr + i) for i in range(Nr)]
    me = bpy.data.meshes.new("Camisa"); me.from_pydata(V, [], F); me.update()
    for p in me.polygons: p.use_smooth = True
    o = bpy.data.objects.new("Camisa", me); bpy.context.scene.collection.objects.link(o)
    o.location = (0.0, -0.04, 0.97); o.rotation_euler = (math.radians(16), 0, 0)   # acompanha a inclinação do torso
    o.data.materials.append(SHIRT())
    o.modifiers.new("sol", 'SOLIDIFY').thickness = 0.02    # parede de pano
    o.modifiers.new("sub", 'SUBSURF').levels = 1
    _esfarrapar(o, 0.02)
    return o


def construir_roupa():
    # CAMISA esfarrapada: chain pelve->peito + mangas curtas (cobre torso e parte do braço),
    # raio maior que o corpo -> "veste". Material sujo. (pernas/antebraços ficam à mostra = rasgado)
    camisa = construir_camisa()
    # CALÇA rasgada: quadris -> joelhos só (joelho->tornozelo fica perna nua = pernas rasgadas)
    Vp = [(0.00,0.02,0.78),(0.10,0.02,0.70),(0.15,-0.16,0.44),    # 0 cintura,1 quadril E,2 joelho E
          (-0.10,0.02,0.70),(-0.16,0.10,0.46)]                    # 3 quadril D,4 joelho D
    Ep = [(0,1),(1,2),(0,3),(3,4)]
    Rp = {0:0.135,1:0.090,2:0.060,3:0.090,4:0.060}
    calca = figura_skin("Calca", Vp, Ep, Rp, root=0, material=PANTS(), subsurf=2, base_r=0.06)
    _esfarrapar(calca, 0.035)
    return camisa, calca


def _esfarrapar(o, forca):
    """Displace com ruído -> tecido amassado/sujo/irregular (silhueta esfarrapada)."""
    tex = bpy.data.textures.new(o.name + "_n", 'CLOUDS'); tex.noise_scale = 0.18
    d = o.modifiers.new("rasgo", 'DISPLACE'); d.texture = tex; d.strength = forca; d.mid_level = 0.4


def construir_cabeca():
    cx, cy, cz = 0.0, -0.13, 1.45    # centro da cabeça (grande, cartoon)
    cab = esfera("Cabeca", (cx, cy, cz), 0.18, SKIN(), escala=(0.95, 1.05, 1.08), segs=32, rings=20)
    # queixo/mandíbula
    esfera("Queixo", (cx, cy - 0.10, cz - 0.13), 0.10, cab.data.materials[0], escala=(1.0, 0.9, 0.7))
    # nariz batata
    esfera("Nariz", (cx, cy - 0.20, cz - 0.02), 0.045, cab.data.materials[0], escala=(1.0, 1.4, 1.0))
    # OLHOS grandes esbugalhados (esclera projetada p/ -Y) + íris
    eye_m, iris_m = EYE(), IRIS()
    for sx in (0.078, -0.078):
        esfera("Olho", (cx + sx, cy - 0.150, cz + 0.055), 0.072, eye_m, segs=20, rings=12)   # esbugalhados
        esfera("Iris", (cx + sx, cy - 0.205, cz + 0.050), 0.028, iris_m, segs=16, rings=10)
        # sobrancelha branca rebelde
        caixa("Sob", (cx + sx, cy - 0.175, cz + 0.135), (0.075, 0.012, 0.018), HAIR(),
              rot=(0, 0, math.radians(18 if sx > 0 else -18)))
    # BOCA maníaca aberta + dentes
    esfera("Boca", (cx, cy - 0.165, cz - 0.085), 0.06, MOUTH(), escala=(1.5, 0.7, 0.9))
    teeth_m = TEETH()
    for tx in (-0.045, -0.015, 0.015, 0.045):
        caixa("Dente", (cx + tx, cy - 0.205, cz - 0.055), (0.012, 0.008, 0.018), teeth_m)
    return cab


def cabelo_selvagem(cabeca):
    """Cabelo de partículas branco, explodindo do topo/trás da cabeça (selvagem)."""
    cabeca.data.materials.append(HAIR())   # slot 1 = cabelo
    vg = cabeca.vertex_groups.new(name="couro")
    for v in cabeca.data.vertices:        # SÓ topo + nuca alta -> cabelo p/ cima (não disco lateral)
        peso = 1.0 if (v.co.z > 0.075 or (v.co.y > 0.06 and v.co.z > -0.02)) else 0.0
        vg.add([v.index], peso, 'REPLACE')
    cabeca.modifiers.new("cabelo", 'PARTICLE_SYSTEM')
    ps = cabeca.particle_systems[-1]; ps.vertex_group_density = "couro"
    p = ps.settings
    p.type = 'HAIR'; p.count = 420; p.hair_length = 0.13     # mais curto e denso = mop selvagem
    p.use_advanced_hair = True; p.use_hair_bspline = True
    p.root_radius = 0.006; p.tip_radius = 0.0
    p.normal_factor = 0.11; p.factor_random = 0.38           # menos radial, ainda caótico
    p.brownian_factor = 0.18
    p.kink = 'CURL'; p.kink_amplitude = 0.035; p.kink_frequency = 2.5
    p.child_type = 'INTERPOLATED'; p.rendered_child_count = 70; p.child_length = 1.0
    p.material = 2                                          # slot 2 (1-based) = HAIR
    return ps


# ---------------------------------------------------------------- estúdio + render
def estudio():
    c3.mundo_hdri(HDRI, 0.55)                               # HDRI ilumina/reflete, câmera vê fundo escuro
    c3.luz("Key", 230, (1.4, -1.8, 2.4), 1.4)
    c3.luz("Fill", 95, (-1.8, -1.2, 1.6), 1.8)
    c3.luz("Rim", 240, (0.0, 1.8, 2.0), 1.0)
    # chão p/ ancorar a sombra de contato
    bpy.ops.mesh.primitive_plane_add(size=14, location=(0, 0, 0))
    ch = bpy.context.active_object
    ch.data.materials.append(mat("Chao", (0.05, 0.05, 0.06), 0.6))


def setup_render(co):
    s = bpy.context.scene; s.camera = co
    c3.gpu()
    s.render.resolution_x = RX; s.render.resolution_y = RY; s.render.fps = 24
    s.view_settings.view_transform = 'AgX'
    try: s.view_settings.look = 'AgX - Medium High Contrast'
    except Exception: pass


def nova_cam():
    cd = bpy.data.cameras.new("Cam"); cd.lens = 55; cd.sensor_width = 36
    co = bpy.data.objects.new("Cam", cd); bpy.context.scene.collection.objects.link(co)
    return co


def main():
    c3.limpar()
    corpo = construir_corpo()
    construir_roupa()
    cab = construir_cabeca()
    cabelo_selvagem(cab)
    estudio()
    co = nova_cam(); setup_render(co)
    alvo = (0.0, 0.0, 0.85)
    s = bpy.context.scene
    s.cycles.samples = SAMPLES
    print("[pers] corpo dim", tuple(round(x, 2) for x in corpo.dimensions),
          "cabeca dim", tuple(round(x, 2) for x in cab.dimensions))

    if MODE == "turn":
        raio, alt = 3.4, 1.05
        s.frame_start = 1; s.frame_end = N
        for fr in (1, N):
            ang = math.radians(360 * (fr - 1) / N)
            co.location = (raio * math.sin(ang), -raio * math.cos(ang), alt)
            look_at(co, alvo); co.keyframe_insert("location", frame=fr); co.keyframe_insert("rotation_euler", frame=fr)
        # interpola posição/rotação a cada frame (órbita real)
        for fr in range(1, N + 1):
            ang = math.radians(360 * (fr - 1) / N)
            co.location = (raio * math.sin(ang), -raio * math.cos(ang), alt)
            look_at(co, alvo); co.keyframe_insert("location", frame=fr); co.keyframe_insert("rotation_euler", frame=fr)
        r = s.render; r.filepath = OUT + ".mp4"
        r.image_settings.file_format = 'FFMPEG'; r.ffmpeg.format = 'MPEG4'; r.ffmpeg.codec = 'H264'
        r.ffmpeg.constant_rate_factor = 'HIGH'; r.ffmpeg.audio_codec = 'NONE'
        print(f"[pers] turntable {N}f -> {r.filepath}")
        bpy.ops.render.render(animation=True)
        print("PERS_OK", r.filepath)
    else:
        raio, alt = 3.5, 0.95
        s.render.image_settings.file_format = 'PNG'
        angulos = [("a", 25), ("b", 90), ("c", 200)]       # 3/4 frente, perfil, 3/4 trás (prova 3D)
        for suf, deg in angulos:
            ang = math.radians(deg)
            co.location = (raio * math.sin(ang), -raio * math.cos(ang), alt)
            look_at(co, alvo)
            s.render.filepath = f"{OUT}_{suf}.png"
            print(f"[pers] still {suf} ({deg}graus) -> {s.render.filepath}")
            bpy.ops.render.render(write_still=True)
        print("PERS_OK", OUT + "_a/_b/_c.png")


main()
