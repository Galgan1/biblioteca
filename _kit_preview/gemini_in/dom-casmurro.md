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

# LIVRO PARA APROFUNDAR: Dom Casmurro — Machado de Assis

**Subtítulo:** VISÃO GERAL · O NARRADOR QUE QUER SER CRIDO
**Ideia central:** Um homem velho e amargo escreve a própria história para 'atar as duas pontas da vida' e acusar a esposa, Capitu, de tê-lo traído com o amigo Escobar. Mas quem conta é parte interessada: Bento Santiago é, ao mesmo tempo, advogado de acusação, juiz e única testemunha. Machado entrega ao leitor as mesmas provas frágeis que cegaram Bentinho — e deixa, de propósito, a pergunta sem resposta: Capitu traiu?

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-o-casmurro-e-o-projeto-de-atar-as-pontas` — MOVIMENTO 1: O Casmurro e o Projeto de 'Atar as Pontas da Vida'
- `ch02-a-denuncia-de-jose-dias-e-a-promessa` — MOVIMENTO 2: A Denúncia de José Dias e a Promessa do Seminário
- `ch03-olhos-de-ressaca-o-amor-de-bentinho-e-capitu` — MOVIMENTO 3: Olhos de Ressaca — o Amor de Bentinho e Capitu
- `ch04-o-seminario-e-o-pacto-com-escobar` — MOVIMENTO 4: O Seminário e o Pacto com Escobar
- `ch05-o-casamento-e-a-felicidade-conjugal` — MOVIMENTO 5: O Casamento e a Felicidade Conjugal
- `ch06-a-morte-de-escobar-e-o-olhar-de-ressaca` — MOVIMENTO 6: A Morte de Escobar e o Olhar de Capitu
- `ch07-ezequiel-o-ciume-e-a-tentacao-do-crime` — MOVIMENTO 7: Ezequiel, o Ciúme e a Tentação do Crime
- `ch08-o-veredicto-suspenso-capitu-traiu` — MOVIMENTO 8: O Veredicto Suspenso — 'Capitu Traiu?'

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-o-casmurro-e-o-projeto-de-atar-as-pontas": {
  "cards": [
   {
    "ic": "book",
    "t": "O Projeto da Narração",
    "b": "O velho escreve para 'atar as duas pontas da vida' — unir infância e velhice. Confessa que o faz para <strong>'enganar o tempo'</strong> e preencher um vazio. O relato nasce de uma carência, não de um compromisso com a verdade.",
    "tip": "<strong>Pista:</strong> um relato que nasce do tédio e da amargura pede desconfiança, não fé."
   },
   {
    "ic": "person",
    "t": "Quem É Dom Casmurro",
    "b": "O apelido veio de um vizinho — 'homem calado e metido consigo'. Bento o adota como título. <strong>Casmurro</strong>: taciturno, fixado numa ideia única. O tom de fundo de todo o livro: ressentimento e isolamento.",
    "tip": "<strong>Modelo mental:</strong> o narrador já se nomeou amargo — tudo o que se segue vem por esses olhos."
   },
   {
    "ic": "clock",
    "t": "A Memória Interessada",
    "b": "Não se lembra do passado: <strong>fabrica-se o passado a partir do presente</strong>. O velho recorda exatamente o que confirma a tese que vai defender. A casa reconstruída igual à da infância é a tentativa (vã) de repor o espaço para repor o tempo.",
    "tip": "<strong>Para refletir:</strong> memória não é arquivo; é reconstrução — e reconstrução tem autor."
   }
  ]
 },
 "ch02-a-denuncia-de-jose-dias-e-a-promessa": {
  "cards": [
   {
    "ic": "mask",
    "t": "José Dias, o 'Superlativo'",
    "b": "O agregado vive de favor na casa e paga com lisonja e mexerico. Mestre do <strong>'superlativo'</strong>: exagera tudo para parecer culto e indispensável. É ele quem define os olhos de Capitu como 'de cigana oblíqua e dissimulada'.",
    "tip": "<strong>Pista:</strong> a frase que vira 'prova' contra Capitu nasce na boca de um interesseiro."
   },
   {
    "ic": "key",
    "t": "A Promessa do Seminário",
    "b": "Dona Glória, viúva e devota, prometera a Deus tornar o filho padre. A promessa é o <strong>obstáculo 'sólido'</strong> entre Bentinho e Capitu — uma dívida com o céu que pesa sobre o corpo do filho.",
    "tip": "<strong>Modelo mental:</strong> no Brasil patriarcal, o destino se decide na sala de visitas."
   },
   {
    "ic": "person",
    "t": "A Casa de Matacavalos",
    "b": "O elenco doméstico: <strong>Dona Glória</strong> (a mãe), <strong>tio Cosme</strong> (advogado cético), <strong>prima Justina</strong> (a língua afiada) e os vizinhos <strong>Pádua</strong>, pais de Capitu. Quem domina a narrativa da casa domina os destinos.",
    "tip": "<strong>Para refletir:</strong> a delação que devia separar o casal é o que revela a Bentinho o próprio amor."
   }
  ]
 },
 "ch03-olhos-de-ressaca-o-amor-de-bentinho-e-capitu": {
  "cards": [
   {
    "ic": "wave",
    "t": "Olhos de Ressaca",
    "b": "A metáfora-síntese de Capitu (cap. XXXII): olhos que <strong>atraem e afogam</strong>, como a ressaca do mar. É elogio e acusação ao mesmo tempo — beleza e ameaça na mesma imagem.",
    "tip": "<strong>Pista:</strong> a 'ressaca' não é de Capitu; é do homem que a recorda já decidido a condená-la."
   },
   {
    "ic": "person",
    "t": "Capitu, a Força do Livro",
    "b": "Quatorze, quinze anos. Pensa rápido, dissimula quando preciso (esconde o namoro dos pais), tem ambição e visão de futuro. É <strong>a personagem mais viva e capaz</strong> do romance — Bentinho é o ingênuo ao lado dela.",
    "tip": "<strong>Para refletir:</strong> vê-la só como 'dissimulada' é aceitar a moldura do narrador."
   },
   {
    "ic": "link",
    "t": "A Cena dos Cabelos",
    "b": "Capitu pede que Bentinho lhe penteie os cabelos; ele a serve embevecido e quase se beijam. É o <strong>ápice da inocência</strong> do casal — e o instante em que o narrador deposita na amada a metáfora do perigo que dará o tom de tudo.",
    "tip": "<strong>Modelo mental:</strong> atenção em quem escolhe as metáforas — elas carregam o veredicto antecipado."
   }
  ]
 },
 "ch04-o-seminario-e-o-pacto-com-escobar": {
  "cards": [
   {
    "ic": "person",
    "t": "Escobar",
    "b": "Colega de seminário e futuro cunhado (casa-se com Sancha). Inteligência prática, talento para números e negócios. O narrador o <strong>admira com afeto</strong> — e depois fará dele o suposto amante de Capitu.",
    "tip": "<strong>Pista:</strong> quando um narrador detalha demais um secundário, pergunte que função futura ele terá no argumento."
   },
   {
    "ic": "link",
    "t": "Amizade × Amor",
    "b": "A intimidade entre Bentinho e Escobar é das mais fundas de sua vida. O narrador <strong>aproxima Escobar de Capitu</strong> (os dois casais andam juntos, Sancha e Capitu inseparáveis) — montagem que torna plausível a traição que ele já decidiu ter ocorrido.",
    "tip": "<strong>Modelo mental:</strong> a simetria dos dois casais será depois relida como triângulo."
   },
   {
    "ic": "key",
    "t": "A Saída Honrosa",
    "b": "Capitu articula com Dona Glória e José Dias a estratégia de <strong>tirar Bentinho do seminário</strong> sem ofender a promessa (pôr no lugar um órfão pago). Revela talento político e domínio sobre os adultos.",
    "tip": "<strong>Para refletir:</strong> a astúcia de Capitu vence a fé da mãe — o engenho humano contorna a dívida com o céu."
   }
  ]
 },
 "ch05-o-casamento-e-a-felicidade-conjugal": {
  "cards": [
   {
    "ic": "spiral",
    "t": "O Ciúme como Temperamento",
    "b": "Bentinho é ciumento <strong>desde menino, antes de qualquer prova</strong>. O ciúme é causa, não consequência: um olhar, um elogio de Capitu a outro homem, e a suspeita acende. O defeito do narrador se disfarça de perspicácia.",
    "tip": "<strong>Pista:</strong> ciúme 'sem causa' que ainda assim conclui culpa pede que você confunda emoção com evidência."
   },
   {
    "ic": "scale",
    "t": "A Felicidade Frágil",
    "b": "A paz doméstica é minada por dentro pela imaginação do marido. Capitu brilha em sociedade — e é justamente sua <strong>desenvoltura, que encanta</strong>, o que mais o inquieta. Ela desarma as tempestades com carinho e bom senso.",
    "tip": "<strong>Modelo mental:</strong> o ciúme é projeção — diz mais de quem sente do que do objeto suspeito."
   },
   {
    "ic": "person",
    "t": "O Filho Desejado",
    "b": "Após a espera, nasce <strong>Ezequiel</strong>, alegria do casal. Os Escobar (Escobar e Sancha) são presença diária; Escobar prospera no comércio. A convivência dos dois casais é a moldura que o marido depois lerá como triângulo.",
    "tip": "<strong>Para refletir:</strong> o filho amado de hoje será o centro da dúvida de amanhã."
   }
  ]
 },
 "ch06-a-morte-de-escobar-e-o-olhar-de-ressaca": {
  "cards": [
   {
    "ic": "wave",
    "t": "O Afogamento de Escobar",
    "b": "Escobar, bom nadador, desafia o mar e morre na ressaca. O motivo marítimo se fecha: a água que o mata é a <strong>mesma metáfora dos olhos da esposa</strong>. O acaso entrega ao ciumento a 'prova' que ele buscava.",
    "tip": "<strong>Modelo mental:</strong> a ressaca liga, simbolicamente, amante suposto e esposa suspeita."
   },
   {
    "ic": "eye",
    "t": "O Olhar no Velório",
    "b": "Diante do caixão, Capitu fixa o morto demoradamente — olhos que Bentinho descreve como <strong>'de ressaca'</strong>. Dentro da cabeça do marido, a amiga vira amante e o luto vira flagrante. Nada se diz; nada se confessa.",
    "tip": "<strong>Pista:</strong> o mesmo olhar pode ser dor de amiga OU paixão de amante — Bentinho escolhe a segunda."
   },
   {
    "ic": "scale",
    "t": "A Interpretação como Prova",
    "b": "Este é o eixo do romance. A 'prova' é <strong>pura interpretação do narrador</strong> — não há testemunha neutra. Machado dá ao leitor os mesmos dados ambíguos que Bento teve, e o deixa cair (ou não) na mesma armadilha.",
    "tip": "<strong>Como aplicar:</strong> distinga o que aconteceu (um olhar) do que foi concluído (adultério)."
   }
  ]
 },
 "ch07-ezequiel-o-ciume-e-a-tentacao-do-crime": {
  "cards": [
   {
    "ic": "masks",
    "t": "A Semelhança como Prova",
    "b": "Ezequiel 'parecido com Escobar' nos gestos e traços. Mas crianças imitam quem convivem, e a semelhança é vista por <strong>olhos já condenatórios</strong>. Ninguém mais a confirma de modo neutro. A paternidade fica indecidível.",
    "tip": "<strong>Pista:</strong> a semelhança é o tipo de prova que confirma quem já decidiu."
   },
   {
    "ic": "triangle",
    "t": "A Tentação do Infanticídio",
    "b": "Bentinho cogita <strong>envenenar Ezequiel e a si mesmo</strong> — o ciúme levado ao extremo. Recua no último instante. O horror revela o que o ciúme é: não amor levado ao limite, mas desejo de posse que destrói o objeto amado.",
    "tip": "<strong>Para refletir:</strong> o ciumento não quer a verdade; quer a confirmação."
   },
   {
    "ic": "gap",
    "t": "O Repúdio Disfarçado",
    "b": "Em vez de processo ou escândalo, Bentinho escolhe o exílio: <strong>manda mulher e filho à Europa</strong> e fica. Capitu, confrontada, nega e pergunta atônita do que é acusada — mas a defesa chega filtrada pelo acusador, que já não a ouve.",
    "tip": "<strong>Modelo mental:</strong> a 'casmurrice' do início nasce aqui — do homem que se condenou à solidão."
   }
  ]
 },
 "ch08-o-veredicto-suspenso-capitu-traiu": {
  "cards": [
   {
    "ic": "scale",
    "t": "A Ambiguidade É o Projeto",
    "b": "Machado não esconde a resposta — torna-a <strong>indecidível</strong>. Dá ao leitor todos os elementos para concluir o oposto: um narrador confessadamente ciumento, parcial, único informante, que controlou cada palavra. Ambiguidade não é falha; é o sentido.",
    "tip": "<strong>Regra de ouro:</strong> a resposta correta a 'Capitu traiu?' é expor o debate, não dar veredicto."
   },
   {
    "ic": "eye",
    "t": "A Verdadeira Pergunta",
    "b": "A última pergunta do livro não é 'Capitu traiu?' e sim <strong>'por que você acreditou em Bentinho?'</strong>. O tema profundo é a leitura, a memória e a manipulação. O leitor é o júri — e julgar, ali, é cair na armadilha.",
    "tip": "<strong>Crítica:</strong> Helen Caldwell (1960) inverteu a leitura — de 'Capitu culpada' para 'Bentinho narrador paranoico'."
   },
   {
    "ic": "book",
    "t": "A Solidão Final",
    "b": "O projeto de 'atar as pontas da vida' <strong>fracassa</strong>: o velho fica mais só do que começou, na casa restaurada e vazia. O silêncio de Capitu — que nunca tem voz própria — é a chave de toda a ambiguidade.",
    "tip": "<strong>Intertexto:</strong> o 'Otelo brasileiro' — mas Machado tira a certeza que Shakespeare dava ao público."
   }
  ]
 }
}
```
