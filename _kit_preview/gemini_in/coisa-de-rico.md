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

# LIVRO PARA APROFUNDAR: Coisa de Rico — Michel Alcoforado

**Subtítulo:** VISÃO GERAL · OS CÓDIGOS DOS ENDINHEIRADOS BRASILEIROS
**Ideia central:** Ser rico no Brasil não é um número — é uma posição social construída e disputada todos os dias. O antropólogo Michel Alcoforado passou 15 anos e 85 entrevistas decifrando os códigos invisíveis que separam quem 'pertence' de quem apenas tem dinheiro.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-antropologia-do-luxo` — CAPÍTULO 1: A Antropologia do Luxo
- `ch02-auge-da-euforia` — CAPÍTULO 2: O Auge da Euforia — Miami e o Real Forte
- `ch03-operacao-da-diferenca` — CAPÍTULO 3: A Operação da Diferença
- `ch04-medo-da-inseguranca` — CAPÍTULO 4: O Medo da Insegurança
- `ch05-quiet-luxury` — CAPÍTULO 5: A Estética do Quiet Luxury

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-antropologia-do-luxo": {
  "cards": [
   {
    "ic": "book",
    "t": "O Rico Como Objeto de Estudo",
    "b": "Michel Alcoforado usa o método da <strong>observação participante</strong>: 15 anos de convívio, 85 entrevistas, trânsito entre Miami, Europa e os enclaves brasileiros. Para entender a tribo fechada, é preciso <strong>performar um papel legível</strong> por ela.",
    "tip": "<strong>Como aplicar:</strong> para decifrar qualquer mundo social fechado, identifique qual papel você precisa encarnar para ser aceito como interlocutor — o acesso etnográfico se conquista, não se pede."
   },
   {
    "ic": "key",
    "t": "Dinheiro Abre a Porta; Código te Mantém",
    "b": "Dois homens com o mesmo patrimônio. Um pergunta o preço e exibe o cartão. O outro é reconhecido pelo vendedor e vai direto ao provador privado. O que os separa não é a conta — é o <strong>repertório de códigos</strong> (gosto, etiqueta, sobrenome, círculo).",
    "tip": "<strong>Modelo mental:</strong> 'endinheirado' (quem tem dinheiro) ≠ 'rico' (quem pertence). A distinção entre os dois é todo o tema do livro."
   },
   {
    "ic": "layers",
    "t": "Capital Cultural Como Senha",
    "b": "Bourdieu: o domínio de gosto e referências que parece <strong>natural</strong> em quem nasceu no código é a moeda de pertencimento. Esforço aparente em aprender o código <strong>denuncia o recém-chegado</strong>. O natural é o herdado.",
    "tip": "<strong>Para refletir:</strong> que domínios do seu campo você trata como 'óbvios' que são, na verdade, capital cultural acumulado — e que filtram quem 'pertence'?"
   }
  ]
 },
 "ch02-auge-da-euforia": {
  "cards": [
   {
    "ic": "cards",
    "t": "Consumo Como Atestado de Ascensão",
    "b": "No boom dos anos 2010, a viagem de compras a Miami era um <strong>carimbo no passaporte social</strong> — o valor estava no carimbo, não na bagagem. Use: <em>o que esse gasto está certificando?</em> antes de 'quanto custou?'",
    "tip": "<strong>Como aplicar:</strong> em qualquer pico de consumo de luxo, identifique o que ele está certificando socialmente — a função simbólica revela mais que o preço do objeto."
   },
   {
    "ic": "pin",
    "t": "O Cartão Como Classificação",
    "b": "O limite e a cor do cartão de crédito <strong>hierarquizam pessoas</strong>. Instituições financeiras não vendem apenas crédito: vendem <strong>pertencimento</strong> (sala VIP, concierge, acesso exclusivo). O objeto é o veículo; o status é a mercadoria.",
    "tip": "<strong>Modelo mental:</strong> o consumo conspícuo (Veblen) — gastar de forma visível para sinalizar status — é racional dentro da lógica de status; não é vaidade boba, é compra de reconhecimento."
   },
   {
    "ic": "clock",
    "t": "Identidade Ancorada na Conjuntura",
    "b": "Quando o real desvalorizou e Miami ficou inacessível, a <strong>identidade que dependia desse consumo entrou em crise</strong>. Riqueza ancorada em consumo conjuntural fica frágil quando a conjuntura muda.",
    "tip": "<strong>Sinal de alerta:</strong> confundir o auge com permanência — a euforia é cíclica; o que ela construiu de identidade fica exposto quando a maré vira (ver Capítulo 4)."
   }
  ]
 },
 "ch03-operacao-da-diferenca": {
  "cards": [
   {
    "ic": "mask",
    "t": "Performar a Distinção",
    "b": "A elite produz e exibe distinção de forma <strong>contínua e performática</strong>: bairro, escola dos filhos, viagens, vocabulário, marcas — ou ausência deliberada delas. A pergunta-chave é sempre: '<strong>contra quem essa escolha distingue?</strong>'",
    "tip": "<strong>Como aplicar:</strong> mapeie os marcadores que uma pessoa aciona e identifique contra quem cada um a posiciona — a escolha de estar num bairro 'X' fala tanto pelo bairro 'Y' que ela recusou."
   },
   {
    "ic": "person",
    "t": "Ocupados Desocupados",
    "b": "Herdeiros (artistas, curadores, marchands, escritores de sobrenome forte) que vivem de renda mas <strong>se mantêm em movimento constante</strong>. Convertem herança (suspeita) em mérito performado (atividade culta, legítima). O ócio visível é estigma no Brasil desde a criminalização da 'vadiagem'.",
    "tip": "<strong>Para refletir:</strong> que 'ocupação culta' você ou pessoas ao seu redor usam para legitimar privilégios que seriam contestados se ficassem ociosos e visíveis?"
   },
   {
    "ic": "eye",
    "t": "O Esforço Que Denuncia",
    "b": "O domínio de código que parece <strong>natural</strong> é o que separa o herdeiro do recém-chegado. <strong>Esforço aparente em aprender</strong> o código delata a origem. O herdeiro performa ocupação culta; o novo-rico performa poder de compra — a diferença de roteiro denuncia a história.",
    "tip": "<strong>Sinal de alerta:</strong> tentar imitar os marcadores de uma classe sem dominar o código pode ter o efeito oposto — a imitação sem repertório denuncia o esforço."
   }
  ]
 },
 "ch04-medo-da-inseguranca": {
  "cards": [
   {
    "ic": "scale",
    "t": "Riqueza Como Relação",
    "b": "Ser rico é posição <strong>relativa</strong>, medida sempre contra quem está acima. Por isso 'sempre há alguém mais rico' e <strong>ninguém se declara rico</strong>. A régua é móvel — nunca se chega ao topo, então a ansiedade é estrutural.",
    "tip": "<strong>Modelo mental:</strong> pense na riqueza como escada rolante descendente — parar de subir já é cair; daí a corrida sem fim. A insegurança não some com mais zeros."
   },
   {
    "ic": "gap",
    "t": "Insegurança Estrutural da Elite",
    "b": "O medo de queda é <strong>inscrito na lógica relacional</strong> da riqueza — não desaparece com mais patrimônio. Use: '<em>contra quem ela se mede?</em>' para encontrar a fonte real da insegurança, que raramente é a falta objetiva de dinheiro.",
    "tip": "<strong>Para refletir:</strong> você ou alguém que conhece se compara para cima compulsivamente mesmo com patrimônio confortável? Isso é a insegurança estrutural em ação."
   },
   {
    "ic": "triangle",
    "t": "Manutenção de Fachada",
    "b": "Famílias em queda cortam liquidez antes de cortar fachada: vendem joias discretamente, endividam-se, mas mantêm a casa, o clube, a escola cara. <strong>Preservar o sinal de pertencimento</strong> fala mais alto que a saúde financeira real.",
    "tip": "<strong>Sinal de alerta:</strong> quando o custo de manter a aparência corrói o patrimônio que deveria gerar segurança, a fachada virou armadilha."
   }
  ]
 },
 "ch05-quiet-luxury": {
  "cards": [
   {
    "ic": "leaf",
    "t": "O Luxo Que Sussurra",
    "b": "<strong>Quiet luxury</strong>: sofisticação sem logotipo. O valor está na qualidade e na referência, não na marca visível. <strong>Quanto mais sutil o sinal, maior o capital cultural exigido</strong> para decifrá-lo — distinção por filtragem.",
    "tip": "<strong>Modelo mental:</strong> pense no quiet luxury como senha sussurrada — alto demais e qualquer um copia; baixo demais e ninguém ouve. A elite calibra para que só a tribo escute."
   },
   {
    "ic": "eye",
    "t": "Logo vs. Código",
    "b": "Grife visível comunica para a <strong>massa</strong>; ausência de grife comunica para a <strong>tribo</strong>. Logo grande grita 'cheguei'; ausência de logo sussurra 'sempre estive aqui'. A heurística-mestra: '<em>esse sinal fala para a massa ou para a tribo?</em>'",
    "tip": "<strong>Como aplicar:</strong> classifique qualquer escolha estética da elite com essa pergunta — ela revela o nível de capital cultural que o emissor supõe no receptor."
   },
   {
    "ic": "triangle",
    "t": "Estrutura Permanece, Estética Muda",
    "b": "A ostentação virou marca de arrivismo; a discrição virou marca de elite tradicional. Mas a <strong>estrutura competitiva de distinção não mudou</strong>: o jogo continua, só ficou mais difícil de copiar. Imitar o quiet luxury sem o repertório denuncia o esforço.",
    "tip": "<strong>Sinal de alerta:</strong> não confunda 'menos ostentação' com 'menos competição por status' — a ausência de logo não é humildade; é a forma mais sofisticada de jogar o mesmo jogo."
   }
  ]
 }
}
```
