import re

with open(r"C:\Users\User\AppData\Local\Temp\book_skill_work\full_text.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Find chapter heading patterns
chapter_titles = [
    "INTRODUCTION",
    "THE STORY PROBLEM",
    "THE STRUCTURE SPECTRUM",
    "STRUCTURE AND SETTING",
    "STRUCTURE AND GENRE",
    "STRUCTURE AND CHARACTER",
    "STRUCTURE AND MEANING",
    "THE SUBSTANCE OF STORY",
    "THE INCITING INCIDENT",
    "ACT DESIGN",
    "SCENE DESIGN",
    "SCENE ANALYSIS",
    "COMPOSITION",
    "CRISIS, CLIMAX, RESOLUTION",
    "THE PRINCIPLE OF ANTAGONISM",
    "EXPOSITION",
    "PROBLEMS AND SOLUTIONS",
    "CHARACTER",
    "THE TEXT",
    "A WRITER'S METHOD",
    "FADE OUT",
]

print(f"Total lines: {len(lines)}")
print()

for title in chapter_titles:
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped == title or stripped.startswith(title):
            print(f"Line {i+1}: {stripped[:80]}")
            break
    else:
        # Try case-insensitive
        for i, line in enumerate(lines):
            if title.lower() in line.strip().lower() and len(line.strip()) < 60:
                print(f"Line {i+1} (fuzzy): {line.strip()[:80]}")
                break
        else:
            print(f"NOT FOUND: {title}")
