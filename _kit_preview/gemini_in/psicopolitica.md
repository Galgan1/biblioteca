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

# LIVRO PARA APROFUNDAR: Psicopolítica — Byung-Chul Han

**Subtítulo:** VISÃO GERAL · O NEOLIBERALISMO E AS NOVAS TÉCNICAS DE PODER
**Ideia central:** O poder saiu do corpo e foi para a psique. O neoliberalismo não reprime — seduz. Faz do sujeito um empreendedor de si que se autoexplora julgando-se livre. Byung-Chul Han mapeia essa guinada — do biopoder de Foucault para a psicopolítica digital — e aponta a única saída: o idiotismo, a coragem do "não".

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-crise-da-liberdade` — CAPÍTULO 1: A Crise da Liberdade
- `ch02-smart-power` — CAPÍTULO 2: O Smart Power (Poder Gentil)
- `ch03-emocionalizacao` — CAPÍTULO 3: A Emocionalização
- `ch04-dataismo` — CAPÍTULO 4–5: Dataísmo e a Guinada Psicopolítica
- `ch05-transparencia-panoptico` — CAPÍTULO 6–7: Transparência e Panóptico Digital
- `ch06-idiotismo` — CAPÍTULO 8: O Idiotismo — Resistência à Psicopolítica

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-crise-da-liberdade": {
  "cards": [
   {
    "ic": "mask",
    "t": "O Empreendedor de Si Mesmo",
    "b": "O indivíduo é gerido como empresa de si. Concorre, otimiza-se, cobra-se. A exploração externa cede lugar à <strong>autoexploração</strong> — mais eficiente porque vem com sensação de liberdade. Sem senhor externo, <strong>não há revolta possível</strong>.",
    "tip": "<strong>Exemplo atual:</strong> o criador de conteúdo \"dono do próprio tempo\" que posta de madrugada e desaba — ninguém o obriga, e é exatamente isso que o impede de parar."
   },
   {
    "ic": "spiral",
    "t": "Coação à Liberdade",
    "b": "O \"poder\" se converte em \"tem-que-poder\". A liberdade sem limite <strong>esgota</strong>, não liberta. A agressividade, sem opressor externo a combater, dobra-se sobre o eu — depressão, burnout.",
    "tip": "<strong>Modelo mental:</strong> a liberdade neoliberal não é ausência de coação, é a forma mais eficiente dela — porque é internalizada e voluntária."
   },
   {
    "ic": "person",
    "t": "Sujeito-Projeto Sempre Incompleto",
    "b": "O eu se concebe como <strong>projeto sempre por concluir</strong> e nisso fracassa cronicamente. Não há chegada — só otimização permanente. A autoexploração é mais total que a externa porque não tem rosto a derrubar.",
    "tip": "<strong>Sinal de alerta:</strong> quando a sensação de \"nunca ser suficiente\" domina, você está no ciclo do sujeito-projeto — a coação vem de dentro."
   }
  ]
 },
 "ch02-smart-power": {
  "cards": [
   {
    "ic": "spark",
    "t": "Poder que Seduz, não Reprime",
    "b": "O smart power não diz \"você deve\" — pergunta \"do que você gosta?\" e oferece o <strong>\"curtir\"</strong>. Não há contra o quê resistir num poder que dá prazer. Quem é seduzido coopera; quem coopera não se rebela.",
    "tip": "<strong>Modelo mental:</strong> o controle mais forte é aquele de que o sujeito gosta. Desconfie do dispositivo que te agrada demais."
   },
   {
    "ic": "bubble",
    "t": "O \"Like\" Como Forma de Poder",
    "b": "A curtida é o verbo do poder gentil: <strong>aprovação como mecanismo de adesão e dado</strong>. O feed que aprende o que você gosta e entrega mais do mesmo não é vigiante — é cortejador. A interface não ordena: ela sugere, recomenda, pergunta \"gostou?\".",
    "tip": "<strong>Como aplicar:</strong> ao sentir que um app é conveniente demais para largar, reconheça o smart power em ação."
   },
   {
    "ic": "leaf",
    "t": "Permissividade Como Controle",
    "b": "\"Seja você mesmo\", \"realize-se\" — a liberalidade não liberta: <strong>vincula</strong>. O sujeito que crê expressar sua singularidade reproduz o padrão que o explora. A permissividade é a forma mais sedutora de conformismo.",
    "tip": "<strong>Sinal de alerta:</strong> quando \"autenticidade\" é um imperativo de marca, a expressão de si já é produção para o mercado."
   }
  ]
 },
 "ch03-emocionalizacao": {
  "cards": [
   {
    "ic": "wave",
    "t": "Emoção Como Força Produtiva",
    "b": "O capitalismo emocional não vende objetos — <strong>vende sentimentos, experiências e sentido</strong>. A emoção contorna a razão: conduz o consumo antes que o sujeito pense. Mobilizar afeto é mais eficaz que convencer.",
    "tip": "<strong>Como aplicar:</strong> ao avaliar uma campanha, pergunte qual emoção ela produz e captura — esse é o produto real."
   },
   {
    "ic": "mask",
    "t": "Autenticidade Como Dispositivo",
    "b": "O imperativo de \"ser autêntico\", \"expressar-se\", \"ser você mesmo\" parece liberdade — mas é <strong>produção do eu para o mercado</strong>. A singularidade vira produto; a diferença, diferencial vendável.",
    "tip": "<strong>Modelo mental:</strong> quando \"seja você mesmo\" é um mandamento de plataforma, a autoexpressão já é trabalho para o algoritmo."
   },
   {
    "ic": "target",
    "t": "Emoção vs. Sentimento vs. Razão",
    "b": "A emoção é dinâmica e performativa — <strong>mobilizável e instrumentalizável</strong>. O capital a prefere porque é o vetor mais ágil de adesão impulsiva, escapando ao controle reflexivo. A razão é lenta e reflexiva — e por isso é contornada.",
    "tip": "<strong>Sinal de alerta:</strong> feed que otimiza para indignação e euforia usa a emoção como ferramenta de captura — engajamento = dado = receita."
   }
  ]
 },
 "ch04-dataismo": {
  "cards": [
   {
    "ic": "lens",
    "t": "Dataísmo — Saber sem Sentido",
    "b": "A crença de que a realidade se reduz a dados e que correlação substitui a causalidade e a compreensão. \"O dado é mais transparente que o espírito.\" Um <strong>niilismo</strong>: pura contagem sem sentido.",
    "tip": "<strong>Modelo mental:</strong> quando um sistema acerta sobre você sem entender você, é dataísmo — poder sem sentido."
   },
   {
    "ic": "eye",
    "t": "Dividual — Fim da Pessoa",
    "b": "O indivíduo (indivisível) se dissolve em <strong>dividual</strong> — fragmentos de dados recombináveis. O Big Data não importa quem você é: importa em que cluster você cai. A liberdade futura é capturada como probabilidade.",
    "tip": "<strong>Como aplicar:</strong> a recomendação que prevê o que você quer ver antes de você saber é psicopolítica preditiva — não te entende, te calcula."
   },
   {
    "ic": "layers",
    "t": "Bio → Psicopolítica (a Guinada)",
    "b": "O biopoder de Foucault disciplinava <strong>corpos</strong> com proibição e vigilância. A psicopolítica disciplina a <strong>psique</strong> — motiva, otimiza, faz desejar. Só é possível porque o sujeito é \"livre\" e é essa liberdade que ela explora.",
    "tip": "<strong>Modelo mental:</strong> o app de bem-estar que te motiva, gameifica e parabeniza é psicopolítica — não proíbe nada, apenas programa o desejo."
   }
  ]
 },
 "ch05-transparencia-panoptico": {
  "cards": [
   {
    "ic": "eye",
    "t": "Transparência Como Controle",
    "b": "O imperativo de tudo expor elimina a <strong>negatividade</strong> (o outro, o oculto, o singular) e produz o igual. Substitui a <strong>confiança pelo controle</strong>: onde tudo é exposto, a confiança é supérflua. E o sujeito se expõe por iniciativa própria.",
    "tip": "<strong>Modelo mental:</strong> tudo transparente = tudo controlável. Desconfie do elogio à transparência total; o que se torna visível, torna-se governável."
   },
   {
    "ic": "constellation",
    "t": "O Panóptico Digital Voluntário",
    "b": "No panóptico de Bentham, havia isolamento e coerção. No digital, há <strong>hipercomunicação e exposição voluntária</strong>. A vigilância é lateral: cada usuário vigia e expõe os outros (e a si). Colaboramos com a própria vigilância.",
    "tip": "<strong>Como aplicar:</strong> você não é vigiado contra a vontade — você colabora: a eficácia está em você querer postar, curtir, compartilhar."
   },
   {
    "ic": "bubble",
    "t": "O Big Brother Amável",
    "b": "A vigilância não inspira medo — inspira <strong>conforto e prazer</strong>. Entregamos dados por conveniência e gratificação. Não somos forçados a entrar: desejamos entrar. Conveniência é a coleira; cada conforto digital é um ponto de coleta.",
    "tip": "<strong>Sinal de alerta:</strong> o assistente de voz que escuta \"para te ajudar\", o wearable que monitora teu sono \"pelo teu bem\" — ninguém te obriga, todos aderem."
   }
  ]
 },
 "ch06-idiotismo": {
  "cards": [
   {
    "ic": "pivot",
    "t": "Idiotismo — a Coragem do Não",
    "b": "O <em>idiotēs</em> grego era o particular, à parte da pólis e do consenso. Han o resgata como figura de liberdade. <strong>Resistir é subtrair, não somar</strong>: desligar, calar, guardar um pensamento sem postá-lo.",
    "tip": "<strong>Como aplicar:</strong> não como detox produtivista (para render mais), mas como reconquista da singularidade fora do enxame digital."
   },
   {
    "ic": "gap",
    "t": "Potência do Não vs. Positividade Compulsiva",
    "b": "A resistência não é mais comunicação ou mais ação — é a capacidade de <strong>não fazer, não reagir, não se expor, não comunicar</strong>. A potência negativa (poder-não) contra a positividade compulsiva da rede.",
    "tip": "<strong>Modelo mental:</strong> o silêncio guarda um espaço para o pensamento que nasce do não-saber, do que ainda não virou dado nem opinião."
   },
   {
    "ic": "leaf",
    "t": "Sair do Enxame Digital",
    "b": "O \"enxame\" (Schwarm) é a massa conectada sem corpo coletivo nem alma — apenas barulho sincronizado. <strong>Tornar-se idiota é sair do enxame</strong>: recuperar a solidão, a distância, a singularidade que o dado não alcança.",
    "tip": "<strong>Sinal de alerta:</strong> acusam Han de oferecer uma saída individualista — a resposta é que o gesto filosófico precede qualquer programa coletivo."
   }
  ]
 }
}
```
