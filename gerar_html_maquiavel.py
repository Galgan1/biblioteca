import os
import re
import shutil

# Paths
SKILL_DIR = r"C:\Users\User\.gemini\config\skills\maquiavel-pedagogo\chapters"
TARGET_DIR = r"c:\Users\User\.gemini\antigravity\scratch\biblioteca\maquiavel-pedagogo"
ASSETS_DIR = r"c:\Users\User\.gemini\antigravity\scratch\biblioteca\assets"
BASE_DIR = r"c:\Users\User\.gemini\antigravity\scratch\biblioteca"

# Ensure target directory exists
os.makedirs(TARGET_DIR, exist_ok=True)

# 1. Copy Cover Image
source_cover = r"C:\Users\User\.gemini\antigravity\brain\f697a393-3bad-4e7c-acbd-bf5a23affa85\maquiavel_cover_png_1781130111298.png"
if os.path.exists(source_cover):
    shutil.copy(source_cover, os.path.join(ASSETS_DIR, "maquiavel-cover.png"))

# 2. Copy script.js from keller-casamento
keller_dir = os.path.join(BASE_DIR, "keller-casamento")
if os.path.exists(os.path.join(keller_dir, "script.js")):
    shutil.copy(os.path.join(keller_dir, "script.js"), os.path.join(TARGET_DIR, "script.js"))

# Helper for HTML generation
def generate_chapter_html(chapter_file, md_content, chapter_num, total_chapters, chapter_files):
    # Parse Markdown
    title_match = re.search(r'^# (.+)$', md_content, re.MULTILINE)
    title = title_match.group(1) if title_match else f"Capítulo {chapter_num}"
    
    sections = {}
    current_section = None
    for line in md_content.split('\n'):
        if line.startswith('## '):
            current_section = line.replace('## ', '').strip()
            sections[current_section] = []
        elif current_section:
            sections[current_section].append(line)
            
    ideia_central = "\n".join(sections.get("Ideia Central", sections.get("Resumo", []))).strip()
    
    licoes_list = sections.get("Principais Lições", [])
    if not licoes_list:
        licoes_list = sections.get("Insights e Padrões de Manipulação", [])
    if not licoes_list:
        licoes_list = sections.get("Conclusão", [])
    licoes = "\n".join(licoes_list).strip()
    
    # Process sections into cards
    cards_html = ""
    card_index = 1
    
    skip_headers = ["Ideia Central", "Resumo", "Principais Lições", "Insights e Padrões de Manipulação", "Conclusão"]
    for sec_title, sec_content in sections.items():
        if sec_title in skip_headers:
            continue
        if "".join(sec_content).strip():
            content = "\n".join(sec_content).strip()
            # Basic parsing of lists to paragraphs or list items
            items = []
            for item in content.split('\n'):
                if item.startswith('- **'):
                    items.append(f"<p style='margin-bottom:0.5rem;'>{item.replace('- **', '<strong>').replace('**:', '</strong>:')}</p>")
                elif item.startswith('- '):
                    items.append(f"<p style='margin-bottom:0.5rem;'>&bull; {item[2:]}</p>")
                elif item.strip():
                    items.append(f"<p style='margin-bottom:0.5rem;'>{item}</p>")
                    
            body_html = "\n".join(items)
            
            cards_html += f"""
            <article class="card animate-entrance" style="--i: {card_index}">
                <div class="card-icon" aria-hidden="true">
                    <svg viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <circle cx="32" cy="32" r="24" stroke="currentColor" stroke-width="3"/>
                        <path d="M32 16V32L42 42" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>
                    </svg>
                </div>
                <div class="card-content">
                    <h2 class="card-title">{sec_title}</h2>
                    <div class="card-details">
                        <div class="card-details-inner">
                            {body_html}
                        </div>
                    </div>
                </div>
            </article>
            """
            card_index += 1

    # Process Lições
    licoes_html = ""
    for item in licoes.split('\n'):
        if item.strip().startswith(('1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.', '- ')):
            licoes_html += f"<li>{re.sub(r'^[0-9]+\.\s*|-\s*', '', item)}</li>\n"


    # Navigation
    prev_file = chapter_files[chapter_num-1].replace('.md', '.html') if chapter_num > 0 else "../maquiavel-pedagogo.html"
    next_file = chapter_files[chapter_num+1].replace('.md', '.html') if chapter_num < total_chapters - 1 else "../maquiavel-pedagogo.html"
    
    prev_link = prev_file
    next_link = next_file
    
    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Maquiavel Pedagogo</title>
    <meta name="theme-color" content="#ffffff">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;500;700;800&family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,600;0,7..72,700;1,7..72,400&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../assets/style.css">
</head>
<body>
    <div class="page">
        <nav aria-label="Navegação principal">
            <a href="../maquiavel-pedagogo.html" class="back-link" style="display:inline-block; margin-bottom: 1.5rem; color: var(--gray-dark); text-decoration: none; font-weight: 500;">&larr; Voltar para Visão Geral</a>
        </nav>

        <header class="header animate-entrance" style="--i: 0">
            <h1 class="header-title">
                <span class="header-title-light">MAQUIAVEL</span>
                <span class="header-title-bold">PEDAGOGO</span>
            </h1>
            <p class="header-subtitle">{title.upper()}</p>
            <p class="header-credit">Pascal Bernardin</p>
            <p class="header-intro">
                {ideia_central}
            </p>
        </header>

        <main id="conteudo">
            <div class="grid">
                {cards_html}
            </div>

            <section class="lessons animate-entrance" style="--i: {card_index}">
                <h2 class="lessons-title">Lições-Chave</h2>
                <ul class="lessons-list">
                    {licoes_html}
                </ul>
            </section>
            
            <div style="display: flex; justify-content: space-between; margin-top: 3rem;">
                <a href="{prev_link}" style="text-decoration: none; padding: 0.5rem 1rem; border: 1px solid var(--border); border-radius: 4px; color: var(--accent); font-weight: bold;">&larr; Anterior</a>
                <a href="{next_link}" style="text-decoration: none; padding: 0.5rem 1rem; border: 1px solid var(--border); border-radius: 4px; color: var(--accent); font-weight: bold;">Próximo &rarr;</a>
            </div>
        </main>

        <footer class="footer">
            <p class="footer-credit">Maquiavel Pedagogo · Pascal Bernardin</p>
        </footer>
    </div>
    <script src="script.js"></script>
</body>
</html>"""
    
    output_filename = os.path.basename(chapter_file).replace('.md', '.html')
    # Make sure we use generic chXX.html names for simpler navigation links (or just replace the name)
    out_path = os.path.join(TARGET_DIR, output_filename)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
        
    return output_filename, title

# Read chapters
chapter_files = [f for f in os.listdir(SKILL_DIR) if f.startswith('ch') and f.endswith('.md')]
chapter_files.sort()

chapter_links = []
for idx, ch_file in enumerate(chapter_files):
    with open(os.path.join(SKILL_DIR, ch_file), "r", encoding="utf-8") as f:
        md = f.read()
    filename, title = generate_chapter_html(ch_file, md, idx, len(chapter_files), chapter_files)
    chapter_links.append(f'<a href="maquiavel-pedagogo/{filename}" style="text-decoration: none; padding: 0.5rem 1rem; border: 1px solid var(--border); border-radius: 4px; color: var(--accent); font-weight: bold; background: rgba(0,0,0,0.02); margin-bottom: 0.5rem; display: block;">{title} &rarr;</a>')

# Generate overview page (maquiavel-pedagogo.html)
overview_html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Visão Geral: Maquiavel Pedagogo | Biblioteca</title>
    <meta name="theme-color" content="#ffffff">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;500;700;800&family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,600;0,7..72,700;1,7..72,400&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="maquiavel-pedagogo/style.css">
</head>
<body>
    <div class="page">
        <nav aria-label="Navegação Voltar">
            <a href="index.html" class="back-link" style="display:inline-block; margin-bottom: 1.5rem; color: var(--text-muted); text-decoration: none; font-weight: 500;">&larr; Voltar para a Biblioteca</a>
        </nav>

        <header class="header animate-entrance" style="--i: 0">
            <h1 class="header-title">
                <span class="header-title-light">MAQUIAVEL</span>
                <span class="header-title-bold">PEDAGOGO</span>
            </h1>
            <p class="header-subtitle">VISÃO GERAL DO LIVRO</p>
            <p class="header-credit">Pascal Bernardin</p>
            <p class="header-intro">
                Desvenda as técnicas de engenharia social aplicadas à educação pela UNESCO para formar o novo cidadão global através da subversão cognitiva e psicológica.
            </p>
        </header>

        <main id="conteudo">
            <div class="grid">
                
                <article class="card animate-entrance" style="--i: 1">
                    <div class="card-icon" aria-hidden="true">
                        <svg viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M32 8L4 56h56L32 8z" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/>
                            <path d="M32 24v16M32 50v-2" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>
                        </svg>
                    </div>
                    <div class="card-content">
                        <h2 class="card-title">Sinais de Alerta (Tells)</h2>
                        <p class="card-body">Como identificar a subversão em curso:</p>
                        <ul style="list-style-type: disc; margin-left: 1.5rem; color: var(--gray-dark); font-size: 0.95rem; margin-top: 0.5rem; margin-bottom: 1rem;">
                            <li style="margin-bottom: 0.5rem;"><strong>Educação moral por especialistas:</strong> Se é definida pelo Estado e não pela família.</li>
                            <li style="margin-bottom: 0.5rem;"><strong>Tolerância seletiva:</strong> Se exclui valores tradicionais/religiosos (revolução ética camuflada).</li>
                            <li style="margin-bottom: 0.5rem;"><strong>Autonomia concedida pelo Estado:</strong> É engajamento manipulatório, não liberdade real.</li>
                            <li style="margin-bottom: 0.5rem;"><strong>Ciência dita valores:</strong> Positivismo totalitário, pois valores não são científicos.</li>
                            <li style="margin-bottom: 0.5rem;"><strong>Nível escolar caindo:</strong> Se ninguém corrige, a queda é funcional ao projeto.</li>
                        </ul>
                    </div>
                </article>

                <article class="card animate-entrance" style="--i: 2">
                    <div class="card-icon" aria-hidden="true">
                        <svg viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <circle cx="32" cy="32" r="24" stroke="currentColor" stroke-width="3"/>
                            <path d="M32 16v16l8 8" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>
                        </svg>
                    </div>
                    <div class="card-content">
                        <h2 class="card-title">Limiares Críticos</h2>
                        <p class="card-body">Estatísticas da manipulação psicológica:</p>
                        <ul style="list-style-type: none; margin-top: 0.5rem; margin-bottom: 1rem;">
                            <li style="margin-bottom: 0.5rem;"><strong style="color: var(--green); font-size: 1.1rem;">60%</strong> obedecem à autoridade até o extremo (Milgram).</li>
                            <li style="margin-bottom: 0.5rem;"><strong style="color: var(--green); font-size: 1.1rem;">92%</strong> obedecem quando a ação é setorizada ou indireta.</li>
                            <li style="margin-bottom: 0.5rem;"><strong style="color: var(--green); font-size: 1.1rem;">75%</strong> cedem ao conformismo de grupo pelo menos uma vez (Asch).</li>
                            <li style="margin-bottom: 0.5rem;"><strong style="color: var(--green); font-size: 1.1rem;">1 aliado</strong> basta para neutralizar a pressão do grupo.</li>
                            <li style="margin-bottom: 0.5rem;"><strong style="color: var(--black);">Pressão Fraca > Forte</strong> para a interiorização de valores.</li>
                        </ul>
                    </div>
                </article>

                <article class="card card-wide animate-entrance" style="--i: 3">
                    <div class="card-content">
                        <h2 class="card-title">Regras de Decisão do Autor</h2>
                        <p class="card-body" style="margin-bottom: 1rem;">Como traduzir o jargão pedagógico ("Língua de Pau"):</p>
                        <div style="overflow-x: auto;">
                            <table style="width: 100%; border-collapse: collapse; font-size: 0.95rem; text-align: left;">
                                <tr style="border-bottom: 2px solid var(--gray-light);">
                                    <th style="padding: 0.75rem; color: var(--green);">Quando você vê...</th>
                                    <th style="padding: 0.75rem; color: var(--green);">Significa que...</th>
                                    <th style="padding: 0.75rem; color: var(--green);">Porque...</th>
                                </tr>
                                <tr style="border-bottom: 1px dashed var(--gray-light);">
                                    <td style="padding: 0.75rem;"><strong>"Métodos ativos"</strong></td>
                                    <td style="padding: 0.75rem; color: var(--gray-dark);">Técnica de engajamento</td>
                                    <td style="padding: 0.75rem; font-style: italic;">Atos aliciadores criam dissonância cognitiva.</td>
                                </tr>
                                <tr style="border-bottom: 1px dashed var(--gray-light);">
                                    <td style="padding: 0.75rem;"><strong>"Ensino não cognitivo"</strong></td>
                                    <td style="padding: 0.75rem; color: var(--gray-dark);">Modificar valores</td>
                                    <td style="padding: 0.75rem; font-style: italic;">Formação intelectual foi subordinada à "formação social".</td>
                                </tr>
                                <tr style="border-bottom: 1px dashed var(--gray-light);">
                                    <td style="padding: 0.75rem;"><strong>"Descentralização"</strong></td>
                                    <td style="padding: 0.75rem; color: var(--gray-dark);">Engajamento de professores</td>
                                    <td style="padding: 0.75rem; font-style: italic;">Participação aparente reduz oposição (pé-na-porta).</td>
                                </tr>
                                <tr>
                                    <td style="padding: 0.75rem;"><strong>"Direitos da criança"</strong></td>
                                    <td style="padding: 0.75rem; color: var(--gray-dark);">Arma contra a família</td>
                                    <td style="padding: 0.75rem; font-style: italic;">Única finalidade é reduzir a autoridade parental.</td>
                                </tr>
                            </table>
                        </div>
                    </div>
                </article>

                <article class="card card-wide card-dashed animate-entrance" style="--i: 4">
                    <div class="card-content">
                        <h2 class="card-title">Aprofunde-se nos Capítulos</h2>
                        <p class="card-body" style="margin-bottom: 1rem;">Acesse as notas detalhadas de cada capítulo:</p>
                        <nav aria-label="Navegação de Capítulos">
                            {"".join(chapter_links)}
                        </nav>
                    </div>
                </article>
            </div>
        </main>
        
        <footer class="footer">
            <p class="footer-credit">Resumo Geral — Baseado na Skill do Livro</p>
        </footer>
    </div>
    <script src="maquiavel-pedagogo/script.js"></script>
</body>
</html>"""

with open(os.path.join(BASE_DIR, "maquiavel-pedagogo.html"), "w", encoding="utf-8") as f:
    f.write(overview_html)

print("Geração HTML para Maquiavel Pedagogo concluída.")
