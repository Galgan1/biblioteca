import os

master_file = r"C:\Users\User\.gemini\config\skills\drdolabela\MASTER_MIND.md"
reports_dir = r"C:\Users\User\.gemini\antigravity\scratch\biblioteca"

master_content = "# MASTER MIND: Grafo Central de Conhecimento\n\n"
master_content += "Este documento unifica as análises profundas das 217 obras, categorizando as linhas de força, convergências filosóficas e conexões esotéricas extraídas pelos agentes de Knowledge Graph.\n\n"
master_content += "---\n\n"

for i in range(1, 6):
    report_path = os.path.join(reports_dir, f"kg_report_{i}.md")
    if os.path.exists(report_path):
        with open(report_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            
        # Ignore first line if it's the title
        if lines and lines[0].startswith("# Knowledge"):
            lines = lines[1:]
            
        master_content += f"## Síntese do Nodo {i}\n\n"
        master_content += "".join(lines) + "\n\n---\n\n"
    else:
        master_content += f"## Síntese do Nodo {i}\n\nRelatório não encontrado.\n\n---\n\n"

with open(master_file, "w", encoding="utf-8") as f:
    f.write(master_content)

print("MASTER_MIND.md unificado com sucesso!")
