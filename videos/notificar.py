# -*- coding: utf-8 -*-
"""notificar.py — alerta via Telegram (Akita pilar 7: erro COM contexto + alerta out-of-band).

Usado quando o operador NÃO está olhando o site (ex.: PC local offline, job da VPS falhou).
Best-effort: sem token/chat_id ou sem rede → loga em stderr e segue (nunca quebra o caller).

SETUP (uma vez, seu):
  1. No Telegram, fale com @BotFather → /newbot → copie o TOKEN.
  2. Salve em  videos/.secrets/telegram_bot_token.txt   (gitignored)
  3. Mande qualquer mensagem pro seu bot novo, depois rode:
       python notificar.py --chatid        (mostra o chat_id; salve em telegram_chat_id.txt)
  4. Teste:  python notificar.py "ola do Minuto Real"
"""
import json
import os
import sys
import urllib.parse
import urllib.request
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT = Path(__file__).parent
_TIMEOUT = 15


def _cred(arquivo: str, env: str) -> str:
    """Lê credencial do env (1º) ou de .secrets/<arquivo> (2º). Ausente → '' (não levanta)."""
    v = os.environ.get(env, "").strip()
    if v:
        return v
    try:
        return (ROOT / ".secrets" / arquivo).read_text(encoding="utf-8").strip()
    except Exception:
        return ""


def notificar(texto: str) -> bool:
    """Manda `texto` pro Telegram. True se enviou; False se não deu (sem cred/rede). NUNCA levanta."""
    token = _cred("telegram_bot_token.txt", "TELEGRAM_BOT_TOKEN")
    chat = _cred("telegram_chat_id.txt", "TELEGRAM_CHAT_ID")
    if not token or not chat:
        print("  [notificar] sem token/chat_id do Telegram -> alerta NAO enviado "
              "(ver setup no topo de notificar.py)", file=sys.stderr)
        return False
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = urllib.parse.urlencode({"chat_id": chat, "text": (texto or "")[:4000],
                                   "disable_web_page_preview": "true"}).encode()
    try:
        with urllib.request.urlopen(urllib.request.Request(url, data=data), timeout=_TIMEOUT) as r:
            return bool(json.load(r).get("ok"))
    except Exception as e:
        print(f"  [notificar] falha ao enviar ao Telegram: {type(e).__name__}: {str(e)[:140]}",
              file=sys.stderr)
        return False


def _mostrar_chatid() -> int:
    """Helper de setup: lê o token e imprime os chat_id que já mandaram mensagem pro bot."""
    token = _cred("telegram_bot_token.txt", "TELEGRAM_BOT_TOKEN")
    if not token:
        print("Salve o token em videos/.secrets/telegram_bot_token.txt primeiro.")
        return 1
    try:
        with urllib.request.urlopen(f"https://api.telegram.org/bot{token}/getUpdates", timeout=_TIMEOUT) as r:
            ups = json.load(r).get("result", [])
    except Exception as e:
        print(f"erro no getUpdates: {str(e)[:160]}")
        return 1
    chats = {str(u.get("message", {}).get("chat", {}).get("id")): u.get("message", {}).get("chat", {}).get("first_name", "")
             for u in ups if u.get("message")}
    chats.pop("None", None)
    if not chats:
        print("Nenhuma mensagem ainda — mande qualquer texto pro seu bot e rode de novo.")
        return 1
    for cid, nome in chats.items():
        print(f"  chat_id = {cid}  ({nome})  -> salve em videos/.secrets/telegram_chat_id.txt")
    return 0


if __name__ == "__main__":
    if "--chatid" in sys.argv:
        sys.exit(_mostrar_chatid())
    msg = " ".join(a for a in sys.argv[1:] if not a.startswith("--")) or "teste de alerta do Minuto Real"
    print("enviado" if notificar(msg) else "NAO enviado (ver setup do Telegram no topo de notificar.py)")
