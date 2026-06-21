# -*- coding: utf-8 -*-
"""Testes das funções compartilhadas da família Facebook (Akita pilar 2 — verde = exit code).

Cobre o comportamento ATUAL de facebook_post.py antes de extrair as funções
duplicadas para um facebook_base.py (refatoração DRY planejada).

Funções testadas (duplicadas 4–6× entre os módulos FB):
  - HASHTAGS_BASE  — valor canônico esperado
  - _token()       — lê .secrets/facebook_page_token.txt; sys.exit se ausente
  - _page_id()     — lê .secrets/facebook_page_id.txt; sys.exit se ausente
  - _post()        — POST url-encoded; sucesso → JSON; HTTPError → {'error': {...}}

Funções puras de facebook_copy.py também cobertas:
  - hashtags()     — base + tags de cfg.youtube.tags, sem repetição, com #
  - _slugify_tag() — normaliza NFKD → ascii → minúsculas → só alnum
  - cta_text()     — (facebook_comment.py) pura, sem I/O

Herméticos: sem rede real, sem token real, sem disco real.
urlopen é mockado via unittest.mock; caminhos de arquivo via tmp_path-equivalente.
"""
import io
import json
import sys
import tempfile
import unittest
import urllib.error
from pathlib import Path
from unittest import mock

# ── caminho do módulo ──────────────────────────────────────────────────────────
# Os módulos ficam em videos/, um nível acima deste arquivo; garante importabilidade.
_VIDEOS_DIR = Path(__file__).parent.parent
if str(_VIDEOS_DIR) not in sys.path:
    sys.path.insert(0, str(_VIDEOS_DIR))

import facebook_comment  # noqa: E402 — importação após ajuste de sys.path
import facebook_copy     # noqa: E402
import facebook_post     # noqa: E402


# ── helpers de mock ───────────────────────────────────────────────────────────

class _FakeHTTPResp:
    """Substituto mínimo para o objeto retornado por urlopen() em facebook_post._post."""

    def __init__(self, payload: dict):
        self._data = json.dumps(payload).encode('utf-8')

    def read(self, *_):
        return self._data

    # json.load chama fp.read(size) internamente (io.BufferedReader protocol).
    # A forma mais simples é wrapar em io.BytesIO.
    def __enter__(self):
        return io.BytesIO(self._data)

    def __exit__(self, *_):
        return False


def _fake_urlopen_ok(payload: dict):
    """Retorna um callable que sempre devolve um BytesIO com `payload` serializado."""
    def _open(req, timeout=None):
        return io.BytesIO(json.dumps(payload).encode('utf-8'))
    return _open


def _fake_http_error(code: int, body: str = 'erro simulado'):
    """Retorna um callable que levanta HTTPError com o código e corpo dados."""
    def _open(req, timeout=None):
        raise urllib.error.HTTPError(
            url=None, code=code, msg=body,
            hdrs={}, fp=io.BytesIO(body.encode('utf-8')))
    return _open


# ── 1. HASHTAGS_BASE ──────────────────────────────────────────────────────────

class TestHashtagsBase(unittest.TestCase):
    """HASHTAGS_BASE deve ser ['livros', 'resumodelivro', 'leitura'] em todos os módulos FB."""

    ESPERADO = ['livros', 'resumodelivro', 'leitura']

    def test_facebook_post_hashtags_base(self):
        self.assertEqual(facebook_post.HASHTAGS_BASE, self.ESPERADO)

    def test_facebook_copy_hashtags_base(self):
        # facebook_copy também define HASHTAGS_BASE (fonte canônica; os outros copiam)
        self.assertEqual(facebook_copy.HASHTAGS_BASE, self.ESPERADO)


# ── 2. _token() ───────────────────────────────────────────────────────────────

class TestToken(unittest.TestCase):
    """_token() deve: retornar o token quando o arquivo existe; sys.exit quando ausente."""

    def _patch_token_file(self, tmp_dir: Path):
        """Aponta PAGE_TOKEN_FILE para um arquivo dentro de tmp_dir."""
        return mock.patch.object(facebook_post, 'PAGE_TOKEN_FILE', tmp_dir / 'token.txt')

    def test_token_retorna_conteudo_sem_espacos(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / 'token.txt'
            p.write_text('  meu_token_falso  \n', encoding='utf-8')
            with mock.patch.object(facebook_post, 'PAGE_TOKEN_FILE', p):
                resultado = facebook_post._token()
        self.assertEqual(resultado, 'meu_token_falso')

    def test_token_sys_exit_quando_arquivo_ausente(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / 'nao_existe.txt'
            with mock.patch.object(facebook_post, 'PAGE_TOKEN_FILE', p):
                with self.assertRaises(SystemExit):
                    facebook_post._token()

    def test_token_mensagem_de_erro_menciona_arquivo(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / 'facebook_page_token.txt'
            with mock.patch.object(facebook_post, 'PAGE_TOKEN_FILE', p):
                try:
                    facebook_post._token()
                except SystemExit as e:
                    self.assertIn('facebook_page_token', str(e))
                else:
                    self.fail('esperava SystemExit')


# ── 3. _page_id() ─────────────────────────────────────────────────────────────

class TestPageId(unittest.TestCase):
    """_page_id() deve: retornar o id quando o arquivo existe; sys.exit quando ausente."""

    def test_page_id_retorna_conteudo_sem_espacos(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / 'page_id.txt'
            p.write_text('  12345678  \n', encoding='utf-8')
            with mock.patch.object(facebook_post, 'PAGE_ID_FILE', p):
                resultado = facebook_post._page_id()
        self.assertEqual(resultado, '12345678')

    def test_page_id_sys_exit_quando_arquivo_ausente(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / 'nao_existe.txt'
            with mock.patch.object(facebook_post, 'PAGE_ID_FILE', p):
                with self.assertRaises(SystemExit):
                    facebook_post._page_id()

    def test_page_id_mensagem_de_erro_menciona_arquivo(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / 'facebook_page_id.txt'
            with mock.patch.object(facebook_post, 'PAGE_ID_FILE', p):
                try:
                    facebook_post._page_id()
                except SystemExit as e:
                    self.assertIn('facebook_page_id', str(e))
                else:
                    self.fail('esperava SystemExit')


# ── 4. _post() ────────────────────────────────────────────────────────────────

class TestPost(unittest.TestCase):
    """_post(path, token, params) deve: sucesso → JSON; HTTPError → {'error': {...}}."""

    @mock.patch('facebook_base.urllib.request.urlopen')
    def test_sucesso_retorna_json(self, m_urlopen):
        payload = {'id': '999_abc'}
        m_urlopen.side_effect = _fake_urlopen_ok(payload)
        resultado = facebook_post._post('/123/feed', 'tok_dummy', {'message': 'oi'})
        self.assertEqual(resultado, payload)

    @mock.patch('facebook_base.urllib.request.urlopen')
    def test_sucesso_inclui_access_token_no_body(self, m_urlopen):
        """access_token é injetado em params antes do POST (nunca viaja fora do corpo)."""
        capturado = {}

        def _open(req, timeout=None):
            capturado['data'] = req.data.decode('utf-8')
            return io.BytesIO(json.dumps({'id': 'x'}).encode())

        m_urlopen.side_effect = _open
        facebook_post._post('/123/feed', 'meu_tok', {'message': 'oi'})
        self.assertIn('access_token=meu_tok', capturado['data'])

    @mock.patch('facebook_base.urllib.request.urlopen')
    def test_http_error_retorna_dict_com_chave_error(self, m_urlopen):
        m_urlopen.side_effect = _fake_http_error(400, 'mensagem de erro da API')
        resultado = facebook_post._post('/123/feed', 'tok_dummy', {})
        self.assertIn('error', resultado)

    @mock.patch('facebook_base.urllib.request.urlopen')
    def test_http_error_preserva_code(self, m_urlopen):
        m_urlopen.side_effect = _fake_http_error(401, 'sem permissao')
        resultado = facebook_post._post('/123/feed', 'tok_dummy', {})
        self.assertEqual(resultado['error']['code'], 401)

    @mock.patch('facebook_base.urllib.request.urlopen')
    def test_http_error_message_truncado_em_300_chars(self, m_urlopen):
        corpo_longo = 'x' * 500
        m_urlopen.side_effect = _fake_http_error(500, corpo_longo)
        resultado = facebook_post._post('/123/feed', 'tok_dummy', {})
        self.assertLessEqual(len(resultado['error']['message']), 300)

    @mock.patch('facebook_base.urllib.request.urlopen')
    def test_url_montada_com_graph_prefix(self, m_urlopen):
        """URL final deve começar com o GRAPH base (não duplicar nem perder a barra)."""
        capturado = {}

        def _open(req, timeout=None):
            capturado['url'] = req.full_url
            return io.BytesIO(json.dumps({'id': 'y'}).encode())

        m_urlopen.side_effect = _open
        facebook_post._post('/pg_id/feed', 'tok', {'message': 'x'})
        self.assertTrue(capturado['url'].startswith('https://graph.facebook.com/'))
        self.assertIn('/pg_id/feed', capturado['url'])


# ── 5. facebook_copy — funções puras ─────────────────────────────────────────

class TestFacebookCopyHashtags(unittest.TestCase):
    """hashtags(cfg, n) deve combinar HASHTAGS_BASE + youtube.tags sem repetição."""

    def _cfg(self, tags):
        return {'titulo': 'Livro X', 'youtube': {'tags': tags}}

    def test_hashtags_sem_tags_extras_retorna_so_a_base(self):
        resultado = facebook_copy.hashtags(self._cfg([]), n=5)
        for base_tag in facebook_copy.HASHTAGS_BASE:
            self.assertIn('#' + base_tag, resultado)
        self.assertEqual(resultado.count('#'), len(facebook_copy.HASHTAGS_BASE))

    def test_hashtags_com_extras_sem_repeticao(self):
        resultado = facebook_copy.hashtags(self._cfg(['livros', 'filosofia']), n=5)
        # 'livros' já está na base — não deve duplicar
        self.assertEqual(resultado.count('#livros'), 1)
        self.assertIn('#filosofia', resultado)

    def test_hashtags_respeita_limite_n(self):
        tags_extras = [f'tag{i}' for i in range(20)]
        resultado = facebook_copy.hashtags(self._cfg(tags_extras), n=4)
        self.assertEqual(resultado.count('#'), 4)

    def test_hashtags_com_espacos_e_acentos_slugificados(self):
        resultado = facebook_copy.hashtags(self._cfg(['Psicologia Financeira']), n=5)
        # espaços removidos + normalização NFKD
        self.assertIn('#psicologiafinanceira', resultado)


class TestFacebookCopySlugifyTag(unittest.TestCase):
    """_slugify_tag deve: minúsculas, sem acentos, sem espaços, só alnum."""

    def test_ascii_simples(self):
        self.assertEqual(facebook_copy._slugify_tag('Leitura'), 'leitura')

    def test_acentos_removidos(self):
        self.assertEqual(facebook_copy._slugify_tag('Psicológica'), 'psicologica')

    def test_espaco_removido(self):
        self.assertEqual(facebook_copy._slugify_tag('resumo de livro'), 'resumodelivro')

    def test_pontuacao_removida(self):
        self.assertEqual(facebook_copy._slugify_tag('livro!'), 'livro')


# ── 6. facebook_comment.cta_text() — função pura ─────────────────────────────

class TestCtaText(unittest.TestCase):
    """cta_text() é pura (sem I/O); testa o contrato de conteúdo."""

    def test_sem_video_id_nao_menciona_youtube(self):
        texto = facebook_comment.cta_text(video_id=None)
        self.assertNotIn('youtu.be', texto)
        self.assertNotIn('YouTube', texto)

    def test_com_video_id_inclui_link_youtube(self):
        texto = facebook_comment.cta_text(video_id='abc123')
        self.assertIn('https://youtu.be/abc123', texto)

    def test_sempre_inclui_link_do_acervo(self):
        texto = facebook_comment.cta_text()
        self.assertIn('andregalgani.com.br', texto)

    def test_site_url_personalizado(self):
        texto = facebook_comment.cta_text(site_url='https://meusite.com')
        self.assertIn('https://meusite.com', texto)

    def test_extra_incluido_quando_fornecido(self):
        texto = facebook_comment.cta_text(extra='Frase extra.')
        self.assertIn('Frase extra.', texto)

    def test_retorna_string_nao_vazia(self):
        self.assertIsInstance(facebook_comment.cta_text(), str)
        self.assertTrue(facebook_comment.cta_text())


if __name__ == '__main__':
    unittest.main(verbosity=2)
