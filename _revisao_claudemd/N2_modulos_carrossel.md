# N2 — Auditoria: "Estrutura de módulos (`gerar_carrossel.py`)" + "Guardas / anti-fantasma"

> Auditor sênior · read-only · Akita (verde = exit code) · pt-BR
> Alvo: `CLAUDE.md` do projeto biblioteca — seções **"Estrutura de módulos (`gerar_carrossel.py`)"** e **"Guardas de máquina: CI real + anti-fantasma"**.
> Diretório: `C:\Users\User\.gemini\antigravity\scratch\biblioteca`
> Data: 2026-06-20

## Veredito por afirmação

| # | Afirmação na constituição | Verificação (evidência) | Veredito |
|---|---|---|---|
| 1 | "`gerar_carrossel.py` é o thin orchestrator (target: ≤ 350 linhas)" | `wc -l gerar_carrossel.py` = **895 linhas** (2,56× o teto). CSS inline (linha 754 + `STORY_CSS`), `montar_slides` inline (456), `build_stories` inline (871). Não é "thin", é monolítico. | **DRIFT (alto)** |
| 2 | "CSS → `_carousel_css.py`; slides → `_carousel_slides.py`; stories → `_carousel_stories.py`" — existem **E** são importados por `gerar_carrossel.py`? | Os 3 arquivos **existem e estão rastreados** (`git ls-files` lista os 4). Linhas: `_carousel_css.py`=344, `_carousel_slides.py`=259, `_carousel_stories.py`=70. **MAS** `gerar_carrossel.py` NÃO importa nenhum deles (imports reais: `gerar_livro`, `instagram_post`, `tokens`, stdlib — linhas 22-30). Único acoplamento entre eles: `_carousel_stories.py:11` importa `_carousel_slides`. São **ilhas órfãs**: ninguém em produção as consome. | **DRIFT (alto)** — existem mas NÃO são importados pelo orquestrador |
| 3 | Anti-fantasma: "`python audita_fantasmas.py` bloqueia .py rastreado que importe módulo de raiz NÃO versionado". Passa? O problema do `gerar_carrossel` importando `_carousel_*` "nunca commitados" foi resolvido? | `python audita_fantasmas.py` → `audita_fantasmas: OK - nenhum fonte rastreado importa modulo orfao.` **EXIT=0**. Os `_carousel_*.py` foram commitados em `79e7b56` (Onda 1). O guarda passa porque **tudo está versionado**. | **CONFERE** — guarda verde; bug do clone quebrado resolvido por versionamento |
| 4 | "`.github/workflows/ci.yml` roda `python testar.py`" | `ci.yml` linha 38: `run: python testar.py` (step "Rodar o mural"). Antes roda `python audita_fantasmas.py` (linha 27, pré-pip) e instala `requirements-dev.txt` + `videos/requirements.txt` (ambos rastreados). `testar.py` agrega `tests/` + `videos/tests/`. | **CONFERE** |

## Nuance importante sobre o item 3 (não confundir guarda com modularização)

O `audita_fantasmas.py` verifica **apenas** se um `.py` rastreado importa um módulo de raiz **órfão (não versionado)**. Ele NÃO verifica se a modularização prometida foi de fato adotada. Resultado:

- **O guarda está verde** porque os `_carousel_*.py` foram committados — o cenário do bug original (importar módulo não versionado → `ImportError` em clone limpo) não existe mais.
- **Mas o guarda passaria mesmo se ninguém importasse os módulos** — que é exatamente o estado atual. Os 673 linhas de `_carousel_*.py` estão versionadas e mortas (dead code rastreado), enquanto `gerar_carrossel.py` mantém CSS/slides/stories **inline**.

Ou seja: a "Onda 1" resolveu o **un-break do repo** (clone limpo não quebra mais), mas **não concluiu a refatoração modular** que a constituição descreve como fato consumado. A constituição descreve o estado-ALVO; o código está no estado-INTERMEDIÁRIO.

## Correções propostas (não aplicadas — read-only)

Há dois caminhos coerentes; o humano decide o *quê*:

**Opção A — fazer o código bater com a constituição (concluir a refatoração).**
Mover CSS / `montar_slides`+slides / `build_stories`+stories de `gerar_carrossel.py` para os respectivos `_carousel_*.py` e importá-los, derrubando o orquestrador para ≤ 350 linhas. Verificar com: `python testar.py` verde (contratos do gerador em `tests/test_carrossel.py` continuam passando) + `wc -l gerar_carrossel.py` ≤ 350. (Mudança grande → lane do Bibliotecario, via Akita + /loop-agente.)

**Opção B — fazer a constituição bater com o código (corrigir o doc).**
Se a refatoração não vai acontecer agora, ajustar a seção "Estrutura de módulos" para descrever o estado real (orquestrador monolítico ~895 linhas; `_carousel_*.py` como rascunho não integrado) OU remover os 3 órfãos do git. Caso contrário a constituição vira "superstição" (memória não validada) e mascara 673 linhas de dead code rastreado.

**Adicional (item 3, opcional):** se o objetivo é IMPOR a modularização (não só evitar clone quebrado), o `audita_fantasmas.py` não basta — seria preciso um teste que afirme que `gerar_carrossel.py` importa os módulos OU que está abaixo do teto de linhas. Hoje nenhum gate impõe o "thin orchestrator".

---

## Resumo (≤ 8 linhas)

1. **DRIFT (alto)** — `gerar_carrossel.py` tem **895 linhas**, 2,56× o teto de 350 ("thin orchestrator" é falso; CSS/slides/stories estão inline).
2. **DRIFT (alto)** — `_carousel_css/_slides/_stories.py` **existem e estão versionados**, mas `gerar_carrossel.py` **NÃO os importa**; são ilhas órfãs (673 linhas de dead code rastreado).
3. **CONFERE** — `python audita_fantasmas.py` → EXIT=0; o clone quebrado da Onda 1 foi resolvido por versionar os módulos.
4. **CONFERE** — `ci.yml` roda `python audita_fantasmas.py` (pré-pip) e `python testar.py` (gate final).
5. Nuance: o anti-fantasma passa porque tudo está committado, mas **não impõe** a modularização — passaria mesmo com os módulos órfãos (como hoje).
6. A constituição descreve o estado-ALVO; o código está no estado-INTERMEDIÁRIO (un-break feito, refatoração não concluída). Decidir: concluir refatoração (A) ou corrigir o doc/remover órfãos (B).
