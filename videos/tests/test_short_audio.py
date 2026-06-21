# -*- coding: utf-8 -*-
"""Testes herméticos do leito de engajamento do Short (`_short_audio.short_bed`).

Fixa os contratos que os 3 autores-juízes pediram (revisão Akita 21/jun):
  - WAV válido, finito, sem clipping (pico < 32767);
  - HOOK: a janela da capa (0→cover) NÃO é silenciosa (evento sônico real) —
    era exatamente o buraco: o Short abria mudo;
  - VOZ SOBERANA: o leito sob a voz (corpo) tem RMS bem abaixo do hook;
  - VETORIZAÇÃO (Chion): dentro do corpo, o leito SOBE rumo ao clímax
    (RMS de um trecho tardio > de um trecho inicial);
  - determinismo por seed.
Sem rede, sem API, sem áudio real — só numpy/WAV no disco temporário.
"""
import sys
import wave
import struct
import tempfile
import unittest
from pathlib import Path

import numpy as np

ROOT = Path(__file__).parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import _short_audio as sa

SR = sa.SR
COVER, LEAD, TOTAL = 2.4, 0.45, 15.0
# pasta inexistente → testa o leito PROCEDURAL puro, sem depender da marca premium
# estar presente no ambiente (determinismo + isola a lógica do short_bed).
_SEM_MARCA = Path('__sem_marca_para_teste__')


def _render(total=TOTAL, cover=COVER, lead=LEAD, seed=7, energia=0.6, reveals=None):
    tmp = Path(tempfile.mktemp(suffix='.wav'))
    sa.short_bed(total, cover, lead, tmp, seed=seed, energia=energia,
                 marca_dir=_SEM_MARCA, reveals=reveals)
    return tmp


def _samples(wav_path):
    with wave.open(str(wav_path), 'r') as wf:
        n = wf.getnframes()
        raw = wf.readframes(n)
    return np.array(struct.unpack(f'{n}h', raw), dtype=np.float64) / 32768.0


def _rms(x):
    return float(np.sqrt(np.mean(x ** 2))) if len(x) else 0.0


class TestShortBed(unittest.TestCase):
    def test_wav_valido_e_comprimento(self):
        tmp = _render()
        try:
            with wave.open(str(tmp), 'r') as wf:
                self.assertEqual(wf.getnchannels(), 1)
                self.assertEqual(wf.getframerate(), SR)
                self.assertEqual(wf.getsampwidth(), 2)
                self.assertEqual(wf.getnframes(), int(TOTAL * SR))
        finally:
            tmp.unlink(missing_ok=True)

    def test_finito_sem_clipping(self):
        tmp = _render()
        try:
            x = _samples(tmp)
            self.assertTrue(np.all(np.isfinite(x)))
            self.assertLess(float(np.max(np.abs(x))) * 32768, 32767)
        finally:
            tmp.unlink(missing_ok=True)

    def test_hook_nao_silencioso(self):
        """A janela da capa (0→cover) tem um evento sônico real — o Short não abre mudo."""
        tmp = _render()
        try:
            x = _samples(tmp)
            hook = x[: int(COVER * SR)]
            self.assertGreater(float(np.max(np.abs(hook))), 0.1)   # pico claro (riser+acento)
            self.assertGreater(_rms(hook), 0.02)                   # energia, não silêncio
        finally:
            tmp.unlink(missing_ok=True)

    def test_voz_soberana_corpo_baixo(self):
        """O leito sob a voz (corpo) é bem mais baixo que o hook — não disputa com a voz."""
        tmp = _render()
        try:
            x = _samples(tmp)
            hook = x[: int(COVER * SR)]
            corpo = x[int((COVER + LEAD) * SR): int((TOTAL - 2.5) * SR)]   # exclui cauda
            self.assertLess(_rms(corpo), 0.6 * _rms(hook))
        finally:
            tmp.unlink(missing_ok=True)

    def test_vetorizacao_corpo_sobe(self):
        """Dentro do corpo, o leito SOBE rumo ao clímax (vetorização — Chion)."""
        tmp = _render()
        try:
            x = _samples(tmp)
            cedo = x[int(4.0 * SR): int(5.0 * SR)]
            tarde = x[int(9.5 * SR): int(10.5 * SR)]
            self.assertGreater(_rms(tarde), _rms(cedo))
        finally:
            tmp.unlink(missing_ok=True)

    def test_determinismo_por_seed(self):
        a, b = _render(seed=3), _render(seed=3)
        try:
            self.assertTrue(np.array_equal(_samples(a), _samples(b)))
        finally:
            a.unlink(missing_ok=True)
            b.unlink(missing_ok=True)

    def test_energia_zero_nao_explode(self):
        tmp = _render(energia=0.0)
        try:
            self.assertTrue(tmp.exists())
            x = _samples(tmp)
            self.assertTrue(np.all(np.isfinite(x)))
        finally:
            tmp.unlink(missing_ok=True)

    def test_tensao_sobrevive_no_celular(self):
        """Risco dos juízes: 40 Hz some no speaker do celular. Os harmônicos (80–200 Hz),
        que o celular reproduz, têm de carregar energia real (fundamental ausente)."""
        sig = sa._tension(SR, 0.6, 0.8)                  # 1s de tensão
        S = np.abs(np.fft.rfft(sig))
        fr = np.fft.rfftfreq(len(sig), 1 / SR)
        audivel = float(S[(fr >= 80) & (fr <= 200)].sum())
        sub = float(S[(fr >= 30) & (fr <= 60)].sum())
        self.assertGreater(audivel, 0.2 * sub)           # harmônicos presentes, não some no fone

    def test_silencio_funcional_apos_acento(self):
        """Há um respiro (dip claro) entre o acento de síncrese e o leito — o impacto pousa."""
        tmp = _render()
        try:
            x = _samples(tmp)
            hook = x[: int(COVER * SR)]
            respiro = x[int((COVER + 0.32) * SR): int((COVER + 0.40) * SR)]
            self.assertLess(_rms(respiro), 0.5 * _rms(hook))
        finally:
            tmp.unlink(missing_ok=True)

    def test_seam_fallback_finito_e_resolve(self):
        """O seam procedural (Lá→Ré) é finito e decai (resolução, não corte seco)."""
        seam = sa._seam(0.6)
        self.assertGreater(len(seam), 0)
        self.assertTrue(np.all(np.isfinite(seam)))
        self.assertLess(abs(seam[-1]), float(np.max(np.abs(seam))))   # decaiu

    def test_tick_finito_e_pico(self):
        tk = sa._tick(0.22)
        self.assertEqual(len(tk), int(SR * 0.10))
        self.assertTrue(np.all(np.isfinite(tk)))
        self.assertAlmostEqual(float(np.max(np.abs(tk))), 0.22, places=2)

    def test_reveal_insere_tick_no_offset(self):
        """Com reveal em t, a janela ao redor ganha um transiente (synch point de conteúdo)."""
        com = _render(reveals=[6.0])
        sem = _render(reveals=None)
        try:
            jan = slice(int(5.95 * SR), int(6.15 * SR))
            pico_com = float(np.max(np.abs(_samples(com)[jan])))
            pico_sem = float(np.max(np.abs(_samples(sem)[jan])))
            self.assertGreater(pico_com, pico_sem + 0.05)
        finally:
            com.unlink(missing_ok=True)
            sem.unlink(missing_ok=True)


if __name__ == '__main__':
    unittest.main()
