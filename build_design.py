# -*- coding: utf-8 -*-
"""Monta a pagina /biblioteca/design como COMPARACAO de estilos lado a lado.
Le videos/_premium/<slug>/<estilo>/01..06.png (cada direcao de arte) + mapa.png,
gera JPGs web e um index que mostra, por peca, todas as versoes para comparar.
Cresce sozinha quando novos estilos forem gerados. Deploy via scp."""
import shutil
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent
SLUG = '48-leis-do-poder'
SRC = ROOT / 'videos' / '_premium' / SLUG
OUT = ROOT / 'design'

PIECES = [('01', '① Capa'), ('02', '② Natureza do Poder'), ('03', '③ Aparências'),
          ('04', '④ Sedução'), ('05', '⑤ Lei Suprema'), ('06', '⑥ CTA')]
LABELS = {'vivido': 'Vívido · claro', 'morbido': 'Mórbido · sombrio'}
ORDER = ['vivido', 'morbido']

styles = sorted([d.name for d in SRC.iterdir() if d.is_dir() and (d / '01.png').exists()],
                key=lambda s: ORDER.index(s) if s in ORDER else 99)

if OUT.exists():
    shutil.rmtree(OUT)
OUT.mkdir()


def _web(png, jpg):
    im = Image.open(png).convert('RGB')
    w = 760
    h = int(im.height * w / im.width)
    im.resize((w, h), Image.LANCZOS).save(jpg, 'JPEG', quality=86, optimize=True)


for st in styles:
    (OUT / st).mkdir()
    for idx, _ in PIECES:
        _web(SRC / st / f'{idx}.png', OUT / st / f'{idx}.jpg')
if (SRC / 'mapa.png').exists():
    _web(SRC / 'mapa.png', OUT / 'mapa.jpg')

sections = []
for idx, label in PIECES:
    cols = ''.join(
        f'''        <figure class="v"><a href="{st}/{idx}.jpg" target="_blank"><img src="{st}/{idx}.jpg" loading="lazy" alt="{label} {st}"></a>
          <figcaption>{LABELS.get(st, st)}</figcaption></figure>''' for st in styles)
    sections.append(f'''    <section class="piece">
      <h2>{label}</h2>
      <div class="versions">
{cols}
      </div>
    </section>''')

mapa_html = ''
if (SRC / 'mapa.png').exists():
    mapa_html = '''    <section class="piece">
      <h2>⑦ Mapa do Livro <span class="note">(escuro · fiel à referência u05)</span></h2>
      <div class="versions one">
        <figure class="v"><a href="mapa.jpg" target="_blank"><img src="mapa.jpg" loading="lazy" alt="Mapa do Livro"></a>
          <figcaption>field-guide</figcaption></figure>
      </div>
    </section>'''

chips = ' · '.join(f'<b>{LABELS.get(s, s)}</b>' for s in styles)
html = f'''<!doctype html>
<html lang="pt-BR"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>Minuto Real — Comparação de estilos (48 Leis)</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@500;700;800;900&family=Literata:ital,wght@0,400;1,500&display=swap" rel="stylesheet">
<style>
  :root{{--green:#22d18a;--bg:#06090c;--bg2:#0b1014;--ink:#eef2f0;--muted:#9aa6a0;--hair:rgba(60,200,140,.22)}}
  *{{margin:0;padding:0;box-sizing:border-box}}
  body{{background:var(--bg);color:var(--ink);font-family:'Hanken Grotesk',system-ui,sans-serif;-webkit-font-smoothing:antialiased}}
  .wrap{{max-width:1240px;margin:0 auto;padding:46px 22px 90px}}
  header{{text-align:center;margin-bottom:30px;border-bottom:1px dashed var(--hair);padding-bottom:28px}}
  .tag{{display:inline-block;font-weight:800;font-size:13px;letter-spacing:.16em;text-transform:uppercase;color:var(--green);
    border:1px solid var(--hair);border-radius:999px;padding:7px 16px;margin-bottom:16px}}
  h1{{font-size:clamp(28px,5vw,46px);font-weight:900;letter-spacing:-.02em}} h1 em{{font-style:normal;color:var(--green)}}
  .sub{{font-family:'Literata',serif;font-style:italic;color:var(--muted);font-size:clamp(15px,2.4vw,20px);margin-top:12px}}
  .piece{{margin-top:40px}}
  .piece h2{{font-size:20px;font-weight:800;margin-bottom:14px;color:var(--ink)}}
  .piece h2 .note{{font-weight:500;font-size:14px;color:var(--muted)}}
  .versions{{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:22px}}
  .versions.one{{grid-template-columns:minmax(300px,420px)}}
  .v{{background:var(--bg2);border:1px solid var(--hair);border-radius:14px;overflow:hidden;transition:transform .15s,border-color .15s}}
  .v:hover{{transform:translateY(-3px);border-color:var(--green)}}
  .v img{{width:100%;display:block;background:#000}}
  figcaption{{padding:11px 14px;font-weight:800;font-size:14px;letter-spacing:.04em;text-transform:uppercase;color:var(--green)}}
  footer{{text-align:center;color:var(--muted);font-size:13px;margin-top:54px}}
  a{{color:inherit;text-decoration:none}}
</style></head>
<body><div class="wrap">
  <header>
    <span class="tag">Comparação de estilos · revisão</span>
    <h1>As 48 Leis do <em>Poder</em></h1>
    <div class="sub">Cada peça em cada direção de arte — clique para abrir em alta. Versões atuais: {chips}.</div>
  </header>
{chr(10).join(sections)}
{mapa_html}
  <footer>@minutoreal1701 · <b style="color:var(--green)">Minuto Real</b> — nada é sobrescrito; novos estilos entram aqui pra comparar.</footer>
</div></body></html>'''

(OUT / 'index.html').write_text(html, encoding='utf-8')
print('OK -> design/ estilos:', styles)
total = sum(1 for _ in OUT.rglob('*.jpg'))
print('  imagens web:', total, '| index.html', round((OUT / 'index.html').stat().st_size / 1024), 'KB')
