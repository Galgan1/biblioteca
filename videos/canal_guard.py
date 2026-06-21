# -*- coding: utf-8 -*-
"""Fonte ÚNICA da identidade do canal YouTube do projeto.

Contrato inviolável (CLAUDE.md): a lane de YouTube publica SEMPRE no canal
**Minuto Real** (@MinutoReal1701) e NUNCA no canal pessoal (andregalgani).

Aqui a regra deixa de ser documento e vira GUARDA DE MÁQUINA: todo cliente da
YouTube API do projeto deve nascer por get_youtube(), que ABORTA se o OAuth
resolver para outro canal — antes de qualquer insert/update/set. Nenhum script
deve chamar build('youtube', ...) direto.
"""
from googleapiclient.discovery import build

CANAL_ID = 'UC2N5xZ-gyCU3hNvH1QqNahA'      # Minuto Real (@MinutoReal1701) — ÚNICO destino
CANAL_TITULO = 'Minuto Real'
CANAL_HANDLE = '@MinutoReal1701'
PESSOAL_ID = 'UCmSpZF4cVFd1kTYomdC_NUw'    # andregalgani (pessoal) — PROIBIDO publicar aqui


class CanalErrado(RuntimeError):
    """OAuth resolveu para um canal que NÃO é o Minuto Real — aborta antes de mutar."""


def assert_canal(yt):
    """Confere que o cliente fala com o Minuto Real; levanta CanalErrado se não.
    Devolve o item do canal (snippet) para quem quiser logar o título."""
    itens = yt.channels().list(part='snippet', mine=True).execute().get('items', [])
    if not itens:
        raise CanalErrado('OAuth sem canal acessível — token inválido/expirado?')
    ch = itens[0]
    if ch['id'] != CANAL_ID:
        raise CanalErrado(
            f"CANAL ERRADO: OAuth resolveu «{ch['snippet']['title']}» ({ch['id']}).\n"
            f"  Esperado {CANAL_TITULO} ({CANAL_ID}). Abortado para NÃO publicar no canal "
            f"pessoal. Refaça o OAuth escolhendo o {CANAL_TITULO}.")
    return ch


def get_youtube():
    """Cliente da YouTube API JÁ verificado no Minuto Real — ponto único do projeto.
    Reusa o OAuth de upload_youtube.get_creds (import tardio p/ evitar ciclo)."""
    from upload_youtube import get_creds
    yt = build('youtube', 'v3', credentials=get_creds())
    assert_canal(yt)
    return yt
