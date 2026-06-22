# -*- coding: utf-8 -*-
"""upload_youtube._enviar — o upload resumável faz retry POR CHUNK (num_retries),
NÃO re-sobe o vídeo inteiro (re-upload total criaria DUPLICATA no canal). Hermético:
HttpRequest falso, sem rede/OAuth. Akita: verde = exit code."""
import contextlib
import io
import sys
import types
import unittest
from pathlib import Path
from unittest import mock

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


def _fake_module(name, **attrs):
    m = types.ModuleType(name)
    for k, v in attrs.items():
        setattr(m, k, v)
    return m


class TestRegistrarUploadNaoEngole(unittest.TestCase):
    """Pior nº1 da auditoria A3: o vídeo JÁ subiu (irreversível, gastou cota); se
    mark_done falha o pipeline ficava SEM saber que o vídeo existe → re-upload +
    video_id perdido. A falha NÃO pode ser silenciosa — tem de registrar o video_id."""

    def test_mark_done_falha_registra_video_id_no_stderr(self):
        def _explode(*a, **k):
            raise RuntimeError('state locado')
        fake_ps = _fake_module('pipeline_state', mark_done=_explode)
        fake_ct = _fake_module('cost_tracker', record_cost=lambda **k: 0.0)

        err = io.StringIO()
        with mock.patch.dict(sys.modules, {'pipeline_state': fake_ps, 'cost_tracker': fake_ct}), \
             contextlib.redirect_stderr(err):
            uy._registrar_upload('arte-da-guerra', 'VID123')   # NÃO pode levantar

        saida = err.getvalue()
        self.assertIn('VID123', saida)          # video_id preservado p/ reconciliação
        self.assertIn('arte-da-guerra', saida)  # com contexto (slug)
        self.assertNotEqual(saida.strip(), '')  # não silencioso

    def test_sucesso_grava_estado_e_custo_sem_ruido(self):
        chamado = {}
        def _mark(slug, stage, data=None):
            chamado['mark'] = (slug, stage, data)
        fake_ps = _fake_module('pipeline_state', mark_done=_mark)
        rec = mock.Mock(return_value=0.0)
        fake_ct = _fake_module('cost_tracker', record_cost=rec)

        err = io.StringIO()
        with mock.patch.dict(sys.modules, {'pipeline_state': fake_ps, 'cost_tracker': fake_ct}), \
             contextlib.redirect_stderr(err):
            uy._registrar_upload('arte-da-guerra', 'VID999')

        self.assertEqual(chamado['mark'], ('arte-da-guerra', 'uploaded', {'video_id': 'VID999'}))
        self.assertTrue(rec.called)
        self.assertEqual(err.getvalue().strip(), '')  # caminho feliz não polui stderr


if __name__ == '__main__':
    unittest.main()
