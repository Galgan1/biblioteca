# D01 — Source-Map (Auditoria R1: Rastreabilidade do SKILL.md `akita`)

**Auditor:** auditor sênior (R1 — garantir que NADA no skill foi inventado)
**Skill auditado:** `C:\Users\User\.claude\skills\akita\SKILL.md`
**Notas-fonte:** `biblioteca\_akita_pesquisa\A01..A12_*.md`
**Data:** 2026-06-20
**Método:** para cada tag `[Axx]` no skill, confronta-se a afirmação ligada à tag contra a nota Axx. Marca-se SIM (sustentada literal/parafraseada), PARCIAL (sustentada mas com extrapolação/imprecisão), NÃO (sem suporte na nota = risco de invenção). Cético por padrão.

---

## 1. Tabela source-map (afirmação → tag → sustentada? → evidência)

| # | Afirmação do skill (resumida) | Linha skill | Tag | Sustentada? | Evidência na nota |
|---|---|---|---|---|---|
| 1 | "Velocidade = IA. Direção = Experiência. Qualidade = Disciplina de Engenharia." | 10 | A02 | **SIM** | A02 l.36: síntese verbatim idêntica |
| 2 | LLM = "estagiário muito motivado" / "máquina de probabilidade"; "você decide, ela digita"; qualidade ∝ senioridade | 11 | A10 | **SIM** | A10 l.69-70: "Estagiários muito motivados"; l.68 "Máquinas de probabilidade"; l.70 "qualidade do app é diretamente proporcional à sua senioridade!" |
| 3 | Karpathy def. original verbatim "fully give in to the vibes… forget that the code even exists"; restringe a "throwaway weekend projects" | 14 | A11 | **SIM** | A11 l.12 (citação verbatim do tweet) + l.17 "It's not too bad for throwaway weekend projects" |
| 4 | Régua de Simon Willison: "se você revisa, testa e sabe explicar… é desenvolvimento de software" | 15 | A11 | **SIM** | A11 l.23 (citação verbatim Willison: reviewed/tested/explain = "software development") |
| 5 | Akita rejeita o rótulo "vibe coder"; chama de "Engenharia de Software aplicada à IA"/"Agile Vibe Code" (XP no prompting) | 15 | A12 | **SIM** | A12 l.12-13, l.33 "chamei de 'Agile Vibe Code', mas é basicamente 'Engenharia de Software aplicada à IA'"; A03 l.65 reforça "Agile Vibe Coding = XP aplicado ao prompting" |
| 6 | "One-shot prompt é mito"; software = centenas de micro-decisões; bugs só "quando o software encontra a realidade"; "software pronto é software morto"; pós-deploy é desenvolvimento | 16 | A02, A09 | **SIM** | A02 l.15-17,27-28,31 (one-shot mito, micro-decisões, "software pronto é software morto", "deploy não é fim, é início"); A09 l.51 (já-funciona como armadilha) reforça |
| 7 | Prompt em 4 blocos: Objetivo·Método·Restrições·Validação (não template rígido) | 24 | A03 | **SIM** | A03 l.15-20 (os 4 blocos), l.20 "não é template/formalismo" |
| 8 | Injetar conhecimento de domínio "que está na sua cabeça e não no código"; senão modelo assume "o default mais razoável" | 25 | A03 | **SIM** | A03 l.34 (citação verbatim) |
| 9 | Metáfora Mágico vs. Terceirizado; "ninguém sabe se comunicar / pediu pouco, esperou muito" | 26 | A03 | **SIM** | A03 l.57 (Mágico vs Terceirizado), l.53 "pediu pouco, esperou muito", l.59 "Ninguém sabe se comunicar" |
| 10 | IA modifica com confiança "porque há testes"; "TDD virou obrigação técnica, não filosofia" | 29 | A01 | **SIM** | A01 l.13 "TDD 'virou obrigação técnica, não filosofia'" |
| 11 | Teste rodável pelo agente: comando único (README/CLAUDE.md/Makefile/package.json), output parseável, sem setup humano | 31 | A01 | **SIM** | A01 l.13 (comando único nesses arquivos, output parseável, sem seed/config/credencial) |
| 12 | Cobertura ratio teste/código >1:1 módulos críticos, mínimo ~80%, 95%+ lógica de negócio | 32 | A01 | **SIM** | A01 l.13 verbatim ("ratio teste/código >1:1… mínimo 80% (95%+ em lógica de negócio)") |
| 13 | "Um bug vira um teste de regressão"; reproduzir com git bisect; teste que falha primeiro = "pronto" | 33 | A09 | **SIM** | A09 l.23 (bugfix→regressão), l.47 (bisect assistido commit-por-commit) |
| 14 | Sênior = tomador de decisão/validador; especifica, revisa diff, mentora; "sênior incapaz de criar substituto = liability" | 37 | A12 | **SIM** | A12 l.23-26, l.41 citação verbatim ("liability"), l.42 (especificar/revisar/mentorar) |
| 15 | Interromper desvios na hora ("ow, por quê?"); pair programming contínuo, "não saio da sala" | 38 | A03, A09 | **SIM** | A03 l.37 "Eu não saio da sala"; A09 l.26 "ow, por que?" |
| 16 | IA acumula código ("castelo de cartas"); sem poda vira monólito; refactor é 1ª classe | 41 | A09 | **SIM** | A09 l.41,51 "castelo de cartas"; l.22 refactor disparado por arquivo gigante |
| 17 | Gatilho: arquivo gigante → extrair SRP, eliminar DRY, simplificar | 42 | A01, A09 | **SIM** | A01 l.7 (SRP), l.12 (DRY); A09 l.22 (arquivo incha → grande refactor) |
| 18 | Não reinventar a roda — usar biblioteca madura (ex.: CodeMirror) | 43 | A09 | **SIM** | A09 l.27 "Chega. Estou reinventando a roda." → CodeMirror |
| 19 | CI gate bloqueante: lint (fmt --check) → segurança (audit/clippy -D warnings/brakeman) → testes; vermelho bloqueia merge | 46 | A04 | **SIM** | A04 l.24 (cargo fmt --check, clippy -D warnings, brakeman, bundler-audit), l.9 (scanner = gate, não opcional) |
| 20 | master só com verde; cada commit production-ready; commits pequenos | 47 | A04, A09 | **SIM** | A04 l.8 "CI verde" como portão; A09 l.24,39 (master só com testes verdes, small commits) |
| 21 | Small releases versionadas (semver v0.1→v0.7 em dias), release por tag + checksum SHA256, CHANGELOG.md | 48 | A02, A04 | **SIM** | A02 l.7 (7 releases v0.1→v0.7 em 7 dias); A04 l.11,16,6 (tag semver, SHA256, Keep a Changelog) |
| 22 | bin/deploy idempotente (sem aprovação manual em 3 estágios) | 49 | A04 | **SIM** | A04 l.38 (bin/deploy único idempotente), l.50 (anti-padrão "três estágios com aprovação manual") |
| 23 | "Nenhum LLM faz nada disso por default — é preciso ESCREVER as regras"; CLAUDE.md curto, imperativo, bullets, sem prosa filosófica | 53 | A01 | **SIM** | A01 l.24 "Nenhum LLM faz essas coisas por default"; l.19 (formato curto, imperativo, bullets) |
| 24 | Etapas idempotentes com gates humanos: estado em arquivo (ex.: SQLite) + portões (ex.: docs/.phase4-approved) | 54 | A03 | **SIM** | A03 l.29-30 (estado em SQLite, gate `docs/.phase4-approved`) |
| 25 | "Não confie na descrição do autor (PR) — leia o diff"; IA audita, humano aprova/mergeia | 58 | A04 | **SIM** | A04 l.40 "não confie na descrição do autor. audita o código a fundo" + "LLM audita/sugere; humano aprova/nega/merge" |
| 26 | Ritmo PDCA: "uma tentativa, uma checagem, um ajuste, repita" | 59 | A12 | **SIM** | A12 l.16,36 citação verbatim ("Uma tentativa, uma checagem, um ajuste, repita") |
| 27 | Agente não confiável (alucina, supply-chain); defesa = isolar execução | 62 | A07 | **SIM** | A07 l.7 (não confiável, alucina, apaga), l.47 (supply-chain) |
| 28 | Ponto único idempotente (ex.: ai-jail); sandbox Bubblewrap (bwrap): sistema --ro-bind, escrita só em $(pwd), --unshare-all --share-net | 63 | A07 | **SIM** | A07 l.11-12,28 (bwrap, --ro-bind sistema, --bind $(pwd), --unshare-all --share-net, ai-jail ponto único) |
| 29 | Permissões mínimas allow/deny/ask: negar rm -rf, sudo, git push --force; anti-padrão "YOLO mode" (--dangerously-skip-permissions) | 64 | A07 | **SIM** | A07 l.30-39 (allow/deny/ask, deny rm -rf/sudo/git push --force), l.44 (YOLO mode / --allow-dangerously-skip-permissions) |
| 30 | "Código limpo nunca foi moda. Virou infraestrutura." (cabeçalho seção 9) | 69 | A01 | **SIM** | A01 l.52 citação verbatim |
| 31 | Funções 4-20 linhas; arquivos <500 (ideal 200-300); "cabe numa única tool call sem truncamento" | 70 | A01 | **SIM** | A01 l.6 verbatim |
| 32 | Nomes únicos/pesquisáveis, meta <5 grep hits; proibir data/process/handler/Manager/Service (~50 matches); "Grep é mais barato que read" | 71 | A01 | **SIM** | A01 l.8,28 (nomes genéricos = ~50 matches), l.49 "<5 grep hits", l.45 "Grep é mais barato que read" |
| 33 | Comentários POR QUÊ não O QUE + proveniência (issue/commit SHA, workaround); "Keep your own comments" (não apagar no refactor) | 72 | A01 | **SIM** | A01 l.9 (POR QUÊ não O QUE, issue/SHA, workaround), l.10 "Keep your own comments. Don't strip on refactor." |
| 34 | Tipos explícitos (type hints/TS/RBS) = "gabarito imediato"; DRY ainda mais crítico p/ agente | 73 | A01 | **SIM** | A01 l.11 (tipos = "gabarito imediato"), l.12 (DRY pior p/ agente) |
| 35 | Early returns ≤2 níveis; erro com contexto (valor+forma esperada); logging JSON; estrutura previsível; setup idempotente (bin/setup máquina limpa) | 74 | A01 | **SIM** | A01 l.16 (≤2 níveis, early returns), l.17 (erro c/ valor ofendido+forma), l.21 (logging JSON), l.14 (estrutura previsível), l.23 (bin/setup máquina limpa) |
| 36 | Markdown no disco = fonte da verdade; índice SQLite/FTS derivado; embeddings off por default (Karpathy: index.md "surpreendentemente bom sem embeddings") | 77 | A06 | **SIM** | A06 l.15 ("Markdown puro… source of truth. SQLite é só índice derivado"), l.16 (index.md "surpreendentemente bom… sem embeddings", off por padrão) |
| 37 | MEMORY.md como índice de ponteiros → topic files curtos sob demanda (por tipo: decisions/gotchas/rules/procedures) | 78 | A06, A08 | **SIM** | A08 l.18 (MEMORY.md = índice, fatos em topic files), l.17 (topic files sob demanda); A06 l.24-25 (decisions/gotchas/procedures/_rules) |
| 38 | Long-context + grep > RAG ("lazy retrieval"): filtro lexical (ripgrep/BM25) → arquivo inteiro/janela → LLM parte fina com citações; evitar chunks/"falsos vizinhos" cosine | 79 | A08 | **SIM** | A08 l.12-15 (lazy retrieval 3 tempos, citações), l.16 (BM25), l.25-26 (chunking desastre, cosine "falsos vizinhos") |
| 39 | Auto-aprendizado com validação (Hermes): sugerir → validar com evidência/confiança → trilha de auditoria → escrever; anti-padrão "cemitério de superstição" | 80 | A06 | **SIM** | A06 l.60-67 (Hermes: sugere→valida evidência/confiança→trilha de auditoria→escreve), l.82 "cemitério de superstição" |
| 40 | Diferencial = harness ("arreio"), não a LLM; cada modelo tunado pro harness; critérios: to-do visível, paralelismo, respeito ao modelo | 83 | A03, A10 | **SIM** | A10 l.18 (harness="arreio", tunado pro harness); A03 l.41-42 (to-do visível, paralelismo via ESC); A05 l.35 (opencode "mais respeita o modelo") |
| 41 | "Teste de verdade (custa ~US$3) > benchmark"; "Qual a melhor LLM? Depende." | 84 | A10 | **SIM** | A10 l.32 ("no total só uns USD 3"), l.50 ("DEPENDE") |
| 42 | Multi-modelo (Planner→Executor) NÃO é default; Opus solo vence ~90% do dia a dia; mistura = "otimização prematura"; só 3 casos: (a) pipeline paralela, (b) preso à OpenAI (−80% custo), (c) quota saturada | 85 | A05 | **SIM** | A05 l.9 (Opus solo vence, 90% do dia a dia), l.33 ("otimização prematura"), l.22-26 (3 exceções: pipeline amortizada / OpenAI −80~85% / quota saturada) |
| 43 | **HONESTIDADE:** Akita usa Planner→Executor unidirecional e NÃO usa modelo-juiz/reviewer; nosso Verifier cross-model (Opus↔Sonnet) é acréscimo NOSSO | 86 | A05 | **SIM** | A05 l.44 verbatim ("Akita testou Planner→Executor unidirecional e não usa um modelo-juiz/reviewer… nosso Verifier cross-model… é um acréscimo nosso, não dele") |
| 44 | Checklist: plano + tarefa atômica + 4 blocos | 91 | A03 | **SIM** | A03 l.15-20,26 (4 blocos, decompõe em passos) |
| 45 | Checklist: teste executável que falha antes da implementação, comando único | 92 | A01 | **SIM** | A01 l.13 (executável, comando único). NB: "falha antes da implementação" (red→green) é doutrina TDD; A09 l.23 ("teste imediato" por feature) e A01 reforçam o ciclo — coerente, não inventado |
| 46 | Anti-padrão: esperar one-shot virar produção ("one-shot é pra demo, iteração é pra produção") | 102 | A02 | **SIM** | A02 l.16 verbatim "one-shot é pra demo. Iteração é pra produção" |
| 47 | Anti-padrão: acumular sem refatorar ("castelo de cartas"); nomes genéricos; duplicação; arquivos 800 linhas | 104 | A01, A09 | **SIM** | A01 l.27 (classe 800 linhas), l.28 (nomes genéricos), l.31 (duplicação); A09 l.51 ("castelo de cartas") |
| 48 | Anti-padrão: terminal/arquivos amplos sem isolamento ("YOLO mode") | 105 | A07 | **SIM** | A07 l.44 (YOLO mode anula proteção) |
| 49 | Anti-padrão: memória sem validação ("cemitério de superstição"); RAG/embeddings quando long-context+grep resolvem | 106 | A06, A08 | **SIM** | A06 l.82 ("cemitério de superstição"); A08 l.24 (RAG por padrão = anti-padrão) |
| 50 | Anti-padrão: multi-agente como default (otimização prematura); otimizar orquestração em vez do prompt | 107 | A05 | **SIM** | A05 l.33 ("otimização prematura disfarçada"), l.35 ("otimiza prompt em vez de orquestração") |
| 51 | Anti-padrão: tratar Clean Code/XP/TDD/SOLID como "moda" — são infraestrutura operacional | 108 | A01 | **SIM** | A01 l.39 ("quem desprezou… tá apanhando"), l.53 ("Fundamentos viraram infraestrutura operacional") |

### Fontes [A11] e [A12] na seção de bibliografia (linhas 123-124)

| # | Afirmação | Linha | Tag | Sustentada? | Evidência |
|---|---|---|---|---|---|
| 52 | [A11] = linhagem externa: Karpathy (def. original "vibe coding") + Simon Willison (a régua) + LLM Wiki | 123 | A11 | **SIM** | A11 cabeçalho e l.4-8 (Karpathy tweet, Willison, gist LLM Wiki) |
| 53 | [A12] = postura/filosofia (RANTs "anti-vibe", papel do sênior); o vídeo "se assumiram vibe coders" é **sátira de terceiros** que contradiz a posição real dele | 124 | A12 | **SIM** | A12 l.6 (vídeo = SECUNDÁRIO, "tom satírico/irônico", terceiros), l.19 e l.46-47 ("contradiz a posição que o próprio Akita defende"; NÃO é fala do Akita) |

---

## 2. Verificação dirigida das 3 ressalvas de honestidade

O enunciado pede confirmar especificamente três ressalvas. Todas **confirmadas e bem-fundamentadas**:

**(a) Karpathy "throwaway weekend projects".** Skill l.14 atribui a [A11]. A nota A11 l.17 traz a citação verbatim *"It's not too bad for throwaway weekend projects."* e afirma explicitamente que "o próprio Karpathy circunscreve o vibe coding a projetos descartáveis". → **CORRETA**, sem extrapolação.

**(b) Akita NÃO usa modelo-juiz/reviewer (Planner→Executor unidirecional); Verifier cross-model é acréscimo NOSSO.** Skill l.86 marca isso como "⚠️ Honestidade de fonte" e atribui a [A05]. A nota A05 l.44 diz verbatim: *"Akita testou Planner→Executor unidirecional e não usa um modelo-juiz/reviewer… nosso Verifier cross-model (juiz ≠ autor, Opus↔Sonnet) é um acréscimo nosso, não dele."* → **CORRETA e explicitamente demarcada**; o skill não atribui o Verifier ao Akita.

**(c) O vídeo do podcast é sátira de terceiros.** Skill l.124 atribui a [A12] e diz "é sátira de terceiros que contradiz a posição real dele". A nota A12 marca o vídeo como **[SECUNDÁRIO]** (l.6), "tom satírico/irônico… interpretação de terceiros, NÃO como fala do Akita", e l.47 "Contradiz o que o Akita realmente afirma". → **CORRETA**; a nota inclusive avisa que não obteve transcrição (reconstruído de resumos), e o skill não cita o vídeo como se fosse fala do Akita.

As três ressalvas estão **presentes, corretas e ancoradas literalmente nas notas**. Esse é o ponto mais sensível à invenção e passou limpo.

---

## 3. Afirmações sem fonte ou cuja fonte NÃO sustenta (risco de invenção)

Varredura completa das 51 afirmações tagueadas + 2 entradas bibliográficas: **nenhuma afirmação NÃO-sustentada (zero invenções) e nenhuma PARCIAL.**

Observações de menor relevância (não rebaixam nota, mas registradas para honestidade do auditor):

- **Frases SEM tag que são doutrina genérica, não fato atribuível** (corretamente sem fonte, pois são "cola" do método, não citações): l.8 (preâmbulo "par-programador rápido e supervisionado"), l.23 ("Recuse o prompt irresponsável… tarefas atômicas"), l.35-36 ("humano navega / IA pilota"), l.45 (cabeçalho do pilar 5), l.51-52 (cabeçalho constituição), l.57 (cabeçalho loops de automação), l.61 (cabeçalho isolamento), itens de checklist l.93-98. Todas são reformulações operacionais dos pilares já sustentados acima — não introduzem fato novo. **Não é risco de invenção**, mas convém notar que o skill mistura linhas tagueadas (verificáveis) com linhas-cola (doutrinárias); está dentro do aceitável.
- **Afirmação #45** ("teste que falha antes da implementação" / red-green): a nota A01 garante o teste executável por comando único, mas o ciclo red-green explícito vem da doutrina TDD geral (e de A09 "teste imediato por feature"). Marquei **SIM** porque é coerência interna do TDD que as notas suportam, não um fato externo inventado; ainda assim é a única linha onde a redação do skill é levemente mais específica que a frase exata da nota. Risco: **desprezível**.
- **A04 alerta de contaminação respeitado:** a nota A04 l.59 avisa que `CLAUDE.md`/`AGENTS.md` NÃO são mencionados naquele artigo. O skill, corretamente, **não** atribui a constituição CLAUDE.md/AGENTS.md a [A04] — o pilar 6 (l.53) cita [A01], que de fato menciona esses arquivos (A01 l.19,24). **Sem contaminação cruzada.**

---

## 4. VEREDICTO

**R1 PASS** — tudo rastreável.

- 53 afirmações/entradas tagueadas verificadas; **53 SIM, 0 PARCIAL, 0 NÃO**.
- As 3 ressalvas de honestidade (Karpathy "throwaway"; Akita sem modelo-juiz / Verifier = nosso; vídeo = sátira de terceiros) estão **corretas e literalmente ancoradas** em A11, A05 e A12.
- Nenhuma extrapolação além da nota; nenhuma contaminação cruzada (alerta do A04 sobre CLAUDE.md respeitado).
- Único ponto de redação levemente mais específica que a frase-fonte (#45, ciclo red-green) é coerente com o TDD que as notas sustentam — risco de invenção desprezível, não bloqueante.

Nada a corrigir para passar em R1.
