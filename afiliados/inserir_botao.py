"""Injeta o card 'Comprar' (multi-loja) nas paginas de livro da Biblioteca.

Le o campo book.compras de ../books.json (lista de lojas, gerada por gerar_links.py)
e insere, em cada {id}.html, um bloco delimitado por marcadores, logo antes do <footer>.
Cada loja ativa com link vira um botao. Idempotente: rodar de novo atualiza no lugar.

Rode depois de gerar_links.py:  python afiliados/inserir_botao.py
"""
import html
import json
import re
import sys
import time
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent
BOOKS = RAIZ / "books.json"

INI = "<!-- amazon-afiliado:start -->"
FIM = "<!-- amazon-afiliado:end -->"

ICONE = (
    '<svg viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">'
    '<path d="M12 16h8l5 26h22l5-19H23" stroke="currentColor" stroke-width="3" '
    'stroke-linecap="round" stroke-linejoin="round"/>'
    '<circle cx="27" cy="51" r="3.5" stroke="currentColor" stroke-width="3"/>'
    '<circle cx="44" cy="51" r="3.5" stroke="currentColor" stroke-width="3"/></svg>'
)


def bloco(titulo, compras):
    t = html.escape(titulo)
    botoes = "\n".join(
        f'            <a class="amazon-btn" href="{html.escape(c["url"], quote=True)}" '
        f'target="_blank" rel="nofollow sponsored noopener">{ICONE} Comprar na {html.escape(c["nome"])}</a>'
        for c in compras
    )
    disc = ("Como Associado da Amazon, ganho comissão por compras qualificadas — sem custo extra para você."
            if len(compras) == 1 else
            "Alguns links acima são de afiliado — posso ganhar comissão por compras qualificadas, sem custo extra para você.")
    return f"""{INI}
        <section class="amazon-cta">
            <p class="amazon-cta-text">Gostou do resumo? Leia <strong>{t}</strong> na íntegra:</p>
{botoes}
            <p class="amazon-cta-disc">{disc}</p>
        </section>
        {FIM}"""


def main():
    books = json.loads(BOOKS.read_text(encoding="utf-8"))
    padrao = re.compile(re.escape(INI) + r".*?" + re.escape(FIM), re.DOTALL)
    feitos, faltando = [], []

    for book in books:
        compras = book.get("compras")
        if not compras:
            continue
        arq = RAIZ / f"{book['id']}.html"
        if not arq.exists():
            faltando.append(book["id"])
            continue

        doc = arq.read_text(encoding="utf-8")
        novo = bloco(book["title"], compras)

        if padrao.search(doc):
            doc = padrao.sub(novo, doc)
            acao = "atualizado"
        else:
            doc = re.sub(r"(\n[ \t]*<footer)", "\n        " + novo + r"\1", doc, count=1)
            acao = "inserido"

        for tentativa in range(6):  # Windows: OSError [Errno 22]/lock transitório na gravação em lote
            try:
                arq.write_text(doc, encoding="utf-8", newline='\n')
                break
            except (OSError, PermissionError):
                if tentativa == 5:
                    raise
                time.sleep(0.15 * (tentativa + 1))
        feitos.append(f"{acao}: {book['id']}.html ({len(compras)} loja)")

    for linha in feitos:
        print(linha)
    if faltando:
        print("\nsem pagina .html (ignorados):", ", ".join(faltando))
    print(f"\n{len(feitos)} pagina(s) com botao de compra.")


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    main()
