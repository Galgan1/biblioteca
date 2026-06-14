"""Gera os links de afiliado da Amazon para os livros da Biblioteca.

Fonte do catalogo: ../books.json (id, title, author).
Config de afiliado:  ./afiliados.json (tag, asins, busca_override, excluir).

Regra: tem ASIN -> link direto /dp/ASIN ; sem ASIN -> link de busca.
Os dois ganham comissao. Rode:  python afiliados/gerar_links.py
Saida: imprime a tabela e escreve ./links.json (id -> url).
"""
import json
import sys
from pathlib import Path
from urllib.parse import quote_plus

AQUI = Path(__file__).resolve().parent
BOOKS = AQUI.parent / "books.json"
CONFIG = AQUI / "afiliados.json"
SAIDA = AQUI / "links.json"


def montar_link(cfg, book):
    tag = cfg["tag"]
    dominio = cfg["dominio"]
    asin = cfg.get("asins", {}).get(book["id"])
    if asin:
        return f"https://www.{dominio}/dp/{asin}/?tag={tag}&language=pt_BR", "direto"
    termo = cfg.get("busca_override", {}).get(book["id"]) or f"{book['title']} {book['author']}"
    return f"https://www.{dominio}/s?k={quote_plus(termo)}&tag={tag}", "busca"


def montar_compras(cfg, book):
    """Lista de {loja, nome, url} de TODAS as lojas ativas com link p/ este livro.
    Amazon = automatica (ASIN/busca). Outras = manuais em links_manuais. Amazon vem 1o."""
    lojas = cfg.get("lojas", {})
    manuais = cfg.get("links_manuais", {}).get(book["id"], {})
    compras = []
    if lojas.get("amazon", {}).get("ativa", True):
        url, _ = montar_link(cfg, book)
        compras.append({"loja": "amazon", "nome": lojas.get("amazon", {}).get("nome", "Amazon"), "url": url})
    for loja, info in lojas.items():
        if loja == "amazon" or not info.get("ativa"):
            continue
        if manuais.get(loja):
            compras.append({"loja": loja, "nome": info.get("nome", loja), "url": manuais[loja]})
    return compras


def main():
    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    books = json.loads(BOOKS.read_text(encoding="utf-8"))
    excluir = set(cfg.get("excluir", []))

    links = {}
    linhas = []
    for book in books:
        if book["id"] in excluir:
            continue
        url, tipo = montar_link(cfg, book)
        links[book["id"]] = url
        linhas.append((book["title"], tipo, url))

    SAIDA.write_text(json.dumps(links, ensure_ascii=False, indent=2), encoding="utf-8")

    # Espelha o link no books.json (campo "amazon") — fonte única que a estante
    # (script.js) lê para o botão de compra discreto por card. Excluídos ficam sem.
    for book in books:
        if book["id"] in links:
            book["amazon"] = links[book["id"]]
            book["compras"] = montar_compras(cfg, book)
        else:
            book.pop("amazon", None)
            book.pop("compras", None)
    BOOKS.write_text(json.dumps(books, ensure_ascii=False, indent=2), encoding="utf-8")

    diretos = sum(1 for _, t, _ in linhas if t == "direto")
    print(f"{len(linhas)} livros | {diretos} link(s) direto(s) | {len(linhas) - diretos} de busca | tag={cfg['tag']}\n")
    for titulo, tipo, url in linhas:
        marca = "[*]" if tipo == "direto" else "[~]"
        print(f"{marca} {titulo}")
        print(f"    {url}")
    print(f"\nEscrito: {SAIDA}")


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    main()
