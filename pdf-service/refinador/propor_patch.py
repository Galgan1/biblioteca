# -*- coding: utf-8 -*-
"""
propor_patch.py — AUTO-IMPLEMENTAÇÃO (camada estrutural, COM PORTÃO).

Quando o ajuste de parâmetros (refinar.py) NÃO resolve — o problema é do CSS de
impressão ou do motor, não de um botão — esta etapa pede ao Claude um PATCH real
e o salva em refinador/propostas/ para revisão. Ela é autônoma até aqui; aplicar
e publicar continua sendo decisão humana (regra de produção).

NÃO aplica diff. NÃO faz deploy. NÃO toca em produção.

Uso:  python propor_patch.py <livro>/<pagina> [<livro>/<pagina> ...]
"""
import datetime
import os
import re
import sys

import claude_cli
import engine
import fitz  # PyMuPDF
import metricas

PROP_DIR = os.path.join(engine.HERE, "propostas")
SERVER_JS = os.path.join(engine.SVC, "server.js")


def _extract_print_css():
    try:
        with open(SERVER_JS, "r", encoding="utf-8") as f:
            src = f.read()
    except FileNotFoundError:
        return ""
    m = re.search(r"const PRINT_CSS = `([\s\S]*?)`;", src)
    return m.group(1).strip() if m else ""


def _png(pdf_bytes, path):
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    pix = doc[0].get_pixmap(matrix=fitz.Matrix(110 / 72, 110 / 72))
    pix.save(path)


def main():
    specs = [s for s in sys.argv[1:] if "/" in s]
    if not specs:
        print("uso: python propor_patch.py <livro>/<pagina> ..."); sys.exit(2)
    if not claude_cli.available():
        print("claude CLI indisponível — esta etapa precisa da rota de fuga."); sys.exit(1)

    ts = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    outdir = os.path.join(PROP_DIR, ts)
    os.makedirs(outdir, exist_ok=True)

    engine.ensure_service()
    casos = []
    try:
        for spec in specs:
            book, page = spec.split("/", 1)
            pdf, _ = engine.render(book, page, None)
            sc = metricas.score_pdf(pdf, expect_pages=1)
            png = os.path.join(outdir, f"{book}__{page}.png")
            _png(pdf, png)
            casos.append((spec, sc))
            print(f"  {spec:40s} {metricas.compact(sc)}  → {os.path.basename(png)}")
    finally:
        engine.stop_service()

    print_css = _extract_print_css()
    casos_txt = "\n".join(
        f"- {spec}: {metricas.compact(sc)}" for spec, sc in casos)
    prompt = f"""Você é engenheiro do motor de PDF da Biblioteca (cheat sheets verdes, A4).
Estas páginas continuam abaixo do alvo de "patus" MESMO após o ajuste automático de
parâmetros (maxFs, fillTarget, rhythmCap, padCap, marginMul). Logo, o gargalo é
ESTRUTURAL: o CSS de impressão (PRINT_CSS) ou o motor — não um botão tunável.

Casos (PNG de cada um foi salvo para conferência):
{casos_txt}

Leitura das métricas: coverage<0.85 = termina cedo; density>0.16 = amontoado;
edge_ink>0.02 = encostando na borda; gap_frac alto = buraco no meio; pages>1 = transbordou.

PRINT_CSS atual (injetado na impressão):
```css
{print_css}
```

Proponha UMA mudança cirúrgica e segura (estética "cheat sheet verde" preservada).
Responda em Markdown com EXATAMENTE estas seções:
## Diagnóstico
(1–3 frases sobre a causa estrutural comum)
## Patch proposto
(um diff unificado mínimo contra pdf-service/server.js — ou um bloco CSS novo claramente delimitado)
## Risco e teste
(o que pode quebrar e como verificar antes de publicar)"""

    resp = claude_cli.ask(prompt)
    md = os.path.join(outdir, "proposta.md")
    with open(md, "w", encoding="utf-8") as f:
        f.write(f"# Proposta de patch estrutural — {ts}\n\n"
                f"Casos:\n{casos_txt}\n\n---\n\n{resp or '(claude não respondeu)'}\n")

    print(f"\nproposta salva em {md}")
    print("PORTÃO: revise o diff. Para aplicar com segurança:")
    print("  1) git switch -c refinador/patch-" + ts)
    print("  2) aplique o diff manualmente e rode `python refinar.py --all` (regressão)")
    print("  3) só então o deploy (scp) — com seu OK explícito.")


if __name__ == "__main__":
    main()
