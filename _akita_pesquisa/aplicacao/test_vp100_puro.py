# -*- coding: utf-8 -*-
"""TDD Akita (pilar nº1) — teste de REPRODUÇÃO de funções puras de vp100.py.

Por que este arquivo existe (proveniência):
  vp100.py vive na RAIZ do projeto e tinha ZERO testes, apesar de conter
  lógica pura crítica (formatação, ordenação topológica do DAG de fallback,
  cálculo de custo). Este é o PRIMEIRO artefato de TDD para a raiz — prova
  que dá para fechar o ciclo "verde = exit code" sem tocar produção.

Akita: "Verde = exit code de teste, não opinião de IA." Roda por comando único,
output parseável (unittest), sem setup humano. Vive em _akita_pesquisa/ (fora
da produção) por enquanto; ao consolidar a etapa, migra para uma pasta tests/.

Como rodar (da raiz do projeto):
  python -m unittest _akita_pesquisa.aplicacao.test_vp100_puro
  # exit 0 = verde; exit != 0 = quebrou (não consolide)
"""
import importlib.util
import unittest
from pathlib import Path

# vp100.py está na raiz do projeto (3 níveis acima deste arquivo).
ROOT = Path(__file__).resolve().parents[2]
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
        # carregar_dag devolve o real (videos/dag.py) se existir, senão o
        # fallback. Para um teste determinístico da LÓGICA, exercitamos o
        # algoritmo de fallback diretamente sobre o DEFAULT_DAG conhecido.
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
        # 'skill' não tem dependências -> sempre o primeiro stage pronto
        ordem = self._topo(self.dag)
        self.assertEqual(ordem[0], "skill")


class TestCustoEtapa(unittest.TestCase):
    """custo_etapa: soma preço*qtd das APIs de um stage. Pura sobre STEPS."""

    def test_stage_sem_custo_e_zero(self):
        # 'skill' não tem dict de custo -> US$ 0,00
        self.assertEqual(vp.custo_etapa("skill", vp.DEFAULT_PRICES), 0.0)

    def test_stage_desconhecido_e_zero(self):
        self.assertEqual(vp.custo_etapa("inexistente", vp.DEFAULT_PRICES), 0.0)

    def test_video_built_soma_apis_corretamente(self):
        # video_built: tts_1k*4 + imagen*8 + veo_8s*3, com DEFAULT_PRICES
        p = vp.DEFAULT_PRICES
        esperado = (
            p["google_tts_1k"] * 4
            + p["google_imagen"] * 8
            + p["google_veo_8s"] * 3
        )
        self.assertAlmostEqual(vp.custo_etapa("video_built", p), esperado)


if __name__ == "__main__":
    unittest.main()
