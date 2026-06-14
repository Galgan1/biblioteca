# -*- coding: utf-8 -*-
"""Rasteriza PDFs em PNG (1 por página) para inspeção visual. Uso:
python render_pdf.py <arquivo.pdf> [mais.pdf ...]   -> _pdfcheck/<nome>-pNN.png
"""

import os, sys, fitz

OUT = "_pdfcheck"
os.makedirs(OUT, exist_ok=True)
for pdf in sys.argv[1:]:
    doc = fitz.open(pdf)
    name = os.path.splitext(os.path.basename(pdf))[0]
    for i in range(doc.page_count):
        doc[i].get_pixmap(dpi=100).save(os.path.join(OUT, f"{name}-p{i + 1:02d}.png"))
    print(f"{name}: {doc.page_count} páginas")
