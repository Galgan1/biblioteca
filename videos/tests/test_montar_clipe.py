# -*- coding: utf-8 -*-
"""Regressão: um clipe de movimento corrompido NÃO pode matar o render (22/jun/26
um clipe 3DGS malformado crashou o ffmpeg e abortou o build de 5 min na cena 2).

Contrato de _montar_clipe: tenta o movimento; se ele LEVANTAR, cai no slide estático
e o build segue. Sem movimento disponível, vai direto pro slide.
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import gerar_video


class TestMontarClipe(unittest.TestCase):
    def test_movimento_ok_nao_chama_slide(self):
        chamou = {'mov': False, 'slide': False}

        def mov():
            chamou['mov'] = True

        def slide():
            chamou['slide'] = True

        usou = gerar_video._montar_clipe('clipe.mp4', mov, slide)
        self.assertEqual(usou, 'movimento')
        self.assertTrue(chamou['mov'])
        self.assertFalse(chamou['slide'])           # não desperdiça o slide se o movimento deu certo

    def test_movimento_falha_cai_no_slide(self):
        # o CORAÇÃO da regressão: ffmpeg crashou no clipe de movimento → build continua
        chamou = {'slide': False}

        def mov():
            raise RuntimeError('ffmpeg returned non-zero exit status 3752568763')

        def slide():
            chamou['slide'] = True

        usou = gerar_video._montar_clipe('clipe_corrompido.mp4', mov, slide)
        self.assertEqual(usou, 'slide')
        self.assertTrue(chamou['slide'])            # caiu no estático em vez de abortar

    def test_sem_movimento_vai_direto_ao_slide(self):
        chamou = {'mov': False, 'slide': False}
        usou = gerar_video._montar_clipe(
            None,
            lambda: chamou.__setitem__('mov', True),
            lambda: chamou.__setitem__('slide', True))
        self.assertEqual(usou, 'slide')
        self.assertFalse(chamou['mov'])
        self.assertTrue(chamou['slide'])


if __name__ == '__main__':
    unittest.main()
