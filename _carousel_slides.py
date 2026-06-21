# -*- coding: utf-8 -*-
"""Funções de geração de slides HTML do carrossel de Instagram.

Extraído de gerar_carrossel.py — contém apenas as funções de slide,
sem CSS, orquestradores, funções de story nem render.
"""
import re
import sys
from pathlib import Path

BASE = Path(__file__).parent
sys.path.insert(0, str(BASE))
from gerar_livro import icon  # reaproveita os ícones de linha reais

# Ícones de linha extras (só usados aqui; mantemos gerar_livro.py intocado).
# Mesma gramática visual: viewBox 64, stroke currentColor, traço 3.
_EXTRA = {
    "bookmark": '<path d="M18 10h28v44L32 44 18 54z" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/>',
    "play": '<circle cx="32" cy="32" r="22" stroke="currentColor" stroke-width="3"/><path d="M27 23l16 9-16 9z" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/>',
    "shelf": '<path d="M14 12h36v40H14z" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/><path d="M14 24h36M14 38h36M24 12v12M40 24v14" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>',
    "spark": '<path d="M32 10l5 17 17 5-17 5-5 17-5-17-17-5 17-5z" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/>',
    "arrow": '<path d="M12 32h36M34 18l16 14-16 14" stroke="currentColor" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>',
    "shield": '<path d="M32 8l20 8v13c0 14-9 23-20 27-11-4-20-13-20-27V16z" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/>',
}


def _ic(name):
    """icon() de gerar_livro, com fallback para os ícones extras locais."""
    if name in _EXTRA:
        return ('<div class="card-icon" aria-hidden="true">'
                '<svg viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">'
                + _EXTRA[name] + '</svg></div>')
    return icon(name)


def _svg(name):
    """SVG cru (sem o wrapper .card-icon), p/ usar inline em selos/rodapés."""
    from gerar_livro import ICONS
    inner = ICONS.get(name) or _EXTRA.get(name, '')
    return f'<svg viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">{inner}</svg>'


def _ghost(style, text):
    """Numeral/símbolo-fantasma de fundo. O estilo (posição + tamanho) vai no
    PRÓPRIO div (que é absolute), senão não posiciona."""
    return f'<div class="ghost" style="{style}">{text}</div>'


def _slide(inner, cls='', ghost=''):
    return f'<div class="slide {cls}">{ghost}{inner}</div>'


def _dots(pos, total):
    return ('<div class="dots">'
            + ''.join(f'<i class="{"on" if k == pos else ""}"></i>' for k in range(1, total + 1))
            + '</div>')


def _kicker_text(book):
    """Kicker curto e escaneável (Krug: omita palavras). Tira o prefixo
    'VISÃO GERAL · ' redundante, corta aposto entre parênteses e limita a ~4
    palavras p/ não competir com o título; cai nas tags se vazio."""
    k = book.get('subtitle', '') or ' · '.join(book.get('tags', [])[:3]).upper()
    k = re.sub(r'^\s*VIS[ÃA]O GERAL\s*[·\-—]\s*', '', k, flags=re.IGNORECASE)
    k = re.sub(r'\s*\([^)]*\)', '', k)
    k = re.sub(r'\s{2,}', ' ', k).strip(' ·-—')
    words = k.split()
    if len(words) > 4:
        words = words[:4]
    # nao pendura preposicao/artigo no fim do corte (Krug: evita "... SOCIAL DO")
    _stop = {'de', 'do', 'da', 'dos', 'das', 'e', 'o', 'a', 'os', 'as',
             'em', 'no', 'na', 'com', 'para', 'por', 'que', 'ao', 'à'}
    while len(words) > 2 and words[-1].lower() in _stop:
        words.pop()
    return ' '.join(words).strip()


def _cap_num(ch):
    """Numero do capitulo, lido do sub ('CAPITULO 3: ...') ou do slug ('ch03-...')."""
    if not ch:
        return None
    m = re.match(r'\s*CAP[IÍ]TULO\s*(\d+)', (ch.get('sub') or ''), re.IGNORECASE)
    if m:
        return int(m.group(1))
    m = re.match(r'ch0*(\d+)', ch.get('slug', '') or '')
    return int(m.group(1)) if m else None


def _cover(book, n, pos, total, ch=None, total_caps=None):
    if ch:
        # capa de CAPITULO: deixa explicito que e 1 capitulo + a posicao na serie
        cap = _cap_num(ch)
        if cap and total_caps:
            kicker = f'CAPÍTULO {cap} DE {total_caps}'
        elif cap:
            kicker = f'CAPÍTULO {cap}'
        else:
            kicker = 'CAPÍTULO'
    else:
        kicker = _kicker_text(book)
    kicker_html = f'<div class="kicker">{kicker}</div>' if kicker else ''
    return _slide(
        f'<div class="wordmark"><span class="seal">{_svg("book")}</span>'
        f'<span class="name">Minuto<b>Real</b></span></div>'
        f'{kicker_html}'
        f'<h1><span class="lt">{book["header_light"]}</span> <span class="bd">{book["header_bold"]}</span></h1>'
        f'<div class="author">por {book["author"]}</div>'
        f'<div class="hook"><span class="num">{n}</span>'
        f'<span class="lbl">ideias<br>que <span>ficam</span></span></div>'
        f'<div class="swipe"><span>arrasta</span>'
        f'<span class="arrow">{_svg("arrow")}</span></div>'
        f'{_dots(pos, total)}',
        'cover')


def _ed_title(t, emph=None):
    """Título editorial: realça em itálico verde a palavra-chave CURADA (campo
    `emph` do card). Sem emph → título limpo, sem itálico posicional. (Diretor de Design)"""
    if emph and emph in t:
        return t.replace(emph, f'<em>{emph}</em>', 1)
    return t


def _ed_source(ch):
    """'Capítulo N · <título>' a partir do sub do capítulo."""
    sub = (ch or {}).get('sub', '') if ch else ''
    if not sub:
        return ''
    m = re.match(r'\s*CAP[IÍ]TULO\s*(\d+)\s*[:\-–·]\s*(.+)', sub, re.IGNORECASE)
    if m:
        return f'Capítulo {m.group(1)} &middot; <b>{m.group(2).strip()}</b>'
    return f'<b>{sub.strip()}</b>'


def _lead(b, max_sent=2, cap=240):
    """CONTRATO KRUG (Diretor de Design): o slide de feed é billboard, não página
    de livro. Corta o corpo para a LIÇÃO em 1-2 frases escaneáveis, preservando o
    <strong> (a frase-chave). A prosa inteira vive no site. Enforça o orçamento de
    texto no gerador → densidade não pode regredir."""
    s = re.sub(r'\s+', ' ', b or '').strip()
    parts = re.split(r'(?<=[.!?]) ', s)
    out = ' '.join(parts[:max_sent]).strip()
    if len(out) > cap:
        out = out[:cap].rsplit(' ', 1)[0].rstrip(' .,;:') + '…'
    if out.count('<strong>') > out.count('</strong>'):
        out += '</strong>'
    return out


def _concept(c, i, total_cards, pos, total, book=None, ch=None):
    cls = 'concept' + (' warn' if c.get('warn') else '')
    kicker = ''
    if book:
        kicker = f"{book.get('header_light','')} {book.get('header_bold','')}".strip()
    kicker = kicker or 'MINUTO REAL'
    # corpo com capitular (drop-cap) na 1ª letra visível (tolera tag inicial)
    body = _lead(c['b'], cap=160 if ch is None else 240)  # overview=billboard (Krug); capitulo=detalhe
    mdc = re.match(r'^(\s*(?:<[^>]+>)*)([A-Za-zÀ-ÿ])(.*)$', body, re.DOTALL)
    body_html = (mdc.group(1) + f'<span class="dc">{mdc.group(2)}</span>' + mdc.group(3)) if mdc else body
    # tip vira caixa editorial: rótulo (do <strong>…:</strong>) + corpo
    tip_html = ''
    if c.get('tip'):
        mt = re.match(r'\s*<strong>(.*?)</strong>\s*(.*)', c['tip'], re.DOTALL)
        if mt:
            label = re.sub(r'[:：]\s*$', '', mt.group(1)).strip()
            tipbody = mt.group(2).strip()
        else:
            label, tipbody = ('Cuidado' if c.get('warn') else 'Dica'), c['tip']
        tipic = _svg('shield') if c.get('warn') else _svg('spark')
        tip_html = (f'<div class="ed-tip"><span class="tipic">{tipic}</span>'
                    f'<div class="tiptext"><div class="tiplabel">{label}</div>'
                    f'<div class="tipbody">{tipbody}</div></div></div>')
    return _slide(
        f'<div class="topbar"><span class="brandmark">'
        f'<span class="seal">{_svg("book")}</span>Minuto<b>Real</b></span></div>'
        f'<div class="ed">'
        f'<div class="ed-head"><div class="ed-num">{i}</div>'
        f'<div class="ed-meta"><div class="ed-kicker">{kicker}</div>'
        f'<div class="ed-rule"></div><div class="ed-source">{_ed_source(ch)}</div></div></div>'
        f'<h1 class="ed-title">{_ed_title(c["t"], c.get("emph"))}</h1>'
        f'<p class="ed-body">{body_html}</p>'
        f'{tip_html}'
        f'</div>'
        f'{_dots(pos, total)}',
        cls)


def _cta(book, pos, total, is_chapter=False):
    linha1 = ('<p>Este é só 1 capítulo — o livro <strong>inteiro</strong> em 1 resumo: '
              'cheat sheet + PDF no acervo &mdash; link na bio.</p>') if is_chapter else (
              '<p>O livro inteiro em 1 página: cheat sheet + PDF no <strong>acervo</strong> &mdash; link na bio.</p>')
    return _slide(
        '<div class="big">Gostou?<br><span class="lt">tem mais.</span></div>'
        '<div class="rows">'
        f'<div class="row"><span class="rico">{_svg("shelf")}</span>'
        f'{linha1}</div>'
        f'<div class="row"><span class="rico">{_svg("play")}</span>'
        f'<p>Prefere assistir? Resumo de ~5 min no <strong>YouTube</strong>.</p></div>'
        f'<div class="row"><span class="rico">{_svg("spark")}</span>'
        '<p>Um grande livro destilado por semana. <strong>Siga @minutoreal1701</strong>.</p></div>'
        '</div>'
        f'<div class="save">{_svg("bookmark")}Salve para revisar</div>'
        '<div class="handle">@minutoreal1701</div>'
        f'{_dots(pos, total)}',
        'cta',
        ghost=_ghost('bottom:150px;right:40px;font-size:300px', '+'))


def _lessons_slide(book, ch, pos, total):
    """Slide de lições-chave ao final do carrossel de capítulo."""
    title = ch.get('lessons_title', 'Licoes-Chave')
    lessons = ch.get('lessons', [])
    items_html = ''.join(
        f'<li><span class="lnum">{i}</span>{l}</li>'
        for i, l in enumerate(lessons, 1)
    )
    kicker = f"{book.get('header_light','')}{book.get('header_bold','')}".strip() or 'MINUTO REAL'
    src = _ed_source(ch) if ch else ''
    return _slide(
        f'<div class="topbar"><span class="brandmark">'
        f'<span class="seal">{_svg("book")}</span>Minuto<b>Real</b></span></div>'
        f'<div class="ed">'
        f'<div class="ed-head"><div class="ed-num">{_svg("bookmark")}</div>'
        f'<div class="ed-meta"><div class="ed-kicker">{kicker}</div>'
        f'<div class="ed-rule"></div><div class="ed-source">{src}</div></div></div>'
        f'<h1 class="ed-title">{title}</h1>'
        f'<ul class="lessons-list">{items_html}</ul>'
        '</div>'
        f'{_dots(pos, total)}',
        'lessons')


def _emph(phrase):
    """Realça as palavras-chave em verde: termo entre travessões ou a última
    oração curta. Heurística leve — sem exagero."""
    # destaca o trecho após o último travessão (o 'punch' da frase)
    if '—' in phrase:
        head, _, tail = phrase.rpartition('—')
        if 6 <= len(tail.strip()) <= 60:
            return f'{head.strip()} — <em>{tail.strip()}</em>'
    return phrase


def _quote_card(q, book, k, total):
    foot = (
        '<div class="foot">'
        '<span class="handle">@minutoreal1701</span>'
        f'<span class="cta-min">{_svg("bookmark")}salve esta</span>'
        '</div>')
    attr = f'<div class="attr">{book["author"]}<br><span class="book">{book["title"]}</span></div>'
    qcount = (f'<div class="qcount"><b>{k:02d}</b><span class="sl">/</span>{total:02d}</div>'
              if total > 1 else '')
    return _slide(
        '<div class="qhead"><div class="qmark">&ldquo;</div></div>'
        f'{qcount}'
        f'<div class="phrase">{_emph(q)}</div>'
        f'{attr}{foot}',
        'quote',
        ghost=_ghost('bottom:150px;right:24px;font-size:320px', '&rdquo;'))
