#!/usr/bin/env python3
"""Contrato da lane Conversor Livro->Skill -- rede de seguranca (Akita pilar 2).

Um livro so esta "pronto" quando passa AQUI -- nao quando "a IA achou que esta
certo". Comando unico, output parseavel, sem setup humano.
Contrato completo em LANE-CONVERSOR-LIVRO-SKILL.md.

As skills vivem em ~/.claude/skills/<slug>/ (FORA do repo). Em CI esse diretorio
nao existe -> a checagem de skill e PULADA (skip != falha); o bridge
`<slug>_data.py` (no repo) roda sempre. Local valida o contrato inteiro.

Uso:
  python valida_skill_lane.py          # resumo legivel; exit 0 sse contrato cumprido
  python valida_skill_lane.py --json   # {"ok","checados","reprovados","detalhes"}
"""

import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SKILLS_DIR = Path(os.path.expanduser("~/.claude/skills"))
BOOKS_JSON = ROOT / "books.json"

# Mapa slug-do-site -> pasta-da-skill (quando divergem). FONTE UNICA do alias (DRY).
ALIAS_SLUG_SKILL = {
    "padrao-bitcoin": "ammous-padrao-bitcoin",
    "coesao-coerencia": "beaugrande-linguistica-textual",
    "audiovisao": "chion-audio-visao",
    "quem-mexeu-no-queijo": "johnson-queijo",
    "nacao-dopamina": "lembke-nacao-dopamina",
    "ponerologia": "lobaczewski-ponerologia",
    "smith-assertividade": "smith-assertiveness",
    "save-the-cat": "snyder-save-the-cat",
    "sound-design": "sonnenschein-sound-design",
    "story-mckee": "story-screenwriting",
    "jornada-do-escritor": "vogler-jornada-do-escritor",
}
# Excecoes EXPLICITAS do contrato (Akita: o contrato declara suas excecoes).
CATALOGO_NAO_LIVRO = {  # no books.json, mas NAO sao conversao desta lane
    "tjmg-regras-cartorios",  # provimento juridico (sem skill)
    "blender-fundamentals",
    "blender-manual",  # fontes de referencia do estudio,
    "blender-noob-to-pro",  # catalogadas por outra lane (sem skill de livro)
}
SKILL_ARQUIVO_UNICO = {"futebol-brasileiro"}  # SKILL.md robusto, sem multi-arquivo
SKILLS_FORA_DO_CATALOGO = {  # entregues skill-only (sem books.json)
    "pragmatic-programmer",
    "clean-code",
    "philosophy-software-design",
    "o-necromante",
    "neuromancer",
}

ARQUIVOS_APOIO = ("SKILL.md", "glossary.md", "patterns.md", "cheatsheet.md")
MOJIBAKE = re.compile(r"Ã[\x80-\xbf]|Â[\x80-\xbf]|ï¿½|�|â€™|â€œ")
TETO_CHARS_SKILL_MD = 24000  # ~6000 tokens: teto duro; alvo do contrato e < 4000 tokens
MIN_CHARS_SKILL_UNICO = 4000  # single-file so vale se for substancial


def icones_do_gerador() -> set[str]:
    """Chaves de icone validas = ICONS do gerador canonico (DRY, nao duplicar)."""
    import gerar_livro

    return set(gerar_livro.ICONS)


def slug_para_skill(slug: str) -> str:
    return ALIAS_SLUG_SKILL.get(slug, slug)


def slug_para_data(slug: str) -> Path:
    return ROOT / (slug.replace("-", "_") + "_data.py")


def livros_do_catalogo() -> list[str]:
    """Ids do books.json que sao livros de frameworks (devem ter skill)."""
    livros = json.loads(BOOKS_JSON.read_text(encoding="utf-8"))
    return [b["id"] for b in livros if b["id"] not in CATALOGO_NAO_LIVRO]


def checa_skill(slug: str) -> list[str]:
    """Valida o contrato da SKILL. Devolve problemas (lista vazia = ok)."""
    skill = slug_para_skill(slug)
    pasta = SKILLS_DIR / skill
    if not pasta.is_dir():
        return [f"pasta da skill ausente: {pasta}"]
    skill_md = pasta / "SKILL.md"
    if not skill_md.is_file():
        return ["SKILL.md ausente"]

    probs: list[str] = []
    txt = skill_md.read_text(encoding="utf-8")
    probs += _checa_frontmatter(txt, skill)
    probs += _checa_procedencia_e_glifos(pasta, txt)
    if len(txt) > TETO_CHARS_SKILL_MD:
        probs.append(
            f"SKILL.md acima do teto ({len(txt)} chars > {TETO_CHARS_SKILL_MD})"
        )

    if skill in SKILL_ARQUIVO_UNICO:
        if len(txt) < MIN_CHARS_SKILL_UNICO:
            probs.append("skill de arquivo unico curta demais")
        return probs
    probs += _checa_multiarquivo(pasta, txt)
    return probs


def _checa_frontmatter(txt: str, skill: str) -> list[str]:
    if not txt.startswith("---"):
        return ["sem frontmatter"]
    m = re.search(r"^name:\s*(\S+)", txt, re.M)
    probs = []
    if not m:
        probs.append("frontmatter sem name")
    elif m.group(1).strip() != skill:
        probs.append(f"name '{m.group(1).strip()}' != slug '{skill}'")
    if not re.search(r"^description:\s*\S", txt, re.M):
        probs.append("frontmatter sem description")
    return probs


def _checa_procedencia_e_glifos(pasta: Path, skill_md_txt: str) -> list[str]:
    arquivos = list(pasta.glob("*.md")) + list(pasta.glob("chapters/*.md"))
    probs = []
    if not any("Base:" in f.read_text(encoding="utf-8") for f in arquivos):
        probs.append("falta a linha de procedencia 'Base: ...'")
    sujos = [f.name for f in arquivos if MOJIBAKE.search(f.read_text(encoding="utf-8"))]
    if sujos:
        probs.append(f"mojibake em: {', '.join(sujos)}")
    return probs


def _checa_multiarquivo(pasta: Path, skill_md_txt: str) -> list[str]:
    probs = [f"falta {f}" for f in ARQUIVOS_APOIO if not (pasta / f).is_file()]
    caps = (
        list((pasta / "chapters").glob("*.md")) if (pasta / "chapters").is_dir() else []
    )
    if not caps:
        probs.append("chapters/ ausente ou vazio")
    for rel in re.findall(r"\]\((chapters/[^)#]+\.md)", skill_md_txt):
        if not (pasta / rel).is_file():
            probs.append(f"link quebrado no indice: {rel}")
    return probs


def checa_data(slug: str, icones: set[str]) -> list[str]:
    """Valida o bridge `<slug>_data.py` (no repo). Ausente = ok (nem todo livro tem)."""
    arq = slug_para_data(slug)
    if not arq.is_file():
        return []
    ns: dict = {}
    try:
        exec(compile(arq.read_text(encoding="utf-8"), str(arq), "exec"), ns)
    except Exception as e:  # noqa: BLE001 - queremos o contexto do erro
        return [f"data.py nao executa: {e}"]
    probs = []
    book, chapters = ns.get("BOOK"), ns.get("CHAPTERS")
    if not isinstance(book, dict):
        probs.append("data.py sem BOOK (dict)")
    else:
        faltam = {"title", "author", "cover"} - set(book)
        if faltam:
            probs.append(f"BOOK sem chaves: {sorted(faltam)}")
        cover = book.get("cover", "")
        if cover and not (ROOT / cover).is_file():
            probs.append(f"capa ausente: {cover}")
    if not isinstance(chapters, list) or not chapters:
        probs.append("data.py sem CHAPTERS (lista nao-vazia)")
    else:
        probs += _checa_icones(chapters, icones)
    return probs


def _checa_icones(chapters: list, icones: set[str]) -> list[str]:
    usados = {
        c.get("ic")
        for ch in chapters
        for c in ch.get("cards", [])
        if isinstance(c, dict)
    }
    invalidos = sorted(i for i in usados if i and i not in icones)
    return [f"icones fora do ICONS do gerador: {invalidos}"] if invalidos else []


def main(argv: list[str]) -> int:
    como_json = "--json" in argv
    skills_presentes = SKILLS_DIR.is_dir()
    icones = icones_do_gerador()

    alvos = sorted(set(livros_do_catalogo()) | SKILLS_FORA_DO_CATALOGO)
    reprovados: dict[str, list[str]] = {}  # DURO (contrato da skill) -> controla o exit
    avisos: dict[str, list[str]] = {}  # SOFT (bridge data.py / icones, lane do site)
    for slug in alvos:
        if skills_presentes and (probs := checa_skill(slug)):
            reprovados[slug] = probs
        if slug not in SKILLS_FORA_DO_CATALOGO and (warns := checa_data(slug, icones)):
            avisos[slug] = warns

    ok = not reprovados
    resumo = {
        "ok": ok,
        "checados": len(alvos),
        "reprovados": len(reprovados),
        "avisos": len(avisos),
        "skills_avaliadas": skills_presentes,
        "detalhes_reprovados": reprovados,
        "detalhes_avisos": avisos,
    }
    if como_json:
        print(json.dumps(resumo, ensure_ascii=False))
        return 0 if ok else 1

    modo = (
        "contrato da skill"
        if skills_presentes
        else "skills ausentes (so avisos de bridge)"
    )
    print(f"Lane Conversor Livro->Skill | {modo} | checados: {len(alvos)}")
    for slug, probs in sorted(reprovados.items()):
        print(f"  REPROVADO {slug}: {'; '.join(probs)}")
    for slug, warns in sorted(avisos.items()):
        print(f"  aviso     {slug}: {'; '.join(warns)}")
    veredito = (
        "VERDE: contrato da skill cumprido."
        if ok
        else f"VERMELHO: {len(reprovados)} reprovado(s)."
    )
    print(f"  >>> {veredito} ({len(avisos)} aviso(s) de bridge, nao bloqueiam)")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
