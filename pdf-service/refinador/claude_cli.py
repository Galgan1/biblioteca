# -*- coding: utf-8 -*-
"""
claude_cli.py — ROTA DE FUGA. Só é acionada quando o laço determinístico
empaca abaixo do alvo (a exceção, fiel ao Modo Soberano).

Manda as MÉTRICAS + o tune atual para o `claude` (CLI) e recebe de volta um tune
sugerido (JSON). Texto puro — sem visão, sem ferramentas, sem prompt interativo:
o prompt vai pelo stdin para não esbarrar em aspas/acentos no Windows.
"""

import json
import re
import shutil
import subprocess

# Botões que o refinador conhece, com faixa segura (o que vier fora é grampeado).
KNOBS = {
    "maxFs": (12.0, 18.0),  # teto da fonte (↑ enche mais com pouco texto)
    "fillTarget": (0.85, 0.98),  # alvo de altura preenchida antes do ritmo
    "rhythmCap": (1.2, 2.6),  # teto do "ar" entre cards (↑ espalha conteúdo curto)
    "padCap": (1.0, 1.8),  # teto do padding interno dos cards
    "marginMul": (0.6, 1.6),  # multiplicador da margem entre cards
}

_SCHEMA = "\n".join(f"  - {k}: faixa [{lo}, {hi}]" for k, (lo, hi) in KNOBS.items())


def available():
    return shutil.which("claude") is not None


def ask(prompt, timeout=300):
    """Chamada crua ao `claude -p` (prompt pelo stdin). Devolve o texto ou None."""
    if not available():
        return None
    try:
        out = subprocess.run(
            "claude -p",
            input=prompt,
            capture_output=True,
            text=True,
            shell=True,
            encoding="utf-8",
            errors="replace",
            timeout=timeout,
        )
    except Exception:  # noqa: BLE001
        return None
    return (out.stdout or "").strip() or None


def _clamptune(t):
    out = {}
    for k, v in (t or {}).items():
        if k in KNOBS:
            lo, hi = KNOBS[k]
            try:
                out[k] = max(lo, min(hi, float(v)))
            except (TypeError, ValueError):
                pass
    return out


def suggest_tune(book, page, metrics, current_tune, timeout=180):
    """Devolve (tune_sugerido | None, diagnostico_str)."""
    if not available():
        return None, "claude CLI indisponível"

    prompt = f"""Você é o ajustador de um motor que gera PDFs A4 "cheat sheet" (resumos de \
livros, estética verde, cards). Meta: cada página deve dar "patus" — sensação de \
página CHEIA até o pé, margens limpas, densidade confortável (nem deserto, nem \
amontoado), idealmente 1 página.

Um laço determinístico já tentou e estacionou. Aqui está o melhor resultado:

Livro/página: {book}/{page}
Métricas (0..1, maior = melhor onde aplicável):
{json.dumps(metrics, ensure_ascii=False, indent=2)}

Leitura: coverage<0.85 = página termina cedo (vazio embaixo); density<0.05 = rala; \
density>0.16 = amontoada; edge_ink>0.02 = conteúdo encostando na borda; gap_frac alto \
= buraco no meio; pages>1 quando devia ser 1 = transbordou.

Tune atual:
{json.dumps(current_tune, ensure_ascii=False)}

Botões disponíveis (só estes; respeite as faixas):
{_SCHEMA}

Responda SOMENTE com um objeto JSON, sem texto fora dele, no formato:
{{"diagnostico": "<1 frase>", "tune": {{<apenas os botões a mudar>}}}}"""

    try:
        out = subprocess.run(
            "claude -p",
            input=prompt,
            capture_output=True,
            text=True,
            shell=True,
            encoding="utf-8",
            errors="replace",
            timeout=timeout,
        )
    except Exception as e:  # noqa: BLE001
        return None, f"falha ao chamar claude: {e}"

    txt = (out.stdout or "").strip()
    m = re.search(r"\{.*\}", txt, re.S)
    if not m:
        return None, f"sem JSON na resposta ({txt[:80]!r})"
    try:
        data = json.loads(m.group(0))
    except json.JSONDecodeError:
        return None, "JSON inválido na resposta"
    return _clamptune(data.get("tune")), str(data.get("diagnostico", "")).strip()
