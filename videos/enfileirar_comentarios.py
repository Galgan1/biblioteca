# -*- coding: utf-8 -*-
"""ROTINA: alimenta a fila de comentários da VPS para um vídeo + seus Shorts.

Uso:  python enfileirar_comentarios.py <slug> <video_id_longo> ["pergunta do longo"]

- Longo: comentário = pergunta de engajamento (arg 3 ou genérica) + CTA padrão.
- Shorts: lê _shorts/<slug>_upload_state.json (criado por produzir_shorts.py)
  e enfileira cada um com CTA + link do vídeo-mãe.
- Atualiza fila.json local (merge idempotente) e envia à VPS via scp.
"""

import sys, json, subprocess

try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass
from pathlib import Path

ROOT = Path(__file__).parent
FILA_LOCAL = ROOT / 'fila.json'
VPS = 'root@andregalgani.com.br:/opt/minutoreal/fila.json'
CTA = (
    'Se o resumo valeu seu tempo, o like ajuda o canal — e a inscrição garante o '
    'próximo livro. Toda semana, uma grande obra em minutos.'
)


def main(slug, longo_id, pergunta=None):
    pergunta = pergunta or 'Qual ideia do livro mais ficou com você? 👇'
    itens = [{'id': longo_id, 'comentario': f'{pergunta}\n\n{CTA}'}]
    st = ROOT / '_shorts' / f'{slug}_upload_state.json'
    if st.exists():
        for vid in json.loads(st.read_text()).values():
            itens.append(
                {
                    'id': vid,
                    'comentario': f'{CTA}\n\n📚 Resumo completo: https://youtu.be/{longo_id}',
                }
            )
    fila = json.loads(FILA_LOCAL.read_text(encoding='utf-8')) if FILA_LOCAL.exists() else []
    ja = {i['id'] for i in fila}
    novos = [i for i in itens if i['id'] not in ja]
    fila += novos
    FILA_LOCAL.write_text(json.dumps(fila, ensure_ascii=False, indent=1), encoding='utf-8')
    print(f'fila local: +{len(novos)} (total {len(fila)})')
    r = subprocess.run(['scp', str(FILA_LOCAL), VPS], capture_output=True, text=True)
    print('VPS atualizada ✓' if r.returncode == 0 else f'scp falhou: {r.stderr[:120]}')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
