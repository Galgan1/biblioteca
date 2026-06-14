#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""[VPS v2 — ROTINA PERMANENTE] Posta o comentário de CTA em cada vídeo da FILA
assim que ele fica público. A fila (fila.json) é alimentada pelo estúdio a cada
produção — este script não precisa mais ser editado.

fila.json: [{"id": "...", "comentario": "..."}, ...]
Estado:    comentarios_state.json (ids já comentados)
Cron:      17 */2 * * * /opt/minutoreal/run.sh   (permanente; ocioso quando nada pende)
"""

import json
from pathlib import Path
from upload_youtube import get_creds
from googleapiclient.discovery import build

ROOT = Path(__file__).parent
FILA = ROOT / 'fila.json'
STATE = ROOT / 'comentarios_state.json'


def main():
    fila = json.loads(FILA.read_text(encoding='utf-8')) if FILA.exists() else []
    feitos = set(json.loads(STATE.read_text(encoding='utf-8'))) if STATE.exists() else set()
    falta = {item['id']: item['comentario'] for item in fila if item['id'] not in feitos}
    if not falta:
        print('fila vazia — nada pendente')
        return
    yt = build('youtube', 'v3', credentials=get_creds())
    # videos.list aceita até 50 ids por chamada
    ids = list(falta)
    publicos = []
    for i in range(0, len(ids), 50):
        r = yt.videos().list(part='status', id=','.join(ids[i : i + 50])).execute()
        publicos += [it['id'] for it in r['items'] if it['status']['privacyStatus'] == 'public']
    for vid in publicos:
        try:
            yt.commentThreads().insert(
                part='snippet',
                body={
                    'snippet': {
                        'videoId': vid,
                        'topLevelComment': {'snippet': {'textOriginal': falta[vid]}},
                    }
                },
            ).execute()
            feitos.add(vid)
            print(f'comentado: {vid}')
        except Exception as e:
            print(f'falhou {vid}: {str(e)[:100]}')
    STATE.write_text(json.dumps(sorted(feitos)), encoding='utf-8')
    print(f'pendentes restantes: {len(falta) - len([v for v in publicos if v in feitos])}')


if __name__ == '__main__':
    main()
