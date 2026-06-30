# -*- coding: utf-8 -*-
"""TDD do core v3 do bot Minuto Real: roteamento PURO + robustez de rede (429/fallback).

Sem rede; sem publicar de verdade. Roda no `python testar.py`.
"""
import os
import unittest
from unittest import mock

import bot_minutoreal as bot

_UID = "999"


def _msg(text, uid=_UID):
    return {"message": {"chat": {"id": uid}, "from": {"id": uid}, "text": text}}


def _cb(data, uid=_UID):
    return {"callback_query": {"id": "1", "data": data, "from": {"id": uid},
                               "message": {"message_id": 5, "chat": {"id": "777"}}}}


class TestHtml(unittest.TestCase):
    def test_negrito_codigo_e_escape(self):
        h = bot._html("*ola* `cd` <x> & y")
        self.assertIn("<b>ola</b>", h)
        self.assertIn("<code>cd</code>", h)
        self.assertIn("&lt;x&gt;", h)


class TestPaginar(unittest.TestCase):
    def test_meio_tem_setas(self):
        sl, nav = bot._paginar(list(range(30)), 1, 12, "livros")
        self.assertEqual(sl, list(range(12, 24)))
        cbs = [b["callback_data"] for b in nav[0]]
        self.assertIn("livros:0", cbs)
        self.assertIn("livros:2", cbs)

    def test_curta_sem_nav(self):
        self.assertEqual(bot._paginar([1, 2], 0, 12, "x")[1], [])


class TestPlanejar(unittest.TestCase):
    def setUp(self):
        os.environ["TELEGRAM_CHAT_ID"] = _UID

    def tearDown(self):
        os.environ.pop("TELEGRAM_CHAT_ID", None)

    def _m(self, plano):
        return [m for m, _ in plano]

    def _flat(self, params):
        return [b["callback_data"] for row in params["reply_markup"]["inline_keyboard"] for b in row]

    def test_estranho_msg_ignorado(self):              # auth por from.id
        self.assertEqual(bot.planejar(_msg("/start", uid="invasor")), [])

    def test_estranho_callback_negado(self):
        p = bot.planejar(_cb("menu", uid="invasor"))
        self.assertIn("não autorizado", p[0][1]["text"])

    def test_start_menu_html(self):
        p = bot.planejar(_msg("/start"))
        self.assertEqual(self._m(p), ["sendMessage"])
        self.assertEqual(p[0][1]["parse_mode"], "HTML")

    def test_toast_vem_primeiro(self):                 # ack antes do edit (feedback instantâneo)
        self.assertEqual(self._m(bot.planejar(_cb("menu"))), ["answerCallbackQuery", "editMessageText"])

    def test_tela_lenta_manda_typing(self):            # saude roda doctor → "digitando"
        with mock.patch.dict(bot.TELAS, {"saude": ("🩺 Saúde", "🩺", lambda: "OK", "🩺")}):
            m = self._m(bot.planejar(_cb("saude")))
        self.assertEqual(m, ["answerCallbackQuery", "sendChatAction", "editMessageText"])

    def test_tela_rapida_sem_typing(self):
        with mock.patch.dict(bot.TELAS, {"vendas": ("💰", "💰", lambda: "Z", "💰")}):
            m = self._m(bot.planejar(_cb("vendas")))
        self.assertEqual(m, ["answerCallbackQuery", "editMessageText"])

    def test_livros_paginado(self):
        with mock.patch.object(bot.h_livros, "lista", return_value=[f"L{i}" for i in range(30)]):
            flat = self._flat(bot.planejar(_cb("livros:1"))[-1][1])
        self.assertIn("livros:0", flat)
        self.assertIn("livros:2", flat)

    def test_publicar_picker(self):
        with mock.patch.object(bot.h_publicar, "slugs", return_value=["meditacoes", "1984"]):
            flat = self._flat(bot.planejar(_cb("publicar"))[-1][1])
        self.assertIn("pub:meditacoes", flat)

    def test_confirm_tem_confirmar_e_ensaio(self):
        with mock.patch.object(bot.h_publicar, "confirmar", return_value="?"):
            flat = self._flat(bot.planejar(_cb("pub:1984"))[-1][1])
        self.assertIn("pubok:1984", flat)
        self.assertIn("pubdry:1984", flat)     # ensaio (--dry) exposto

    def test_pubok_real(self):
        with mock.patch.object(bot.h_publicar, "executar", return_value="ok") as ex:
            bot.planejar(_cb("pubok:1984"))
        ex.assert_called_once_with("1984")     # dry NÃO passado → publish real

    def test_pubdry_ensaio(self):
        with mock.patch.object(bot.h_publicar, "executar", return_value="ok") as ex:
            bot.planejar(_cb("pubdry:1984"))
        ex.assert_called_once_with("1984", dry=True)


class TestRedeRobusta(unittest.TestCase):
    def setUp(self):
        os.environ["TELEGRAM_BOT_TOKEN"] = "x"

    def tearDown(self):
        os.environ.pop("TELEGRAM_BOT_TOKEN", None)

    def test_429_respeita_retry_e_repete(self):
        seq = [{"ok": False, "error_code": 429, "parameters": {"retry_after": 0}}, {"ok": True}]
        with mock.patch.object(bot, "_post", side_effect=seq) as post:
            self.assertTrue(bot._chamar("sendMessage", {"text": "x"})["ok"])
        self.assertEqual(post.call_count, 2)

    def test_html_quebrado_reenvia_sem_tags(self):
        seq = [{"ok": False, "description": "can't parse entities"}, {"ok": True}]
        with mock.patch.object(bot, "_post", side_effect=seq) as post:
            bot._chamar("sendMessage", {"text": "<b>x</b>", "parse_mode": "HTML"})
        txt = post.call_args_list[1].args[1]["text"]
        self.assertNotIn("<", txt)             # tags removidas no fallback

    def test_not_modified_e_sucesso(self):
        with mock.patch.object(bot, "_post", return_value={"ok": False, "description": "message is not modified"}):
            self.assertTrue(bot._chamar("editMessageText", {"text": "x"})["ok"])


if __name__ == "__main__":
    unittest.main()
