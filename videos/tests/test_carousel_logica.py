# -*- coding: utf-8 -*-
"""Testes da lógica LIVRO (overview) × CAPÍTULO do carrossel (Akita).
Puros (operam nas strings HTML dos slides), sem render. Cobrem: fonte única
montar_slides, capa de série, CTA contextual, teto/clamp, _cap_num, densidade."""
import sys
import types
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]  # .../biblioteca
sys.path.insert(0, str(ROOT))

try:
    import gerar_carrossel as gc
    _OK = True
except Exception:
    _OK = False


def _book():
    return {'title': 'Livro Teste', 'author': 'Autor X',
            'header_light': 'LIVRO', 'header_bold': 'TESTE',
            'subtitle': 'VISÃO GERAL · UM TEMA QUALQUER', 'tags': ['a', 'b']}


def _card(t='Ideia', b='Corpo curto da ideia.'):
    return {'t': t, 'b': b}


def _cards(n):
    return [_card(f'Ideia {i}', f'Corpo da ideia {i}.') for i in range(1, n + 1)]


@unittest.skipUnless(_OK, 'gerar_carrossel indisponivel')
class TestMontarSlides(unittest.TestCase):
    def test_contagem_capa_conceitos_cta(self):
        sl = gc.montar_slides(_book(), _cards(3), ch=None, total_caps=9)
        self.assertEqual(len(sl), 5)  # capa + 3 + cta

    def test_teto_de_slides(self):
        sl = gc.montar_slides(_book(), _cards(12), ch=None, total_caps=9)
        self.assertEqual(len(sl), gc.MAX_CONCEITOS + 2)  # clamp -> 8 conceitos + 2

    def test_capa_de_capitulo_tem_selo_de_serie(self):
        ch = {'slug': 'ch03-titulo', 'sub': 'CAPÍTULO 3: O Título', 'cards': _cards(3)}
        sl = gc.montar_slides(_book(), ch['cards'], ch=ch, total_caps=9)
        self.assertIn('CAPÍTULO 3 DE 9', sl[0])

    def test_capa_de_livro_nao_tem_selo_de_serie(self):
        sl = gc.montar_slides(_book(), _cards(3), ch=None, total_caps=9)
        self.assertNotIn('DE 9', sl[0])

    def test_cta_capitulo_difere_do_livro(self):
        ch = {'slug': 'ch01-x', 'sub': 'CAPÍTULO 1: X', 'cards': _cards(3)}
        cta_livro = gc.montar_slides(_book(), _cards(3), ch=None, total_caps=9)[-1]
        cta_cap = gc.montar_slides(_book(), ch['cards'], ch=ch, total_caps=9)[-1]
        self.assertNotEqual(cta_livro, cta_cap)
        self.assertIn('só 1 capítulo', cta_cap)


@unittest.skipUnless(_OK, 'gerar_carrossel indisponivel')
class TestCapNum(unittest.TestCase):
    def test_do_sub(self):
        self.assertEqual(gc._cap_num({'sub': 'CAPÍTULO 7: Algo', 'slug': 'x'}), 7)

    def test_do_slug(self):
        self.assertEqual(gc._cap_num({'sub': '', 'slug': 'ch05-titulo'}), 5)

    def test_none(self):
        self.assertIsNone(gc._cap_num(None))


@unittest.skipUnless(_OK, 'gerar_carrossel indisponivel')
class TestOverviewFallback(unittest.TestCase):
    def test_fallback_para_capitulo_1(self):
        data = types.SimpleNamespace(CHAPTERS=[{'slug': 'ch01', 'cards': _cards(2)}])
        book = {'title': 'Sem Overview'}  # sem overview_cards
        self.assertEqual(gc._overview_cards(book, data), data.CHAPTERS[0]['cards'])

    def test_usa_overview_quando_existe(self):
        data = types.SimpleNamespace(CHAPTERS=[{'slug': 'ch01', 'cards': _cards(2)}])
        ovs = _cards(4)
        book = {'title': 'Com Overview', 'overview_cards': ovs}
        self.assertEqual(gc._overview_cards(book, data), ovs)


@unittest.skipUnless(_OK, 'gerar_carrossel indisponivel')
class TestDensidadeBillboard(unittest.TestCase):
    def test_overview_mais_curto_que_capitulo(self):
        longo = ' '.join(['palavra'] * 80) + '. Segunda frase tambem longa aqui. Terceira.'
        body_overview = gc._lead(longo, cap=160)
        body_capitulo = gc._lead(longo, cap=240)
        self.assertLessEqual(len(body_overview), len(body_capitulo))
        self.assertLess(len(body_overview), len(longo))


if __name__ == '__main__':
    unittest.main()
