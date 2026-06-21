# -*- coding: utf-8 -*-
"""Testes do Gate de QC integrado ao build (Akita: TDD real, verde = exit code).

Cobrem:
  - montar_veredicto(): função PURA que converte (falhas, avisos) → dict JSON-serializável
  - aprovado(slug):  helper de consulta que lê _stems/<slug>/qc.json (ou False se ausente)
  - salvar_veredicto(): persiste o dict em _stems/<slug>/qc.json
"""
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]  # .../videos
sys.path.insert(0, str(ROOT))

import qc  # noqa: E402


class TestMontarVeredicto(unittest.TestCase):
    """montar_veredicto() deve ser PURA: só transforma (falhas, avisos) → dict."""

    def test_sem_falhas_aprovado(self):
        v = qc.montar_veredicto([], [])
        self.assertTrue(v['aprovado'])
        self.assertEqual(v['falhas'], [])
        self.assertEqual(v['avisos'], [])

    def test_com_falha_reprovado(self):
        v = qc.montar_veredicto(['resolução abaixo de 1080p'], ['loudness fora do alvo'])
        self.assertFalse(v['aprovado'])
        self.assertEqual(len(v['falhas']), 1)
        self.assertEqual(len(v['avisos']), 1)

    def test_retorno_e_dict_serializavel(self):
        """dict deve ser serializável em JSON sem exceção."""
        v = qc.montar_veredicto(['falha x'], ['aviso y'])
        dumped = json.dumps(v, ensure_ascii=False)
        recarregado = json.loads(dumped)
        self.assertEqual(recarregado['aprovado'], v['aprovado'])


class TestSalvarVeredicto(unittest.TestCase):
    """salvar_veredicto() deve criar _stems/<slug>/qc.json com o conteúdo correto."""

    def test_arquivo_criado_com_conteudo_correto(self):
        with tempfile.TemporaryDirectory() as tmp:
            stems = Path(tmp) / '_stems'
            veredicto = {'aprovado': True, 'falhas': [], 'avisos': ['loudness baixo']}
            qc.salvar_veredicto('meu-livro', veredicto, stems_root=Path(tmp))
            qc_json = stems / 'meu-livro' / 'qc.json'
            self.assertTrue(qc_json.exists(), 'qc.json deve ser criado')
            dados = json.loads(qc_json.read_text(encoding='utf-8'))
            self.assertTrue(dados['aprovado'])
            self.assertEqual(dados['avisos'], ['loudness baixo'])

    def test_sobrescreve_veredicto_anterior(self):
        with tempfile.TemporaryDirectory() as tmp:
            # primeiro: reprovado
            v1 = {'aprovado': False, 'falhas': ['x'], 'avisos': []}
            qc.salvar_veredicto('slug-a', v1, stems_root=Path(tmp))
            # segundo: aprovado (novo build corrigiu)
            v2 = {'aprovado': True, 'falhas': [], 'avisos': []}
            qc.salvar_veredicto('slug-a', v2, stems_root=Path(tmp))
            dados = json.loads((Path(tmp) / '_stems' / 'slug-a' / 'qc.json').read_text('utf-8'))
            self.assertTrue(dados['aprovado'])


class TestAprovado(unittest.TestCase):
    """aprovado(slug) é o helper que a lane de publicação consulta."""

    def test_false_se_qc_json_ausente(self):
        with tempfile.TemporaryDirectory() as tmp:
            resultado = qc.aprovado('nao-existe', stems_root=Path(tmp))
            self.assertFalse(resultado)

    def test_true_quando_aprovado(self):
        with tempfile.TemporaryDirectory() as tmp:
            v = {'aprovado': True, 'falhas': [], 'avisos': []}
            qc.salvar_veredicto('livro-ok', v, stems_root=Path(tmp))
            self.assertTrue(qc.aprovado('livro-ok', stems_root=Path(tmp)))

    def test_false_quando_reprovado(self):
        with tempfile.TemporaryDirectory() as tmp:
            v = {'aprovado': False, 'falhas': ['clip'], 'avisos': []}
            qc.salvar_veredicto('livro-ruim', v, stems_root=Path(tmp))
            self.assertFalse(qc.aprovado('livro-ruim', stems_root=Path(tmp)))

    def test_false_se_json_corrompido(self):
        """JSON inválido no disco = False seguro (nunca lança exceção)."""
        with tempfile.TemporaryDirectory() as tmp:
            d = Path(tmp) / '_stems' / 'corrompido'
            d.mkdir(parents=True)
            (d / 'qc.json').write_text('{ invalido', encoding='utf-8')
            self.assertFalse(qc.aprovado('corrompido', stems_root=Path(tmp)))


if __name__ == '__main__':
    unittest.main()
