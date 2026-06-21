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

# LIVRO PARA APROFUNDAR: Garra — Angela Duckworth

**Subtítulo:** VISÃO GERAL · O PODER DA PAIXÃO E DA PERSEVERANÇA
**Ideia central:** O que separa quem realiza grandes coisas não é o talento — é a garra: paixão (um interesse de longo prazo, constante) somada à perseverança (não desistir diante dos reveses). Duckworth mostra que o talento não é destino: o esforço 'conta duas vezes', e a garra cresce de dentro (interesse, prática, propósito, esperança) e de fora (pais, treinadores, cultura).

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-o-que-e-garra` — CAPÍTULO 1: O que é Garra
- `ch02-talento-nao-e-destino` — CAPÍTULO 2: O Talento não é Destino
- `ch03-as-duas-equacoes-do-esforco` — CAPÍTULO 3: As Duas Equações do Esforço
- `ch04-interesse` — CAPÍTULO 4: Interesse
- `ch05-pratica-deliberada` — CAPÍTULO 5: Prática Deliberada
- `ch06-proposito-e-esperanca` — CAPÍTULO 6: Propósito e Esperança
- `ch07-cultivar-de-fora` — CAPÍTULO 7: Cultivar a Garra de Fora

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-o-que-e-garra": {
  "cards": [
   {
    "ic": "spark",
    "t": "Garra = Paixão + Perseverança",
    "b": "<strong>Paixão</strong> é constância de direção — perseguir o mesmo objetivo de topo por anos, <em>não</em> fervor momentâneo. <strong>Perseverança</strong> é continuar apesar de fracassos, tédio e platôs. Garra é a soma das duas, no longo prazo.",
    "tip": "<strong>Como aplicar:</strong> pergunte de um objetivo — 'ainda estou nele há anos?'. Paixão é constância, não calor."
   },
   {
    "ic": "target",
    "t": "A Escala de Garra",
    "b": "A <strong>Grit Scale</strong> mede paixão + perseverança. Pontuação alta previu quem persiste onde o talento não previu: cadetes que aguentam West Point, finalistas de soletração, vendedores que não largam.",
    "tip": "<strong>Modelo mental:</strong> em tarefas longas, otimize primeiro para <em>não desistir</em>; brilhar vem depois."
   },
   {
    "ic": "mountain",
    "t": "Maratona, não Sprint",
    "b": "Intensidade é fácil e barata; <strong>garra é o compromisso que dura</strong> quando a empolgação some. Em muitos contextos, a maior parte do sucesso é simplesmente não sair antes da hora.",
    "tip": "<strong>Para refletir:</strong> quem fica vence — boa parte do êxito é resistência, não talento."
   }
  ]
 },
 "ch02-talento-nao-e-destino": {
  "cards": [
   {
    "ic": "lens",
    "t": "Viés Contra o Esforço",
    "b": "Dizemos admirar quem se esforça, mas, na prática, preferimos o '<strong>talento natural</strong>' e o julgamos mais capaz. Esconder o suor faz o feito parecer mágica — e recompensamos a mágica.",
    "tip": "<strong>Modelo mental:</strong> por trás do 'ele nasceu para isso' quase sempre há milhares de horas escondidas."
   },
   {
    "ic": "bulb",
    "t": "O Mito do Gênio",
    "b": "Chamar alguém de '<strong>gênio</strong>' o põe num pedestal que nos isenta de tentar — é desculpa para não nos esforçarmos. Sem trabalho, talento é só <em>potencial não realizado</em>.",
    "tip": "<strong>Para refletir:</strong> suspeite da palavra 'gênio' — ela costuma apagar o trabalho que explica o feito."
   },
   {
    "ic": "steps",
    "t": "Talento = Velocidade, não Teto",
    "b": "Talento é a <strong>rapidez</strong> com que se aprende; não diz onde se chega. A linha de chegada depende do esforço. Largar na frente não decide a corrida longa.",
    "tip": "<strong>Como aplicar:</strong> trate o talento como dado inicial e o esforço como a variável sob seu controle."
   }
  ]
 },
 "ch03-as-duas-equacoes-do-esforco": {
  "cards": [
   {
    "ic": "scale",
    "t": "O Esforço Conta Duas Vezes",
    "b": "<strong>Talento × Esforço = Habilidade</strong>. <strong>Habilidade × Esforço = Realização</strong>. O esforço aparece nas duas linhas; o talento, só na primeira. Dobrar o esforço cresce a realização mais do que dobrar o talento.",
    "tip": "<strong>Como aplicar:</strong> ao decidir onde investir energia, lembre que o esforço compõe em dois níveis."
   },
   {
    "ic": "layers",
    "t": "Hierarquia de Objetivos",
    "b": "Uma pirâmide: muitos <strong>objetivos-meio</strong> (táticas) servem a poucos de médio nível, todos a <strong>um único objetivo de topo</strong> (a paixão). Pessoas com garra têm um topo claro e duradouro ao qual quase tudo se subordina.",
    "tip": "<strong>Como aplicar:</strong> para cada meta, pergunte 'para quê isto?' (sobe) e 'como faço?' (desce)."
   },
   {
    "ic": "key",
    "t": "Firme no Topo, Flexível Embaixo",
    "b": "Largar uma tática ou um meio que falhou é <strong>saudável</strong>; largar o objetivo de topo no primeiro revés é falta de garra. Troque o 'como', raramente o 'fim'.",
    "tip": "<strong>Regra:</strong> quando algo falhar, mude o meio — não a paixão."
   }
  ]
 },
 "ch04-interesse": {
  "cards": [
   {
    "ic": "spark",
    "t": "O Paradoxo da Paixão",
    "b": "Esperamos a paixão '<strong>pronta</strong>' antes de nos comprometer — mas o interesse só se aprofunda <em>com</em> a prática, não antes. Quem trata 'siga sua paixão' como certeza prévia fica paralisado.",
    "tip": "<strong>Para refletir:</strong> paixão é cozida em fogo brando — algo a desenvolver, não a encontrar de pronto."
   },
   {
    "ic": "lens",
    "t": "Descobrir → Desenvolver → Aprofundar",
    "b": "O interesse nasce de <strong>experimentar muito</strong> (descobrir), cresce com <strong>engajamento repetido</strong> (desenvolver) e dura por <strong>anos de novidade no mesmo campo</strong> (aprofundar). Especialistas acham o campo cada vez mais fascinante.",
    "tip": "<strong>Como aplicar:</strong> experimente muito e dê tempo de aprofundar antes de julgar."
   },
   {
    "ic": "person",
    "t": "O Papel do Encorajamento",
    "b": "Interesses brotam quando há <strong>liberdade para explorar</strong> e alguém que apoia o início. A fase de diversão (play) precede a fase de disciplina — não o contrário.",
    "tip": "<strong>Para refletir:</strong> não espere fogos de artifício no começo — o interesse cresce com a exposição."
   }
  ]
 },
 "ch05-pratica-deliberada": {
  "cards": [
   {
    "ic": "target",
    "t": "Os 4 Requisitos da Prática Deliberada",
    "b": "<strong>Meta de stretch</strong> (alvo um pouco além do atual) → <strong>foco total</strong> → <strong>feedback imediato</strong> (sobretudo do erro) → <strong>repetição com refinamento</strong>. Exigente, não prazerosa no momento.",
    "tip": "<strong>Como aplicar:</strong> caçar o ponto fraco; praticar o que já é fácil não desenvolve ninguém."
   },
   {
    "ic": "wave",
    "t": "Prática Deliberada × Flow",
    "b": "<strong>Prática deliberada</strong> = esforço na <em>preparação</em> (suor). <strong>Flow</strong> = absorção sem esforço na <em>performance</em> (prazer). Não competem: pratica-se com suor para depois fluir.",
    "tip": "<strong>Modelo mental:</strong> suar no treino para fluir na hora — as duas, em momentos diferentes."
   },
   {
    "ic": "steps",
    "t": "Vire Hábito",
    "b": "A prática deliberada é desconfortável; transformá-la em <strong>rotina</strong> (mesmo horário e lugar) reduz o atrito de começar. 'Horas de voo' sem foco nem feedback não viram maestria.",
    "tip": "<strong>Para refletir:</strong> aceite o desconforto como sinal de que está aprendendo, não falhando."
   }
  ]
 },
 "ch06-proposito-e-esperanca": {
  "cards": [
   {
    "ic": "constellation",
    "t": "Propósito: Servir aos Outros",
    "b": "O interesse pessoal inicia a paixão; o <strong>propósito</strong> a torna duradoura. Os mais gritty veem o trabalho como <strong>importante para o mundo</strong>. Parábola dos pedreiros: 'ponho tijolos' × '<em>construo uma catedral</em>'.",
    "tip": "<strong>Como aplicar:</strong> pergunte 'para quem?' — ligar o trabalho a um beneficiário transforma tarefa em missão."
   },
   {
    "ic": "leaf",
    "t": "Esperança = Crescimento + Otimismo",
    "b": "A esperança da garra não é 'tomara que dê certo'; é '<strong>eu posso melhorar isto</strong>'. Apoia-se na <strong>mentalidade de crescimento</strong> (habilidade é maleável) e no <strong>otimismo</strong> (reveses são temporários e específicos).",
    "tip": "<strong>Como aplicar:</strong> ao falhar, troque 'sou incapaz' por 'ainda não consegui'."
   },
   {
    "ic": "mountain",
    "t": "Anti-Desamparo: Reescreva o Revés",
    "b": "O oposto da esperança é o <strong>desamparo aprendido</strong> ('nada que eu faça adianta'). A diferença não é o revés, é a <strong>interpretação</strong>: explique-o como temporário e específico, e aja sobre a causa.",
    "tip": "<strong>Síntese:</strong> cair sete vezes, levantar oito (Nana korobi ya oki)."
   }
  ]
 },
 "ch07-cultivar-de-fora": {
  "cards": [
   {
    "ic": "person",
    "t": "Parenting Sábio: Exigente E Acolhedor",
    "b": "O estilo que mais gera garra é <strong>autoritativo</strong>: pede muito <em>e</em> apoia muito. Os outros falham — autoritário (exige, não acolhe), permissivo (acolhe, não exige), negligente (nenhum). Vale para qualquer mentor ou chefe.",
    "tip": "<strong>Regra:</strong> padrões sem calor viram tirania; calor sem padrões vira moleza — precisa dos dois."
   },
   {
    "ic": "target",
    "t": "A Regra do Difícil",
    "b": "A prática da família Duckworth: (1) <strong>todos</strong> praticam algo difícil; (2) <strong>não se desiste num dia ruim</strong> — só ao fim do período combinado; (3) <strong>você escolhe</strong> a coisa difícil. Ensina que reveses fazem parte.",
    "tip": "<strong>Como aplicar:</strong> escolha uma coisa difícil, comprometa-se até o fim da temporada e não largue no meio."
   },
   {
    "ic": "constellation",
    "t": "Cultura de Garra",
    "b": "A forma mais forte de ganhar garra é <strong>pertencer a um grupo cheio dela</strong>. Adotamos a <em>identidade</em> do grupo ('aqui a gente termina o que começa'), não só os comportamentos. Garra por contágio.",
    "tip": "<strong>Modelo mental:</strong> escolha a tribo — a cultura faz o que a força de vontade sozinha não faz."
   }
  ]
 }
}
```
