# -*- coding: utf-8 -*-
"""Testes das funções puras/mockáveis de tiktok_post.py (Akita pilar 2 — verde = exit code).

Cobertura:
  TestCaptionFor       — caption_for(): gancho + CTA + hashtags base + tags do roteiro
  TestToken            — _token(): lê token simples (TOKEN_FILE), lê token do JSON,
                         expira e tenta renovar, arquivo ausente → sys.exit
  TestAfiliadoBlock    — _afiliado_block() de instagram_post: disclosure obrigatória

Todos herméticos: sem rede, sem token real, sem disco real.
"""
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

# Garante que o pacote raiz seja encontrado sem instalar
ROOT = Path(__file__).parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import tiktok_post
import instagram_post


# ---------------------------------------------------------------------------
# Fixtures in-memory
# ---------------------------------------------------------------------------

def _cfg_basico():
    """Roteiro mínimo com 2 cenas e tags no YouTube."""
    return {
        'titulo': 'Habitos Atomicos',
        'slug': 'habitos-atomicos',
        'cenas': [
            {'narracao': 'Cada pequena ação molda quem você se torna. O segredo está nos hábitos atômicos.'},
            {'narracao': 'Identidade antes de metas. Seja a pessoa que já faz isso todo dia.'},
        ],
        'youtube': {
            'tags': ['habitos', 'produtividade', 'desenvolvimento pessoal', 'livros', 'extra-ignorada'],
        },
        'shorts': [0, 1],
    }


def _cfg_sem_tags():
    """Roteiro sem bloco youtube.tags."""
    return {
        'titulo': 'O Príncipe',
        'slug': 'o-principe',
        'cenas': [
            {'narracao': 'O poder não se pede. Se toma com inteligência e timing.'},
        ],
        'shorts': [0],
    }


# ---------------------------------------------------------------------------
# TestCaptionFor
# ---------------------------------------------------------------------------

class TestCaptionFor(unittest.TestCase):
    """caption_for(cfg, idx) → legenda TikTok: gancho + CTA + hashtags."""

    def test_retorna_string_nao_vazia(self):
        cap = tiktok_post.caption_for(_cfg_basico(), 0)
        self.assertIsInstance(cap, str)
        self.assertTrue(cap.strip())

    def test_gancho_e_primeira_frase_da_narracao(self):
        """A 1ª frase da narração deve abrir a legenda (gancho)."""
        cfg = _cfg_basico()
        narracao = cfg['cenas'][0]['narracao']
        gancho_esperado = 'Cada pequena ação molda quem você se torna.'
        cap = tiktok_post.caption_for(cfg, 0)
        self.assertTrue(cap.startswith(gancho_esperado),
                        f'legenda não começa com o gancho esperado.\nLegenda: {cap!r}')

    def test_cta_menciona_titulo_e_canal(self):
        """A legenda deve mencionar o título do livro e o canal Minuto Real."""
        cfg = _cfg_basico()
        cap = tiktok_post.caption_for(cfg, 0)
        self.assertIn('Habitos Atomicos', cap)
        self.assertIn('Minuto Real', cap)

    def test_hashtags_base_presentes(self):
        """Todas as hashtags base do módulo devem aparecer."""
        cfg = _cfg_basico()
        cap = tiktok_post.caption_for(cfg, 0)
        for tag in tiktok_post.HASHTAGS_BASE:
            self.assertIn('#' + tag, cap,
                          f'hashtag base #{tag} ausente na legenda')

    def test_tags_do_roteiro_incluidas_ate_4(self):
        """As primeiras 4 tags do roteiro aparecem como hashtags."""
        cfg = _cfg_basico()
        cap = tiktok_post.caption_for(cfg, 0)
        tags_esperadas = ['#habitos', '#produtividade', '#desenvolvimentopessoal', '#livros']
        for t in tags_esperadas:
            self.assertIn(t, cap, f'tag do roteiro {t} ausente na legenda')

    def test_quinta_tag_ignorada(self):
        """Somente as 4 primeiras tags do roteiro entram; a 5ª é ignorada."""
        cfg = _cfg_basico()
        cap = tiktok_post.caption_for(cfg, 0)
        self.assertNotIn('#extra-ignorada', cap)
        self.assertNotIn('#extraignorada', cap)

    def test_sem_tags_usa_so_hashtags_base(self):
        """Roteiro sem youtube.tags: legenda ainda tem as hashtags base."""
        cfg = _cfg_sem_tags()
        cap = tiktok_post.caption_for(cfg, 0)
        for tag in tiktok_post.HASHTAGS_BASE:
            self.assertIn('#' + tag, cap)

    def test_segunda_cena(self):
        """Funciona para idx != 0."""
        cfg = _cfg_basico()
        cap = tiktok_post.caption_for(cfg, 1)
        self.assertIn('Identidade antes de metas.', cap)

    def test_espacos_na_tag_removidos(self):
        """Tags com espaços são convertidas para hashtags sem espaço."""
        cfg = _cfg_basico()
        cap = tiktok_post.caption_for(cfg, 0)
        # 'desenvolvimento pessoal' → '#desenvolvimentopessoal'
        self.assertNotIn('desenvolvimento pessoal', cap)
        self.assertIn('#desenvolvimentopessoal', cap)


# ---------------------------------------------------------------------------
# TestToken
# ---------------------------------------------------------------------------

class TestToken(unittest.TestCase):
    """_token(): caminhos de leitura e saída de emergência."""

    def _patch_paths(self, token_file=None, token_json=None):
        """Retorna context manager que substitui TOKEN_FILE e TOKEN_JSON no módulo."""
        patches = []
        if token_file is not None:
            patches.append(mock.patch.object(tiktok_post, 'TOKEN_FILE', token_file))
        if token_json is not None:
            patches.append(mock.patch.object(tiktok_post, 'TOKEN_JSON', token_json))
        return patches

    def test_le_token_simples_de_arquivo(self):
        """TOKEN_FILE presente, TOKEN_JSON ausente → retorna conteúdo do txt."""
        with tempfile.TemporaryDirectory() as d:
            tf = Path(d) / 'tiktok_token.txt'
            tf.write_text('meu-token-fake\n', encoding='utf-8')
            # TOKEN_JSON aponta para arquivo inexistente
            tj_inexistente = Path(d) / 'tiktok_token.json'
            with mock.patch.object(tiktok_post, 'TOKEN_FILE', tf), \
                 mock.patch.object(tiktok_post, 'TOKEN_JSON', tj_inexistente):
                token = tiktok_post._token()
        self.assertEqual(token, 'meu-token-fake')

    def test_le_access_token_do_json_valido(self):
        """TOKEN_JSON presente e não expirado → retorna access_token do JSON."""
        import time
        with tempfile.TemporaryDirectory() as d:
            tj = Path(d) / 'tiktok_token.json'
            # _obtained_at agora → não expira por 86400 - 300 = 86100s
            dados = {
                'access_token': 'token-do-json',
                'refresh_token': 'refresh-fake',
                'expires_in': 86400,
                '_obtained_at': int(time.time()),
            }
            tj.write_text(json.dumps(dados), encoding='utf-8')
            tf_inexistente = Path(d) / 'tiktok_token.txt'
            with mock.patch.object(tiktok_post, 'TOKEN_JSON', tj), \
                 mock.patch.object(tiktok_post, 'TOKEN_FILE', tf_inexistente):
                token = tiktok_post._token()
        self.assertEqual(token, 'token-do-json')

    def test_json_expirado_chama_refresh(self):
        """TOKEN_JSON expirado (obtido há mais de expires_in - 300s) → chama _refresh."""
        import time
        with tempfile.TemporaryDirectory() as d:
            tj = Path(d) / 'tiktok_token.json'
            dados = {
                'access_token': 'token-velho',
                'refresh_token': 'refresh-fake',
                'expires_in': 3600,
                '_obtained_at': int(time.time()) - 4000,  # já expirou
            }
            tj.write_text(json.dumps(dados), encoding='utf-8')
            with mock.patch.object(tiktok_post, 'TOKEN_JSON', tj), \
                 mock.patch.object(tiktok_post, '_refresh', return_value='token-renovado') as m_refresh:
                token = tiktok_post._token()
        self.assertEqual(token, 'token-renovado')
        m_refresh.assert_called_once()

    def test_arquivo_ausente_causa_sys_exit(self):
        """TOKEN_FILE e TOKEN_JSON ausentes → sys.exit com mensagem útil."""
        with tempfile.TemporaryDirectory() as d:
            tf = Path(d) / 'nao-existe.txt'
            tj = Path(d) / 'nao-existe.json'
            with mock.patch.object(tiktok_post, 'TOKEN_FILE', tf), \
                 mock.patch.object(tiktok_post, 'TOKEN_JSON', tj):
                with self.assertRaises(SystemExit) as ctx:
                    tiktok_post._token()
        # mensagem deve mencionar o caminho ou orientar o usuário
        msg = str(ctx.exception)
        self.assertTrue(
            'token' in msg.lower() or 'acesso' in msg.lower() or 'video.publish' in msg.lower(),
            f'sys.exit sem mensagem orientativa: {msg!r}',
        )

    def test_json_sem_refresh_token_cai_no_txt(self):
        """TOKEN_JSON sem refresh_token → ignora JSON e lê TOKEN_FILE."""
        with tempfile.TemporaryDirectory() as d:
            tj = Path(d) / 'tiktok_token.json'
            # JSON sem refresh_token → bloco if tj.get('refresh_token') falha
            dados = {'access_token': 'incompleto'}
            tj.write_text(json.dumps(dados), encoding='utf-8')
            tf = Path(d) / 'tiktok_token.txt'
            tf.write_text('token-do-arquivo', encoding='utf-8')
            with mock.patch.object(tiktok_post, 'TOKEN_JSON', tj), \
                 mock.patch.object(tiktok_post, 'TOKEN_FILE', tf):
                token = tiktok_post._token()
        self.assertEqual(token, 'token-do-arquivo')


# ---------------------------------------------------------------------------
# TestAfiliadoBlock  (instagram_post._afiliado_block)
# ---------------------------------------------------------------------------

class TestAfiliadoBlock(unittest.TestCase):
    """_afiliado_block(slug) de instagram_post: apenas a disclosure obrigatória."""

    def test_retorna_string_nao_vazia(self):
        resultado = instagram_post._afiliado_block('habitos-atomicos')
        self.assertIsInstance(resultado, str)
        self.assertTrue(resultado.strip())

    def test_contem_disclosure_amazon(self):
        """Disclosure obrigatória de afiliado deve estar presente (palavra 'Amazon')."""
        resultado = instagram_post._afiliado_block('qualquer-slug')
        self.assertIn('Amazon', resultado)

    def test_disclosure_menciona_associado(self):
        """Texto deve mencionar 'Associado' (contrato do programa de afiliados)."""
        resultado = instagram_post._afiliado_block('qualquer-slug')
        self.assertIn('Associado', resultado)

    def test_nao_contem_url_de_busca(self):
        """Legenda de IG não pode ter URL de busca Amazon (/s?k=...) — link só na bio."""
        resultado = instagram_post._afiliado_block('qualquer-slug')
        self.assertNotIn('/s?k=', resultado)
        self.assertNotIn('amazon.com', resultado.lower())

    def test_slug_diferente_mesma_disclosure(self):
        """_afiliado_block é agnóstica ao slug (retorna só a disclosure global)."""
        r1 = instagram_post._afiliado_block('livro-a')
        r2 = instagram_post._afiliado_block('livro-b')
        self.assertEqual(r1, r2)


if __name__ == '__main__':
    unittest.main()
