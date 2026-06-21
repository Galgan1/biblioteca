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

# LIVRO PARA APROFUNDAR: Sapiens — Yuval Noah Harari

**Subtítulo:** VISÃO GERAL · UMA BREVE HISTÓRIA DA HUMANIDADE
**Ideia central:** Um animal sem importância — o Homo sapiens — virou senhor do planeta. Como? Por três grandes revoluções (Cognitiva, Agrícola, Científica) e, acima de tudo, pela capacidade única de criar e crer em ficções compartilhadas — deuses, dinheiro, nações, direitos. São esses mitos que permitem cooperar com estranhos em número ilimitado. E o livro fecha encarando o que vem depois: o sapiens prestes a trocar a seleção natural pelo design inteligente.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-revolucao-cognitiva` — CAPÍTULO 1: A Revolução Cognitiva
- `ch02-cacadores-coletores` — CAPÍTULO 2: O Mundo dos Caçadores-Coletores
- `ch03-revolucao-agricola` — CAPÍTULO 3: A Revolução Agrícola — A Maior Fraude da História
- `ch04-piramides-escrita-memoria` — CAPÍTULO 4: Pirâmides, Burocracia e Escrita
- `ch05-ordem-imaginada-hierarquias` — CAPÍTULO 5: A Ordem Imaginada e as Hierarquias
- `ch06-dinheiro` — CAPÍTULO 6: O Dinheiro
- `ch07-imperios` — CAPÍTULO 7: Os Impérios
- `ch08-religioes` — CAPÍTULO 8: As Religiões
- `ch09-revolucao-cientifica` — CAPÍTULO 9: A Revolução Científica — A Descoberta da Ignorância
- `ch10-ciencia-imperio-capital` — CAPÍTULO 10: O Casamento Ciência-Império-Capital
- `ch11-capitalismo-credito` — CAPÍTULO 11: O Credo Capitalista — Crédito e o Futuro
- `ch12-felicidade` — CAPÍTULO 12: E Eles Viveram Felizes? — A (In)felicidade do Sapiens
- `ch13-fim-do-homo-sapiens` — CAPÍTULO 13: O Fim do Homo Sapiens

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-revolucao-cognitiva": {
  "cards": [
   {
    "ic": "bulb",
    "t": "Ficção Compartilhada",
    "b": "O sapiens cria entidades que só existem na <strong>imaginação coletiva</strong>: deuses, dinheiro, nações, empresas. Não são mentiras nem realidade física — são <strong>realidade intersubjetiva</strong>: reais enquanto muitos creem.",
    "tip": "<strong>Modelo mental:</strong> pense em 'real' em 3 camadas — objetivo (rios), subjetivo (minha dor), intersubjetivo (dinheiro, leis)."
   },
   {
    "ic": "link",
    "t": "Cooperação Flexível",
    "b": "O que separou o sapiens das outras espécies humanas não foi força nem inteligência individual: foi <strong>cooperar com estranhos</strong> em número ilimitado, com base num mito comum.",
    "tip": "<strong>Como aplicar:</strong> toda ordem em larga escala (religião, nação, corporação) repousa sobre uma ficção aceita."
   },
   {
    "ic": "person",
    "t": "O Teto dos 150",
    "b": "Laços por conhecimento pessoal e fofoca saturam em ~150 pessoas (<strong>número de Dunbar</strong>). Acima disso, só um <strong>mito comum</strong> sustenta a cooperação — e nascem cidades, exércitos, impérios.",
    "tip": "<strong>Regra:</strong> acima de ~150, procure sempre a ficção que faz milhares agirem juntos."
   }
  ]
 },
 "ch02-cacadores-coletores": {
  "cards": [
   {
    "ic": "leaf",
    "t": "Abundância Original",
    "b": "Dieta variada, menos horas de trabalho, menos doenças que o agricultor. O forrageador 'trabalhava' poucas horas e conhecia centenas de espécies do seu ambiente.",
    "tip": "<strong>Para refletir:</strong> muitos males modernos vêm do descompasso entre genes de forrageador e ambiente de hoje."
   },
   {
    "ic": "steps",
    "t": "Preconceito do Progresso",
    "b": "A tendência de ler a história como ascensão linear. Muitas mudanças — sobretudo a agricultura — <strong>pioraram</strong> a vida do indivíduo médio mesmo aumentando o poder da espécie.",
    "tip": "<strong>Como aplicar:</strong> ao avaliar uma 'revolução', pergunte: melhorou para a espécie ou para o indivíduo?"
   },
   {
    "ic": "mountain",
    "t": "Extinção da Megafauna",
    "b": "Ao se espalhar (Austrália, Américas), o sapiens dizimou os grandes animais. Foi o <strong>primeiro grande impacto ecológico</strong> — muito antes da era industrial.",
    "tip": "<strong>Para refletir:</strong> o dano ecológico do sapiens é antigo, não invenção da indústria."
   }
  ]
 },
 "ch03-revolucao-agricola": {
  "cards": [
   {
    "ic": "layers",
    "t": "A Maior Fraude",
    "b": "A agricultura multiplicou a população (sucesso da <strong>espécie</strong>) mas piorou a vida do <strong>indivíduo</strong> médio: jornadas exaustivas, dieta pobre, doenças da aglomeração. O luxo de poucos pago pelo trabalho de muitos.",
    "tip": "<strong>Modelo mental:</strong> separe 'mais poder/quantidade' de 'mais bem-estar' — a agricultura é o exemplo-mãe da divergência."
   },
   {
    "ic": "spiral",
    "t": "Quem Domesticou Quem",
    "b": "O trigo passou de erva selvagem a um dos vegetais mais difundidos do planeta — usando o sapiens como <strong>ferramenta de reprodução</strong>. Medido em DNA, o trigo 'venceu'; medido em felicidade, o camponês perdeu.",
    "tip": "<strong>Para refletir:</strong> sucesso evolutivo não é sinônimo de indivíduos mais felizes."
   },
   {
    "ic": "key",
    "t": "Armadilha do Luxo",
    "b": "Cada melhoria vira <strong>necessidade</strong> e gera mais trabalho, não mais lazer. Conveniências criam novas obrigações — vale do trigo ao e-mail.",
    "tip": "<strong>Como aplicar:</strong> ao adotar uma conveniência, pergunte que novo trabalho ela vai criar."
   }
  ]
 },
 "ch04-piramides-escrita-memoria": {
  "cards": [
   {
    "ic": "layers",
    "t": "A Ordem Antes da Pedra",
    "b": "Monumentos, exércitos e impérios são erguidos por gente que acredita num <strong>mito comum</strong> (o faraó-deus, o rei legítimo). Antes da pedra, a ficção crida por muitos.",
    "tip": "<strong>Modelo mental:</strong> em todo grande projeto coletivo, procure a história que faz milhares obedecerem."
   },
   {
    "ic": "book",
    "t": "Escrita = Contabilidade",
    "b": "Os registros mais antigos são listas de impostos e estoques — <strong>não literatura</strong>. A escrita supera o limite do cérebro para guardar informação impessoal. A poesia veio muito depois.",
    "tip": "<strong>Para refletir:</strong> a escrita nasceu do fisco, não da arte."
   },
   {
    "ic": "cards",
    "t": "A Burocracia como Prateleira",
    "b": "Catalogar exige categorias, índices, gavetas. A burocracia <strong>compartimenta a realidade</strong> para administrá-la — eficiente, mas deformante.",
    "tip": "<strong>Como aplicar:</strong> gaveta administrativa não é a coisa em si; não tome a categoria pela realidade."
   }
  ]
 },
 "ch05-ordem-imaginada-hierarquias": {
  "cards": [
   {
    "ic": "scale",
    "t": "A Ordem Imaginada",
    "b": "A teia de regras compartilhadas que estrutura a vida coletiva (Hamurabi, Declaração de Independência). É objetiva (existe fora de mim), mas só porque é <strong>intersubjetiva</strong> — crida por muitos.",
    "tip": "<strong>Modelo mental:</strong> 'todos os homens são criados iguais' é tão imaginado quanto a ordem das castas — o que muda é a qualidade da ficção."
   },
   {
    "ic": "eye",
    "t": "Os 3 Truques",
    "b": "A ordem se sustenta porque: (1) está <strong>embutida no mundo material</strong> (arquitetura, roupas); (2) <strong>molda nossos desejos</strong>; (3) é <strong>intersubjetiva</strong> — mudá-la exige convencer milhões ao mesmo tempo.",
    "tip": "<strong>Regra:</strong> para mudar uma ordem imaginada, não basta querer — é preciso convencer multidões."
   },
   {
    "ic": "spiral",
    "t": "Hierarquia 'Natural'",
    "b": "Castas, escravidão, racismo, patriarcado nascem de <strong>acidentes históricos</strong> e se autoperpetuam por um <strong>círculo vicioso</strong>: lei → discriminação → 'prova' de inferioridade → lei.",
    "tip": "<strong>Para refletir:</strong> quando algo parece 'naturalmente assim', suspeite de uma ordem imaginada — e veja quem ela beneficia."
   }
  ]
 },
 "ch06-dinheiro": {
  "cards": [
   {
    "ic": "key",
    "t": "Confiança Intersubjetiva",
    "b": "O valor do dinheiro está na <strong>crença mútua</strong>: a mais universal e eficiente forma de confiança já inventada. Não confiamos no humano, mas no <strong>sistema</strong>.",
    "tip": "<strong>Modelo mental:</strong> quando estranhos cooperam sem se conhecer, o dinheiro é a ponte de confiança."
   },
   {
    "ic": "link",
    "t": "Conversor Universal",
    "b": "O dinheiro transforma <strong>tudo em tudo</strong> — terra em saúde, honra em comida — e estoca/transporta valor. Por isso é o <strong>maior unificador</strong> da humanidade.",
    "tip": "<strong>Como aplicar:</strong> o ouro liga economias que jamais se encontraram, só porque todos creem nele."
   },
   {
    "ic": "scale",
    "t": "O Lado Sombrio",
    "b": "O dinheiro corrói valores e laços locais que <strong>não se deixam quantificar</strong>. Tudo vira preço; a confiança no sistema pode minar a confiança nas pessoas.",
    "tip": "<strong>Para refletir:</strong> o que o dinheiro converte com eficiência, também tende a esvaziar de sentido."
   }
  ]
 },
 "ch07-imperios": {
  "cards": [
   {
    "ic": "layers",
    "t": "Motor da Fusão Cultural",
    "b": "O ciclo imperial: conquista → imposição de cultura → assimilação → a elite local adota a cultura imperial → surge uma <strong>cultura nova, sincrética</strong>, que sobrevive ao império.",
    "tip": "<strong>Modelo mental:</strong> pense no império como liquidificador cultural — tritura a diversidade e gera novas sínteses."
   },
   {
    "ic": "link",
    "t": "A Herança Inescapável",
    "b": "Rebeldes adotam os <strong>próprios valores do império</strong> para combatê-lo (direitos, autodeterminação, Estado-nação são ideias imperiais). Não há como 'voltar' a uma pureza pré-imperial.",
    "tip": "<strong>Para refletir:</strong> quando alguém invoca uma 'cultura pura e autêntica', desconfie — pureza cultural é quase sempre miragem."
   },
   {
    "ic": "target",
    "t": "A Visão Universalista",
    "b": "Muitos impérios se justificaram como projeto de <strong>civilizar/beneficiar a humanidade</strong> — ideologia que encobriu a exploração, mas também legou ideais universais.",
    "tip": "<strong>Como aplicar:</strong> julgar o império exige segurar as duas pontas — opressão real e produção de ideais universais."
   }
  ]
 },
 "ch08-religioes": {
  "cards": [
   {
    "ic": "mountain",
    "t": "Ordem Sobre-Humana",
    "b": "O que conta não é o 'deus', mas a <strong>função</strong>: uma ordem absoluta que sustenta normas e valores e confere a leis humanas a aparência de leis universais.",
    "tip": "<strong>Modelo mental:</strong> toda grande ordem social precisa de uma fonte de legitimidade 'acima dos humanos'."
   },
   {
    "ic": "wave",
    "t": "Universal e Missionária",
    "b": "Religiões locais cedem a religiões <strong>universais</strong> (válidas para todos) e <strong>missionárias</strong> (que querem converter todos) — outra grande força de unificação.",
    "tip": "<strong>Como aplicar:</strong> é a terceira ordem unificadora — dá legitimidade transcendente ao dinheiro e ao império."
   },
   {
    "ic": "person",
    "t": "O Humanismo como Fé",
    "b": "Ideologias modernas operam como religiões naturais. O <strong>humanismo</strong> cultua a 'humanidade' no lugar de Deus — ramos liberal (sacralidade do indivíduo), socialista e evolucionista.",
    "tip": "<strong>Para refletir:</strong> quando uma ideologia trata seus valores como absolutos e universais, leia-a como religião."
   }
  ]
 },
 "ch09-revolucao-cientifica": {
  "cards": [
   {
    "ic": "lens",
    "t": "Descoberta da Ignorância",
    "b": "Não foi uma 'revolução do conhecimento', mas da <strong>ignorância</strong>: a descoberta de que ignoramos as respostas mais importantes. As tradições antigas presumiam ter tudo no texto sagrado; a ciência institucionaliza a dúvida.",
    "tip": "<strong>Como aplicar:</strong> comece por admitir o que não sabe — o salto de poder vem de tratar a ignorância como ponto de partida."
   },
   {
    "ic": "target",
    "t": "Os 3 Pilares",
    "b": "(1) Disposição a <strong>admitir ignorância</strong>; (2) centralidade da <strong>observação e da matemática</strong>; (3) busca de <strong>novos poderes</strong> — teorias devem render tecnologias úteis.",
    "tip": "<strong>Modelo mental:</strong> avalie uma teoria pelo que ela permite fazer, não só pela verdade que contempla."
   },
   {
    "ic": "spark",
    "t": "Saber é Poder",
    "b": "O teste de uma teoria moderna não é a verdade pura, mas a <strong>capacidade de gerar poder</strong> e ferramentas. Ciência e tecnologia casam-se — nasce a ideia de progresso ilimitado.",
    "tip": "<strong>Para refletir:</strong> o mapa com 'espaços em branco' é a Revolução Científica em imagem — a ignorância como motor."
   }
  ]
 },
 "ch10-ciencia-imperio-capital": {
  "cards": [
   {
    "ic": "link",
    "t": "A Tríade em Feedback",
    "b": "Ciência fornece poder e mapas; o império fornece território e dados; o capital financia ambos e colhe lucros que reinvestem no ciclo. Um <strong>motor de feedback</strong> que disparou a expansão europeia.",
    "tip": "<strong>Modelo mental:</strong> em toda grande expansão moderna, ache o triângulo — quem conhece, quem controla, quem financia."
   },
   {
    "ic": "lens",
    "t": "Mentalidade Exploratória",
    "b": "O europeu admitia ignorância (há terras desconhecidas), queria preenchê-la e converter o saber em <strong>poder e lucro</strong>. Os impérios asiáticos sabiam tanto, mas não tinham essa fome.",
    "tip": "<strong>Para refletir:</strong> atitude vence dotação inicial — a fome de explorar superou o estoque de quem já era mais rico."
   },
   {
    "ic": "target",
    "t": "O 'Vazio no Mapa'",
    "b": "A descoberta da América como modelo: o <strong>espaço em branco</strong> preenchido por exploração financiada — protótipo do casamento entre curiosidade, ambição imperial e capital de risco.",
    "tip": "<strong>Como aplicar:</strong> a diferença não foi o estoque, foi a fome — e o motor de feedback que a sustentava."
   }
  ]
 },
 "ch11-capitalismo-credito": {
  "cards": [
   {
    "ic": "spiral",
    "t": "Crédito = Fé no Futuro",
    "b": "O crédito existe porque acreditamos que <strong>amanhã haverá mais riqueza</strong> que hoje. Sem essa fé, ninguém empresta para empreender; com ela, financia-se o que ainda não foi produzido.",
    "tip": "<strong>Modelo mental:</strong> a saúde de uma economia é, em parte, o quanto ela acredita no próprio amanhã."
   },
   {
    "ic": "steps",
    "t": "O Círculo Virtuoso",
    "b": "Crença no crescimento → crédito → investimento → crescimento real → mais crédito. A <strong>profecia que se autorrealiza</strong> — em contraste com economias que viam o bolo como fixo.",
    "tip": "<strong>Como aplicar:</strong> quando o crédito seca, foi a fé no crescimento que falhou — e o sistema entra em crise."
   },
   {
    "ic": "target",
    "t": "O Mandamento de Reinvestir",
    "b": "O capitalista não consome todo o lucro — <strong>reinveste na produção</strong>. Mas o imperativo de crescer sempre ignora externalidades: o sofrimento humano e ecológico fica fora da conta.",
    "tip": "<strong>Para refletir:</strong> quando o crescimento vira mandamento absoluto, pergunte o que fica de fora da conta."
   }
  ]
 },
 "ch12-felicidade": {
  "cards": [
   {
    "ic": "wave",
    "t": "O Teto Bioquímico",
    "b": "A felicidade gira em torno de um <strong>ponto de equilíbrio</strong> relativamente fixo. Conquistas dão picos breves; voltamos ao patamar de base — a 'esteira hedônica'.",
    "tip": "<strong>Modelo mental:</strong> mais poder não comprou mais felicidade — porque a química nivela os ganhos."
   },
   {
    "ic": "scale",
    "t": "Realidade ÷ Expectativas",
    "b": "Felicidade não é o que se tem, é a <strong>distância entre o que se tem e o que se espera</strong>. A abundância e a mídia inflam as expectativas — por isso o conforto moderno rende menos felicidade.",
    "tip": "<strong>Como aplicar:</strong> antes de buscar 'mais', examine suas expectativas — gerenciá-las muda mais que mudar as circunstâncias."
   },
   {
    "ic": "bulb",
    "t": "Sentido e o Anseio",
    "b": "Vidas duras podem ser felizes se percebidas como <strong>significativas</strong>. E a visão budista: a própria busca por sensações agradáveis é a raiz do sofrimento — a paz vem de <strong>largar o anseio</strong>.",
    "tip": "<strong>Para refletir:</strong> pergunte da vida pelo sentido, não só pelo prazer."
   }
  ]
 },
 "ch13-fim-do-homo-sapiens": {
  "cards": [
   {
    "ic": "spiral",
    "t": "Do Natural ao Design",
    "b": "Por 4 bilhões de anos a vida evoluiu por <strong>seleção natural</strong>; agora o sapiens pode dirigir a própria evolução — o <strong>design inteligente</strong>. É o fim de uma era biológica.",
    "tip": "<strong>Modelo mental:</strong> trate o aumento de poder como aumento de responsabilidade."
   },
   {
    "ic": "layers",
    "t": "Os 3 Caminhos",
    "b": "(1) <strong>Engenharia biológica</strong> (alterar genes/corpos); (2) <strong>engenharia ciborgue</strong> (fundir orgânico e inorgânico); (3) <strong>vida inorgânica / IA</strong> (seres que não dependem de matéria orgânica).",
    "tip": "<strong>Para refletir:</strong> o gargalo deixou de ser o poder — passou a ser o propósito."
   },
   {
    "ic": "fork",
    "t": "Poder × Propósito",
    "b": "Nunca fomos tão poderosos, mas seguimos insatisfeitos e irresponsáveis. A pergunta crucial não é o que <strong>podemos</strong> fazer, mas <strong>o que queremos nos tornar</strong> — e o que queremos querer.",
    "tip": "<strong>Citação-síntese:</strong> 'existe algo mais perigoso do que deuses insatisfeitos e irresponsáveis, que não sabem o que querem?'"
   }
  ]
 }
}
```
