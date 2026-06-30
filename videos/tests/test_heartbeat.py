# -*- coding: utf-8 -*-
"""heartbeat.pc_online — decisao PURA de vivacidade do PC local (T7).

Hermetico: injeta `caminho` (arquivo temp) + `agora` (relogio fixo) -> sem ssh,
sem relogio real. Fresco => True; velho/ausente/lixo => False (degrada soberano).
"""
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]   # .../videos
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import heartbeat  # noqa: E402


class TestPcOnline(unittest.TestCase):
    def setUp(self):
        self._dir = tempfile.TemporaryDirectory()
        self.hb = Path(self._dir.name) / "heartbeat.txt"
        self.addCleanup(self._dir.cleanup)

    def _escreve(self, texto):
        self.hb.write_text(texto, encoding="utf-8")

    def test_timestamp_fresco_online(self):
        agora = 1_000_000.0
        self._escreve(str(agora - 60))            # batida de 1 min atras
        self.assertTrue(heartbeat.pc_online(self.hb, agora=agora, max_idade_s=600))

    def test_timestamp_velho_offline(self):
        agora = 1_000_000.0
        self._escreve(str(agora - 1200))          # 20 min atras > 600s
        self.assertFalse(heartbeat.pc_online(self.hb, agora=agora, max_idade_s=600))

    def test_arquivo_ausente_offline(self):
        ausente = Path(self._dir.name) / "nao_existe.txt"
        self.assertFalse(heartbeat.pc_online(ausente, agora=1_000_000.0))

    def test_conteudo_lixo_offline(self):
        self._escreve("nao-sou-um-numero")
        self.assertFalse(heartbeat.pc_online(self.hb, agora=1_000_000.0))


if __name__ == "__main__":
    unittest.main()
