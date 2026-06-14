# -*- coding: utf-8 -*-
"""Gera thumbnail 1280x720 de um vídeo, a partir de uma cena já renderizada.
Reaproveita _img/<slug>_NN.png + texto-bomba. Custo R$0 (Pillow). A maior alavanca de CTR.

Uso:  python gerar_thumb.py <slug> <idx> "TEXTO BOMBA" ["Subtítulo"]
Saída: _thumbs/<slug>.png
"""
import sys, json
from pathlib import Path
from PIL import Image, ImageDraw
import gerar_video as gv

ROOT = Path(__file__).parent
W, H = 1280, 720
F_BLACK = lambda s: gv.font('ariblk.ttf', s)   # Arial Black — leitura em miniatura


def cover(src):
    im = Image.open(src).convert('RGB')
    s = max(W / im.width, H / im.height)
    im = im.resize((max(W, int(im.width * s)), max(H, int(im.height * s))), Image.LANCZOS)
    x, y = (im.width - W) // 2, (im.height - H) // 2
    return im.crop((x, y, x + W, y + H)).convert('RGBA')


def fit_font(d, lines, maxw, start=200, floor=64):
    s = start
    while s > floor:
        f = F_BLACK(s)
        if max(d.textlength(ln, font=f) for ln in lines) <= maxw:
            return f
        s -= 5
    return F_BLACK(floor)


def main(slug, idx, punch, sub=None):
    cfg = json.loads((ROOT / 'roteiros' / f'{slug}.json').read_text(encoding='utf-8'))
    accent = gv.hex_rgb(cfg.get('acento', '#d8a64a'))
    src = ROOT / '_img' / f'{slug}_{idx:02d}.png'
    if not src.exists():
        sys.exit(f'[!] imagem ausente: {src}')

    img = cover(src)
    ov = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(ov)
    # escurecimento base + leve esquerda p/ o texto saltar
    for py in range(H - 460, H, 2):
        a = int(225 * ((py - (H - 460)) / 460) ** 1.1)
        od.rectangle([(0, py), (W, py + 2)], fill=(4, 4, 8, a))
    for px in range(0, 520, 2):
        a = int(120 * (1 - px / 520) ** 1.3)
        od.rectangle([(px, 0), (px + 2, H)], fill=(4, 4, 8, a))
    img.alpha_composite(ov)
    d = ImageDraw.Draw(img)

    # tag topo-esquerda
    gv.tracked(d, (54, 50), 'MINUTO REAL', gv.F_UI_B(34), accent, 8)

    # TEXTO-BOMBA (Arial Black, branco com contorno preto grosso) — embaixo
    words = punch.upper().split()
    mid = (len(words) + 1) // 2
    lines = [' '.join(words[:mid]), ' '.join(words[mid:])] if len(words) > 2 else [punch.upper()]
    lines = [ln for ln in lines if ln]
    ft = fit_font(d, lines, W - 108)
    lh = int(ft.size * 1.02)
    y = H - 70 - len(lines) * lh
    for ln in lines:
        d.text((54, y), ln, font=ft, fill=(248, 248, 250), stroke_width=10, stroke_fill=(6, 6, 10))
        y += lh
    # filete de acento acima do texto
    d.rectangle([(58, H - 80 - len(lines) * lh - 20), (58 + 120, H - 80 - len(lines) * lh - 8)], fill=accent)

    # subtítulo (livro) topo-direita — largura real considerando o tracking
    if sub:
        fs = gv.F_UI_B(34)
        tw = sum(d.textlength(c, font=fs) + 3 for c in sub.upper()) - 3
        gv.tracked(d, (W - tw - 54, 56), sub.upper(), fs, (235, 235, 240), 3)

    out = ROOT / '_thumbs'
    out.mkdir(exist_ok=True)
    p = out / f'{slug}.png'
    img.convert('RGB').save(p, quality=95)
    print(f'OK -> {p}')


if __name__ == '__main__':
    sub = sys.argv[4] if len(sys.argv) > 4 else None
    main(sys.argv[1], int(sys.argv[2]), sys.argv[3], sub)
