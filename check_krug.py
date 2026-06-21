# -*- coding: utf-8 -*-
"""check_krug.py — guardrail de USABILIDADE do build (lente Krug + Norman).

Espelha o "Contrato por formato" de
  ~/.claude/skills/estudio-de-producao/references/usabilidade.md
e FALHA o build (exit != 0) quando uma peça fura a spec de um jeito que dá
para verificar ESTATICAMENTE — sem renderizar nada. É o irmão do check_marca.py
(tokens) só que para usabilidade.

================================ O QUE COBRE ================================
1. ORÇAMENTO DE TEXTO (régua do vídeo, ≤52 palavras/cena)
   Varre videos/roteiros/*.json e flagueia toda `cena.narracao` com >52 palavras.
   Doutrina do próprio código (gerar_video._to_ssml): "manter narração ≤ ~52
   palavras/cena para caber nos 30s/cena". -> AVISO (soft), não derruba o build:
   é pervasivo na narração FALADA e mais um sinal de QC do que um erro de spec.

2. PROGRESSO DUPLO (proibido: 2 sistemas no mesmo tipo de slide)
   Heurística sobre gerar_carrossel.py: nenhum builder de slide pode emitir ao
   mesmo tempo `_dots(...)`/.dots E um contador `.qcount`/`NN/NN`. -> FALHA dura.

3. SAFE-ZONE (story / capa de Reel) >= ~260px
   - gerar_carrossel.py STORY_CSS: `.badge{top:NNpx}` e `.foot{bottom:NNpx}`.
   - videos/gerar_short.py: âncoras de safe-zone da CAPA do Reel (topo = y do
     wordmark; rodapé = margem do bloco inferior até a borda H).
   Qualquer valor < 260 -> FALHA dura (algo essencial sob a UI do app).

4. THUMBNAIL (≤6 palavras)
   Não há fonte ESTÁTICA de punches de thumbnail (o punch entra como argumento
   de CLI em gerar_thumb.main e já é validado lá em runtime). Então expomos um
   hook reutilizável `assert_thumb_punch(text)` para o gerador/build chamar
   ANTES de renderizar. Não varre nada — não há dado estático a varrer.

================================== TODO ===================================
Exige RENDER (teste de miniatura) — fora do escopo deste guardrail estático,
fica para auditoria por subagente olhando a peça reduzida:
  - Billboard test (thumb/capa "pega" num relance de polegar).
  - Trunk test das páginas de capítulo (breadcrumb, "onde estou?").
  - Affordance / feedback (o que é clicável; hover/view-transition).
  - Contraste/legibilidade sob movimento no vídeo.
  - Densidade real do infográfico na grade.
  - Mobile / alvos de toque >=44px.
  - Capa de Reel nunca caindo em frame preto (depende do thumb_offset render).

Uso:  python check_krug.py
Exit: 0 se nenhuma violação DURA; != 0 se houver (avisos não derrubam).
"""
import json
import re
import sys
from pathlib import Path

# Console do Windows costuma vir em cp1252 e quebra com ≤/·/—. Força UTF-8 no
# stdout para o guardrail rodar igual em qualquer ambiente de build.
try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

ROOT = Path(__file__).resolve().parent
ROTEIROS = ROOT / "videos" / "roteiros"
CARROSSEL = ROOT / "gerar_carrossel.py"
SHORT = ROOT / "videos" / "gerar_short.py"

WORD_BUDGET = 52      # régua do vídeo (≤52 palavras/cena)
THUMB_WORDS = 6       # thumbnail ≤6 palavras
SAFE_MIN = 260        # piso da zona segura 9:16 (UI do IG cobre ~250px)


# --------------------------------------------------------------------------- #
# Hook reutilizável (check #4) — para o gerador/build chamar antes do render.  #
# --------------------------------------------------------------------------- #
def assert_thumb_punch(text):
    """Régua de thumbnail (Krug, billboard): punch <=6 palavras.
    Levanta ValueError se estourar. Reutilizável pelo build/gerador ANTES de
    renderizar a thumb (gerar_thumb.py já faz a mesma checagem em runtime)."""
    n = len(str(text).split())
    if n > THUMB_WORDS:
        raise ValueError(
            f"thumbnail: punch com {n} palavras (max {THUMB_WORDS}) -> encurte: {text!r}"
        )
    return True


# --------------------------------------------------------------------------- #
# Check 1 — orçamento de texto nas narrações dos roteiros.                     #
# --------------------------------------------------------------------------- #
def check_text_budget():
    """Retorna lista de avisos 'arquivo:cena:contagem' p/ narração >52 palavras."""
    warns = []
    if not ROTEIROS.is_dir():
        return warns, 0
    files = sorted(ROTEIROS.glob("*.json"))
    cenas_total = 0
    for fp in files:
        try:
            data = json.loads(fp.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError) as e:
            warns.append(f"{fp.name}: nao deu p/ ler ({e})")
            continue
        for i, cena in enumerate(data.get("cenas", [])):
            cenas_total += 1
            n = len((cena.get("narracao") or "").split())
            if n > WORD_BUDGET:
                warns.append(f"{fp.name}:cena[{i}]:{n} palavras")
    return warns, cenas_total


# --------------------------------------------------------------------------- #
# Check 2 — progresso duplo no carrossel (2 sistemas no mesmo slide).          #
# --------------------------------------------------------------------------- #
def check_double_progress():
    """Heurística: nenhum builder de slide pode emitir dots E contador NN/NN.
    Quebra gerar_carrossel.py em funções `def _xxx(...)` e, em cada uma que
    monta slide, vê se aparecem AS DUAS marcas de progresso juntas."""
    fails = []
    if not CARROSSEL.exists():
        fails.append(f"{CARROSSEL.name} nao encontrado")
        return fails
    src = CARROSSEL.read_text(encoding="utf-8")

    # quebra em blocos por definição de função (escopo do builder de slide)
    parts = re.split(r"(?m)^def\s+(\w+)\s*\(", src)
    # parts = [head, name1, body1, name2, body2, ...]
    dots_re = re.compile(r"_dots\s*\(|class=\"dots\"|class='dots'")
    count_re = re.compile(r"qcount|\bclass=\"count\"|\bclass='count'|\d{2}\s*/\s*\d{2}|\bNN\s*/\s*NN\b")
    for k in range(1, len(parts), 2):
        name, body = parts[k], parts[k + 1]
        # só faz sentido em quem realmente monta slide (emite _slide(...))
        if "_slide(" not in body:
            continue
        has_dots = bool(dots_re.search(body))
        has_count = bool(count_re.search(body))
        if has_dots and has_count:
            fails.append(
                f"{CARROSSEL.name}:def {name}() emite dots E contador NN/NN "
                "(2 sistemas de progresso no mesmo slide)"
            )
    return fails


# --------------------------------------------------------------------------- #
# Check 3 — safe-zone >= 260px (story + capa de Reel).                         #
# --------------------------------------------------------------------------- #
def check_safe_zones():
    """Lê valores numéricos de zona segura no CÓDIGO e reporta < 260."""
    fails = []

    # 3a) STORY_CSS do carrossel: .badge{top:NNpx}  e  .foot{bottom:NNpx}
    if CARROSSEL.exists():
        src = CARROSSEL.read_text(encoding="utf-8")
        m = re.search(r"STORY_CSS\s*=\s*(?:'''|\"\"\")(.*?)(?:'''|\"\"\")", src, re.S)
        story_css = m.group(1) if m else ""
        if not story_css:
            fails.append(f"{CARROSSEL.name}: STORY_CSS nao localizado")
        else:
            for sel, prop in (("badge", "top"), ("foot", "bottom")):
                mm = re.search(rf"\.{sel}\s*\{{[^}}]*?\b{prop}\s*:\s*(\d+)px", story_css)
                if mm:
                    val = int(mm.group(1))
                    if val < SAFE_MIN:
                        fails.append(
                            f"{CARROSSEL.name} STORY_CSS .{sel} {prop}:{val}px < {SAFE_MIN}px"
                        )
                else:
                    fails.append(
                        f"{CARROSSEL.name} STORY_CSS: nao achei .{sel} {prop} (safe-zone)"
                    )

    # 3b) Capa de Reel (videos/gerar_short.py): topo = y do wordmark; rodapé =
    #     margem (H - y) do bloco inferior. Lemos as âncoras anotadas como
    #     "safe-zone" no make_cover.
    if SHORT.exists():
        src = SHORT.read_text(encoding="utf-8")
        H = _int_const(src, "H") or 1920

        # topo: a 1ª âncora vertical do bloco do topo na capa (wordmark a y=260)
        top = _short_cover_top(src)
        if top is None:
            fails.append(f"{SHORT.name}: nao achei o topo da safe-zone da capa")
        elif top < SAFE_MIN:
            fails.append(f"{SHORT.name} capa: topo y={top}px < {SAFE_MIN}px")

        # rodapé: menor margem (H - y) entre as âncoras inferiores da capa
        bottom = _short_cover_bottom(src, H)
        if bottom is None:
            fails.append(f"{SHORT.name}: nao achei o rodape da safe-zone da capa")
        elif bottom < SAFE_MIN:
            fails.append(f"{SHORT.name} capa: rodape margem={bottom}px (H-y) < {SAFE_MIN}px")

    return fails


def _int_const(src, name):
    """Lê uma constante simples no topo do módulo, ex.: W, H = 1080, 1920."""
    m = re.search(rf"(?m)^\s*W\s*,\s*H\s*=\s*\d+\s*,\s*(\d+)", src)
    if name == "H" and m:
        return int(m.group(1))
    m2 = re.search(rf"(?m)^\s*{re.escape(name)}\s*=\s*(\d+)\b", src)
    return int(m2.group(1)) if m2 else None


def _short_cover_top(src):
    """Topo da safe-zone da capa do Reel = y do wordmark 'MINUTO REAL' em make_cover.
    Procura a chamada `gv.tracked(d, (x, Y), 'MINUTO REAL', ...)`."""
    m = re.search(
        r"gv\.tracked\(\s*d\s*,\s*\(\s*\d+\s*,\s*(\d+)\s*\)\s*,\s*['\"]MINUTO REAL['\"]",
        src,
    )
    return int(m.group(1)) if m else None


def _short_cover_bottom(src, H):
    """Rodapé da safe-zone da capa = menor margem (H - y) entre as âncoras
    inferiores ancoradas em H na make_cover. Pega todos os `H - NN` usados como
    coordenada y de texto e devolve o menor (H - max(offset))."""
    cover = _slice_func(src, "make_cover")
    if not cover:
        return None
    offs = [int(x) for x in re.findall(r"\bH\s*-\s*(\d+)\b", cover)]
    if not offs:
        return None
    # a âncora MAIS BAIXA é a de maior offset; a margem dela até a borda é o offset
    return min(offs)


def _slice_func(src, name):
    """Recorta o corpo de uma função top-level por indentação."""
    m = re.search(rf"(?m)^def\s+{re.escape(name)}\s*\(", src)
    if not m:
        return ""
    rest = src[m.end():]
    nxt = re.search(r"(?m)^def\s+\w+\s*\(", rest)
    return rest[: nxt.start()] if nxt else rest


# --------------------------------------------------------------------------- #
# Relatório + exit code.                                                       #
# --------------------------------------------------------------------------- #
def main():
    text_warns, cenas = check_text_budget()
    dbl_fails = check_double_progress()
    safe_fails = check_safe_zones()

    hard = dbl_fails + safe_fails
    soft = text_warns

    print("=" * 64)
    print("  check_krug.py — guardrail de usabilidade (Krug + Norman)")
    print("=" * 64)

    # 1 — orçamento de texto (soft)
    print(f"\n[1] Orçamento de texto · narração ≤{WORD_BUDGET} palavras/cena (AVISO)")
    print(f"    cenas varridas: {cenas} · acima do orçamento: {len(text_warns)}")
    for w in text_warns[:25]:
        print(f"      - {w}")
    if len(text_warns) > 25:
        print(f"      ... (+{len(text_warns) - 25} cenas)")

    # 2 — progresso duplo (hard)
    print(f"\n[2] Progresso duplo · 1 só sistema por slide (FALHA)")
    if dbl_fails:
        for f in dbl_fails:
            print(f"      - {f}")
    else:
        print("      OK — nenhum slide com dois sistemas de progresso.")

    # 3 — safe-zone (hard)
    print(f"\n[3] Safe-zone · story + capa de Reel ≥{SAFE_MIN}px (FALHA)")
    if safe_fails:
        for f in safe_fails:
            print(f"      - {f}")
    else:
        print(f"      OK — todas as âncoras de zona segura ≥{SAFE_MIN}px.")

    # 4 — thumbnail (hook)
    print(f"\n[4] Thumbnail · punch ≤{THUMB_WORDS} palavras (HOOK)")
    print("      Sem fonte estática de punches (entram via CLI em gerar_thumb).")
    print("      Hook reutilizável exposto: assert_thumb_punch(text).")

    # resumo
    print("\n" + "-" * 64)
    print(f"  Violações DURAS: {len(hard)}   ·   Avisos: {len(soft)}")
    print("-" * 64)
    if hard:
        print("  RESULTADO: FALHOU (violação dura) — corrija antes de publicar.")
        return 1
    print("  RESULTADO: OK (sem violação dura).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
