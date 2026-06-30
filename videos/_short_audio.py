# -*- coding: utf-8 -*-
"""Sonoplastia de ENGAJAMENTO do Short — o leito que o Short NÃO tinha.

Antes (revisão Akita 21/jun): o Short era VOZ sobre SILÊNCIO — a capa de 2,4s
abria MUDA (`gerar_short.py` só mapeia a voz) → no Reels/TikTok/Shorts o polegar
desliza antes da 1ª palavra. Os 3 autores-juízes convergiram nessa lacuna:
  - Chion: a capa estática não VETORIZA — o tempo não corre, o espectador sai.
  - Lembke: sem ANTECIPAÇÃO (riser/promessa) não há dopamina de busca.
  - Sonnenschein: silêncio sem contraste não é gancho — é ausência.

short_bed() desenha o leito de engajamento, tudo procedural/numpy (soberano):
  - INTRO (22/jun, pedido do André): UM impacto grave — gongo OU tambor — no
    CONTRA-TEMPO (meia batida antes do corte capa→cena), no lugar do leito de hook
    empilhado (riser+knock, que ficou "não legal"). A cauda do impacto vetoriza por
    cima do corte (temporalização — Chion) sem a camada cheia anterior.
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


def _fade_out(sig, secs):
    """Fade-out meio-cosseno nos últimos `secs`s: a cauda do impacto MORRE em silêncio
    real, sem corte seco (o array terminava em ~7% de amplitude = clique). Conexão natural
    impacto→fala. Pedido do André (22/jun)."""
    n = min(len(sig), max(1, int(SR * secs)))
    sig[-n:] *= np.cos(np.linspace(0, np.pi / 2, n)) ** 2     # 1→0 suave
    return sig


def _gongo(peak=0.66, f0=56.0, dur=1.7):
    """Gongo grave: parciais INARMÔNICOS (timbre metálico) com os graves dominando,
    ataque rápido (sem clique) e cauda CONTROLADA que vetoriza por cima do corte mas
    resolve antes de disputar com a voz (voz soberana). Pedido do André (22/jun)."""
    n = int(SR * dur)
    t = np.arange(n) / SR
    ratios = (1.0, 2.0, 2.76, 3.76, 5.40)              # razões de placa/gongo (inarmônicas)
    gains = (1.0, 0.42, 0.24, 0.13, 0.08)              # graves pesam mais → "grave de verdade"
    sig = sum(g * np.sin(2 * np.pi * f0 * r * t) for r, g in zip(ratios, gains))
    sig *= (1 + 0.05 * np.sin(2 * np.pi * 3.1 * t))    # shimmer/batimento leve
    env = np.exp(-t / (dur * 0.38))                    # cauda controlada (resolve ~1,7s)
    atk = int(SR * 0.012)
    env[:atk] *= np.linspace(0, 1, atk)               # ataque sem clique de DC
    sig *= env
    return _fade_out(sig / (np.max(np.abs(sig)) + 1e-9) * peak, 0.5)   # cauda morre suave p/ a fala


def _tambor_grave(peak=0.85, f0=60.0, dur=0.95):
    """Tambor grave (taiko/surdo): fundamental baixo com GLIDE de pitch (punch), corpo
    focado e cauda média seca. Alternativa ao gongo p/ o impacto de contra-tempo."""
    n = int(SR * dur)
    t = np.arange(n) / SR
    pitch = f0 * (1 + 1.2 * np.exp(-t / 0.05))        # glide descendente = soco de tambor
    fase = 2 * np.pi * np.cumsum(pitch) / SR
    body = np.sin(fase) + 0.25 * np.sin(2 * fase)     # 2º harmônico p/ corpo
    env = np.exp(-t / (dur * 0.28))
    atk = int(SR * 0.002)
    env[:atk] *= np.linspace(0, 1, atk)               # mata o clique
    body *= env
    return _fade_out(body / (np.max(np.abs(body)) + 1e-9) * peak, 0.25)   # cauda morre suave p/ a fala


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


def short_bed(total, cover, lead, out_wav, seed=7, energia=0.6, marca_dir=MARCA,
              reveals=None, intro='gongo'):
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
    beat = 60.0 / (60.0 + 18.0 * energia)

    # INTRO — UM impacto grave (gongo|tambor) no CONTRA-TEMPO CEDO (off-beat da 1ª batida)
    # que RESSOA até a fala: a voz EMERGE da cauda decaindo (overlap), sem o gap de silêncio
    # que soava desconexo. Pedido do André (22/jun): "acerte o timing". A duração é medida
    # da posição do impacto até ~0,3s DEPOIS da entrada da voz (cover+lead) → conexão contínua.
    pos = beat * 0.5
    span = (cover + lead) - pos + 0.30
    hit = _tambor_grave(dur=span) if intro == 'tambor' else _gongo(dur=span)
    _overlay(buf, hit, pos)

    # LEITO sob a voz (corpo) — soberano-safe, bem abaixo da voz; sobe rumo ao clímax.
    body_start = cover + 0.40
    nb = n - int(body_start * SR)
    if nb > 0:
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
