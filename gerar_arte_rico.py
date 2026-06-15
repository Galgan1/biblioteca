# -*- coding: utf-8 -*-
"""Gera os 13 capitulos de A Arte da Guerra no padrao rico (Keller):
header + cards especificos (icone variado + titulo + body + card-tip + details)
+ licoes-chave + navegacao. Fonte: skill sun-tzu-arte-da-guerra."""
from pathlib import Path

OUT = Path(__file__).parent / 'arte-da-guerra'

# --- Biblioteca de icones SVG de linha (stroke currentColor) ---
def svg(*paths):
    inner = ''.join(paths)
    return ('<svg viewBox="0 0 64 64" fill="none" '
            'xmlns="http://www.w3.org/2000/svg">' + inner + '</svg>')

P = lambda d, w=3, extra='': f'<path d="{d}" stroke="currentColor" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"{(" " + extra) if extra else ""}/>'
C = lambda cx, cy, r, w=3, extra='': f'<circle cx="{cx}" cy="{cy}" r="{r}" stroke="currentColor" stroke-width="{w}"{(" " + extra) if extra else ""}/>'

ICONS = {
    'balance': svg(P('M32 12V50'), P('M18 50H46'), P('M12 22H52'), P('M12 22L7 33H17L12 22Z'), P('M52 22L47 33H57L52 22Z')),
    'checklist': svg(P('M14 16H50'), P('M14 32H50'), P('M14 48H50'), P('M6 14L9 17L13 12', 2.5), P('M6 30L9 33L13 28', 2.5), P('M6 46L9 49L13 44', 2.5)),
    'mask': svg(P('M12 18C12 18 20 16 32 16C44 16 52 18 52 18C52 34 44 48 32 48C20 48 12 34 12 18Z'), P('M22 28C22 30 24 31 26 31'), P('M42 28C42 30 40 31 38 31'), P('M26 40C28 42 36 42 38 40')),
    'temple': svg(P('M12 24L32 12L52 24'), P('M16 24V44'), P('M26 24V44'), P('M38 24V44'), P('M48 24V44'), P('M12 50H52')),
    'alert': svg(P('M32 10L56 52H8L32 10Z'), P('M32 28V40'), C(32, 47, 1.5, 0, 'fill="currentColor"')),
    'bolt': svg(P('M36 8L16 36H30L26 56L48 26H34L36 8Z')),
    'coins': svg(C(24, 24, 12), P('M24 18V30'), P('M20 21H27C28.7 21 30 22.3 30 24C30 25.7 28.7 27 27 27H20'), C(40, 42, 12), P('M40 36V48'), P('M36 39H43C44.7 39 46 40.3 46 42C46 43.7 44.7 45 43 45H36')),
    'cascade': svg(P('M10 14H26V26'), P('M26 26H42V38'), P('M42 38H54V50'), P('M22 22L26 26L30 22', 2.5), P('M38 34L42 38L46 34', 2.5)),
    'trophy': svg(P('M20 12H44V26C44 33 38 38 32 38C26 38 20 33 20 26V12Z'), P('M20 16H12V20C12 25 16 28 20 28'), P('M44 16H52V20C52 25 48 28 44 28'), P('M32 38V48'), P('M22 52H42'), P('M26 52C26 49 28 48 32 48C36 48 38 49 38 52')),
    'hierarchy': svg(P('M32 8L44 20H20L32 8Z'), P('M24 26L36 38H12L24 26Z'), P('M44 26L56 38H32L44 26Z')),
    'ratio': svg(P('M14 50L50 14'), C(20, 20, 7), C(44, 44, 7)),
    'brain': svg(P('M32 14C26 14 22 18 22 22C18 22 14 26 14 32C14 38 18 42 22 42C22 48 26 52 32 52V14Z'), P('M32 14C38 14 42 18 42 22C46 22 50 26 50 32C50 38 46 42 42 42C42 48 38 52 32 52'), P('M32 22V44')),
    'shield': svg(P('M32 10L52 18V32C52 44 43 52 32 56C21 52 12 44 12 32V18L32 10Z'), P('M24 32L30 38L42 26', 2.5)),
    'mountain': svg(P('M8 50L24 22L34 38L42 26L56 50H8Z'), P('M24 22L29 31', 2.5)),
    'music': svg(C(20, 46, 6), C(44, 40, 6), P('M26 46V18L50 12V40'), P('M26 24L50 18')),
    'target': svg(C(32, 32, 22), C(32, 32, 13), C(32, 32, 4, 0, 'fill="currentColor"')),
    'water': svg(P('M8 26C14 20 18 20 24 26C30 32 34 32 40 26C46 20 50 20 56 26'), P('M8 40C14 34 18 34 24 40C30 46 34 46 40 40C46 34 50 34 56 40')),
    'focus': svg(C(32, 32, 8), P('M32 8V18'), P('M32 46V56'), P('M8 32H18'), P('M46 32H56'), P('M15 15L22 22', 2.5), P('M49 49L42 42', 2.5), P('M49 15L42 22', 2.5), P('M15 49L22 42', 2.5)),
    'compass': svg(C(32, 32, 22), P('M40 24L36 36L24 40L28 28L40 24Z'), C(32, 32, 2.5, 0, 'fill="currentColor"')),
    'flag': svg(P('M18 10V54'), P('M18 12H46L40 22L46 32H18')),
    'wind': svg(P('M8 24H38C42 24 46 21 46 16C46 11 42 10 39 13'), P('M8 34H50C54 34 56 31 56 27'), P('M8 44H34C38 44 42 47 42 52C42 56 38 57 35 54')),
    'eye': svg(P('M8 32C8 32 18 18 32 18C46 18 56 32 56 32C56 32 46 46 32 46C18 46 8 32 8 32Z'), C(32, 32, 7)),
    'map': svg(P('M12 18L24 14L40 18L52 14V46L40 50L24 46L12 50V18Z'), P('M24 14V46'), P('M40 18V50')),
    'snake': svg(P('M14 20C14 20 26 20 26 28C26 36 14 36 14 44C14 50 22 52 28 50'), P('M26 28C26 20 38 20 38 28C38 36 50 36 50 44C50 50 44 52 40 50'), C(16, 18, 2.5, 0, 'fill="currentColor"')),
    'fire': svg(P('M32 8C32 8 20 20 20 36C20 45 25 52 32 52C39 52 44 45 44 36C44 30 40 26 40 26C40 30 37 32 35 32C35 24 32 8 32 8Z'), P('M30 44C30 40 32 38 34 38')),
    'spy': svg(P('M14 30C14 30 20 18 32 18C44 18 50 30 50 30'), P('M10 32H54'), C(22, 40, 7), C(42, 40, 7), P('M29 40H35')),
    'crown': svg(P('M12 44L16 20L26 32L32 16L38 32L48 20L52 44H12Z'), P('M12 50H52')),
    'people': svg(C(22, 22, 7), C(42, 22, 7), P('M10 48C10 38 16 34 22 34C28 34 34 38 34 48'), P('M30 48C30 38 36 34 42 34C48 34 54 38 54 48')),
    'network': svg(C(32, 14, 5), C(14, 44, 5), C(50, 44, 5), P('M30 18L16 40', 2.5), P('M34 18L48 40', 2.5), P('M19 44H45', 2.5)),
    'hourglass': svg(P('M16 10H48'), P('M16 54H48'), P('M18 10C18 24 32 28 32 32C32 36 18 40 18 54'), P('M46 10C46 24 32 28 32 32C32 36 46 40 46 54')),
    'sword': svg(P('M48 12L28 32L32 36L52 16V12H48Z'), P('M14 44L24 34', 2.5), P('M12 52L20 44'), P('M16 40L24 48', 2.5)),
    'castle': svg(P('M12 26V52H52V26L46 26V20H40V26H36V20H28V26H24V20H18V26H12Z'), P('M26 52V40H38V52')),
    'lock': svg(P('M18 30H46V52H18V30Z'), P('M24 30V22C24 17 27 14 32 14C37 14 40 17 40 22V30'), C(32, 41, 3, 0, 'fill="currentColor"')),
    'split': svg(P('M32 12V28'), P('M32 28C32 28 32 38 20 42'), P('M32 28C32 28 32 38 44 42'), P('M16 48L20 42L26 46', 2.5), P('M38 46L44 42L48 48', 2.5)),
}


def card(c, idx):
    classes = 'card'
    if c.get('wide'):
        classes += ' card-wide'
    if c.get('warning'):
        classes += ' card-warning'
    parts = [f'            <article class="{classes} animate-entrance" style="--i: {idx}">']
    parts.append('                <div class="card-icon" aria-hidden="true">')
    parts.append('                    ' + ICONS[c['icon']])
    parts.append('                </div>')
    parts.append('                <div class="card-content">')
    parts.append(f'                    <h2 class="card-title">{c["title"]}</h2>')
    if c.get('body'):
        parts.append(f'                    <p class="card-body">{c["body"]}</p>')
    if c.get('list'):
        parts.append('                    <ul class="content-list">')
        for li in c['list']:
            parts.append(f'                        <li>{li}</li>')
        parts.append('                    </ul>')
    if c.get('tip'):
        parts.append(f'                    <p class="card-tip">{c["tip"]}</p>')
    if c.get('details'):
        parts.append('                    <div class="card-details">')
        parts.append('                        <div class="card-details-inner">')
        parts.append(f'                            <p>{c["details"]}</p>')
        parts.append('                        </div>')
        parts.append('                    </div>')
    parts.append('                </div>')
    parts.append('            </article>')
    return '\n'.join(parts)


def page(ch, prev_href, prev_label, next_href, next_label):
    cards_html = '\n\n'.join(card(c, i + 1) for i, c in enumerate(ch['cards']))
    lessons_html = '\n'.join(f'                    <li>{l}</li>' for l in ch['lessons'])
    n_cards = len(ch['cards'])
    return f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{ch['num_label_title']} | A Arte da Guerra</title>
    <meta name="theme-color" content="#ffffff">
    <meta name="description" content="{ch['meta']}">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;500;700;800&family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,600;0,7..72,700;1,7..72,400&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../assets/style.css">
</head>
<body>
    <a href="#conteudo" class="skip-link">Ir para o conteúdo</a>
    <div class="page">
        <nav aria-label="Navegação principal">
            <a href="../arte-da-guerra.html" class="back-link"><span class="icon-arrow" aria-hidden="true">&larr;</span> Voltar para Visão Geral</a>
        </nav>

        <header class="header animate-entrance" style="--i: 0">
            <h1 class="header-title">
                <span class="header-title-light">A ARTE DA</span>
                <span class="header-title-bold">GUERRA</span>
            </h1>
            <p class="header-subtitle">{ch['num_label']}</p>
            <p class="header-credit">Sun Tzu</p>
            <p class="header-intro">
                {ch['intro']}
            </p>
        </header>

        <main id="conteudo">
            <div class="grid">

{cards_html}

            </div>

            <section class="lessons animate-entrance" style="--i: {n_cards + 1}" aria-labelledby="licoes-titulo">
                <h2 class="lessons-title" id="licoes-titulo">Lições-Chave</h2>
                <ul class="lessons-list">
{lessons_html}
                </ul>
            </section>

            <nav aria-label="Navegação entre capítulos" class="chapter-nav">
                <a href="{prev_href}" class="chapter-nav-link">&larr; {prev_label}</a>
                <a href="{next_href}" class="chapter-nav-link">{next_label} &rarr;</a>
            </nav>
        </main>

        <footer class="footer">
            <p class="footer-credit">A Arte da Guerra · Sun Tzu</p>
        </footer>
    </div>
    <script src="script.js"></script>
</body>
</html>
'''


# placeholder — dados injetados por gerar_arte_dados.py
CHAPTERS = {}
ORDER = []

if __name__ == '__main__':
    import gerar_arte_dados as D
    CHAPTERS = D.CHAPTERS
    ORDER = D.ORDER
    OVERVIEW = '../arte-da-guerra.html'
    for i, slug in enumerate(ORDER):
        prev_href = (ORDER[i - 1] + '.html') if i > 0 else OVERVIEW
        prev_label = 'Anterior' if i > 0 else 'Visão Geral'
        next_href = (ORDER[i + 1] + '.html') if i < len(ORDER) - 1 else OVERVIEW
        next_label = 'Próximo' if i < len(ORDER) - 1 else 'Visão Geral'
        out = OUT / (slug + '.html')
        out.write_text(page(CHAPTERS[slug], prev_href, prev_label, next_href, next_label), encoding='utf-8')
        print(f'{slug}.html: {len(CHAPTERS[slug]["cards"])} cards')
    print('OK')
