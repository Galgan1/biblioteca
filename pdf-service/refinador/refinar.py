# -*- coding: utf-8 -*-
"""
refinar.py — O LAÇO. Gera → mede o "patus" → ajusta → regera, até passar do alvo
ou estagnar; e na exceção aciona a rota de fuga (Claude). Grava a melhor config
por (livro, página exata) em tuned.json, que o motor lê em produção.

Uso:
  python refinar.py <livro> [pagina ...]      # páginas explícitas
  python refinar.py <livro>                    # descobre visão-geral + capítulos
  python refinar.py <livro> --budget 10        # limita nº de renders por página

Tudo local e offline. Não publica nada.
"""

import json
import os
import re
import sys

import claude_cli
import engine
import metricas

DEFAULT = {"maxFs": 15.5, "fillTarget": 0.94, "rhythmCap": 1.9, "padCap": 1.4, "marginMul": 1.0}
GRID = {
    "fillTarget": [0.90, 0.94, 0.97],
    "maxFs": [14.0, 15.5, 17.0],
    "rhythmCap": [1.6, 1.9, 2.3],
    "marginMul": [0.85, 1.0, 1.25],
}
THRESHOLD = 0.85


def discover_pages(book):
    """visão-geral + capítulos, na ordem dos links da página do livro."""
    over = os.path.join(engine.SITE_ROOT, f"{book}.html")
    pages = ["visao-geral"]
    try:
        with open(over, "r", encoding="utf-8") as f:
            html = f.read()
        for href in re.findall(r'href="([^"]+\.html)"[^>]*class="chapter-link"', html):
            if href.startswith(f"{book}/"):
                pages.append(os.path.basename(href)[:-5])  # tira ".html"
    except FileNotFoundError:
        pass
    return pages


def evaluate(book, page, tune):
    pdf, _diag = engine.render(book, page, tune)
    return metricas.score_pdf(pdf, expect_pages=1), pdf


def refine_page(book, page, budget=16, log=print):
    best = dict(DEFAULT)
    sc, _ = evaluate(book, page, best)
    best_patus, best_sc = sc["patus"], sc
    used = 1
    log(f"  base   {metricas.compact(sc)}")

    improved = True
    while improved and used < budget:
        improved = False
        for knob, vals in GRID.items():
            for v in vals:
                if used >= budget:
                    break
                if best.get(knob) == v:
                    continue
                cand = dict(best)
                cand[knob] = v
                sc, _ = evaluate(book, page, cand)
                used += 1
                if sc["patus"] > best_patus + 0.004:
                    best, best_patus, best_sc = cand, sc["patus"], sc
                    improved = True
                    log(f"  +{knob}={v:<5} {metricas.compact(sc)}")

    if best_patus < THRESHOLD and claude_cli.available():
        log(f"  alvo não atingido ({best_patus}) — rota de fuga (Claude)…")
        sug, diag = claude_cli.suggest_tune(book, page, best_sc, best)
        if sug:
            cand = {**best, **sug}
            sc, _ = evaluate(book, page, cand)
            used += 1
            adot = sc["patus"] > best_patus
            log(
                f"  Claude {sug} → {metricas.compact(sc)} "
                f"[{'adotado' if adot else 'descartado'}] «{diag[:70]}»"
            )
            if adot:
                best, best_patus, best_sc = cand, sc["patus"], sc
        else:
            log(f"  rota de fuga sem sugestão útil ({diag})")

    return best, best_patus, used


def diff_from_default(t):
    return {k: v for k, v in t.items() if DEFAULT.get(k) != v}


def save_tune(book, page, tune):
    try:
        with open(engine.TUNED_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}
    data.setdefault(book, {})[page] = tune
    with open(engine.TUNED_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def all_books():
    """Livros com páginas de capítulo (têm diretório próprio no site)."""
    try:
        with open(os.path.join(engine.SITE_ROOT, "books.json"), "r", encoding="utf-8") as f:
            ids = [b["id"] for b in json.load(f)]
    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        ids = []
    return [i for i in ids if os.path.isdir(os.path.join(engine.SITE_ROOT, i))]


def main():
    args = sys.argv[1:]
    budget = 16
    if "--budget" in args:
        i = args.index("--budget")
        budget = int(args[i + 1])
        del args[i : i + 2]
    fleet = "--all" in args
    if fleet:
        args = [a for a in args if a != "--all"]
    if not args and not fleet:
        print(
            "uso: python refinar.py <livro> [pagina ...] [--budget N]\n"
            "     python refinar.py --all            # catálogo inteiro"
        )
        sys.exit(2)

    if fleet:
        jobs = [(b, discover_pages(b)) for b in all_books()]
    else:
        book = args[0]
        jobs = [(book, [p for p in args[1:] if p != "livro-completo"] or discover_pages(book))]

    total = sum(len(p) for _, p in jobs)
    print(f"refinador · {len(jobs)} livro(s) · {total} página(s) · budget {budget}/página")
    engine.ensure_service()
    results = []
    try:
        for book, pages in jobs:
            for pg in pages:
                print(f"\n■ {book}/{pg}")
                best, patus, used = refine_page(book, pg, budget=budget)
                tune = diff_from_default(best)
                if tune:
                    save_tune(book, pg, tune)
                results.append((book, pg, patus, used, tune))
        engine.reload_tuned()
    finally:
        engine.stop_service()

    results.sort(key=lambda r: r[2])  # piores primeiro
    print("\n── resumo (piores no topo) ─────────────────────────────")
    for book, pg, patus, used, tune in results:
        flag = "✓" if patus >= THRESHOLD else "·"
        print(f" {flag} {patus:.3f}  {book}/{pg:30s} {used:>2}r  {tune or '(default)'}")
    abaixo = [r for r in results if r[2] < THRESHOLD]
    print(f"\n{len(results)} páginas · {len(abaixo)} abaixo do alvo ({THRESHOLD})")
    if abaixo:
        print(
            "→ candidatas a patch estrutural: python propor_patch.py "
            + " ".join(f"{b}/{p}" for b, p, *_ in abaixo[:8])
        )
    print(f"tuned.json em {engine.TUNED_PATH}")


if __name__ == "__main__":
    main()
