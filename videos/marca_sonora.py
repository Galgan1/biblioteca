# -*- coding: utf-8 -*-
"""MARCA SONORA do Minuto Real — 10 sons procedurais (livres de direitos) com DNA único.

Identidade sonora do canal sintetizada em Python: nada de pacote de prateleira (o
anti-pattern do cap.7 do Sonnenschein, "ambiência genérica → sem alma"). Cada som é a
camada "sound design / sons inventados" (cap.2) e serve à curva emocional (cap.8).

DNA compartilhado: tonalidade **Ré menor** (D/A/F), caráter grave, quente, premium e
CONTIDO; motivo da marca = salto ascendente **Lá → Ré** (na assinatura e no encerramento,
como colchetes da identidade). Mono 44,1 kHz (igual ao pipeline).

Uso:
  python marca_sonora.py            # renderiza os 10 em _marca_sonora/ + uma demo (reel)
  python marca_sonora.py reel       # só a demo

Os 10:
  01 assinatura  02 transicao  03 revelacao  04 riser  05 impacto
  06 resolucao   07 pagina     08 tick       09 roomtone 10 encerramento
"""

import sys, wave
from pathlib import Path
import numpy as np
import dsp  # cadeia premium (reverb/saturação/ar/low-cut)

SR = 44100
OUT = Path(__file__).parent / '_marca_sonora'

# --- tonalidade do canal (Ré menor) ---
D2, D3, A3, F3, A2 = 73.42, 146.83, 220.00, 174.61, 110.00
D4, F4, A4, D5, A5, D6 = 293.66, 349.23, 440.00, 587.33, 880.00, 1174.66
FS4 = 369.99  # Fá# (terça de Ré MAIOR — picardia p/ alívio na resolução)


def _t(dur):
    return np.arange(int(SR * dur)) / SR


def _norm(x, peak=0.9):
    m = np.max(np.abs(x)) + 1e-9
    return x * (peak / m)


def _fade(x, fi=0.005, fo=0.02):
    a, b = int(SR * fi), int(SR * fo)
    if len(x) > a + b:
        x[:a] *= np.linspace(0, 1, a)
        x[-b:] *= np.linspace(1, 0, b)
    return x


def _band(sig, lo, hi):
    """Filtro passa-banda via FFT (numpy puro)."""
    n = len(sig)
    f = np.fft.rfftfreq(n, 1 / SR)
    S = np.fft.rfft(sig)
    S[(f < lo) | (f > hi)] = 0
    return np.fft.irfft(S, n)


def _bell(freq, dur, decay, detune=0.0, parts=((1, 1.0), (2.01, 0.4), (3.02, 0.18), (4.7, 0.08))):
    """Sino/marimba: parciais ligeiramente inarmônicas com decaimento exponencial."""
    t = _t(dur)
    s = np.zeros(len(t))
    for mult, amp in parts:
        s += amp * np.sin(2 * np.pi * freq * mult * (1 + detune) * t)
    return s * np.exp(-t / decay)


def _bumbo(dur=0.18, f_hi=120, f_lo=45, decay=0.085, click=0.22):
    """O bumbo seco da marca (a transição)."""
    t = _t(dur)
    f = f_lo + (f_hi - f_lo) * np.exp(-t / 0.012)
    body = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / decay) * (1 - np.exp(-t / 0.0008))
    rng = np.random.default_rng(3)
    n = int(SR * 0.02)
    c = np.diff(rng.standard_normal(n), prepend=0)
    c *= np.exp(-np.arange(n) / (SR * 0.0025))
    c = c / (np.max(np.abs(c)) + 1e-9) * click
    body[:n] += c
    return body


# ───────────────────────── os 10 sons ─────────────────────────


def s01_assinatura():
    """Logo do canal (~2.4s): leito grave que sobe + motivo Lá→Ré em sino + bumbo + brilho."""
    dur = 2.5
    t = _t(dur)
    out = np.zeros(len(t))
    # leito grave (D3+A3+D4) que entra suave
    bed = (
        np.sin(2 * np.pi * D3 * t)
        + 0.6 * np.sin(2 * np.pi * A3 * t)
        + 0.4 * np.sin(2 * np.pi * D4 * t)
    )
    bed *= np.clip(t / 0.5, 0, 1) * np.exp(-np.maximum(0, t - 1.4) / 0.6)
    out += 0.35 * bed

    def place(sig, at):
        s = int(at * SR)
        m = min(len(sig), len(out) - s)
        out[s : s + m] += sig[:m]

    # motivo da marca: Lá → Ré (salto ascendente = esperança)
    place(0.5 * _bell(A4, 1.3, 0.7), 0.25)
    place(0.55 * _bell(D5, 1.6, 0.9), 0.78)
    # bumbo pontua
    place(0.7 * _bumbo(), 1.25)
    # brilho (oitava alta) na cauda
    place(
        0.12
        * _fade(
            _band(np.random.default_rng(1).standard_normal(int(SR * 1.0)), 4000, 12000)
            * np.exp(-_t(1.0) / 0.5)
        ),
        0.8,
    )
    return _fade(out)


def s02_transicao():
    """Bumbo seco — a virada de cena (a batida da marca)."""
    return _fade(_bumbo())


def s03_revelacao():
    """Shimmer de revelação (~1.2s): oitavas agudas de Ré com glissando p/ cima + ar."""
    dur = 1.2
    t = _t(dur)
    out = np.zeros(len(t))
    gl = 1 + 0.015 * (1 - np.exp(-t / 0.3))  # leve subida
    for f, a in ((D5, 1.0), (A5, 0.7), (D6, 0.5)):
        trem = 1 + 0.12 * np.sin(2 * np.pi * 7 * t)
        out += a * np.sin(2 * np.pi * f * gl * t) * trem
    out *= np.exp(-t / 0.55) * (1 - np.exp(-t / 0.02))
    out += (
        0.18
        * _band(np.random.default_rng(2).standard_normal(len(t)), 6000, 14000)
        * np.exp(-t / 0.4)
    )
    return _fade(out)


def s04_riser():
    """Riser de tensão (~2.0s): ruído filtrado subindo + tom subindo + crescendo."""
    dur = 2.0
    t = _t(dur)
    out = np.zeros(len(t))
    sweep = np.sin(2 * np.pi * np.cumsum(120 + 700 * (t / dur) ** 2) / SR)  # 120→820 Hz
    noise = np.random.default_rng(4).standard_normal(len(t))
    noise = _band(noise, 300, 5000) * (t / dur)  # ruído ganha brilho subindo
    out = 0.6 * sweep + 0.6 * noise
    out *= (t / dur) ** 1.5  # crescendo
    return _fade(out, fo=0.01)


def s05_impacto():
    """Impacto/braam de clímax (~0.7s): sub grave + braam com grit, escuro."""
    dur = 0.7
    t = _t(dur)
    out = np.zeros(len(t))
    f = D2 * (1 + 0.5 * np.exp(-t / 0.02))
    sub = np.sin(2 * np.pi * np.cumsum(f) / SR) + 0.5 * np.sin(2 * np.pi * np.cumsum(f * 0.5) / SR)
    braam = np.tanh(
        3 * (np.sin(2 * np.pi * D3 * t) + np.sin(2 * np.pi * A3 * 1.005 * t))
    )  # grit harmônico
    nz = np.random.default_rng(6).standard_normal(len(t)) * np.exp(-t / 0.01)
    out = (0.9 * sub + 0.35 * braam) * np.exp(-t / 0.42) * (1 - np.exp(-t / 0.001)) + 0.25 * nz
    return _fade(out)


def s06_resolucao():
    """Resolução quente (~1.8s): acorde de Ré MAIOR (picardia = alívio) que floresce e some."""
    dur = 1.8
    t = _t(dur)
    out = np.zeros(len(t))
    for f, a in ((D3, 0.8), (FS4, 0.6), (A4, 0.6), (D5, 0.4)):
        out += a * np.sin(2 * np.pi * f * t) * (1 + 0.05 * np.sin(2 * np.pi * 5 * t))
    out += 0.15 * _band(np.random.default_rng(7).standard_normal(len(t)), 5000, 11000)
    env = np.clip(t / 0.7, 0, 1) * np.exp(-np.maximum(0, t - 0.9) / 0.7)
    return _fade(out * env)


def s07_pagina():
    """Virar de página (~0.45s): ruído de papel (passa-banda) com varredura rápida."""
    dur = 0.45
    t = _t(dur)
    nz = np.random.default_rng(8).standard_normal(len(t))
    paper = _band(nz, 1800, 7000)
    env = np.exp(-(((t - 0.10) / 0.05) ** 2)) + 0.7 * np.exp(
        -(((t - 0.26) / 0.06) ** 2)
    )  # "shff-shff"
    return _fade(paper * env * 1.2)


def s08_tick():
    """Marcador de dado (~0.08s): clique curtíssimo e preciso, agudo+corpo."""
    dur = 0.10
    t = _t(dur)
    body = np.sin(2 * np.pi * 1500 * t) * np.exp(-t / 0.012)
    click = np.diff(np.random.default_rng(9).standard_normal(len(t)), prepend=0) * np.exp(
        -t / 0.0015
    )
    return _fade(body * 0.7 + 0.5 * click / (np.max(np.abs(click)) + 1e-9))


def s09_roomtone():
    """Leito/room tone (~4s, loopável): drone grave + ruído marrom baixo, quase inaudível."""
    dur = 4.0
    t = _t(dur)
    drone = 0.5 * np.sin(2 * np.pi * D2 * t) + 0.3 * np.sin(2 * np.pi * A2 * t)
    drone *= 1 + 0.15 * np.sin(2 * np.pi * 0.07 * t)
    brown = np.cumsum(np.random.default_rng(10).standard_normal(len(t)))
    brown = _band(brown, 40, 350)
    brown /= np.max(np.abs(brown)) + 1e-9
    out = 0.35 * drone + 0.5 * brown
    return _fade(out, fi=0.5, fo=0.5)  # bordas casadas p/ loop


def s10_encerramento():
    """Encerramento/CTA (~2.3s): motivo Lá→Ré (eco da assinatura) + pad quente convidativo."""
    dur = 2.3
    t = _t(dur)
    out = np.zeros(len(t))
    pad = (
        np.sin(2 * np.pi * D3 * t)
        + 0.6 * np.sin(2 * np.pi * A3 * t)
        + 0.4 * np.sin(2 * np.pi * D4 * t)
    )
    pad *= np.clip(t / 0.4, 0, 1) * np.exp(-np.maximum(0, t - 1.3) / 0.7)
    out += 0.3 * pad

    def place(sig, at):
        s = int(at * SR)
        m = min(len(sig), len(out) - s)
        out[s : s + m] += sig[:m]

    place(0.45 * _bell(A4, 1.2, 0.7), 0.2)
    place(0.5 * _bell(D5, 1.5, 0.9), 0.62)
    place(
        0.10
        * _band(np.random.default_rng(11).standard_normal(int(SR * 1.2)), 4000, 12000)
        * np.exp(-_t(1.2) / 0.6),
        0.6,
    )
    return _fade(out)


SONS = [
    ('01_assinatura', s01_assinatura),
    ('02_transicao', s02_transicao),
    ('03_revelacao', s03_revelacao),
    ('04_riser', s04_riser),
    ('05_impacto', s05_impacto),
    ('06_resolucao', s06_resolucao),
    ('07_pagina', s07_pagina),
    ('08_tick', s08_tick),
    ('09_roomtone', s09_roomtone),
    ('10_encerramento', s10_encerramento),
]


# Perfil premium por som (botões do dsp.master) — espaço/calor/ar afinados por função.
# fmt: off
PREMIUM = {
    '01_assinatura':  dict(lowcut_fc=45,  sat=1.6, air_db=3.0,           rev=0.30, decay=1.6, dark=0.50, seed=1),
    '02_transicao':   dict(lowcut_fc=35,  sat=2.2, air_db=1.5,           rev=0.10, decay=0.28, dark=0.70, seed=2),
    '03_revelacao':   dict(lowcut_fc=200, sat=1.3, air_db=4.5, air_fc=9000, rev=0.34, decay=1.3, dark=0.30, seed=3),
    '04_riser':       dict(lowcut_fc=70,  sat=1.8, air_db=3.0,           rev=0.24, decay=1.0, dark=0.50, seed=4),
    '05_impacto':     dict(lowcut_fc=28,  sat=2.6, air_db=1.0,           rev=0.28, decay=1.3, dark=0.65, predelay=0.020, seed=5),
    '06_resolucao':   dict(lowcut_fc=55,  sat=1.4, air_db=3.5,           rev=0.36, decay=1.7, dark=0.45, seed=6),
    '07_pagina':      dict(lowcut_fc=400, sat=1.2, air_db=3.0,           rev=0.14, decay=0.4, dark=0.40, seed=7),
    '08_tick':        dict(lowcut_fc=300, sat=1.5, air_db=4.0, air_fc=9000, rev=0.10, decay=0.22, dark=0.40, seed=8),
    '09_roomtone':    dict(lowcut_fc=28,  sat=1.2, air_db=0.5,           rev=0.16, decay=1.4, dark=0.70, seed=9),
    '10_encerramento':dict(lowcut_fc=45,  sat=1.5, air_db=3.2,           rev=0.32, decay=1.5, dark=0.50, seed=10),
}
# fmt: on


def _premiumize(name, sig):
    """Passa o som cru pela cadeia premium do seu perfil (espaço + calor + ar)."""
    p = PREMIUM.get(name)
    return dsp.master(sig, **p) if p else sig


def _save(name, sig, peak=0.9):
    OUT.mkdir(parents=True, exist_ok=True)
    sig = np.clip(_norm(sig.astype(np.float64), peak), -1, 1)
    with wave.open(str(OUT / f'{name}.wav'), 'w') as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes((sig * 32767).astype(np.int16).tobytes())
    return sig


def render_all():
    rendered = {}
    for name, fn in SONS:
        rendered[name] = _save(name, _premiumize(name, fn()))
        print(f'  OK {name}.wav')
    return rendered


def render_reel(rendered=None):
    if rendered is None:
        rendered = {name: _norm(_premiumize(name, fn())) for name, fn in SONS}
    gap = np.zeros(int(SR * 0.6))
    reel = []
    for name, _ in SONS:
        reel.append(rendered[name])
        reel.append(gap)
    reel = np.concatenate(reel)
    OUT.mkdir(parents=True, exist_ok=True)
    with wave.open(str(OUT / '00_demo_reel.wav'), 'w') as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes((np.clip(reel, -1, 1) * 32767).astype(np.int16).tobytes())
    print(f'  OK 00_demo_reel.wav ({len(reel) / SR:.1f}s)')


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'reel':
        render_reel()
    else:
        r = render_all()
        render_reel(r)
    print(f'marca sonora -> {OUT.resolve()}')
