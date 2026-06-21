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

# LIVRO PARA APROFUNDAR: O Milionário Mora ao Lado — Thomas J. Stanley & William D. Danko

**Subtítulo:** VISÃO GERAL · OS SEGREDOS SURPREENDENTES DOS RICOS DA AMÉRICA
**Ideia central:** Pesquisa empírica com milionários americanos revela um retrato que desmente o estereótipo: o rico de verdade é frugal e invisível — mora há décadas na mesma casa comum, dirige carro usado e é dono de um negócio sem glamour. Riqueza não é o que se gasta nem o que se aparenta; é o que se acumula e não se vê. Stanley e Danko destrincham os 7 fatores comuns de quem fica rico — e por que renda alta e patrimônio alto raramente moram na mesma pessoa.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-conheca-o-milionario` — CAPÍTULO 1: Conheça o Milionário ao Lado
- `ch02-frugal-frugal-frugal` — CAPÍTULO 2: Frugal, Frugal, Frugal
- `ch03-tempo-energia-dinheiro` — CAPÍTULO 3: Tempo, Energia e Dinheiro
- `ch04-voce-nao-e-o-que-dirige` — CAPÍTULO 4: Você Não É o que Dirige
- `ch05-assistencia-economica-externa` — CAPÍTULO 5: Assistência Econômica Externa
- `ch06-acao-afirmativa-em-familia` — CAPÍTULO 6: Ação Afirmativa em Família
- `ch07-ache-seu-nicho` — CAPÍTULO 7: Ache Seu Nicho
- `ch08-empregos-milionarios-x-herdeiros` — CAPÍTULO 8: Empregos — Milionários × Herdeiros

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-conheca-o-milionario": {
  "cards": [
   {
    "ic": "eye",
    "t": "O Milionário Invisível",
    "b": "O rico de verdade é <strong>indistinguível do vizinho de classe média</strong>: carro usado, casa antiga, terno de liquidação. Quem exibe símbolos de riqueza sem patrimônio é o '<em>grande chapéu, sem gado</em>' (Big Hat, No Cattle).",
    "tip": "<strong>Modelo mental:</strong> muito brilho na vitrine costuma indicar cofre vazio — o status exibido é sinal invertido."
   },
   {
    "ic": "scale",
    "t": "Renda ≠ Riqueza",
    "b": "<strong>Renda</strong> (income) é o fluxo que entra; <strong>riqueza</strong> (net worth) é o que sobrou e acumulou. São independentes — e frequentemente inversas. O placar do jogo é acumular, não faturar.",
    "tip": "<strong>Como aplicar:</strong> o profissional liberal que ganha muito e gasta tudo é UAW, não rico."
   },
   {
    "ic": "target",
    "t": "Fórmula da Riqueza Esperada",
    "b": "<strong>Idade × Renda Bruta Anual ÷ 10.</strong> Compare com o real: ≥ 2× = <strong>PAW</strong> (acumulador prodigioso); ~igual = AAW (médio); ≤ ½ = <strong>UAW</strong> (subacumulador / 'economicamente desajustado').",
    "tip": "<strong>Para refletir:</strong> alta renda + UAW = o dinheiro está vazando em algum lugar."
   },
   {
    "ic": "layers",
    "t": "Os 7 Fatores",
    "b": "Os acumuladores: 1) vivem abaixo das posses; 2) alocam tempo/energia/dinheiro com eficiência; 3) valorizam independência sobre status; 4) não foram sustentados pelos pais; 5) têm filhos autossuficientes; 6) miram o nicho; 7) <strong>escolheram a ocupação certa</strong>.",
    "tip": "<strong>Como aplicar:</strong> trate os 7 fatores como checklist de comportamento, não como sorte."
   }
  ]
 },
 "ch02-frugal-frugal-frugal": {
  "cards": [
   {
    "ic": "leaf",
    "t": "Frugalidade",
    "b": "Gastar consistentemente <strong>abaixo do que se ganha</strong> — o oposto do consumo conspícuo. É hábito de fundo, não dieta temporária: viva como se ganhasse menos e transforme a diferença em patrimônio investido.",
    "tip": "<strong>Como aplicar:</strong> cada real economizado vale mais que um real ganho — não paga imposto."
   },
   {
    "ic": "sword",
    "t": "Ataque × Defesa",
    "b": "<strong>Ataque</strong> = gerar renda; <strong>defesa</strong> = não deixá-la vazar (orçamento, frugalidade, planejamento). A riqueza vem de jogar <strong>boa defesa</strong> — o alicerce. Renda alta com defesa fraca = UAW.",
    "tip": "<strong>Modelo mental:</strong> dobrar a renda é difícil; cortar o desperdício está sob seu controle imediato. Comece pela defesa."
   },
   {
    "ic": "steps",
    "t": "Orçar para Enriquecer",
    "b": "PAW sabem exatamente quanto gastam por categoria; UAW não fazem ideia. O orçamento é o <strong>GPS do dinheiro</strong> — sem ele, dirige-se no escuro e culpa-se a estrada.",
    "tip": "<strong>Tell:</strong> 'ganho bem, não preciso orçar' é a receita clássica do UAW."
   }
  ]
 },
 "ch03-tempo-energia-dinheiro": {
  "cards": [
   {
    "ic": "clock",
    "t": "Alocação Eficiente",
    "b": "Os três recursos finitos — <strong>tempo, energia e dinheiro</strong> — viram patrimônio quando dirigidos ao planejamento. Não é falta de tempo: é escolha de para onde o tempo vai. O UAW tem o mesmo tempo e o gasta consumindo.",
    "tip": "<strong>Modelo mental:</strong> horas estudando dinheiro hoje são capital semente que rende patrimônio amanhã."
   },
   {
    "ic": "bulb",
    "t": "Planejar × Preocupar-se",
    "b": "PAW passam mais tempo <strong>planejando</strong> finanças; UAW passam mais tempo <strong>ansiosos</strong> com dinheiro sem agir. Plano sem ansiedade acumula; ansiedade sem plano só desperdiça energia.",
    "tip": "<strong>Para refletir:</strong> a preocupação não muda o patrimônio — o plano, sim."
   },
   {
    "ic": "key",
    "t": "Pague-se Primeiro",
    "b": "A regra de ouro: separar <strong>~15–20% da renda</strong> para investir <strong>antes</strong> de gastar o resto — não com o que sobra (que nunca sobra). A independência financeira, não o status, é a estrela-guia.",
    "tip": "<strong>Como aplicar:</strong> trate o investimento como conta fixa do início do mês, não como sobra eventual."
   }
  ]
 },
 "ch04-voce-nao-e-o-que-dirige": {
  "cards": [
   {
    "ic": "eye",
    "t": "O Teste do Carro",
    "b": "O veículo é o <strong>item de status mais visível</strong>; a escolha revela se a pessoa joga acumulação ou aparência. A maioria dos milionários dirige carros comuns, muitos usados — vários não compram um carro há anos.",
    "tip": "<strong>Tell:</strong> carro novo de luxo financiado é sinal forte de subacumulador, não de rico."
   },
   {
    "ic": "mask",
    "t": "Consumo Conspícuo",
    "b": "Gastar em <strong>símbolos visíveis</strong> (Veblen) em vez de em patrimônio invisível. A lealdade à marca é armadilha: paga-se o logo, não o transporte. O carro novo perde valor ao sair da loja — o oposto de um ativo.",
    "tip": "<strong>Modelo mental:</strong> depreciação é vazamento; comprar carro novo é despejar dinheiro num ativo que encolhe."
   },
   {
    "ic": "target",
    "t": "Comprar Valor, Não Marca",
    "b": "Os acumuladores compram <strong>usado de poucos anos, negociam agressivamente</strong> e mantêm o carro por muito tempo, sem lealdade a marca. O carro é ferramenta, não identidade.",
    "tip": "<strong>Para refletir:</strong> bem invisível (patrimônio) vale mais que bem visível (status). Você não é o que dirige."
   }
  ]
 },
 "ch05-assistencia-economica-externa": {
  "cards": [
   {
    "ic": "link",
    "t": "Assistência Econômica Externa",
    "b": "A <strong>EOC</strong> (Economic Outpatient Care): ajuda financeira contínua dos pais a filhos já adultos — mesada, entrada da casa, 'empréstimos' que não voltam. Parece amor, <strong>age como veneno</strong>: cria dependência crônica.",
    "tip": "<strong>Modelo mental:</strong> a EOC é anestésico que vicia — alivia agora e cria dependência depois."
   },
   {
    "ic": "wave",
    "t": "O Veneno do Subsídio",
    "b": "Quem recebe EOC <strong>consome mais, poupa menos, depende de crédito</strong> e acumula menos patrimônio do que quem nunca recebeu. O que os pais carregam, o filho deixa de exercitar — músculo atrofiado.",
    "tip": "<strong>Para refletir:</strong> a 'ajuda' frequentemente sustenta um padrão de vida acima da renda real do filho."
   },
   {
    "ic": "person",
    "t": "O Melhor Presente",
    "b": "O cheque pode prejudicar exatamente quem se quer proteger. O melhor presente é <strong>educação financeira, valores e exemplo</strong> — não dinheiro recorrente. Generosidade não é o mesmo que ajuda.",
    "tip": "<strong>Como aplicar:</strong> não sustente o padrão de vida do filho adulto; ensine-o a sustentá-lo sozinho."
   }
  ]
 },
 "ch06-acao-afirmativa-em-familia": {
  "cards": [
   {
    "ic": "scale",
    "t": "Ação Afirmativa em Família",
    "b": "O padrão em que <strong>mais dinheiro flui para o filho que menos prospera</strong>, reforçando a fraqueza que se queria socorrer. Premia-se o fracasso e penaliza-se o autossuficiente — cada resgate adia o ajuste que faria o filho crescer.",
    "tip": "<strong>Tell:</strong> pais sempre socorrendo o filho mais fraco perpetuam a dependência onde queriam curá-la."
   },
   {
    "ic": "person",
    "t": "Filhos Autossuficientes",
    "b": "O objetivo central: adultos que <strong>sustentam o próprio padrão sem subsídio</strong>. Ensine disciplina e frugalidade cedo; deixe o filho ganhar e gerir o próprio dinheiro; não resgate de toda consequência.",
    "tip": "<strong>Como aplicar:</strong> recompense autonomia e realização — não necessidade e ostentação."
   },
   {
    "ic": "book",
    "t": "Herança × Veneno",
    "b": "Capital sem competência produz dependentes, não acumuladores. <strong>Não anuncie nem antecipe heranças</strong>: o filho que se sabe herdeiro raramente desenvolve o músculo de acumular. Transmita as duas coisas — competência e capital.",
    "tip": "<strong>Modelo mental:</strong> ajuda é adubo seletivo — no esforço, fortalece; no filho fraco, perpetua a fraqueza."
   }
  ]
 },
 "ch07-ache-seu-nicho": {
  "cards": [
   {
    "ic": "target",
    "t": "Ache o Nicho",
    "b": "Identificar mercados em que a <strong>demanda dos ricos</strong> (ou dos que querem parecer ricos) cria oportunidade durável. Pergunte: 'quem tem dinheiro e o que ele compra ou precisa?' — e posicione-se ali.",
    "tip": "<strong>Modelo mental:</strong> nicho é o ângulo de ataque da renda; a defesa guarda, o nicho fatura."
   },
   {
    "ic": "layers",
    "t": "Vender aos Ricos",
    "b": "O afluente é <strong>cliente de alto valor</strong>; os profissionais que o atendem (contadores, advogados, consultores patrimoniais) prosperam junto. Poucos clientes certos valem mais que muitos clientes baratos.",
    "tip": "<strong>Como aplicar:</strong> em vez de competir no mercado de massa de baixa margem, sirva quem tem poder de compra."
   },
   {
    "ic": "link",
    "t": "Lucrar com a EOC do Mercado",
    "b": "Os filhos subsidiados <strong>gastam</strong> — e quem vende a eles acumula. O dinheiro que enfraquece o herdeiro enriquece o fornecedor: o gasto de um é o faturamento de outro (demanda derivada).",
    "tip": "<strong>Para refletir:</strong> o consumo dos outros pode ser exatamente a sua oportunidade de negócio."
   }
  ]
 },
 "ch08-empregos-milionarios-x-herdeiros": {
  "cards": [
   {
    "ic": "steps",
    "t": "Autofeitos × Herdeiros",
    "b": "A riqueza estudada é <strong>majoritariamente construída</strong> (self-made), não recebida. A herança ajuda menos do que se imagina e, sem disciplina, dissipa-se. Acumular é hábito construído, não sorte herdada.",
    "tip": "<strong>Para refletir:</strong> herança sem competência dissipa; competência sem herança acumula."
   },
   {
    "ic": "wrench",
    "t": "Autônomos × Empregados",
    "b": "Cerca de <strong>dois terços</strong> dos milionários americanos são autônomos ou donos de negócio. O autoemprego dá controle sobre renda, gasto e tempo — quem controla o placar controla a acumulação.",
    "tip": "<strong>Modelo mental:</strong> a vocação é alavanca: define não só quanto entra, mas quanto controle você tem sobre o que sobra."
   },
   {
    "ic": "book",
    "t": "A Vocação Certa",
    "b": "Campos '<strong>sem glamour</strong>' (manufatura, serviços, comércio especializado) produzem mais milionários discretos que carreiras de prestígio e alto consumo. Menos brilho social = menos pressão de consumo = mais margem para acumular.",
    "tip": "<strong>Tell:</strong> escolher a carreira pelo status, e não pela acumulação, costuma vir com pressão de consumo alta."
   }
  ]
 }
}
```
