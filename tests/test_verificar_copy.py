# -*- coding: utf-8 -*-
"""Gate de COPY no ponto único (testar.py): as CHECAGENS DURAS (regras inegociáveis do
projeto) são determinísticas e entram aqui. O juiz cross-model (API) NÃO entra no CI —
roda no publish/sob demanda. POR QUÊ: excelência de copy vira exit code no que é objetivo."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import verificar_copy as vc  # noqa: E402


class TestChecaDuro(unittest.TestCase):
    def test_pt_pt_bloqueia(self):
        self.assertTrue(any("pt-PT" in f for f in vc.checa_duro("Vê no ecrã do telemóvel.", "ig")))

    def test_pt_pt_grafia_ct(self):
        self.assertTrue(any("pt-PT" in f for f in vc.checa_duro("Foi um facto actual.", "youtube")))

    def test_pt_br_limpo(self):
        self.assertEqual(vc.checa_duro("Veja na tela do celular. Salve e marque alguém.", "ig"), [])

    def test_ig_link_cru_falha(self):
        self.assertTrue(any("link CRU" in f for f in vc.checa_duro("Acesse https://x.com/y agora", "ig")))

    def test_youtube_link_ok(self):
        # no YouTube o link na descrição É clicável → não falha por isso
        falhas = vc.checa_duro("Resumo: https://www.andregalgani.com.br/biblioteca", "youtube")
        self.assertFalse(any("link CRU" in f for f in falhas))

    def test_amazon_busca_falha(self):
        self.assertTrue(any("BUSCA" in f for f in vc.checa_duro("compre https://amazon.com.br/s?k=livro", "youtube")))

    def test_amazon_produto_ok(self):
        falhas = vc.checa_duro("o livro: https://amazon.com.br/dp/B0123 produto", "youtube")
        self.assertFalse(any("Amazon" in f for f in falhas))

    def test_excesso_hashtags(self):
        muitas = " ".join(f"#tag{i}" for i in range(20))
        self.assertTrue(any("excesso" in f for f in vc.checa_duro("texto " + muitas, "ig")))

    def test_poucas_hashtags_ok(self):
        self.assertFalse(any("hashtag" in f for f in vc.checa_duro("texto #livros #educacao #resumo", "ig")))


if __name__ == "__main__":
    unittest.main()
