"""Gate da lane Conversor Livro->Skill (Akita pilar 2/5).

Pluga no comando unico `python testar.py` (unittest discover). VERDE = exit code,
nao "a IA achou que esta certo". O contrato vive em valida_skill_lane.py (rede de
seguranca) e em LANE-CONVERSOR-LIVRO-SKILL.md (constituicao).

As skills moram em ~/.claude/skills (fora do repo): em CI o teste de skill e PULADO;
local (onde o agente produz a skill) ele roda o contrato inteiro.
"""

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import valida_skill_lane as v  # noqa: E402


class TestContratoDaLane(unittest.TestCase):
    def test_skills_cumprem_o_contrato_duro(self):
        """Toda skill do acervo cumpre o contrato duro."""
        if not v.SKILLS_DIR.is_dir():
            self.skipTest("~/.claude/skills ausente (CI); roda local no agente")
        alvos = sorted(set(v.livros_do_catalogo()) | v.SKILLS_FORA_DO_CATALOGO)
        reprovados = {s: p for s in alvos if (p := v.checa_skill(s))}
        self.assertEqual(reprovados, {}, f"skills fora do contrato: {reprovados}")

    def test_constituicao_da_lane_existe(self):
        """A constituicao (contrato + prompt 4-blocos) existe e cobre os 4 blocos."""
        doc = ROOT / "LANE-CONVERSOR-LIVRO-SKILL.md"
        self.assertTrue(doc.is_file(), "LANE-CONVERSOR-LIVRO-SKILL.md ausente")
        txt = doc.read_text(encoding="utf-8")
        for bloco in ("Objetivo", "Método", "Restrições", "Validação"):
            self.assertIn(bloco, txt, f"prompt 4-blocos sem '{bloco}'")


if __name__ == "__main__":
    unittest.main()
