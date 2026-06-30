# -*- coding: utf-8 -*-
"""publicar_tudo — orquestrador 1-clique: coordena 4 superfícies, idempotente, erro vira
alerta sem derrubar as outras, gate de copy barra defeito. Hermético (publishers/render/
Telegram mocados). Akita: verde = exit code."""
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import publicar_tudo as pt  # noqa: E402


class TestPublicarTudo(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.mkdtemp()
        self._alertas = []
        # Slate limpo de teto: o entrypoint faz setdefault — tirar o env torna os testes
        # de catraca determinísticos e evita vazar WEEKLY_BUDGET_USD p/ outros arquivos.
        self._env_budget = os.environ.pop("WEEKLY_BUDGET_USD", None)
        self._p = [
            mock.patch.object(pt, "_garante_video", return_value="/fake/v.mp4"),
            mock.patch.object(pt, "_estado_path", side_effect=lambda s: Path(self._tmp) / f"{s}.json"),
            mock.patch.object(pt, "_alerta", side_effect=lambda m: self._alertas.append(m)),
            mock.patch.object(pt, "publicavel", return_value=(True, "")),  # estes testes focam orquestração, não preflight
        ]
        for p in self._p:
            p.start()

    def tearDown(self):
        for p in self._p:
            p.stop()
        if self._env_budget is None:
            os.environ.pop("WEEKLY_BUDGET_USD", None)
        else:
            os.environ["WEEKLY_BUDGET_USD"] = self._env_budget

    def _surfaces(self, falha=None):
        chamadas = []

        def mk(nome):
            def fn(slug, ctx):
                chamadas.append(nome)
                if nome == falha:
                    raise RuntimeError("boom")
                return f"{nome}-id"
            return fn
        sup = [(n, mk(n)) for n in ("youtube_longo", "youtube_shorts", "instagram", "facebook")]
        return sup, chamadas

    def test_roda_todas_as_superficies(self):
        sup, chamadas = self._surfaces()
        with mock.patch.object(pt, "SUPERFICIES", sup):
            res = pt.publicar_tudo("slugx")
        self.assertEqual(set(chamadas), {"youtube_longo", "youtube_shorts", "instagram", "facebook"})
        self.assertTrue(all("ok" in v for v in res.values()))

    def test_idempotente_segunda_vez_pula(self):
        sup, _ = self._surfaces()
        with mock.patch.object(pt, "SUPERFICIES", sup):
            pt.publicar_tudo("slugy")
        sup2, chamadas2 = self._surfaces()
        with mock.patch.object(pt, "SUPERFICIES", sup2):
            res = pt.publicar_tudo("slugy")
        self.assertEqual(chamadas2, [])                       # nada re-publicado
        self.assertTrue(all("pulado" in v for v in res.values()))

    def test_erro_alerta_e_nao_derruba_as_outras(self):
        sup, _ = self._surfaces(falha="instagram")
        with mock.patch.object(pt, "SUPERFICIES", sup):
            res = pt.publicar_tudo("slugz")
        self.assertTrue(res["instagram"].startswith("ERRO"))
        self.assertIn("ok", res["facebook"])                  # seguiu após o erro
        self.assertTrue(any("instagram" in a for a in self._alertas))  # disparou alerta

    def test_dry_run_nao_publica(self):
        sup, chamadas = self._surfaces()
        with mock.patch.object(pt, "SUPERFICIES", sup):
            res = pt.publicar_tudo("slugd", dry=True)
        self.assertEqual(chamadas, [])
        self.assertTrue(all(v == "dry-run" for v in res.values()))

    def test_filtro_so(self):
        sup, chamadas = self._surfaces()
        with mock.patch.object(pt, "SUPERFICIES", sup):
            pt.publicar_tudo("slugf", so={"facebook"})
        self.assertEqual(chamadas, ["facebook"])

    def test_gate_barra_pt_pt(self):
        with self.assertRaises(ValueError):
            pt._gate("Vê no ecrã do telemóvel.", "youtube")

    def test_gate_passa_copy_limpa(self):
        pt._gate("Resumo em pt-BR. Salve e marque alguém.", "youtube")  # não levanta

    def test_notifica_placar_no_sucesso(self):
        # J3 nº2: sucesso TOTAL também avisa. Antes: silêncio = sucesso, e o "te aviso ao
        # concluir" do bot Telegram nunca se cumpria (só FALHA alertava).
        sup, _ = self._surfaces()
        with mock.patch.object(pt, "SUPERFICIES", sup):
            pt.publicar_tudo("slugn")
        self.assertTrue(self._alertas, "sucesso total tem que disparar alerta de fim")
        placar = self._alertas[-1]
        for rotulo in ("YouTube", "Shorts", "Instagram", "Facebook"):
            self.assertIn(rotulo, placar)
        self.assertIn("✅", placar)
        self.assertNotIn("❌", placar)

    def test_placar_marca_rede_que_falhou(self):
        sup, _ = self._surfaces(falha="instagram")
        with mock.patch.object(pt, "SUPERFICIES", sup):
            pt.publicar_tudo("slugpf")
        placar = self._alertas[-1]
        self.assertIn("✅", placar)                # as que saíram
        self.assertIn("❌", placar)                # a que falhou

    def test_placar_ensaio_se_explica(self):
        # auto-explicativo: diz que foi ensaio, qual livro, sem jargão, com próximo passo.
        sup, _ = self._surfaces()
        with mock.patch.object(pt, "SUPERFICIES", sup):
            pt.publicar_tudo("slugd", dry=True)
        placar = self._alertas[-1]
        self.assertIn("ENSAIO", placar)
        self.assertIn("slugd", placar)                 # diz QUAL livro
        self.assertNotIn("dry-run", placar)            # jargão fora
        self.assertIn("publicar de verdade", placar)   # próximo passo

    def test_placar_sucesso_sem_jargao(self):
        sup, _ = self._surfaces()
        with mock.patch.object(pt, "SUPERFICIES", sup):
            pt.publicar_tudo("slugps")
        placar = self._alertas[-1]
        self.assertIn("Publicado", placar)
        self.assertNotIn("[publicar_tudo]", placar)    # sem nome de módulo cru
        self.assertNotIn("dry-run", placar)

    def test_teto_ligado_no_entrypoint_premium(self):
        # J3 nº3: caminho premium (.mp4 já existe -> gerar_video.main NÃO roda). O teto
        # tem que valer mesmo assim, senão uma chamada paga (gv.tts dos Shorts) gasta sem
        # catraca. Imitamos gv.tts com check_budget; SEM o setdefault no entrypoint isto
        # seria no-op (env ausente) e a superfície "publicaria".
        import cost_tracker as ct

        def paga(slug, ctx):
            ct.check_budget("google_tts_1k")       # o que gv.tts faz via @budget_guard
            return "gastou"

        with mock.patch.object(ct, "weekly_cost", return_value=9999.0), \
             mock.patch.object(pt, "SUPERFICIES", [("youtube_shorts", paga)]):
            res = pt.publicar_tudo("slugp")
        self.assertTrue(res["youtube_shorts"].startswith("ERRO"))
        self.assertIn("teto", res["youtube_shorts"].lower())

    def test_teto_respeita_override_existente(self):
        # setdefault não pode sobrescrever um teto já configurado (operador/CI).
        sup, _ = self._surfaces()
        with mock.patch.dict(os.environ, {"WEEKLY_BUDGET_USD": "7"}, clear=False), \
             mock.patch.object(pt, "SUPERFICIES", sup):
            pt.publicar_tudo("slugov")
            self.assertEqual(os.environ["WEEKLY_BUDGET_USD"], "7")


class TestRoteiroSubdir(unittest.TestCase):
    """Regressão (bug jun/26): publish da VPS só passava no YouTube-longo porque
    IG/FB/Shorts leem roteiros/<slug>.json e o deploy punha o roteiro flat. O
    orquestrador espelha p/ a subpasta (self-healing)."""

    def test_espelha_flat_para_subdir(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / 'meu-livro.json').write_text('{"titulo":"x"}', encoding='utf-8')
            with mock.patch.object(pt, 'ROOT', root):
                pt._garante_roteiro_subdir('meu-livro')
            sub = root / 'roteiros' / 'meu-livro.json'
            self.assertTrue(sub.exists(), 'roteiro deveria ter sido espelhado p/ roteiros/')
            self.assertEqual(sub.read_text(encoding='utf-8'), '{"titulo":"x"}')

    def test_nao_quebra_sem_roteiro_flat(self):
        with tempfile.TemporaryDirectory() as d:
            with mock.patch.object(pt, 'ROOT', Path(d)):
                pt._garante_roteiro_subdir('inexistente')  # não levanta


class TestPreflightRoteiro(unittest.TestCase):
    """Regressão (bug 22/jun): 81/103 livros do acervo não têm roteiro, e o --dry
    curto-circuitava ANTES de ler dados -> devolvia exit 0 (falso-verde) p/ todos. O
    roteiro <slug>.json (titulo+cenas) é a ÚNICA fonte do render — não o _data.py/skill.
    Agora publicavel() é o gate canônico (mesma regra de servir_publicar._livros)."""

    def setUp(self):
        self._d = tempfile.mkdtemp()
        self._root = mock.patch.object(pt, 'ROOT', Path(self._d))
        self._root.start()
        # HERMÉTICO: mockar _alerta — senão o alerta de FIM (placar) ia pro Telegram REAL a
        # cada rodada do gate (bug: test_main_dry_com_roteiro vazava "ok-livro — concluído").
        self._alertas = []
        self._alerta_p = mock.patch.object(pt, '_alerta', side_effect=lambda m: self._alertas.append(m))
        self._alerta_p.start()
        # main()/publicar_tudo fazem setdefault('WEEKLY_BUDGET_USD') no entrypoint — isolar
        # p/ não vazar o teto p/ outros módulos do gate (test_veo aborta via @budget_guard).
        self._env_budget = os.environ.pop("WEEKLY_BUDGET_USD", None)

    def tearDown(self):
        self._alerta_p.stop()
        self._root.stop()
        if self._env_budget is None:
            os.environ.pop("WEEKLY_BUDGET_USD", None)
        else:
            os.environ["WEEKLY_BUDGET_USD"] = self._env_budget

    def _escreve(self, slug, cfg):
        (Path(self._d) / f'{slug}.json').write_text(json.dumps(cfg), encoding='utf-8')

    def test_publicavel_true_com_titulo_e_cenas(self):
        self._escreve('bom', {'titulo': 'X', 'cenas': [{'narracao': 'oi'}]})
        ok, motivo = pt.publicavel('bom')
        self.assertTrue(ok)
        self.assertEqual(motivo, '')

    def test_publicavel_false_sem_roteiro(self):
        ok, motivo = pt.publicavel('fantasma')
        self.assertFalse(ok)
        self.assertIn('sem roteiro', motivo)

    def test_publicavel_false_roteiro_sem_cenas(self):
        self._escreve('vazio', {'titulo': 'X'})           # sem 'cenas'
        ok, motivo = pt.publicavel('vazio')
        self.assertFalse(ok)
        self.assertIn('sem titulo/cenas', motivo)

    def test_publicavel_acha_no_subdir(self):
        sub = Path(self._d) / 'roteiros'
        sub.mkdir()
        (sub / 'subli.json').write_text(json.dumps({'titulo': 'Y', 'cenas': [1]}), encoding='utf-8')
        self.assertTrue(pt.publicavel('subli')[0])

    def test_dry_sem_roteiro_reprova(self):
        """O coração do bug: --dry NÃO pode dar verde p/ livro sem roteiro."""
        res = pt.publicar_tudo('fantasma', dry=True)
        self.assertIn('_sem_roteiro', res)
        self.assertNotIn('youtube_longo', res)            # nada de falso 'dry-run'

    def test_main_dry_sem_roteiro_exit_1(self):
        self.assertEqual(pt.main(['fantasma', '--dry']), 1)   # exit != 0 = preflight reprovou

    def test_main_dry_com_roteiro_exit_0(self):
        self._escreve('ok-livro', {'titulo': 'Z', 'cenas': [1]})
        self.assertEqual(pt.main(['ok-livro', '--dry']), 0)

    def test_real_sem_roteiro_alerta(self):
        alertas = []
        with mock.patch.object(pt, '_alerta', side_effect=lambda m: alertas.append(m)):
            res = pt.publicar_tudo('fantasma', dry=False)   # NÃO toca API: aborta no preflight
        self.assertIn('_sem_roteiro', res)
        self.assertTrue(any('fantasma' in a for a in alertas))   # operador aprende pelo Telegram


if __name__ == "__main__":
    unittest.main()
