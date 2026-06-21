# -*- coding: utf-8 -*-
"""QC do carrossel: renderiza capa + slides de conceito do 1o capitulo de cada
slug dado, usando os dados emitidos (slides.json + _carousel.css) e a MESMA
receita do gerar_carrossel._render (shrink de titulo incluso). Reusa 1 navegador.

Uso: python _kit_preview/qc_render.py <slug> [slug2 ...]
Saida: _kit_preview/_qc/<slug>/00-capa.png, 01.png, 02.png ...  (pula o CTA, que e fixo)
"""
import json, sys
from pathlib import Path
from playwright.sync_api import sync_playwright

BASE = Path(__file__).resolve().parent.parent
KIT = BASE / 'assets' / 'kit'
QC = Path(__file__).resolve().parent / '_qc'
CSS = (KIT / '_carousel.css').read_text(encoding='utf-8')
SHRINK = """() => {
  for (const el of document.querySelectorAll('.cover h1, .st h1')) {
    const box = el.parentElement, cs = getComputedStyle(box);
    const avail = box.clientWidth - parseFloat(cs.paddingLeft) - parseFloat(cs.paddingRight);
    let fs = parseFloat(getComputedStyle(el).fontSize), g = 0;
    while (el.getBoundingClientRect().width > avail && fs > 50 && g < 120) { fs -= 3; el.style.fontSize = fs+'px'; g++; }
  }
  for (const slide of document.querySelectorAll('.slide.concept')) {
    const body = slide.querySelector('.ed-body'); if (!body) continue;
    const last = slide.querySelector('.ed-tip') || body;
    const safeBottom = slide.getBoundingClientRect().bottom - 128;
    let fs = parseFloat(getComputedStyle(body).fontSize), g = 0;
    while (last.getBoundingClientRect().bottom > safeBottom && fs > 40 && g < 80) { fs -= 1; body.style.fontSize = fs+'px'; g++; }
  }
}"""

slugs = sys.argv[1:]
with sync_playwright() as p:
    b = p.chromium.launch()
    for slug in slugs:
        try:
            sj = json.loads((KIT / slug / 'slides.json').read_text(encoding='utf-8'))
        except Exception as e:
            print(f'{slug}: SEM slides.json ({e})'); continue
        chapters = sj.get('chapters', {})
        if not chapters:
            print(f'{slug}: sem capitulos'); continue
        cap = next(iter(chapters))
        slides = chapters[cap]
        # capa (0) + conceitos (1..n-2); pula o CTA (ultimo, fixo)
        keep = [slides[0]] + slides[1:-1]
        html = f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{"".join(keep)}</body></html>'
        out = QC / slug
        out.mkdir(parents=True, exist_ok=True)
        pg = b.new_page(viewport={'width': 1080, 'height': 1350}, device_scale_factor=1)
        pg.set_content(html, wait_until='networkidle')
        pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(300); pg.evaluate(SHRINK)
        els = pg.query_selector_all('.slide')
        names = ['00-capa'] + [f'{i:02d}' for i in range(1, len(els))]
        for el, nm in zip(els, names):
            el.screenshot(path=str(out / f'{nm}.png'))
        pg.close()
        print(f'{slug}: {len(els)} slides ({cap})')
    b.close()
print('qc done')
