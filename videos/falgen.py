# -*- coding: utf-8 -*-
"""Cliente fal.ai — imagem (Flux) + movimento (Kling 3.0 image-to-video).
Substitui Google Imagen/Veo com UMA chave, faturamento separado do Google.

Pré-requisito (uma vez, feito pelo Showrunner):
  1. Criar conta em https://fal.ai e adicionar forma de pagamento (billing).
  2. Copiar a API key (Dashboard → Keys) para  .secrets/fal_key.txt
  3. pip install fal-client   (já instalado neste ambiente)

Mantém a MESMA assinatura de imagen.gen() e veo.animate(), então o pipeline
só troca o provedor — nada mais muda.
"""
import os, sys, urllib.request
from pathlib import Path

try:
    from circuit_breaker import circuit_breaker, retry, CircuitOpenError
except ImportError:
    def circuit_breaker(**kw): return lambda f: f
    def retry(**kw): return lambda f: f
    class CircuitOpenError(Exception): pass

_KEY = Path(__file__).parent / '.secrets' / 'fal_key.txt'
if _KEY.exists():
    os.environ['FAL_KEY'] = _KEY.read_text(encoding='utf-8').strip()

import fal_client

try:
    from cost_tracker import record_cost as _record_cost
except ImportError:
    def _record_cost(**kw): pass  # fallback silencioso

# Modelos (verificáveis em https://fal.ai/models). Configuráveis por env.
IMG_MODEL = os.environ.get('FAL_IMG_MODEL', 'fal-ai/flux-2/pro')
VID_MODEL = os.environ.get('FAL_VID_MODEL', 'fal-ai/kling-video/v3/pro/image-to-video')


_DL_TIMEOUT_S = 120   # download não pode pendurar a produção pra sempre (retry/breaker não pegam hang)


def _download(url, out_path):
    """Baixa url -> out_path. Timeout DURO (pilar 7: um hang sem timeout nunca vira
    falha retentável — só o timeout o transforma em erro que o @retry trata) +
    anti-fantasma: bytes vazios levantam, em vez de gravar um arquivo-fantasma."""
    dados = urllib.request.urlopen(url, timeout=_DL_TIMEOUT_S).read()
    if not dados:
        raise ValueError(f'download vazio de {str(url)[:80]}')
    Path(out_path).write_bytes(dados)


@retry(max_attempts=3, base_s=2.0)
@circuit_breaker(api='fal-flux', threshold=3, timeout_s=300)
def gen(prompt, out_png, aspect='16:9'):
    """Gera imagem (Flux). Mesma assinatura de imagen.gen(). Retorna model id ou None."""
    res = fal_client.subscribe(IMG_MODEL, arguments={
        'prompt': prompt,
        'image_size': 'landscape_16_9',
        'num_images': 1,
    }, with_logs=False)
    imgs = res.get('images') or res.get('image') or []
    if isinstance(imgs, dict):
        imgs = [imgs]
    if not imgs or not imgs[0].get('url'):
        print(f'  ERRO fal imagem: resposta inesperada — {str(res)[:200]}')
        return None
    _download(imgs[0]['url'], out_png)
    try:
        _record_cost(api='fal-flux')
    except Exception:
        pass
    return IMG_MODEL


@retry(max_attempts=2, base_s=3.0)
@circuit_breaker(api='fal-kling', threshold=2, timeout_s=600)
def animate(img_path, prompt, out_mp4, duration=5):
    """Anima img_path (Kling i2v). Mesma assinatura de veo.animate(). Retorna True/False."""
    img_url = fal_client.upload_file(str(img_path))
    res = fal_client.subscribe(VID_MODEL, arguments={
        'prompt': prompt,
        'image_url': img_url,
        'duration': str(duration),
        'aspect_ratio': '16:9',
    }, with_logs=False)
    vid = res.get('video') or {}
    url = vid.get('url') if isinstance(vid, dict) else None
    if not url:
        print(f'  ERRO fal vídeo: resposta inesperada — {str(res)[:200]}')
        return False
    _download(url, out_mp4)
    try:
        _record_cost(api='fal-kling')
    except Exception:
        pass
    return True


AVATAR_MODEL = os.environ.get('FAL_AVATAR_MODEL', 'fal-ai/kling-video/ai-avatar/v2/pro')


@retry(max_attempts=2, base_s=3.0)
@circuit_breaker(api='fal-avatar', threshold=2, timeout_s=900)
def lip_sync(img_path, audio_path, out_mp4,
             prompt='a calm composed man narrating to camera, subtle natural head motion, serious editorial'):
    """Cabeça FALANTE (Kling AI Avatar): foto + áudio → vídeo com lip-sync.
    PAGO: ~$0.115/segundo de saída. Retorna True/False."""
    img_url = fal_client.upload_file(str(img_path))
    aud_url = fal_client.upload_file(str(audio_path))
    res = fal_client.subscribe(AVATAR_MODEL, arguments={
        'image_url': img_url, 'audio_url': aud_url, 'prompt': prompt,
    }, with_logs=False)
    vid = res.get('video') or {}
    url = vid.get('url') if isinstance(vid, dict) else None
    if not url:
        print(f'  ERRO fal avatar: resposta inesperada — {str(res)[:200]}')
        return False
    _download(url, out_mp4)
    try:
        _record_cost(api='fal-avatar')
    except Exception:
        pass
    return True


if __name__ == '__main__':
    # Smoke test:  python falgen.py img   |   python falgen.py vid <img.png>
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'img'
    if cmd == 'img':
        m = gen('a vast dark cinema with a projector beam through haze, '
                'cinematic atmospheric digital painting', '_img/_falcheck.png')
        print('OK img ->', m if m else 'FALHOU')
    elif cmd == 'vid':
        ok = animate(sys.argv[2], 'slow cinematic push-in, drifting haze, gentle light flicker',
                     '_motion/_falcheck.mp4')
        print('OK vid' if ok else 'FALHOU vid')
