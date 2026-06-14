import os
import glob
import re

base_dir = r"c:\Users\User\.gemini\antigravity\scratch\biblioteca"

# Atualizar arquivos na raiz (index.html, keller-casamento.html, maquiavel-pedagogo.html)
root_files = glob.glob(os.path.join(base_dir, "*.html"))
for fpath in root_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Substituir link do css (estava "style.css" ou "keller-casamento/style.css" ou "maquiavel-pedagogo/style.css")
    content = re.sub(r'<link rel="stylesheet" href="[^"]*style\.css">', '<link rel="stylesheet" href="assets/style.css">', content)
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)

# Atualizar arquivos nas subpastas
subfolders = ["keller-casamento", "maquiavel-pedagogo", "print"]
for folder in subfolders:
    sub_files = glob.glob(os.path.join(base_dir, folder, "*.html"))
    for fpath in sub_files:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Substituir link do css para apontar um nível acima
        content = re.sub(r'<link rel="stylesheet" href="[^"]*style\.css">', '<link rel="stylesheet" href="../assets/style.css">', content)
        
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)

print("HTMLs atualizados para referenciar assets/style.css")
