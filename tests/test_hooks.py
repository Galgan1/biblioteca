# -*- coding: utf-8 -*-
"""TDD dos hooks de enforcement (Akita pilar 2+7): testa a LÓGICA do guarda.

Alimenta o stdin JSON que o Claude Code mandaria e confere a decisão + exit code.
Roda no gate `python testar.py`. Verde = exit 0.
"""
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GIT = ROOT / "hooks" / "git_guard.py"
FAN = ROOT / "hooks" / "fantasma_guard.py"


def _run(script, payload):
    return subprocess.run([sys.executable, str(script)],
                          input=json.dumps(payload), capture_output=True, text=True)


class TestGitGuard(unittest.TestCase):
    def test_commit_bloqueia(self):
        p = _run(GIT, {"tool_input": {"command": "git commit -m x"}})
        self.assertEqual(p.returncode, 0)
        self.assertIn("deny", p.stdout)

    def test_push_bloqueia(self):
        self.assertIn("deny", _run(GIT, {"tool_input": {"command": "git push origin main"}}).stdout)

    def test_pr_create_bloqueia(self):
        self.assertIn("deny", _run(GIT, {"tool_input": {"command": "gh pr create -f"}}).stdout)

    def test_gitguy_bypassa(self):
        self.assertNotIn("deny", _run(GIT, {"tool_input": {"command": "GITGUY=1 git commit -m x"}}).stdout)

    def test_status_libera(self):
        self.assertNotIn("deny", _run(GIT, {"tool_input": {"command": "git status"}}).stdout)

    def test_comando_inocente_libera(self):
        self.assertNotIn("deny", _run(GIT, {"tool_input": {"command": "ls -la"}}).stdout)

    def test_clean_bloqueia(self):  # o incidente que apagou _akita_pesquisa
        self.assertIn("deny", _run(GIT, {"tool_input": {"command": "git clean -fdx"}}).stdout)

    def test_reset_hard_bloqueia(self):
        self.assertIn("deny", _run(GIT, {"tool_input": {"command": "git reset --hard HEAD~1"}}).stdout)

    def test_gitguy_bypassa_clean(self):
        self.assertNotIn("deny", _run(GIT, {"tool_input": {"command": "GITGUY=1 git clean -fdx"}}).stdout)

    def test_trocar_branch_libera(self):  # checkout <branch> não é destrutivo de untracked
        self.assertNotIn("deny", _run(GIT, {"tool_input": {"command": "git checkout main"}}).stdout)

    def test_stdin_invalido_failopen(self):
        p = subprocess.run([sys.executable, str(GIT)], input="nao eh json",
                           capture_output=True, text=True)
        self.assertEqual(p.returncode, 0)
        self.assertNotIn("deny", p.stdout)


class TestFantasmaGuard(unittest.TestCase):
    def test_nao_py_pula(self):
        p = _run(FAN, {"tool_input": {"file_path": "README.md"}})
        self.assertEqual(p.returncode, 0)

    def test_py_repo_limpo_passa(self):
        # repo atual está sem fantasma (audita exit 0) → guard exit 0
        p = _run(FAN, {"tool_input": {"file_path": "vp100.py"}})
        self.assertEqual(p.returncode, 0)

    def test_stdin_invalido_failopen(self):
        p = subprocess.run([sys.executable, str(FAN)], input="x",
                           capture_output=True, text=True)
        self.assertEqual(p.returncode, 0)


if __name__ == "__main__":
    unittest.main()
