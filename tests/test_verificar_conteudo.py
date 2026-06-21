import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import verificar_conteudo as vc


# ---------------------------------------------------------------------------
# _load_skill
# ---------------------------------------------------------------------------

def test_load_skill_retorna_conteudo():
    """Skill conhecida deve retornar texto com mais de 100 chars e conter 'hábito'/'habito'."""
    texto = vc._load_skill("habitos-atomicos")
    assert len(texto) > 100, f"Esperado >100 chars, obtido {len(texto)}"
    assert "hábito" in texto.lower() or "habito" in texto.lower(), (
        "Texto não contém 'hábito' ou 'habito'"
    )


def test_load_skill_inexistente():
    """Slug que não existe deve devolver string vazia."""
    assert vc._load_skill("xyz-inexistente") == ""


# ---------------------------------------------------------------------------
# _load_skill_chapter
# ---------------------------------------------------------------------------

def test_load_skill_chapter_zero():
    """Capítulo 0 de skill conhecida deve retornar texto com mais de 50 chars."""
    texto = vc._load_skill_chapter("habitos-atomicos", 0)
    assert len(texto) > 50, f"Esperado >50 chars, obtido {len(texto)}"


def test_load_skill_chapter_fora_idx():
    """Índice inexistente deve devolver string vazia."""
    assert vc._load_skill_chapter("habitos-atomicos", 999) == ""


# ---------------------------------------------------------------------------
# _parse_json
# ---------------------------------------------------------------------------

def test_parse_json_valido():
    """JSON limpo deve ser parseado em dict."""
    src = '{"cards": [], "lessons": [], "mudancas": []}'
    resultado = vc._parse_json(src)
    assert resultado == {"cards": [], "lessons": [], "mudancas": []}


def test_parse_json_markdown():
    """JSON envolto em bloco markdown deve ser extraído e parseado."""
    src = '```json\n{"a": 1}\n```'
    assert vc._parse_json(src) == {"a": 1}


def test_parse_json_invalido():
    """Texto que não é JSON deve retornar None."""
    assert vc._parse_json("nao e json") is None


# ---------------------------------------------------------------------------
# _replace_in_py
# ---------------------------------------------------------------------------

def test_replace_in_py_substitui():
    """Substituição simples deve retornar True e novo texto."""
    src = '"b": "texto original"'
    changed, novo = vc._replace_in_py(src, "texto original", "texto novo")
    assert changed is True
    assert "texto novo" in novo
    assert "texto original" not in novo


def test_replace_in_py_sem_mudanca():
    """old == new não deve produzir mudança."""
    src = '"b": "igual"'
    changed, novo = vc._replace_in_py(src, "igual", "igual")
    assert changed is False
    assert novo == src


def test_replace_in_py_com_html():
    """Deve substituir strings que contêm tags HTML."""
    src = '"desc": "<b>antigo</b>"'
    changed, novo = vc._replace_in_py(src, "<b>antigo</b>", "<b>novo</b>")
    assert changed is True
    assert "<b>novo</b>" in novo


def test_replace_in_py_nao_encontrada():
    """old ausente do src não deve alterar nada."""
    src = '"b": "texto original"'
    changed, novo = vc._replace_in_py(src, "fantasma", "qualquer coisa")
    assert changed is False
    assert novo == src
