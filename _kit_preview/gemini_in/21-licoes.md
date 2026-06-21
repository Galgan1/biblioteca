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

# LIVRO PARA APROFUNDAR: 21 Lições para o Século 21 — Yuval Noah Harari

**Subtítulo:** VISÃO GERAL · NAVEGAR O PRESENTE COM LUCIDEZ
**Ideia central:** Se Sapiens olhou o passado e Homo Deus o futuro, este livro encara o agora. Harari mapeia os desafios sem precedentes do século 21 — IA, biotech, pós-verdade, vazio de narrativa — e aponta a defesa final: conhece-te a ti mesmo antes que um algoritmo o faça.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-desilusao` — CAPÍTULO 1: Desilusão — o Fim das Grandes Narrativas
- `ch02-trabalho` — CAPÍTULO 2: Trabalho — a IA e a 'Classe Inútil'
- `ch03-liberdade` — CAPÍTULO 3: Liberdade — Big Data e o Hackeamento Humano
- `ch04-igualdade` — CAPÍTULO 4: Igualdade — Quem Tem os Dados Tem o Futuro
- `ch05-comunidade-civilizacao` — CAPÍTULO 5: Comunidade e Civilização
- `ch06-nacionalismo-religiao-imigracao` — CAPÍTULO 6: Nacionalismo, Religião e Imigração
- `ch07-terrorismo-guerra` — CAPÍTULO 7: Terrorismo e Guerra
- `ch08-humildade-deus-secularismo` — CAPÍTULO 8: Humildade, Deus e Secularismo
- `ch09-ignorancia-posverdade-meditacao` — CAPÍTULO 9: Ignorância, Pós-verdade e Conhece-te a Ti Mesmo

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-desilusao": {
  "cards": [
   {
    "ic": "pivot",
    "t": "O Vazio de Narrativa",
    "b": "Sem uma história compartilhada, a humanidade enfrenta crises globais sem precedentes (IA, clima, biotech) sem um relato que explique o presente e oriente o futuro. <strong>O populismo é sintoma desse vazio — não uma nova narrativa.</strong>",
    "tip": "<strong>Modelo mental:</strong> pense na narrativa como sistema operacional coletivo; sem ela, as pessoas não sabem interpretar os fatos."
   },
   {
    "ic": "clock",
    "t": "Nostalgia Não É Programa",
    "b": "Populistas vendem um passado idealizado ('voltar a ser grande') porque não têm uma história do futuro — só a rejeição da história liberal. <strong>Quando uma sociedade abraça a nostalgia, suspeite de desilusão sistêmica</strong>, não de um líder isolado.",
    "tip": "<strong>Para refletir:</strong> toda narrativa pode ruir — inclusive a que parece definitiva."
   },
   {
    "ic": "gap",
    "t": "O Vazio É Instável",
    "b": "Nenhuma história é um lugar estável de chegada. <strong>O vazio de narrativa é preenchido por fantasias regressivas e bodes expiatórios</strong>. Diagnosticar o vazio não basta — é preciso construir uma história nova para os desafios globais reais.",
    "tip": "<strong>Para refletir:</strong> sem história compartilhada, é difícil enfrentar problemas que exigem cooperação global."
   }
  ]
 },
 "ch02-trabalho": {
  "cards": [
   {
    "ic": "person",
    "t": "A Classe Inútil",
    "b": "O risco não é o desemprego clássico: é multidões economicamente <em>desnecessárias</em>. <strong>Pior que ser explorado é ser dispensável.</strong> A IA não precisa ter alma para superar o humano — basta superar o humano médio em tarefas específicas.",
    "tip": "<strong>Modelo mental:</strong> pense em 'tarefas', não 'empregos' — a IA fatia profissões em tarefas automatizáveis."
   },
   {
    "ic": "link",
    "t": "Conectividade + Atualizabilidade",
    "b": "A IA vence porque pode ser conectada em rede (toda a frota aprende junto) e atualizada de uma vez. <strong>Humanos aprendem isoladamente; a IA aprende em escala.</strong> Não é questão de alma — é de arquitetura.",
    "tip": "<strong>Para refletir:</strong> qual parte do seu trabalho é reconhecimento de padrão? Essa parte é automatizável."
   },
   {
    "ic": "spiral",
    "t": "Reinvenção em Série",
    "b": "Novos empregos surgirão — mas exigirão recriar-se aos 40, 50, 60 anos. A estabilidade profissional some; o desafio é <strong>psicológico e existencial, não só técnico</strong>. A grande aposta é aprender a reaprender.",
    "tip": "<strong>Como aplicar:</strong> a habilidade mais valiosa não é uma competência específica — é a capacidade de mudar de competência."
   }
  ]
 },
 "ch03-liberdade": {
  "cards": [
   {
    "ic": "gap",
    "t": "A Equação do Hackeamento",
    "b": "<strong>Conhecimento Biológico × Poder Computacional × Dados = hackear humanos.</strong> Quando o produto cresce o suficiente, sistemas externos preveem e moldam suas escolhas. A liberdade liberal supõe que seus sentimentos são a autoridade máxima — premissa que isso solapa.",
    "tip": "<strong>Modelo mental:</strong> a pergunta não é 'estão me vendo?' — é 'quem decide por mim: eu ou o sistema que me conhece?'"
   },
   {
    "ic": "eye",
    "t": "Ditadura Digital",
    "b": "O perigo não é só o Big Brother que vigia por fora, mas <strong>o sistema que te conhece por dentro</strong> e antecipa seus desejos. Controle por dentro é mais eficaz que controle por fora — dispensa a bota.",
    "tip": "<strong>Sinal de alerta:</strong> quando a recomendação 'perfeita' aparece, pergunte: quem sabe mais sobre você — você ou o app?"
   },
   {
    "ic": "key",
    "t": "Regular os Dados, Conhecer-se",
    "b": "Duas defesas: <strong>coletiva</strong> (regular a posse de dados — quem os concentra concentra o poder do futuro) e <strong>individual</strong> (conhecer-se melhor que o algoritmo — liga-se à meditação do capítulo final).",
    "tip": "<strong>Como aplicar:</strong> entregas de dados sem atenção são entregas de autoridade. Escolha conscientemente."
   }
  ]
 },
 "ch04-igualdade": {
  "cards": [
   {
    "ic": "layers",
    "t": "Do Econômico ao Biológico",
    "b": "Se os ricos compram aprimoramentos genéticos e cognitivos por gerações, a diferença deixa de ser de posses e passa a ser de <strong>capacidades — hereditária e biológica</strong>. A questão de igualdade vira, pela primeira vez na história, questão de espécie.",
    "tip": "<strong>Para refletir:</strong> a igualdade do século 20 foi interesseira, não generosa — sem a dependência das massas, não acontece espontaneamente."
   },
   {
    "ic": "target",
    "t": "Dados São o Novo Ativo de Poder",
    "b": "Terra (era agrária) → maquinário (era industrial) → <strong>dados (era digital)</strong>. Quem concentra dados controla o futuro. A concentração em poucas mãos (corporações/governos) gera a nova desigualdade — e ainda sem regulação madura.",
    "tip": "<strong>Como aplicar:</strong> siga o ativo de poder da era — quer entender quem manda, veja quem controla o dado."
   },
   {
    "ic": "scale",
    "t": "A Redistribuição Não Acontece Por Bondade",
    "b": "Historicamente, elites redistribuíram porque <em>precisavam</em> das massas. <strong>Tirada essa necessidade pela automação, o incentivo histórico some.</strong> A igualdade futura dependerá de escolha política consciente, não de interesse natural.",
    "tip": "<strong>Para refletir:</strong> sem a dependência das massas, a redistribuição precisa ser deliberada — não automática."
   }
  ]
 },
 "ch05-comunidade-civilizacao": {
  "cards": [
   {
    "ic": "link",
    "t": "Conectar ≠ Pertencer",
    "b": "O Facebook conecta bilhões, mas o <strong>pertencimento exige presença corporal, intimidade e responsabilidade mútua</strong>. A tecnologia que prometia unir frequentemente isola e polariza. 'Comunidade' que não te socorre quando você adoece é, na prática, uma lista de contatos.",
    "tip": "<strong>Modelo mental:</strong> use a tecnologia para agendar o encontro presencial — não no lugar dele."
   },
   {
    "ic": "wave",
    "t": "Uma Só Civilização",
    "b": "O 'choque de civilizações' assume blocos fechados e incompatíveis. Na prática, todos jogam o <strong>mesmo jogo</strong> — Estados-nação, mercados, ciência, esportes globais. As brigas são internas a uma civilização compartilhada, não entre mundos estanques.",
    "tip": "<strong>Modelo mental:</strong> procure o jogo comum — quando dois 'lados' disputam ferozmente, disputam dentro das mesmas regras."
   },
   {
    "ic": "mask",
    "t": "Identidades São Histórias Mutáveis",
    "b": "Civilizações mudam, fundem-se e se reinventam. <strong>Tratá-las como blocos eternos é ficção útil para quem quer dividir</strong>. Identidades coletivas são narrativas, não essências fixas.",
    "tip": "<strong>Para refletir:</strong> 'eles são de outra civilização' é narrativa de divisão, não fato antropológico."
   }
  ]
 },
 "ch06-nacionalismo-religiao-imigracao": {
  "cards": [
   {
    "ic": "triangle",
    "t": "Nacionalismo Benigno × Tóxico",
    "b": "Patriotismo que cuida dos compatriotas é positivo. Vira veneno quando se converte em <strong>supremacia e ódio ao estrangeiro</strong>. O problema não é amar a própria nação — é odiar as outras. O teste: o orgulho nacional exclui ou coopera?",
    "tip": "<strong>Como aplicar:</strong> lealdade em camadas — pertencer à nação E à humanidade, sem exclusão."
   },
   {
    "ic": "scale",
    "t": "Religião Dá Coesão, Não Soluções Técnicas",
    "b": "A fé é ótima para identidade e pertencimento, mas <strong>não fornece soluções técnicas para clima, IA ou vírus</strong>. Confundir os planos é erro de categoria: não peça engenharia à fé nem substituição de valores à ciência.",
    "tip": "<strong>Modelo mental:</strong> separe coesão de competência — religião e nação dão pertencimento; engenharia e política dão soluções."
   },
   {
    "ic": "key",
    "t": "O Trato da Imigração em Três Termos",
    "b": "(1) o país anfitrião acolhe; (2) o imigrante adota valores centrais; (3) com o tempo, integra-se. <strong>O debate trava porque cada lado discorda de qual termo é o decisivo — e se é dever ou favor.</strong> Nomear os três termos desarma o falso debate.",
    "tip": "<strong>Como aplicar:</strong> antes de discutir imigração, identifique qual dos três termos está em disputa."
   }
  ]
 },
 "ch07-terrorismo-guerra": {
  "cards": [
   {
    "ic": "eye",
    "t": "O Terror Como Teatro do Medo",
    "b": "O dano real do terrorismo é mínimo (menos mortos que acidentes de carro); o dano <strong>psicológico e político</strong> é o objetivo. O terrorista é militarmente fraco — sua arma é a imagem que aterroriza. <strong>Só vence se você reagir com pânico e excesso.</strong>",
    "tip": "<strong>Modelo mental:</strong> não seja o touro — ao sofrer provocação espetacular, pergunte que reação o provocador quer, e faça o contrário."
   },
   {
    "ic": "pivot",
    "t": "A Mosca e o Touro",
    "b": "A mosca não derruba o touro, mas entra em seu ouvido e o faz <strong>quebrar a própria loja de porcelana</strong>. A reação desproporcional (guerra total, suspensão de direitos) é exatamente a vitória que o terrorista busca. Negar-lhe o teatro é a defesa.",
    "tip": "<strong>Como aplicar:</strong> compare riscos com números, não manchetes — o medo do terror é inversamente proporcional ao seu dano estatístico."
   },
   {
    "ic": "mountain",
    "t": "A Tentação Fatal da Guerra",
    "b": "Na era do conhecimento, a riqueza está em capital humano e dados — que não se saqueiam por invasão. <strong>A guerra deixou de ser lucrativa</strong>, mas a ilusão da 'vitória rápida' ainda seduz líderes. O caos da guerra raramente produz o resultado previsto.",
    "tip": "<strong>Para refletir:</strong> antes de apoiar qualquer 'guerra cirúrgica', lembre: guerra é caótica e seu resultado, imprevisível."
   }
  ]
 },
 "ch08-humildade-deus-secularismo": {
  "cards": [
   {
    "ic": "person",
    "t": "Humildade Histórica",
    "b": "Judeus, cristãos, muçulmanos, hindus, chineses — cada cultura se vê como eixo da história e fonte da moral. <strong>Esse narcisismo coletivo é ficção e fonte de conflito.</strong> Suspeite de toda história em que o seu grupo é o herói do universo.",
    "tip": "<strong>Modelo mental:</strong> a humildade histórica não nega a identidade — apenas recusa o protagonismo exclusivo."
   },
   {
    "ic": "scale",
    "t": "Deus-Mistério × Deus-Legislador",
    "b": "Do inefável (o cosmos como mistério sagrado) <strong>não se deduzem regras concretas</strong> (dieta, vestuário, quem pode casar). Invocam o primeiro para autorizar o segundo — o contrabando teológico. A ética secular pergunta: 'isso causa sofrimento?' — não 'Deus permite?'",
    "tip": "<strong>Como aplicar:</strong> separe o Deus-mistério (humilde e indiscutível) do Deus-legislador (que dita regras concretas)."
   },
   {
    "ic": "leaf",
    "t": "Secularismo Como Código Positivo",
    "b": "Ser secular não é vazio nem niilismo. É comprometer-se com <strong>verdade, compaixão, igualdade, liberdade, coragem e responsabilidade</strong> — incluindo reconhecer o próprio erro. É um código exigente, com a verdade no topo.",
    "tip": "<strong>Modelo mental:</strong> trate o secularismo como um conjunto de valores que cobram honestidade — não como ausência de valores."
   }
  ]
 },
 "ch09-ignorancia-posverdade-meditacao": {
  "cards": [
   {
    "ic": "lens",
    "t": "A Ilusão do Conhecimento",
    "b": "Você acha que sabe como funciona um zíper, um vaso sanitário, a economia — até ter de explicar em detalhe. O <strong>conhecimento real está distribuído na tribo</strong>; o indivíduo acessa o todo e confunde com saber próprio. <strong>Teste: explique do zero.</strong>",
    "tip": "<strong>Como aplicar:</strong> antes de opinar com firmeza, tente explicar o mecanismo do zero — a ilusão desaba rápido."
   },
   {
    "ic": "bubble",
    "t": "O Sapiens Sempre Foi Pós-verdade",
    "b": "Dominamos o planeta porque conseguimos cooperar em massa em torno de <strong>ficções coletivas</strong> — religiões, ideologias, dinheiro, nações. A ficção partilhada é a tecnologia social fundadora. Trade-off: <strong>poder pede ficções; verdade exige renunciar a ilusões.</strong>",
    "tip": "<strong>Modelo mental:</strong> distinga ficção útil (dinheiro, direitos) de ficção tóxica — e saiba conscientemente qual você usa."
   },
   {
    "ic": "leaf",
    "t": "Conhece-te a Ti Mesmo — Como Sobrevivência",
    "b": "Harari pratica meditação Vipassana: observar a respiração, notar como a mente foge e conta histórias. A função não é religiosa — é de <strong>segurança da informação aplicada à própria mente</strong>. Se você não se conhece, um algoritmo o conhecerá por você.",
    "tip": "<strong>Como aplicar:</strong> os 4 Cs (pensamento crítico, comunicação, colaboração, criatividade) + equilíbrio emocional = currículo para o século instável."
   }
  ]
 }
}
```
