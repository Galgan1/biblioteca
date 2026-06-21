# N1 — Auditoria: "Contratos de Formato — Gerador de Conteúdo"

Alvo: `CLAUDE.md` (biblioteca), seção linhas 15–39.
Método: Akita — "verde = exit code". Verificação read-only contra o código real em `biblioteca/`.
Data: 2026-06-20. Python 3.13.7.

## Achado-mãe (contexto de TODOS os drifts abaixo)

Existem **DUAS versões** do gerador:

- **ATIVO (raiz):** `biblioteca/gerar_carrossel.py` — monolito de 896 linhas com cópias
  INLINE de `_cover/_concept/_cta/montar_slides/_story_*` e do CSS. É o que `gerar_dados_kit.py`
  e o build de fato importam (`import gerar_carrossel as gc`). **NÃO** tem `_lessons_slide`,
  `_story_insights`, nem slide/frame de lições.
- **WORKTREE (não comitado):** `.claude/worktrees/agent-a996b1ba779ec8152/gerar_carrossel.py`
  — JÁ implementa o contrato: `_lessons_slide` ligado em `montar_slides` (l.502),
  `_story_insights` (l.915) e `build_stories` montando 4 frames (l.958–961).

Os módulos `_carousel_slides.py` (tem `_lessons_slide`, l.209) e `_carousel_css.py` (tem `.lessons`,
l.185–192) existem na raiz, mas **o gerador ativo NÃO os importa** (único import a `_carousel_*` é
`_carousel_stories.py` → `_carousel_slides`, e nada importa `_carousel_stories`). São órfãos do
caminho de produção. **A seção do CLAUDE.md foi escrita contra a versão da worktree, não contra o
código vivo.**

| # | Afirmação (CLAUDE.md) | file:line CLAUDE.md | Realidade / evidência | Veredito | Correção sugerida |
|---|---|---|---|---|---|
| 1a | "verificados pela bateria `pytest tests/test_carrossel.py`" | l.17 | O arquivo existe. Rodado: `python -m pytest tests/test_carrossel.py -q` → **6 FAILED, 2 passed, exit code = 1 (VERMELHO)**. O comando pytest roda, mas reprova. | **DRIFT (alta)** | Corrigir o código (item-mãe) OU corrigir a constituição. Enquanto não, a frase "verificados" é falsa: a bateria está vermelha. |
| 1b | "Violar qualquer contrato aqui resulta em teste vermelho" | l.18 | O gate canônico do projeto é `python testar.py` (= o que a CI roda), que usa **`unittest discover`**, NÃO pytest. `test_carrossel.py` são funções estilo-pytest (sem `TestCase`) → `unittest discover` coleta **0** delas. `python testar.py` → "raiz 17 testes OK / TOTAL 451 VERDE / exit 0". Ou seja: **os contratos falham no pytest mas o gate oficial fica VERDE porque não os enxerga.** | **DRIFT (alta)** | Drift de comando + drift de cobertura. Ou (a) portar `test_carrossel.py` para `unittest.TestCase` (assim entra no `testar.py`), ou (b) acrescentar pytest ao `testar.py`. Citar o comando canônico (`python testar.py`), não `pytest …`. |
| 2a | Story = **SEMPRE 4 frames** (teaser→quote→insights→CTA) | l.21 | ATIVO `gerar_carrossel.build_stories` (l.871–881) monta `frames = [_story_teaser, _story_quote, _story_cta]` = **3 frames**. Sem insights. (Worktree tem 4, condicional a `lessons`.) | **DRIFT (alta)** | No ativo são 3, e o 4º é condicional (worktree). Trocar "SEMPRE 4" por "4 quando há lessons; 3 caso contrário" — e ligar o código ao contrato. |
| 2b | Frame 3 = `_story_insights`; coleta 1ª lição dos 3 primeiros caps | l.22–23 | `_story_insights` **não existe** no ativo: `python -c "import gerar_carrossel as g; g._story_insights"` → AttributeError; teste `test_story_insights_function_existe` FALHA. A função e a lógica de agregação só estão na worktree (`build_stories` l.945–953) e em `_carousel_stories.py` (l.41, módulo órfão). | **DRIFT (alta)** | Wirear `_story_insights` no `build_stories` ativo (portar da worktree) OU remover a afirmação. |
| 3a | Carrossel de capítulo (`montar_slides` com ch=) = **SEMPRE ≥6 slides** quando há lessons | l.26 | ATIVO `montar_slides` (l.456–467) = capa + N conceitos + CTA, sem lições. Para `habitos-atomicos` cap 1 (3 cards) → **5 slides**. Teste `test_montar_slides_chapter_tem_6_slides` FALHA: "Esperado >=6, obtido 5". | **DRIFT (alta)** | Portar o ramo `has_lessons` da worktree (`total = n+2+1`, append `_lessons_slide`) para o ativo. |
| 3b | Usa a classe `.lessons` (CSS) e o componente `_lessons_slide()` | l.28 | `_lessons_slide` **não existe** no ativo (só em `_carousel_slides.py` l.209 e na worktree l.428). A CSS `.lessons` do carrossel está em `_carousel_css.py` (l.185), módulo que o gerador ativo **não importa**; a `CSS` inline do ativo (l.64–260) **não** define `.lessons` do carrossel. (Há `.lessons` em `assets/style.css` e `pdf-service/server.js`, mas é do SITE/PDF, não deste gerador.) | **DRIFT (alta)** | Idem item-mãe: o componente e a CSS precisam estar no caminho de produção, não em módulos órfãos. |
| 3c | Sem ch (overview) ou sem lessons: NÃO insere slide de lições | l.27 | Verdadeiro por vacuidade no ativo (nunca insere). No alvo-correto (worktree) também é honrado via `has_lessons`. Teste `test_montar_slides_overview_sem_lessons` é um dos **2 que passam**. | **CONFERE** | — |
| 4a | Kit: `insights-story.html` gerado p/ todo livro com lessons, em `gerar_dados_kit.py` | l.30–31 | `gerar_dados_kit.emit()` (l.154–185) emite `ideia/quote/quote-story/capa-story/mapa/thumb.html` — **nenhuma referência a `insights-story` ou a `lessons`** no arquivo (grep: 0 hits em `gerar_dados_kit.py`). | **DRIFT (alta)** | A lógica não existe. Implementar em `emit()` (gate por `ch.get('lessons')`) OU remover a afirmação. |
| 4b | Template fica em `assets/kit/_tpl/<slug>/insights-story.html` | l.32 | Glob `**/insights-story.html` → **nenhum arquivo no repo**. `ls assets/kit/_tpl/habitos-atomicos/` mostra capa-story, ideia, mapa, quote-story, quote, thumb — sem insights-story. Testes `test_insights_story_html_existe` e `..._tem_3_licoes` FALHAM (FileNotFoundError). | **DRIFT (alta)** | Consequência de 4a. Gerar o template ao implementar `emit()`. |
| 4c | Endpoint VPS `/pdf/asset/<slug>/insights-story.jpg` → 200 | l.33 | **NÃO-VERIFICÁVEL** localmente (read-only; sem rede/VPS). Pré-condição (4a/4b) está quebrada → improvável retornar 200 hoje. | **NÃO-VERIFICÁVEL** | Verificar após 4a/4b; deixar como meta, não como fato. |
| 5 | Estrutura de módulos: `gerar_carrossel.py` thin orchestrator ≤350 linhas; CSS→`_carousel_css.py`; slides→`_carousel_slides.py`; stories→`_carousel_stories.py` | l.35–39 | `gerar_carrossel.py` ativo tem **896 linhas** (>350) e é monolito: CSS, slides E stories INLINE. Os módulos `_carousel_css.py` / `_carousel_slides.py` / `_carousel_stories.py` existem mas estão **órfãos** (não importados pelo gerador ativo). | **DRIFT (média)** | A refatoração-alvo não foi efetivada no ativo (só na intenção / nos órfãos). Ou concluir a extração e fazer o ativo importar os 3 módulos, ou reescrever a afirmação como meta. |

## Resumo dos DRIFTs

- **[ALTA] Drift estrutural-mãe:** o `gerar_carrossel.py` ATIVO (raiz, 896 l., monolito) é uma versão
  ANTIGA. A versão que cumpre o contrato (lessons + insights + 4º frame) vive só na worktree não
  comitada (`.claude/worktrees/agent-a996b1ba779ec8152/`) e em `_carousel_*.py` órfãos. Itens 2,3,4 caem todos daqui.
- **[ALTA] Drift de comando:** CLAUDE.md manda `pytest tests/test_carrossel.py`, mas o gate canônico
  (`python testar.py`, o da CI) usa `unittest discover` e **não coleta** o `test_carrossel.py` (estilo pytest, sem `TestCase`).
- **[ALTA] Drift de verificação ("verde = exit code" furado):** `pytest tests/test_carrossel.py` = exit 1 (6/8 falham),
  mas `python testar.py` = exit 0 VERDE. A frase "violar qualquer contrato resulta em teste vermelho" é FALSA hoje:
  os contratos estão violados E o gate está verde, porque o gate não roda esse arquivo.
- **[ALTA] Story 4 frames / `_story_insights` (l.21–23):** ativo faz 3 frames; função inexistente no ativo.
- **[ALTA] Carrossel ≥6 / `.lessons` / `_lessons_slide` (l.26,28):** ativo gera 5 slides p/ cap com lessons; componente/CSS ausentes do caminho de produção.
- **[ALTA] `insights-story.html` (l.30–33):** lógica e arquivo inexistentes; testes correspondentes vermelhos.
- **[MÉDIA] Estrutura de módulos (l.35–39):** 896 ≠ ≤350; extração CSS/slides/stories não efetivada no ativo (módulos órfãos).
- **[BAIXA / único CONFERE]:** "overview/sem-lessons NÃO insere lições" (l.27) — verdadeiro; e "endpoint VPS" (l.33) = NÃO-VERIFICÁVEL (read-only).
