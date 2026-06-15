# -*- coding: utf-8 -*-
"""Gerador de legendas premium para o Facebook — por formato (módulo de copy).

Importado pelos postadores (facebook_reels.py, facebook_carrossel.py,
facebook_video.py). Funções PURAS: nada de rede, nenhum I/O além do roteiro que
o __main__ lê para os exemplos. Cada função recebe `cfg` (dict do roteiro do
livro) e devolve uma string de legenda pronta pro feed da Página.

Doutrina de copy do FB premium aplicada:
  - Hook na 1ª linha (o feed corta em ~125 chars antes do "ver mais").
  - Valor primeiro: a ideia do livro destilada, não "saiu vídeo novo".
  - SEM link externo no corpo (FB rebaixa post-link; o link vai por comentário).
    Exceção: vídeo nativo aceita um link discreto do acervo ao final.
  - 3 a 5 hashtags de nicho no fim.
  - Divulgação de IA obrigatória: "Narração e arte por IA."
  - pt-BR, tom de quem ama livros (não publicitário).
"""

HASHTAGS_BASE = ['livros', 'resumodelivro', 'leitura']
HUB = 'https://www.andregalgani.com.br/biblioteca'
IA = 'Narração e arte por IA.'


def _slugify_tag(s):
    """Vira uma hashtag colada: minúsculas, sem espaços nem acentos."""
    import unicodedata
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode('ascii')
    return ''.join(ch for ch in s.lower() if ch.isalnum())


def hashtags(cfg, n=5):
    """Monta `n` hashtags: base (#livros #resumodelivro #leitura) + tema do
    youtube.tags, sem repetir, na ordem base→tema. Retorna a string já com '#'."""
    tags = list(HASHTAGS_BASE)
    for t in cfg.get('youtube', {}).get('tags', []):
        slug = _slugify_tag(t)
        if slug and slug not in tags:
            tags.append(slug)
        if len(tags) >= n:
            break
    return ' '.join('#' + t for t in tags[:n])


def _conceitos(cfg):
    """Cenas de conceito (as que têm 'kicker'), na ordem do roteiro."""
    return [c for c in cfg.get('cenas', []) if c.get('tipo') == 'conceito']


def _ideia(cena):
    """Frase de uma linha que destila a cena: o título + a 1ª frase da narração."""
    titulo = cena.get('titulo', '').strip()
    narr = cena.get('narracao', '').strip()
    primeira = narr.split('.')[0].strip() if narr else ''
    if titulo and primeira:
        return f'{titulo}: {primeira}.'
    return f'{titulo}.' if titulo else primeira


def reel_caption(cfg, cena=None):
    """Legenda de um Reel — curta, 1 ideia só. Se `cena` for dada, usa o
    título/conceito dela como gancho; senão pega a 1ª cena de conceito."""
    titulo, autor = cfg['titulo'], cfg.get('autor', '')
    if cena is None:
        conc = _conceitos(cfg)
        cena = conc[0] if conc else {}
    gancho = cena.get('titulo', '').strip() or titulo
    ideia = _ideia(cena)
    creditos = f'De "{titulo}"' + (f', de {autor}.' if autor else '.')
    return (f'{gancho}\n\n'
            f'{ideia}\n\n'
            f'{creditos} Uma ideia que muda como você pensa — em segundos.\n\n'
            f'Salve pra lembrar e siga a Página: um grande livro destilado por semana.\n'
            f'{IA}\n\n{hashtags(cfg, 5)}')


def carousel_caption(cfg):
    """Legenda do carrossel — visão geral do livro (gancho + promessa do acervo,
    sem link no corpo: o link vai por comentário)."""
    titulo, autor = cfg['titulo'], cfg.get('autor', '')
    yt = cfg.get('youtube', {})
    gancho = yt.get('titulo', titulo).split('|')[0].strip()
    conc = _conceitos(cfg)
    de = f'"{titulo}"' + (f', de {autor},' if autor else '')
    miolo = (f'{de} em poucos cartões — as ideias que ficam, sem enrolação.'
             if conc else
             f'O essencial de {de} em poucos cartões.')
    return (f'{gancho}\n\n'
            f'{miolo}\n'
            f'Arrasta pro lado 👉 e, no fim, leva o livro inteiro num cheat sheet.\n\n'
            f'O acervo completo (cheat sheet + PDF, de graça) está no link do primeiro comentário.\n'
            f'Curta a Página e acompanhe — um grande livro destilado por semana.\n'
            f'{IA}\n\n{hashtags(cfg, 5)}')


def native_video_caption(cfg):
    """Legenda do vídeo longo NATIVO (upload direto no FB). Vídeo nativo não é
    rebaixado, então pode levar um link discreto do acervo ao final."""
    titulo, autor = cfg['titulo'], cfg.get('autor', '')
    yt = cfg.get('youtube', {})
    gancho = yt.get('titulo', titulo).split('|')[0].strip()
    de = f'"{titulo}"' + (f', de {autor}' if autor else '')
    return (f'{gancho}\n\n'
            f'As ideias que ficam de {de} — destiladas, em poucos minutos.\n'
            f'Aperte o play e veja o resumo completo. 🎬\n\n'
            f'Gostou? O livro inteiro vira um cheat sheet (e PDF) de graça no acervo:\n'
            f'{HUB}\n\n'
            f'Curta a Página e acompanhe — um grande livro destilado por semana.\n'
            f'{IA}\n\n{hashtags(cfg, 5)}')


def text_caption(cfg):
    """Post de texto/imagem com UMA ideia-conceito forte (a 1ª cena de conceito).
    Sem link no corpo: o link vai por comentário."""
    titulo, autor = cfg['titulo'], cfg.get('autor', '')
    conc = _conceitos(cfg)
    cena = conc[0] if conc else {}
    gancho = cena.get('titulo', '').strip() or titulo
    ideia = _ideia(cena)
    creditos = f'— de "{titulo}"' + (f', de {autor}.' if autor else '.')
    return (f'{gancho}\n\n'
            f'{ideia}\n\n'
            f'{creditos}\n'
            f'Esse livro inteiro virou um cheat sheet de graça — link no primeiro comentário.\n'
            f'Curta a Página: um grande livro destilado por semana.\n'
            f'{IA}\n\n{hashtags(cfg, 4)}')


if __name__ == '__main__':
    import json
    import sys
    from pathlib import Path

    try:  # console Windows (cp1252) não engole emoji/setas — força UTF-8 só no demo
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

    cfg = json.loads(
        (Path(__file__).parent / 'roteiros' / 'psicologia-financeira.json')
        .read_text(encoding='utf-8'))

    def show(nome, txt):
        print('=' * 70)
        print(f'## {nome}')
        print('=' * 70)
        print(txt)
        print()

    show('reel_caption(cfg)  [sem cena → 1ª de conceito]', reel_caption(cfg))
    show('carousel_caption(cfg)', carousel_caption(cfg))
    show('native_video_caption(cfg)', native_video_caption(cfg))
    show('text_caption(cfg)', text_caption(cfg))
