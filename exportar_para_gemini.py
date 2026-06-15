# -*- coding: utf-8 -*-
"""Gera os pacotes de entrada para delegar o aprofundamento de textos ao Gemini.

Para cada livro PENDENTE (com <slug>_data.py e ainda sem texto profundo), escreve
um arquivo autocontido em _kit_preview/gemini_in/<slug>.md =
  [a skill SKILL-TEXTOS-GEMINI.md]  +  [a ficha do livro]  +  [o esqueleto dos cards].

Fluxo: abra um <slug>.md, cole no Gemini, salve a resposta JSON como
_kit_preview/text/<slug>.json e rode `python aplicar_texto.py <slug>`.

Uso: python exportar_para_gemini.py            (todos os pendentes)
     python exportar_para_gemini.py <slug> ...  (livros específicos)
"""
import importlib, json, sys, glob, os
from pathlib import Path

BASE = Path(__file__).parent
SKILL = (BASE / '_kit_preview' / 'SKILL-TEXTOS-GEMINI.md').read_text(encoding='utf-8')
OUT = BASE / '_kit_preview' / 'gemini_in'

# Livros que já têm texto profundo aplicado (piloto + ondas 1 e 2) — pular.
DONE = {
    "leis-da-natureza-humana", "48-leis-do-poder", "aristoteles-poetica",
    "armas-da-persuasao", "como-fazer-amigos", "comunicacao-nao-violenta",
    "coragem-de-nao-agradar", "essencialismo", "marketing-4-0",
    "poder-de-delegar", "psicologia-financeira", "rapido-e-devagar", "sutil-arte",
}


_BOOKS_JSON = {b['id']: b for b in json.load(open(BASE / 'books.json', encoding='utf-8'))}


def skeleton(slug):
    d = importlib.import_module(slug.replace('-', '_') + '_data')
    book = getattr(d, 'BOOK', None) or _BOOKS_JSON.get(slug, {})
    ficha = [
        f"# LIVRO PARA APROFUNDAR: {book.get('title','?')} — {book.get('author','?')}",
        "",
        f"**Subtítulo:** {book.get('subtitle','—')}",
        f"**Ideia central:** {book.get('intro') or book.get('description','—')}",
        "",
        "## Capítulos (contexto — mantenha estes slugs e títulos)",
    ]
    skel = {}
    for ch in d.CHAPTERS:
        ficha.append(f"- `{ch['slug']}` — {ch.get('sub','')}")
        skel[ch['slug']] = {"cards": [
            {k: c[k] for k in ('ic', 't', 'b', 'tip') if k in c} for c in ch['cards']
        ]}
    body = "\n".join(ficha) + "\n\n## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)\n\n```json\n"
    body += json.dumps(skel, ensure_ascii=False, indent=1) + "\n```\n"
    return SKILL + "\n\n---\n\n" + body


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    args = [a for a in sys.argv[1:]]
    if args:
        slugs = args
    else:
        all_slugs = sorted(os.path.basename(f)[:-8].replace('_', '-') for f in glob.glob(str(BASE / '*_data.py')))
        slugs = [s for s in all_slugs if s not in DONE]
    ok = err = 0
    for slug in slugs:
        try:
            (OUT / f'{slug}.md').write_text(skeleton(slug), encoding='utf-8', newline='\n')
            ok += 1
        except Exception as e:
            print(f'FAIL {slug}: {e}'); err += 1
    print(f'{ok} pacotes em _kit_preview/gemini_in/ ({err} falhas)')


if __name__ == '__main__':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    main()
