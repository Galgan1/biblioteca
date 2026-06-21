# -*- coding: utf-8 -*-
"""Testes da camada de efeitos de transição `efeitos_transicao.py` (Akita pilar 2).

Cobre apenas funções PURAS (numpy): `_curve` e `_knock`.
100% hermético — sem rede, disco, MP3 nem escrita de .wav.
Contratos verificados: arco Fibonacci, silêncio no clímax, swell de gain,
comprimento da curva e forma do sinal de knock.
"""
import sys
import unittest
from pathlib import Path

import numpy as np

# Garante que `videos/` está no path (rodado de dentro de `videos/` ou da raiz)
_VIDEOS = Path(__file__).parent.parent
if str(_VIDEOS) not in sys.path:
    sys.path.insert(0, str(_VIDEOS))

import efeitos_transicao as et


# --------------------------------------------------------------------------- #
# helpers                                                                      #
# --------------------------------------------------------------------------- #

_LEVELS = [1, 1, 2, 3, 5]   # cópia dos defaults do módulo


def _curva_padrao(n_trans=12, climax=8):
    """Retorna curva com os parâmetros padrão (SILENCE_AT_CLIMAX em vigor)."""
    return et._curve(n_trans, climax, _LEVELS, et.GAIN_MIN, et.GAIN_MAX)


# --------------------------------------------------------------------------- #
# _curve — contratos do arco Fibonacci                                         #
# --------------------------------------------------------------------------- #

class TestCurveComprimento(unittest.TestCase):
    """(d) len(curva) == n_trans para qualquer combinação razoável."""

    def test_comprimento_n_trans_tipico(self):
        curva = et._curve(10, 6, _LEVELS, 0.3, 0.9)
        self.assertEqual(len(curva), 10)

    def test_comprimento_n_trans_minimo(self):
        curva = et._curve(1, 0, _LEVELS, 0.3, 0.9)
        self.assertEqual(len(curva), 1)

    def test_comprimento_n_trans_grande(self):
        curva = et._curve(20, 14, _LEVELS, 0.3, 0.9)
        self.assertEqual(len(curva), 20)


class TestCurveSubidaFibonacci(unittest.TestCase):
    """(a) contagem de batidas na subida NÃO decresce — escada Fibonacci esticada."""

    def setUp(self):
        self._sac_orig = et.SILENCE_AT_CLIMAX
        et.SILENCE_AT_CLIMAX = True

    def tearDown(self):
        et.SILENCE_AT_CLIMAX = self._sac_orig

    def test_subida_nao_decrescente(self):
        # Doze transições, clímax na 8ª (0-base) — subida = índices 0..7
        curva = _curva_padrao(n_trans=12, climax=8)
        counts_subida = [c for c, _ in curva[:8]]
        for a, b in zip(counts_subida, counts_subida[1:]):
            self.assertLessEqual(a, b,
                msg=f"contagem decresceu: {counts_subida} — arco Fibonacci quebrado")

    def test_subida_primeiro_elemento_eh_minimo_da_escada(self):
        # O primeiro elemento da subida deve ser o menor valor de levels
        curva = _curva_padrao(n_trans=12, climax=8)
        count_primeiro, _ = curva[0]
        self.assertEqual(count_primeiro, min(_LEVELS))

    def test_subida_ultimo_antes_do_climax_eh_maximo_ou_cap(self):
        # O elemento imediatamente anterior ao clímax deve ser o máximo de levels
        curva = _curva_padrao(n_trans=12, climax=8)
        count_pre_climax, _ = curva[7]   # índice 7 = climax-1
        self.assertEqual(count_pre_climax, max(_LEVELS))


class TestCurveClimax(unittest.TestCase):
    """(b) virada do clímax: count == 0 com SILENCE_AT_CLIMAX=True, == max com False."""

    def setUp(self):
        self._sac_orig = et.SILENCE_AT_CLIMAX

    def tearDown(self):
        et.SILENCE_AT_CLIMAX = self._sac_orig

    def test_climax_count_zero_quando_silencio_ligado(self):
        et.SILENCE_AT_CLIMAX = True
        curva = et._curve(10, 6, _LEVELS, 0.3, 0.9)
        count_climax, _ = curva[6]
        self.assertEqual(count_climax, 0,
            "SILENCE_AT_CLIMAX=True: count no clímax deve ser 0")

    def test_climax_count_maximo_quando_silencio_desligado(self):
        et.SILENCE_AT_CLIMAX = False
        curva = et._curve(10, 6, _LEVELS, 0.3, 0.9)
        count_climax, _ = curva[6]
        self.assertEqual(count_climax, _LEVELS[-1],
            "SILENCE_AT_CLIMAX=False: count no clímax deve ser levels[-1]")

    def test_climax_gain_e_gmax(self):
        # Independentemente de SILENCE_AT_CLIMAX, gain no clímax == gmax
        for silencio in (True, False):
            et.SILENCE_AT_CLIMAX = silencio
            curva = et._curve(10, 6, _LEVELS, 0.3, 0.9)
            _, gain_climax = curva[6]
            self.assertAlmostEqual(gain_climax, 0.9, places=9,
                msg=f"gain no clímax deve ser gmax=0.9 (SILENCE={silencio})")


class TestCurveSwellDeGain(unittest.TestCase):
    """(c) gain sobe de gmin rumo a gmax durante a subida."""

    def setUp(self):
        self._sac_orig = et.SILENCE_AT_CLIMAX
        et.SILENCE_AT_CLIMAX = True

    def tearDown(self):
        et.SILENCE_AT_CLIMAX = self._sac_orig

    def test_gain_subida_nao_decrescente(self):
        curva = _curva_padrao(n_trans=12, climax=8)
        gains_subida = [g for _, g in curva[:8]]
        for a, b in zip(gains_subida, gains_subida[1:]):
            self.assertLessEqual(a - b, 1e-9,
                msg=f"gain decresceu na subida: {gains_subida}")

    def test_gain_primeiro_elemento_proximo_de_gmin(self):
        # Primeiro elemento: p=0/climax=0 → gp=0 → gain=gmin
        curva = et._curve(10, 6, _LEVELS, 0.3, 0.9)
        _, gain_0 = curva[0]
        self.assertAlmostEqual(gain_0, 0.3, places=9,
            msg="primeiro gain deve ser gmin")

    def test_gain_em_climax_menos_1_proximo_de_gmax(self):
        # Elemento climax-1: gp = (climax-1)/(climax-1) = 1.0 → gain=gmax
        curva = et._curve(10, 6, _LEVELS, 0.3, 0.9)
        _, gain_pre = curva[5]   # índice 5 = climax-1
        self.assertAlmostEqual(gain_pre, 0.9, places=9,
            msg="gain antes do clímax deve ser gmax")

    def test_gain_resolucao_e_resolve_gain(self):
        # Após o clímax, gain deve ser RESOLVE_GAIN
        curva = et._curve(10, 6, _LEVELS, 0.3, 0.9)
        for i in range(7, 10):   # índices 7, 8, 9 = resolução
            _, g = curva[i]
            self.assertAlmostEqual(g, et.RESOLVE_GAIN, places=9,
                msg=f"gain de resolução no índice {i} deve ser RESOLVE_GAIN")


class TestCurveCasoEdge(unittest.TestCase):
    """Casos de borda: climax=0 (sem subida), climax=n_trans-1 (sem resolução)."""

    def setUp(self):
        self._sac_orig = et.SILENCE_AT_CLIMAX
        et.SILENCE_AT_CLIMAX = True

    def tearDown(self):
        et.SILENCE_AT_CLIMAX = self._sac_orig

    def test_climax_zero_sem_subida(self):
        # Sem subida: índice 0 = clímax, count deve ser 0
        curva = et._curve(5, 0, _LEVELS, 0.3, 0.9)
        count_0, _ = curva[0]
        self.assertEqual(count_0, 0)

    def test_climax_igual_a_n_trans_menos_1_sem_resolucao(self):
        # Sem resolução: só subida + clímax, comprimento correto
        curva = et._curve(5, 4, _LEVELS, 0.3, 0.9)
        self.assertEqual(len(curva), 5)
        count_climax, _ = curva[4]
        self.assertEqual(count_climax, 0)


# --------------------------------------------------------------------------- #
# _knock — contratos do sinal de batida                                        #
# --------------------------------------------------------------------------- #

class TestKnock(unittest.TestCase):
    """_knock: retorna array finito, comprimento > 0, pico ≈ peak pedido."""

    def test_retorna_ndarray(self):
        sig = et._knock()
        self.assertIsInstance(sig, np.ndarray)

    def test_comprimento_maior_que_zero(self):
        sig = et._knock()
        self.assertGreater(len(sig), 0)

    def test_comprimento_corresponde_a_knock_dur(self):
        # Comprimento esperado: int(SR * KNOCK_DUR)
        esperado = int(et.SR * et.KNOCK_DUR)
        self.assertEqual(len(et._knock()), esperado)

    def test_finito_sem_nan(self):
        sig = et._knock(peak=0.55)
        self.assertTrue(np.all(np.isfinite(sig)),
            "sinal de knock contém NaN ou inf")

    def test_pico_aproximado_ao_peak_pedido(self):
        for peak in (0.3, 0.55, 0.8, 0.95):
            with self.subTest(peak=peak):
                sig = et._knock(peak=peak)
                pico = float(np.max(np.abs(sig)))
                self.assertAlmostEqual(pico, peak, delta=1e-6,
                    msg=f"pico {pico:.6f} diverge de peak={peak}")

    def test_peak_diferente_muda_amplitude(self):
        sig_low = et._knock(peak=0.3)
        sig_high = et._knock(peak=0.9)
        self.assertGreater(float(np.max(np.abs(sig_high))),
                           float(np.max(np.abs(sig_low))))

    def test_f0_diferente_nao_quebra_geracao(self):
        # Apenas verifica que a geração com f0 diferente não lança exceção e é finita
        for f0 in (55.0, 88.0, 110.0):
            with self.subTest(f0=f0):
                sig = et._knock(peak=0.5, f0=f0)
                self.assertTrue(np.all(np.isfinite(sig)))

    def test_sinal_nao_e_silencio(self):
        sig = et._knock(peak=0.5)
        self.assertGreater(float(np.max(np.abs(sig))), 0.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
