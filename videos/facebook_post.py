# -*- coding: utf-8 -*-
"""Publicação automática na Página do Facebook "Minuto Real" via Graph API.

Irmão do instagram_post.py. A Página (id em facebook_page_id.txt) está vinculada à
mesma conta @minutoreal1701; o token de Página (pages_manage_posts) vive em
facebook_page_token.txt. NUNCA imprimir/versionar os .secrets.

O funil do canal é FB → YouTube/Biblioteca, então o post padrão é um POST-LINK do
vídeo longo (mensagem-gancho + link do YouTube, que vira card de preview no feed).

PRÉ-REQUISITOS (passos do Showrunner — já concluídos pela lane do Instagram):
  - Página FB vinculada à @minutoreal1701 (Meta Business Suite).
  - App Meta "Minuto Real Poster" com escopo `pages_manage_posts` (+ pages_show_list).
  - `.secrets/facebook_page_token.txt` (Page access token) + `.secrets/facebook_page_id.txt`.
    (Opcional auto-refresh: instagram_app_id.txt + instagram_app_secret.txt já servem —
     Page token derivado de user token de longa duração não expira enquanto o user token valer.)

Uso:
  python facebook_post.py <slug> <video_id_do_longo>   # post-link do longo no feed da Página
  python facebook_post.py text "<mensagem>"            # post de texto avulso
  python facebook_post.py link "<url>" "<mensagem>"     # post-link avulso
"""
import sys, json, urllib.request, urllib.parse, urllib.error
from pathlib import Path

ROOT = Path(__file__).parent
SH = ROOT / '_shorts'
SEC = ROOT / '.secrets'
GRAPH = 'https://graph.facebook.com/v21.0'
PAGE_TOKEN_FILE = SEC / 'facebook_page_token.txt'
PAGE_ID_FILE = SEC / 'facebook_page_id.txt'
HASHTAGS_BASE = ['livros', 'resumodelivro', 'leitura']
HUB = 'https://www.andregalgani.com.br/biblioteca'


def _token():
    if not PAGE_TOKEN_FILE.exists():
        sys.exit(f'[!] {PAGE_TOKEN_FILE} ausente: salve o Page access token (escopo '
                 'pages_manage_posts). Veja o cabeçalho deste arquivo.')
    return PAGE_TOKEN_FILE.read_text(encoding='utf-8').strip()


def _page_id():
    if not PAGE_ID_FILE.exists():
        sys.exit(f'[!] {PAGE_ID_FILE} ausente: salve o id numérico da Página do Facebook.')
    return PAGE_ID_FILE.read_text(encoding='utf-8').strip()


def _post(path, token, params):
    data = urllib.parse.urlencode({**params, 'access_token': token}).encode()
    req = urllib.request.Request(f'{GRAPH}{path}', data=data)
    try:
        return json.load(urllib.request.urlopen(req, timeout=120))
    except urllib.error.HTTPError as e:
        return {'error': {'code': e.code, 'message': e.read().decode()[:300]}}


def caption_for(cfg):
    """Mensagem do post-link: gancho + entrega + CTA de conversão pro acervo (site)
    + reforço do vídeo (card abaixo) + 3–5 hashtags de nicho. Coeso e voltado à conversão."""
    yt = cfg.get('youtube', {})
    gancho = yt.get('titulo', cfg['titulo']).split('|')[0].strip()
    tags = [t.replace(' ', '').lower() for t in yt.get('tags', [])[:2]]
    hs = ' '.join('#' + t for t in (HASHTAGS_BASE + tags))
    return (f"{gancho}\n\n"
            f"As ideias que ficam de \"{cfg['titulo']}\" — destiladas, em minutos.\n"
            f"📄 O livro inteiro em 1 cheat sheet + PDF, de graça, no acervo: {HUB}\n"
            f"🎬 Prefere assistir? O resumo de ~5 min está no vídeo abaixo. 👇\n\n"
            f"Curta a Página e acompanhe — um grande livro destilado por semana.\n"
            f"Narração e arte por IA.\n\n{hs}")


def post_link(url, message):
    """Publica um post-link no feed da Página. Retorna o post id ou None."""
    token, pid = _token(), _page_id()
    r = _post(f'/{pid}/feed', token, {'message': message, 'link': url})
    if 'id' in r:
        print(f'  OK post_id={r["id"]}')
        return r['id']
    print(f'  ERRO feed: {r.get("error", r)}')
    return None


def post_text(message):
    token, pid = _token(), _page_id()
    r = _post(f'/{pid}/feed', token, {'message': message})
    if 'id' in r:
        print(f'  OK post_id={r["id"]}')
        return r['id']
    print(f'  ERRO feed: {r.get("error", r)}')
    return None


def postar_longo(slug, video_id):
    """Post-link do vídeo longo (idempotente em _shorts/<slug>_facebook_state.json)."""
    cfg = json.loads((ROOT / 'roteiros' / f'{slug}.json').read_text(encoding='utf-8'))
    state_f = SH / f'{slug}_facebook_state.json'
    state = json.loads(state_f.read_text()) if state_f.exists() else {}
    if video_id in state:
        print(f'  já no Facebook: {video_id} ({state[video_id]})'); return
    msg = caption_for(cfg)
    (SH / f'{slug}_facebook_caption.md').write_text(msg, encoding='utf-8')
    print(f'  postando link do longo de {slug}...')
    pid = post_link(f'https://youtu.be/{video_id}', msg)
    if pid:
        state[video_id] = pid
        state_f.write_text(json.dumps(state, ensure_ascii=False, indent=1), encoding='utf-8')


if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) >= 3 and args[0] == 'link':
        post_link(args[1], args[2])
    elif len(args) >= 2 and args[0] == 'text':
        post_text(args[1])
    elif len(args) == 2:
        postar_longo(args[0], args[1])
    else:
        sys.exit('uso: python facebook_post.py <slug> <video_id>  |  '
                 'python facebook_post.py text "<mensagem>"  |  '
                 'python facebook_post.py link "<url>" "<mensagem>"')
