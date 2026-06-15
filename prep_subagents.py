import json
import re

prompt_file = r"C:\Users\User\.gemini\antigravity\scratch\biblioteca\_kit_preview\PROMPT-GEMINI-COMPLETO.md"
out_file = r"C:\Users\User\.gemini\antigravity\scratch\biblioteca\phase2_payloads.json"

with open(prompt_file, 'r', encoding='utf-8') as f:
    content = f.read()

# The system prompt is everything before "# OS LIVROS" or "### LIVRO"
parts = content.split("### LIVRO ", 1)
system_instructions = parts[0]
books_content = "### LIVRO " + parts[1]

# Split by "### LIVRO " to get individual books
book_blocks = ["### LIVRO " + b for b in books_content.split("### LIVRO ") if b.strip()]

# Distribute into 10 batches
num_batches = 10
batches = [[] for _ in range(num_batches)]
for i, book in enumerate(book_blocks):
    batches[i % num_batches].append(book)

# Format each batch as a single string
batch_strings = ["\n\n".join(b) for b in batches]

output_data = {
    "system_prompt": system_instructions,
    "batches": batch_strings
}

with open(out_file, 'w', encoding='utf-8') as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print(f"Parsed {len(book_blocks)} books into 10 batches.")
