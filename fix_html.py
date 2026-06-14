import os
import re

directory = r"c:\Users\User\.gemini\antigravity\scratch\biblioteca"

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # 1. Add skip-link if not exists
    if 'class="skip-link"' not in content:
        # insert right after <body>
        content = re.sub(
            r'(<body[^>]*>)',
            r'\1\n    <a href="#conteudo" class="skip-link">Ir para o conteúdo</a>',
            content,
            count=1
        )

    # 2. Fix inline styles and arrow in back-link
    # Find back-link tags
    def replace_backlink(match):
        attrs = match.group(1)
        inner_html = match.group(2)
        
        # Remove style attribute
        attrs = re.sub(r'\s*style="[^"]*"', '', attrs)
        
        # Replace textual &larr; or ← with the new icon-arrow span if not present
        if 'class="icon-arrow"' not in inner_html:
            inner_html = re.sub(r'(?:&larr;|←)\s*', '', inner_html)
            inner_html = '<span class="icon-arrow" aria-hidden="true">&larr;</span> ' + inner_html.strip()
            
        return f'<a{attrs}>{inner_html}</a>'

    content = re.sub(r'<a([^>]*?class="[^"]*?\bback-link\b[^"]*"[^>]*?)>(.*?)</a>', replace_backlink, content, flags=re.DOTALL)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")

for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".html"):
            process_file(os.path.join(root, file))

print("Done processing HTML files.")
