# -*- coding: utf-8 -*-
"""Gera CARROSSEL de Instagram (slides 1080x1350) de um livro da biblioteca,
na estética "Cheat Sheet Verde" (dark) PREMIUM, a partir do <slug>_data.py.

Fonte = a destilação que já existe (overview_cards ou os cards de um capítulo) —
NÃO o PDF cru. 1 carrossel = o livro em N ideias (ou 1 capítulo). Renderiza com
Playwright (Chromium) reusando os ícones de linha de gerar_livro.py.

Design (premium, jun/2026): fundo em camadas (glow + vinheta + grade de pontos +
grão), moldura tracejada refinada, numeral-fantasma por slide, ícones em selo com
halo, indicador de progresso (dots) e capa "para o dedo". Mesmo DNA verde 152.

Uso:
  python gerar_carrossel.py <slug>                 # carrossel da VISÃO GERAL (overview_cards)
  python gerar_carrossel.py <slug> --cap chNN-...  # carrossel de um capítulo
  python gerar_carrossel.py <slug> --citacao       # cards de citação (frases-bomba)

Saída:
  videos/_carrossel/<slug>_<parte>/01.png ... NN.png   (capa + conceitos + CTA)
  videos/_carrossel/<slug>_citacoes/01.png ... NN.png  (cards de citação)
"""
import sys, os, re, json, importlib
from pathlib import Path

BASE = Path(__file__).parent
sys.path.insert(0, str(BASE))
sys.path.insert(0, str(BASE / 'videos'))
from gerar_livro import icon  # reaproveita os ícones de linha reais
from instagram_post import _afiliado_block  # rodapé único de afiliado/disclosure

OUT_ROOT = BASE / 'videos' / '_carrossel'
ROTEIROS = BASE / 'videos' / 'roteiros'
W, H = 1080, 1350

# Ícones de linha extras (só usados aqui; mantemos gerar_livro.py intocado).
# Mesma gramática visual: viewBox 64, stroke currentColor, traço 3.
_EXTRA = {
    "bookmark": '<path d="M18 10h28v44L32 44 18 54z" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/>',
    "play": '<circle cx="32" cy="32" r="22" stroke="currentColor" stroke-width="3"/><path d="M27 23l16 9-16 9z" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/>',
    "shelf": '<path d="M14 12h36v40H14z" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/><path d="M14 24h36M14 38h36M24 12v12M40 24v14" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>',
    "spark": '<path d="M32 10l5 17 17 5-17 5-5 17-5-17-17-5 17-5z" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/>',
    "arrow": '<path d="M12 32h36M34 18l16 14-16 14" stroke="currentColor" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>',
    "shield": '<path d="M32 8l20 8v13c0 14-9 23-20 27-11-4-20-13-20-27V16z" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/>',
}


def _ic(name):
    """icon() de gerar_livro, com fallback para os ícones extras locais."""
    if name in _EXTRA:
        return ('<div class="card-icon" aria-hidden="true">'
                '<svg viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">'
                + _EXTRA[name] + '</svg></div>')
    return icon(name)


def _svg(name):
    """SVG cru (sem o wrapper .card-icon), p/ usar inline em selos/rodapés."""
    from gerar_livro import ICONS
    inner = ICONS.get(name) or _EXTRA.get(name, '')
    return f'<svg viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">{inner}</svg>'


CSS = """
@import url('https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;500;600;700;800;900&family=Literata:ital,opsz,wght@1,7..72,500;1,7..72,600&display=swap');
:root{
  --green: oklch(70% 0.13 152); --green-soft: oklch(85% 0.105 152); --green-deep: oklch(56% 0.14 152);
  --ink: oklch(98% 0.008 152); --muted: oklch(75% 0.022 152); --ink-dim: oklch(64% 0.02 152);
  --bg: oklch(14.5% 0.014 152); --bg2: oklch(10.5% 0.012 152); --on-green: oklch(13% 0.02 152);
  --gold: oklch(76% 0.105 83);
  --warn: oklch(72% 0.16 30); --on-warn: oklch(16% 0.03 30);
  --hair: oklch(73% 0.05 152 / .30); --hair2: oklch(73% 0.05 152 / .14);
}
*{margin:0;padding:0;box-sizing:border-box}
body{background:#000;font-family:'Hanken Grotesk',system-ui,sans-serif;
  -webkit-font-smoothing:antialiased;text-rendering:geometricPrecision}

/* ---------- base do slide: profundidade em camadas ---------- */
.slide{width:1080px;height:1350px;color:var(--ink);padding:92px 90px 150px;
  display:flex;flex-direction:column;position:relative;overflow:hidden;
  background:
   radial-gradient(135% 95% at 102% 108%, oklch(24% 0.045 152 / .85) 0%, transparent 48%),
   radial-gradient(115% 72% at 50% -12%, oklch(27% 0.05 152) 0%, transparent 60%),
   radial-gradient(150% 125% at 50% 48%, transparent 52%, oklch(5% 0.012 152 / .6) 100%),
   linear-gradient(177deg, var(--bg) 0%, var(--bg2) 100%);}
/* textura: grade de pontos finos (fade do topo) */
.slide::before{content:'';position:absolute;inset:0;pointer-events:none;
  background-image:radial-gradient(oklch(78% 0.07 152 / .055) 1.1px, transparent 1.3px);
  background-size:36px 36px;background-position:center;
  -webkit-mask-image:radial-gradient(125% 105% at 50% -5%, #000 50%, transparent 100%);}
/* moldura tracejada (DNA cheat sheet), refinada + halo interno */
.slide::after{content:'';position:absolute;inset:38px;border:2px dashed var(--green);
  border-radius:32px;opacity:.38;pointer-events:none;
  box-shadow:inset 0 0 90px oklch(70% 0.13 152 / .05)}
/* numeral-fantasma de fundo (contido pela moldura p/ não virar artefato) */
.slide>*{position:relative;z-index:1}
.slide>.ghost{position:absolute;font-family:'Hanken Grotesk';font-weight:900;line-height:.74;
  color:transparent;-webkit-text-stroke:2px oklch(74% 0.09 152 / .10);
  pointer-events:none;letter-spacing:-.05em;z-index:0;-webkit-user-select:none;overflow:hidden;
  -webkit-mask-image:radial-gradient(120% 120% at 50% 50%, #000 60%, transparent 100%)}
/* indicador de progresso */
.dots{position:absolute;left:0;right:0;bottom:74px;display:flex;gap:13px;
  justify-content:center;align-items:center;z-index:2}
.dots i{width:11px;height:11px;border-radius:999px;background:var(--hair);
  display:block;transition:none}
.dots i.on{width:38px;background:var(--green);
  box-shadow:0 0 18px oklch(72% 0.14 152 / .55)}
.wm{position:absolute;left:0;right:0;bottom:40px;text-align:center;font-weight:800;
  letter-spacing:.26em;font-size:21px;color:var(--ink-dim);text-transform:uppercase;z-index:2}

/* ---------- topbar (slides de conceito) ---------- */
.topbar{display:flex;justify-content:space-between;align-items:center}
.brandmark{display:inline-flex;align-items:center;gap:12px;font-weight:900;
  letter-spacing:.03em;font-size:28px;color:var(--ink);text-transform:uppercase}
.brandmark .seal{width:46px;height:46px;border-radius:13px;display:flex;align-items:center;
  justify-content:center;background:var(--green);color:var(--on-green);flex:0 0 auto}
.brandmark .seal svg{width:28px;height:28px;color:var(--on-green)}
.brandmark b{color:var(--green);font-weight:900}
.count{display:inline-flex;align-items:baseline;gap:4px;font-weight:800;
  font-size:26px;letter-spacing:.04em;color:var(--green-soft)}
.count b{font-size:34px;color:var(--green)} .count .sl{color:var(--hair);font-weight:700}

/* ---------- selo do ícone ---------- */
.card-icon{width:108px;height:108px;border-radius:26px;display:flex;align-items:center;
  justify-content:center;margin:46px 0 28px;
  background:linear-gradient(160deg, oklch(70% 0.14 152 / .16), oklch(70% 0.14 152 / .04));
  border:2px solid var(--hair);
  box-shadow:0 0 48px oklch(70% 0.14 152 / .14), inset 0 1px 0 oklch(90% 0.1 152 / .12)}
.card-icon svg{width:58px;height:58px;color:var(--green);
  filter:drop-shadow(0 0 12px oklch(72% 0.14 152 / .45))}
.warn .card-icon{background:linear-gradient(160deg, oklch(75% 0.16 38 / .16), oklch(75% 0.16 38 / .04));
  border-color:oklch(75% 0.16 38 / .42);box-shadow:0 0 48px oklch(75% 0.16 38 / .14)}
.warn .card-icon svg{color:var(--warn);filter:drop-shadow(0 0 12px oklch(75% 0.16 38 / .45))}

/* ---------- conceito ---------- */
.card-title{display:inline-block;background:var(--green);color:var(--on-green);
  font-weight:800;font-size:52px;line-height:1.12;padding:15px 30px;border-radius:16px;
  text-transform:uppercase;text-wrap:balance;align-self:flex-start;letter-spacing:.004em;
  box-shadow:0 14px 40px oklch(60% 0.14 152 / .3)}
.warn .card-title{background:var(--warn);color:var(--on-warn);
  box-shadow:0 14px 40px oklch(65% 0.16 38 / .3)}
.card-body{font-size:45px;line-height:1.4;color:var(--ink);margin-top:28px;
  font-weight:500;text-wrap:pretty}
.card-body strong{color:var(--green-soft);font-weight:800}
.warn .card-body strong{color:var(--warn)}
.card-tip{display:flex;gap:20px;align-items:flex-start;font-size:31px;line-height:1.36;
  color:var(--green-soft);margin-top:auto;margin-bottom:8px;border-top:2px dashed var(--green);
  padding-top:30px;font-weight:500;text-wrap:pretty}
.card-tip .tipic{flex:0 0 auto;width:42px;height:42px;margin-top:2px;color:var(--green)}
.card-tip .tipic svg{width:42px;height:42px}
.card-tip strong{color:var(--green);font-weight:800}
.warn .card-tip{color:var(--warn);border-color:oklch(75% 0.16 38 / .5)}
.warn .card-tip .tipic{color:var(--warn)} .warn .card-tip strong{color:var(--warn)}

/* ---------- conceito EDITORIAL (padrão quente W2) ---------- */
.ed{flex:1;display:flex;flex-direction:column;margin-top:30px}
.ed-head{display:flex;align-items:flex-end;gap:34px;margin-bottom:8px}
.ed-num{font-family:'Literata',Georgia,serif;font-weight:600;font-size:300px;line-height:.72;
  color:transparent;-webkit-text-stroke:2.5px oklch(74% 0.11 152 / .55);letter-spacing:-.04em;
  flex:0 0 auto;text-shadow:0 0 70px oklch(72% 0.14 152 / .12)}
.warn .ed-num{-webkit-text-stroke-color:oklch(75% 0.16 38 / .5)}
.ed-meta{flex:1;padding-bottom:22px}
.ed-kicker{font-weight:800;font-size:23px;letter-spacing:.26em;text-transform:uppercase;color:var(--green);margin-bottom:14px}
.warn .ed-kicker{color:var(--warn)}
.ed-rule{height:0;border-top:2px dashed var(--green);opacity:.7;margin-bottom:18px}
.warn .ed-rule{border-color:var(--warn)}
.ed-source{font-family:'Literata',Georgia,serif;font-style:italic;font-weight:400;font-size:27px;line-height:1.3;color:var(--muted)}
.ed-source b{color:var(--green-soft);font-style:normal;font-weight:600}
.ed-title{font-family:'Literata',Georgia,serif;font-weight:700;font-size:80px;line-height:1.04;color:var(--ink);letter-spacing:-.018em;text-wrap:balance;margin:18px 0 6px}
.ed-title em{font-style:italic;font-weight:600;color:var(--green)}
.warn .ed-title em{color:var(--warn)}
.ed-body{font-family:'Literata',Georgia,serif;font-weight:400;font-size:44px;line-height:1.5;color:var(--ink);text-wrap:pretty;margin-top:30px;padding-top:34px;border-top:2px solid var(--hair2);position:relative}
.ed-body::before{content:'';position:absolute;top:-1px;left:0;width:120px;height:0;border-top:3px solid var(--green)}
.warn .ed-body::before{border-color:var(--warn)}
.ed-body strong{font-weight:700;color:var(--green-soft)}
.warn .ed-body strong{color:var(--warn)}
.ed-body .dc{float:left;font-family:'Literata',Georgia,serif;font-weight:600;font-size:138px;line-height:.78;color:var(--green);margin:8px 22px -6px 0;text-shadow:0 0 44px oklch(72% 0.14 152 / .3)}
.warn .ed-body .dc{color:var(--warn)}
.ed-tip{margin-top:auto;display:flex;gap:26px;align-items:flex-start;background:linear-gradient(150deg, oklch(70% 0.14 152 / .14), oklch(70% 0.14 152 / .035));border:2px solid var(--hair);border-left:6px solid var(--green);border-radius:22px;padding:34px 38px;box-shadow:0 16px 44px oklch(8% 0.02 152 / .45), inset 0 1px 0 oklch(90% 0.1 152 / .08)}
.warn .ed-tip{border-left-color:var(--warn);background:linear-gradient(150deg, oklch(75% 0.16 38 / .14), oklch(75% 0.16 38 / .035))}
.ed-tip .tipic{flex:0 0 auto;width:60px;height:60px;border-radius:16px;display:flex;align-items:center;justify-content:center;background:var(--green);color:var(--on-green);box-shadow:0 8px 22px oklch(60% 0.14 152 / .4)}
.warn .ed-tip .tipic{background:var(--warn)}
.ed-tip .tipic svg{width:34px;height:34px;color:var(--on-green)}
.ed-tip .tiptext{flex:1}
.ed-tip .tiplabel{font-weight:900;font-size:20px;letter-spacing:.22em;text-transform:uppercase;color:var(--green);margin-bottom:9px}
.warn .ed-tip .tiplabel{color:var(--warn)}
.ed-tip .tipbody{font-size:31px;line-height:1.36;color:var(--green-soft);font-weight:500;text-wrap:pretty}
.ed-tip .tipbody strong{color:var(--green);font-weight:800}
.warn .ed-tip .tipbody{color:oklch(82% 0.08 38)} .warn .ed-tip .tipbody strong{color:var(--warn)}

/* ---------- capa ---------- */
.cover{justify-content:center;text-align:center;align-items:center}
/* wordmark = ASSINATURA forte do canal (a marca para o dedo) */
.cover .wordmark{position:absolute;top:74px;left:0;right:0;display:flex;
  align-items:center;justify-content:center;gap:16px;z-index:2}
.cover .wordmark .seal{width:62px;height:62px;border-radius:18px;display:flex;
  align-items:center;justify-content:center;background:var(--green);color:var(--on-green);
  box-shadow:0 10px 30px oklch(60% 0.14 152 / .4)}
.cover .wordmark .seal svg{width:38px;height:38px;color:var(--on-green)}
.cover .wordmark .name{font-weight:900;letter-spacing:.04em;font-size:40px;
  color:var(--ink);text-transform:uppercase;line-height:1}
.cover .wordmark .name b{color:var(--green)}
.cover .kicker{display:inline-block;font-size:21px;color:var(--green-soft);font-weight:800;
  letter-spacing:.2em;text-transform:uppercase;margin-top:0;max-width:680px;line-height:1.35;
  border:1.5px solid var(--hair);border-radius:999px;padding:11px 26px;
  background:oklch(70% 0.14 152 / .06)}
.cover h1{font-size:124px;line-height:.92;font-weight:900;text-transform:uppercase;
  margin:30px 0 0;text-wrap:balance;letter-spacing:-.022em}
.cover h1 .lt{color:var(--green);text-shadow:0 0 60px oklch(72% 0.14 152 / .4)}
.cover h1 .bd{color:var(--ink)}
.cover .author{font-size:34px;color:var(--muted);margin-top:30px;font-weight:700;letter-spacing:.01em}
.cover .hook{display:flex;align-items:center;justify-content:center;gap:28px;
  margin-top:58px;border-top:3px dashed var(--green);border-bottom:3px dashed var(--green);
  padding:32px 0;max-width:820px}
.cover .hook .num{font-size:128px;font-weight:900;line-height:.76;color:var(--gold);
  letter-spacing:-.04em;text-shadow:0 0 50px oklch(84% 0.12 92 / .35)}
.cover .hook .lbl{font-size:48px;font-weight:800;color:var(--ink);text-align:left;
  line-height:1.04;text-transform:uppercase;text-wrap:balance}
.cover .hook .lbl span{color:var(--green)}
/* swipe = affordance principal: pill verde, grande, perto do polegar */
.cover .swipe{position:absolute;bottom:120px;left:50%;transform:translateX(-50%);
  font-weight:800;letter-spacing:.16em;font-size:30px;color:var(--on-green);
  text-transform:uppercase;display:inline-flex;align-items:center;justify-content:center;
  gap:18px;z-index:2;background:var(--green);padding:20px 44px;border-radius:999px;
  box-shadow:0 16px 44px oklch(60% 0.14 152 / .42);white-space:nowrap}
.cover .swipe .arrow{display:inline-flex;width:38px;height:38px}
.cover .swipe .arrow svg{width:38px;height:38px;color:var(--on-green)}

/* ---------- cta ---------- */
.cta{justify-content:center;text-align:center;align-items:center;padding-top:110px}
.cta .big{font-size:90px;line-height:1.0;font-weight:900;text-transform:uppercase;text-wrap:balance;letter-spacing:-.015em}
.cta .big .lt{color:var(--green);text-shadow:0 0 56px oklch(72% 0.14 152 / .32)}
.cta .rows{display:flex;flex-direction:column;gap:0;margin-top:58px;width:100%;max-width:780px}
.cta .row{display:flex;align-items:center;gap:26px;padding:30px 4px;text-align:left}
.cta .row + .row{border-top:2px dashed var(--hair)}
.cta .row .rico{flex:0 0 auto;width:70px;height:70px;border-radius:18px;display:flex;
  align-items:center;justify-content:center;background:oklch(70% 0.14 152 / .12);
  border:2px solid var(--hair);color:var(--green)}
.cta .row .rico svg{width:40px;height:40px}
.cta .row p{font-size:38px;line-height:1.24;color:var(--ink);font-weight:600;text-wrap:pretty}
.cta .row p strong{color:var(--green-soft);font-weight:800}
.cta .save{margin-top:60px;display:inline-flex;align-items:center;gap:18px;background:var(--green);
  color:var(--on-green);font-weight:800;font-size:40px;padding:24px 52px;border-radius:20px;
  text-transform:uppercase;box-shadow:0 18px 50px oklch(60% 0.14 152 / .4)}
.cta .save svg{width:44px;height:44px;flex:0 0 auto}
.cta .handle{position:absolute;bottom:116px;left:0;right:0;font-weight:900;letter-spacing:.12em;
  font-size:30px;color:var(--green-soft);text-transform:uppercase;z-index:2}

/* ---------- citação ---------- */
.quote{justify-content:center;align-items:flex-start;text-align:left;padding-top:120px}
.quote .qhead{position:absolute;top:80px;left:90px}
.quote .qmark{font-family:'Literata',Georgia,serif;font-style:italic;font-weight:600;
  font-size:280px;line-height:.62;color:var(--green);opacity:.92;height:150px;
  text-shadow:0 0 50px oklch(72% 0.14 152 / .3)}
.quote .qcount{position:absolute;top:104px;right:90px;z-index:2;
  font-weight:800;font-size:26px;letter-spacing:.04em;color:var(--green-soft);
  display:inline-flex;align-items:baseline;gap:4px}
.quote .qcount b{font-size:32px;color:var(--green)} .quote .qcount .sl{color:var(--hair)}
.quote .phrase{font-size:66px;line-height:1.2;font-weight:800;color:var(--ink);
  margin-top:8px;text-wrap:balance;letter-spacing:-.012em}
.quote .phrase em{color:var(--green);font-style:normal}
.quote .attr{margin-top:50px;padding-top:32px;border-top:3px dashed var(--green);
  font-size:34px;line-height:1.34;color:var(--green-soft);font-weight:800;letter-spacing:.01em}
.quote .attr .book{color:var(--muted);font-weight:600;font-style:italic}
.quote .foot{position:absolute;left:90px;right:90px;bottom:104px;display:flex;
  align-items:center;justify-content:space-between;z-index:2}
.quote .foot .handle{font-weight:900;letter-spacing:.08em;font-size:28px;color:var(--green-soft);text-transform:uppercase}
.quote .foot .cta-min{font-weight:800;letter-spacing:.02em;font-size:25px;color:var(--on-green);
  text-transform:uppercase;display:inline-flex;align-items:center;gap:12px;background:var(--green);
  padding:14px 26px;border-radius:999px;box-shadow:0 10px 30px oklch(60% 0.14 152 / .35)}
.quote .foot .cta-min svg{width:30px;height:30px;color:var(--on-green)}
"""


def _ghost(style, text):
    """Numeral/símbolo-fantasma de fundo. O estilo (posição + tamanho) vai no
    PRÓPRIO div (que é absolute), senão não posiciona."""
    return f'<div class="ghost" style="{style}">{text}</div>'


def _slide(inner, cls='', ghost=''):
    return f'<div class="slide {cls}">{ghost}{inner}</div>'


def _dots(pos, total):
    return ('<div class="dots">'
            + ''.join(f'<i class="{"on" if k == pos else ""}"></i>' for k in range(1, total + 1))
            + '</div>')


def _kicker_text(book):
    """Kicker curto e escaneável (Krug: omita palavras). Tira o prefixo
    'VISÃO GERAL · ' redundante p/ não competir com o título; cai nas tags se vazio."""
    k = book.get('subtitle', '') or ' · '.join(book.get('tags', [])[:3]).upper()
    k = re.sub(r'^\s*VIS[ÃA]O GERAL\s*[·\-—]\s*', '', k, flags=re.IGNORECASE)
    return k.strip()


def _cover(book, n, pos, total):
    kicker = _kicker_text(book)
    kicker_html = f'<div class="kicker">{kicker}</div>' if kicker else ''
    return _slide(
        f'<div class="wordmark"><span class="seal">{_svg("book")}</span>'
        f'<span class="name">Minuto<b>Real</b></span></div>'
        f'{kicker_html}'
        f'<h1><span class="lt">{book["header_light"]}</span> <span class="bd">{book["header_bold"]}</span></h1>'
        f'<div class="author">por {book["author"]}</div>'
        f'<div class="hook"><span class="num">{n}</span>'
        f'<span class="lbl">ideias<br>que <span>ficam</span></span></div>'
        f'<div class="swipe"><span>arrasta</span>'
        f'<span class="arrow">{_svg("arrow")}</span></div>'
        f'{_dots(pos, total)}',
        'cover')


def _ed_title(t):
    """Título editorial: última palavra significativa em itálico verde (acento)."""
    words = t.split()
    if len(words) >= 2:
        return ' '.join(words[:-1]) + f' <em>{words[-1]}</em>'
    return f'<em>{t}</em>'


def _ed_source(ch):
    """'Capítulo N · <título>' a partir do sub do capítulo."""
    sub = (ch or {}).get('sub', '') if ch else ''
    if not sub:
        return ''
    m = re.match(r'\s*CAP[IÍ]TULO\s*(\d+)\s*[:\-–·]\s*(.+)', sub, re.IGNORECASE)
    if m:
        return f'Capítulo {m.group(1)} &middot; <b>{m.group(2).strip()}</b>'
    return f'<b>{sub.strip()}</b>'


def _concept(c, i, total_cards, pos, total, book=None, ch=None):
    cls = 'concept' + (' warn' if c.get('warn') else '')
    kicker = ''
    if book:
        kicker = f"{book.get('header_light','')} {book.get('header_bold','')}".strip()
    kicker = kicker or 'MINUTO REAL'
    # corpo com capitular (drop-cap) na 1ª letra visível (tolera tag inicial)
    body = c['b']
    mdc = re.match(r'^(\s*(?:<[^>]+>)*)([A-Za-zÀ-ÿ])(.*)$', body, re.DOTALL)
    body_html = (mdc.group(1) + f'<span class="dc">{mdc.group(2)}</span>' + mdc.group(3)) if mdc else body
    # tip vira caixa editorial: rótulo (do <strong>…:</strong>) + corpo
    tip_html = ''
    if c.get('tip'):
        mt = re.match(r'\s*<strong>(.*?)</strong>\s*(.*)', c['tip'], re.DOTALL)
        if mt:
            label = re.sub(r'[:：]\s*$', '', mt.group(1)).strip()
            tipbody = mt.group(2).strip()
        else:
            label, tipbody = ('Cuidado' if c.get('warn') else 'Dica'), c['tip']
        tipic = _svg('shield') if c.get('warn') else _svg('spark')
        tip_html = (f'<div class="ed-tip"><span class="tipic">{tipic}</span>'
                    f'<div class="tiptext"><div class="tiplabel">{label}</div>'
                    f'<div class="tipbody">{tipbody}</div></div></div>')
    return _slide(
        f'<div class="topbar"><span class="brandmark">'
        f'<span class="seal">{_svg("book")}</span>Minuto<b>Real</b></span>'
        f'<span class="count"><b>{i:02d}</b><span class="sl">/</span>{total_cards:02d}</span></div>'
        f'<div class="ed">'
        f'<div class="ed-head"><div class="ed-num">{i}</div>'
        f'<div class="ed-meta"><div class="ed-kicker">{kicker}</div>'
        f'<div class="ed-rule"></div><div class="ed-source">{_ed_source(ch)}</div></div></div>'
        f'<h1 class="ed-title">{_ed_title(c["t"])}</h1>'
        f'<p class="ed-body">{body_html}</p>'
        f'{tip_html}'
        f'</div>'
        f'{_dots(pos, total)}',
        cls)


def _cta(book, pos, total):
    return _slide(
        '<div class="big">Gostou?<br><span class="lt">tem mais.</span></div>'
        '<div class="rows">'
        f'<div class="row"><span class="rico">{_svg("shelf")}</span>'
        '<p>O livro inteiro em 1 página: cheat sheet + PDF no <strong>acervo</strong> &mdash; link na bio.</p></div>'
        f'<div class="row"><span class="rico">{_svg("play")}</span>'
        f'<p>Prefere assistir? Resumo de ~5 min no <strong>YouTube</strong>.</p></div>'
        f'<div class="row"><span class="rico">{_svg("spark")}</span>'
        '<p>Um grande livro destilado por semana. <strong>Siga @minutoreal1701</strong>.</p></div>'
        '</div>'
        f'<div class="save">{_svg("bookmark")}Salve para revisar</div>'
        '<div class="handle">@minutoreal1701</div>'
        f'{_dots(pos, total)}',
        'cta',
        ghost=_ghost('bottom:150px;right:40px;font-size:300px', '+'))


# ---------- modo citação ----------

def _strip_html(s):
    return re.sub(r'<[^>]+>', '', s).strip()


def _split_sentences(text):
    """Quebra a narração em frases, mantendo travessões/reticências legíveis."""
    parts = re.split(r'(?<=[.!?])\s+', text.strip())
    return [p.strip() for p in parts if p.strip()]


def _score(sent):
    """Pontua o quão 'frase-bomba' é: curta o bastante p/ caber grande,
    com travessão/contraste (caro do tipo 'X não é Y'), sem ser pergunta."""
    n = len(sent)
    if n < 28 or n > 150:
        return -1
    s = 0
    if 40 <= n <= 110:
        s += 3
    if '—' in sent or ' — ' in sent:
        s += 2
    low = sent.lower()
    for kw in (' não é ', 'não há', 'sempre', 'nunca', 'toda', 'todo ', 'a meta', 'o segredo',
               'a régua', 'a lei', 'a porta', 'é a ', ' é o '):
        if kw in low:
            s += 1
    if sent.endswith('?'):
        s -= 3
    if sent.endswith(':'):
        s -= 2
    return s


def _best_quotes(slug, book, data, want=5):
    """Extrai as melhores frases: prioriza as cenas marcadas em `shorts` do
    roteiro; completa com cards do _data.py (campos b/tip). Devolve lista de
    dicts {phrase, attr}."""
    quotes = []
    seen = set()

    def add(phrase):
        phrase = phrase.strip().rstrip(' .')
        key = phrase.lower()[:48]
        if len(phrase) < 24 or len(phrase) > 150 or key in seen:
            return
        seen.add(key)
        quotes.append(phrase)

    rot = ROTEIROS / f'{slug}.json'
    if rot.exists():
        r = json.loads(rot.read_text(encoding='utf-8'))
        cenas = r.get('cenas', [])
        heroes = set(r.get('shorts', []))
        # indexa cenas-conceito por número (kicker "01 · ...") p/ casar com shorts
        ordered = []  # (is_hero, scene)
        ci = 0
        for sc in cenas:
            if sc.get('tipo') == 'conceito':
                ci += 1
                ordered.append((ci in heroes, sc))
            else:
                ordered.append((False, sc))
        # 1) cenas-herói primeiro, melhor frase de cada
        for is_hero, sc in ordered:
            if not is_hero:
                continue
            cands = sorted(_split_sentences(sc.get('narracao', '')), key=_score, reverse=True)
            if cands and _score(cands[0]) >= 0:
                add(cands[0])
        # 2) completa com as melhores frases de qualquer cena
        pool = []
        for _, sc in ordered:
            for s in _split_sentences(sc.get('narracao', '')):
                pool.append(s)
        for s in sorted(pool, key=_score, reverse=True):
            if len(quotes) >= want:
                break
            if _score(s) >= 2:
                add(s)

    # 3) reforço com os cards do _data.py (campo b destacado)
    cards = book.get('overview_cards') or (data.CHAPTERS[0]['cards'] if data.CHAPTERS else [])
    for c in cards:
        if len(quotes) >= want:
            break
        for field in ('tip', 'b'):
            cand = _strip_html(c.get(field, ''))
            # a 'dica' costuma vir como "Modelo mental: <frase>" — fica a frase
            cand = re.sub(r'^[^:]{0,28}:\s*', '', cand)
            for s in _split_sentences(cand):
                if _score(s) >= 3:
                    add(s)
                    break

    return quotes[:want]


def _emph(phrase):
    """Realça as palavras-chave em verde: termo entre travessões ou a última
    oração curta. Heurística leve — sem exagero."""
    # destaca o trecho após o último travessão (o 'punch' da frase)
    if '—' in phrase:
        head, _, tail = phrase.rpartition('—')
        if 6 <= len(tail.strip()) <= 60:
            return f'{head.strip()} — <em>{tail.strip()}</em>'
    return phrase


def _quote_card(q, book, k, total):
    foot = (
        '<div class="foot">'
        '<span class="handle">@minutoreal1701</span>'
        f'<span class="cta-min">{_svg("bookmark")}salve esta</span>'
        '</div>')
    attr = f'<div class="attr">{book["author"]}<br><span class="book">{book["title"]}</span></div>'
    qcount = (f'<div class="qcount"><b>{k:02d}</b><span class="sl">/</span>{total:02d}</div>'
              if total > 1 else '')
    return _slide(
        '<div class="qhead"><div class="qmark">&ldquo;</div></div>'
        f'{qcount}'
        f'<div class="phrase">{_emph(q)}</div>'
        f'{attr}{foot}',
        'quote',
        ghost=_ghost('bottom:150px;right:24px;font-size:320px', '&rdquo;'))


def _render(slides, out, scale=2, w=W, h=H, css=None):
    out.mkdir(parents=True, exist_ok=True)
    html = (f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
            f'<style>{css or CSS}</style></head><body>{"".join(slides)}</body></html>')
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={'width': w, 'height': h}, device_scale_factor=scale)
        pg.set_content(html, wait_until='networkidle')
        pg.evaluate('document.fonts.ready')
        pg.wait_for_timeout(500)
        # auto-encolhe titulos que estouram a caixa (palavra unica longa: METAMORFOSE,
        # COMUNICACAO, INSUSTENTAVEL...). Duravel: blinda qualquer titulo futuro sem
        # tocar nos que ja cabem. O h1 e flex-item centralizado (encolhe no proprio
        # texto), entao medimos contra a CAIXA DE CONTEUDO do contentor, nao o h1.
        pg.evaluate("""() => {
          for (const el of document.querySelectorAll('.cover h1, .st h1')) {
            const box = el.parentElement, cs = getComputedStyle(box);
            const avail = box.clientWidth - parseFloat(cs.paddingLeft) - parseFloat(cs.paddingRight);
            let fs = parseFloat(getComputedStyle(el).fontSize), guard = 0;
            while (el.getBoundingClientRect().width > avail && fs > 50 && guard < 120) {
              fs -= 3; el.style.fontSize = fs + 'px'; guard++;
            }
          }
        }""")
        paths = []
        for i, el in enumerate(pg.query_selector_all('.slide, .story'), 1):
            fp = out / f'{i:02d}.png'
            el.screenshot(path=str(fp))
            paths.append(fp)
        b.close()
    print(f'OK: {len(paths)} slides -> {out}')
    for fp in paths:
        print('  ', fp.name)
    return out


def build(slug, cap=None):
    data = importlib.import_module(slug.replace('-', '_') + '_data')
    book = data.BOOK
    ch = None
    if cap:
        ch = next((c for c in data.CHAPTERS if c['slug'] == cap or c['slug'].startswith(cap)), None)
        if not ch:
            sys.exit(f'[!] capitulo {cap} nao encontrado em {slug}')
        cards = ch['cards']
        part = ch['slug']
    else:
        cards = book.get('overview_cards') or (data.CHAPTERS[0]['cards'])
        part = 'overview'
    n = len(cards)
    total = n + 2  # capa + conceitos + cta
    slides = [_cover(book, n, 1, total)]
    slides += [_concept(c, i, n, i + 1, total, book, ch) for i, c in enumerate(cards, 1)]
    slides.append(_cta(book, total, total))
    out = _render(slides, OUT_ROOT / f'{slug}_{part}')
    qs = _best_quotes(slug, book, data, want=1)
    quote = _strip_html(qs[0]).rstrip(' .') if qs else book.get('subtitle', '')
    _write_stories(out, slug, book, n, quote)
    return out


def _caption_citacao(slug, book, quotes):
    """Legenda premium do carrossel de citações: a frase-bomba como gancho +
    apelo de salvar + CTA em camadas + seguir + afiliado/disclosure + hashtags."""
    gancho = _strip_html(quotes[0]).rstrip(' .') if quotes else book['title']
    tags = [re.sub(r'[^0-9a-z]', '', t.lower().replace(' ', '')) for t in book.get('tags', [])[:2]]
    hs = ' '.join('#' + t for t in (['livros', 'resumodelivro', 'leitura']
                                     + [t for t in tags if t]))
    return (f'"{gancho}"\n— {book["author"]}, em "{book["title"]}"\n\n'
            f'📌 Salve as frases que ficam.\n\n'
            f'📄 Cheat sheet + PDF, de graça, no acervo — link na bio.\n'
            f'🎬 Resumo em vídeo (~5 min) no YouTube.\n\n'
            f'Siga @minutoreal1701 — um grande livro por semana.\n\n'
            f'{_afiliado_block(slug)}\nNarração e arte por IA.\n\n{hs}')


def _write_stories(out, slug, book, n, quote):
    """Roteiro premium de STORIES (3 frames) p/ empurrar o post novo -> YouTube/
    acervo/Amazon. Texto pronto p/ overlay; salvo em stories.txt."""
    titulo = f'{book["header_light"]} {book["header_bold"]}'.strip()
    txt = (f"=== STORIES - {book['title']} ===\n"
           "1 frame por tela (1080x1920 vertical). Texto = overlay na arte; [..] = figurinha.\n\n"
           "FRAME 1 - TEASER\n"
           "NOVO no acervo\n"
           f'"{titulo}" em {n} ideias que ficam.\n'
           "[enquete] Ja conhece esse livro?  Sim / Ainda nao\n"
           "-> Cheat sheet + PDF: toque no link da bio\n\n"
           "FRAME 2 - FRASE-BOMBA\n"
           f'"{quote}"\n'
           f"- {book['author']}\n"
           "[caixa de perguntas] O que isso muda pra voce?\n"
           "-> O livro inteiro em 1 pagina, no acervo (link na bio)\n\n"
           "FRAME 3 - CTA (3 destinos)\n"
           "3 lugares, 1 toque:\n"
           "> Acervo - cheat sheet + PDF (de graca)\n"
           "> YouTube - o resumo em ~5 min\n"
           "> Amazon - o livro (link de afiliado)\n"
           "Tudo no link da bio. Salve e compartilhe.\n")
    (out / 'stories.txt').write_text(txt, encoding='utf-8')
    print('  stories.txt (roteiro de stories premium)')


def build_citacao(slug):
    data = importlib.import_module(slug.replace('-', '_') + '_data')
    book = data.BOOK
    quotes = _best_quotes(slug, book, data, want=5)
    if not quotes:
        sys.exit(f'[!] nenhuma frase forte encontrada para {slug}')
    total = len(quotes)
    slides = [_quote_card(q, book, k, total) for k, q in enumerate(quotes, 1)]
    out = _render(slides, OUT_ROOT / f'{slug}_citacoes')
    cap = _caption_citacao(slug, book, quotes)
    (out / 'caption.txt').write_text(cap, encoding='utf-8')
    print('  caption.txt (legenda com CTA Biblioteca + Amazon + disclosure)')
    _write_stories(out, slug, book, len(quotes), _strip_html(quotes[0]).rstrip(' .'))
    return out


# ---------- STORIES (9:16, 1080x1920) ----------
STORY_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;500;600;700;800;900&family=Literata:ital,opsz,wght@1,7..72,500;1,7..72,600&display=swap');
:root{
  --green: oklch(70% 0.13 152); --green-soft: oklch(85% 0.105 152);
  --ink: oklch(98% 0.008 152); --muted: oklch(75% 0.022 152);
  --bg: oklch(14.5% 0.014 152); --bg2: oklch(10.5% 0.012 152); --on-green: oklch(13% 0.02 152);
  --gold: oklch(76% 0.105 83); --hair: oklch(73% 0.05 152 / .30);
}
*{margin:0;padding:0;box-sizing:border-box}
body{background:#000;font-family:'Hanken Grotesk',system-ui,sans-serif;-webkit-font-smoothing:antialiased}
/* zona segura de story: conteudo no miolo (topo/rodape ~290px livres p/ UI do IG) */
.story{width:1080px;height:1920px;color:var(--ink);padding:300px 100px;display:flex;
  flex-direction:column;align-items:center;justify-content:center;text-align:center;
  position:relative;overflow:hidden;
  background:
   radial-gradient(120% 50% at 100% 104%, oklch(24% 0.045 152 / .85) 0%, transparent 44%),
   radial-gradient(110% 42% at 50% -4%, oklch(27% 0.05 152) 0%, transparent 54%),
   radial-gradient(140% 120% at 50% 50%, transparent 50%, oklch(5% 0.012 152 / .62) 100%),
   linear-gradient(178deg, var(--bg) 0%, var(--bg2) 100%);}
.story::before{content:'';position:absolute;inset:0;pointer-events:none;
  background-image:radial-gradient(oklch(78% 0.07 152 / .05) 1.1px, transparent 1.3px);
  background-size:38px 38px;background-position:center;
  -webkit-mask-image:radial-gradient(120% 88% at 50% 0%, #000 50%, transparent 100%);}
.story::after{content:'';position:absolute;inset:208px 60px;border:2px dashed var(--green);
  border-radius:40px;opacity:.32;pointer-events:none}
.story>*{position:relative;z-index:1}
.story>.ghost{position:absolute;font-family:'Hanken Grotesk';font-weight:900;line-height:.74;
  color:transparent;-webkit-text-stroke:2px oklch(74% 0.09 152 / .10);pointer-events:none;
  letter-spacing:-.05em;z-index:0;overflow:hidden;
  -webkit-mask-image:radial-gradient(120% 120% at 50% 50%, #000 60%, transparent 100%)}
/* wordmark de story = selo cheio + nome (assinatura forte do canal) */
.badge{position:absolute;top:218px;left:50%;transform:translateX(-50%);
  display:inline-flex;align-items:center;gap:16px;white-space:nowrap}
.badge .seal{width:58px;height:58px;border-radius:17px;display:flex;align-items:center;
  justify-content:center;background:var(--green);color:var(--on-green);flex:0 0 auto;
  box-shadow:0 10px 28px oklch(60% 0.14 152 / .4)}
.badge .seal svg{width:36px;height:36px;color:var(--on-green)}
.badge .name{font-weight:900;letter-spacing:.03em;font-size:38px;color:var(--ink);text-transform:uppercase}
.badge .name b{color:var(--green)}
.foot{position:absolute;bottom:236px;left:80px;right:80px;text-align:center}
.foot .tap{display:inline-flex;align-items:center;gap:14px;font-weight:800;font-size:36px;
  letter-spacing:.02em;color:var(--on-green);background:var(--green);padding:24px 46px;border-radius:999px;
  text-transform:uppercase;box-shadow:0 18px 54px oklch(60% 0.14 152 / .42)}
.foot .tap svg{width:40px;height:40px}
.foot .handle{display:block;margin-top:28px;font-weight:800;letter-spacing:.2em;font-size:25px;
  color:var(--muted);text-transform:uppercase}
/* teaser */
.eyebrow{font-size:31px;font-weight:800;letter-spacing:.2em;text-transform:uppercase;color:var(--muted)}
.st h1{font-size:158px;line-height:.9;font-weight:900;text-transform:uppercase;margin:34px 0 0;
  text-wrap:balance;letter-spacing:-.022em}
.st h1 .lt{color:var(--green);text-shadow:0 0 80px oklch(72% 0.14 152 / .42)}
.st h1 .bd{color:var(--ink)}
.st .hook{margin-top:60px;font-size:60px;font-weight:800;color:var(--ink);text-transform:uppercase;
  display:inline-flex;align-items:center;gap:26px;border-top:3px dashed var(--green);padding-top:46px}
.st .hook .num{font-size:140px;font-weight:900;color:var(--gold);line-height:.78;
  text-shadow:0 0 56px oklch(84% 0.12 92 / .38)}
/* quote */
.sq{align-items:flex-start;text-align:left}
.sq .qmark{font-family:'Literata',Georgia,serif;font-style:italic;font-weight:600;font-size:300px;
  line-height:.46;color:var(--green);height:150px;text-shadow:0 0 60px oklch(72% 0.14 152 / .35)}
.sq .phrase{font-size:88px;line-height:1.14;font-weight:800;color:var(--ink);margin-top:34px;
  text-wrap:balance;letter-spacing:-.014em}
.sq .phrase em{color:var(--green);font-style:normal}
.sq .attr{margin-top:60px;padding-top:38px;border-top:3px dashed var(--green);font-size:42px;
  color:var(--green-soft);font-weight:800}
.sq .attr .book{display:block;color:var(--muted);font-weight:600;font-style:italic;font-size:36px;margin-top:8px}
/* cta */
.sc .big{font-size:104px;line-height:.98;font-weight:900;text-transform:uppercase;letter-spacing:-.018em;text-wrap:balance}
.sc .big .lt{color:var(--green);text-shadow:0 0 60px oklch(72% 0.14 152 / .34)}
.sc .rows{display:flex;flex-direction:column;gap:0;margin-top:70px;width:100%}
.sc .row{display:flex;align-items:center;gap:32px;padding:38px 6px;text-align:left}
.sc .row + .row{border-top:2px dashed var(--hair)}
.sc .row .rico{flex:0 0 auto;width:92px;height:92px;border-radius:22px;display:flex;align-items:center;
  justify-content:center;background:oklch(70% 0.14 152 / .12);border:2px solid var(--hair);color:var(--green)}
.sc .row .rico svg{width:52px;height:52px}
.sc .row p{font-size:50px;font-weight:800;color:var(--ink);line-height:1.05}
.sc .row p span{display:block;font-size:33px;color:var(--muted);font-weight:600;margin-top:6px;text-transform:none;letter-spacing:0}
"""


def _story(inner, cls='', ghost=''):
    return f'<div class="story {cls}">{ghost}{inner}</div>'


def _story_teaser(book, n):
    return _story(
        f'<div class="badge"><span class="seal">{_svg("book")}</span>'
        f'<span class="name">Minuto<b>Real</b></span></div>'
        '<div class="eyebrow">novo · resumo da semana</div>'
        f'<h1><span class="lt">{book["header_light"]}</span><br>'
        f'<span class="bd">{book["header_bold"]}</span></h1>'
        f'<div class="hook"><span class="num">{n}</span> ideias que ficam</div>'
        f'<div class="foot"><span class="tap">toque no link da bio {_svg("arrow")}</span>'
        '<span class="handle">@minutoreal1701</span></div>',
        'st', ghost=_ghost('top:430px;right:70px;font-size:440px', f'{n}'))


def _story_quote(quote, book):
    return _story(
        '<div class="qmark">&ldquo;</div>'
        f'<div class="phrase">{_emph(quote)}</div>'
        f'<div class="attr">{book["author"]}<span class="book">{book["title"]}</span></div>'
        f'<div class="foot"><span class="tap">resumo no YouTube {_svg("play")}</span>'
        '<span class="handle">link na bio</span></div>',
        'sq', ghost=_ghost('bottom:330px;right:40px;font-size:420px', '&rdquo;'))


def _story_cta(book):
    return _story(
        '<div class="big">tudo em<br><span class="lt">1 toque</span></div>'
        '<div class="rows">'
        f'<div class="row"><span class="rico">{_svg("shelf")}</span>'
        '<p>Acervo<span>cheat sheet + PDF (de graça)</span></p></div>'
        f'<div class="row"><span class="rico">{_svg("play")}</span>'
        '<p>YouTube<span>o resumo em ~5 min</span></p></div>'
        f'<div class="row"><span class="rico">{_svg("spark")}</span>'
        '<p>Amazon<span>o livro (link de afiliado)</span></p></div>'
        '</div>'
        f'<div class="foot"><span class="tap">link na bio {_svg("arrow")}</span>'
        '<span class="handle">@minutoreal1701</span></div>',
        'sc', ghost=_ghost('top:430px;left:60px;font-size:400px', '+'))


def build_stories(slug):
    data = importlib.import_module(slug.replace('-', '_') + '_data')
    book = data.BOOK
    cards = book.get('overview_cards') or (data.CHAPTERS[0]['cards'])
    n = len(cards)
    qs = _best_quotes(slug, book, data, want=1)
    quote = _strip_html(qs[0]).rstrip(' .') if qs else book.get('subtitle', '')
    frames = [_story_teaser(book, n), _story_quote(quote, book), _story_cta(book)]
    out = _render(frames, OUT_ROOT / f'{slug}_stories', w=1080, h=1920, css=STORY_CSS)
    _write_stories(out, slug, book, n, quote)   # roteiro de texto p/ figurinhas manuais
    return out


if __name__ == '__main__':
    args = sys.argv[1:]
    if not args:
        sys.exit('uso: python gerar_carrossel.py <slug> [--cap chNN-... | --citacao | --stories]')
    slug = args[0]
    if '--citacao' in args:
        build_citacao(slug)
    elif '--stories' in args:
        build_stories(slug)
    else:
        cap = args[args.index('--cap') + 1] if '--cap' in args else None
        build(slug, cap)
