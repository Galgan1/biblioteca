# -*- coding: utf-8 -*-
"""Teste de OVERFLOW do carrossel (Akita: verde = nada estoura).

Renderiza (Playwright real) slides-estresse com conteúdo deliberadamente longo
(citação e corpo) usando o CSS real do carrossel, e prova num único teste o
ciclo red->green: ANTES do _FIT_JS há overflow; DEPOIS, zero. Pula com elegância
se Playwright/Chromium não estiver disponível (ex.: CI sem browser)."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]  # .../biblioteca
sys.path.insert(0, str(ROOT))

try:
    from playwright.sync_api import sync_playwright
    import gerar_carrossel as gc
    with sync_playwright() as _p:
        _b = _p.chromium.launch()
        _b.close()
    _OK = True
except Exception:
    _OK = False

# Mede quantos slides têm o texto mais baixo ALÉM da margem segura (= padding-bottom).
# Mesmo critério do _FIT_JS, para que "depois" baixe a zero.
_OVERFLOW_JS = """() => {
  const SHRINK = '.ed-title,.ed-body,.ed-tip .tipbody,.phrase,.cta .big,.cta .row p,.cta .save,.card-title,.card-body,.card-tip';
  let n = 0;
  for (const slide of document.querySelectorAll('.slide, .story')) {
    const padB = parseFloat(getComputedStyle(slide).paddingBottom) || 110;
    const safe = slide.getBoundingClientRect().bottom - Math.max(padB, 40);
    let m = 0;
    for (const el of slide.querySelectorAll(SHRINK)) { const r = el.getBoundingClientRect(); if (r.height > 0) m = Math.max(m, r.bottom); }
    if (m > safe + 1) n++;
  }
  return n;
}"""


def _slides_estresse():
    frase = ' '.join(['liberdade'] * 60)
    corpo = ' '.join(['vigilancia'] * 150)
    quote = f'<div class="slide quote"><div class="phrase">{frase}.</div></div>'
    concept = ('<div class="slide concept"><div class="ed-title">Titulo de teste</div>'
               f'<div class="ed-body">{corpo}.</div></div>')
    return quote + concept


@unittest.skipUnless(_OK, 'playwright/chromium/gerar_carrossel indisponivel')
class TestCarouselFit(unittest.TestCase):
    def test_fit_elimina_overflow(self):
        html = (f'<!doctype html><html><head><meta charset="utf-8"><style>{gc.CSS}</style>'
                f'</head><body>{_slides_estresse()}</body></html>')
        with sync_playwright() as p:
            b = p.chromium.launch()
            pg = b.new_page(viewport={'width': 1080, 'height': 1350}, device_scale_factor=1)
            pg.set_content(html, wait_until='domcontentloaded')
            pg.wait_for_timeout(400)
            antes = pg.evaluate(_OVERFLOW_JS)
            pg.evaluate(gc._FIT_JS)
            depois = pg.evaluate(_OVERFLOW_JS)
            b.close()
        # red: o estresse precisa estourar antes (senao o teste nao prova nada)
        self.assertGreater(antes, 0, 'os slides-estresse deveriam estourar ANTES do fit')
        # green: o fit precisa zerar o overflow
        self.assertEqual(depois, 0, f'o _FIT_JS deveria eliminar o overflow (sobraram {depois})')


if __name__ == '__main__':
    unittest.main()
