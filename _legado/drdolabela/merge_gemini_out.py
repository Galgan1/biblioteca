import os
import glob

in_dir = r"C:\Users\User\.gemini\antigravity\scratch\biblioteca\_kit_preview\gemini_in"
out_file = r"C:\Users\User\.gemini\antigravity\scratch\biblioteca\_kit_preview\gemini_out.md"

batch_files = []
for i in range(10):
    bf = os.path.join(in_dir, f"batch_{i}_out.md")
    if os.path.exists(bf):
        batch_files.append(bf)

# We expect 10 files
if len(batch_files) == 10:
    with open(out_file, 'w', encoding='utf-8') as outfile:
        for f in batch_files:
            with open(f, 'r', encoding='utf-8') as infile:
                outfile.write(infile.read() + "\n\n")
    print(f"Sucesso! {len(batch_files)} arquivos mesclados em gemini_out.md")
else:
    print(f"Atenção: Apenas {len(batch_files)} arquivos de saída encontrados.")
