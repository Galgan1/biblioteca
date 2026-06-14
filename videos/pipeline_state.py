# -*- coding: utf-8 -*-
"""Rastreador de estado da pipeline por slug.

Cada etapa registra status (done/pending/blocked/skipped) + timestamp + dados opcionais.
Arquivo físico: biblioteca/pipeline/state/<slug>.json

Uso (nos scripts de produção):
  import pipeline_state as ps
  ps.mark_done('arte-da-guerra', 'uploaded', data={'video_id': 'abc123'})
  ps.is_done('arte-da-guerra', 'uploaded')   # True
  ps.summary('arte-da-guerra')               # imprime o estado completo
  ps.pending_stages('arte-da-guerra')        # ['shorts', 'scheduled', ...]

Uso (no maestro — pular etapas já feitas):
  Leia `pipeline/state/<slug>.json` para saber o que retomar.
  Stages: skill · biblioteca · video_built · uploaded · shorts · scheduled · instagram · tiktok · facebook
"""
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent          # biblioteca/
STATE_DIR = ROOT / 'pipeline' / 'state'

STAGES = [
    'skill',        # book-to-skill concluído
    'biblioteca',   # publicar_livro.py --deploy OK
    'video_built',  # gerar_video.py finalizado
    'uploaded',     # upload_youtube.py → video_id
    'shorts',       # produzir_shorts.py concluído
    'scheduled',    # agendar_lote.py + enfileirar_comentarios OK
    'instagram',    # instagram_post.py (reel + carrossel)
    'tiktok',       # tiktok_post.py
    'facebook',     # facebook_post.py
]


def _path(slug):
    return STATE_DIR / f'{slug}.json'


def get_state(slug):
    p = _path(slug)
    return json.loads(p.read_text(encoding='utf-8')) if p.exists() else {}


def is_done(slug, stage):
    return get_state(slug).get(stage, {}).get('status') == 'done'


EVENTS_FILE = ROOT / 'pipeline' / 'events.jsonl'


def _log(slug, stage, status, detail=None):
    """Telemetria: append de evento estruturado em pipeline/events.jsonl."""
    EVENTS_FILE.parent.mkdir(parents=True, exist_ok=True)
    ev = {'ts': datetime.now(timezone.utc).isoformat(), 'slug': slug,
          'stage': stage, 'status': status}
    if detail:
        ev['detail'] = detail
    with open(EVENTS_FILE, 'a', encoding='utf-8') as f:
        f.write(json.dumps(ev, ensure_ascii=False) + '\n')


def mark_done(slug, stage, data=None, run_id=None, cost_usd=None):
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    state = get_state(slug)
    entry = {'status': 'done', 'ts': datetime.now(timezone.utc).isoformat()}
    if data:
        entry['data'] = data
    if run_id:
        entry['run_id'] = run_id
    if cost_usd is not None:
        entry['cost_usd'] = cost_usd
    state[stage] = entry
    state.setdefault('slug', slug)
    _path(slug).write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding='utf-8')
    _log(slug, stage, 'done', data)


def total_cost(slug) -> float:
    """Soma cost_usd de todas as entradas done do slug."""
    state = get_state(slug)
    return round(sum(
        e.get('cost_usd', 0.0)
        for e in state.values()
        if isinstance(e, dict) and e.get('cost_usd') is not None
    ), 4)


def mark_blocked(slug, stage, reason):
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    state = get_state(slug)
    state[stage] = {'status': 'blocked', 'reason': reason,
                    'ts': datetime.now(timezone.utc).isoformat()}
    state.setdefault('slug', slug)
    _path(slug).write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding='utf-8')
    _log(slug, stage, 'blocked', {'reason': reason})


def mark_skipped(slug, stage, reason=''):
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    state = get_state(slug)
    state[stage] = {'status': 'skipped', 'reason': reason,
                    'ts': datetime.now(timezone.utc).isoformat()}
    state.setdefault('slug', slug)
    _path(slug).write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding='utf-8')
    _log(slug, stage, 'skipped', {'reason': reason} if reason else None)


def pending_stages(slug):
    """Retorna as etapas que ainda não têm status 'done'."""
    state = get_state(slug)
    return [s for s in STAGES if state.get(s, {}).get('status') != 'done']


def summary(slug):
    state = get_state(slug)
    lines = [f"Pipeline · {slug}"]
    for s in STAGES:
        entry = state.get(s, {})
        status = entry.get('status', 'pending')
        data = entry.get('data')
        extra = f"  → {data}" if data else ''
        ts = entry.get('ts', '')[:10]
        marker = {'done': '✓', 'blocked': '✗', 'skipped': '–', 'pending': '·'}[status]
        lines.append(f"  {marker} {s:<16} {status:<8} {ts}{extra}")
    return '\n'.join(lines)


if __name__ == '__main__':
    import sys
    slug = sys.argv[1] if len(sys.argv) > 1 else 'arte-da-guerra'
    print(summary(slug))
    pend = pending_stages(slug)
    if pend:
        print(f"\nPendentes: {pend}")
