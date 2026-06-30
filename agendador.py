#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Agendador de publicações do canal Minuto Real via Windows schtasks.

Lê fila.json (gerado por fila.py) e cria/lista/remove tarefas agendadas.

Uso:
  python agendador.py --dry-run   # mostra próximas 7 publicações sem criar tarefas
  python agendador.py --criar     # cria schtasks para a semana atual
  python agendador.py --limpar    # remove schtasks criadas por este script
  python agendador.py --listar    # lista schtasks ativas do Minuto Real
"""
import json
import subprocess
import sys
from datetime import date, timedelta
from pathlib import Path

FILA_JSON = Path(__file__).parent / "fila.json"
PREFIX = "MinutoReal-"
PYTHON = sys.executable
PUBLICAR = str(Path(__file__).parent / "publicar_livro.py")

# Dias da semana → número (0=segunda, 6=sábado; aceita abreviações de fila.py)
_DIAS = {
    "segunda": 0, "seg": 0,
    "terca": 1,   "ter": 1,
    "quarta": 2,  "qua": 2,
    "quinta": 3,  "qui": 3,
    "sexta": 4,   "sex": 4,
    "sabado": 5,  "sab": 5,
}


def _ler_fila() -> list[dict]:
    if not FILA_JSON.exists():
        print("ERRO: fila.json não encontrado. Rode fila.py primeiro.", file=sys.stderr)
        sys.exit(1)
    return json.loads(FILA_JSON.read_text(encoding="utf-8"))


def _data_slot(dia_nome: str, hoje: date) -> date:
    """Retorna a data do próximo 'dia_nome' na semana atual (seg–dom)."""
    alvo = _DIAS.get(dia_nome.lower(), 0)
    # Início da semana atual (segunda-feira)
    inicio = hoje - timedelta(days=hoje.weekday())
    return inicio + timedelta(days=alvo)


def _nome_tarefa(slug: str, data: date) -> str:
    return f"{PREFIX}{slug}-{data.strftime('%Y%m%d')}"


def _cmd_publicar(slug: str, plataformas: str) -> str:
    return f'"{PYTHON}" "{PUBLICAR}" {slug} --plataformas {plataformas}'


def _cmd_criar(nome: str, cmd: str, horario: str, data: date) -> list[str]:
    return [
        "schtasks", "/Create",
        "/TN", nome,
        "/TR", cmd,
        "/SC", "ONCE",
        "/ST", horario,
        "/SD", data.strftime("%m/%d/%Y"),
        "/F",
    ]


def _tarefa_existe(nome: str) -> bool:
    r = subprocess.run(
        ["schtasks", "/Query", "/TN", nome],
        capture_output=True, text=True,
    )
    return r.returncode == 0


def _slots_semana(fila: list[dict], hoje: date) -> list[dict]:
    """Retorna os slots da semana atual, limitado a 7."""
    resultado = []
    for slot in fila:
        data = _data_slot(slot.get("dia", "segunda"), hoje)
        resultado.append({**slot, "_data": data})
    # Ordena por data/horário e limita a 7
    resultado.sort(key=lambda s: (s["_data"], s.get("horario", "00:00")))
    return resultado[:7]


def cmd_dry_run(fila: list[dict], hoje: date) -> None:
    slots = _slots_semana(fila, hoje)
    print("DRY-RUN: proximas 7 publicacoes")
    print(f"{'SLUG':<25} {'DATA/HORA':<22} {'FORMATO'}")
    print("-" * 65)
    for s in slots:
        data = s["_data"]
        horario = s.get("horario", "18:30")
        plataformas = s.get("plataformas", "ig,fb,yt")
        data_hora = f"{data.strftime('%Y-%m-%d')} {horario}"
        print(f"{s['slug']:<25} {data_hora:<22} {plataformas}")


def cmd_criar(fila: list[dict], hoje: date) -> None:
    slots = _slots_semana(fila, hoje)
    for s in slots:
        data = s["_data"]
        horario = s.get("horario", "18:30")
        plataformas = s.get("plataformas", "ig,fb,yt")
        nome = _nome_tarefa(s["slug"], data)
        if _tarefa_existe(nome):
            print(f"[skip] {nome} ja existe")
            continue
        cmd = _cmd_criar(nome, _cmd_publicar(s["slug"], plataformas), horario, data)
        r = subprocess.run(cmd, capture_output=True, text=True)
        if r.returncode == 0:
            print(f"[ok]   {nome}")
        else:
            print(f"[erro] {nome}: {r.stderr.strip()}", file=sys.stderr)


def cmd_limpar() -> None:
    r = subprocess.run(
        ["schtasks", "/Query", "/FO", "CSV", "/NH"],
        capture_output=True, text=True,
    )
    removidas = 0
    for linha in r.stdout.splitlines():
        if PREFIX not in linha:
            continue
        nome = linha.split(",")[0].strip('"')
        subprocess.run(["schtasks", "/Delete", "/TN", nome, "/F"],
                       capture_output=True)
        print(f"[removida] {nome}")
        removidas += 1
    if removidas == 0:
        print("Nenhuma tarefa MinutoReal encontrada.")


def cmd_listar() -> None:
    r = subprocess.run(
        ["schtasks", "/Query", "/FO", "LIST"],
        capture_output=True, text=True,
    )
    blocos = r.stdout.split("\n\n")
    encontrados = [b for b in blocos if PREFIX in b]
    if not encontrados:
        print("Nenhuma tarefa MinutoReal ativa.")
        return
    for b in encontrados:
        print(b.strip())
        print()


def main(argv: list[str]) -> int:
    modos = {"--dry-run", "--criar", "--limpar", "--listar"}
    modo = next((a for a in argv if a in modos), None)
    if not modo:
        print(f"Uso: python agendador.py [{' | '.join(sorted(modos))}]")
        return 1

    if modo == "--limpar":
        cmd_limpar()
        return 0
    if modo == "--listar":
        cmd_listar()
        return 0

    fila = _ler_fila()
    hoje = date.today()
    if modo == "--dry-run":
        cmd_dry_run(fila, hoje)
    elif modo == "--criar":
        cmd_criar(fila, hoje)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
