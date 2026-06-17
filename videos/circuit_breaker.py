# -*- coding: utf-8 -*-
"""Circuit breaker + retry decorators para APIs externas do pipeline.

Estado do circuit (CLOSED/OPEN/HALF_OPEN) persistido em videos/canal-state.json
no campo "api_health".<api_name>.

Uso:
  from circuit_breaker import circuit_breaker, retry, CircuitOpenError

  @retry(max_attempts=3, base_s=2.0, jitter=True)
  @circuit_breaker(api='google_imagen', threshold=3, timeout_s=300)
  def gen_image(prompt, out_png):
      ...
"""
import json
import random
import time
import functools
from pathlib import Path

_STATE_FILE = Path(__file__).parent / 'canal-state.json'

_DEFAULTS = {'state': 'closed', 'failures': 0, 'opened_at': None, 'last_error': None}


class CircuitOpenError(Exception):
    """Sinaliza ao caller que o circuit está OPEN — usar fallback."""


# ---------------------------------------------------------------------------
# Persistência (leitura/escrita atômica simples com try/except para concorrência)
# ---------------------------------------------------------------------------

def _load_state() -> dict:
    try:
        data = json.loads(_STATE_FILE.read_text(encoding='utf-8'))
        return data.get('api_health', {})
    except Exception:
        return {}


def _save_state(api_health: dict) -> None:
    try:
        try:
            data = json.loads(_STATE_FILE.read_text(encoding='utf-8'))
        except Exception:
            data = {}
        data['api_health'] = api_health
        # Escrita atômica via arquivo temporário
        tmp = _STATE_FILE.with_suffix('.json.tmp')
        tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
        tmp.replace(_STATE_FILE)
    except Exception as e:
        print(f'[circuit_breaker] aviso: não salvou estado — {e}')


def _get_api(api: str) -> dict:
    health = _load_state()
    return health.get(api, dict(_DEFAULTS))


def _set_api(api: str, info: dict) -> None:
    health = _load_state()
    health[api] = info
    _save_state(health)


# ---------------------------------------------------------------------------
# API pública utilitária
# ---------------------------------------------------------------------------

def get_circuit_state(api: str) -> dict:
    """Retorna o estado atual do circuit para a API informada."""
    return _get_api(api)


def reset_circuit(api: str) -> None:
    """Força o circuit para CLOSED. Usar após resolver o problema manualmente."""
    _set_api(api, dict(_DEFAULTS))
    print(f'[circuit_breaker] {api}: reset para CLOSED')


def print_circuit_status() -> None:
    """Imprime o status de todos os circuits registrados em api_health."""
    health = _load_state()
    if not health:
        print('[circuit_breaker] Nenhum circuit registrado em api_health.')
        return
    print(f'{"API":<20} {"STATE":<10} {"FAILURES":<10} {"OPENED_AT":<22} LAST_ERROR')
    print('-' * 80)
    for api, info in health.items():
        opened = info.get('opened_at') or '-'
        err = (info.get('last_error') or '-')[:40]
        print(f'{api:<20} {info.get("state","?"):<10} {info.get("failures",0):<10} {str(opened):<22} {err}')


# ---------------------------------------------------------------------------
# Decorators
# ---------------------------------------------------------------------------

def circuit_breaker(api: str, threshold: int = 3, timeout_s: float = 300):
    """Decorator de circuit breaker.

    Args:
        api: chave em canal-state.json["api_health"]
        threshold: nº de falhas consecutivas para abrir o circuit
        timeout_s: segundos em OPEN antes de tentar HALF_OPEN
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            info = _get_api(api)
            state = info.get('state', 'closed')

            if state == 'open':
                opened_at = info.get('opened_at')
                if opened_at and (time.time() - opened_at) >= timeout_s:
                    # Timeout expirou — tenta HALF_OPEN
                    info['state'] = 'half_open'
                    _set_api(api, info)
                    state = 'half_open'
                else:
                    raise CircuitOpenError(f'Circuit OPEN for {api}')

            # Executa a função (state == 'closed' ou 'half_open')
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                # Falha
                info['failures'] = info.get('failures', 0) + 1
                info['last_error'] = str(e)[:200]
                if info['failures'] >= threshold or state == 'half_open':
                    info['state'] = 'open'
                    info['opened_at'] = time.time()
                    print(f'[circuit_breaker] {api}: ABERTO após {info["failures"]} falha(s)')
                _set_api(api, info)
                raise

            # Sucesso
            if state == 'half_open':
                print(f'[circuit_breaker] {api}: HALF_OPEN -> CLOSED (recuperado)')
            info.update({'state': 'closed', 'failures': 0, 'opened_at': None, 'last_error': None})
            _set_api(api, info)
            return result

        return wrapper
    return decorator


def retry(max_attempts: int = 3, base_s: float = 2.0, jitter: bool = True):
    """Decorator de retry com backoff exponencial.

    Args:
        max_attempts: número máximo de tentativas
        base_s: base do backoff em segundos (espera = base_s * 2^attempt)
        jitter: se True, adiciona ±50% de aleatoriedade à espera
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except CircuitOpenError:
                    raise  # Não retenta — re-raise imediato
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    wait = base_s * (2 ** attempt)
                    if jitter:
                        wait *= random.uniform(0.5, 1.5)
                    print(f'[retry] {func.__name__} tentativa {attempt + 1}/{max_attempts} '
                          f'falhou ({type(e).__name__}: {e}), aguardando {wait:.1f}s')
                    time.sleep(wait)
        return wrapper
    return decorator


if __name__ == '__main__':
    print_circuit_status()
