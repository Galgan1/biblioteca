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

# LIVRO PARA APROFUNDAR: Comece pelo Porquê — Simon Sinek

**Subtítulo:** VISÃO GERAL · COMO GRANDES LÍDERES INSPIRAM A AGIR
**Ideia central:** As pessoas não compram o que você faz; compram por que você faz. Sinek mostra que líderes e marcas que inspiram pensam, agem e comunicam de dentro para fora — partem do Círculo Dourado (Porquê → Como → O Quê), apoiados na própria biologia da decisão. Inspiração constrói lealdade; manipulação só fecha a venda.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-o-circulo-dourado` — CAPÍTULOS 1-3: O Círculo Dourado
- `ch02-biologia-clareza-confianca` — CAPÍTULOS 4-6: Biologia, Clareza e Confiança
- `ch03-difusao-e-teste-do-aipo` — CAPÍTULOS 7-10: Difusão, o Aipo e a Comunicação
- `ch04-a-cisao-e-a-sucessao` — CAPÍTULOS 11-14: A Cisão e a Nova Competição

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-o-circulo-dourado": {
  "cards": [
   {
    "ic": "target",
    "t": "Os Três Anéis",
    "b": "<strong>O QUÊ</strong>: o produto/serviço — todos sabem o seu. <strong>COMO</strong>: os diferenciais e valores. <strong>PORQUÊ</strong>: a causa/crença pela qual você existe — <em>nunca</em> 'lucrar' (lucro é resultado).",
    "tip": "<strong>Como aplicar:</strong> escreva seu Porquê em uma frase. Se não cabe numa frase clara, ele ainda não está definido."
   },
   {
    "ic": "spiral",
    "t": "De Dentro para Fora",
    "b": "O discurso que inspira começa pela crença e termina no produto. O mesmo produto, na ordem certa, deixa de ser 'compre' e passa a ser desejo. <strong>Só muda a ordem</strong> — e muda tudo.",
    "tip": "<strong>Modelo mental:</strong> pessoas não compram o que você faz; compram <em>por que</em> você faz."
   },
   {
    "ic": "fork",
    "t": "Manipular × Inspirar",
    "b": "As 6 manipulações: <strong>preço, promoções, medo, aspiração, pressão dos pares, novidade</strong>. Funcionam, mas viciam e não criam lealdade. A inspiração nasce do Porquê.",
    "tip": "<strong>Para refletir:</strong> guerra de preço ensina o cliente a comprar só por preço — insustentável."
   },
   {
    "ic": "spark",
    "t": "O Exemplo Apple",
    "b": "'Em tudo que fazemos, desafiamos o status quo (Porquê). Fazemos isso com produtos lindos e simples (Como). E acontece que fazemos ótimos computadores (O Quê).' A mesma empresa — agora você quer comprar.",
    "tip": "<strong>Como aplicar:</strong> teste seu pitch — ele abre pela crença ou pelas características?"
   }
  ]
 },
 "ch02-biologia-clareza-confianca": {
  "cards": [
   {
    "ic": "spiral",
    "t": "O Cérebro Decide no Límbico",
    "b": "O <strong>neocórtex</strong> (O Quê) entende fatos e linguagem, mas não decide. O <strong>sistema límbico</strong> (Porquê/Como) governa sentimento, confiança e a decisão — e <em>não tem linguagem</em>. Daí o 'sinto que está certo'.",
    "tip": "<strong>Modelo mental:</strong> mais dados não vencem a falta de Porquê — a decisão é do coração."
   },
   {
    "ic": "steps",
    "t": "Clareza · Disciplina · Consistência",
    "b": "<strong>Clareza</strong> do Porquê (saber em palavras), <strong>disciplina</strong> do Como (valores viram <em>verbos</em>) e <strong>consistência</strong> do O Quê (tudo prova o Porquê). É o que gera autenticidade.",
    "tip": "<strong>Como aplicar:</strong> transforme cada valor em verbo — 'integridade' → 'fazer o certo mesmo quando custa'."
   },
   {
    "ic": "link",
    "t": "Confiança = Crença Compartilhada",
    "b": "Confiança não se ordena: surge quando os valores batem. Por isso, <strong>contrate por atitude/crença, treine a habilidade</strong> (Herb Kelleher, Southwest). Quem acredita entrega muito além do salário.",
    "tip": "<strong>Modelo mental:</strong> primeiro pergunte 'ele acredita no que acreditamos?', depois olhe o currículo."
   }
  ]
 },
 "ch03-difusao-e-teste-do-aipo": {
  "cards": [
   {
    "ic": "mountain",
    "t": "A Lei da Difusão da Inovação",
    "b": "Curva em sino: inovadores (2,5%), <strong>adotantes iniciais (13,5%)</strong>, maioria inicial (34%), maioria tardia (34%), retardatários (16%). Os primeiros 16% compram o seu <strong>Porquê</strong>.",
    "tip": "<strong>Como aplicar:</strong> mire os que já creem (esquerda da curva); não tente convencer a maioria primeiro."
   },
   {
    "ic": "pin",
    "t": "O Ponto de Inflexão",
    "b": "Não dá para alcançar o mercado de massa direto. Só após <strong>~15-18% de penetração</strong> a maioria segue. A TiVo falhou por comunicar <em>recursos</em> (O Quê), não crença (Porquê).",
    "tip": "<strong>Modelo mental:</strong> a maioria 'pega' a ideia de quem confia, não da propaganda."
   },
   {
    "ic": "leaf",
    "t": "O Teste do Aipo",
    "b": "Diante de várias 'boas ideias' ou conselhos, aceite <strong>só o que prova o seu Porquê</strong> e rejeite o resto, por lucrativo que pareça. Quem olha seu 'carrinho' lê sua crença só pela coerência.",
    "tip": "<strong>Como aplicar:</strong> 'boa ideia' não basta — tem de ser <em>coerente</em> com a crença."
   },
   {
    "ic": "bubble",
    "t": "Tenho um Sonho",
    "b": "Martin Luther King não disse 'tenho um plano' (O Quê), e sim '<strong>tenho um sonho</strong>' (Porquê). 250 mil foram por elas mesmas — pela própria crença. Símbolos só valem quando representam um Porquê.",
    "tip": "<strong>Modelo mental:</strong> dê às pessoas algo em que crer; elas espalham a mensagem como sua."
   }
  ]
 },
 "ch04-a-cisao-e-a-sucessao": {
  "cards": [
   {
    "ic": "gap",
    "t": "A Cisão do Porquê",
    "b": "Quando o sucesso escala, o foco migra do Porquê para o O Quê (métricas, preço). A crença se dilui e a manipulação volta. Distinga <strong>sucesso</strong> (atingir o O Quê) de <strong>realização</strong> (viver o Porquê).",
    "tip": "<strong>Modelo mental:</strong> faça o check-up — 'ainda sabemos por que existimos?'"
   },
   {
    "ic": "person",
    "t": "O Desafio da Sucessão",
    "b": "A Cisão se aprofunda quando o fundador sai: herdeiros recebem o negócio (O Quê), mas não a crença (Porquê). Sem ela, recorrem à manipulação e a cultura esfria (Walmart pós-Sam Walton).",
    "tip": "<strong>Como aplicar:</strong> forme sucessores como guardiães do Porquê, não só gestores do O Quê."
   },
   {
    "ic": "key",
    "t": "Descobrir o Porquê",
    "b": "O Porquê <strong>não se inventa, se descobre</strong> — olhando para trás, para a história e os valores que te formaram. Um Porquê de marketing soa falso e não passa no Teste do Aipo.",
    "tip": "<strong>Para refletir:</strong> 'o que sempre me moveu, mesmo sem recompensa?' — o padrão recorrente é o Porquê."
   },
   {
    "ic": "spark",
    "t": "A Nova Competição",
    "b": "Quem vive o Porquê <strong>compete contra si mesmo</strong>, não contra o rival. Os irmãos Wright voaram por uma causa; Langley, com mais verba e fama (O Quê), desistiu quando perdeu o ineditismo.",
    "tip": "<strong>Modelo mental:</strong> crença vence recurso — o Porquê sustenta quando dinheiro e fama acabam."
   }
  ]
 }
}
```
