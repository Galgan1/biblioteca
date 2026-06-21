# SKILL — Aprofundador de Textos do Carrossel (Biblioteca · Minuto Real)

> **Para o Gemini.** Você é um redator editorial de não-ficção em **português do Brasil**.
> Sua tarefa: pegar os cards rasos de um livro e transformá-los em texto **profundo,
> quente e premium** para os slides de carrossel da Biblioteca — sem inventar fatos,
> fiel à tese do autor. Cada slide é uma página fotografada; o texto é a alma dela.

---

## O que você recebe

Para **um livro por vez**, você recebe:

1. **Ficha do livro** — título, autor, subtítulo, ideia central.
2. **Os capítulos**, cada um com seu `slug`, título e os **cards atuais (rasos)** —
   já com ícone (`ic`), título (`t`) e um corpo curto (`b`). Esse é o seu **esqueleto
   de partida**: a estrutura está certa, falta profundidade e calor.

Você **mantém** o número de cards e os `slug` dos capítulos. Você **aprofunda** cada card.

---

## A RÉGUA (o padrão de qualidade — siga à risca)

Cada card é um objeto com estes campos:

| campo | obrigatório | o que é |
|-------|-------------|---------|
| `ic`   | sim | nome do ícone de linha (use a LISTA abaixo; mantenha o do esqueleto, salvo se houver um claramente melhor). |
| `t`    | sim | título do card — a grande ideia, **2 a 5 palavras**, em Caixa Alta de Título. |
| `emph` | recomendado | **um trecho EXATO de `t`** (substring literal) que será posto em itálico — a "alma" do título. Tem que aparecer idêntico dentro de `t`. |
| `b`    | sim | o corpo. **3 a 4 frases, ~260 a 340 caracteres.** pt-BR, 2ª pessoa, concreto, editorial e caloroso (não acadêmico, não lista). **Exatamente UMA `<strong>…</strong>`** marcando a frase-bomba. Aspas curvas `“ ”`. |
| `tip`  | recomendado | um fechamento prático no formato `"<strong>Rótulo:</strong> frase curta."`. Rótulos válidos: **Modelo mental, Sinal de alerta, Como aplicar, Regra, Prática, Pergunta-chave, Armadilha, Atalho**. |
| `warn` | ~1 por capítulo | `true` no card de **alerta/perigo** do capítulo (renderiza em coral). No máximo um por capítulo. |

### Princípios de redação
- **Uma ideia por card.** Não empilhe conceitos; aprofunde um só.
- **Calor, não frieza.** Escreva como um grande autor de não-ficção falando com o leitor — imagens concretas, ritmo, 2ª pessoa. Nada de "neste capítulo o autor argumenta que…".
- **Fidelidade.** Use as ideias REAIS do livro (estão no esqueleto + na ficha). Não invente dados, estatísticas, nomes ou citações.
- **A bomba.** A única `<strong>` marca o coração da ideia — a frase que a pessoa printaria.
- **O `tip` paga o ingresso.** Tem que ser acionável: algo que o leitor FAZ ou PERCEBE.
- **Aspas sempre curvas** `“ ”` (nunca `"`). Travessão `—` quando couber.
- **pt-BR sempre.** Nada de português de Portugal (ex.: use "você", "celular", "tela", "ônibus").

### Ícones válidos (campo `ic` — use SÓ estes nomes)
```
arrow book bookmark bubble bulb cards clock constellation eye fork gap key
layers leaf lens link mask masks mountain person pin pivot play scale shelf
shield spark spiral steps sword target triangle wave wrench
```

---

## PADRÃO-OURO (copie este nível de profundidade e calor)

Do livro *As Leis da Natureza Humana* (Robert Greene), capítulo `ch01-irracionalidade`:

```json
{
  "ch01-irracionalidade": {
    "cards": [
      {"ic":"wave","t":"A Emoção Chega Primeiro","emph":"Primeiro","b":"Você sente primeiro e justifica depois — nunca o contrário. A emoção dispara antes do pensamento, e a razão corre atrás dando motivos nobres ao que o corpo já decidiu. Racionalidade não é ausência de emoção: é a emoção <strong>vista de fora e regulada</strong> — e tudo começa em admitir-se mais irracional do que pensa.","tip":"<strong>Modelo mental:</strong> trate a emoção como clima, não como verdade — ela informa, não dita."},
      {"ic":"eye","t":"A Baixa Intensidade Engana Mais","emph":"Baixa Intensidade","b":"A raiva explícita passa; o ressentimento crônico, a inveja morna, o tédio que vira pressa — esses corroem o juízo <strong>sem disparar alarme</strong>, fingindo-se de razão. O perigo não é o furacão visível: é a corrente fria que arrasta devagar. Quanto mais “lógico” você se sente, mais vale desconfiar.","tip":"<strong>Sinal de alerta:</strong> certeza calma e definitiva costuma ser emoção disfarçada de clareza.","warn":true},
      {"ic":"lens","t":"Os Vieses São Lentes Coloridas","emph":"Lentes Coloridas","b":"Confirmação, convicção, aparência, grupo, culpa, superioridade: seis lentes que tingem tudo a favor do <strong>ego</strong>. Você não as arranca — aprende a cor de cada uma e desconta a distorção antes de agir. Sentir muito não torna nada verdadeiro.","tip":"<strong>Como aplicar:</strong> antes de decidir, pergunte “qual viés me favoreceria agora?” — e corrija a rota."},
      {"ic":"gap","t":"A Liberdade Mora no Intervalo","emph":"Intervalo","b":"Entre o que te acontece e o que você faz existe uma fresta — e nela cabe toda a sua liberdade. Uma pausa, nomear a emoção, ver-se como veria um estranho: cada gesto <strong>alarga a fresta</strong> e devolve o comando ao Adulto, tirando-o da Criança e do Pai que reagem por impulso.","tip":"<strong>Regra:</strong> quando a intensidade for alta, espere 24h. Pressa emocional quase nunca decide bem."}
    ]
  }
}
```

Repare: `emph` é um pedaço literal de `t`; uma só `<strong>` por corpo; `tip` rotulado e prático; um `warn:true` no card de alerta; aspas curvas; tom de autor, não de resumo escolar.

---

## FORMATO DE SAÍDA (obrigatório — não desvie)

Devolva **UM único bloco ```json**, um objeto cujas chaves são os `slug` dos capítulos
recebidos (na ordem recebida), cada um com `{"cards":[ … ]}`:

```json
{
  "ch01-...": {"cards":[ {card}, {card}, {card} ]},
  "ch02-...": {"cards":[ {card}, {card}, {card} ]}
}
```

Regras do retorno:
- **Todos** os capítulos recebidos, nenhum a mais, nenhum a menos.
- **Mesmos `slug`** que vieram no esqueleto (copie exatos).
- **Mesma contagem de cards** por capítulo que veio no esqueleto.
- JSON **válido** (aspas duplas nas chaves; as aspas curvas `“ ”` ficam DENTRO das strings, isso é permitido). Sem comentários, sem texto fora do bloco.
- `warn` só quando for `true` (pode omitir nos demais). `emph`/`tip` podem ser omitidos só se realmente não couberem — mas o normal é ter.

O resultado vira `_kit_preview/text/<slug>.json` e entra direto no pipeline da Biblioteca.


---

# LIVRO PARA APROFUNDAR: A Startup Enxuta — Eric Ries

**Subtítulo:** VISÃO GERAL · O MÉTODO CIENTÍFICO PARA EMPREENDER NA INCERTEZA
**Ideia central:** Empreender deixou de ser sorte ou genialidade: virou disciplina. Eric Ries propõe gerir a startup como um experimento contínuo — construir um produto mínimo, medir o que clientes reais fazem e aprender rápido o bastante para decidir entre pivotar e perseverar. O objetivo é eliminar o pior desperdício de todos: construir, com esforço, algo que ninguém quer.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-comecar` — CAPÍTULO 1: Começar (Visão)
- `ch02-definir` — CAPÍTULO 2: Definir (Visão)
- `ch03-aprender` — CAPÍTULO 3: Aprender (Visão)
- `ch04-experimentar` — CAPÍTULO 4: Experimentar (Visão)
- `ch05-saltar` — CAPÍTULO 5: Saltar (Dirigir)
- `ch06-testar` — CAPÍTULO 6: Testar (Dirigir)
- `ch07-medir` — CAPÍTULO 7: Medir (Dirigir)
- `ch08-pivotar-ou-perseverar` — CAPÍTULO 8: Pivotar (ou Perseverar) (Dirigir)
- `ch09-lotes` — CAPÍTULO 9: Lotes (Acelerar)
- `ch10-crescer` — CAPÍTULO 10: Crescer (Acelerar)
- `ch11-adaptar` — CAPÍTULO 11: Adaptar (Acelerar)
- `ch12-inovar` — CAPÍTULO 12: Inovar (Acelerar)
- `ch13-epilogo-nao-desperdice` — CAPÍTULO 13: Epílogo — Não Desperdice (Acelerar)
- `ch14-juntar-se-ao-movimento` — CAPÍTULO 14: Junte-se ao Movimento (Acelerar)

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-comecar": {
  "cards": [
   {
    "ic": "spark",
    "t": "O Que É uma Startup",
    "b": "'Uma <strong>instituição humana</strong> projetada para criar um novo produto ou serviço sob condições de <strong>extrema incerteza</strong>.' Tamanho, setor e idade não importam — o que define é a incerteza.",
    "tip": "<strong>Como aplicar:</strong> se você não sabe quem é o cliente nem o que ele quer, está numa startup — mesmo dentro de uma grande empresa."
   },
   {
    "ic": "wrench",
    "t": "Empreendedorismo É Gestão",
    "b": "A startup precisa de uma gestão <strong>própria</strong>, calibrada para a incerteza — nem a gestão de execução das empresas maduras, nem a ausência de método ('é só fazer'). O vácuo de gestão é tão fatal quanto o excesso.",
    "tip": "<strong>Modelo mental:</strong> disciplina não mata a criatividade; canaliza-a para o aprendizado."
   },
   {
    "ic": "layers",
    "t": "As Cinco Raízes",
    "b": "O método bebe da <strong>produção enxuta</strong> (Toyota), do <em>design thinking</em>, do <strong>desenvolvimento de clientes</strong> (Steve Blank) e do pensamento ágil. Empreendedores estão por toda parte — da garagem à multinacional.",
    "tip": "<strong>Para refletir:</strong> o sucesso de uma startup pode ser ensinado e aprendido — não é só sorte."
   }
  ]
 },
 "ch02-definir": {
  "cards": [
   {
    "ic": "person",
    "t": "Empreendedor Como Cargo",
    "b": "Qualquer pessoa, em qualquer organização, que cria um novo produto sob extrema incerteza — o <strong>intraempreendedor</strong> incluído. Inovar não é monopólio das startups jovens.",
    "tip": "<strong>Para refletir:</strong> a desculpa de que 'só garagens inovam' impede a empresa grande de criar seu próprio espaço de experimentação."
   },
   {
    "ic": "mountain",
    "t": "O Porto Seguro da Inovação",
    "b": "A inovação interna exige três coisas: <strong>recursos escassos porém seguros</strong>, <strong>autoridade independente</strong> para tocar o negócio e <strong>participação pessoal</strong> no resultado.",
    "tip": "<strong>Como aplicar:</strong> dê à equipe um espaço protegido onde experimentar sem ser esmagada pela máquina de execução."
   },
   {
    "ic": "layers",
    "t": "Portfólio de Inovação",
    "b": "Veja a empresa madura como um portfólio de <strong>execução</strong> e de <strong>experimentos</strong> — e proteja os experimentos da lógica (processos, métricas, prazos) do negócio maduro.",
    "tip": "<strong>Modelo mental:</strong> inovação é capacidade contínua, não projeto pontual."
   }
  ]
 },
 "ch03-aprender": {
  "cards": [
   {
    "ic": "target",
    "t": "Aprendizado Validado",
    "b": "Demonstrar <strong>empiricamente</strong>, com dados de clientes reais, que se descobriu algo verdadeiro sobre o presente e o futuro do negócio. É a métrica do progresso real — não 'entregamos o recurso X'.",
    "tip": "<strong>Como aplicar:</strong> pergunte de cada atividade — 'que aprendizado isto produz?'. Se a resposta é 'nenhum', é desperdício."
   },
   {
    "ic": "key",
    "t": "As Duas Perguntas",
    "b": "Para todo plano, separe '<strong>Este produto PODE ser construído?</strong>' de '<strong>DEVEMOS construí-lo?</strong>' e 'há um <strong>negócio sustentável</strong> em torno dele?'. A engenharia heroica responde à primeira e ignora as outras duas.",
    "tip": "<strong>Para refletir:</strong> a pergunta certa quase nunca é 'podemos?', mas 'devemos, e há negócio aqui?'."
   },
   {
    "ic": "lens",
    "t": "O Caso IMVU",
    "b": "Ries gastou meses construindo integração com mensageiros existentes, supondo que os usuários só adotariam o avatar se usassem com amigos antigos. Eles queriam <strong>fazer novos amigos</strong> — todo o esforço foi <strong>desperdício</strong>.",
    "tip": "<strong>Modelo mental:</strong> 'aprendemos muito' sem dados de cliente é racionalização de fracasso, não aprendizado validado."
   }
  ]
 },
 "ch04-experimentar": {
  "cards": [
   {
    "ic": "scale",
    "t": "As Duas Hipóteses",
    "b": "Todo plano repousa sobre <strong>saltos de fé</strong>. A <strong>hipótese de valor</strong> testa se o produto entrega valor real ao ser usado; a <strong>hipótese de crescimento</strong> testa como novos clientes o descobrem e o espalham.",
    "tip": "<strong>Como aplicar:</strong> liste as suposições, ordene por risco e teste primeiro a mais arriscada."
   },
   {
    "ic": "spark",
    "t": "A Startup É um Experimento",
    "b": "Trate o plano como <strong>teste de hipóteses</strong>, não como execução. 'Quem é o cliente?' e 'o que ele considera valor?' se respondem <strong>empiricamente</strong> — pense grande, mas comece pelo experimento mais barato.",
    "tip": "<strong>Para refletir:</strong> confie no que o cliente FAZ, não no que ele DIZ numa pesquisa de opinião."
   },
   {
    "ic": "steps",
    "t": "O Caso Zappos",
    "b": "Antes de ter estoque, Nick Swinmurn <strong>fotografou sapatos de lojas reais</strong> e os vendeu online; quando alguém comprava, ele ia à loja e enviava. Um experimento barato testou a hipótese de valor ('as pessoas comprarão sapatos pela internet?').",
    "tip": "<strong>Modelo mental:</strong> um experimento é um produto — rode-o cedo, barato, com clientes reais."
   }
  ]
 },
 "ch05-saltar": {
  "cards": [
   {
    "ic": "scale",
    "t": "Suposições de Salto de Fé",
    "b": "As duas mais importantes são a <strong>hipótese de valor</strong> e a <strong>hipótese de crescimento</strong>. São o ponto de partida da estratégia: a suposição mais arriscada da qual <strong>tudo o mais depende</strong>.",
    "tip": "<strong>Como aplicar:</strong> ordene as suposições por risco e teste primeiro a que, se falsa, derruba o negócio."
   },
   {
    "ic": "eye",
    "t": "Genchi Gembutsu",
    "b": "O princípio da Toyota: '<strong>vá e veja por si mesmo</strong>'. Fundamente a estratégia em conhecimento de primeira mão do cliente, não em relatórios de segunda mão. <strong>Saia do prédio</strong> (Steve Blank).",
    "tip": "<strong>Para refletir:</strong> estratégia de gabinete, sem nunca observar um cliente real, é fé disfarçada de plano."
   },
   {
    "ic": "link",
    "t": "Analogias e Antílogos",
    "b": "Para sustentar saltos de fé, identifique o que outra empresa <strong>provou</strong> (analogia) e o que ela deliberadamente <strong>não fez</strong> (antílogo) — isolando a pergunta de fé que ainda resta sem resposta.",
    "tip": "<strong>Modelo mental:</strong> copiar o sucesso alheio sem isolar a hipótese não testada é confundir analogia com prova."
   }
  ]
 },
 "ch06-testar": {
  "cards": [
   {
    "ic": "spark",
    "t": "Produto Mínimo Viável (MVP)",
    "b": "'A versão de um novo produto que permite coletar o <strong>máximo de aprendizado validado</strong> com o <strong>menor esforço</strong>.' Existe para aprender — corte tudo que não serve ao aprendizado de agora.",
    "tip": "<strong>Como aplicar:</strong> recurso polido que o cliente não usa não é qualidade — é desperdício."
   },
   {
    "ic": "eye",
    "t": "MVP de Vídeo (Dropbox)",
    "b": "Drew Houston gravou um <strong>vídeo de 3 minutos</strong> mostrando como o produto funcionaria, antes de construí-lo. A lista de espera saltou de <strong>5 mil para 75 mil</strong> em uma noite — validação suficiente para justificar a construção.",
    "tip": "<strong>Modelo mental:</strong> o vídeo testou a hipótese de valor sem escrever o produto inteiro."
   },
   {
    "ic": "person",
    "t": "Conserje e Mágico de Oz",
    "b": "No <strong>MVP conserje</strong>, o serviço é entregue <strong>manualmente</strong>, um cliente por vez, sem automação. No <strong>Mágico de Oz</strong>, o cliente pensa interagir com um produto automatizado, mas há humanos 'atrás da cortina'.",
    "tip": "<strong>Para refletir:</strong> não escala — de propósito; máximo aprendizado por cliente antes de codar."
   }
  ]
 },
 "ch07-medir": {
  "cards": [
   {
    "ic": "steps",
    "t": "Contabilidade da Inovação",
    "b": "Três passos: (1) use um MVP para estabelecer o <strong>baseline</strong> real; (2) <strong>afine o motor</strong> com experimentos rumo ao ideal; (3) decida <strong>pivotar ou perseverar</strong>. É como saber se a startup faz progresso real.",
    "tip": "<strong>Como aplicar:</strong> defina a meta de melhoria ANTES; se os experimentos não a movem, a estratégia está furada."
   },
   {
    "ic": "eye",
    "t": "Acionáveis × de Vaidade",
    "b": "<strong>Vaidade:</strong> números brutos que sobem com o tempo e agradam (total de usuários, hits), mas não orientam decisão. <strong>Acionáveis:</strong> demonstram causa→efeito claros. Boa métrica = <strong>3 As</strong>: Acionável, Acessível, Auditável.",
    "tip": "<strong>Sinal de alerta:</strong> o gráfico que 'só sobe' costuma esconder a estagnação real."
   },
   {
    "ic": "layers",
    "t": "Coorte e Teste A/B",
    "b": "A <strong>análise de coorte</strong> mede cada grupo de clientes que entrou no mesmo período (cadastro → uso → retorno → pagamento), revelando a verdade que os totais escondem. O <strong>teste A/B</strong> isola o efeito de uma mudança.",
    "tip": "<strong>Modelo mental:</strong> coortes mostram se o produto melhora de fato, não só se cresce o número bruto."
   }
  ]
 },
 "ch08-pivotar-ou-perseverar": {
  "cards": [
   {
    "ic": "fork",
    "t": "O Pivô",
    "b": "'Uma <strong>correção estruturada de curso</strong> para testar uma nova hipótese fundamental sobre o produto, a estratégia e o motor de crescimento.' Muda a <strong>estratégia</strong>, mantém a <strong>visão</strong> — e não é admissão de fracasso.",
    "tip": "<strong>Como aplicar:</strong> mantenha reuniões regulares de pivotar-ou-perseverar guiadas por dados, não por opinião."
   },
   {
    "ic": "cards",
    "t": "O Catálogo de Pivôs",
    "b": "Tipos: <strong>zoom-in</strong> (um recurso vira o produto), <strong>zoom-out</strong> (o produto vira recurso de algo maior), segmento de cliente, necessidade, plataforma, arquitetura de negócio, <strong>captura de valor</strong> (monetização), motor de crescimento, canal e tecnologia.",
    "tip": "<strong>Modelo mental:</strong> pivô não é mudar tudo no pânico — é trocar UMA hipótese, com clareza."
   },
   {
    "ic": "pin",
    "t": "A Pista É o Nº de Pivôs",
    "b": "Redefina a <strong>pista (runway)</strong>: não 'dinheiro restante', mas o <strong>número de pivôs que ainda dá para fazer</strong>. Acelerar o ciclo aumenta a pista sem mais capital. Cuidado com a <strong>'terra dos mortos-vivos'</strong>.",
    "tip": "<strong>Sinal de alerta:</strong> crescer o bastante para sobreviver, mas não para validar nem encerrar — falta pivotar."
   }
  ]
 },
 "ch09-lotes": {
  "cards": [
   {
    "ic": "steps",
    "t": "Lotes Pequenos",
    "b": "Mover <strong>uma unidade de trabalho por vez</strong> pelo fluxo (single-piece flow) vence o lote grande: feedback mais rápido, defeitos detectados cedo, menos retrabalho — mesmo parecendo contraintuitivo.",
    "tip": "<strong>Como aplicar:</strong> implantação contínua leva mudanças pequenas à produção muitas vezes ao dia."
   },
   {
    "ic": "spark",
    "t": "O Cordão Andon",
    "b": "Na Toyota, qualquer operário <strong>puxa o cordão (andon) para parar a linha</strong> ao ver um defeito. Qualidade é <strong>construída na fonte</strong>, não inspecionada no fim — quando o custo de corrigir é máximo.",
    "tip": "<strong>Modelo mental:</strong> pare a linha cedo; o defeito barato de hoje é o desastre caro de amanhã."
   },
   {
    "ic": "wave",
    "t": "Puxar, Não Empurrar",
    "b": "Como na fábrica enxuta, a produção é <strong>puxada pela demanda</strong> e pelo aprendizado real — não <strong>empurrada por um plano</strong>. O experimento dos envelopes prova: a carta completa, uma por vez, termina antes do lote.",
    "tip": "<strong>Para refletir:</strong> no lote grande, o erro só aparece no fim — com 100 unidades para refazer."
   }
  ]
 },
 "ch10-crescer": {
  "cards": [
   {
    "ic": "spiral",
    "t": "Motor Recorrente (Pegajoso)",
    "b": "Cresce <strong>retendo clientes</strong>. A métrica-mestra é a <strong>taxa de atrito (churn)</strong>: se a aquisição supera o cancelamento, o produto cresce. Foque em retenção.",
    "tip": "<strong>Sinal de alerta:</strong> total de usuários sobe mas churn > aquisição = encolhendo em segredo."
   },
   {
    "ic": "link",
    "t": "Motor Viral",
    "b": "Cresce porque o <strong>uso normal do produto</strong> o espalha entre novos clientes. A métrica é o <strong>coeficiente viral</strong> — quantos usuários cada usuário traz. Acima de <strong>1,0</strong> = crescimento exponencial.",
    "tip": "<strong>Modelo mental:</strong> ciclo viral vem do produto em uso, não de uma campanha de marketing."
   },
   {
    "ic": "scale",
    "t": "Motor Pago",
    "b": "Cresce <strong>reinvestindo a receita</strong> em aquisição. Funciona enquanto o <strong>valor do tempo de vida do cliente (LTV)</strong> for maior que o <strong>custo de aquisição (CPA)</strong>; a margem entre eles financia o crescimento.",
    "tip": "<strong>Regra:</strong> foque em UM motor por vez — misturar alavancas embaralha as métricas."
   }
  ]
 },
 "ch11-adaptar": {
  "cards": [
   {
    "ic": "spiral",
    "t": "Os 5 Porquês",
    "b": "Diante de um problema, pergunte '<strong>por quê?</strong>' cinco vezes para ir da causa sintomática (técnica) à <strong>causa-raiz</strong> (quase sempre humana/de processo). Cada 'porquê' desce um nível.",
    "tip": "<strong>Como aplicar:</strong> servidor caiu → ... → 'o gerente acha que não há tempo para treinar' — a raiz é a política de onboarding, não o engenheiro."
   },
   {
    "ic": "scale",
    "t": "Investimento Proporcional",
    "b": "Gaste em correção <strong>na medida da gravidade</strong> do sintoma: pequenos problemas, pequenas correções. Isso evita tanto a <strong>burocracia excessiva</strong> quanto a negligência que deixa o erro voltar.",
    "tip": "<strong>Para refletir:</strong> reagir a um problema pequeno com uma reforma gigante é overdose de processo."
   },
   {
    "ic": "person",
    "t": "Mire o Sistema, Não a Pessoa",
    "b": "A regra de ouro: comece com <strong>tolerância</strong> e mire o processo. 'Se você comete um erro e é humilhado, aprende a <strong>esconder erros</strong>.' Os '5 porquês' viram '<strong>5 culpados</strong>' quando usados para apontar dedos.",
    "tip": "<strong>Modelo mental:</strong> a organização adaptativa regula seu ritmo de processo conforme cresce — nem caos, nem burocracia."
   }
  ]
 },
 "ch12-inovar": {
  "cards": [
   {
    "ic": "mountain",
    "t": "Os Três Requisitos",
    "b": "Toda equipe de inovação precisa de: (1) <strong>recursos escassos porém seguros</strong>; (2) <strong>autoridade independente</strong> para tocar o negócio; (3) <strong>participação pessoal</strong> (pele em jogo) no resultado.",
    "tip": "<strong>Como aplicar:</strong> uma equipe pequena, multifuncional e dedicada, dona do experimento inteiro."
   },
   {
    "ic": "target",
    "t": "O Sandbox de Experimentação",
    "b": "Um espaço delimitado com <strong>regras claras</strong>: cada experimento atende um nº limitado de clientes, dura um tempo definido, mede métricas acionáveis fixas, e a <strong>mesma equipe</strong> acompanha o resultado de ponta a ponta.",
    "tip": "<strong>Modelo mental:</strong> o sandbox protege a empresa (do risco) e a equipe (da máquina de execução)."
   },
   {
    "ic": "layers",
    "t": "Gestão de Portfólio",
    "b": "Empresas maduras precisam gerir, ao mesmo tempo, a <strong>inovação disruptiva</strong> e a <strong>execução do negócio existente</strong> — com lideranças e métricas distintas. Inovação é capacidade contínua, não evento.",
    "tip": "<strong>Sinal de alerta:</strong> experimentar sem que alguém responda pelo aprendizado é inovação sem responsabilidade."
   }
  ]
 },
 "ch13-epilogo-nao-desperdice": {
  "cards": [
   {
    "ic": "leaf",
    "t": "Eliminar o Desperdício",
    "b": "Na herança da produção enxuta, desperdício é tudo que <strong>não cria valor</strong> para o cliente — e o pior é a <strong>energia humana</strong> gasta no produto errado. Cada esforço deve passar no teste do aprendizado validado.",
    "tip": "<strong>Para refletir:</strong> ser ótimo a construir algo que não deveria existir é eficiência no lugar errado."
   },
   {
    "ic": "target",
    "t": "Produtividade Real",
    "b": "Em startups, mede-se não por <strong>quanto se produz</strong>, mas por <strong>quanto aprendizado validado</strong> se gera. A abundância de ideias não é o gargalo — falta o método que filtra quais merecem ser construídas.",
    "tip": "<strong>Modelo mental:</strong> o método enxuto é esse filtro contra o desperdício de ideias."
   },
   {
    "ic": "lens",
    "t": "Honestidade Científica",
    "b": "Aplique o método com rigor honesto, <strong>sem usar dados para confirmar</strong> o que já se queria fazer. A Startup Enxuta é um <strong>movimento em evolução</strong>, não um ritual fechado de autoengano.",
    "tip": "<strong>Sinal de alerta:</strong> 'experimentos' desenhados para confirmar a decisão já tomada são ciência de fachada."
   }
  ]
 },
 "ch14-juntar-se-ao-movimento": {
  "cards": [
   {
    "ic": "spiral",
    "t": "O Ciclo Como Cultura",
    "b": "A meta não é rodar o ciclo uma vez, mas torná-lo o <strong>sistema operacional</strong> da organização — minimizando o tempo total de cada volta de Construir-Medir-Aprender.",
    "tip": "<strong>Como aplicar:</strong> internalize o laço; cada decisão vira hipótese a testar, não aposta a defender."
   },
   {
    "ic": "book",
    "t": "Princípios, Não Receitas",
    "b": "Técnicas específicas (MVP de vídeo, conserje, 5 porquês) <strong>envelhecem</strong>; os <strong>princípios</strong> (aprendizado validado, experimentação rigorosa, contabilidade da inovação) permanecem e devem ser <strong>adaptados</strong> ao seu contexto.",
    "tip": "<strong>Sinal de alerta:</strong> aplicar uma ferramenta fora de contexto, ignorando o princípio, é culto à técnica."
   },
   {
    "ic": "clock",
    "t": "Gestão de Longo Prazo",
    "b": "Empresas que pensam em <strong>décadas</strong> precisam de estruturas que recompensem o <strong>aprendizado contínuo</strong>, não só o resultado trimestral. O objetivo final: uma economia que desperdice menos talento humano.",
    "tip": "<strong>Para refletir:</strong> medir só o trimestre sufoca a inovação que rende em anos."
   }
  ]
 }
}
```
