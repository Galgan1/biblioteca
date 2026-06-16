# -*- coding: utf-8 -*-
"""check_marca.py — Guardrail de saúde do sistema de design (marca.py).

(A) DRIFT: garante que os geradores NÃO hardcodam cor/fonte de marca — tudo lê marca.py.
(B) CONTRASTE: reporta a razão WCAG dos pares-chave no canvas escuro (acessibilidade).

Uso:  python check_marca.py        (sai != 0 se houver drift)
"""
import sys
import math
import re
from pathlib import Path
import marca

ROOT = Path(__file__).parent

# Superfícies que DEVEM ler a marca (não hardcodar)
TARGETS = ['gerar_carrossel.py', 'gerar_infografico.py', 'assets/style.css',
           'videos/gerar_video.py', 'videos/gerar_thumb.py', 'videos/gerar_canal_art.py']

# Tokens/fontes PROIBIDOS de aparecer hardcoded nessas superfícies
FORBIDDEN = {
    '#d8a64a': 'âmbar hardcoded → marca.hex_of("ouro")',
    'ariblk.ttf': 'Arial Black → marca.font("display", s, "Black")',
    'georgia.ttf': 'Georgia → marca.font("serif", ...)',
    'arial.ttf': 'Arial → marca.font("display", ...)',
    'oklch(84% 0.115 92)': 'ouro antigo (h92) → alinhe à marca (h83)',
    'oklch(75% 0.16 38)': 'alerta antigo (h38) → alinhe à marca (h30)',
    'oklch(73% 0.15 152)': 'verde antigo (L73) → alinhe à marca (L70)',
}


def scan_drift():
    viol = 0
    for rel in TARGETS:
        p = ROOT / rel
        if not p.exists():
            continue
        for i, line in enumerate(p.read_text(encoding='utf-8').splitlines(), 1):
            for bad, why in FORBIDDEN.items():
                if bad in line:
                    print(f'  DRIFT  {rel}:{i}  "{bad}" — {why}')
                    viol += 1
    return viol


# --- WCAG -------------------------------------------------------------------
def _lin(c):
    c /= 255
    return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4


def _lum(hexv):
    h = hexv.lstrip('#')
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return 0.2126 * _lin(r) + 0.7152 * _lin(g) + 0.0722 * _lin(b)


def ratio(fg, bg):
    a, b = _lum(fg), _lum(bg)
    hi, lo = max(a, b), min(a, b)
    return (hi + 0.05) / (lo + 0.05)


def contrast_report():
    H = lambda n: marca.hex_of(n)
    pairs = [
        ('texto (tinta) sobre fundo', H('tinta'), H('papel'), 4.5),
        ('verde sobre fundo', H('verde'), H('papel'), 3.0),
        ('ouro sobre fundo', H('ouro'), H('papel'), 3.0),
        ('texto escuro sobre pílula verde', H('papel'), H('verde'), 4.5),
    ]
    print('\nContraste WCAG (canvas escuro):')
    for name, fg, bg, minimo in pairs:
        r = ratio(fg, bg)
        tag = 'AA ok' if r >= minimo else 'ABAIXO'
        print(f'  {r:4.1f}:1  [{tag}, min {minimo}]  {name}')


# --- OKLCH -> sRGB (modo claro do site; só math, sem libs) -------------------
def oklch_to_srgb(oklch_str):
    """Converte 'oklch(L% C H)' -> (r, g, b) inteiros 0..255.
    L em %, C cromaticidade, H matiz em graus. Pipeline OKLab -> linear sRGB -> gamma."""
    m = re.match(r'\s*oklch\(\s*([\d.]+)%\s+([\d.]+)\s+([\d.]+)\s*\)\s*$', oklch_str)
    if not m:
        raise ValueError(f'OKLCH inválido: {oklch_str!r}')
    L = float(m.group(1)) / 100.0
    C = float(m.group(2))
    H = math.radians(float(m.group(3)))

    a = C * math.cos(H)
    b = C * math.sin(H)

    l_ = L + 0.3963377774 * a + 0.2158037573 * b
    m_ = L - 0.1055613458 * a - 0.0638541728 * b
    s_ = L - 0.0894841775 * a - 1.2914855480 * b

    l = l_ ** 3
    mm = m_ ** 3
    s = s_ ** 3

    lr = +4.0767416621 * l - 3.3077115913 * mm + 0.2309699292 * s
    lg = -1.2684380046 * l + 2.6097574011 * mm - 0.3413193965 * s
    lb = -0.0041960863 * l - 0.7034186147 * mm + 1.7076147010 * s

    def _gamma(c):
        c = 12.92 * c if c <= 0.0031308 else 1.055 * (c ** (1 / 2.4)) - 0.055
        return max(0.0, min(1.0, c))

    return tuple(round(_gamma(c) * 255) for c in (lr, lg, lb))


def _hex_of_oklch(oklch_str):
    return '#%02x%02x%02x' % oklch_to_srgb(oklch_str)


def contrast_report_light():
    """Contraste WCAG do MODO CLARO do site (valores OKLCH índice [0] da marca)."""
    L = lambda n: _hex_of_oklch(marca.TOKENS[n][0])
    on_green = '#%02x%02x%02x' % oklch_to_srgb('oklch(99% 0.002 152)')  # ~branco da pílula
    pairs = [
        ('texto (tinta) sobre fundo (papel)', L('tinta'), L('papel'), 4.5),
        ('verde (UI/borda) sobre fundo (papel)', L('verde'), L('papel'), 3.0),
        ('texto ~branco (on-green) sobre pílula verde', on_green, L('verde'), 4.5),
        ('ouro sobre fundo (papel)', L('ouro'), L('papel'), 3.0),
    ]
    print('\nContraste WCAG (modo claro do site):')
    for name, fg, bg, minimo in pairs:
        r = ratio(fg, bg)
        tag = 'AA ok' if r >= minimo else 'ABAIXO'
        print(f'  {r:4.1f}:1  [{tag}, min {minimo}]  {name}')


if __name__ == '__main__':
    print('== Drift (geradores × marca.py) ==')
    v = scan_drift()
    print('  OK — nenhum hardcode; tudo lê marca.py' if v == 0 else f'  FALHOU — {v} drift(s)')
    contrast_report()
    contrast_report_light()
    sys.exit(1 if v else 0)
