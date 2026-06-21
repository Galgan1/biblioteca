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

# LIVRO PARA APROFUNDAR: Do Mil ao Milhão — Thiago Nigro (Primo Rico)

**Subtítulo:** VISÃO GERAL · SEM CORTAR O CAFEZINHO
**Ideia central:** Enriquecer não depende de cortar o cafezinho. Depende de atuar sobre três pilares ao mesmo tempo — Gastar Bem, Investir Melhor e Ganhar Mais. Thiago Nigro mostra que gasto tem piso (zero), mas renda não tem teto, e por isso ganhar mais é a maior alavanca de todas.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-tres-pilares` — CAPÍTULO 1: Os Três Pilares da Riqueza
- `ch02-gastar-bem-orcamento` — CAPÍTULO 2: Gastar Bem — Orçamento
- `ch03-tipos-de-gasto` — CAPÍTULO 3: Os Tipos de Gasto
- `ch04-sair-das-dividas` — CAPÍTULO 4: Sair das Dívidas
- `ch05-investir-melhor-renda-fixa-variavel` — CAPÍTULO 5: Renda Fixa × Renda Variável
- `ch06-juros-compostos-comecar-cedo` — CAPÍTULO 6: Juros Compostos e Começar Cedo
- `ch07-diversificacao-erro-da-poupanca` — CAPÍTULO 7: Diversificação e o Erro da Poupança
- `ch08-ganhar-mais-investir-em-si` — CAPÍTULO 8: Ganhar Mais — A Maior Alavanca
- `ch09-primeiro-milhao-liberdade-financeira` — CAPÍTULO 9: O Primeiro Milhão e a Liberdade Financeira

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-tres-pilares": {
  "cards": [
   {
    "ic": "triangle",
    "t": "Os Três Pilares",
    "b": "(1) <strong>Gastar Bem</strong> — gastar menos do que ganha, sair das dívidas; (2) <strong>Investir Melhor</strong> — render acima da inflação, com diversificação; (3) <strong>Ganhar Mais</strong> — aumentar a renda (a maior alavanca). Quem foca só no 1 tem teto baixo.",
    "tip": "<strong>Como aplicar:</strong> avalie os três; diagnostique o mais fraco e comece por ele."
   },
   {
    "ic": "spark",
    "t": "O Mito do Cafezinho",
    "b": "Cortar R$ 5/dia não muda patamar. <strong>Gasto tem piso (zero); renda não tem teto</strong> — por isso ganhar mais é mais potente que economizar mais. A metáfora do cafezinho é a distração que impede de ver os outros dois pilares.",
    "tip": "<strong>Modelo mental:</strong> renda não tem teto; gasto tem piso zero. Por isso 'ganhar mais' supera 'gastar menos'."
   },
   {
    "ic": "layers",
    "t": "A Equação da Riqueza",
    "b": "<strong>Patrimônio = (Renda − Gastos) investido ao longo do tempo, com juros compostos.</strong> Os três pilares operam sobre essas variáveis — é uma equação simples que exige os três termos positivos.",
    "tip": "<strong>Regra:</strong> renda alta resolve sozinha sem investir e sem controlar — o dinheiro escorre. Os três pilares juntos é o que muda."
   }
  ]
 },
 "ch02-gastar-bem-orcamento": {
  "cards": [
   {
    "ic": "scale",
    "t": "A Regra-Mãe",
    "b": "<strong>Gaste menos do que ganha.</strong> A sobra mensal (renda − gastos) é a matéria-prima da riqueza. Quanto maior e mais constante a sobra, mais rápido se acumula patrimônio.",
    "tip": "<strong>Como aplicar:</strong> registre toda a renda e todos os gastos; a sobra é o número que importa."
   },
   {
    "ic": "lens",
    "t": "O Orçamento como Espelho",
    "b": "Registre toda a renda; liste todos os gastos; classifique em fixos, variáveis e supérfluos; defina limite por categoria; revise mês a mês. <strong>O orçamento é espelho, não prisão</strong> — ele revela os vazamentos, não proíbe viver.",
    "tip": "<strong>Modelo mental:</strong> não saber para onde vai o dinheiro (gastar no automático) é o estado padrão que precisa mudar."
   },
   {
    "ic": "clock",
    "t": "Padrão de Vida × Renda",
    "b": "Não deixe o padrão de vida subir na mesma velocidade que a renda — a <strong>inflação do estilo de vida</strong> mantém gente de salário alto sem patrimônio. Ao receber aumento, invista primeiro; consuma devagar.",
    "tip": "<strong>Sinal de alerta:</strong> cada promoção que vira carro novo e apartamento maior sem investir primeiro é inflação de estilo de vida."
   }
  ]
 },
 "ch03-tipos-de-gasto": {
  "cards": [
   {
    "ic": "cards",
    "t": "A Classificação dos Gastos",
    "b": "<strong>Fixos</strong> (repetem com valor estável), <strong>variáveis</strong> (necessários mas oscilam), <strong>supérfluos</strong> (prazeres cortáveis) e <strong>investimentos disfarçados de gasto</strong> (cursos, saúde — geram renda futura). Classifique antes de cortar.",
    "tip": "<strong>Como aplicar:</strong> corte primeiro os supérfluos de baixo valor emocional; renegocie os fixos; nunca corte o que gera renda."
   },
   {
    "ic": "wrench",
    "t": "Ataque os Fixos Primeiro",
    "b": "Renegociar um gasto recorrente vale muito mais que cortar um prazer pontual. Muitos gastos 'fixos' (juros, planos, assinaturas) são <strong>negociáveis</strong> e dão ganho recorrente.",
    "tip": "<strong>Modelo mental:</strong> pergunte 'isso me aproxima ou me afasta da liberdade financeira?' antes de cada gasto relevante."
   },
   {
    "ic": "bulb",
    "t": "Gasto Bom × Gasto Ruim",
    "b": "Gasto bom se paga (gera renda, economia futura ou bem-estar real); gasto ruim drena sem retorno. <strong>Nunca corte o que aumenta sua renda futura</strong> (qualificação, saúde, ferramentas) por parecer despesa.",
    "tip": "<strong>Cuidado:</strong> cortar gastos que aumentam a renda (qualificação, saúde) é economizar na semente para não ter colheita."
   }
  ]
 },
 "ch04-sair-das-dividas": {
  "cards": [
   {
    "ic": "sword",
    "t": "Juro da Dívida > Retorno",
    "b": "O rotativo do cartão pode custar centenas de por cento ao ano. Quitar dívida de 300% ao ano é 'render' 300% líquido e garantido — <strong>nenhum investimento bate isso</strong>. Comece sempre pela dívida de maior taxa.",
    "tip": "<strong>Como aplicar:</strong> liste todas as dívidas com suas taxas; ataque primeiro a de maior taxa; renegocie prazos e taxas."
   },
   {
    "ic": "spiral",
    "t": "Juros Compostos Contra Você",
    "b": "Na dívida, o mesmo mecanismo que enriquece no investimento empobrece — a dívida cresce sobre si mesma. <strong>Não adianta encher o barco com o casco furado</strong>: investir mantendo dívida cara é perder nos dois lados.",
    "tip": "<strong>Sinal de alerta:</strong> pagar o mínimo do cartão e rolar o rotativo — o saldo só cresce."
   },
   {
    "ic": "wrench",
    "t": "Renegociação",
    "b": "Credor prefere receber menos a não receber — sempre há margem para negociar. Troque dívida cara por dívida barata (crédito pessoal em vez de rotativo) e reduza a taxa antes de acelerar o pagamento.",
    "tip": "<strong>Regra:</strong> só depois de zeradas as dívidas caras, direcione os mesmos recursos para investir."
   }
  ]
 },
 "ch05-investir-melhor-renda-fixa-variavel": {
  "cards": [
   {
    "ic": "scale",
    "t": "Renda Fixa × Variável",
    "b": "<strong>Renda fixa</strong> (Tesouro Direto, CDB, LCI/LCA) — você empresta e sabe o retorno; mais previsível e menor risco. <strong>Renda variável</strong> (ações, FIIs) — você vira sócio; maior potencial e maior risco. Use fixa para reserva; variável para longo prazo.",
    "tip": "<strong>Modelo mental:</strong> o perfil é tempo + temperamento — quanto mais longo o prazo, mais variável você pode suportar."
   },
   {
    "ic": "lens",
    "t": "Perfil do Investidor",
    "b": "<strong>Conservador</strong> (predomínio de fixa), <strong>moderado</strong> (equilíbrio) e <strong>arrojado</strong> (mais variável). Defina pelo risco tolerado <strong>e</strong> pelo horizonte de tempo — não só pela coragem do momento.",
    "tip": "<strong>Como aplicar:</strong> construa primeiro a reserva em renda fixa de liquidez; só depois, com o que é de longo prazo, exponha à variável."
   },
   {
    "ic": "key",
    "t": "Risco × Retorno",
    "b": "Não existe retorno alto sem risco — promessa de 'alto e garantido' é golpe. <strong>Liquidez</strong> (facilidade de transformar em dinheiro sem perda) é crítica para a reserva de emergência.",
    "tip": "<strong>Cuidado:</strong> entrar em renda variável sem reserva e sem horizonte de longo prazo é especulação disfarçada de investimento."
   }
  ]
 },
 "ch06-juros-compostos-comecar-cedo": {
  "cards": [
   {
    "ic": "spiral",
    "t": "Juro sobre Juro",
    "b": "Rendimento vira capital que também rende — crescimento <strong>exponencial</strong>, não linear. A curva é quase plana no começo e dispara no fim; por isso a impaciência atrapalha e interromper a capitalização por resgate é o erro mais caro.",
    "tip": "<strong>Como aplicar:</strong> reinvista sempre os rendimentos; quanto mais cedo começar e mais tempo deixar, mais a curva acelera."
   },
   {
    "ic": "clock",
    "t": "Tempo > Montante",
    "b": "O ano que você não investiu <strong>não volta</strong>. Começar cedo com aportes pequenos costuma superar começar tarde com aportes grandes — o tempo de capitalização é o recurso mais escasso e insubstituível.",
    "tip": "<strong>Modelo mental:</strong> a 'bola de neve' — pequena no topo da montanha, gigante embaixo, desde que role tempo suficiente."
   },
   {
    "ic": "steps",
    "t": "Aporte Recorrente",
    "b": "Investir um valor fixo constantemente é a disciplina que aproveita o tempo. <strong>Adiar o começo</strong> 'até ter mais dinheiro' é perder o ativo mais valioso: o tempo de capitalização dos anos iniciais.",
    "tip": "<strong>Sinal de alerta:</strong> resgatar e interromper a capitalização por impaciência desfaz o efeito composto justamente quando ele começaria a disparar."
   }
  ]
 },
 "ch07-diversificacao-erro-da-poupanca": {
  "cards": [
   {
    "ic": "cards",
    "t": "Não Ponha Todos os Ovos na Mesma Cesta",
    "b": "Distribua entre <strong>classes</strong> (renda fixa, ações, FIIs), prazos e emissores. Ativos que não sobem e descem juntos (baixa correlação) reduzem o risco da carteira sem sacrificar o retorno.",
    "tip": "<strong>Cuidado:</strong> 'diversificar' não é comprar dezenas de coisas que não entende — é distribuir entre classes compreendidas."
   },
   {
    "ic": "wave",
    "t": "O Erro da Poupança",
    "b": "A poupança frequentemente rende <strong>abaixo da inflação</strong> — o saldo cresce nominalmente, mas compra menos. O Tesouro Selic ou CDB de liquidez diária oferecem segurança comparável <strong>com mais retorno</strong>.",
    "tip": "<strong>Modelo mental:</strong> poupança não é investir, é perder devagar — segura por costume, não por mérito."
   },
   {
    "ic": "lens",
    "t": "Ganho Real vs. Nominal",
    "b": "O que importa é o <strong>ganho acima da inflação</strong> (ganho real), não o número nominal. A poupança muitas vezes tem ganho real negativo — o dinheiro 'guardado' perde poder de compra com o tempo.",
    "tip": "<strong>Sinal de alerta:</strong> concentrar o patrimônio num único ativo, setor ou emissor é o segundo erro mais comum."
   }
  ]
 },
 "ch08-ganhar-mais-investir-em-si": {
  "cards": [
   {
    "ic": "mountain",
    "t": "Renda Não Tem Teto",
    "b": "Dedicar toda a energia a economizar centavos e nenhuma a aumentar a renda é a estratégia de menor potência. <strong>Gasto tem piso; renda não tem limite</strong> — por isso ganhar mais supera economizar mais na alavancagem do patrimônio.",
    "tip": "<strong>Modelo mental:</strong> você é seu melhor investimento — cada real em qualificação tende a render mais que no mercado financeiro, no início da jornada."
   },
   {
    "ic": "bulb",
    "t": "Investir em Si Mesmo",
    "b": "O ativo de maior retorno é a própria capacidade de gerar renda — <strong>qualificação, habilidades, rede de contatos</strong>. Tratar cursos, livros e saúde como gasto a cortar (em vez de investimento em capital humano) é cortar a semente da renda futura.",
    "tip": "<strong>Como aplicar:</strong> separe parte da renda para educação e desenvolvimento profissional — é o investimento de maior retorno no começo."
   },
   {
    "ic": "spiral",
    "t": "Renda Ativa → Renda Passiva",
    "b": "Use a sobra da renda ativa (salário, serviços) para comprar ativos que geram <strong>renda passiva</strong> (investimentos, royalties, negócio sem troca de tempo). Com o tempo, a renda passiva cobre os custos de vida — isso é liberdade.",
    "tip": "<strong>Regra:</strong> ao ganhar mais, segure o padrão de vida (Cap 2) e invista o aumento — não consuma o aumento."
   }
  ]
 },
 "ch09-primeiro-milhao-liberdade-financeira": {
  "cards": [
   {
    "ic": "target",
    "t": "Meta Calculável",
    "b": "O primeiro milhão é consequência de <strong>gastar bem + investir melhor + ganhar mais</strong> ao longo do tempo — não um golpe de sorte. Defina o patrimônio-alvo, o prazo e o aporte necessário; deixe os juros compostos fazerem o trabalho.",
    "tip": "<strong>Como aplicar:</strong> calcule: com seu aporte atual, taxa estimada e prazo, qual patrimônio você atinge? Ajuste os três pilares para chegar ao número."
   },
   {
    "ic": "leaf",
    "t": "Liberdade Financeira",
    "b": "<strong>Renda passiva ≥ custo de vida</strong> — quando os rendimentos dos seus ativos cobrem seu padrão de vida, trabalhar vira opção. Controlar o padrão de vida (Cap 2) aproxima a meta tanto quanto aumentar o patrimônio.",
    "tip": "<strong>Modelo mental:</strong> liberdade é sobre cobrir o padrão de vida com renda passiva — não sobre ostentação."
   },
   {
    "ic": "clock",
    "t": "Constância como Motor",
    "b": "O milhão nasce de <strong>constância nos três pilares ao longo do tempo</strong> — não de esforço heroico nem de atalho arriscado. Os que buscam o milhão por atalhos violam os pilares 1 e 2 e acabam mais atrás.",
    "tip": "<strong>Sinal de alerta:</strong> inflar o padrão de vida a cada aumento empurra a liberdade financeira para sempre."
   }
  ]
 }
}
```
