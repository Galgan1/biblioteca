# -*- coding: utf-8 -*-
"""Cluster de áudio/trilha — extraído de gerar_video.py (Akita pilar 9: arquivo < 500 linhas).

Funções exportadas:
  sintetiza_ambiente(dur, out_wav, seed=7, energia=0.65)  — síntese procedural WAV
"""
import sys
import wave
from pathlib import Path

import numpy as np


def sintetiza_ambiente(dur, out_wav, seed=7, energia=0.65):
    """Leito procedural livre de direitos em Ré menor — agora com PULSO RÍTMICO
    (parâmetro `energia` 0..1) para uma trilha mais dinâmica e enérgica, SEM perder a
    identidade do canal nem a voz soberana. Sonnenschein cap.5: ritmo/andamento → energia.
      energia=0   → pad contemplativo puro (comportamento antigo);
      energia~0.65 → leito pulsante + batida de coração grave (padrão do canal);
      energia=1.0 → mais movimento. Tunável por vídeo via cfg 'musica_energia'
    (livros contemplativos pedem menos; tática/ação/ofício pedem mais)."""
    sr = 44100
    rng = np.random.default_rng(seed)
    energia = max(0.0, min(1.0, energia))
    # Progressão modal contemplativa (Ré menor), graves + camada de oitava
    prog = [
        [146.83, 220.00, 293.66],   # Dm  (D3 A3 D4)
        [116.54, 174.61, 233.08],   # Bb  (Bb2 F3 Bb3)
        [174.61, 220.00, 261.63],   # F    (F3 A3 C4)
        [146.83, 196.00, 233.08],   # Gm  (D3 G3 Bb3)
    ]
    seg = 24.0 - 4.0 * energia      # mais enérgico = harmonia anda mais rápido (24s → 20s)
    xf = 6.0                        # crossfade entre acordes
    n_total = int(dur * sr)
    out = np.zeros(n_total, dtype=np.float64)
    bpm = 60.0 + 18.0 * energia     # andamento do pulso (60 → 78 BPM)
    beat = 60.0 / bpm

    def voice(freqs, length, t0):
        t = np.arange(length) / sr
        sig = np.zeros(length)
        for f in freqs:
            for h, amp in [(1, 1.0), (2, 0.18), (3, 0.08)]:
                det = 0.18 * h
                sig += amp * (np.sin(2*np.pi*(f*h+det)*t) + np.sin(2*np.pi*(f*h-det)*t)) * 0.5
            sig += 0.10 * np.sin(2*np.pi*f*2*t)   # shimmer de oitava
        # gate RÍTMICO (o pad pulsa no tempo) + resíduo de tremolo lento
        gate = 1 - (0.24 * energia) * (0.5 - 0.5*np.cos(2*np.pi*((t + t0)/beat)))  # cheio no tempo, recua entre tempos
        slow = 0.88 + 0.12*np.sin(2*np.pi*0.05*t + rng.random()*6.28)
        env = np.ones(length)
        nxf = int(xf*sr)
        env[:nxf] = np.sin(np.linspace(0, np.pi/2, nxf))**2
        env[-nxf:] = np.sin(np.linspace(np.pi/2, 0, nxf))**2
        return sig * gate * slow * env / max(1, len(freqs))

    pos, i = 0, 0
    step = int((seg - xf) * sr)
    while pos < n_total:
        length = int(seg * sr)
        v = voice(prog[i % len(prog)], length, pos / sr)
        end = min(pos + length, n_total)
        out[pos:end] += v[:end-pos]
        pos += step
        i += 1

    # batida de coração: pulso grave no tempo (raiz do acorde, oitava abaixo) — a energia
    if energia > 0:
        plen = int(0.5 * sr)
        tt = np.arange(plen) / sr
        penv = (1 - np.exp(-tt/0.004)) * np.exp(-tt/0.16)        # pluck: ataque rápido, decay curto
        for k in range(int(np.ceil(dur / beat))):
            tb = k * beat
            ic = int(tb / max(1e-9, (seg - xf))) % len(prog)     # acorde tocando em tb
            root = prog[ic][0] / 2.0                              # oitava abaixo da fundamental
            accent = 1.0 if (k % 4 == 0) else 0.66                # acento no 1º tempo do compasso
            s = int(tb * sr)
            m = max(0, min(plen, n_total - s))
            if m > 0:
                out[s:s+m] += (np.sin(2*np.pi*root*tt) * penv * (0.42 * energia * accent))[:m]

    # cadeia premium (espaço/calor/ar) — mão leve p/ não embolar sob a voz
    try:
        import dsp
        out = dsp.master(out, lowcut_fc=40, sat=1.3, air_db=2.0, rev=0.08, decay=1.0, dark=0.7, seed=31, peak=1.0)[:n_total]
    except Exception as _e:
        # pilar 7: erro com contexto (tipo + motivo) no canal de diagnóstico (stderr),
        # sem alterar o fallback — a trilha segue sem o master DSP.
        print(f"  [aviso] DSP da trilha pulado: {type(_e).__name__}: {_e}", file=sys.stderr)
    # normaliza + fade global
    out /= (np.max(np.abs(out)) + 1e-9)
    # clampa a janela de fade ao buffer real: dur curta (n_total < fade) estourava
    # o slice (out[-fo:] *= linspace de tamanho fixo) com ValueError de broadcast.
    # n_total//2 garante que fade-in e fade-out nunca se sobreponham nem extrapolem;
    # para durações longas (produção = minutos) o min é no-op (mantém 4s/7s).
    half = n_total // 2
    fi, fo = min(int(4*sr), half), min(int(7*sr), half)
    out[:fi] *= np.linspace(0, 1, fi)
    out[-fo:] *= np.linspace(1, 0, fo)
    out = (out * 0.9 * 32767).astype(np.int16)

    with wave.open(str(out_wav), 'w') as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr)
        w.writeframes(out.tobytes())
