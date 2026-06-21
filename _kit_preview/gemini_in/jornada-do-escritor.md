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

# LIVRO PARA APROFUNDAR: A Jornada do Escritor — Christopher Vogler

**Subtítulo:** VISÃO GERAL · A ESTRUTURA MÍTICA PARA ROTEIRISTAS
**Ideia central:** Christopher Vogler traduziu o monomito de Joseph Campbell para a linguagem do roteiro. Sob a infinita variedade das histórias, há um único padrão — a Jornada do Herói — porque ele descreve a forma da transformação humana. Vogler organiza esse padrão em 12 estágios e 8 arquétipos, ferramentas para escrever (e diagnosticar) qualquer narrativa, do mito épico ao drama doméstico.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-monomito-arquetipos` — CAPÍTULO 1: O Monomito e os Arquétipos
- `ch02-mundo-comum-chamado` — CAPÍTULO 2: Mundo Comum e o Chamado à Aventura
- `ch03-recusa-mentor` — CAPÍTULO 3: Recusa do Chamado e o Encontro com o Mentor
- `ch04-travessia-limiar` — CAPÍTULO 4: A Travessia do Primeiro Limiar
- `ch05-provas-aliados-inimigos` — CAPÍTULO 5: Provas, Aliados e Inimigos
- `ch06-aproximacao-provacao` — CAPÍTULO 6: Aproximação e a Provação
- `ch07-recompensa` — CAPÍTULO 7: A Recompensa (Apoderar-se da Espada)
- `ch08-caminho-de-volta` — CAPÍTULO 8: O Caminho de Volta
- `ch09-ressurreicao` — CAPÍTULO 9: A Ressurreição
- `ch10-retorno-com-elixir` — CAPÍTULO 10: O Retorno com o Elixir

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-monomito-arquetipos": {
  "cards": [
   {
    "ic": "spiral",
    "t": "O Monomito",
    "b": "Um herói parte do mundo conhecido, atravessa um limiar, enfrenta provações e uma <strong>crise de morte/renascimento</strong>, conquista uma recompensa e retorna transformado, trazendo algo que beneficia os outros.",
    "tip": "<strong>Como aplicar:</strong> o mundo externo da jornada espelha o conflito interno do herói."
   },
   {
    "ic": "layers",
    "t": "Arquétipo = Função",
    "b": "Cada arquétipo é um <strong>papel que a narrativa precisa</strong> — uma energia psicológica —, não um personagem fixo. Personagens são máscaras que esses arquétipos vestem.",
    "tip": "<strong>Modelo mental:</strong> um personagem pode trocar de máscara ao longo do arco."
   },
   {
    "ic": "eye",
    "t": "Bússola, Não Trilho",
    "b": "A estrutura pode ser comprimida, reordenada, repetida ou subvertida sem perder o efeito. Tratá-la como <strong>checklist rígido</strong> mata o orgânico.",
    "tip": "<strong>Cuidado:</strong> arquétipo como estereótipo (\"o velho sábio barbudo\") engessa o elenco."
   }
  ]
 },
 "ch02-mundo-comum-chamado": {
  "cards": [
   {
    "ic": "book",
    "t": "Mundo Comum",
    "b": "A linha de base contra a qual mediremos a transformação. Mostre a rotina, a falha e a <strong>ferida</strong> que a aventura virá desafiar ou curar.",
    "tip": "<strong>Como aplicar:</strong> você só sente a viagem se viu a casa."
   },
   {
    "ic": "wave",
    "t": "O Chamado",
    "b": "A perturbação que apresenta o problema ou desafio e <strong>encerra a possibilidade</strong> de seguir como antes. Fecha a porta de trás.",
    "tip": "<strong>Modelo mental:</strong> um evento que o herói pode ignorar sem custo não é chamado, é convite."
   },
   {
    "ic": "target",
    "t": "O Arauto",
    "b": "A força que entrega o Chamado — pessoa, notícia ou mudança de circunstância. <strong>Anuncia que a mudança chegou.</strong>",
    "tip": "<strong>Cuidado:</strong> Mundo Comum longo demais faz o público embarcar tarde."
   }
  ]
 },
 "ch03-recusa-mentor": {
  "cards": [
   {
    "ic": "clock",
    "t": "A Recusa",
    "b": "A manifestação do medo: o herói recua, ou alguém alerta do perigo. <strong>Ninguém hesita diante do que é fácil</strong> — a Recusa prova que a aposta é real.",
    "tip": "<strong>Como aplicar:</strong> coragem só existe contra o medo."
   },
   {
    "ic": "key",
    "t": "O Mentor",
    "b": "A fonte de <strong>sabedoria, treino ou dom</strong> que arma o herói para o limiar. Representa o eu superior — e depois se retira.",
    "tip": "<strong>Modelo mental:</strong> o Mentor abre a porta; quem atravessa é o herói."
   },
   {
    "ic": "eye",
    "t": "Mentor Onipotente",
    "b": "Se o Mentor pode resolver, por que o herói? <strong>O dom é meio, não substituto da ação.</strong>",
    "tip": "<strong>Cuidado:</strong> mentor que resolve tudo rouba o arco do protagonista."
   }
  ]
 },
 "ch04-travessia-limiar": {
  "cards": [
   {
    "ic": "steps",
    "t": "O Comprometimento",
    "b": "O herói entra no desconhecido por vontade própria, aceitando suas regras e perigos. Depois do limiar, <strong>o mundo antigo se fecha</strong>.",
    "tip": "<strong>Como aplicar:</strong> cruzar o limiar é assinar o contrato da aventura."
   },
   {
    "ic": "gap",
    "t": "O Guardião do Limiar",
    "b": "A força que bloqueia a passagem e <strong>testa o comprometimento</strong>. Não é o vilão final — é o filtro de quem não está pronto.",
    "tip": "<strong>Modelo mental:</strong> guardiões não são para derrotar, e sim para passar (vencer, contornar ou converter)."
   },
   {
    "ic": "eye",
    "t": "Limiar Morno",
    "b": "Passagem sem peso nem risco <strong>não sinaliza o ponto sem retorno</strong>. E herói sempre empurrado segue passivo no Ato 2.",
    "tip": "<strong>Cuidado:</strong> tratar o Guardião como batalha final gasta o clímax cedo."
   }
  ]
 },
 "ch05-provas-aliados-inimigos": {
  "cards": [
   {
    "ic": "target",
    "t": "Provas",
    "b": "Desafios menores que <strong>treinam o herói</strong>, revelam seu caráter e elevam as estacas. São o aquecimento para a Provação.",
    "tip": "<strong>Como aplicar:</strong> o meio do Ato 2 é uma escola; cada prova é uma aula com nota."
   },
   {
    "ic": "layers",
    "t": "Aliados e a Sombra",
    "b": "O herói descobre em quem confiar (<strong>Aliado</strong>) e quem temer (<strong>Sombra</strong>, a oposição). O Camaleão semeia dúvida; o Pícaro alivia a tensão.",
    "tip": "<strong>Modelo mental:</strong> a melhor Sombra é um espelho — mostra o que o herói poderia se tornar."
   },
   {
    "ic": "eye",
    "t": "Provas Avulsas",
    "b": "Desafios que <strong>não escalam nem ensinam</strong> viram enchimento; aliados sem função tornam o time decorativo.",
    "tip": "<strong>Cuidado:</strong> inimigo sem relação com a falha do herói desperdiça o tema."
   }
  ]
 },
 "ch06-aproximacao-provacao": {
  "cards": [
   {
    "ic": "spiral",
    "t": "A Provação",
    "b": "O ponto médio dramático, o confronto supremo. O herói <strong>toca o fundo</strong>, encara seu maior medo e parece morrer — para então renascer. É a fonte da magia da história.",
    "tip": "<strong>Como aplicar:</strong> sem morte, sem ressurreição — algo no herói precisa acabar."
   },
   {
    "ic": "key",
    "t": "Morte e Renascimento",
    "b": "O herói experimenta uma <strong>morte simbólica</strong> (perda, fracasso, escuridão) e emerge transformado. O público morre e ressuscita com ele.",
    "tip": "<strong>Modelo mental:</strong> a Provação é o centro de gravidade — tudo antes prepara, tudo depois decorre."
   },
   {
    "ic": "eye",
    "t": "Provação Sem Risco",
    "b": "Se o público nunca teme a derrota, o <strong>renascimento não emociona</strong>. Vencer fácil esvazia o arco inteiro.",
    "tip": "<strong>Cuidado:</strong> derrotar o inimigo sem nada mudar por dentro é ação sem transformação."
   }
  ]
 },
 "ch07-recompensa": {
  "cards": [
   {
    "ic": "target",
    "t": "Apoderar-se da Espada",
    "b": "O herói toma posse do que buscava — literal (tesouro, arma) ou interno (autoconhecimento, perdão, amor). <strong>Conquista-se algo por ter enfrentado a morte.</strong>",
    "tip": "<strong>Como aplicar:</strong> a espada é ganha, não dada; o que vem fácil não é recompensa."
   },
   {
    "ic": "clock",
    "t": "A Falsa Paz",
    "b": "A calmaria pós-Provação: celebração, intimidade, vanglória — e a <strong>ilusão de que a história terminou</strong>. O autor usa o respiro para preparar a virada.",
    "tip": "<strong>Modelo mental:</strong> cuidado com o final que parece chegar cedo."
   },
   {
    "ic": "eye",
    "t": "Parar na Celebração",
    "b": "Tratar a Recompensa como desfecho deixa a jornada pela metade — <strong>falta o retorno</strong>.",
    "tip": "<strong>Cuidado:</strong> herói que toma o prêmio igual a quem entrou anula a Provação."
   }
  ]
 },
 "ch08-caminho-de-volta": {
  "cards": [
   {
    "ic": "steps",
    "t": "O Caminho de Volta",
    "b": "O herói decide retornar e completar a missão; muitas vezes começa com uma <strong>perseguição</strong> — a Sombra contra-ataca, as escolhas cobram seu preço.",
    "tip": "<strong>Como aplicar:</strong> sair do Mundo Especial é tão difícil quanto entrar."
   },
   {
    "ic": "key",
    "t": "O Recomprometimento",
    "b": "Depois da falsa paz, o herói <strong>reassume o propósito</strong>, agora ciente do custo. É a 'segunda virada de ato'.",
    "tip": "<strong>Modelo mental:</strong> a escolha de voltar e terminar prova que a transformação pegou."
   },
   {
    "ic": "eye",
    "t": "Retorno Sem Atrito",
    "b": "Voltar sem perseguição nem custo <strong>esvazia o terceiro ato</strong>; herói arrastado de volta perde o protagonismo na reta final.",
    "tip": "<strong>Cuidado:</strong> não deixe a história desinflar entre a Recompensa e o clímax."
   }
  ]
 },
 "ch09-ressurreicao": {
  "cards": [
   {
    "ic": "spiral",
    "t": "A Ressurreição",
    "b": "O confronto culminante, <strong>mais alto que a Provação</strong>. O herói é testado com tudo em jogo e renasce purificado, dominando a lição que antes só vislumbrara.",
    "tip": "<strong>Como aplicar:</strong> é o exame final — a Provação foi a aula, aqui ele prova que aprendeu."
   },
   {
    "ic": "target",
    "t": "A Prova da Mudança",
    "b": "O herói <strong>age como o novo eu sob pressão máxima</strong> — não basta dizer que mudou. Reúne tudo (dom, lições, aliados) num ato final.",
    "tip": "<strong>Modelo mental:</strong> mudança se mostra em ação, sob fogo, não narrada."
   },
   {
    "ic": "sword",
    "t": "Resolução por Terceiros",
    "b": "Se outro salva o dia, o herói <strong>não ressuscita</strong> (deus ex machina). E clímax menor que a Provação é anticlímax.",
    "tip": "<strong>Cuidado:</strong> deve ser o próprio herói a vencer o clímax."
   }
  ]
 },
 "ch10-retorno-com-elixir": {
  "cards": [
   {
    "ic": "key",
    "t": "O Elixir",
    "b": "O herói volta transformado e traz um <strong>benefício para a comunidade</strong>: tesouro, amor, sabedoria, liberdade, cura. Concreto ou intangível.",
    "tip": "<strong>Como aplicar:</strong> a marca da jornada bem-sucedida é que o ganho do herói cura também os outros."
   },
   {
    "ic": "spiral",
    "t": "O Círculo Fechado",
    "b": "A Imagem do Mundo Comum retorna, agora <strong>curada pela presença do herói mudado</strong> — o 'depois' que dá sentido ao 'antes'. A última imagem responde à primeira.",
    "tip": "<strong>Modelo mental:</strong> transformação que não volta para casa é incompleta."
   },
   {
    "ic": "eye",
    "t": "Voltar de Mãos Vazias",
    "b": "Sem Elixir, a aventura <strong>não significou nada</strong> para o mundo; o herói que guarda tudo para si frustra a função social do mito.",
    "tip": "<strong>Cuidado:</strong> terminar no Mundo Especial deixa o público sem catarse."
   }
  ]
 }
}
```
