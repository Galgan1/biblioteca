# CLAUDE.md — Projeto Biblioteca (bazuka)

> Complementa o CLAUDE.md raiz em `scratch/`. Aqui ficam só os **contratos do PROJETO**; a doutrina genérica de ofício mora na skill `akita` (não duplicar — DRY).

## Modo de trabalho PADRÃO (obrigatório neste projeto)

Tudo que gera/edita código de produção:
1. **Método = Akita (anti-vibe coding).** Siga a skill `akita` (`SKILL.md`): planejar antes de codar (tarefas atômicas), **TDD real** (verde = exit code, nunca "a IA achou que está certo"), humano decide o *quê* / IA o *como*, refatoração contínua, CI, isolamento.
2. **Execução = `/loop-agente`** (Planner → Executor → Verifier; rúbrica antes; parada em 5). Tarefas grandes: o Planner decompõe em subagentes.
   - ⚠️ **Cross-model (juiz Opus↔Sonnet) NÃO é default** — é **acréscimo nosso**, não do Akita (ver skill `akita` §11: solo frontier vence ~90%; multi-modelo é p/ trabalho paralelo desacoplado). Use cross-model quando o custo do erro justificar; senão, solo.

Triviais (1 linha, leitura) dispensam o cerimonial — use bom senso.

## Contratos de Formato — Gerador de Conteúdo (IMPLEMENTADO — gate verde 21/jun)

Gate (o que a CI roda): **`python testar.py`** — `unittest discover` agrega `tests/` (inclui `tests/test_carrossel.py`, 8 testes de contrato já em `unittest.TestCase`, + `tests/test_verificar_conteudo.py`) e `videos/tests/`. Verde = exit code; **violar um contrato abaixo = teste VERMELHO no gate** (não só num `pytest` focado). `pytest tests/test_carrossel.py` segue válido como atalho de dev.

- **Story (9:16 — `build_stories`):** 4 frames teaser → quote → insights/lições → CTA. Frame 3 = 1ª lição de cada um dos 3 primeiros capítulos (`_story_insights` de `_carousel_stories.py`).
- **Carrossel de capítulo (`montar_slides` com `ch=`):** ≥ 6 slides quando há `lessons` (capa → N cards → lições → CTA); sem `ch`/sem `lessons` NÃO insere lições (`_lessons_slide` de `_carousel_slides.py`).
- **Kit (`gerar_dados_kit.py`):** `insights-story.html` p/ todo livro com `lessons`; template em `assets/kit/_tpl/<slug>/`.
- **Módulos auxiliares (wired):** slides → `_carousel_slides.py` (`_lessons_slide`), stories → `_carousel_stories.py` (`_story_insights`); `gerar_carrossel.py` importa deles. **CSS/JS-de-fit = inline em `gerar_carrossel.py`** (fonte única — o antigo `_carousel_css.py` era cópia órfã divergente, removido; o `.lessons` foi portado p/ a CSS inline). `gerar_carrossel.py` segue monolito (~920 l.); reduzir ao orquestrador-fino é alvo de consolidação, não fato.

## Verificação Editorial — Fidelidade ao Autor (IMPLEMENTADO — 21/jun)

**Contrato:** nenhuma imagem publicada pode contradizer o que o autor defendeu. A skill é a referência canônica.

- **`verificar_conteudo.py <slug> [--fix]`**: carrega `~/.claude/skills/<slug>/` (SKILL.md + chapters/*.md) como referência; chama Claude UMA VEZ por capítulo; verifica `b`, `tip`, `lessons` contra a skill; com `--fix` corrige cirurgicamente o `_data.py` (backup `.py.bak` + validação de importabilidade).
- **Integrado em `publicar_livro.py` como step 1b** (antes de gerar qualquer coisa): corrige o `_data.py`, recarrega o módulo (`del sys.modules[...]`), depois gera tudo — site + kit + carrossel + stories — com o conteúdo verificado.
- **Resultado esperado:** ao clicar "publicar" no site, o `_data.py` é revisto automaticamente contra a skill antes de qualquer imagem ser gerada.

## Git — REGRA ABSOLUTA: não commitar, não fazer push

O agente **GitGuy** é a ÚNICA lane autorizada a `git commit`/`git push`/criar PR (repo `Galgan1/biblioteca`).
- **Você:** cria/edita/gera arquivos no disco e avisa quando pronto.
- **Você NUNCA:** `git commit` (nem `-m`), `git push`, `git add`+commit, `gh pr create`.
- **Por quê:** working tree compartilhado entre lanes — commit fora de hora enterra trabalho alheio e dificulta rollback. O GitGuy age no `/create-pr` (revisa tudo no disco, agrupa por lane, commita).
- **GitGuy NUNCA roda `git clean -fdx`/`reset --hard` com outra lane tendo untracked WIP** — varre trabalho não-commitado alheio (já apagou `_akita_pesquisa` + `.claude/settings.local.json` num resync pós-squash, jun/26). Antes de limpar: `git clean -nd` (dry-run); o `deny` em `.claude/settings.local.json` reforça.
- **Enforcement por máquina (hook `PreToolUse`):** `hooks/git_guard.py` BLOQUEIA `git commit`/`push`/`gh pr create` — o **GitGuy commita prefixando `GITGUY=1`** (ex.: `GITGUY=1 git commit -m "..."`). Vale a partir da próxima sessão; scripts em `hooks/` (versionados), wiring em `.claude/settings.json` (gitignored → recriar se varrido).

## O que versionar (referência para o GitGuy)

| Versionar ✅ | Nunca versionar ❌ |
|---|---|
| `*_data.py` — fonte autoral dos livros | `videos/canal-state.json` — runtime |
| `*.html`, `assets/`, `books.json` | `datas_coletadas.json` — runtime |
| `gerar_*.py`, `publicar_livro.py` | `historico_metadados.json` — runtime |
| `assets/style.css`, `script.js` | `_remote_books.json`, `_ssh_err.txt` — temp |
| Skills e skills data | `pipeline/state/`, `pdf-service/cache/` |

## Contratos Invioláveis — Constituição (Akita, pilar 6)

Regras cross-cutting que **nenhuma lane quebra**. Norte em `AKITA-PLANO-ALVO.md`; estado em `AKITA-DIAGNOSTICO.md`.

1. **Git:** só o **GitGuy** commita/pusha/cria PR (ver seção Git acima).
2. **Fontes da verdade** (edite a fonte, nunca o derivado): livros = `<slug>_data.py` (HTML é gerado dela); Amazon/afiliados = `afiliados/afiliados.json`; estado do canal = `canal-state.json` (runtime, não versionar).
3. **Qualidade (Akita):** nada se consolida sem **teste verde** (verde = exit code), não "a IA achou"; execução só por **ponto único idempotente** (nada de comando solto); na dúvida, o verificador reprova. Alvo: CI verde antes do merge.
4. **Geração do site:** um gerador canônico (`gerar_livro.py`); estética "cheat-sheet verde" e tokens de marca são **únicos** (não inventar cor/variável). Detalhe: skill `biblioteca`.
5. **Distribuição/afiliado:** link Amazon só de **produto** (`/dp/`, `/gp/`), nunca busca; no Instagram o link vai na **bio** (legenda não é clicável); no Facebook, **post nativo + link no 1º comentário**. Detalhe: skills das lanes.
6. **Idioma:** todo conteúdo em **pt-BR** (pt-PT é bloqueante).
7. **Soberania:** o pipeline roda local/grátis; sem crédito de IA externa há rota de fuga (voz → edge-tts). Detalhe: `MODO-SOBERANO.md`.
8. **Canal YouTube = SÓ Minuto Real (NUNCA o pessoal):** todo conteúdo do canal publica no **Minuto Real** (`@MinutoReal1701`, id `UC2N5xZ-gyCU3hNvH1QqNahA`) e **JAMAIS** no pessoal André Galgani (`UCmSpZF4cVFd1kTYomdC_NUw`). Isto é **guarda de máquina, não confiança no operador**: nenhuma lane chama `build('youtube', …)` direto — o cliente nasce de **`videos/canal_guard.py::get_youtube()`**, que **ABORTA** (`CanalErrado`) se o OAuth resolver para o canal errado, antes de qualquer `insert/update/set`. Ao reautorizar (`reauth_youtube.py`), no consentimento Google **escolher o brand Minuto Real**. Origem: incidente 21/jun (token expirou → re-auth caiu no pessoal → upload foi p/ o canal errado). Lição Akita pilar 7: regra em doc ≠ regra cumprida.

## Contratos de módulo — lane de vídeo (`videos/`) [Akita pilar 6]

Mapa dos módulos do Criador de Vídeos (revisão Akita; detalhe em `AKITA-REVISAO-VIDEOS.md`). Edite a responsabilidade no módulo dono — não espalhe nem duplique.

- **Auth das redes = fonte única.** Facebook → `facebook_base.py` (`token/page_id/post`, `GRAPH`, `HASHTAGS_BASE`); Instagram → `ig_base.py` (`read_token/refresh_token/read_user_id`). Os postadores (`facebook_*`, `instagram_post`, `analytics_ig`) IMPORTAM daí — PROIBIDO redefinir `_token/_page_id/_post` (só wrapper fino que passa o `*_FILE` do módulo, p/ o mock do teste valer).
- **Identidade do canal YouTube = fonte única `canal_guard.py`.** `CANAL_ID` (Minuto Real), `PESSOAL_ID` (proibido), `assert_canal(yt)`→`CanalErrado`, `get_youtube()` (cliente já verificado). TODO script que toca a YouTube API obtém o cliente por `get_youtube()` (ou chama `assert_canal` se tiver `creds()` próprio, ex.: `afiliado_youtube`) — PROIBIDO `build('youtube', …)` direto num caller. Contrato inviolável nº 8.
- **Resiliência em todo cliente de API paga:** `@retry(...)` (fora) + `@circuit_breaker(api=...)` (dentro) — NESSA ordem — + `record_cost(api=...)` no sucesso. Hoje completo em `imagen/tts_gcloud/falgen`; **`veo` e `upload_youtube` têm só `@circuit_breaker` (retry pendente — ver revisão).** Estado do breaker em `canal-state.json["api_health"]`.
- **Roteiro inválido ABORTA antes de gastar API.** `contracts.load_roteiro` é guarda dura nos callers (`gerar_video`, `upload_youtube`): fora do `try/except` (só `ImportError` silenciado, p/ ambiente sem pydantic).
- **Som procedural (numpy puro):** `dsp.py` (low-cut→saturação→ar→reverb), `marca_sonora.py` (10 sons, Ré menor), `efeitos_transicao.py` (arco Fibonacci + `place_marca`). `_video_audio.py` = trilha (`sintetiza_ambiente`); `_video_tts.py` = voz (`_to_ssml`, `tts` fallback Eleven→Google→edge).
- **`gerar_video.py` é orquestrador fino** (< 500 linhas): delega som a `_video_audio`/`_video_tts` — não reabsorva.

## Normas de ofício (Akita) — detalhe na skill `akita`, aqui só os ganchos do projeto

A doutrina completa (clean-code, memória, prompt 4-blocos, isolamento) vive na skill `akita` — **NÃO duplicar aqui**. Ganchos que valem para este repo:

- **Clean code (pilar 9):** funções 4–20 linhas; arquivos < 500; nomes com < 5 grep hits (proibido `data`/`handler`/`Manager`/`Service`); comentário = POR QUÊ + proveniência ("keep your own comments"). Só p/ código novo/editado — não refatore código alheio que não quebrou (cirúrgico, raiz §3).
- **Teste = comando único (pilar 2):** o gate é **`python testar.py`** (raiz `tests/` + `videos/tests/`), output parseável, sem setup humano. **Um bug vira teste de regressão** antes do fix. Modelos: `book-to-skill/` (pytest+CI) e `videos/tests/` (unittest).
- **Memória (pilar 10):** markdown + grep, **nunca RAG**; `MEMORY.md` = índice de ponteiros; não escreva sem validar ("cemitério de superstição"); frontmatter usa `kind`/`confidence` (lint `valida_memoria.py`, na pasta de memória do agente). Fato vivo (ex.: metadados) → invocar a skill, não responder de memória.
- **Prompt 4 blocos (pilar 1):** Objetivo · Método · Restrições · Validação. Tarefa atômica, uma por vez.
- **Isolamento (pilar 8):** ponto único idempotente revisável; negar `rm -rf`/`sudo`/`git push --force`; nunca **YOLO mode** (`--dangerously-skip-permissions`); segredos fora do working tree.
- **Erro fica registrado (pilares 7+9):** nada de `except: pass` silencioso — erro **com contexto** (valor ofendido + forma esperada). Registros vivos: API paga → `canal-state.json` `api_health.last_error` (circuit_breaker); stage → `pipeline_state` (`blocked`+`reason` → `events.jsonl`); loop → `historico_loop.log`; saúde → `doctor.py`. E **bug → teste de regressão** (pilar 2) antes do fix.

## Guardas de máquina: CI real + anti-fantasma (revisão Akita)

A CI (`.github/workflows/ci.yml`) é o gate que IMPÕE os contratos:
- **Ponto único de teste:** `python testar.py` agrega `tests/` (contratos do gerador) + `videos/tests/` (pipeline). É o que a CI roda. Verde = exit code.
- **Anti-fantasma (pilar 7):** `python audita_fantasmas.py` (na CI, ANTES do pip) bloqueia `.py` rastreado que importe módulo de raiz NÃO versionado. Origem: `gerar_carrossel.py` importava `_carousel_*` nunca commitados → repo quebrava em clone limpo. **Regra: "passa local" ≠ "está no git"** — todo entrypoint tem seu import-closure versionado.
