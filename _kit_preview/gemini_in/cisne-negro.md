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

# LIVRO PARA APROFUNDAR: A Lógica do Cisne Negro — Nassim Nicholas Taleb

**Subtítulo:** VISÃO GERAL · O IMPACTO DO ALTAMENTE IMPROVÁVEL
**Ideia central:** Um Cisne Negro é o evento raro, de impacto extremo, que depois racionalizamos como se fosse previsível. Taleb mostra que quase tudo que importa na história vem desses eventos — e que nossas ferramentas de previsão (a curva de sino, as narrativas, os modelos de jogo) nos cegam para eles. A saída não é prever melhor, mas tornar-se robusto ao imprevisível.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-o-cisne-negro` — CAPÍTULO 1: O que é um Cisne Negro
- `ch02-arrogancia-epistemica` — CAPÍTULO 2: Arrogância Epistêmica e a Tríade da Opacidade
- `ch03-falacia-narrativa` — CAPÍTULO 3: A Falácia Narrativa
- `ch04-mediocristao-extremistao` — CAPÍTULO 4: Mediocristão × Extremistão
- `ch05-falacia-ludica` — CAPÍTULO 5: A Falácia Lúdica e a Evidência Silenciosa
- `ch06-limites-da-previsao` — CAPÍTULO 6: Os Limites da Previsão
- `ch07-fraude-do-sino` — CAPÍTULO 7: A Curva de Sino, Essa Grande Fraude Intelectual
- `ch08-robustez-e-barbell` — CAPÍTULO 8: Robustez, Fragilidade e a Estratégia Barbell

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-o-cisne-negro": {
  "cards": [
   {
    "ic": "wave",
    "t": "A Tríade do Cisne Negro",
    "b": "Três traços juntos: <strong>raridade</strong> (fora das expectativas), <strong>impacto extremo</strong> e <strong>previsibilidade retrospectiva</strong> (parece óbvio só depois). É raro, mas decide o jogo — e quase tudo que importa na história entra nessa categoria.",
    "tip": "<strong>Como aplicar:</strong> trate todo 'eu sabia que ia acontecer' como ilusão — se fosse óbvio, alguém teria lucrado antes, com risco real."
   },
   {
    "ic": "spiral",
    "t": "O Peru de Russell",
    "b": "O peru é alimentado todo dia; a cada refeição sua confiança de que 'cuidam de mim' cresce. No milésimo dia, véspera de Ação de Graças, no auge da certeza, é abatido. O ponto de <strong>máxima certeza estatística</strong> foi o de <strong>máximo risco</strong>.",
    "tip": "<strong>Modelo mental:</strong> ausência de evidência ≠ evidência de ausência. Nunca ter visto algo não prova que não exista."
   },
   {
    "ic": "lens",
    "t": "Previsibilidade Retrospectiva",
    "b": "Depois do fato, a mente costura uma narrativa que apaga a surpresa. Isso nos faz confiar de novo e <strong>não aprender que não previmos</strong>. O 'óbvio em retrospecto' é uma ilusão fabricada pela memória.",
    "tip": "<strong>Para refletir:</strong> registre previsões por escrito ANTES; depois compare com a história que você conta. O choque revela o quanto não previu."
   },
   {
    "ic": "book",
    "t": "A Antibiblioteca de Eco",
    "b": "Os livros <strong>não lidos</strong> valem mais que os lidos: sabem o que você ignora. A biblioteca é monumento ao desconhecido, não troféu do conhecido. Meça seu saber pela consciência do que falta, não pelo que domina.",
    "tip": "<strong>Modelo mental:</strong> quanto mais você sabe, mais sabe o tamanho do que não sabe — e é de lá que vem o Cisne Negro."
   }
  ]
 },
 "ch02-arrogancia-epistemica": {
  "cards": [
   {
    "ic": "target",
    "t": "Arrogância Epistêmica",
    "b": "Superestimar o que se sabe e subestimar a incerteza. Mais informação aumenta a <strong>confiança</strong> muito mais que a <strong>acurácia</strong>. O especialista erra quase como o leigo — porém com mais convicção.",
    "tip": "<strong>Como aplicar:</strong> compare a confiança declarada com o histórico real de acertos. Quando divergem, desconfie do confiante."
   },
   {
    "ic": "triangle",
    "t": "A Tríade da Opacidade",
    "b": "Três doenças da mente diante da história: <strong>(a) ilusão de entender</strong> um mundo mais aleatório do que cremos; <strong>(b) distorção retrospectiva</strong> (só julgamos depois, reescrevendo); <strong>(c) excesso de fé na informação</strong> e nos que 'platonificam'.",
    "tip": "<strong>Modelo mental:</strong> para cada explicação histórica, pergunte se não é só uma história contada de trás para frente."
   },
   {
    "ic": "layers",
    "t": "Platonicidade",
    "b": "Confundir o <strong>mapa</strong> com o <strong>território</strong>: preferir formas puras e categorias limpas (triângulos, utopias) à bagunça do real. A 'prega platônica' é onde o modelo quebra — e o Cisne Negro entra justamente ali.",
    "tip": "<strong>Para refletir:</strong> quanto mais elegante e lisa a teoria, mais perigosa a borda onde ela falha."
   },
   {
    "ic": "eye",
    "t": "O Idiota Sortudo",
    "b": "Vemos só os vencedores; quem arriscou igual e quebrou some da amostra (a <strong>evidência silenciosa</strong>). Assim, sorte vira 'talento' e acaso vira 'método'. Buscar exemplos que confirmam não prova nada — um contraexemplo derruba.",
    "tip": "<strong>Regra:</strong> procure o contraexemplo que refuta, não os mil casos que confirmam."
   }
  ]
 },
 "ch03-falacia-narrativa": {
  "cards": [
   {
    "ic": "bubble",
    "t": "A Falácia Narrativa",
    "b": "A tendência a impor enredos lineares sobre fatos, preferindo <strong>histórias compactas à verdade bruta</strong>. Toda narrativa adiciona um 'porque' que pode não existir. Lembramos melhor o que tem enredo — e passamos a acreditar nele.",
    "tip": "<strong>Como aplicar:</strong> separe o que aconteceu (fato) do porquê alegado (interpolação)."
   },
   {
    "ic": "fork",
    "t": "O Teste das Duas Histórias",
    "b": "Se uma narrativa convincente explicaria <strong>igualmente bem o resultado oposto</strong>, ela não explica nada. O noticiário usa 'a inflação' para explicar a alta E a queda do mercado — sinal de que a história é decorativa, não causal.",
    "tip": "<strong>Modelo mental:</strong> quanto mais redonda e fluente a explicação, mais ela apagou o acaso."
   },
   {
    "ic": "steps",
    "t": "Fatos Antes da Narrativa",
    "b": "O cérebro premia o reconhecimento de padrões mesmo onde só há <strong>ruído</strong>. Em decisão real, prefira a lista crua de fatos à história bem contada — e registre previsões por escrito para flagrar a falácia depois.",
    "tip": "<strong>Para refletir:</strong> pós-racionalizar o sucesso ou o fracasso é montar a cadeia causal só depois de saber o desfecho."
   }
  ]
 },
 "ch04-mediocristao-extremistao": {
  "cards": [
   {
    "ic": "mountain",
    "t": "Mediocristão",
    "b": "Domínio do <strong>não escalável</strong> e da física: adicione a maior amostra possível e a média quase não se move (peso, altura, calorias). Há um teto natural. Aqui a curva de sino funciona e o Cisne Negro é fraco.",
    "tip": "<strong>Régua:</strong> 'o maior caso isolado muda o total?' Se não, é Mediocristão."
   },
   {
    "ic": "spark",
    "t": "Extremistão",
    "b": "Domínio do <strong>escalável</strong> (riqueza, vendas, fama, mortes em guerra). Um único caso pode ser maior que todos os outros somados. A média engana, a gaussiana mente — e é aqui que vivem os Cisnes Negros.",
    "tip": "<strong>Régua:</strong> 'um único evento pode ser maior que todo o resto junto?' Se sim, é Extremistão — espere Cisnes Negros."
   },
   {
    "ic": "scale",
    "t": "Escalável × Não Escalável",
    "b": "O dentista é não escalável (ganho proporcional às horas); o escritor, o ator e o trader são escaláveis (um trabalho atinge milhões — <strong>winner-take-all</strong>). O escalável concentra ganhos e amplia o risco de cauda.",
    "tip": "<strong>Modelo mental:</strong> classifique o 'país' ANTES de usar qualquer estatística — a ferramenta gaussiana só vale no Mediocristão."
   }
  ]
 },
 "ch05-falacia-ludica": {
  "cards": [
   {
    "ic": "target",
    "t": "A Falácia Lúdica",
    "b": "Tratar a incerteza da vida como a de um jogo de azar com probabilidades calculáveis. No cassino você conhece as regras; na vida, não — e <strong>o que te quebra vem de fora do modelo</strong>. Precisão decimal sobre incerteza real é fingimento.",
    "tip": "<strong>Como aplicar:</strong> diante de um modelo de risco, pergunte 'que evento, fora deste modelo, tornaria estes cálculos irrelevantes?'"
   },
   {
    "ic": "eye",
    "t": "Evidência Silenciosa",
    "b": "Julgamos pelo que sobrou, ignorando o <strong>cemitério dos que fracassaram igual</strong>. Cícero: os náufragos que rezaram e se salvaram pintam quadros; os que rezaram e afundaram, não. A história é escrita pelos sobreviventes.",
    "tip": "<strong>Modelo mental:</strong> antes de copiar uma receita de sucesso, reconstrua a amostra completa — incluindo os invisíveis."
   },
   {
    "ic": "person",
    "t": "Os Idiotas Sortudos",
    "b": "Entre milhares de gestores, alguns 'ganham do mercado' por puro acaso e viram 'gênios' de palco. O histórico é <strong>artefato de sobrevivência</strong>: resultado não é prova de habilidade. A sorte do Extremistão se disfarça de talento.",
    "tip": "<strong>Para refletir:</strong> o desempenho se mantém quando se conta TODO o universo inicial, não só os sobreviventes?"
   }
  ]
 },
 "ch06-limites-da-previsao": {
  "cards": [
   {
    "ic": "lens",
    "t": "O Escândalo da Previsão",
    "b": "Especialistas erram quase tanto quanto leigos no longo prazo — e com <strong>mais confiança</strong>. Mais credenciais aumentam a arrogância, não a acurácia. A previsão de longo prazo do que importa é logicamente impossível.",
    "tip": "<strong>Como aplicar:</strong> peça o histórico de erros do previsor; olhe o intervalo de incerteza, ignore o ponto central."
   },
   {
    "ic": "key",
    "t": "Serendipidade",
    "b": "Penicilina, internet, laser: grandes descobertas foram <strong>acidentais</strong>. O conhecimento avança mais por acaso explorado do que por planejamento. Para prever o futuro, você teria de prever as descobertas futuras — o que é impossível.",
    "tip": "<strong>Modelo mental:</strong> maximize a exposição ao acaso positivo em vez de apostar num plano único."
   },
   {
    "ic": "pivot",
    "t": "Tinkering (Bricolagem)",
    "b": "Avançar por <strong>tentativa e erro barata</strong>, com muitas apostas pequenas, colhendo Cisnes Negros positivos. Troque 'prever o futuro' por 'preparar-se para vários futuros'. Foque em robustez, não em acerto.",
    "tip": "<strong>Para refletir:</strong> planejamento rígido de longo prazo assume um futuro conhecível — e quebra no primeiro Cisne Negro."
   }
  ]
 },
 "ch07-fraude-do-sino": {
  "cards": [
   {
    "ic": "wave",
    "t": "A Fraude do Sino",
    "b": "Na gaussiana, a probabilidade <strong>despenca exponencialmente</strong> à medida que o evento se afasta da média — um desvio de 10 sigmas é 'impossível'. No Extremistão esses desvios acontecem e definem tudo. Usar o sino ali subestima o risco em ordens de magnitude.",
    "tip": "<strong>Como aplicar:</strong> a variável é escalável? Então o sino está mentindo sobre as caudas."
   },
   {
    "ic": "layers",
    "t": "Caudas Gordas (Fat Tails)",
    "b": "A gaussiana tem <strong>caudas finas</strong> (extremos somem rápido); o Extremistão tem <strong>caudas gordas</strong> (extremos raros, porém devastadores e mais frequentes do que o sino prevê). Desvio-padrão e 'sigmas' dão falsa segurança.",
    "tip": "<strong>Regra:</strong> em domínios sociais e financeiros, assuma fat tails por padrão."
   },
   {
    "ic": "constellation",
    "t": "Cisnes Cinza",
    "b": "O crash de 1987 (-22,6% num dia) tinha, pelo sino, probabilidade quase nula — e aconteceu, e voltou (1998, 2008). Modelados por <strong>fractais</strong>, esses extremos viram <strong>cisnes cinza</strong>: raros e grandes, mas não totalmente surpreendentes.",
    "tip": "<strong>Modelo mental:</strong> a curva de sino é mapa de cidade plana usado numa cordilheira — preciso onde foi desenhado, suicida fora dela."
   }
  ]
 },
 "ch08-robustez-e-barbell": {
  "cards": [
   {
    "ic": "scale",
    "t": "Robustez × Fragilidade",
    "b": "O <strong>frágil</strong> é destruído pelo evento extremo; o <strong>robusto</strong> sobrevive a ele. Como o extremo é inevitável e imprevisível, projete carteira, carreira e sistema para resistir ao pior caso desconhecido — antes de otimizar retorno.",
    "tip": "<strong>Como aplicar:</strong> pergunte 'o que me mata se o impensável acontecer?' e elimine essa exposição primeiro."
   },
   {
    "ic": "wrench",
    "t": "Estratégia Barbell",
    "b": "Combine <strong>extremo conservadorismo</strong> (~85–90% em ativos hiperseguros, perda máxima conhecida e pequena) com <strong>extrema especulação</strong> (~10–15% em apostas de alto retorno e perda limitada). <strong>Esvazie o meio-termo</strong> de risco 'moderado' — que esconde a cauda gorda.",
    "tip": "<strong>Regra:</strong> blindar embaixo, apostar pequeno em cima, esvaziar o meio."
   },
   {
    "ic": "spark",
    "t": "Assimetria (Convexidade)",
    "b": "Busque posições com <strong>perda pequena e limitada</strong> e <strong>ganho grande e ilimitado</strong>. Uma aposta de 10% pode multiplicar por 100; o máximo que se perde são os 10%. Os fractais de Mandelbrot modelam o Extremistão melhor que o sino.",
    "tip": "<strong>Para refletir:</strong> o 'risco moderado' é a posição mais perigosa — confiança falsa somada à exposição à cauda."
   }
  ]
 }
}
```
