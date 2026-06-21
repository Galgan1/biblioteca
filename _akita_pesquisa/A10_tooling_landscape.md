# A10 — Panorama de ferramentas e modelos (agentes × LLMs): o que Akita escolhe e por quê

**Fonte(s):**
- https://akitaonrails.com/2026/01/24/ai-agents-qual-e-o-melhor-opencode-crush-claude-code-gpt-codex-copilot-cursor-windsurf-antigravity/ (agentes/harness)
- https://akitaonrails.com/2026/01/29/vibe-code-qual-llm-%C3%A9-a-melhor-vamos-falar-a-real/ (modelos/LLMs)

**Publicado:** 24 de janeiro de 2026 (agentes) · 29 de janeiro de 2026 (modelos)
**Autor:** Fábio Akita (akitaonrails.com)

> Nota de rastreabilidade (R1): tudo abaixo vem dos dois posts acima. Citações literais entre aspas.
> Nada foi inventado; onde o post não detalha ou não menciona, está marcado como "não na fonte".

---

## Práticas concretas

### 1. Escolher pelo **harness**, não pelo modelo
"Harness", como o próprio nome diz, é um **"arreio"**, uma **"correia de segurança"**: "é tudo que segura a LLM bruta pra torná-la mais efetiva especificamente pra código" (system prompts, tools, formato de patch). O critério-mãe: cada modelo foi **tunado para um harness específico**. "Os modelos GPT Codex foram tunados especificament pra esse harness **proprietário** — só ele se comporta assim." Daí a regra prática: **"quer tirar o máximo proveito de Claude? Use Claude Code / quer tirar o máximo proveito de GPT? Use Codex CLI."**

### 2. Mapa de agentes (analogia "Guerra dos Navegadores")
Ele posiciona cada agente como um navegador da Browser War:
- **Claude Code** = "Internet Explorer 11" (proprietário, dominante, otimizado pro próprio modelo).
- **GPT Codex / Codex CLI** = "Netscape".
- **Cursor, Windsurf, Copilot** = "os Operas" (plugins/IDE proprietários sobre harness alheio).
- **OpenCode / Crush** = "Chromium em 2006" (open source, agnóstico de modelo, a aposta de futuro).
- Antigravity, Gemini CLI, Aider: **não mencionados** nominalmente nesses dois posts.

### 3. Preferência declarada: **Crush**, Claude Code pontual
TL;DR dele: **"por preferência pessoal, eu vou continuar usando Crush. Pontualmente vou usar Claude Code."** Motivo concreto, não ideológico: **"A performance de Claude via Crush está muito boa pra mim, por isso vou continuar no Crush"** — ou seja, roda Claude (o modelo) dentro de um harness open source/agnóstico (o agente). Critério de fundo: evitar lock-in — agnósticos "ainda não tem suporte ao harness proprietário da OpenAI", mas valem a pena pra não "ficar fechado em ferramenta proprietária".

### 4. Método de comparação de modelos: **teste real, não benchmark**
O critério não é context window nem leaderboard — é rodar em código real. Ele pediu "uma análise **EXTENSIVA** de segurança, otimização, testes" ao Claude Code e depois **a mesma análise EXTENSIVA** a cada outro modelo, em cima do que o anterior corrigiu, comparando o que cada um **pega** ou **deixa passar**. Custo total do experimento: **"no total só uns USD 3"** (critério de custo: vibe code de qualidade é barato).

### 5. Leitura por modelo (qual e por quê)
- **Claude Opus 4.5** — default seguro: **"na dúvida, use Claude Code. É o melhor balanceado entre velocidade e qualidade."** Defeito: **"Opus tende a ser proativo demais em aspectos que costumam ser desnecessários"** (overengineering) — "aquele estagiário chato que lê muito blog post".
- **GPT 5.2 Codex** — **"mais 'honesto' do que o Opus"**: "vai mais direto ao ponto e segue mais de perto exatamente o que eu pedi." Pegou config de timeout que o Opus ignorou.
- **Gemini 3 Pro Preview** — também **"um pouco mais 'honesto' e direto ao ponto"**; achado único: deadlock no shutdown do servidor.
- **Kimi 2.5** — "mais lento que Opus ou GPT, mas melhor que GLM"; mesmo assim "continuou achando itens que não sei como o Opus deixou passar".
- **GLM** — pior do trio aberto comparado (Kimi > GLM).
- **MiniMax v2.1** — pegou **"besteiras de boas práticas de Go que todo mundo deixou passar"**.

### 6. Cuidar do custo de contexto das Skills
Anthropic Skills custam tokens: cada skill concatena metadados no system prompt (estimativa dele: **"80 a 250 tokens por skill"**). Conselho: **"Skills automáticas são facas de dois gumes: não instale tudo que ver pela frente."** As skills oficiais da Anthropic são open source mas "não tem nenhuma skill muito interessante".

---

## Anti-padrões

- **Perguntar "qual é a melhor LLM?" esperando UMA resposta** — pra ele a resposta é **"NENHUMA!"**: "A única coisa que existe são seus requerimentos."
- **Escolher agente por opinião/hype** em vez de teste técnico próprio: "você deve escolher baseado nas suas próprias necessidades e testes." (Conclusão central: **"DEPENDE"**.)
- **Tratar o agnóstico como equivalente perfeito do proprietário** — sem o harness proprietário (ex.: `apply_patch` da OpenAI), você não extrai 100% daquele modelo.
- **Confiar cego no modelo "proativo"** — overengineering é frequente ("É overengineering, mas tudo bem também"; "é um storage hiper pequeno, kilobytes"). Precisa de revisão.
- **Achar IA infalível/mágica** — "IAs são máquinas de probabilidade, cuspidores de texto glorificados, sem nenhuma inteligência"; "não é mágica e nem é infalível, muito longe disso".
- **Instalar toda skill que aparece** — estoura o orçamento de tokens do system prompt.

---

## Termos / jargões exatos

- **Harness** — o "arreio"/"correia de segurança"; tudo que segura a LLM bruta pra código. Critério nº1 de escolha de agente.
- **Harness proprietário** — o da OpenAI (Codex), pra o qual os modelos GPT foram "tunados"; agentes open source "ainda não tem suporte" a ele.
- **apply_patch** — formato de patch proprietário da OpenAI (sem números de linha, usa linhas de contexto + "delimitadores claros pra código velho vs novo"); o Codex prefere a `sed`/diff comum.
- **Agnóstico (de modelo)** — Crush/OpenCode rodam qualquer LLM; o oposto de proprietário (Claude Code/Codex CLI).
- **"Guerra de Agentes" / "bolha de IAs"** — o momento atual; espelha as **Browser Wars** (IE11=Claude Code, Netscape=Codex, Operas=Cursor/Windsurf/Copilot, Chromium 2006=OpenCode/Crush).
- **Vibe code** — programar conversando com a LLM; o tema do 2º post.
- **Overengineering / "proativo demais"** — defeito recorrente do Opus.
- **"Honesto" / "direto ao ponto"** — elogio dele a GPT 5.2 Codex e Gemini 3 Pro (segue o pedido sem tangentes).
- **"Máquinas de probabilidade" / "cuspidores de texto glorificados"** — o que LLM é.
- **"Estagiários muito motivados"** — metáfora do papel da LLM (exige supervisão).
- **"A qualidade do app é diretamente proporcional à sua senioridade!"** — a tese central do 2º post.
- **Skills automáticas = "facas de dois gumes"** — custam "80 a 250 tokens por skill".
- **"DEPENDE" / "NENHUMA!"** — as respostas dele a "qual o melhor agente / a melhor LLM".
- Modelos citados: **Opus 4.5, GPT 5.2 Codex, Gemini 3 Pro Preview, Kimi 2.5, GLM, MiniMax v2.1** (Qwen/DeepSeek: não na fonte).

---

## Aplicação (1–2 linhas)
Confirma a doutrina do projeto: separar **harness** (agente) de **modelo** e escolher por teste real, não hype — rodar Claude (modelo) dentro do nosso fluxo é legítimo, e a verificação cross-model (Opus "proativo demais" ↔ GPT/Gemini "mais honesto") do `/loop-agente` é exatamente o método dele de pegar o que um modelo deixa passar. Tratar Skills como custo de token ("não instale tudo que ver").
