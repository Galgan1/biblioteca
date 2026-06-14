# -*- coding: utf-8 -*-
"""Verificação da taxonomia de coleções da estante curada.
Atribui cada livro à PRIMEIRA coleção (ordem = prioridade) cuja lista de tags
intersecta as tags do livro. Imprime a distribuição p/ eu validar/ajustar antes
de levar a lógica para o script.js. OVERRIDES corrige casos de borda por id."""
import json, sys

# ordem importa: a 1ª coleção que casa vence
COLLECTIONS = [
    ("Som & cinema",                ["Som", "Cinema"]),
    ("Espiritualidade & consciência",["Espiritualidade", "Consciência", "Misticismo", "Meditação", "Sabedoria"]),
    ("Literatura & clássicos",      ["Literatura", "Rússia", "Distopia", "Ficção", "Ficção Científica"]),
    ("Roteiro & narrativa",         ["Roteiro", "Narrativa", "Dramaturgia", "Mito", "Escrita Criativa"]),
    ("Comunicação & linguagem",     ["Comunicação", "Persuasão", "Influência", "Negociação", "Assertividade",
                                     "Empatia", "Escuta", "Feedback", "Análise Transacional", "Conflito",
                                     "Língua", "Texto", "Redação"]),
    ("Dinheiro & finanças",         ["Finanças", "Dinheiro", "Investimentos", "Riqueza", "Educação Financeira",
                                     "Economia", "Bitcoin"]),
    ("Poder, política & estratégia",["Poder", "Estratégia", "Política", "Liderança", "Geopolítica", "Sedução", "Gestão"]),
    ("Psicologia & comportamento",  ["Psicologia", "Neurociência", "Comportamento", "Decisão",
                                     "Economia Comportamental", "Introversão", "Psicologia Social", "Mitologia", "Feminino"]),
    ("Filosofia & pensamento",      ["Filosofia", "Existência", "Complexidade", "Epistemologia",
                                     "História das Ideias"]),
    ("Sociedade & cultura",         ["Sociedade", "Sociologia", "Modernidade", "Tecnologia", "Futuro",
                                     "Cultura", "Educação", "Antropologia", "Trabalho"]),
    ("Crescimento & hábitos",       ["Autodesenvolvimento", "Produtividade", "Foco", "Mudança", "Sucesso",
                                     "Mentalidade", "Carreira", "Hábitos"]),
    ("Direito & registros",         ["Direito", "Cartório", "Registros Públicos"]),
]
OVERRIDES = {}  # id -> nome da coleção, p/ corrigir borda

def classify(book):
    if book["id"] in OVERRIDES:
        return OVERRIDES[book["id"]]
    tags = set(book.get("tags", []))
    for name, taglist in COLLECTIONS:
        if tags & set(taglist):
            return name
    return "Outros"

def main():
    b = json.load(open("books.json", encoding="utf-8"))
    buckets = {name: [] for name, _ in COLLECTIONS}
    buckets["Outros"] = []
    for x in b:
        buckets[classify(x)].append(x)
    for name in [n for n, _ in COLLECTIONS] + ["Outros"]:
        books = buckets[name]
        if not books and name != "Outros":
            print(f"\n## {name}  — VAZIA"); continue
        prontos = sum(1 for x in books if not x.get("comingSoon"))
        print(f"\n## {name}  ({len(books)} livros · {prontos} prontos)")
        for x in books:
            mark = "•" if not x.get("comingSoon") else "→"
            print(f"   {mark} {x['title']}  [{', '.join(x.get('tags', []))}]")

if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    main()
