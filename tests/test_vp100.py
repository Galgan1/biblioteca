# -*- coding: utf-8 -*-
"""TDD Akita (pilar nº1) — teste de funções puras de vp100.py.

Proveniência: vp100.py vive na RAIZ e tinha ZERO testes, apesar de lógica pura
crítica (formatação, ordenação topológica do DAG de fallback, custo). Este é o
primeiro teste da raiz; prova que dá para fechar "verde = exit code" na raiz.

Rodar (da raiz): python testar.py   (ou: python -m unittest discover -s tests -t .)
"""
import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VP100 = ROOT / "vp100.py"


def _carregar_vp100():
    """Importa vp100.py por caminho. Seguro: main() está sob if __name__."""
    spec = importlib.util.spec_from_file_location("vp100_sut", VP100)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


vp = _carregar_vp100()


class TestFmtTempo(unittest.TestCase):
    """fmt_tempo: segundos -> 'Ns' ou 'NmSSs'. Função pura, determinística."""

    def test_zero_segundos(self):
        self.assertEqual(vp.fmt_tempo(0), "0s")

    def test_abaixo_de_um_minuto(self):
        self.assertEqual(vp.fmt_tempo(59), "59s")

    def test_exatamente_um_minuto_zera_padding(self):
        # regressão: o resto precisa vir com zero à esquerda (00), não "0"
        self.assertEqual(vp.fmt_tempo(60), "1m00s")

    def test_minutos_e_segundos_com_padding(self):
        self.assertEqual(vp.fmt_tempo(125), "2m05s")

    def test_arredonda_float(self):
        # 89.6s -> 90s -> 1m30s (round, não truncamento)
        self.assertEqual(vp.fmt_tempo(89.6), "1m30s")


class TestCarregarDagTopo(unittest.TestCase):
    """A ordenação topológica do DAG de fallback é lógica pura crítica:
    nenhuma etapa pode vir antes de uma dependência dela."""

    def setUp(self):
        _, self._topo, self._groups = vp.carregar_dag()
        self.dag = vp.DEFAULT_DAG

    def test_inclui_todos_os_stages_sem_duplicar(self):
        ordem = self._topo(self.dag)
        self.assertEqual(set(ordem), set(self.dag))
        self.assertEqual(len(ordem), len(self.dag))

    def test_dependencia_vem_antes_do_dependente(self):
        ordem = self._topo(self.dag)
        pos = {s: i for i, s in enumerate(ordem)}
        for stage, deps in self.dag.items():
            for d in deps:
                self.assertLess(
                    pos[d], pos[stage],
                    f'"{d}" deveria vir antes de "{stage}"'
                )

    def test_skill_e_a_raiz_do_grafo(self):
        ordem = self._topo(self.dag)
        self.assertEqual(ordem[0], "skill")


class TestCustoEtapa(unittest.TestCase):
    """custo_etapa: soma preço*qtd das APIs de um stage. Pura sobre STEPS."""

    def test_stage_sem_custo_e_zero(self):
        self.assertEqual(vp.custo_etapa("skill", vp.DEFAULT_PRICES), 0.0)

    def test_stage_desconhecido_e_zero(self):
        self.assertEqual(vp.custo_etapa("inexistente", vp.DEFAULT_PRICES), 0.0)

    def test_video_built_soma_apis_corretamente(self):
        p = vp.DEFAULT_PRICES
        esperado = (
            p["google_tts_1k"] * 4
            + p["google_imagen"] * 8
            + p["google_veo_8s"] * 3
        )
        self.assertAlmostEqual(vp.custo_etapa("video_built", p), esperado)


if __name__ == "__main__":
    unittest.main()
