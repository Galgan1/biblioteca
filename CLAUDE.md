# CLAUDE.md — Projeto Biblioteca (bazuka)

> Complementa o CLAUDE.md raiz em `scratch/`. Regras específicas deste projeto.

## Modo de trabalho PADRÃO (obrigatório neste projeto)

Toda tarefa não-trivial neste projeto roda sob dois padrões. Não é opcional.

1. **Método = Akita (anti-vibe coding).** Siga a skill `akita` / `akita.md`: planejar antes de codar (tarefas atômicas), **TDD real** (verde = exit code de teste, nunca "a IA achou que está certo"), humano decide o *quê* / IA o *como*, refatoração contínua, CI obrigatória, isolamento de execução. Constituição = este arquivo.

2. **Execução = `/loop-agente`.** Não responda/entregue direto: passe pelo ciclo **Planner → Executor → Verifier**, com **rúbrica** definida antes e **verificação cross-model** (juiz ≠ autor: Opus ↔ Sonnet). Só entrega o que passar na rúbrica (parada em 5 tentativas). Para tarefas grandes, o Planner decompõe em subagentes (mesmo sistema).

Tarefas triviais (ex.: 1 linha, leitura simples) dispensam o cerimonial — use bom senso. Tudo que gera/edita código de produção: Akita + loop, sem exceção.

## Git — REGRA ABSOLUTA: não commitar, não fazer push

**Você NÃO é o responsável pelo git deste projeto.**

O agente **GitGuy** é a única lane autorizada a fazer `git commit`, `git push` e criar PRs no repositório `Galgan1/biblioteca`.

**O que VOCÊ faz:**
- Cria, edita e gera arquivos no disco normalmente.
- Quando terminar, avisa o usuário que o trabalho está pronto no disco.

**O que VOCÊ nunca faz:**
- `git commit` (nem com `-m`, nem interativo)
- `git push` (nem `origin`, nem qualquer remote)
- `git add` seguido de commit
- `gh pr create` ou qualquer operação de PR

**Por quê:** múltiplos agentes editam o mesmo working tree. Commits fora de hora criam estados inconsistentes, enterram trabalho de outras lanes no meio do histórico e dificultam o rollback. O GitGuy tem contexto de TODAS as lanes antes de commitar.

**Quando o GitGuy age:** o usuário chama `/create-pr` em qualquer sessão. GitGuy então revisa tudo que está no disco, agrupa por lane, commita com mensagem adequada e empurra.

## O que versionar (referência para o GitGuy)

| Versionar ✅ | Nunca versionar ❌ |
|---|---|
| `*_data.py` — fonte autoral dos livros | `videos/canal-state.json` — runtime |
| `*.html`, `assets/`, `books.json` | `datas_coletadas.json` — runtime |
| `gerar_*.py`, `publicar_livro.py` | `historico_metadados.json` — runtime |
| `assets/style.css`, `script.js` | `_remote_books.json`, `_ssh_err.txt` — temp |
| Skills e skills data | `pipeline/state/`, `pdf-service/cache/` |

## Contratos Invioláveis — Constituição (Akita, pilar 6)

Regras cross-cutting que **nenhuma lane quebra**. O detalhe de cada lane vive na skill da lane; aqui ficam só os contratos que valem para todo o projeto. Norte em `AKITA-PLANO-ALVO.md`; estado atual em `AKITA-DIAGNOSTICO.md`.

1. **Git:** só o **GitGuy** commita/pusha/cria PR (ver seção acima).
2. **Fontes da verdade** (edite a fonte, nunca o derivado): livros = `<slug>_data.py` (o HTML é gerado a partir dela); Amazon/afiliados = `afiliados.json`; estado do canal = `canal-state.json` (runtime, não versionar).
3. **Qualidade (Akita):** nada se consolida sem **teste verde** (verde = exit code), não "a IA achou que está certo"; execução só por **ponto único idempotente** (nada de comando solto); na dúvida, o verificador reprova. Alvo: CI verde antes do merge.
4. **Geração do site:** um gerador canônico (`gerar_livro.py`); estética "cheat-sheet verde" e tokens de marca são **únicos** (não inventar cor/variável). Detalhe: skill `biblioteca`.
5. **Distribuição/afiliado:** link Amazon só de **produto** (`/dp/`, `/gp/`), nunca busca; no Instagram o link vai na **bio** (legenda não é clicável); no Facebook, **post nativo + link no 1º comentário** (não post-link). Detalhe: skills das lanes.
6. **Idioma:** todo conteúdo em **pt-BR** (pt-PT é bloqueante).
7. **Soberania:** o pipeline roda local/grátis; sem crédito de IA externa há rota de fuga (voz → edge-tts). Detalhe: `MODO-SOBERANO.md`.
