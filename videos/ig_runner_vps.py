#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""[VPS - ROTINA PERMANENTE] Runner do ECO Instagram da sincronia YouTube->IG.

Roda no cron de /opt/minutoreal. A cada execucao le o manifesto
(sync_manifest.json, espelhado do PC por sincronizar.py) e, para cada job cuja
hora-alvo do IG ja chegou, publica a peca no Instagram via instagram_post.py e
limpa a pasta provisoria daquele job. Idempotente: estado em sync_state.json.

Confirmacao opcional do longo: se o job tem "youtube_id" e as credenciais do
YouTube estao disponiveis (mesmas do comentar_pendentes_vps.py), o runner so
dispara o IG depois de confirmar que o longo esta PUBLIC — garante o eco
("IG depois do longo"). Sem youtube_id ou sem creds, confia na hora-alvo
(o longo ja foi agendado por agendar_lote.py para o anchor).

Manifesto (cada job):
  {"slug","tipo","parte","ig_alvo_utc","youtube_id","status","media":[...remotos...],"cmd":[...]}

Cron sugerido (a cada 15 min; ocioso quando nada vence):
  */15 * * * * /opt/minutoreal/run_ig.sh >> /opt/minutoreal/ig.log 2>&1

Stdlib + (no momento do disparo) instagram_post. Console = sem nao-ASCII em print().
"""
import json
import time
import shutil
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent
MANIFEST = ROOT / 'sync_manifest.json'
STATE = ROOT / 'sync_state.json'
PROVISORIO = ROOT / 'ig-provisorio'


def _load(p, default):
    return json.loads(p.read_text(encoding='utf-8')) if p.exists() else default


def _save(p, data):
    p.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding='utf-8')


def job_key(job):
    return f"{job['slug']}|{job['tipo']}|{job.get('parte')}"


def due(job):
    alvo = datetime.strptime(job['ig_alvo_utc'], '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=timezone.utc)
    return datetime.now(timezone.utc) >= alvo


def longo_publico(youtube_id):
    """True se o longo ja esta public. Best-effort: usa as creds do YouTube se houver.
    Sem id ou sem creds, devolve True (confia na hora-alvo do anchor)."""
    if not youtube_id:
        return True
    try:
        from upload_youtube import get_creds
        from googleapiclient.discovery import build
    except Exception:
        return True
    try:
        yt = build('youtube', 'v3', credentials=get_creds())
        r = yt.videos().list(part='status', id=youtube_id).execute()
        items = r.get('items', [])
        if not items:
            return False
        return items[0]['status']['privacyStatus'] == 'public'
    except Exception as e:
        print(f'  [aviso] checagem YouTube falhou ({str(e)[:80]}); confiando na hora-alvo')
        return True


def publicar(job):
    """Dispara o post no IG conforme cmd do job. Retorna o media_id ou None.
    Importa o poster em runtime (sem editar instagram_post.py)."""
    import instagram_post as ig
    cmd = job.get('cmd') or []
    if not cmd:
        print('  [!] job sem cmd; pulando')
        return None
    kind = cmd[0]
    if kind == 'file_reel':
        slug, idx = cmd[1], cmd[2]
        # midia esta na pasta provisoria; nome = <slug>_NN.mp4
        mp4 = PROVISORIO / slug / f'{slug}_{int(idx):02d}.mp4'
        if not mp4.exists():
            # fallback: 1o .mp4 da pasta do slug
            mp4s = sorted((PROVISORIO / slug).glob('*.mp4'))
            if not mp4s:
                print(f'  [!] midia ausente na provisoria: {mp4}')
                return None
            mp4 = mp4s[0]
        cfg = json.loads((ROOT / 'roteiros' / f'{slug}.json').read_text(encoding='utf-8'))
        caption = ig.caption_for(cfg, int(idx))
        print(f'  publicando Reel-heroi {slug} cena {idx}...')
        return ig.post_reel(str(mp4), caption)
    if kind == 'carousel':
        slug = cmd[1]
        part = cmd[2] if len(cmd) > 2 else 'overview'
        print(f'  publicando carrossel {slug}/{part}...')
        return ig.post_carousel(slug, part, publish=True)
    if kind == 'story':
        slug = cmd[1]
        story_dir = ROOT / '_carrossel' / f'{slug}_stories'
        web_dir = Path('/var/www/andregalgani/biblioteca/_carrossel') / f'{slug}_stories'
        pub_base = 'https://www.andregalgani.com.br/biblioteca/_carrossel'
        try:
            from PIL import Image
            import os
            web_dir.mkdir(parents=True, exist_ok=True)
            urls = []
            for png in sorted(story_dir.glob('[0-9][0-9].png')):
                jpg = web_dir / png.with_suffix('.jpg').name
                with Image.open(png) as im:
                    im.convert('RGB').save(jpg, 'JPEG', quality=88)
                os.chmod(jpg, 0o644)
                urls.append(f'{pub_base}/{slug}_stories/{jpg.name}')
            if not urls:
                print(f'  [!] nenhum frame de story em {story_dir}')
                return None
            print(f'  {len(urls)} frames hospedados em {web_dir}')
            ids = ig.post_story_from_urls(urls, publish=True)
            return ids[0] if ids else None
        except Exception as e:
            print(f'  ERRO story {slug}: {str(e)[:160]}')
            return None
    print(f'  [!] cmd desconhecido: {kind}')
    return None


def limpar_provisorio(job):
    """Remove a pasta provisoria do job na VPS (a copia do PC permanece)."""
    slug = job['slug']
    d = PROVISORIO / slug
    if d.exists():
        shutil.rmtree(d, ignore_errors=True)
        print(f'  provisoria limpa: {d}')


def main():
    jobs = _load(MANIFEST, [])
    state = _load(STATE, {})        # {job_key: {"media_id":..., "em":...}}
    if not jobs:
        print('manifesto vazio - nada a sincronizar')
        return

    pendentes = [j for j in jobs if state.get(job_key(j), {}).get('media_id') is None]
    vencidos = [j for j in pendentes if due(j)]
    if not vencidos:
        print(f'nada vencido agora (pendentes: {len(pendentes)})')
        return

    for job in vencidos:
        k = job_key(job)
        if not longo_publico(job.get('youtube_id')):
            print(f'  aguardando longo ficar publico: {k}')
            continue
        mid = publicar(job)
        if mid:
            state[k] = {'media_id': mid, 'em': int(time.time())}
            job['status'] = 'publicado'
            _save(STATE, state)
            _save(MANIFEST, jobs)
            limpar_provisorio(job)
            print(f'  OK eco publicado: {k} -> {mid}')
        else:
            job['status'] = 'falhou'
            _save(MANIFEST, jobs)
            print(f'  FALHOU: {k} (sera tentado de novo na proxima rodada)')

    feitos = sum(1 for j in jobs if state.get(job_key(j), {}).get('media_id'))
    print(f'jobs publicados: {feitos}/{len(jobs)}')


if __name__ == '__main__':
    main()
