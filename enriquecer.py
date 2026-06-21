# -*- coding: utf-8 -*-
"""Enriquece os cards JÁ profundos de um livro até o padrão-ouro, SEM reescrever
o corpo: adiciona `emph` (curado, trecho literal do título → itálico verde) e
marca `warn` automaticamente quando a dica é de alerta. Mantém ic/t/b/tip.

Uso (programático): EMPH[slug] = {cap_slug: ["emph c1","emph c2",...]} ; enrich(slug)
Escreve _kit_preview/text/<slug>.json no formato combinado p/ o aplicar_texto.
"""
import sys, json, importlib, re
from pathlib import Path

BASE = Path(__file__).parent
sys.stdout.reconfigure(encoding='utf-8')
TEXT = BASE / '_kit_preview' / 'text'

# dica de alerta → card vira coral (warn). Rótulos perigo no início do tip.
WARN_RX = re.compile(r'<strong>\s*(sinal de alerta|cuidado|armadilha|perigo|risco)', re.IGNORECASE)


def enrich(slug, emph_map):
    d = importlib.import_module(slug.replace('-', '_') + '_data')
    out = {}
    for ch in d.CHAPTERS:
        cap = ch['slug']
        emphs = emph_map.get(cap, [])
        cards = []
        for i, c in enumerate(ch['cards']):
            nc = {'ic': c['ic'], 't': c['t']}
            e = emphs[i] if i < len(emphs) else ''
            if e and e in c['t']:
                nc['emph'] = e
            elif e:
                print(f"  [!] {slug}/{cap} card{i+1}: emph {e!r} não está em t={c['t']!r}")
            nc['b'] = c['b']
            if c.get('tip'):
                nc['tip'] = c['tip']
                if WARN_RX.search(c['tip']):
                    nc['warn'] = True
            if c.get('wide'):
                nc['wide'] = True
            cards.append(nc)
        out[cap] = {'cards': cards}
    TEXT.mkdir(parents=True, exist_ok=True)
    (TEXT / f'{slug}.json').write_text(json.dumps(out, ensure_ascii=False), encoding='utf-8', newline='\n')
    nwarn = sum(1 for ch in out.values() for c in ch['cards'] if c.get('warn'))
    nemph = sum(1 for ch in out.values() for c in ch['cards'] if c.get('emph'))
    print(f'{slug}: {len(out)} caps | emph {nemph} | warn {nwarn} → text/{slug}.json')


if __name__ == '__main__':
    from emph_data import EMPH
    for slug in (sys.argv[1:] or sorted(EMPH)):
        if slug in EMPH:
            enrich(slug, EMPH[slug])
        else:
            print(f'sem EMPH p/ {slug}')
