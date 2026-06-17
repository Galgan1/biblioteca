# -*- coding: utf-8 -*-
"""Doctor - loop de auditoria de SAUDE do pipeline (Akita pilar 7).

Agrega os sinais que JA existem (circuit_breaker em canal-state.json, estados em
pipeline/state/, segredos em .secrets/) num unico health-check, pensado para rodar
AUTOMATICAMENTE (agendador/cron) sem intervencao. Read-only: nao muta nada nem
imprime o conteudo de segredos (so os nomes).

Exit code: 0 = saudavel; 1 = FALHA (algum circuit OPEN).
Avisos (nao derrubam o exit): circuit HALF_OPEN, stages bloqueados, segredos ausentes.

Uso:  python doctor.py
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent
CANAL_STATE = ROOT / 'canal-state.json'
STATE_DIR = ROOT.parent / 'pipeline' / 'state'
SECRETS_DIR = ROOT / '.secrets'

SECRETS_ESPERADOS = {
    'facebook_page_token.txt', 'facebook_page_id.txt',
    'instagram_token.txt', 'instagram_user_id.txt',
    'tiktok_token.txt', 'tts_api_key.txt', 'imagen_api_key.txt',
}


# --------------------------------------------------------------------------
# Funcoes puras (testaveis sem tocar disco)
# --------------------------------------------------------------------------

def checar_circuits(api_health):
    """-> (falhas, avisos). OPEN = falha; HALF_OPEN = aviso."""
    falhas, avisos = [], []
    for api, info in (api_health or {}).items():
        st = (info or {}).get('state', 'closed')
        if st == 'open':
            falhas.append(f"circuit OPEN: {api} ({(info or {}).get('failures', 0)} falhas)")
        elif st == 'half_open':
            avisos.append(f"circuit HALF_OPEN: {api}")
    return falhas, avisos


def checar_blocked(estados):
    """estados: {slug: {stage: entry}} -> avisos de stages bloqueados (atencao, nao falha)."""
    avisos = []
    for slug, st in (estados or {}).items():
        for stage, entry in (st or {}).items():
            if isinstance(entry, dict) and entry.get('status') == 'blocked':
                avisos.append(f"bloqueado: {slug}/{stage} - {entry.get('reason', '?')}")
    return avisos


def checar_secrets(presentes, esperados):
    """-> avisos de segredos esperados ausentes (SO os nomes, nunca o conteudo)."""
    return [f"secret ausente: {s}" for s in sorted(set(esperados) - set(presentes))]


def exit_code(falhas):
    return 1 if falhas else 0


# --------------------------------------------------------------------------
# Wrapper que le o estado real (nunca lanca)
# --------------------------------------------------------------------------

def _load_json(p):
    try:
        return json.loads(Path(p).read_text(encoding='utf-8'))
    except Exception:
        return {}


def coletar():
    """Le o estado real e devolve (falhas, avisos)."""
    falhas, avisos = [], []

    api_health = _load_json(CANAL_STATE).get('api_health', {})
    f, a = checar_circuits(api_health)
    falhas += f
    avisos += a

    estados = {}
    if STATE_DIR.exists():
        for p in STATE_DIR.glob('*.json'):
            estados[p.stem] = _load_json(p)
    avisos += checar_blocked(estados)

    presentes = {p.name for p in SECRETS_DIR.glob('*.txt')} if SECRETS_DIR.exists() else set()
    avisos += checar_secrets(presentes, SECRETS_ESPERADOS)

    return falhas, avisos


def main():
    falhas, avisos = coletar()
    print('=== doctor - auditoria de saude do pipeline ===')
    print(f'FALHAS ({len(falhas)}):' if falhas else 'FALHAS: nenhuma')
    for x in falhas:
        print('  [FALHA]', x)
    if avisos:
        print(f'AVISOS ({len(avisos)}):')
        for x in avisos:
            print('  [aviso]', x)
    code = exit_code(falhas)
    print(f"\nSTATUS: {'OK' if code == 0 else 'PROBLEMAS'} (exit {code})")
    return code


if __name__ == '__main__':
    sys.exit(main())
