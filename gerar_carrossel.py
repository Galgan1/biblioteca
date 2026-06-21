# -*- coding: utf-8 -*-
"""Gera CARROSSEL de Instagram (slides 1080x1350) de um livro da biblioteca,
na estética "Cheat Sheet Verde" (dark) PREMIUM, a partir do <slug>_data.py.

Fonte = a destilação que já existe (overview_cards ou os cards de um capítulo) —
NÃO o PDF cru. 1 carrossel = o livro em N ideias (ou 1 capítulo). Renderiza com
Playwright (Chromium) reusando os ícones de linha de gerar_livro.py.

Design (premium, jun/2026): fundo em camadas (glow + vinheta + grade de pontos +
grão), moldura tracejada refinada, numeral-fantasma por slide, ícones em selo com
halo, indicador de progresso (dots) e capa "para o dedo". Mesmo DNA verde 152.

Uso:
  python gerar_carrossel.py <slug>                 # carrossel da VISÃO GERAL (overview_cards)
  python gerar_carrossel.py <slug> --cap chNN-...  # carrossel de um capítulo
  python gerar_carrossel.py <slug> --citacao       # cards de citação (frases-bomba)

Saída:
  videos/_carrossel/<slug>_<parte>/01.png ... NN.png   (capa + conceitos + CTA)
  videos/_carrossel/<slug>_citacoes/01.png ... NN.png  (cards de citação)
"""
import sys, os, re, json, importlib
from pathlib import Path

BASE = Path(__file__).parent
sys.path.insert(0, str(BASE))
sys.path.insert(0, str(BASE / 'videos'))
from instagram_post import _afiliado_block  # rodapé único de afiliado/disclosure

from _carousel_css import CSS, STORY_CSS, _FIT_JS
from _carousel_slides import (_svg, _ic, _ghost, _slide, _dots, _kicker_text,
                               _cap_num, _cover, _ed_title, _ed_source, _lead,
                               _concept, _cta, _lessons_slide, _emph, _quote_card)
from _carousel_stories import (_story, _story_teaser, _story_quote,
                                _story_insights, _story_cta)

OUT_ROOT = BASE / 'videos' / '_carrossel'
ROTEIROS = BASE / 'videos' / 'roteiros'
W, H = 1080, 1350

MAX_CONCEITOS = 8   # capa + conceitos + cta <= 10 slides (limite pratico do Instagram)


# ---------- modo citação ----------

def _strip_html(s):
    return re.sub(r'<[^>]+>', '', s).strip()


def _split_sentences(text):
    """Quebra a narração em frases, mantendo travessões/reticências legíveis."""
    parts = re.split(r'(?<=[.!?])\s+', text.strip())
    return [p.strip() for p in parts if p.strip()]


def _score(sent):
    """Pontua o quão 'frase-bomba' é: curta o bastante p/ caber grande,
    com travessão/contraste (caro do tipo 'X não é Y'), sem ser pergunta."""
    n = len(sent)
    if n < 28 or n > 150:
        return -1
    s = 0
    if 40 <= n <= 110:
        s += 3
    if '—' in sent or ' — ' in sent:
        s += 2
    low = sent.lower()
    for kw in (' não é ', 'não há', 'sempre', 'nunca', 'toda', 'todo ', 'a meta', 'o segredo',
               'a régua', 'a lei', 'a porta', 'é a ', ' é o '):
        if kw in low:
            s += 1
    if sent.endswith('?'):
        s -= 3
    if sent.endswith(':'):
        s -= 2
    return s


def _best_quotes(slug, book, data, want=5):
    """Extrai as melhores frases: prioriza as cenas marcadas em `shorts` do
    roteiro; completa com cards do _data.py (campos b/tip). Devolve lista de
    dicts {phrase, attr}."""
    quotes = []
    seen = set()

    def add(phrase):
        phrase = phrase.strip().rstrip(' .')
        key = phrase.lower()[:48]
        if len(phrase) < 24 or len(phrase) > 150 or key in seen:
            return
        seen.add(key)
        quotes.append(phrase)

    rot = ROTEIROS / f'{slug}.json'
    if rot.exists():
        r = json.loads(rot.read_text(encoding='utf-8'))
        cenas = r.get('cenas', [])
        heroes = set(r.get('shorts', []))
        # indexa cenas-conceito por número (kicker "01 · ...") p/ casar com shorts
        ordered = []  # (is_hero, scene)
        ci = 0
        for sc in cenas:
            if sc.get('tipo') == 'conceito':
                ci += 1
                ordered.append((ci in heroes, sc))
            else:
                ordered.append((False, sc))
        # 1) cenas-herói primeiro, melhor frase de cada
        for is_hero, sc in ordered:
            if not is_hero:
                continue
            cands = sorted(_split_sentences(sc.get('narracao', '')), key=_score, reverse=True)
            if cands and _score(cands[0]) >= 0:
                add(cands[0])
        # 2) completa com as melhores frases de qualquer cena
        pool = []
        for _, sc in ordered:
            for s in _split_sentences(sc.get('narracao', '')):
                pool.append(s)
        for s in sorted(pool, key=_score, reverse=True):
            if len(quotes) >= want:
                break
            if _score(s) >= 2:
                add(s)

    # 3) reforço com os cards do _data.py (campo b destacado)
    cards = book.get('overview_cards') or (data.CHAPTERS[0]['cards'] if data.CHAPTERS else [])
    for c in cards:
        if len(quotes) >= want:
            break
        for field in ('tip', 'b'):
            cand = _strip_html(c.get(field, ''))
            # a 'dica' costuma vir como "Modelo mental: <frase>" — fica a frase
            cand = re.sub(r'^[^:]{0,28}:\s*', '', cand)
            for s in _split_sentences(cand):
                if _score(s) >= 3:
                    add(s)
                    break

    return quotes[:want]


def _overview_cards(book, data):
    """Cards do carrossel do LIVRO. Fallback p/ o capitulo 1 — mas AVISA (nao silencioso)."""
    ov = book.get('overview_cards')
    if not ov:
        print(f"[aviso] {book.get('title', '?')}: overview_cards ausente/vazio; "
              f"usando os cards do capitulo 1 como visao geral")
        ov = data.CHAPTERS[0]['cards'] if getattr(data, 'CHAPTERS', None) else []
    return ov


def _clamp_cards(book, cards, ch):
    """Valida/limita os cards antes de renderizar (evita carrossel inpostavel ou raquitico)."""
    cards = cards or []
    rotulo = (ch.get('slug') if ch else 'overview')
    n = len(cards)
    if n == 1:
        print(f"[aviso] {book.get('title','?')}/{rotulo}: so 1 card (carrossel de 3 slides)")
    if n > MAX_CONCEITOS:
        print(f"[aviso] {book.get('title','?')}/{rotulo}: {n} cards excedem o limite do IG; "
              f"usando os {MAX_CONCEITOS} primeiros")
        cards = cards[:MAX_CONCEITOS]
    return cards


def montar_slides(book, cards, ch=None, total_caps=None):
    """FONTE UNICA da sequencia do carrossel: capa -> N conceitos -> [licoes] -> CTA.
    ch=None => carrossel do LIVRO (overview, billboard); ch dado => CAPITULO (detalhe).
    Usada pelo render Python (build) E pelo caminho Node (gerar_dados_carrossel) —
    zero deriva entre eles."""
    cards = _clamp_cards(book, cards, ch)
    n = len(cards)
    has_lessons = bool(ch and ch.get('lessons'))
    total = n + 2 + (1 if has_lessons else 0)
    slides = [_cover(book, n, 1, total, ch=ch, total_caps=total_caps)]
    slides += [_concept(c, i, n, i + 1, total, book, ch) for i, c in enumerate(cards, 1)]
    if has_lessons:
        slides.append(_lessons_slide(book, ch, n + 2, total))
    slides.append(_cta(book, total, total, is_chapter=bool(ch)))
    return slides


def _render(slides, out, scale=2, w=W, h=H, css=None):
    out.mkdir(parents=True, exist_ok=True)
    html = (f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
            f'<style>{css or CSS}</style></head><body>{"".join(slides)}</body></html>')
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={'width': w, 'height': h}, device_scale_factor=scale)
        pg.set_content(html, wait_until='networkidle')
        pg.evaluate('document.fonts.ready')
        pg.wait_for_timeout(500)
        # auto-encolhe titulos que estouram a caixa (palavra unica longa: METAMORFOSE,
        # COMUNICACAO, INSUSTENTAVEL...). Duravel: blinda qualquer titulo futuro sem
        # tocar nos que ja cabem. O h1 e flex-item centralizado (encolhe no proprio
        # texto), entao medimos contra a CAIXA DE CONTEUDO do contentor, nao o h1.
        pg.evaluate(_FIT_JS)
        paths = []
        for i, el in enumerate(pg.query_selector_all('.slide, .story'), 1):
            fp = out / f'{i:02d}.png'
            el.screenshot(path=str(fp))
            paths.append(fp)
        b.close()
    print(f'OK: {len(paths)} slides -> {out}')
    for fp in paths:
        print('  ', fp.name)
    return out


def build(slug, cap=None):
    data = importlib.import_module(slug.replace('-', '_') + '_data')
    book = data.BOOK
    ch = None
    if cap:
        ch = next((c for c in data.CHAPTERS if c['slug'] == cap or c['slug'].startswith(cap)), None)
        if not ch:
            sys.exit(f'[!] capitulo {cap} nao encontrado em {slug}')
        cards = ch['cards']
        part = ch['slug']
    else:
        cards = _overview_cards(book, data)
        part = 'overview'
    if not cards:
        sys.exit(f'[!] {slug}/{part}: sem cards para gerar o carrossel')
    total_caps = len(getattr(data, 'CHAPTERS', []) or [])
    slides = montar_slides(book, cards, ch=ch, total_caps=total_caps)
    n = len(slides) - 2  # nº de conceitos (sem capa/cta), p/ as stories
    out = _render(slides, OUT_ROOT / f'{slug}_{part}')
    qs = _best_quotes(slug, book, data, want=1)
    quote = _strip_html(qs[0]).rstrip(' .') if qs else book.get('subtitle', '')
    _write_stories(out, slug, book, n, quote)
    return out


def _caption_citacao(slug, book, quotes):
    """Legenda premium do carrossel de citações: a frase-bomba como gancho +
    apelo de salvar + CTA em camadas + seguir + afiliado/disclosure + hashtags."""
    gancho = _strip_html(quotes[0]).rstrip(' .') if quotes else book['title']
    tags = [re.sub(r'[^0-9a-z]', '', t.lower().replace(' ', '')) for t in book.get('tags', [])[:2]]
    hs = ' '.join('#' + t for t in (['livros', 'resumodelivro', 'leitura']
                                     + [t for t in tags if t]))
    return (f'"{gancho}"\n— {book["author"]}, em "{book["title"]}"\n\n'
            f'📌 Salve as frases que ficam.\n\n'
            f'📄 Cheat sheet + PDF, de graça, no acervo — link na bio.\n'
            f'🎬 Resumo em vídeo (~5 min) no YouTube.\n\n'
            f'Siga @minutoreal1701 — um grande livro por semana.\n\n'
            f'{_afiliado_block(slug)}\nNarração e arte por IA.\n\n{hs}')


def _write_stories(out, slug, book, n, quote):
    """Roteiro premium de STORIES (3 frames) p/ empurrar o post novo -> YouTube/
    acervo/Amazon. Texto pronto p/ overlay; salvo em stories.txt."""
    titulo = f'{book["header_light"]} {book["header_bold"]}'.strip()
    txt = (f"=== STORIES - {book['title']} ===\n"
           "1 frame por tela (1080x1920 vertical). Texto = overlay na arte; [..] = figurinha.\n\n"
           "FRAME 1 - TEASER\n"
           "NOVO no acervo\n"
           f'"{titulo}" em {n} ideias que ficam.\n'
           "[enquete] Ja conhece esse livro?  Sim / Ainda nao\n"
           "-> Cheat sheet + PDF: toque no link da bio\n\n"
           "FRAME 2 - FRASE-BOMBA\n"
           f'"{quote}"\n'
           f"- {book['author']}\n"
           "[caixa de perguntas] O que isso muda pra voce?\n"
           "-> O livro inteiro em 1 pagina, no acervo (link na bio)\n\n"
           "FRAME 3 - CTA (3 destinos)\n"
           "3 lugares, 1 toque:\n"
           "> Acervo - cheat sheet + PDF (de graca)\n"
           "> YouTube - o resumo em ~5 min\n"
           "> Amazon - o livro (link de afiliado)\n"
           "Tudo no link da bio. Salve e compartilhe.\n")
    (out / 'stories.txt').write_text(txt, encoding='utf-8')
    print('  stories.txt (roteiro de stories premium)')


def build_citacao(slug):
    data = importlib.import_module(slug.replace('-', '_') + '_data')
    book = data.BOOK
    quotes = _best_quotes(slug, book, data, want=5)
    if not quotes:
        sys.exit(f'[!] nenhuma frase forte encontrada para {slug}')
    total = len(quotes)
    slides = [_quote_card(q, book, k, total) for k, q in enumerate(quotes, 1)]
    out = _render(slides, OUT_ROOT / f'{slug}_citacoes')
    cap = _caption_citacao(slug, book, quotes)
    (out / 'caption.txt').write_text(cap, encoding='utf-8')
    print('  caption.txt (legenda com CTA Biblioteca + Amazon + disclosure)')
    _write_stories(out, slug, book, len(quotes), _strip_html(quotes[0]).rstrip(' .'))
    return out


def build_stories(slug, cap=None):
    """Gera frames de story (9:16). cap=None => story do livro; cap=slug_do_cap => story do capitulo."""
    data = importlib.import_module(slug.replace('-', '_') + '_data')
    book = data.BOOK
    if cap:
        ch = next((c for c in getattr(data, 'CHAPTERS', []) if c.get('slug') == cap), None)
        if not ch:
            sys.exit(f'[!] capitulo "{cap}" nao encontrado em {slug}')
        cards = ch['cards']
        lessons = ch.get('lessons', [])
        lessons_title = ch.get('lessons_title', 'O Que Fica')
        out_dir = OUT_ROOT / f'{slug}_{cap}_stories'
    else:
        cards = book.get('overview_cards') or (data.CHAPTERS[0]['cards'] if getattr(data, 'CHAPTERS', None) else [])
        # agrega 1a licao de cada capitulo (max 3)
        lessons = []
        for chap in getattr(data, 'CHAPTERS', []) or []:
            ls = chap.get('lessons', [])
            if ls:
                lessons.append(ls[0])
            if len(lessons) >= 3:
                break
        lessons_title = 'O que voce vai levar'
        out_dir = OUT_ROOT / f'{slug}_stories'
    n = len(cards)
    qs = _best_quotes(slug, book, data, want=1)
    quote = _strip_html(qs[0]).rstrip(' .') if qs else book.get('subtitle', '')
    frames = [_story_teaser(book, n), _story_quote(quote, book)]
    if lessons:
        frames.append(_story_insights(book, lessons, lessons_title))
    frames.append(_story_cta(book))
    out = _render(frames, out_dir, w=1080, h=1920, css=STORY_CSS)
    if not cap:
        _write_stories(out, slug, book, n, quote)
    return out


if __name__ == '__main__':
    args = sys.argv[1:]
    if not args:
        sys.exit('uso: python gerar_carrossel.py <slug> [--cap chNN-... | --citacao | --stories [--cap chNN-...]]')
    slug = args[0]
    if '--citacao' in args:
        build_citacao(slug)
    elif '--stories' in args:
        cap = args[args.index('--cap') + 1] if '--cap' in args else None
        build_stories(slug, cap)
    else:
        cap = args[args.index('--cap') + 1] if '--cap' in args else None
        build(slug, cap)
