# -*- coding: utf-8 -*-
"""Contrato: voz POR CENA (2+ vozes no mesmo vídeo, sem virar podcast).
Origem: Admirável Mundo Novo (22/jun) — narrador masc. + voz feminina nos slogans do Estado."""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import gerar_video as g


class TestVozCena(unittest.TestCase):
    def test_cena_sem_voz_usa_global(self):
        voz, rate = g._voz_cena({'narracao': 'x'}, 'eleven:NARRADOR', 1.0)
        self.assertEqual(voz, 'eleven:NARRADOR')
        self.assertEqual(rate, 1.0)

    def test_cena_com_voz_sobrepoe(self):
        voz, rate = g._voz_cena({'voz': 'eleven:FEMININA'}, 'eleven:NARRADOR', 1.0)
        self.assertEqual(voz, 'eleven:FEMININA')          # a 2ª voz (slogan do Estado)

    def test_tts_rate_por_cena(self):
        # slogan hipnótico pode pedir ritmo mais lento que o narrador
        _, rate = g._voz_cena({'tts_rate': 0.9}, 'eleven:N', 1.0)
        self.assertAlmostEqual(rate, 0.9)


if __name__ == '__main__':
    unittest.main()
