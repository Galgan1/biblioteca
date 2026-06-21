# -*- coding: utf-8 -*-
"""Regressão do publish_to_live.py — o copiador staging→ao vivo (portão de publicação).

Hermético: pastas TEMPORÁRIAS, nunca /opt nem /var/www reais. Verde = exit code
(Akita pilar 2). Recria o teste que se perdeu no sumiço de arquivos não-commitados.
"""
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import publish_to_live as P  # noqa: E402


def _fake_build(build, slug):
    """Monta um livro 'construído' fake (página + capítulos + kit + capa) na build."""
    b = Path(build)
    (b / f"{slug}.html").write_text("<html>página</html>", encoding="utf-8")
    (b / "books.json").write_text("[]", encoding="utf-8")
    cap = b / slug
    cap.mkdir(parents=True, exist_ok=True)
    (cap / "ch01.html").write_text("cap1", encoding="utf-8")
    (cap / "script.js").write_text("//", encoding="utf-8")
    assets = b / "assets"
    assets.mkdir(parents=True, exist_ok=True)
    (assets / "style.css").write_text("x", encoding="utf-8")
    (assets / "favicon.svg").write_text("<svg/>", encoding="utf-8")
    (assets / f"{slug}-capa.png").write_bytes(b"PNG")
    kit = assets / "kit" / slug
    kit.mkdir(parents=True, exist_ok=True)
    (kit / "manifest.json").write_text("{}", encoding="utf-8")


class TestPublish(unittest.TestCase):
    def test_copia_pagina_capitulos_e_kit(self):
        with tempfile.TemporaryDirectory() as build, tempfile.TemporaryDirectory() as live:
            _fake_build(build, "meu-livro")
            P.publish("meu-livro", build, live)
            L = Path(live)
            for rel in ("meu-livro.html", "books.json", "meu-livro/ch01.html",
                        "assets/kit/meu-livro/manifest.json", "assets/meu-livro-capa.png"):
                self.assertTrue((L / rel).exists(), f"faltou no live: {rel}")

    def test_conteudo_e_preservado(self):
        with tempfile.TemporaryDirectory() as build, tempfile.TemporaryDirectory() as live:
            _fake_build(build, "x")
            P.publish("x", build, live)
            self.assertEqual((Path(live) / "x.html").read_text(encoding="utf-8"),
                             "<html>página</html>")

    def test_obrigatorio_ausente_aborta(self):
        # build sem o <slug>.html obrigatório → encerra com exit != 0 (não publica meia-página)
        with tempfile.TemporaryDirectory() as build, tempfile.TemporaryDirectory() as live:
            with self.assertRaises(SystemExit) as cm:
                P.publish("nao-existe", build, live)
            self.assertNotEqual(cm.exception.code, 0)


if __name__ == "__main__":
    unittest.main()
