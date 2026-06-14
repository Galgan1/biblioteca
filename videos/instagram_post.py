# -*- coding: utf-8 -*-
"""Publicação automática de Reels no Instagram via Instagram Graph API. Conta: @minutoreal1701.

Usa o UPLOAD RESUMÁVEL (envia os bytes do mp4 direto, sem precisar hospedar em URL
pública) — o análogo do FILE_UPLOAD que o tiktok_post.py usa. Fluxo de 3 passos da
Graph API: criar contêiner (media_type=REELS, upload_type=resumable) → enviar os bytes
para rupload.facebook.com → publicar (media_publish).

PRÉ-REQUISITOS (passos do Showrunner — NÃO dá para automatizar):
  1. Vincular uma Página do Facebook à conta Creator @minutoreal1701 (no app do IG ou
     no Meta Business Suite).
  2. Criar um app em https://developers.facebook.com → adicionar o produto
     "Instagram Graph API" (ou "Instagram" com Instagram Login).
  3. Solicitar as permissões `instagram_content_publish` (+ `instagram_basic`,
     `pages_show_list`) e submeter o app à APP REVIEW da Meta (gated; é o gargalo de
     tempo — dias a semanas, igual à auditoria do TikTok). Sem isso, só publica em
     conta de teste.
  4. Gerar um token de LONGA DURAÇÃO (60 dias) e descobrir o IG user id (numérico).
     Salvar em `.secrets/`:
        instagram_token.txt    -> o access_token (1 linha)
        instagram_user_id.txt  -> o id numérico da conta IG Business/Creator
     (Opcional, para renovação automática do token de 60 dias:
        instagram_app_id.txt + instagram_app_secret.txt + instagram_token.json)

Depois disso:
  python instagram_post.py <slug>              # posta os Reels dos shorts do livro (idempotente)
  python instagram_post.py file <mp4> "legenda"  # posta um Reel avulso
  python instagram_post.py carousel <slug> [parte] [--publish]  # carrossel de imagens

Stdlib only (urllib). Conteúdo do canal é narrado/ilustrado por IA (perfil já tem o
rótulo "Criador de conteúdo de IA"; a legenda reforça a divulgação).
"""
import sys, json, time, urllib.request, urllib.parse, urllib.error
from pathlib import Path

ROOT = Path(__file__).parent
SH = ROOT / '_shorts'
GRAPH = 'https://graph.facebook.com/v21.0'
RUPLOAD = 'https://rupload.facebook.com/ig-api-upload/v21.0'
SEC = ROOT / '.secrets'
TOKEN_FILE = SEC / 'instagram_token.txt'
TOKEN_JSON = SEC / 'instagram_token.json'
USER_ID_FILE = SEC / 'instagram_user_id.txt'
APP_ID_FILE = SEC / 'instagram_app_id.txt'
APP_SECRET_FILE = SEC / 'instagram_app_secret.txt'
# IG premia 3–5 hashtags de nicho (não 30) — doutrina de distribuicao.md
HASHTAGS_BASE = ['livros', 'resumodelivro', 'leitura']

# Afiliados Amazon (tag andregalgani-20). links.json mapeia slug -> URL.
AFILIADOS = ROOT.parent / 'afiliados' / 'links.json'
BOOKS_JSON = ROOT.parent / 'books.json'
DISCLOSURE = 'Como Associado da Amazon, ganho com compras qualificadas.'


def _amazon_url(slug):
    """URL de afiliado Amazon do livro pelo slug — SÓ link de PRODUTO (/dp/ ou /gp/).
    Lê afiliados/links.json; fallback: campo `amazon` em books.json.
    Link de BUSCA (amazon.com.br/s?k=...) é REJEITADO: não 'monta' no comentário do
    Instagram (não vira card/link limpo). Sem produto válido -> None (a linha é omitida)."""
    cand = None
    try:
        links = json.loads(AFILIADOS.read_text(encoding='utf-8'))
        cand = links.get(slug)
    except (OSError, ValueError):
        pass
    if not cand:
        try:
            books = json.loads(BOOKS_JSON.read_text(encoding='utf-8'))
            for b in books:
                if b.get('slug') == slug and b.get('amazon'):
                    cand = b['amazon']
                    break
        except (OSError, ValueError):
            pass
    # só link de PRODUTO entra na legenda; busca (/s?k=...) é descartada
    if cand and ('/dp/' in cand or '/gp/' in cand):
        return cand
    return None


def _afiliado_block(slug):
    """Rodapé das legendas: link de afiliado Amazon (texto, copiável) +
    disclosure obrigatória. O CTA da Biblioteca/YouTube fica no corpo."""
    url = _amazon_url(slug)
    linhas = []
    if url:
        linhas.append(f'🛒 Comprar (afiliado): {url}')
    linhas.append(DISCLOSURE)
    return '\n'.join(linhas)


def _frases(texto):
    """Quebra um texto em frases limpas (p/ gancho + 1 linha de valor)."""
    import re
    return [s.strip() for s in re.split(r'(?<=[.?!])\s+', (texto or '').strip()) if s.strip()]


def _refresh(tj):
    """Troca o token de 60 dias por outro de 60 dias (fb_exchange_token). Best-effort:
    só roda se houver app_id + app_secret em .secrets. Atualiza os dois arquivos."""
    if not (APP_ID_FILE.exists() and APP_SECRET_FILE.exists()):
        return tj['access_token']
    q = urllib.parse.urlencode({
        'grant_type': 'fb_exchange_token',
        'client_id': APP_ID_FILE.read_text(encoding='utf-8').strip(),
        'client_secret': APP_SECRET_FILE.read_text(encoding='utf-8').strip(),
        'fb_exchange_token': tj['access_token'],
    })
    try:
        r = json.load(urllib.request.urlopen(f'{GRAPH}/oauth/access_token?{q}', timeout=60))
    except urllib.error.HTTPError as e:
        print(f'  [aviso] falha ao renovar token IG: {e.code} {e.read().decode()[:160]}')
        return tj['access_token']
    if 'access_token' not in r:
        return tj['access_token']
    r['_obtained_at'] = int(time.time())
    TOKEN_JSON.write_text(json.dumps(r, ensure_ascii=False, indent=2), encoding='utf-8')
    TOKEN_FILE.write_text(r['access_token'], encoding='utf-8')
    print('  [token IG renovado automaticamente]')
    return r['access_token']


def _token():
    # Token de longa duração (60 dias). Renova ~7 dias antes de expirar, se houver app creds.
    if TOKEN_JSON.exists():
        tj = json.loads(TOKEN_JSON.read_text(encoding='utf-8'))
        if tj.get('access_token') and tj.get('_obtained_at'):
            if time.time() - tj['_obtained_at'] >= tj.get('expires_in', 5184000) - 7 * 86400:
                return _refresh(tj)
            return tj['access_token']
    if not TOKEN_FILE.exists():
        sys.exit(f'[!] token ausente: crie {TOKEN_FILE} com o access_token (permissão '
                 'instagram_content_publish). Veja o cabeçalho deste arquivo.')
    return TOKEN_FILE.read_text(encoding='utf-8').strip()


def _user_id():
    if not USER_ID_FILE.exists():
        sys.exit(f'[!] {USER_ID_FILE} ausente: salve o id numérico da conta IG Business/Creator.')
    return USER_ID_FILE.read_text(encoding='utf-8').strip()


def _get(path, token, fields=None):
    q = urllib.parse.urlencode({'access_token': token, **({'fields': fields} if fields else {})})
    try:
        return json.load(urllib.request.urlopen(f'{GRAPH}{path}?{q}', timeout=60))
    except urllib.error.HTTPError as e:
        return {'error': {'code': e.code, 'message': e.read().decode()[:300]}}


def _post(path, token, params):
    data = urllib.parse.urlencode({**params, 'access_token': token}).encode()
    req = urllib.request.Request(f'{GRAPH}{path}', data=data)
    try:
        return json.load(urllib.request.urlopen(req, timeout=120))
    except urllib.error.HTTPError as e:
        return {'error': {'code': e.code, 'message': e.read().decode()[:300]}}


COVER_OFFSET_MS = 1500   # capa do Reel num frame APÓS o fade-in (~0,45s) — senão IG usa o frame 0 (PRETO)


def post_reel(mp4, caption, share_to_feed=True, thumb_offset=COVER_OFFSET_MS):
    """Publica um mp4 vertical como Reel. Retorna o media_id publicado ou None.
    `thumb_offset` (ms) escolhe o frame de capa — default ~1,5s p/ pular o fade-in preto."""
    token, uid = _token(), _user_id()
    data = Path(mp4).read_bytes()
    size = len(data)
    # 1) cria o contêiner em modo resumável
    cont = _post(f'/{uid}/media', token, {
        'media_type': 'REELS',
        'upload_type': 'resumable',
        'caption': caption,
        'share_to_feed': 'true' if share_to_feed else 'false',
        **({'thumb_offset': str(int(thumb_offset))} if thumb_offset else {}),
    })
    if 'error' in cont or 'id' not in cont:
        print(f'  ERRO container: {cont.get("error", cont)}')
        return None
    cid = cont['id']
    # 2) envia os bytes para o rupload (offset 0, arquivo inteiro)
    up = urllib.request.Request(f'{RUPLOAD}/{cid}', data=data, method='POST',
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
    # 3) espera o processamento e publica
    for _ in range(40):
        st = _get(f'/{cid}', token, fields='status_code').get('status_code')
        if st == 'FINISHED':
            break
        if st in ('ERROR', 'EXPIRED'):
            print(f'  FALHOU processamento: {st}')
            return None
        time.sleep(10)
    pub = _post(f'/{uid}/media_publish', token, {'creation_id': cid})
    if 'id' in pub:
        print(f'  OK media_id={pub["id"]}')
        return pub['id']
    print(f'  ERRO publish: {pub.get("error", pub)}')
    return None


def caption_for(cfg, idx):
    """Legenda premium de Reel: GANCHO (1ª frase, fica antes do 'mais') + 1 linha
    de valor + CTA em camadas (YouTube/acervo) + apelo de salvar/seguir (BAR,
    Marketing 4.0) + afiliado/disclosure + 3–5 hashtags de nicho."""
    frases = _frases(cfg['cenas'][idx].get('narracao', ''))
    gancho = frases[0] if frases else cfg['titulo']
    valor = frases[1] if len(frases) > 1 and len(frases[1]) <= 120 else ''
    corpo = gancho + (f'\n\n{valor}' if valor else '')
    tags = [t.replace(' ', '').lower() for t in cfg.get('youtube', {}).get('tags', [])[:2]]
    hs = ' '.join('#' + t for t in (HASHTAGS_BASE + [t for t in tags if t]))
    return (f"{corpo}\n\n"
            f"Essa é uma das ideias de \"{cfg['titulo']}\".\n"
            f"📄 O livro inteiro em 1 cheat sheet + PDF, de graça, no acervo — link na bio.\n"
            f"🎬 Prefere assistir? O resumo de ~5 min está no YouTube.\n\n"
            f"Salve para aplicar e siga @minutoreal1701 — um grande livro destilado por semana.\n\n"
            f"{_afiliado_block(cfg['slug'])}\n🎬 Narração e arte por IA.\n\n{hs}")


def postar_reels(slug):
    cfg = json.loads((ROOT / 'roteiros' / f'{slug}.json').read_text(encoding='utf-8'))
    state_f = SH / f'{slug}_instagram_state.json'
    state = json.loads(state_f.read_text()) if state_f.exists() else {}
    caps = '\n\n'.join(f'### cena {i}\n{caption_for(cfg, i)}' for i in cfg.get('shorts', []))
    (SH / f'{slug}_instagram_captions.md').write_text(caps, encoding='utf-8')
    for i in cfg.get('shorts', []):
        key = str(i)
        mp4 = SH / f'{slug}_{i:02d}.mp4'
        if key in state:
            print(f'  já no Instagram: cena {i} ({state[key]})'); continue
        if not mp4.exists():
            print(f'  [!] short ausente: {mp4.name}'); continue
        print(f'  postando Reel cena {i}...')
        mid = post_reel(str(mp4), caption_for(cfg, i))
        if mid:
            state[key] = mid
            state_f.write_text(json.dumps(state, ensure_ascii=False, indent=1), encoding='utf-8')


# ----------------------------------------------------------------------------
# CARROSSEL DE IMAGENS
# A Graph API de IMAGEM exige uma URL pública JPEG (PNG não é aceito). Fluxo:
# converte os slides PNG -> JPEG -> hospeda na VPS -> contêineres-filho ->
# contêiner CAROUSEL -> (só com --publish) media_publish.
# ----------------------------------------------------------------------------
CARR = ROOT / '_carrossel'
VPS_HOST = 'root@andregalgani.com.br'
VPS_BASE = '/var/www/andregalgani/biblioteca/_carrossel'
PUB_BASE = 'https://www.andregalgani.com.br/biblioteca/_carrossel'


def _book_for(slug):
    """Importa o BOOK do <slug>_data.py (mesma convenção do gerar_carrossel.py)."""
    import importlib
    root = ROOT.parent  # raiz do projeto, onde vivem os *_data.py
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))
    data = importlib.import_module(slug.replace('-', '_') + '_data')
    return data.BOOK


def caption_carousel(slug):
    """Legenda premium de carrossel: GANCHO (1ª frase da intro) + 1 linha de valor
    + apelo de SALVAR (carrossel é campeão de salvamento) + CTA em camadas +
    seguir + afiliado/disclosure + 3–5 hashtags de nicho."""
    import re
    book = _book_for(slug)
    frases = _frases(book.get('intro') or book.get('description') or '')
    gancho = frases[0] if frases else book['title']
    valor = frases[1] if len(frases) > 1 and len(frases[1]) <= 140 else ''
    corpo = gancho + (f'\n\n{valor}' if valor else '')
    tags = [re.sub(r'[^0-9a-z]', '', t.lower().replace(' ', '')) for t in book.get('tags', [])[:2]]
    hs = ' '.join('#' + t for t in (HASHTAGS_BASE + [t for t in tags if t]))
    return (f"{corpo}\n\n"
            f"Arrasta para o lado: as ideias que ficam de \"{book['title']}\", de {book['author']}.\n"
            f"📌 Salve para não perder.\n\n"
            f"📄 Quer o livro inteiro em 1 página? Cheat sheet + PDF no acervo — link na bio.\n"
            f"🎬 E o resumo em vídeo (~5 min) está no YouTube.\n\n"
            f"Siga @minutoreal1701 — um grande livro destilado por semana.\n\n"
            f"{_afiliado_block(slug)}\nNarração e arte por IA.\n\n{hs}")


def _png_to_jpg(folder):
    """Converte NN.png -> NN.jpg (qualidade 88, RGB). Retorna os .jpg ordenados."""
    from PIL import Image
    jpgs = []
    for png in sorted(folder.glob('[0-9][0-9].png')):
        jpg = png.with_suffix('.jpg')
        with Image.open(png) as im:
            im.convert('RGB').save(jpg, 'JPEG', quality=88)
        jpgs.append(jpg)
    return jpgs


def _scp_host(jpgs, slug, part):
    """Envia os JPEGs para a VPS, chmod 644, e retorna as URLs públicas."""
    import subprocess
    remote_dir = f'{VPS_BASE}/{slug}_{part}'
    subprocess.run(['ssh', VPS_HOST, f'mkdir -p {remote_dir}'], check=True)
    for jpg in jpgs:
        subprocess.run(['scp', '-q', str(jpg), f'{VPS_HOST}:{remote_dir}/{jpg.name}'],
                       check=True)
    subprocess.run(['ssh', VPS_HOST, f'chmod 644 {remote_dir}/*.jpg'], check=True)
    return [f'{PUB_BASE}/{slug}_{part}/{jpg.name}' for jpg in jpgs]


def post_carousel(slug, part='overview', caption=None, publish=False):
    """Publica os slides de videos/_carrossel/<slug>_<part>/ como carrossel no IG.
    Converte PNG->JPEG, hospeda na VPS, monta contêineres-filho + CAROUSEL.
    media_publish SÓ roda com publish=True. Retorna o creation_id (ou media_id)."""
    token, uid = _token(), _user_id()
    folder = CARR / f'{slug}_{part}'
    if not folder.exists():
        print(f'  [!] pasta de slides ausente: {folder}')
        return None
    jpgs = _png_to_jpg(folder)
    if not (2 <= len(jpgs) <= 10):
        print(f'  [!] carrossel precisa de 2 a 10 slides; encontrei {len(jpgs)}')
        return None
    print(f'  {len(jpgs)} slides convertidos para JPEG')
    urls = _scp_host(jpgs, slug, part)
    print(f'  slides hospedados na VPS ({len(urls)} URLs publicas)')
    cap_file = folder / 'caption.txt'
    if caption is not None:
        cap = caption
    elif cap_file.exists():
        cap = cap_file.read_text(encoding='utf-8').strip()
    else:
        cap = caption_carousel(slug)
    # 1) contêineres-filho (um por slide)
    children = []
    for url in urls:
        c = _post(f'/{uid}/media', token, {'image_url': url, 'is_carousel_item': 'true'})
        if 'id' not in c:
            print(f'  ERRO container-filho: {c.get("error", c)}')
            return None
        children.append(c['id'])
    print(f'  {len(children)} conteineres-filho criados')
    # 2) contêiner CAROUSEL
    parent = _post(f'/{uid}/media', token, {
        'media_type': 'CAROUSEL',
        'children': ','.join(children),
        'caption': cap,
    })
    if 'id' not in parent:
        print(f'  ERRO container CAROUSEL: {parent.get("error", parent)}')
        return None
    cid = parent['id']
    print(f'  OK creation_id={cid}')
    if not publish:
        print('  (modo teste: nao publicado; rode com --publish para media_publish)')
        return cid
    # 3) espera o processamento e publica
    for _ in range(40):
        st = _get(f'/{cid}', token, fields='status_code').get('status_code')
        if st == 'FINISHED':
            break
        if st in ('ERROR', 'EXPIRED'):
            print(f'  FALHOU processamento: {st}')
            return None
        time.sleep(5)
    pub = _post(f'/{uid}/media_publish', token, {'creation_id': cid})
    if 'id' in pub:
        print(f'  OK media_id={pub["id"]}')
        return pub['id']
    print(f'  ERRO publish: {pub.get("error", pub)}')
    return None


def post_story(slug, publish=False):
    """Publica os frames de videos/_carrossel/<slug>_stories/ como STORIES (9:16).
    Converte PNG->JPEG, hospeda na VPS (image_url público), e cada frame vira uma
    media STORIES -> media_publish. Story é efêmero (24h). Retorna os media_ids."""
    token, uid = _token(), _user_id()
    folder = CARR / f'{slug}_stories'
    if not folder.exists():
        print(f'  [!] pasta de stories ausente: {folder} '
              f'(rode: python gerar_carrossel.py {slug} --stories)')
        return []
    jpgs = _png_to_jpg(folder)
    if not jpgs:
        print('  [!] nenhum frame de story encontrado')
        return []
    urls = _scp_host(jpgs, slug, 'stories')
    print(f'  {len(jpgs)} frames de story hospedados na VPS')
    ids = []
    for i, url in enumerate(urls, 1):
        cont = _post(f'/{uid}/media', token, {'media_type': 'STORIES', 'image_url': url})
        if 'id' not in cont:
            print(f'  ERRO container story {i}: {cont.get("error", cont)}')
            continue
        cid = cont['id']
        if not publish:
            print(f'  (teste) frame {i} creation_id={cid}')
            ids.append(cid)
            continue
        ok = True
        for _ in range(30):
            st = _get(f'/{cid}', token, fields='status_code').get('status_code')
            if st in (None, 'FINISHED'):
                break
            if st in ('ERROR', 'EXPIRED'):
                print(f'  FALHOU processamento story {i}: {st}')
                ok = False
                break
            time.sleep(4)
        if not ok:
            continue
        pub = _post(f'/{uid}/media_publish', token, {'creation_id': cid})
        if 'id' in pub:
            print(f'  OK story {i} media_id={pub["id"]}')
            ids.append(pub['id'])
        else:
            print(f'  ERRO publish story {i}: {pub.get("error", pub)}')
    return ids


if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) >= 3 and args[0] == 'file':
        post_reel(args[1], args[2])
    elif args and args[0] == 'carousel' and len(args) >= 2:
        rest = [a for a in args[1:] if a != '--publish']
        publish = '--publish' in args
        slug = rest[0]
        part = rest[1] if len(rest) >= 2 else 'overview'
        post_carousel(slug, part, publish=publish)
    elif args and args[0] == 'story' and len(args) >= 2:
        publish = '--publish' in args
        rest = [a for a in args[1:] if a != '--publish']
        post_story(rest[0], publish=publish)
    elif len(args) == 1:
        postar_reels(args[0])
    else:
        sys.exit('uso: python instagram_post.py <slug>  |  '
                 'python instagram_post.py file <mp4> "legenda"  |  '
                 'python instagram_post.py carousel <slug> [parte] [--publish]  |  '
                 'python instagram_post.py story <slug> [--publish]')
