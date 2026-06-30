# -*- coding: utf-8 -*-
"""h_publicacoes.render — resumo do que JÁ saiu. Hermético: fixture em disco
temporário, METADADOS apontado via patch (sem rede, sem o JSON real do repo).
Prova: render devolve str não-vazia e reflete a contagem do fixture
(só status 'publico' conta; agendado/previsto não)."""
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]   # .../videos
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from _bot_handlers import h_publicacoes  # noqa: E402

# Fixture mínimo com a estrutura REAL: 3 publicadas (2 YT longo, 1 IG short),
# + 1 agendada (NÃO conta) + 1 previsto (NÃO conta).
FIXTURE = {
    "livros": [
        {"slug": "livro-a", "pecas": [
            {"tipo": "video", "rotulo": "Vídeo-resumo", "pubs": [
                {"rede": "YouTube", "status": "publico", "data": "2026-06-12", "id": "x"}]},
            {"tipo": "short", "rotulo": "Short 1", "pubs": [
                {"rede": "YouTube Shorts", "status": "agendado", "data": "2026-06-20"},
                {"rede": "Instagram", "status": "publico", "data": "2026-06-13", "id": "y"}]},
        ]},
        {"slug": "livro-b", "pecas": [
            {"tipo": "video", "rotulo": "Vídeo-resumo", "pubs": [
                {"rede": "YouTube", "status": "publico", "data": "2026-06-14", "id": "z"}]},
            {"tipo": "short", "rotulo": "Short prev", "pubs": [
                {"rede": "YouTube Shorts", "status": "previsto", "data": ""}]},
        ]},
    ]
}


class TestBotPublicacoes(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", delete=False, encoding="utf-8")
        json.dump(FIXTURE, self.tmp)
        self.tmp.close()
        self.patcher = mock.patch.object(
            h_publicacoes, "METADADOS", Path(self.tmp.name))
        self.patcher.start()

    def tearDown(self):
        self.patcher.stop()
        Path(self.tmp.name).unlink(missing_ok=True)

    def test_render_str_nao_vazia(self):
        out = h_publicacoes.render()
        self.assertIsInstance(out, str)
        self.assertTrue(out.strip())
        self.assertLessEqual(len(out), 3500)

    def test_reflete_contagem_do_fixture(self):
        out = h_publicacoes.render()
        # 3 publicadas no total (2 YT longo + 1 IG), 2 livros
        self.assertIn("3 peças no ar", out)
        self.assertIn("2 livros", out)
        # contagem por plataforma
        self.assertIn("YouTube (longo): 2", out)
        self.assertIn("Instagram: 1", out)
        # agendado/previsto NÃO entram (não há Shorts publicado no fixture)
        self.assertNotIn("YouTube Shorts:", out)

    def test_ultimas_ordenadas_por_data_desc(self):
        out = h_publicacoes.render()
        # a mais recente publicada é 2026-06-14 (livro-b)
        i14 = out.find("2026-06-14")
        i13 = out.find("2026-06-13")
        self.assertGreater(i14, -1)
        self.assertGreater(i13, -1)
        self.assertLess(i14, i13)  # 14 aparece antes de 13 (desc)

    def test_best_effort_arquivo_ausente_nao_levanta(self):
        with mock.patch.object(h_publicacoes, "METADADOS",
                               Path(self.tmp.name + ".naoexiste")):
            try:
                out = h_publicacoes.render()
            except Exception as e:
                self.fail(f"render levantou com arquivo ausente (deveria degradar): {e}")
            self.assertIsInstance(out, str)
            self.assertTrue(out.strip())


if __name__ == "__main__":
    unittest.main()
