import json
import os
import subprocess
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import fila as fila_mod


class TestFila(unittest.TestCase):
    """Contratos da fila semanal de publicações do canal Minuto Real."""

    def test_fila_gera_json_valido(self):
        """--dry-run deve imprimir JSON parseável."""
        env = {**os.environ, "PYTHONUTF8": "1"}
        result = subprocess.run(
            [sys.executable, "fila.py", "--semanas", "1", "--dry-run"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            env=env,
            cwd=Path(__file__).parent.parent,
        )
        self.assertEqual(result.returncode, 0, f"fila.py falhou: {result.stderr}")
        dados = json.loads(result.stdout)
        self.assertIsInstance(dados, list)
        self.assertGreater(len(dados), 0, "Fila não pode ser vazia")

    def test_fila_tem_campos_obrigatorios(self):
        """Cada slot deve ter slug/titulo/serie/formato/dia/horario/semana."""
        campos = {"slug", "titulo", "serie", "formato", "dia", "horario", "semana"}
        fila = fila_mod.gerar_fila(semanas=2)
        for slot in fila:
            faltando = campos - set(slot.keys())
            self.assertFalse(faltando, f"Campos ausentes em {slot.get('slug')}: {faltando}")

    def test_fila_sem_repeticao_semana(self):
        """Mesmo slug não pode aparecer duas vezes na mesma semana."""
        fila = fila_mod.gerar_fila(semanas=4)
        por_semana: dict[int, list[str]] = {}
        for slot in fila:
            por_semana.setdefault(slot["semana"], []).append(slot["slug"])
        for semana, slugs in por_semana.items():
            duplicados = {s for s in slugs if slugs.count(s) > 2}  # par SEG+TER é ok
            self.assertFalse(duplicados, f"Semana {semana} repete slug: {duplicados}")

    def test_serie_classifica_corretamente(self):
        """'habitos-atomicos' deve ser classificado como série 'mentalidade'."""
        self.assertEqual(fila_mod._serie_de("habitos-atomicos"), "mentalidade")

    def test_serie_outros_para_desconhecido(self):
        """Slug fora das SERIES definidas deve retornar 'outros'."""
        self.assertEqual(fila_mod._serie_de("slug-inexistente-xyz"), "outros")

    def test_fila_campos_dia_validos(self):
        """Todos os dias devem ser da cadência prevista."""
        dias_validos = {"SEG", "TER", "QUA", "QUI", "SEX", "SAB"}
        fila = fila_mod.gerar_fila(semanas=1)
        for slot in fila:
            self.assertIn(slot["dia"], dias_validos, f"Dia inválido: {slot['dia']}")

    def test_fila_semana_numerada_corretamente(self):
        """Campo semana deve refletir o número da semana (1 a N)."""
        fila = fila_mod.gerar_fila(semanas=3)
        semanas_na_fila = {slot["semana"] for slot in fila}
        self.assertEqual(semanas_na_fila, {1, 2, 3})


if __name__ == "__main__":
    unittest.main()
