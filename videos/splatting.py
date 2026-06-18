# -*- coding: utf-8 -*-
"""Cinegrafista 3D — 3D Gaussian Splatting local (GPU). Eleva a imagem estática a uma
CENA 3D navegável: a imagem vira um campo de Gaussians 3D e renderizamos um movimento
de câmera (dolly/órbita) — profundidade real, além do parallax 2.5D do DepthFlow.

Custo por vídeo: ~zero (roda na GPU local). PRÉ-REQUISITOS DUROS:
  • GPU NVIDIA + torch COM CUDA (torch CPU NÃO serve);
  • um motor 3DGS de imagem única (ex.: gsplat) instalado e compilado p/ a sua GPU.

Enquanto faltarem, `gaussian_disponivel()` é False e o pipeline cai para parallax
(DepthFlow) → Ken Burns — ZERO regressão (mesma filosofia soberana do tts/cinegrafista).
O que está coberto por teste aqui é a DECISÃO, o GUARD e a MATEMÁTICA da órbita; o
render 3DGS real precisa de smoke-test em GPU (ver `splatting_smoke.py`).
"""
import importlib.util
import os
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).parent


def gaussian_disponivel():
    """True só se houver torch COM CUDA E o backend CUDA do gsplat REALMENTE compilado.
    Instalar o pacote `gsplat` NÃO basta: sem CUDA toolkit (nvcc) + compilador (MSVC), o
    backend fica desabilitado (`_C is None`) e o gsplat se auto-desativa. Só então o
    tratamento 'gaussian' entra; senão devolve False e o caller usa parallax/Ken Burns."""
    try:
        import torch
        if not torch.cuda.is_available():
            return False
    except Exception:
        return False
    if importlib.util.find_spec('gsplat') is None:
        return False
    try:
        from gsplat.cuda._backend import _C    # dispara o build; _C is None se não compilou
        return _C is not None
    except Exception:
        return False


def orbit_poses(n=48, raio=2.0, arco_graus=30.0, altura=0.0, alvo=(0.0, 0.0, 0.0)):
    """PURO: posições de câmera de um movimento cinematográfico suave em arco horizontal
    ao redor do alvo (não 360° — um leve travelling que revela profundidade sem enjoo).

    -> np.ndarray (n, 3) de posições XYZ; toda câmera fica a `raio` do alvo.
    O motor de render usa estas poses (look-at no alvo) para gerar os frames."""
    alvo = np.asarray(alvo, dtype=np.float64)
    meia = np.deg2rad(arco_graus) / 2.0
    thetas = np.linspace(-meia, meia, n)
    # arco no plano XZ, câmera "à frente" do alvo (eixo +Z), olhando para ele
    x = alvo[0] + raio * np.sin(thetas)
    z = alvo[2] + raio * np.cos(thetas)
    y = np.full(n, alvo[1] + altura)
    pos = np.stack([x, y, z], axis=1)
    # normaliza a distância exata ao alvo (a altura encurtaria o raio no plano)
    d = np.linalg.norm(pos - alvo, axis=1, keepdims=True)
    return alvo + (pos - alvo) / d * raio


def splat_clip(src_png, out_mp4, dur=6.0, fps=30):
    """Renderiza um clipe 3DGS (mudo) com movimento de câmera a partir de UMA imagem.
    True em sucesso; False se indisponível ou se o render falhar (nunca levanta) — o
    caller faz fallback para parallax/Ken Burns.

    NOTA HONESTA: o motor concreto (imagem→Gaussians→render das `orbit_poses`) é
    plugado no setup de GPU; enquanto `gaussian_disponivel()` é False, retorna aqui
    sem tocar a GPU. Validar com `splatting_smoke.py` numa máquina com CUDA."""
    if not gaussian_disponivel():
        return False
    try:
        import splatting_engine                      # motor concreto, instalado no setup de GPU
        poses = orbit_poses(n=int(dur * fps))
        splatting_engine.render(str(src_png), str(out_mp4), poses=poses, fps=fps)
        return Path(out_mp4).exists()
    except Exception:
        return False


if __name__ == '__main__':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    print('=== Cinegrafista 3D (3D Gaussian Splatting) ===')
    print(f'  gaussian_disponivel(): {gaussian_disponivel()}')
    print(f'  órbita de exemplo (6 poses): {orbit_poses(n=6).round(3).tolist()}')
    if not gaussian_disponivel():
        print('  [pendente] sem torch+CUDA e/ou motor 3DGS — pipeline usa parallax/Ken Burns.')
