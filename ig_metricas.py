# -*- coding: utf-8 -*-
"""Métricas de engajamento do Instagram para o canal Minuto Real.

CLI:
  python ig_metricas.py --relatorio         # top-3 e bottom-3 por score
  python ig_metricas.py --update            # consulta IG API e atualiza canal-state.json
  python ig_metricas.py --slug habitos      # detalhes de um livro específico
"""
import sys
import json
import argparse
import urllib.request
import urllib.error
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
STATE_FILE = ROOT / "canal-state.json"
SECRETS = ROOT / ".secrets"
GRAPH = "https://graph.facebook.com/v21.0"


# ---------------------------------------------------------------------------
# I/O do state
# ---------------------------------------------------------------------------

def _ler_state() -> dict:
    if not STATE_FILE.exists():
        return {"metricas": {}}
    return json.loads(STATE_FILE.read_text(encoding="utf-8"))


def _salvar_state(state: dict) -> None:
    STATE_FILE.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")


# ---------------------------------------------------------------------------
# Token IG
# ---------------------------------------------------------------------------

def _ler_token(state: dict) -> str | None:
    token = state.get("ig_token", "")
    if token:
        return token
    f = SECRETS / "ig_token.txt"
    if f.exists():
        return f.read_text(encoding="utf-8").strip()
    return None


# ---------------------------------------------------------------------------
# Chamada à Graph API
# ---------------------------------------------------------------------------

def _get(url: str) -> dict | None:
    try:
        with urllib.request.urlopen(url, timeout=15) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        print(f"  [erro] HTTP {e.code}: {e.read().decode(errors='replace')[:160]}")
    except Exception as e:
        print(f"  [erro] {e}")
    return None


def _buscar_medias(user_id: str, token: str) -> list[dict]:
    """Retorna publicações dos últimos 30 dias."""
    desde = (datetime.now(timezone.utc) - timedelta(days=30)).strftime("%Y-%m-%dT%H:%M:%S%z")
    url = (
        f"{GRAPH}/{user_id}/media"
        f"?fields=id,caption,timestamp"
        f"&since={desde}"
        f"&access_token={token}"
    )
    resp = _get(url)
    return (resp or {}).get("data", [])


def _buscar_insights(media_id: str, token: str) -> dict:
    url = (
        f"{GRAPH}/{media_id}/insights"
        f"?metric=impressions,reach,saved,shares"
        f"&access_token={token}"
    )
    resp = _get(url)
    if not resp:
        return {}
    return {item["name"]: item["values"][0]["value"] for item in resp.get("data", [])}


def _slug_da_caption(caption: str) -> str | None:
    """Extrai slug da legenda; retorna None se não detectar."""
    if not caption:
        return None
    primeira = caption.splitlines()[0].lower()
    return primeira.replace(" ", "-")[:50] if primeira else None


# ---------------------------------------------------------------------------
# Score
# ---------------------------------------------------------------------------

def calcular_score(m: dict) -> float:
    return m.get("views", 0) + m.get("saves", 0) * 10 + m.get("reach", 0) * 0.1


# ---------------------------------------------------------------------------
# Comandos
# ---------------------------------------------------------------------------

def cmd_update(state: dict) -> None:
    token = _ler_token(state)
    if not token:
        print("[aviso] token IG ausente — modo offline, nenhuma atualização feita.")
        return

    user_id = state.get("ig_user_id", "")
    f = SECRETS / "ig_user_id.txt"
    if not f.exists() and not user_id:
        print("[aviso] ig_user_id ausente — modo offline.")
        return
    if not user_id:
        user_id = f.read_text(encoding="utf-8").strip()

    medias = _buscar_medias(user_id, token)
    metricas = state.setdefault("metricas", {})
    for media in medias:
        slug = _slug_da_caption(media.get("caption", ""))
        if not slug:
            continue
        ins = _buscar_insights(media["id"], token)
        metricas[slug] = {
            "views": ins.get("impressions", 0),
            "saves": ins.get("saved", 0),
            "reach": ins.get("reach", 0),
            "share_rate": round(ins.get("shares", 0) / max(ins.get("impressions", 1), 1), 4),
            "updated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S"),
        }
        print(f"  ok {slug}")
    _salvar_state(state)
    print(f"[ok] {len(medias)} publicações processadas.")


def cmd_relatorio(state: dict) -> None:
    metricas = state.get("metricas", {})
    if not metricas:
        print("sem dados")
        return
    scored = sorted(metricas.items(), key=lambda kv: calcular_score(kv[1]), reverse=True)
    top = scored[:3]
    bottom = scored[-3:] if len(scored) > 3 else []

    def _linha(pos: int, slug: str, m: dict) -> str:
        sc = calcular_score(m)
        return f"  {pos}. {slug:<24} score={sc:.0f} views={m.get('views',0)} saves={m.get('saves',0)}"

    print("TOP-3:")
    for i, (slug, m) in enumerate(top, 1):
        print(_linha(i, slug, m))
    if bottom:
        print("BOTTOM-3:")
        for i, (slug, m) in enumerate(bottom, 1):
            print(_linha(i, slug, m))


def cmd_slug(state: dict, slug: str) -> None:
    metricas = state.get("metricas", {})
    m = metricas.get(slug)
    if not m:
        print(f"[!] slug '{slug}' não encontrado nas métricas.")
        return
    print(f"slug: {slug}")
    for k, v in m.items():
        print(f"  {k}: {v}")
    print(f"  score: {calcular_score(m):.1f}")


# ---------------------------------------------------------------------------
# Entrypoint
# ---------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Métricas IG — Minuto Real")
    p.add_argument("--relatorio", action="store_true")
    p.add_argument("--update", action="store_true")
    p.add_argument("--slug", metavar="SLUG")
    args = p.parse_args(argv)

    state = _ler_state()

    if args.update:
        cmd_update(state)
    elif args.relatorio:
        cmd_relatorio(state)
    elif args.slug:
        cmd_slug(state, args.slug)
    else:
        p.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
