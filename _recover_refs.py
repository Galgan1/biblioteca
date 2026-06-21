# -*- coding: utf-8 -*-
"""Recupera imagens grandes que o USUARIO colou nas sessoes principais mais
recentes (exclui subagents). Resgata as referencias verdadeiras de design."""
import json, base64
from pathlib import Path

PROJ = Path(r"C:\Users\User\.claude\projects\C--Users-User--gemini-antigravity-scratch-biblioteca")
OUT = Path(r"C:\Users\User\.gemini\antigravity\scratch\biblioteca\videos\_refs")
OUT.mkdir(parents=True, exist_ok=True)
MINLEN = 40000   # so imagens substanciais (referencias), nao icones

# sessoes principais = .jsonl direto na pasta do projeto (nao em /subagents/)
sessions = [p for p in PROJ.glob("*.jsonl") if p.is_file()]
sessions.sort(key=lambda p: p.stat().st_mtime, reverse=True)

total = 0
for sess in sessions[:8]:
    sid = sess.stem[:8]
    n = 0
    try:
        with sess.open(encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    ev = json.loads(line)
                except Exception:
                    continue
                if ev.get("type") != "user":
                    continue
                msg = ev.get("message") or {}
                if msg.get("role") != "user":
                    continue
                content = msg.get("content")
                if not isinstance(content, list):
                    continue
                for blk in content:
                    if not isinstance(blk, dict) or blk.get("type") != "image":
                        continue
                    data = (blk.get("source") or {}).get("data")
                    if not data or len(data) < MINLEN:
                        continue
                    mt = ((blk.get("source") or {}).get("media_type") or "image/png").split("/")[-1].replace("jpeg", "jpg")
                    n += 1
                    total += 1
                    d = OUT / sid
                    d.mkdir(exist_ok=True)
                    (d / f"u{n:02d}.{mt}").write_bytes(base64.b64decode(data))
    except Exception as e:
        print(f"  [erro {sid}: {e}]")
        continue
    import datetime
    mt_str = datetime.datetime.fromtimestamp(sess.stat().st_mtime).strftime("%d/%m %H:%M")
    if n:
        print(f"  {sid}  ({mt_str})  -> {n} imagem(ns) grande(s) do usuario")

print(f"\nTOTAL: {total} imagens -> {OUT}\\<sessao>\\")
