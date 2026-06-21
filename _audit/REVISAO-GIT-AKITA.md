# Revisão do Sistema de Git · Método Akita

> Auditoria de 10 lanes paralelas (subagentes) + síntese Opus, verificação cross-model Sonnet.
> Repo: `Galgan1/biblioteca` (público). Data: 2026-06-20. Lane: GitGuy.

## Placar de saúde

| # | Dimensão | Veredito | Pior achado |
|---|---|---|---|
| 1 | Histórico de commits | 🔴 RUIM | 65/113 (57%) são `chore(auto)` — bisect inútil |
| 2 | Branches & worktrees | 🟡 SUJO | 4 worktrees órfãos + 7 PRs parqueados atrás 66–91 commits |
| 3 | .gitignore / tracking | 🔴 FAIL | 3 arquivos de runtime rastreados (viola constituição) |
| 4 | Line endings | 🟢 OK | index já renormalizado; 0 a corrigir |
| 5 | Segredos (tree+histórico) | 🟢 PASS | nada vazado, nunca |
| 6 | CI ↔ testes | 🔴 FAIL | CI não roda `test_carrossel.py` (caminho crítico) |
| 7 | auto_git.ps1 | 🔴 REMOVER | push direto na main sem teste; fonte do ruído |
| 8 | Permissões / isolamento | 🟡 FRACO | `deny` cobre só 4 comandos; faltam os destrutivos |
| 9 | Peso de binários | 🟡 INCHADO | .git 134 MB; migração WebP incompleta = 64 MB morto |
| 10 | Doutrina GitGuy vs prática | 🔴 GAP | regra é 100% convenção, 0 imposição por máquina |

**3 verdes, 2 amarelos fortes, 5 vermelhos.** Nada catastrófico (sem vazamento, sem corrupção), mas o sistema é **disciplinado no papel e frouxo na máquina** — exatamente o que o Akita combate.

---

## Achados por severidade

### 🔴 CRÍTICO

**C1 — 3 arquivos de runtime estão versionados** · *Akita: constituição contrato 2; pilar 6*
Evidência: `datas_coletadas.json`, `historico_metadados.json`, `videos/canal-state.json` — rastreados e SEM regra no `.gitignore`. A constituição os lista como "nunca versionar". São a causa dos "modificados eternos" que aparecem em todo `git status`.
Ação (segura): `git rm --cached <cada um>` + 3 linhas no `.gitignore`. (Possível 4º: `_audit/loop_state.json`.)

**C2 — CI não testa o caminho crítico** · *Akita pilar 5 ("master só com verde") + pilar 2*
Evidência: `ci.yml` roda só `unittest discover` em `videos/` (169 ok). NÃO roda `tests/test_carrossel.py` (contratos de story/carrossel que a constituição cita) nem `testar.py` (ponto único: **182 verde** = 13 raiz + 169 videos, exit 0 confirmado). Um PR que quebre um contrato de formato passa pela CI verde.
Ação (segura): trocar o passo final do `ci.yml` por `run: python testar.py` (remover `working-directory: videos`). Casa CI ⇄ constituição com o mesmo comando do dev.

**C3 — `auto_git.ps1` viola a constituição e gerou o ruído** · *Akita pilar 5, 7; contrato 1*
Evidência: o script faz `git commit` + `git push origin main` direto, SEM rodar testes e SEM PR/revisão. É a fonte dos 65 `chore(auto)`. A task do Scheduler já foi removida → o arquivo é código morto que contradiz a regra "só GitGuy commita".
Ação (segura): remover do repo (`git rm auto_git.ps1`). Se a automação voltar algum dia, só consertada (gate `python testar.py` + abrir PR em vez de push direto).

### 🟡 ALTO

**A1 — `deny` de permissões cobre só 4 comandos** · *Akita pilar 8*
Evidência: num working tree COMPARTILHADO por sessões simultâneas, faltam os destruidores de trabalho não-commitado de outras lanes: `git reset --hard`, `git clean -f/-fd/-fdx`, `git checkout -- .`, `git restore`, `git branch -D`, `git push --delete`, `filter-branch`. Pior: a worktree `agent-a0cab…` tem `allow: rm -rf _work/*` sem nenhum `deny`.
Ação (segura): expandir o bloco `deny` em `.claude/settings.local.json` (lista pronta na lane 8).

**A2 — migração WebP nunca foi concluída** · *Akita pilar 4 (castelo de cartas)*
Evidência: 207 imagens `.webp` versionadas (gêmeas dos PNG), mas o site referencia `.png` **4668×** e `.webp` **0×**. Geraram-se os WebP, dobrou-se o peso (+64 MB), e ninguém trocou as referências. Os WebP são peso morto; os PNG não podem ser podados.
Ação (decisão do André): ou (1) concluir — trocar refs no gerador → apagar os 64 MB de PNG; ou (2) descartar os WebP não usados. Hoje versiona os dois.

**A3 — 4 worktrees órfãos** · *higiene*
Evidência: `.claude/worktrees/agent-*` (4) — todos em commits JÁ alcançáveis a partir de `main` (zero trabalho exclusivo a salvar). São lixo de subagentes de background.
Ação (segura): `git worktree remove` nos 4 (um precisa `--force`: tem 1 arquivo sujo). `.claude/` é gitignored → não polui o git, só disco.

### 🟡 MÉDIO

**M1 — doutrina GitGuy é convenção sem imposição** · *Akita pilar 7*
Evidência: a regra "só GitGuy commita" está no CLAUDE.md + 3 skills, mas NADA na máquina a impõe: `.git/hooks/` só tem `.sample`, sem `core.hooksPath`, CI não checa procedência. O próprio repo violou a regra 65×.
Ação (decisão do André): (a) `pre-commit` hook versionado que exige um marcador de autorização; OU (b) reconhecer `chore(auto)` como exceção sancionada e documentar; OU (c) aceitar que é convenção e parar de afirmar um absoluto que o histórico desmente. Recomendo (a) — torna "verde = exit code" também para a procedência.

**M2 — 7 PRs parqueados divergiram muito** · *Akita pilar 5 (small releases)*
Evidência: branches atrás 66–91 commits da main (o auto-versionamento empurrou demais). Ordem de merge: **#2 → #3 → #4 → #6 → #7 → #5(regenerar)**. `feat/premium-biblioteca` já é ancestral da main → deletar. `style/ruff-format` (#5): regenerar com `ruff format` pós-merges em vez de resolver 79 conflitos.
Ação (parcial GitGuy / parcial decisão): mergear os limpos (#2, #3); os de conflito pesado precisam de sessão dedicada.

**M3 — 4 arquivos `.claude/` rastreados (cache pré-gitignore)** · *higiene*
Evidência: `.claude/` está no `.gitignore` mas `launch.json`, `settings.local.json` e 2 `package*.json` seguem rastreados. Inspecionados: só config/allowlist, sem segredo.
Ação (segura): `git rm --cached` nos 4.

### 🟢 BAIXO

**B1** — 2 textos marcados como binário (`_kit_preview/gemini_in/extract.py`, `dirs.txt`): perdem diff por linha. Fix: `text` no `.gitattributes`.
**B2** — `$neverStage` no auto_git.ps1 tem entrada duplicada — irrelevante se o arquivo for removido (C3).

---

## 🔴 DESTRUTIVO — só com aprovação explícita do André

Estas reescrevem histórico de branch PÚBLICA (exigem `push --force`, hoje **negado** no settings) e quebram os clones / 7 branches / worktrees derivados. **GitGuy NÃO executa sozinho.**

**D1 — squash dos 65 `chore(auto)`** · ponto de corte `7b08067` (último commit manual).
Comando: `git reset --soft 7b08067 && git commit -m "chore: consolida versionamento automatico (jun)"` → depois `push --force`.
Ganho: bisect volta a funcionar, histórico legível. Risco: reescreve main pública.
**Recomendação:** adiar até os 7 PRs serem mergeados (senão recria divergência). Decisão do André.

**D2 — Git LFS para `assets/*.{png,webp,jpg}` + `*.ttf`** · tira ~100 MB do pack.
`git lfs migrate` reescreve histórico = destrutivo, force-push coordenado.
**Recomendação:** decidir A2 (WebP) primeiro; só então LFS. Decisão do André.

---

## Plano priorizado (ondas)

**Onda 1 — GitGuy autônomo, seguro, sem reescrever histórico** (fecha 4 dos 5 vermelhos):
1. C1: `git rm --cached` nos 3 runtime + `.gitignore`.
2. C2: patch `ci.yml` → `python testar.py`.
3. C3: `git rm auto_git.ps1`.
4. A1: expandir `deny` em settings.local.json.
5. A3 + M3: remover 4 worktrees órfãos + `git rm --cached` nos 4 `.claude/`.
6. B1: `.gitattributes` para os 2 textos.
→ Tudo isso num PR único `chore(git): higiene do versionamento` (verde na CI nova).

**Onda 2 — decisão do André (direção, não destrutivo ainda):**
7. A2: finalizar ou descartar WebP.
8. M1: escolher modelo de enforcement da doutrina GitGuy.
9. M2: agenda de merge dos 7 PRs.

**Onda 3 — destrutivo, aprovação explícita + execução GitGuy:**
10. D1: squash do ruído (depois dos PRs).
11. D2: Git LFS (depois de A2).

---

## Separação de autoridade

| Pode o GitGuy sozinho | Precisa do André |
|---|---|
| C1, C2, C3, A1, A3, M3, B1 (Onda 1) | A2 (direção WebP) |
| Mergear PRs limpos #2, #3 | M1 (modelo de enforcement) |
| — | D1 squash (reescreve público) |
| — | D2 Git LFS (reescreve público) |

**Nenhuma ação foi executada nesta revisão — é diagnóstico.** A Onda 1 está pronta para virar um PR assim que você aprovar.
