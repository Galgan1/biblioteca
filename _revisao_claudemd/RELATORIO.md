# Relatório de Saúde — CLAUDE.md (×2) + skill /akita
> Revisão "0 a produção" (20/jun/2026) via /loop-agente · 7 revisores paralelos + verificação direta.
> Detalhe por lente: N1..N7 nesta pasta. Cada achado tem evidência (file:line/comando).

## Veredito geral: **7/10 — ossos bons, mas com 1 rachadura grave de integridade**
A constituição tem contratos REAIS, gate de CI e honestidade de fonte. Mas a seção-vitrine
("Contratos de Formato") descreve uma worktree não-commitada, não o código vivo — e o gate
oficial é cego a ela. Constituição que afirma um enforcement que não tem corrói a confiança.

---

## ALTA
1. **Carrossel: o doc descreve a worktree, não o código vivo** (N1,N2,N7). `gerar_carrossel.py` = **895 linhas** (contrato diz ≤350), monolito; **NÃO importa** `_carousel_css/_slides/_stories` — eles existem mas estão **órfãos** (~673 linhas de dead code). A versão que cumpre os contratos (lessons, story 4 frames, insights) só vive em `.claude/worktrees/...` não-commitada. Viola o próprio **pilar 9** ("<500 linhas").
2. **Gate cego + claim falso** (N1). CLAUDE.md L17: "verificado por `pytest tests/test_carrossel.py`" e "violar contrato = teste vermelho". Real: `pytest tests/test_carrossel.py` → **6/8 FALHAM (exit 1)**; mas o gate oficial `python testar.py` (unittest discover) **não coleta** esse arquivo pytest-style → fica **VERDE**. Contratos violados + gate verde = a frase de enforcement é **falsa hoje**.
3. **Contradição constituição × skill** (N5). "Modo de trabalho PADRÃO" (L11-13) impõe `/loop-agente` cross-model como obrigatório "sem exceção"; mas **akita SKILL.md §11** diz que multi-modelo/juiz **NÃO é default** ("otimização prematura"; "acréscimo nosso, não do Akita"). O CLAUDE.md manda seguir a skill e a contradiz.
4. **Dead references confirmadas** (N6,N7 + verificação direta): akita SKILL.md L126 → `biblioteca/_akita_pesquisa/Axx_*.md` **não existe**; CLAUDE.md L126 + akita A07 → `.claude/settings.local.json` **não existe**; `valida_memoria.py` (L115) vive **fora do repo** (pasta de memória) — não rodável do projeto. **Causa provável: git clean/worktree de outra lane varreu untracked** (hazard operacional).
5. **Duplicação quase-literal doc × skill** (N5). clean-code/memória/4-blocos/isolamento são cópia das seções da skill (mesmas frases: "<5 grep hits", "cemitério de superstição") → viola o **DRY-p/-agente** que ambos pregam; risco de drift entre as cópias. Deveriam ser ponteiros de 1 linha.

## MÉDIA
- `veo.py` e `upload_youtube.py` têm só `@circuit_breaker`, **sem `@retry`** — mas L105 os lista com retry (N3). Corrigir código (add @retry+teste) OU a linha do doc.
- `afiliados.json` está em **`afiliados/afiliados.json`** (subpasta), não raiz (Contrato 2 impreciso) (N4,N7).
- `requirements.txt` da raiz **não existe**; reais = `requirements-dev.txt` + `videos/requirements.txt` (a CI usa esses). [ADIÇÃO] L127 genérico (N4,N7).
- "skill akita / **akita.md**" (L9): o arquivo é `SKILL.md`; e há `biblioteca/akita.md` homônimo (notas locais) que induz ao errado (N4,N7).
- **Numeração** da skill: pilares 1-8 + seções soltas `## 9/10/11` — rebaixar p/ `###` dentro de "Os pilares" (N6).
- **Inchaço**: 134 linhas, ~8 seções de doutrina genérica; enxugar p/ ~80 com ponteiros; "Git" aparece 2×; ordem mistura núcleo/genérico/específico (N5).

## BAIXA
- `facebook_insights.py` duplica leitura de segredo (read-only, fora da letra do contrato) (N3).
- `bin/setup` (L91) é exemplo genérico do Akita, não arquivo real (N7).
- raiz `scratch/CLAUDE.md` em inglês × projeto pt-BR (não é contradição real) (N5).

## SAUDÁVEL (confirmado verde — não mexer)
- Contratos de módulo de **vídeo**: auth fonte única (`facebook_base`/`ig_base`), som procedural, `gerar_video.py`=454 linhas (<500), guarda `load_roteiro` — N3 CONFERE.
- `audita_fantasmas.py` → exit 0; CI roda `testar.py`; `python testar.py` = **451 testes VERDE** (17 raiz + 434 vídeo).
- `gerar_livro.py` canônico; `canal-state.json["api_health"]`; `MODO-SOBERANO.md`, `AKITA-PLANO-ALVO/DIAGNOSTICO/REVISAO-VIDEOS.md` existem.
- Geradores legados corretamente em `_legado/`; `loop-agente` (sem "loop-engineering" morto); `drdolabela` ausente dos docs.
- akita skill: as **3 ressalvas de honestidade** intactas; tags `[Axx]` íntegras internamente (12 usadas = 12 definidas).

---

## Correções recomendadas (por classe)
**Doc-only, seguras (posso aplicar já — CLAUDE.md é tracked, persiste):**
- D1 trocar `pytest tests/test_carrossel.py` → `python testar.py` (gate real) e reescrever a frase de enforcement para a verdade.
- D2 corrigir caminhos: `afiliados/afiliados.json`; `requirements-dev.txt`/`videos/requirements.txt`; `SKILL.md` (não `akita.md`).
- D3 remover/realinhar dead refs: `.claude/settings.local.json` (recriar ou parar de citar), `_akita_pesquisa/Axx` na skill, `valida_memoria.py` (dizer que vive na pasta de memória).
- D4 numeração da skill (9/10/11 → ### sob "Os pilares").
- D5 adicionar a ressalva A05 ao "Modo PADRÃO" (resolver a contradição com §11).

**Estruturais / outra lane / judgment (PROPOR, não aplicar sozinho):**
- E1 **Carrossel** (lane do Bibliotecário): portar a worktree p/ `gerar_carrossel.py` ativo + converter `test_carrossel.py` p/ `unittest.TestCase` (entra no `testar.py`/CI) — OU reescrever a seção como "alvo", não "fato", e remover os 3 órfãos.
- E2 enxugar 134→~80 linhas (doutrina vira ponteiro p/ a skill) — resolve a duplicação (achado 5).
- E3 `@retry` em veo/upload_youtube (lane de vídeo) com teste de regressão.

**Operacional:** investigar por que untracked some (git clean/worktree) — risrco de perder trabalho não-commitado entre lanes.
