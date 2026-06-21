#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PostToolUse hook: roda audita_fantasmas.py ao editar um .py.

Akita pilar 7 — pega o "fantasma" (import de módulo de raiz NÃO-versionado) no
instante em que é introduzido, não só na CI. O edit já aconteceu (PostToolUse),
então é SURFACE-only: exit 2 mostra a saída ao Claude como aviso para corrigir.

Fail-open: só age quando o audita acusa fantasma (returncode 1); qualquer outro
caso (arquivo não-.py, audita ausente, crash) → exit 0.
"""
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    try:
        fp = json.load(sys.stdin).get("tool_input", {}).get("file_path", "")
    except Exception:
        return 0
    if not fp.endswith(".py"):
        return 0
    audita = os.path.join(ROOT, "audita_fantasmas.py")
    if not os.path.exists(audita):
        return 0
    r = subprocess.run([sys.executable, audita], cwd=ROOT,
                       capture_output=True, text=True)
    if r.returncode == 1:  # fantasma encontrado
        sys.stderr.write(
            f"audita_fantasmas: import-closure quebrado após editar "
            f"{os.path.basename(fp)} (módulo de raiz não-versionado):\n{r.stdout}\n")
        return 2  # surface ao Claude
    return 0


if __name__ == "__main__":
    sys.exit(main())
