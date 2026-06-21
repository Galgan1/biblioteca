# -*- coding: utf-8 -*-
"""Testes dos contratos Pydantic (valida o roteiro antes de gastar credito de API)."""
import unittest

try:
    from contracts import RoteiroCfg, PipelineStageResult
    from pydantic import ValidationError
    _OK = True
except Exception:
    _OK = False


def _roteiro_valido():
    return {
        'slug': 'x', 'titulo': 'X', 'autor': 'A',
        'cenas': [
            {'titulo': 'a', 'narracao': 'n'},
            {'titulo': 'b', 'narracao': 'n'},
            {'titulo': 'c', 'narracao': 'n'},
        ],
    }


@unittest.skipUnless(_OK, 'contracts/pydantic indisponivel')
class TestRoteiroCfg(unittest.TestCase):
    def test_roteiro_valido_passa(self):
        cfg = RoteiroCfg.model_validate(_roteiro_valido())
        self.assertEqual(cfg.slug, 'x')
        self.assertEqual(len(cfg.cenas), 3)
        self.assertEqual(cfg.provider, 'base')  # default

    def test_falta_campo_obrigatorio_falha(self):
        r = _roteiro_valido()
        del r['autor']
        with self.assertRaises(ValidationError):
            RoteiroCfg.model_validate(r)

    def test_menos_de_tres_cenas_falha(self):
        r = _roteiro_valido()
        r['cenas'] = r['cenas'][:2]
        with self.assertRaises(ValidationError):
            RoteiroCfg.model_validate(r)

    def test_indice_de_short_invalido_falha(self):
        r = dict(_roteiro_valido(), shorts=[0, 99])  # so ha 3 cenas (0-2)
        with self.assertRaises(ValidationError):
            RoteiroCfg.model_validate(r)

    def test_indice_de_short_valido_passa(self):
        cfg = RoteiroCfg.model_validate(dict(_roteiro_valido(), shorts=[0, 2]))
        self.assertEqual(cfg.shorts, [0, 2])

    def test_tts_rate_fora_do_intervalo_falha(self):
        r = dict(_roteiro_valido(), tts_rate=2.0)  # le=1.5
        with self.assertRaises(ValidationError):
            RoteiroCfg.model_validate(r)


@unittest.skipUnless(_OK, 'contracts/pydantic indisponivel')
class TestPipelineStageResult(unittest.TestCase):
    def test_status_valido(self):
        r = PipelineStageResult(slug='x', stage='uploaded', status='done')
        self.assertEqual(r.status, 'done')

    def test_status_invalido_falha(self):
        with self.assertRaises(ValidationError):
            PipelineStageResult(slug='x', stage='uploaded', status='concluido')


if __name__ == '__main__':
    unittest.main()
