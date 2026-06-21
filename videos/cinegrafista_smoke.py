# -*- coding: utf-8 -*-
"""Smoke-test manual do render parallax 2.5D via DepthFlow.

Rodável em qualquer máquina após `pip install depthflow`:
    python cinegrafista_smoke.py [<imagem.png>] [<saida.mp4>]

Sem GPU: roda em CPU (lento, ~15s p/ 3s de vídeo). Com GPU: ~2-5s.
Imprime o resultado honesto: mp4 gerado, duração real, tempo de render.
"""
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

import cinegrafista as cg

# ---------------------------------------------------------------------- #
# Argumentos opcionais: imagem de entrada e arquivo de saída
# ---------------------------------------------------------------------- #
def _default_png() -> Path:
    """Usa o primeiro PNG em _img/ ou gera um slide 1920×1080 com PIL."""
    imgs = sorted((ROOT / '_img').glob('*.png'))
    if imgs:
        return imgs[0]
    # sem _img/, gera um slide mínimo para o smoke
    try:
        from PIL import Image, ImageDraw
        p = ROOT / '_tmp_smoke_input.png'
        img = Image.new('RGB', (1920, 1080), (20, 60, 40))
        ImageDraw.Draw(img).text((80, 80), 'DepthFlow smoke test', fill=(255, 255, 255))
        img.save(str(p))
        print(f'[smoke] gerado PNG de teste: {p}')
        return p
    except ImportError:
        print('[smoke] ERRO: sem Pillow e sem _img/ — forneça um PNG como argumento.')
        sys.exit(1)


src  = Path(sys.argv[1]) if len(sys.argv) > 1 else _default_png()
out  = Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT / '_tmp_smoke_parallax_final.mp4'
DUR  = 3.0   # segundos de vídeo
FPS  = 24

# ---------------------------------------------------------------------- #
print(f'\n=== Smoke-test cinegrafista.parallax() ===')
print(f'  entrada : {src}')
print(f'  saida   : {out}')
print(f'  duração : {DUR}s @ {FPS}fps')
print(f'  depthflow disponivel: {cg.depthflow_disponivel()}')

if not cg.depthflow_disponivel():
    print('\n[BLOQUEIO] DepthFlow não importável — rode: pip install depthflow')
    sys.exit(1)

if not src.exists():
    print(f'\n[BLOQUEIO] Imagem não encontrada: {src}')
    sys.exit(1)

if out.exists():
    out.unlink()

t0 = time.monotonic()
ok = cg.parallax(str(src), str(out), dur=DUR, fps=FPS)
elapsed = time.monotonic() - t0

print(f'\n  parallax() retornou: {ok}  ({elapsed:.1f}s)')

if ok and out.exists():
    size_kb = out.stat().st_size // 1024
    # duração real via ffprobe
    r = subprocess.run(
        ['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
         '-of', 'default=noprint_wrappers=1:nokey=1', str(out)],
        capture_output=True, timeout=15
    )
    duracao_real = r.stdout.decode(errors='replace').strip()
    print(f'  mp4 gerado  : {out}  ({size_kb} KB)')
    print(f'  duração real: {duracao_real}s  (esperado: {DUR}s)')
    print('\n[OK] Smoke-test PASSOU — DepthFlow funcional nesta máquina.')
else:
    print('\n[FALHOU] mp4 não gerado. Verifique stderr do processo acima.')
    sys.exit(2)
