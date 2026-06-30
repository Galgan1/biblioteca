# -*- coding: utf-8 -*-
"""Testes de contrato do agendador.py (unittest.TestCase — gate python testar.py)."""
import io
import sys
import unittest
from datetime import date
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import agendador

FIXTURE = Path(__file__).parent / "fixtures" / "fila_fixture.json"


def _fila():
    import json
    return json.loads(FIXTURE.read_text(encoding="utf-8"))


class TestDryRun(unittest.TestCase):
    """--dry-run imprime slots sem chamar schtasks."""

    def test_dry_run_imprime_7_slots(self):
        """Saída do dry-run deve ter pelo menos 7 linhas de dados (1 por slot)."""
        fila = _fila()
        # 2026-06-29 é segunda-feira; fixture tem slots de 2 semanas (SEG a SAB x2)
        hoje = date(2026, 6, 29)
        buf = io.StringIO()
        with mock.patch("sys.stdout", buf):
            agendador.cmd_dry_run(fila, hoje)
        linhas_dados = [
            l for l in buf.getvalue().splitlines()
            if l and not l.startswith("DRY") and not l.startswith("SLUG") and not l.startswith("-")
        ]
        self.assertGreaterEqual(len(linhas_dados), 7,
                                f"Esperado >=7 linhas, obtido {len(linhas_dados)}: {linhas_dados}")

    def test_dry_run_sem_criar_tarefas(self):
        """--dry-run nunca chama subprocess.run com 'schtasks /Create'."""
        fila = _fila()
        hoje = date(2026, 6, 29)
        with mock.patch("subprocess.run") as mock_run:
            with mock.patch("sys.stdout", io.StringIO()):
                agendador.cmd_dry_run(fila, hoje)
            for call in mock_run.call_args_list:
                args = call[0][0] if call[0] else call[1].get("args", [])
                if isinstance(args, list):
                    self.assertFalse(
                        "schtasks" in args and "/Create" in args,
                        f"dry-run nao deve criar schtask, chamou: {args}",
                    )


class TestCmdSchtasks(unittest.TestCase):
    """A funcao _cmd_criar monta o comando correto."""

    def test_cmd_schtasks_bem_formado(self):
        """/TN, /TR e /ST devem estar presentes no comando montado."""
        nome = "MinutoReal-sapiens-20260701"
        cmd_tr = '"python" "publicar_livro.py" sapiens --plataformas ig,yt'
        horario = "18:30"
        data = date(2026, 7, 1)
        cmd = agendador._cmd_criar(nome, cmd_tr, horario, data)
        self.assertIn("/TN", cmd)
        self.assertIn("/TR", cmd)
        self.assertIn("/ST", cmd)
        self.assertIn(nome, cmd)
        self.assertIn(horario, cmd)

    def test_nome_tarefa_formato(self):
        """Nome da tarefa segue padrao MinutoReal-{slug}-{YYYYMMDD}."""
        nome = agendador._nome_tarefa("habitos-atomicos", date(2026, 7, 1))
        self.assertEqual(nome, "MinutoReal-habitos-atomicos-20260701")


class TestErroSemFilaJson(unittest.TestCase):
    """Erro claro quando fila.json nao existe."""

    def test_erro_sem_fila_json(self):
        """_ler_fila() deve chamar sys.exit(1) com mensagem clara."""
        caminho_inexistente = Path("/nao/existe/fila.json")
        with mock.patch.object(agendador, "FILA_JSON", caminho_inexistente):
            buf = io.StringIO()
            with mock.patch("sys.stderr", buf):
                with self.assertRaises(SystemExit) as ctx:
                    agendador._ler_fila()
        self.assertEqual(ctx.exception.code, 1)
        self.assertIn("fila.py", buf.getvalue())


if __name__ == "__main__":
    unittest.main()
