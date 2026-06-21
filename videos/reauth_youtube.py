# -*- coding: utf-8 -*-
"""Re-autoriza SÓ o acesso ao YouTube (salva .secrets/token_v2.json) — NÃO faz upload.

Rode UMA vez no seu terminal:
    cd C:\\Users\\User\\.gemini\\antigravity\\scratch\\biblioteca\\videos
    python reauth_youtube.py

Vai abrir o navegador p/ você logar no Google e ESCOLHER o canal **Minuto Real**
(@MinutoReal1701) — NÃO o André Galgani pessoal. Ao terminar ele CONFERE o canal
e avisa na hora se você escolheu o errado.
"""
import time
from googleapiclient.discovery import build
import upload_youtube
import canal_guard

if __name__ == '__main__':
    # Força novo consentimento: guarda o token atual p/ o navegador reabrir e você poder
    # ESCOLHER o canal certo. Sem isso, get_creds só daria refresh no canal errado.
    tok = upload_youtube.TOKEN
    if tok.exists():
        bak = tok.with_name(f'token_v2.{int(time.time())}.bak.json')
        tok.rename(bak)
        print(f"(token anterior guardado em {bak.name})")
    creds = upload_youtube.get_creds()   # abre o navegador (run_local_server) e salva token_v2.json novo
    yt = build('youtube', 'v3', credentials=creds)
    try:
        ch = canal_guard.assert_canal(yt)
        print(f"\nOK ✓ Autorizado no canal CERTO: {ch['snippet']['title']} ({ch['id']}). Avise: 'autorizado'.")
    except canal_guard.CanalErrado as e:
        print(f"\n✗ {e}\n→ Rode 'python reauth_youtube.py' DE NOVO e selecione o canal {canal_guard.CANAL_HANDLE} (Minuto Real).")
