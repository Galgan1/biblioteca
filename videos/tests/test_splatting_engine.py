# -*- coding: utf-8 -*-
"""Motor 3DGS (splatting_engine) — GEOMETRIA pura (sem GPU): intrínsecos, unprojeção,
look-at e init dos Gaussians. O render real (depth + gsplat + ffmpeg) é provado pelo
smoke na GPU. Akita: prova o que dá pra provar; isola o que não dá."""
import sys
import unittest
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]  # .../videos
sys.path.insert(0, str(ROOT))

import splatting_engine as se  # noqa: E402


class TestIntrinsecos(unittest.TestCase):
    def test_centro_e_foco(self):
        K = se.intrinsics(64, 48, fov_graus=60)
        self.assertEqual(K.shape, (3, 3))
        self.assertAlmostEqual(K[0, 2], 32.0)   # cx = w/2
        self.assertAlmostEqual(K[1, 2], 24.0)   # cy = h/2
        self.assertGreater(K[0, 0], 0)          # fx > 0


class TestUnproject(unittest.TestCase):
    def test_shape_e_centro(self):
        w, h = 8, 6
        K = se.intrinsics(w, h, fov_graus=60)
        depth = np.full((h, w), 2.0, dtype=np.float64)
        pts = se.unproject(depth, K)
        self.assertEqual(pts.shape, (h * w, 3))
        # pixel central deve ficar ~ no eixo óptico (x≈0,y≈0) à profundidade 2
        self.assertTrue(np.all(np.isclose(pts[:, 2], 2.0)))   # Z = profundidade
        cx_idx = (h // 2) * w + (w // 2)
        self.assertLess(abs(pts[cx_idx, 0]), 0.6)             # perto do eixo


class TestLookAt(unittest.TestCase):
    def test_4x4_ortonormal_e_mapeia_eye(self):
        eye = np.array([0.0, 0.0, 2.0])
        vm = se.look_at(eye, alvo=np.zeros(3))
        self.assertEqual(vm.shape, (4, 4))
        R = vm[:3, :3]
        self.assertTrue(np.allclose(R @ R.T, np.eye(3), atol=1e-6))   # rotação ortonormal
        # o eye deve mapear para a origem da câmera
        eh = vm @ np.array([*eye, 1.0])
        self.assertTrue(np.allclose(eh[:3], 0.0, atol=1e-6))


class TestInitGaussians(unittest.TestCase):
    def _dados(self, w=8, h=6):
        rgb = np.random.rand(h, w, 3).astype(np.float32)
        depth = np.random.rand(h, w).astype(np.float32) + 0.5
        K = se.intrinsics(w, h)
        return rgb, depth, K

    def test_campos_e_formas(self):
        rgb, depth, K = self._dados()
        g = se.init_gaussians(rgb, depth, K, stride=1)
        N = rgb.shape[0] * rgb.shape[1]
        self.assertEqual(g['means'].shape, (N, 3))
        self.assertEqual(g['colors'].shape, (N, 3))
        self.assertEqual(g['scales'].shape, (N, 3))
        self.assertEqual(g['quats'].shape, (N, 4))
        self.assertEqual(g['opacities'].shape, (N,))

    def test_cores_normalizadas_e_quats_unit(self):
        rgb, depth, K = self._dados()
        g = se.init_gaussians(rgb, depth, K, stride=1)
        self.assertTrue(np.all((g['colors'] >= 0) & (g['colors'] <= 1)))
        norms = np.linalg.norm(g['quats'], axis=1)
        self.assertTrue(np.allclose(norms, 1.0, atol=1e-5))
        self.assertTrue(np.all(g['scales'] > 0))

    def test_stride_reduz_a_nuvem(self):
        rgb, depth, K = self._dados(w=8, h=8)
        g1 = se.init_gaussians(rgb, depth, K, stride=1)
        g2 = se.init_gaussians(rgb, depth, K, stride=2)
        self.assertLess(g2['means'].shape[0], g1['means'].shape[0])


class TestCamadaDeFundo(unittest.TestCase):
    """Flash3D-style: camada(s) atrás preenchem a disocclusion (buracos pretos)."""
    def _dados(self, w=16, h=12):
        rgb = np.random.rand(h, w, 3).astype(np.float32)
        depth = (np.random.rand(h, w).astype(np.float32) + 0.5)   # 0.5..1.5
        return rgb, depth, se.intrinsics(w, h)

    def test_fundo_adiciona_gaussians(self):
        rgb, depth, K = self._dados()
        g0 = se.init_gaussians(rgb, depth, K, stride=2, com_fundo=False)
        g1 = se.init_gaussians(rgb, depth, K, stride=2, com_fundo=True)
        self.assertGreater(g1['means'].shape[0], g0['means'].shape[0])

    def test_fundo_fica_atras(self):
        # as gaussians do fundo devem estar mais LONGE que o objeto mais distante
        rgb, depth, K = self._dados()
        g0 = se.init_gaussians(rgb, depth, K, stride=2, com_fundo=False)
        g1 = se.init_gaussians(rgb, depth, K, stride=2, com_fundo=True)
        z_obj_max = g0['means'][:, 2].max()
        n_extra = g1['means'].shape[0] - g0['means'].shape[0]
        z_fundo = g1['means'][-n_extra:, 2]          # as últimas são o fundo
        self.assertTrue(np.all(z_fundo >= z_obj_max))

    def test_campos_consistentes_com_fundo(self):
        rgb, depth, K = self._dados()
        g = se.init_gaussians(rgb, depth, K, stride=2, com_fundo=True)
        n = g['means'].shape[0]
        self.assertEqual(g['colors'].shape, (n, 3))
        self.assertEqual(g['scales'].shape, (n, 3))
        self.assertEqual(g['quats'].shape, (n, 4))
        self.assertEqual(g['opacities'].shape, (n,))
        self.assertTrue(np.all((g['colors'] >= 0) & (g['colors'] <= 1)))


if __name__ == '__main__':
    unittest.main()
