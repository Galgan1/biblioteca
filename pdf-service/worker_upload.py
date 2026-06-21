# -*- coding: utf-8 -*-
"""worker_upload.py — drena a fila de uploads de livro, UM job por execução.

    python worker_upload.py

One-shot por design: pega o job `queued` mais antigo em UPLOAD_DIR, processa-o
e sai. Quem repete é o cron/systemd (nada de laço infinito aqui). Idempotente:
se não há job queued, sai 0 sem efeito.

Fluxo de um job (UPLOAD_DIR/<jobId>/ com job.json + source.<ext>):
  1. marca status 'processing';
  2. deriva o slug (job.json.slug, senão o nome do arquivo de origem);
  3. renderiza runbook_upload.md trocando {SLUG} e {SOURCE_FILE};
  4. chama `claude -p` (prompt no stdin) com cwd=raiz do projeto e SEM
     credencial de deploy/git no env — o agente só produz a skill + o
     `<slug>_data.py` (NÃO publica);
  5. roda `python data_gate.py <slug>` — se reprovar, status 'failed' + a saída
     do gate, e PARA (não publica);
  6. se passar, roda a publicação DETERMINÍSTICA, FORA do agente:
       python publicar_livro.py <slug> --deploy
       python afiliados/gerar_links.py
       python afiliados/inserir_botao.py
  7. sucesso -> status 'done' + url.

Toda saída (stdout/stderr) de cada subprocesso é capturada em arquivos dentro
da pasta do job (agent.out, gate.out, publicar.out, afiliados.out).

FRONTEIRA DE SEGURANÇA: a chamada `claude -p` roda com um env LIMPO (sem chaves
SSH/deploy/git/tokens). Os passos de deploy rodam aqui, no worker — nunca dentro
do agente.
"""
import json
import os
import subprocess
import sys

try:  # console Windows é cp1252 — força UTF-8
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:  # noqa: BLE001
    pass

# pdf-service/ e a raiz do projeto (um nível acima).
AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)

# Mesma pasta-raiz de jobs que o upload.js usa (sobrescrevível por env).
UPLOAD_DIR = os.environ.get("UPLOAD_DIR", "/opt/biblioteca-pdf/uploads")
RUNBOOK = os.path.join(AQUI, "runbook_upload.md")

# Ambiente de BUILD (clone do projeto Python na VPS): o agente autora o
# <slug>_data.py AQUI e o build roda AQUI (STAGING). O deploy para o site é
# separado (portão humano via publish_to_live.py), nunca pelo worker/agente.
BUILD_DIR = os.environ.get("BUILD_DIR", "/opt/biblioteca-build")

# Timeout generoso p/ a conversão book-to-skill + autoria do _data.py.
AGENT_TIMEOUT = int(os.environ.get("AGENT_TIMEOUT", "1800"))

# Variáveis de ambiente removidas do env do AGENTE (fronteira de segurança):
# nenhuma credencial de deploy/git/token deve vazar para dentro do `claude -p`.
ENV_SENSIVEL = (
    "SSH_AUTH_SOCK", "SSH_AGENT_PID", "GIT_SSH", "GIT_SSH_COMMAND",
    "GITHUB_TOKEN", "GH_TOKEN", "DEPLOY_KEY", "VPS_KEY",
)


def _ler_job(job_dir):
    with open(os.path.join(job_dir, "job.json"), encoding="utf-8") as f:
        return json.load(f)


def _gravar_job(job_dir, job):
    with open(os.path.join(job_dir, "job.json"), "w", encoding="utf-8") as f:
        json.dump(job, f, ensure_ascii=False, indent=2)


def _proximo_queued():
    """Pasta do job 'queued' mais antigo (jobId é <timestamp>-..., ordenável)."""
    if not os.path.isdir(UPLOAD_DIR):
        return None
    for nome in sorted(os.listdir(UPLOAD_DIR)):
        job_dir = os.path.join(UPLOAD_DIR, nome)
        jpath = os.path.join(job_dir, "job.json")
        if not os.path.isfile(jpath):
            continue
        try:
            job = _ler_job(job_dir)
        except Exception:  # noqa: BLE001
            continue
        if job.get("status") == "queued":
            return job_dir
    return None


def _derivar_slug(job, job_dir):
    """slug do job.json; senão do nome do arquivo de origem (source.<ext>)."""
    slug = (job.get("slug") or "").strip()
    if slug:
        return slug
    src = job.get("file") or ""
    base = os.path.splitext(os.path.basename(src))[0]
    # vazio (sem file) ou "source.<ext>" não dizem o nome → cai no jobId (nunca slug "")
    if not base or base.lower() == "source":
        return os.path.basename(job_dir)
    return base


def _env_agente():
    """Cópia do env SEM as credenciais de deploy/git (fronteira de segurança)."""
    env = dict(os.environ)
    for k in ENV_SENSIVEL:
        env.pop(k, None)
    return env


def _rodar(cmd, cwd, out_path, env=None, timeout=None, stdin_text=None):
    """Roda um subprocesso, captura stdout+stderr em out_path. Devolve returncode."""
    try:
        r = subprocess.run(
            cmd, cwd=cwd, env=env, input=stdin_text,
            capture_output=True, text=True, encoding="utf-8",
            errors="replace", timeout=timeout, shell=isinstance(cmd, str))
    except subprocess.TimeoutExpired as e:
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(f"TIMEOUT após {timeout}s\n{e}\n")
        return 124
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(r.stdout or "")
        if r.stderr:
            f.write("\n--- stderr ---\n")
            f.write(r.stderr)
    return r.returncode


def _resumo(slug):
    """Resumo do livro staged (título/autor/nº capítulos/capa) p/ a tela de revisão.
    Importa o <slug>_data.py direto do build env (sem mexer em sys.path global)."""
    try:
        import importlib.util
        nome = slug.replace("-", "_") + "_data"
        path = os.path.join(BUILD_DIR, nome + ".py")
        spec = importlib.util.spec_from_file_location(nome, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        b = getattr(mod, "BOOK", {})
        return {"title": b.get("title"), "author": b.get("author"),
                "chapters": len(getattr(mod, "CHAPTERS", [])), "cover": bool(b.get("cover"))}
    except Exception as e:  # noqa: BLE001
        return {"error": str(e)}


def processar(job_dir):
    job = _ler_job(job_dir)
    slug = _derivar_slug(job, job_dir)
    job["slug"] = slug
    job["status"] = "processing"
    job["stage"] = "ia"  # passo descritivo p/ a barra de progresso do frontend
    _gravar_job(job_dir, job)
    print(f"[worker] job {os.path.basename(job_dir)} -> slug {slug!r} (processing)")

    # --- caminho do arquivo de origem (source.<ext>) ---
    source_file = os.path.join(job_dir, job.get("file") or f"source{job.get('ext', '')}")

    # --- 1) renderiza o runbook com os placeholders literais ---
    with open(RUNBOOK, encoding="utf-8") as f:
        prompt = f.read()
    # {SLUG_UNDER} = slug com underscore (nome de módulo Python; o arquivo de
    # conteúdo é <slug_under>_data.py). Substituído ANTES de {SLUG}.
    prompt = (prompt
              .replace("{SLUG_UNDER}", slug.replace("-", "_"))
              .replace("{SLUG}", slug)
              .replace("{SOURCE_FILE}", source_file))

    # --- 2) chama o agente (claude -p) — env SEM credencial, cwd = raiz ---
    print("[worker] chamando o agente (claude -p) — sem credencial de deploy/git, no build env")
    # --permission-mode acceptEdits + a política .claude/settings.json (allow/deny)
    # = age sozinho dentro dos limites, sem YOLO (constituição Akita pilar 8).
    rc = _rodar("claude -p --permission-mode acceptEdits", cwd=BUILD_DIR,
                out_path=os.path.join(job_dir, "agent.out"),
                env=_env_agente(), timeout=AGENT_TIMEOUT, stdin_text=prompt)
    if rc != 0:
        job["status"] = "failed"
        job["error"] = f"agente falhou (rc={rc}); ver agent.out"
        _gravar_job(job_dir, job)
        print(f"[worker] FALHOU: agente rc={rc}")
        return

    # --- 3) PORTÃO: data_gate.py — sem verde, não publica ---
    job["stage"] = "gate"; _gravar_job(job_dir, job)
    print("[worker] portão: data_gate.py (no build env)")
    gate_out = os.path.join(job_dir, "gate.out")
    rc = _rodar([sys.executable, "data_gate.py", slug],
                cwd=BUILD_DIR, out_path=gate_out)
    if rc != 0:
        motivos = ""
        try:
            with open(gate_out, encoding="utf-8") as f:
                motivos = f.read().strip()
        except Exception:  # noqa: BLE001
            pass
        job["status"] = "failed"
        job["error"] = f"data_gate reprovou:\n{motivos}"
        _gravar_job(job_dir, job)
        print(f"[worker] FALHOU no portão (rc={rc}) — NÃO publica")
        return

    # --- 4) build DETERMINÍSTICO no STAGING (build env), SEM deploy ---
    # publicar_livro (sem --deploy) gera página+capa+retrofit+afiliado+kit DENTRO
    # do build env. NÃO copia p/ o site — isso é o portão humano (publish_to_live).
    job["stage"] = "build"; _gravar_job(job_dir, job)
    print("[worker] build staging — publicar_livro (sem --deploy)")
    rc = _rodar([sys.executable, "publicar_livro.py", slug],
                cwd=BUILD_DIR, out_path=os.path.join(job_dir, "publicar.out"))
    if rc != 0:
        job["status"] = "failed"
        job["error"] = f"publicar_livro (staging) falhou (rc={rc}); ver publicar.out"
        _gravar_job(job_dir, job)
        print(f"[worker] FALHOU no build staging (rc={rc})")
        return

    # --- 5) PRONTO p/ revisão (portão humano) — NÃO publica ---
    job["status"] = "ready"
    job["stage"] = "ready"
    job["summary"] = _resumo(slug)
    job.pop("error", None)
    _gravar_job(job_dir, job)
    print(f"[worker] READY (staged) — aguardando aprovação do admin: {slug}")


def main():
    job_dir = _proximo_queued()
    if not job_dir:
        print("[worker] nenhum job 'queued' — nada a fazer.")
        return
    processar(job_dir)


if __name__ == "__main__":
    main()
