import os
import json
import re

lote_4 = [
    "kingsley-story-waiting-to-pierce-you",
    "koyre-mundo-fechado-universo-infinito",
    "krenak-a-vida-nao-e-util",
    "laberge-rheingold-lucid-dreaming",
    "laks-most-derveni-papyrus",
    "leite-psiconautas",
    "long-sedley-hellenistic-philosophers",
    "lucrecio-sobre-a-natureza-das-coisas",
    "magee-western-mysticism-esotericism",
    "marco-aurelio-meditacoes",
    "colli-nascimento-da-filosofia",
    "martin-velasco-greek-philosophy",
    "maximo-tiro-philosophical-orations",
    "mayer-nag-hammadi",
    "chase-did-socrates-meditate-2022",
    "mcevilley-shape-ancient-thought",
    "mckirahan-filosofia-antes-socrates",
    "mcnamara-cognitive-neuroscience-religious",
    "mckenna-food-of-the-gods",
    "mills-zend-avesta",
    "morgan-platonic-piety",
    "buxton-from-myth-to-reason",
    "muraresku-immortality-key",
    "naddaf-greek-concept-nature",
    "nietzsche-alem-do-bem-e-do-mal",
    "nietzsche-ecce-homo",
    "nietzsche-genealogia-da-moral",
    "nietzsche-o-nascimento-da-tragedia",
    "nietzsche-a-gaia-ciencia",
    "acker-diotima-de-mantineia",
    "nussbaum-therapy-of-desire",
    "ogden-greek-roman-necromancy",
    "origenes-contra-celso",
    "otto-idea-of-the-holy",
    "padmasambhava-tibetan-book-of-the-dead",
    "palmer-parmenides",
    "pascal-pensamentos",
    "pausanias-description-greece",
    "adluri-initiation-mysteries-plato",
    "platao-carta-vii",
    "platao-o-banquete"
]

SKILLS_DIR = r"C:\Users\User\.gemini\config\skills\drdolabela"
JSON_PATH = r"C:\Users\User\.gemini\antigravity\scratch\biblioteca\mapped_books.json"

with open(JSON_PATH, "r", encoding="utf-8") as f:
    books = json.load(f)

books.sort(key=lambda x: len(x.get('bib', {}).get('title', '')), reverse=True)

patterns = []
for b in books:
    title = b.get('bib', {}).get('title', '').strip()
    skill = b.get('skill', '')
    if len(title) > 5 and skill:
        escaped_title = re.escape(title)
        patterns.append((re.compile(r'(?<!\[)\b(' + escaped_title + r')\b(?!\])', flags=re.IGNORECASE), skill))

def process_file(filepath, current_skill):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    original_content = content
    
    for pattern, skill in patterns:
        if skill == current_skill:
            continue
        def replacer(match):
            matched_text = match.group(1)
            return f"[{matched_text}]({skill})"
        
        parts = re.split(r'(\[[^\]]+\]\([^\)]+\))', content)
        new_parts = []
        for p in parts:
            if p.startswith('[') and p.endswith(')'):
                new_parts.append(p)
            else:
                new_parts.append(pattern.sub(replacer, p))
        content = "".join(new_parts)

    if content != original_content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {filepath}")

for target in lote_4:
    target_dir = os.path.join(SKILLS_DIR, target)
    if not os.path.exists(target_dir):
        print(f"Dir not found: {target_dir}")
        continue
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            if file.endswith(".md"):
                process_file(os.path.join(root, file), target)

print("DONE_PROCESSING")
