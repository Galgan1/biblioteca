# -*- coding: utf-8 -*-
"""Contratos Pydantic v2 — Biblioteca / Canal Minuto Real (Fase A).

Valida o roteiro JSON e as saídas de cada stage ANTES de qualquer chamada de API,
evitando quebras silenciosas (ex.: índice shorts inválido só detectado após gastar crédito).

Uso rápido:
    from contracts import load_roteiro
    cfg = load_roteiro('roteiros/arte-da-guerra.json')
"""

from __future__ import annotations

import warnings
from pathlib import Path
from typing import List, Literal, Optional

from pydantic import BaseModel, Field, field_validator, model_validator, ConfigDict


# ---------------------------------------------------------------------------
# CenaSchema
# ---------------------------------------------------------------------------


class CenaSchema(BaseModel):
    model_config = ConfigDict(extra='allow')

    tipo: Literal['abertura', 'conceito', 'encerramento'] = 'conceito'
    titulo: str
    narracao: str

    # opcionais
    kicker: Optional[str] = None
    subtitulo: Optional[str] = None
    img: Optional[str] = None
    motion: Optional[str] = None

    @field_validator('narracao')
    @classmethod
    def avisa_narracao_longa(cls, v: str) -> str:
        n_palavras = len(v.split())
        if n_palavras > 65:
            print(
                f'  [contracts] aviso: narracao com {n_palavras} palavras '
                f'(regra do estudio: max 60 palavras/cena). Cena: "{v[:60]}..."'
            )
        return v


# ---------------------------------------------------------------------------
# YouTubeCfg
# ---------------------------------------------------------------------------


class YouTubeCfg(BaseModel):
    model_config = ConfigDict(extra='allow')

    titulo: Optional[str] = Field(default=None, max_length=100)
    descricao: Optional[str] = Field(default=None, max_length=5000)
    tags: Optional[List[str]] = None
    privacidade: Literal['unlisted', 'private', 'public'] = 'unlisted'
    playlist: Optional[str] = None


# ---------------------------------------------------------------------------
# RoteiroCfg
# ---------------------------------------------------------------------------


class RoteiroCfg(BaseModel):
    model_config = ConfigDict(extra='allow')

    # obrigatórios
    slug: str
    titulo: str
    autor: str

    # com default
    voz: str = 'pt-BR-Chirp3-HD-Iapetus'
    tts_rate: float = Field(default=1.0, ge=0.5, le=1.5)
    musica: bool = True
    provider: Literal['base', 'google', 'fal'] = 'base'

    # opcionais
    acento: Optional[str] = None
    estilo_img: Optional[str] = None
    youtube: Optional[YouTubeCfg] = None

    # listas
    cenas: List[CenaSchema] = Field(min_length=3)
    shorts: Optional[List[int]] = None

    @model_validator(mode='after')
    def valida_indices_shorts(self) -> 'RoteiroCfg':
        if self.shorts is None:
            return self
        n = len(self.cenas)
        invalidos = [i for i in self.shorts if i < 0 or i >= n]
        if invalidos:
            raise ValueError(
                f'shorts contém índices inválidos {invalidos} '
                f'(roteiro tem {n} cenas, índices válidos: 0–{n - 1})'
            )
        return self


# ---------------------------------------------------------------------------
# PipelineStageResult
# ---------------------------------------------------------------------------


class PipelineStageResult(BaseModel):
    slug: str
    stage: str
    status: Literal['done', 'blocked', 'skipped']
    data: Optional[dict] = None
    error: Optional[str] = None


# ---------------------------------------------------------------------------
# SkillOutput
# ---------------------------------------------------------------------------


class SkillOutput(BaseModel):
    slug: str
    skill_path: str
    has_skill_md: bool = True
    chapter_count: int
    tone: Optional[str] = None  # ex: "contemplativo", "prático"


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------


def load_roteiro(path) -> RoteiroCfg:
    import json

    raw = json.loads(Path(path).read_text(encoding='utf-8'))
    return RoteiroCfg.model_validate(raw)


# ---------------------------------------------------------------------------
# __main__ — smoke test
# ---------------------------------------------------------------------------

if __name__ == '__main__':
    import json

    roteiro_exemplo = {
        "slug": "arte-da-guerra",
        "titulo": "A Arte da Guerra",
        "autor": "Sun Tzu",
        "voz": "pt-BR-Chirp3-HD-Iapetus",
        "tts_rate": 0.96,
        "acento": "#d8a64a",
        "musica": True,
        "provider": "google",
        "estilo_img": "cinematic atmospheric dark painting",
        "youtube": {
            "titulo": "A Arte da Guerra — Resumo em 5 minutos",
            "descricao": "Os princípios de Sun Tzu em menos de 5 minutos.",
            "tags": ["arte da guerra", "sun tzu", "resumo"],
            "privacidade": "unlisted",
            "playlist": "Minuto Real — Estratégia",
        },
        "cenas": [
            {
                "tipo": "abertura",
                "titulo": "A Arte da Guerra",
                "subtitulo": "Sun Tzu",
                "img": "ancient chinese scroll battlefield",
                "motion": "slow pan across ancient scroll",
                "narracao": "Há mais de dois mil anos, um general escreveu o tratado militar mais influente da história.",
            },
            {
                "tipo": "conceito",
                "kicker": "01 · A Estratégia Suprema",
                "titulo": "Vencer sem lutar",
                "img": "two armies facing each other across a misty valley",
                "narracao": "O general supremo vence a batalha antes de ela começar. A vitória máxima é dobrar o inimigo sem combate.",
            },
            {
                "tipo": "conceito",
                "kicker": "02 · Conhecimento",
                "titulo": "Conheça seu inimigo",
                "narracao": "Conheça o inimigo e a si mesmo. Em cem batalhas, jamais estarás em perigo.",
            },
            {
                "tipo": "encerramento",
                "titulo": "A Arte da Guerra",
                "narracao": "A estratégia não é sobre força bruta. É sobre inteligência, timing e adaptação.",
            },
        ],
        "shorts": [0, 2],
    }

    print("--- Smoke test: roteiro válido ---")
    cfg = RoteiroCfg.model_validate(roteiro_exemplo)
    print(f"  slug={cfg.slug!r}, cenas={len(cfg.cenas)}, shorts={cfg.shorts}")
    print(f"  provider={cfg.provider!r}, tts_rate={cfg.tts_rate}")

    print("\n--- Smoke test: narração longa (aviso, não erro) ---")
    roteiro_long = dict(roteiro_exemplo)
    roteiro_long['cenas'] = list(roteiro_exemplo['cenas'])
    roteiro_long['cenas'][1] = dict(roteiro_exemplo['cenas'][1])
    roteiro_long['cenas'][1]['narracao'] = ' '.join(['palavra'] * 70)
    cfg2 = RoteiroCfg.model_validate(roteiro_long)
    print(f"  cenas ok={len(cfg2.cenas)}")

    print("\n--- Smoke test: shorts com índice inválido (deve lançar erro) ---")
    roteiro_bad = dict(roteiro_exemplo, shorts=[0, 99])
    try:
        RoteiroCfg.model_validate(roteiro_bad)
        print("  FALHOU: deveria ter lançado erro")
    except Exception as e:
        print(f"  OK: erro capturado — {e}")

    print("\n--- Smoke test: PipelineStageResult ---")
    r = PipelineStageResult(slug='arte-da-guerra', stage='tts', status='done', data={'files': 4})
    print(f"  {r}")

    print("\n--- Smoke test: SkillOutput ---")
    s = SkillOutput(
        slug='arte-da-guerra',
        skill_path='~/.claude/skills/arte-da-guerra',
        chapter_count=12,
        tone='contemplativo',
    )
    print(f"  {s}")

    print("\nTodos os smoke tests passaram.")
