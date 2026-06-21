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

# LIVRO PARA APROFUNDAR: Os Segredos da Mente Milionária — T. Harv Eker

**Subtítulo:** VISÃO GERAL · REPROGRAME SEU TERMOSTATO FINANCEIRO
**Ideia central:** Seu resultado financeiro é definido por um modelo interno — o 'termostato' — programado na infância. T. Harv Eker mostra como a cadeia Pensamento→Sentimento→Ação→Resultado parte dessa raiz, e apresenta os 17 Arquivos de Riqueza que distinguem como ricos e pobres pensam e agem.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-modelo-de-dinheiro` — CAPÍTULO 1: O Modelo de Dinheiro
- `ch02-processo-pensamento-resultado` — CAPÍTULO 2: A Cadeia P→S→A→R
- `ch03-condicionamento-e-declaracoes` — CAPÍTULO 3: Condicionamento e Declarações
- `ch04-arquivos-protagonismo` — CAPÍTULO 4: Arquivos — Protagonismo e Compromisso
- `ch05-arquivos-visao-oportunidade` — CAPÍTULO 5: Arquivos — Visão Grande e Oportunidade
- `ch06-arquivos-relacoes-valor` — CAPÍTULO 6: Arquivos — Companhias, Valor e Abundância
- `ch07-arquivos-autoestima-receber` — CAPÍTULO 7: Arquivos — Autoestima, Receber e Resultado
- `ch08-arquivos-gestao-patrimonio` — CAPÍTULO 8: Arquivos — Patrimônio e Gestão
- `ch09-arquivos-coragem-crescimento` — CAPÍTULO 9: Arquivos — Coragem e Crescimento

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-modelo-de-dinheiro": {
  "cards": [
   {
    "ic": "spiral",
    "t": "O Termostato Financeiro",
    "b": "O <strong>modelo de dinheiro</strong> é o conjunto pré-programado de crenças, sentimentos e ações sobre dinheiro. Você sempre retorna ao 'ponto de ajuste' — ganhadores de loteria que falência logo exemplificam isso.",
    "tip": "<strong>Modelo mental:</strong> trocar de roupa (técnica ou sorte) não muda o ambiente se o termostato continua no mesmo nível."
   },
   {
    "ic": "layers",
    "t": "As Três Fontes da Programação",
    "b": "O modelo foi instalado por: (1) <strong>verbalização</strong> — o que você ouviu ('dinheiro é a raiz do mal'); (2) <strong>modelagem</strong> — o que viu seus pais fazerem; (3) <strong>incidentes</strong> — experiências emocionais marcantes que viraram decisões inconscientes.",
    "tip": "<strong>Como aplicar:</strong> ao perceber que 'sabota' ganhos ou recai no mesmo saldo, suba à crença que instalou o padrão."
   },
   {
    "ic": "leaf",
    "t": "Causa e Efeito: Raiz e Fruto",
    "b": "O mundo visível (frutos = resultados) é gerado pelo invisível (raízes = mentalidade). <strong>Mexa na raiz, não no fruto.</strong> O modelo não é destino; pode ser reescrito conscientemente.",
    "tip": "<strong>Cuidado:</strong> buscar a 'fórmula' externa sem tocar no modelo interno não muda o termostato."
   }
  ]
 },
 "ch02-processo-pensamento-resultado": {
  "cards": [
   {
    "ic": "steps",
    "t": "A Cadeia Completa",
    "b": "<strong>Pensamento → Sentimento → Ação → Resultado.</strong> O ponto de alavanca está no pensamento (a montante), nunca no resultado (a jusante). Agir só sobre o resultado sem mudar a crença é tarde demais.",
    "tip": "<strong>Como aplicar:</strong> ao diagnosticar resultado ruim, suba a cadeia: resultado → ação → sentimento → crença. Reprograme a crença."
   },
   {
    "ic": "lens",
    "t": "O Resultado como Espelho",
    "b": "O saldo na conta revela o modelo interno com fidelidade — é um <strong>relatório, não uma sentença</strong>. Culpar fatores externos (economia, sorte) ignora os elos internos da cadeia.",
    "tip": "<strong>Modelo mental:</strong> trate o resultado financeiro como feedback do modelo interno, não como destino fixo."
   },
   {
    "ic": "bulb",
    "t": "A Montante vs. A Jusante",
    "b": "Tentar mudar o resultado mudando só a ação ('vou trabalhar mais') sem tocar no pensamento que limita é podar os frutos sem mexer na raiz. O <strong>energy mental é a semente</strong>; o resultado, a colheita.",
    "tip": "<strong>Regra:</strong> o problema está sempre a montante — na crença que origina o sentimento que gera a ação."
   }
  ]
 },
 "ch03-condicionamento-e-declaracoes": {
  "cards": [
   {
    "ic": "steps",
    "t": "Os 4 Passos da Mudança",
    "b": "(1) <strong>Consciência</strong> — perceba a programação. (2) <strong>Compreensão</strong> — entenda de onde veio. (3) <strong>Dissociação</strong> — 'essa é a voz do meu pai, não a minha verdade'. (4) <strong>Recondicionamento</strong> — instale o novo por declaração e ação repetida.",
    "tip": "<strong>Como aplicar:</strong> ao notar o pensamento 'nunca vou guardar dinheiro', rode os 4 passos antes de qualquer outra ação."
   },
   {
    "ic": "spark",
    "t": "As Declarações de Poder",
    "b": "Afirmações ditas em <strong>voz alta, mão no coração, emoção presente</strong>, encerradas por 'Eu tenho uma mente milionária!'. Corpo + voz + emoção gravam mais fundo que o pensamento mudo.",
    "tip": "<strong>Modelo mental:</strong> trate a crença como software — você pode desinstalar a versão herdada e instalar outra."
   },
   {
    "ic": "key",
    "t": "Dissociação: Não Sou Meus Pensamentos",
    "b": "A mudança real exige separar-se da gravação antiga: <strong>'eu posso observar meus pensamentos e escolhê-los'</strong>. A crença herdada é uma gravação, não a sua identidade nem a verdade sobre você.",
    "tip": "<strong>Regra:</strong> confundir a gravação antiga com identidade permanente é o que trava a reprogramação."
   }
  ]
 },
 "ch04-arquivos-protagonismo": {
  "cards": [
   {
    "ic": "target",
    "t": "Arquivo 1 — Criar vs. Ser Vítima",
    "b": "Ricos acreditam que <strong>criam</strong> a própria vida; pobres acreditam que a vida lhes <strong>acontece</strong>. As 3 marcas da vítima: <strong>culpar</strong> (outros), <strong>justificar</strong> ('dinheiro não é importante') e <strong>reclamar</strong> (atrai mais do que foca).",
    "tip": "<strong>Como aplicar:</strong> assuma 100% de responsabilidade — se você criou o resultado, pode recriá-lo."
   },
   {
    "ic": "spark",
    "t": "Arquivo 2 — Jogar para Ganhar",
    "b": "Ricos jogam o jogo do dinheiro <strong>para ganhar</strong> (meta: abundância e liberdade); pobres jogam <strong>para não perder</strong> (meta: sobreviver). A diferença de meta define o teto do resultado.",
    "tip": "<strong>Modelo mental:</strong> defina a meta como riqueza e liberdade — não apenas pagar as contas."
   },
   {
    "ic": "mountain",
    "t": "Arquivo 3 — Compromisso Total",
    "b": "'Querer' ficar rico não basta — ricos <strong>comprometem-se</strong> de verdade ('estou disposto a fazer o que for preciso, dentro da ética'). Compromisso 100% elimina o 'se der'.",
    "tip": "<strong>Cuidado:</strong> desejo vago sem compromisso real produz tentativas que nunca decolam."
   }
  ]
 },
 "ch05-arquivos-visao-oportunidade": {
  "cards": [
   {
    "ic": "triangle",
    "t": "Arquivo 4 — Pensar Grande",
    "b": "Ricos pensam <strong>grande</strong>; pobres pensam pequeno. A Lei da Renda: você é pago na proporção do <strong>valor que entrega</strong> e do número de pessoas que serve. Renda ≈ valor × alcance.",
    "tip": "<strong>Como aplicar:</strong> pergunte 'como posso servir mais pessoas / entregar mais valor?' em vez de 'como ganho mais?'."
   },
   {
    "ic": "lens",
    "t": "Arquivo 5 — Foco em Oportunidades",
    "b": "Ricos focam em <strong>oportunidades</strong> (crescimento potencial); pobres focam em <strong>obstáculos</strong> (risco de perder). O que você procura é o que você enxerga. Aja apesar do risco e ajuste o curso depois.",
    "tip": "<strong>Modelo mental:</strong> veja a oportunidade primeiro, o obstáculo depois — e mesmo assim aja."
   },
   {
    "ic": "bulb",
    "t": "Arquivo 6 — Admirar vs. Ressentir",
    "b": "Ricos <strong>admiram</strong> outros ricos e bem-sucedidos; pobres os <strong>ressentem</strong>. Você não pode se tornar o que despreza. Abençoe o que quer ser — admire como modelo a estudar e superar.",
    "tip": "<strong>Sinal de alerta:</strong> falar mal de ricos programa a mente para não se tornar um."
   }
  ]
 },
 "ch06-arquivos-relacoes-valor": {
  "cards": [
   {
    "ic": "person",
    "t": "Arquivo 7 — Círculo de Convívio",
    "b": "Ricos associam-se a pessoas <strong>positivas e bem-sucedidas</strong>; pobres, a pessoas negativas e malsucedidas. <strong>Você é a média do seu convívio</strong> — modele quem já chegou onde você quer chegar.",
    "tip": "<strong>Como aplicar:</strong> aproxime-se de quem inspira e cresce; reduza exposição a pessimismo crônico."
   },
   {
    "ic": "spark",
    "t": "Arquivo 8 — Promover o Próprio Valor",
    "b": "Ricos promovem a si mesmos e seu valor; pobres enxergam venda negativamente. Se você acredita no que oferece, é <strong>seu dever</strong> fazê-lo chegar a quem precisa. Promoção é serviço, não manipulação.",
    "tip": "<strong>Modelo mental:</strong> trate promoção como dever ético quando você crê no que entrega."
   },
   {
    "ic": "scale",
    "t": "Arquivo 11 — Pensar 'Tanto/Ambos'",
    "b": "Ricos pensam '<strong>tanto... como também</strong>'; pobres pensam '<strong>ou... ou</strong>'. Recuse falsas escolhas (dinheiro <strong>ou</strong> felicidade; carreira <strong>ou</strong> família) — o bolo pode crescer para as duas coisas.",
    "tip": "<strong>Como aplicar:</strong> substitua 'ou' por 'e' e pergunte 'como ter as duas coisas?'."
   }
  ]
 },
 "ch07-arquivos-autoestima-receber": {
  "cards": [
   {
    "ic": "mountain",
    "t": "Arquivo 9 — Maior que os Problemas",
    "b": "Ricos são <strong>maiores</strong> que seus problemas; pobres são menores. O tamanho do problema é fixo — o que muda é o tamanho da pessoa. Cresça você e o problema encolhe relativamente.",
    "tip": "<strong>Regra:</strong> 'Não peça uma vida mais fácil; torne-se mais pessoa.'"
   },
   {
    "ic": "key",
    "t": "Arquivo 10 — Ótimo Recebedor",
    "b": "Ricos são <strong>excelentes recebedores</strong>; pobres bloqueiam o fluxo (recusam elogios com 'imagina, foi sorte', sentem-se indignos). Dizer 'obrigado' sem se diminuir abre o canal da abundância.",
    "tip": "<strong>Como aplicar:</strong> aceite o elogio com 'obrigado, trabalhei muito por isso' — sem diminuir nem inflar."
   },
   {
    "ic": "spark",
    "t": "Arquivo 12 — Pago por Resultado",
    "b": "Ricos preferem ser pagos pelos <strong>resultados</strong>; pobres, pelo <strong>tempo</strong>. Salário por hora tem teto; remuneração por valor entregue (comissão, sociedade, royalties, negócio próprio) não tem.",
    "tip": "<strong>Cuidado:</strong> agarrar-se à segurança do salário por hora bloqueia o acesso ao retorno sem teto."
   }
  ]
 },
 "ch08-arquivos-gestao-patrimonio": {
  "cards": [
   {
    "ic": "scale",
    "t": "Arquivo 13 — Patrimônio Líquido",
    "b": "Ricos focam no <strong>patrimônio líquido</strong> (renda + poupança + investimentos + simplificação do estilo de vida); pobres focam na renda do trabalho. <strong>Patrimônio líquido é o número-mestre</strong> — a verdadeira medida da riqueza.",
    "tip": "<strong>Como aplicar:</strong> acompanhe o patrimônio líquido mensalmente — não apenas o salário."
   },
   {
    "ic": "cards",
    "t": "Arquivo 14 — Sistema dos Frascos",
    "b": "Gestão por percentuais fixos: <strong>NEC 55% · FFA 10% · EDU 10% · PLAY 10% · LTSS 10% · GIVE 5%</strong>. A conta FFA (Liberdade Financeira) <strong>nunca se gasta</strong> — só investe; é a 'galinha dos ovos de ouro'. O hábito conta mais que a quantia.",
    "tip": "<strong>Modelo mental:</strong> gerir bem R$ 1 hoje prepara para gerir R$ 1 milhão — comece com qualquer renda."
   },
   {
    "ic": "leaf",
    "t": "Arquivo 15 — Dinheiro Trabalhando",
    "b": "Ricos fazem o <strong>dinheiro trabalhar duro</strong> por eles; pobres trabalham duro pelo dinheiro. A meta é a renda passiva cobrir o estilo de vida. Trabalhar a vida toda pelo dinheiro sem pôr o dinheiro a render é o ciclo que não muda.",
    "tip": "<strong>Regra:</strong> cada real da conta FFA, investido, aproxima a independência financeira."
   }
  ]
 },
 "ch09-arquivos-coragem-crescimento": {
  "cards": [
   {
    "ic": "sword",
    "t": "Arquivo 16 — Agir Apesar do Medo",
    "b": "Ricos <strong>agem apesar do medo</strong>; pobres deixam o medo detê-los. Coragem não é ausência de medo — é agir com ele presente. A zona de conforto e a zona de riqueza <strong>não se sobrepõem</strong>.",
    "tip": "<strong>Como aplicar:</strong> aja antes de 'se sentir pronto'; treine para o desconforto — é um músculo."
   },
   {
    "ic": "bulb",
    "t": "Arquivo 17 — Aprender e Crescer Sempre",
    "b": "Ricos estão dispostos a <strong>aprender e crescer</strong> constantemente; pobres acham que já sabem tudo. O objetivo não é só <strong>ter</strong> — é <strong>tornar-se</strong> a pessoa capaz de criar e manter riqueza.",
    "tip": "<strong>Modelo mental:</strong> a maior das fortunas é quem você vira — se perdesse tudo, recuperaria, porque o 'como' está em você."
   },
   {
    "ic": "mountain",
    "t": "Expanda a Zona de Conforto",
    "b": "Cada ação fora da zona de conforto <strong>alarga o que é confortável</strong>. A riqueza começa onde o conforto termina. Confundir conforto com segurança e nunca arriscar nada é o anti-padrão que prende.",
    "tip": "<strong>Sinal de alerta:</strong> esperar o medo passar ou 'estar pronto' — o medo não some, a vida passa."
   }
  ]
 }
}
```
