# -*- coding: utf-8 -*-
"""Motor 3D Gaussian Splatting — imagem única → cena 3D → render de órbita.

Pipeline (feed-forward, SEM treino, fit p/ nossas imagens de IA):
  1. estima PROFUNDIDADE monocular da imagem (DepthAnything);
  2. desprojeta cada pixel para um PONTO 3D (câmera pinhole) → nuvem colorida;
  3. cada ponto vira um GAUSSIAN (cor do pixel, escala ~ footprint, opacidade 1);
  4. renderiza as `orbit_poses` com o rasterizador do gsplat (GPU) → frames → mp4.

GEOMETRIA (intrinsics/unproject/look_at/init_gaussians) é PURA e testada (CPU).
O render real exige gsplat compilado (CUDA) + modelo de profundidade — provado pelo
smoke (`splatting_smoke.py`) quando a toolchain de GPU estiver de pé. Aqui nada de GPU
é importado no topo: torch/gsplat/modelo só entram dentro das funções de render.
"""
import subprocess
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).parent


# --------------------------------------------------------------------------
# GEOMETRIA — pura (numpy), testável sem GPU
# --------------------------------------------------------------------------

def intrinsics(w, h, fov_graus=55.0):
    """Matriz K (3x3) de uma câmera pinhole centrada, FOV horizontal `fov_graus`."""
    fx = fy = 0.5 * w / np.tan(np.deg2rad(fov_graus) / 2.0)
    return np.array([[fx, 0, w / 2.0],
                     [0, fy, h / 2.0],
                     [0,  0, 1.0]], dtype=np.float64)


def unproject(depth, K):
    """Desprojeta um mapa de profundidade (h,w) em pontos 3D (N,3) na convenção
    OpenCV (x→direita, y→baixo, z→frente). N = h*w (ordem row-major)."""
    h, w = depth.shape
    fx, fy, cx, cy = K[0, 0], K[1, 1], K[0, 2], K[1, 2]
    us, vs = np.meshgrid(np.arange(w), np.arange(h))
    d = depth.astype(np.float64)
    x = (us - cx) * d / fx
    y = (vs - cy) * d / fy
    z = d
    return np.stack([x.ravel(), y.ravel(), z.ravel()], axis=1)


def look_at(eye, alvo, up=(0.0, -1.0, 0.0)):
    """Matriz view (world→camera, 4x4) OpenCV: +Z aponta para o alvo. `up` default
    y-para-baixo (convenção de imagem). Mapeia `eye` para a origem da câmera."""
    eye = np.asarray(eye, dtype=np.float64)
    alvo = np.asarray(alvo, dtype=np.float64)
    up = np.asarray(up, dtype=np.float64)
    f = alvo - eye
    f = f / (np.linalg.norm(f) + 1e-12)            # +Z (frente, p/ o alvo)
    r = np.cross(f, up)
    r = r / (np.linalg.norm(r) + 1e-12)            # +X (direita)
    u = np.cross(f, r)                              # +Y (baixo, fecha a tríade dextrógira)
    R = np.stack([r, u, f], axis=0)                # linhas = eixos da câmera (world→cam)
    t = -R @ eye
    vm = np.eye(4)
    vm[:3, :3] = R
    vm[:3, 3] = t
    return vm


def init_gaussians(rgb, depth, K, stride=2):
    """Constrói os Gaussians a partir de imagem (h,w,3 em [0,1]) + profundidade (h,w).
    `stride` subamostra a grade (1 = um Gaussian por pixel). PURO (numpy)."""
    h, w = depth.shape
    rgb = rgb[::stride, ::stride]
    depth_s = depth[::stride, ::stride]
    K2 = K.copy()
    K2[0, 0] /= stride; K2[1, 1] /= stride; K2[0, 2] /= stride; K2[1, 2] /= stride
    means = unproject(depth_s, K2)
    colors = rgb.reshape(-1, 3).astype(np.float64)
    n = means.shape[0]
    # escala ~ footprint de um pixel na profundidade (z / fx); isotrópica
    fx = K2[0, 0]
    s = np.clip(means[:, 2] / fx, 1e-3, None)
    scales = np.repeat(s[:, None], 3, axis=1)
    opacities = np.ones(n, dtype=np.float64)
    quats = np.tile(np.array([1.0, 0.0, 0.0, 0.0]), (n, 1))   # identidade
    return {'means': means, 'colors': colors, 'scales': scales,
            'opacities': opacities, 'quats': quats}


# --------------------------------------------------------------------------
# RENDER — GPU (gsplat + modelo de profundidade). Provado pelo smoke, não por unit.
# --------------------------------------------------------------------------

def estimar_profundidade(rgb):
    """Profundidade monocular (h,w) em [perto..longe]. Usa DepthAnything via transformers.
    Só roda na GPU/CPU com o modelo disponível — fora do escopo de teste unitário."""
    import torch
    from transformers import pipeline
    dev = 0 if torch.cuda.is_available() else -1
    pipe = pipeline('depth-estimation', model='depth-anything/Depth-Anything-V2-Small-hf', device=dev)
    from PIL import Image
    out = pipe(Image.fromarray((rgb * 255).astype(np.uint8)))
    d = np.asarray(out['depth'], dtype=np.float32)
    d = d / (d.max() + 1e-6)                  # normaliza
    return 0.5 + 2.0 * (1.0 - d)             # invertido: claro=perto → z menor


def render(src_png, out_mp4, poses, fps=24):
    """Render real 3DGS (GPU): imagem→profundidade→Gaussians→rasteriza órbita→mp4.
    Requer gsplat compilado (CUDA). Levanta se a toolchain faltar — o caller
    (`splatting.splat_clip`) captura e faz fallback. Provado por `splatting_smoke.py`."""
    import torch
    from gsplat import rasterization
    import imageio_ffmpeg
    from PIL import Image

    rgb = np.asarray(Image.open(src_png).convert('RGB'), dtype=np.float32) / 255.0
    h, w = rgb.shape[:2]
    depth = estimar_profundidade(rgb)
    K = intrinsics(w, h)
    g = init_gaussians(rgb, depth, K, stride=2)

    dev = 'cuda'
    means = torch.tensor(g['means'], dtype=torch.float32, device=dev)
    quats = torch.tensor(g['quats'], dtype=torch.float32, device=dev)
    scales = torch.tensor(g['scales'], dtype=torch.float32, device=dev)
    opac = torch.tensor(g['opacities'], dtype=torch.float32, device=dev)
    colors = torch.tensor(g['colors'], dtype=torch.float32, device=dev)
    Kt = torch.tensor(K, dtype=torch.float32, device=dev)[None]

    alvo = means.mean(dim=0).cpu().numpy()
    writer = imageio_ffmpeg.write_frames(str(out_mp4), (w, h), fps=fps, macro_block_size=None)
    writer.send(None)
    try:
        for eye in poses:
            vm = torch.tensor(look_at(np.asarray(eye) + alvo, alvo), dtype=torch.float32, device=dev)[None]
            img, _, _ = rasterization(means, quats, scales, opac, colors, vm, Kt, w, h)
            frame = (img[0].clamp(0, 1).cpu().numpy() * 255).astype(np.uint8)
            writer.send(np.ascontiguousarray(frame))
    finally:
        writer.close()
    return Path(out_mp4).exists()


if __name__ == '__main__':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    K = intrinsics(1920, 1080)
    print('intrinsics 1920x1080 ->', K[0, 0].round(1), 'fx | cx', K[0, 2])
    print('módulo de geometria OK (render real precisa de gsplat compilado + GPU).')
