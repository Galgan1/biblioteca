# -*- coding: utf-8 -*-
"""Regenera story PNGs com 4 frames e atualiza manifesto.

Para cada slug com story pendente no manifesto:
  1. Roda gerar_carrossel.py {slug} --stories  (gera 4 frames: teaser+quote+insights+CTA)
  2. SCP do 04.png novo para a VPS
  3. Atualiza media/media_local no manifesto para incluir 04.png
  4. Push do manifesto para a VPS ao final

Uso: python regen_stories_4frame.py [--dry-run]
"""
import sys, json, subprocess, time
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

ROOT       = Path(__file__).parent.parent           # biblioteca/
VIDEOS     = Path(__file__).parent                  # biblioteca/videos/
CARR       = VIDEOS / '_carrossel'
MANIFEST   = VIDEOS / '_sync' / 'sync_manifest.json'
GC         = ROOT / 'gerar_carrossel.py'
VPS_HOST   = 'root@andregalgani.com.br'
VPS_CARR   = '/opt/minutoreal/_carrossel'
VPS_MAN    = '/opt/minutoreal/sync_manifest.json'
DRY        = '--dry-run' in sys.argv or '--dry' in sys.argv


def load_manifest():
    return json.loads(MANIFEST.read_text(encoding='utf-8'))


def save_manifest(jobs):
    MANIFEST.write_text(json.dumps(jobs, ensure_ascii=False, indent=1), encoding='utf-8')


def push_manifest():
    r = subprocess.run(['scp', '-q', str(MANIFEST), f'{VPS_HOST}:{VPS_MAN}'],
                       capture_output=True, text=True)
    if r.returncode == 0:
        print('  manifesto enviado para a VPS')
    else:
        print(f'  [!] push manifesto falhou: {r.stderr[:80]}')


def scp_file(local: Path, remote: str) -> bool:
    r = subprocess.run(['scp', '-q', str(local), f'{VPS_HOST}:{remote}'],
                       capture_output=True, text=True)
    return r.returncode == 0


def regen_stories(slug: str) -> bool:
    """Roda gerar_carrossel.py {slug} --stories. Retorna True se 04.png foi gerado."""
    r = subprocess.run(
        [sys.executable, str(GC), slug, '--stories'],
        capture_output=True, text=True, cwd=str(ROOT)
    )
    if r.returncode != 0:
        print(f'    [!] gerar_carrossel falhou:\n{r.stderr[-300:]}')
        return False
    out_dir = CARR / f'{slug}_stories'
    if not (out_dir / '04.png').exists():
        print(f'    [!] 04.png nao gerado para {slug}')
        return False
    return True


def update_job_media(job: dict, slug: str) -> bool:
    """Adiciona 04.png ao job se ele tiver apenas 3 mídias. Retorna True se mudou."""
    if job['tipo'] != 'story' or job['slug'] != slug:
        return False
    if job.get('status') == 'publicado':
        return False
    media = job.get('media', [])
    if len(media) >= 4:
        return False  # já tem 4 frames
    remote_dir = f'{VPS_CARR}/{slug}_stories'
    remote_04 = f'{remote_dir}/04.png'
    local_04 = str(CARR / f'{slug}_stories' / '04.png')
    if remote_04 not in media:
        job['media'].append(remote_04)
    if local_04 not in job.get('media_local', []):
        if 'media_local' not in job:
            job['media_local'] = []
        job['media_local'].append(local_04)
    return True


def main():
    print(f'=== regen_stories_4frame.py  DRY={DRY} ===')

    jobs = load_manifest()
    # Slugs únicos com story pendente
    slugs = list(dict.fromkeys(
        j['slug'] for j in jobs
        if j['tipo'] == 'story' and j.get('status') != 'publicado'
    ))
    print(f'  Slugs com story pendente: {len(slugs)}')

    ok = 0
    skip = 0
    fail = 0

    for i, slug in enumerate(slugs, 1):
        out_dir = CARR / f'{slug}_stories'
        already_has_4 = (out_dir / '04.png').exists() and \
                        len(list(out_dir.glob('[0-9][0-9].png'))) >= 4

        print(f'  [{i:03}/{len(slugs)}] {slug}', end='', flush=True)

        if DRY:
            print(f'  [dry] {"ok" if already_has_4 else "regen"}')
            continue

        if not already_has_4:
            print('  → gerando...', end='', flush=True)
            if not regen_stories(slug):
                print('  FAIL')
                fail += 1
                continue
            print('  ✓', end='', flush=True)
        else:
            print('  (já tem 4 frames)', end='', flush=True)

        # SCP do 04.png para VPS
        local_04 = out_dir / '04.png'
        remote_dir = f'{VPS_CARR}/{slug}_stories'
        # garantir que diretório existe na VPS
        subprocess.run(['ssh', VPS_HOST, f'mkdir -p {remote_dir}'],
                       capture_output=True)
        if not scp_file(local_04, f'{remote_dir}/04.png'):
            print('  [!] scp 04.png falhou')
            fail += 1
            continue

        # Atualizar manifesto
        changed = False
        for job in jobs:
            if update_job_media(job, slug):
                changed = True

        if changed:
            print('  → manifesto atualizado')
        else:
            print('  (manifesto já OK)')
        ok += 1

    if not DRY:
        save_manifest(jobs)
        push_manifest()

    print(f'\n=== CONCLUIDO: {ok} OK, {skip} skip, {fail} falhas ===')


if __name__ == '__main__':
    main()
