# -*- coding: utf-8 -*-
"""produzir_shorts._short_privacidade — o Short herda a privacidade do roteiro
(consistente com o longo), não fica preso em 'unlisted'. Regressão jun/26: Shorts
subiam unlisted mesmo com o longo público -> não apareciam publicados no YouTube.
Akita: verde = exit code."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import produzir_shorts as ps  # noqa: E402


class TestShortPrivacidade(unittest.TestCase):
    def test_herda_publico_do_roteiro(self):
        self.assertEqual(ps._short_privacidade({'youtube': {'privacidade': 'public'}}), 'public')

    def test_default_unlisted_sem_campo(self):
        self.assertEqual(ps._short_privacidade({}), 'unlisted')
        self.assertEqual(ps._short_privacidade({'youtube': {}}), 'unlisted')

    def test_respeita_unlisted_explicito(self):
        self.assertEqual(ps._short_privacidade({'youtube': {'privacidade': 'unlisted'}}), 'unlisted')


if __name__ == '__main__':
    unittest.main()
