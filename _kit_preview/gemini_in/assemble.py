import json
import re
import os

DIR = r"C:\Users\User\.gemini\antigravity\scratch\biblioteca\_kit_preview\gemini_in"

def read_file(name):
    with open(os.path.join(DIR, name), 'r', encoding='utf-8') as f:
        return f.read()

book_data = {
    'antifragil': {},
    'comece-pelo-porque': {},
    'futebol-brasileiro': {},
    'investidor-inteligente': {},
    'mulheres-que-correm-com-os-lobos': {},
    'padrao-bitcoin': {},
    'quem-mexeu-no-queijo': {},
    'sound-design': {}
}

def extract_json_blocks(content):
    parts = re.split(r'^===\s*([a-z0-9-]+)\s*===\s*$', content, flags=re.MULTILINE)
    if len(parts) > 1:
        for i in range(1, len(parts), 2):
            slug = parts[i]
            block = parts[i+1]
            match = re.search(r'```json(.*?)```', block, re.DOTALL)
            if match:
                try:
                    data = json.loads(match.group(1).strip())
                    for ch, ch_data in data.items():
                        if slug in book_data:
                            book_data[slug][ch] = ch_data
                except Exception as e:
                    print(f"Error parsing json for {slug}: {e}")

f1 = read_file('batch_6_out.md')
extract_json_blocks(f1)

f2 = read_file('batch_6_out_2.md')
extract_json_blocks(f2)

f3 = read_file('batch_6_out_3.md')
extract_json_blocks(f3)

f4 = read_file('batch_6_out_4.md')
extract_json_blocks(f4)

f5 = read_file('batch_6_out_5.md')
extract_json_blocks(f5)

f6 = read_file('batch_6_out_6.md')
extract_json_blocks(f6)

f7 = read_file('batch_6_out_7.md')
extract_json_blocks(f7)

with open(os.path.join(DIR, 'batch_6_out_8.json'), 'r', encoding='utf-8') as f:
    d8 = json.load(f)
    for b_slug, b_data in d8.items():
        if b_slug in book_data:
            for ch, ch_data in b_data.items():
                book_data[b_slug][ch] = ch_data

with open(os.path.join(DIR, 'batch_6_out.md'), 'w', encoding='utf-8') as f:
    for b_slug, b_data in book_data.items():
        f.write(f"=== {b_slug} ===\n```json\n")
        f.write(json.dumps(b_data, ensure_ascii=False, indent=2))
        f.write("\n```\n\n")

