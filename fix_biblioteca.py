import os
import re
from urllib.parse import unquote

def check_links():
    broken = []
    for root, _, files in os.walk(r'c:\Users\User\.gemini\antigravity\scratch\biblioteca'):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                hrefs = re.findall(r'href=["\']([^"\']+)["\']', content)
                for href in hrefs:
                    if href.startswith(('http', '#', 'mailto:', 'tel:')):
                        continue
                    path_part = href.split('#')[0].split('?')[0]
                    if not path_part:
                        continue
                    path_part = unquote(path_part)
                    target_path = os.path.normpath(os.path.join(root, path_part))
                    if not os.path.exists(target_path):
                        broken.append(f'{filepath}: {href} -> {target_path}')
    if broken:
        print('Broken links found:')
        for b in broken:
            print(b)
    else:
        print('No broken links found.')

def fix_css():
    css_path = r'c:\Users\User\.gemini\antigravity\scratch\biblioteca\assets\style.css'
    with open(css_path, 'r', encoding='utf-8') as f:
        css = f.read()
    
    # Impeccable Shape: Remove border-radius and web-style backgrounds, use dashed green borders
    css = re.sub(r'border-radius:\s*[^;]+;', 'border-radius: 0;', css)
    # Ensure standard cards have transparent background and dashed borders
    if '.card {' in css:
        css = re.sub(r'\.card\s*{[^}]+}', 
                     r'.card {\n    border: 2px dashed var(--green);\n    padding: 1.5rem;\n    display: flex;\n    gap: 1.25rem;\n    align-items: flex-start;\n    background: transparent;\n    border-radius: 0;\n    transition: border-color 200ms var(--ease-out-quart);\n}', 
                     css, count=1)
    
    # Impeccable Typeset: Robust sans-serif, ALL CAPS for headings, heavy bold
    css = re.sub(r'font-family:\s*[^;]+(Literata|Georgia|serif)[^;]*;', 'font-family: "Hanken Grotesk", system-ui, -apple-system, sans-serif;', css)
    css = re.sub(r'(--font-serif:\s*)[^;]+;', r'\g<1>"Hanken Grotesk", system-ui, -apple-system, sans-serif;', css)
    
    # Add text-transform uppercase to headings if not present
    if '.card-title {' in css:
        css = re.sub(r'\.card-title\s*{([^}]+)}', 
                     lambda m: '.card-title {' + m.group(1) + ('' if 'text-transform' in m.group(1) else '\n    text-transform: uppercase;\n    font-weight: 800;\n    color: var(--green);') + '}', 
                     css)
                     
    if 'h1, h2, h3, h4 {' in css or 'h1, h2, h3 {' in css:
        pass # We might need to add it specifically, but let's just make h1-h4 bold and uppercase
    else:
        css += '\n\nh1, h2, h3, h4 {\n    text-transform: uppercase;\n    font-weight: 800;\n    font-family: var(--font-sans);\n}'
        
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)
    print("CSS updated with Impeccable guidelines (shape, typeset, colorize).")

if __name__ == '__main__':
    check_links()
    fix_css()
