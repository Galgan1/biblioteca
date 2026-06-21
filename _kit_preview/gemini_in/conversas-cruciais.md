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

# LIVRO PARA APROFUNDAR: Conversas Cruciais — Kerry Patterson, Joseph Grenny, Ron McMillan & Al Switzler

**Subtítulo:** VISÃO GERAL · DIÁLOGO DE ALTO RISCO
**Ideia central:** Uma conversa vira crucial quando três condições se cruzam: altas apostas, opiniões opostas e emoções fortes. São exatamente as conversas que mais importam — e nas quais costumamos nos sair pior. Patterson, Grenny, McMillan e Switzler mostram como encher o Pool de Significado Comum e dialogar em vez de fugir ou explodir.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-conversa-crucial` — CAPÍTULO 1: O que é uma Conversa Crucial
- `ch02-pool-de-significado` — CAPÍTULOS 2–3: Diálogo e Coração
- `ch04-aprender-a-observar` — CAPÍTULO 4: Aprender a Observar
- `ch05-tornar-seguro` — CAPÍTULO 5: Tornar Seguro
- `ch06-dominar-historias` — CAPÍTULO 6: Dominar Minhas Histórias
- `ch07-state` — CAPÍTULO 7: Expressar Meu Caminho — STATE
- `ch08-ampp` — CAPÍTULO 8: Explorar os Caminhos do Outro — AMPP
- `ch09-passar-a-acao` — CAPÍTULO 9: Passar à Ação — WWWF

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-conversa-crucial": {
  "cards": [
   {
    "ic": "triangle",
    "t": "As 3 Condições",
    "b": "<strong>(1) Altas apostas</strong>, <strong>(2) opiniões divergem</strong> e <strong>(3) emoções estão fortes</strong>. As três juntas ativam o modo 'conversa crucial'. A lei cruel: quanto mais a conversa importa, pior tendemos a nos comportar.",
    "tip": "<strong>Como aplicar:</strong> nomeie internamente 'isto virou crucial' e desacelere antes de reagir."
   },
   {
    "ic": "fork",
    "t": "As 3 Saídas Possíveis",
    "b": "<strong>Evitar</strong> (fugir), <strong>enfrentar mal</strong> (atacar ou calar) ou <strong>dialogar</strong>. Só a terceira preserva o resultado e a relação ao mesmo tempo. O livro inteiro é o caminho para a terceira via.",
    "tip": "<strong>Modelo mental:</strong> troque o reflexo 'fugir ou explodir' pela escolha deliberada de dialogar."
   },
   {
    "ic": "spark",
    "t": "Sequestro Emocional",
    "b": "Sob ameaça, o sangue migra para os músculos e o cérebro 'pensante' fica subnutrido — daí decisões piores justamente na hora crucial. Os sinais físicos (estômago aperta, voz endurece) são o alarme de que a conversa virou crucial.",
    "tip": "<strong>Sinal de alerta:</strong> impulso de fugir ou atacar = sinal fisiológico, não estratégia. Desacelere."
   }
  ]
 },
 "ch02-pool-de-significado": {
  "cards": [
   {
    "ic": "layers",
    "t": "Pool de Significado Comum",
    "b": "O reservatório de tudo que os envolvidos pensam e sentem sobre o tema. <strong>Pool cheio = decisões melhores + adesão maior</strong>. Silêncio (reter) e violência (impor) são as duas formas de esvaziá-lo.",
    "tip": "<strong>Modelo mental:</strong> cada ideia retida ou imposta é uma retirada; cada ideia honesta é um depósito no pool."
   },
   {
    "ic": "bulb",
    "t": "Começar pelo Coração",
    "b": "A única pessoa que você controla é você. Antes da técnica, ajuste o <strong>motivo</strong>: foque no que você realmente quer — para si, para o outro e para a relação. Sob estresse, o objetivo degrada silenciosamente (de resolver → punir, ganhar, fugir).",
    "tip": "<strong>Como aplicar:</strong> teste do 'querer vs. fazer' — 'estou agindo como alguém que quer X?'."
   },
   {
    "ic": "pivot",
    "t": "Recuse a Escolha do Tolo",
    "b": "A dicotomia falsa: 'ou falo a verdade ou preservo a relação'. A <strong>pergunta-E</strong>: 'Como eu poderia ser totalmente honesto E preservar a relação?' Buscar as duas coisas reativa o cérebro criativo.",
    "tip": "<strong>Regra:</strong> quando travar, trate o impulso de 'ganhar' como bandeira vermelha — o objetivo degradou."
   }
  ]
 },
 "ch04-aprender-a-observar": {
  "cards": [
   {
    "ic": "eye",
    "t": "Visão Dupla: Conteúdo + Condições",
    "b": "Divida a atenção: uma parte no assunto, outra no termômetro emocional. O sinal-mestre é a <strong>perda de segurança</strong> — quando alguém se sente inseguro, sai do diálogo para silêncio ou violência.",
    "tip": "<strong>Como aplicar:</strong> ao notar mudança no clima, pare o conteúdo e leia a condição: 'o que ameaçou a segurança?'."
   },
   {
    "ic": "mask",
    "t": "Silêncio × Violência em Detalhe",
    "b": "<strong>Silêncio</strong>: mascarar (ironia, açúcar), esquivar (desviar do tema real), recuar (sair). <strong>Violência</strong>: controlar (forçar a visão), rotular (estereotipar), atacar (humilhar). Ambos são sintomas de medo, não de maldade.",
    "tip": "<strong>Modelo mental:</strong> veja silêncio e violência como medo — a pergunta vira 'o que ameaçou?', não 'como retaliar?'."
   },
   {
    "ic": "person",
    "t": "Seu Estilo sob Estresse",
    "b": "Qual é o seu reflexo quando a pressão sobe — silêncio ou violência? Conhecer seu gatilho pessoal é o pré-requisito para não ser refém dele na hora que mais importa.",
    "tip": "<strong>Sinal de alerta:</strong> quem ignora o próprio gatilho é conduzido por ele — justamente na conversa crucial."
   }
  ]
 },
 "ch05-tornar-seguro": {
  "cards": [
   {
    "ic": "scale",
    "t": "Propósito + Respeito Mútuos",
    "b": "Segurança apoia-se em duas condições. <strong>Propósito Mútuo</strong> (a porta de entrada): o outro acredita que você trabalha por um objetivo comum. <strong>Respeito Mútuo</strong> (condição de continuidade): o outro se sente tratado com dignidade.",
    "tip": "<strong>Como aplicar:</strong> ao travar, pergunte 'qual condição quebrou — propósito ou respeito?' antes de qualquer argumento."
   },
   {
    "ic": "pivot",
    "t": "Contraste (Não-/Sim-)",
    "b": "Afirmação em dois tempos para reparar mal-entendidos sem recuar do conteúdo. <strong>Parte 'não'</strong>: diga o que você não quis dizer. <strong>Parte 'sim'</strong>: confirme o respeito e o real propósito. Contraste ≠ recuar — você mantém o conteúdo.",
    "tip": "<strong>Como aplicar:</strong> 'Não quero dizer X. Quero Y.' — a ordem importa: desfaça o medo antes de afirmar."
   },
   {
    "ic": "spiral",
    "t": "CRIB — Criar Propósito Mútuo",
    "b": "Quando os propósitos genuinamente divergem: <strong>C</strong>ommit (comprometa-se a buscar algo comum) → <strong>R</strong>ecognize (propósito por trás da estratégia) → <strong>I</strong>nvent (propósito mais alto) → <strong>B</strong>rainstorm (novas estratégias). Só gere opções depois de alinhar o propósito.",
    "tip": "<strong>Sinal de alerta:</strong> brainstorm sem propósito alinhado = disputa de estratégias. Faça o I antes do B."
   }
  ]
 },
 "ch06-dominar-historias": {
  "cards": [
   {
    "ic": "spiral",
    "t": "O Caminho para a Ação",
    "b": "A sequência: <strong>Ver/ouvir → contar uma História → Sentir → Agir</strong>. Você não controla o sentimento diretamente, mas controla a história que o gera. Rastreie de trás para frente: do sentir até a história e os fatos.",
    "tip": "<strong>Modelo mental:</strong> toda emoção forte é uma placa de 'história em construção' — pare e encontre a história por trás."
   },
   {
    "ic": "mask",
    "t": "As 3 Histórias Espertas",
    "b": "Interpretações que nos isentam: <strong>Vítima</strong> ('não é minha culpa' — omite seu papel), <strong>Vilão</strong> ('a culpa é toda dele' — demoniza o outro), <strong>Impotente</strong> ('não há nada que eu possa fazer' — justifica inação).",
    "tip": "<strong>Sinal de alerta:</strong> 'eu tive que…' é linguagem de impotência que esconde uma escolha que você fez."
   },
   {
    "ic": "bulb",
    "t": "Questões Espertas",
    "b": "Antídotos para recontar a história: <em>Estou fingindo não notar meu papel?</em> (desfaz Vítima). <em>Por que uma pessoa razoável faria isto?</em> (desfaz Vilão). <em>O que eu realmente quero?</em> (desfaz Impotente). <em>O que eu faria se quisesse mesmo isso?</em>",
    "tip": "<strong>Como aplicar:</strong> 'por que uma pessoa razoável, racional e decente faria isso?' — devolve humanidade ao outro."
   }
  ]
 },
 "ch07-state": {
  "cards": [
   {
    "ic": "steps",
    "t": "O Método STATE",
    "b": "<strong>S</strong>hare your facts → <strong>T</strong>ell your story → <strong>A</strong>sk for others' paths → <strong>T</strong>alk tentatively → <strong>E</strong>ncourage testing. Os três primeiros: o que fazer. Os dois últimos: como fazer.",
    "tip": "<strong>Como aplicar:</strong> comece pelos fatos (menos controverso, mais persuasivo) — nunca pela conclusão."
   },
   {
    "ic": "bulb",
    "t": "Fatos Primeiro, Conclusão Depois",
    "b": "Abrir pela conclusão ('você é desorganizado') mata a segurança antes do primeiro fato. Fatos são o terreno menos discutível. A <strong>história provisória</strong> — dita com humildade ('começo a achar que…') — convida ao teste.",
    "tip": "<strong>Modelo mental:</strong> STATE é uma escada — fato → história → convite; quem começa pela conclusão cai."
   },
   {
    "ic": "leaf",
    "t": "Confiança + Humildade",
    "b": "Defender sua visão com firmeza <strong>e</strong> tratá-la como uma visão entre outras. Encorajar testes ≠ ceder: convidar discordância não é abrir mão do que você pensa. Tato é volume, não conteúdo — baixe a certeza no tom sem apagar a mensagem.",
    "tip": "<strong>Sinal de alerta:</strong> tanto tato que a mensagem real nunca chega é tão ruim quanto atacar."
   }
  ]
 },
 "ch08-ampp": {
  "cards": [
   {
    "ic": "wave",
    "t": "AMPP — Abrir a Porta",
    "b": "Quatro habilidades da intervenção mais suave à mais forte: <strong>A</strong>sk (pergunte) → <strong>M</strong>irror (espelhe a emoção visível) → <strong>P</strong>araphrase (reformule para provar que entendeu) → <strong>P</strong>rime (ofereça um palpite do sentimento). Comece por Ask; use Prime só em último caso.",
    "tip": "<strong>Como aplicar:</strong> 'O que está acontecendo?' → se nada vem → 'Você parece chateado' → reformule → 'Será que você está achando que…?'"
   },
   {
    "ic": "bubble",
    "t": "ABC — Responder sem Brigar",
    "b": "Ao discordar, em vez de 'você está errado': <strong>A</strong>gree (concorde no que concorda), <strong>B</strong>uild (acrescente o que faltou), <strong>C</strong>ompare (compare as visões). Quase toda discordância é sobre 10% — comece pelos 90% de concordância.",
    "tip": "<strong>Modelo mental:</strong> 'Concordamos em 90%; a briga é pelos 10%.' Comece pelos 90."
   },
   {
    "ic": "key",
    "t": "Curiosidade Genuína",
    "b": "A postura que torna o AMPP verdadeiro. Escuta fingida soa manipuladora e quebra a segurança. <strong>Trate o silêncio/violência do outro como medo, não ataque</strong> — a pergunta vira 'o que o assustou?'.",
    "tip": "<strong>Sinal de alerta:</strong> parafrasear sem curiosidade real soa falso e destrói mais segurança do que silêncio."
   }
  ]
 },
 "ch09-passar-a-acao": {
  "cards": [
   {
    "ic": "fork",
    "t": "Os 4 Métodos de Decisão",
    "b": "Do menos ao mais participativo: <strong>Comando</strong> (autoridade decide) → <strong>Consulta</strong> (ouve e decide sozinho) → <strong>Voto</strong> (maioria) → <strong>Consenso</strong> (todos concordam). Escolha com as 4 perguntas: quem se importa? quem sabe? quem precisa concordar? quantos vale envolver?",
    "tip": "<strong>Modelo mental:</strong> defina o método antes de mergulhar no mérito — evita briga depois sobre 'quem tinha o direito de decidir'."
   },
   {
    "ic": "wrench",
    "t": "WWWF — Feche com Compromisso",
    "b": "Sem registro, o diálogo evapora em 'todo mundo' = ninguém. Defina: <strong>W</strong>ho (quem — nome específico), <strong>W</strong>hat (o quê — entregável claro), <strong>W</strong>hen (quando — data), <strong>F</strong>ollow-up (como e quando revisar).",
    "tip": "<strong>Como aplicar:</strong> 'Marina implanta o checklist até sexta; revisão na segunda de 15 min.' — nomes + entregável + data + revisão."
   },
   {
    "ic": "target",
    "t": "Diálogo ≠ Decisão",
    "b": "Concordar sobre significado é o pré-requisito, não o ato de decidir. <strong>'Todo mundo' = ninguém.</strong> Tarefa sem dono nomeado não é executada. Trate o fim de toda conversa crucial como um mini-contrato: quem, o quê, quando, e quando a gente revisa.",
    "tip": "<strong>Sinal de alerta:</strong> sair da conversa sem WWWF é converter bom diálogo em intenção sem dono."
   }
  ]
 }
}
```
