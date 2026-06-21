# -*- coding: utf-8 -*-
"""Fonte ÚNICA de tokens de design do Kit de Divulgação (fontes + cores da marca).

Todo gerador de peça (carrossel, infográfico, citação, thumb...) deve começar seu
CSS com `tokens.TOKENS`, para a marca NÃO derivar entre peças. Diretor de Design:
"três peças bonitas viram um sistema quando partilham os mesmos tokens."

A espinha da marca (verde h152 · ouro h83 · alerta h30) DERIVA de marca.py — a
fonte única da rede. Os demais tons (fundos, tintas e os pares on-*) são a paleta
DARK específica do Kit; ficam aqui (candidatos a subir para marca.py no futuro).
"""
import marca

# Fontes: Hanken Grotesk (display/sans) + Literata (serifa editorial — romana E itálica).
FONTS = (
    "@import url('https://fonts.googleapis.com/css2?"
    "family=Hanken+Grotesk:wght@400;500;600;700;800;900&"
    "family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,500;0,7..72,600;0,7..72,700;"
    "1,7..72,400;1,7..72,500;1,7..72,600&display=swap');"
)

# Espinha da marca, lida de marca.py (tema escuro = índice [1]). NÃO redeclarar:
# se a marca mudar o verde/ouro/alerta, o Kit acompanha de graça.
_GREEN, _GOLD, _WARN = (marca.TOKENS[t][1] for t in ('verde', 'ouro', 'alerta'))

# Cores da marca (verde h152 + acentos) no tema DARK do Kit, em oklch.
ROOT = f""":root{{
  --green: {_GREEN}; --green-soft: oklch(85% 0.105 152); --green-deep: oklch(56% 0.14 152);
  --ink: oklch(98% 0.008 152); --muted: oklch(75% 0.022 152); --ink-dim: oklch(64% 0.02 152);
  --bg: oklch(14.5% 0.014 152); --bg2: oklch(10.5% 0.012 152); --on-green: oklch(13% 0.02 152);
  --gold: {_GOLD}; --on-gold: oklch(20% 0.04 83);
  --warn: {_WARN}; --on-warn: oklch(16% 0.03 30);
  --hair: oklch(73% 0.05 152 / .30); --hair2: oklch(73% 0.05 152 / .14);
}}"""

TOKENS = FONTS + "\n" + ROOT
