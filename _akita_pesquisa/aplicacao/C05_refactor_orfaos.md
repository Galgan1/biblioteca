# C05 — Refatoração: scripts órfãos do pipeline (Akita pilar 4)

> Aplicação do método Akita (refatoração contínua) ao acervo de scripts do projeto
> Biblioteca / Minuto Real. Norte: remover código morto **sem** quebrar nada, com
> verificação por **exit code** (verde = teste, não "a IA achou que está certo").
>
> **Este documento NÃO deleta nem edita nada.** É só diagnóstico + plano. Quem executa
> remoção/commit é outra lane (GitGuy / decisão humana). Pilar Akita: *humano decide o
> quê, IA o como*.

---

## 1. Estado atual

Comando rodado (leitura idempotente, nada alterado):

```
python vp100.py mapa --no-color --speed fast
```

Resultado: **74 scripts órfãos** (não alcançados pelo pipeline automático derivado de
`videos/orquestrador.py`). O pipeline real mapeado:

| Etapa | Runner real |
|---|---|
| skill | UNMANAGED (manual/outro script) |
| biblioteca | `publicar_livro.py` |
| instagram | `gerar_carrossel.py` |
| video_built | `gerar_video.py` |
| uploaded | `upload_youtube.py` |
| facebook | `facebook_publicar.py` |
| shorts | `produzir_shorts.py` |
| scheduled / tiktok | UNMANAGED |

### Como o vp100 deriva "órfão" (e onde ele erra)

O `cmd_mapa` (vp100.py L718–782) faz BFS de alcançabilidade a partir de seeds
(`ENTRYPOINT_SEEDS = {orquestrador, publicar_livro, gerar_metadados, coletar_datas}` +
nomes citados em **`.bat` da raiz**), seguindo `_refs()` (imports reais + `'X.py'` em
subprocess). Tudo em disco que não for alcançado vira órfão.

**Dois vieses estruturais do detector (causam falsos-positivos):**

1. **Ignora `videos/*.bat`** — só varre `ROOT.glob('*.bat')`. Logo, scripts invocados
   apenas por batches dentro de `videos/` aparecem como órfãos:
   - `videos/auditoria.bat` → `doctor.py`
   - `videos/gravar_demo.bat` → `tiktok_oauth.py`, `tiktok_post.py`
2. **Ignora a suíte de testes** (`videos/tests/`). Scripts cobertos por teste e rodados
   por `videos/ci.bat` (`python -m unittest discover -s tests`) são código **vivo e
   mantido**, mas o BFS não parte dos testes. Falsos-positivos confirmados:
   `diretor` (test_diretor), `doctor` (test_doctor), `pesquisador` (test_pesquisador),
   `gerar_premium` (test_marca_consistencia).

> **Observação:** os geradores legados citados no briefing
> (`gerar_arte_dados*`, `gerar_maquiavel_*`, `gerar_psicodelia*`, `gerar_smith`,
> `gerar_story`, `gerar_html_maquiavel`) **já não existem em disco** — foram removidos
> numa rodada anterior. A lista atual de 74 é diferente da "última rodada ~71".

### Método de triagem (evidência objetiva por script)

Para cada órfão coletei 4 sinais, todos restritos ao **mesmo universo do vp100** (raiz
`*.py` não-`_data` + `videos/*.py`, excluindo `_blender/`, `site-packages/`,
`worktrees/`):

- **§main** — tem `if __name__ == '__main__'`? (executável standalone)
- **§imp** — algum script **vivo** faz `import <orfao>` ou roda `'<orfao>.py'`?
- **§bat** — citado em qualquer `.bat` (raiz **e** `videos/`)?
- **§test** — coberto por `videos/tests/test_*.py`?
- **§ilha** — só referenciado por outro órfão, ou por ninguém?

---

## 2. Tabela de triagem (script | grupo | evidência)

Grupos: **MORTO** (candidato a remoção) · **MANUAL** (ferramenta/cron legítima, manter) ·
**CHECAR** (precisa decisão humana antes de qualquer ação).

### 2a. Grupo MORTO — "ilha drdolabela" (18: ingestão acadêmica + depuração)

Pipeline pontual **já encerrado** de ingestão da bibliografia acadêmica `drdolabela`
(217 obras, lotes 2–5, knowledge-graph). Caminhos hard-coded para
`config\skills\drdolabela`, `mapped_books.json`, `phase2_payloads.json`,
`kg_report_*.md`, `MASTER_MIND.md`. Nenhum `__main__` estruturado, nenhum import por
vivo, nenhum teste, nenhum `.bat`. Referenciam-se só entre si → **ilha morta**.

| Script | Grupo | Evidência |
|---|---|---|
| `parse_bib.py` | MORTO | lê `parsed_bibliography.json`; sem main/imp/bat/test; ilha |
| `map_books.py` | MORTO | escreve `mapped_books.json`; paths drdolabela; ilha |
| `match_books.py` | MORTO | lista de keywords hard-coded; ilha |
| `generate.py` | MORTO | dict de skills campbell/carter hard-coded; ilha (0 ref a imagen/veo) |
| `generate_master_mind.py` | MORTO | lê `mapped_books.json`; categoriza; ilha |
| `generate_payload.py` | MORTO | gera payload de subagentes p/ `mapped_books`; ilha |
| `generate_phase2_payloads.py` | MORTO | gera `phase2_payloads.json`; ilha |
| `prep_subagents.py` | MORTO | lê `_kit_preview/PROMPT-GEMINI-COMPLETO.md` → `phase2_payloads.json`; ilha |
| `dump_batches.py` | MORTO | quebra `phase2_payloads.json` em `gemini_in/batch_*`; ilha |
| `merge_gemini_out.py` | MORTO | junta `gemini_in/batch_*_out.md`; ilha |
| `merge_kg_reports.py` | MORTO | junta `kg_report_1..5.md` em `MASTER_MIND.md` (ausente); ilha |
| `hyperlinker.py` | MORTO | `lote_5` de skills drdolabela hard-coded; ilha |
| `hyperlink_lote2.py` | MORTO | `target_skills` drdolabela hard-coded; ilha |
| `lote3_link.py` | MORTO | `lote3_skills` hard-coded; ilha |
| `audit_script.py` | MORTO | audita `mapped_books.json` vs skills drdolabela; ilha |
| `debug.py` | MORTO | cópia da lista `lote3_skills` (sobra de depuração); ilha |
| `dump_transcript.py` | MORTO | lê `antigravity\brain\<uuid>\...\transcript.jsonl` (sessão única) |
| `dump_full_transcript.py` | MORTO | idem `transcript_full.jsonl` de **uma** sessão específica |

*(18 scripts. `cleanup.py` e `list_skills.py` ficam em CHECAR — ver abaixo.)*

### 2b. Grupo MANUAL — ferramentas e cron legítimos (manter)

Scripts com `__main__`, propósito declarado, e/ou que pertencem a **lanes ativas**
documentadas na memória do usuário (Instagram @minutoreal1701, Facebook "Minuto Real",
TikTok @minuto_real2, Amazon afiliados, vídeo premium/3D). Não são alcançados pelo
**orquestrador automático** porque são acionados **à mão** ou por **cron/wave** — exatamente
o caso de uso "ferramenta manual" que o próprio vp100 descreve.

| Script | Sub-lane | Evidência |
|---|---|---|
| `afiliado_youtube.py` | Amazon/YouTube | main; "link de afiliado na descrição dos vídeos" |
| `agendar_denso.py` | Instagram | main; "calendário denso IG: carrossel+stories" |
| `agendar_instagram.py` | Instagram | main; "popula fila IG ≥1 post/dia" |
| `agendar_lancamento.py` | Instagram | main; agenda lançamento |
| `agendar_lote.py` | scheduling | main; importa `dag`/`pipeline_state` (motores vivos) |
| `analytics_ig.py` | Instagram | main; "analytics de performance do IG" |
| `auth_analytics.py` | Instagram | helper de auth para analytics_ig |
| `aplicar_pos.py` | YouTube | main; "pós-produção (legendas+capítulos) em vídeo já no YT" |
| `recuperar_timing.py` | YouTube | main; recupera timing de vídeo já construído |
| `comentar_pendentes.py` | Instagram/FB | main; comenta CTA pendente |
| `comentar_pendentes_vps.py` | Instagram/FB | main; variante VPS |
| `enfileirar_comentarios.py` | Instagram/FB | main; usa `pipeline_state` |
| `ig_runner_vps.py` | Instagram | main; runner IG na VPS |
| `facebook_post.py` | Facebook | main; "publicação na Página FB via Graph API"; usa facebook_comment/insights/video |
| `facebook_carrossel.py` | Facebook | main; "carrossel nativo FB"; usa facebook_copy |
| `facebook_reels.py` | Facebook | main; "Reels nativos FB"; usa facebook_copy |
| `tiktok_oauth.py` | TikTok | main; citado em `videos/gravar_demo.bat` |
| `tiktok_post.py` | TikTok | main; "Content Posting API @minuto_real2"; em `gravar_demo.bat` |
| `upload_shorts_batch.py` | YouTube | main; upload de Shorts em lote |
| `gerar_thumb.py` | YouTube | main; gera thumbnail; usa check_krug/check_marca |
| `thumb_set.py` | YouTube | "define thumbnail custom via YouTube Data API" |
| `gerar_canal_art.py` | YouTube | main; arte de canal; usa check_marca |
| `sincronizar.py` | wave/distrib. | main; "orquestrador da sincronia YT→IG (eco)" |
| `doctor.py` | CI/saúde | main; citado em `videos/auditoria.bat`; test_doctor |
| `diretor.py` | vídeo | main; "shot list"; coberto por test_diretor |
| `pesquisador.py` | vídeo | main; "gera/pontua ganchos"; coberto por test_pesquisador |
| `gerar_premium.py` | carrossel | "gerador PREMIUM 1080×1350"; coberto por test_marca_consistencia |
| `gerar_mapa.py` | infográfico | main; "MAPA DO LIVRO field-guide 1080×1350" |
| `marca_sonora.py` | áudio | main; "10 sons procedurais (marca sonora)"; importa `dsp` (feature não ligada ao build) |
| `check_krug.py` | guardrail | main; "guardrail de usabilidade (Krug+Norman)" |
| `check_marca.py` | guardrail | main; "guardrail de saúde do design (marca.py)" |
| `cinegrafista_smoke.py` | smoke 3D | smoke test manual do cinegrafista |
| `splatting_smoke.py` | smoke 3D | smoke test manual do gaussian-splatting |
| `cenario3d.py` | Blender | main; "livro 3D girando (turntable)" |
| `personagem_3d.py` | Blender | main; "personagem 3D procedural" |
| `cena_professor.py` | Blender | "cena professor + livro 3D" |
| `orbita_3d.py` | Blender/GPU | main; "render de órbita 3D (DepthFlow)" |
| `proto_cena.py` | protótipo | "protótipo de uma cena premium (Ken Burns)" |
| `proto_premium.py` | protótipo | main; "proof slide premium" |
| `relatorio_desempenho.py` | analytics | main; "cientista de dados — lê datas_coletadas.json" |
| `ocr_pdf.py` | book-to-skill | main; "OCR de PDFs-imagem via Tesseract" |
| `converter_webp.py` | site/assets | converte imagens p/ webp |
| `revisar_textos.py` | conteúdo | "revisão de markdown cru remanescente" |
| `enriquecer.py` | conteúdo | main; "enriquece cards de um livro até padrão-ouro" |
| `scan_magros.py` | conteúdo/QC | "conta cards por capítulo, lista capítulos magros" |
| `build_design.py` | site | "monta /biblioteca/design (comparação de estilos)" |
| `render_pdf.py` | QC visual | "rasteriza PDFs em PNG p/ inspeção" |
| `retrofit_breadcrumb.py` | site (retrofit) | main; injeta breadcrumb em páginas já geradas |
| `inserir_candidatos.py` | site | main; "insere livros candidatos na estante" |
| `classify_collections.py` | site | main; "verificação da taxonomia de coleções" |
| `aplicar_texto.py` | conteúdo | main; aplicador de texto (par do ingerir_gemini) |

### 2c. Grupo CHECAR — decisão humana antes de tocar

| Script | Por que CHECAR |
|---|---|
| `exportar_para_gemini.py` | main; "gera pacotes p/ delegar aprofundamento ao Gemini". Faz par com `ingerir_gemini.py` / `aplicar_texto.py`. Fluxo de delegação **ainda usado**? Pode ser MANUAL ativo ou rota soberana parada. |
| `ingerir_gemini.py` | main; "ingere resposta do Gemini de volta no pipeline". Mesmo par acima. |
| `cleanup.py` | sem main; limpa `BOOK_SKILL_WORKDIR` (temp do book-to-skill). Trivial, mas pode ser chamado à mão pós-extração. Baixo valor, baixo risco. |
| `list_skills.py` | sem main; dumpa `config/skills/*` → `skills_list.json`. Genérico; pode servir a outra lane fora do escopo vp100. |
| `process.py` | **Ambíguo**: o cabeçalho é a lista `lote_4` drdolabela (cheira a MORTO/ilha), mas o nome genérico e os imports largos pedem leitura completa antes de condenar. Tratar como drdolabela só após confirmar que todo o corpo é daquele pipeline. |
| `marca_sonora.py` | listado em MANUAL, mas **atenção**: a memória do usuário diz que `place_marca` *deveria* estar mapeado às cenas via `gerar_video`; hoje **não está importado** por nenhum vivo. É *feature pendente de fiação*, não morto — não remover. |

**Risco transversal de toda a ilha drdolabela:** os artefatos que ela consome **ainda
existem** em disco (`mapped_books.json`, `parsed_bibliography.json`,
`phase2_payloads.json`, `audit_validation.md`, `kg_report_1.md`, `user_messages.json`) e
a pasta `config/skills/drdolabela` **existe**. A memória do usuário registra um
*"backlog-bibliografia-academica"* (~200+ refs) com a regra **"confirmar com usuário
antes de produzir"**. Ou seja: o pipeline está **dormente**, não comprovadamente lixo. Por
isso a remoção do grupo MORTO **exige aval humano explícito** (Akita: humano decide o quê).

---

## 3. Plano de remoção do grupo MORTO (verificação por exit code)

Espírito Akita: a remoção só "fica verde" se for provada por comandos com **exit code**,
não por inspeção visual. Sequência incremental e reversível.

**Pré-condição (gate humano):** o usuário confirma que o pipeline `drdolabela` /
knowledge-graph está encerrado e pode sair do repo. Sem esse "sim", **não** prosseguir.

### Passo 0 — Baseline verde (antes de tocar em nada)

```bash
cd videos && python -m py_compile net.py dag.py contracts.py circuit_breaker.py \
  pipeline_state.py cost_tracker.py orquestrador.py        # esperar exit 0
python -m unittest discover -s tests -t .                  # esperar exit 0  (== videos/ci.bat)
cd .. && python vp100.py mapa --no-color --speed fast      # registrar baseline: 74 órfãos
```

Guardar a contagem de órfãos e o "[ok] CI local verde" como linha-base.

### Passo 1 — Provar zero referências vivas a cada candidato

Para cada um dos 17 candidatos MORTO, confirmar que **nenhum script de produção** (raiz
não-`_data` + `videos/`, fora de `_blender`/`site-packages`/`worktrees`) o importa ou o
invoca por subprocess, e que **nenhum `.bat`** o cita:

```bash
# alvo = nome sem .py ; deve imprimir NADA (grep retorna exit 1 = "limpo")
ALVO=parse_bib
grep -rnE "^\s*(import|from)\s+${ALVO}\b|['\"]${ALVO}\.py['\"]" \
  --include=*.py . \
  | grep -vE "_blender|site-packages|/\.git/|worktrees|/${ALVO}\.py:"
grep -rn "${ALVO}\.py" --include=*.bat .
```

Critério verde: as duas buscas vêm **vazias** para todos os 18. (Já pré-verificado neste
diagnóstico — §imp/§bat/§test = vazios para os 17 — mas repetir no momento da remoção,
pois o working tree é compartilhado entre lanes.)

### Passo 2 — Remoção em UM lote atômico (só os 18 confirmados)

`parse_bib map_books match_books generate generate_master_mind generate_payload
generate_phase2_payloads prep_subagents dump_batches merge_gemini_out merge_kg_reports
hyperlinker hyperlink_lote2 lote3_link audit_script debug dump_transcript
dump_full_transcript`

> A remoção é da lane GitGuy / decisão humana. **Este documento não deleta.** Recomenda-se
> remover num único conjunto, sem misturar com outras mudanças, para diff limpo e rollback
> trivial (`git restore`).
>
> Opcional menos destrutivo: mover para `_legado/` (já existe no repo) em vez de apagar —
> preserva o histórico de uso fora do caminho dos detectores.

### Passo 3 — Provar que nada quebrou (re-verde)

```bash
cd videos && python -m py_compile net.py dag.py contracts.py circuit_breaker.py \
  pipeline_state.py cost_tracker.py orquestrador.py        # exit 0
python -m unittest discover -s tests -t .                  # exit 0  (mesma suíte do baseline)
cd .. && python -c "import publicar_livro, gerar_livro"    # geradores do site importam OK
python vp100.py mapa --no-color --speed fast               # órfãos = 74 - 18 = 56
```

### Passo 4 — Provar que o SITE ainda gera

Sanidade end-to-end do produto (estética cheat-sheet verde):

```bash
python gerar_livro.py <um-slug-existente>     # regenera 1 página → exit 0, HTML emitido
# ou a skill run-biblioteca para smoke + screenshot da estante
```

Critério de aceite global (rúbrica): **(a)** CI local verde igual ao baseline; **(b)**
órfãos caíram exatamente de 74 → 56, sem novos órfãos surgirem; **(c)** site gera 1 página
sem erro. Falhou qualquer um → `git restore` e reabrir triagem.

---

## 4. Risco / colisão

- **Working tree compartilhado entre lanes (Bibliotecário, YouTube, Instagram, etc.).**
  É o hazard nº1 do projeto. A janela entre o Passo 1 (grep limpo) e o Passo 2 (remoção)
  deve ser curta; rodar grep imediatamente antes de remover, não confiar só neste
  snapshot.
- **MANUAL ≠ inútil.** A lista 2b é majoritariamente do **Bibliotecário** (site:
  `inserir_candidatos`, `classify_collections`, `build_design`, `retrofit_breadcrumb`,
  `enriquecer`, `scan_magros`, `converter_webp`) e das lanes de redes/vídeo. **Não tocar.**
  O vp100 marca como órfão porque são manuais — é o comportamento esperado, não defeito.
- **Falsos-positivos do detector ainda presentes** (`doctor`, `tiktok_*` via
  `videos/auditoria.bat`/`gravar_demo.bat`; `diretor`/`pesquisador`/`doctor`/`gerar_premium`
  via testes). *Melhoria opcional* (fora deste escopo, requer editar vp100 = produção):
  fazer o BFS também semear de `videos/*.bat` e de `videos/tests/`. Isso reduziria o ruído
  de ~14 órfãos sozinho. **Proposto, não executado.**
- **drdolabela dormente, não morto.** Artefatos e pasta de skills ainda existem; há backlog
  acadêmico registrado. Remover sem aval pode enterrar trabalho que o usuário pretende
  retomar. Gate humano é obrigatório.
- **`process.py` e `marca_sonora.py`** são as duas armadilhas: nome/uso que enganam.
  `process` parece drdolabela mas exige leitura integral; `marca_sonora` é feature a fiar,
  não lixo. Ambos ficam fora do lote de remoção até decisão explícita.
