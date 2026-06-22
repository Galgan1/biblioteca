# -*- coding: utf-8 -*-
"""Testes do circuit breaker + retry. Estado isolado num arquivo temporario."""
import contextlib
import io
import os
import tempfile
import unittest
from pathlib import Path

import circuit_breaker as cb
from circuit_breaker import retry, circuit_breaker, CircuitOpenError, get_circuit_state


class TestRetry(unittest.TestCase):
    def test_sucesso_apos_falhas_transitorias(self):
        chamadas = {'n': 0}

        @retry(max_attempts=3, base_s=0.001, jitter=False)
        def f():
            chamadas['n'] += 1
            if chamadas['n'] < 3:
                raise ValueError('transitorio')
            return 'ok'

        self.assertEqual(f(), 'ok')
        self.assertEqual(chamadas['n'], 3)

    def test_esgota_tentativas_e_levanta(self):
        @retry(max_attempts=2, base_s=0.001, jitter=False)
        def f():
            raise ValueError('sempre falha')

        with self.assertRaises(ValueError):
            f()

    def test_circuit_open_nao_e_retentado(self):
        chamadas = {'n': 0}

        @retry(max_attempts=3, base_s=0.001, jitter=False)
        def f():
            chamadas['n'] += 1
            raise CircuitOpenError('aberto')

        with self.assertRaises(CircuitOpenError):
            f()
        self.assertEqual(chamadas['n'], 1)  # re-raise imediato, sem retentar


class TestCircuitBreaker(unittest.TestCase):
    def setUp(self):
        fd, nome = tempfile.mkstemp(suffix='.json')
        os.close(fd)
        self._tmp = Path(nome)
        self._orig = cb._STATE_FILE
        cb._STATE_FILE = self._tmp  # isola do canal-state.json real

    def tearDown(self):
        cb._STATE_FILE = self._orig
        self._tmp.unlink(missing_ok=True)

    def test_abre_apos_atingir_threshold(self):
        @circuit_breaker(api='t', threshold=2, timeout_s=300)
        def f():
            raise ValueError('falha')

        with self.assertRaises(ValueError):
            f()  # falha 1
        self.assertEqual(get_circuit_state('t')['state'], 'closed')
        with self.assertRaises(ValueError):
            f()  # falha 2 -> abre
        self.assertEqual(get_circuit_state('t')['state'], 'open')

    def test_open_levanta_circuitopenerror(self):
        @circuit_breaker(api='t', threshold=1, timeout_s=300)
        def f():
            raise ValueError('falha')

        with self.assertRaises(ValueError):
            f()  # abre
        with self.assertRaises(CircuitOpenError):
            f()  # ja aberto -> nem executa a funcao

    def test_half_open_sucesso_volta_a_fechar(self):
        estado = {'n': 0}

        @circuit_breaker(api='t', threshold=1, timeout_s=0)  # timeout 0 -> half_open imediato
        def f():
            estado['n'] += 1
            if estado['n'] == 1:
                raise ValueError('falha inicial')
            return 'ok'

        with self.assertRaises(ValueError):
            f()  # abre (opened_at = agora)
        self.assertEqual(f(), 'ok')  # half_open -> sucesso -> closed
        self.assertEqual(get_circuit_state('t')['state'], 'closed')


class TestLoadStateLeituraDefeituosa(unittest.TestCase):
    """Pior nº2 da auditoria A3: estado corrompido NÃO pode virar 'API saudável' calado —
    isso esquece um circuit OPEN (libera chamadas a uma API quebrada) e apaga last_error.
    Arquivo AUSENTE é legítimo (primeira execução) → {} silencioso."""

    def setUp(self):
        fd, nome = tempfile.mkstemp(suffix='.json')
        os.close(fd)
        self._tmp = Path(nome)
        self._orig = cb._STATE_FILE
        cb._STATE_FILE = self._tmp

    def tearDown(self):
        cb._STATE_FILE = self._orig
        self._tmp.unlink(missing_ok=True)

    def test_corrompido_avisa_nao_finge_saude(self):
        self._tmp.write_text('{ isto não é json válido', encoding='utf-8')
        err = io.StringIO()
        with contextlib.redirect_stderr(err):
            estado = cb._load_state()
        self.assertEqual(estado, {})                 # não tem como confiar no conteúdo
        self.assertNotEqual(err.getvalue().strip(), '')  # mas AVISA — não silencioso
        self.assertIn(str(self._tmp), err.getvalue())    # com contexto (qual arquivo)

    def test_ausente_e_silencioso(self):
        self._tmp.unlink(missing_ok=True)   # arquivo não existe → primeira execução legítima
        err = io.StringIO()
        with contextlib.redirect_stderr(err):
            estado = cb._load_state()
        self.assertEqual(estado, {})
        self.assertEqual(err.getvalue().strip(), '')  # ausência legítima não polui stderr


if __name__ == '__main__':
    unittest.main()
