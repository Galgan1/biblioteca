# -*- coding: utf-8 -*-
"""Retrofit Fase 2+3: navegação nomeada, favicon, Open Graph e link da estante
no rodapé, em todas as páginas existentes. Idempotente (pode rodar de novo)."""
import json
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).parent
BASE = "https://www.andregalgani.com.br/biblioteca"
books = json.loads((ROOT / "books.json").read_text(encoding="utf-8"))


def _safe_write(path, text):
    # Windows devolve OSError [Errno 22]/lock transitório ao reabrir arquivo p/ escrita
    # logo após gravá-lo (AV/indexer) durante a gravação em lote. Retry curto resolve.
    for tentativa in range(6):
        try:
            path.write_text(text, encoding="utf-8", newline='\n')
            return
        except (OSError, PermissionError):
            if tentativa == 5:
                raise
            time.sleep(0.15 * (tentativa + 1))

ARROW_L = "←"  # ←
ARROW_R = "→"  # →

# Livros com pele temática própria (fundo escuro em qualquer modo) → a barra
# do navegador no celular deve casar com o fundo da pele, não com o papel claro.
# Chave = classe do <body>; valor = cor de fundo base da pele.
SKIN_THEME = {"psy": "#0a0118", "zen": "#0b1a17"}


def shorten(name, limit=44):
    name = re.sub(r"\s+", " ", name).strip()
    if len(name) <= limit:
        return name
    cut = name[:limit].rsplit(" ", 1)[0].rstrip(" ,;:—-")
    return cut + "…"


def head_inject(html, prefix, title, desc, image, url):
    """Insere favicon + theme-color + meta description (se faltar) + OG/Twitter antes de </head>."""
    html = re.sub(r'\s*<link rel="icon"[^>]*>', "", html)
    html = re.sub(r'\s*<meta name="theme-color"[^>]*>', "", html)
    html = re.sub(r'\s*<!-- og-retrofit -->.*?<!-- /og-retrofit -->', "", html, flags=re.S)
    desc = re.sub(r"\s+", " ", desc).strip()
    if len(desc) > 155:
        desc = desc[:155].rsplit(" ", 1)[0].rstrip(" ,;:") + "…"
    has_desc = re.search(r'<meta name="description"', html)
    desc_tag = "" if has_desc else f'\n    <meta name="description" content="{desc}">'
    m_body = re.search(r'<body class="(\w+)"', html)
    skin = SKIN_THEME.get(m_body.group(1)) if m_body else None
    if skin:
        theme = f'\n    <meta name="theme-color" content="{skin}">'
    else:
        theme = ('\n    <meta name="theme-color" content="#fcfdfc" media="(prefers-color-scheme: light)">'
                 '\n    <meta name="theme-color" content="#1c1f1d" media="(prefers-color-scheme: dark)">')
    block = f"""    <link rel="icon" type="image/svg+xml" href="{prefix}assets/favicon.svg">{theme}{desc_tag}
    <!-- og-retrofit -->
    <meta property="og:type" content="article">
    <meta property="og:locale" content="pt_BR">
    <meta property="og:site_name" content="Biblioteca André Galgani">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{desc}">
    <meta property="og:image" content="{image}">
    <meta property="og:url" content="{url}">
    <meta name="twitter:card" content="summary">
    <!-- /og-retrofit -->
"""
    return html.replace("</head>", block + "</head>")


def footer_link(html, prefix):
    """Acrescenta o link da estante ao crédito do rodapé (uma vez)."""
    if 'class="footer-link"' in html:
        return html
    m = re.search(r'<p class="footer-credit">(.*?)</p>', html, flags=re.S)
    if not m:
        return html
    inner = m.group(1).strip()
    new = (f'<p class="footer-credit">{inner} · '
           f'<a class="footer-link" href="{prefix}index.html">Biblioteca</a></p>')
    return html.replace(m.group(0), new, 1)


def esc(s):
    return s.replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;")


total_pages = 0
total_nav = 0

# ---------------------------------------------------------------- index.html
idx_file = ROOT / "index.html"
idx = idx_file.read_text(encoding="utf-8")
idx = head_inject(idx, "", "Biblioteca — André Galgani",
                  "Livros inteiros, destilados numa página. Resumos visuais, capítulo a capítulo.",
                  f"{BASE}/assets/og-banner.png", f"{BASE}/")
idx = idx.replace('<meta property="og:type" content="article">',
                  '<meta property="og:type" content="website">')
idx = idx.replace('<meta name="twitter:card" content="summary">',
                  '<meta name="twitter:card" content="summary_large_image">')
_safe_write(idx_file, idx)
total_pages += 1

# ------------------------------------------------------------------- livros
for book in books:
    slug = book["id"]
    ov_file = ROOT / f"{slug}.html"
    if not ov_file.exists():
        print(f"!! sem visão geral: {slug}")
        continue
    ov = ov_file.read_text(encoding="utf-8")

    # mapa slug-do-capítulo -> nome (texto do chapter-link na visão geral)
    names = {}
    order = []
    for m in re.finditer(r'<a href="([^"]+)" class="chapter-link"[^>]*>(.*?)</a>', ov, flags=re.S):
        href, inner = m.groups()
        text = re.sub(r"<span.*?</span>", "", inner, flags=re.S)
        text = re.sub(r"<[^>]+>", "", text)
        text = re.sub(r"\s+", " ", text).strip().rstrip(ARROW_R).strip()
        page = href.split("/")[-1].replace(".html", "")
        names[page] = text
        order.append(page)

    cover = f"{BASE}/{book['coverUrl']}"
    ov = head_inject(ov, "", esc(book["title"]), esc(book["description"]), cover, f"{BASE}/{slug}.html")
    ov = footer_link(ov, "")
    _safe_write(ov_file, ov)
    total_pages += 1

    book_dir = ROOT / slug
    if not book_dir.is_dir():
        continue
    for ch_file in sorted(book_dir.glob("*.html")):
        page = ch_file.stem
        html = ch_file.read_text(encoding="utf-8")

        # título/descrição do capítulo
        m = re.search(r"<title>(.*?)</title>", html, flags=re.S)
        page_title = re.sub(r"\s+", " ", m.group(1)).strip() if m else book["title"]
        m = re.search(r'<p class="header-intro"[^>]*>(.*?)</p>', html, flags=re.S)
        intro = re.sub(r"<[^>]+>", "", m.group(1)) if m else book["description"]

        html = head_inject(html, "../", esc(page_title), esc(intro), cover, f"{BASE}/{slug}/{page}.html")
        html = footer_link(html, "../")

        # navegação nomeada
        def nav_label(href_page, is_prev):
            if href_page not in names:
                return "Visão Geral" if is_prev else None
            return shorten(names[href_page])

        def sub_prev(mm):
            href = mm.group(1)
            target = href.split("/")[-1].replace(".html", "")
            label = "Visão Geral" if href.startswith("..") else nav_label(target, True)
            if label is None:
                return mm.group(0)
            return (f'<a href="{href}" class="chapter-nav-link" rel="prev" '
                    f'aria-label="Capítulo anterior: {esc(label)}">'
                    f'<span class="cn-lab">Capítulo anterior</span>'
                    f'<span class="cn-ttl">{esc(label)}</span></a>')

        def sub_next(mm):
            href = mm.group(1)
            target = href.split("/")[-1].replace(".html", "")
            label = "Visão Geral" if href.startswith("..") else nav_label(target, False)
            if label is None:
                return mm.group(0)
            return (f'<a href="{href}" class="chapter-nav-link" rel="next" '
                    f'aria-label="Próximo capítulo: {esc(label)}">'
                    f'<span class="cn-lab">Próximo capítulo</span>'
                    f'<span class="cn-ttl">{esc(label)}</span></a>')

        n0 = html
        html = re.sub(r'<a href="([^"]+)" class="chapter-nav-link"[^>]*>\s*(?:&larr;|←)[^<]*</a>',
                      sub_prev, html)
        html = re.sub(r'<a href="([^"]+)" class="chapter-nav-link"[^>]*>[^<]*(?:&rarr;|→)\s*</a>',
                      sub_next, html)
        if html != n0:
            total_nav += 1

        _safe_write(ch_file, html)
        total_pages += 1

print(f"ok: {total_pages} páginas processadas, {total_nav} navegações nomeadas")
