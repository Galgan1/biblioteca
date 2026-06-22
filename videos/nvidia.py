# -*- coding: utf-8 -*-
"""Cliente NVIDIA NIM (build.nvidia.com) — geração de IMAGEM (Flux) + chat (LLM).

GRÁTIS (key `nvapi-`, sem cartão; ~1000 créditos, 40 req/min). Camada de geração
alinhada à soberania (rota free). Imagem usa o endpoint genai; chat é OpenAI-compatible.

  python nvidia.py face        # gera o rosto do avatar "O Narrador" (Flux) em _canal/
  python nvidia.py models      # lista modelos do endpoint de chat
NUNCA imprime a key.
"""
import sys
import json
import base64
import urllib.request
import urllib.error
from pathlib import Path

ROOT = Path(__file__).parent
KEY = (ROOT / '.secrets' / 'nvidia_key.txt').read_text(encoding='utf-8').strip()
GENAI = 'https://ai.api.nvidia.com/v1/genai'
CHAT = 'https://integrate.api.nvidia.com/v1'

try:                                   # resiliência: mesma fonte do falgen/imagen/veo
    from circuit_breaker import retry
except ImportError:                    # ambiente sem o módulo → no-op (não quebra import)
    def retry(**kw):
        return lambda f: f


class _TransitorioNIM(Exception):
    """Erro NIM retentável (5xx/429/408/timeout). Taxonomia: TRANSITÓRIO → @retry resolve.
    Origem: 22/jun/26 um 500 isolado matou um render de 5 min na cena 5 (gen sem retry)."""

# Persona-bible "O Narrador" (en — Flux é prompted em inglês). Ver AVATAR-MINUTO-REAL.md.
FACE_PROMPT = (
    "A photorealistic editorial portrait of a credible Brazilian man in his mid-forties, "
    "neutral-to-light-brown skin, short well-groomed dark hair with subtle gray at the temples, "
    "calm composed concentrated expression with a faint closed-mouth micro-smile, direct eye "
    "contact with the camera, subtle catchlight in the eyes, natural skin texture and pores; "
    "wearing a dark charcoal fine shirt, no tie; black background lit by a single warm amber-gold "
    "directional Rembrandt side light; premium cinematic editorial mood; head and shoulders bust "
    "shot; sharp focus on the eyes"
)


def _post(url, body):
    req = urllib.request.Request(
        url, data=json.dumps(body).encode(),
        headers={'Authorization': 'Bearer ' + KEY, 'Accept': 'application/json',
                 'Content-Type': 'application/json'})
    try:
        return json.load(urllib.request.urlopen(req, timeout=120))
    except urllib.error.HTTPError as e:
        if e.code in (408, 429) or e.code >= 500:        # TRANSITÓRIO → o @retry retenta
            raise _TransitorioNIM(f'NIM {e.code}') from e
        return {'_http_error': e.code, '_body': e.read().decode()[:700]}   # 4xx permanente: não retenta
    except urllib.error.URLError as e:                   # timeout/conexão = transitório
        raise _TransitorioNIM(f'rede: {e.reason}') from e


def _extract_b64(r):
    """Acha o base64 da imagem nos formatos possíveis da resposta NIM."""
    if r.get('artifacts'):
        a = r['artifacts'][0]
        return a.get('base64') or a.get('b64_json')
    if r.get('data') and isinstance(r['data'], list) and r['data']:
        return r['data'][0].get('b64_json') or r['data'][0].get('base64')
    return r.get('image') or r.get('b64_json')


@retry(max_attempts=3, base_s=2.0)       # 5xx/429/timeout retentados antes de desistir (build de 5 min não morre por 1 erro isolado)
def gen_image(prompt, out_png, model='black-forest-labs/flux.1-dev',
              width=1024, height=1024, steps=50, cfg=3.5, seed=0):
    r = _post(f'{GENAI}/{model}', {'prompt': prompt, 'mode': 'base', 'cfg_scale': cfg,
                                   'width': width, 'height': height, 'seed': seed, 'steps': steps})
    if '_http_error' in r:
        print('ERRO', r['_http_error'], '->', r['_body'])
        return None
    b64 = _extract_b64(r)
    if not b64:
        print('resposta inesperada:', json.dumps(r)[:500])
        return None
    out = Path(out_png)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(base64.b64decode(b64))
    print('OK ->', out, f'({out.stat().st_size // 1024} KB)')
    return str(out)


_DIMS = {'16:9': (1344, 768), '9:16': (768, 1344), '1:1': (1024, 1024)}


def _gen_safe(prompt, out_png, w, h):
    """gen_image já passou pelo @retry; se ainda assim levantar (NIM fora), vira None
    em vez de propagar — quem decide o aborte é o gerar_video (mantém o contrato)."""
    try:
        return gen_image(prompt, out_png, width=w, height=h)
    except Exception as e:
        print(f'  [nvidia] geração falhou após retries: {str(e)[:100]}')
        return None


def gen(prompt, out_png, aspect='16:9'):
    """Interface compatível com imagen.gen/falgen.gen (provider do gerar_video).
    Imagens GRÁTIS (NIM Flux). Fallback p/ 1024² se as dims do aspecto derem erro/500."""
    w, h = _DIMS.get(aspect, (1024, 1024))
    r = _gen_safe(prompt, out_png, w, h)
    if r is None and (w, h) != (1024, 1024):
        r = _gen_safe(prompt, out_png, 1024, 1024)
    return r


def face():
    gen_image(FACE_PROMPT, ROOT / '_canal' / 'avatar_narrador.png')


def models():
    req = urllib.request.Request(CHAT + '/models', headers={'Authorization': 'Bearer ' + KEY})
    d = json.load(urllib.request.urlopen(req, timeout=30))
    print('\n'.join(sorted(m.get('id', '') for m in d.get('data', []))))


if __name__ == '__main__':
    {'face': face, 'models': models}.get(sys.argv[1] if len(sys.argv) > 1 else 'face', face)()
