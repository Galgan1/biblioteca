# Carrossel: Livro (overview) × Capítulo — o que melhorar (Akita)

> Diagnóstico grounded (5 subagentes auditaram o código real; números reais: 99 livros, 868 capítulos, 88% dos capítulos têm 3 cards). Foco: a lógica que gera imagem de **livro** vs **capítulo**.

## Como funciona hoje
Ambos: `capa + N conceitos + CTA` (N+2 slides). **Livro** usa `overview_cards` (curados); **capítulo** usa **todos** os `ch['cards']`. Mesmos builders (`_cover/_concept/_cta`). A montagem está em **2 lugares** (`build` em Python e `_chapter_slides` no caminho Node).

## O que pode ser melhorado (prioritizado)

| Prio | Melhoria | Hoje (problema) | Fix | Onde |
|---|---|---|---|---|
| **ALTA** | **Capa não distingue livro × capítulo** | `_cover` ignora `ch`; a capa do capítulo é idêntica à do livro. O `ch['sub']` ("CAPÍTULO 1: Oceania…") existe mas não é usado → informação errada no lugar mais escaneável | `_cover(..., ch=None)`: kicker = `ch['sub']` quando houver | `gerar_carrossel._cover` ~298 + chamadas |
| **ALTA** | **Sem selo de SÉRIE** | nem capítulo ("cap X de M") nem overview ("veja os capítulos") indicam a relação → quebra o formato-assinatura do plano-alvo | selo "CAPÍTULO N · M IDEIAS" na capa do capítulo | `_cover` |
| **ALTA** | **CTA idêntico** livro × capítulo | `_cta` é byte-a-byte igual nos dois | `_cta(..., is_chapter)`: capítulo → "veja o resumo completo do livro" | `_cta` ~387 |
| **ALTA** | **Montagem duplicada (deriva Python↔Node)** | a sequência capa+conceitos+cta está copiada em `build` e `_chapter_slides`; muda um, o outro fica pra trás (+ divergência `ch=None` no overview) | extrair `montar_slides(book, cards, ch)` como **fonte única**; os dois delegam | `gerar_carrossel` + `gerar_dados_carrossel` |
| **ALTA** | **Sem teto/validação de slides** | capítulo usa todos os cards (futuro cap com 15+ = carrossel inpostável); a validação 2–10 do IG só roda **depois** de renderizar (desperdício ~30s/slide); 0 cards → "0 ideias"; 1 card → carrossel raquítico | clamp p/ ≤8 conceitos + avisos **antes** de renderizar; abortar 0 cards | `build` ~609, `gerar_dados` ~25 |
| MÉDIA | **Fallback silencioso** overview→cap1 | `overview_cards` ausente/`[]` vira o capítulo 1 sem avisar (pasta diz "overview", conteúdo é cap1) | aviso explícito no terminal | `build` ~607, `gerar_dados` ~37 |
| MÉDIA | **Densidade invertida** | o overview ficou MAIS denso (~41 palavras/slide) que o capítulo (~50) — o inverso do esperado (livro = billboard, capítulo = detalhe); ambos estouram o orçamento (~35) | overview mais billboard: reduzir `cap` no `_lead` p/ overview; usar `text_budget` como régua | `_lead` ~334 |

## GAP nº1
**O capítulo não se apresenta como capítulo, e a montagem duplica.** A capa/CTA não distinguem livro de capítulo (o leitor não sabe o que está vendo, nem que há uma série), e a sequência de slides vive em 2 arquivos (deriva silenciosa). Ou seja: falta **identidade de série** + **fonte única de montagem**.

## Plano de execução (ordem segura — arquivo compartilhado, sequencial)
1. **`montar_slides()` fonte única** (base p/ o resto) — lógica, testável (saída idêntica nos 2 caminhos).
2. **Validação/teto/clamp + aviso de fallback** — lógica, testável.
3. **`_cover(ch)` — capa de capítulo + selo de série** — visual (decisão de design).
4. **`_cta(is_chapter)` — CTA contextual** — visual (wording).
5. **Densidade billboard do overview** — visual (alvo de palavras).

**Split:** itens 1–2 são **lógica** (executo com teste verde, sem risco de gosto). Itens 3–5 envolvem **decisão visual/wording** (selo de série, texto do CTA, alvo de densidade) — confirmar com o Diretor/dono antes.
