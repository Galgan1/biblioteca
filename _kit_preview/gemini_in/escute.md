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

# LIVRO PARA APROFUNDAR: Escute! — Kate Murphy

**Subtítulo:** VISÃO GERAL · ESCUTA COMO HABILIDADE ESSENCIAL
**Ideia central:** Ensinam a ler, escrever e falar — nunca a escutar. A jornalista Kate Murphy revela que a escuta é a habilidade mais subestimada e a primeira a se perder na era da distração. Ouvir é passivo; escutar é ativo. E é a base de toda conexão, compreensão e influência real.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-habilidade-perdida` — CAPÍTULO 1: A Habilidade Perdida da Era da Distração
- `ch02-paradoxo-da-familiaridade` — CAPÍTULO 2: O Paradoxo da Familiaridade
- `ch03-deslocamento-e-apoio` — CAPÍTULO 3: Resposta de Deslocamento × Resposta de Apoio
- `ch04-compreender-nao-responder` — CAPÍTULO 4: Escutar para Compreender, não para Responder
- `ch05-ruido-e-tecnologia` — CAPÍTULO 5: O Ruído, os Fones e o Texting
- `ch06-curiosidade-genuina` — CAPÍTULO 6: A Curiosidade Genuína e a Pergunta que Abre
- `ch07-silencio-e-pausas` — CAPÍTULO 7: O Silêncio, as Pausas e o Medo do Vazio
- `ch08-lacuna-fala-pensamento` — CAPÍTULO 8: Escutar a Si Mesmo
- `ch09-solidao-e-polarizacao` — CAPÍTULO 9: Solidão e Polarização

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-habilidade-perdida": {
  "cards": [
   {
    "ic": "wave",
    "t": "Escutar como Músculo",
    "b": "Passamos anos aprendendo a falar, zero a escutar — embora escutar seja o que mais fazemos e pior fazemos. <strong>É uma habilidade aprendível</strong>, não um traço fixo. Atrofia sem prática; fortalece com esforço deliberado.",
    "tip": "<strong>Como aplicar:</strong> trate a escuta como treino: cada conversa é uma repetição, não uma performance natural."
   },
   {
    "ic": "gap",
    "t": "O Paradoxo da Hiperconexão",
    "b": "Nunca fomos tão 'conectados' e tão solitários. Temos mais canais e menos escuta real. A solidão moderna não é falta de companhia — é falta de ser <strong>de fato ouvido</strong>.",
    "tip": "<strong>Modelo mental:</strong> conexão digital é quantidade; escuta real é qualidade — são coisas diferentes."
   },
   {
    "ic": "eye",
    "t": "A Assimetria do Ensino",
    "b": "A escuta é o que mais fazemos e menos treinamos. <strong>Quem se acha bom ouvinte</strong> raramente investe em melhorar — o primeiro passo é a humildade de reconhecer que há muito a aprender.",
    "tip": "<strong>Sinal de alerta:</strong> achar que 'eu já sou bom ouvinte' é o maior obstáculo à melhora real."
   }
  ]
 },
 "ch02-paradoxo-da-familiaridade": {
  "cards": [
   {
    "ic": "lens",
    "t": "Viés da Familiaridade",
    "b": "Presumimos entender melhor quem amamos do que estranhos — quando na verdade os escutamos <strong>pior</strong>. As pessoas mudam; a imagem que temos delas não. Respondemos a uma versão congelada, não à pessoa real.",
    "tip": "<strong>Como aplicar:</strong> trate o conhecido com a curiosidade que daria a um estranho fascinante."
   },
   {
    "ic": "clock",
    "t": "Imagem Congelada",
    "b": "Guardamos uma representação mental desatualizada do outro e respondemos a ela, não à pessoa que está na nossa frente <strong>hoje</strong>. Intimidade não dá licença para parar de escutar — exige o contrário.",
    "tip": "<strong>Modelo mental:</strong> 'Eu conheço a pessoa de ontem, não a de hoje' — toda relação exige re-escuta contínua."
   },
   {
    "ic": "gap",
    "t": "Completar Frases",
    "b": "Completar a frase do outro, prever o que vai dizer — são sinais de escuta desligada. Você decidiu que já sabe o final antes de ele terminar. <strong>Quase sempre haverá surpresa</strong> se você esperar.",
    "tip": "<strong>Sinal de alerta:</strong> 'já sei o que você vai dizer' encerra a conversa antes de ela existir."
   }
  ]
 },
 "ch03-deslocamento-e-apoio": {
  "cards": [
   {
    "ic": "bubble",
    "t": "Deslocamento (Shift Response)",
    "b": "Redirecionar a conversa para a própria experiência: 'Isso me lembra quando eu…'. Tell: sua fala começa por <strong>'eu / comigo / quando eu'</strong>. Parece identificação — comunica 'chega de você, agora sou eu'.",
    "tip": "<strong>Sinal de alerta:</strong> monitore a frequência com que sua próxima fala começa por 'eu'. Se for alta, você está deslocando."
   },
   {
    "ic": "wave",
    "t": "Apoio (Support Response)",
    "b": "Manter o holofote no outro com perguntas que <strong>aprofundam</strong>: 'Que parte? O que mais te marcou lá?' A resposta de apoio é quase sempre uma pergunta de seguimento — não uma história sua.",
    "tip": "<strong>Como aplicar:</strong> faça uma pergunta de seguimento antes de oferecer qualquer história sua."
   },
   {
    "ic": "person",
    "t": "Egoísmo Conversacional",
    "b": "O padrão sistemático de levar tudo de volta para si — geralmente <strong>inconsciente</b>. Micro-deslocamentos acumulados monopolizam a atenção e esvaziam a conexão. Você pode compartilhar suas experiências — depois de o outro ter sido plenamente ouvido.",
    "tip": "<strong>Regra:</strong> apoio antes de história — sempre."
   }
  ]
 },
 "ch04-compreender-nao-responder": {
  "cards": [
   {
    "ic": "eye",
    "t": "Escutar para Compreender",
    "b": "No modo 'para responder', você ensaia o contra-argumento enquanto o outro ainda fala — e ouve metade. No modo 'para compreender', você <strong>suspende a resposta</strong> até captar sentido E emoção. Minha vez de falar não está cronometrada.",
    "tip": "<strong>Como aplicar:</strong> proíba-se de formular a resposta enquanto o outro fala; só depois pense no que dizer."
   },
   {
    "ic": "leaf",
    "t": "'Sim, e…' no lugar de 'Não, mas…'",
    "b": "Do improv: aceite o que o outro trouxe ('sim') e construa sobre isso ('e…'), em vez de negar e impor a própria pauta ('não, mas…'). <strong>'Não, mas…'</strong> encerra o fluxo; <strong>'Sim, e…'</strong> o amplia.",
    "tip": "<strong>Modelo mental:</strong> trate o que o outro diz como ponto de partida, não como tese a derrubar."
   },
   {
    "ic": "spark",
    "t": "Escutar a Emoção, não só a Informação",
    "b": "O conteúdo muitas vezes é pretexto — o que pede escuta é o sentimento por baixo. <strong>Compreenda a emoção por baixo do conteúdo</strong> antes de reagir ao conteúdo. A resposta real que o outro precisa raramente é a que você preparou.",
    "tip": "<strong>Sinal de alerta:</strong> responder ao conteúdo quando a emoção não foi ouvida gera desconexão — o outro sente que não foi escutado."
   }
  ]
 },
 "ch05-ruido-e-tecnologia": {
  "cards": [
   {
    "ic": "pin",
    "t": "Celular Visível = Conversa Degradada",
    "b": "A simples presença visível de um smartphone na mesa reduz a profundidade e a satisfação da conversa — mesmo sem ninguém tocá-lo. <strong>A mera presença já é uma terceira pessoa na conversa</strong> — e a mais barulhenta.",
    "tip": "<strong>Como aplicar:</strong> ao sentar para uma conversa que importa, vire o celular para baixo e tire-o do campo de visão."
   },
   {
    "ic": "person",
    "t": "Phubbing",
    "b": "Desprezar quem está na sua frente para olhar a tela — mesmo 'só dando uma olhadinha'. <strong>Degrada o vínculo</strong> e sinaliza 'você não vale minha atenção plena'. O outro sente, mesmo que não diga.",
    "tip": "<strong>Sinal de alerta:</strong> mão indo ao bolso em qualquer pausa da conversa = fuga do desconforto da presença."
   },
   {
    "ic": "gap",
    "t": "Multitarefa é Mito",
    "b": "O cérebro <strong>alterna</strong> entre tarefas, não paraleliza. Escutar e fazer outra coisa significa escutar mal as duas. Tédio e silêncio são portas para a escuta, não falhas a tapar com tela.",
    "tip": "<strong>Modelo mental:</strong> treine o cérebro a tolerar a presença — cada vez que resiste ao celular, fortalece o músculo da escuta."
   }
  ]
 },
 "ch06-curiosidade-genuina": {
  "cards": [
   {
    "ic": "bulb",
    "t": "Curiosidade Genuína",
    "b": "Querer de verdade saber o que se passa na cabeça do outro — pressuposto: <em>'cada pessoa sabe algo que eu não sei'</em>. Curiosidade genuína vale mais do que qualquer técnica de escuta ativa performática.",
    "tip": "<strong>Como aplicar:</strong> antes de cada pergunta, cheque: 'quero mesmo saber a resposta, ou quero falar da minha experiência?'"
   },
   {
    "ic": "spark",
    "t": "'Qual a Coisa Mais…?'",
    "b": "A pergunta-chave que abre histórias: <strong>'Qual a coisa mais marcante / mais difícil / mais inesperada de…?'</strong> Pede um detalhe vivo, não um sim/não. Sinaliza interesse real e destrava narrativas que perguntas genéricas nunca alcançam.",
    "tip": "<strong>Como aplicar:</strong> substitua 'Como foi?' (capciosa) por 'Qual foi a coisa mais inesperada que te aconteceu lá?' — e escute a diferença."
   },
   {
    "ic": "mask",
    "t": "Pergunta Capciosa",
    "b": "A que já embute a resposta desejada: 'Você não achou ótimo?' Busca confirmação, não informação — e mata a escuta. <strong>Perguntar só para emendar sua própria história</strong> é deslocamento disfarçado de pergunta.",
    "tip": "<strong>Sinal de alerta:</strong> se a pergunta já contém a resposta que você quer, não é pergunta — é afirmação disfarçada."
   }
  ]
 },
 "ch07-silencio-e-pausas": {
  "cards": [
   {
    "ic": "wave",
    "t": "A Pausa como Ferramenta",
    "b": "Após uma pergunta importante ou quando o outro hesita: <strong>deixe o silêncio respirar</strong>. Quase sempre vem um segundo andar da fala, mais verdadeiro que o primeiro. Regra prática: conte até três antes de preencher qualquer pausa.",
    "tip": "<strong>Como aplicar:</strong> jornalistas e negociadores usam o 'silêncio constrangedor' de propósito — feita a pergunta, calam e colhem."
   },
   {
    "ic": "clock",
    "t": "Horror ao Silêncio",
    "b": "O desconforto cultural com pausas nos faz interromper, completar frases e tagarelar — <strong>sufocando a fala do outro</strong>. A compulsão de preencher qualquer vazio é treinada pela tela, não pela natureza. Trate o silêncio como convite, não como constrangimento.",
    "tip": "<strong>Modelo mental:</strong> 'O silêncio é o convite, não o constrangimento' — pausa do outro = pensamento em formação."
   },
   {
    "ic": "gap",
    "t": "Interrupção",
    "b": "Cortar a fala do outro — frequentemente por achar que 'já entendeu' (viés da familiaridade) ou que sua ideia é urgente. É o oposto operacional do silêncio e a forma mais explícita de dizer 'minha vez importa mais'.",
    "tip": "<strong>Sinal de alerta:</strong> se você interrompe muito, provavelmente também completa frases e desvia o assunto para si."
   }
  ]
 },
 "ch08-lacuna-fala-pensamento": {
  "cards": [
   {
    "ic": "spiral",
    "t": "A Lacuna Fala-Pensamento",
    "b": "Falamos a ~120–150 palavras/min, mas pensamos muito mais rápido. A mente preenche o excedente — com julgamento, ensaio de resposta ou distração. <strong>A mesma lacuna que distrai é a que, redirecionada, capta o subtexto.</strong>",
    "tip": "<strong>Como aplicar:</strong> redirecione a sobra de tempo para processar e formular perguntas sobre o que o outro diz — não para fugir."
   },
   {
    "ic": "eye",
    "t": "A Voz Interior",
    "b": "O diálogo mental constante que comenta, julga e ensaia durante a escuta. Escutar bem o outro depende de <strong>reconhecer e silenciar a própria voz interior</strong>. Cheque: foi o outro que disse, ou foi minha voz interpretando?",
    "tip": "<strong>Modelo mental:</strong> a sobra de tempo é combustível — ou para entender o outro, ou para me distrair. Você escolhe."
   },
   {
    "ic": "mask",
    "t": "Ensaio Interno como Vilão",
    "b": "Usar a lacuna para preparar a réplica é a raiz de 'escutar para responder' (Ch 4). <strong>Você ouviu metade</strong> — porque a outra metade você passou formulando o que ia dizer. Resultado: resposta que não responde ao que foi de fato dito.",
    "tip": "<strong>Sinal de alerta:</strong> se sua resposta já estava pronta antes do outro terminar, você estava ensaiando, não escutando."
   }
  ]
 },
 "ch09-solidao-e-polarizacao": {
  "cards": [
   {
    "ic": "person",
    "t": "Solidão como Déficit de Escuta",
    "b": "A dor não é estar só — é <strong>não se sentir ouvido</strong>. Conexão real exige alguém que escute de verdade, não apenas a presença de pessoas ou de notificações. É por isso que estamos mais 'conectados' e mais solitários do que nunca.",
    "tip": "<strong>Como aplicar:</strong> combata a solidão (própria e alheia) escutando de verdade uma pessoa por vez."
   },
   {
    "ic": "scale",
    "t": "Polarização como Recusa de Escutar",
    "b": "Paramos de ouvir quem pensa diferente, viramos câmaras de eco e tratamos o adversário como caricatura. <strong>Escutar não é concordar — é entender</strong> por que uma pessoa razoável chega a uma conclusão que você rejeita.",
    "tip": "<strong>Modelo mental:</strong> 'Escutar não é concordar; é entender por que o outro pensa o que pensa.'"
   },
   {
    "ic": "leaf",
    "t": "Escutar o Discordante",
    "b": "A curiosidade genuína (Ch 6) aplicada a quem pensa diferente quebra a caricatura e reduz o desprezo. Faça uma pergunta sincera ('O que te levou a pensar assim?') e escute <strong>até o fim</strong> antes de qualquer réplica. Quase nunca o outro é a caricatura imaginada.",
    "tip": "<strong>Sinal de alerta:</strong> ouvir só para refutar é a versão social de 'escutar para responder' — e aprofunda a polarização."
   }
  ]
 }
}
```
