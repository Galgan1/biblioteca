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

# LIVRO PARA APROFUNDAR: O Príncipe — Nicolau Maquiavel

**Subtítulo:** VISÃO GERAL · COMO O PODER REALMENTE FUNCIONA
**Ideia central:** Maquiavel abandona o 'como deveria ser' e vai direto ao 'como é'. O Príncipe não pergunta se o poder é justo — pergunta como se conquista e se mantém. Um manual de realismo político que fundou a ciência política moderna.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-tipos-de-principados` — CAPÍTULO 1: Os Tipos de Principado
- `ch02-principados-mistos` — CAPÍTULO 2: Principados Mistos — Conservar o Conquistado
- `ch03-virtu-e-fortuna` — CAPÍTULO 3: Virtù × Fortuna — As Duas Vias para o Poder
- `ch04-armas-proprias` — CAPÍTULO 4: Armas Próprias × Mercenárias e Auxiliares
- `ch05-temido-ou-amado` — CAPÍTULO 5: Temido × Amado — A Verdade Efetiva
- `ch06-raposa-e-leao` — CAPÍTULO 6: A Raposa e o Leão
- `ch07-evitar-odio-desprezo` — CAPÍTULO 7: Evitar o Ódio e o Desprezo
- `ch08-reputacao-lisonjeiros` — CAPÍTULO 8: Reputação, Ministros e Lisonjeiros
- `ch09-fortuna-e-virtu` — CAPÍTULO 9: 'A Fortuna é Mulher' — Virtù e Ocasião

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-tipos-de-principados": {
  "cards": [
   {
    "ic": "layers",
    "t": "Hereditário × Novo × Misto",
    "b": "<strong>Hereditário</strong>: inércia a favor, fácil de manter. <strong>Novo</strong>: toda a dificuldade nasce aqui. <strong>Misto</strong> (território anexado): o mais traiçoeiro — gera esperança e decepção.",
    "tip": "<strong>Modelo mental:</strong> diagnostique o tipo antes de decidir a terapia — a mesma ação que sustenta um arruína o outro."
   },
   {
    "ic": "clock",
    "t": "O Tempo como Aliado",
    "b": "A <strong>antiguidade do domínio</strong> apaga a memória das mudanças. Quanto mais o poder dura, mais parece natural. O príncipe hereditário tem menos razões para ofender e por isso é mais amado.",
    "tip": "<strong>Regra:</strong> no hereditário, a inércia trabalha a seu favor — não a rompa sem necessidade."
   },
   {
    "ic": "mountain",
    "t": "A Dificuldade do Novo",
    "b": "O principado novo nasce da ambição e gera <strong>novos inimigos</strong>: todos os que se davam bem com a ordem antiga e os tíbios que poderiam se dar bem com a nova. A resistência à mudança é quase sempre mais feroz que o apoio.",
    "tip": "<strong>Sinal de alerta:</strong> ao instaurar uma nova ordem, espere oposição feroz dos antigos beneficiários e apoio morno dos futuros."
   }
  ]
 },
 "ch02-principados-mistos": {
  "cards": [
   {
    "ic": "eye",
    "t": "Cure o Mal no Broto",
    "b": "'Como a tísica: fácil de curar e difícil de conhecer no início; depois, fácil de conhecer e impossível de curar.' O custo de agir <strong>cresce exponencialmente</strong> com o tempo. <strong>Não existe evitar a guerra — só adiá-la em vantagem do inimigo.</strong>",
    "tip": "<strong>Como aplicar:</strong> aja cedo sobre sinais fracos. O problema pequeno ignorado vira crise sem solução."
   },
   {
    "ic": "pin",
    "t": "Resida no Conquistado",
    "b": "Ir morar no território conquistado (ou fundar colônias) permite ver os males nascendo e cortá-los cedo. O governo <strong>à distância</strong> só percebe quando o mal já é incurável. Colônias custam pouco e ofendem poucos; guarnições militares custam caro e ofendem todos.",
    "tip": "<strong>Modelo mental:</strong> presença detecta a desordem; distância a deixa crescer até o ponto sem retorno."
   },
   {
    "ic": "spark",
    "t": "Concentre a Dor, Dilua o Prazer",
    "b": "Ofensas devem ser feitas <strong>todas de uma vez</strong>, para serem menos sentidas; benefícios, <strong>aos poucos</strong>, para serem mais saboreados. A memória do mal feito de uma vez se apaga; a do mal repetido se acumula em ódio.",
    "tip": "<strong>Regra:</strong> ao entrar num novo Estado, decida todas as durezas necessárias de uma vez — não as renove dia após dia."
   }
  ]
 },
 "ch03-virtu-e-fortuna": {
  "cards": [
   {
    "ic": "mountain",
    "t": "Virtù: A Metade que é Sua",
    "b": "Os grandes fundadores deveram à fortuna apenas <strong>a ocasião</strong> — a matéria a ser moldada. Todo o resto foi virtù. Sem a ocasião, a virtù se desperdiça; sem virtù, a ocasião passa em vão. A virtù não é virtude moral: é eficácia, energia, audácia.",
    "tip": "<strong>Como aplicar:</strong> distinga como você chegou ao poder — por mérito (mantenha o método) ou por sorte (corra para criar raízes)."
   },
   {
    "ic": "sword",
    "t": "O Profeta Armado",
    "b": "'Todos os profetas armados venceram; os desarmados se perderam.' A persuasão sem poder de coerção é frágil: os povos são <strong>volúveis</strong>, fáceis de persuadir e difíceis de manter na crença. Quando deixam de crer, é preciso fazê-los crer à força.",
    "tip": "<strong>Modelo mental:</strong> quem implanta uma nova ordem precisa de força para sustentá-la quando a persuasão falhar."
   },
   {
    "ic": "clock",
    "t": "Fortuna Pede Raízes Rápidas",
    "b": "Quem sobe pela fortuna deve <strong>lançar raízes depressa</strong> — construir estrutura, alianças e legitimidade que não dependam do favor que o elevou. A fortuna é árbitra de metade; só a virtù garante a outra.",
    "tip": "<strong>Sinal de alerta:</strong> poder obtido por sorte ou favor alheio é frágil enquanto não tiver raízes próprias."
   }
  ]
 },
 "ch04-armas-proprias": {
  "cards": [
   {
    "ic": "sword",
    "t": "Mercenárias: Infiéis e Covardes",
    "b": "Tropas pagas lutam apenas pelo soldo, que não basta para fazê-las morrer por você. <strong>Bravas entre amigos, covardes diante do inimigo</strong> — sem fé nem disciplina real. A Itália de Maquiavel foi humilhada por confiar décadas em condottieri mercenários.",
    "tip": "<strong>Modelo mental:</strong> capacidade comprada cria dependência de quem vende, não vínculo com quem comprou."
   },
   {
    "ic": "triangle",
    "t": "Auxiliares: Ainda Piores",
    "b": "Tropas emprestadas por um aliado forte são eficazes — e por isso <strong>mais perigosas</strong>: se perdem, você está perdido com elas; se vencem, você fica refém delas. São 'armas que pesam, apertam ou cortam' em quem as veste.",
    "tip": "<strong>Sinal de alerta:</strong> vencer com força alheia não é sua vitória — é a dívida que você acumula."
   },
   {
    "ic": "key",
    "t": "A Arma Própria é a Única Segura",
    "b": "'Nenhum principado está seguro sem armas próprias; depende inteiramente da fortuna, sem virtù que o defenda na adversidade.' A guerra é o <strong>core business</strong> do príncipe — o que define a função não pode ser delegado.",
    "tip": "<strong>Como aplicar:</strong> construa competência interna nas áreas que definem o seu poder; nunca delegue o núcleo estratégico."
   }
  ]
 },
 "ch05-temido-ou-amado": {
  "cards": [
   {
    "ic": "scale",
    "t": "Temor > Amor (mas jamais Ódio)",
    "b": "Não cabendo ser ambos, <strong>prefira ser temido</strong>: o amor depende dos outros (ingratos), o temor depende de você (medo do castigo). Mas <strong>nunca odiado</strong> — a linha vermelha é não tocar nos bens e na honra dos súditos. 'Os homens esquecem mais depressa a morte do pai que a perda do patrimônio.'",
    "tip": "<strong>Modelo mental:</strong> funde o poder no que está sob seu controle — o temor. O amor depende de quem pode mudar de humor."
   },
   {
    "ic": "leaf",
    "t": "A Parcimônia Governa",
    "b": "Aceitar a fama de <strong>avaro</strong> é mais sábio que a de liberal: a liberalidade ostensiva exige sobrecarregar o povo de impostos e gera ódio; a parcimônia governa sem espoliar. Gaste o alheio com largueza; o próprio, com cautela.",
    "tip": "<strong>Como aplicar:</strong> a parcimônia é a virtude que permite manter o Estado sem criar dependência de recursos que acabam."
   },
   {
    "ic": "target",
    "t": "A Crueldade Bem Usada",
    "b": "Não temer a fama de cruel quando ela mantém os súditos unidos: poucos <strong>castigos exemplares</strong> são mais piedosos que a clemência que deixa o desgoverno gerar mortes e saques. 'A clemência mal calculada é a maior crueldade.'",
    "tip": "<strong>Regra:</strong> faça-a de uma vez, por necessidade, e não a renove — a dor concentrada se apaga; a difusa acumula ódio."
   }
  ]
 },
 "ch06-raposa-e-leao": {
  "cards": [
   {
    "ic": "mask",
    "t": "Dois Modos de Combater",
    "b": "O leão não se defende das armadilhas; a raposa, não dos lobos. É preciso ser <strong>raposa para conhecer as ciladas</strong> e <strong>leão para espantar os lobos</strong>. Cada um sozinho é cego — o príncipe alterna os dois conforme o adversário.",
    "tip": "<strong>Modelo mental:</strong> astúcia (raposa) detecta a fraude; força (leão) impede o ataque. Nunca use só um."
   },
   {
    "ic": "eye",
    "t": "A Palavra Não É Sagrada",
    "b": "A palavra <strong>não obriga</strong> quando prejudica e quando cessou a razão que a motivou — 'pois os homens, sendo maus, não a guardariam com você'. O príncipe deve ser grande simulador e dissimulador; sempre há razões legítimas para encobrir a quebra.",
    "tip": "<strong>Chave analítica:</strong> serve sobretudo para reconhecer quando um poderoso está sendo 'raposa' — quebrando a palavra sob capa de virtude."
   },
   {
    "ic": "person",
    "t": "As Cinco Aparências",
    "b": "Parecer <strong>clemente, fiel, humano, íntegro e religioso</strong> — e até sê-lo. Mas estar pronto a inverter sob necessidade. A maioria julga pela aparência e pelo resultado: 'que vença e mantenha o Estado, e os meios serão julgados honrosos.'",
    "tip": "<strong>Sinal de alerta:</strong> a aparência da virtude vale mais que a virtude num mundo que julga pelos olhos e pelo fim."
   }
  ]
 },
 "ch07-evitar-odio-desprezo": {
  "cards": [
   {
    "ic": "gap",
    "t": "As Duas Coisas a Evitar",
    "b": "<strong>Ódio</strong> (gerado por rapacidade sobre bens e honra alheios) e <strong>desprezo</strong> (gerado por aparecer volúvel, frívolo, pusilânime, irresoluto). Evitar os dois é quase suficiente — quem não é nem um nem outro raramente tem conspiradores.",
    "tip": "<strong>Regra:</strong> mostre grandeza, firmeza e decisão irrevogável; que ninguém pense em ludibriá-lo."
   },
   {
    "ic": "person",
    "t": "O Povo é a Maior Fortaleza",
    "b": "O conspirateur anda com medo e a lei contra si; o príncipe tem poder e amigos. Se o povo está do seu lado, conspirar fica <strong>quase impossível</strong>. 'A melhor fortaleza é não ser odiado pelo povo — nenhuma muralha salva quem o povo detesta.'",
    "tip": "<strong>Modelo mental:</strong> o escudo do poder é a opinião popular — base que nenhuma pedra substitui."
   },
   {
    "ic": "fork",
    "t": "Delegue o Odioso",
    "b": "As coisas de <strong>favor</strong>, o príncipe faz por si; as de <strong>punição e desagrado</strong>, delega a outros. Colhe a gratidão, terceiriza o rancor. Borgia mandou cortar ao meio o executor Remirro de Orco e o povo ficou 'satisfeito e estupefato' — a crueldade foi atribuída a um terceiro.",
    "tip": "<strong>Como aplicar:</strong> separe os fluxos de crédito e culpa. Faça o bem com seu nome; o mal, com o nome dos outros."
   }
  ]
 },
 "ch08-reputacao-lisonjeiros": {
  "cards": [
   {
    "ic": "mountain",
    "t": "Reputação por Grandes Feitos",
    "b": "Realizações notáveis e gestos memoráveis impõem admiração. <strong>Tome partido com clareza</strong>: declarar-se franco amigo ou inimigo é sempre mais útil que a neutralidade. 'Quem fica em cima do muro é descartado pelo vencedor e desprezado pelo perdedor.'",
    "tip": "<strong>Regra:</strong> posicione-se — o neutro vira presa de ambos os lados."
   },
   {
    "ic": "key",
    "t": "Bons Ministros",
    "b": "O bom ministro pensa mais no <strong>Estado que em si</strong>. Para mantê-lo fiel: honre-o, enriqueça-o e partilhe responsabilidades, para que dependa de você e tema a mudança. 'Os três cérebros': o que entende por si, o que entende o que outros entendem, e o que não entende nem por si.",
    "tip": "<strong>Como aplicar:</strong> a qualidade da equipe é o primeiro sinal da sua própria inteligência — você é julgado por quem escolhe."
   },
   {
    "ic": "bubble",
    "t": "Blinde-se dos Lisonjeiros",
    "b": "As cortes estão cheias de lisonjeiros — e os homens se comprazem com as próprias coisas. O remédio: dê a <strong>poucos sábios</strong> a liberdade de dizer a verdade, <strong>só quando perguntados</strong>. Ouça amplo, decida sozinho. 'Bons conselhos nascem da prudência do príncipe, não a prudência dos bons conselhos.'",
    "tip": "<strong>Sinal de alerta:</strong> quem ouve todos sobre tudo perde o respeito; quem não ouve ninguém se arruína."
   }
  ]
 },
 "ch09-fortuna-e-virtu": {
  "cards": [
   {
    "ic": "wave",
    "t": "Rio e Diques",
    "b": "A fortuna é um <strong>rio impetuoso</strong>: quando enfurece, arrasa tudo. Mas na calmaria os homens erguem <strong>diques e barreiras</strong> — assim o rio não causa ruína. A fortuna mostra seu poder onde não há virtù preparada para resistir.",
    "tip": "<strong>Modelo mental:</strong> metade é sorte, metade é sua. Construa os diques na calmaria — a crise só revela quem se preparou."
   },
   {
    "ic": "clock",
    "t": "Adapte-se aos Tempos",
    "b": "Feliz é quem <strong>harmoniza seu modo de agir com a qualidade dos tempos</strong>; infeliz, quem descompassa. O mesmo método dá certo numa época e arruína em outra. O problema: o homem não consegue mudar a própria natureza — por isso a fortuna varia.",
    "tip": "<strong>Como aplicar:</strong> revise periodicamente se o seu método ainda se encaixa nos tempos — a virtù que não muda vira o vício de outrora."
   },
   {
    "ic": "spark",
    "t": "A Audácia Vence o Acaso",
    "b": "A fortuna cede mais aos <strong>audaciosos</strong> do que aos cautelosos. 'É melhor ser impetuoso que cauteloso' — desde que os diques estejam de pé. Quem perde o Estado falhou em virtù, não foi traído pela sorte: 'nossa liberdade depende de nós.'",
    "tip": "<strong>Regra:</strong> na incerteza, prefira a audácia à hesitação — mas tendo construído a estrutura de suporte antes."
   }
  ]
 }
}
```
