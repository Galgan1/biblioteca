# -*- coding: utf-8 -*-
"""Regressão: um 500 isolado da NIM NÃO pode matar o build (22/jun/26 matou na cena 5).

O contrato do fix: `_post` distingue TRANSITÓRIO (5xx/429/timeout → levanta p/ o @retry
retentar) de PERMANENTE (4xx → devolve dict, não adianta retentar). E `gen()` nunca
propaga exceção — devolve None p/ o gerar_video decidir.
"""
import io
import os
import sys
import unittest
import urllib.error
from unittest import mock

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import nvidia


def _http_error(code):
    return urllib.error.HTTPError('http://x', code, 'msg', {}, io.BytesIO(b'corpo do erro'))


class TestPostTaxonomia(unittest.TestCase):
    def test_500_levanta_transitorio(self):
        # 5xx é retentável — tem que VIRAR exceção p/ o @retry pegar (não dict)
        with mock.patch('urllib.request.urlopen', side_effect=_http_error(500)):
            with self.assertRaises(nvidia._TransitorioNIM):
                nvidia._post('http://x', {})

    def test_429_levanta_transitorio(self):
        with mock.patch('urllib.request.urlopen', side_effect=_http_error(429)):
            with self.assertRaises(nvidia._TransitorioNIM):
                nvidia._post('http://x', {})

    def test_timeout_levanta_transitorio(self):
        with mock.patch('urllib.request.urlopen', side_effect=urllib.error.URLError('timed out')):
            with self.assertRaises(nvidia._TransitorioNIM):
                nvidia._post('http://x', {})

    def test_400_devolve_dict_sem_levantar(self):
        # 4xx é permanente — retentar não adianta; volta como dict de erro
        with mock.patch('urllib.request.urlopen', side_effect=_http_error(400)):
            r = nvidia._post('http://x', {})
        self.assertEqual(r['_http_error'], 400)


class TestRetryRecupera(unittest.TestCase):
    def test_gen_image_retenta_e_sucede(self):
        # 500 nas 2 primeiras, sucesso na 3ª → o @retry tem que ENTREGAR a imagem
        import base64
        png_b64 = base64.b64encode(b'\x89PNG' + b'z' * 50000).decode()   # > _MIN_IMG_BYTES (não-degenerado)
        ok = {'artifacts': [{'base64': png_b64}]}
        seq = [nvidia._TransitorioNIM('NIM 500'), nvidia._TransitorioNIM('NIM 500'), ok]
        out = os.path.join(os.path.dirname(__file__), '_tmp_nvidia.png')
        try:
            with mock.patch.object(nvidia, '_post', side_effect=seq), \
                 mock.patch('time.sleep'):                       # não dorme no teste
                r = nvidia.gen_image('prompt', out)
            self.assertIsNotNone(r)
            self.assertTrue(os.path.exists(out))
        finally:
            if os.path.exists(out):
                os.remove(out)

    def test_gen_nunca_propaga_excecao(self):
        # NIM fora de vez (sempre 500): gen() devolve None, NÃO crasha o caller
        with mock.patch.object(nvidia, '_post', side_effect=nvidia._TransitorioNIM('NIM 500')), \
             mock.patch('time.sleep'):
            r = nvidia.gen('prompt', os.path.join(os.path.dirname(__file__), '_nao_criado.png'))
        self.assertIsNone(r)


class TestImagemDegenerada(unittest.TestCase):
    def test_png_minusculo_e_descartado(self):
        # 200 com PNG ~6KB = placeholder de MODERAÇÃO → tem que virar None E apagar o cache
        import base64
        tiny = {'artifacts': [{'base64': base64.b64encode(b'x' * 6332).decode()}]}
        out = os.path.join(os.path.dirname(__file__), '_tmp_tiny.png')
        try:
            with mock.patch.object(nvidia, '_post', return_value=tiny):
                r = nvidia.gen_image('prompt moderado', out)
            self.assertIsNone(r)                       # não trata blank como sucesso
            self.assertFalse(os.path.exists(out))      # não envenena o cache
        finally:
            if os.path.exists(out):
                os.remove(out)

    def test_png_normal_passa(self):
        import base64
        big = {'artifacts': [{'base64': base64.b64encode(b'y' * 50000).decode()}]}
        out = os.path.join(os.path.dirname(__file__), '_tmp_big.png')
        try:
            with mock.patch.object(nvidia, '_post', return_value=big):
                r = nvidia.gen_image('prompt ok', out)
            self.assertIsNotNone(r)
            self.assertTrue(os.path.exists(out))
        finally:
            if os.path.exists(out):
                os.remove(out)


if __name__ == '__main__':
    unittest.main()
