# -*- coding: utf-8 -*-
"""OCR de PDFs-imagem (livros escaneados/fotos) via Tesseract — CPU, sem GPU.

Para páginas de livro (texto impresso denso), Tesseract é o motor certo: é OCR de
documento, entende layout/parágrafos e suporta português. easyocr/paddle (GPU) são
para texto de cena e embolam página cheia — por isso a GPU NÃO é necessária aqui.

Uso:  python ocr_pdf.py <entrada.pdf> [saida.txt] [--lang por] [--dpi 300]
Sem saida.txt, imprime no stdout.

Pré-requisitos (já instalados): tesseract.exe (winget UB-Mannheim) + por.traineddata
em ./ocr_data/ (alta acurácia, tessdata_best).
"""
import sys, os
from pathlib import Path
import fitz                      # PyMuPDF — renderiza a página em imagem
from PIL import Image
import pytesseract

TESS = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
TESSDATA = str(Path(__file__).parent / "ocr_data")
pytesseract.pytesseract.tesseract_cmd = TESS
os.environ["TESSDATA_PREFIX"] = TESSDATA   # aponta p/ os .traineddata locais (por/eng/osd)


def is_image_pdf(doc):
    """Heurística: pouco texto extraível + tem imagens => é scan/foto (precisa OCR)."""
    txt = sum(len(p.get_text()) for p in doc)
    imgs = sum(len(p.get_images()) for p in doc)
    return txt < 100 * len(doc) and imgs > 0


def _ocr_chunk(path, page_ini, page_fim, lang, dpi, wid):
    """Um worker: abre o PRÓPRIO handle do PDF (fitz não é thread-safe entre
    threads no mesmo doc) e processa um intervalo contíguo de páginas."""
    doc = fitz.open(path)
    out = []
    for i in range(page_ini, page_fim):
        pix = doc[i].get_pixmap(dpi=dpi)
        img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
        t = pytesseract.image_to_string(img, lang=lang)
        out.append((i, t))
        print(f"  [w{wid}] página {i+1}: {len(t)} chars", file=sys.stderr)
    return out


def ocr_pdf(path, lang="por", dpi=300, workers=1):
    """OCR do PDF inteiro. workers>1 = paralelo: divide as páginas em blocos
    contíguos; cada thread roda seu próprio tesseract.exe (subprocesso →
    paralelismo real, o GIL não atrapalha)."""
    from concurrent.futures import ThreadPoolExecutor
    n = len(fitz.open(path))
    workers = max(1, min(workers, n))
    # blocos contíguos de tamanho ~igual (ex.: 124 págs / 10 workers = 13,13,13,13,12,...)
    base, extra = divmod(n, workers)
    bounds, ini = [], 0
    for w in range(workers):
        fim = ini + base + (1 if w < extra else 0)
        bounds.append((ini, fim)); ini = fim
    print(f"  OCR paralelo: {n} páginas / {workers} workers "
          f"(~{base + (1 if extra else 0)} págs/worker) @ {dpi}dpi", file=sys.stderr)
    resultados = []
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futs = [ex.submit(_ocr_chunk, path, a, b, lang, dpi, w)
                for w, (a, b) in enumerate(bounds)]
        for f in futs:
            resultados.extend(f.result())
    resultados.sort(key=lambda x: x[0])   # reordena pelas páginas
    return "\n".join(t for _, t in resultados)


def extract_any(path, lang="por", dpi=300, workers=1, force_ocr=False):
    """Texto nativo se houver; senão OCR. É o ponto de entrada do workflow."""
    doc = fitz.open(path)
    native = "\n".join(p.get_text() for p in doc)
    if not is_image_pdf(doc) and not force_ocr:
        return native, "texto-nativo"
    return ocr_pdf(path, lang, dpi, workers), "ocr"


if __name__ == "__main__":
    args = sys.argv[1:]
    inp = args[0]
    outp = args[1] if len(args) > 1 and not args[1].startswith("--") else None
    lang = args[args.index("--lang") + 1] if "--lang" in args else "por"
    dpi = int(args[args.index("--dpi") + 1]) if "--dpi" in args else 300
    workers = int(args[args.index("--workers") + 1]) if "--workers" in args else 1
    text, modo = extract_any(inp, lang, dpi, workers, force_ocr="--force-ocr" in args)
    print(f"modo: {modo} · {len(text)} chars", file=sys.stderr)
    if outp:
        Path(outp).write_text(text, encoding="utf-8")
        print(f"OK -> {outp} ({len(text)} chars)")
    else:
        sys.stdout.write(text)
