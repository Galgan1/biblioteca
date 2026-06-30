# -*- coding: utf-8 -*-
"""sincronizar_facebook.fila_pendente — fila interleaved (round-robin por livro) dos
Reels pendentes no FB, pulando o que já saiu. Pura/hermética. Akita: verde = exit code."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import sincronizar_facebook as sf  # noqa: E402


class TestFilaPendente(unittest.TestCase):
    def test_interleave_round_robin_pula_feito(self):
        clipes = {'a': [1, 2, 3], 'b': [1, 2], 'c': [1]}
        feito = {'a': {1}}                      # a1 já no FB -> pendentes de a = [2,3]
        fila = sf.fila_pendente(clipes, feito)
        # pos0: a2, b1, c1 ; pos1: a3, b2 (c só tem 1)
        self.assertEqual(fila, [('a', 2), ('b', 1), ('c', 1), ('a', 3), ('b', 2)])

    def test_tudo_feito_fila_vazia(self):
        self.assertEqual(sf.fila_pendente({'a': [1, 2]}, {'a': {1, 2}}), [])

    def test_sem_feito_posta_tudo(self):
        fila = sf.fila_pendente({'x': [1], 'y': [1]}, {})
        self.assertEqual(fila, [('x', 1), ('y', 1)])


if __name__ == '__main__':
    unittest.main()
