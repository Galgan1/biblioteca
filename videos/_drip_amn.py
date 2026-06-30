# -*- coding: utf-8 -*-
"""Drip dos Reels do AMN (cenas 2-6, IG+FB) a cada 2 min. Idempotente/logado/resiliente.
Cena 1 + carrossel + story já foram à mão. YouTube (vídeo inteiro) já publicado."""
import sys
import time
import json
import datetime
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

import instagram_post as ig
import facebook_reels as fr

ROOT = Path(__file__).parent
SLUG = 'admiravel-mundo-novo-controle-pelo-prazer'
INTERVAL = 120
cfg = json.loads((ROOT / 'roteiros' / f'{SLUG}.json').read_text(encoding='utf-8'))


def log(m):
    print(f'[{datetime.datetime.now():%H:%M:%S}] {m}', flush=True)


def _ja(suf, i):
    sf = ROOT / '_shorts' / f'{SLUG}_{suf}.json'
    return sf.exists() and str(i) in json.loads(sf.read_text())


def ig_post(i):
    mid = ig.post_reel(str(ROOT / '_shorts' / f'{SLUG}_{i:02d}.mp4'), ig.caption_for(cfg, i))
    if mid:
        sf = ROOT / '_shorts' / f'{SLUG}_instagram_state.json'
        st = json.loads(sf.read_text()) if sf.exists() else {}
        st[str(i)] = mid
        sf.write_text(json.dumps(st, ensure_ascii=False, indent=1), encoding='utf-8')
    return mid


fila = [(plat, i) for i in range(2, 7) for plat in ('ig', 'fb')]
log(f'DRIP AMN: {len(fila)} reels (cenas 2-6, IG+FB), 1 a cada {INTERVAL // 60} min')
for n, (plat, i) in enumerate(fila, 1):
    try:
        if plat == 'ig':
            if _ja('instagram_state', i):
                log(f'{n}/{len(fila)} SKIP ig cena {i}'); continue
            log(f'{n}/{len(fila)} IG cena {i} -> {ig_post(i)}')
        else:
            if _ja('fbreels_state', i):
                log(f'{n}/{len(fila)} SKIP fb cena {i}'); continue
            fr.postar_reels(SLUG, idxs=[i])
            log(f'{n}/{len(fila)} FB cena {i} ok')
    except Exception as e:
        log(f'{n}/{len(fila)} ERRO {plat} {i}: {type(e).__name__}: {str(e)[:90]}')
    if n < len(fila):
        time.sleep(INTERVAL)
log('DRIP AMN DONE')
