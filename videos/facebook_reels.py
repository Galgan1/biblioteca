# -*- coding: utf-8 -*-
"""Publicação de Reels NATIVOS na Página do Facebook "Minuto Real" via Graph API.

Irmão do facebook_post.py (que faz post-LINK do vídeo longo). Aqui reusamos os
Shorts 9:16 já produzidos e os publicamos como Reels nativos — a superfície de
maior alcance orgânico do Facebook hoje. Sem link do YouTube no corpo: o FB pune
link externo na legenda; o link vai em comentário (tratado por outro módulo).

Reusa a mesma Página e os mesmos segredos do facebook_post.py:
  - `.secrets/facebook_page_token.txt` -> Page access token (escopo pages_manage_posts).
  - `.secrets/facebook_page_id.txt`    -> id numérico da Página.
NUNCA imprimir/logar/versionar nada de `.secrets/`.

FLUXO de Reels do FB (upload resumível em 3 fases, endpoint /{page-id}/video_reels):
  1. start:  POST upload_phase=start            -> retorna video_id + upload_url
  2. upload: POST do binário .mp4 para a upload_url (host rupload.facebook.com),
             headers Authorization: OAuth <token>, offset: 0, file_size: <bytes>
  3. finish: POST upload_phase=finish, video_id, video_state=PUBLISHED, description

ASSETS:
  - Shorts: `videos/_shorts/<slug>_NN.mp4` (NN = índice da cena, ex: 02, 04, 07, 08).
  - Roteiro: `videos/roteiros/<slug>.json` (titulo, autor, cenas[].titulo, ...).

Uso:
  python facebook_reels.py <slug> [--dry-run]   # posta cada Short do slug como Reel

Stdlib only (urllib). Conteúdo narrado/ilustrado por IA (a legenda divulga isso).
"""
import sys, json, time, urllib.request, urllib.parse, urllib.error
from pathlib import Path
from facebook_base import (
    GRAPH, HASHTAGS_BASE, PAGE_TOKEN_FILE, PAGE_ID_FILE,
    token as _token, page_id as _page_id, post as _post,
)

ROOT = Path(__file__).parent
SH = ROOT / '_shorts'
RUPLOAD = 'https://rupload.facebook.com/video-upload/v21.0'

# Reusa a copy compartilhada se existir (não duplicar legendas); senão, fallback inline.
try:
    import facebook_copy  # função esperada: reel_caption(cfg, cena)
except ImportError:
    facebook_copy = None


def reel_caption(cfg, cena):
    """Legenda de Reel do FB. Usa facebook_copy.reel_caption se existir (copy única);
    senão, fallback simples: gancho + crédito de IA + 3 hashtags de nicho.
    SEM link externo no corpo (o FB pune; o link vai por comentário em outro módulo)."""
    if facebook_copy and hasattr(facebook_copy, 'reel_caption'):
        return facebook_copy.reel_caption(cfg, cena)
    gancho = (cena.get('titulo') or '').strip() or cfg.get('titulo', '')
    livro = cfg.get('titulo', '')
    autor = cfg.get('autor', '')
    cred = f'{livro}' + (f', de {autor}' if autor else '')
    hs = ' '.join('#' + t for t in HASHTAGS_BASE)
    return (f"{gancho}\n\n"
            f"Uma das ideias de \"{cred}\".\n"
            f"Narração e arte por IA.\n\n{hs}")


def _shorts_existentes(slug):
    """Lista os índices NN dos Shorts <slug>_NN.mp4 presentes em _shorts, ordenados."""
    idxs = []
    for f in SH.glob(f'{slug}_[0-9][0-9].mp4'):
        suf = f.stem.rsplit('_', 1)[-1]
        if suf.isdigit():
            idxs.append(int(suf))
    return sorted(idxs)


def post_reel(mp4, description):
    """Publica um mp4 vertical como Reel nativo da Página (3 fases). Retorna o video_id ou None."""
    token, pid = _token(), _page_id()
    data = Path(mp4).read_bytes()
    size = len(data)
    # 1) start: reserva o vídeo e obtém a upload_url
    start = _post(f'/{pid}/video_reels', token, {'upload_phase': 'start'})
    if 'error' in start or 'video_id' not in start:
        print(f'  ERRO start: {start.get("error", start)}')
        return None
    vid = start['video_id']
    upload_url = start.get('upload_url') or f'{RUPLOAD}/{vid}'
    # 2) upload: envia o binário inteiro (offset 0) para o host rupload
    up = urllib.request.Request(upload_url, data=data, method='POST',
                                headers={'Authorization': f'OAuth {token}',
                                         'offset': '0', 'file_size': str(size)})
    try:
        r = json.load(urllib.request.urlopen(up, timeout=600))
    except urllib.error.HTTPError as e:
        print(f'  ERRO upload: {e.code} {e.read().decode()[:200]}')
        return None
    if not r.get('success', True):
        print(f'  ERRO upload: {r}')
        return None
    # 3) finish: publica o Reel com a descrição
    fin = _post(f'/{pid}/video_reels', token, {
        'upload_phase': 'finish',
        'video_id': vid,
        'video_state': 'PUBLISHED',
        'description': description,
    })
    if fin.get('success') or fin.get('id') or fin.get('post_id'):
        print(f'  OK video_id={vid}')
        return vid
    print(f'  ERRO finish: {fin.get("error", fin)}')
    return None


def postar_reels(slug, idxs=None, dry_run=False):
    """Posta cada Short do slug como Reel nativo na Página. Idempotente em
    _shorts/<slug>_fbreels_state.json (não re-posta). idxs=None usa todos os
    <slug>_NN.mp4 existentes. dry_run valida arquivos/legendas e PARA antes de
    qualquer chamada que crie post."""
    roteiro = ROOT / 'roteiros' / f'{slug}.json'
    if not roteiro.exists():
        sys.exit(f'[!] roteiro ausente: {roteiro}')
    cfg = json.loads(roteiro.read_text(encoding='utf-8'))
    cenas = cfg.get('cenas', [])
    state_f = SH / f'{slug}_fbreels_state.json'
    state = json.loads(state_f.read_text(encoding='utf-8')) if state_f.exists() else {}

    if idxs is None:
        idxs = _shorts_existentes(slug)
    if not idxs:
        print(f'  [!] nenhum Short encontrado para {slug} em {SH}')
        return

    # legendas (escritas em disco p/ revisão, como o irmão faz)
    def _cena(i):
        return cenas[i] if 0 <= i < len(cenas) else {}
    caps = '\n\n'.join(f'### cena {i}\n{reel_caption(cfg, _cena(i))}' for i in idxs)
    (SH / f'{slug}_fbreels_captions.md').write_text(caps, encoding='utf-8')

    for i in idxs:
        key = str(i)
        mp4 = SH / f'{slug}_{i:02d}.mp4'
        if key in state:
            print(f'  já no Facebook Reels: cena {i} ({state[key]})')
            continue
        if not mp4.exists():
            print(f'  [!] short ausente: {mp4.name}')
            continue
        cena = _cena(i)
        cap = reel_caption(cfg, cena)
        if dry_run:
            titulo = (cena.get('titulo') or '(sem título)').strip()
            print(f'  [dry-run] cena {i}: {mp4.name} ({mp4.stat().st_size} bytes) '
                  f'-> "{titulo}" | legenda {len(cap)} chars')
            continue
        print(f'  postando Reel cena {i}...')
        vid = post_reel(str(mp4), cap)
        if vid:
            state[key] = vid
            state_f.write_text(json.dumps(state, ensure_ascii=False, indent=1), encoding='utf-8')

    if dry_run:
        print('  [dry-run] OK: arquivos e legendas validados; nada publicado.')


if __name__ == '__main__':
    args = sys.argv[1:]
    dry = '--dry-run' in args
    rest = [a for a in args if a != '--dry-run']
    if len(rest) != 1:
        sys.exit('uso: python facebook_reels.py <slug> [--dry-run]')
    postar_reels(rest[0], dry_run=dry)
