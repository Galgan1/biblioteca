import json
import os

books = [
    {"slug": "de-zero-a-um", "file": "gen_b3.json"},
    {"slug": "habitos-atomicos", "file": "gen_b4.json"},
    {"slug": "mais-esperto-que-o-diabo", "file": "gen_b5.json"},
    {"slug": "noites-brancas", "file": "gen_b6.json"},
    {"slug": "poder-do-habito", "file": "gen_b7.json"},
    {"slug": "sapiens", "file": "gen_b8.json"},
    {"slug": "trabalho-focado", "file": "gen_b9.json"},
]

def fix_loops(text):
    if not isinstance(text, str): return text
    # Fix book 7
    text = text.replace(" caladas cegas frias rústicas gordas velhas cegas falsas surdas pesadas pesadas densas lentas...", ".")
    text = text.replace(" velha amarga parda oca falsa, cortando o laço mudo falso e sujo e sujo sujo pardo", ", cortando o laço da inércia corporativa")
    text = text.replace(" duras grossas rudes e cruas densas lentas", " e difíceis")
    text = text.replace(" escuro sujo sujo grosso falho cego cego morno frio mole mudo surdo", " ineficiente e falho")
    text = text.replace(" raros ciegos ciegos crus", " que não percebemos")
    text = text.replace(" com crueldade letal veloz livre clara e reta e cega cega", " de forma implacável e silenciosa")
    text = text.replace(" miúdos bobos sujos largados no piso branco sujo cego mudo", " do dia a dia")
    # Fix book 9
    text = text.replace(" rachado solto pobre pardo trêmulo triste sujo e podre e feio", " mal-feito")
    text = text.replace(" trágicas velhas gastas tolas", " trágicas")
    text = text.replace(" curtas fáceis que apenas deprimem a manhã morna", " fúteis que empobrecem o dia")
    text = text.replace(" do corpo isolado forte puro calado sério leve frio rápido reto", " de quem trabalha focado")
    text = text.replace(" sofá solto mudo tonto sujo e inerte do domingo murcho bobo cinza e pobre tonto fofo", " tédio dominical")
    text = text.replace(" prancha frouxa solta leve exata pura séria dura grossa feia rústica viva plena... Pare", " prancha")
    return text

def walk_and_fix(d):
    if isinstance(d, dict):
        for k, v in d.items():
            if isinstance(v, str):
                d[k] = fix_loops(v)
            else:
                walk_and_fix(v)
    elif isinstance(d, list):
        for i, item in enumerate(d):
            if isinstance(item, str):
                d[i] = fix_loops(item)
            else:
                walk_and_fix(item)

out_text = ""
with open("chunk1.txt", "r", encoding="utf-8") as f:
    out_text += f.read().strip() + "\n\n"

for b in books:
    with open(b["file"], "r", encoding="utf-8") as f:
        data = json.load(f)
        
    # Some of my files wrapped the chapters inside the book slug, some didn't.
    # We want the chapters directly under the book.
    if b["slug"] in data:
        chapters = data[b["slug"]]
    else:
        chapters = data
        
    walk_and_fix(chapters)
    
    out_text += f"=== {b['slug']} ===\n"
    out_text += "```json\n"
    out_text += json.dumps(chapters, ensure_ascii=False, indent=2)
    out_text += "\n```\n\n"

with open("batch_0_out.md", "w", encoding="utf-8") as f:
    f.write(out_text.strip() + "\n")

