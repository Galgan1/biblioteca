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

# LIVRO PARA APROFUNDAR: A História do Futebol Brasileiro — Mário Filho e clássicos do tema

**Subtítulo:** VISÃO GERAL · COMO UM ESPORTE DE ELITE VIROU A ALMA DO BRASIL
**Ideia central:** O futebol chegou ao Brasil em 1894 como passatempo de uma elite branca e europeizada — e virou a coisa mais brasileira que existe. O clássico de Mário Filho, 'O Negro no Futebol Brasileiro', conta como: foi quando o negro, o mulato e o pobre furaram a barreira e venceram que o jogo deixou de ser cópia e ganhou ginga, drible e alma. Desse encontro nasceram o futebol-arte, a glória do tri de Pelé e os traumas do Maracanazo e do 7 a 1. A história do futebol brasileiro é o próprio Brasil aprendendo a se olhar no espelho.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-origem-aristocratica` — CAPÍTULO 1: A Origem Aristocrática (1894)
- `ch02-barreira-racial` — CAPÍTULO 2: A Barreira Racial e o 'Pó de Arroz'
- `ch03-ruptura-vasco` — CAPÍTULO 3: A Ruptura — o Vasco da Gama (1923)
- `ch04-friedenreich` — CAPÍTULO 4: Friedenreich, o Primeiro Craque Mestiço
- `ch05-profissionalizacao` — CAPÍTULO 5: A Profissionalização (1933) e Leônidas (1938)
- `ch06-futebol-arte` — CAPÍTULO 6: O Futebol-Arte — a Ginga
- `ch07-maracanazo` — CAPÍTULO 7: O Maracanazo (1950) e o 'Complexo de Vira-Lata'
- `ch08-tri-pele` — CAPÍTULO 8: A Glória — 1958, 1962, 1970
- `ch09-1982-tetra-penta` — CAPÍTULO 9: 1982, o Tetra e o Penta
- `ch10-7x1-legado` — CAPÍTULO 10: O 7 a 1, o Legado e o Debate

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-origem-aristocratica": {
  "cards": [
   {
    "ic": "flag",
    "t": "Charles Miller Traz o Jogo",
    "b": "Filho de pai escocês e mãe brasileira, <strong>Charles Miller</strong> voltou a São Paulo em <strong>1894</strong> com duas bolas, chuteiras, bomba de ar e um livro de regras. Organizou a <strong>primeira partida oficial</strong> do país em 14 de abril de 1895, na Várzea do Carmo.",
    "tip": "<strong>Marco:</strong> o futebol entra pelo trilho inglês — funcionários da São Paulo Railway e do gás."
   },
   {
    "ic": "mask",
    "t": "Esporte de Distinção",
    "b": "Nos primeiros anos o futebol 'oficial' é <strong>amador, branco e de elite</strong>. Jogar era exibir status — pertencer a um clube de sócios ricos, vestir-se 'à inglesa'. O povo jogava nas várzeas, fora das ligas.",
    "tip": "<strong>Cuidado com o mito:</strong> a paixão nacional não é a origem — é a conquista que veio depois."
   },
   {
    "ic": "key",
    "t": "O Amadorismo como Filtro",
    "b": "Exigir que ninguém recebesse para jogar era, na prática, um <strong>filtro de classe</strong>: só jogava quem podia se dar ao luxo de não ser pago. O muro do amadorismo guardava o jogo para os ricos.",
    "tip": "<strong>Antecipe o conflito:</strong> derrubar esse muro será o motor de toda a história seguinte."
   }
  ]
 },
 "ch02-barreira-racial": {
  "cards": [
   {
    "ic": "mask",
    "t": "O 'Pó de Arroz'",
    "b": "Conta a lenda que o mulato <strong>Carlos Alberto</strong>, do Fluminense, <strong>empoava o rosto</strong> para clarear a pele e ser aceito — daí o apelido 'pó de arroz' da torcida tricolor. O corpo do jogador virou o palco do preconceito.",
    "tip": "<strong>Símbolo:</strong> para ser tolerado, o talento negro tinha de se disfarçar de branco."
   },
   {
    "ic": "gap",
    "t": "Dois Futebóis Paralelos",
    "b": "De um lado, as <strong>ligas de elite</strong> (brancas, amadoras); de outro, o <strong>futebol de várzea</strong>, onde negros e operários jogavam com craque de sobra, longe dos holofotes oficiais.",
    "tip": "<strong>Tensão:</strong> o talento estava do lado de fora — pressionando para entrar."
   },
   {
    "ic": "lens",
    "t": "A Tese de Mário Filho",
    "b": "Para o autor, a história do nosso futebol <strong>é</strong> a história dessa barreira sendo furada. O jogo só vira brasileiro quando o excluído entra — e ganha.",
    "tip": "<strong>Atribua sempre:</strong> 'segundo Mário Filho' — é a tese do livro, não um fato neutro."
   }
  ]
 },
 "ch03-ruptura-vasco": {
  "cards": [
   {
    "ic": "mountain",
    "t": "O Título de 1923",
    "b": "Sustentado pela colônia portuguesa, o <strong>Vasco</strong> montou um time de <strong>negros, mulatos e trabalhadores</strong> e venceu o Campeonato Carioca de 1923 na primeira tentativa. A prova em campo de que o talento não tinha cor nem classe.",
    "tip": "<strong>Virada:</strong> pela primeira vez, o excluído ganha dentro do sistema oficial."
   },
   {
    "ic": "sword",
    "t": "A Reação da Elite (AMEA)",
    "b": "Os clubes de elite criaram uma liga separada com exigências — comprovante de <strong>emprego</strong>, prova de <strong>alfabetização</strong> — desenhadas para excluir o jogador pobre e negro disfarçando o preconceito de 'critério'.",
    "tip": "<strong>Reconheça o padrão:</strong> a regra 'neutra' como instrumento de exclusão."
   },
   {
    "ic": "key",
    "t": "A Resistência",
    "b": "O Vasco se recusou a dispensar seus jogadores. A pressão pela inclusão tornou-se <strong>irreversível</strong> — o futebol brasileiro já tinha mudado de dono.",
    "tip": "<strong>Lição:</strong> conquistas sociais avançam quando alguém se recusa a recuar."
   }
  ]
 },
 "ch04-friedenreich": {
  "cards": [
   {
    "ic": "spark",
    "t": "O Gol de 1919",
    "b": "<strong>Arthur Friedenreich</strong> marcou o gol do título sul-americano de <strong>1919</strong> sobre o Uruguai. Considerado o <strong>maior craque brasileiro antes da era Pelé</strong>, foi o primeiro ídolo a unir técnica de elite e origem popular.",
    "tip": "<strong>Pioneiro:</strong> a ponte entre o futebol importado e o futebol-arte por vir."
   },
   {
    "ic": "mask",
    "t": "O Corpo do Conflito",
    "b": "Mulato de olhos verdes, <strong>alisava o cabelo</strong> no vestiário antes de entrar em campo. O maior ídolo do país encarnava a mesma tensão racial que a sociedade tentava esconder.",
    "tip": "<strong>Leitura:</strong> o ídolo não escapa do preconceito — ele o carrega à vista de todos."
   },
   {
    "ic": "constellation",
    "t": "A Semente do Estilo",
    "b": "Em Friedenreich já aparece o <strong>drible</strong> como linguagem — o gosto pela jogada de efeito que, décadas depois, definiria o Brasil no mundo.",
    "tip": "<strong>Continuidade:</strong> de Fried a Garrincha e Pelé, a mesma assinatura."
   }
  ]
 },
 "ch05-profissionalizacao": {
  "cards": [
   {
    "ic": "key",
    "t": "O Fim do Amadorismo",
    "b": "A <strong>profissionalização de 1933</strong> derrubou o filtro de classe: quem joga, recebe. O acesso ao futebol de ponta se <strong>democratiza</strong>, e a era dos grandes craques populares começa.",
    "tip": "<strong>Marco:</strong> o talento, não a origem, passa a decidir quem joga."
   },
   {
    "ic": "spark",
    "t": "Leônidas, o Diamante Negro",
    "b": "Associado à <strong>bicicleta</strong>, <strong>Leônidas da Silva</strong> foi artilheiro da <strong>Copa de 1938</strong> (França), onde o Brasil ficou em 3º. Primeiro ídolo negro de massa do país.",
    "tip": "<strong>Prova mundial:</strong> em campo internacional, o futebol brasileiro mostra voz própria."
   },
   {
    "ic": "steps",
    "t": "Talento Popular no Topo",
    "b": "Com o muro derrubado, o repertório das várzeas chega à seleção. O futebol deixa de imitar a Europa e começa a <strong>inventar a si mesmo</strong>.",
    "tip": "<strong>Transição:</strong> daqui ao futebol-arte é um passo."
   }
  ]
 },
 "ch06-futebol-arte": {
  "cards": [
   {
    "ic": "spark",
    "t": "A Ginga",
    "b": "O traço brasileiro: <strong>drible, finta e improviso</strong>, um jeito de jogar que herda o gingado da capoeira e o suingue do samba. Não é só eficiência — é <strong>expressão</strong>.",
    "tip": "<strong>Identidade:</strong> o mundo aprende a reconhecer o 'jogo brasileiro' pela ginga."
   },
   {
    "ic": "leaf",
    "t": "Beleza como Fim",
    "b": "Para Galeano, o <strong>futebol-arte</strong> se opõe ao futebol-resultado: jogar bonito tem valor próprio, mesmo quando não vence. A torcida brasileira ama o gol de placa tanto quanto a taça.",
    "tip": "<strong>Valor cultural:</strong> a estética do jogo vira patrimônio nacional."
   },
   {
    "ic": "link",
    "t": "Mestiçagem em Campo",
    "b": "O estilo é <strong>mestiço</strong> por definição — soma de heranças africanas, europeias e indígenas traduzidas em movimento. Gilberto Freyre leu nisso a 'cara' do Brasil.",
    "tip": "<strong>Atribua:</strong> a leitura 'dionisíaca/mestiça' é de Freyre — fundadora e hoje debatida."
   }
  ]
 },
 "ch07-maracanazo": {
  "cards": [
   {
    "ic": "wave",
    "t": "A Tragédia de 1950",
    "b": "Diante de quase 200 mil pessoas, o Brasil saiu na frente e <strong>perdeu de virada para o Uruguai, 2 a 1</strong>, o <strong>Maracanazo</strong>. O silêncio do estádio virou símbolo de uma nação em choque.",
    "tip": "<strong>Trauma fundador:</strong> a derrota em casa marca o futebol brasileiro para sempre."
   },
   {
    "ic": "mask",
    "t": "O Complexo de Vira-Lata",
    "b": "<strong>Nelson Rodrigues</strong> cunhou a expressão: o brasileiro que se sente <strong>inferior</strong> diante do resto do mundo. A ferida de 1950 virou diagnóstico de um país.",
    "tip": "<strong>Atribua:</strong> 'complexo de vira-lata' é de Nelson Rodrigues, após 1950."
   },
   {
    "ic": "spark",
    "t": "A Ferida como Combustível",
    "b": "O trauma não paralisou — virou <strong>fome de redenção</strong>. A dor de 1950 prepara o terreno para a explosão de 1958.",
    "tip": "<strong>Arco:</strong> toda grande redenção começa numa grande queda."
   }
  ]
 },
 "ch08-tri-pele": {
  "cards": [
   {
    "ic": "mountain",
    "t": "1958 e 1962 — o Bi",
    "b": "<strong>1958 (Suécia):</strong> primeiro título, 5 a 2 na final sobre os donos da casa; surge <strong>Pelé</strong>, aos 17 anos, ao lado de <strong>Garrincha</strong>. <strong>1962 (Chile):</strong> bicampeão, 3 a 1 na final; com Pelé lesionado, Garrincha carrega o time.",
    "tip": "<strong>Redenção:</strong> oito anos depois do Maracanazo, o Brasil é campeão do mundo."
   },
   {
    "ic": "spark",
    "t": "1970 — o Time Perfeito",
    "b": "<strong>Tricampeão</strong> no México, 4 a 1 sobre a Itália, campanha perfeita. <strong>Pelé, Tostão, Gérson, Jairzinho, Rivelino e Carlos Alberto</strong> — o gol coletivo da final é eleito por muitos o melhor de todos os tempos.",
    "tip": "<strong>Auge:</strong> o futebol-arte e o resultado, finalmente, na mesma equipe."
   },
   {
    "ic": "constellation",
    "t": "O 'País do Futebol'",
    "b": "Com o tri, o Brasil ganha de vez a taça Jules Rimet e a <strong>identidade mundial</strong> de melhor do mundo no esporte. O futebol vira religião nacional.",
    "tip": "<strong>Significado:</strong> a vitória esportiva vira projeto de autoestima de um povo."
   }
  ]
 },
 "ch09-1982-tetra-penta": {
  "cards": [
   {
    "ic": "leaf",
    "t": "1982 — a Beleza que Perdeu",
    "b": "O time de <strong>Telê Santana</strong> — <strong>Sócrates, Zico, Falcão, Cerezo</strong> — encantou o mundo, mas caiu para a Itália de Paolo Rossi (3 a 2). Virou o símbolo eterno de que jogar bonito nem sempre vence — e por isso é amado.",
    "tip": "<strong>Paradoxo:</strong> a derrota mais querida da história do futebol brasileiro."
   },
   {
    "ic": "key",
    "t": "1994 — o Tetra",
    "b": "Nos <strong>Estados Unidos</strong>, o Brasil é <strong>tetracampeão</strong> nos pênaltis sobre a Itália após 0 a 0. O pragmatismo de <strong>Romário e Bebeto</strong> exorciza, 44 anos depois, o fantasma de 1950.",
    "tip": "<strong>Cura:</strong> a vitória que fecha a ferida aberta no Maracanã."
   },
   {
    "ic": "spark",
    "t": "2002 — o Penta",
    "b": "Na <strong>Coreia/Japão</strong>, <strong>pentacampeão</strong>, 2 a 0 sobre a Alemanha, dois gols de <strong>Ronaldo</strong>, com Rivaldo e Ronaldinho. O Brasil chega a cinco estrelas, recordista mundial.",
    "tip": "<strong>Marca:</strong> nenhuma seleção ganhou mais Copas do que o Brasil."
   }
  ]
 },
 "ch10-7x1-legado": {
  "cards": [
   {
    "ic": "wave",
    "t": "2014 — o Mineiraço",
    "b": "Na semifinal da Copa em casa, o Brasil foi goleado pela <strong>Alemanha por 7 a 1</strong>, sem o lesionado Neymar. O avesso de 1950, em escala digital — e, como ele, um espelho do país em crise consigo mesmo.",
    "tip": "<strong>Eco:</strong> 64 anos depois, outra tragédia em casa marca uma geração."
   },
   {
    "ic": "lens",
    "t": "O Mito da Democracia Racial",
    "b": "Freyre leu no futebol a prova de uma <strong>'democracia racial'</strong>. A crítica atual responde: a inclusão no gramado <strong>conviveu com o racismo</strong> — do 'pó de arroz' aos casos de injúria racial nas arquibancadas no século XXI.",
    "tip": "<strong>Honestidade:</strong> o futebol foi arena da disputa racial, não a sua solução."
   },
   {
    "ic": "constellation",
    "t": "O Futebol como Brasil",
    "b": "De Charles Miller a Neymar, o futebol é onde o Brasil <strong>se vê inteiro</strong>: a inclusão e o preconceito, o gênio e a tragédia, a festa e a ferida.",
    "tip": "<strong>Síntese:</strong> entender o futebol brasileiro é entender o Brasil."
   }
  ]
 }
}
```
