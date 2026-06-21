import json
slugs = ['21-licoes', 'busca-de-sentido', 'design-do-dia-a-dia', 'homem-mais-rico-babilonia', 'meditacoes', 'nunca-divida-a-diferenca', 'poder-dos-quietos', 'save-the-cat']

out_content = ''
for i, slug in enumerate(slugs):
    try:
        with open(fr'C:\Users\User\.gemini\antigravity\scratch\biblioteca\_kit_preview\gemini_in\book_{i}_out.json', 'r', encoding='utf-8') as f:
            data = f.read()
            out_content += f'=== {slug} ===\n```json\n{data}\n```\n\n'
    except Exception as e:
        print(f'Error reading book {i}: {e}')

with open(r'C:\Users\User\.gemini\antigravity\scratch\biblioteca\_kit_preview\gemini_in\batch_1_out.md', 'w', encoding='utf-8') as f:
    f.write(out_content)
