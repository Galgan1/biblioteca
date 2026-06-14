# -*- coding: utf-8 -*-
"""Cliente do Imagen (Google Gemini API) — gera imagens cinematográficas por prompt.
Usa a API key em .secrets/imagen_api_key.txt. Stdlib only."""
import sys, json, base64, urllib.request, urllib.error
from pathlib import Path

KEY = (Path(__file__).parent / '.secrets' / 'imagen_api_key.txt').read_text(encoding='utf-8').strip()
MODELS = ['imagen-4.0-generate-001', 'imagen-4.0-fast-generate-001']


def gen(prompt, out_png, aspect='16:9'):
    body = json.dumps({
        'instances': [{'prompt': prompt}],
        'parameters': {'sampleCount': 1, 'aspectRatio': aspect},
    }).encode('utf-8')
    last = ''
    for model in MODELS:
        url = f'https://generativelanguage.googleapis.com/v1beta/models/{model}:predict?key={KEY}'
        req = urllib.request.Request(url, data=body, headers={'Content-Type': 'application/json'})
        try:
            resp = json.load(urllib.request.urlopen(req))
        except urllib.error.HTTPError as e:
            last = f'{model}: {e.code} {e.read().decode()[:300]}'
            continue
        preds = resp.get('predictions', [])
        if preds and preds[0].get('bytesBase64Encoded'):
            Path(out_png).write_bytes(base64.b64decode(preds[0]['bytesBase64Encoded']))
            return model
        last = f'{model}: sem imagem — {json.dumps(resp)[:200]}'
    print('ERRO:', last)
    return None


if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else 'test.png'
    prompt = sys.argv[2] if len(sys.argv) > 2 else 'cinematic dark atmospheric scene'
    m = gen(prompt, out)
    print(f'OK ({m}) -> {out}' if m else 'falhou')
