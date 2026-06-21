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

# LIVRO PARA APROFUNDAR: O Homem Mais Rico da Babilônia — George S. Clason

**Subtítulo:** VISÃO GERAL · OS SEGREDOS ATEMPORAIS DA RIQUEZA
**Ideia central:** Em parábolas ambientadas na antiga Babilônia, George Clason traduz princípios financeiros em regras simples e atemporais. O fio que costura todas as histórias é uma frase: "uma parte de tudo que você ganha é sua para guardar". Não é o tamanho do salário que enriquece — é o hábito de pagar a si mesmo primeiro, controlar gastos, multiplicar o ouro e protegê-lo de perdas.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-homem-que-desejava-ouro` — CAPÍTULO 1: O Homem que Desejava Ouro
- `ch02-homem-mais-rico` — CAPÍTULO 2: O Homem Mais Rico da Babilônia
- `ch03-sete-curas` — CAPÍTULO 3: As Sete Curas para uma Bolsa Vazia
- `ch04-deusa-da-boa-sorte` — CAPÍTULO 4: Conheça a Deusa da Boa Sorte
- `ch05-cinco-leis-do-ouro` — CAPÍTULO 5: As Cinco Leis do Ouro
- `ch06-emprestador-de-ouro` — CAPÍTULO 6: O Emprestador de Ouro da Babilônia
- `ch07-muralhas-da-babilonia` — CAPÍTULO 7: As Muralhas da Babilônia
- `ch08-mercador-de-camelos` — CAPÍTULO 8: O Mercador de Camelos da Babilônia
- `ch09-tabuas-de-argila-e-trabalho` — CAPÍTULO 9: As Tábuas de Argila e a Sorte Maior

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-homem-que-desejava-ouro": {
  "cards": [
   {
    "ic": "gap",
    "t": "Trabalhar Duro ≠ Enriquecer",
    "b": "Esforço sozinho não cria riqueza. Quem nunca <strong>aprendeu as leis do dinheiro</strong> permanece pobre por mais que sue. A diferença entre o rico e o pobre é o <strong>conhecimento dos princípios</strong>, não a quantidade de trabalho.",
    "tip": "<strong>Como aplicar:</strong> antes de buscar ganhar mais, aprenda a guardar e multiplicar o que já ganha."
   },
   {
    "ic": "bulb",
    "t": "A Insatisfação como Ponto de Partida",
    "b": "Bansir e Kobbi reconhecem que estão presos no mesmo lugar há anos. <strong>Admitir a pobreza e querer mudá-la</strong> é o primeiro passo — quem se conforma nunca procura o caminho.",
    "tip": "<strong>Modelo mental:</strong> use o desconforto com o presente como combustível para procurar quem já tem o que você quer."
   },
   {
    "ic": "target",
    "t": "Procure Quem Sabe",
    "b": "Em vez de invejar Arkad, os amigos decidem <strong>ir perguntar a ele</strong> como ficou rico. Aprenda com quem já chegou lá, não com quem só reclama.",
    "tip": "<strong>Cuidado:</strong> pedir conselho financeiro a quem também é pobre — eles ensinam os hábitos que os mantêm pobres."
   }
  ]
 },
 "ch02-homem-mais-rico": {
  "cards": [
   {
    "ic": "key",
    "t": "\"Uma Parte de Tudo que Você Ganha é Sua para Guardar\"",
    "b": "O segredo de Arkad: do que você ganha, <strong>pague a si mesmo primeiro</strong> — guarde no mínimo <strong>1/10</strong> antes de pagar qualquer outra pessoa. Você trabalha para o sapateiro, o alfaiate e todos os outros; comece a trabalhar para você.",
    "tip": "<strong>Como aplicar:</strong> ao receber, separe 10% imediatamente e viva com os 90% restantes — você nem sentirá falta."
   },
   {
    "ic": "leaf",
    "t": "Faça o Ouro Trabalhar por Você",
    "b": "O ouro guardado deve <strong>gerar mais ouro</strong>: cada moeda poupada é um \"escravo\" que trabalha, e seus filhos (os juros) também trabalham. Riqueza é uma <strong>árvore que cresce do dízimo guardado</strong>.",
    "tip": "<strong>Modelo mental:</strong> reinvista os rendimentos; não gaste os \"filhos\" do seu ouro."
   },
   {
    "ic": "mask",
    "t": "Conselho de Quem Não Entende",
    "b": "Arkad perdeu suas primeiras economias seguindo o conselho de Azmur, o <strong>fabricante de tijolos</strong>, sobre comprar joias — algo que ele não dominava. Peça conselho a quem é <strong>competente no assunto</strong>.",
    "tip": "<strong>Sinal de alerta:</strong> aceitar dica de investimento de quem não tem experiência comprovada naquele campo."
   }
  ]
 },
 "ch03-sete-curas": {
  "cards": [
   {
    "ic": "steps",
    "t": "As Sete Curas (o programa completo)",
    "b": "<strong>1.</strong> Comece a engordar a bolsa (guarde 10%). <strong>2.</strong> Controle os gastos. <strong>3.</strong> Multiplique o ouro (invista). <strong>4.</strong> Proteja o tesouro de perdas. <strong>5.</strong> Faça da casa um bom investimento. <strong>6.</strong> Garanta renda futura. <strong>7.</strong> Aumente sua capacidade de ganhar.",
    "tip": "<strong>Como aplicar:</strong> trate como uma escada — domine cada cura antes de subir para a próxima."
   },
   {
    "ic": "fork",
    "t": "Cura 2 — Desejos ≠ Necessidades",
    "b": "\"Gastos necessários\" crescem para consumir toda a renda, se você deixar. <strong>Orce o essencial</strong> e perceba que muitos \"desejos\" se disfarçam de necessidades — você não pode satisfazer todos.",
    "tip": "<strong>Regra:</strong> escreva o orçamento; gaste em necessidades e nos desejos mais valiosos, dentro dos 90%."
   },
   {
    "ic": "scale",
    "t": "Cura 4 — Proteja o Principal",
    "b": "A primeira regra do investimento é <strong>não perder o que se tem</strong>. Só aplique onde o <strong>principal está seguro</strong> e onde você pode recuperá-lo; um retorno alto não compensa o risco de perder tudo.",
    "tip": "<strong>Sinal de alerta:</strong> promessas de lucro irreal que ignoram a segurança do capital."
   }
  ]
 },
 "ch04-deusa-da-boa-sorte": {
  "cards": [
   {
    "ic": "spark",
    "t": "A Sorte Segue a Ação",
    "b": "A deusa da boa sorte favorece <strong>quem age sobre uma oportunidade</strong>, não quem aposta em dados. As maiores chances vêm disfarçadas de trabalho ou negócio — e exigem decisão rápida.",
    "tip": "<strong>Como aplicar:</strong> quando uma oportunidade boa aparece, prepare-se e aja — não a deixe esfriar."
   },
   {
    "ic": "clock",
    "t": "O Procrastinador Espanta a Sorte",
    "b": "O \"espírito da procrastinação\" mora em todo homem e <strong>mata as oportunidades</strong> com o \"depois eu vejo\". A boa sorte raramente espera o indeciso.",
    "tip": "<strong>Cuidado:</strong> adiar a decisão sobre uma boa oportunidade equivale a recusá-la."
   },
   {
    "ic": "target",
    "t": "Atraia a Sorte com Preparo",
    "b": "Sorte não é puro acaso: é o encontro de <strong>oportunidade com quem está pronto</strong> para agarrá-la. Estar poupado, informado e disposto multiplica a \"sorte\".",
    "tip": "<strong>Modelo mental:</strong> a sorte é o ponto em que preparo e oportunidade se cruzam."
   }
  ]
 },
 "ch05-cinco-leis-do-ouro": {
  "cards": [
   {
    "ic": "layers",
    "t": "As Cinco Leis do Ouro",
    "b": "<strong>1.</strong> O ouro vem com prazer a quem guarda ao menos 1/10 para a família. <strong>2.</strong> O ouro trabalha com diligência para quem o emprega bem. <strong>3.</strong> O ouro fica com quem o investe com conselho sábio. <strong>4.</strong> O ouro escapa de quem investe no que não entende. <strong>5.</strong> O ouro foge de quem busca lucros impossíveis.",
    "tip": "<strong>Como aplicar:</strong> use as 5 leis como checklist antes de qualquer aplicação."
   },
   {
    "ic": "eye",
    "t": "Lei 4 — Não Invista no que Não Entende",
    "b": "O ouro <strong>escapa</strong> de quem o aplica em negócios que desconhece ou que \"especialistas\" desaprovam. Domínio do assunto é proteção; ignorância é perda quase certa.",
    "tip": "<strong>Regra:</strong> só invista onde você (ou um conselheiro confiável) realmente entende o negócio."
   },
   {
    "ic": "sword",
    "t": "Lei 5 — Cuidado com Lucros Impossíveis",
    "b": "O ouro <strong>foge</strong> de quem persegue retornos românticos e impossíveis, ou confia em trapaceiros e na própria inexperiência. Ganância é a porta da ruína.",
    "tip": "<strong>Sinal de alerta:</strong> qualquer proposta que prometa enriquecimento rápido e garantido."
   }
  ]
 },
 "ch06-emprestador-de-ouro": {
  "cards": [
   {
    "ic": "scale",
    "t": "Avalie a Segurança Antes do Lucro",
    "b": "Antes de emprestar ou investir, pergunte: <strong>o principal está seguro? Posso reavê-lo?</strong> A melhor garantia é um bem de valor ou um devedor com histórico e capacidade de pagar.",
    "tip": "<strong>Como aplicar:</strong> exija garantia real e avalie o caráter e a renda de quem recebe seu dinheiro."
   },
   {
    "ic": "bubble",
    "t": "Ajudar ≠ Dar o seu Ouro",
    "b": "Emprestar a parentes e amigos sem critério costuma <strong>perder o ouro e o amigo</strong>. A boa intenção não substitui a garantia; às vezes o melhor auxílio não é dinheiro.",
    "tip": "<strong>Cuidado:</strong> ceder à pressão emocional e emprestar a quem não tem como pagar."
   },
   {
    "ic": "key",
    "t": "Conselho de Quem Lida com Dinheiro",
    "b": "Mathon recomenda buscar a opinião de <strong>quem lida com risco profissionalmente</strong>. A experiência de quem já emprestou muito é um seguro contra perdas.",
    "tip": "<strong>Modelo mental:</strong> consulte quem tem cicatrizes no assunto antes de arriscar."
   }
  ]
 },
 "ch07-muralhas-da-babilonia": {
  "cards": [
   {
    "ic": "mountain",
    "t": "Toda Pessoa Precisa de Muralhas",
    "b": "As muralhas que protegeram a Babilônia simbolizam a <strong>proteção financeira</strong>: seguros, poupança de emergência e investimentos confiáveis que <strong>nos blindam contra a tragédia inesperada</strong>.",
    "tip": "<strong>Como aplicar:</strong> construa uma reserva de emergência antes de pensar em luxos — é a sua muralha."
   },
   {
    "ic": "wave",
    "t": "O Imprevisto é Certo",
    "b": "Cedo ou tarde, todos enfrentam um \"cerco\": doença, desemprego, crise. <strong>Quem tem reserva resiste; quem não tem, cai.</strong>",
    "tip": "<strong>Regra:</strong> não conte com a sorte; conte com a muralha que você construiu."
   }
  ]
 },
 "ch08-mercador-de-camelos": {
  "cards": [
   {
    "ic": "pivot",
    "t": "O Plano de Dabasir (70 / 20 / 10)",
    "b": "Divida toda a renda em três partes: <strong>70% para viver</strong>, <strong>20% para pagar as dívidas</strong> (rateadas entre os credores) e <strong>10% para guardar (pagar-se primeiro)</strong>. Mantido com disciplina, o plano quita as dívidas e ainda enriquece.",
    "tip": "<strong>Como aplicar:</strong> liste seus credores, distribua os 20% proporcionalmente e nunca pule o seu 10%."
   },
   {
    "ic": "sword",
    "t": "A Alma de um Homem Livre",
    "b": "Antes do plano, vem a <strong>decisão</strong>: \"onde há determinação, há um caminho\". Dabasir deixa de fugir, encara os credores e <strong>assume as dívidas como dívidas de honra</strong>.",
    "tip": "<strong>Modelo mental:</strong> a vontade de pagar precede o plano — escolha a alma do homem livre, não a do escravo."
   },
   {
    "ic": "link",
    "t": "Pague Todos, Não Esconda",
    "b": "Dabasir procura <strong>cada credor</strong>, explica o plano e paga o que pode a cada um. Encarar os credores e honrá-los, em vez de se esconder, <strong>recupera a reputação</strong>.",
    "tip": "<strong>Cuidado:</strong> fugir dos credores afunda mais — a dívida e a vergonha só crescem."
   }
  ]
 },
 "ch09-tabuas-de-argila-e-trabalho": {
  "cards": [
   {
    "ic": "constellation",
    "t": "O Trabalho é o Melhor Amigo",
    "b": "Sharru Nada ensina que <strong>o trabalho bem-feito</strong> foi o que o tirou da escravidão e o tornou próspero. O trabalho atrai bons amigos, abre portas e é <strong>a base de toda riqueza</strong>.",
    "tip": "<strong>Como aplicar:</strong> trate o trabalho como aliado, não como castigo — faça-o melhor do que precisa."
   },
   {
    "ic": "spiral",
    "t": "Os Princípios Atravessam o Tempo",
    "b": "As tábuas de argila aplicadas por um homem moderno e endividado <strong>quitam suas dívidas e o enriquecem</strong> — provando que as leis da Babilônia continuam válidas hoje.",
    "tip": "<strong>Modelo mental:</strong> os fundamentos do dinheiro não mudam; só mudam as moedas."
   },
   {
    "ic": "steps",
    "t": "Cura 7 — Aumente sua Capacidade de Ganhar",
    "b": "Quanto mais o homem <strong>aperfeiçoa seu ofício</strong> e cumpre o que promete, mais ganha. Cultivar o desejo de prosperar e <strong>melhorar a habilidade</strong> é a sétima cura em ação.",
    "tip": "<strong>Regra:</strong> invista em aprender e fazer melhor — sua maior fonte de renda é você mesmo."
   }
  ]
 }
}
```
