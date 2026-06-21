# -*- coding: utf-8 -*-
"""Testes do rastreador de estado da pipeline. Estado isolado em pasta temporaria."""
import shutil
import tempfile
import threading
import unittest
from pathlib import Path

import pipeline_state as ps


class TestPipelineState(unittest.TestCase):
    def setUp(self):
        self._tmp = Path(tempfile.mkdtemp())
        self._od, self._oe = ps.STATE_DIR, ps.EVENTS_FILE
        ps.STATE_DIR = self._tmp / 'state'
        ps.EVENTS_FILE = self._tmp / 'events.jsonl'

    def tearDown(self):
        ps.STATE_DIR, ps.EVENTS_FILE = self._od, self._oe
        shutil.rmtree(self._tmp, ignore_errors=True)

    def test_mark_done_e_is_done(self):
        self.assertFalse(ps.is_done('s', 'skill'))
        ps.mark_done('s', 'skill')
        self.assertTrue(ps.is_done('s', 'skill'))

    def test_get_state_inexistente_vazio(self):
        self.assertEqual(ps.get_state('nao-existe'), {})

    def test_dados_sao_persistidos(self):
        ps.mark_done('s', 'uploaded', data={'video_id': 'abc'})
        self.assertEqual(ps.get_state('s')['uploaded']['data']['video_id'], 'abc')

    def test_pending_exclui_o_que_esta_done(self):
        ps.mark_done('s', 'skill')
        self.assertNotIn('skill', ps.pending_stages('s'))
        self.assertIn('uploaded', ps.pending_stages('s'))

    def test_blocked_nao_conta_como_done(self):
        ps.mark_blocked('s', 'tiktok', 'sem token')
        self.assertFalse(ps.is_done('s', 'tiktok'))
        self.assertEqual(ps.get_state('s')['tiktok']['status'], 'blocked')

    def test_total_cost_soma(self):
        ps.mark_done('s', 'video_built', cost_usd=0.10)
        ps.mark_done('s', 'uploaded', cost_usd=0.05)
        self.assertAlmostEqual(ps.total_cost('s'), 0.15)

    def test_escritas_concorrentes_no_mesmo_slug_nao_se_perdem(self):
        def worker(stage):
            ps.mark_done('s', stage)

        threads = [threading.Thread(target=worker, args=(f'stg{i}',))
                   for i in range(8)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        st = ps.get_state('s')
        for i in range(8):
            self.assertEqual(st[f'stg{i}']['status'], 'done',
                             f'stg{i} perdida na concorrencia')


if __name__ == '__main__':
    unittest.main()
