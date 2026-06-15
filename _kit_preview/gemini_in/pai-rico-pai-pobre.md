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

# LIVRO PARA APROFUNDAR: Pai Rico, Pai Pobre — Robert T. Kiyosaki

**Subtítulo:** VISÃO GERAL · O QUE OS RICOS ENSINAM AOS FILHOS
**Ideia central:** Robert Kiyosaki cresceu entre dois pais: um instruído, professor e financeiramente conservador (o Pai Pobre), e o pai de um amigo, empreendedor que largou a escola mas dominava o jogo do dinheiro (o Pai Rico). Conselhos opostos, destinos opostos. A lição central: a escola ensina a trabalhar por dinheiro; os ricos aprendem a fazer o dinheiro trabalhar para eles — e isso começa por saber a diferença entre um ativo e um passivo.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-dois-pais` — CAPÍTULO 1: A Parábola dos Dois Pais
- `ch02-nao-trabalhar-por-dinheiro` — CAPÍTULO 2 (Lição 1): Os Ricos Não Trabalham por Dinheiro
- `ch03-ativo-passivo` — CAPÍTULO 3 (Lição 2): Alfabetização Financeira — Ativo vs. Passivo
- `ch04-cuide-do-seu-negocio` — CAPÍTULO 4 (Lição 3): Cuide do Seu Próprio Negócio
- `ch05-impostos-corporacoes` — CAPÍTULO 5 (Lição 4): Impostos & o Poder das Corporações
- `ch06-inventar-dinheiro` — CAPÍTULO 6 (Lição 5): Os Ricos Inventam Dinheiro
- `ch07-trabalhe-para-aprender` — CAPÍTULO 7 (Lição 6): Trabalhe para Aprender, Não pelo Dinheiro
- `ch08-cinco-obstaculos` — CAPÍTULO 8: Os 5 Obstáculos
- `ch09-pague-se-primeiro` — CAPÍTULO 9: Pague-se Primeiro & Hábitos
- `ch10-comecar` — CAPÍTULO 10: Como Começar

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-dois-pais": {
  "cards": [
   {
    "ic": "fork",
    "t": "Os Dois Pais",
    "b": "Dois conjuntos de crenças sobre dinheiro. O Pai Pobre: 'estude e arrume um emprego seguro'. O Pai Rico: 'aprenda a <strong>fazer o dinheiro trabalhar para você</strong>'. Conselhos opostos, destinos opostos.",
    "tip": "<strong>Como aplicar:</strong> a cada decisão, note qual 'voz' fala — a da segurança ou a do ativo."
   },
   {
    "ic": "lens",
    "t": "Acadêmico ≠ Financeiro",
    "b": "Ser bom na escola <strong>não ensina a lidar com dinheiro</strong>. Diploma e salário alto não bastam — o que decide é a alfabetização financeira.",
    "tip": "<strong>Cuidado:</strong> não aceite como verdade conselhos de quem nunca enriqueceu, por mais instruído que seja."
   },
   {
    "ic": "bulb",
    "t": "\"Como Posso Pagar?\"",
    "b": "O pobre diz '<strong>não posso pagar</strong>' (afirmação que fecha a mente). O rico pergunta '<strong>como posso pagar?</strong>' (pergunta que ativa a solução).",
    "tip": "<strong>Regra:</strong> troque a frase que paralisa pela pergunta que faz pensar."
   }
  ]
 },
 "ch02-nao-trabalhar-por-dinheiro": {
  "cards": [
   {
    "ic": "spiral",
    "t": "A Corrida dos Ratos",
    "b": "O ciclo acordar–trabalhar–pagar contas–repetir, em que <strong>cada aumento de salário vira mais consumo</strong>. Você corre cada vez mais rápido sem sair do lugar.",
    "tip": "<strong>Como aplicar:</strong> se o salário sobe junto com as despesas, você está na corrida — a saída é comprar ativos, não ganhar mais."
   },
   {
    "ic": "wave",
    "t": "Medo e Ganância",
    "b": "O motor da maioria: <strong>medo</strong> (de não ter, de não pagar contas) e <strong>ganância/desejo</strong> (do que o dinheiro compra). O salário chega e o desejo cria novas despesas.",
    "tip": "<strong>Cuidado:</strong> não decida por reação ao medo — reconheça a emoção antes de agir."
   },
   {
    "ic": "target",
    "t": "Trabalhe para Aprender",
    "b": "Faça o medo <strong>trabalhar a seu favor</strong>: a maioria deixa o medo dirigir; o rico o usa como combustível para aprender o jogo financeiro.",
    "tip": "<strong>Modelo mental:</strong> pergunte 'que oportunidade existe aqui?' em vez de 'quanto eu ganho?'."
   }
  ]
 },
 "ch03-ativo-passivo": {
  "cards": [
   {
    "ic": "scale",
    "t": "Ativo vs. Passivo (a Regra nº1)",
    "b": "<strong>Ativo</strong> põe dinheiro no seu bolso (renda entrante); <strong>passivo</strong> tira (despesa saindo). Antes de qualquer compra, pergunte: 'isto traz ou leva dinheiro?'.",
    "tip": "<strong>Como aplicar:</strong> só chame de investimento o que gera fluxo de caixa entrante."
   },
   {
    "ic": "steps",
    "t": "O Padrão de Fluxo de Caixa",
    "b": "Pobre: renda → todas as despesas. Classe média: renda → <strong>passivos disfarçados de ativos</strong>. Rico: renda → ativos → ativos geram mais renda.",
    "tip": "<strong>Modelo mental:</strong> leia o fluxo de caixa, não o preço nem a aparência."
   },
   {
    "ic": "gap",
    "t": "A Casa Não É um Ativo",
    "b": "Tese controversa do autor: a residência <strong>tira dinheiro do bolso</strong> (prestação, IPTU, manutenção), então é um <strong>passivo</strong> — só seria ativo se gerasse renda líquida.",
    "tip": "<strong>Cuidado:</strong> 'investir' tudo na casa própria pode travar a construção da coluna de ativos."
   }
  ]
 },
 "ch04-cuide-do-seu-negocio": {
  "cards": [
   {
    "ic": "layers",
    "t": "Emprego ≠ Negócio",
    "b": "O que você faz pelos outros (profissão) é diferente do que você <strong>possui</strong> (ativos). Mantenha a profissão como caixa, mas dedique uma parte fixa a construir a <strong>coluna de ativos</strong>.",
    "tip": "<strong>Como aplicar:</strong> trabalhe de dia, construa o seu negócio (ativos) à noite."
   },
   {
    "ic": "leaf",
    "t": "Construa a Coluna de Ativos",
    "b": "Acumule itens que geram renda e valorizam: ações, fundos, imóveis de renda, royalties, negócios sem sua presença. Comece pequeno e <strong>mantenha passivos enxutos</strong>.",
    "tip": "<strong>Regra:</strong> cada real não gasto em passivo pode virar ativo."
   },
   {
    "ic": "sword",
    "t": "Luxos por Último",
    "b": "O luxo é a <strong>recompensa que a coluna de ativos paga</strong>, não uma compra direta do salário. Subir o padrão antes da coluna sustentá-lo é trocar de coleira.",
    "tip": "<strong>Sinal de alerta:</strong> financiar luxos com salário em vez de com a renda dos ativos."
   }
  ]
 },
 "ch05-impostos-corporacoes": {
  "cards": [
   {
    "ic": "key",
    "t": "A Inversão da Ordem Tributária",
    "b": "Indivíduo (CLT): <strong>ganha → é taxado → gasta</strong> o líquido. Corporação: <strong>ganha → gasta (deduz) → é taxada</strong> sobre o lucro. A mesma receita rende mais bem organizada.",
    "tip": "<strong>Como aplicar:</strong> ao gerar renda própria, pense como empresa — deduzir despesas legítimas antes do imposto."
   },
   {
    "ic": "layers",
    "t": "As 4 Inteligências Financeiras",
    "b": "O conhecimento que protege e multiplica: <strong>contabilidade</strong> (ler números), <strong>investimento</strong>, <strong>conhecer mercados</strong> (oferta/demanda) e <strong>a lei</strong> (tributária e societária).",
    "tip": "<strong>Regra:</strong> a vantagem do rico é entender as regras melhor — não trapacear."
   },
   {
    "ic": "mask",
    "t": "Conhecimento, Não Trapaça",
    "b": "A corporação é um <strong>escudo legal</strong> que protege o patrimônio e permite deduções dentro da lei. É planejamento tributário, <strong>não sonegação</strong>.",
    "tip": "<strong>Cuidado:</strong> ignorar a estrutura jurídica deixa todo o ganho exposto ao imposto."
   }
  ]
 },
 "ch06-inventar-dinheiro": {
  "cards": [
   {
    "ic": "spark",
    "t": "Inteligência Financeira Inventa Dinheiro",
    "b": "A mente educada <strong>vê e cria oportunidades</strong> onde a maioria não vê. O limite à riqueza é mais a falta de coragem treinada do que a falta de capital.",
    "tip": "<strong>Como aplicar:</strong> estude o cenário (mercado, lei, números) até enxergar o ganho que ninguém vê."
   },
   {
    "ic": "mountain",
    "t": "Risco Calculado",
    "b": "Assumir risco <strong>com conhecimento</strong>, não fugir dele. 'Jogar sempre pelo seguro' é, no longo prazo, o maior risco.",
    "tip": "<strong>Regra:</strong> prepare-se, comece pequeno e aprenda com o erro — assim o medo de perder encolhe."
   },
   {
    "ic": "pivot",
    "t": "Os Dois Tipos de Investidor",
    "b": "(1) o que <strong>compra</strong> investimentos prontos; (2) o que <strong>monta</strong> o próprio investimento — encontra a oportunidade, estrutura o negócio e cria valor.",
    "tip": "<strong>Modelo mental:</strong> oportunidade é fabricada, não só encontrada — seja o investidor tipo 2."
   }
  ]
 },
 "ch07-trabalhe-para-aprender": {
  "cards": [
   {
    "ic": "book",
    "t": "Cada Emprego é uma Escola",
    "b": "Trate o trabalho como um <strong>curso pago</strong>: o salário é secundário, o repertório que você sai dele é o ativo. Aceite menos dinheiro por mais aprendizado quando ele constrói patrimônio futuro.",
    "tip": "<strong>Como aplicar:</strong> pergunte 'que habilidade ganho aqui?' antes de 'quanto paga?'."
   },
   {
    "ic": "link",
    "t": "Habilidades Amplas > Especialização",
    "b": "Domine um pouco de muitas áreas-chave: <strong>vendas e marketing</strong>, comunicação, gestão de pessoas, sistemas e fluxo de caixa. O especialista estreito fica preso ao emprego.",
    "tip": "<strong>Regra:</strong> generalista treinável monta e dirige negócios; especialista estreito depende da função."
   },
   {
    "ic": "target",
    "t": "Saber Vender é a Habilidade nº1",
    "b": "Nenhum bom produto ou ideia prospera <strong>sem venda</strong>. É a competência mais subestimada e mais decisiva para gerar renda própria.",
    "tip": "<strong>Sinal de alerta:</strong> trocar de emprego sempre pelo salário maior, acumulando dinheiro mas não habilidades."
   }
  ]
 },
 "ch08-cinco-obstaculos": {
  "cards": [
   {
    "ic": "wave",
    "t": "Medo & Cinismo",
    "b": "<strong>Medo</strong> de perder dinheiro (todo rico já perdeu — comece cedo e não paralise) e <strong>cinismo</strong> (as dúvidas e 'e se' dos Chicken Little que matam a ação).",
    "tip": "<strong>Como aplicar:</strong> erre pequeno e ignore os que só apontam o céu caindo."
   },
   {
    "ic": "clock",
    "t": "Preguiça & Maus Hábitos",
    "b": "<strong>Preguiça</strong> muitas vezes disfarçada de 'estou ocupado'; o antídoto é um pouco de ambição saudável. <strong>Mau hábito</strong> nº1: pagar a si mesmo por último.",
    "tip": "<strong>Regra:</strong> troque 'não posso' por 'como eu poderia ter isso?' — e pague-se primeiro."
   },
   {
    "ic": "mask",
    "t": "Arrogância (ego + ignorância)",
    "b": "Achar que sabe o que <strong>não sabe</strong> faz perder dinheiro. 'O que sei me faz dinheiro; o que não sei me faz perder.'",
    "tip": "<strong>Sinal de alerta:</strong> investir por ego sem admitir o que não entende — admitir a ignorância protege."
   }
  ]
 },
 "ch09-pague-se-primeiro": {
  "cards": [
   {
    "ic": "key",
    "t": "Pague-se Primeiro",
    "b": "No recebimento, destine uma parcela fixa à coluna de ativos <strong>antes</strong> de pagar contas. A <strong>primeira conta é você</strong>; trate o aporte como obrigação inadiável.",
    "tip": "<strong>Como aplicar:</strong> automatize o aporte no dia do salário, antes de qualquer boleto."
   },
   {
    "ic": "spark",
    "t": "A Pressão como Combustível",
    "b": "Resista a sacar dos investimentos para pagar contas. A tensão de ainda dever <strong>força a criatividade</strong> — vender mais, criar, cortar gastos.",
    "tip": "<strong>Modelo mental:</strong> a folga adormece; a pressão desperta."
   },
   {
    "ic": "steps",
    "t": "Autodisciplina",
    "b": "O poder de controle interno é o fator <strong>mais difícil e mais determinante</strong>. 'Com o que sobra' nunca sobra — por isso o aporte vem primeiro.",
    "tip": "<strong>Sinal de alerta:</strong> sacar dos ativos para cobrir contas mata o efeito do pague-se-primeiro."
   }
  ]
 },
 "ch10-comecar": {
  "cards": [
   {
    "ic": "mountain",
    "t": "Uma Razão Maior que a Realidade",
    "b": "Um <strong>porquê forte</strong> (combinação de querer e não-querer) sustenta a disciplina quando a motivação cai. Sem ele, o conhecimento não vira ação.",
    "tip": "<strong>Como aplicar:</strong> escreva seu porquê — ex.: liberdade de tempo, não depender de salário aos 60."
   },
   {
    "ic": "constellation",
    "t": "Poder da Escolha & da Associação",
    "b": "Invista primeiro em <strong>educação</strong> (livros, cursos, pessoas) e escolha bem as companhias: aprenda com quem tem dinheiro, não com quem só reclama dele.",
    "tip": "<strong>Modelo mental:</strong> você se torna o que estuda e com quem anda."
   },
   {
    "ic": "steps",
    "t": "Comece Pequeno, mas Comece",
    "b": "O conhecimento só vira riqueza quando vira <strong>ação</strong>. Compre um primeiro ativo real; use os ativos para comprar luxos; pague bons assessores.",
    "tip": "<strong>Sinal de alerta:</strong> acumular livros e cursos sem nunca fazer o primeiro investimento (paralisia por análise)."
   }
  ]
 }
}
```
