# -*- coding: utf-8 -*-
"""QC — Gate 2 executável (rúbrica de 4 estágios). Estágios PUROS, testáveis sem
render: técnico, conteúdo (pt-PT bloqueante), compliance (afiliado só produto).
Akita: verde = exit code; na dúvida o verificador reprova."""
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]  # .../videos
sys.path.insert(0, str(ROOT))

import qc  # noqa: E402  (import direto — falha real se o módulo não existir)


def _ffmpeg_exe():
    """-> caminho do ffmpeg empacotado, ou None se indisponível."""
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        return None


def _gerar_mp4_tom(destino, alvo_lufs=-14.0):
    """Gera um mp4 com áudio de loudness CONHECIDO: tom 440 Hz normalizado a
    *alvo_lufs* (loudnorm) + vídeo preto 320x240. Fixture do teste de regressão."""
    ff = _ffmpeg_exe()
    subprocess.run(
        [ff, '-y', '-f', 'lavfi', '-i', 'sine=frequency=440:duration=4',
         '-f', 'lavfi', '-i', 'color=c=black:s=320x240:d=4',
         '-af', f'loudnorm=I={alvo_lufs}:TP=-1.5',
         '-c:a', 'aac', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-shortest', destino],
        capture_output=True, text=True)
    return destino


class TestPtPt(unittest.TestCase):
    def test_marcadores_pt_pt_detectados(self):
        m = qc.detectar_pt_pt('O utilizador abriu o ecrã no telemóvel.')
        self.assertIn('utilizador', m)
        self.assertIn('ecrã', m)

    def test_ortografia_pre_acordo(self):
        self.assertIn('facto', qc.detectar_pt_pt('Isto é um facto comprovado.'))
        self.assertIn('acção', qc.detectar_pt_pt('A acção decisiva.'))

    def test_texto_pt_br_limpo(self):
        self.assertEqual(qc.detectar_pt_pt('O usuário abriu a tela no celular.'), [])


class TestConteudo(unittest.TestCase):
    def _cenas(self, **kw):
        base = [
            {'tipo': 'abertura', 'narracao': 'Você lê esse livro errado.'},
            {'tipo': 'conceito', 'narracao': 'A ideia central é simples e poderosa.'},
            {'tipo': 'encerramento', 'narracao': 'Siga para o próximo insight.'},
        ]
        return kw.get('cenas', base)

    def test_pt_pt_bloqueia(self):
        cenas = self._cenas()
        cenas[1]['narracao'] = 'O utilizador entende o facto.'
        falhas, _ = qc.avaliar_conteudo(cenas)
        self.assertTrue(falhas)

    def test_sem_abertura_bloqueia(self):
        cenas = [{'tipo': 'conceito', 'narracao': 'Sem gancho.'}]
        falhas, _ = qc.avaliar_conteudo(cenas)
        self.assertTrue(falhas)

    def test_br_limpo_passa(self):
        falhas, _ = qc.avaliar_conteudo(self._cenas())
        self.assertEqual(falhas, [])


class TestTecnico(unittest.TestCase):
    def test_full_hd_no_alvo_passa(self):
        falhas, _ = qc.avaliar_tecnico(1920, 1080, -14.1, -1.3)
        self.assertEqual(falhas, [])

    def test_resolucao_baixa_bloqueia(self):
        falhas, _ = qc.avaliar_tecnico(1280, 720, -14.0, -1.5)
        self.assertTrue(falhas)

    def test_true_peak_clipando_bloqueia(self):
        falhas, _ = qc.avaliar_tecnico(1920, 1080, -14.0, 0.0)
        self.assertTrue(falhas)

    def test_loudness_fora_do_alvo_avisa_sem_bloquear(self):
        falhas, avisos = qc.avaliar_tecnico(1920, 1080, -20.0, -1.5)
        self.assertEqual(falhas, [])
        self.assertTrue(avisos)


class TestCompliance(unittest.TestCase):
    def test_link_de_produto_valido(self):
        self.assertTrue(qc.link_amazon_valido('https://www.amazon.com.br/dp/B00XYZ'))
        self.assertTrue(qc.link_amazon_valido('https://amzn.to/gp/product/123'))

    def test_link_de_busca_invalido(self):
        self.assertFalse(qc.link_amazon_valido('https://www.amazon.com.br/s?k=1984'))

    def test_compliance_bloqueia_busca(self):
        falhas = qc.avaliar_compliance(['https://www.amazon.com.br/s?k=1984'])
        self.assertTrue(falhas)

    def test_compliance_ok_com_produto(self):
        self.assertEqual(qc.avaliar_compliance(['https://www.amazon.com.br/dp/B00XYZ']), [])


class TestExit(unittest.TestCase):
    def test_verde_sem_falhas(self):
        self.assertEqual(qc.exit_code([]), 0)

    def test_vermelho_com_falha(self):
        self.assertEqual(qc.exit_code(['qualquer falha']), 1)


class TestParseLoudness(unittest.TestCase):
    """Regressão do bug -70: o ebur128 imprime linhas de progresso que começam no
    piso -70 LUFS; a medição antiga pegava a 1ª delas. O parser tem de ler a
    medição do ARQUIVO INTEIRO (JSON do loudnorm), nunca o 1º frame. PURO, sem I/O."""

    # stderr realista: dump do -i (com resolução) + progresso no piso -70 + JSON final.
    _STDERR = (
        'Input #0, mov,mp4,m4a, from \'x.mp4\':\n'
        '  Stream #0:0: Video: h264, yuv420p, 1920x1080 [SAR 1:1 DAR 16:9], 30 fps\n'
        '[Parsed_ebur128_0 @ 1] t: 0.1 TARGET:-23 LUFS  M: -70.0 S: -70.0  I: -70.0 LUFS  LRA: 0.0 LU\n'
        '[Parsed_ebur128_0 @ 1] t: 0.2 TARGET:-23 LUFS  M: -40.0 S: -40.0  I: -70.0 LUFS  LRA: 0.0 LU\n'
        '[Parsed_loudnorm_0 @ 1] \n'
        '{\n'
        '\t"input_i" : "-15.11",\n'
        '\t"input_tp" : "-0.65",\n'
        '\t"input_lra" : "5.90",\n'
        '\t"input_thresh" : "-25.20",\n'
        '\t"output_i" : "-14.00"\n'
        '}\n'
    )

    def test_le_loudness_final_nao_o_piso_70(self):
        self.assertAlmostEqual(qc._parse_loudness(self._STDERR), -15.11, places=2)

    def test_resolucao_extraida(self):
        self.assertEqual(qc._parse_resolucao(self._STDERR), (1920, 1080))

    def test_sem_json_retorna_none(self):
        # arquivo sem áudio: loudnorm não emite JSON -> medição honesta = None (não -70)
        self.assertIsNone(qc._parse_loudness('Stream #0:0: Video: h264 640x480\n'))

    def test_resolucao_ausente_retorna_none(self):
        self.assertEqual(qc._parse_resolucao('sem dimensoes aqui'), (None, None))


@unittest.skipUnless(_ffmpeg_exe(), 'ffmpeg indisponível (imageio_ffmpeg)')
class TestMedirArquivoReal(unittest.TestCase):
    """Roda a medição sobre um mp4 real com loudness CONHECIDO (-14 LUFS) e confirma
    a leitura correta — o teste que prova que o -70 morreu. Akita: verde = exit code."""

    @classmethod
    def setUpClass(cls):
        fd, cls.mp4 = tempfile.mkstemp(suffix='.mp4', prefix='qc_tom_')
        os.close(fd)
        _gerar_mp4_tom(cls.mp4, alvo_lufs=-14.0)

    @classmethod
    def tearDownClass(cls):
        try:
            os.unlink(cls.mp4)
        except OSError:
            pass

    def test_le_loudness_no_alvo_e_nunca_70(self):
        w, h, lufs, _tp = qc.medir_arquivo(self.mp4)
        self.assertIsNotNone(lufs, 'loudness não medido sobre arquivo com áudio')
        self.assertGreater(lufs, -60.0, f'caiu no piso/sentinela -70 ({lufs})')
        self.assertLess(abs(lufs - (-14.0)), 2.0, f'loudness {lufs} longe do alvo -14')
        self.assertEqual((w, h), (320, 240))

    def test_gate_tecnico_nao_avisa_loudness_no_alvo(self):
        _w, _h, lufs, tp = qc.medir_arquivo(self.mp4)
        falhas, avisos = qc.avaliar_tecnico(1920, 1080, lufs, tp)
        self.assertEqual(falhas, [])
        self.assertFalse(any('loudness' in a for a in avisos),
                         f'falso aviso de loudness sobre áudio no alvo: {avisos}')


if __name__ == '__main__':
    unittest.main()
