import os
import json
import re

lote3_skills = [
    "grimal-dicionario-mitologia",
    "grof-adventure-self-discovery",
    "guthrie-pythagorean-sourcebook",
    "guthrie-orpheus-greek-religion",
    "bernabe-platao-e-o-orfismo",
    "hadot-marius-victorinus",
    "chase-observations-pierre-hadot",
    "hadot-philosophie-antique",
    "hadot-inner-citadel",
    "hadot-maniere-de-vivre",
    "hadot-exercices-spirituels",
    "lucrecio-sobre-a-natureza-das-coisas",
    "hadot-wittgenstein-limites",
    "hadot-discours-mode-vie",
    "hadot-plotino-simplicidade",
    "hadot-selected-writings-practice",
    "hanegraaff-hermetic-spirituality",
    "foucault-technologies-of-the-self",
    "harari-sapiens",
    "harari-homo-deus",
    "harari-21-licoes",
    "ambury-philosophy-as-a-way-of-life",
    "hegel-fenomenologia-do-espirito",
    "hesiodo-trabalhos-e-dias",
    "homero-iliada",
    "homero-odisseia",
    "huxley-perennial-philosophy",
    "huxley-doors-of-perception",
    "inwood-poem-of-empedocles",
    "jaeger-theology-early-greek-philosophers",
    "jamblico-vie-de-pythagore",
    "jung-symbols-of-transformation",
    "jung-psychology-and-religion",
    "jung-alchemical-studies",
    "jung-mysterium-coniunctionis",
    "kardec-livro-dos-espiritos",
    "killen-mycenaean-greek",
    "kingsley-ancient-philosophy-mystery-magic",
    "kingsley-dark-places-of-wisdom",
    "kingsley-reality"
]

mapped_books_path = r"C:\Users\User\.gemini\antigravity\scratch\biblioteca\mapped_books.json"
skills_base_dir = r"C:\Users\User\.gemini\config\skills\drdolabela"

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

for skill in set(lote3_skills):
    skill_dir = os.path.join(skills_base_dir, skill)
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

print("LOTE 3 DONE")
