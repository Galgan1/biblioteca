import json
import os
import re

SKILLS_DIR = r"C:\Users\User\.gemini\config\skills\drdolabela"
JSON_PATH = r"C:\Users\User\.gemini\antigravity\scratch\biblioteca\mapped_books.json"

target_skills = [
    "colli-sabedoria-grega",
    "colli-sabedoria-grega-ii",
    "colli-nascimento-da-filosofia",
    "collins-magic-ancient-greek",
    "cooper-pursuits-of-wisdom",
    "cornelli-on-pythagoreanism",
    "cornford-principium-sapientiae",
    "descartes-discurso-do-metodo",
    "detienne-mestres-da-verdade",
    "detienne-pensee-religieuse-philosophique",
    "dienstag-pessimism",
    "diodoro-library-of-history",
    "diogenes-vidas-e-doutrinas",
    "diogenes-lives-of-eminent-philosophers",
    "bernabe-platao-e-o-orfismo",
    "budge-book-of-the-dead",
    "eliade-shamanism",
    "eliade-yoga",
    "estrabao-geography",
    "epicuro-cartas-maximas",
    "epiteto-complete-works",
    "euripides-as-bacantes",
    "euripides-fragments",
    "faivre-western-esotericism",
    "ambury-philosophy-as-a-way-of-life",
    "faustino-late-foucault",
    "chase-hadot-critics-2024",
    "faustino-filosofia-forma-de-vida-ensaios",
    "fiordalis-buddhist-spiritual-practices",
    "foucault-hermeneutica-do-sujeito",
    "foucault-historia-da-sexualidade-2",
    "franz-sonhos-estudo",
    "freud-conferencias-introdutorias",
    "gazzinelli-fragmentos-orficos",
    "gazzinelli-vida-cetica-pirro",
    "goenka-vipassana-discourse",
    "goldmann-le-dieu-cache",
    "gouhier-pascal-conversao",
    "graf-magic-ancient-world",
    "graves-difficult-questions-easy-answers",
    "griffith-rig-veda"
]

def load_books():
    with open(JSON_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def process_file(file_path, books):
    if not os.path.exists(file_path):
        return
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    for book in books:
        skill_id = book.get('skill')
        if not skill_id:
            continue
        title = book.get('bib', {}).get('title', '')
        if not title or len(title) < 5:
            continue
        
        escaped_title = re.escape(title)
        
        # Regex to match markdown link OR the title. 
        # We use re.IGNORECASE.
        pattern = re.compile(rf'(\[.*?\]\(.*?\)|\<.*?\>)|({escaped_title})', re.IGNORECASE)
        
        def replacer(match):
            if match.group(1):
                return match.group(1)
            else:
                matched_text = match.group(2)
                # Link to the skill folder's SKILL.md
                # Assuming the format is [Title](../skill-id/SKILL.md)
                return f'[{matched_text}](../{skill_id}/SKILL.md)'
        
        content = pattern.sub(replacer, content)

    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file_path}")

def main():
    books = load_books()
    for b in books:
        t = b.get('bib', {}).get('title', '')
        b['bib']['title'] = t.strip('.,;:')

    books.sort(key=lambda x: len(x.get('bib', {}).get('title', '')), reverse=True)

    for skill in target_skills:
        skill_dir = os.path.join(SKILLS_DIR, skill)
        if not os.path.exists(skill_dir):
            print(f"Skill dir not found: {skill_dir}")
            continue
        
        skill_md = os.path.join(skill_dir, "SKILL.md")
        process_file(skill_md, books)
        
        chapters_dir = os.path.join(skill_dir, "chapters")
        if os.path.exists(chapters_dir):
            for filename in os.listdir(chapters_dir):
                if filename.endswith(".md"):
                    process_file(os.path.join(chapters_dir, filename), books)

if __name__ == "__main__":
    main()
