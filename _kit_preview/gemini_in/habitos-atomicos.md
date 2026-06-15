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

# LIVRO PARA APROFUNDAR: Hábitos Atômicos — James Clear

**Subtítulo:** VISÃO GERAL · PEQUENAS MUDANÇAS, RESULTADOS NOTÁVEIS
**Ideia central:** Você não sobe ao nível das suas metas — cai ao nível dos seus sistemas. Um hábito atômico é uma mudança de 1% que, repetida, compõe resultados notáveis. James Clear mostra o loop do hábito, as quatro leis da mudança de comportamento e a alavanca mais profunda de todas: a identidade.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-1porcento-sistemas` — CAPÍTULO 1: O 1% e os Sistemas
- `ch02-identidade` — CAPÍTULO 2: Hábitos e Identidade
- `ch03-loop-do-habito` — CAPÍTULO 3: O Loop do Hábito
- `ch04-lei1-obvio` — CAPÍTULO 4: 1ª Lei — Torne Óbvio
- `ch05-lei2-atraente` — CAPÍTULO 5: 2ª Lei — Torne Atraente
- `ch06-lei3-facil` — CAPÍTULO 6: 3ª Lei — Torne Fácil
- `ch07-lei4-satisfatorio` — CAPÍTULO 7: 4ª Lei — Torne Satisfatório
- `ch08-avancado` — CAPÍTULO 8: Avançado — Manter e Dominar

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-1porcento-sistemas": {
  "cards": [
   {
    "ic": "spark",
    "t": "Os Juros Compostos do Comportamento",
    "b": "<strong>1% melhor a cada dia ≈ 37×</strong> em um ano; 1% pior tende a zero. O hábito é a unidade que compõe — para o bem ou para o mal.",
    "tip": "<strong>Modelo mental:</strong> importa a trajetória do 1%, não o ponto de hoje."
   },
   {
    "ic": "pivot",
    "t": "Sistemas > Metas",
    "b": "\"Você não sobe ao nível das suas metas — <strong>cai ao nível dos seus sistemas</strong>.\" Vencedores e perdedores têm as mesmas metas; o que difere é o sistema diário.",
    "tip": "<strong>Como aplicar:</strong> projete o sistema; deixe a meta ser subproduto."
   },
   {
    "ic": "clock",
    "t": "O Platô do Potencial Latente",
    "b": "O progresso fica invisível antes de aparecer — o <strong>vale da decepção</strong>. Como o gelo que só derrete ao cruzar zero grau: persistir é cruzar o platô.",
    "tip": "<strong>Cuidado:</strong> abandonar no vale, às vésperas do platô virar, é o erro mais comum."
   }
  ]
 },
 "ch02-identidade": {
  "cards": [
   {
    "ic": "layers",
    "t": "Os Três Níveis",
    "b": "<strong>Resultados → processos → identidade.</strong> A maioria muda de fora para dentro; o durável é de dentro para fora — começa por quem você crê ser.",
    "tip": "<strong>Como aplicar:</strong> decida que tipo de pessoa quer ser e prove com pequenas ações."
   },
   {
    "ic": "key",
    "t": "Cada Hábito é um Voto",
    "b": "Ler uma página é um voto em \"sou um leitor\". A meta não é correr uma maratona — é <strong>tornar-se um corredor</strong>. A prova acumulada reescreve a autoimagem.",
    "tip": "<strong>Regra:</strong> colete votos, não perfeição — não precisa de maioria absoluta."
   },
   {
    "ic": "mask",
    "t": "A Identidade que Aprisiona",
    "b": "\"Sou desorganizado\", \"sou ruim de número\" — uma identidade rígida vira <strong>profecia autorrealizável</strong>. Segure suas identidades de forma leve.",
    "tip": "<strong>Sinal de alerta:</strong> quando a autoimagem trava a mudança, ela virou jaula."
   }
  ]
 },
 "ch03-loop-do-habito": {
  "cards": [
   {
    "ic": "spiral",
    "t": "Os Quatro Estágios",
    "b": "<strong>Deixa → Desejo → Resposta → Recompensa.</strong> A deixa dispara, o desejo motiva, a resposta executa, a recompensa satisfaz e <strong>ensina</strong> o cérebro a repetir.",
    "tip": "<strong>Como aplicar:</strong> hábito que não pega? veja qual dos 4 estágios falhou."
   },
   {
    "ic": "target",
    "t": "Você Não Deseja o Hábito",
    "b": "Você deseja a <strong>mudança de estado</strong> que ele promete — não a ação em si. O cigarro não é o desejo; o alívio é.",
    "tip": "<strong>Modelo mental:</strong> mude a recompensa esperada e muda o desejo."
   },
   {
    "ic": "gap",
    "t": "Problema vs. Solução",
    "b": "Deixa + desejo = a fase do <strong>problema</strong>; resposta + recompensa = a <strong>solução</strong>. Hábitos resolvem problemas recorrentes com o mínimo de energia.",
    "tip": "<strong>Regra:</strong> não ataque só a força de vontade (a resposta) — use a lei do estágio certo."
   }
  ]
 },
 "ch04-lei1-obvio": {
  "cards": [
   {
    "ic": "eye",
    "t": "Pontuação e Intenção",
    "b": "<strong>Pontuação de hábitos</strong> (liste e marque +/–/=): a consciência vem antes da mudança. <strong>Intenção de implementação</strong> — \"vou [hábito] às [hora] em [local]\".",
    "tip": "<strong>Como aplicar:</strong> datar e localizar o hábito dobra a adesão."
   },
   {
    "ic": "link",
    "t": "Empilhamento de Hábitos",
    "b": "Ancore o novo num que já existe — \"<strong>depois de [hábito atual], vou [novo hábito]</strong>\". A rotina antiga vira a deixa da nova.",
    "tip": "<strong>Exemplo:</strong> \"depois de fazer o café, leio uma página\"."
   },
   {
    "ic": "pin",
    "t": "O Ambiente Vence a Vontade",
    "b": "Deixas do bom hábito <strong>visíveis</strong>; do mau, escondidas. O ambiente é constante; a força de vontade é finita. Cada espaço, um uso.",
    "tip": "<strong>Regra:</strong> para largar um mau hábito, torne a deixa invisível — não resista a ela."
   }
  ]
 },
 "ch05-lei2-atraente": {
  "cards": [
   {
    "ic": "spark",
    "t": "Agrupamento de Tentação",
    "b": "Junte algo que você <strong>quer</strong> fazer com algo que <strong>precisa</strong> fazer — \"só vejo a série na esteira\". O desejo de um puxa o outro.",
    "tip": "<strong>Como aplicar:</strong> emparelhe o hábito necessário com um prazer imediato."
   },
   {
    "ic": "bubble",
    "t": "As Normas do Grupo",
    "b": "Copiamos os <strong>próximos</strong> (família/amigos), os <strong>muitos</strong> (a maioria) e os <strong>poderosos</strong> (status). Entre na tribo onde o seu hábito já é o normal.",
    "tip": "<strong>Regra:</strong> pertencimento vence lógica — escolha a cultura, não só o hábito."
   },
   {
    "ic": "bulb",
    "t": "Reformule a Mente",
    "b": "Troque \"<strong>tenho que</strong>\" por \"<strong>tenho a oportunidade de</strong>\". A associação emocional da deixa muda o desejo.",
    "tip": "<strong>Modelo mental:</strong> o pico de dopamina vem na antecipação, antes da recompensa."
   }
  ]
 },
 "ch06-lei3-facil": {
  "cards": [
   {
    "ic": "leaf",
    "t": "A Lei do Menor Esforço",
    "b": "O cérebro escolhe o caminho de <strong>menor atrito</strong>. Reduza o atrito do bom hábito e aumente o do mau — o ambiente faz o trabalho.",
    "tip": "<strong>Como aplicar:</strong> −atrito no bom, +atrito no mau (tire a bateria do controle)."
   },
   {
    "ic": "clock",
    "t": "A Regra dos 2 Minutos",
    "b": "Toda nova rotina começa numa versão de <strong>≤ 2 minutos</strong> — \"ler\" = ler uma página; \"treinar\" = calçar o tênis. Domine a <strong>arte de aparecer</strong>; escale depois.",
    "tip": "<strong>Regra:</strong> padronize antes de otimizar — primeiro o hábito existe, depois cresce."
   },
   {
    "ic": "steps",
    "t": "Compromisso e Automação",
    "b": "Decisões únicas que <strong>travam o futuro</strong> — débito automático para poupar, deletar o app. Um esforço hoje, o comportamento certo por meses.",
    "tip": "<strong>Modelo mental:</strong> facilite o começo; a inércia inicial é o maior obstáculo."
   }
  ]
 },
 "ch07-lei4-satisfatorio": {
  "cards": [
   {
    "ic": "key",
    "t": "Recompensa Imediata",
    "b": "O cérebro prioriza o presente; a recompensa tardia perde para a tentação imediata. Anexe uma <strong>pequena gratificação</strong> ao fim do hábito — coerente com a identidade desejada.",
    "tip": "<strong>Como aplicar:</strong> feche o loop com prazer imediato, senão o bom hábito morre de tédio."
   },
   {
    "ic": "steps",
    "t": "O Rastreador de Hábitos",
    "b": "Marcar \"feito\" é satisfatório e visual — \"<strong>não quebre a corrente</strong>\". O que se mede e se vê progredir, se mantém.",
    "tip": "<strong>Regra:</strong> a própria corrente vira a recompensa e o jogo."
   },
   {
    "ic": "target",
    "t": "Nunca Falhe Duas Vezes",
    "b": "Errar uma vez é acidente; <strong>duas seguidas</strong> é o início de um novo (mau) hábito. Recompor rápido vale mais que ser perfeito.",
    "tip": "<strong>Sinal de alerta:</strong> \"já que falhei, desisto\" é a armadilha — só não falhe de novo."
   }
  ]
 },
 "ch08-avancado": {
  "cards": [
   {
    "ic": "mountain",
    "t": "O Jogo Certo + Cachinhos Dourados",
    "b": "Genes e aptidões inclinam o tabuleiro — jogue onde sua natureza favorece. E a <strong>Regra de Cachinhos Dourados</strong>: motivação no pico quando o desafio está <strong>no limite</strong> da capacidade (nem fácil, nem impossível).",
    "tip": "<strong>Como aplicar:</strong> ajuste a dificuldade ao seu limite para manter o engajamento."
   },
   {
    "ic": "eye",
    "t": "O Lado Sombrio dos Hábitos",
    "b": "A automaticidade cria <strong>platôs</strong>: você repete sem melhorar. Hábito + prática deliberada — automatize o básico e direcione a atenção à próxima fronteira.",
    "tip": "<strong>Cuidado:</strong> piloto automático cego para de crescer."
   },
   {
    "ic": "pivot",
    "t": "Revisão e Reflexão",
    "b": "Revisões periódicas evitam que o hábito siga no automático longe do objetivo e reavaliam a identidade. <strong>Apaixonar-se pelo tédio</strong> é o que separa o profissional do amador.",
    "tip": "<strong>Regra:</strong> o profissional aparece mesmo sem novidade; o amador só com motivação."
   }
  ]
 }
}
```
