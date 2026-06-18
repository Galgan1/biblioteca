# -*- coding: utf-8 -*-
"""Cinegrafista 3D — 3D Gaussian Splatting local. Testa a DECISÃO, o GUARD e a
MATEMÁTICA da órbita de câmera (tudo puro, sem GPU). O render real (GPU) é
smoke-testado à parte. Akita: verde = exit code."""
import sys
import unittest
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]  # .../videos
sys.path.insert(0, str(ROOT))

import splatting as sp        # noqa: E402
import cinegrafista as cg     # noqa: E402


class TestDisponibilidade(unittest.TestCase):
    def test_disponivel_retorna_bool(self):
        self.assertIsInstance(sp.gaussian_disponivel(), bool)


class TestGuard(unittest.TestCase):
    def test_splat_clip_false_sem_motor(self):
        orig = sp.gaussian_disponivel
        sp.gaussian_disponivel = lambda: False
        try:
            self.assertFalse(sp.splat_clip('qualquer.png', 'saida.mp4'))
        finally:
            sp.gaussian_disponivel = orig


class TestOrbita(unittest.TestCase):
    def test_numero_de_poses(self):
        poses = sp.orbit_poses(n=48)
        self.assertEqual(poses.shape, (48, 3))

    def test_camera_mantem_raio_do_alvo(self):
        alvo = (0.0, 0.0, 0.0)
        poses = sp.orbit_poses(n=24, raio=2.5, alvo=alvo)
        dist = np.linalg.norm(poses - np.array(alvo), axis=1)
        self.assertTrue(np.allclose(dist, 2.5, atol=1e-6))

    def test_camera_realmente_se_move(self):
        poses = sp.orbit_poses(n=10, arco_graus=30)
        self.assertFalse(np.allclose(poses[0], poses[-1]))   # arco != ponto fixo


class TestDecisaoGaussian(unittest.TestCase):
    def test_gaussian_preferido_quando_disponivel(self):
        # com imagem e 3DGS disponível → 'gaussian' (melhor tratamento local)
        self.assertEqual(
            cg.tratamento('normal', tem_imagem=True, motion_pago=False,
                          depthflow_ok=True, gaussian_ok=True), 'gaussian')

    def test_motion_pago_ainda_vence_gaussian(self):
        self.assertEqual(
            cg.tratamento('premium', tem_imagem=True, motion_pago=True,
                          depthflow_ok=True, gaussian_ok=True), 'motion')

    def test_sem_gaussian_cai_para_parallax(self):
        self.assertEqual(
            cg.tratamento('normal', tem_imagem=True, motion_pago=False,
                          depthflow_ok=True, gaussian_ok=False), 'parallax')

    def test_gaussian_default_off_nao_muda_comportamento_antigo(self):
        # chamada antiga (4 args) segue idêntica — gaussian_ok default False
        self.assertEqual(
            cg.tratamento('normal', tem_imagem=True, motion_pago=False,
                          depthflow_ok=False), 'ken_burns')


if __name__ == '__main__':
    unittest.main()
