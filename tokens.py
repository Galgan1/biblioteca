# -*- coding: utf-8 -*-
"""Fonte ÚNICA de tokens de design do Kit de Divulgação (fontes + cores da marca).

Todo gerador de peça (carrossel, infográfico, citação, thumb...) deve começar seu
CSS com `tokens.TOKENS`, para a marca NÃO derivar entre peças. Diretor de Design:
"três peças bonitas viram um sistema quando partilham os mesmos tokens."
"""

# Fontes: Hanken Grotesk (display/sans) + Literata (serifa editorial — romana E itálica).
FONTS = (
    "@import url('https://fonts.googleapis.com/css2?"
    "family=Hanken+Grotesk:wght@400;500;600;700;800;900&"
    "family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,500;0,7..72,600;0,7..72,700;"
    "1,7..72,400;1,7..72,500;1,7..72,600&display=swap');"
)

# Cores da marca (verde h152 + acentos), em oklch.
ROOT = """:root{
  --green: oklch(70% 0.13 152); --green-soft: oklch(85% 0.105 152); --green-deep: oklch(56% 0.14 152);
  --ink: oklch(98% 0.008 152); --muted: oklch(75% 0.022 152); --ink-dim: oklch(64% 0.02 152);
  --bg: oklch(14.5% 0.014 152); --bg2: oklch(10.5% 0.012 152); --on-green: oklch(13% 0.02 152);
  --gold: oklch(76% 0.105 83);
  --warn: oklch(72% 0.16 30); --on-warn: oklch(16% 0.03 30);
  --hair: oklch(73% 0.05 152 / .30); --hair2: oklch(73% 0.05 152 / .14);
}"""

TOKENS = FONTS + "\n" + ROOT
