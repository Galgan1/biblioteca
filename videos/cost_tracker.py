# -*- coding: utf-8 -*-
"""Rastreador de custo por operação de API externa.

Persiste em analytics/custos.json, indexado por run_id.

Preços embutidos (jun/2026, estimados):
  google_imagen  US$0.04 / imagem
  google_veo_8s  US$1.20 / clip de 8s (fast)
  google_tts_1k  US$0.016 / 1 000 chars (Chirp3-HD)
  youtube_upload US$0.00

Uso (nos scripts de geração):
  from cost_tracker import new_run_id, record_cost
  run_id = new_run_id()
  record_cost(run_id, slug='arte-da-guerra', api='google_imagen', units=5)

Consulta:
  from cost_tracker import get_run_cost, get_slug_total, print_costs
  print_costs()
"""
import json
import os
import uuid
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent   # biblioteca/
COSTS_FILE = ROOT / 'analytics' / 'custos.json'

PRICES = {
    'google_imagen':  0.04,    # por imagem
    'google_veo_8s':  1.20,    # por clip de 8s
    'google_tts_1k':  0.016,   # por 1 000 caracteres
    'youtube_upload': 0.00,
    'instagram_api':  0.00,
}


def new_run_id() -> str:
    return str(uuid.uuid4())[:8]


def _env_run_id() -> str:
    """Lê PIPELINE_RUN_ID do ambiente, ou gera um novo."""
    return os.environ.get('PIPELINE_RUN_ID') or new_run_id()


def _env_slug() -> str:
    return os.environ.get('PIPELINE_SLUG', 'unknown')


def _load() -> dict:
    COSTS_FILE.parent.mkdir(parents=True, exist_ok=True)
    if COSTS_FILE.exists():
        try:
            return json.loads(COSTS_FILE.read_text(encoding='utf-8'))
        except Exception:
            pass
    return {'runs': {}, 'by_slug': {}}


def _save(data: dict) -> None:
    try:
        tmp = COSTS_FILE.with_suffix('.json.tmp')
        tmp.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding='utf-8')
        tmp.replace(COSTS_FILE)
    except Exception as e:
        print(f'[cost_tracker] aviso: não salvou — {e}')


def record_cost(run_id: str = None, slug: str = None, api: str = '',
                units: float = 1.0, cost_usd: float = None) -> float:
    """Registra uma operação de API e retorna o custo em US$."""
    if run_id is None:
        run_id = _env_run_id()
    if slug is None:
        slug = _env_slug()
    if cost_usd is None:
        price = PRICES.get(api)
        if price is None:
            print(f'[cost_tracker] aviso: api desconhecida {api!r}, custo = 0')
            cost_usd = 0.0
        else:
            cost_usd = price * units

    data = _load()

    # Entrada do run
    if run_id not in data['runs']:
        data['runs'][run_id] = {
            'slug': slug,
            'ts': datetime.now(timezone.utc).isoformat(),
            'items': [],
            'total_usd': 0.0,
        }
    run = data['runs'][run_id]
    run['items'].append({'api': api, 'units': units, 'cost_usd': cost_usd})
    run['total_usd'] = round(sum(i['cost_usd'] for i in run['items']), 4)

    # Índice por slug
    if slug not in data['by_slug']:
        data['by_slug'][slug] = {'total_usd': 0.0, 'runs': 0}
    # Recalcula do zero para evitar dupla-contagem em re-runs
    slug_runs = [r for r in data['runs'].values() if r.get('slug') == slug]
    data['by_slug'][slug] = {
        'total_usd': round(sum(r['total_usd'] for r in slug_runs), 4),
        'runs': len(slug_runs),
    }

    _save(data)
    return cost_usd


def get_run_cost(run_id: str) -> float:
    return _load()['runs'].get(run_id, {}).get('total_usd', 0.0)


def get_slug_total(slug: str) -> float:
    return _load()['by_slug'].get(slug, {}).get('total_usd', 0.0)


def weekly_cost() -> float:
    """Custo total dos runs da semana corrente (seg–dom UTC)."""
    from datetime import date, timedelta
    today = date.today()
    start = today - timedelta(days=today.weekday())  # segunda-feira
    start_iso = start.isoformat()
    data = _load()
    total = 0.0
    for run in data['runs'].values():
        ts = run.get('ts', '')
        if ts[:10] >= start_iso:
            total += run.get('total_usd', 0.0)
    return round(total, 4)


def print_costs() -> None:
    data = _load()
    if not data['runs']:
        print('[cost_tracker] Nenhum custo registrado ainda.')
        return

    print(f'\n{"SLUG":<28} {"RUNS":>5} {"TOTAL US$":>12}')
    print('-' * 50)
    for slug, info in sorted(data['by_slug'].items()):
        print(f'{slug:<28} {info["runs"]:>5} {info["total_usd"]:>11.4f}')

    grand = sum(r['total_usd'] for r in data['runs'].values())
    print('-' * 50)
    print(f'{"TOTAL":<28} {len(data["runs"]):>5} {grand:>11.4f}')
    print(f'\nSemana atual: US$ {weekly_cost():.4f}')


if __name__ == '__main__':
    print_costs()
