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

# LIVRO PARA APROFUNDAR: Realismo Capitalista — Mark Fisher

**Subtítulo:** VISÃO GERAL · NÃO HÁ ALTERNATIVA?
**Ideia central:** É mais fácil imaginar o fim do mundo do que o fim do capitalismo. Mark Fisher mapeia a atmosfera invisível que torna o pós-capitalismo impensável antes mesmo de ser examinado — e os três Reais (saúde mental, ecologia, burocracia) que furam essa superfície para mostrar que há alternativa.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-fim-do-mundo` — CAPÍTULO 1: É Mais Fácil Imaginar o Fim do Mundo
- `ch02-precorporacao` — CAPÍTULO 2: Precorporação e Anticapitalismo Gestual
- `ch03-os-tres-reais` — CAPÍTULO 3: Capitalismo e o Real
- `ch04-impotencia-reflexiva` — CAPÍTULO 4: Impotência Reflexiva e Hedonia Depressiva
- `ch05-stalinismo-de-mercado` — CAPÍTULO 5–6: Pós-Fordismo e Stalinismo de Mercado
- `ch06-dreamwork-central-de-trocas` — CAPÍTULO 7–8: Trabalho de Sonho e a Estrutura Invisível
- `ch07-supernanny-marxista` — CAPÍTULO 9: Supernanny Marxista — a Saída

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-fim-do-mundo": {
  "cards": [
   {
    "ic": "gap",
    "t": "TINA — Não Há Alternativa",
    "b": "O slogan de Thatcher virou condição ontológica. O capitalismo se apresenta como o próprio campo do real — <strong>opera como pano de fundo, não como tese</strong>. Funciona melhor quanto menos é percebido como ideologia.",
    "tip": "<strong>Como aplicar:</strong> nomeie o realismo capitalista como construção política, não como destino — isso já é o primeiro golpe."
   },
   {
    "ic": "eye",
    "t": "A Esterilidade da Imaginação",
    "b": "Após 1989, a queda do bloco soviético removeu o \"fora\" de onde a crítica falava. A imaginação apocalíptica prolifera (<em>Filhos da Esperança</em>) porque <strong>a imaginação pós-capitalista secou</strong>. A força do sistema está em fazer o pós-capitalismo parecer impossível, não em provar que o capitalismo é bom.",
    "tip": "<strong>Modelo mental:</strong> o realismo capitalista é o ar da sala, não um quadro na parede — ninguém o defende porque ninguém o vê."
   },
   {
    "ic": "layers",
    "t": "Subsunção Real da Cultura",
    "b": "O capitalismo não só ocupa a economia — coloniza o inconsciente, o desejo, o sonho e a imaginação. Não sobra \"fora\" de onde criticá-lo. A cultura que deveria resistir <strong>já vem pré-capturada</strong>.",
    "tip": "<strong>Sinal de alerta:</strong> quando a dissidência cultural vem com etiqueta de preço e patrocinador, o capitalismo já a digeriu."
   }
  ]
 },
 "ch02-precorporacao": {
  "cards": [
   {
    "ic": "mask",
    "t": "Precorporação",
    "b": "A formatação <strong>antecipada</strong> de desejos e rebeldias pela cultura capitalista — a dissidência já vem pré-empacotada antes de existir. Mais sutil que a cooptação (que absorve depois): formata antes. A camiseta do Che, o capitalismo consciente.",
    "tip": "<strong>Como aplicar:</strong> pergunte \"esse gesto crítico está sendo vendido de volta para mim como identidade ou produto?\""
   },
   {
    "ic": "bubble",
    "t": "Interpassividade",
    "b": "O filme/produto protesta por você; você assiste à crítica e <strong>fica quite</strong>, livre para continuar consumindo. WALL-E retrata a humanidade consumista e a plateia ri de si — compra depois os brinquedos do filme. <strong>Sentir-se crítico não é agir politicamente.</strong>",
    "tip": "<strong>Modelo mental:</strong> pense na crítica pop ao capital como válvula de escape — libera a pressão para que a máquina não exploda."
   },
   {
    "ic": "triangle",
    "t": "Anticapitalismo Gestual",
    "b": "A crítica ao \"vilão corporação maligna\" circula dentro do capitalismo e o reabastece com a sensação de que já estamos cientes do problema. <strong>Confirma que o problema são empresas más isoladas, não a estrutura.</strong>",
    "tip": "<strong>Sinal de alerta:</strong> denunciar a \"corporação maligna\" é o anticapitalismo que o capitalismo adora — isenta a máquina, culpa o operador."
   }
  ]
 },
 "ch03-os-tres-reais": {
  "cards": [
   {
    "ic": "triangle",
    "t": "Os Três Reais",
    "b": "<strong>(1) Epidemia de transtornos mentais</strong> · <strong>(2) Catástrofe ecológica</strong> · <strong>(3) Proliferação burocrática</strong>. Cada um é um limite que o sistema trata como falha pontual — nunca como sintoma estrutural. O Real não se argumenta: ele irrompe.",
    "tip": "<strong>Modelo mental:</strong> pense no Real como a rachadura que o reboco esconde — o sistema repinta a parede em vez de olhar a estrutura."
   },
   {
    "ic": "person",
    "t": "Privatização do Estresse",
    "b": "Transferir ao indivíduo (química cerebral, \"resiliência\", terapia, coaching) o sofrimento de causa social — <strong>despolitizando-o</strong>. Onde o sistema diz \"problema individual\", procure o sintoma estrutural recalcado.",
    "tip": "<strong>Como aplicar:</strong> repolitize: troque \"o que há de errado comigo?\" por \"o que há de errado no sistema que adoece tanta gente?\""
   },
   {
    "ic": "leaf",
    "t": "Sustentabilidade Como Negação",
    "b": "O capitalismo não pode encarar que crescimento infinito num planeta finito é o problema — então trata o ambiente como <strong>nicho de mercado verde</strong>. A crise ecológica vira oportunidade de produto, não chamado à mudança estrutural.",
    "tip": "<strong>Sinal de alerta:</strong> tratar a crise ecológica como problema de comportamento do consumidor desloca a responsabilidade da estrutura para o indivíduo."
   }
  ]
 },
 "ch04-impotencia-reflexiva": {
  "cards": [
   {
    "ic": "gap",
    "t": "Impotência Reflexiva",
    "b": "A crença autorrealizável de que, mesmo sabendo que a situação é ruim, <strong>qualquer ação é inútil</strong> — e por isso nada se faz, o que confirma a impotência. Distinga \"não saber\" de \"saber e mesmo assim não agir\" — a segunda é a patologia específica do realismo capitalista.",
    "tip": "<strong>Modelo mental:</strong> a impotência reflexiva é profecia que se cumpre — \"não adianta\" produz a inação que prova o \"não adianta\"."
   },
   {
    "ic": "wave",
    "t": "Hedonia Depressiva",
    "b": "Não é incapacidade de sentir prazer (anedonia clássica) — é <strong>incapacidade de fazer outra coisa que não buscar prazer raso</strong>. O sujeito rola o feed sem parar e ainda assim sente vazio. O prazer existe; o preenchimento, não.",
    "tip": "<strong>Como aplicar:</strong> o aluno que mexe no celular em aula não é rebelde — é incapaz de tolerar o silêncio que o estímulo constante destruiu."
   },
   {
    "ic": "scale",
    "t": "Comunismo Liberal (o Anticapitalismo que o Capital Adora)",
    "b": "A figura do empresário-filantropo (Davos, Soros, Gates) que pratica caridade <em>dentro</em> do sistema, <strong>neutralizando a crítica ao próprio sistema que o enriquece</strong>. A filantropia do bilionário é o anticapitalismo que o capitalismo adora.",
    "tip": "<strong>Sinal de alerta:</strong> mais informação e consciência não bastam para mobilizar — a saída da impotência reflexiva é política e coletiva, não individual."
   }
  ]
 },
 "ch05-stalinismo-de-mercado": {
  "cards": [
   {
    "ic": "clock",
    "t": "\"Não Se Apegue a Nada\" — Pós-Fordismo",
    "b": "O regime de trabalho precário, multitarefa e em reconfiguração permanente é a <strong>causa material</strong> da epidemia de adoecimento. \"Flexibilidade\" e \"resiliência\" são nomes elegantes para transferir o custo do sistema ao indivíduo.",
    "tip": "<strong>Como aplicar:</strong> repolitize a saúde mental — troque \"o que há de errado comigo?\" por \"que tipo de sofrimento este regime de trabalho fabrica?\""
   },
   {
    "ic": "wrench",
    "t": "Stalinismo de Mercado",
    "b": "O que importa não é o trabalho real, mas <strong>representar o trabalho</strong> (relatórios, metas, PR, auditoria). Como no stalinismo importava a propaganda da produção — não a produção. O neoliberalismo multiplica a burocracia, agora privatizada.",
    "tip": "<strong>Modelo mental:</strong> localize onde a energia institucional vai para parecer que se trabalha (auditoria, branding interno) em vez de para o trabalho em si."
   },
   {
    "ic": "mask",
    "t": "Ontologia Empresarial",
    "b": "A pressuposição naturalizada de que tudo — escola, hospital, arte — deve ser gerido como empresa. O <strong>grande Outro</strong> (Lacan) é a plateia imaginária para quem as métricas são performadas: ninguém acredita nelas, todos as produzem.",
    "tip": "<strong>Sinal de alerta:</strong> mais métrica ≠ mais qualidade — a metrificação desloca o esforço da coisa para o símbolo da coisa (lei de Goodhart)."
   }
  ]
 },
 "ch06-dreamwork-central-de-trocas": {
  "cards": [
   {
    "ic": "spiral",
    "t": "Trabalho de Sonho e Disavowal",
    "b": "A ideologia capitalista <strong>reconcilia contradições sem que ninguém perceba</strong> — como num sonho. O disavowal (\"sabe muito bem, mas mesmo assim…\") é o cinismo funcional: a crença mora nos atos, não na cabeça. Apontar a contradição não basta.",
    "tip": "<strong>Exemplo histórico:</strong> 2008 — décadas pregando \"o mercado se autorregula\"; na crise, resgates bilionários do Estado sem que a doutrina fosse abalada. Trabalho de sonho perfeito."
   },
   {
    "ic": "clock",
    "t": "Distúrbio de Memória",
    "b": "O apagamento da continuidade histórica que impede comparar o discurso de agora com o de antes — a <strong>memória política é desligada</strong>. \"Restaurar a memória histórica\" — lembrar o que foi dito ontem — é um ato político.",
    "tip": "<strong>Como aplicar:</strong> o cinismo (\"não acredito em nada disso\") não protege da ideologia — ela mora nos atos, não nas convicções."
   },
   {
    "ic": "gap",
    "t": "Não Há Central de Trocas",
    "b": "Quando algo dá errado, a culpa vai para o indivíduo ou para uma burocracia abstrata — o capitalismo não tem rosto nem endereço, então é inimputável. <strong>Pergunte: \"a quem esta narrativa atribui a culpa — e a quem poupa?\"</strong>",
    "tip": "<strong>Sinal de alerta:</strong> responsabilizar o \"consumidor consciente\" pelo desastre ecológico é o deslocamento que isenta a estrutura e produz culpa privada."
   }
  ]
 },
 "ch07-supernanny-marxista": {
  "cards": [
   {
    "ic": "scale",
    "t": "A Supernanny Marxista",
    "b": "A metáfora-proposta: uma <strong>autoridade coletiva, racional e democrática</strong> que diz \"até aqui\" onde o mercado só estimula desejo. Como a Supernanny que entra em lares caóticos — sem repressão autoritária, com limites claros e consistentes.",
    "tip": "<strong>Como aplicar:</strong> identifique onde o \"deixa o desejo correr solto\" do mercado precisa de um limite coletivo decidido democraticamente — ex.: racionamento de recursos diante do colapso ecológico."
   },
   {
    "ic": "mountain",
    "t": "Indulgência Não é Liberdade",
    "b": "O capitalismo tardio não governa pela proibição — governa pela <strong>estimulação sem fim</strong>. A ausência de limites não gera sujeitos autônomos: gera consumidores dependentes e ansiosos. O mercado como o pai ausente que tudo permite.",
    "tip": "<strong>Modelo mental:</strong> a permissividade não é liberdade — é abandono. Limites coletivos são condição de liberdade real, não sua negação."
   },
   {
    "ic": "spark",
    "t": "Contra-Hegemonia — Reabrir o Horizonte",
    "b": "A tarefa estratégica: <strong>tornar o impensável de novo pensável</strong>, mostrando que o \"não há alternativa\" é uma escolha política, não um fato. Até pequenas ações contra-hegemônicas podem fissurar a aparência de inevitabilidade.",
    "tip": "<strong>Como aplicar:</strong> não espere a revolução total — para Fisher, mesmo ações imperfeitas coordenadas racham o mito do TINA."
   }
  ]
 }
}
```
