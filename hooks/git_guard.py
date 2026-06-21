#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PreToolUse hook: bloqueia git commit/push/PR fora do GitGuy (contrato nº1).

Akita pilar 7 — enforcement por MÁQUINA, não por confiança. O contrato "só o
GitGuy commita/pusha/cria PR" deixa de depender de boa vontade da lane.

Bypass do GitGuy: prefixe o comando com `GITGUY=1` (ex.: `GITGUY=1 git commit ...`).
A marca viaja no PRÓPRIO comando (que o hook recebe via stdin) — não depende de env
herdada, que seria global ao projeto e furaria o contrato.

Fail-open: qualquer erro (stdin inválido etc.) → libera. Um hook NUNCA trava o Bash.
"""
import json
import re
import sys

ALVO = re.compile(r"\bgit\s+commit\b|\bgit\s+push\b|\bgh\s+pr\s+create\b")


def main():
    try:
        cmd = json.load(sys.stdin).get("tool_input", {}).get("command", "")
    except Exception:
        return 0  # stdin inválido → fail-open (não trava a tool)
    if ALVO.search(cmd) and "GITGUY=1" not in cmd:
        print(json.dumps({"hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": (
                "Contrato nº1 (constituição): só o GitGuy commita/pusha/cria PR. "
                "Se você É o GitGuy, prefixe o comando com `GITGUY=1`."),
        }}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
