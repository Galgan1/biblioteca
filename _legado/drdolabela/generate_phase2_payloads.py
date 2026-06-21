import json

with open(r"C:\Users\User\.gemini\antigravity\scratch\biblioteca\mapped_books.json", 'r', encoding='utf-8') as f:
    books = json.load(f)

skills = [b['skill'] for b in books]

chunks = [skills[i:i + 44] for i in range(0, len(skills), 44)]

hyperlink_payloads = []
kg_payloads = []

for idx, chunk in enumerate(chunks, 1):
    chunk_str = "\n- ".join([""] + chunk)
    
    hyperlink_prompt = f"Implement semantic hyperlinking for the following skills (Lote {idx}):{chunk_str}\nWhen finished, reply exactly with the word 'DONE' and nothing else."
    
    kg_prompt = f"Build the Knowledge Graph partial report (save to kg_report_{idx}.md) for the following skills (Lote {idx}):{chunk_str}\nWhen finished, reply exactly with the word 'DONE' and nothing else."
    
    hyperlink_payloads.append({
        "TypeName": "drdolabela_hyperlinker",
        "Role": f"Hyperlinker Lote {idx}",
        "Prompt": hyperlink_prompt
    })
    
    kg_payloads.append({
        "TypeName": "drdolabela_kg_builder",
        "Role": f"KG Builder Lote {idx}",
        "Prompt": kg_prompt
    })

payloads = {
    "hyperlink": hyperlink_payloads,
    "kg": kg_payloads
}

with open(r"C:\Users\User\.gemini\antigravity\scratch\biblioteca\phase2_payloads.json", "w", encoding="utf-8") as f:
    json.dump(payloads, f, indent=2)

print("Payloads gerados!")
