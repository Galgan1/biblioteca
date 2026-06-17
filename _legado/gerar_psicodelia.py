# -*- coding: utf-8 -*-
"""Gera o livro 'A Experiencia Psicodelica' — visao geral + 8 capitulos —
no PADRAO ESTRUTURAL do projeto, mas com a PELE psicodelica (style.css +
psicodelia.css, body.psy). Fonte: skill experiencia-psicodelica."""
from pathlib import Path

ROOT = Path(__file__).parent
OUT = ROOT / 'experiencia-psicodelica'
OUT.mkdir(exist_ok=True)

def svg(*paths):
    return ('<svg viewBox="0 0 64 64" fill="none" '
            'xmlns="http://www.w3.org/2000/svg">' + ''.join(paths) + '</svg>')

P = lambda d, w=3, extra='': f'<path d="{d}" stroke="currentColor" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"{(" " + extra) if extra else ""}/>'
C = lambda cx, cy, r, w=3, extra='': f'<circle cx="{cx}" cy="{cy}" r="{r}" stroke="currentColor" stroke-width="{w}"{(" " + extra) if extra else ""}/>'

ICONS = {
    'eye': svg(P('M6 32C6 32 17 18 32 18C47 18 58 32 58 32C58 32 47 46 32 46C17 46 6 32 6 32Z'), C(32, 32, 9), C(32, 32, 3, 0, 'fill="currentColor"')),
    'lotus': svg(P('M32 16C28 24 28 34 32 44C36 34 36 24 32 16Z'), P('M32 44C24 40 18 32 16 22C26 24 32 34 32 44Z'), P('M32 44C40 40 46 32 48 22C38 24 32 34 32 44Z'), P('M10 44C18 50 46 50 54 44', 2.5)),
    'spiral': svg(P('M32 32C32 28 36 28 36 32C36 38 28 38 28 32C28 24 40 24 40 32C40 42 24 42 24 32C24 20 44 20 44 32C44 46 20 46 20 32', 2.8)),
    'wave': svg(P('M6 26C12 20 16 20 22 26C28 32 32 32 38 26C44 20 48 20 54 26'), P('M6 40C12 34 16 34 22 40C28 46 32 46 38 40C44 34 48 34 54 40')),
    'flame': svg(P('M32 8C32 8 20 20 20 36C20 45 25 52 32 52C39 52 44 45 44 36C44 30 40 26 40 26C40 30 37 32 35 32C35 24 32 8 32 8Z'), P('M30 44C30 40 32 38 34 38', 2.5)),
    'sun': svg(C(32, 32, 12), P('M32 8V16'), P('M32 48V56'), P('M8 32H16'), P('M48 32H56'), P('M14 14L20 20'), P('M44 44L50 50'), P('M50 14L44 20'), P('M20 44L14 50')),
    'infinity': svg(P('M20 32C20 26 26 26 32 32C38 38 44 38 44 32C44 26 38 26 32 32C26 38 20 38 20 32Z', 3)),
    'yinyang': svg(C(32, 32, 22), P('M32 10A22 22 0 0 1 32 54A11 11 0 0 1 32 32A11 11 0 0 0 32 10Z', 0, 'fill="currentColor"'), C(32, 21, 2.5, 0, 'fill="#160233"'), C(32, 43, 2.5)),
    'mountain': svg(P('M8 50L24 22L34 38L42 26L56 50H8Z'), P('M24 22L29 31', 2.5)),
    'key': svg(C(22, 24, 10), P('M29 31L48 50'), P('M40 42L46 36', 2.5), P('M44 46L50 40', 2.5), C(22, 24, 3, 0, 'fill="currentColor"')),
    'door': svg(P('M18 10H46V54H18V10Z'), P('M24 10V54M40 10V54', 2), C(36, 32, 2, 0, 'fill="currentColor"')),
    'mirror': svg('<ellipse cx="32" cy="26" rx="16" ry="20" stroke="currentColor" stroke-width="3"/>', P('M24 18C26 16 30 15 33 16', 2.5), P('M32 46V56'), P('M24 56H40', 2.5)),
    'theatre': svg(P('M10 16H30V30C30 36 25 40 20 40C15 40 10 36 10 30V16Z'), P('M34 24H54V38C54 44 49 48 44 48C39 48 34 44 34 38V24Z'), P('M15 30C16 32 18 32 19 30', 2), P('M45 38C44 36 42 36 41 38', 2)),
    'portal': svg('<ellipse cx="32" cy="32" rx="14" ry="22" stroke="currentColor" stroke-width="3"/>', '<ellipse cx="32" cy="32" rx="7" ry="14" stroke="currentColor" stroke-width="2.5"/>', P('M32 10V8M32 56V54', 2)),
    'meditate': svg(C(32, 16, 6), P('M20 50C20 40 25 34 32 34C39 34 44 40 44 50'), P('M14 48C20 44 24 44 24 48', 2.5), P('M50 48C44 44 40 44 40 48', 2.5)),
    'helix': svg(P('M22 10C42 18 22 30 42 38C22 46 42 54 22 54', 2.8), P('M42 10C22 18 42 30 22 38C42 46 22 54 42 54', 2.8), P('M26 16H38M26 32H38M26 48H38', 2)),
    'kaleidoscope': svg(C(32, 32, 22), P('M32 10V54'), P('M13 21L51 43'), P('M13 43L51 21'), C(32, 32, 7)),
    'hand': svg(P('M22 34V18C22 15 26 15 26 18V30'), P('M26 30V14C26 11 30 11 30 14V30'), P('M30 30V16C30 13 34 13 34 16V30'), P('M34 30V20C34 17 38 17 38 20V38C38 46 33 52 26 52C20 52 18 46 16 40L14 34C13 31 17 29 19 32L22 36')),
    'moon': svg(P('M40 12C30 14 24 22 24 32C24 42 30 50 40 52C30 56 16 48 16 32C16 16 30 8 40 12Z')),
    'droplet': svg(P('M32 10C32 10 18 28 18 38C18 47 24 52 32 52C40 52 46 47 46 38C46 28 32 10 32 10Z'), P('M26 40C26 44 28 46 31 47', 2.5)),
    'bolt': svg(P('M36 8L16 36H30L26 56L48 26H34L36 8Z')),
    'scales': svg(P('M32 12V52'), P('M16 50H48'), P('M12 22H52'), P('M12 22L7 33H17L12 22Z'), P('M52 22L47 33H57L52 22Z')),
    'skull': svg(P('M32 12C22 12 16 19 16 28C16 33 18 36 20 38V46H44V38C46 36 48 33 48 28C48 19 42 12 32 12Z'), C(25, 28, 3, 0, 'fill="currentColor"'), C(39, 28, 3, 0, 'fill="currentColor"'), P('M32 34L29 40H35L32 34Z', 2)),
    'compass': svg(C(32, 32, 22), P('M40 24L36 36L24 40L28 28L40 24Z'), C(32, 32, 2.5, 0, 'fill="currentColor"')),
    'star': svg(P('M32 8L39 26H58L43 38L48 56L32 45L16 56L21 38L6 26H25L32 8Z')),
    'cube': svg(P('M32 8L54 20V44L32 56L10 44V20L32 8Z'), P('M32 8V32M32 32L54 20M32 32L10 20M32 32V56', 2)),
    'people': svg(C(22, 22, 7), C(42, 22, 7), P('M10 48C10 38 16 34 22 34C28 34 34 38 34 48'), P('M30 48C30 38 36 34 42 34C48 34 54 38 54 48')),
    'list': svg(P('M14 16H50'), P('M14 32H50'), P('M14 48H50'), C(8, 16, 1.5, 0, 'fill="currentColor"'), C(8, 32, 1.5, 0, 'fill="currentColor"'), C(8, 48, 1.5, 0, 'fill="currentColor"')),
}

HEAD = '''<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="theme-color" content="#0a0118">
    <meta name="description" content="{meta}">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;500;700;800&family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,600;0,7..72,700;1,7..72,400&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="{css}style.css">
    <link rel="stylesheet" href="{css}psicodelia.css">
</head>
<body class="psy">'''


def card(c, idx):
    classes = 'card'
    if c.get('wide'):
        classes += ' card-wide'
    if c.get('warning'):
        classes += ' card-warning'
    out = [f'            <article class="{classes} animate-entrance" style="--i: {idx}">']
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
        out.append('                    <div class="card-details"><div class="card-details-inner">')
        out.append(f'                        <blockquote>{c["quote"]}</blockquote>')
        out.append('                    </div></div>')
    elif c.get('details'):
        out.append('                    <div class="card-details"><div class="card-details-inner">')
        out.append(f'                        <p>{c["details"]}</p>')
        out.append('                    </div></div>')
    out.append('                </div>')
    out.append('            </article>')
    return '\n'.join(out)


def chapter_page(ch, prev_href, prev_label, next_href, next_label):
    cards_html = '\n\n'.join(card(c, i + 1) for i, c in enumerate(ch['cards']))
    lessons_html = '\n'.join(f'                    <li>{l}</li>' for l in ch['lessons'])
    n = len(ch['cards'])
    head = HEAD.format(title=ch['title_page'] + ' | A Experiência Psicodélica', meta=ch['meta'], css='../assets/')
    return f'''{head}
    <a href="#conteudo" class="skip-link">Ir para o conteúdo</a>
    <div class="page">
        <nav aria-label="Navegação principal">
            <a href="../experiencia-psicodelica.html" class="back-link"><span class="icon-arrow" aria-hidden="true">&larr;</span> Voltar para Visão Geral</a>
        </nav>

        <header class="header animate-entrance" style="--i: 0">
            <h1 class="header-title">
                <span class="header-title-light">A EXPERIÊNCIA</span>
                <span class="header-title-bold">PSICODÉLICA</span>
            </h1>
            <p class="header-subtitle">{ch['subtitle']}</p>
            <p class="header-credit">Leary · Metzner · Alpert</p>
            <p class="header-intro">
                {ch['intro']}
            </p>
        </header>

        <main id="conteudo">
            <div class="grid">

{cards_html}

            </div>

            <section class="lessons animate-entrance" style="--i: {n + 1}" aria-labelledby="licoes-titulo">
                <h2 class="lessons-title" id="licoes-titulo">Pontos de Navegação</h2>
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
            <p class="footer-credit">A Experiência Psicodélica · Leary, Metzner &amp; Alpert</p>
        </footer>
    </div>
    <script src="script.js"></script>
</body>
</html>
'''


def overview_page(ov, chapters_order, chapter_titles):
    cards_html = '\n\n'.join(card(c, i + 1) for i, c in enumerate(ov['cards']))
    n = len(ov['cards'])
    links = []
    for i, slug in enumerate(chapters_order):
        links.append(f'                        <a href="experiencia-psicodelica/{slug}.html" class="chapter-link">{chapter_titles[slug]} <span class="arrow" aria-hidden="true">&rarr;</span></a>')
    links_html = '\n'.join(links)
    head = HEAD.format(title='A Experiência Psicodélica | Biblioteca', meta=ov['meta'], css='assets/')
    return f'''{head}
    <a href="#conteudo" class="skip-link">Ir para o conteúdo</a>
    <div class="page">
        <nav aria-label="Navegação Voltar">
            <a href="index.html" class="back-link"><span class="icon-arrow" aria-hidden="true">&larr;</span> Voltar para a Biblioteca</a>
        </nav>

        <header class="header animate-entrance" style="--i: 0">
            <h1 class="header-title">
                <span class="header-title-light">A EXPERIÊNCIA</span>
                <span class="header-title-bold">PSICODÉLICA</span>
            </h1>
            <p class="header-subtitle">UM MANUAL BASEADO NO LIVRO TIBETANO DOS MORTOS</p>
            <p class="header-credit">Timothy Leary · Ralph Metzner · Richard Alpert</p>
            <p class="header-intro">
                {ov['intro']}
            </p>
        </header>

        <main id="conteudo">
            <div class="grid">

{cards_html}

            <article class="card card-wide animate-entrance" style="--i: {n + 1}">
                <div class="card-icon" aria-hidden="true">
                    {ICONS['list']}
                </div>
                <div class="card-content">
                    <h2 class="card-title">Os 8 Movimentos da Viagem</h2>
                    <p class="card-body">Percorra cada fase do manual:</p>
                    <nav aria-label="Navegação de Capítulos" class="chapter-list">
{links_html}
                    </nav>
                </div>
            </article>

            </div>
        </main>

        <footer class="footer">
            <p class="footer-credit">A Experiência Psicodélica · Leary, Metzner &amp; Alpert</p>
        </footer>
    </div>
    <script src="experiencia-psicodelica/script.js"></script>
</body>
</html>
'''


ORDER = [
    'ch1-introducao-geral', 'ch2-tributos-e-contexto', 'ch3-primeiro-bardo',
    'ch4-segundo-bardo-visoes-1-3', 'ch5-segundo-bardo-visoes-4-7', 'ch6-terceiro-bardo',
    'ch7-comentarios-tecnicos', 'ch8-instrucoes-para-sessao',
]

if __name__ == '__main__':
    import gerar_psicodelia_dados as D
    OVERVIEW = '../experiencia-psicodelica.html'
    titles = {s: D.CHAPTERS[s]['nav_title'] for s in ORDER}
    # capitulos
    for i, slug in enumerate(ORDER):
        prev_href = (ORDER[i - 1] + '.html') if i > 0 else OVERVIEW
        prev_label = 'Anterior' if i > 0 else 'Visão Geral'
        next_href = (ORDER[i + 1] + '.html') if i < len(ORDER) - 1 else OVERVIEW
        next_label = 'Próximo' if i < len(ORDER) - 1 else 'Visão Geral'
        (OUT / (slug + '.html')).write_text(
            chapter_page(D.CHAPTERS[slug], prev_href, prev_label, next_href, next_label), encoding='utf-8')
        print(f'{slug}.html: {len(D.CHAPTERS[slug]["cards"])} cards')
    # visao geral
    (ROOT / 'experiencia-psicodelica.html').write_text(
        overview_page(D.OVERVIEW, ORDER, titles), encoding='utf-8')
    print('experiencia-psicodelica.html (visão geral)')
    # script.js (mesmo toggle dos outros livros)
    (OUT / 'script.js').write_text(
        (ROOT / 'keller-casamento' / 'script.js').read_text(encoding='utf-8'), encoding='utf-8')
    print('OK')
