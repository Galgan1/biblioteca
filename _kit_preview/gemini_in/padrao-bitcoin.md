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

# LIVRO PARA APROFUNDAR: O Padrão Bitcoin — Saifedean Ammous

**Subtítulo:** VISÃO GERAL · DINHEIRO FORTE E A HISTÓRIA DO DINHEIRO
**Ideia central:** Para entender o Bitcoin, é preciso primeiro entender o dinheiro. Ammous percorre toda a história monetária — do escambo às conchas, do ouro ao fiat — para extrair a lei que governa todo dinheiro: vence o que é mais difícil de produzir. A régua é a razão estoque/fluxo, e a tese é que o Bitcoin, com oferta absolutamente fixa, é o dinheiro mais forte já inventado.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-dinheiro-vendabilidade` — CAPÍTULO 1: Dinheiro e Vendabilidade
- `ch02-estoque-fluxo` — CAPÍTULO 2: Estoque, Fluxo e a Moeda Forte
- `ch03-moedas-primitivas` — CAPÍTULO 3: Moedas Primitivas
- `ch04-metais-monetarios` — CAPÍTULO 4: Os Metais Monetários
- `ch05-dinheiro-governamental` — CAPÍTULO 5: O Dinheiro Governamental
- `ch06-preferencia-temporal` — CAPÍTULO 6: Dinheiro e Preferência Temporal
- `ch07-ciclos-economicos` — CAPÍTULO 7: O Sistema de Informação do Capitalismo
- `ch08-dinheiro-solido-liberdade` — CAPÍTULO 8: Dinheiro Sólido e Liberdade
- `ch09-bitcoin-dinheiro-digital` — CAPÍTULO 9: O Dinheiro Digital (Bitcoin)
- `ch10-para-que-serve-bitcoin` — CAPÍTULO 10: Para Que Serve o Bitcoin

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-dinheiro-vendabilidade": {
  "cards": [
   {
    "ic": "target",
    "t": "Vendabilidade (Carl Menger)",
    "b": "A facilidade de vender um bem com a <strong>menor perda de valor</strong>. Três faces: <strong>escala</strong> (divisível), <strong>espaço</strong> (transportável) e <strong>tempo</strong> (mantém valor) — esta é a decisiva.",
    "tip": "<strong>Como aplicar:</strong> o melhor dinheiro é o mais vendável no tempo."
   },
   {
    "ic": "fork",
    "t": "O Problema do Escambo",
    "b": "A troca direta falha por falta de coincidência: <strong>em escala</strong> (o sapato não compra a casa em pedaços), <strong>no tempo</strong> (o perecível não acumula até o durável) e <strong>no espaço</strong> (a casa não se transporta).",
    "tip": "<strong>Saída:</strong> a troca indireta — adquirir um bem intermediário que todos aceitam (dinheiro)."
   },
   {
    "ic": "book",
    "t": "As Duas Funções",
    "b": "<strong>Meio de troca</strong> (a função-mãe: comprar não para consumir, mas para trocar depois) e <strong>reserva de valor</strong> (transportar poder de compra ao futuro).",
    "tip": "<strong>Cuidado:</strong> dinheiro ≠ investimento — investimento dá ganho, tem risco e é menos líquido."
   },
   {
    "ic": "scale",
    "t": "Unidade de Conta",
    "b": "A terceira função <strong>emerge das duas primeiras</strong>: quando um bem vira meio de troca, todos os preços passam a ser medidos nele. Não há unidade de conta sem antes ser o bem mais vendável.",
    "tip": "<strong>Modelo mental:</strong> o dinheiro é a régua dos preços — e só vira régua quem já é o mais líquido."
   },
   {
    "ic": "eye",
    "t": "O Dinheiro Não é Inventado",
    "b": "Menger mostrou que o dinheiro <strong>emerge espontaneamente do mercado</strong>: cada um aceita o bem mais fácil de revender, e a convergência elege um só. O Estado reconhece o dinheiro — não o cria.",
    "tip": "<strong>Lição:</strong> bom dinheiro é descoberto por milhões de escolhas, não decretado."
   },
   {
    "ic": "wave",
    "t": "O Prêmio de Liquidez",
    "b": "O bem mais vendável ganha um <strong>valor extra</strong> só por ser aceito por todos — demanda monetária acima do uso prático. Foi assim que o ouro valeu muito mais que sua utilidade industrial.",
    "tip": "<strong>Cuidado:</strong> esse prêmio evapora se a oferta do bem fica fácil de aumentar."
   }
  ]
 },
 "ch02-estoque-fluxo": {
  "cards": [
   {
    "ic": "scale",
    "t": "Estoque / Fluxo",
    "b": "<strong>Estoque</strong> = tudo já produzido (menos o consumido). <strong>Fluxo</strong> = a produção nova de um período. Razão <strong>alta</strong> = nem um grande aumento de produção move o total = o valor resiste.",
    "tip": "<strong>Regra:</strong> mede-se a força pela oferta FUTURA (o fluxo), não pela foto atual."
   },
   {
    "ic": "clock",
    "t": "A Armadilha da Moeda Fraca",
    "b": "Tudo que vira reserva atrai produção; se a produção é fácil, ela <strong>expropria quem poupou</strong>. Corolário: todo dinheiro que dura é <strong>caro de produzir</strong>.",
    "tip": "<strong>Sinal de alerta:</strong> oferta fácil de inflar = riqueza fácil de evaporar."
   },
   {
    "ic": "target",
    "t": "A Régua na Prática",
    "b": "O ouro nunca teve a oferta crescendo mais que ~<strong>1,5% ao ano</strong> — por isso resiste como nenhum outro. A prata cresce mais rápido; bens de consumo têm a oferta acompanhando a demanda quase 1:1.",
    "tip": "<strong>Modelo mental:</strong> estoque/fluxo alto = 'mesmo todo mundo cavando, mal move o total'."
   },
   {
    "ic": "steps",
    "t": "Seleção Natural Monetária",
    "b": "Numa competição entre reservas de valor, quem produz a moeda barato dilui todos os outros. Sobrevive a que <strong>ninguém consegue inflar</strong> — a de maior estoque/fluxo.",
    "tip": "<strong>Como aplicar:</strong> antes de poupar em algo, pergunte 'quão fácil é fabricar mais disto?'."
   },
   {
    "ic": "key",
    "t": "Moeda Sonante",
    "b": "A moeda forte <strong>emerge pela escolha livre do mercado</strong> e seu valor é determinado pelo mercado, não pelo decreto. A competição sempre tende ao dinheiro mais forte.",
    "tip": "<strong>Modelo mental:</strong> o fluxo é o inimigo do poupador."
   },
   {
    "ic": "wrench",
    "t": "A Lei de Gresham",
    "b": "Quando o Estado força as duas a valerem igual (curso legal), a <strong>moeda fraca expulsa a forte de circulação</strong>: gasta-se a ruim e entesoura-se a boa.",
    "tip": "<strong>Cuidado:</strong> isso só acontece sob decreto — no mercado livre, a forte vence."
   }
  ]
 },
 "ch03-moedas-primitivas": {
  "cards": [
   {
    "ic": "mountain",
    "t": "Pedras de Yap e Conchas",
    "b": "As pedras de Rai foram dinheiro por séculos porque eram dificílimas de obter — até alguém com ferramentas modernas produzi-las em massa. Conchas: dinheiro enquanto raras; a importação em massa destruiu seu valor.",
    "tip": "<strong>Lição:</strong> a escassez de hoje não garante a de amanhã."
   },
   {
    "ic": "wave",
    "t": "A Regra da Oferta Súbita",
    "b": "Um meio monetário sobrevive enquanto o fluxo é pequeno; quando um avanço dispara a oferta, o bem <strong>perde o status de dinheiro</strong>.",
    "tip": "<strong>Modelo mental:</strong> a tecnologia é a juíza silenciosa do dinheiro."
   },
   {
    "ic": "eye",
    "t": "Transferência de Riqueza",
    "b": "Em toda moeda primitiva, quem conseguia <strong>produzir o bem barato</strong> trocava-o por bens reais de quem poupava nele — expropriando-os.",
    "tip": "<strong>Cuidado:</strong> dinheiro fraco é um mecanismo silencioso de transferência de riqueza."
   },
   {
    "ic": "link",
    "t": "As Contas de Vidro da África",
    "b": "Europeus produziam contas de vidro <strong>baratíssimas</strong> e as trocavam por ouro, marfim e pessoas escravizadas. Para os africanos eram raras (dinheiro forte); para os europeus, triviais — uma das maiores expropriações da história.",
    "tip": "<strong>Lição:</strong> quem tem o dinheiro mais difícil drena a riqueza de quem tem o mais fácil."
   },
   {
    "ic": "sword",
    "t": "Dinheiro Difícil Conquista o Fácil",
    "b": "Repetidamente, sociedades com moeda mais forte <strong>subjugaram</strong> as de moeda mais fraca — economicamente e militarmente. A dureza monetária foi vantagem civilizacional.",
    "tip": "<strong>Modelo mental:</strong> a escolha do dinheiro não é técnica — é questão de sobrevivência."
   },
   {
    "ic": "clock",
    "t": "O Padrão se Repete",
    "b": "Gado, sal, contas, conchas, metais: cada um reinou e caiu pela <strong>mesma causa única</strong> — a oferta deixou de ser difícil.",
    "tip": "<strong>Como aplicar:</strong> ao avaliar qualquer 'novo dinheiro', olhe o que acontece com a oferta quando a demanda sobe."
   }
  ]
 },
 "ch04-metais-monetarios": {
  "cards": [
   {
    "ic": "target",
    "t": "Por que o Ouro Venceu",
    "b": "<strong>Indestrutibilidade</strong> → quase todo ouro já garimpado ainda existe (estoque cumulativo). <strong>Produção mínima</strong> → fluxo ínfimo frente ao estoque. Resultado: a maior razão estoque/fluxo = o melhor reserva de valor.",
    "tip": "<strong>Lição:</strong> o ouro venceu por durar, não por brilhar."
   },
   {
    "ic": "scale",
    "t": "A Derrota da Prata",
    "b": "A prata teve seu papel (mais divisível para o dia a dia), mas sua oferta cresce mais rápido e ela <strong>oxida e se consome</strong>. Quando foi desmonetizada, quem poupava nela empobreceu.",
    "tip": "<strong>Modelo mental:</strong> entre dois metais, vence o de menor crescimento de oferta."
   },
   {
    "ic": "steps",
    "t": "O Padrão-Ouro Clássico",
    "b": "De ~1871 a 1914: com o ouro como âncora, os preços eram estáveis no longo prazo, a poupança valia e o capital se acumulava — a 'Belle Époque' de inovação, livre-comércio e baixa preferência temporal.",
    "tip": "<strong>Como aplicar:</strong> dinheiro forte como base da prosperidade duradoura."
   },
   {
    "ic": "wrench",
    "t": "A Âncora Disciplina o Estado",
    "b": "Sob o ouro, déficits causavam <strong>saída de ouro</strong> e forçavam o ajuste automático. O governo não podia gastar além do que arrecadava sem sentir o freio.",
    "tip": "<strong>Lição:</strong> o ouro impunha honestidade fiscal sem precisar de promessa política."
   },
   {
    "ic": "gap",
    "t": "O Calcanhar de Aquiles",
    "b": "O ouro é pesado e difícil de transportar/verificar — o que forçou a <strong>centralização em cofres de bancos</strong>. E foi essa centralização que abriu a porta para o Estado confiscá-lo.",
    "tip": "<strong>Sinal de alerta:</strong> resolver a fraqueza do peso centralizando foi o pecado original."
   },
   {
    "ic": "book",
    "t": "Papel Lastreado: a Brecha",
    "b": "As notas 'resgatáveis em ouro' eram convenientes — mas permitiram emitir <strong>mais papel do que havia metal</strong>. A conveniência preparou o terreno para romper a âncora.",
    "tip": "<strong>Cuidado:</strong> toda camada de abstração sobre o dinheiro forte é uma chance de inflá-lo."
   }
  ]
 },
 "ch05-dinheiro-governamental": {
  "cards": [
   {
    "ic": "wrench",
    "t": "A Captura do Ouro",
    "b": "Como o ouro estava em cofres centrais, bastou suspender a conversibilidade e <strong>emitir papel além das reservas</strong>. A Primeira Guerra é o marco: os países abandonaram o padrão-ouro para imprimir e financiar o conflito.",
    "tip": "<strong>Modelo mental:</strong> quando a régua é elástica, a estabilidade vira promessa política."
   },
   {
    "ic": "clock",
    "t": "Inflação como Imposto Invisível",
    "b": "Emitir moeda nova transfere poder de compra de quem poupa para <strong>quem recebe o dinheiro novo primeiro</strong> (o Estado e os próximos da fonte). É o <strong>Efeito Cantillon</strong> — tributação sem voto.",
    "tip": "<strong>Cuidado:</strong> inflação é transferência, não geração de riqueza."
   },
   {
    "ic": "gap",
    "t": "1971: o Fim da Âncora",
    "b": "Bretton Woods atou as moedas ao dólar e o dólar ao ouro. Em 1971, Nixon 'suspendeu temporariamente' a conversão — e a suspensão <strong>nunca acabou</strong>. Desde então, o mundo vive sob fiat puro.",
    "tip": "<strong>Lição:</strong> 'temporário' em política monetária costuma significar permanente."
   },
   {
    "ic": "book",
    "t": "Curso Legal",
    "b": "Imposição estatal de que a moeda seja aceita — o <strong>oposto da moeda sonante</strong>, que o mercado escolhe. Ser obrigatório denuncia que o mercado não a escolheria.",
    "tip": "<strong>Sinal de alerta:</strong> 'um pouco de inflação é saudável' = normalização do confisco gradual."
   },
   {
    "ic": "spiral",
    "t": "O Fim do Jogo: Hiperinflação",
    "b": "Sem limite físico, a tentação de imprimir não tem freio. Weimar, Zimbábue, Venezuela: quando a confiança quebra, a moeda <strong>colapsa por completo</strong> e a poupança de gerações evapora.",
    "tip": "<strong>Cuidado:</strong> toda hiperinflação começou como 'só um pouco' de emissão."
   },
   {
    "ic": "eye",
    "t": "O Calote Silencioso",
    "b": "Governos preferem inflar a dar calote honesto: a dívida é paga em moeda que <strong>vale cada vez menos</strong>. O credor recebe o número, não o valor.",
    "tip": "<strong>Modelo mental:</strong> a inflação é um default que não precisa ser declarado."
   }
  ]
 },
 "ch06-preferencia-temporal": {
  "cards": [
   {
    "ic": "clock",
    "t": "Preferência Temporal",
    "b": "Quanto se valoriza o presente sobre o futuro. <strong>Baixa</strong> = paciência, poupança, planejamento; <strong>alta</strong> = impaciência, consumo imediato, dívida. O dinheiro forte recompensa adiar; o fraco pune.",
    "tip": "<strong>Como aplicar:</strong> o dinheiro é um sinal de paciência — molda a cultura, não só os preços."
   },
   {
    "ic": "steps",
    "t": "A Escada da Civilização",
    "b": "Baixa preferência temporal → <strong>poupança</strong> → acúmulo de <strong>capital</strong> → mais produtividade → tempo livre para ciência, arte e família. O dinheiro forte estaria na base.",
    "tip": "<strong>Modelo mental:</strong> civilizações de dinheiro forte fazem obras para durar séculos."
   },
   {
    "ic": "key",
    "t": "Poupar é Plantar",
    "b": "Guardar valor com segurança é o que permite <strong>investir no eu futuro</strong>: estudo, saúde, ferramentas, negócios. A poupança é a semente de todo capital.",
    "tip": "<strong>Lição:</strong> sem reserva de valor confiável, ninguém tem motivo para adiar a gratificação."
   },
   {
    "ic": "mountain",
    "t": "A Arte que Dura",
    "b": "Ammous liga o dinheiro forte às catedrais, à Renascença e à arte feita <strong>para durar séculos</strong>. Sob fiat, a produção tende ao descartável e ao imediato.",
    "tip": "<strong>Modelo mental:</strong> o horizonte de tempo de uma cultura aparece no que ela constrói."
   },
   {
    "ic": "eye",
    "t": "A Cultura do Imediato",
    "b": "Inflação reeduca a sociedade para <strong>gastar e se endividar</strong> — o consumo financiado por dívida é o futuro pagando o presente, não riqueza nova.",
    "tip": "<strong>Cuidado:</strong> você compete com o seu eu futuro; dinheiro que apodrece o expropria."
   },
   {
    "ic": "target",
    "t": "O Juro Nasce da Poupança",
    "b": "Quando muita gente poupa (baixa preferência temporal), os juros caem <strong>naturalmente</strong> e há capital barato para projetos longos. É o oposto de baixar o juro por decreto (cap. 7).",
    "tip": "<strong>Lição:</strong> juro saudável é fruto de poupança real, não de impressora."
   }
  ]
 },
 "ch07-ciclos-economicos": {
  "cards": [
   {
    "ic": "target",
    "t": "Juros como Sinal",
    "b": "A taxa de juros comunica <strong>quanta poupança real existe</strong> para investir. Juro alto = poupe mais antes; juro baixo = há recursos para projetos longos. Baixá-lo por decreto é <strong>mentir ao mercado</strong>.",
    "tip": "<strong>Modelo mental:</strong> juro é um preço — mexer nele à força cega a economia."
   },
   {
    "ic": "spiral",
    "t": "Boom → Bust",
    "b": "Crédito fácil gera um <strong>boom</strong> de investimentos insustentáveis; quando se revela que a poupança real não existe, vem o <strong>bust</strong> — a correção que liquida os erros.",
    "tip": "<strong>Lição:</strong> a recessão não é a doença; é a cura."
   },
   {
    "ic": "book",
    "t": "A Teoria Austríaca",
    "b": "Mises e Hayek (Nobel de 1974) mostraram que o ciclo nasce da <strong>expansão artificial do crédito</strong>, não de um defeito do mercado. O dinheiro fácil é a causa, não o remédio.",
    "tip": "<strong>Como aplicar:</strong> ao ouvir 'falha de mercado', pergunte quem manipulou o juro antes."
   },
   {
    "ic": "wrench",
    "t": "Capital Mal Alocado",
    "b": "Com juro falso, projetos que só parecem lucrativos a essa taxa atraem capital, trabalho e recursos. O bust <strong>revela o desperdício</strong> — fábricas, imóveis e empresas que não deviam existir.",
    "tip": "<strong>Modelo mental:</strong> o estrago se faz no boom; o bust apenas o expõe."
   },
   {
    "ic": "eye",
    "t": "Quem Paga o Boom",
    "b": "O crédito novo não é poupança — é dinheiro criado. Ele transfere recursos para <strong>quem o recebe primeiro</strong> e deixa a conta (inflação e crise) para o resto.",
    "tip": "<strong>Cuidado:</strong> crescimento por dívida barata é riqueza emprestada do futuro."
   },
   {
    "ic": "clock",
    "t": "O Erro do Estímulo",
    "b": "Tratar a recessão como o inimigo a combater com <strong>mais estímulo</strong> apenas semeia o próximo ciclo, maior. A 'cura' vira a causa.",
    "tip": "<strong>Cuidado:</strong> PIB inflado por dívida não é riqueza real."
   }
  ]
 },
 "ch08-dinheiro-solido-liberdade": {
  "cards": [
   {
    "ic": "scale",
    "t": "Dinheiro Forte = Freio ao Poder",
    "b": "Sob o padrão-ouro, o Estado só gasta o que <strong>arrecada ou toma emprestado abertamente</strong> — e o povo sente o custo, o que gera resistência. O fiat remove esse freio: gasta-se e guerreia-se sem aprovação direta.",
    "tip": "<strong>Modelo mental:</strong> quem controla a régua do valor, controla a sociedade."
   },
   {
    "ic": "steps",
    "t": "O Crescimento do Leviatã",
    "b": "Foi sob o fiat que o Estado <strong>explodiu de tamanho</strong> no séc. XX. Sem o limite do ouro, programas e burocracias crescem financiados pela impressora, não pelo consentimento do contribuinte.",
    "tip": "<strong>Lição:</strong> o tamanho do governo acompanha a elasticidade do dinheiro."
   },
   {
    "ic": "sword",
    "t": "Guerra e Fiat",
    "b": "A escala industrial das guerras do séc. XX só foi possível porque os Estados podiam <strong>imprimir</strong>. O ouro as teria abreviado — a diferença entre uma guerra de meses e uma de anos.",
    "tip": "<strong>Cuidado:</strong> a guerra total é financiada pela inflação, não pelo imposto declarado."
   },
   {
    "ic": "eye",
    "t": "Inflação e Desigualdade",
    "b": "O dinheiro novo chega primeiro a bancos e aos próximos do poder (Efeito Cantillon), que compram ativos <strong>antes dos preços subirem</strong>. O assalariado recebe por último — concentração de riqueza embutida.",
    "tip": "<strong>Modelo mental:</strong> nem toda desigualdade é de mercado; parte é desenhada pela emissão."
   },
   {
    "ic": "key",
    "t": "Poupança é Liberdade Estocada",
    "b": "Poder guardar valor com segurança permite <strong>dizer não, esperar, escolher</strong>. Quando a poupança apodrece, o indivíduo perde independência e fica mais dependente do Estado e do crédito.",
    "tip": "<strong>Como aplicar:</strong> destruir a reserva de valor é destruir a soberania do indivíduo."
   },
   {
    "ic": "book",
    "t": "O Mecenas e o Estado",
    "b": "Sob dinheiro forte, ciência e arte eram bancadas por <strong>poupança e mecenato privado</strong>. Sob fiat, passam a depender de subsídio estatal — e da agenda de quem o concede.",
    "tip": "<strong>Lição:</strong> quem financia a cultura molda a cultura."
   }
  ]
 },
 "ch09-bitcoin-dinheiro-digital": {
  "cards": [
   {
    "ic": "spiral",
    "t": "Escassez Absoluta (21 milhões)",
    "b": "A oferta total é <strong>fixa por código</strong>; nenhum governo, banco ou maioria pode emitir mais. O oposto do fiat, cuja oferta é, por definição, ilimitada.",
    "tip": "<strong>Chave:</strong> pela 1ª vez, a oferta é perfeitamente inelástica à demanda."
   },
   {
    "ic": "layers",
    "t": "Prova de Trabalho + Dificuldade Ajustável",
    "b": "Mineradores gastam <strong>energia real</strong> para validar e emitir — o 'custo de produção' que protege a moeda. E a <strong>dificuldade se ajusta</strong>: se mais poder entra, a emissão segue o cronograma — a oferta NÃO acelera.",
    "tip": "<strong>Modelo mental:</strong> a armadilha da moeda fraca foi tornada impossível por design."
   },
   {
    "ic": "clock",
    "t": "O Cronograma dos Halvings",
    "b": "A emissão cai pela metade a cada ~4 anos (210.000 blocos), até a última fração de moeda por volta de <strong>2140</strong>. O fluxo só encolhe — a razão estoque/fluxo só sobe, ultrapassando o ouro.",
    "tip": "<strong>Lição:</strong> a política monetária do Bitcoin é conhecida até o último satoshi."
   },
   {
    "ic": "link",
    "t": "Descentralização",
    "b": "A rede é mantida por <strong>milhares de nós independentes</strong>; alterar a oferta exigiria consenso impossível. Não há ponto único para o Estado capturar — a falha do ouro centralizado, resolvida.",
    "tip": "<strong>Lição:</strong> confiança substituída por verificação — você audita, não confia."
   },
   {
    "ic": "key",
    "t": "Autocustódia = Soberania",
    "b": "Quem detém as <strong>chaves privadas</strong> detém o dinheiro, sem depender de banco ou custodiante. É a posse direta que o ouro físico prometia, sem o peso nem o cofre.",
    "tip": "<strong>Cuidado:</strong> 'not your keys, not your coins' — em corretora, você tem uma promessa, não o ativo."
   },
   {
    "ic": "eye",
    "t": "Resistência à Censura",
    "b": "Transações e saldos <strong>não podem ser bloqueados ou confiscados</strong> por decreto enquanto você controla as chaves. É dinheiro que não pede permissão.",
    "tip": "<strong>Modelo mental:</strong> o que não pode ser apreendido não pode ser usado como alavanca contra você."
   }
  ]
 },
 "ch10-para-que-serve-bitcoin": {
  "cards": [
   {
    "ic": "target",
    "t": "Reserva de Valor Soberana",
    "b": "Um ativo que ninguém pode <strong>confiscar, inflar ou congelar</strong> — poupança fora do alcance de qualquer Estado ou banco. É o caso de uso primário do livro.",
    "tip": "<strong>Como aplicar:</strong> pense em ouro digital — o concorrente é a reserva de valor, não o meio de pagamento."
   },
   {
    "ic": "layers",
    "t": "Camada de Liquidação",
    "b": "Cada transação na base é cara e definitiva — como a liquidação entre bancos centrais. A <strong>escala vem de camadas superiores</strong> (rápidas, baratas), não de inchar a base.",
    "tip": "<strong>Modelo mental:</strong> a base resolve confiança; as camadas resolvem velocidade."
   },
   {
    "ic": "key",
    "t": "Poupança de Longo Prazo",
    "b": "O uso realista para o indivíduo é <strong>guardar</strong>, não negociar: estocar poder de compra por anos, imune à inflação. O comportamento certo é o do poupador paciente, não do especulador.",
    "tip": "<strong>Lição:</strong> baixa preferência temporal aplicada — comprar para deter, não para girar."
   },
   {
    "ic": "link",
    "t": "Ativo ao Portador, Sem Contraparte",
    "b": "Diferente de um depósito ou título, o Bitcoin <strong>não é dívida de ninguém</strong>: não há banco que possa quebrar, congelar ou não honrar. Você detém o ativo, não a promessa de alguém.",
    "tip": "<strong>Modelo mental:</strong> sem contraparte = sem o risco de o outro lado falhar."
   },
   {
    "ic": "wave",
    "t": "Volatilidade = Preço da Adoção",
    "b": "Como ativo monetário jovem em monetização, oscila muito — é o <strong>custo de ser cedo</strong>, e tende a diminuir conforme cresce e se torna líquido.",
    "tip": "<strong>Cuidado:</strong> só arrisque o que aguenta a volatilidade; o horizonte é de anos, não de semanas."
   },
   {
    "ic": "eye",
    "t": "O que o Bitcoin NÃO é",
    "b": "Não é investimento 'que só sobe', não é dinheiro barato de varejo, não é isento de risco. <strong>Tratá-lo como qualquer dessas coisas leva a erro.</strong>",
    "tip": "<strong>Cuidado:</strong> confundir reserva de valor com varejo (ou com retorno garantido) é a porta da especulação ingênua."
   }
  ]
 }
}
```
