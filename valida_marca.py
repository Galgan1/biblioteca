# -*- coding: utf-8 -*-
"""valida_marca.py — GUARDA DE MÁQUINA da identidade visual (exit code, estilo audita_fantasmas.py).

POR QUÊ (Akita): "regra em doc != regra cumprida". A marca decidiu paleta MONO —
verde (h152) + ouro (h83, acento ÚNICO) + alerta (h30) — "sem arco-íris". Sem um
portão, qualquer cor solta (azul/roxo/teal) de um gerador VAZA pra peça pública e
o defeito propaga. Este gate RECUSA cor cromática cujo hue não seja da marca.

Os hues permitidos são DERIVADOS de marca.py (fonte única) — não hardcoded aqui:
se a marca mudar, o gate segue. Cores NEUTRAS (chroma baixo = cinza/preto/branco)
são livres em qualquer hue. Uso:  python valida_marca.py   (exit 0 = limpo, 1 = viola)
"""
import re
import sys
from pathlib import Path

try:                                       # gate nunca pode quebrar na PRÓPRIA saída (console cp1252)
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

ROOT = Path(__file__).parent
CHROMA_MIN = 0.04   # abaixo disto a cor é praticamente neutra (cinza) — hue não importa
HUE_TOL = 5         # tolerância de arredondamento em torno de um hue canônico

# Arquivos que EMITEM peça (cor pode vazar). marca.py/tokens.py são a fonte — não se auto-violam.
ALVOS = sorted(ROOT.glob('gerar_*.py')) + sorted((ROOT / 'assets').glob('*.css')) + [ROOT / 'tokens.py']

_OKLCH = re.compile(r'oklch\(\s*([\d.]+)%?\s+([\d.]+)\s+([\d.]+)')


def hues_da_marca():
    """Hues cromáticos canônicos, LIDOS de marca.py (fonte única da verdade)."""
    txt = (ROOT / 'marca.py').read_text(encoding='utf-8')
    return {round(float(h)) for _l, c, h in _OKLCH.findall(txt) if float(c) > CHROMA_MIN}


def _na_marca(hue, permitidos):
    return any(abs(hue - p) <= HUE_TOL for p in permitidos)


def violacoes():
    permitidos = hues_da_marca()
    achados = []
    for arq in ALVOS:
        if not arq.exists():
            continue
        for i, linha in enumerate(arq.read_text(encoding='utf-8').splitlines(), 1):
            for _l, c, h in _OKLCH.findall(linha):
                if float(c) > CHROMA_MIN and not _na_marca(round(float(h)), permitidos):
                    achados.append((arq.relative_to(ROOT).as_posix(), i, round(float(h)), float(c)))
    return permitidos, achados


# CATRACA: dívida CONHECIDA (arquivo -> hues fora da marca já presentes em 21/jun/2026).
# O gate fica VERDE com isto, mas REPROVA qualquer hue NOVO → o defeito para de propagar
# a partir de agora. Queime a dívida (mono-ize o mapa/painel, conserte o carrossel) e
# REMOVA daqui — encolher este dict é o progresso. NUNCA inflar sem justificativa revisada.
_BASELINE = {}   # dívida ZERADA (21/jun/2026): mapa/painel/carrossel mono-izados (verde/ouro/
                 # alerta). Catraca PURA agora — qualquer cor cromática fora da marca reprova na
                 # hora. Manter vazio; só inflar com exceção CONSCIENTE e justificada (ex.: data-viz).


def _baselined(arq, hue):
    """True se (arquivo, hue) já é dívida conhecida (tolerância de arredondamento)."""
    return any(abs(hue - b) <= HUE_TOL for b in _BASELINE.get(arq, ()))


def novas(achados):
    """Violações que NÃO estão na dívida conhecida — estas reprovam o gate."""
    return [(a, i, h, c) for (a, i, h, c) in achados if not _baselined(a, h)]


def main():
    permitidos, achados = violacoes()
    nv = novas(achados)
    print(f"marca: hues canonicos (de marca.py) = {sorted(permitidos)} | chroma_min={CHROMA_MIN}")
    if nv:
        print(f"\n[FALHA] {len(nv)} cor(es) NOVA(s) fora da marca (nao estao na divida/baseline):")
        for a, i, h, c in nv:
            print(f"  {a}:{i}  hue {h} (chroma {c}) — fora de {sorted(permitidos)}")
        print("\nUse os tokens de marca.py. Se for exceção consciente, adicione ao _BASELINE com justificativa.")
        return 1
    print(f"[OK] nenhuma cor NOVA fora da marca. (divida conhecida no baseline: {len(achados)} ocorrencia(s))")
    presentes = {(a, h) for a, _i, h, _c in achados}
    obsoletos = [(a, h) for a, hs in _BASELINE.items() for h in hs
                 if not any(abs(h - ph) <= HUE_TOL and a == pa for pa, ph in presentes)]
    if obsoletos:
        print(f"  divida ja quitada (pode remover do _BASELINE): {obsoletos}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
