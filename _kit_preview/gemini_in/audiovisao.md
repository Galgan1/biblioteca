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

# LIVRO PARA APROFUNDAR: A Audiovisão — Michel Chion

**Subtítulo:** VISÃO GERAL · SOM E IMAGEM NO CINEMA
**Ideia central:** Chion derruba a intuição de que vemos uma coisa e ouvimos outra, somando as duas. Na audiovisão, som e imagem se transformam mutuamente — é um contrato, uma fusão consentida em que o som faz o trabalho e a imagem leva o crédito. Do valor acrescentado à síncrese, do acusmático ao rendering, é a teoria que explica por que metade do que sentimos num filme vem do que ouvimos sem perceber.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-contrato-audiovisual` — CAPÍTULO 1: O Contrato Audiovisual
- `ch02-valor-acrescentado` — CAPÍTULO 2: O Valor Acrescentado
- `ch03-sincrese` — CAPÍTULO 3: A Síncrese
- `ch04-modos-de-escuta` — CAPÍTULO 4: Os Três Modos de Escuta
- `ch05-acusmatico-acusmetre` — CAPÍTULO 5: O Acusmático e o Acusmêtre
- `ch06-temporalizacao` — CAPÍTULO 6: A Temporalização
- `ch07-rendering` — CAPÍTULO 7: O Rendering
- `ch08-espacos-vococentrismo` — CAPÍTULO 8: Os Espaços do Som e o Vococentrismo

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-contrato-audiovisual": {
  "cards": [
   {
    "ic": "link",
    "t": "Audiovisão",
    "b": "A percepção em que o som influencia o que vemos e a imagem o que ouvimos — um <strong>terceiro sentido</strong>, irredutível à soma de ver + ouvir.",
    "tip": "<strong>Como aplicar:</strong> troque a trilha e a expressão dos atores parece mudar, sem retocar um pixel."
   },
   {
    "ic": "pivot",
    "t": "Contrato, não soma",
    "b": "A relação é uma <strong>convenção consentida</strong>, não uma adição natural. A mesma imagem com som diferente vira outra cena.",
    "tip": "<strong>Modelo mental:</strong> a cena é um acordo, não uma gravação."
   },
   {
    "ic": "gap",
    "t": "Som como \"acompanhamento\"",
    "b": "Tratá-lo como camada opcional sobre a imagem <strong>ignora que ele redefine a imagem</strong>.",
    "tip": "<strong>Cuidado:</strong> analisar som e imagem isolados perde o fenômeno — a fusão."
   }
  ]
 },
 "ch02-valor-acrescentado": {
  "cards": [
   {
    "ic": "eye",
    "t": "Valeur ajoutée",
    "b": "A informação ou emoção com que um som <strong>enriquece</strong> a imagem, fazendo parecer que ela emana naturalmente do que se vê.",
    "tip": "<strong>Como aplicar:</strong> o melhor som é invisível — sentido como propriedade da imagem."
   },
   {
    "ic": "target",
    "t": "A fala estrutura a imagem",
    "b": "O texto (valor acrescentado semântico) <strong>orienta o olhar</strong> e impõe leitura à imagem ambígua. O ritmo do som impõe a sensação de tempo.",
    "tip": "<strong>Modelo mental:</strong> o som planta; a imagem colhe o crédito."
   },
   {
    "ic": "gap",
    "t": "Som redundante",
    "b": "Dizer no áudio o que a imagem já diz <strong>não acrescenta valor</strong> — só ocupa espaço.",
    "tip": "<strong>Cuidado:</strong> mixar sem testar a ausência esconde o que o som realmente faz."
   }
  ]
 },
 "ch03-sincrese": {
  "cards": [
   {
    "ic": "target",
    "t": "Síncrese",
    "b": "A fusão <strong>involuntária e reflexa</strong> de um evento sonoro e um visual simultâneos. Não é aprendida nem opcional.",
    "tip": "<strong>Como aplicar:</strong> você não precisa do som real — precisa do som certo no tempo certo."
   },
   {
    "ic": "pin",
    "t": "Synch points",
    "b": "Os instantes em que som e imagem batem juntos com força são <strong>acentos</strong> — pontuam a cena como acentos numa frase.",
    "tip": "<strong>Modelo mental:</strong> a sincronia cola; a fonte é livre."
   },
   {
    "ic": "gap",
    "t": "Synch points em excesso",
    "b": "Bater som+imagem o tempo todo (mickey-mousing) <strong>cansa e perde o acento</strong>.",
    "tip": "<strong>Cuidado:</strong> sincronia desleixada quebra a solda e denuncia a costura."
   }
  ]
 },
 "ch04-modos-de-escuta": {
  "cards": [
   {
    "ic": "lens",
    "t": "Os três modos",
    "b": "<strong>Causal</strong> (identificar a fonte), <strong>semântica</strong> (decodificar a fala/código) e <strong>reduzida</strong> (o som em si — altura, textura, independente da fonte).",
    "tip": "<strong>Como aplicar:</strong> mixe para o modo dominante de cada trecho."
   },
   {
    "ic": "key",
    "t": "A escuta reduzida é o ofício",
    "b": "Descrever o som por suas <strong>qualidades</strong> (não \"um carro\", mas \"um grave áspero crescente\") é como o designer escolhe e molda sons.",
    "tip": "<strong>Modelo mental:</strong> na fala o público está na semântica — proteja a inteligibilidade."
   },
   {
    "ic": "gap",
    "t": "Tratar tudo como causal",
    "b": "Ignorar que, na fala, o que importa é o <strong>código (semântica)</strong> faz a trilha cobrir a voz.",
    "tip": "<strong>Cuidado:</strong> a escuta causal pode ser enganada (a síncrese planta uma causa falsa)."
   }
  ]
 },
 "ch05-acusmatico-acusmetre": {
  "cards": [
   {
    "ic": "mask",
    "t": "O acusmêtre",
    "b": "A voz acusmática (off, narrador invisível, o vilão que só se ouve) tende a parecer <strong>onisciente, onipresente e ameaçadora</strong> — não está em lugar nenhum, logo está em todo lugar.",
    "tip": "<strong>Como aplicar:</strong> o invisível é mais poderoso que o visível."
   },
   {
    "ic": "eye",
    "t": "Des-acusmatização",
    "b": "O momento em que vemos a fonte da voz. O corpo a <strong>aprisiona</strong> no espaço e no tempo — e o acusmêtre perde os poderes, vira humano.",
    "tip": "<strong>Modelo mental:</strong> revelar é rebaixar."
   },
   {
    "ic": "gap",
    "t": "Mostrar cedo demais",
    "b": "Revelar a fonte de uma ameaça acusmática <strong>mata o suspense</strong> que ela sustentava.",
    "tip": "<strong>Cuidado:</strong> des-acusmatização acidental joga fora um trunfo dramático."
   }
  ]
 },
 "ch06-temporalizacao": {
  "cards": [
   {
    "ic": "clock",
    "t": "Temporalização",
    "b": "O som impõe à imagem um <strong>fluxo temporal</strong> — um presente que corre. A mesma imagem fixa \"ganha tempo\" sob um som que progride.",
    "tip": "<strong>Como aplicar:</strong> sem som a imagem \"fica\"; com som ela \"anda\"."
   },
   {
    "ic": "pivot",
    "t": "Vetorização",
    "b": "O som <strong>aponta para o futuro</strong> — um ruído que cresce cria expectativa de um desfecho. Dá direção ao tempo, um antes e um depois.",
    "tip": "<strong>Modelo mental:</strong> o som é a flecha do tempo da cena."
   },
   {
    "ic": "gap",
    "t": "Imagem lenta + som parado",
    "b": "Sem vetorização, a cena <strong>\"morre\"</strong> e o público sente que nada acontece.",
    "tip": "<strong>Cuidado:</strong> cortar o som a cada corte de imagem destrói a continuidade temporal."
   }
  ]
 },
 "ch07-rendering": {
  "cards": [
   {
    "ic": "spark",
    "t": "Rendering vs. reprodução",
    "b": "Reprodução é o som acústico real; <strong>rendering</strong> é o conjunto de sensações (força, peso, violência) traduzido em som. O cinema faz rendering.",
    "tip": "<strong>Como aplicar:</strong> renderize a sensação, não o evento."
   },
   {
    "ic": "target",
    "t": "O irreal convincente",
    "b": "O som real costuma ser <strong>decepcionante</strong>; o som que \"soa verdadeiro\" é construído e exagerado para entregar a sensação.",
    "tip": "<strong>Modelo mental:</strong> o real é o ponto de partida, não a meta — a meta é a experiência."
   },
   {
    "ic": "gap",
    "t": "Fetiche do realismo",
    "b": "Insistir no som real (fraco) por purismo faz a cena <strong>perder impacto</strong>.",
    "tip": "<strong>Cuidado:</strong> rendering tímido entrega menos do que a cena precisa sentir."
   }
  ]
 },
 "ch08-espacos-vococentrismo": {
  "cards": [
   {
    "ic": "layers",
    "t": "Os três espaços",
    "b": "<strong>In</strong> (fonte na tela), <strong>fora de campo</strong> (diegético, fonte fora do quadro) e <strong>off</strong> (não-diegético: trilha, voz over). Mover um som entre eles é recurso dramático.",
    "tip": "<strong>Como aplicar:</strong> a posição define o sentido tanto quanto o som em si."
   },
   {
    "ic": "target",
    "t": "Vococentrismo",
    "b": "Na presença de voz, o público a escuta <strong>antes de tudo</strong>; e, sendo fala, busca primeiro o sentido das palavras (verbocentrismo).",
    "tip": "<strong>Modelo mental:</strong> a voz é o sol; os outros sons orbitam."
   },
   {
    "ic": "pivot",
    "t": "Empático × anempático",
    "b": "Som que <strong>acompanha</strong> a emoção (empático) vs. som <strong>indiferente</strong> (anempático) — a indiferença amplifica o horror ao lembrar que o mundo segue alheio.",
    "tip": "<strong>Cuidado:</strong> cobrir a voz com trilha/efeito viola o vococentrismo — o pecado capital."
   }
  ]
 }
}
```
