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

alvo = xyz.mean(0)
extent = float(np.linalg.norm(xyz - alvo, axis=1).mean())   # raio "natural" da nuvem
raio = extent * 2.2 * RAIOF
K = se.intrinsics(W, H, fov_graus=FOV)
Kt = torch.tensor(K, dtype=torch.float32, device=dev)[None]
poses = sp.orbit_poses(n=DUR * FPS, raio=raio, arco_graus=ARCO)

wr = imageio_ffmpeg.write_frames(out_mp4, (W, H), fps=FPS, macro_block_size=None)
wr.send(None)
try:
    for eye in poses:
        vm = torch.tensor(se.look_at(np.asarray(eye) + alvo, alvo), dtype=torch.float32, device=dev)[None]
        img, _, _ = rasterization(means, quats, scales, opac, colors, vm, Kt, W, H)
        fr = (img[0].clamp(0, 1).cpu().numpy() * 255).astype(np.uint8)
        wr.send(np.ascontiguousarray(fr))
finally:
    wr.close()
print("RENDER_OK", out_mp4)
