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

# LIVRO PARA APROFUNDAR: Sound Design — David Sonnenschein

**Subtítulo:** VISÃO GERAL · O PODER EXPRESSIVO DO SOM NO CINEMA
**Ideia central:** Sonnenschein trata a trilha sonora — voz, música e efeitos — como uma camada de contar história tão poderosa quanto a imagem, e quase sempre subutilizada. O som percorre uma cadeia (vibração → sensação → percepção → emoção), e o ofício é desenhá-la de ponta a ponta: traçar a curva emocional da história e pintá-la com tom, ritmo, intensidade, timbre, espaço e silêncio.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-processo-sound-design` — CAPÍTULO 1: O Processo do Sound Design
- `ch02-criatividade-sons` — CAPÍTULO 2: Criatividade e a Invenção de Sons
- `ch03-vibracao-sensacao` — CAPÍTULO 3: Da Vibração à Sensação
- `ch04-sensacao-percepcao` — CAPÍTULO 4: Da Sensação à Percepção
- `ch05-musica` — CAPÍTULO 5: A Música
- `ch06-voz-humana` — CAPÍTULO 6: A Voz Humana
- `ch07-efeitos-paisagem` — CAPÍTULO 7: Efeitos e Paisagem Sonora
- `ch08-som-imagem-emocao` — CAPÍTULO 8: Som, Imagem e o Mapa Emocional

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-processo-sound-design": {
  "cards": [
   {
    "ic": "eye",
    "t": "Spotting (a leitura sonora)",
    "b": "Percorrer o roteiro perguntando, cena a cena — <strong>o que se ouve aqui, e o que esse som deve fazer pela história?</strong> Mapear voz, música, efeito e silêncio.",
    "tip": "<strong>Como aplicar:</strong> spotting é o storyboard do ouvido."
   },
   {
    "ic": "target",
    "t": "Intenção por som",
    "b": "Todo som deve responder <strong>por que está aqui?</strong> Som sem função é ruído que rouba a atenção que a história precisa.",
    "tip": "<strong>Modelo mental:</strong> antes de criar, defina a paleta — o vocabulário sonoro do projeto."
   },
   {
    "ic": "gap",
    "t": "\"Resolvemos na pós\"",
    "b": "Tratar o áudio como etapa cosmética final <strong>perde oportunidades narrativas</strong> e gera remendos caros.",
    "tip": "<strong>Cuidado:</strong> o som se decide no papel, não na mesa de mixagem."
   }
  ]
 },
 "ch02-criatividade-sons": {
  "cards": [
   {
    "ic": "spark",
    "t": "Metáfora sonora",
    "b": "Representar uma ideia por um som que <strong>evoca a sensação certa</strong>, não o real (um soco = galho quebrando + sub-grave = dor e peso que o soco real não tem).",
    "tip": "<strong>Como aplicar:</strong> projete a sensação, não a fidelidade ao objeto."
   },
   {
    "ic": "layers",
    "t": "Camadas",
    "b": "O som final costuma ser uma <strong>mistura</strong> de fontes inesperadas (rugido + tigre + voz humana abafada) — a camada é o que dá assinatura e emoção.",
    "tip": "<strong>Modelo mental:</strong> o som é uma mentira útil — honesta com a emoção."
   },
   {
    "ic": "gap",
    "t": "Biblioteca preguiçosa",
    "b": "Pegar o efeito genérico de prateleira para tudo faz o filme <strong>soar como todos os outros</strong>.",
    "tip": "<strong>Cuidado:</strong> literalidade mata a metáfora; um som original vira identidade."
   }
  ]
 },
 "ch03-vibracao-sensacao": {
  "cards": [
   {
    "ic": "scale",
    "t": "As alavancas físicas",
    "b": "<strong>Grave</strong> = peso, ameaça, intimidade; <strong>agudo</strong> = tensão, alerta. <strong>Intensidade</strong> (contraste) = urgência; <strong>ritmo</strong> = energia; <strong>reverberação</strong> = tamanho do mundo.",
    "tip": "<strong>Como aplicar:</strong> cada propriedade é um botão emocional."
   },
   {
    "ic": "pivot",
    "t": "O contraste é tudo",
    "b": "Nenhuma propriedade significa em absoluto — significa <strong>em relação</strong>. O grave só pesa depois do agudo; o alto só impacta depois do silêncio.",
    "tip": "<strong>Modelo mental:</strong> o subsônico cria tensão corporal que ninguém percebe."
   },
   {
    "ic": "gap",
    "t": "Tudo no mesmo nível",
    "b": "Sem contraste de intensidade/frequência, o ouvido <strong>satura</strong> e nada se destaca.",
    "tip": "<strong>Cuidado:</strong> reverberação que contradiz a cena quebra a imersão."
   }
  ]
 },
 "ch04-sensacao-percepcao": {
  "cards": [
   {
    "ic": "lens",
    "t": "Figura e fundo",
    "b": "O cérebro separa o som <strong>principal</strong> (figura) do leito (fundo) e só processa <strong>um fluxo consciente por vez</strong> — em geral a voz. A hierarquia respeita esse limite.",
    "tip": "<strong>Como aplicar:</strong> se dois sons disputam o principal, o público perde os dois."
   },
   {
    "ic": "wave",
    "t": "Mascaramento",
    "b": "Um som forte <strong>esconde</strong> um fraco próximo em frequência. Use a favor (esconder um corte) ou evite contra (a voz some sob a trilha).",
    "tip": "<strong>Modelo mental:</strong> metade da emoção mora abaixo do consciente."
   },
   {
    "ic": "gap",
    "t": "Trilha que mascara a voz",
    "b": "Competir na mesma faixa de frequência da fala = <strong>inteligibilidade perdida</strong> (o defeito nº 1).",
    "tip": "<strong>Cuidado:</strong> saturar a atenção cansa e o público desliga."
   }
  ]
 },
 "ch05-musica": {
  "cards": [
   {
    "ic": "spark",
    "t": "As alavancas musicais",
    "b": "<strong>Melodia</strong> (a linha que se lembra), <strong>harmonia</strong> (maior = alegria; menor = tensão; dissonância = desconforto), <strong>ritmo</strong> (energia), <strong>timbre</strong> (a cor emocional).",
    "tip": "<strong>Como aplicar:</strong> música comenta, não ilustra."
   },
   {
    "ic": "link",
    "t": "Leitmotiv",
    "b": "Um tema associado a um personagem ou ideia, que <strong>retorna transformado</strong> conforme a história muda. Constrói significado por repetição e variação.",
    "tip": "<strong>Modelo mental:</strong> o público sente o personagem chegar antes de vê-lo."
   },
   {
    "ic": "gap",
    "t": "Mickey-mousing",
    "b": "A música sublinhar <strong>cada gesto literalmente</strong> infantiliza e cansa. Trilha onipresente anula o próprio poder.",
    "tip": "<strong>Cuidado:</strong> música não salva cena ruim — o problema é a cena."
   }
  ]
 },
 "ch06-voz-humana": {
  "cards": [
   {
    "ic": "key",
    "t": "As camadas da voz",
    "b": "<strong>Conteúdo</strong> (palavras) + <strong>prosódia</strong> (entonação, ritmo, ênfase, pausa) + <strong>grão</strong> (a textura física). A mesma frase muda de sentido pela prosódia.",
    "tip": "<strong>Como aplicar:</strong> pontuação é direção de ator — onde a vírgula cai, a emoção acontece."
   },
   {
    "ic": "target",
    "t": "Vococentrismo",
    "b": "Na presença de voz, o público a escuta <strong>primeiro</strong>; tudo o mais vira fundo. A mixagem protege a inteligibilidade absoluta.",
    "tip": "<strong>Modelo mental:</strong> a voz é o rei da mixagem; nada disputa com ela."
   },
   {
    "ic": "gap",
    "t": "Texto certo, tom errado",
    "b": "O público acredita no <strong>tom antes do conteúdo</strong>; uma fala certa dita com tom errado mente. Leitura plana desliga o ouvinte.",
    "tip": "<strong>Cuidado:</strong> voz coberta por trilha/efeito é o pecado capital do áudio."
   }
  ]
 },
 "ch07-efeitos-paisagem": {
  "cards": [
   {
    "ic": "layers",
    "t": "As camadas do efeito",
    "b": "<strong>Foley</strong> (passos, roupas — presença física), <strong>hard effects</strong> (porta, tiro), <strong>ambiência/room tone</strong> (o leito do lugar) e <strong>sound design</strong> (os sons inventados).",
    "tip": "<strong>Como aplicar:</strong> sem foley, atores parecem fantasmas."
   },
   {
    "ic": "lens",
    "t": "Hiper-realismo seletivo",
    "b": "Na vida tudo soa; no cinema, <strong>escolhe-se</strong> o que se ouve. Exagerar UM som (a gota, o relógio) e apagar o resto dirige a atenção.",
    "tip": "<strong>Modelo mental:</strong> a emoção mora no foco, não na soma de tudo."
   },
   {
    "ic": "gap",
    "t": "Realismo indiscriminado",
    "b": "Pôr todo som que existiria vira <strong>lama sonora sem foco</strong>; ambiência genérica não dá alma a nenhum lugar.",
    "tip": "<strong>Cuidado:</strong> no cinema o silêncio é uma escolha e o som é curadoria."
   }
  ]
 },
 "ch08-som-imagem-emocao": {
  "cards": [
   {
    "ic": "clock",
    "t": "O mapa emocional",
    "b": "Desenhe a linha de emoção pretendida (calma → tensão → clímax → alívio) e atribua a cada trecho as <strong>alavancas sonoras</strong> que a sustentam.",
    "tip": "<strong>Como aplicar:</strong> projete a curva, depois pinte-a — senão o filme não respira."
   },
   {
    "ic": "pivot",
    "t": "Empático × anempático",
    "b": "Som <strong>empático</strong> acompanha a emoção; som <strong>anempático</strong> (indiferente — uma valsa alegre numa tragédia) <strong>amplifica</strong> o horror.",
    "tip": "<strong>Modelo mental:</strong> a imagem mostra; o som diz o que sentir. Eles se multiplicam."
   },
   {
    "ic": "key",
    "t": "O silêncio como clímax",
    "b": "O ponto mais alto da curva muitas vezes é a <strong>ausência total de som</strong> — o vazio que o público preenche com a própria emoção.",
    "tip": "<strong>Cuidado:</strong> curva plana (mesma densidade o tempo todo) não deixa sentir subidas nem quedas."
   }
  ]
 }
}
```
