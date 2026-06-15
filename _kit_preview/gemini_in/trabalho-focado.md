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

# LIVRO PARA APROFUNDAR: Trabalho Focado — Cal Newport

**Subtítulo:** VISÃO GERAL · REGRAS PARA O SUCESSO FOCADO NUM MUNDO DISTRAÍDO
**Ideia central:** Na economia do conhecimento, a capacidade de focar sem distração ficou rara — e justamente por isso, valiosa. Cal Newport chama isso de superpoder do século 21: o trabalho profundo cria valor, aprimora a habilidade e é difícil de copiar. O livro separa o profundo do superficial e dá quatro regras para reconstruir a concentração num mundo que conspira contra ela.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-o-trabalho-profundo-e-valioso` — CAPÍTULO 1: O Trabalho Profundo é Valioso
- `ch02-o-trabalho-profundo-e-raro` — CAPÍTULO 2: O Trabalho Profundo é Raro
- `ch03-o-trabalho-profundo-e-significativo` — CAPÍTULO 3: O Trabalho Profundo é Significativo
- `ch04-regra-1-trabalhe-profundamente` — CAPÍTULO 4: Regra 1 — Trabalhe Profundamente
- `ch05-regra-2-abrace-o-tedio` — CAPÍTULO 5: Regra 2 — Abrace o Tédio
- `ch06-regra-3-abandone-as-redes-sociais` — CAPÍTULO 6: Regra 3 — Abandone as Redes Sociais
- `ch07-regra-4-drene-o-raso` — CAPÍTULO 7: Regra 4 — Drene o Raso

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-o-trabalho-profundo-e-valioso": {
  "cards": [
   {
    "ic": "target",
    "t": "As 2 Habilidades Centrais",
    "b": "A economia muda rápido, e duas competências decidem quem prospera: <strong>dominar coisas difíceis depressa</strong> (aprender) e <strong>produzir em nível de elite</strong> (qualidade + velocidade). Sem foco intenso, nenhuma das duas é possível.",
    "tip": "<strong>Como aplicar:</strong> escolha onde investir tempo de carreira pela alavanca dessas duas habilidades — não pela atividade visível."
   },
   {
    "ic": "spark",
    "t": "Aprender pela Prática Deliberada",
    "b": "Você domina coisas difíceis com <strong>atenção focada na habilidade exata</strong> e <strong>feedback que corrige a rota</strong>. A distração é inimiga direta do aprendizado: o cérebro só isola (mieliniza) os circuitos que você ativa em foco.",
    "tip": "<strong>Para refletir:</strong> aprendizado de elite exige foco ininterrupto — não há atalho em ambiente fragmentado."
   },
   {
    "ic": "scale",
    "t": "Lei da Produtividade",
    "b": "<strong>Trabalho de Alta Qualidade = Tempo × Intensidade do Foco.</strong> Maximizar a intensidade comprime o tempo. Foco fragmentado, mesmo por muitas horas, produz pouco.",
    "tip": "<strong>Modelo mental:</strong> trate a intensidade como multiplicador — uma hora concentrada vale várias hora dispersas."
   },
   {
    "ic": "gap",
    "t": "Atenção Residual",
    "b": "Ao trocar da tarefa A para a B, parte da atenção fica <strong>presa em A</strong>. A multitarefa e a troca constante reduzem a performance cognitiva e impõem um imposto invisível ao seu cérebro.",
    "tip": "<strong>Regra:</strong> termine (ou estacione formalmente) uma tarefa antes de abrir a próxima — evite deixar resíduo."
   }
  ]
 },
 "ch02-o-trabalho-profundo-e-raro": {
  "cards": [
   {
    "ic": "eye",
    "t": "A Métrica Negra",
    "b": "O valor do foco e o custo da distração são <strong>quase impossíveis de medir</strong> nas empresas. Sem métrica clara, prevalece o que é cômodo, não o que é eficaz.",
    "tip": "<strong>Para aplicar:</strong> quando faltar métrica, defina a sua própria — não deixe o 'menor esforço' decidir por você."
   },
   {
    "ic": "wave",
    "t": "O Princípio do Menor Esforço",
    "b": "Sem feedback claro sobre o impacto no resultado, tendemos ao <strong>comportamento mais fácil no momento</strong>: responder e-mail na hora, ficar 'disponível', reunir sem fim.",
    "tip": "<strong>Regra:</strong> trate 'estar sempre disponível' como custo, não como virtude."
   },
   {
    "ic": "clock",
    "t": "Ocupação como Produtividade",
    "b": "Sem saber medir produtividade, demonstra-se produtividade <strong>fazendo muitas coisas visivelmente</strong> — a atividade vira teatro. 'Ocupado' virou prova social de 'produtivo'.",
    "tip": "<strong>Para refletir:</strong> sentir-se produtivo o dia todo sem criar nada novo é o sintoma clássico da superficialidade."
   },
   {
    "ic": "link",
    "t": "O Culto da Internet",
    "b": "Presume-se que qualquer ferramenta 'de ponta' (redes, chat constante) é boa por definição; questionar é parecer atrasado. Toda nova tecnologia é tida como progresso, esvaziando o juízo sobre seu <strong>custo de atenção</strong>.",
    "tip": "<strong>Modelo mental:</strong> tornar-se focado num ambiente que premia a distração é, justamente, a vantagem competitiva."
   }
  ]
 },
 "ch03-o-trabalho-profundo-e-significativo": {
  "cards": [
   {
    "ic": "eye",
    "t": "Argumento Neurológico",
    "b": "O que você dá atenção <strong>molda sua experiência de mundo</strong>. Foco em coisas profundas constrói um mundo rico de sentido; atenção fragmentada constrói um mundo de pequenas frustrações e ansiedades.",
    "tip": "<strong>Modelo mental:</strong> a atenção é o pincel que pinta a sua vida — 'seremos aquilo a que prestamos atenção'."
   },
   {
    "ic": "spiral",
    "t": "Argumento Psicológico (Flow)",
    "b": "As melhores experiências vêm do <strong>flow</strong>: absorção total numa tarefa desafiadora à altura da habilidade. Paradoxo: o trabalho dá mais flow que o lazer passivo — e o trabalho profundo é uma máquina de gerar flow.",
    "tip": "<strong>Para aplicar:</strong> busque o ponto desafio = habilidade — nem tédio (fácil demais) nem ansiedade (difícil demais)."
   },
   {
    "ic": "leaf",
    "t": "Argumento Filosófico (Ofício)",
    "b": "O sentido não está só no 'o quê', mas no 'como'. Tarefas comuns, executadas com <strong>maestria e cuidado</strong>, geram significado — o ofício bem-feito revela um sentido que já estava no trabalho.",
    "tip": "<strong>Para refletir:</strong> mais foco profundo costuma trazer mais satisfação que mais ócio."
   }
  ]
 },
 "ch04-regra-1-trabalhe-profundamente": {
  "cards": [
   {
    "ic": "clock",
    "t": "Os 4 Ritmos do Foco",
    "b": "<strong>Monástico</strong>: elimina quase todo o raso (objetivo único). <strong>Bimodal</strong>: blocos longos de reclusão alternados com tempo aberto. <strong>Rítmico</strong>: hábito diário em horário fixo — o mais sustentável. <strong>Jornalístico</strong>: encaixar foco em qualquer brecha (avançado).",
    "tip": "<strong>Como escolher:</strong> a maioria prospera com o ritmo rítmico — a regularidade vence a inspiração."
   },
   {
    "ic": "wrench",
    "t": "Ritualizar (não improvisar)",
    "b": "Defina antes <strong>onde</strong> (local e duração), <strong>como</strong> (regras: sem internet, metas por bloco) e <strong>com que apoio</strong> (café, materiais, caminhada). Rituais poupam força de vontade — você não decide, você executa.",
    "tip": "<strong>Grande aposta:</strong> investimento radical (hotel, retiro) que eleva a importância psicológica e força o foco. Usar com parcimônia."
   },
   {
    "ic": "steps",
    "t": "Execute com o 4DX",
    "b": "Das '4 Disciplinas da Execução': <strong>foque no que é vital</strong>; aja sobre as <strong>medidas de direção</strong> (horas em foco), não só nas de resultado; mantenha um <strong>placar visível</strong>; crie uma <strong>cadência de prestação de contas</strong> (revisão semanal).",
    "tip": "<strong>Modelo mental:</strong> meça as horas de foco (lead measure) — é o que você controla; o resultado vem depois."
   },
   {
    "ic": "pin",
    "t": "Ritual de Fim de Expediente",
    "b": "Ao acabar o dia, <strong>resolva ou registre</strong> toda pendência num plano confiável e diga uma frase de encerramento ('encerramento concluído'). A mente em descanso <strong>recupera o foco e incuba soluções</strong> em segundo plano.",
    "tip": "<strong>Regra:</strong> depois do encerramento, zero trabalho — nem checar e-mail. O descanso restaura a atenção."
   }
  ]
 },
 "ch05-regra-2-abrace-o-tedio": {
  "cards": [
   {
    "ic": "link",
    "t": "Agende a Internet",
    "b": "Não faça pausas da distração; faça <strong>pausas do foco</strong>. Programe blocos em que a internet é permitida e, fora deles, fique 100% offline — inclusive em casa. Uma única espiada quebra o treino.",
    "tip": "<strong>Como aplicar:</strong> anote num papel o próximo horário liberado para internet; até lá, nada online."
   },
   {
    "ic": "target",
    "t": "Treine sob Pressão",
    "b": "Imponha <strong>metas-relâmpago</strong> ('vou terminar isto em 60 min') para forçar intensidade e treinar a resistência à distração. A escassez de tempo é aliada da concentração.",
    "tip": "<strong>Para refletir:</strong> cada cedência à distração é uma repetição na academia errada — você treina o músculo da distração."
   },
   {
    "ic": "spiral",
    "t": "Meditação Produtiva",
    "b": "Ocupe um período físico-mas-não-mental (caminhar, dirigir, banho) com <strong>um único problema profissional</strong> bem definido. Cuidado com loops de distração e com repisar o mesmo ponto — force o avanço estruturando o problema.",
    "tip": "<strong>Modelo mental:</strong> o objetivo não é eliminar o tédio, mas tolerá-lo sem fugir para a tela."
   }
  ]
 },
 "ch06-regra-3-abandone-as-redes-sociais": {
  "cards": [
   {
    "ic": "wrench",
    "t": "A Abordagem do Artesão",
    "b": "Identifique os <strong>poucos objetivos centrais</strong> (pessoais e profissionais); adote uma ferramenta só se seu impacto positivo neles <strong>superar substancialmente</strong> o negativo. Rejeita a 'mentalidade do qualquer-benefício'.",
    "tip": "<strong>Regra:</strong> 'tem coisa útil lá' não basta — pese o custo de atenção contra suas metas centrais."
   },
   {
    "ic": "scale",
    "t": "A Lei dos Poucos Vitais",
    "b": "A regra 80-20: ~<strong>80% de um efeito vem de ~20% das causas</strong>. Identifique as poucas atividades que mais contribuem para suas metas e concentre-se nelas; o resto rouba tempo das que importam.",
    "tip": "<strong>Como aplicar:</strong> liste suas atividades e corte o cauda longa que pouco move suas metas."
   },
   {
    "ic": "clock",
    "t": "O Teste dos 30 Dias",
    "b": "Pare de usar uma rede por <strong>30 dias, sem anunciar</strong>. Ao fim: (1) as semanas teriam sido nitidamente melhores com ela? (2) alguém se importou que você parou? Se 'não' às duas, abandone-a.",
    "tip": "<strong>Para refletir:</strong> recupere o lazer com atividades de qualidade — não terceirize seu tempo livre à internet."
   }
  ]
 },
 "ch07-regra-4-drene-o-raso": {
  "cards": [
   {
    "ic": "steps",
    "t": "Planeje Cada Minuto",
    "b": "<strong>Time blocking</strong>: divida o dia em blocos e atribua a cada um uma tarefa (inclusive raso e descanso). Não é prisão — ao surgir um imprevisto, <strong>replaneje</strong> os blocos restantes. O ponto é decidir, não reagir.",
    "tip": "<strong>Regra:</strong> o plano serve para decidir intencionalmente, não para punir — replaneje sem culpa."
   },
   {
    "ic": "scale",
    "t": "Orçamento de Raso",
    "b": "Defina a fração do tempo permitida para o raso (tipicamente <strong>30–50%</strong>); o que passar do teto, corta-se. Classifique pelo <strong>teste do recém-formado</strong>: 'quantos meses de treino levaria?' Muitos = profundo.",
    "tip": "<strong>Como aplicar:</strong> some suas horas de raso por semana, fixe um teto e comprima o excedente."
   },
   {
    "ic": "clock",
    "t": "Agenda Fixa + E-mail",
    "b": "<strong>Produtividade de agenda fixa</strong>: fixe um fim de expediente rígido (ex.: 17h30) e trabalhe para trás. <strong>Dome o e-mail</strong>: responda de modo a encerrar o assunto (process-centric) e não responda por padrão o que não merece.",
    "tip": "<strong>Modelo mental:</strong> a escassez de tempo é uma restrição criativa — força a eliminar o raso e proteger o profundo."
   }
  ]
 }
}
```
