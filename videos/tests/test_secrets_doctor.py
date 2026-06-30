# -*- coding: utf-8 -*-
"""Contrato da taxonomia de erro do doutor de APIs (Akita pilar 9: erro com contexto).

A função pura classify(code) é o coração da disciplina: dado um HTTP status,
dizer SE o bloqueio é conta/billing, crédito, endpoint ou transitório — isso
evita horas caçando o problema errado (ex.: trocar de modelo quando era billing).
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import secrets_doctor as sd


class TestClassify(unittest.TestCase):
    def test_401_403_sao_conta(self):
        # auth/entitlement — trocar de modelo ou re-tentar NÃO resolve
        self.assertEqual(sd.classify(401), 'CONTA/BILLING/KEY')
        self.assertEqual(sd.classify(403), 'CONTA/BILLING/KEY')

    def test_402_e_credito(self):
        self.assertEqual(sd.classify(402), 'CRÉDITO')

    def test_404_e_endpoint(self):
        # nome de modelo mudou / rota errada — caso real do fal/nvidia
        self.assertEqual(sd.classify(404), 'ENDPOINT/MODELO')

    def test_429_e_5xx_sao_transitorios(self):
        # retry + circuit_breaker resolvem; não é erro de configuração
        for code in (408, 429, 500, 502, 503):
            self.assertEqual(sd.classify(code), 'TRANSITÓRIO')

    def test_status_desconhecido_e_explicito(self):
        # nunca engole em silêncio — devolve o código cru
        self.assertEqual(sd.classify(418), 'HTTP 418')


class TestPresenca(unittest.TestCase):
    def test_ausente_quando_arquivo_nao_existe(self):
        label, marca, det = sd.check_presenca('Fantasma', 'nao_existe_xyz.txt')
        self.assertEqual(marca, '•')
        self.assertEqual(det, 'ausente')


if __name__ == '__main__':
    unittest.main()
