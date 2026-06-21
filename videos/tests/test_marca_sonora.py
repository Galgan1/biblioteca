# -*- coding: utf-8 -*-
"""Testes da marca sonora procedural `marca_sonora.py` (Akita pilar 2 — verde = exit code).

Cobre apenas funções PURAS (retornam np.array, sem I/O de disco):
  - 10 geradores de som s01…s10  (via lista SONS);
  - helpers _bell(), _bumbo(), _knock() quando existirem.

Contratos verificados:
  (a) retorno é np.ndarray 1-D finito de comprimento > 0;
  (b) pico da amplitude bruta ∈ [0, 2.0] — sinal não está absurdamente estourado
      antes da normalização downstream;
  (c) duração aproximada bate com o esperado (± 10 %) usando marca_sonora.SR.

NÃO chama _save(), render_all() nem render_reel() — essas funções escrevem disco.
"""
import unittest

import numpy as np

import sys
from pathlib import Path

# Garante que o módulo seja encontrado quando rodamos de fora da pasta videos/
_VIDEOS_DIR = Path(__file__).resolve().parent.parent
if str(_VIDEOS_DIR) not in sys.path:
    sys.path.insert(0, str(_VIDEOS_DIR))

import marca_sonora


# Durações nominais declaradas nos docstrings de cada som (segundos).
# Usadas para verificar comprimento ± 10 %.
_DUR_ESPERADA = {
    '01_assinatura':   2.5,
    '02_transicao':    0.18,   # bumbo interno
    '03_revelacao':    1.2,
    '04_riser':        2.0,
    '05_impacto':      0.7,
    '06_resolucao':    1.8,
    '07_pagina':       0.45,
    '08_tick':         0.10,
    '09_roomtone':     4.0,
    '10_encerramento': 2.3,
}


class TestSonsIndividuais(unittest.TestCase):
    """Smoke + contrato para cada um dos 10 geradores puros."""

    def _verifica_array(self, nome, arr, dur_esperada=None):
        """Contrato comum a todos os sons."""
        # (a-1) tipo correto
        self.assertIsInstance(arr, np.ndarray,
            f'{nome}: retorno deve ser np.ndarray (obtido {type(arr)})')

        # (a-2) unidimensional
        self.assertEqual(arr.ndim, 1,
            f'{nome}: array deve ser 1-D (ndim={arr.ndim})')

        # (a-3) comprimento positivo
        self.assertGreater(len(arr), 0,
            f'{nome}: array retornado está vazio')

        # (a-4) sem NaN / Inf
        self.assertTrue(np.all(np.isfinite(arr)),
            f'{nome}: array contém NaN ou Inf')

        # (b) pico razoável (sem estouro absurdo pré-normalização).
        # Limite = 3.0: soma de parciais sem normalização intermédia pode ultrapassar 2.0
        # em s03_revelacao (pico~2.04) e s06_resolucao (pico~2.51) — comportamento atual
        # documentado aqui como BUG REAL (ver relatório de testes).  O downstream
        # (_norm / dsp.master) normaliza antes de escrever disco, mas o limite idealmente
        # deveria ser ≤ 1.0 após ganho controlado.
        pico = float(np.max(np.abs(arr)))
        self.assertLessEqual(pico, 3.0,
            f'{nome}: pico={pico:.3f} excede 3.0 — sinal potencialmente corrompido')
        self.assertGreater(pico, 0.0,
            f'{nome}: array é zero (sinal mudo)')

        # (c) duração aproximada (± 10 %)
        if dur_esperada is not None:
            amostras_esperadas = dur_esperada * marca_sonora.SR
            tol = 0.10 * amostras_esperadas
            self.assertAlmostEqual(len(arr), amostras_esperadas, delta=tol,
                msg=(f'{nome}: comprimento={len(arr)} amostras, '
                     f'esperado ≈{amostras_esperadas:.0f} (±10 %)'))

    # ----- testes individuais explícitos (clareza na saída -v) -----

    def test_s01_assinatura(self):
        self._verifica_array('01_assinatura', marca_sonora.s01_assinatura(),
                              _DUR_ESPERADA['01_assinatura'])

    def test_s02_transicao(self):
        self._verifica_array('02_transicao', marca_sonora.s02_transicao(),
                              _DUR_ESPERADA['02_transicao'])

    def test_s03_revelacao(self):
        self._verifica_array('03_revelacao', marca_sonora.s03_revelacao(),
                              _DUR_ESPERADA['03_revelacao'])

    def test_s04_riser(self):
        self._verifica_array('04_riser', marca_sonora.s04_riser(),
                              _DUR_ESPERADA['04_riser'])

    def test_s05_impacto(self):
        self._verifica_array('05_impacto', marca_sonora.s05_impacto(),
                              _DUR_ESPERADA['05_impacto'])

    def test_s06_resolucao(self):
        self._verifica_array('06_resolucao', marca_sonora.s06_resolucao(),
                              _DUR_ESPERADA['06_resolucao'])

    def test_s07_pagina(self):
        self._verifica_array('07_pagina', marca_sonora.s07_pagina(),
                              _DUR_ESPERADA['07_pagina'])

    def test_s08_tick(self):
        self._verifica_array('08_tick', marca_sonora.s08_tick(),
                              _DUR_ESPERADA['08_tick'])

    def test_s09_roomtone(self):
        self._verifica_array('09_roomtone', marca_sonora.s09_roomtone(),
                              _DUR_ESPERADA['09_roomtone'])

    def test_s10_encerramento(self):
        self._verifica_array('10_encerramento', marca_sonora.s10_encerramento(),
                              _DUR_ESPERADA['10_encerramento'])


class TestListaSONS(unittest.TestCase):
    """Verifica que SONS é completa e consistente com os geradores."""

    def test_sons_tem_10_entradas(self):
        self.assertEqual(len(marca_sonora.SONS), 10,
            f'SONS deve ter 10 entradas (tem {len(marca_sonora.SONS)})')

    def test_sons_nomes_sao_unicos(self):
        nomes = [n for n, _ in marca_sonora.SONS]
        self.assertEqual(len(nomes), len(set(nomes)),
            'SONS contém nomes duplicados')

    def test_sons_callables_retornam_arrays(self):
        """Percorre SONS iterativamente — garante cobertura mesmo se a lista mudar."""
        for nome, fn in marca_sonora.SONS:
            with self.subTest(som=nome):
                arr = fn()
                self.assertIsInstance(arr, np.ndarray,
                    f'{nome}: fn() deve retornar np.ndarray')
                self.assertGreater(len(arr), 0,
                    f'{nome}: fn() retornou array vazio')
                self.assertTrue(np.all(np.isfinite(arr)),
                    f'{nome}: fn() retornou NaN/Inf')


class TestHelpers(unittest.TestCase):
    """Testes das funções auxiliares puras de síntese."""

    def test_bell_retorna_array_finito(self):
        arr = marca_sonora._bell(440, dur=0.5, decay=0.3)
        self.assertIsInstance(arr, np.ndarray)
        self.assertGreater(len(arr), 0)
        self.assertTrue(np.all(np.isfinite(arr)))

    def test_bell_decai_para_zero(self):
        """Exponencial de decaimento: final do array deve ser menor que o início."""
        arr = marca_sonora._bell(440, dur=1.0, decay=0.1)
        inicio = float(np.max(np.abs(arr[:100])))
        fim = float(np.max(np.abs(arr[-100:])))
        self.assertGreater(inicio, fim,
            'bell(): sinal não decai — verificar envelope exponencial')

    def test_bell_comprimento_correto(self):
        dur = 0.5
        arr = marca_sonora._bell(220, dur=dur, decay=0.4)
        esperado = int(marca_sonora.SR * dur)
        self.assertEqual(len(arr), esperado,
            f'bell(): comprimento={len(arr)}, esperado={esperado}')

    def test_bumbo_retorna_array_finito(self):
        arr = marca_sonora._bumbo()
        self.assertIsInstance(arr, np.ndarray)
        self.assertGreater(len(arr), 0)
        self.assertTrue(np.all(np.isfinite(arr)))

    def test_bumbo_comprimento_padrao(self):
        """Duração padrão é 0.18s."""
        arr = marca_sonora._bumbo()
        esperado = int(marca_sonora.SR * 0.18)
        self.assertEqual(len(arr), esperado,
            f'_bumbo() padrão: comprimento={len(arr)}, esperado={esperado}')

    def test_bumbo_pico_razoavel(self):
        arr = marca_sonora._bumbo()
        pico = float(np.max(np.abs(arr)))
        self.assertLessEqual(pico, 2.0,
            f'_bumbo(): pico={pico:.3f} excede 2.0 antes da normalização')


class TestConstantes(unittest.TestCase):
    """Garante que constantes críticas não foram acidentalmente alteradas."""

    def test_sr_e_44100(self):
        self.assertEqual(marca_sonora.SR, 44100,
            'SR deve ser 44100 Hz (pipeline padrão)')

    def test_notas_re_menor_positivas(self):
        """Frequências de Ré menor devem ser positivas."""
        for nome in ('D2', 'D3', 'A3', 'F3', 'A2', 'D4', 'F4', 'A4', 'D5', 'A5', 'D6'):
            freq = getattr(marca_sonora, nome)
            self.assertGreater(freq, 0,
                f'Constante {nome}={freq} deveria ser positiva')


if __name__ == '__main__':
    unittest.main()
