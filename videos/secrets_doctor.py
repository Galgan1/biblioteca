# -*- coding: utf-8 -*-
"""Doutor de APIs/segredos — responde "as APIs trabalham corretamente?" com EVIDÊNCIA.

Para cada chave em .secrets/: presente? autentica? capability/endpoint certo?
crédito/billing? Distingue o BLOQUEIO (a dor: não saber se é key, billing, crédito
ou endpoint). Faz só chamadas GRÁTIS de auth/status; presença p/ o que não dá checar barato.

Uso:  python secrets_doctor.py
"""
import json
import os
import sys
import tempfile
import urllib.error
import urllib.request
from pathlib import Path

SEC = Path(__file__).parent / '.secrets'

# Console Windows nasce cp1252 → o ✅/❌ estoura UnicodeEncodeError. Mesma cura do gate.
for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding='utf-8')
    except Exception:
        pass


def classify(code):
    """Taxonomia do bloqueio a partir do HTTP status — o coração da disciplina:
    saber SE é conta, crédito, endpoint ou transitório evita horas de caça errada."""
    if code in (401, 403):
        return 'CONTA/BILLING/KEY'          # auth/entitlement — NÃO é código
    if code == 402:
        return 'CRÉDITO'                    # sem saldo
    if code == 404:
        return 'ENDPOINT/MODELO'            # nome mudou / rota errada
    if code in (408, 429) or code >= 500:
        return 'TRANSITÓRIO'                # retry/breaker resolvem
    return f'HTTP {code}'


def _key(name):
    f = SEC / name
    return f.read_text(encoding='utf-8').strip() if f.exists() else None


def _auth_get(url, headers):
    """GET grátis de auth/status → ('✅', detalhe) ou ('❌', bloqueio classificado)."""
    try:
        urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=20)
        return '✅', 'autentica'
    except urllib.error.HTTPError as e:
        return '❌', classify(e.code)
    except Exception as e:
        return '❌', f'rede: {type(e).__name__}'


def check_nvidia():
    k = _key('nvidia_key.txt')
    if not k:
        return ('NVIDIA (Flux/LLM)', '⚠', 'key ausente')
    st, det = _auth_get('https://integrate.api.nvidia.com/v1/models', {'Authorization': 'Bearer ' + k})
    extra = ' — imagem(genai) é entitlement à parte' if st == '✅' else ''
    return ('NVIDIA (Flux/LLM)', st, det + extra)


def check_google_tts():
    k = _key('tts_api_key.txt')
    if not k:
        return ('Google TTS (Chirp)', '⚠', 'key ausente')
    st, det = _auth_get(f'https://texttospeech.googleapis.com/v1/voices?languageCode=pt-BR&key={k}', {})
    return ('Google TTS (Chirp)', st, det)


def check_fal():
    """fal: o teste real é o UPLOAD (era o 403 de billing)."""
    k = _key('fal_key.txt')
    if not k:
        return ('fal.ai (Wan/Kling/Flux)', '⚠', 'key ausente')
    os.environ['FAL_KEY'] = k
    try:
        import fal_client
        with tempfile.NamedTemporaryFile('w', suffix='.txt', delete=False) as f:
            f.write('ping')
            p = f.name
        fal_client.upload_file(p)
        return ('fal.ai (Wan/Kling/Flux)', '✅', 'auth+billing ok (upload aceito)')
    except Exception as e:
        s = str(e)
        bloqueio = 'CONTA/BILLING' if ('403' in s or 'Forbidden' in s) else type(e).__name__
        return ('fal.ai (Wan/Kling/Flux)', '❌', bloqueio)


def check_elevenlabs():
    """Narração principal. /v1/user é GET grátis que prova key+conta."""
    k = _key('elevenlabs_key.txt')
    if not k:
        return ('ElevenLabs (narração)', '⚠', 'key ausente')
    st, det = _auth_get('https://api.elevenlabs.io/v1/user', {'xi-api-key': k})
    return ('ElevenLabs (narração)', st, det)


def check_presenca(label, fname):
    return (label, '•', 'presente' if (SEC / fname).exists() else 'ausente')


# APIs vivas (auth/billing checados de graça) primeiro; presença para o resto.
PROVAS_VIVAS = (check_elevenlabs, check_fal, check_nvidia, check_google_tts)
PRESENCAS = (
    ('Imagen (Google)', 'imagen_api_key.txt'),
    ('Instagram token', 'instagram_token.txt'),
    ('Facebook token', 'facebook_page_token.txt'),
    ('TikTok token', 'tiktok_token.txt'),
    ('YouTube OAuth', 'token_v2.json'),
)


def main():
    linhas = [prova() for prova in PROVAS_VIVAS]
    linhas += [check_presenca(label, fname) for label, fname in PRESENCAS]
    print('\n=== Doutor de APIs — Minuto Real ===')
    print(f'  {"API":<26} {"":<3} detalhe')
    for nome, st, det in linhas:
        print(f'  {nome:<26} {st:<3} {det}')
    falhas = [n for n, st, _ in linhas if st == '❌']
    print(f'\n  bloqueadas: {falhas or "nenhuma"} '
          f'| legenda: ✅ ok · ❌ falha · ⚠ key ausente · • só presença')
    return 1 if falhas else 0


if __name__ == '__main__':
    sys.exit(main())
