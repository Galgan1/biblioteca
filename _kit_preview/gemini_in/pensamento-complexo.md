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

# LIVRO PARA APROFUNDAR: Introdução ao Pensamento Complexo — Edgar Morin

**Subtítulo:** VISÃO GERAL · RELIGAR SEM MUTILAR
**Ideia central:** O conhecimento ocidental separa, reduz e abstrai — e por isso produz uma inteligência cega que enxerga peças, mas perde o tecido. Edgar Morin propõe o paradigma da complexidade: distinguir sem isolar, ligar sem fundir, conviver com a contradição como parte do real.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-inteligencia-cega` — CAPÍTULO 1: A Inteligência Cega
- `ch02-desenho-intencao-complexos` — CAPÍTULO 2: O Desenho e a Intenção Complexos
- `ch03-paradigma-da-complexidade` — CAPÍTULO 3: O Paradigma da Complexidade
- `ch04-complexidade-e-acao` — CAPÍTULO 4: A Complexidade e a Ação
- `ch05-complexidade-e-empresa` — CAPÍTULO 5: A Complexidade e a Empresa
- `ch06-epistemologia-da-complexidade` — CAPÍTULO 6: Epistemologia da Complexidade

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-inteligencia-cega": {
  "cards": [
   {
    "ic": "lens",
    "t": "As Três Operações Cegas",
    "b": "<strong>Disjunção</strong> separa o que está ligado. <strong>Redução</strong> explica o todo pelo elementar ('no fundo é só química'). <strong>Abstração</strong> descola o objeto do seu contexto. Juntas, produzem a <strong>patologia do saber</strong>.",
    "tip": "<strong>Sinal de alerta:</strong> 'isso é assunto de outra área' — quando fronteiras de disciplina viram fronteiras do real, a disjunção já fez seu trabalho."
   },
   {
    "ic": "eye",
    "t": "A Inteligência Cega",
    "b": "A hiperespecialização sabe cada vez mais de cada vez <strong>menos</strong> — e ninguém vê o conjunto. Vê as peças; perde o tecido. A clareza de uma explicação simples pode ser uma <strong>mutilação bem-acabada</strong>.",
    "tip": "<strong>Modelo mental:</strong> confundir clareza com verdade é o erro da inteligência cega — a explicação mais elegante pode estar esquartejando o real."
   },
   {
    "ic": "link",
    "t": "Religar Sem Fundir",
    "b": "O gesto-chave da complexidade é <strong>religar</strong> (<em>relier</em>): distinguir sem isolar, associar sem fundir. Não pede menos rigor — pede um rigor que <strong>contextualiza e globaliza</strong>.",
    "tip": "<strong>Como aplicar:</strong> ao analisar qualquer fenômeno humano, pergunte quais dimensões (física, psíquica, social, histórica) estão tecidas juntas — e recuse-se a tratá-las em gavetas separadas."
   },
   {
    "ic": "mountain",
    "t": "O Humano Esquartejado",
    "b": "A biologia pega o corpo, a psicologia a mente, a sociologia o grupo, a economia o trabalhador. Cada uma trata sua fatia como se as outras não existissem. O resultado é um <strong>humano que não existe em lugar nenhum</strong>.",
    "tip": "<strong>Para refletir:</strong> que dimensão do problema você tende a ignorar porque 'não é da sua área'?"
   }
  ]
 },
 "ch02-desenho-intencao-complexos": {
  "cards": [
   {
    "ic": "layers",
    "t": "Mais E Menos que a Soma",
    "b": "O todo organizacional <strong>cria emergências</strong> (propriedades que só existem no conjunto) e ao mesmo tempo <strong>constrange</strong> as partes (reprime qualidades que elas teriam soltas). Guardar os dois lados evita tanto o reducionismo quanto o holismo.",
    "tip": "<strong>Modelo mental:</strong> pense no redemoinho — tem forma estável e identidade, mas só existe porque a água passa por ele continuamente (sistema aberto)."
   },
   {
    "ic": "spiral",
    "t": "Auto-Organização",
    "b": "Um sistema vivo se produz e se mantém a partir das interações dos seus componentes — e depende profundamente do meio para isso (<strong>auto-eco-organização</strong>). Autonomia e dependência não se opõem: <strong>alimentam-se mutuamente</strong>.",
    "tip": "<strong>Como aplicar:</strong> ao estudar qualquer organização, mapeie tanto o que ela produz por dentro (auto) quanto o que recebe do meio (eco) — nenhum lado basta sozinho."
   },
   {
    "ic": "person",
    "t": "Reintroduzir o Sujeito",
    "b": "A ciência clássica expulsou o observador em nome da objetividade. A complexidade o <strong>reintroduz</strong>: não há objeto conhecido sem um sujeito situado no mundo. Objetividade não é ausência de sujeito — é <strong>vigilância sobre ele</strong>.",
    "tip": "<strong>Para refletir:</strong> em toda análise que você produz, qual é o seu ponto de vista que está moldando o que você consegue ver?"
   }
  ]
 },
 "ch03-paradigma-da-complexidade": {
  "cards": [
   {
    "ic": "fork",
    "t": "Princípio Dialógico",
    "b": "Manter <strong>dois termos antagônicos</strong> que são ao mesmo tempo complementares e indispensáveis — sem dissolver a tensão entre eles. <strong>Dialógico ≠ dialético</strong>: a contradição não se resolve numa síntese; ela permanece viva e fecunda.",
    "tip": "<strong>Como aplicar:</strong> quando descartar um dos polos empobrecer o fenômeno (ordem/desordem, autonomia/dependência), nomeie os dois e recuse a 'escolha' entre eles."
   },
   {
    "ic": "spiral",
    "t": "Princípio Recursivo",
    "b": "O <strong>produto é produtor do que o produz</strong>. Os indivíduos produzem a sociedade que produz os indivíduos. Rompe a causalidade linear (causa → efeito): causa e efeito se geram mutuamente num <strong>anel recursivo</strong>.",
    "tip": "<strong>Modelo mental:</strong> quando vir uma causalidade linear num sistema vivo ou social, pergunte: 'onde está o anel recursivo?'"
   },
   {
    "ic": "constellation",
    "t": "Princípio Hologramático",
    "b": "Não só <strong>a parte está no todo</strong>, mas <strong>o todo está na parte</strong>. Como no holograma, cada fragmento contém quase toda a informação do objeto. Transcende o reducionismo (só as partes) e o holismo (só o todo).",
    "tip": "<strong>Como aplicar:</strong> enriqueça o conhecimento das partes pelo todo e do todo pelas partes, num vaivém recursivo — pergunte o que cada perspectiva ilumina na outra."
   },
   {
    "ic": "triangle",
    "t": "O Tetragrama",
    "b": "O anel <strong>ordem ⇄ desordem ⇄ interações ⇄ organização</strong>: os quatro termos se produzem mutuamente. A organização do cosmos não nasce só da ordem nem só do acaso. <strong>Sem desordem não há novidade nem organização.</strong>",
    "tip": "<strong>Para refletir:</strong> em que situação da sua vida ou trabalho a 'desordem' está, na verdade, gerando uma reorganização necessária?"
   }
  ]
 },
 "ch04-complexidade-e-acao": {
  "cards": [
   {
    "ic": "wave",
    "t": "Ecologia da Ação",
    "b": "Assim que uma ação entra no mundo, ela <strong>escapa das mãos</strong> de quem a fez. As interações do meio podem desviá-la do propósito — até invertê-lo. A ação pertence ao seu ambiente, <strong>não à intenção do agente</strong>.",
    "tip": "<strong>Sinal de alerta:</strong> prever todas as consequências é impossível — projete pontos de correção, não planos fechados."
   },
   {
    "ic": "pivot",
    "t": "Estratégia × Programa",
    "b": "<strong>Programa</strong> — sequência predeterminada; quebra diante do inesperado. <strong>Estratégia</strong> — cenário flexível que se modifica conforme chegam novas informações; usa o aleatório a seu favor. Em ambiente incerto, estratégia vence programa.",
    "tip": "<strong>Como aplicar:</strong> pense na ação como soltar um barco no rio — escolha o ponto de partida, mas ajuste o leme continuamente (estratégia), não confie no mapa fixo (programa)."
   },
   {
    "ic": "target",
    "t": "Decidir É Apostar",
    "b": "Toda decisão complexa é uma <strong>aposta</strong>: conhecimento incompleto + futuro aberto. A consciência da aposta substitui a falsa certeza. Agir <em>com</em> a incerteza — não fugir dela — é o que a complexidade pede.",
    "tip": "<strong>Modelo mental:</strong> 'aja, mas vigie a ação' — decidir não encerra a responsabilidade; abre o acompanhamento."
   }
  ]
 },
 "ch05-complexidade-e-empresa": {
  "cards": [
   {
    "ic": "leaf",
    "t": "Auto-Eco-Organização Aplicada",
    "b": "A empresa se produz a si mesma (<strong>auto</strong>), mas só existe trocando com seu meio (<strong>eco</strong>). <strong>Autonomia e dependência andam juntas</strong>: mais autonomia interna exige mais (não menos) trocas com o ambiente.",
    "tip": "<strong>Como aplicar:</strong> ao diagnosticar uma organização, mapeie as duas dimensões: o que ela gera internamente (auto) e como alimenta sua dependência do meio (eco)."
   },
   {
    "ic": "scale",
    "t": "A Dose Dialógica",
    "b": "Excesso de ordem (rigidez, hipercontrole) mata a adaptação. Excesso de desordem dissolve a empresa. A vitalidade está na <strong>dose dialógica</strong>: ordem suficiente para existir, desordem suficiente para mudar.",
    "tip": "<strong>Modelo mental:</strong> veja a empresa como organismo vivo, não máquina — precisa de metabolismo, tolera ruído e se regenera. 'Ordem demais engessa, desordem demais dissolve.'"
   },
   {
    "ic": "spark",
    "t": "Emergências e Constrangimentos",
    "b": "O todo organizacional <strong>produz mais</strong> que a soma das partes (emergências: capacidades que ninguém tinha sozinho) e <strong>produz menos</strong> (reprime qualidades dos indivíduos que o todo não comporta). Conte os dois lados.",
    "tip": "<strong>Para refletir:</strong> que capacidades coletivas sua equipe produz que ninguém tem individualmente? Que capacidades individuais o formato atual suprime?"
   }
  ]
 },
 "ch06-epistemologia-da-complexidade": {
  "cards": [
   {
    "ic": "eye",
    "t": "Conhecimento do Conhecimento",
    "b": "O pensamento que se volta sobre si mesmo para <strong>vigiar seus próprios erros, ilusões e limites</strong>. É a auto-reflexão necessária para um <strong>conhecimento pertinente</strong> — que situa, contextualiza e religa — em vez de um saber cego.",
    "tip": "<strong>Como aplicar:</strong> 'O mapa não é o território, e quem desenha o mapa está no mapa' — inclua o observador (você mesmo) na descrição do que observa."
   },
   {
    "ic": "key",
    "t": "A Incerteza Como Bússola",
    "b": "Não há fundamento absoluto, lei total nem ordem perfeita. A incerteza é <strong>parte do real e do saber</strong> — não é falha a eliminar, é condição a integrar. Trate-a como bússola: ela mantém o pensamento <strong>aberto, vigilante e corrigível</strong>.",
    "tip": "<strong>Sinal de alerta:</strong> confundir 'buscar certeza total' com rigor é o erro — a abertura à incerteza não dispensa o rigor, pede mais dele."
   },
   {
    "ic": "bulb",
    "t": "O Imperativo da Complexidade",
    "b": "Não um método-receita, mas uma <strong>exigência ética e cognitiva</strong>: pensar de modo a contextualizar e ligar, conviver com a contradição e o incompleto, sem cair no holismo vago nem no reducionismo mutilante. <strong>Ligar é mais difícil que separar.</strong>",
    "tip": "<strong>Modelo mental:</strong> a complexidade não resolve tudo — combate a mutilação, não entrega a verdade pronta. A pergunta certa tem mais valor que a resposta limpa."
   }
  ]
 }
}
```
