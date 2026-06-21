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

# LIVRO PARA APROFUNDAR: Mindset — Carol S. Dweck

**Subtítulo:** VISÃO GERAL · A NOVA PSICOLOGIA DO SUCESSO
**Ideia central:** Uma crença simples sobre você mesmo — se suas qualidades são fixas ou cultiváveis — organiza grande parte da sua vida. Dweck mostra como a mentalidade fixa transforma cada situação num veredito, e a de crescimento transforma erro, esforço e crítica em combustível para aprender.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-as-mentalidades` — CAPÍTULO 1: As Mentalidades
- `ch02-por-dentro-das-mentalidades` — CAPÍTULO 2: Por Dentro das Mentalidades
- `ch03-a-verdade-sobre-capacidade-e-realizacao` — CAPÍTULO 3: A Verdade sobre a Capacidade e a Realização
- `ch04-esporte-a-mentalidade-de-um-campeao` — CAPÍTULO 4: Esporte — A Mentalidade de um Campeão
- `ch05-negocios-mentalidade-e-lideranca` — CAPÍTULO 5: Negócios — Mentalidade e Liderança
- `ch06-relacionamentos-mentalidades-no-amor` — CAPÍTULO 6: Relacionamentos — Mentalidades no Amor
- `ch07-pais-professores-treinadores` — CAPÍTULO 7: Pais, Professores e Treinadores
- `ch08-mudando-mentalidades` — CAPÍTULO 8: Mudando Mentalidades

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-as-mentalidades": {
  "cards": [
   {
    "ic": "key",
    "t": "Mentalidade Fixa",
    "b": "A crença de que qualidades — inteligência, talento, caráter — são <strong>fixas e dadas de uma vez por todas</strong>. Diante de erro, crítica ou esforço, o foco vira 'provar quanto valho'. Cada situação é um veredito.",
    "tip": "<strong>Tell:</strong> ler tudo como nota final sobre quem você é."
   },
   {
    "ic": "leaf",
    "t": "Mentalidade de Crescimento",
    "b": "A crença de que qualidades básicas podem ser <strong>cultivadas com esforço, estratégia e ajuda</strong>. Não é 'todos podem tudo' — é que o potencial real é desconhecido e desenvolvível.",
    "tip": "<strong>Como aplicar:</strong> trate cada situação como oportunidade de aprender, não como teste de valor."
   },
   {
    "ic": "scale",
    "t": "Veredito × Jornada",
    "b": "A mesma situação vira <strong>'ameaça à minha imagem'</strong> (fixa) ou <strong>'informação para aprender'</strong> (crescimento). A lente decide a leitura — e a leitura decide a reação.",
    "tip": "<strong>Modelo mental:</strong> a mentalidade é uma crença — e crenças podem mudar."
   }
  ]
 },
 "ch02-por-dentro-das-mentalidades": {
  "cards": [
   {
    "ic": "layers",
    "t": "Fracasso: Informação × Identidade",
    "b": "Na mente fixa, 'eu falhei' vira '<strong>eu sou um fracasso</strong>' (identidade). Na de crescimento, fracassar é uma ação que <strong>ensina</strong> — dado de diagnóstico, não rótulo.",
    "tip": "<strong>Como reverter:</strong> separe o ato ('isto não deu certo') da pessoa ('eu não presto')."
   },
   {
    "ic": "spark",
    "t": "O Poder do 'Ainda'",
    "b": "Trocar 'não consigo' por '<strong>não consigo ainda</strong>' reintroduz a linha do tempo e aponta para o próximo passo. Não nega a realidade — adia o veredito.",
    "tip": "<strong>Como aplicar:</strong> qualquer 'não sei/não consigo' ganha um 'ainda' — e a próxima estratégia."
   },
   {
    "ic": "mountain",
    "t": "A Crença sobre o Esforço",
    "b": "Para a mente fixa, esforço é sinal de <strong>pouca capacidade</strong> ('se preciso me esforçar, não sou talentoso'). Para a de crescimento, esforço é o que <strong>torna você competente</strong> — é o caminho, não a vergonha.",
    "tip": "<strong>Para refletir:</strong> ler esforço como humilhação faz desistir justo quando o trabalho daria fruto."
   }
  ]
 },
 "ch03-a-verdade-sobre-capacidade-e-realizacao": {
  "cards": [
   {
    "ic": "constellation",
    "t": "O Mito do Gênio Solitário",
    "b": "A história contada esconde o trabalho. Edison tinha equipe de <strong>~30 assistentes</strong> e avançava por tentativa e erro; Mozart levou <strong>mais de dez anos</strong> até obra original; Darwin, meia vida. Atrás do 'talento' há, quase sempre, uma montanha de trabalho.",
    "tip": "<strong>Modelo mental:</strong> ao admirar um feito, pergunte 'que trabalho invisível tornou isto possível?'"
   },
   {
    "ic": "mask",
    "t": "O Perigo do Rótulo 'Inteligente'",
    "b": "Dizer a alguém que é talentoso parece um presente, mas <strong>planta a mente fixa</strong>: agora a pessoa precisa proteger o rótulo evitando riscos. Quando vem a dificuldade, foge do desafio.",
    "tip": "<strong>Cuidado:</strong> elogiar a inteligência reduz a resiliência; elogie o processo."
   },
   {
    "ic": "steps",
    "t": "Realização = Capacidade × Esforço",
    "b": "Se você crê que 'esforço = não ser inteligente', não se esforçar protege a desculpa ('eu poderia, se quisesse'). Mas o feito vem de <strong>capacidade + mentalidade + esforço</strong>, não de dom puro.",
    "tip": "<strong>Para refletir:</strong> o ponto de partida não decide o destino — a mentalidade e o esforço decidem."
   }
  ]
 },
 "ch04-esporte-a-mentalidade-de-um-campeao": {
  "cards": [
   {
    "ic": "target",
    "t": "Talento × Trabalho",
    "b": "O talento, quase sempre, foi sustentado por uma quantidade <strong>gigantesca de trabalho</strong>. Muitos atletas de topo nem eram os mais talentosos quando jovens — a trajetória fez a diferença.",
    "tip": "<strong>Modelo mental:</strong> 'campeão' é verbo (constrói-se), não substantivo (algo que se é)."
   },
   {
    "ic": "mountain",
    "t": "Caráter sob Pressão",
    "b": "A capacidade de dar o melhor <strong>justamente quando é mais difícil</strong> não é dom: é mentalidade de crescimento aplicada. A mente fixa, que precisa ser número um sem esforço, quebra quando o talento bruto não basta.",
    "tip": "<strong>Para refletir:</strong> precisar de vitória fácil para se sentir bem torna o atleta frágil diante de qualquer adversário à altura."
   },
   {
    "ic": "pivot",
    "t": "Reveses como Diagnóstico",
    "b": "O atleta de crescimento usa a derrota para <strong>corrigir e voltar mais forte</strong>; o de mente fixa a usa como prova de que 'não tem mais'. E ama o processo — o treino chato e repetido —, não só o troféu.",
    "tip": "<strong>Como aplicar:</strong> veja a derrota como o melhor treinador — ela aponta onde melhorar."
   }
  ]
 },
 "ch05-negocios-mentalidade-e-lideranca": {
  "cards": [
   {
    "ic": "eye",
    "t": "A Doença do CEO",
    "b": "O líder de mente fixa precisa provar superioridade o tempo todo. <strong>Cerca-se de bajuladores, expulsa os críticos e para de aprender.</strong> Iacocca (Chrysler) perdeu mercado para os japoneses por não se dispor a mudar.",
    "tip": "<strong>Tell:</strong> avalie um líder pela quantidade de más notícias que chegam até ele."
   },
   {
    "ic": "constellation",
    "t": "Cultura de Aprendizado × de Gênios",
    "b": "Empresas que <strong>cultuam o talento individual</strong> (o astro solitário) criam competição tóxica. As que cultuam <strong>desenvolvimento, colaboração e melhoria contínua</strong> vencem no longo prazo.",
    "tip": "<strong>Para refletir:</strong> a mente fixa do líder silencia o dissenso; a de crescimento o convida para chegar à melhor decisão."
   },
   {
    "ic": "bulb",
    "t": "Convidar a Verdade Dura",
    "b": "O líder de crescimento busca a <strong>verdade desconfortável</strong>, cerca-se de gente mais capaz, admite erros e desenvolve os outros. Fere o ego no curto prazo; protege a organização no longo.",
    "tip": "<strong>Como aplicar:</strong> busque ativamente as más notícias — elas são o sistema de navegação da empresa."
   }
  ]
 },
 "ch06-relacionamentos-mentalidades-no-amor": {
  "cards": [
   {
    "ic": "mask",
    "t": "Os Mitos do Amor Fixo",
    "b": "(1) Se é amor verdadeiro, não dá trabalho; (2) parceiros devem <strong>ler a mente</strong> um do outro; (3) tudo deve ser perfeito sem esforço. Cada mito sabota o vínculo ao primeiro atrito.",
    "tip": "<strong>Tell:</strong> 'se temos que trabalhar nisso, não era para ser' — o pensamento que faz desistir de relações boas."
   },
   {
    "ic": "link",
    "t": "Conflito como Aprendizado",
    "b": "Na mente fixa, um problema = '<strong>somos incompatíveis</strong>, não tem conserto'. Na de crescimento, um problema = algo a entender e trabalhar a dois. Habilidades de relação — comunicação, empatia — se aprendem.",
    "tip": "<strong>Como aplicar:</strong> trate o conflito como problema compartilhado a resolver, não como prova contra o outro."
   },
   {
    "ic": "person",
    "t": "Definir-se pela Rejeição",
    "b": "A mente fixa lê o término como <strong>veredito permanente</strong> sobre o próprio valor e se fixa em vingança. A de crescimento busca aprender, perdoar e seguir em frente.",
    "tip": "<strong>Para refletir:</strong> transformar mágoa em identidade de vítima/vingador aprisiona no passado."
   }
  ]
 },
 "ch07-pais-professores-treinadores": {
  "cards": [
   {
    "ic": "target",
    "t": "Elogiar o Processo",
    "b": "Elogiar a inteligência ('você é tão inteligente!') instala mente fixa; elogiar <strong>esforço, estratégia, foco e persistência</strong> instala mente de crescimento. Descreva o que a pessoa <em>fez</em>, não o que ela <em>é</em>.",
    "tip": "<strong>Antes de elogiar:</strong> 'estou elogiando quem a pessoa é, ou o que ela fez?' Só o segundo constrói crescimento."
   },
   {
    "ic": "layers",
    "t": "O Estudo do Elogio",
    "b": "Crianças elogiadas pela <strong>inteligência</strong> depois evitaram desafios, mentiram sobre as notas e <strong>pioraram</strong>; as elogiadas pelo <strong>esforço</strong> buscaram desafios e melhoraram. O elogio molda a mentalidade.",
    "tip": "<strong>Cuidado:</strong> consolar baixando o sarrafo ('nem todo mundo é bom em matemática') comunica que a capacidade é fixa."
   },
   {
    "ic": "scale",
    "t": "Padrões Altos + Apoio",
    "b": "A combinação que forma mente de crescimento: <strong>exigir muito E dar suporte</strong> para chegar lá. Só exigência vira pressão fixa; só apoio (baixar o sarrafo) comunica teto fixo.",
    "tip": "<strong>Como aplicar:</strong> trate cada erro da criança como oportunidade de ensino, não como julgamento."
   }
  ]
 },
 "ch08-mudando-mentalidades": {
  "cards": [
   {
    "ic": "steps",
    "t": "Os 4 Passos da Mudança",
    "b": "(1) <strong>Aceitar</strong>: todos têm mente fixa em parte; (2) <strong>Observar</strong> os gatilhos (desafio, crítica, sucesso alheio); (3) <strong>Nomear</strong> a persona fixa e seus medos; (4) <strong>Educá-la</strong>: reconhecer o medo e explicar o plano de seguir mesmo assim.",
    "tip": "<strong>Modelo mental:</strong> é jornada, não interruptor — a persona fixa é aliada, não inimiga."
   },
   {
    "ic": "triangle",
    "t": "A Falsa Mentalidade de Crescimento",
    "b": "O alerta da própria Dweck. NÃO é crescimento: declarar que se 'tem'; elogiar <strong>esforço sem progresso</strong>; afirmar <strong>potencial sem dar os meios</strong>; ou culpar a 'mentalidade fixa' do outro.",
    "tip": "<strong>Cuidado:</strong> banir/envergonhar a mente fixa FABRICA a falsa — eduque a persona, não a expulse."
   },
   {
    "ic": "pivot",
    "t": "Esforço com Estratégia",
    "b": "A mente de crescimento verdadeira inclui <strong>tentar novas abordagens e pedir ajuda</strong>, não apenas 'se esforçar mais'. A oficina de mentalidade (cérebro muda com o aprendizado + técnicas de estudo) melhorou adolescentes de fato.",
    "tip": "<strong>Como aplicar:</strong> 'não consigo ainda — qual a próxima estratégia?' Sem estratégia, é só clichê."
   }
  ]
 }
}
```
