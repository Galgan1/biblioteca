# -*- coding: utf-8 -*-
"""Programa o lançamento do canal: agenda os 2 longos + 8 Shorts via publishAt.
Regra da API: vídeo agendado fica 'private' até a hora marcada; o YouTube publica sozinho.

Plano (Especialista de Algoritmo): cadência semanal, longo na segunda 19h BRT,
Shorts espalhados na semana (ter 12h, qua 19h, sex 12h, sáb 10h).

Uso:  python agendar_lancamento.py            (mostra o plano, não executa)
      python agendar_lancamento.py --executar
"""

import sys
from datetime import datetime, timedelta, timezone

try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass
from upload_youtube import get_creds
from googleapiclient.discovery import build

BRT = timezone(timedelta(hours=-3))


def prox_segunda(base):
    d = base + timedelta(days=(7 - base.weekday()) % 7 or 7)
    return d


def brt(d, h):
    return datetime(d.year, d.month, d.day, h, 0, tzinfo=BRT)


hoje = datetime.now(BRT)
seg1 = prox_segunda(hoje)  # semana 1 — A Arte da Guerra
seg2 = seg1 + timedelta(days=7)  # semana 2 — Maquiavel Pedagogo

PLANO = [
    # (video_id, rótulo, datetime BRT)
    ('zLqdMHJ-k8A', 'LONGO  · A Arte da Guerra', brt(seg1, 19)),
    ('fEVIgIFu8og', 'SHORT  · A maior vitória', brt(seg1 + timedelta(days=1), 12)),
    ('sW8KKf3-CoA', 'SHORT  · Serpente de Chang', brt(seg1 + timedelta(days=2), 19)),
    ('xtrshk9yadA', 'SHORT  · Posição, não esforço', brt(seg1 + timedelta(days=4), 12)),
    ('BeR1z9GKygs', 'SHORT  · 5 fraquezas do líder', brt(seg1 + timedelta(days=5), 10)),
    ('QIYk743VByU', 'LONGO  · Maquiavel Pedagogo', brt(seg2, 19)),
    ('ODqa4x0uMTc', 'SHORT  · Experimento de 1 dólar', brt(seg2 + timedelta(days=1), 12)),
    ('A3ms3ixqn74', 'SHORT  · Queda do ensino', brt(seg2 + timedelta(days=2), 19)),
    ('gWa8BL1iZP8', 'SHORT  · Obedecer sentindo que escolheu', brt(seg2 + timedelta(days=4), 12)),
    ('eUXaxESkSCo', 'SHORT  · Manobra em três tempos', brt(seg2 + timedelta(days=5), 10)),
]


def main(executar=False):
    print(f"PLANO DE LANÇAMENTO (hoje: {hoje:%a %d/%m %H:%M} BRT)\n")
    for vid, rotulo, dt in PLANO:
        print(f"  {dt:%a %d/%m %H:%M}  {rotulo}  ({vid})")
    if not executar:
        print("\n(prévia — rode com --executar para agendar de verdade)")
        return
    yt = build('youtube', 'v3', credentials=get_creds())
    print()
    for vid, rotulo, dt in PLANO:
        body = {
            'id': vid,
            'status': {
                'privacyStatus': 'private',
                # formato exigido: ISO 8601 com sufixo Z (UTC), sem offset +00:00
                'publishAt': dt.astimezone(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.0Z'),
                'selfDeclaredMadeForKids': False,
                'containsSyntheticMedia': True,
            },
        }
        try:
            yt.videos().update(part='status', body=body).execute()
            print(f"  AGENDADO ✓ {dt:%a %d/%m %H:%M} BRT — {rotulo}")
        except Exception as e:
            print(f"  FALHOU ✗ {rotulo}: {str(e)[:120]}")
    print("\nTudo agendado. O YouTube publica sozinho nos horários acima.")


if __name__ == '__main__':
    main('--executar' in sys.argv)
