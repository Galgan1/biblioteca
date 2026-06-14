# -*- coding: utf-8 -*-
"""Sonoplasta — camada de efeitos de TRANSIÇÃO em ARCO DE COMOÇÃO (Fibonacci).

Evolução do knock único: a batida grave agora ACUMULA num padrão Fibonacci ao longo
do vídeo (1,1,2,3,5...), ganhando volume e peso — CONSTRÓI até a saturação e então a
virada do clímax cai em SILÊNCIO. É o arco emocional feito só de som:
  Sonnenschein (cap. 8): "construir camadas até a saturação e então cortar para o
  silêncio é um arco emocional inteiro feito só de som; o clímax muitas vezes é o vazio."
Cada cacho é uma figura rítmica que vai de macio a forte e termina num ACENTO (mais
grave e mais alto) colado no corte — síncrese (Chion): o cérebro solda o som ao corte.
Tudo procedural e livre de direitos (mesmo motor do pad ambiente).

Gera _stems/<slug>/efeitos.wav; depois rode `python mixmaster.py <slug>` p/ re-mixar
SEM re-renderizar. Os offsets vêm dos mp3 do build (_work/aNN.mp3): dur = mp3 + TAIL,
idêntico ao gerar_video.py — o acento bate exatamente no corte.

Uso: python efeitos_transicao.py roteiros/<slug>.json

Afinação por roteiro (opcional), bloco "efeitos" no JSON:
  {"efeitos": {"climax_cena": 11, "cap": 5, "intensidade": 1.0, "silencio_no_climax": true}}
  - climax_cena: nº da cena (1-base) cuja ENTRADA recebe a saturação; a SAÍDA dela é o
    silêncio. Omitido => ~78% do vídeo (curva padrão).
  - cap: teto de batidas por cacho (livros leves/negócios: 3; dramáticos/míticos: 5).
  - intensidade: multiplica os volumes (0.6 contido … 1.2 intenso).
  - silencio_no_climax: a virada do clímax é o vazio (True, recomendado) ou o pico (False).
"""
import sys, json, wave
from pathlib import Path
import numpy as np
from mutagen.mp3 import MP3

ROOT = Path(__file__).parent
WORK = ROOT / '_work'
STEMS = ROOT / '_stems'
SR = 44100
TAIL = 0.7              # idêntico ao gerar_video.py (respiro ao fim de cada cena)

# --- timbre do knock (design aprovado) ---
KNOCK_DUR = 0.34
F0 = 88.0              # fundamental GRAVE (Hz) — "batida de porta, porém mais grave"
DECAY = 0.090         # corpo: maior = mais redondo

# --- arco de comoção (Fibonacci) ---
LEVELS = [1, 1, 2, 3, 5]    # escada Fibonacci dos tamanhos de cacho (último = teto)
CLIMAX_FRAC = 0.78          # onde a saturação pico cai (fração das viradas), se não houver override
SILENCE_AT_CLIMAX = True    # a virada do clímax é o vazio (o silêncio é o pico)
GAIN_MIN, GAIN_MAX = 0.42, 0.95   # swell de volume do começo à saturação (intensidade)
RESOLVE_GAIN = 0.42         # cachos depois do clímax — alívio/resolução
ACCENT_BOOST = 1.18         # último golpe do cacho = acento (mais alto)
ACCENT_F0 = 0.90            # acento mais grave (peso/gravidade)
ACCENT_AT = 0.22            # o acento cai este tanto antes do corte (síncrese; resto cai no respiro)
GAP = 0.15                 # espaçamento alvo entre golpes do cacho (s)
GAP_MIN = 0.085            # piso (cachos grandes comprimem para caber no respiro)

# --- marca sonora nos pontos estruturais (sons já premium em _marca_sonora/) ---
MARCA = ROOT / '_marca_sonora'
MARCA_GAINS = {'04_riser': 0.50, '05_impacto': 0.85, '06_resolucao': 0.48, '10_encerramento': 0.42}


def _load_wav(p):
    with wave.open(str(p)) as w:
        return np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float64) / 32768


def place_marca(buf, bounds, climax, total):
    """Sobrepõe a MARCA SONORA nos momentos estruturais (sons já premium; voz-safe).
    'Menos é mais' (cap. 7): só o ARCO DO CLÍMAX + o encerramento — nada a cada cena.
      riser → crescendo terminando no corte do clímax (suave sob a voz, alto só no respiro)
      impacto → braam grave colado no corte do clímax (síncrese; respiro = voz em silêncio)
      resolução → swell quente no corte para a cena de resolução
      encerramento → motivo Lá→Ré na cauda final (pós-conteúdo).
    Logo (01) NÃO entra no pré-roll do longo (retenção): fica p/ Shorts/end-card."""
    if not MARCA.exists():
        return buf
    def at(name, start, gain):
        f = MARCA / f'{name}.wav'
        if not f.exists():
            return 0
        sig = _load_wav(f) * gain
        s = max(0, int(start * SR)); m = max(0, min(len(sig), len(buf) - s))
        if m > 0:
            buf[s:s+m] += sig[:m]
        return len(sig)
    if 0 <= climax < len(bounds):
        bc = float(bounds[climax])
        rlen = (_len(MARCA / '04_riser.wav'))
        at('04_riser', bc - rlen/SR + 0.05, MARCA_GAINS['04_riser'])      # crescendo até o corte
        at('05_impacto', bc - 0.10, MARCA_GAINS['05_impacto'])           # braam no corte (síncrese)
        if climax + 1 < len(bounds):
            at('06_resolucao', float(bounds[climax+1]) - 0.10, MARCA_GAINS['06_resolucao'])
    elen = _len(MARCA / '10_encerramento.wav')
    at('10_encerramento', total - elen/SR - 0.2, MARCA_GAINS['10_encerramento'])
    return buf


def _len(p):
    if not p.exists():
        return 0
    with wave.open(str(p)) as w:
        return w.getnframes()


def _knock(peak=0.55, f0=F0):
    n = int(SR * KNOCK_DUR)
    t = np.arange(n) / SR
    pitch = f0 * (1 + 0.8 * np.exp(-t / 0.028))         # glide descendente = punch
    phase = 2 * np.pi * np.cumsum(pitch) / SR
    body = np.sin(phase)
    body += 0.42 * np.sin(2 * np.pi * 1.8 * f0 * t)     # parciais de madeira
    body += 0.20 * np.sin(2 * np.pi * 2.6 * f0 * t)
    body *= np.exp(-t / DECAY)
    rng = np.random.default_rng(3)
    click = np.convolve(rng.standard_normal(n), np.ones(10) / 10, mode='same')
    click *= np.exp(-t / 0.008)                         # transiente curto ('tok', não 'tick')
    sig = body * 0.9 + click * 0.40                     # mais transiente = batida mais enérgica/snappy
    a = int(SR * 0.0015)
    sig[:a] *= np.linspace(0, 1, a)                     # ataque 1,5ms (mata o clique de DC)
    sig /= (np.max(np.abs(sig)) + 1e-9)
    return sig * peak


def _curve(n_trans, climax, levels, gmin, gmax):
    """Devolve [(count, gain), ...] por virada — a densidade e o volume desenhados pela curva."""
    out = []
    for i in range(n_trans):
        if i < climax:                                  # SUBIDA: Fibonacci esticado + swell
            p = i / max(1, climax)
            count = levels[min(len(levels) - 1, int(p * len(levels)))]
            gp = i / max(1, climax - 1) if climax > 1 else 1.0
            gain = gmin + (gmax - gmin) * gp
        elif i == climax:                               # CLÍMAX: o vazio (ou o pico)
            count = 0 if SILENCE_AT_CLIMAX else levels[-1]
            gain = gmax
        else:                                           # RESOLUÇÃO: alívio, fecha em silêncio
            count = 1 if (n_trans - 1 - i) >= 1 else 0
            gain = RESOLVE_GAIN
        out.append((count, gain))
    return out


def _place(buf, bound, k, gain):
    """Cola um cacho de k golpes terminando no acento (perto do corte), macio→forte."""
    if k <= 0 or gain <= 0:
        return
    acc_t = bound - ACCENT_AT
    avail = acc_t - (bound - TAIL + 0.02)               # quanto cabe no respiro antes do acento
    gap = min(GAP, max(GAP_MIN, avail / (k - 1))) if k > 1 else 0.0
    for j in range(k):                                  # j=0 o mais antigo; j=k-1 o acento
        is_acc = (j == k - 1)
        t = acc_t - (k - 1 - j) * gap
        ramp = 0.6 + 0.4 * (j / max(1, k - 1))          # macio → forte rumo ao acento
        g = gain * (ACCENT_BOOST if is_acc else ramp)
        kn = _knock(peak=g, f0=F0 * (ACCENT_F0 if is_acc else 1.0))
        start = max(0, int(t * SR))
        buf[start:start + len(kn)] += kn


def main(roteiro_path):
    if not roteiro_path:
        sys.exit("uso: python efeitos_transicao.py roteiros/<slug>.json")
    cfg = json.loads(Path(roteiro_path).read_text(encoding='utf-8'))
    slug = cfg['slug']
    n = len(cfg['cenas'])
    ef = cfg.get('efeitos', {})

    durs = []
    for i in range(n):
        mp3 = WORK / f'a{i:02d}.mp3'
        if not mp3.exists():
            sys.exit(f'[!] {mp3} ausente — gere o vídeo de {slug} antes (e não construa outro no meio).')
        durs.append(MP3(mp3).info.length + TAIL)
    total = sum(durs)

    voz = STEMS / slug / 'voz.wav'
    if voz.exists():
        with wave.open(str(voz)) as w:
            vlen = w.getnframes() / w.getframerate()
        if abs(vlen - total) > 0.6:
            sys.exit(f'[!] _work nao bate com os stems ({total:.1f}s vs voz {vlen:.1f}s) — rebuild {slug}.')

    bounds = np.cumsum(durs)[:-1]                        # n-1 viradas de cena
    n_trans = len(bounds)

    # teto de batidas e intensidade afináveis por roteiro
    cap = int(ef.get('cap', LEVELS[-1]))
    levels = [min(v, cap) for v in LEVELS]
    inten = float(ef.get('intensidade', 1.0))
    gmin, gmax = GAIN_MIN * inten, GAIN_MAX * inten
    global SILENCE_AT_CLIMAX
    SILENCE_AT_CLIMAX = bool(ef.get('silencio_no_climax', SILENCE_AT_CLIMAX))

    # clímax = virada cuja chegada satura; default ~78% do vídeo
    if 'climax_cena' in ef:
        climax = max(0, min(n_trans - 1, int(ef['climax_cena']) - 2))  # entrada da cena S = virada S-2 (0-base)
    else:
        climax = round(CLIMAX_FRAC * (n_trans - 1))

    plano = _curve(n_trans, climax, levels, gmin, gmax)

    kn_len = len(_knock())
    buf = np.zeros(int(total * SR) + kn_len * 4, dtype=np.float64)
    for b, (k, g) in zip(bounds, plano):
        _place(buf, float(b), k, g)
    buf = buf[:int(total * SR)]
    try:                                                # cadeia premium: sala curta + calor/ar (bumbo segue seco)
        import dsp
        buf = dsp.master(buf, lowcut_fc=35, sat=1.6, air_db=1.5, rev=0.10, decay=0.28, dark=0.7, seed=21, peak=0.82)[:int(total * SR)]
    except Exception as _e:                             # fallback: trava anti-clipping simples
        print(f"  [aviso] DSP das batidas pulado: {_e}")
        peak = float(np.max(np.abs(buf))) or 1.0
        if peak > 0.82:
            buf *= 0.82 / peak
    try:                                                # marca sonora nos pontos estruturais (arco do clímax + encerramento)
        place_marca(buf, bounds, climax, total)
    except Exception as _e:
        print(f"  [aviso] marca sonora pulada: {_e}")
    buf = np.clip(buf, -1.0, 1.0)

    efe = STEMS / slug / 'efeitos.wav'
    efe.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(efe), 'w') as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((buf * 32767).astype(np.int16).tobytes())

    mapa = ' '.join((str(k) if k else '·') for k, _ in plano)
    print(f'OK efeitos -> {efe}')
    print(f'   arco de comoção (Fibonacci), clímax na virada {climax}'
          f'{" = SILÊNCIO" if SILENCE_AT_CLIMAX else ""}, cap={cap}, intensidade={inten}')
    print(f'   batidas por virada:  {mapa}   (· = silêncio)')
    print(f'   agora: python mixmaster.py {slug}')


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else None)
