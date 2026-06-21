# Constituição — Lane Conversor Livro→Skill (Akita)

> Constituição da lane (Akita pilar 6): contratos **invioláveis**, imperativos, em bullets.
> O agente lê ANTES de cada conversão. "Pronto" = **`python valida_skill_lane.py` verde (exit 0)**,
> não "a IA achou que está certo" (Akita pilar 2). Gate no comando único: `python testar.py`.

## Papel (o QUÊ é da lane)
- A lane entrega **a SKILL destilada** em `~/.claude/skills/<slug>/`. Etapa 1 do maestro.
- **Não sobe nada ao site por default** (data.py/books.json/página/deploy = lane do site), salvo pedido explícito. Ver memória `padrao-nao-upar-site`.

## Contrato DURO da skill (o validador reprova se faltar)
- `SKILL.md` com **frontmatter**: `name` == slug exato + `description` não-vazia.
- Arquivos de apoio: `SKILL.md` + `glossary.md` + `patterns.md` + `cheatsheet.md`.
- `chapters/` não-vazio; **todo link `](chapters/…md)` do índice RESOLVE** em disco.
- **Linha de procedência** `Base: …` em algum `.md` — a lane **sintetiza, nunca copia** o texto.
- **100% pt-BR**; **sem mojibake** (rodar com `PYTHONIOENCODING=utf-8 python -X utf8`).
- `SKILL.md` no orçamento de tokens (alvo < 4000; teto duro ~6000); conteúdo mais importante primeiro.
- Cada capítulo traz os blocos: Ideia Central · Frameworks/Temas · Conceitos-Chave · Modelos Mentais · Anti-padrões · (Exemplo Trabalhado) · Principais Lições · Conecta Com.
- **Ficção/filosofia:** adaptar os blocos (Temas & Ideias · Personagens & Forças · Estrutura · Símbolos · **Cena-Chave RECONSTRUÍDA**, nunca citada).

## Exceções DECLARADAS (o contrato declara as suas)
- `tjmg-regras-cartorios` — provimento jurídico, **não** vira skill de frameworks.
- `blender-fundamentals/-manual/-noob-to-pro` — fontes de referência do estúdio, catalogadas por **outra** lane (sem skill de livro).
- `futebol-brasileiro` — skill de **arquivo único** (SKILL.md robusto), exceção ao multi-arquivo.

## Bridge (AVISO, não bloqueia — é da lane do site)
- `<slug>_data.py`: `ast` válido, `BOOK`+`CHAPTERS`, capa existe, `ic ⊂ ICONS` do `gerar_livro`.
- `ic` fora do `ICONS` **não quebra** (fallback gracioso → ícone "book"), mas degrada o ícone → reportar.

## Prompt do subagente — 4 blocos (Akita pilar 1)
Toda conversão nasce com **Objetivo · Método · Restrições · Validação** + o conhecimento de domínio do livro (senão o modelo assume o "default mais razoável" e erra):
- **Objetivo:** a skill de `<slug>` em `~/.claude/skills/<slug>/` (âncora do livro em 1 linha).
- **Método:** `book-to-skill` (Full Conversion, text, study); fonte = INTERNET (sem PDF), sintetizar estrutura.
- **Restrições:** pt-BR; NUNCA copiar texto; escrever só os próprios arquivos (paralelo-seguro); não publicar/deploy/books.json.
- **Validação:** todos os links resolvem; `python valida_skill_lane.py` verde para o slug; devolver caminho + nº de capítulos + tipo/tom.

## Execução (Akita pilares 7/8 + loop-agente)
- **Lote:** ondas de subagentes em paralelo (cada um só escreve a própria pasta — isolamento). Akita: paralelizar é para pipeline amortizada (N livros), não default.
- **Rate-limit** é a falha comum em ondas grandes → **retentar** o subagente (idempotente: sobrescreve parciais).
- **Verde = exit code.** Consolidar só com `valida_skill_lane.py`/`testar.py` verdes. Verificação cruzada (juiz ≠ autor, Opus↔Sonnet) via `loop-agente`.
