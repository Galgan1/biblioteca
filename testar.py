#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ponto único de teste do projeto (Akita pilar 2: verde = exit code).

Agrega as DUAS baterias unittest do repo, cada uma em seu próprio processo
(isolamento — Akita pilar 8), e devolve UM exit code:
  - tests/         (raiz)
  - videos/tests/  (pipeline de vídeo)

Uso:
  python testar.py            # resumo legível; exit 0 sse tudo verde, !=0 senão
  python testar.py --json     # {"passed","failed","total","ok"} parseável

Idempotente: sem rede, sem credencial, sem seed manual. Mesmo comando que a CI roda.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

# (nome, cwd, start_dir-de-teste) — comando canônico: unittest discover -s tests -t .
SUITES = [
    ("raiz", ROOT, ROOT / "tests"),
    ("videos", ROOT / "videos", ROOT / "videos" / "tests"),
]


def _rodar(cwd):
    """Roda a bateria de uma pasta como subprocesso. Devolve (ran, falhas, ok, saida)."""
    p = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-t", "."],
        cwd=str(cwd), capture_output=True, text=True,
    )
    saida = p.stderr + p.stdout
    ran = int(m.group(1)) if (m := re.search(r"Ran (\d+) test", saida)) else 0
    falhas = sum(int(x) for x in re.findall(r"(?:failures|errors)=(\d+)", saida))
    return ran, falhas, p.returncode == 0, saida


def main(argv):
    as_json = "--json" in argv
    total = passed = failed = 0
    linhas = []
    for nome, cwd, start in SUITES:
        if not start.exists():
            linhas.append((nome, 0, 0, None))
            continue
        ran, falhas, ok, saida = _rodar(cwd)
        total += ran
        failed += falhas
        passed += ran - falhas
        linhas.append((nome, ran, falhas, ok))
        # Gate diagnosticável (Akita pilar 5): se a bateria falhou, mostra QUAL
        # teste — senão a CI só diz "VERMELHO" sem dizer o quê, e fica opaca.
        if not as_json and (falhas or not ok):
            print(f"\n----- saída da bateria '{nome}' (falhou) -----")
            print(saida.rstrip())
            print("-" * 48)

    ok_geral = failed == 0 and all(l[3] is not False for l in linhas)

    if as_json:
        print(json.dumps({"passed": passed, "failed": failed, "total": total, "ok": ok_geral}))
    else:
        for nome, ran, falhas, ok in linhas:
            estado = "pulado" if ok is None else ("OK" if falhas == 0 and ok else f"FALHOU ({falhas})")
            print(f"  {nome:<8} {ran:>4} testes  {estado}")
        print(f"  {'TOTAL':<8} {total:>4} testes  " + ("VERDE" if ok_geral else f"VERMELHO ({failed})"))
    return 0 if ok_geral else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
