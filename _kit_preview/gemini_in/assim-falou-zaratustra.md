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

# LIVRO PARA APROFUNDAR: Assim Falou Zaratustra — Friedrich Nietzsche

**Subtítulo:** VISÃO GERAL · MORTE DE DEUS, ALÉM-DO-HOMEM E AMOR FATI
**Ideia central:** Zaratustra desce da montanha para ensinar o além-do-homem — porque 'Deus morreu' e cabe ao humano criar novo sentido na Terra. Uma filosofia encenada em parábolas, símbolos e discursos que não argumenta: canta. Seu teste supremo é o eterno retorno — querer que cada instante volte infinitas vezes.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-prologo-morte-de-deus` — CAPÍTULO 1: Prólogo — A Descida e a Morte de Deus
- `ch02-alem-do-homem` — CAPÍTULO 2: O Além-do-Homem — o Sentido da Terra
- `ch03-tres-metamorfoses` — CAPÍTULO 3: As Três Metamorfoses do Espírito
- `ch04-corpo-desprezadores` — CAPÍTULO 4: O Corpo e a Virtude Doadora
- `ch05-vontade-de-potencia` — CAPÍTULO 5: A Vontade de Potência
- `ch06-ressentimento-rebanho` — CAPÍTULO 6: Ressentimento e Transvaloração
- `ch07-eterno-retorno` — CAPÍTULO 7: O Eterno Retorno e o Convalescente
- `ch08-amor-fati-sim` — CAPÍTULO 8: Amor Fati — o Sagrado 'Sim' e o Meio-Dia
- `ch09-estrutura-simbolos` — CAPÍTULO 9: Estrutura, Símbolos e 'Para Todos e Para Ninguém'

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-prologo-morte-de-deus": {
  "cards": [
   {
    "ic": "triangle",
    "t": "Morte de Deus",
    "b": "'Deus morreu' não é ateísmo triunfante — é <strong>diagnóstico cultural</strong>: os valores supremos perderam a força de organizar a vida. Sobra o perigo do niilismo. A tarefa é criar sentido novo aqui, na Terra, sem o fiador celeste.",
    "tip": "<strong>Modelo mental:</strong> leia 'Deus morreu' como tarefa, não festa — o vazio é perigo; criar sentido novo é o trabalho."
   },
   {
    "ic": "steps",
    "t": "A Corda sobre o Abismo",
    "b": "'O homem é uma corda estendida entre o animal e o além-do-homem — uma corda sobre um abismo.' O valor do humano está em ser <strong>travessia e queda</strong>, não ponto de chegada. Valorize a travessia: o que dignifica é arriscar-se por algo maior que si.",
    "tip": "<strong>Como aplicar:</strong> o que ainda te prende ao lado do animal? o que te puxa para o outro lado? nomeie as duas forças."
   },
   {
    "ic": "mask",
    "t": "O Último Homem",
    "b": "O oposto do além-do-homem: <strong>'inventou a felicidade' e pisca</strong>. Quer só conforto, segurança e pequenos prazeres; aboliu o risco e o grande desejo. Quando Zaratustra o descreve como horror, a multidão aplaude e pede para ser ele. Lente afiada para a cultura do conforto/anestesia.",
    "tip": "<strong>Sinal de alerta:</strong> onde a vida só quer conforto e segurança, o último homem já reina — e reina com o aplauso da maioria."
   }
  ]
 },
 "ch02-alem-do-homem": {
  "cards": [
   {
    "ic": "mountain",
    "t": "Sentido Imanente",
    "b": "'O além-do-homem é o sentido da Terra.' Após a morte de Deus, o sentido não pode mais vir de um além-mundo: precisa ser criado <strong>aqui, fiel ao corpo e ao instante</strong>. Pergunte de cada ideal: aterra ou desterra?",
    "tip": "<strong>Modelo mental:</strong> meça cada valor por este critério — ele afirma a vida aqui ou foge para um 'além'?"
   },
   {
    "ic": "spark",
    "t": "Ser Humano é Ser Superável",
    "b": "'O homem é algo que deve ser superado.' Ser humano é ser <strong>material de obra, não obra acabada</strong>. Zaratustra não pede discípulos: pede criadores. Ninguém 'é' o super-homem; é horizonte que se cria pela ação.",
    "tip": "<strong>Como aplicar:</strong> crie, não copie — o além-do-homem se realiza quando você gera valores, não quando imita um modelo."
   },
   {
    "ic": "leaf",
    "t": "Fidelidade à Terra",
    "b": "Contra os 'desprezadores do corpo': amar o corpo, o instante, o real. Recusar a fuga para o transcendente é <strong>fidelidade à Terra</strong> — o solo do além-do-homem. Não é hedonismo: é afirmação do real a serviço da criação.",
    "tip": "<strong>Sinal de alerta:</strong> qualquer doutrina que rebaixa o corpo em nome da alma fala por uma vida fraca — suspeite dela."
   }
  ]
 },
 "ch03-tres-metamorfoses": {
  "cards": [
   {
    "ic": "steps",
    "t": "Camelo — O Espírito que Carrega",
    "b": "O camelo carrega o 'Tu Deves' com reverência: a moral, a tradição, o dever herdado. É <strong>necessário</strong> (sem disciplina não há força), mas é obediência. Ainda não é liberdade: é o estágio de quem aprende os valores antes de poder questioná-los.",
    "tip": "<strong>Modelo mental:</strong> o camelo é o ponto de partida indispensável — mas travar ali é permanecer na obediência sem criação."
   },
   {
    "ic": "sword",
    "t": "Leão — O Espírito que Conquista",
    "b": "No deserto, o camelo vira leão. Enfrenta o dragão 'Tu Deves' e diz '<strong>Eu Quero</strong>' em lugar de 'Tu Deves'. Conquista a liberdade <em>para</em> o novo — mas ainda só sabe <strong>negar e destruir</strong>. Ainda não cria.",
    "tip": "<strong>Sinal de alerta:</strong> muita rebeldia trava no leão — sabe recusar, não sabe construir. A liberdade é meio, não fim."
   },
   {
    "ic": "spark",
    "t": "Criança — O Espírito que Cria",
    "b": "'Inocência e esquecimento, um recomeço, um jogo, uma roda que gira por si, um sagrado <strong>sim</strong>.' Só a criança, livre do peso do passado, <strong>inventa valores novos</strong>. O ápice não é a seriedade do leão: é a leveza criadora da criança.",
    "tip": "<strong>Como aplicar:</strong> criar valores próprios exige esquecer o peso do 'tu deves' — a maturidade mais alta parece leveza, não peso."
   }
  ]
 },
 "ch04-corpo-desprezadores": {
  "cards": [
   {
    "ic": "person",
    "t": "O Corpo como Grande Razão",
    "b": "'Corpo sou eu inteiro, e nada além disso; a alma é apenas uma palavra para algo no corpo.' O <strong>Si-mesmo</strong> (Selbst) que habita o corpo é mais sábio que o 'eu' consciente. A consciência é um instrumento do corpo, não seu senhor.",
    "tip": "<strong>Como aplicar:</strong> ouça o Si-mesmo — a sabedoria está na vida inteira, não só na cabeça."
   },
   {
    "ic": "spark",
    "t": "A Virtude Doadora",
    "b": "A virtude mais alta <strong>transborda e cria</strong> — como o ouro, rara e inútil ao mercado, que brilha por se dar. A abstinência e a proibição são virtudes de fraqueza; a virtude doadora nasce de plenitude, não de dever.",
    "tip": "<strong>Modelo mental:</strong> meça a virtude pelo que ela doa, não pelo que proíbe — a virtude alta cria e transborda."
   },
   {
    "ic": "key",
    "t": "'Torna-te quem Tu és'",
    "b": "O fim do ensino de Zaratustra não é criar discípulos: é que cada um <strong>se perca e se reencontre</strong>. 'Agora vos perco; encontrai-vos a vós mesmos.' Realizar a própria potência singular — não copiar um modelo, nem mesmo o do mestre.",
    "tip": "<strong>Como aplicar:</strong> o objetivo não é ser Zaratustra — é ser você, com toda a força singular que isso implica."
   }
  ]
 },
 "ch05-vontade-de-potencia": {
  "cards": [
   {
    "ic": "mountain",
    "t": "Expansão, Não Conservação",
    "b": "A vontade de potência não é sobrevivência nem prazer: é <strong>crescer, superar-se, dar forma</strong>. 'Onde encontrei o vivente, encontrei vontade de potência.' Até a busca da verdade é uma forma de potência — querer tornar o mundo pensável.",
    "tip": "<strong>Modelo mental:</strong> leia motivações pela potência, não pelo prazer — o que parece busca de conforto costuma ser busca de sentir-se mais."
   },
   {
    "ic": "sword",
    "t": "Autossuperação — a Potência Suprema",
    "b": "'O que obedece a si mesmo é o que ordena.' A forma mais alta da vontade de potência é exercida sobre <strong>si mesmo</strong>: mandar em si é mais difícil que mandar nos outros. Autodomínio e autossuperação são o ápice.",
    "tip": "<strong>Como aplicar:</strong> comece o domínio por você — a maior potência não é controlar os outros, é comandar-se."
   },
   {
    "ic": "triangle",
    "t": "Criar Custa",
    "b": "Para criar valores novos é preciso destruir os velhos — o leão vem antes da criança. <strong>Não há autossuperação indolor.</strong> A vida se ultrapassa sempre, por isso há criação e destruição contínuas; resistir ao custo é resistir ao crescimento.",
    "tip": "<strong>Sinal de alerta:</strong> confundir vontade de potência com dominação dos outros é a distorção mais grosseira e a mais perigosa."
   }
  ]
 },
 "ch06-ressentimento-rebanho": {
  "cards": [
   {
    "ic": "lens",
    "t": "Genealogia dos Valores",
    "b": "Faça genealogia: de cada 'bem' pergunte <strong>de onde vem e a quem serve</strong>. A moral de rebanho nasce do ressentimento — primeiro dizem 'não' ao forte, e só então um 'sim' pálido a si. A fraqueza que chama de virtude sua própria impotência.",
    "tip": "<strong>Como aplicar:</strong> de cada valor pergunte — isso é força que transborda ou fraqueza que se vinga?"
   },
   {
    "ic": "scale",
    "t": "Moral de Senhor × Moral de Escravo",
    "b": "A do forte afirma a partir de si ('bom = nobre, pleno'). A do fraco define a partir do inimigo ('mau = o forte; logo eu, oposto a ele, sou bom'). <strong>Dois critérios opostos</strong> — um que parte de si, outro que parte do ódio.",
    "tip": "<strong>Modelo mental:</strong> desconfie da pregação da igualdade quando cheira a vingança — querer rebaixar o alto não é justiça, é ressentimento fantasiado."
   },
   {
    "ic": "spark",
    "t": "Transvaloração",
    "b": "Não é trocar valores por seus opostos: é mudar o <strong>critério</strong> — medir tudo pela vida e pela potência criadora, não pela conservação do rebanho. O espírito de gravidade (o peso dos 'bem e mal' herdados) vence-se rindo e dançando, não pela força bruta.",
    "tip": "<strong>Como aplicar:</strong> troque a régua, não só a tabela — transvalorar é mudar o critério (vida × negação), não inverter os itens."
   }
  ]
 },
 "ch07-eterno-retorno": {
  "cards": [
   {
    "ic": "spiral",
    "t": "O Teste Supremo",
    "b": "'E se cada instante — cada dor, cada tédio, cada alegria — tivesse de voltar infinitas vezes, idêntico?' É o <strong>peso máximo</strong>: você viveria de modo a querer isto de novo, eternamente? Quem suporta e ama isso alcança o amor fati.",
    "tip": "<strong>Como aplicar:</strong> use o retorno como teste — 'Quereria viver isto de novo infinitas vezes?' Se não, mude a vida ou sua relação com ela."
   },
   {
    "ic": "mask",
    "t": "O Nojo do Pequeno",
    "b": "O mais difícil de aceitar não é a dor — é que <strong>também o homem pequeno, o mesquinho, retorna eternamente</strong>. Vencer esse nojo (morder e cuspir a serpente) é a prova real. O pastor que morde ri como nunca riu ninguém — transfigurado.",
    "tip": "<strong>Modelo mental:</strong> o teste mais duro não é a dor; é o pequeno — aceitar que a mesquinhez também volta e ainda assim afirmar a vida."
   },
   {
    "ic": "clock",
    "t": "O Instante Carregado",
    "b": "O portão '<strong>Instante</strong>' (Augenblick): o agora onde passado e futuro se tocam. Se o tempo é infinito e as coisas finitas, tudo já passou por aqui e tudo voltará. O instante presente carrega em si toda a eternidade.",
    "tip": "<strong>Sinal de alerta:</strong> confundir eterno retorno com reencarnação ou progresso espiritual — não há evolução; é o mesmo, idêntico, sem redenção externa."
   }
  ]
 },
 "ch08-amor-fati-sim": {
  "cards": [
   {
    "ic": "spark",
    "t": "Amor Fati",
    "b": "Amar o destino — não resignação ('aceito porque não há jeito'), mas <strong>afirmação ativa</strong> ('quero exatamente isto, e que volte sempre'). Dizer sim à vida inteira, com seus contrários, alturas e abismos — o sim dionisíaco.",
    "tip": "<strong>Como aplicar:</strong> transforme aceitação em amor — o degrau acima de 'tolerar o que é' é querer que seja assim e que retorne."
   },
   {
    "ic": "eye",
    "t": "O Grande Meio-Dia",
    "b": "O instante de plenitude — '<strong>a sombra mais curta</strong>', o ponto médio do caminho entre o animal e o além-do-homem. O momento em que o homem pode dizer sim ao instante: 'a alegria quer eternidade, quer profunda, profunda eternidade.'",
    "tip": "<strong>Modelo mental:</strong> inclua a sombra — dizer sim só ao bom é meio-sim; o sim dionisíaco abraça dor e perda como parte do mesmo anel."
   },
   {
    "ic": "triangle",
    "t": "A Tentação da Compaixão",
    "b": "O 'último pecado' de Zaratustra (Parte IV): a compaixão pelos homens superiores. Superá-la não é dureza com os outros — é não deixar a <strong>pena adiar a tarefa criadora</strong>. A piedade mal dosada paralisa a obra.",
    "tip": "<strong>Sinal de alerta:</strong> amor fati não é fatalismo passivo — é afirmação intensa e ativa; confundi-los é deixar a vida acontecer em vez de querê-la."
   }
  ]
 },
 "ch09-estrutura-simbolos": {
  "cards": [
   {
    "ic": "book",
    "t": "Evangelho Invertido",
    "b": "Estilo bíblico ('Assim falou Zaratustra', bem-aventuranças, tentação no deserto) para anunciar o <strong>oposto da mensagem cristã</strong> — fidelidade à Terra, não ao céu. A forma é inseparável do conteúdo: a paródia é o argumento.",
    "tip": "<strong>Modelo mental:</strong> não leia como tratado com teses lineares — é poema/drama; contradiz-se, recua, ironiza; a forma faz parte do sentido."
   },
   {
    "ic": "constellation",
    "t": "Símbolos-Chave",
    "b": "<strong>Águia</strong> (orgulho) + <strong>Serpente</strong> em anel (sabedoria/eterno retorno); <strong>Corda/Abismo</strong> (o homem como travessia); <strong>Montanha × Mercado</strong> (solidão criadora × multidão); <strong>Meio-Dia</strong> (plenitude); <strong>Dança e Riso</strong> (vitória sobre o espírito de gravidade).",
    "tip": "<strong>Como aplicar:</strong> ao ler uma cena (pastor e serpente, portão 'Instante'), traduza a imagem em tese — qual ideia ela encarna?"
   },
   {
    "ic": "person",
    "t": "'Para Todos e Para Ninguém'",
    "b": "O subtítulo anuncia o paradoxo: universal no alcance, <strong>radicalmente solitário na compreensão</strong>. Zaratustra recusa discípulos: 'Agora vos perco; encontrai-vos a vós mesmos.' O livro aponta para fora de si — para que cada leitor encontre seu próprio caminho.",
    "tip": "<strong>Modelo mental:</strong> não confunda Zaratustra com Nietzsche o tempo todo — o personagem falha e aprende; a obra é um drama do pensamento."
   }
  ]
 }
}
```
