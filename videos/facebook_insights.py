# -*- coding: utf-8 -*-
"""Metricas READ-ONLY da Pagina do Facebook "Minuto Real" via Graph API.

Irmao de leitura do facebook_post.py (que escreve): aqui SO se faz GET. Serve para
o coletor de metadados (coletar_datas.py) passar a enxergar o Facebook, do mesmo
jeito que ja enxerga YouTube e Instagram.

Mesma fiacao de segredos do facebook_post.py:
  - Page access token -> .secrets/facebook_page_token.txt
  - id numerico da Pagina -> .secrets/facebook_page_id.txt
NUNCA imprimir/logar/versionar o token nem o conteudo de .secrets — so os numeros.

Devolve um formato compativel com a secao do Instagram do coletor
(resultado['instagram_account'] / resultado['instagram_media']):
  coletar() -> {
    'facebook_account': {name, fan_count, followers_count},
    'facebook_posts':   [ {id, message, created_time, permalink,
                           impressions, reach, engaged, shares}, ... ],
    'erros':            [ ... ]
  }
coletar() NUNCA lanca: captura tudo e acumula em 'erros'.

Uso:  python facebook_insights.py     # imprime resumo legivel (read-only)
"""
import sys, urllib.parse
from pathlib import Path

import net  # camada HTTP isolada — circuit_breaker aplicado (Akita, isolamento)

try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

ROOT = Path(__file__).parent
SEC = ROOT / '.secrets'
GRAPH = 'https://graph.facebook.com/v21.0'
PAGE_TOKEN_FILE = SEC / 'facebook_page_token.txt'
PAGE_ID_FILE = SEC / 'facebook_page_id.txt'


def _token():
    """Page access token, ou None se ausente (coletar() trata sem quebrar)."""
    if not PAGE_TOKEN_FILE.exists():
        return None
    return PAGE_TOKEN_FILE.read_text(encoding='utf-8').strip()


def _page_id():
    """Id numerico da Pagina, ou None se ausente."""
    if not PAGE_ID_FILE.exists():
        return None
    return PAGE_ID_FILE.read_text(encoding='utf-8').strip()


def _get(path, token, fields=None, extra=None):
    """GET na Graph API via camada isolada `net` (circuit_breaker aplicado).
    Mantem o contrato: devolve o JSON, ou {'error': {...}} — NUNCA lanca."""
    q = {'access_token': token}
    if fields:
        q['fields'] = fields
    if extra:
        q.update(extra)
    url = f'{GRAPH}{path}?{urllib.parse.urlencode(q)}'
    try:
        r = net.request_json(url, method='GET', api='facebook_graph', timeout=60)
    except net.CircuitOpenError:
        return {'error': {'code': 'circuit_open', 'message': 'circuit OPEN (facebook_graph)'}}
    except net.TransientError as e:
        return {'error': {'code': 'transient', 'message': str(e)[:300]}}
    if r.get('ok'):
        return r['data']
    return {'error': {'code': r.get('status'), 'message': (r.get('erro') or '')[:300]}}


def coletar():
    """Coleta read-only da Pagina do Facebook. NUNCA lanca."""
    resultado = {'facebook_account': {}, 'facebook_posts': [], 'erros': []}

    token, pid = _token(), _page_id()
    if not token:
        resultado['erros'].append(
            'Facebook: token ausente (.secrets/facebook_page_token.txt)')
    if not pid:
        resultado['erros'].append(
            'Facebook: page id ausente (.secrets/facebook_page_id.txt)')
    if not token or not pid:
        return resultado

    # ---------------- Conta (andamento geral da Pagina) ----------------
    try:
        acc = _get(f'/{pid}', token, fields='name,fan_count,followers_count')
        if isinstance(acc, dict) and 'error' in acc:
            resultado['facebook_account'] = {'erro': acc['error'].get('message', '')[:160]}
            resultado['erros'].append('FB conta: ' + acc['error'].get('message', '')[:160])
        else:
            resultado['facebook_account'] = {
                'name': acc.get('name'),
                'fan_count': acc.get('fan_count'),
                'followers_count': acc.get('followers_count'),
            }
    except Exception as e:
        resultado['facebook_account'] = {'erro': str(e)[:160]}
        resultado['erros'].append(f'FB conta: {str(e)[:160]}')

    # ---------------- Posts recentes (fonte de verdade do "no ar") ----------------
    posts = []
    try:
        page = _get(f'/{pid}/posts', token,
                    fields='id,message,created_time,permalink_url,shares',
                    extra={'limit': '25'})
        if isinstance(page, dict) and 'error' in page:
            resultado['erros'].append('FB posts: ' + page['error'].get('message', '')[:160])
        else:
            posts = page.get('data', [])
    except Exception as e:
        resultado['erros'].append(f'FB posts: {str(e)[:160]}')

    # ---------------- Insights por post (pode falhar por permissao) ----------------
    # post_impressions / _unique / post_engaged_users exigem read_insights.
    # No 1o erro de permissao desiste do resto (sem escopo), como o coletor faz no IG.
    ins_ok = True
    for p in posts:
        post = {
            'id': p.get('id'),
            'message': (p.get('message') or '')[:200],
            'created_time': p.get('created_time'),
            'permalink': p.get('permalink_url'),
            'shares': (p.get('shares') or {}).get('count'),
            'impressions': None,
            'reach': None,
            'engaged': None,
        }
        if ins_ok and post['id']:
            d = _get(f"/{post['id']}/insights", token, extra={
                'metric': 'post_impressions,post_impressions_unique,post_engaged_users'})
            if isinstance(d, dict) and 'error' in d:
                msg = d['error'].get('message', '')
                if d['error'].get('code') == 10 or '#10' in msg or 'permission' in msg.lower():
                    ins_ok = False
                    resultado['erros'].append('FB insights: sem permissao (read_insights)')
                else:
                    resultado['erros'].append(f'FB insights {post["id"]}: {msg[:120]}')
            else:
                vals = {x.get('name'): (x.get('values') or [{}])[0].get('value')
                        for x in d.get('data', [])}
                post['impressions'] = vals.get('post_impressions')
                post['reach'] = vals.get('post_impressions_unique')
                post['engaged'] = vals.get('post_engaged_users')
        resultado['facebook_posts'].append(post)

    return resultado


def _resumo(resultado):
    """Imprime um resumo legivel (conta + nº de posts + reach por post). So numeros/titulos."""
    acc = resultado['facebook_account']
    if acc.get('erro'):
        print(f"Facebook conta: ERRO ({acc['erro']})")
    else:
        print(f"Facebook: {acc.get('name')} | curtidas={acc.get('fan_count')} "
              f"| seguidores={acc.get('followers_count')}")

    posts = resultado['facebook_posts']
    print(f"Posts recentes: {len(posts)}")
    for p in posts:
        titulo = (p.get('message') or '').replace('\n', ' ').strip()[:48] or '(sem texto)'
        reach = p.get('reach')
        reach_s = reach if reach is not None else '-'
        impr = p.get('impressions')
        impr_s = impr if impr is not None else '-'
        print(f"  {p.get('created_time', '?')[:10]} | reach={reach_s} | impr={impr_s} | {titulo}")

    if resultado['erros']:
        print('ERROS:', resultado['erros'])


if __name__ == '__main__':
    _resumo(coletar())
