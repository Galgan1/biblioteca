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

# LIVRO PARA APROFUNDAR: Crime e Castigo — Fiódor Dostoiévski

**Subtítulo:** VISÃO GERAL · A CONSCIÊNCIA COMO VERDADEIRO TRIBUNAL
**Ideia central:** Raskólnikov mata uma agiota para provar que é um 'homem extraordinário' acima da lei moral. Mas o castigo do título não é a Sibéria — é a consciência. Dostoiévski não refuta o niilismo por argumento: refuta-o pela vida de quem o viveu.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-teoria-homem-extraordinario` — CAPÍTULO 1: A Teoria do 'Homem Extraordinário'
- `ch02-o-crime-petersburgo` — CAPÍTULO 2: O Crime — Aliona, Lizavieta, Petersburgo
- `ch03-culpa-consciencia-castigo` — CAPÍTULO 3: A Culpa e a Consciência — O Verdadeiro Castigo
- `ch04-sonia-amor-sacrificio-fe` — CAPÍTULO 4: Sônia — Amor, Sacrifício e Fé
- `ch05-porfiry-duelo-psicologico` — CAPÍTULO 5: Porfiry — O Duelo Psicológico
- `ch06-svidrigailov-o-duplo` — CAPÍTULO 6: Svidrigáilov — O Duplo Niilista
- `ch07-razumikhin-dunia-familia` — CAPÍTULO 7: Razumíkhin, Dúnia e a Família
- `ch08-petersburgo-miseria-simbolos` — CAPÍTULO 8: Petersburgo, Miséria e Símbolos
- `ch09-confissao-sofrimento-epilogo` — CAPÍTULO 9: Confissão, Sofrimento e Ressurreição

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-teoria-homem-extraordinario": {
  "cards": [
   {
    "ic": "triangle",
    "t": "Ordinários × Extraordinários",
    "b": "A tese central: os <strong>extraordinários</strong> (Napoleão, legisladores) teriam o direito de 'transpor o sangue' por uma ideia nova; os <strong>ordinários</strong> existem para obedecer. O crime é a prova — não o roubo.",
    "tip": "<strong>Modelo mental:</strong> leia o assassinato como experimento filosófico, não como crime passional."
   },
   {
    "ic": "spark",
    "t": "A Refutação pela Carne",
    "b": "Dostoiévski não derrota a teoria no debate: deixa Raskólnikov <strong>aplicá-la</strong> e ver o que acontece. A refutação é a febre, o delírio e o isolamento — o sofrimento que a razão não previu.",
    "tip": "<strong>Para o leitor:</strong> quando uma ideia parece 'logicamente fechada' e custa sofrimento real, suspeite da lógica."
   },
   {
    "ic": "mask",
    "t": "A Dupla Justificativa",
    "b": "Raskólnikov tem duas razões para o mesmo ato — a <strong>utilitarista</strong> ('uma morte para mil bens') e a <strong>napoleônica</strong> ('o direito do superior'). Quando um ato precisa de duas justificativas nobres, a verdadeira causa está escondida: orgulho ferido, miséria, isolamento.",
    "tip": "<strong>Como aplicar:</strong> identifique quando você usa duas razões para justificar uma mesma decisão inconveniente."
   }
  ]
 },
 "ch02-o-crime-petersburgo": {
  "cards": [
   {
    "ic": "eye",
    "t": "Lizavieta Refuta a Teoria",
    "b": "A morte <strong>acidental</strong> de Lizavieta — irmã pobre da agiota, uma das 'humilhadas' que a teoria pretendia salvar — já derruba o plano no ato: qualquer crime 'cirúrgico' produz vítimas não previstas.",
    "tip": "<strong>Modelo mental:</strong> toda ação sobre o mundo tem consequências que o planejador não vê. A teoria nunca é cirúrgica."
   },
   {
    "ic": "mountain",
    "t": "A Cidade como Estado de Alma",
    "b": "Petersburgo não é cenário: é <strong>personagem</strong>. O calor sufocante, as ruas imundas, o quarto-caixão amarelo — a miséria torna a teoria utilitarista sedutora. O romance a denuncia sem aceitar a miséria como desculpa.",
    "tip": "<strong>Para o leitor:</strong> o ambiente que Dostoiévski constrói é argumento — identifique como o espaço molda o pensamento dos personagens."
   },
   {
    "ic": "gap",
    "t": "O Butim Abandonado",
    "b": "Raskólnikov <strong>mal toca no butim</strong>: esconde-o e esquece. Prova que o motivo nunca foi o dinheiro — foi a teoria. O crime como teste existencial, não como crime de necessidade.",
    "tip": "<strong>Como aplicar:</strong> quando alguém age de forma contrária ao seu 'interesse declarado', procure a motivação real escondida."
   }
  ]
 },
 "ch03-culpa-consciencia-castigo": {
  "cards": [
   {
    "ic": "spiral",
    "t": "Castigo Interior, Antes da Lei",
    "b": "O remorso é <strong>involuntário</strong>: a teoria decretou o crime inocente; a consciência não aceitou o decreto. O sofrimento não é medo de cadeia — é a descoberta de que ele não é Napoleão.",
    "tip": "<strong>Modelo mental:</strong> a lei interna cobra antes da lei externa. O 'castigo' começa no momento do ato."
   },
   {
    "ic": "gap",
    "t": "O Isolamento como Morte em Vida",
    "b": "A culpa corta o fio que liga Raskólnikov aos vivos: ele não consegue mais ser tocado pela mãe, pela irmã, pelo amigo. O crime o separa da humanidade antes de qualquer prisão — <strong>morte em vida</strong>.",
    "tip": "<strong>Para o leitor:</strong> observe como o isolamento voluntário do culpado é mais punitivo que qualquer sentença."
   },
   {
    "ic": "bulb",
    "t": "A Necessidade de Confessar",
    "b": "Ele quase confessa a estranhos várias vezes — atração pelo abismo de se entregar. O segredo pesa mais que o medo de ser pego: a consciência busca <strong>testemunha</strong>.",
    "tip": "<strong>Como aplicar:</strong> a necessidade de partilhar o peso moral é mais forte que o cálculo racional. A confissão é humana."
   }
  ]
 },
 "ch04-sonia-amor-sacrificio-fe": {
  "cards": [
   {
    "ic": "leaf",
    "t": "Transgressão por Amor",
    "b": "Sônia também transgrediu a lei moral — mas por <strong>amor à família</strong>, não por orgulho ou teoria. O contraste é o coração do romance: o mesmo ato tem raízes opostas e destinos opostos.",
    "tip": "<strong>Modelo mental:</strong> o 'o quê' (a transgressão) é menos revelador que o 'por quê' (o móvel). O móvel define o destino."
   },
   {
    "ic": "book",
    "t": "A Leitura de Lázaro",
    "b": "Sônia lê a Raskólnikov a ressurreição de Lázaro. A cena é a <strong>promessa</strong> do epílogo: o morto-em-vida pode ressuscitar, mas só pelo sofrimento aceito e pela fé — não pela teoria que o matou.",
    "tip": "<strong>Para o leitor:</strong> a escolha do episódio bíblico por Dostoiévski não é ornamento — é programa narrativo."
   },
   {
    "ic": "key",
    "t": "A Fé sem Argumento",
    "b": "Sônia não refuta a teoria de Raskólnikov com lógica — ela lhe apresenta <strong>uma vida</strong>. A fé aqui não é doutrina: é amor encarnado que resiste onde a razão colapsa.",
    "tip": "<strong>Como aplicar:</strong> diante de uma ideia que destrói, o contra-argumento mais forte é uma vida bem vivida, não um silogismo."
   }
  ]
 },
 "ch05-porfiry-duelo-psicologico": {
  "cards": [
   {
    "ic": "lens",
    "t": "O Investigador que Caça a Alma",
    "b": "Porfiry não tem provas físicas: usa a <strong>própria teoria</strong> de Raskólnikov como isca. Ao fazê-lo expor o artigo, está coletando a confissão do móvel. O método é psicológico — cada pergunta é uma estocada disfarçada de curiosidade acadêmica.",
    "tip": "<strong>Modelo mental:</strong> o investigador explora a necessidade do culpado de ser reconhecido — 'você quer me contar, eu sei'."
   },
   {
    "ic": "wave",
    "t": "A Culpa como Aliada",
    "b": "Porfiry sabe que o tormento interior fará o trabalho por ele: basta <strong>não deixar Raskólnikov se anestesiar</strong>. O tempo, a culpa e a necessidade de confessar são seus aliados — a prisão seria um alívio.",
    "tip": "<strong>Para o leitor:</strong> o investigador não é o antagonista — é quase um terapeuta que força a crise necessária."
   },
   {
    "ic": "fork",
    "t": "'Você Precisa de Ar'",
    "b": "Porfiry diz: 'entregue-se — você precisa de ar'. A confissão não é derrota: é libertação da asfixia do segredo. O <strong>sofrimento aceito</strong>, prefigura ele, é o caminho — não a impunidade.",
    "tip": "<strong>Como aplicar:</strong> reconhecer o erro publicamente é doloroso, mas o silêncio culpado sufoca mais."
   }
  ]
 },
 "ch06-svidrigailov-o-duplo": {
  "cards": [
   {
    "ic": "masks",
    "t": "O Duplo sem Consciência",
    "b": "Svidrigáilov prova a teoria pela <strong>ausência de remorso</strong>: vive o 'tudo é permitido' e não se destrói por dentro — destrói-se por fora (o vazio). É o futuro de Raskólnikov sem a consciência que ainda o salva.",
    "tip": "<strong>Modelo mental:</strong> o duplo revela o destino do herói se ele seguisse a lógica até o fim sem o freio moral."
   },
   {
    "ic": "gap",
    "t": "O Niilismo que Esvazia",
    "b": "Svidrigáilov é capaz de boas ações (liberta Sônia, cuida de crianças) — mas o gesto não o preenche. O niilismo coerente <strong>não dá sentido</strong>: as boas ações são caprichos, não compromisso. O vazio final é o suicídio.",
    "tip": "<strong>Para o leitor:</strong> Dostoiévski mostra que mesmo o niilista 'benevolente' colapsa — sem fundamento, qualquer gesto é arbitrário."
   },
   {
    "ic": "mountain",
    "t": "O Suicídio como Lógica Final",
    "b": "Svidrigáilov não morre por culpa: morre por <strong>tédio do nada</strong>. Sem consciência que torture nem fé que sustente, o niilismo consistente tem um único destino. É o anti-epílogo de Raskólnikov.",
    "tip": "<strong>Como aplicar:</strong> meça qualquer sistema de ideias pelo que acontece quando ele é vivido até as últimas consequências."
   }
  ]
 },
 "ch07-razumikhin-dunia-familia": {
  "cards": [
   {
    "ic": "person",
    "t": "Razumíkhin — O Foil Vital",
    "b": "Amigo leal, pobre como Raskólnikov mas trabalhador e alegre, Razumíkhin é o <strong>contra-argumento vivo</strong>: as mesmas condições, escolhas diferentes. A miséria não gera a teoria — o orgulho isolado a gera.",
    "tip": "<strong>Modelo mental:</strong> o foil mede o herói pela comparação — identifique quem em sua vida faz escolhas diferentes nas mesmas circunstâncias."
   },
   {
    "ic": "scale",
    "t": "Dúnia — Orgulho com Fé",
    "b": "Tão forte e orgulhosa quanto o irmão, Dúnia tem a <strong>fé</strong> que ele perdeu. Quando Svidrigáilov a cerca, ela resiste e foge — o mesmo orgulho que em Raskólnikov virou teoria, nela vira recusa ética.",
    "tip": "<strong>Para o leitor:</strong> a fé não é fraqueza nem ingenuidade — é o que distingue o orgulho que salva do orgulho que destrói."
   },
   {
    "ic": "key",
    "t": "Lújin — O Crime Respeitável",
    "b": "Lújin é o egoísmo calculado dentro dos limites da lei: usa pessoas, manipula, instrumentaliza — mas com <strong>respeitabilidade social</strong>. É a face 'aceitável' do 'tudo é permitido'. O romance o expõe como crime sem machado.",
    "tip": "<strong>Como aplicar:</strong> identifique quando a frieza calculista 'legal' causa tanto dano quanto a transgressão declarada."
   }
  ]
 },
 "ch08-petersburgo-miseria-simbolos": {
  "cards": [
   {
    "ic": "layers",
    "t": "A Cidade como Argumento",
    "b": "Petersburgo não é fundo decorativo: o <strong>calor, a sujeira, a superlotação</strong> são argumentos narrativos que tornam a teoria de Raskólnikov compreensível — mas não justificada. Dostoiévski denuncia a miséria e a teoria ao mesmo tempo.",
    "tip": "<strong>Para o leitor:</strong> observe como Dostoiévski usa o ambiente para gerar empatia sem isentar o protagonista da responsabilidade moral."
   },
   {
    "ic": "eye",
    "t": "O Mapa dos Símbolos",
    "b": "<strong>Amarelo</strong> = doença e sordidez. <strong>Machado</strong> = violência sob a teoria abstrata. <strong>Água</strong> = morte (Svidrigáilov) e batismo (epílogo). <strong>Cruz/encruzilhada</strong> = sofrimento aceito e contrição. <strong>Sonho da peste</strong> = niilismo racionalista como epidemia.",
    "tip": "<strong>Como aplicar:</strong> leia os objetos e cores como portadores de tese — em Dostoiévski nada é decorativo."
   },
   {
    "ic": "pin",
    "t": "O Quarto-Caixão",
    "b": "O quarto de Raskólnikov — estreito, amarelo, sufocante — é a <strong>externalização da clausura mental</strong>: a ideia apodrece no mesmo espaço que o mantém vivo. Porfiry diz 'você precisa de ar': o quarto é o oposto do ar.",
    "tip": "<strong>Modelo mental:</strong> os espaços físicos em Dostoiévski espelham o estado psicológico — identifique qual 'quarto-caixão' aprisiona seus personagens favoritos."
   }
  ]
 },
 "ch09-confissao-sofrimento-epilogo": {
  "cards": [
   {
    "ic": "mountain",
    "t": "A Confissão sem Arrependimento",
    "b": "Ele se entrega — mas <strong>ainda defende a teoria</strong>. O arrependimento moral só vem no epílogo. A confissão é o primeiro passo, não a chegada: o ato externo precede a transformação interna.",
    "tip": "<strong>Modelo mental:</strong> a mudança real costuma começar pela ação (a confissão) antes que o sentimento (o arrependimento) a acompanhe."
   },
   {
    "ic": "spiral",
    "t": "O Sonho da Peste",
    "b": "Na Sibéria, Raskólnikov sonha com uma 'praga' que faz cada pessoa crer-se depositária da verdade única — <strong>niilismo racionalista como epidemia</strong>. O sonho é o diagnóstico de toda uma época de ideias.",
    "tip": "<strong>Para o leitor:</strong> o sonho da peste é a metáfora mais densa de Dostoiévski — toda ideologia que exclui a consciência moral se torna contágio coletivo."
   },
   {
    "ic": "leaf",
    "t": "A Ressurreição pelo Amor",
    "b": "No epílogo, ao desabar aos pés de Sônia, o 'novo homem' emerge. A 'vida toma o lugar da dialética': não a lógica, não o argumento — o <strong>amor e o sofrimento aceito</strong> fazem o que a razão não fez.",
    "tip": "<strong>Como aplicar:</strong> a transformação profunda não vem de raciocínio melhor, mas de experiência vivida — sofrimento recebido e amor correspondido."
   }
  ]
 }
}
```
