# -*- coding: utf-8 -*-
"""Sonoplastia de ENGAJAMENTO do Short — o leito que o Short NÃO tinha.

Antes (revisão Akita 21/jun): o Short era VOZ sobre SILÊNCIO — a capa de 2,4s
abria MUDA (`gerar_short.py` só mapeia a voz) → no Reels/TikTok/Shorts o polegar
desliza antes da 1ª palavra. Os 3 autores-juízes convergiram nessa lacuna:
  - Chion: a capa estática não VETORIZA — o tempo não corre, o espectador sai.
  - Lembke: sem ANTECIPAÇÃO (riser/promessa) não há dopamina de busca.
  - Sonnenschein: silêncio sem contraste não é gancho — é ausência.

short_bed() desenha o leito de engajamento, tudo procedural/numpy (soberano):
  - HOOK 0→capa: riser acusmático que CONSTRÓI e termina no corte (antecipação
    que NÃO resolve — Lembke; valor acrescentado/temporalização — Chion).
  - ACENTO no corte capa→cena: knock grave colado no corte (SÍNCRESE — Chion).
  - LEITO sob a voz: sub-grave 40–55 Hz pulsante, ABAIXO da faixa da fala
    (VOZ SOBERANA), com gain baixo e curva de VETORIZAÇÃO (sobe rumo a ~75% e
    resolve) — o Short "puxa" em vez de "apresentar".
Forward-looking: módulo novo, não re-renderiza catálogo. A marca sonora premium
(_marca_sonora/*.wav) é sobreposta SE existir (reforço de DNA), senão o leito
procedural basta.

  short_bed(total, cover, lead, out_wav, seed=7, energia=0.6) -> grava WAV mono 44.1k
"""
import wave
from pathlib import Path

import numpy as np

SR = 44100
MARCA = Path(__file__).parent / '_marca_sonora'


def _riser(n):
    """Sweep + ar com brilho crescente que dispara rumo ao corte — antecipação."""
    t = np.arange(n) / SR
    d = max(1e-6, n / SR)
    env = 0.20 + 0.80 * (t / d) ** 2.0                  # presença imediata que CONSTRÓI
    sweep = np.sin(2 * np.pi * (180 + 560 * (t / d) ** 1.7) * t)
    rng = np.random.default_rng(5)
    air = np.cumsum(rng.standard_normal(n)) / np.sqrt(np.arange(1, n + 1))
    air /= (np.max(np.abs(air)) + 1e-9)                 # ruído rosa-ish (brilho)
    return (sweep * 0.55 + air * 0.40) * env


def _knock(peak=0.6, f0=80.0):
    """Acento grave de síncrese no corte (porta seca + glide → punch)."""
    n = int(SR * 0.32)
    t = np.arange(n) / SR
    pitch = f0 * (1 + 0.8 * np.exp(-t / 0.03))
    body = np.sin(2 * np.pi * np.cumsum(pitch) / SR) * np.exp(-t / 0.10)
    a = int(SR * 0.0015)
    body[:a] *= np.linspace(0, 1, a)                    # mata o clique de DC
    return body / (np.max(np.abs(body)) + 1e-9) * peak


def _tick(peak=0.22, f0=1400.0):
    """Tick de revelação: ping curto e brilhante (síncrese no dado/insight — Chion).
    Transiente, não sustentado → marca 'isto é importante' sem mascarar a voz."""
    n = int(SR * 0.10)
    t = np.arange(n) / SR
    ping = np.sin(2 * np.pi * f0 * t) * np.exp(-t / 0.025)      # agudo, decay rápido
    rng = np.random.default_rng(8)
    click = rng.standard_normal(n) * np.exp(-t / 0.004)         # transiente 'tk'
    sig = ping * 0.8 + click * 0.3
    return sig / (np.max(np.abs(sig)) + 1e-9) * peak


def _tension(n, energia, beat):
    """Tensão grave pulsante. O fundamental (40–55 Hz) é SENTIDO em bons alto-falantes;
    os harmônicos (2ª/3ª, ~80–165 Hz) SOBREVIVEM ao speaker de celular (que corta <100 Hz)
    e o cérebro reconstrói o grave (fenômeno do fundamental ausente). Risco achado pelos
    juízes (21/jun): sub-grave puro a 40 Hz some em ~90% da audiência (celular). Fica
    abaixo da faixa central da voz; gain baixo no caller mantém a VOZ SOBERANA."""
    t = np.arange(n) / SR
    f = 40.0 + 14.0 * energia
    pulse = 0.55 + 0.45 * np.cos(2 * np.pi * t / (beat * 2))
    grave = (np.sin(2 * np.pi * f * t)
             + 0.32 * np.sin(2 * np.pi * 2 * f * t)     # ~80–110 Hz: o celular reproduz
             + 0.16 * np.sin(2 * np.pi * 3 * f * t))    # ~120–165 Hz: reforça a reconstrução
    return grave * pulse


def _seam(energia=0.6):
    """Seam de replay PROCEDURAL: motivo Lá→Ré (resolução na tônica) que fecha o arco
    quando a marca premium (10_encerramento.wav) não existe — assim TODO Short ganha o
    cue de loop (juízes: sem isso, só os Shorts com a marca premium fechavam)."""
    notas = [(220.00, 0.5), (293.66, 0.9)]              # Lá3 → Ré4 (resolução)
    out = []
    for f, dur in notas:
        t = np.arange(int(SR * dur)) / SR
        env = np.exp(-t / (dur * 0.5))
        out.append((np.sin(2*np.pi*f*t) + 0.3*np.sin(2*np.pi*2*f*t)) * env)
    return np.concatenate(out) * (0.30 + 0.10 * energia)


def _vetor(n, climax=0.75):
    """Curva de vetorização: 0→1 rumo ao clímax, depois resolve p/ ~0.5 (o leito 'puxa')."""
    x = np.linspace(0, 1, n)
    up = np.clip(x / climax, 0, 1) ** 1.3
    down = np.clip((1 - x) / (1 - climax), 0, 1) ** 0.8
    return np.where(x < climax, up, 0.5 + 0.5 * down)


def _overlay(buf, sig, start):
    """Soma `sig` em `buf` a partir de `start` segundos (clampa às bordas)."""
    s = max(0, int(start * SR))
    m = max(0, min(len(sig), len(buf) - s))
    if m > 0:
        buf[s:s + m] += sig[:m]


def _marca(name, gain, marca_dir):
    """Carrega um som premium da marca (se existir) — reforço de DNA, opcional."""
    f = marca_dir / f'{name}.wav'
    if not f.exists():
        return None
    with wave.open(str(f)) as w:
        raw = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16)
    return raw.astype(np.float64) / 32768 * gain


def short_bed(total, cover, lead, out_wav, seed=7, energia=0.6, marca_dir=MARCA, reveals=None):
    """Desenha e grava o leito de engajamento do Short (WAV mono 44.1k).

    total: duração total do short (s); cover: janela da capa de marca (s);
    lead: respiro antes da voz (s); energia: 0..1 (livro contemplativo pede menos);
    marca_dir: pasta dos sons premium da marca (overlay opcional; ausente = só procedural);
    reveals: offsets absolutos (s) de ticks de revelação — synch point no pico de conteúdo.
    A voz (mixada por fora) começa em cover+lead — o leito é soberano-safe sob ela.
    """
    energia = max(0.0, min(1.0, energia))
    n = int(total * SR)
    buf = np.zeros(n, dtype=np.float64)

    # HOOK — riser na janela da capa, termina no corte (antecipação que não resolve)
    nh = max(1, int(cover * SR))
    _overlay(buf, _riser(nh) * 0.6, 0.0)
    riser_marca = _marca('04_riser', 0.5, marca_dir)
    if riser_marca is not None:
        _overlay(buf, riser_marca, max(0.0, cover - len(riser_marca) / SR + 0.05))

    # ACENTO de síncrese no corte capa→cena
    _overlay(buf, _knock(0.6), max(0.0, cover - 0.04))
    impacto = _marca('05_impacto', 0.5, marca_dir)
    if impacto is not None:
        _overlay(buf, impacto, max(0.0, cover - 0.06))

    # SILÊNCIO FUNCIONAL: respiro após o acento antes do leito subir — o impacto pousa
    # no vazio (Sonnenschein) e a voz "emerge" do silêncio (acusmêtre — Chion).
    gap = 0.40
    body_start = cover + gap
    nb = n - int(body_start * SR)
    if nb > 0:
        beat = 60.0 / (60.0 + 18.0 * energia)
        bed = _tension(nb, energia, beat) * _vetor(nb) * 0.12
        _overlay(buf, bed, body_start)

    # seam de replay na cauda: marca premium se houver, senão fallback procedural
    enc = _marca('10_encerramento', 0.4, marca_dir)
    if enc is None:
        enc = _seam(energia)
    _overlay(buf, enc, max(0.0, total - len(enc) / SR - 0.2))

    # synch points de CONTEÚDO: tick brilhante no dado/insight (o pico sonoro coincide
    # com o pico de informação — Chion síncrese, Sonnenschein mapa emocional, Lembke).
    for rt in (reveals or []):
        _overlay(buf, _tick(0.22), max(0.0, float(rt)))

    try:                                                # polimento (sala curta/calor/ar)
        import dsp
        buf = dsp.master(buf, lowcut_fc=30, sat=1.2, air_db=1.0, rev=0.10,
                         decay=0.4, seed=seed, peak=0.85)[:n]
    except Exception as _e:                             # fallback: trava anti-clipping
        print(f"  [aviso] DSP do leito do short pulado: {_e}")
        p = float(np.max(np.abs(buf))) or 1.0
        if p > 0.85:
            buf *= 0.85 / p
    buf = np.clip(buf, -1.0, 1.0)

    with wave.open(str(out_wav), 'w') as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes((buf * 32767).astype(np.int16).tobytes())
