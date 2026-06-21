# -*- coding: utf-8 -*-
"""Smoke test: verifica que gerar_video importa sem erro após a extração de módulos.

Um import quebrado (circular, nome faltando, símbolo não exportado) falha aqui
antes de qualquer teste de comportamento. Rápido: sem I/O, sem numpy, sem rede.
"""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


class TestGerarvVideoImport(unittest.TestCase):
    def test_import_sem_erro(self):
        """gerar_video deve importar sem lançar exceção."""
        import gerar_video  # noqa: F401

    def test_simbolos_tts_acessiveis(self):
        """Símbolos TTS devem ser acessíveis via gerar_video (re-export de _video_tts)."""
        import gerar_video
        self.assertTrue(callable(gerar_video._provedor_voz))
        self.assertTrue(callable(gerar_video._tts_eleven))
        self.assertTrue(callable(gerar_video._to_ssml))
        self.assertTrue(callable(gerar_video.tts))

    def test_simbolo_audio_acessivel(self):
        """sintetiza_ambiente deve ser acessível via gerar_video (re-export de _video_audio)."""
        import gerar_video
        self.assertTrue(callable(gerar_video.sintetiza_ambiente))

    def test_video_tts_import_isolado(self):
        """_video_tts importa de forma autônoma (sem depender de gerar_video)."""
        import _video_tts
        self.assertTrue(callable(_video_tts._to_ssml))

    def test_video_audio_import_isolado(self):
        """_video_audio importa de forma autônoma (sem depender de gerar_video)."""
        import _video_audio
        self.assertTrue(callable(_video_audio.sintetiza_ambiente))


if __name__ == '__main__':
    unittest.main()
