# -*- coding: utf-8 -*-
"""Read-only: confere o estado REAL de agendamento dos vídeos no YouTube
(privacyStatus + publishAt) contra o que o cronograma afirma. Não muta nada.
"""
import sys
from datetime import datetime, timezone, timedelta
try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass
from upload_youtube import get_creds
from googleapiclient.discovery import build

BRT = timezone(timedelta(hours=-3))
CANAL_OK = 'UC2N5xZ-gyCU3hNvH1QqNahA'

# (id, rótulo, esperado-BRT segundo o cronograma)
ESPERADO = [
    # longos
    ('WAHhiIW6Wjc', 'Save the Cat [LONGO]', 'público 13/06'),
    ('Eb4LTgfF65o', 'Jornada [LONGO]', '14/06 19h'),
    ('dzPz77iqffs', 'Nação Dopamina [LONGO]', '15/06 19h'),
    ('3X5s-p2LH9c', 'Silêncio [LONGO]', '29/06 19h'),
    ('JDmuaZ9hA_U', 'Quem Mexeu [LONGO]', '06/07 19h'),
    ('ur9LHfpKUCY', 'Padrão Bitcoin [LONGO]', '13/07 19h'),
    # STC shorts
    ('QVKAObJqcQg', 'STC short #1', 'público 13/06'),
    ('3sXdnZ3avHU', 'STC short #2', '14/06 10h'),
    ('9E0napGqpnY', 'STC short #3', '15/06 12h'),
    ('1wUlNH-otWE', 'STC short #4', '16/06 10h'),
    # shorts de lançamento
    ('fEVIgIFu8og', 'Lançamento short A', '16/06 12h'),
    ('sW8KKf3-CoA', 'Lançamento short B', '17/06 19h'),
    ('xtrshk9yadA', 'Lançamento short C', '19/06 12h'),
    ('ODqa4x0uMTc', 'Lançamento short D', '23/06 12h'),
    ('gWa8BL1iZP8', 'Lançamento short E', '26/06 12h'),
    ('eUXaxESkSCo', 'Lançamento short F', '27/06 10h'),
    # Silêncio shorts
    ('LAlSS3Gkbgk', 'Silêncio short #1', '30/06 12h'),
    ('XbR5IfLl190', 'Silêncio short #2', '01/07 19h'),
    ('zSyLcgLWBwo', 'Silêncio short #3', '03/07 12h'),
    ('JPYYyEVZVlU', 'Silêncio short #4', '04/07 10h'),
    # Quem Mexeu shorts
    ('ynwCFDI8Vl4', 'Quem Mexeu short #1', '07/07'),
    ('fnzyThF7fic', 'Quem Mexeu short #2', '08/07'),
    ('VijxfJZj-vQ', 'Quem Mexeu short #3', '10/07'),
    ('vvlVJxGaG98', 'Quem Mexeu short #4', '11/07'),
    # Bitcoin shorts
    ('iXQOU8uVCJs', 'Bitcoin short #1', '14/07'),
    ('OuIMtbDcxUk', 'Bitcoin short #2', '15/07'),
    ('seCJSaOZOpk', 'Bitcoin short #3', '17/07'),
]


def fmt(pub):
    if not pub:
        return '—'
    dt = datetime.fromisoformat(pub.replace('Z', '+00:00')).astimezone(BRT)
    return dt.strftime('%d/%m %H:%M BRT')


def main():
    yt = build('youtube', 'v3', credentials=get_creds())
    ch = yt.channels().list(part='snippet', mine=True).execute()['items'][0]
    if ch['id'] != CANAL_OK:
        sys.exit(f"[X] canal errado: {ch['snippet']['title']} ({ch['id']})")
    print(f"canal: {ch['snippet']['title']} ✓\n")

    ids = [i for i, _, _ in ESPERADO]
    got = {}
    for k in range(0, len(ids), 50):
        chunk = ids[k:k + 50]
        resp = yt.videos().list(part='status,snippet', id=','.join(chunk)).execute()
        for it in resp.get('items', []):
            got[it['id']] = it

    agora = datetime.now(BRT)
    print(f"{'rótulo':<22} {'esperado':<14} {'privacidade':<11} {'publishAt real':<18} obs")
    print('-' * 90)
    faltando, alertas = [], []
    for vid, rot, esp in ESPERADO:
        it = got.get(vid)
        if not it:
            faltando.append((rot, vid))
            print(f"{rot:<22} {esp:<14} {'AUSENTE':<11} {'—':<18} ❌ não encontrado no canal")
            continue
        st = it['status']
        priv = st.get('privacyStatus', '?')
        pub = st.get('publishAt')
        real = fmt(pub)
        obs = ''
        if priv == 'public':
            obs = '✅ já público'
        elif priv == 'private' and pub:
            dt = datetime.fromisoformat(pub.replace('Z', '+00:00')).astimezone(BRT)
            if dt < agora:
                obs = '⚠️ publishAt no PASSADO (travado private?)'
                alertas.append((rot, real))
            else:
                obs = '🕒 agendado'
        elif priv == 'private' and not pub:
            obs = '⚠️ private SEM publishAt (não vai ao ar sozinho)'
            alertas.append((rot, 'sem publishAt'))
        elif priv == 'unlisted':
            obs = '⚠️ unlisted (não agendado)'
            alertas.append((rot, 'unlisted'))
        print(f"{rot:<22} {esp:<14} {priv:<11} {real:<18} {obs}")

    print('\n=== RESUMO ===')
    print(f"verificados: {len(ESPERADO)} · encontrados: {len(got)} · ausentes: {len(faltando)} · alertas: {len(alertas)}")
    if faltando:
        print('AUSENTES:', ', '.join(f'{r} ({v})' for r, v in faltando))
    if alertas:
        print('ALERTAS:', ', '.join(f'{r} [{x}]' for r, x in alertas))


if __name__ == '__main__':
    main()
