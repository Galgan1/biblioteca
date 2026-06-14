# -*- coding: utf-8 -*-
"""
metricas.py — a NOTA DE "PATUS" de um PDF (heurística determinística, local).

Não tenta "ver beleza" — mede proxies objetivos que, na prática, separam um PDF
que dá prazer de um que dá desconforto:

  · coverage  — o quanto o conteúdo desce até o pé da página (página cheia × pela
                metade dá sensação de "faltou");
  · density   — densidade de tinta na região com conteúdo (nem deserto, nem
                amontoado ilegível);
  · gap_frac  — buracos vazios NO MEIO do conteúdo (quebra feia entre blocos);
  · edge_ink  — tinta encostando na borda (corte/sangria — sempre ruim);
  · pages     — nº de páginas vs. o esperado (capítulo deve caber no alvo).

A nota é um proxy; quando ela trava abaixo do alvo, o refinador chama a rota de
fuga (Claude) para o julgamento que a métrica não captura. Rasteriza com PyMuPDF.

Uso avulso:  python metricas.py arquivo.pdf [--expect N]
"""
import sys
import fitz  # PyMuPDF


def _clamp(x, lo=0.0, hi=1.0):
    return max(lo, min(hi, x))


def _ink_profile(page, dpi=80, bands=24, thresh=205):
    """Perfil de tinta da página: cobertura por faixa horizontal + anel de borda."""
    zoom = dpi / 72.0
    pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), colorspace=fitz.csGRAY, alpha=False)
    w, h = pix.width, pix.height
    data = pix.samples  # bytes, row-major, 1 canal
    table = bytes(1 if i < thresh else 0 for i in range(256))  # escuro -> 1
    mask = data.translate(table)
    total = w * h or 1

    band_h = max(1, h // bands)
    prof = []
    for b in range(bands):
        y0 = b * band_h
        y1 = h if b == bands - 1 else (b + 1) * band_h
        seg = mask[y0 * w:y1 * w]
        prof.append(seg.count(1) / max(1, len(seg)))

    # anel de borda (~3% de cada lado): tinta aqui = conteúdo encostando na margem
    m = max(2, int(min(w, h) * 0.03))
    ring = mask[0:m * w].count(1) + mask[(h - m) * w:h * w].count(1)
    ringpx = 2 * m * w
    for y in range(m, h - m):
        row = mask[y * w:(y + 1) * w]
        ring += row[:m].count(1) + row[-m:].count(1)
        ringpx += 2 * m

    return {"w": w, "h": h, "ink": mask.count(1) / total, "prof": prof,
            "edge": ring / max(1, ringpx)}


def _page_shape(p, eps=0.004):
    """Reduz o perfil a (cobertura, densidade, buraco_interno)."""
    prof = p["prof"]
    bands = len(prof)
    covered = [i for i, v in enumerate(prof) if v > eps]
    last = covered[-1] if covered else 0
    coverage = (last + 1) / bands
    cov_vals = prof[:last + 1] or [0.0]
    density = sum(cov_vals) / len(cov_vals)
    holes = sum(1 for v in cov_vals if v <= eps)
    gap_frac = holes / max(1, len(cov_vals))
    return coverage, density, gap_frac


def score_pdf(pdf_bytes, expect_pages=1, dpi=80):
    """Devolve dict com 'patus' (0..1) e os componentes/medidas crus."""
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    n = doc.page_count
    if n == 0:
        return {"patus": 0.0, "pages": 0, "erro": "pdf vazio"}

    first = _ink_profile(doc[0], dpi=dpi)
    cov, dens, gap = _page_shape(first)

    coverage_s = _clamp(cov / 0.92)
    edge_s = 1.0 if first["edge"] < 0.02 else _clamp(1 - (first["edge"] - 0.02) / 0.10)
    lo, hi = 0.05, 0.16  # faixa de densidade confortável p/ texto
    if dens < lo:
        comfort_s = _clamp(dens / lo)
    elif dens > hi:
        comfort_s = _clamp(1 - (dens - hi) / 0.12)
    else:
        comfort_s = 1.0
    gap_s = _clamp(1 - gap / 0.18)
    pages_s = 1.0 if n == expect_pages else (0.25 if n > expect_pages else 0.6)

    if n > 1:
        lcov, _, _ = _page_shape(_ink_profile(doc[n - 1], dpi=dpi))
        lastfill_s = _clamp(lcov / 0.5)  # última página ao menos meio cheia
    else:
        lastfill_s = 1.0

    patus = (0.42 * coverage_s + 0.15 * edge_s + 0.18 * comfort_s
             + 0.10 * gap_s + 0.10 * pages_s + 0.05 * lastfill_s)

    return {
        "patus": round(patus, 3),
        "pages": n,
        "coverage": round(cov, 3),
        "density": round(dens, 4),
        "gap_frac": round(gap, 3),
        "edge_ink": round(first["edge"], 4),
        "sub": {
            "coverage": round(coverage_s, 3), "edge": round(edge_s, 3),
            "comfort": round(comfort_s, 3), "gap": round(gap_s, 3),
            "pages": round(pages_s, 3), "lastfill": round(lastfill_s, 3),
        },
    }


def compact(sc):
    return (f"patus={sc['patus']} cov={sc.get('coverage')} dens={sc.get('density')} "
            f"edge={sc.get('edge_ink')} gap={sc.get('gap_frac')} pg={sc['pages']}")


if __name__ == "__main__":
    args = sys.argv[1:]
    expect = 1
    if "--expect" in args:
        i = args.index("--expect")
        expect = int(args[i + 1]); del args[i:i + 2]
    if not args:
        print("uso: python metricas.py arquivo.pdf [--expect N]"); sys.exit(2)
    with open(args[0], "rb") as f:
        print(compact(score_pdf(f.read(), expect_pages=expect)))
