# -*- coding: utf-8 -*-
"""data_gate.py — porteiro da RÚBRICA do `<slug>_data.py`.

    python data_gate.py <slug>

Sai 0 se o `<slug>_data.py` passa em TODA a rúbrica; senão sai 1 e imprime,
linha a linha, cada motivo da reprovação. É o "verde = exit code" do Akita:
nada se publica sem este portão fechar. NÃO escreve nada, NÃO chama IA, NÃO
faz deploy — só lê o arquivo de conteúdo e o julga.

Rúbrica (espelha o padrão-ouro `leis_da_natureza_humana_data.py`):
  - o módulo `<slug>_data.py` importa sem erro;
  - BOOK existe e tem title / author / cover / overview_cards;
  - todo card (de overview_cards e de cada CHAPTERS[].cards) tem:
      * `ic` dentro da lista válida de ícones;
      * `t` e `b` não-vazios;
      * `b` com PELO MENOS um `<strong>` (ver nota em _checar_card);
      * `emph` (quando presente) é substring EXATA de `t`;
  - há ao menos 3 CHAPTERS.
"""
import importlib
import os
import sys

try:  # console Windows é cp1252 — força UTF-8 p/ não quebrar nos acentos
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:  # noqa: BLE001
    pass

# A raiz do projeto (um nível acima de pdf-service/) onde vivem os `*_data.py`.
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Lista FECHADA de ícones de linha que o gerador conhece. Card com `ic` fora
# desta lista renderiza um buraco — por isso é bloqueante.
ICONES_VALIDOS = {
    "arrow", "book", "bookmark", "bubble", "bulb", "cards", "clock",
    "constellation", "eye", "fork", "gap", "key", "layers", "leaf", "lens",
    "link", "mask", "masks", "mountain", "person", "pin", "pivot", "play",
    "scale", "shelf", "shield", "spark", "spiral", "steps", "sword", "target",
    "triangle", "wave", "wrench",
}


def _strong_count(texto):
    """Quantas tags <strong> abertas há no texto (case-insensitive)."""
    return texto.lower().count("<strong>")


def _checar_card(card, onde, motivos):
    """Aplica a régua do card e ACUMULA os motivos de reprovação em `motivos`."""
    if not isinstance(card, dict):
        motivos.append(f"{onde}: card não é um dict ({card!r})")
        return

    ic = card.get("ic")
    if ic not in ICONES_VALIDOS:
        motivos.append(f"{onde}: ic {ic!r} fora da lista válida de ícones")

    t = card.get("t")
    if not isinstance(t, str) or not t.strip():
        motivos.append(f"{onde}: 't' vazio ou ausente")
        t = ""

    b = card.get("b")
    if not isinstance(b, str) or not b.strip():
        motivos.append(f"{onde}: 'b' vazio ou ausente")
        b = ""
    else:
        # NOTA (conflito de spec resolvido): a rúbrica pedida diz "EXATAMENTE um
        # <strong>", mas o padrão-ouro `leis_da_natureza_humana_data.py` — citado
        # como o exemplo bom — tem cards com 2–3 <strong> (enumerações como a das
        # "Três Alavancas"). Um portão que reprova o próprio gold standard estaria
        # errado. O contrato inviolável que o gold satisfaz é "NUNCA zero". É isso
        # que travamos aqui; o runbook ainda orienta o autor a usar 1 por padrão.
        # Para forçar `== 1`, troque `< 1` por `!= 1`.
        if _strong_count(b) < 1:
            motivos.append(f"{onde}: 'b' precisa de PELO MENOS um <strong> (tem 0)")

    emph = card.get("emph")
    if emph is not None:
        if not isinstance(emph, str) or emph not in t:
            motivos.append(f"{onde}: 'emph' {emph!r} não é substring exata de 't'")


def revisar(slug):
    """Devolve a lista de motivos de reprovação. Vazia = passou na rúbrica."""
    motivos = []

    # 1) importa o módulo de conteúdo (a raiz precisa estar no sys.path)
    if RAIZ not in sys.path:
        sys.path.insert(0, RAIZ)
    mod_name = slug.replace("-", "_") + "_data"
    try:
        mod = importlib.import_module(mod_name)
    except Exception as e:  # noqa: BLE001
        return [f"{mod_name}.py não importa: {e}"]

    BOOK = getattr(mod, "BOOK", None)
    CHAPTERS = getattr(mod, "CHAPTERS", None)

    # 2) BOOK e suas chaves obrigatórias
    if not isinstance(BOOK, dict):
        motivos.append("BOOK ausente ou não é dict")
        BOOK = {}
    for chave in ("title", "author", "cover", "overview_cards"):
        val = BOOK.get(chave)
        if val is None or (isinstance(val, str) and not val.strip()):
            motivos.append(f"BOOK faltando/vazio: {chave!r}")

    # 2b) cards da visão geral
    ov = BOOK.get("overview_cards")
    if not isinstance(ov, list) or not ov:
        motivos.append("BOOK['overview_cards'] ausente ou vazio")
    else:
        for i, card in enumerate(ov):
            _checar_card(card, f"overview_cards[{i}]", motivos)

    # 3) CHAPTERS — ao menos 3, cada card pela régua
    if not isinstance(CHAPTERS, list):
        motivos.append("CHAPTERS ausente ou não é lista")
        CHAPTERS = []
    if len(CHAPTERS) < 3:
        motivos.append(f"CHAPTERS precisa de >=3 capítulos (tem {len(CHAPTERS)})")
    for ch in CHAPTERS:
        slug_ch = ch.get("slug", "?") if isinstance(ch, dict) else "?"
        cards = ch.get("cards") if isinstance(ch, dict) else None
        if not isinstance(cards, list) or not cards:
            motivos.append(f"capítulo {slug_ch!r}: sem cards")
            continue
        for i, card in enumerate(cards):
            _checar_card(card, f"{slug_ch}.cards[{i}]", motivos)

    return motivos


def main():
    if len(sys.argv) != 2:
        print("uso: python data_gate.py <slug>")
        sys.exit(1)
    slug = sys.argv[1]
    motivos = revisar(slug)
    if motivos:
        print(f"REPROVADO: {slug}_data.py não passou na rúbrica ({len(motivos)} motivos):")
        for m in motivos:
            print(f"  - {m}")
        sys.exit(1)
    print(f"OK: {slug}_data.py passou na rúbrica.")
    sys.exit(0)


if __name__ == "__main__":
    main()
