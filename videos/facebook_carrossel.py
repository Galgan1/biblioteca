# -*- coding: utf-8 -*-
"""Publicação de CARROSSEL DE FOTOS NATIVO na Página do Facebook "Minuto Real".

Irmão do facebook_post.py — reusa os slides já gerados para o Instagram
(videos/_carrossel/<slug>_<variante>/NN.png|jpg). Conteúdo NATIVO (as fotos ficam
hospedadas na própria Página) tem muito mais alcance que um post-link do YouTube,
porque o feed do FB privilegia mídia que mantém o usuário na plataforma.

Reaproveita as mesmas credenciais e convenções do irmão:
  - Graph API v21.0;
  - `_token()`  -> .secrets/facebook_page_token.txt (escopo pages_manage_posts);
  - `_page_id()`-> .secrets/facebook_page_id.txt;
  - estado idempotente em _shorts/<slug>_fbcarrossel_state.json.
NUNCA imprimir/logar/versionar nada de .secrets/.

FLUXO de carrossel de fotos no FB (2 passos):
  1. Para CADA imagem: POST /{page-id}/photos com published=false + o binário da
     foto (multipart/form-data) -> retorna o `id` (media_fbid) da foto não publicada.
  2. POST /{page-id}/feed com `message` + `attached_media` (JSON com os media_fbid)
     -> cria UM post de feed com todas as fotos como carrossel nativo.

Uso:
  python facebook_carrossel.py <slug> [--variante overview] [--dry-run]
"""
import sys, json, mimetypes, urllib.request, urllib.parse, urllib.error
from pathlib import Path

ROOT = Path(__file__).parent
SH = ROOT / '_shorts'
SEC = ROOT / '.secrets'
CARR = ROOT / '_carrossel'
GRAPH = 'https://graph.facebook.com/v21.0'
PAGE_TOKEN_FILE = SEC / 'facebook_page_token.txt'
PAGE_ID_FILE = SEC / 'facebook_page_id.txt'
HASHTAGS_BASE = ['livros', 'resumodelivro', 'leitura']


def _token():
    if not PAGE_TOKEN_FILE.exists():
        sys.exit(f'[!] {PAGE_TOKEN_FILE} ausente: salve o Page access token (escopo '
                 'pages_manage_posts). Veja o cabeçalho do facebook_post.py.')
    return PAGE_TOKEN_FILE.read_text(encoding='utf-8').strip()


def _page_id():
    if not PAGE_ID_FILE.exists():
        sys.exit(f'[!] {PAGE_ID_FILE} ausente: salve o id numérico da Página do Facebook.')
    return PAGE_ID_FILE.read_text(encoding='utf-8').strip()


def _post(path, token, params):
    """POST application/x-www-form-urlencoded (igual ao irmão). Para o /feed final."""
    data = urllib.parse.urlencode({**params, 'access_token': token}).encode()
    req = urllib.request.Request(f'{GRAPH}{path}', data=data)
    try:
        return json.load(urllib.request.urlopen(req, timeout=120))
    except urllib.error.HTTPError as e:
        return {'error': {'code': e.code, 'message': e.read().decode()[:300]}}


def _post_multipart(path, token, fields, file_field, file_path):
    """POST multipart/form-data com UM arquivo binário, montado à mão.

    A stdlib (urllib) não tem cliente multipart, e a Graph API exige
    multipart/form-data para enviar o binário da foto em /{page-id}/photos.
    Por isso montamos o corpo manualmente: um boundary único separa cada parte;
    campos de texto viram partes 'Content-Disposition: form-data; name="x"' e o
    arquivo ganha também filename + Content-Type. Cada linha do protocolo termina
    em CRLF (\\r\\n), exigência do multipart.
    """
    boundary = '----MinutoRealFBCarrossel7f3a9b'  # qualquer string que não apareça nos dados
    crlf = '\r\n'
    parts = []
    full_fields = {**fields, 'access_token': token, 'published': 'false'}
    for name, value in full_fields.items():
        parts.append(f'--{boundary}{crlf}'
                     f'Content-Disposition: form-data; name="{name}"{crlf}{crlf}'
                     f'{value}{crlf}')
    # parte do arquivo: precisa de filename + Content-Type para o FB tratar como imagem
    fp = Path(file_path)
    ctype = mimetypes.guess_type(fp.name)[0] or 'application/octet-stream'
    head = (f'--{boundary}{crlf}'
            f'Content-Disposition: form-data; name="{file_field}"; filename="{fp.name}"{crlf}'
            f'Content-Type: {ctype}{crlf}{crlf}')
    # corpo = (campos de texto em utf-8) + (cabeçalho do arquivo) + (bytes crus) + fecho
    body = b''.join(p.encode('utf-8') for p in parts)
    body += head.encode('utf-8')
    body += fp.read_bytes()
    body += f'{crlf}--{boundary}--{crlf}'.encode('utf-8')

    req = urllib.request.Request(f'{GRAPH}{path}', data=body)
    req.add_header('Content-Type', f'multipart/form-data; boundary={boundary}')
    try:
        return json.load(urllib.request.urlopen(req, timeout=180))
    except urllib.error.HTTPError as e:
        return {'error': {'code': e.code, 'message': e.read().decode()[:300]}}


def _slides(slug, variante):
    """Lista ordenada dos slides NN.png/NN.jpg da pasta da variante. None se ausente."""
    pasta = CARR / f'{slug}_{variante}'
    if not pasta.is_dir():
        return None, pasta
    imgs = sorted(p for p in pasta.iterdir()
                  if p.suffix.lower() in ('.png', '.jpg', '.jpeg') and p.stem.isdigit())
    return imgs, pasta


def carousel_caption(cfg):
    """Legenda do carrossel: gancho + entrega + crédito de IA + hashtags de nicho.
    SEM link externo no corpo (conteúdo nativo; o funil vai pela bio/Página)."""
    yt = cfg.get('youtube', {})
    gancho = yt.get('titulo', cfg['titulo']).split('|')[0].strip()
    autor = cfg.get('autor', '')
    tags = [t.replace(' ', '').lower() for t in yt.get('tags', [])[:2]]
    hs = ' '.join('#' + t for t in (HASHTAGS_BASE + tags))
    credito_obra = f'"{cfg["titulo"]}"' + (f', de {autor}' if autor else '')
    return (f"{gancho}\n\n"
            f"As ideias que ficam de {credito_obra} — destiladas, slide a slide.\n"
            f"Arraste para o lado. 👉\n\n"
            f"Curta a Página e acompanhe — um grande livro destilado por semana.\n"
            f"Narração e arte por IA.\n\n{hs}")


def _load_caption(cfg):
    """Usa facebook_copy.carousel_caption(cfg) se o módulo existir; senão, fallback."""
    try:
        import facebook_copy  # opcional; só existe se a lane de copy o criar
        if hasattr(facebook_copy, 'carousel_caption'):
            return facebook_copy.carousel_caption(cfg)
    except ImportError:
        pass
    return carousel_caption(cfg)


def postar_carrossel(slug, variante='overview', dry_run=False):
    """Sobe os slides como fotos não publicadas e cria o post de carrossel nativo.

    Idempotente em _shorts/<slug>_fbcarrossel_state.json: a chave é a variante.
    Em dry_run, valida arquivos/params e PARA antes de qualquer POST mutante.
    """
    roteiro = ROOT / 'roteiros' / f'{slug}.json'
    if not roteiro.exists():
        sys.exit(f'[!] roteiro ausente: {roteiro}')
    cfg = json.loads(roteiro.read_text(encoding='utf-8'))

    imgs, pasta = _slides(slug, variante)
    if imgs is None:
        sys.exit(f'[!] pasta de slides ausente: {pasta}')
    if not imgs:
        sys.exit(f'[!] nenhum slide NN.png/NN.jpg em {pasta}')
    if len(imgs) > 10:
        print(f'  [aviso] {len(imgs)} slides; o FB exibe no máx. ~10 no carrossel.')

    state_f = SH / f'{slug}_fbcarrossel_state.json'
    state = json.loads(state_f.read_text(encoding='utf-8')) if state_f.exists() else {}
    if variante in state:
        print(f'  já no Facebook: {slug}/{variante} (post {state[variante]})'); return

    msg = _load_caption(cfg)

    print(f'  carrossel FB: {slug} / {variante}')
    print(f'  pasta: {pasta}')
    print(f'  slides ({len(imgs)}): ' + ', '.join(p.name for p in imgs))
    print('  --- legenda ---')
    print(msg)
    print('  ---------------')

    if dry_run:
        # valida que as credenciais ao menos existem (sem ler/imprimir o conteúdo)
        cred_ok = PAGE_TOKEN_FILE.exists() and PAGE_ID_FILE.exists()
        print(f'  credenciais .secrets presentes: {cred_ok} '
              '(token+page_id; conteúdo nunca é exibido)')
        print('  [dry-run] validação OK — nenhum POST enviado.')
        return

    # grava a legenda pra auditoria (mesmo padrão do irmão), só fora do dry-run
    (SH / f'{slug}_fbcarrossel_caption.md').write_text(msg, encoding='utf-8')

    token, pid = _token(), _page_id()

    # passo 1: subir cada foto como NÃO publicada -> coletar media_fbid
    fbids = []
    for img in imgs:
        print(f'  upload {img.name}...')
        r = _post_multipart(f'/{pid}/photos', token, {}, 'source', img)
        if 'id' not in r:
            print(f'  ERRO upload {img.name}: {r.get("error", r)}')
            return
        fbids.append(r['id'])
        print(f'    media_fbid={r["id"]}')

    # passo 2: criar o post de feed com todas as fotos anexadas (carrossel nativo)
    attached = json.dumps([{'media_fbid': fid} for fid in fbids])
    r = _post(f'/{pid}/feed', token, {'message': msg, 'attached_media': attached})
    if 'id' not in r:
        print(f'  ERRO feed: {r.get("error", r)}')
        return
    print(f'  OK post_id={r["id"]}')
    state[variante] = r['id']
    state_f.write_text(json.dumps(state, ensure_ascii=False, indent=1), encoding='utf-8')


if __name__ == '__main__':
    # console do Windows (cp1252) quebra ao imprimir emoji da legenda; força UTF-8.
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except (AttributeError, ValueError):
        pass
    args = sys.argv[1:]
    if not args:
        sys.exit('uso: python facebook_carrossel.py <slug> [--variante overview] [--dry-run]')
    slug = args[0]
    variante = 'overview'
    dry_run = False
    rest = args[1:]
    i = 0
    while i < len(rest):
        a = rest[i]
        if a == '--dry-run':
            dry_run = True
        elif a == '--variante':
            i += 1
            if i >= len(rest):
                sys.exit('[!] --variante exige um valor (ex.: overview, citacoes, stories)')
            variante = rest[i]
        elif a.startswith('--variante='):
            variante = a.split('=', 1)[1]
        else:
            sys.exit(f'[!] argumento desconhecido: {a}')
        i += 1
    postar_carrossel(slug, variante=variante, dry_run=dry_run)
