# -*- coding: utf-8 -*-
"""Cluster TTS/voz — extraído de gerar_video.py (Akita pilar 9: arquivo < 500 linhas).

Funções exportadas:
  _provedor_voz(voice) -> 'eleven' | 'google' | 'edge'   — pura, sem I/O
  _tts_eleven(text, voice_id, out_mp3) -> bool            — REST ElevenLabs, nunca lança
  _to_ssml(text) -> str                                   — pura, prosódia SSML
  tts(text, voice, out_mp3, rate=1.0)                     — síntese com fallback encadeado
"""
import sys
import subprocess
from pathlib import Path

ROOT = Path(__file__).parent


def _provedor_voz(voice: str) -> str:
    """Função PURA: classifica a string 'voice' no provedor correto.

    Retornos possíveis:
      'eleven' — prefixo 'eleven:' ou 'el:' (case-insensitive)
      'google' — contém marcador de voz Cloud TTS (Chirp3/Studio/Neural2/Wavenet)
      'edge'   — qualquer outro valor (inclui pt-BR-AntonioNeural, string vazia, etc.)

    Exemplos:
      'eleven:Rachel'                 → 'eleven'
      'el:21m00Tcm4TlvDq8ikWAM'      → 'eleven'
      'pt-BR-Chirp3-HD-Iapetus'       → 'google'
      'pt-BR-Studio-B'                → 'google'
      'pt-BR-AntonioNeural'           → 'edge'
    """
    v = voice.lower()
    if v.startswith('eleven:') or v.startswith('el:'):
        return 'eleven'
    if any(t in voice for t in ('Chirp3', 'Studio', 'Neural2', 'Wavenet')):
        return 'google'
    return 'edge'


TOM_TAG = {'serio': '[serious]', 'quieto': '[quietly]', 'deliberado': '[deliberate]',
           'sombrio': '[somber]', 'neutro': ''}


def _intonar(texto: str, tom: str = 'serio') -> str:
    """Injeta audio tags v3 (intonação) em narração pt-BR plana, IDEMPOTENTE.

    POR QUÊ: o eleven_v3 lê tags como [serious]/[pause] como DIREÇÃO de performance;
    isto garante que TODA narração ElevenLabs saia com entonação mesmo sem diretor
    humano (pedido do André: "sempre enviado"). Se o texto já vem dirigido (tem tags),
    devolve intacto. Tags/boas-práticas: docs oficiais ElevenLabs v3 audio tags (jun/2026).
    """
    import re
    t = (texto or '').strip()
    if not t or re.search(r'\[[A-Za-zÀ-ÿ ]+\]', t):        # vazio ou já dirigido → não mexe
        return t
    tag = TOM_TAG.get(tom, '[serious]')
    if tag:
        t = f'{tag} {t}'
    t = re.sub(r'\.\.\.\s+(?=[A-ZÁÉÍÓÚÂÊÔÃÕ])', ' [pause] ', t)          # reticências dramáticas
    t = re.sub(r'\?\s+(?=[A-ZÁÉÍÓÚÂÊÔÃÕ])', '? [pause] ', t)            # pergunta retórica
    m = re.search(r'^\[[^\]]+\]\s+([^.!?]{1,45}\.)\s+(?=[A-ZÁÉÍÓÚÂÊÔÃÕ])', t)  # gancho curto de abertura
    if m and len(m.group(1).split()) <= 6:
        t = t[:m.end(1)] + ' [pause]' + t[m.end(1):]
    return re.sub(r'  +', ' ', t).strip()


def _tts_eleven(text: str, voice_id: str, out_mp3: str) -> bool:
    """Chama a API ElevenLabs TTS (REST, modelo eleven_v3 c/ audio tags, saída mp3_44100_128).

    Lê a chave em ordem de prioridade:
      1. variável de ambiente ELEVENLABS_API_KEY
      2. arquivo .secrets/elevenlabs_key.txt

    Se a chave estiver AUSENTE ou VAZIA, imprime aviso e retorna False (sem chamar
    a rede) — a lógica de fallback fica em tts(). Mesma filosofia soberana do projeto.

    Retorna True em caso de sucesso, False em qualquer falha (ausência de chave,
    erro de rede, status != 200). Nunca lança exceção — nunca quebra o build.

    ATENÇÃO: a chamada real gasta créditos ElevenLabs. NÃO use sem autorização de
    gasto e sem a chave configurada. Ver pendência em PENDENTE.md / resumo do PR.
    """
    import os

    # 1. Obter chave
    chave = os.environ.get('ELEVENLABS_API_KEY', '').strip()
    if not chave:
        try:
            chave = (ROOT / '.secrets' / 'elevenlabs_key.txt').read_text(encoding='utf-8').strip()
        except (FileNotFoundError, OSError):
            chave = ''

    if not chave:
        print('  [aviso] ElevenLabs sem chave -> rota de fuga ativada')
        return False

    # 2. Chamar a API (REST puro via requests)
    url = f'https://api.elevenlabs.io/v1/text-to-speech/{voice_id}'
    payload = {
        'text': _intonar(text),            # SEMPRE com audio tags de intonação (v3); idempotente
        'model_id': 'eleven_v3',           # v3 = modelo que interpreta as audio tags [serious]/[pause]
        'voice_settings': {
            'stability': 0.50,             # modo "Natural": expressivo sem errar
            'similarity_boost': 0.75,
        },
    }
    headers = {
        'xi-api-key': chave,
        'Content-Type': 'application/json',
        'Accept': 'audio/mpeg',
    }
    try:
        import requests as _req
        import json as _json
        resp = _req.post(url, headers=headers, json=payload, timeout=60)
        resp.raise_for_status()
        Path(out_mp3).write_bytes(resp.content)
        try:
            from cost_tracker import record_cost
            chars = len(text)
            record_cost(api='elevenlabs_1k', units=chars / 1000)
        except Exception:
            pass
        return True
    except Exception as _e:
        print(f'  [aviso] ElevenLabs falhou: {str(_e)[:120]}')
        return False


def _to_ssml(text):
    """Direção de prosódia PREMIUM (jun/2026): cadência VARIADA, não metronômica.
    O salto amador→premium é a MICRO-PAUSA DE VÍRGULA — sem ela a lista/oração 'corre'
    e soa robótica; com ela a frase respira e ganha fraseado humano. As pausas são
    diferenciadas por pontuação (cada sinal tem seu peso) e as reticências criam
    suspense. Chirp3-HD/Studio/Neural2 aceitam <break> via SSML.
    NB de orçamento: pausas custam tempo — manter narração ≤ ~52 palavras/cena para
    caber nos 30s/cena do QC (premium pede frase enxuta, não densa)."""
    import html as _html
    t = _html.escape(text, quote=False)              # & < > seguros no XML
    t = t.replace('... ', '…<break time="500ms"/> ')  # reticências → suspense
    t = t.replace('… ', '…<break time="500ms"/> ')
    t = t.replace('? ', '?<break time="560ms"/> ')    # pergunta pousa e respira
    t = t.replace('! ', '!<break time="440ms"/> ')
    t = t.replace('. ', '.<break time="400ms"/> ')    # ponto final: settle pleno
    t = t.replace('; ', ';<break time="300ms"/> ')    # ponto-e-vírgula
    t = t.replace(' — ', ' —<break time="330ms"/> ')  # travessão: pausa dramática
    t = t.replace(', ', ',<break time="150ms"/> ')    # VÍRGULA: micro-pausa de fraseado (o salto premium)
    return f'<speak>{t}</speak>'


def tts(text, voice, out_mp3, rate=1.0):
    """Narração TTS com fallback encadeado (Akita — soberania):

      ElevenLabs (premium, mais humano pt-BR)
        → Google Cloud TTS Chirp3-HD (se voice/credencial permitirem)
          → edge-tts local GRÁTIS (NUNCA falha — a produção nunca para)

    Prefixos de voz ElevenLabs:  'eleven:<voice_id>'  ou  'el:<voice_id>'
    Vozes Google:                 contêm Chirp3 / Studio / Neural2 / Wavenet
    Rota de fuga edge-tts:       qualquer outro valor (ex.: pt-BR-AntonioNeural)
    """
    FUGA_VOZ = 'pt-BR-AntonioNeural'   # voz de fuga: masculina, sóbria (mais próxima do Iapetus)

    provedor = _provedor_voz(voice)

    # --- 1ª opção: ElevenLabs ---
    if provedor == 'eleven':
        voice_id = voice.split(':', 1)[1]   # 'eleven:Rachel' → 'Rachel'
        if _tts_eleven(text, voice_id, str(out_mp3)):
            return
        # ElevenLabs falhou → tenta Google Chirp3-HD (mesmo SSML) antes de cair no edge
        print(f'  [ROTA DE FUGA] ElevenLabs indisponível → tentando Google Chirp3-HD')
        voice = 'pt-BR-Chirp3-HD-Iapetus'
        provedor = 'google'

    # --- 2ª opção: Google Cloud TTS ---
    if provedor == 'google':
        import time as _time
        for _tentativa in range(2):
            try:
                import tts_gcloud
                if tts_gcloud.synth(text, voice, str(out_mp3), rate=rate, ssml=_to_ssml(text)):
                    return
            except Exception as _e:
                print(f'  [aviso] Cloud TTS tentativa {_tentativa + 1}/2: {str(_e)[:100]}')
            _time.sleep(2)
        print(f'  [ROTA DE FUGA] Cloud TTS indisponível → voz grátis local edge-tts ({FUGA_VOZ})')
        voice = FUGA_VOZ

    # --- 3ª opção (e fallback final): edge-tts local GRÁTIS ---
    subprocess.run([sys.executable, '-m', 'edge_tts', '--voice', voice,
                    '--text', text, '--write-media', str(out_mp3)],
                   check=True, capture_output=True)
