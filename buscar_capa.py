# -*- coding: utf-8 -*-
"""Baixa a CAPA ORIGINAL de um livro (arte real publicada) para assets/<slug>-cover.png.
Padrão da biblioteca: toda capa é a original — a tipográfica de `gerar_capa.py` é só
último recurso para itens que NÃO são livros publicados (ex.: provimento jurídico).

Fonte: Open Library (stdlib, sem API key).
  - por ISBN:   https://covers.openlibrary.org/b/isbn/<isbn>-L.jpg
  - por busca:  search.json (title+author) -> cover_i -> /b/id/<id>-L.jpg
Rejeita o "blank" do Open Library (~2,7 KB). Verifique sempre o resultado na estante.

Uso:
  python buscar_capa.py <slug> "Título" "Autor" [ISBN]
"""

import io
import os
import sys
import urllib.parse
import urllib.request

from PIL import Image

BASE = os.path.dirname(os.path.abspath(__file__))
UA = {"User-Agent": "biblioteca-cover/1.0 (andregalgani.com.br)"}
MIN_BYTES = 4000  # abaixo disso é o placeholder em branco do Open Library


def _get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def cover_ids(title, author):
    q = urllib.parse.urlencode({"title": title, "author": author, "limit": 8, "fields": "cover_i"})
    import json

    data = json.loads(_get("https://openlibrary.org/search.json?" + q))
    seen, ids = set(), []
    for d in data.get("docs", []):
        c = d.get("cover_i")
        if c and c not in seen:
            seen.add(c)
            ids.append(c)
    return ids


def try_save(data, slug):
    if not data or len(data) < MIN_BYTES:
        return False
    im = Image.open(io.BytesIO(data)).convert("RGB")
    if im.height > 900:
        im = im.resize((round(im.width * 900 / im.height), 900), Image.LANCZOS)
    out = os.path.join(BASE, "assets", f"{slug}-cover.png")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    im.save(out, "PNG")
    print(f"OK capa original -> assets/{slug}-cover.png ({im.width}x{im.height})")
    return True


def fetch(slug, title, author, isbn=None):
    if isbn:
        try:
            if try_save(
                _get(f"https://covers.openlibrary.org/b/isbn/{isbn}-L.jpg?default=false"), slug
            ):
                return True
        except Exception:
            pass
    try:
        for cid in cover_ids(title, author):
            try:
                if try_save(_get(f"https://covers.openlibrary.org/b/id/{cid}-L.jpg"), slug):
                    return True
            except Exception:
                continue
    except Exception as e:
        print(f"AVISO: busca falhou ({e})")
    print(
        f"AVISO: nenhuma capa original encontrada p/ '{title}' / '{author}'. "
        f"Forneça manualmente (Google Books/editora) ou use gerar_capa.py só se NÃO for livro publicado."
    )
    return False


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print('uso: python buscar_capa.py <slug> "Título" "Autor" [ISBN]')
        sys.exit(2)
    ok = fetch(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4] if len(sys.argv) > 4 else None)
    sys.exit(0 if ok else 1)
