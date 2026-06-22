# -*- coding: utf-8 -*-
"""Contratos do ORQUESTRADOR de publicação (`publicar_livro.py`).

Antes deste arquivo o orquestrador tinha 0 cobertura (A2_testes nº2). Cobre:
  - `validate()`: o schema-guard que ABORTA cedo (antes de gastar geração) em
    `<slug>_data.py` malformado;
  - a SEQUÊNCIA do contrato "Verificação Editorial": o step-1b
    (`verificar_conteudo --fix`) roda ANTES de gerar qualquer página.

unittest.TestCase p/ entrar no gate canônico `python testar.py`.
"""
import os
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import publicar_livro as P  # noqa: E402
import gerar_livro          # noqa: E402

_VALID = """
BOOK = {"title": "T", "author": "A", "header_light": "H", "header_bold": "B",
        "intro": "i", "description": "d"}
CHAPTERS = [{"slug": "ch01", "sub": "Cap 1", "intro": "i",
             "cards": [{"ic": "book", "t": "t", "b": "b"}]}]
"""


class TestValidate(unittest.TestCase):
    """`validate(slug)` carrega <slug>_data.py e ABORTA (SystemExit) se inválido."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        sys.path.insert(0, self._tmp.name)
        self._mods = []
        self.addCleanup(self._cleanup)

    def _cleanup(self):
        sys.path.remove(self._tmp.name)
        for m in self._mods:
            sys.modules.pop(m, None)
        self._tmp.cleanup()

    def _write(self, slug, body):
        """Grava <slug>_data.py no tmpdir e devolve o slug (importável)."""
        mod = slug.replace("-", "_") + "_data"
        Path(self._tmp.name, mod + ".py").write_text(textwrap.dedent(body), encoding="utf-8")
        self._mods.append(mod)
        return slug

    def test_valido_retorna_book_e_chapters(self):
        slug = self._write("zz-valido", _VALID)
        B, CH = P.validate(slug)
        self.assertEqual(B["title"], "T")
        self.assertEqual(len(CH), 1)

    def test_book_sem_chave_obrigatoria_aborta(self):
        slug = self._write("zz-sem-author", _VALID.replace('"author": "A",', ""))
        with self.assertRaises(SystemExit):
            P.validate(slug)

    def test_capitulo_sem_cards_aborta(self):
        body = _VALID.replace('"cards": [{"ic": "book", "t": "t", "b": "b"}]', '"cards": []')
        slug = self._write("zz-sem-cards", body)
        with self.assertRaises(SystemExit):
            P.validate(slug)

    def test_slugs_de_capitulo_duplicados_aborta(self):
        body = """
        BOOK = {"title": "T", "author": "A", "header_light": "H", "header_bold": "B",
                "intro": "i", "description": "d"}
        CHAPTERS = [{"slug": "ch01", "sub": "C1", "intro": "i", "cards": [{"ic":"book","t":"t","b":"b"}]},
                    {"slug": "ch01", "sub": "C2", "intro": "i", "cards": [{"ic":"book","t":"t","b":"b"}]}]
        """
        slug = self._write("zz-dup", body)
        with self.assertRaises(SystemExit):
            P.validate(slug)

    def test_card_sem_ic_t_b_aborta(self):
        body = _VALID.replace('{"ic": "book", "t": "t", "b": "b"}', '{"ic": "book"}')
        slug = self._write("zz-card-incompleto", body)
        with self.assertRaises(SystemExit):
            P.validate(slug)


class TestStep1bAntesDeGerar(unittest.TestCase):
    """Contrato 'Verificação Editorial': a checagem de fidelidade roda ANTES da geração."""

    def test_verificar_conteudo_roda_antes_de_gerar_livro(self):
        order = []
        B = {"title": "T", "author": "A", "cover": "x"}
        CH = [{"slug": "ch01", "cards": [{}]}]

        def fake_run(cmd, cwd=None):
            order.append(" ".join(str(c) for c in cmd))

        with mock.patch.object(sys, "argv", ["publicar_livro.py", "zz-ord"]), \
             mock.patch.object(P, "validate", return_value=(B, CH)), \
             mock.patch.object(P, "run", side_effect=fake_run), \
             mock.patch.object(P, "ensure_cover"), \
             mock.patch.object(P, "verify"), \
             mock.patch.object(gerar_livro, "main",
                               side_effect=lambda s: order.append("GERAR_LIVRO")):
            P.main()

        joined = "\n".join(order)
        self.assertIn("verificar_conteudo.py", joined)
        self.assertIn("--fix", joined)                       # corrige cirurgicamente
        i_verif = next(i for i, c in enumerate(order) if "verificar_conteudo.py" in c)
        i_gerar = order.index("GERAR_LIVRO")
        self.assertLess(i_verif, i_gerar,
                        f"verificar_conteudo deve preceder a geração; ordem={order}")


if __name__ == "__main__":
    unittest.main()
