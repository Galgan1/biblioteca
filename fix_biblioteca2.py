import os

def fix_css():
    css_path = r'c:\Users\User\.gemini\antigravity\scratch\biblioteca\assets\style.css'
    with open(css_path, 'r', encoding='utf-8') as f:
        css = f.read()
    
    # Fix the undefined --font-sans variable
    css = css.replace('var(--font-sans)', 'var(--font-display)')
    
    # Let's ensure a.card looks good with dashed border
    if 'a.card:hover' in css and 'border-color: var(--green);' in css:
        pass # Already has hover state
        
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)

def copy_cover():
    import shutil
    src = r'C:\Users\User\.gemini\antigravity\brain\e3b3f63f-7ba5-463c-b315-622c803dacae\media__1781129727101.jpg'
    dst = r'c:\Users\User\.gemini\antigravity\scratch\biblioteca\assets\maquiavel-cover.jpg'
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print("Copied cover image successfully.")
    else:
        print("Source image not found.")

def write_biblioteca_md():
    md_path = r'c:\Users\User\.gemini\antigravity\scratch\biblioteca\biblioteca.md'
    content = """# Biblioteca
Bem-vindo à Biblioteca.

## Funcionamento e Estética
Tudo o que está dentro do diretório `/biblioteca` possuirá **rigorosamente o mesmo estilo**.
A estética adota o design "Cheat Sheet Verde", utilizando:
- Fontes robustas e sem serifa (Hanken Grotesk).
- Títulos em MAIÚSCULAS e negrito pesado.
- Cards transparentes com bordas tracejadas verdes.
- Ícones limpos, sem fundo.
Este é um repositório centralizado onde todos os resumos de livros seguem uma padronização visual impecável.

## Acesso aos Livros
- [O Significado do Casamento (Keller)](keller-casamento.html)
- [Maquiavel Pedagogo (Pascal Bernardin)](maquiavel-pedagogo.html)

*A opção de PDF não é mais suportada nas páginas; a impressão deve ser feita nativamente via navegador se necessário.*
"""
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("biblioteca.md created.")

if __name__ == '__main__':
    fix_css()
    copy_cover()
    write_biblioteca_md()
