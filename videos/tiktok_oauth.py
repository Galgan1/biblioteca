# -*- coding: utf-8 -*-
"""Troca o authorization_code do TikTok por um access_token e salva no mesmo formato
que o tiktok_post.py espera (.secrets/tiktok_token.json + .txt).

Uso (na conta do canal, depois de autorizar e cair no callback):
  python tiktok_oauth.py              # lê o code do clipboard (botão "Copiar tudo" do callback)
  python tiktok_oauth.py <code>       # ou passe o code direto

O code é de uso único e expira em poucos minutos — rode logo após autorizar.
Stdlib only (urllib) + PowerShell Get-Clipboard como fallback.
"""

import sys, re, json, time, subprocess, urllib.parse, urllib.request, urllib.error
from pathlib import Path

ROOT = Path(__file__).parent
SEC = ROOT / '.secrets'
TOKEN_JSON = SEC / 'tiktok_token.json'
TOKEN_TXT = SEC / 'tiktok_token.txt'
OAUTH_TOKEN_URL = 'https://open.tiktokapis.com/v2/oauth/token/'
REDIRECT_URI = 'https://www.andregalgani.com.br/tiktok-callback.html'


def _code_from_clipboard():
    """Lê o clipboard (formato 'code=...\\nstate=...' que o callback copia) e extrai o code."""
    try:
        out = subprocess.run(
            ['powershell', '-NoProfile', '-Command', 'Get-Clipboard'],
            capture_output=True,
            text=True,
            timeout=15,
        ).stdout
    except Exception as e:
        sys.exit(f'[!] não consegui ler o clipboard: {e}. Passe o code como argumento.')
    m = re.search(r'code=([^\s&]+)', out) or re.search(r'(\S{40,})', out)
    if not m:
        sys.exit(
            '[!] nenhum code no clipboard. Clique "Copiar tudo" no callback, ou passe o code como argumento.'
        )
    return m.group(1).strip()


def exchange(code):
    data = urllib.parse.urlencode(
        {
            'client_key': (SEC / 'tiktok_client_key.txt').read_text(encoding='utf-8').strip(),
            'client_secret': (SEC / 'tiktok_client_secret.txt').read_text(encoding='utf-8').strip(),
            'code': code,
            'grant_type': 'authorization_code',
            'redirect_uri': REDIRECT_URI,
        }
    ).encode()
    req = urllib.request.Request(
        OAUTH_TOKEN_URL, data=data, headers={'Content-Type': 'application/x-www-form-urlencoded'}
    )
    try:
        r = json.load(urllib.request.urlopen(req, timeout=60))
    except urllib.error.HTTPError as e:
        sys.exit(
            f'[!] troca falhou: {e.code} {e.read().decode()[:300]} '
            '(code expira em minutos — re-autorize e rode de novo).'
        )
    if 'access_token' not in r:
        sys.exit(f'[!] resposta sem access_token: {r}')
    r['_obtained_at'] = int(time.time())
    TOKEN_JSON.write_text(json.dumps(r, ensure_ascii=False, indent=2), encoding='utf-8')
    TOKEN_TXT.write_text(r['access_token'], encoding='utf-8')
    return r['access_token']


def _whoami(token):
    req = urllib.request.Request(
        'https://open.tiktokapis.com/v2/user/info/?fields=display_name',
        headers={'Authorization': f'Bearer {token}'},
    )
    try:
        r = json.load(urllib.request.urlopen(req, timeout=30))
        return r.get('data', {}).get('user', {}).get('display_name', '?')
    except Exception:
        return '?'


if __name__ == '__main__':
    code = sys.argv[1] if len(sys.argv) > 1 else _code_from_clipboard()
    tok = exchange(code)
    print(f'  Token salvo OK -> conta @{_whoami(tok)}  (tiktok_token.json + .txt atualizados)')
