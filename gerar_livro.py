# -*- coding: utf-8 -*-
"""GERADOR UNIVERSAL de livro para a biblioteca (padrão "Cheat Sheet Verde").

Lê  <slug>_data.py  (que define BOOK e CHAPTERS) e produz:
  <slug>.html                  visão geral
  <slug>/chNN-*.html           uma página cheat sheet por capítulo
e registra/atualiza o livro em books.json. O JS é ÚNICO e compartilhado
(assets/script-livro.js — botões de PDF + expansão); nenhuma cópia por-livro.

Uso:  python gerar_livro.py <slug>

BOOK = {
  "slug","title","author","header_light","header_bold","subtitle","intro",
  "description","tags":[...],"cover":"assets/<slug>-cover.png","progress":"N Capítulos",
  "overview_cards":[ {ic,t,b,tip?,list?,wide?,warn?,det?}, ... ]   # opcional
}
CHAPTERS = [ {"slug","sub","intro","cards":[...],"lessons_title","lessons":[...]} ]
"""
import os, sys, json, importlib
from datetime import date

BASE = os.path.dirname(os.path.abspath(__file__))
SITE_URL = 'https://www.andregalgani.com.br/biblioteca/'
TODAY = date.today().isoformat()

ICONS = {
    "masks": '<path d="M10 14h18v14a9 9 0 0 1-18 0z" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/><path d="M15 20h3M22 20h1" stroke="currentColor" stroke-width="3" stroke-linecap="round"/><path d="M14 26a5 4 0 0 0 10 0" stroke="currentColor" stroke-width="3" stroke-linecap="round"/><path d="M36 18h18v14a9 9 0 0 1-18 0z" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/><path d="M41 24h3M48 24h1" stroke="currentColor" stroke-width="3" stroke-linecap="round"/><path d="M40 32a5 4 0 0 1 10 0" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>',
    "triangle": '<path d="M32 10L56 52H8L32 10z" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/><circle cx="32" cy="22" r="2" fill="currentColor"/>',
    "clock": '<circle cx="32" cy="32" r="22" stroke="currentColor" stroke-width="3"/><path d="M32 18v14l10 6" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>',
    "pin": '<path d="M32 56s16-14 16-28a16 16 0 0 0-32 0c0 14 16 28 16 28z" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/><circle cx="32" cy="28" r="6" stroke="currentColor" stroke-width="3"/>',
    "gap": '<path d="M10 32h16M38 32h16" stroke="currentColor" stroke-width="3" stroke-linecap="round"/><path d="M22 24l-6 8 6 8M42 24l6 8-6 8" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>',
    "person": '<circle cx="32" cy="20" r="10" stroke="currentColor" stroke-width="3"/><path d="M14 52c0-10 8-18 18-18s18 8 18 18" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>',
    "mask": '<path d="M14 14h36v18c0 12-9 22-18 22s-18-10-18-22z" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/><circle cx="24" cy="28" r="3" stroke="currentColor" stroke-width="3"/><circle cx="40" cy="28" r="3" stroke="currentColor" stroke-width="3"/><path d="M26 40a8 6 0 0 0 12 0" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>',
    "bulb": '<path d="M22 44a14 14 0 1 1 20 0c-2 2-3 4-3 7H25c0-3-1-5-3-7z" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/><path d="M26 56h12" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>',
    "target": '<circle cx="32" cy="32" r="22" stroke="currentColor" stroke-width="3"/><circle cx="32" cy="32" r="12" stroke="currentColor" stroke-width="3"/><circle cx="32" cy="32" r="2.5" fill="currentColor"/>',
    "spark": '<path d="M34 8L18 36h12l-4 20 20-30H34l4-18z" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/>',
    "steps": '<path d="M10 52h12V40h12V28h12V16h8" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>',
    "pivot": '<path d="M16 32a16 16 0 1 1 6 12" stroke="currentColor" stroke-width="3" stroke-linecap="round"/><path d="M16 24v10h10" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>',
    "layers": '<path d="M32 10L54 22 32 34 10 22 32 10z" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/><path d="M10 32l22 12 22-12M10 42l22 12 22-12" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/>',
    "lens": '<circle cx="28" cy="28" r="16" stroke="currentColor" stroke-width="3"/><path d="M40 40l12 12" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>',
    "link": '<path d="M26 38l12-12" stroke="currentColor" stroke-width="3" stroke-linecap="round"/><path d="M22 32l-6 6a8 8 0 0 0 11 11l6-6" stroke="currentColor" stroke-width="3" stroke-linecap="round"/><path d="M42 32l6-6a8 8 0 0 0-11-11l-6 6" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>',
    "fork": '<path d="M32 56V34" stroke="currentColor" stroke-width="3" stroke-linecap="round"/><path d="M32 34L16 14M32 34l16-20" stroke="currentColor" stroke-width="3" stroke-linecap="round"/><circle cx="16" cy="12" r="4" stroke="currentColor" stroke-width="3"/><circle cx="48" cy="12" r="4" stroke="currentColor" stroke-width="3"/>',
    "sword": '<path d="M44 12l8 8-22 22-8-8 22-22z" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/><path d="M22 42l-8 8M12 44l8 8" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>',
    "eye": '<path d="M6 32s10-16 26-16 26 16 26 16-10 16-26 16S6 32 6 32z" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/><circle cx="32" cy="32" r="7" stroke="currentColor" stroke-width="3"/>',
    "wrench": '<path d="M44 14a10 10 0 0 0-13 13L14 44a5 5 0 0 0 7 7l17-17a10 10 0 0 0 13-13l-7 7-6-1-1-6 7-7z" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/>',
    "constellation": '<circle cx="32" cy="32" r="6" stroke="currentColor" stroke-width="3"/><circle cx="14" cy="16" r="3" stroke="currentColor" stroke-width="3"/><circle cx="50" cy="18" r="3" stroke="currentColor" stroke-width="3"/><circle cx="48" cy="48" r="3" stroke="currentColor" stroke-width="3"/><circle cx="16" cy="48" r="3" stroke="currentColor" stroke-width="3"/><path d="M27 28L16 18M37 29l11-9M37 36l9 10M27 36l-9 10" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>',
    "bubble": '<path d="M10 14h44v28H30l-12 10v-10H10z" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/><path d="M20 24h24M20 32h16" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>',
    "cards": '<rect x="14" y="16" width="26" height="34" rx="3" transform="rotate(-8 27 33)" stroke="currentColor" stroke-width="3"/><rect x="26" y="14" width="26" height="34" rx="3" transform="rotate(6 39 31)" stroke="currentColor" stroke-width="3"/>',
    "spiral": '<path d="M32 32a6 6 0 1 1 6 6 12 12 0 1 1-12-12 18 18 0 1 1 18 18" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>',
    "scale": '<path d="M32 10v40M18 50h28" stroke="currentColor" stroke-width="3" stroke-linecap="round"/><path d="M14 20h36" stroke="currentColor" stroke-width="3" stroke-linecap="round"/><path d="M14 20l-6 12a7 7 0 0 0 12 0L14 20zM50 20l-6 12a7 7 0 0 0 12 0L50 20z" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/>',
    "mountain": '<path d="M6 50l16-30 10 16 8-12 18 26z" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/>',
    "book": '<path d="M32 16C26 12 16 12 12 14v34c4-2 14-2 20 2 6-4 16-4 20-2V14c-4-2-14-2-20 2z" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/><path d="M32 18v34" stroke="currentColor" stroke-width="3"/>',
    "leaf": '<path d="M48 14C28 14 14 28 14 48c20 0 34-14 34-34z" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/><path d="M22 42L42 22" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>',
    "wave": '<path d="M6 38c6-8 12-8 18 0s12 8 18 0 12-8 16 0" stroke="currentColor" stroke-width="3" stroke-linecap="round"/><path d="M6 26c6-8 12-8 18 0s12 8 18 0 12-8 16 0" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>',
    "key": '<circle cx="22" cy="22" r="12" stroke="currentColor" stroke-width="3"/><path d="M30 30l22 22M44 44l6-6M38 50l6-6" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>',
}


def icon(name):
    return ('<div class="card-icon" aria-hidden="true">'
            '<svg viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">'
            + ICONS.get(name, ICONS["book"]) + '</svg></div>')


def card(c):
    cls = "card card-warning" if c.get("warn") else "card"
    if c.get("wide"):
        cls += " card-wide"
    parts = [f'<article class="{cls} animate-entrance" style="--i: {c["i"]}">',
             icon(c["ic"]), '<div class="card-content">',
             f'<h2 class="card-title">{c["t"]}</h2>',
             f'<p class="card-body">{c["b"]}</p>']
    if c.get("list"):
        parts.append('<ul class="content-list">' + "".join(f'<li>{x}</li>' for x in c["list"]) + '</ul>')
    if c.get("tip"):
        parts.append(f'<p class="card-tip">{c["tip"]}</p>')
    if c.get("det"):
        parts.append('<div class="card-details"><div class="card-details-inner">' + c["det"] + '</div></div>')
    parts.append('</div></article>')
    return "\n".join(parts)


def _og_img_url(slug):
    """Usa og banner por-livro se existir (Fase 5), senão cai no genérico."""
    per_book = os.path.join(BASE, 'assets', f'{slug}-og.png')
    name = f'{slug}-og.png' if os.path.exists(per_book) else 'og-banner.png'
    return SITE_URL + 'assets/' + name


def head(title, css, og_title='', og_desc='', og_type='article', og_url='', og_img=''):
    og = ''
    if og_title:
        og = (f'    <meta property="og:type" content="{og_type}">\n'
              f'    <meta property="og:locale" content="pt_BR">\n'
              f'    <meta property="og:site_name" content="Biblioteca André Galgani">\n'
              f'    <meta property="og:title" content="{og_title}">\n'
              f'    <meta property="og:description" content="{og_desc}">\n'
              f'    <meta property="og:image" content="{og_img}">\n'
              f'    <meta property="og:image:width" content="1200">\n'
              f'    <meta property="og:image:height" content="630">\n'
              f'    <meta property="og:url" content="{og_url}">\n'
              f'    <meta name="twitter:card" content="summary_large_image">\n')
    return (f'<!DOCTYPE html>\n<html lang="pt-BR">\n<head>\n'
            f'    <meta charset="UTF-8">\n'
            f'    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
            f'    <title>{title}</title>\n'
            f'    <meta name="theme-color" media="(prefers-color-scheme: light)" content="#fcfdfc">\n'
            f'    <meta name="theme-color" media="(prefers-color-scheme: dark)" content="#1c1f1d">\n'
            f'{og}'
            f'    <link rel="preconnect" href="https://fonts.googleapis.com">\n'
            f'    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
            f'    <link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;500;700;800&family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,600;0,7..72,700;1,7..72,400&display=swap" rel="stylesheet">\n'
            f'    <link rel="stylesheet" href="{css}">\n'
            f'</head>\n<body>\n'
            f'    <a href="#conteudo" class="skip-link">Ir para o conteúdo</a>\n'
            f'    <div class="page">')

FOOT = '''        <footer class="footer">
            <p class="footer-credit">{credit}</p>
        </footer>
    </div>
    <script defer src="{script}"></script>
</body>
</html>
'''


def header_block(B, subtitle, intro):
    return f'''
        <header class="header animate-entrance" style="--i: 0">
            <h1 class="header-title">
                <span class="header-title-light">{B["header_light"]}</span>
                <span class="header-title-bold">{B["header_bold"]}</span>
            </h1>
            <p class="header-subtitle">{subtitle}</p>
            <p class="header-credit">{B["author"]}</p>
            <p class="header-intro">{intro}</p>
        </header>'''


def chapter_page(B, ch, prev_href, prev_label, next_href, next_label):
    cards_html = "\n".join(card({**c, "i": i + 1}) for i, c in enumerate(ch["cards"]))
    lessons_html = "\n".join(f"<li>{x}</li>" for x in ch.get("lessons", []))
    li = len(ch["cards"]) + 1
    page_title = f'{ch["sub"]} | {B["title"]} | Biblioteca'
    og_title = (f'{ch["sub"]} · {B["title"]}')[:65]
    og_desc = ch.get("intro", B.get("description", ""))[:155]
    og_url = SITE_URL + f'{B["slug"]}/{ch["slug"]}.html'
    jsonld = (f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Article",'
              f'"headline":{json.dumps(og_title)},"description":{json.dumps(og_desc)},'
              f'"author":{{"@type":"Person","name":{json.dumps(B["author"])}}},'
              f'"datePublished":"{TODAY}","dateModified":"{TODAY}","inLanguage":"pt-BR"}}</script>')
    html = head(page_title, "../assets/style.css",
                og_title=og_title, og_desc=og_desc, og_type='article',
                og_url=og_url, og_img=_og_img_url(B["slug"])) + '\n' + jsonld
    html += f'''
        <nav class="crumbs" aria-label="Trilha de navegação">
            <a class="crumbs-home" href="../index.html">Biblioteca</a>
            <span class="crumbs-sep" aria-hidden="true">›</span>
            <a href="../{B["slug"]}.html">{B["title"]}</a>
            <span class="crumbs-sep" aria-hidden="true">›</span>
            <span class="crumbs-current" aria-current="page">{ch["sub"].replace("CAPÍTULO", "Cap.").replace("Capítulo", "Cap.")}</span>
        </nav>
{header_block(B, ch["sub"], ch["intro"])}
        <main id="conteudo">
            <div class="grid">
{cards_html}
            </div>'''
    if ch.get("lessons"):
        html += f'''
            <section class="lessons animate-entrance" style="--i: {li}">
                <h2 class="lessons-title">{ch.get("lessons_title", "Lições-Chave")}</h2>
                <ul class="lessons-list">
{lessons_html}
                </ul>
            </section>'''
    html += f'''
            <nav aria-label="Navegação entre capítulos" class="chapter-nav">
                <a href="{prev_href}" class="chapter-nav-link" rel="prev">{prev_label}</a>
                <a href="{next_href}" class="chapter-nav-link" rel="next">{next_label}</a>
            </nav>
        </main>
'''
    html += FOOT.format(credit=f'{B["title"]} · {B["author"]}', script="../assets/script-livro.js")
    return html


def overview_page(B, chapters):
    links = "\n".join(
        f'                            <a href="{B["slug"]}/{ch["slug"]}.html" class="chapter-link">{ch["sub"].replace("CAPÍTULO", "Cap.").replace("Capítulo", "Cap.")} <span class="arrow" aria-hidden="true">&rarr;</span></a>'
        for ch in chapters)
    og_title = f'{B["title"]} · Resumo Completo'
    og_desc = B.get("description", "")[:155]
    og_url = SITE_URL + f'{B["slug"]}.html'
    jsonld = (f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Book",'
              f'"name":{json.dumps(B["title"])},"author":{{"@type":"Person","name":{json.dumps(B["author"])}}},'
              f'"description":{json.dumps(og_desc)},'
              f'"inLanguage":"pt-BR","datePublished":"{TODAY}","dateModified":"{TODAY}"}}</script>')
    html = head(f'Visão Geral: {B["title"]} | Biblioteca', "assets/style.css",
                og_title=og_title, og_desc=og_desc, og_type='book',
                og_url=og_url, og_img=_og_img_url(B["slug"])) + '\n' + jsonld
    html += f'''
        <nav class="crumbs" aria-label="Trilha de navegação">
            <a class="crumbs-home" href="index.html">Biblioteca</a>
            <span class="crumbs-sep" aria-hidden="true">›</span>
            <span class="crumbs-current" aria-current="page">{B["title"]}</span>
        </nav>
{header_block(B, B.get("subtitle", "VISÃO GERAL"), B["intro"])}
        <main id="conteudo">
            <div class="grid">
'''
    ov = list(B.get("overview_cards", []))
    html += "\n".join(card({**c, "i": i + 1}) for i, c in enumerate(ov))
    html += f'''
                <article class="card card-wide animate-entrance" style="--i: {len(ov)+1}">
                    <div class="card-content">
                        <h2 class="card-title">Aprofunde-se nos Capítulos</h2>
                        <p class="card-body">As notas detalhadas dos {len(chapters)} capítulos do livro:</p>
                        <nav aria-label="Navegação de Capítulos" class="chapter-list">
{links}
                        </nav>
                    </div>
                </article>
            </div>
        </main>
'''
    html += FOOT.format(credit=f'{B["title"]} · {B["author"]}', script="assets/script-livro.js")
    return html


def update_books_json(B):
    path = os.path.join(BASE, "books.json")
    data = json.load(open(path, encoding="utf-8"))
    entry = {"id": B["slug"], "title": B["title"], "author": B["author"],
             "coverUrl": f'assets/{B["slug"]}-capa.png',
             "description": B["description"], "tags": B.get("tags", []),
             "progress": B.get("progress", f'{B["_n"]} Capítulos'),
             "url": f'{B["slug"]}.html'}
    data = [e for e in data if e.get("id") != B["slug"]] + [entry]
    json.dump(data, open(path, "w", encoding="utf-8", newline='\n'), ensure_ascii=False, indent=2)


def main(slug):
    data = importlib.import_module(f"{slug.replace('-', '_')}_data")
    B, CH = data.BOOK, data.CHAPTERS
    B["slug"], B["_n"] = slug, len(CH)
    out = os.path.join(BASE, slug)
    os.makedirs(out, exist_ok=True)

    n = len(CH)
    for i, ch in enumerate(CH):
        prev_href = f'../{slug}.html' if i == 0 else CH[i - 1]["slug"] + ".html"
        prev_label = "&larr; Visão Geral" if i == 0 else "&larr; Anterior"
        next_href = f'../{slug}.html' if i == n - 1 else CH[i + 1]["slug"] + ".html"
        next_label = "Visão Geral &rarr;" if i == n - 1 else "Próximo &rarr;"
        open(os.path.join(out, ch["slug"] + ".html"), "w", encoding="utf-8", newline='\n').write(
            chapter_page(B, ch, prev_href, prev_label, next_href, next_label))

    open(os.path.join(BASE, slug + ".html"), "w", encoding="utf-8", newline='\n').write(overview_page(B, CH))
    update_books_json(B)
    print(f"OK: {slug} — {n} capítulos + visão geral; books.json atualizado (JS único compartilhado).")
    # Kit de Divulgação: emite os dados do carrossel (slides.json + caps.json) p/ o
    # serviço gerar sob demanda. Import tardio evita ciclo (gerar_carrossel→gerar_livro).
    try:
        import gerar_dados_carrossel as _gdc
        ncap = _gdc.emit(slug)
        print(f"     + kit: {ncap} capítulos de carrossel emitidos (assets/kit/{slug}/)")
    except Exception as e:
        print(f"     [!] kit não emitido para {slug}: {e}")
    # Kit de Divulgação: peças estáticas (ideia/citação/capa/mapa/thumb) + manifest.
    try:
        import gerar_dados_kit as _gdk
        npg = _gdk.emit(slug)
        print(f"     + kit: {len(npg)} peças estáticas + manifest (assets/kit/_tpl/{slug}/)")
    except Exception as e:
        print(f"     [!] peças estáticas não emitidas para {slug}: {e}")


if __name__ == "__main__":
    main(sys.argv[1])
