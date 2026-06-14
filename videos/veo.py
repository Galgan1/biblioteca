# -*- coding: utf-8 -*-
"""Cliente do Veo 3.1 (Gemini API) — anima uma imagem (image-to-video).
Usa a mesma API key do Imagen (.secrets/imagen_api_key.txt). Stdlib only.

Custo: variante fast ≈ US$0,15/s (8s ≈ US$1,20/clipe). Saída 1280x720 24fps.
"""

import sys, json, time, base64, urllib.request, urllib.error
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


KEY = (
    (Path(__file__).parent / '.secrets' / 'imagen_api_key.txt').read_text(encoding='utf-8').strip()
)
BASE = 'https://generativelanguage.googleapis.com/v1beta'
MODEL = 'veo-3.1-fast-generate-preview'


@circuit_breaker(api='google_veo', threshold=2, timeout_s=600)
def animate(img_path, prompt, out_mp4, duration=8, aspect='16:9'):
    """Anima img_path segundo o prompt de movimento. Retorna True se gerou."""
    b64 = base64.b64encode(Path(img_path).read_bytes()).decode()
    body = {
        'instances': [
            {
                'prompt': prompt,
                'image': {'bytesBase64Encoded': b64, 'mimeType': 'image/png'},
            }
        ],
        'parameters': {
            'aspectRatio': aspect,
            'durationSeconds': duration,
            'sampleCount': 1,
            'personGeneration': 'allow_adult',
        },
    }
    url = f'{BASE}/models/{MODEL}:predictLongRunning?key={KEY}'
    req = urllib.request.Request(
        url, data=json.dumps(body).encode('utf-8'), headers={'Content-Type': 'application/json'}
    )
    try:
        op = json.load(urllib.request.urlopen(req))
    except urllib.error.HTTPError as e:
        # Erros 4xx/5xx no start → falha real (circuit breaker conta)
        raise RuntimeError(f'Veo start: HTTP {e.code} {e.read().decode()[:300]}')

    poll = f"{BASE}/{op['name']}?key={KEY}"
    for _ in range(90):  # até 15 min
        time.sleep(10)
        try:
            st = json.load(urllib.request.urlopen(poll))
        except urllib.error.HTTPError as e:
            raise RuntimeError(f'Veo poll: HTTP {e.code} {e.read().decode()[:300]}')
        if st.get('done'):
            if 'error' in st:
                # Erro da operação (ex: prompt bloqueado) — não abre circuit
                print(f"  ERRO Veo: {json.dumps(st['error'])[:300]}")
                return False
            uri = _find_uri(st.get('response', {}))
            if not uri:
                print('  ERRO Veo: resposta sem URI de vídeo')
                return False
            dl = uri + (('&' if '?' in uri else '?') + f'key={KEY}')
            Path(out_mp4).write_bytes(urllib.request.urlopen(dl).read())
            try:
                from cost_tracker import record_cost

                record_cost(api='google_veo_8s', units=duration / 8)
            except Exception:
                pass
            return True
    print('  ERRO Veo: timeout')
    return False


def _find_uri(o):
    if isinstance(o, dict):
        for k, v in o.items():
            if k in ('uri', 'videoUri', 'fileUri') and isinstance(v, str):
                return v
            r = _find_uri(v)
            if r:
                return r
    elif isinstance(o, list):
        for it in o:
            r = _find_uri(it)
            if r:
                return r
    return None


if __name__ == '__main__':
    img, prompt = sys.argv[1], sys.argv[2]
    out = sys.argv[3] if len(sys.argv) > 3 else 'veo_out.mp4'
    print('OK ->', out) if animate(img, prompt, out) else print('falhou')
