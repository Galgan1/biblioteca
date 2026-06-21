# -*- coding: utf-8 -*-
"""Helpers compartilhados de autenticação Instagram Graph API.

Extraído de instagram_post.py + analytics_ig.py (DRY — pilar 4 Akita) porque
_refresh e _user_id eram cópias byte-a-byte; _token divergia só na mensagem de
permissão, resolvido com o parâmetro `permission`.

As funções recebem os objetos Path como parâmetros em vez de ler módulo-global
para que os testes (mock.patch.object) continuem a fazer patch nos módulos
consumidores sem precisar alterar ig_base.
"""
import sys
import json
import time
import urllib.request
import urllib.parse
import urllib.error
from pathlib import Path

GRAPH = 'https://graph.facebook.com/v21.0'


def refresh_token(
    tj: dict,
    app_id_file: Path,
    app_secret_file: Path,
    token_json_file: Path,
    token_file: Path,
) -> str:
    """Troca o token de 60 dias por outro de 60 dias (fb_exchange_token). Best-effort:
    só roda se houver app_id + app_secret em .secrets. Atualiza os dois arquivos.

    Parâmetros recebidos por injeção para que os chamadores possam ter caminhos
    distintos e os testes façam mock nos módulos consumidores, não aqui.
    """
    if not (app_id_file.exists() and app_secret_file.exists()):
        return tj['access_token']
    q = urllib.parse.urlencode({
        'grant_type': 'fb_exchange_token',
        'client_id': app_id_file.read_text(encoding='utf-8').strip(),
        'client_secret': app_secret_file.read_text(encoding='utf-8').strip(),
        'fb_exchange_token': tj['access_token'],
    })
    try:
        r = json.load(urllib.request.urlopen(f'{GRAPH}/oauth/access_token?{q}', timeout=60))
    except urllib.error.HTTPError as e:
        print(f'  [aviso] falha ao renovar token IG: {e.code} {e.read().decode()[:160]}')
        return tj['access_token']
    if 'access_token' not in r:
        return tj['access_token']
    r['_obtained_at'] = int(time.time())
    token_json_file.write_text(json.dumps(r, ensure_ascii=False, indent=2), encoding='utf-8')
    token_file.write_text(r['access_token'], encoding='utf-8')
    print('  [token IG renovado automaticamente]')
    return r['access_token']


def read_token(
    token_file: Path,
    token_json_file: Path,
    app_id_file: Path,
    app_secret_file: Path,
    permission: str = 'instagram_content_publish',
) -> str:
    """Token de longa duração (60 dias). Renova ~7 dias antes de expirar, se houver app creds.

    `permission` aparece na mensagem de erro — cada módulo passa a permissão
    que solicita (content_publish vs basic) sem precisar duplicar a lógica.
    """
    if token_json_file.exists():
        tj = json.loads(token_json_file.read_text(encoding='utf-8'))
        if tj.get('access_token') and tj.get('_obtained_at'):
            if time.time() - tj['_obtained_at'] >= tj.get('expires_in', 5184000) - 7 * 86400:
                return refresh_token(tj, app_id_file, app_secret_file, token_json_file, token_file)
            return tj['access_token']
    if not token_file.exists():
        sys.exit(
            f'[!] token ausente: crie {token_file} com o access_token '
            f'(permissão {permission}). Veja o cabeçalho deste arquivo.'
        )
    return token_file.read_text(encoding='utf-8').strip()


def read_user_id(user_id_file: Path) -> str:
    """Lê o id numérico da conta IG Business/Creator. Encerra se ausente."""
    if not user_id_file.exists():
        sys.exit(f'[!] {user_id_file} ausente: salve o id numérico da conta IG Business/Creator.')
    return user_id_file.read_text(encoding='utf-8').strip()
