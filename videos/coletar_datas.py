# -*- coding: utf-8 -*-
"""Coleta as datas REAIS de cada peca direto das APIs (YouTube + Instagram)
e grava em ../datas_coletadas.json para a planilha de metadados consumir.

YouTube  -> videos.list(part=snippet,status): publishedAt (publicacao/upload),
            publishAt (agendamento atual, reflete remarcacoes), privacyStatus.
Instagram-> Graph API media node: timestamp (publicacao real) + permalink.

Uso:  python coletar_datas.py
"""

import sys, os, json
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

ROOT = Path(__file__).parent  # scripts + .secrets + upload_youtube/instagram_post
BASE = Path(
    os.environ.get('MR_BASE', ROOT.parent)
)  # dados + saidas (local: biblioteca/ ; VPS: MR_BASE)
META = BASE / 'metadados.json'
OUT = BASE / 'datas_coletadas.json'

meta = json.loads(META.read_text(encoding='utf-8'))

yt_ids, ig_ids = [], []
for livro in meta['livros']:
    for p in livro['pecas']:
        for pub in p['pubs']:
            pid = pub.get('id', '')
            if not pid:
                continue
            if pub['rede'] in ('YouTube', 'YouTube Shorts'):
                yt_ids.append(pid)
            elif pub['rede'] == 'Instagram':
                ig_ids.append(pid)

yt_ids = sorted(set(yt_ids))
ig_ids = sorted(set(ig_ids))
print(f'YouTube IDs: {len(yt_ids)} | Instagram IDs: {len(ig_ids)}')

resultado = {'youtube': {}, 'instagram': {}, 'erros': []}

# ---------------- YouTube ----------------
try:
    from upload_youtube import get_creds
    from googleapiclient.discovery import build

    yt = build('youtube', 'v3', credentials=get_creds())
    for i in range(0, len(yt_ids), 50):
        lote = yt_ids[i : i + 50]
        r = yt.videos().list(part='snippet,status,statistics', id=','.join(lote)).execute()
        achados = set()
        for it in r['items']:
            achados.add(it['id'])
            st = it.get('statistics', {})
            resultado['youtube'][it['id']] = {
                'publishedAt': it['snippet'].get('publishedAt'),
                'publishAt': it['status'].get('publishAt'),
                'privacyStatus': it['status'].get('privacyStatus'),
                'title': it['snippet'].get('title'),
                'viewCount': st.get('viewCount'),
                'likeCount': st.get('likeCount'),
                'commentCount': st.get('commentCount'),
            }
        for faltou in set(lote) - achados:
            resultado['youtube'][faltou] = {'erro': 'nao encontrado (apagado/sem acesso)'}
    print(
        f'  YouTube OK: {len([v for v in resultado["youtube"].values() if "erro" not in v])} videos'
    )
except Exception as e:
    msg = f'YouTube falhou: {str(e)[:200]}'
    print('  ' + msg)
    resultado['erros'].append(msg)

# ---------------- YouTube Analytics (retencao/CTR/inscritos) ----------------
# Usa um token SEPARADO (token_analytics.json, escopo yt-analytics.readonly) para
# NAO tocar no token de upload/producao. So roda se o token ja existir (consentido
# uma vez via:  python coletar_datas.py --auth-analytics). Headless-safe.
SEC = ROOT / '.secrets'
TOK_A = SEC / 'token_analytics.json'
SCOPES_A = [
    'https://www.googleapis.com/auth/yt-analytics.readonly',
    'https://www.googleapis.com/auth/youtube.readonly',
]


def creds_analytics(interactive=False):
    from google.oauth2.credentials import Credentials
    from google.auth.transport.requests import Request

    creds = Credentials.from_authorized_user_file(str(TOK_A), SCOPES_A) if TOK_A.exists() else None
    if creds and creds.valid:
        return creds
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
        TOK_A.write_text(creds.to_json(), encoding='utf-8')
        return creds
    if interactive:
        from google_auth_oauthlib.flow import InstalledAppFlow

        flow = InstalledAppFlow.from_client_secrets_file(str(SEC / 'client_secret.json'), SCOPES_A)
        print(">> Abrindo o navegador. ESCOLHA O CANAL 'Minuto Real' (NAO o pessoal).")
        creds = flow.run_local_server(port=0)
        TOK_A.write_text(creds.to_json(), encoding='utf-8')
        return creds
    return None


if '--auth-analytics' in sys.argv:
    creds_analytics(interactive=True)
    print('token_analytics.json salvo. Rode novamente sem a flag para coletar.')
    raise SystemExit(0)

if TOK_A.exists():
    try:
        from googleapiclient.discovery import build as _build

        ya = _build('youtubeAnalytics', 'v2', credentials=creds_analytics())
        pub_ids = [k for k, v in resultado['youtube'].items() if v.get('privacyStatus') == 'public']
        if pub_ids:
            import datetime as _dt

            filt = 'video==' + ','.join(pub_ids)
            base = dict(
                ids='channel==MINE',
                startDate='2026-01-01',
                endDate=_dt.date.today().isoformat(),
                dimensions='video',
                filters=filt,
            )
            r1 = (
                ya.reports()
                .query(
                    metrics='views,averageViewPercentage,averageViewDuration,subscribersGained',
                    **base,
                )
                .execute()
            )
            for row in r1.get('rows', []):
                vid = row[0]
                if vid in resultado['youtube']:
                    resultado['youtube'][vid]['retencao'] = round(row[2], 1)
                    resultado['youtube'][vid]['dur_media'] = int(row[3])
                    resultado['youtube'][vid]['subs'] = int(row[4])
            try:  # CTR/impressoes em consulta separada (grupo de metrica distinto)
                r2 = (
                    ya.reports()
                    .query(metrics='impressions,impressionsClickThroughRate', **base)
                    .execute()
                )
                for row in r2.get('rows', []):
                    vid = row[0]
                    if vid in resultado['youtube']:
                        resultado['youtube'][vid]['impressoes'] = int(row[1])
                        resultado['youtube'][vid]['ctr'] = round(row[2], 1)
            except Exception as e:
                resultado['erros'].append(f'YT Analytics CTR: {str(e)[:120]}')
        print(f'  YouTube Analytics OK: retencao/subs em {len(pub_ids)} videos publicos')
    except Exception as e:
        resultado['erros'].append(f'YT Analytics: {str(e)[:160]}')
else:
    print('  YouTube Analytics: pulado (sem token_analytics.json — rode --auth-analytics 1x)')

# ---------------- Instagram ----------------
try:
    import urllib.request, urllib.parse
    from instagram_post import _get, _token, _user_id, GRAPH

    tok, uid = _token(), _user_id()

    def _graph(path, fields=None, extra=None):
        p = {'access_token': tok}
        if fields:
            p['fields'] = fields
        if extra:
            p.update(extra)
        return json.load(
            urllib.request.urlopen(f'{GRAPH}{path}?{urllib.parse.urlencode(p)}', timeout=60)
        )

    # conta (andamento geral)
    try:
        resultado['instagram_account'] = _graph(
            f'/{uid}', 'id,username,media_count,followers_count'
        )
    except Exception as e:
        resultado['instagram_account'] = {'erro': str(e)[:160]}

    # lista REAL de midias publicadas (fonte de verdade do "no ar")
    media = []
    try:
        page = _graph(
            f'/{uid}/media',
            'id,caption,media_type,media_product_type,timestamp,permalink,like_count,comments_count',
            {'limit': '50'},
        )
        media = page.get('data', [])
    except Exception as e:
        resultado['erros'].append(f'IG media list: {str(e)[:160]}')
    resultado['instagram_media'] = media

    # insights por midia (alcance/salvamentos/compart.) — exige instagram_manage_insights.
    # No 1o erro de permissao (#10) desiste do resto (sem escopo). Headless-safe.
    ins_ok, ins_n = True, 0
    for m in media:
        if not ins_ok or not m.get('id'):
            continue
        mset = 'reach,saved,shares,total_interactions'
        try:
            d = _graph(f"/{m['id']}/insights", None, {'metric': mset})
            m['insights'] = {
                x['name']: (x.get('values') or [{}])[0].get('value') for x in d.get('data', [])
            }
            ins_n += 1
        except urllib.error.HTTPError as e:
            body = e.read().decode()
            if '"code":10' in body or '(#10)' in body:
                ins_ok = False
                resultado['erros'].append('IG insights: sem permissao (instagram_manage_insights)')
            else:
                try:  # fallback metrica minima
                    d = _graph(f"/{m['id']}/insights", None, {'metric': 'reach,saved'})
                    m['insights'] = {
                        x['name']: (x.get('values') or [{}])[0].get('value')
                        for x in d.get('data', [])
                    }
                    ins_n += 1
                except Exception:
                    pass
        except Exception:
            pass
    resultado['ig_insights_ok'] = ins_ok
    if ins_ok and ins_n:
        print(f'  Instagram insights OK: {ins_n} midias com alcance/salvamentos')

    # lookup por-id (compat com os state.json antigos)
    for mid in ig_ids:
        try:
            d = _get(f'/{mid}', tok, fields='timestamp,permalink,media_type,media_product_type')
            resultado['instagram'][mid] = (
                {'erro': d['error'].get('message', '')[:120]}
                if isinstance(d, dict) and 'error' in d
                else {
                    'timestamp': d.get('timestamp'),
                    'permalink': d.get('permalink'),
                    'media_type': d.get('media_type'),
                }
            )
        except Exception as e:
            resultado['instagram'][mid] = {'erro': str(e)[:160]}

    acc = resultado['instagram_account']
    print(
        f'  Instagram: @{acc.get("username")} | media_count={acc.get("media_count")} '
        f'| seguidores={acc.get("followers_count")} | media list={len(media)}'
    )
except Exception as e:
    msg = f'Instagram falhou: {str(e)[:200]}'
    print('  ' + msg)
    resultado['erros'].append(msg)

# ---------------- Site (visitas por pagina via logs do nginx) ----------------
import subprocess

try:
    agg = (
        r"zcat -f /var/log/nginx/access.log* 2>/dev/null | "
        r"grep -oE 'GET /biblioteca/[a-z0-9-]+\.html' | "
        r"sed 's#GET /biblioteca/##;s#\.html##' | sort | uniq -c"
    )
    cmd = (
        ['bash', '-lc', agg]
        if os.environ.get('MR_LOCAL_LOGS')
        else ['ssh', 'root@andregalgani.com.br', agg]
    )
    out = subprocess.run(cmd, capture_output=True, text=True, timeout=90)
    vis = {}
    for line in out.stdout.splitlines():
        line = line.strip()
        if not line:
            continue
        n, _, slug = line.partition(' ')
        try:
            vis[slug.strip()] = int(n)
        except ValueError:
            pass
    resultado['site_visitas'] = vis
    resultado['site_periodo'] = 'ultimos ~14 dias (retencao dos logs nginx)'
    print(f"  Site: {len(vis)} paginas com visita | total {sum(vis.values())} hits")
except Exception as e:
    resultado['erros'].append(f'Site visitas: {str(e)[:160]}')

# ---------------- Amazon (vendas — opcional, colado pelo usuario) ----------------
# Sem API: PA-API exige 3 vendas; relatorio so no painel Associados. Se existir
# ../amazon_vendas.json ({slug|asin: qtd}), e ingerido; senao fica vazio.
av = BASE / 'amazon_vendas.json'
resultado['amazon_vendas'] = json.loads(av.read_text(encoding='utf-8')) if av.exists() else {}

from datetime import datetime, timezone, timedelta

resultado['coletado_em'] = datetime.now(timezone.utc).isoformat()

# ---------------- Historico (serie temporal p/ tendencias) ----------------
# 1 snapshot por DIA (substitui o do mesmo dia); guarda 120 dias.
HIST = BASE / 'historico_metadados.json'
yt_pub = {k: v for k, v in resultado['youtube'].items() if v.get('privacyStatus') == 'public'}
hoje_brt = (datetime.now(timezone.utc) - timedelta(hours=3)).strftime('%Y-%m-%d')
snap = {
    'data': hoje_brt,
    'views_total': sum(int(v.get('viewCount') or 0) for v in yt_pub.values()),
    'likes_total': sum(int(v.get('likeCount') or 0) for v in yt_pub.values()),
    'yt_no_ar': len(yt_pub),
    'ig_no_ar': resultado.get('instagram_account', {}).get('media_count', 0) or 0,
    'ig_seguidores': resultado.get('instagram_account', {}).get('followers_count', 0) or 0,
    'visitas': sum(resultado.get('site_visitas', {}).values()),
    'por_video': {k: int(v.get('viewCount') or 0) for k, v in yt_pub.items()},
}
try:
    hist = json.loads(HIST.read_text(encoding='utf-8')) if HIST.exists() else []
except Exception:
    hist = []
hist = [h for h in hist if h.get('data') != hoje_brt]
hist.append(snap)
hist = sorted(hist, key=lambda h: h['data'])[-120:]
HIST.write_text(json.dumps(hist, ensure_ascii=False), encoding='utf-8')
resultado['historico'] = hist
print(
    f'  Historico: {len(hist)} snapshots (hoje: {snap["views_total"]} views, {snap["likes_total"]} likes)'
)

OUT.write_text(json.dumps(resultado, ensure_ascii=False, indent=1), encoding='utf-8')
print(f'-> {OUT}')
if resultado['erros']:
    print('ERROS:', resultado['erros'])
