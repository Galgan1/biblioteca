# -*- coding: utf-8 -*-
"""Testes herméticos do leito de engajamento do Short (`_short_audio.short_bed`).

Fixa os contratos que os 3 autores-juízes pediram (revisão Akita 21/jun):
  - WAV válido, finito, sem clipping (pico < 32767);
  - INTRO (22/jun): UM impacto grave (gongo|tambor) no CONTRA-TEMPO — a capa NÃO abre
    muda, mas o impacto cai longe do início (off-beat) e o começo fica quieto (sem riser);
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


def _render(total=TOTAL, cover=COVER, lead=LEAD, seed=7, energia=0.6, reveals=None, intro='gongo'):
    tmp = Path(tempfile.mktemp(suffix='.wav'))
    sa.short_bed(total, cover, lead, tmp, seed=seed, energia=energia,
                 marca_dir=_SEM_MARCA, reveals=reveals, intro=intro)
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
            self.assertGreater(float(np.max(np.abs(hook))), 0.1)   # pico claro (impacto de contra-tempo)
            self.assertGreater(_rms(hook), 0.02)                   # energia, não silêncio
        finally:
            tmp.unlink(missing_ok=True)

    def test_voz_soberana_corpo_baixo(self):
        """O leito SUSTENTADO sob a voz é bem mais baixo que o impacto da intro — não
        disputa com a voz. Mede após a cauda do impacto (cover+2s), que é esperada/curta."""
        tmp = _render()
        try:
            x = _samples(tmp)
            hook = x[: int(COVER * SR)]
            corpo = x[int((COVER + 2.0) * SR): int((TOTAL - 2.5) * SR)]   # após a cauda do impacto
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

    def test_intro_no_contratempo(self):
        """O impacto cai no CONTRA-TEMPO (off-beat da 1ª batida, ~0,4s — NÃO no downbeat t=0),
        soa CEDO (sem o dead-air que o fazia passar despercebido), e o instante inicial fica quieto."""
        tmp = _render()
        try:
            x = _samples(tmp)
            jan = x[: int((COVER + 0.3) * SR)]
            pico_t = int(np.argmax(np.abs(jan))) / SR
            self.assertGreater(pico_t, 0.2)                    # não no downbeat (é contra-tempo)
            self.assertLess(pico_t, 0.9)                       # mas CEDO (sem 1,9s de silêncio antes)
            self.assertLess(_rms(x[: int(0.2 * SR)]), 0.03)    # instante inicial quieto (off-beat, sem riser)
        finally:
            tmp.unlink(missing_ok=True)

    def test_intro_e_grave(self):
        """As duas opções de impacto são GRAVES: energia <120 Hz domina os agudos (>400 Hz)."""
        for nome, sig in (('gongo', sa._gongo()), ('tambor', sa._tambor_grave())):
            S = np.abs(np.fft.rfft(sig))
            fr = np.fft.rfftfreq(len(sig), 1 / SR)
            grave = float(S[fr < 120].sum())
            agudo = float(S[fr > 400].sum())
            self.assertGreater(grave, 3 * agudo, f'{nome} não é grave o bastante')

    def test_intro_tambor_difere_do_gongo(self):
        """gongo e tambor produzem leitos distintos — o André escolhe de ouvido."""
        g, t = _render(intro='gongo'), _render(intro='tambor')
        try:
            self.assertFalse(np.array_equal(_samples(g), _samples(t)))
        finally:
            g.unlink(missing_ok=True)
            t.unlink(missing_ok=True)

    def test_impacto_cauda_morre_suave(self):
        """Fade-out: gongo e tambor terminam em silêncio real (sem corte seco/clique) —
        a conexão impacto→fala soa natural. O array antes acabava em ~7% (clique)."""
        for nome, sig in (('gongo', sa._gongo()), ('tambor', sa._tambor_grave())):
            pico = float(np.max(np.abs(sig)))
            fim = float(np.max(np.abs(sig[-int(SR * 0.01):])))     # 10 ms finais
            self.assertLess(fim, 0.02 * pico, f'{nome} corta seco (não fez fade-out)')

    def test_impacto_ressoa_ate_a_voz_sem_gap(self):
        """O timing certo: o impacto RESSOA até a entrada da voz (cover+lead). A janela logo
        ANTES da fala NÃO é silêncio — a fala emerge da cauda (sem o gap que soava desconexo)."""
        for intro in ('gongo', 'tambor'):
            tmp = _render(intro=intro)
            try:
                x = _samples(tmp)
                antes = x[int((COVER + LEAD - 0.25) * SR): int((COVER + LEAD) * SR)]
                self.assertGreater(_rms(antes), 0.003, f'{intro}: gap de silêncio antes da voz')
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
