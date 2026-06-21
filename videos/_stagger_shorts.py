# -*- coding: utf-8 -*-
"""One-off: solta os Shorts de 'futebol-brasileiro' de 15 em 15 min, hoje.
Short A = ancora (ja publico, t=0). B/C/D ficam PRIVADOS agora e viram PUBLICOS
em +15 / +30 / +45 min. Idempotente o suficiente para um disparo unico."""
import sys, time
sys.path.insert(0, r'C:\Users\User\.gemini\antigravity\scratch\biblioteca\videos')
from canal_guard import get_youtube

yt = get_youtube()   # cliente JÁ verificado no Minuto Real


def setp(vid, status):
    yt.videos().update(part='status', body={'id': vid, 'status': {
        'privacyStatus': status, 'selfDeclaredMadeForKids': False,
        'containsSyntheticMedia': True}}).execute()
    print(time.strftime('%H:%M:%S'), status.upper(), vid, flush=True)


A = 'HqUq3UaQR-8'  # cena 3 — O Vasco quebra o muro (ancora, t=0)
B = 'u-MFX8AcTg4'  # cena 8 — 1958, enfim campeao   (+15 min)
C = 'eF9wJWeiPvQ'  # cena 10 — gloria               (+30 min)
D = 't_wyaqoDrjs'  # cena 12 — encerramento          (+45 min)

# t=0: ancora publica; recolhe os outros tres
setp(A, 'public')
for v in (B, C, D):
    setp(v, 'private')

# drip de 15 em 15 minutos
time.sleep(900); setp(B, 'public')
time.sleep(900); setp(C, 'public')
time.sleep(900); setp(D, 'public')
print('DONE drip 15min', flush=True)
