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

# LIVRO PARA APROFUNDAR: O Poder do Hábito — Charles Duhigg

**Subtítulo:** VISÃO GERAL · POR QUE FAZEMOS O QUE FAZEMOS
**Ideia central:** Quase metade do que fazemos todo dia não é decisão: é hábito. Duhigg revela o circuito neurológico por trás disso — o loop deixa → rotina → recompensa, movido pelo desejo — e mostra a Regra de Ouro para reescrevê-lo. A mesma mecânica explica a pessoa que perde peso, a empresa que ressurge e o movimento que muda a sociedade.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-o-loop-do-habito` — CAPÍTULO 1: O Loop do Hábito — Como os Hábitos Funcionam
- `ch02-o-cerebro-ansioso` — CAPÍTULO 2: O Cérebro Ansioso — Como Criar Novos Hábitos
- `ch03-a-regra-de-ouro` — CAPÍTULO 3: A Regra de Ouro da Mudança de Hábitos
- `ch04-habitos-angulares` — CAPÍTULO 4: Hábitos Angulares — Quais Hábitos Importam Mais
- `ch05-forca-de-vontade` — CAPÍTULO 5: Força de Vontade — O Hábito Angular Mais Importante
- `ch06-habitos-das-organizacoes` — CAPÍTULO 6: O Poder de uma Crise — Hábitos das Organizações
- `ch07-habitos-do-consumidor` — CAPÍTULO 7: Como o Varejo Sabe o que Você Quer
- `ch08-habitos-da-sociedade` — CAPÍTULO 8: Como Nascem os Movimentos — Hábitos da Sociedade
- `ch09-neurologia-do-livre-arbitrio` — CAPÍTULO 9: A Neurologia do Livre-Arbítrio

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-o-loop-do-habito": {
  "cards": [
   {
    "ic": "pivot",
    "t": "Deixa → Rotina → Recompensa",
    "b": "A unidade básica de todo comportamento automático. A <strong>deixa</strong> diz ao cérebro entrar em modo automático; a <strong>rotina</strong> é o comportamento; a <strong>recompensa</strong> é o que faz o cérebro lembrar de repetir.",
    "tip": "<strong>Como aplicar:</strong> mapeie as 3 peças de qualquer hábito antes de mexer nele."
   },
   {
    "ic": "target",
    "t": "As 5 Categorias de Deixa",
    "b": "Quase toda deixa cai em cinco tipos: <strong>local, hora, estado emocional, outras pessoas, ação imediatamente anterior</strong>. Achar a deixa é o primeiro ato de qualquer mudança.",
    "tip": "<strong>Como aplicar:</strong> no momento do impulso, anote as 5 dimensões — o padrão aparece em poucos dias."
   },
   {
    "ic": "spiral",
    "t": "Chunking (segmentação)",
    "b": "O cérebro converte sequências de ações numa <strong>rotina automática única</strong>, gravada nos gânglios da base. É o que permite agir sem pensar — e por isso o hábito não se apaga, só fica latente.",
    "tip": "<strong>Modelo mental:</strong> hábito é atalho de energia; some da consciência, não do cérebro."
   }
  ]
 },
 "ch02-o-cerebro-ansioso": {
  "cards": [
   {
    "ic": "spark",
    "t": "O Craving (desejo)",
    "b": "A peça oculta que energiza o loop. Com a repetição, a deixa passa a disparar a <strong>antecipação</strong> da recompensa — e é essa ânsia que torna o hábito irresistível.",
    "tip": "<strong>Modelo mental:</strong> deixa e recompensa são o circuito; o craving é a corrente que o mantém ligado."
   },
   {
    "ic": "bulb",
    "t": "Receita do Hábito Novo",
    "b": "Um hábito só 'gruda' quando há craving. Deixa simples + recompensa que o cérebro aprenda a desejar. <strong>Pepsodent</strong> criou o frescor mentolado; <strong>Febreze</strong> só pegou ao virar 'prêmio' perfumado da faxina.",
    "tip": "<strong>Pergunta-chave:</strong> qual recompensa o cérebro vai aprender a desejar aqui?"
   },
   {
    "ic": "eye",
    "t": "A Deixa Que Fisga",
    "b": "O craving torna o hábito vulnerável a deixas externas — cheiro de donut, som de notificação. O pico de dopamina <strong>migra para a deixa</strong>: o cérebro saboreia o prêmio antes de recebê-lo.",
    "tip": "<strong>Para refletir:</strong> as telas e os apps exploram exatamente esse craving antecipado."
   }
  ]
 },
 "ch03-a-regra-de-ouro": {
  "cards": [
   {
    "ic": "pivot",
    "t": "Trocar a Rotina",
    "b": "A rotina é a <strong>única peça que se pode trocar</strong>. Mantém-se deixa e recompensa; muda-se só o miolo. É cirurgia no loop, não demolição.",
    "tip": "<strong>Passos:</strong> identifique a rotina → experimente recompensas → isole a deixa → tenha um plano."
   },
   {
    "ic": "lens",
    "t": "Diagnosticar a Recompensa",
    "b": "Quase nunca é o objeto óbvio. Teste recompensas (comer / caminhar / conversar) e veja qual <strong>dissipa a ânsia</strong> — ela revela o desejo real. O cookie da tarde podia ser socialização, não fome.",
    "tip": "<strong>Como aplicar:</strong> ao sentir o impulso, varie a recompensa e espere 15 min."
   },
   {
    "ic": "constellation",
    "t": "Crença e Comunidade",
    "b": "Para a mudança resistir ao <strong>estresse</strong>, é preciso acreditar que ela é possível — e a crença costuma nascer e se sustentar num grupo (como o AA). Sem crença, a velha rotina ressurge.",
    "tip": "<strong>Para aplicar:</strong> ancore mudanças difíceis numa comunidade que torne crível o 'eu consigo'."
   }
  ]
 },
 "ch04-habitos-angulares": {
  "cards": [
   {
    "ic": "layers",
    "t": "Hábito Angular",
    "b": "Hábito que, ao mudar, <strong>transborda</strong> e transforma áreas não relacionadas. Mude o angular e o resto se reordena. Pergunta-chave: 'o que, se eu mudar, muda tudo o mais?'",
    "tip": "<strong>Modelo mental:</strong> não empurre as 100 peças do dominó — empurre a certa."
   },
   {
    "ic": "steps",
    "t": "Pequenas Vitórias",
    "b": "Vitórias modestas e consistentes que constroem <strong>impulso e crença</strong> de que mudanças maiores são possíveis. São o motor que faz o angular escalar.",
    "tip": "<strong>Como aplicar:</strong> projete a mudança para gerar vitórias visíveis cedo."
   },
   {
    "ic": "mountain",
    "t": "O Caso Alcoa",
    "b": "Paul O'Neill elegeu a <strong>segurança do trabalhador</strong> como prioridade nº 1 — o hábito angular. Zerar acidentes forçou comunicação, processos e qualidade a se reorganizarem. Resultado: lucro líquido <strong>quintuplicou</strong>.",
    "tip": "<strong>Para aplicar:</strong> em organizações, um angular bem escolhido reorganiza a operação inteira."
   }
  ]
 },
 "ch05-forca-de-vontade": {
  "cards": [
   {
    "ic": "scale",
    "t": "Vontade é Músculo",
    "b": "Recurso <strong>finito</strong> que se esgota ao longo do dia (esgotamento do ego) e <strong>cresce</strong> com exercício regular. Treiná-la numa área (exercício, finanças) transborda para todas.",
    "tip": "<strong>Modelo mental:</strong> trate como bateria — recarrega com sono/comida/descanso, ganha capacidade com treino."
   },
   {
    "ic": "key",
    "t": "Autonomia Poupa Vontade",
    "b": "Quando a pessoa sente que <strong>escolheu</strong> (não foi mandada), o músculo cansa mais devagar. Impor mudança sem senso de escolha acelera o esgotamento.",
    "tip": "<strong>Para aplicar:</strong> dê autonomia a quem você quer que mude — não ordens."
   },
   {
    "ic": "steps",
    "t": "Planejar o Ponto de Crise (LATTE)",
    "b": "Não confie na vontade na hora difícil — <strong>planeje a reação antes</strong>. A Starbucks treina o roteiro LATTE (Listen, Acknowledge, Take action, Thank, Explain): vontade vira rotina automática.",
    "tip": "<strong>Como aplicar:</strong> escreva de antemão como vai reagir ao ponto de dor."
   }
  ]
 },
 "ch06-habitos-das-organizacoes": {
  "cards": [
   {
    "ic": "link",
    "t": "Rotinas e a Trégua",
    "b": "As empresas operam por hábitos coletivos que distribuem poder e mantêm a <strong>paz interna</strong>. Quando a trégua fica desequilibrada, instalam-se hábitos perigosos — e a 'paz' esconde o risco.",
    "tip": "<strong>Modelo mental:</strong> não procure o vilão; procure a rotina por trás da falha."
   },
   {
    "ic": "spark",
    "t": "A Crise como Oportunidade",
    "b": "Na crise, as rotinas se afrouxam e <strong>podem ser reescritas</strong>. Bons líderes mantêm deliberadamente a sensação de crise para forçar a substituição de hábitos entranhados.",
    "tip": "<strong>Regra:</strong> não desperdice uma boa crise — a janela fecha rápido."
   },
   {
    "ic": "wrench",
    "t": "Hospital de Rhode Island",
    "b": "Hábitos davam poder excessivo aos cirurgiões e silenciavam enfermeiras — uma trégua doente que gerou erros graves. Só após a crise vieram <strong>checklists e autoridade redistribuída</strong>.",
    "tip": "<strong>Para aplicar:</strong> instale hábitos angulares (protocolos) enquanto a crise ainda abre a janela."
   }
  ]
 },
 "ch07-habitos-do-consumidor": {
  "cards": [
   {
    "ic": "mask",
    "t": "A Trama da Familiaridade",
    "b": "O cérebro evita o desconhecido. Para um hábito novo pegar, <strong>esconda-o entre estímulos familiares</strong> — a música nova entre dois sucessos, o produto novo embrulhado no conhecido.",
    "tip": "<strong>Como aplicar:</strong> calibre a dose — ser óbvio demais assusta; familiar demais não inova."
   },
   {
    "ic": "lens",
    "t": "Predição por Dados",
    "b": "Padrões de compra revelam quando hábitos estão <strong>destravados</strong>. A Target detectava gestantes pelos itens comprados — e teve de camuflar os cupons de bebê entre ofertas aleatórias para não assustar.",
    "tip": "<strong>Para refletir:</strong> a precisão preditiva levanta a questão ética da manipulação."
   },
   {
    "ic": "pin",
    "t": "Janelas de Mudança de Vida",
    "b": "Grandes eventos — filho, casamento, mudança — <strong>afrouxam todos os hábitos</strong> e tornam o consumidor maleável. O varejo mira nesses momentos raros de abertura.",
    "tip": "<strong>Modelo mental:</strong> eventos de vida = hábitos destravados = janela de mudança."
   }
  ]
 },
 "ch08-habitos-da-sociedade": {
  "cards": [
   {
    "ic": "person",
    "t": "Laços Fortes Acendem",
    "b": "O movimento começa pelos <strong>hábitos de amizade</strong> e laços íntimos. Rosa Parks era respeitada e conectada a muitos círculos — por isso sua prisão mobilizou de imediato.",
    "tip": "<strong>Modelo mental:</strong> a amizade é a faísca, mas sozinha não escala."
   },
   {
    "ic": "constellation",
    "t": "Laços Fracos Espalham",
    "b": "A causa cresce pela <strong>pressão de pares</strong> da comunidade — os conhecidos distantes. O custo de não aderir (perder reputação) converte simpatia passiva em ação.",
    "tip": "<strong>Para aplicar:</strong> a rede ampla de conhecidos é o que propaga o movimento."
   },
   {
    "ic": "leaf",
    "t": "Novos Hábitos Fazem Durar",
    "b": "Para perdurar, os líderes dão aos participantes <strong>hábitos novos</strong> que criam identidade e propósito próprios — o movimento ganha vida sem depender de um único líder.",
    "tip": "<strong>Regra:</strong> depender só do carisma do líder faz o movimento morrer quando ele sai."
   }
  ]
 },
 "ch09-neurologia-do-livre-arbitrio": {
  "cards": [
   {
    "ic": "key",
    "t": "Responsabilidade pós-Consciência",
    "b": "Conhecer o loop <strong>devolve a liberdade</strong> — e com ela o dever de agir. Não saber pode desculpar; saber, não. Acender a luz no quarto escuro torna o tropeço uma escolha sua.",
    "tip": "<strong>Para refletir:</strong> 'é só um hábito' deixa de ser álibi depois que você o conhece."
   },
   {
    "ic": "target",
    "t": "O Quase-Acerto (near miss)",
    "b": "O cérebro do jogador patológico registra a <strong>quase-vitória como vitória</strong>, alimentando o loop até perder tudo. Cuidado com 'quases' que reforçam o hábito errado.",
    "tip": "<strong>Modelo mental:</strong> em metas e jogos, o near miss engana — não o trate como progresso."
   },
   {
    "ic": "steps",
    "t": "Mudar em 4 Passos (o Apêndice)",
    "b": "A receita que aplica o livro inteiro: <strong>(1) identifique a rotina, (2) experimente recompensas, (3) isole a deixa, (4) tenha um plano</strong>. Hábito não é destino: visto, pode ser reescrito.",
    "tip": "<strong>Como aplicar:</strong> use os 4 passos como checklist sempre que for mudar um hábito."
   }
  ]
 }
}
```
