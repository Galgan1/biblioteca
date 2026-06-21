# -*- coding: utf-8 -*-
"""PROOF — slide PREMIUM (no nivel das referencias u02/u03/u04 do usuario):
ilustracao cinematografica gerada por IA (videos/imagen.py = Google Imagen 4.0)
+ composicao da marca por cima (wordmark, titulo serifa, caixa de takeaway, cromo).

NAO e producao — e a prova de direcao. Gera 1 imagem (1 chamada Imagen).
Saida: videos/_premium/<slug>_<n>.png
"""
import sys, base64
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / 'videos'))
import imagen

OUT = ROOT / 'videos' / '_premium'
OUT.mkdir(parents=True, exist_ok=True)
FONTS = ROOT / '_fonts'
W, H = 1080, 1350


def _b64(p):
    return base64.b64encode(Path(p).read_bytes()).decode('ascii')


def _font_face():
    faces = []
    for fam, fn in (('Hanken Grotesk', 'HankenGrotesk.ttf'), ('Literata', 'Literata.ttf')):
        p = FONTS / fn
        if p.exists():
            faces.append(f"@font-face{{font-family:'{fam}';font-weight:100 900;font-display:block;"
                         f"src:url(data:font/ttf;base64,{_b64(p)}) format('truetype')}}")
    return '\n'.join(faces)


# ----- a peca-proof: capitulo 1 das 48 Leis (mesmo conteudo do u02/site) -----
PROMPT = (
    "Cinematic painterly digital illustration, opulent baroque palace court at night, "
    "silhouetted aristocrats and courtiers conversing and scheming under warm candlelight, "
    "dramatic chiaroscuro lighting, deep emerald green and antique gold color palette, "
    "drifting smoke and deep shadow, mysterious atmosphere of power and intrigue, "
    "rich texture and detail, dark moody empty negative space in the lower half for text, "
    "premium editorial book-summary cover art, masterpiece, no text, no words, no letters"
)

EYEBROW = "AS 48 LEIS DO PODER"
SOURCE = "Capítulo 1 · A Natureza do Poder"
TITLE_LT = "Toda mesa"
TITLE_BD = "tem um jogo"
TAKE_LABEL = "Modelo mental"
TAKE_BODY = ("Antes de reagir, leia a jogada — <b>toda interação carrega uma "
             "camada de poder</b>, mesmo a mais cordial.")


def compose(art_png, out_png):
    css = """
__FF__
*{margin:0;padding:0;box-sizing:border-box}
.slide{width:1080px;height:1350px;position:relative;overflow:hidden;font-family:'Hanken Grotesk',sans-serif;background:#05070a}
.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
/* scrim p/ legibilidade (topo e base), no DNA das capas de Reel */
.scrim{position:absolute;inset:0;background:
  linear-gradient(180deg, rgba(5,9,8,.78) 0%, rgba(5,9,8,.05) 26%, rgba(5,9,8,.02) 46%, rgba(5,9,8,.72) 74%, rgba(5,9,8,.94) 100%)}
.frame{position:absolute;inset:34px;border:2px dashed oklch(80% 0.12 152 / .42);border-radius:30px;pointer-events:none}
.wrap{position:absolute;inset:0;padding:74px 76px 70px;display:flex;flex-direction:column;color:#f3f5f4}
.top{display:flex;justify-content:space-between;align-items:center}
.brand{display:inline-flex;align-items:center;gap:12px;font-weight:900;letter-spacing:.04em;font-size:27px;text-transform:uppercase}
.brand .seal{width:46px;height:46px;border-radius:13px;display:flex;align-items:center;justify-content:center;
  background:oklch(72% 0.16 152);color:#06140d;box-shadow:0 8px 26px rgba(0,0,0,.5)}
.brand .seal svg{width:27px;height:27px}
.brand b{color:oklch(82% 0.14 152)}
.tag{font-weight:800;font-size:20px;letter-spacing:.14em;text-transform:uppercase;color:oklch(86% 0.10 152);
  border:1.5px solid oklch(80% 0.12 152 / .4);border-radius:999px;padding:9px 20px;background:rgba(8,20,14,.5);backdrop-filter:blur(4px)}
.spacer{flex:1 1 auto}
.src{font-family:'Literata',serif;font-weight:600;font-size:30px;color:oklch(88% 0.07 152);letter-spacing:.01em;margin-bottom:8px;
  text-shadow:0 2px 16px rgba(0,0,0,.8)}
.src b{color:oklch(84% 0.13 152)}
h1{font-family:'Literata',serif;font-weight:600;font-size:104px;line-height:.98;letter-spacing:-.01em;text-shadow:0 4px 30px rgba(0,0,0,.85)}
h1 .lt{color:#fff} h1 .bd{color:oklch(84% 0.14 152);font-style:italic}
.take{margin-top:34px;display:flex;gap:22px;align-items:flex-start;
  border:1.5px solid oklch(80% 0.12 152 / .3);border-left:5px solid oklch(76% 0.105 83);border-radius:20px;
  padding:26px 30px;background:rgba(6,12,10,.62);backdrop-filter:blur(7px);box-shadow:0 18px 50px rgba(0,0,0,.5)}
.take .ic{flex:0 0 auto;width:58px;height:58px;border-radius:15px;display:flex;align-items:center;justify-content:center;
  background:oklch(76% 0.105 83);color:#1a1205}
.take .ic svg{width:36px;height:36px}
.take .lbl{font-weight:900;font-size:20px;letter-spacing:.18em;text-transform:uppercase;color:oklch(80% 0.10 83)}
.take p{font-size:29px;line-height:1.28;color:#eef2f0;font-weight:500;margin-top:5px}
.take p b{color:oklch(86% 0.12 152);font-weight:800}
.hand{position:absolute;left:0;right:0;bottom:40px;text-align:center;font-weight:800;letter-spacing:.26em;
  font-size:19px;color:oklch(78% 0.04 152 / .8);text-transform:uppercase}
"""
    book_svg = ('<svg viewBox="0 0 64 64" fill="none"><path d="M12 14h18a6 6 0 016 6v30a6 6 0 00-6-6H12z" '
                'stroke="currentColor" stroke-width="3" stroke-linejoin="round"/><path d="M52 14H34a6 6 0 00-6 6v30a6 6 0 016-6h18z" '
                'stroke="currentColor" stroke-width="3" stroke-linejoin="round"/></svg>')
    spark = ('<svg viewBox="0 0 64 64" fill="none"><path d="M32 10l5 17 17 5-17 5-5 17-5-17-17-5 17-5z" '
             'stroke="currentColor" stroke-width="3" stroke-linejoin="round"/></svg>')
    html = (
        '<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>'
        + css.replace('__FF__', _font_face()) +
        '</style></head><body><div class="slide">'
        f'<img class="bg" src="data:image/png;base64,{_b64(art_png)}">'
        '<div class="scrim"></div><div class="frame"></div>'
        '<div class="wrap">'
        f'<div class="top"><span class="brand"><span class="seal">{book_svg}</span>MINUTO<b>REAL</b></span>'
        f'<span class="tag">{EYEBROW}</span></div>'
        '<div class="spacer"></div>'
        f'<div class="src">{SOURCE}</div>'
        f'<h1><span class="lt">{TITLE_LT}</span> <span class="bd">{TITLE_BD}</span></h1>'
        f'<div class="take"><span class="ic">{spark}</span><div>'
        f'<div class="lbl">{TAKE_LABEL}</div><p>{TAKE_BODY}</p></div></div>'
        '</div>'
        '<div class="hand">@minutoreal1701 · o livro em 1 página</div>'
        '</div></body></html>')

    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={'width': W, 'height': H}, device_scale_factor=2)
        pg.set_content(html, wait_until='networkidle')
        pg.evaluate('document.fonts.ready')
        pg.wait_for_timeout(400)
        pg.query_selector('.slide').screenshot(path=str(out_png))
        b.close()
    print('OK ->', out_png)


if __name__ == '__main__':
    art = OUT / '48-leis_art.png'
    print('Gerando ilustracao via Imagen 4.0 (3:4)...')
    m = imagen.gen(PROMPT, str(art), aspect='3:4')
    if not m:
        sys.exit('FALHOU a geracao da imagem (cheque .secrets/imagen_api_key.txt / cota).')
    print('arte:', m)
    compose(str(art), str(OUT / '48-leis_premium.png'))
