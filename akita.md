# O Método Akita: Anti-Vibe Coding

Este documento registra os princípios extraídos da nossa sessão e a implementação da metodologia de Fábio Akita no projeto do orquestrador `vp100`. O foco central é abandonar o amadorismo do "Vibe Coding" em favor de uma Engenharia de Software rigorosa, utilizando a IA não como um gerador mágico, mas como um par de programação supervisionado.

## Pilares do Método no Nosso Projeto

### 1. Anti-Vibe Coding
A recusa formal de usar prompts irresponsáveis de "um clique". O desenvolvimento é inteiramente focado na etapa de planejamento arquitetural:
- Todo problema complexo deve ser quebrado em tarefas atômicas e testáveis.
- É obrigatório **pensar antes de codar** (elaboração de planos de ação).

### 2. O Mural de Testes (TDD Rigoroso)
Inteligências Artificiais são incrivelmente rápidas, o que significa que podem destruir um repositório inteiro em questão de segundos. A única forma de domá-las é usar testes:
- O TDD atua como a espinha dorsal e a "rede de segurança" do projeto.
- A IA só deve avançar ou consolidar uma feature quando o mural de testes estiver 100% "verde".

### 3. Governança via `CLAUDE.md`
O `CLAUDE.md` deixa de ser um mero guia de estilo e passa a ser a **Constituição do Projeto**:
- Nele estão gravados os contratos arquiteturais invioláveis (como o desacoplamento de CLI e JSON via `@with_json`).
- O agente IA deve consultá-lo continuamente para manter a consistência do ecossistema, independente do tamanho da janela de contexto da sessão.

### 4. Loops de Automação e Auditoria (`@loop-agente`)
Garantia de sanidade contínua através da verificação autônoma:
- Engatilhamento de processos agendados que rodam baterias de teste sem intervenção humana.
- Na nossa sessão, realizamos testes a cada 5 minutos usando `venci.bat` para rodar integrações (`status`, `doctor`, `mapa`, `dag`).

### 5. Isolamento Operacional (A Regra `.ouro`)
A aplicação de restrições severas sobre como a IA interage com a máquina hospedeira:
- O agente não tem permissão para rodar comandos soltos no terminal.
- Toda e qualquer execução, seja para testar, compilar ou iniciar servidores, ocorre de forma idempotente e segura dentro do arquivo descartável `venci.bat`.

## Referências e Links

- **Vídeo Base:** [O "Jeito Akita" de Programar com IA](https://www.youtube.com/watch?v=cWY7iBafw7I)
- **Canal Original:** [Akitando - Fábio Akita](https://www.youtube.com/@Akitando)
