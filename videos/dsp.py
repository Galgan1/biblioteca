# -*- coding: utf-8 -*-
"""DSP premium — primitivas livres de direitos (numpy puro) que elevam a síntese
procedural de "limpa" para "cinema". Qualquer motor do estúdio (marca_sonora,
sintetiza_ambiente, efeitos_transicao) pode passar o sinal por esta cadeia.

O que torna um som PREMIUM (alvos do Sonnenschein cap. 3/4):
  • ESPAÇO  → reverb de convolução com IR sintética (o maior salto barato→caro);
  • CALOR   → saturação suave (tanh), o "analógico" que cola e arredonda;
  • AR/FOCO → high-shelf de brilho + low-cut que tira a lama;
  • ORGANICIDADE → micro-variação por instância (mata o "robótico" da repetição).

Tudo mono 44,1 kHz (igual ao pipeline). Sem dependências além de numpy.
"""

import numpy as np

SR = 44100


def _fftconv(x, h):
    """Convolução rápida via FFT (numpy puro)."""
    n = len(x) + len(h) - 1
    nfft = 1 << int(np.ceil(np.log2(max(2, n))))
    y = np.fft.irfft(np.fft.rfft(x, nfft) * np.fft.rfft(h, nfft), nfft)[:n]
    return y


def _nfft(n):
    return 1 << int(np.ceil(np.log2(max(2, n))))  # potência de 2 → FFT rápida p/ sinal longo


def lowcut(x, fc=40):
    """Passa-altas suave (tira rumble/lama abaixo de fc)."""
    if fc <= 0:
        return x
    n = len(x)
    nf = _nfft(n)
    f = np.fft.rfftfreq(nf, 1 / SR)
    hp = 1 / (1 + (fc / np.maximum(f, 1e-9)) ** 4)
    return np.fft.irfft(np.fft.rfft(x, nf) * hp, nf)[:n]


def highshelf(x, fc=8000, gain_db=3.0):
    """Realça o AR acima de fc (brilho/presença sem ficar estridente)."""
    if gain_db == 0:
        return x
    n = len(x)
    nf = _nfft(n)
    f = np.fft.rfftfreq(nf, 1 / SR)
    g = 10 ** (gain_db / 20)
    curve = 1 + (g - 1) * (1 / (1 + (fc / np.maximum(f, 1e-9)) ** 2))
    return np.fft.irfft(np.fft.rfft(x, nf) * curve, nf)[:n]


def saturate(x, drive=1.6):
    """Saturação analógica suave (tanh) — calor e cola harmônica."""
    if drive <= 1.0:
        return x
    return np.tanh(drive * x) / np.tanh(drive)


def make_ir(decay=1.1, predelay=0.012, er_n=12, seed=1, dark=0.55):
    """IR de sala/hall sintética: reflexões iniciais discretas + cauda difusa
    exponencial, escurecendo com o tempo (quanto maior `dark`, mais quente/abafado)."""
    rng = np.random.default_rng(seed)
    L = int(SR * (predelay + decay + 0.15))
    ir = np.zeros(L)
    pd = int(SR * predelay)
    for _ in range(er_n):  # early reflections
        t = pd + int(SR * rng.uniform(0.003, 0.07))
        if t < L:
            ir[t] += rng.uniform(0.25, 0.7) * rng.choice([-1.0, 1.0])
    tail = rng.standard_normal(L) * np.exp(-np.arange(L) / (SR * decay * 0.35))
    f = np.fft.rfftfreq(L, 1 / SR)
    fc = 2000 + 9000 * (1 - dark)
    tail = np.fft.irfft(np.fft.rfft(tail) * (1 / (1 + (f / fc) ** 2)), L)
    ir[pd:] += 0.5 * tail[: L - pd]
    ir[0] += 1e-4
    return ir / (np.max(np.abs(ir)) + 1e-9)


def reverb(x, amount=0.25, decay=1.1, predelay=0.012, seed=1, dark=0.55):
    """Reverb de convolução. Devolve o sinal com a CAUDA (mais longo que x)."""
    if amount <= 0:
        return x
    ir = make_ir(decay, predelay, seed=seed, dark=dark)
    wet = _fftconv(x, ir)
    wet = wet / (np.max(np.abs(wet)) + 1e-9) * (np.max(np.abs(x)) + 1e-9)
    dry = np.zeros(len(wet))
    dry[: len(x)] = x
    return dry + amount * wet


def chorus(x, depth_ms=6.0, rate=0.6, mix=0.3, seed=2):
    """Coro/ensemble: delay modulado — largura e movimento (mesmo em mono)."""
    n = len(x)
    t = np.arange(n) / SR
    lfo = (depth_ms / 1000) * (
        0.5 + 0.5 * np.sin(2 * np.pi * rate * t + np.random.default_rng(seed).random() * 6.28)
    )
    d = (0.008 + lfo) * SR
    idx = np.clip(np.arange(n) - d, 0, n - 1)
    i0 = idx.astype(int)
    frac = idx - i0
    wet = x[i0] * (1 - frac) + x[np.clip(i0 + 1, 0, n - 1)] * frac
    return x * (1 - mix) + wet * mix


def master(
    x,
    lowcut_fc=40,
    sat=1.6,
    air_db=3.0,
    air_fc=8000,
    rev=0.25,
    decay=1.1,
    dark=0.55,
    predelay=0.012,
    seed=1,
    peak=0.9,
):
    """Cadeia premium completa: low-cut → saturação → ar → reverb → normaliza.
    Cada parâmetro é um botão; rev=0 e sat<=1 desligam os estágios."""
    y = lowcut(x.astype(np.float64), lowcut_fc)
    y = saturate(y, sat)
    y = highshelf(y, air_fc, air_db)
    y = reverb(y, amount=rev, decay=decay, predelay=predelay, seed=seed, dark=dark)
    return y / (np.max(np.abs(y)) + 1e-9) * peak
