# -*- coding: utf-8 -*-
"""Guarda de roteiro — validação dura ANTES de gastar API, e AVISO quando o validador falta.

Pior nº2 da auditoria A6 (ALTO): `load_roteiro` ficava sob `try/except ImportError: pass`.
Sem pydantic/contracts a guarda paga SUMIA calada e o gasto rodava sem validação. Aqui:
se o validador faltar, AVISA explicitamente (Akita pilar 7 — guarda em silêncio é pior);
com o validador presente, a guarda continua DURA (roteiro inválido aborta).

Hermético: sem rede, sem API. Akita: verde = exit code.
"""
import contextlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

_VIDEOS = Path(__file__).resolve().parents[1]
if str(_VIDEOS) not in sys.path:
    sys.path.insert(0, str(_VIDEOS))

import gerar_video
import upload_youtube


def _roteiro(tmp, cenas=3, **extra):
    cfg = {
        'slug': 'x', 'titulo': 'X', 'autor': 'Y',
        'cenas': [{'titulo': f'c{i}', 'narracao': 'n'} for i in range(cenas)],
        **extra,
    }
    p = Path(tmp) / 'r.json'
    p.write_text(json.dumps(cfg), encoding='utf-8')
    return str(p)


class _GuardaCompartilhada:
    """Mesma bateria p/ os dois entrypoints donos de uma guarda de roteiro."""
    modulo = None  # subclasses definem

    def _validar(self, path):
        return self.modulo._validar_roteiro(path)

    def test_validador_ausente_avisa(self):
        with tempfile.TemporaryDirectory() as d:
            path = _roteiro(d)
            err = io.StringIO()
            # contracts indisponível: from contracts import ... → ImportError
            with mock.patch.dict(sys.modules, {'contracts': None}), \
                 contextlib.redirect_stderr(err):
                self._validar(path)   # não pode levantar — apenas avisar
            saida = err.getvalue()
            self.assertNotEqual(saida.strip(), '')      # NÃO silencioso
            self.assertIn('contracts', saida.lower())   # diz o que falta (com contexto)

    def test_validador_presente_roteiro_valido_nao_avisa(self):
        with tempfile.TemporaryDirectory() as d:
            path = _roteiro(d)
            err = io.StringIO()
            with contextlib.redirect_stderr(err):
                self._validar(path)
            self.assertEqual(err.getvalue().strip(), '')  # caminho feliz não polui stderr

    def test_validador_presente_roteiro_invalido_aborta(self):
        # Guarda DURA: < 3 cenas viola o contrato → ValueError/ValidationError.
        with tempfile.TemporaryDirectory() as d:
            path = _roteiro(d, cenas=2)
            with self.assertRaises(Exception):
                self._validar(path)


class TestGuardaGerarVideo(_GuardaCompartilhada, unittest.TestCase):
    modulo = gerar_video


class TestGuardaUploadYoutube(_GuardaCompartilhada, unittest.TestCase):
    modulo = upload_youtube


if __name__ == '__main__':
    unittest.main(verbosity=2)
