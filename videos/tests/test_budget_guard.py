# -*- coding: utf-8 -*-
"""Teto de gasto semanal — toda chamada paga consulta o orçamento ANTES de disparar.

Pior nº1 da auditoria A6 (CRÍTICO): `weekly_cost()` não tinha consumidor — `record_cost`
só contava DEPOIS. Aqui a catraca: `check_budget`/`budget_guard` ABORTAM com `BudgetExceeded`
antes de qualquer chamada de rede quando o gasto da semana estoura `WEEKLY_BUDGET_USD`.

O guard é o decorator MAIS EXTERNO (fora de @retry/@circuit_breaker) — um abort por
orçamento NÃO é falha de API e não pode tripar o breaker nem ser re-tentado.

Hermético: sem rede, sem custo real (weekly_cost mockado; env isolado). Akita: verde = exit code.
"""
import os
import sys
import unittest
from pathlib import Path
from unittest import mock

_VIDEOS = Path(__file__).resolve().parents[1]
if str(_VIDEOS) not in sys.path:
    sys.path.insert(0, str(_VIDEOS))

import cost_tracker as ct


class TestCheckBudget(unittest.TestCase):
    def test_acima_do_teto_levanta(self):
        with mock.patch.dict(os.environ, {'WEEKLY_BUDGET_USD': '10'}, clear=False), \
             mock.patch.object(ct, 'weekly_cost', return_value=12.0):
            with self.assertRaises(ct.BudgetExceeded):
                ct.check_budget(api='google_veo')

    def test_no_limite_levanta(self):
        # >= é estouro (gastar mais ultrapassaria o teto)
        with mock.patch.dict(os.environ, {'WEEKLY_BUDGET_USD': '10'}, clear=False), \
             mock.patch.object(ct, 'weekly_cost', return_value=10.0):
            with self.assertRaises(ct.BudgetExceeded):
                ct.check_budget(api='google_veo')

    def test_abaixo_do_teto_nao_levanta(self):
        with mock.patch.dict(os.environ, {'WEEKLY_BUDGET_USD': '10'}, clear=False), \
             mock.patch.object(ct, 'weekly_cost', return_value=3.0):
            ct.check_budget(api='google_veo')  # não levanta

    def test_env_ausente_inativo(self):
        # Sem WEEKLY_BUDGET_USD a catraca fica inativa (preserva comportamento atual /
        # rota soberana): nem com gasto altíssimo deve abortar.
        env = {k: v for k, v in os.environ.items() if k != 'WEEKLY_BUDGET_USD'}
        with mock.patch.dict(os.environ, env, clear=True), \
             mock.patch.object(ct, 'weekly_cost', return_value=9999.0):
            ct.check_budget(api='google_veo')  # não levanta

    def test_teto_zero_desativa(self):
        # Teto 0/negativo = desligado explicitamente (rota de fuga soberana).
        with mock.patch.dict(os.environ, {'WEEKLY_BUDGET_USD': '0'}, clear=False), \
             mock.patch.object(ct, 'weekly_cost', return_value=9999.0):
            ct.check_budget(api='google_veo')  # não levanta

    def test_mensagem_tem_contexto(self):
        # Akita pilar 9: erro com contexto (gasto, teto, api ofendida).
        with mock.patch.dict(os.environ, {'WEEKLY_BUDGET_USD': '10'}, clear=False), \
             mock.patch.object(ct, 'weekly_cost', return_value=12.5):
            try:
                ct.check_budget(api='google_veo')
                self.fail('deveria ter levantado BudgetExceeded')
            except ct.BudgetExceeded as e:
                msg = str(e)
                self.assertIn('12.5', msg)
                self.assertIn('10', msg)
                self.assertIn('google_veo', msg)


class TestBudgetGuardDecorator(unittest.TestCase):
    def test_aborta_antes_de_executar_a_funcao(self):
        chamou = {'n': 0}

        @ct.budget_guard(api='google_veo')
        def paga():
            chamou['n'] += 1
            return 'gastou'

        with mock.patch.dict(os.environ, {'WEEKLY_BUDGET_USD': '5'}, clear=False), \
             mock.patch.object(ct, 'weekly_cost', return_value=99.0):
            with self.assertRaises(ct.BudgetExceeded):
                paga()
        self.assertEqual(chamou['n'], 0)  # corpo da função paga NUNCA rodou

    def test_dentro_do_teto_executa_normal(self):
        @ct.budget_guard(api='google_veo')
        def paga():
            return 'ok'

        with mock.patch.dict(os.environ, {'WEEKLY_BUDGET_USD': '5'}, clear=False), \
             mock.patch.object(ct, 'weekly_cost', return_value=1.0):
            self.assertEqual(paga(), 'ok')


class TestImagenAbortaAntesDaRede(unittest.TestCase):
    """Integração: o cliente pago real (imagen) aborta ANTES de qualquer urlopen."""

    def test_acima_do_teto_nao_chama_urlopen(self):
        import imagen
        with mock.patch.dict(os.environ, {'WEEKLY_BUDGET_USD': '1'}, clear=False), \
             mock.patch.object(ct, 'weekly_cost', return_value=500.0), \
             mock.patch.object(imagen, 'KEY', 'FAKE'), \
             mock.patch.object(imagen.urllib.request, 'urlopen') as m_urlopen:
            with self.assertRaises(ct.BudgetExceeded):
                imagen.gen('prompt qualquer', '/tmp/_budget_test.png')
        m_urlopen.assert_not_called()  # nenhuma chamada paga disparada


if __name__ == '__main__':
    unittest.main(verbosity=2)
