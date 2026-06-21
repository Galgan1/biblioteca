# C01 — Estado de testes + harness de TDD (Akita, pilar nº1)

> Aplicação do método Akita ao projeto Biblioteca/Minuto Real.
> Pilar nº1 = **TDD real: "verde = exit code"**, comando único, output parseável, sem setup humano, e **um bug vira teste de regressão**. [akita/SKILL.md §2]
> Todos os números abaixo foram **medidos por execução** (exit code), não estimados.

---

## Estado atual (com paths/linhas)

**Existe UMA ilha de TDD bem-feita — só no subprojeto de vídeo.**

- `videos/tests/` — **21 arquivos `test_*.py`** em `unittest` puro (stdlib, zero dependência nova).
  - Rodam por comando único de dentro de `videos/`:
    `python -m unittest discover -s tests -t .` (documentado em `videos/tests/README.md:6-10`).
  - **Medido agora: `Ran 169 tests ... OK`, exit 0, ~6,5 s.** Bateria 100% verde.
  - Padrão: importam o módulo sob teste direto (`from dag import ...`) ou via
    `sys.path.insert(0, parent)` (ex.: `test_text_budget.py:8-10`). `if __name__ == '__main__': unittest.main()` em cada um.
  - Cobertura é só do **caminho crítico do pipeline de vídeo**: `dag.py`, `contracts.py`,
    `circuit_breaker.py`, `pipeline_state.py`, `text_budget.py`, `qc*`, `mixmaster`, `splatting`, etc.
    (`videos/tests/README.md:16-24`).
  - Estado de runtime é isolado em arquivos temporários nos testes (não toca dados reais).

**A RAIZ do projeto (o grosso da produção) tem cobertura ~nula.**

- `vp100.py` (908 linhas, raiz) — simulador/diagnóstico cheio de **lógica pura crítica**
  e **ZERO testes**: `fmt_tempo` (`vp100.py:178-180`), `carregar_dag`+`topo`+`groups`
  (`:104-128`), `custo_etapa` (`:174-175`), `plan_publish` (`:261-300`),
  `calc_pipeline_state` (`:334-365`).
- Geradores de produção da raiz (`gerar_*.py`, `publicar_livro.py`, `build_design.py`,
  `aplicar_texto.py`, dezenas de `*_data.py`) — **sem nenhum `test_*.py`** que os cubra.
- Verificação por busca: `def test_` / `import unittest` / `import pytest` casam **apenas**
  dentro de `videos/tests/` em todo o repo (fora de `node_modules`/`site-packages`).

**Não há ponto único de teste do PROJETO INTEIRO.**

- `verificar.bat` (raiz) **não é uma bateria de testes**: roda 4 comandos `vp100` (custo/doctor)
  e imprime na tela — **sem asserts, sem exit code agregado** (`verificar.bat:1-14`). É smoke manual.
- Não existe `conftest.py`, `pytest.ini`, `Makefile`, `tox.ini` nem `testar.py`/`run_tests` na raiz.
- **`pytest` não está instalado** (`No module named pytest`); ambiente é **Python 3.13.7** + stdlib `unittest`.
  (Coerente com a soberania do projeto: nada de dependência nova.)

---

## Gap vs Akita

| Exigência Akita (§2) | Hoje |
|---|---|
| "Verde = exit code", bateria 100% verde antes de consolidar | ✅ **só** em `videos/` (169 verdes); ❌ a raiz não tem bateria |
| **Comando único** que roda toda a bateria e devolve exit code | ❌ existem **dois mundos**: `videos/` tem um comando próprio; a raiz, nenhum. Quem consolida na raiz não tem como "ficar verde" |
| Teste rodável pelo agente, **output parseável, sem setup humano** | ✅ (unittest, stdlib) onde há teste |
| Cobertura > 1:1 em módulos críticos | ❌ `vp100.py` e geradores da raiz = 0% |
| **Um bug → teste de regressão** | parcial: cultura existe em `videos/`, ausente na raiz |
| CI bloqueante que roda a bateria (§5) | ❌ inexistente (etapa futura, já anotada no README) |

**Gap nº1:** não há **ponto único idempotente** que rode *tudo* (raiz + `videos/`) e devolva
um exit code agregado. Sem isso, o agente que mexe na raiz não tem "definição de pronto" executável.
**Gap nº2:** `vp100.py`, que é justamente a ferramenta de diagnóstico do pipeline, é a mais exposta
(lógica pura, alto uso) e a menos testada.

---

## Proposta (gap → mudança → COMO VERIFICAR por exit code)

### P1 — Ponto único idempotente de teste: `testar.py` (raiz)
- **Gap:** dois mundos de teste, nenhum agregador; a raiz não tem "verde".
- **Mudança (interface, não implementar agora):** um `testar.py` na raiz que:
  1. roda a bateria de `videos/` via `unittest` discover (`-s videos/tests -t videos`);
  2. roda a bateria da raiz (`_akita_pesquisa/aplicacao/test_*.py` hoje; futura `tests/` da raiz);
  3. agrega resultados e **sai com `0` sse tudo verde, `≠0` caso contrário**;
  4. é **idempotente e sem setup humano** (sem rede, sem credencial, sem seed manual);
  5. aceita `--json` para output parseável (alinha ao estilo `--json` já presente no `vp100.py`).
  - Idempotência/isolamento (Akita §8): nada de comando solto — este é o wrapper revisável único.
- **COMO VERIFICAR por exit code:**
  ```bash
  python testar.py            # esperado: imprime resumo e exit 0 quando tudo verde
  echo $?                     # 0 = consolida; ≠0 = não consolida
  python testar.py --json     # objeto {passed,failed,total} parseável
  ```
  Critério de aceite executável: numa árvore limpa, `python testar.py; echo $?` ⇒ `0`;
  injetando um teste que falha de propósito, ⇒ `≠0`. (mesma prova de fogo do artefato abaixo)

### P2 — Quebrar a cobertura zero da raiz começando por `vp100.py`
- **Gap:** lógica pura crítica da raiz sem rede de segurança.
- **Mudança:** testar primeiro as **funções puras** (sem I/O): `fmt_tempo`, `topo`/`groups`
  do DAG de fallback, `custo_etapa` — e depois as semi-puras (`plan_publish`,
  `calc_pipeline_state`) com `canal-state.json`/`books.json` **fixos de fixture** (não os reais).
  É o **artefato inicial** desta entrega (ver abaixo) — já criado e verde.
- **COMO VERIFICAR por exit code:**
  ```bash
  python _akita_pesquisa/aplicacao/test_vp100_puro.py; echo $?   # 0 = verde
  ```

### P3 (futuro, fora desta etapa) — CI bloqueante (Akita §5)
- **Mudança:** workflow que roda `python testar.py` em cada push; **vermelho bloqueia o merge**.
- **COMO VERIFICAR:** o job de CI falha (exit ≠0) quando qualquer teste quebra. Já existe
  `.github/` no working tree (não auditado aqui) — candidato natural a receber o gate.

---

## Artefato inicial (criado nesta entrega)

**Arquivo:** `_akita_pesquisa/aplicacao/test_vp100_puro.py` (fora da produção, por enquanto).

- **11 testes** `unittest` sobre funções puras de `vp100.py` (`fmt_tempo`, ordenação topológica
  do DAG de fallback, `custo_etapa`). Importa `vp100.py` por caminho absoluto — seguro porque
  `main()` está sob `if __name__ == '__main__'` (sem efeito colateral ao importar).
- **Comando único:** `python _akita_pesquisa/aplicacao/test_vp100_puro.py`
  (rodar por discover exige pacote importável — Python recusa pasta começada por `_`;
  por isso o comando canônico é **pelo caminho do arquivo**).
- **Verificação por exit code (medida agora):**
  - verde: `Ran 11 tests ... OK`, **exit 0**.
  - prova de regressão: ao mutar 1 assert ⇒ `FAILED (failures=1)`, **exit 1**;
    restaurado ⇒ **exit 0**. Logo é teste real, não no-op.

---

## Risco / colisão

- **Sem colisão com produção:** só foram **criados** arquivos novos dentro de
  `_akita_pesquisa/aplicacao/`. Nenhum arquivo de produção foi editado; **nenhum comando git** rodado.
- **`testar.py` (P1) ainda NÃO foi criado** — é proposta de interface. Quando criado, será na raiz
  (lane do Programador/Bibliotecario) e deve **importar/disparar** as baterias, não duplicá-las.
- **Pasta `_`:** `unittest discover` não importa pastas iniciadas por `_`. Decisão consciente:
  enquanto o teste mora em `_akita_pesquisa/`, o comando é **pelo caminho do arquivo**. Ao consolidar,
  migrar para `tests/` na raiz (aí discover volta a funcionar) — migração é trabalho da etapa de
  consolidação, não desta pesquisa.
- **Git:** este projeto proíbe a esta lane commitar/pushar (só GitGuy). Cumprido: zero git.
- **Determinismo:** o artefato usa só funções puras e `DEFAULT_DAG`/`DEFAULT_PRICES` (constantes do
  módulo). Se um dia `videos/dag.py` mudar, o teste do *fallback* não quebra (ele testa a lógica do
  fallback, não o DAG real) — escolha proposital para não acoplar a runtime.
