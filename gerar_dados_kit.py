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
import gerar_infografico as gi
import tokens

BASE = Path(__file__).parent
TPL = BASE / 'assets' / 'kit' / '_tpl'

# CSS do MAPA (infográfico LISTA): fontes via @import (não base64) p/ o server. ----
MAPA_CSS = tokens.FONTS + gi.BASE_CSS.replace('__FONT_FACE__', '') + gi.ARCH_CSS['lista']

# CSS da thumbnail do YouTube (16:9, alto contraste, legível em miniatura). ----
THUMB_CSS = tokens.TOKENS + """
*{margin:0;padding:0;box-sizing:border-box}
body{background:#000;font-family:'Hanken Grotesk',system-ui,sans-serif;-webkit-font-smoothing:antialiased}
.thumb{width:1280px;height:720px;color:var(--ink);padding:70px 84px;display:flex;flex-direction:column;
  justify-content:space-between;position:relative;overflow:hidden;
  background:
   radial-gradient(120% 95% at 104% 110%, oklch(26% 0.05 152 / .9) 0%, transparent 46%),
   radial-gradient(110% 70% at 0% -10%, oklch(27% 0.05 152) 0%, transparent 58%),
   linear-gradient(165deg, var(--bg) 0%, var(--bg2) 100%);}
.thumb::after{content:'';position:absolute;inset:30px;border:2px dashed var(--green);border-radius:28px;opacity:.34;pointer-events:none}
.thumb>*{position:relative;z-index:1}
.thumb .ghost{position:absolute;right:30px;bottom:-90px;font-weight:900;font-size:520px;line-height:.7;
  color:transparent;-webkit-text-stroke:2px oklch(74% 0.09 152 / .12);z-index:0;letter-spacing:-.05em}
.thumb .top{display:inline-flex;align-items:center;gap:14px;font-weight:900;font-size:30px;
  letter-spacing:.04em;text-transform:uppercase}
.thumb .top .seal{width:50px;height:50px;border-radius:14px;display:flex;align-items:center;justify-content:center;
  background:var(--green);color:var(--on-green);box-shadow:0 8px 22px oklch(60% 0.14 152 / .4)}
.thumb .top .seal svg{width:30px;height:30px;color:var(--on-green)} .thumb .top b{color:var(--green)}
.thumb .eyebrow{font-weight:800;font-size:30px;letter-spacing:.22em;text-transform:uppercase;color:var(--green);margin-bottom:14px}
.thumb h1{font-weight:900;font-size:118px;line-height:.9;text-transform:uppercase;letter-spacing:-.022em;text-wrap:balance;max-width:1040px}
.thumb h1 .lt{color:var(--green);text-shadow:0 0 60px oklch(72% 0.14 152 / .4)} .thumb h1 .bd{color:var(--ink)}
.thumb .foot{display:flex;align-items:center;gap:24px}
.thumb .foot .num{font-weight:900;font-size:96px;line-height:.8;color:var(--gold);text-shadow:0 0 50px oklch(84% 0.12 83 / .4)}
.thumb .foot .lbl{font-weight:800;font-size:44px;line-height:1.02;color:var(--ink);text-transform:uppercase}
"""

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

# Auto-fit (equivalente ao de gerar_carrossel._render / gerar_infografico): encolhe a
# fonte ate o titulo caber na caixa. Cobre .head h1 (mapa), .ed-title (ideia) e .fitv
# (mapa), + .thumb h1 (titulo longo na thumb 16:9). Roda apos document.fonts.ready.
_FIT_JS = """() => {
  for (const el of document.querySelectorAll('.head h1, .ed-title, .thumb h1')) {
    const box = el.parentElement, cs = getComputedStyle(box);
    const avail = box.clientWidth - parseFloat(cs.paddingLeft) - parseFloat(cs.paddingRight);
    let fs = parseFloat(getComputedStyle(el).fontSize), g = 0;
    while (el.scrollWidth > avail && fs > 40 && g < 120){ fs -= 3; el.style.fontSize = fs+'px'; g++; }
  }
  for (const el of document.querySelectorAll('.fitv')) {
    let fs = parseFloat(getComputedStyle(el).fontSize), g = 0;
    while (el.scrollHeight > el.clientHeight + 1 && fs > 24 && g < 60){ fs -= 1; el.style.fontSize = fs+'px'; g++; }
  }
}"""


def _page(fragment, w, h, css_extra='', css=None):
    """Página HTML autônoma (fontes + tokens + CSS + extra) que o server
    fotografa no viewport w×h. Uma só .slide/.story dentro."""
    return (
        '<!DOCTYPE html><html lang="pt-BR"><head><meta charset="UTF-8">'
        '<title>kit · minuto real</title>'
        f'<style>{css or gc.CSS}{css_extra}</style></head>'
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
    body = gc._lead(card['b'])  # orcamento Krug: cartaz, nao paragrafo (reusa o do carrossel)
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


def _resolve_book(slug, data):
    """Dict do livro robusto: BOOK do _data.py + campos do books.json; deriva
    header_light/header_bold a partir do título quando faltam."""
    book = dict(getattr(data, 'BOOK', None) or {})
    for k, v in (_books_json().get(slug) or {}).items():
        book.setdefault(k, v)
    if not book.get('header_light'):
        words = (book.get('title') or slug.replace('-', ' ')).split()
        cut = (len(words) + 1) // 2
        book['header_light'] = ' '.join(words[:cut])
        book['header_bold'] = ' '.join(words[cut:]) or book['header_light']
    book.setdefault('author', '—')
    book.setdefault('title', book['header_light'])
    return book


def _thumb_fragment(book, data):
    n = len(book.get('overview_cards') or []) or sum(len(ch.get('cards', [])) for ch in data.CHAPTERS)
    return (
        f'<div class="thumb"><div class="ghost">{n}</div>'
        f'<div class="top"><span class="seal">{gc._svg("book")}</span>Minuto<b>Real</b></div>'
        '<div><div class="eyebrow">o livro em ~5 min</div>'
        f'<h1><span class="lt">{book["header_light"]}</span> <span class="bd">{book["header_bold"]}</span></h1></div>'
        f'<div class="foot"><span class="num">{n}</span>'
        '<span class="lbl">ideias</span></div></div>')


def emit(slug):
    data = importlib.import_module(slug.replace('-', '_') + '_data')
    book = _resolve_book(slug, data)
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
        # citação 9:16 (story) — mesma frase, layout vertical
        pages['quote-story.html'] = _page(gc._story_quote(quotes[0], book), 1080, 1920, css=gc.STORY_CSS)
    # capa 9:16 (story) — anúncio do livro com nº de ideias
    n = len(book.get('overview_cards') or []) or sum(len(ch.get('cards', [])) for ch in data.CHAPTERS)
    pages['capa-story.html'] = _page(gc._story_teaser(book, n), 1080, 1920, css=gc.STORY_CSS)
    # insights 9:16 (story) — 3 lições-chave: 1ª lição de cada capítulo (max 3)
    _lessons = []
    for chap in getattr(data, 'CHAPTERS', []) or []:
        ls = chap.get('lessons', [])
        if ls:
            _lessons.append(ls[0])
        if len(_lessons) >= 3:
            break
    if _lessons:
        pages['insights-story.html'] = _page(
            gc._story_insights(book, _lessons, 'O que você vai levar'),
            1080, 1920, css=gc.STORY_CSS)
    # MAPA DO LIVRO 4:5 (infográfico LISTA, universal) — só se houver BOOK+CHAPTERS
    try:
        frag = gi.build_lista(data)
        if frag:
            pages['mapa.html'] = _page(frag, 1080, 1350, css=MAPA_CSS)
    except Exception as e:
        print(f'  [mapa pulado] {slug}: {e}')
    # thumbnail YouTube 16:9
    pages['thumb.html'] = _page(_thumb_fragment(book, data), 1280, 720, css=THUMB_CSS)
    for name, html in pages.items():
        (out / name).write_text(html, encoding='utf-8', newline='\n')
    _write_manifest(slug, book, pages)
    return list(pages)


# tipo de peça → metadados p/ a pílula da UI (id casa com KIT_TPL no server.js)
ASSET_META = {
    'ideia':         {'tpl': 'ideia.html',       'icon': 'idea',   'label': 'Ideia-chave',        'rede': 'Instagram', 'fmt': '1:1'},
    'mapa':          {'tpl': 'mapa.html',        'icon': 'idea',   'label': 'Mapa do livro',      'rede': 'Instagram', 'fmt': '4:5'},
    'citacao-feed':  {'tpl': 'quote.html',       'icon': 'quote',  'label': 'Citação (feed)',     'rede': 'Instagram', 'fmt': '4:5'},
    'citacao-story': {'tpl': 'quote-story.html', 'icon': 'quote',  'label': 'Citação (story)',    'rede': 'Stories',   'fmt': '9:16'},
    'capa-story':    {'tpl': 'capa-story.html',    'icon': 'cover',  'label': 'Capa (story)',        'rede': 'Stories',   'fmt': '9:16'},
    'insights-story':{'tpl': 'insights-story.html','icon': 'idea',   'label': 'Insights (story)',    'rede': 'Stories',   'fmt': '9:16'},
    'thumb':         {'tpl': 'thumb.html',         'icon': 'cover',  'label': 'Thumbnail YouTube',   'rede': 'YouTube',   'fmt': '16:9'},
}
# ordem de exibição na UI (carrossel do livro entra primeiro, à parte)
ASSET_ORDER = ['mapa', 'ideia', 'citacao-feed', 'citacao-story', 'capa-story', 'insights-story', 'thumb']


def _write_manifest(slug, book, pages):
    """manifest.json do kit do LIVRO (lido pela página de visão geral). Lista o
    carrossel do livro (tipo carousel) + as peças estáticas geradas (tipo image)."""
    tpls = set(pages)
    assets = [{'id': 'overview', 'type': 'carousel', 'icon': 'carousel',
               'label': 'Carrossel do livro', 'rede': 'Instagram', 'fmt': '4:5',
               'pill': 'IG · carrossel · 4:5'}]
    for fid in ASSET_ORDER:
        m = ASSET_META[fid]
        if m['tpl'] not in tpls:
            continue
        assets.append({'id': fid, 'type': 'image', 'icon': m['icon'], 'label': m['label'],
                       'rede': m['rede'], 'fmt': m['fmt'], 'pill': f"{m['rede']} · {m['fmt']}"})
    manifest = {
        'title': 'Kit de Divulgação', 'ondemand': True,
        'intro': 'Peças no padrão da Biblioteca, geradas na hora. Gerar conta como um curtir — '
                 'os livros mais pedidos entram na esteira de produção.',
        'assets': assets,
    }
    (BASE / 'assets' / 'kit' / slug).mkdir(parents=True, exist_ok=True)
    (BASE / 'assets' / 'kit' / slug / 'manifest.json').write_text(
        json.dumps(manifest, ensure_ascii=False), encoding='utf-8', newline='\n')


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
             'quote-story.html': (1080, 1920), 'capa-story.html': (1080, 1920),
             'insights-story.html': (1080, 1920),
             'mapa.html': (1080, 1350), 'thumb.html': (1280, 720)}
    made = []
    with sync_playwright() as p:
        b = p.chromium.launch()
        for name in names:
            w, h = sizes[name]
            pg = b.new_page(viewport={'width': w, 'height': h}, device_scale_factor=2)
            pg.goto((TPL / slug / name).as_uri(), wait_until='networkidle')
            pg.evaluate('document.fonts.ready')
            pg.wait_for_timeout(500)
            pg.evaluate(_FIT_JS)
            png = out / name.replace('.html', '.png')
            pg.locator('.slide, .story, .thumb').first.screenshot(path=str(png))
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
        slugs = [b['id'] for b in _books_json().values()
                 if os.path.exists(BASE / (b['id'].replace('-', '_') + '_data.py'))]
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
