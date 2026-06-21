import os

skills_base_dir = r"C:\Users\User\.gemini\config\skills"
lote3_skills = [
    "grimal-dicionario-mitologia",
    "grof-adventure-self-discovery",
    "guthrie-pythagorean-sourcebook",
    "guthrie-orpheus-greek-religion",
    "bernabe-platao-e-o-orfismo",
    "hadot-marius-victorinus",
    "chase-observations-pierre-hadot",
    "hadot-philosophie-antique",
    "hadot-inner-citadel",
    "hadot-maniere-de-vivre",
    "hadot-exercices-spirituels",
    "lucrecio-sobre-a-natureza-das-coisas",
    "hadot-wittgenstein-limites",
    "hadot-discours-mode-vie",
    "hadot-plotino-simplicidade",
    "hadot-selected-writings-practice",
    "hanegraaff-hermetic-spirituality",
    "foucault-technologies-of-the-self",
    "harari-sapiens",
    "harari-homo-deus",
    "harari-21-licoes",
    "ambury-philosophy-as-a-way-of-life",
    "hegel-fenomenologia-do-espirito",
    "hesiodo-trabalhos-e-dias",
    "homero-iliada",
    "homero-odisseia",
    "huxley-perennial-philosophy",
    "huxley-doors-of-perception",
    "inwood-poem-of-empedocles",
    "jaeger-theology-early-greek-philosophers",
    "jamblico-vie-de-pythagore",
    "jung-symbols-of-transformation",
    "jung-psychology-and-religion",
    "jung-alchemical-studies",
    "jung-mysterium-coniunctionis",
    "kardec-livro-dos-espiritos",
    "killen-mycenaean-greek",
    "kingsley-ancient-philosophy-mystery-magic",
    "kingsley-dark-places-of-wisdom",
    "kingsley-reality"
]
missing = []
for s in lote3_skills:
    p = os.path.join(skills_base_dir, s)
    if not os.path.isdir(p): missing.append(s)

print(f"Missing: {len(missing)} out of {len(lote3_skills)}")
if missing: print(missing)
