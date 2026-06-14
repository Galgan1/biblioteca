# -*- coding: utf-8 -*-
"""Consentimento UMA VEZ para o YouTube Analytics (token SEPARADO, nao toca no de upload).
Abre o navegador -> ESCOLHA O CANAL 'Minuto Real' (nao o pessoal).
Uso: python auth_analytics.py
"""
import sys
from pathlib import Path
try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass
from google_auth_oauthlib.flow import InstalledAppFlow

SEC = Path(__file__).parent / '.secrets'
# yt-analytics + youtube.readonly: o segundo (escopo de CANAL) forca o seletor de
# canal de marca no consentimento -> permite escolher "Minuto Real" e confirmar o nome.
SCOPES = ['https://www.googleapis.com/auth/yt-analytics.readonly',
          'https://www.googleapis.com/auth/youtube.readonly']

flow = InstalledAppFlow.from_client_secrets_file(str(SEC / 'client_secret.json'), SCOPES)
creds = flow.run_local_server(port=0, open_browser=False, prompt='consent',
                              authorization_prompt_message='AUTHURL::{url}')
(SEC / 'token_analytics.json').write_text(creds.to_json(), encoding='utf-8')
print('OK - token_analytics.json salvo (escopo yt-analytics.readonly)')
