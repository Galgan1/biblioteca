# -*- coding: utf-8 -*-
"""Testes do wiring de áudio do Short (`gerar_short._audio_filter`).

Prova a LÓGICA do filtro sem rodar o ffmpeg: a voz é atrasada (entra após
capa+respiro) e o leito de engajamento [4] é mixado por baixo (voz soberana).
Import smoke garante que o wiring não quebrou o módulo.
"""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import gerar_short as gs


class TestAudioFilter(unittest.TestCase):
    def test_voz_atrasada_pela_capa_mais_respiro(self):
        f = gs._audio_filter(2.4, 0.45)
        self.assertIn('adelay=2850:all=1', f)        # (2.4+0.45)*1000 ms

    def test_leito_mixado_sob_a_voz(self):
        f = gs._audio_filter(2.4, 0.45)
        self.assertIn('[4:a]', f)                    # o leito de engajamento entra
        self.assertIn('amix=inputs=2', f)
        self.assertIn('normalize=0', f)              # voz cheia, leito por baixo
        self.assertIn('alimiter', f)                 # trava o pico acento+voz

    def test_saida_rotulada_a(self):
        self.assertTrue(gs._audio_filter(2.4, 0.45).endswith('[a]'))


class TestRevealOffsets(unittest.TestCase):
    """`_reveal_offsets` — synch point de conteúdo a partir do campo `reveal` da cena."""

    def test_ausente_vazio(self):
        self.assertEqual(gs._reveal_offsets({'narracao': 'oi'}, 2.85, 10.0), [])

    def test_false_vazio(self):
        self.assertEqual(gs._reveal_offsets({'reveal': False, 'narracao': 'oi'}, 2.85, 10.0), [])

    def test_true_meio_da_narracao(self):
        off = gs._reveal_offsets({'reveal': True, 'narracao': 'oi'}, 2.85, 10.0)
        self.assertAlmostEqual(off[0], 7.85, places=6)             # voice_start + voice_dur/2

    def test_numero_segundos(self):
        off = gs._reveal_offsets({'reveal': 4.2, 'narracao': 'oi'}, 2.85, 10.0)
        self.assertAlmostEqual(off[0], 7.05, places=6)             # voice_start + 4.2

    def test_substring_proporcional(self):
        off = gs._reveal_offsets({'reveal': 'f', 'narracao': 'abcdefghij'}, 2.85, 10.0)
        self.assertAlmostEqual(off[0], 7.85, places=3)             # 'f' no índice 5/10 = 0.5

    def test_substring_inexistente_vazio(self):
        self.assertEqual(gs._reveal_offsets({'reveal': 'zzz', 'narracao': 'abc'}, 2.85, 10.0), [])

    def test_offset_clampado_ao_fim(self):
        off = gs._reveal_offsets({'reveal': 999.0, 'narracao': 'oi'}, 2.85, 10.0)
        self.assertAlmostEqual(off[0], 12.85, places=6)            # clampa em voice_start+voice_dur


if __name__ == '__main__':
    unittest.main()
