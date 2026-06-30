# -*- coding: utf-8 -*-
"""bot_minutoreal.py — painel de controle do Minuto Real no Telegram (long-polling, stdlib).

Interface PRO: HTML formatado (com fallback que tira tags se o parse falhar), header/
breadcrumb por tela, teclado grade 2-colunas, navegação universal (« Menu / 🔄), feedback
instantâneo (toast PRIMEIRO) + "digitando…" nas telas lentas, paginação real (livros/publicar),
confirmação com idempotência visível + ensaio (--dry) p/ publicar, e setMyCommands.
Robustez Bot API: trata 409 (poller duplo), 429 (rate-limit), edit-stale, backoff de rede.
AUTH por `from.id` (a pessoa, não o chat → seguro até em grupo). Soberano: urllib/json.

Akita: `planejar(update)->[(method,params)]` é PURO (toda a UX) → testável sem rede;
`executar` dispara as chamadas (com fallback); `loop` faz getUpdates→planejar→executar.

Uso:  python bot_minutoreal.py            # loop (PM2-ready)
      python bot_minutoreal.py --once     # 1 ciclo (teste/cron)
"""
import html
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from notificar import _cred
from _bot_handlers import h_livros, h_publicacoes, h_vendas, h_saude, h_status, h_publicar

_API = "https://api.telegram.org/bot{}/{}"
_TIMEOUT = 35
_MAXLEN = 4000
_STRIP = re.compile(r"<[^>]+>")
_LENTAS = {"saude", "status", "publicacoes"}   # rodam I/O → mandar "digitando" antes

# cmd -> (rótulo do botão, emoji, render read-only, toast)
TELAS = {
    "livros":      ("📚 Livros",      "📚", None,                 "📚"),
    "publicacoes": ("📊 Publicações", "📊", h_publicacoes.render, "📊 carregando…"),
    "vendas":      ("💰 Vendas",      "💰", h_vendas.render,      "💰"),
    "saude":       ("🩺 Saúde",       "🩺", h_saude.render,       "🩺 verificando…"),
    "status":      ("⚙️ Status",      "⚙️", h_status.render,      "⚙️"),
    "publicar":    ("🚀 Publicar",    "🚀", None,                 "🚀"),
}
_COMANDOS = [
    ("menu", "Abrir o painel de controle"), ("livros", "Acervo de livros"),
    ("publicacoes", "O que já foi publicado"), ("vendas", "Afiliados / vendas"),
    ("saude", "Saúde do pipeline"), ("status", "Status geral"),
    ("publicar", "Publicar um livro (com confirmação)"),
]


# ---------- formatação (HTML seguro) ----------
def _html(texto: str) -> str:
    t = html.escape(texto or "", quote=False)
    t = re.sub(r"\*(.+?)\*", r"<b>\1</b>", t)
    t = re.sub(r"`(.+?)`", r"<code>\1</code>", t)
    return t[:_MAXLEN]


def _tela(titulo: str, corpo_html: str) -> str:
    return f"🤖 <b>Minuto Real</b>  ·  <b>{html.escape(titulo)}</b>\n\n{corpo_html}"[:_MAXLEN]


def _b(texto, cb):
    return {"text": texto, "callback_data": cb}


def _kb_menu():
    return {"inline_keyboard": [
        [_b("📚 Livros", "livros"), _b("📊 Publicações", "publicacoes")],
        [_b("💰 Vendas", "vendas"), _b("🩺 Saúde", "saude")],
        [_b("⚙️ Status", "status"), _b("🚀 Publicar", "publicar")],
    ]}


def _kb_dados(cb_atual):
    return {"inline_keyboard": [[_b("🔄 Atualizar", cb_atual), _b("« Menu", "menu")]]}


def _kb_voltar():
    return {"inline_keyboard": [[_b("« Menu", "menu")]]}


def _paginar(itens, page, per, prefixo):
    total = max(1, (len(itens) + per - 1) // per)
    page = max(0, min(page, total - 1))
    sl = itens[page * per:(page + 1) * per]
    nav = []
    if page > 0:
        nav.append(_b("‹", f"{prefixo}:{page - 1}"))
    if total > 1:
        nav.append(_b(f"{page + 1}/{total}", "noop"))
    if page < total - 1:
        nav.append(_b("›", f"{prefixo}:{page + 1}"))
    return sl, ([nav] if nav else [])


# ---------- auth (por usuário, não por chat) ----------
def _quem(update):
    src = update.get("message") or update.get("callback_query") or {}
    return src.get("from", {}).get("id")


def autorizado(uid) -> bool:
    alvo = _cred("telegram_chat_id.txt", "TELEGRAM_CHAT_ID")
    return bool(alvo) and str(uid) == str(alvo)


# ---------- telas ----------
def _tela_menu():
    corpo = ("Bem-vindo ao painel do canal. Escolha uma opção 👇\n"
             "<i>Os comandos /livros, /publicar… também funcionam.</i>")
    return _tela("Painel", corpo), _kb_menu()


def _tela_livros(page):
    itens = h_livros.lista()
    sl, nav = _paginar(itens, page, 12, "livros")
    corpo = (f"<b>{len(itens)}</b> livros no acervo\n\n"
             + "\n".join("• " + html.escape(x) for x in sl)) if sl else "Acervo indisponível."
    return _tela("📚 Livros", corpo), {"inline_keyboard": nav + [[_b("« Menu", "menu")]]}


def _tela_publicar(page):
    slugs = h_publicar.slugs()
    sl, nav = _paginar(slugs, page, 8, "publicar")
    botoes = [[_b("📖 " + s, "pub:" + s)] for s in sl]
    corpo = "Escolha o livro para <b>publicar</b> (YouTube + Instagram + Facebook):" if sl \
        else "Nenhum livro disponível."
    return _tela("🚀 Publicar", corpo), {"inline_keyboard": botoes + nav + [[_b("« Menu", "menu")]]}


# ---------- roteamento PURO ----------
def planejar(update: dict):
    """update -> lista de (method, params). Toda a UX, sem rede. Testável."""
    uid = _quem(update)
    msg = update.get("message")
    cb = update.get("callback_query")

    if msg:
        if not autorizado(uid):
            return []
        cmd = (msg.get("text") or "").lstrip("/").split("@")[0].strip().lower()
        if cmd in TELAS and TELAS[cmd][2]:
            return [("sendMessage", _p(msg["chat"]["id"],
                    _tela(TELAS[cmd][0], _html(TELAS[cmd][2]())), _kb_dados(cmd)))]
        if cmd == "livros":
            t, kb = _tela_livros(0)
        elif cmd == "publicar":
            t, kb = _tela_publicar(0)
        else:
            t, kb = _tela_menu()
        return [("sendMessage", _p(msg["chat"]["id"], t, kb))]

    if not cb:
        return []
    chat = cb.get("message", {}).get("chat", {}).get("id")
    mid = cb.get("message", {}).get("message_id")
    cbid = cb.get("id")
    data = cb.get("data", "")
    if not autorizado(uid):
        return [("answerCallbackQuery", {"callback_query_id": cbid, "text": "🔒 não autorizado"})]

    base, _, arg = data.partition(":")

    def resp(texto, kb, toast=""):
        # ACK PRIMEIRO (toast instantâneo) → "digitando" se lento → edit.
        plano = [("answerCallbackQuery", {"callback_query_id": cbid, "text": toast})]
        if base in _LENTAS:
            plano.append(("sendChatAction", {"chat_id": chat, "action": "typing"}))
        plano.append(("editMessageText", _p(chat, texto, kb, mid)))
        return plano

    if data == "noop":
        return [("answerCallbackQuery", {"callback_query_id": cbid})]
    if data == "menu":
        t, kb = _tela_menu()
        return resp(t, kb)
    if base == "livros":
        t, kb = _tela_livros(int(arg) if arg.isdigit() else 0)
        return resp(t, kb, "📚")
    if base == "publicar":
        t, kb = _tela_publicar(int(arg) if arg.isdigit() else 0)
        return resp(t, kb, "🚀")
    if base == "pub":
        kb = {"inline_keyboard": [[_b("✅ Confirmar", f"pubok:{arg}"), _b("🧪 Ensaio", f"pubdry:{arg}")],
                                  [_b("« cancelar", "menu")]]}
        return resp(_tela("🚀 Confirmar", _html(h_publicar.confirmar(arg))), kb, "⚠️ confirmar")
    if base == "pubok":
        return resp(_tela("🚀 Publicação", _html(h_publicar.executar(arg))),
                    {"inline_keyboard": [[_b("📊 Publicações", "publicacoes"), _b("« Menu", "menu")]]},
                    "🚀 publicando")
    if base == "pubdry":
        return resp(_tela("🧪 Ensaio", _html(h_publicar.executar(arg, dry=True))), _kb_voltar(), "🧪 ensaio")
    if base in TELAS and TELAS[base][2]:
        try:
            texto = _html(TELAS[base][2]())
        except Exception as e:
            texto = f"erro ({type(e).__name__})"
        return resp(_tela(TELAS[base][0], texto), _kb_dados(base), TELAS[base][3])
    return [("answerCallbackQuery", {"callback_query_id": cbid})]


def _p(chat, texto, kb, mid=None):
    d = {"chat_id": chat, "text": texto[:_MAXLEN], "parse_mode": "HTML",
         "disable_web_page_preview": "true", "reply_markup": kb}
    if mid is not None:
        d["message_id"] = mid
    return d


# ---------- efeito de rede (robusto: 429 / parse / not-modified) ----------
def _post(method, params):
    tok = _token()
    enc = {k: (json.dumps(v) if isinstance(v, (dict, list)) else v) for k, v in params.items()}
    req = urllib.request.Request(_API.format(tok, method), data=urllib.parse.urlencode(enc).encode())
    try:
        with urllib.request.urlopen(req, timeout=_TIMEOUT) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:           # Telegram manda JSON de erro no corpo (4xx)
        try:
            return json.load(e)
        except Exception:
            return {"ok": False, "error_code": e.code}


def _chamar(method, params):
    if not _token():
        return {}
    try:
        res = _post(method, params)
        if not res.get("ok"):
            desc = (res.get("description") or "").lower()
            if res.get("error_code") == 429:                       # rate-limit: respeita retry_after
                ra = (res.get("parameters") or {}).get("retry_after", 1)
                time.sleep(min(ra, 30))
                res = _post(method, params)
            elif "not modified" in desc:                           # editar igual = sucesso silencioso
                return {"ok": True}
            elif "parse_mode" in params:                           # HTML quebrou → texto puro SEM tags
                p2 = dict(params)
                p2.pop("parse_mode", None)
                p2["text"] = _STRIP.sub("", p2.get("text", ""))
                res = _post(method, p2)
        return res
    except Exception as e:
        print(f"[bot] {method} falhou: {type(e).__name__}: {str(e)[:120]}", file=sys.stderr)
        return {}


def executar(plano):
    for method, params in plano:
        _chamar(method, params)


def _setup():
    _chamar("setMyCommands", {"commands": [{"command": c, "description": d} for c, d in _COMANDOS]})


def loop(once: bool = False):
    print("[bot] Minuto Real no ar (long-polling, UI pro v3).", file=sys.stderr)
    _setup()
    off = 0
    falhas = 0
    while True:
        r = _chamar("getUpdates", {"offset": off, "timeout": 30})
        if not r.get("ok"):
            if r.get("error_code") == 409:                          # outro poller ativo
                print("[bot] 409: outro getUpdates ativo — backoff 5s.", file=sys.stderr)
                time.sleep(5)
            else:                                                   # rede instável: backoff incremental
                time.sleep(min(2 + falhas, 15))
                falhas += 1
            if once:
                return
            continue
        falhas = 0
        for u in r.get("result", []):
            off = max(off, u.get("update_id", 0) + 1)
            try:
                executar(planejar(u))
            except Exception as e:
                print(f"[bot] update falhou: {type(e).__name__}", file=sys.stderr)
        if once:
            return
        time.sleep(1)


def _token():
    return _cred("telegram_bot_token.txt", "TELEGRAM_BOT_TOKEN")


if __name__ == "__main__":
    loop(once="--once" in sys.argv)
