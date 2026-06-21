# -*- coding: utf-8 -*-
"""Gate de MARCA no ponto único (testar.py): nenhuma cor cromática NOVA fora da paleta
canônica (verde h152 / ouro h83 / alerta h30 — lida de marca.py). A dívida conhecida
fica no _BASELINE de valida_marca.py e é queimada aos poucos.

POR QUÊ (Akita): excelência de design vira EXIT CODE, sourced do mestre (marca.py) —
o defeito (cor fora da marca) não propaga porque o portão recusa, não só avisa."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import valida_marca  # noqa: E402


class TestPaletaMarca(unittest.TestCase):
    def test_sem_cor_nova_fora_da_marca(self):
        _permitidos, achados = valida_marca.violacoes()
        novas = valida_marca.novas(achados)
        msg = "; ".join(f"{a}:{i} hue{h}" for a, i, h, _c in novas)
        self.assertEqual(novas, [], f"cor(es) NOVA(s) fora da marca (use tokens de marca.py): {msg}")

    def test_hues_canonicos_vem_de_marca(self):
        # a régua sai do MESTRE (marca.py), não hardcoded no gate.
        self.assertEqual(valida_marca.hues_da_marca(), {30, 83, 152})


if __name__ == '__main__':
    unittest.main()
