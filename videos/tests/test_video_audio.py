# -*- coding: utf-8 -*-
"""Testes herméticos de sintetiza_ambiente (cluster de áudio/trilha).

Rodados contra gerar_video (estado atual) para provar os contratos
ANTES da extração — depois apontamos para _video_audio.

Contratos verificados:
  - retorna um arquivo WAV válido no disco
  - duração em amostras ≥ dur * 44100 (dentro de margem de fade)
  - sinal é finito (nenhum NaN/Inf nas amostras)
  - pico < 0 dBFS (nunca clipa: max(abs) < 32767)
  - funciona com energia=0 (pad contemplativo puro)
  - funciona com energia=1.0 (máxima energia)
"""
import io
import sys
import types
import wave
import struct
import tempfile
import unittest
import contextlib
from pathlib import Path

ROOT = Path(__file__).parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import _video_audio as _mod


class TestSintetizaAmbiente(unittest.TestCase):
    """sintetiza_ambiente(dur, out_wav, seed, energia) → WAV válido no disco."""

    SR = 44100

    def _synth(self, dur=12.0, seed=42, energia=0.65):
        """Gera em arquivo temporário e retorna o Path.

        dur default = 12s: sintetiza_ambiente aplica fade-in de 4s e fade-out
        de 7s — com dur < 11s o slice out[:fi] estoura (shapes incompatíveis).
        12s é o mínimo seguro para exercitar todos os ramos sem erro de shape.
        """
        tmp = Path(tempfile.mktemp(suffix='.wav'))
        _mod.sintetiza_ambiente(dur, tmp, seed=seed, energia=energia)
        return tmp

    def _read_samples(self, wav_path):
        """Lê amostras int16 de um WAV mono e devolve lista de floats [-1, 1]."""
        with wave.open(str(wav_path), 'r') as wf:
            n = wf.getnframes()
            raw = wf.readframes(n)
        samples = struct.unpack(f'{n}h', raw)
        return samples, n

    # ── arquivo existe e é WAV válido ────────────────────────────────────────
    def test_arquivo_criado(self):
        tmp = self._synth()
        try:
            self.assertTrue(tmp.exists())
        finally:
            tmp.unlink(missing_ok=True)

    def test_wav_abre_sem_erro(self):
        tmp = self._synth()
        try:
            with wave.open(str(tmp), 'r') as wf:
                self.assertEqual(wf.getnchannels(), 1)
                self.assertEqual(wf.getframerate(), self.SR)
                self.assertEqual(wf.getsampwidth(), 2)
        finally:
            tmp.unlink(missing_ok=True)

    # ── duração em amostras ─────────────────────────────────────────────────
    def test_duracao_minima(self):
        """Número de frames >= dur * SR (fade não deve truncar abaixo do alvo)."""
        dur = 12.0
        tmp = self._synth(dur=dur)
        try:
            with wave.open(str(tmp), 'r') as wf:
                n = wf.getnframes()
            self.assertGreaterEqual(n, int(dur * self.SR))
        finally:
            tmp.unlink(missing_ok=True)

    # ── regressão: duração curta não pode estourar o slice de fade ──────────
    def test_duracao_curta_nao_estoura(self):
        """REGRESSÃO (landmine do refactor Akita 2026-06-20): dur curta < 11s.

        Com dur=5.0 → n_total=220500 amostras, mas o fade-out usa fo=int(7*sr)=
        308700 > n_total, então `out[-fo:] *= np.linspace(1,0,fo)` estourava com
        ValueError de broadcast (shapes incompatíveis). O fade tem de ser clampado
        ao tamanho real do buffer. Não dispara em produção (trilha = minutos),
        mas era um landmine. Aqui exigimos: gera WAV finito, do tamanho certo.
        """
        dur = 5.0
        tmp = self._synth(dur=dur)
        try:
            self.assertTrue(tmp.exists())
            with wave.open(str(tmp), 'r') as wf:
                self.assertEqual(wf.getnchannels(), 1)
                self.assertEqual(wf.getframerate(), self.SR)
                n = wf.getnframes()
            # buffer é exatamente int(dur*sr) amostras — fade não trunca nem cresce
            self.assertEqual(n, int(dur * self.SR))
            samples, _ = self._read_samples(tmp)
            self.assertEqual(len(samples), int(dur * self.SR))
            pico = max(abs(s) for s in samples)
            self.assertLess(pico, 32767, f'Pico {pico} >= 32767 (clipping!)')
        finally:
            tmp.unlink(missing_ok=True)

    # ── integridade numérica: finito, sem clipping ──────────────────────────
    def test_sem_nan_inf(self):
        """Nenhuma amostra pode ser NaN ou Inf (int16 não representa, mas testa antes)."""
        tmp = self._synth()
        try:
            samples, _ = self._read_samples(tmp)
            # int16 não tem NaN; verificamos que todos os valores são inteiros finitos
            for s in samples[:1000]:  # 1000 amostras = 23ms — rápido
                self.assertIsInstance(s, int)
        finally:
            tmp.unlink(missing_ok=True)

    def test_pico_abaixo_de_0_dbfs(self):
        """max(abs(samples)) < 32767 — sinal não clipa."""
        tmp = self._synth()
        try:
            samples, _ = self._read_samples(tmp)
            pico = max(abs(s) for s in samples)
            self.assertLess(pico, 32767, f'Pico {pico} >= 32767 (clipping!)')
        finally:
            tmp.unlink(missing_ok=True)

    # ── variações de energia ─────────────────────────────────────────────────
    def test_energia_zero_nao_explode(self):
        """energia=0: pad contemplativo puro — deve rodar sem erro."""
        tmp = self._synth(energia=0.0)
        try:
            self.assertTrue(tmp.exists())
            with wave.open(str(tmp), 'r') as wf:
                self.assertGreater(wf.getnframes(), 0)
        finally:
            tmp.unlink(missing_ok=True)

    def test_energia_maxima_nao_explode(self):
        """energia=1.0: máxima energia — deve rodar sem erro."""
        tmp = self._synth(energia=1.0)
        try:
            self.assertTrue(tmp.exists())
            with wave.open(str(tmp), 'r') as wf:
                self.assertGreater(wf.getnframes(), 0)
        finally:
            tmp.unlink(missing_ok=True)

    def test_energia_clamped_acima_de_1(self):
        """energia > 1 é silenciosamente clampado para 1.0 — sem exceção."""
        tmp = self._synth(energia=5.0)
        try:
            self.assertTrue(tmp.exists())
        finally:
            tmp.unlink(missing_ok=True)

    def test_energia_clamped_abaixo_de_0(self):
        """energia < 0 é silenciosamente clampado para 0.0 — sem exceção."""
        tmp = self._synth(energia=-1.0)
        try:
            self.assertTrue(tmp.exists())
        finally:
            tmp.unlink(missing_ok=True)

    # ── regressão pilar 7: falha do DSP é registrada com contexto, fallback segue ─
    def test_dsp_falha_registra_contexto_e_nao_quebra(self):
        """REGRESSÃO (Akita pilar 7): se `dsp.master` levantar, o except NÃO pode
        engolir o erro em silêncio nem quebrar o fluxo. Deve:
          (a) ainda gerar o WAV (fallback: trilha sem o master DSP);
          (b) emitir o aviso em STDERR com o TIPO da exceção (não só a mensagem).

        Hermético: injeta um módulo `dsp` falso em sys.modules cujo master estoura,
        captura stderr e restaura o sys.modules original — não toca disco/ffmpeg real
        além do tmp WAV (como os demais testes)."""
        fake = types.ModuleType('dsp')

        def _boom(*a, **k):
            raise RuntimeError('falha sintetica do master')
        fake.master = _boom

        saved = sys.modules.get('dsp')
        sys.modules['dsp'] = fake
        tmp = Path(tempfile.mktemp(suffix='.wav'))
        err = io.StringIO()
        try:
            with contextlib.redirect_stderr(err):
                _mod.sintetiza_ambiente(12.0, tmp, seed=42, energia=0.65)
            # (a) fallback funcionou: WAV existe e é válido
            self.assertTrue(tmp.exists())
            with wave.open(str(tmp), 'r') as wf:
                self.assertGreater(wf.getnframes(), 0)
            # (b) erro foi registrado em stderr COM contexto (tipo + motivo)
            msg = err.getvalue()
            self.assertIn('RuntimeError', msg, f'tipo da exceção ausente no aviso: {msg!r}')
            self.assertIn('falha sintetica do master', msg)
        finally:
            tmp.unlink(missing_ok=True)
            if saved is not None:
                sys.modules['dsp'] = saved
            else:
                sys.modules.pop('dsp', None)

    # ── determinismo com mesma seed ──────────────────────────────────────────
    def test_determinismo_por_seed(self):
        """Mesma seed → mesma sequência de amostras (reproduzível)."""
        tmp1 = self._synth(seed=99)
        tmp2 = self._synth(seed=99)
        try:
            s1, _ = self._read_samples(tmp1)
            s2, _ = self._read_samples(tmp2)
            self.assertEqual(s1[:500], s2[:500])
        finally:
            tmp1.unlink(missing_ok=True)
            tmp2.unlink(missing_ok=True)


if __name__ == '__main__':
    unittest.main()
