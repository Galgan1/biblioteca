# -*- coding: utf-8 -*-
"""Gera LOCAL os shorts (1 por cena-conceito) dos 2 vídeos. NÃO publica, NÃO usa fal.
Reaproveita a narração cacheada em _work quando ela é do build mais recente (Ponerologia)
= custo zero de eleven. Pedido do André (22/jun): gerar tudo local p/ revisão antes de publicar."""
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT))
import gerar_short

WORK = ROOT / '_work'
SH = ROOT / '_shorts'
SH.mkdir(exist_ok=True)

# reuse=True só p/ o slug cuja narração está AGORA em _work (último build = Ponerologia)
PLAN = [('ponerologia-pathocracia', True), ('arte-da-guerra-vencer-sem-lutar', False)]

total = 0
for slug, reuse in PLAN:
    cfg = json.loads((ROOT / 'roteiros' / f'{slug}.json').read_text(encoding='utf-8'))
    idxs = [i for i, c in enumerate(cfg['cenas']) if c.get('tipo') == 'conceito']
    print(f'=== {slug}: {len(idxs)} shorts (cenas {idxs}) ===', flush=True)
    for i in idxs:
        if reuse:                                   # copia a narração já paga → gerar_short pula o tts
            src, dst = WORK / f'a{i:02d}.mp3', SH / f'{slug}_{i:02d}_aud.mp3'
            if src.exists() and not dst.exists():
                shutil.copy(src, dst)
        try:
            gerar_short.main(slug, i)
            total += 1
        except Exception as e:
            print(f'  [!] short cena {i} FALHOU: {type(e).__name__}: {str(e)[:90]}', flush=True)

print(f'SHORTS DONE — {total} gerados em _shorts/', flush=True)
