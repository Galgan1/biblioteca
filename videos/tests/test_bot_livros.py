"""Testa o handler /livros do bot (videos/_bot_handlers/h_livros.py).

Hermético: escreve um books.json de fixture num tempdir e aponta o handler
para ele (monkeypatch de h_livros._BOOKS). Sem rede.
"""
import json
import tempfile
import unittest
from pathlib import Path

from _bot_handlers import h_livros


def _fixture(n):
    return [
        {
            "id": f"livro-{i}",
            "title": f"Título {i}",
            "author": f"Autor {i}",
            "progress": "9 Capítulos" if i % 2 else "8 Movimentos",
            "url": f"livro-{i}.html",
        }
        for i in range(n)
    ]


class TestBotLivros(unittest.TestCase):
    def setUp(self):
        self._orig = h_livros._BOOKS
        self._tmp = tempfile.TemporaryDirectory()
        self._path = Path(self._tmp.name) / "books.json"
        h_livros._BOOKS = self._path

    def tearDown(self):
        h_livros._BOOKS = self._orig
        self._tmp.cleanup()

    def _escreve(self, dados):
        self._path.write_text(
            json.dumps(dados, ensure_ascii=False), encoding="utf-8"
        )

    def test_str_nao_vazia_e_conta_certo(self):
        self._escreve(_fixture(103))
        out = h_livros.render()
        self.assertIsInstance(out, str)
        self.assertTrue(out.strip())
        # total correto
        self.assertIn("103 livros", out)
        # contagem por status confere: i in 0..102 -> 52 pares ("8 Movimentos"),
        # 51 ímpares ("9 Capítulos")
        self.assertIn("8 Movimentos: 52", out)
        self.assertIn("9 Capítulos: 51", out)
        # trunca a lista em 25 e avisa o resto
        self.assertIn("Primeiros 25", out)
        self.assertIn("...e mais 78", out)
        # respeita o teto do Telegram
        self.assertLessEqual(len(out), 3500)

    def test_acervo_pequeno_sem_mais(self):
        self._escreve(_fixture(3))
        out = h_livros.render()
        self.assertIn("3 livros", out)
        self.assertNotIn("...e mais", out)

    def test_best_effort_arquivo_ausente(self):
        # _path não existe -> não pode levantar exceção
        out = h_livros.render()
        self.assertIsInstance(out, str)
        self.assertTrue(out.strip())

    def test_lista_vazia(self):
        self._escreve([])
        out = h_livros.render()
        self.assertIsInstance(out, str)
        self.assertTrue(out.strip())


if __name__ == "__main__":
    unittest.main()
