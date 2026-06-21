# -*- coding: utf-8 -*-
"""Teste de publish_to_live.py — usa SOMENTE pastas temporarias (nunca /opt nem
/var/www reais). Constroi um livro-fake "construido", roda o copiador apontando
para build/live temporarios e verifica que os arquivos aterrissaram no live —
incluindo a pasta do kit.

    python publish_to_live.test.py     # exit 0 = passou, 1 = falhou
"""
import os
import subprocess
import sys
import tempfile

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(HERE, "publish_to_live.py")
SLUG = "livro-fake"


def _write(path, content="x"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def build_fake(build_dir):
    """Cria um livro-fake JA construido dentro de build_dir."""
    _write(os.path.join(build_dir, f"{SLUG}.html"), "<html>capa</html>")
    _write(os.path.join(build_dir, "books.json"), '[{"id":"livro-fake"}]')
    # pasta do livro: 2 capitulos + script.js
    _write(os.path.join(build_dir, SLUG, "cap-1.html"), "<html>1</html>")
    _write(os.path.join(build_dir, SLUG, "cap-2.html"), "<html>2</html>")
    _write(os.path.join(build_dir, SLUG, "script.js"), "//js")
    # raiz opcional
    _write(os.path.join(build_dir, "index.html"), "<html>estante</html>")
    # assets
    _write(os.path.join(build_dir, "assets", "style.css"), "body{}")
    _write(os.path.join(build_dir, "assets", "favicon.svg"), "<svg/>")
    _write(os.path.join(build_dir, "assets", f"{SLUG}-capa.png"), "PNG")
    # KIT
    _write(os.path.join(build_dir, "assets", "kit", SLUG, "manifest.json"), "{}")
    _write(os.path.join(build_dir, "assets", "kit", SLUG, "slides.json"), "[]")
    _write(os.path.join(build_dir, "assets", "kit", SLUG, "caps.json"), "[]")
    _write(os.path.join(build_dir, "assets", "kit", "_tpl", SLUG, "quote.html"), "<q/>")
    _write(os.path.join(build_dir, "assets", "kit", "_carousel.css"), ".c{}")


def main():
    with tempfile.TemporaryDirectory() as tmp:
        build_dir = os.path.join(tmp, "build")
        live_dir = os.path.join(tmp, "live")
        build_fake(build_dir)

        r = subprocess.run(
            [sys.executable, SCRIPT, SLUG,
             "--build-dir", build_dir, "--live-dir", live_dir],
            capture_output=True, text=True, encoding="utf-8",
        )
        print(r.stdout)
        if r.stderr:
            print("STDERR:", r.stderr)

        if r.returncode != 0:
            print(f"FALHA: o copiador saiu com codigo {r.returncode}")
            sys.exit(1)

        # arquivos que DEVEM existir no live
        esperados = [
            f"{SLUG}.html",
            "books.json",
            os.path.join(SLUG, "cap-1.html"),
            os.path.join(SLUG, "cap-2.html"),
            os.path.join(SLUG, "script.js"),
            "index.html",
            os.path.join("assets", "style.css"),
            os.path.join("assets", "favicon.svg"),
            os.path.join("assets", f"{SLUG}-capa.png"),
            os.path.join("assets", "kit", SLUG, "manifest.json"),
            os.path.join("assets", "kit", SLUG, "slides.json"),
            os.path.join("assets", "kit", SLUG, "caps.json"),
            os.path.join("assets", "kit", "_tpl", SLUG, "quote.html"),
            os.path.join("assets", "kit", "_carousel.css"),
        ]
        faltando = [e for e in esperados
                    if not os.path.exists(os.path.join(live_dir, e))]
        if faltando:
            print(f"FALHA: nao aterrissaram no live: {faltando}")
            sys.exit(1)

        # sanidade: conteudo preservado (copia real, nao arquivo vazio)
        with open(os.path.join(live_dir, f"{SLUG}.html"), encoding="utf-8") as f:
            if f.read() != "<html>capa</html>":
                print("FALHA: conteudo de livro-fake.html nao bateu")
                sys.exit(1)

        # sanidade: a fonte real (/opt, /var/www) nao foi tocada — usamos so tmp,
        # entao basta garantir que tudo viveu dentro de tmp.
        assert live_dir.startswith(tmp) and build_dir.startswith(tmp)

        print(f"OK: {len(esperados)} arquivos aterrissaram no live temporario.")
        sys.exit(0)


if __name__ == "__main__":
    main()
