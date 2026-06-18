# -*- coding: utf-8 -*-
"""Cinegrafista NORMAL — decisão de movimento e rota de fuga (parallax→Ken Burns).
Testa a DECISÃO pura e o GUARD do DepthFlow (não roda torch/GPU). Mesmo padrão
soberano do tts(): a produção nunca para por falta de uma dependência pesada."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]  # .../videos
sys.path.insert(0, str(ROOT))

try:
    import cinegrafista as cg
    _OK = True
except Exception:
    _OK = False


@unittest.skipUnless(_OK, 'cinegrafista indisponivel')
class TestTratamento(unittest.TestCase):
    def test_motion_pago_vence(self):
        self.assertEqual(cg.tratamento('normal', tem_imagem=True, motion_pago=True, depthflow_ok=True), 'motion')

    def test_normal_com_imagem_e_depthflow_usa_parallax(self):
        self.assertEqual(cg.tratamento('normal', tem_imagem=True, motion_pago=False, depthflow_ok=True), 'parallax')

    def test_normal_sem_depthflow_cai_para_ken_burns(self):
        self.assertEqual(cg.tratamento('normal', tem_imagem=True, motion_pago=False, depthflow_ok=False), 'ken_burns')

    def test_imagem_sem_motion_nem_parallax_e_ken_burns(self):
        # premium sem motion pago, com imagem: zoompan (parallax é da lane NORMAL grátis)
        self.assertEqual(cg.tratamento('premium', tem_imagem=True, motion_pago=False, depthflow_ok=True), 'ken_burns')

    def test_sem_imagem_e_slide_parado(self):
        self.assertEqual(cg.tratamento('normal', tem_imagem=False, motion_pago=False, depthflow_ok=False), 'still')


@unittest.skipUnless(_OK, 'cinegrafista indisponivel')
class TestGuard(unittest.TestCase):
    def test_disponivel_retorna_bool(self):
        self.assertIsInstance(cg.depthflow_disponivel(), bool)

    def test_parallax_retorna_false_sem_depthflow(self):
        orig = cg.depthflow_disponivel
        cg.depthflow_disponivel = lambda: False
        try:
            self.assertFalse(cg.parallax('qualquer.png', 'saida.mp4'))
        finally:
            cg.depthflow_disponivel = orig


@unittest.skipUnless(_OK, 'cinegrafista indisponivel')
class TestCmd(unittest.TestCase):
    def test_cmd_inclui_entrada_saida_e_duracao(self):
        cmd = cg._depthflow_cmd('cap.png', 'out.mp4', 6.0, 30)
        self.assertIn('cap.png', cmd)
        self.assertIn('out.mp4', cmd)
        self.assertTrue(any('6' in str(a) for a in cmd))   # duração presente


if __name__ == '__main__':
    unittest.main()
