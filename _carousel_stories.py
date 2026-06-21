# -*- coding: utf-8 -*-
"""Frames de Story (1080x1920) para Instagram — Minuto Real.

Exporta 5 funções de montagem de story HTML:
  _story          — wrapper base
  _story_teaser   — 1º frame (chamada + número de ideias)
  _story_quote    — 2º frame (frase-bomba)
  _story_insights — 3º frame (lista de lições-chave)
  _story_cta      — 4º frame (call-to-action)
"""
from _carousel_slides import _svg, _ghost, _emph


def _story(inner, cls='', ghost=''):
    return f'<div class="story {cls}">{ghost}{inner}</div>'


def _story_teaser(book, n):
    return _story(
        f'<div class="badge"><span class="seal">{_svg("book")}</span>'
        f'<span class="name">Minuto<b>Real</b></span></div>'
        '<div class="eyebrow">novo · resumo da semana</div>'
        f'<h1><span class="lt">{book["header_light"]}</span><br>'
        f'<span class="bd">{book["header_bold"]}</span></h1>'
        f'<div class="hook"><span class="num">{n}</span> ideias que ficam</div>'
        f'<div class="foot"><span class="tap">toque no link da bio {_svg("arrow")}</span>'
        '<span class="handle">@minutoreal1701</span></div>',
        'st', ghost=_ghost('top:430px;right:70px;font-size:440px', f'{n}'))


def _story_quote(quote, book):
    return _story(
        '<div class="qmark">&ldquo;</div>'
        f'<div class="phrase">{_emph(quote)}</div>'
        f'<div class="attr">{book["author"]}<span class="book">{book["title"]}</span></div>'
        f'<div class="foot"><span class="tap">resumo no YouTube {_svg("play")}</span>'
        '<span class="handle">link na bio</span></div>',
        'sq', ghost=_ghost('bottom:330px;right:40px;font-size:420px', '&rdquo;'))


def _story_insights(book, lessons, title='O que fica'):
    """Frame de insights: lista de lições-chave do livro/capítulo."""
    items = lessons[:3]
    li_html = ''.join(
        f'<li><span class="num">{i}</span>{l}</li>'
        for i, l in enumerate(items, 1)
    )
    return _story(
        f'<div class="eyebrow">{title}</div>'
        f'<ul>{li_html}</ul>'
        f'<div class="foot"><span class="tap">salve para revisar {_svg("bookmark")}</span>'
        '<span class="handle">@minutoreal1701</span></div>',
        'si',
        ghost=_ghost('bottom:380px;right:50px;font-size:500px', str(len(items))))


def _story_cta(book):
    return _story(
        '<div class="big">tudo em<br><span class="lt">1 toque</span></div>'
        '<div class="rows">'
        f'<div class="row"><span class="rico">{_svg("shelf")}</span>'
        '<p>Acervo<span>cheat sheet + PDF (de graça)</span></p></div>'
        f'<div class="row"><span class="rico">{_svg("play")}</span>'
        '<p>YouTube<span>o resumo em ~5 min</span></p></div>'
        f'<div class="row"><span class="rico">{_svg("spark")}</span>'
        '<p>Amazon<span>o livro (link de afiliado)</span></p></div>'
        '</div>'
        f'<div class="foot"><span class="tap">link na bio {_svg("arrow")}</span>'
        '<span class="handle">@minutoreal1701</span></div>',
        'sc', ghost=_ghost('top:430px;left:60px;font-size:400px', '+'))
