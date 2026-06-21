# A12 — Postura / Filosofia

Fontes:
- [PRIMÁRIO] https://akitaonrails.com/2026/02/24/rant-o-akita-abriu-as-pernas-pra-ia/ (rant do próprio Akita)
- [PRIMÁRIO] https://akitaonrails.com/2026/02/08/rant-ia-acabou-com-programadores/ (rant do próprio Akita)
- [SECUNDÁRIO] https://www.youtube.com/watch?v=G_8uG1Ot0yo — "A farsa acabou: Akita, Montano e Deyvin se assumiram vibe coders" (Mano Deyvin / MANO RAGE SHOW, ~2h27, ar em 02/03/2026). Comentário SOBRE o Akita, em tom satírico/irônico. Sem transcrição obtida via WebFetch; conteúdo abaixo reconstruído de resumos de busca (Apple Podcasts/Spotify/YouTube) — tratar como interpretação de terceiros, NÃO como fala do Akita.

> Nota de método: as citações entre aspas nas seções 1–3 são falas literais do Akita extraídas dos dois rants primários. A seção do vídeo é claramente identificada como voz de terceiros (sátira), separada da posição real do autor.

## A posição dele (vibe coder? anti-vibe? o que ele realmente defende)

- **Ele NÃO se assume "vibe coder" — rejeita o rótulo.** Para Akita, os nomes da moda são todos a mesma coisa e mascaram o que importa (programar com disciplina). O termo, pra ele, é marketing vazio.
- **A posição real: "Engenharia de Software aplicada à IA"** (que ele apelidou de "Agile Vibe Code"). Não é deixar a IA decidir; é o sênior dirigindo a IA sob processo de engenharia. Defende que o ganho **depende de engenharia, benchmarks e decisões de arquitetura** — não da IA "sozinha".
- **Distingue dois caminhos opostos:**
  - *Errado* (o que ele critica, e que a sátira do vídeo confunde com "vibe coding"): largar a IA fazer o código, não saber revisar/criticar, subir pra produção sem entender os riscos (cita o app Tea como exemplo de fiasco).
  - *Certo*: PDCA rigoroso — "uma tentativa, uma checagem, um ajuste, repita"; nada vai pra produção sem revisão humana; verificação sistemática (testes, CI, security scanning, small releases).
- **Visão histórica, não nostálgica nem apocalíptica:** LLM é só a próxima forma — mais eficiente — de "informar instruções à máquina", na mesma linha evolutiva de entrar bit a bit na memória → SSD NVMe. Usar a ferramenta com rigor profissional, sem glorificar nem odiar.
- **Sobre "IA acabou com programadores":** *não* acabou com os bons; *vai sim* extinguir a categoria de baixo valor agregado (volume sem profundidade) — e ele acha isso bom. Quem só copiava código "já era ineficaz antes".
- **[SECUNDÁRIO / sátira do vídeo]:** o episódio do Mano Deyvin brinca que o Akita — antes "fiscal do código raiz" e "pai do 'não terceirize seu cérebro'" — teria "se assumido vibe coder" ao "abrir as pernas pra IA". É *zoeira* sobre a (aparente) virada dele; **contradiz a posição que o próprio Akita defende nos rants** (ele explicitamente nega ser vibe coder e ataca o vibe coding sem disciplina). Útil só como termômetro da repercussão na comunidade dev BR.

## O papel do programador SÊNIOR na era da IA (segundo Akita)

- **Tomador de decisão e validador:** o sênior decide o que a IA ainda não consegue decidir (arquitetura, hipóteses, trade-offs); a IA assume o mundano (CRUD, CSS, setup de ambiente).
- **Três responsabilidades críticas:** (1) **especificar** — "precisa de um sênior pra especificar"; (2) **revisar** — "precisa de um sênior pra revisar"; (3) **mentorar júniors** ("a segunda tarefa mais importante de qualquer sênior").
- **Pré-requisito é conhecimento profundo:** só sabe usar IA do jeito certo quem "estudou e tem experiência". Não há atalho de bootcamp.
- **Auto-renovação obrigatória:** o sênior tem de ser capaz de formar o próprio substituto; quem não consegue vira passivo, não ativo.
- **Lei da adaptação:** quem não se adapta é extinto — é ciclo econômico/evolutivo, não fim do mundo.

## Frases/citações marcantes

Do Akita (PRIMÁRIO):
- "Não importa se quer chamar de 'Vibe Code', 'Agentic Engineering', 'IA Assisted Programming', é tudo bullshit." (rant 24/02)
- "eu chamei de 'Agile Vibe Code', mas é basicamente 'Engenharia de Software aplicada à IA' e adivinhe: precisa ter estudado e experiência pra saber" (rant 24/02)
- "deixam a IA fazer o código, não sabem revisar nem criticar esse código, sobem pra produção e deixam usuários usarem, sem saber dos riscos" (rant 24/02)
- "Nenhum código gerado por IA vai ser automaticamente perfeito pra ser colocado em produção sem nenhum tipo de revisão ou intervenção humana" (rant 08/02)
- "Tudo é feito PASSO A PASSO. Uma tentativa, uma checagem, um ajuste, repita" (rant 08/02)
- "IAs nunca vão substituir programadores COMO EU - EU nunca vou ser substituído" (rant 08/02)
- "Programadores como eu sempre vão existir. O que sempre deixa de existir são profissões que só têm volume, mas baixo valor agregado" (rant 08/02)
- "Sim, eu também acredito que uma categoria inteira, que se autointitulava 'engenheiro de software', vai deixar de existir por causa das IAs" (rant 08/02)
- "Não existe virar 'engenheiro' em um bootcamp de 1 mês. Isso era bullshit" (rant 08/02)
- "Sênior incapaz de criar seu próprio substituto não é um sênior, é uma liability" (rant 08/02)
- "Precisa de um sênior pra especificar" / "Precisa de um sênior pra revisar" / "A segunda tarefa mais importante de qualquer sênior é mentorar júniors" (rant 08/02)
- "É tudo uma questão de adaptação: quem não se adapta é extinto. Essa é a lei" (rant 08/02)
- "[LLMs] são, de fato, a forma mais eficiente [de informar instruções à máquina]" (rant 24/02)

De terceiros (SECUNDÁRIO — sátira, NÃO é fala do Akita):
- Título/tese do vídeo: "A farsa acabou: Akita, Montano e Deyvin se assumiram vibe coders" — pilhéria de que o "pai do 'não terceirize seu cérebro'" teria virado vibe coder. Contradiz o que o Akita realmente afirma.

## Aplicação (1-2 linhas)
- Confirma a tese da skill `akita`/CLAUDE.md: IA pesada SÓ com engenharia (TDD/CI/small releases, revisão humana, PDCA), sênior dirige e especifica — o "anti-vibe coding" é exatamente a doutrina do projeto. Usar como respaldo direto da Constituição Akita.
