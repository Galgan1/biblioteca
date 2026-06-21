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

# LIVRO PARA APROFUNDAR: A Única Coisa — Gary Keller & Jay Papasan

**Subtítulo:** VISÃO GERAL · A VERDADE SURPREENDENTEMENTE SIMPLES POR TRÁS DE RESULTADOS EXTRAORDINÁRIOS
**Ideia central:** Resultados extraordinários não vêm de fazer mais — vêm de estreitar o foco. Keller e Papasan reduzem a produtividade a uma pergunta (a Pergunta Focal) e a uma imagem (o efeito dominó): alinhe as prioridades, derrube a primeira peça e deixe o momento fazer o resto. Faça menos para fazer mais.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-a-tese-do-foco` — CAPÍTULO 1: A tese do foco
- `ch02-o-efeito-domino` — CAPÍTULO 2: O efeito dominó
- `ch03-as-seis-mentiras` — CAPÍTULO 3: As 6 mentiras entre você e o sucesso
- `ch04-a-pergunta-focal` — CAPÍTULO 4: A Pergunta Focal
- `ch05-proposito-prioridade-produtividade` — CAPÍTULO 5: Propósito, prioridade e produtividade
- `ch06-os-quatro-ladroes` — CAPÍTULO 6: Os 4 ladrões e a jornada

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-a-tese-do-foco": {
  "cards": [
   {
    "ic": "target",
    "t": "A Única Coisa",
    "b": "Em cada domínio existe uma ação que, feita primeiro, <strong>destrava ou dispensa o resto</strong>. Identificá-la e proteger seu tempo é todo o jogo. Sucesso e foco são diretamente proporcionais.",
    "tip": "<strong>Como aplicar:</strong> 'se eu só pudesse fazer uma coisa aqui hoje, qual tornaria as outras mais fáceis ou desnecessárias?'"
   },
   {
    "ic": "lens",
    "t": "Faça menos para fazer mais",
    "b": "Contra o instinto de 'fazer tudo': estreitar o foco a uma coisa por vez é o que produz o <strong>desproporcional</strong> — não a multiplicação de tarefas. A mesma luz, concentrada num ponto, queima; espalhada, só aquece.",
    "tip": "<strong>Modelo mental:</strong> trate a lista de afazeres como ruído — ela cresce sozinha; sua tarefa é extrair dela A Única Coisa."
   },
   {
    "ic": "steps",
    "t": "O afunilamento",
    "b": "Vá do <strong>amplo</strong> (todas as opções) ao <strong>único</strong> (a alavanca), descartando o que não é alavanca — não adiando tudo em paralelo. O filtro decisivo: 'mais fácil <em>ou</em> desnecessário'.",
    "tip": "<strong>Para refletir:</strong> a melhor ação não só acelera o resto — às vezes o elimina."
   }
  ]
 },
 "ch02-o-efeito-domino": {
  "cards": [
   {
    "ic": "layers",
    "t": "Sucesso sequencial",
    "b": "Um dominó pode derrubar outro <strong>~50% maior</strong>. Em sequência geométrica, a partir de 5 cm, o 23º dominó teria a altura da Torre Eiffel. Quem persegue tudo ao mesmo tempo não derruba nada.",
    "tip": "<strong>Como aplicar:</strong> a cada dia, ache A Única Coisa de hoje e bata só nela; a sequência faz o que a força bruta não faz."
   },
   {
    "ic": "spark",
    "t": "Momento (momentum)",
    "b": "Cada peça derrubada <strong>facilita a próxima</strong>: é a energia acumulada da sequência. Pequenas ações certas, empilhadas na direção certa, compõem-se em saltos enormes — efeito geométrico, não linear.",
    "tip": "<strong>Modelo mental:</strong> trate o progresso como juro composto de ações — a peça de hoje torna a de amanhã maior."
   },
   {
    "ic": "pin",
    "t": "A pedra angular",
    "b": "A <strong>primeira peça da fila</strong> é onde toda a energia deve ir. Empresas e pessoas extraordinárias começaram com uma prioridade e foram acumulando — o resultado visível é a soma invisível de peças alinhadas em ordem.",
    "tip": "<strong>Para refletir:</strong> 'uma coisa de cada vez' não é lentidão — é a única via geométrica para o extraordinário."
   }
  ]
 },
 "ch03-as-seis-mentiras": {
  "cards": [
   {
    "ic": "scale",
    "t": "Tudo importa igualmente (mentira)",
    "b": "Falso: ~<strong>20% das ações geram ~80% dos resultados</strong> (Pareto). Faça uma <em>lista de sucesso</em> (priorizada pela alavanca), não uma <em>lista de afazeres</em> (tudo no mesmo peso).",
    "tip": "<strong>Como aplicar:</strong> corte da lista até sobrar o que de fato move o resultado — e afunile até a única coisa."
   },
   {
    "ic": "fork",
    "t": "Multitarefa (mentira)",
    "b": "Falso: o cérebro <strong>alterna</strong>, não paraleliza. Cada troca custa tempo e atenção (custo de troca), gerando mais erros e estresse. Verdade: uma coisa por vez.",
    "tip": "<strong>Tell:</strong> orgulho de 'fazer várias coisas ao mesmo tempo' = ineficiência disfarçada de eficiência."
   },
   {
    "ic": "spiral",
    "t": "Disciplina × hábito (mentira 3)",
    "b": "Ninguém é disciplinado em tudo. Você não precisa de mais disciplina — precisa de <strong>hábitos certos</strong>. Use a disciplina (escassa) só para instalar <strong>um hábito de cada vez</strong> (média citada ~66 dias).",
    "tip": "<strong>Modelo mental:</strong> discipline-se só até o hábito assumir; depois ele roda no automático."
   },
   {
    "ic": "clock",
    "t": "Força de vontade (mentira 4)",
    "b": "A força de vontade tem <strong>bateria limitada</strong> que se esgota com decisões ao longo do dia. Por isso faça A Única Coisa <strong>cedo</strong>, com a carga cheia; recarregue com descanso e comida.",
    "tip": "<strong>Tell:</strong> tarefa de maior alavanca deixada para o fim do dia = desperdício da vontade."
   },
   {
    "ic": "wave",
    "t": "Equilíbrio × contrapeso (mentira 5)",
    "b": "O equilíbrio perfeito é mito: buscar o centro dá atenção medíocre a tudo. Verdade: <strong>contrapese</strong> (counterbalance) — desequilíbrio proposital, com janelas curtas (vida) e longas (trabalho).",
    "tip": "<strong>Para refletir:</strong> 'equilíbrio' é verbo (contrapesar), não estado — não fique muito tempo fora do prumo."
   },
   {
    "ic": "mountain",
    "t": "Grande é ruim (mentira 6)",
    "b": "Pensar grande não é perigoso nem arrogante: é o que <strong>abre o campo do possível</strong>. Verdade: pense grande, aja específico — e 'pense como' alguém que já alcançou a meta para achar os passos.",
    "tip": "<strong>Como aplicar:</strong> defina a meta grande e faça engenharia reversa até a ação de agora."
   }
  ]
 },
 "ch04-a-pergunta-focal": {
  "cards": [
   {
    "ic": "target",
    "t": "A Pergunta Focal",
    "b": "<strong>'Qual é A Única Coisa que eu posso fazer, de tal modo que, ao fazê-la, tudo o mais ficará mais fácil ou desnecessário?'</strong> Os dois critérios: <em>posso fazer</em> (ação possível) e <em>mais fácil ou desnecessário</em> (efeito de alavanca).",
    "tip": "<strong>Como aplicar:</strong> use para qualquer meta, projeto, dia ou área da vida — em vez de perguntar 'o que mais posso fazer?'."
   },
   {
    "ic": "key",
    "t": "Grande e específica",
    "b": "A boa resposta é <strong>grande</strong> (mira o resultado extraordinário) e <strong>específica</strong> (aponta a próxima ação concreta) ao mesmo tempo. Vaga demais não move; pequena demais não importa.",
    "tip": "<strong>Tell:</strong> resposta como 'ser mais produtivo' não é ação nem alavanca — refaça a pergunta."
   },
   {
    "ic": "lens",
    "t": "Panorama × Pequeno-foco",
    "b": "Use a pergunta em duas escalas. <strong>Panorama</strong>: 'Qual é A MINHA Única Coisa?' (direção de vida). <strong>Pequeno-foco</strong>: 'Qual é A Única Coisa AGORA para colocar isso em marcha?' (ação de hoje).",
    "tip": "<strong>Modelo mental:</strong> pense num GPS — o panorama é o destino; o pequeno-foco é a próxima curva."
   },
   {
    "ic": "steps",
    "t": "Afunilar no tempo",
    "b": "Encadeie a pergunta: Única Coisa de algum dia → cinco anos → este ano → este mês → esta semana → hoje → <strong>agora</strong>. Cada resposta é o primeiro dominó da anterior (engenharia reversa da meta).",
    "tip": "<strong>Para refletir:</strong> a Única Coisa de hoje deriva da de cinco anos — não pule o panorama nem pare no abstrato."
   }
  ]
 },
 "ch05-proposito-prioridade-produtividade": {
  "cards": [
   {
    "ic": "constellation",
    "t": "Propósito → Prioridade → Produtividade",
    "b": "<strong>Propósito</strong> (a Única Coisa grande, o porquê) define a <strong>prioridade</strong> (a Única Coisa de agora), que dirige a <strong>produtividade</strong> (a ação). Produtividade serve ao propósito — não o contrário.",
    "tip": "<strong>Modelo mental:</strong> um funil, do 'para quê vivo' até 'o que faço nos próximos 90 minutos'."
   },
   {
    "ic": "pivot",
    "t": "Ancorar a meta no futuro",
    "b": "Parta da meta grande lá-na-frente e faça <strong>engenharia reversa</strong> até 'o que devo fazer AGORA?'. Pergunte em sequência: algum dia → 5 anos → este ano → este mês → esta semana → hoje → agora.",
    "tip": "<strong>Como aplicar:</strong> cada passo é o dominó do anterior — a meta vira ação de hoje."
   },
   {
    "ic": "clock",
    "t": "Time blocking",
    "b": "Reserve o tempo da Única Coisa como compromisso inviolável: (1) bloqueie <strong>as férias</strong>; (2) ~<strong>4h seguidas/dia</strong> para A Única Coisa, cedo; (3) <strong>1h/semana</strong> para planejar; (4) <strong>proteja</strong> os blocos.",
    "tip": "<strong>Regra:</strong> o que não é bloqueado e protegido não acontece — bloco não protegido é bloco perdido."
   }
  ]
 },
 "ch06-os-quatro-ladroes": {
  "cards": [
   {
    "ic": "sword",
    "t": "Incapacidade de dizer não",
    "b": "Cada <strong>'sim' a algo é um 'não'</strong> à sua Única Coisa. Diga não com mais frequência — proteja o grande sim com muitos nãos pequenos. Dizer não a uma distração é dizer sim à prioridade.",
    "tip": "<strong>Modelo mental:</strong> trate cada 'sim' como despesa; o orçamento é o tempo da Única Coisa."
   },
   {
    "ic": "triangle",
    "t": "Medo do caos",
    "b": "Focar uma coisa <strong>deixa outras desarrumadas</strong> — e isso assusta. Aceite a desordem periférica como preço inevitável do extraordinário; perfeição em tudo é incompatível com excelência em algo.",
    "tip": "<strong>Para refletir:</strong> onde há luz concentrada, há sombra ao lado — a bagunça é sinal de foco, não de fracasso."
   },
   {
    "ic": "leaf",
    "t": "Maus hábitos de saúde",
    "b": "'A má gestão da energia pessoal é um <strong>ladrão silencioso</strong>.' Sem sono, comida e movimento, o foco desmorona. Cuide do corpo como infraestrutura da produtividade.",
    "tip": "<strong>Como aplicar:</strong> trate energia (sono, comida, movimento) como combustível do foco, não como sobra."
   },
   {
    "ic": "person",
    "t": "Ambiente que não apoia",
    "b": "As <strong>pessoas e o espaço</strong> ao redor moldam você. Cerque-se de quem puxa para cima e organize o entorno para o foco; ambiente errado dobra qualquer disciplina.",
    "tip": "<strong>Modelo mental:</strong> o entorno é corrente de rio — nadar a favor ou contra muda tudo. O maior risco é o arrependimento de não perseguir A Única Coisa."
   }
  ]
 }
}
```
