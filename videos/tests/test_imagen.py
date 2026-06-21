# -*- coding: utf-8 -*-
"""imagen.py — guarda da chave (ausente NÃO derruba o import do pipeline) e degradação
limpa quando não há chave. Hermético: sem rede, sem chave real. Akita: verde = exit code."""
import sys
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]   # .../videos
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import imagen  # noqa: E402


class TestChaveGuard(unittest.TestCase):
    def test_read_key_ausente_retorna_vazio(self):
        # chave ilegível/ausente -> '' (em vez de levantar e derrubar o import do módulo).
        with mock.patch('pathlib.Path.read_text', side_effect=FileNotFoundError):
            self.assertEqual(imagen._read_key(), '')

    def test_sem_chave_gen_retorna_none_sem_excecao(self):
        # sem chave, gen() aborta com None (caller cai p/ provider 'fal'/'local'),
        # nunca levanta nem chama a rede.
        with mock.patch.object(imagen, 'KEY', ''):
            try:
                self.assertIsNone(imagen.gen('prompt qualquer', '/tmp/_imagen_test.png'))
            except Exception as e:
                self.fail(f'gen() sem chave levantou exceção (deveria degradar): {e}')


if __name__ == '__main__':
    unittest.main()
