# -*- coding: utf-8 -*-
"""
gerar_viral.py <slug>       — avalia viralidade (relatorio)
gerar_viral.py <slug> --fix — aplica melhorias no _data.py
"""
import sys, json, shutil, importlib.util, subprocess
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BASE   = Path(__file__).parent
SKILLS = Path.home() / ".claude" / "skills"

from verificar_conteudo import _replace_in_py, _validate_importable, _parse_json


def _load_skill_chapter(slug: str, idx: int) -> str:
    ch_dir = SKILLS / slug / "chapters"
    if not ch_dir.is_dir():
        return ""
    files = sorted(f for f in ch_dir.iterdir() if f.suffix == ".md")
    return files[idx].read_text(encoding="utf-8", errors="replace") if idx < len(files) else ""


def _call_claude(prompt: str, model: str = "claude-sonnet-4-6", timeout: int = 180) -> str | None:
    r = subprocess.run(
        f"claude -p --model {model}",
        input=prompt, capture_output=True, text=True,
        shell=True, encoding="utf-8", errors="replace", timeout=timeout,
    )
    out = (r.stdout or "").strip()
    if r.returncode != 0 or not out:
        err = (r.stderr or r.stdout or "").strip()
        if err:
            print(f"    AVISO claude ({model}): {err[:120]}")
    return out or None


def _melhorar_chapter(ch: dict, skill_ref: str, feedback: str = "") -> dict | None:
    cards_json   = json.dumps(ch.get("cards", []),   ensure_ascii=False, indent=2)
    lessons_json = json.dumps(ch.get("lessons", []), ensure_ascii=False, indent=2)
    feedback_block = (
        f"FEEDBACK DO JUIZ (na tentativa anterior):\n{feedback}"
        if feedback else ""
    )
    prompt = (
        "Você é CRIADOR DE CONTEÚDO VIRAL especialista em livros de não-ficção no Instagram brasileiro.\n\n"
        "MISSÃO: Reescreva os cards e lições para viralidade MÁXIMA no Instagram, sem distorcer o que o autor defendeu.\n\n"
        f"REFERÊNCIA DO AUTOR (respeite sempre):\n{skill_ref}\n\n"
        f"CAPÍTULO: \"{ch.get('sub', '')}\"\n"
        f"LIVRO: \"{ch.get('title', '')}\"\n\n"
        f"CONTEÚDO ATUAL:\ncards: {cards_json}\nlessons: {lessons_json}\n\n"
        "REGRAS DE VIRALIDADE (todas obrigatórias para 9/10):\n"
        "- Card 1: crie uma LACUNA DE CURIOSIDADE — revele que existe algo que o leitor não sabe\n"
        "  e que vai mudar como ele age. Não afirmação ousada — PERGUNTA IMPLÍCITA que obriga a deslizar.\n"
        "  Exemplos bons: 'A regra que separa quem termina os hábitos de quem desiste no dia 3',\n"
        "  'O erro que 97% das pessoas cometem ao tentar mudar'\n"
        "  Exemplos ruins: 'Hábitos são importantes' / 'Você precisa mudar sua rotina'\n"
        "- Cada card: UM insight contra-intuitivo + número concreto ou exemplo específico\n"
        "  (não conceito abstrato). Máx 50 palavras no campo \"b\".\n"
        "- Inclua ao menos 1 gancho de comentário/salvamento: pergunta divisiva ou 'qual desses é você?'\n"
        "  Pode ser no último card ou numa lesson.\n"
        "- Lessons: frases de alta densidade semântica que alguém encaminharia no WhatsApp.\n"
        "  Prefira concretude: 'A identidade antecede o hábito' > 'Você precisa mudar quem você é'\n"
        "- Tom: voz de áudio de WhatsApp — zero anglicismo, zero pt-PT, zero academicismo.\n"
        "- Mantenha TODOS os campos dos cards (ic, t, emph, b, tip, warn, wide — todos).\n\n"
        f"{feedback_block}\n\n"
        "Retorne APENAS JSON válido (sem markdown):\n"
        "{\"cards\": [...], \"lessons\": [...], \"mudancas\": [\"o que mudou\"]}"
    )
    return _parse_json(_call_claude(prompt))


def _julgar_chapter(ch: dict, book_title: str) -> dict | None:
    cards_json   = json.dumps(ch.get("cards", []),   ensure_ascii=False, indent=2)
    lessons_json = json.dumps(ch.get("lessons", []), ensure_ascii=False, indent=2)
    prompt = (
        "Você é JUIZ DE VIRALIDADE do Instagram, especialista em crescimento orgânico no nicho de livros de não-ficção em pt-BR.\n\n"
        "ÂNCORAS DE CALIBRAÇÃO:\n"
        "Exemplo 6/10 (não vira): 'Hábitos são importantes para sua vida. Aprenda a criá-los com consistência.' — verdadeiro mas óbvio.\n"
        "Exemplo 9/10 (vira): 'A regra dos 2 minutos: qualquer hábito que leva menos de 2 minutos para começar, você não tem desculpa para não fazer agora.' — específico, acionável, surpreendente.\n\n"
        "CRITÉRIOS (avalie 1 a 10 em CADA critério; score final = média arredondada):\n"
        "C1. LACUNA DE CURIOSIDADE no card 1: o título abre uma pergunta implícita que obriga a deslizar?\n"
        "    (9: sim, para o scroll; 5: afirma algo ousado mas não abre lacuna; 1: genérico)\n"
        "C2. CONTRA-INTUIÇÃO: há pelo menos 2 cards com insight que contradiz o senso comum?\n"
        "    (9: mínimo 2 insights que surpreendem; 5: apenas 1; 1: todos óbvios)\n"
        "C3. GANCHO DE COMENTÁRIO/SALVAMENTO: há uma pergunta divisiva, 'qual desses é você?' ou lista-referência?\n"
        "    (9: gancho explícito que força resposta; 5: implícito; 1: ausente)\n"
        "C4. LESSONS COMPARTILHÁVEIS: as lições são frases que alguém encaminharia no WhatsApp?\n"
        "    (9: todas densas e memoráveis; 5: algumas; 1: genéricas)\n"
        "C5. TOM pt-BR: zero anglicismo, zero pt-PT, voz de WhatsApp, zero academicismo?\n"
        "    (9: 100% correto; 5: alguns deslizes; 1: acadêmico ou pt-PT)\n"
        "C6. VETO DE FIDELIDADE: algum card distorce ou contradiz a referência do autor?\n"
        "    (se sim: score FINAL máximo = 4, independente dos outros critérios)\n\n"
        "APROVADO se score final >= 9 E C6 não acionou veto.\n\n"
        "CONTEÚDO A JULGAR:\n"
        f"Livro: \"{book_title}\"\n"
        f"Capítulo: \"{ch.get('sub', '')}\"\n"
        f"cards: {cards_json}\nlessons: {lessons_json}\n\n"
        "Responda APENAS JSON válido (sem markdown):\n"
        "{\"c1\": N, \"c2\": N, \"c3\": N, \"c4\": N, \"c5\": N, \"c6_veto\": false, "
        "\"score\": N, \"aprovado\": bool, \"feedback\": \"...\", \"pontos_fracos\": [\"...\"]}"
    )
    raw = _parse_json(_call_claude(prompt, model="claude-opus-4-8", timeout=240))
    if raw is None:
        return None
    # garantir portão de veto e score >= 9 como condição de aprovação (não confiar no campo do Claude)
    veto = bool(raw.get("c6_veto"))
    score = int(raw.get("score", 0))
    if veto:
        raw["score"] = min(score, 4)
        raw["aprovado"] = False
    else:
        raw["aprovado"] = raw["score"] >= 9
    return raw


def _load_data(slug: str):
    mod_name = slug.replace("-", "_") + "_data"
    path     = BASE / (mod_name + ".py")
    if not path.exists():
        raise FileNotFoundError(f"Não encontrado: {path}")
    spec = importlib.util.spec_from_file_location(mod_name, path)
    mod  = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.CHAPTERS, path


def _apply_viral_fixes(py_path: Path, chapters_orig: list, results: list) -> int:
    bak = py_path.with_suffix(".py.bak")
    shutil.copy2(py_path, bak)
    src   = py_path.read_text(encoding="utf-8", errors="replace")
    total = 0
    for orig_ch, res in zip(chapters_orig, results):
        if not res:
            continue
        new_ch = res.get("best_ch") or {}
        for oc, nc in zip(orig_ch.get("cards", []), new_ch.get("cards", [])):
            for field in ("b", "tip", "t"):
                ov, nv = oc.get(field, ""), nc.get(field, "")
                if ov and nv and ov != nv:
                    changed, src = _replace_in_py(src, ov, nv)
                    if changed:
                        total += 1
        for ov, nv in zip(orig_ch.get("lessons", []), new_ch.get("lessons", [])):
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


def run_viral(slug: str, ch_idx: int | None = None, fix: bool = False, max_iter: int = 5) -> dict:
    print(f"\n=== gerar_viral: {slug} ({'fix' if fix else 'relatorio'}) ===\n")

    try:
        chapters, py_path = _load_data(slug)
    except FileNotFoundError as e:
        print(f"ERRO: {e}")
        return {"slug": slug, "erro": str(e)}

    book_title = chapters[0].get("title", slug) if chapters else slug
    indices = [ch_idx] if ch_idx is not None else list(range(len(chapters)))

    cap_results = []   # per-chapter outcome for final JSON
    fix_data    = []   # (orig_ch, best_ch) pairs for --fix

    for idx in indices:
        if idx >= len(chapters):
            print(f"  [ch{idx+1}] índice fora do intervalo — pulando")
            continue
        ch       = chapters[idx]
        sub      = ch.get("sub", f"ch{idx+1}")
        skill_ref = _load_skill_chapter(slug, idx) or ""

        feedback  = ""
        best_ch   = None
        best_score = 0
        tentativas = 0

        for tentativa in range(max_iter):
            result = _melhorar_chapter(ch, skill_ref, feedback)
            if not result:
                print(f"  [ch{idx+1}] tentativa {tentativa+1}: sem resposta do executor")
                break

            # merge structure so julgar sees full chapter
            candidate = dict(ch)
            candidate["cards"]   = result.get("cards",   ch.get("cards", []))
            candidate["lessons"] = result.get("lessons", ch.get("lessons", []))

            veredicto = _julgar_chapter(candidate, book_title)
            if not veredicto:
                print(f"  [ch{idx+1}] tentativa {tentativa+1}: sem resposta do juiz")
                break

            score    = veredicto.get("score", 0)
            aprovado = veredicto.get("aprovado", False)
            tentativas += 1
            print(f"  [ch{idx+1}] tentativa {tentativa+1}: score {score}/10 — {'APROVADO' if aprovado else 'reprovado'}")

            if score > best_score:
                best_score = score
                best_ch    = candidate

            if aprovado:
                break
            feedback = veredicto.get("feedback", "")

        cap_results.append({
            "sub":       sub,
            "score":     best_score,
            "tentativas": tentativas,
            "best_ch":   best_ch,
        })
        # portão: só aplica fix quando aprovado (score >= 9); senão mantém original
        apply = best_ch if (best_ch and best_score >= 9) else None
        fix_data.append((ch, {"best_ch": apply} if apply else None))

    aprovados = sum(1 for r in cap_results if r["score"] >= 9)
    report = {
        "slug":      slug,
        "aprovados": aprovados,
        "total":     len(cap_results),
        "capitulos": [{"sub": r["sub"], "score": r["score"], "tentativas": r["tentativas"]}
                      for r in cap_results],
    }

    report_dir = BASE / "assets" / "kit" / slug
    report_dir.mkdir(parents=True, exist_ok=True)
    rp = report_dir / "viral.json"
    rp.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nRelatório salvo em: {rp}")
    print(f"RESUMO: {aprovados}/{len(cap_results)} capítulos aprovados (≥9/10).")

    if fix and fix_data:
        orig_chs  = [pair[0] for pair in fix_data]
        res_items = [pair[1] for pair in fix_data]
        total_fixed = _apply_viral_fixes(py_path, orig_chs, res_items)
        print(f"Fix: {total_fixed} campo(s) substituído(s) em {py_path.name}")
        if total_fixed:
            print(f"Backup salvo em {py_path.with_suffix('.py.bak').name}")

    return report


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        print("Uso: gerar_viral.py <slug> [--fix]")
        sys.exit(0)
    run_viral(args[0], fix="--fix" in args)
