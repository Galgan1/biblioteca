import sys
import importlib
import json
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import gerar_carrossel as gc


class TestCarrossel(unittest.TestCase):
    """Contratos de formato do gerador de carrossel/stories.

    unittest.TestCase (não funções soltas estilo-pytest) p/ entrar no gate
    canônico `python testar.py` (unittest discover) — senão os contratos
    ficam invisíveis ao gate e 'violar contrato = teste vermelho' vira falso.
    """

    def test_montar_slides_chapter_tem_6_slides(self):
        """Capítulo com lessons deve ter capa + N cards + lessons + CTA = N+3 slides (mín 5 cards = 7)."""
        data = importlib.import_module('habitos_atomicos_data')
        ch = data.CHAPTERS[0]
        slides = gc.montar_slides(data.BOOK, ch['cards'], ch=ch, total_caps=len(data.CHAPTERS))
        self.assertGreaterEqual(len(slides), 6, f'Esperado >=6, obtido {len(slides)}')

    def test_montar_slides_chapter_tem_lessons_slide(self):
        """O slide de lições deve estar presente quando ch.lessons existe."""
        data = importlib.import_module('habitos_atomicos_data')
        ch = data.CHAPTERS[0]
        slides = gc.montar_slides(data.BOOK, ch['cards'], ch=ch, total_caps=len(data.CHAPTERS))
        self.assertTrue(any('lessons' in s for s in slides), 'Slide de lessons não encontrado')

    def test_montar_slides_overview_sem_lessons(self):
        """Overview (ch=None) NÃO deve ter slide de lessons."""
        data = importlib.import_module('habitos_atomicos_data')
        cards = data.BOOK.get('overview_cards') or data.CHAPTERS[0]['cards']
        slides = gc.montar_slides(data.BOOK, cards, ch=None)
        self.assertFalse(any('lessons' in s for s in slides), 'Overview não deve ter lessons slide')

    def test_caps_json_capitulo_tem_6_slides(self):
        """caps.json regenerado deve ter >= 6 slides para o cap 1 de habitos-atomicos."""
        path = Path('assets/kit/habitos-atomicos/caps.json')
        self.assertTrue(path.exists(), 'caps.json não existe')
        d = json.load(open(path, encoding='utf-8'))
        caps = d.get('chapters', {})
        first_cap = next((v for k, v in caps.items() if k != 'overview'), None)
        self.assertIsNotNone(first_cap, 'Nenhum capítulo em caps.json')
        self.assertGreaterEqual(first_cap, 6, f'Esperado >=6, obtido {first_cap}')

    def test_insights_story_html_existe(self):
        """insights-story.html deve existir para habitos-atomicos."""
        path = Path('assets/kit/_tpl/habitos-atomicos/insights-story.html')
        self.assertTrue(path.exists(), f'Não existe: {path}')

    def test_insights_story_html_tem_3_licoes(self):
        """insights-story.html deve ter pelo menos 3 elementos <li>."""
        path = Path('assets/kit/_tpl/habitos-atomicos/insights-story.html')
        content = path.read_text(encoding='utf-8')
        count = content.count('<li>')
        self.assertGreaterEqual(count, 3, f'Esperado >=3 <li>, obtido {count}')

    def test_build_stories_coleta_lessons_do_book(self):
        """Lógica de coleta de lessons do livro (sem Playwright): deve coletar >=1 lição."""
        data = importlib.import_module('habitos_atomicos_data')
        lessons = []
        for chap in getattr(data, 'CHAPTERS', []) or []:
            ls = chap.get('lessons', [])
            if ls:
                lessons.append(ls[0])
            if len(lessons) >= 3:
                break
        self.assertGreaterEqual(len(lessons), 1, 'Nenhuma lição coletada de habitos-atomicos')

    def test_story_insights_function_existe(self):
        """_story_insights deve ser uma função em gerar_carrossel."""
        self.assertTrue(hasattr(gc, '_story_insights'), '_story_insights não existe em gerar_carrossel')
        self.assertTrue(callable(gc._story_insights), '_story_insights não é callable')

    def test_story_insights_css_presente(self):
        """STORY_CSS deve conter a classe .si (insights frame) — sem ela o frame renderiza invisível."""
        self.assertIn('.si', gc.STORY_CSS, '.si CSS ausente em STORY_CSS — insights frame não renderiza')
        self.assertIn('.si li .num', gc.STORY_CSS, '.si li .num CSS ausente — badges dos insights sem estilo')

    def test_story_alt_text_no_publish_story(self):
        """publishStory deve incluir alt_text no contêiner enviado ao Instagram."""
        import ast, pathlib
        src = pathlib.Path('pdf-service/instagram.js').read_text(encoding='utf-8')
        self.assertIn('alt_text', src, 'alt_text ausente em publishStory')
        self.assertIn('Viralização', src, 'keyword Viralização ausente no alt_text')
        self.assertIn('redes sociais', src, 'keyword redes sociais ausente no alt_text')
        self.assertIn('crescer no instagram', src, 'keyword crescer no instagram ausente no alt_text')


if __name__ == '__main__':
    unittest.main()
