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

# LIVRO PARA APROFUNDAR: O Poder dos Quietos — Susan Cain

**Subtítulo:** VISÃO GERAL · A INTROVERSÃO COMO VANTAGEM
**Ideia central:** Vivemos sob um Ideal da Extroversão que supervaloriza o falante e o ousado — e desperdiça os dons dos quietos. Susan Cain mostra que introversão não é defeito a corrigir, mas um temperamento com base biológica e um modo particular de poder: foco, profundidade, escuta, persistência.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-o-ideal-da-extroversao` — CAPÍTULO 1: O Ideal da Extroversão
- `ch02-introversao-extroversao-e-energia` — CAPÍTULO 2: Introversão, Extroversão e Energia
- `ch03-temperamento-e-biologia` — CAPÍTULO 3: Temperamento e Biologia
- `ch04-elastico-e-tracos-livres` — CAPÍTULO 4: O Elástico e os Traços Livres
- `ch05-mito-da-colaboracao` — CAPÍTULO 5: O Mito da Colaboração
- `ch06-poder-silencioso` — CAPÍTULO 6: O Poder Silencioso
- `ch07-criar-filhos-quietos` — CAPÍTULO 7: Criar Filhos Quietos
- `ch08-relacionamentos-introvertido-extrovertido` — CAPÍTULO 8: Relacionamentos Opostos
- `ch09-quando-agir-como-o-oposto` — CAPÍTULO 9: Quando Agir como o Oposto

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-o-ideal-da-extroversao": {
  "cards": [
   {
    "ic": "eye",
    "t": "Ideal da Extroversão",
    "b": "A convicção cultural, em geral inconsciente, de que o 'eu ideal' é dominante e confortável sob os holofotes. Tornou-se o modelo medido em escolas, empresas e mídia.",
    "tip": "<strong>Como aplicar:</strong> separe estilo de substância — confiança performada ≠ competência real."
   },
   {
    "ic": "pivot",
    "t": "Caráter × Personalidade",
    "b": "Virada histórica (início do séc. XX): de uma sociedade que valorizava o <strong>caráter</strong> (integridade no privado) para uma que valoriza a <strong>personalidade</strong> (magnetismo em público). A urbanização e a cultura de vendas premiaram quem brilhava diante de estranhos.",
    "tip": "<strong>Modelo mental:</strong> o que parece 'a melhor pessoa da sala' pode ser apenas a mais barulhenta."
   },
   {
    "ic": "mask",
    "t": "O Custo do Ideal",
    "b": "Quando uma cultura supervaloriza um único tipo, desperdiça os talentos da metade diferente e empurra os quietos a atuar contra a própria natureza — com desgaste real e perda organizacional.",
    "tip": "<strong>Sinal de alerta:</strong> sempre que competência estiver sendo julgada por rapidez e volume de fala, não por qualidade de pensamento."
   }
  ]
 },
 "ch02-introversao-extroversao-e-energia": {
  "cards": [
   {
    "ic": "spark",
    "t": "Fonte de Energia",
    "b": "Introvertido: o convívio intenso <strong>gasta</strong> bateria e a quietude a <strong>recompõe</strong>. Extrovertido: a interação <strong>carrega</strong> a bateria e o isolamento a <strong>esvazia</strong>. A mesma festa carrega um e descarrega o outro.",
    "tip": "<strong>Como aplicar:</strong> ao planejar o dia, intercale interação com janelas de recuperação."
   },
   {
    "ic": "wave",
    "t": "Nível Ótimo de Estímulo",
    "b": "Cada pessoa tem um 'ponto doce' de estimulação (ruído, gente, novidade). Introvertidos atingem o ótimo com <strong>pouco</strong>; o excesso vira sobrecarga. Extrovertidos precisam de <strong>mais</strong> para se sentir vivos.",
    "tip": "<strong>Modelo mental:</strong> introversão é espectro — quase ninguém é 100% de um lado; ambiverts existem."
   },
   {
    "ic": "fork",
    "t": "Introversão ≠ Timidez",
    "b": "Timidez = dor/ansiedade na avaliação social. Introversão = preferência por ambientes de baixo estímulo. <strong>Eixos distintos</strong>: existem extrovertidos tímidos e introvertidos socialmente habilidosos e destemidos.",
    "tip": "<strong>Cuidado:</strong> confundir introversão com timidez leva a 'tratar' a pessoa errada."
   }
  ]
 },
 "ch03-temperamento-e-biologia": {
  "cards": [
   {
    "ic": "leaf",
    "t": "Alta Reatividade (Kagan)",
    "b": "~20% de bebês são <strong>altamente reativos</strong> — se agitam diante do novo. Esses bebês tendem a virar adultos mais introvertidos, cautelosos e reflexivos. Biologia dá a faixa; não o destino.",
    "tip": "<strong>Modelo mental:</strong> pense na reatividade como o ganho de um microfone — capta nuances finas e também distorce com volume alto."
   },
   {
    "ic": "mountain",
    "t": "Sensibilidade ao Estímulo",
    "b": "Introvertidos são, em média, <strong>mais sensíveis</strong> a todo tipo de estímulo (luz, ruído, gente, cafeína) — atingem a sobrecarga mais cedo e preferem ambientes calmos. Extrovertidos precisam de mais estímulo para se sentir vivos.",
    "tip": "<strong>Como aplicar:</strong> ao entender a si mesmo ou a uma criança — sobrecarregar cedo não é defeito, é o limiar de estímulo mais baixo."
   },
   {
    "ic": "triangle",
    "t": "Orquídea × Dente-de-Leão",
    "b": "O altamente reativo ('orquídea') <strong>definham</strong> em ambientes ruins, mas <strong>florescem acima da média</strong> em ambientes nutritivos. Sensibilidade é faca de dois gumes: mais vulnerável ao estresse, mais responsivo ao cuidado.",
    "tip": "<strong>Modelo mental:</strong> sensibilidade alta é dupla face — maior captação do bom e do ruim."
   }
  ]
 },
 "ch04-elastico-e-tracos-livres": {
  "cards": [
   {
    "ic": "spiral",
    "t": "Teoria do Elástico",
    "b": "Temperamento fixa a faixa, mas há elasticidade. Agimos fora do traço quando o contexto pede — mas o elástico só estica até certo ponto e volta. Forçar além do limite por tempo demais <strong>desgasta</strong>.",
    "tip": "<strong>Como aplicar:</strong> planeje 'esticar' em momentos que importam e relaxe o elástico depois — não viva esticado o tempo todo."
   },
   {
    "ic": "target",
    "t": "Traços Livres (Brian Little)",
    "b": "Podemos agir como <strong>pseudo-extrovertidos</strong> a serviço de <strong>projetos pessoais centrais</strong> — coisas que amamos, pessoas que valorizamos. Não é máscara vazia; é atuação autêntica movida por um valor interno.",
    "tip": "<strong>Modelo mental:</strong> pense no traço livre como um traje a rigor — você o veste para a ocasião que importa e depois precisa tirá-lo para respirar."
   },
   {
    "ic": "leaf",
    "t": "Nichos Restauradores",
    "b": "Após atuar fora do traço, é indispensável um <strong>nicho restaurador</strong> — lugar/momento de retorno ao eu verdadeiro. Uma pausa quieta, uma caminhada, um fim de semana sem agenda. Sem nicho, atuar fora do traço adoece.",
    "tip": "<strong>Sinal de alerta:</strong> esticar sem nicho restaurador cobra exaustão, irritabilidade e adoecimento."
   }
  ]
 },
 "ch05-mito-da-colaboracao": {
  "cards": [
   {
    "ic": "bubble",
    "t": "O Mito do Brainstorming",
    "b": "Indivíduos sozinhos (ou somados depois) geram <strong>mais e melhores</strong> ideias que grupos presenciais. Três bloqueios: preguiça social, bloqueio de produção (só um fala por vez) e apreensão de avaliação. Brainstorming eletrônico/escrito é exceção positiva.",
    "tip": "<strong>Como aplicar:</strong> para gerar ideias, deixe as pessoas pensarem sozinhas primeiro; combine depois — 'sozinhos juntos'."
   },
   {
    "ic": "lens",
    "t": "Open Office: Custo Real",
    "b": "Escritórios abertos aumentam ruído, interrupção e estresse — e correlacionam-se com <strong>queda</strong> de produtividade e satisfação. Privacidade e controle do ambiente importam para o trabalho profundo.",
    "tip": "<strong>Modelo mental:</strong> o grupo presencial amplifica o mais alto, não o mais certo."
   },
   {
    "ic": "mountain",
    "t": "Solitude e Maestria",
    "b": "Apoiada em Anders Ericsson: o aprofundamento numa habilidade quase sempre exige longas horas de concentração <strong>sozinho</strong>. Steve Wozniak projetou o primeiro Apple em noites de silêncio na HP — maestria nasceu de solitude, não de comitê.",
    "tip": "<strong>Regra:</strong> pense sozinho primeiro; reúna depois para combinar e decidir."
   }
  ]
 },
 "ch06-poder-silencioso": {
  "cards": [
   {
    "ic": "person",
    "t": "Liderança Introvertida",
    "b": "Estudo de Adam Grant: com <strong>equipes proativas</strong> (cheias de iniciativa), líderes introvertidos geram <strong>melhores resultados</strong> — escutam as ideias e dão espaço. Com equipes passivas, extrovertidos brilham mais. O ajuste líder–equipe importa.",
    "tip": "<strong>Como aplicar:</strong> lidere 'introvertido' (ouvindo, cedendo espaço) quando sua gente já tem iniciativa."
   },
   {
    "ic": "bubble",
    "t": "Negociação Silenciosa",
    "b": "O introvertido prepara mais, fala menos e ouve mais: revela o interesse real do outro e evita concessões precipitadas. <strong>Calma sob pressão</strong> é alavanca. Em negociação, o silêncio é uma pergunta.",
    "tip": "<strong>Modelo mental:</strong> quem fala menos costuma descobrir mais."
   },
   {
    "ic": "clock",
    "t": "Persistência como Poder",
    "b": "Grande parte da realização não vem de carisma, e sim de <strong>foco obstinado</strong> e capacidade de trabalhar sozinho por muito tempo num problema difícil. A quietude sustenta a maratona.",
    "tip": "<strong>Regra:</strong> entusiasmo anima; convicção e escuta sustentam a longo prazo."
   }
  ]
 },
 "ch07-criar-filhos-quietos": {
  "cards": [
   {
    "ic": "leaf",
    "t": "Ambiente Nutritivo",
    "b": "A criança altamente reativa ('orquídea') é mais vulnerável a ambientes hostis, mas <strong>rende acima da média</strong> em ambientes nutritivos: pais calorosos, previsíveis e respeitosos. O ambiente é alavanca, não detalhe.",
    "tip": "<strong>Como aplicar:</strong> dê estrutura, baixe o estímulo, valide a sensibilidade, exponha ao novo aos poucos."
   },
   {
    "ic": "steps",
    "t": "Exposição Gradual",
    "b": "Para ajudar a criança quieta/tímida a enfrentar o novo: prepare e exponha em <strong>doses pequenas e crescentes</strong>, ao lado dela. Nem forçar (empurrão bruto), nem blindar (superproteção). Os dois extremos travam o crescimento.",
    "tip": "<strong>Modelo mental:</strong> a criança quieta é como planta de sombra — murcha no sol forte, viceja na luz certa."
   },
   {
    "ic": "bulb",
    "t": "Reformular a Quietude",
    "b": "Ensine a criança a ver introversão como vantagem (foco, empatia, profundidade), não falha. <strong>A linguagem dos pais vira o monólogo interno do filho</strong>. Chame de força o que de fato é força.",
    "tip": "<strong>Cuidado:</strong> envergonhar a criança por ser quieta ('fala com a tia!') fixa a vergonha como identidade."
   }
  ]
 },
 "ch08-relacionamentos-introvertido-extrovertido": {
  "cards": [
   {
    "ic": "gap",
    "t": "Choque das Doses",
    "b": "O que recarrega um descarrega o outro. Sem nomear isso, cada um lê o outro errado: 'ele me rejeita' × 'ela me sufoca'. O correto é tratar como <strong>diferença de necessidade energética</strong>, não de afeto.",
    "tip": "<strong>Como aplicar:</strong> negocie a dose de convívio como acordo mútuo: quantas noites sociais por semana, sinais combinados, quando sair mais cedo sem culpa."
   },
   {
    "ic": "scale",
    "t": "Estilos de Conflito",
    "b": "Introvertidos tendem a <strong>evitar</strong> conflito intenso (alto estímulo emocional); extrovertidos toleram mais o calor da discussão. Reconhecer o ciclo 'persegue × se retrai' evita escalada.",
    "tip": "<strong>Modelo mental:</strong> 'ele foge' pode ser 'ele está sobrecarregado' — dê pausa antes de retomar."
   },
   {
    "ic": "link",
    "t": "Complementaridade",
    "b": "Bem ajustados, os opostos se cobrem: o extrovertido abre portas e energiza; o introvertido aprofunda, escuta e estabiliza. <strong>A diferença de dose vira ativo</strong> quando os dois se entendem.",
    "tip": "<strong>Regra:</strong> cada um estica um pouco em direção ao outro — por amor, com nicho restaurador embutido."
   }
  ]
 },
 "ch09-quando-agir-como-o-oposto": {
  "cards": [
   {
    "ic": "key",
    "t": "O Pacto de Livre Traço",
    "b": "Combine consigo (e com quem convive) em que situações vai atuar fora do traço e em troca de quais espaços de restauração. <strong>Você dá o 'show' onde importa e ganha o silêncio depois.</strong>",
    "tip": "<strong>Como aplicar:</strong> liste os poucos contextos que merecem esticar; negocie a recompensa restauradora de cada um."
   },
   {
    "ic": "target",
    "t": "Quando Vale Esticar",
    "b": "Vale agir como o oposto quando: (1) o projeto é central a você; (2) o ganho é alto; (3) você consegue se recompor depois. Não vale: por status vazio, pressão difusa, ou sem refúgio para repor energia.",
    "tip": "<strong>Regra:</strong> aja seu traço por padrão; aja o oposto por decisão deliberada — a exceção precisa de motivo e de descanso."
   },
   {
    "ic": "leaf",
    "t": "Nicho Restaurador como Contrapartida",
    "b": "Toda atuação extrovertida deve ser paga com <strong>recuperação quieta</strong>. É a condição que torna o esticar saudável em vez de tóxico. Viver permanentemente fora do traço é caminho do esgotamento.",
    "tip": "<strong>Sinal de alerta:</strong> esticar sem refúgio cobra com exaustão e irritabilidade."
   }
  ]
 }
}
```
