# -*- coding: utf-8 -*-
"""Corrige markdown cru nos capitulos do maquiavel, remove licoes vazias
e adiciona navegacao anterior/proximo aos capitulos do keller."""
import re
from pathlib import Path

BASE = Path(__file__).parent

def fix_markdown(text):
    changes = 0
    lines = text.split('\n')
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r'^(\s*)<p>\*\s+(.*?)</p>\s*$', line)
        if m:
            indent = m.group(1)
            items = []
            while i < len(lines):
                m2 = re.match(r'^\s*<p>\*\s+(.*?)</p>\s*$', lines[i])
                if not m2:
                    break
                items.append(m2.group(1))
                i += 1
            out.append(indent + '<ul class="content-list">')
            for item in items:
                out.append(indent + '    <li>' + item + '</li>')
            out.append(indent + '</ul>')
            changes += len(items)
            continue
        m = re.match(r'^(\s*)<p>###\s*(.*?)</p>\s*$', line)
        if m:
            out.append(m.group(1) + '<h3>' + m.group(2) + '</h3>')
            changes += 1
            i += 1
            continue
        out.append(line)
        i += 1
    text = '\n'.join(out)

    # negrito **texto** -> <strong>
    text, n = re.subn(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    changes += n
    # italico *texto* -> <em> (apenas em linhas de conteudo)
    new_lines = []
    for line in text.split('\n'):
        if '*' in line and re.match(r'^\s*<(p|li|blockquote)[ >]', line.strip() and line.lstrip() or ''):
            line, n = re.subn(r'\*([^*<>]+?)\*', r'<em>\1</em>', line)
            changes += n
        new_lines.append(line)
    text = '\n'.join(new_lines)

    # secao de licoes vazia -> remover
    text, n = re.subn(
        r'\n\s*<section class="lessons[^>]*>\s*<h2[^>]*>[^<]*</h2>\s*<ul class="lessons-list">\s*</ul>\s*</section>',
        '', text)
    changes += n
    return text, changes


# --- 1. Maquiavel: markdown cru + licoes vazias ---
for f in sorted((BASE / 'maquiavel-pedagogo').glob('*.html')):
    text = f.read_text(encoding='utf-8')
    text, changes = fix_markdown(text)
    if changes:
        f.write_text(text, encoding='utf-8')
        print(f'{f.name}: {changes} correcoes')

# --- 2. Maquiavel: rotulos das pontas da navegacao ---
ch00 = BASE / 'maquiavel-pedagogo' / 'ch00-introducao.html'
t = ch00.read_text(encoding='utf-8')
t2 = t.replace('class="chapter-nav-link">&larr; Anterior</a>', 'class="chapter-nav-link">&larr; Visão Geral</a>')
if t2 != t:
    ch00.write_text(t2, encoding='utf-8')
    print('ch00: rotulo "Visão Geral"')
ch15 = BASE / 'maquiavel-pedagogo' / 'ch15-conclusao.html'
t = ch15.read_text(encoding='utf-8')
t2 = t.replace('class="chapter-nav-link">Próximo &rarr;</a>', 'class="chapter-nav-link">Visão Geral &rarr;</a>')
if t2 != t:
    ch15.write_text(t2, encoding='utf-8')
    print('ch15: rotulo "Visão Geral"')

# --- 3. Keller: adicionar navegacao anterior/proximo ---
ordem = ['introducao.html'] + [f'capitulo-{n}.html' for n in range(1, 9)]
OVERVIEW = '../keller-casamento.html'
for idx, name in enumerate(ordem):
    f = BASE / 'keller-casamento' / name
    text = f.read_text(encoding='utf-8')
    if 'chapter-nav' in text:
        print(f'{name}: navegacao ja existe, pulando')
        continue
    prev_href = ordem[idx - 1] if idx > 0 else OVERVIEW
    prev_label = 'Anterior' if idx > 0 else 'Visão Geral'
    next_href = ordem[idx + 1] if idx < len(ordem) - 1 else OVERVIEW
    next_label = 'Próximo' if idx < len(ordem) - 1 else 'Visão Geral'
    nav = (
        '\n            <nav aria-label="Navegação entre capítulos" class="chapter-nav">\n'
        f'                <a href="{prev_href}" class="chapter-nav-link">&larr; {prev_label}</a>\n'
        f'                <a href="{next_href}" class="chapter-nav-link">{next_label} &rarr;</a>\n'
        '            </nav>\n        </main>'
    )
    assert text.count('</main>') == 1, f'{name}: </main> ambiguo'
    text = text.replace('</main>', nav)
    f.write_text(text, encoding='utf-8')
    print(f'{name}: navegacao adicionada ({prev_label} <- -> {next_label})')

print('Concluido.')
