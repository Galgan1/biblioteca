# -*- coding: utf-8 -*-
"""Testes das funções PURAS de `youtube_pos.py` (Akita pilar 2 — verde = exit code).

Cobre os contratos do YouTube que uma regressão quebraria silenciosamente:
  (a) timestamp SRT no formato HH:MM:SS,mmm (vírgula como decimal);
  (b) 1º capítulo sempre em 0:00 quando há entradas válidas;
  (c) regra ≥3 capítulos e ≥10s de gap (build_chapters devolve '' quando não atende);
  (d) with_chapters injeta timestamps na descrição sem perder o texto original.

Herméticas: nenhum arquivo lido do disco, nenhuma rede chamada.
"""
import sys
import os
import unittest
from unittest.mock import patch

# Garante que 'videos/' está no path para importar youtube_pos diretamente
_VIDEOS_DIR = os.path.join(os.path.dirname(__file__), '..')
if _VIDEOS_DIR not in sys.path:
    sys.path.insert(0, _VIDEOS_DIR)

import youtube_pos as yt_pos


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

def _cenas_simples():
    """6 cenas com narração, tipos variados e títulos explícitos."""
    return [
        {'tipo': 'abertura',     'kicker': 'Abertura',   'narracao': 'Bem-vindo ao resumo.'},
        {'tipo': 'conceito',     'titulo': 'Ideia 1',    'narracao': 'A primeira ideia é poderosa. Ela transforma tudo.'},
        {'tipo': 'conceito',     'titulo': 'Ideia 2',    'narracao': 'A segunda ideia complementa a primeira.'},
        {'tipo': 'conceito',     'titulo': 'Ideia 3',    'narracao': 'Terceira ideia fecha o arco. É a mais importante.'},
        {'tipo': 'conceito',     'titulo': 'Ideia 4',    'narracao': 'Quarta ideia reforça o argumento central.'},
        {'tipo': 'encerramento', 'kicker': 'Conclusão',  'narracao': 'Até o próximo resumo!'},
    ]


def _durs_simples():
    """Durações para 6 cenas — total ≈ 90s, gap entre cada uma > 10s."""
    return [5.0, 20.0, 20.0, 20.0, 15.0, 10.0]


def _tail():
    return 0.7


# ---------------------------------------------------------------------------
# _srt_ts — formato HH:MM:SS,mmm
# ---------------------------------------------------------------------------

class TestSrtTs(unittest.TestCase):
    """Contrato (a): timestamp SRT com vírgula decimal, dois dígitos em tudo."""

    def test_formato_usa_virgula_nao_ponto(self):
        """O separador decimal deve ser ',' (padrão SRT), nunca '.'."""
        ts = yt_pos._srt_ts(1.500)
        self.assertIn(',', ts)
        self.assertNotIn('.', ts)

    def test_zero_segundos(self):
        self.assertEqual(yt_pos._srt_ts(0.0), '00:00:00,000')

    def test_millisegundos_preservados(self):
        ts = yt_pos._srt_ts(1.234)
        # ms deve ser 234
        self.assertTrue(ts.endswith(',234'), f"Esperado fim ',234', obtido '{ts}'")

    def test_hora_cheia(self):
        ts = yt_pos._srt_ts(3661.0)  # 1h 1min 1s
        self.assertEqual(ts, '01:01:01,000')

    def test_valor_negativo_clampado_a_zero(self):
        self.assertEqual(yt_pos._srt_ts(-5.0), '00:00:00,000')

    def test_ms_maximo_999(self):
        # ms = round(0.9999 * 1000) = 1000 → deve ser travado em 999
        ts = yt_pos._srt_ts(0.9999)
        ms_part = ts.split(',')[1]
        self.assertLessEqual(int(ms_part), 999)

    def test_dois_digitos_em_horas(self):
        ts = yt_pos._srt_ts(7261.0)  # 2h 1min 1s
        h_part = ts.split(':')[0]
        self.assertEqual(len(h_part), 2)


# ---------------------------------------------------------------------------
# _chap_ts — timestamp de capítulo (sem milissegundos)
# ---------------------------------------------------------------------------

class TestChapTs(unittest.TestCase):
    """_chap_ts deve produzir M:SS (sem horas) ou H:MM:SS (com horas)."""

    def test_menos_de_uma_hora_sem_horas(self):
        ts = yt_pos._chap_ts(65)  # 1min5s
        self.assertEqual(ts, '1:05')

    def test_zero(self):
        self.assertEqual(yt_pos._chap_ts(0), '0:00')

    def test_com_horas(self):
        ts = yt_pos._chap_ts(3661)  # 1h1m1s
        self.assertEqual(ts, '1:01:01')

    def test_trunca_fracionario(self):
        # _chap_ts(65.9) deve truncar para 65, produzindo '1:05'
        self.assertEqual(yt_pos._chap_ts(65.9), '1:05')


# ---------------------------------------------------------------------------
# _starts — acumulação de tempos
# ---------------------------------------------------------------------------

class TestStarts(unittest.TestCase):
    """_starts devolve o início acumulado de cada cena."""

    def test_primeiro_e_zero(self):
        starts = yt_pos._starts([5.0, 10.0, 15.0])
        self.assertEqual(starts[0], 0.0)

    def test_acumulacao_correta(self):
        starts = yt_pos._starts([5.0, 10.0, 15.0])
        self.assertEqual(starts, [0.0, 5.0, 15.0])

    def test_lista_vazia(self):
        self.assertEqual(yt_pos._starts([]), [])

    def test_unico_elemento(self):
        self.assertEqual(yt_pos._starts([7.5]), [0.0])


# ---------------------------------------------------------------------------
# build_srt — contratos do bloco SRT gerado
# ---------------------------------------------------------------------------

class TestBuildSrt(unittest.TestCase):
    """Contratos do SRT: blocos numerados, timestamps com vírgula, cenas sem narração puladas."""

    def setUp(self):
        self.cenas = _cenas_simples()
        self.durs = _durs_simples()
        self.tail = _tail()
        self.srt = yt_pos.build_srt(self.cenas, self.durs, self.tail)

    def test_resultado_nao_vazio(self):
        self.assertTrue(self.srt.strip())

    def test_virgula_decimal_em_todos_os_timestamps(self):
        """Cada linha com '-->' deve ter vírgula, nunca ponto, nos timestamps."""
        for linha in self.srt.splitlines():
            if '-->' in linha:
                ts_esq, ts_dir = linha.split('-->')
                self.assertIn(',', ts_esq)
                self.assertIn(',', ts_dir)
                self.assertNotIn('.', ts_esq.strip())
                self.assertNotIn('.', ts_dir.strip())

    def test_blocos_sao_numerados_sequencialmente(self):
        blocos = [b for b in self.srt.strip().split('\n\n') if b.strip()]
        for i, bloco in enumerate(blocos, 1):
            primeira_linha = bloco.strip().splitlines()[0]
            self.assertEqual(primeira_linha.strip(), str(i))

    def test_cena_sem_narracao_e_pulada(self):
        cenas_com_vazio = [
            {'tipo': 'abertura', 'narracao': 'Texto inicial.'},
            {'tipo': 'conceito', 'titulo': 'X', 'narracao': ''},  # sem narração → pula
            {'tipo': 'encerramento', 'narracao': 'Fim.'},
        ]
        durs = [5.0, 10.0, 5.0]
        srt = yt_pos.build_srt(cenas_com_vazio, durs, 0.7)
        blocos = [b for b in srt.strip().split('\n\n') if b.strip()]
        # deve ter 2 blocos, não 3
        self.assertEqual(len(blocos), 2)

    def test_srt_vazio_quando_nenhuma_narracao(self):
        cenas_mudas = [{'tipo': 'conceito', 'titulo': 'X', 'narracao': ''} for _ in range(3)]
        srt = yt_pos.build_srt(cenas_mudas, [5.0, 5.0, 5.0], 0.7)
        self.assertEqual(srt.strip(), '')

    def test_timestamps_crescentes(self):
        """O início de cada cue deve ser menor que seu fim."""
        for linha in self.srt.splitlines():
            if '-->' in linha:
                esq, dir_ = linha.split('-->')
                # converte HH:MM:SS,mmm → segundos para comparar
                def ts2sec(s):
                    s = s.strip().replace(',', '.')
                    h, m, rest = s.split(':')
                    return int(h)*3600 + int(m)*60 + float(rest)
                self.assertLess(ts2sec(esq), ts2sec(dir_))


# ---------------------------------------------------------------------------
# build_chapters — contratos de capítulo
# ---------------------------------------------------------------------------

class TestBuildChapters(unittest.TestCase):
    """Contratos (b) e (c): 1º em 0:00, ≥3 entradas, ≥10s de gap."""

    def test_primeiro_capitulo_em_zero(self):
        """Contrato (b): a primeira linha de capítulo deve começar com '0:00'."""
        out = yt_pos.build_chapters(_cenas_simples(), _durs_simples())
        self.assertTrue(out, "build_chapters devolveu string vazia")
        primeira_linha = out.splitlines()[0]
        self.assertTrue(primeira_linha.startswith('0:00'), f"Primeiro capítulo: '{primeira_linha}'")

    def test_retorna_pelo_menos_tres_capitulos(self):
        """Contrato (c): resultado válido tem ≥3 linhas."""
        out = yt_pos.build_chapters(_cenas_simples(), _durs_simples())
        self.assertGreaterEqual(len(out.splitlines()), 3)

    def test_gap_menor_que_10s_e_pulado(self):
        """Cenas com gap < 10s entre elas não devem aparecer como capítulos distintos."""
        cenas = [
            {'tipo': 'abertura',     'titulo': 'Intro',   'narracao': 'Intro.'},
            {'tipo': 'conceito',     'titulo': 'Rápida',  'narracao': 'Cena rápida.'},  # 3s depois
            {'tipo': 'conceito',     'titulo': 'Normal',  'narracao': 'Cena normal.'},
            {'tipo': 'encerramento', 'titulo': 'Fim',     'narracao': 'Fim.'},
        ]
        durs = [3.0, 3.0, 30.0, 10.0]  # 'abertura' em 0, 'Rápida' em 3s (<10s gap)
        out = yt_pos.build_chapters(cenas, durs)
        if out:
            linhas = out.splitlines()
            # nenhum par de linhas consecutivas deve ter gap < 10s
            def ts_linha_to_sec(l):
                ts = l.split(' ')[0]
                parts = ts.split(':')
                if len(parts) == 2:
                    return int(parts[0])*60 + int(parts[1])
                return int(parts[0])*3600 + int(parts[1])*60 + int(parts[2])
            secs = [ts_linha_to_sec(l) for l in linhas]
            for i in range(1, len(secs)):
                self.assertGreaterEqual(secs[i] - secs[i-1], 10)

    def test_retorna_string_vazia_quando_menos_de_tres_capitulos(self):
        """Menos de 3 capítulos → '' (inválido para o YouTube)."""
        cenas_duas = [
            {'tipo': 'abertura',     'titulo': 'Intro', 'narracao': 'Intro.'},
            {'tipo': 'encerramento', 'titulo': 'Fim',   'narracao': 'Fim.'},
        ]
        durs = [5.0, 60.0]
        out = yt_pos.build_chapters(cenas_duas, durs)
        self.assertEqual(out, '')

    def test_cenas_sem_label_sao_puladas(self):
        """Cenas sem tipo reconhecido e sem título ficam de fora."""
        cenas = [
            {'tipo': 'abertura',  'titulo': '',       'narracao': 'A.'},
            {'tipo': 'conceito',  'titulo': '',       'narracao': 'B.'},  # sem título → pula
            {'tipo': 'conceito',  'titulo': 'Cap 2',  'narracao': 'C.'},
            {'tipo': 'conceito',  'titulo': 'Cap 3',  'narracao': 'D.'},
            {'tipo': 'encerramento', 'titulo': '',    'narracao': 'E.'},
        ]
        durs = [0.1, 15.0, 15.0, 15.0, 10.0]
        out = yt_pos.build_chapters(cenas, durs)
        if out:
            for linha in out.splitlines():
                label = ' '.join(linha.split(' ')[1:])
                self.assertNotEqual(label.strip(), '')

    def test_sem_zero_ponto_zero_retorna_vazio(self):
        """Se a 1ª entrada labelled começa depois de 0.5s, build_chapters devolve ''.

        BUG DOCUMENTADO (não corrigido): build_chapters usa o limiar 0.5s (não 0s)
        para julgar "começa em zero". Isso significa que uma cena que começa em 0.1s
        *sem* label mas seguida de cenas labelled a partir de 0.1s é aceita, pois
        a primeira entrada labelled (ts=0.1) ≤ 0.5 passa o guarda.
        Este teste verifica o comportamento REAL: só retorna '' quando a primeira
        entrada labelled está além de 0.5s.
        """
        cenas_sem_zero = [
            {'tipo': 'conceito', 'titulo': '',  'narracao': 'A.'},   # ts=0, sem label → pula
            {'tipo': 'conceito', 'titulo': '',  'narracao': 'B.'},   # ts=1s, sem label → pula
            {'tipo': 'conceito', 'titulo': 'C', 'narracao': 'C.'},   # ts=2s → 1ª labelled
            {'tipo': 'conceito', 'titulo': 'D', 'narracao': 'D.'},   # ts=17s
            {'tipo': 'conceito', 'titulo': 'E', 'narracao': 'E.'},   # ts=32s
        ]
        # durs: C começa em 0+1+1=2s (> 0.5s) → limiar falha → resultado vazio
        durs = [1.0, 1.0, 15.0, 15.0, 10.0]
        out = yt_pos.build_chapters(cenas_sem_zero, durs)
        self.assertEqual(out, '')

    def test_abertura_vira_introducao(self):
        """Tipo 'abertura' deve gerar label 'Introdução'."""
        out = yt_pos.build_chapters(_cenas_simples(), _durs_simples())
        self.assertIn('Introdução', out)

    def test_encerramento_vira_conclusao(self):
        """Tipo 'encerramento' deve gerar label 'Conclusão'."""
        out = yt_pos.build_chapters(_cenas_simples(), _durs_simples())
        self.assertIn('Conclusão', out)


# ---------------------------------------------------------------------------
# with_chapters — injeta bloco na descrição sem perder texto original
# ---------------------------------------------------------------------------

class TestWithChapters(unittest.TestCase):
    """Contrato (d): with_chapters injeta os capítulos mantendo a descrição intacta."""

    def _cfg_com_timing(self, cenas, durs, tail=0.7):
        """Retorna cfg com load_timing patchado para evitar leitura de disco."""
        return {
            'slug': 'livro-teste',
            'cenas': cenas,
            '_timing': (tail, durs),
        }

    def _patch_load_timing(self, timing_val):
        """Retorna context manager que substitui load_timing pelo valor dado."""
        return patch.object(yt_pos, 'load_timing', return_value=timing_val)

    def test_descricao_original_preservada(self):
        """O texto original deve aparecer intacto no início do resultado."""
        desc = 'Resumo completo do livro Sapiens.'
        cfg = {'slug': 'sapiens', 'cenas': _cenas_simples()}
        with self._patch_load_timing((_tail(), _durs_simples())):
            resultado = yt_pos.with_chapters(desc, cfg)
        self.assertTrue(resultado.startswith(desc))

    def test_bloco_de_capitulos_e_injetado(self):
        """Deve conter '0:00' no resultado quando o bloco é válido."""
        desc = 'Minha descrição.'
        cfg = {'slug': 'sapiens', 'cenas': _cenas_simples()}
        with self._patch_load_timing((_tail(), _durs_simples())):
            resultado = yt_pos.with_chapters(desc, cfg)
        self.assertIn('0:00', resultado)

    def test_sem_timing_retorna_descricao_intacta(self):
        """Sem timing.json (load_timing devolve None), descrição volta sem alteração."""
        desc = 'Descrição original.'
        cfg = {'slug': 'sem-timing', 'cenas': _cenas_simples()}
        with self._patch_load_timing(None):
            resultado = yt_pos.with_chapters(desc, cfg)
        self.assertEqual(resultado, desc)

    def test_nao_duplica_capitulos_se_ja_existem(self):
        """Se a descrição já tem '0:00', with_chapters não injeta nada."""
        desc = 'Descrição.\n\n⏱️ Capítulos\n0:00 Introdução\n1:00 Parte 1'
        cfg = {'slug': 'sapiens', 'cenas': _cenas_simples()}
        with self._patch_load_timing((_tail(), _durs_simples())):
            resultado = yt_pos.with_chapters(desc, cfg)
        self.assertEqual(resultado, desc)

    def test_tamanho_maximo_5000_chars(self):
        """Resultado truncado a 5000 caracteres (limite da API do YouTube)."""
        desc_longa = 'A' * 4900
        cfg = {'slug': 'sapiens', 'cenas': _cenas_simples()}
        with self._patch_load_timing((_tail(), _durs_simples())):
            resultado = yt_pos.with_chapters(desc_longa, cfg)
        self.assertLessEqual(len(resultado), 5000)

    def test_durs_incompativel_com_cenas_retorna_descricao_intacta(self):
        """Se len(durs) != len(cenas), devolve desc sem modificação."""
        desc = 'Texto.'
        cfg = {'slug': 'sapiens', 'cenas': _cenas_simples()}  # 6 cenas
        with self._patch_load_timing((_tail(), [5.0, 10.0])):  # só 2 durs → incompatível
            resultado = yt_pos.with_chapters(desc, cfg)
        self.assertEqual(resultado, desc)


# ---------------------------------------------------------------------------
# playlist_title_for — sem rede
# ---------------------------------------------------------------------------

class TestPlaylistTitleFor(unittest.TestCase):
    """Contratos da função pura playlist_title_for."""

    def test_sem_tema_retorna_padrao(self):
        cfg = {'youtube': {}, 'tema': ''}
        self.assertEqual(
            yt_pos.playlist_title_for(cfg),
            'Minuto Real — Resumos de Livros'
        )

    def test_tema_sem_prefixo_recebe_prefixo(self):
        cfg = {'youtube': {'playlist': 'Finanças'}, 'tema': ''}
        self.assertEqual(yt_pos.playlist_title_for(cfg), 'Minuto Real — Finanças')

    def test_tema_com_prefixo_nao_duplica(self):
        cfg = {'youtube': {'playlist': 'Minuto Real — Filosofia'}, 'tema': ''}
        self.assertEqual(yt_pos.playlist_title_for(cfg), 'Minuto Real — Filosofia')

    def test_fallback_para_tema_do_cfg(self):
        cfg = {'youtube': {}, 'tema': 'Autoconhecimento'}
        self.assertEqual(yt_pos.playlist_title_for(cfg), 'Minuto Real — Autoconhecimento')


if __name__ == '__main__':
    unittest.main()
