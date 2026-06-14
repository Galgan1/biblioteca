# Relatório de Otimização de Performance (Impeccable Optimize)

Com base nas heurísticas do `optimize.md`, realizei uma auditoria técnica de performance nos arquivos do projeto `biblioteca`. Abaixo estão os gargalos identificados e as recomendações práticas para mitigá-los, focando em métricas de Core Web Vitals (LCP, CLS, INP) e eficiência de renderização.

## 1. Gargalos de Renderização (Paint & Composite)

**SVG Noise Filter (Problema Crítico de CPU/GPU)**
- **Problema**: No arquivo `assets/style.css` (linha 62), a classe `.page` aplica um `background-image` embutido com um filtro SVG `<feTurbulence>`. Filtros matemáticos de ruído fractal processados em tempo de execução para preencher grandes áreas (neste caso, a página inteira) exigem alto processamento de *paint*. Durante o scroll ou na animação inicial de `fade-in`, isso vai causar queda severa de frames (jank), especialmente em dispositivos móveis.
- **Recomendação**: Substituir o Data URI dinâmico por um padrão de imagem pré-renderizado, pequeno (ex: tile PNG ou WebP em base64) repetido na tela, ou usar um ruído muito simples em CSS estático.

## 2. Cumulative Layout Shift (CLS) e Loading Performance

**Carregamento e Espaçamento de Imagens**
- **Problema**: No `script.js` (linha 32), a injeção da capa do livro (`<img>`) não inclui o atributo `loading="lazy"`. O navegador baixará todas as capas da biblioteca de uma só vez, mesmo as que estão abaixo da dobra. Além disso, a ausência de propriedades que definam a relação de aspecto (ex: `aspect-ratio` no CSS ou atributos inline) pode causar reflows de layout tardios.
- **Recomendação**: Injetar `<img loading="lazy" ...>` e garantir que o contêiner `.card-cover` e a imagem usem a propriedade CSS `aspect-ratio` nativa, preservando o retângulo de desenho mesmo se a rede for lenta.

**Layout Shift no Estado de Loading**
- **Problema**: O arquivo `script.js` começa inserindo um texto simples ("Carregando acervo...") na grid principal. Ao terminar o fetch, este texto é destruído e a grid preenchida, empurrando subitamente elementos (como o rodapé) para baixo. Este é um CLS clássico que prejudica a experiência e métricas de Web Vitals.
- **Recomendação**: Substituir a mensagem de carregamento por um "Skeleton Loader". Desenhe cards cinzas intermitentes que imitem a altura real dos cards finais, segurando a estabilidade visual da página até os dados entrarem.

## 3. Manipulação do DOM (Layout Thrashing)

**Escrita no DOM dentro do Loop**
- **Problema**: Em `script.js` (linha 42), utiliza-se `bookshelf.appendChild(bookEl)` a cada iteração do `forEach()`. Alterar diretamente uma árvore visível dentro de laços leva o navegador a recalcular estilos prematuramente (*reflow*).
- **Recomendação**: Centralizar a manipulação com a API de `DocumentFragment`. Anexe cada `bookEl` a esse fragmento invisível durante o loop e, depois do laço, insira o fragmento inteiro de uma única vez com `bookshelf.appendChild()`. Alternativamente, criar um array de nós e inseri-los com `.append(...nodes)`.

## 4. Animações e GPU Acceleration

**Pontos de Excelência e Observação**
- **Ponto Positivo**: As classes `.animate-entrance` e animações base de página dependem ativamente de propriedades compostas (`transform` e `opacity`). Isso obedece ao requisito de otimização em placa de vídeo listado nas diretrizes, garantindo os cobiçados 60fps.
- **Atenção**: O acordeão em `style.css` (expansão via `grid-template-rows: 0fr -> 1fr`) altera propriedades de layout para funcionar. Embora essa seja uma estratégia moderna aceitável (diferente de alterar alturas via JavaScript), certifique-se de que a leitura de longas listas nas páginas HTML estáticas não sofra Input Delay (INP) perceptível se os browsers demorarem a recalcular o layout de todos os irmãos adjacentes ao se clicar num detalhe.
