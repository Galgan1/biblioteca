# -*- coding: utf-8 -*-
"""heartbeat.py — vivacidade do PC local p/ a VPS (T7 do plano 1-clique).

PORQUE: o premium (3DGS) só renderiza no PC local (Windows); a VPS publica e
renderiza soberano. A VPS NAO alcanca o PC (NAT) -> quem fala e o PC: a cada
~5 min empurra um timestamp pra VPS. A VPS le esse timestamp (`pc_online`) e,
se o PC estiver mudo, AVISA (Telegram) e cai no soberano em vez de travar o job.

Dois papeis num arquivo so:
  - LADO PC (Windows):  `heartbeat()` / CLI -> ssh empurra `date +%s` pra VPS.
  - LADO VPS (Linux):   `pc_online()` -> le o arquivo e decide se o PC esta vivo.

CLI (no PC, via Task Scheduler):  python heartbeat.py
Agendar a cada 5 min (PowerShell/cmd, uma vez):
  schtasks /Create /TN "MinutoReal-Heartbeat" /SC MINUTE /MO 5 ^
    /TR "python C:\\Users\\User\\.gemini\\antigravity\\scratch\\biblioteca\\videos\\heartbeat.py" /F
"""
import subprocess
import sys
import time
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

VPS = "root@andregalgani.com.br"                 # SSH sem senha ja configurado
REMOTO = "/opt/minutoreal/heartbeat.txt"          # arquivo do batimento (epoch s) na VPS
_SSH_TIMEOUT = 25                                  # ssh trava? aborta — nao pendura o agendador


def heartbeat() -> bool:
    """LADO PC: empurra o epoch atual pra VPS via ssh. True se empurrou; False se nao.

    Idempotente (sobrescreve o arquivo) e NUNCA levanta — o Task Scheduler nao
    deve acumular falha. Loga sucesso/erro COM contexto (Akita pilar 7).
    """
    cmd = ["ssh", "-o", "BatchMode=yes", VPS, f"date +%s > {REMOTO}"]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=_SSH_TIMEOUT)
    except Exception as e:
        print(f"  [heartbeat] ssh falhou: {type(e).__name__}: {str(e)[:160]}", file=sys.stderr)
        return False
    if r.returncode != 0:
        print(f"  [heartbeat] ssh saiu {r.returncode}: {(r.stderr or '').strip()[:200]}",
              file=sys.stderr)
        return False
    print(f"  [heartbeat] ok -> {VPS}:{REMOTO}")
    return True


def pc_online(caminho=None, agora=None, max_idade_s=600) -> bool:
    """LADO VPS: o PC local esta vivo? True se o batimento e mais novo que max_idade_s.

    PURO/testavel: `caminho` (default REMOTO) e `agora` (default time.time()) entram
    por parametro -> da p/ testar sem relogio nem arquivo reais. Velho/ausente/ilegivel
    => False (degrada p/ soberano, nunca levanta).
    """
    p = Path(caminho) if caminho is not None else Path(REMOTO)
    agora = time.time() if agora is None else agora
    try:
        bruto = p.read_text(encoding="utf-8").strip()
        batida = float(bruto)
    except (OSError, ValueError):
        return False
    return (agora - batida) < max_idade_s


if __name__ == "__main__":
    sys.exit(0 if heartbeat() else 1)
