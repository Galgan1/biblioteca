"""Adiciona o link de afiliado da Amazon na descricao dos videos do canal.

  python videos/afiliado_youtube.py list    # SO LEITURA: lista videos + casamento com livro
  python videos/afiliado_youtube.py apply    # edita as descricoes (idempotente)

Usa o token ja existente (.secrets/token_v2.json, escopo force-ssl). Nunca dispara
login interativo: se o token estiver invalido, encerra pedindo pra rodar upload_youtube.py.
Casa video->livro pelo titulo (titulo do livro aparece no titulo do video). Pega o
link em ../afiliados/links.json. Append idempotente (marcador), preserva o resto da descricao.
"""

import json
import re
import sys
import unicodedata
from pathlib import Path

from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

ROOT = Path(__file__).resolve().parent
BASE = ROOT.parent
TOKEN = ROOT / ".secrets" / "token_v2.json"
SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]

MARCADOR = "📕 Compre o livro"


def creds():
    if not TOKEN.exists():
        sys.exit(f"[!] token nao encontrado: {TOKEN} — rode upload_youtube.py uma vez.")
    c = Credentials.from_authorized_user_file(str(TOKEN), SCOPES)
    if not c.valid:
        if c.expired and c.refresh_token:
            c.refresh(Request())
        else:
            sys.exit(
                "[!] token invalido/expirado sem refresh — rode upload_youtube.py p/ reautorizar."
            )
    return c


def norm(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9 ]", " ", s)


def casa_livro(titulo_video, books):
    nv = norm(titulo_video)
    melhor = None
    for b in books:
        nt = norm(b["title"])
        # casa se o titulo do livro (>=4 chars) aparece no titulo do video
        if len(nt) >= 4 and nt in nv:
            if melhor is None or len(nt) > len(norm(melhor["title"])):
                melhor = b
    return melhor


def listar_videos(yt):
    up = yt.channels().list(part="contentDetails", mine=True).execute()
    pl = up["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
    ids, tok = [], None
    while True:
        r = (
            yt.playlistItems()
            .list(part="contentDetails", playlistId=pl, maxResults=50, pageToken=tok)
            .execute()
        )
        ids += [it["contentDetails"]["videoId"] for it in r["items"]]
        tok = r.get("nextPageToken")
        if not tok:
            break
    vids = []
    for i in range(0, len(ids), 50):
        r = yt.videos().list(part="snippet", id=",".join(ids[i : i + 50])).execute()
        vids += r["items"]
    return vids


def bloco_afiliado(book, url):
    return (
        f"\n\n———\n{MARCADOR} \"{book['title']}\" na Amazon: {url}\n"
        f"Como Associado da Amazon, ganho com compras qualificadas — sem custo extra para você."
    )


def main():
    modo = sys.argv[1] if len(sys.argv) > 1 else "list"
    books = json.loads((BASE / "books.json").read_text(encoding="utf-8"))
    links = json.loads((BASE / "afiliados" / "links.json").read_text(encoding="utf-8"))
    yt = build("youtube", "v3", credentials=creds())
    vids = listar_videos(yt)

    print(f"{len(vids)} videos no canal\n")
    planos = []
    for v in vids:
        vid = v["id"]
        sn = v["snippet"]
        titulo = sn["title"]
        is_short = "#shorts" in (titulo + sn.get("description", "")).lower()
        book = casa_livro(titulo, books)
        tem_link = MARCADOR in sn.get("description", "")
        url = links.get(book["id"]) if book else None
        status = (
            "ja tem"
            if tem_link
            else "ADD"
            if (url and not is_short)
            else "short"
            if is_short
            else "sem match"
            if not book
            else "livro excluido"
        )
        print(f"[{status:>12}] {vid}  {titulo[:58]}")
        if book:
            print(f"               -> {book['id']}  {url}")
        if status == "ADD":
            planos.append((vid, sn, book, url))

    print(f"\n{len(planos)} video(s) receberiam o link.")
    if modo == "apply":
        for vid, sn, book, url in planos:
            novo = sn.get("description", "") + bloco_afiliado(book, url)
            body = {
                "id": vid,
                "snippet": {
                    "title": sn["title"],
                    "categoryId": sn.get("categoryId", "27"),
                    "description": novo[:5000],
                    "tags": sn.get("tags", []),
                },
            }
            if sn.get("defaultLanguage"):
                body["snippet"]["defaultLanguage"] = sn["defaultLanguage"]
            yt.videos().update(part="snippet", body=body).execute()
            print(f"OK editado: {vid}  ({book['id']})")
        print(f"\n{len(planos)} descricao(oes) atualizada(s).")
    else:
        print("(dry-run — nada foi editado. Rode com 'apply' para gravar.)")


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    main()
