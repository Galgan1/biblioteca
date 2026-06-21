import json

with open(r"C:\Users\User\.gemini\antigravity\scratch\biblioteca\mapped_books.json", 'r', encoding='utf-8') as f:
    books = json.load(f)

# Basic categorization based on keywords
categories = {
    "Filosofia Antiga & Estoicismo": ["platao", "aristoteles", "socrates", "epiteto", "seneca", "marco-aurelio", "epicuro"],
    "Modo de Vida & Pierre Hadot": ["hadot", "sellars", "way-of-life", "faustino", "chase"],
    "Mito, Religião & Mistérios": ["burkert", "mystery", "myth", "campbell", "eliade", "dionysus", "orpheus", "orfismo"],
    "Magia, Enteógenos & Alteração de Consciência": ["magic", "psychedelic", "entheogen", "shamanism", "pollan", "mckenna"],
    "Pensamento Moderno & Foucault": ["foucault", "nietzsche", "schopenhauer", "rousseau", "descartes"]
}

categorized = {k: [] for k in categories}
categorized["Outros"] = []

for item in books:
    skill = item['skill']
    placed = False
    for cat, keywords in categories.items():
        if any(kw in skill.lower() for kw in keywords):
            categorized[cat].append(item)
            placed = True
            break
    if not placed:
        categorized["Outros"].append(item)

# Generate Markdown
md = "# Master Mind: Biblioteca Dr. Dolabela\n\n"
md += "Esta página funciona como o cérebro unificado das 217 obras e skills processadas, interligando conceitos sob a metodologia `/book-to-skill`.\n\n"

for cat, items in categorized.items():
    md += f"## {cat}\n"
    for i in items:
        bib = i['bib']
        md += f"- **{bib['author']}** ({bib['year']}). *{bib['title']}* -> [`{i['skill']}`](file:///C:/Users/User/.gemini/config/skills/drdolabela/{i['skill']})\n"
    md += "\n"

with open(r"C:\Users\User\.gemini\config\skills\drdolabela\MASTER_MIND.md", "w", encoding="utf-8") as f:
    f.write(md)

print("MASTER_MIND.md gerado com sucesso!")
