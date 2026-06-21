# A01 — Clean Code para Agentes de IA
Fonte: https://akitaonrails.com/2026/04/20/clean-code-para-agentes-de-ia/
Publicado: 20 de abril de 2026

## Práticas concretas (acionáveis)
- **Funções pequenas e arquivos pequenos** — função 4-20 linhas (Uncle Bob); arquivo idealmente 200-300 linhas, máximo 500; cada unidade cabe numa única tool call sem truncamento ["Uma função pequena cabe numa única tool call sem truncamento"]
- **Single Responsibility Principle (SRP)** — um módulo faz uma coisa, tem uma razão para mudar; deixa o agente isolar a unidade sem carregar o sistema inteiro e torna o grep por responsabilidade previsível ["Single Responsibility Principle (SRP)"]
- **Nomes significativos e únicos** — nomes "distintivos e pesquisáveis" são a propriedade mais importante; teste prático: o grep deve retornar poucas ocorrências relevantes; preferir `UserRegistrationValidator` a `Manager`/`Service` ["Nome genérico (`data`, `process`, `handler`) retorna cinquenta matches"]
- **Comentários com contexto e proveniência (POR QUÊ, não O QUE)** — o agente LÊ e VALORIZA comentários (inversão vs. Clean Code original); incluir motivação de bug de produção, constraint de negócio, workaround upstream, referência a issue/commit SHA; docstring obrigatória (intenção + 1 exemplo de uso) ["Comentário vira contexto de primeira classe"]
- **Não remover os comentários que o próprio agente escreveu** — preservar no refactor, pois carregam a intenção para a próxima iteração ["Keep your own comments. Don't strip on refactor."]
- **Tipos explícitos** — type hints em Python, TypeScript (não JS puro), RBS em Ruby; a assinatura vira "gabarito imediato" e evita inferência custosa a partir do uso ["Tipos Explícitos"]
- **DRY (Don't Repeat Yourself)** — duplicação é PIOR para agente que para humano: ele atualiza uma cópia e esquece as outras; a janela de atenção "não tem gravidade natural para lembrar das réplicas" ["DRY (Don't Repeat Yourself)"]
- **Testes que o agente consegue rodar sozinho** — comando único em README/`CLAUDE.md`/`Makefile`/`package.json`; output parseável; sem seed manual, config ausente ou credencial secreta; TDD "virou obrigação técnica, não filosofia"; cobertura: ratio teste/código >1:1 em módulos críticos, mínimo 80% (95%+ em lógica de negócio) ["Teste precisa ser executável pelo agente sem setup humano"]
- **Estrutura de diretório previsível** — convenções fortes de framework (Rails, Django, Next.js, Laravel) deixam o agente antecipar paths sem listar diretório; ex.: `src/controllers/users.rb` implica `src/models/user.rb`
- **Dependency Injection e testabilidade** — dependências injetadas (não hardcoded) para trocar `EmailSender` por `FakeEmailSender`; config isolada em constante única, não replicada em 24 arquivos ["Dependency Injection e Testabilidade"]
- **Evitar aninhamento profundo** — um nível de abstração por função; guard clauses, early returns, pattern matching; máximo 2 níveis de indentação (cada indentação custa atenção do modelo)
- **Erro com contexto** — incluir o valor ofendido e a forma esperada, ex.: `ValueError(f"invalid input: {repr(x)}, esperado string não-vazia")`; o agente usa a mensagem da exceção para debugar ["`raise ValueError('invalid input')` não ajuda o agente"]
- **Formatação via formatador default** — `cargo fmt`, `gofmt`, `prettier`, `black`, `rubocop -A` em pre-commit/editor; qualquer estilo consistente serve, evita discutir tabs vs. espaços
- **Arquivos de meta-documentação** — `CLAUDE.md`, `AGENTS.md`, `.cursor/rules`, `.github/copilot-instructions.md`: lidos antes de qualquer tool call; formato curto, imperativo, orientado a ação, bulletpoints (sem prosa filosófica)
- **README com arquitetura de alto nível** — diagrama simples em ASCII ou Mermaid encurta o caminho do agente para entender o "shape" do projeto (Uncle Bob pouco se importava; para agente é crítico)
- **Logging estruturado** — JSON com campos nomeados (parseável trivialmente) para debug/observabilidade; texto plano só para output ao usuário
- **Comandos de observabilidade acessíveis** — quanto mais comandos previsíveis de validação melhor: `pnpm test`, `make lint`, `cargo check`, `python -m mypy` ["`pnpm test`, `make lint`, `cargo check`, `python -m mypy`"]
- **Scripts de setup idempotentes** — `bin/setup` / `scripts/bootstrap.sh` que rodam em máquina limpa; onboarding só na "cabeça humana" exclui o agente do jogo
- **Instruir o agente explicitamente** — nenhum LLM faz nada disso por default; é preciso ESCREVER as regras em `CLAUDE.md`/`AGENTS.md`/`.cursor/rules` ["Nenhum LLM faz essas coisas por default"]

## Anti-padrões / o que ele critica
- **Classe de 800 linhas com múltiplas responsabilidades** — não cabe numa tool call, paginação fragmenta o raciocínio do modelo
- **Nomes genéricos** (`data`, `process`, `handler`, `Manager`, `Service`) — grep retorna ~50 matches e força o agente a ler vários arquivos irrelevantes
- **Comentários óbvios** — ex.: `// increment i by 1` acima de `i++` desperdiça tokens; o modelo sabe ler código ["NÃO Escrever Comentários Óbvios"]
- **Remover comentários do agente durante refactor** — apaga a intenção da iteração anterior
- **Duplicação de código (violar DRY)** — o agente atualiza uma cópia e esquece as réplicas
- **JS puro / tipos implícitos** — obriga inferência custosa de tipo a partir do uso
- **Mensagens de erro vazias** — `raise ValueError('invalid input')` não dá ao agente o que precisa para debugar
- **Logging em texto livre / `printf`** — força parsing heurístico em vez de leitura trivial de JSON
- **Setup em 10 passos manuais / onboarding só na cabeça humana** — o agente não consegue rodar os testes
- **Código sem teste** — agente entrega "código plausível que silenciosamente quebra algo"
- **Aninhamento profundo** — cada indentação custa atenção do modelo para rastrear estado
- **Projeto sem convenção de estrutura** — força exploração custosa com `find`
- **Tratar Clean Code / XP / TDD / SOLID como "moda" descartável** — quem desprezou nos anos 2010 "tá apanhando pra ensinar agente a não cometer erros mapeados 25 anos atrás"

## Termos/jargão do Akita
- "Clean Code para agentes de IA" — recontextualização do Clean Code do Uncle Bob para o modo de trabalho de LLMs
- "Comentário vira contexto de primeira classe" — inversão central: o agente valoriza comentários (ao contrário do humano que os ignora)
- "Truncamento de arquivo" / "tool call" — leitura limitada (Claude Code: 2000 linhas por chamada); função pequena cabe numa tool call sem truncamento
- "Grep é mais barato que read" — o agente prefere busca lexical a carregar arquivos inteiros (por isso nomes pesquisáveis importam)
- "Tool calls custam token" / "Latência importa" — cada Read/Edit/Bash gasta tokens e adiciona segundos ao loop
- "Atenção degrada com contexto" — a qualidade cai antes do limite declarado de contexto
- "POR QUÊ, não O QUE" — critério para o que escrever em comentários/docstrings
- "Nome que retorna <5 grep hits" — métrica prática de nome bom ("Prefer names that return <5 grep hits")
- "Gabarito imediato" — papel da assinatura tipada/explícita para o agente
- "Shape do projeto" — o que o README/diagrama deve comunicar de cara
- "Código limpo nunca foi moda. Virou infraestrutura." — tese final
- "Fundamentos viraram infraestrutura operacional" — SRP, DI, funções pequenas e testes abundantes hoje são diferencial técnico, não estética

## Aplicação a um projeto de IA-coding (1-2 linhas)
- Materializar essas regras num `CLAUDE.md` curto e imperativo (template do Akita: funções 4-20 linhas, arquivos <500, nomes com <5 grep hits, tipos explícitos, DRY, early returns ≤2 níveis, exceções com valor+forma esperada, "keep your own comments", testes por comando único com fakes nomeados, DI por construtor).
- Garantir o "ponto único idempotente" de validação (um comando roda lint+tipos+testes com output parseável) para que o agente feche o loop sozinho — alinhado com o pilar Akita de "verde = exit code de teste".
