# -*- coding: utf-8 -*-
"""Testa que gerar_premium.BASE_CSS e gerar_carrossel.STORY_CSS NÃO contêm
literais de cor de marca (oklch com hue 152 ou 83) fora de blocos :root{}.

Cores de marca devem vir via var(--...) — os próprios :root{} (de tokens.py
ou vars auxiliares declaradas ali) são a exceção permitida.

Falha ANTES do fix (cores hardcoded no corpo); verde DEPOIS do fix."""
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]   # .../biblioteca
sys.path.insert(0, str(ROOT))


def _strip_root_blocks(css: str) -> str:
    """Remove todos os blocos :root{...} do CSS (podem aninhar vars de marca).
    Usa uma varredura simples de balanceamento de chaves."""
    result = []
    i = 0
    while i < len(css):
        # detecta início de :root{
        m = re.search(r':root\s*\{', css[i:])
        if not m:
            result.append(css[i:])
            break
        # texto antes do :root
        result.append(css[i: i + m.start()])
        # avança para a chave de abertura
        start = i + m.end() - 1   # posição da '{'
        depth = 1
        j = start + 1
        while j < len(css) and depth:
            if css[j] == '{':
                depth += 1
            elif css[j] == '}':
                depth -= 1
            j += 1
        # pula o bloco inteiro (incluindo :root{...})
        i = j
    return ''.join(result)


# padrão: oklch( ... 152 ...) ou oklch( ... 83 ...) como hue final
_LITERAL_COLOR = re.compile(r'oklch\([^)]*\b(152|83)\b[^)]*\)')


class TestMarcaConsistencia(unittest.TestCase):

    def _check_css(self, name: str, css: str):
        stripped = _strip_root_blocks(css)
        matches = _LITERAL_COLOR.findall(stripped)
        self.assertEqual(
            matches, [],
            f"{name}: encontradas {len(matches)} cor(es) literal(is) de marca "
            f"fora do :root (hue 152/83). Use var(--...) no corpo do CSS.\n"
            f"Ocorrências: {_LITERAL_COLOR.findall(stripped)}"
        )

    def test_premium_sem_literais_de_marca(self):
        import gerar_premium as gp
        self._check_css('gerar_premium.BASE_CSS', gp.BASE_CSS)

    def test_carrossel_story_sem_literais_de_marca(self):
        import gerar_carrossel as gc
        self._check_css('gerar_carrossel.STORY_CSS', gc.STORY_CSS)


if __name__ == '__main__':
    unittest.main()
