# -*- coding: utf-8 -*-
"""Sonoplasta — master −14 LUFS (alvo YouTube). Testa a decisão de mix PURA
(montagem do grafo de áudio) sem tocar ffmpeg/disco. Akita: verde = exit code."""
import subprocess
import sys
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]  # .../videos
sys.path.insert(0, str(ROOT))

try:
    import mixmaster as mm
    _OK = True
except Exception:
    _OK = False


@unittest.skipUnless(_OK, 'mixmaster indisponivel')
class TestDefaultMix(unittest.TestCase):
    def test_loudnorm_ligado_por_padrao(self):
        # o master deve normalizar por padrão (era inerte: ligado mas off por default)
        self.assertTrue(mm.DEFAULT_MIX['loudnorm'])

    def test_alvo_youtube(self):
        self.assertEqual(mm.DEFAULT_MIX['lufs'], -14)
        self.assertEqual(mm.DEFAULT_MIX['tp'], -1.0)


@unittest.skipUnless(_OK, 'mixmaster indisponivel')
class TestBuildAudioFilter(unittest.TestCase):
    def setUp(self):
        self.mix = dict(mm.DEFAULT_MIX)

    def test_voz_so_com_loudnorm(self):
        parts, last = mm._build_audio_filter(self.mix, has_trilha=False, has_efe=False)
        self.assertEqual(parts, ['[1:a]loudnorm=I=-14:TP=-1.0:LRA=11[a]'])
        self.assertEqual(last, '[a]')

    def test_loudnorm_desligado_nao_normaliza(self):
        self.mix['loudnorm'] = False
        parts, last = mm._build_audio_filter(self.mix, has_trilha=False, has_efe=False)
        self.assertEqual(parts, [])
        self.assertEqual(last, '[1:a]')

    def test_trilha_rebaixada_e_voz_soberana(self):
        self.mix['loudnorm'] = False
        parts, last = mm._build_audio_filter(self.mix, has_trilha=True, has_efe=False)
        self.assertEqual(parts[0], f'[2:a]volume={self.mix["music_gain"]}[m]')
        self.assertEqual(parts[1], '[1:a][m]amix=inputs=2:duration=first:dropout_transition=2[vt]')
        self.assertEqual(last, '[vt]')

    def test_sfx_sem_normalizar_e_indice_correto(self):
        self.mix['loudnorm'] = False
        parts, last = mm._build_audio_filter(self.mix, has_trilha=True, has_efe=True)
        # com trilha (idx 2) o SFX entra no idx 3
        self.assertIn('[3:a]volume=1.0[e]', parts)
        self.assertIn('normalize=0', parts[-1])
        self.assertEqual(last, '[ve]')

    def test_sfx_sem_trilha_usa_indice_2(self):
        self.mix['loudnorm'] = False
        parts, _ = mm._build_audio_filter(self.mix, has_trilha=False, has_efe=True)
        self.assertEqual(parts[0], '[2:a]volume=1.0[e]')

    def test_cadeia_completa_termina_em_loudnorm(self):
        parts, last = mm._build_audio_filter(self.mix, has_trilha=True, has_efe=True)
        self.assertEqual(parts[-1], '[ve]loudnorm=I=-14:TP=-1.0:LRA=11[a]')
        self.assertEqual(last, '[a]')


@unittest.skipUnless(_OK, 'mixmaster indisponivel')
class TestRunErroComContexto(unittest.TestCase):
    """Pilar 7: ffmpeg que falha NÃO pode propagar mudo — o MOTIVO (stderr) tem
    de ficar diagnosticável. HERMÉTICO: subprocess.run mockado, ffmpeg nunca roda."""

    def test_falha_ffmpeg_inclui_stderr_no_erro(self):
        stderr = b'A' * 50 + b'loudnorm: Invalid argument near LRA'
        erro = subprocess.CalledProcessError(1, ['ffmpeg'], stderr=stderr)
        with mock.patch.object(mm.subprocess, 'run', side_effect=erro):
            with self.assertRaises(RuntimeError) as ctx:
                mm._run(['ffmpeg', '-y', 'x'])
        msg = str(ctx.exception)
        # o motivo do ffmpeg (cauda do stderr) tem de aparecer
        self.assertIn('loudnorm: Invalid argument near LRA', msg)
        # e o codigo de retorno, p/ diagnostico
        self.assertIn('1', msg)

    def test_falha_ffmpeg_sem_stderr_nao_quebra_a_mensagem(self):
        erro = subprocess.CalledProcessError(2, ['ffmpeg'], stderr=None)
        with mock.patch.object(mm.subprocess, 'run', side_effect=erro):
            with self.assertRaises(RuntimeError) as ctx:
                mm._run(['ffmpeg'])
        self.assertIn('2', str(ctx.exception))  # rc continua presente

    def test_sucesso_nao_levanta(self):
        # contrato: quando o ffmpeg funciona, _run continua silencioso (sem regressao)
        with mock.patch.object(mm.subprocess, 'run', return_value=None) as run:
            mm._run(['ffmpeg', '-y', 'ok'])
        run.assert_called_once()


@unittest.skipUnless(_OK, 'mixmaster indisponivel')
class TestMasterAntiFantasma(unittest.TestCase):
    """Anti-fantasma: um master de 0 byte / ausente NAO e sucesso. HERMETICO:
    stems forjados num tmpdir; subprocess.run mockado (nao toca o master de verdade)."""

    def setUp(self):
        import tempfile
        self._tmp = tempfile.TemporaryDirectory()
        self.d = Path(self._tmp.name) / 'slug-fantasma'
        self.d.mkdir(parents=True)
        # stems minimos exigidos por master(): video_mudo.mp4 + voz.wav
        (self.d / 'video_mudo.mp4').write_bytes(b'fake-video')
        (self.d / 'voz.wav').write_bytes(b'fake-voz')
        self._stems_patch = mock.patch.object(mm, 'STEMS', self.d.parent)
        self._stems_patch.start()
        self.out = self.d.parent / 'out.mp4'

    def tearDown(self):
        self._stems_patch.stop()
        self._tmp.cleanup()

    def test_master_vazio_falha_com_contexto(self):
        # ffmpeg "sucede" mas deixa um arquivo de 0 byte -> fantasma
        def _fake_run(args, **kw):
            self.out.write_bytes(b'')  # master vazio
        with mock.patch.object(mm.subprocess, 'run', side_effect=_fake_run):
            with self.assertRaises(RuntimeError) as ctx:
                mm.master('slug-fantasma', out=self.out)
        msg = str(ctx.exception)
        self.assertIn(str(self.out), msg)  # diz QUAL arquivo
        self.assertIn('0', msg)            # e que tem 0 bytes

    def test_master_ausente_falha_com_contexto(self):
        # ffmpeg "sucede" mas nem cria o arquivo -> fantasma
        with mock.patch.object(mm.subprocess, 'run', return_value=None):
            with self.assertRaises(RuntimeError) as ctx:
                mm.master('slug-fantasma', out=self.out)
        self.assertIn(str(self.out), str(ctx.exception))

    def test_master_valido_retorna_o_caminho(self):
        # contrato de SUCESSO: master nao-vazio -> devolve o Path, sem levantar
        def _fake_run(args, **kw):
            self.out.write_bytes(b'x' * 4096)  # master "real"
        with mock.patch.object(mm.subprocess, 'run', side_effect=_fake_run):
            res = mm.master('slug-fantasma', out=self.out)
        self.assertEqual(Path(res), self.out)


if __name__ == '__main__':
    unittest.main()
