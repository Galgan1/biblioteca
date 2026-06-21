# C02 — CI como gate bloqueante (Akita pilar 5)

> Lane C02 (Wave 3) do plano `_akita_pesquisa/_PLANO.md`. Proposta verificável: gap → mudança → verificação por exit code.
> Constituição: `CLAUDE.md` (GitGuy-only-git, pt-BR, soberania). Norte do pilar: skill `akita` §5 / [A04].
> **Entrega = PROPOSTA + DRAFT.** Nada foi escrito em `.github/` nem em arquivo de produção. Eu não rodo git.

---

## 1. Estado atual (paths reais)

| O que | Path | Situação |
|---|---|---|
| Workflow CI existente | `.github/workflows/ci.yml` | **Já existe** (outra lane). Roda **só** `python -m unittest discover -s tests -t .` em `videos/`, em push na `main` e em PR. `permissions: contents: read`. Python 3.12. |
| Deps de teste | `requirements-dev.txt` | `pydantic`, `depthflow`. Usado pelo CI atual. |
| Bateria de testes | `videos/tests/` (20 arquivos `test_*.py`, stdlib `unittest`) | Verde = exit 0 (doc em `videos/tests/README.md`). |
| Config ruff | **NÃO EXISTE** | A tarefa supôs um `pyproject.toml` com config ruff — **não há** ruff config em lugar nenhum do repo. O único `pyproject.toml` é `videos/_flash3d/pyproject.toml` e configura **basedpyright**, não ruff. Existe um `.ruff_cache/` na raiz (ruff já rodou local, sem config commitada). |
| Ponto único de teste (`testar.py`) | **NÃO EXISTE** | É o runner proposto pela lane **C01**. Hoje o "comando único" é o `unittest discover`. |
| Secret scan | **NÃO EXISTE** no CI | Mas o `.gitignore` já barra `*.key`, `*.pem`, `*.env`, `*token*.json`, `*client_secret*`. Confirmado: `pdf-service/secret.key` está **ignorado** (`git check-ignore` confirma) e **não** é versionado. |
| Ferramenta local | `python -m ruff` → **ruff 0.15.17** disponível na máquina. |

---

## 2. Gap vs. Akita (gate bloqueante completo? secret scan? testes no CI?)

O Akita [A04] exige um gate de 3 estágios — **estilo/lint → segurança → testes** — em que **vermelho bloqueia o merge** e **master só fica verde com tudo verde**.

| Estágio do gate Akita | Hoje | Gap |
|---|---|---|
| **Lint / estilo** (`fmt --check`) | ausente do CI | **GAP**. Sem `ruff check` nem `ruff format --check`. Pior: não há config ruff commitada, então o padrão hoje seria caótico (ver risco abaixo). |
| **Segurança** (audit / secret scan) | ausente do CI | **GAP**. `.gitignore` é prevenção do working tree, mas não varre **histórico**. Falta uma rede (gitleaks/trufflehog) que pegue um segredo commitado por engano em qualquer commit. |
| **Testes** | **presente** ✅ | Cobre o caminho crítico (`videos/tests`). É o único estágio que já existe. |
| **needs/ordem** (vermelho cedo bloqueia) | n/a | **GAP**. Hoje só há 1 job; não há encadeamento "testes só rodam se lint+segurança passarem". |

**Achado crítico (sizing do gate):** rodei ruff em report-only (sem alterar nada):
- `python -m ruff check .` → **489 erros** (top: 278 `E702`, 63 `E401`, 38 `E701`, 32 `F401`).
- `python -m ruff format --check .` → **294 de 296** arquivos seriam reformatados.

Ou seja: ligar um gate ruff "cru" hoje deixaria a `master` **permanentemente vermelha**. O gate exige **primeiro uma config ruff enxuta commitada** (pré-requisito), não só o YAML.

---

## 3. Proposta — gap → mudança → verificação por exit code

> Princípio Akita: a IA não decide que "passou"; **verde = exit code**. Cada item abaixo é verificável localmente ANTES de subir o YAML.

### P1 — Lint/estilo no CI (`ruff check` + `ruff format --check`)
- **Gap:** sem estágio de estilo no gate.
- **Mudança:** adicionar job `lint` (no `ci_draft.yml`) com `ruff==0.15.17` fixado (= versão local, evita drift). **Pré-requisito bloqueante:** commitar uma config ruff em `pyproject.toml` na raiz com `select`/`exclude` enxutos (e/ou `ruff format` aplicado uma vez) — senão os 489 erros / 294 arquivos travam a master. **Esta lane NÃO commita a config nem reformata** (é mudança de produção + git = GitGuy/Bibliotecario); apenas a especifica como dependência.
- **Verificação local (exit code):**
  ```bash
  python -m ruff check .            # objetivo: exit 0
  python -m ruff format --check .   # objetivo: exit 0 (nenhum "would reformat")
  echo "EXIT=$?"                     # só sobe o gate quando os dois derem 0
  ```

### P2 — Secret scan no CI (gitleaks)
- **Gap:** nenhuma varredura de segredo no histórico.
- **Mudança:** job `secret-scan` com `gitleaks/gitleaks-action@v2` e `fetch-depth: 0` (varre todos os commits, não só o working tree). Complementa — não substitui — o `.gitignore`.
- **Verificação local (exit code):**
  ```bash
  # binário gitleaks (uma vez) — depois:
  gitleaks detect --no-banner --redact   # exit 0 = nenhum segredo; exit 1 = vazamento
  echo "EXIT=$?"
  ```
  (Sem o binário, o próprio job do PR é a primeira verificação — mas o ideal Akita é provar local antes.)

### P3 — Testes via ponto único idempotente
- **Gap:** o CI atual chama o comando de teste direto (`unittest discover`), o que acopla a CI ao layout. O Akita [A07] pede **ponto único idempotente** (nada de comando solto).
- **Mudança:** o job `testes` prefere `python testar.py` (runner da lane C01) e cai no `unittest discover` atual como fallback enquanto `testar.py` não existir. `needs: [lint, secret-scan]` garante a ordem do gate.
- **Verificação local (exit code):**
  ```bash
  # quando C01 entregar o runner:
  python testar.py ; echo "EXIT=$?"        # objetivo: exit 0
  # fallback atual (já verde hoje):
  cd videos && python -m unittest discover -s tests -t . ; echo "EXIT=$?"
  ```

### Sequência recomendada de adoção (para não pintar a master de vermelho)
1. **Primeiro** commitar a config ruff + reformatar uma vez (lane de produção/GitGuy) → `ruff check`/`format --check` local = exit 0.
2. **Depois** o GitGuy mescla o `ci_draft.yml` ao `.github/workflows/ci.yml` (lint + secret-scan + testes).
3. `testar.py` (C01) entra quando pronto; o fallback cobre o intervalo.

---

## 4. Artefato

`_akita_pesquisa/aplicacao/ci_draft.yml` — workflow DRAFT com os 3 jobs (`lint` → `secret-scan` → `testes`, este com `needs`), ruff fixado em `0.15.17`, gitleaks com histórico completo, e teste preferindo `testar.py` com fallback ao `unittest discover` atual. Cabeçalho do arquivo lista os 2 pré-requisitos (config ruff + `testar.py`) e o aviso de não copiar para `.github/` sem aval.

---

## 5. Risco / colisão (não pisar no `.github/` de outra lane)

- **Colisão de lane:** `.github/workflows/ci.yml` **já existe** e é de outra lane (GitGuy/Bibliotecario). **Não editei, não sobrescrevi, não criei nada em `.github/`.** O DRAFT vive só em `_akita_pesquisa/aplicacao/`. A fusão é decisão do GitGuy (constituição §1: só ele commita/mescla).
- **Suposição da tarefa que não bateu:** a tarefa afirmava existir `pyproject.toml` com config ruff — **não existe**. O DRAFT trata isso como pré-requisito explícito em vez de assumir que está pronto (honestidade de fonte, Akita).
- **Risco de master vermelha:** ligar ruff sem config = 489 erros / 294 arquivos reformatáveis. Mitigado por ordenar config-ruff-primeiro (seção 3).
- **Dependência externa:** `gitleaks-action` é action de terceiros e adiciona rede/supply-chain ao CI. Alternativa soberana: rodar o binário `gitleaks`/`trufflehog` baixado por hash. Decisão fica com a lane de segurança/GitGuy.
- **`testar.py` ainda não existe:** o DRAFT não quebra por isso (fallback), mas a forma final depende da entrega da lane C01.
