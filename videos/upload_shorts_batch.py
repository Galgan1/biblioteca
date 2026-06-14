# -*- coding: utf-8 -*-
"""Sobe a leva de Shorts ao YouTube (unlisted) via a mesma API/OAuth do canal.
Cada Short: vertical 9:16 + #Shorts no título → YouTube classifica como Short.

Uso:  python upload_shorts_batch.py
"""

import sys, time

try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass
from pathlib import Path
from upload_youtube import get_creds
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

ROOT = Path(__file__).parent
SH = ROOT / '_shorts'
LINK_BIB = 'www.andregalgani.com.br/biblioteca'

# (arquivo, título com #Shorts, link do vídeo-mãe, tags)
ARTE = 'youtu.be/zLqdMHJ-k8A'
MAQ = 'youtu.be/QIYk743VByU'
SHORTS = [
    (
        'arte-da-guerra_01.mp4',
        'A maior vitória não é vencer a batalha #Shorts',
        ARTE,
        ['a arte da guerra', 'sun tzu', 'estratégia', 'shorts', 'livros'],
    ),
    (
        'arte-da-guerra_06.mp4',
        'A energia vem da posição, não do esforço #Shorts',
        ARTE,
        ['a arte da guerra', 'sun tzu', 'estratégia', 'foco', 'shorts'],
    ),
    (
        'arte-da-guerra_09.mp4',
        'O exército que se move como uma serpente #Shorts',
        ARTE,
        ['a arte da guerra', 'sun tzu', 'liderança', 'equipe', 'shorts'],
    ),
    (
        'arte-da-guerra_10.mp4',
        'As 5 fraquezas que destroem um líder #Shorts',
        ARTE,
        ['a arte da guerra', 'sun tzu', 'liderança', 'autoconhecimento', 'shorts'],
    ),
    (
        'maquiavel-pedagogo_02.mp4',
        'O experimento de 1 dólar que inverteu a psicologia #Shorts',
        MAQ,
        ['maquiavel pedagogo', 'pascal bernardin', 'psicologia', 'educação', 'shorts'],
    ),
    (
        'maquiavel-pedagogo_03.mp4',
        'Por que você obedece sentindo que escolheu #Shorts',
        MAQ,
        ['maquiavel pedagogo', 'pascal bernardin', 'psicologia', 'educação', 'shorts'],
    ),
    (
        'maquiavel-pedagogo_06.mp4',
        'A manobra em três tempos para controlar valores #Shorts',
        MAQ,
        ['maquiavel pedagogo', 'pascal bernardin', 'educação', 'sociedade', 'shorts'],
    ),
    (
        'maquiavel-pedagogo_10.mp4',
        'E se a queda do ensino não for um fracasso? #Shorts',
        MAQ,
        ['maquiavel pedagogo', 'pascal bernardin', 'educação', 'sociedade', 'shorts'],
    ),
]


def desc(parent):
    return (
        f"Corte do resumo completo no canal Minuto Real.\n\n"
        f"▶ Vídeo completo: {parent}\n"
        f"📚 Acervo em cheat sheets: {LINK_BIB}\n\n"
        f"Narração e imagens geradas por inteligência artificial.\n\n"
        f"#Shorts #livros #resumo #minutoreal"
    )


def main():
    yt = build('youtube', 'v3', credentials=get_creds())
    links = []
    for fname, title, parent, tags in SHORTS:
        path = SH / fname
        if not path.exists():
            print(f'[!] ausente: {fname}')
            continue
        body = {
            'snippet': {
                'title': title[:100],
                'description': desc(parent)[:5000],
                'tags': tags,
                'categoryId': '27',
                'defaultLanguage': 'pt-BR',
            },
            'status': {
                'privacyStatus': 'unlisted',
                'selfDeclaredMadeForKids': False,
                'containsSyntheticMedia': True,
            },
        }
        media = MediaFileUpload(
            str(path), mimetype='video/mp4', resumable=True, chunksize=1024 * 1024
        )
        req = yt.videos().insert(part='snippet,status', body=body, media_body=media)
        resp = None
        while resp is None:
            _, resp = req.next_chunk()
        vid = resp['id']
        print(f"OK  {fname}  ->  https://youtu.be/{vid}")
        links.append((fname, vid))
        time.sleep(1)
    print('\n=== TODOS OS SHORTS ===')
    for f, v in links:
        print(f"https://youtu.be/{v}   ({f})")


if __name__ == '__main__':
    main()
