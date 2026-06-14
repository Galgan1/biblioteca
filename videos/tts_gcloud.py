# -*- coding: utf-8 -*-
"""Cliente do Google Cloud Text-to-Speech (vozes naturais Chirp3-HD / Studio).
Usa a API key restrita em .secrets/tts_api_key.txt. Stdlib only (urllib)."""

import sys, json, base64, urllib.request, urllib.error
from pathlib import Path

try:
    from circuit_breaker import circuit_breaker, retry, CircuitOpenError
except ImportError:

    def circuit_breaker(**kw):
        return lambda f: f

    def retry(**kw):
        return lambda f: f

    class CircuitOpenError(Exception):
        pass


KEY = (Path(__file__).parent / '.secrets' / 'tts_api_key.txt').read_text(encoding='utf-8').strip()
BASE = 'https://texttospeech.googleapis.com/v1'


def list_voices(lang='pt-BR'):
    url = f'{BASE}/voices?languageCode={lang}&key={KEY}'
    data = json.load(urllib.request.urlopen(url))
    return data.get('voices', [])


@retry(max_attempts=4, base_s=3.0)
@circuit_breaker(api='google_tts', threshold=3, timeout_s=300)
def synth(text, voice, out_mp3, rate=1.0, pitch=0.0, ssml=None):
    body = json.dumps(
        {
            'input': {'ssml': ssml} if ssml else {'text': text},
            'voice': {'languageCode': 'pt-BR', 'name': voice},
            'audioConfig': {'audioEncoding': 'MP3', 'speakingRate': rate, 'pitch': pitch},
        }
    ).encode('utf-8')
    req = urllib.request.Request(
        f'{BASE}/text:synthesize?key={KEY}', data=body, headers={'Content-Type': 'application/json'}
    )
    try:
        resp = json.load(urllib.request.urlopen(req, timeout=60))
        Path(out_mp3).write_bytes(base64.b64decode(resp['audioContent']))
        try:
            from cost_tracker import record_cost

            record_cost(api='google_tts_1k', units=len(ssml or text) / 1000)
        except Exception:
            pass
        return True
    except urllib.error.HTTPError as e:
        raise RuntimeError(f'{voice}: HTTP {e.code} {e.read().decode()[:200]}')
    except (urllib.error.URLError, ConnectionError, TimeoutError, OSError) as e:
        raise RuntimeError(f'{voice}: rede — {e}')


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'list'
    if cmd == 'list':
        vs = list_voices()
        for v in sorted(vs, key=lambda x: x['name']):
            n = v['name']
            if any(t in n for t in ('Chirp3-HD', 'Studio', 'Neural2')):
                print(f"  {n:32} {v['ssmlGender']}")
    elif cmd == 'synth':
        synth(sys.argv[3], sys.argv[2], sys.argv[4])
