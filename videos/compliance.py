# -*- coding: utf-8 -*-
"""Conferente de direitos — lar CANÔNICO das regras de direito do estúdio (bloqueantes).

Três frentes, todas locais/grátis:
  1. Link de afiliado só de PRODUTO Amazon (/dp/, /gp/) — nunca busca (s?k=).
  2. Prompt de imagem sem PROPRIEDADE INTELECTUAL protegida (personagem/marca) — gerar
     "Mickey Mouse"/"Batman" é risco de direito autoral; cena descritiva é segura.
  3. Trilha com licença limpa (procedural própria / CC0) — nunca áudio externo de origem incerta.

O `qc.py` (Gate 2) importa daqui a regra de link e chama `auditar()` — este módulo é a
fonte única; o gate apenas orquestra. Não importa `qc` (evita ciclo).

Uso:  python compliance.py roteiros/<slug>.json
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent

# IP protegida que não pode aparecer em prompt de imagem (conservador p/ evitar falso
# positivo em cena descritiva). Personagens/marcas de alto risco de direito autoral.
_IP_PROTEGIDA = [
    'mickey', 'minnie', 'disney', 'pixar', 'marvel', 'batman', 'superman',
    'spider-man', 'spiderman', 'homem-aranha', 'star wars', 'darth vader',
    'harry potter', 'hogwarts', 'pikachu', 'pokemon', 'pokémon', 'mario bros',
    'super mario', 'hello kitty', 'coca-cola', 'nike', 'adidas', 'apple logo',
]

# Fontes de trilha com licença limpa (próprias/livres).
_TRILHA_OK = {'procedural', 'propria', 'própria', 'cc0', 'autoral', ''}


def link_amazon_valido(url):
    """True se for link de PRODUTO Amazon (/dp/ ou /gp/); False se busca (s?k=) ou outro."""
    u = (url or '').lower()
    if 's?k=' in u or '/s?' in u:
        return False
    return '/dp/' in u or '/gp/' in u


def auditar_links(links):
    """-> falhas (BLOQUEANTE): todo link de afiliado tem de ser de produto."""
    return [f'link de afiliado inválido (não é /dp//gp/): {u}'
            for u in (links or []) if not link_amazon_valido(u)]


def prompt_seguro(texto):
    """-> lista de IP protegida encontrada no prompt (vazia = seguro)."""
    t = (texto or '').lower()
    return [ip for ip in _IP_PROTEGIDA
            if re.search(r'(?<![\w-])' + re.escape(ip) + r'(?![\w-])', t)]


def licenca_trilha_ok(fonte):
    """True se a trilha tem licença limpa: procedural própria, CC0, ou booleano (procedural).
    False para qualquer arquivo/fonte externa de origem incerta."""
    if isinstance(fonte, bool) or fonte is None:
        return True                                   # musica=True → trilha procedural própria
    return str(fonte).strip().lower() in _TRILHA_OK


def auditar(cfg):
    """Audita um roteiro: prompts de imagem (IP) + licença de trilha. -> (falhas, avisos).
    NÃO checa links aqui (o gate `qc` já faz, usando link_amazon_valido daqui — sem duplicar)."""
    falhas, avisos = [], []
    estilo = cfg.get('estilo_img', '')
    for i, c in enumerate(cfg.get('cenas', [])):
        prompt = f"{c.get('img', '')} {estilo}"
        ip = prompt_seguro(prompt)
        if ip:
            falhas.append(f'cena {i+1}: prompt com IP protegida {ip}')
    if not licenca_trilha_ok(cfg.get('musica')):
        falhas.append(f"trilha de origem incerta: {cfg.get('musica')!r} (use procedural/CC0)")
    return falhas, avisos


def main():
    if len(sys.argv) < 2:
        sys.exit('uso: python compliance.py <roteiro.json>')
    cfg = json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
    falhas, avisos = auditar(cfg)
    print('=== Conferente de direitos ===')
    print(f'FALHAS ({len(falhas)}):' if falhas else 'FALHAS: nenhuma')
    for x in falhas:
        print('  [REPROVA]', x)
    for x in avisos:
        print('  [aviso]', x)
    code = 1 if falhas else 0
    print(f"\nVEREDICTO: {'APROVADO' if code == 0 else 'REPROVADO'} (exit {code})")
    return code


if __name__ == '__main__':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.exit(main())
