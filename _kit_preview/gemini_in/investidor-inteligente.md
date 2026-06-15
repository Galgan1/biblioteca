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

# LIVRO PARA APROFUNDAR: O Investidor Inteligente — Benjamin Graham

**Subtítulo:** VISÃO GERAL · A BÍBLIA DO VALUE INVESTING
**Ideia central:** O 'investidor inteligente' não é o mais esperto — é o mais paciente e disciplinado. Graham mostra que o maior inimigo do investidor é ele mesmo, e que duas palavras resumem tudo: margem de segurança. A alegoria do Sr. Mercado, a distinção preço × valor e as regras para o defensivo e o empreendedor compõem o manual definitivo.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-investidor-vs-especulador` — CAPÍTULO 1: Investimento vs. Especulação
- `ch02-inflacao` — CAPÍTULO 2: O Investidor e a Inflação
- `ch03-historico-do-mercado` — CAPÍTULO 3: Um Século de História do Mercado
- `ch04-investidor-defensivo` — CAPÍTULO 4: A Carteira do Investidor Defensivo
- `ch05-investidor-empreendedor` — CAPÍTULO 5: A Carteira do Investidor Empreendedor
- `ch06-preco-vs-valor` — CAPÍTULO 6: Preço vs. Valor
- `ch07-sr-mercado` — CAPÍTULO 7: A Alegoria do Sr. Mercado
- `ch08-margem-de-seguranca` — CAPÍTULO 8: A Margem de Segurança
- `ch09-temperamento-e-disciplina` — CAPÍTULO 9: Temperamento e Disciplina
- `ch10-analise-de-empresas` — CAPÍTULO 10: Análise e Seleção de Ações

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-investidor-vs-especulador": {
  "cards": [
   {
    "ic": "scale",
    "t": "A Definição Tríplice",
    "b": "<strong>Investimento</strong> = análise minuciosa + segurança do principal + retorno adequado. Faltando qualquer um dos três pilares, é <strong>especulação</strong> — consciente ou não.",
    "tip": "<strong>Como aplicar:</strong> antes de qualquer aplicação, classifique-a pelos três pilares — se faltar um, admita que está especulando."
   },
   {
    "ic": "fork",
    "t": "Defensivo × Empreendedor",
    "b": "Dois perfis, duas estratégias coerentes. O <strong>defensivo</strong> busca tranquilidade e ausência de erros graves; o <strong>empreendedor</strong> dedica tempo e método para superar a média. O erro é o meio-termo sem disciplina.",
    "tip": "<strong>Regra:</strong> escolha um perfil e seja coerente — o amador que tenta ser ativo sem método destrói valor."
   },
   {
    "ic": "gap",
    "t": "Especulação Inteligente vs. Burra",
    "b": "Especular pode ser legítimo — desde que <strong>consciente, isolado e dimensionado</strong>. A conta separada de especulação preserva o capital de investimento. O erro fatal é especular acreditando estar investindo.",
    "tip": "<strong>Sinal de alerta:</strong> misturar o capital de longo prazo com apostas de curto prazo na mesma conta."
   }
  ]
 },
 "ch02-inflacao": {
  "cards": [
   {
    "ic": "wave",
    "t": "Retorno Real vs. Nominal",
    "b": "O que importa é o ganho <strong>acima da inflação</strong>, não o número de cotação. Ganhar 6% com inflação de 8% é perder 2% de poder de compra ao ano — uma perda real, mesmo que o saldo suba nominalmente.",
    "tip": "<strong>Como aplicar:</strong> ao avaliar qualquer rendimento, sempre subtraia a inflação esperada."
   },
   {
    "ic": "triangle",
    "t": "Ações como Hedge Imperfeito",
    "b": "Empresas reajustam preços e lucros, oferecendo proteção <strong>parcial</strong> contra inflação — útil, mas não garantida em todo cenário. Títulos sofrem com inflação alta; ações sofrem em deflação/recessão.",
    "tip": "<strong>Modelo mental:</strong> trate a inflação como um cenário a defender, não a prever — prepare a carteira para conviver com ela."
   },
   {
    "ic": "layers",
    "t": "Diversificação Defensiva",
    "b": "Ter ações <strong>e</strong> renda fixa defende contra cenários opostos — nenhuma alocação única ganha em todos os ambientes. Mesmo o defensivo precisa de parcela permanente em ações.",
    "tip": "<strong>Cuidado:</strong> manter todo o patrimônio em caixa/renda fixa em ambiente inflacionário é uma perda lenta garantida."
   }
  ]
 },
 "ch03-historico-do-mercado": {
  "cards": [
   {
    "ic": "clock",
    "t": "O Preço Pago Define o Retorno",
    "b": "Quanto mais caro o mercado hoje, menor o retorno esperado e maior o risco. Os múltiplos (preço/lucro ajustado) são a bússola de expectativa — não uma bola de cristal, mas o dado mais confiável disponível.",
    "tip": "<strong>Como aplicar:</strong> quando o mercado estiver em múltiplos históricos altos, reduza expectativas e reforce cautela."
   },
   {
    "ic": "spiral",
    "t": "Reversão à Média",
    "b": "Extremos de valuation tendem a se corrigir. O que sobe demais costuma voltar; o que cai demais também. A euforia 'desta vez é diferente' marcou quase todos os topos históricos.",
    "tip": "<strong>Modelo mental:</strong> use a história como bússola de expectativa, não como bola de cristal — ela ensina padrões, não datas."
   },
   {
    "ic": "wave",
    "t": "Ajuste a Alocação ao Ciclo",
    "b": "Variar entre ~50% e ~75% em ações conforme o mercado esteja caro ou barato — mas sempre <strong>dentro de limites disciplinados</strong>. Comprar mais justamente quando está mais caro (FOMO) é o erro mais comum.",
    "tip": "<strong>Sinal de alerta:</strong> quando todos estão eufóricos, mais cautela — não mais coragem."
   }
  ]
 },
 "ch04-investidor-defensivo": {
  "cards": [
   {
    "ic": "scale",
    "t": "A Faixa 50/50 a 75/25",
    "b": "Nunca menos de 25% nem mais de 75% em ações; o ponto neutro é <strong>50/50</strong>. Quando o mercado empurrar a proporção para fora da faixa, rebalanceie — essa mecânica <strong>vende caro e compra barato</strong> no automático.",
    "tip": "<strong>Como aplicar:</strong> regras > previsões — o defensivo terceiriza a decisão para um sistema, não para o palpite."
   },
   {
    "ic": "clock",
    "t": "Dollar-Cost Averaging",
    "b": "Investir um valor fixo em intervalos fixos (aportes regulares) compra mais cotas quando barato e menos quando caro — neutraliza o timing e <strong>disciplina sem força de vontade</strong>. Abandone os aportes justamente nas quedas e perde o que é mais valioso.",
    "tip": "<strong>Regra:</strong> defina valor e periodicidade e cumpra-os independente do humor do mercado."
   },
   {
    "ic": "key",
    "t": "Blue Chips e Simplicidade",
    "b": "Empresas grandes, conservadoramente financiadas, com longo histórico de lucros e dividendos. <strong>Simplicidade como estratégia</strong>: menos decisões discricionárias = menos erros emocionais.",
    "tip": "<strong>Modelo mental:</strong> concentrar em poucas ou em modismos sem histórico é o oposto do que o defensivo deve fazer."
   }
  ]
 },
 "ch05-investidor-empreendedor": {
  "cards": [
   {
    "ic": "lens",
    "t": "Caça às Pechinchas",
    "b": "Comprar ativos cotados <strong>bem abaixo do valor intrínseco/contábil</strong> — empresas sólidas em desgraça temporária ou negligenciadas pelo mercado. O coração da estratégia ativa é comprar o dólar por cinquenta centavos.",
    "tip": "<strong>Como aplicar:</strong> quando você pode analisar a fundo e o mercado precifica mal por pessimismo ou desatenção."
   },
   {
    "ic": "gap",
    "t": "Net-Nets (NCAV)",
    "b": "Ações negociadas abaixo do <strong>ativo circulante líquido</strong> (capital de giro menos todo o passivo) oferecem margem extrema — você recebe o negócio 'de graça'. Exigem <strong>cesta diversificada</strong>: são frágeis individualmente.",
    "tip": "<strong>Cuidado:</strong> concentrar numa única net-net é o erro — são situações de risco; só funcionam em cesta."
   },
   {
    "ic": "target",
    "t": "Esforço com Método",
    "b": "Ser 'ativo' no sentido de girar a carteira, pagar corretagem e seguir manchetes <strong>não é</strong> investimento empreendedor. Atividade sem disciplina destrói valor; sem método, o empreendedor é pior que o defensivo.",
    "tip": "<strong>Regra:</strong> só seja ativo se tiver disciplina e método comprovados; senão, seja definitivamente defensivo."
   }
  ]
 },
 "ch06-preco-vs-valor": {
  "cards": [
   {
    "ic": "scale",
    "t": "Preço ≠ Valor",
    "b": "<strong>Preço</strong> = cotação de mercado, volátil e emocional. <strong>Valor</strong> = estimativa fundamentada do que o negócio vale. Nunca os confunda — o erro de confundir preço subindo com valor aumentando é o mais caro do investidor.",
    "tip": "<strong>Como aplicar:</strong> se preço << valor, compre; se preço >> valor, evite ou venda; no meio, abstenha-se."
   },
   {
    "ic": "wave",
    "t": "Votação × Balança",
    "b": "No <strong>curto prazo</strong> o mercado é uma máquina de votação (popularidade, emoção); no <strong>longo prazo</strong>, é uma balança (pesa o valor real). Tenha paciência para a balança agir.",
    "tip": "<strong>Modelo mental:</strong> o esquecido com desconto é preferível ao querido sobreprecificado."
   },
   {
    "ic": "lens",
    "t": "Faixas, não Precisão",
    "b": "Estime valor por <strong>faixas amplas</strong>, não por números exatos ilusórios. Graham desconfia do qualitativo excessivo — números (lucros, dívida, ativos) ancoram; qualidade refina.",
    "tip": "<strong>Cuidado:</strong> comprar pelo 'momentum' da popularidade (votação), não pelo fundamento (peso), é especulação."
   }
  ]
 },
 "ch07-sr-mercado": {
  "cards": [
   {
    "ic": "person",
    "t": "Servo, Não Guia",
    "b": "O Sr. Mercado está a seu serviço com cotações diárias — explore suas extravagâncias, não as siga. Aja quando o preço for <strong>absurdamente baixo</strong> (compre) ou alto (venda/ignore); nos demais dias, ignore-o.",
    "tip": "<strong>Regra:</strong> quando ele entra em pânico, faça compras; quando eufórico, fique cético."
   },
   {
    "ic": "spark",
    "t": "Volatilidade = Oportunidade",
    "b": "A oscilação só prejudica quem deixa o Sr. Mercado <strong>ditar</strong> suas decisões. Para o disciplinado, ela cria pechinchas — compra-se mais caro no topo e mais barato no fundo sem nenhuma análise extra.",
    "tip": "<strong>Modelo mental:</strong> sua riqueza real depende do negócio, não da cotação de hoje."
   },
   {
    "ic": "mask",
    "t": "Imunidade Emocional",
    "b": "Tratar a cotação diária como medida de quanto você é rico ou sábio é deixar o humor do Sr. Mercado contaminar sua avaliação. <strong>Vender no pânico e comprar na euforia</strong> é o ciclo que destrói patrimônio.",
    "tip": "<strong>Sinal de alerta:</strong> sentir urgência de 'fazer algo' com a carteira toda vez que o mercado oscila."
   }
  ]
 },
 "ch08-margem-de-seguranca": {
  "cards": [
   {
    "ic": "scale",
    "t": "O Conceito Central",
    "b": "A margem de segurança é a diferença entre o valor intrínseco estimado e o preço pago. Quanto maior o desconto, maior a proteção. Só compre quando o preço estiver <strong>bem abaixo do valor</strong>, deixando folga para você estar errado.",
    "tip": "<strong>Como aplicar:</strong> se você estima o valor em R$ 100/ação, não compre a R$ 95 — espere R$ 60 ou R$ 70."
   },
   {
    "ic": "key",
    "t": "Proteção contra o Erro",
    "b": "A margem existe <strong>porque</strong> o futuro é incerto e suas estimativas são imperfeitas. Protege contra <strong>perda permanente</strong> — não evita a volatilidade. Construa a ponte para 30 toneladas e dirija o caminhão de 10.",
    "tip": "<strong>Modelo mental:</strong> pense primeiro em não perder; o ganho vem como consequência da disciplina."
   },
   {
    "ic": "layers",
    "t": "Margem + Diversificação",
    "b": "Mesmo com margem, espalhe o risco. Algumas teses falharão — a margem + diversificação garantem o resultado do conjunto. Concentrar tudo numa tese, mesmo com margem ampla, é dispensar o seguro contra o imprevisto.",
    "tip": "<strong>Cuidado:</strong> confiar tanto na própria análise a ponto de dispensar a margem ou a diversificação."
   }
  ]
 },
 "ch09-temperamento-e-disciplina": {
  "cards": [
   {
    "ic": "mountain",
    "t": "Caráter > QI",
    "b": "O principal inimigo do investidor é <strong>ele mesmo</strong>. Dois investidores com o mesmo conhecimento e a mesma carteira: na queda, um vende em pânico e cristaliza a perda; o outro compra mais e segue o plano. A diferença não foi inteligência — foi <strong>temperamento</strong>.",
    "tip": "<strong>Como aplicar:</strong> tenha regras escritas e siga-as — a disciplina substitui a força de vontade no momento da pressão."
   },
   {
    "ic": "clock",
    "t": "Não Prever, Proteger",
    "b": "A meta não é antecipar movimentos do mercado — é garantir que você não tome decisões autodestrutivas. <strong>Proteja-se da sua própria burrice</strong>: desenhe o sistema para o seu pior momento emocional.",
    "tip": "<strong>Modelo mental:</strong> sentir necessidade de 'fazer algo' sempre, em vez de esperar a oportunidade, é o sintoma do problema."
   },
   {
    "ic": "key",
    "t": "Paciência como Vantagem",
    "b": "O investidor pode esperar indefinidamente pela pechincha certa, sem pressão de 'fazer algo'. Abandonar as regras justamente quando elas mais protegem (no pânico ou na euforia) desfaz anos de disciplina.",
    "tip": "<strong>Regra:</strong> regras escritas e paciência são as armas centrais — o investidor inteligente é paciente, não genial."
   }
  ]
 },
 "ch10-analise-de-empresas": {
  "cards": [
   {
    "ic": "lens",
    "t": "Filtro Qualidade + Preço",
    "b": "Critérios do defensivo: tamanho adequado, posição financeira forte (ativo circulante folgado, baixa dívida), histórico de lucros <strong>estável</strong>, dividendos contínuos, crescimento moderado e <strong>múltiplos baixos</strong>. Solidez verificável bate narrativa empolgante.",
    "tip": "<strong>Como aplicar:</strong> compre solidez com desconto — fundamentos verificáveis sempre."
   },
   {
    "ic": "scale",
    "t": "P/L e P/VPA com Tetos",
    "b": "Pagar pouco em relação aos lucros (P/L baixo) <strong>e</strong> ao patrimônio (P/VPA baixo) limita o sobrepreço. Graham combina os dois — uma empresa pode ter P/L razoável mas P/VPA elevado, o que sinaliza risco.",
    "tip": "<strong>Modelo mental:</strong> os números são o piso; a margem nasce de pagar pouco por eles."
   },
   {
    "ic": "key",
    "t": "Solidez Financeira",
    "b": "Lucros que cobrem juros com folga e ativos que cobrem passivos sustentam a 'segurança do principal'. <strong>Ignorar a dívida e a liquidez</strong> é o erro que leva à empresa frágil que quebra justamente quando você mais precisava que não quebrasse.",
    "tip": "<strong>Sinal de alerta:</strong> confiar em lucros de um único ano em vez do histórico de longo prazo."
   }
  ]
 }
}
```
