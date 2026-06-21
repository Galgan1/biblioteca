# -*- coding: utf-8 -*-
"""worker_upload.test.py — teste do portão e do runbook (sem IA, sem deploy).

    python pdf-service/worker_upload.test.py

Verifica, em isolamento (NÃO chama `claude -p`, NÃO publica, NÃO faz deploy):
  1. data_gate.py sai 1 num `<slug>_data.py` propositalmente quebrado;
  2. data_gate.py sai 0 num `<slug>_data.py` bom de verdade
     (usa o padrão-ouro existente: 'leis-da-natureza-humana');
  3. runbook_upload.md contém os placeholders {SLUG} e {SOURCE_FILE} e a lista
     de ícones válida.

Saída: sys.exit(0) se tudo passar; sys.exit(1) na primeira falha.
"""
import os
import subprocess
import sys
import tempfile

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
DATA_GATE = os.path.join(AQUI, "data_gate.py")
RUNBOOK = os.path.join(AQUI, "runbook_upload.md")

falhas = 0


def ok(label):
    print(f"ok - {label}")


def falha(label, detalhe=""):
    global falhas
    falhas += 1
    print(f"FALHA - {label}: {detalhe}")


def rodar_gate(slug):
    """Roda data_gate.py <slug> com cwd=RAIZ (onde vivem os *_data.py). rc."""
    r = subprocess.run(
        [sys.executable, DATA_GATE, slug], cwd=RAIZ,
        capture_output=True, text=True, encoding="utf-8", errors="replace")
    return r.returncode, (r.stdout or "") + (r.stderr or "")


# --- 1) gate reprova (rc=1) um _data.py quebrado ----------------------------
# Card com `ic` inválido, `b` sem <strong>, BOOK sem cover/overview_cards e só
# 1 capítulo: vários motivos de uma vez. Escrito num slug temporário na RAIZ.
QUEBRADO = '''# -*- coding: utf-8 -*-
BOOK = {"title": "X", "author": "Y"}
CHAPTERS = [
  {"slug": "ch01", "sub": "CAP 1", "intro": "i",
   "cards": [{"ic": "naoexiste", "t": "T", "b": "corpo sem strong nenhum aqui."}]},
]
'''

slug_ruim = "zzz-gate-teste-quebrado"
arq_ruim = os.path.join(RAIZ, slug_ruim.replace("-", "_") + "_data.py")
try:
    with open(arq_ruim, "w", encoding="utf-8") as f:
        f.write(QUEBRADO)
    rc, out = rodar_gate(slug_ruim)
    if rc == 1:
        ok("data_gate sai 1 num _data.py quebrado")
    else:
        falha("data_gate deveria reprovar o quebrado", f"rc={rc}; saída:\n{out}")
finally:
    if os.path.exists(arq_ruim):
        os.remove(arq_ruim)
    # limpa o .pyc para não envenenar uma reimportação futura do mesmo nome
    pyc = os.path.join(RAIZ, "__pycache__")
    if os.path.isdir(pyc):
        for n in os.listdir(pyc):
            if n.startswith(slug_ruim.replace("-", "_")):
                try:
                    os.remove(os.path.join(pyc, n))
                except OSError:
                    pass


# --- 2) gate aprova (rc=0) um _data.py bom de verdade -----------------------
rc, out = rodar_gate("leis-da-natureza-humana")
if rc == 0:
    ok("data_gate sai 0 no padrão-ouro (leis-da-natureza-humana)")
else:
    falha("data_gate deveria aprovar o padrão-ouro", f"rc={rc}; saída:\n{out}")


# --- 3) runbook contém placeholders + lista de ícones -----------------------
with open(RUNBOOK, encoding="utf-8") as f:
    runbook = f.read()

for token in ("{SLUG}", "{SOURCE_FILE}"):
    if token in runbook:
        ok(f"runbook contém o placeholder {token}")
    else:
        falha("runbook sem placeholder", token)

# alguns ícones-âncora que TÊM de estar na lista impressa no runbook
ICONES_ANCORA = ["arrow", "bubble", "constellation", "mask", "triangle", "wrench"]
faltando = [ic for ic in ICONES_ANCORA if ic not in runbook]
if not faltando:
    ok("runbook contém a lista de ícones válida")
else:
    falha("runbook sem ícones da lista", str(faltando))


# --- veredito ---------------------------------------------------------------
if falhas:
    print(f"\n{falhas} falha(s).")
    sys.exit(1)
print("\nTudo verde.")
sys.exit(0)
