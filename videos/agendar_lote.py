# -*- coding: utf-8 -*-
"""ROTINA: agenda a publicação de um lote (longo + Shorts) na grade do canal.

Cadência (parecer do Especialista de Algoritmo, jun/2026): **2 longos por semana
(SEGUNDA e QUINTA, 19h BRT) + 1 short por dia**. Cada longo é agendado no seu dia;
seus 4 shorts caem nos 4 dias seguintes, 1 por dia. Assim o canal publica todo dia
(≥2/dia quando longo+short coincidem) sem empilhar longos nem queimar o acervo.
Regra da API: publishAt exige o vídeo 'private' (e que nunca tenha sido público).

Ao agendar o longo, o ECO no Instagram é enfileirado AUTOMATICAMENTE (Reel-herói,
+2h, via sincronizar.py) — uma única ação agenda as duas plataformas em sincronia.

Uso:  python agendar_lote.py <slug> <video_id_longo> <DD/MM>  (use SEGUNDAS e QUINTAS)
Ex.:  python agendar_lote.py sound-design <id> 20/07   (seg)
      python agendar_lote.py audiovisao  <id> 23/07   (qui)
"""
import sys, json
from datetime import datetime, timedelta, timezone
try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass
from pathlib import Path
from upload_youtube import get_creds
from googleapiclient.discovery import build

ROOT = Path(__file__).parent
BRT = timezone(timedelta(hours=-3))
DOW = ['seg', 'ter', 'qua', 'qui', 'sex', 'sáb', 'dom']
SLOTS_SHORTS = [(1, 12), (2, 19), (3, 12), (4, 10)]  # (dias após o longo, hora) — 1/dia


def agendar(yt, vid, dt, rotulo):
    body = {'id': vid, 'status': {
        'privacyStatus': 'private',
        'publishAt': dt.astimezone(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.0Z'),
        'selfDeclaredMadeForKids': False, 'containsSyntheticMedia': True}}
    try:
        yt.videos().update(part='status', body=body).execute()
        print(f'  AGENDADO ✓ {dt:%a %d/%m %H:%M} BRT — {rotulo} ({vid})')
    except Exception as e:
        print(f'  FALHOU ✗ {rotulo} ({vid}): {str(e)[:110]}')


def main(slug, longo_id, ddmm):
    d, m = map(int, ddmm.split('/'))
    ano = datetime.now(BRT).year
    dia = datetime(ano, m, d, hour=19, tzinfo=BRT)
    if dia.weekday() not in (0, 3):
        print(f'  [i] {ddmm} é {DOW[dia.weekday()]}; para 2 longos/semana use SEGUNDA e QUINTA.')
    yt = build('youtube', 'v3', credentials=get_creds())
    agendar(yt, longo_id, dia, f'LONGO · {slug} ({DOW[dia.weekday()]})')
    st = ROOT / '_shorts' / f'{slug}_upload_state.json'
    shorts = list(json.loads(st.read_text()).values()) if st.exists() else []
    for vid, (dias, hora) in zip(shorts, SLOTS_SHORTS):
        alvo = (dia + timedelta(days=dias)).replace(hour=hora)
        agendar(yt, vid, alvo, f'SHORT · {slug} ({DOW[alvo.weekday()]})')

    try:
        import pipeline_state
        pipeline_state.mark_done(slug, 'scheduled', data={'longo_id': longo_id, 'date': ddmm})
    except Exception:
        pass
    # --- Sincronia YouTube -> Instagram (eco) -------------------------------
    # Agendar o longo é a ÚNICA ação necessária: ela também enfileira o eco do
    # Instagram (Reel-herói, +2h, janela <= 4h) e espelha a fila para a VPS, que
    # dispara no horário. Assim as duas plataformas ficam sempre sincronizadas.
    # Falha aqui NUNCA derruba o agendamento do YouTube (já concluído acima).
    try:
        import sincronizar
        print('--- sincronia Instagram (eco +2h) ---')
        sincronizar.enqueue(slug, ddmm=f'{dia.day:02d}/{dia.month:02d}',
                            hhmm=f'{dia.hour:02d}:{dia.minute:02d}',
                            youtube_id=longo_id)
    except SystemExit as e:
        print(f'  [sync IG] pulado (YouTube ok): {e}')
    except Exception as e:
        print(f'  [sync IG] FALHOU (YouTube ok): {str(e)[:140]}')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
