# -*- coding: utf-8 -*-
"""StateGraph LangGraph — pipeline Minuto Real com checkpointing SQLite.

Diferencial sobre o orquestrador.py:
  • Checkpointing persistente: se o pipeline cair no meio (crash, quota esgotada),
    retome com o mesmo comando — o grafo continua do último ponto salvo.
  • Time-travel: inspecione qualquer estado passado via get_state_history().
  • thread_id = slug: cada livro tem sua própria trilha de checkpoints.

Uso:
  # Executa (ou resume) o pipeline de um slug
  python pipeline/graph.py arte-da-guerra

  # Dry-run (só mostra o estado atual, não executa)
  python pipeline/graph.py arte-da-guerra --dry-run

  # Inspeciona histórico de checkpoints
  python pipeline/graph.py arte-da-guerra --history

Dependências:
  pip install langgraph langchain-anthropic
"""
import sys
from pathlib import Path
from typing import Annotated, Optional
import operator

# Garante que os scripts de vídeo são encontráveis
ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT / 'videos'))
sys.path.insert(0, str(ROOT / 'pipeline'))

from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.sqlite import SqliteSaver
from typing import TypedDict

from nodes import (
    node_load_state,
    node_validate,
    node_run_biblioteca,
    node_run_video_build,
    node_run_upload,
    node_run_shorts,
    node_run_carrossel,
    node_verify,
)

# ---------------------------------------------------------------------------
# Estado do grafo
# ---------------------------------------------------------------------------

class PipelineState(TypedDict):
    slug: str
    stages_done: list[str]
    video_id: Optional[str]
    errors: Annotated[list[str], operator.add]   # reducer: append-only
    run_id: str


# ---------------------------------------------------------------------------
# Roteamento condicional
# ---------------------------------------------------------------------------

def _route_after_validate(state: PipelineState) -> str:
    """Após validação: decide se há skill disponível para produzir."""
    if state.get('errors'):
        return 'verify'
    # A skill (book-to-skill) é feita pelo maestro antes deste grafo.
    # Aqui apenas verificamos que roteiro.json existe (feito em node_validate).
    return 'run_biblioteca'


def _route_after_upload(state: PipelineState) -> str:
    """Se upload falhou (sem video_id), pula shorts."""
    if not state.get('video_id'):
        return 'verify'
    return 'run_shorts'


# ---------------------------------------------------------------------------
# Construção do grafo
# ---------------------------------------------------------------------------

def build_graph(checkpointer=None):
    builder = StateGraph(PipelineState)

    # Nós
    builder.add_node('load_state',      node_load_state)
    builder.add_node('validate',        node_validate)
    builder.add_node('run_biblioteca',  node_run_biblioteca)
    builder.add_node('run_video_build', node_run_video_build)
    builder.add_node('run_upload',      node_run_upload)
    builder.add_node('run_shorts',      node_run_shorts)
    builder.add_node('run_carrossel',   node_run_carrossel)
    builder.add_node('verify',          node_verify)

    # Fluxo principal
    builder.add_edge(START,              'load_state')
    builder.add_edge('load_state',       'validate')

    # Após validate: vai para biblioteca ou direto para verify (em caso de erro)
    builder.add_conditional_edges(
        'validate',
        _route_after_validate,
        {'run_biblioteca': 'run_biblioteca', 'verify': 'verify'},
    )

    # biblioteca e video_build correm em sequência dentro do grafo
    # (a verdadeira paralelização está no orquestrador.py + ThreadPoolExecutor)
    builder.add_edge('run_biblioteca',  'run_video_build')
    builder.add_edge('run_video_build', 'run_upload')

    # Após upload: shorts (se video_id disponível) ou verify
    builder.add_conditional_edges(
        'run_upload',
        _route_after_upload,
        {'run_shorts': 'run_shorts', 'verify': 'verify'},
    )

    # Instagram corre depois dos shorts
    builder.add_edge('run_shorts',      'run_carrossel')
    builder.add_edge('run_carrossel',   'verify')
    builder.add_edge('verify',          END)

    return builder.compile(checkpointer=checkpointer)


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------

DB_PATH = ROOT / 'pipeline' / 'checkpoints.db'


def run_pipeline(slug: str, run_id: str = None, dry_run: bool = False):
    """Executa (ou resume) o pipeline para um slug.

    O thread_id é o slug — cada livro tem sua própria trilha de checkpoints.
    Chamadas subsequentes retomam de onde pararam.
    """
    import uuid
    if run_id is None:
        run_id = str(uuid.uuid4())[:8]

    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    with SqliteSaver.from_conn_string(str(DB_PATH)) as checkpointer:
        graph = build_graph(checkpointer)
        config = {'configurable': {'thread_id': slug}}

        if dry_run:
            # Apenas mostra o estado atual sem executar
            try:
                snapshot = graph.get_state(config)
                print(f'Checkpoint atual para {slug!r}:')
                print(f'  values: {snapshot.values}')
                print(f'  next: {snapshot.next}')
            except Exception:
                print(f'Nenhum checkpoint encontrado para {slug!r}.')
            return

        initial_state: PipelineState = {
            'slug': slug,
            'stages_done': [],
            'video_id': None,
            'errors': [],
            'run_id': run_id,
        }

        print(f'\n[pipeline] Iniciando slug={slug!r} run_id={run_id!r}')
        print(f'[pipeline] Checkpoint DB: {DB_PATH}')
        print()

        final = graph.invoke(initial_state, config)
        return final


def show_history(slug: str):
    """Imprime o histórico de checkpoints para um slug."""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    with SqliteSaver.from_conn_string(str(DB_PATH)) as checkpointer:
        graph = build_graph(checkpointer)
        config = {'configurable': {'thread_id': slug}}
        history = list(graph.get_state_history(config))
        if not history:
            print(f'Nenhum checkpoint para {slug!r}.')
            return
        print(f'Histórico de checkpoints para {slug!r} ({len(history)} entradas):')
        for i, snap in enumerate(history):
            ts = getattr(snap, 'created_at', '?')
            vals = snap.values or {}
            stages = vals.get('stages_done', [])
            errors = vals.get('errors', [])
            print(f'  [{i}] ts={ts}  done={stages}  errors={len(errors)}')


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Pipeline LangGraph — Minuto Real')
    parser.add_argument('slug', help='Slug do livro (ex: arte-da-guerra)')
    parser.add_argument('--dry-run', action='store_true',
                        help='Exibe checkpoint atual sem executar')
    parser.add_argument('--history', action='store_true',
                        help='Exibe histórico de checkpoints')
    parser.add_argument('--run-id', default=None,
                        help='ID de run (gerado automaticamente se omitido)')
    args = parser.parse_args()

    if args.history:
        show_history(args.slug)
    else:
        run_pipeline(args.slug, run_id=args.run_id, dry_run=args.dry_run)
