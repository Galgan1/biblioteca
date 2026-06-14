# -*- coding: utf-8 -*-
"""Pós-produção via API do YouTube (lane YouTube) — 3 alavancas nativas:

  1) LEGENDAS  — gera um SRT a partir da narração + timing das cenas e sobe via
                 captions().insert (escopo youtube.force-ssl).
  2) CAPÍTULOS — injeta timestamps na descrição (regra do YouTube: 1º em 0:00,
                 ≥3 capítulos, ≥10s cada).
  3) PLAYLISTS — garante a playlist temática do canal e adiciona o vídeo.

O timing de cada cena vem de `_stems/<slug>/timing.json` (escrito por gerar_video.py:
`{"tail": 0.7, "durs": [<dur por cena>]}`). Como o master copia a faixa de vídeo sem
deslocar a timeline, o início da cena i = soma das durações anteriores.

Tudo é best-effort: o chamador (upload_youtube.py) embrulha em try/except — nada aqui
pode derrubar o upload. Sem timing.json (ex.: vídeo antigo), legendas/capítulos são
pulados de forma graciosa; a playlist ainda roda.
"""
import json, re
from pathlib import Path
from googleapiclient.http import MediaFileUpload

ROOT = Path(__file__).parent
STEMS = ROOT / '_stems'
LEG = ROOT / '_legendas'


# ---------- timing ----------

def load_timing(slug):
    """Devolve (tail, [durs]) de _stems/<slug>/timing.json, ou None se ausente."""
    f = STEMS / slug / 'timing.json'
    if not f.exists():
        return None
    d = json.loads(f.read_text(encoding='utf-8'))
    return float(d.get('tail', 0.7)), [float(x) for x in d['durs']]


def _starts(durs):
    """Início acumulado de cada cena (a 1ª começa em 0)."""
    t, out = 0.0, []
    for d in durs:
        out.append(t)
        t += d
    return out


# ---------- formatação de tempo ----------

def _srt_ts(sec):
    sec = max(0.0, sec)
    h, rem = divmod(int(sec), 3600)
    m, s = divmod(rem, 60)
    ms = int(round((sec - int(sec)) * 1000))
    if ms > 999:
        ms = 999
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def _chap_ts(sec):
    sec = int(sec)
    h, rem = divmod(sec, 3600)
    m, s = divmod(rem, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


def _sentencas(texto):
    texto = (texto or '').strip()
    if not texto:
        return []
    return [p.strip() for p in re.split(r'(?<=[.!?…])\s+', texto) if p.strip()]


# ---------- legendas (SRT) ----------

def build_srt(cenas, durs, tail):
    """SRT em nível de FRASE: dentro da janela falada de cada cena ([início,
    início+dur−tail]), distribui as frases proporcionalmente ao número de caracteres.
    Aproximação honesta (as pausas SSML já estão embutidas na dur real da cena)."""
    starts = _starts(durs)
    cues = []
    for cena, dur, start in zip(cenas, durs, starts):
        fala = max(0.5, dur - tail)              # tira o respiro final do TAIL
        sents = _sentencas(cena.get('narracao'))
        if not sents:
            continue
        total = sum(len(s) for s in sents) or 1
        cur = start
        for s in sents:
            seg = fala * len(s) / total
            cues.append((cur, min(cur + seg, start + fala), s))
            cur += seg
    blocos = [f"{i}\n{_srt_ts(a)} --> {_srt_ts(b)}\n{txt}"
              for i, (a, b, txt) in enumerate(cues, 1)]
    return "\n\n".join(blocos) + ("\n" if blocos else "")


def upload_caption(yt, video_id, srt_path, language='pt-BR', name='Português'):
    body = {'snippet': {'videoId': video_id, 'language': language,
                        'name': name, 'isDraft': False}}
    media = MediaFileUpload(str(srt_path), mimetype='application/octet-stream', resumable=False)
    yt.captions().insert(part='snippet', body=body, media_body=media).execute()


# ---------- capítulos (na descrição) ----------

def build_chapters(cenas, durs, min_gap=10.0):
    """Linhas de capítulo seguindo a regra do YouTube: 1º em 0:00, ≥3, ≥10s cada.
    Rótulo = título da cena (abertura→Introdução, encerramento→Conclusão)."""
    starts = _starts(durs)
    rotulos = {'abertura': 'Introdução', 'encerramento': 'Conclusão'}
    linhas, last = [], -min_gap
    for cena, ts in zip(cenas, starts):
        label = rotulos.get(cena.get('tipo', 'conceito')) or (cena.get('titulo') or '').strip()
        if not label:
            continue
        if linhas and ts - last < min_gap:        # respeita o mínimo de 10s
            continue
        linhas.append((ts, label))
        last = ts
    if len(linhas) < 3 or linhas[0][0] > 0.5:      # sem 0:00 ou <3 → inválido p/ o YouTube
        return ''
    out = [f"{_chap_ts(ts)} {label}" for ts, label in linhas]
    out[0] = f"0:00 {linhas[0][1]}"                # garante o 0:00 exato
    return "\n".join(out)


def with_chapters(desc, cfg):
    """Anexa o bloco de capítulos à descrição, se houver timing válido."""
    tm = load_timing(cfg['slug'])
    if not tm:
        return desc
    tail, durs = tm
    cenas = cfg['cenas']
    if len(durs) != len(cenas):
        return desc
    bloco = build_chapters(cenas, durs)
    if not bloco or '0:00' in desc:                # nada a fazer / já tem capítulos
        return desc
    return f"{desc}\n\n⏱️ Capítulos\n{bloco}"[:5000]


# ---------- playlists ----------

def playlist_title_for(cfg):
    yt = cfg.get('youtube', {})
    tema = (yt.get('playlist') or cfg.get('tema') or '').strip()
    if not tema:
        return 'Minuto Real — Resumos de Livros'
    return tema if tema.lower().startswith('minuto real') else f'Minuto Real — {tema}'


def ensure_playlist(yt, title):
    """Acha a playlist pelo título (entre as minhas) ou cria uma pública."""
    req = yt.playlists().list(part='snippet', mine=True, maxResults=50)
    while req is not None:
        res = req.execute()
        for it in res.get('items', []):
            if it['snippet']['title'].strip().lower() == title.strip().lower():
                return it['id']
        req = yt.playlists().list_next(req, res)
    res = yt.playlists().insert(part='snippet,status', body={
        'snippet': {'title': title, 'description': 'Resumos cinematográficos de livros — canal Minuto Real.',
                    'defaultLanguage': 'pt-BR'},
        'status': {'privacyStatus': 'public'}}).execute()
    return res['id']


def add_to_playlist(yt, playlist_id, video_id):
    yt.playlistItems().insert(part='snippet', body={'snippet': {
        'playlistId': playlist_id,
        'resourceId': {'kind': 'youtube#video', 'videoId': video_id}}}).execute()


# ---------- orquestração pós-publicação ----------

def post_publish(yt, cfg, video_id):
    """Roda legendas + playlist após o upload. Best-effort; devolve a lista do que saiu."""
    slug = cfg['slug']
    feito = []
    tm = load_timing(slug)
    if tm:
        tail, durs = tm
        cenas = cfg['cenas']
        if len(durs) == len(cenas):
            srt = build_srt(cenas, durs, tail)
            if srt.strip():
                LEG.mkdir(exist_ok=True)
                p = LEG / f'{slug}.srt'
                p.write_text(srt, encoding='utf-8')
                try:
                    upload_caption(yt, video_id, p)
                    feito.append('legendas')
                except Exception as e:
                    print(f"  [aviso] legendas nao subiram: {str(e)[:130]}")
    else:
        print("  [aviso] sem _stems/<slug>/timing.json -> legendas/capitulos pulados (use um build atual)")
    try:
        titulo = playlist_title_for(cfg)
        pid = ensure_playlist(yt, titulo)
        add_to_playlist(yt, pid, video_id)
        feito.append(f'playlist «{titulo}»')
    except Exception as e:
        print(f"  [aviso] playlist pulada: {str(e)[:130]}")
    if feito:
        print("  pos-producao API:", " · ".join(feito))
    return feito
