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

# LIVRO PARA APROFUNDAR: O Mundo de Sofia — Jostein Gaarder

**Subtítulo:** VISÃO GERAL · HISTÓRIA DA FILOSOFIA EM FORMA DE ROMANCE
**Ideia central:** Sofia Amundsen, 14 anos, começa a receber cartas misteriosas com duas perguntas: 'Quem é você?' e 'De onde vem o mundo?' O remetente é Alberto Knox, um filósofo que a conduz por toda a história da filosofia ocidental — dos pré-socráticos a Sartre. No caminho, descobrem que são personagens de um livro.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-espanto-e-a-moldura` — CAPÍTULO 1: O Espanto e a Moldura
- `ch02-pre-socraticos` — CAPÍTULO 2: Os Pré-socráticos — do Mito ao Logos
- `ch03-socrates-platao-aristoteles` — CAPÍTULO 3: Sócrates, Platão e Aristóteles
- `ch04-helenismo-e-idade-media` — CAPÍTULO 4: Helenismo e Idade Média
- `ch05-renascenca-descartes` — CAPÍTULO 5: Renascença e Descartes
- `ch06-spinoza-empiristas` — CAPÍTULO 6: Spinoza e os Empiristas
- `ch07-kant` — CAPÍTULO 7: Kant — a Grande Síntese
- `ch08-hegel-kierkegaard-marx-freud` — CAPÍTULO 8: Hegel, Kierkegaard e os Mestres da Suspeita
- `ch09-sartre-virada-meta` — CAPÍTULO 9: Sartre, a Virada Meta e o Cosmos

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-espanto-e-a-moldura": {
  "cards": [
   {
    "ic": "eye",
    "t": "O Coelho na Cartola",
    "b": "O universo é o coelho que o mágico tira da cartola. Nós nascemos na <strong>ponta dos pelos finos</strong> (a criança que acha tudo estranho) e vamos deslizando para o conforto do pelo, deixando de ver o truque. Filósofos são os que tentam subir pelos pelos para espiar o mágico nos olhos.",
    "tip": "<strong>Como aplicar:</strong> pense no adulto como alguém que 'afundou no pelo do coelho' — filosofar é voltar a ser criança intelectualmente, sem perder o rigor."
   },
   {
    "ic": "bulb",
    "t": "Perguntas Valem Mais que Respostas",
    "b": "Filosofia não é acumular respostas prontas: é a arte de fazer as perguntas e de <strong>não se conformar</strong>. O espanto não é ingenuidade — é o ponto de partida de um pensamento que depois se torna disciplinado.",
    "tip": "<strong>Modelo mental:</strong> use o espanto como teste — se algo deixou de parecer estranho (a consciência, o tempo, o existir), você parou de filosofar sobre isso."
   },
   {
    "ic": "bubble",
    "t": "Mito × Razão",
    "b": "A filosofia surge quando se troca a explicação mítica (os deuses fazem chover) pela explicação <strong>natural e racional</strong>. Não é o fim do encantamento — é a recusa de tomar o mundo como óbvio mesmo sem deuses.",
    "tip": "<strong>Como aplicar:</strong> toda vez que você aceita uma explicação 'porque sempre foi assim', está do lado do mito; filosofar é pedir a justificativa."
   }
  ]
 },
 "ch02-pre-socraticos": {
  "cards": [
   {
    "ic": "wave",
    "t": "Tudo Flui × Nada Muda",
    "b": "<strong>Heráclito</strong>: 'panta rhei' — tudo flui, ninguém entra duas vezes no mesmo rio; o logos é a unidade dos opostos. <strong>Parmênides</strong>: o ser é imutável, a mudança é ilusão dos sentidos — só a razão revela o real. O primeiro grande eixo da filosofia.",
    "tip": "<strong>Modelo mental:</strong> Heráclito × Parmênides = confie nos sentidos × confie só na razão. Toda a história posterior oscila entre esses polos."
   },
   {
    "ic": "layers",
    "t": "A Busca pela Physis",
    "b": "Tales (água), Anaximandro (o indefinido/ápeiron), Anaxímenes (ar): a ousadia de buscar <strong>um princípio natural unificador</strong> para tudo. Não é adivinhação: é o gesto de explicar o complexo por algo interno à natureza, sem recorrer aos deuses.",
    "tip": "<strong>Como aplicar:</strong> pense em Tales não pelo resultado (água) mas pelo método — uma única pergunta racional para explicar tudo."
   },
   {
    "ic": "link",
    "t": "Demócrito e os Átomos",
    "b": "Partículas eternas e indivisíveis (<strong>átomos</strong>) que, combinadas em diferentes arranjos, formam tudo. O primeiro materialismo completo — e o avô do método científico. A ideia de que o complexo se explica por partes simples e mecânicas, sem propósito divino.",
    "tip": "<strong>Modelo mental:</strong> o materialismo de Demócrito é tão antigo quanto a filosofia — a ciência moderna é sua descendente direta."
   }
  ]
 },
 "ch03-socrates-platao-aristoteles": {
  "cards": [
   {
    "ic": "bubble",
    "t": "A Maiêutica Socrática",
    "b": "Sócrates 'parte ideias' pelo diálogo: ele não ensina, faz pensar. 'Só sei que nada sei' — a consciência da própria ignorância é o ponto de partida do conhecimento. <strong>Conhecimento = virtude</strong>; a ignorância é a raiz do mal.",
    "tip": "<strong>Como aplicar:</strong> faça perguntas em vez de dar respostas — a maiêutica revela o que o interlocutor já sabe mas não sabia que sabia."
   },
   {
    "ic": "mountain",
    "t": "O Mundo das Ideias",
    "b": "As <strong>Formas</strong> eternas e perfeitas (o Cavalo em si, o Belo em si) existem num mundo à parte; o mundo sensível é cópia imperfeita. A <strong>alegoria da caverna</strong>: prisioneiros tomam sombras por realidade — o filósofo se liberta, vê a luz e volta para libertar os outros.",
    "tip": "<strong>Modelo mental:</strong> use a caverna para qualquer crítica de ilusão — o que tomamos por real pode ser sombra de algo mais verdadeiro."
   },
   {
    "ic": "lens",
    "t": "Aristóteles — A Forma nas Coisas",
    "b": "Aristóteles 'traz Platão de volta à terra': a forma está <strong>nas coisas</strong>, não num céu à parte. O conhecimento começa pelos sentidos; a lógica e as quatro causas explicam qualquer fenômeno. A virtude é o <strong>justo meio</strong> entre excessos.",
    "tip": "<strong>Sinal de alerta:</strong> Platão × Aristóteles = o segundo grande eixo — toda a filosofia medieval e moderna escolhe um lado ou tenta síntese."
   }
  ]
 },
 "ch04-helenismo-e-idade-media": {
  "cards": [
   {
    "ic": "leaf",
    "t": "Filosofia como Arte de Viver",
    "b": "<strong>Estoicos</strong>: viver conforme a razão; aceitar o destino com serenidade. <strong>Epicuristas</strong>: o maior prazer é a ausência de dor (ataraxia) — não a devassidão. <strong>Cínicos</strong>: felicidade na independência dos bens materiais. Helenismo = filosofia-terapia.",
    "tip": "<strong>Como aplicar:</strong> o estoico Epicteto, escravo, distinguia o que depende de nós (o juízo) do que não depende — e só cobrava a si o primeiro."
   },
   {
    "ic": "scale",
    "t": "Agostinho × Tomás — Fé e Razão",
    "b": "<strong>Agostinho</strong> (Platão batizado): as Ideias estão na mente de Deus; a fé busca o entendimento. <strong>Tomás de Aquino</strong> (Aristóteles batizado): razão e fé não se contradizem; a razão pode chegar a Deus pelo mundo. Dois modos de conciliar o mesmo eixo.",
    "tip": "<strong>Modelo mental:</strong> a Idade Média não foi 'buraco negro' — foi a ponte que preservou e integrou a herança grega na cultura cristã."
   },
   {
    "ic": "spiral",
    "t": "Neoplatonismo — A Emanação do Uno",
    "b": "Plotino: tudo <strong>emana</strong> do Uno como a luz do sol — a matéria é a borda mais escura dessa emanação. O objetivo é retornar ao Uno pelo caminho interior. O misticismo filosófico que influenciará Agostinho e, mais tarde, o Romantismo.",
    "tip": "<strong>Modelo mental:</strong> o neoplatonismo conecta Platão ao misticismo cristão — o Uno de Plotino será depois identificado com Deus."
   }
  ]
 },
 "ch05-renascenca-descartes": {
  "cards": [
   {
    "ic": "bulb",
    "t": "A Dúvida Metódica",
    "b": "Descartes decide duvidar de <strong>tudo o que pode ser posto em dúvida</strong> (sentidos, sonho, até a matemática), para encontrar o que resiste. Não é ceticismo: é uma <em>etapa</em> para chegar à certeza — derruba primeiro tudo que pode tremer e vê o que sobra de pé.",
    "tip": "<strong>Como aplicar:</strong> use a dúvida metódica como ferramenta — para achar o que é sólido, derrube primeiro tudo o que pode tremer."
   },
   {
    "ic": "spark",
    "t": "'Penso, Logo Existo'",
    "b": "<em>Cogito, ergo sum</em>: mesmo enganado, há um eu que pensa; eis a primeira certeza indubitável. O <strong>ponto de Arquimedes da modernidade</strong> — a filosofia deixa de partir do cosmos e passa a partir do sujeito consciente.",
    "tip": "<strong>Modelo mental:</strong> o cogito é uma virada copernicana — não o mundo me define, sou eu que, ao pensar, certifico que existo."
   },
   {
    "ic": "gap",
    "t": "O Problema do Dualismo",
    "b": "Descartes separa duas substâncias: <strong>res cogitans</strong> (pensamento, alma) e <strong>res extensa</strong> (matéria, extensão). Corpo e mente são realidades distintas. Abre o problema filosófico que ocupará toda a modernidade: como e onde interagem?",
    "tip": "<strong>Sinal de alerta:</strong> Descartes ainda precisa de Deus para reconstruir a confiança na realidade externa — o cogito prova que existe, não que o mundo externo é real."
   }
  ]
 },
 "ch06-spinoza-empiristas": {
  "cards": [
   {
    "ic": "leaf",
    "t": "Deus sive Natura",
    "b": "Spinoza: 'Deus, ou seja, a Natureza' — uma só substância infinita; tudo é modo dela. Ver as coisas <em>sub specie aeternitatis</em> (do ponto de vista da eternidade). <strong>Panteísmo</strong> que recusa o dualismo cartesiano: não há dois mundos, só um.",
    "tip": "<strong>Modelo mental:</strong> para Spinoza, estudar a natureza é estudar Deus — não há separação entre criador e criatura."
   },
   {
    "ic": "eye",
    "t": "A Tabula Rasa e o Esse Est Percipi",
    "b": "<strong>Locke</strong>: a mente nasce folha em branco, a experiência escreve nela. <strong>Berkeley</strong>: 'existir é ser percebido' — só existem espíritos e suas ideias; a matéria como tal não existe fora da percepção. Semente filosófica da virada meta do livro.",
    "tip": "<strong>Como aplicar:</strong> o 'esse est percipi' de Berkeley antecipa a ideia de Sofia existir por ser pensada/escrita pelo major Knag."
   },
   {
    "ic": "lens",
    "t": "Hume Dissolve a Causalidade",
    "b": "Não vemos causas — vemos <strong>sucessão de eventos que vira hábito</strong> de esperar B depois de A. Não há 'eu' substancial: só um feixe de percepções. O ceticismo radical de Hume 'acorda Kant do sono dogmático' e força a grande síntese.",
    "tip": "<strong>Sinal de alerta:</strong> antes de afirmar uma conexão necessária, pergunte com Hume — eu a observo ou apenas me acostumei a esperá-la?"
   }
  ]
 },
 "ch07-kant": {
  "cards": [
   {
    "ic": "lens",
    "t": "Os Óculos da Mente",
    "b": "<strong>Espaço, tempo e causalidade</strong> são formas a priori da mente — 'óculos' que toda mente humana usa. Não estão 'lá fora' nas coisas: são as lentes pelas quais tudo é percebido. Por isso a ciência é possível (todos usam os mesmos óculos) mas limitada ao fenômeno.",
    "tip": "<strong>Modelo mental:</strong> se você usasse óculos vermelhos colados, veria tudo vermelho e nunca saberia a cor real — espaço, tempo e causa são esses óculos."
   },
   {
    "ic": "gap",
    "t": "Fenômeno × Coisa-em-Si",
    "b": "Conhecemos o mundo como ele <strong>nos aparece</strong> (fenômeno), nunca como ele é em si mesmo (Ding an sich — inacessível). Kant não diz que o mundo é ilusão; diz que só temos acesso a ele filtrado pelas nossas estruturas mentais.",
    "tip": "<strong>Sinal de alerta:</strong> a causalidade não é negada como em Hume — ela é garantida, mas como forma do nosso entendimento, não propriedade das coisas em si."
   },
   {
    "ic": "scale",
    "t": "O Imperativo Categórico",
    "b": "Lei moral interior: '<strong>age só segundo a máxima que possas querer que se torne lei universal</strong>' e 'trata a humanidade sempre como fim, nunca apenas como meio'. A moralidade nasce de dentro, da razão autônoma — não de recompensa nem medo.",
    "tip": "<strong>Como aplicar:</strong> use como teste moral — universalize sua ação ('e se todos fizessem isso?'); se ela se autodestrói ao virar regra geral, é imoral."
   }
  ]
 },
 "ch08-hegel-kierkegaard-marx-freud": {
  "cards": [
   {
    "ic": "spiral",
    "t": "A Dialética de Hegel",
    "b": "A verdade é <strong>histórica e processual</strong>: tese → antítese → síntese, em ciclo contínuo. O Espírito (Geist) se desdobra na história. Use a dialética para ler conflitos: raramente um lado está totalmente certo — o avanço costuma ser a síntese que conserva o melhor de cada polo.",
    "tip": "<strong>Como aplicar:</strong> diante de um impasse, pergunte — qual seria a síntese que conserva o melhor da tese e da antítese?"
   },
   {
    "ic": "person",
    "t": "Kierkegaard — O Indivíduo Concreto",
    "b": "Contra o sistema abstrato de Hegel: importa o <strong>singular que existe, escolhe e sofre</strong>. 'A verdade é subjetividade.' Os três estágios: estético (prazer/instante) → ético (dever, responsabilidade) → religioso (fé, salto). Pai do existencialismo.",
    "tip": "<strong>Modelo mental:</strong> Kierkegaard como antídoto ao excesso de sistema — 'e o indivíduo concreto, que precisa escolher e viver, onde fica?'"
   },
   {
    "ic": "triangle",
    "t": "Os Três Mestres da Suspeita",
    "b": "<strong>Marx</strong>: a base econômica determina as ideias (materialismo histórico). <strong>Darwin</strong>: o homem evoluiu, não foi criado. <strong>Freud</strong>: não somos senhores em nossa própria casa (o inconsciente governa). Os três descentram o homem — e tornam mais urgente a pergunta existencialista pela liberdade.",
    "tip": "<strong>Como aplicar:</strong> use a suspeita como método — por trás de uma ideia 'neutra', pergunte a quem serve (Marx), que herança biológica a condiciona (Darwin), que desejo recalcado a move (Freud)."
   }
  ]
 },
 "ch09-sartre-virada-meta": {
  "cards": [
   {
    "ic": "key",
    "t": "'Condenados a ser Livres'",
    "b": "Não há natureza humana dada de antemão: primeiro existimos, depois nos definimos pelas <strong>escolhas</strong>. A liberdade é inescapável — até não escolher é uma escolha. Daí a angústia: somos totalmente responsáveis por quem nos tornamos.",
    "tip": "<strong>Sinal de alerta:</strong> 'má-fé' é autoengano — quando diz 'não tive escolha' ou 'é só o meu trabalho', está fugindo de assumir a própria liberdade."
   },
   {
    "ic": "constellation",
    "t": "A Virada Meta",
    "b": "Sofia e Alberto descobrem que são <strong>personagens de um livro</strong> que o major Knag escreve para a filha Hilde. Realiza o 'esse est percipi' de Berkeley (existir é ser percebido/escrito) e o existencialismo de Sartre (existir = agir por si para além do roteiro). A pergunta 'Quem é você?' torna-se vertiginosa.",
    "tip": "<strong>Modelo mental:</strong> use as camadas (Knag → Sofia; Gaarder → Hilde; você lendo) para pensar — quantas 'molduras' cercam minha sensação de realidade?"
   },
   {
    "ic": "eye",
    "t": "O Cosmos e o Espanto Final",
    "b": "O livro fecha onde abriu: no espanto. Somos <strong>poeira de estrelas</strong> — os átomos do nosso corpo foram forjados em estrelas extintas. O ser humano é a parte do cosmos que pergunta sobre o cosmos. A ciência explica o 'como'; o espanto filosófico diante do 'que haja algo' permanece.",
    "tip": "<strong>Como aplicar:</strong> ao perceber a escala do universo e nossa origem estelar, o trivial recupera o caráter de milagre — e o espanto retorna."
   }
  ]
 }
}
```
