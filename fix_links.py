import os
import re
import glob

files = sorted(glob.glob("c:/Users/User/.gemini/antigravity/scratch/biblioteca/maquiavel-pedagogo/ch*.html"))
basenames = [os.path.basename(f) for f in files]

for i, filepath in enumerate(files):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    prev_link = basenames[i-1] if i > 0 else "../maquiavel-pedagogo.html"
    next_link = basenames[i+1] if i < len(files)-1 else "../maquiavel-pedagogo.html"

    # Substituir link anterior (procura algo com "&larr; Anterior" ou "Anterior")
    content = re.sub(
        r'<a href="[^"]+"([^>]*)>((?:&larr;|←)?\s*Anterior\s*(?:&larr;|←)?)</a>', 
        rf'<a href="{prev_link}"\1>\2</a>', 
        content
    )
    
    # Substituir link proximo
    content = re.sub(
        r'<a href="[^"]+"([^>]*)>((?:&rarr;|→)?\s*Próximo\s*(?:&rarr;|→)?)</a>', 
        rf'<a href="{next_link}"\1>\2</a>', 
        content
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Fixed links in chapter files.")
