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

# LIVRO PARA APROFUNDAR: O Corpo Guarda as Marcas — Bessel van der Kolk

**Subtítulo:** VISÃO GERAL · CÉREBRO, MENTE E CORPO NA CURA DO TRAUMA
**Ideia central:** O trauma não é um evento do passado que se conta: é uma marca viva, gravada no corpo e no cérebro, que segue reorganizando a percepção e a fisiologia no presente. Van der Kolk mostra por que só falar não cura — e como a amígdala (alarme), o nervo vago, a janela de tolerância e a memória traumática explicam o sofrimento, abrindo as vias de cura que alcançam o corpo: EMDR, yoga, neurofeedback, IFS, ritmo e teatro.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-a-redescoberta-do-trauma` — CAPÍTULOS 1–3: A Redescoberta do Trauma
- `ch04-correndo-pela-vida` — CAPÍTULO 4: Correndo pela Vida — a Anatomia da Sobrevivência
- `ch05-conexoes-corpo-cerebro` — CAPÍTULO 5: Conexões Corpo-Cérebro
- `ch06-perdendo-o-corpo` — CAPÍTULO 6: Perdendo o Corpo, Perdendo o Self
- `ch07-apego-e-sintonia` — CAPÍTULOS 7–9: As Mentes das Crianças
- `ch11-memoria-traumatica` — CAPÍTULOS 11–12: A Marca do Trauma
- `ch13-curar-janela-de-tolerancia` — CAPÍTULO 13: Curar-se do Trauma — Apropriar-se de Si
- `ch14-linguagem` — CAPÍTULO 14: Linguagem — Milagre e Tirania
- `ch15-emdr` — CAPÍTULO 15: Soltar o Passado — EMDR
- `ch16-yoga` — CAPÍTULO 16: Aprender a Habitar o Corpo — Yoga
- `ch17-ifs` — CAPÍTULO 17: Juntar as Peças — Autoliderança e IFS
- `ch19-neurofeedback-teatro` — CAPÍTULOS 18–20: Refazer a Fiação e a Voz Comunal

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-a-redescoberta-do-trauma": {
  "cards": [
   {
    "ic": "wave",
    "t": "Trauma é Marca Viva",
    "b": "Trauma não é o evento, mas <strong>a marca</strong> que ele deixa em mente, cérebro e corpo quando excede a capacidade de processar. Não é recordado como história — é revivido como sensação no agora.",
    "tip": "<strong>Modelo mental:</strong> pense num disco riscado — o presente toca, mas o cérebro pula de volta ao sulco antigo."
   },
   {
    "ic": "bubble",
    "t": "Afasia do Trauma",
    "b": "Ao reviver o trauma no scanner, acende a área visual/emocional e <strong>apaga a área da fala (Broca)</strong>. É o 'terror sem palavras': a vítima não acha palavras porque o cérebro verbal saiu do ar.",
    "tip": "<strong>Para refletir:</strong> se a marca é corporal e pré-verbal, falar sobre ela não basta — e pode reativar sem curar."
   },
   {
    "ic": "spiral",
    "t": "Reencenação",
    "b": "A compulsão de <strong>repetir, agir ou recriar</strong> a situação traumática sem reconhecê-la. O sintoma (hipervigilância, entorpecimento, reencenação) foi solução de sobrevivência travada no 'ligado'.",
    "tip": "<strong>Como aplicar:</strong> trate o sintoma como adaptação, não defeito — foi o que salvou a pessoa, ficou aceso depois do perigo."
   }
  ]
 },
 "ch04-correndo-pela-vida": {
  "cards": [
   {
    "ic": "eye",
    "t": "Alarme × Torre",
    "b": "A <strong>amígdala</strong> detecta perigo e dispara instantaneamente. O <strong>córtex pré-frontal medial</strong> avalia o contexto e modula o medo. No trauma: alarme sensível demais, torre fraca demais.",
    "tip": "<strong>Regra:</strong> reação 'desproporcional' = o alarme venceu a torre."
   },
   {
    "ic": "layers",
    "t": "Cérebro de Dois Andares",
    "b": "O 'porão' reptiliano/límbico cuida da sobrevivência; o 'andar de cima' (neocórtex/pré-frontal) raciocina. O trauma <strong>rompe a escada</strong> entre eles — o porão grita e o andar racional não escuta.",
    "tip": "<strong>Como aplicar:</strong> a cura precisa de duas vias — top-down (observar/nomear) e bottom-up (respirar/mover/ritmo)."
   },
   {
    "ic": "clock",
    "t": "Hipocampo Sem Data",
    "b": "O <strong>hipocampo</strong> contextualiza e data a memória, mas o cortisol do estresse o prejudica. Por isso o trauma fica 'sem data', sempre presente. Luta, fuga e — quando ambas falham — <strong>congelamento</strong>.",
    "tip": "<strong>Para refletir:</strong> congelamento/colapso é resposta neurobiológica, não passividade nem consentimento."
   }
  ]
 },
 "ch05-conexoes-corpo-cerebro": {
  "cards": [
   {
    "ic": "link",
    "t": "Teoria Polivagal",
    "b": "O nervo vago opera em escada: (1) <strong>engajamento social</strong> (acalmar-se via rosto/voz/conexão), (2) <strong>mobilização</strong> (luta/fuga), (3) <strong>colapso</strong> (congelamento, dissociação). Subimos a escada na cura.",
    "tip": "<strong>Modelo mental:</strong> primeiro tento conexão; se falha, luto/fujo; se falha, colapso."
   },
   {
    "ic": "person",
    "t": "Segurança é Social",
    "b": "O sistema de engajamento social liga coração, rosto, voz e ouvido. Quando ativo, ele <strong>freia o alarme via conexão humana</strong>. Sentir-se visto e ouvido por alguém seguro desliga o perigo.",
    "tip": "<strong>Para refletir:</strong> isolar a pessoa traumatizada agrava — a base da calma é o vínculo seguro."
   },
   {
    "ic": "lens",
    "t": "Neurocepção",
    "b": "A avaliação <strong>automática e inconsciente</strong> de segurança/perigo no ambiente, antes da consciência. No trauma, ela lê perigo onde há segurança — daí a hipervigilância crônica.",
    "tip": "<strong>Como aplicar:</strong> a baixa VFC (variabilidade cardíaca) acompanha o trauma; é alvo de yoga e respiração."
   }
  ]
 },
 "ch06-perdendo-o-corpo": {
  "cards": [
   {
    "ic": "target",
    "t": "Interocepção",
    "b": "A percepção das sensações internas (batimento, respiração, vísceras) é a <strong>base do senso de si</strong> — sentimos quem somos a partir do que o corpo sente. Embotada, vem o vazio.",
    "tip": "<strong>Modelo mental:</strong> a interocepção é a bússola interna; sem ela, navega-se a vida sem saber para onde aponta."
   },
   {
    "ic": "mask",
    "t": "Alexitimia",
    "b": "A incapacidade de <strong>identificar e nomear as próprias emoções</strong> — 'sem palavras para os sentimentos'. O corpo reage, mas a pessoa não sabe a quê. Junto vem a despersonalização: ver-se de fora.",
    "tip": "<strong>Para refletir:</strong> não force 'sentir os sentimentos' sem segurança — sensações internas podem ser aterrorizantes."
   },
   {
    "ic": "scale",
    "t": "O Preço do Entorpecimento",
    "b": "Desligar-se da dor para sobreviver <strong>apaga também o prazer e a vitalidade</strong>. Sem habitar o corpo, perde-se a agência — a sensação de estar no comando da própria vida.",
    "tip": "<strong>Como aplicar:</strong> reabitar o corpo com segurança é pré-requisito da agência — e da cura."
   }
  ]
 },
 "ch07-apego-e-sintonia": {
  "cards": [
   {
    "ic": "person",
    "t": "Apego e Sintonia",
    "b": "O vínculo precoce com um cuidador responsivo é onde se aprende a regular emoções. A regulação começa <strong>de fora (co-regulação)</strong> e só depois vira interna — não há autorregulação sem ter sido primeiro regulado.",
    "tip": "<strong>Modelo mental:</strong> o cuidador é o primeiro termostato emocional, até a criança aprender a regular sozinha."
   },
   {
    "ic": "triangle",
    "t": "Apego Desorganizado",
    "b": "O padrão mais ligado ao trauma: o cuidador é, ao mesmo tempo, <strong>porto seguro e fonte de terror</strong>. 'Medo sem solução' — não dá para fugir nem buscar conforto na mesma pessoa.",
    "tip": "<strong>Para refletir:</strong> é um alarme sem saída — a corrida pela proteção leva à própria fonte do medo."
   },
   {
    "ic": "layers",
    "t": "Trauma do Desenvolvimento",
    "b": "O efeito cumulativo de abuso/negligência crônicos na infância afeta <strong>regulação, atenção, autoimagem e relações</strong> — de forma mais ampla que o TEPT clássico.",
    "tip": "<strong>Como aplicar:</strong> não leia comportamentos de trauma do desenvolvimento como 'birra' ou má conduta — são marcas de uma fiação afetiva ferida."
   }
  ]
 },
 "ch11-memoria-traumatica": {
  "cards": [
   {
    "ic": "book",
    "t": "Traumática × Narrativa",
    "b": "A memória <strong>narrativa</strong> é contável, em palavras, situada no tempo. A <strong>traumática</strong> é fragmento sensorial sem palavras e sem data — invade como flashback, no presente.",
    "tip": "<strong>Modelo mental:</strong> a memória comum é um livro na estante; a traumática é um alarme que toca sozinho."
   },
   {
    "ic": "steps",
    "t": "Integrar",
    "b": "A meta terapêutica é <strong>dar palavras, contexto e ordem temporal</strong> ao fragmento, para que o trauma vire passado — 'uma história entre outras', e não um presente eterno.",
    "tip": "<strong>Para refletir:</strong> reviver a memória bruta sem regulação retraumatiza, em vez de integrar."
   },
   {
    "ic": "lens",
    "t": "Vívido ≠ Exato",
    "b": "A memória é <strong>reconstrutiva e sugestionável</strong>. O caráter vívido do trauma não garante exatidão literal — daí a cautela com memórias 'recuperadas' ou implantadas.",
    "tip": "<strong>Como aplicar:</strong> respeite o vívido da experiência sem tratá-la como relato literal e infalível."
   }
  ]
 },
 "ch13-curar-janela-de-tolerancia": {
  "cards": [
   {
    "ic": "gap",
    "t": "Janela de Tolerância",
    "b": "A zona ótima em que o cérebro racional e o emocional cooperam. <strong>Acima</strong> = hiperexcitação (pânico, fúria). <strong>Abaixo</strong> = hipoexcitação (entorpecimento, dissociação). A cura <strong>alarga a janela</strong>.",
    "tip": "<strong>Regra:</strong> fora da janela, o racional está offline — primeiro regular, só depois processar."
   },
   {
    "ic": "wave",
    "t": "Top-down + Bottom-up",
    "b": "Regular pela <strong>mente</strong> (observar, nomear, mindfulness) E pelo <strong>corpo</strong> (respiração, ritmo, movimento, toque). Nenhum sozinho basta; a cura robusta casa os dois.",
    "tip": "<strong>Como aplicar:</strong> a expiração lenta é um freio parassimpático imediato para voltar à janela."
   },
   {
    "ic": "steps",
    "t": "Pendulação",
    "b": "Tocar a ativação difícil <strong>em doses pequenas</strong> e voltar à segurança — sem inundar (flooding) o sistema. Aproximar-se do trauma por dosagem, com ancoragem no presente.",
    "tip": "<strong>Para refletir:</strong> cura é dosagem, não enxurrada — inundar retraumatiza."
   }
  ]
 },
 "ch14-linguagem": {
  "cards": [
   {
    "ic": "bubble",
    "t": "A Palavra que Cura",
    "b": "Nomear sentimentos e contar a história <strong>integra a experiência</strong>, dá controle e reconecta aos outros. A escrita expressiva (Pennebaker) melhora saúde física e mental.",
    "tip": "<strong>Modelo mental:</strong> a linguagem é a ponte de volta ao mundo — dar nome ao caos interno permite atravessá-lo."
   },
   {
    "ic": "mask",
    "t": "A Tirania da Palavra",
    "b": "Confiar só na fala falha: no auge do flashback a <strong>área de Broca desliga</strong> (terror sem palavras), e racionalizar pode encobrir em vez de curar. A terapia só-verbal pode estagnar.",
    "tip": "<strong>Para refletir:</strong> onde o corpo grita sem voz, primeiro regular o corpo, depois nomear."
   },
   {
    "ic": "target",
    "t": "Sentir Antes de Nomear",
    "b": "A autoconsciência começa na <strong>percepção das sensações</strong>; a palavra ancora-se nelas. Conhecer-se exige sentir o corpo — não apenas raciocinar sobre ele.",
    "tip": "<strong>Como aplicar:</strong> a cura plena casa palavra e corpo — autoconsciência nasce de sentir, depois nomear."
   }
  ]
 },
 "ch15-emdr": {
  "cards": [
   {
    "ic": "wave",
    "t": "EMDR",
    "b": "Dessensibilização e Reprocessamento por Movimentos Oculares: mantendo em mente a imagem do trauma, o terapeuta guia <strong>movimentos oculares (estimulação bilateral)</strong>. A perturbação cai e a memória se reorganiza.",
    "tip": "<strong>Como aplicar:</strong> alvo (imagem + crença negativa + sensação) → estimulação em séries → associação livre → crença positiva → checar o corpo."
   },
   {
    "ic": "steps",
    "t": "Sem Reviver Tudo",
    "b": "O paciente <strong>não precisa contar nem reviver inteiro</strong> — a integração ocorre internamente. Útil inclusive quando a via verbal trava.",
    "tip": "<strong>Para refletir:</strong> exigir o relato verbal completo pode ser contraproducente; o cérebro faz o trabalho associativo."
   },
   {
    "ic": "pivot",
    "t": "O Trauma Vira Passado",
    "b": "A carga emocional/corporal ligada à memória cai (dessensibilização) e a <strong>crença negativa</strong> ('é minha culpa') dá lugar à adaptativa ('eu sobrevivi'). O fragmento 'preso' volta a ser arquivado como passado.",
    "tip": "<strong>Modelo mental:</strong> é como digerir um alimento empacado — a memória presa volta a ser processada."
   }
  ]
 },
 "ch16-yoga": {
  "cards": [
   {
    "ic": "leaf",
    "t": "Reabitar o Corpo",
    "b": "Posturas + respiração + atenção às sensações treinam a pessoa a <strong>sentir o corpo sem pânico</strong> — o oposto do entorpecimento. Aprende-se que as sensações têm começo, meio e fim.",
    "tip": "<strong>Modelo mental:</strong> o yoga é a academia da interocepção — treina o músculo de sentir o corpo sem fugir dele."
   },
   {
    "ic": "wave",
    "t": "Respiração como Freio",
    "b": "A <strong>expiração lenta ativa o parassimpático</strong> (freio) e baixa a excitação — ferramenta bottom-up imediata para voltar à janela de tolerância.",
    "tip": "<strong>Como aplicar:</strong> use a expiração lenta como freio de mão do sistema nervoso — alavanca sempre disponível."
   },
   {
    "ic": "target",
    "t": "Corpo Mais Resiliente",
    "b": "O yoga e a respiração melhoram a <strong>variabilidade da frequência cardíaca (VFC)</strong> — marcador de autorregulação. Não é exercício físico: é reaprender a habitar e regular o corpo.",
    "tip": "<strong>Para refletir:</strong> respeite a janela de tolerância — uma postura pode disparar gatilhos; o objetivo é tolerar aos poucos."
   }
  ]
 },
 "ch17-ifs": {
  "cards": [
   {
    "ic": "person",
    "t": "A Família Interna (IFS)",
    "b": "A psique como um sistema de partes: <strong>exilados</strong> (feridos, carregam a dor), <strong>gerentes</strong> (controlam para a dor não vazar) e <strong>bombeiros</strong> (apagam a dor às pressas: impulsos, vícios). Nenhuma é má — todas protegem.",
    "tip": "<strong>Modelo mental:</strong> a mente é uma família interna; o Self é quem reconcilia, não quem combate."
   },
   {
    "ic": "target",
    "t": "O Self Nuclear",
    "b": "A sede de consciência <strong>calma, curiosa, compassiva e confiante</strong> — não é uma parte e o trauma não a destrói. Liderar a partir do Self (autoliderança) é a meta.",
    "tip": "<strong>Como aplicar:</strong> separar-se da parte ('tenho uma parte que…', não 'eu sou') já devolve o comando ao Self."
   },
   {
    "ic": "key",
    "t": "Descarregar o Fardo",
    "b": "Curar é o Self acolher cada parte, entender seu <strong>papel protetor</strong> e libertá-la do fardo (a crença/dor extrema que carrega desde o trauma).",
    "tip": "<strong>Para refletir:</strong> não combata as partes 'ruins' — o crítico e o bombeiro protegem um exilado ferido."
   }
  ]
 },
 "ch19-neurofeedback-teatro": {
  "cards": [
   {
    "ic": "constellation",
    "t": "Neurofeedback",
    "b": "Treinar o cérebro a alterar seus próprios padrões de ondas: sensores leem a atividade elétrica e <strong>recompensam ritmos mais regulados</strong>. Com a repetição, o cérebro reaprende a se estabilizar.",
    "tip": "<strong>Modelo mental:</strong> é fisioterapia para os ritmos do cérebro — treino dirigido recupera a função."
   },
   {
    "ic": "spark",
    "t": "Neuroplasticidade",
    "b": "A capacidade do cérebro de <strong>reorganizar circuitos com a experiência repetida</strong> é a base de toda recuperação. As estruturas (terapias psicomotoras) criam a experiência corretiva que faltou — no corpo.",
    "tip": "<strong>Para refletir:</strong> o cérebro traumatizado não é imutável — circuitos se refazem com prática dirigida."
   },
   {
    "ic": "bubble",
    "t": "Voz, Ritmo e Teatro",
    "b": "A sincronia coletiva (cantar, tocar, atuar, dançar juntos) <strong>regula o sistema nervoso, restaura o engajamento social</strong> e devolve agência e pertencimento. Encarnar um papel permite experimentar emoções novas em segurança.",
    "tip": "<strong>Como aplicar:</strong> a cura não se completa só no consultório isolado — o grupo e o ritmo são parte do remédio."
   }
  ]
 }
}
```
