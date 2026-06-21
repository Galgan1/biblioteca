#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Guarda contra arquivos-fonte FANTASMA (Akita pilar 7: auditoria automatica).

POR QUE existe (20/jun/2026, revisao Akita do git): `gerar_carrossel.py` estava
RASTREADO mas importava `_carousel_css/_carousel_slides/_carousel_stories` que
NUNCA foram commitados -> o repo quebrava em clone limpo com ImportError, embora
"passasse local" (os arquivos existiam no disco do dev). A CI fantasma nao pegava.

Este guarda detecta o padrao: um `.py` RASTREADO que importa um modulo LOCAL de
raiz (`<mod>.py` existe no disco) que NAO esta rastreado pelo git. Exit 1 se achar
-> a CI bloqueia o merge. Determinista, sem rede, so stdlib + git (Akita pilar 2).

Escopo v1: modulos de RAIZ (onde o bug ocorreu). Subpacotes (videos/) tem
resolucao propria via sys.path e ficam fora para nao gerar falso-positivo.

Uso: python audita_fantasmas.py     # exit 0 = limpo, 1 = ha fantasma (lista)
"""
import ast
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def _imports_locais(fonte: str) -> set[str]:
    """Nomes de modulo top-level importados por um fonte Python (via ast)."""
    nomes: set[str] = set()
    for node in ast.walk(ast.parse(fonte)):
        if isinstance(node, ast.Import):
            nomes.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.level == 0 and node.module:
            nomes.add(node.module.split(".")[0])
    return nomes


def detectar(rastreados: set[str], root: Path) -> list[tuple[str, str]]:
    """Pares (arquivo, modulo) onde um .py rastreado importa modulo de raiz orfao.

    `rastreados` = caminhos relativos dos arquivos versionados (saida de ls-files).
    Orfao = `<modulo>.py` existe no disco da raiz, mas nao esta em `rastreados`.
    """
    mods_raiz_ok = {f[:-3] for f in rastreados if "/" not in f and f.endswith(".py")}
    achados: list[tuple[str, str]] = []
    for arquivo in sorted(f for f in rastreados if f.endswith(".py")):
        caminho = root / arquivo
        if not caminho.is_file():
            continue
        try:
            imps = _imports_locais(caminho.read_text(encoding="utf-8"))
        except (SyntaxError, UnicodeDecodeError):
            continue
        for mod in sorted(imps):
            if (root / f"{mod}.py").is_file() and mod not in mods_raiz_ok:
                achados.append((arquivo, mod))
    return achados


def _rastreados_git(root: Path) -> set[str]:
    """Conjunto de .py rastreados pelo git (caminhos relativos a raiz)."""
    saida = subprocess.run(
        ["git", "ls-files", "*.py"], cwd=str(root), capture_output=True, text=True
    ).stdout
    return set(saida.split())


def main() -> int:
    achados = detectar(_rastreados_git(ROOT), ROOT)
    if not achados:
        print("audita_fantasmas: OK - nenhum fonte rastreado importa modulo orfao.")
        return 0
    print("audita_fantasmas: FANTASMA - fonte rastreada importa modulo NAO versionado:")
    for arquivo, mod in achados:
        print(f"  {arquivo}  ->  import {mod}  (mas {mod}.py nao esta no git)")
    print("Corrija: `git add <modulo>.py` (ou remova o import). Pilar: nada fantasma no git.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
