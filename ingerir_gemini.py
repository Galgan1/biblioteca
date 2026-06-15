# -*- coding: utf-8 -*-
"""Ingere a resposta do Gemini (trabalho massivo) de volta no pipeline.

A resposta vem como blocos `=== <slug> ===` seguidos de um ```json {cap: {"cards":[...]}}```.
Salve a resposta colada em _kit_preview/gemini_out.md (pode colar vários "continuar"
no mesmo arquivo) e rode:

  python ingerir_gemini.py                 # lê _kit_preview/gemini_out.md, grava text/<slug>.json e aplica
  python ingerir_gemini.py arquivo.md      # outro arquivo de entrada
  python ingerir_gemini.py --no-apply      # só extrai os JSON, não aplica ainda
"""
import re, json, sys, subprocess
from pathlib import Path

BASE = Path(__file__).parent
sys.stdout.reconfigure(encoding='utf-8')
TEXT = BASE / '_kit_preview' / 'text'

BLOCK = re.compile(r'===\s*([a-z0-9-]+)\s*===\s*```(?:json)?\s*(\{.*?\})\s*```', re.DOTALL)


def main():
    args = [a for a in sys.argv[1:]]
    apply = '--no-apply' not in args
    args = [a for a in args if a != '--no-apply']
    src = Path(args[0]) if args else (BASE / '_kit_preview' / 'gemini_out.md')
    if not src.is_file():
        sys.exit(f'entrada não encontrada: {src} (cole a resposta do Gemini aí)')
    text = src.read_text(encoding='utf-8')
    TEXT.mkdir(parents=True, exist_ok=True)
    slugs = []
    for slug, blob in BLOCK.findall(text):
        try:
            obj = json.loads(blob)
        except json.JSONDecodeError as e:
            print(f'  [!] {slug}: JSON inválido ({e}) — pulado'); continue
        (TEXT / f'{slug}.json').write_text(json.dumps(obj, ensure_ascii=False), encoding='utf-8', newline='\n')
        slugs.append(slug)
    print(f'{len(slugs)} livros extraídos: {", ".join(slugs) or "—"}')
    if apply and slugs:
        print('\naplicando…')
        subprocess.run([sys.executable, str(BASE / 'aplicar_texto.py'), *slugs])
        print('\nrevise e rode:  python gerar_livro.py <slug>  + deploy, p/ cada livro.')


if __name__ == '__main__':
    main()
