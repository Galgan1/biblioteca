# -*- coding: utf-8 -*-
"""ROTINA DE DISTRIBUIÇÃO premium do Facebook — costura os módulos nativos numa
publicação só, do jeito que o orquestrador chama.

Doutrina premium (ver FACEBOOK-PREMIUM.md): o Facebook rebaixa post-link (ainda
mais do YouTube). Então publicamos o vídeo longo como VÍDEO NATIVO e jogamos o
link (YouTube + acervo) no PRIMEIRO COMENTÁRIO — onde não pune o alcance.

Uso:  python facebook_publicar.py <slug> <video_id_do_youtube> [--dry-run]

Idempotente (cada módulo guarda seu próprio _shorts/<slug>_fb*_state.json).
Os Reels e o carrossel da semana são distribuídos pela cadência
(facebook_cadence.json), não aqui — esta rotina é o disparo único pós-upload.
"""
import sys
try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

import facebook_video
import facebook_comment


def publicar(slug, video_id, dry_run=False):
    """Vídeo longo nativo + CTA (YouTube + acervo) no 1º comentário."""
    print(f'[facebook] {slug} — vídeo nativo + CTA no 1º comentário')
    post_id = facebook_video.postar_video(slug, dry_run=dry_run)
    if dry_run:
        print('[facebook] [dry-run] CTA no 1º comentário seria postado após o vídeo.')
        facebook_comment.comentar_cta('<post_id>', video_id=video_id, dry_run=True)
        return None
    if not post_id:
        print('[facebook] vídeo nativo não publicou — pulando o comentário-CTA.')
        return None
    facebook_comment.comentar_cta(post_id, video_id=video_id)
    return post_id


if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    dry = '--dry-run' in sys.argv
    if len(args) < 2:
        sys.exit('uso: python facebook_publicar.py <slug> <video_id_do_youtube> [--dry-run]')
    publicar(args[0], args[1], dry_run=dry)
