# -*- coding: utf-8 -*-
"""Emite os DADOS do carrossel por capítulo para o serviço Node gerar sob demanda.

Usa os MESMOS construtores do gerar_carrossel.py (zero deriva visual). Não renderiza
imagem aqui — só emite o HTML dos slides + o CSS, como texto estático:

  assets/kit/_carousel.css            CSS compartilhado (verbatim gerar_carrossel.CSS)
  assets/kit/<slug>/slides.json       {chapters: {<cap>: ["<div class=slide>...", x5]}}  (servidor lê)
  assets/kit/<slug>/caps.json         {chapters: {<cap>: <n_slides>}}                     (UI lê — leve)

O Node (server.js) monta a página com este CSS + os slides do capítulo, tira screenshot
(png + webp), cacheia e serve. Uso: python gerar_dados_carrossel.py [slug|--all]
"""
import importlib, json, sys, os
from pathlib import Path
import gerar_carrossel as gc

BASE = Path(__file__).parent
KIT = BASE / 'assets' / 'kit'


def _chapter_slides(book, ch):
    cards = ch['cards']
    n = len(cards)
    total = n + 2  # capa + conceitos + cta
    slides = [gc._cover(book, n, 1, total)]
    slides += [gc._concept(c, i, n, i + 1, total, book, ch) for i, c in enumerate(cards, 1)]
    slides.append(gc._cta(book, total, total))
    return slides


def emit(slug):
    data = importlib.import_module(slug.replace('-', '_') + '_data')
    book = data.BOOK
    chapters, counts = {}, {}
    # carrossel do LIVRO (visão geral) — usa overview_cards (cap "overview", sem underscore p/ passar no SLUG_RE)
    ov_cards = book.get('overview_cards') or (data.CHAPTERS[0]['cards'] if data.CHAPTERS else [])
    if ov_cards:
        ov = {'slug': 'overview', 'sub': '', 'cards': ov_cards}
        chapters['overview'] = _chapter_slides(book, ov)
        counts['overview'] = len(chapters['overview'])
    for ch in data.CHAPTERS:
        sl = _chapter_slides(book, ch)
        chapters[ch['slug']] = sl
        counts[ch['slug']] = len(sl)
    out = KIT / slug
    out.mkdir(parents=True, exist_ok=True)
    (out / 'slides.json').write_text(json.dumps({'chapters': chapters}, ensure_ascii=False), encoding='utf-8', newline='\n')
    (out / 'caps.json').write_text(json.dumps({'chapters': counts}, ensure_ascii=False), encoding='utf-8', newline='\n')
    return len(chapters)


def main():
    KIT.mkdir(parents=True, exist_ok=True)
    (KIT / '_carousel.css').write_text(gc.CSS, encoding='utf-8', newline='\n')
    args = sys.argv[1:]
    if args and args[0] != '--all':
        slugs = [args[0]]
    else:
        books = json.load(open(BASE / 'books.json', encoding='utf-8'))
        slugs = [b['id'] for b in books if os.path.exists(BASE / (b['id'].replace('-', '_') + '_data.py'))]
    ok = err = 0
    for slug in slugs:
        try:
            ncap = emit(slug)
            ok += 1
        except Exception as e:
            print(f'FAIL {slug}: {e}')
            err += 1
    print(f'CSS + {ok} livros emitidos ({err} falhas) em assets/kit/')


if __name__ == '__main__':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    main()
