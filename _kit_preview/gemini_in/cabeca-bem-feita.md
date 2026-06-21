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

# LIVRO PARA APROFUNDAR: A Cabeça Bem-Feita — Edgar Morin

**Subtítulo:** VISÃO GERAL · REPENSAR A REFORMA, REFORMAR O PENSAMENTO
**Ideia central:** Vale mais uma cabeça bem-feita — que sabe organizar e religar saberes, colocar e tratar problemas — do que uma cabeça bem-cheia de informação acumulada e desconexa. O drama do ensino é a inadequação cada vez mais ampla, profunda e grave entre saberes separados e problemas multidimensionais. A saída é circular: reformar o pensamento para reformar o ensino — e vice-versa.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-os-desafios` — CAPÍTULO 1: Os Desafios
- `ch02-a-cabeca-bem-feita` — CAPÍTULO 2: A Cabeça Bem-Feita
- `ch03-a-condicao-humana` — CAPÍTULO 3: A Condição Humana
- `ch04-aprender-a-viver` — CAPÍTULO 4: Aprender a Viver
- `ch05-enfrentar-a-incerteza` — CAPÍTULO 5: Enfrentar a Incerteza
- `ch06-a-aprendizagem-cidada` — CAPÍTULO 6: A Aprendizagem Cidadã
- `ch07-os-tres-graus` — CAPÍTULO 7: Os Três Graus
- `ch08-a-reforma-do-pensamento` — CAPÍTULO 8: A Reforma do Pensamento
- `ch09-para-alem-das-contradicoes` — CAPÍTULO 9: Para Além das Contradições

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-os-desafios": {
  "cards": [
   {
    "ic": "triangle",
    "t": "A Inadequação Ampla e Grave",
    "b": "Fosso crescente entre <strong>saberes desunidos</strong> (disciplinas) e <strong>problemas entrelaçados</strong> (clima, saúde, cidade, paz). O especialista domina a parte e perde as interações que definem o todo. A cura não é mais conteúdo — é a <strong>aptidão para religar</strong>.",
    "tip": "<strong>Para refletir:</strong> 'isso é assunto de especialista' = o cidadão abdicou da democracia cognitiva."
   },
   {
    "ic": "fork",
    "t": "Os 3 Desafios + O Decisivo",
    "b": "<strong>Cultural</strong>: a ruptura entre as duas culturas (científica × humanística, C.P. Snow). <strong>Sociológico</strong>: sem organização, afogamos no dilúvio de informação. <strong>Cívico</strong>: a perda do global enfraquece responsabilidade. O <strong>desafio dos desafios</strong>: a reforma do pensamento que torna possível os três.",
    "tip": "<strong>Modelo mental:</strong> gavetas que não se abrem juntas — informação demais, compreensão de menos."
   },
   {
    "ic": "lens",
    "t": "Inteligência Parcelada",
    "b": "Visão profunda de um campo + <strong>cegueira total para suas conexões e consequências</strong>. A hiperespecialização rompe o complexo e o global, tornando invisíveis a solidariedade e as interações. Resultado: incapacidade de pensar os problemas que mais importam.",
    "tip": "<strong>Como aplicar:</strong> 'qual o contexto e o todo?' — essa pergunta sozinha já combate a inteligência parcelada."
   }
  ]
 },
 "ch02-a-cabeca-bem-feita": {
  "cards": [
   {
    "ic": "bulb",
    "t": "Aptidão Geral × Enciclopédia",
    "b": "A cabeça bem-feita tem <strong>aptidão para colocar e tratar o problema</strong>, não para guardar respostas prontas. Diante do novo: o 'bem-cheio' trava (sem fórmula); o 'bem-feito' pergunta 'qual é o problema?' e <strong>constrói o tratamento religando</strong> o que sabe.",
    "tip": "<strong>Como aplicar:</strong> 'que aptidão isto desenvolve?' — se o conteúdo não fortalece a capacidade de religar, é peso morto."
   },
   {
    "ic": "layers",
    "t": "Conhecimento Pertinente",
    "b": "Um saber só serve se restituir o <strong>contexto</strong> (sentido vem do conjunto), o <strong>global</strong> (partes ↔ todo), o <strong>multidimensional</strong> (realidade tem várias faces ao mesmo tempo) e o <strong>complexo</strong> (o que é tecido junto). Faltou um → parcelado.",
    "tip": "<strong>Modelo mental:</strong> pense nos 4 como checklist antes de concluir."
   },
   {
    "ic": "spark",
    "t": "Curiosidade como Combustível",
    "b": "A <strong>curiosidade é a faísca</strong> da cabeça bem-feita — a escola pode estimulá-la ou sufocá-la. Especialização precoce mata a curiosidade antes que ela floresça; sem curiosidade, a inteligência geral murcha. Proteja-a como o recurso que é.",
    "tip": "<strong>Para refletir:</strong> a pergunta ingênua é muitas vezes a mais pertinente — preserve o espanto."
   }
  ]
 },
 "ch03-a-condicao-humana": {
  "cards": [
   {
    "ic": "person",
    "t": "Unidualidade do Humano",
    "b": "Somos <strong>totalmente biológicos e totalmente culturais</strong> ao mesmo tempo — não metade de cada. Separar natureza e cultura mutila a compreensão de nós mesmos. O humano como nó onde física, biologia, psique, sociedade e cultura se atam.",
    "tip": "<strong>Modelo mental:</strong> use 'e... e...' em vez de 'ou... ou...' ao descrever o humano — biológico E cultural; sapiens E demens."
   },
   {
    "ic": "spiral",
    "t": "Tríade Indivíduo/Espécie/Sociedade",
    "b": "Cada termo produz e é produzido pelos outros — <strong>anel recursivo</strong>. Nenhum se entende isolado. E o anel interno: <strong>cérebro ⇄ mente ⇄ cultura</strong> — sem um não há os outros.",
    "tip": "<strong>Como aplicar:</strong> situe o humano no cosmos (poeira de estrelas), na vida (ser vivo) e na Terra (terráqueo) — restitui o sentido perdido pela disjunção."
   },
   {
    "ic": "constellation",
    "t": "Unitas Multiplex",
    "b": "A unidade humana <strong>contém</strong> a diversidade, e a diversidade <strong>contém</strong> a unidade — pensar as duas juntas, não escolher uma. O universalismo que apaga e o relativismo que separa são os dois anti-padrões simétricas.",
    "tip": "<strong>Para refletir:</strong> o conflito cultural tem terceira via — reconhecer a mesma condição humana sob a diversidade."
   }
  ]
 },
 "ch04-aprender-a-viver": {
  "cards": [
   {
    "ic": "bubble",
    "t": "Compreensão × Explicação",
    "b": "A <strong>explicação</strong> basta para o mundo dos objetos (causas, leis). A <strong>compreensão</strong> é indispensável para o mundo humano — captar o outro de dentro, com empatia. A escola ensina muito a explicar e quase nada a compreender.",
    "tip": "<strong>Como aplicar:</strong> 'estou explicando ou compreendendo?' — explicar fecha o caso; compreender abre o sujeito."
   },
   {
    "ic": "book",
    "t": "Literatura como Escola de Vida",
    "b": "Romance, poesia, cinema, teatro ensinam a <strong>complexidade humana</strong> que a explicação científica não alcança — sentimentos, destino, contradição. O personagem do romance é simulador de vidas: nele se experimenta, sem risco, a complexidade dos outros.",
    "tip": "<strong>Para refletir:</strong> rebaixar a arte a 'matéria acessória' é descartar a principal escola de compreensão."
   },
   {
    "ic": "leaf",
    "t": "Prosa e Poesia da Existência",
    "b": "Viver não é só a <strong>prosa</strong> (o utilitário, a sobrevivência); é também a <strong>poesia</strong> (o amor, a comunhão, o êxtase, a festa). Aprender a viver inclui aprender a viver poeticamente. A eficiência sem poesia empobrece a existência que o ensino deveria nutrir.",
    "tip": "<strong>Modelo mental:</strong> pense no romance como simulador de vidas — experimenta-se a complexidade dos outros sem o risco real."
   }
  ]
 },
 "ch05-enfrentar-a-incerteza": {
  "cards": [
   {
    "ic": "wave",
    "t": "Ecologia da Ação",
    "b": "A ação, uma vez lançada, <strong>escapa às intenções</strong> — entra num jogo de interações que pode desviá-la ou invertê-la. Não 'errei ao agir', mas 'preciso monitorar e corrigir'. Lembre: você soltou um barco no rio; <strong>fique ao leme</strong>.",
    "tip": "<strong>Como aplicar:</strong> lançou uma ação? — lembre da ecologia da ação: ela escapa de você → monitore e corrija."
   },
   {
    "ic": "fork",
    "t": "Estratégia × Programa",
    "b": "<strong>Programa</strong>: sequência fixa — quebra ao primeiro imprevisto. <strong>Estratégia</strong>: rumo + correção — se adapta ao inesperado em vez de ser destruída. Em mundo instável: estratégia. A cabeça bem-feita prefere planos que se reformulam.",
    "tip": "<strong>Regra:</strong> ambiente pode mudar? → use estratégia, não programa. Rigidez = transformar imprevisto em fracasso."
   },
   {
    "ic": "mountain",
    "t": "A Aposta Consciente",
    "b": "Agir é <strong>apostar</strong> — assumir a decisão com consciência do risco e sem garantia. A história não é linear; avança por bifurcações, acasos e retrocessos. Educar é preparar para navegar, não para controlar.",
    "tip": "<strong>Para refletir:</strong> 'navegar por um oceano de incertezas por arquipélagos de certezas locais'."
   }
  ]
 },
 "ch06-a-aprendizagem-cidada": {
  "cards": [
   {
    "ic": "constellation",
    "t": "Terra-Pátria",
    "b": "Além da pátria nacional, existe a <strong>pátria comum — o planeta</strong>. A cidadania do século XXI é simultaneamente local, nacional e terrena. A crise climática regional é sempre nó da comunidade de destino — não 'problema de fora'.",
    "tip": "<strong>Como aplicar:</strong> pense a cidadania como anéis concêntricos: bairro → nação → Terra — nenhum anula o outro."
   },
   {
    "ic": "layers",
    "t": "Democracia Cognitiva",
    "b": "A democracia exige cidadãos capazes de <strong>compreender os problemas</strong> sobre os quais votam. Sem reforma do pensamento, os grandes problemas escapam ao cidadão e o poder migra para os 'experts'. <strong>Cabeça bem-feita é condição da democracia.</strong>",
    "tip": "<strong>Para refletir:</strong> 'isso é assunto de especialista, não opino' = déficit de democracia cognitiva."
   },
   {
    "ic": "link",
    "t": "Responsabilidade Planetária",
    "b": "A <strong>solidariedade e responsabilidade</strong> são enfraquecidas pela perda do global: 'cada um responde só pelo seu pedaço'. A comunidade de destino funda um vínculo que ultrapassa fronteiras — a mesma disjunção do saber, agora na ética cívica.",
    "tip": "<strong>Modelo mental:</strong> 'isso não é comigo' é responsabilidade fatiada — a mesma fragmentação do pensamento, agora em ação."
   }
  ]
 },
 "ch07-os-tres-graus": {
  "cards": [
   {
    "ic": "steps",
    "t": "Do Primário à Universidade",
    "b": "<strong>Primário</strong>: partir da curiosidade e do espanto, ligando saberes a perguntas vivas. <strong>Secundário</strong>: temas integradores que religam matérias (a condição humana, a era planetária). <strong>Universidade</strong>: conservar, transmitir e <strong>regenerar</strong> a cultura — abrir à transdisciplinaridade.",
    "tip": "<strong>Como aplicar:</strong> use temas integradores (Terra, humano, vida) — não matérias empilhadas."
   },
   {
    "ic": "link",
    "t": "Transdisciplinaridade",
    "b": "Não basta justapor disciplinas (multidisciplinar) nem fazê-las cooperar pontualmente (interdisciplinar). A <strong>transdisciplinaridade</strong> busca o que <em>atravessa, ultrapassa e religa</em> as disciplinas em torno de problemas e paradigmas comuns. Pense nas disciplinas como instrumentos de uma orquestra.",
    "tip": "<strong>Modelo mental:</strong> cada disciplina tem seu timbre — a música só existe quando tocam a mesma partitura (o problema comum)."
   },
   {
    "ic": "leaf",
    "t": "Ecologizar as Disciplinas",
    "b": "A disciplina é necessária (foca, aprofunda) mas vira <strong>prisão quando se fecha</strong>. 'Ecologizar': fazê-la dialogar no seu ambiente, abrir-se ao que a envolve. Não destruir a competência disciplinar — <strong>abri-la</strong> ao todo.",
    "tip": "<strong>Para refletir:</strong> disciplinas empilhadas sem religação continuam fragmentadas mesmo com novo nome."
   }
  ]
 },
 "ch08-a-reforma-do-pensamento": {
  "cards": [
   {
    "ic": "spiral",
    "t": "O Desafio dos Desafios",
    "b": "Nenhuma reforma de conteúdo resolve a fragmentação — é o <strong>paradigma</strong> (separar × religar) que precisa mudar. O pensamento dominante <strong>separa</strong> (disjunção) e <strong>reduz</strong> (simplificação). O paradigma da complexidade distingue sem isolar e religa sem fundir.",
    "tip": "<strong>Modelo mental:</strong> trocar a lente (de separar para religar) muda tudo que se vê — sem trocar nenhum conteúdo."
   },
   {
    "ic": "pivot",
    "t": "O Anel Pensamento ⇄ Ensino",
    "b": "'<strong>Reformar o pensamento para reformar o ensino — e reformar o ensino para reformar o pensamento.</strong>' É anel recursivo, não sequência. Sem reforma do pensamento, toda reforma de currículo é cosmética; com ela, até a velha grade se transforma.",
    "tip": "<strong>Para refletir:</strong> reforma só de grade, mesmo paradigma → nada muda no fundo. O professor religador transforma o conteúdo que encontra."
   },
   {
    "ic": "wrench",
    "t": "Princípios Organizadores",
    "b": "As ferramentas da religação: <strong>sistêmico</strong> (todo ≠ soma das partes) · <strong>hologramático</strong> (a parte no todo, o todo na parte) · <strong>retroativo</strong> (causa age sobre efeito e vice-versa) · <strong>recursivo</strong> (produto vira produtor) · <strong>dialógico</strong> (termos antagônicos que se completam).",
    "tip": "<strong>Como aplicar:</strong> dois termos se excluem? — aplique a dialógica: talvez ambos sejam necessários e complementares."
   }
  ]
 },
 "ch09-para-alem-das-contradicoes": {
  "cards": [
   {
    "ic": "spark",
    "t": "A Trindade do Ensino",
    "b": "O verdadeiro professor é animado por: <strong>Eros</strong> — o desejo e o amor pelo conhecimento e pelos alunos; <strong>missão</strong> — vocação que transcende a função técnica; <strong>fé</strong> — convicção na necessidade e possibilidade da reforma. Cada termo alimenta o outro.",
    "tip": "<strong>Termômetro:</strong> 'ainda tenho Eros nisto?' — sem desejo/missão/fé, o ensino vira rotina morta."
   },
   {
    "ic": "mountain",
    "t": "Começar pelas Margens",
    "b": "As grandes reformas não nascem do centro — nascem de <strong>focos marginais</strong> que se irradiam. A reforma do pensamento começará por uma minoria que a encarna. O paradoxo (mente ⇄ sociedade) só se rompe pela <strong>ação</strong>, não pela espera.",
    "tip": "<strong>Como aplicar:</strong> não espere decreto — comece pelas margens, por uma minoria que encarna a mudança."
   },
   {
    "ic": "leaf",
    "t": "Regenerar, Não Apenas Reformar",
    "b": "A missão é <strong>regeneradora</strong> — reanimar o ensino e o pensamento, devolver-lhes vida e sentido. A esperança não é ingenuidade: é a <strong>aposta consciente</strong> de quem inicia o anel. A reforma começa como faísca numa minoria e se alastra.",
    "tip": "<strong>Para refletir:</strong> o professor apaixonado contagia; o que perdeu o Eros apenas 'dá aula'. A diferença é toda."
   }
  ]
 }
}
```
