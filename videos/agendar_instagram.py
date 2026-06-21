# -*- coding: utf-8 -*-
"""Popula a fila IG com pelo menos 1 post/dia de Jun/18 a Ago/09.

Para cada entrada: SCP das mídias necessárias + enqueue no manifesto.
- reel     → sincronizar.enqueue (faz scp do mp4)
- carousel → scp PNGs para /opt/minutoreal/_carrossel/ + enqueue
- story    → sincronizar.enqueue (faz scp dos frames)

Extra: 3 Reels avulsos de 48-leis (partes 4, 9, 11) via manifest direto.

Uso: python agendar_instagram.py [--dry-run]
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
MANIFEST = ROOT / '_sync' / 'sync_manifest.json'
CARR = ROOT / '_carrossel'
SHORTS = ROOT / '_shorts'
VPS_HOST = 'root@andregalgani.com.br'
VPS_CARR = '/opt/minutoreal/_carrossel'
VPS_MANIFEST = '/opt/minutoreal/sync_manifest.json'
BRT = timezone(timedelta(hours=-3))

DRY = '--dry-run' in sys.argv or '--dry' in sys.argv

# ---------------------------------------------------------------------------
# Plano: (DD/MM, slug, tipo)  — 1+ posts/dia Jun18 → Ago09
# ---------------------------------------------------------------------------
PLANO = [
    # --- Jun 18-23: Reels dos 6 slugs novos ---
    ('18/06', 'aristoteles-poetica',  'reel'),
    ('19/06', 'futebol-brasileiro',   'reel'),
    ('20/06', 'marketing-4-0',        'reel'),
    ('21/06', 'poder-de-delegar',     'reel'),
    ('22/06', 'poder-do-silencio',    'reel'),
    ('23/06', 'quem-mexeu-no-queijo', 'reel'),
    # --- Jun 24-29: Carrossels dos mesmos ---
    ('24/06', 'aristoteles-poetica',  'carousel'),
    ('25/06', 'futebol-brasileiro',   'carousel'),
    ('26/06', 'marketing-4-0',        'carousel'),
    ('27/06', 'poder-de-delegar',     'carousel'),
    ('28/06', 'poder-dos-quietos',    'carousel'),  # poder-do-silencio sem carrossel gerado
    ('29/06', 'quem-mexeu-no-queijo', 'carousel'),
    # --- Jun 30 / Jul 01-05: Stories ---
    ('30/06', 'aristoteles-poetica',  'story'),
    ('01/07', 'futebol-brasileiro',   'story'),
    ('02/07', 'marketing-4-0',        'story'),
    ('03/07', 'poder-de-delegar',     'story'),
    ('04/07', 'poder-dos-quietos',    'story'),     # poder-do-silencio sem story gerado
    ('05/07', 'quem-mexeu-no-queijo', 'story'),
    # --- Jul 06-09: Carrossels de slugs já postados (catch-up) ---
    ('06/07', 'save-the-cat',         'carousel'),
    ('07/07', 'inteligencia-emocional', 'carousel'),  # maquiavel sem carrossel gerado
    ('08/07', 'mindset',              'carousel'),     # arte-da-guerra sem carrossel gerado
    ('09/07', 'padrao-bitcoin',       'carousel'),
    # --- Jul 10-13: Stories de slugs já postados ---
    ('10/07', 'save-the-cat',         'story'),
    ('11/07', 'inteligencia-emocional', 'story'),
    ('12/07', 'mindset',              'story'),
    ('13/07', 'padrao-bitcoin',       'story'),
    # --- Jul 14-17: Teasers pré-lançamento YouTube (carrossel) ---
    ('14/07', 'sound-design',         'carousel'),
    ('15/07', 'audiovisao',           'carousel'),
    ('16/07', 'coesao-coerencia',     'carousel'),
    ('17/07', 'ponerologia',          'carousel'),
    # --- Jul 18-19 + 21-22: Stories pré-lançamento ---
    ('18/07', 'sound-design',         'story'),
    ('19/07', 'audiovisao',           'story'),
    ('21/07', 'coesao-coerencia',     'story'),
    ('22/07', 'ponerologia',          'story'),
    # --- Jul 24-28: Aquecimento dos Reels de agosto ---
    ('24/07', 'habitos-atomicos',     'carousel'),
    ('25/07', 'sutil-arte',           'carousel'),
    ('26/07', 'habitos-atomicos',     'story'),
    ('28/07', 'sutil-arte',           'story'),
    # --- Jul 29-31 / Ago 01-02 ---
    ('29/07', 'psicologia-financeira','carousel'),
    ('31/07', 'psicologia-financeira','story'),
    ('01/08', 'pai-rico-pai-pobre',   'carousel'),
    ('02/08', 'pai-rico-pai-pobre',   'story'),
]

# Reels avulsos (partes não-herói de 48-leis) — inseridos direto no manifesto
# (ddmm, parte_num)
EXTRAS_48 = [
    ('03/08', 4),   # 48-leis-do-poder_04.mp4
    ('05/08', 9),   # 48-leis-do-poder_09.mp4
    ('07/08', 11),  # 48-leis-do-poder_11.mp4
]


def parse_brt(ddmm, hora=17, minuto=0):
    d, m = map(int, ddmm.split('/'))
    ano = datetime.now(BRT).year
    dt = datetime(ano, m, d, hora, minuto, tzinfo=BRT)
    if dt.date() < datetime.now(BRT).date():
        dt = datetime(ano + 1, m, d, hora, minuto, tzinfo=BRT)
    return dt


def scp_carousel_pngs(slug):
    """Envia os PNGs de _carrossel/{slug}_overview/ para a VPS."""
    local = CARR / f'{slug}_overview'
    pngs = sorted(local.glob('[0-9][0-9].png'))
    if not pngs:
        print(f'  [!] sem PNGs em {local}')
        return False
    remote = f'{VPS_CARR}/{slug}_overview'
    subprocess.run(['ssh', VPS_HOST, f'mkdir -p {remote}'], check=True)
    for p in pngs:
        r = subprocess.run(['scp', '-q', str(p), f'{VPS_HOST}:{remote}/{p.name}'],
                           capture_output=True, text=True)
        if r.returncode != 0:
            print(f'  [!] scp falhou ({p.name}): {r.stderr[:100]}')
            return False
        print(f'  enviado: {p.name}')
    return True


def load_manifest():
    return json.loads(MANIFEST.read_text(encoding='utf-8')) if MANIFEST.exists() else []


def save_and_push(jobs):
    MANIFEST.parent.mkdir(exist_ok=True)
    MANIFEST.write_text(json.dumps(jobs, ensure_ascii=False, indent=1), encoding='utf-8')
    r = subprocess.run(['scp', '-q', str(MANIFEST), f'{VPS_HOST}:{VPS_MANIFEST}'],
                       capture_output=True, text=True)
    if r.returncode == 0:
        print('  manifesto enviado para a VPS OK')
    else:
        print(f'  [!] push manifesto falhou: {r.stderr[:80]}')


def extra_reel_job(slug, parte, ddmm):
    anchor = parse_brt(ddmm, 17, 0)
    alvo = anchor + timedelta(hours=2)
    mp4_local = SHORTS / f'{slug}_{int(parte):02d}.mp4'
    if not mp4_local.exists():
        print(f'  [!] mp4 ausente: {mp4_local}')
        return None
    remote_dir = f'/opt/minutoreal/ig-provisorio/{slug}'
    if not DRY:
        subprocess.run(['ssh', VPS_HOST, f'mkdir -p {remote_dir}'], check=True)
        r = subprocess.run(['scp', '-q', str(mp4_local),
                            f'{VPS_HOST}:{remote_dir}/{mp4_local.name}'],
                           capture_output=True, text=True)
        if r.returncode != 0:
            print(f'  [!] scp mp4 falhou: {r.stderr[:100]}')
            return None
        print(f'  mp4 enviado: {mp4_local.name}')
    return {
        'slug': slug,
        'tipo': 'reel',
        'parte': parte,
        'anchor_brt': anchor.strftime('%Y-%m-%dT%H:%M:%S%z'),
        'ig_alvo_brt': alvo.strftime('%Y-%m-%dT%H:%M:%S%z'),
        'ig_alvo_utc': alvo.astimezone(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'offset_h': 2.0,
        'youtube_id': None,
        'status': 'pendente',
        'media': [f'{remote_dir}/{mp4_local.name}'],
        'media_local': [str(mp4_local)],
        'cmd': ['file_reel', slug, parte],
        'criado_em': int(time.time()),
    }


def job_key(j):
    return (j['slug'], j['tipo'], j.get('parte'))


def main():
    import sincronizar

    print(f'=== agendar_instagram.py  DRY={DRY} ===')
    print(f'  plano: {len(PLANO)} entradas + 3 extras 48-leis')

    for ddmm, slug, tipo in PLANO:
        print(f'\n--- {ddmm}  {slug}  {tipo} ---')
        if tipo == 'reel':
            if not DRY:
                sincronizar.enqueue(slug, ddmm=ddmm, hhmm='17:00',
                                    offset_h=2.0, tipo='reel')
            else:
                print('  [dry] enqueue reel')
        elif tipo == 'carousel':
            local_dir = CARR / f'{slug}_overview'
            if not local_dir.exists():
                print(f'  [!] carrossel ausente localmente: {local_dir}')
                continue
            if not DRY:
                ok = scp_carousel_pngs(slug)
                if not ok:
                    continue
                sincronizar.enqueue(slug, ddmm=ddmm, hhmm='17:00',
                                    offset_h=2.0, tipo='carousel')
            else:
                pngs = list(local_dir.glob('[0-9][0-9].png'))
                print(f'  [dry] carousel: {len(pngs)} PNGs locais')
        elif tipo == 'story':
            story_dir = CARR / f'{slug}_stories'
            if not story_dir.exists():
                print(f'  [!] stories ausentes: {story_dir}')
                continue
            if not DRY:
                sincronizar.enqueue(slug, ddmm=ddmm, hhmm='17:00',
                                    offset_h=2.0, tipo='story')
            else:
                frames = list(story_dir.glob('[0-9][0-9].png'))
                print(f'  [dry] story: {len(frames)} frames locais')

    # Extras: Reels avulsos de 48-leis
    print('\n--- extras 48-leis-do-poder ---')
    jobs = load_manifest()
    existing_keys = {job_key(j) for j in jobs}
    for ddmm, parte in EXTRAS_48:
        slug = '48-leis-do-poder'
        print(f'  {ddmm}  {slug}  reel parte={parte}')
        k = (slug, 'reel', parte)
        if k in existing_keys:
            print('  já existe no manifesto; pulando')
            continue
        job = extra_reel_job(slug, parte, ddmm)
        if job and not DRY:
            jobs = load_manifest()  # recarrega caso sincronizar tenha adicionado
            existing_keys2 = {job_key(j) for j in jobs}
            if k not in existing_keys2:
                jobs.append(job)
                save_and_push(jobs)
                print(f'  enfileirado ({ddmm} parte={parte})')
        elif DRY:
            print(f'  [dry] reel extra parte={parte}')

    print(f'\n=== CONCLUIDO ===')
    print(f'  manifesto local: {MANIFEST}')
    if not DRY:
        jobs = load_manifest()
        pendentes = [j for j in jobs if j.get('status') == 'pendente']
        print(f'  total pendentes na fila: {len(pendentes)}')


if __name__ == '__main__':
    main()
