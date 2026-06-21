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

# LIVRO PARA APROFUNDAR: A Revolução dos Bichos — George Orwell

**Subtítulo:** VISÃO GERAL · A ALEGORIA DA REVOLUÇÃO TRAÍDA
**Ideia central:** Os animais da Granja do Solar expulsam o fazendeiro e fundam uma sociedade igualitária sob o Animalismo e os Sete Mandamentos. Mas os porcos vão corrompendo o ideal passo a passo — reescrevem a lei, exploram o rebanho, mandam o leal Sansão ao matadouro — até a igualdade virar 'alguns são mais iguais que os outros'. Fábula de Orwell sobre como uma revolução de libertação se converte em tirania.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-sonho-do-major-animalismo` — CAPÍTULO 1: O Sonho de Major e o Animalismo
- `ch02-rebeliao-sete-mandamentos` — CAPÍTULO 2: A Rebelião e os Sete Mandamentos
- `ch03-trabalho-leite-privilegio` — CAPÍTULO 3: O Trabalho, o Leite e o Primeiro Privilégio
- `ch04-batalha-do-estabulo` — CAPÍTULO 4: A Batalha do Estábulo
- `ch05-cisao-napoleao-bola-de-neve` — CAPÍTULO 5: A Cisão — Napoleão × Bola-de-Neve
- `ch06-moinho-reescrita-mandamentos` — CAPÍTULO 6: O Moinho e a Reescrita dos Mandamentos
- `ch07-fome-expurgos-confissoes` — CAPÍTULO 7: Fome, Expurgos e Confissões
- `ch08-culto-batalha-do-moinho` — CAPÍTULO 8: O Culto ao Líder e a Batalha do Moinho
- `ch09-sansao-final-mais-iguais` — CAPÍTULO 9: O Destino de Sansão e o Final

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-sonho-do-major-animalismo": {
  "cards": [
   {
    "ic": "bulb",
    "t": "O Sonho de Major",
    "b": "O porco-patriarca (alegoria de <strong>Marx/Lênin</strong>) sonha uma vida sem o homem que rouba o fruto do trabalho. Morre antes da revolução — e o vácuo do profeta é onde o poder se infiltra.",
    "tip": "<strong>Modelo mental:</strong> toda tirania começa capturando um ideal verdadeiro, não inventando um falso."
   },
   {
    "ic": "wave",
    "t": "'Bichos da Inglaterra'",
    "b": "O hino da revolução (a Internacional em fábula): canto de esperança capaz de <strong>unir e mobilizar</strong> — e que depois será proibido quando deixar de convir ao poder.",
    "tip": "<strong>Para refletir:</strong> um slogan ou hino é ferramenta de mobilização — e, por isso, também de manipulação."
   },
   {
    "ic": "person",
    "t": "O Homem como Inimigo",
    "b": "'O homem é a única criatura que consome sem produzir.' A análise é simples e poderosa — e planta a <strong>semente do dogma</strong> que os porcos depois manipularão a seu favor.",
    "tip": "<strong>Modelo mental:</strong> o profeta que sonha e o herdeiro que governa raramente são o mesmo."
   }
  ]
 },
 "ch02-rebeliao-sete-mandamentos": {
  "cards": [
   {
    "ic": "spark",
    "t": "A Rebelião",
    "b": "Jones esquece de alimentar os animais; a fome detona a revolta e ele é expulso. A <strong>vitória vem cedo</strong> (a Revolução Russa de 1917) — é o ponto mais alto da granja. Tudo depois é declínio disfarçado de progresso.",
    "tip": "<strong>Modelo mental:</strong> a conquista da revolução é seu ponto mais frágil — é onde se decide quem escreve as regras."
   },
   {
    "ic": "book",
    "t": "Os Sete Mandamentos",
    "b": "A lei suprema, em letras brancas no celeiro. O sétimo e mais belo: <strong>'Todos os animais são iguais.'</strong> É a maior conquista e o futuro alvo da fraude — pois a maioria não sabe ler para cobrá-la.",
    "tip": "<strong>Regra:</strong> uma constituição só protege se a maioria puder lê-la e cobrá-la."
   },
   {
    "ic": "mountain",
    "t": "Os Porcos à Frente",
    "b": "Por serem 'os mais espertos', os porcos assumem a organização. A <strong>separação entre quem pensa e quem trabalha</strong> nasce no dia um — e o leite ordenhado já some discretamente para a ração deles.",
    "tip": "<strong>Para refletir:</strong> o privilégio começa pequeno e 'justificável', não com um golpe escancarado."
   }
  ]
 },
 "ch03-trabalho-leite-privilegio": {
  "cards": [
   {
    "ic": "steps",
    "t": "'Trabalharei Mais'",
    "b": "Sem o homem, todos se esforçam mais; o cavalo <strong>Sansão</strong> dobra a jornada com seu lema 'Trabalharei mais'. A energia da revolução é real — e sua virtude será também o que o regime explora.",
    "tip": "<strong>Modelo mental:</strong> a virtude do trabalhador, descolada de poder e leitura crítica, vira combustível da casta dominante."
   },
   {
    "ic": "triangle",
    "t": "O Leite e as Maçãs",
    "b": "O primeiro fruto desviado: leite e maçãs vão só para os porcos, sob o argumento de que 'o cérebro que administra precisa'. O <strong>privilégio mínimo que abre todos os outros</strong>.",
    "tip": "<strong>Para refletir:</strong> a exploração mais durável é a que se apresenta como serviço prestado ao explorado."
   },
   {
    "ic": "mask",
    "t": "A Retórica de Garganta",
    "b": "Garganta não espera a revolta: antecipa-a. Transforma o privilégio em <strong>sacrifício</strong> ('nem gostamos de leite, fazemos por vocês') e cala a crítica com a chantagem: 'querem o Sr. Jones de volta?'",
    "tip": "<strong>Modelo mental:</strong> o medo do passado é a chantagem que neutraliza a crítica ao presente."
   }
  ]
 },
 "ch04-batalha-do-estabulo": {
  "cards": [
   {
    "ic": "sword",
    "t": "O Mito Fundador",
    "b": "Os animais emboscam os homens de Jones e os põem em fuga. A batalha vira <strong>data sagrada</strong>, com honras e medalhas — o capital simbólico que legitima a granja (a Guerra Civil Russa em fábula).",
    "tip": "<strong>Modelo mental:</strong> quem controla a memória do mito fundador controla a própria legitimidade."
   },
   {
    "ic": "target",
    "t": "O Heroísmo de Bola-de-Neve",
    "b": "<strong>Bola-de-Neve</strong> (alegoria de Trótski) planeja a defesa, lidera a investida e é ferido; ganha a condecoração de 'Herói-Animal'. Seu heroísmo é documentado — para depois ser apagado.",
    "tip": "<strong>Para refletir:</strong> o heroísmo registrado de hoje pode virar o 'crime' de amanhã — basta controlar quem conta a história."
   },
   {
    "ic": "person",
    "t": "A Bondade de Sansão",
    "b": "Sansão luta com a força dos cascos e fica <strong>horrorizado por crer ter matado um homem</strong>. Sua compaixão contrasta com a frieza futura de Napoleão — que, nesta batalha, sequer brilha.",
    "tip": "<strong>Modelo mental:</strong> uma ameaça externa real é o cimento mais forte de um regime — e a tentação de fabricá-la quando falta."
   }
  ]
 },
 "ch05-cisao-napoleao-bola-de-neve": {
  "cards": [
   {
    "ic": "fork",
    "t": "Ideia × Força",
    "b": "Bola-de-Neve vence pela eloquência e pelo projeto do moinho. Napoleão (alegoria de <strong>Stálin</strong>), sem talento oratório, responde soltando os cães. Sob a tirania, <strong>o melhor argumento perde para o melhor cão de guarda</strong>.",
    "tip": "<strong>Modelo mental:</strong> a tirania não vence o debate — ela o encerra, trocando o argumento pela ameaça."
   },
   {
    "ic": "sword",
    "t": "Os Nove Cães",
    "b": "Filhotes que Napoleão tirou das mães e criou à parte: a <strong>polícia secreta</strong> (NKVD), força bruta leal só a ele. É o passo que converte influência em poder absoluto.",
    "tip": "<strong>Para refletir:</strong> criar uma força leal só a si é o que transforma um líder em um tirano."
   },
   {
    "ic": "pivot",
    "t": "O Roubo da Ideia",
    "b": "Napoleão rejeita o moinho de Bola-de-Neve e, semanas depois, <strong>adota-o como se fosse seu</strong>. As assembleias são abolidas: dali em diante, um comitê de porcos decide tudo.",
    "tip": "<strong>Modelo mental:</strong> o ditador rouba as ideias do rival depois de eliminá-lo, apresentando-as como próprias."
   }
  ]
 },
 "ch06-moinho-reescrita-mandamentos": {
  "cards": [
   {
    "ic": "book",
    "t": "A Reescrita da Lei",
    "b": "'Nenhum animal dormirá numa cama' amanhece com duas palavras a mais: <strong>'...com lençóis'</strong>. A constituição vira documento vivo, manipulado para legitimar o privilégio. A lei dobra-se ao crime, não o contrário.",
    "tip": "<strong>Modelo mental:</strong> quem controla o texto da lei e sua leitura controla a realidade."
   },
   {
    "ic": "eye",
    "t": "A Memória Contra a Evidência",
    "b": "Os animais lembram vagamente que o mandamento era outro, mas Garganta lê a versão atual em voz alta — e a <strong>dúvida deles cede à autoridade dele</strong>. Sem registro independente, a memória é sobrescrita.",
    "tip": "<strong>Para refletir:</strong> a memória coletiva, sem registro, é facilmente reescrita por quem detém o microfone."
   },
   {
    "ic": "link",
    "t": "Comércio com o Inimigo",
    "b": "Napoleão passa a negociar com humanos pelo intermediário Whymper — exatamente o que Major proibira. O <strong>ideal já se dissolveu na conveniência</strong>; a granja 'pura' depende do mundo dos homens.",
    "tip": "<strong>Modelo mental:</strong> a traição do ideal não é um golpe, é uma sequência de exceções 'razoáveis'."
   }
  ]
 },
 "ch07-fome-expurgos-confissoes": {
  "cards": [
   {
    "ic": "clock",
    "t": "Os Expurgos",
    "b": "Animais admitem traições impossíveis — conluio com Bola-de-Neve — e os cães os dilaceram diante de todos. É o eco dos <strong>Processos de Moscou</strong>: o medo substitui a lei e a revolução devora os próprios filhos.",
    "tip": "<strong>Modelo mental:</strong> a confissão forçada não busca a verdade — busca o espetáculo do terror, que ensina a obedecer."
   },
   {
    "ic": "lens",
    "t": "O Bode Expiatório",
    "b": "Tudo o que dá errado é atribuído a Bola-de-Neve, agora 'agente de Jones desde sempre'. O <strong>inimigo invisível justifica qualquer crueldade</strong> e nunca aparece para se defender.",
    "tip": "<strong>Para refletir:</strong> quando todo problema interno é culpa de um traidor externo que nunca surge, há um bode expiatório em ação."
   },
   {
    "ic": "book",
    "t": "'...Sem Motivo'",
    "b": "O sexto mandamento ganha um adendo: 'Nenhum animal matará outro animal <strong>sem motivo</strong>', legitimando o massacre. E 'Bichos da Inglaterra' é proibido — a esperança silenciada por decreto.",
    "tip": "<strong>Modelo mental:</strong> quando a lei contra a violência é emendada para permiti-la, o regime já não tem freio interno."
   }
  ]
 },
 "ch08-culto-batalha-do-moinho": {
  "cards": [
   {
    "ic": "constellation",
    "t": "O Culto à Personalidade",
    "b": "Napoleão é 'Líder', 'Pai de Todos os Animais'; o poeta Mínimo compõe odes a ele. A <strong>figura do tirano substitui o ideal coletivo</strong> e a infalibilidade ('Napoleão está sempre certo') torna a crítica heresia.",
    "tip": "<strong>Modelo mental:</strong> o culto desloca a lealdade do ideal para a pessoa — e uma pessoa redefine o ideal a seu bel-prazer."
   },
   {
    "ic": "mask",
    "t": "Derrota Vendida como Vitória",
    "b": "A Batalha do Moinho é um desastre — o moinho explode, muitos morrem (a invasão nazista em fábula) —, mas Garganta a anuncia como <strong>triunfo</strong>, e os exaustos animais aplaudem, convencidos de que venceram.",
    "tip": "<strong>Para refletir:</strong> com o povo exausto e sem informação, a propaganda consegue vender a derrota como vitória."
   },
   {
    "ic": "scale",
    "t": "'...Em Excesso'",
    "b": "Os porcos descobrem o uísque de Jones; 'Nenhum animal beberá álcool' amanhece com '<strong>...em excesso</strong>'. E Napoleão alterna entre Frederico (Hitler) e Pilkington (o Ocidente): o regime não tem princípios, só conveniências.",
    "tip": "<strong>Modelo mental:</strong> o oportunismo diplomático expõe que o regime não tem princípios, só interesses."
   }
  ]
 },
 "ch09-sansao-final-mais-iguais": {
  "cards": [
   {
    "ic": "pin",
    "t": "A Carroça do Açougueiro",
    "b": "Sansão deu tudo ('Trabalharei mais') e é descartado quando deixa de ser útil: vendido por uísque. Benjamim, o burro cético, lê tarde demais a placa na carroça. O <strong>destino do crente sincero sob a tirania</strong>.",
    "tip": "<strong>Modelo mental:</strong> a tirania descarta seus servidores mais leais assim que eles param de produzir."
   },
   {
    "ic": "key",
    "t": "'Mais Iguais que os Outros'",
    "b": "Os Sete Mandamentos somem, substituídos por uma frase única: <strong>'Todos os animais são iguais, mas alguns são mais iguais que os outros.'</strong> O epitáfio da revolução traída — a igualdade virou sua própria paródia.",
    "tip": "<strong>Para refletir:</strong> o totalitarismo não abandona a linguagem dos ideais; ele a esvazia por dentro."
   },
   {
    "ic": "spiral",
    "t": "Porcos = Humanos",
    "b": "Na cena final, porcos jogam cartas com humanos e brigam por uma trapaça; os animais, espiando pela janela, <strong>já não sabem quem é porco e quem é homem</strong>. A granja voltou a ser a Granja do Solar.",
    "tip": "<strong>Modelo mental:</strong> a revolução que não muda a estrutura do poder apenas troca seu dono — que se torna igual ao antigo."
   }
  ]
 }
}
```
