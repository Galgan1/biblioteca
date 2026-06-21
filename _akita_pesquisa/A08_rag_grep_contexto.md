# A08 — Como o agente navega o código: contexto longo + grep, não RAG

**Fonte:** https://akitaonrails.com/2026/04/06/rag-esta-morto-contexto-longo/
**Publicado:** 6 de abril de 2026 (Fábio Akita)

> Tese central: em 2026 a equação de 2023 se inverteu. O **long context** (janela de contexto generosa) + **busca lexical** (grep) + **compactação inteligente** substituem o pipeline RAG/vector DB clássico para fazer o agente navegar código e conhecimento. "Pra que cargas d'água eu preciso montar uma stack vector pra resolver problema que cabe na janela do modelo?"

---

## Práticas concretas

- **"Lazy retrieval"** — a arquitetura que Akita defende (título de seção: *"Lazy retrieval: a receita que eu defendo"*). Fluxo em 3 tempos:
  1. **Filtro lexical rápido** — `grep`/`ripgrep`/BM25 para achar candidatos.
  2. **Carregar generosamente** — arquivo inteiro ou "janela grande em volta" do match (não chunk arbitrário).
  3. **Deixa o LLM fazer a parte fina** — "Passa a pergunta original, manda o modelo encontrar o que importa, descartar o resto, e responder com citações."
- **Busca lexical em vez de vetor:** "um `grep` bem feito mais uma janela de contexto generosa". "E ripgrep voa em cima de milhões de linhas." Alternativas citadas: BM25 com Tantivy/SQLite FTS5, `LIKE` em Postgres, regex simples.
- **Carregar sob demanda, não pré-indexar:** os fatos de verdade ficam em **"topic files" buscados sob demanda quando o agente precisa** — não num índice vetorial mantido de antemão. "Arquivo mudou? Próxima query já vê" (frescor sem re-embedding).
- **MEMORY.md como índice de ponteiros, não dados:** "Um `MEMORY.md` que fica permanentemente carregado no contexto" — disciplinado (~150 chars/linha, ~200 linhas, ~25 KB). Funciona como índice; os fatos reais ficam nos topic files. "Sem embedding. Sem Pinecone. Disciplina de escrita (topic file primeiro, índice depois) e busca lexical, só isso."
- **Compactação inteligente** (5 estratégias de compactação de contexto): `microcompact` (limpa resultados de tool antigos por tempo), `context collapse` (resume trechos longos da conversa), `autocompact` (dispara quando o contexto chega perto do limite).
- **Prova de autoridade:** o `autoDream` da Anthropic (consolidação de memória do agente) "é um subagente forkado, com bash read-only no projeto" que faz grep em logs de texto (JSONL no disco) — "os transcripts brutos das sessões anteriores nunca são relidos inteiros, só pesquisados com grep atrás de identificador específico". Os agentes de ponta "tão indo na direção de contexto generoso, busca lexical e compactação inteligente, não na direção de pipeline RAG clássico".

## Anti-padrões

- **RAG/vector DB clássico por padrão** — montar stack vetorial (Pinecone, Weaviate, pgvector) para problema que cabe na janela; overhead de re-embedding, índice, monitoramento e fila.
- **Chunking** — "Chunking é o segundo [pecado], e é um desastre disfarçado": corta definições, tabelas e contexto ao meio.
- **Cosine similarity / "falsos vizinhos"** — "Cosine similarity premia similaridade tópica, não relevância"; "Falsos vizinhos é o primeiro [pecado]". Falha opaca: o vector DB devolve um chunk plausível e errado.
- **Dump cego de contexto** — "Dump de 200k de contexto é mais opaco em auditoria"; carregar tudo sem filtro lexical antes não é o caminho (daí o "lazy").
- **Excesso de framework** — "Stack menor, infraestrutura mais simples, contexto generoso, e muito menos LangChain."

## Termos / jargão exato

`Lazy retrieval` · `grep` · `ripgrep` · `BM25` (benchmarks **BEIR**) · filtro **lexical** · **chunking** · **cosine similarity** · **falsos vizinhos** · `MEMORY.md` · **topic file** · **compactação** de contexto · `microcompact` · `context collapse` · `autocompact` · **subagente forkado** (bash read-only) · `autoDream` (Anthropic) · janela de contexto / **janela do modelo** (200k–1M) · Tantivy / SQLite FTS5.

## Aplicação (1-2 linhas)

Para navegar este repo, o agente deve fazer `grep`/`ripgrep` para localizar e então ler o arquivo inteiro (ou janela larga) — em vez de embeddings/vector DB — e manter um `MEMORY.md` como índice de ponteiros para topic files buscados sob demanda. É exatamente o padrão já adotado aqui (MEMORY.md + skills carregadas just-in-time).
