# -*- coding: utf-8 -*-
"""Testes da logica pura do doctor (auditoria de saude). Sem tocar disco."""
import unittest

import doctor


class TestCircuits(unittest.TestCase):
    def test_open_eh_falha(self):
        f, a = doctor.checar_circuits({'imagen': {'state': 'open', 'failures': 3}})
        self.assertEqual(len(f), 1)
        self.assertEqual(a, [])
        self.assertIn('imagen', f[0])

    def test_half_open_eh_aviso(self):
        f, a = doctor.checar_circuits({'tts': {'state': 'half_open'}})
        self.assertEqual(f, [])
        self.assertEqual(len(a), 1)

    def test_closed_sem_problema(self):
        self.assertEqual(doctor.checar_circuits({'x': {'state': 'closed'}}), ([], []))

    def test_vazio(self):
        self.assertEqual(doctor.checar_circuits({}), ([], []))
        self.assertEqual(doctor.checar_circuits(None), ([], []))


class TestBlocked(unittest.TestCase):
    def test_blocked_vira_aviso(self):
        avisos = doctor.checar_blocked({
            's': {'tiktok': {'status': 'blocked', 'reason': 'sem token'},
                  'skill': {'status': 'done'}}})
        self.assertEqual(len(avisos), 1)
        self.assertIn('tiktok', avisos[0])
        self.assertIn('sem token', avisos[0])

    def test_done_nao_eh_aviso(self):
        self.assertEqual(doctor.checar_blocked({'s': {'skill': {'status': 'done'}}}), [])

    def test_vazio(self):
        self.assertEqual(doctor.checar_blocked({}), [])


class TestSecrets(unittest.TestCase):
    def test_ausente_vira_aviso(self):
        self.assertEqual(
            doctor.checar_secrets({'a.txt'}, {'a.txt', 'b.txt'}),
            ['secret ausente: b.txt'])

    def test_todos_presentes(self):
        self.assertEqual(doctor.checar_secrets({'a.txt', 'b.txt'}, {'a.txt'}), [])


class TestExitCode(unittest.TestCase):
    def test_sem_falha_zero(self):
        self.assertEqual(doctor.exit_code([]), 0)

    def test_com_falha_um(self):
        self.assertEqual(doctor.exit_code(['circuit OPEN: x']), 1)


if __name__ == '__main__':
    unittest.main()
