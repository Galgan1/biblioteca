# -*- coding: utf-8 -*-
"""Testes herméticos de veo.py — sem rede real, sem chave Google.

urllib.request.urlopen é mockado no módulo veo antes de qualquer chamada de rede.
Estado do circuit breaker isolado em arquivo temporário (mesmo padrão de
test_falgen.py: mixin _IsolateCB + mock de time.sleep p/ não esperar o backoff).

Nota sobre interação retry × breaker (igual falgen):
  Ordem dos decoradores: @retry(externo) → @circuit_breaker(interno).
  Cada tentativa do retry chega ao breaker como chamada independente.
  Com max_attempts=2 e threshold=2, UMA chamada a animate() com erro de
  rede permanente já abre o circuit (2 tentativas = 2 incrementos de falha).
"""
import io
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

# Garante que o diretório videos/ está no sys.path para importar veo.
_VIDEOS = Path(__file__).resolve().parent.parent
if str(_VIDEOS) not in sys.path:
    sys.path.insert(0, str(_VIDEOS))

# Precisamos de circuit_breaker antes de importar veo para poder
# redirecionar _STATE_FILE para o arquivo temporário.
import circuit_breaker as cb

# veo.py lê a chave do disco no import. Em CI mínimo o arquivo pode não
# existir — stuba o read_text de Path só durante o import do módulo.
if not (_VIDEOS / '.secrets' / 'imagen_api_key.txt').exists():
    with mock.patch.object(Path, 'read_text', return_value='FAKE_KEY'):
        import veo  # noqa: E402
else:
    import veo  # noqa: E402


def _resp(payload):
    """Fabrica um file-like que devolve `payload` (bytes) em .read() e funciona
    com json.load (que chama .read())."""
    if isinstance(payload, (dict, list)):
        payload = json.dumps(payload).encode('utf-8')
    return io.BytesIO(payload)


class _IsolateCB:
    """Mixin: redireciona cb._STATE_FILE para temp e restaura no tearDown.
    Também mocka time.sleep (do circuit_breaker E do veo) para eliminar
    espera real do backoff de retry e do poll de 10s."""

    def setUp(self):
        fd, nome = tempfile.mkstemp(suffix='.json')
        os.close(fd)
        self._tmp = Path(nome)
        self._orig_state = cb._STATE_FILE
        cb._STATE_FILE = self._tmp
        # Elimina backoff real do retry e o sleep(10) do loop de poll do veo.
        self._sleep_cb = mock.patch('circuit_breaker.time.sleep')
        self._sleep_veo = mock.patch('veo.time.sleep')
        self._sleep_cb.start()
        self._sleep_veo.start()

    def tearDown(self):
        self._sleep_cb.stop()
        self._sleep_veo.stop()
        cb._STATE_FILE = self._orig_state
        self._tmp.unlink(missing_ok=True)


# ---------------------------------------------------------------------------
# animate() — sucesso
# ---------------------------------------------------------------------------

class TestAnimateSucesso(_IsolateCB, unittest.TestCase):
    """animate() bem-sucedido retorna True, grava arquivo não-vazio e fecha o circuit."""

    def test_sucesso_grava_arquivo_nao_vazio_e_retorna_true(self):
        # urlopen é chamado 3x: start (op) -> poll (done) -> download (bytes).
        start = _resp({'name': 'operations/abc'})
        poll = _resp({'done': True, 'response': {'videoUri': 'https://v/out.mp4'}})
        download = _resp(b'MP4DATA' * 50)
        seq = [start, poll, download]

        with tempfile.TemporaryDirectory() as d:
            out = os.path.join(d, 'out.mp4')
            with mock.patch.object(Path, 'read_bytes', return_value=b'\x89PNG'), \
                 mock.patch.object(veo.urllib.request, 'urlopen',
                                   side_effect=lambda *a, **k: seq.pop(0)):
                result = veo.animate('img.png', 'movimento', out)

            self.assertTrue(result)
            self.assertTrue(os.path.exists(out))
            self.assertGreater(os.path.getsize(out), 0)

        self.assertEqual(cb.get_circuit_state('google_veo')['state'], 'closed')


# ---------------------------------------------------------------------------
# animate() — exceção de rede → retry + breaker
# ---------------------------------------------------------------------------

class TestAnimateRetryEBreaker(_IsolateCB, unittest.TestCase):
    """Exceção de rede: @retry tenta 2x e o breaker abre (threshold=2)."""

    def test_retry_tenta_2_vezes_e_breaker_abre(self):
        chamadas = {'n': 0}

        def urlopen_falha(*args, **kwargs):
            chamadas['n'] += 1
            raise urllib_error_urlerror('conexão recusada')

        with mock.patch.object(Path, 'read_bytes', return_value=b'\x89PNG'), \
             mock.patch.object(veo.urllib.request, 'urlopen', side_effect=urlopen_falha):
            with self.assertRaises(Exception):
                veo.animate('img.png', 'p', '/tmp/x.mp4')

        # @retry(max_attempts=2): exatamente 2 tentativas chegaram ao urlopen.
        self.assertEqual(chamadas['n'], 2)
        # 2 falhas == threshold → circuit OPEN.
        self.assertEqual(cb.get_circuit_state('google_veo')['state'], 'open')


# ---------------------------------------------------------------------------
# animate() — anti-fantasma: download vazio
# ---------------------------------------------------------------------------

class TestAnimateDownloadVazio(_IsolateCB, unittest.TestCase):
    """Download de 0 bytes NÃO grava arquivo e retorna False (anti-fantasma)."""

    def test_download_vazio_retorna_false_e_nao_grava(self):
        start = _resp({'name': 'operations/abc'})
        poll = _resp({'done': True, 'response': {'videoUri': 'https://v/out.mp4'}})
        download = _resp(b'')  # resposta vazia (ex.: página de erro de 0 byte)
        seq = [start, poll, download]

        with tempfile.TemporaryDirectory() as d:
            out = os.path.join(d, 'out.mp4')
            with mock.patch.object(Path, 'read_bytes', return_value=b'\x89PNG'), \
                 mock.patch.object(veo.urllib.request, 'urlopen',
                                   side_effect=lambda *a, **k: seq.pop(0)):
                result = veo.animate('img.png', 'p', out)

            self.assertFalse(result)
            # Nenhum arquivo-fantasma deve existir.
            self.assertFalse(os.path.exists(out))

        # Download vazio não é exceção → breaker não conta falha.
        self.assertEqual(cb.get_circuit_state('google_veo')['failures'], 0)


# ---------------------------------------------------------------------------
# urlopen SEMPRE chamado com timeout (anti-hang)
# ---------------------------------------------------------------------------

class TestUrlopenComTimeout(_IsolateCB, unittest.TestCase):
    """Toda chamada a urlopen (start, poll e download) passa timeout."""

    def test_todas_as_chamadas_de_urlopen_tem_timeout(self):
        start = _resp({'name': 'operations/abc'})
        poll = _resp({'done': True, 'response': {'videoUri': 'https://v/out.mp4'}})
        download = _resp(b'MP4DATA' * 50)
        seq = [start, poll, download]

        with tempfile.TemporaryDirectory() as d:
            out = os.path.join(d, 'out.mp4')
            with mock.patch.object(Path, 'read_bytes', return_value=b'\x89PNG'), \
                 mock.patch.object(veo.urllib.request, 'urlopen',
                                   side_effect=lambda *a, **k: seq.pop(0)) as m:
                veo.animate('img.png', 'p', out)

            # 3 chamadas: start, poll, download — todas com kwarg timeout.
            self.assertEqual(m.call_count, 3)
            for call in m.call_args_list:
                self.assertIn('timeout', call.kwargs)
                self.assertGreater(call.kwargs['timeout'], 0)


def urllib_error_urlerror(msg):
    """Helper: instancia urllib.error.URLError (erro de rede genérico que
    propaga direto, sem ser convertido em RuntimeError pelo except de HTTPError)."""
    import urllib.error
    return urllib.error.URLError(msg)


if __name__ == '__main__':
    unittest.main(verbosity=2)
