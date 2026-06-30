# -*- coding: utf-8 -*-
"""Contrato do handler /vendas (afiliados) do bot Telegram.

SEM rede: usa um fixture de afiliados.json em tmp e aponta o módulo para ele.
Verde = exit code. Roda no ponto único `python testar.py` (videos/tests/).
"""
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]  # .../videos
sys.path.insert(0, str(ROOT))

from _bot_handlers import h_vendas  # noqa: E402


class _Base(unittest.TestCase):
    def _render_com(self, dados) -> str:
        """Escreve `dados` num arquivo temp e roda render() apontado p/ ele."""
        d = tempfile.mkdtemp()
        p = Path(d) / "afiliados.json"
        p.write_text(json.dumps(dados), encoding="utf-8")
        orig = h_vendas._AFILIADOS
        h_vendas._AFILIADOS = p
        try:
            return h_vendas.render()
        finally:
            h_vendas._AFILIADOS = orig


class TestRender(_Base):
    def setUp(self):
        self.fixture = {
            "tag": "andregalgani-20",
            "dominio": "amazon.com.br",
            "lojas": {
                "amazon": {"nome": "Amazon", "ativa": True},
                "magalu": {"nome": "Magalu", "ativa": False},
            },
            "links_manuais": {},
            "asins": {
                "1984": "8535914846",
                "habitos-atomicos": "8550807567",
                "sapiens": "8535933921",
            },
        }

    def test_str_nao_vazia(self):
        out = self._render_com(self.fixture)
        self.assertIsInstance(out, str)
        self.assertTrue(out.strip())

    def test_reflete_a_tag_do_fixture(self):
        self.assertIn("andregalgani-20", self._render_com(self.fixture))

    def test_conta_livros_com_link(self):
        # 3 ASINs no fixture → "3" aparece na contagem de links de produto.
        out = self._render_com(self.fixture)
        self.assertIn("3", out)

    def test_vendas_honestas_sem_fonte(self):
        out = self._render_com(self.fixture).lower()
        self.assertIn("indispon", out)
        self.assertIn("pa-api", out)

    def test_vendas_reais_quando_ha_fonte(self):
        d = dict(self.fixture, vendas=7)
        out = self._render_com(d)
        self.assertIn("7", out)

    def test_teto_telegram(self):
        self.assertLessEqual(len(self._render_com(self.fixture)), 3500)


class TestBestEffort(_Base):
    def test_nao_levanta_com_json_invalido(self):
        d = tempfile.mkdtemp()
        p = Path(d) / "afiliados.json"
        p.write_text("{ nao eh json", encoding="utf-8")
        orig = h_vendas._AFILIADOS
        h_vendas._AFILIADOS = p
        try:
            out = h_vendas.render()  # não pode levantar
        finally:
            h_vendas._AFILIADOS = orig
        self.assertIsInstance(out, str)
        self.assertTrue(out.strip())

    def test_arquivo_ausente_nao_levanta(self):
        orig = h_vendas._AFILIADOS
        h_vendas._AFILIADOS = Path(tempfile.mkdtemp()) / "nao_existe.json"
        try:
            out = h_vendas.render()
        finally:
            h_vendas._AFILIADOS = orig
        self.assertIsInstance(out, str)
        self.assertTrue(out.strip())


if __name__ == "__main__":
    unittest.main()
