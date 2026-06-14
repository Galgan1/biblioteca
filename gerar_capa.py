# -*- coding: utf-8 -*-
"""Capa tipográfica (fallback) no verde da biblioteca, quando não há capa real do PDF.
Uso:  python gerar_capa.py <slug> "Título do Livro" "Autor"
Saída: assets/<slug>-cover.png  (800x1200)
"""

import sys, os
from PIL import Image, ImageDraw, ImageFont

BASE = os.path.dirname(os.path.abspath(__file__))
W, H = 800, 1200
GREEN = (35, 158, 90)
PAPER = (247, 248, 245)
INK = (24, 28, 24)


def font(sz, bold=True):
    for name in (("Hanken Grotesk", "ariblk.ttf"), ("arialbd.ttf",), ("arial.ttf",)):
        for f in name:
            try:
                return ImageFont.truetype(f"C:/Windows/Fonts/{f}", sz)
            except Exception:
                continue
    return ImageFont.load_default()


def wrap(d, text, fnt, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=fnt) <= maxw:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def main(slug, title, author):
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W, 130], fill=GREEN)  # faixa superior
    d.rectangle([0, H - 90, W, H], fill=GREEN)  # faixa inferior
    # moldura tracejada
    for x in range(40, W - 40, 22):
        d.line([(x, 170), (x + 12, 170)], fill=GREEN, width=3)
        d.line([(x, H - 130), (x + 12, H - 130)], fill=GREEN, width=3)
    for y in range(170, H - 130, 22):
        d.line([(40, y), (40, y + 12)], fill=GREEN, width=3)
        d.line([(W - 40, y), (W - 40, y + 12)], fill=GREEN, width=3)
    d.text((50, 44), "BIBLIOTECA", font=font(34), fill=PAPER)
    # título centralizado
    ft = font(86)
    lines = wrap(d, title.upper(), ft, W - 160)
    while len(lines) > 4 and ft.size > 48:
        ft = font(ft.size - 6)
        lines = wrap(d, title.upper(), ft, W - 160)
    y = H // 2 - len(lines) * int(ft.size * 0.58)
    for ln in lines:
        w = d.textlength(ln, font=ft)
        d.text(((W - w) // 2, y), ln, font=ft, fill=INK)
        y += int(ft.size * 1.12)
    d.rectangle([(W // 2 - 60, y + 30), (W // 2 + 60, y + 38)], fill=GREEN)
    fa = font(40, bold=False)
    wa = d.textlength(author, font=fa)
    d.text(((W - wa) // 2, y + 70), author, font=fa, fill=GREEN)
    os.makedirs(os.path.join(BASE, "assets"), exist_ok=True)
    out = os.path.join(BASE, "assets", f"{slug}-cover.png")
    img.save(out, quality=95)
    print(f"OK -> assets/{slug}-cover.png")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
