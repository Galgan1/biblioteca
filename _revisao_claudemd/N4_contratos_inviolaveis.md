# N4 — Auditoria: Constituição × Código (Contratos Invioláveis 1-7, "O que versionar", [ADIÇÃO])

> Auditor sênior, read-only. Akita: verde = exit code. Alvo = `CLAUDE.md` do projeto biblioteca.
> Data: 2026-06-20. Comando único provado: `python testar.py` → **EXIT=0, 451 testes VERDE**.

## Tabela de veredito

| # | Item da constituição | Veredito | Evidência |
|---|---|---|---|
| 1 | Contrato 2: "Amazon/afiliados = `afiliados.json`" | **DRIFT (caminho)** | O arquivo existe, mas em `afiliados/afiliados.json` (subpasta), **não na raiz**. A constituição cita o nome nu, sugerindo raiz. Confirmado por `gerar_metadados.py:40` (`ROOT/"afiliados"/"afiliados.json"`), `inserir_candidatos.py:27`, `afiliados/gerar_links.py:17`. `AKITA-DIAGNOSTICO.md:9` já registra o caminho certo (`afiliados/afiliados.json`). Tag `andregalgani-20` vive nesse JSON + é injetada em HTMLs/postadores. |
| 2 | Contrato 4: "um gerador canônico (`gerar_livro.py`)" | **CONFERE** | `gerar_livro.py` existe e se autodeclara "GERADOR UNIVERSAL de livro para a biblioteca" (lê `<slug>_data.py` → `.html` + páginas + `books.json`). `gerar_carrossel.py` NÃO concorre: gera carrossel de Instagram (peça), reusa ícones de `gerar_livro.py`. Não há ambiguidade de "qual gera o site". |
| 3a | [ADIÇÃO isolamento]: "venv/`requirements.txt`" | **DRIFT (arquivo)** | **Não existe `requirements.txt` na raiz.** Existe `videos/requirements.txt` (escopo só da lane de vídeo) e `requirements-dev.txt` na raiz. A CI (`ci.yml:33-34`) instala `requirements-dev.txt` + `videos/requirements.txt` — nunca um `requirements.txt` raiz. O próprio comentário `ci.yml:30` fala "o requirements.txt de runtime" referindo-se a `videos/requirements.txt`. A constituição cita o nome genérico como se houvesse um único na raiz. |
| 3b | [ADIÇÃO teste]: "Ponto único `python testar.py`" | **CONFERE** | `testar.py` existe, agrega `tests/` (raiz) + `videos/tests/` em subprocessos isolados, devolve UM exit code. Rodado: **EXIT=0**; `raiz 17 OK · videos 434 OK · TOTAL 451 VERDE`. É exatamente o que a CI roda (`ci.yml:38`). |
| 4 | "skill `akita` / `akita.md`" (linha ~9) | **DRIFT (nome)** | O arquivo da skill é `C:\Users\User\.claude\skills\akita\SKILL.md` (frontmatter `name: akita`). **Não existe `akita.md`.** Convenção de skill é `SKILL.md`. A constituição cita `akita.md` como nome alternativo inexistente. |
| 5a | `canal-state.json` tem chave `api_health` | **CONFERE** | `videos/canal-state.json` tem `api_health` — e é a **única** chave do JSON (`keys() == ['api_health']`). |
| 5b | `MODO-SOBERANO.md` existe | **CONFERE** | Existe na raiz (`MODO-SOBERANO.md`, 4012 bytes, 14/jun). Citado pelo Contrato 7 (Soberania). |

## Resumo dos DRIFTs (severidade)

| Drift | Severidade | Por quê |
|---|---|---|
| #1 `afiliados.json` (caminho) | **Média** | Path real é `afiliados/`. Não quebra código (todos os consumidores usam o caminho completo), mas a constituição engana quem grep só a raiz. Fonte da verdade nº 2 com endereço impreciso. |
| #3a `requirements.txt` raiz inexistente | **Média** | A constituição manda usar `venv/requirements.txt` "antes de qualquer gate"; o arquivo nu não existe — são dois (`requirements-dev.txt` + `videos/requirements.txt`). Risco: agente novo roda `pip install -r requirements.txt` e falha. |
| #4 `akita.md` (nome) | **Baixa** | Nome alternativo inexistente; o `SKILL.md` resolve via skill-loader. Só confunde quem procura o arquivo pelo nome citado. |

## Correções propostas (no `CLAUDE.md`, NÃO aplicadas — read-only)

1. **Contrato 2** — trocar `Amazon/afiliados = \`afiliados.json\`` por `Amazon/afiliados = \`afiliados/afiliados.json\`` (alinha com `AKITA-DIAGNOSTICO.md:9`).
2. **[ADIÇÃO isolamento]** — trocar `venv/\`requirements.txt\`` por `venv + \`requirements-dev.txt\` (raiz) e \`videos/requirements.txt\` (lane vídeo)` — ou criar um `requirements.txt` raiz que faça `-r requirements-dev.txt` / `-r videos/requirements.txt` se quiser honrar o nome genérico. Recomendo ajustar o texto (menos código novo).
3. **Linha ~9 (Modo de trabalho)** — trocar `skill \`akita\` / \`akita.md\`` por `skill \`akita\` (\`SKILL.md\`)`.

## CONFERE (sem ação)
Contrato 4 (`gerar_livro.py` canônico), ponto único `testar.py` (451 verde), `canal-state.json` → `api_health`, `MODO-SOBERANO.md`.

## NÃO-VERIFICÁVEL
Nenhum item ficou não-verificável nesta rodada.
