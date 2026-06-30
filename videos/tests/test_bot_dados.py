# -*- coding: utf-8 -*-
"""Regressão do resolvedor de dados (_dados.caminho).

BUG 22/jun: o bot mostrava 73 livros (cópia stale /opt/minutoreal/books.json) em vez
dos 103 do site. Causa: o resolvedor preferia o dir do pipeline ao CANÔNICO do site.
Estes testes pinam o conserto: o canônico do site vem PRIMEIRO e, entre raízes que
têm o arquivo, vence a anterior. Sem rede; roda no `python testar.py`.
"""
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from _bot_handlers import _dados


class TestResolvedor(unittest.TestCase):
    def test_canonico_do_site_vem_primeiro(self):
        # invariante do conserto: o site (verdade do usuário) é a 1ª prioridade.
        self.assertEqual(_dados._RAIZES[0], Path("/var/www/andregalgani/biblioteca"))

    def test_entre_raizes_com_o_arquivo_vence_a_anterior(self):
        # modela o cenário do bug: canônico (103) antes da cópia stale (73).
        with tempfile.TemporaryDirectory() as d:
            site = Path(d) / "site"
            stale = Path(d) / "stale"
            site.mkdir()
            stale.mkdir()
            (site / "books.json").write_text(json.dumps([{}] * 103), encoding="utf-8")
            (stale / "books.json").write_text(json.dumps([{}] * 73), encoding="utf-8")
            with mock.patch.object(_dados, "_RAIZES", [site, stale]):
                p = _dados.caminho("books.json")
            self.assertEqual(len(json.loads(p.read_text(encoding="utf-8"))), 103)  # NÃO 73

    def test_env_override_vence_tudo(self):
        with tempfile.TemporaryDirectory() as d:
            alvo = Path(d)
            (alvo / "books.json").write_text("[]", encoding="utf-8")
            with mock.patch.dict(os.environ, {"BIBLIOTECA_DADOS": str(alvo)}):
                self.assertEqual(_dados.caminho("books.json"), alvo / "books.json")

    def test_inexistente_devolve_primeiro_candidato(self):
        # nunca levanta; devolve um caminho legível p/ a mensagem de erro.
        self.assertTrue(str(_dados.caminho("__nao_existe__.json")))


if __name__ == "__main__":
    unittest.main()
