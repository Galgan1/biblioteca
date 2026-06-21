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

# LIVRO PARA APROFUNDAR: A Arte da Sedução — Robert Greene

**Subtítulo:** VISÃO GERAL · PODER SUAVE, INDIRETO E PSICOLÓGICO
**Ideia central:** Sedução é a forma mais sofisticada de poder — indireta, suave, psicológica. Greene mapeia 9 tipos de sedutor, o Anti-Sedutor e 24 manobras organizadas em 4 fases. Lente analítica: reconhecer a dinâmica para não ser conduzido às cegas.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-seducao-como-poder` — CAPÍTULO 1: A Sedução como Poder
- `ch02-tipos-sedutor-1` — CAPÍTULO 2: Os Tipos de Sedutor I
- `ch03-tipos-sedutor-2` — CAPÍTULO 3: Os Tipos de Sedutor II
- `ch04-anti-sedutor-vitimas` — CAPÍTULO 4: O Anti-Sedutor e as Vítimas
- `ch05-fase1-separar` — CAPÍTULO 5: Fase 1 — Separar / Criar Desejo
- `ch06-fase2-penetrar` — CAPÍTULO 6: Fase 2 — Penetrar / Prazer e Confusão
- `ch07-fase3-precipitar` — CAPÍTULO 7: Fase 3 — Precipitar
- `ch08-fase4-o-tombo` — CAPÍTULO 8: Fase 4 — O Tombo / Aprofundar
- `ch09-lente-analitica` — CAPÍTULO 9: A Lente Analítica — Reconhecer para Escolher

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-seducao-como-poder": {
  "cards": [
   {
    "ic": "spark",
    "t": "Poder por Atração",
    "b": "O sedutor nunca pressiona; cria um <strong>vácuo de desejo</strong> que a vítima preenche sozinha. A paciência, a indireção e a teatralidade fazem o efeito parecer 'natural' — como se o encontro fosse destino, não estratégia.",
    "tip": "<strong>Modelo mental:</strong> pense como dramaturgo — a sedução tem arco (início, clímax, fim), não é um único lance de conquista."
   },
   {
    "ic": "eye",
    "t": "Foco na Carência do Outro",
    "b": "A habilidade-mãe é identificar o que <strong>falta na vida da vítima</strong> (vazio, fantasia reprimida, ferida, tédio) e tornar-se a resposta viva. O sedutor suspende o próprio ego para refletir o do outro.",
    "tip": "<strong>Como aplicar:</strong> observe do que a pessoa reclama, o que idealiza, qual fantasia repete — esse é o mapa da carência e da porta de entrada."
   },
   {
    "ic": "mask",
    "t": "A Sedução como Personagem",
    "b": "Não é uma técnica isolada — é <strong>encarnar um tipo</strong> que projeta uma promessa específica. Aparência, mistério e drama valem mais que sinceridade nua. A resistência inicial é matéria-prima: o 'não' dá tensão ao 'sim' futuro.",
    "tip": "<strong>Sinal de alerta:</strong> falar de si, exibir-se, querer agradar rápido — é o caminho do Anti-Sedutor. A insistência e a pressão ativam a defesa, matam o desejo."
   }
  ]
 },
 "ch02-tipos-sedutor-1": {
  "cards": [
   {
    "ic": "wave",
    "t": "Sereia e Libertino",
    "b": "<strong>Sereia</strong>: aura sensual e ar de perigo — promete aventura e prazer fora da rotina. <strong>Libertino</strong>: desejo aparentemente incontrolável e palavras ardentes — faz o outro sentir-se objeto de um anseio total. Ambos vendem intensidade como promessa.",
    "tip": "<strong>Modelo mental:</strong> Sereia e Libertino jogam com intensidade — são os tipos para quem quer ser desejado com força e sem reservas."
   },
   {
    "ic": "constellation",
    "t": "Amante Ideal e Dândi",
    "b": "<strong>Amante Ideal</strong>: estuda a fantasia da vítima e se molda a ela — promete o romance/vida que a pessoa sempre sonhou (exaustivo de sustentar). <strong>Dândi</strong>: ambiguidade de gênero e papéis — promete transgredir convenções com elegância.",
    "tip": "<strong>Como aplicar:</strong> Amante Ideal/Dândi jogam com adequação à fantasia — são os tipos para quem quer sentir-se compreendido ou libertado."
   },
   {
    "ic": "mask",
    "t": "O Erro de Cada Tipo",
    "b": "<strong>Sereia</strong> sem mistério vira caricatura. <strong>Libertino</strong> sem sinceridade aparente vira predador óbvio. <strong>Amante Ideal</strong> que projeta a <strong>própria</strong> fantasia (não a da vítima) fracassa. Todo tipo precisa de aura ou mistério para não soar transparente.",
    "tip": "<strong>Sinal de alerta:</strong> o erro mais comum é projetar a própria fantasia em vez de ler a do outro — é o anti-foco, o traço do Anti-Sedutor."
   }
  ]
 },
 "ch03-tipos-sedutor-2": {
  "cards": [
   {
    "ic": "leaf",
    "t": "Natural e Coquete",
    "b": "<strong>Natural</strong>: espontaneidade e vulnerabilidade infantis que desarmam — promete leveza e ternura num mundo cínico. <strong>Coquete</strong>: domina pelo dar-e-retirar — calor seguido de frieza calculada; a recompensa sempre adiada cria o vício da conquista nunca concluída.",
    "tip": "<strong>Modelo mental:</strong> Natural e Coquete são opostos — um desarma pela ausência de ameaça; o outro prende pela escassez emocional."
   },
   {
    "ic": "person",
    "t": "Encantador e Carismático",
    "b": "<strong>Encantador</strong>: foco 100% no outro, agrado sem confronto — o outro se sente o centro do mundo. <strong>Carismático</strong>: aura interior de convicção e propósito que faz multidões seguirem — promete sentido maior e pertencimento.",
    "tip": "<strong>Como aplicar:</strong> Encantador é o tipo mais útil em ambientes profissionais; Carismático e Estrela são os tipos da influência em escala — marketing, política, liderança."
   },
   {
    "ic": "constellation",
    "t": "A Estrela — Tela de Projeção",
    "b": "A <strong>Estrela</strong> funciona como tela em branco onde cada um projeta o próprio ideal. Presença marcante + ausência de definição (deixa espaço para a fantasia alheia). Kennedy na TV, Marilyn Monroe, Warhol enigmático — construídos, não dados.",
    "tip": "<strong>Sinal de alerta:</strong> Carismático sem substância vira demagogo. Estrela que se define demais perde o poder de projeção — o mistério é estrutural."
   }
  ]
 },
 "ch04-anti-sedutor-vitimas": {
  "cards": [
   {
    "ic": "triangle",
    "t": "O Anti-Sedutor",
    "b": "O que repele: <strong>insegurança</strong> (suga energia, mata o mistério), <strong>foco em si</strong> (falar só de si, não ouvir), <strong>pressão e pressa</strong> (forçar intimidade ativa a defesa), <strong>falta de mistério</strong> (previsibilidade total). Sedução é subtração antes de adição: remova os anti-traços primeiro.",
    "tip": "<strong>Regra:</strong> preserve o mistério — não diga nem mostre tudo. Dê espaço: o desejo cresce no vácuo, morre no sufoco."
   },
   {
    "ic": "eye",
    "t": "Ler a Carência da Vítima",
    "b": "Cada pessoa carrega uma <strong>carência específica</strong>: fantasia reprimida, vazio afetivo, tédio crônico, medo de envelhecer. Não há vítima genérica — a mesma manobra que arrebata um perfil repele outro. Observe do que a pessoa reclama, o que idealiza, qual fantasia repete.",
    "tip": "<strong>Como aplicar:</strong> Casanova mudava de personagem conforme a mulher — o mesmo sedutor, lendo carências distintas, oferecia promessas distintas."
   },
   {
    "ic": "person",
    "t": "Reconheça seu Próprio Perfil",
    "b": "Em chave analítica: reconhecer <strong>seu próprio</strong> perfil de vítima é a melhor defesa — saber qual vazio o torna influenciável. A resistência que você mais nega às vezes aponta o desejo reprimido que alguém pode explorar.",
    "tip": "<strong>Modelo mental:</strong> espelhe a fantasia do outro, não imponha a sua. O erro do Anti-Sedutor é sempre esse — projeta a própria necessidade em vez de ler a alheia."
   }
  ]
 },
 "ch05-fase1-separar": {
  "cards": [
   {
    "ic": "fork",
    "t": "Aproximação Indireta",
    "b": "Nunca avance frontalmente. Apareça como <strong>amigo, terceiro neutro, presença casual</strong> — desarme a suspeita antes de despertar o desejo. A aproximação frontal alerta a defesa; a oblíqua cria espaço para o desejo crescer sem resistência.",
    "tip": "<strong>Como aplicar:</strong> surja como aliado de um interesse comum, converse sobre um terceiro tema — e ao sair, deixe um comentário ambíguo. A iniciativa de reaproximar tenderá a partir da vítima."
   },
   {
    "ic": "wave",
    "t": "Sinais Ambíguos (Quente e Frio)",
    "b": "Misture <strong>interesse e distância</strong>. A ambiguidade gera curiosidade e ocupa a mente da vítima ('ela gosta ou não?'). Ser só 'quente' sufoca; ser só 'frio' é indiferença real. A tensão entre os dois é o motor que mantém a atenção.",
    "tip": "<strong>Modelo mental:</strong> tensão &gt; declaração — o não-dito atrai mais que a confissão. Ocupe a mente, não a agenda."
   },
   {
    "ic": "gap",
    "t": "Crie a Carência",
    "b": "Faça a pessoa sentir uma <strong>leve falta</strong> — um descontentamento com a vida atual — que só você parece preencher. Entre como objeto de desejo via aura ou prova social: ser visto como desejado por outros eleva automaticamente o valor percebido.",
    "tip": "<strong>Regra:</strong> declare interesse cedo demais e a tensão desaparece. Escolha a vítima errada (sem carência aberta) e não há porta de entrada."
   }
  ]
 },
 "ch06-fase2-penetrar": {
  "cards": [
   {
    "ic": "bubble",
    "t": "Espelhe e Isole",
    "b": "<strong>Espelhar</strong>: adote o humor, os valores e o ritmo da vítima — faça-a sentir um eco raro de si mesma. A semelhança percebida reduz a resistência. <strong>Isolar</strong>: afaste-a sutilmente de amigos, hábitos e senso crítico. Sozinha no 'mundo de vocês dois', ela depende mais.",
    "tip": "<strong>Sinal de alerta:</strong> isolamento visível e controlador ativa a defesa — e em chave defensiva, é sinal de manipulação/abuso. Reconheça-o em relações reais."
   },
   {
    "ic": "eye",
    "t": "Insinuação: A Carta de Amor",
    "b": "Comunique por <strong>insinuação</strong> — bilhetes, sugestões, referências que só os dois entendem. Evite o direto ('eu te amo, namore comigo'): a mensagem implícita recruta a imaginação da vítima, que se torna co-autora do romance. Isso aprofunda o envolvimento mais que qualquer declaração.",
    "tip": "<strong>Como aplicar:</strong> descreva uma cena, um sentimento vago, uma referência compartilhada — deixe o sujeito implícito. A vítima preenche o espaço com a própria imaginação."
   },
   {
    "ic": "wave",
    "t": "Prazer e Dor — A Montanha-Russa",
    "b": "Alterne ternura com momentos de retração, ciúme leve ou desafio. A <strong>recompensa intermitente</strong> fixa o vínculo mais que o prazer constante — eco do ciclo dopaminérgico. Antecipação &gt; entrega: tente sempre, conceda devagar.",
    "tip": "<strong>Modelo mental:</strong> prazer constante entedia; a alternância prende. A imaginação da vítima, recrutada pelo não-dito, é sempre mais poderosa que a realidade entregue."
   }
  ]
 },
 "ch07-fase3-precipitar": {
  "cards": [
   {
    "ic": "spark",
    "t": "O Inesperado Reacende",
    "b": "Quebre o padrão previsível — <strong>surpreenda</strong>. O cérebro fixa o que é inesperado; a novidade reacende a tensão que a familiaridade apagaria. A previsibilidade é o inimigo do desejo construído nas fases anteriores.",
    "tip": "<strong>Como aplicar:</strong> mude de canal inesperadamente — um gesto diferente, um plano imprevisto, um presente incomum — quando a relação começar a esfriar na rotina."
   },
   {
    "ic": "gap",
    "t": "Ausência Estratégica",
    "b": "Afaste-se <strong>no auge do interesse</strong>. A falta inflama o desejo — a vítima preenche o vácuo idealizando você. 'Distância faz o coração crescer.' Presença constante satura; ausência calculada inflama. A Coquete leva isso ao extremo: é a ausência como personagem permanente.",
    "tip": "<strong>Modelo mental:</strong> não confunda ausência estratégica com sumiço real — o primeiro mantém o mistério; o segundo apenas afasta."
   },
   {
    "ic": "sword",
    "t": "Audácia Cronometrada",
    "b": "No momento da hesitação, um gesto ousado e <strong>decidido</strong> — não tímido, não pedido — rompe a indecisão e empura a relação ao próximo nível. A timidez aqui é fatal. A audácia bem-cronometrada (sem as fases 1–2 por trás) é invasão; com elas, é irresistível.",
    "tip": "<strong>Regra:</strong> a hesitação é contagiosa — a audácia também. Assuma a iniciativa decidida e o outro tende a seguir."
   }
  ]
 },
 "ch08-fase4-o-tombo": {
  "cards": [
   {
    "ic": "leaf",
    "t": "Regressão e Ilusão",
    "b": "Induza um estado de <strong>dependência e entrega</strong> — cuidado, ternura, nostalgia — em que a vítima baixa as defesas adultas e se abandona ao vínculo. Sustente a fantasia criada; não deixe a rotina e a literalidade matarem o encanto. O desejo vive da idealização.",
    "tip": "<strong>Sinal de alerta:</strong> regressão + isolamento + dependência são exatamente os sinais de uma relação manipuladora/abusiva. Reconheça-os como defesa."
   },
   {
    "ic": "spark",
    "t": "O Golpe Final",
    "b": "No auge da entrega, o gesto que <strong>consuma</strong> a sedução — a iniciativa decidida que fecha o arco. Nem cedo demais (sem o vínculo), nem tarde (quando o interesse esfria). O timing do golpe final é tanto arte quanto as fases anteriores.",
    "tip": "<strong>Como aplicar:</strong> o golpe final é sempre uma ação, não uma declaração — um gesto concreto que traduz o que foi construído."
   },
   {
    "ic": "gap",
    "t": "Evite o Anticlímax",
    "b": "O erro fatal pós-conquista: relaxar e cair na previsibilidade. A <strong>rotina desfaz</strong> tudo o que as fases anteriores construíram. Sedutores que mantiveram o poder nunca se tornaram totalmente previsíveis — preservavam uma reserva de mistério que renovava o desejo. O fim da sedução exige tanto cálculo quanto o começo.",
    "tip": "<strong>Regra:</strong> a conquista não é o fim do trabalho. O anticlímax ressuscita o Anti-Sedutor justamente quando você baixa a guarda."
   }
  ]
 },
 "ch09-lente-analitica": {
  "cards": [
   {
    "ic": "eye",
    "t": "Nomeie a Dinâmica",
    "b": "Reconhecer a <strong>ausência estratégica</strong> de um pretendente, a <strong>prova social</strong> de uma marca-Estrela, o <strong>carisma</strong> de um líder, a <strong>Coquete</strong> que adia para prender — nomear a dinâmica <strong>devolve a você a escolha</strong>. Você para de ser conduzido e começa a decidir.",
    "tip": "<strong>Modelo mental:</strong> o valor analítico supera o prescritivo — entender como a influência opera é mais poderoso que seguir um roteiro."
   },
   {
    "ic": "mask",
    "t": "Marketing, Política e Liderança",
    "b": "Os 9 tipos operam em todos os contextos: a <strong>marca-Estrela</strong> é tela de projeção do consumidor, o <strong>líder Carismático</strong> vende sentido e pertencimento, o <strong>Natural</strong> da política desarma pela autenticidade percebida. A sedução não é só interpessoal — é a gramática da influência em escala.",
    "tip": "<strong>Como aplicar:</strong> ao analisar um líder, marca ou movimento, pergunte: qual dos 9 tipos está sendo encarnado? Que carência do público está sendo explorada?"
   },
   {
    "ic": "scale",
    "t": "O Uso Ético",
    "b": "A leitura analítica serve para <strong>entender e se defender</strong>, não para manipular. A linha entre influência legítima e manipulação é a transparência sobre a própria intenção e o respeito pela autonomia do outro. Reconhecer a dinâmica é o que permite escolher conscientemente entrar ou sair.",
    "tip": "<strong>Regra:</strong> 'que carência minha isto explora?' — essa pergunta é o antídoto contra ser conduzido. Nomear o jogo é recuperar o controle."
   }
  ]
 }
}
```
