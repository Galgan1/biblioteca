# -*- coding: utf-8 -*-
"""Publicação automática no TikTok via Content Posting API. Conta do canal: @minuto_real2.

Dois modos: Direct Post (publica direto — exige app AUDITADO + escopo video.publish) e
rascunho/inbox (--draft — escopo video.upload, SEM auditoria; você toca publicar no app).

PRÉ-REQUISITOS (passos do Showrunner — NÃO dá para automatizar):
  1. Conta em https://developers.tiktok.com → criar um app.
  2. Adicionar o produto "Content Posting API" e o escopo `video.publish`
     (Direct Post). Submeter o app à AUDITORIA do TikTok (gated; sem auditoria
     só dá para `video.upload` = rascunho).
  3. Fazer o OAuth com a conta do canal (escopo video.publish) e obter o
     `access_token`. Salvar em `.secrets/tiktok_token.txt` (1 linha).
     (Tokens expiram — renovar via refresh_token quando necessário.)
  4. Verificar o domínio se for usar PULL_FROM_URL (aqui usamos FILE_UPLOAD,
     que NÃO exige verificação de domínio).

Depois disso:
  python tiktok_post.py <slug>                 # posta os shorts do livro (idempotente)
  python tiktok_post.py file <mp4> "legenda"   # posta um arquivo avulso

Stdlib only (urllib). Conteúdo do canal é narrado por IA → marcamos AIGC.
"""

import sys, json, time, urllib.request, urllib.error, math
from pathlib import Path

ROOT = Path(__file__).parent
SH = ROOT / '_shorts'
BASE = 'https://open.tiktokapis.com/v2'
TOKEN_FILE = ROOT / '.secrets' / 'tiktok_token.txt'
TOKEN_JSON = ROOT / '.secrets' / 'tiktok_token.json'
CLIENT_KEY_FILE = ROOT / '.secrets' / 'tiktok_client_key.txt'
CLIENT_SECRET_FILE = ROOT / '.secrets' / 'tiktok_client_secret.txt'
OAUTH_TOKEN_URL = 'https://open.tiktokapis.com/v2/oauth/token/'
HASHTAGS_BASE = ['resumodelivro', 'livros', 'conhecimento', 'aprendanotiktok']


def _refresh(tj):
    """Renova o access_token via refresh_token. Atualiza os dois arquivos e devolve o token novo."""
    import urllib.parse

    data = urllib.parse.urlencode(
        {
            'client_key': CLIENT_KEY_FILE.read_text(encoding='utf-8').strip(),
            'client_secret': CLIENT_SECRET_FILE.read_text(encoding='utf-8').strip(),
            'grant_type': 'refresh_token',
            'refresh_token': tj['refresh_token'],
        }
    ).encode()
    req = urllib.request.Request(
        OAUTH_TOKEN_URL, data=data, headers={'Content-Type': 'application/x-www-form-urlencoded'}
    )
    try:
        r = json.load(urllib.request.urlopen(req, timeout=60))
    except urllib.error.HTTPError as e:
        sys.exit(
            f'[!] falha ao renovar token TikTok: {e.code} {e.read().decode()[:200]} '
            '(refresh_token pode ter expirado — refaça o OAuth).'
        )
    if 'access_token' not in r:
        sys.exit(f'[!] resposta de refresh sem access_token: {r}')
    r['_obtained_at'] = int(time.time())
    TOKEN_JSON.write_text(json.dumps(r, ensure_ascii=False, indent=2), encoding='utf-8')
    TOKEN_FILE.write_text(r['access_token'], encoding='utf-8')
    print('  [token TikTok renovado automaticamente]')
    return r['access_token']


def _token():
    # Fonte de verdade = tiktok_token.json (tem refresh_token); renova sozinho ~5min antes de expirar.
    if TOKEN_JSON.exists():
        tj = json.loads(TOKEN_JSON.read_text(encoding='utf-8'))
        if tj.get('refresh_token') and tj.get('_obtained_at'):
            if time.time() - tj['_obtained_at'] >= tj.get('expires_in', 86400) - 300:
                return _refresh(tj)
            return tj['access_token']
    if not TOKEN_FILE.exists():
        sys.exit(
            f'[!] token ausente: crie {TOKEN_FILE} com o access_token (escopo video.publish). '
            'Veja o cabeçalho deste arquivo para os passos.'
        )
    return TOKEN_FILE.read_text(encoding='utf-8').strip()


def _api(path, token, body):
    req = urllib.request.Request(
        f'{BASE}{path}',
        data=json.dumps(body).encode('utf-8'),
        headers={
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json; charset=UTF-8',
        },
    )
    try:
        return json.load(urllib.request.urlopen(req, timeout=60))
    except urllib.error.HTTPError as e:
        return {'error': {'code': e.code, 'message': e.read().decode()[:300]}}


def post_video(mp4, caption, privacy='PUBLIC_TO_EVERYONE', aigc=True, draft=False):
    """Posta um vídeo. draft=False → Direct Post (app auditado, escopo video.publish);
    draft=True → manda para os RASCUNHOS do TikTok (escopo video.upload, SEM auditoria —
    você finaliza no app). Retorna publish_id ou None."""
    token = _token()
    data = Path(mp4).read_bytes()
    size = len(data)
    # FILE_UPLOAD: vídeos pequenos cabem num único chunk (limite 5MB–64MB/chunk)
    src = {'source': 'FILE_UPLOAD', 'video_size': size, 'chunk_size': size, 'total_chunk_count': 1}
    if draft:
        init = _api('/post/publish/inbox/video/init/', token, {'source_info': src})
    else:
        init = _api(
            '/post/publish/video/init/',
            token,
            {
                'post_info': {
                    'title': caption[:2200],
                    'privacy_level': privacy,  # PUBLIC_TO_EVERYONE exige app auditado
                    'disable_comment': False,
                    'disable_duet': False,
                    'disable_stitch': False,
                    'video_cover_timestamp_ms': 1000,
                    'is_aigc': bool(aigc),  # disclosure de conteúdo gerado por IA
                },
                'source_info': src,
            },
        )
    if init.get('error', {}).get('code') not in (None, 'ok'):
        print(f'  ERRO init: {init["error"]}')
        return None
    d = init['data']
    pid, upload_url = d['publish_id'], d['upload_url']
    # envia os bytes (PUT com Content-Range)
    put = urllib.request.Request(
        upload_url,
        data=data,
        method='PUT',
        headers={
            'Content-Type': 'video/mp4',
            'Content-Range': f'bytes 0-{size - 1}/{size}',
            'Content-Length': str(size),
        },
    )
    try:
        urllib.request.urlopen(put, timeout=300)
    except urllib.error.HTTPError as e:
        print(f'  ERRO upload: {e.code} {e.read().decode()[:200]}')
        return None
    # confirma o processamento
    for _ in range(20):
        st = _api('/post/publish/status/fetch/', token, {'publish_id': pid}).get('data', {})
        s = st.get('status')
        if s in ('PUBLISH_COMPLETE', 'SEND_TO_USER_INBOX'):
            print(f'  OK ✓ {s} · publish_id={pid}')
            return pid
        if s == 'FAILED':
            print(f'  FALHOU: {st.get("fail_reason")}')
            return None
        time.sleep(6)
    print(f'  (ainda processando) publish_id={pid}')
    return pid


def caption_for(cfg, idx):
    """Legenda nativa de TikTok: 1ª frase (gancho) + CTA + hashtags amplas+nicho."""
    import re

    cena = cfg['cenas'][idx]
    gancho = re.split(r'(?<=[.?!])\s', cena['narracao'].strip())[0].strip()  # 1ª frase inteira
    tags = [t.replace(' ', '') for t in cfg.get('youtube', {}).get('tags', [])[:4]]
    hs = ' '.join('#' + t for t in (tags + HASHTAGS_BASE))
    return f"{gancho}\n\n📚 {cfg['titulo']} — resumo completo no canal Minuto Real (link na bio).\n\n{hs}"


def postar_shorts(slug, draft=False):
    cfg = json.loads((ROOT / 'roteiros' / f'{slug}.json').read_text(encoding='utf-8'))
    state_f = SH / f'{slug}_tiktok_state.json'
    state = json.loads(state_f.read_text()) if state_f.exists() else {}
    # salva as legendas sugeridas (útil no modo rascunho: copie e cole no app)
    caps = '\n\n'.join(f'### cena {i}\n{caption_for(cfg, i)}' for i in cfg.get('shorts', []))
    (SH / f'{slug}_tiktok_captions.md').write_text(caps, encoding='utf-8')
    for i in cfg.get('shorts', []):
        key = str(i)
        mp4 = SH / f'{slug}_{i:02d}.mp4'
        if key in state:
            print(f'  já no TikTok: cena {i} ({state[key]})')
            continue
        if not mp4.exists():
            print(f'  [!] short ausente: {mp4.name}')
            continue
        print(f'  postando cena {i}{" (rascunho)" if draft else ""}...')
        pid = post_video(str(mp4), caption_for(cfg, i), draft=draft)
        if pid:
            state[key] = pid
            state_f.write_text(json.dumps(state, ensure_ascii=False, indent=1), encoding='utf-8')


if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if a != '--draft']
    draft = '--draft' in sys.argv
    if len(args) >= 3 and args[0] == 'file':
        post_video(args[1], args[2], draft=draft)
    elif len(args) == 1:
        postar_shorts(args[0], draft=draft)
    else:
        sys.exit(
            'uso: python tiktok_post.py <slug> [--draft]  |  python tiktok_post.py file <mp4> "legenda" [--draft]'
        )
