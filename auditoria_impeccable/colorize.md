# Auditoria de Cores (Impeccable Colorize)
**Projeto:** Biblioteca (Cheat Sheets)
**Estratégia Recomendada:** Restrained (com base na marca "Infographic Green")

## 1. Avaliação do Estado Atual (Assess Color Opportunity)
- **Paleta Atual:** O projeto utiliza uma paleta Restrained baseada em tons de verde (`#1b4332`, `#e8eee9`) e cinzas quentes/amarelados para simular papel (`#fcfbf8`, `#e9e6df`).
- **Problemas Identificados:**
  - **Uso de HEX:** O arquivo `assets/style.css` utiliza cores em HEX. O guia exige o uso de **OKLCH** para garantir a uniformidade perceptiva.
  - **Tintura AI "Cream/Sand" Giveaway:** As cores de fundo (`#fcfbf8` e `#e9e6df`) são típicos amarelos/beges "quentes". Como a cor da marca é verde, os neutros devem ser matizados (tinted) em direção ao verde, e não usar esse bege/creme padrão.
  - **Alpha como "Design Smell":** Existem usos de `rgba(255, 255, 255, 0.5)` no `:hover` dos cards e `rgba(0,0,0,0.02)` nos botões de navegação dos HTMLs. O uso de transparência (alpha) gera contrastes imprevisíveis.
  - **Falta de Cores Semânticas:** Embora seja uma interface de leitura, a ausência de uma paleta semântica impede destaques consistentes de categorias ou alertas (ex: sucesso, erro, warning, info).

## 2. Estratégia de Cores (Plan Color Strategy)
A paleta deve continuar sendo "Restrained", mas precisa ser migrada para OKLCH e ganhar coesão subconsciente amarrando os tons de cinza à matiz (hue) do verde principal.

- **Cor Dominante / Accent:** Verde Escuro. Em OKLCH, a matiz correspondente fica em torno de `150`.
- **Neutros:** Todos os cinzas (`--black`, `--gray-dark`, `--gray-light`) devem ter um croma muito leve (0.005 a 0.015) com a mesma matiz do verde (`hue ~150`), eliminando o cinza puro ou o bege puro.
- **Superfícies:** O fundo da página e os cards devem adotar um fundo claro matizado de verde, abandonando o bege atual.

## 3. Recomendações de Implementação

### 3.1. Migração para OKLCH e Fim do "Cream/Sand"
Atualize a raiz (`:root`) do `style.css` e o `body` para a seguinte lógica (valores de exemplo na matiz verde `150`):
```css
:root {
    --green: oklch(35% 0.06 150);
    --green-light: oklch(92% 0.02 150);
    
    /* Neutros matizados em direção ao verde (chroma ~0.01) */
    --black: oklch(25% 0.01 150); 
    --gray-dark: oklch(50% 0.01 150);
    --gray-light: oklch(85% 0.01 150);
    
    /* Superfícies matizadas no verde da marca, não no bege padrão */
    --paper-bg: oklch(98% 0.005 150); 
    --body-bg: oklch(94% 0.01 150);
}

body {
    background: var(--body-bg);
}
```

### 3.2. Eliminação de Canais Alpha (RGBA)
Substitua todos os fundos translúcidos por cores sólidas sobrepostas que pertençam à escala OKLCH.
- Em `.card:hover`, remova `background-color: rgba(255, 255, 255, 0.5);` e utilize um valor sólido mais claro que `--paper-bg`, como `oklch(99% 0.002 150)`.
- Nos links de capítulos (arquivos HTML com `style="... background: rgba(0,0,0,0.02);"`), remova o estilo inline e use uma variável `--surface-hover` com um cinza sólido explícito ou verde ultra-claro.

### 3.3. Adição de Paleta Semântica
Mesmo com uma estética contida, defina tokens semânticos (em OKLCH) na matiz apropriada, caso precise destacar trechos de atenção:
```css
:root {
    --color-success: oklch(65% 0.12 150);
    --color-warning: oklch(75% 0.15 65);
    --color-error: oklch(60% 0.15 25);
    --color-info: oklch(65% 0.10 250);
}
```

### 3.4. Refinamento de Contraste e Bordas
- As bordas tracejadas (`--border-dashed: 2px dashed #a2b8ab`) devem ser convertidas para uma variável OKLCH correspondente.
- Mantenha a prática correta de aplicar as bordas de maneira global nos cards e não utilizar side-stripes (ex: `border-left > 1px`), o que cumpre com os absolute bans da heurística Impeccable.

### 3.5. Parâmetros de Assinatura (Live-mode)
Para integração do cheat sheet em ambientes "live mode", adicione o parâmetro de controle de quantidade de cor:
```css
:root {
    --p-color-amount: 0.5; /* Modulado de 0 a 1 */
    --surface-tint: oklch(98% calc(0.01 * var(--p-color-amount)) 150);
}
```
Isso permitirá ao usuário controlar o quão "drenched" a superfície ficará com a cor da marca.
