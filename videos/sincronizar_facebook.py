# -*- coding: utf-8 -*-
"""sincronizar_facebook.py — sincroniza o Facebook com TUDO que já produzimos,
RESPEITANDO O TIMING: posta os Reels (Shorts 9:16 já renderizados) que ainda não
saíram, em LOTES diários (default 3), interleaved por livro (variedade no feed).
Idempotente (_shorts/<slug>_fbreels_state.json — não re-posta), resiliente (1 falha
não para o lote), logado. Roda LOCAL (assets + segredos vivem aqui). Feito p/ um
schtasks diário esvaziar a fila sem inundar a Página (o FB Reels publica na hora —
não há agendamento por API, por isso o drip é o mecanismo de timing).

Uso:
  python sincronizar_facebook.py --status         # mostra a fila pendente, NÃO posta
  python sincronizar_facebook.py [--n 3]          # posta os próximos N (default 3)
  python sincronizar_facebook.py --n 3 --dry-run  # valida sem publicar
"""
import sys
import json
import re
import datetime
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.stderr.reconfigure(encoding='utf-8', errors='replace')

ROOT = Path(__file__).parent
SH = ROOT / '_shorts'
ROT = ROOT / 'roteiros'
_SUFIXO = '_fbreels_state.json'


def _clipes_por_slug():
    """{slug: [idxs]} dos Reels renderizados em _shorts/<slug>_NN.mp4 que TÊM roteiro."""
    out = {}
    for f in SH.glob('*_[0-9][0-9].mp4'):
        m = re.match(r'(.+)_(\d{2})$', f.stem)
        if not m:
            continue
        slug, idx = m.group(1), int(m.group(2))
        if (ROT / f'{slug}.json').exists():
            out.setdefault(slug, []).append(idx)
    return {s: sorted(v) for s, v in out.items()}


def _feito_por_slug():
    """{slug: set(idxs já no FB)} lidos dos _shorts/<slug>_fbreels_state.json."""
    out = {}
    for f in SH.glob('*' + _SUFIXO):
        slug = f.name[:-len(_SUFIXO)]
        try:
            out[slug] = {int(k) for k in json.loads(f.read_text(encoding='utf-8'))}
        except Exception:
            out[slug] = set()
    return out


def fila_pendente(clipes, feito):
    """Fila interleaved (round-robin por livro): 1º clipe pendente de cada livro, depois
    2º de cada, etc. — variedade no feed em vez de 4 reels do mesmo livro seguidos.
    clipes={slug:[idxs]}, feito={slug:set(idxs no FB)}. Pula o que já saiu."""
    pend = {s: [i for i in ix if i not in feito.get(s, set())] for s, ix in clipes.items()}
    fila, p = [], 0
    while any(len(v) > p for v in pend.values()):
        for s in sorted(pend):
            if len(pend[s]) > p:
                fila.append((s, pend[s][p]))
        p += 1
    return fila


def _log(m):
    print(f'[{datetime.datetime.now():%H:%M:%S}] {m}', flush=True)


def main(argv):
    n = int(argv[argv.index('--n') + 1]) if '--n' in argv else 3
    dry = '--dry-run' in argv
    fila = fila_pendente(_clipes_por_slug(), _feito_por_slug())
    if '--status' in argv:
        print(f'fila pendente no Facebook: {len(fila)} reels')
        for s, i in fila:
            print(f'  {s} cena {i}')
        return 0
    import facebook_reels as fr
    lote = fila[:n]
    _log(f'sincronizar_facebook: {len(fila)} pendentes; postando {len(lote)} (n={n}, dry={dry})')
    feitos = 0
    for s, i in lote:
        try:
            fr.postar_reels(s, idxs=[i], dry_run=dry)
            feitos += 1
            _log(f'OK {s} cena {i}')
        except Exception as e:
            _log(f'ERRO {s} cena {i}: {type(e).__name__}: {str(e)[:100]}')
    _log(f'lote done — {feitos}/{len(lote)} postados | restam ~{len(fila) - feitos} na fila')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
