# -*- coding: utf-8 -*-
"""Diretor — plano cena-a-cena (shot list) com 4 campos por cena: texto/visual/voz/som.
Reusa cinegrafista p/ o tratamento visual. Tudo PURO/local. Akita: verde = exit code."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]  # .../videos
sys.path.insert(0, str(ROOT))

import diretor as dr  # noqa: E402


def _cenas():
    return [
        {'tipo': 'abertura', 'titulo': 'Gancho', 'narracao': 'Você lê errado.'},
        {'tipo': 'conceito', 'titulo': 'Ideia', 'img': 'a foggy plain', 'narracao': 'A ideia.'},
        {'tipo': 'conceito', 'titulo': 'Ação', 'img': 'a battle', 'motion': 'camera moves', 'narracao': 'Ação.'},
        {'tipo': 'encerramento', 'titulo': 'CTA', 'narracao': 'Próximo vídeo.'},
    ]


class TestShotList(unittest.TestCase):
    def test_quatro_campos_por_cena(self):
        sl = dr.montar_shot_list(_cenas(), modo='normal', depthflow_ok=False)
        self.assertEqual(len(sl), 4)
        for s in sl:
            for campo in ('texto', 'visual', 'voz', 'som'):
                self.assertIn(campo, s)
                self.assertTrue(s[campo], f'campo {campo} vazio em {s}')

    def test_visual_motion_quando_ha_motion(self):
        sl = dr.montar_shot_list(_cenas(), modo='normal', depthflow_ok=False)
        self.assertEqual(sl[2]['visual'], 'motion')   # cena com 'motion' pago

    def test_visual_parallax_com_depthflow(self):
        sl = dr.montar_shot_list(_cenas(), modo='normal', depthflow_ok=True)
        self.assertEqual(sl[1]['visual'], 'parallax')  # imagem + depthflow

    def test_visual_ken_burns_sem_depthflow(self):
        sl = dr.montar_shot_list(_cenas(), modo='normal', depthflow_ok=False)
        self.assertEqual(sl[1]['visual'], 'ken_burns')  # imagem, sem depthflow

    def test_visual_still_sem_imagem(self):
        sl = dr.montar_shot_list(_cenas(), modo='normal', depthflow_ok=True)
        self.assertEqual(sl[0]['visual'], 'still')     # abertura sem imagem

    def test_tom_de_voz_difere_por_tipo(self):
        sl = dr.montar_shot_list(_cenas(), modo='normal', depthflow_ok=False)
        self.assertNotEqual(sl[0]['voz'], sl[1]['voz'])  # abertura != conceito


class TestRitmo(unittest.TestCase):
    def test_avisa_cena_estatica(self):
        # uma cena 'conceito' sem imagem (slide chapado) = risco anti-slop
        cenas = [{'tipo': 'conceito', 'titulo': 'X', 'narracao': 'sem imagem'}]
        sl = dr.montar_shot_list(cenas, modo='normal', depthflow_ok=False)
        self.assertTrue(dr.revisar_ritmo(sl))


class TestDoRoteiro(unittest.TestCase):
    def test_shot_list_cobre_todas_as_cenas(self):
        cfg = {'slug': 't', 'titulo': 'T', 'cenas': _cenas()}
        r = dr.do_roteiro(cfg)
        self.assertEqual(len(r['shot_list']), len(_cenas()))


if __name__ == '__main__':
    unittest.main()
