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

# LIVRO PARA APROFUNDAR: Não Me Faça Pensar — Steve Krug

**Subtítulo:** VISÃO GERAL · USABILIDADE E O BOM SENSO NA WEB
**Ideia central:** E se a regra de ouro da usabilidade coubesse numa frase? Steve Krug a resume assim: 'Não me faça pensar'. Uma página, um botão, um link — tudo deve ser auto-evidente, óbvio sem esforço. Porque as pessoas não leem, escaneiam; não escolhem a melhor opção, pegam a primeira razoável; não entendem o sistema, se viram. Não Me Faça Pensar é o bom senso aplicado ao design digital — e a prova de que boa usabilidade se descobre testando, não discutindo.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-nao-me-faca-pensar` — CAPÍTULO 1: Não Me Faça Pensar (a 1ª Lei)
- `ch02-como-usamos-a-web` — CAPÍTULO 2: Como Realmente Usamos a Web
- `ch03-design-escaneabilidade` — CAPÍTULO 3: Design para Escaneabilidade (Billboard 101)
- `ch04-omita-palavras` — CAPÍTULO 4: Omita as Palavras Desnecessárias
- `ch05-navegacao-persistente` — CAPÍTULO 5: Navegação Persistente
- `ch06-teste-do-tronco` — CAPÍTULO 6: O Teste do Tronco (Trunk Test)
- `ch07-pagina-inicial` — CAPÍTULO 7: A Página Inicial (Home)
- `ch08-teste-de-usabilidade` — CAPÍTULO 8: Teste de Usabilidade Barato
- `ch09-boa-vontade` — CAPÍTULO 9: A Reserva de Boa Vontade
- `ch10-acessibilidade-mobile` — CAPÍTULO 10: Acessibilidade e Mobile

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-nao-me-faca-pensar": {
  "cards": [
   {
    "ic": "bulb",
    "t": "A 1ª Lei de Krug",
    "b": "A página deve ser <strong>auto-evidente</strong>: o usuário 'entende' sem deliberar. Cada elemento que provoca um <strong>ponto de interrogação na cabeça</strong> ('isto é clicável?', 'começo por onde?') cobra um pequeno imposto de atenção. A meta é tornar o uso óbvio, não esperto.",
    "tip": "<strong>Como aplicar:</strong> revise cada tela perguntando 'isto gera alguma dúvida?'. Cada dúvida é um ponto a corrigir."
   },
   {
    "ic": "scale",
    "t": "Auto-evidente > Autoexplicativo > Confuso",
    "b": "Mire no <strong>auto-evidente</strong> (captado à primeira vista). Aceite o <strong>autoexplicativo</strong> (exige um pouco de pensamento, mas a explicação está ali) só quando for inevitável, em telas complexas. <strong>Confuso / precisa de instrução</strong> é inaceitável.",
    "tip": "<strong>Modelo mental:</strong> a página é um outdoor passando a 100 km/h — precisa ser 'pega' num relance."
   },
   {
    "ic": "gap",
    "t": "Nomes Criativos no Lugar de Rótulos Óbvios",
    "b": "Chamar 'Vagas' de 'Jobs!' ou 'Produtos' de 'Soluções' força o usuário a <strong>decodificar</strong>. Nomes de marketing 'fofos' geram interrogações; rótulos comuns são entendidos sem pensar.",
    "tip": "<strong>Sinal de alerta:</strong> se um rótulo exige tradução mental, ele falha na 1ª Lei. Prefira o óbvio ao criativo."
   }
  ]
 },
 "ch02-como-usamos-a-web": {
  "cards": [
   {
    "ic": "eye",
    "t": "Não Lemos — Escaneamos",
    "b": "O olho <strong>varre a página</strong> buscando palavras-âncora que combinem com o objetivo, em vez de ler frase a frase. Otimizar para o 'leitor cuidadoso' que para e pondera é desenhar para alguém que não existe.",
    "tip": "<strong>Como aplicar:</strong> use hierarquia visual e palavras-chave que 'saltem' — desenhe para quem bate o olho, não para quem lê tudo."
   },
   {
    "ic": "fork",
    "t": "Satisficing (Satisfazer)",
    "b": "Em vez da melhor opção, o usuário pega <strong>a primeira que parece servir</strong> (termo de Herbert Simon: <em>satisfy</em> + <em>suffice</em>). Procurar a ótima custa esforço, errar tem baixo custo (basta voltar) e adivinhar é até divertido.",
    "tip": "<strong>Regra:</strong> faça a opção certa ser a mais saliente — o usuário vai clicar na primeira razoável, não na melhor escondida."
   },
   {
    "ic": "wave",
    "t": "Muddling Through (Se Virar)",
    "b": "O usuário <strong>usa sem entender o modelo</strong> do sistema; se funciona 'mais ou menos', ele segue e nunca descobre o jeito 'certo'. Contar que ele 'vá descobrir navegando' é apostar contra o comportamento real.",
    "tip": "<strong>Cuidado:</strong> interfaces que quebram quando o usuário improvisa punem exatamente o jeito como as pessoas agem."
   }
  ]
 },
 "ch03-design-escaneabilidade": {
  "cards": [
   {
    "ic": "layers",
    "t": "Os 5 Movimentos do Billboard 101",
    "b": "Desenhe a página como um outdoor: <strong>1) aproveite convenções</strong> (logo no topo-esquerda, carrinho à direita); <strong>2) crie hierarquia visual</strong> (importante = proeminente, relacionado = agrupado); <strong>3) divida em áreas claras</strong>; <strong>4) deixe óbvio o que é clicável</strong>; <strong>5) elimine o ruído</strong>.",
    "tip": "<strong>Como aplicar:</strong> faça a aparência refletir a estrutura — o olho deve 'ler' a organização antes de ler as palavras."
   },
   {
    "ic": "book",
    "t": "Convenções > Inovação",
    "b": "Padrões consagrados são processados <strong>sem esforço</strong> porque já foram aprendidos em mil outros sites. Inove apenas quando tiver certeza de que a nova forma é claramente melhor e tão óbvia quanto a convenção.",
    "tip": "<strong>Modelo mental:</strong> convenções são vocabulário compartilhado — economizam o 'pensar' do usuário."
   },
   {
    "ic": "spark",
    "t": "Eliminar o Ruído (Noise)",
    "b": "Banners, animações e cores que competem entre si <strong>afogam o conteúdo</strong>. Há três tipos de ruído: barulho de fundo, bagunça e tagarelice visual. Cada elemento extra rouba atenção do que importa.",
    "tip": "<strong>Cuidado:</strong> hierarquia plana (tudo do mesmo tamanho/peso) deixa o usuário sem saber por onde começar."
   }
  ]
 },
 "ch04-omita-palavras": {
  "cards": [
   {
    "ic": "steps",
    "t": "A 3ª Lei: Corte pela Metade, Duas Vezes",
    "b": "Adaptando Strunk & White à web: <strong>'livre-se de metade das palavras de cada página, depois livre-se de metade do que sobrou'</strong>. A maioria das páginas suporta esse corte sem perda de informação — só de ruído.",
    "tip": "<strong>Como aplicar:</strong> seja um editor implacável; cada palavra deve justificar a própria presença ou sair."
   },
   {
    "ic": "bubble",
    "t": "Mate o Happy Talk",
    "b": "O <strong>'blá-blá feliz'</strong> de boas-vindas e auto-promoção ('Bem-vindo ao nosso site! É um prazer recebê-lo...') não diz nada útil e ocupa o espaço nobre. É ruído puro: corte por inteiro.",
    "tip": "<strong>Regra:</strong> se o texto não ajuda o usuário a agir, ele é candidato a corte."
   },
   {
    "ic": "gap",
    "t": "Instruções São um Sintoma",
    "b": "A maioria das instruções é <strong>ignorada</strong>. Em vez de explicar, torne as coisas tão óbvias que dispensem instrução; o que sobrar, reduza ao mínimo essencial, junto do ponto de uso.",
    "tip": "<strong>Cuidado:</strong> precisar de instrução longa costuma significar que o design não está óbvio o bastante."
   }
  ]
 },
 "ch05-navegacao-persistente": {
  "cards": [
   {
    "ic": "pin",
    "t": "O \"Billboard de Navegação\"",
    "b": "O núcleo que se repete em todas as páginas: <strong>Site ID</strong> (logo no topo, clicável, leva à home), <strong>Seções</strong> (navegação primária), <strong>'Você está aqui'</strong> (destaque da seção atual), <strong>Busca</strong> (caixa simples, sempre no mesmo lugar) e atalhos/utilitários.",
    "tip": "<strong>Como aplicar:</strong> repita exatamente o mesmo núcleo de navegação em toda página, na mesma posição."
   },
   {
    "ic": "pin",
    "t": "Sempre Marque \"Você Está Aqui\"",
    "b": "O usuário <strong>não chega pela home</strong> — entra fundo, por links do Google. Por isso precisa se localizar de qualquer ponto. O marcador 'você está aqui' (a seção atual destacada) e os breadcrumbs respondem 'onde estou?'.",
    "tip": "<strong>Modelo mental:</strong> pense nas placas de um shopping — 'Você está aqui', mapa sempre no mesmo lugar."
   },
   {
    "ic": "link",
    "t": "O Logo Leva à Home",
    "b": "Convenção universal: clicar no <strong>Site ID volta ao começo</strong>. Navegação que muda de página para página, ou busca escondida atrás de filtros, desorienta e viola o satisficing.",
    "tip": "<strong>Cuidado:</strong> navegação inconsistente entre páginas quebra a persistência e perde o usuário."
   }
  ]
 },
 "ch06-teste-do-tronco": {
  "cards": [
   {
    "ic": "lens",
    "t": "As 6 Perguntas do Trunk Test",
    "b": "Pegue uma página interna qualquer, isolada do contexto, e responda de relance: <strong>1)</strong> que site é este? (Site ID) <strong>2)</strong> em que página estou? (título) <strong>3)</strong> quais as seções principais? <strong>4)</strong> quais minhas opções neste nível? <strong>5)</strong> onde estou na hierarquia? ('você está aqui') <strong>6)</strong> como faço uma busca?",
    "tip": "<strong>Como aplicar:</strong> abra uma página profunda fora de contexto e cheque os 6 itens em segundos — um veredito barato e honesto."
   },
   {
    "ic": "key",
    "t": "Cada Página É uma Porta de Entrada",
    "b": "A maioria dos usuários <strong>não entra pela home</strong>: chega fundo, via busca e links. Logo, toda página deve <strong>se sustentar sozinha</strong> e responder às perguntas-âncora sem depender do caminho percorrido.",
    "tip": "<strong>Modelo mental:</strong> não desenhe a jornada 'desde a home'; desenhe cada página como uma entrada autônoma."
   },
   {
    "ic": "gap",
    "t": "Páginas Internas Sem Título",
    "b": "Sem um <strong>título claro e proeminente</strong> (que bata com o link clicado e com o item destacado na navegação), o usuário não sabe onde está nem como subir um nível — falha imediata no trunk test.",
    "tip": "<strong>Cuidado:</strong> navegação que só faz sentido se você 'veio da home' perde quem chega pelo meio."
   }
  ]
 },
 "ch07-pagina-inicial": {
  "cards": [
   {
    "ic": "target",
    "t": "Vença o \"Big Honkin' Question\"",
    "b": "Nunca deixe o visitante sem resposta para <strong>'o que é este site?'</strong>. No espaço nobre (visível sem rolar), entregue uma <strong>tagline / proposta de valor</strong> concreta — 'o que é isto e por que eu deveria me importar?' — não happy talk genérico.",
    "tip": "<strong>Como aplicar:</strong> troque 'Inovação que transforma' por algo concreto: 'Software de agendamento para clínicas — menos faltas, mais consultas'."
   },
   {
    "ic": "scale",
    "t": "As Tarefas que a Home Equilibra",
    "b": "A home precisa cumprir, ao mesmo tempo: <strong>identidade e missão</strong>, <strong>hierarquia do site</strong> (as seções), <strong>busca</strong>, <strong>conteúdo em destaque/atalhos</strong> e <strong>registro/login</strong>. Nem tudo cabe no espaço nobre — priorize por trade-off.",
    "tip": "<strong>Modelo mental:</strong> a home é a fachada e a vitrine da loja: num relance, diz o que vende e convida a entrar."
   },
   {
    "ic": "mask",
    "t": "O Mito da Home Perfeita",
    "b": "Tentar encaixar <strong>todas as prioridades de todos os stakeholders</strong> transforma a home num mural de banners que não diz o que o site é. A 'home perfeita' que agrada a todos resulta em ruído e mensagem diluída.",
    "tip": "<strong>Cuidado:</strong> cada departamento 'pendurando' seu banner é o caminho mais curto para uma home que não comunica nada."
   }
  ]
 },
 "ch08-teste-de-usabilidade": {
  "cards": [
   {
    "ic": "target",
    "t": "A Fórmula do Teste Barato",
    "b": "<strong>Quantos:</strong> ~3 usuários por rodada (já revelam os problemas mais sérios). <strong>Quando:</strong> comece cedo e teste sempre — <strong>'uma manhã por mês'</strong>. <strong>Como:</strong> dê tarefas reais, peça para <strong>pensar em voz alta</strong> (<em>think aloud</em>) e observe sem ajudar nem guiar.",
    "tip": "<strong>Como aplicar:</strong> faça o debrief no mesmo dia e conserte só os problemas mais sérios primeiro — resista a consertar tudo."
   },
   {
    "ic": "gap",
    "t": "O Mito do \"Usuário Médio\"",
    "b": "Não há usuário típico: 'todos os usuários da web são únicos e todo uso é basicamente imprevisível'. Invocar o <strong>'usuário médio'</strong> para vencer uma discussão é apoiar-se numa figura inexistente.",
    "tip": "<strong>Sinal de alerta:</strong> quando alguém diz 'o usuário médio vai entender', é hora de testar, não de debater."
   },
   {
    "ic": "lens",
    "t": "Testar para Achar, não para Provar",
    "b": "O objetivo <strong>não é estatística científica</strong> — é encontrar e corrigir problemas. Teste qualitativo, faça-você-mesmo: <strong>pouco e frequente vence muito e raro</strong>. Cada rodada troca horas de opinião por minutos de evidência.",
    "tip": "<strong>Modelo mental:</strong> testar é acender a luz — você para de tropeçar no que não via."
   }
  ]
 },
 "ch09-boa-vontade": {
  "cards": [
   {
    "ic": "scale",
    "t": "A Paciência É um Tanque Finito",
    "b": "A boa vontade começa cheia (em grau variável) e se esvazia com cada frustração. O perigoso é a <strong>soma de pequenos atritos</strong> — cada um 'pequeno demais para reclamar' — que vaza o tanque até o usuário desistir <strong>sem avisar</strong>.",
    "tip": "<strong>Como aplicar:</strong> a cada exigência, pergunte 'isto enche ou esvazia o tanque?'. Trate o usuário como convidado."
   },
   {
    "ic": "sword",
    "t": "O Que ESVAZIA o Reservatório",
    "b": "Drenam a boa vontade: <strong>esconder o que o usuário quer</strong> (preço, contato, suporte); <strong>puni-lo por não fazer 'do seu jeito'</strong> (rejeitar telefone com parênteses); <strong>pedir dados desnecessários</strong>; empurrar para ele um trabalho que é seu; e a aparência amadora.",
    "tip": "<strong>Cuidado:</strong> esconder o preço para 'capturar o lead' esvazia o tanque na hora."
   },
   {
    "ic": "leaf",
    "t": "O Que REABASTECE",
    "b": "Recompõem a paciência: <strong>dizer claramente o que ele quer saber</strong> (frete, prazo, disponibilidade); <strong>poupar passos</strong> e não pedir o que você não precisa; <strong>antecipar dúvidas</strong> (ajuda no ponto de uso); e caprichar nos detalhes e na cortesia.",
    "tip": "<strong>Modelo mental:</strong> hospitalidade reabastece; rispidez drena. Trate o usuário como você gostaria de ser tratado."
   }
  ]
 },
 "ch10-acessibilidade-mobile": {
  "cards": [
   {
    "ic": "key",
    "t": "Acessibilidade É Usabilidade Estendida",
    "b": "Corrigir os problemas mais comuns costuma ser <strong>barato e beneficia a todos</strong> ('a maré que sobe levanta todos os barcos'): <strong>alt text</strong> em imagens informativas, <strong>rótulos</strong> em formulários, <strong>contraste e fonte</strong> legíveis, <strong>navegação por teclado</strong> e ordem semântica.",
    "tip": "<strong>Como aplicar:</strong> nunca transmita informação só por cor (ex.: 'campos em vermelho são obrigatórios') — exclui daltônicos."
   },
   {
    "ic": "wave",
    "t": "Mobile É o Stress Test da 1ª Lei",
    "b": "Celular <strong>não é desktop encolhido</strong>: tela menor, dedo grosso, atenção dividida. Priorize o essencial, use <strong>alvos de toque grandes e espaçados</strong> e exija ainda menos pensamento. Se passa no mobile distraído, passa em qualquer contexto.",
    "tip": "<strong>Modelo mental:</strong> a acessibilidade é como a rampa de calçada — feita para cadeirantes, ajuda carrinhos, malas e todo mundo."
   },
   {
    "ic": "clock",
    "t": "Usabilidade × Aprendabilidade (Learnability)",
    "b": "Interfaces mobile escondem comandos atrás de gestos e ícones. Vale sacrificar um pouco de usabilidade imediata se o usuário <strong>aprende rápido</strong> — mas não exagere no obscuro: gesto crítico sem nenhuma pista tem learnability zero.",
    "tip": "<strong>Cuidado:</strong> esconder ações importantes atrás de ícones ambíguos faz ninguém adivinhar como agir."
   }
  ]
 }
}
```
