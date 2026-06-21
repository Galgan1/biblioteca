# -*- coding: utf-8 -*-
"""Testes dos contratos Pydantic (valida o roteiro antes de gastar credito de API)."""
import json
import tempfile
import unittest
from pathlib import Path

try:
    from contracts import RoteiroCfg, PipelineStageResult, load_roteiro
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


@unittest.skipUnless(_OK, 'contracts/pydantic indisponivel')
class TestLoadRoteiro(unittest.TestCase):
    """Testa load_roteiro como guarda dura (lê arquivo, não dict)."""

    def _escreve_json(self, tmp_dir, dados):
        p = Path(tmp_dir) / 'roteiro.json'
        p.write_text(json.dumps(dados, ensure_ascii=False), encoding='utf-8')
        return str(p)

    def test_roteiro_minimo_valido_passa(self):
        """Roteiro com campos obrigatórios mínimos → load_roteiro retorna RoteiroCfg sem lançar."""
        dados = {
            'slug': 'teste', 'titulo': 'Teste', 'autor': 'Autor',
            'cenas': [
                {'titulo': 'c1', 'narracao': 'n1'},
                {'titulo': 'c2', 'narracao': 'n2'},
                {'titulo': 'c3', 'narracao': 'n3'},
            ],
        }
        with tempfile.TemporaryDirectory() as tmp:
            cfg = load_roteiro(self._escreve_json(tmp, dados))
        self.assertEqual(cfg.slug, 'teste')
        self.assertEqual(len(cfg.cenas), 3)

    def test_roteiro_invalido_campo_ausente_lanca(self):
        """Roteiro sem campo obrigatório ('autor') → load_roteiro LANÇA ValidationError.
        Este é o comportamento da guarda dura: bloqueia ANTES de gastar API."""
        dados = {
            'slug': 'teste', 'titulo': 'Teste',
            # 'autor' ausente — campo obrigatório
            'cenas': [
                {'titulo': 'c1', 'narracao': 'n1'},
                {'titulo': 'c2', 'narracao': 'n2'},
                {'titulo': 'c3', 'narracao': 'n3'},
            ],
        }
        with tempfile.TemporaryDirectory() as tmp:
            path = self._escreve_json(tmp, dados)
            with self.assertRaises(ValidationError):
                load_roteiro(path)

    def test_roteiro_invalido_shorts_fora_do_range_lanca(self):
        """Roteiro com shorts=[0, 99] (só há 3 cenas) → load_roteiro LANÇA ValidationError."""
        dados = {
            'slug': 'teste', 'titulo': 'Teste', 'autor': 'Autor',
            'shorts': [0, 99],
            'cenas': [
                {'titulo': 'c1', 'narracao': 'n1'},
                {'titulo': 'c2', 'narracao': 'n2'},
                {'titulo': 'c3', 'narracao': 'n3'},
            ],
        }
        with tempfile.TemporaryDirectory() as tmp:
            path = self._escreve_json(tmp, dados)
            with self.assertRaises(ValidationError):
                load_roteiro(path)


if __name__ == '__main__':
    unittest.main()
