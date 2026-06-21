# -*- coding: utf-8 -*-
"""Regressão do worker_upload.py — orquestrador do upload→skill→staging.

Herméticos: sem rede, sem `claude`, sem deploy. Verde = exit code (Akita pilar 2).
Cobre o que foi enviado em 21/jun sem teste: derivação de slug, a FRONTEIRA DE
SEGURANÇA (env sem credencial p/ o agente) e o resumo da revisão.
"""
import os
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "pdf-service"))
import worker_upload as W  # noqa: E402


class TestDerivarSlug(unittest.TestCase):
    def test_slug_explicito_vence(self):
        self.assertEqual(W._derivar_slug({"slug": "a-arte-da-guerra"}, "/x/job1"), "a-arte-da-guerra")

    def test_slug_do_nome_do_arquivo(self):
        self.assertEqual(W._derivar_slug({"file": "meu-livro.pdf"}, "/x/job1"), "meu-livro")

    def test_source_generico_cai_no_jobid(self):
        # source.<ext> não diz o nome do livro → usa o id do job (basename do dir)
        self.assertEqual(W._derivar_slug({"file": "source.epub"}, "/x/1782-abc"), "1782-abc")

    def test_sem_slug_e_sem_file_cai_no_jobid(self):
        # job sem slug e sem file (campo ausente) NÃO pode virar slug vazio (quebra o gate)
        self.assertEqual(W._derivar_slug({}, "/x/1782-abc"), "1782-abc")

    def test_slug_whitespace_e_file_none_cai_no_jobid(self):
        self.assertEqual(W._derivar_slug({"slug": "  ", "file": None}, "/x/1782-abc"), "1782-abc")


class TestFronteiraDeSeguranca(unittest.TestCase):
    """Akita pilar 8: NENHUMA credencial de deploy/git pode vazar p/ o `claude -p`."""

    def test_remove_todas_as_credenciais(self):
        for k in W.ENV_SENSIVEL:
            os.environ[k] = "segredo"
        try:
            env = W._env_agente()
            for k in W.ENV_SENSIVEL:
                self.assertNotIn(k, env, f"{k} deveria ter sido removido do env do agente")
        finally:
            for k in W.ENV_SENSIVEL:
                os.environ.pop(k, None)

    def test_preserva_variaveis_nao_sensiveis(self):
        os.environ["VAR_TESTE_NAO_SENSIVEL"] = "ok"
        try:
            self.assertEqual(W._env_agente().get("VAR_TESTE_NAO_SENSIVEL"), "ok")
        finally:
            os.environ.pop("VAR_TESTE_NAO_SENSIVEL", None)


class TestResumo(unittest.TestCase):
    def test_resumo_le_data_py_staged(self):
        with tempfile.TemporaryDirectory() as d:
            (Path(d) / "meu_livro_data.py").write_text(
                "BOOK={'title':'T','author':'A','cover':'c.png'}\n"
                "CHAPTERS=[{'slug':'ch1'},{'slug':'ch2'},{'slug':'ch3'}]\n",
                encoding="utf-8")
            old, W.BUILD_DIR = W.BUILD_DIR, d
            try:
                r = W._resumo("meu-livro")
            finally:
                W.BUILD_DIR = old
            self.assertEqual(r["title"], "T")
            self.assertEqual(r["author"], "A")
            self.assertEqual(r["chapters"], 3)
            self.assertTrue(r["cover"])

    def test_resumo_arquivo_ausente_devolve_erro(self):
        old, W.BUILD_DIR = W.BUILD_DIR, tempfile.gettempdir()
        try:
            self.assertIn("error", W._resumo("nao-existe-xyz-123"))
        finally:
            W.BUILD_DIR = old


if __name__ == "__main__":
    unittest.main()
