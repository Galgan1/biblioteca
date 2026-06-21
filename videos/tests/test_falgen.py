# -*- coding: utf-8 -*-
"""Testes herméticos de falgen.py — sem rede real, sem chave fal.ai.

fal_client é mockado no módulo falgen antes de qualquer chamada.
Estado do circuit breaker isolado em arquivo temporário (mesmo padrão
de test_circuit_breaker.py e test_net.py).

Nota sobre interação retry × breaker:
  A ordem de decoradores é @retry(externo) → @circuit_breaker(interno).
  Cada tentativa do retry chega ao breaker como chamada independente.
  Com max_attempts=3 e threshold=3, UMA chamada a gen() com erro
  permanente já abre o circuit (3 tentativas = 3 incrementos de failure).
  Com max_attempts=2 e threshold=2, igualmente 1 chamada já abre.
"""
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

# Garante que o diretório videos/ está no sys.path para importar falgen
_VIDEOS = Path(__file__).resolve().parent.parent
if str(_VIDEOS) not in sys.path:
    sys.path.insert(0, str(_VIDEOS))

# Precisamos de circuit_breaker antes de importar falgen para poder
# redirecionar _STATE_FILE para o arquivo temporário.
import circuit_breaker as cb

# Impede a leitura da chave real ao importar falgen (arquivo pode não existir).
# Cria um módulo stub de fal_client se ainda não existir no sys.modules.
_fal_stub = mock.MagicMock()
sys.modules.setdefault('fal_client', _fal_stub)

# cost_tracker também pode não existir em ambientes de CI mínimos
_cost_stub = mock.MagicMock()
sys.modules.setdefault('cost_tracker', _cost_stub)

import falgen  # noqa: E402 — importado após os stubs


class _IsolateCB:
    """Mixin: redireciona cb._STATE_FILE para temp e restaura no tearDown.
    Também mocka time.sleep para eliminar espera real do backoff de retry."""

    def setUp(self):
        fd, nome = tempfile.mkstemp(suffix='.json')
        os.close(fd)
        self._tmp = Path(nome)
        self._orig_state = cb._STATE_FILE
        cb._STATE_FILE = self._tmp
        # Elimina o backoff real — testes devem ser rápidos
        self._sleep_patch = mock.patch('circuit_breaker.time.sleep')
        self._sleep_patch.start()

    def tearDown(self):
        self._sleep_patch.stop()
        cb._STATE_FILE = self._orig_state
        self._tmp.unlink(missing_ok=True)


# ---------------------------------------------------------------------------
# gen() — Flux image
# ---------------------------------------------------------------------------

class TestGenSucesso(_IsolateCB, unittest.TestCase):
    """gen() bem-sucedido retorna IMG_MODEL e chama _record_cost."""

    def test_retorna_model_e_registra_custo(self):
        img_url = 'https://cdn.fal.ai/out.png'
        fake_res = {'images': [{'url': img_url}]}

        with mock.patch.object(falgen, 'fal_client') as m_fal, \
             mock.patch.object(falgen, '_download') as m_dl, \
             mock.patch.object(falgen, '_record_cost') as m_cost:
            m_fal.subscribe.return_value = fake_res
            result = falgen.gen('teste prompt', '/tmp/out.png')

        self.assertEqual(result, falgen.IMG_MODEL)
        m_dl.assert_called_once_with(img_url, '/tmp/out.png')
        m_cost.assert_called_once_with(api='fal-flux')
        # Circuit deve continuar fechado após sucesso
        self.assertEqual(cb.get_circuit_state('fal-flux')['state'], 'closed')

    def test_resposta_sem_url_retorna_none_sem_abrir_breaker(self):
        """Resposta malformada (sem URL) retorna None — não é exceção de rede,
        portanto NÃO deve incrementar falhas no circuit breaker."""
        with mock.patch.object(falgen, 'fal_client') as m_fal, \
             mock.patch.object(falgen, '_download'), \
             mock.patch.object(falgen, '_record_cost'):
            m_fal.subscribe.return_value = {'images': []}
            result = falgen.gen('teste', '/tmp/x.png')

        self.assertIsNone(result)
        # Retorno None não lança exceção, logo o breaker não conta falha
        self.assertEqual(cb.get_circuit_state('fal-flux')['failures'], 0)


class TestGenRetryEBreaker(_IsolateCB, unittest.TestCase):
    """gen() com exceções de rede: retry tenta N vezes e breaker abre."""

    def test_retry_tenta_3_vezes_antes_de_falhar(self):
        chamadas = {'n': 0}

        def subscribe_falha(*args, **kwargs):
            chamadas['n'] += 1
            raise RuntimeError('timeout de rede')

        with mock.patch.object(falgen, 'fal_client') as m_fal:
            m_fal.subscribe.side_effect = subscribe_falha
            with self.assertRaises(RuntimeError):
                falgen.gen('teste', '/tmp/x.png')

        # @retry(max_attempts=3): exatamente 3 tentativas
        self.assertEqual(chamadas['n'], 3)

    def test_breaker_abre_apos_threshold_de_falhas(self):
        """Uma chamada a gen() com erro permanente e max_attempts=3 gera
        3 falhas consecutivas no breaker (threshold=3) → circuit OPEN."""
        with mock.patch.object(falgen, 'fal_client') as m_fal:
            m_fal.subscribe.side_effect = RuntimeError('erro permanente')
            with self.assertRaises(RuntimeError):
                falgen.gen('teste', '/tmp/x.png')

        self.assertEqual(cb.get_circuit_state('fal-flux')['state'], 'open')

    def test_circuit_aberto_levanta_circuitopenerror(self):
        """Quando o circuit está OPEN, gen() levanta CircuitOpenError sem chamar fal_client."""
        from circuit_breaker import CircuitOpenError

        with mock.patch.object(falgen, 'fal_client') as m_fal:
            m_fal.subscribe.side_effect = RuntimeError('erro')
            # Abre o circuit (1 chamada com 3 tentativas = threshold atingido)
            with self.assertRaises(RuntimeError):
                falgen.gen('teste', '/tmp/x.png')

        chamadas_antes = falgen.fal_client.subscribe.call_count

        # Próxima chamada deve falhar com CircuitOpenError sem chamar fal_client
        with self.assertRaises(CircuitOpenError):
            falgen.gen('teste', '/tmp/x.png')

        # fal_client.subscribe NÃO foi chamado nesta tentativa extra
        self.assertEqual(falgen.fal_client.subscribe.call_count, chamadas_antes)


# ---------------------------------------------------------------------------
# animate() — Kling video
# ---------------------------------------------------------------------------

class TestAnimateSucesso(_IsolateCB, unittest.TestCase):
    """animate() bem-sucedido retorna True e chama _record_cost."""

    def test_retorna_true_e_registra_custo(self):
        vid_url = 'https://cdn.fal.ai/out.mp4'
        fake_res = {'video': {'url': vid_url}}

        with mock.patch.object(falgen, 'fal_client') as m_fal, \
             mock.patch.object(falgen, '_download') as m_dl, \
             mock.patch.object(falgen, '_record_cost') as m_cost:
            m_fal.upload_file.return_value = 'https://storage.fal.ai/img.png'
            m_fal.subscribe.return_value = fake_res
            result = falgen.animate('/tmp/img.png', 'movimento lento', '/tmp/out.mp4')

        self.assertTrue(result)
        m_dl.assert_called_once_with(vid_url, '/tmp/out.mp4')
        m_cost.assert_called_once_with(api='fal-kling')
        self.assertEqual(cb.get_circuit_state('fal-kling')['state'], 'closed')

    def test_resposta_sem_url_retorna_false_sem_abrir_breaker(self):
        """Resposta malformada retorna False — não dispara o circuit breaker."""
        with mock.patch.object(falgen, 'fal_client') as m_fal, \
             mock.patch.object(falgen, '_download'), \
             mock.patch.object(falgen, '_record_cost'):
            m_fal.upload_file.return_value = 'https://storage.fal.ai/img.png'
            m_fal.subscribe.return_value = {'video': {}}
            result = falgen.animate('/tmp/img.png', 'p', '/tmp/out.mp4')

        self.assertFalse(result)
        self.assertEqual(cb.get_circuit_state('fal-kling')['failures'], 0)


class TestAnimateRetryEBreaker(_IsolateCB, unittest.TestCase):
    """animate() com exceções de rede: retry tenta N vezes e breaker abre."""

    def test_retry_tenta_2_vezes_antes_de_falhar(self):
        chamadas = {'n': 0}

        def upload_falha(*args, **kwargs):
            chamadas['n'] += 1
            raise RuntimeError('upload falhou')

        with mock.patch.object(falgen, 'fal_client') as m_fal:
            m_fal.upload_file.side_effect = upload_falha
            with self.assertRaises(RuntimeError):
                falgen.animate('/tmp/img.png', 'p', '/tmp/out.mp4')

        # @retry(max_attempts=2): exatamente 2 tentativas
        self.assertEqual(chamadas['n'], 2)

    def test_breaker_abre_apos_threshold_de_falhas(self):
        """Uma chamada a animate() com erro permanente e max_attempts=2 gera
        2 falhas consecutivas no breaker (threshold=2) → circuit OPEN."""
        with mock.patch.object(falgen, 'fal_client') as m_fal:
            m_fal.upload_file.side_effect = RuntimeError('erro upload')
            with self.assertRaises(RuntimeError):
                falgen.animate('/tmp/img.png', 'p', '/tmp/out.mp4')

        self.assertEqual(cb.get_circuit_state('fal-kling')['state'], 'open')

    def test_circuit_aberto_nao_chama_fal_client(self):
        """Circuit OPEN em fal-kling levanta CircuitOpenError sem tocar fal_client."""
        from circuit_breaker import CircuitOpenError

        with mock.patch.object(falgen, 'fal_client') as m_fal:
            m_fal.upload_file.side_effect = RuntimeError('erro')
            # Abre o circuit (1 chamada com 2 tentativas = threshold atingido)
            with self.assertRaises(RuntimeError):
                falgen.animate('/tmp/img.png', 'p', '/tmp/out.mp4')

        chamadas_antes = falgen.fal_client.upload_file.call_count

        with self.assertRaises(CircuitOpenError):
            falgen.animate('/tmp/img.png', 'p', '/tmp/out.mp4')

        self.assertEqual(falgen.fal_client.upload_file.call_count, chamadas_antes)


if __name__ == '__main__':
    unittest.main(verbosity=2)
