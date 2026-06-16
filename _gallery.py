# -*- coding: utf-8 -*-
"""Monta UM contact-sheet leve (as 7 pecas numa imagem so, com rotulos) e grava o
HTML do widget (1 img base64) — pequeno o bastante p/ exibir INLINE."""
import base64, io
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

SRC = Path('videos/_premium/48-leis-do-poder/_preview')
ITEMS = [('01.jpg','1 Capa'),('02.jpg','2 Natureza'),('03.jpg','3 Aparencias'),
         ('04.jpg','4 Seducao'),('05.jpg','5 Lei Suprema'),('06.jpg','6 CTA'),('mapa.jpg','7 Mapa')]

COLS, TW, PAD, LBL = 4, 108, 7, 16
TH = int(TW * 1350 / 1080)
rows = (len(ITEMS) + COLS - 1) // COLS
W = COLS * TW + (COLS + 1) * PAD
H = rows * (TH + LBL + PAD) + PAD
sheet = Image.new('RGB', (W, H), (8, 11, 14))
d = ImageDraw.Draw(sheet)
try:
    font = ImageFont.truetype(str(Path('_fonts/HankenGrotesk.ttf')), 12)
except Exception:
    font = ImageFont.load_default()

for i, (f, lab) in enumerate(ITEMS):
    r, c = divmod(i, COLS)
    x = PAD + c * (TW + PAD)
    y = PAD + r * (TH + LBL + PAD)
    im = Image.open(SRC / f).convert('RGB').resize((TW, TH), Image.LANCZOS)
    sheet.paste(im, (x, y))
    d.text((x + 2, y + TH + 2), lab, fill=(150, 220, 180), font=font)

buf = io.BytesIO()
sheet.save(buf, 'JPEG', quality=32, optimize=True)
b64 = base64.b64encode(buf.getvalue()).decode()
html = (f'<div style="padding:4px 0"><img src="data:image/jpeg;base64,{b64}" '
        f'style="width:100%;border-radius:12px;display:block" alt="48 Leis - 7 pecas premium"></div>')
Path('videos/_premium/48-leis-do-poder/_preview/cs_widget.html').write_text(html, encoding='utf-8')
print('img KB:', round(len(buf.getvalue()) / 1024), '| base64 chars:', len(b64), '| html chars:', len(html))
