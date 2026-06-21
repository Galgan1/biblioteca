# -*- coding: utf-8 -*-
"""Testes da lógica de roteamento de provedor de voz e do helper ElevenLabs.

Cobrem funções PURAS — sem tocar disco, rede ou API paga.

Suíte:
  TestProvedorVoz        — _provedor_voz() para as 3 rotas (eleven / google / edge)
  TestTtsElevenSemChave  — _tts_eleven() sem chave cai na rota de fuga (edge-tts)
  TestTtsElevenMockado   — _tts_eleven() com chave presente usa requests (mockado)
"""
import os
import sys
import types
import unittest
from pathlib import Path
from unittest import mock

# Garante que o pacote raiz seja encontrado (mesmo sem instalar)
ROOT = Path(__file__).parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import gerar_video


class TestProvedorVoz(unittest.TestCase):
    """_provedor_voz(voice) -> 'eleven' | 'google' | 'edge'"""

    # --- rota eleven ---
    def test_prefixo_eleven_colon(self):
        self.assertEqual(gerar_video._provedor_voz('eleven:Rachel'), 'eleven')

    def test_prefixo_el_colon(self):
        self.assertEqual(gerar_video._provedor_voz('el:21m00Tcm4TlvDq8ikWAM'), 'eleven')

    def test_prefixo_el_maiusculo(self):
        # case-insensitive no prefixo
        self.assertEqual(gerar_video._provedor_voz('EL:algum-id'), 'eleven')

    def test_prefixo_eleven_maiusculo(self):
        self.assertEqual(gerar_video._provedor_voz('ELEVEN:Rachel'), 'eleven')

    # --- rota google ---
    def test_chirp3_google(self):
        self.assertEqual(gerar_video._provedor_voz('pt-BR-Chirp3-HD-Iapetus'), 'google')

    def test_studio_google(self):
        self.assertEqual(gerar_video._provedor_voz('pt-BR-Studio-B'), 'google')

    def test_neural2_google(self):
        self.assertEqual(gerar_video._provedor_voz('pt-BR-Neural2-A'), 'google')

    def test_wavenet_google(self):
        self.assertEqual(gerar_video._provedor_voz('pt-BR-Wavenet-A'), 'google')

    # --- rota edge ---
    def test_edge_antonio(self):
        self.assertEqual(gerar_video._provedor_voz('pt-BR-AntonioNeural'), 'edge')

    def test_edge_francisca(self):
        self.assertEqual(gerar_video._provedor_voz('pt-BR-FranciscaNeural'), 'edge')

    def test_edge_string_arbitraria(self):
        self.assertEqual(gerar_video._provedor_voz('qualquer-coisa'), 'edge')

    def test_edge_string_vazia(self):
        self.assertEqual(gerar_video._provedor_voz(''), 'edge')


class TestTtsElevenSemChave(unittest.TestCase):
    """Sem chave ElevenLabs → cai na rota de fuga (edge-tts), sem lançar exceção."""

    def _call_sem_chave(self, out_mp3):
        """Chama _tts_eleven garantindo ausência de chave no env e no disco.

        Faz o patch apenas em 'gerar_video.ROOT' para que o caminho do segredo
        aponte para um diretório temporário sem o arquivo, evitando interferir
        com outros Path.read_text chamados durante o import do módulo.
        """
        import tempfile
        with tempfile.TemporaryDirectory() as tmpdir:
            # ROOT sem pasta .secrets → read_text lança FileNotFoundError
            fake_root = Path(tmpdir)
            with mock.patch.dict(os.environ, {'ELEVENLABS_API_KEY': ''}, clear=False):
                with mock.patch.object(gerar_video, 'ROOT', fake_root):
                    result = gerar_video._tts_eleven(
                        text='Teste sem chave.',
                        voice_id='Rachel',
                        out_mp3=str(out_mp3),
                    )
        return result, None

    def test_sem_chave_retorna_false(self):
        """_tts_eleven sem chave deve retornar False (sinaliza fallback necessário)."""
        out = Path('/tmp/test_eleven_sem_chave.mp3')
        resultado, _ = self._call_sem_chave(out)
        self.assertFalse(resultado)

    def test_sem_chave_nao_lanca_excecao(self):
        """_tts_eleven sem chave NÃO deve lançar exceção — nunca quebra o build."""
        out = Path('/tmp/test_eleven_sem_chave2.mp3')
        try:
            self._call_sem_chave(out)
        except Exception as e:
            self.fail(f'_tts_eleven lançou exceção inesperada: {e}')


class TestTtsElevenMockado(unittest.TestCase):
    """Com chave presente e requests mockado — verifica que a API é chamada corretamente."""

    def _make_mock_requests(self, status_code=200, content=b'ID3fake_mp3_data'):
        """Cria um módulo requests falso que retorna uma resposta controlada."""
        resp = mock.Mock()
        resp.status_code = status_code
        resp.content = content
        resp.raise_for_status = mock.Mock(
            side_effect=None if status_code == 200
            else Exception(f'HTTP {status_code}')
        )

        fake_requests = types.ModuleType('requests')
        fake_requests.post = mock.Mock(return_value=resp)
        return fake_requests

    def _call_com_chave(self, out_mp3, fake_requests, chave='fake-key-1234'):
        """Chama _tts_eleven injetando chave via env e requests mockado."""
        with mock.patch.dict(os.environ, {'ELEVENLABS_API_KEY': chave}, clear=False):
            with mock.patch.dict(sys.modules, {'requests': fake_requests}):
                # Patch write_bytes para não tocar disco
                with mock.patch.object(Path, 'write_bytes'):
                    resultado = gerar_video._tts_eleven(
                        text='Olá mundo.',
                        voice_id='21m00Tcm4TlvDq8ikWAM',
                        out_mp3=str(out_mp3),
                    )
        return resultado

    def test_sucesso_retorna_true(self):
        out = Path('/tmp/test_eleven_ok.mp3')
        fake_req = self._make_mock_requests(200)
        resultado = self._call_com_chave(out, fake_req)
        self.assertTrue(resultado)

    def test_sucesso_chama_post(self):
        out = Path('/tmp/test_eleven_post.mp3')
        fake_req = self._make_mock_requests(200)
        self._call_com_chave(out, fake_req)
        self.assertTrue(fake_req.post.called)

    def test_sucesso_url_contem_voice_id(self):
        out = Path('/tmp/test_eleven_url.mp3')
        fake_req = self._make_mock_requests(200)
        self._call_com_chave(out, fake_req, chave='k')
        url_chamada = fake_req.post.call_args[0][0]
        self.assertIn('21m00Tcm4TlvDq8ikWAM', url_chamada)

    def test_sucesso_header_tem_chave(self):
        out = Path('/tmp/test_eleven_header.mp3')
        fake_req = self._make_mock_requests(200)
        self._call_com_chave(out, fake_req, chave='minha-chave-secreta')
        kwargs = fake_req.post.call_args[1]
        headers = kwargs.get('headers', {})
        self.assertIn('minha-chave-secreta', headers.get('xi-api-key', ''))

    def test_erro_api_retorna_false(self):
        """Falha na API ElevenLabs → retorna False (permite fallback no chamador)."""
        out = Path('/tmp/test_eleven_err.mp3')
        fake_req = self._make_mock_requests(500)
        fake_req.post.side_effect = Exception('conexão recusada')
        with mock.patch.dict(os.environ, {'ELEVENLABS_API_KEY': 'k'}, clear=False):
            with mock.patch.dict(sys.modules, {'requests': fake_req}):
                resultado = gerar_video._tts_eleven(
                    text='Erro.',
                    voice_id='Rachel',
                    out_mp3=str(out),
                )
        self.assertFalse(resultado)

    def test_usa_modelo_eleven_v3(self):
        """A intonação só funciona no eleven_v3 — o payload DEVE usar esse modelo."""
        out = Path('/tmp/test_eleven_v3.mp3')
        fake_req = self._make_mock_requests(200)
        self._call_com_chave(out, fake_req)
        payload = fake_req.post.call_args[1]['json']
        self.assertEqual(payload['model_id'], 'eleven_v3')

    def test_aplica_intonar_no_texto(self):
        """Texto plano enviado ao ElevenLabs DEVE sair com audio tag de intonação."""
        out = Path('/tmp/test_eleven_tag.mp3')
        fake_req = self._make_mock_requests(200)
        self._call_com_chave(out, fake_req)   # _call usa text='Olá mundo.'
        payload = fake_req.post.call_args[1]['json']
        self.assertIn('[', payload['text'])   # alguma tag foi injetada


class TestIntonar(unittest.TestCase):
    """_intonar() injeta audio tags v3 em texto plano e é idempotente."""

    def test_injeta_tom_e_pausa(self):
        out = gerar_video._intonar('Você desconfia. Bem. Pascal reuniu as provas.', tom='serio')
        self.assertIn('[serious]', out)
        self.assertIn('[pause]', out)

    def test_idempotente_se_ja_dirigido(self):
        ja = '[serious] A instrução foi trocada. [pause] Está nos documentos.'
        self.assertEqual(gerar_video._intonar(ja, tom='serio'), ja)

    def test_pergunta_retorica_ganha_pausa(self):
        out = gerar_video._intonar('Qual o segredo? A liberdade percebida.', tom='neutro')
        self.assertIn('? [pause]', out)

    def test_vazio_continua_vazio(self):
        self.assertEqual(gerar_video._intonar('', tom='serio'), '')


if __name__ == '__main__':
    unittest.main()
