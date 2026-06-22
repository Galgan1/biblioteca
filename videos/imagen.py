# -*- coding: utf-8 -*-
"""Cliente do Imagen (Google Gemini API) — gera imagens cinematográficas por prompt.
Usa a API key em .secrets/imagen_api_key.txt. Stdlib only."""
import sys, json, base64, urllib.request, urllib.error
from pathlib import Path

try:
    from circuit_breaker import circuit_breaker, retry, CircuitOpenError
    from cost_tracker import budget_guard
    _cb_available = True
except ImportError:
    _cb_available = False
    def circuit_breaker(**kw): return lambda f: f
    def retry(**kw): return lambda f: f
    def budget_guard(**kw): return lambda f: f

def _read_key():
    """Lê a chave COM guarda: ausente/ilegível -> '' em vez de derrubar o IMPORT do
    módulo inteiro (e, por tabela, todo pipeline que importe imagen). Sem chave, gen()
    aborta com mensagem e o caller cai p/ provider 'fal'/'local'."""
    try:
        return (Path(__file__).parent / '.secrets' / 'imagen_api_key.txt').read_text(encoding='utf-8').strip()
    except Exception:
        return ''


KEY = _read_key()
_REQ_TIMEOUT_S = 120   # request ao Imagen não pode pendurar a produção pra sempre
MODELS = ['imagen-4.0-generate-001', 'imagen-4.0-fast-generate-001']

# Tiers de qualidade (cada um cai p/ o de baixo se faltar): ultra = topo (mais caro),
# usado nas pecas premium; standard = padrao (Reels/video); fast = barato.
TIERS = {
    'fast': ['imagen-4.0-fast-generate-001'],
    'standard': MODELS,
    'ultra': ['imagen-4.0-ultra-generate-001', 'imagen-4.0-generate-001'],
}


@budget_guard(api='google_imagen')   # catraca de teto FORA do retry/breaker (abort != falha de API)
@retry(max_attempts=3, base_s=2.0)
@circuit_breaker(api='google_imagen', threshold=3, timeout_s=300)
def gen(prompt, out_png, aspect='16:9', tier='standard', size=None):
    if not KEY:
        print('ERRO imagen: sem chave em .secrets/imagen_api_key.txt -> use provider "fal" ou "local"')
        return None
    params = {'sampleCount': 1, 'aspectRatio': aspect}
    if size:
        params['sampleImageSize'] = size                 # '1K' | '2K' (Imagen 4 std/ultra)
    body = json.dumps({'instances': [{'prompt': prompt}], 'parameters': params}).encode('utf-8')
    last = ''
    for model in TIERS.get(tier, MODELS):
        url = f'https://generativelanguage.googleapis.com/v1beta/models/{model}:predict?key={KEY}'
        req = urllib.request.Request(url, data=body, headers={'Content-Type': 'application/json'})
        try:
            resp = json.load(urllib.request.urlopen(req, timeout=_REQ_TIMEOUT_S))
        except urllib.error.HTTPError as e:
            last = f'{model}: {e.code} {e.read().decode()[:300]}'
            continue
        preds = resp.get('predictions', [])
        if preds and preds[0].get('bytesBase64Encoded'):
            Path(out_png).write_bytes(base64.b64decode(preds[0]['bytesBase64Encoded']))
            try:
                from cost_tracker import record_cost
                record_cost(api='google_imagen')
            except Exception:
                pass
            return model
        last = f'{model}: sem imagem — {json.dumps(resp)[:200]}'
    print('ERRO:', last)
    return None


if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else 'test.png'
    prompt = sys.argv[2] if len(sys.argv) > 2 else 'cinematic dark atmospheric scene'
    m = gen(prompt, out)
    print(f'OK ({m}) -> {out}' if m else 'falhou')
