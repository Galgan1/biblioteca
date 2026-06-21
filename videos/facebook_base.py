# -*- coding: utf-8 -*-
"""Helpers compartilhados da família Facebook do Minuto Real.

Extraído de facebook_post.py, facebook_reels.py, facebook_carrossel.py,
facebook_video.py e facebook_comment.py, onde GRAPH, HASHTAGS_BASE,
PAGE_TOKEN_FILE, PAGE_ID_FILE, _token(), _page_id() e _post() eram idênticos
(ou quase — as variações de msg de erro foram unificadas na mensagem canônica
de facebook_post.py, usando o caminho completo, não só o .name).

Importar em cada módulo-filho:
    from facebook_base import (
        GRAPH, HASHTAGS_BASE, PAGE_TOKEN_FILE, PAGE_ID_FILE,
        token, page_id, post,
    )
e criar aliases locais _token/_page_id/_post se necessário para preservar API
interna. facebook_post.py mantém _token/_page_id/_post como funções próprias
porque os testes de unittest usam mock.patch('facebook_post.urllib.request.urlopen')
e mock.patch.object(facebook_post, 'PAGE_TOKEN_FILE') — esses patches só funcionam
quando a função que lê o arquivo e chama urlopen está definida no próprio módulo.
"""
import sys
import json
import urllib.request
import urllib.parse
import urllib.error
from pathlib import Path

ROOT = Path(__file__).parent
SEC = ROOT / '.secrets'

GRAPH = 'https://graph.facebook.com/v21.0'
HASHTAGS_BASE = ['livros', 'resumodelivro', 'leitura']

PAGE_TOKEN_FILE = SEC / 'facebook_page_token.txt'
PAGE_ID_FILE = SEC / 'facebook_page_id.txt'


def token(path: Path = PAGE_TOKEN_FILE) -> str:
    """Lê e retorna o Page access token; sys.exit se o arquivo não existir."""
    if not path.exists():
        sys.exit(
            f'[!] {path} ausente: salve o Page access token (escopo '
            'pages_manage_posts). Veja o cabeçalho do facebook_post.py.'
        )
    return path.read_text(encoding='utf-8').strip()


def page_id(path: Path = PAGE_ID_FILE) -> str:
    """Lê e retorna o id numérico da Página; sys.exit se o arquivo não existir."""
    if not path.exists():
        sys.exit(f'[!] {path} ausente: salve o id numérico da Página do Facebook.')
    return path.read_text(encoding='utf-8').strip()


def post(path: str, tok: str, params: dict) -> dict:
    """POST application/x-www-form-urlencoded na Graph API.

    Injeta access_token nos params. Sucesso → dict com a resposta JSON.
    HTTPError → {'error': {'code': <int>, 'message': <str truncada em 300 chars>}}.
    """
    data = urllib.parse.urlencode({**params, 'access_token': tok}).encode()
    req = urllib.request.Request(f'{GRAPH}{path}', data=data)
    try:
        return json.load(urllib.request.urlopen(req, timeout=120))
    except urllib.error.HTTPError as e:
        return {'error': {'code': e.code, 'message': e.read().decode()[:300]}}
