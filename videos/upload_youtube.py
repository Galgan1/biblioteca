# -*- coding: utf-8 -*-
"""Faz upload de um vídeo para o YouTube via YouTube Data API v3 (OAuth 2.0).

Pré-requisitos (uma vez):
  1. Google Cloud Console → projeto → habilitar "YouTube Data API v3".
  2. Criar credencial OAuth 2.0 do tipo "App para computador (Desktop)".
  3. Baixar o JSON e salvá-lo em  videos/.secrets/client_secret.json
  4. Adicionar seu e-mail como "usuário de teste" na tela de consentimento OAuth.

Na 1ª execução abre o navegador para você autorizar; o token fica salvo em
.secrets/token.json e os uploads seguintes são automáticos.

Uso:  python upload_youtube.py [video.mp4] [roteiro.json]
"""
import sys, json
try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass
from pathlib import Path
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# force-ssl = escopo amplo (upload + editar/agendar + comentários). O token antigo
# (só-upload) fica preservado em token.json; o novo vive em token_v2.json.
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
ROOT = Path(__file__).parent
SECRETS = ROOT / '.secrets'
CLIENT = SECRETS / 'client_secret.json'
TOKEN = SECRETS / 'token_v2.json'


def get_creds():
    # Via 1 — OAuth client próprio (client_secret.json), se fornecido
    if CLIENT.exists():
        creds = None
        if TOKEN.exists():
            creds = Credentials.from_authorized_user_file(str(TOKEN), SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(str(CLIENT), SCOPES)
                print("→ Abrindo o navegador para autorizar o acesso ao seu canal...")
                creds = flow.run_local_server(port=0)
            SECRETS.mkdir(exist_ok=True)
            TOKEN.write_text(creds.to_json(), encoding='utf-8')
        return creds
    # Via 2 — Application Default Credentials do gcloud (sem Console):
    #   gcloud auth application-default login --scopes=openid,...youtube.upload
    try:
        from google.auth import default as adc_default
        creds, _ = adc_default(scopes=SCOPES)
        if not creds.valid:
            creds.refresh(Request())
        return creds
    except Exception as e:
        sys.exit(f"\n[!] Sem credenciais. Rode uma vez:\n"
                 f"    gcloud auth application-default login --scopes=openid,{SCOPES[0]}\n"
                 f"    (ou salve client_secret.json em {CLIENT})\n    detalhe: {e}\n")


def build_metadata(roteiro_path):
    cfg = json.loads(Path(roteiro_path).read_text(encoding='utf-8'))
    yt = cfg.get('youtube', {})
    conceitos = ' • '.join(c['titulo'] for c in cfg['cenas'] if c.get('tipo') == 'conceito')
    titulo = yt.get('titulo') or f"{cfg['titulo']}, de {cfg['autor']} — Resumo em ~5 min"
    desc = yt.get('descricao') or (
        f"Um resumo essencial de \"{cfg['titulo']}\", de {cfg['autor']}.\n\n"
        f"Princípios abordados: {conceitos}.\n\n"
        f"📚 Biblioteca de André Galgani — https://www.andregalgani.com.br/biblioteca\n\n"
        f"#resumo #livros #{cfg['slug'].replace('-', '')}"
    )
    tags = yt.get('tags') or [cfg['titulo'], cfg['autor'], 'resumo de livro',
                              'resumo', 'livros', 'audiolivro', 'filosofia']
    return {
        'titulo': titulo[:100],
        'descricao': desc[:5000],
        'tags': tags,
        'privacidade': yt.get('privacidade', 'unlisted'),  # unlisted = não público até você revisar
    }


def upload(video_path, roteiro_path):
    cfg = json.loads(Path(roteiro_path).read_text(encoding='utf-8'))
    meta = build_metadata(roteiro_path)
    # Pós-produção API (capítulos): injeta timestamps na descrição se houver timing.
    try:
        import youtube_pos
        meta['descricao'] = youtube_pos.with_chapters(meta['descricao'], cfg)
    except Exception as e:
        print(f"  [aviso] capitulos pulados: {str(e)[:120]}")
    yt = build('youtube', 'v3', credentials=get_creds())
    body = {
        'snippet': {
            'title': meta['titulo'],
            'description': meta['descricao'],
            'tags': meta['tags'],
            'categoryId': '27',  # Education
            'defaultLanguage': 'pt-BR',
        },
        'status': {
            'privacyStatus': meta['privacidade'],
            'selfDeclaredMadeForKids': False,
            # Divulgação obrigatória (política YouTube): narração e visuais gerados por IA
            'containsSyntheticMedia': True,
        },
    }
    media = MediaFileUpload(str(video_path), mimetype='video/mp4', resumable=True, chunksize=1024 * 1024)
    req = yt.videos().insert(part='snippet,status', body=body, media_body=media)
    print(f"Enviando '{meta['titulo']}' ({meta['privacidade']})...")
    resp = None
    while resp is None:
        status, resp = req.next_chunk()
        if status:
            print(f"  {int(status.progress() * 100)}%")
    vid = resp['id']
    print(f"\nOK ✓  https://youtu.be/{vid}   (privacidade: {meta['privacidade']})")
    # Pós-produção API (legendas + playlist temática) — best-effort, nunca derruba o upload.
    try:
        import youtube_pos
        youtube_pos.post_publish(yt, cfg, vid)
    except Exception as e:
        print(f"  [aviso] legendas/playlist puladas: {str(e)[:120]}")
    return vid


if __name__ == '__main__':
    video = sys.argv[1] if len(sys.argv) > 1 else str(ROOT / 'arte-da-guerra.mp4')
    roteiro = sys.argv[2] if len(sys.argv) > 2 else str(ROOT / 'roteiros' / 'arte-da-guerra.json')
    upload(video, roteiro)
