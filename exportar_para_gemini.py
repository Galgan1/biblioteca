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


def _book_body(slug):
    """Ficha + esqueleto JSON de UM livro (sem a skill na frente)."""
    d = importlib.import_module(slug.replace('-', '_') + '_data')
    book = getattr(d, 'BOOK', None) or _BOOKS_JSON.get(slug, {})
    ficha = [
        f"### LIVRO `{slug}` — {book.get('title','?')} ({book.get('author','?')})",
        "",
        f"**Subtítulo:** {book.get('subtitle','—')}",
        f"**Ideia central:** {book.get('intro') or book.get('description','—')}",
        "",
        "Capítulos (mantenha estes slugs e títulos):",
    ]
    skel = {}
    for ch in d.CHAPTERS:
        ficha.append(f"- `{ch['slug']}` — {ch.get('sub','')}")
        skel[ch['slug']] = {"cards": [
            {k: c[k] for k in ('ic', 't', 'b', 'tip') if k in c} for c in ch['cards']
        ]}
    body = "\n".join(ficha) + "\n\nEsqueleto (aprofunde os corpos):\n\n```json\n"
    body += json.dumps(skel, ensure_ascii=False, indent=1) + "\n```\n"
    return body


def skeleton(slug):
    return SKILL + "\n\n---\n\n# LIVRO PARA APROFUNDAR\n\n" + _book_body(slug)


PROTOCOLO = """

---

# PROTOCOLO DO TRABALHO MASSIVO (leia antes de começar)

Abaixo estão **TODOS os livros** a aprofundar, cada um com sua ficha e esqueleto.
Processe **na ordem em que aparecem**. Para cada livro, produza um bloco ```json no
FORMATO DE SAÍDA da skill — um objeto chaveado pelos slugs dos capítulos daquele livro:

```json
{ "<cap-slug>": {"cards":[ {card}, ... ]}, ... }
```

Regras do lote:
- **Um bloco ```json por livro**, precedido por uma linha `=== <slug> ===` (ex.: `=== sapiens ===`),
  para eu salvar cada um como `_kit_preview/text/<slug>.json`.
- Gere quantos livros couberem na sua resposta. Ao se aproximar do limite de saída,
  **pare no fim de um livro** (nunca corte um livro no meio) e escreva apenas `CONTINUAR`.
  Eu responderei `continuar` e você segue do próximo livro.
- Mantenha os mesmos slugs de capítulo e a mesma contagem de cards do esqueleto.
- Vale tudo da RÉGUA acima (corpo ~260–340 caracteres, uma `<strong>`, `emph` literal,
  `tip` rotulado, ~1 `warn` por capítulo, aspas curvas, pt-BR, tom de autor).

# OS LIVROS

"""


def consolidado(slugs):
    """Escreve UM prompt completo: skill + protocolo de lote + esqueletos de todos
    os livros. O usuário cola isso de uma vez no Gemini."""
    parts = [SKILL, PROTOCOLO]
    ok = err = 0
    for slug in slugs:
        try:
            parts.append(_book_body(slug) + "\n")
            ok += 1
        except Exception as e:
            print(f'FAIL {slug}: {e}'); err += 1
    out = BASE / '_kit_preview' / 'PROMPT-GEMINI-COMPLETO.md'
    out.write_text("\n".join(parts), encoding='utf-8', newline='\n')
    kb = out.stat().st_size // 1024
    print(f'prompt completo: {ok} livros, {kb} KB → {out} ({err} falhas)')


def _pending():
    all_slugs = sorted(os.path.basename(f)[:-8].replace('_', '-') for f in glob.glob(str(BASE / '*_data.py')))
    return [s for s in all_slugs if s not in DONE]


def main():
    args = [a for a in sys.argv[1:]]
    if args and args[0] == '--consolidado':
        consolidado(args[1:] or _pending())
        return
    OUT.mkdir(parents=True, exist_ok=True)
    slugs = args or _pending()
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
