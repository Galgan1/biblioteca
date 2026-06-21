# -*- coding: utf-8 -*-
"""Primeiro comentário-CTA num post da Página do Facebook "Minuto Real" via Graph API.

Irmão do facebook_post.py. A TÁTICA PREMIUM do FB: o post em si é NATIVO (Reel/vídeo/
carrossel, sem link no corpo, para não ser rebaixado pelo alcance), e o link de
conversão (vídeo no YouTube + acervo no site) vai no PRIMEIRO COMENTÁRIO. Este módulo
posta esse comentário-CTA logo após a publicação.

O post_id vem dos módulos de postagem (feed/photos/video_reels/videos do facebook_post.py).

PRÉ-REQUISITOS (mesmos do facebook_post.py):
  - `.secrets/facebook_page_token.txt` (Page access token, escopo pages_manage_posts).
    NUNCA imprimir/versionar os .secrets.

Uso:
  python facebook_comment.py <post_id> [--video <video_id>] [--dry-run]
"""
import sys, json, urllib.request, urllib.parse, urllib.error
from pathlib import Path
from facebook_base import GRAPH, PAGE_TOKEN_FILE, token as _token, post as _post

ROOT = Path(__file__).parent
HUB = 'https://www.andregalgani.com.br/biblioteca'


def cta_text(video_id=None, site_url=HUB, extra=''):
    """Mensagem do primeiro comentário-CTA: gancho curto + links (YouTube se houver +
    acervo no site) + convite a curtir a Página. pt-BR. Função pura, sem efeitos."""
    linhas = ['O link tá aqui nos comentários 👇']
    if video_id:
        linhas.append(f'🎬 Resumo completo (~5 min) no YouTube: https://youtu.be/{video_id}')
    linhas.append(f'📚 O livro em 1 cheat sheet + PDF, de graça, no acervo: {site_url}')
    if extra:
        linhas.append(extra.strip())
    linhas.append('Curta a Página pra não perder — um grande livro destilado por semana.')
    return '\n'.join(linhas)


def comentar_cta(post_id, video_id=None, site_url=HUB, extra='', dry_run=False):
    """Monta e posta o comentário-CTA como primeiro comentário do post.
    Se video_id for dado, inclui o link do YouTube. Retorna o comment id ou None."""
    msg = cta_text(video_id, site_url, extra)
    params = {'message': msg}
    if video_id:
        params['attachment_url'] = f'https://youtu.be/{video_id}'  # gera preview do link
    if dry_run:
        print(f'[dry-run] POST /{post_id}/comments')
        print(f'[dry-run] params: {json.dumps(params, ensure_ascii=False, indent=1)}')
        print('[dry-run] mensagem:\n' + msg)
        print('[dry-run] PARANDO antes do POST (nada foi publicado).')
        return None
    token = _token()
    r = _post(f'/{post_id}/comments', token, params)
    if 'id' in r:
        print(f'  OK comment_id={r["id"]}')
        return r['id']
    print(f'  ERRO comments: {r.get("error", r)}')
    return None


if __name__ == '__main__':
    args = sys.argv[1:]
    if not args:
        sys.exit('uso: python facebook_comment.py <post_id> [--video <video_id>] [--dry-run]')
    post_id = args[0]
    rest = args[1:]
    dry_run = '--dry-run' in rest
    video_id = None
    if '--video' in rest:
        i = rest.index('--video')
        if i + 1 < len(rest):
            video_id = rest[i + 1]
        else:
            sys.exit('[!] --video requer um <video_id>')
    comentar_cta(post_id, video_id=video_id, dry_run=dry_run)
