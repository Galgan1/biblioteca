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

# LIVRO PARA APROFUNDAR: Sociedade do Cansaço — Byung-Chul Han

**Subtítulo:** VISÃO GERAL · AUTOEXPLORAÇÃO, BURNOUT E A SAÍDA PELA SUBTRAÇÃO
**Ideia central:** Saímos da sociedade disciplinar do 'não pode' para a sociedade do desempenho do 'you can'. O resultado é um sujeito que é senhor e escravo de si mesmo, que se autoexplora com sensação de liberdade — até implodir. Byung-Chul Han mostra por que o burnout é a doença de uma época que nega a negatividade.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-violencia-neuronal` — CAPÍTULO 1: A Violência Neuronal
- `ch02-alem-da-sociedade-disciplinar` — CAPÍTULO 2: Além da Sociedade Disciplinar
- `ch03-tedio-profundo` — CAPÍTULO 3: O Tédio Profundo
- `ch04-vita-activa` — CAPÍTULO 4: Vita Activa
- `ch05-pedagogia-do-ver` — CAPÍTULO 5: Pedagogia do Ver
- `ch06-caso-bartleby` — CAPÍTULO 6: O Caso Bartleby
- `ch07-sociedade-do-cansaco` — CAPÍTULO 7: A Sociedade do Cansaço
- `ch08-burnout-senhor-e-escravo` — CAPÍTULO 8: Burnout — Senhor e Escravo de Si

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-violencia-neuronal": {
  "cards": [
   {
    "ic": "gap",
    "t": "Do Viral ao Neuronal",
    "b": "A violência imunológica pressupõe um <em>outro</em> hostil a repelir. A violência neuronal é <strong>imanente ao sistema</strong> — não vem do estranho negativo, mas do <strong>Igual em excesso</strong>. Não se combate com remédios imunológicos.",
    "tip": "<strong>Modelo mental:</strong> pense em 'excesso', não em 'ataque' — quando algo adoece sem inimigo identificável, suspeite de saturação do positivo."
   },
   {
    "ic": "bulb",
    "t": "Excesso de Positividade",
    "b": "O adoecimento atual não nasce do negativo (inimigo, proibição, falta), mas do <strong>positivo em demasia</strong>: excesso de estímulo, informação, desempenho, comunicação. Não é uma negação que mata — é um <em>demais</em> que esgota.",
    "tip": "<strong>Como aplicar:</strong> combater o burnout com mais esforço e positividade é repetir a doença como cura."
   },
   {
    "ic": "lens",
    "t": "O Fim do Paradigma Imunológico",
    "b": "A globalização dissolve a <strong>alteridade forte</strong>; sem o outro propriamente estranho, a reação imunológica perde o objeto. A diferença vira mera diferença domesticada — 'o diferente do Igual'.",
    "tip": "<strong>Modelo mental:</strong> o Igual não imuniza — defesas pensadas para o estranho são inúteis contra o esgotamento do mesmo."
   }
  ]
 },
 "ch02-alem-da-sociedade-disciplinar": {
  "cards": [
   {
    "ic": "sword",
    "t": "Dever → Poder Fazer",
    "b": "A primeira produz por <strong>proibição</strong>; a segunda, por <strong>ilimitação</strong>. Trocamos o 'não pode' pelo 'yes, we can' — e o imperativo 'você pode' esconde a coação 'você tem que conseguir'. Mais liberdade aparente, mais exaustão real.",
    "tip": "<strong>Modelo mental:</strong> procure o capataz interno — quando você se cobra ao colapso sem chefe, a disciplina virou autodesempenho."
   },
   {
    "ic": "person",
    "t": "A Autoexploração",
    "b": "Explorar-se por livre vontade, com <strong>sensação de liberdade</strong>. É mais total e mais perniciosa que a exploração externa: não há sujeito de exploração a derrubar, não há revolta possível. A vítima é cúmplice voluntária.",
    "tip": "<strong>Sinal de alerta:</strong> o freelancer que trabalha noites 'porque quer' e desaba em burnout é o caso exemplar — ninguém o proíbe de parar."
   },
   {
    "ic": "spiral",
    "t": "Guerra Consigo Mesmo",
    "b": "Sem opressor externo, a <strong>agressividade volta-se para dentro</strong>: explorador e explorado são a mesma pessoa. A depressão não é falta do dever — é o fracasso do poder, o colapso de quem se cobrou ilimitadamente.",
    "tip": "<strong>Como aplicar:</strong> sem inimigo externo, suspeite de si — quando não há a quem culpar e mesmo assim você desaba, o explorador é interno."
   }
  ]
 },
 "ch03-tedio-profundo": {
  "cards": [
   {
    "ic": "eye",
    "t": "Multitarefa como Regressão",
    "b": "Não é competência: é o retorno à atenção <strong>animal e dispersa</strong>, dividida entre ameaças. A capacidade de alternar doze abas não é evolução cognitiva — é vigilância de presa disfarçada de produtividade.",
    "tip": "<strong>Sinal de alerta:</strong> a dificuldade de ler um livro inteiro sem parar para o celular é o sintoma direto da extinção da atenção contemplativa."
   },
   {
    "ic": "clock",
    "t": "O Tédio como Ninho Criativo",
    "b": "Walter Benjamin: o tédio é '<strong>o pássaro de sonho que choca o ovo da experiência</strong>'. A inquietude e a atividade nervosas matam a paciência — e com ela tudo o que só amadurece na demora. Tolerar o vazio é condição do profundo.",
    "tip": "<strong>Modelo mental:</strong> pense no demorar-se como produção, não desperdício — o profundo só amadurece quando se permite não fazer nada."
   },
   {
    "ic": "lens",
    "t": "Atenção Profunda × Hiperatenção",
    "b": "A <strong>atenção profunda</strong> (longa, imersa, contemplativa) cede para a <strong>hiperatenção</strong> (rápida troca de foco, intolerante ao tédio). A cultura nasce da primeira; a segunda só pode consumir o que a primeira criou.",
    "tip": "<strong>Como aplicar:</strong> reserve blocos de tempo sem troca de foco — sem notificações, sem alternância; deixe o tédio entrar antes de agir."
   }
  ]
 },
 "ch04-vita-activa": {
  "cards": [
   {
    "ic": "mountain",
    "t": "Hiperatividade como Não-Liberdade",
    "b": "O excesso de atividade é, paradoxalmente, uma forma de <strong>não-liberdade</strong>. Quem só reage, só executa, só corre está tão preso quanto o passivo — é 'ativo' sem ser livre, movido pela compulsão e não pela escolha.",
    "tip": "<strong>Modelo mental:</strong> hiperativo ≠ potente — agitação contínua é compulsão. Suspeite da atividade que não consegue parar."
   },
   {
    "ic": "pivot",
    "t": "A Pausa como Soberania",
    "b": "Ser livre é poder <strong>interromper, hesitar, não reagir</strong>. A capacidade de parar — de recusar a resposta imediata — é mais soberana que a de agir. Quem não consegue parar não é livre: é escravo da ação.",
    "tip": "<strong>Como aplicar:</strong> a pessoa verdadeiramente livre é a que pode dizer 'não vou reagir agora' — cultive essa capacidade."
   },
   {
    "ic": "clock",
    "t": "A Perda do Demorar-se",
    "b": "O <strong>Verweilen</strong> (demorar-se) — permanecer junto ao que se contempla — é a condição da experiência plena. A aceleração transforma o tempo em sucessão de presentes pontuais, sem duração, destruindo toda experiência que exige permanência.",
    "tip": "<strong>Modelo mental:</strong> agenda lotada, zero tempo morto = sinal de servidão, não de potência."
   }
  ]
 },
 "ch05-pedagogia-do-ver": {
  "cards": [
   {
    "ic": "eye",
    "t": "Aprender a Ver",
    "b": "A primeira tarefa da cultura: '<strong>habituar o olho à calma, à paciência, ao deixar-as-coisas-virem-a-nós</strong>' (Nietzsche). O contrário — reagir a todo estímulo — é doença e esgotamento.",
    "tip": "<strong>Como aplicar:</strong> deixar uma notificação sem resposta por uma hora é um exercício de liberdade — pratique a demora deliberada."
   },
   {
    "ic": "scale",
    "t": "Potência Negativa",
    "b": "A verdadeira soberania é negativa: poder <strong>interromper, recusar, deixar passar</strong>. Distingue-se da impotência: impotência é fraqueza; potência negativa é a força ativa de suspender o impulso.",
    "tip": "<strong>Modelo mental:</strong> distinga 'não poder' de 'poder não' — o primeiro é fraqueza; o segundo é liberdade soberana."
   },
   {
    "ic": "gap",
    "t": "A Hesitação como Inteligência",
    "b": "O <strong>intervalo</strong> entre estímulo e resposta é onde mora o pensamento. Encurtá-lo a zero é regredir ao reflexo. A compulsão à reação imediata elimina toda demora e mata o pensamento antes de começar.",
    "tip": "<strong>Sinal de alerta:</strong> ter opinião imediata sobre tudo no feed, responder mensagem no segundo em que chega — ninguém ali está vendo; todos estão reagindo."
   }
  ]
 },
 "ch06-caso-bartleby": {
  "cards": [
   {
    "ic": "book",
    "t": "Bartleby como Figura Disciplinar",
    "b": "O sofrimento de Bartleby é da <strong>negatividade</strong> (a parede, o muro, a recusa) — não do excesso de positividade. O ambiente quase carcerário de Wall Street é o mundo disciplinar foucaultiano. Ele adoece <em>contra</em> a ordem; o sujeito de desempenho adoece <em>cumprindo</em> a ordem que ele mesmo se dá.",
    "tip": "<strong>Como aplicar:</strong> use Bartleby como contraprova histórica — ele serve para datar a doença: pertence ao ontem disciplinar; o burnout pertence ao hoje do desempenho."
   },
   {
    "ic": "lens",
    "t": "Han Rejeita a Leitura Messiânica",
    "b": "Agamben e Deleuze veem no 'preferiria não' uma <strong>potência ontológica pura</strong>. Han discorda: é caso patológico de uma época específica, não herói da potência negativa. A recusa de Bartleby é colapso, não liberdade soberana.",
    "tip": "<strong>Modelo mental:</strong> cuidado com a romantização da recusa — nem toda recusa é potência; a de Bartleby é paralisia sem mundo."
   },
   {
    "ic": "triangle",
    "t": "A Doença Mudou de Lógica",
    "b": "O empregado disciplinar adoecia <em>contra</em> a ordem (resistia, definhava na parede); o sujeito de desempenho adoece <em>cumprindo</em> a ordem que ele mesmo se dá. <strong>Confundir os dois é tratar o esgotamento de hoje com a terapêutica de ontem.</strong>",
    "tip": "<strong>Sinal de alerta:</strong> oferecer 'mais autonomia' como cura do burnout pode aprofundá-lo — se a coação é interna, mais liberdade vira mais pressão."
   }
  ]
 },
 "ch07-sociedade-do-cansaco": {
  "cards": [
   {
    "ic": "gap",
    "t": "O Cansaço que Divide",
    "b": "O esgotamento do desempenho (<em>Ich-Müdigkeit</em>) é <strong>solitário e violento</strong>: incapacita para a fala, para o olhar, para a comunidade. É o cansaço do 'eu' que se exauriu sozinho — um cansaço da violência que separa.",
    "tip": "<strong>Sinal de alerta:</strong> o cansaço do domingo à noite, ansioso e solitário, que já antecipa a semana — esse é o Ich-Müdigkeit."
   },
   {
    "ic": "wave",
    "t": "O Cansaço que Reconcilia",
    "b": "O <strong>cansaço fundamental</strong> (Handke) é eloquente e sereno: <strong>abre</strong> o eu, afrouxa a tirania do ego e devolve a confiança. É um cansaço da paz, não da violência; do 'nós', não do 'eu'. Longe de incapacitar, ele inspira.",
    "tip": "<strong>Modelo mental:</strong> o cansaço bom de uma longa caminhada com amigos, em que se fica em silêncio juntos sem pressa — esse é o cansaço que reconcilia."
   },
   {
    "ic": "leaf",
    "t": "A Comunidade do Cansaço",
    "b": "Contra a exaustão patológica, Han vislumbra uma <strong>comunidade do cansaço fundamental</strong> — um 'estar-cansado' partilhado que dissolve o isolamento. O cansaço bom é uma forma de demorar-se e de contemplação — a 'menos-ação' que refaz o vínculo.",
    "tip": "<strong>Como aplicar:</strong> distinga os dois cansaços: o que te isola é doença; o que te abre e serena, cuida."
   }
  ]
 },
 "ch08-burnout-senhor-e-escravo": {
  "cards": [
   {
    "ic": "triangle",
    "t": "Depressão como Fracasso do Poder",
    "b": "A depressão não é falta do <em>dever</em> — é o <strong>fracasso do poder</strong>: o colapso de quem se exauriu tentando ser ele mesmo de forma ilimitada. O depressivo não transgrediu uma proibição; não conseguiu cumprir o imperativo de desempenho que ele mesmo se impôs.",
    "tip": "<strong>Modelo mental:</strong> sem inimigo externo, suspeite de si — quando não há a quem culpar e você desaba, o explorador é interno."
   },
   {
    "ic": "spiral",
    "t": "O Infarto da Alma",
    "b": "Sem o negativo (o outro, o limite, a recusa), o sujeito perde a forma e se dissolve no excesso de si mesmo. O eu <strong>cheio de si, sem fora, entra em curto</strong>. A perda de rituais e formas que fecham torna o desempenho um processo aberto e infinito — e o infinito sem forma é a fórmula do esgotamento.",
    "tip": "<strong>Sinal de alerta:</strong> a frase reveladora é 'eu mesmo me cobro' — ali está o senhor-escravo de si que Han descreve."
   },
   {
    "ic": "leaf",
    "t": "A Cura é por Subtração",
    "b": "O que esgota é o <em>demais</em> — a terapêutica é <strong>menos</strong> (limite, pausa, forma), não mais esforço. Reintroduzir o negativo (o não, a fronteira, o intervalo) é o que permite ao eu recuperar a forma e descansar.",
    "tip": "<strong>Como aplicar:</strong> a cura começa por reintroduzir o limite, a pausa, o não — não por aumentar a positividade."
   }
  ]
 }
}
```
