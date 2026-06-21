import json

# List of keywords for the books identified in the prompt
book_keywords = [
    "agostinho-confissoes",
    "apolodoro-library",
    "apolonio-argonauticas",
    "aristofanes-nuvens",
    "aristofanes-birds",
    "aristofanes-vespas",
    "aristoteles-problemata",
    "aristoteles-etica",
    "aristoteles-fisica",
    "aristoteles-metafisica",
    "aristoteles-retorica",
    "aristoteles-poetica",
    "ateneu-deipnosophists",
    "bergson-pensamento",
    "cicero-nature",
    "descartes-meditacoes",
    "descartes-discurso",
    "diogenes-vidas",
    "epicuro-cartas",
    "epiteto-handbook",
    "epiteto-discourses",
    "foucault-hermeneutica",
    "foucault-historia-sexualidade",
    "freud-conferencias",
    "harari-sapiens",
    "harari-homo-deus",
    "harari-21-licoes",
    "hegel-fenomenologia",
    "herodoto-historia",
    "hesiodo-teogonia",
    "hesiodo-trabalhos",
    "homero-iliada",
    "homero-odisseia",
    "jung-mysterium",
    "marco-aurelio-meditacoes",
    "nietzsche-alem-do-bem",
    "nietzsche-ecce-homo",
    "nietzsche-genealogia",
    "nietzsche-nascimento",
    "nietzsche-gaia-ciencia",
    "nietzsche-crepusculo",
    "ovidio-metamorfoses",
    "pascal-pensamentos",
    "platao-leis",
    "platao-carta-vii",
    "platao-teeteto",
    "platao-fedon",
    "platao-fedro",
    "platao-banquete",
    "platao-republica",
    "platao-timeu",
    "platao-apologia",
    "platao-cratilo",
    "platao-alcibiades",
    "platao-gorgias",
    "platao-politico",
    "plutarco-vidas",
    "seneca-cartas",
    "seneca-natural-questions",
    "schopenhauer-mundo-vontade",
    "schopenhauer-essays"
]

with open("skills_list.json", "r", encoding="utf-8") as f:
    skills = json.load(f)

matched_skills = []
for skill in skills:
    for kw in book_keywords:
        # fuzzy match
        parts = kw.split("-")
        if all(p in skill.lower() for p in parts):
            matched_skills.append(skill)
            break

with open("matched_books.json", "w", encoding="utf-8") as f:
    json.dump(matched_skills, f, indent=2)

print(f"Encontrados {len(matched_skills)} livros na biblioteca.")
