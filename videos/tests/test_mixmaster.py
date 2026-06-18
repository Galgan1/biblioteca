# -*- coding: utf-8 -*-
"""Sonoplasta — master −14 LUFS (alvo YouTube). Testa a decisão de mix PURA
(montagem do grafo de áudio) sem tocar ffmpeg/disco. Akita: verde = exit code."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]  # .../videos
sys.path.insert(0, str(ROOT))

try:
    import mixmaster as mm
    _OK = True
except Exception:
    _OK = False


@unittest.skipUnless(_OK, 'mixmaster indisponivel')
class TestDefaultMix(unittest.TestCase):
    def test_loudnorm_ligado_por_padrao(self):
        # o master deve normalizar por padrão (era inerte: ligado mas off por default)
        self.assertTrue(mm.DEFAULT_MIX['loudnorm'])

    def test_alvo_youtube(self):
        self.assertEqual(mm.DEFAULT_MIX['lufs'], -14)
        self.assertEqual(mm.DEFAULT_MIX['tp'], -1.0)


@unittest.skipUnless(_OK, 'mixmaster indisponivel')
class TestBuildAudioFilter(unittest.TestCase):
    def setUp(self):
        self.mix = dict(mm.DEFAULT_MIX)

    def test_voz_so_com_loudnorm(self):
        parts, last = mm._build_audio_filter(self.mix, has_trilha=False, has_efe=False)
        self.assertEqual(parts, ['[1:a]loudnorm=I=-14:TP=-1.0:LRA=11[a]'])
        self.assertEqual(last, '[a]')

    def test_loudnorm_desligado_nao_normaliza(self):
        self.mix['loudnorm'] = False
        parts, last = mm._build_audio_filter(self.mix, has_trilha=False, has_efe=False)
        self.assertEqual(parts, [])
        self.assertEqual(last, '[1:a]')

    def test_trilha_rebaixada_e_voz_soberana(self):
        self.mix['loudnorm'] = False
        parts, last = mm._build_audio_filter(self.mix, has_trilha=True, has_efe=False)
        self.assertEqual(parts[0], f'[2:a]volume={self.mix["music_gain"]}[m]')
        self.assertEqual(parts[1], '[1:a][m]amix=inputs=2:duration=first:dropout_transition=2[vt]')
        self.assertEqual(last, '[vt]')

    def test_sfx_sem_normalizar_e_indice_correto(self):
        self.mix['loudnorm'] = False
        parts, last = mm._build_audio_filter(self.mix, has_trilha=True, has_efe=True)
        # com trilha (idx 2) o SFX entra no idx 3
        self.assertIn('[3:a]volume=1.0[e]', parts)
        self.assertIn('normalize=0', parts[-1])
        self.assertEqual(last, '[ve]')

    def test_sfx_sem_trilha_usa_indice_2(self):
        self.mix['loudnorm'] = False
        parts, _ = mm._build_audio_filter(self.mix, has_trilha=False, has_efe=True)
        self.assertEqual(parts[0], '[2:a]volume=1.0[e]')

    def test_cadeia_completa_termina_em_loudnorm(self):
        parts, last = mm._build_audio_filter(self.mix, has_trilha=True, has_efe=True)
        self.assertEqual(parts[-1], '[ve]loudnorm=I=-14:TP=-1.0:LRA=11[a]')
        self.assertEqual(last, '[a]')


if __name__ == '__main__':
    unittest.main()
