# -*- coding: utf-8 -*-
"""Revisao de texto: converte markdown cru remanescente (<p> - item</p>,
<p>&bull; item</p>, <p>* item</p>) em listas HTML reais, agrupando runs
consecutivos. Aplica a todos os livros."""
import re
from pathlib import Path

BASE = Path(__file__).parent
BOOK_DIRS = ['keller-casamento', 'maquiavel-pedagogo', 'arte-da-guerra']

# <p> que comeca com marcador de lista (-, *, bullet) — sub-item cru
ITEM_RE = re.compile(r'^(\s*)<p>\s*(?:-|\*|&bull;|•)\s+(.*?)</p>\s*$')


def convert(text):
    lines = text.split('\n')
    out = []
    i = 0
    converted = 0
    while i < len(lines):
        m = ITEM_RE.match(lines[i])
        if m:
            indent = m.group(1)
            items = []
            while i < len(lines):
                mm = ITEM_RE.match(lines[i])
                if not mm:
                    break
                items.append(mm.group(2).strip())
                i += 1
            out.append(f'{indent}<ul class="content-list">')
            for it in items:
                out.append(f'{indent}    <li>{it}</li>')
            out.append(f'{indent}</ul>')
            converted += len(items)
            continue
        out.append(lines[i])
        i += 1
    return '\n'.join(out), converted


total = 0
for d in BOOK_DIRS:
    for f in sorted((BASE / d).glob('*.html')):
        text = f.read_text(encoding='utf-8')
        new, n = convert(text)
        if n:
            f.write_text(new, encoding='utf-8')
            total += n
            print(f'{d}/{f.name}: {n} itens -> lista')
print(f'TOTAL: {total} itens convertidos')
