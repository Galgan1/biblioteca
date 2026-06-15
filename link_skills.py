import os
import json
import re

lote_1_skills = [
    "agostinho-confissoes",
    "ambury-philosophy-as-a-way-of-life",
    "apolodoro-library-of-greek-mythology",
    "acker-diotima-de-mantineia",
    "aristofanes-birds-lysistrata-thesmophoria",
    "aristofanes-vespas-aves-ras",
    "armstrong-ancient-pieties-greek-world",
    "aristoteles-problemata",
    "aristoteles-elencos-sofisticos",
    "aristoteles-constituicao-dos-atenienses",
    "aristoteles-historia-animais-vii-x",
    "aristoteles-partes-dos-animais",
    "ateneu-deipnosophists",
    "attali-pascal",
    "barbieri-hinos-antigos",
    "barres-angoisse-de-pascal",
    "beckwith-greek-buddha",
    "bergson-pensamento-movente",
    "bernabe-redefining-dionysus",
    "bernabe-platao-e-o-orfismo",
    "bernabe-hieros-logos",
    "betegh-derveni-papyrus",
    "betz-greek-magical-papyri-translation",
    "bowden-mystery-cults-ancient-world",
    "bremmer-initiation-mysteries",
    "brisson-filosofia-do-mito",
    "brochard-ceticos-gregos",
    "burkert-ancient-mystery-cults",
    "burkert-greek-religion",
    "burkert-babylon-memphis-persepolis",
    "buxton-from-myth-to-reason",
    "campbell-masks-of-god",
    "campbell-o-poder-do-mito",
    "campbell-inner-reaches-outer-space",
    "campbell-hero-thousand-faces",
    "carter-tomb-tutankhamen-vol3",
    "chase-did-socrates-meditate-2022",
    "chaui-filosofia-modo-de-vida",
    "cicero-nature-gods-academics"
]

base_dir = r"C:\Users\User\.gemini\config\skills\drdolabela"
mapped_books_path = r"C:\Users\User\.gemini\antigravity\scratch\biblioteca\mapped_books.json"

with open(mapped_books_path, "r", encoding="utf-8") as f:
    mapped_books = json.load(f)

terms = {}
for entry in mapped_books:
    skill = entry["skill"]
    bib = entry.get("bib", {})
    author = bib.get("author", "")
    title = bib.get("title", "")
    
    if title and len(title) > 4:
        terms[title] = skill
    if author and title:
        terms[f"{author} - {title}"] = skill
        terms[f"{author}: {title}"] = skill

sorted_terms = sorted(terms.keys(), key=len, reverse=True)

def replace_in_file(filepath, skill_name):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return

    original_content = content
    if "chapters" in filepath.replace("\\", "/"):
        rel_prefix = "../../"
    else:
        rel_prefix = "../"

    for term in sorted_terms:
        target_skill = terms[term]
        if target_skill == skill_name:
            continue
            
        pattern = re.compile(r'\b' + re.escape(term) + r'\b', re.IGNORECASE)
        
        def replacer(match):
            original = match.group(0)
            return f"[{original}]({rel_prefix}{target_skill}/SKILL.md)"
            
        parts = re.split(r'(\[.*?\]\(.*?\))', content)
        for i in range(0, len(parts), 2):
            parts[i] = pattern.sub(replacer, parts[i])
        content = "".join(parts)

    if content != original_content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {filepath}")

for skill in set(lote_1_skills):
    skill_dir = os.path.join(base_dir, skill)
    if not os.path.isdir(skill_dir):
        print(f"Skill dir not found: {skill_dir}")
        continue
    
    skill_md = os.path.join(skill_dir, "SKILL.md")
    if os.path.isfile(skill_md):
        replace_in_file(skill_md, skill)
        
    chapters_dir = os.path.join(skill_dir, "chapters")
    if os.path.isdir(chapters_dir):
        for root, dirs, files in os.walk(chapters_dir):
            for file in files:
                if file.endswith(".md"):
                    replace_in_file(os.path.join(root, file), skill)

print("PYTHON SCRIPT DONE")
