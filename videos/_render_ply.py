"""Renderiza uma órbita a partir de um PLY 3DGS (ex.: saída do Flash3D) usando o gsplat.
Uso: python _render_ply.py <in.ply> <out.mp4> [raio_factor] [arco_graus] [fov]"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import torch
from plyfile import PlyData
from gsplat import rasterization
import imageio_ffmpeg
import splatting_engine as se
import splatting as sp

ply_path, out_mp4 = sys.argv[1], sys.argv[2]
RAIOF = float(sys.argv[3]) if len(sys.argv) > 3 else 1.0
ARCO = float(sys.argv[4]) if len(sys.argv) > 4 else 30.0
FOV = float(sys.argv[5]) if len(sys.argv) > 5 else 55.0
W, H, FPS, DUR = 512, 512, 24, 5

v = PlyData.read(ply_path)['vertex']
xyz = np.stack([v['x'], v['y'], v['z']], 1).astype(np.float32)
scales = np.exp(np.stack([v['scale_0'], v['scale_1'], v['scale_2']], 1)).astype(np.float32)
quats = np.stack([v['rot_0'], v['rot_1'], v['rot_2'], v['rot_3']], 1).astype(np.float32)
quats /= (np.linalg.norm(quats, axis=1, keepdims=True) + 1e-9)
opac = (1.0 / (1.0 + np.exp(-v['opacity']))).astype(np.float32)
C0 = 0.28209479177387814
rgb = np.clip(0.5 + C0 * np.stack([v['f_dc_0'], v['f_dc_1'], v['f_dc_2']], 1), 0, 1).astype(np.float32)
print(f"gaussians: {xyz.shape[0]}  z[min/med/max]={xyz[:,2].min():.2f}/{np.median(xyz[:,2]):.2f}/{xyz[:,2].max():.2f}")

dev = 'cuda'
means = torch.tensor(xyz, device=dev)
quats = torch.tensor(quats, device=dev)
scales = torch.tensor(scales, device=dev)
opac = torch.tensor(opac, device=dev)
colors = torch.tensor(rgb, device=dev)

# Enquadra a MASSA PRINCIPAL (conteúdo perto; ignora cauda de fundo distante) e
# posiciona a câmera À FRENTE, a uma distância que cabe a bounding box. Órbita = pequeno
# wobble lateral mantendo a câmera de frente (Flash3D só reconstrói o lado visível).
mask = (xyz[:, 2] > 0.05) & (xyz[:, 2] < np.percentile(xyz[:, 2], 90))
core = xyz[mask] if int(mask.sum()) > 100 else xyz
center = core.mean(0).astype(np.float32)
size = float(np.linalg.norm(core - center, axis=1).max()) + 1e-6
cam_dist = size / np.tan(np.radians(FOV) / 2.0) * 1.15
r = RAIOF * 0.15 * cam_dist
print(f"center={center} size={size:.3f} cam_dist={cam_dist:.3f} r={r:.3f}")
K = se.intrinsics(W, H, fov_graus=FOV)
Kt = torch.tensor(K, dtype=torch.float32, device=dev)[None]

N = DUR * FPS
wr = imageio_ffmpeg.write_frames(out_mp4, (W, H), fps=FPS, macro_block_size=None)
wr.send(None)
try:
    for i in range(N):
        phi = 2.0 * np.pi * i / N
        eye = center + np.array([r * np.cos(phi), r * np.sin(phi) * 0.4, -cam_dist], dtype=np.float32)
        vm = torch.tensor(se.look_at(eye, center), dtype=torch.float32, device=dev)[None]
        img, _, _ = rasterization(means, quats, scales, opac, colors, vm, Kt, W, H)
        fr = (img[0].clamp(0, 1).cpu().numpy() * 255).astype(np.uint8)
        wr.send(np.ascontiguousarray(fr))
finally:
    wr.close()
print("RENDER_OK", out_mp4)
