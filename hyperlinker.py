import os
import json
import re

lote_5 = [
    "adluri-initiation-mysteries-plato",
    "acker-diotima-de-mantineia",
    "lucrecio-sobre-a-natureza-das-coisas",
    "bernabe-platao-e-o-orfismo",
    "plinio-natural-history-vol-ix",
    "plutarco-banquete-sete-sabios",
    "plutarco-vidas-paralelas-solon-publicola",
    "plutarco-de-isis-e-osiris",
    "pollan-how-to-change-your-mind",
    "porfirio-abstinence-killing-animals",
    "ribeiro-oraculo-da-noite",
    "ribeiro-jr-hinos-homericos",
    "porfirio-life-of-pythagoras",
    "rinella-pharmakon",
    "budge-book-of-the-dead",
    "rothschild-paul-in-athens",
    "rousseau-discours-inegalite",
    "rousseau-reveries-promeneur",
    "schopenhauer-essays-aphorisms",
    "schopenhauer-mundo-vontade-representacao-tomo-ii",
    "seaford-money-early-greek-mind",
    "sellars-art-of-living-stoics",
    "seneca-cartas-a-lucilio",
    "seneca-natural-questions",
    "ambury-philosophy-as-a-way-of-life",
    "shaw-theurgy-soul-iamblichus",
    "sin-leqi-unninni-epopeia-gilgamesh",
    "sjostedt-h-noumenautics",
    "stein-persephone-unveiled",
    "stein-ecstatic-experience",
    "taylor-atomists-leucippus-democritus",
    "teofrasto-enquiry-into-plants",
    "totelin-hippocratic-recipes"
]

base_dir = r"C:\Users\User\.gemini\config\skills\drdolabela"
mapped_books_path = r"C:\Users\User\.gemini\antigravity\scratch\biblioteca\mapped_books.json"

with open(mapped_books_path, "r", encoding="utf-8") as f:
    mapped_books = json.load(f)

keywords = {}

for entry in mapped_books:
    skill = entry.get("skill")
    if not skill: continue
    
    bib = entry.get("bib", {})
    title = bib.get("title", "").strip()
    author = bib.get("author", "").strip()
    
    title = title.split(":")[0].strip()
    
    if len(title) > 6 and title.lower() not in ["problemata", "the", "a", "(ed.)", "(eds)", "birds", "works"]:
        keywords[title] = skill

def add_links(content, is_chapter, current_skill):
    parts = re.split(r'(\[[^\]]+\]\([^)]+\))', content)
    sorted_kws = sorted(keywords.keys(), key=len, reverse=True)
    
    new_parts = []
    for part in parts:
        if part.startswith('[') and part.endswith(')'):
            new_parts.append(part)
        else:
            text = part
            for kw in sorted_kws:
                target_skill = keywords[kw]
                if target_skill == current_skill:
                    continue
                
                link_path = f"../../{target_skill}/SKILL.md" if is_chapter else f"../{target_skill}/SKILL.md"
                pattern = r'(?i)\b(' + re.escape(kw) + r')\b'
                
                # Check for match before doing sub to save time and prevent double sub issues
                # (Though double sub is prevented by iterating words, but wait, a substituted keyword
                # could be matched again if another keyword is a substring. Sorting by length avoids this
                # mostly, but the replacement introduces `[...]` and `(../../skill/SKILL.md)`.
                # We should be careful not to match inside the newly added link.
                
                if re.search(pattern, text):
                    # To avoid replacing inside links we just added, we do another split!
                    sub_parts = re.split(r'(\[[^\]]+\]\([^)]+\))', text)
                    text = ""
                    for sp in sub_parts:
                        if sp.startswith('[') and sp.endswith(')'):
                            text += sp
                        else:
                            text += re.sub(pattern, r'[\1](' + link_path + r')', sp)
            new_parts.append(text)
    return "".join(new_parts)

for skill_folder in set(lote_5):
    folder_path = os.path.join(base_dir, skill_folder)
    if not os.path.exists(folder_path):
        continue
        
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                is_chapter = "chapters" in root.replace('\\', '/')
                
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    
                new_content = add_links(content, is_chapter, skill_folder)
                
                if new_content != content:
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"Updated {file_path}")

print("DONE")
