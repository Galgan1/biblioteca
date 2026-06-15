# -*- coding: utf-8 -*-
"""Publicação do VÍDEO LONGO como VÍDEO NATIVO na Página do Facebook "Minuto Real".

Irmão do facebook_post.py — mesma Página (@minutoreal1701), mesmo Page token. A
diferença é a ESTRATÉGIA: em vez de um POST-LINK do YouTube (que o feed do FB
rebaixa, ainda mais por ser link de concorrente), aqui o mp4 sobe como VÍDEO
NATIVO via upload direto. Vídeo nativo tem alcance muito maior e NÃO sofre a
penalização de post-link — por isso o link do acervo pode (discretamente) ir no
fim da própria descrição do vídeo.

NUNCA imprimir/versionar os .secrets.

PRÉ-REQUISITOS (mesmos do facebook_post.py):
  - Página FB vinculada à @minutoreal1701 (Meta Business Suite).
  - App Meta "Minuto Real Poster" com escopo `pages_manage_posts` (publish_video).
  - `.secrets/facebook_page_token.txt` (Page access token) + `.secrets/facebook_page_id.txt`.

ASSETS:
  - Vídeo longo:  videos/<slug>.mp4
  - Roteiro:      videos/roteiros/<slug>.json (titulo, autor, youtube.titulo/tags, cenas[]).

FLUXO (upload SIMPLES, multipart/form-data):
  POST /{page-id}/videos  com  description, title  e o binário do mp4 no campo
  `source` (multipart). Funciona bem para arquivos pequenos — o longo tem ~8MB.
  >>> Para arquivos GRANDES (acima de ~100MB / vídeos longos), trocar este POST
      simples pelo upload RESUMÍVEL em 3 fases (upload_phase=start → transfer →
      finish): `start` devolve upload_session_id + start/end_offset; faz-se um
      `transfer` por chunk (video_file_chunk) avançando o offset; e `finish`
      fecha a sessão. Plugar essa rotina em _post_video_resumivel() abaixo. <<<

Uso:
  python facebook_video.py <slug> [--dry-run]
"""
import sys, json, mimetypes, urllib.request, urllib.error
from pathlib import Path

ROOT = Path(__file__).parent
SH = ROOT / '_shorts'
SEC = ROOT / '.secrets'
GRAPH = 'https://graph.facebook.com/v21.0'
PAGE_TOKEN_FILE = SEC / 'facebook_page_token.txt'
PAGE_ID_FILE = SEC / 'facebook_page_id.txt'
HASHTAGS_BASE = ['livros', 'resumodelivro', 'leitura']
HUB = 'https://www.andregalgani.com.br/biblioteca'

# Acima deste tamanho, o upload simples é arriscado: usar o resumível (ver topo).
LIMITE_SIMPLES = 100 * 1024 * 1024  # 100 MB


def _token():
    if not PAGE_TOKEN_FILE.exists():
        sys.exit(f'[!] {PAGE_TOKEN_FILE} ausente: salve o Page access token (escopo '
                 'pages_manage_posts). Veja o cabeçalho deste arquivo.')
    return PAGE_TOKEN_FILE.read_text(encoding='utf-8').strip()


def _page_id():
    if not PAGE_ID_FILE.exists():
        sys.exit(f'[!] {PAGE_ID_FILE} ausente: salve o id numérico da Página do Facebook.')
    return PAGE_ID_FILE.read_text(encoding='utf-8').strip()


def native_video_caption(cfg):
    """Descrição do vídeo nativo: gancho (do youtube.titulo) + entrega + crédito de
    IA + 3–5 hashtags de nicho. Como vídeo nativo NÃO é penalizado como post-link, o
    link do acervo entra discreto no fim. Fallback inline (não há facebook_copy)."""
    yt = cfg.get('youtube', {})
    gancho = yt.get('titulo', cfg['titulo']).split('|')[0].strip()
    tags = [t.replace(' ', '').lower() for t in yt.get('tags', [])[:2]]
    hs = ' '.join('#' + t for t in (HASHTAGS_BASE + tags))
    return (f"{gancho}\n\n"
            f"As ideias que ficam de \"{cfg['titulo']}\" — destiladas, em ~5 minutos.\n"
            f"Curta a Página e acompanhe — um grande livro destilado por semana.\n"
            f"Narração e arte por IA.\n\n"
            f"O livro inteiro em 1 cheat sheet + PDF, de graça, no acervo: {HUB}\n\n"
            f"{hs}")


def _caption(cfg):
    """Usa facebook_copy.native_video_caption(cfg) se existir; senão o fallback inline."""
    try:
        import facebook_copy  # noqa: local, opcional
        if hasattr(facebook_copy, 'native_video_caption'):
            return facebook_copy.native_video_caption(cfg)
    except Exception:
        pass
    return native_video_caption(cfg)


def _multipart(fields, file_field, filename, file_bytes):
    """Monta um corpo multipart/form-data (boundary manual, stdlib only).

    `fields`: dict de campos de texto. `file_field`: nome do campo do arquivo
    ('source'). Retorna (content_type, body_bytes)."""
    boundary = '----MinutoRealFBVideo' + filename.replace('.', '').replace(' ', '')[:24]
    sep = ('--' + boundary).encode()
    crlf = b'\r\n'
    parts = []
    for name, value in fields.items():
        parts += [sep, crlf,
                  f'Content-Disposition: form-data; name="{name}"'.encode(), crlf, crlf,
                  str(value).encode('utf-8'), crlf]
    ctype = mimetypes.guess_type(filename)[0] or 'video/mp4'
    parts += [sep, crlf,
              (f'Content-Disposition: form-data; name="{file_field}"; '
               f'filename="{filename}"').encode(), crlf,
              f'Content-Type: {ctype}'.encode(), crlf, crlf,
              file_bytes, crlf,
              ('--' + boundary + '--').encode(), crlf]
    body = b''.join(parts)
    return f'multipart/form-data; boundary={boundary}', body


def _post_video_simples(token, pid, mp4_path, description, title):
    """Upload SIMPLES (multipart) para /{page-id}/videos. Retorna a resposta JSON."""
    file_bytes = mp4_path.read_bytes()
    fields = {'access_token': token, 'description': description, 'title': title}
    ctype, body = _multipart(fields, 'source', mp4_path.name, file_bytes)
    req = urllib.request.Request(f'{GRAPH}/{pid}/videos', data=body)
    req.add_header('Content-Type', ctype)
    try:
        return json.load(urllib.request.urlopen(req, timeout=300))
    except urllib.error.HTTPError as e:
        return {'error': {'code': e.code, 'message': e.read().decode()[:300]}}


# def _post_video_resumivel(token, pid, mp4_path, description, title):
#     """TODO: upload resumível em 3 fases para arquivos grandes (ver cabeçalho).
#     start → (loop) transfer por chunk → finish. Plugar aqui quando o longo crescer."""
#     raise NotImplementedError


def postar_video(slug, dry_run=False):
    """Sobe o vídeo longo de <slug> como VÍDEO NATIVO do Facebook.

    Idempotente em _shorts/<slug>_fbvideo_state.json. Com dry_run=True, valida o
    mp4 e os params e PARA antes do POST (não publica)."""
    roteiro = ROOT / 'roteiros' / f'{slug}.json'
    if not roteiro.exists():
        sys.exit(f'[!] roteiro ausente: {roteiro}')
    cfg = json.loads(roteiro.read_text(encoding='utf-8'))

    mp4_path = ROOT / f'{slug}.mp4'
    if not mp4_path.exists():
        sys.exit(f'[!] vídeo longo ausente: {mp4_path}')
    size = mp4_path.stat().st_size

    state_f = SH / f'{slug}_fbvideo_state.json'
    state = json.loads(state_f.read_text()) if state_f.exists() else {}
    if state.get('video_id'):
        print(f'  já no Facebook (vídeo nativo): video_id={state["video_id"]}')
        return state['video_id']

    title = cfg.get('youtube', {}).get('titulo', cfg['titulo'])
    description = _caption(cfg)
    (SH / f'{slug}_fbvideo_caption.md').write_text(description, encoding='utf-8')

    print(f'  slug={slug}')
    print(f'  mp4={mp4_path.name} ({size/1024/1024:.2f} MB)')
    print(f'  title={title}')
    print(f'  description ({len(description)} chars):\n    ' +
          description.replace('\n', '\n    '))

    if size > LIMITE_SIMPLES:
        print(f'  [!] {size/1024/1024:.0f} MB acima do limite do upload simples '
              f'({LIMITE_SIMPLES//1024//1024} MB) — use o upload resumível (ver cabeçalho).')
        if not dry_run:
            sys.exit('[!] abortado: arquivo grande exige upload resumível (não implementado).')

    if dry_run:
        # Valida que os secrets existem (sem imprimi-los) e PARA antes do POST.
        ok = PAGE_TOKEN_FILE.exists() and PAGE_ID_FILE.exists()
        print(f'  secrets presentes: {"sim" if ok else "NAO (token/page_id ausente)"}')
        print('  [dry-run] validado — nenhuma publicação feita.')
        return None

    token, pid = _token(), _page_id()
    print('  enviando vídeo nativo ao Facebook...')
    r = _post_video_simples(token, pid, mp4_path, description, title)
    if 'id' in r:
        print(f'  OK video_id={r["id"]}')
        state['video_id'] = r['id']
        state_f.write_text(json.dumps(state, ensure_ascii=False, indent=1), encoding='utf-8')
        return r['id']
    print(f'  ERRO videos: {r.get("error", r)}')
    return None


if __name__ == '__main__':
    try:  # console Windows (cp1252) não engole emoji da legenda — força UTF-8 no print
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass
    args = sys.argv[1:]
    if not args:
        sys.exit('uso: python facebook_video.py <slug> [--dry-run]')
    slug = args[0]
    dry = '--dry-run' in args[1:]
    postar_video(slug, dry_run=dry)
