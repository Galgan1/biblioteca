# CLAUDE.md — Projeto Biblioteca

> Complementa o CLAUDE.md raiz em `scratch/`. Regras específicas deste projeto.

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
