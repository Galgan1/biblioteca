# A11 — Linhagem externa (Karpathy)

Fontes:
- Tweet original (fonte primária): https://x.com/karpathy/status/1886192184808149383 (2 fev 2025) — bloqueado a robôs (HTTP 402), porém o texto integral foi capturado via busca e confirmado por terceiro confiável abaixo.
- Simon Willison, "Not all AI-assisted programming is vibe coding (but vibe coding rocks)" (19 mar 2025): https://simonwillison.net/2025/Mar/19/vibe-coding/ — reproduz o tweet na íntegra e faz a distinção ingênuo × disciplinado.
- Karpathy, gist "LLM Wiki" (fonte primária do padrão de memória): https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
  - RESSALVA DE PROVENIÊNCIA: a página renderiza como gist do próprio Karpathy e o padrão é amplamente atribuído a ele na imprensa técnica, mas NÃO consegui confirmar o dono via API do GitHub (a API devolveu "Server Error" / rate-limit no momento da coleta). Tratar a autoria do gist como "muito provável, não 100% verificada por API".

## Definição original de "vibe coding" (Karpathy) — citação exata

- Tweet (2 de fevereiro de 2025), texto verbatim em inglês:
  > "There's a new kind of coding I call 'vibe coding', where you fully give in to the vibes, embrace exponentials, and forget that the code even exists. It's possible because the LLMs (e.g. Cursor Composer w Sonnet) are getting too good. Also I just talk to Composer with SuperWhisper..."

- Descrição prática da experiência, no mesmo tweet (verbatim):
  > "I just see stuff, say stuff, run stuff, and copy-paste stuff, and it mostly works."

- Detalhes que ele dá do método (parafraseado do tweet, reportado por Willison): pedir mudanças por voz tipo "decrease the padding on the sidebar by half" sem localizá-las no código; **aceitar tudo ("Accept All") sem ler os diffs**; colar mensagens de erro de volta sem comentário; deixar o código crescer além da própria compreensão. Ele mesmo fecha: **"It's not too bad for throwaway weekend projects."** (ou seja, o próprio Karpathy circunscreve o vibe coding a projetos descartáveis).

## O que isso significa (ingênuo) vs. o que o Akita faz (disciplinado)

- **Vibe coding ingênuo (Karpathy):** entregar-se à intuição ("give in to the vibes"), **"esquecer que o código existe"**, aceitar diffs sem revisar, não entender o que foi escrito. Serve para protótipo de fim de semana descartável — não para produção.
- **A fronteira (Willison, fonte primária da distinção):**
  > "If an LLM wrote the code for you, and you then reviewed it, tested it thoroughly and made sure you could explain how it works to someone else — that's not vibe coding, it's software development."
- **Anti-vibe / vibe disciplinado (Akita):** mantém a IA escrevendo o código, mas **devolve ao humano o controle que o vibe coding abandona** — exatamente os passos que Karpathy pula: planejar antes de codar, **revisar todo diff**, **TDD real (verde = exit code de teste, não "a IA achou que está certo")**, refatoração contínua, CI obrigatória, isolamento de execução. O humano decide o *quê*; a IA executa o *como*; nada se consolida sem teste verde. É o oposto literal de "forget that the code even exists".

## Karpathy LLM Wiki / memória de agentes — ideia central

- Em vez de RAG (consultar os documentos crus a cada query), o LLM **constrói e mantém incrementalmente um wiki persistente** — coleção estruturada e interligada de arquivos markdown.
- Fluxo: fontes cruas/imutáveis ficam numa pasta `raw/`; o LLM lê cada fonte nova e a **integra** num diretório `wiki/` (extrai o essencial, atualiza páginas de entidades, revisa sínteses, anota contradições); um arquivo de esquema (estilo `CLAUDE.md`) governa estrutura e regras de manutenção.
- Tese central (verbatim do gist): o conhecimento é **"compiled once and then kept current, not re-derived on every query"** — o wiki é um **"compounding artifact"** (artefato que se acumula: as referências cruzadas já estão lá, a síntese já reflete tudo que foi lido).
- É, na prática, uma **camada de memória para agentes**: responde à pergunta "como o agente lembra entre sessões/threads, ao longo de meses?" — uma memória persistente, estruturada e auto-mantida que o agente lê e escreve. (Espelha o próprio `CLAUDE.md`/MEMORY.md deste projeto.)

## Aplicação a um projeto de IA-coding (1-2 linhas)

- Adote a IA como autora do código (produtividade do "vibe"), mas blinde com o cinturão do Akita — plano + TDD verde + revisão de diff + CI — para nunca "esquecer que o código existe"; e use um LLM Wiki (ex.: `CLAUDE.md` + MEMORY.md como esquema/memória) para que cada lane/sessão herde o conhecimento já compilado em vez de re-derivá-lo a cada vez.
