# -*- coding: utf-8 -*-
"""DAG declarativo das dependências entre stages do pipeline.
Cada stage lista seus pré-requisitos. O orquestrador resolve a ordem topológica.
"""

# Stages e suas dependências
# fmt: off
DAG = {
    'skill':       [],                # sequencial (book-to-skill via Claude)
    'biblioteca':  ['skill'],         # publicar_livro.py --deploy
    'video_built': ['skill'],         # gerar_video.py (paralelizável com biblioteca)
    'uploaded':    ['video_built'],   # upload_youtube.py
    'shorts':      ['uploaded'],      # produzir_shorts.py
    'scheduled':   ['shorts'],        # agendar_lote.py
    'instagram':   ['skill'],         # gerar_carrossel.py (paralelizável)
    'tiktok':      ['shorts'],        # tiktok_post.py (quando tiver token)
    'facebook':    ['uploaded'],      # facebook_post.py
}
# fmt: on


def topological_sort(dag: dict) -> list:
    """Kahn's algorithm — retorna os stages em ordem de execução."""
    in_degree = {s: 0 for s in dag}
    for deps in dag.values():
        for d in deps:
            in_degree[d] = in_degree.get(d, 0)  # garante chave
    for s, deps in dag.items():
        for d in deps:
            if d in in_degree:
                in_degree[s] = in_degree.get(s, 0)

    # recalcular in_degree corretamente
    in_degree = {s: 0 for s in dag}
    for s, deps in dag.items():
        for d in deps:
            pass  # deps não incrementam o grau de entrada deles; s depende deles
        in_degree[s] = len(deps)

    queue = [s for s, deg in in_degree.items() if deg == 0]
    result = []
    while queue:
        queue.sort()  # determinismo
        node = queue.pop(0)
        result.append(node)
        for s, deps in dag.items():
            if node in deps:
                in_degree[s] -= 1
                if in_degree[s] == 0:
                    queue.append(s)
    return result


def ready_stages(dag: dict, done: set) -> list:
    """Stages cujas dependências estão todas em 'done' e que ainda não foram feitos."""
    return [s for s, deps in dag.items() if s not in done and all(d in done for d in deps)]


def parallel_groups(dag: dict) -> list:
    """Retorna grupos (sets) de stages que podem rodar em paralelo.

    Agrupa por 'nível' na topologia: stages no mesmo nível não dependem entre si
    e podem ser executados ao mesmo tempo.
    """
    remaining = set(dag.keys())
    done = set()
    groups = []
    while remaining:
        group = {s for s in remaining if all(d in done for d in dag.get(s, []))}
        if not group:
            break  # ciclo ou stage sem deps resolvíveis — não deve ocorrer
        groups.append(group)
        done |= group
        remaining -= group
    return groups


if __name__ == '__main__':
    print("Ordem topológica:", topological_sort(DAG))
    print("\nGrupos paralelos:")
    for i, g in enumerate(parallel_groups(DAG), 1):
        print(f"  {i}. {sorted(g)}")
