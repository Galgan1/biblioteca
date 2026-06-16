# -*- coding: utf-8 -*-
"""Monta a pagina de galeria /biblioteca/design (HTML + imagens web) com as pecas
premium para revisao no navegador. Saida: design/ (deploy via scp para a VPS)."""
import shutil
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent
SRC = ROOT / 'videos' / '_premium' / '48-leis-do-poder'
OUT = ROOT / 'design'
if OUT.exists():
    shutil.rmtree(OUT)
OUT.mkdir()

PIECES = [
    ('01.png', 'Capa', 'Cena cinematográfica + título + “N ideias” + arrasta'),
    ('02.png', 'Conceito · A Natureza do Poder', 'Ilustração simbólica + caixa “Modelo mental”'),
    ('03.png', 'Conceito · Domine as Aparências', 'Máscara + espelho (corrigida, sem texto borrado)'),
    ('04.png', 'Conceito · Sedução, Audácia e Timing', 'Figura encapuzada + a rosa'),
    ('05.png', 'Conceito · A Lei Suprema', 'Figura de energia + símbolos'),
    ('06.png', 'CTA', 'Livro brilhando + “Gostou? tem mais” + salve'),
    ('mapa.png', 'Mapa do Livro', 'Field-guide multicor + mini-ilustrações + neon'),
]

cards = []
for f, title, sub in PIECES:
    jpg = f.replace('.png', '.jpg')
    im = Image.open(SRC / f).convert('RGB')
    w = 1080
    h = int(im.height * w / im.width)
    im.resize((w, h), Image.LANCZOS).save(OUT / jpg, 'JPEG', quality=88, optimize=True)
    cards.append(f'''      <figure class="card">
        <a href="{jpg}" target="_blank"><img src="{jpg}" loading="lazy" alt="{title}"></a>
        <figcaption><b>{title}</b><span>{sub}</span></figcaption>
      </figure>''')

html = f'''<!doctype html>
<html lang="pt-BR"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>Minuto Real — Padrão Premium (As 48 Leis do Poder)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@500;700;800;900&family=Literata:ital,opsz,wght@0,400;0,600;1,500&display=swap" rel="stylesheet">
<style>
  :root{{--green:#22d18a;--bg:#06090c;--bg2:#0b1014;--ink:#eef2f0;--muted:#9aa6a0;--hair:rgba(60,200,140,.22)}}
  *{{margin:0;padding:0;box-sizing:border-box}}
  body{{background:var(--bg);color:var(--ink);font-family:'Hanken Grotesk',system-ui,sans-serif;-webkit-font-smoothing:antialiased}}
  .wrap{{max-width:1180px;margin:0 auto;padding:48px 22px 80px}}
  header{{text-align:center;margin-bottom:38px;border-bottom:1px dashed var(--hair);padding-bottom:34px}}
  .tag{{display:inline-block;font-weight:800;font-size:13px;letter-spacing:.18em;text-transform:uppercase;color:var(--green);
    border:1px solid var(--hair);border-radius:999px;padding:7px 16px;margin-bottom:18px}}
  h1{{font-size:clamp(30px,5vw,52px);font-weight:900;line-height:1.02;letter-spacing:-.02em}}
  h1 em{{font-style:normal;color:var(--green)}}
  .sub{{font-family:'Literata',serif;font-style:italic;color:var(--muted);font-size:clamp(16px,2.4vw,21px);margin-top:14px}}
  .grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:26px;margin-top:8px}}
  .card{{background:var(--bg2);border:1px solid var(--hair);border-radius:16px;overflow:hidden;transition:transform .15s,border-color .15s}}
  .card:hover{{transform:translateY(-3px);border-color:var(--green)}}
  .card img{{width:100%;display:block;background:#000}}
  figcaption{{padding:14px 16px 16px}}
  figcaption b{{display:block;font-weight:800;font-size:17px}}
  figcaption span{{display:block;color:var(--muted);font-size:14px;margin-top:3px;line-height:1.35}}
  footer{{text-align:center;color:var(--muted);font-size:13px;margin-top:48px;letter-spacing:.04em}}
  footer b{{color:var(--green)}}
  a{{color:inherit;text-decoration:none}}
</style></head>
<body><div class="wrap">
  <header>
    <span class="tag">Padrão premium · revisão</span>
    <h1>As 48 Leis do <em>Poder</em></h1>
    <div class="sub">7 peças geradas com IA de imagem (Imagen 4.0) + composição da marca — clique para abrir em alta.</div>
  </header>
  <div class="grid">
{chr(10).join(cards)}
  </div>
  <footer>@minutoreal1701 · <b>Minuto Real</b> — gerado por gerar_premium.py + gerar_mapa.py</footer>
</div></body></html>'''

(OUT / 'index.html').write_text(html, encoding='utf-8')
print('OK -> design/ com', len(PIECES), 'imagens + index.html')
for p in sorted(OUT.iterdir()):
    print('  ', p.name, round(p.stat().st_size / 1024), 'KB')
