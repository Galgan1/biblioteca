# -*- coding: utf-8 -*-
"""
engine.py — fala com o serviço biblioteca-pdf em modo refinador.

Sobe a NOSSA instância (REFINADOR=1) numa porta própria se ela não estiver no ar,
e renderiza páginas FRESCAS (sem cache) com um `tune` ad-hoc. Tudo local.
"""
import json
import os
import subprocess
import time
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
SVC = os.path.dirname(HERE)             # .../pdf-service
SITE_ROOT = os.path.dirname(SVC)        # .../biblioteca  (HTML do site ao vivo)
TUNED_PATH = os.path.join(HERE, "tuned.json")

PORT = int(os.environ.get("PDF_PORT", "3009"))  # porta do refinador (≠ 3008 de prod)
BASE = f"http://127.0.0.1:{PORT}"
CHROME = os.environ.get(
    "CHROME", r"C:\Program Files\Google\Chrome\Application\chrome.exe")

_proc = None  # instância que NÓS subimos (p/ encerrar no fim)


def health():
    try:
        with urllib.request.urlopen(BASE + "/health", timeout=3) as r:
            return json.load(r)
    except Exception:
        return None


def ensure_service(timeout=45):
    """Garante o serviço no ar com REFINADOR=1. Devolve o Popen se subimos nós."""
    global _proc
    if health():
        return None  # já estava no ar (assumimos que com REFINADOR=1)
    env = dict(os.environ, SITE_ROOT=SITE_ROOT, CHROME=CHROME,
               PORT=str(PORT), REFINADOR="1")
    _proc = subprocess.Popen(
        ["node", "server.js"], cwd=SVC, env=env,
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    t0 = time.time()
    while time.time() - t0 < timeout:
        if health():
            return _proc
        if _proc.poll() is not None:
            raise RuntimeError("node saiu antes de subir (cheque deps/Chrome)")
        time.sleep(0.6)
    stop_service()
    raise RuntimeError("serviço não respondeu /health a tempo")


def stop_service():
    global _proc
    if _proc and _proc.poll() is None:
        _proc.terminate()
        try:
            _proc.wait(timeout=8)
        except Exception:
            _proc.kill()
    _proc = None


def render(book, page, tune=None, timeout=150):
    """Renderiza fresco. Devolve (pdf_bytes, diag_do_fit)."""
    q = ""
    if tune:
        q = "?tune=" + urllib.parse.quote(json.dumps(tune, separators=(",", ":")))
    url = f"{BASE}/pdf/_refinar/{book}/{page}{q}"
    with urllib.request.urlopen(url, timeout=timeout) as r:
        try:
            diag = json.loads(r.headers.get("X-Fit-Diag") or "{}")
        except Exception:
            diag = {}
        return r.read(), diag


def reload_tuned():
    """Pede ao serviço para reler o tuned.json (após gravarmos)."""
    req = urllib.request.Request(BASE + "/pdf/_reload-tuned", method="POST", data=b"")
    with urllib.request.urlopen(req, timeout=10) as r:
        return json.load(r)
