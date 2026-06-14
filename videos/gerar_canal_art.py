# -*- coding: utf-8 -*-
"""Gera a arte do canal Minuto Real: avatar (800x800) e banner (2560x1440).
Custo R$0 (Pillow). Identidade: carvão + âmbar, serif elegante.

Uso:  python gerar_canal_art.py
Saída: _canal/avatar.png, _canal/banner.png
"""

from pathlib import Path
from PIL import Image, ImageDraw
import gerar_video as gv

ROOT = Path(__file__).parent
AC = gv.marca.rgb('ouro')  # ouro canônico (marca.py) = cor-assinatura do canal
BG = (10, 10, 14)


def radial(img, cx, cy, r, color, amax):
    ov = Image.new('RGBA', img.size, (0, 0, 0, 0))
    od = ImageDraw.Draw(ov)
    for i in range(40, 0, -1):
        rr = int(r * i / 40)
        a = int(amax * (1 - i / 40) ** 1.7)
        od.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], fill=color + (a,))
    img.alpha_composite(ov)


def avatar():
    S = 800
    img = Image.new('RGBA', (S, S), BG + (255,))
    radial(img, S // 2, int(S * 0.42), 460, AC, 38)
    d = ImageDraw.Draw(img)
    # anel
    d.ellipse([40, 40, S - 40, S - 40], outline=AC, width=6)
    # monograma "MR"
    fm = gv.F_TITLE(300)
    t = 'MR'
    tw = d.textlength(t, font=fm)
    d.text(((S - tw) // 2, S * 0.20), t, font=fm, fill=(245, 245, 248))
    # wordmark
    fw = gv.F_UI_B(40)
    wm = 'MINUTO REAL'
    ww = sum(d.textlength(c, font=fw) + 8 for c in wm) - 8
    gv.tracked(d, ((S - ww) // 2, int(S * 0.70)), wm, fw, AC, 8)
    out = ROOT / '_canal'
    out.mkdir(exist_ok=True)
    img.convert('RGB').save(out / 'avatar.png', quality=95)
    print('OK -> _canal/avatar.png (800x800)')


def banner():
    W, H = 2560, 1440
    img = Image.new('RGBA', (W, H), BG + (255,))
    # leve aura âmbar atrás do centro
    radial(img, W // 2, H // 2, 1100, AC, 24)
    # vinheta nas bordas
    ov = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(ov)
    for px in range(0, 700, 3):
        a = int(160 * (1 - px / 700) ** 1.4)
        od.rectangle([(px, 0), (px + 3, H)], fill=(6, 6, 9, a))
        od.rectangle([(W - px - 3, 0), (W - px, H)], fill=(6, 6, 9, a))
    img.alpha_composite(ov)
    d = ImageDraw.Draw(img)
    # SAFE AREA central ~1546x423 — todo texto aqui
    cx, cy = W // 2, H // 2
    # wordmark grande
    ft = gv.F_TITLE(150)
    t = 'MINUTO REAL'
    tw = d.textlength(t, font=ft)
    d.text((cx - tw // 2, cy - 150), t, font=ft, fill=(246, 246, 249))
    # filete
    d.rectangle([(cx - 70, cy + 28), (cx + 70, cy + 34)], fill=AC)
    # tagline
    fs = gv.F_UI(46)
    s = 'Grandes livros. As ideias que ficam — em minutos.'
    sw = d.textlength(s, font=fs)
    d.text((cx - sw // 2, cy + 58), s, font=fs, fill=(205, 205, 215))
    # cadência
    fc = gv.F_UI_B(30)
    c = 'NOVOS RESUMOS TODA SEMANA'
    cw = sum(d.textlength(ch, font=fc) + 6 for ch in c) - 6
    gv.tracked(d, (cx - cw // 2, cy + 130), c, fc, AC, 6)
    img.convert('RGB').save(ROOT / '_canal' / 'banner.png', quality=95)
    print('OK -> _canal/banner.png (2560x1440)')


if __name__ == '__main__':
    avatar()
    banner()
