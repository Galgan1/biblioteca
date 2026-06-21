import sys
import importlib
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import gerar_carrossel as gc


def test_montar_slides_chapter_tem_6_slides():
    """Capítulo com lessons deve ter capa + N cards + lessons + CTA = N+3 slides (mín 5 cards = 7)."""
    data = importlib.import_module('habitos_atomicos_data')
    ch = data.CHAPTERS[0]
    slides = gc.montar_slides(data.BOOK, ch['cards'], ch=ch, total_caps=len(data.CHAPTERS))
    assert len(slides) >= 6, f'Esperado >=6, obtido {len(slides)}'


def test_montar_slides_chapter_tem_lessons_slide():
    """O slide de lições deve estar presente quando ch.lessons existe."""
    data = importlib.import_module('habitos_atomicos_data')
    ch = data.CHAPTERS[0]
    slides = gc.montar_slides(data.BOOK, ch['cards'], ch=ch, total_caps=len(data.CHAPTERS))
    assert any('lessons' in s for s in slides), 'Slide de lessons não encontrado'


def test_montar_slides_overview_sem_lessons():
    """Overview (ch=None) NÃO deve ter slide de lessons."""
    data = importlib.import_module('habitos_atomicos_data')
    cards = data.BOOK.get('overview_cards') or data.CHAPTERS[0]['cards']
    slides = gc.montar_slides(data.BOOK, cards, ch=None)
    assert not any('lessons' in s for s in slides), 'Overview não deve ter lessons slide'


def test_caps_json_capitulo_tem_6_slides():
    """caps.json regenerado deve ter >= 6 slides para o cap 1 de habitos-atomicos."""
    path = Path('assets/kit/habitos-atomicos/caps.json')
    assert path.exists(), 'caps.json não existe'
    d = json.load(open(path, encoding='utf-8'))
    caps = d.get('chapters', {})
    first_cap = next((v for k, v in caps.items() if k != 'overview'), None)
    assert first_cap is not None, 'Nenhum capítulo em caps.json'
    assert first_cap >= 6, f'Esperado >=6, obtido {first_cap}'


def test_insights_story_html_existe():
    """insights-story.html deve existir para habitos-atomicos."""
    path = Path('assets/kit/_tpl/habitos-atomicos/insights-story.html')
    assert path.exists(), f'Não existe: {path}'


def test_insights_story_html_tem_3_licoes():
    """insights-story.html deve ter pelo menos 3 elementos <li>."""
    path = Path('assets/kit/_tpl/habitos-atomicos/insights-story.html')
    content = path.read_text(encoding='utf-8')
    count = content.count('<li>')
    assert count >= 3, f'Esperado >=3 <li>, obtido {count}'


def test_build_stories_coleta_lessons_do_book():
    """Lógica de coleta de lessons do livro (sem Playwright): deve coletar >=1 lição."""
    data = importlib.import_module('habitos_atomicos_data')
    lessons = []
    for chap in getattr(data, 'CHAPTERS', []) or []:
        ls = chap.get('lessons', [])
        if ls:
            lessons.append(ls[0])
        if len(lessons) >= 3:
            break
    assert len(lessons) >= 1, 'Nenhuma lição coletada de habitos-atomicos'


def test_story_insights_function_existe():
    """_story_insights deve ser uma função em gerar_carrossel."""
    assert hasattr(gc, '_story_insights'), '_story_insights não existe em gerar_carrossel'
    assert callable(gc._story_insights), '_story_insights não é callable'
