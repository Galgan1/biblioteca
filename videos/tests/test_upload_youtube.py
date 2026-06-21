# -*- coding: utf-8 -*-
"""upload_youtube._enviar — o upload resumável faz retry POR CHUNK (num_retries),
NÃO re-sobe o vídeo inteiro (re-upload total criaria DUPLICATA no canal). Hermético:
HttpRequest falso, sem rede/OAuth. Akita: verde = exit code."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]   # .../videos
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import upload_youtube as uy  # noqa: E402


class _Status:
    def __init__(self, p):
        self._p = p

    def progress(self):
        return self._p


class _FakeReq:
    """Simula um HttpRequest resumável: 1 chunk parcial e depois conclui."""
    def __init__(self):
        self.retries_vistos = []
        self._n = 0

    def next_chunk(self, num_retries=0):
        self.retries_vistos.append(num_retries)
        self._n += 1
        if self._n < 2:
            return (_Status(0.5), None)      # chunk parcial (50%)
        return (None, {'id': 'VID123'})      # conclusão


class TestEnviarChunkRetry(unittest.TestCase):
    def test_conclui_e_retorna_resposta(self):
        resp = uy._enviar(_FakeReq())
        self.assertEqual(resp['id'], 'VID123')

    def test_todo_chunk_pede_retry_positivo(self):
        # cada next_chunk recebe num_retries > 0 → resiliência POR CHUNK,
        # nunca re-upload do vídeo inteiro (que duplicaria no canal).
        req = _FakeReq()
        uy._enviar(req)
        self.assertTrue(req.retries_vistos)
        self.assertTrue(all(nr > 0 for nr in req.retries_vistos))


if __name__ == '__main__':
    unittest.main()
