# -*- coding: utf-8 -*-
"""Retrofit: injeta o breadcrumb VISIVEL (Site ID 'Biblioteca' + 'voce esta aqui')
no topo das paginas da Biblioteca, substituindo o antigo back-link. Idempotente,
agnostico de gerador, preserva todo o resto (SEO, OG, botao de PDF).

Dois modos, detectados pela nav existente:
  - CAPITULO  (nav "Navegação principal")  -> Biblioteca > Livro > Cap.
  - VISAO GERAL (nav "Navegação Voltar")    -> Biblioteca > Livro

Uso:
  python retrofit_breadcrumb.py --all                 # varre o projeto todo
  python retrofit_breadcrumb.py <a.html> [<b.html> ...]
"""
import re, json, sys
from pathlib import Path

NAV_PRINCIPAL_RE = re.compile(r'<nav aria-label="Navegação principal">.*?</nav>', re.S)
NAV_VOLTAR_RE = re.compile(r'<nav aria-label="Navegação Voltar">.*?</nav>', re.S)
JSONLD_RE = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.S)
TITLE_RE = re.compile(r'<title>(.*?)</title>', re.S)

SKIP_DIRS = {".claude", "node_modules", "pdf-service", "assets", "downloads", "pdfs",
             "_linkhub", "afiliados", "metadados", "videos", "book-to-skill",
             "ocr_data", "__pycache__", "auditoria_impeccable", "_motion"}


def _cap(s):
    return s.replace("CAPÍTULO", "Cap.").replace("Capítulo", "Cap.")


def crumbs_html(items):
    out = ['<nav class="crumbs" aria-label="Trilha de navegação">']
    for i, (name, href) in enumerate(items):
        if i:
            out.append('            <span class="crumbs-sep" aria-hidden="true">›</span>')
        if href is None:
            out.append(f'            <span class="crumbs-current" aria-current="page">{name}</span>')
        elif i == 0:
            out.append(f'            <a class="crumbs-home" href="{href}">{name}</a>')
        else:
            out.append(f'            <a href="{href}">{name}</a>')
    out.append('        </nav>')
    return '\n'.join(out)


def items_from_jsonld(html):
    for block in JSONLD_RE.findall(html):
        try:
            data = json.loads(block)
        except Exception:
            continue
        for node in data.get("@graph", [data]):
            if node.get("@type") == "BreadcrumbList":
                els = sorted(node["itemListElement"], key=lambda e: e.get("position", 0))
                n = len(els)
                items = []
                for j, e in enumerate(els):
                    name = _cap(e["name"])
                    if j == n - 1:
                        items.append((name, None))
                    elif j == 0:
                        items.append((name, "../index.html"))
                    else:
                        items.append((name, "../" + e["item"].rstrip("/").split("/")[-1]))
                return items
    return None


def items_from_title(p, html):
    tm = TITLE_RE.search(html)
    if not tm:
        return None
    segs = [s.strip() for s in tm.group(1).split('|')]
    if len(segs) >= 3:                       # "SUB | LIVRO | Biblioteca"
        return [("Biblioteca", "../index.html"),
                (segs[1], f"../{p.parent.name}.html"),
                (_cap(segs[0]), None)]
    return None


def overview_items(html):
    tm = TITLE_RE.search(html)
    book = tm.group(1).strip() if tm else "Biblioteca"
    book = re.sub(r'^Visão Geral:\s*', '', book.split('|')[0].strip())
    return [("Biblioteca", "index.html"), (book, None)]


def retrofit(p):
    p = Path(p)
    html = p.read_text(encoding="utf-8")
    if 'class="crumbs"' in html:
        print(f"  skip (ja tem): {p.name}"); return
    if NAV_PRINCIPAL_RE.search(html):
        items = items_from_jsonld(html) or items_from_title(p, html)
        if not items:
            print(f"  skip (cap sem dados): {p.name}"); return
        html = NAV_PRINCIPAL_RE.sub(lambda m: crumbs_html(items), html, count=1)
        p.write_text(html, encoding="utf-8")
        print(f"  OK cap: {p.parent.name}/{p.name}"); return
    if NAV_VOLTAR_RE.search(html):
        html = NAV_VOLTAR_RE.sub(lambda m: crumbs_html(overview_items(html)), html, count=1)
        p.write_text(html, encoding="utf-8")
        print(f"  OK ovr: {p.name}"); return
    print(f"  skip (sem nav): {p.name}")


def iter_targets(base):
    base = Path(base)
    for f in base.glob("*.html"):
        yield f
    for sub in base.iterdir():
        if sub.is_dir() and sub.name not in SKIP_DIRS:
            yield from sub.glob("ch*.html")
            yield from sub.glob("capitulo*.html")


if __name__ == "__main__":
    args = sys.argv[1:]
    targets = list(iter_targets(Path(__file__).parent)) if args == ["--all"] else [Path(a) for a in args]
    for t in targets:
        retrofit(t)
