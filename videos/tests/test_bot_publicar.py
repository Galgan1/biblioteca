# -*- coding: utf-8 -*-
"""test_bot_publicar — handler PUBLICAR do bot Telegram. SEM publicar de verdade:
subprocess.Popen é mocado. Prova o gate de SEGURANÇA (R3): slug VÁLIDO → Popen com os
args certos; slug INVÁLIDO → NÃO chama Popen (texto de erro). Akita: verde = exit code."""
import sys
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]            # .../videos
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from _bot_handlers import h_publicar as hp  # noqa: E402

VALIDO = 'meu-livro-valido'


def _slugs_falsos():
    return [VALIDO, 'outro-livro']


class TestSlugs(unittest.TestCase):
    def test_books_json_ausente_lista_vazia(self):
        # Best-effort: arquivo inexistente → [] (gate recusa tudo, não explode).
        with mock.patch.object(hp, 'BOOKS_JSON', ROOT / '_nao_existe_xyz.json'):
            self.assertEqual(hp.slugs(), [])


class TestConfirmar(unittest.TestCase):
    def test_slug_valido_texto_de_confirmacao(self):
        with mock.patch.object(hp, 'slugs', _slugs_falsos):
            txt = hp.confirmar(VALIDO)
        self.assertIn(VALIDO, txt)
        self.assertIn('Publicar', txt)   # intenção de confirmação (texto premium novo)

    def test_slug_invalido_texto_de_erro(self):
        with mock.patch.object(hp, 'slugs', _slugs_falsos):
            txt = hp.confirmar('nao-existe')
        self.assertIn('invalido', txt.lower())


class TestExecutar(unittest.TestCase):
    def test_slug_valido_dispara_popen_com_args_certos(self):
        with mock.patch.object(hp, 'slugs', _slugs_falsos), \
             mock.patch.object(hp.subprocess, 'Popen') as popen:
            ret = hp.executar(VALIDO)
        popen.assert_called_once()
        args, kwargs = popen.call_args
        cmd = args[0]
        self.assertIsInstance(cmd, list)                  # lista, não string → sem injeção
        self.assertEqual(cmd[0], sys.executable)
        self.assertTrue(cmd[1].endswith('publicar_tudo.py'))
        self.assertEqual(cmd[2], VALIDO)
        self.assertNotIn('--dry', cmd)                    # default = publica de verdade
        self.assertNotIn('shell', kwargs)                 # nunca shell=True
        self.assertIn(VALIDO, ret)

    def test_dry_passa_flag(self):
        with mock.patch.object(hp, 'slugs', _slugs_falsos), \
             mock.patch.object(hp.subprocess, 'Popen') as popen:
            hp.executar(VALIDO, dry=True)
        cmd = popen.call_args[0][0]
        self.assertIn('--dry', cmd)

    def test_slug_invalido_NAO_dispara_popen(self):
        # R3: o coração da segurança — slug fora de books.json nunca chama Popen.
        with mock.patch.object(hp, 'slugs', _slugs_falsos), \
             mock.patch.object(hp.subprocess, 'Popen') as popen:
            ret = hp.executar('nao-existe')
        popen.assert_not_called()
        self.assertIn('invalido', ret.lower())


if __name__ == '__main__':
    unittest.main()
