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
from dataclasses import dataclass, field

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
    def __init__(self, on): self.on = on
    def c(self, s, c): return f'[{c}m{s}[0m' if self.on else str(s)
    def green(self, s): return self.c(s, '32')
    def gold(self, s): return self.c(s, '33')
    def red(self, s): return self.c(s, '31')
    def dim(self, s): return self.c(s, '2')
    def bold(self, s): return self.c(s, '1')
    def cyan(self, s): return self.c(s, '36')


# ---------------------------------------------------------------------------
# Leitura das fontes de verdade (com fallback gracioso)
# ---------------------------------------------------------------------------
def _import(nome: str, caminho: Path | str):
    try:
        spec = importlib.util.spec_from_file_location(nome, caminho)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod
    except Exception:
        return None


def carregar_dag() -> tuple:
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
    def groups(d: dict) -> list:
        rem, done, gs = set(d), set(), []
        while rem:
            g = {s for s in rem if all(x in done for x in d[s])}
            if not g:
                break
            gs.append(g); done |= g; rem -= g
        return gs
    return dag, topo, groups


def carregar_precos() -> dict[str, float]:
    precos: dict[str, float] = DEFAULT_PRICES.copy()
    mod = _import('cost_tracker', COST_TRACKER_FILE)
    if mod and hasattr(mod, 'PRICES') and isinstance(mod.PRICES, dict):
        for k, v in mod.PRICES.items():
            if isinstance(v, (int, float)):
                precos[k] = float(v)
    return precos


def carregar_json(caminho: Path | str, default: dict | list) -> dict | list:
    try:
        return json.loads(Path(caminho).read_text(encoding='utf-8', errors='replace'))
    except (OSError, ValueError):
        return default


# ---------------------------------------------------------------------------
# Manifesto das etapas (a narração de cada stage)  ·  seg = tempo SIMULADO
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class Step:
    label: str
    script: str
    produz: str
    seg: int
    subs: list[str]
    lane: str | None = None
    terminal: bool = False
    cost: dict[str, float] = field(default_factory=dict)

STEPS: dict[str, Step] = {
    'skill':       Step('skill',      'book-to-skill',              'base de conhecimento destilada', 8,   ['ler livro/PDF', 'extrair capítulos', 'validar taxonomia']),
    'biblioteca':  Step('biblioteca', 'publicar_livro.py --deploy', '<slug>.html + capítulos + deploy VPS', 60,  ['gerar_livro.py (páginas)', 'gerar_capa', 'retrofit-fase23', 'scp + chmod (VPS)'], lane='biblioteca', terminal=True),
    'video_built': Step('vídeo',      'gerar_video.py',             'videos/<slug>.mp4 (~5min)',      240, ['roteiro.json', 'TTS pt-BR', 'slides Pillow', 'trilha + marca sonora', 'montagem ffmpeg'], lane='youtube', cost={'google_tts_1k':4, 'google_imagen':8, 'google_veo_8s':3}),
    'uploaded':    Step('upload YT',  'upload_youtube.py',          'vídeo no canal (unlisted)',      120, ['OAuth token', 'upload resumable', 'metadados + thumb'], lane='youtube'),
    'shorts':      Step('shorts',     'produzir_shorts.py',         '4 shorts 9:16',                  180, ['cortar cenas', 'legendar', 'render 1080×1920'], lane='youtube', cost={'google_tts_1k':1}),
    'scheduled':   Step('agendar',    'agendar_lote.py',            'posts agendados (qua/qui)',      12,  ['calcular slots', 'setPublishAt'], lane='youtube', terminal=True),
    'instagram':   Step('instagram',  'gerar_carrossel.py',         'carrossel no @minutoreal1701',   38,  ['gerar_carrossel (7 cards)', 'legenda 5 As + disclosure', 'post manual via instagram_post.py (fora do orquestrador)'], lane='instagram', terminal=True),
    'tiktok':      Step('tiktok',     'tiktok_post.py --draft',     'RASCUNHO no TikTok',             30,  ['refresh token', 'upload draft'], lane='tiktok', terminal=True),
    'facebook':    Step('facebook',   'facebook_publicar.py',       'vídeo nativo + link no 1º comentário', 25,  ['reusar ativo do IG', 'publicar nativo', 'comentar CTA (link)'], lane='facebook', terminal=True),
}

def custo_etapa(stage, p):
    return sum(p.get(k, 0.0) * v for k, v in STEPS.get(stage, Step('', '', '', 0, [])).cost.items())


def fmt_tempo(seg):
    seg = int(round(seg))
    return f'{seg // 60}m{seg % 60:02d}s' if seg >= 60 else f'{seg}s'


# ---------------------------------------------------------------------------
# Encenação (animação)
# ---------------------------------------------------------------------------
class Tela:
    def __init__(self, p, animar): self.p, self.animar = p, animar
    def passo(self, pre, rot, dur, res, marca=''):
        ln = f'{pre}{rot} '.ljust(40, '.')
        if self.animar and dur > 0:
            import time, sys
            t0, k, S = time.time(), 0, '⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏'
            while time.time() - t0 < dur:
                sys.stdout.write(f'\r{ln} {self.p.gold(S[k%10])}'); sys.stdout.flush(); time.sleep(0.08); k += 1
        import sys
        sys.stdout.write(f'\r{ln} {self.p.green("✓")} {self.p.dim(res + (" " + marca if marca else ""))}\n')
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
        alvo = next((s for s, m in STEPS.items() if m.lane == lane and m.terminal), None)
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


def plan_publish(ctx, lane, escopo):
    terminais = {m.lane: s for s, m in STEPS.items() if m.terminal}
    if lane not in terminais:
        return None, f"lane desconhecida: {lane}. Use: " + ", ".join(terminais.keys())

    slug = ctx.resolver_slug(escopo)
    info = ctx.estado.get('lanes', {}).get(lane, {})
    stages = ctx.stages_da_lane(lane)
    
    plan = {
        'lane': lane,
        'slug': slug,
        'account': info.get('account', ''),
        'status': info.get('status'),
        'reason': info.get('reason', '?'),
        'stages': []
    }

    terminal = terminais[lane]
    for st in stages:
        m = STEPS[st]
        stage_info = {
            'id': st,
            'label': m.label,
            'script': m.script,
            'produz': m.produz,
            'seg': m.seg,
            'cost': custo_etapa(st, ctx.precos),
            'subs': []
        }
        if st == terminal:
            for sub in m.subs:
                rede = any(k in sub for k in ('container', 'publish', 'upload', 'permalink', 'comentar'))
                stage_info['subs'].append({'label': sub, 'simulated': rede})
        plan['stages'].append(stage_info)
        
    plan['total_cost'] = sum(s['cost'] for s in plan['stages'])
    plan['total_time'] = sum(s['seg'] for s in plan['stages'])
    
    return plan, None


def cmd_publicar(ctx, lane, escopo):
    plan, err = plan_publish(ctx, lane, escopo)
    if err:
        print(ctx.p.red(err))
        return 2

    if ctx.json:
        import json
        print(json.dumps(plan, ensure_ascii=False, indent=2))
        return 0

    conta = plan['account']
    ctx.banner(f'lane: {ctx.p.cyan(plan["lane"])}' + (f' · {conta}' if conta else '') + f' · livro: {ctx.p.bold(plan["slug"])}', 'sim')
    
    if plan['status'] == 'blocked':
        print(ctx.p.gold(f'  ⚠ lane BLOQUEADA ({plan["reason"]}) — simulando o fluxo mesmo assim.\n'))

    total = len(plan['stages'])
    for i, st in enumerate(plan['stages'], 1):
        marca = st['script'] if ctx.verbose else ''
        ctx.tela.passo(f'  [{i}/{total}] ', st['label'], min(st['seg'] * 0.01, 1.0), st['produz'], marca)
        for sub in st['subs']:
            res = 'ok (SIMULADO)' if sub['simulated'] else 'ok'
            ctx.tela.passo('        · ', sub['label'], 0.3, res)

    print()
    print('  ' + ctx.p.green('✓ publicado (simulado)') + '  ·  custo US$ %.2f  ·  tempo simulado ~%s' % (plan['total_cost'], fmt_tempo(plan['total_time'])))
    _proximo(ctx)
    return 0


def calc_pipeline_state(ctx, slug):
    slug = ctx.resolver_slug(slug)
    ativas = [ln for ln, v in ctx.estado.get('lanes', {}).items() if v.get('status') == 'active']
    ordem = ctx.topo(ctx.dag)
    
    plan = []
    custo = 0.0
    for gi, grupo in enumerate(ctx.groups(ctx.dag), 1):
        gstages = [s for s in ordem if s in grupo]
        steps = []
        for st in gstages:
            if st not in STEPS:
                continue
            step = STEPS[st]
            skipped = bool(step.lane and step.lane not in ativas and step.lane != 'biblioteca')
            if not skipped:
                custo += custo_etapa(st, ctx.precos)
            
            steps.append({
                'id': st, 'label': step.label, 'skipped': skipped, 
                'seg': step.seg, 'produz': step.produz, 'script': step.script
            })
            
        plan.append({'index': gi, 'labels': [STEPS[s].label for s in gstages if s in STEPS], 'steps': steps})
        
    return {
        'slug': slug,
        'ativas': ativas,
        'plan': plan,
        'custo': custo,
        'seg': sum(STEPS[s].seg for s in ordem if (s in STEPS and not bool(STEPS[s].lane and STEPS[s].lane not in ativas and STEPS[s].lane != 'biblioteca')))
    }


def cmd_pipeline(ctx, slug):
    state = calc_pipeline_state(ctx, slug)
    
    if ctx.json:
        import json
        print(json.dumps(state, ensure_ascii=False, indent=2))
        return 0

    ctx.banner(f'pipeline COMPLETO · livro: {ctx.p.bold(state["slug"])} · lanes ativas: {ctx.p.cyan(", ".join(state["ativas"]) or "—")}', 'sim')
    
    for g in state['plan']:
        print(ctx.p.dim(f'  grupo {g["index"]} (paralelo): ') + ', '.join(g['labels']))
        for st in g['steps']:
            if st['skipped']:
                ctx.tela.passo('    ', st['label'], 0.0, 'pulado (lane inativa)')
            else:
                marca = st['script'] if ctx.verbose else ''
                ctx.tela.passo('    ', st['label'], min(st['seg'] * 0.008, 0.9), st['produz'], marca)
                
    print()
    print('  ' + ctx.p.green('✓ pipeline simulado') + '  ·  custo US$ %.2f  ·  tempo simulado ~%s' % (state['custo'], fmt_tempo(state['seg'])))
    return 0


def with_json(func):
    """Decorator to isolate JSON output from the CLI presentation layer."""
    def wrapper(ctx, *args, **kwargs):
        data, render = func(ctx, *args, **kwargs)
        if ctx.json:
            import json
            print(json.dumps(data, ensure_ascii=False, indent=2))
        else:
            render()
        return 0
    return wrapper

@with_json
def cmd_status(ctx):
    e = ctx.estado
    data = {
        'lanes': e.get('lanes'), 'agenda': e.get('schedule_cadence'),
        'upcoming': e.get('upcoming_schedule'), 'pending': e.get('pending_operations'),
        'api_health': e.get('api_health')
    }
    
    def render():
        ctx.banner('status do canal (lido de canal-state.json)')
        print(ctx.p.bold('  Lanes'))
        for ln, v in (data['lanes'] or {}).items():
            st, cor = v.get('status', '?'), ctx.p.green if v.get('status') == 'active' else ctx.p.red
            ext = f" — {v['reason']}" if v.get('reason') else (f" · {v['account']}" if v.get('account') else "")
            print(f'    {cor("●")} {ln:<11} {cor(st)}{ctx.p.dim(ext)}')
            
        if u := data['upcoming']:
            print(ctx.p.bold('\n  Próximos longos'))
            for it in u[:5]: print(f'    {ctx.p.gold("›")} {it.get("slug","?"):<16} {ctx.p.dim(str(it.get("longo_date","?")))}')
            
        if p := data['pending']:
            print(ctx.p.bold('\n  Pendências'))
            for k, v in p.items(): print(f'    {ctx.p.gold("•")} {k} {ctx.p.dim("— " + str(v.get("note", ""))[:70])}')
            
        abertos = [k for k, v in (data['api_health'] or {}).items() if v.get('state') != 'closed']
        print(ctx.p.bold('\n  Circuit breakers\n    ') + (ctx.p.red('ABERTOS: ' + ', '.join(abertos)) if abertos else ctx.p.green('todos fechados (saudáveis)')))
        
    return data, render

@with_json
def cmd_dag(ctx):
    ordem, grupos = ctx.topo(ctx.dag), ctx.groups(ctx.dag)
    
    def render():
        lbl = lambda s: STEPS[s].label if s in STEPS else s
        ctx.banner('grafo de dependências (videos/dag.py)')
        print(ctx.p.bold('  Ordem topológica\n    ') + ctx.p.dim(' → ').join(map(lbl, ordem)))
        print(ctx.p.bold('\n  Grupos paralelos'))
        for i, g in enumerate(grupos, 1): print(f'    {i}. ' + ', '.join(sorted(map(lbl, g))))
        
    return {'ordem': ordem, 'grupos': [sorted(g) for g in grupos]}, render


@with_json
def cmd_custo(ctx, slug):
    p = ctx.precos
    linhas = [(STEPS[s].label, custo_etapa(s, p)) for s in ctx.topo(ctx.dag) if custo_etapa(s, p) > 0]
    total = sum(c for _, c in linhas)

    def render():
        ctx.banner(f'custo simulado · livro: {ctx.p.bold(slug)} ' + ctx.p.dim('(estimativa, preços de cost_tracker.py)'))
        for nome, c in linhas:
            print(f'    {nome:<12} US$ %.2f' % c)
        print(ctx.p.dim('    ' + '-' * 22))
        print('    ' + ctx.p.bold('TOTAL') + '        US$ %.2f' % total)
        print(ctx.p.dim('    (carrossel/IG e site = US$0 — geração local)'))

    return {'slug': slug, 'itens': linhas, 'total_usd': round(total, 4)}, render


@with_json
def cmd_doctor(ctx):
    lanes = ctx.estado.get('lanes', {})
    checks = {r: (ROOT / r).exists() for r in EXPECTED_SCRIPTS} | {
        'videos/canal-state.json (válido)': bool(lanes),
        REQUIREMENTS_FILE.name: REQUIREMENTS_FILE.exists()
    }
    
    data = {
        'checks': checks,
        'catalogo': (nbooks := len(ctx.books)),
        'lanes_ativas': (ativas := sum(1 for v in lanes.values() if v.get('status') == 'active')),
        'lanes_total': (nlanes := len(lanes)),
        'ambiente_ok': not (faltam := [n for n, ok in checks.items() if not ok])
    }

    def render():
        ctx.banner('sanidade do ambiente (vp100 doctor)')
        for n, ok in checks.items():
            print(f'    {ctx.p.green("✓") if ok else ctx.p.red("✗")} {n}')
        print(ctx.p.dim(f'\n    catálogo: {nbooks} livros · lanes ativas: {ativas}/{nlanes}'))
        print(f'    {ctx.p.gold("faltando: " + ", ".join(faltam)) if faltam else ctx.p.green("ambiente OK")}')

    return data, render


@with_json
def cmd_agentes(ctx):
    """Lista os agentes ATUAIS — derivado do real (canal-state.json + CLAUDE.md + worktrees)."""
    lanes = ctx.estado.get('lanes', {})
    gitguy = CLAUDE_MD_FILE.exists() and 'gitguy' in CLAUDE_MD_FILE.read_text(encoding='utf-8', errors='replace').lower()
    wt = sorted(d.name for d in WORKTREES_DIR.iterdir() if d.is_dir() and d.name.startswith('agent-')) if WORKTREES_DIR.exists() else []

    data = {
        'lanes': {k: {'status': v.get('status'), 'agent': v.get('agent'), 'account': v.get('account')} for k, v in lanes.items()},
        'gitguy': gitguy, 'worktrees_vivos': wt
    }

    def render():
        ctx.banner('agentes ' + ctx.p.dim('(derivado de canal-state.json + CLAUDE.md + git worktree)'))
        print(ctx.p.bold('  Lanes operacionais') + ctx.p.dim('  · canal-state.json'))
        
        sem_agente = sum(1 for v in lanes.values() if not v.get('agent'))
        for ln, v in lanes.items():
            bola = ctx.p.green('●') if v.get('status') == 'active' else ctx.p.red('○')
            agtxt = ctx.p.cyan(ag) if (ag := v.get('agent')) else ctx.p.gold('— não nomeado')
            acct = ctx.p.dim(' · ' + acc) if (acc := v.get('account')) else ''
            print(f'    {bola} {ln:<11} {v.get("status", ""):<8} agente: {agtxt}{acct}')

        print(ctx.p.bold('\n  Governança') + ctx.p.dim('  · biblioteca/CLAUDE.md'))
        print('    ' + (ctx.p.cyan('⬢ GitGuy') + ctx.p.dim(' — único autorizado a commit / push / criar PR')
                        if gitguy else ctx.p.dim('(nenhuma regra de versionamento detectada)')))

        print(ctx.p.bold('\n  Sessões de agente vivas') + ctx.p.dim('  · .claude/worktrees'))
        print('\n'.join(f'    {ctx.p.gold("•")} {w}' for w in wt) if wt else f'    {ctx.p.dim("nenhuma")}')

        if sem_agente:
            print('\n  ' + ctx.p.gold(f'⚠ achado: {sem_agente}/{len(lanes)} lanes sem campo "agent" no canal-state.json — fonte de verdade incompleta.'))

    return data, render


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
        if ctx.json:
            import json
            print(json.dumps({"error": f"opção desconhecida: {sub}"}, ensure_ascii=False))
        else:
            print(ctx.p.red(f'opção desconhecida: bibliotecario {sub}  ·  use: livros [<slug>]'))
        return 2
    return _bib_perfil(ctx)


@with_json
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
        
    data = {
        'agente': 'Bibliotecario',
        'lane': 'biblioteca',
        'status': lane.get('status'),
        'catalogo': len(books),
        'paginas_disco': no_disco,
        'com_data': com_data,
        'com_capa': com_capa,
        'com_amazon': com_amz,
        'desc': desc
    }

    def render():
        ctx.banner('agente: ' + ctx.p.cyan('Bibliotecario') + ctx.p.dim('  (leitura do real)'))
        print(ctx.p.bold('  Função') + ctx.p.dim('  · biblioteca.md'))
        print('    ' + (data['desc'] or 'responsável pelo site /biblioteca — estética, páginas, PDF, afiliados, SEO, deploy'))
        st = data['status'] or '?'
        print('    lane: ' + ctx.p.cyan('biblioteca') + ' · ' + (ctx.p.green(st) if st == 'active' else ctx.p.red(st)))
        
        print(ctx.p.bold('\n  Acervo') + ctx.p.dim('  · books.json + disco'))
        n = data['catalogo']
        print(f'    catálogo ............ {n}')
        
        def show_metric(label, value, total, warn_msg):
            msg = f'    {label:<21} {value}'
            if value < total:
                msg += ctx.p.gold(warn_msg.format(faltam=total-value, total=total, value=value))
            print(msg)
            
        show_metric('páginas no disco ....', data['paginas_disco'], n, '  (faltam {faltam})')
        show_metric('com fonte _data.py ..', data['com_data'], n, '  (faltam {faltam})')
        show_metric('com capa ............', data['com_capa'], n, '  (faltam {faltam})')
        show_metric('com link Amazon .....', data['com_amazon'], n, '  ⚠ só {value}/{total} monetizados')
        
        print(ctx.p.bold('\n  Opções'))
        print('    ' + ctx.p.dim('vp100 bibliotecario livros') + '          tabela de todos os livros')
        print('    ' + ctx.p.dim('vp100 bibliotecario livros <slug>') + '   status de um livro')

    return data, render


@with_json
def _bib_tabela(ctx):
    books = sorted(ctx.books, key=lambda b: b.get('title', '').lower())
    
    data = []
    for b in books:
        data.append({
            'id': b['id'],
            'title': b.get('title', ''),
            'pagina': _pagina(b, b['id']).exists(),
            'caps': _capitulos(b['id']),
            'data': _data_py(b['id']).exists(),
            'capa': _tem_capa(b),
            'amazon': bool(b.get('amazon'))
        })

    def render():
        ctx.banner('Bibliotecario · livros ' + ctx.p.dim(f'({len(data)} no books.json)'))
        print(ctx.p.dim('   pág  livro                                   cap  capa data amz'))
        for row in data:
            pg = ctx.p.green('✓') if row['pagina'] else ctx.p.red('✗')
            cap = str(row['caps'] or '·')
            capa = '✓' if row['capa'] else ctx.p.gold('·')
            dat = '✓' if row['data'] else ctx.p.gold('·')
            amz = '✓' if row['amazon'] else ctx.p.dim('·')
            print(f'    {pg}   {row["title"][:38].ljust(38)} {cap:>3}  {capa:>3} {dat:>3} {amz:>3}')
        print(ctx.p.dim('\n  pág ✓=página no disco · cap=nº de .html · data=fonte _data.py · amz=link Amazon'))

    return data, render


@with_json
def _bib_livro(ctx, slug):
    b = _bk(ctx, slug)
    pagina, caps, data_py = _pagina(b, slug), _capitulos(slug), _data_py(slug)
    
    data = {
        'slug': slug,
        'no_catalogo': bool(b),
        'titulo': b.get('title') if b else None,
        'author': b.get('author') if b else None,
        'progress': b.get('progress') if b else None,
        'tags': b.get('tags', []) if b else [],
        'pagina': pagina.exists(),
        'pagina_name': pagina.name,
        'capitulos': caps,
        'fonte_data': data_py.exists(),
        'fonte_name': data_py.name,
        'capa': _tem_capa(b),
        'capa_name': b.get('coverUrl') if b else None,
        'amazon': bool(b and b.get('amazon')),
        'amazon_link': b.get('amazon') if b else None
    }

    def render():
        ctx.banner('Bibliotecario · livro: ' + ctx.p.bold(slug))
        if not data['no_catalogo']:
            print('  ' + ctx.p.red('não está no books.json') + ctx.p.dim(' — checando o disco mesmo assim'))
        else:
            print(f'    título ...... {data["titulo"] or "?"} · {ctx.p.dim(data["author"] or "?")}')
            print(f'    progresso ... {ctx.p.dim(data["progress"] or "—")}')
            print(f'    tags ........ {ctx.p.dim(", ".join(data["tags"] or ["—"]))}')

        def linha(rot, ok, det=''):
            m = ctx.p.green('✓') if ok else ctx.p.red('✗')
            return f'    {rot:<13} {m}' + (ctx.p.dim('  ' + det) if det else '')

        print(linha('página', data['pagina'], data['pagina_name']))
        print(linha('capítulos', data['capitulos'] > 0, f'{data["capitulos"]} .html em {slug}/'))
        print(linha('fonte _data', data['fonte_data'], data['fonte_name']))
        print(linha('capa', data['capa'], data['capa_name'] or ''))
        
        amz_link = data['amazon_link'] or ''
        print(linha('amazon', data['amazon'], (amz_link[:48] + '...') if len(amz_link) > 48 else amz_link))
        
        probs = []
        if data['pagina'] and not data['fonte_data']:
            probs.append('página sem _data.py (fonte)')
        if data['no_catalogo'] and not data['capa']:
            probs.append('sem capa no disco')
        if data['no_catalogo'] and not data['amazon']:
            probs.append('sem link Amazon (não monetizado)')
            
        if probs:
            print('\n  ' + ctx.p.gold('⚠ ' + ' · '.join(probs)))

    return data, render


def _refs(p):
    """basenames referenciados por um .py (imports + 'X.py' em subprocess)."""
    t = p.read_text(encoding='utf-8', errors='replace')
    out = set(re.findall(r'(?:^|\n)\s*(?:import|from)\s+([A-Za-z_]\w*)', t))
    out |= set(re.findall(r"""['"]([A-Za-z_][\w\-]*)\.py['"]""", t))
    return out


@with_json
def cmd_mapa(ctx):
    """Esqueleto REAL: stage→script (do orquestrador) × disco, + divergências e órfãos."""
    orq = ORQUESTRADOR_FILE.read_text(encoding='utf-8', errors='replace') if ORQUESTRADOR_FILE.exists() else ''
    
    stage_script, last = {}, None
    for ln in orq.splitlines():
        if m := re.search(r"cmd\s*=\s*\[sys\.executable,\s*'([\w\-.]+\.py)'", ln):
            last = m.group(1)
        if (m2 := re.search(r"_run\(cmd,\s*[\w_]+,\s*'(\w+)'", ln)) and last:
            stage_script[m2.group(1)] = last

    unmanaged = set(re.findall(r"'(\w+)'", mu.group(1))) if (mu := re.search(r"UNMANAGED\s*=\s*\{([^}]*)\}", orq)) else set()

    discos = {
        p.stem: p for base in (ROOT, VIDEOS) if base.exists() 
        for p in base.glob('*.py') 
        if not (p.name.endswith('_data.py') or p.name in ('vp100.py', 'limpar.py') or p.name.startswith('_'))
    }

    seeds = set(ENTRYPOINT_SEEDS)
    for bat in ROOT.glob('*.bat'):
        try: seeds |= set(re.findall(r'([A-Za-z_][\w\-]*)\.py', bat.read_text('utf-8', 'replace')))
        except Exception: pass

    vivos, fila = set(), list(seeds)
    while fila:
        if (b := fila.pop()) not in vivos:
            vivos.add(b)
            if b in discos:
                fila.extend(r for r in _refs(discos[b]) if r in discos and r not in vivos)

    orfaos = sorted(n + '.py' for n in discos if n not in vivos and n not in ('orquestrador', 'publicar_livro'))

    div = []
    for st, real in stage_script.items():
        mscripts = set(re.findall(r'([\w\-]+\.py)', (modelo := STEPS[st].script if st in STEPS else '')))
        if real not in mscripts:
            div.append(f'{st}: real é "{real}", mas o modelo do vp100 diz "{modelo}"')
        elif extra := mscripts - {real}:
            div.append(f'{st}: modelo cita {", ".join(sorted(extra))} que o orquestrador NÃO roda')

    def render():
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

        if div:
            print(ctx.p.bold('\n  Divergências vp100 × real') + ctx.p.dim('  (corrigir o modelo)'))
            for d in div: print('    ' + ctx.p.gold('⚠ ') + d)

        print(ctx.p.bold('\n  Scripts órfãos') + ctx.p.dim(f'  ({len(orfaos)} não alcançados pelo pipeline — código morto OU ferramenta manual)'))
        for i in range(0, len(orfaos), 3):
            print('    ' + ctx.p.gold(' · '.join(orfaos[i:i + 3])))

    return {'stage_script': stage_script, 'unmanaged': sorted(unmanaged), 'orfaos': orfaos, 'divergencias': div}, render


@with_json
def cmd_update(ctx):
    """(Re)instala o atalho `vp100` no PowerShell e mostra como ativar sem reabrir."""
    alvo = str(VP100_FILE)
    func = 'function vp100 { python "' + alvo + '" @args }'
    docs = Path.home() / 'Documents'
    profiles = [
        docs / 'WindowsPowerShell' / 'Microsoft.PowerShell_profile.ps1',  # PS 5.1
        docs / 'PowerShell' / 'Microsoft.PowerShell_profile.ps1'          # PS 7 (pwsh)
    ]
    
    res = []
    for prof in profiles:
        if prof.parent.name == 'PowerShell' and not prof.parent.exists():
            res.append(('skip', prof))
            continue  # pwsh7 não instalado — não criar lixo
            
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

    data = {
        'vp100': alvo,
        'profiles': [(s, str(p)) for s, p in res]
    }

    def render():
        ctx.banner('vp100 update — integração do terminal', 'leitura')
        
        mtime = time.strftime('%d/%m %H:%M', time.localtime((VP100_FILE).stat().st_mtime))
        print('    script ...... ' + alvo + ctx.p.dim(f'  (atualizado {mtime})'))
        
        print(ctx.p.bold('\n  Função vp100 no PowerShell'))
        rotulo = {
            'ok': ctx.p.green('já estava'), 
            'add': ctx.p.gold('INSTALADA'),
            'skip': ctx.p.dim('pulado (sem pwsh7)'), 
            'erro': ctx.p.red('erro')
        }
        
        for s, p in res:
            ver = 'PS5.1' if p.parent.name == 'WindowsPowerShell' else 'PS7  '
            print(f'    {ver}  {rotulo[s]}  {ctx.p.dim(str(p))}')
            
        print(ctx.p.bold('\n  Comandos'))
        print('    ' + ctx.p.dim('publicar · pipeline · agentes · bibliotecario · status · dag · custo · doctor · update'))
        print('\n  ' + ctx.p.gold('▶ ativar AGORA (sem reabrir o terminal):') + '  ' + ctx.p.bold('. $PROFILE'))
        print('  ' + ctx.p.dim('(ou abra um terminal novo — a função carrega sozinha)'))
        print('  ' + ctx.p.dim('obs.: editar o vp100.py NÃO exige reabrir — a função sempre roda a versão atual.'))

    return data, render


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

    p0 = rest[0] if len(rest) > 0 else None
    p1 = rest[1] if len(rest) > 1 else None

    routes = {
        'publicar':      lambda: cmd_publicar(ctx, p0 or 'instagram', p1 or 'full'),
        'pipeline':      lambda: cmd_pipeline(ctx, p0 or 'full'),
        'agentes':       lambda: cmd_agentes(ctx),
        'bibliotecario': lambda: cmd_bibliotecario(ctx, rest),
        'biblioteca':    lambda: cmd_bibliotecario(ctx, rest),
        'status':        lambda: cmd_status(ctx),
        'dag':           lambda: cmd_dag(ctx),
        'mapa':          lambda: cmd_mapa(ctx),
        'custo':         lambda: cmd_custo(ctx, p0 or 'full'),
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
