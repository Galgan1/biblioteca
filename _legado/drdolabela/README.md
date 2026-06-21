# Quarentena — ilha "drdolabela" (ingestão acadêmica)

> Refatoração Akita (pilar 4 — refatoração contínua). **Quarentena reversível**, NÃO deleção
> (mesmo padrão da etapa 7 da akita-ização: `_legado/` com manifesto).
> Movidos em 20/jun/2026. Aval humano dado (André: "sim" para C05).

## O que é
Pipeline **pontual e encerrado** de ingestão da bibliografia acadêmica `drdolabela`
(217 obras, lotes 2–5, knowledge-graph). Caminhos hard-coded para
`config/skills/drdolabela`, `mapped_books.json`, `phase2_payloads.json`,
`kg_report_*.md`, `MASTER_MIND.md`. Os 18 scripts referenciam-se só entre si (ilha).

## Por que saiu da raiz
Diagnóstico C05 (`_akita_pesquisa/aplicacao/C05_refactor_orfaos.md`) + gate verificado
em 20/jun: **nenhum** script vivo importa/invoca estes 18, **nenhum** `.bat` os cita,
**nenhum** teste os cobre, e não têm `__main__` estruturado. Eram ruído permanente no
`vp100 mapa` (órfãos). Tirá-los da raiz limpa o diagnóstico sem perder nada.

## ⚠️ Dormente, não morto
Os artefatos que estes scripts consomem **ainda existem** (`mapped_books.json`,
`parsed_bibliography.json`, etc.) e a pasta `config/skills/drdolabela` permanece. Há um
**backlog de bibliografia acadêmica** registrado na memória do agente (~200+ refs, regra
"confirmar com usuário antes de produzir"). Se esse backlog for retomado, **restaure**.

## Scripts (18)
parse_bib · map_books · match_books · generate · generate_master_mind · generate_payload ·
generate_phase2_payloads · prep_subagents · dump_batches · merge_gemini_out ·
merge_kg_reports · hyperlinker · hyperlink_lote2 · lote3_link · audit_script · debug ·
dump_transcript · dump_full_transcript

## Como restaurar
Mover de volta para a raiz: `mv _legado/drdolabela/<script>.py ./` (ou `git restore` se já
versionado). Nada foi alterado nos scripts — só relocados.

## NÃO movidos (ficaram na raiz, decisão humana pendente — grupo CHECAR do C05)
`process.py` (cabeçalho cheira a drdolabela, mas imports largos — ler antes de condenar),
`exportar_para_gemini.py`/`ingerir_gemini.py` (par de delegação, pode estar ativo),
`cleanup.py`, `list_skills.py`. `marca_sonora.py` = feature pendente de fiação, não lixo.
