# Auditoria de UX Writing: Impeccable Clarify

## Visão Geral
Esta auditoria avalia a clareza e eficácia do texto nas interfaces do projeto Biblioteca, aplicando as heurísticas do framework Clarify (`impeccable/reference/clarify.md`). O objetivo é garantir que a cópia seja clara, específica, humana e oriente os usuários de forma eficiente.

---

## 1. Estados Vazios (Empty States)
**Onde:** `script.js` (Linha 18)
**Texto Atual:** `"A biblioteca está vazia no momento."`
**Problema:** A mensagem funciona como um "beco sem saída" (dead-end). Ela apenas constata o fato, mas não explica o que o usuário deve fazer para povoar a biblioteca, perdendo uma oportunidade de onboarding.
**Recomendação:** `"Sua biblioteca está vazia. Adicione resumos ao arquivo books.json para começar."`
**Princípio Clarify:** *Explain why it's empty. Show next action clearly. Make it welcoming, not dead-end.*

## 2. Mensagens de Erro (Error Messages)
**Onde:** `script.js` (Linha 47)
**Texto Atual:** `"Erro ao carregar a biblioteca. Certifique-se de estar rodando em um servidor local."`
**Problema:** O uso da palavra "Erro" em conjunção com um comando imperativo ("Certifique-se") pode soar acusatório ou excessivamente técnico para um usuário leigo.
**Recomendação:** `"Não foi possível carregar os livros. Verifique se a página está sendo executada por meio de um servidor local (ex: Live Server)."`
**Princípio Clarify:** *Explain what went wrong in plain language. Suggest how to fix it. Don't blame the user.*

## 3. Estados de Carregamento (Loading States)
**Onde:** `script.js` (Linha 5)
**Texto Atual:** `"Carregando acervo..."`
**Problema:** Muito genérico e não define expectativas claras nem tem um tom acolhedor.
**Recomendação:** `"Buscando os livros da sua biblioteca..."` ou `"Carregando seus livros..."`
**Princípio Clarify:** *Set expectations. Explain what's happening.*

## 4. Navegação e Wayfinding (Pontos Positivos)
**Onde:** `keller-casamento.html`, `maquiavel-pedagogo.html`, e páginas de capítulos.
**Texto Atual:** 
- `"Ir para o conteúdo"`
- `"&larr; Voltar para a Biblioteca"`
- `"Aprofunde-se nos Capítulos"`
**Avaliação:** **Excelente.** O uso de verbos ativos e claros para links de navegação descreve de maneira específica a ação e o destino, substituindo rótulos genéricos por orientações significativas. As tabelas em `maquiavel-pedagogo.html` usando as colunas *"Quando você vê..."*, *"Significa que..."* e *"Porque..."* demonstram uma empatia excepcional com o modelo mental do leitor.
**Princípio Clarify:** *Be specific and descriptive. Match user's mental model.*

---

## Resumo de Ação
- **Foco de Refatoração:** Alterar as 3 strings estáticas injetadas pelo arquivo `script.js` para melhorar a experiência em cenários de exceção e primeiro uso.
- **HTML:** Não requerem refatoração de cópia no momento. A arquitetura de texto de navegação está sólida e em conformidade com as diretrizes do Clarify.
