# -*- coding: utf-8 -*-
"""Integra o texto profundo gerado pelos agentes no <slug>_data.py do livro.

Lê _kit_preview/text/<slug>/<cap>.json (cada um {"cards":[...]}) e substitui, no
arquivo de dados do livro, o array "cards" de cada capítulo correspondente. Valida
o import no fim. Reutilizável por onda. Uso: python aplicar_texto.py <slug> [<slug2> ...]
"""
import json, re, sys, importlib
from pathlib import Path

BASE = Path(__file__).parent
sys.stdout.reconfigure(encoding='utf-8')


def card_lit(c):
    p = [f'"ic":{json.dumps(c["ic"], ensure_ascii=False)}', f'"t":{json.dumps(c["t"], ensure_ascii=False)}']
    if c.get('emph'):
        p.append(f'"emph":{json.dumps(c["emph"], ensure_ascii=False)}')
    p.append(f'"b":{json.dumps(c["b"], ensure_ascii=False)}')
    if c.get('tip'):
        p.append(f'"tip":{json.dumps(c["tip"], ensure_ascii=False)}')
    if c.get('warn'):
        p.append('"warn":True')
    if c.get('wide'):
        p.append('"wide":True')
    return '{' + ','.join(p) + '}'


def apply_book(slug):
    tdir = BASE / '_kit_preview' / 'text' / slug
    if not tdir.is_dir():
        print(f'{slug}: SEM pasta de texto ({tdir})'); return False
    src_path = BASE / (slug.replace('-', '_') + '_data.py')
    src = src_path.read_text(encoding='utf-8')
    patched = missed = 0
    for jf in sorted(tdir.glob('*.json')):
        cap = jf.stem
        cards = json.loads(jf.read_text(encoding='utf-8')).get('cards', [])
        if not cards:
            continue
        middle = '\n      ' + ',\n      '.join(card_lit(c) for c in cards) + ',\n    '
        # fecha o array de cards no "lessons_title"/"lessons" do mesmo capítulo
        pat = re.compile(r'("slug":\s*"' + re.escape(cap) + r'".*?"cards":\s*\[).*?(\]\s*,\s*\n\s*"lessons)', re.DOTALL)
        new, n = pat.subn(lambda m: m.group(1) + middle + m.group(2), src, count=1)
        if n == 1:
            src = new; patched += 1
        else:
            print(f'  [!] {slug}/{cap}: não casou'); missed += 1
    src_path.write_text(src, encoding='utf-8', newline='\n')
    # valida
    importlib.invalidate_caches()
    mod = slug.replace('-', '_') + '_data'
    if mod in sys.modules:
        importlib.reload(sys.modules[mod])
    else:
        importlib.import_module(mod)
    print(f'{slug}: {patched} capítulos integrados' + (f' | {missed} falharam' if missed else '') + ' | import OK')
    return missed == 0


if __name__ == '__main__':
    slugs = sys.argv[1:]
    if not slugs:
        sys.exit('uso: python aplicar_texto.py <slug> [<slug2> ...]')
    ok = sum(1 for s in slugs if apply_book(s))
    print(f'\n{ok}/{len(slugs)} livros integrados sem falhas')
