# -*- coding: utf-8 -*-
"""Contrato inviolável: a YouTube API só fala com o canal Minuto Real.
Sem rede — usa um cliente falso (fluent) que devolve o id de canal configurado.
"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import canal_guard


class _FakeReq:
    def __init__(self, payload):
        self._payload = payload

    def execute(self):
        return self._payload


class _FakeChannels:
    def __init__(self, cid, com_item=True):
        self._cid = cid
        self._com_item = com_item

    def list(self, **_):
        if not self._com_item:
            return _FakeReq({'items': []})
        return _FakeReq({'items': [{'id': self._cid, 'snippet': {'title': 'X'}}]})


class _FakeYT:
    def __init__(self, cid, com_item=True):
        self._ch = _FakeChannels(cid, com_item)

    def channels(self):
        return self._ch


class TestCanalGuard(unittest.TestCase):
    def test_canal_certo_passa(self):
        ch = canal_guard.assert_canal(_FakeYT(canal_guard.CANAL_ID))
        self.assertEqual(ch['id'], canal_guard.CANAL_ID)

    def test_canal_pessoal_aborta(self):
        with self.assertRaises(canal_guard.CanalErrado):
            canal_guard.assert_canal(_FakeYT(canal_guard.PESSOAL_ID))

    def test_canal_desconhecido_aborta(self):
        with self.assertRaises(canal_guard.CanalErrado):
            canal_guard.assert_canal(_FakeYT('UCqualquer_outro_canal_aqui'))

    def test_sem_canal_aborta(self):
        with self.assertRaises(canal_guard.CanalErrado):
            canal_guard.assert_canal(_FakeYT(None, com_item=False))

    def test_pessoal_diferente_do_oficial(self):
        # sanidade: as duas constantes nunca podem coincidir
        self.assertNotEqual(canal_guard.CANAL_ID, canal_guard.PESSOAL_ID)


if __name__ == '__main__':
    unittest.main()
