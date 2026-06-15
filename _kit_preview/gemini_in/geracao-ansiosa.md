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

# LIVRO PARA APROFUNDAR: A Geração Ansiosa — Jonathan Haidt

**Subtítulo:** VISÃO GERAL · A GRANDE RECONFIGURAÇÃO DA INFÂNCIA
**Ideia central:** Por volta de 2012, os indicadores de saúde mental de adolescentes dispararam em todo o mundo. Jonathan Haidt identifica a causa: trocamos a infância baseada em brincadeira pela infância baseada no celular. E o caminho de volta exige ação coletiva — não heroísmo individual.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-onda-de-sofrimento` — CAPÍTULO 1: A Onda de Sofrimento
- `ch02-o-que-criancas-precisam` — CAPÍTULO 2: O Que as Crianças Precisam na Infância
- `ch03-modo-descoberta` — CAPÍTULO 3–4: Modo Descoberta e Ritos de Passagem
- `ch04-quatro-danos` — CAPÍTULO 5: Os Quatro Danos Fundamentais
- `ch05-meninas-meninos` — CAPÍTULO 6–7: Meninas, Meninos e o Dano Assimétrico
- `ch06-elevacao-espiritual` — CAPÍTULO 8: Degradação e Elevação Espiritual
- `ch07-acao-coletiva` — CAPÍTULO 9 + 13: Ação Coletiva e as 4 Normas

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-onda-de-sofrimento": {
  "cards": [
   {
    "ic": "wave",
    "t": "A Grande Reconfiguração (~2010-2015)",
    "b": "A janela curta em que a infância foi reprogramada. Smartphone com câmera frontal (2010), feed/curtidas, 4G e banda larga móvel tornaram a internet onipresente e <strong>\"viciante por design\"</strong>. A Gen Z foi a primeira a entrar na puberdade já com o celular.",
    "tip": "<strong>Modelo mental:</strong> use 2012 como divisor de águas — meça qualquer fenômeno juvenil como \"antes\" × \"depois\"."
   },
   {
    "ic": "triangle",
    "t": "Curva em Taco de Hóquei",
    "b": "Internações por automutilação entre meninas pré-adolescentes (10-14 anos): estáveis nos 2000, disparadas ~+180% após 2012. A curva é <strong>abrupta, sincronizada internacionalmente</strong> e mais aguda em meninas pré-adolescentes — impressão digital de uma causa global comum.",
    "tip": "<strong>Modelo mental:</strong> quando muitos indicadores quebram juntos no mesmo ano, suspeite de um fator único e global — não de mil causas locais."
   },
   {
    "ic": "gap",
    "t": "Não São \"Os Tempos Difíceis\"",
    "b": "A crise de 2008 e questões políticas não explicam por que a quebra é em 2012 nem por que atinge especialmente meninas pré-adolescentes. <strong>Descartar como pânico moral ignora a magnitude e a sincronia dos dados.</strong>",
    "tip": "<strong>Sinal de alerta:</strong> \"os jovens sempre foram assim\" é a resposta que impede a ação — a escala e a sincronia deste surto são sem precedentes históricos."
   }
  ]
 },
 "ch02-o-que-criancas-precisam": {
  "cards": [
   {
    "ic": "leaf",
    "t": "Brincadeira Livre — o Currículo Oculto",
    "b": "Atividade autodirigida, sem objetivo externo, com risco e negociação entre as próprias crianças. É o <strong>principal mecanismo de desenvolvimento social e emocional</strong>. Duas crianças disputando quem é \"pega\" aprendem mais que num app solo.",
    "tip": "<strong>Como aplicar:</strong> garanta tempo não estruturado, sem adulto comandando e com algum risco real — é o currículo da vida adulta."
   },
   {
    "ic": "bubble",
    "t": "Sintonia — a Base da Autorregulação",
    "b": "Dança de revezamento de gestos, expressões e voz entre a criança e o outro — a base da autorregulação emocional. <strong>Telas interrompem a sintonia.</strong> Dar o celular para \"acalmar\" o bebê treina o oposto da autorregulação.",
    "tip": "<strong>Sinal de alerta:</strong> substituir sintonia por tela no primeiro ano de vida compromete a base da inteligência emocional."
   },
   {
    "ic": "clock",
    "t": "Puberdade — Período Sensível para a Cultura",
    "b": "A puberdade é uma janela em que aprender algo é fácil — e a Gen Z a passou com o celular como \"professor\". <strong>O que entra nesse período, fixa.</strong> Se entra Instagram/TikTok, é isso que calibra a identidade.",
    "tip": "<strong>Modelo mental:</strong> pense na puberdade como solo fértil a ser semeado — o que se planta ali molda o adulto que virá."
   }
  ]
 },
 "ch03-modo-descoberta": {
  "cards": [
   {
    "ic": "mountain",
    "t": "Modo Descoberta vs. Modo Defesa",
    "b": "Descoberta = curioso, sociável, corajoso (florescer). Defesa = ansioso, fechado (sobreviver). A meta é mais descoberta. <strong>Base segura + risco gradual</strong> empurram para descoberta; securitismo + celular empurram para defesa.",
    "tip": "<strong>Como aplicar:</strong> ao avaliar qualquer ambiente ou atividade para uma criança, pergunte: \"isto empurra para descoberta ou para defesa?\""
   },
   {
    "ic": "leaf",
    "t": "Antifragilidade — o Risco é o Ingrediente",
    "b": "Crianças são antifrágeis: precisam de estresse moderado e tombos para ficar mais fortes. A brincadeira arriscada (altura, velocidade, luta de mentira) é <strong>vacina emocional</strong>. Superproteger é como viver estéril — produz adultos hipersensíveis.",
    "tip": "<strong>Modelo mental:</strong> pense em superproteção como alergia por excesso de higiene — ambiente limpo demais produz sistema emocional hipersensível."
   },
   {
    "ic": "steps",
    "t": "Ritos de Passagem e a Grande Inversão",
    "b": "Sociedades sempre marcaram a passagem para a vida adulta. A modernidade apagou os ritos e o celular travou a transição: <strong>superprotegemos no mundo real e subprotegemos no virtual</strong>. A régua invertida: mais autonomia real, menos liberdade virtual.",
    "tip": "<strong>Como aplicar:</strong> escalone responsabilidades por idade com reconhecimento explícito — ir sozinho à padaria, primeiro emprego, dirigir. Cada degrau é um rito."
   }
  ]
 },
 "ch04-quatro-danos": {
  "cards": [
   {
    "ic": "triangle",
    "t": "Os 4 Danos — Checklist Diagnóstico",
    "b": "<strong>1. Privação social</strong> (122→67 min/dia cara a cara, 2012-2019) · <strong>2. Privação de sono</strong> (tela na cama na fase de cabeamento cerebral) · <strong>3. Fragmentação da atenção</strong> (~192 notificações/dia) · <strong>4. Vício</strong> (recompensa variável + córtex frontal imaturo).",
    "tip": "<strong>Como aplicar:</strong> para cada hábito digital, pergunte qual dos 4 danos ele agrava — se marca vários, é grave."
   },
   {
    "ic": "gap",
    "t": "Bloqueadores de Experiência",
    "b": "O pior do celular muitas vezes não é o que ele faz — é tudo o que ele <strong>impede de acontecer</strong>: sono, amizade presencial, foco, brincadeira. Pense em custo de oportunidade, não só em conteúdo.",
    "tip": "<strong>Sinal de alerta:</strong> \"é conteúdo educativo!\" ignora que o dano vem do deslocamento de experiências reais e do design viciante, não só do conteúdo."
   },
   {
    "ic": "spiral",
    "t": "Recompensa Variável + Córtex Imaturo",
    "b": "O mecanismo de máquina caça-níquel das curtidas/feed — o mais viciante que existe. O cérebro adolescente é alvo fácil porque o <strong>córtex pré-frontal (o freio) ainda não amadureceu</strong>. Rede social não cura solidão: é substituto pobre da presença.",
    "tip": "<strong>Modelo mental:</strong> \"só mais um vídeo\" é a recompensa variável intermitente em ação — o design que fisga o cérebro adolescente."
   }
  ]
 },
 "ch05-meninas-meninos": {
  "cards": [
   {
    "ic": "wave",
    "t": "Meninas — os 4 Caminhos do Dano",
    "b": "As redes amplificam o que é mais sensível na vida social feminina: <strong>(1) contágio sociogênico</strong> (transtornos se espalham por imitação) · <strong>(2) comparação visual constante</strong> · <strong>(3) agressão relacional amplificada</strong> (exclusão pública 24h) · <strong>(4) predadores</strong>.",
    "tip": "<strong>Sinal de alerta:</strong> permanência e publicidade digital transformam humilhação passageira em registro público permanente — muito mais danoso que o bullying presencial."
   },
   {
    "ic": "gap",
    "t": "Meninos — Falha em Decolar",
    "b": "O dano é mais antigo, lento e difuso: retraimento para games e pornografia. O mundo real ficou menos recompensador; o virtual oferece <strong>progressão, status e prazer sem risco de rejeição</strong>. Game/pornô são sintoma de um real pouco recompensador, não a raiz.",
    "tip": "<strong>Como aplicar:</strong> não demonize só os games — a pergunta é \"do que o real deixou de recompensar este menino?\". Aumente a gravidade do mundo real."
   },
   {
    "ic": "scale",
    "t": "Mesma Causa, Sintomas Opostos",
    "b": "Meninas internalizam (ansiedade, depressão). Meninos se retiram (desengajamento, isolamento). Ignorar os meninos porque \"as meninas estão pior\" é erro — o dano deles é <strong>silencioso e tardio, mas profundo</strong>.",
    "tip": "<strong>Modelo mental:</strong> pense em gravidade dos mundos — quando o virtual puxa mais que o real, o jovem orbita a tela. Aumente a atratividade do real."
   }
  ]
 },
 "ch06-elevacao-espiritual": {
  "cards": [
   {
    "ic": "mountain",
    "t": "As 6 Práticas de Elevação",
    "b": "Contra a degradação: <strong>(1) Sacralidade compartilhada</strong> · <strong>(2) Encarnação</strong> (fazer com o corpo) · <strong>(3) Quietude e meditação</strong> · <strong>(4) Autotranscendência</strong> (natureza, espanto) · <strong>(5) Perdão</strong> (sair do ciclo de indignação) · <strong>(6) O sublime na natureza</strong>.",
    "tip": "<strong>Como aplicar:</strong> use a efervescência coletiva como teste — a atividade gera energia de \"estar junto\"? Se sim, é elevadora."
   },
   {
    "ic": "leaf",
    "t": "Efervescência Coletiva",
    "b": "A energia emocional compartilhada gerada por estar <strong>junto fisicamente</strong> — esporte, ritual, festa, canto, refeição. Fonte de pertencimento que a tela não replica. O sábado digital (telas guardadas, caminhada, refeição juntos) exemplifica.",
    "tip": "<strong>Regra:</strong> só restringir sem substituir: tirar a tela e deixar o vazio convida à recaída — preencha com encarnação e comunidade."
   },
   {
    "ic": "spark",
    "t": "Sagrado vs. Profano",
    "b": "A tela achata tudo ao <strong>profano comum</strong> (fragmentado, comparativo, raso). Práticas sagradas reintroduzem hierarquia de significado. O ciclo de raiva premiado pelo feed é <strong>degradação espiritual disfarçada de virtude</strong>.",
    "tip": "<strong>Sinal de alerta:</strong> indignação como esporte é degradação — o feed premia o engajamento emocional negativo porque gera mais dados."
   }
  ]
 },
 "ch07-acao-coletiva": {
  "cards": [
   {
    "ic": "link",
    "t": "Dilema do Prisioneiro dos Pais",
    "b": "Cada pai dá o celular para o filho não ficar de fora → resultado coletivo pior para todos. <strong>Não é falha de força de vontade individual</strong> — é estrutura de incentivos. A saída é coletiva, eliminando o custo de ir primeiro e atingindo massa crítica.",
    "tip": "<strong>Como aplicar:</strong> pare de buscar solução individual para problema coletivo — a pergunta certa é \"como mudamos a norma do grupo?\""
   },
   {
    "ic": "steps",
    "t": "As 4 Alavancas da Ação Coletiva",
    "b": "(1) <strong>Coordenação voluntária</strong> (pais de uma turma combinam juntos) · (2) <strong>Normas/moralização</strong> (comunidade tornando inaceitável, como dirigir bêbado) · (3) <strong>Tecnologia</strong> (celulares básicos, bolsas com cadeado) · (4) <strong>Leis</strong> (idade mínima, verificação).",
    "tip": "<strong>Regra:</strong> combine as quatro alavancas — nenhuma basta isolada; juntas, atingem a massa crítica que vira o padrão."
   },
   {
    "ic": "mountain",
    "t": "De Volta à Terra — a Bússola",
    "b": "Toda medida boa devolve a criança ao <strong>mundo físico, encarnado e comunitário</strong>. A Grande Reconfiguração foi feita por nós e é reversível por nós. Você não age sozinho contra a maré — você acelera uma maré que já começou.",
    "tip": "<strong>Como aplicar:</strong> use \"de volta à Terra\" como bússola de decisão — a medida reconecta a criança ao mundo físico e à comunidade? Então é boa."
   }
  ]
 }
}
```
