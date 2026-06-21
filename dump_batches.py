import json
import os

in_file = r"C:\Users\User\.gemini\antigravity\scratch\biblioteca\phase2_payloads.json"
out_dir = r"C:\Users\User\.gemini\antigravity\scratch\biblioteca\_kit_preview\gemini_in"

os.makedirs(out_dir, exist_ok=True)

with open(in_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

for i, batch in enumerate(data['batches']):
    out_path = os.path.join(out_dir, f"batch_{i}.md")
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(batch)

print("Created 10 batch files.")
