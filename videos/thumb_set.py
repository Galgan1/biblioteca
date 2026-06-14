# -*- coding: utf-8 -*-
"""Define a thumbnail custom de um vídeo via YouTube Data API (thumbnails.set).
Reusa as credenciais OAuth do upload_youtube. Requer canal verificado p/ thumb custom.

Uso:  python thumb_set.py <video_id> <imagem.png>
"""

import sys

try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass
from upload_youtube import get_creds
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from googleapiclient.errors import HttpError

vid, img = sys.argv[1], sys.argv[2]
yt = build('youtube', 'v3', credentials=get_creds())
try:
    yt.thumbnails().set(videoId=vid, media_body=MediaFileUpload(img)).execute()
    print(f'OK ✓ thumbnail definida em https://youtu.be/{vid}')
except HttpError as e:
    print(f'FALHA ({e.resp.status}): {e}')
    print('Provável causa: canal não verificado p/ thumbnail custom OU escopo OAuth insuficiente.')
    print('Solução: suba o arquivo manualmente no YouTube Studio (1 clique).')
