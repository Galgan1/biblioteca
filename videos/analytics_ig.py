# -*- coding: utf-8 -*-
"""Analytics de performance do Instagram @minutoreal1701.

Puxa /media/insights para os últimos 50 posts e calcula save_rate, share_rate e
reach_rate. Salva JSON + CSV em videos/_analytics/ e imprime relatório no terminal.

Uso:
  python analytics_ig.py           # últimos 50 posts
  python analytics_ig.py --limit N # últimos N posts (máx 100)
  python analytics_ig.py --csv     # só o CSV, sem relatório
"""
import sys, json, csv, time, urllib.request, urllib.parse, urllib.error
from pathlib import Path
from datetime import datetime, timezone
from ig_base import refresh_token as _ig_refresh, read_token as _ig_read_token, read_user_id as _ig_read_user_id

ROOT = Path(__file__).parent
SEC = ROOT / '.secrets'
TOKEN_FILE = SEC / 'instagram_token.txt'
TOKEN_JSON = SEC / 'instagram_token.json'
USER_ID_FILE = SEC / 'instagram_user_id.txt'
APP_ID_FILE = SEC / 'instagram_app_id.txt'
APP_SECRET_FILE = SEC / 'instagram_app_secret.txt'
GRAPH = 'https://graph.facebook.com/v21.0'
OUT_DIR = ROOT / '_analytics'

# ---------------------------------------------------------------------------
# Auth — delegado para ig_base (DRY: pilar 4 Akita)
# Wrappers locais passam os caminhos deste módulo; ig_base não lê globals.
# ---------------------------------------------------------------------------

def _refresh(tj):
    return _ig_refresh(tj, APP_ID_FILE, APP_SECRET_FILE, TOKEN_JSON, TOKEN_FILE)


def _token():
    return _ig_read_token(TOKEN_FILE, TOKEN_JSON, APP_ID_FILE, APP_SECRET_FILE,
                          permission='instagram_basic')


def _user_id():
    return _ig_read_user_id(USER_ID_FILE)


def _get(path, token, params=None):
    """GET {GRAPH}{path} com access_token + params extras. Retorna dict JSON."""
    q = urllib.parse.urlencode({'access_token': token, **(params or {})})
    try:
        return json.load(urllib.request.urlopen(f'{GRAPH}{path}?{q}', timeout=60))
    except urllib.error.HTTPError as e:
        return {'error': {'code': e.code, 'message': e.read().decode()[:300]}}

# ---------------------------------------------------------------------------
# Coleta de dados
# ---------------------------------------------------------------------------

def _fetch_media(token, uid, limit):
    """Retorna lista de posts recentes (id, timestamp, media_type, permalink, caption)."""
    r = _get(f'/{uid}/media', token, {
        'fields': 'id,timestamp,media_type,permalink,caption',
        'limit': str(min(limit, 100)),
    })
    if 'error' in r:
        sys.exit(f'[!] erro ao buscar /media: {r["error"]}')
    return r.get('data', [])


def _fetch_insights(token, media_id):
    """Busca reach, saved, shares, video_views, total_interactions via /insights.
    Retorna dict métrica->valor. Campos indisponíveis ficam como None."""
    metrics = 'reach,saved,shares,video_views,total_interactions'
    r = _get(f'/{media_id}/insights', token, {'metric': metrics, 'period': 'lifetime'})
    if 'error' in r:
        # Post com < 24h ou sem permissão de insights pode retornar erro
        return {}
    result = {}
    for item in r.get('data', []):
        result[item['name']] = item.get('values', [{}])[0].get('value')
    return result


def _fetch_followers(token, uid):
    """Retorna contagem de seguidores ou None."""
    r = _get(f'/{uid}', token, {'fields': 'followers_count'})
    if 'error' in r:
        return None
    return r.get('followers_count')


def _slug_from_caption(caption):
    """Tenta extrair o slug de um livro da legenda. O slug aparece no nome do arquivo
    de short (ex: habitos-atomicos_01.mp4) ou na legenda como parte de uma frase.
    Estratégia simples: pega a primeira palavra-chave em kebab-case com 2+ hífens."""
    import re
    if not caption:
        return None
    # Procura por padrão slug kebab-case (2+ segmentos)
    m = re.search(r'\b([a-z][a-z0-9]+-[a-z][a-z0-9]+(?:-[a-z][a-z0-9]+)*)\b', caption)
    return m.group(1) if m else None

# ---------------------------------------------------------------------------
# Cálculo de métricas derivadas
# ---------------------------------------------------------------------------

def _rates(ins, followers):
    reach = ins.get('reach') or 0
    saved = ins.get('saved') or 0
    shares = ins.get('shares') or 0
    views = ins.get('video_views')
    interactions = ins.get('total_interactions')

    save_rate = saved / reach if reach > 0 else None
    share_rate = shares / reach if reach > 0 else None
    reach_rate = reach / followers if (followers and followers > 0) else None
    views_rate = (views / reach) if (views is not None and reach > 0) else None

    return {
        'reach': reach if reach > 0 else ins.get('reach'),
        'saved': saved if saved > 0 else ins.get('saved'),
        'shares': shares if shares > 0 else ins.get('shares'),
        'video_views': views,
        'total_interactions': interactions,
        'save_rate': save_rate,
        'share_rate': share_rate,
        'reach_rate': reach_rate,
        'views_rate': views_rate,
    }

# ---------------------------------------------------------------------------
# Relatório no terminal
# ---------------------------------------------------------------------------

def _pct(v):
    return f'{v*100:.1f}%' if v is not None else 'n/d'


def _report(posts, followers):
    today = datetime.now(tz=timezone.utc).strftime('%Y-%m-%d')
    n = len(posts)
    if followers:
        print(f'Seguidores: {followers:,}  |  Posts analisados: {n}  |  Data: {today}\n')
    else:
        print(f'Seguidores: n/d  |  Posts analisados: {n}  |  Data: {today}\n')

    def _label(p):
        slug = p.get('slug') or ''
        ts = p.get('timestamp', '')[:10]
        name = slug or p.get('permalink', '').rstrip('/').split('/')[-1]
        return name, ts

    def _top5(key):
        ranked = sorted(
            [p for p in posts if p.get(key) is not None],
            key=lambda p: p[key],
            reverse=True
        )[:5]
        other_key = 'share_rate' if key == 'save_rate' else 'save_rate'
        print(f'TOP 5 por {key}:')
        for i, p in enumerate(ranked, 1):
            name, ts = _label(p)
            other = p.get(other_key)
            reach = p.get('reach')
            print(f'  {i}. {name:<30} {key}={_pct(p[key])}  {other_key}={_pct(other)}'
                  f'  reach={reach if reach is not None else "n/d"}  ({ts})')
        if not ranked:
            print('  (sem dados suficientes)')
        print()

    print(f'\n=== Instagram Analytics — @minutoreal1701 ===')
    _top5('save_rate')
    _top5('share_rate')

    # Médias gerais (apenas posts com dados)
    def _avg(key):
        vals = [p[key] for p in posts if p.get(key) is not None]
        return sum(vals) / len(vals) if vals else None

    print('MÉDIAS GERAIS:')
    print(f'  save_rate médio:  {_pct(_avg("save_rate"))}')
    print(f'  share_rate médio: {_pct(_avg("share_rate"))}')
    print(f'  reach_rate médio: {_pct(_avg("reach_rate"))}')

    by_type = {}
    for p in posts:
        t = p.get('media_type', 'UNKNOWN')
        by_type[t] = by_type.get(t, 0) + 1
    type_parts = '  |  '.join(f'{t}: {c} posts' for t, c in sorted(by_type.items()))
    print(f'  {type_parts}')
    print()

# ---------------------------------------------------------------------------
# Persistência: JSON e CSV
# ---------------------------------------------------------------------------

def _save_json(posts, out_dir):
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / 'ig_insights.json'
    path.write_text(json.dumps(posts, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'  JSON salvo: {path}')


def _save_csv(posts, out_dir):
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / 'ig_insights.csv'
    cols = ['id', 'media_type', 'timestamp', 'permalink',
            'reach', 'saved', 'shares', 'video_views',
            'save_rate', 'share_rate', 'reach_rate', 'total_interactions']
    with open(path, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction='ignore')
        w.writeheader()
        for p in posts:
            w.writerow({k: p.get(k) for k in cols})
    print(f'  CSV salvo: {path}')

# ---------------------------------------------------------------------------
# Entrada principal
# ---------------------------------------------------------------------------

def run(limit=50, csv_only=False):
    token = _token()
    uid = _user_id()

    print(f'Coletando os últimos {limit} posts...')
    media_list = _fetch_media(token, uid, limit)
    if not media_list:
        print('[!] Nenhum post encontrado. Verifique token e permissões (instagram_basic).')
        return

    followers = _fetch_followers(token, uid)

    posts = []
    for i, m in enumerate(media_list, 1):
        mid = m['id']
        print(f'  [{i}/{len(media_list)}] {mid}  {m.get("media_type","?")}  {m.get("timestamp","")[:10]}')
        ins = _fetch_insights(token, mid)
        rates = _rates(ins, followers)
        slug = _slug_from_caption(m.get('caption', ''))
        post = {
            'id': mid,
            'slug': slug,
            'media_type': m.get('media_type'),
            'permalink': m.get('permalink'),
            'timestamp': m.get('timestamp'),
            **rates,
        }
        posts.append(post)

    _save_json(posts, OUT_DIR)
    _save_csv(posts, OUT_DIR)

    if not csv_only:
        _report(posts, followers)


if __name__ == '__main__':
    args = sys.argv[1:]
    limit = 50
    csv_only = False

    if '--csv' in args:
        csv_only = True
        args = [a for a in args if a != '--csv']

    if '--limit' in args:
        idx = args.index('--limit')
        if idx + 1 < len(args):
            try:
                limit = int(args[idx + 1])
            except ValueError:
                sys.exit('[!] --limit requer um número inteiro (ex: --limit 20)')
        else:
            sys.exit('[!] --limit requer um valor (ex: --limit 20)')

    run(limit=limit, csv_only=csv_only)
