# A04 — O Mínimo de boas práticas num projeto open-source com LLM (Akita)

**Fonte:** https://akitaonrails.com/2026/05/30/boas-praticas-projetos-codigo-aberto-llm-o-minimo/
**Publicado:** 2026-05-30

> Recorte: o que Akita exige como "o mínimo" para que um projeto open-source feito com IA esteja *pronto pra publicar*. Tese central — "nenhum projeto de código aberto está pronto pra ser publicado sem três coisas". Gerar código com LLM é a parte fácil; **"o que vem depois é o desafio"**.

---

## Práticas concretas

Cada item é um requisito. Termo/jargão exato entre `crases` ou aspas.

### Pilar 1 — "Superfície de instalação"
1. **Instalar e testar com o mínimo de atrito** — "Um comando, de preferência." Múltiplos caminhos de instalação (ex.: 5 caminhos no projeto `ai-jail`).
2. **Gerenciadores de pacote** como alvo de empacotamento: `Homebrew`, `AUR` (variantes `-bin` e source), `cargo`, `mise`, download direto.
3. **Princípio "compile uma vez, reempacote várias"** — um binário único, várias embalagens (Tarball `.tar.gz`, `AppImage`, `RPM`/`DEB` via `nfpm`).
4. **Builds por plataforma/arquitetura**: Linux x86_64/ARM, macOS (`aarch64-apple-darwin` e `x86_64-apple-darwin`), Windows (`x86_64-pc-windows-msvc`).
5. **Assinatura e notarização no macOS**: `codesign` + notarização via `xcrun notarytool`.
6. **Verificação de integridade**: `SHA256` checksums em cada artefato.

### Pilar 2 — "CI/CD e testes automatizados" (gate obrigatório)
7. **CI em `GitHub Actions` com matrix de builds** por plataforma/arquitetura (teste nativo em x86; ARM por cross-compile sem teste).
8. **Lint + format + testes + auditoria como gate**: em Rust — `cargo fmt --check`, `cargo clippy -D warnings`, `cargo test`, `cargo audit`; em Rails — `rubocop`, `brakeman`, `bundler-audit` + suíte `Minitest`.
9. **Scanner de segurança obrigatório no CI** (`brakeman`, `bundler-audit`, `cargo audit`) — segurança é gate, não opcional.
10. **Cobertura de testes adequada e auditada** (evidências citadas: `FrankMD` 1800+ testes; `Frank Sherlock` ~300 Rust + 300 frontend).
11. **Release disparada por tag semver** (`v*.*.*`).
12. **Cache de compilação no CI** (ex.: `Swatinem/rust-cache`).
13. **Publicação idempotente** (ex.: `cargo publish` tolerando versão já existente).

### Pilar 3 — "Documentação e comunicação"
14. **`README` focado no caso de uso / problema resolvido**, não na stack — "ninguém liga pra sua stack".
15. **`docs/` com decisões arquiteturais** "pra quem vai contribuir".
16. **`CHANGELOG.md` no formato `Keep a Changelog`** (seção por versão); release notes do GitHub extraídas dele automaticamente (o que mudou + instalação + checksums SHA256).
17. **`config/deploy.env.example` versionado** (valores reais no `.gitignore`).

### Deploy + integração com agentes
18. **`bin/deploy` único e idempotente** (build → push → SSH remoto); Docker multi-estágio (usuário não-root); `docker-compose.production.yml` em registry privado; `restart: always`.
19. **Padronização entre projetos = automação confiável** — estrutura idêntica permite ordens diretas ao agente ("roda o deploy", "solta uma release") sem o agente "precisar adivinhar nada".
20. **Code review com LLM, decisão humana**: prompt para PR — *"não confie na descrição do autor. audita o código a fundo"*; prompt pós-vários-PRs — auditar código morto, duplicação, magic numbers, cobertura, clean code, docs. **LLM audita/sugere; humano aprova/nega/merge.**

---

## Anti-padrões

- **"Vibe coding"** — achar que gerar o código resolve; "o que vem depois é o desafio".
- **Negligenciar a "superfície de instalação"** — perde-se a maioria dos usuários potenciais por atrito de instalação.
- **Recompilar em cada formato** — viola "compile uma vez, reempacote várias".
- **README focado em stack/tecnologia** — "ninguém liga pra sua stack"; "solução em busca de um problema".
- **Deploy em "três estágios com aprovação manual"** — overengineering desnecessário (prefira `bin/deploy` único idempotente).
- **Omitir o changelog** — deixa o usuário sem contexto de atualização.

---

## Termos

`superfície de instalação` · `compile uma vez, reempacote várias` · `GitHub Actions matrix` · `cargo fmt --check` · `cargo clippy -D warnings` · `cargo test` · `cargo audit` · `rubocop` · `brakeman` · `bundler-audit` · `Minitest` · semver `v*.*.*` · `Swatinem/rust-cache` · publicação idempotente · `Keep a Changelog` / `CHANGELOG.md` · `SHA256` checksums · `codesign` / `xcrun notarytool` · `nfpm` · `AppImage` · `bin/deploy` idempotente · `docker-compose.production.yml` / `restart: always` · `deploy.env.example` · "vibe coding" · code review com LLM (humano decide).

> **NÃO mencionados no texto** (verificado em 2ª passada, para não contaminar a constituição): `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.cursorrules`, `conventional commits`, `pre-commit hooks`, `.editorconfig`, `LICENSE`/`CONTRIBUTING.md`/`CODE_OF_CONDUCT`/templates de issue-PR. O artigo trata "docs de governança" só como `docs/` genérico — a doutrina AGENTS.md/CLAUDE.md vem de OUTROS textos do Akita, não deste.

---

## Aplicação (1-2 linhas)

Antes de chamar um projeto da Biblioteca de "pronto", exigir o mínimo: CI verde com lint+format+testes+scanner de segurança como gate, release por tag semver com checksums, `CHANGELOG.md` (Keep a Changelog), `README` por caso-de-uso e `bin/deploy` idempotente. Reforça o pilar 3 (qualidade) da Constituição e o anti-vibe-coding: LLM audita, humano decide o merge.
