# -*- coding: utf-8 -*-
"""Contratos do GERADOR CANÔNICO do site (`gerar_livro.py`, contrato inviolável nº4).

Antes deste arquivo o gerador do site tinha 0 cobertura: `python testar.py` passava
mesmo se TODAS as páginas saíssem erradas (gate cego no produto principal — A2_testes).
Aqui ficam os contratos das funções PURAS (entrada BOOK/CHAPTER → HTML esperado).

unittest.TestCase (não funções soltas estilo-pytest) p/ entrar no gate canônico
`python testar.py` (unittest discover) — senão o contrato fica invisível ao gate.
"""
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import gerar_livro as gl


# --- fixtures mínimas (um livro de 1 card / 1 capítulo) ---------------------
def _book():
    return {
        "slug": "livro-teste", "title": "Livro Teste", "author": "Autor Teste",
        "header_light": "LIVRO", "header_bold": "TESTE",
        "subtitle": "VISÃO GERAL", "intro": "Intro do livro.",
        "description": "Descrição do livro de teste.", "tags": ["t1", "t2"],
        "_n": 1,
    }


def _chapter(**extra):
    ch = {
        "slug": "ch01-abertura", "sub": "CAPÍTULO 1 — Abertura",
        "intro": "Intro do capítulo.",
        "cards": [{"ic": "book", "t": "Card A", "b": "Corpo do card A."}],
    }
    ch.update(extra)
    return ch


class TestCard(unittest.TestCase):
    def test_estrutura_basica(self):
        html = gl.card({"ic": "book", "t": "Meu Título", "b": "Meu corpo", "i": 3})
        self.assertIn('class="card animate-entrance"', html)
        self.assertIn('style="--i: 3"', html)          # ordem de entrada preservada
        self.assertIn('<h2 class="card-title">Meu Título</h2>', html)
        self.assertIn('<p class="card-body">Meu corpo</p>', html)
        self.assertIn('class="card-icon"', html)       # ícone de linha (estética da marca)

    def test_warn_vira_card_warning(self):
        html = gl.card({"ic": "book", "t": "T", "b": "B", "i": 1, "warn": True})
        self.assertIn("card-warning", html)

    def test_wide_vira_card_wide(self):
        html = gl.card({"ic": "book", "t": "T", "b": "B", "i": 1, "wide": True})
        self.assertIn("card-wide", html)

    def test_campos_opcionais(self):
        html = gl.card({"ic": "book", "t": "T", "b": "B", "i": 1,
                        "list": ["um", "dois"], "tip": "uma dica", "det": "<b>det</b>"})
        self.assertIn('class="content-list"', html)
        self.assertIn("<li>um</li>", html)
        self.assertIn('class="card-tip"', html)
        self.assertIn("uma dica", html)
        self.assertIn('class="card-details"', html)

    def test_sem_opcionais_nao_emite_listas(self):
        html = gl.card({"ic": "book", "t": "T", "b": "B", "i": 1})
        self.assertNotIn("content-list", html)
        self.assertNotIn("card-tip", html)
        self.assertNotIn("card-details", html)


class TestChapterPage(unittest.TestCase):
    def _gen(self, ch=None):
        ch = ch or _chapter()
        return gl.chapter_page(_book(), ch, "../livro-teste.html", "&larr; Visão Geral",
                               "ch02.html", "Próximo &rarr;")

    def test_contem_titulo_subtitulo_e_card(self):
        html = self._gen()
        self.assertIn("Livro Teste", html)               # título do livro
        self.assertIn("CAPÍTULO 1 — Abertura", html)      # subtítulo do capítulo
        self.assertIn("Card A", html)                     # card do capítulo
        self.assertIn("Autor Teste", html)

    def test_breadcrumb_e_css_relativo(self):
        html = self._gen()
        self.assertIn('class="crumbs"', html)
        self.assertIn("../index.html", html)              # volta p/ a estante
        self.assertIn('href="../assets/style.css"', html)  # CSS único compartilhado

    def test_navegacao_prev_next(self):
        html = self._gen()
        self.assertIn('href="../livro-teste.html"', html)
        self.assertIn("&larr; Visão Geral", html)
        self.assertIn('href="ch02.html"', html)
        self.assertIn("Próximo &rarr;", html)

    def test_lessons_quando_presentes(self):
        html = self._gen(_chapter(lessons_title="Lições", lessons=["Lição um", "Lição dois"]))
        self.assertIn('class="lessons-list"', html)
        self.assertIn('<h2 class="lessons-title">Lições</h2>', html)
        self.assertIn("<li>Lição um</li>", html)

    def test_sem_lessons_nao_emite_secao(self):
        html = self._gen()                                # _chapter() não tem lessons
        self.assertNotIn("lessons-list", html)

    # --- CONTRATO DRY (A4): script único compartilhado, não cópia por livro ---
    def test_script_compartilhado(self):
        html = self._gen()
        self.assertIn("../assets/script-livro.js", html)  # referência ao JS único
        self.assertNotIn('src="script.js"', html)         # nunca a cópia por-pasta


class TestOverviewPage(unittest.TestCase):
    def _gen(self):
        return gl.overview_page(_book(), [_chapter()])

    def test_contem_titulo_links_e_css(self):
        html = self._gen()
        self.assertIn("Livro Teste", html)
        self.assertIn("Aprofunde-se nos Capítulos", html)
        self.assertIn('href="livro-teste/ch01-abertura.html"', html)  # link p/ o capítulo
        self.assertIn('href="assets/style.css"', html)                # CSS único

    # --- CONTRATO DRY (A4): script único compartilhado, não cópia por livro ---
    def test_script_compartilhado(self):
        html = self._gen()
        self.assertIn("assets/script-livro.js", html)
        self.assertNotIn("livro-teste/script.js", html)   # nunca a cópia por-pasta


class TestUpdateBooksJson(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self._base_orig = gl.BASE
        gl.BASE = self._tmp.name
        # books.json pré-existente com OUTRO livro (a função não pode apagá-lo)
        with open(os.path.join(gl.BASE, "books.json"), "w", encoding="utf-8") as f:
            json.dump([{"id": "outro", "title": "Outro Livro"}], f)
        self.addCleanup(self._tmp.cleanup)
        self.addCleanup(lambda: setattr(gl, "BASE", self._base_orig))

    def _read(self):
        with open(os.path.join(gl.BASE, "books.json"), encoding="utf-8") as f:
            return json.load(f)

    def test_insere_e_preserva_existente(self):
        gl.update_books_json(_book())
        data = self._read()
        ids = {e["id"] for e in data}
        self.assertEqual(ids, {"outro", "livro-teste"})   # não apaga o que já existia
        entry = next(e for e in data if e["id"] == "livro-teste")
        self.assertEqual(entry["title"], "Livro Teste")
        self.assertEqual(entry["coverUrl"], "assets/livro-teste-capa.png")
        self.assertEqual(entry["url"], "livro-teste.html")

    def test_idempotente(self):
        gl.update_books_json(_book())
        gl.update_books_json(_book())                     # 2ª vez não duplica
        ids = [e["id"] for e in self._read()]
        self.assertEqual(ids.count("livro-teste"), 1)


if __name__ == "__main__":
    unittest.main()
