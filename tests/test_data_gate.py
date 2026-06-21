# -*- coding: utf-8 -*-
"""Regressão do data_gate.py — o PORTÃO de qualidade que decide o que vai ao ar.

É o firewall do publish autônomo (Akita pilar 2: sem verde, não publica). Herméticos:
sem rede, sem IA. Testa a régua do card direto (`_checar_card`) + a `revisar` ponta a
ponta com módulos temporários (BOOK/CHAPTERS + contagem de capítulos).
"""
import importlib
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "pdf-service"))
import data_gate as G  # noqa: E402


def card(**kw):
    base = {"ic": "key", "t": "Título", "b": "Corpo com <strong>chave</strong> aqui."}
    base.update(kw)
    return base


class TestReguaDoCard(unittest.TestCase):
    def test_card_valido_nao_acusa(self):
        m = []
        G._checar_card(card(), "x", m)
        self.assertEqual(m, [])

    def test_icone_fora_da_lista(self):
        m = []
        G._checar_card(card(ic="naoexiste"), "x", m)
        self.assertTrue(any("ic" in s for s in m))

    def test_emph_que_nao_e_substring(self):
        m = []
        G._checar_card(card(t="Abc", emph="Xyz"), "x", m)
        self.assertTrue(any("emph" in s for s in m))

    def test_emph_substring_exata_passa(self):
        m = []
        G._checar_card(card(t="A Regra de Ouro", emph="Regra"), "x", m)
        self.assertEqual(m, [])

    def test_emph_vazio_reprova(self):
        # emph="" é substring de qualquer t, mas não destaca nada → tem que reprovar
        m = []
        G._checar_card(card(emph=""), "x", m)
        self.assertTrue(any("emph" in s for s in m))

    def test_b_sem_nenhum_strong(self):
        m = []
        G._checar_card(card(b="Corpo sem destaque nenhum."), "x", m)
        self.assertTrue(any("strong" in s for s in m))

    def test_titulo_vazio(self):
        m = []
        G._checar_card(card(t=""), "x", m)
        self.assertTrue(any("'t'" in s for s in m))

    def test_card_que_nao_e_dict(self):
        m = []
        G._checar_card("não sou um dict", "x", m)
        self.assertTrue(any("dict" in s for s in m))


class TestRevisarPontaAPonta(unittest.TestCase):
    def _rodar(self, corpo, nome, slug):
        with tempfile.TemporaryDirectory() as d:
            (Path(d) / nome).write_text(corpo, encoding="utf-8")
            old, G.RAIZ = G.RAIZ, d
            sys.path.insert(0, d)
            importlib.invalidate_caches()
            try:
                return G.revisar(slug)
            finally:
                G.RAIZ = old
                if d in sys.path:
                    sys.path.remove(d)
                sys.modules.pop(slug.replace("-", "_") + "_data", None)

    def test_livro_bom_passa(self):
        corpo = (
            "_c={'ic':'key','t':'Título','b':'Corpo <strong>x</strong>.'}\n"
            "BOOK={'title':'T','author':'A','cover':'c.png','overview_cards':[_c]}\n"
            "CHAPTERS=[{'slug':'ch1','cards':[_c]},{'slug':'ch2','cards':[_c]},"
            "{'slug':'ch3','cards':[_c]}]\n"
        )
        self.assertEqual(self._rodar(corpo, "bom_livro_data.py", "bom-livro"), [])

    def test_menos_de_3_capitulos_reprova(self):
        corpo = (
            "_c={'ic':'key','t':'T','b':'B <strong>x</strong>.'}\n"
            "BOOK={'title':'T','author':'A','cover':'c','overview_cards':[_c]}\n"
            "CHAPTERS=[{'slug':'ch1','cards':[_c]}]\n"
        )
        motivos = self._rodar(corpo, "curto_data.py", "curto")
        self.assertTrue(any("CHAPTERS" in s for s in motivos))

    def test_capitulo_que_nao_e_dict_reprova(self):
        # um item solto (string) no meio de CHAPTERS não pode passar silencioso
        corpo = (
            "_c={'ic':'key','t':'T','b':'B <strong>x</strong>.'}\n"
            "BOOK={'title':'T','author':'A','cover':'c','overview_cards':[_c]}\n"
            "CHAPTERS=['introducao',{'slug':'ch1','cards':[_c]},"
            "{'slug':'ch2','cards':[_c]},{'slug':'ch3','cards':[_c]}]\n"
        )
        self.assertTrue(self._rodar(corpo, "capstr_data.py", "capstr"))

    def test_BOOK_sem_chave_obrigatoria_reprova(self):
        corpo = (
            "_c={'ic':'key','t':'T','b':'B <strong>x</strong>.'}\n"
            "BOOK={'title':'T','overview_cards':[_c]}\n"  # falta author/cover
            "CHAPTERS=[{'slug':'ch1','cards':[_c]},{'slug':'ch2','cards':[_c]},"
            "{'slug':'ch3','cards':[_c]}]\n"
        )
        motivos = self._rodar(corpo, "semautor_data.py", "semautor")
        self.assertTrue(any("author" in s or "cover" in s for s in motivos))


if __name__ == "__main__":
    unittest.main()
