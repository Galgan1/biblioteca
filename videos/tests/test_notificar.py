# -*- coding: utf-8 -*-
"""notificar.py — alerta Telegram best-effort: sem credencial não quebra; sucesso = ok:true;
falha de rede degrada. Hermético (sem rede/token real)."""
import sys
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]   # .../videos
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import notificar  # noqa: E402


class TestNotificar(unittest.TestCase):
    def test_sem_credencial_retorna_false_sem_levantar(self):
        with mock.patch.object(notificar, "_cred", return_value=""):
            try:
                self.assertFalse(notificar.notificar("x"))
            except Exception as e:
                self.fail(f"notificar levantou sem credencial (deveria degradar): {e}")

    def test_envia_com_credencial(self):
        resp = mock.MagicMock()
        resp.read.return_value = b'{"ok": true}'
        cm = mock.MagicMock()
        cm.__enter__.return_value = resp
        with mock.patch.object(notificar, "_cred", side_effect=["tok", "chat"]), \
             mock.patch.object(notificar.urllib.request, "urlopen", return_value=cm):
            self.assertTrue(notificar.notificar("alerta"))

    def test_falha_de_rede_retorna_false_sem_levantar(self):
        import urllib.error
        with mock.patch.object(notificar, "_cred", side_effect=["tok", "chat"]), \
             mock.patch.object(notificar.urllib.request, "urlopen",
                               side_effect=urllib.error.URLError("offline")):
            try:
                self.assertFalse(notificar.notificar("alerta"))
            except Exception as e:
                self.fail(f"notificar levantou em falha de rede (deveria degradar): {e}")


if __name__ == "__main__":
    unittest.main()
