# N6 — Auditoria da SKILL `akita`

> Auditor sênior, read-only. Alvo: `C:\Users\User\.claude\skills\akita\SKILL.md` (128 linhas).
> Fontes de verificação tentadas: `biblioteca/_akita_pesquisa/Axx_*.md` (notas que a própria skill cita), `biblioteca/akita.md`, `scratch/transcript_akita.txt`, `scratch/extract_akita.py`.
> Veredito geral: **skill saudável e bem estruturada**, com **1 achado ALTO de rastreabilidade** (lastro externo ausente no disco) e ajustes menores de numeração/concisão. Nada bloqueia o uso.

---

## 1. RASTREABILIDADE (R1) — ACHADO ALTO

### 1a. [SEVERIDADE ALTA] A pasta de notas-fonte que a skill cita NÃO existe no disco
A SKILL afirma (linha 126):
> "Notas detalhadas e auditáveis (uma por fonte) ficam em `biblioteca/_akita_pesquisa/Axx_*.md`."

A pasta `biblioteca/_akita_pesquisa/` **não existe** (busca recursiva em `scratch/` e `.gemini/` — zero resultados). O único arquivo que menciona `_akita_pesquisa` em todo o projeto é o próprio SKILL.md. Ou seja: o lastro auditável prometido (uma nota Axx por fonte) **não está versionado / não está no disco**.

O que existe de corpus Akita on-disk:
- `biblioteca/akita.md` — resumo de **36 linhas**, 5 pilares genéricos, **sem** o detalhamento [A01]..[A12] nem os URLs.
- `scratch/transcript_akita.txt` — transcrição crua (dict Python, mojibake) de **um único vídeo** do YouTube (`cWY7iBafw7I`), não dos 12 posts.
- `scratch/extract_akita.py` — script que baixou essa transcrição.

Nenhum desses sustenta as 12 fontes [Axx], que são **12 posts distintos** de akitaonrails.com. Os URLs no rodapé da skill são plausíveis e bem-formados, mas **não há nota local que prove que a afirmação X veio da fonte Axx** — exatamente o lastro que o R1 da criação exige.

**Correção mínima (escolha uma):**
- (preferida) **Recriar/versionar** `biblioteca/_akita_pesquisa/A01_*.md … A12_*.md`, uma nota curta por fonte com 2-3 citações-âncora de cada post. Restaura a auditabilidade prometida.
- (paliativo, se as notas se perderam) **Corrigir a linha 126** para não prometer arquivos inexistentes — ex.: "Fontes primárias = os 12 posts linkados abaixo (akitaonrails.com); notas locais a recriar". Não deixar a skill apontar para um caminho-fantasma.

> Observação anti-fantasma: este é o mesmo anti-padrão que a CI do projeto combate (`audita_fantasmas.py`: "passa local ≠ está no git"). Uma skill que aponta para notas não versionadas é a versão-documental do mesmo problema.

### 1b. [OK] Integridade interna de tags está íntegra
Cross-check feito: as **12 tags usadas** no corpo (A01–A12) **batem 1:1** com as **12 entradas** da seção Fontes. Nenhuma tag órfã (usada sem definição) e nenhuma definição morta (definida sem uso). A "fiação" interna está correta — o problema é só o lastro externo (1a).

### 1c. Amostra de 5 afirmações — plausibilidade vs. fonte citada
Como as notas Axx não existem, não foi possível confirmar **palavra-a-palavra** contra a fonte. Avaliei coerência interna + se a fonte citada é o post temático certo:

| # | Afirmação (linha) | Tag | Fonte coerente com o tema? | Verificável agora? |
|---|---|---|---|---|
| 1 | Karpathy "throwaway weekend projects" (L14) | [A11] | Sim — A11 é "linhagem externa / Karpathy" | Citação é factual e pública (def. de fev/2025); **OK** |
| 2 | Nomes "<5 grep hits", proíbe `data/handler/Manager` (~50 matches) (L71) | [A01] | Sim — A01 = "Clean Code pra Agentes" | Plausível; sem nota local para conferir o número exato |
| 3 | "Verde = exit code", cobertura >1:1 / ~80% (L30,32) | [A01] | Sim — TDD cai em A01 | Plausível; o nº 80%/95% precisa de âncora (não está no transcript) |
| 4 | Multi-modelo não-default; "Opus solo vence ~90%"; 3 exceções (L85) | [A05] | Sim — A05 = post "vale a pena misturar 2 modelos?" | Coerente com o título; **conferir nº "90%" na fonte** |
| 5 | Long-context+grep > RAG, "embeddings off by default" (Karpathy) (L77,79) | [A06][A08] | Sim — A08 = "RAG está morto?", A06 = ai-memory | Coerente; sem nota local p/ a citação exata |

Conclusão 1c: nada parece **inventado** — todas as 5 caem no post temático certo e são consistentes com a posição pública do Akita. Mas a verificação é **circunstancial**, não documental, justamente por causa de 1a. O nº "90%" (#4) e "~80%/95%" (#3) são os que mais pedem uma âncora explícita.

---

## 2. NUMERAÇÃO — ACHADO MÉDIO (consistência)

### [SEVERIDADE MÉDIA] "Os pilares" diz 1–8, mas há `## 9.`, `## 10.`, `## 11.` como seções soltas
Estrutura atual:
- `## Os pilares` (L20) → blocos `### 1.` a `### 8.` (subníveis `###`, dentro de "Os pilares").
- Depois, fora desse guarda-chuva: `## 9. Clean Code para agentes` (L68), `## 10. Memória e contexto` (L76), `## 11. Ferramentas` (L82) — agora em nível `##` (mesmo nível de "Os pilares").

Isso gera ambiguidade real: a numeração 1→11 sugere **11 pilares**, mas o título "Os pilares" cobre só 1–8, e 9/10/11 aparecem como **seções de topo** com `[Axx]` no título. O leitor (e o agente) não sabe se 9–11 são pilares ou apêndices. Agrava: o CLAUDE.md do projeto refere-se a "pilar 9", "pilar 10", "pilar 11", "Akita pilar 1/2/8" — ou seja, **o resto do projeto trata 9–11 como pilares**, então a skill deveria refleti-lo.

**Correção mínima (a mais barata, alinha com o CLAUDE.md):** trazer 9–11 para **dentro** de "Os pilares", como `### 9.`, `### 10.`, `### 11.` (rebaixar de `##` para `###`), e renomear o cabeçalho `## Os pilares` para algo como `## Os pilares (1–11)`. Zero perda de conteúdo, resolve a ambiguidade e fica fiel à nomenclatura "pilar N" já usada no projeto.
*(Alternativa, se quiser manter 1–8 como "núcleo":* renomear 9–11 para `## Extensões (clean code · memória · ferramentas)` **sem número**, e tirar a sequência numérica — mas isso conflita com "pilar 9/10/11" do CLAUDE.md, então é pior.)*

---

## 3. AS 3 RESSALVAS DE HONESTIDADE — TODAS PRESENTES E CORRETAS [OK]

| Ressalva | Onde | Texto | Status |
|---|---|---|---|
| (a) Karpathy "throwaway weekend projects" | L14 | "...o próprio Karpathy o restringe a *'throwaway weekend projects'*. [A11]" | **Presente, correto.** Enquadra vibe coding como o oposto do método. |
| (b) Verifier cross-model é acréscimo NOSSO; Akita não usa modelo-juiz | L86 | "⚠️ **Honestidade de fonte:** o Akita usa Planner→Executor **unidirecional** e **não usa modelo-juiz/reviewer**. Nosso `loop-agente` (Verifier **cross-model**...) é **acréscimo nosso** — não atribua ao Akita. [A05]" | **Presente, correto e explícito** (até com ⚠️). Exemplar. |
| (c) Vídeo-podcast é sátira de terceiros | L124 | "...o vídeo 'se assumiram vibe coders' é sátira de terceiros que contradiz a posição real dele" | **Presente, correto** (embutido na entrada [A12]). |

As três continuam intactas. (b) é o padrão-ouro de honestidade de fonte — não confunde o método do Akita com a extensão local. Nenhuma sugestão de mudança aqui, exceto: a ressalva (c) poderia ganhar um link/identificação do vídeo na nota A12 quando 1a for resolvido (hoje fica como afirmação sem âncora).

---

## 4. FRONTMATTER `description` — ACHADO BAIXO

O `description` (L3) é longo, denso e **alinhado ao conteúdo**: cita anti-vibe, Objetivo·Método·Restrições·Validação (pilar 1), verde=exit code (pilar 2), humano-quê/IA-como (3), refatoração (4), CI+small releases (5), constituição CLAUDE.md/AGENTS.md (6), clean code/<5 grep hits/comentário POR QUÊ (9), memória markdown+grep não-RAG (10), escolha pelo harness (11), isolamento (8). Cobertura boa.

### [SEVERIDADE BAIXA] Gatilhos ausentes / desbalanço
- **Pilar 7 (Loops de automação e auditoria) não aparece** no description — está em todos os outros pilares. "Não confie no PR, leia o diff" / auditoria contínua é um diferencial citável; vale acrescentar ("auditoria de diff, não confiar na descrição do PR").
- **Falta o gatilho de "code review / revisar diff de IA"** — um caso de uso óbvio em que esta skill deveria disparar e que não está nas palavras-chave do description.
- A ressalva (b) (Verifier ≠ Akita) é um diferencial forte da skill, mas o description não dá pista de que a skill **demarca o que é Akita vs. extensão local** — quem busca por "loop-agente / cross-model" não cai aqui. Opcional, mas é um gancho de disparo perdido.

Severidade baixa porque o description **não tem erro factual** e cobre o miolo; são gatilhos a mais, não correções.

---

## 5. CONCISÃO — ACHADO BAIXO

A skill é **densa, não inchada** — cada bullet carrega informação. Está dentro do espírito "clean code para agentes" (a própria skill prega arquivos curtos; 128 linhas cabem numa tool call). Pontos:

### [SEVERIDADE BAIXA] Pequenas repetições aceitáveis, mas mapeáveis
- "Castelo de cartas" aparece 2x (L41 pilar 4 e L104 anti-padrões) — **proposital** (princípio + anti-padrão espelhado). Idem "cemitério de superstição", "YOLO mode", "one-shot é mito". O bloco **Anti-padrões** (L100–108) é, por desenho, o espelho negativo dos pilares. É redundância **funcional** (reforço), não gordura. **Não mexer** — é um padrão de checklist útil.
- O **Checklist por tarefa** (L90–98) é **acionável e bem-feito**: 8 itens, todos verificáveis (tarefa atômica? teste executável que falha antes? 100% verde por exit code? funções ≤20 linhas / nomes <5 grep? CI passou? etc.). É o melhor pedaço operacional da skill. **Manter como está.**

### [OK] Acionabilidade
Checklist e Anti-padrões dão à skill dois "modos de uso" claros (planejar uma tarefa / detectar regressão de processo). Bom design de skill.

---

## Resumo executivo dos achados (por severidade)

| # | Severidade | Achado | Correção mínima |
|---|---|---|---|
| 1a | **ALTA** | Pasta-fonte `_akita_pesquisa/Axx_*.md` citada (L126) **não existe** — lastro auditável das 12 fontes ausente do disco | Recriar/versionar as 12 notas **ou** corrigir L126 para não apontar caminho-fantasma |
| 2 | MÉDIA | "Os pilares" diz 1–8, mas `## 9/10/11` ficam soltos como seções de topo (ambíguo: pilar ou apêndice?) | Rebaixar 9–11 para `###` dentro de "Os pilares"; título → "Os pilares (1–11)" (fiel ao CLAUDE.md, que já diz "pilar 9/10/11") |
| 4 | BAIXA | `description` não cita pilar 7 (auditoria de diff) nem gatilho "code review de IA" | Acrescentar 1–2 gatilhos ao description |
| 5 | BAIXA | Repetições princípio↔anti-padrão (intencionais) | Nenhuma ação — é reforço funcional |
| 1b/1c/3/5(checklist) | OK | Tags internas íntegras (12=12); 5 afirmações coerentes com a fonte temática; 3 ressalvas presentes e corretas; checklist acionável | — |

**Prioridade de fix:** 1a (restaura auditabilidade — o coração do R1) → 2 (consistência que confunde o agente) → 4 (gatilhos). Nada impede o uso da skill hoje; 1a é dívida de proveniência, não de correção de conteúdo.
