# -*- coding: utf-8 -*-
"""Testes de contrato para ig_metricas.py.

unittest.TestCase (não funções soltas) para entrar no gate canônico
`python testar.py` (unittest discover).
"""
import io
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).parent.parent))

import ig_metricas as im


class TestRelatorioSemDados(unittest.TestCase):
    def test_relatorio_sem_dados_imprime_sem_crash(self):
        """Com metricas={} deve imprimir 'sem dados' sem lançar exceção."""
        state = {"metricas": {}}
        buf = io.StringIO()
        with patch("sys.stdout", buf):
            im.cmd_relatorio(state)
        self.assertIn("sem dados", buf.getvalue())


class TestScore(unittest.TestCase):
    def test_score_calculo(self):
        """score = views + saves*10 + reach*0.1 = 100+100+100 = 300."""
        m = {"views": 100, "saves": 10, "reach": 1000}
        self.assertAlmostEqual(im.calcular_score(m), 300.0)

    def test_score_zeros(self):
        self.assertEqual(im.calcular_score({}), 0.0)

    def test_score_so_reach(self):
        self.assertAlmostEqual(im.calcular_score({"reach": 200}), 20.0)


class TestTop3Bottom3(unittest.TestCase):
    LIVROS = {
        "alfa":    {"views": 1000, "saves": 50, "reach": 500},   # score=1550
        "beta":    {"views": 500,  "saves": 30, "reach": 300},   # score=830
        "gama":    {"views": 200,  "saves": 10, "reach": 100},   # score=310
        "delta":   {"views": 100,  "saves": 5,  "reach": 50},    # score=155
        "epsilon": {"views": 10,   "saves": 1,  "reach": 10},    # score=21
    }

    def _capturar_relatorio(self, livros: dict) -> str:
        buf = io.StringIO()
        with patch("sys.stdout", buf):
            im.cmd_relatorio({"metricas": livros})
        return buf.getvalue()

    def test_top3_correto(self):
        saida = self._capturar_relatorio(self.LIVROS)
        linhas_top = saida.split("TOP-3:")[1].split("BOTTOM-3:")[0]
        self.assertIn("alfa", linhas_top)
        self.assertIn("beta", linhas_top)
        self.assertIn("gama", linhas_top)

    def test_bottom3_correto(self):
        saida = self._capturar_relatorio(self.LIVROS)
        self.assertIn("BOTTOM-3:", saida)
        linhas_bot = saida.split("BOTTOM-3:")[1]
        self.assertIn("epsilon", linhas_bot)
        self.assertIn("delta", linhas_bot)

    def test_top3_exatos_3_itens(self):
        saida = self._capturar_relatorio(self.LIVROS)
        linhas_top = [l for l in saida.split("TOP-3:")[1].split("BOTTOM-3:")[0].splitlines() if l.strip()]
        self.assertEqual(len(linhas_top), 3)

    def test_menos_de_4_livros_sem_bottom(self):
        """Com <=3 livros não deve imprimir BOTTOM-3."""
        tres = dict(list(self.LIVROS.items())[:3])
        saida = self._capturar_relatorio(tres)
        self.assertNotIn("BOTTOM-3:", saida)


class TestUpdateOffline(unittest.TestCase):
    def test_update_sem_token_modo_offline(self):
        """--update sem token não deve fazer HTTP nem crashar."""
        state = {"metricas": {}}
        chamadas_http = []

        def _get_mock(url: str):
            chamadas_http.append(url)
            return None

        buf = io.StringIO()
        with patch("ig_metricas._get", _get_mock), patch("sys.stdout", buf):
            im.cmd_update(state)

        self.assertEqual(chamadas_http, [], "Não deve chamar HTTP sem token")
        self.assertIn("offline", buf.getvalue().lower())

    def test_update_com_token_sem_user_id_modo_offline(self):
        """Token presente mas sem user_id também deve cair em modo offline."""
        state = {"ig_token": "tok_fake", "metricas": {}}
        chamadas_http = []

        def _get_mock(url: str):
            chamadas_http.append(url)
            return None

        buf = io.StringIO()
        with (
            patch("ig_metricas._get", _get_mock),
            patch("ig_metricas.SECRETS", Path("/nao/existe")),
            patch("sys.stdout", buf),
        ):
            im.cmd_update(state)

        self.assertEqual(chamadas_http, [], "Não deve chamar HTTP sem user_id")


if __name__ == "__main__":
    unittest.main()
