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

# LIVRO PARA APROFUNDAR: Homo Deus — Yuval Noah Harari

**Subtítulo:** VISÃO GERAL · UMA BREVE HISTÓRIA DO AMANHÃ
**Ideia central:** Vencidos a fome, a peste e a guerra, a humanidade do século 21 mira uma nova agenda: imortalidade, felicidade e divindade — o upgrade de Homo sapiens a Homo deus. Mas o mesmo motor que nos deu esse poder (ver o humano como algoritmo bioquímico) corrói o livre-arbítrio, o indivíduo e o humanismo — e anuncia um novo culto: o dataísmo, a religião dos dados.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-nova-agenda-humana` — CAPÍTULO 1: A Nova Agenda Humana
- `ch02-antropoceno` — CAPÍTULO 2: O Antropoceno
- `ch03-fagulha-humana` — CAPÍTULO 3: A Fagulha Humana
- `ch04-contadores-de-historias` — CAPÍTULO 4: Os Contadores de Histórias
- `ch05-o-casal-estranho` — CAPÍTULO 5: O Casal Estranho
- `ch06-o-pacto-moderno` — CAPÍTULO 6: O Pacto Moderno
- `ch07-a-revolucao-humanista` — CAPÍTULO 7: A Revolução Humanista
- `ch08-a-bomba-relogio-no-laboratorio` — CAPÍTULO 8: A Bomba-Relógio no Laboratório
- `ch09-a-grande-desconexao-e-dataismo` — CAPÍTULO 9: A Grande Desconexão e o Dataísmo

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-nova-agenda-humana": {
  "cards": [
   {
    "ic": "spark",
    "t": "Os Três Flagelos Vencidos",
    "b": "Hoje morre mais gente de <strong>excesso</strong> (obesidade) que de fome, mais de velhice que de peste, mais por suicídio que por guerra. Não foram milagres: foram <strong>conquistas humanas</strong>. Fome, peste e guerra deixaram de ser destino e viraram <em>falhas de gestão</em>.",
    "tip": "<strong>Modelo mental:</strong> pense 'problema gerenciável', não 'fatalidade' — é aí que a ambição salta de patamar."
   },
   {
    "ic": "clock",
    "t": "A Nova Agenda",
    "b": "Três projetos substituem o cardápio de sobrevivência: <strong>imortalidade</strong> (a-mortalidade: a morte como problema técnico), <strong>felicidade</strong> (engenharia bioquímica do bem-estar) e <strong>divindade</strong> (poderes de criação via bio e máquina).",
    "tip": "<strong>Para refletir:</strong> a felicidade vira projeto de engenharia porque o prazer tem teto biológico."
   },
   {
    "ic": "pivot",
    "t": "De Pedir a Tornar-se Deus",
    "b": "A religião antiga pedia alívio dos flagelos. A humanidade do século 21 quer se <strong>promover</strong>: fazer o upgrade da espécie de <em>Homo sapiens</em> a <strong>Homo deus</strong>. Toda solução abre uma agenda maior — e mais perigosa.",
    "tip": "<strong>Modelo mental:</strong> resolver a sobrevivência não traz paz; libera energia para projetos de risco existencial."
   }
  ]
 },
 "ch02-antropoceno": {
  "cards": [
   {
    "ic": "layers",
    "t": "O Antropoceno",
    "b": "Pela primeira vez, <strong>uma espécie</strong> altera clima, ecossistemas e a própria vida na Terra. O Sapiens já provocou a maior onda de extinções desde o asteroide.",
    "tip": "<strong>Modelo mental:</strong> o domínio humano é fato biológico — não licença moral."
   },
   {
    "ic": "leaf",
    "t": "A Queda da Alma",
    "b": "A tradição dizia: humanos têm <strong>alma</strong>, animais não — daí nossa superioridade. A evolução não encontra alma alguma: humano e animal diferem em <strong>grau</strong>, não em <strong>essência</strong>. Cai o pilar que justificava o domínio.",
    "tip": "<strong>Para refletir:</strong> a 'alma' é uma ficção herdada, não um dado da ciência."
   },
   {
    "ic": "scale",
    "t": "Capacidade ≠ Direito",
    "b": "A pecuária industrial é o maior 'sucesso' evolutivo e a maior catástrofe de <strong>sofrimento</strong>: seres sencientes reduzidos a máquinas de produção. Poder dominar não nos torna justos — e prefigura como o forte pode tratar o dispensável.",
    "tip": "<strong>Modelo mental:</strong> o tratamento dos animais é espelho preditivo da relação elite × 'classe inútil'."
   }
  ]
 },
 "ch03-fagulha-humana": {
  "cards": [
   {
    "ic": "bulb",
    "t": "Consciência × Inteligência",
    "b": "<strong>Consciência</strong> = sentir; <strong>inteligência</strong> = resolver problemas. Animais têm consciência, e a ciência sequer sabe <em>para que ela serve</em>. São coisas diferentes — e isso prepara o desacoplamento que define o futuro.",
    "tip": "<strong>Modelo mental:</strong> 'sentir' e 'resolver' podem se separar — guarde isso para ler o futuro do trabalho."
   },
   {
    "ic": "gap",
    "t": "Não Há Livre-Arbítrio",
    "b": "Você faz o que <strong>deseja</strong>, mas não escolhe o que deseja: os desejos brotam de processos bioquímicos. Experimentos <strong>provocam vontades</strong> por estímulo externo. O liberalismo, fundado no livre-arbítrio, perde o chão.",
    "tip": "<strong>Para refletir:</strong> sentir um desejo não é tê-lo escolhido — daí a manipulabilidade."
   },
   {
    "ic": "fork",
    "t": "O 'Dividual'",
    "b": "Há dois eus: o <strong>experiencial</strong> (vive o instante) e o <strong>narrador</strong> (conta a história e decide, distorcendo pela regra do <em>pico-fim</em>). O humano não é um <em>in</em>divíduo, é um <strong>feixe de algoritmos</strong> sem CEO interno.",
    "tip": "<strong>Modelo mental:</strong> desconfie do seu narrador — ele guarda picos e finais, não a verdade do que viveu."
   }
  ]
 },
 "ch04-contadores-de-historias": {
  "cards": [
   {
    "ic": "layers",
    "t": "Três Níveis de Realidade",
    "b": "<strong>Objetiva</strong> (existe sem crença: a gravidade); <strong>subjetiva</strong> (na mente de um: minha dor); <strong>intersubjetiva</strong> (na rede de crenças de muitos: dinheiro, Estado, Deus). Some a crença coletiva, some a coisa.",
    "tip": "<strong>Teste do real:</strong> só o que pode <em>sofrer</em> é objetivamente real; o resto é história compartilhada."
   },
   {
    "ic": "book",
    "t": "Ficções Movem o Mundo",
    "b": "Nenhuma instituição grande funciona sem uma história. O <strong>dinheiro</strong> é a ficção de maior sucesso já contada — confiam nele até os que não confiam em mais nada.",
    "tip": "<strong>Modelo mental:</strong> quem fala em 'mercado', 'nação' e 'empresa' como fatos naturais esquece que são acordos revogáveis."
   },
   {
    "ic": "mask",
    "t": "A Ferramenta Vira Senhor",
    "b": "Criamos ficções como ferramentas, mas elas viram <strong>fins em si</strong>: sacrificamos vidas reais por entidades imaginadas (honra nacional, lucro, fé). A história a serviço de humanos passa a ter humanos a seu serviço.",
    "tip": "<strong>Para refletir:</strong> cuidado quando o real (sofrimento, vidas) é sacrificado pelo imaginado."
   }
  ]
 },
 "ch05-o-casal-estranho": {
  "cards": [
   {
    "ic": "link",
    "t": "Religião (def. de Harari)",
    "b": "Religião não é crença em deuses: é qualquer <strong>sistema de normas com legitimidade sobre-humana</strong> (acima do arbítrio humano). Logo <strong>liberalismo, comunismo e nazismo</strong> são religiões tanto quanto o islã.",
    "tip": "<strong>Como aplicar:</strong> ache a autoridade última invocada — Deus? povo? natureza? dados? — para identificar a 'religião'."
   },
   {
    "ic": "spiral",
    "t": "Religião × Espiritualidade",
    "b": "<strong>Religião</strong> é um acordo: dá <strong>respostas</strong> prontas e impõe ordem. <strong>Espiritualidade</strong> é uma viagem: persegue as grandes <strong>perguntas</strong> sem aceitar respostas dadas. São opostas, não sinônimas.",
    "tip": "<strong>Para refletir:</strong> o buscador espiritual costuma ser inimigo da religião estabelecida — ele questiona; ela ordena."
   },
   {
    "ic": "scale",
    "t": "Poder × Sentido",
    "b": "A ciência responde 'o que é e como funciona'; a religião, 'o que devemos fazer'. Ética não se deduz de fatos — por isso o <strong>casal não se separa</strong>: poder sem sentido é cego; sentido sem poder é impotente.",
    "tip": "<strong>Modelo mental:</strong> saber <em>como</em> fazer algo nunca diz <em>se você deve</em> — esse vácuo é preenchido por uma religião."
   }
  ]
 },
 "ch06-o-pacto-moderno": {
  "cards": [
   {
    "ic": "scale",
    "t": "O Pacto: Poder × Sentido",
    "b": "Renunciamos a um plano cósmico que dava significado ao sofrimento; em troca, ganhamos poder crescente para reduzi-lo e adiar a morte. Trocamos <strong>consolo</strong> por <strong>controle</strong>.",
    "tip": "<strong>Modelo mental:</strong> toda promessa moderna entrega poder, não sentido — cobrar sentido do poder é erro de categoria."
   },
   {
    "ic": "constellation",
    "t": "Universo Sem Roteiro",
    "b": "A ciência não acha propósito embutido no cosmos. Sem roteirista, <strong>nada tem sentido dado</strong> — o que é assustador e, ao mesmo tempo, <strong>libertador</strong>: se nada é prescrito, tudo é possível.",
    "tip": "<strong>Para refletir:</strong> a mesma ausência de roteiro que angustia é a que autoriza a nova agenda (imortalidade etc.)."
   },
   {
    "ic": "spark",
    "t": "Crescimento como Religião",
    "b": "Para sustentar a ordem no vazio de sentido, elege-se o <strong>crescimento econômico perpétuo</strong> como valor supremo — fé no futuro que justifica dívida e consumo. Mas é a <strong>bomba-relógio ecológica</strong>: crescimento infinito × planeta finito.",
    "tip": "<strong>Modelo mental:</strong> recessão assusta tanto porque falha a <em>cola</em>, não só o dinheiro."
   }
  ]
 },
 "ch07-a-revolucao-humanista": {
  "cards": [
   {
    "ic": "person",
    "t": "Deus → Humano",
    "b": "Antes o sentido vinha de fora (escrituras). O humanismo declara que ele <strong>brota de dentro do humano</strong>: 'o cliente tem razão', 'siga seu coração', 'beleza está nos olhos de quem vê'. O ser humano vira a <strong>autoridade última</strong>.",
    "tip": "<strong>Como aplicar:</strong> mesmo discursos ateus assumem que a experiência humana dá valor — isso também é uma fé."
   },
   {
    "ic": "fork",
    "t": "Os Três Ramos",
    "b": "<strong>Liberal</strong>: cada indivíduo é único e soberano. <strong>Socialista</strong>: a verdade está na experiência <em>coletiva</em>. <strong>Evolutivo</strong>: algumas experiências/seres valem mais — a raiz do nazismo.",
    "tip": "<strong>Modelo mental:</strong> para localizar a fé de uma ideologia, ache onde ela ancora o sentido — no indivíduo, no coletivo ou na hierarquia."
   },
   {
    "ic": "sword",
    "t": "As Guerras de Religião",
    "b": "Liberalismo × comunismo × fascismo não foram só disputas políticas: foram um <strong>cisma humanista</strong> sobre <em>qual</em> humano tem autoridade. O <strong>liberalismo venceu</strong> — mas sobre um alicerce (indivíduo, livre-arbítrio) que a ciência vai abalar.",
    "tip": "<strong>Para refletir:</strong> o humanismo não é neutro nem óbvio — é uma religião datada, com dogmas."
   }
  ]
 },
 "ch08-a-bomba-relogio-no-laboratorio": {
  "cards": [
   {
    "ic": "gap",
    "t": "As Três Premissas Caem",
    "b": "'Sou um <strong>indivíduo</strong>' → você é divisível (um 'dividual'). 'Tenho <strong>livre-arbítrio</strong>' → desejos são bioquímicos e induzíveis de fora. 'Eu <strong>me conheço</strong> melhor que ninguém' → algoritmos já te preveem melhor que você.",
    "tip": "<strong>Modelo mental:</strong> separe 'o que desejo' de 'eu não escolhi desejar isso' — aí desaba a ilusão do livre-arbítrio."
   },
   {
    "ic": "eye",
    "t": "A Autoridade Migra",
    "b": "Enquanto ninguém te conhecia por dentro, 'ouça seu coração' era bom conselho. Quando um algoritmo te conhece melhor que você, a autoridade — antes em Deus, depois no indivíduo — <strong>migra para o algoritmo</strong>.",
    "tip": "<strong>Pergunta-chave:</strong> se o sistema me conhece melhor que eu, a quem pertence a decisão? Vigilância importa menos que autoridade."
   },
   {
    "ic": "clock",
    "t": "Por Que é Bomba-Relógio",
    "b": "Leis, política e economia ainda rodam sobre 'o eleitor/consumidor soberano que sabe o que quer'. Quando a premissa cai de vez, instituições ficam <strong>sem chão</strong> — mas o efeito é lento, daí o relógio.",
    "tip": "<strong>Para refletir:</strong> defender a liberdade só contra o Estado, ignorando quem detém os dados, é mirar a ameaça errada."
   }
  ]
 },
 "ch09-a-grande-desconexao-e-dataismo": {
  "cards": [
   {
    "ic": "gap",
    "t": "A Grande Desconexão",
    "b": "Sempre só seres conscientes eram inteligentes, por isso valorizamos a consciência. A IA é <strong>muito inteligente e nada consciente</strong> — e a economia só precisa da inteligência. A consciência vira <strong>economicamente supérflua</strong>.",
    "tip": "<strong>Como aplicar:</strong> a tarefa exige <em>sentir</em> (consciência) ou só <em>processar</em> (inteligência)? A segunda é automatizável."
   },
   {
    "ic": "layers",
    "t": "Classe Inútil × Super-Humanos",
    "b": "Quando algoritmos superam humanos em tarefa após tarefa, multidões não serão exploradas — serão <strong>dispensáveis</strong> ('classe inútil'). Em paralelo, a elite que detém dados e bioengenharia se aprimora numa <strong>desigualdade biológica</strong> entre 'espécies' de humanos.",
    "tip": "<strong>Para refletir:</strong> o perigo real não é a IA que se rebela, é a IA sem consciência que te torna dispensável."
   },
   {
    "ic": "key",
    "t": "O Dataísmo",
    "b": "A nova religião: o universo é <strong>fluxo de dados</strong>, o valor de tudo é sua contribuição ao processamento, o mandamento é <strong>conectar tudo</strong>. Ele destrona o humanismo: o homem deixa de ser a fonte de sentido (Deus → humano → <strong>dados</strong>) e vira um chip talvez obsoleto.",
    "tip": "<strong>Modelo mental:</strong> 'só vale se virar dado compartilhado' transfere ao fluxo a autoridade que o humanismo dava a você."
   }
  ]
 }
}
```
