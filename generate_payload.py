import json

with open(r"C:\Users\User\.gemini\antigravity\scratch\biblioteca\mapped_books.json", 'r', encoding='utf-8') as f:
    books = json.load(f)

# Extract unique skills
unique_skills = list(set([item['skill'] for item in books]))
unique_skills.sort()

# Divide into 10 chunks
num_agents = 10
chunk_size = len(unique_skills) // num_agents + 1

subagents = []
for i in range(num_agents):
    chunk = unique_skills[i*chunk_size : (i+1)*chunk_size]
    if not chunk:
        continue
    
    prompt = "Crie a estrutura /book-to-skill (arquivos chXX na pasta chapters) para as seguintes skills:\n"
    for skill in chunk:
        prompt += f"- {skill}\n"
    
    subagents.append({
        "TypeName": "drdolabela_book_to_skill_applier",
        "Role": f"BookToSkill Lote {i+1}",
        "Prompt": prompt
    })

with open(r"C:\Users\User\.gemini\antigravity\scratch\biblioteca\subagents_payload.json", "w", encoding="utf-8") as f:
    json.dump(subagents, f, indent=2, ensure_ascii=False)
