# -*- coding: utf-8 -*-
"""Renderiza um template do kit (HTML) em PNG na resolução-alvo, via Playwright
(escala 2x, igual ao carrossel). Uso: python _kit_preview/render.py quote.html 1984-citacao 1080 1350
"""
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

HERE = Path(__file__).parent
src = HERE / sys.argv[1]
out_name = sys.argv[2]
W, H = int(sys.argv[3]), int(sys.argv[4])
out = HERE / f'{out_name}.png'

with sync_playwright() as p:
    b = p.chromium.launch()
    page = b.new_page(viewport={'width': W, 'height': H}, device_scale_factor=2)
    page.goto(src.as_uri(), wait_until='networkidle')
    page.evaluate('document.fonts.ready')
    el = page.query_selector('.slide')
    el.screenshot(path=str(out))
    b.close()

kb = out.stat().st_size // 1024
print(f'OK {out.name}  {W}x{H} @2x  ({kb}KB)')
