# -*- coding: utf-8 -*-
"""Cliente do Google Cloud Text-to-Speech (vozes naturais Chirp3-HD / Studio).
Usa a API key restrita em .secrets/tts_api_key.txt. Stdlib only (urllib)."""
import sys, json, time, base64, urllib.request, urllib.error
from pathlib import Path

KEY = (Path(__file__).parent / '.secrets' / 'tts_api_key.txt').read_text(encoding='utf-8').strip()
BASE = 'https://texttospeech.googleapis.com/v1'


def list_voices(lang='pt-BR'):
    url = f'{BASE}/voices?languageCode={lang}&key={KEY}'
    data = json.load(urllib.request.urlopen(url))
    return data.get('voices', [])


def synth(text, voice, out_mp3, rate=1.0, pitch=0.0, ssml=None):
    body = json.dumps({
        'input': {'ssml': ssml} if ssml else {'text': text},
        'voice': {'languageCode': 'pt-BR', 'name': voice},
        'audioConfig': {'audioEncoding': 'MP3', 'speakingRate': rate, 'pitch': pitch},
    }).encode('utf-8')
    req = urllib.request.Request(f'{BASE}/text:synthesize?key={KEY}', data=body,
                                headers={'Content-Type': 'application/json'})
    # retry: quedas transitórias de conexão não podem matar um build longo
    for tent in range(4):
        try:
            resp = json.load(urllib.request.urlopen(req, timeout=60))
            Path(out_mp3).write_bytes(base64.b64decode(resp['audioContent']))
            return True
        except urllib.error.HTTPError as e:
            print(f"  ERRO {voice}: {e.read().decode()[:200]}")
            return False
        except (urllib.error.URLError, ConnectionError, TimeoutError, OSError) as e:
            if tent == 3:
                print(f"  ERRO {voice}: rede após 4 tentativas — {e}")
                return False
            time.sleep(2 ** tent * 3)  # 3s, 6s, 12s
    return False


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
