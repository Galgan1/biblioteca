# -*- coding: utf-8 -*-
"""Converte todos os *-capa.png da estante para WebP (q=82).
Idempotente: pula arquivos que já têm versão .webp.
Uso: python converter_webp.py
"""
from pathlib import Path
from PIL import Image

BASE = Path(__file__).parent
ASSETS = BASE / 'assets'
QUALITY = 82

capas = sorted(ASSETS.glob('*-capa.png'))
total_before = total_after = 0
converted = skipped = 0

for png in capas:
    webp = png.with_suffix('.webp')
    if webp.exists():
        skipped += 1
        continue
    img = Image.open(png).convert('RGB')
    img.save(webp, 'WEBP', quality=QUALITY, method=6)
    before = png.stat().st_size
    after = webp.stat().st_size
    total_before += before
    total_after += after
    ratio = (1 - after / before) * 100
    print(f'  {png.name}: {before//1024}KB -> {after//1024}KB  (-{ratio:.0f}%)')
    converted += 1

print(f'\nConvertidos: {converted}  Pulados: {skipped}')
if total_before:
    print(f'Total: {total_before//1024}KB → {total_after//1024}KB  (-{(1-total_after/total_before)*100:.0f}%)')
