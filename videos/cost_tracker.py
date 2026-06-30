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
import functools
import json
import os
import sys
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


# ---------------------------------------------------------------------------
# Teto de gasto (catraca ANTES da chamada paga) — Akita pilar 8
# ---------------------------------------------------------------------------
# Pior nº1 da auditoria A6: weekly_cost() não tinha consumidor; record_cost só
# contava DEPOIS do gasto. Aqui a catraca: nenhuma chamada paga dispara se a semana
# já estourou o teto. Default-on no pipeline via WEEKLY_BUDGET_USD (gerar_video.main e
# publicar_tudo o definem); ausente = inativo (preserva comportamento atual e a rota
# soberana grátis).

DEFAULT_WEEKLY_BUDGET_USD = 20.0   # teto que o pipeline (gerar_video.main + publicar_tudo) liga por default


class BudgetExceeded(RuntimeError):
    """Teto semanal de gasto de API atingido — chamada paga abortada (não é falha de API)."""


def _budget_limit() -> float:
    """Teto ativo em US$. 0 = catraca desligada (env ausente, ou 0/negativo explícito)."""
    raw = os.environ.get('WEEKLY_BUDGET_USD', '').strip()
    if not raw:
        return 0.0   # não configurado → inativo (não inventa teto sem o caller pedir)
    try:
        return max(0.0, float(raw))
    except ValueError:
        # Akita pilar 7: env inválido não pode sumir calado. Avisa e mantém a catraca
        # no default (um typo não deve DESLIGAR a guarda — fail-safe p/ o lado seguro).
        print(f'[cost_tracker] WEEKLY_BUDGET_USD inválido ({raw!r}) — '
              f'usando default US$ {DEFAULT_WEEKLY_BUDGET_USD:.2f}', file=sys.stderr)
        return DEFAULT_WEEKLY_BUDGET_USD


def check_budget(api: str = '') -> None:
    """Aborta com BudgetExceeded se o gasto da semana já atingiu o teto. No-op se inativo."""
    limit = _budget_limit()
    if limit <= 0:
        return
    gasto = weekly_cost()
    if gasto >= limit:
        raise BudgetExceeded(
            f'teto semanal de gasto atingido: US$ {gasto:.4f} >= US$ {limit:.2f} '
            f'(WEEKLY_BUDGET_USD); chamada paga {api!r} abortada. Aumente o teto ou '
            f'rode o pipeline soberano (provider="base", R$0).')


def budget_guard(api: str = ''):
    """Decorator de catraca de orçamento. APLICAR COMO O MAIS EXTERNO (fora de
    @retry/@circuit_breaker): um abort por teto não é falha de API — não pode tripar
    o breaker (apagaria last_error) nem ser re-tentado pelo @retry."""
    def deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            check_budget(api)
            return func(*args, **kwargs)
        return wrapper
    return deco


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
