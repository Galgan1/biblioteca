# -*- coding: utf-8 -*-
"""Dashboard de metadados do canal Minuto Real.

Fontes:
  - metadados.json        : pecas por livro + plano/handoff (IDs, datas previstas)
  - books.json            : titulo/autor/capa/temas
  - datas_coletadas.json  : datas REAIS das APIs (YouTube + Instagram), via videos/coletar_datas.py

Quando ha dado de API, ele MANDA (privacidade, publishAt=programado, publishedAt=publicado/enviado, views).
Saida: metadados/index.html (dashboard premium no tema "Cheat Sheet Verde").

Pipeline:  python videos/coletar_datas.py  →  python gerar_metadados.py
Futuro (por temas): cada livro carrega `temas`; basta trocar o agrupamento.
"""
import json
import html
import os
from pathlib import Path
from datetime import date, datetime, timedelta

ROOT = Path(os.environ.get("MR_BASE", Path(__file__).parent))   # dados (books/metadados/datas/afiliados)
OUT_DIR = Path(os.environ.get("MR_OUT", ROOT / "metadados"))    # onde gravar o index.html (VPS: web root)
OUT_DIR.mkdir(parents=True, exist_ok=True)

books = {b["id"]: b for b in json.loads((ROOT / "books.json").read_text(encoding="utf-8"))}
meta = json.loads((ROOT / "metadados.json").read_text(encoding="utf-8"))
DF = ROOT / "datas_coletadas.json"
datas = json.loads(DF.read_text(encoding="utf-8")) if DF.exists() else {"youtube": {}, "instagram": {}}
YT, IG = datas.get("youtube", {}), datas.get("instagram", {})
IG_MEDIA = datas.get("instagram_media", [])          # midias REAIS no ar
IG_ACCT = datas.get("instagram_account", {})         # {username, media_count, followers_count}
IG_LIVE_IDS = {m.get("id") for m in IG_MEDIA if m.get("id")}
IG_BY_ID = {m.get("id"): m for m in IG_MEDIA}
VISITAS = datas.get("site_visitas", {})              # {slug: hits} via logs nginx
SITE_PERIODO = datas.get("site_periodo", "")
VENDAS = datas.get("amazon_vendas", {})              # {slug|asin: qtd} (opcional)

afil = json.loads((ROOT / "afiliados" / "afiliados.json").read_text(encoding="utf-8"))
ASINS = afil.get("asins", {})
EXCLUIR = set(afil.get("excluir", []))
try:
    LINKS = json.loads((ROOT / "afiliados" / "links.json").read_text(encoding="utf-8"))
except Exception:
    LINKS = {}


def vendas_de(slug):
    if slug in VENDAS:
        return VENDAS[slug]
    asin = ASINS.get(slug)
    if asin and asin in VENDAS:
        return VENDAS[asin]
    return None


def ig_live(pid, title):
    """Retorna a midia ao vivo que corresponde a peca (por id ou legenda), ou None."""
    if pid and pid in IG_BY_ID:
        return IG_BY_ID[pid]
    t = (title or "").lower()
    for m in IG_MEDIA:
        if t and t in (m.get("caption") or "").lower():
            return m
    return None

MES = ["", "jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]
MES_F = ["", "Janeiro", "Fevereiro", "Marco", "Abril", "Maio", "Junho",
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

# situ -> (rotulo, classe)
SIT = {
    "publico":   ("No ar",         "s-pub"),
    "agendado":  ("Agendado",      "s-age"),
    "privado":   ("Privado",       "s-pri"),
    "pendente":  ("Pendente",      "s-pen"),
    "previsto":  ("Previsto",      "s-pre"),
    "rascunho":  ("Rascunho",      "s-ras"),
    "naopub":    ("Nao publicado", "s-nao"),
    "enviado":   ("Enviado",       "s-nao"),
    "produzido": ("Gerado",        "s-pro"),
}
REDE = {"YouTube": ("YouTube", "r-yt"), "YouTube Shorts": ("Shorts", "r-yt"),
        "Instagram": ("Instagram", "r-ig"), "TikTok": ("TikTok", "r-tt")}
TIPO = {"video": "Video-resumo", "short": "Short", "carrossel": "Carrossel"}


def to_brt(iso):
    if not iso:
        return None
    try:
        return datetime.strptime(iso[:19], "%Y-%m-%dT%H:%M:%S") - timedelta(hours=3)
    except Exception:
        return None


def yt_url(rede, pid):
    return ("https://www.youtube.com/shorts/" if rede == "YouTube Shorts" else "https://youtu.be/") + pid


def plano_dt(iso):
    try:
        return datetime.strptime(iso, "%Y-%m-%d")
    except Exception:
        return None


def _m(n, sing, plur):
    if n is None or n == "":
        return None
    n = int(n)
    return f"{n:,}".replace(",", ".") + " " + (sing if n == 1 else plur)


def eng_str(views=None, likes=None, coms=None):
    parts = [p for p in (_m(views, "view", "views"), _m(likes, "like", "likes"),
                         _m(coms, "coment.", "coments.")) if p]
    return " · ".join(parts)


def rec(slug, bm, tipo, rotulo, rede, pub):
    pid = pub.get("id", "")
    plano_iso, hora = pub.get("data", ""), pub.get("hora", "")
    r = {"slug": slug, "title": bm.get("title", slug), "author": bm.get("author", ""),
         "cover": f"../{bm.get('coverUrl','')}" if bm.get("coverUrl") else "",
         "tipo": tipo, "rotulo": rotulo, "rede": rede,
         "situ": "previsto", "date": None, "date_label": "", "link": "", "id": pid,
         "eng": "", "nota": pub.get("nota", "")}

    if rede in ("YouTube", "YouTube Shorts") and pid in YT and "erro" not in YT[pid]:
        a = YT[pid]
        ps = a.get("privacyStatus")
        r["link"] = yt_url(rede, pid)
        if ps == "public":
            r["situ"], r["date"], r["date_label"] = "publico", to_brt(a.get("publishedAt")), "Publicado"
            extra = []
            if a.get("retencao") is not None:
                extra.append(f'{a["retencao"]:.0f}% reten&ccedil;&atilde;o')
            if a.get("ctr") is not None:
                extra.append(f'CTR {a["ctr"]:.1f}%')
            if a.get("subs"):
                extra.append(f'+{a["subs"]} inscr.')
            r["eng"] = " &middot; ".join(filter(None, [eng_str(a.get("viewCount"), a.get("likeCount"), a.get("commentCount"))] + extra))
        elif a.get("publishAt"):
            r["situ"], r["date"], r["date_label"] = "agendado", to_brt(a["publishAt"]), "Agendado"
            if plano_iso and r["date"] and r["date"].strftime("%Y-%m-%d") != plano_iso:
                d = plano_dt(plano_iso)
                r["nota"] = f"remarcado (plano: {d.day:02d}/{MES[d.month]})" if d else "remarcado"
        else:
            r["situ"], r["date"], r["date_label"] = "privado", to_brt(a.get("publishedAt")), "Enviado"
        return r

    if rede == "Instagram":
        live = ig_live(pid, r["title"])
        if live and live.get("timestamp"):
            r["situ"], r["date"], r["date_label"] = "publico", to_brt(live["timestamp"]), "Publicado"
            r["link"] = live.get("permalink", "")
            ins = live.get("insights") or {}
            extra = []
            if ins.get("reach") is not None:
                extra.append(f'{ins["reach"]} alcance')
            if ins.get("saved") is not None:
                extra.append(f'{ins["saved"]} salvos')
            if ins.get("shares") is not None:
                extra.append(f'{ins["shares"]} compart.')
            r["eng"] = " &middot; ".join(filter(None, [eng_str(likes=live.get("like_count"), coms=live.get("comments_count"))] + extra))
        elif pid:  # upload tentado (state tem id), mas nao consta no ar
            r["situ"], r["date_label"] = "enviado", "Enviado, sem confirmacao"
        else:      # gerado localmente, ainda nao enviado (ex.: carrossel)
            st = pub.get("status", "produzido")
            r["situ"], r["date_label"] = ("produzido" if st in ("publico", "produzido") else st), "Gerado (local)"
        return r

    if rede == "TikTok":
        r["situ"], r["date_label"] = "rascunho", "Rascunho"
        return r

    st = pub.get("status", "previsto")
    r["situ"] = st
    if st == "pendente":
        r["date"], r["date_label"] = plano_dt(plano_iso), "Pendente"
    else:
        r["date_label"] = "A produzir" if st == "previsto" else st.capitalize()
    return r


# ---------------------------------------------------------------- coleta
items = []
livros_agg = []
for livro in meta["livros"]:
    slug = livro["slug"]
    bm = books.get(slug, {})
    short_total = sum(1 for p in livro["pecas"] if p["tipo"] == "short")
    grupo = {"slug": slug, "title": bm.get("title", slug), "author": bm.get("author", ""),
             "cover": f"../{bm.get('coverUrl','')}" if bm.get("coverUrl") else "",
             "tags": bm.get("tags", []) or [], "url": bm.get("url", ""),
             "destaque": livro.get("destaque", ""), "video_situ": "previsto",
             "short_done": 0, "short_total": short_total, "reels": 0, "tt": 0, "carr": 0,
             "prox": None}
    for p in livro["pecas"]:
        feito = False
        for pub in p["pubs"]:
            r = rec(slug, bm, p["tipo"], p["rotulo"], pub["rede"], pub)
            items.append(r)
            if p["tipo"] == "video" and pub["rede"] == "YouTube":
                grupo["video_situ"] = r["situ"]
            if p["tipo"] == "short" and pub["rede"] in ("YouTube", "YouTube Shorts") and r["id"]:
                feito = True
            if pub["rede"] == "Instagram" and r["situ"] == "publico":
                grupo["reels"] += 1
            if pub["rede"] == "TikTok":
                grupo["tt"] += 1
            if r["situ"] == "agendado" and r["date"] and (grupo["prox"] is None or r["date"] < grupo["prox"]):
                grupo["prox"] = r["date"]
        if p["tipo"] == "short" and feito:
            grupo["short_done"] += 1
        if p["tipo"] == "carrossel":
            grupo["carr"] += 1
    livros_agg.append(grupo)

# KPIs
def cnt(pred):
    return sum(1 for r in items if pred(r))

kpi = {
    "livros": len(livros_agg),
    "no_ar": cnt(lambda r: r["situ"] == "publico" and r["rede"] in ("YouTube", "YouTube Shorts")),
    "agendado": cnt(lambda r: r["situ"] == "agendado"),
    "pendente": cnt(lambda r: r["situ"] in ("pendente", "previsto", "privado")),
    "pecas": len(items),
    "views": 0,
}
for pid, a in YT.items():
    if a.get("privacyStatus") == "public":
        try:
            kpi["views"] += int(a.get("viewCount") or 0)
        except Exception:
            pass

# proxima publicacao (menor data agendada futura)
hoje = datetime.now()
futuras = sorted([r["date"] for r in items if r["situ"] == "agendado" and r["date"] and r["date"] >= hoje])
prox_pub = futuras[0] if futuras else None


# ---------------------------------------------------------------- helpers de render
def datechip(r):
    d, lab, sit = r["date"], r["date_label"], r["situ"]
    cls = SIT.get(sit, ("", ""))[1]
    if d:
        hora = "" if (d.hour == 0 and d.minute == 0) else f'<span class="d-hr">{d.hour:02d}:{d.minute:02d}</span>'
        return (f'<div class="chip-cal {cls}"><span class="d-day">{d.day:02d}</span>'
                f'<span class="d-mo">{MES[d.month]} {d.year}</span>{hora}'
                f'<span class="d-lab">{lab}</span></div>')
    return f'<div class="chip-cal cal-none {cls}"><span class="d-na">{lab or "&mdash;"}</span></div>'


def item_html(r, show_book=True):
    rrot, rcls = REDE.get(r["rede"], (r["rede"], ""))
    srot, scls = SIT.get(r["situ"], (r["situ"], ""))
    book = (f'<img class="it-cover" src="{r["cover"]}" alt="" loading="lazy">' if (show_book and r["cover"]) else "")
    title_line = (f'<span class="it-book">{html.escape(r["title"])}</span> &middot; ' if show_book else "")
    views = f'<span class="it-views">{r["eng"]}</span>' if r["eng"] else ""
    nota = f'<span class="it-nota">{html.escape(r["nota"])}</span>' if r["nota"] else ""
    if r["link"]:
        link = f'<a class="it-go" href="{r["link"]}" target="_blank" rel="noopener" title="{html.escape(r["id"])}">abrir &#8599;</a>'
    elif r["id"]:
        link = f'<span class="it-go muted" title="{html.escape(r["id"])}">sem link</span>'
    else:
        link = ""
    return f"""<div class="it {scls}" data-rede="{html.escape(r['rede'])}" data-situ="{r['situ']}" data-slug="{r['slug']}">
  {book}
  <div class="it-main">
    <div class="it-title">{title_line}<span class="it-piece">{html.escape(r['rotulo'])}</span></div>
    <div class="it-tags"><span class="badge {rcls}">{rrot}</span><span class="pill {scls}">{srot}</span>{views}{nota}</div>
  </div>
  {datechip(r)}
  <div class="it-link">{link}</div>
</div>"""


# ---- Todos os livros (planilha mestra: os 70 do books.json)
video_by_slug = {g["slug"]: g for g in livros_agg}
SIT_ORD = {"publico": 3, "agendado": 2, "privado": 1, "pendente": 1, "previsto": 1}
book_rows = []
for b in sorted(books.values(), key=lambda x: -VISITAS.get(x["id"], 0)):
    slug = b["id"]
    title, author = b.get("title", slug), b.get("author", "")
    tags = b.get("tags", []) or []
    tema = tags[0] if tags else ""
    url = b.get("url", "")
    cover = f"../{b.get('coverUrl','')}" if b.get("coverUrl") else ""
    vis = VISITAS.get(slug, 0)
    g = video_by_slug.get(slug)
    if g:
        vs = SIT.get(g["video_situ"], (g["video_situ"], ""))
        video_cell, vord = f'<span class="pill {vs[1]}">{vs[0]}</span>', SIT_ORD.get(g["video_situ"], 1)
    else:
        video_cell, vord = '<span class="muted">&mdash;</span>', 0
    if slug in EXCLUIR:
        amz = '<span class="muted">n/a</span>'
    else:
        url_amz = LINKS.get(slug) or b.get("amazon", "")
        amz = (f'<a class="it-go" href="{url_amz}" target="_blank" rel="noopener">comprar &#8599;</a>'
               if url_amz else '<span class="muted">&mdash;</span>')
    v = vendas_de(slug)
    vendas_cell = f'<b>{v}</b>' if v else '<span class="muted">&mdash;</span>'
    cov = (f'<img class="bt-cover" src="{cover}" loading="lazy" alt="">' if cover
           else '<span class="bt-cover bt-none"></span>')
    tlink = (f'<a href="../{url}" target="_blank" rel="noopener">{html.escape(title)}</a>' if url else html.escape(title))
    book_rows.append(f"""<tr data-blob="{html.escape((title+' '+author+' '+' '.join(tags)).lower())}" data-vis="{vis}" data-vendas="{v or 0}" data-video="{vord}" data-title="{html.escape(title.lower())}">
  <td class="bt-livro">{cov}<div class="bt-id"><span class="bt-t">{tlink}</span><span class="bt-a">{html.escape(author)}</span></div></td>
  <td>{html.escape(tema)}</td>
  <td class="bt-prog">{html.escape(b.get('progress',''))}</td>
  <td class="bt-num">{vis}</td>
  <td>{video_cell}</td>
  <td>{amz}</td>
  <td class="bt-num">{vendas_cell}</td>
</tr>""")
books_table = "\n".join(book_rows)
com_amazon = sum(1 for b in books.values() if b["id"] not in EXCLUIR and (LINKS.get(b["id"]) or b.get("amazon")))
tot_visitas = sum(VISITAS.values())

# ---- Agenda (timeline cronologica)
items_sorted = sorted(items, key=lambda r: (0, r["date"]) if r["date"] else (1, datetime(9999, 1, 1)))
tl_blocks, atual = [], None
for r in items_sorted:
    lab = (f"{MES_F[r['date'].month]} de {r['date'].year}" if r["date"] else "Sem data definida")
    if lab != atual:
        if atual is not None:
            tl_blocks.append("</div></section>")
        passado = bool(r["date"]) and r["date"] < hoje
        tl_blocks.append(f'<section class="tl-grp"><h3 class="tl-h{" past" if passado else ""}">{lab}</h3><div class="tl-items">')
        atual = lab
    tl_blocks.append(item_html(r, show_book=True))
if atual is not None:
    tl_blocks.append("</div></section>")
timeline = "\n".join(tl_blocks)

# ---- Por livro (mesmo item, sem capa repetida)
porlivro = []
for g in livros_agg:
    its = [r for r in items if r["slug"] == g["slug"]]
    cover = (f'<img class="pl-cover" src="{g["cover"]}" alt="" loading="lazy">' if g["cover"] else "")
    rows = "\n".join(item_html(r, show_book=False) for r in its)
    dest = f'<p class="pl-dest">{html.escape(g["destaque"])}</p>' if g["destaque"] else ""
    bib = f'<a class="pl-bib" href="../{g["url"]}" target="_blank">cheat sheet &#8599;</a>' if g["url"] else ""
    porlivro.append(f"""<section class="pl" data-slug="{g['slug']}" data-blob="{html.escape((g['title']+' '+g['author']+' '+' '.join(g['tags'])).lower())}">
  <div class="pl-head">{cover}<div><div class="pl-title">{html.escape(g['title'])} {bib}</div>
  <div class="pl-author">{html.escape(g['author'])}</div></div></div>
  {dest}
  <div class="pl-items">{rows}</div>
</section>""")
porlivro_html = "\n".join(porlivro)

# ---- Instagram (andamento dos posts) ----
IG_STAGE = {"produzido": 1, "enviado": 2, "publico": 3}
STEP_LABELS = ["Gerado", "Enviado", "No ar"]


def stepper(situ):
    reached = IG_STAGE.get(situ, 0)
    sp = "".join(f'<span class="step {"done" if i <= reached else "todo"}">{lab}</span>'
                 for i, lab in enumerate(STEP_LABELS, start=1))
    return f'<div class="steps">{sp}</div>'


def igrow_html(r):
    srot, scls = SIT.get(r["situ"], (r["situ"], ""))
    date = ""
    if r["situ"] == "publico" and r["date"]:
        d = r["date"]
        date = f'<div class="ig-date">{d.day:02d}/{MES[d.month]}/{d.year}</div>'
    link = (f'<a class="it-go" href="{r["link"]}" target="_blank" rel="noopener">ver post &#8599;</a>'
            if r["link"] else "")
    eng = f'<div class="ig-eng">{r["eng"]}</div>' if r["eng"] else ""
    return f"""<div class="igrow {scls}" data-rede="Instagram" data-situ="{r['situ']}" data-slug="{r['slug']}">
  <div class="ig-main"><div class="ig-piece">{html.escape(r['rotulo'])}</div>{stepper(r['situ'])}</div>
  <div class="ig-end">{eng}<span class="pill {scls}">{srot}</span>{date}{link}</div>
</div>"""


ig_items = [r for r in items if r["rede"] == "Instagram"]
ig_funnel = {
    "gerado": sum(1 for r in ig_items if r["situ"] in ("produzido", "enviado", "publico")),
    "enviado": sum(1 for r in ig_items if r["situ"] in ("enviado", "publico")),
    "no_ar": sum(1 for r in ig_items if r["situ"] == "publico"),
}
ig_secs = []
for g in livros_agg:
    its = [r for r in ig_items if r["slug"] == g["slug"]]
    if not its:
        continue
    cover = f'<img class="pl-cover" src="{g["cover"]}" alt="" loading="lazy">' if g["cover"] else ""
    rows = "\n".join(igrow_html(r) for r in its)
    ig_secs.append(f"""<section class="pl" data-slug="{g['slug']}" data-blob="{html.escape((g['title']+' '+g['author']).lower())}">
  <div class="pl-head">{cover}<div><div class="pl-title">{html.escape(g['title'])}</div></div></div>
  <div class="pl-items">{rows}</div>
</section>""")
acct_name = IG_ACCT.get("username", "minutoreal1701")
acct_count = IG_ACCT.get("media_count", 0)
acct_foll = IG_ACCT.get("followers_count", 0)
aviso = ('<p class="ig-aviso">Nenhum post no ar ainda. As pe&ccedil;as abaixo j&aacute; foram geradas; '
         'os Reels tiveram envio sem confirma&ccedil;&atilde;o (n&atilde;o constam na conta via API).</p>'
         if acct_count == 0 else "")
ig_banner = f"""<div class="ig-acct">
  <div class="ig-acct-head">
    <span class="ig-at">@{html.escape(str(acct_name))}</span>
    <span class="ig-stat"><b>{acct_count}</b> posts no ar</span>
    <span class="ig-stat"><b>{acct_foll}</b> seguidores</span>
  </div>
  <div class="ig-funnel">
    <span class="ff"><b>{ig_funnel['gerado']}</b> geradas</span><span class="farrow">&rarr;</span>
    <span class="ff"><b>{ig_funnel['enviado']}</b> enviadas</span><span class="farrow">&rarr;</span>
    <span class="ff hi"><b>{ig_funnel['no_ar']}</b> no ar</span>
  </div>
  {aviso}
</div>"""
instagram_html = ig_banner + "\n".join(ig_secs)

# ---------------------------------------------------------------- insights + tendencias
HIST = datas.get("historico", [])
views_delta = (HIST[-1]["views_total"] - HIST[-2]["views_total"]) if len(HIST) >= 2 else None

# oportunidades: livros mais visitados que ainda NAO viraram video
oport = sorted((b for b in books.values() if b["id"] not in video_by_slug),
               key=lambda b: -VISITAS.get(b["id"], 0))
oport = [b for b in oport if VISITAS.get(b["id"], 0) >= 4][:5]

# alertas acionaveis
alertas = []
_n = sum(1 for r in items if r["tipo"] == "video" and r["situ"] == "pendente")
if _n:
    alertas.append(("s-pen", f"{_n} video(s) construido(s) aguardando upload no YouTube (cota diaria)"))
_n = sum(1 for r in items if r["rede"] == "Instagram" and r["situ"] == "enviado")
if _n:
    alertas.append(("s-nao", f"{_n} Reel(s) do Instagram sem confirmacao na conta — refazer/checar"))
_n = sum(1 for r in items if r["rede"] == "TikTok" and r["situ"] == "rascunho")
if _n:
    alertas.append(("s-ras", f"{_n} TikTok(s) parado(s) em rascunho — publicar"))
if (not VENDAS) or all(str(k).startswith("_") for k in VENDAS):
    alertas.append(("s-pre", "Vendas Amazon sem dados — colar relatorio em amazon_vendas.json"))

prox7 = sorted((r for r in items if r["situ"] == "agendado" and r["date"]
                and hoje <= r["date"] <= hoje + timedelta(days=7)), key=lambda r: r["date"])[:8]

_empty = '<li class="ins-empty">nada por aqui &#10003;</li>'
oport_html = "".join(
    f'<li><a href="../{b.get("url","")}" target="_blank">{html.escape(b.get("title",""))}</a>'
    f'<span class="ins-n">{VISITAS.get(b["id"],0)} visitas &middot; sem video</span></li>' for b in oport) or _empty
prox_html = "".join(
    f'<li><b>{r["date"].day:02d}/{MES[r["date"].month]}</b> {html.escape(r["title"])}'
    f'<span class="ins-n">{html.escape(r["rotulo"])} &middot; {REDE.get(r["rede"],(r["rede"],""))[0]}</span></li>'
    for r in prox7) or _empty
alert_html = "".join(
    f'<li><span class="dot {cls}"></span>{html.escape(txt)}</li>' for cls, txt in alertas) or _empty

# cadencia: pecas datadas por mes
from collections import Counter
cad = Counter()
for r in items:
    if r["date"]:
        cad[(r["date"].year, r["date"].month)] += 1
cad_mx = max(cad.values()) if cad else 1
cad_bars = "".join(
    f'<div class="bar" title="{v} pecas">'
    f'<div class="bar-track"><div class="bar-fill" style="height:{max(8,int(v/cad_mx*100))}%"></div></div>'
    f'<span class="bar-n">{v}</span><span class="bar-l">{MES[m]}/{str(y)[2:]}</span></div>'
    for (y, m), v in sorted(cad.items())) or '<div class="spark-empty">sem datas ainda</div>'


def svg_spark(vals, w=220, h=44):
    if len(vals) < 2:
        return '<div class="spark-empty">1 ponto coletado — a curva aparece a partir de 2 dias</div>'
    mn, mx = min(vals), max(vals)
    rng = (mx - mn) or 1
    pts = " ".join(f"{i/(len(vals)-1)*w:.1f},{h-(v-mn)/rng*(h-6)-3:.1f}" for i, v in enumerate(vals))
    return (f'<svg class="spark" viewBox="0 0 {w} {h}" preserveAspectRatio="none">'
            f'<polyline points="{pts}"/></svg>')


spark = svg_spark([h["views_total"] for h in HIST])
spark_lo = HIST[0]["views_total"] if HIST else 0
spark_hi = HIST[-1]["views_total"] if HIST else 0
delta_html = ""
if views_delta is not None:
    delta_html = f'<span class="kpi-delta">{"+" if views_delta >= 0 else ""}{views_delta} desde ontem</span>'

col = to_brt(datas.get("coletado_em", "").replace("+00:00", "Z")) if datas.get("coletado_em") else None
col_str = f"{col.day:02d}/{MES[col.month]}/{col.year} {col.hour:02d}:{col.minute:02d}" if col else "n/d"
prox_str = f"{prox_pub.day:02d}/{MES[prox_pub.month]}" if prox_pub else "&mdash;"
gerado = meta.get("gerado_em", str(date.today()))

HTML = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex, nofollow">
<title>Painel &middot; Minuto Real</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;500;600;700;800&family=Literata:opsz,wght@7..72,400;7..72,600;7..72,700&display=swap" rel="stylesheet">
<link rel="icon" type="image/svg+xml" href="../assets/favicon.svg">
<style>
:root {{
  --green: oklch(52% 0.14 152); --green-dark: oklch(42% 0.13 152); --green-deep: oklch(33% 0.10 152);
  --green-light: oklch(95% 0.03 152); --on-green: oklch(99% 0.005 152);
  --ink: oklch(24% 0.015 152); --muted: oklch(48% 0.012 152); --line: oklch(89% 0.008 152);
  --bg: oklch(97% 0.006 152); --card: oklch(99.5% 0.002 152); --hover: oklch(96.5% 0.014 152);
  --amber: oklch(58% 0.14 70); --amber-bg: oklch(94% 0.06 75);
  --red: oklch(56% 0.18 25); --red-bg: oklch(94% 0.05 25);
  --orange: oklch(62% 0.16 50); --orange-bg: oklch(94% 0.06 50);
  --blue: oklch(56% 0.13 250); --blue-bg: oklch(94% 0.05 250);
  --violet: oklch(54% 0.16 305); --violet-bg: oklch(94% 0.05 305);
  --teal: oklch(56% 0.11 200); --teal-bg: oklch(94% 0.04 200);
  --radius: 16px; --radius-sm: 10px;
  --shadow: 0 1px 2px oklch(20% 0.02 152 / .05), 0 8px 28px oklch(20% 0.04 152 / .07);
  --shadow-sm: 0 1px 2px oklch(20% 0.02 152 / .06), 0 3px 10px oklch(20% 0.03 152 / .05);
  --font: 'Hanken Grotesk', system-ui, sans-serif; --serif: 'Literata', Georgia, serif;
}}
@media (prefers-color-scheme: dark) {{
  :root {{
    --green: oklch(70% 0.13 152); --green-dark: oklch(76% 0.12 152); --green-deep: oklch(58% 0.12 152);
    --green-light: oklch(30% 0.05 152); --on-green: oklch(15% 0.02 152);
    --ink: oklch(94% 0.01 152); --muted: oklch(68% 0.012 152); --line: oklch(33% 0.012 152);
    --bg: oklch(15% 0.012 152); --card: oklch(20% 0.012 152); --hover: oklch(25% 0.015 152);
    --amber: oklch(80% 0.13 75); --amber-bg: oklch(32% 0.06 75);
    --red: oklch(72% 0.16 25); --red-bg: oklch(31% 0.07 25);
    --orange: oklch(76% 0.14 50); --orange-bg: oklch(33% 0.07 50);
    --blue: oklch(74% 0.12 250); --blue-bg: oklch(31% 0.06 250);
    --violet: oklch(76% 0.14 305); --violet-bg: oklch(32% 0.07 305);
    --teal: oklch(75% 0.10 200); --teal-bg: oklch(31% 0.05 200);
    --shadow: 0 1px 2px oklch(0% 0 0 / .3), 0 10px 30px oklch(0% 0 0 / .35);
    --shadow-sm: 0 1px 2px oklch(0% 0 0 / .25), 0 4px 12px oklch(0% 0 0 / .25);
  }}
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--bg); color: var(--ink); font-family: var(--font);
  line-height: 1.5; -webkit-font-smoothing: antialiased; font-size: 15px; }}
.wrap {{ max-width: 1240px; margin: 0 auto; padding: 1.5rem 1.25rem 5rem; }}
a {{ color: var(--green-dark); }}
.muted {{ color: var(--muted); }}

/* hero */
.hero {{ position: relative; border-radius: var(--radius); padding: 2rem 2rem 1.75rem; margin-bottom: 1.5rem;
  background: linear-gradient(135deg, var(--green-deep), var(--green-dark)); color: var(--on-green);
  box-shadow: var(--shadow); overflow: hidden; }}
.hero::after {{ content: ""; position: absolute; right: -80px; top: -80px; width: 300px; height: 300px; border-radius: 50%;
  background: radial-gradient(circle, oklch(99% 0.03 152 / .14), transparent 70%); }}
.hero .eyebrow {{ font-size: .72rem; letter-spacing: .18em; text-transform: uppercase; font-weight: 700; opacity: .82; }}
.hero h1 {{ font-family: var(--serif); font-weight: 700; font-size: clamp(1.8rem, 4.2vw, 2.7rem); margin: .35rem 0 .4rem; }}
.hero p {{ margin: 0; max-width: 64ch; opacity: .9; font-size: .96rem; }}
.hero .meta {{ margin-top: .9rem; font-size: .8rem; opacity: .8; display: flex; gap: 1.2rem; flex-wrap: wrap; }}
.hero .back {{ color: var(--on-green); text-decoration: none; font-weight: 600; opacity: .9; }}

/* kpis */
.kpis {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: .8rem; margin-bottom: 1.6rem; }}
.kpi {{ background: var(--card); border: 1px solid var(--line); border-radius: var(--radius-sm); padding: 1rem 1.1rem;
  box-shadow: var(--shadow-sm); position: relative; overflow: hidden; }}
.kpi::before {{ content: ""; position: absolute; left: 0; top: 0; bottom: 0; width: 4px; background: var(--green); }}
.kpi.k-age::before {{ background: var(--amber); }} .kpi.k-pen::before {{ background: var(--orange); }}
.kpi.k-view::before {{ background: var(--violet); }} .kpi.k-prox::before {{ background: var(--blue); }}
.kpi b {{ display: block; font-family: var(--serif); font-weight: 700; font-size: 2rem; line-height: 1; color: var(--ink); }}
.kpi span {{ font-size: .78rem; color: var(--muted); display: block; margin-top: .35rem; }}

h2.sec {{ font-family: var(--serif); font-weight: 700; font-size: 1.35rem; margin: 2rem 0 1rem; display: flex; align-items: center; gap: .6rem; }}
h2.sec::before {{ content: ""; width: 22px; height: 3px; background: var(--green); border-radius: 2px; }}

/* acervo (grade) */
.grade {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(290px, 1fr)); gap: .9rem; }}
.card {{ display: flex; gap: .9rem; text-align: left; cursor: pointer; font-family: var(--font);
  background: var(--card); border: 1px solid var(--line); border-radius: var(--radius-sm); padding: .9rem;
  box-shadow: var(--shadow-sm); transition: transform .15s, box-shadow .15s, border-color .15s; color: inherit; }}
.card:hover {{ transform: translateY(-3px); box-shadow: var(--shadow); border-color: var(--green); }}
.card[aria-pressed="true"] {{ border-color: var(--green); box-shadow: 0 0 0 2px var(--green) inset, var(--shadow); }}
.cd-cover {{ width: 58px; height: 84px; object-fit: cover; border-radius: 6px; border: 1px solid var(--line); flex-shrink: 0; }}
.cd-none {{ background: var(--green-light); }}
.cd-body {{ min-width: 0; flex: 1; }}
.cd-title {{ font-family: var(--serif); font-weight: 700; font-size: 1.02rem; color: var(--ink); line-height: 1.2; }}
.cd-author {{ font-size: .8rem; color: var(--muted); margin: .1rem 0 .45rem; }}
.cd-temas {{ display: flex; gap: .25rem; flex-wrap: wrap; margin-bottom: .45rem; }}
.cd-chips {{ display: flex; gap: .3rem; flex-wrap: wrap; }}
.ck {{ font-size: .68rem; font-weight: 600; border: 1px solid var(--line); border-radius: 6px; padding: .08rem .42rem; background: var(--hover); color: var(--ink); }}
.ck-prox {{ font-size: .72rem; color: var(--blue); font-weight: 600; margin-top: .5rem; }}
.ck-prox.ok {{ color: var(--green-dark); }}
.tema {{ font-size: .66rem; color: var(--green-dark); border: 1px solid var(--green); border-radius: 999px; padding: .04rem .45rem; }}

/* toolbar */
.bar {{ display: flex; flex-wrap: wrap; gap: .5rem; align-items: center; margin: 1.4rem 0 1.1rem;
  position: sticky; top: 0; z-index: 9; padding: .7rem 0; background: var(--bg); }}
.views-tg {{ display: flex; background: var(--card); border: 1px solid var(--line); border-radius: 999px; padding: 3px; box-shadow: var(--shadow-sm); }}
.views-tg button {{ border: 0; background: transparent; color: var(--muted); font-family: var(--font); font-weight: 700;
  font-size: .82rem; padding: .35rem .9rem; border-radius: 999px; cursor: pointer; }}
.views-tg button[aria-pressed="true"] {{ background: var(--green); color: var(--on-green); }}
#busca {{ flex: 1; min-width: 180px; padding: .55rem .85rem; border: 1px solid var(--line); border-radius: 999px;
  background: var(--card); color: var(--ink); font-family: var(--font); font-size: .9rem; box-shadow: var(--shadow-sm); }}
.fg {{ display: flex; gap: .25rem; flex-wrap: wrap; }}
.fbtn {{ border: 1px solid var(--line); background: var(--card); color: var(--ink); border-radius: 999px;
  padding: .3rem .7rem; font-size: .78rem; cursor: pointer; font-family: var(--font); box-shadow: var(--shadow-sm); }}
.fbtn[aria-pressed="true"] {{ background: var(--green); color: var(--on-green); border-color: var(--green); }}
.btn-csv {{ border: 0; background: var(--ink); color: var(--bg); border-radius: 999px; padding: .35rem .9rem;
  font-size: .78rem; cursor: pointer; font-weight: 700; font-family: var(--font); }}
.fchip {{ display: none; align-items: center; gap: .4rem; background: var(--green-light); color: var(--green-dark);
  border-radius: 999px; padding: .3rem .7rem; font-size: .8rem; font-weight: 600; }}
.fchip button {{ border: 0; background: var(--green-dark); color: var(--on-green); width: 18px; height: 18px;
  border-radius: 50%; cursor: pointer; font-size: .75rem; line-height: 1; }}

/* item (linha) */
.it {{ display: flex; align-items: center; gap: .85rem; background: var(--card); border: 1px solid var(--line);
  border-left: 4px solid var(--muted); border-radius: var(--radius-sm); padding: .7rem .9rem; box-shadow: var(--shadow-sm);
  transition: transform .12s, box-shadow .12s; }}
.it:hover {{ transform: translateX(2px); box-shadow: var(--shadow); }}
.it.s-pub {{ border-left-color: var(--green); }} .it.s-age {{ border-left-color: var(--amber); }}
.it.s-pri {{ border-left-color: var(--blue); }} .it.s-pen {{ border-left-color: var(--red); }}
.it.s-nao {{ border-left-color: var(--orange); }} .it.s-ras {{ border-left-color: var(--violet); }}
.it.s-pro {{ border-left-color: var(--teal); }} .it.s-pre {{ border-left-color: var(--line); }}
.it-cover {{ width: 38px; height: 54px; object-fit: cover; border-radius: 5px; border: 1px solid var(--line); flex-shrink: 0; }}
.it-main {{ flex: 1; min-width: 0; }}
.it-title {{ font-size: .94rem; line-height: 1.3; }}
.it-book {{ font-weight: 700; color: var(--ink); }}
.it-piece {{ color: var(--muted); }}
.it-tags {{ display: flex; align-items: center; gap: .4rem; flex-wrap: wrap; margin-top: .3rem; }}
.badge {{ font-size: .68rem; font-weight: 700; padding: .1rem .5rem; border-radius: 5px; }}
.r-yt {{ background: var(--red-bg); color: var(--red); }}
.r-ig {{ background: var(--violet-bg); color: var(--violet); }}
.r-tt {{ background: var(--hover); color: var(--ink); }}
.pill {{ font-size: .68rem; font-weight: 700; padding: .1rem .55rem; border-radius: 999px; }}
.s-pub {{ }} .pill.s-pub {{ background: var(--green); color: var(--on-green); }}
.pill.s-age {{ background: var(--amber-bg); color: var(--amber); }}
.pill.s-pri {{ background: var(--blue-bg); color: var(--blue); }}
.pill.s-pen {{ background: var(--red-bg); color: var(--red); }}
.pill.s-nao {{ background: var(--orange-bg); color: var(--orange); }}
.pill.s-ras {{ background: var(--violet-bg); color: var(--violet); }}
.pill.s-pro {{ background: var(--teal-bg); color: var(--teal); }}
.pill.s-pre {{ background: var(--hover); color: var(--muted); }}
.it-views {{ font-size: .72rem; color: var(--muted); font-weight: 600; }}
.it-nota {{ font-size: .72rem; color: var(--orange); font-style: italic; }}

/* calendar chip */
.chip-cal {{ flex-shrink: 0; width: 92px; text-align: center; border-radius: var(--radius-sm); padding: .35rem .2rem;
  background: var(--hover); border: 1px solid var(--line); line-height: 1.1; }}
.chip-cal .d-day {{ display: block; font-family: var(--serif); font-weight: 700; font-size: 1.35rem; color: var(--ink); }}
.chip-cal .d-mo {{ display: block; font-size: .66rem; text-transform: uppercase; letter-spacing: .04em; color: var(--muted); }}
.chip-cal .d-hr {{ display: block; font-size: .66rem; color: var(--muted); margin-top: .05rem; }}
.chip-cal .d-lab {{ display: block; font-size: .62rem; font-weight: 700; text-transform: uppercase; letter-spacing: .03em; margin-top: .2rem; }}
.chip-cal .d-na {{ font-size: .72rem; font-weight: 700; color: var(--muted); }}
.chip-cal.cal-none {{ display: flex; align-items: center; justify-content: center; min-height: 50px; }}
.chip-cal.s-pub {{ background: var(--green-light); }} .chip-cal.s-pub .d-lab {{ color: var(--green-dark); }}
.chip-cal.s-age {{ background: var(--amber-bg); }} .chip-cal.s-age .d-lab {{ color: var(--amber); }}
.chip-cal.s-pri {{ background: var(--blue-bg); }} .chip-cal.s-pri .d-lab {{ color: var(--blue); }}
.chip-cal.s-pen {{ background: var(--red-bg); }} .chip-cal.s-pen .d-lab, .chip-cal.s-pen .d-na {{ color: var(--red); }}
.chip-cal.s-nao .d-na {{ color: var(--orange); }} .chip-cal.s-ras .d-na {{ color: var(--violet); }}
.it-link {{ flex-shrink: 0; width: 56px; text-align: right; }}
.it-go {{ font-size: .8rem; font-weight: 700; text-decoration: none; white-space: nowrap; }}

/* timeline groups */
.tl-grp {{ margin-bottom: 1.4rem; }}
.tl-h {{ font-family: var(--serif); font-weight: 700; font-size: 1.05rem; color: var(--green-dark);
  margin: 0 0 .7rem; display: flex; align-items: center; gap: .6rem; }}
.tl-h::after {{ content: ""; flex: 1; height: 1px; background: var(--line); }}
.tl-h.past {{ color: var(--muted); }}
.tl-items {{ display: flex; flex-direction: column; gap: .55rem; }}

/* por livro */
.pl {{ background: var(--card); border: 1px solid var(--line); border-radius: var(--radius); padding: 1.1rem;
  margin-bottom: 1rem; box-shadow: var(--shadow-sm); }}
.pl-head {{ display: flex; gap: .9rem; align-items: center; margin-bottom: .9rem; }}
.pl-cover {{ width: 50px; height: 72px; object-fit: cover; border-radius: 6px; border: 1px solid var(--line); }}
.pl-title {{ font-family: var(--serif); font-weight: 700; font-size: 1.2rem; color: var(--green-dark); }}
.pl-bib {{ font-size: .72rem; font-weight: 600; }}
.pl-author {{ font-size: .85rem; color: var(--muted); }}
.pl-dest {{ font-size: .82rem; color: var(--muted); font-style: italic; margin: 0 0 .8rem; }}
.pl-items {{ display: flex; flex-direction: column; gap: .5rem; }}

#agenda, #porlivro, #instagram {{ display: none; }}

/* tabela mestra de livros */
.tbl-hint {{ font-size: .8rem; color: var(--muted); margin: 0 0 .7rem; }}
.tbl-wrap {{ overflow-x: auto; background: var(--card); border: 1px solid var(--line); border-radius: var(--radius); box-shadow: var(--shadow-sm); }}
table.books {{ width: 100%; border-collapse: collapse; font-size: .88rem; min-width: 740px; }}
table.books th {{ position: sticky; top: 0; background: var(--card); text-align: left; font-size: .7rem; text-transform: uppercase;
  letter-spacing: .04em; color: var(--muted); font-weight: 700; padding: .7rem .8rem; border-bottom: 2px solid var(--line); white-space: nowrap; }}
table.books th[data-sort] {{ cursor: pointer; user-select: none; }}
table.books th[data-sort]:hover {{ color: var(--green-dark); }}
table.books th.sorted {{ color: var(--green-dark); }}
table.books th.sorted::after {{ content: " ▾"; }}
table.books th.sorted.asc::after {{ content: " ▴"; }}
table.books td {{ padding: .5rem .8rem; border-bottom: 1px solid var(--line); vertical-align: middle; }}
table.books tbody tr:last-child td {{ border-bottom: 0; }}
table.books tbody tr:hover {{ background: var(--hover); }}
.bt-livro {{ min-width: 230px; }}
.bt-livro {{ display: flex; align-items: center; gap: .7rem; }}
.bt-cover {{ width: 32px; height: 46px; object-fit: cover; border-radius: 4px; border: 1px solid var(--line); flex-shrink: 0; }}
.bt-none {{ display: inline-block; background: var(--green-light); }}
.bt-id {{ display: flex; flex-direction: column; min-width: 0; }}
.bt-t {{ font-weight: 700; line-height: 1.2; }}
.bt-t a {{ text-decoration: none; color: var(--ink); }} .bt-t a:hover {{ color: var(--green-dark); }}
.bt-a {{ font-size: .76rem; color: var(--muted); }}
.bt-prog {{ font-size: .78rem; color: var(--muted); white-space: nowrap; }}
.bt-num {{ text-align: right; font-variant-numeric: tabular-nums; font-weight: 700; }}

/* instagram view */
.ig-acct {{ background: linear-gradient(135deg, var(--violet-bg), var(--card)); border: 1px solid var(--line);
  border-radius: var(--radius); padding: 1.1rem 1.3rem; margin-bottom: 1.2rem; box-shadow: var(--shadow-sm); }}
.ig-acct-head {{ display: flex; align-items: baseline; gap: 1.3rem; flex-wrap: wrap; }}
.ig-at {{ font-family: var(--serif); font-weight: 700; font-size: 1.3rem; color: var(--violet); }}
.ig-stat {{ font-size: .85rem; color: var(--muted); }}
.ig-stat b {{ font-size: 1.05rem; color: var(--ink); font-family: var(--serif); }}
.ig-funnel {{ display: flex; align-items: center; gap: .7rem; margin-top: .8rem; flex-wrap: wrap; }}
.ff {{ background: var(--card); border: 1px solid var(--line); border-radius: 999px; padding: .3rem .85rem; font-size: .82rem; color: var(--muted); }}
.ff b {{ color: var(--ink); font-family: var(--serif); font-size: 1.05rem; margin-right: .15rem; }}
.ff.hi {{ background: var(--green-light); border-color: var(--green); }} .ff.hi b {{ color: var(--green-dark); }}
.farrow {{ color: var(--muted); font-weight: 700; }}
.ig-aviso {{ margin: .9rem 0 0; font-size: .82rem; color: var(--orange); }}
.igrow {{ display: flex; align-items: center; gap: 1rem; justify-content: space-between; background: var(--card);
  border: 1px solid var(--line); border-left: 4px solid var(--muted); border-radius: var(--radius-sm);
  padding: .7rem .9rem; box-shadow: var(--shadow-sm); }}
.igrow.s-pub {{ border-left-color: var(--green); }} .igrow.s-nao {{ border-left-color: var(--orange); }}
.igrow.s-pro {{ border-left-color: var(--teal); }} .igrow.s-pre {{ border-left-color: var(--line); }}
.ig-main {{ min-width: 0; flex: 1; }}
.ig-piece {{ font-weight: 600; font-size: .92rem; margin-bottom: .5rem; }}
.ig-end {{ display: flex; align-items: center; gap: .7rem; flex-shrink: 0; }}
.ig-date {{ font-size: .78rem; color: var(--muted); }}
.steps {{ display: flex; align-items: center; gap: 0; }}
.step {{ position: relative; font-size: .7rem; font-weight: 700; padding: .18rem .6rem .18rem 1.3rem; }}
.step::before {{ content: ""; position: absolute; left: .55rem; top: 50%; transform: translateY(-50%);
  width: 9px; height: 9px; border-radius: 50%; background: var(--line); border: 2px solid var(--line); }}
.step + .step {{ margin-left: .2rem; }}
.step + .step::after {{ content: ""; position: absolute; left: -.55rem; top: 50%; width: .9rem; height: 2px; background: var(--line); }}
.step.done {{ color: var(--green-dark); }}
.step.done::before {{ background: var(--green); border-color: var(--green); }}
.step.done + .step.done::after {{ background: var(--green); }}
.step.todo {{ color: var(--muted); }}
/* insights + tendencias */
.kpi-delta {{ display: inline-block; margin-left: .4rem; color: var(--green-dark); font-weight: 700; font-size: .72rem; }}
.insights {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: .9rem; margin-bottom: 1.1rem; }}
.ins-card {{ background: var(--card); border: 1px solid var(--line); border-radius: var(--radius-sm); padding: 1rem 1.1rem; box-shadow: var(--shadow-sm); }}
.ins-card h3 {{ font-family: var(--serif); font-size: 1rem; margin: 0 0 .6rem; color: var(--ink); }}
.ins-list {{ list-style: none; margin: 0; padding: 0; display: flex; flex-direction: column; gap: .5rem; }}
.ins-list li {{ font-size: .85rem; line-height: 1.35; display: flex; flex-direction: column; }}
.ins-list li a {{ font-weight: 700; text-decoration: none; color: var(--green-dark); }}
.ins-list li b {{ color: var(--ink); }}
.ins-n {{ font-size: .76rem; color: var(--muted); }}
.ins-empty {{ color: var(--muted); font-style: italic; }}
.ins-foot {{ font-size: .72rem; color: var(--muted); margin: .7rem 0 0; }}
.dot {{ display: inline-block; width: 9px; height: 9px; border-radius: 50%; margin-right: .5rem; flex-shrink: 0; }}
.ins-list li {{ flex-direction: row; align-items: baseline; }}
.ins-list li.ins-empty {{ flex-direction: row; }}
.dot.s-pen {{ background: var(--red); }} .dot.s-nao {{ background: var(--orange); }}
.dot.s-ras {{ background: var(--violet); }} .dot.s-pre {{ background: var(--muted); }}
.ins-card:nth-child(3) .ins-list li {{ gap: 0; }}
.trends {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: .9rem; margin-bottom: 1.4rem; }}
.trend-card {{ background: var(--card); border: 1px solid var(--line); border-radius: var(--radius-sm); padding: 1rem 1.1rem; box-shadow: var(--shadow-sm); }}
.trend-h {{ font-weight: 700; font-size: .85rem; margin-bottom: .7rem; display: flex; justify-content: space-between; align-items: baseline; }}
.trend-sub {{ font-size: .72rem; color: var(--muted); font-weight: 500; }}
.spark {{ width: 100%; height: 48px; }}
.spark polyline {{ fill: none; stroke: var(--green); stroke-width: 2; vector-effect: non-scaling-stroke; stroke-linejoin: round; stroke-linecap: round; }}
.spark-empty {{ font-size: .78rem; color: var(--muted); font-style: italic; padding: .8rem 0; }}
.bars {{ display: flex; align-items: flex-end; gap: .5rem; height: 90px; }}
.bar {{ flex: 1; display: flex; flex-direction: column; align-items: center; gap: .25rem; min-width: 0; }}
.bar-track {{ width: 100%; max-width: 34px; height: 56px; display: flex; align-items: flex-end; }}
.bar-fill {{ width: 100%; background: var(--green); border-radius: 4px 4px 0 0; min-height: 4px; }}
.bar-n {{ font-size: .72rem; font-weight: 700; color: var(--green-dark); }}
.bar-l {{ font-size: .64rem; color: var(--muted); white-space: nowrap; }}
.vazio {{ text-align: center; color: var(--muted); padding: 3rem; display: none; }}
footer {{ margin-top: 2.5rem; padding-top: 1.2rem; border-top: 1px solid var(--line); font-size: .78rem; color: var(--muted); }}
footer code {{ font-size: .72rem; color: var(--green-dark); background: var(--green-light); padding: .05rem .35rem; border-radius: 4px; }}
@media (max-width: 560px) {{
  .it {{ flex-wrap: wrap; }} .it-link {{ width: auto; }} .chip-cal {{ width: 78px; }}
  .hero {{ padding: 1.5rem 1.25rem; }}
}}
</style>
</head>
<body>
<div class="wrap">
  <div class="hero">
    <div class="eyebrow">Minuto Real &middot; Painel de Publica&ccedil;&otilde;es</div>
    <h1>O que cada livro virou</h1>
    <p>Acervo completo de livros e o que cada um virou. <strong>Livros</strong> = a planilha de todos os t&iacute;tulos com visitas do site e link Amazon;
       <strong>Agenda/Por livro/Instagram</strong> = as pe&ccedil;as (v&iacute;deo, Shorts, Reels) com datas reais das APIs &mdash; programada, remarcada e publicada.</p>
    <div class="meta">
      <span>Atualizado em <strong>{col_str}</strong></span>
      <span>Pr&oacute;xima publica&ccedil;&atilde;o: <strong>{prox_str}</strong></span>
      <a class="back" href="../">&larr; Biblioteca</a>
    </div>
  </div>

  <div class="kpis">
    <div class="kpi"><b>{len(books)}</b><span>livros no acervo</span></div>
    <div class="kpi k-prox"><b>{tot_visitas}</b><span>visitas no site (~14d)</span></div>
    <div class="kpi"><b>{kpi['livros']}</b><span>com v&iacute;deo</span></div>
    <div class="kpi k-age"><b>{kpi['no_ar']}</b><span>no ar (YouTube)</span></div>
    <div class="kpi k-view"><b>{kpi['views']}</b><span>views YouTube{delta_html}</span></div>
    <div class="kpi k-pen"><b>{com_amazon}</b><span>com link Amazon</span></div>
  </div>

  <div class="insights">
    <div class="ins-card">
      <h3>&#128640; Oportunidades</h3>
      <ul class="ins-list">{oport_html}</ul>
      <p class="ins-foot">mais visitados sem v&iacute;deo &mdash; pr&oacute;ximos a produzir</p>
    </div>
    <div class="ins-card">
      <h3>&#128197; Pr&oacute;ximos 7 dias</h3>
      <ul class="ins-list">{prox_html}</ul>
    </div>
    <div class="ins-card">
      <h3>&#9888; Aten&ccedil;&atilde;o</h3>
      <ul class="ins-list">{alert_html}</ul>
    </div>
  </div>

  <div class="trends">
    <div class="trend-card">
      <div class="trend-h">Views no YouTube <span class="trend-sub">{spark_lo} &rarr; {spark_hi}</span></div>
      {spark}
    </div>
    <div class="trend-card">
      <div class="trend-h">Cad&ecirc;ncia de publica&ccedil;&atilde;o <span class="trend-sub">pe&ccedil;as por m&ecirc;s</span></div>
      <div class="bars">{cad_bars}</div>
    </div>
  </div>

  <div class="bar">
    <div class="views-tg" id="viewTg">
      <button data-v="livros" aria-pressed="true">Livros</button>
      <button data-v="agenda" aria-pressed="false">Agenda</button>
      <button data-v="livro" aria-pressed="false">Por livro</button>
      <button data-v="instagram" aria-pressed="false">Instagram</button>
    </div>
    <input type="search" id="busca" placeholder="Buscar livro, autor ou tema...">
    <div class="fg" id="fRede">
      <button class="fbtn" aria-pressed="true" data-f="all">Redes</button>
      <button class="fbtn" data-f="YouTube">YT</button>
      <button class="fbtn" data-f="YouTube Shorts">Shorts</button>
      <button class="fbtn" data-f="Instagram">IG</button>
      <button class="fbtn" data-f="TikTok">TikTok</button>
    </div>
    <div class="fg" id="fSitu">
      <button class="fbtn" aria-pressed="true" data-s="all">Status</button>
      <button class="fbtn" data-s="publico">No ar</button>
      <button class="fbtn" data-s="agendado">Agendado</button>
      <button class="fbtn" data-s="pendente">Pendente</button>
    </div>
    <button class="btn-csv" id="csv">CSV</button>
  </div>

  <div id="livros">
    <p class="tbl-hint">Todos os {len(books)} livros do acervo &middot; ordene clicando nos cabe&ccedil;alhos &middot; <strong>visitas</strong> = hits da p&aacute;gina nos logs do site ({SITE_PERIODO}).</p>
    <div class="tbl-wrap"><table class="books">
      <thead><tr>
        <th data-sort="title">Livro</th>
        <th>Tema</th>
        <th>Conte&uacute;do</th>
        <th data-sort="vis" class="sorted">Visitas</th>
        <th data-sort="video">V&iacute;deo</th>
        <th>Amazon</th>
        <th data-sort="vendas">Vendas</th>
      </tr></thead>
      <tbody>{books_table}</tbody>
    </table></div>
  </div>
  <div id="agenda">{timeline}</div>
  <div id="porlivro">{porlivro_html}</div>
  <div id="instagram">{instagram_html}</div>
  <p class="vazio" id="vazio">Nenhuma pe&ccedil;a corresponde aos filtros.</p>

  <footer>
    Fontes (coletadas em {col_str}): <strong>YouTube Data API v3</strong> (datas + views) &middot; <strong>Instagram Graph</strong> (posts) &middot;
    <strong>logs do nginx</strong> (visitas por p&aacute;gina, {SITE_PERIODO}) &middot; <code>afiliados.json</code> (links Amazon, tag andregalgani-20).<br>
    <strong>Vendas Amazon:</strong> sem API (PA-API exige 3 vendas; relat&oacute;rio s&oacute; no painel Associados). Para preencher, baixe o relat&oacute;rio e salve <code>amazon_vendas.json</code> (&#123;slug ou ASIN: quantidade&#125;) &mdash; a coluna Vendas passa a mostrar os n&uacute;meros.<br>
    Instagram (@minutoreal1701): {acct_count} posts no ar. Atualizar tudo: <code>python videos/coletar_datas.py</code> &rarr; <code>python gerar_metadados.py</code> &rarr; deploy.
  </footer>
</div>

<script>
let fRede='all', fSitu='all', q='', view='livros';
const $=s=>document.querySelector(s), $$=s=>[...document.querySelectorAll(s)];
const CONT = {{livros:'#livros', agenda:'#agenda', livro:'#porlivro', instagram:'#instagram'}};

function apply() {{
  if (view==='livros') {{
    let any=false;
    $$('#livros tbody tr').forEach(tr=>{{ const ok=!q||tr.dataset.blob.includes(q); tr.style.display=ok?'':'none'; if(ok)any=true; }});
    $('#vazio').style.display = any?'none':'block'; return;
  }}
  const cont = CONT[view];
  const rows = $$(cont+' .it, '+cont+' .igrow');
  rows.forEach(r=>{{
    const blob = (r.closest('.pl')?.dataset.blob || '') + ' ' + r.textContent.toLowerCase();
    const ok = (fRede==='all' || r.dataset.rede===fRede)
      && (fSitu==='all' || r.dataset.situ===fSitu)
      && (!q || blob.includes(q));
    r.style.display = ok ? '' : 'none';
  }});
  $$('#agenda .tl-grp').forEach(g=>{{ g.style.display = g.querySelector('.it:not([style*="none"])') ? '' : 'none'; }});
  $$('#porlivro .pl, #instagram .pl').forEach(p=>{{
    p.style.display = p.querySelector('.it:not([style*="none"]), .igrow:not([style*="none"])') ? '' : 'none';
  }});
  const any = rows.some(r=>r.style.display!=='none');
  $('#vazio').style.display = any ? 'none' : 'block';
}}
function group(id, attr, fn) {{
  $$('#'+id+' button').forEach(b=>b.addEventListener('click',()=>{{
    $$('#'+id+' button').forEach(x=>x.setAttribute('aria-pressed','false'));
    b.setAttribute('aria-pressed','true'); fn(b.dataset[attr]); apply();
  }}));
}}
group('fRede','f',v=>fRede=v);
group('fSitu','s',v=>fSitu=v);
$('#viewTg').querySelectorAll('button').forEach(b=>b.addEventListener('click',()=>{{
  $('#viewTg').querySelectorAll('button').forEach(x=>x.setAttribute('aria-pressed','false'));
  b.setAttribute('aria-pressed','true'); view=b.dataset.v;
  $('#livros').style.display = view==='livros'?'block':'none';
  $('#agenda').style.display = view==='agenda'?'block':'none';
  $('#porlivro').style.display = view==='livro'?'block':'none';
  $('#instagram').style.display = view==='instagram'?'block':'none';
  const peca = view!=='livros';
  $('#fRede').style.display = peca?'':'none';
  $('#fSitu').style.display = peca?'':'none';
  apply();
}}));
$('#busca').addEventListener('input',e=>{{ q=e.target.value.toLowerCase().trim(); apply(); }});

// ordenacao da planilha de livros
$$('#livros th[data-sort]').forEach(th=>th.addEventListener('click',()=>{{
  const key=th.dataset.sort, tb=$('#livros tbody');
  const asc = th.classList.contains('sorted') ? !th.classList.contains('asc') : (key==='title');
  $$('#livros th').forEach(h=>h.classList.remove('sorted','asc'));
  th.classList.add('sorted'); if(asc) th.classList.add('asc');
  const rows=[...tb.querySelectorAll('tr')];
  rows.sort((a,b)=> key==='title'
    ? (asc?a.dataset.title.localeCompare(b.dataset.title):b.dataset.title.localeCompare(a.dataset.title))
    : (asc?(+a.dataset[key])-(+b.dataset[key]):(+b.dataset[key])-(+a.dataset[key])));
  rows.forEach(r=>tb.appendChild(r));
}}));

// inicio: view Livros, filtros de peca ocultos
$('#fRede').style.display='none'; $('#fSitu').style.display='none';

$('#csv').addEventListener('click',()=>{{
  const cl=e=>e?e.textContent.replace(/\\s+/g,' ').trim():'';
  let L, fname;
  if (view==='livros') {{
    L=[['Livro','Autor','Tema','Conteudo','Visitas','Video','Amazon','Vendas']];
    $$('#livros tbody tr').forEach(tr=>{{
      if (tr.style.display==='none') return;
      const td=tr.querySelectorAll('td');
      const amz=td[5].querySelector('a')?.href || cl(td[5]);
      L.push([cl(td[0].querySelector('.bt-t')), cl(td[0].querySelector('.bt-a')), cl(td[1]), cl(td[2]), cl(td[3]), cl(td[4]), amz, cl(td[6])]);
    }});
    fname='minuto-real-livros';
  }} else {{
    const cont=CONT[view];
    L=[['Livro','Peca','Rede','Situacao','Data','DataLabel','Link']];
    $$(cont+' .it, '+cont+' .igrow').forEach(it=>{{
      if (it.style.display==='none') return;
      const piece = (it.querySelector('.it-piece')||it.querySelector('.ig-piece'))?.textContent||'';
      const book = it.querySelector('.it-book')?.textContent || it.closest('.pl')?.querySelector('.pl-title')?.childNodes[0].textContent.trim() || '';
      const rede = it.querySelector('.badge')?.textContent || 'Instagram';
      const cal = it.querySelector('.chip-cal');
      const day=cl(cal?.querySelector('.d-day')), mo=cl(cal?.querySelector('.d-mo')), na=cl(cal?.querySelector('.d-na'));
      const igdate=cl(it.querySelector('.ig-date'));
      const lab=cl(cal?.querySelector('.d-lab'))||na;
      const data=day?(day+' '+mo):(igdate||na);
      const link=it.querySelector('a.it-go')?.href||'';
      L.push([book.trim(),piece.trim(),rede.trim(),cl(it.querySelector('.pill')),data.trim(),lab.trim(),link]);
    }});
    fname='minuto-real-metadados';
  }}
  const csv=L.map(r=>r.map(v=>'"'+String(v).replace(/"/g,'""')+'"').join(',')).join('\\n');
  const b=new Blob(['\\ufeff'+csv],{{type:'text/csv;charset=utf-8;'}});
  const a=document.createElement('a'); a.href=URL.createObjectURL(b); a.download=fname+'.csv'; a.click();
}});
</script>
</body>
</html>"""

(OUT_DIR / "index.html").write_text(HTML, encoding="utf-8")
print(f"OK -> {OUT_DIR/'index.html'}  ({len(livros_agg)} livros, {len(items)} pecas)")
print(f"KPIs: {kpi} | proxima: {prox_str}")
