# -*- coding: utf-8 -*-
"""Camada HTTP isolada (Akita pilar 8 · Isolamento de execução).

Toda chamada externa passa por aqui, protegida pelo circuit_breaker + retry que JÁ
existem (circuit_breaker.py), com a distinção do Release It!:

- 5xx / 429 / timeout / conexão  -> TransientError -> retenta + conta no circuit
- 4xx (erro de cliente)          -> retorna {'ok': False, ...} SEM derrubar o circuit
- 2xx                            -> {'ok': True, 'status', 'data'}

Assim uma instabilidade real da API abre o circuit (para de martelar), mas um payload
inválido (4xx) não é retentado nem contamina a saúde da API.
"""
import json
import urllib.request
import urllib.error

from circuit_breaker import retry, circuit_breaker, CircuitOpenError  # noqa: F401 (reexport)


class TransientError(Exception):
    """Falha transitória (5xx/429/timeout/conexão) — vale retentar e contar no circuit."""


def _raw(url, data, headers, method, timeout):
    req = urllib.request.Request(url, data=data, headers=headers or {}, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            corpo = r.read().decode('utf-8', 'replace')
            try:
                payload = json.loads(corpo)
            except ValueError:
                payload = corpo
            return {'ok': True, 'status': getattr(r, 'status', 200), 'data': payload}
    except urllib.error.HTTPError as e:
        corpo = e.read().decode('utf-8', 'replace')[:500]
        if e.code == 429 or 500 <= e.code < 600:
            raise TransientError(f'HTTP {e.code}: {corpo}')
        return {'ok': False, 'status': e.code, 'erro': corpo}   # 4xx: não aciona o circuit
    except urllib.error.URLError as e:
        raise TransientError(f'conexao: {e.reason}')
    except TimeoutError as e:
        raise TransientError(f'timeout: {e}')


def request_json(url, data=None, headers=None, method='GET', api='generic',
                 timeout=60, max_attempts=3, base_s=2.0, threshold=4, timeout_s=300):
    """Chamada HTTP guardada por circuit_breaker + retry.

    Retorna dict {'ok': bool, 'status': int, 'data'|'erro': ...}.
    Levanta CircuitOpenError se o circuit da `api` estiver OPEN (use fallback no caller).
    Levanta TransientError se esgotar as tentativas numa falha transitória.
    """
    @retry(max_attempts=max_attempts, base_s=base_s)
    @circuit_breaker(api=api, threshold=threshold, timeout_s=timeout_s)
    def _attempt():
        return _raw(url, data, headers, method, timeout)

    return _attempt()
