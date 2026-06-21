# -*- coding: utf-8 -*-
"""Testes das funcoes puras de logica de tempo/negocio de `sincronizar.py`.

Akita pilar 2 — verde = exit code. 100% hermetico: sem disco, sem rede,
sem scp, sem manifesto. Cobre os contratos que uma regressao quebraria:

  - clamp_offset: offset default=+2h, trava em <=4h, nunca negativo/zero;
  - ig_time: hora-alvo = anchor + offset_h exato;
  - parse_anchor: timezone BRT/-3, hora default 19:00, parsing DD/MM e HH:MM;
  - job_key: chave de idempotencia = (slug, tipo, parte);
  - _parse_cli: flags --offset/--tipo/--yt/--dry-run e posicionais.
"""
import sys
import unittest
from datetime import datetime, timedelta, timezone
from unittest.mock import patch

# garante import do modulo a partir de videos/
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import sincronizar as S


BRT = timezone(timedelta(hours=-3))


# ──────────────────────────────────────────────────────────────────────────────
# Fixtures utilitarios
# ──────────────────────────────────────────────────────────────────────────────

def _anchor(ano=2026, mes=6, dia=16, hora=19, minuto=0):
    """Cria um datetime de ancora em BRT (SEG 19h tipico)."""
    return datetime(ano, mes, dia, hora, minuto, 0, tzinfo=BRT)


# ──────────────────────────────────────────────────────────────────────────────
# clamp_offset
# ──────────────────────────────────────────────────────────────────────────────

class TestClampOffset(unittest.TestCase):
    """Contratos da janela de eco: sempre dentro de (0h, 4h]."""

    def test_offset_default_dois_horas(self):
        """Valor sem customizacao = OFFSET_DEFAULT_H = 2h."""
        self.assertEqual(S.OFFSET_DEFAULT_H, 2.0)

    def test_clamp_mantém_valor_valido(self):
        """Offset dentro da janela (0 < h <= 4) nao e alterado."""
        self.assertEqual(S.clamp_offset(1.0), 1.0)
        self.assertEqual(S.clamp_offset(2.0), 2.0)
        self.assertEqual(S.clamp_offset(4.0), 4.0)

    def test_clamp_trava_em_4h_quando_excede(self):
        """5h de offset deve ser travado em 4h (janela maxima)."""
        with patch('builtins.print'):  # suprime aviso de console
            resultado = S.clamp_offset(5.0)
        self.assertEqual(resultado, S.MAX_OFFSET_H)
        self.assertEqual(resultado, 4.0)

    def test_clamp_trava_valores_muito_altos(self):
        """100h deve ser travado em 4h."""
        with patch('builtins.print'):
            resultado = S.clamp_offset(100.0)
        self.assertEqual(resultado, 4.0)

    def test_clamp_substitui_zero_pelo_default(self):
        """Offset zero e invalido (eco deve ser DEPOIS do longo) -> vira default 2h."""
        with patch('builtins.print'):
            resultado = S.clamp_offset(0.0)
        self.assertEqual(resultado, S.OFFSET_DEFAULT_H)

    def test_clamp_substitui_negativo_pelo_default(self):
        """Offset negativo e invalido (eco nao pode ser ANTES do longo) -> default 2h."""
        with patch('builtins.print'):
            resultado = S.clamp_offset(-1.0)
        self.assertEqual(resultado, S.OFFSET_DEFAULT_H)

    def test_max_offset_e_4_horas(self):
        """Constante MAX_OFFSET_H deve ser 4h (contrato de negocio)."""
        self.assertEqual(S.MAX_OFFSET_H, 4.0)


# ──────────────────────────────────────────────────────────────────────────────
# ig_time
# ──────────────────────────────────────────────────────────────────────────────

class TestIgTime(unittest.TestCase):
    """ig_time = anchor + timedelta(hours=offset_h), sem logica adicional."""

    def test_offset_2h_padrao(self):
        """Longo 19h BRT -> IG 21h BRT com offset default +2h."""
        anchor = _anchor(hora=19)
        alvo = S.ig_time(anchor, 2.0)
        self.assertEqual(alvo.hour, 21)
        self.assertEqual(alvo.minute, 0)

    def test_offset_4h_limite(self):
        """Longo 19h BRT -> IG 23h BRT com offset maximo +4h."""
        anchor = _anchor(hora=19)
        alvo = S.ig_time(anchor, 4.0)
        self.assertEqual(alvo.hour, 23)

    def test_timezone_brt_preservado(self):
        """ig_time deve preservar o timezone BRT/-3 do anchor."""
        anchor = _anchor()
        alvo = S.ig_time(anchor, 2.0)
        self.assertEqual(alvo.tzinfo, BRT)

    def test_offset_fracionario(self):
        """offset_h=1.5 deve adicionar 1h30 exatos."""
        anchor = _anchor(hora=19, minuto=0)
        alvo = S.ig_time(anchor, 1.5)
        esperado = anchor + timedelta(hours=1.5)
        self.assertEqual(alvo, esperado)
        self.assertEqual(alvo.minute, 30)

    def test_eco_nunca_antes_do_longo(self):
        """ig_time com offset positivo => alvo > anchor (invariante do eco)."""
        anchor = _anchor()
        alvo = S.ig_time(anchor, S.OFFSET_DEFAULT_H)
        self.assertGreater(alvo, anchor)

    def test_utc_correto_brt_menos_3(self):
        """BRT = UTC-3: IG 21h BRT = 00h UTC do dia seguinte."""
        anchor = _anchor(ano=2026, mes=6, dia=15, hora=19)
        alvo = S.ig_time(anchor, 2.0)
        utc = alvo.astimezone(timezone.utc)
        self.assertEqual(utc.hour, 0)   # 21 BRT - (-3) = 00 UTC
        self.assertEqual(utc.day, 16)   # vira meia-noite do dia seguinte


# ──────────────────────────────────────────────────────────────────────────────
# parse_anchor
# ──────────────────────────────────────────────────────────────────────────────

class TestParseAnchor(unittest.TestCase):
    """parse_anchor retorna datetime em BRT a partir de strings DD/MM e HH:MM."""

    def test_timezone_resultado_e_brt(self):
        """Resultado deve ter timezone = BRT (UTC-3)."""
        dt = S.parse_anchor('16/06', '19:00')
        self.assertEqual(dt.tzinfo, BRT)

    def test_hora_e_minuto_corretos(self):
        """HH:MM deve ser aplicado exatamente ao resultado."""
        dt = S.parse_anchor('16/06', '21:30')
        self.assertEqual(dt.hour, 21)
        self.assertEqual(dt.minute, 30)

    def test_hora_default_19_00(self):
        """Sem hhmm, a hora default e 19:00 (horario do longo)."""
        dt = S.parse_anchor('16/06', None)
        self.assertEqual(dt.hour, 19)
        self.assertEqual(dt.minute, 0)

    def test_dia_e_mes_corretos(self):
        """DD/MM deve resultar no dia e mes informados."""
        dt = S.parse_anchor('20/03', '10:00')
        self.assertEqual(dt.day, 20)
        self.assertEqual(dt.month, 3)

    def test_segundo_e_microsegundo_zerados(self):
        """Resultado deve ter second=0 e microsecond=0 (horario limpo)."""
        dt = S.parse_anchor('16/06', '19:00')
        self.assertEqual(dt.second, 0)
        self.assertEqual(dt.microsecond, 0)

    def test_ddmm_nenhum_usa_hoje(self):
        """Sem ddmm, parse_anchor usa a data de hoje em BRT."""
        hoje = datetime.now(BRT).date()
        dt = S.parse_anchor(None, '10:00')
        self.assertEqual(dt.date(), hoje)

    def test_ddmm_nenhum_hhmm_nenhum_usa_19h_hoje(self):
        """Sem argumentos, ancora = hoje 19:00 BRT."""
        hoje = datetime.now(BRT).date()
        dt = S.parse_anchor(None, None)
        self.assertEqual(dt.date(), hoje)
        self.assertEqual(dt.hour, 19)


# ──────────────────────────────────────────────────────────────────────────────
# job_key
# ──────────────────────────────────────────────────────────────────────────────

class TestJobKey(unittest.TestCase):
    """job_key extrai a chave de idempotencia (slug, tipo, parte)."""

    def _job(self, slug='habitos-atomicos', tipo='reel', parte=1):
        return {'slug': slug, 'tipo': tipo, 'parte': parte}

    def test_chave_e_tupla_de_tres(self):
        k = S.job_key(self._job())
        self.assertIsInstance(k, tuple)
        self.assertEqual(len(k), 3)

    def test_chave_contem_slug_tipo_parte(self):
        job = self._job('sapiens', 'reel', 2)
        k = S.job_key(job)
        self.assertEqual(k, ('sapiens', 'reel', 2))

    def test_chave_overview_para_carousel(self):
        job = self._job('sapiens', 'carousel', 'overview')
        k = S.job_key(job)
        self.assertEqual(k, ('sapiens', 'carousel', 'overview'))

    def test_parte_ausente_vira_none(self):
        """Job sem campo 'parte' usa None como fallback (get com default)."""
        job = {'slug': 'sapiens', 'tipo': 'reel'}
        k = S.job_key(job)
        self.assertEqual(k[2], None)

    def test_jobs_iguais_mesma_chave(self):
        """Dois jobs com mesmo slug/tipo/parte devem ter a mesma chave."""
        j1 = self._job('sapiens', 'reel', 1)
        j2 = self._job('sapiens', 'reel', 1)
        self.assertEqual(S.job_key(j1), S.job_key(j2))

    def test_jobs_diferentes_chaves_distintas(self):
        j1 = self._job('sapiens', 'reel', 1)
        j2 = self._job('sapiens', 'carousel', 'overview')
        self.assertNotEqual(S.job_key(j1), S.job_key(j2))


# ──────────────────────────────────────────────────────────────────────────────
# _parse_cli
# ──────────────────────────────────────────────────────────────────────────────

class TestParseCli(unittest.TestCase):
    """_parse_cli separa flags e posicionais dos argumentos de linha de comando."""

    def test_sem_argumentos_usa_defaults(self):
        ddmm, hhmm, offset, tipo, yt, dry = S._parse_cli([])
        self.assertIsNone(ddmm)
        self.assertIsNone(hhmm)
        self.assertEqual(offset, S.OFFSET_DEFAULT_H)
        self.assertEqual(tipo, 'reel')
        self.assertIsNone(yt)
        self.assertFalse(dry)

    def test_posicional_ddmm(self):
        ddmm, hhmm, *_ = S._parse_cli(['16/06'])
        self.assertEqual(ddmm, '16/06')
        self.assertIsNone(hhmm)

    def test_posicionais_ddmm_e_hhmm(self):
        ddmm, hhmm, *_ = S._parse_cli(['16/06', '21:00'])
        self.assertEqual(ddmm, '16/06')
        self.assertEqual(hhmm, '21:00')

    def test_flag_offset(self):
        _, _, offset, *_ = S._parse_cli(['--offset', '3.5'])
        self.assertAlmostEqual(offset, 3.5)

    def test_flag_tipo(self):
        *_, tipo, _, _ = S._parse_cli(['--tipo', 'carousel'])
        self.assertEqual(tipo, 'carousel')

    def test_flag_yt(self):
        ddmm, hhmm, offset, tipo, yt, dry = S._parse_cli(['--yt', 'abc123'])
        self.assertEqual(yt, 'abc123')

    def test_flag_dry_run_longa(self):
        *_, dry = S._parse_cli(['--dry-run'])
        self.assertTrue(dry)

    def test_flag_dry_curta(self):
        *_, dry = S._parse_cli(['--dry'])
        self.assertTrue(dry)

    def test_combinacao_completa(self):
        """Todos os flags juntos com posicionais."""
        args = ['16/06', '19:00', '--offset', '3', '--tipo', 'story',
                '--yt', 'xYz789', '--dry-run']
        ddmm, hhmm, offset, tipo, yt, dry = S._parse_cli(args)
        self.assertEqual(ddmm, '16/06')
        self.assertEqual(hhmm, '19:00')
        self.assertAlmostEqual(offset, 3.0)
        self.assertEqual(tipo, 'story')
        self.assertEqual(yt, 'xYz789')
        self.assertTrue(dry)


# ──────────────────────────────────────────────────────────────────────────────
# Contratos de integracao (composicao clamp + ig_time)
# ──────────────────────────────────────────────────────────────────────────────

class TestContratosCoreografia(unittest.TestCase):
    """Contratos de negocio do sistema como um todo (clamp + ig_time compostos)."""

    def test_eco_com_offset_default_cai_2h_apos_ancora(self):
        """Caminho feliz: longo 19h, IG 21h (offset default 2h)."""
        anchor = _anchor(hora=19)
        offset = S.clamp_offset(S.OFFSET_DEFAULT_H)
        alvo = S.ig_time(anchor, offset)
        self.assertEqual(alvo - anchor, timedelta(hours=2))

    def test_eco_com_5h_travado_em_4h(self):
        """Offset 5h deve ser travado em 4h: longo 19h -> IG 23h (nao 00h)."""
        anchor = _anchor(hora=19)
        with patch('builtins.print'):
            offset = S.clamp_offset(5.0)
        alvo = S.ig_time(anchor, offset)
        self.assertEqual(alvo - anchor, timedelta(hours=4))
        self.assertEqual(alvo.hour, 23)

    def test_eco_com_offset_zero_usa_default_2h(self):
        """Offset 0 invalido -> default 2h -> eco 2h apos o longo."""
        anchor = _anchor(hora=19)
        with patch('builtins.print'):
            offset = S.clamp_offset(0.0)
        alvo = S.ig_time(anchor, offset)
        self.assertEqual(alvo - anchor, timedelta(hours=2))

    def test_eco_nunca_antes_do_longo_com_negativo(self):
        """Offset negativo travado no default: eco SEMPRE depois do longo."""
        anchor = _anchor(hora=19)
        with patch('builtins.print'):
            offset = S.clamp_offset(-3.0)
        alvo = S.ig_time(anchor, offset)
        self.assertGreater(alvo, anchor)

    def test_janela_maxima_4h_nunca_excedida(self):
        """Com qualquer offset >= 0, ig_time(anchor, clamp(h)) <= anchor + 4h."""
        anchor = _anchor(hora=19)
        for h in [0.5, 1.0, 2.0, 3.0, 4.0, 5.0, 10.0, 99.0]:
            with patch('builtins.print'):
                offset = S.clamp_offset(h)
            alvo = S.ig_time(anchor, offset)
            self.assertLessEqual(
                alvo - anchor,
                timedelta(hours=4),
                msg=f'offset {h}h excedeu a janela de 4h'
            )


if __name__ == '__main__':
    unittest.main()
