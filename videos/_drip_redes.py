# -*- coding: utf-8 -*-
"""Drip de 4 min dos Reels nas redes (IG + FB), os 2 livros. Pedido do André (22/jun):
soltar 1 peça a cada 4 minutos. Idempotente (pula o que já saiu), logado, resiliente
(um post que falha NÃO para o drip). YouTube fica de fora (cota → tarefa à parte)."""
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
INTERVAL = 120  # 2 minutos (ajustado a pedido do André)
SLUGS = ['arte-da-guerra-vencer-sem-lutar', 'ponerologia-pathocracia']
JÁ_FEITO = {('ig', 'arte-da-guerra-vencer-sem-lutar', 1),   # verificados à mão antes do drip
            ('fb', 'arte-da-guerra-vencer-sem-lutar', 1)}


def log(m):
    print(f'[{datetime.datetime.now():%H:%M:%S}] {m}', flush=True)


def ig_ja(slug, idx):
    sf = ROOT / '_shorts' / f'{slug}_instagram_state.json'
    return sf.exists() and str(idx) in json.loads(sf.read_text())


def fb_ja(slug, idx):
    sf = ROOT / '_shorts' / f'{slug}_fbreels_state.json'
    return sf.exists() and str(idx) in json.loads(sf.read_text())


def ig_post(slug, idx):
    cfg = json.loads((ROOT / 'roteiros' / f'{slug}.json').read_text(encoding='utf-8'))
    mp4 = ROOT / '_shorts' / f'{slug}_{idx:02d}.mp4'
    mid = ig.post_reel(str(mp4), ig.caption_for(cfg, idx))
    if mid:
        sf = ROOT / '_shorts' / f'{slug}_instagram_state.json'
        st = json.loads(sf.read_text()) if sf.exists() else {}
        st[str(idx)] = mid
        sf.write_text(json.dumps(st, ensure_ascii=False, indent=1), encoding='utf-8')
    return mid


# fila interleaved: por cena, IG e FB dos 2 livros (exclui os já feitos)
fila = []
for idx in range(1, 11):
    for slug in SLUGS:
        for plat in ('ig', 'fb'):
            if (plat, slug, idx) not in JÁ_FEITO:
                fila.append((plat, slug, idx))

log(f'DRIP iniciado — {len(fila)} reels, 1 a cada {INTERVAL//60} min (~{len(fila)*INTERVAL//60} min)')
feitos = 0
for n, (plat, slug, idx) in enumerate(fila, 1):
    try:
        if plat == 'ig':
            if ig_ja(slug, idx):
                log(f'{n}/{len(fila)} SKIP ig {slug} cena {idx}')
                continue
            mid = ig_post(slug, idx)
            log(f'{n}/{len(fila)} IG {slug} cena {idx} -> {mid}')
        else:
            if fb_ja(slug, idx):
                log(f'{n}/{len(fila)} SKIP fb {slug} cena {idx}')
                continue
            fr.postar_reels(slug, idxs=[idx])     # idempotente internamente
            log(f'{n}/{len(fila)} FB {slug} cena {idx} ok')
        feitos += 1
    except Exception as e:
        log(f'{n}/{len(fila)} ERRO {plat} {slug} {idx}: {type(e).__name__}: {str(e)[:90]}')
    if n < len(fila):
        time.sleep(INTERVAL)
log(f'DRIP DONE — {feitos} reels processados')
