# -*- coding: utf-8 -*-
"""Calendário denso IG: 1 carrossel + 2 stories por dia, Jun/18 → Ago/09.

Lê o manifesto atual, descobre quais dias ainda precisam de carrossel e/ou
stories, e preenche com slugs do pool de 92 (cycling). Sobe mídias via SCP
antes de enfileirar cada job; push único do manifesto ao final.

Uso: python agendar_denso.py [--dry-run]
"""
import sys, json, time, subprocess
from datetime import datetime, timedelta, timezone, date
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

ROOT   = Path(__file__).parent
CARR   = ROOT / '_carrossel'
SYNC   = ROOT / '_sync'
MANIFEST = SYNC / 'sync_manifest.json'
VPS_HOST = 'root@andregalgani.com.br'
VPS_CARR = '/opt/minutoreal/_carrossel'
VPS_MAN  = '/opt/minutoreal/sync_manifest.json'
BRT  = timezone(timedelta(hours=-3))
DRY  = '--dry-run' in sys.argv or '--dry' in sys.argv

# Pool de slugs com overview + stories disponíveis
POOL = [
    '1984','21-licoes','48-leis-do-poder','7-habitos','admiravel-mundo-novo',
    'amor-liquido','antifragil','aristoteles-poetica','armas-da-persuasao',
    'arte-da-seducao','assim-falou-zaratustra','audiovisao','a-unica-coisa',
    'axiomas-de-zurique','busca-de-sentido','cabeca-bem-feita','cisne-negro',
    'coesao-coerencia','coisa-de-rico','comece-pelo-porque','como-fazer-amigos',
    'comunicacao-nao-violenta','conversas-cruciais','coragem-de-nao-agradar',
    'corpo-guarda-as-marcas','crime-e-castigo','design-do-dia-a-dia','de-zero-a-um',
    'dom-casmurro','do-mil-ao-milhao','escute','essencialismo','flow',
    'futebol-brasileiro','garra','gene-egoista','geracao-ansiosa','habitos-atomicos',
    'homem-mais-rico-babilonia','homo-deus','hora-da-estrela',
    'insustentavel-leveza-do-ser','inteligencia-emocional','investidor-inteligente',
    'irmaos-karamazov','jogos-da-vida','jornada-do-escritor','leis-da-natureza-humana',
    'mais-esperto-que-o-diabo','marketing-4-0','meditacoes','memorias-do-subsolo',
    'metamorfose','milionario-mora-ao-lado','mindset','mulheres-que-correm-com-os-lobos',
    'mundo-de-sofia','nacao-dopamina','nao-me-faca-pensar','noites-brancas',
    'nunca-divida-a-diferenca','o-alquimista','obrigado-pelo-feedback','o-idiota',
    'o-principe','padrao-bitcoin','pai-rico-pai-pobre','pensamento-complexo',
    'pequeno-principe','poder-de-delegar','poder-do-habito','poder-dos-quietos',
    'ponerologia','psicologia-financeira','psicopolitica','quatro-compromissos',
    'quebrando-o-habito','quem-mexeu-no-queijo','quem-pensa-enriquece','rapido-e-devagar',
    'realismo-capitalista','revolucao-dos-bichos','sapiens','save-the-cat',
    'segredos-da-mente-milionaria','sete-saberes','sociedade-do-cansaco','sound-design',
    'startup-enxuta','sutil-arte','trabalhe-4-horas','trabalho-focado',
]

START = date(2026, 6, 18)
END   = date(2026, 8, 9)   # inclusive


def load_manifest():
    return json.loads(MANIFEST.read_text(encoding='utf-8')) if MANIFEST.exists() else []


def save_manifest(jobs):
    SYNC.mkdir(exist_ok=True)
    MANIFEST.write_text(json.dumps(jobs, ensure_ascii=False, indent=1), encoding='utf-8')


def push_manifest():
    r = subprocess.run(['scp', '-q', str(MANIFEST), f'{VPS_HOST}:{VPS_MAN}'],
                       capture_output=True, text=True)
    if r.returncode == 0:
        print('  manifesto enviado para a VPS')
    else:
        print(f'  [!] push falhou: {r.stderr[:80]}')


def as_brt(d: date, h: int, m: int = 0):
    return datetime(d.year, d.month, d.day, h, m, tzinfo=BRT)


def make_job(slug, tipo, anchor_dt, offset_h=2.0):
    alvo = anchor_dt + timedelta(hours=offset_h)
    base = {
        'slug': slug, 'tipo': tipo,
        'anchor_brt': anchor_dt.strftime('%Y-%m-%dT%H:%M:%S%z'),
        'ig_alvo_brt': alvo.strftime('%Y-%m-%dT%H:%M:%S%z'),
        'ig_alvo_utc': alvo.astimezone(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'offset_h': offset_h, 'youtube_id': None,
        'status': 'pendente', 'criado_em': int(time.time()),
    }
    if tipo == 'carousel':
        base.update({'parte': 'overview', 'media': [], 'media_local': [],
                     'cmd': ['carousel', slug, 'overview']})
    else:  # story
        story_dir = CARR / f'{slug}_stories'
        pngs = sorted(story_dir.glob('[0-9][0-9].png'))
        remote_dir = f'{VPS_CARR}/{slug}_stories'
        base.update({'parte': 'stories',
                     'media': [f'{remote_dir}/{p.name}' for p in pngs],
                     'media_local': [str(p) for p in pngs],
                     'cmd': ['story', slug]})
    return base


def scp_carousel(slug):
    local = CARR / f'{slug}_overview'
    pngs = sorted(local.glob('[0-9][0-9].png'))
    if not pngs:
        return False
    remote = f'{VPS_CARR}/{slug}_overview'
    subprocess.run(['ssh', VPS_HOST, f'mkdir -p {remote}'], check=True, capture_output=True)
    for p in pngs:
        r = subprocess.run(['scp', '-q', str(p), f'{VPS_HOST}:{remote}/{p.name}'],
                           capture_output=True, text=True)
        if r.returncode != 0:
            print(f'    scp {p.name} falhou: {r.stderr[:60]}')
            return False
    return True


def scp_story(slug):
    local = CARR / f'{slug}_stories'
    pngs = sorted(local.glob('[0-9][0-9].png'))
    if not pngs:
        return False
    remote = f'{VPS_CARR}/{slug}_stories'
    subprocess.run(['ssh', VPS_HOST, f'mkdir -p {remote}'], check=True, capture_output=True)
    for p in pngs:
        r = subprocess.run(['scp', '-q', str(p), f'{VPS_HOST}:{remote}/{p.name}'],
                           capture_output=True, text=True)
        if r.returncode != 0:
            print(f'    scp {p.name} falhou: {r.stderr[:60]}')
            return False
    return True


def main():
    print(f'=== agendar_denso.py  DRY={DRY} ===')

    jobs = load_manifest()
    # Conjunto de chaves já agendadas (pendentes)
    scheduled = {(j['slug'], j['tipo']) for j in jobs if j.get('status') != 'publicado'}
    print(f'  jobs existentes no manifesto: {len(jobs)}')

    # Ciclos independentes para carousel e story
    # Prioridade editorial: temas de alto desempenho primeiro
    priority = ['48-leis-do-poder','poder-do-habito','o-alquimista','habitos-atomicos',
                'quem-pensa-enriquece','homem-mais-rico-babilonia','psicologia-financeira',
                'inteligencia-emocional','mindset','sapiens','homo-deus','cisne-negro',
                'antifragil','nacao-dopamina','geracao-ansiosa']
    others   = [s for s in POOL if s not in priority]
    full_pool = priority + others

    carr_pool   = [s for s in full_pool if (s, 'carousel') not in scheduled]
    story_pool  = [s for s in full_pool if (s, 'story')   not in scheduled]
    carr_idx  = 0
    s1_idx    = 0
    s2_idx    = len(story_pool) // 2  # começa no meio para diversificar

    new_jobs = []
    day = START
    while day <= END:
        day_scheduled = {(j['slug'], j['tipo'])
                         for j in jobs + new_jobs
                         if j.get('ig_alvo_brt', '').startswith(day.strftime('%Y-%m-%d'))}

        # ---- CAROUSEL ----
        has_carr = any(t == 'carousel' for _, t in day_scheduled)
        if not has_carr:
            while carr_idx < len(carr_pool):
                slug = carr_pool[carr_idx]; carr_idx += 1
                if (slug, 'carousel') not in {(j['slug'], j['tipo']) for j in jobs + new_jobs}:
                    anchor = as_brt(day, 17)
                    new_jobs.append(make_job(slug, 'carousel', anchor, 2.0))
                    break

        # ---- STORY 1 (19:30) ----
        story_count = sum(1 for _, t in day_scheduled if t == 'story')
        if story_count < 1:
            while s1_idx < len(story_pool):
                slug = story_pool[s1_idx]; s1_idx += 1
                if (slug, 'story') not in {(j['slug'], j['tipo']) for j in jobs + new_jobs}:
                    anchor = as_brt(day, 17, 30)
                    new_jobs.append(make_job(slug, 'story', anchor, 2.0))
                    break

        # ---- STORY 2 (21:00) ----
        story_count = sum(1 for _, t in day_scheduled if t == 'story') + \
                      sum(1 for j in new_jobs
                          if j.get('ig_alvo_brt','').startswith(day.strftime('%Y-%m-%d'))
                          and j['tipo'] == 'story')
        if story_count < 2:
            while s2_idx != s1_idx and s2_idx < len(story_pool):
                slug = story_pool[s2_idx % len(story_pool)]; s2_idx += 1
                if (slug, 'story') not in {(j['slug'], j['tipo']) for j in jobs + new_jobs}:
                    anchor = as_brt(day, 19)
                    new_jobs.append(make_job(slug, 'story', anchor, 2.0))
                    break

        day += timedelta(days=1)

    print(f'  novos jobs a adicionar: {len(new_jobs)}')

    if DRY:
        for j in new_jobs:
            print(f'  [dry] {j["ig_alvo_brt"][:10]}  {j["slug"]:30} {j["tipo"]}')
        return

    # Upload e enqueue
    ok = 0
    for i, job in enumerate(new_jobs, 1):
        slug, tipo = job['slug'], job['tipo']
        print(f'  [{i:03}/{len(new_jobs)}] {job["ig_alvo_brt"][:10]} {slug} {tipo}')
        if tipo == 'carousel':
            if not scp_carousel(slug):
                print(f'    SCP falhou; pulando')
                continue
        else:
            if not scp_story(slug):
                print(f'    SCP falhou; pulando')
                continue
        jobs.append(job)
        ok += 1

    save_manifest(jobs)
    push_manifest()
    print(f'\n=== CONCLUIDO: {ok} novos jobs adicionados — total no manifesto: {len(jobs)} ===')


if __name__ == '__main__':
    main()
