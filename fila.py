#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera a fila semanal de publicações do canal Minuto Real.

Entrada:  videos/roteiros/*.json
Saída:    fila.json (array de slots de publicação)

Uso:
  python fila.py --semanas 4 --output fila.json
  python fila.py --semanas 1 --dry-run
"""
import argparse
import json
import sys
from datetime import date, timedelta
from pathlib import Path

ROTEIROS_DIR = Path(__file__).parent / "videos" / "roteiros"
PUBLICADOS_JSON = Path(__file__).parent / "publicados.json"

SERIES: dict[str, list[str]] = {
    "poder": ["48-leis-do-poder", "arte-da-guerra", "maquiavel-pedagogo", "o-principe"],
    "dinheiro": ["padrao-bitcoin", "pai-rico-pai-pobre", "psicologia-financeira"],
    "mentalidade": ["habitos-atomicos", "sutil-arte", "nacao-dopamina", "poder-do-silencio"],
    "comportamento": ["admiravel-mundo-novo", "quem-mexeu-no-queijo", "gene-egoista", "1984"],
    "narrativa": ["jornada-do-escritor", "aristoteles-poetica", "save-the-cat"],
    "marketing": ["marketing-4-0"],
    "futebol": ["futebol-brasileiro"],
}

# Ordem de séries por semana (índice = (semana-1) % len)
SERIE_ROTATION: list[list[str]] = [
    ["poder", "dinheiro"],
    ["mentalidade", "comportamento"],
    ["narrativa", "marketing"],
    ["futebol", "outros"],
]

# (dia, horario, formato) — cadência padrão por semana
CADENCIA: list[tuple[str, str, str]] = [
    ("SEG", "18:30", "reel"),
    ("TER", "08:00", "stories"),
    ("QUA", "18:30", "reel"),
    ("QUI", "08:00", "stories"),
    ("SEX", "18:30", "carrossel"),
    ("SAB", "10:00", "stories"),
]


def _ler_roteiros() -> dict[str, dict]:
    """Retorna {slug: roteiro} de todos os arquivos em ROTEIROS_DIR."""
    roteiros = {}
    for path in sorted(ROTEIROS_DIR.glob("*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            slug = data.get("slug") or path.stem
            roteiros[slug] = data
        except (json.JSONDecodeError, OSError):
            pass
    return roteiros


def _serie_de(slug: str) -> str:
    """Classifica um slug na série temática (ou 'outros')."""
    for serie, slugs in SERIES.items():
        if slug in slugs:
            return serie
    return "outros"


def _slugs_por_serie(roteiros: dict[str, dict]) -> dict[str, list[str]]:
    """Agrupa slugs disponíveis por série."""
    grupos: dict[str, list[str]] = {}
    for slug in roteiros:
        serie = _serie_de(slug)
        grupos.setdefault(serie, []).append(slug)
    return grupos


def _publicados_recentes(dias: int = 30) -> set[str]:
    """Retorna slugs publicados nos últimos `dias` dias (via publicados.json)."""
    if not PUBLICADOS_JSON.exists():
        return set()
    try:
        dados = json.loads(PUBLICADOS_JSON.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return set()
    corte = date.today() - timedelta(days=dias)
    recentes = set()
    for entry in dados:
        try:
            if date.fromisoformat(entry["data"]) >= corte:
                recentes.add(entry["slug"])
        except (KeyError, ValueError):
            pass
    return recentes


def _series_da_semana(semana: int) -> list[str]:
    """Retorna as duas séries ativas para a semana dada (1-indexada)."""
    return SERIE_ROTATION[(semana - 1) % len(SERIE_ROTATION)]


def _proximo_slug(
    grupos: dict[str, list[str]],
    serie: str,
    usados: set[str],
    recentes: set[str],
) -> tuple[str, str] | None:
    """Pega o próximo slug disponível da série, evitando usados e recentes."""
    candidatos = grupos.get(serie, [])
    # Prefere não-recentes; aceita recentes se não houver outra opção
    for prioridade in (
        [s for s in candidatos if s not in usados and s not in recentes],
        [s for s in candidatos if s not in usados],
    ):
        if prioridade:
            slug = prioridade[0]
            return slug, serie
    # Fallback: qualquer série disponível
    for s, slugs in grupos.items():
        disponiveis = [x for x in slugs if x not in usados]
        if disponiveis:
            return disponiveis[0], s
    return None


def gerar_fila(semanas: int = 4) -> list[dict]:
    """Gera a lista de slots de publicação para N semanas."""
    roteiros = _ler_roteiros()
    grupos = _slugs_por_serie(roteiros)
    recentes = _publicados_recentes()
    slots = []
    usados_global: set[str] = set()

    for semana in range(1, semanas + 1):
        series_ativas = _series_da_semana(semana)
        usados_semana: set[str] = set()
        # Pares: SEG→série[0], QUA→série[1], SEX→série[0]
        serie_por_slot = [
            series_ativas[0],  # SEG reel
            series_ativas[0],  # TER stories (acompanha SEG)
            series_ativas[1] if len(series_ativas) > 1 else series_ativas[0],  # QUA reel
            series_ativas[1] if len(series_ativas) > 1 else series_ativas[0],  # QUI stories
            series_ativas[0],  # SEX carrossel
            series_ativas[0],  # SAB stories reforço
        ]
        # Slugs por par (SEG+TER compartilham, QUA+QUI compartilham, SEX+SAB compartilham)
        pares: list[str | None] = [None, None, None]

        for i, (dia, horario, fmt) in enumerate(CADENCIA):
            par_idx = i // 2
            if pares[par_idx] is None:
                resultado = _proximo_slug(
                    grupos,
                    serie_por_slot[i],
                    usados_semana | usados_global,
                    recentes,
                )
                if resultado is None:
                    continue
                slug, serie_real = resultado
                pares[par_idx] = slug
                usados_semana.add(slug)
                usados_global.add(slug)
            else:
                slug = pares[par_idx]
                serie_real = _serie_de(slug)

            roteiro = roteiros[slug]
            formato_slot = fmt if par_idx < 2 else fmt
            # stories acompanha com formato combinado no slot reel
            if i % 2 == 0:
                formato_slot = "reel+stories" if fmt == "reel" else fmt

            slots.append({
                "slug": slug,
                "titulo": roteiro.get("titulo", slug),
                "serie": serie_real,
                "formato": formato_slot,
                "dia": dia,
                "horario": horario,
                "semana": semana,
            })

    return slots


def main() -> None:
    parser = argparse.ArgumentParser(description="Gera fila semanal do canal Minuto Real")
    parser.add_argument("--semanas", type=int, default=4)
    parser.add_argument("--output", default="fila.json")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    fila = gerar_fila(args.semanas)
    saida = json.dumps(fila, ensure_ascii=False, indent=2)

    if args.dry_run:
        print(saida)
    else:
        Path(args.output).write_text(saida, encoding="utf-8")
        print(f"Fila gerada: {len(fila)} slots em {args.output}")


if __name__ == "__main__":
    main()
