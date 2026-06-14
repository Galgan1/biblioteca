# -*- coding: utf-8 -*-
"""Gera analytics/dashboard.html — painel consolidado do canal Minuto Real.

Fontes (todas opcionais — degrada graciosamente se faltarem):
  analytics/aprendizados.json   (relatorio_desempenho.py)
  analytics/custos.json         (cost_tracker.py)
  pipeline/events.jsonl         (pipeline_state.py)
  pipeline/state/*.json         (estado por slug)
  videos/canal-state.json       (estado das lanes)

Uso:
  python analytics/dashboard.py           # gera analytics/dashboard.html
  python analytics/dashboard.py --open    # gera e abre no navegador
"""
import json
import sys
from collections import defaultdict
from datetime import date, datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
ANALYTICS = ROOT / 'analytics'
PIPELINE  = ROOT / 'pipeline'
VIDEOS    = ROOT / 'videos'

OUT = ANALYTICS / 'dashboard.html'

STAGE_ICONS = {
    'done':    '✓',
    'blocked': '✗',
    'skipped': '–',
    'pending': '·',
}

STAGES = ['skill', 'biblioteca', 'video_built', 'uploaded',
          'shorts', 'scheduled', 'instagram', 'tiktok', 'facebook']


# ---------------------------------------------------------------------------
# Carregamento de dados
# ---------------------------------------------------------------------------

def _load_json(path: Path, default=None):
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except Exception:
        return default if default is not None else {}


def load_data() -> dict:
    d = {}

    # Aprendizados
    d['aprendizados'] = _load_json(ANALYTICS / 'aprendizados.json')

    # Custos
    d['custos'] = _load_json(ANALYTICS / 'custos.json', {'runs': {}, 'by_slug': {}})

    # Canal state
    d['canal'] = _load_json(VIDEOS / 'canal-state.json')

    # Pipeline states por slug
    states = {}
    state_dir = PIPELINE / 'state'
    if state_dir.exists():
        for f in state_dir.glob('*.json'):
            states[f.stem] = _load_json(f)
    d['states'] = states

    # Events (throughput)
    events = []
    events_file = PIPELINE / 'events.jsonl'
    if events_file.exists():
        for line in events_file.read_text(encoding='utf-8').splitlines():
            try:
                events.append(json.loads(line))
            except Exception:
                pass
    d['events'] = events

    return d


# ---------------------------------------------------------------------------
# Cálculos
# ---------------------------------------------------------------------------

def throughput_by_week(events: list) -> dict:
    """Conta eventos 'done' por semana (ISO week string)."""
    by_week = defaultdict(int)
    for ev in events:
        if ev.get('status') == 'done':
            ts = ev.get('ts', '')[:10]
            try:
                dt = date.fromisoformat(ts)
                week = dt.strftime('%Y-W%W')
                by_week[week] += 1
            except Exception:
                pass
    return dict(sorted(by_week.items()))


def canal_metrics(aprendizados: dict) -> dict:
    return aprendizados.get('canal', {})


# ---------------------------------------------------------------------------
# Renderização HTML
# ---------------------------------------------------------------------------

CSS = """
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  background: #111; color: #d4d4d4;
  font-family: 'Consolas', 'Courier New', monospace;
  font-size: 13px; line-height: 1.6;
  padding: 24px 32px;
}
h1 { color: oklch(75% 0.17 152); font-size: 18px; margin-bottom: 4px; }
.subtitle { color: #666; margin-bottom: 28px; }
h2 { color: oklch(70% 0.14 152); font-size: 13px; text-transform: uppercase;
     letter-spacing: 1px; margin: 28px 0 10px; border-bottom: 1px solid #222;
     padding-bottom: 4px; }
.cards { display: flex; gap: 16px; flex-wrap: wrap; margin-bottom: 8px; }
.card {
  background: #1a1a1a; border: 1px solid #2a2a2a;
  border-radius: 6px; padding: 12px 18px; min-width: 140px;
}
.card .label { color: #666; font-size: 11px; text-transform: uppercase; }
.card .value { color: oklch(78% 0.18 152); font-size: 22px; font-weight: bold; }
.card .sub   { color: #555; font-size: 11px; }
table { width: 100%; border-collapse: collapse; margin-bottom: 8px; }
th { color: #555; font-size: 11px; text-transform: uppercase; text-align: left;
     padding: 4px 8px; border-bottom: 1px solid #222; }
td { padding: 4px 8px; border-bottom: 1px solid #1c1c1c; }
tr:hover td { background: #161616; }
.done    { color: oklch(72% 0.18 152); }
.blocked { color: #e05; }
.skipped { color: #555; }
.pending { color: #444; }
.ok      { color: oklch(72% 0.18 152); }
.warn    { color: #fa0; }
.error   { color: #e05; }
.bar-wrap { background: #1a1a1a; border-radius: 3px; height: 8px; width: 120px; }
.bar      { background: oklch(62% 0.18 152); height: 8px; border-radius: 3px; }
"""


def card(label: str, value, sub: str = '') -> str:
    return (f'<div class="card"><div class="label">{label}</div>'
            f'<div class="value">{value}</div>'
            f'{"<div class=sub>" + sub + "</div>" if sub else ""}</div>')


def status_cell(status: str) -> str:
    icon = STAGE_ICONS.get(status, '?')
    return f'<td class="{status}">{icon}</td>'


def render(data: dict) -> str:
    aprendizados = data['aprendizados']
    custos       = data['custos']
    canal_state  = data['canal']
    states       = data['states']
    events       = data['events']

    now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
    canal_name = canal_state.get('channel_name', 'Minuto Real')

    # --- Métricas do canal ---
    metrics = canal_metrics(aprendizados)
    total_views = metrics.get('total_views', '—')
    n_videos    = metrics.get('total_videos', len(states))
    ctr_med     = metrics.get('ctr_medio', None)
    ret_med     = metrics.get('retencao_media', None)
    grand_cost  = sum(r.get('total_usd', 0) for r in custos.get('runs', {}).values())

    ctr_txt = f'{ctr_med:.1f}%' if ctr_med else '—'
    ret_txt = f'{ret_med:.1f}%' if ret_med else '—'

    cards_html = (
        card('Total Views', total_views) +
        card('Vídeos', n_videos) +
        card('CTR médio', ctr_txt) +
        card('Retenção', ret_txt) +
        card('Custo acum.', f'US$ {grand_cost:.2f}')
    )

    # --- Lanes ---
    lanes = canal_state.get('lanes', {})
    lane_rows = ''
    for lane, info in lanes.items():
        status = info.get('status', '?')
        reason = info.get('reason', '')
        cls = 'ok' if status == 'active' else ('warn' if status == 'blocked' else 'error')
        lane_rows += (f'<tr><td>{lane}</td>'
                      f'<td class="{cls}">{status}</td>'
                      f'<td style="color:#555;font-size:11px">{reason}</td></tr>')

    # --- Pipeline por slug ---
    slug_rows = ''
    for slug in sorted(states):
        state = states[slug]
        cells = ''.join(
            status_cell(state.get(s, {}).get('status', 'pending'))
            for s in STAGES
        )
        slug_rows += f'<tr><td>{slug}</td>{cells}</tr>'

    stage_headers = ''.join(f'<th>{s[:6]}</th>' for s in STAGES)

    # --- Custos por slug ---
    cost_rows = ''
    for slug, info in sorted(custos.get('by_slug', {}).items()):
        cost_rows += (f'<tr><td>{slug}</td>'
                      f'<td>{info.get("runs", 0)}</td>'
                      f'<td>US$ {info.get("total_usd", 0):.4f}</td>'
                      f'<td>US$ {info.get("total_usd",0)/max(info.get("runs",1),1):.4f}</td></tr>')

    # --- Desempenho por vídeo ---
    perf_rows = ''
    for vid in aprendizados.get('por_video', []):
        slug  = vid.get('slug', '?')
        views = vid.get('views', '—')
        ctr   = vid.get('ctr', None)
        ret   = vid.get('retencao', None)
        alerts = ', '.join(vid.get('alertas', []))
        cls   = 'warn' if alerts else 'done'
        ctr_s = f'{ctr:.1f}%' if ctr else '—'
        ret_s = f'{ret:.1f}%' if ret else '—'
        perf_rows += (f'<tr><td>{slug}</td><td>{views}</td>'
                      f'<td>{ctr_s}</td><td>{ret_s}</td>'
                      f'<td class="{cls}" style="font-size:11px">{alerts or "ok"}</td></tr>')

    # --- Throughput ---
    tp = throughput_by_week(events)
    tp_rows = ''
    for week, count in list(tp.items())[-8:]:  # últimas 8 semanas
        pct = min(count * 8, 100)
        tp_rows += (f'<tr><td>{week}</td><td>{count} eventos done</td>'
                    f'<td><div class="bar-wrap"><div class="bar" style="width:{pct}%"></div></div></td></tr>')

    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{canal_name} — Dashboard</title>
<style>{CSS}</style>
</head>
<body>
<h1>{canal_name} · Dashboard</h1>
<div class="subtitle">Gerado em {now}</div>

<h2>Canal</h2>
<div class="cards">{cards_html}</div>

<h2>Lanes</h2>
<table>
<tr><th>Lane</th><th>Status</th><th>Nota</th></tr>
{lane_rows}
</table>

<h2>Pipeline por Slug</h2>
<table>
<tr><th>Slug</th>{stage_headers}</tr>
{slug_rows if slug_rows else '<tr><td colspan="10" style="color:#444">Nenhum slug rastreado ainda.</td></tr>'}
</table>

<h2>Custo por Slug</h2>
<table>
<tr><th>Slug</th><th>Runs</th><th>Total</th><th>Média/Run</th></tr>
{cost_rows if cost_rows else '<tr><td colspan="4" style="color:#444">Nenhum custo registrado.</td></tr>'}
</table>

<h2>Desempenho por Vídeo</h2>
<table>
<tr><th>Slug</th><th>Views</th><th>CTR</th><th>Retenção</th><th>Alertas</th></tr>
{perf_rows if perf_rows else '<tr><td colspan="5" style="color:#444">Sem dados de desempenho (rode relatorio_desempenho.py).</td></tr>'}
</table>

<h2>Throughput (eventos done / semana)</h2>
<table>
<tr><th>Semana</th><th>Eventos</th><th>Volume</th></tr>
{tp_rows if tp_rows else '<tr><td colspan="3" style="color:#444">Sem eventos registrados ainda.</td></tr>'}
</table>

</body>
</html>"""
    return html


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    data = load_data()
    html = render(data)
    ANALYTICS.mkdir(parents=True, exist_ok=True)
    OUT.write_text(html, encoding='utf-8')
    print(f'Dashboard gerado: {OUT}')

    if '--open' in sys.argv:
        import webbrowser
        webbrowser.open(OUT.as_uri())


if __name__ == '__main__':
    main()
