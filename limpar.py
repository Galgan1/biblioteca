"""limpar.py — Higiene do projeto: purga artefatos REGENERÁVEIS.

Apaga: caches Python (__pycache__/*.pyc), logs (*.log), sondas (_probe_*) e
o QA visual de PDF (_pdfcheck/, recriável por render_pdf.py).

NUNCA toca em fonte ou dados: .secrets/, ocr_data/ (modelo Tesseract),
pdfs/, downloads/ (material-fonte), *_data.py, assets/, _fonts/, node_modules/, .git/.

Uso:
  python limpar.py            # limpa
  python limpar.py --dry-run  # só mostra o que apagaria
"""

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DRY = '--dry-run' in sys.argv or '-n' in sys.argv

# diretórios que a varredura nem entra (fonte, dados, deps, segredos)
PODA = {
    '.git',
    '.secrets',
    'node_modules',
    'ocr_data',
    'pdfs',
    'downloads',
    'assets',
    '_fonts',
    'book-to-skill',
}


def categoria(caminho, partes):
    """Retorna a categoria do artefato (ou None se for para preservar)."""
    nome = caminho.name
    if caminho.suffix == '.pyc' or '__pycache__' in partes:
        return 'cache'
    if caminho.suffix == '.log':
        return 'log'
    if nome.startswith('_probe_'):
        return 'probe'
    if partes and partes[0] == '_pdfcheck':
        return 'pdfcheck'
    return None


def main():
    stats = {}  # categoria -> [n_arquivos, bytes]
    travados = []
    vazios = set()  # dirs candidatos a remover se ficarem vazios

    for dp, dn, fn in os.walk(ROOT):
        dn[:] = [d for d in dn if d not in PODA]  # poda in-place
        for f in fn:
            p = Path(dp) / f
            partes = p.relative_to(ROOT).parts
            cat = categoria(p, partes)
            if not cat:
                continue
            try:
                tam = p.stat().st_size
            except OSError:
                continue
            s = stats.setdefault(cat, [0, 0])
            s[0] += 1
            s[1] += tam
            if cat in ('cache', 'pdfcheck'):
                vazios.add(Path(dp))
            if not DRY:
                try:
                    os.remove(p)
                except OSError:
                    travados.append(str(p.relative_to(ROOT)))

    # remove diretórios que esvaziaram (__pycache__, _pdfcheck e subpastas)
    if not DRY:
        for d in sorted(vazios, key=lambda x: len(str(x)), reverse=True):
            try:
                d.rmdir()
            except OSError:
                pass
        # tenta remover _pdfcheck raiz se sobrou vazio
        try:
            (ROOT / '_pdfcheck').rmdir()
        except OSError:
            pass

    rotulo = 'SIMULAÇÃO (nada apagado)' if DRY else 'LIMPEZA CONCLUÍDA'
    print(f'== {rotulo} ==')
    total_n = total_b = 0
    for cat in ('cache', 'log', 'probe', 'pdfcheck'):
        n, b = stats.get(cat, (0, 0))
        total_n += n
        total_b += b
        print(f'  {cat:9} {n:5} arquivos  {b / 1024:10,.0f} KB')
    print(f'  {"TOTAL":9} {total_n:5} arquivos  {total_b / 1024 / 1024:10,.1f} MB')
    if travados:
        print(f'  travados (em uso): {len(travados)}')


if __name__ == '__main__':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass
    main()
