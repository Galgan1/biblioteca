# -*- coding: utf-8 -*-
"""Cria o avatar do Minuto Real no HeyGen — Photo Avatar via prompt-to-avatar.

Persona: "O Narrador" (homem ~45, sóbrio, preto-e-ouro) — ver AVATAR-MINUTO-REAL.md.
Voz é EXTERNA (Iapetus/edge-tts) — o HeyGen não sintetiza voz aqui; o áudio do
pipeline entra na geração de vídeo. Camada PAGA/externa (premium, fora do core soberano).

Fluxo:
  python heygen_avatar.py status            # quota/créditos
  python heygen_avatar.py generate          # gera 4 rostos por prompt → salva URLs (1 crédito de imagem)
  python heygen_avatar.py group <image_key> # cria o grupo do rosto ESCOLHIDO e treina (humano escolhe antes)

Estado em _canal/heygen_avatar.json. NUNCA imprime a API key.
"""
import sys
import json
import time
import urllib.request
import urllib.error
from pathlib import Path

ROOT = Path(__file__).parent
KEY = (ROOT / '.secrets' / 'heygen_key.txt').read_text(encoding='utf-8').strip()
STATE = ROOT / '_canal' / 'heygen_avatar.json'
API = 'https://api.heygen.com'

# Prompt curado da persona-bible (en — o gerador é prompted em inglês).
APPEARANCE = (
    "A composed, credible Brazilian man in his mid-forties, neutral-to-light-brown skin, "
    "short well-groomed dark hair with subtle gray at the temples, calm concentrated expression "
    "with a faint closed-mouth micro-smile, direct eye contact with the camera, subtle catchlight "
    "in the eyes, natural skin texture; wearing a dark charcoal fine shirt, no tie; black background "
    "lit by a single warm amber-gold directional Rembrandt side light; editorial premium cinematic "
    "mood; mouth slightly open and relaxed; sharp focus on the eyes; photorealistic"
)


def _req(method, path, body=None):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(API + path, data=data, method=method,
                                 headers={'X-Api-Key': KEY, 'Content-Type': 'application/json'})
    try:
        return json.load(urllib.request.urlopen(req, timeout=60))
    except urllib.error.HTTPError as e:
        return {'_http_error': e.code, '_body': e.read().decode()[:700]}


def status():
    print(json.dumps(_req('GET', '/v2/user/remaining_quota'), indent=2)[:700])


def generate():
    body = {"name": "Narrador Minuto Real", "age": "Early Middle Age", "gender": "Man",
            "ethnicity": "Unspecified", "orientation": "vertical", "pose": "half_body",
            "style": "Realistic", "appearance": APPEARANCE}
    r = _req('POST', '/v2/photo_avatar/photo/generate', body)
    print('generate ->', json.dumps(r)[:700])
    gid = (r.get('data') or {}).get('generation_id')
    if not gid:
        return
    for _ in range(40):
        time.sleep(6)
        s = _req('GET', f'/v2/photo_avatar/generation/{gid}')
        st = (s.get('data') or {}).get('status') or s.get('_http_error')
        print('  status:', st)
        if st in ('success', 'completed', 'failed', 'error'):
            d = s.get('data', s)
            STATE.parent.mkdir(parents=True, exist_ok=True)
            STATE.write_text(json.dumps({'generation': d}, indent=2), encoding='utf-8')
            urls = d.get('image_url_list') or []
            keys = d.get('image_key_list') or []
            print(f'\n{len(urls)} rostos gerados:')
            for i, (u, k) in enumerate(zip(urls, keys)):
                print(f'  [{i}] key={k}\n      {u}')
            return
    print('timeout no polling')


def group(image_key):
    r = _req('POST', '/v2/photo_avatar/avatar_group/create',
             {"name": "Narrador Minuto Real", "image_key": image_key})
    print('group ->', json.dumps(r)[:700])
    gid = (r.get('data') or {}).get('id') or (r.get('data') or {}).get('group_id')
    if gid:
        print('train ->', json.dumps(_req('POST', '/v2/photo_avatar/train', {"group_id": gid}))[:400])
        st = json.loads(STATE.read_text(encoding='utf-8')) if STATE.exists() else {}
        st['group_id'] = gid
        st['chosen_image_key'] = image_key
        STATE.write_text(json.dumps(st, indent=2), encoding='utf-8')


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'status'
    {'status': status, 'generate': generate,
     'group': lambda: group(sys.argv[2])}.get(cmd, status)()
