# -*- coding: utf-8 -*-
"""Testes da camada de DSP premium `dsp.py` (Akita pilar 2 — verde = exit code).

Funções numpy PURAS, então 100% herméticas (sem rede, disco ou seed humano).
Cobre os contratos que uma regressão silenciosa quebraria sem alarme:
  - identidade quando o estágio está desligado (drive<=1, gain=0, amount=0);
  - reverb ADICIONA cauda (saída mais longa que a entrada);
  - master normaliza ao pico pedido e nunca produz NaN/inf;
  - convolução FFT tem o comprimento linear correto e bate com np.convolve.
"""
import unittest

import numpy as np

import dsp


def _sine(freq, dur=0.2, sr=dsp.SR):
    t = np.arange(int(sr * dur)) / sr
    return 0.5 * np.sin(2 * np.pi * freq * t)


class TestDSP(unittest.TestCase):
    def test_saturate_identidade_quando_drive_baixo(self):
        x = _sine(440)
        np.testing.assert_array_equal(dsp.saturate(x, 1.0), x)

    def test_saturate_limita_amplitude_e_finito(self):
        y = dsp.saturate(_sine(440) * 1.5, 3.0)
        self.assertLessEqual(float(np.max(np.abs(y))), 1.0 + 1e-9)
        self.assertTrue(np.all(np.isfinite(y)))

    def test_lowcut_atenua_grave_abaixo_do_corte(self):
        # 15 Hz = 3 ciclos exatos em 0.2s (fecha em ~0, sem borda no zero-pad do FFT).
        orig = _sine(15)
        y = dsp.lowcut(orig, fc=40)             # corte 40 Hz → 15 Hz fortemente atenuado
        self.assertEqual(len(y), len(orig))
        self.assertLess(float(np.max(np.abs(y))), 0.3 * float(np.max(np.abs(orig))))

    def test_lowcut_deixa_passar_o_agudo(self):
        x = _sine(2000)
        y = dsp.lowcut(x, fc=40)
        self.assertGreater(float(np.max(np.abs(y))), 0.4 * float(np.max(np.abs(x))))

    def test_highshelf_identidade_quando_gain_zero(self):
        x = _sine(1000)
        y = dsp.highshelf(x, fc=8000, gain_db=0)
        self.assertEqual(len(y), len(x))
        np.testing.assert_allclose(y, x, atol=1e-6)

    def test_reverb_zero_e_identidade(self):
        x = _sine(440)
        np.testing.assert_array_equal(dsp.reverb(x, amount=0.0), x)

    def test_reverb_adiciona_cauda(self):
        x = _sine(440, dur=0.1)
        y = dsp.reverb(x, amount=0.3, decay=0.5)
        self.assertGreater(len(y), len(x))      # cauda = saída mais longa
        self.assertTrue(np.all(np.isfinite(y)))

    def test_make_ir_normalizado(self):
        ir = dsp.make_ir(decay=1.0)
        self.assertAlmostEqual(float(np.max(np.abs(ir))), 1.0, places=5)

    def test_master_normaliza_ao_pico_pedido(self):
        y = dsp.master(_sine(220) * 0.3, peak=0.9)
        self.assertAlmostEqual(float(np.max(np.abs(y))), 0.9, places=4)
        self.assertTrue(np.all(np.isfinite(y)))

    def test_fftconv_comprimento_linear_bate_com_convolve(self):
        x = np.random.default_rng(0).standard_normal(1000)
        h = np.random.default_rng(1).standard_normal(64)
        y = dsp._fftconv(x, h)
        self.assertEqual(len(y), len(x) + len(h) - 1)
        np.testing.assert_allclose(y, np.convolve(x, h), atol=1e-6)


if __name__ == "__main__":
    unittest.main()
