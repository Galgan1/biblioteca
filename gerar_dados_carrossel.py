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


def emit(slug):
    data = importlib.import_module(slug.replace('-', '_') + '_data')
    book = data.BOOK
    total_caps = len(getattr(data, 'CHAPTERS', []) or [])
    chapters, counts = {}, {}
    # carrossel do LIVRO (visão geral) — ch=None (consistente com o build); avisa se faltar
    ov_cards = gc._overview_cards(book, data)
    if ov_cards:
        chapters['overview'] = gc.montar_slides(book, ov_cards, ch=None, total_caps=total_caps)
        counts['overview'] = len(chapters['overview'])
    for ch in getattr(data, 'CHAPTERS', []) or []:
        if not ch.get('cards'):
            print(f"[aviso] {slug}/{ch.get('slug','?')}: capitulo sem cards, pulado")
            continue
        sl = gc.montar_slides(book, ch['cards'], ch=ch, total_caps=total_caps)
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
