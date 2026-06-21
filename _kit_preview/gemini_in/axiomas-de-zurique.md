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

# LIVRO PARA APROFUNDAR: Os Axiomas de Zurique — Max Gunther

**Subtítulo:** VISÃO GERAL · A SABEDORIA ESPECULATIVA DOS BANQUEIROS SUÍÇOS
**Ideia central:** Doze regras destiladas da experiência de banqueiros e investidores suíços para quem aceita arriscar a fim de enriquecer. Gunther inverte o senso comum: a preocupação é saúde, o lucro deve ser realizado cedo demais e a posição perdedora deve ser abandonada sem reza. O inimigo nunca é o risco — é a própria emoção (ganância, esperança, orgulho, manada).

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-risco-e-ganancia` — CAPÍTULO 1: O Risco e a Ganância (1º e 2º Axiomas)
- `ch02-esperanca-e-mobilidade` — CAPÍTULO 2: A Esperança e a Mobilidade (3º e 6º Axiomas)
- `ch03-previsoes-padroes-planejamento` — CAPÍTULO 3: Previsões, Padrões e Planejamento (4º, 5º e 12º Axiomas)
- `ch04-intuicao-e-ocultismo` — CAPÍTULO 4: A Intuição e o Ocultismo (7º e 8º Axiomas)
- `ch05-otimismo-consenso-teimosia` — CAPÍTULO 5: Otimismo, Consenso e Teimosia (9º, 10º e 11º Axiomas)
- `ch06-espirito-especulativo-axiomas-menores` — CAPÍTULO 6: O Espírito Especulativo e os Axiomas Menores

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-risco-e-ganancia": {
  "cards": [
   {
    "ic": "spark",
    "t": "1º Axioma — Do Risco",
    "b": "<strong>'A preocupação não é doença, mas sinal de saúde.'</strong> Se você não está preocupado, não está arriscando o suficiente. O desconforto controlado é o pedágio do enriquecimento, não um erro.",
    "tip": "<strong>Como aplicar:</strong> aposte um valor que importe — grande o bastante para que ganhar mude algo e perder doa."
   },
   {
    "ic": "layers",
    "t": "Apostas Significativas",
    "b": "Diversificar demais <strong>pulveriza o ganho</strong>. Cada aposta deve ser grande o suficiente para fazer diferença. 'Segurança' que espalha o dinheiro em apostas mínimas só garante a mediocridade do resultado.",
    "tip": "<strong>Cuidado:</strong> 'significativo' não é irresponsável — é o que dói, não o que arruína."
   },
   {
    "ic": "target",
    "t": "2º Axioma — Da Ganância",
    "b": "<strong>'Realize o lucro sempre cedo demais.'</strong> Decida de antemão quanto quer ganhar e, ao chegar lá, saia — mesmo que pareça que 'ainda vai subir'. A ganância te mantém na mesa tempo demais.",
    "tip": "<strong>Modelo mental:</strong> o lucro é um trem do qual você desce uma estação antes do fim — perde-se um pouco, mas nunca se descarrila."
   },
   {
    "ic": "scale",
    "t": "Não Espere o Topo",
    "b": "Tentar vender no pico é a forma mais comum de <strong>transformar lucro em prejuízo</strong>. Ninguém acerta o topo de propósito; o alvo de ganho é fixado a frio, antes de entrar, não no calor da euforia.",
    "tip": "<strong>Para refletir:</strong> a ganância sussurra 'só mais um pouco' — é ela que enche o caixa do cassino."
   }
  ]
 },
 "ch02-esperanca-e-mobilidade": {
  "cards": [
   {
    "ic": "wave",
    "t": "3º Axioma — Da Esperança",
    "b": "<strong>'Quando o barco começa a afundar, não reze. Pule.'</strong> Aceite pequenas perdas rapidamente para proteger o capital; não espere uma reviravolta que talvez não venha.",
    "tip": "<strong>Como aplicar:</strong> corte a perda enquanto é pequena — muitas perdas pequenas são o custo normal do jogo."
   },
   {
    "ic": "steps",
    "t": "Perdas Pequenas, com um Sorriso",
    "b": "Pequenas perdas são <strong>esperadas</strong> — espere ter muitas. Segurar a perdedora 'para sair no zero a zero' é o erro que transforma perda pequena em catástrofe.",
    "tip": "<strong>Modelo mental:</strong> a perda pequena é uma vacina — uma dose de dor que evita a doença grave."
   },
   {
    "ic": "leaf",
    "t": "6º Axioma — Da Mobilidade",
    "b": "<strong>'Evite lançar raízes. Elas impedem o movimento.'</strong> Não se apegue a um investimento; o que prende é o sentimentalismo, a lealdade e a inércia. Trate cada posição como provisória.",
    "tip": "<strong>Modelo mental:</strong> seu capital é água, não terra — deve fluir para onde rende mais."
   },
   {
    "ic": "link",
    "t": "Não Ame o Ativo",
    "b": "Apego sentimental ('é a minha ação') custa <strong>mobilidade e dinheiro</strong>. O mercado não retribui afeto. E não recuse a boa oportunidade só porque ela é nova e desconhecida.",
    "tip": "<strong>Para refletir:</strong> 'torcer' por uma posição é confissão de que a razão já mandou sair."
   }
  ]
 },
 "ch03-previsoes-padroes-planejamento": {
  "cards": [
   {
    "ic": "eye",
    "t": "4º Axioma — Das Previsões",
    "b": "<strong>'O comportamento humano não pode ser previsto.'</strong> Os preços movem-se por decisões humanas em massa — imprevisíveis. Desconfie de quem afirma conhecer o futuro do mercado.",
    "tip": "<strong>Como aplicar:</strong> trate toda previsão como opinião, não como fato; aja por gestão de risco, não por adivinhação."
   },
   {
    "ic": "constellation",
    "t": "5º Axioma — Dos Padrões",
    "b": "<strong>'O caos não é perigoso até começar a parecer ordenado.'</strong> O perigo é acreditar que se descobriu uma ordem onde só há acaso. Padrões aparentes são, em sua maioria, coincidência.",
    "tip": "<strong>Modelo mental:</strong> todo 'padrão infalível' é uma constelação — estrelas reais, figura imaginada por nós."
   },
   {
    "ic": "book",
    "t": "A Armadilha do Historiador",
    "b": "Supor que, porque algo se repetiu, vai se repetir. O <strong>passado não obriga o futuro</strong> e correlação não é causa. O mercado não tem memória nem obrigação de repetir.",
    "tip": "<strong>Cuidado:</strong> operar por padrões de gráfico como se fossem leis é ler ordem no que é ruído."
   },
   {
    "ic": "steps",
    "t": "12º Axioma — Do Planejamento",
    "b": "<strong>'Planos de longo prazo geram a crença perigosa de que o futuro está sob controle.'</strong> Eles ancoram você a decisões tomadas com informação velha.",
    "tip": "<strong>Modelo mental:</strong> o plano de longo prazo é bússola, não trilho — indica a direção, não prende ao caminho."
   }
  ]
 },
 "ch04-intuicao-e-ocultismo": {
  "cards": [
   {
    "ic": "bulb",
    "t": "7º Axioma — Da Intuição",
    "b": "<strong>'Um palpite pode ser confiado se puder ser explicado.'</strong> A intuição é conhecimento real registrado na mente, mais rápido que o raciocínio consciente — não é magia.",
    "tip": "<strong>Como aplicar:</strong> antes de agir, pergunte 'que informação real está por trás disso?'. Rastreável = confiável; sem base = desejo disfarçado."
   },
   {
    "ic": "gap",
    "t": "Palpite × Esperança",
    "b": "O palpite confiável vem de <strong>dados</strong>; a esperança vem do <strong>medo de perder</strong>. Saiba distinguir: o palpite verdadeiro informa, o falso só repete o que você quer que aconteça.",
    "tip": "<strong>Para refletir:</strong> a intuição é testemunha — só vale no tribunal se disser de onde tirou o que sabe."
   },
   {
    "ic": "target",
    "t": "8º Axioma — Do Ocultismo",
    "b": "<strong>'É improvável que o desígnio de Deus para o universo inclua deixar você rico.'</strong> Não atribua resultados a sorte mística, sinais, astros ou superstição. Separe fé (vida) de finanças (razão e risco).",
    "tip": "<strong>Teste do astrólogo rico:</strong> se a astrologia previsse o mercado, os astrólogos já seriam ricos — não são."
   },
   {
    "ic": "key",
    "t": "Superstição sem Atrapalhar",
    "b": "Rituais inofensivos podem ser <strong>divertidos</strong> — desde que não substituam o ato de pensar. Terceirizar a decisão financeira ao sobrenatural é o erro; o pé-de-coelho dá conforto, nunca previsão.",
    "tip": "<strong>Modelo mental:</strong> decisão financeira responde só a evidência e risco, não a devoção."
   }
  ]
 },
 "ch05-otimismo-consenso-teimosia": {
  "cards": [
   {
    "ic": "scale",
    "t": "9º Axioma — Otimismo × Confiança",
    "b": "<strong>'Otimismo é esperar o melhor; confiança é saber como você lidará com o pior.'</strong> Nunca faça uma jogada por mero otimismo. Só entre quando tiver um plano para o cenário ruim.",
    "tip": "<strong>Como aplicar:</strong> confiança = ter a saída pronta (onde sai, quanto perde); otimismo = só torcer."
   },
   {
    "ic": "person",
    "t": "10º Axioma — Do Consenso",
    "b": "<strong>'Ignore a opinião da maioria. Ela provavelmente está errada.'</strong> Quando todos concordam para onde o mercado vai, o movimento já aconteceu — já está no preço. A manada erra junto.",
    "tip": "<strong>Modelo mental:</strong> quando o táxi, o vizinho e o jornal dizem a mesma coisa, trate como sinal de saída, não de entrada."
   },
   {
    "ic": "pivot",
    "t": "11º Axioma — Da Teimosia",
    "b": "<strong>'Se não deu certo, não insista para recuperar.'</strong> Não persista numa aposta perdedora por orgulho ou para 'se vingar' do prejuízo. O dinheiro perdido não volta por persistência (custo afundado).",
    "tip": "<strong>Para refletir:</strong> a posição perdedora é um ex-relacionamento — insistir por orgulho só aprofunda o prejuízo."
   },
   {
    "ic": "fork",
    "t": "Média para Baixo é Teimosia",
    "b": "Comprar mais de uma ação que cai para 'baixar a média' costuma ser <strong>teimosia disfarçada de estratégia</strong>. Avalie cada decisão isoladamente: 'compraria isto hoje, sem o histórico?'",
    "tip": "<strong>Cuidado:</strong> não se apaixone por um investimento — ele não sabe que você existe."
   }
  ]
 },
 "ch06-espirito-especulativo-axiomas-menores": {
  "cards": [
   {
    "ic": "spark",
    "t": "A Atitude Especulativa",
    "b": "A vida pede que se arrisque para enriquecer; a <strong>mediocridade vem da fuga ao risco</strong>, não do risco em si. Especular conscientemente é mais sábio que 'investir com segurança' e ficar para trás.",
    "tip": "<strong>Modelo mental:</strong> a 'segurança' total que garante a mediocridade é, ela mesma, um risco disfarçado."
   },
   {
    "ic": "layers",
    "t": "Os 12 Axiomas como um Corpo",
    "b": "Não são dicas avulsas: <strong>se equilibram entre si</strong>. Cortar perdas (3º) mas teimar depois (11º) anula o sistema. Pilotar bem é lê-los juntos — risco, ganância, esperança, previsões, padrões, mobilidade, intuição, ocultismo, otimismo, consenso, teimosia, planejamento.",
    "tip": "<strong>Modelo mental:</strong> os axiomas são um cockpit — cada um é um instrumento; vence quem os lê em conjunto."
   },
   {
    "ic": "eye",
    "t": "Disciplina sobre Emoção",
    "b": "O inimigo número um é a <strong>própria emoção</strong>: ganância, esperança, orgulho, euforia da manada. Dominado o emocional, as regras se cumprem sozinhas. Os axiomas menores são as regras táticas que operacionalizam os grandes.",
    "tip": "<strong>Para refletir:</strong> enriquecer importa pela liberdade que dá, não pelo acúmulo em si."
   }
  ]
 }
}
```
