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


if __name__ == '__main__':
    unittest.main()
