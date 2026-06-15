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

# LIVRO PARA APROFUNDAR: ? — ?

**Subtítulo:** —
**Ideia central:** —

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-sobrevivencia` — CAPÍTULO I: Sobrevivência e as Raízes da Não Assertividade
- `ch02-direito-primario` — CAPÍTULO II: O Direito Primário e Como Somos Manipulados
- `ch03-dez-direitos` — CAPÍTULO III: Os Dez Direitos Assertivos
- `ch04-disco-riscado` — CAPÍTULO IV: Persistência — Disco Riscado e Acordo Viável
- `ch05-conversa-assertiva` — CAPÍTULO V: Conversa Assertiva — Informação Gratuita e Autorrevelação
- `ch06-lidar-com-critica` — CAPÍTULO VI: Lidando com a Crítica — Banco de Névoa e Asserção Negativa
- `ch07-interrogacao-negativa` — CAPÍTULO VII: Estimulando o Outro — Interrogação Negativa
- `ch08-situacoes-comerciais` — CAPÍTULO VIII: Situações Comerciais — Onde Há Dinheiro Envolvido
- `ch09-situacoes-autoridade` — CAPÍTULO IX: Situações de Autoridade — Supervisão e Especialização
- `ch10-situacoes-iguais` — CAPÍTULO X: Situações entre Iguais — Amigos, Vizinhos, Família
- `ch11-desejos-sexuais` — CAPÍTULO XI: Afirmar os Desejos Sexuais — e a Questão Social

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-sobrevivencia": {
  "cards": [
   {
    "ic": "fork",
    "t": "Luta, Fuga ou Palavra",
    "b": "As três respostas ao conflito. Luta (agressão) e fuga (evitação) são <strong>reflexos primitivos de sobrevivência</strong>; a solução verbal é a alternativa humana e eficaz. Troque o reflexo de atacar ou se retirar por um enfrentamento <strong>calmo e persistente</strong>.",
    "tip": "<strong>Modelo mental:</strong> luta e fuga são o réptil que sobrou; a assertividade é o córtex fazendo o que só o humano consegue."
   },
   {
    "ic": "sword",
    "t": "As 3 Alavancas Emocionais",
    "b": "Como a criança — e depois o adulto — fica manipulável: <strong>Ansiedade</strong> (“se não fizer X, algo ruim acontece”), <strong>Ignorância</strong> (“você não sabe o bastante, deixe a autoridade decidir”) e <strong>Culpa</strong> (“se fizer X, você é mau”). O “me sinto culpado” do título é esta última.",
    "tip": "<strong>Sinal de alerta:</strong> uma onda súbita de culpa, ansiedade ou autodúvida num conflito é uma alavanca sendo puxada — não informação sobre a realidade."
   },
   {
    "ic": "mask",
    "t": "O que é Manipulação",
    "b": "Qualquer tentativa indireta de controlar seu comportamento <strong>mexendo nas suas emoções</strong>, em vez de declarar um desejo às claras. Os pais <em>podem</em> impor limites sem gerar ansiedade, ignorância ou culpa — a maioria não o faz, criando adultos passivos e manipuláveis.",
    "tip": "<strong>Como aplicar:</strong> a não assertividade é aprendida; logo, pode ser desaprendida."
   },
   {
    "ic": "scale",
    "t": "O Placar é o Autorrespeito",
    "b": "O ganho da assertividade é interno: o <strong>autorrespeito</strong>, preservado mesmo quando você não alcança o objetivo material. Conseguir o que quer é um bônus frequente — <strong>não a medida do sucesso</strong>.",
    "tip": "<strong>Regra:</strong> tentar nunca desagradar ninguém garante manipulação. O conflito não se evita; só se escolhe a resposta."
   }
  ]
 },
 "ch02-direito-primario": {
  "cards": [
   {
    "ic": "target",
    "t": "Você é o Seu Juiz (Direito I)",
    "b": "“Você tem o direito de julgar seu próprio comportamento, pensamentos e emoções, e de assumir a responsabilidade por sua iniciativa e consequências.” Você pode ouvir os outros, mas <strong>o veredito sobre você é seu</strong>. Todos os demais direitos derivam deste.",
    "tip": "<strong>Como aplicar:</strong> quando ouvir “você deveria”, traduza para “<em>eu</em> preferiria que você…” — devolvendo a frase a um mero desejo, que você aceita ou recusa."
   },
   {
    "ic": "book",
    "t": "A Estrutura Externa",
    "b": "A ferramenta básica do manipulador: invocar <strong>regras, normas, lógica</strong> ou “o jeito que as coisas se fazem” como se isso decidisse seu comportamento por você (“todo mundo sabe que você deveria…”). Você não é obrigado a viver por estruturas que não aceitou.",
    "tip": "<strong>Sinal de alerta:</strong> um argumento “lógico” sobre o que você deveria fazer ainda é só a preferência de outra pessoa fantasiada."
   },
   {
    "ic": "fork",
    "t": "Os 3 Tipos de Interação",
    "b": "Para saber quanto pode se impor: <strong>Comercial</strong> (troca explícita; contratos prévios obrigam; menor margem); <strong>Autoridade</strong> (poder legítimo só sobre uma área definida, não sobre você como pessoa); <strong>Igual</strong> (sem estrutura externa; assertividade plena).",
    "tip": "<strong>Regra:</strong> classifique a interação antes de reagir — a margem cresce de comercial → autoridade → igual."
   },
   {
    "ic": "sword",
    "t": "Ferramentas Amorais",
    "b": "As habilidades assertivas são <strong>amorais</strong> — como dirigir um carro, servem para o bem ou para o mal. Ser seu próprio juiz significa que <strong>você responde pelo uso</strong> que faz delas.",
    "tip": "<strong>Cuidado:</strong> a assertividade não derruba um contrato prévio genuíno (o pneu já rodado) — tentar parece tolice."
   }
  ]
 },
 "ch03-dez-direitos": {
  "cards": [
   {
    "ic": "book",
    "t": "A Carta de Direitos Assertivos",
    "b": "Os dez direitos — cada um anula um “deveria” manipulativo:",
    "tip": "<strong>Como aplicar:</strong> sob pressão, pergunte em silêncio “qual direito está sendo negado aqui?”. Nomeá-lo vira posição clara."
   },
   {
    "ic": "target",
    "t": "Os Dois Mais Potentes",
    "b": "<strong>Direito II</strong> (nenhuma razão nem desculpa): toda razão que você dá vira um gancho para o outro discutir. <strong>Direito VII</strong> (independência da boa vontade): você não precisa que gostem de você <em>antes</em> de poder lidar com eles — pode ser querido de novo <em>depois</em> do não.",
    "tip": "<strong>Regra:</strong> no instante em que você se justifica (viola o II), convida o manipulador a refutar suas razões e reabrir o conflito."
   },
   {
    "ic": "pivot",
    "t": "O Direito de Ser Ilógico (VIII)",
    "b": "Desejos e sentimentos <strong>não precisam passar num teste de lógica</strong>; “porque eu quero” é uma razão completa para si mesmo. Você também pode mudar de ideia (IV) — ideias e circunstâncias mudam.",
    "tip": "<strong>Sinal de alerta:</strong> trate “mas isso não é lógico / justo / legal” como uma alavanca, não um xeque-mate."
   },
   {
    "ic": "scale",
    "t": "Direito ↔ Crença Manipulativa",
    "b": "Todo direito tem uma sombra: <strong>III</strong> ↔ “você tem de me ajudar”; <strong>V</strong> ↔ “errar é vergonhoso”; <strong>VI–IX</strong> ↔ “um adulto competente sempre sabe/entende”; <strong>X</strong> ↔ “você tem de se importar com o que penso”.",
    "tip": "<strong>Como aplicar:</strong> recuse a crença afirmando o direito correspondente."
   }
  ]
 },
 "ch04-disco-riscado": {
  "cards": [
   {
    "ic": "spiral",
    "t": "Disco Riscado (Broken Record)",
    "b": "Repetição calma do seu desejo, sem ensaiar argumentos nem acumular raiva. <strong>(1)</strong> decida o desejo em uma frase; <strong>(2)</strong> reconheça brevemente cada objeção e <strong>repita</strong> sem mudar a essência; <strong>(3)</strong> não responda a desvios nem “lógica irrelevante”; <strong>(4)</strong> tom no mesmo nível.",
    "tip": "<strong>Por que funciona:</strong> a maioria tem poucos “nãos” no bolso. “Se ele tem três, você só precisa de quatro.”"
   },
   {
    "ic": "scale",
    "t": "Os Dois Placares",
    "b": "Separe o <strong>objetivo material</strong> (negociável; ceda à vontade) do <strong>autorrespeito</strong> (inegociável; nunca ceda). Perder o objetivo material mantendo o autorrespeito <strong>é uma vitória</strong>.",
    "tip": "<strong>Modelo mental:</strong> imagine um disco riscado de verdade — mesmo sulco, mesma frase, repetição sem emoção: entediante, inabalável, eficaz."
   },
   {
    "ic": "link",
    "t": "Acordo Viável (Workable Compromise)",
    "b": "Sempre que o autorrespeito <strong>não</strong> estiver em jogo, ofereça um acordo prático no objetivo material (“metade agora, metade na sexta”). Você sempre pode negociar <em>coisas</em>.",
    "tip": "<strong>Regra dura:</strong> se o objetivo toca o autovalor, <strong>não há acordo</strong> — cedê-lo é derrota disfarçada de vitória."
   },
   {
    "ic": "sword",
    "t": "O Erro Nº 1: Desistir",
    "b": "Desistir <strong>depois do primeiro “não”</strong> é a razão mais comum pela qual a pessoa não assertiva perde. A persistência vence o argumento: você não precisa de uma lógica melhor, só de mais fôlego.",
    "tip": "<strong>Sinal de alerta:</strong> ser puxado para o assunto paralelo que o manipulador levanta, em vez de repetir o seu desejo."
   }
  ]
 },
 "ch05-conversa-assertiva": {
  "cards": [
   {
    "ic": "bubble",
    "t": "Informação Gratuita (Free Information)",
    "b": "Reconhecer as pequenas <strong>deixas não solicitadas</strong> que a pessoa oferece sobre o que lhe importa — e desdobrá-las. Escute o detalhe oferecido (“…depois que voltei da viagem…”) e pergunte sobre <em>aquilo</em>.",
    "tip": "<strong>Como aplicar:</strong> trate cada resposta como uma sacola de informação gratuita — puxe um fio e a conversa anda sozinha."
   },
   {
    "ic": "person",
    "t": "Autorrevelação (Self-Disclosure)",
    "b": "Falar livremente dos seus lados <strong>positivos e negativos</strong> — comportamento, estilo de vida, opiniões — para aprofundar a comunicação e <strong>matar a manipulação de fome</strong>. Ofereça você mesmo o que normalmente esconderia, sem pedir desculpa.",
    "tip": "<strong>Modelo mental:</strong> o que você revela não pode ser usado como arma — não há o que “expor” se você já disse."
   },
   {
    "ic": "eye",
    "t": "Congruência Não Verbal",
    "b": "As palavras dizem uma coisa, o corpo diz outra — as pessoas acreditam no <strong>corpo</strong>. O sinal mais claro de ansiedade é a <strong>falta de contato olho a olho</strong>; o nervosismo visível faz os outros te tolerarem em vez de honrar seus combinados.",
    "tip": "<strong>Sinal de alerta:</strong> dizer as palavras confiantes desviando o olhar — o que chega é o nervosismo."
   },
   {
    "ic": "book",
    "t": "Revelação como Armadura",
    "b": "Segredos são <strong>munição</strong>; assumir abertamente seus defeitos remove a alavanca. Esconder os negativos preserva exatamente as ansiedades (ignorância, culpa) que tornam você manipulável.",
    "tip": "<strong>Cuidado:</strong> interrogatório não é conversa — siga a informação oferecida em vez de disparar perguntas prontas."
   }
  ]
 },
 "ch06-lidar-com-critica": {
  "cards": [
   {
    "ic": "layers",
    "t": "Banco de Névoa (Fogging)",
    "b": "Reconhecer com calma a <strong>probabilidade</strong> de haver algo de verdade numa crítica, sem deixar de ser o juiz do que você faz. Três movimentos: concorde com a <strong>verdade</strong> (“tem razão, estou atrasado”), com a <strong>probabilidade</strong> (“você pode ter razão”) ou com o <strong>princípio</strong> (“se eu fizesse isso, você teria um ponto”).",
    "tip": "<strong>Por que funciona:</strong> como a névoa, você não oferece parede sólida — as farpas atravessam, você fica imóvel e a crítica não recebe recompensa."
   },
   {
    "ic": "person",
    "t": "Asserção Negativa (Negative Assertion)",
    "b": "Quando você está <strong>de fato errado</strong> (mesmo 100%), concorde de forma firme e solidária com a crítica — <strong>sem pedir desculpas</strong>. “Você tem razão, isso foi um descuido meu.”",
    "tip": "<strong>Regra:</strong> quando errou de verdade, concorde mais que o crítico (“foi burrice minha”) — encerra o ataque mais rápido que qualquer defesa."
   },
   {
    "ic": "scale",
    "t": "Elogio = Crítica",
    "b": "Para o assertivo, elogio e crítica são <strong>a mesma coisa</strong>: apenas o julgamento alheio. Receba qualquer um com a mesma calma, continuando seu próprio juiz. A crítica é informação que você pode usar ou descartar — não um veredito sobre seu valor.",
    "tip": "<strong>Como aplicar:</strong> estas técnicas deixam você olhar para os próprios negativos sem ansiedade e sem mentir sobre um erro real."
   },
   {
    "ic": "sword",
    "t": "Não se Defenda, Não Negue",
    "b": "Defender-se ou negar transforma <strong>uma única crítica num debate</strong> que o manipulador pode vencer. Pedir desculpa por ser humano (excesso de desculpas) também perde.",
    "tip": "<strong>Sinal de alerta:</strong> tratar a crítica como veredito sobre seu valor, em vez de informação a usar ou descartar."
   }
  ]
 },
 "ch07-interrogacao-negativa": {
  "cards": [
   {
    "ic": "lens",
    "t": "Interrogação Negativa (Negative Inquiry)",
    "b": "Provocar ativamente a crítica a si mesmo: pergunte, com calma e repetidamente, por mais — “o que tem no meu fazer X que te incomoda?”, “o que mais?” — até o problema real vir à tona ou a crítica fabricada secar.",
    "tip": "<strong>Por que funciona:</strong> a crítica manipulativa depende de ficar vaga; exigir detalhes ou rende informação genuína ou esvazia a sacola."
   },
   {
    "ic": "scale",
    "t": "Use ou Esgote",
    "b": "Toda crítica é <strong>feedback útil</strong> (guarde) ou <strong>um truque</strong> (drene) — a investigação separa os dois. Ao investigar em vez de se defender, você dissolve o enquadramento de “você está errado” usado para te controlar.",
    "tip": "<strong>Como aplicar:</strong> continue pedindo detalhes até a informação real aparecer; não pare na primeira reclamação vaga."
   },
   {
    "ic": "link",
    "t": "Treina o Outro a Ser Direto",
    "b": "Perguntar repetidamente “o que você realmente quer?” <strong>ensina os íntimos</strong> a declarar desejos diretamente, em vez de manipular — substituindo o emburramento e a indireta por pedidos honestos que dá para negociar.",
    "tip": "<strong>Cuidado:</strong> o tom precisa ser curiosidade genuína; com sarcasmo, vira uma nova briga."
   },
   {
    "ic": "target",
    "t": "Corra para a Crítica",
    "b": "Corra <em>em direção</em> à crítica como um <strong>aspirador</strong>, não para longe dela: “me conta mais o que está errado no que eu fiz” tira o poder de ferir e o uso como alavanca.",
    "tip": "<strong>Modelo mental:</strong> é depurar a relação — continue perguntando até achar o bug real, em vez de remendar sintomas."
   }
  ]
 },
 "ch08-situacoes-comerciais": {
  "cards": [
   {
    "ic": "wrench",
    "t": "A Pilha de Enfrentamento",
    "b": "Combine: <strong>Disco Riscado</strong> (declare e repita o desejo) + <strong>Banco de Névoa</strong> (neutralize desvios de “política”/culpa) + <strong>Acordo Viável</strong> (negocie o dinheiro) + escalar com calma até quem <strong>pode</strong> dizer sim.",
    "tip": "<strong>Como aplicar:</strong> trate “é a nossa política” como desvio gratuito, não uma parede — dê Banco de Névoa e repita o desejo."
   },
   {
    "ic": "book",
    "t": "Prévio × Renegociável",
    "b": "Um termo assinado ou afixado, combinado de antemão, em geral <strong>vale</strong> (o pneu já bem rodado). Já um <strong>defeito</strong> ou mau atendimento é justo de cobrar. Tentar se impor por cima de um contrato real parece tolice e perde.",
    "tip": "<strong>Sinal de alerta:</strong> discutir o mérito em vez de repetir o desejo dá ao funcionário ângulos para recusar."
   },
   {
    "ic": "steps",
    "t": "Suba até Quem Pode Dizer Sim",
    "b": "Pergunte <strong>“quem aqui pode de fato conceder o que quero?”</strong> e suba até essa pessoa com o Disco Riscado. Não aceite o primeiro “não” de alguém que de toda forma não tem autoridade para dizer sim.",
    "tip": "<strong>Como aplicar:</strong> ceda só no dinheiro (Acordo Viável); nunca abra mão de um tratamento respeitoso."
   },
   {
    "ic": "bubble",
    "t": "Vendedor: Sem Explicação",
    "b": "Na venda de porta em porta ou por telefone, você não deve <strong>nenhuma razão</strong> (Direito II): “não tenho interesse”, repetido, basta. Como funcionário, dar Banco de Névoa num cliente raivoso (“o senhor pode ter razão de que está lento…”) reduz a tensão sem abrir mão das regras.",
    "tip": "<strong>Regra:</strong> persista e dê Banco de Névoa nos desvios — sem argumentar o mérito."
   }
  ]
 },
 "ch09-situacoes-autoridade": {
  "cards": [
   {
    "ic": "person",
    "t": "Autoridade é Limitada",
    "b": "Pergunte: <strong>“a autoridade dela cobre mesmo isto?”</strong>. Cumpra a parte legítima; imponha-se contra o excesso. Dê Banco de Névoa/Asserção Negativa à crítica válida ao seu <strong>trabalho</strong>; use o Disco Riscado no que está fora da função.",
    "tip": "<strong>Modelo mental:</strong> desenhe uma linha em volta do cargo — dentro, coopere; fora (vida privada, seu valor), imponha-se."
   },
   {
    "ic": "target",
    "t": "Entrevista Assertiva",
    "b": "Antecipe o próprio nervosismo com Asserção Negativa + Interrogação Negativa: <strong>“eu sempre fico um pouco nervoso em entrevista — isso vai atrapalhar?”</strong>. Assumir a fraqueza a desarma e soa como confiança.",
    "tip": "<strong>Sinal de alerta:</strong> transmitir dúvida sobre habilidades menores faz você parecer uma dor de cabeça futura."
   },
   {
    "ic": "link",
    "t": "A Linha do Cargo",
    "b": "Você pode <strong>fazer o que o cargo exige</strong> e, ao mesmo tempo, <strong>recusar-se a ser diminuído</strong> como pessoa. Pais e professores também impõem limites e recebem reclamações com Banco de Névoa, em vez de batalhas de justificativa.",
    "tip": "<strong>Exemplo:</strong> “você pode ter razão que é arriscado, e como passo minhas noites é decisão minha.”"
   },
   {
    "ic": "sword",
    "t": "Não se Justifique ao Chefe",
    "b": "Justificar-se à autoridade <strong>convida a mais supervisão</strong>. E esconder o nervosismo na entrevista só o amplifica — revele e siga em frente.",
    "tip": "<strong>Cuidado:</strong> deixar a autoridade do cargo vazar para o controle pessoal (um chefe ditando sua vida privada) sem questionar."
   }
  ]
 },
 "ch10-situacoes-iguais": {
  "cards": [
   {
    "ic": "fork",
    "t": "Dizer “Não” a um Par",
    "b": "Disco Riscado + Direito II (nenhuma razão). Quando insistirem, <strong>não dê razões</strong> (que convidam à réplica): “entendo que você precise, e não”. Repita. Dê Banco de Névoa na culpa (“você pode achar isso egoísmo — e não”).",
    "tip": "<strong>Regra:</strong> sem razões = sem ganchos — o “não” sem justificativa é irrespondível."
   },
   {
    "ic": "sword",
    "t": "A Alavanca da Culpa",
    "b": "A culpa é a <strong>ferramenta principal</strong> do manipulador-par: “eu faria por você”, “você mudou”, “um amigo de verdade faria”. Reconheça, dê Banco de Névoa no enquadramento moral e segure a linha — uma relação de verdade sobrevive a um não.",
    "tip": "<strong>Sinal de alerta:</strong> comprar o enquadramento “um amigo de verdade faria…” — isso é a manipulação, não um fato sobre amizade."
   },
   {
    "ic": "book",
    "t": "O Direito VII na Prática",
    "b": "Você <strong>não precisa da aprovação</strong> deles <em>antes</em> de poder lidar com eles — dá para ser querido de novo <em>depois</em> de ter dito não. Pais intrometidos podem ser recusados com as mesmas técnicas, com gentileza mas firmeza.",
    "tip": "<strong>Como aplicar:</strong> com pares, decida sua linha antes da conversa — espere a alavanca da culpa como padrão."
   },
   {
    "ic": "link",
    "t": "Não Explique o seu “Não”",
    "b": "Toda razão que você dá a um amigo é <strong>algo para ele rebater</strong>. Ceder para acabar com a culpa só ensina os pares de que a culpa funciona com você.",
    "tip": "<strong>Regra:</strong> recuse com um “não” simples; o nome do jogo é não dar gancho."
   }
  ]
 },
 "ch11-desejos-sexuais": {
  "cards": [
   {
    "ic": "person",
    "t": "Mesmas Técnicas, Terreno Carregado",
    "b": "Autorrevelação + Interrogação Negativa + Acordo Viável aplicados ao sexo: revele seus desejos e receios com clareza; investigue os do parceiro; negocie os <strong>atos</strong> (material), nunca o autorrespeito. Dizer não à sedução é o mesmo enfrentamento de qualquer manipulação.",
    "tip": "<strong>Frase do livro:</strong> “primeiro a asserção, depois a inserção” — a assertividade é pré-requisito de uma relação sexual saudável."
   },
   {
    "ic": "eye",
    "t": "Agendas Ocultas de Ansiedade",
    "b": "Medos não ditos sobre mudança se <strong>disfarçam de preferências</strong>; a revelação os traz à luz, onde podem ser negociados. Dar indiretas em vez de revelar um desejo — e depois se ressentir de o parceiro não ter adivinhado — é antipadrão.",
    "tip": "<strong>Como aplicar:</strong> a Interrogação Negativa substitui o emburramento e a indireta por desejos ditos com honestidade."
   },
   {
    "ic": "scale",
    "t": "Negocie os Atos, Não a Dignidade",
    "b": "Negocie livremente os <strong>atos</strong> sexuais; uma exigência que custa seu <strong>autovalor</strong> é inegociável. A manipulação no sexo (culpa, “mágoa”, acusação) é a mesma alavanca de qualquer lugar — reconheça e use o mesmo enfrentamento.",
    "tip": "<strong>Sinal de alerta:</strong> passividade silenciosa ou manipulação no sexo é rota documentada para a disfunção."
   },
   {
    "ic": "constellation",
    "t": "A Questão Social",
    "b": "Perguntado sobre o que aconteceria com a sociedade se muitos virassem assertivos, Smith responde com honestidade: <strong>“Não sei.”</strong> Sua preocupação está nos dois extremos — o <strong>indivíduo</strong> e a <strong>espécie</strong> — e na menor unidade social: duas pessoas resolvendo disputas pelos temas reais, não por quem manipula melhor.",
    "tip": "<strong>Fecho:</strong> o objetivo de toda a obra é resolver o conflito pelos fatos da disputa, não pela força relativa das personalidades."
   }
  ]
 }
}
```
