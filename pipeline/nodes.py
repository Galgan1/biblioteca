# -*- coding: utf-8 -*-
"""Funções de nó para o StateGraph do pipeline Minuto Real.

Cada função recebe o PipelineState, executa um stage do pipeline e devolve
um dict com os campos de estado a serem atualizados.

As funções chamam os scripts Python existentes via subprocess — não duplicam
lógica. O grafo (graph.py) conecta esses nós com checkpointing SQLite.
"""

import json
import os
import subprocess
import sys
import time
from pathlib import Path
from typing import Optional

ROOT_VIDEOS = Path(__file__).parent.parent / 'videos'
ROOT = Path(__file__).parent.parent

sys.path.insert(0, str(ROOT_VIDEOS))


def _run(cmd: list, cwd: Path, label: str) -> tuple[bool, str]:
    """Executa subprocess, retorna (sucesso, stderr_ou_stdout)."""
    print(f'[pipeline] {label}...')
    t0 = time.monotonic()
    r = subprocess.run(
        cmd,
        cwd=str(cwd),
        capture_output=True,
        text=True,
        encoding='utf-8',
        errors='replace',
    )
    elapsed = time.monotonic() - t0
    if r.returncode == 0:
        print(f'[pipeline] ✓ {label} ({elapsed:.1f}s)')
        return True, r.stdout
    err = (r.stderr or r.stdout or f'exit {r.returncode}')[:400]
    print(f'[pipeline] ✗ {label} ({elapsed:.1f}s): {err}')
    return False, err


def _get_video_id(slug: str) -> Optional[str]:
    """Lê video_id do pipeline_state persistido."""
    import pipeline_state as ps

    state = ps.get_state(slug)
    return state.get('uploaded', {}).get('data', {}).get('video_id')


# ---------------------------------------------------------------------------
# Nós do grafo
# ---------------------------------------------------------------------------


def node_load_state(state: dict) -> dict:
    """Carrega o estado atual do pipeline_state para o slug."""
    import pipeline_state as ps

    slug = state['slug']
    run_id = state.get('run_id', '')
    # Propaga run_id e slug via env para todos os subprocessos deste grafo
    if run_id:
        os.environ['PIPELINE_RUN_ID'] = run_id
    os.environ['PIPELINE_SLUG'] = slug
    stages_done = [s for s in ps.STAGES if ps.is_done(slug, s)]
    video_id = _get_video_id(slug)
    print(f'[pipeline] slug={slug!r} run_id={run_id!r} | stages done: {stages_done}')
    return {
        'stages_done': stages_done,
        'video_id': video_id,
    }


def node_validate(state: dict) -> dict:
    """Valida que o roteiro.json existe e é válido (contracts.py)."""
    slug = state['slug']
    roteiro = ROOT_VIDEOS / 'roteiros' / f'{slug}.json'
    if not roteiro.exists():
        return {'errors': state.get('errors', []) + [f'roteiro.json não encontrado: {roteiro}']}

    try:
        sys.path.insert(0, str(ROOT_VIDEOS))
        from contracts import load_roteiro

        load_roteiro(roteiro)
    except Exception as e:
        # Aviso não-fatal (contracts é best-effort)
        print(f'[pipeline] aviso contracts: {e}')

    return {}


def node_run_biblioteca(state: dict) -> dict:
    """Executa publicar_livro.py --deploy para publicar no site."""
    import pipeline_state as ps

    slug = state['slug']
    if ps.is_done(slug, 'biblioteca'):
        return {}
    ok, out = _run(
        [sys.executable, 'publicar_livro.py', slug, '--deploy'],
        ROOT,
        'biblioteca',
    )
    if ok:
        ps.mark_done(slug, 'biblioteca')
        return {}
    return {'errors': state.get('errors', []) + [f'biblioteca: {out}']}


def node_run_video_build(state: dict) -> dict:
    """Executa gerar_video.py para construir o arquivo MP4."""
    import pipeline_state as ps

    slug = state['slug']
    if ps.is_done(slug, 'video_built'):
        return {}
    roteiro = ROOT_VIDEOS / 'roteiros' / f'{slug}.json'
    ok, out = _run(
        [sys.executable, 'gerar_video.py', str(roteiro)],
        ROOT_VIDEOS,
        'video_built',
    )
    if ok:
        ps.mark_done(slug, 'video_built')
        return {}
    return {'errors': state.get('errors', []) + [f'video_built: {out}']}


def node_run_upload(state: dict) -> dict:
    """Executa upload_youtube.py e captura o video_id."""
    import pipeline_state as ps

    slug = state['slug']
    if ps.is_done(slug, 'uploaded'):
        return {'video_id': _get_video_id(slug)}

    video = ROOT_VIDEOS / f'{slug}.mp4'
    roteiro = ROOT_VIDEOS / 'roteiros' / f'{slug}.json'
    if not video.exists():
        return {'errors': state.get('errors', []) + [f'MP4 não encontrado: {video}']}

    ok, out = _run(
        [sys.executable, 'upload_youtube.py', str(video), str(roteiro)],
        ROOT_VIDEOS,
        'uploaded',
    )
    if ok:
        video_id = _get_video_id(slug)
        return {'video_id': video_id}
    return {'errors': state.get('errors', []) + [f'upload: {out}']}


def node_run_shorts(state: dict) -> dict:
    """Executa produzir_shorts.py."""
    import pipeline_state as ps

    slug = state['slug']
    if ps.is_done(slug, 'shorts'):
        return {}
    video_id = state.get('video_id') or _get_video_id(slug)
    if not video_id:
        return {'errors': state.get('errors', []) + ['shorts: video_id ausente']}
    ok, out = _run(
        [sys.executable, 'produzir_shorts.py', slug, video_id],
        ROOT_VIDEOS,
        'shorts',
    )
    if not ok:
        return {'errors': state.get('errors', []) + [f'shorts: {out}']}
    return {}


def node_run_carrossel(state: dict) -> dict:
    """Executa gerar_carrossel.py para o Instagram."""
    import pipeline_state as ps

    slug = state['slug']
    if ps.is_done(slug, 'instagram'):
        return {}
    ok, out = _run(
        [sys.executable, 'gerar_carrossel.py', slug],
        ROOT,
        'instagram',
    )
    if not ok:
        return {'errors': state.get('errors', []) + [f'instagram: {out}']}
    return {}


def node_verify(state: dict) -> dict:
    """Re-lê pipeline_state e atualiza stages_done."""
    import pipeline_state as ps

    slug = state['slug']
    stages_done = [s for s in ps.STAGES if ps.is_done(slug, s)]
    pending = [s for s in ps.STAGES if s not in stages_done]

    print()
    print(ps.summary(slug))
    if pending:
        print(f'\nPendentes: {pending}')
    else:
        print('\nPipeline completo!')

    errors = state.get('errors', [])
    if errors:
        print(f'\nErros registrados:')
        for e in errors:
            print(f'  ✗ {e}')

    return {'stages_done': stages_done}
