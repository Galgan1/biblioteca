import os
import json

base_dir = r"C:\Users\User\.gemini\config\skills\drdolabela"
mapped_books_path = r"C:\Users\User\.gemini\antigravity\scratch\biblioteca\mapped_books.json"
report_path = r"C:\Users\User\.gemini\antigravity\scratch\biblioteca\audit_validation.md"

with open(mapped_books_path, "r", encoding="utf-8") as f:
    books = json.load(f)

total = len(books)
passed = 0
failed = []

report = "# Relatório de Validação da Estrutura /book-to-skill\n\n"

for book in books:
    skill = book["skill"]
    skill_dir = os.path.join(base_dir, skill)
    skill_md = os.path.join(skill_dir, "SKILL.md")
    chapters_dir = os.path.join(skill_dir, "chapters")
    
    issues = []
    
    if not os.path.exists(skill_md):
        issues.append("SKILL.md ausente")
        
    if not os.path.exists(chapters_dir):
        issues.append("Pasta chapters/ ausente")
    else:
        chapter_files = [f for f in os.listdir(chapters_dir) if f.endswith(".md") and f.startswith("ch")]
        if not chapter_files:
            issues.append("Pasta chapters/ está vazia ou não contém arquivos chXX.md")
            
    if not issues:
        passed += 1
    else:
        failed.append({"skill": skill, "issues": issues})

report += f"**Total de Skills Analisadas:** {total}\n"
report += f"**Skills Aprovadas (100% aderentes à estrutura):** {passed}\n"
report += f"**Skills com Falhas:** {len(failed)}\n\n"

if failed:
    report += "## Skills que necessitam de correção:\n"
    for f in failed:
        report += f"- `{f['skill']}`: {', '.join(f['issues'])}\n"
else:
    report += "## Conclusão\nTodas as skills estão rigorosamente dentro do padrão exigido pelo `/book-to-skill`."

with open(report_path, "w", encoding="utf-8") as f:
    f.write(report)

print("Validação concluída com sucesso!")
