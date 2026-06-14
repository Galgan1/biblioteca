import os
import re

directory = r"c:\Users\User\.gemini\antigravity\scratch\biblioteca"

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # 1. Clean paragraph styles
    content = re.sub(r'<p\s+style=[\'"]margin-bottom:\s*0\.5rem;?[\'"]>', '<p>', content)
    content = re.sub(r'<p\s+style=[\'"]margin-bottom:\s*1rem;?[\'"]>', '<p>', content) # just in case

    # 2. Refactor pagination
    # Find the pagination div
    div_pattern = r'<div\s+style=[\'"]display:\s*flex;\s*justify-content:\s*space-between;\s*margin-top:\s*3rem;?[\'"]>(.*?)</div>'
    
    def replace_nav(match):
        inner_html = match.group(1)
        # Replace the a tags inside
        # <a href="..." style="...">...</a>
        a_pattern = r'<a\s+href=([\'"][^\'"]+[\'"])\s+style=[\'"][^\'"]+[\'"]>([^<]+)</a>'
        def replace_a(a_match):
            href = a_match.group(1)
            text = a_match.group(2)
            return f'<a href={href} class="chapter-nav-link">{text}</a>'
            
        inner_html = re.sub(a_pattern, replace_a, inner_html)
        return f'<nav aria-label="Navegação entre capítulos" class="chapter-nav">{inner_html}</nav>'

    content = re.sub(div_pattern, replace_nav, content, flags=re.DOTALL)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Cleaned {filepath}")

for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".html"):
            process_file(os.path.join(root, file))

print("Done cleaning HTML files.")
