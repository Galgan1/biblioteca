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

# LIVRO PARA APROFUNDAR: Obrigado pelo Feedback — Douglas Stone & Sheila Heen

**Subtítulo:** VISÃO GERAL · A ARTE DE RECEBER BEM
**Ideia central:** Treinamos pessoas a dar feedback melhor — mas o ganho real está em receber. Douglas Stone e Sheila Heen revelam que quem recebe é o porteiro do que entra. Receber bem não é engolir tudo: é entender, e depois decidir. Receber ≠ aceitar.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-tres-tipos-de-feedback` — CAPÍTULO 1: Os Três Tipos de Feedback
- `ch02-tres-gatilhos` — CAPÍTULO 2: Os Três Gatilhos
- `ch03-de-certo-ou-errado-para-entender` — CAPÍTULO 3: Do 'Certo ou Errado' para 'Me Ajude a Entender'
- `ch04-pontos-cegos` — CAPÍTULO 4: Pontos Cegos
- `ch05-encontrar-o-certo-no-errado` — CAPÍTULO 5: Encontrar o Certo no Feedback Errado
- `ch06-gatilho-de-relacionamento` — CAPÍTULO 6: Separar o 'O Quê' do 'Quem'
- `ch07-sistema-entre-nos` — CAPÍTULO 7: O Sistema entre Nós
- `ch08-identidade-e-fiacao` — CAPÍTULO 8: Gatilhos de Identidade e a Fiação
- `ch09-limites-e-crescimento` — CAPÍTULO 9: Limites e Mentalidade de Crescimento

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-tres-tipos-de-feedback": {
  "cards": [
   {
    "ic": "fork",
    "t": "Apreciação / Orientação / Avaliação",
    "b": "<strong>Apreciação</strong>: ser visto e valorizado. <strong>Orientação</strong>: ajuda para crescer e melhorar. <strong>Avaliação</strong>: saber onde se está em relação a um padrão. Querer uma e receber outra gera frustração — mesmo que o feedback seja 'bom'.",
    "tip": "<strong>Como aplicar:</strong> 'Você quer desabafar, quer ajuda para melhorar ou quer saber como está indo?' — negocie o tipo explicitamente."
   },
   {
    "ic": "scale",
    "t": "A Avaliação Abafa",
    "b": "A avaliação tem peso emocional (status, segurança) e <strong>'grita' mais alto</strong> — impede a pessoa de ouvir a orientação que veio junto. Resolva a avaliação primeiro: ela precisa ser digerida antes que a orientação possa entrar.",
    "tip": "<strong>Modelo mental:</strong> pense no feedback como três alimentos diferentes — receber orientação quando queria apreciação é receber a coisa errada, não a ruim."
   },
   {
    "ic": "spark",
    "t": "Apreciação Eficaz",
    "b": "Apreciação não é elogio vazio ('bom trabalho!'). Para funcionar, precisa ser <strong>específica</strong> — fala do esforço ou do efeito real: 'Você percebeu que eu estava sobrecarregada e assumiu aquela tarefa sem que eu pedisse.' Genérica, soa como protocolo.",
    "tip": "<strong>Sinal de alerta:</strong> 'Eu dei apreciação' dito sobre um elogio genérico raramente satisfaz a necessidade de ser visto."
   }
  ]
 },
 "ch02-tres-gatilhos": {
  "cards": [
   {
    "ic": "triangle",
    "t": "Gatilho de Verdade",
    "b": "Reagimos ao <strong>conteúdo</strong>: o feedback parece errado, injusto, inútil ou off. 'Isso está equivocado.' O antídoto: trocar 'certo ou errado?' por 'o que ele vê que eu não vejo?' — curiosidade em vez de veredicto imediato.",
    "tip": "<strong>Como aplicar:</strong> ao pensar 'isso está errado', adie o veredito e pergunte: 'o que pode haver de certo aqui?'"
   },
   {
    "ic": "person",
    "t": "Gatilho de Relacionamento",
    "b": "Reagimos a <strong>quem deu</strong> ou <strong>como deu</strong>: 'Logo você vai me dizer isso?' Trocamos o assunto do feedback pela relação — o conteúdo se perde na queixa. A validade da mensagem não depende do mensageiro.",
    "tip": "<strong>Modelo mental:</strong> são dois tópicos: o feedback e a relação. Trate um de cada vez — senão nenhum é resolvido."
   },
   {
    "ic": "mask",
    "t": "Gatilho de Identidade",
    "b": "Reagimos ao que o feedback diz sobre <strong>quem somos</strong>: abala a autoimagem e dispara medo, vergonha ou sobrecarga. 'Eu sou um fracasso.' Gatilho ≠ feedback ruim — a força da reação não mede a gravidade do feedback.",
    "tip": "<strong>Sinal de alerta:</strong> generalizar o feedback para um rótulo total ('eu nunca consigo') é o gatilho de identidade em ação."
   }
  ]
 },
 "ch03-de-certo-ou-errado-para-entender": {
  "cards": [
   {
    "ic": "bulb",
    "t": "De Avaliação para Curiosidade",
    "b": "Troque 'isso é certo ou errado?' por '<strong>o que pode haver de certo nisso? o que ele percebe que eu não percebo?</strong>' Adie o veredito. Primeiro colete dados sobre o que o outro quis dizer.",
    "tip": "<strong>Como aplicar:</strong> ao sentir 'discordo', pause e pergunte: 'Me dá um exemplo de quando viu isso?'"
   },
   {
    "ic": "wrench",
    "t": "Desempacotar o Rótulo",
    "b": "Todo feedback chega vago: 'seja mais estratégico', 'tenha mais presença'. Cada rótulo esconde duas pontas: os <strong>dados</strong> (o que o outro observou) e o <strong>conselho</strong> (o que ele sugere). Sua tarefa: desempacotar as duas.",
    "tip": "<strong>Como aplicar:</strong> 'O que você quer dizer com isso?' + 'Me dá um exemplo?' — dois passos que transformam rótulo em dado acionável."
   },
   {
    "ic": "key",
    "t": "Entender não Obriga a Aceitar",
    "b": "Recusar-se a ouvir por medo de ser obrigado a concordar é a maior barreira ao aprendizado. <strong>Receber não obriga a aceitar</strong> — você pode ouvir com curiosidade e depois descartar conscientemente.",
    "tip": "<strong>Regra:</strong> achar a primeira coisa certa antes de catalogar o que está errado — é mais fácil aprender assim."
   }
  ]
 },
 "ch04-pontos-cegos": {
  "cards": [
   {
    "ic": "eye",
    "t": "Intenção × Impacto",
    "b": "Eu me julgo pela minha <strong>intenção</strong>; o outro me julga pelo meu <strong>impacto</strong>. Os dois são dados reais, mas diferentes. <strong>'Eu não quis' não cancela 'doeu'</strong>. Não use a boa intenção para anular o impacto relatado.",
    "tip": "<strong>Modelo mental:</strong> pense no feedback como um espelho da sua nuca — você nunca a viu, mas ela existe e os outros olham para ela o tempo todo."
   },
   {
    "ic": "gap",
    "t": "Leak Emocional",
    "b": "Suas emoções e padrões <strong>vazam sem você perceber</strong> — tom de voz, expressão, microcomportamentos. É justamente isso que o outro está vendo e relatando no feedback. O ponto cego mais comum é a emoção que você acha estar escondendo.",
    "tip": "<strong>Sinal de alerta:</strong> 'mas eu nem queria transmitir isso' — o outro reagiu ao seu impacto, não à sua intenção."
   },
   {
    "ic": "lens",
    "t": "Diferença de Mapas",
    "b": "Discordância raramente é má-fé — é <strong>mapas diferentes</strong>: dados e interpretações distintos. Separe dados (o que aconteceu) de interpretação (o significado dado). Pergunte de onde vêm os dados do outro.",
    "tip": "<strong>Como aplicar:</strong> 'O que você estava vendo quando chegou a essa conclusão?' — localiza a diferença de mapa sem acusar."
   }
  ]
 },
 "ch05-encontrar-o-certo-no-errado": {
  "cards": [
   {
    "ic": "bulb",
    "t": "Pedir Exemplos Concretos",
    "b": "Peça o caso específico que gerou o feedback: <strong>'Me dá um exemplo de uma vez em que viu isso?'</strong> + 'O que eu poderia ter feito diferente ali?' O exemplo transforma rótulo vago em observação verificável.",
    "tip": "<strong>Como aplicar:</strong> nunca concorde nem discorde de um rótulo sem antes mapear o caso concreto."
   },
   {
    "ic": "layers",
    "t": "Ver o Sistema, não só a Pessoa",
    "b": "Muito do 'feedback sobre você' é sobre a <strong>interação entre você e o outro</strong>, ou sobre papéis, processos e contexto. Dê 3 passos para trás: (1) a combinação você+outro, (2) papéis & cenário, (3) processos & incentivos.",
    "tip": "<strong>Modelo mental:</strong> 'dados → interpretação → conclusão' — discordâncias quase sempre estão na camada de dados ou de interpretação."
   },
   {
    "ic": "target",
    "t": "A Primeira Coisa Certa",
    "b": "Antes de listar tudo que está errado no feedback, encontre o <strong>1 ponto em que ele tem razão</strong>. Caçar erros para invalidar o feedback inteiro ('wrong-spotting') é a armadilha — você joga fora o grão de verdade junto com a palha.",
    "tip": "<strong>Sinal de alerta:</strong> 'mas ele está errado em X' não invalida Y. Separe o que está errado do que está certo."
   }
  ]
 },
 "ch06-gatilho-de-relacionamento": {
  "cards": [
   {
    "ic": "fork",
    "t": "Dois Trilhos, um de cada vez",
    "b": "Ao sentir o gatilho de relacionamento, identifique que há <strong>dois tópicos misturados</strong>: (1) o feedback em si e (2) algo na relação. Discuta os dois — mas um de cada vez: 'Há duas coisas aqui. Posso tratar do relatório agora e do segundo ponto depois?'",
    "tip": "<strong>Como aplicar:</strong> nomeie os dois trilhos em voz alta — isso já reduz a carga emocional e organiza a conversa."
   },
   {
    "ic": "spiral",
    "t": "Comutação de Trilhos (Switchtracking)",
    "b": "O padrão em que cada pessoa responde a um tópico diferente: A dá feedback sobre a tarefa; B responde com uma queixa sobre A. Os dois 'trocaram de trilho' e ninguém é ouvido. <strong>Nomeie a comutação</strong> e escolha qual trilho seguir primeiro.",
    "tip": "<strong>Modelo mental:</strong> dois trilhos de trem não se cruzam — misturá-los descarrilha os dois. Percorra um por vez."
   },
   {
    "ic": "key",
    "t": "Mensagem ≠ Mensageiro",
    "b": "A validade do conteúdo não depende de você gostar ou confiar em quem falou. O 'como' desajeitado é um segundo assunto legítimo — não é desculpa para ignorar o conteúdo. <strong>O feedback pode estar certo mesmo vindo de quem você não respeita.</strong>",
    "tip": "<strong>Sinal de alerta:</strong> 'você não tem moral para falar isso' — mesmo que verdadeiro, não responde ao conteúdo."
   }
  ]
 },
 "ch07-sistema-entre-nos": {
  "cards": [
   {
    "ic": "layers",
    "t": "3 Passos para Trás",
    "b": "<strong>(1) Você + outro</strong> (a combinação — a fricção nasce da diferença de estilos). <strong>(2) Papéis & cenário</strong> (o que parece traço pode ser a posição). <strong>(3) Processos, políticas & estruturas</strong> (incentivos que empurram o comportamento).",
    "tip": "<strong>Como aplicar:</strong> 'Quanto disto é meu, quanto é nosso, quanto é do sistema?' — tripé de diagnóstico antes de qualquer conclusão."
   },
   {
    "ic": "scale",
    "t": "Contribuição × Culpa",
    "b": "<strong>Culpa</strong> é retrospectiva, moral, busca um réu. <strong>Contribuição</strong> é sistêmica, voltada a consertar. Trocar 'de quem é a culpa?' por 'como cada parte contribuiu?' abre a possibilidade de correção sem paralisar ninguém na defensiva.",
    "tip": "<strong>Modelo mental:</strong> contribuição mapeia todas as partes; culpa congela todas na defensiva."
   },
   {
    "ic": "person",
    "t": "A Combinação",
    "b": "O atrito que só existe entre <em>este</em> você e <em>este</em> outro — invisível se olhar um isolado. <strong>Diferença não é defeito</strong>: leia 'ele é desorganizado' e pergunte se não é apenas 'temos estilos diferentes'. A combinação é a alavanca invisível.",
    "tip": "<strong>Sinal de alerta:</strong> 'diluir sua parte no sistema' como desculpa para não mudar nada seu é o outro extremo — ver o sistema não isenta sua parte."
   }
  ]
 },
 "ch08-identidade-e-fiacao": {
  "cards": [
   {
    "ic": "wave",
    "t": "A Fiação (Baseline · Swing · Recuperação)",
    "b": "Três variáveis que definem quanto o feedback abala: <strong>Baseline</strong> (nível habitual de bem-estar), <strong>Swing</strong> (amplitude de reação), <strong>Recuperação</strong> (tempo para voltar ao baseline). Saber a própria fiação evita confundir a intensidade da reação com a gravidade do feedback.",
    "tip": "<strong>Modelo mental:</strong> a fiação é o 'volume' e o 'eco' do seu alarme — pessoas diferentes têm volumes e ecos diferentes para o mesmo estímulo."
   },
   {
    "ic": "layers",
    "t": "Identidade Complexa × Fixa",
    "b": "Identidade fixa (rótulo tudo-ou-nada): 'sou competente / sou um fracasso' — desaba com qualquer crítica. <strong>Identidade complexa</strong>: 'eu cometo erros + minhas intenções são complexas + eu contribuo para os problemas'. Absorve o feedback como informação, não como veredito.",
    "tip": "<strong>Como aplicar:</strong> quando um feedback ameaça derrubar sua autoimagem, acione as três realidades — erro, intenção complexa, contribuição."
   },
   {
    "ic": "mask",
    "t": "As 3 Distorções",
    "b": "Amplificações automáticas que fazem um feedback pequeno parecer um ataque total: <strong>catastrofizar</strong> ('vai arruinar tudo'), <strong>generalizar</strong> ('eu sempre erro'), <strong>eternizar</strong> ('nunca vou mudar'). Reconhecê-las já as parcialmente desarma.",
    "tip": "<strong>Sinal de alerta:</strong> 'isso prova que eu sempre X' — a palavra 'sempre' quase sempre é uma distorção do gatilho de identidade."
   }
  ]
 },
 "ch09-limites-e-crescimento": {
  "cards": [
   {
    "ic": "leaf",
    "t": "Mentalidade Fluida (de Crescimento)",
    "b": "Quem tem identidade fixa ouve feedback como veredito sobre traços imutáveis. Quem tem identidade de crescimento ouve como <strong>informação sobre algo treinável</strong>. Foque a energia no coaching ('como melhorar'), não só na avaliação ('onde estou').",
    "tip": "<strong>Modelo mental:</strong> você é o porteiro do próprio feedback: pode receber todos os recados e decidir quais entram em ação."
   },
   {
    "ic": "scale",
    "t": "Os 3 Limites Legítimos",
    "b": "<strong>'Não, obrigado'</strong> — ouço, mas sigo do meu jeito. <strong>'Não agora/assim'</strong> — o conteúdo pode ser válido, mas renegocio quando/como. <strong>'Pare'</strong> — feedback persistente que corrói a relação ou a saúde. Diga com cuidado pela relação — limite ao feedback ≠ fechar a porta à pessoa.",
    "tip": "<strong>Como aplicar:</strong> 'Eu te ouvi. Por ora vou seguir do meu jeito.' — dito com clareza e cuidado, é um limite saudável, não defensividade."
   },
   {
    "ic": "key",
    "t": "Você é o Porteiro",
    "b": "<strong>Receber bem = aceitar tudo</strong> é a falácia que transforma bom recebedor em capacho. Você é o dono da decisão final sobre o que fazer com o feedback. <strong>Ouvir é generosidade; decidir é seu direito.</strong> Experimente em escala pequena se não tiver certeza.",
    "tip": "<strong>Sinal de alerta:</strong> 'cortar a relação para se livrar do feedback' — pular de 'não a este feedback' para 'não a esta pessoa' é o limite mal-aplicado."
   }
  ]
 }
}
```
