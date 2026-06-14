# -*- coding: utf-8 -*-
"""Conta cards por capítulo em cada <slug>_data.py e lista os capítulos magros."""

import importlib, glob, os, sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

rows = []
for f in sorted(glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), "*_data.py"))):
    mod = os.path.basename(f)[:-3]
    try:
        m = importlib.import_module(mod)
    except Exception as e:
        print("ERRO importando", mod, "->", e)
        continue
    for c in getattr(m, "CHAPTERS", []):
        rows.append(
            (len(c.get("cards", [])), mod, c.get("slug", "?"), 1 if c.get("lessons") else 0)
        )

rows.sort()
print("=== capítulos MAGROS (<=4 cards de conteúdo) ===")
for n, mod, slug, les in rows:
    if n <= 4:
        print(f"  {n} cards {'+liç' if les else '    '}  {mod:32s} {slug}")
cnt = Counter(n for n, _, _, _ in rows)
print("\ndistribuição cards/capítulo:", dict(sorted(cnt.items())))
print(
    f"total capítulos: {len(rows)} | magros(<=4): {sum(1 for n, _, _, _ in rows if n <= 4)} | (<=3): {sum(1 for n, _, _, _ in rows if n <= 3)}"
)
