# -*- coding: utf-8 -*-
"""Checagem de densidade de texto por slide — princípio Krug (~35 palavras/slide).

AVISO DE CURADORIA: estas funções NÃO truncam nem alteram o conteúdo.
O auto-fit do gerador garante que o texto caiba visualmente; este módulo
é sobre LEGIBILIDADE — textos acima do limite ficam densos demais para
leitura confortável em 30 s.

Uso típico (no curador ou nos testes):
    from videos.text_budget import excede, contar_palavras
    if excede(cena_texto):
        print("AVISO: cena densa — revisar roteiro")
"""
import re


def contar_palavras(texto: str) -> int:
    """Conta palavras em *texto* (separa por espaço/pontuação; stdlib, sem deps)."""
    return len(re.findall(r'\S+', texto))


def excede(texto: str, limite: int = 35) -> bool:
    """Retorna True se *texto* ultrapassar *limite* palavras.

    O limite padrão de 35 é baseado na heurística Krug de carga cognitiva
    por slide/cena. Apenas sinaliza — não trunca.
    """
    return contar_palavras(texto) > limite
