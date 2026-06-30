# -*- coding: utf-8 -*-
"""servir_publicar (T2) — serviço HTTP isolado do botão 1-clique. Testa a LÓGICA sem subir
servidor real: funções puras (_autoriza/_slug_valido/_dispara/_status) + o handler com
rfile/wfile mocados. Anti-injeção: _dispara usa lista de args (Popen mocado). Akita: verde
= exit code."""
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import servir_publicar as sp  # noqa: E402


class TestAutoriza(unittest.TestCase):
    def setUp(self):
        self._tmp = Path(tempfile.mkdtemp())
        self._tok = self._tmp / 'publicar_token.txt'
        self._p = mock.patch.object(sp, 'TOKEN_FILE', self._tok)
        self._p.start()

    def tearDown(self):
        self._p.stop()

    def test_token_certo_autoriza(self):
        self._tok.write_text('s3gr3do\n', encoding='utf-8')  # \n -> strip
        self.assertTrue(sp._autoriza('s3gr3do'))

    def test_token_errado_nega(self):
        self._tok.write_text('s3gr3do', encoding='utf-8')
        self.assertFalse(sp._autoriza('outro'))

    def test_token_vazio_nega(self):
        self._tok.write_text('s3gr3do', encoding='utf-8')
        self.assertFalse(sp._autoriza(''))

    def test_arquivo_ausente_nega(self):
        self.assertFalse(self._tok.exists())
        self.assertFalse(sp._autoriza('qualquer'))  # ausente nunca "abre"


class TestSlugValido(unittest.TestCase):
    def test_aceita_validos(self):
        for s in ('1984', '48-leis-do-poder', 'a-unica-coisa'):
            self.assertTrue(sp._slug_valido(s), s)

    def test_recusa_invalidos(self):
        for s in ('', 'Maiusc', 'com espaco', '../etc', 'a;rm -rf', 'slug.py', 'acentuação'):
            self.assertFalse(sp._slug_valido(s), s)


class TestDispara(unittest.TestCase):
    def test_usa_lista_de_args_nunca_shell(self):
        with mock.patch.object(sp.subprocess, 'Popen') as popen:
            sp._dispara('48-leis-do-poder')
        popen.assert_called_once()
        args, kwargs = popen.call_args
        cmd = args[0]
        self.assertIsInstance(cmd, list)                 # lista, não string -> sem injeção
        self.assertEqual(cmd[0], sys.executable)
        self.assertTrue(cmd[1].endswith('publicar_tudo.py'))
        self.assertEqual(cmd[2], '48-leis-do-poder')
        self.assertNotIn('shell', kwargs)                # nunca shell=True


class TestStatus(unittest.TestCase):
    def setUp(self):
        self._tmp = Path(tempfile.mkdtemp())
        self._p = mock.patch.object(sp, 'ESTADO_DIR', self._tmp)
        self._p.start()

    def tearDown(self):
        self._p.stop()

    def test_le_state_file(self):
        est = {'youtube_longo': 'ok', 'instagram': 'erro', '_video_id': 'abc'}
        (self._tmp / 'slugx_publicar_tudo.json').write_text(
            json.dumps(est), encoding='utf-8')
        self.assertEqual(sp._status('slugx'), est)

    def test_sem_state_devolve_vazio(self):
        self.assertEqual(sp._status('nuncacomecou'), {})


# --- handler sem socket real ----------------------------------------------
class _FakeHandler(sp.Handler):
    """Instancia o handler sem o __init__ do BaseHTTPRequestHandler (que abriria socket)."""
    def __init__(self, path, headers, body=b''):
        self.path = path
        self.headers = headers
        self.rfile = io.BytesIO(body)
        self.wfile = io.BytesIO()
        self._status_code = None

    def send_response(self, code, message=None):
        self._status_code = code

    def send_header(self, *a, **k):
        pass

    def end_headers(self):
        pass


def _resp(h):
    return h._status_code, json.loads(h.wfile.getvalue().decode('utf-8'))


class TestHandlerPOST(unittest.TestCase):
    def _post(self, token, slug='1984'):
        body = json.dumps({'slug': slug}).encode('utf-8')
        h = _FakeHandler('/publicar',
                         {'X-Admin-Token': token, 'Content-Length': str(len(body))},
                         body)
        return h

    def test_token_errado_401(self):
        with mock.patch.object(sp, '_autoriza', return_value=False):
            h = self._post('errado')
            h.do_POST()
        code, payload = _resp(h)
        self.assertEqual(code, 401)
        self.assertFalse(payload['ok'])

    def test_slug_invalido_400(self):
        with mock.patch.object(sp, '_autoriza', return_value=True), \
             mock.patch.object(sp, '_dispara') as disp:
            h = self._post('ok', slug='Slug Invalido!')
            h.do_POST()
        code, payload = _resp(h)
        self.assertEqual(code, 400)
        disp.assert_not_called()                          # não dispara job com slug sujo

    def test_token_ok_slug_ok_dispara_e_200(self):
        with mock.patch.object(sp, '_autoriza', return_value=True), \
             mock.patch.object(sp, '_dispara') as disp:
            h = self._post('ok', slug='1984')
            h.do_POST()
        code, payload = _resp(h)
        self.assertEqual(code, 200)
        self.assertEqual(payload, {'ok': True, 'job': '1984', 'dry': False})  # sem 'dry' no body → publica de verdade
        disp.assert_called_once_with('1984', False)

    def test_rota_post_desconhecida_404(self):
        h = _FakeHandler('/outra', {}, b'')
        h.do_POST()
        code, payload = _resp(h)
        self.assertEqual(code, 404)


class TestHandlerGET(unittest.TestCase):
    def test_status_le_state(self):
        with mock.patch.object(sp, '_status', return_value={'instagram': 'ok'}) as st:
            h = _FakeHandler('/status?slug=1984', {}, b'')
            h.do_GET()
        code, payload = _resp(h)
        self.assertEqual(code, 200)
        self.assertEqual(payload, {'instagram': 'ok'})
        st.assert_called_once_with('1984')

    def test_status_slug_invalido_400(self):
        h = _FakeHandler('/status?slug=../etc', {}, b'')
        h.do_GET()
        code, payload = _resp(h)
        self.assertEqual(code, 400)

    def test_rota_get_desconhecida_404(self):
        h = _FakeHandler('/qualquer', {}, b'')
        h.do_GET()
        code, _ = _resp(h)
        self.assertEqual(code, 404)

    def test_livros_lista_via_get(self):
        with mock.patch.object(sp, '_livros', return_value=[{'slug': 'x', 'titulo': 'X', 'autor': 'A'}]):
            h = _FakeHandler('/livros', {}, b'')
            h.do_GET()
        code, payload = _resp(h)
        self.assertEqual(code, 200)
        self.assertEqual(payload, {'livros': [{'slug': 'x', 'titulo': 'X', 'autor': 'A'}]})


class TestLivros(unittest.TestCase):
    """_livros lista só os roteiros publicáveis (titulo+cenas, slug válido) — pra UI
    não exigir slug de cor. Ignora config/estado/json-quebrado/nome-invalido."""

    def test_lista_so_roteiros_validos(self):
        import json as _j
        import tempfile
        from pathlib import Path as _P
        with tempfile.TemporaryDirectory() as d:
            base = _P(d)
            (base / '1984-showcase.json').write_text(
                _j.dumps({'titulo': '1984', 'autor': 'Orwell', 'cenas': [{'x': 1}]}), encoding='utf-8')
            (base / 'config.json').write_text(_j.dumps({'foo': 'bar'}), encoding='utf-8')   # não-roteiro
            (base / 'quebrado.json').write_text('{nao json', encoding='utf-8')              # inválido
            (base / 'Slug_Ruim.json').write_text(                                            # nome fora do ^[a-z0-9-]+$
                _j.dumps({'titulo': 'x', 'cenas': [{}]}), encoding='utf-8')
            livros = sp._livros(base)
            slugs = [b['slug'] for b in livros]
            self.assertIn('1984-showcase', slugs)
            self.assertNotIn('config', slugs)        # sem 'cenas' -> fora
            self.assertNotIn('quebrado', slugs)      # json inválido -> fora
            self.assertNotIn('Slug_Ruim', slugs)     # slug inválido -> fora
            b = next(x for x in livros if x['slug'] == '1984-showcase')
            self.assertEqual(b['titulo'], '1984')
            self.assertEqual(b['autor'], 'Orwell')


if __name__ == '__main__':
    unittest.main()
