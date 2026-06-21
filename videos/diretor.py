# -*- coding: utf-8 -*-
"""Diretor — monta o PLANO cena-a-cena (shot list) antes de "gravar". Local, grátis.

Torna EXPLÍCITO o que hoje é implícito no roteiro: para cada cena, os 4 campos que
um diretor decide — TEXTO (narração), VISUAL (tratamento de imagem), VOZ (tom) e
SOM (deixa de sonoplastia). Reusa `cinegrafista.tratamento` para o visual (decisão
única, sem duplicar) e marca o ritmo anti-slop (cena estática = risco).

Uso:  python diretor.py roteiros/<slug>.json
"""
import json
import sys
from pathlib import Path

import cinegrafista

ROOT = Path(__file__).parent

# Tom de voz por papel da cena (direção para o Narrador).
_TOM = {
    'abertura':     'impactante, direto — fisga nos 3 primeiros segundos',
    'conceito':     'explicativo e claro, ritmo firme',
    'encerramento': 'convite caloroso — fecha o loop e chama o próximo',
}

# Deixa de SOM por papel da cena (direção para o Sonoplasta).
_SOM = {
    'abertura':     'riser de entrada + respiro antes da 1ª palavra',
    'conceito':     'batida sutil de transição na virada',
    'encerramento': 'resolução harmônica + marca sonora de encerramento',
}


def _visual(cena, modo, depthflow_ok):
    """Tratamento visual da cena via decisão única do Cinegrafista."""
    return cinegrafista.tratamento(
        modo,
        tem_imagem=bool(cena.get('img')),
        motion_pago=bool(cena.get('motion')),
        depthflow_ok=depthflow_ok,
    )


def montar_shot_list(cenas, modo='normal', depthflow_ok=None):
    """-> lista de shots {n, tipo, texto, visual, voz, som}. Um por cena."""
    if depthflow_ok is None:
        depthflow_ok = cinegrafista.depthflow_disponivel()
    shots = []
    for i, c in enumerate(cenas or []):
        tipo = c.get('tipo', 'conceito')
        shots.append({
            'n': i + 1,
            'tipo': tipo,
            'texto': c.get('narracao', '') or '(sem narração)',
            'visual': _visual(c, modo, depthflow_ok),
            'voz': _TOM.get(tipo, _TOM['conceito']),
            'som': _SOM.get(tipo, _SOM['conceito']),
        })
    return shots


def revisar_ritmo(shot_list):
    """-> avisos anti-slop: cena 'still' (slide chapado, sem movimento) é risco de
    'tudo IA'/monotonia. Não bloqueia — orienta o Diretor a dar movimento/imagem."""
    avisos = []
    for s in shot_list:
        if s['visual'] == 'still':
            avisos.append(f"cena {s['n']} ({s['tipo']}): estática sem imagem — "
                          f"considere imagem + parallax/Ken Burns (anti-slop)")
    return avisos


def do_roteiro(cfg, modo='normal', depthflow_ok=None):
    """-> {slug, titulo, modo, shot_list, avisos} a partir de um roteiro carregado."""
    shot_list = montar_shot_list(cfg.get('cenas', []), modo=modo, depthflow_ok=depthflow_ok)
    return {
        'slug': cfg.get('slug', ''),
        'titulo': cfg.get('titulo', ''),
        'modo': modo,
        'shot_list': shot_list,
        'avisos': revisar_ritmo(shot_list),
    }


def main():
    if len(sys.argv) < 2:
        sys.exit('uso: python diretor.py <roteiro.json>')
    cfg = json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
    r = do_roteiro(cfg)
    print(f"=== Diretor — plano de '{r['titulo']}' (modo {r['modo']}) ===")
    for s in r['shot_list']:
        print(f"\n[{s['n']:02d}] {s['tipo'].upper()}  · visual: {s['visual']}")
        print(f"     TEXTO: {s['texto'][:80]}")
        print(f"     VOZ  : {s['voz']}")
        print(f"     SOM  : {s['som']}")
    if r['avisos']:
        print(f"\nRITMO — {len(r['avisos'])} aviso(s):")
        for a in r['avisos']:
            print('  [aviso]', a)


if __name__ == '__main__':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    main()
