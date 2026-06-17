# -*- coding: utf-8 -*-
"""vp100 — simulador local (dry-run NARRADO) do pipeline Minuto Real / Biblioteca.

NÃO executa nada real: zero upload, zero deploy, zero chamada de API. Lê a
definição REAL do projeto e ENCENA o que cada etapa faria, na tela.

Fontes de verdade lidas:
  videos/dag.py            ordem das etapas (fan-out paralelo)
  videos/canal-state.json  lanes (ativa/bloqueada), agenda, pendências, breakers
  videos/cost_tracker.py   preços (custo simulado)
  books.json               catálogo (valida o slug)

Uso:
  vp100 publicar <lane> <full|slug>   simula a publicação numa lane
  vp100 pipeline <slug>               o livro inteiro (todas as lanes, ordem do dag)
  vp100 agentes                       lista os agentes/lanes atuais (derivado do real)
  vp100 bibliotecario [livros [slug]] perfil do agente · tabela de livros · status de 1 livro
  vp100 status                        lanes, agenda, pendências, circuit breakers
  vp100 dag                           grafo de dependências + grupos paralelos
  vp100 mapa                          esqueleto REAL: stage→script, divergências e órfãos
  vp100 custo <slug>                  custo simulado (PRICES reais)
  vp100 doctor                        sanidade do ambiente simulado
  vp100 update                        (re)instala o atalho 'vp100' no terminal e mostra como ativar
  vp100 ajuda

Flags: --speed fast|real  --verbose  --seed N  --no-color  --json
"""
import argparse
import importlib.util
import json
import re
import sys
import time
from pathlib import Path

# ---------------------------------------------------------------------------
# CONSTANTS
# ---------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parent
VIDEOS = ROOT / 'videos'

DAG_FILE = VIDEOS / 'dag.py'
COST_TRACKER_FILE = VIDEOS / 'cost_tracker.py'
CANAL_STATE_FILE = VIDEOS / 'canal-state.json'
ORQUESTRADOR_FILE = VIDEOS / 'orquestrador.py'

BOOKS_FILE = ROOT / 'books.json'
CLAUDE_MD_FILE = ROOT / 'CLAUDE.md'
BIBLIOTECA_MD_FILE = ROOT / 'biblioteca.md'
REQUIREMENTS_FILE = ROOT / 'requirements.txt'
VP100_FILE = ROOT / 'vp100.py'
WORKTREES_DIR = ROOT / '.claude' / 'worktrees'

DEFAULT_CHANNEL_NAME = 'Minuto Real'
DEFAULT_FALLBACK_SLUG = 'padrao-bitcoin'

DEFAULT_DAG = {
    'skill': [], 'biblioteca': ['skill'], 'video_built': ['skill'],
    'uploaded': ['video_built'], 'shorts': ['uploaded'], 'scheduled': ['shorts'],
    'instagram': ['skill'], 'tiktok': ['shorts'], 'facebook': ['uploaded'],
}

DEFAULT_PRICES = {
    'google_imagen': 0.04, 'google_veo_8s': 1.20, 'google_tts_1k': 0.016,
    'youtube_upload': 0.0, 'instagram_api': 0.0
}

EXPECTED_SCRIPTS = [
    'videos/gerar_video.py', 'gerar_carrossel.py', 'videos/instagram_post.py',
    'videos/upload_youtube.py', 'publicar_livro.py', 'videos/dag.py',
    'videos/cost_tracker.py', 'books.json'
]

ENTRYPOINT_SEEDS = {'orquestrador', 'publicar_livro', 'gerar_metadados', 'coletar_datas'}

# ---------------------------------------------------------------------------
# Cores ANSI (desligam fora de terminal ou com --no-color)
# ---------------------------------------------------------------------------
class Paint:
    def __init__(self, on):
        self.on = on

    def _w(self, s, c):
        return f'\033[{c}m{s}\033[0m' if self.on else s

    def green(self, s): return self._w(s, '32')
    def gold(self, s): return self._w(s, '33')
    def red(self, s): return self._w(s, '31')
    def dim(self, s): return self._w(s, '2')
    def bold(self, s): return self._w(s, '1')
    def cyan(self, s): return self._w(s, '36')


# ---------------------------------------------------------------------------
# Leitura das fontes de verdade (com fallback gracioso)
# ---------------------------------------------------------------------------
def _import(nome, caminho):
    try:
        spec = importlib.util.spec_from_file_location(nome, caminho)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod
    except Exception:
        return None


def carregar_dag():
    mod = _import('dag', DAG_FILE)
    if mod and hasattr(mod, 'DAG'):
        return mod.DAG, mod.topological_sort, mod.parallel_groups
    dag = DEFAULT_DAG
    def topo(d):
        ind = {s: len(v) for s, v in d.items()}
        q, out = sorted([s for s, n in ind.items() if n == 0]), []
        while q:
            n = q.pop(0); out.append(n)
            for s, deps in d.items():
                if n in deps:
                    ind[s] -= 1
                    if ind[s] == 0:
                        q.append(s); q.sort()
        return out
    def groups(d):
        rem, done, gs = set(d), set(), []
        while rem:
            g = {s for s in rem if all(x in done for x in d[s])}
            if not g:
                break
            gs.append(g); done |= g; rem -= g
        return gs
    return dag, topo, groups


def carregar_precos():
    mod = _import('cost_tracker', COST_TRACKER_FILE)
    if mod and hasattr(mod, 'PRICES'):
        return mod.PRICES
    return DEFAULT_PRICES


def carregar_json(caminho, default):
    try:
        return json.loads(Path(caminho).read_text(encoding='utf-8', errors='replace'))
    except Exception:
        return default


# ---------------------------------------------------------------------------
# Manifesto das etapas (a narração de cada stage)  ·  seg = tempo SIMULADO
# ---------------------------------------------------------------------------
STAGE_LANE = {
    'skill': None, 'biblioteca': 'biblioteca', 'video_built': 'youtube',
    'uploaded': 'youtube', 'shorts': 'youtube', 'scheduled': 'youtube',
    'instagram': 'instagram', 'tiktok': 'tiktok', 'facebook': 'facebook',
}

STEPS = {
    'skill':       dict(label='skill',      script='book-to-skill',
                        produz='base de conhecimento destilada', seg=8,
                        subs=['ler livro/PDF', 'extrair capítulos', 'validar taxonomia']),
    'biblioteca':  dict(label='biblioteca', script='publicar_livro.py --deploy',
                        produz='<slug>.html + capítulos + deploy VPS', seg=60,
                        subs=['gerar_livro.py (páginas)', 'gerar_capa', 'retrofit-fase23', 'scp + chmod (VPS)']),
    'video_built': dict(label='vídeo',      script='gerar_video.py',
                        produz='videos/<slug>.mp4 (~5min)', seg=240,
                        subs=['roteiro.json', 'TTS pt-BR', 'slides Pillow', 'trilha + marca sonora', 'montagem ffmpeg']),
    'uploaded':    dict(label='upload YT',  script='upload_youtube.py',
                        produz='vídeo no canal (unlisted)', seg=120,
                        subs=['OAuth token', 'upload resumable', 'metadados + thumb']),
    'shorts':      dict(label='shorts',     script='produzir_shorts.py',
                        produz='4 shorts 9:16', seg=180,
                        subs=['cortar cenas', 'legendar', 'render 1080×1920']),
    'scheduled':   dict(label='agendar',    script='agendar_lote.py',
                        produz='posts agendados (qua/qui)', seg=12,
                        subs=['calcular slots', 'setPublishAt']),
    'instagram':   dict(label='instagram',  script='gerar_carrossel.py',
                        produz='carrossel no @minutoreal1701', seg=38,
                        subs=['gerar_carrossel (7 cards)', 'legenda 5 As + disclosure',
                              'post manual via instagram_post.py (fora do orquestrador)']),
    'tiktok':      dict(label='tiktok',     script='tiktok_post.py --draft',
                        produz='RASCUNHO no TikTok', seg=30,
                        subs=['refresh token', 'upload draft']),
    'facebook':    dict(label='facebook',   script='facebook_publicar.py',
                        produz='vídeo nativo + link no 1º comentário', seg=25,
                        subs=['reusar ativo do IG', 'publicar nativo', 'comentar CTA (link)']),
}

LANE_TERMINAL = {
    'instagram': 'instagram', 'youtube': 'scheduled', 'facebook': 'facebook',
    'tiktok': 'tiktok', 'biblioteca': 'biblioteca',
}


def custo_etapa(stage, p):
    if stage == 'video_built':
        return p['google_tts_1k'] * 4 + p['google_imagen'] * 8 + p['google_veo_8s'] * 3
    if stage == 'shorts':
        return p['google_tts_1k'] * 1
    return 0.0


def fmt_tempo(seg):
    seg = int(round(seg))
    return f'{seg // 60}m{seg % 60:02d}s' if seg >= 60 else f'{seg}s'


# ---------------------------------------------------------------------------
# Encenação (animação)
# ---------------------------------------------------------------------------
SPIN = '⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏'


class Tela:
    def __init__(self, paint, animar):
        self.p = paint
        self.animar = animar

    def passo(self, prefixo, rotulo, dur, resumo, marca=''):
        linha = f'{prefixo}{rotulo} '.ljust(40, '.')
        if self.animar and dur > 0:
            t0, k = time.time(), 0
            while time.time() - t0 < dur:
                sys.stdout.write('\r' + linha + ' ' + self.p.gold(SPIN[k % len(SPIN)]))
                sys.stdout.flush(); time.sleep(0.08); k += 1
        extra = self.p.dim(' ' + marca) if marca else ''
        sys.stdout.write('\r' + linha + ' ' + self.p.green('✓') + ' ' + self.p.dim(resumo) + extra + '\n')
        sys.stdout.flush()


# ---------------------------------------------------------------------------
# Contexto (tudo lido das fontes reais)
# ---------------------------------------------------------------------------
class Ctx:
    def __init__(self, args):
        self.p = Paint(on=(not args.no_color) and sys.stdout.isatty())
        self.animar = (args.speed != 'fast') and sys.stdout.isatty()
        self.verbose = args.verbose
        self.json = args.json
        self.tela = Tela(self.p, self.animar)
        self.dag, self.topo, self.groups = carregar_dag()
        self.precos = carregar_precos()
        self.estado = carregar_json(CANAL_STATE_FILE, {'lanes': {}})
        self.books = carregar_json(BOOKS_FILE, [])

    def banner(self, titulo, modo='leitura'):
        canal = self.estado.get('channel_name', DEFAULT_CHANNEL_NAME)
        sub = ('· SIMULAÇÃO (dry-run — nada é executado)' if modo == 'sim'
               else '· leitura do real (diagnóstico — nada é alterado)')
        print(self.p.bold(self.p.green('▶ ' + canal)) + '  ' + self.p.dim(sub))
        if titulo:
            print('  ' + titulo)
        print()

    def resolver_slug(self, escopo):
        ids = [b.get('id') for b in self.books if b.get('id')]
        if escopo and escopo != 'full':
            if ids and escopo not in ids:
                print(self.p.gold(f'  ⚠ "{escopo}" não está no books.json — simulando assim mesmo.\n'))
            return escopo
        prox = self.estado.get('upcoming_schedule') or []
        if prox and prox[0].get('slug'):
            return prox[0]['slug']
        return ids[0] if ids else DEFAULT_FALLBACK_SLUG

    def stages_da_lane(self, lane):
        alvo = LANE_TERMINAL.get(lane)
        if not alvo:
            return []
        vis = set()

        def dfs(s):
            if s in vis:
                return
            for d in self.dag.get(s, []):
                dfs(d)
            vis.add(s)
        dfs(alvo)
        return [s for s in self.topo(self.dag) if s in vis]


# ---------------------------------------------------------------------------
# Comandos
# ---------------------------------------------------------------------------
def _proximo(ctx):
    prox = ctx.estado.get('upcoming_schedule') or []
    if prox:
        it = prox[0]
        print('  ' + ctx.p.dim('↪ próximo na agenda: ') + f"{it.get('slug', '?')} · {it.get('longo_date', '?')}")


def cmd_publicar(ctx, lane, escopo):
    if lane not in LANE_TERMINAL:
        print(ctx.p.red(f'lane desconhecida: {lane}. Use: ' + ', '.join(LANE_TERMINAL)))
        return 2
    slug = ctx.resolver_slug(escopo)
    info = ctx.estado.get('lanes', {}).get(lane, {})
    conta = info.get('account', '')
    ctx.banner(f'lane: {ctx.p.cyan(lane)}' + (f' · {conta}' if conta else '') + f' · livro: {ctx.p.bold(slug)}', 'sim')
    if info.get('status') == 'blocked':
        print(ctx.p.gold(f'  ⚠ lane BLOQUEADA ({info.get("reason", "?")}) — simulando o fluxo mesmo assim.\n'))

    stages = ctx.stages_da_lane(lane)
    terminal = LANE_TERMINAL[lane]
    total = len(stages)
    custo = 0.0
    for i, st in enumerate(stages, 1):
        m = STEPS[st]
        custo += custo_etapa(st, ctx.precos)
        marca = m['script'] if ctx.verbose else ''
        ctx.tela.passo(f'  [{i}/{total}] ', m['label'], min(m['seg'] * 0.01, 1.0), m['produz'], marca)
        if st == terminal:  # detalha os sub-passos da etapa-fim da lane
            subs = m['subs']
            for j, sub in enumerate(subs):
                rede = ' (SIMULADO)' if any(k in sub for k in ('container', 'publish', 'upload', 'permalink', 'comentar')) else ''
                ctx.tela.passo('        · ', sub, 0.3, ('ok' + rede) if rede else 'ok')
    seg = sum(STEPS[s]['seg'] for s in stages)
    print()
    print('  ' + ctx.p.green('✓ publicado (simulado)') + '  ·  custo US$ %.2f  ·  tempo simulado ~%s' % (custo, fmt_tempo(seg)))
    _proximo(ctx)
    return 0


def cmd_pipeline(ctx, slug):
    slug = ctx.resolver_slug(slug)
    ativas = [ln for ln, v in ctx.estado.get('lanes', {}).items() if v.get('status') == 'active']
    ctx.banner(f'pipeline COMPLETO · livro: {ctx.p.bold(slug)} · lanes ativas: {ctx.p.cyan(", ".join(ativas) or "—")}', 'sim')
    ordem = ctx.topo(ctx.dag)
    custo = 0.0
    for gi, grupo in enumerate(ctx.groups(ctx.dag), 1):
        gstages = [s for s in ordem if s in grupo]
        print(ctx.p.dim(f'  grupo {gi} (paralelo): ') + ', '.join(STEPS[s]['label'] for s in gstages))
        for st in gstages:
            lane = STAGE_LANE.get(st)
            if lane and lane not in ativas and lane != 'biblioteca':
                ctx.tela.passo('    ', STEPS[st]['label'], 0.0, ctx.p.gold('pulado (lane inativa)') if False else 'pulado (lane inativa)')
                continue
            custo += custo_etapa(st, ctx.precos)
            marca = STEPS[st]['script'] if ctx.verbose else ''
            ctx.tela.passo('    ', STEPS[st]['label'], min(STEPS[st]['seg'] * 0.008, 0.9), STEPS[st]['produz'], marca)
    seg = sum(STEPS[s]['seg'] for s in ordem)
    print()
    print('  ' + ctx.p.green('✓ pipeline simulado') + '  ·  custo US$ %.2f  ·  tempo simulado ~%s' % (custo, fmt_tempo(seg)))
    return 0


def cmd_status(ctx):
    e = ctx.estado
    if ctx.json:
        print(json.dumps({'lanes': e.get('lanes'), 'agenda': e.get('schedule_cadence'),
                          'upcoming': e.get('upcoming_schedule'), 'pending': e.get('pending_operations'),
                          'api_health': e.get('api_health')}, ensure_ascii=False, indent=2))
        return 0
    ctx.banner('status do canal (lido de canal-state.json)')
    print(ctx.p.bold('  Lanes'))
    for ln, v in e.get('lanes', {}).items():
        st = v.get('status', '?')
        cor = ctx.p.green if st == 'active' else ctx.p.red
        extra = ' — ' + v.get('reason', '') if v.get('reason') else (' · ' + v.get('account', '') if v.get('account') else '')
        print(f'    {cor("●")} {ln:<11} {cor(st)}{ctx.p.dim(extra)}')
    prox = e.get('upcoming_schedule') or []
    if prox:
        print(ctx.p.bold('\n  Próximos longos'))
        for it in prox[:5]:
            print(f'    {ctx.p.gold("›")} {it.get("slug","?"):<16} {ctx.p.dim(str(it.get("longo_date","?")))}')
    pend = e.get('pending_operations') or {}
    if pend:
        print(ctx.p.bold('\n  Pendências'))
        for k, v in pend.items():
            print(f'    {ctx.p.gold("•")} {k} {ctx.p.dim("— " + str(v.get("note", ""))[:70])}')
    ah = e.get('api_health') or {}
    abertos = [k for k, v in ah.items() if v.get('state') != 'closed']
    print(ctx.p.bold('\n  Circuit breakers'))
    print('    ' + (ctx.p.red('ABERTOS: ' + ', '.join(abertos)) if abertos else ctx.p.green('todos fechados (saudáveis)')))
    return 0


def cmd_dag(ctx):
    ordem = ctx.topo(ctx.dag)
    if ctx.json:
        print(json.dumps({'ordem': ordem, 'grupos': [sorted(g) for g in ctx.groups(ctx.dag)]}, ensure_ascii=False, indent=2))
        return 0
    ctx.banner('grafo de dependências (videos/dag.py)')
    print(ctx.p.bold('  Ordem topológica'))
    print('    ' + ctx.p.dim(' → ').join(STEPS.get(s, {}).get('label', s) for s in ordem))
    print(ctx.p.bold('\n  Grupos paralelos'))
    for i, g in enumerate(ctx.groups(ctx.dag), 1):
        print(f'    {i}. ' + ', '.join(sorted(STEPS.get(s, {}).get('label', s) for s in g)))
    return 0


def cmd_custo(ctx, slug):
    slug = ctx.resolver_slug(slug)
    p = ctx.precos
    linhas = [(STEPS[s]['label'], custo_etapa(s, p)) for s in ctx.topo(ctx.dag) if custo_etapa(s, p) > 0]
    total = sum(c for _, c in linhas)
    if ctx.json:
        print(json.dumps({'slug': slug, 'itens': linhas, 'total_usd': round(total, 4)}, ensure_ascii=False, indent=2))
        return 0
    ctx.banner(f'custo simulado · livro: {ctx.p.bold(slug)} ' + ctx.p.dim('(estimativa, preços de cost_tracker.py)'))
    for nome, c in linhas:
        print(f'    {nome:<12} US$ %.2f' % c)
    print(ctx.p.dim('    ' + '-' * 22))
    print('    ' + ctx.p.bold('TOTAL') + '        US$ %.2f' % total)
    print(ctx.p.dim('    (carrossel/IG e site = US$0 — geração local)'))
    return 0


def cmd_doctor(ctx):
    ctx.banner('sanidade do ambiente (vp100 doctor)')
    checks = []
    scripts = EXPECTED_SCRIPTS
    for rel in scripts:
        checks.append((rel, (ROOT / rel).exists()))
    ok_estado = bool(ctx.estado.get('lanes'))
    checks.append(('videos/canal-state.json (válido)', ok_estado))
    checks.append((REQUIREMENTS_FILE.name, REQUIREMENTS_FILE.exists()))
    for nome, ok in checks:
        mark = ctx.p.green('✓') if ok else ctx.p.red('✗')
        print(f'    {mark} {nome}')
    nbooks = len(ctx.books)
    lanes = ctx.estado.get('lanes', {})
    ativas = sum(1 for v in lanes.values() if v.get('status') == 'active')
    print(ctx.p.dim(f'\n    catálogo: {nbooks} livros · lanes ativas: {ativas}/{len(lanes)}'))
    faltando = [n for n, ok in checks if not ok]
    print('    ' + (ctx.p.green('ambiente OK') if not faltando else ctx.p.gold('faltando: ' + ', '.join(faltando))))
    return 0


def cmd_agentes(ctx):
    """Lista os agentes ATUAIS — derivado do real (canal-state.json + CLAUDE.md + worktrees)."""
    lanes = ctx.estado.get('lanes', {})
    # governança: GitGuy declarado no CLAUDE.md do projeto
    gitguy = False
    try:
        gitguy = 'gitguy' in CLAUDE_MD_FILE.read_text(encoding='utf-8', errors='replace').lower()
    except Exception:
        pass
    # sessões de agente vivas no disco (worktrees do harness)
    wt = []
    wtdir = WORKTREES_DIR
    if wtdir.exists():
        wt = sorted(d.name for d in wtdir.iterdir() if d.is_dir() and d.name.startswith('agent-'))

    if ctx.json:
        print(json.dumps({
            'lanes': {k: {'status': v.get('status'), 'agent': v.get('agent'),
                          'account': v.get('account')} for k, v in lanes.items()},
            'gitguy': gitguy, 'worktrees_vivos': wt,
        }, ensure_ascii=False, indent=2))
        return 0

    ctx.banner('agentes ' + ctx.p.dim('(derivado de canal-state.json + CLAUDE.md + git worktree)'))
    print(ctx.p.bold('  Lanes operacionais') + ctx.p.dim('  · canal-state.json'))
    sem_agente = 0
    for ln, v in lanes.items():
        ativo = v.get('status') == 'active'
        bola = ctx.p.green('●') if ativo else ctx.p.red('○')
        ag = v.get('agent')
        if ag:
            agtxt = ctx.p.cyan(ag)
        else:
            agtxt = ctx.p.gold('— não nomeado')
            sem_agente += 1
        acct = ctx.p.dim(' · ' + v['account']) if v.get('account') else ''
        print(f'    {bola} {ln:<11} {v.get("status", ""):<8} agente: {agtxt}{acct}')

    print(ctx.p.bold('\n  Governança') + ctx.p.dim('  · biblioteca/CLAUDE.md'))
    print('    ' + (ctx.p.cyan('⬢ GitGuy') + ctx.p.dim(' — único autorizado a commit / push / criar PR')
                    if gitguy else ctx.p.dim('(nenhuma regra de versionamento detectada)')))

    print(ctx.p.bold('\n  Sessões de agente vivas') + ctx.p.dim('  · .claude/worktrees'))
    if wt:
        for w in wt:
            print('    ' + ctx.p.gold('•') + ' ' + w)
    else:
        print('    ' + ctx.p.dim('nenhuma'))

    if sem_agente:
        print('\n  ' + ctx.p.gold(f'⚠ achado: {sem_agente}/{len(lanes)} lanes sem campo "agent" no '
                                  'canal-state.json — fonte de verdade incompleta.'))
    return 0


def _bk(ctx, slug):
    return next((b for b in ctx.books if b.get('id') == slug), None)


def _pagina(b, slug):
    return ROOT / ((b or {}).get('url') or f'{slug}.html')


def _capitulos(slug):
    d = ROOT / slug
    return len(list(d.glob('*.html'))) if d.is_dir() else 0


def _data_py(slug):
    return ROOT / (slug.replace('-', '_') + '_data.py')


def _tem_capa(b):
    cu = (b or {}).get('coverUrl')
    return bool(cu) and (ROOT / cu).exists()


def cmd_bibliotecario(ctx, rest):
    sub = rest[0] if rest else None
    if sub == 'livros':
        return _bib_livro(ctx, rest[1]) if len(rest) > 1 else _bib_tabela(ctx)
    if sub:
        print(ctx.p.red(f'opção desconhecida: bibliotecario {sub}  ·  use: livros [<slug>]'))
        return 2
    return _bib_perfil(ctx)


def _bib_perfil(ctx):
    books = ctx.books
    no_disco = sum(1 for b in books if _pagina(b, b['id']).exists())
    com_data = sum(1 for b in books if _data_py(b['id']).exists())
    com_capa = sum(1 for b in books if _tem_capa(b))
    com_amz = sum(1 for b in books if b.get('amazon'))
    lane = ctx.estado.get('lanes', {}).get('biblioteca', {})
    desc = ''
    try:
        for ln in BIBLIOTECA_MD_FILE.read_text(encoding='utf-8', errors='replace').splitlines():
            if 'Bibliotecario' in ln and 'respons' in ln.lower():
                desc = ln.lstrip('> *').strip().replace('**', ''); break
    except Exception:
        pass
    if ctx.json:
        print(json.dumps({'agente': 'Bibliotecario', 'lane': 'biblioteca', 'status': lane.get('status'),
                          'catalogo': len(books), 'paginas_disco': no_disco, 'com_data': com_data,
                          'com_capa': com_capa, 'com_amazon': com_amz}, ensure_ascii=False, indent=2))
        return 0
    ctx.banner('agente: ' + ctx.p.cyan('Bibliotecario') + ctx.p.dim('  (leitura do real)'))
    print(ctx.p.bold('  Função') + ctx.p.dim('  · biblioteca.md'))
    print('    ' + (desc or 'responsável pelo site /biblioteca — estética, páginas, PDF, afiliados, SEO, deploy'))
    st = lane.get('status', '?')
    print('    lane: ' + ctx.p.cyan('biblioteca') + ' · ' + (ctx.p.green(st) if st == 'active' else ctx.p.red(st)))
    print(ctx.p.bold('\n  Acervo') + ctx.p.dim('  · books.json + disco'))
    n = len(books)
    print(f'    catálogo ............ {n}')
    print(f'    páginas no disco .... {no_disco}' + (ctx.p.gold(f'  (faltam {n - no_disco})') if no_disco < n else ''))
    print(f'    com fonte _data.py .. {com_data}' + (ctx.p.gold(f'  (faltam {n - com_data})') if com_data < n else ''))
    print(f'    com capa ............ {com_capa}' + (ctx.p.gold(f'  (faltam {n - com_capa})') if com_capa < n else ''))
    print(f'    com link Amazon ..... {com_amz}' + (ctx.p.gold(f'  ⚠ só {com_amz}/{n} monetizados') if com_amz < n else ''))
    print(ctx.p.bold('\n  Opções'))
    print('    ' + ctx.p.dim('vp100 bibliotecario livros') + '          tabela de todos os livros')
    print('    ' + ctx.p.dim('vp100 bibliotecario livros <slug>') + '   status de um livro')
    return 0


def _bib_tabela(ctx):
    books = sorted(ctx.books, key=lambda b: b.get('title', '').lower())
    if ctx.json:
        print(json.dumps([{'id': b['id'], 'pagina': _pagina(b, b['id']).exists(),
                           'caps': _capitulos(b['id']), 'data': _data_py(b['id']).exists(),
                           'capa': _tem_capa(b), 'amazon': bool(b.get('amazon'))} for b in books],
                         ensure_ascii=False))
        return 0
    ctx.banner('Bibliotecario · livros ' + ctx.p.dim(f'({len(books)} no books.json)'))
    print(ctx.p.dim('   pág  livro                                   cap  capa data amz'))
    for b in books:
        slug = b['id']
        pg = ctx.p.green('✓') if _pagina(b, slug).exists() else ctx.p.red('✗')
        cap = _capitulos(slug)
        capa = '✓' if _tem_capa(b) else ctx.p.gold('·')
        dat = '✓' if _data_py(slug).exists() else ctx.p.gold('·')
        amz = '✓' if b.get('amazon') else ctx.p.dim('·')
        print(f'    {pg}   {b.get("title", "")[:38].ljust(38)} {str(cap or "·"):>3}  {capa:>3} {dat:>3} {amz:>3}')
    print(ctx.p.dim('\n  pág ✓=página no disco · cap=nº de .html · data=fonte _data.py · amz=link Amazon'))
    return 0


def _bib_livro(ctx, slug):
    b = _bk(ctx, slug)
    pagina, caps, data = _pagina(b, slug), _capitulos(slug), _data_py(slug)
    if ctx.json:
        print(json.dumps({'slug': slug, 'no_catalogo': bool(b), 'titulo': b.get('title') if b else None,
                          'pagina': pagina.exists(), 'capitulos': caps, 'fonte_data': data.exists(),
                          'capa': _tem_capa(b), 'amazon': bool(b and b.get('amazon'))},
                         ensure_ascii=False, indent=2))
        return 0
    ctx.banner('Bibliotecario · livro: ' + ctx.p.bold(slug))
    if not b:
        print('  ' + ctx.p.red('não está no books.json') + ctx.p.dim(' — checando o disco mesmo assim'))
    else:
        print(f'    título ...... {b.get("title", "?")} · {ctx.p.dim(b.get("author", "?"))}')
        print(f'    progresso ... {ctx.p.dim(b.get("progress", "—"))}')
        print(f'    tags ........ {ctx.p.dim(", ".join(b.get("tags", []) or ["—"]))}')

    def linha(rot, ok, det=''):
        m = ctx.p.green('✓') if ok else ctx.p.red('✗')
        return f'    {rot:<13} {m}' + (ctx.p.dim('  ' + det) if det else '')
    print(linha('página', pagina.exists(), pagina.name))
    print(linha('capítulos', caps > 0, f'{caps} .html em {slug}/'))
    print(linha('fonte _data', data.exists(), data.name))
    print(linha('capa', _tem_capa(b), (b.get('coverUrl') if b else '')))
    print(linha('amazon', bool(b and b.get('amazon')), ((b.get('amazon') or '')[:48] if b else '')))
    probs = []
    if pagina.exists() and not data.exists():
        probs.append('página sem _data.py (fonte)')
    if b and not _tem_capa(b):
        probs.append('sem capa no disco')
    if b and not b.get('amazon'):
        probs.append('sem link Amazon (não monetizado)')
    if probs:
        print('\n  ' + ctx.p.gold('⚠ ' + ' · '.join(probs)))
    return 0


def _refs(p):
    """basenames referenciados por um .py (imports + 'X.py' em subprocess)."""
    t = p.read_text(encoding='utf-8', errors='replace')
    out = set(re.findall(r'(?:^|\n)\s*(?:import|from)\s+([A-Za-z_]\w*)', t))
    out |= set(re.findall(r"""['"]([A-Za-z_][\w\-]*)\.py['"]""", t))
    return out


def cmd_mapa(ctx):
    """Esqueleto REAL: stage→script (do orquestrador) × disco, + divergências e órfãos."""
    orq = ORQUESTRADOR_FILE.read_text(encoding='utf-8', errors='replace') if ORQUESTRADOR_FILE.exists() else ''
    # stage -> script real: parse 'cmd = [sys.executable, "X.py"]' seguido de _run(cmd,_,'stage')
    stage_script, last = {}, None
    for ln in orq.splitlines():
        m = re.search(r"cmd\s*=\s*\[sys\.executable,\s*'([\w\-.]+\.py)'", ln)
        if m:
            last = m.group(1)
        m2 = re.search(r"_run\(cmd,\s*[\w_]+,\s*'(\w+)'", ln)
        if m2 and last:
            stage_script[m2.group(1)] = last
    mu = re.search(r"UNMANAGED\s*=\s*\{([^}]*)\}", orq)
    unmanaged = set(re.findall(r"'(\w+)'", mu.group(1))) if mu else set()

    # universo de scripts no disco (sem _data, tools, privados)
    discos = {}
    for base in (ROOT, VIDEOS):
        if base.exists():
            for p in base.glob('*.py'):
                if p.name.endswith('_data.py') or p.name in ('vp100.py', 'limpar.py') or p.name.startswith('_'):
                    continue
                discos[p.stem] = p
    # alcançáveis a partir dos entrypoints (BFS por import + subprocess)
    seeds = set(ENTRYPOINT_SEEDS)
    for bat in ROOT.glob('*.bat'):
        try:
            seeds |= set(re.findall(r'([A-Za-z_][\w\-]*)\.py', bat.read_text(encoding='utf-8', errors='replace')))
        except Exception:
            pass
    vivos, fila = set(), list(seeds)
    while fila:
        b = fila.pop()
        if b in vivos:
            continue
        vivos.add(b)
        if b in discos:
            fila += [r for r in _refs(discos[b]) if r in discos and r not in vivos]
    orfaos = sorted(n + '.py' for n in discos if n not in vivos and n not in ('orquestrador', 'publicar_livro'))

    if ctx.json:
        print(json.dumps({'stage_script': stage_script, 'unmanaged': sorted(unmanaged),
                          'orfaos': orfaos}, ensure_ascii=False, indent=2))
        return 0

    ctx.banner('mapa — esqueleto REAL ' + ctx.p.dim('(derivado de orquestrador.py + disco)'), 'leitura')
    print(ctx.p.bold('  Etapas (dag) → runner real'))
    for st in ctx.topo(ctx.dag):
        if st in stage_script:
            sc = stage_script[st]
            existe = (ROOT / sc).exists() or (VIDEOS / sc).exists()
            print(f'    {st:<12} {sc:<22} ' + (ctx.p.green('✓') if existe else ctx.p.red('✗ não existe!')))
        elif st in unmanaged:
            print(f'    {st:<12} ' + ctx.p.dim('(sem runner · UNMANAGED — manual/outro script)'))
        else:
            print(f'    {st:<12} ' + ctx.p.red('SEM runner e fora de UNMANAGED — GAP'))

    div = []
    for st, real in stage_script.items():
        modelo = STEPS.get(st, {}).get('script', '')
        mscripts = set(re.findall(r'([\w\-]+\.py)', modelo))
        if real not in mscripts:
            div.append(f'{st}: real é "{real}", mas o modelo do vp100 diz "{modelo}"')
        else:
            extra = mscripts - {real}
            if extra:
                div.append(f'{st}: modelo cita {", ".join(sorted(extra))} que o orquestrador NÃO roda')
    if div:
        print(ctx.p.bold('\n  Divergências vp100 × real') + ctx.p.dim('  (corrigir o modelo)'))
        for d in div:
            print('    ' + ctx.p.gold('⚠ ') + d)

    print(ctx.p.bold('\n  Scripts órfãos') + ctx.p.dim(f'  ({len(orfaos)} não alcançados pelo pipeline — código morto OU ferramenta manual)'))
    for i in range(0, len(orfaos), 3):
        print('    ' + ctx.p.gold(' · '.join(orfaos[i:i + 3])))
    return 0


def cmd_update(ctx):
    """(Re)instala o atalho `vp100` no PowerShell e mostra como ativar sem reabrir."""
    alvo = str(VP100_FILE)
    func = 'function vp100 { python "' + alvo + '" @args }'
    docs = Path.home() / 'Documents'
    profiles = [docs / 'WindowsPowerShell' / 'Microsoft.PowerShell_profile.ps1',  # PS 5.1
                docs / 'PowerShell' / 'Microsoft.PowerShell_profile.ps1']         # PS 7 (pwsh)
    res = []
    for prof in profiles:
        if prof.parent.name == 'PowerShell' and not prof.parent.exists():
            res.append(('skip', prof)); continue  # pwsh7 não instalado — não criar lixo
        try:
            txt = prof.read_text(encoding='utf-8', errors='replace') if prof.exists() else ''
            if 'function vp100' in txt:
                res.append(('ok', prof))
            else:
                prof.parent.mkdir(parents=True, exist_ok=True)
                sep = '' if (not txt or txt.endswith('\n')) else '\n'
                with open(prof, 'a', encoding='utf-8') as f:
                    f.write(sep + func + '\n')
                res.append(('add', prof))
        except Exception:
            res.append(('erro', prof))

    if ctx.json:
        print(json.dumps({'vp100': alvo, 'profiles': [(s, str(p)) for s, p in res]}, ensure_ascii=False, indent=2))
        return 0
    ctx.banner('vp100 update — integração do terminal', 'leitura')
    mtime = time.strftime('%d/%m %H:%M', time.localtime((VP100_FILE).stat().st_mtime))
    print('    script ...... ' + alvo + ctx.p.dim(f'  (atualizado {mtime})'))
    print(ctx.p.bold('\n  Função vp100 no PowerShell'))
    rotulo = {'ok': ctx.p.green('já estava'), 'add': ctx.p.gold('INSTALADA'),
              'skip': ctx.p.dim('pulado (sem pwsh7)'), 'erro': ctx.p.red('erro')}
    for s, p in res:
        ver = 'PS5.1' if p.parent.name == 'WindowsPowerShell' else 'PS7  '
        print(f'    {ver}  {rotulo[s]}  {ctx.p.dim(str(p))}')
    print(ctx.p.bold('\n  Comandos'))
    print('    ' + ctx.p.dim('publicar · pipeline · agentes · bibliotecario · status · dag · custo · doctor · update'))
    print('\n  ' + ctx.p.gold('▶ ativar AGORA (sem reabrir o terminal):') + '  ' + ctx.p.bold('. $PROFILE'))
    print('  ' + ctx.p.dim('(ou abra um terminal novo — a função carrega sozinha)'))
    print('  ' + ctx.p.dim('obs.: editar o vp100.py NÃO exige reabrir — a função sempre roda a versão atual.'))
    return 0


AJUDA = __doc__


def main(argv=None):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass
    pa = argparse.ArgumentParser(prog='vp100', add_help=False)
    pa.add_argument('verbo', nargs='?', default='ajuda')
    pa.add_argument('args', nargs='*')
    pa.add_argument('--speed', choices=['fast', 'real'], default='real')
    pa.add_argument('--verbose', action='store_true')
    pa.add_argument('--seed', type=int, default=0)
    pa.add_argument('--no-color', action='store_true')
    pa.add_argument('--json', action='store_true')
    a = pa.parse_args(argv)

    if a.verbo in ('ajuda', 'help', '-h', '--help'):
        print(AJUDA)
        return 0
    ctx = Ctx(a)
    v, rest = a.verbo, a.args

    routes = {
        'publicar':      lambda: cmd_publicar(ctx, rest[0] if rest else 'instagram', rest[1] if len(rest) > 1 else 'full'),
        'pipeline':      lambda: cmd_pipeline(ctx, rest[0] if rest else 'full'),
        'agentes':       lambda: cmd_agentes(ctx),
        'bibliotecario': lambda: cmd_bibliotecario(ctx, rest),
        'biblioteca':    lambda: cmd_bibliotecario(ctx, rest),
        'status':        lambda: cmd_status(ctx),
        'dag':           lambda: cmd_dag(ctx),
        'mapa':          lambda: cmd_mapa(ctx),
        'custo':         lambda: cmd_custo(ctx, rest[0] if rest else 'full'),
        'doctor':        lambda: cmd_doctor(ctx),
        'update':        lambda: cmd_update(ctx),
    }

    if v in routes:
        return routes[v]()

    import difflib
    sug = difflib.get_close_matches(v, list(routes.keys()) + ['ajuda'], n=1)
    print(f'comando desconhecido: {v}' + (f'  ·  você quis dizer "{sug[0]}"?' if sug else ''))
    print('\n' + AJUDA)
    return 2


if __name__ == '__main__':
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n\033[33m⚠ Simulação interrompida (Ctrl+C).\033[0m")
        sys.exit(130)
    except Exception as e:
        print(f"\n\033[31m✗ Erro fatal: {e}\033[0m")
        sys.exit(1)
