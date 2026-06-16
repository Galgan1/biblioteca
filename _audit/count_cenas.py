# -*- coding: utf-8 -*-
"""Conta palavras por cena (mesma régua do check_krug: split() simples).
Uso: python _audit/count_cenas.py <arquivo.json> [<arquivo2.json> ...]
     python _audit/count_cenas.py            -> varre todos e lista só os >52
"""
import json, glob, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROT = os.path.join(ROOT, "videos", "roteiros")

def conta(fp, only_over=False):
    data = json.load(open(fp, encoding="utf-8"))
    base = os.path.basename(fp)
    over = 0
    for i, c in enumerate(data.get("cenas", [])):
        n = len((c.get("narracao") or "").split())
        flag = ">52" if n > 52 else "ok"
        if n > 52:
            over += 1
        if not only_over or n > 52:
            print(f"  {base}:cena[{i}] = {n} {flag}")
    return over

if __name__ == "__main__":
    args = sys.argv[1:]
    if args:
        tot = 0
        for a in args:
            fp = a if os.path.isabs(a) else os.path.join(ROT, a)
            tot += conta(fp)
        print(f"TOTAL >52: {tot}")
    else:
        tot = 0
        for fp in sorted(glob.glob(os.path.join(ROT, "*.json"))):
            tot += conta(fp, only_over=True)
        print(f"TOTAL >52: {tot}")
