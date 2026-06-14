# -*- coding: utf-8 -*-
"""Capa de MARCA da Biblioteca — UNIFORME p/ todo livro, lê `marca.py`.

Substitui a capa de editora (cada uma um estilo) por uma estante COESA e premium,
na identidade da rede: fundo escuro + glow verde, moldura tracejada (DNA cheat sheet),
wordmark, título em Hanken Black, fio de ouro e autor. Estrutura igual p/ todos;
conteúdo único por livro.

Uso:  python gerar_capa.py <slug> "Título" "Autor"
Saída: assets/<slug>-cover.png  (800x1200, 2:3)
"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw
import marca

BASE = Path(__file__).parent
W, H = 800, 1200


def radial_glow(img, cx, cy, r, color, amax):
    ov = Image.new('RGBA', img.size, (0, 0, 0, 0))
    od = ImageDraw.Draw(ov)
    for i in range(44, 0, -1):
        rr = int(r * i / 44)
        a = int(amax * (1 - i / 44) ** 1.8)
        od.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], fill=color + (a,))
    img.alpha_composite(ov)


def dashed_rect(d, box, color, w=3, dash=14, gap=11):
    x0, y0, x1, y1 = box
    x = x0
    while x < x1:
        d.line([(x, y0), (min(x + dash, x1), y0)], fill=color, width=w)
        d.line([(x, y1), (min(x + dash, x1), y1)], fill=color, width=w)
        x += dash + gap
    y = y0
    while y < y1:
        d.line([(x0, y), (x0, min(y + dash, y1))], fill=color, width=w)
        d.line([(x1, y), (x1, min(y + dash, y1))], fill=color, width=w)
        y += dash + gap


def wrap(d, text, fnt, maxw):
    words, lines, cur = text.split(), [], ''
    for wd in words:
        t = (cur + ' ' + wd).strip()
        if d.textlength(t, font=fnt) <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = wd
    if cur:
        lines.append(cur)
    return lines


def tracked(d, text, fnt, fill, tr, cy, y):
    """Desenha `text` com tracking `tr`, centralizado horizontalmente em cy."""
    tw = sum(d.textlength(c, font=fnt) + tr for c in text) - (tr if text else 0)
    x = cy - tw / 2
    for ch in text:
        d.text((x, y), ch, font=fnt, fill=fill)
        x += d.textlength(ch, font=fnt) + tr


def main(slug, title, author):
    papel, verde, ouro = marca.rgb('papel'), marca.rgb('verde'), marca.rgb('ouro')
    ink, dim = marca.rgb('tinta'), marca.rgb('tinta-fraca')
    img = Image.new('RGBA', (W, H), papel + (255,))
    radial_glow(img, W // 2, int(H * 0.34), 560, verde, 24)
    radial_glow(img, int(W * 0.5), int(H * 0.04), 360, ouro, 11)
    d = ImageDraw.Draw(img)

    dashed_rect(d, (46, 46, W - 46, H - 46), verde + (255,), 3)

    # wordmark + fio de ouro
    tracked(d, 'BIBLIOTECA', marca.font('display', 31, 'ExtraBold'), verde, 7, W // 2, 96)
    d.rectangle([(W // 2 - 60, 150), (W // 2 + 60, 156)], fill=ouro)

    # título (Hanken Black), encolhe até caber em ≤4 linhas
    ft = marca.font('display', 96, 'Black')
    lines = wrap(d, title.upper(), ft, W - 210)
    while len(lines) > 4 and ft.size > 50:
        ft = marca.font('display', ft.size - 6, 'Black')
        lines = wrap(d, title.upper(), ft, W - 210)
    lh = int(ft.size * 1.05)
    y = (H - len(lines) * lh) // 2 - 24
    for ln in lines:
        lw = d.textlength(ln, font=ft)
        d.text(((W - lw) // 2, y), ln, font=ft, fill=ink)
        y += lh

    # fio de ouro + autor
    d.rectangle([(W // 2 - 46, y + 30), (W // 2 + 46, y + 36)], fill=ouro)
    tracked(d, author.upper(), marca.font('display', 33, 'SemiBold'), marca.rgb('ouro-soft'), 4, W // 2, y + 66)

    # selo rodapé
    tracked(d, 'RESUMO · UMA PÁGINA', marca.font('display', 24, 'Bold'), dim, 6, W // 2, H - 150)

    (BASE / 'assets').mkdir(exist_ok=True)
    out = BASE / 'assets' / f'{slug}-cover.png'
    img.convert('RGB').save(out, quality=95)
    print(f'OK -> assets/{slug}-cover.png')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
