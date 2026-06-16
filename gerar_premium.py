# -*- coding: utf-8 -*-
"""Gerador PREMIUM de carrossel (1080x1350) — nivel das referencias do usuario
(u02/u03/u04): ILUSTRACAO cinematografica por IA (videos/imagen.py = Imagen 4.0)
+ COMPOSICAO da marca por cima (wordmark, titulo serifa, caixa de takeaway, cromo).

Obedece o contrato de usabilidade: texto enxuto (gc._lead), 1 so progresso (dots),
marca coesa, billboard. Cache das artes de IA em videos/_premium/<slug>/art_*.png
(nao regera se ja existe = controle de custo; a composicao e' refeita sempre).

  python gerar_premium.py <slug>            # capa + conceitos + CTA (premium)
  python gerar_premium.py <slug> --no-img   # so recompoe (usa arte em cache)
Saida: videos/_premium/<slug>/NN.png
"""
import sys, base64
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / 'videos'))
import gerar_carrossel as gc                      # _lead (orcamento de texto)
from gerar_infografico import _chapter_title, _chapter_num, _even_sample, _first_sentence

OUT = ROOT / 'videos' / '_premium'
FONTS = ROOT / '_fonts'
W, H = 1080, 1350

# estilo visual unico da marca (todo prompt termina com isto -> coesao entre pecas)
BASE_STYLE = (
    "deep emerald green and antique gold color palette, cinematic chiaroscuro lighting, "
    "painterly digital illustration, dramatic moody atmosphere, rich texture and detail, "
    "dark empty negative space for text, premium editorial book-summary art, masterpiece, "
    "absolutely no text of any kind, no words, no letters, no typography, no book titles, "
    "no signage, no nameplates, no captions, no watermark")


def _b64(p):
    return base64.b64encode(Path(p).read_bytes()).decode('ascii')


def _font_face():
    out = []
    for fam, fn in (('Hanken Grotesk', 'HankenGrotesk.ttf'), ('Literata', 'Literata.ttf')):
        p = FONTS / fn
        if p.exists():
            out.append(f"@font-face{{font-family:'{fam}';font-weight:100 900;font-display:block;"
                       f"src:url(data:font/ttf;base64,{_b64(p)}) format('truetype')}}")
    return '\n'.join(out)


def _art(slug, key, scene, no_img=False, aspect='3:4'):
    """Gera (ou reusa do cache) a ilustracao de IA p/ um slide."""
    d = OUT / slug
    d.mkdir(parents=True, exist_ok=True)
    p = d / f'art_{key}.png'
    if p.exists() or no_img:
        return p if p.exists() else None
    import imagen
    prompt = f'{scene}. {BASE_STYLE}'
    print(f'  [imagen] {key}: {scene[:60]}...')
    if not imagen.gen(prompt, str(p), aspect=aspect):
        return None
    return p


# ----------------------------- CROMO + CSS compartilhado -----------------------------
_ICON_BOOK = ('<svg viewBox="0 0 64 64" fill="none"><path d="M12 14h18a6 6 0 016 6v30a6 6 0 00-6-6H12z" '
              'stroke="currentColor" stroke-width="3" stroke-linejoin="round"/><path d="M52 14H34a6 6 0 00-6 6v30a6 6 0 016-6h18z" '
              'stroke="currentColor" stroke-width="3" stroke-linejoin="round"/></svg>')
_ICON_SPARK = ('<svg viewBox="0 0 64 64" fill="none"><path d="M32 10l5 17 17 5-17 5-5 17-5-17-17-5 17-5z" '
               'stroke="currentColor" stroke-width="3" stroke-linejoin="round"/></svg>')
_ICON_ARROW = ('<svg viewBox="0 0 64 64" fill="none"><path d="M12 32h36M34 18l16 14-16 14" '
               'stroke="currentColor" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/></svg>')
_ICON_BOOK_MARK = ('<svg viewBox="0 0 64 64" fill="none"><path d="M18 10h28v44L32 44 18 54z" '
                   'stroke="currentColor" stroke-width="3" stroke-linejoin="round"/></svg>')

BASE_CSS = """
__FF__
*{margin:0;padding:0;box-sizing:border-box}
.slide{width:1080px;height:1350px;position:relative;overflow:hidden;font-family:'Hanken Grotesk',sans-serif;background:#05070a;color:#f3f5f4}
.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.scrim{position:absolute;inset:0;background:
  linear-gradient(180deg, rgba(5,9,8,.80) 0%, rgba(5,9,8,.05) 25%, rgba(5,9,8,.02) 44%, rgba(5,9,8,.70) 72%, rgba(5,9,8,.95) 100%)}
.frame{position:absolute;inset:34px;border:2px dashed oklch(80% 0.12 152 / .42);border-radius:30px;pointer-events:none}
.wrap{position:absolute;inset:0;padding:74px 76px 70px;display:flex;flex-direction:column}
.top{display:flex;justify-content:space-between;align-items:center}
.brand{display:inline-flex;align-items:center;gap:12px;font-weight:900;letter-spacing:.04em;font-size:27px;text-transform:uppercase}
.brand .seal{width:46px;height:46px;border-radius:13px;display:flex;align-items:center;justify-content:center;background:oklch(72% 0.16 152);color:#06140d;box-shadow:0 8px 26px rgba(0,0,0,.5)}
.brand .seal svg{width:27px;height:27px}
.brand b{color:oklch(82% 0.14 152)}
.tag{font-weight:800;font-size:20px;letter-spacing:.14em;text-transform:uppercase;color:oklch(86% 0.10 152);border:1.5px solid oklch(80% 0.12 152 / .4);border-radius:999px;padding:9px 20px;background:rgba(8,20,14,.5)}
.spacer{flex:1 1 auto}
.src{font-family:'Literata',serif;font-weight:600;font-size:29px;color:oklch(88% 0.07 152);margin-bottom:8px;text-shadow:0 2px 16px rgba(0,0,0,.85)}
.src b{color:oklch(84% 0.13 152)}
h1{font-family:'Literata',serif;font-weight:600;line-height:.98;letter-spacing:-.01em;text-shadow:0 4px 30px rgba(0,0,0,.9)}
.cover h1{font-size:118px;font-weight:700;text-transform:uppercase;letter-spacing:-.02em;font-family:'Hanken Grotesk';line-height:.9}
.cover h1 .lt{color:oklch(84% 0.14 152)} .cover h1 .bd{color:#fff}
.concept h1{font-size:100px} .concept h1 .lt{color:#fff} .concept h1 .bd{color:oklch(84% 0.14 152);font-style:italic}
.cta h1{font-size:120px;font-weight:800;text-transform:uppercase;font-family:'Hanken Grotesk';line-height:.88}
.cta h1 .bd{color:oklch(84% 0.14 152)} .cta h1 .lt{color:#fff}
.take{margin-top:32px;display:flex;gap:22px;align-items:flex-start;border:1.5px solid oklch(80% 0.12 152 / .3);border-left:5px solid oklch(76% 0.105 83);border-radius:20px;padding:24px 30px;background:rgba(6,12,10,.62);box-shadow:0 18px 50px rgba(0,0,0,.5)}
.take .ic{flex:0 0 auto;width:58px;height:58px;border-radius:15px;display:flex;align-items:center;justify-content:center;background:oklch(76% 0.105 83);color:#1a1205}
.take .ic svg{width:36px;height:36px}
.take .lbl{font-weight:900;font-size:20px;letter-spacing:.18em;text-transform:uppercase;color:oklch(80% 0.10 83)}
.take p{font-size:28px;line-height:1.26;color:#eef2f0;font-weight:500;margin-top:5px}
.take p b{color:oklch(86% 0.12 152);font-weight:800}
.promise{font-size:30px;color:oklch(88% 0.06 152);font-weight:600;margin-top:14px;max-width:840px;text-shadow:0 2px 14px rgba(0,0,0,.8)}
.hook{margin-top:26px;display:inline-flex;align-items:center;gap:18px;font-size:54px;font-weight:900;text-transform:uppercase;color:#fff}
.hook .n{font-size:96px;color:oklch(80% 0.10 83);line-height:.8}
.swipe{margin-top:30px;align-self:flex-start;display:inline-flex;align-items:center;gap:16px;font-weight:800;font-size:30px;letter-spacing:.12em;text-transform:uppercase;color:#06140d;background:oklch(80% 0.14 152);padding:18px 40px;border-radius:999px;box-shadow:0 16px 44px oklch(50% 0.12 152 / .5)}
.swipe svg{width:34px;height:34px}
.rows{margin-top:8px;display:flex;flex-direction:column;gap:18px}
.row{display:flex;gap:18px;align-items:center;font-size:30px;font-weight:600;color:#eef2f0}
.row .ri{flex:0 0 auto;width:54px;height:54px;border-radius:14px;display:flex;align-items:center;justify-content:center;background:rgba(8,20,14,.6);border:1.5px solid oklch(80% 0.12 152 / .35);color:oklch(84% 0.13 152)}
.row .ri svg{width:30px;height:30px}
.row b{color:oklch(84% 0.13 152);font-weight:800}
.save{margin-top:30px;align-self:flex-start;display:inline-flex;align-items:center;gap:16px;font-weight:900;font-size:32px;letter-spacing:.06em;text-transform:uppercase;color:#06140d;background:oklch(80% 0.14 152);padding:20px 44px;border-radius:18px;box-shadow:0 16px 44px oklch(50% 0.12 152 / .5)}
.save svg{width:34px;height:34px}
.dots{display:flex;gap:12px;justify-content:center;margin-top:26px}
.dots i{width:11px;height:11px;border-radius:999px;background:oklch(80% 0.05 152 / .4)}
.dots i.on{width:36px;background:oklch(80% 0.14 152)}
.hand{text-align:center;font-weight:800;letter-spacing:.24em;font-size:18px;color:oklch(80% 0.04 152 / .8);text-transform:uppercase;margin-top:16px}
"""


def _brand(eyebrow):
    return (f'<div class="top"><span class="brand"><span class="seal">{_ICON_BOOK}</span>MINUTO<b>REAL</b></span>'
            f'<span class="tag">{eyebrow}</span></div>')


def _dots(pos, total):
    return '<div class="dots">' + ''.join(f'<i class="{"on" if k == pos else ""}"></i>' for k in range(total)) + '</div>'


def _doc(inner):
    return ('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>'
            + BASE_CSS.replace('__FF__', _font_face()) + '</style></head><body>' + inner + '</body></html>')


def _slide(cls, art, body):
    bg = f'<img class="bg" src="data:image/png;base64,{_b64(art)}">' if art else ''
    return (f'<div class="slide {cls}">{bg}<div class="scrim"></div><div class="frame"></div>'
            f'<div class="wrap">{body}</div></div>')


# ----------------------------- layouts -----------------------------
def cover_html(book, art, n_ideias, total):
    return _slide('cover', art,
        _brand(' · '.join(book.get('tags', [])[:2]).upper() or 'Resumo')
        + '<div class="spacer"></div>'
        + f'<h1><span class="lt">{book["header_light"]}</span> <span class="bd">{book["header_bold"]}</span></h1>'
        + f'<div class="promise">{_first_sentence(book.get("intro", ""), 130)}</div>'
        + f'<div class="hook"><span class="n">{n_ideias}</span>ideias que ficam</div>'
        + f'<div class="swipe">arrasta {_ICON_ARROW}</div>'
        + _dots(0, total))


def concept_html(book, ch, art, pos, total):
    num = _chapter_num(ch)
    src = f'Capítulo {int(num)} · <b>{_chapter_title(ch)}</b>' if num else f'<b>{_chapter_title(ch)}</b>'
    title = _chapter_title(ch)
    # takeaway: melhor tip do capitulo, enxuto
    tip = ''
    for c in ch.get('cards', []):
        if c.get('tip'):
            tip = gc._lead(__import__('re').sub(r'^<strong>.*?</strong>\s*', '', c['tip']), max_sent=2, cap=150)
            break
    if not tip:
        tip = gc._lead(ch.get('intro', ''), max_sent=2, cap=150)
    return _slide('concept', art,
        _brand(f'{book["header_light"]} {book["header_bold"]}'.strip())
        + '<div class="spacer"></div>'
        + f'<div class="src">{src}</div>'
        + f'<h1><span class="lt">{title}</span></h1>'
        + f'<div class="take"><span class="ic">{_ICON_SPARK}</span><div>'
        + f'<div class="lbl">Modelo mental</div><p>{tip}</p></div></div>'
        + _dots(pos, total))


def cta_html(book, art, total):
    return _slide('cta', art,
        _brand('Minuto Real') + '<div class="spacer"></div>'
        + '<h1><span class="lt">Gostou?</span> <span class="bd">tem mais.</span></h1>'
        + '<div class="rows" style="margin-top:30px">'
        + f'<div class="row"><span class="ri">{_ICON_BOOK_MARK}</span>O livro inteiro em 1 página — <b>no acervo</b></div>'
        + f'<div class="row"><span class="ri">{_ICON_SPARK}</span>Resumo de ~5 min <b>no YouTube</b></div>'
        + '</div>'
        + f'<div class="save">{_ICON_BOOK_MARK} Salve para revisar</div>'
        + _dots(total - 1, total)
        + '<div class="hand">@minutoreal1701 · link na bio</div>')


def build(slug, no_img=False):
    data = __import__(slug.replace('-', '_') + '_data')
    book = data.BOOK
    chaps = _even_sample(getattr(data, 'CHAPTERS', []), 4)
    total = 1 + len(chaps) + 1                       # capa + conceitos + cta
    out = OUT / slug
    out.mkdir(parents=True, exist_ok=True)

    slides = []
    # capa — cena TEMATICA (nunca o titulo do livro no prompt: isso faz a IA cravar texto borrado)
    _theme = ', '.join(book.get('tags', [])[:3]) or 'wisdom, insight, transformation'
    art = _art(slug, 'cover', f"a grand cinematic atmospheric establishing scene evoking the themes of {_theme}", no_img)
    slides.append(cover_html(book, art, len(chaps), total))
    # conceitos
    for i, ch in enumerate(chaps, 1):
        sc = (f"a cinematic symbolic painterly scene evoking the concept of {_chapter_title(ch)}, "
              "told purely through imagery, objects, figures and symbolism")
        art = _art(slug, f'c{i}', sc, no_img)
        slides.append(concept_html(book, ch, art, i, total))
    # cta
    art = _art(slug, 'cta', "an atmospheric cinematic still life of an open antique book glowing with emerald-green light, floating dust, dark background", no_img)
    slides.append(cta_html(book, art, total))

    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={'width': W, 'height': H}, device_scale_factor=2)
        for i, html in enumerate(slides, 1):
            pg.set_content(_doc(html), wait_until='networkidle')
            pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(350)
            fp = out / f'{i:02d}.png'
            pg.query_selector('.slide').screenshot(path=str(fp))
            print('OK ->', fp)
        b.close()


if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if not x.startswith('--')]
    if not a:
        sys.exit('uso: python gerar_premium.py <slug> [--no-img]')
    build(a[0], no_img='--no-img' in sys.argv)
