# -*- coding: utf-8 -*-
"""Testes da camada HTTP isolada (net.py): transitório x cliente, circuit + retry.
Sem rede real — urllib é mockado; estado do circuit isolado em temp."""
import io
import json
import os
import tempfile
import unittest
import urllib.error
from pathlib import Path
from unittest import mock

import circuit_breaker as cb
import net


class _Resp:
    """Resposta fake usável como context manager (with urlopen() as r)."""
    def __init__(self, body, status=200):
        self._b = body.encode('utf-8')
        self.status = status

    def read(self):
        return self._b

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False


class TestNet(unittest.TestCase):
    def setUp(self):
        fd, nome = tempfile.mkstemp(suffix='.json')
        os.close(fd)
        self._tmp = Path(nome)
        self._orig = cb._STATE_FILE
        cb._STATE_FILE = self._tmp  # isola o circuit do canal-state.json real

    def tearDown(self):
        cb._STATE_FILE = self._orig
        self._tmp.unlink(missing_ok=True)

    @mock.patch('net.urllib.request.urlopen')
    def test_sucesso_retorna_data(self, m):
        m.return_value = _Resp(json.dumps({'x': 1}), 200)
        r = net.request_json('http://x', api='a', base_s=0.001)
        self.assertTrue(r['ok'])
        self.assertEqual(r['data'], {'x': 1})
        self.assertEqual(cb.get_circuit_state('a')['state'], 'closed')

    @mock.patch('net.urllib.request.urlopen')
    def test_4xx_nao_derruba_o_circuit(self, m):
        m.side_effect = urllib.error.HTTPError('http://x', 400, 'bad', {}, io.BytesIO(b'ruim'))
        r = net.request_json('http://x', api='a', threshold=2, base_s=0.001)
        self.assertFalse(r['ok'])
        self.assertEqual(r['status'], 400)
        self.assertEqual(cb.get_circuit_state('a')['state'], 'closed')  # 4xx não conta

    @mock.patch('net.urllib.request.urlopen')
    def test_5xx_retenta_e_abre_o_circuit(self, m):
        m.side_effect = urllib.error.HTTPError('http://x', 503, 'down', {}, io.BytesIO(b'boom'))
        with self.assertRaises(net.TransientError):
            net.request_json('http://x', api='a', threshold=2, max_attempts=2, base_s=0.001)
        self.assertEqual(cb.get_circuit_state('a')['state'], 'open')  # transitório abre


if __name__ == '__main__':
    unittest.main()
