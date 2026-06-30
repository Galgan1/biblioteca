# -*- coding: utf-8 -*-
"""Pré-flight de PUBLICAÇÃO: o token de YT/IG/FB está vivo? (chamada de status grátis).
O doutor previne — antes de tentar postar 25+ peças no canal real. NÃO publica nada."""
import json
import sys
import urllib.request
import urllib.error
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding='utf-8')
    except Exception:
        pass

SEC = Path(__file__).parent / '.secrets'
GRAPH = 'https://graph.facebook.com/v21.0'


def _get(url):
    try:
        return json.load(urllib.request.urlopen(url, timeout=30)), None
    except urllib.error.HTTPError as e:
        return None, f'HTTP {e.code}: {e.read().decode()[:140]}'
    except Exception as e:
        return None, f'{type(e).__name__}: {str(e)[:80]}'


def _read(name):
    f = SEC / name
    return f.read_text(encoding='utf-8').strip() if f.exists() else None


def ig():
    tok = None
    tj = SEC / 'instagram_token.json'
    if tj.exists():
        tok = json.loads(tj.read_text(encoding='utf-8')).get('access_token')
    tok = tok or _read('instagram_token.txt')
    uid = _read('instagram_user_id.txt')
    if not tok or not uid:
        return ('Instagram', '⚠', 'token/user_id ausente')
    d, err = _get(f'{GRAPH}/{uid}?fields=username&access_token={tok}')
    return ('Instagram', '❌', err) if err else ('Instagram', '✅', f"@{d.get('username')}")


def fb():
    tok = _read('facebook_page_token.txt')
    pid = _read('facebook_page_id.txt')
    if not tok or not pid:
        return ('Facebook', '⚠', 'token/page_id ausente')
    d, err = _get(f'{GRAPH}/{pid}?fields=name&access_token={tok}')
    return ('Facebook', '❌', err) if err else ('Facebook', '✅', d.get('name'))


def yt():
    try:
        import canal_guard
        canal_guard.get_youtube()                 # já chama assert_canal (Minuto Real)
        return ('YouTube', '✅', 'Minuto Real (canal verificado)')
    except Exception as e:
        return ('YouTube', '❌', f'{type(e).__name__}: {str(e)[:110]}')


print('\n=== Pré-flight de PUBLICAÇÃO — Minuto Real ===')
falhas = []
for fn in (yt, ig, fb):
    n, st, det = fn()
    print(f'  {n:<12} {st}  {det}')
    if st == '❌':
        falhas.append(n)
print(f"\n  bloqueadas: {falhas or 'nenhuma'}")
sys.exit(1 if falhas else 0)
