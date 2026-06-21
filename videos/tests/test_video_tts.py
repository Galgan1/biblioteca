# -*- coding: utf-8 -*-
"""Testes herméticos das funções PURAS do cluster TTS/voz.

Rodados contra gerar_video (estado atual) para provar que os contratos
existem ANTES da extração — depois apontamos para _video_tts.

Suíte:
  TestToSsml  — _to_ssml(): transformações de pontuação → <break>
"""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import _video_tts as _mod


class TestToSsml(unittest.TestCase):
    """_to_ssml(text) -> '<speak>…</speak>' com <break> nos pontos de prosódia."""

    def _ssml(self, text):
        return _mod._to_ssml(text)

    # ── estrutura básica ────────────────────────────────────────────────────
    def test_envolve_em_speak(self):
        out = self._ssml('Olá mundo.')
        self.assertTrue(out.startswith('<speak>'))
        self.assertTrue(out.endswith('</speak>'))

    def test_texto_vazio(self):
        out = self._ssml('')
        self.assertEqual(out, '<speak></speak>')

    # ── vírgula: micro-pausa de fraseado ────────────────────────────────────
    def test_virgula_injeta_break_150ms(self):
        """', ' → ',<break time="150ms"/> ' (o salto premium de prosódia)."""
        out = self._ssml('Leia, escreva e aprenda.')
        self.assertIn(',<break time="150ms"/> ', out)

    def test_virgula_sem_espaco_nao_injeta(self):
        """Vírgula SEM espaço seguinte NÃO deve injetar pausa (evita falso positivo)."""
        out = self._ssml('número,sem_espaço')
        self.assertNotIn('<break', out)

    # ── ponto final ─────────────────────────────────────────────────────────
    def test_ponto_injeta_break_400ms(self):
        out = self._ssml('Fim de frase. Próxima.')
        self.assertIn('.<break time="400ms"/> ', out)

    # ── ponto de interrogação ───────────────────────────────────────────────
    def test_interrogacao_injeta_break_560ms(self):
        out = self._ssml('O que fazer? Depende.')
        self.assertIn('?<break time="560ms"/> ', out)

    # ── exclamação ──────────────────────────────────────────────────────────
    def test_exclamacao_injeta_break_440ms(self):
        out = self._ssml('Incrível! Veja isto.')
        self.assertIn('!<break time="440ms"/> ', out)

    # ── ponto-e-vírgula ─────────────────────────────────────────────────────
    def test_ponto_virgula_injeta_break_300ms(self):
        out = self._ssml('Primeiro; segundo.')
        self.assertIn(';<break time="300ms"/> ', out)

    # ── travessão ───────────────────────────────────────────────────────────
    def test_travessao_injeta_break_330ms(self):
        out = self._ssml('A decisão — a grande decisão — foi tomada.')
        self.assertIn(' —<break time="330ms"/> ', out)

    # ── reticências ─────────────────────────────────────────────────────────
    def test_reticencias_3pontos_injeta_break_500ms(self):
        out = self._ssml('Será... que sim?')
        self.assertIn('…<break time="500ms"/> ', out)

    def test_reticencias_unicode_injeta_break_500ms(self):
        out = self._ssml('Talvez… não.')
        self.assertIn('…<break time="500ms"/> ', out)

    # ── escaping HTML ────────────────────────────────────────────────────────
    def test_ampersand_escapado(self):
        """& é escapado para &amp; (html.escape). O '; ' do &amp; também aciona
        o replace de ponto-e-vírgula — isso é comportamento atual, não bug."""
        out = self._ssml('sal & pimenta.')
        self.assertIn('&amp;', out)

    def test_menor_escapado(self):
        """< é escapado para &lt;. O ; em &lt; aciona break de ponto-e-vírgula."""
        out = self._ssml('x < y.')
        self.assertIn('&lt;', out)

    def test_maior_escapado(self):
        """> é escapado para &gt;. O ; em &gt; aciona break de ponto-e-vírgula."""
        out = self._ssml('x > y.')
        self.assertIn('&gt;', out)

    # ── múltiplas pausas ─────────────────────────────────────────────────────
    def test_multiplas_pausas_na_mesma_frase(self):
        """Texto complexo: todas as pontuações presentes ao mesmo tempo."""
        out = self._ssml('Sim, claro! E depois? Então; é isso — pronto.')
        self.assertIn(',<break time="150ms"/> ', out)
        self.assertIn('!<break time="440ms"/> ', out)
        self.assertIn('?<break time="560ms"/> ', out)
        self.assertIn(';<break time="300ms"/> ', out)
        self.assertIn(' —<break time="330ms"/> ', out)


class TestElevenAntiFantasma(unittest.TestCase):
    """_tts_eleven: HTTP 200 com corpo vazio NÃO é sucesso (não grava fantasma)."""

    def test_corpo_vazio_retorna_false(self):
        import os, types
        from unittest import mock
        resp = mock.Mock()
        resp.content = b''                      # 200, mas sem áudio
        resp.raise_for_status = mock.Mock()     # não levanta
        fake_req = types.ModuleType('requests')
        fake_req.post = mock.Mock(return_value=resp)
        with mock.patch.dict(os.environ, {'ELEVENLABS_API_KEY': 'k'}, clear=False), \
             mock.patch.dict(sys.modules, {'requests': fake_req}), \
             mock.patch.object(Path, 'write_bytes') as m_write:
            self.assertFalse(_mod._tts_eleven('texto', 'voiceid', '/tmp/_x.mp3'))
            m_write.assert_not_called()          # nenhum arquivo-fantasma gravado


class TestTtsRotaFinalEdge(unittest.TestCase):
    """tts() na rota edge (voz pt-BR-AntonioNeural pula eleven/google):
    falha do edge ABORTA com contexto; saída vazia ABORTA; sucesso não levanta."""

    def test_edge_falha_aborta_com_contexto(self):
        from unittest import mock
        def boom(cmd, **k):
            raise _mod.subprocess.CalledProcessError(1, cmd, stderr=b'No internet connection')
        with mock.patch.object(_mod.subprocess, 'run', boom):
            with self.assertRaises(RuntimeError) as ctx:
                _mod.tts('texto', 'pt-BR-AntonioNeural', '/tmp/_x.mp3')
        self.assertIn('edge-tts', str(ctx.exception))     # erro diagnosticável, não CalledProcessError cru

    def test_edge_arquivo_vazio_aborta(self):
        import os, tempfile
        from unittest import mock
        with tempfile.TemporaryDirectory() as d:
            out = os.path.join(d, 'a.mp3')
            def fake_run(cmd, **k):
                open(out, 'wb').close()           # rc=0 mas 0 byte (fantasma)
                return mock.Mock()
            with mock.patch.object(_mod.subprocess, 'run', fake_run):
                with self.assertRaises(RuntimeError):
                    _mod.tts('texto', 'pt-BR-AntonioNeural', out)

    def test_edge_sucesso_nao_aborta(self):
        import os, tempfile
        from unittest import mock
        with tempfile.TemporaryDirectory() as d:
            out = os.path.join(d, 'a.mp3')
            def fake_run(cmd, **k):
                with open(out, 'wb') as f:
                    f.write(b'\x00' * (_mod._AUDIO_MIN_BYTES + 64))
                return mock.Mock()
            with mock.patch.object(_mod.subprocess, 'run', fake_run):
                try:
                    _mod.tts('texto', 'pt-BR-AntonioNeural', out)
                except Exception as e:
                    self.fail(f'tts edge com áudio válido levantou: {e}')


class TestDespirTags(unittest.TestCase):
    """_despir_tags: remove audio tags v3 (p/ Google/edge não FALAREM 'serious'), mantém o texto."""

    def test_remove_tags_conhecidas(self):
        out = _mod._despir_tags('[serious] Texto. [pause] Mais texto.')
        self.assertNotIn('[', out)
        self.assertIn('Texto', out)
        self.assertIn('Mais texto', out)

    def test_texto_plano_intacto(self):
        self.assertEqual(_mod._despir_tags('Sem tags aqui.'), 'Sem tags aqui.')

    def test_vazio(self):
        self.assertEqual(_mod._despir_tags(''), '')


class TestNormalizaFala(unittest.TestCase):
    """normaliza_fala: siglas não-palavra soletradas, símbolos expandidos, idempotente."""

    def test_sigla_soletrada(self):
        self.assertIn('ó cê dê é', _mod.normaliza_fala('A OCDE alertou.'))

    def test_sigla_palavra_intacta(self):
        # UNESCO/INGSOC são lidas inteiras → NÃO entram na allowlist (soletrar seria erro).
        self.assertIn('UNESCO', _mod.normaliza_fala('A UNESCO publicou.'))
        self.assertIn('INGSOC', _mod.normaliza_fala('O INGSOC governa.'))

    def test_simbolos_expandidos(self):
        self.assertIn('por cento', _mod.normaliza_fala('Caiu 3%.'))
        self.assertIn('reais', _mod.normaliza_fala('Custa R$ 1500 hoje.'))

    def test_idempotente_e_vazio(self):
        once = _mod.normaliza_fala('A OCDE caiu 3%.')
        self.assertEqual(_mod.normaliza_fala(once), once)
        self.assertEqual(_mod.normaliza_fala(''), '')


class TestIntonarIdempotenciaPrecisa(unittest.TestCase):
    """_intonar: só tag v3 CONHECIDA é 'já dirigido'; colchete estranho não silencia a injeção."""

    def test_colchete_desconhecido_nao_silencia(self):
        # '[risos]' não é audio tag → o texto AINDA recebe direção (antes ficava mudo).
        out = _mod._intonar('[risos] Algo aconteceu. Preste atenção.', tom='serio')
        self.assertIn('[serious]', out)

    def test_tag_conhecida_preserva_intacto(self):
        ja = '[deliberate] A regra é clara. [pause] Repare nela.'
        self.assertEqual(_mod._intonar(ja, tom='serio'), ja)


class TestEdgeSanitiza(unittest.TestCase):
    """tts() na rota edge: texto com tags chega ao edge-tts SEM colchetes (voz não fala 'serious')."""

    def test_edge_recebe_texto_limpo(self):
        import os, tempfile
        from unittest import mock
        capt = {}
        with tempfile.TemporaryDirectory() as d:
            out = os.path.join(d, 'a.mp3')
            def fake_run(cmd, **k):
                capt['cmd'] = cmd
                with open(out, 'wb') as f:
                    f.write(b'\x00' * (_mod._AUDIO_MIN_BYTES + 64))
                return mock.Mock()
            with mock.patch.object(_mod.subprocess, 'run', fake_run):
                _mod.tts('[serious] Texto importante. [pause] Fim.', 'pt-BR-AntonioNeural', out)
            cmd = capt['cmd']
            arg_texto = cmd[cmd.index('--text') + 1]
            self.assertNotIn('[', arg_texto)        # tags removidas
            self.assertIn('Texto importante', arg_texto)


if __name__ == '__main__':
    unittest.main()
