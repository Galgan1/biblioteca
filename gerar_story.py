# -*- coding: utf-8 -*-
"""Gera as páginas da biblioteca para o livro Story (Robert McKee),
no padrão "Cheat Sheet Verde". Saída: story-mckee.html (visão geral) +
story-mckee/chNN-*.html (19 capítulos) + story-mckee/script.js.
Usa apenas classes de assets/style.css — nenhum estilo inline."""

import os

BASE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(BASE, "story-mckee")
os.makedirs(OUT_DIR, exist_ok=True)

# --- Biblioteca de ícones de linha (inner SVG) -------------------------------
ICONS = {
    "masks": '<path d="M10 14h18v14a9 9 0 0 1-18 0z" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/><path d="M15 20h3M22 20h1" stroke="currentColor" stroke-width="3" stroke-linecap="round"/><path d="M14 26a5 4 0 0 0 10 0" stroke="currentColor" stroke-width="3" stroke-linecap="round"/><path d="M36 18h18v14a9 9 0 0 1-18 0z" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/><path d="M41 24h3M48 24h1" stroke="currentColor" stroke-width="3" stroke-linecap="round"/><path d="M40 32a5 4 0 0 1 10 0" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>',
    "triangle": '<path d="M32 10L56 52H8L32 10z" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/><path d="M32 30v0M22 42h20" stroke="currentColor" stroke-width="3" stroke-linecap="round"/><circle cx="32" cy="22" r="2" fill="currentColor"/><circle cx="18" cy="48" r="2" fill="currentColor"/><circle cx="46" cy="48" r="2" fill="currentColor"/>',
    "clock": '<circle cx="32" cy="32" r="22" stroke="currentColor" stroke-width="3"/><path d="M32 18v14l10 6" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>',
    "pin": '<path d="M32 56s16-14 16-28a16 16 0 0 0-32 0c0 14 16 28 16 28z" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/><circle cx="32" cy="28" r="6" stroke="currentColor" stroke-width="3"/>',
    "gap": '<path d="M10 32h16M38 32h16" stroke="currentColor" stroke-width="3" stroke-linecap="round"/><path d="M22 24l-6 8 6 8M42 24l6 8-6 8" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/><path d="M30 18l4 28" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-dasharray="3 5"/>',
    "person": '<circle cx="32" cy="20" r="10" stroke="currentColor" stroke-width="3"/><path d="M14 52c0-10 8-18 18-18s18 8 18 18" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>',
    "mask": '<path d="M14 14h36v18c0 12-9 22-18 22s-18-10-18-22z" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/><circle cx="24" cy="28" r="3" stroke="currentColor" stroke-width="3"/><circle cx="40" cy="28" r="3" stroke="currentColor" stroke-width="3"/><path d="M26 40a8 6 0 0 0 12 0" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>',
    "bulb": '<path d="M22 44a14 14 0 1 1 20 0c-2 2-3 4-3 7H25c0-3-1-5-3-7z" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/><path d="M26 56h12" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>',
    "target": '<circle cx="32" cy="32" r="22" stroke="currentColor" stroke-width="3"/><circle cx="32" cy="32" r="12" stroke="currentColor" stroke-width="3"/><circle cx="32" cy="32" r="2.5" fill="currentColor"/>',
    "spark": '<path d="M34 8L18 36h12l-4 20 20-30H34l4-18z" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/>',
    "steps": '<path d="M10 52h12V40h12V28h12V16h8" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>',
    "pivot": '<path d="M16 32a16 16 0 1 1 6 12" stroke="currentColor" stroke-width="3" stroke-linecap="round"/><path d="M16 24v10h10" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>',
    "layers": '<path d="M32 10L54 22 32 34 10 22 32 10z" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/><path d="M10 32l22 12 22-12M10 42l22 12 22-12" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/>',
    "lens": '<circle cx="28" cy="28" r="16" stroke="currentColor" stroke-width="3"/><path d="M40 40l12 12" stroke="currentColor" stroke-width="3" stroke-linecap="round"/><path d="M22 28h12M28 22v12" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>',
    "link": '<path d="M26 38l12-12" stroke="currentColor" stroke-width="3" stroke-linecap="round"/><path d="M22 32l-6 6a8 8 0 0 0 11 11l6-6" stroke="currentColor" stroke-width="3" stroke-linecap="round"/><path d="M42 32l6-6a8 8 0 0 0-11-11l-6 6" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>',
    "fork": '<path d="M32 56V34" stroke="currentColor" stroke-width="3" stroke-linecap="round"/><path d="M32 34L16 14M32 34l16-20" stroke="currentColor" stroke-width="3" stroke-linecap="round"/><circle cx="16" cy="12" r="4" stroke="currentColor" stroke-width="3"/><circle cx="48" cy="12" r="4" stroke="currentColor" stroke-width="3"/>',
    "sword": '<path d="M44 12l8 8-22 22-8-8 22-22z" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/><path d="M22 42l-8 8M12 44l8 8" stroke="currentColor" stroke-width="3" stroke-linecap="round"/><path d="M40 16l8 8" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>',
    "eye": '<path d="M6 32s10-16 26-16 26 16 26 16-10 16-26 16S6 32 6 32z" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/><circle cx="32" cy="32" r="7" stroke="currentColor" stroke-width="3"/>',
    "wrench": '<path d="M44 14a10 10 0 0 0-13 13L14 44a5 5 0 0 0 7 7l17-17a10 10 0 0 0 13-13l-7 7-6-1-1-6 7-7z" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/>',
    "constellation": '<circle cx="32" cy="32" r="6" stroke="currentColor" stroke-width="3"/><circle cx="14" cy="16" r="3" stroke="currentColor" stroke-width="3"/><circle cx="50" cy="18" r="3" stroke="currentColor" stroke-width="3"/><circle cx="48" cy="48" r="3" stroke="currentColor" stroke-width="3"/><circle cx="16" cy="48" r="3" stroke="currentColor" stroke-width="3"/><path d="M27 28L16 18M37 29l11-9M37 36l9 10M27 36l-9 10" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>',
    "bubble": '<path d="M10 14h44v28H30l-12 10v-10H10z" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/><path d="M20 24h24M20 32h16" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>',
    "cards": '<rect x="14" y="16" width="26" height="34" rx="3" transform="rotate(-8 27 33)" stroke="currentColor" stroke-width="3"/><rect x="26" y="14" width="26" height="34" rx="3" transform="rotate(6 39 31)" stroke="currentColor" stroke-width="3"/>',
    "spiral": '<path d="M32 32a6 6 0 1 1 6 6 12 12 0 1 1-12-12 18 18 0 1 1 18 18" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>',
    "scale": '<path d="M32 10v40M18 50h28" stroke="currentColor" stroke-width="3" stroke-linecap="round"/><path d="M14 20h36" stroke="currentColor" stroke-width="3" stroke-linecap="round"/><path d="M14 20l-6 12a7 7 0 0 0 12 0L14 20zM50 20l-6 12a7 7 0 0 0 12 0L50 20z" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/>',
    "mountain": '<path d="M6 50l16-30 10 16 8-12 18 26z" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/><path d="M18 28l4 6 4-4" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>',
    "book": '<path d="M32 16C26 12 16 12 12 14v34c4-2 14-2 20 2 6-4 16-4 20-2V14c-4-2-14-2-20 2z" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/><path d="M32 18v34" stroke="currentColor" stroke-width="3"/>',
}


def icon(name):
    return (
        '<div class="card-icon" aria-hidden="true">'
        '<svg viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">'
        + ICONS[name]
        + '</svg></div>'
    )


def card(c):
    cls = "card card-warning" if c.get("warn") else "card"
    if c.get("wide"):
        cls += " card-wide"
    parts = [
        f'<article class="{cls} animate-entrance" style="--i: {c["i"]}">',
        icon(c["ic"]),
        '<div class="card-content">',
        f'<h2 class="card-title">{c["t"]}</h2>',
        f'<p class="card-body">{c["b"]}</p>',
    ]
    if c.get("tip"):
        parts.append(f'<p class="card-tip">{c["tip"]}</p>')
    if c.get("det"):
        parts.append(
            '<div class="card-details"><div class="card-details-inner">' + c["det"] + '</div></div>'
        )
    parts.append('</div></article>')
    return "\n".join(parts)


HEAD = '''<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="theme-color" content="#ffffff">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;500;700;800&family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,600;0,7..72,700;1,7..72,400&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="{css}">
</head>
<body>
    <a href="#conteudo" class="skip-link">Ir para o conteúdo</a>
    <div class="page">'''

FOOT = '''        <footer class="footer">
            <p class="footer-credit">Story · Robert McKee</p>
        </footer>
    </div>
    <script src="{script}"></script>
</body>
</html>
'''


def chapter_page(ch, prev_href, prev_label, next_href, next_label):
    cards_html = "\n".join(card({**c, "i": idx + 1}) for idx, c in enumerate(ch["cards"]))
    lessons_html = "\n".join(f"<li>{x}</li>" for x in ch["lessons"])
    li = len(ch["cards"]) + 1
    html = HEAD.format(title=f'{ch["sub"]} | Story (McKee) | Biblioteca', css="../assets/style.css")
    html += f'''
        <nav aria-label="Navegação principal">
            <a href="../story-mckee.html" class="back-link"><span class="icon-arrow" aria-hidden="true">&larr;</span> Voltar para Visão Geral</a>
        </nav>

        <header class="header animate-entrance" style="--i: 0">
            <h1 class="header-title">
                <span class="header-title-light">STORY</span>
                <span class="header-title-bold">McKEE</span>
            </h1>
            <p class="header-subtitle">{ch["sub"]}</p>
            <p class="header-credit">Robert McKee</p>
            <p class="header-intro">{ch["intro"]}</p>
        </header>

        <main id="conteudo">
            <div class="grid">
{cards_html}
            </div>

            <section class="lessons animate-entrance" style="--i: {li}">
                <h2 class="lessons-title">{ch["lessons_title"]}</h2>
                <ul class="lessons-list">
{lessons_html}
                </ul>
            </section>

            <nav aria-label="Navegação entre capítulos" class="chapter-nav">
                <a href="{prev_href}" class="chapter-nav-link">{prev_label}</a>
                <a href="{next_href}" class="chapter-nav-link">{next_label}</a>
            </nav>
        </main>
'''
    html += FOOT.format(script="script.js")
    return html


# script.js (expansão de card)
SCRIPT_JS = """document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.card').forEach(card => {
        card.addEventListener('click', () => {
            if (card.querySelector('.card-details')) card.classList.toggle('expanded');
        });
    });
});
"""


def overview_page(chapters):
    links = "\n".join(
        f'                            <a href="story-mckee/{ch["slug"]}.html" class="chapter-link">{ch["sub"].replace("CAPÍTULO", "Cap.")} <span class="arrow" aria-hidden="true">&rarr;</span></a>'
        for ch in chapters
    )
    html = HEAD.format(title="Visão Geral: Story (McKee) | Biblioteca", css="assets/style.css")
    html += (
        '''
        <nav aria-label="Navegação Voltar">
            <a href="index.html" class="back-link"><span class="icon-arrow" aria-hidden="true">&larr;</span> Voltar para a Biblioteca</a>
        </nav>

        <header class="header animate-entrance" style="--i: 0">
            <h1 class="header-title">
                <span class="header-title-light">STORY</span>
                <span class="header-title-bold">McKEE</span>
            </h1>
            <p class="header-subtitle">VISÃO GERAL · OS PRINCÍPIOS DO ROTEIRO</p>
            <p class="header-credit">Robert McKee</p>
            <p class="header-intro">
                A bíblia do roteiro. McKee transforma os princípios eternos da narrativa — estrutura, personagem e significado — num método prático: o evento que dispara a história (o Incidente Incitante), a força que a empurra adiante (A Lacuna, entre o que se espera e o que acontece), a oposição que a torna grandiosa (o Princípio do Antagonismo) e a virada que a encerra (o Clímax). Esta é a referência rápida, capítulo a capítulo.
            </p>
        </header>

        <main id="conteudo">
            <div class="grid">

                <article class="card animate-entrance" style="--i: 1">
                    <div class="card-icon" aria-hidden="true">
                        <svg viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">'''
        + ICONS["target"]
        + '''</svg>
                    </div>
                    <div class="card-content">
                        <h2 class="card-title">Os 5 Frameworks Centrais</h2>
                        <p class="card-body">A caixa de ferramentas de McKee:</p>
                        <ul class="content-list">
                            <li><strong>O Espectro Estrutural:</strong> Arquitrama, Minitrama, Antitrama.</li>
                            <li><strong>Personagem vs. Caracterização:</strong> quem você é se revela na escolha sob pressão.</li>
                            <li><strong>A Lacuna:</strong> o abismo entre expectativa e resultado move a narrativa.</li>
                            <li><strong>O Princípio do Antagonismo:</strong> o herói só é tão grande quanto a oposição o força a ser.</li>
                            <li><strong>O Incidente Incitante:</strong> a faísca que desequilibra a vida e lança a história.</li>
                        </ul>
                    </div>
                </article>

                <article class="card animate-entrance" style="--i: 2">
                    <div class="card-icon" aria-hidden="true">
                        <svg viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">'''
        + ICONS["fork"]
        + '''</svg>
                    </div>
                    <div class="card-content">
                        <h2 class="card-title">O Teste de Design</h2>
                        <p class="card-body">Três perguntas sobre o protagonista — se alguma for fraca, a história falha:</p>
                        <ul class="content-list">
                            <li><strong>O que ele quer?</strong> (desejo consciente e/ou inconsciente)</li>
                            <li><strong>O que acontece se ele não conseguir?</strong> (os riscos — idealmente vida ou morte)</li>
                            <li><strong>O que o impede?</strong> (forças de antagonismo: interna, pessoal, extrapessoal)</li>
                        </ul>
                    </div>
                </article>

                <article class="card card-wide animate-entrance" style="--i: 3">
                    <div class="card-content">
                        <h2 class="card-title">Checklist da Cena</h2>
                        <p class="card-body">Antes de escrever qualquer cena, verifique:</p>
                        <div class="table-scroll">
                            <table class="data-table">
                                <tr><th>Pergunta</th><th>Regra</th><th>Por quê</th></tr>
                                <tr><td><strong>A cena vira?</strong></td><td>A carga de valor muda do início ao fim</td><td>Mesma carga = atividade, não ação. Corte ou redesenhe.</td></tr>
                                <tr><td><strong>Onde está o subtexto?</strong></td><td>Personagens dizem uma coisa, querem outra</td><td>Se a cena é sobre o que ela é sobre, está “na cara”.</td></tr>
                                <tr><td><strong>Onde está a Lacuna?</strong></td><td>Expectativa colide com a realidade</td><td>O mundo reage diferente — esse é o pivô da cena.</td></tr>
                                <tr><td><strong>É escolha verdadeira?</strong></td><td>Bens irreconciliáveis ou mal menor</td><td>Bem-contra-mal não é escolha dramática.</td></tr>
                            </table>
                        </div>
                    </div>
                </article>

                <article class="card card-wide animate-entrance" style="--i: 4">
                    <div class="card-content">
                        <h2 class="card-title">Aprofunde-se nos Capítulos</h2>
                        <p class="card-body">As notas detalhadas dos 19 capítulos de <em>Story</em>:</p>
                        <nav aria-label="Navegação de Capítulos" class="chapter-list">
'''
        + links
        + '''
                        </nav>
                    </div>
                </article>
            </div>
        </main>
'''
    )
    html += FOOT.format(script="story-mckee/script.js")
    return html


if __name__ == "__main__":
    from story_data import CHAPTERS  # noqa

    # script.js
    with open(os.path.join(OUT_DIR, "script.js"), "w", encoding="utf-8") as f:
        f.write(SCRIPT_JS)
    # capítulos
    n = len(CHAPTERS)
    for idx, ch in enumerate(CHAPTERS):
        prev_href = "../story-mckee.html" if idx == 0 else CHAPTERS[idx - 1]["slug"] + ".html"
        prev_label = "&larr; Visão Geral" if idx == 0 else "&larr; Anterior"
        next_href = "../story-mckee.html" if idx == n - 1 else CHAPTERS[idx + 1]["slug"] + ".html"
        next_label = "Visão Geral &rarr;" if idx == n - 1 else "Próximo &rarr;"
        html = chapter_page(ch, prev_href, prev_label, next_href, next_label)
        with open(os.path.join(OUT_DIR, ch["slug"] + ".html"), "w", encoding="utf-8") as f:
            f.write(html)
    # visão geral
    with open(os.path.join(BASE, "story-mckee.html"), "w", encoding="utf-8") as f:
        f.write(overview_page(CHAPTERS))
    print(f"OK: {n} capítulos + visão geral + script.js gerados em {OUT_DIR}")
