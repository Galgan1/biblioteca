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

# LIVRO PARA APROFUNDAR: Antifrágil — Nassim Nicholas Taleb

**Subtítulo:** VISÃO GERAL · COISAS QUE SE BENEFICIAM COM O CAOS
**Ideia central:** Existe uma categoria sem nome além de 'frágil' e 'robusto': o antifrágil — o que ganha com a desordem, a volatilidade e o estresse, em vez de só resistir. Taleb mostra como detectar fragilidade sem prever o futuro, comprar 'opcionalidade' (ganhos assimétricos) e construir sistemas — corpo, carreira, finanças, instituições — que prosperam no caos.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-o-antifragil-uma-introducao` — LIVRO 1: O Antifrágil — Uma Introdução
- `ch02-modernidade-e-a-negacao-da-antifragilidade` — LIVRO 2: Modernidade e a Negação da Antifragilidade
- `ch03-uma-visao-nao-preditiva-do-mundo` — LIVRO 3: Uma Visão Não-Preditiva do Mundo
- `ch04-opcionalidade-tecnologia-e-a-inteligencia-da-antifragilidade` — LIVRO 4: Opcionalidade, Tecnologia e a Inteligência da Antifragilidade
- `ch05-o-nao-linear-e-o-nao-linear` — LIVRO 5: O Não-Linear e o Não-Linear
- `ch06-via-negativa` — LIVRO 6: Via Negativa
- `ch07-a-etica-da-fragilidade-e-da-antifragilidade` — LIVRO 7: A Ética da Fragilidade e da Antifragilidade

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-o-antifragil-uma-introducao": {
  "cards": [
   {
    "ic": "scale",
    "t": "A Tríade",
    "b": "<strong>Frágil</strong> quebra com o choque (a espada de Dâmocles); <strong>robusto</strong> aguenta e volta igual (a Fênix); <strong>antifrágil</strong> melhora (a Hidra: corta-se uma cabeça, nascem duas). A volatilidade é veneno para um, indiferente para outro, alimento para o terceiro.",
    "tip": "<strong>Como aplicar:</strong> classifique tudo pela reação ao choque — não pergunte 'isto é bom?', pergunte 'como isto reage à desordem?'."
   },
   {
    "ic": "leaf",
    "t": "Hormese",
    "b": "O estressor em <strong>pequena dose fortalece</strong>: o músculo cresce sob carga, o osso densifica, o corpo se imuniza com um pouco de veneno (mitridatização). Privar um sistema antifrágil de estressores o <strong>atrofia</strong> — a iatrogenia do conforto.",
    "tip": "<strong>Modelo mental:</strong> pense numa 'resposta a doses' — antifrágil é remédio em dose pequena e veneno em dose enorme."
   },
   {
    "ic": "target",
    "t": "Sobrecompensação",
    "b": "O sistema antifrágil não só repara o dano: cria <strong>capacidade extra</strong>, uma reserva para o próximo choque. O estressor é informação — sem ele, o sistema fica cego ao próprio risco e fragiliza em silêncio.",
    "tip": "<strong>Para refletir:</strong> conforto e estabilidade total não trazem segurança; produzem fragilidade oculta que estoura de uma vez."
   }
  ]
 },
 "ch02-modernidade-e-a-negacao-da-antifragilidade": {
  "cards": [
   {
    "ic": "wrench",
    "t": "Iatrogenia",
    "b": "'Causado pelo curador': o <strong>dano oculto da intervenção</strong>. O intervencionista vê o ganho visível da ação e ignora o dano invisível e tardio — na medicina, na economia, na política, na criação dos filhos.",
    "tip": "<strong>Regra:</strong> só intervir quando o benefício for grande e claro; no caso leve, pratique a procrastinação racional (deixe o sistema se autocorrigir)."
   },
   {
    "ic": "clock",
    "t": "O Peru de Russell",
    "b": "O peru alimentado todo dia ganha 'confiança' crescente na bondade do dono — até a véspera do Dia de Ação de Graças. <strong>Estabilidade aparente = fragilidade máxima acumulada.</strong> Quanto mais longa a calmaria, maior o risco escondido na cauda.",
    "tip": "<strong>Para refletir:</strong> este sistema está calmo porque é saudável, ou porque está sendo artificialmente segurado?"
   },
   {
    "ic": "wave",
    "t": "Volatilidade Suprimida",
    "b": "Apagar todo incêndio pequeno acumula combustível para o incêndio catastrófico; reprimir toda recessão prepara o colapso. O risco <strong>não desaparece — migra para a cauda</strong>, vira raro porém devastador. Sistemas vivos pedem solavancos pequenos e frequentes.",
    "tip": "<strong>Modelo mental:</strong> a Suíça (decisões locais, bottom-up) é robusta; o Estado tecnocrático top-down é frágil."
   }
  ]
 },
 "ch03-uma-visao-nao-preditiva-do-mundo": {
  "cards": [
   {
    "ic": "scale",
    "t": "A Assimetria de Sêneca",
    "b": "O estoico Sêneca, riquíssimo, já contava as posses como perdidas: <strong>neutralizado o downside, só sobrava upside</strong>. Antifragilidade = mais upside que downside diante da volatilidade; fragilidade, o inverso. O formato do payoff importa mais que a probabilidade.",
    "tip": "<strong>Como aplicar:</strong> aniquile o downside primeiro — só então o upside é gratuito."
   },
   {
    "ic": "person",
    "t": "Fat Tony × Dr. John",
    "b": "<strong>Fat Tony</strong> fareja a fragilidade pelo bom senso e pela pele em jogo; <strong>Dr. John</strong> raciocina por modelos frágeis e probabilidades falsas. A sabedoria prática (mêtis) bate o conhecimento acadêmico abstrato no terreno do incerto.",
    "tip": "<strong>Para refletir:</strong> quem tem pele em jogo fareja o que o modelo não vê."
   },
   {
    "ic": "eye",
    "t": "Não Prever, Medir Fragilidade",
    "b": "Erramos sistematicamente nas caudas; planejar sobre previsões é construir na areia. Mas a <strong>fragilidade é mensurável e previsível</strong> — o evento, não. Quem não está frágil dispensa o oráculo.",
    "tip": "<strong>Modelo mental:</strong> troque 'qual a probabilidade do evento?' por 'qual o meu payoff se o evento vier?'."
   }
  ]
 },
 "ch04-opcionalidade-tecnologia-e-a-inteligencia-da-antifragilidade": {
  "cards": [
   {
    "ic": "fork",
    "t": "Opcionalidade",
    "b": "Assimetria embutida: <strong>pequeno custo de entrada, downside travado, upside aberto</strong>. 'Você não precisa estar certo com frequência — só quando a recompensa for grande.' A opção dá antifragilidade sem exigir previsão.",
    "tip": "<strong>Como aplicar:</strong> prefira posições com pouco a perder e muito a ganhar; mantenha-se exposto a boas surpresas."
   },
   {
    "ic": "scale",
    "t": "Estratégia Barbell (Halteres)",
    "b": "Combine dois extremos e evite o meio: <strong>~85–90% extremamente seguro + ~10–15% muito arriscado e pequeno</strong>. Downside travado pelo lado seguro, upside aberto pelo agressivo. O 'moderado' do meio engana — esconde risco de cauda.",
    "tip": "<strong>Para refletir:</strong> pior caso = perder só a fração arriscada; melhor caso = um acerto que paga tudo."
   },
   {
    "ic": "spark",
    "t": "Tinkering (Tentativa-e-Erro)",
    "b": "A inovação real nasce de <strong>muitas tentativas baratas</strong>, não de grandes planos (a ilusão 'Soviético-Harvard'). Cada erro é informação de baixo custo; o acerto ocasional paga por todos. A prática precede a teoria.",
    "tip": "<strong>Modelo mental:</strong> erre barato e cedo — mas só se o pior caso for pequeno e conhecido."
   }
  ]
 },
 "ch05-o-nao-linear-e-o-nao-linear": {
  "cards": [
   {
    "ic": "gap",
    "t": "Convexidade × Concavidade",
    "b": "O que importa não é a média do estressor, mas a resposta a <strong>doses crescentes</strong>. <strong>Côncavo (frágil):</strong> o dano cresce mais que proporcionalmente — cair de 10 m machuca muito mais que dez quedas de 1 m. <strong>Convexo (antifrágil):</strong> o ganho cresce mais que proporcionalmente.",
    "tip": "<strong>Como aplicar:</strong> dobre o estressor — se o dano mais que dobra, é frágil; se o ganho mais que dobra, é antifrágil."
   },
   {
    "ic": "lens",
    "t": "O Efeito de Jensen",
    "b": "Sob não-linearidade, a <strong>média dos resultados ≠ resultado da média</strong>. O frágil sofre da 'média escondida': parece OK na média, mas a variação o destrói. O que mata (ou salva) é a dispersão, não o valor médio.",
    "tip": "<strong>Para refletir:</strong> raciocinar pela média esconde a cauda — e a cauda é onde tudo se decide."
   },
   {
    "ic": "layers",
    "t": "O Efeito do Tamanho",
    "b": "A mesma 'quantidade' de estresse fere muito mais se vier <strong>concentrada e rápida</strong>. O grande e concentrado é frágil (um elefante despenca; muitos camundongos, não). Prefira muitos pequenos e independentes a um grande.",
    "tip": "<strong>Modelo mental:</strong> concentração e gigantismo escondem risco de cauda côncava."
   }
  ]
 },
 "ch06-via-negativa": {
  "cards": [
   {
    "ic": "leaf",
    "t": "Via Negativa",
    "b": "Agir por <strong>subtração</strong>: o que é mau é mais conhecível que o bom. Recomendação por remoção (parar de fumar, cortar açúcar, eliminar a má dívida) é mais robusta que por adição — porque toda adição carrega iatrogenia oculta.",
    "tip": "<strong>Como aplicar:</strong> antes de adicionar uma solução, pergunte 'o que posso remover para resolver isto?'."
   },
   {
    "ic": "clock",
    "t": "O Efeito Lindy",
    "b": "Para o <strong>não-perecível</strong> (ideias, livros, tecnologias, instituições), a expectativa de vida futura cresce com a idade já vivida: cada ano sobrevivido prevê mais um. O que durou prova durabilidade — o tempo é o melhor filtro de fragilidade.",
    "tip": "<strong>Regra:</strong> na dúvida, prefira o que já passou no teste do tempo."
   },
   {
    "ic": "pivot",
    "t": "Neomania",
    "b": "O vício no <strong>novo pelo novo</strong>: superestimar o recente e descartar o que o tempo já validou. Antídoto: o filtro de Lindy. O moderno confunde novidade com qualidade — e troca o robusto testado pelo frágil da moda.",
    "tip": "<strong>Para refletir:</strong> o novíssimo ainda não passou no teste do tempo; o clássico já passou."
   }
  ]
 },
 "ch07-a-etica-da-fragilidade-e-da-antifragilidade": {
  "cards": [
   {
    "ic": "scale",
    "t": "Pele em Jogo",
    "b": "<strong>Simetria</strong> entre quem decide e quem sofre o resultado: 'todo capitão afunda com seu navio'. Sem pele em jogo, o agente fica antifrágil às custas do sistema — ganha nos bônus, socializa as perdas.",
    "tip": "<strong>Como aplicar:</strong> antes de confiar numa decisão ou conselho, pergunte 'quem paga se isto der errado?'."
   },
   {
    "ic": "link",
    "t": "Transferência de Fragilidade",
    "b": "Alguns ganham robustez <strong>extraindo-a de outrem</strong>: o banqueiro que lucra no risco e é socorrido na quebra, o 'especialista' sem custo do erro. É roubo de cauda — upside privado, downside coletivo.",
    "tip": "<strong>Para refletir:</strong> incentivos que premiam o ganho e isentam da perda são fábrica de risco transferido."
   },
   {
    "ic": "person",
    "t": "O Problema do Agente",
    "b": "Gestores, consultores e burocratas com <strong>opção sem obrigação</strong>: capturam o ganho visível, transferem o risco oculto. O herói antigo (que pagava com a própria vida) é o oposto do agente moderno. A coragem é a única virtude impossível de fingir.",
    "tip": "<strong>Modelo mental:</strong> desconfie de quem opina/decide sem custo; valorize quem arca com o próprio erro."
   }
  ]
 }
}
```
