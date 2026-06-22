# -*- coding: utf-8 -*-
"""ORQUESTRADOR de publicacao de um livro na biblioteca — um comando, do
`<slug>_data.py` ao site verificado (e, opcionalmente, ao ar).

    python publicar_livro.py <slug>            # gera + capa + retrofit + verifica (local)
    python publicar_livro.py <slug> --check    # so valida o <slug>_data.py (nao escreve nada)
    python publicar_livro.py <slug> --deploy   # tudo acima + scp p/ VPS + chmod da pasta

Encadeia, na ordem certa e sem deixar esquecer nenhum passo:
  1. valida o schema do `<slug>_data.py`
  2. gera visao geral + capitulos + books.json   (gerar_livro; JS unico compartilhado)
  2b. gera kit de divulgacao (templates HTML para o admin do site)  (gerar_dados_kit)
  2c. gera dados de carrossel (slides.json + caps.json)             (gerar_dados_carrossel)
  2d. gera story PNGs com 4 frames (teaser+quote+insights+CTA)      (gerar_carrossel --stories)
  3. garante a capa (gera tipografica on-brand se faltar)     (gerar_capa)
  4. roda o retrofit (favicon, OG/Twitter, theme-color, nav nomeada, rodape)
  5. verifica: paginas existem + smoke no navegador
  6. [--deploy] sobe os arquivos do livro + assets e corrige a permissao da pasta
             + kit/_tpl/<slug>/ + assets/kit/<slug>/ + story PNGs para a VPS
"""
import importlib
import os
import subprocess
import sys

try:  # console do Windows e cp1252 — forca UTF-8 para nao quebrar nos acentos
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

BASE = os.path.dirname(os.path.abspath(__file__))
SKILL = os.path.join(os.path.expanduser("~"), ".claude", "skills", "run-biblioteca")
VPS = "root@andregalgani.com.br"
REMOTE = "/var/www/andregalgani/biblioteca"

REQ_BOOK = {"title", "author", "header_light", "header_bold", "intro", "description"}
REQ_CH = {"slug", "sub", "intro", "cards"}


def step(n, msg):
    print(f"\n[{n}] {msg}")


def fail(msg):
    print(f"ERRO: {msg}")
    sys.exit(1)


def validate(slug):
    """Carrega e valida o <slug>_data.py. Devolve (BOOK, CHAPTERS)."""
    mod_name = slug.replace("-", "_") + "_data"
    try:
        mod = importlib.import_module(mod_name)
    except ModuleNotFoundError:
        fail(f"nao encontrei {mod_name}.py — escreva o arquivo de conteudo primeiro.")
    B, CH = getattr(mod, "BOOK", None), getattr(mod, "CHAPTERS", None)
    if not isinstance(B, dict) or not isinstance(CH, list) or not CH:
        fail(f"{mod_name}.py precisa definir BOOK (dict) e CHAPTERS (lista nao vazia).")
    miss = REQ_BOOK - set(B)
    if miss:
        fail(f"BOOK faltando chaves obrigatorias: {sorted(miss)}")
    slugs = [c.get("slug") for c in CH]
    if len(slugs) != len(set(slugs)):
        dups = sorted({s for s in slugs if slugs.count(s) > 1})
        fail(f"slugs de capitulo duplicados: {dups}")
    for c in CH:
        cmiss = REQ_CH - set(c)
        if cmiss:
            fail(f"capitulo '{c.get('slug', '?')}' faltando: {sorted(cmiss)}")
        if not c.get("cards"):
            fail(f"capitulo '{c['slug']}' sem cards.")
        for card in c["cards"]:
            if not {"ic", "t", "b"} <= set(card):
                fail(f"card em '{c['slug']}' precisa de ic/t/b: {card!r}")
    print(f"OK: {mod_name}.py valido — {len(CH)} capitulos, "
          f"{sum(len(c['cards']) for c in CH)} cards.")
    return B, CH


def run(cmd, cwd=None):
    r = subprocess.run(cmd, cwd=cwd)
    if r.returncode != 0:
        fail(f"falhou: {' '.join(cmd)}")


def _repoint_cover(slug):
    """Aponta o coverUrl do livro no books.json para a capa HIBRIDA de estante."""
    import json
    p = os.path.join(BASE, "books.json")
    data = json.load(open(p, encoding="utf-8"))
    for b in data:
        if b.get("id") == slug:
            b["coverUrl"] = f"assets/{slug}-capa.png"
    json.dump(data, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"OK: books.json coverUrl -> assets/{slug}-capa.png (hibrida)")


def ensure_cover(B, slug):
    # DOUTRINA HIBRIDA (Diretor de Design, 14/jun): a arte ORIGINAL e' obrigatoria
    # (reconhecimento), MAS a capa da ESTANTE e' a HIBRIDA — arte original emoldurada
    # na marca (le marca.py) -> assets/<slug>-capa.png; books.json aponta p/ ela.
    # O original -cover.png segue como fonte da arte + OG. Assim a estante fica COESA.
    import gerar_capa
    cover = B.get("cover", f"assets/{slug}-cover.png")
    cover_path = os.path.join(BASE, cover)
    if not os.path.exists(cover_path):
        print(f"... capa original ausente — buscando no Open Library para '{slug}'")
        cmd = [sys.executable, "buscar_capa.py", slug, B["title"], B["author"]]
        if B.get("isbn"):
            cmd.append(str(B["isbn"]))
        subprocess.run(cmd, cwd=BASE)
    if os.path.exists(cover_path):
        gerar_capa.framed(slug, cover_path)              # arte real emoldurada na marca
    else:
        print("AVISO: sem capa original — tipografica de marca (so vale p/ nao-livros).")
        gerar_capa.typographic(slug, B["title"], B["author"])
    _repoint_cover(slug)


def verify(slug, CH):
    falta = [f"{slug}.html"] + [f"{slug}/{c['slug']}.html" for c in CH]
    falta = [f for f in falta if not os.path.exists(os.path.join(BASE, f))]
    if falta:
        fail(f"paginas nao geradas: {falta}")
    print(f"OK: {len(CH) + 1} paginas no disco.")
    if os.path.exists(os.path.join(SKILL, "driver.mjs")):
        print("... smoke no navegador (driver.mjs)")
        run(["node", "driver.mjs", "smoke"], cwd=SKILL)
    else:
        print("AVISO: driver.mjs nao encontrado — pulei o smoke (rode a skill run-biblioteca).")


def deploy(slug, CH):
    step("6", f"deploy -> {VPS}:{REMOTE}/{slug}")
    run(["ssh", VPS, f"mkdir -p {REMOTE}/{slug}"])
    run(["scp", f"{slug}.html", "index.html", "books.json", "sitemap.xml", "robots.txt",
         f"{VPS}:{REMOTE}/"], cwd=BASE)
    files = [os.path.join(slug, f"{c['slug']}.html") for c in CH]
    run(["scp", *files, f"{VPS}:{REMOTE}/{slug}/"], cwd=BASE)
    # Inclui só as capas que existem: livro sem capa original tem só o -capa.png
    # (tipografica); o -cover.png pode não existir e quebraria o scp.
    cover_assets = [p for p in (f"assets/{slug}-cover.png", f"assets/{slug}-capa.png")
                    if os.path.exists(os.path.join(BASE, p))]
    run(["scp", "assets/style.css", "assets/script-livro.js", *cover_assets, "assets/favicon.svg",
         f"{VPS}:{REMOTE}/assets/"], cwd=BASE)
    # corrige a permissao da pasta nova (senao o nginx da 404 — o bug classico)
    run(["ssh", VPS, f"chmod 755 {REMOTE}/{slug} && chmod 644 {REMOTE}/{slug}/*"])

    # _data.py necessario para o pipeline viral (gerar_viral.py na VPS)
    data_py = os.path.join(BASE, slug.replace("-", "_") + "_data.py")
    if os.path.exists(data_py):
        run(["scp", data_py, f"{VPS}:{REMOTE}/"])

    # kit de divulgacao (templates HTML para o admin + dados do carrossel)
    kit_tpl = os.path.join(BASE, "assets", "kit", "_tpl", slug)
    kit_data_dir = os.path.join(BASE, "assets", "kit", slug)
    if os.path.isdir(kit_tpl):
        run(["ssh", VPS, f"mkdir -p {REMOTE}/assets/kit/_tpl/{slug}"])
        run(["scp", "-r", kit_tpl, f"{VPS}:{REMOTE}/assets/kit/_tpl/"], cwd=BASE)
    for fname in ("manifest.json", "slides.json", "caps.json"):
        src = os.path.join(kit_data_dir, fname)
        if os.path.exists(src):
            run(["ssh", VPS, f"mkdir -p {REMOTE}/assets/kit/{slug}"])
            run(["scp", src, f"{VPS}:{REMOTE}/assets/kit/{slug}/"], cwd=BASE)

    # story PNGs (para o cron do Instagram)
    story_dir = os.path.join(BASE, "videos", "_carrossel", f"{slug}_stories")
    pngs = sorted(
        [os.path.join(story_dir, p) for p in os.listdir(story_dir) if p.endswith(".png")]
    ) if os.path.isdir(story_dir) else []
    if pngs:
        vps_stories = f"/opt/minutoreal/_carrossel/{slug}_stories"
        run(["ssh", VPS, f"mkdir -p {vps_stories}"])
        run(["scp", *pngs, f"{VPS}:{vps_stories}/"], cwd=BASE)
        print(f"OK: {len(pngs)} story PNGs enviados para {vps_stories}")

    print(f"OK: no ar -> https://www.andregalgani.com.br/biblioteca/{slug}.html")


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = {a for a in sys.argv[1:] if a.startswith("--")}
    if not args:
        fail("uso: python publicar_livro.py <slug> [--check] [--deploy]")
    slug = args[0]

    step("1", f"validando {slug}_data.py")
    validate(slug)
    if "--check" in flags:
        print("\nOK: --check: schema ok, nada escrito.")
        return

    step("1b", "verificacao editorial (fidelidade ao autor — skill e a referencia)")
    run([sys.executable, "verificar_conteudo.py", slug, "--fix"], cwd=BASE)
    # Recarrega o modulo apos possiveis correcoes (file pode ter mudado)
    _mod = slug.replace("-", "_") + "_data"
    if _mod in sys.modules:
        del sys.modules[_mod]
    B, CH = validate(slug)

    step("2", "gerando paginas + books.json")
    import gerar_livro
    gerar_livro.main(slug)

    step("2b", "gerando kit de divulgacao (templates do admin)")
    run([sys.executable, "gerar_dados_kit.py", slug], cwd=BASE)

    step("2c", "gerando dados do carrossel (slides.json + caps.json)")
    run([sys.executable, "gerar_dados_carrossel.py", slug], cwd=BASE)

    step("2d", "gerando story PNGs (4 frames: teaser+quote+insights+CTA)")
    run([sys.executable, "gerar_carrossel.py", slug, "--stories"], cwd=BASE)

    step("3", "garantindo a capa")
    ensure_cover(B, slug)

    step("4", "retrofit (favicon - OG - theme-color - nav nomeada - rodape)")
    run([sys.executable, "retrofit-fase23.py"], cwd=BASE)

    step("4b", "afiliado Amazon (gera links + injeta botao Comprar)")
    run([sys.executable, os.path.join("afiliados", "gerar_links.py")], cwd=BASE)
    run([sys.executable, os.path.join("afiliados", "inserir_botao.py")], cwd=BASE)

    step("4c", "SEO (sitemap.xml + robots.txt + JSON-LD/canonical)")
    run([sys.executable, "gerar_seo.py"], cwd=BASE)

    step("5", "verificacao")
    verify(slug, CH)

    if "--deploy" in flags:
        deploy(slug, CH)
    else:
        print(f"\nOK: pronto localmente. Para publicar:  python publicar_livro.py {slug} --deploy")


if __name__ == "__main__":
    main()
