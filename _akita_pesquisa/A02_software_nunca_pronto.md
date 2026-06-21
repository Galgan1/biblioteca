# A02 — Software Nunca Está 'Pronto' / One-Shot é Mito
Fonte: https://akitaonrails.com/2026/03/01/software-nunca-esta-pronto-4-projetos-a-vida-pos-deploy-e-por-que-one-shot-prompt-e-mito/
Publicado: 01/03/2026

## Práticas concretas (acionáveis)
- **TDD real, em ritmo de produção:** toda feature nova vem com teste novo; todo bug fix vira teste de regressão. Akita adicionou +99 testes em 10 dias num projeto (de 1.323 → 1.422) e cita 4.057 testes somando os 4 projetos como prova de sustentabilidade. Sem teste, "cada merge é roleta russa".
- **Small releases (releases pequenas e frequentes):** publique pedaços pequenos e versionados — 7 releases do Frank Sherlock em 7 dias (v0.1 → v0.7), cada uma com binários compilados, CI verde e release notes. Vantagem prática: "Deu problema? Reverte uma versão".
- **CI/CD automatizado e cross-platform:** configure GitHub Actions para build em Linux (AppImage), macOS (DMG com notarização/signing) e Windows (MSI / UNC paths); publish automático no AUR. Mantenha "CI verde" e "Brakeman zerado" como portão.
- **Refatoração contínua:** centralize config repetida (ex.: `Centralize LLM model config` — tocou 24 arquivos para reduzir a 1 linha de config), extraia helpers compartilhados, delete código morto. Ciclo: benchmark → implementar → refatorar.
- **Versionamento semântico + releases públicos:** adote v0.1.0 → v0.7.0; publique binários em GitHub Releases + AUR. Contribuidores externos (PRs) só aparecem quando há releases versionados e testes — "ninguém manda PR pra protótipo sem testes".
- **Pair programming full-time com o agente:** o humano decide QUAL código escrever; o agente escreve. Aplique "a mesma disciplina que eu usaria com um par humano" — incluindo decisões operacionais (ex.: circuit breaker vs. retry) que nenhum prompt substitui.
- **Trate pós-deploy como desenvolvimento, não manutenção:** continue iterando em produção — features não previstas e 13+ bug fixes reais surgem só depois de processar dados reais e bater em APIs reais.

## Anti-padrões / o que ele critica
- **A fantasia do one-shot prompt:** acreditar que "uma especificação suficientemente detalhada" faz a IA produzir o software perfeito. Ilusão lógica: "se você soubesse de antemão tudo que vai dar errado, você não precisaria da especificação — já teria o software pronto".
- **One-shot + abandono:** "one-shot é pra demo. Iteração é pra produção." Serve só para "vídeo de 10 minutos mostrando 'SaaS pronto'".
- **Declarar "done" e parar:** "software pronto é software morto" — o software que não itera, morre.
- **"6 meses + big bang release"** em vez de small releases — pior e mais arriscado que 7 releases em 7 dias.
- **Velocidade sem direção:** "aceleração sem direção é só entropia mais rápida"; código rápido sem disciplina = "dívida técnica acumula mais rápido".
- **Usar IA como "autocomplete glorificado":** deixa "90% do ganho na mesa".
- **Protótipo sem testes:** o clássico "funciona na minha máquina" — sem testes, não há base para evolução nem para PRs externos.
- **Confiar que a spec prevê tudo:** bugs reais (Gmail corta emails >102KB; Steam API devolve datas em pt abreviado "fev"/"abr"; MIME types .dmg/.deb/.msi fora do seed; tag `<article>` não-semântica em Elementor; paths Windows `\\?\`) só apareceram em produção — "nenhum desses bugs poderia ter sido previsto numa spec".

## Termos/jargão do Akita
- "one-shot prompt" (é "mito")
- "especificação suficientemente detalhada"
- "software bom é o resultado de centenas de micro-decisões" (vs. "macro-decisão tomada antes de escrever a primeira linha")
- "software encontra a realidade" / "software em produção diverge da spec em horas, não em meses"
- "deployment não é fim, é início" / "deploy não é o fim, é o início"
- "Pós-produção é desenvolvimento" (não é "manutenção"); "software vivo itera"
- "software pronto é software morto"
- "aceleração sem direção é só entropia mais rápida"
- "Extreme Programming" (XP) como guarda-chuva: TDD, small releases, pair programming, refactoring contínuo
- "circuit breaker vs. retry" (a decisão operacional que exige experiência)
- "CI verde", "Brakeman zerado", "sem atalho"
- Síntese: "Velocidade = IA. Direção = Experiência. Qualidade = Disciplina de Engenharia."
- Números-bandeira: 692 commits · 4.057 testes · 4 projetos em produção · 125 commits pós-deploy (1 dev + 1 agente)

## Aplicação a um projeto de IA-coding (1-2 linhas)
- Não persiga o "one-shot": entregue em small releases versionadas com CI verde e TDD (teste por feature, regressão por bug), tratando o pós-deploy como desenvolvimento contínuo — o humano decide o quê (circuit breaker vs. retry), o agente faz o como. No projeto Biblioteca isso casa com a constituição Akita: verde = exit code de teste, nunca "a IA achou que está certo".
