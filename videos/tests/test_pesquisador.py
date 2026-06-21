# -*- coding: utf-8 -*-
"""Pesquisador — geração e pontuação de ganchos (hooks). Tudo PURO, local, sem rede.
Akita: verde = exit code."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]  # .../videos
sys.path.insert(0, str(ROOT))

import pesquisador as pq  # noqa: E402 (import direto — falha real se não existir)


class TestGerarGanchos(unittest.TestCase):
    def test_uma_por_formula(self):
        gs = pq.gerar_ganchos('A Arte da Guerra', 'estratégia')
        self.assertEqual(len(gs), len(pq.FORMULAS))
        self.assertEqual({g['formula'] for g in gs}, set(pq.FORMULAS))

    def test_texto_menciona_livro_ou_conceito(self):
        gs = pq.gerar_ganchos('Hábitos Atômicos', 'hábitos')
        for g in gs:
            self.assertTrue('Hábitos Atômicos' in g['texto'] or 'hábitos' in g['texto'].lower(),
                            f"gancho sem livro/conceito: {g['texto']}")


class TestPontuar(unittest.TestCase):
    def test_curto_e_curioso_vence_longo_e_morno(self):
        bom = pq.pontuar_gancho('Por que quase ninguém entende isso?')
        ruim = pq.pontuar_gancho('Este texto é apenas uma descrição comum e bem longa '
                                 'que se arrasta sem qualquer curiosidade por muitas palavras')
        self.assertGreater(bom, ruim)

    def test_pontuacao_no_intervalo(self):
        s = pq.pontuar_gancho('Existe um segredo aqui.')
        self.assertGreaterEqual(s, 0.0)
        self.assertLessEqual(s, 1.0)


class TestMelhor(unittest.TestCase):
    def test_melhor_e_o_de_maior_pontuacao(self):
        m = pq.melhor_gancho('A Arte da Guerra', 'estratégia')
        gs = pq.gerar_ganchos('A Arte da Guerra', 'estratégia')
        melhor_score = max(pq.pontuar_gancho(g['texto']) for g in gs)
        self.assertAlmostEqual(pq.pontuar_gancho(m['texto']), melhor_score)


class TestDoRoteiro(unittest.TestCase):
    def test_extrai_titulo_e_conceito(self):
        cfg = {'titulo': 'Livro X', 'cenas': [
            {'tipo': 'abertura', 'titulo': 'Abertura'},
            {'tipo': 'conceito', 'titulo': 'A Grande Ideia'},
        ]}
        r = pq.do_roteiro(cfg)
        self.assertEqual(r['titulo'], 'Livro X')
        self.assertEqual(r['conceito'], 'A Grande Ideia')
        self.assertTrue(r['ganchos'] and r['melhor'])


if __name__ == '__main__':
    unittest.main()
