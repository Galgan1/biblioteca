# -*- coding: utf-8 -*-
"""Smoke-test do Cinegrafista 3D (3D Gaussian Splatting).

Rodável numa máquina com GPU + torch CUDA + motor 3DGS:
    python splatting_smoke.py [<imagem.png>] [<saida.mp4>]

Reporta o estado HONESTO: torch/CUDA, motor 3DGS, e tenta o render real.
Sem a toolchain, sai com diagnóstico (sem fingir sucesso)."""
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

import splatting as sp

print('=== Smoke-test 3D Gaussian Splatting ===')
try:
    import torch
    print(f'  torch: {torch.__version__} | CUDA: {torch.cuda.is_available()}')
    if torch.cuda.is_available():
        print(f'  GPU: {torch.cuda.get_device_name(0)}')
except Exception as e:
    print(f'  torch indisponível: {e}')

print(f'  gaussian_disponivel(): {sp.gaussian_disponivel()}')

if not sp.gaussian_disponivel():
    print('\n[PENDENTE] falta torch+CUDA e/ou motor 3DGS (gsplat) + splatting_engine.')
    print('           o pipeline segue usando parallax/Ken Burns — sem regressão.')
    sys.exit(1)

src = Path(sys.argv[1]) if len(sys.argv) > 1 else next(iter(sorted((ROOT / '_img').glob('*.png'))), None)
out = Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT / '_tmp_smoke_3dgs.mp4'
if not src or not Path(src).exists():
    print(f'\n[BLOQUEIO] imagem de entrada não encontrada: {src}')
    sys.exit(1)

t0 = time.monotonic()
ok = sp.splat_clip(str(src), str(out), dur=3.0, fps=24)
print(f'\n  splat_clip() -> {ok}  ({time.monotonic() - t0:.1f}s)')
if ok and out.exists():
    print(f'  mp4 gerado: {out} ({out.stat().st_size // 1024} KB)')
    print('\n[OK] Smoke-test PASSOU — 3DGS funcional nesta máquina.')
else:
    print('\n[FALHOU] render não saiu — ver motor 3DGS / splatting_engine.')
    sys.exit(2)
