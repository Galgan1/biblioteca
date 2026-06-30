"""Testa o handler de status geral do bot (videos/_bot_handlers/h_status.py).

Hermético: aponta TODOS os caminhos do handler para um tempdir de fixtures
(monkeypatch dos atributos de módulo). Sem rede. Prova o contrato best-effort:
render() devolve str não-vazia mesmo com TODAS as fontes ausentes.
"""
import json
import tempfile
import unittest
from pathlib import Path

from _bot_handlers import h_status


class TestBotStatus(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        base = Path(self._tmp.name)
        self._canal = base / "canal-state.json"
        self._pipe = base / "pipeline" / "state"
        self._books = base / "books.json"
        self._skills = base / "skills"
        self._tests_a = base / "tests"
        self._tests_b = base / "vtests"
        # guarda originais
        self._orig = {
            k: getattr(h_status, k)
            for k in ("_CANAL_STATE", "_PIPELINE_STATE_DIR", "_BOOKS",
                      "_SKILLS_DIR", "_TESTS_DIRS")
        }
        h_status._CANAL_STATE = self._canal
        h_status._PIPELINE_STATE_DIR = self._pipe
        h_status._BOOKS = self._books
        h_status._SKILLS_DIR = self._skills
        h_status._TESTS_DIRS = [self._tests_a, self._tests_b]

    def tearDown(self):
        for k, v in self._orig.items():
            setattr(h_status, k, v)
        self._tmp.cleanup()

    def _w(self, p: Path, obj):
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(obj, ensure_ascii=False), encoding="utf-8")

    # ----- contrato principal: best-effort com fontes ausentes -----
    def test_best_effort_tudo_ausente(self):
        # nada existe no tempdir -> NÃO pode levantar, str não-vazia
        out = h_status.render()
        self.assertIsInstance(out, str)
        self.assertTrue(out.strip())
        self.assertLessEqual(len(out), 3500)
        # blocos vazios viram "—", não derrubam
        self.assertIn("—", out)

    def test_panorama_completo(self):
        self._w(self._canal, {
            "channel_name": "Minuto Real",
            "lanes": {
                "biblioteca": {"status": "active"},
                "tiktok": {"status": "blocked", "reason": "token pendente"},
            },
            "api_health": {
                "google_tts": {"state": "closed", "failures": 0},
                "fal-avatar": {"state": "open", "failures": 2},
            },
            "upcoming_schedule": [
                {"slug": "sound-design", "longo_date": "2026-07-20"},
                {"slug": "audiovisao", "longo_date": "2026-07-23"},
            ],
            "pending_operations": {"bitcoin_short4": {"note": "x"}},
        })
        self._w(self._books, [{"id": "a"}, {"id": "b"}, {"id": "c"}])
        (self._skills / "akita").mkdir(parents=True)
        (self._skills / "biblioteca").mkdir(parents=True)
        (self._tests_a).mkdir(parents=True)
        (self._tests_a / "test_um.py").write_text("", encoding="utf-8")
        (self._tests_b).mkdir(parents=True)
        (self._tests_b / "test_dois.py").write_text("", encoding="utf-8")
        (self._pipe).mkdir(parents=True)
        (self._pipe / "sound-design.json").write_text("{}", encoding="utf-8")

        out = h_status.render()
        self.assertIsInstance(out, str)
        self.assertLessEqual(len(out), 3500)
        # lanes
        self.assertIn("biblioteca", out)
        self.assertIn("tiktok", out)
        self.assertIn("token pendente", out)
        # api aberta destacada
        self.assertIn("fal-avatar", out)
        # agenda
        self.assertIn("sound-design", out)
        # pipeline
        self.assertIn("sound-design", out)
        self.assertIn("bitcoin_short4", out)
        # contagens
        self.assertIn("3 livros", out)
        self.assertIn("2 skills", out)
        self.assertIn("2 testes", out)

    def test_canal_json_corrompido_nao_quebra(self):
        self._canal.parent.mkdir(parents=True, exist_ok=True)
        self._canal.write_text("{ nao eh json", encoding="utf-8")
        out = h_status.render()
        self.assertIsInstance(out, str)
        self.assertTrue(out.strip())

    def test_apis_todas_ok(self):
        self._w(self._canal, {
            "api_health": {
                "a": {"state": "closed"},
                "b": {"state": "closed"},
            },
        })
        out = h_status.render()
        self.assertIn("2 OK", out)


if __name__ == "__main__":
    unittest.main()
