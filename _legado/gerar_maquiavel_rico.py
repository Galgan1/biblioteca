# -*- coding: utf-8 -*-
"""Gera os 9 capitulos genericos de Maquiavel Pedagogo no padrao rico (ch09).
Mantem a navegacao na sequencia completa dos 16 capitulos.
Fonte: skill maquiavel-pedagogo."""
from pathlib import Path

OUT = Path(__file__).parent / 'maquiavel-pedagogo'

def svg(*paths):
    return ('<svg viewBox="0 0 64 64" fill="none" '
            'xmlns="http://www.w3.org/2000/svg">' + ''.join(paths) + '</svg>')

P = lambda d, w=3, extra='': f'<path d="{d}" stroke="currentColor" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"{(" " + extra) if extra else ""}/>'
C = lambda cx, cy, r, w=3, extra='': f'<circle cx="{cx}" cy="{cy}" r="{r}" stroke="currentColor" stroke-width="{w}"{(" " + extra) if extra else ""}/>'
R = lambda x, y, w, h, rx=2, sw=3: f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" stroke="currentColor" stroke-width="{sw}"/>'

ICONS = {
    'globe': svg(C(32, 32, 22), P('M10 32H54'), P('M32 10C40 18 40 46 32 54C24 46 24 18 32 10Z')),
    'cycle': svg(P('M16 24C20 16 30 12 38 16C46 20 49 30 45 38'), P('M14 20V28H22'), P('M48 40C44 48 34 52 26 48C18 44 15 34 19 26'), P('M50 44V36H42')),
    'layers': svg(P('M32 10L54 22L32 34L10 22L32 10Z'), P('M10 32L32 44L54 32'), P('M10 42L32 54L54 42')),
    'mask': svg(P('M12 18C12 18 20 16 32 16C44 16 52 18 52 18C52 34 44 48 32 48C20 48 12 34 12 18Z'), P('M22 28C22 30 24 31 26 31'), P('M42 28C42 30 40 31 38 31'), P('M26 40C28 42 36 42 38 40')),
    'magnet': svg(P('M18 12V32C18 40 24 46 32 46C40 46 46 40 46 32V12'), P('M18 12H28V24H18'), P('M36 12H46V24H36')),
    'shock': svg(P('M36 8L16 36H30L26 56L48 26H34L36 8Z')),
    'group3': svg(C(32, 16, 6), C(16, 40, 6), C(48, 40, 6), P('M24 22L20 34', 2.5), P('M40 22L44 34', 2.5), P('M22 40H42', 2.5)),
    'door': svg(P('M16 12H40V52H16'), P('M40 12L48 16V48L40 52'), C(36, 32, 2, 0, 'fill="currentColor"'), P('M52 26V38', 2.5)),
    'scale-tip': svg(P('M32 10V20'), P('M14 26L32 20L50 30'), P('M14 26L9 38H19L14 26Z'), P('M50 30L45 42H55L50 30Z'), P('M22 50H42')),
    'drama': svg(P('M10 16H30V30C30 36 25 40 20 40C15 40 10 36 10 30V16Z'), P('M34 24H54V38C54 44 49 48 44 48C39 48 34 44 34 38V24Z'), P('M15 22C16 24 18 24 19 22', 2), P('M21 22C22 24 24 24 25 22', 2)),
    'school': svg(P('M12 26L32 12L52 26'), P('M16 26V50H48V26'), R(28, 36, 8, 14, 1), P('M12 50H52')),
    'family': svg(C(22, 18, 6), C(44, 18, 6), P('M12 50V40C12 34 16 30 22 30C28 30 32 34 32 40V50'), P('M32 50V40C32 34 38 30 44 30C50 30 52 34 52 40V50'), C(38, 38, 4)),
    'recycle': svg(P('M22 16L28 10L34 16'), P('M28 10V26C28 30 25 32 22 32H14'), P('M44 24L50 30L44 36'), P('M50 30H34', 2.5), P('M40 50L34 50C30 50 28 47 30 43'), C(32, 40, 3, 0, 'fill="currentColor"')),
    'fusion': svg(C(24, 32, 14), C(40, 32, 14), P('M32 22V42', 2)),
    'speech': svg(P('M12 16H52V40H30L20 50V40H12V16Z'), P('M22 26H42', 2.5), P('M22 32H36', 2.5)),
    'book': svg(P('M12 14C12 14 18 12 24 12C30 12 32 16 32 16C32 16 34 12 40 12C46 12 52 14 52 14V48C52 48 46 46 40 46C34 46 32 50 32 50C32 50 30 46 24 46C18 46 12 48 12 48V14Z'), P('M32 16V50')),
    'palimpsest': svg(R(14, 10, 36, 44, 2), P('M20 22H44', 2.5), P('M20 30H44', 2.5, 'stroke-dasharray="3 3"'), P('M20 38H38', 2.5), P('M40 44L50 34L54 38L44 48H40V44Z', 2.5)),
    'database': svg('<ellipse cx="32" cy="16" rx="18" ry="6" stroke="currentColor" stroke-width="3"/>', P('M14 16V32C14 35 22 38 32 38C42 38 50 35 50 32V16'), P('M14 32V48C14 51 22 54 32 54C42 54 50 51 50 48V32')),
    'barcode': svg(P('M14 16V48'), P('M20 16V48', 2), P('M26 16V48'), P('M32 16V48', 2), P('M38 16V48'), P('M44 16V48', 2), P('M50 16V48')),
    'chart-down': svg(P('M12 12V52H52'), P('M18 22L28 32L36 26L48 40'), P('M48 32V40H40')),
    'gauge': svg(P('M12 44C12 33 21 24 32 24C43 24 52 33 52 44'), P('M32 44L42 30', 2.5), C(32, 44, 3, 0, 'fill="currentColor"'), P('M12 44H18', 2), P('M46 44H52', 2)),
    'eu-stars': svg(C(32, 32, 22), C(32, 14, 1.6, 0, 'fill="currentColor"'), C(46, 20, 1.6, 0, 'fill="currentColor"'), C(50, 34, 1.6, 0, 'fill="currentColor"'), C(44, 47, 1.6, 0, 'fill="currentColor"'), C(20, 47, 1.6, 0, 'fill="currentColor"'), C(14, 34, 1.6, 0, 'fill="currentColor"'), C(18, 20, 1.6, 0, 'fill="currentColor"')),
    'trojan': svg(P('M14 44H50V50H14V44Z'), P('M18 44V30C18 22 24 16 32 16L30 24'), P('M18 30H40C46 30 50 36 50 44'), C(40, 36, 2, 0, 'fill="currentColor"'), P('M22 44V50', 2), P('M44 44V50', 2)),
    'hierarchy': svg(P('M32 8L44 20H20L32 8Z'), P('M24 26L36 38H12L24 26Z'), P('M44 26L56 38H32L44 26Z')),
    'lock': svg(P('M18 30H46V52H18V30Z'), P('M24 30V22C24 17 27 14 32 14C37 14 40 17 40 22V30'), C(32, 41, 3, 0, 'fill="currentColor"')),
    'eye': svg(P('M8 32C8 32 18 18 32 18C46 18 56 32 56 32C56 32 46 46 32 46C18 46 8 32 8 32Z'), C(32, 32, 7)),
    'peers': svg(C(20, 22, 6), C(44, 22, 6), C(32, 44, 6), P('M25 26L29 38', 2.5), P('M39 26L35 38', 2.5), P('M26 22H38', 2.5)),
    'handshake': svg(P('M8 26L20 24L30 32L26 38L20 34'), P('M56 26L44 24L34 32'), P('M30 32L38 40L44 36', 2.5), P('M20 34L26 40', 2.5), P('M8 26V38H14', 2), P('M56 26V38H50', 2)),
    'doc-seal': svg(P('M16 10H40L48 18V44H16V10Z'), P('M40 10V18H48'), P('M22 24H40', 2.5), P('M22 30H40', 2.5), C(38, 46, 7), P('M38 42V50M34 46H42', 2)),
    'brain': svg(P('M32 14C26 14 22 18 22 22C18 22 14 26 14 32C14 38 18 42 22 42C22 48 26 52 32 52V14Z'), P('M32 14C38 14 42 18 42 22C46 22 50 26 50 32C50 38 46 42 42 42C42 48 38 52 32 52'), P('M32 22V44')),
    'alert': svg(P('M32 10L56 52H8L32 10Z'), P('M32 28V40'), C(32, 47, 1.5, 0, 'fill="currentColor"')),
    'network': svg(C(32, 14, 5), C(14, 44, 5), C(50, 44, 5), P('M30 18L16 40', 2.5), P('M34 18L48 40', 2.5), P('M19 44H45', 2.5)),
    'target': svg(C(32, 32, 22), C(32, 32, 13), C(32, 32, 4, 0, 'fill="currentColor"')),
    'snowball': svg(C(20, 24, 8), C(40, 40, 12), P('M14 24C14 24 30 28 34 44', 2.5, 'stroke-dasharray="2 4"')),
}


def card(c, idx):
    classes = 'card'
    if c.get('wide'):
        classes += ' card-wide'
    if c.get('warning'):
        classes += ' card-warning'
    idattr = f' id="{c["id"]}"' if c.get('id') else ''
    out = [f'            <article class="{classes} animate-entrance" style="--i: {idx}"{idattr}>']
    out.append('                <div class="card-icon" aria-hidden="true">')
    out.append('                    ' + ICONS[c['icon']])
    out.append('                </div>')
    out.append('                <div class="card-content">')
    out.append(f'                    <h2 class="card-title">{c["title"]}</h2>')
    if c.get('body'):
        out.append(f'                    <p class="card-body">{c["body"]}</p>')
    if c.get('list'):
        out.append('                    <ul class="content-list">')
        for li in c['list']:
            out.append(f'                        <li>{li}</li>')
        out.append('                    </ul>')
    if c.get('tip'):
        out.append(f'                    <p class="card-tip">{c["tip"]}</p>')
    if c.get('quote'):
        out.append('                    <div class="card-details">')
        out.append('                        <div class="card-details-inner">')
        out.append(f'                            <blockquote>{c["quote"]}</blockquote>')
        out.append('                        </div>')
        out.append('                    </div>')
    elif c.get('details'):
        out.append('                    <div class="card-details">')
        out.append('                        <div class="card-details-inner">')
        out.append(f'                            <p>{c["details"]}</p>')
        out.append('                        </div>')
        out.append('                    </div>')
    out.append('                </div>')
    out.append('            </article>')
    return '\n'.join(out)


def page(ch, prev_href, prev_label, next_href, next_label):
    cards_html = '\n\n'.join(card(c, i + 1) for i, c in enumerate(ch['cards']))
    lessons_html = '\n'.join(f'                    <li>{l}</li>' for l in ch['lessons'])
    n = len(ch['cards'])
    return f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{ch['title_page']} | Maquiavel Pedagogo</title>
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
            <a href="../maquiavel-pedagogo.html" class="back-link"><span class="icon-arrow" aria-hidden="true">&larr;</span> Voltar para Visão Geral</a>
        </nav>

        <header class="header animate-entrance" style="--i: 0">
            <h1 class="header-title">
                <span class="header-title-light">MAQUIAVEL</span>
                <span class="header-title-bold">PEDAGOGO</span>
            </h1>
            <p class="header-subtitle">{ch['subtitle']}</p>
            <p class="header-credit">Pascal Bernardin</p>
            <p class="header-intro">
                {ch['intro']}
            </p>
        </header>

        <main id="conteudo">
            <div class="grid">

{cards_html}

            </div>

            <section class="lessons animate-entrance" style="--i: {n + 1}" aria-labelledby="licoes-titulo">
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
            <p class="footer-credit">Maquiavel Pedagogo · Pascal Bernardin</p>
        </footer>
    </div>
    <script src="script.js"></script>
</body>
</html>
'''

# Sequencia completa dos 16 capitulos (para navegacao correta)
FULL_ORDER = [
    'ch00-introducao', 'ch01-tecnicas-manipulacao', 'ch02-psicologia-social-educacao',
    'ch03-unesco-controle-psicologico', 'ch04-redefinicao-papel-escola', 'ch05-revolucao-etica',
    'ch06-revolucao-cultural-interculturalismo', 'ch07-reescrever-historia', 'ch08-iufms-formacao-professores',
    'ch09-descentralizacao', 'ch10-avaliacao-informatizacao', 'ch11-europa',
    'ch12-revolucao-pedagogica-franca', 'ch13-sociedade-dual', 'ch14-totalitarismo-psicopedagogico',
    'ch15-conclusao',
]

if __name__ == '__main__':
    import gerar_maquiavel_dados as D
    OVERVIEW = '../maquiavel-pedagogo.html'
    for slug, ch in D.CHAPTERS.items():
        i = FULL_ORDER.index(slug)
        prev_href = (FULL_ORDER[i - 1] + '.html') if i > 0 else OVERVIEW
        prev_label = 'Anterior' if i > 0 else 'Visão Geral'
        next_href = (FULL_ORDER[i + 1] + '.html') if i < len(FULL_ORDER) - 1 else OVERVIEW
        next_label = 'Próximo' if i < len(FULL_ORDER) - 1 else 'Visão Geral'
        (OUT / (slug + '.html')).write_text(page(ch, prev_href, prev_label, next_href, next_label), encoding='utf-8')
        print(f'{slug}.html: {len(ch["cards"])} cards')
    print('OK')
