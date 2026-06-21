# -*- coding: utf-8 -*-
"""Testes do DAG do pipeline (ordem topologica, prontos, grupos paralelos)."""
import unittest

from dag import DAG, topological_sort, ready_stages, parallel_groups


class TestTopologicalSort(unittest.TestCase):
    def test_inclui_todos_os_stages(self):
        order = topological_sort(DAG)
        self.assertEqual(set(order), set(DAG))
        self.assertEqual(len(order), len(DAG))  # sem duplicatas

    def test_dependencia_vem_antes_do_dependente(self):
        order = topological_sort(DAG)
        pos = {s: i for i, s in enumerate(order)}
        for stage, deps in DAG.items():
            for d in deps:
                self.assertLess(pos[d], pos[stage],
                                f'{d} deveria vir antes de {stage}')


class TestReadyStages(unittest.TestCase):
    def test_no_inicio_so_skill_esta_pronto(self):
        self.assertEqual(ready_stages(DAG, set()), ['skill'])

    def test_apos_skill_liberam_os_dependentes_diretos(self):
        self.assertEqual(set(ready_stages(DAG, {'skill'})),
                         {'biblioteca', 'video_built', 'instagram'})

    def test_nao_repete_stage_ja_feito(self):
        self.assertNotIn('skill', ready_stages(DAG, {'skill'}))


class TestParallelGroups(unittest.TestCase):
    def test_primeiro_grupo_eh_skill(self):
        self.assertEqual(parallel_groups(DAG)[0], {'skill'})

    def test_grupos_cobrem_todos_os_stages(self):
        union = set().union(*parallel_groups(DAG))
        self.assertEqual(union, set(DAG))

    def test_nenhum_stage_antes_de_sua_dependencia(self):
        groups = parallel_groups(DAG)
        nivel = {}
        for i, g in enumerate(groups):
            for s in g:
                nivel[s] = i
        for stage, deps in DAG.items():
            for d in deps:
                self.assertLess(nivel[d], nivel[stage])


if __name__ == '__main__':
    unittest.main()
