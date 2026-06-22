# PLANO — "Publicar Tudo" (livro completo: overview + capítulos, playlist, cronograma, API-first)

> Plano Akita (planejar antes de codar, pilar 1). Decisões do André (22/jun): **vídeo longo por
> capítulo + 1 overview, todos na playlist do livro**; **cadência ∝ nº de capítulos** (livro da
> semana); **render API-first** (soberano = fallback). Estado-norte vive aqui; execução por
> `/loop-agente` em fatias atômicas. **Nada se consolida sem teste verde** (verde = exit code).

## Bloco 1 · Objetivo
Transformar `publicar_tudo <slug>` de "1 vídeo + redes" em **"o livro inteiro"**: 1 vídeo-overview + **1 vídeo longo por capítulo**, todos numa **playlist do YouTube por livro**, produzidos e publicados por um **cronograma inteligente** (livro da semana, janela proporcional ao nº de capítulos), com **render API-first**. Sintoma que disparou: `ponerologia: render/asset FALHOU -> No such file or directory: '/opt/minutoreal/ponerologia.json'` — o **roteiro não é gerado** antes de renderizar.

## Bloco 2 · Método (arquitetura — estender o que existe, não reinventar, pilar 4)
Fluxo atual (medido): `publicar_tudo <slug>` → `_cfg` lê `ROOT/<slug>.json` (o **roteiro**) → `_garante_video` (usa `<slug>.mp4` local OU `gerar_video.main(<slug>.json)`) → `upload_youtube` (longo) → `produzir_shorts` → IG → FB; idempotência em `_shorts/<slug>_publicar_tudo.json`. Roteiros vivem em `videos/roteiros/<slug>.json`; schema validado por `contracts.load_roteiro`. Playlist já aparece em `upload_youtube.py`/`youtube_pos.py`/`aplicar_pos.py`. Agendamento já existe: `agendar_lancamento.py`, `agendar_lote.py`, `dag.py`, `pipeline_state.py`, `fila.json`. Cliente YouTube SEMPRE por `canal_guard.get_youtube()` (contrato nº 8).

**Fonte canônica do conteúdo** = a **skill** `~/.claude/skills/<slug>/` (`SKILL.md` + `chapters/*.md`) — mesma fonte do verificador editorial. O roteiro é DERIVADO dela (edite a skill, nunca o roteiro à mão).

## Bloco 3 · Restrições (constituição — nenhuma lane quebra)
- **Git:** só o GitGuy commita/pusha. Eu deixo a árvore pronta + deploy VPS.
- **Canal:** todo upload via `canal_guard.get_youtube()` → JAMAIS o canal pessoal (contrato nº 8).
- **Roteiro ausente ABORTA com contexto** antes de gastar API (já é guarda dura em `gerar_video`/`upload_youtube`). Passo 0 gera o roteiro; se a geração falhar, aborta — nunca publica vazio.
- **Idempotência:** re-rodar PULA o que já saiu (por PEÇA: overview e cada capítulo têm estado próprio).
- **pt-BR** em tudo; **API paga** com `@retry`+`@circuit_breaker`+`record_cost`+ teto `WEEKLY_BUDGET_USD`.
- **"Não testar tudo na fase de testes":** o gate (`python testar.py`) usa **mocks/--dry/contratos** — NUNCA dispara publicação paga real. E2E real = manual, gateado, fora do gate.

## Bloco 4 · Validação (como cada fase fica "pronta" = teste executável)
Cada fase abaixo tem um gate verde em `python testar.py`. "Pronto" = o teste que falhava passa.

---

## Fases (atômicas, sequenciais onde há dependência)

### FASE 0 — Destravar publish real (o bug do `ponerologia`) — **desbloqueia tudo**
- **0.1** `gerar_roteiro.py <slug>`: lê a skill (`SKILL.md`+`chapters/*.md`) → escreve `roteiros/<slug>.json` (overview) válido por `contracts.load_roteiro`. Idempotente; se a skill não existir, ABORTA com contexto.
- **0.2** `publicar_tudo`: **passo 0** — se o roteiro do slug não existe, chama `gerar_roteiro` antes de `_garante_video`. Erro de geração = abort limpo (não meio-publica).
  - *Verify:* teste — slug sem roteiro → `publicar_tudo(..., dry=True)` gera o roteiro e completa; roteiro inválido → aborta. (mock de render/upload).

### FASE 1 — "Tudo" = overview + 1 vídeo longo por capítulo
- **1.1** `gerar_roteiro` produz **N+1** roteiros: `<slug>.json` (overview) + `<slug>--capNN.json` por capítulo (de `chapters/NN.md`). Contrato de nome `--capNN` (zero-padded, ordenável).
- **1.2** `publicar_tudo` itera as peças: renderiza+sobe overview e **cada capítulo**; estado por peça em `_shorts/<slug>_publicar_tudo.json` (`{overview:..., cap01:..., ...}`).
  - *Verify:* skill-fake com 3 capítulos → 4 roteiros; `publicar_tudo` (mock) chama render/upload 4×, em ordem; re-run pula os `ok`.

### FASE 2 — Playlist por livro no YouTube
- **2.1** `youtube_playlist.py`: `garante_playlist(slug, titulo)` → cria (ou acha) a playlist do livro via `canal_guard.get_youtube()`; guarda `playlist_id` no estado (idempotente). `adiciona(playlist_id, video_id, posicao)`.
- **2.2** `publicar_tudo`: após subir cada vídeo, adiciona à playlist do livro na ordem (overview 1º, capítulos em sequência).
  - *Verify:* mock do client YouTube — playlist criada 1× por livro; vídeos adicionados na ordem; re-run não duplica.

### FASE 3 — Cronograma inteligente (livro da semana, janela ∝ capítulos)
- **3.1** `cronograma.py` (função PURA, testável sem tempo/rede, estilo `planejar` do bot): dado o acervo + estado, decide **qual livro** (da semana) e **datas por peça** — janela proporcional ao nº de capítulos (livro de 5 caps = janela curta; de 15 = janela longa); produção ANTES, publicação dripada.
- **3.2** Produção desacoplada da publicação: o cronograma **produz** (render) com antecedência e marca cada peça com `publish_date`; um tick idempotente publica o que vence no dia. Estado em `canal-state.json.upcoming_schedule` (reusa `pipeline_state`/`dag`).
- **3.3** Runner: tick diário idempotente (cron OU o PM2 `publicar-1click` + agenda). Alerta Telegram no início/fim (reusa `notificar`).
  - *Verify:* `cronograma.proximo(acervo, hoje)` puro → escolhe o livro certo + janela ∝ caps; tick num dia sem nada devido = no-op; com peça devida = publica 1×.

### FASE 4 — Render API-first (soberano = fallback)
- **4.1** `gerar_video`: inverter a decisão de render — **API (Imagen/Veo) é o PADRÃO**; soberano (Ken Burns/3DGS local via `heartbeat`) só quando a API falha/satura (circuit breaker aberto) ou estoura o teto.
- **4.2** Ligar o teto de custo de verdade: `WEEKLY_BUDGET_USD` no entrypoint do `publicar_tudo` (herda no Popen do bot) — fecha o gap do chip de orçamento. `record_cost` por peça.
  - *Verify:* `decide_render()` puro → API por padrão; com breaker aberto → fallback soberano; teto estourado → aborta peça com contexto. (sem chamar API real).

---

## Estratégia de testes (honra "não testar tudo")
Gate = `python testar.py` (unittest discover, `tests/` + `videos/tests/`): **contratos + mocks + funções puras**. NUNCA publica de verdade nem chama API paga no gate. As peças "puras" (geração de roteiro a partir de skill-fake, `cronograma.proximo`, `decide_render`, iteração de `publicar_tudo` com mocks) cobrem a lógica. **E2E real** (1 livro de verdade na VPS) = manual, 1×, gateado por confirmação — fora do gate.

## Constituição — deltas a colar no `CLAUDE.md` (após aprovar)
1. **"Publicar tudo" = overview + 1 vídeo longo por capítulo, todos na playlist do livro.** Roteiro é DERIVADO da skill; ausente → gerar (passo 0), nunca publicar sem roteiro.
2. **Playlist por livro** sempre via `canal_guard.get_youtube()` (reforça contrato nº 8).
3. **Render API-first; soberano = fallback** (atualiza pilar 7: a rota de fuga agora é o soberano, não o default — porque o André comprou capacidade de API).
4. **Cronograma:** produção desacoplada da publicação; janela ∝ nº de capítulos; tick idempotente.

## Execução por `/loop-agente` (teto 20 subagentes — A05: teto, não cota)
As fases são **majoritariamente sequenciais** (0 desbloqueia 1 → 2; 3 e 4 dependem de 1). Paralelismo real é pequeno; usar subagentes só onde o trabalho é genuinamente independente, com **juiz cross-model (Sonnet)** nas peças de risco (publish-safety, quota YouTube, custo de API):
- Onda A (paralela): **Fase 0+1** (roteiro/iteração) ‖ **Fase 4** (decisão de render) — independentes.
- Onda B: **Fase 2** (playlist) depois de 1.
- Onda C: **Fase 3** (cronograma) por último (orquestra tudo).
- Cada peça: Planner→Executor→Verifier; rúbrica antes; parada em 5; **prova = `python testar.py` verde**.

## Riscos / pontos a vigiar
- **Volume de render** (N+1/livro): o teto de custo (4.2) é a catraca — ligar ANTES de produzir em lote.
- **Quota da YouTube Data API** (upload + playlist insert custam quota): medir; backoff; talvez espaçar uploads (combina com o drip do cronograma).
- **Fonte do conteúdo na VPS:** a skill precisa estar acessível na VPS (hoje `~/.claude/skills`); senão roteiro-gen lê de `/var/www/.../<slug>_data.py` (105 lá). Confirmar na Fase 0.
- **Idempotência por peça** é o que torna re-run seguro num pipeline grande — não pular.
```
