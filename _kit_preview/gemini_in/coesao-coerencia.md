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

# LIVRO PARA APROFUNDAR: Coesão e Coerência — Beaugrande, Dressler & Halliday

**Subtítulo:** VISÃO GERAL · OS 7 CRITÉRIOS DA TEXTUALIDADE
**Ideia central:** O que faz de um conjunto de frases um texto? Beaugrande & Dressler respondem com sete critérios de textualidade — e Halliday & Hasan detalham os cinco mecanismos que amarram a superfície. Um texto não é frase grande: é uma ocorrência comunicativa que precisa se conectar (coesão), fazer sentido (coerência) e funcionar numa situação real. É a régua para diagnosticar por que um texto não fecha.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-textualidade` — CAPÍTULO 1: O Que É Um Texto — Os 7 Critérios
- `ch02-coesao-referencia` — CAPÍTULO 2: Coesão I — Referência, Substituição, Elipse
- `ch03-coesao-conjuncao-lexical` — CAPÍTULO 3: Coesão II — Conjunção e Coesão Lexical
- `ch04-coerencia` — CAPÍTULO 4: Coerência — A Continuidade de Sentidos
- `ch05-intencionalidade-aceitabilidade` — CAPÍTULO 5: Intencionalidade e Aceitabilidade
- `ch06-informatividade` — CAPÍTULO 6: Informatividade
- `ch07-situacionalidade` — CAPÍTULO 7: Situacionalidade
- `ch08-intertextualidade` — CAPÍTULO 8: Intertextualidade
- `ch09-principios-regulativos` — CAPÍTULO 9: Os Princípios Regulativos

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-textualidade": {
  "cards": [
   {
    "ic": "layers",
    "t": "Os 7 critérios",
    "b": "<strong>Coesão</strong> (superfície) e <strong>coerência</strong> (sentido) são centrados no texto; <strong>intencionalidade, aceitabilidade, informatividade, situacionalidade e intertextualidade</strong> são centrados no uso.",
    "tip": "<strong>Como aplicar:</strong> cada critério é uma condição — a falha de um compromete o todo."
   },
   {
    "ic": "bubble",
    "t": "Ocorrência comunicativa",
    "b": "O texto <strong>acontece numa situação real</strong>, com alguém querendo dizer algo a alguém. Avalie-o pela comunicação que realiza, não pela gramática isolada.",
    "tip": "<strong>Modelo mental:</strong> texto é evento, não objeto."
   },
   {
    "ic": "gap",
    "t": "Gramática ≠ textualidade",
    "b": "Frases corretas e <strong>desconexas</strong> não fazem um texto. Avaliar o texto fora da situação mede só metade.",
    "tip": "<strong>Cuidado:</strong> não busque perfeição nos sete — eles se equilibram."
   }
  ]
 },
 "ch02-coesao-referencia": {
  "cards": [
   {
    "ic": "link",
    "t": "Referência",
    "b": "Uma forma que <strong>aponta</strong> para outro elemento em vez de nomeá-lo de novo — pronomes, demonstrativos, artigos. <strong>Anafórica</strong> (aponta para trás) ou <strong>catafórica</strong> (para frente).",
    "tip": "<strong>Como aplicar:</strong> todo pronome é uma promessa de antecedente claro."
   },
   {
    "ic": "pivot",
    "t": "Substituição e elipse",
    "b": "<strong>Substituição</strong> troca um item por forma curta ('outra'); <strong>elipse</strong> omite o recuperável ('Eu [quero]') — a substituição por zero.",
    "tip": "<strong>Modelo mental:</strong> só funcionam se o leitor reconstrói sem esforço."
   },
   {
    "ic": "gap",
    "t": "Pronome ambíguo",
    "b": "'João disse a Pedro que <strong>ele</strong> errou' — quem? A ambiguidade referencial é o defeito de coesão <strong>mais comum</strong>.",
    "tip": "<strong>Cuidado:</strong> referência distante demais faz o leitor perder o fio."
   }
  ]
 },
 "ch03-coesao-conjuncao-lexical": {
  "cards": [
   {
    "ic": "steps",
    "t": "Conjunção (conectores)",
    "b": "As expressões que <strong>sinalizam a relação</strong> — aditiva (e), adversativa (mas), causal (porque), temporal (então), conclusiva (portanto). O conectivo é a placa de trânsito do raciocínio.",
    "tip": "<strong>Como aplicar:</strong> o conectivo é a seta do raciocínio — confirma, contradiz ou conclui."
   },
   {
    "ic": "constellation",
    "t": "Coesão lexical",
    "b": "Amarração pelo vocabulário — <strong>reiteração</strong> (repetir, sinônimo, hiperônimo) e <strong>colocação</strong> (palavras do mesmo <strong>campo semântico</strong> que coocorrem).",
    "tip": "<strong>Modelo mental:</strong> as palavras de um texto devem 'se conhecer'."
   },
   {
    "ic": "gap",
    "t": "Conectivo errado ou demais",
    "b": "'mas' onde a relação é causal, ou 'portanto' sem premissa, <strong>desorienta</strong>. Excesso de 'aí/então/daí' vira ruído.",
    "tip": "<strong>Cuidado:</strong> trocar de campo semântico sem transição faz o texto 'pular de assunto'."
   }
  ]
 },
 "ch04-coerencia": {
  "cards": [
   {
    "ic": "constellation",
    "t": "Mundo textual e inferência",
    "b": "A coerência é a <strong>estabilidade</strong> dos conceitos que o texto ativa na mente — sem contradições nem buracos. Muito dela é construído por <strong>inferência</strong>, não escrito.",
    "tip": "<strong>Como aplicar:</strong> a coerência mora na cabeça do leitor; o texto dá as pistas."
   },
   {
    "ic": "layers",
    "t": "Esquemas, frames e scripts",
    "b": "Estruturas de conhecimento (o 'roteiro do restaurante') que o texto <strong>evoca</strong> e o leitor usa — economia: não é preciso explicar o óbvio.",
    "tip": "<strong>Modelo mental:</strong> sentido é uma rede, não uma fila."
   },
   {
    "ic": "gap",
    "t": "Salto lógico e contradição",
    "b": "Pular uma etapa que o leitor <strong>não infere</strong> abre um buraco; afirmar o que choca com o mundo textual gera ruído.",
    "tip": "<strong>Cuidado:</strong> coeso e incoerente existe — a coerência é a prova final."
   }
  ]
 },
 "ch05-intencionalidade-aceitabilidade": {
  "cards": [
   {
    "ic": "target",
    "t": "Intencionalidade",
    "b": "A intenção do produtor de que aquilo <strong>conte como texto</strong> coeso e coerente e sirva a um plano — informar, persuadir, emocionar. O texto é instrumento de um objetivo.",
    "tip": "<strong>Como aplicar:</strong> texto sem propósito visível é abandonado."
   },
   {
    "ic": "bubble",
    "t": "Aceitabilidade",
    "b": "A disposição do receptor de <strong>cooperar</strong> — preencher lacunas, tolerar pequenas falhas — desde que perceba relevância e utilidade.",
    "tip": "<strong>Modelo mental:</strong> texto é cooperação, não transmissão."
   },
   {
    "ic": "gap",
    "t": "Ignorar o destinatário",
    "b": "Escrever para si, não para quem recebe, derruba a aceitabilidade. Abusar da cooperação (defeitos demais) faz o leitor <strong>parar de colaborar</strong>.",
    "tip": "<strong>Cuidado:</strong> a mesma mensagem muda de forma conforme quem recebe."
   }
  ]
 },
 "ch06-informatividade": {
  "cards": [
   {
    "ic": "scale",
    "t": "As três ordens",
    "b": "<strong>1ª ordem</strong> — trivial, entedia. <strong>2ª ordem</strong> — o equilíbrio ideal, informa sem sobrecarregar. <strong>3ª ordem</strong> — inesperado a ponto de exigir grande esforço (arriscado).",
    "tip": "<strong>Como aplicar:</strong> mire a 2ª ordem; o tédio e o caos são vizinhos do fracasso."
   },
   {
    "ic": "spark",
    "t": "Surpresa motivada",
    "b": "A quebra de expectativa funciona quando o leitor <strong>encontra a razão</strong> dela. Surpreenda, mas dê a chave.",
    "tip": "<strong>Modelo mental:</strong> o esperado garante compreensão; o novo garante interesse."
   },
   {
    "ic": "gap",
    "t": "Óbvio ou denso demais",
    "b": "Dizer o que o público já sabe (1ª) faz pular; empilhar novidade sem âncora (3ª) faz <strong>se perder</strong>.",
    "tip": "<strong>Cuidado:</strong> densidade plana, sem picos, não cria interesse."
   }
  ]
 },
 "ch07-situacionalidade": {
  "cards": [
   {
    "ic": "pin",
    "t": "O contexto é metade do texto",
    "b": "Os fatores que tornam o texto <strong>relevante</strong> ao contexto. O contexto carrega sentido que as palavras não precisam repetir e define o que pode ficar implícito.",
    "tip": "<strong>Como aplicar:</strong> 'Cuidado, degrau' é texto completo na situação — fora dela, fragmento."
   },
   {
    "ic": "pivot",
    "t": "Monitorar vs. gerenciar",
    "b": "O texto pode só <strong>descrever</strong> a situação (monitorar) ou <strong>agir para mudá-la</strong> (gerenciar — uma ordem, um pedido, uma persuasão).",
    "tip": "<strong>Modelo mental:</strong> texto certo, lugar errado, é texto errado."
   },
   {
    "ic": "gap",
    "t": "Ignorar o suporte",
    "b": "Escrever para o YouTube como se fosse ensaio acadêmico é <strong>desajuste de situação</strong>. Repetir o que o contexto já diz é ruído.",
    "tip": "<strong>Cuidado:</strong> texto irrelevante à situação falha mesmo sendo coeso e coerente."
   }
  ]
 },
 "ch08-intertextualidade": {
  "cards": [
   {
    "ic": "link",
    "t": "O texto depende de textos",
    "b": "Os fatores que fazem o uso de um texto depender do <strong>conhecimento de outros</strong>. Nenhum texto começa do zero — herda formas e expectativas.",
    "tip": "<strong>Como aplicar:</strong> aludir ao que o público conhece economiza; ao obscuro, quebra a ponte."
   },
   {
    "ic": "book",
    "t": "Gêneros = contrato prévio",
    "b": "Reconhecer o gênero (notícia, receita, resumo) <strong>ativa expectativas</strong> que guiam produtor e receptor — intertextualidade institucionalizada.",
    "tip": "<strong>Modelo mental:</strong> o gênero é metade da compreensão antes da 1ª palavra."
   },
   {
    "ic": "gap",
    "t": "Clichê e alusão obscura",
    "b": "Repetir fórmulas sem perceber gera previsibilidade (1ª ordem); referir um texto que o público não conhece <strong>não forma a ponte</strong>.",
    "tip": "<strong>Cuidado:</strong> quebrar o gênero pode encantar (surpresa motivada) ou frustrar."
   }
  ]
 },
 "ch09-principios-regulativos": {
  "cards": [
   {
    "ic": "scale",
    "t": "Eficiência × Efetividade → Adequação",
    "b": "<strong>Eficiência</strong> = mínimo esforço (mas, só, entedia). <strong>Efetividade</strong> = forte impressão (mas, só, cansa). <strong>Adequação</strong> = o equilíbrio calibrado à situação.",
    "tip": "<strong>Como aplicar:</strong> eficiência poupa; efetividade marca; adequação decide."
   },
   {
    "ic": "pivot",
    "t": "Otimizar, não maximizar",
    "b": "Não se <strong>maximiza</strong> um critério — otimiza-se o conjunto. Maximizar um sempre custa outro.",
    "tip": "<strong>Modelo mental:</strong> o alvo é o ponto ótimo, não o extremo."
   },
   {
    "ic": "gap",
    "t": "Só fluência ou só impacto",
    "b": "100% eficiente = fluente e <strong>esquecível</strong>; 100% efetivo = impactante e <strong>exaustivo</strong>. Os dois extremos falham.",
    "tip": "<strong>Cuidado:</strong> o equilíbrio certo muda com gênero, canal e público."
   }
  ]
 }
}
```
