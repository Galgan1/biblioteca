# -*- coding: utf-8 -*-
"""
verificar_conteudo.py <slug>        — relatório (só lê, exit 0)
verificar_conteudo.py <slug> --fix  — corrige _data.py + backup .py.bak (exit 0)
"""
import sys, json, shutil, importlib.util, subprocess, re
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BASE   = Path(__file__).parent
SKILLS = Path.home() / ".claude" / "skills"


def _load_skill(slug: str) -> str:
    """Devolve todo o conteudo da skill como string (SKILL.md + chapters)."""
    sd = SKILLS / slug
    if not sd.exists():
        return ""
    parts = []
    main = sd / "SKILL.md"
    if main.exists():
        parts.append(main.read_text(encoding="utf-8", errors="replace"))
    ch_dir = sd / "chapters"
    if ch_dir.is_dir():
        for f in sorted(ch_dir.iterdir()):
            if f.suffix == ".md":
                parts.append(f"=== {f.name} ===\n" + f.read_text(encoding="utf-8", errors="replace"))
    return "\n\n".join(parts)


def _load_skill_chapter(slug: str, idx: int) -> str:
    """Carrega o arquivo de capitulo da skill pelo indice 0-based."""
    ch_dir = SKILLS / slug / "chapters"
    if not ch_dir.is_dir():
        return ""
    files = sorted(f for f in ch_dir.iterdir() if f.suffix == ".md")
    return files[idx].read_text(encoding="utf-8", errors="replace") if idx < len(files) else ""


def _parse_json(text: str) -> dict | None:
    """Extrai e parseia JSON da resposta do Claude (tolerante a markdown)."""
    if not text:
        return None
    txt = re.sub(r"^```(?:json)?\s*", "", text.strip())
    txt = re.sub(r"\s*```$", "", txt)
    m = re.search(r"\{.*\}", txt, re.S)
    if not m:
        return None
    try:
        return json.loads(m.group(0))
    except json.JSONDecodeError:
        return None


def _load_data(slug: str):
    mod_name = slug.replace("-", "_") + "_data"
    path     = BASE / (mod_name + ".py")
    if not path.exists():
        raise FileNotFoundError(f"Não encontrado: {path}")
    spec = importlib.util.spec_from_file_location(mod_name, path)
    mod  = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.CHAPTERS, path


def _ask_claude(prompt: str, timeout: int = 180) -> str | None:
    r = subprocess.run(
        "claude -p --model claude-sonnet-4-6",
        input=prompt, capture_output=True, text=True,
        shell=True, encoding="utf-8", errors="replace", timeout=timeout,
    )
    return (r.stdout or "").strip() or None


def _review_chapter(ch: dict, ref: str) -> dict | None:
    prompt = (
        "Você é REVISOR EDITORIAL de livros de não-ficção em pt-BR.\n\n"
        f"REFERÊNCIA CANÔNICA — o que o autor defende neste capítulo:\n{ref}\n\n"
        f"CAPÍTULO: \"{ch.get('sub', '')}\"\n\n"
        "Revise os CARDS e LIÇÕES. Para cada texto (campos \"b\", \"tip\", \"lessons\"):\n"
        "- Se contradiz ou distorce o autor → corrija usando só a referência\n"
        "- Se está em pt-PT (ex: \"utilizar\", \"efectivamente\", \"deve-se\") → converta p/ pt-BR\n"
        "- Se está correto e fiel → devolva IDÊNTICO\n\n"
        f"CARDS ATUAIS:\n{json.dumps(ch.get('cards', []), ensure_ascii=False, indent=2)}\n\n"
        f"LIÇÕES ATUAIS:\n{json.dumps(ch.get('lessons', []), ensure_ascii=False, indent=2)}\n\n"
        'Responda APENAS JSON válido (sem markdown):\n'
        '{\n'
        '  "cards": [/* mesma estrutura, todos os campos, textos corrigidos ou idênticos */],\n'
        '  "lessons": [/* lições corrigidas ou idênticas */],\n'
        '  "mudancas": ["o que mudou — lista vazia se nada mudou"]\n'
        '}\n\n'
        "REGRAS:\n"
        "- Preserve TODOS os campos dos cards (ic, t, emph, b, tip, warn, wide — tudo)\n"
        "- NÃO invente ideias ausentes da referência\n"
        "- Campo \"b\": máx 60 palavras\n"
        "- Não altere \"t\" (título) nem \"emph\" nem \"ic\" (salvo erro flagrante de pt-PT)"
    )
    raw = _ask_claude(prompt)
    return _parse_json(raw)


def _replace_in_py(src: str, old: str, new: str) -> tuple[bool, str]:
    """Substitui o valor de uma string Python no source. Retorna (changed, novo_src)."""
    if old == new or not old:
        return False, src
    old_dq = old.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n")
    new_dq = new.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n")
    if f'"{old_dq}"' in src:
        return True, src.replace(f'"{old_dq}"', f'"{new_dq}"', 1)
    old_sq = old.replace("\\", "\\\\").replace("'", "\\'").replace("\n", "\\n")
    new_sq = new.replace("\\", "\\\\").replace("'", "\\'").replace("\n", "\\n")
    if f"'{old_sq}'" in src:
        return True, src.replace(f"'{old_sq}'", f"'{new_sq}'", 1)
    return False, src


def _validate_importable(path: Path) -> bool:
    r = subprocess.run(
        [sys.executable, "-c",
         f"import importlib.util; s=importlib.util.spec_from_file_location('x',{str(path)!r});"
         "m=importlib.util.module_from_spec(s); s.loader.exec_module(m)"],
        capture_output=True, text=True,
    )
    return r.returncode == 0


def _apply_fixes(py_path: Path, chapters_orig: list, results: list) -> int:
    bak = py_path.with_suffix(".py.bak")
    shutil.copy2(py_path, bak)
    src   = py_path.read_text(encoding="utf-8", errors="replace")
    total = 0
    for orig_ch, res in zip(chapters_orig, results):
        if not res or not res.get("mudancas"):
            continue
        for oc, nc in zip(orig_ch.get("cards", []), res.get("cards", [])):
            for field in ("b", "tip"):
                ov, nv = oc.get(field, ""), nc.get(field, "")
                if ov and nv and ov != nv:
                    changed, src = _replace_in_py(src, ov, nv)
                    if changed:
                        total += 1
        for ov, nv in zip(orig_ch.get("lessons", []), res.get("lessons", [])):
            if ov and nv and ov != nv:
                changed, src = _replace_in_py(src, ov, nv)
                if changed:
                    total += 1
    py_path.write_text(src, encoding="utf-8")
    if not _validate_importable(py_path):
        shutil.copy2(bak, py_path)
        print("ERRO: arquivo corrigido não importável — backup restaurado.")
        return 0
    return total


def run(slug: str, fix: bool) -> None:
    print(f"\n=== verificar_conteudo: {slug} ({'fix' if fix else 'relatorio'}) ===\n")
    skill_full = _load_skill(slug)
    if not skill_full:
        print(f"ERRO: skill '{slug}' não encontrada em {SKILLS}"); return
    try:
        chapters, py_path = _load_data(slug)
    except FileNotFoundError as e:
        print(f"ERRO: {e}"); return

    results = []
    for i, ch in enumerate(chapters):
        sub = ch.get("sub", f"ch{i}")
        ref = _load_skill_chapter(slug, i) or skill_full[:4000]
        print(f"  [{i+1}/{len(chapters)}] {sub} … ", end="", flush=True)
        res = _review_chapter(ch, ref)
        results.append(res)
        if res is None:
            print("sem resposta do Claude")
        else:
            n = len(res.get("mudancas") or [])
            print(f"{n} mudança(s)")
            for msg in (res.get("mudancas") or []):
                print(f"      - {msg}")

    total_fixed = 0
    if fix:
        total_fixed = _apply_fixes(py_path, chapters, results)
        print(f"\nFix: {total_fixed} campo(s) substituído(s) em {py_path.name}")
        if total_fixed:
            print(f"Backup salvo em {py_path.with_suffix('.py.bak').name}")

    report_dir = BASE / "assets" / "kit" / slug
    report_dir.mkdir(parents=True, exist_ok=True)
    report = {
        "slug": slug, "fix": fix, "total_fixed": total_fixed,
        "chapters": [
            {"sub": chapters[i].get("sub"), "mudancas": (results[i] or {}).get("mudancas", [])}
            for i in range(len(chapters))
        ],
    }
    rp = report_dir / "verificacao.json"
    rp.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nRelatório salvo em: {rp}")
    total_changes = sum(len((r or {}).get("mudancas") or []) for r in results)
    print(f"\nRESUMO: {total_changes} mudança(s) detectada(s) em {len(chapters)} capítulo(s).")


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        print("Uso: verificar_conteudo.py <slug> [--fix]")
        sys.exit(0)
    run(args[0], "--fix" in args)
