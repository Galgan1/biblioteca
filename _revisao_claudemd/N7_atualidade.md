# N7 — Auditoria de ATUALIDADE (referências mortas)

Auditor sênior de atualidade · pt-BR · read-only. Verificação: 2026-06-20.
Alvos: `scratch/CLAUDE.md` (raiz), `biblioteca/CLAUDE.md`, `~/.claude/skills/akita/SKILL.md`.
Base de verdade do disco: `C:\Users\User\.gemini\antigravity\scratch\biblioteca`.

Convenção: cada item = `doc:linha | referência | por que está morta | correção`.
Severidade: **MORTA** (não existe / contradiz o disco) · **MÉDIA** (vivo, mas nome impreciso/inconsistente).

---

## MORTAS (alta prioridade)

### 1. `_carousel_*` — decomposição modular DESFEITA (contrato inverso ao disco)
- **`biblioteca/CLAUDE.md:35-39`** | "`gerar_carrossel.py` é o thin orchestrator (target: ≤ 350 linhas); CSS → `_carousel_css.py`; slides → `_carousel_slides.py`; stories → `_carousel_stories.py`."
- **Por que está morta:** o disco contradiz frontalmente o contrato.
  - `gerar_carrossel.py` tem **895 linhas** (não ≤ 350).
  - `gerar_carrossel.py` **NÃO importa** nenhum `_carousel_*` (grep `_carousel` no arquivo = 0 hits; os únicos imports são `gerar_livro`, `instagram_post`, `tokens`).
  - `montar_slides` (linha 456) e `build_stories` (linha 871) e `_lessons_slide` estão **definidos dentro do próprio `gerar_carrossel.py`** — exatamente o que o contrato diz que foi extraído.
  - Os arquivos `_carousel_css.py` (344L), `_carousel_slides.py` (259L), `_carousel_stories.py` (70L) existem mas estão **órfãos** — ninguém de produção os importa (só `audita_fantasmas.py` os cita como string, e `_carousel_stories.py` se auto-referencia). `_lessons_slide` também existe em `_carousel_slides.py`, duplicado.
- **Correção:** ou (a) atualizar o contrato para refletir o estado real (orquestrador monolítico de 895L, funções inline) e remover/arquivar os `_carousel_*` órfãos; ou (b) reverter `gerar_carrossel.py` à decomposição prometida. **Não deixar o contrato mentir.** (Sub-issue: viola o próprio pilar 9 do CLAUDE.md — "Arquivos < 500 linhas".)

### 2. `pytest tests/test_carrossel.py` — gate canônico é `unittest`, não `pytest`
- **`biblioteca/CLAUDE.md:17`** | "Estes contratos são verificados pela bateria de testes (`pytest tests/test_carrossel.py`)."
- **Por que está (semi-)morta:** o ponto único de teste do projeto (`testar.py`) roda **`python -m unittest discover`**, não `pytest` (ver `testar.py:34`). O próprio CLAUDE.md (linhas 97, 109, 132) define o comando único como `python testar.py`. A referência a `pytest` é um framework diferente do gate oficial — inconsistência interna. (Nota: `pytest 9.1.1` está instalado e o arquivo é pytest-style, então roda; por isso não é 100% quebrada, mas o comando-verdade diverge.)
- **Correção:** trocar por `python testar.py` (gate canônico) ou `python -m unittest discover -s tests -t .`. Se quiser nomear o arquivo, deixar claro que o gate é unittest.

### 3. `.claude/settings.local.json` (bloco `deny`) — arquivo NÃO existe
- **`biblioteca/CLAUDE.md:126`** | "Negar por padrão: `rm -rf`, `sudo`, `git push --force` (ver `.claude/settings.local.json` → `deny`)."
- **`akita/SKILL.md:64`** (A07) | mesma doutrina de `allow`/`deny`, apontando para esse mecanismo.
- **Por que está morta:** não existe `settings.local.json` em lugar nenhum da árvore — nem em `biblioteca/.claude/` (só há `scheduled_tasks.lock`, `skills/`, `worktrees/`), nem na raiz `scratch/.claude/` (só `launch.json`, que não contém `deny`). A tarefa #7 do backlog ("Segurança — settings.local.json") está marcada como completa, mas o artefato não está no disco.
- **Correção:** criar de fato o `.claude/settings.local.json` com o bloco `deny`, OU remover a citação ao arquivo inexistente. Hoje a regra aponta para um guard-rail fantasma.

### 4. `valida_memoria.py` — script NÃO existe
- **`biblioteca/CLAUDE.md:115`** | "Lint: `valida_memoria.py` (verde = exit 0)."
- **Por que está morta:** não há `valida_memoria.py` em parte alguma do projeto.
- **Correção:** criar o linter de memória, ou remover a referência (e não prometer "verde = exit 0" de um comando que não roda).

### 5. `afiliados.json` — caminho implícito errado (está em subpasta `afiliados/`)
- **`biblioteca/CLAUDE.md:76`** | "Amazon/afiliados = `afiliados.json`." (também §79 e §5 da Constituição)
- **Por que está (semi-)morta:** não existe `afiliados.json` na raiz do projeto; o arquivo real é **`afiliados/afiliados.json`** (subpasta). Quem ler o contrato e procurar na raiz não acha. (Há também `amazon_vendas.json` na raiz, que pode confundir.)
- **Correção:** corrigir o caminho para `afiliados/afiliados.json`.

### 6. `bin/setup` — não existe (e nem `bin/`)
- **`biblioteca/CLAUDE.md:91`** | "Setup idempotente (`bin/setup` roda em máquina limpa)."
- **`akita/SKILL.md:74`** (A09) | "`bin/setup` roda em máquina limpa."
- **Por que está morta:** não há diretório `bin/` no projeto, nem `bin/setup`. (Genérico no SKILL.md — aceitável como exemplo; no CLAUDE.md do projeto soa como contrato concreto e induz a erro.)
- **Correção:** no CLAUDE.md do projeto, ou criar o `bin/setup`, ou marcar como exemplo genérico (não-existente aqui).

### 7. `requirements.txt` — não existe na raiz
- **`biblioteca/CLAUDE.md:127`** | "ambiente reproduzível (venv/`requirements.txt`) antes de qualquer gate de teste."
- **Por que está morta:** não há `requirements.txt` na raiz de `biblioteca/`. (A memória do agente — `papel-programador.md` — cita `requirements.txt` como ferramenta; pode estar noutro lugar/subprojeto, mas não na raiz onde o contrato implica.)
- **Correção:** confirmar onde o requirements vive (ex.: `videos/`? `book-to-skill/`?) e citar o caminho real, ou criar na raiz.

---

## MÉDIA (vivo, mas nome/caminho impreciso)

### 8. `akita` / `akita.md` — `akita.md` ≠ a skill
- **`biblioteca/CLAUDE.md:9`** | "Siga a skill `akita` / `akita.md`."
- **Por quê (MÉDIA):** a skill é `~/.claude/skills/akita/SKILL.md` (existe, vivo). Mas há um `biblioteca/akita.md` no disco que é **outro documento** ("O Método Akita: Anti-Vibe Coding... no projeto do orquestrador `vp100`") — notas locais, não a skill. Citar "`akita.md`" como sinônimo da skill é ambíguo: aponta para o arquivo errado.
- **Correção:** referir apenas a skill `akita` (ou o caminho `~/.claude/skills/akita/SKILL.md`); não equiparar a `akita.md`.

### 9. `book-to-skill/` e `videos/tests/` como "modelos pytest" — videos/tests é unittest
- **`biblioteca/CLAUDE.md:98`** | "Modelos a replicar: `book-to-skill/` (pytest + CI) e `videos/tests/` (unittest, verde)."
- **Por quê (MÉDIA):** consistente (já diz unittest p/ videos). Sem problema grave; só atenção: o gate raiz é unittest (ver item 2), então "pytest" como padrão a replicar conflita levemente com o gate oficial. Manter coerência com `testar.py`.
- **Correção:** opcional — alinhar a narrativa de framework (unittest é o gate).

### 10. `_akita_pesquisa/Axx_*.md` — pasta de notas não encontrada
- **`akita/SKILL.md:126`** | "Notas detalhadas... ficam em `biblioteca/_akita_pesquisa/Axx_*.md`."
- **Por quê (MÉDIA→MORTA):** não existe `biblioteca/_akita_pesquisa/` nem arquivos `A01_*.md`…`A12_*.md` no disco. A trilha de proveniência citada não está versionada aqui.
- **Correção:** criar a pasta de notas, ou remover a promessa de "notas auditáveis uma por fonte".

---

## VIVOS confirmados (não são problema — registro de cobertura)
`gerar_livro.py`, `publicar_livro.py`, `gerar_dados_kit.py`, `gerar_carrossel.py`, `testar.py`, `audita_fantasmas.py` (roda OK, exit 0), `.github/workflows/ci.yml`, `script.js`, `assets/style.css`, `books.json`, `MODO-SOBERANO.md`, `AKITA-PLANO-ALVO.md`, `AKITA-DIAGNOSTICO.md`, `AKITA-REVISAO-VIDEOS.md`, `videos/canal-state.json`, `videos/facebook_base.py`, `videos/ig_base.py`, `videos/_video_audio.py`, `videos/_video_tts.py`, `videos/dsp.py`, `videos/marca_sonora.py`, `videos/efeitos_transicao.py`, `videos/contracts.py`, `assets/kit/_tpl/<slug>/insights-story.html` (existe p/ vários slugs), funções `build_stories`/`montar_slides`/`_lessons_slide` (existem e os 17 testes de carrossel passam). Geradores legados (`gerar_maquiavel*`, `gerar_psicodelia*`, `gerar_arte*`, `gerar_smith`, `gerar_story`) corretamente movidos para `_legado/` — nenhum dos 3 docs ainda os cita (bom). `drdolabela`/`dolabela`: não aparece em nenhum dos 3 docs nem no disco (não é referência morta — está ausente em ambos). `loop-engineering`: NÃO citado nos 3 docs (usam `/loop-agente`, correto); a skill em disco é `loop-agente/SKILL.md` (existe).

---

## RESUMO (≤ 8 linhas)
7 referências MORTAS + 3 MÉDIA. As mais graves: (1) o contrato `_carousel_*` está **invertido** — `gerar_carrossel.py` tem 895 linhas (não ≤350), define as funções inline e NÃO importa os `_carousel_*`, que estão órfãos; (2) `pytest tests/test_carrossel.py` diverge do gate canônico real `python testar.py` (unittest); (3) `.claude/settings.local.json` (bloco `deny`) NÃO existe — guard-rail fantasma citado 2×; (4) `valida_memoria.py` não existe; (5) `afiliados.json` está em `afiliados/afiliados.json`, não na raiz; (6) `bin/setup` e (7) `requirements.txt` ausentes. MÉDIA: `akita.md` ≠ skill (arquivo local homônimo), framework pytest×unittest inconsistente, pasta `_akita_pesquisa/Axx` ausente. Legados e `loop-agente` estão corretos. Nada foi editado além deste N7.
