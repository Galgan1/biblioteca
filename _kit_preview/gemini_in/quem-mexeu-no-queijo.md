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

# LIVRO PARA APROFUNDAR: Quem Mexeu no Meu Queijo? — Spencer Johnson

**Subtítulo:** VISÃO GERAL · A PARÁBOLA DA MUDANÇA
**Ideia central:** Uma fábula curta sobre quatro personagens num labirinto à procura de Queijo — metáfora do que queremos na vida. Dois ratos, Sniff e Scurry, agem com simplicidade; dois duendes, Hem e Haw, complicam com crenças e medo. Quando o Queijo some, descobrimos quem somos diante da mudança — e como antecipá-la, monitorá-la e nos adaptar a tempo.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-quatro-personagens` — CAPÍTULO 1: Os Quatro Personagens
- `ch02-queijo-e-labirinto` — CAPÍTULO 2: O Queijo e o Labirinto
- `ch03-nao-ha-queijo` — CAPÍTULO 3: Não Há Queijo!
- `ch04-vencendo-o-medo` — CAPÍTULO 4: Vencendo o Medo
- `ch05-manuscrito-na-parede` — CAPÍTULO 5: O Manuscrito na Parede
- `ch06-novo-queijo` — CAPÍTULO 6: Saboreando o Novo Queijo
- `ch07-aplicacoes` — CAPÍTULO 7: Aplicações (O Debate)

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-quatro-personagens": {
  "cards": [
   {
    "ic": "fork",
    "t": "Ratos e Duendes",
    "b": "Dois <strong>ratos</strong> (cérebro simples, instinto aguçado) e dois <strong>duendes</strong> (cérebro complexo, cheio de crenças). Sniff fareja, Scurry corre; Hem resiste, Haw se adapta.",
    "tip": "<strong>Como aplicar:</strong> identifique qual personagem você encarna a cada sinal de mudança."
   },
   {
    "ic": "spark",
    "t": "A Vantagem da Simplicidade",
    "b": "Os ratos vencem não por serem mais espertos (humanos são mais inteligentes que ratos), mas por <strong>manterem as coisas simples</strong>: o queijo sumiu, então mude.",
    "tip": "<strong>Regra:</strong> simplicidade é força, não burrice; análise demais paralisa."
   },
   {
    "ic": "eye",
    "t": "O Cérebro que Atrapalha",
    "b": "A mesma capacidade de pensar que ajuda os duendes é a que os afunda quando <strong>crenças e emoções assumem o comando</strong> e transformam um fato simples num drama de injustiça.",
    "tip": "<strong>Sinal de alerta:</strong> quando o pensamento vira sofrimento, o cérebro complexo assumiu o volante."
   },
   {
    "ic": "clock",
    "t": "Mesma Situação, Dois Destinos",
    "b": "Sniff e Scurry inspecionavam o Posto C toda manhã e viram o estoque diminuir; Hem e Haw chegavam de chinelos e nem perceberam. Quando o queijo some, os ratos <strong>já estão calçando os tênis</strong>.",
    "tip": "<strong>Lição:</strong> inteligência não é adaptação — quem não se adapta a tempo talvez nunca se adapte."
   }
  ]
 },
 "ch02-queijo-e-labirinto": {
  "cards": [
   {
    "ic": "target",
    "t": "O Que é o Queijo",
    "b": "O Queijo é <strong>o que queremos ter na vida</strong>: emprego, relacionamento, dinheiro, casa, liberdade, saúde, reconhecimento, paz espiritual. O Labirinto é onde você o procura — a empresa, a sociedade, as relações.",
    "tip": "<strong>Como aplicar:</strong> nomeie o seu Queijo. Saber o que teme perder torna o medo concreto e tratável."
   },
   {
    "ic": "scale",
    "t": "A Arrogância do Sucesso",
    "b": "Ter Queijo por muito tempo gera confiança → arrogância → cegueira. “Pouco a pouco a confiança de Hem e Haw se transformou em <strong>arrogância</strong>.”",
    "tip": "<strong>Sinal de alerta:</strong> quando você se sente seguro e merecedor demais, parou de cheirar o queijo."
   },
   {
    "ic": "clock",
    "t": "O Queijo Tem Vida Própria",
    "b": "O estoque <strong>sempre diminui antes de zerar</strong>. “O Queijo tem vida própria e um dia acaba.” Você nem viu de onde ele veio — só presumiu que estaria sempre lá.",
    "tip": "<strong>Modelo mental:</strong> seu Queijo não é seu; tratá-lo como propriedade é o primeiro erro."
   },
   {
    "ic": "pin",
    "t": "Não Decore a Zona de Conforto",
    "b": "Hem e Haw mudaram-se para perto do Posto C, criaram vida social ao redor e pintaram <strong>“TER QUEIJO O FAZ FELIZ”</strong> na parede. Quanto mais você se instala, mais dói (e tarda) sair.",
    "tip": "<strong>Cuidado:</strong> conforto excessivo é o anestésico que esconde o estoque acabando."
   }
  ]
 },
 "ch03-nao-ha-queijo": {
  "cards": [
   {
    "ic": "mask",
    "t": "A Sequência da Negação",
    "b": "O padrão Hem em 4 passos: <strong>1) Choque</strong> (“Não há Queijo?”), <strong>2) Indignação</strong> (“Isso não é justo!”), <strong>3) Senso de direito</strong> (“temos direito ao Queijo”), <strong>4) Paralisia</strong> (voltar todo dia ao posto vazio).",
    "tip": "<strong>Sinal de alerta:</strong> ao se ouvir dizer “não é justo” ou “eu mereço”, você está em modo Hem."
   },
   {
    "ic": "wrench",
    "t": "Atividade ≠ Produtividade",
    "b": "Hem e Haw cavam um buraco na parede do Posto C com martelo e cinzel — <strong>muita atividade, zero queijo</strong>. Esforço na direção errada não é progresso.",
    "tip": "<strong>Regra:</strong> antes de martelar mais forte, pergunte se há queijo nessa parede."
   },
   {
    "ic": "scale",
    "t": "O Senso de Direito Trava",
    "b": "“Por que deveríamos mudar? Somos especiais. <strong>Temos direito</strong> ao nosso Queijo.” A lógica é impecável e inútil — nenhuma dessas frases produz queijo.",
    "tip": "<strong>Modelo mental:</strong> “não é justo” sente-se como verdade sobre o mundo, mas é só a alavanca que te mantém parado."
   },
   {
    "ic": "lens",
    "t": "O Primeiro Lampejo",
    "b": "Haw pergunta: “<strong>Você acha que eles sabem algo que nós não sabemos?</strong>” — a primeira abertura para questionar a própria posição em vez do mundo.",
    "tip": "<strong>Como aplicar:</strong> trocar “quem mexeu no meu queijo?” por “por que eu não me mexi antes?”."
   }
  ]
 },
 "ch04-vencendo-o-medo": {
  "cards": [
   {
    "ic": "key",
    "t": "A Pergunta Libertadora",
    "b": "<strong>“O que você faria se não tivesse medo?”</strong> — separa o medo útil (protege de risco real) do paralisante (inventa perigos). A resposta quase sempre é: seguir em frente.",
    "tip": "<strong>Como aplicar:</strong> escreva a pergunta e responda com a primeira ação concreta que surgir."
   },
   {
    "ic": "bulb",
    "t": "Rir de Si Mesmo",
    "b": "“O caminho mais rápido para mudar é <strong>rir da própria insensatez</strong> — então você se liberta e segue rapidamente.” O riso quebra a identificação com o medo.",
    "tip": "<strong>Atalho:</strong> levar-se a sério demais é exatamente o que prende Hem."
   },
   {
    "ic": "eye",
    "t": "O Medo Imaginado",
    "b": "“O que você teme nunca é tão ruim quanto se imagina. O <strong>medo que você deixa crescer na mente é pior</strong> do que a situação real.” Haw entra no labirinto ainda com medo.",
    "tip": "<strong>Regra:</strong> aja com medo; a coragem chega depois do movimento, não antes."
   },
   {
    "ic": "spark",
    "t": "Vencer o Medo = Liberdade",
    "b": "Correndo pelo corredor escuro, Haw sorri e escreve: <strong>“QUANDO VOCÊ VENCE O SEU MEDO, SENTE-SE LIVRE.”</strong> Estava preso pelo próprio medo; mover-se o libertou.",
    "tip": "<strong>Modelo mental:</strong> o medo é um carcereiro imaginário — a chave é o primeiro passo."
   }
  ]
 },
 "ch05-manuscrito-na-parede": {
  "cards": [
   {
    "ic": "book",
    "t": "Os 7 Princípios",
    "b": "O ciclo completo da mudança:",
    "tip": "<strong>Como aplicar:</strong> trate como checklist diário, não como frase de efeito."
   },
   {
    "ic": "clock",
    "t": "Cheire o Queijo Todo Dia",
    "b": "A vigilância barata (monitorar) evita o choque caro (ser pego de surpresa). <strong>“Notar cedo as pequenas mudanças ajuda-o a adaptar-se às maiores.”</strong>",
    "tip": "<strong>Regra:</strong> os sinais pequenos sempre chegam antes da crise grande."
   },
   {
    "ic": "spiral",
    "t": "É um Ciclo, Não uma Linha",
    "b": "O 7º princípio fecha o laço: a mudança <strong>nunca termina</strong>. A preparação é permanente — o Novo Queijo de hoje é o Velho de amanhã.",
    "tip": "<strong>Cuidado:</strong> achar que “já mudei, acabou” é a porta de volta para o modo Hem."
   }
  ]
 },
 "ch06-novo-queijo": {
  "cards": [
   {
    "ic": "bulb",
    "t": "A Felicidade Não É o Queijo",
    "b": "“Apenas ter Queijo não era o que o tornava feliz. <strong>Haw era feliz quando não estava sendo movido pelo medo.</strong>” O prêmio é o estado interno, não o objeto.",
    "tip": "<strong>Modelo mental:</strong> o queijo é o efeito; o estado interno (sem medo) é a causa."
   },
   {
    "ic": "clock",
    "t": "Monitorar na Abundância",
    "b": "Mesmo com o Posto N cheio, Haw <strong>inspeciona o estoque todo dia</strong> e vai ao labirinto explorar — “mais seguro do que se isolar numa zona de conforto”.",
    "tip": "<strong>Regra:</strong> a zona de conforto se reconstrói sozinha; a inspeção diária a impede."
   },
   {
    "ic": "target",
    "t": "O Obstáculo é Interno",
    "b": "<strong>“O maior obstáculo à mudança está dentro de você mesmo — e nada melhora até você mudar.”</strong> A mudança temida virou “benefício disfarçado”: um Queijo melhor e uma parte melhor de si.",
    "tip": "<strong>Como aplicar:</strong> use a reflexão sobre erros passados para planejar o futuro — a inteligência vira vantagem quando não vira medo."
   }
  ]
 },
 "ch07-aplicacoes": {
  "cards": [
   {
    "ic": "fork",
    "t": "“Qual Personagem Você É?”",
    "b": "A pergunta que abre o autoconhecimento. Carlos admite ter sido Hem (“não quis nem enxergar”); Nathan vê a empresa familiar como Hem diante do shopping.",
    "tip": "<strong>Como aplicar:</strong> faça a pergunta a si e ao seu time antes de qualquer reação à mudança."
   },
   {
    "ic": "person",
    "t": "Gerir os Quatro (liderança)",
    "b": "Cada personagem precisa de tratamento diferente: <strong>Sniffs</strong> farejam o mercado; <strong>Scurrys</strong> agem (monitorados); <strong>Hems</strong> precisam ver que a mudança aumenta sua segurança; <strong>Haws</strong> ajudam a construir a visão.",
    "tip": "<strong>Regra:</strong> “uma mudança imposta é uma mudança oposta” — dê uma linguagem comum, não uma ordem."
   },
   {
    "ic": "link",
    "t": "Velho Queijo = Comportamento",
    "b": "Num relacionamento ruim, o Novo Queijo pode ser “<strong>um novo relacionamento com a mesma pessoa</strong>” — abrir mão do comportamento antigo, não da pessoa.",
    "tip": "<strong>Como aplicar:</strong> repetir o mesmo comportamento só repete os mesmos resultados."
   },
   {
    "ic": "mountain",
    "t": "Mova Seu Próprio Queijo",
    "b": "Nathan: melhor mudar enquanto se pode do que ser forçado — “<strong>vender as lojas antigas e construir uma modeníssima</strong> para competir”. Antecipar é mais barato que reagir.",
    "tip": "<strong>Lição:</strong> uma organização só muda quando gente suficiente muda."
   }
  ]
 }
}
```
