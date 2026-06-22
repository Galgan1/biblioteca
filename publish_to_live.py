# -*- coding: utf-8 -*-
"""PORTAO DE PUBLICACAO — copia um livro JA construido do ambiente de build da
VPS para o site ao vivo. E o passo "publicar" (o portao humano) que roda DENTRO
da VPS: nao e scp, e copia local (shutil).

    python3 publish_to_live.py <slug> [--build-dir DIR] [--live-dir DIR]

Contexto: na VPS, `/opt/biblioteca-build/` roda `publicar_livro.py <slug>` (SEM
--deploy) e gera ali a pagina + capitulos + capa + kit + books.json. Este script
move o conjunto construido -> `/var/www/andregalgani/biblioteca/`.

O conjunto copiado espelha o que `publicar_livro.deploy()` envia por scp, mais os
extras combinados (OG e o KIT inteiro):
  - <slug>.html                                         (obrigatorio)
  - books.json                                          (obrigatorio)
  - pasta <slug>/ inteira (capitulos; JS unico compartilhado)
  - index.html, sitemap.xml, robots.txt                 (os que existirem)
  - assets/style.css, assets/script-livro.js, assets/favicon.svg
  - assets/<slug>-capa.png                              (capa de estante)
  - assets/<slug>-cover.png, assets/<slug>-og.png       (se existirem)
  - assets/kit/<slug>/ inteira (manifest.json, slides.json, caps.json)
  - assets/kit/_tpl/<slug>/ inteira
  - assets/kit/_carousel.css

Permissoes: 755 nas pastas, 644 nos arquivos — sem isso o nginx da 404.
"""
import os
import shutil
import stat
import sys

try:  # console do Windows e cp1252 — forca UTF-8 para nao quebrar nos acentos
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

BUILD_DEFAULT = os.environ.get("BUILD_DIR", "/opt/biblioteca-build")
LIVE_DEFAULT = os.environ.get("LIVE_DIR", "/var/www/andregalgani/biblioteca")


def _chmod_file(path):
    """644 no arquivo (rw-r--r--)."""
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


def _chmod_dir(path):
    """755 na pasta (rwxr-xr-x)."""
    os.chmod(path, (stat.S_IRWXU | stat.S_IRGRP | stat.S_IXGRP
                    | stat.S_IROTH | stat.S_IXOTH))


def _ensure_dir(path):
    """Cria a pasta-destino (e ancestrais) com 755 se ainda nao existir."""
    if not os.path.isdir(path):
        os.makedirs(path, exist_ok=True)
    _chmod_dir(path)


def copy_file(src, dst, copied, missing, *, required=False, label=None):
    """Copia src -> dst se src existir. Registra em copied/missing.

    Se required e a fonte faltar, encerra com erro claro.
    """
    name = label or os.path.basename(src)
    if not os.path.exists(src):
        if required:
            print(f"ERRO: fonte obrigatoria ausente: {src}")
            sys.exit(1)
        missing.append(name)
        return
    _ensure_dir(os.path.dirname(dst))
    shutil.copy2(src, dst)
    _chmod_file(dst)
    copied.append(name)


def copy_tree(src, dst, copied, missing, *, required=False, label=None):
    """Copia a pasta src -> dst inteira (idempotente). Registra em copied/missing.

    Reaplica 755/644 em tudo que aterrissar. Se required e faltar, erro claro.
    """
    name = label or (os.path.basename(src.rstrip("/\\")) + "/")
    if not os.path.isdir(src):
        if required:
            print(f"ERRO: pasta obrigatoria ausente: {src}")
            sys.exit(1)
        missing.append(name)
        return
    # dirs_exist_ok=True torna a copia idempotente (sobrescreve o conteudo).
    shutil.copytree(src, dst, dirs_exist_ok=True)
    _chmod_dir(dst)
    for root, dirs, files in os.walk(dst):
        for d in dirs:
            _chmod_dir(os.path.join(root, d))
        for f in files:
            _chmod_file(os.path.join(root, f))
    copied.append(name)


def publish(slug, build_dir, live_dir):
    """Copia o livro <slug> de build_dir -> live_dir. Devolve (copied, missing)."""
    b = lambda *p: os.path.join(build_dir, *p)   # caminho na build
    l = lambda *p: os.path.join(live_dir, *p)     # caminho no live

    if not os.path.isdir(build_dir):
        print(f"ERRO: build-dir nao existe: {build_dir}")
        sys.exit(1)

    _ensure_dir(live_dir)
    copied, missing = [], []

    # --- obrigatorios: a pagina e o catalogo ---
    copy_file(b(f"{slug}.html"), l(f"{slug}.html"), copied, missing, required=True)
    copy_file(b("books.json"), l("books.json"), copied, missing, required=True)

    # --- pasta do livro inteira: capitulos (o JS e o unico assets/script-livro.js) ---
    copy_tree(b(slug), l(slug), copied, missing, required=True, label=f"{slug}/")

    # --- raiz: opcionais "os que existirem" ---
    for f in ("index.html", "sitemap.xml", "robots.txt"):
        copy_file(b(f), l(f), copied, missing)

    # --- assets de marca (sempre presentes) + capas ---
    copy_file(b("assets", "style.css"), l("assets", "style.css"),
              copied, missing, label="assets/style.css")
    # JS unico compartilhado por TODAS as paginas (substitui as 103 copias por-livro)
    copy_file(b("assets", "script-livro.js"), l("assets", "script-livro.js"),
              copied, missing, label="assets/script-livro.js")
    copy_file(b("assets", "favicon.svg"), l("assets", "favicon.svg"),
              copied, missing, label="assets/favicon.svg")
    # -capa.png e a capa de estante (hibrida); -cover.png/-og.png podem faltar.
    copy_file(b("assets", f"{slug}-capa.png"), l("assets", f"{slug}-capa.png"),
              copied, missing, label=f"assets/{slug}-capa.png")
    copy_file(b("assets", f"{slug}-cover.png"), l("assets", f"{slug}-cover.png"),
              copied, missing, label=f"assets/{slug}-cover.png")
    copy_file(b("assets", f"{slug}-og.png"), l("assets", f"{slug}-og.png"),
              copied, missing, label=f"assets/{slug}-og.png")

    # --- KIT de divulgacao ---
    copy_tree(b("assets", "kit", slug), l("assets", "kit", slug),
              copied, missing, label=f"assets/kit/{slug}/")
    copy_tree(b("assets", "kit", "_tpl", slug), l("assets", "kit", "_tpl", slug),
              copied, missing, label=f"assets/kit/_tpl/{slug}/")
    copy_file(b("assets", "kit", "_carousel.css"),
              l("assets", "kit", "_carousel.css"),
              copied, missing, label="assets/kit/_carousel.css")

    return copied, missing


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = sys.argv[1:]
    if not args:
        print("uso: python3 publish_to_live.py <slug> [--build-dir DIR] [--live-dir DIR]")
        sys.exit(1)
    slug = args[0]

    def _opt(name, default):
        if name in flags:
            i = flags.index(name)
            if i + 1 < len(flags):
                return flags[i + 1]
            print(f"ERRO: {name} exige um valor.")
            sys.exit(1)
        return default

    build_dir = _opt("--build-dir", BUILD_DEFAULT)
    live_dir = _opt("--live-dir", LIVE_DEFAULT)

    print(f"[publish] {slug}: {build_dir} -> {live_dir}")
    copied, missing = publish(slug, build_dir, live_dir)

    print(f"\nOK: {len(copied)} item(ns) publicado(s):")
    for c in copied:
        print(f"  + {c}")
    if missing:
        print(f"\nAVISO: {len(missing)} opcional(is) ausente(s) (pulado):")
        for m in missing:
            print(f"  - {m}")
    print(f"\nOK: no ar -> {live_dir}/{slug}.html")
    sys.exit(0)


if __name__ == "__main__":
    main()
