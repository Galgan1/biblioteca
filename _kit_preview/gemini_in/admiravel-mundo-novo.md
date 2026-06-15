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

# LIVRO PARA APROFUNDAR: Admirável Mundo Novo — Aldous Huxley

**Subtítulo:** VISÃO GERAL · A DISTOPIA DO PRAZER E O DIREITO DE SER INFELIZ
**Ideia central:** No ano 632 d.F. (depois de Ford), o Estado Mundial garante felicidade total — fabricando gente em frascos, dividindo-a em castas e condicionando-a a amar a servidão. Quando John, o Selvagem, reivindica o direito à dor, a Deus e à liberdade, descobre que não há lugar para o humano inteiro nesse paraíso.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-estado-mundial-divisa` — CAPÍTULO 1: O Estado Mundial e a Divisa
- `ch02-fabricacao-castas` — CAPÍTULO 2: A Fabricação de Gente e o Sistema de Castas
- `ch03-condicionamento-hipnopedia` — CAPÍTULO 3: O Condicionamento — Hipnopedia e Pavlov
- `ch04-soma-felicidade-quimica` — CAPÍTULO 4: Soma e a Felicidade Química
- `ch05-consumismo-tabu-solidao` — CAPÍTULO 5: Consumismo, Sexo e os Tabus
- `ch06-bernard-lenina-desajuste` — CAPÍTULO 6: Bernard e Lenina — o Desajuste e o Desejo
- `ch07-reserva-selvagem-john` — CAPÍTULO 7: A Reserva Selvagem — Linda, John e Shakespeare
- `ch08-debate-mond-john-fim` — CAPÍTULO 8: O Debate Mond × John e o Fim

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-estado-mundial-divisa": {
  "cards": [
   {
    "ic": "mountain",
    "t": "Estabilidade Como Deus",
    "b": "A <strong>estabilidade</strong> é o valor supremo: nada pode mudar, porque mudança é instabilidade. Tudo que poderia desestabilizar — paixão, família, arte, religião, solidão — foi engenheirado para fora da existência.",
    "tip": "<strong>Para refletir:</strong> estabilidade não é paz — é a morte da mudança e do risco que dão sentido à vida."
   },
   {
    "ic": "layers",
    "t": "O Lema Invertido",
    "b": "<em>Comunidade</em> sem indivíduos, <em>Identidade</em> imposta de fora, <em>Estabilidade</em> que é estagnação. <strong>Cada palavra do lema é uma palavra esvaziada do seu sentido</strong> — primeira pista da inversão de valores.",
    "tip": "<strong>Modelo mental:</strong> leia a felicidade do mundo como acusação, não como elogio."
   },
   {
    "ic": "eye",
    "t": "A Distopia ao Avesso",
    "b": "Não há tirano cruel nem repressão visível. O controle é <strong>prévio, biológico e psicológico</strong> — exercido sobre o desejo, não sobre a vontade. O abraço que sufoca é mais perfeito que a bota na cara.",
    "tip": "<strong>Contraste com 1984:</strong> Orwell temia quem proíbe livros; Huxley, que não houvesse ninguém querendo lê-los."
   }
  ]
 },
 "ch02-fabricacao-castas": {
  "cards": [
   {
    "ic": "steps",
    "t": "A Fábrica de Seres Humanos",
    "b": "O <strong>Processo Bokanovsky</strong> aplica a lógica fordista ao nascimento: produção em massa de gêmeos idênticos destinados à mesma fábrica, mesma máquina. <strong>A homogeneidade é garantia de estabilidade</strong>; a individualidade, um erro de qualidade.",
    "tip": "<strong>Modelo mental:</strong> padronizar pessoas é o passo lógico de uma civilização que padronizou tudo."
   },
   {
    "ic": "triangle",
    "t": "A Desigualdade Desejada",
    "b": "Épsilons são deliberadamente embrutecidos (privados de oxigênio no frasco) para serem felizes em tarefas que torturariam um Alfa. <strong>A injustiça mais profunda é a que a própria vítima foi feita para amar.</strong> Não há vítima consciente a libertar.",
    "tip": "<strong>Para refletir:</strong> 'eficiência' e 'estabilidade' podem justificar qualquer horror quando postas acima da dignidade da pessoa."
   },
   {
    "ic": "key",
    "t": "Casta é Destino Sem Escolha",
    "b": "Não há mobilidade porque não há acaso: cada um foi feito sob medida. <strong>O Bokanovsky é 'um dos maiores instrumentos da estabilidade social'</strong> — a frase mais perturbadora do capítulo.",
    "tip": "<strong>Modelo mental:</strong> a produção em massa aplicada ao ser humano elimina a individualidade na origem."
   }
  ]
 },
 "ch03-condicionamento-hipnopedia": {
  "cards": [
   {
    "ic": "wave",
    "t": "Condicionamento Neopavloviano",
    "b": "Bebês Deltas levam choques ao tocar livros e flores — para <strong>odiá-los para sempre</strong>. A aversão é implantada antes de qualquer escolha. O controle precede a consciência.",
    "tip": "<strong>Para refletir:</strong> a liberdade mais difícil de defender é a que você foi ensinado a não desejar."
   },
   {
    "ic": "bubble",
    "t": "Hipnopedia: o Slogan que Substitui o Pensamento",
    "b": "'Todo mundo pertence a todo mundo', 'fora é melhor que conserto', 'um grama na hora certa' — repetidos no sono até virarem convicções nunca questionadas. <strong>Slogan = pensamento terceirizado.</strong> A moral pré-mastigada é a morte da reflexão disfarçada de senso comum.",
    "tip": "<strong>Modelo mental:</strong> repetir não é pensar — identifique quando você reproduz slogans em vez de raciocinar."
   },
   {
    "ic": "mask",
    "t": "A Felicidade Implantada",
    "b": "O condicionamento 'funciona': os cidadãos são genuinamente felizes. A obra pergunta: <strong>uma felicidade que a pessoa não escolheu nem pode questionar ainda é felicidade?</strong> Ou apenas a ausência de quem poderia ser infeliz?",
    "tip": "<strong>Para refletir:</strong> educar pode ser libertar ou doutrinar; a diferença está em ensinar a pensar ou a obedecer sem pensar."
   }
  ]
 },
 "ch04-soma-felicidade-quimica": {
  "cards": [
   {
    "ic": "leaf",
    "t": "A Felicidade Como Algema",
    "b": "Sentiu tristeza, dúvida, raiva? Um grama de soma e o problema some. <strong>A felicidade química substitui a polícia, a propaganda e a repressão de uma só vez.</strong> A válvula que impede a revolta é o instrumento mais elegante do controle.",
    "tip": "<strong>Modelo mental:</strong> toda emoção negativa no mundo é um sintoma a ser medicado — nunca um sinal a ser ouvido."
   },
   {
    "ic": "spark",
    "t": "Anestesia, Não Plenitude",
    "b": "O soma não resolve conflitos — os apaga. <strong>Anestesiar toda dor é também anestesiar a profundidade</strong>: sem desconforto não há reflexão, arte nem mudança. A felicidade vira ausência de tudo que incomoda.",
    "tip": "<strong>Para refletir:</strong> a droga é a metáfora de qualquer entretenimento ou distração que neutraliza a inquietação humana."
   },
   {
    "ic": "eye",
    "t": "O Preço Político do Conforto",
    "b": "Um povo permanentemente contente nunca pergunta 'por quê?'. <strong>O soma é genial politicamente</strong>: elimina a indignação antes de ela se organizar. A tranquilidade fabricada é a forma mais eficaz de despolitização.",
    "tip": "<strong>Sinal de alerta:</strong> pergunte sempre 'o que este conforto está abafando?' A resposta revela o que o poder teme."
   }
  ]
 },
 "ch05-consumismo-tabu-solidao": {
  "cards": [
   {
    "ic": "target",
    "t": "Consumir é um Dever Cívico",
    "b": "'Fora é melhor que conserto': o descarte como virtude. Gastar é o que mantém a economia e, com ela, a estabilidade. <strong>O consumismo não é liberdade — é o canal aprovado que gasta a energia que poderia virar revolta.</strong>",
    "tip": "<strong>Para refletir:</strong> quando consumir se torna identidade, o sistema que se beneficia não precisa de propaganda."
   },
   {
    "ic": "person",
    "t": "'Todo Mundo Pertence a Todo Mundo'",
    "b": "O sexo é recreação sem vínculo; o amor exclusivo, a maternidade e a família são tabus. <strong>Laços fortes (amor, lealdade) são focos de instabilidade.</strong> O prazer sexual controlado gasta a tensão emocional antes que ela vire laço.",
    "tip": "<strong>Para refletir:</strong> substituir o amor pela recreação esvazia o vínculo humano mais profundo."
   },
   {
    "ic": "gap",
    "t": "O Tabu da Interioridade",
    "b": "Solidão, silêncio, arte que dói e religião foram banidos porque <strong>levam a pessoa para dentro de si — onde o Estado não alcança</strong>. O indivíduo deve estar sempre no grupo, ocupado e distraído.",
    "tip": "<strong>Modelo mental:</strong> tudo que gera interioridade é perigoso para o poder — porque a revolta nasce por dentro."
   }
  ]
 },
 "ch06-bernard-lenina-desajuste": {
  "cards": [
   {
    "ic": "pivot",
    "t": "Inadaptação Como Consciência",
    "b": "É justamente por não se encaixarem que Bernard e Helmholtz conseguem (parcialmente) ver o sistema de fora. <strong>Num mundo de cópias, a individualidade só sobrevive na inadaptação</strong> — e é tratada como doença.",
    "tip": "<strong>Para refletir:</strong> quem não se encaixa ainda pode pensar; quem se encaixa perfeitamente perdeu esse privilégio."
   },
   {
    "ic": "mask",
    "t": "Duas Rebeldias, Dois Testes",
    "b": "Bernard critica o sistema por <strong>ressentimento</strong> (quer aceitação); quando vira celebridade, abraça tudo que dizia odiar. Helmholtz critica por <strong>excesso de sentido</strong> — e aceita o exílio com serenidade. O teste é o que se faz quando o sistema recompensa.",
    "tip": "<strong>Modelo mental:</strong> rebeldia por ressentimento não é a mesma coisa que rebeldia por princípio."
   },
   {
    "ic": "person",
    "t": "Lenina: o Produto Perfeito",
    "b": "Bonita, alegre, promíscua por hábito, incapaz de entender o amor que John lhe oferecerá. Ela não é vilã — <strong>é o produto perfeito, e por isso trágica</strong>. O condicionamento eliminou o amor antes de ela poder escolhê-lo.",
    "tip": "<strong>Para refletir:</strong> o produto perfeito do sistema é incapaz de amar — o preço pago pela estabilidade."
   }
  ]
 },
 "ch07-reserva-selvagem-john": {
  "cards": [
   {
    "ic": "lens",
    "t": "O Olhar de Fora",
    "b": "John é o forasteiro necessário: <strong>o personagem que vê a distopia com olhos não-condicionados</strong>. Suas reações de horror são a régua humana — o que para ele parece monstruoso é a rotina civilizada. Use-as para medir o custo do sistema.",
    "tip": "<strong>Modelo mental:</strong> precisamos de um olhar de fora para enxergar a própria distopia."
   },
   {
    "ic": "book",
    "t": "Shakespeare Como Contramotivo",
    "b": "A linguagem da paixão, da tragédia e da grandeza humana — <strong>exatamente o que o Estado proibiu</strong>. John pensa e sente em Shakespeare; é sua alma e sua condenação. A grande literatura é perigosa para o poder porque mantém vivas a paixão e a profundidade.",
    "tip": "<strong>Para refletir:</strong> arte que dói é perigosa porque dá sentido ao sofrimento — e sentido ao sofrimento é o começo da resistência."
   },
   {
    "ic": "fork",
    "t": "A Reserva Não é o Paraíso",
    "b": "Huxley a mostra suja, cruel e supersticiosa. <strong>A obra recusa a falsa escolha tecnologia má × natureza boa.</strong> O problema não é a tecnologia — é a perda do humano em qualquer extremo. John idealiza Londres à distância; ao chegar, desilude-se.",
    "tip": "<strong>Modelo mental:</strong> 'ó admirável mundo novo' — o deslumbramento que vira ironia trágica."
   }
  ]
 },
 "ch08-debate-mond-john-fim": {
  "cards": [
   {
    "ic": "scale",
    "t": "A Grande Troca",
    "b": "Mond admite: <strong>trocaram verdade, beleza e liberdade por conforto e estabilidade</strong>. Arte, ciência verdadeira e Deus foram sacrificados porque ameaçavam a felicidade coletiva. O defensor da distopia é lúcido — isso torna o debate mais perturbador, não menos.",
    "tip": "<strong>Modelo mental:</strong> Mond não é caricatura — dê os melhores argumentos do sistema a sério; só então os derrote por dentro."
   },
   {
    "ic": "mountain",
    "t": "'O Direito de Ser Infeliz'",
    "b": "John recusa o paraíso inteiro: quer Deus, poesia, perigo, liberdade, bondade, pecado — <strong>e o direito de envelhecer, adoecer, temer e sofrer</strong>. Felicidade sem isso, diz, não vale ser vivida. A reivindicação mais radical do livro.",
    "tip": "<strong>Para refletir:</strong> sofrimento e dificuldade não são apenas males a abolir — são parte do que dá sentido e dignidade à vida."
   },
   {
    "ic": "gap",
    "t": "O Fim Trágico Como Tese",
    "b": "John não consegue viver nem no Estado nem fora dele; sua autoaniquilação é o veredito de que <strong>a civilização do prazer não tem como conviver com a alma humana</strong>. O suicídio é o impasse — não uma solução, mas um aviso.",
    "tip": "<strong>Para refletir:</strong> a distopia mais perigosa pode ser a que nos dá tudo que pedimos e, em troca, tira tudo que somos — sem que percebamos."
   }
  ]
 }
}
```
