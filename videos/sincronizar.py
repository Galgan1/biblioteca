# -*- coding: utf-8 -*-
"""ORQUESTRADOR da sincronia YouTube -> Instagram (coreografia "eco").

Para cada livro, o post do Instagram dispara como ECO algumas horas DEPOIS de o
vídeo longo entrar no ar no YouTube, dentro de uma janela de no máximo 4h. O
disparo em si roda na VPS (sempre ligada) — veja ig_runner_vps.py. Este script
roda no PC: calcula a hora-alvo do IG, prepara a mídia, envia para a pasta
provisória da VPS (mantendo cópia de segurança no PC) e enfileira o job num
manifesto JSON idempotente que é espelhado para a VPS.

ANCHOR = o publishAt do longo no YouTube (definido por agendar_lote.py:
SEG e QUI 19h BRT). Aqui o anchor entra como argumento (DD/MM[ HH:MM], default
19:00 BRT) — o mesmo horário usado para agendar o longo.

HORA IG = anchor + OFFSET. OFFSET default = +2h, configurável, e TRAVADO em
<= 4h (a peça de IG é sempre um eco DEPOIS do longo, nunca antes nem fora da
janela). Ex.: longo SEG 19h -> Reel SEG 21h.

Peça sincronizada padrão = o REEL-HERÓI do livro (o 1º short, cena
cfg['shorts'][0], arquivo _shorts/<slug>_NN.mp4). A fila é extensível para
carrossel/citação (campo "tipo").

Uso:
  python sincronizar.py enqueue <slug> [DD/MM] [HH:MM] [--offset H] [--tipo reel]
  python sincronizar.py enqueue <slug> --dry-run [DD/MM] [HH:MM] [--offset H]
  python sincronizar.py list
  python sincronizar.py push        # reenvia só o manifesto para a VPS

Stdlib only. Console Windows = cp1252: sem caractere não-ASCII em print().
"""
import sys
import json
import time
import subprocess
from datetime import datetime, timedelta, timezone
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

ROOT = Path(__file__).parent
SH = ROOT / '_shorts'
SYNC = ROOT / '_sync'
MANIFEST = SYNC / 'sync_manifest.json'

BRT = timezone(timedelta(hours=-3))
DOW = ['seg', 'ter', 'qua', 'qui', 'sex', 'sab', 'dom']

# Coreografia do eco: IG depois do longo, dentro de uma janela curta.
OFFSET_DEFAULT_H = 2.0          # +2h por padrao
MAX_OFFSET_H = 4.0             # trava dura: nunca mais que 4h depois do longo

# VPS (sempre ligada). A pasta provisoria fica FORA da web, dentro de /opt.
VPS_HOST = 'root@andregalgani.com.br'
VPS_BASE = '/opt/minutoreal'
VPS_PROVISORIO = f'{VPS_BASE}/ig-provisorio'        # /opt/minutoreal/ig-provisorio/<slug>/
VPS_MANIFEST = f'{VPS_BASE}/sync_manifest.json'


def _cfg(slug):
    f = ROOT / 'roteiros' / f'{slug}.json'
    if not f.exists():
        sys.exit(f'[!] roteiro ausente: {f}')
    return json.loads(f.read_text(encoding='utf-8'))


def hero_index(cfg):
    """Indice da cena-heroi = o 1o short do livro (cfg['shorts'][0])."""
    shorts = cfg.get('shorts') or []
    if not shorts:
        sys.exit('[!] roteiro sem lista "shorts"; nao da para escolher o Reel-heroi.')
    return shorts[0]


def parse_anchor(ddmm, hhmm):
    """anchor em BRT a partir de DD/MM e HH:MM (default hoje / 19:00)."""
    agora = datetime.now(BRT)
    if ddmm:
        d, m = map(int, ddmm.split('/'))
        ano = agora.year
        # se a data ja passou neste ano, assume o proximo ano
        cand = datetime(ano, m, d, tzinfo=BRT)
        if cand.date() < agora.date():
            cand = datetime(ano + 1, m, d, tzinfo=BRT)
    else:
        cand = agora
    if hhmm:
        h, mi = map(int, hhmm.split(':'))
    else:
        h, mi = 19, 0
    return cand.replace(hour=h, minute=mi, second=0, microsecond=0)


def clamp_offset(offset_h):
    """Garante 0 < offset <= 4h. Eco: sempre DEPOIS, nunca alem da janela."""
    if offset_h <= 0:
        print(f'  [aviso] offset {offset_h}h invalido (eco e DEPOIS do longo); usando {OFFSET_DEFAULT_H}h')
        offset_h = OFFSET_DEFAULT_H
    if offset_h > MAX_OFFSET_H:
        print(f'  [aviso] offset {offset_h}h excede a janela; travando em {MAX_OFFSET_H}h')
        offset_h = MAX_OFFSET_H
    return offset_h


def ig_time(anchor, offset_h):
    return anchor + timedelta(hours=offset_h)


def load_manifest():
    if MANIFEST.exists():
        return json.loads(MANIFEST.read_text(encoding='utf-8'))
    return []


def save_manifest(jobs):
    SYNC.mkdir(exist_ok=True)
    MANIFEST.write_text(json.dumps(jobs, ensure_ascii=False, indent=1), encoding='utf-8')


def push_manifest():
    """Espelha o manifesto para a VPS (idempotente; o runner le de la)."""
    if not MANIFEST.exists():
        print('  [i] nada para enviar (manifesto local nao existe)')
        return False
    subprocess.run(['ssh', VPS_HOST, f'mkdir -p {VPS_PROVISORIO}'], check=True)
    r = subprocess.run(['scp', '-q', str(MANIFEST), f'{VPS_HOST}:{VPS_MANIFEST}'],
                       capture_output=True, text=True)
    if r.returncode == 0:
        print('  manifesto enviado para a VPS OK')
        return True
    print(f'  [!] scp do manifesto falhou: {r.stderr[:160]}')
    return False


def upload_media(slug, media_files):
    """Envia a midia do job para a pasta provisoria da VPS (a copia do PC fica).
    Retorna a lista de caminhos remotos."""
    remote_dir = f'{VPS_PROVISORIO}/{slug}'
    subprocess.run(['ssh', VPS_HOST, f'mkdir -p {remote_dir}'], check=True)
    remotes = []
    for f in media_files:
        p = Path(f)
        if not p.exists():
            sys.exit(f'[!] midia ausente: {p} (gere o short antes de enfileirar)')
        r = subprocess.run(['scp', '-q', str(p), f'{VPS_HOST}:{remote_dir}/{p.name}'],
                           capture_output=True, text=True)
        if r.returncode != 0:
            sys.exit(f'[!] scp da midia falhou ({p.name}): {r.stderr[:160]}')
        remotes.append(f'{remote_dir}/{p.name}')
        print(f'  enviado p/ provisorio VPS: {p.name}')
    return remotes


def build_job(slug, tipo, anchor, offset_h):
    """Monta o dict do job (sem efeitos colaterais). tipo: reel | carousel | quote."""
    cfg = _cfg(slug)
    offset_h = clamp_offset(offset_h)
    alvo = ig_time(anchor, offset_h)
    job = {
        'slug': slug,
        'tipo': tipo,
        'parte': None,
        'anchor_brt': anchor.strftime('%Y-%m-%dT%H:%M:%S%z'),
        'ig_alvo_brt': alvo.strftime('%Y-%m-%dT%H:%M:%S%z'),
        'ig_alvo_utc': alvo.astimezone(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'offset_h': offset_h,
        'youtube_id': None,        # opcional: id do longo p/ o runner confirmar "publico"
        'status': 'pendente',      # pendente -> publicado | falhou
        'media': [],               # caminhos REMOTOS na pasta provisoria da VPS
        'criado_em': int(time.time()),
    }
    if tipo == 'reel':
        idx = hero_index(cfg)
        job['parte'] = idx
        job['media_local'] = [str(SH / f'{slug}_{idx:02d}.mp4')]
        # comando que o runner roda na VPS (instagram_post.py file <mp4> "<legenda>")
        # a legenda e calculada na VPS no momento do disparo (caption_for do poster).
        job['cmd'] = ['file_reel', slug, idx]
    elif tipo == 'carousel':
        job['parte'] = 'overview'
        job['media_local'] = []     # carrossel hospeda via VPS no proprio poster
        job['cmd'] = ['carousel', slug, 'overview']
    else:
        sys.exit(f'[!] tipo "{tipo}" ainda nao suportado (use reel | carousel).')
    return job


def job_key(job):
    return (job['slug'], job['tipo'], job.get('parte'))


def enqueue(slug, ddmm=None, hhmm=None, offset_h=OFFSET_DEFAULT_H, tipo='reel',
            youtube_id=None, dry_run=False):
    anchor = parse_anchor(ddmm, hhmm)
    job = build_job(slug, tipo, anchor, offset_h)
    job['youtube_id'] = youtube_id
    alvo = datetime.fromisoformat(job['ig_alvo_brt'])

    print('=== SINCRONIA YouTube -> Instagram (eco) ===')
    print(f'  slug      : {slug}')
    print(f'  tipo      : {tipo} (parte {job["parte"]})')
    print(f'  anchor    : {anchor:%a %d/%m %H:%M} BRT  (publishAt do longo)')
    print(f'  offset    : +{job["offset_h"]}h  (travado em <= {MAX_OFFSET_H}h)')
    print(f'  IG dispara: {alvo:%a %d/%m %H:%M} BRT  ({alvo.astimezone(timezone.utc):%H:%M} UTC)')
    dentro = (alvo - anchor) <= timedelta(hours=MAX_OFFSET_H) and alvo > anchor
    print(f'  janela    : {"OK eco dentro de 4h" if dentro else "FORA DA JANELA"}')

    if dry_run:
        print('  [DRY-RUN] nada enviado, nada enfileirado.')
        print('  media local (backup no PC):')
        for m in job.get('media_local', []):
            ex = 'existe' if Path(m).exists() else 'AUSENTE'
            print(f'    - {m}  [{ex}]')
        return job

    # 1) sobe a midia para a pasta provisoria da VPS (copia do PC permanece)
    if job.get('media_local'):
        job['media'] = upload_media(slug, job['media_local'])

    # 2) merge idempotente no manifesto (mesma chave slug/tipo/parte = atualiza)
    jobs = load_manifest()
    k = job_key(job)
    jobs = [j for j in jobs if job_key(j) != k or j.get('status') == 'publicado']
    if any(job_key(j) == k and j.get('status') == 'publicado' for j in jobs):
        print('  [i] ja PUBLICADO antes; mantendo registro, nao reenfileira.')
    else:
        jobs.append(job)
        save_manifest(jobs)
        print(f'  enfileirado no manifesto ({MANIFEST.name}); total de jobs: {len(jobs)}')

    # 3) espelha o manifesto para a VPS
    push_manifest()
    return job


def cmd_list():
    jobs = load_manifest()
    if not jobs:
        print('manifesto vazio')
        return
    for j in jobs:
        alvo = j.get('ig_alvo_brt', '?')
        print(f"  [{j.get('status'):9}] {j['slug']:22} {j['tipo']:8} parte={j.get('parte')}  IG={alvo}")


def _parse_cli(args):
    """Extrai flags --offset/--tipo/--yt/--dry-run e os posicionais DD/MM, HH:MM."""
    offset = OFFSET_DEFAULT_H
    tipo = 'reel'
    youtube_id = None
    dry = False
    pos = []
    i = 0
    while i < len(args):
        a = args[i]
        if a == '--offset':
            offset = float(args[i + 1]); i += 2
        elif a == '--tipo':
            tipo = args[i + 1]; i += 2
        elif a == '--yt':
            youtube_id = args[i + 1]; i += 2
        elif a in ('--dry-run', '--dry'):
            dry = True; i += 1
        else:
            pos.append(a); i += 1
    ddmm = pos[0] if len(pos) >= 1 else None
    hhmm = pos[1] if len(pos) >= 2 else None
    return ddmm, hhmm, offset, tipo, youtube_id, dry


if __name__ == '__main__':
    a = sys.argv[1:]
    if not a:
        sys.exit('uso: python sincronizar.py enqueue <slug> [DD/MM] [HH:MM] '
                 '[--offset H] [--tipo reel|carousel] [--yt <id>] [--dry-run]  |  list  |  push')
    if a[0] == 'list':
        cmd_list()
    elif a[0] == 'push':
        push_manifest()
    elif a[0] == 'enqueue' and len(a) >= 2:
        slug = a[1]
        ddmm, hhmm, offset, tipo, yt, dry = _parse_cli(a[2:])
        enqueue(slug, ddmm, hhmm, offset, tipo, yt, dry)
    else:
        sys.exit('comando invalido. uso: enqueue <slug> [...] | list | push')
