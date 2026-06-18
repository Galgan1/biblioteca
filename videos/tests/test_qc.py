# -*- coding: utf-8 -*-
"""QC — Gate 2 executável (rúbrica de 4 estágios). Estágios PUROS, testáveis sem
render: técnico, conteúdo (pt-PT bloqueante), compliance (afiliado só produto).
Akita: verde = exit code; na dúvida o verificador reprova."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]  # .../videos
sys.path.insert(0, str(ROOT))

import qc  # noqa: E402  (import direto — falha real se o módulo não existir)


class TestPtPt(unittest.TestCase):
    def test_marcadores_pt_pt_detectados(self):
        m = qc.detectar_pt_pt('O utilizador abriu o ecrã no telemóvel.')
        self.assertIn('utilizador', m)
        self.assertIn('ecrã', m)

    def test_ortografia_pre_acordo(self):
        self.assertIn('facto', qc.detectar_pt_pt('Isto é um facto comprovado.'))
        self.assertIn('acção', qc.detectar_pt_pt('A acção decisiva.'))

    def test_texto_pt_br_limpo(self):
        self.assertEqual(qc.detectar_pt_pt('O usuário abriu a tela no celular.'), [])


class TestConteudo(unittest.TestCase):
    def _cenas(self, **kw):
        base = [
            {'tipo': 'abertura', 'narracao': 'Você lê esse livro errado.'},
            {'tipo': 'conceito', 'narracao': 'A ideia central é simples e poderosa.'},
            {'tipo': 'encerramento', 'narracao': 'Siga para o próximo insight.'},
        ]
        return kw.get('cenas', base)

    def test_pt_pt_bloqueia(self):
        cenas = self._cenas()
        cenas[1]['narracao'] = 'O utilizador entende o facto.'
        falhas, _ = qc.avaliar_conteudo(cenas)
        self.assertTrue(falhas)

    def test_sem_abertura_bloqueia(self):
        cenas = [{'tipo': 'conceito', 'narracao': 'Sem gancho.'}]
        falhas, _ = qc.avaliar_conteudo(cenas)
        self.assertTrue(falhas)

    def test_br_limpo_passa(self):
        falhas, _ = qc.avaliar_conteudo(self._cenas())
        self.assertEqual(falhas, [])


class TestTecnico(unittest.TestCase):
    def test_full_hd_no_alvo_passa(self):
        falhas, _ = qc.avaliar_tecnico(1920, 1080, -14.1, -1.3)
        self.assertEqual(falhas, [])

    def test_resolucao_baixa_bloqueia(self):
        falhas, _ = qc.avaliar_tecnico(1280, 720, -14.0, -1.5)
        self.assertTrue(falhas)

    def test_true_peak_clipando_bloqueia(self):
        falhas, _ = qc.avaliar_tecnico(1920, 1080, -14.0, 0.0)
        self.assertTrue(falhas)

    def test_loudness_fora_do_alvo_avisa_sem_bloquear(self):
        falhas, avisos = qc.avaliar_tecnico(1920, 1080, -20.0, -1.5)
        self.assertEqual(falhas, [])
        self.assertTrue(avisos)


class TestCompliance(unittest.TestCase):
    def test_link_de_produto_valido(self):
        self.assertTrue(qc.link_amazon_valido('https://www.amazon.com.br/dp/B00XYZ'))
        self.assertTrue(qc.link_amazon_valido('https://amzn.to/gp/product/123'))

    def test_link_de_busca_invalido(self):
        self.assertFalse(qc.link_amazon_valido('https://www.amazon.com.br/s?k=1984'))

    def test_compliance_bloqueia_busca(self):
        falhas = qc.avaliar_compliance(['https://www.amazon.com.br/s?k=1984'])
        self.assertTrue(falhas)

    def test_compliance_ok_com_produto(self):
        self.assertEqual(qc.avaliar_compliance(['https://www.amazon.com.br/dp/B00XYZ']), [])


class TestExit(unittest.TestCase):
    def test_verde_sem_falhas(self):
        self.assertEqual(qc.exit_code([]), 0)

    def test_vermelho_com_falha(self):
        self.assertEqual(qc.exit_code(['qualquer falha']), 1)


if __name__ == '__main__':
    unittest.main()
