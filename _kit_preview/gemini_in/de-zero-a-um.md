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

# LIVRO PARA APROFUNDAR: De Zero a Um — Peter Thiel com Blake Masters

**Subtítulo:** VISÃO GERAL · COMO CONSTRUIR O FUTURO
**Ideia central:** O futuro valioso não vem de copiar o que existe (ir de 1 a n), mas de criar o que nunca existiu (ir de 0 a 1). Thiel mostra por que o monopólio criativo bate a concorrência, como encontrar o segredo que poucos veem, e quais as 7 perguntas que toda startup precisa acertar.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-o-desafio-do-futuro` — CAPÍTULO 1: O Desafio do Futuro
- `ch02-festa-como-em-1999` — CAPÍTULO 2: Festa como em 1999
- `ch03-todas-as-empresas-felizes-sao-diferentes` — CAPÍTULO 3: Todas as Empresas Felizes São Diferentes
- `ch04-a-ideologia-da-concorrencia` — CAPÍTULO 4: A Ideologia da Concorrência
- `ch05-vantagem-do-pioneiro` — CAPÍTULO 5: Vantagem do Pioneiro (Last Mover)
- `ch06-voce-nao-e-um-bilhete-de-loteria` — CAPÍTULO 6: Você Não É um Bilhete de Loteria
- `ch07-siga-o-dinheiro` — CAPÍTULO 7: Siga o Dinheiro
- `ch08-segredos` — CAPÍTULO 8: Segredos
- `ch09-fundacoes` — CAPÍTULO 9: Fundações
- `ch10-a-mecanica-da-mafia` — CAPÍTULO 10: A Mecânica da Máfia
- `ch11-se-voce-construir-eles-virao` — CAPÍTULO 11: Se Você Construir, Eles Virão?
- `ch12-o-homem-e-a-maquina` — CAPÍTULO 12: O Homem e a Máquina
- `ch13-vendo-verde` — CAPÍTULO 13: Vendo Verde
- `ch14-o-paradoxo-do-fundador` — CAPÍTULO 14: O Paradoxo do Fundador

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-o-desafio-do-futuro": {
  "cards": [
   {
    "ic": "spark",
    "t": "0→1 × 1→n",
    "b": "<strong>Vertical (0→1)</strong> = tecnologia, criar o que não existia. <strong>Horizontal (1→n)</strong> = globalização, copiar e espalhar. O mundo é finito: copiar sem inventar esgota; o futuro precisa do 0→1.",
    "tip": "<strong>Como aplicar:</strong> pergunte 'isto é invenção do novo (0→1) ou cópia melhorada (1→n)?'."
   },
   {
    "ic": "lens",
    "t": "A Pergunta Contrária",
    "b": "'Que verdade importante <strong>pouquíssimas pessoas concordam com você</strong>?' Boas respostas revelam o futuro que ninguém vê. A resposta certa é impopular — mas verdadeira.",
    "tip": "<strong>Modelo mental:</strong> o que é óbvio para você e estranho para os outros pode ser sua oportunidade."
   },
   {
    "ic": "wave",
    "t": "Tecnologia ≠ Globalização",
    "b": "Confundir progresso com globalização é o erro de base. Copiar o que funciona em escala não é criar o futuro — é só 1→n. <strong>Tecnologia, não consenso</strong>, cria valor radicalmente novo.",
    "tip": "<strong>Para refletir:</strong> a startup é o maior grupo que você convence de um plano para um futuro diferente."
   }
  ]
 },
 "ch02-festa-como-em-1999": {
  "cards": [
   {
    "ic": "scale",
    "t": "As 4 Lições Erradas",
    "b": "O crash ensinou o oposto do certo: (1) avançar passo a passo; (2) ser lean/flexível; (3) melhorar sobre o concorrente; (4) focar produto, não vendas. <strong>Lição de consenso = sinal de alerta.</strong>",
    "tip": "<strong>Como aplicar:</strong> para cada dogma pós-bolha, considere a verdade contrária."
   },
   {
    "ic": "spark",
    "t": "As 4 Verdades Opostas",
    "b": "(1) Melhor a ousadia que a trivialidade; (2) um plano ruim > nenhum plano; (3) mercados competitivos destroem lucro — fuja; (4) <strong>vendas importam tanto quanto o produto</strong>.",
    "tip": "<strong>Modelo mental:</strong> ousadia com tese é menos arriscada que trivialidade sem direção."
   }
  ]
 },
 "ch03-todas-as-empresas-felizes-sao-diferentes": {
  "cards": [
   {
    "ic": "target",
    "t": "Monopólio Criativo",
    "b": "<strong>'A concorrência é para perdedores.'</strong> O monopólio aqui não é cartel: é ser radicalmente melhor em algo. É a condição de qualquer negócio duradouro e lucrativo — só sobra lucro para quem escapa da concorrência.",
    "tip": "<strong>Como aplicar:</strong> 'esta empresa é única e dona do seu mercado, ou só mais uma de margens espremidas?'."
   },
   {
    "ic": "key",
    "t": "Criar × Capturar Valor",
    "b": "Criar valor não basta — é preciso <strong>reter</strong> parte dele. As companhias aéreas criam muito valor e capturam quase nada; o Google cria menos e captura uma fatia imensa. A diferença é monopólio × concorrência.",
    "tip": "<strong>Modelo mental:</strong> separe 'quanto valor gera para o mundo' de 'quanto fica para si'."
   },
   {
    "ic": "mask",
    "t": "As Duas Mentiras",
    "b": "O monopolista <strong>finge competir</strong> (para não chamar atenção); o não-monopolista <strong>inventa um nicho próprio</strong> (para parecer único). Suspeite das duas narrativas e leia o mercado por trás delas.",
    "tip": "<strong>Para refletir:</strong> definir o mercado como interseção estreita revela se você é único de verdade."
   }
  ]
 },
 "ch04-a-ideologia-da-concorrencia": {
  "cards": [
   {
    "ic": "sword",
    "t": "Concorrência como Ideologia",
    "b": "Somos ensinados a competir, e isso vira hábito mental que nos prende a brigas sem prêmio. A rivalidade leva a <strong>guerras que destroem valor</strong> para os dois lados.",
    "tip": "<strong>Como aplicar:</strong> 'estou lutando por este mercado porque ele vale, ou só porque há alguém para vencer?'."
   },
   {
    "ic": "fork",
    "t": "Guerra × Lucro",
    "b": "Quanto mais parecidos os rivais, mais feroz e inútil a disputa (eco de Girard: desejamos o que o outro deseja). Às vezes a jogada certa é <strong>não lutar</strong> — recuar ou fundir cria mais valor que vencer.",
    "tip": "<strong>Modelo mental:</strong> par de gêmeos brigando — guerra simbólica que custa mais do que rende."
   }
  ]
 },
 "ch05-vantagem-do-pioneiro": {
  "cards": [
   {
    "ic": "layers",
    "t": "As 4 Forças de Durabilidade",
    "b": "<strong>Tecnologia proprietária</strong> (~10× melhor, não marginal), <strong>efeitos de rede</strong> (mais usuários = mais valor), <strong>economias de escala</strong> e <strong>marca</strong>. Quanto mais presentes, mais defensável.",
    "tip": "<strong>Como aplicar:</strong> melhoria precisa ser de ordem de grandeza (10×), não de 20%."
   },
   {
    "ic": "clock",
    "t": "Vantagem do Último (Last Mover)",
    "b": "Melhor que ser o primeiro é fazer o <strong>grande avanço final</strong> e dominar por décadas. O pioneirismo é tática, não objetivo. Valor = soma dos fluxos de caixa futuros → durabilidade > faturamento de hoje.",
    "tip": "<strong>Modelo mental:</strong> árvore que dá fruto por décadas — o valor está nas safras futuras."
   },
   {
    "ic": "mountain",
    "t": "Comece Pequeno e Domine",
    "b": "Comece num <strong>mercado pequeno dominável</strong> (fatia grande de um nicho), depois expanda. Monopólio local antes de global — é mais fácil dominar uma interseção estreita.",
    "tip": "<strong>Para refletir:</strong> efeito de rede precisa ser valioso já para os primeiros usuários."
   }
  ]
 },
 "ch06-voce-nao-e-um-bilhete-de-loteria": {
  "cards": [
   {
    "ic": "steps",
    "t": "Definido × Indefinido",
    "b": "Quatro visões de futuro. O <strong>otimista-definido</strong> tem plano e esperança — é o motor do 0→1. O <strong>otimista-indefinido</strong> (Ocidente atual) acredita que melhora, mas sem plano; cultua 'manter opções abertas'.",
    "tip": "<strong>Como aplicar:</strong> há um plano específico (definido) e há esperança (otimista)?"
   },
   {
    "ic": "key",
    "t": "Sorte × Projeto",
    "b": "Tratar o sucesso como loteria desvaloriza o planejamento. Fundadores de 0→1 <strong>recusam a 'sorte'</strong> como explicação. 'Manter as opções abertas' é um custo, não uma virtude — sem compromisso, nada de 0→1 acontece.",
    "tip": "<strong>Para refletir:</strong> o futuro definido prefere quem constrói uma coisa a quem diversifica para tudo."
   }
  ]
 },
 "ch07-siga-o-dinheiro": {
  "cards": [
   {
    "ic": "spark",
    "t": "Lei de Potência (Power Law)",
    "b": "O melhor investimento de um fundo iguala ou supera <strong>todos os outros juntos</strong>. A distribuição é radicalmente desigual, não normal. Aposte em poucas coisas com potencial de serem enormes — não pulverize.",
    "tip": "<strong>Modelo mental:</strong> uma sequoia gigante entre arbustos — o resultado total é a sequoia."
   },
   {
    "ic": "target",
    "t": "A Regra do VC",
    "b": "Só invista no que tem potencial de <strong>devolver o fundo inteiro</strong> sozinho. Apostas medianas, mesmo lucrativas, não movem o ponteiro. A diversificação cega dilui justamente o vencedor que define o resultado.",
    "tip": "<strong>Para refletir:</strong> vale para a carreira — poucas apostas grandes batem muitas pequenas."
   }
  ]
 },
 "ch08-segredos": {
  "cards": [
   {
    "ic": "key",
    "t": "Segredos × Mistérios",
    "b": "Entre as verdades fáceis (convencionais) e as impossíveis (mistérios) estão os <strong>segredos</strong>: difíceis, mas descobríveis. São o material de 0→1 — a versão prática da pergunta contrária.",
    "tip": "<strong>Como aplicar:</strong> não confunda mistério (ninguém pode saber) com segredo (difícil, mas alcançável)."
   },
   {
    "ic": "lens",
    "t": "Onde Procurar",
    "b": "Há segredos de <strong>natureza</strong> (o mundo físico) e de <strong>pessoas</strong> (o que escondem ou não sabem de si). Procure em áreas negligenciadas, campos 'resolvidos' ou tabu — o segredo está onde ninguém olha.",
    "tip": "<strong>Para refletir:</strong> o 'fim dos segredos' é o mito que faz a cultura parar de procurá-los."
   }
  ]
 },
 "ch09-fundacoes": {
  "cards": [
   {
    "ic": "layers",
    "t": "Lei de Thiel",
    "b": "<strong>Uma startup estragada na fundação não pode ser consertada.</strong> Por isso as escolhas do 'dia zero' são as mais importantes: cofundadores com história, expectativas alinhadas antes de começar.",
    "tip": "<strong>Modelo mental:</strong> concreto fresco — molda-se uma vez; depois de curado, não se reforma."
   },
   {
    "ic": "scale",
    "t": "Propriedade · Posse · Controle",
    "b": "Quem detém o capital (<strong>propriedade</strong>), quem toca o dia a dia (<strong>posse</strong>) e quem governa as decisões (<strong>controle</strong>). O conflito surge quando os três se desencontram — alinhe-os cedo.",
    "tip": "<strong>Como aplicar:</strong> conselho enxuto (idealmente 3); maior = mais difícil decidir."
   },
   {
    "ic": "person",
    "t": "Dentro ou Fora",
    "b": "Todo envolvido deve estar <strong>em tempo integral e com capital</strong>, ou de fora — meios-termos (part-time, consultores no núcleo) corroem. Pague pouco em salário e muito em participação para alinhar o longo prazo.",
    "tip": "<strong>Para refletir:</strong> CEO mal pago é bom sinal — prova compromisso com o valor de longo prazo."
   }
  ]
 },
 "ch10-a-mecanica-da-mafia": {
  "cards": [
   {
    "ic": "constellation",
    "t": "A Empresa como Tribo",
    "b": "A melhor startup é uma 'seita leve': vínculo forte, missão compartilhada, identidade própria. <strong>Cultura não é perk</strong> — é quem você contrata e por quê. Recrutar é conspirar para uma missão, não preencher vagas.",
    "tip": "<strong>Como aplicar:</strong> 'por que trabalhar AQUI e não em qualquer lugar que pague igual?'."
   },
   {
    "ic": "fork",
    "t": "Mercenários × Zelotes",
    "b": "Evite os extremos: nem <strong>mercenários</strong> (só por dinheiro) nem <strong>zelotes</strong> (fanáticos cegos). Busque o meio — comprometidos com a missão e com as pessoas. E dê a cada um uma <strong>responsabilidade única</strong>.",
    "tip": "<strong>Para refletir:</strong> papéis sobrepostos criam guerra interna — a concorrência ideológica dentro de casa."
   }
  ]
 },
 "ch11-se-voce-construir-eles-virao": {
  "cards": [
   {
    "ic": "link",
    "t": "A Primazia da Distribuição",
    "b": "Vender e distribuir são tão decisivos quanto construir — e a melhor venda é <strong>invisível</strong> (parece que 'o produto se vendeu'). Trate distribuição como parte do design do negócio, não como detalhe final.",
    "tip": "<strong>Como aplicar:</strong> em geral, UM canal domina — ache-o e foque nele, não disperse."
   },
   {
    "ic": "scale",
    "t": "CLV × CAC",
    "b": "O valor do cliente (<strong>CLV</strong>) precisa superar com folga o custo de adquiri-lo (<strong>CAC</strong>). O método de venda segue o ticket: venda complexa (deals grandes) → vendedor → publicidade → viral (grátis).",
    "tip": "<strong>Modelo mental:</strong> viral exige coeficiente > 1 — cada usuário traz mais de um novo."
   },
   {
    "ic": "gap",
    "t": "A Zona Morta",
    "b": "Há uma 'zona morta' de ticket médio (~US$ 1.000): <strong>caro demais</strong> para vender só com anúncios, <strong>barato demais</strong> para sustentar um vendedor. Preso nela? Suba o ticket ou desça drasticamente.",
    "tip": "<strong>Para refletir:</strong> ficar no meio mata; o CAC come o CLV."
   }
  ]
 },
 "ch12-o-homem-e-a-maquina": {
  "cards": [
   {
    "ic": "link",
    "t": "Complemento × Substituto",
    "b": "A globalização vê o trabalho como competição (máquina × humano); a tecnologia de verdade vê <strong>complementaridade</strong>. Humanos decidem e dão sentido; máquinas processam e escalam. Os melhores produtos juntam os dois.",
    "tip": "<strong>Como aplicar:</strong> pergunte 'como a máquina amplia o humano?', não 'como o substitui?'."
   },
   {
    "ic": "person",
    "t": "O Centauro",
    "b": "Humano + máquina supera tanto o humano sozinho quanto a máquina sozinha. A máquina <strong>sinaliza</strong> padrões em volumes imensos; o humano <strong>julga</strong> os casos difíceis. Não compita com o computador — faça par com ele.",
    "tip": "<strong>Para refletir:</strong> ganhos reais vêm de máquinas que ajudam pessoas, não de uma superinteligência futura."
   }
  ]
 },
 "ch13-vendo-verde": {
  "cards": [
   {
    "ic": "target",
    "t": "As 7 Perguntas",
    "b": "<strong>(1) Engenharia</strong> (10×?) · <strong>(2) Timing</strong> (a hora certa?) · <strong>(3) Monopólio</strong> (nicho dominável?) · <strong>(4) Equipe</strong> (os sócios certos?) · <strong>(5) Distribuição</strong> (plano de venda?) · <strong>(6) Durabilidade</strong> (10–20 anos?) · <strong>(7) Segredo</strong> (oportunidade única?).",
    "tip": "<strong>Como aplicar:</strong> é preciso ir bem na MAIORIA — acertar uma ou duas não salva."
   },
   {
    "ic": "leaf",
    "t": "Setor da Moda ≠ Tese",
    "b": "O 'verde' estava na moda, mas moda <strong>não responde nenhuma das 7 perguntas</strong> — daí a quebra em massa. Painéis 'um pouco melhores' falham na engenharia (não é 10×), no timing, no monopólio e no segredo.",
    "tip": "<strong>Modelo mental:</strong> use as 7 perguntas como raio-X — poucas respostas fortes = bolha."
   }
  ]
 },
 "ch14-o-paradoxo-do-fundador": {
  "cards": [
   {
    "ic": "person",
    "t": "O Paradoxo do Fundador",
    "b": "Grandes fundadores acumulam traços <strong>opostos em grau extremo</strong> (gênio e ingênuo, querido e odiado, insider e outsider). Não são 'normais' — são outliers. A média não cria 0→1; o novo nasce do extremo.",
    "tip": "<strong>Para refletir:</strong> não tente fabricar um fundador 'equilibrado' — o valor está na excentricidade produtiva."
   },
   {
    "ic": "spark",
    "t": "Preservar o Pensamento de 0→1",
    "b": "Porque o futuro depende de poucos indivíduos singulares, a tarefa final é <strong>cultivar</strong> (não nivelar) os que veem segredos e criam o novo. O '1' decisivo vem de pessoas excepcionais, não de algoritmos.",
    "tip": "<strong>Modelo mental:</strong> resista à pressão de nivelar tudo à média — o progresso vertical vem do incomum."
   }
  ]
 }
}
```
