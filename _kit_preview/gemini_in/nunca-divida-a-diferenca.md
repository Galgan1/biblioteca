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

# LIVRO PARA APROFUNDAR: Nunca Divida a Diferença — Chris Voss

**Subtítulo:** VISÃO GERAL · NEGOCIE COMO SE SUA VIDA DEPENDESSE DISSO
**Ideia central:** Negociação não é um debate racional ganho com lógica — é um processo emocional. O ex-negociador-chefe do FBI Chris Voss revela que entender e nomear a emoção do outro vale mais que qualquer planilha. Com empatia tática, você faz o interlocutor se sentir compreendido, dá a ele a ilusão de controle e molda a realidade a seu favor.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-novas-regras` — CAPÍTULO 1: As Novas Regras
- `ch02-espelhamento` — CAPÍTULO 2: Seja um Espelho
- `ch03-rotulacao` — CAPÍTULO 3: Não Sinta a Dor Deles, Rotule-a
- `ch04-nao-e-isso-mesmo` — CAPÍTULOS 4–5: O 'Não' e o 'É Isso Mesmo'
- `ch06-curvar-realidade` — CAPÍTULO 6: Curve a Realidade Dele
- `ch07-perguntas-calibradas` — CAPÍTULO 7: Crie a Ilusão de Controle
- `ch09-barganha-ackerman` — CAPÍTULO 9: Negocie Duro — Método Ackerman
- `ch10-cisnes-negros` — CAPÍTULO 10: Encontre o Cisne Negro
- `ch08-garantir-execucao` — CAPÍTULO 8: Garanta a Execução

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-novas-regras": {
  "cards": [
   {
    "ic": "wave",
    "t": "Emoção Decide, Razão Justifica",
    "b": "A decisão nasce no <strong>Sistema 1</strong> (rápido, emocional); o Sistema 2 (lógico) só racionaliza depois. Você negocia com a emoção do outro — não com fatos e cálculos.",
    "tip": "<strong>Modelo mental:</strong> a pessoa do outro lado nunca é tão racional quanto você supõe."
   },
   {
    "ic": "lens",
    "t": "Negociação como Descoberta",
    "b": "Seu objetivo não é vencer um argumento, é <strong>extrair o que o outro realmente quer e teme</strong>. Trate cada interação como coleta de inteligência: faça o outro falar mais que você.",
    "tip": "<strong>Como aplicar:</strong> entre em toda negociação com a pergunta 'o que ele precisa saber que está certo?'."
   },
   {
    "ic": "eye",
    "t": "Empatia Tática",
    "b": "Entender deliberadamente os sentimentos e a perspectiva do outro <strong>e vocalizar</strong> esse entendimento para influenciá-lo. Empatia não é ser bonzinho — é uma ferramenta de influência.",
    "tip": "<strong>Regra:</strong> ouça para mapear a emoção, nomeie-a, use-a para construir confiança."
   }
  ]
 },
 "ch02-espelhamento": {
  "cards": [
   {
    "ic": "bubble",
    "t": "Espelhamento (Mirroring)",
    "b": "Repita, em tom de pergunta, as últimas <strong>1–3 palavras</strong> do outro. Depois: <strong>silêncio de 4+ segundos</strong>. Aciona afiliação — 'somos parecidos' — e o desconforto do silêncio força o outro a revelar mais.",
    "tip": "<strong>Como aplicar:</strong> (1) voz de FM noturno; (2) espelhe as palavras-chave; (3) cale-se; (4) repita."
   },
   {
    "ic": "wave",
    "t": "As Três Vozes",
    "b": "<strong>FM noturno</strong> (grave, descendente): transmite controle e tranquiliza. <strong>Positiva/jovial</strong> (padrão): descontrai. <strong>Assertiva</strong> (raríssima): gera reação — use com cuidado.",
    "tip": "<strong>Regra:</strong> a voz descendente afirma, a ascendente pede — escolha a inflexão conscientemente."
   },
   {
    "ic": "gap",
    "t": "Silêncio Dinâmico",
    "b": "Pausa intencional após espelhar. O desconforto faz o outro preencher o vácuo — e revelar o que não diria sob pressão. <strong>Quanto menos você fala, mais aprende.</strong>",
    "tip": "<strong>Sinal de alerta:</strong> falar para preencher o silêncio entrega informação e poder de graça."
   }
  ]
 },
 "ch03-rotulacao": {
  "cards": [
   {
    "ic": "bubble",
    "t": "Rotulação (Labeling)",
    "b": "Nomeie a emoção: <strong>'Parece que…'</strong>, <strong>'Soa como…'</strong> — nunca 'Eu acho que você…' (gera ego). Depois: silêncio. Dar nome a um medo o reduz; nomear uma emoção positiva a reforça.",
    "tip": "<strong>Como aplicar:</strong> 'Parece que isso foi frustrante para você.' → silêncio → deixe processar."
   },
   {
    "ic": "mask",
    "t": "Auditoria de Acusações",
    "b": "Antes de uma proposta difícil, liste em voz alta as piores críticas que o outro faria de você: 'Vai parecer injusto…', 'Vou soar ganancioso…'. Dizê-las primeiro <strong>as desarma</strong> — ele não pode usar o que você já disse.",
    "tip": "<strong>Como aplicar:</strong> enumere as objeções com superlativos antes de apresentar sua proposta."
   },
   {
    "ic": "spark",
    "t": "Empatia ≠ Concordância",
    "b": "Nomear o sentimento do outro não significa ceder a ele. A rotulação cria confiança <strong>sem concessões</strong>. Neutralize o negativo, reforce o positivo — e avance nos seus termos.",
    "tip": "<strong>Modelo mental:</strong> toda emoção tem um nome; dizê-lo a desativa."
   }
  ]
 },
 "ch04-nao-e-isso-mesmo": {
  "cards": [
   {
    "ic": "key",
    "t": "O 'Não' como Início",
    "b": "O 'não' protege, dá poder e autonomia ao outro — só depois dele as pessoas relaxam e decidem de verdade. Convide o 'não': <strong>'Seria uma má ideia se…?'</strong>. Para reativar silêncio: <strong>'Você desistiu deste projeto?'</strong>",
    "tip": "<strong>Regra:</strong> não force o 'sim'; caçar o 'não' abre o diálogo real."
   },
   {
    "ic": "spiral",
    "t": "Os Três Tipos de 'Sim'",
    "b": "<strong>Falso</strong> (para fugir), <strong>de confirmação</strong> (reflexo simples) e <strong>de compromisso</strong> (o verdadeiro). Não comemore 'tem razão' — quase sempre é o 'sim' falso para te dispensar.",
    "tip": "<strong>Sinal de alerta:</strong> 'tem razão' fecha a porta; 'é isso mesmo' abre o coração."
   },
   {
    "ic": "lens",
    "t": "Provoque o 'É Isso Mesmo'",
    "b": "O ponto de virada: o outro sente que você o compreendeu por completo. Ferramenta: <strong>resumo = paráfrase do conteúdo + rótulo da emoção</strong>. Articule o mundo do outro melhor do que ele — e ele se renderá à compreensão.",
    "tip": "<strong>Como aplicar:</strong> combine paráfrase + rótulos até ouvir 'é isso mesmo' — aí a adesão é real."
   }
  ]
 },
 "ch06-curvar-realidade": {
  "cards": [
   {
    "ic": "target",
    "t": "Nunca Divida a Diferença",
    "b": "Rachar no meio produz dois perdedores. Descubra a necessidade real por trás da posição e molde os termos. <strong>50/50 parece justo e costuma ser preguiçoso.</strong>",
    "tip": "<strong>Modelo mental:</strong> não negocie o número; molde a percepção em volta dele."
   },
   {
    "ic": "scale",
    "t": "Aversão à Perda e 'Justo'",
    "b": "Enquadre pela <strong>perda</strong>, não pelo ganho — as pessoas arriscam mais para evitar uma perda. Ao ouvir 'só quero o que é justo', responda: <strong>'Me diga onde fui injusto.'</strong>",
    "tip": "<strong>Como aplicar:</strong> reframe de ganho para perda dobra o impacto psicológico da sua oferta."
   },
   {
    "ic": "clock",
    "t": "Prazos São Negociáveis",
    "b": "Quase todo prazo existe para criar urgência — quase nunca é real. Não se apresse por causa do relógio do outro. <strong>Ancore antes do outro</strong>: quem ancora primeiro enquadra a faixa percebida.",
    "tip": "<strong>Sinal de alerta:</strong> concessões ruins nascem da pressa — quem se apressa, perde."
   }
  ]
 },
 "ch07-perguntas-calibradas": {
  "cards": [
   {
    "ic": "bulb",
    "t": "Perguntas Calibradas",
    "b": "Abertas, com <strong>'Como'</strong> e <strong>'O quê'</strong> — nunca 'por quê' (soa acusatório). Desarmam a agressividade e transferem o esforço de resolver para o outro. Ilusão de controle: ele sente que conduz, mas você definiu o trilho.",
    "tip": "<strong>Como aplicar:</strong> 'O que estamos tentando alcançar aqui?' / 'O que torna isso difícil?'"
   },
   {
    "ic": "wrench",
    "t": "'Como Eu Faço Isso?'",
    "b": "A pergunta-superpoder: recusa amável e firme que força o outro a olhar para o seu lado e — muitas vezes — melhorar a própria oferta. <strong>Diz 'não' sem dizer 'não'</strong> e mantém a porta aberta.",
    "tip": "<strong>Modelo mental:</strong> não resolva o problema do outro — peça que ele resolva o seu."
   },
   {
    "ic": "gap",
    "t": "Evite 'Por Quê'",
    "b": "Em quase toda língua, 'por que você…?' coloca o outro na defensiva e acusa. Reformule: <strong>'O que te levou a isso?'</strong> ou <strong>'Como isso funcionou?'</strong> — o sentido é o mesmo, o efeito é oposto.",
    "tip": "<strong>Sinal de alerta:</strong> toda vez que sua pergunta começar com 'por que você', reescreva com 'o que' ou 'como'."
   }
  ]
 },
 "ch09-barganha-ackerman": {
  "cards": [
   {
    "ic": "steps",
    "t": "O Método Ackerman",
    "b": "Alvo definido → <strong>65%</strong> → suba a <strong>85% → 95% → 100%</strong> em incrementos decrescentes. Entre cada lance: rótulo + pergunta calibrada (faça o outro dizer 'não' antes de subir). Concessões decrescentes comunicam 'estou no limite'.",
    "tip": "<strong>Como aplicar:</strong> feche com cifra precisa (R$ 4.387, não R$ 4.400) + item não-monetário para selar o limite."
   },
   {
    "ic": "person",
    "t": "Os Três Tipos de Negociador",
    "b": "<strong>Analista</strong>: metódico, quer dados, valoriza tempo. <strong>Acomodador</strong>: relacional, fala muito, quer o vínculo. <strong>Assertivo</strong>: direto, competitivo, quer ser ouvido. Identifique o tipo do outro e adapte ritmo e tom.",
    "tip": "<strong>Modelo mental:</strong> adapte-se ao tipo do outro, não ao seu conforto."
   },
   {
    "ic": "fork",
    "t": "Número Preciso + Item Extra",
    "b": "A cifra final <strong>não-redonda</strong> (R$ 4.387 em vez de R$ 4.400) soa calculada — transmite que não há mais de onde tirar. O item não-monetário extra sinaliza o mesmo: 'dei tudo que podia.'",
    "tip": "<strong>Como aplicar:</strong> calcule o número final com decimais e leve um 'brinde' irrelevante que mostre o fundo do cofre."
   }
  ]
 },
 "ch10-cisnes-negros": {
  "cards": [
   {
    "ic": "constellation",
    "t": "Cisnes Negros",
    "b": "Fatos desconhecidos de alto impacto que reconfiguram a negociação — cada lado costuma ter ~3 escondidos. Quando algo <strong>'parece louco'</strong>, não falta bom-senso no outro — falta informação no seu mapa.",
    "tip": "<strong>Modelo mental:</strong> 'isso é loucura' significa 'falta informação'. Caçe o cisne negro em vez de julgar."
   },
   {
    "ic": "triangle",
    "t": "As Três Alavancagens",
    "b": "<strong>Positiva</strong>: você tem o que o outro quer. <strong>Negativa</strong>: capacidade de causar perda (use com cautela). <strong>Normativa</strong>: use os próprios valores declarados do outro contra a posição dele — 'isso bate com seus princípios?'",
    "tip": "<strong>Como aplicar:</strong> prefira a alavancagem normativa — usa os valores do próprio outro e não gera reação."
   },
   {
    "ic": "eye",
    "t": "Entre no Mundo do Outro",
    "b": "Descubra as crenças, valores e referências que regem o outro — sua 'religião'. Falar dentro do mundo dele dá acesso e influência que nenhum argumento externo dá. Encontros presenciais revelam cisnes que o telefone esconde.",
    "tip": "<strong>Regra:</strong> influência mora dentro da lógica do outro, não da sua."
   }
  ]
 },
 "ch08-garantir-execucao": {
  "cards": [
   {
    "ic": "wrench",
    "t": "A Regra 7-38-55",
    "b": "As palavras carregam <strong>7%</strong> do significado; o tom de voz, <strong>38%</strong>; a linguagem corporal, <strong>55%</strong>. Se as palavras dizem 'sim' mas o tom e o corpo dizem outra coisa, confie no não-verbal.",
    "tip": "<strong>Como aplicar:</strong> quando palavras e corpo dissonarem, nomeie a dissonância: 'Você diz que está animado, mas soa hesitante — o que está passando?'"
   },
   {
    "ic": "steps",
    "t": "A Regra dos Três 'Sins'",
    "b": "Faça o outro confirmar o compromisso de <strong>três formas diferentes</strong> na mesma conversa (paráfrase, pergunta calibrada, resumo). Fingir três vezes seguidas é difícil — a terceira confirmação expõe o 'sim' falso.",
    "tip": "<strong>Modelo mental:</strong> um 'sim' é educação; três confirmações distintas são compromisso."
   },
   {
    "ic": "target",
    "t": "'Como' Garante a Execução",
    "b": "'Sim' sem plano é intenção. Cubra a implementação: <strong>'Como saberemos que está no caminho?'</strong>, <strong>'Quem precisa saber disso?'</strong>. Quem responde 'como' passa a trabalhar pela sua causa.",
    "tip": "<strong>Como aplicar:</strong> termine toda negociação com perguntas calibradas de implementação, não de celebração."
   }
  ]
 }
}
```
