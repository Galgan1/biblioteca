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

# LIVRO PARA APROFUNDAR: Trabalhe 4 Horas por Semana — Tim Ferriss

**Subtítulo:** VISÃO GERAL · O ESTILO DE VIDA DOS NOVOS RICOS
**Ideia central:** A meta não é ter mais dinheiro — é ter mais vida. Os Novos Ricos (NR) abandonam a hipótese adiada ('trabalhe 40 anos e descanse no fim') e tornam a moeda real o tempo e a mobilidade, agora. O caminho é o processo DEAL: Definição, Eliminação, Automação e Libertação — fazer menos do que não importa para viver o que importa.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-novos-ricos-eficacia` — CAPÍTULO 1: Os Novos Ricos & a Nova Moeda
- `ch02-definicao-regras-do-jogo` — CAPÍTULO 2: Definição — Inverter as Regras do Jogo
- `ch03-definicao-medo-dreamlining` — CAPÍTULO 3: Definição — Fear-setting & Dreamlining
- `ch04-eliminacao-pareto-parkinson` — CAPÍTULO 4: Eliminação — Pareto, Parkinson & a Dieta de Baixa Informação
- `ch05-automacao-musa-terceirizacao` — CAPÍTULO 5: Automação — A Musa & Terceirização
- `ch06-libertacao-remoto-mini-aposentadorias` — CAPÍTULO 6: Libertação — Trabalho Remoto & Mini-aposentadorias
- `ch07-preencher-o-vacuo` — CAPÍTULO 7: Preencher o Vácuo & Erros Finais

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-novos-ricos-eficacia": {
  "cards": [
   {
    "ic": "target",
    "t": "Os Novos Ricos (NR)",
    "b": "Quem abandona o adiamento da vida e usa <strong>tempo + mobilidade</strong> no presente, com renda automatizada modesta porém suficiente. A bússola de toda decisão: 'isto me dá mais tempo e mobilidade?'.",
    "tip": "<strong>Como aplicar:</strong> defina o estilo de vida, calcule o custo e desenhe a renda mínima que o sustente no piloto automático."
   },
   {
    "ic": "wave",
    "t": "As variáveis O-Q-Q",
    "b": "O poder não vem só de quanto você ganha, mas de <strong>O</strong> que faz, <strong>Q</strong>uando faz e onde/com <strong>Q</strong>uem. Liberdade nessas três multiplica o valor de cada real ganho.",
    "tip": "<strong>Modelo mental:</strong> pense em tempo e mobilidade como a moeda real — dinheiro só vale pelo que liberta."
   },
   {
    "ic": "scale",
    "t": "Renda Relativa × Absoluta",
    "b": "Meça o ganho por <strong>hora de vida gasta</strong>, não pelo total. R$ 200/hora trabalhando 10h/semana <strong>derrota</strong> R$ 50/hora trabalhando 80h. Renda alta com vida sequestrada não é riqueza.",
    "tip": "<strong>Para refletir:</strong> ao comparar empregos/projetos, divida sempre o ganho pelas horas e pela liberdade que custa."
   },
   {
    "ic": "eye",
    "t": "Eficácia antes de Eficiência",
    "b": "<strong>Eficácia</strong> = fazer o certo; <strong>eficiência</strong> = fazer econômico. 'Fazer bem o que não devia ser feito' é a armadilha do trabalhador ocupado. Movimento não é resultado.",
    "tip": "<strong>Regra:</strong> antes de otimizar uma tarefa, pergunte se ela deveria existir."
   }
  ]
 },
 "ch02-definicao-regras-do-jogo": {
  "cards": [
   {
    "ic": "pivot",
    "t": "A Hipótese Adiada",
    "b": "O roteiro tradicional: trabalhar duro 40 anos e <strong>descansar só na aposentadoria</strong>. Aposta as melhores décadas num descanso futuro e incerto. O NR distribui a 'aposentadoria' ao longo da vida.",
    "tip": "<strong>Para refletir:</strong> adiar a vida para 'um dia' é o plano-padrão — e o mais arriscado de todos."
   },
   {
    "ic": "sword",
    "t": "O 'Realismo' é a Cilada",
    "b": "As metas 'realistas' atraem multidão e por isso são <strong>mais competidas</strong> do que as ousadas. O irreal costuma ser mais fácil: menos gente tenta. Mire alto para enfrentar menos concorrência.",
    "tip": "<strong>Modelo mental:</strong> 'fazer o que a maioria evita' é vantagem competitiva, não imprudência."
   },
   {
    "ic": "spark",
    "t": "Tédio × Felicidade",
    "b": "O oposto de feliz não é triste — é o <strong>tédio</strong>. O que dá energia é a empolgação (excitement). Por isso lazer ilimitado satura: falta o que empolga e desafia.",
    "tip": "<strong>Para refletir:</strong> troque 'o que me faria feliz?' por 'o que me empolga?' — a segunda gera ação."
   }
  ]
 },
 "ch03-definicao-medo-dreamlining": {
  "cards": [
   {
    "ic": "gap",
    "t": "Fear-setting (Definição do Medo)",
    "b": "Substitui 'definir metas' por 'definir medos'. Três colunas: (1) <strong>defina</strong> o pior cenário; (2) como <strong>prevenir</strong>; (3) como <strong>reparar</strong> se acontecer. Depois pese o custo da inação.",
    "tip": "<strong>Como aplicar:</strong> use sempre que o medo paralisar uma decisão — escrever o pior cenário o encolhe."
   },
   {
    "ic": "clock",
    "t": "O Custo da Inação",
    "b": "O preço (financeiro, emocional, físico) de <strong>não</strong> agir — em 6 meses, 1 ano, 3 anos. Quase sempre maior que o do pior cenário, que costuma ser reversível. O perigo real é a paralisia, não o risco.",
    "tip": "<strong>Para refletir:</strong> o pior caso quase sempre se conserta; o arrependimento da inação, não."
   },
   {
    "ic": "constellation",
    "t": "Dreamlining",
    "b": "Transforma 'quero ser feliz/rico' em planos datados e precificados. Liste o que quer <strong>Ter, Ser e Fazer</strong> em 6 e 12 meses ('ser X' vira 'fazer Y'), e precifique cada sonho como custo mensal.",
    "tip": "<strong>Como aplicar:</strong> defina 3 passos por sonho e dê o primeiro nos próximos 5 minutos."
   },
   {
    "ic": "key",
    "t": "Renda-Alvo (TMM / TDI)",
    "b": "Some os custos dos sonhos → <strong>Renda-Alvo Mensal (TMM)</strong>; divida pelos dias → <strong>Diária (TDI)</strong>. A surpresa recorrente: o 'sonho de milionário' exige renda modesta, não fortuna.",
    "tip": "<strong>Modelo mental:</strong> pense no sonho como uma fatura mensal — tudo vira número, e o número costuma ser pequeno."
   }
  ]
 },
 "ch04-eliminacao-pareto-parkinson": {
  "cards": [
   {
    "ic": "lens",
    "t": "Lei de Pareto (80/20)",
    "b": "~80% dos resultados vêm de ~20% das causas (e dos problemas). Amplie os <strong>20% que geram 80% do resultado</strong> e corte/demita os <strong>20% que geram 80% dos problemas</strong>.",
    "tip": "<strong>Pergunta:</strong> 'se eu só pudesse manter 20% disto, qual 20% manteria?'."
   },
   {
    "ic": "clock",
    "t": "Lei de Parkinson",
    "b": "O trabalho se expande para preencher o tempo disponível. <strong>Encurte o prazo</strong> drasticamente — um prazo apertado força só o essencial e mata o perfeccionismo e a distração.",
    "tip": "<strong>Como aplicar:</strong> em qualquer tarefa que 'se arrasta', defina um prazo curto, quase desconfortável."
   },
   {
    "ic": "eye",
    "t": "Dieta de Baixa Informação",
    "b": "Jejum seletivo e deliberado de notícias, e-mail, reuniões e mídia irrelevante. Pratique a <strong>ignorância seletiva</strong>: informação sob demanda ('just-in-time'), não acúmulo ('just-in-case').",
    "tip": "<strong>Filtro:</strong> 'isto muda alguma decisão minha?' Se não, ignore."
   },
   {
    "ic": "steps",
    "t": "A Combinação Mágica",
    "b": "Faça <strong>só o que importa</strong> (Pareto) <strong>em prazos curtos</strong> (Parkinson) — uma sem a outra falha. Mantenha uma <strong>lista de não-fazer</strong>; estar atarefado costuma ser preguiça disfarçada.",
    "tip": "<strong>Modelo mental:</strong> ocupação ≠ produtividade; muita gente se ocupa para evitar as poucas tarefas que assustam."
   }
  ]
 },
 "ch05-automacao-musa-terceirizacao": {
  "cards": [
   {
    "ic": "wrench",
    "t": "A Musa",
    "b": "Negócio simples desenhado para <strong>renda automatizada</strong>, não para realização pessoal: produto de margem alta, demanda comprovada e operação delegável. Existe para cobrir a TMM, não para maximizar lucro.",
    "tip": "<strong>Como aplicar:</strong> escolha um nicho que você entenda, crie/licencie um produto e prepare a operação para terceiros."
   },
   {
    "ic": "target",
    "t": "Microteste a Demanda",
    "b": "Antes de fabricar ou estocar, monte <strong>anúncio + página de venda</strong> e meça cliques/pedidos. Demanda confirmada → produz. Sem cliques → não há produto. Barato, rápido e à prova de prejuízo.",
    "tip": "<strong>Anti-padrão:</strong> construir o produto antes de testar a demanda = estoque parado e prejuízo."
   },
   {
    "ic": "person",
    "t": "Terceirização & AVs",
    "b": "Delegue tarefas (pessoais e do negócio) a fornecedores e <strong>assistentes virtuais</strong>. Comece por tarefas pequenas e bem definidas, teste a comunicação e meça por resultado antes de confiar o grande.",
    "tip": "<strong>Modelo mental:</strong> pense na musa como uma máquina, não um filho — ela gera caixa enquanto você vive."
   },
   {
    "ic": "fork",
    "t": "A Regra de Não-Decidir",
    "b": "O gargalo da automação é <strong>você</strong> no centro de cada decisão. Dê <strong>autonomia por valor</strong> à equipe ('resolva sozinho até R$ X') e pare de aprovar minúcias. Troque 'me pergunte' por 'decida e me informe'.",
    "tip": "<strong>Regra:</strong> a meta não é gerenciar melhor — é não precisar gerenciar."
   }
  ]
 },
 "ch06-libertacao-remoto-mini-aposentadorias": {
  "cards": [
   {
    "ic": "pin",
    "t": "A Fuga do Escritório",
    "b": "Roteiro para se libertar do local fixo sendo empregado: (1) torne-se valioso; (2) prove produtividade num <strong>teste curto e reversível</strong> e documente o ganho; (3) aumente os dias fora; (4) torne o retorno indesejável ao chefe.",
    "tip": "<strong>Regra:</strong> peça perdão, não permissão — e escale aos poucos, nunca tudo de uma vez."
   },
   {
    "ic": "leaf",
    "t": "Mini-aposentadorias",
    "b": "Intercalar períodos de 1–6 meses de 'vida' (viagem, projetos, descanso) <strong>ao longo da carreira</strong>, em vez de uma aposentadoria única no fim. É a resposta concreta à hipótese adiada.",
    "tip": "<strong>Diferença:</strong> férias = escapismo curto; mini-aposentadoria = realocação temporária com ritmo de vida local."
   },
   {
    "ic": "mountain",
    "t": "Eliminar antes de Libertar",
    "b": "Para empregados, a ordem é <strong>D-E-L-A</strong>: corte o trabalho inútil <strong>antes</strong> de pedir remoto. Sem eliminar primeiro, a liberdade vira a mesma prisão em outro lugar — você só leva o caos para casa.",
    "tip": "<strong>Modelo mental:</strong> pense na vida como blocos intercalados de trabalho e exploração, não como longa espera pelo descanso."
   }
  ]
 },
 "ch07-preencher-o-vacuo": {
  "cards": [
   {
    "ic": "gap",
    "t": "O Vácuo Pós-Libertação",
    "b": "O vazio que aparece quando o trabalho deixa de organizar a vida: tédio, crise existencial, 'e agora?'. <strong>Não é fracasso do plano</strong> — é etapa esperada da transição. Reconheça-o antes de libertar tempo.",
    "tip": "<strong>Para refletir:</strong> lazer ilimitado satura rápido; tempo livre é espaço a habitar, não prêmio passivo."
   },
   {
    "ic": "bulb",
    "t": "As Perguntas que Dão Sentido",
    "b": "Troque 'qual o sentido da vida?' (insolúvel) por perguntas acionáveis: <strong>'o que me empolga / dá vida?'</strong> e <strong>'como posso servir/contribuir?'</strong>. Empolgação é bússola melhor que 'felicidade'.",
    "tip": "<strong>Como aplicar:</strong> quando travar em 'não sei o que quero', pergunte 'o que me empolga?' — gera ação."
   },
   {
    "ic": "leaf",
    "t": "Aprender & Servir",
    "b": "As duas atividades que sustentam o NR depois que o dinheiro deixou de ser o jogo: <strong>aprendizado contínuo</strong> (mantém o crescimento) e <strong>serviço/contribuição</strong> (gera significado). O foco sai do 'eu'.",
    "tip": "<strong>Modelo mental:</strong> redirecione para aprender e servir a energia que antes ia para ganhar dinheiro."
   },
   {
    "ic": "sword",
    "t": "Os Erros dos NR",
    "b": "Os recaídas mais comuns: perder a noção dos sonhos e <strong>virar workaholic de novo</strong>; subautomatizar (microgerenciar de longe); e supersaturar (encher a agenda livre com tarefas inúteis).",
    "tip": "<strong>Tell:</strong> 'automatizei' mas ainda aprovo tudo = não automatizei, só mudei o lugar do gargalo."
   }
  ]
 }
}
```
