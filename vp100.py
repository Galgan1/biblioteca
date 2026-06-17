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
  vp100 status                        lanes, agenda, pendências, circuit breakers
  vp100 dag                           grafo de dependências + grupos paralelos
  vp100 custo <slug>                  custo simulado (PRICES reais)
  vp100 doctor                        sanidade do ambiente simulado
  vp100 ajuda

Flags: --speed fast|real  --verbose  --seed N  --no-color  --json
"""
import argparse
import importlib.util
import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VIDEOS = ROOT / 'videos'

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
    mod = _import('dag', VIDEOS / 'dag.py')
    if mod and hasattr(mod, 'DAG'):
        return mod.DAG, mod.topological_sort, mod.parallel_groups
    dag = {
        'skill': [], 'biblioteca': ['skill'], 'video_built': ['skill'],
        'uploaded': ['video_built'], 'shorts': ['uploaded'], 'scheduled': ['shorts'],
        'instagram': ['skill'], 'tiktok': ['shorts'], 'facebook': ['uploaded'],
    }
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
    mod = _import('cost_tracker', VIDEOS / 'cost_tracker.py')
    if mod and hasattr(mod, 'PRICES'):
        return mod.PRICES
    return {'google_imagen': 0.04, 'google_veo_8s': 1.20, 'google_tts_1k': 0.016,
            'youtube_upload': 0.0, 'instagram_api': 0.0}


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
    'instagram':   dict(label='instagram',  script='gerar_carrossel.py + instagram_post.py',
                        produz='carrossel no @minutoreal1701', seg=38,
                        subs=['gerar_carrossel (7 cards)', 'legenda 5 As + disclosure',
                              'criar media container', 'media_publish', 'permalink']),
    'tiktok':      dict(label='tiktok',     script='tiktok_post.py --draft',
                        produz='RASCUNHO no TikTok', seg=30,
                        subs=['refresh token', 'upload draft']),
    'facebook':    dict(label='facebook',   script='facebook_post.py',
                        produz='post nativo + link no 1º comentário', seg=25,
                        subs=['reusar ativo do IG', 'publicar', 'comentar CTA']),
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
        self.estado = carregar_json(VIDEOS / 'canal-state.json', {'lanes': {}})
        self.books = carregar_json(ROOT / 'books.json', [])

    def banner(self, titulo):
        canal = self.estado.get('channel_name', 'Minuto Real')
        print(self.p.bold(self.p.green('▶ ' + canal)) + '  ' + self.p.dim('· SIMULAÇÃO (dry-run — nada é executado)'))
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
        return ids[0] if ids else 'padrao-bitcoin'

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
    ctx.banner(f'lane: {ctx.p.cyan(lane)}' + (f' · {conta}' if conta else '') + f' · livro: {ctx.p.bold(slug)}')
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
    ctx.banner(f'pipeline COMPLETO · livro: {ctx.p.bold(slug)} · lanes ativas: {ctx.p.cyan(", ".join(ativas) or "—")}')
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
    scripts = ['videos/gerar_video.py', 'gerar_carrossel.py', 'videos/instagram_post.py',
               'videos/upload_youtube.py', 'publicar_livro.py', 'videos/dag.py',
               'videos/cost_tracker.py', 'books.json']
    for rel in scripts:
        checks.append((rel, (ROOT / rel).exists()))
    ok_estado = bool(ctx.estado.get('lanes'))
    checks.append(('videos/canal-state.json (válido)', ok_estado))
    checks.append(('requirements.txt', (ROOT / 'requirements.txt').exists()))
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
        gitguy = 'gitguy' in (ROOT / 'CLAUDE.md').read_text(encoding='utf-8', errors='replace').lower()
    except Exception:
        pass
    # sessões de agente vivas no disco (worktrees do harness)
    wt = []
    wtdir = ROOT / '.claude' / 'worktrees'
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
    if v == 'publicar':
        return cmd_publicar(ctx, rest[0] if rest else 'instagram', rest[1] if len(rest) > 1 else 'full')
    if v == 'pipeline':
        return cmd_pipeline(ctx, rest[0] if rest else 'full')
    if v == 'agentes':
        return cmd_agentes(ctx)
    if v == 'status':
        return cmd_status(ctx)
    if v == 'dag':
        return cmd_dag(ctx)
    if v == 'custo':
        return cmd_custo(ctx, rest[0] if rest else 'full')
    if v == 'doctor':
        return cmd_doctor(ctx)
    print(Paint(False).red(f'comando desconhecido: {v}\n'))
    print(AJUDA)
    return 2


if __name__ == '__main__':
    sys.exit(main())
