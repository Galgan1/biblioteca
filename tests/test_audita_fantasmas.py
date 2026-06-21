# -*- coding: utf-8 -*-
"""Testa o guarda anti-fantasma (audita_fantasmas.detectar).

Input sintetico em tmpdir — sem git, sem rede, determinista. Reproduz o bug
que motivou o guarda: fonte rastreada importando modulo local nao versionado.
"""
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import audita_fantasmas  # noqa: E402


class TestDetectarFantasma(unittest.TestCase):
    def _cenario(self, root: Path):
        """app.py (importa helper) + helper.py no disco — como o bug do carrossel."""
        (root / "app.py").write_text("import helper\nx = helper.f()\n", encoding="utf-8")
        (root / "helper.py").write_text("def f():\n    return 1\n", encoding="utf-8")

    def test_importa_modulo_orfao_e_flagado(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self._cenario(root)
            # helper.py existe no disco mas NAO esta rastreado -> fantasma
            achados = audita_fantasmas.detectar({"app.py"}, root)
            self.assertEqual(achados, [("app.py", "helper")])

    def test_modulo_rastreado_nao_e_flagado(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self._cenario(root)
            # helper.py rastreado -> sem fantasma (o caso saudavel)
            achados = audita_fantasmas.detectar({"app.py", "helper.py"}, root)
            self.assertEqual(achados, [])

    def test_import_stdlib_nao_e_flagado(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "app.py").write_text("import os\nimport json\n", encoding="utf-8")
            # os.py/json.py nao existem na raiz -> nao sao locais, nao flaga
            self.assertEqual(audita_fantasmas.detectar({"app.py"}, root), [])

    def test_from_import_orfao_e_flagado(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "app.py").write_text("from helper import f\n", encoding="utf-8")
            (root / "helper.py").write_text("def f():\n    return 1\n", encoding="utf-8")
            self.assertEqual(audita_fantasmas.detectar({"app.py"}, root), [("app.py", "helper")])


if __name__ == "__main__":
    unittest.main()
