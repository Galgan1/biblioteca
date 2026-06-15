# -*- coding: utf-8 -*-
"""marca.py — Fonte UNICA de verdade do design da rede Minuto Real / Biblioteca.

Todo gerador (site, carrossel, video, thumbnail, arte de canal) le os tokens daqui
em vez de hardcodar cor e fonte. Decisao de marca (14/jun/2026):
  - VERDE (hue 152) lidera — e a cor-mae da Biblioteca.
  - UM OURO (hue 83, ancorado no ambar #d8a64a, ja com equity no YouTube) e o
    UNICO acento premium, e passa a existir tambem no site.
  - Tipografia unica: Hanken Grotesk (display) + Literata (serif/editorial).

Consumo:
  CSS (site, carrossel)  ->  marca.css_root('dark' | 'light')
  Pillow (video, thumb)  ->  marca.rgb('ouro'),  marca.font('display', 120, 'Black')

Fontes em _fonts/ (variaveis, OFL, Google Fonts). Se faltarem, o font() cai de
forma graciosa nas fontes do Windows — o pipeline nunca quebra por causa disso.
"""
from pathlib import Path

DIR = Path(__file__).parent
FONTS = DIR / '_fonts'

# ---------------------------------------------------------------------------
# PALETA  ·  hue 152 = verde-mae   ·   hue 83 = ouro (acento UNICO, #d8a64a)
# Cada token:  (oklch claro,  oklch escuro,  hex p/ Pillow no canvas escuro)
# ---------------------------------------------------------------------------
TOKENS = {
    'verde':       ('oklch(52% 0.14 152)',  'oklch(70% 0.13 152)',  '#3faf76'),
    'verde-deep':  ('oklch(40% 0.12 152)',  'oklch(76% 0.11 152)',  '#5cc28a'),
    'verde-soft':  ('oklch(95% 0.03 152)',  'oklch(28% 0.04 152)',  '#a9e6c4'),  # matches --green-light in style.css
    'ouro':        ('oklch(60% 0.10 83)',   'oklch(76% 0.105 83)',  '#d8a64a'),
    'ouro-soft':   ('oklch(72% 0.09 83)',   'oklch(86% 0.075 83)',  '#ecca8c'),
    'alerta':      ('oklch(55% 0.17 30)',   'oklch(72% 0.16 30)',   '#e8744f'),
    'tinta':       ('oklch(22% 0.01 152)',  'oklch(95% 0.01 152)',  '#f2f2f5'),
    'tinta-fraca': ('oklch(46% 0.01 152)',  'oklch(72% 0.01 152)',  '#9aa0a2'),
    'papel':       ('oklch(99% 0.002 152)', 'oklch(16% 0.01 152)',  '#08080c'),
}

# token -> nome canonico da variavel CSS (vocabulario do site — style.css e fonte de verdade)
_CSS_VARMAP = {
    'verde':       '--green',
    'verde-deep':  '--green-dark',    # site usa --green-dark (semantico)
    'verde-soft':  '--green-light',   # site usa --green-light
    'ouro':        '--gold',
    'ouro-soft':   '--gold-soft',
    'alerta':      '--dislike',       # site usa --dislike (contexto de voto)
    'tinta':       '--black',         # site usa --black
    'tinta-fraca': '--gray-dark',     # site usa --gray-dark
    'papel':       '--paper-bg',      # site usa --paper-bg
}

# ---------------------------------------------------------------------------
# TIPOGRAFIA
# ---------------------------------------------------------------------------
_FONT_FILES = {'display': FONTS / 'HankenGrotesk.ttf', 'serif': FONTS / 'Literata.ttf'}
_FALLBACK = {'display': 'C:/Windows/Fonts/arialbd.ttf', 'serif': 'C:/Windows/Fonts/georgia.ttf'}


def font(role, size, weight='SemiBold'):
    """Fonte da marca p/ Pillow. role: 'display' (Hanken) | 'serif' (Literata).
    weight: Thin/ExtraLight/Light/Regular/Medium/SemiBold/Bold/ExtraBold/Black."""
    from PIL import ImageFont
    path = _FONT_FILES.get(role)
    if path and path.exists():
        ft = ImageFont.truetype(str(path), size)
        try:
            ft.set_variation_by_name(weight)
        except Exception:
            pass
        return ft
    return ImageFont.truetype(_FALLBACK.get(role, _FALLBACK['display']), size)


# ---------------------------------------------------------------------------
# CONSUMO POR PILLOW (canvas escuro)
# ---------------------------------------------------------------------------
def hex_of(name):
    return TOKENS[name][2]


def rgb(name):
    h = TOKENS[name][2].lstrip('#')
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


# ---------------------------------------------------------------------------
# CONSUMO POR CSS (site, carrossel)
# ---------------------------------------------------------------------------
def css_root(mode='dark'):
    """Bloco :root{} canonico. mode='dark' (carrossel/video) ou 'light' (site claro)."""
    i = 1 if mode == 'dark' else 0
    decls = '\n'.join(f'  {var}: {TOKENS[tok][i]};' for tok, var in _CSS_VARMAP.items())
    fonts = ("  --font-display: 'Hanken Grotesk', system-ui, sans-serif;\n"
             "  --font-serif: 'Literata', Georgia, serif;")
    return f':root{{\n{decls}\n{fonts}\n}}'


if __name__ == '__main__':
    print(css_root('dark'))
    print('\nouro rgb ->', rgb('ouro'), '| verde rgb ->', rgb('verde'))
    print('font display Black ->', font('display', 120, 'Black').getname())
