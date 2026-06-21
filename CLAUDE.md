# CLAUDE.md — Projeto Biblioteca (bazuka)

> Complementa o CLAUDE.md raiz em `scratch/`. Regras específicas deste projeto.

## Modo de trabalho PADRÃO (obrigatório neste projeto)

Toda tarefa não-trivial neste projeto roda sob dois padrões. Não é opcional.

1. **Método = Akita (anti-vibe coding).** Siga a skill `akita` / `akita.md`: planejar antes de codar (tarefas atômicas), **TDD real** (verde = exit code de teste, nunca "a IA achou que está certo"), humano decide o *quê* / IA o *como*, refatoração contínua, CI obrigatória, isolamento de execução. Constituição = este arquivo.

2. **Execução = `/loop-agente`.** Não responda/entregue direto: passe pelo ciclo **Planner → Executor → Verifier**, com **rúbrica** definida antes e **verificação cross-model** (juiz ≠ autor: Opus ↔ Sonnet). Só entrega o que passar na rúbrica (parada em 5 tentativas). Para tarefas grandes, o Planner decompõe em subagentes (mesmo sistema).

Tarefas triviais (ex.: 1 linha, leitura simples) dispensam o cerimonial — use bom senso. Tudo que gera/edita código de produção: Akita + loop, sem exceção.

## Contratos de Formato — Gerador de Conteúdo

Estes contratos são verificados pela bateria de testes (`pytest tests/test_carrossel.py`).
Violar qualquer contrato aqui resulta em teste vermelho.

### Story (9:16 — `build_stories`)
- **Sempre 4 frames**, nesta ordem: teaser → quote → insights/lições → CTA
- Frame 3 = insights: coleta a 1ª lição de cada um dos 3 primeiros capítulos do livro
- Para story de capítulo: usa `ch['lessons']`; para story de livro: agrega 1 lição por capítulo

### Carrossel de capítulo (`montar_slides` com `ch=`)
- **Sempre ≥ 6 slides** quando o capítulo tem `lessons`: capa → N cards → lições → CTA
- Sem `ch` (overview) ou sem `lessons`: NÃO insere slide de lições
- O slide de lições usa a classe `.lessons` (CSS) e o componente `_lessons_slide()`

### Kit de publicação (`gerar_dados_kit.py`)
- `insights-story.html` é gerado automaticamente para todo livro que tem `lessons` nos capítulos
- Template fica em `assets/kit/_tpl/<slug>/insights-story.html`
- Endpoint VPS: `/pdf/asset/<slug>/insights-story.jpg` → deve retornar 200

### Estrutura de módulos (`gerar_carrossel.py`)
- `gerar_carrossel.py` é o thin orchestrator (target: ≤ 350 linhas)
- CSS strings → `_carousel_css.py`
- Funções de slide HTML → `_carousel_slides.py`
- Funções de story HTML → `_carousel_stories.py`

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

## Clean Code para agentes — normas de ofício (Akita pilar 9) [ADIÇÃO]

Otimize o código para a forma como o agente lê e edita. Concretiza o contrato 3 (qualidade).

- **Funções 4–20 linhas. Arquivos < 500 linhas (ideal 200–300)** — deve caber numa tool call sem truncar. Arquivo gigante → extraia responsabilidade (não "depois").
- **Nomes únicos e pesquisáveis: meta < 5 hits de grep.** PROIBIDO `data`, `process`, `handler`, `Manager`, `Service` (~50 matches). Grep é mais barato que read.
- **Comentário = POR QUÊ, não O QUE** + proveniência (issue/SHA/workaround/constraint). **Não apague comentário alheio no refactor** — carrega a intenção da iteração anterior ("keep your own comments").
- **Tipos explícitos** (type hints) = gabarito p/ o agente. **DRY é mais crítico ainda** (o agente atualiza uma cópia e esquece as réplicas).
- **Early returns, ≤ 2 níveis de indentação.** Erro com contexto (valor ofendido + forma esperada). Setup idempotente (`bin/setup` roda em máquina limpa).
- Vale só para código novo/editado por você. NÃO refatore código alheio que não está quebrado (mudança cirúrgica — CLAUDE.md raiz §3).

## Teste = comando único que o agente roda sozinho (Akita pilar 2) [ADIÇÃO]

Concretiza o contrato 3 ("verde = exit code"):
- O teste que define "pronto" é **um comando único** (na raiz: `python testar.py`), **output parseável**, **sem setup humano** (sem seed manual, credencial secreta ou config ausente).
- **Um bug vira um teste de regressão** antes do fix. Modelos a replicar: `book-to-skill/` (pytest + CI) e `videos/tests/` (unittest, verde).

## Contratos de módulo — lane de vídeo (`videos/`) [Akita pilar 6]

Mapa dos módulos do Criador de Vídeos (revisão Akita 2026-06-20; detalhe em `AKITA-REVISAO-VIDEOS.md`). Edite a responsabilidade no módulo dono — não espalhe nem duplique.

- **Auth das redes = fonte única.** Facebook → `facebook_base.py` (`token/page_id/post`, `GRAPH`, `HASHTAGS_BASE`); Instagram → `ig_base.py` (`read_token/refresh_token/read_user_id`). Os postadores (`facebook_*`, `instagram_post`, `analytics_ig`) IMPORTAM daí — PROIBIDO redefinir `_token/_page_id/_post` no módulo (só wrapper fino que passa o `*_FILE` do módulo, p/ o mock do teste valer).
- **Resiliência obrigatória em todo cliente de API paga.** Decore `@retry(...)` (fora) + `@circuit_breaker(api=...)` (dentro) — NESSA ordem — e chame `record_cost(api=...)` no sucesso. Já vale p/ `imagen/veo/tts_gcloud/upload_youtube/falgen`. Estado do breaker em `canal-state.json["api_health"]`.
- **Roteiro inválido ABORTA antes de gastar API.** `contracts.load_roteiro` é guarda dura nos callers (`gerar_video`, `upload_youtube`): fora do `try/except` (só `ImportError` é silenciado, p/ ambiente sem pydantic).
- **Som procedural (numpy puro, sem lib externa):** `dsp.py` (cadeia premium low-cut→saturação→ar→reverb), `marca_sonora.py` (10 sons da marca, Ré menor), `efeitos_transicao.py` (arco Fibonacci de comoção + `place_marca`). `_video_audio.py` = trilha (`sintetiza_ambiente`); `_video_tts.py` = voz (`_to_ssml`, `tts` com fallback Eleven→Google→edge).
- **`gerar_video.py` é orquestrador fino** (< 500 linhas): delega som a `_video_audio`/`_video_tts` — não reabsorva essas funções no arquivo.
- **Gate da lane:** `python testar.py` (raiz + `videos/tests`); verde = exit code. Todo módulo novo não-trivial nasce com teste hermético.

## Memória do agente: markdown + grep, nunca RAG (Akita pilar 10) [ADIÇÃO]

- **Markdown no disco = fonte da verdade.** `MEMORY.md` é índice de ponteiros → topic files curtos sob demanda. Embeddings/RAG ficam OFF: long-context + grep (ripgrep) > vector DB.
- **Não escreva memória sem validar** (evidência/confiança/trilha). Memória sem validação = "cemitério de superstição".
- Frontmatter do fato: além de `type`, use `kind` ∈ {decision,gotcha,rule,fact,concept,procedure}; `confidence` nasce `low` sem `evidence`. Lint: `valida_memoria.py` (verde = exit 0).
- Toda lane que precisar de fato vivo (ex.: metadados) **invoca a skill** e lê ao vivo — não responde de memória.

## Prompt em 4 blocos (Akita pilar 1) [ADIÇÃO]

Toda tarefa não-trivial nasce com: **Objetivo · Método · Restrições · Validação**, e injeta o conhecimento de domínio que está na sua cabeça (senão o modelo assume o "default mais razoável" e erra). Tarefa atômica, uma por vez.

## Isolamento e permissões mínimas (Akita pilar 8) [ADIÇÃO]

Estende o contrato 1 (git) ao host inteiro:
- Execução por **ponto único idempotente revisável** — nunca comando solto/destrutivo no host.
- **Negar por padrão:** `rm -rf`, `sudo`, `git push --force` (ver `.claude/settings.local.json` → `deny`). Anti-padrão proibido: **YOLO mode** (`--dangerously-skip-permissions`).
- Segredos **fora do working tree**; ambiente reproduzível (venv/`requirements.txt`) antes de qualquer gate de teste.
