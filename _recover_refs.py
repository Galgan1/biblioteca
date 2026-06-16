# -*- coding: utf-8 -*-
"""Recupera as imagens que o USUARIO enviou (coladas) no transcript da sessao,
para resgatar as referencias verdadeiras perdidas na compactacao de contexto.
So extrai blocos de imagem que sao itens DIRETOS de mensagens do usuario
(ignora tool_result = imagens que EU li). Ordem cronologica = ordem de envio."""
import json, base64
from pathlib import Path

SRC = Path(r"C:\Users\User\.claude\projects\C--Users-User--gemini-antigravity-scratch-biblioteca\62cba2fc-b80b-4caa-82c0-8214a618c903.jsonl")
OUT = Path(r"C:\Users\User\.gemini\antigravity\scratch\biblioteca\videos\_refs")
OUT.mkdir(parents=True, exist_ok=True)

n = 0
with SRC.open(encoding="utf-8") as f:
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
            src = blk.get("source") or {}
            data = src.get("data")
            if not data:
                continue
            mt = (src.get("media_type") or "image/png").split("/")[-1].replace("jpeg", "jpg")
            n += 1
            (OUT / f"ref_{n:02d}.{mt}").write_bytes(base64.b64decode(data))
            print(f"  ref_{n:02d}.{mt}  ({len(data)} b64 chars)")

print(f"\nTOTAL de imagens enviadas pelo usuario: {n}  -> {OUT}")
