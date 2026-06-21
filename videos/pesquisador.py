# -*- coding: utf-8 -*-
"""Pesquisador — gera e pontua GANCHOS (hooks) de abertura. Local, grátis, sem rede.

Usa as 5 fórmulas de gancho comprovadas (pesquisa de retenção 2025-26):
Bold Claim, Curiosity Gap, Direct Question, Visual Shock, Micro-Story. Preenche cada
fórmula com o título do livro + um conceito-chave e pontua por heurística de retenção
(brevidade + curiosidade + concretude). O Diretor/Roteirista escolhe entre os candidatos.

Sem IA e sem rede: é a base local. (Premium: um LLM pode refinar os candidatos.)

Uso:  python pesquisador.py roteiros/<slug>.json
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent

FORMULAS = ['bold_claim', 'curiosity_gap', 'direct_question', 'visual_shock', 'micro_story']

# Cada fórmula é um molde pt-BR preenchido com (titulo, conceito).
_MOLDES = {
    'bold_claim':      'A maioria entende {conceito} errado — e {titulo} mostra por quê.',
    'curiosity_gap':   'Existe uma ideia em {titulo} sobre {conceito} que quase ninguém comenta.',
    'direct_question': 'Você sabe por que {conceito} muda tudo? {titulo} responde.',
    'visual_shock':    '{conceito}: a virada de {titulo} que põe sua lógica de cabeça para baixo.',
    'micro_story':     'Quando li {titulo}, {conceito} mudou como eu penso — em três páginas.',
}

# Marcadores que abrem "loop de curiosidade" (sobem a pontuação).
_CURIOSIDADE = ('por que', 'quase ninguém', 'ninguém', 'errado', 'segredo',
                'virada', 'cabeça para baixo', 'muda tudo', 'ninguem')


def gerar_ganchos(titulo, conceito):
    """-> lista de {'formula', 'texto'}, uma por fórmula comprovada."""
    return [{'formula': f, 'texto': _MOLDES[f].format(titulo=titulo, conceito=conceito)}
            for f in FORMULAS]


def _palavras(t):
    return len(re.findall(r'\S+', t))


def pontuar_gancho(texto):
    """Heurística de retenção em [0,1]: brevidade + curiosidade + concretude.
    Não é verdade absoluta — é um ranqueador local para escolher entre candidatos."""
    t = (texto or '').lower()
    n = _palavras(texto)
    # brevidade: ideal <= 14 palavras; cai linearmente até 26
    brev = 1.0 if n <= 14 else max(0.0, 1 - (n - 14) / 12)
    if n < 4:
        brev *= 0.5                      # curto demais não diz nada
    curiosidade = 1.0 if any(m in t for m in _CURIOSIDADE) else 0.0
    pergunta = 1.0 if '?' in texto else 0.0
    numero = 1.0 if re.search(r'\d', texto) else 0.0   # número concreto prende o olho
    score = 0.45 * brev + 0.30 * curiosidade + 0.15 * pergunta + 0.10 * numero
    return round(min(1.0, max(0.0, score)), 4)


def melhor_gancho(titulo, conceito):
    """-> o gancho de maior pontuação (dict com 'formula','texto','score')."""
    cand = gerar_ganchos(titulo, conceito)
    for g in cand:
        g['score'] = pontuar_gancho(g['texto'])
    return max(cand, key=lambda g: g['score'])


def _conceito_de(cfg):
    """Conceito-chave do roteiro: título da 1ª cena 'conceito', senão a 1ª cena."""
    cenas = cfg.get('cenas', [])
    for c in cenas:
        if c.get('tipo') == 'conceito' and c.get('titulo'):
            return c['titulo']
    return cenas[0].get('titulo', cfg.get('titulo', '')) if cenas else cfg.get('titulo', '')


def do_roteiro(cfg):
    """-> {titulo, conceito, ganchos, melhor} a partir de um roteiro carregado."""
    titulo = cfg.get('titulo', '')
    conceito = _conceito_de(cfg)
    ganchos = gerar_ganchos(titulo, conceito)
    for g in ganchos:
        g['score'] = pontuar_gancho(g['texto'])
    melhor = max(ganchos, key=lambda g: g['score'])
    return {'titulo': titulo, 'conceito': conceito, 'ganchos': ganchos, 'melhor': melhor}


def main():
    if len(sys.argv) < 2:
        sys.exit('uso: python pesquisador.py <roteiro.json>')
    cfg = json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
    r = do_roteiro(cfg)
    print(f"=== Pesquisador — ganchos de '{r['titulo']}' (conceito: {r['conceito']}) ===")
    for g in sorted(r['ganchos'], key=lambda x: -x['score']):
        marca = '★' if g is r['melhor'] else ' '
        print(f"  {marca} [{g['score']:.2f}] ({g['formula']}) {g['texto']}")
    print(f"\nMELHOR: {r['melhor']['texto']}")


if __name__ == '__main__':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    main()
