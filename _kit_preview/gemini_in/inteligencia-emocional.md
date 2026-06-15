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

# LIVRO PARA APROFUNDAR: Inteligência Emocional — Daniel Goleman

**Subtítulo:** VISÃO GERAL · POR QUE ELA PODE SER MAIS IMPORTANTE QUE O QI
**Ideia central:** O QI prediz só uma fração do sucesso na vida; o resto depende, em larga medida, de competências emocionais. Goleman mostra que a inteligência emocional — perceber, regular e usar as emoções, e ler as dos outros — tem base no cérebro (o 'sequestro da amígdala') e se organiza em cinco competências aprendíveis, da autoconsciência às habilidades sociais.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-o-cerebro-emocional` — CAPÍTULO 1: O Cérebro Emocional
- `ch02-a-natureza-da-inteligencia-emocional` — CAPÍTULO 2: A Natureza da Inteligência Emocional
- `ch03-autoconsciencia-e-autocontrole` — CAPÍTULO 3: Autoconsciência e Autocontrole
- `ch04-automotivacao-e-fluxo` — CAPÍTULO 4: Automotivação e Fluxo
- `ch05-empatia-e-artes-sociais` — CAPÍTULO 5: Empatia e Artes Sociais
- `ch06-inteligencia-emocional-aplicada` — CAPÍTULO 6: Inteligência Emocional Aplicada
- `ch07-janelas-de-oportunidade` — CAPÍTULO 7: Janelas de Oportunidade
- `ch08-alfabetizacao-emocional` — CAPÍTULO 8: Alfabetização Emocional

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-o-cerebro-emocional": {
  "cards": [
   {
    "ic": "spark",
    "t": "O Sequestro da Amígdala",
    "b": "A amígdala recebe um <strong>atalho sensorial direto</strong> e pode disparar a reação (luta/fuga) antes que o córtex avalie. O resultado é rápido, intenso e — só depois — lamentado. Ganhar tempo devolve o comando à razão.",
    "tip": "<strong>Como aplicar:</strong> ao sentir os sinais do corpo (calor, coração acelerado), diga 'é um sequestro' e faça a pausa."
   },
   {
    "ic": "scale",
    "t": "Duas Mentes",
    "b": "O <strong>sistema límbico</strong> (emoção) é evolutivamente mais antigo que o <strong>neocórtex</strong> (razão). Bem afinadas, operam em harmonia; em conflito, a mente emocional pode tomar o comando. A boa decisão exige as duas.",
    "tip": "<strong>Modelo mental:</strong> emoção e razão são dois pilotos — o erro é deixar um voar sem o outro."
   },
   {
    "ic": "key",
    "t": "Para que Servem as Emoções",
    "b": "Cada emoção predispõe a uma ação ancestral: medo → fugir; raiva → defender; tristeza → recolher-se. São heranças <strong>adaptativas</strong>, não defeitos. Razão sem emoção decide pior — não melhor.",
    "tip": "<strong>Para refletir:</strong> diante de uma reação 'exagerada', pergunte que ação antiga aquela emoção está preparando."
   }
  ]
 },
 "ch02-a-natureza-da-inteligencia-emocional": {
  "cards": [
   {
    "ic": "scale",
    "t": "QE × QI",
    "b": "O QI mede o raciocínio lógico; o QE mede a competência de perceber, usar e administrar emoções. São <strong>independentes</strong> — e nos resultados de longo prazo (relacionamentos, liderança, bem-estar) o QE muitas vezes pesa mais.",
    "tip": "<strong>Para refletir:</strong> explica por que 'o melhor aluno' nem sempre vira 'o mais bem-sucedido'."
   },
   {
    "ic": "layers",
    "t": "As 5 Competências",
    "b": "O mapa do livro: <strong>autoconsciência</strong> (a base), <strong>autocontrole</strong>, <strong>automotivação</strong>, <strong>empatia</strong> e <strong>habilidades sociais</strong>. São sequenciais — cada uma depende da anterior.",
    "tip": "<strong>Como aplicar:</strong> diagnostique uma situação perguntando qual das 5 competências está faltando."
   },
   {
    "ic": "leaf",
    "t": "Aptidão, Não Destino",
    "b": "Como o cérebro é plástico, as cinco competências podem ser <strong>desenvolvidas a vida toda</strong>. Rotular alguém como 'sem jeito' fecha a porta do treino. O QE é aprendível — e por isso pode ser ensinado.",
    "tip": "<strong>Modelo mental:</strong> trate o QE como músculo, não como talento de nascença."
   }
  ]
 },
 "ch03-autoconsciencia-e-autocontrole": {
  "cards": [
   {
    "ic": "eye",
    "t": "Autoconsciência",
    "b": "Prestar atenção ao próprio estado <strong>enquanto ele acontece</strong> — nomear a emoção em tempo real. É a competência da qual todas as outras dependem; só regula quem percebe.",
    "tip": "<strong>Como aplicar:</strong> nomear ('estou com raiva') já reduz a intensidade; use os sinais do corpo como avisos precoces."
   },
   {
    "ic": "scale",
    "t": "Regular, Não Reprimir",
    "b": "O autocontrole é um <strong>termostato, não um interruptor</strong>: regula a intensidade e o tempo da emoção, não a nega. A meta (Aristóteles): a raiva certa, na medida certa, com a pessoa certa, no momento certo.",
    "tip": "<strong>Modelo mental:</strong> reprimir a emoção não a desliga — só tira de você a chance de geri-la."
   },
   {
    "ic": "mountain",
    "t": "A Falácia da Catarse",
    "b": "Extravasar a raiva ('desabafar batendo') tende a <strong>aumentá-la</strong>, não a aliviá-la. A raiva se alimenta dos pensamentos de ofensa; acalmar exige cortar essa lenha mental e dar tempo à adrenalina baixar.",
    "tip": "<strong>Cuidado:</strong> ruminar a tristeza/ansiedade prolonga o estado — redirecione a atenção e reavalie."
   }
  ]
 },
 "ch04-automotivacao-e-fluxo": {
  "cards": [
   {
    "ic": "target",
    "t": "A Aptidão Mestra",
    "b": "Canalizar a emoção para perseguir um objetivo com energia e foco — a competência que <strong>alavanca todas as outras</strong>. Entusiasmo, esperança e otimismo decidem quem persiste apesar dos reveses.",
    "tip": "<strong>Como aplicar:</strong> reenquadre o revés como 'temporário e mudável' (otimista) para sustentar o esforço."
   },
   {
    "ic": "clock",
    "t": "O Teste do Marshmallow",
    "b": "No estudo de Mischel, crianças de 4 anos que <strong>adiaram</strong> o doce para ganhar dois depois viraram adultos mais ajustados e bem-sucedidos. O controle de impulso é dos melhores preditores isolados — e é treinável.",
    "tip": "<strong>Modelo mental:</strong> diante da tentação, pergunte 'qual é o doce maior depois?'."
   },
   {
    "ic": "spiral",
    "t": "Fluxo",
    "b": "Estado de <strong>absorção total</strong> numa tarefa que equilibra desafio e habilidade — nem tédio (fácil demais) nem ansiedade (difícil demais). É o QE no auge a serviço do desempenho e do aprendizado.",
    "tip": "<strong>Como aplicar:</strong> ajuste a dificuldade da tarefa ao seu nível para entrar (e manter) o fluxo."
   }
  ]
 },
 "ch05-empatia-e-artes-sociais": {
  "cards": [
   {
    "ic": "person",
    "t": "Empatia",
    "b": "Sentir o que o outro sente; lê-se mais nos <strong>sinais não-verbais</strong> (tom, expressão, postura) do que nas palavras. Nasce da autoconsciência: só lê a emoção alheia quem reconhece a própria.",
    "tip": "<strong>Como aplicar:</strong> quando palavra e corpo discordam, acredite no corpo."
   },
   {
    "ic": "wave",
    "t": "Contágio Emocional",
    "b": "Humores se 'pegam' — captamos e propagamos estados afetivos, em geral fora da consciência. Numa equipe, o estado de quem conduz <strong>vaza para os demais</strong>. Gerir o próprio humor é, em parte, gerir o do grupo.",
    "tip": "<strong>Modelo mental:</strong> o humor é um vírus — o líder é o primeiro a contagiar a sala."
   },
   {
    "ic": "link",
    "t": "As Artes Sociais",
    "b": "Administrar as emoções dos outros: coordenar grupos, negociar conflitos, conectar, persuadir. A fórmula: <strong>empatia (perceber) + autorregulação (não se descontrolar)</strong> para conduzir a interação.",
    "tip": "<strong>Cuidado:</strong> ler a emoção alheia para explorá-la é empatia sem cuidado — a porta da manipulação."
   }
  ]
 },
 "ch06-inteligencia-emocional-aplicada": {
  "cards": [
   {
    "ic": "sword",
    "t": "Inimigos Íntimos",
    "b": "O que destrói o casal não é o conflito, mas o <strong>modo emocional</strong> de conduzi-lo. Os padrões corrosivos (Gottman): crítica, <strong>desprezo</strong> (o mais letal), defensividade e muro de pedra. Não é 'se brigam', é 'como brigam'.",
    "tip": "<strong>Como aplicar:</strong> troque a crítica de caráter ('você é egoísta') por uma queixa específica."
   },
   {
    "ic": "gap",
    "t": "O Alagamento Emocional",
    "b": "Na briga, a emoção transborda e a pessoa fica <strong>fisiologicamente inundada</strong> — incapaz de ouvir ou pensar. Muitos se amuralham no silêncio (muro de pedra) para escapar. Falar inundado só piora.",
    "tip": "<strong>Como aplicar:</strong> ao sentir o alagamento, peça pausa, acalme-se e só então retome."
   },
   {
    "ic": "person",
    "t": "Liderar e a Saúde",
    "b": "No trabalho, a competência emocional é a da liderança: <strong>crítica construtiva</strong> (específica, com solução), sintonia e gestão do contágio do humor. Na saúde, emoções tóxicas crônicas são fator de risco; o apoio emocional ajuda a curar.",
    "tip": "<strong>Modelo mental:</strong> a crítica é presente (específica + saída) ou bomba (ataque de caráter)."
   }
  ]
 },
 "ch07-janelas-de-oportunidade": {
  "cards": [
   {
    "ic": "mask",
    "t": "A Fornalha Familiar",
    "b": "A casa é a primeira escola emocional: o jeito como os pais lidam com os próprios sentimentos e com os da criança ensina competência (ou incompetência). Pais que <strong>sintonizam</strong> — validam e ajudam a nomear o sentimento — formam filhos mais competentes.",
    "tip": "<strong>Cuidado:</strong> desvalidar a criança ('não foi nada, para de chorar') sabota a sintonização."
   },
   {
    "ic": "pivot",
    "t": "Reaprender o Trauma",
    "b": "Experiências traumáticas marcam a amígdala de forma duradoura, mas é possível <strong>reaprender</strong>: recondicionar a resposta de medo em ambiente seguro. É a base da terapia — reexpor a memória até a amígdala atualizar.",
    "tip": "<strong>Modelo mental:</strong> o trauma é um aprendizado que pode ser reaprendido, não uma marca eterna."
   },
   {
    "ic": "leaf",
    "t": "Temperamento Não é Destino",
    "b": "A criança nasce com uma tendência (ex.: a tímida/inibida), mas a experiência e a criação podem <strong>remodelar</strong> essa disposição. A plasticidade do cérebro mantém aberta a porta da mudança.",
    "tip": "<strong>Para refletir:</strong> o temperamento é a argila, não a estátua — dá o formato inicial, mas ainda se molda."
   }
  ]
 },
 "ch08-alfabetizacao-emocional": {
  "cards": [
   {
    "ic": "mountain",
    "t": "O Custo do Analfabetismo Emocional",
    "b": "A incompetência emocional na população alimenta <strong>agressividade, depressão, ansiedade precoce, vício e fracasso escolar</strong>. Muitos problemas 'de comportamento' são, no fundo, déficits de competência emocional — treináveis.",
    "tip": "<strong>Para refletir:</strong> leia a violência/o vício como déficit de competência, não só falha de caráter."
   },
   {
    "ic": "book",
    "t": "A Terceira Alfabetização",
    "b": "Ensinar autoconsciência, autocontrole, automotivação, empatia e habilidades sociais de forma <strong>deliberada na escola</strong> — depois de ler e contar, aprender a sentir e a conviver. Programas de aprendizado socioemocional reduzem violência e até melhoram as notas.",
    "tip": "<strong>Modelo mental:</strong> o QE como vacina social — ensinar cedo previne o custo lá na frente."
   },
   {
    "ic": "steps",
    "t": "Caráter é Hábito Emocional",
    "b": "Virtudes como autodomínio e empatia são, no fundo, <strong>competências cultiváveis</strong> — não dons morais fixos. E a emoção se aprende pela prática e pelo exemplo do ambiente, não por sermão.",
    "tip": "<strong>Cuidado:</strong> tratar o emocional como 'extra' da escola relega o que sustenta todo o resto do aprendizado."
   }
  ]
 }
}
```
