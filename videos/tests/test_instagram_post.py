# -*- coding: utf-8 -*-
"""Testes de pin de comportamento para instagram_post.py (Akita pilar 2 — verde = exit code).

Cobertos: funções PURAS e mockáveis. Nada de rede, token real ou disco de produção.
  - _frases(texto)          — split de frases por .?!
  - _afiliado_block(slug)   — rodapé de disclosure (sem link cru na legenda do IG)
  - caption_for(cfg, idx)   — legenda do Reel: gancho + hashtags + disclosure
  - _token()                — ausência de arquivo → sys.exit
  - _user_id()              — ausência de arquivo → sys.exit
  - COVER_OFFSET_MS         — constante de capa de Reel presente e próxima a 1500
  - post_reel(...)          — rota video_url (rede/scp/_post mockados): contêiner com
                              video_url + thumb_offset, depois media_publish

NÃO testados: post_carousel, _png_to_jpg, _scp_host, _scp_video (rede/API/PIL/scp).
caption_carousel: depende de importar <slug>_data.py em runtime — coberto via mock
de _book_for para evitar dependência de arquivo de dados de produção.
"""
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

# Importa o módulo alvo; para _token/_user_id não lerem disco de produção durante
# a importação (eles só leem ao serem chamados), não é necessário patch no import.
import instagram_post as ig


# ---------------------------------------------------------------------------
# Helpers de fixture
# ---------------------------------------------------------------------------

def _cfg_minimo(slug='test-slug', titulo='Livro Teste', narracao='Frase um. Frase dois. Frase três.'):
    """Configuração de roteiro mínima (in-memory) para caption_for."""
    return {
        'slug': slug,
        'titulo': titulo,
        'cenas': [
            {'narracao': narracao},
        ],
        'shorts': [0],
        'youtube': {'tags': ['hábito', 'produtividade']},
    }


# ---------------------------------------------------------------------------
# _frases
# ---------------------------------------------------------------------------

class TestFrases(unittest.TestCase):
    def test_separa_frases_por_ponto(self):
        resultado = ig._frases('Primeira frase. Segunda frase. Terceira frase.')
        self.assertEqual(len(resultado), 3)
        self.assertEqual(resultado[0], 'Primeira frase.')
        self.assertEqual(resultado[2], 'Terceira frase.')

    def test_separa_por_interrogacao(self):
        resultado = ig._frases('Você sabia? Isso muda tudo. Veja como!')
        self.assertEqual(len(resultado), 3)
        self.assertEqual(resultado[0], 'Você sabia?')

    def test_separa_por_exclamacao(self):
        resultado = ig._frases('Incrível! Funciona assim.')
        self.assertEqual(len(resultado), 2)
        self.assertEqual(resultado[0], 'Incrível!')

    def test_texto_vazio_retorna_lista_vazia(self):
        self.assertEqual(ig._frases(''), [])
        self.assertEqual(ig._frases(None), [])

    def test_texto_sem_separador_retorna_uma_frase(self):
        resultado = ig._frases('Apenas uma frase sem ponto final')
        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0], 'Apenas uma frase sem ponto final')

    def test_espacos_extras_sao_ignorados(self):
        resultado = ig._frases('  Frase com espaço.   Outra frase.  ')
        for f in resultado:
            self.assertEqual(f, f.strip())


# ---------------------------------------------------------------------------
# _afiliado_block — regra do IG: sem link cru na legenda
# ---------------------------------------------------------------------------

class TestAfiliado(unittest.TestCase):
    def test_nao_contem_link_cru(self):
        """IG não torna URL clicável na legenda — URL http não deve aparecer aqui.
        Nota: a disclosure PODE conter a palavra 'Amazon' (é texto, não URL) — ok."""
        bloco = ig._afiliado_block('qualquer-slug')
        self.assertNotIn('http', bloco, 'Link cru (URL) encontrado na legenda do IG — viola a regra de afiliado')
        self.assertNotIn('amazon.com', bloco.lower(), 'Domínio amazon.com encontrado na legenda do IG')

    def test_contem_disclosure_obrigatoria(self):
        """Disclosure de Associado Amazon deve estar presente (obrigação legal)."""
        bloco = ig._afiliado_block('qualquer-slug')
        self.assertIn('Associado', bloco)

    def test_retorna_string_nao_vazia(self):
        bloco = ig._afiliado_block('algum-livro')
        self.assertIsInstance(bloco, str)
        self.assertTrue(bloco.strip())

    def test_slug_nao_altera_resultado(self):
        """O slug não muda o bloco (link não fica na legenda de nenhum livro)."""
        b1 = ig._afiliado_block('habitos-atomicos')
        b2 = ig._afiliado_block('sapiens')
        self.assertEqual(b1, b2)


# ---------------------------------------------------------------------------
# caption_for — legenda do Reel
# ---------------------------------------------------------------------------

class TestCaptionFor(unittest.TestCase):
    def setUp(self):
        self.cfg = _cfg_minimo()

    def test_contem_gancho_da_primeira_frase(self):
        cap = ig.caption_for(self.cfg, 0)
        # a 1ª frase da narração deve estar no começo da legenda
        self.assertIn('Frase um.', cap)

    def test_contem_hashtags_base(self):
        cap = ig.caption_for(self.cfg, 0)
        for tag in ig.HASHTAGS_BASE:
            self.assertIn(f'#{tag}', cap)

    def test_contem_disclosure_afiliado(self):
        cap = ig.caption_for(self.cfg, 0)
        self.assertIn(ig.DISCLOSURE, cap)

    def test_contem_marca_narrado_ia(self):
        """Divulgação de conteúdo gerado por IA deve estar presente."""
        cap = ig.caption_for(self.cfg, 0)
        self.assertIn('IA', cap)

    def test_nao_contem_link_cru(self):
        """Link cru não deve aparecer na legenda do IG (só disclosure)."""
        cap = ig.caption_for(self.cfg, 0)
        self.assertNotIn('amazon.com.br', cap)

    def test_contem_cta_link_na_bio(self):
        """CTA deve mencionar 'link na bio' — único lugar clicável no IG."""
        cap = ig.caption_for(self.cfg, 0)
        self.assertIn('link na bio', cap)

    def test_contem_salve_e_siga(self):
        """Apelo de salvamento e seguimento — sinal de ranking do algoritmo."""
        cap = ig.caption_for(self.cfg, 0)
        self.assertIn('Salve', cap)
        self.assertIn('@minutoreal1701', cap)

    def test_contem_titulo_do_livro(self):
        cap = ig.caption_for(self.cfg, 0)
        self.assertIn(self.cfg['titulo'], cap)

    def test_narracao_vazia_usa_titulo_como_gancho(self):
        """Quando não há narração, o título substitui o gancho."""
        cfg = _cfg_minimo(narracao='')
        cap = ig.caption_for(cfg, 0)
        self.assertIn(cfg['titulo'], cap)

    def test_retorna_string(self):
        cap = ig.caption_for(self.cfg, 0)
        self.assertIsInstance(cap, str)
        self.assertTrue(len(cap) > 50)


# ---------------------------------------------------------------------------
# caption_carousel — via mock de _book_for
# ---------------------------------------------------------------------------

class TestCaptionCarousel(unittest.TestCase):
    def _book_fake(self):
        return {
            'title': 'Livro de Teste',
            'author': 'Autor Fictício',
            'intro': 'Uma grande ideia. Que muda tudo. Veja como funciona.',
            'tags': ['hábito', 'produtividade'],
        }

    @mock.patch('instagram_post._book_for')
    def test_contem_gancho_da_intro(self, mock_book):
        mock_book.return_value = self._book_fake()
        cap = ig.caption_carousel('slug-qualquer')
        self.assertIn('Uma grande ideia.', cap)

    @mock.patch('instagram_post._book_for')
    def test_contem_cta_salvar(self, mock_book):
        """Carrossel é campeão de salvamento — CTA de salvar deve estar presente."""
        mock_book.return_value = self._book_fake()
        cap = ig.caption_carousel('slug-qualquer')
        self.assertIn('Salve', cap)

    @mock.patch('instagram_post._book_for')
    def test_contem_disclosure(self, mock_book):
        mock_book.return_value = self._book_fake()
        cap = ig.caption_carousel('slug-qualquer')
        self.assertIn(ig.DISCLOSURE, cap)

    @mock.patch('instagram_post._book_for')
    def test_nao_contem_link_cru(self, mock_book):
        mock_book.return_value = self._book_fake()
        cap = ig.caption_carousel('slug-qualquer')
        self.assertNotIn('amazon.com.br', cap)

    @mock.patch('instagram_post._book_for')
    def test_contem_autor(self, mock_book):
        mock_book.return_value = self._book_fake()
        cap = ig.caption_carousel('slug-qualquer')
        self.assertIn('Autor Fictício', cap)

    @mock.patch('instagram_post._book_for')
    def test_contem_link_na_bio(self, mock_book):
        mock_book.return_value = self._book_fake()
        cap = ig.caption_carousel('slug-qualquer')
        self.assertIn('link na bio', cap)

    @mock.patch('instagram_post._book_for')
    def test_contem_hashtags_base(self, mock_book):
        mock_book.return_value = self._book_fake()
        cap = ig.caption_carousel('slug-qualquer')
        for tag in ig.HASHTAGS_BASE:
            self.assertIn(f'#{tag}', cap)


# ---------------------------------------------------------------------------
# _token — ausência de arquivo deve encerrar com sys.exit
# ---------------------------------------------------------------------------

class TestToken(unittest.TestCase):
    def test_token_ausente_causa_sys_exit(self):
        """Sem token_file e sem token_json → sys.exit (fluxo de erro claro)."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            with (mock.patch.object(ig, 'TOKEN_FILE', tmp / 'instagram_token.txt'),
                  mock.patch.object(ig, 'TOKEN_JSON', tmp / 'instagram_token.json')):
                with self.assertRaises(SystemExit):
                    ig._token()

    def test_token_arquivo_presente_retorna_conteudo(self):
        """Com token_file válido → retorna o token sem sys.exit."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            token_file = tmp / 'instagram_token.txt'
            token_file.write_text('meu-token-ficticio', encoding='utf-8')
            with (mock.patch.object(ig, 'TOKEN_FILE', token_file),
                  mock.patch.object(ig, 'TOKEN_JSON', tmp / 'instagram_token.json')):
                resultado = ig._token()
        self.assertEqual(resultado, 'meu-token-ficticio')

    def test_token_json_valido_retorna_sem_renovar(self):
        """token_json com _obtained_at recente → retorna token do JSON sem renovar."""
        import time, json
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            tj = {
                'access_token': 'token-do-json',
                '_obtained_at': int(time.time()),   # agora → não expirado
                'expires_in': 5184000,              # 60 dias
            }
            token_json = tmp / 'instagram_token.json'
            token_json.write_text(json.dumps(tj), encoding='utf-8')
            with mock.patch.object(ig, 'TOKEN_JSON', token_json):
                resultado = ig._token()
        self.assertEqual(resultado, 'token-do-json')


# ---------------------------------------------------------------------------
# _user_id — ausência de arquivo deve encerrar com sys.exit
# ---------------------------------------------------------------------------

class TestUserId(unittest.TestCase):
    def test_user_id_ausente_causa_sys_exit(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            with mock.patch.object(ig, 'USER_ID_FILE', tmp / 'instagram_user_id.txt'):
                with self.assertRaises(SystemExit):
                    ig._user_id()

    def test_user_id_presente_retorna_conteudo(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            uid_file = tmp / 'instagram_user_id.txt'
            uid_file.write_text('1234567890', encoding='utf-8')
            with mock.patch.object(ig, 'USER_ID_FILE', uid_file):
                resultado = ig._user_id()
        self.assertEqual(resultado, '1234567890')


# ---------------------------------------------------------------------------
# COVER_OFFSET_MS — constante de capa
# ---------------------------------------------------------------------------

class TestCoverOffset(unittest.TestCase):
    def test_constante_existe(self):
        self.assertTrue(hasattr(ig, 'COVER_OFFSET_MS'))

    def test_valor_proximo_de_1500(self):
        """Deve ser ~1500ms para pular o fade-in preto (~0,45s) com margem."""
        self.assertGreaterEqual(ig.COVER_OFFSET_MS, 1000)
        self.assertLessEqual(ig.COVER_OFFSET_MS, 3000)

    def test_e_numero_inteiro_ou_float(self):
        self.assertIsInstance(ig.COVER_OFFSET_MS, (int, float))


# ---------------------------------------------------------------------------
# post_reel — rota video_url (rupload por bytes abandonado, 21/jun/26)
# Rede/scp/_post mockados: pin do CONTRATO, não chamada real à Graph API.
# ---------------------------------------------------------------------------

class TestPostReel(unittest.TestCase):
    def _post_reel(self, mp4='/tmp/x_00.mp4', caption='legenda', **kw):
        """Roda post_reel com toda a borda (token/uid/scp/_post/_get/sleep) mockada.
        Devolve (media_id, lista de chamadas (path, params) feitas a _post)."""
        chamadas = []

        def fake_post(path, token, params):
            chamadas.append((path, params))
            if path.endswith('/media'):
                return {'id': 'CONTAINER123'}
            if path.endswith('/media_publish'):
                return {'id': 'MEDIA456'}
            return {}

        with (mock.patch.object(ig, '_token', return_value='tok'),
              mock.patch.object(ig, '_user_id', return_value='999'),
              mock.patch.object(ig, '_scp_video',
                                return_value='https://www.andregalgani.com.br/biblioteca/_reels/x_00.mp4') as scp,
              mock.patch.object(ig, '_post', side_effect=fake_post),
              mock.patch.object(ig, '_get', return_value={'status_code': 'FINISHED'}),
              mock.patch.object(ig.time, 'sleep')):
            mid = ig.post_reel(mp4, caption, **kw)
        self.scp = scp
        return mid, chamadas

    def _container_params(self, chamadas):
        return next(p for path, p in chamadas if path.endswith('/media'))

    def test_hospeda_o_mp4_via_scp_video(self):
        """A mídia é hospedada na VPS (rota video_url), não enviada por bytes."""
        _, _ = self._post_reel(mp4='/tmp/x_00.mp4')
        self.scp.assert_called_once_with('/tmp/x_00.mp4')

    def test_container_usa_video_url(self):
        _, chamadas = self._post_reel()
        params = self._container_params(chamadas)
        self.assertEqual(params['media_type'], 'REELS')
        self.assertIn('video_url', params)
        self.assertTrue(params['video_url'].startswith('https://'))

    def test_container_nao_usa_upload_resumavel(self):
        """Regressão: a rota rupload (upload_type=resumable) foi abandonada."""
        _, chamadas = self._post_reel()
        params = self._container_params(chamadas)
        self.assertNotIn('upload_type', params)

    def test_repassa_caption_e_thumb_offset(self):
        _, chamadas = self._post_reel(caption='minha legenda', thumb_offset=1500)
        params = self._container_params(chamadas)
        self.assertEqual(params['caption'], 'minha legenda')
        self.assertEqual(params['thumb_offset'], '1500')

    def test_share_to_feed_false_vira_string(self):
        _, chamadas = self._post_reel(share_to_feed=False)
        params = self._container_params(chamadas)
        self.assertEqual(params['share_to_feed'], 'false')

    def test_publica_com_creation_id_do_container(self):
        mid, chamadas = self._post_reel()
        self.assertEqual(mid, 'MEDIA456')
        pub = next(p for path, p in chamadas if path.endswith('/media_publish'))
        self.assertEqual(pub['creation_id'], 'CONTAINER123')

    def test_erro_no_container_retorna_none_sem_publicar(self):
        with (mock.patch.object(ig, '_token', return_value='tok'),
              mock.patch.object(ig, '_user_id', return_value='999'),
              mock.patch.object(ig, '_scp_video', return_value='https://x/y.mp4'),
              mock.patch.object(ig, '_post', return_value={'error': {'message': 'falhou'}}) as p,
              mock.patch.object(ig.time, 'sleep')):
            mid = ig.post_reel('/tmp/x_00.mp4', 'legenda')
        self.assertIsNone(mid)
        # só a tentativa de contêiner; media_publish não é chamado
        self.assertTrue(all(c.args[0].endswith('/media') for c in p.call_args_list))


if __name__ == '__main__':
    unittest.main()
