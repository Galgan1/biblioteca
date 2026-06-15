# -*- coding: utf-8 -*-
"""Gerador de INFOGRAFICOS densos para o Instagram (1080x1350) — "muita informacao
organizada numa imagem, com estilo, elegancia e ilustracoes" dentro da marca do canal.

Cinco arquetipos (a "alma" de posts-cheat-sheet, traduzida p/ a nossa marca:
verde-lidera + 1 ouro, sem arco-iris; cor nunca e' o unico sinal):

  LISTA     — "Mapa do livro": um no por capitulo. UNIVERSAL (sai de qualquer livro).
  FLUXO     — linha do tempo / passos de um processo.        curado (campo FLUXO)
  COMPARA   — duas colunas X x Y / quadrante.                curado (campo COMPARA)
  NUMEROS   — numeros-heroi + mini-viz on-brand.             curado (campo NUMEROS)
  ANATOMIA  — ilustracao de linha com callouts.              curado (campo ANATOMIA)

Os 4 curados leem um dict opcional no <slug>_data.py; se ausente, o arquetipo e'
pulado. A LISTA sai sempre, dos CHAPTERS. Cada arquetipo e' renderizado numa
pagina ISOLADA (BASE_CSS + so o CSS dele), entao nao ha vazamento de estilo.

  python gerar_infografico.py <slug>              # todos os arquetipos disponiveis
  python gerar_infografico.py <slug> lista fluxo  # so os pedidos
Saida: videos/_infograficos/<slug>/<arquetipo>.png  (regeneravel, fora do git)
"""
import sys, re, base64, importlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from gerar_livro import ICONS
try:
    from gerar_carrossel import _EXTRA          # icones extra (arrow, shield, ...)
except Exception:
    _EXTRA = {}

OUTBASE = ROOT / 'videos' / '_infograficos'
FONTS = ROOT / '_fonts'
W, H = 1080, 1350

try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass


# ============================ CROMO DE MARCA (compartilhado) ============================
def _font_face():
    faces = []
    for fam, fn in (('Hanken Grotesk', 'HankenGrotesk.ttf'), ('Literata', 'Literata.ttf')):
        p = FONTS / fn
        if not p.exists():
            continue
        b64 = base64.b64encode(p.read_bytes()).decode('ascii')
        faces.append(f"@font-face{{font-family:'{fam}';font-weight:100 900;font-display:block;"
                     f"src:url(data:font/ttf;base64,{b64}) format('truetype')}}")
    return '\n'.join(faces)


def _svg(name):
    inner = ICONS.get(name) or _EXTRA.get(name) or ICONS['book']
    return (f'<svg viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">{inner}</svg>')


# esqueleto comum a TODOS os arquetipos: tokens, base do slide (profundidade em
# camadas + moldura tracejada + grade de pontos), brandmark e ghost. Tudo o mais
# (cabecalho/rodape/conteudo) vive no CSS de cada arquetipo, p/ nao colidir.
BASE_CSS = """
__FONT_FACE__
:root{
  --green: oklch(70% 0.13 152); --green-soft: oklch(85% 0.105 152); --green-deep: oklch(56% 0.14 152);
  --ink: oklch(98% 0.008 152); --muted: oklch(75% 0.022 152); --ink-dim: oklch(64% 0.02 152);
  --bg: oklch(14.5% 0.014 152); --bg2: oklch(10.5% 0.012 152); --on-green: oklch(13% 0.02 152);
  --gold: oklch(76% 0.105 83); --on-gold: oklch(20% 0.04 83);
  --warn: oklch(72% 0.15 40); --hair: oklch(73% 0.05 152 / .30); --hair2: oklch(73% 0.05 152 / .14);
}
*{margin:0;padding:0;box-sizing:border-box}
body{background:#000;font-family:'Hanken Grotesk',system-ui,sans-serif;
  -webkit-font-smoothing:antialiased;text-rendering:geometricPrecision}
.slide{width:1080px;height:1350px;color:var(--ink);padding:70px 76px 50px;
  display:flex;flex-direction:column;position:relative;overflow:hidden;
  background:
   radial-gradient(135% 95% at 102% 108%, oklch(24% 0.045 152 / .85) 0%, transparent 48%),
   radial-gradient(115% 72% at 50% -12%, oklch(27% 0.05 152) 0%, transparent 60%),
   radial-gradient(150% 125% at 50% 48%, transparent 52%, oklch(5% 0.012 152 / .6) 100%),
   linear-gradient(177deg, var(--bg) 0%, var(--bg2) 100%);}
.slide::before{content:'';position:absolute;inset:0;pointer-events:none;
  background-image:radial-gradient(oklch(78% 0.07 152 / .055) 1.1px, transparent 1.3px);
  background-size:36px 36px;background-position:center;
  -webkit-mask-image:radial-gradient(125% 105% at 50% -5%, #000 50%, transparent 100%);}
.slide::after{content:'';position:absolute;inset:38px;border:2px dashed var(--green);
  border-radius:32px;opacity:.38;pointer-events:none;box-shadow:inset 0 0 90px oklch(70% 0.13 152 / .05)}
.slide>*{position:relative;z-index:1}
.slide>.ghost{position:absolute;font-family:'Hanken Grotesk';font-weight:900;line-height:.74;
  color:transparent;-webkit-text-stroke:2px oklch(74% 0.09 152 / .09);pointer-events:none;
  letter-spacing:-.05em;z-index:0;overflow:hidden;
  -webkit-mask-image:radial-gradient(120% 120% at 50% 50%, #000 60%, transparent 100%)}
.brandmark{display:inline-flex;align-items:center;gap:11px;font-weight:900;
  letter-spacing:.03em;font-size:25px;color:var(--ink);text-transform:uppercase}
.brandmark .seal{width:42px;height:42px;border-radius:12px;display:flex;align-items:center;
  justify-content:center;background:var(--green);color:var(--on-green);flex:0 0 auto;
  box-shadow:0 8px 22px oklch(60% 0.14 152 / .35)}
.brandmark .seal svg{width:25px;height:25px;color:var(--on-green)}
.brandmark b{color:var(--green);font-weight:900}
"""

ARCH_CSS = {}  # nome -> CSS especifico (concatenado ao BASE_CSS na pagina isolada)


# ============================ helpers de conteudo ============================
def _clean(s):
    return re.sub(r'\s+', ' ', (s or '')).strip()


def _first_sentence(html, cap=150):
    """Primeira oracao (mantem <strong>), com teto de tamanho."""
    s = _clean(html)
    m = re.search(r'(?<=[.!?]) ', s)
    if m:
        s = s[:m.start() + 1]
    if len(s) > cap:
        cut = s[:cap].rsplit(' ', 1)[0]
        if cut.count('<strong>') > cut.count('</strong>'):
            cut += '</strong>'
        s = cut.rstrip(' .,;:') + '…'
    return s


def _chapter_title(ch):
    sub = _clean(ch.get('sub', ''))
    return sub.split(': ', 1)[1] if ': ' in sub else sub


def _chapter_num(ch):
    m = re.search(r'(\d+)', ch.get('sub', '') or ch.get('slug', ''))
    return f"{int(m.group(1)):02d}" if m else ''


def _even_sample(seq, k):
    n = len(seq)
    if n <= k:
        return list(seq)
    idx = [round(i * (n - 1) / (k - 1)) for i in range(k)]
    return [seq[i] for i in sorted(set(idx))]


def _load(slug):
    return importlib.import_module(slug.replace('-', '_') + '_data')


def _brand(badge_html):
    return ('<div class="top">'
            f'<span class="brandmark"><span class="seal">{_svg("book")}</span>Minuto<b>Real</b></span>'
            f'{badge_html}</div>')


# ============================ ARQUETIPO: LISTA (universal) ============================
ARCH_CSS['lista'] = """
.head{flex:0 0 auto}
.head .top{display:flex;justify-content:space-between;align-items:center}
.head .badge{font-weight:800;font-size:20px;letter-spacing:.12em;color:var(--green-soft);
  text-transform:uppercase;border:1.5px solid var(--hair);border-radius:999px;
  padding:9px 20px;background:oklch(70% 0.14 152 / .06);white-space:nowrap}
.head h1{font-size:78px;line-height:.92;font-weight:900;text-transform:uppercase;
  margin:26px 0 0;letter-spacing:-.022em;text-wrap:balance}
.head h1 .lt{color:var(--green);text-shadow:0 0 50px oklch(72% 0.14 152 / .38)}
.head h1 .bd{color:var(--ink)}
.head .promise{font-size:30px;line-height:1.24;color:var(--muted);font-weight:600;
  margin-top:16px;max-width:880px;text-wrap:pretty}
.head .promise strong{color:var(--green-soft);font-weight:800}
.head .rule{margin-top:24px;border-top:2px dashed var(--green);opacity:.55}
.rows{flex:1 1 auto;display:flex;flex-direction:column;justify-content:space-between;padding:26px 0 4px;font-size:40px}
.row{display:grid;grid-template-columns:auto 1fr auto;align-items:center;column-gap:28px;padding:6px 0}
.row .seal{width:84px;height:84px;border-radius:22px;display:flex;align-items:center;justify-content:center;
  flex:0 0 auto;background:linear-gradient(160deg, oklch(70% 0.14 152 / .16), oklch(70% 0.14 152 / .04));
  border:2px solid var(--hair);box-shadow:0 0 34px oklch(70% 0.14 152 / .12), inset 0 1px 0 oklch(90% 0.1 152 / .12)}
.row .seal svg{width:46px;height:46px;filter:drop-shadow(0 0 9px oklch(72% 0.14 152 / .4))}
.row .txt{min-width:0}
.row .lbl{font-size:.97em;line-height:1.04;font-weight:900;text-transform:uppercase;letter-spacing:.002em;text-wrap:balance}
.row .sub{font-size:.65em;line-height:1.26;color:var(--muted);font-weight:500;margin-top:7px;text-wrap:pretty}
.row .sub strong{font-weight:800}
.row .chip{flex:0 0 auto;justify-self:end;align-self:center;font-weight:900;font-size:21px;letter-spacing:.02em;
  text-transform:uppercase;white-space:nowrap;padding:11px 17px;border-radius:13px;text-align:center;line-height:1}
.row .chip .big{display:block;font-size:33px;line-height:.92}
.row.deep .seal svg{color:var(--green-deep)} .row.deep .lbl{color:var(--green-deep)} .row.deep .sub strong{color:var(--green-deep)}
.row.mid  .seal svg{color:var(--green)}      .row.mid .lbl{color:var(--green)}      .row.mid .sub strong{color:var(--green)}
.row.soft .seal svg{color:var(--green-soft)} .row.soft .lbl{color:var(--green-soft)} .row.soft .sub strong{color:var(--green-soft)}
.row.gold .seal{background:linear-gradient(160deg, oklch(76% 0.11 83 / .18), oklch(76% 0.11 83 / .04));
  border-color:oklch(76% 0.11 83 / .45);box-shadow:0 0 38px oklch(76% 0.11 83 / .16)}
.row.gold .seal svg{color:var(--gold);filter:drop-shadow(0 0 10px oklch(80% 0.1 83 / .5))}
.row.gold .lbl{color:var(--gold)} .row.gold .sub strong{color:var(--gold)}
.chip.g{background:oklch(70% 0.14 152 / .14);color:var(--green-soft);border:1.5px solid var(--hair)} .chip.g .big{color:var(--green)}
.chip.au{background:var(--gold);color:var(--on-gold);box-shadow:0 8px 22px oklch(70% 0.1 83 / .3)} .chip.au .big{color:var(--on-gold)}
.divider{height:2px;background:repeating-linear-gradient(90deg,var(--hair2) 0 14px,transparent 14px 26px);margin:2px 0}
.foot{flex:0 0 auto;display:flex;align-items:center;gap:22px;margin-top:18px;
  border:2px solid var(--hair);border-radius:22px;padding:22px 28px;
  background:linear-gradient(160deg, oklch(70% 0.14 152 / .10), oklch(70% 0.14 152 / .02))}
.foot .ic{flex:0 0 auto;width:62px;height:62px;border-radius:17px;display:flex;align-items:center;
  justify-content:center;background:var(--green);color:var(--on-green);box-shadow:0 10px 26px oklch(60% 0.14 152 / .38)}
.foot .ic svg{width:38px;height:38px;color:var(--on-green)}
.foot .body{min-width:0}
.foot .kick{font-size:21px;font-weight:900;letter-spacing:.18em;text-transform:uppercase;color:var(--green);display:block}
.foot .tactic{font-size:27px;line-height:1.22;color:var(--ink);font-weight:600;margin-top:5px;text-wrap:pretty}
.foot .tactic strong{color:var(--green-soft);font-weight:800}
.wm{text-align:center;font-weight:800;letter-spacing:.24em;font-size:18px;
  color:var(--ink-dim);text-transform:uppercase;margin-top:13px;flex:0 0 auto}
"""


def build_lista(data):
    book = data.BOOK
    chaps = _even_sample(getattr(data, 'CHAPTERS', []), 6)
    if not chaps:
        return None
    cycle = ['soft', 'mid', 'deep']
    rows = []
    for i, ch in enumerate(chaps):
        tone = 'gold' if i == len(chaps) - 1 else cycle[i % 3]
        ic = (ch.get('cards') or [{}])[0].get('ic', 'book')
        num = _chapter_num(ch)
        chip = ''
        if num:
            ck = 'au' if tone == 'gold' else 'g'
            chip = f'<span class="chip {ck}"><span class="big">{num}</span>cap</span>'
        rows.append(
            f'<div class="row {tone}"><span class="seal">{_svg(ic)}</span>'
            f'<span class="txt"><div class="lbl">{_chapter_title(ch)}</div>'
            f'<div class="sub">{_first_sentence(ch.get("intro",""), 100)}</div></span>{chip}</div>')
    rows_html = '<div class="divider"></div>'.join(rows)

    tip = ''
    for c in book.get('overview_cards', []):
        if c.get('tip'):
            tip = _first_sentence(re.sub(r'^<strong>.*?</strong>\s*', '', c['tip']), 150)
            break
    if not tip:
        tip = _first_sentence(book.get('intro', ''), 150)

    return (
        '<div class="slide lista">'
        '<div class="head">' + _brand('<span class="badge">Mapa do livro</span>') +
        f'<h1><span class="lt">{book["header_light"]}</span> <span class="bd">{book["header_bold"]}</span></h1>'
        f'<div class="promise">{_first_sentence(book.get("intro",""), 150)}</div>'
        '<div class="rule"></div></div>'
        f'<div class="rows fitv">{rows_html}</div>'
        '<div class="foot"><span class="ic">' + _svg('spark') + '</span>'
        f'<span class="body"><span class="kick">Na prática</span><span class="tactic">{tip}</span></span></div>'
        '<div class="wm">@minutoreal1701 · o livro inteiro em 1 página</div>'
        '</div>')


# ============================ ARQUETIPO: FLUXO (curado: campo FLUXO) ============================
# FLUXO = {"kicker": str, "steps": [{"n","ic","lbl","law","sub","gold"?}], "na_pratica": str}
ARCH_CSS['fluxo'] = """
.slide.fluxo{padding:84px 84px 96px}
.topbar{display:flex;justify-content:space-between;align-items:center}
.byline{font-weight:700;font-size:22px;color:var(--muted);letter-spacing:.01em;text-align:right}
.head{margin-top:30px;flex:0 0 auto}
.head .kicker{display:inline-block;font-size:20px;color:var(--green-soft);font-weight:800;
  letter-spacing:.16em;text-transform:uppercase;border:1.5px solid var(--hair);
  border-radius:999px;padding:9px 22px;background:oklch(70% 0.14 152 / .06)}
.head h1{font-size:74px;line-height:.94;font-weight:900;text-transform:uppercase;
  margin:22px 0 0;letter-spacing:-.022em;text-wrap:balance}
.head h1 .lt{color:var(--green);text-shadow:0 0 56px oklch(72% 0.14 152 / .38)}
.head h1 .bd{color:var(--ink)}
.flow{margin-top:40px;display:flex;flex-direction:column;gap:0;flex:1 1 auto}
.step{display:flex;gap:30px;align-items:flex-start;position:relative;padding-bottom:24px}
.step:last-child{padding-bottom:0}
.step:not(:last-child)::before{content:'';position:absolute;left:53px;top:108px;bottom:-2px;
  width:0;border-left:2px dashed var(--green);opacity:.5}
.step.gold:not(:last-child)::before,.step.gold + .step::before{border-color:var(--gold);opacity:.55}
.flow .seal{flex:0 0 auto;width:108px;height:108px;border-radius:50%;display:flex;
  flex-direction:column;align-items:center;justify-content:center;gap:1px;
  background:linear-gradient(160deg, oklch(70% 0.14 152 / .18), oklch(70% 0.14 152 / .05));
  border:2px solid var(--hair);position:relative;z-index:2;
  box-shadow:0 0 40px oklch(70% 0.14 152 / .14), inset 0 1px 0 oklch(90% 0.1 152 / .12)}
.flow .seal .num{font-weight:900;font-size:44px;line-height:.9;color:var(--green);text-shadow:0 0 14px oklch(72% 0.14 152 / .4)}
.flow .seal .ic{width:30px;height:30px;color:var(--green-soft);opacity:.92}
.flow .seal .ic svg{width:30px;height:30px}
.step.gold .seal{background:linear-gradient(160deg, oklch(80% 0.12 83 / .26), oklch(80% 0.12 83 / .06));
  border-color:oklch(80% 0.12 83 / .5);box-shadow:0 0 52px oklch(80% 0.12 83 / .22)}
.step.gold .seal .num{color:var(--gold);text-shadow:0 0 16px oklch(84% 0.12 83 / .45)}
.step.gold .seal .ic{color:var(--gold)}
.flow .body{flex:1 1 auto;padding-top:6px;min-width:0}
.flow .body .law{font-size:21px;font-weight:800;letter-spacing:.07em;text-transform:uppercase;color:var(--green);display:inline-block}
.step.gold .body .law{color:var(--gold)}
.flow .body .lbl{font-size:46px;font-weight:900;line-height:1.02;color:var(--ink);margin-top:4px;letter-spacing:-.01em}
.flow .body .sub{font-size:27px;line-height:1.3;color:var(--muted);margin-top:9px;font-weight:500;text-wrap:pretty;max-width:660px}
.flow .body .sub strong{color:var(--green-soft);font-weight:700}
.crown{display:inline-flex;align-items:center;gap:9px;margin-top:12px;font-size:18px;font-weight:800;
  letter-spacing:.08em;text-transform:uppercase;color:var(--on-gold);background:var(--gold);padding:7px 16px;border-radius:999px}
.crown svg{width:22px;height:22px;color:var(--on-gold)}
.foot{margin-top:30px;border-top:3px dashed var(--green);padding-top:24px;display:flex;gap:24px;align-items:flex-start;flex:0 0 auto}
.foot .ic{flex:0 0 auto;width:62px;height:62px;border-radius:16px;display:flex;align-items:center;
  justify-content:center;background:var(--green);color:var(--on-green);box-shadow:0 12px 34px oklch(60% 0.14 152 / .34)}
.foot .ic svg{width:38px;height:38px;color:var(--on-green)}
.foot .tag{font-size:21px;font-weight:900;letter-spacing:.14em;text-transform:uppercase;color:var(--green)}
.foot p{font-size:28px;line-height:1.3;color:var(--ink);font-weight:500;margin-top:6px;text-wrap:pretty}
.foot p strong{color:var(--green-soft);font-weight:800}
.wm{position:absolute;left:0;right:0;bottom:40px;text-align:center;font-weight:800;
  letter-spacing:.26em;font-size:19px;color:var(--ink-dim);text-transform:uppercase;z-index:2}
"""


def build_fluxo(data):
    book, f = data.BOOK, data.FLUXO
    steps = f['steps']
    out = []
    for s in steps:
        cls = 'step gold' if s.get('gold') else 'step'
        crown = f'<span class="crown">{_svg("spark")}Passo-chave</span>' if s.get('gold') else ''
        law = f'<span class="law">{s["law"]}</span>' if s.get('law') else ''
        out.append(
            f'<div class="{cls}"><div class="seal"><span class="num">{s["n"]}</span>'
            f'<span class="ic">{_svg(s["ic"])}</span></div>'
            f'<div class="body">{law}<div class="lbl">{s["lbl"]}</div>'
            f'<div class="sub">{s["sub"]}</div>{crown}</div></div>')
    return (
        '<div class="slide fluxo">'
        '<div class="ghost" style="top:360px;right:54px;font-size:240px">&#8594;</div>'
        '<div class="topbar">'
        f'<span class="brandmark"><span class="seal">{_svg("book")}</span>Minuto<b>Real</b></span>'
        f'<span class="byline">{book.get("author","")}</span></div>'
        f'<div class="head"><span class="kicker">{f["kicker"]}</span>'
        f'<h1><span class="lt">{book["header_light"]}</span> <span class="bd">{book["header_bold"]}</span></h1></div>'
        f'<div class="flow">{"".join(out)}</div>'
        '<div class="foot"><span class="ic">' + _svg('arrow') + '</span>'
        '<div><span class="tag">Na prática · comece hoje</span>'
        f'<p>{f["na_pratica"]}</p></div></div>'
        '<div class="wm">@minutoreal1701 · o livro em 1 página</div>'
        '</div>')


# ============================ ARQUETIPO: COMPARA (curado: campo COMPARA) ============================
# COMPARA = {"kicker","title" (com <span class='hi'>), "left"/"right":{ic,tag,label,items[]},
#            "verdict_ic","verdict"}.  Lado A=evite(verde-deep)+✕ · Lado B=faça(verde)+✓.
_CROSS = ('<svg viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">'
          '<path d="M20 20l24 24M44 20L20 44" stroke="currentColor" stroke-width="6" stroke-linecap="round"/></svg>')
_CHECK = ('<svg viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">'
          '<path d="M16 34l11 12 21-26" stroke="currentColor" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/></svg>')

ARCH_CSS['compara'] = """
.slide.compara{padding:74px 74px 122px}
.head{display:flex;flex-direction:column;gap:16px;align-items:center;text-align:center;flex:0 0 auto}
.kicker{font-size:18px;font-weight:800;letter-spacing:.22em;text-transform:uppercase;color:var(--green-soft)}
.head h1{font-size:54px;line-height:1.02;font-weight:900;text-transform:uppercase;letter-spacing:-.018em;text-wrap:balance;margin-top:2px}
.head h1 .hi{color:var(--green);text-shadow:0 0 46px oklch(72% 0.14 152 / .35)}
.versus{position:relative;display:grid;grid-template-columns:1fr 1fr;gap:0;margin-top:40px;flex:1 1 auto;
  border:2px solid var(--hair);border-radius:26px;overflow:hidden;background:oklch(70% 0.14 152 / .03)}
.vs{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);z-index:3;width:84px;height:84px;border-radius:50%;
  display:flex;align-items:center;justify-content:center;font-weight:900;font-size:30px;color:var(--on-gold);
  background:var(--gold);text-transform:uppercase;box-shadow:0 0 0 9px var(--bg2), 0 14px 38px oklch(20% 0.04 83 / .5)}
.col{padding:36px 32px;display:flex;flex-direction:column}
.col.b{border-left:2px solid var(--hair)}
.col-head{display:flex;flex-direction:column;align-items:flex-start;gap:15px;padding-bottom:24px;border-bottom:2px dashed var(--hair)}
.col-seal{width:88px;height:88px;border-radius:22px;display:flex;align-items:center;justify-content:center;position:relative;
  border:2px solid var(--hair);box-shadow:0 0 38px oklch(70% 0.14 152 / .12), inset 0 1px 0 oklch(90% 0.1 152 / .1)}
.col-seal svg{width:48px;height:48px;filter:drop-shadow(0 0 10px oklch(72% 0.14 152 / .35))}
.col-seal .mark{position:absolute;right:-13px;bottom:-13px;width:44px;height:44px;border-radius:50%;
  display:flex;align-items:center;justify-content:center;border:3px solid var(--bg2);box-shadow:0 6px 16px oklch(8% 0.01 152 / .6)}
.col-seal .mark svg{width:26px;height:26px;filter:none;color:inherit}
.col-label{font-weight:900;font-size:31px;line-height:1.04;text-transform:uppercase;letter-spacing:-.005em;text-wrap:balance}
.col-tag{display:inline-block;font-size:16px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;padding:6px 14px;border-radius:999px}
.col.a .col-seal{background:linear-gradient(160deg, oklch(56% 0.14 152 / .14), oklch(56% 0.14 152 / .03));border-color:oklch(56% 0.14 152 / .4)}
.col.a .col-seal>svg{color:var(--green-deep)}
.col.a .col-seal .mark{background:var(--green-deep);color:var(--ink)}
.col.a .col-label{color:var(--green-deep)}
.col.a .col-tag{color:var(--green-deep);background:oklch(56% 0.14 152 / .12);border:1.5px solid oklch(56% 0.14 152 / .35)}
.col.a .it::before{background:var(--green-deep)} .col.a .it b{color:var(--green-soft)}
.col.b .col-seal{background:linear-gradient(160deg, oklch(70% 0.14 152 / .18), oklch(70% 0.14 152 / .04));border-color:var(--hair)}
.col.b .col-seal>svg{color:var(--green)}
.col.b .col-seal .mark{background:var(--green);color:var(--on-green)}
.col.b .col-label{color:var(--ink)}
.col.b .col-tag{color:var(--green);background:oklch(70% 0.14 152 / .1);border:1.5px solid var(--hair)}
.col.b .it::before{background:var(--green)} .col.b .it b{color:var(--green-soft)}
.items{display:flex;flex-direction:column;gap:0;margin-top:22px}
.it{position:relative;padding:16px 0 16px 30px;font-size:25px;line-height:1.26;color:var(--ink);font-weight:500;text-wrap:pretty}
.it + .it{border-top:1.5px solid var(--hair2)}
.it::before{content:'';position:absolute;left:0;top:24px;width:13px;height:13px;border-radius:50%}
.it b{font-weight:800}
.verdict{display:flex;align-items:center;gap:24px;margin-top:34px;flex:0 0 auto;
  border:2px solid oklch(76% 0.105 83 / .4);border-radius:22px;padding:26px 32px;background:oklch(76% 0.105 83 / .07)}
.verdict .vseal{flex:0 0 auto;width:70px;height:70px;border-radius:18px;display:flex;align-items:center;justify-content:center;
  background:var(--gold);color:var(--on-gold);box-shadow:0 12px 32px oklch(50% 0.1 83 / .4)}
.verdict .vseal svg{width:42px;height:42px;color:var(--on-gold)}
.verdict .vlbl{font-weight:900;font-size:19px;letter-spacing:.2em;text-transform:uppercase;color:var(--gold)}
.verdict .vbody{font-size:27px;line-height:1.24;font-weight:600;color:var(--ink);text-wrap:pretty;margin-top:5px}
.verdict .vbody b{color:var(--gold);font-weight:800}
.wm{position:absolute;left:0;right:0;bottom:46px;text-align:center;font-weight:800;
  letter-spacing:.24em;font-size:20px;color:var(--ink-dim);text-transform:uppercase;z-index:2}
"""


def _col(side, spec):
    mark = _CROSS if side == 'a' else _CHECK
    items = ''.join(f'<div class="it">{it}</div>' for it in spec['items'])
    return (f'<div class="col {side}"><div class="col-head">'
            f'<div class="col-seal">{_svg(spec["ic"])}<span class="mark">{mark}</span></div>'
            f'<span class="col-tag">{spec["tag"]}</span>'
            f'<div class="col-label">{spec["label"]}</div></div>'
            f'<div class="items">{items}</div></div>')


def build_compara(data):
    book, d = data.BOOK, data.COMPARA
    kicker = d.get('kicker') or f'{book["title"]} · {book.get("author","")}'
    return (
        '<div class="slide compara">'
        '<div class="ghost" style="bottom:120px;left:50%;transform:translateX(-50%);font-size:300px">VS</div>'
        '<div class="head">'
        f'<span class="brandmark"><span class="seal">{_svg("book")}</span>Minuto<b>Real</b></span>'
        f'<span class="kicker">{kicker}</span>'
        f'<h1>{d["title"]}</h1></div>'
        f'<div class="versus">{_col("a", d["left"])}{_col("b", d["right"])}<span class="vs">vs</span></div>'
        '<div class="verdict"><span class="vseal">' + _svg(d.get('verdict_ic', 'scale')) + '</span>'
        '<span class="vtxt"><span class="vlbl">Na prática</span>'
        f'<span class="vbody">{d["verdict"]}</span></span></div>'
        '<div class="wm">@minutoreal1701</div>'
        '</div>')


# ============================ ARQUETIPO: NUMEROS (curado: campo NUMEROS) ============================
# NUMEROS = {"kicker"?, "tag"?, "stats":[{ic,pre?,num,unit?,star?,lbl,ctx}],
#            "viz"?:{type:"curve"|"bar", title, note, frac?, left?, right?}, "foot":{ic,text}}
ARCH_CSS['numeros'] = """
.slide.numeros{padding:74px 80px 66px}
.topbar{display:flex;justify-content:space-between;align-items:center}
.topbar .tag{font-weight:800;font-size:21px;letter-spacing:.16em;color:var(--green-soft);text-transform:uppercase;
  border:1.5px solid var(--hair);border-radius:999px;padding:9px 22px;background:oklch(70% 0.14 152 / .06)}
.head{margin-top:32px;flex:0 0 auto}
.head .kicker{font-size:22px;font-weight:800;letter-spacing:.2em;color:var(--green-soft);text-transform:uppercase}
.head h1{font-size:76px;line-height:.94;font-weight:900;text-transform:uppercase;margin-top:12px;letter-spacing:-.02em;text-wrap:balance}
.head h1 .lt{color:var(--green);text-shadow:0 0 56px oklch(72% 0.14 152 / .38)}
.head h1 .bd{color:var(--ink)}
.head .by{font-size:25px;color:var(--muted);font-weight:700;margin-top:12px}
.stats{margin-top:34px;display:flex;flex-direction:column;gap:0;flex:1 1 auto}
.stat{display:flex;align-items:center;gap:30px;padding:26px 0}
.stat + .stat{border-top:2px dashed var(--hair)}
.stat .ic{flex:0 0 auto;width:80px;height:80px;border-radius:20px;display:flex;align-items:center;justify-content:center;
  border:2px solid var(--hair);color:var(--green);background:linear-gradient(160deg, oklch(70% 0.14 152 / .14), oklch(70% 0.14 152 / .03));
  box-shadow:inset 0 1px 0 oklch(90% 0.1 152 / .1)}
.stat .ic svg{width:46px;height:46px;filter:drop-shadow(0 0 10px oklch(72% 0.14 152 / .4))}
.stat .num{flex:0 0 auto;min-width:236px;font-weight:900;line-height:.82;letter-spacing:-.04em;color:var(--green);
  font-size:104px;text-align:left;text-shadow:0 0 46px oklch(72% 0.14 152 / .30)}
.stat .num .u{font-size:52px;font-weight:900;letter-spacing:-.02em;margin-left:4px}
.stat .num .pre{font-size:54px;font-weight:800;color:var(--green-soft);margin-right:2px}
.stat.star .ic{border-color:oklch(76% 0.105 83 / .5);color:var(--gold);
  background:linear-gradient(160deg, oklch(76% 0.105 83 / .16), oklch(76% 0.105 83 / .03))}
.stat.star .ic svg{filter:drop-shadow(0 0 10px oklch(80% 0.11 83 / .45))}
.stat.star .num{color:var(--gold);text-shadow:0 0 46px oklch(80% 0.11 83 / .3)}
.stat.star .num .pre{color:oklch(82% 0.09 83)}
.stat .meta{display:flex;flex-direction:column;gap:7px;min-width:0}
.stat .meta .lbl{font-size:32px;font-weight:800;color:var(--ink);text-transform:uppercase;letter-spacing:.01em;line-height:1.04;text-wrap:balance}
.stat .meta .ctx{font-size:25px;font-weight:500;color:var(--muted);line-height:1.24;text-wrap:pretty}
.stat .meta .ctx b{color:var(--green-soft);font-weight:800}
.stat.star .meta .ctx b{color:oklch(82% 0.09 83)}
.viz{margin-top:22px;padding:20px 30px 16px;border-radius:22px;border:2px solid var(--hair2);background:oklch(70% 0.14 152 / .045);flex:0 0 auto}
.viz .vhead{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:8px}
.viz .vtitle{font-size:21px;font-weight:800;letter-spacing:.12em;color:var(--green-soft);text-transform:uppercase}
.viz .vnote{font-size:21px;font-weight:600;color:var(--muted)} .viz .vnote b{color:var(--gold);font-weight:800}
.viz svg{display:block;width:100%;height:auto}
.foot{margin-top:20px;display:flex;gap:22px;align-items:flex-start;border-top:3px dashed var(--green);padding-top:20px;flex:0 0 auto}
.foot .fic{flex:0 0 auto;width:54px;height:54px;border-radius:15px;display:flex;align-items:center;justify-content:center;
  background:var(--green);color:var(--on-green);margin-top:2px}
.foot .fic svg{width:34px;height:34px;color:var(--on-green)}
.foot .ft{min-width:0;flex:1}
.foot .ft .labrow{display:flex;justify-content:space-between;align-items:baseline;gap:16px}
.foot .ft .lab{font-size:23px;font-weight:900;letter-spacing:.18em;color:var(--green);text-transform:uppercase}
.foot .ft .handle{font-size:21px;font-weight:900;letter-spacing:.14em;color:var(--ink-dim);text-transform:uppercase}
.foot .ft p{font-size:29px;line-height:1.26;color:var(--ink);font-weight:600;margin-top:8px;text-wrap:pretty}
.foot .ft p strong{color:var(--green-soft);font-weight:800}
"""


def _viz_curve():
    """Curva de juros compostos (exponencial visual): sobe e dispara vs. plano cinza,
    ponto-ouro no fim. Generica (nao depende de numeros literais)."""
    import math
    base_y, span = 112, 96
    pts = []
    for i in range(53):
        t = i / 52
        y = base_y - (math.exp(3.6 * t) - 1) / (math.exp(3.6) - 1) * span
        pts.append(f'{14 + t * 506:.1f},{y:.1f}')
    curve = 'M' + ' L'.join(pts)
    ex, ey = 520, base_y - span
    return (
        '<svg viewBox="0 0 534 128" xmlns="http://www.w3.org/2000/svg" fill="none">'
        f'<line x1="14" y1="{base_y}" x2="520" y2="{base_y}" stroke="oklch(73% 0.05 152 / .25)" stroke-width="2"/>'
        f'<path d="M14,{base_y} L520,{base_y-7}" stroke="oklch(64% 0.02 152 / .55)" stroke-width="3" stroke-dasharray="8 8" stroke-linecap="round"/>'
        f'<path d="{curve} L520,{base_y} L14,{base_y} Z" fill="oklch(70% 0.13 152 / .12)"/>'
        f'<path d="{curve}" stroke="oklch(70% 0.13 152)" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>'
        f'<circle cx="{ex}" cy="{ey}" r="9" fill="oklch(76% 0.105 83)"/>'
        f'<circle cx="{ex}" cy="{ey}" r="16" fill="none" stroke="oklch(76% 0.105 83 / .5)" stroke-width="2.5"/>'
        '</svg>')


def _viz_bar(frac, left, right):
    """Barra empilhada: fatia pequena (verde-deep) vs. fatia dominante (ouro)."""
    full_w = 506
    bw = max(full_w * float(frac), 9)
    aw = full_w - bw
    y, h = 18, 48
    return (
        '<svg viewBox="0 0 534 96" xmlns="http://www.w3.org/2000/svg" fill="none">'
        f'<rect x="14" y="{y}" width="{full_w}" height="{h}" rx="13" fill="oklch(70% 0.14 152 / .08)" stroke="oklch(73% 0.05 152 / .25)" stroke-width="2"/>'
        f'<clipPath id="bz"><rect x="14" y="{y}" width="{full_w}" height="{h}" rx="13"/></clipPath>'
        f'<g clip-path="url(#bz)">'
        f'<rect x="14" y="{y}" width="{bw:.1f}" height="{h}" fill="oklch(56% 0.14 152)"/>'
        f'<rect x="{14+bw:.1f}" y="{y}" width="{aw:.1f}" height="{h}" fill="oklch(76% 0.105 83)"/></g>'
        f'<text x="14" y="{y+h+26}" font-family="Hanken Grotesk" font-weight="800" font-size="22" fill="oklch(64% 0.02 152)">{left}</text>'
        f'<text x="520" y="{y+h+26}" text-anchor="end" font-family="Hanken Grotesk" font-weight="900" font-size="22" fill="oklch(76% 0.105 83)">{right}</text>'
        '</svg>')


def build_numeros(data):
    book, d = data.BOOK, data.NUMEROS

    def stat(s):
        cls = 'stat star' if s.get('star') else 'stat'
        pre = f'<span class="pre">{s["pre"]}</span>' if s.get('pre') else ''
        unit = f'<span class="u">{s["unit"]}</span>' if s.get('unit') else ''
        return (f'<div class="{cls}"><span class="ic">{_svg(s["ic"])}</span>'
                f'<span class="num">{pre}{s["num"]}{unit}</span>'
                f'<span class="meta"><span class="lbl">{s["lbl"]}</span>'
                f'<span class="ctx">{s["ctx"]}</span></span></div>')

    stats = ''.join(stat(s) for s in d['stats'])
    viz_html = ''
    v = d.get('viz')
    if v:
        t = v.get('type')
        svg = _viz_curve() if t == 'curve' else (_viz_bar(v['frac'], v['left'], v['right']) if t == 'bar' else v.get('svg', ''))
        if svg:
            viz_html = ('<div class="viz"><div class="vhead">'
                        f'<span class="vtitle">{v.get("title","")}</span>'
                        f'<span class="vnote">{v.get("note","")}</span></div>{svg}</div>')
    return (
        '<div class="slide numeros">'
        '<div class="ghost" style="bottom:8px;right:14px;font-size:300px">%</div>'
        '<div class="topbar">'
        f'<span class="brandmark"><span class="seal">{_svg("book")}</span>Minuto<b>Real</b></span>'
        f'<span class="tag">{d.get("tag","Dados")}</span></div>'
        f'<div class="head"><div class="kicker">{d.get("kicker","O livro em números")}</div>'
        f'<h1><span class="lt">{book["header_light"]}</span> <span class="bd">{book["header_bold"]}</span></h1>'
        f'<div class="by">por {book.get("author","")}</div></div>'
        f'<div class="stats">{stats}</div>'
        f'{viz_html}'
        '<div class="foot"><span class="fic">' + _svg(d.get('foot', {}).get('ic', 'spark')) + '</span>'
        '<span class="ft"><span class="labrow"><span class="lab">Na prática</span>'
        '<span class="handle">@minutoreal1701</span></span>'
        f'<p>{d["foot"]["text"]}</p></span></div>'
        '</div>')


# ============================ ARQUETIPO: ANATOMIA (curado: campo ANATOMIA) ============================
# Layout "anel": ciclo de 4 nos (N,E,S,O, sentido horario) ao redor de um hub central,
# com callouts numerados nos 4 cantos. ANATOMIA = {"eyebrow"?, "h1" (com <span class='lt'>),
# "sub", "hub":{l1,l2,note}, "nodes":[4x {ic,law,lbl,exp}], "practice":{kicker,text,ic}}
ARCH_CSS['anatomia'] = """
.slide.anatomia{padding:74px 76px 72px}
.topbar{display:flex;justify-content:space-between;align-items:center;flex:0 0 auto}
.kpill{display:inline-flex;align-items:center;gap:10px;font-weight:800;font-size:19px;letter-spacing:.14em;
  text-transform:uppercase;color:var(--green-soft);border:1.5px solid var(--hair);border-radius:999px;
  padding:9px 20px;background:oklch(70% 0.14 152 / .06)}
.kpill .dot{width:9px;height:9px;border-radius:999px;background:var(--green);box-shadow:0 0 12px oklch(72% 0.14 152 / .7)}
.head{flex:0 0 auto;margin-top:28px}
.head .ey{font-size:21px;font-weight:800;letter-spacing:.22em;text-transform:uppercase;color:var(--green-soft)}
.head h1{font-size:60px;line-height:.98;font-weight:900;text-transform:uppercase;margin-top:12px;letter-spacing:-.02em;text-wrap:balance}
.head h1 .lt{color:var(--green);text-shadow:0 0 50px oklch(72% 0.14 152 / .38)}
.head .sub{font-size:25px;line-height:1.3;color:var(--muted);font-weight:500;margin-top:14px;max-width:840px;text-wrap:pretty}
.head .sub b{color:var(--green-soft);font-weight:800}
.stage{flex:1 1 auto;position:relative;margin:6px 0 12px;min-height:0}
.stage>svg{position:absolute;inset:0;width:100%;height:100%;overflow:visible}
.co{font-family:'Hanken Grotesk',sans-serif;color:var(--ink)}
.co .lbl{display:block;font-weight:900;font-size:30px;line-height:1.0;letter-spacing:.004em;color:var(--ink);text-transform:uppercase}
.co .lbl .law{display:block;font-size:16px;font-weight:800;letter-spacing:.08em;color:var(--green);margin-bottom:5px;text-transform:uppercase}
.co .exp{font-size:21px;line-height:1.24;color:var(--muted);font-weight:500;margin-top:8px}
.co .exp b{color:var(--green-soft);font-weight:800}
.co.ta-r{text-align:right} .co.ta-r .lbl .law{text-align:right}
.practice{flex:0 0 auto;display:flex;align-items:center;gap:24px;border:2px solid var(--hair);border-left:6px solid var(--green);
  border-radius:18px;padding:24px 30px;background:linear-gradient(100deg, oklch(70% 0.14 152 / .10), oklch(70% 0.14 152 / .02))}
.practice .pico{flex:0 0 auto;width:64px;height:64px;border-radius:16px;display:flex;align-items:center;justify-content:center;
  background:var(--green);color:var(--on-green);box-shadow:0 8px 24px oklch(60% 0.14 152 / .35)}
.practice .pico svg{width:38px;height:38px;color:var(--on-green)}
.practice .pk{font-size:18px;font-weight:900;letter-spacing:.2em;color:var(--green);text-transform:uppercase}
.practice p{font-size:27px;line-height:1.24;color:var(--ink);font-weight:600;margin-top:4px;text-wrap:pretty}
.practice p b{color:var(--green-soft);font-weight:800}
.foothandle{position:absolute;bottom:44px;right:62px;font-weight:800;letter-spacing:.16em;font-size:18px;color:var(--ink-dim);text-transform:uppercase;z-index:2}
"""


def _an_defs():
    return ('<defs><filter id="gl" x="-30%" y="-30%" width="160%" height="160%">'
            '<feGaussianBlur stdDeviation="3.2" result="b"/>'
            '<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>'
            '<marker id="ah" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6.5" markerHeight="6.5" '
            'orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="var(--green)"/></marker></defs>')


def _an_node(x, y, r, ic):
    inner = ICONS.get(ic, ICONS['book'])
    s = r / 32 * 0.92
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="var(--bg)" stroke="var(--green)" stroke-width="3" filter="url(#gl)"/>'
            f'<g transform="translate({x - 32 * s:.1f},{y - 32 * s:.1f}) scale({s:.3f})" '
            f'stroke="var(--green-soft)" color="oklch(85% 0.105 152)">{inner}</g>')


def _an_conn(x1, y1, x2, y2):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="var(--green)" stroke-width="1.6" '
            f'stroke-dasharray="2 6" stroke-linecap="round" opacity=".7"/>'
            f'<circle cx="{x2}" cy="{y2}" r="4.5" fill="var(--green)"/>')


def _an_cnum(x, y, n):
    return (f'<circle cx="{x}" cy="{y}" r="25" fill="var(--green)" stroke="var(--bg)" stroke-width="6"/>'
            f'<text x="{x}" y="{y}" text-anchor="middle" dominant-baseline="central" font-family="Hanken Grotesk" '
            f'font-weight="900" font-size="28" fill="var(--on-green)">{n}</text>')


def _art_ring(hub, nodes):
    """Anel de 4 nos (N,E,S,O horario) + hub central + callouts nos 4 cantos."""
    import math
    VBW, VBH = 928, 700
    cx, cy, R, nr = 464, 348, 176, 58
    pos = [(cx, cy - R), (cx + R, cy), (cx, cy + R), (cx - R, cy)]   # N,E,S,O
    arcs = ''
    pad, rr = nr + 16, R + 2
    seq = pos + [pos[0]]
    for (ax, ay), (bx, by) in zip(seq, seq[1:]):
        a, b = math.atan2(ay - cy, ax - cx), math.atan2(by - cy, bx - cx)
        sx, sy = cx + math.cos(a + .30) * pad, cy + math.sin(a + .30) * pad
        ex, ey = cx + math.cos(b - .30) * pad, cy + math.sin(b - .30) * pad
        arcs += (f'<path d="M{sx:.0f} {sy:.0f} A{rr} {rr} 0 0 1 {ex:.0f} {ey:.0f}" fill="none" '
                 f'stroke="var(--green)" stroke-width="3" marker-end="url(#ah)" opacity=".9"/>')
    art = ''.join(_an_node(x, y, nr, n['ic']) for (x, y), n in zip(pos, nodes))
    core = (f'<text x="{cx}" y="{cy-14}" text-anchor="middle" font-family="Hanken Grotesk" font-weight="900" '
            f'font-size="31" fill="var(--ink)">{hub.get("l1","")}</text>'
            f'<text x="{cx}" y="{cy+20}" text-anchor="middle" font-family="Hanken Grotesk" font-weight="900" '
            f'font-size="31" fill="var(--ink)">{hub.get("l2","")}</text>'
            f'<text x="{cx}" y="{cy+52}" text-anchor="middle" font-family="Hanken Grotesk" font-weight="700" '
            f'font-size="15" letter-spacing="2.4" fill="var(--green-soft)">{hub.get("note","")}</text>')
    nN, nE, nS, nW = pos
    # mapeamento fixo: no -> (caixa callout, alinhamento, conector, pos-numero, n)
    layout = [
        ((8, 16, 286, 150), 'l', (300, 76, nN[0] - nr, nN[1]), (300, 70), 1),
        ((650, 150, 278, 150), 'r', (650, 226, nE[0] + nr * .2, nE[1] - nr * .9), (650, 220), 2),
        ((642, 516, 286, 150), 'r', (628, 614, nS[0] + nr, nS[1]), (628, 620), 3),
        ((8, 516, 286, 150), 'l', (300, 614, nW[0] - nr * .2, nW[1] + nr * .9), (300, 620), 4),
    ]
    conns = nums = fos = ''
    for nd, (box, al, cn, nmp, n) in zip(nodes, layout):
        conns += _an_conn(*cn)
        nums += _an_cnum(nmp[0], nmp[1], str(n))
        cls = 'co ta-r' if al == 'r' else 'co'
        x, y, w, h = box
        fos += (f'<foreignObject x="{x}" y="{y}" width="{w}" height="{h}">'
                f'<div xmlns="http://www.w3.org/1999/xhtml" class="{cls}">'
                f'<span class="lbl"><span class="law">{nd["law"]}</span>{nd["lbl"]}</span>'
                f'<div class="exp">{nd["exp"]}</div></div></foreignObject>')
    return (f'<svg viewBox="0 0 {VBW} {VBH}" preserveAspectRatio="xMidYMid meet">'
            f'{_an_defs()}{arcs}{conns}{art}{core}{nums}{fos}</svg>')


def build_anatomia(data):
    book, d = data.BOOK, data.ANATOMIA
    eyebrow = d.get('eyebrow') or f'Anatomia · {book["title"]}'
    pr = d.get('practice', {})
    return (
        '<div class="slide anatomia">'
        f'<div class="topbar"><span class="brandmark"><span class="seal">{_svg("book")}</span>Minuto<b>Real</b></span>'
        f'<span class="kpill"><span class="dot"></span>{eyebrow}</span></div>'
        f'<div class="head"><div class="ey">{book.get("author","")}</div>'
        f'<h1>{d["h1"]}</h1><div class="sub">{d["sub"]}</div></div>'
        f'<div class="stage">{_art_ring(d.get("hub", {}), d["nodes"])}</div>'
        f'<div class="practice"><span class="pico">{_svg(pr.get("ic","spark"))}</span>'
        f'<div><div class="pk">{pr.get("kicker","Na prática")}</div><p>{pr.get("text","")}</p></div></div>'
        '<div class="foothandle">@minutoreal1701</div>'
        '</div>')


# registro: nome -> (builder, campo curado exigido | None se universal)
ARCHETYPES = {
    'lista': (build_lista, None),
    'fluxo': (build_fluxo, 'FLUXO'),
    'compara': (build_compara, 'COMPARA'),
    'numeros': (build_numeros, 'NUMEROS'),
    'anatomia': (build_anatomia, 'ANATOMIA'),
}


# ============================ render (paginas isoladas + auto-fit) ============================
_FIT_JS = """() => {
  for (const el of document.querySelectorAll('.head h1')) {
    const box = el.parentElement, cs = getComputedStyle(box);
    const avail = box.clientWidth - parseFloat(cs.paddingLeft) - parseFloat(cs.paddingRight);
    let fs = parseFloat(getComputedStyle(el).fontSize), g = 0;
    while (el.getBoundingClientRect().width > avail && fs > 40 && g < 120){ fs -= 3; el.style.fontSize = fs+'px'; g++; }
  }
  for (const el of document.querySelectorAll('.fitv')) {
    let fs = parseFloat(getComputedStyle(el).fontSize), g = 0;
    while (el.scrollHeight > el.clientHeight + 1 && fs > 24 && g < 60){ fs -= 1; el.style.fontSize = fs+'px'; g++; }
  }
}"""


def _render(slug, items, scale=2):
    out = OUTBASE / slug
    out.mkdir(parents=True, exist_ok=True)
    ff = _font_face()
    from playwright.sync_api import sync_playwright
    paths = []
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={'width': W, 'height': H}, device_scale_factor=scale)
        for arch, html in items:
            css = (BASE_CSS + ARCH_CSS.get(arch, '')).replace('__FONT_FACE__', ff)
            full = (f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
                    f'<style>{css}</style></head><body>{html}</body></html>')
            pg.set_content(full, wait_until='networkidle')
            pg.evaluate('document.fonts.ready')
            pg.wait_for_timeout(400)
            pg.evaluate(_FIT_JS)
            fp = out / f'{arch}.png'
            pg.query_selector('.slide').screenshot(path=str(fp))
            paths.append(fp)
            print('OK ->', fp)
        b.close()
    return paths


def main(slug, want):
    data = _load(slug)
    items = []
    for name in (want or list(ARCHETYPES)):
        builder, field = ARCHETYPES.get(name, (None, None))
        if not builder:
            print(f'[!] arquetipo desconhecido: {name} (tenho: {", ".join(ARCHETYPES)})')
            continue
        if field and not hasattr(data, field):
            print(f'[i] {slug} sem campo {field} — pulo "{name}" (arquetipo curado)')
            continue
        html = builder(data)
        if html:
            items.append((name, html))
    if not items:
        print(f'[!] nada a renderizar p/ {slug}')
        return
    _render(slug, items)


if __name__ == '__main__':
    a = sys.argv[1:]
    if not a:
        sys.exit('uso: python gerar_infografico.py <slug> [lista fluxo compara numeros anatomia]')
    main(a[0], a[1:])
