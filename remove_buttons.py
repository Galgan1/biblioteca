import os
import re

base_dir = r"c:\Users\User\.gemini\antigravity\scratch\biblioteca"

html_files = []
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.html'):
            html_files.append(os.path.join(root, file))

pattern = re.compile(r'<div class="actions"[^>]*>\s*<a href="[^"]+" download class="btn-download">[\s\S]*?</a>\s*</div>', re.IGNORECASE)

removed_count = 0
for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    new_content = pattern.sub('', content)
    
    if new_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Removido de {os.path.relpath(file_path, base_dir)}")
        removed_count += 1

print(f"\nBotões removidos com sucesso em {removed_count} arquivos!")
