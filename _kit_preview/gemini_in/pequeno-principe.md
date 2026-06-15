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

# LIVRO PARA APROFUNDAR: O Pequeno Príncipe — Antoine de Saint-Exupéry

**Subtítulo:** VISÃO GERAL · UMA FÁBULA SOBRE O QUE OS OLHOS NÃO VEEM
**Ideia central:** Um aviador cai no deserto e encontra um menino vindo de outro planeta. Da rosa que ele ama à raposa que lhe ensina a cativar, a fábula opõe o olhar da criança — que vê o essencial — à literalidade das 'pessoas grandes', obcecadas por números e 'coisas sérias'. A chave de tudo: o essencial é invisível aos olhos.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-o-chapeu-e-as-pessoas-grandes` — MOVIMENTO 1: O Chapéu e as Pessoas Grandes
- `ch02-o-planeta-do-principe-e-a-rosa` — MOVIMENTO 2: O Planeta do Príncipe e a Rosa
- `ch03-os-seis-planetas-e-as-pessoas-grandes` — MOVIMENTO 3: Os Seis Planetas
- `ch04-a-terra-a-serpente-e-o-jardim-de-rosas` — MOVIMENTO 4: A Terra, a Serpente e o Jardim de Rosas
- `ch05-a-raposa-e-o-segredo-de-cativar` — MOVIMENTO 5: A Raposa e o Segredo de Cativar
- `ch06-o-poco-e-o-essencial-invisivel` — MOVIMENTO 6: O Poço e o Essencial Invisível
- `ch07-a-partida-as-estrelas-que-riem` — MOVIMENTO 7: A Partida e as Estrelas que Riem

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-o-chapeu-e-as-pessoas-grandes": {
  "cards": [
   {
    "ic": "lens",
    "t": "O Chapéu ou a Jiboia?",
    "b": "O Desenho nº 1 testa quem vê além da superfície: as 'pessoas grandes' enxergam um chapéu; quem tem alma de criança vê a <strong>jiboia que engoliu um elefante</strong>. Ver só o chapéu é já ter se rendido ao mundo adulto.",
    "tip": "<strong>Modelo mental:</strong> a imaginação não é fuga do real — é o que permite ver o que está escondido nele."
   },
   {
    "ic": "person",
    "t": "As Pessoas Grandes",
    "b": "Os adultos só entendem <strong>números, negócios e 'coisas sérias'</strong>, e precisam que tudo lhes seja explicado. Cansado de não achar com quem falar do que importa, o aviador aprendeu a falar de bridge, golfe e política — e ficou só.",
    "tip": "<strong>Para refletir:</strong> crescer não obriga a perder o olhar; o aviador é a prova de que o adulto pode reaprender a ver."
   },
   {
    "ic": "bulb",
    "t": "O Carneiro na Caixa",
    "b": "Frustrado com os carneiros que desenha, o aviador rabisca uma simples <strong>caixa furada</strong> e diz: 'o carneiro está aí dentro'. O rosto do menino se ilumina. A imaginação completa o que o traço não mostra.",
    "tip": "<strong>Como aplicar:</strong> às vezes mostrar menos diz mais — a mente de quem olha preenche o essencial."
   }
  ]
 },
 "ch02-o-planeta-do-principe-e-a-rosa": {
  "cards": [
   {
    "ic": "leaf",
    "t": "A Rosa",
    "b": "Única no planeta, bela e vaidosa, a rosa cobra cuidados e mente por orgulho — mas ama. Símbolo do <strong>amor, da vaidade e da responsabilidade</strong> (inspirada em Consuelo, esposa do autor). O príncipe a serve, mas se cansa das vaidades e parte.",
    "tip": "<strong>Para refletir:</strong> devia tê-la julgado pelos atos, não pelas palavras — 'ela perfumava o meu planeta, e eu não soube amá-la'."
   },
   {
    "ic": "mountain",
    "t": "Os Baobás",
    "b": "Árvores-praga que rachariam o planeta se não fossem arrancadas <strong>ainda brotos</strong>. Metáfora dos vícios e das ideias ruins: vigiados cedo, sai fácil; deixados crescer, viram catástrofe.",
    "tip": "<strong>Como aplicar:</strong> corte o mal pela raiz — o hábito destrutivo é mais fácil de arrancar enquanto é pequeno."
   },
   {
    "ic": "target",
    "t": "Vulcões e Cuidado",
    "b": "O príncipe limpa seus vulcões e cuida do que é seu — as <strong>tarefas humildes de manter o próprio mundo</strong>. O cuidado cotidiano (regar, cobrir do vento, ouvir) é o que constrói o vínculo, mesmo antes de ele entender isso.",
    "tip": "<strong>Modelo mental:</strong> o laço se faz nos pequenos gestos, não nos grandes gestos."
   }
  ]
 },
 "ch03-os-seis-planetas-e-as-pessoas-grandes": {
  "cards": [
   {
    "ic": "cards",
    "t": "A Galeria dos Adultos",
    "b": "<strong>Rei</strong> (poder vazio, só ordena o que já aconteceria) · <strong>Vaidoso</strong> (só ouve elogios) · <strong>Bêbado</strong> (bebe para esquecer que bebe) · <strong>Homem de negócios</strong> (conta estrelas, não usa nenhuma) · <strong>Geógrafo</strong> (sabe tudo, nunca saiu da mesa).",
    "tip": "<strong>Como aplicar:</strong> cada planeta isola um vício que encolhe a vida a um único tema — e isola quem o cultiva."
   },
   {
    "ic": "bulb",
    "t": "O Acendedor de Lampiões",
    "b": "Acende e apaga o lampião sem parar, fiel a uma ordem que <strong>perdeu o sentido</strong> (o planeta gira rápido demais). É o único que o príncipe respeita: cuida de algo além de si — mas virou escravo da rotina.",
    "tip": "<strong>Para refletir:</strong> o dever é nobre quando serve a algo, trágico quando vira pura repetição."
   },
   {
    "ic": "key",
    "t": "A Pergunta 'Para Quê?'",
    "b": "A criança fura a lógica de cada adulto com uma só pergunta. Ao negociante que 'possui' estrelas: <strong>'para que te serve possuir estrelas?'</strong> — e ele não tem resposta. Útil é cuidar do que se ama; possuir por possuir é estéril.",
    "tip": "<strong>Modelo mental:</strong> 'para quê?' desmonta a seriedade que se levou a sério demais."
   }
  ]
 },
 "ch04-a-terra-a-serpente-e-o-jardim-de-rosas": {
  "cards": [
   {
    "ic": "spiral",
    "t": "A Serpente",
    "b": "Criatura enigmática do deserto, fala por charadas e promete devolver o príncipe à sua terra. <strong>Símbolo de morte e transição</strong> — 'mais poderosa que o dedo de um rei', mas que reconduz, não destrói.",
    "tip": "<strong>Para refletir:</strong> aqui a morte é lida como porta de volta, não como fim — uma releitura poética."
   },
   {
    "ic": "layers",
    "t": "O Jardim de Cinco Mil Rosas",
    "b": "Diante de mil flores idênticas à sua, o príncipe chora: pensava-se dono de uma rosa <strong>única no universo</strong> e tinha apenas uma rosa comum. A crença na singularidade desaba — falta-lhe ainda a chave que a raposa vai dar.",
    "tip": "<strong>Modelo mental:</strong> valor de um vínculo não se mede por raridade objetiva."
   },
   {
    "ic": "wave",
    "t": "Solidão em Meio à Multidão",
    "b": "A Terra grande não cura a solidão; pode aprofundá-la. 'O que torna o deserto belo é que ele <strong>esconde, em algum lugar, um poço</strong>' — o sentido está oculto, à espera de quem o procure com o coração.",
    "tip": "<strong>Para refletir:</strong> os maiores desertos da alma se abrem justamente no meio da multidão."
   }
  ]
 },
 "ch05-a-raposa-e-o-segredo-de-cativar": {
  "cards": [
   {
    "ic": "link",
    "t": "Cativar = Criar Laços",
    "b": "'Tu não és, para mim, senão um menino igual a cem mil. Mas, se me <strong>cativas</strong>, seremos únicos um para o outro.' Amor e amizade se constroem aproximando-se aos poucos, com tempo e paciência — não se acham prontos.",
    "tip": "<strong>Como aplicar:</strong> o laço se faz cativando — investindo presença, dia após dia."
   },
   {
    "ic": "clock",
    "t": "O Rito e o Trigo Dourado",
    "b": "Chegar sempre à mesma hora faz o coração se preparar desde antes: o <strong>rito</strong> cria a expectativa que é parte do amor. E o trigo, antes indiferente à raposa, passa a evocar os cabelos do amigo — o vínculo <strong>recolore o mundo</strong>.",
    "tip": "<strong>Modelo mental:</strong> o ritual não é detalhe — é o que prepara o coração e dá cor ao mundo."
   },
   {
    "ic": "eye",
    "t": "O Segredo",
    "b": "No adeus, a raposa revela: '<strong>o essencial é invisível aos olhos</strong>'. E completa: 'foi o tempo que perdeste com tua rosa que a fez tão importante… tu te tornas eternamente responsável por aquilo que cativas'.",
    "tip": "<strong>Para refletir:</strong> a singularidade do ser amado não vem da espécie, mas do laço investido nele."
   }
  ]
 },
 "ch06-o-poco-e-o-essencial-invisivel": {
  "cards": [
   {
    "ic": "key",
    "t": "A Água Como Presente",
    "b": "A água do poço faz bem ao coração porque <strong>nasceu da caminhada</strong>, da roldana, do esforço dos braços. 'Era boa como um presente.' O esforço investido é parte inseparável do valor — o que se conquista vale pelo caminho.",
    "tip": "<strong>Modelo mental:</strong> o que sacia a alma vem do laço e da busca, não do objeto isolado."
   },
   {
    "ic": "constellation",
    "t": "As Estrelas e a Flor",
    "b": "As estrelas são belas porque '<strong>em algum lugar há uma flor</strong>'. O céu inteiro se recolore pelo laço — eco do trigo da raposa. O que se ama transforma o modo como vemos tudo o mais.",
    "tip": "<strong>Para refletir:</strong> olhar com o coração transforma o deserto, a água e as estrelas."
   },
   {
    "ic": "person",
    "t": "A Amizade Consolidada",
    "b": "O aviador carrega o menino adormecido e sente que guarda 'um <strong>tesouro frágil</strong>'. Os dois agora estão cativados um pelo outro — é o respiro de plenitude antes do desfecho.",
    "tip": "<strong>Para refletir:</strong> é a criança que guia o adulto de volta ao essencial."
   }
  ]
 },
 "ch07-a-partida-as-estrelas-que-riem": {
  "cards": [
   {
    "ic": "leaf",
    "t": "Responsável pela Rosa",
    "b": "Faz um ano que caiu; ele precisa voltar, pois é <strong>responsável por sua rosa</strong>. O amor exige regressar para cuidar de quem se cativou — ainda que custe a vida. É o ápice ético da fábula.",
    "tip": "<strong>Para refletir:</strong> 'responsável por aquilo que cativas' se realiza aqui, no preço mais alto."
   },
   {
    "ic": "constellation",
    "t": "As Estrelas que Riem",
    "b": "O presente de despedida: como o príncipe estará rindo numa estrela, para o aviador <strong>todas as estrelas rirão</strong> — 'terás estrelas que sabem rir'. O riso do amigo, guardado no céu, transforma o luto em ternura.",
    "tip": "<strong>Modelo mental:</strong> quem amamos, ao partir, recolore o mundo — o céu inteiro ri por causa do laço."
   },
   {
    "ic": "spiral",
    "t": "O Retorno e a História Aberta",
    "b": "Ao anoitecer, perto da serpente, ele cai devagar, <strong>sem ruído</strong>, na areia — 'como cai uma árvore'. De manhã, o corpo não está lá. A morte é passagem, não horror. E o aviador ainda pergunta: o carneiro terá comido a flor?",
    "tip": "<strong>Para refletir:</strong> a história fica aberta de propósito — o luto convive com a esperança."
   }
  ]
 }
}
```
