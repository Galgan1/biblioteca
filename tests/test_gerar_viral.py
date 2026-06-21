import sys
import json
import importlib
import pytest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

# Importação adiada: gerar_viral.py ainda não existe (red → green).
# Cada teste que precisa do módulo captura o ImportError e pula.
try:
    import gerar_viral as gv
    _HAS_MODULE = True
except ImportError:
    gv = None
    _HAS_MODULE = False


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _skip_sem_modulo():
    if not _HAS_MODULE:
        pytest.skip("gerar_viral.py ainda não existe")


# ---------------------------------------------------------------------------
# 1. Carregamento de capítulo da skill
# ---------------------------------------------------------------------------

def test_load_skill_chapter_habitos_atomicos_zero():
    """_load_skill_chapter retorna texto com >50 chars para capítulo 0 existente."""
    _skip_sem_modulo()
    texto = gv._load_skill_chapter("habitos-atomicos", 0)
    assert isinstance(texto, str), "deve retornar str"
    assert len(texto) > 50, f"texto muito curto ({len(texto)} chars)"


def test_load_skill_chapter_idx_inexistente():
    """Índice fora do range retorna string vazia."""
    _skip_sem_modulo()
    resultado = gv._load_skill_chapter("habitos-atomicos", 999)
    assert resultado == "", f"esperado '', obtido {resultado!r}"


def test_load_skill_chapter_slug_inexistente():
    """Slug que não existe retorna string vazia."""
    _skip_sem_modulo()
    resultado = gv._load_skill_chapter("xyz-livro-fantasma", 0)
    assert resultado == "", f"esperado '', obtido {resultado!r}"


# ---------------------------------------------------------------------------
# 2. Estrutura do módulo — callables obrigatórios
# ---------------------------------------------------------------------------

def test_viral_tem_funcoes_publicas():
    """Módulo deve expor run_viral, _melhorar_chapter, _julgar_chapter, _load_skill_chapter."""
    _skip_sem_modulo()
    for nome in ("run_viral", "_melhorar_chapter", "_julgar_chapter", "_load_skill_chapter"):
        assert hasattr(gv, nome), f"falta '{nome}' em gerar_viral"
        assert callable(getattr(gv, nome)), f"'{nome}' não é callable"


# ---------------------------------------------------------------------------
# 3. viral.json — estrutura quando já rodou antes (skip se não existir)
# ---------------------------------------------------------------------------

def test_viral_relatorio_estrutura():
    """viral.json (se existir) deve ter campos slug, aprovados, total, capitulos."""
    caminho = Path("assets/kit/habitos-atomicos/viral.json")
    if not caminho.exists():
        pytest.skip("viral.json não existe ainda — rode run_viral primeiro")

    dados = json.loads(caminho.read_text(encoding="utf-8"))

    for campo in ("slug", "aprovados", "total", "capitulos"):
        assert campo in dados, f"campo '{campo}' ausente em viral.json"

    # total deve bater com o número de capítulos do livro
    data_mod = importlib.import_module("habitos_atomicos_data")
    assert dados["total"] == len(data_mod.CHAPTERS), (
        f"total={dados['total']} != {len(data_mod.CHAPTERS)} capítulos"
    )

    # capitulos deve ser lista
    assert isinstance(dados["capitulos"], list), "'capitulos' deve ser lista"


# ---------------------------------------------------------------------------
# 4. Prompt puro — _prompt_melhorar inclui skill_ref
# ---------------------------------------------------------------------------

def test_prompt_melhorar_inclui_skill_ref():
    """_prompt_melhorar (se existir) deve embutir o texto de skill_ref no prompt."""
    _skip_sem_modulo()
    if not hasattr(gv, "_prompt_melhorar"):
        pytest.skip("_prompt_melhorar não exposta como função pura")

    data = importlib.import_module("habitos_atomicos_data")
    ch = data.CHAPTERS[0]
    skill_ref = "TRECHO DE SKILL DE REFERÊNCIA ÚNICO_XYZ"
    prompt = gv._prompt_melhorar(ch, skill_ref, feedback="melhorar tom")

    assert isinstance(prompt, str), "_prompt_melhorar deve retornar str"
    assert skill_ref in prompt, "skill_ref deve aparecer literalmente no prompt"
    assert len(prompt) > 100, "prompt muito curto para ser útil"


# ---------------------------------------------------------------------------
# 5. Prompt puro — _prompt_julgar inclui book_title
# ---------------------------------------------------------------------------

def test_prompt_julgar_inclui_book_title():
    """_prompt_julgar (se existir) deve embutir o título do livro no prompt."""
    _skip_sem_modulo()
    if not hasattr(gv, "_prompt_julgar"):
        pytest.skip("_prompt_julgar não exposta como função pura")

    data = importlib.import_module("habitos_atomicos_data")
    ch = data.CHAPTERS[0]
    titulo = data.BOOK["title"]
    prompt = gv._prompt_julgar(ch, titulo)

    assert isinstance(prompt, str), "_prompt_julgar deve retornar str"
    assert titulo in prompt, "book_title deve aparecer no prompt"
    assert len(prompt) > 50, "prompt muito curto"
