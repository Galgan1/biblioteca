import os
import json

skills_dir = r"C:\Users\User\.gemini\config\skills"
skills = []
if os.path.exists(skills_dir):
    skills = [d for d in os.listdir(skills_dir) if os.path.isdir(os.path.join(skills_dir, d))]

with open("skills_list.json", "w", encoding="utf-8") as f:
    json.dump(skills, f, indent=2, ensure_ascii=False)
