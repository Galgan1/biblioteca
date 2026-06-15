# -*- coding: utf-8 -*-
"""Orquestrador programático — fan-out paralelo das lanes de produção.

Recebe um slug, lê pipeline_state para saber o que já foi feito, e executa
os scripts Python em paralelo via ThreadPoolExecutor para as lanes ativas.

A parte CRIATIVA (escrever roteiro.json, <slug>_data.py) ainda é feita pelo
maestro (Claude agent). Este script cuida da EXECUÇÃO MECÂNICA pós-criação.

Uso:
  python orquestrador.py <slug>                          # tudo pendente
  python orquestrador.py <slug> --stages biblioteca,video_built  # só essas
  python orquestrador.py <slug> --dry-run                # mostra o que faria
"""
import os
import sys
import json
import logging
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

# Garante UTF-8 no Windows
try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

ROOT_VIDEOS = Path(__file__).parent          # biblioteca/videos/
ROOT = ROOT_VIDEOS.parent                    # biblioteca/

sys.path.insert(0, str(ROOT_VIDEOS))
import pipeline_state as ps
from dag import DAG, ready_stages

logging.basicConfig(
    level=logging.INFO,
    format='[orq] %(message)s',
    stream=sys.stdout,
)
log = logging.getLogger('orq')

CANAL_STATE = ROOT_VIDEOS / 'canal-state.json'

# Mapeamento stage → lane (para filtrar por lanes ativas)
STAGE_LANE = {
    'skill':       None,        # sempre (não é uma lane)
    'biblioteca':  'biblioteca',
    'video_built': 'youtube',
    'uploaded':    'youtube',
    'shorts':      'youtube',
    'scheduled':   'youtube',
    'instagram':   'instagram',
    'tiktok':      'tiktok',
    'facebook':    'facebook',
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def get_active_lanes() -> set:
    """Lê canal-state.json e retorna o set de lanes com status == 'active'."""
    try:
        data = json.loads(CANAL_STATE.read_text(encoding='utf-8'))
        return {lane for lane, cfg in data.get('lanes', {}).items()
                if cfg.get('status') == 'active'}
    except Exception as e:
        log.warning(f"Não conseguiu ler canal-state.json: {e}. Assumindo todas ativas.")
        return {'biblioteca', 'youtube', 'instagram', 'facebook'}


def _run(cmd: list, cwd: Path, stage: str, slug: str, dry_run: bool) -> dict:
    """Executa um subprocess e retorna dict com status/stdout/stderr/elapsed."""
    if dry_run:
        log.info(f"[dry-run] {stage}: {' '.join(cmd)}  (cwd={cwd})")
        return {'status': 'dry-run', 'stage': stage}

    log.info(f"iniciando {stage}...")
    t0 = time.monotonic()
    result = subprocess.run(
        cmd,
        cwd=str(cwd),
        capture_output=True,
        text=True,
        encoding='utf-8',
        errors='replace',
    )
    elapsed = time.monotonic() - t0

    if result.returncode == 0:
        log.info(f"✓ {stage} done ({elapsed:.1f}s)")
        return {'status': 'done', 'stage': stage, 'elapsed': elapsed,
                'stdout': result.stdout}
    else:
        reason = (result.stderr or result.stdout or 'exit code != 0')[:300]
        log.error(f"✗ {stage} falhou ({elapsed:.1f}s): {reason}")
        ps.mark_blocked(slug, stage, reason)
        return {'status': 'error', 'stage': stage, 'elapsed': elapsed,
                'stderr': result.stderr}


# ---------------------------------------------------------------------------
# Runners por stage
# ---------------------------------------------------------------------------

def run_biblioteca(slug: str, dry_run: bool) -> dict:
    if ps.is_done(slug, 'biblioteca'):
        return {'status': 'skipped', 'stage': 'biblioteca'}
    cmd = [sys.executable, 'publicar_livro.py', slug, '--deploy']
    r = _run(cmd, ROOT, 'biblioteca', slug, dry_run)
    if r['status'] == 'done':
        ps.mark_done(slug, 'biblioteca')
    return r


def run_video_build(slug: str, dry_run: bool) -> dict:
    if ps.is_done(slug, 'video_built'):
        return {'status': 'skipped', 'stage': 'video_built'}
    roteiro = ROOT_VIDEOS / 'roteiros' / f'{slug}.json'
    cmd = [sys.executable, 'gerar_video.py', str(roteiro)]
    r = _run(cmd, ROOT_VIDEOS, 'video_built', slug, dry_run)
    if r['status'] == 'done':
        ps.mark_done(slug, 'video_built')
    return r


def run_upload(slug: str, dry_run: bool) -> dict:
    if ps.is_done(slug, 'uploaded'):
        return {'status': 'skipped', 'stage': 'uploaded'}
    video = ROOT_VIDEOS / f'{slug}.mp4'
    roteiro = ROOT_VIDEOS / 'roteiros' / f'{slug}.json'
    cmd = [sys.executable, 'upload_youtube.py', str(video), str(roteiro)]
    r = _run(cmd, ROOT_VIDEOS, 'uploaded', slug, dry_run)
    # upload_youtube.py já chama ps.mark_done internamente com o video_id.
    # Se dry-run, apenas retornamos sem tocar o estado.
    return r


def run_shorts(slug: str, dry_run: bool) -> dict:
    if ps.is_done(slug, 'shorts'):
        return {'status': 'skipped', 'stage': 'shorts'}
    # Obtém video_id do estado persistido (gravado pelo upload_youtube.py)
    state = ps.get_state(slug)
    video_id = state.get('uploaded', {}).get('data', {}).get('video_id', '')
    if not video_id and not dry_run:
        reason = 'video_id ausente em pipeline_state — rode uploaded primeiro'
        ps.mark_blocked(slug, 'shorts', reason)
        return {'status': 'error', 'stage': 'shorts', 'stderr': reason}
    cmd = [sys.executable, 'produzir_shorts.py', slug, video_id or '<video_id>']
    r = _run(cmd, ROOT_VIDEOS, 'shorts', slug, dry_run)
    if r['status'] == 'done':
        ps.mark_done(slug, 'shorts')
    return r


def run_carrossel(slug: str, dry_run: bool) -> dict:
    """Instagram — gerar_carrossel.py roda na raiz do projeto."""
    if ps.is_done(slug, 'instagram'):
        return {'status': 'skipped', 'stage': 'instagram'}
    cmd = [sys.executable, 'gerar_carrossel.py', slug]
    r = _run(cmd, ROOT, 'instagram', slug, dry_run)
    if r['status'] == 'done':
        ps.mark_done(slug, 'instagram')
    return r


def run_facebook(slug: str, dry_run: bool) -> dict:
    """Facebook — vídeo longo NATIVO + CTA no 1º comentário (doutrina premium).
    Depende de 'uploaded' (precisa do video_id do YouTube p/ o link no comentário)."""
    if ps.is_done(slug, 'facebook'):
        return {'status': 'skipped', 'stage': 'facebook'}
    state = ps.get_state(slug)
    video_id = state.get('uploaded', {}).get('data', {}).get('video_id', '')
    if not video_id and not dry_run:
        reason = 'video_id ausente em pipeline_state — rode uploaded primeiro'
        ps.mark_blocked(slug, 'facebook', reason)
        return {'status': 'error', 'stage': 'facebook', 'stderr': reason}
    cmd = [sys.executable, 'facebook_publicar.py', slug, video_id or '<video_id>']
    if dry_run:
        cmd.append('--dry-run')
    r = _run(cmd, ROOT_VIDEOS, 'facebook', slug, dry_run)
    if r['status'] == 'done':
        ps.mark_done(slug, 'facebook')
    return r


# ---------------------------------------------------------------------------
# Mapa stage → função runner
# ---------------------------------------------------------------------------

RUNNERS = {
    'biblioteca':  run_biblioteca,
    'video_built': run_video_build,
    'uploaded':    run_upload,
    'shorts':      run_shorts,
    'instagram':   run_carrossel,
    'facebook':    run_facebook,
}

# Stages sem runner próprio no orquestrador (feitos manualmente ou por outro script)
UNMANAGED = {'skill', 'scheduled', 'tiktok'}


# ---------------------------------------------------------------------------
# Executor principal
# ---------------------------------------------------------------------------

def main(slug: str, stages: list = None, dry_run: bool = False):
    from cost_tracker import new_run_id
    run_id = new_run_id()
    os.environ['PIPELINE_RUN_ID'] = run_id
    os.environ['PIPELINE_SLUG'] = slug

    active_lanes = get_active_lanes()
    log.info(f"slug={slug} run_id={run_id} | lanes ativas={sorted(active_lanes)} | dry_run={dry_run}")

    # Stages já concluídos
    done = {s for s in DAG if ps.is_done(slug, s)}
    log.info(f"stages já done: {sorted(done) or '(nenhum)'}")

    # Filtra stages elegíveis
    if stages:
        requested = set(stages)
    else:
        requested = set(DAG.keys()) - UNMANAGED

    def stage_eligible(s: str) -> bool:
        if s in done:
            return False
        if s in UNMANAGED:
            return False
        if s not in requested:
            return False
        lane = STAGE_LANE.get(s)
        if lane and lane not in active_lanes:
            log.info(f"  pulando {s} (lane '{lane}' não está ativa)")
            return False
        return True

    # Executa respeitando dependências (loop até não restar nada elegível pronto)
    max_rounds = len(DAG) + 1
    for _ in range(max_rounds):
        candidates = [s for s in ready_stages(DAG, done) if stage_eligible(s)]
        if not candidates:
            break

        log.info(f"rodando em paralelo: {candidates}")
        futures = {}
        with ThreadPoolExecutor(max_workers=4) as pool:
            for s in candidates:
                runner = RUNNERS.get(s)
                if runner is None:
                    log.info(f"  sem runner para {s} — pulando")
                    done.add(s)
                    continue
                futures[pool.submit(runner, slug, dry_run)] = s

            for fut in as_completed(futures):
                s = futures[fut]
                try:
                    result = fut.result()
                    status = result.get('status', '?')
                    if status in ('done', 'skipped', 'dry-run'):
                        done.add(s)
                except Exception as exc:
                    log.error(f"exceção em {s}: {exc}")
                    ps.mark_blocked(slug, s, str(exc)[:300])

    # Resumo final
    print()
    print(ps.summary(slug))
    pending = ps.pending_stages(slug)
    if pending:
        print(f"\nPendentes: {pending}")
    else:
        print("\nPipeline completo!")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='Orquestrador programático do pipeline Minuto Real'
    )
    parser.add_argument('slug', help='Slug do livro (ex: arte-da-guerra)')
    parser.add_argument(
        '--stages',
        help='Subset de stages a executar, separados por vírgula (ex: biblioteca,video_built)',
        default=None,
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Mostra o que seria executado sem de fato rodar',
    )
    args = parser.parse_args()

    stage_list = [s.strip() for s in args.stages.split(',')] if args.stages else None
    main(args.slug, stages=stage_list, dry_run=args.dry_run)
