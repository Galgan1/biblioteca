# -*- coding: utf-8 -*-
"""verificar_copy.py — GATE de COPY/MARKETING (blindagem: amplificar mestres, não defeitos).

Dois níveis, espelhando o split do projeto (determinístico sempre + juiz no publish):
  1. CHECAGENS DURAS (determinísticas, sem API): regras inegociáveis do projeto —
     pt-PT bloqueante, link cru na legenda do IG, link Amazon de BUSCA, excesso de hashtag.
     São o "verde = exit code" que NÃO flaka e NÃO custa API → entram no testar.py via teste.
  2. JUIZ CROSS-MODEL (Claude Sonnet, juiz != autor): nota a copy contra os MESTRES
     (Cialdini/Kotler/Krug/Beaugrande). Roda no publish/sob demanda (custa API) — não no CI.

A régua sai dos MESTRES (skills armas-da-persuasao, marketing-4-0, nao-me-faca-pensar,
beaugrande-linguistica-textual), não do gosto de quem escreveu. exit 0 = aprovado, 1 = reprovado.

Uso:
  echo "<copy>" | python verificar_copy.py --plataforma ig
  python verificar_copy.py --plataforma youtube --arquivo legenda.txt
  python verificar_copy.py --plataforma ig --texto "..." --rapido   # só checagens duras (sem juiz/API)
"""
import os
import re
import subprocess
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

# pt-PT bloqueante (contrato 6): marcadores de ALTA confiança (não aparecem em pt-BR).
# Evita "utilizar"/"deve-se" (comuns no BR) — só grafias/léxico inequívocos de Portugal.
_PT_PT = re.compile(
    r"\b(ecrã|telemóvel|autocarro|comboio|casa de banho|pequeno-almoço|rapariga|"
    r"fact[o]s?|actual\w*|acç\w+|direcç\w+|colecç\w+|efectiv\w+|óptim\w+|óptic\w+|"
    r"exact[oa]s?|contacto|baptiz\w+|percebes\b|estás a\b)\b", re.IGNORECASE)


def checa_duro(texto: str, plataforma: str = "ig") -> list[str]:
    """Regras inegociáveis (determinísticas). Devolve lista de FALHAS (vazia = ok)."""
    t = texto or ""
    falhas = []
    if _PT_PT.search(t):
        m = _PT_PT.search(t)
        falhas.append(f"pt-PT bloqueante (contrato idioma): termo '{m.group(0)}' — todo conteúdo é pt-BR")
    if plataforma == "ig" and re.search(r"https?://", t):
        falhas.append("link CRU na legenda do IG: URL não é clicável no feed → afiliado/CTA vai na BIO")
    if re.search(r"amazon\.[^\s]*([?&]k=|/s\?|/s/)", t, re.IGNORECASE):
        falhas.append("link Amazon de BUSCA (s?k=): use só link de PRODUTO (/dp/ ou /gp/)")
    n_tags = len(re.findall(r"(?<!\w)#\w+", t))
    if n_tags > 15:
        falhas.append(f"hashtags em excesso ({n_tags}): doutrina = 3–5 de nicho, não enxurrada")
    return falhas


_RUBRICA = (
    "Você é JUIZ de COPY/MARKETING em pt-BR — independente de quem escreveu, RIGOROSO e "
    "ANTI-BAJULAÇÃO (seu trabalho é achar o que está fraco, não agradar). Julgue a copy "
    "contra os MESTRES. Plataforma: {plat}.\n\n"
    "RÚBRICA (0-10 cada):\n"
    "1. GANCHO (Krug, billboard/omita o desnecessário): a 1ª linha para o dedo? curiosidade "
    "ou afirmação ousada, sem enrolar?\n"
    "2. PERSUASÃO (Cialdini): usa arma LEGÍTIMA (prova social, autoridade/autor, reciprocidade="
    "entrega valor antes do pedido, unidade) sem manipulação barata nem escassez falsa?\n"
    "3. FUNIL/CTA (Kotler — 5 As + BAR): CTA claro que move pra SALVAR/COMPARTILHAR/seguir/"
    "link-na-bio (ação→apologia), NÃO pra 'like'?\n"
    "4. CLAREZA (Krug): enxuto, escaneável, sem jargão; cada palavra ganha seu lugar?\n"
    "5. COESÃO (Beaugrande): flui (dado→novo), sem cacofonia nem repetição tosca?\n"
    "6. ADEQUAÇÃO: pt-BR de verdade; tom sóbrio/premium da marca?\n\n"
    "COPY A JULGAR:\n\"\"\"\n{copy}\n\"\"\"\n\n"
    "Responda APENAS JSON válido (sem markdown):\n"
    '{{"criterios":{{"gancho":n,"persuasao":n,"funil_cta":n,"clareza":n,"coesao":n,"adequacao":n}},'
    '"nota_geral":n,"veredicto":"APROVADO"|"AJUSTE","problemas":["..."],'
    '"sugestao_1a_linha":"uma 1ª linha melhor, ou \'\' se a atual já é ótima"}}\n'
    "APROVADO só se nota_geral>=7 E nenhum critério<5."
)


def _ask(prompt: str, model: str, timeout: int = 180) -> str | None:
    """Juiz headless (claude -p --model). model CONFIGURÁVEL p/ apontar pro que tiver
    crédito/disponível (env JUIZ_COPY_MODEL). Nunca lança — None se falhar/sem crédito."""
    try:
        r = subprocess.run(f"claude -p --model {model}", input=prompt, capture_output=True,
                           text=True, shell=True, encoding="utf-8", errors="replace", timeout=timeout)
        out = (r.stdout or "").strip()
        return out if out and "balance is too low" not in out.lower() else None
    except Exception:
        return None


def julga(texto: str, plataforma: str = "ig", model: str | None = None) -> dict | None:
    """Juiz cross-model (juiz != autor). model: arg/env JUIZ_COPY_MODEL ou claude-sonnet-4-6."""
    from verificar_conteudo import _parse_json                # reusa só o parser (model-agnóstico)
    model = model or os.environ.get("JUIZ_COPY_MODEL", "claude-sonnet-4-6")
    return _parse_json(_ask(_RUBRICA.format(plat=plataforma, copy=texto), model))


def _entrada(args) -> str:
    if "--arquivo" in args:
        from pathlib import Path
        return Path(args[args.index("--arquivo") + 1]).read_text(encoding="utf-8", errors="replace")
    if "--texto" in args:
        return args[args.index("--texto") + 1]
    return sys.stdin.read() if not sys.stdin.isatty() else ""


def main(args) -> int:
    plat = args[args.index("--plataforma") + 1] if "--plataforma" in args else "ig"
    texto = (_entrada(args) or "").strip()
    if not texto:
        print("Uso: ... | python verificar_copy.py --plataforma ig   (ou --arquivo / --texto)")
        return 0

    falhas = checa_duro(texto, plat)
    print(f"=== verificar_copy ({plat}) — checagens duras ===")
    if falhas:
        for f in falhas:
            print(f"  [DURO] {f}")
    else:
        print("  [OK] nenhuma regra inegociável violada.")

    if "--rapido" in args:
        return 1 if falhas else 0

    print("\n=== juiz cross-model (mestres) ===")
    model = args[args.index("--model") + 1] if "--model" in args else None
    v = julga(texto, plat, model)
    if not v:
        print("  (juiz indisponível — sem resposta do modelo; valeu só a checagem dura)")
        return 1 if falhas else 0
    cr = v.get("criterios", {})
    print(f"  nota geral: {v.get('nota_geral')}  | veredicto: {v.get('veredicto')}")
    print("  criterios: " + " · ".join(f"{k}={cr[k]}" for k in cr))
    for p in v.get("problemas", []):
        print(f"   - {p}")
    if v.get("sugestao_1a_linha"):
        print(f"  sugestão de 1ª linha: {v['sugestao_1a_linha']}")

    aprovado = (not falhas) and v.get("veredicto") == "APROVADO" and (v.get("nota_geral", 0) or 0) >= 7
    print(f"\nRESULTADO: {'APROVADO (exit 0)' if aprovado else 'REPROVADO (exit 1)'}")
    return 0 if aprovado else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
