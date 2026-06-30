# -*- coding: utf-8 -*-
"""publicar_tudo.py — orquestrador 1-clique (roda na VPS): slug -> YouTube(longo+Shorts)
+ Instagram + Facebook. O CORAÇÃO do plano PUBLICACAO-1CLICK.

Contratos:
- HÍBRIDO: usa <slug>.mp4 se já existe (premium 3DGS vem do PC local); senão renderiza
  soberano (gerar_video, Ken Burns) na VPS.
- IDEMPOTENTE: estado em _shorts/<slug>_publicar_tudo.json — re-rodar PULA o que já saiu.
- GATE no caminho: verificar_copy.checa_duro em cada legenda (pt-PT/link-cru/Amazon-busca/
  spam) — reprova = a superfície falha, não publica defeito. canal_guard (YT) vive dentro
  do upload_youtube.
- ERRO não derruba as outras superfícies: registra estado + dispara ALERTA no Telegram
  (notificar) com contexto (Akita pilar 7). Verde = exit 0 (tudo ok/pulado); 1 se algo falhou.

Uso:  python publicar_tudo.py <slug> [--so youtube_longo,instagram] [--dry]
"""
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).parent
for _p in (ROOT, ROOT.parent):            # VPS é flat; local faz a ponte videos<->raiz
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))


# --- estado / alerta -------------------------------------------------------
def _estado_path(slug):
    return ROOT / '_shorts' / f'{slug}_publicar_tudo.json'


def _carrega(slug):
    try:
        return json.loads(_estado_path(slug).read_text(encoding='utf-8'))
    except Exception:
        return {}


def _salva(slug, est):
    p = _estado_path(slug)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(est, ensure_ascii=False, indent=2), encoding='utf-8')


def _alerta(msg):
    """Best-effort: alerta no Telegram (notificar). Nunca quebra o orquestrador."""
    try:
        import notificar
        notificar.notificar(msg)
    except Exception:
        pass


def _gate(caption, plataforma):
    """Piso de copy determinístico — levanta se reprovar (o defeito não vai ao ar)."""
    try:
        from verificar_copy import checa_duro
    except Exception:
        return
    falhas = checa_duro(caption or '', plataforma)
    if falhas:
        raise ValueError('copy reprovada (' + plataforma + '): ' + '; '.join(falhas))


def _cfg(slug):
    return json.loads((ROOT / f'{slug}.json').read_text(encoding='utf-8'))


def _roteiro_paths(slug):
    """Os dois lugares onde o roteiro pode estar: flat em ROOT (o deploy põe assim na
    VPS) e roteiros/<slug>.json (layout local). É a ÚNICA fonte do conteúdo: gerar_video
    + youtube/IG/FB/shorts leem o roteiro — NÃO o <slug>_data.py, nem a skill, nem /var/www."""
    return (ROOT / f'{slug}.json', ROOT / 'roteiros' / f'{slug}.json')


def publicavel(slug):
    """-> (ok, motivo). Há roteiro RENDERÁVEL p/ o slug? Mesma definição canônica que
    servir_publicar._livros usa na UI: JSON dict com 'titulo' e 'cenas'. Preflight de
    leitura (grátis, sem API) p/ o --dry parar de dar FALSO-VERDE em livro sem roteiro
    — 81/103 do acervo não tinham roteiro em 22/jun, e o --dry curto-circuitava antes de
    qualquer leitura, devolvendo exit 0 como se fossem publicáveis."""
    p_flat, _ = _roteiro_paths(slug)
    for p in _roteiro_paths(slug):
        try:
            cfg = json.loads(p.read_text(encoding='utf-8'))
        except (OSError, ValueError):
            continue
        if isinstance(cfg, dict) and cfg.get('titulo') and cfg.get('cenas'):
            return True, ''
        return False, f'roteiro {p.name} sem titulo/cenas'
    return False, f'sem roteiro p/ {slug} (esperado {p_flat.name} com titulo+cenas)'


def _garante_roteiro_subdir(slug):
    """Os postadores (produzir_shorts/instagram_post/facebook_post) leem
    roteiros/<slug>.json (subpasta); o deploy põe o roteiro FLAT em ROOT. Espelha p/ a
    subpasta se faltar — senão IG/FB/Shorts quebram com FileNotFoundError (bug real
    jun/26: publish da VPS só passava no YouTube-longo, que lê flat). Self-healing p/
    não depender de patch manual de deploy."""
    flat = ROOT / f'{slug}.json'
    sub = ROOT / 'roteiros' / f'{slug}.json'
    if flat.exists() and not sub.exists():
        sub.parent.mkdir(parents=True, exist_ok=True)
        import shutil
        shutil.copy2(flat, sub)


# --- híbrido: garante o vídeo-mãe ------------------------------------------
def _garante_video(slug):
    """Usa <slug>.mp4 se existe (premium do PC local); senão renderiza soberano na VPS.
    T7: se o config pediu premium mas o asset não chegou e o PC local (3DGS) está offline
    (heartbeat velho), avisa no Telegram e degrada pro soberano — em vez de esperar um
    render que não vem."""
    mp4 = ROOT / f'{slug}.mp4'
    if mp4.exists():
        return str(mp4)
    if _cfg(slug).get('premium') or _cfg(slug).get('nivel') == 'premium':
        try:
            from heartbeat import pc_online
            if not pc_online():
                _alerta(f'[publicar_tudo] {slug}: PC local offline (3DGS) — caindo no render soberano')
        except Exception:
            pass
    import gerar_video                       # soberano (Ken Burns) — imagens via Imagen (API)
    gerar_video.main(str(ROOT / f'{slug}.json'))
    if not mp4.exists():
        raise RuntimeError(f'render nao produziu {mp4.name}')
    return str(mp4)


# --- superfícies (cada uma: gate + publica + devolve resumo) ---------------
def _pub_youtube_longo(slug, ctx):
    import upload_youtube
    _gate((_cfg(slug).get('youtube') or {}).get('descricao', ''), 'youtube')
    vid = upload_youtube.upload(ctx['video'], str(ROOT / f'{slug}.json'))   # canal_guard dentro
    ctx['video_id'] = vid
    return vid


def _pub_youtube_shorts(slug, ctx):
    import produzir_shorts
    return produzir_shorts.main(slug, ctx.get('video_id'))


def _pub_instagram(slug, ctx):
    import instagram_post
    return instagram_post.postar_reels(slug)   # Reels dos cortes (carrossel/story = passo futuro)


def _pub_facebook(slug, ctx):
    import facebook_post
    _gate(facebook_post.caption_for(_cfg(slug)), 'facebook') if hasattr(facebook_post, 'caption_for') else None
    return facebook_post.postar_longo(slug, ctx.get('video_id'))


SUPERFICIES = [
    ('youtube_longo', _pub_youtube_longo),
    ('youtube_shorts', _pub_youtube_shorts),
    ('instagram', _pub_instagram),
    ('facebook', _pub_facebook),
]

# --- alerta de FIM (AUTO-EXPLICATIVO, disparado SEMPRE) --------------------
_ICONES = {'ok': '✅', 'pulado': '⏭️', 'ERRO': '❌', 'dry-run': '🧪'}
_ROTULOS = {'youtube_longo': 'YouTube (vídeo longo)', 'youtube_shorts': 'YouTube Shorts',
            'instagram': 'Instagram', 'facebook': 'Facebook'}
# Estado cru -> frase humana. POR QUÊ: o operador não sabe o que é "dry-run"/"pulado";
# o alerta tem que se explicar sozinho, sem jargão (pedido do André, 22/jun).
_HUMANO = {'ok': 'publicado', 'pulado': 'já estava no ar (pulei)',
           'ERRO': 'FALHOU', 'dry-run': 'pronto, mas NÃO publiquei (era só ensaio)'}


def _titulo(slug):
    """Título legível do livro (de books.json); cai no slug se não achar. Best-effort."""
    try:
        for b in json.loads((ROOT / 'books.json').read_text(encoding='utf-8')):
            s = b.get('id') or b.get('url', '').rsplit('/', 1)[-1].replace('.html', '')
            if s == slug:
                return b.get('titulo') or b.get('title') or slug
    except Exception:
        pass
    return slug


def _estado(v):
    """Estado cru ('ok'/'pulado'/'ERRO'/'dry-run') a partir do valor da superfície."""
    return v.split(':', 1)[0].split(' ', 1)[0]


def _linha(nome, v):
    """Uma linha do placar em linguagem humana + o detalhe (link/id no ok, motivo no erro)."""
    est = _estado(v)
    linha = f'{_ICONES.get(est, "•")} {_ROTULOS.get(nome, nome)}: {_HUMANO.get(est, v)}'
    detalhe = v.split(':', 1)[1].strip() if ':' in v and est in ('ok', 'ERRO') else ''
    return f'{linha} — {detalhe}' if detalhe else linha


def _placar(slug, res):
    """Alerta de FIM auto-explicativo: diz O QUE é, QUAL livro e O QUE aconteceu em cada rede.
    J3 nº2: avisa SEMPRE (sucesso inclusive) p/ cumprir o 'te aviso ao concluir' do bot."""
    redes = [(n, res[n]) for n, _fn in SUPERFICIES if res.get(n) is not None]
    estados = {_estado(v) for _n, v in redes}
    titulo = _titulo(slug)
    livro = titulo if titulo == slug else f'{titulo} ({slug})'      # evita "X (X)" sem título
    corpo = '\n'.join(_linha(n, v) for n, v in redes)
    if estados and estados <= {'dry-run', 'pulado'}:               # ensaio: nada real saiu
        return ('🧪 ENSAIO concluído — nada foi publicado de verdade\n\n'
                f'📕 Livro: {livro}\n'
                'Foi um TESTE do fluxo: nenhum vídeo subiu e nenhuma cota/API foi gasta.\n'
                f'O que aconteceria numa publicação REAL:\n\n{corpo}\n\n'
                '▶️ Para publicar de verdade: no bot, menu 🚀 Publicar → ✅ Confirmar.')
    if 'ERRO' in estados:                                          # publicou, mas algo falhou
        return ('⚠️ Publicação concluída COM FALHAS\n\n'
                f'📕 Livro: {livro}\n\n{corpo}\n\n'
                '↻ Pode re-publicar: o pipeline retoma só o que faltou (o que já saiu é pulado).')
    return (f'✅ Publicado com sucesso\n📕 Livro: {livro}\n\n{corpo}')   # tudo no ar


def publicar_tudo(slug, so=None, dry=False):
    """Orquestra as 4 superfícies. so=set de nomes p/ filtrar; dry=não publica. Devolve dict."""
    # Catraca de gasto (Akita pilar 8) ligada no ENTRYPOINT — vale p/ TODO disparo,
    # inclusive o do bot Telegram (o Popen herda este env). No caminho premium o <slug>.mp4
    # já existe e gerar_video.main (que ligava o teto) NÃO roda, então sem isto o TTS pago
    # dos Shorts (gv.tts) gastaria SEM catraca (J3 nº3). setdefault respeita override do CI.
    import cost_tracker
    os.environ.setdefault('WEEKLY_BUDGET_USD', str(cost_tracker.DEFAULT_WEEKLY_BUDGET_USD))
    ok, motivo = publicavel(slug)
    if not ok:                                   # gate canônico: sem roteiro = NADA renderiza/publica
        if not dry:                              # real: registra (Akita pilar 7) — operador aprende pelo Telegram
            _alerta(f'[publicar_tudo] {slug}: NAO publicavel -> {motivo}')
        return {'_sem_roteiro': motivo}
    est = _carrega(slug)
    ctx = {'video_id': est.get('_video_id')}
    res = {}
    if not dry:                                  # dry = teste do fluxo: NÃO toca render/asset/APIs
        _garante_roteiro_subdir(slug)            # IG/FB/Shorts leem roteiros/<slug>.json
        try:
            ctx['video'] = _garante_video(slug)
        except Exception as e:
            _alerta(f'[publicar_tudo] {slug}: render/asset FALHOU -> {str(e)[:300]}')
            return {'_erro_render': str(e)}
    for nome, fn in SUPERFICIES:
        if so and nome not in so:
            continue
        if est.get(nome) == 'ok':
            res[nome] = 'pulado (idempotente)'
            continue
        if dry:
            res[nome] = est[nome] = 'dry-run'   # grava p/ a página mostrar o status ('dry-run' != 'ok' → run real depois publica)
            _salva(slug, est)
            continue
        try:
            r = fn(slug, ctx)
            est[nome] = 'ok'
            res[nome] = f'ok: {r}'
        except Exception as e:
            est[nome] = 'erro'
            res[nome] = f'ERRO: {str(e)[:200]}'
            _alerta(f'[publicar_tudo] {slug} / {nome} FALHOU -> {str(e)[:300]}')
        est['_video_id'] = ctx.get('video_id')
        _salva(slug, est)
    _alerta(_placar(slug, res))                   # FIM: avisa SEMPRE (sucesso inclusive) — J3 nº2
    return res


def main(argv):
    if not argv or argv[0].startswith('--'):
        print('uso: python publicar_tudo.py <slug> [--so youtube_longo,instagram] [--dry]')
        return 0
    slug = argv[0]
    so = set(argv[argv.index('--so') + 1].split(',')) if '--so' in argv else None
    res = publicar_tudo(slug, so, '--dry' in argv)
    print(json.dumps(res, ensure_ascii=False, indent=2))
    falhou = ('_erro_render' in res or '_sem_roteiro' in res
              or any(str(v).startswith('ERRO') for v in res.values()))
    return 1 if falhou else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
