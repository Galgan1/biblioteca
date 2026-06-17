# -*- coding: utf-8 -*-
"""Capa de estante da Biblioteca — HÍBRIDA: arte ORIGINAL do livro (reconhecimento)
dentro de uma moldura de MARCA uniforme (coesão). Lê `marca.py`.

Estante coesa SEM perder o reconhecimento da capa real. Saída em `-capa.png`
(preserva o original `-cover.png/.jpg`, que segue como fonte da arte).

  framed(slug, art)      -> arte real emoldurada
  typographic(slug,t,a)  -> fallback tipográfico (itens sem capa real)

Uso:  python gerar_capa.py <slug> <art.png>            # híbrida
      python gerar_capa.py <slug> --typo "Título" "Autor"
Saída: assets/<slug>-capa.png (800x1200, 2:3)
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


def _wrap(d, text, fnt, maxw):
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


def _tracked(d, text, fnt, fill, tr, cx, y):
    tw = sum(d.textlength(c, font=fnt) + tr for c in text) - (tr if text else 0)
    x = cx - tw / 2
    for ch in text:
        d.text((x, y), ch, font=fnt, fill=fill)
        x += d.textlength(ch, font=fnt) + tr


def _chrome(img, d):
    """Moldura de marca comum a todas as capas: glow + traço tracejado + wordmark."""
    verde, ouro, dim = marca.rgb('verde'), marca.rgb('ouro'), marca.rgb('tinta-fraca')
    radial_glow(img, W // 2, int(H * 0.30), 560, verde, 22)
    radial_glow(img, W // 2, int(H * 0.03), 340, ouro, 9)
    dashed_rect(d, (40, 40, W - 40, H - 40), verde + (255,), 3)
    _tracked(d, 'BIBLIOTECA', marca.font('display', 30, 'ExtraBold'), verde, 7, W // 2, 80)
    d.rectangle([(W // 2 - 58, 124), (W // 2 + 58, 130)], fill=ouro)
    # CTA preenchido: fundo verde da marca + texto escuro (papel) — Norman: significante saliente
    cta_fnt = marca.font('display', 23, 'Bold')
    cta_text = 'RESUMO · UMA PÁGINA'
    cta_tw = sum(d.textlength(c, font=cta_fnt) + 6 for c in cta_text) - 6
    cta_pad_x, cta_pad_y = 18, 8
    cta_y = H - 150
    cta_x0 = W // 2 - cta_tw // 2 - cta_pad_x
    cta_x1 = W // 2 + cta_tw // 2 + cta_pad_x
    cta_y0 = cta_y - cta_pad_y
    cta_y1 = cta_y + cta_fnt.size + cta_pad_y
    d.rectangle([(cta_x0, cta_y0), (cta_x1, cta_y1)], fill=verde)
    _tracked(d, cta_text, cta_fnt, marca.rgb('papel'), 6, W // 2, cta_y)


def _band(img, d, title, author, top, bottom):
    """Faixa inferior de marca com titulo + autor proprios (legibilidade na miniatura,
    independente da arte). Reaproveita o bloco de texto do `typographic`."""
    ink, ouro = marca.rgb('tinta'), marca.rgb('ouro')
    # backing solido na zona livre (cobre a tagline compartilhada, sela a base da faixa)
    d.rectangle([(50, top), (W - 50, bottom)], fill=marca.rgb('papel'))
    # hairline dourada separando a arte da faixa
    d.rectangle([(W // 2 - 58, top + 8), (W // 2 + 58, top + 14)], fill=ouro)
    # titulo (mesmo wrap/auto-fit do typographic, comprimido p/ a faixa)
    ft = marca.font('display', 46, 'Black')
    lines = _wrap(d, title.upper(), ft, W - 150)
    while len(lines) > 2 and ft.size > 26:
        ft = marca.font('display', ft.size - 4, 'Black')
        lines = _wrap(d, title.upper(), ft, W - 150)
    lines = lines[:2]
    lh = int(ft.size * 1.04)
    fa = marca.font('display', 24, 'SemiBold')
    block_h = len(lines) * lh + 22 + fa.size
    y = top + 24 + ((bottom - top - 24) - block_h) // 2
    for ln in lines:
        lw = d.textlength(ln, font=ft)
        d.text(((W - lw) // 2, y), ln, font=ft, fill=ink)
        y += lh
    _tracked(d, author.upper(), fa, marca.rgb('ouro-soft'), 4, W // 2, y + 14)


def framed(slug, art_path, title=None, author=None):
    """Arte real do livro emoldurada na marca, com faixa inferior de titulo+autor."""
    img = Image.new('RGBA', (W, H), marca.rgb('papel') + (255,))
    d = ImageDraw.Draw(img)
    _chrome(img, d)
    WIN_T, WIN_B, WIN_W = 176, 1010, 612
    win_h = WIN_B - WIN_T
    art = Image.open(art_path).convert('RGB')
    s = min(WIN_W / art.width, win_h / art.height)
    aw, ah = max(1, int(art.width * s)), max(1, int(art.height * s))
    art = art.resize((aw, ah), Image.LANCZOS)
    ax, ay = (W - aw) // 2, WIN_T + (win_h - ah) // 2
    d.rectangle([(ax - 3, ay - 3), (ax + aw + 2, ay + ah + 2)], outline=marca.rgb('ouro'), width=2)
    img.paste(art, (ax, ay))
    if title is None or author is None:
        import json
        books = {b['id']: b for b in json.load(open(BASE / 'books.json', encoding='utf-8'))}
        b = books.get(slug, {})
        title = title or b.get('title', slug)
        author = author or b.get('author', '')
    _band(img, d, title, author, WIN_B + 8, H - 48)
    out = BASE / 'assets' / f'{slug}-capa.png'
    img.convert('RGB').save(out, quality=92)
    print(f'OK framed -> assets/{slug}-capa.png')


def typographic(slug, title, author):
    """Fallback p/ itens sem capa real (não-livros)."""
    img = Image.new('RGBA', (W, H), marca.rgb('papel') + (255,))
    d = ImageDraw.Draw(img)
    _chrome(img, d)
    ink, ouro = marca.rgb('tinta'), marca.rgb('ouro')
    ft = marca.font('display', 92, 'Black')
    lines = _wrap(d, title.upper(), ft, W - 210)
    while len(lines) > 4 and ft.size > 50:
        ft = marca.font('display', ft.size - 6, 'Black')
        lines = _wrap(d, title.upper(), ft, W - 210)
    lh = int(ft.size * 1.05)
    y = (H - len(lines) * lh) // 2 - 24
    for ln in lines:
        lw = d.textlength(ln, font=ft)
        d.text(((W - lw) // 2, y), ln, font=ft, fill=ink)
        y += lh
    d.rectangle([(W // 2 - 46, y + 28), (W // 2 + 46, y + 34)], fill=ouro)
    _tracked(d, author.upper(), marca.font('display', 33, 'SemiBold'), marca.rgb('ouro-soft'), 4, W // 2, y + 64)
    out = BASE / 'assets' / f'{slug}-capa.png'
    img.convert('RGB').save(out, quality=92)
    print(f'OK typo -> assets/{slug}-capa.png')


def banner(slug, title, author, art_path=None):
    """OG banner 1200×630 (1.91:1) para compartilhamento social.
    Saída: assets/{slug}-og.png
    """
    BW, BH = 1200, 630
    PAD = 60

    # fundo escuro da marca
    bg = marca.rgb('papel')   # dark hex (#08080c) — usamos o hex escuro direto
    ink = marca.rgb('tinta')  # claro no canvas escuro (#f2f2f5)
    verde = marca.rgb('verde')
    ouro = marca.rgb('ouro')
    dim = marca.rgb('tinta-fraca')

    img = Image.new('RGB', (BW, BH), bg)
    d = ImageDraw.Draw(img)

    # --- área do livro: direita ---
    COVER_X = 680
    COVER_W = BW - COVER_X - PAD
    COVER_H = BH - PAD * 2
    if art_path and Path(art_path).exists():
        art = Image.open(art_path).convert('RGB')
        s = min(COVER_W / art.width, COVER_H / art.height)
        aw, ah = max(1, int(art.width * s)), max(1, int(art.height * s))
        art = art.resize((aw, ah), Image.LANCZOS)
        ax = COVER_X + (COVER_W - aw) // 2
        ay = (BH - ah) // 2
        img.paste(art, (ax, ay))
        # sombra leve à esquerda da capa
        ov = Image.new('RGBA', (BW, BH), (0, 0, 0, 0))
        od = ImageDraw.Draw(ov)
        for i in range(60):
            alpha = int(80 * (1 - i / 60) ** 1.5)
            od.line([(ax - i, 0), (ax - i, BH)], fill=(0, 0, 0, alpha))
        img = Image.alpha_composite(img.convert('RGBA'), ov).convert('RGB')
        d = ImageDraw.Draw(img)

    # --- área de texto: esquerda ---
    TX = PAD + 10

    # wordmark BIBLIOTECA
    ft_brand = marca.font('display', 26, 'ExtraBold')
    _tracked(d, 'BIBLIOTECA', ft_brand, verde, 6, TX + 120, PAD + 2)
    # traço dourado
    d.rectangle([(TX, PAD + 42), (TX + 240, PAD + 46)], fill=ouro)

    # título — font grande, quebra em linhas
    ft_title = marca.font('display', 76, 'Black')
    lines = _wrap(d, title.upper(), ft_title, 620 - TX)
    while len(lines) > 4 and ft_title.size > 44:
        ft_title = marca.font('display', ft_title.size - 8, 'Black')
        lines = _wrap(d, title.upper(), ft_title, 620 - TX)
    lh = int(ft_title.size * 1.08)
    text_block_h = len(lines) * lh
    ty = (BH - text_block_h) // 2 - 20
    for ln in lines:
        d.text((TX, ty), ln, font=ft_title, fill=ink)
        ty += lh

    # autor
    ft_author = marca.font('display', 28, 'SemiBold')
    d.text((TX, ty + 16), author.upper(), font=ft_author, fill=ouro)

    # tagline em baixo
    ft_tag = marca.font('display', 20, 'Bold')
    _tracked(d, 'RESUMO · UMA PÁGINA', ft_tag, dim, 4, TX + 140, BH - PAD - 22)

    out = BASE / 'assets' / f'{slug}-og.png'
    img.save(out, quality=92)
    print(f'OK banner -> assets/{slug}-og.png')


if __name__ == '__main__':
    if len(sys.argv) >= 4 and sys.argv[2] == '--typo':
        typographic(sys.argv[1], sys.argv[3], sys.argv[4])
    elif len(sys.argv) >= 3 and sys.argv[2] == '--banner':
        art = sys.argv[3] if len(sys.argv) >= 4 else None
        import json
        books = {b['id']: b for b in json.load(open(BASE / 'books.json', encoding='utf-8'))}
        b = books[sys.argv[1]]
        banner(sys.argv[1], b['title'], b['author'], art)
    else:
        framed(sys.argv[1], sys.argv[2])
