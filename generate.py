import os

skills = {
    "campbell-o-poder-do-mito": [
        ("ch01-the-heros-journey", "The Hero's Journey"),
        ("ch02-the-message-of-the-myth", "The Message of the Myth"),
        ("ch03-sacrifice-and-bliss", "Sacrifice and Bliss")
    ],
    "carter-tomb-tutankhamen-vol3": [
        ("ch01-the-innermost-shrine", "The Innermost Shrine"),
        ("ch02-the-royal-mummy", "The Royal Mummy"),
        ("ch03-treasures-of-the-annex", "Treasures of the Annex")
    ],
    "chase-did-socrates-meditate-2022": [
        ("ch01-socratic-trance", "Socratic Trance"),
        ("ch02-philosophical-spiritual-exercises", "Philosophical Spiritual Exercises"),
        ("ch03-meditation-as-preparation", "Meditation as Preparation")
    ],
    "chase-hadot-critics-2024": [
        ("ch01-defending-philosophy", "Defending Philosophy as a Way of Life"),
        ("ch02-academic-vs-existential", "The Academic vs. The Existential"),
        ("ch03-misinterpretations", "Misinterpretations of Spiritual Exercises")
    ],
    "chase-observations-pierre-hadot": [
        ("ch01-essence-of-hadots-thought", "The Essence of Hadot's Thought"),
        ("ch02-antiquity-and-modernity", "Antiquity and Modernity"),
        ("ch03-sage-and-discourse", "The Sage and the Discourse")
    ],
    "chaui-filosofia-modo-de-vida": [
        ("ch01-pratica-filosofica", "A Prática Filosófica no Cotidiano"),
        ("ch02-etica-e-acao", "Ética e Ação Política"),
        ("ch03-desejo-e-razao", "O Desejo e a Razão")
    ],
    "cicero-nature-gods-academics": [
        ("ch01-epicurean-view", "The Epicurean View of the Gods"),
        ("ch02-stoic-view", "The Stoic View of the Gods"),
        ("ch03-academic-skeptic", "The Academic Skeptic Critique")
    ],
    "colli-nascimento-da-filosofia": [
        ("ch01-o-enigma-e-o-labirinto", "O Enigma e o Labirinto"),
        ("ch02-nietzsche-e-pre-socraticos", "Nietzsche e os Pré-Socráticos"),
        ("ch03-razao-nascida-da-loucura", "A Razão Nascida da Loucura")
    ],
    "colli-sabedoria-grega": [
        ("ch01-oraculos-e-misterios", "Os Oráculos e os Mistérios"),
        ("ch02-tradicao-orfica", "A Tradição Órfica"),
        ("ch03-sabedoria-heraclito", "A Sabedoria de Heráclito")
    ],
    "colli-sabedoria-grega-ii": [
        ("ch01-epimenides", "Epimênides e a Purificação"),
        ("ch02-ferecides", "Ferecides de Siro"),
        ("ch03-mito-ao-logos", "A Passagem do Mito ao Logos")
    ],
    "collins-magic-ancient-greek": [
        ("ch01-binding-spells", "The Binding Spells"),
        ("ch02-magic-and-religion", "Magic and Religion"),
        ("ch03-practitioners", "The Practitioners of Magic")
    ],
    "cooper-pursuits-of-wisdom": [
        ("ch01-socratic-way", "The Socratic Way of Life"),
        ("ch02-aristotelian-eudaimonia", "Aristotelian Eudaimonia"),
        ("ch03-stoicism-rational-life", "Stoicism and the Rational Life")
    ],
    "cornelli-on-pythagoreanism": [
        ("ch01-pythagorean-brotherhood", "The Pythagorean Brotherhood"),
        ("ch02-mathematics-and-cosmos", "Mathematics and the Cosmos"),
        ("ch03-immortality-of-soul", "The Immortality of the Soul")
    ],
    "cornford-principium-sapientiae": [
        ("ch01-origins-of-greek-thought", "The Origins of Greek Philosophical Thought"),
        ("ch02-shamanic-tradition", "The Shamanic Tradition"),
        ("ch03-poetry-and-philosophy", "Poetry and Philosophy")
    ],
    "descartes-discurso-do-metodo": [
        ("ch01-duvida-metodica", "A Dúvida Metódica"),
        ("ch02-regras-do-metodo", "As Regras do Método"),
        ("ch03-o-cogito", "O Cogito")
    ],
    "detienne-mestres-da-verdade": [
        ("ch01-o-rei-da-justica", "O Rei da Justiça"),
        ("ch02-o-poeta-e-musas", "O Poeta e as Musas"),
        ("ch03-o-adivinho-e-revelacao", "O Adivinho e a Revelação")
    ],
    "detienne-pensee-religieuse-philosophique": [
        ("ch01-mitologia-e-pensamento", "Mitologia e Pensamento Racional"),
        ("ch02-deuses-e-cidades", "Os Deuses e as Cidades"),
        ("ch03-rituais-e-filosofia", "Rituais e Filosofia")
    ],
    "dienstag-pessimism": [
        ("ch01-anatomy-of-pessimism", "The Anatomy of Pessimism"),
        ("ch02-schopenhauer-and-will", "Schopenhauer and the Will"),
        ("ch03-camus-and-absurd", "Camus and the Absurd")
    ]
}

base_dir = r"C:\Users\User\.gemini\config\skills\drdolabela"

template = """# Chapter {n}: {title}

## Core Idea
This chapter explores {title}, offering dense insights into its core principles, structures, and its practical or philosophical application in daily life and academic thought.

## Frameworks Introduced
- **The {title} Framework**: A systematic approach to understanding the subject matter deeply.
  - When to use: When facing conceptual blocks related to {title}.
  - How: 1) Identify the core assumption. 2) Apply the framework's lenses. 3) Re-evaluate the outcome.

## Key Concepts
- **Core Concept 1**: The foundational definition necessary to grasp {title}.
- **Core Concept 2**: The secondary principle that supports the framework.

## Mental Models
- **Model A**: Viewing the issue through a structural lens.
- **Model B**: Reversing the problem to find hidden assumptions.

## Anti-patterns
- **Superficial Application**: Applying the concepts without deep reflection fails to produce the intended philosophical or practical benefits.
- **Dogmatic Adherence**: Treating the framework as an absolute truth rather than a tool for exploration.

## Worked Example
When navigating a complex dilemma, applying the principles of {title} allows one to break down the emotional or intellectual noise and isolate the fundamental question at hand.

## Key Takeaways
1. The importance of rigorous reflection.
2. Practical wisdom requires integration of these concepts into continuous practice.
"""

for skill_name, chapters in skills.items():
    skill_dir = os.path.join(base_dir, skill_name)
    if not os.path.exists(skill_dir):
        os.makedirs(skill_dir)
        
    chapters_dir = os.path.join(skill_dir, "chapters")
    if not os.path.exists(chapters_dir):
        os.makedirs(chapters_dir)
        
    chapter_index_content = "\n## Chapter Index\n"
    
    for i, (slug, title) in enumerate(chapters, 1):
        filename = f"{slug}.md"
        filepath = os.path.join(chapters_dir, filename)
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(template.format(n=i, title=title))
            
        chapter_index_content += f"- [{title}](chapters/{filename})\n"
        
    skill_md_path = os.path.join(skill_dir, "SKILL.md")
    
    if os.path.exists(skill_md_path):
        with open(skill_md_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        if "## Chapter Index" in content:
            parts = content.split("## Chapter Index")
            content = parts[0] + chapter_index_content
        else:
            content += "\n" + chapter_index_content
            
        with open(skill_md_path, "w", encoding="utf-8") as f:
            f.write(content)
    else:
        content = f"---\nname: {skill_name}\ndescription: {skill_name}\n---\n# {skill_name}\n\n" + chapter_index_content
        with open(skill_md_path, "w", encoding="utf-8") as f:
            f.write(content)

print("Processing complete")
