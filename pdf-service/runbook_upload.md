# Runbook — converter um upload em skill + `{SLUG}_data.py`

Você é um agente de produção da Biblioteca (cheat sheets de livros). Recebeu UM
arquivo de livro enviado pelo admin. Sua entrega são DOIS artefatos no disco —
nada além disso. NÃO faça deploy, NÃO use git, NÃO toque em nenhum outro livro,
NÃO publique em rede. O worker que te chamou cuida da publicação depois, fora de
você. Trabalhe em pt-BR.

Variáveis deste job (já substituídas pelo worker):
- SLUG do livro: `{SLUG}`
- Arquivo de origem: `{SOURCE_FILE}`

## Passo 1 — Converter o arquivo em skill (book-to-skill)

Rode a skill **book-to-skill** sobre `{SOURCE_FILE}`, gerando a skill em
`~/.claude/skills/{SLUG}/` (SKILL.md + chapters/ + glossary + patterns +
cheatsheet). Modo de conteúdo: se o livro for prosa, use texto; se tiver
tabelas/código/fórmulas, use técnico. Esta skill é a matéria-prima do Passo 2.

## Passo 2 — Autorar `{SLUG_UNDER}_data.py` no diretório de trabalho atual

Crie o arquivo `{SLUG_UNDER}_data.py` no **diretório de trabalho atual** (onde
você já está — é onde mora `leis_da_natureza_humana_data.py`, o padrão-ouro).
ATENÇÃO ao nome: o slug usa hífen, mas o **nome do arquivo usa underscore** (é
nome de módulo Python). Ex.: slug `leis-da-natureza-humana` → arquivo
`leis_da_natureza_humana_data.py`. Replique
EXATAMENTE a estrutura e o padrão de qualidade desse padrão-ouro — abra-o e
siga-o à risca. O arquivo define duas variáveis no nível do módulo: `BOOK`
(dict) e `CHAPTERS` (lista).

### `BOOK` (dict)
Mesmas chaves do padrão-ouro: `title`, `author`, `header_light`, `header_bold`,
`subtitle`, `intro`, `description`, `tags` (lista), `progress`, `cover`
(`"assets/{SLUG}-cover.png"`) e `overview_cards` (lista de 2–3 cards seguindo a
régua do card abaixo, com `wide:True` no primeiro quando fizer sentido).

### `CHAPTERS` (lista, >= 3 itens)
Cada capítulo é um dict com `slug` (`"chNN-tema"`, único), `sub`
(`"CAPÍTULO N: ..."`), `intro` (2–3 frases), `cards` (lista), `lessons_title`
(`"Lições-Chave do Capítulo N"`) e `lessons` (lista de 3 frases).

### A RÉGUA DO CARD (vale para overview_cards e para todo cards[])
Cada card é um dict com:
- **`ic`** — UM ícone EXATAMENTE desta lista (qualquer outro é bloqueante):
  `arrow book bookmark bubble bulb cards clock constellation eye fork gap key
  layers leaf lens link mask masks mountain person pin pivot play scale shelf
  shield spark spiral steps sword target triangle wave wrench`
- **`t`** — título curto do card (não-vazio).
- **`emph`** — trecho a destacar; DEVE ser uma substring EXATA de `t` (mesmas
  letras, acentos e maiúsculas/minúsculas). Se não for casar exato, omita `emph`.
- **`b`** — corpo de ~260–340 caracteres, em pt-BR, com EXATAMENTE um
  `<strong>...</strong>` (nem zero, nem dois) marcando a frase-chave. Use aspas
  curvas (“ ” ‘ ’) e travessões (—), nunca aspas retas. Pode usar `<br>`.
- **`tip`** — dica rotulada, no formato `"<strong>Rótulo:</strong> texto"` (ex.:
  `<strong>Como aplicar:</strong> ...`, `<strong>Regra:</strong> ...`,
  `<strong>Modelo mental:</strong> ...`, `<strong>Sinal de alerta:</strong> ...`).
- **`warn`** — `True` em ~1 card por capítulo (o de maior risco/alerta); omita
  nos demais.

Codificação UTF-8 (`# -*- coding: utf-8 -*-` no topo, como no padrão-ouro).

## Fronteiras (NÃO faça)
- NÃO rode `publicar_livro.py`, `gerar_*.py`, scp, ssh nem qualquer deploy.
- NÃO rode `git` (add/commit/push) nem crie PR.
- NÃO edite outros `*_data.py`, `books.json`, `index.html` nem outro livro.
- NÃO publique em YouTube/Instagram/Amazon nem gere vídeo.

Sua tarefa termina quando existirem, no disco: a skill em
`~/.claude/skills/{SLUG}/` e o arquivo `{SLUG_UNDER}_data.py` no diretório de
trabalho atual, pronto para passar no `data_gate.py {SLUG}`. Não há mais nada a fazer.
