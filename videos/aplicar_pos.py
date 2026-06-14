# -*- coding: utf-8 -*-
"""Aplica a pós-produção (legendas + capítulos + playlist) num vídeo JÁ no YouTube
(backfill retroativo). Recupera o timing do artefato se faltar.

Uso:  python aplicar_pos.py <slug> <video_id>
Ex.:  python aplicar_pos.py padrao-bitcoin ur9LHfpKUCY

- Capítulos: lê o snippet atual e ANEXA o bloco à descrição (videos.update, só campos
  graváveis — preserva título/tags/categoria; NÃO toca status/publishAt/agendamento).
- Legendas: sobe faixa standard pt-BR (pula se já existir uma).
- Playlist: garante a temática e adiciona o vídeo.
Idempotente: não duplica capítulos (checa '0:00'), legenda standard nem item de playlist.
"""

import sys, json
from pathlib import Path
from upload_youtube import get_creds
from googleapiclient.discovery import build
import youtube_pos as yp
import recuperar_timing

ROOT = Path(__file__).parent
CANAL_OK = 'UC2N5xZ-gyCU3hNvH1QqNahA'  # Minuto Real (NUNCA o pessoal)


def _writable_snippet(old, new_desc):
    snip = {'title': old['title'], 'categoryId': old['categoryId'], 'description': new_desc}
    for k in ('tags', 'defaultLanguage', 'defaultAudioLanguage'):
        if k in old:
            snip[k] = old[k]
    return snip


def main(slug, vid):
    cfg = json.loads((ROOT / 'roteiros' / f'{slug}.json').read_text(encoding='utf-8'))
    if not yp.load_timing(slug):
        print('timing ausente -> recuperando do artefato...')
        recuperar_timing.main(slug)
    tm = yp.load_timing(slug)
    yt = build('youtube', 'v3', credentials=get_creds())

    ch = yt.channels().list(part='snippet', mine=True).execute()['items'][0]
    if ch['id'] != CANAL_OK:
        sys.exit(f"[X] canal errado: {ch['snippet']['title']} ({ch['id']}) — aborta.")
    print(f"canal: {ch['snippet']['title']} ✓")

    feito = []
    cenas = cfg['cenas']
    if tm and len(tm[1]) == len(cenas):
        tail, durs = tm
        # 1) CAPÍTULOS
        bloco = yp.build_chapters(cenas, durs)
        snip = yt.videos().list(part='snippet', id=vid).execute()['items'][0]['snippet']
        if bloco and '0:00' not in snip.get('description', ''):
            nd = f"{snip.get('description', '')}\n\n⏱️ Capítulos\n{bloco}"[:5000]
            yt.videos().update(
                part='snippet', body={'id': vid, 'snippet': _writable_snippet(snip, nd)}
            ).execute()
            feito.append(f'capítulos ({len(bloco.splitlines())})')
        else:
            print('  capítulos já presentes — pulando')
        # 2) LEGENDAS
        srt = yp.build_srt(cenas, durs, tail)
        if srt.strip():
            yp.LEG.mkdir(exist_ok=True)
            p = yp.LEG / f'{slug}.srt'
            p.write_text(srt, encoding='utf-8')
            existing = yt.captions().list(part='snippet', videoId=vid).execute().get('items', [])
            ja = any(
                c['snippet'].get('trackKind') == 'standard'
                and c['snippet'].get('language', '').startswith('pt')
                for c in existing
            )
            if ja:
                print('  legenda standard pt já existe — pulando')
            else:
                yp.upload_caption(yt, vid, p)
                feito.append(f'legendas ({srt.count(" --> ")} cues)')
    else:
        print('  [aviso] sem timing válido -> capítulos/legendas pulados')

    # 3) PLAYLIST
    title = yp.playlist_title_for(cfg)
    pid = yp.ensure_playlist(yt, title)
    try:  # playlist recém-criada pode demorar a responder ao list (404) — então só dedup se der
        itens = (
            yt.playlistItems()
            .list(part='snippet', playlistId=pid, maxResults=50)
            .execute()
            .get('items', [])
        )
    except Exception:
        itens = []
    if any(i['snippet']['resourceId'].get('videoId') == vid for i in itens):
        print(f'  já na playlist «{title}» — pulando')
    else:
        yp.add_to_playlist(yt, pid, vid)
        feito.append(f'playlist «{title}»')

    print('\nAPLICADO:', ' · '.join(feito) if feito else '(nada novo)')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
