import re
import json

def parse_bibliography(filepath):
    books = []
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    for line in lines:
        line = line.strip()
        if not line or line.startswith("<USER_REQUEST>") or line.startswith("quero que") or line.startswith("Bibliografia"):
            continue
            
        # Example line: Acker, Clara Britto. 2008. “Dioniso, Diotima, Sócrates e a Erosofia”, in.: AISTHE, n. 3, 16–29.
        # Example line: Agostinho. 2017. Confissões. Tradução de Lorenzo Mammi. São Paulo: Companhia das Letras.
        
        # We need to distinguish between articles (have quotes "") and books (italics/no quotes, but in plain text usually just title before period)
        if '“' in line or '"' in line:
            # It's an article, maybe ignore or keep? "nos livros da lista" implies books.
            is_book = False
        else:
            is_book = True
            
        # Let's extract author, year, title.
        # usually format is: Author. Year. Title.
        parts = line.split('. ', 2)
        if len(parts) >= 3:
            author = parts[0]
            year = parts[1]
            title = parts[2].split('. ')[0] if is_book else parts[2]
            
            books.append({
                "author": author,
                "year": year,
                "title": title,
                "is_book": is_book,
                "full_line": line
            })
            
    with open("parsed_bibliography.json", "w", encoding="utf-8") as out:
        json.dump(books, out, indent=2, ensure_ascii=False)

parse_bibliography("full_bibliography_message.txt")
