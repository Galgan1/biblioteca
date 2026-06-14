# -*- coding: utf-8 -*-
"""Recupera o timing por cena de um vídeo JÁ construído (sem timing.json) lendo as
transições fade-to-black do próprio artefato via blackdetect — a ÚNICA fonte fiel
para o backlog (re-sintetizar o TTS não reproduz a duração original; o vídeo pode ter
caído na rota-de-fuga edge-tts, e neural-TTS não é determinístico).

Cada cena termina com fade-to-black (FADE=0.45). O blackdetect acha: abertura (~0),
as (n-1) fronteiras internas e o fechamento (~total). Escreve _stems/<slug>/timing.json
no MESMO formato do build, deixando o vídeo pronto p/ legendas/capítulos retroativos.

Fonte do vídeo: _stems/<slug>/video_mudo.mp4 (preferido) ou <slug>.mp4.
Uso:  python recuperar_timing.py <slug> [<slug> ...]
"""

import sys, json, subprocess, re
from pathlib import Path
import imageio_ffmpeg

ROOT = Path(__file__).parent
STEMS = ROOT / '_stems'
FF = imageio_ffmpeg.get_ffmpeg_exe()
TAIL = 0.7


def _video_for(slug):
    for p in (STEMS / slug / 'video_mudo.mp4', ROOT / f'{slug}.mp4'):
        if p.exists():
            return p
    return None


def _total(path):
    r = subprocess.run([FF, '-i', str(path)], capture_output=True, text=True)
    m = re.search(r'Duration: (\d+):(\d+):([\d.]+)', r.stderr)
    return int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3)) if m else None


# Escada de (pix_th, d): base escuro casa em pix_th baixo; premium/movimento (imagens
# brilhantes, fade curto) precisa de pix_th maior e d menor. Auto-sweep aceita o
# PRIMEIRO par que isola exatamente n_cenas — autotunagem por vídeo.
_LADDER = [(0.06, 0.06), (0.10, 0.05), (0.13, 0.05), (0.16, 0.04), (0.08, 0.08)]


def _boundaries(vid, total, pix_th, d):
    r = subprocess.run(
        [FF, '-i', str(vid), '-vf', f'blackdetect=d={d}:pix_th={pix_th}', '-an', '-f', 'null', '-'],
        capture_output=True,
        text=True,
    )
    blacks = [float(x) for x in re.findall(r'black_start:([\d.]+)', r.stderr)]
    internas = [
        b for b in blacks if 1.0 < b < total - 1.0
    ]  # tira abertura(~0) e fechamento(~total)
    return [0.0] + internas


def recover(slug, n_cenas):
    vid = _video_for(slug)
    if not vid:
        return None, 'sem video_mudo.mp4 nem <slug>.mp4'
    total = _total(vid)
    if not total:
        return None, 'duração ilegível'
    for pix_th, d in _LADDER:
        starts = _boundaries(vid, total, pix_th, d)
        if len(starts) == n_cenas:
            durs = [round(starts[i + 1] - starts[i], 2) for i in range(n_cenas - 1)]
            durs.append(round(total - starts[-1], 2))
            return (
                {
                    'tail': TAIL,
                    'durs': durs,
                    'fonte': f'blackdetect@{pix_th}/{d}',
                    'total': round(total, 2),
                },
                'ok',
            )
    return None, f'blackdetect não isolou {n_cenas} cenas em nenhum threshold da escada'


def main(slug):
    cfg = json.loads((ROOT / 'roteiros' / f'{slug}.json').read_text(encoding='utf-8'))
    n = len(cfg['cenas'])
    data, msg = recover(slug, n)
    if not data:
        print(f'{slug}: FALHOU — {msg}')
        return False
    (STEMS / slug).mkdir(parents=True, exist_ok=True)
    (STEMS / slug / 'timing.json').write_text(
        json.dumps(data, ensure_ascii=False), encoding='utf-8'
    )
    print(f'{slug}: OK — {n} cenas, total {data["total"]}s -> _stems/{slug}/timing.json')
    return True


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('uso: python recuperar_timing.py <slug> [<slug> ...]')
    ok = sum(main(s) for s in sys.argv[1:])
    print(f'\n{ok}/{len(sys.argv) - 1} recuperados.')
