# -*- coding: utf-8 -*-
"""Gerador PREMIUM do "MAPA DO LIVRO" (infografico field-guide, 1080x1350) — no
nivel da referencia do usuario: colunas MULTICOR, uma MINI-ILUSTRACAO de IA por
item (videos/imagen.py), icones NEON com glow, chips com glow, fundo de hexagonos.

Cache das artes em videos/_premium/<slug>/mapa_*.png (nao regera se existe).
  python gerar_mapa.py <slug> [--no-img]
Saida: videos/_premium/<slug>/mapa.png
"""
import sys, base64
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / 'videos'))
import gerar_carrossel as gc
from gerar_livro import ICONS
from gerar_infografico import _chapter_title, _chapter_num, _even_sample, _first_sentence, _font_face

OUT = ROOT / 'videos' / '_premium'
FONTS = ROOT / '_fonts'
W, H = 1080, 1350

# paleta multicor controlada (1 cor por coluna) — verde lidera, depois varia
ACCENTS = [
    ('oklch(74% 0.17 152)', 'emerald green'),
    ('oklch(70% 0.15 245)', 'electric blue'),
    ('oklch(76% 0.15 190)', 'cyan teal'),
    ('oklch(78% 0.15 75)',  'amber gold'),
    ('oklch(66% 0.19 300)', 'violet purple'),
]
BASE_STYLE = ("single central symbolic object, glowing neon rim light, dark moody background, "
              "cinematic product-shot, painterly digital art, highly detailed, centered composition, "
              "no text, no words, no letters")


def _b64(p): return base64.b64encode(Path(p).read_bytes()).decode('ascii')



def _svg(name, ic=None):
    inner = ICONS.get(name) or ICONS['book']
    return f'<svg viewBox="0 0 64 64" fill="none">{inner}</svg>'


def _art(slug, key, scene, cname, no_img):
    d = OUT / slug; d.mkdir(parents=True, exist_ok=True)
    p = d / f'mapa_{key}.png'
    if p.exists() or no_img:
        return p if p.exists() else None
    import imagen
    prompt = f"a symbolic illustration representing '{scene}', {cname} neon glow, {BASE_STYLE}"
    print(f'  [imagen-ultra] {key}: {scene[:48]}...')
    return p if imagen.gen(prompt, str(p), aspect='3:4', tier='ultra') else None


# fundo de hexagonos (SVG data-uri, faint verde)
_HEX = ("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='56' height='48' "
        "viewBox='0 0 56 48'><path d='M14 0l14 8v16l-14 8L0 24V8z M42 0l14 8v16l-14 8-14-8V8z' "
        "fill='none' stroke='%2316c97a' stroke-opacity='0.10' stroke-width='1'/></svg>")

CSS = """
__FF__
*{margin:0;padding:0;box-sizing:border-box}
.slide{width:1080px;height:1350px;position:relative;overflow:hidden;font-family:'Hanken Grotesk',sans-serif;
  color:#eef2f0;padding:46px 40px 30px;display:flex;flex-direction:column;
  background:#06090c;background-image:url("__HEX__"),radial-gradient(120% 70% at 50% 0%, oklch(26% 0.06 152 / .5), transparent 60%);}
.slide::after{content:'';position:absolute;inset:24px;border:2px solid oklch(74% 0.12 152 / .22);border-radius:26px;pointer-events:none}
.head{flex:0 0 auto;text-align:center;position:relative;z-index:1}
.htop{display:flex;justify-content:space-between;align-items:center}
.brand{display:inline-flex;align-items:center;gap:11px;font-weight:900;letter-spacing:.04em;font-size:24px;text-transform:uppercase}
.brand .seal{width:42px;height:42px;border-radius:12px;display:flex;align-items:center;justify-content:center;background:oklch(74% 0.17 152);color:#06140d}
.brand .seal svg{width:25px;height:25px} .brand b{color:oklch(82% 0.14 152)}
.maptag{font-weight:800;font-size:18px;letter-spacing:.14em;text-transform:uppercase;color:oklch(86% 0.10 152);
  border:1.5px solid oklch(80% 0.14 152 / .5);border-radius:999px;padding:8px 18px;box-shadow:0 0 18px oklch(74% 0.17 152 / .35)}
.title{font-size:74px;font-weight:900;line-height:.92;letter-spacing:-.02em;text-transform:uppercase;margin-top:18px;color:#fff;
  text-shadow:0 0 38px oklch(80% 0.16 152 / .55)}
.promise{font-family:'Literata',serif;font-style:italic;font-size:27px;color:oklch(88% 0.07 152);margin-top:12px}
.grid{flex:1 1 auto;display:grid;grid-template-columns:repeat(5,1fr);gap:12px;margin-top:22px;position:relative;z-index:1}
.col{display:flex;flex-direction:column;border-radius:14px;overflow:hidden;background:oklch(16% 0.02 152 / .6);
  border:1.5px solid var(--ac);box-shadow:0 0 22px color-mix(in oklch, var(--ac) 22%, transparent)}
.chead{background:var(--ac);color:#06120b;font-weight:900;font-size:18px;line-height:1.04;text-transform:uppercase;padding:10px 9px;min-height:74px}
.chead small{display:block;font-size:13px;opacity:.8;letter-spacing:.06em}
.cimg{width:100%;height:150px;object-fit:cover;border-bottom:1.5px solid var(--ac)}
.cdesc{font-size:17px;line-height:1.22;color:#dfe6e2;font-weight:500;padding:11px 10px;flex:1 1 auto}
.cdesc b{color:var(--ac);font-weight:800}
.cicon{align-self:center;width:54px;height:54px;display:flex;align-items:center;justify-content:center;margin:2px 0}
.cicon svg{width:40px;height:40px;color:var(--ac);filter:drop-shadow(0 0 9px var(--ac))}
.cuso{padding:6px 10px 10px;font-size:14px;line-height:1.2;color:#c4ccc7;font-weight:600;text-align:center}
.cuso b{display:block;color:var(--ac);font-weight:900;letter-spacing:.1em;margin-bottom:3px;text-shadow:0 0 10px color-mix(in oklch, var(--ac) 60%, transparent)}
.cchip{margin:0 auto 12px;width:54px;height:54px;border-radius:50%;border:2px solid var(--ac);display:flex;flex-direction:column;
  align-items:center;justify-content:center;font-weight:900;color:var(--ac);box-shadow:0 0 16px color-mix(in oklch, var(--ac) 45%, transparent)}
.cchip .n{font-size:22px;line-height:.9} .cchip .l{font-size:11px;letter-spacing:.1em}
.foot{flex:0 0 auto;display:flex;align-items:center;gap:16px;margin-top:16px;padding:16px 22px;border-radius:16px;position:relative;z-index:1;
  border:1.5px solid oklch(78% 0.14 152 / .4);background:oklch(20% 0.05 152 / .5);box-shadow:0 0 26px oklch(74% 0.17 152 / .25)}
.foot .fi{flex:0 0 auto;width:52px;height:52px;border-radius:13px;display:flex;align-items:center;justify-content:center;background:oklch(78% 0.15 152);color:#06140d}
.foot .fi svg{width:32px;height:32px}
.foot .ft{font-size:22px;font-weight:600;color:#eef2f0} .foot .ft b{color:oklch(84% 0.13 152);font-weight:900;letter-spacing:.06em;text-transform:uppercase}
.hand{text-align:center;font-weight:800;letter-spacing:.2em;font-size:16px;color:oklch(80% 0.05 152 / .8);text-transform:uppercase;margin-top:10px;position:relative;z-index:1}
"""


def _col(item, accent):
    ac, _ = accent
    art = item['art']
    img = f'<img class="cimg" src="data:image/png;base64,{_b64(art)}">' if art else '<div class="cimg"></div>'
    return (f'<div class="col" style="--ac:{ac}">'
            f'<div class="chead"><small>{item["kicker"]}</small>{item["title"]}</div>'
            f'{img}'
            f'<div class="cdesc">{item["desc"]}</div>'
            f'<div class="cicon">{_svg(item["ic"])}</div>'
            f'<div class="cuso"><b>Uso</b>{item["uso"]}</div>'
            f'<div class="cchip"><span class="n">{item["cap"]}</span><span class="l">cap</span></div>'
            f'</div>')


def build(slug, no_img=False):
    data = __import__(slug.replace('-', '_') + '_data')
    book = data.BOOK
    chaps = _even_sample(getattr(data, 'CHAPTERS', []), 5)
    items = []
    for i, ch in enumerate(chaps):
        t = _chapter_title(ch)
        card = (ch.get('cards') or [{}])[0]
        uso = gc._lead(__import__('re').sub(r'^<strong>.*?</strong>\s*', '', card.get('tip', '') or ch.get('intro', '')), max_sent=1, cap=70)
        items.append({
            'kicker': f'Eixo Nº {i + 1}:',
            'title': t,
            'desc': _first_sentence(ch.get('intro', ''), 90),
            'ic': card.get('ic', 'book'),
            'uso': uso,
            'cap': _chapter_num(ch) or f'{i + 1:02d}',
            'art': _art(slug, f'{i + 1}', t, ACCENTS[i % len(ACCENTS)][1], no_img),
        })

    cols = ''.join(_col(it, ACCENTS[i % len(ACCENTS)]) for i, it in enumerate(items))
    spark = ('<svg viewBox="0 0 64 64" fill="none"><path d="M32 10l5 17 17 5-17 5-5 17-5-17-17-5 17-5z" '
             'stroke="currentColor" stroke-width="3" stroke-linejoin="round"/></svg>')
    # melhor dica do overview
    dica = ''
    for c in book.get('overview_cards', []):
        if c.get('tip'):
            dica = gc._lead(__import__('re').sub(r'^<strong>.*?</strong>\s*', '', c['tip']), max_sent=1, cap=95)
            break
    dica = dica or _first_sentence(book.get('intro', ''), 95)

    title = f'{book["header_light"]} {book["header_bold"]}'.strip()
    html = (
        '<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>'
        + CSS.replace('__FF__', _font_face()).replace('__HEX__', _HEX) +
        '</style></head><body><div class="slide">'
        '<div class="head"><div class="htop">'
        '<span class="brand"><span class="seal"><svg viewBox="0 0 64 64" fill="none">' + ICONS['book'] + '</svg></span>MINUTO<b>REAL</b></span>'
        '<span class="maptag">Mapa do livro</span></div>'
        f'<div class="title">{title} — um guia de campo</div>'
        f'<div class="promise">{_first_sentence(book.get("intro",""), 80)}</div></div>'
        f'<div class="grid">{cols}</div>'
        f'<div class="foot"><span class="fi">{spark}</span>'
        f'<span class="ft"><b>Dica estratégica:</b> {dica}</span></div>'
        '<div class="hand">@minutoreal1701 · o livro inteiro em 1 página</div>'
        '</div></body></html>')

    out = OUT / slug; out.mkdir(parents=True, exist_ok=True)
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={'width': W, 'height': H}, device_scale_factor=2)
        pg.set_content(html, wait_until='networkidle')
        pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(400)
        fp = out / 'mapa.png'
        pg.query_selector('.slide').screenshot(path=str(fp))
        b.close()
    print('OK ->', fp)


if __name__ == '__main__':
    import re  # noqa
    a = [x for x in sys.argv[1:] if not x.startswith('--')]
    if not a:
        sys.exit('uso: python gerar_mapa.py <slug> [--no-img]')
    build(a[0], no_img='--no-img' in sys.argv)
