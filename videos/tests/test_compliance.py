# -*- coding: utf-8 -*-
"""Conferente de direitos (compliance) — lar canônico das regras de direito:
link de afiliado só de produto, prompt de imagem sem IP protegida, trilha licenciada.
Tudo PURO/local. Akita: verde = exit code; estes são BLOQUEANTES."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]  # .../videos
sys.path.insert(0, str(ROOT))

import compliance as cp  # noqa: E402


class TestLink(unittest.TestCase):
    def test_produto_valido(self):
        self.assertTrue(cp.link_amazon_valido('https://www.amazon.com.br/dp/B00X'))
        self.assertTrue(cp.link_amazon_valido('https://amzn.to/gp/product/1'))

    def test_busca_invalido(self):
        self.assertFalse(cp.link_amazon_valido('https://www.amazon.com.br/s?k=1984'))

    def test_auditar_links_bloqueia_busca(self):
        self.assertTrue(cp.auditar_links(['https://www.amazon.com.br/s?k=x']))
        self.assertEqual(cp.auditar_links(['https://www.amazon.com.br/dp/B00X']), [])


class TestPromptSeguro(unittest.TestCase):
    def test_ip_protegida_detectada(self):
        achados = cp.prompt_seguro('a portrait of Mickey Mouse in ancient China')
        self.assertTrue(achados)

    def test_prompt_descritivo_limpo(self):
        limpo = ('two vast ancient armies facing each other across a foggy plain, '
                 'banners raised, distant mountains, cinematic painterly')
        self.assertEqual(cp.prompt_seguro(limpo), [])


class TestLicencaTrilha(unittest.TestCase):
    def test_procedural_propria_ok(self):
        self.assertTrue(cp.licenca_trilha_ok(True))
        self.assertTrue(cp.licenca_trilha_ok('procedural'))
        self.assertTrue(cp.licenca_trilha_ok('cc0'))

    def test_externa_desconhecida_reprovada(self):
        self.assertFalse(cp.licenca_trilha_ok('musica_baixada_do_youtube.mp3'))


class TestAuditar(unittest.TestCase):
    def _cfg(self, img='a foggy plain with armies', musica=True):
        return {'slug': 't', 'titulo': 'T', 'musica': musica,
                'estilo_img': 'cinematic painterly',
                'cenas': [{'tipo': 'conceito', 'img': img, 'narracao': 'x'}]}

    def test_cfg_limpo_passa(self):
        falhas, _ = cp.auditar(self._cfg())
        self.assertEqual(falhas, [])

    def test_ip_no_prompt_bloqueia(self):
        falhas, _ = cp.auditar(self._cfg(img='Batman flying over Gotham'))
        self.assertTrue(falhas)

    def test_trilha_externa_bloqueia(self):
        falhas, _ = cp.auditar(self._cfg(musica='rip_album.mp3'))
        self.assertTrue(falhas)


if __name__ == '__main__':
    unittest.main()
