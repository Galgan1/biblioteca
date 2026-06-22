#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Backup/restore dos segredos FORA do alcance do git (Akita pilar 8 — recuperação).

POR QUÊ: os segredos vivos (`videos/.secrets/`, `pdf-service/secret.key`) são
gitignored (não vazam), mas um `git clean -fdx` apaga untracked — já apagou
`_akita_pesquisa`/`settings.local.json` antes. Perder esses tokens = re-auth de
FB/IG/TikTok/YouTube (e re-auth do YouTube já caiu no canal errado uma vez).
Este script guarda uma cópia FORA do repo (git clean não alcança) e restaura o
que faltar. NUNCA imprime conteúdo de segredo.

Uso:
  python restaurar_segredos.py --backup   # tree -> backup externo (RODE após cada (re)auth)
  python restaurar_segredos.py            # backup -> tree, SÓ o que estiver faltando (idempotente)
"""
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BACKUP = Path.home() / ".minutoreal_secrets_backup"   # fora do repo = fora do git clean
ALVOS = [
    (ROOT / "videos" / ".secrets", BACKUP / "videos_secrets"),
    (ROOT / "pdf-service" / "secret.key", BACKUP / "pdf-service" / "secret.key"),
]


def _copia(src: Path, dst: Path) -> None:
    if src.is_dir():
        shutil.copytree(src, dst, dirs_exist_ok=True)
    else:
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)


def main() -> int:
    backup = "--backup" in sys.argv
    feitos = []
    for tree, ext in ALVOS:
        src, dst = (tree, ext) if backup else (ext, tree)
        if not src.exists():
            continue
        if not backup and dst.exists():
            continue  # restore não sobrescreve o que já está no tree (idempotente)
        _copia(src, dst)
        feitos.append(dst.name)
    acao = "backup" if backup else "restore"
    print(f"{acao}: {len(feitos)} alvo(s) -> {feitos or '(nada a fazer)'}. Local do backup: {BACKUP}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
