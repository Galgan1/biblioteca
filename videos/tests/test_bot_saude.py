# -*- coding: utf-8 -*-
"""Testa o handler /saude do bot (videos/_bot_handlers/h_saude.py).

Hermético, SEM rede/subprocess real: monkeypatch de subprocess.run com a saída
fake do doctor. Prova os 2 casos do contrato — "tudo verde" e "1 circuito OPEN"
— e o fallback (doctor timeout → lê canal-state.json).
"""
import subprocess
import tempfile
import unittest
from pathlib import Path

from _bot_handlers import h_saude


# Saídas REAIS do doctor.py (mesmo formato do `python doctor.py`).
_VERDE = (
    "=== doctor - auditoria de saude do pipeline ===\n"
    "FALHAS: nenhuma\n"
    "\nSTATUS: OK (exit 0)\n"
)
_OPEN = (
    "=== doctor - auditoria de saude do pipeline ===\n"
    "FALHAS (1):\n"
    "  [FALHA] circuit OPEN: fal-avatar (2 falhas)\n"
    "AVISOS (1):\n"
    "  [aviso] bloqueado: smoke-test/video_built - teste: recurso indisponivel\n"
    "\nSTATUS: PROBLEMAS (exit 1)\n"
)


class _FakeRun:
    """Substitui subprocess.run: devolve um CompletedProcess com stdout/returncode
    fixos. Sem rede, sem processo real."""

    def __init__(self, stdout, returncode):
        self.stdout, self.returncode = stdout, returncode

    def __call__(self, *a, **k):
        return subprocess.CompletedProcess(
            args=a[0] if a else [], returncode=self.returncode,
            stdout=self.stdout, stderr="",
        )


class TestBotSaude(unittest.TestCase):
    def setUp(self):
        self._orig_run = subprocess.run

    def tearDown(self):
        subprocess.run = self._orig_run

    def test_tudo_verde(self):
        subprocess.run = _FakeRun(_VERDE, 0)
        out = h_saude.render()
        self.assertIsInstance(out, str)
        self.assertIn("✅", out)
        self.assertIn("tudo verde", out)
        self.assertNotIn("🔴", out)
        self.assertLessEqual(len(out), 3500)

    def test_um_circuito_open(self):
        subprocess.run = _FakeRun(_OPEN, 1)
        out = h_saude.render()
        self.assertIn("🔴", out)
        self.assertIn("PROBLEMAS", out)
        # a falha do doctor aparece traduzida
        self.assertIn("circuit OPEN: fal-avatar (2 falhas)", out)
        # o aviso vira ⚠️
        self.assertIn("⚠️", out)
        self.assertIn("bloqueado: smoke-test/video_built", out)
        self.assertLessEqual(len(out), 3500)

    def test_fallback_quando_doctor_timeout(self):
        # doctor estoura timeout -> render usa o canal-state direto
        def _boom(*a, **k):
            raise subprocess.TimeoutExpired(cmd="doctor.py", timeout=30)

        subprocess.run = _boom
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        state = Path(tmp.name) / "canal-state.json"
        state.write_text(
            '{"api_health": {"fal-avatar": {"state": "open", "failures": 3}, '
            '"google_tts": {"state": "closed", "failures": 0}}}',
            encoding="utf-8",
        )
        orig = h_saude.CANAL_STATE
        h_saude.CANAL_STATE = state
        self.addCleanup(lambda: setattr(h_saude, "CANAL_STATE", orig))

        out = h_saude.render()
        self.assertIn("canal-state", out)          # sinaliza o modo fallback
        self.assertIn("🔴", out)
        self.assertIn("circuit OPEN: fal-avatar (3 falhas)", out)


if __name__ == "__main__":
    unittest.main()
