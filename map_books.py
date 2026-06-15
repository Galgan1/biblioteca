import os
import json
import re

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s-]+', '-', text)
    return text.strip('-')

skills_dir = r"C:\Users\User\.gemini\config\skills\drdolabela"
existing_skills = [d for d in os.listdir(skills_dir) if os.path.isdir(os.path.join(skills_dir, d))]

with open(r"C:\Users\User\.gemini\antigravity\scratch\biblioteca\parsed_bibliography.json", 'r', encoding='utf-8') as f:
    books = json.load(f)

matched = []
unmatched = []

for item in books:
    if not item['is_book']:
        continue
        
    combined = slugify(item['author'] + " " + item['title'])
    best_match = None
    best_score = 0
    for skill in existing_skills:
        skill_parts = set(skill.split('-'))
        combined_parts = set(combined.split('-'))
        overlap = len(skill_parts.intersection(combined_parts))
        # require at least some match
        if overlap > best_score and overlap >= 1: 
            best_score = overlap
            best_match = skill
            
    if best_match:
        matched.append({"bib": item, "skill": best_match})
    else:
        unmatched.append(item)

print(f"Matched {len(matched)} books to skills.")
with open(r"C:\Users\User\.gemini\antigravity\scratch\biblioteca\mapped_books.json", "w", encoding="utf-8") as f:
    json.dump(matched, f, indent=2, ensure_ascii=False)
