# -*- coding: utf-8 -*-
"""ROTINA DE DISTRIBUIÇÃO — gera E sobe os Shorts de um vídeo, de uma vez.

Cenas-herói: lê o campo top-level "shorts": [idx,...] do roteiro. Se ausente,
usa um espalhamento padrão (3 conceitos: ~1/4, ~1/2, ~3/4 do vídeo).

Uso:  python produzir_shorts.py <slug> <video_id_do_longo>
Ex.:  python produzir_shorts.py poder-do-silencio A9vOvkLDj0w

Sobe cada Short unlisted (#Shorts, flag de IA, CTA p/ o vídeo-mãe). Idempotente:
estado em _shorts/<slug>_upload_state.json — não re-sobe o que já subiu.
"""
import sys, json, time
try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass
from pathlib import Path
import gerar_short
from upload_youtube import get_creds
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

ROOT = Path(__file__).parent
SH = ROOT / '_shorts'
LINK_BIB = 'www.andregalgani.com.br/biblioteca'


def hero_idxs(cfg):
    if cfg.get('shorts'):
        return cfg['shorts']
    conceitos = [i for i, c in enumerate(cfg['cenas']) if c.get('tipo') == 'conceito']
    if len(conceitos) < 3:
        return conceitos
    n = len(conceitos)
    return [conceitos[n // 4], conceitos[n // 2], conceitos[3 * n // 4]]


def short_title(cena):
    base = cena['titulo']
    return f"{base} #Shorts"[:100]


def short_desc(parent):
    return (f"Corte do resumo completo no canal Minuto Real.\n\n"
            f"▶ Vídeo completo: https://youtu.be/{parent}\n"
            f"📚 Acervo: {LINK_BIB}\n\n"
            f"Narração gerada por inteligência artificial.\n\n"
            f"#Shorts #livros #resumo #minutoreal")


def main(slug, parent):
    cfg = json.loads((ROOT / 'roteiros' / f'{slug}.json').read_text(encoding='utf-8'))
    tags = cfg.get('youtube', {}).get('tags', [])[:8] + ['shorts']
    idxs = hero_idxs(cfg)
    print(f"Cenas-herói de '{slug}': {idxs}")

    state_f = SH / f'{slug}_upload_state.json'
    state = json.loads(state_f.read_text()) if state_f.exists() else {}

    # 1) gerar os cortes que faltam
    for i in idxs:
        out = SH / f'{slug}_{i:02d}.mp4'
        if not out.exists():
            gerar_short.main(slug, i)
        else:
            print(f"  corte já existe: {out.name}")

    # 2) subir os que ainda não subiram
    yt = build('youtube', 'v3', credentials=get_creds())
    for i in idxs:
        key = str(i)
        if key in state:
            print(f"  já no ar: cena {i} -> https://youtu.be/{state[key]}")
            continue
        path = SH / f'{slug}_{i:02d}.mp4'
        cena = cfg['cenas'][i]
        body = {
            'snippet': {'title': short_title(cena), 'description': short_desc(parent),
                        'tags': tags, 'categoryId': '27', 'defaultLanguage': 'pt-BR'},
            'status': {'privacyStatus': 'unlisted', 'selfDeclaredMadeForKids': False,
                       'containsSyntheticMedia': True},
        }
        media = MediaFileUpload(str(path), mimetype='video/mp4', resumable=True, chunksize=1024 * 1024)
        req = yt.videos().insert(part='snippet,status', body=body, media_body=media)
        resp = None
        while resp is None:
            _, resp = req.next_chunk()
        state[key] = resp['id']
        state_f.write_text(json.dumps(state), encoding='utf-8')
        print(f"  SUBIU cena {i} -> https://youtu.be/{resp['id']}")
        time.sleep(1)

    print("\n=== SHORTS DE", slug, "===")
    for i in idxs:
        print(f"https://youtu.be/{state[str(i)]}  (cena {i} — {cfg['cenas'][i]['titulo']})")


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
