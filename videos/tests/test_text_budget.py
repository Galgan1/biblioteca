# -*- coding: utf-8 -*-
"""Testes unitários para videos/text_budget.py."""
import unittest
import sys
from pathlib import Path

# garante que o diretório pai (videos/) está no path ao rodar de dentro de tests/
sys.path.insert(0, str(Path(__file__).parent.parent))

from text_budget import contar_palavras, excede


class TestContarPalavras(unittest.TestCase):
    def test_conta_corretamente(self):
        self.assertEqual(contar_palavras("um dois três quatro cinco"), 5)

    def test_string_vazia(self):
        self.assertEqual(contar_palavras(""), 0)

    def test_multiplos_espacos(self):
        self.assertEqual(contar_palavras("  a  b  c  "), 3)

    def test_pontuacao_junto_conta_como_palavra(self):
        # "hábito," conta como 1 token — comportamento esperado por design
        self.assertEqual(contar_palavras("hábito, rotina."), 2)


class TestExcede(unittest.TestCase):
    def test_abaixo_do_limite_nao_excede(self):
        texto = " ".join(["palavra"] * 35)  # exatamente 35
        self.assertFalse(excede(texto))

    def test_acima_do_limite_excede(self):
        texto = " ".join(["palavra"] * 36)  # 36 > 35
        self.assertTrue(excede(texto))

    def test_limite_customizado(self):
        texto = "um dois três"  # 3 palavras
        self.assertFalse(excede(texto, limite=5))
        self.assertTrue(excede(texto, limite=2))


if __name__ == '__main__':
    unittest.main()
