# -*- coding: utf-8 -*-
"""Emite os TEMPLATES HTML do Kit de Divulgação (peças estáticas) por livro,
na MESMA linguagem editorial quente do carrossel (zero deriva — reusa gerar_carrossel).

O server.js (KIT_TPL) fotografa cada um sob demanda (png+webp), cacheia e serve:
  assets/kit/_tpl/<slug>/ideia.html        1080×1080  ideia-chave (1:1, feed)
  assets/kit/_tpl/<slug>/quote.html        1080×1350  citação (4:5, feed)
  assets/kit/_tpl/<slug>/quote-story.html  1080×1920  citação (9:16, story)
  assets/kit/_tpl/<slug>/capa-story.html   1080×1920  capa (9:16, story)

Uso:
  python gerar_dados_kit.py <slug>          emite os _tpl de um livro
  python gerar_dados_kit.py --all           todos os livros com _data.py
  python gerar_dados_kit.py --proof <slug>  renderiza PNGs locais p/ conferência (sem deploy)
"""
import importlib, json, sys, os, re, glob
from pathlib import Path
import gerar_carrossel as gc

BASE = Path(__file__).parent
TPL = BASE / 'assets' / 'kit' / '_tpl'

# CSS extra das peças estáticas (override de tamanho do .slide; reusa todo o resto). ----
IDEIA_CSS = """
.slide.ideia{height:1080px;padding:88px 92px 96px}
.slide.ideia .ed{margin-top:18px}
.slide.ideia .ed-title{font-size:72px;margin:16px 0 4px}
.slide.ideia .ed-body{font-size:40px;line-height:1.46;margin-top:26px;padding-top:30px}
.slide.ideia .ed-body .dc{font-size:118px}
.slide.ideia .handle{position:absolute;bottom:54px;left:0;right:0;text-align:center;
  font-weight:600;font-size:24px;letter-spacing:.04em;color:var(--ink-dim)}
.slide.ideia .idtag{font-weight:900;font-size:19px;letter-spacing:.28em;text-transform:uppercase;color:var(--green)}
"""


def _page(fragment, w, h, css_extra=''):
    """Página HTML autônoma (fontes + tokens + CSS do carrossel + extra) que o
    server fotografa no viewport w×h. Uma só .slide/.story dentro."""
    return (
        '<!DOCTYPE html><html lang="pt-BR"><head><meta charset="UTF-8">'
        '<title>kit · minuto real</title>'
        f'<style>{gc.CSS}{css_extra}</style></head>'
        f'<body style="width:{w}px;height:{h}px">{fragment}</body></html>')


def _pick_idea(book, data):
    """A carta mais forte p/ virar 'ideia-chave': prefere overview_cards; dentro
    delas, a que tem tip + maior corpo (mais profunda)."""
    cards = book.get('overview_cards') or (data.CHAPTERS[0]['cards'] if data.CHAPTERS else [])
    if not cards:
        return None
    return max(cards, key=lambda c: (1 if c.get('tip') else 0, len(c.get('b', ''))))


def _ideia_fragment(book, card):
    kicker = f"{book.get('header_light','')} {book.get('header_bold','')}".strip() or 'MINUTO REAL'
    body = card['b']
    mdc = re.match(r'^(\s*(?:<[^>]+>)*)([A-Za-zÀ-ÿ])(.*)$', body, re.DOTALL)
    body_html = (mdc.group(1) + f'<span class="dc">{mdc.group(2)}</span>' + mdc.group(3)) if mdc else body
    tip_html = ''
    if card.get('tip'):
        mt = re.match(r'\s*<strong>(.*?)</strong>\s*(.*)', card['tip'], re.DOTALL)
        label, tipbody = (re.sub(r'[:：]\s*$', '', mt.group(1)).strip(), mt.group(2).strip()) if mt else ('Dica', card['tip'])
        tip_html = (f'<div class="ed-tip"><span class="tipic">{gc._svg("spark")}</span>'
                    f'<div class="tiptext"><div class="tiplabel">{label}</div>'
                    f'<div class="tipbody">{tipbody}</div></div></div>')
    inner = (
        '<div class="topbar"><span class="brandmark">'
        f'<span class="seal">{gc._svg("book")}</span>Minuto<b>Real</b></span>'
        '<span class="idtag">Ideia-chave</span></div>'
        '<div class="ed">'
        f'<div class="ed-kicker">{kicker}</div><div class="ed-rule"></div>'
        f'<h1 class="ed-title">{gc._ed_title(card["t"], card.get("emph"))}</h1>'
        f'<p class="ed-body">{body_html}</p>{tip_html}</div>'
        '<div class="handle">andregalgani.com.br/biblioteca</div>')
    return f'<div class="slide ideia">{inner}</div>'


def emit(slug):
    data = importlib.import_module(slug.replace('-', '_') + '_data')
    book = getattr(data, 'BOOK', None) or _books_json().get(slug, {})
    out = TPL / slug
    out.mkdir(parents=True, exist_ok=True)
    pages = {}
    # ideia-chave 1:1
    idea = _pick_idea(book, data)
    if idea:
        pages['ideia.html'] = _page(_ideia_fragment(book, idea), 1080, 1080, IDEIA_CSS)
    # citação 4:5 (reusa _quote_card; já é quente)
    quotes = gc._best_quotes(slug, book, data, want=1)
    if quotes:
        pages['quote.html'] = _page(gc._quote_card(quotes[0], book, 1, 1), 1080, 1350)
    for name, html in pages.items():
        (out / name).write_text(html, encoding='utf-8', newline='\n')
    return list(pages)


_BJ = None
def _books_json():
    global _BJ
    if _BJ is None:
        _BJ = {b['id']: b for b in json.load(open(BASE / 'books.json', encoding='utf-8'))}
    return _BJ


def proof(slug):
    """Renderiza os _tpl do livro em PNG local p/ conferência visual (playwright)."""
    names = emit(slug)
    out = BASE / '_kit_preview' / '_qc_kit' / slug
    out.mkdir(parents=True, exist_ok=True)
    from playwright.sync_api import sync_playwright
    sizes = {'ideia.html': (1080, 1080), 'quote.html': (1080, 1350),
             'quote-story.html': (1080, 1920), 'capa-story.html': (1080, 1920)}
    made = []
    with sync_playwright() as p:
        b = p.chromium.launch()
        for name in names:
            w, h = sizes[name]
            pg = b.new_page(viewport={'width': w, 'height': h}, device_scale_factor=2)
            pg.goto((TPL / slug / name).as_uri(), wait_until='networkidle')
            pg.wait_for_timeout(500)
            png = out / name.replace('.html', '.png')
            pg.locator('.slide, .story').first.screenshot(path=str(png))
            made.append(png); pg.close()
        b.close()
    print('proof:', ', '.join(str(m) for m in made))


def main():
    args = sys.argv[1:]
    if args and args[0] == '--proof':
        proof(args[1]); return
    TPL.mkdir(parents=True, exist_ok=True)
    if args and args[0] != '--all':
        slugs = [args[0]]
    else:
        slugs = [os.path.basename(f)[:-8].replace('_', '-') for f in glob.glob(str(BASE / '*_data.py'))]
    ok = err = 0
    for slug in slugs:
        try:
            emit(slug); ok += 1
        except Exception as e:
            print(f'FAIL {slug}: {e}'); err += 1
    print(f'{ok} livros com _tpl emitido ({err} falhas)')


if __name__ == '__main__':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    main()
