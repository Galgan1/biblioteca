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

# LIVRO PARA APROFUNDAR: Os Sete Saberes Necessários à Educação do Futuro — Edgar Morin

**Subtítulo:** VISÃO GERAL · OS BURACOS QUE A EDUCAÇÃO IGNORA
**Ideia central:** Há sete saberes fundamentais que o ensino, em qualquer cultura ou época, ignora ou trata mal — e que são vitais para formar mentes capazes de enfrentar a complexidade do mundo. Morin os apresenta como bússola: não um currículo, mas os sete buracos a tapar para que o pensamento volte a religar o que foi separado.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-cegueiras-do-conhecimento` — SABER 1: As Cegueiras do Conhecimento
- `ch02-conhecimento-pertinente` — SABER 2: O Conhecimento Pertinente
- `ch03-condicao-humana` — SABER 3: Ensinar a Condição Humana
- `ch04-identidade-terrena` — SABER 4: Ensinar a Identidade Terrena
- `ch05-enfrentar-as-incertezas` — SABER 5: Enfrentar as Incertezas
- `ch06-ensinar-a-compreensao` — SABER 6: Ensinar a Compreensão
- `ch07-antropoetica` — SABER 7: A Antropoética

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-cegueiras-do-conhecimento": {
  "cards": [
   {
    "ic": "eye",
    "t": "O Erro é Estrutural",
    "b": "O erro não é só falha externa (dados ruins); nasce da própria tradução <strong>cérebro → mente → cultura</strong>. Conhecer já é interpretar — e interpretar já é arriscar-se a errar. Quatro focos: erros mentais, intelectuais, da razão e cegueiras paradigmáticas.",
    "tip": "<strong>Como aplicar:</strong> antes de confiar num saber, audite seu erro/ilusão possível e o paradigma que o gerou."
   },
   {
    "ic": "lens",
    "t": "Racionalidade × Racionalização",
    "b": "<strong>Racionalidade</strong>: sistema aberto, dialoga com o real e se corrige. <strong>Racionalização</strong>: sistema fechado, expulsa o que o contradiz — se disfarça de 'ser racional'. A mesma lógica; sinais opostos.",
    "tip": "<strong>Sinal de alerta:</strong> quando uma ideia rejeita todo fato que a contraria, é racionalização, não racionalidade."
   },
   {
    "ic": "triangle",
    "t": "O Paradigma Invisível",
    "b": "O paradigma decide, <strong>por baixo do consciente</strong>, o que é pensável e o que é impensável. A cegueira mais perigosa: a que se sente como certeza evidente. Procure o paradigma, não só o argumento.",
    "tip": "<strong>Para refletir:</strong> 'isso é óbvio' é o sinal mais confiável de que um paradigma está operando sem ser visto."
   }
  ]
 },
 "ch02-conhecimento-pertinente": {
  "cards": [
   {
    "ic": "layers",
    "t": "Os 4 Traços do Saber Pertinente",
    "b": "<strong>Contexto</strong> (informação isolada = ruído) · <strong>Global</strong> (o todo é mais que a soma das partes) · <strong>Multidimensional</strong> (o real é ao mesmo tempo econômico, psíquico, biológico, social) · <strong>Complexo</strong> (o que é tecido junto). Faltou um → conhecimento parcelado.",
    "tip": "<strong>Como aplicar:</strong> diante de qualquer problema real, marque os 4 antes de analisar."
   },
   {
    "ic": "spiral",
    "t": "Inteligência Geral",
    "b": "A aptidão de <strong>religar e contextualizar</strong> é mais fundamental que qualquer competência especializada — e a que a escola menos cultiva. A hiperespecialização vê o fio e perde o tecido; a inteligência geral vê o tecido.",
    "tip": "<strong>Modelo mental:</strong> use a especialização como ferramenta, não como teto — útil para aprofundar, perigosa como única lente."
   },
   {
    "ic": "fork",
    "t": "Disjunção e Redução",
    "b": "Os dois vícios do pensamento dominante: <strong>disjunção</strong> (separar o que está ligado) e <strong>redução</strong> (reduzir o múltiplo a uma causa). Resultado: exatidão local + cegueira do conjunto. A cura não é mais conteúdo, mas religar.",
    "tip": "<strong>Para refletir:</strong> quando a explicação cabe em uma só causa ou disciplina, suspeite — o real raramente é assim."
   }
  ]
 },
 "ch03-condicao-humana": {
  "cards": [
   {
    "ic": "person",
    "t": "Unitas Multiplex",
    "b": "A humanidade é <strong>UNA</strong> (mesma espécie, mesma condição) e <strong>MÚLTIPLA</strong> (línguas, culturas, indivíduos irrepetíveis) — as duas ao mesmo tempo, sem dissolver uma na outra. Recuse tanto o universalismo abstrato que apaga quanto o relativismo que separa.",
    "tip": "<strong>Modelo mental:</strong> o diferente é uma variação da mesma condição que é a sua."
   },
   {
    "ic": "spiral",
    "t": "A Tríade Recursiva",
    "b": "<strong>Indivíduo ⇄ Sociedade ⇄ Espécie</strong>: nenhum é primeiro; cada um produz e é produzido pelos outros. O mesmo anel interno: <strong>cérebro ⇄ mente ⇄ cultura</strong> — sem cérebro não há mente, sem cultura não há mente humana.",
    "tip": "<strong>Como aplicar:</strong> diante de conflito cultural, busque a terceira via: reconhecer a mesma condição humana sob a diversidade."
   },
   {
    "ic": "masks",
    "t": "Homo Complexus",
    "b": "Somos <em>sapiens</em> <strong>e</strong> <em>demens</em> (sábio e louco), <em>faber</em> <strong>e</strong> <em>ludens</em> (operário e brincalhão), prosaico e poético — a contradição é constitutiva, não defeito. Reduzir o humano a uma só dimensão mutila.",
    "tip": "<strong>Para refletir:</strong> use 'e... e...' em vez de 'ou... ou...' ao descrever o humano."
   }
  ]
 },
 "ch04-identidade-terrena": {
  "cards": [
   {
    "ic": "constellation",
    "t": "Terra-Pátria",
    "b": "A Terra não é só meio ambiente: é a <strong>pátria comum</strong>, organizadora da vida. A mundialização <strong>une e divide ao mesmo tempo</strong> — gera interdependência e desigualdade. Ver com os dois olhos, não celebrar ingenuamente.",
    "tip": "<strong>Modelo mental:</strong> trate a Terra como pátria, não como recurso — muda o que se considera 'progresso'."
   },
   {
    "ic": "link",
    "t": "Comunidade de Destino",
    "b": "Estamos na <strong>era planetária</strong>: os mesmos perigos (climáticos, nucleares, pandêmicos) e o mesmo futuro comum. As identidades são <strong>concêntricas, não excludentes</strong>: ser do bairro, do país E da Terra ao mesmo tempo.",
    "tip": "<strong>Como aplicar:</strong> pense local e planetário ao mesmo tempo — as decisões locais têm efeito global e vice-versa."
   },
   {
    "ic": "eye",
    "t": "A Face Dupla da Mundialização",
    "b": "O processo planetário gera <strong>interdependência E desigualdade</strong> simultaneamente. Globalismo ingênuo (só a integração) e nacionalismo fechado (nega o destino comum) são os dois anti-padrões. A educação mostra as duas faces.",
    "tip": "<strong>Para refletir:</strong> uma crise climática regional é sempre um nó da comunidade de destino — não 'problema de fora'."
   }
  ]
 },
 "ch05-enfrentar-as-incertezas": {
  "cards": [
   {
    "ic": "wave",
    "t": "Ecologia da Ação",
    "b": "Assim que uma ação é lançada, ela <strong>escapa às intenções</strong> de quem a iniciou e entra no jogo das interações do meio — pode ser desviada, até para o oposto do pretendido. A ação é aposta, não execução de plano.",
    "tip": "<strong>Como aplicar:</strong> pergunte 'o que o meio fará com a minha ação?' — decida pensando no efeito, não só na intenção."
   },
   {
    "ic": "fork",
    "t": "Estratégia × Programa",
    "b": "<strong>Programa</strong>: sequência fixa — eficiente em ambiente estável, quebra ao primeiro imprevisto. <strong>Estratégia</strong>: cenário aberto que se modifica conforme o acaso — usa o inesperado em vez de ser destruído por ele. Em mundo incerto, sempre estratégia.",
    "tip": "<strong>Regra:</strong> na dúvida, estratégia. Se o novo fosse previsível, não seria novo."
   },
   {
    "ic": "mountain",
    "t": "A Aposta Consciente",
    "b": "Agir sob incerteza é <strong>apostar</strong> — assumir convicção sabendo que pode falhar, e por isso manter-se vigilante e corrigível. A história avança por bifurcações, acasos e retrocessos — não em linha reta de progresso.",
    "tip": "<strong>Modelo mental:</strong> 'navegar um oceano de incertezas por arquipélagos de certezas locais'."
   }
  ]
 },
 "ch06-ensinar-a-compreensao": {
  "cards": [
   {
    "ic": "bubble",
    "t": "Compreender × Explicar",
    "b": "<strong>Explicação</strong>: apreende um objeto por causas e dados — suficiente para coisas. <strong>Compreensão humana</strong>: capta o outro como sujeito — por empatia e identificação. Só explicar uma pessoa = desumanizar.",
    "tip": "<strong>Como aplicar:</strong> com objetos → explique; com pessoas → explique E compreenda."
   },
   {
    "ic": "mask",
    "t": "Os Obstáculos à Compreensão",
    "b": "<strong>Egocentrismo</strong> (self-deception) e <strong>etnocentrismo</strong> (própria cultura como medida de tudo) são os maiores bloqueios. Some a <strong>redução</strong> (rotular o outro por um traço) e a <strong>possessão por ideias</strong> — e o diálogo fecha.",
    "tip": "<strong>Sinal de alerta:</strong> você está rotulando o outro por um traço ou justificando-se — pare e compreenda."
   },
   {
    "ic": "key",
    "t": "Ética da Compreensão",
    "b": "Compreender não é desculpar tudo — é recusar a condenação fácil. <strong>'Compreender é encontrar de novo o humano no outro'</strong>, ainda no inimigo. A introspecção revela em você o que você condena no outro. Base de toda paz.",
    "tip": "<strong>Para refletir:</strong> a incompreensão é o solo da violência; a compreensão a desarma."
   }
  ]
 },
 "ch07-antropoetica": {
  "cards": [
   {
    "ic": "spiral",
    "t": "A Tríade Ética",
    "b": "<strong>Indivíduo ⇄ Sociedade ⇄ Espécie</strong> — cada termo é meio e fim dos outros. A antropoética exige os três planos ao mesmo tempo: autonomia individual, participação social e consciência de pertencer à espécie. Nenhum polo sozinho basta.",
    "tip": "<strong>Como aplicar:</strong> teste qualquer decisão nos 3 anéis — avançar num destruindo os outros = falha ética."
   },
   {
    "ic": "balance",
    "t": "Democracia como Dialógica",
    "b": "Democracia não é só voto: é o <strong>circuito de controle mútuo</strong> sociedade ↔ indivíduo, que vive de <strong>diversidade + conflito regrado + consenso</strong>. Degenera quando a diversidade some ou o conflito perde a regra. Sem isso, vira tirania da maioria.",
    "tip": "<strong>Para refletir:</strong> cuide da diversidade e do conflito regrado — é deles que a democracia vive."
   },
   {
    "ic": "leaf",
    "t": "Cidadania Terrena",
    "b": "A <strong>hominização é inacabada</strong>: tornar-se humano é tarefa, não dado pronto. A meta é a <strong>cidadania terrena</strong> — realizar a humanidade em nós e responder pela Terra-Pátria. 'Ser humano' como verbo, não substantivo.",
    "tip": "<strong>Modelo mental:</strong> pense ética em três planos ao mesmo tempo: o eu, o nós e a humanidade."
   }
  ]
 }
}
```
