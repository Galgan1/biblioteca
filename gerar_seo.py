# -*- coding: utf-8 -*-
"""SEO da Biblioteca (pilar 4): sitemap.xml + robots.txt + JSON-LD + canonical.

Idempotente. Lê books.json e os HTML existentes; NÃO regenera páginas.
  - sitemap.xml: home + páginas de livro (Visão Geral) + TODOS os capítulos (lastmod = mtime).
  - robots.txt: libera tudo + aponta o sitemap.
  - index.html: injeta JSON-LD (WebSite + CollectionPage com ItemList dos livros lê-veis) + canonical.
  - <slug>.html (cada livro com página): injeta JSON-LD (Book + BreadcrumbList) + canonical.
Bloco injetado entre marcadores <!-- seo:start --> / <!-- seo:end --> (re-escrito a cada rodada).

Uso:  python gerar_seo.py
"""

import json
import os
import re
import sys
import glob
from datetime import date

BASE = "https://www.andregalgani.com.br/biblioteca"
SITE_NAME = "Biblioteca André Galgani"
AUTHOR = "André Galgani"
ROOT = os.path.dirname(os.path.abspath(__file__))

SEO_RE = re.compile(r'\n?[ \t]*<!-- seo:start -->.*?<!-- seo:end -->', re.S)
TITLE_RE = re.compile(r'<title>(.*?)</title>', re.S | re.I)


def absurl(rel):
    return BASE + "/" + rel.replace("\\", "/").lstrip("/")


def mtime(path):
    return date.fromtimestamp(os.path.getmtime(path)).isoformat()


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def write(path, text):
    with open(path, "w", encoding="utf-8", newline='\n') as f:
        f.write(text)


def ld(obj):
    return json.dumps(obj, ensure_ascii=False, indent=2)


def inject(html, canonical, jsonld):
    """Substitui (ou insere antes de </head>) o bloco SEO."""
    block = (
        '\n    <!-- seo:start -->'
        f'\n    <link rel="canonical" href="{canonical}">'
        '\n    <script type="application/ld+json">'
        f'\n{jsonld}'
        '\n    </script>'
        '\n    <!-- seo:end -->'
    )
    html = SEO_RE.sub("", html)
    return html.replace("</head>", block + "\n</head>", 1)


def chapter_files(slug):
    files = sorted(glob.glob(os.path.join(ROOT, slug, "*.html")))
    return [os.path.relpath(f, ROOT) for f in files]


def chapter_name(html, fallback):
    """Nome do capítulo a partir do <title> ('CAPÍTULO N: X | Livro | Biblioteca')."""
    m = TITLE_RE.search(html)
    if not m:
        return fallback
    return m.group(1).split("|")[0].strip() or fallback


def main():
    books = json.loads(read(os.path.join(ROOT, "books.json")))
    readable = [b for b in books if not b.get("comingSoon") and b.get("url")]

    # ---------- sitemap.xml ----------
    entries = []  # (loc, lastmod, priority)
    entries.append((BASE + "/", mtime(os.path.join(ROOT, "index.html")), "1.0"))
    for b in readable:
        f = os.path.join(ROOT, b["url"])
        if os.path.exists(f):
            entries.append((absurl(b["url"]), mtime(f), "0.8"))
    for b in readable:
        for ch in chapter_files(b["id"]):
            entries.append((absurl(ch), mtime(os.path.join(ROOT, ch)), "0.6"))

    urls = "\n".join(
        f"  <url><loc>{loc}</loc><lastmod>{lm}</lastmod>"
        f"<changefreq>monthly</changefreq><priority>{pr}</priority></url>"
        for loc, lm, pr in entries
    )
    sitemap = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{urls}\n</urlset>\n"
    )
    write(os.path.join(ROOT, "sitemap.xml"), sitemap)

    # ---------- robots.txt ----------
    write(
        os.path.join(ROOT, "robots.txt"),
        "User-agent: *\nAllow: /\n\nSitemap: " + BASE + "/sitemap.xml\n",
    )

    # ---------- JSON-LD: home ----------
    item_list = [
        {"@type": "ListItem", "position": i + 1, "url": absurl(b["url"]), "name": b["title"]}
        for i, b in enumerate(readable)
    ]
    home_ld = ld(
        {
            "@context": "https://schema.org",
            "@graph": [
                {
                    "@type": "WebSite",
                    "@id": BASE + "/#website",
                    "url": BASE + "/",
                    "name": SITE_NAME,
                    "inLanguage": "pt-BR",
                    "publisher": {"@type": "Person", "name": AUTHOR},
                },
                {
                    "@type": "CollectionPage",
                    "@id": BASE + "/#biblioteca",
                    "url": BASE + "/",
                    "name": "Biblioteca",
                    "isPartOf": {"@id": BASE + "/#website"},
                    "inLanguage": "pt-BR",
                    "description": "Livros inteiros, destilados numa página. Resumos visuais, capítulo a capítulo.",
                    "mainEntity": {
                        "@type": "ItemList",
                        "numberOfItems": len(item_list),
                        "itemListElement": item_list,
                    },
                },
            ],
        }
    )
    idx = os.path.join(ROOT, "index.html")
    write(idx, inject(read(idx), BASE + "/", home_ld))

    # ---------- JSON-LD: cada página de livro ----------
    n_book = 0
    for b in readable:
        f = os.path.join(ROOT, b["url"])
        if not os.path.exists(f):
            continue
        page = absurl(b["url"])
        book_ld = ld(
            {
                "@context": "https://schema.org",
                "@graph": [
                    {
                        "@type": "Book",
                        "@id": page + "#book",
                        "name": b["title"],
                        "author": {"@type": "Person", "name": b["author"]},
                        "description": b.get("description", ""),
                        "image": absurl(b["coverUrl"]),
                        "url": page,
                        "inLanguage": "pt-BR",
                        "genre": b.get("tags", []),
                    },
                    {
                        "@type": "BreadcrumbList",
                        "itemListElement": [
                            {
                                "@type": "ListItem",
                                "position": 1,
                                "name": "Biblioteca",
                                "item": BASE + "/",
                            },
                            {"@type": "ListItem", "position": 2, "name": b["title"], "item": page},
                        ],
                    },
                ],
            }
        )
        write(f, inject(read(f), page, book_ld))
        n_book += 1

    # ---------- JSON-LD: capítulos (Article + BreadcrumbList) ----------
    n_ch = 0
    for b in readable:
        page = absurl(b["url"])
        cover = absurl(b["coverUrl"])
        for ch in chapter_files(b["id"]):
            f = os.path.join(ROOT, ch)
            html = read(f)
            name = chapter_name(html, b["title"])
            ch_url = absurl(ch)
            ch_ld = ld(
                {
                    "@context": "https://schema.org",
                    "@graph": [
                        {
                            "@type": "Article",
                            "@id": ch_url + "#article",
                            "headline": name,
                            "inLanguage": "pt-BR",
                            "url": ch_url,
                            "image": cover,
                            "author": {"@type": "Person", "name": b["author"]},
                            "isPartOf": {
                                "@type": "Book",
                                "@id": page + "#book",
                                "name": b["title"],
                            },
                        },
                        {
                            "@type": "BreadcrumbList",
                            "itemListElement": [
                                {
                                    "@type": "ListItem",
                                    "position": 1,
                                    "name": "Biblioteca",
                                    "item": BASE + "/",
                                },
                                {
                                    "@type": "ListItem",
                                    "position": 2,
                                    "name": b["title"],
                                    "item": page,
                                },
                                {"@type": "ListItem", "position": 3, "name": name, "item": ch_url},
                            ],
                        },
                    ],
                }
            )
            write(f, inject(html, ch_url, ch_ld))
            n_ch += 1

    print(
        f"sitemap.xml: {len(entries)} URLs | robots.txt | "
        f"JSON-LD em index.html + {n_book} páginas de livro + {n_ch} capítulos"
    )


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    main()
