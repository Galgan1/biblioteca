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

# LIVRO PARA APROFUNDAR: A Metamorfose — Franz Kafka

**Subtítulo:** VISÃO GERAL · DIE VERWANDLUNG (1915)
**Ideia central:** Gregor Samsa acorda transformado num inseto monstruoso — e sua primeira aflição não é o corpo, mas perder o trem para o trabalho. Kafka literaliza a alienação: o provedor-máquina vira bicho, e a família, que vivia dele, revive na exata medida em que ele definha. Uma novela sobre o absurdo aceito sem explicação, o corpo contra a identidade, e os laços que duram só enquanto somos úteis.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `parte01-a-transformacao-e-o-trabalho` — PARTE I: A Transformação e o Trabalho
- `parte02-adaptacao-e-a-maca` — PARTE II: Adaptação e a Maçã
- `parte03-declinio-morte-e-renascimento` — PARTE III: Declínio, Morte e Renascimento

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "parte01-a-transformacao-e-o-trabalho": {
  "cards": [
   {
    "ic": "book",
    "t": "O Absurdo Sem Explicação",
    "b": "A metamorfose é dada na primeira frase — sem causa, diagnóstico ou tentativa de cura. O leitor (e o próprio Gregor) trata o impossível como <strong>problema logístico</strong>: o trem perdido, o chefe à porta.",
    "tip": "<strong>Como aplicar:</strong> note quando um sistema absorve o absurdo como rotina — esse é o efeito kafkiano."
   },
   {
    "ic": "layers",
    "t": "O Provedor-Máquina",
    "b": "Gregor sustenta pai, mãe e irmã e vive em função do dever, não de si. O emprego de caixeiro-viajante é um cárcere: viagens sem fim, contatos passageiros, medo do patrão. <strong>Sua identidade está soldada ao papel de provedor.</strong>",
    "tip": "<strong>Para refletir:</strong> sem a função, o lugar dele na família evapora."
   },
   {
    "ic": "eye",
    "t": "A Engrenagem Burocrática",
    "b": "Ao primeiro atraso, o gerente da firma aparece <em>em pessoa</em> — a suspeita corporativa é instantânea. O indivíduo é sempre menor que o sistema impessoal que o cerca.",
    "tip": "<strong>Modelo mental:</strong> o gerente é a voz do sistema; foge horrorizado e sela a perda do emprego."
   },
   {
    "ic": "gap",
    "t": "A Porta e a Primeira Ferida",
    "b": "Gregor abre a porta com as mandíbulas e se mostra; o pânico é geral. O pai o empurra de volta ao quarto com bengala e jornal, <strong>ferindo-o no vão da porta</strong> — primeira ferida de uma série. A porta vira a medida da exclusão.",
    "tip": "<strong>Símbolo:</strong> a porta é a fronteira entre o humano (a sala) e o exilado (o quarto)."
   }
  ]
 },
 "parte02-adaptacao-e-a-maca": {
  "cards": [
   {
    "ic": "person",
    "t": "Corpo × Humanidade",
    "b": "Gregor adquire hábitos de bicho (rasteja pelas paredes, prefere comida estragada), mas conserva memória, afeto e vergonha. <strong>Por dentro, segue humano; por fora, é repugnante.</strong> A consciência resiste enquanto o corpo a trai.",
    "tip": "<strong>Para refletir:</strong> o que define o humano — a aparência que os outros veem ou a consciência que ninguém alcança?"
   },
   {
    "ic": "scale",
    "t": "A Inversão Começa",
    "b": "Cada membro da família reassume uma função produtiva. O pai renasce como autoridade fardada e vigorosa; a mãe costura; Grete cuida do quarto. <strong>Gregor, antes o eixo, vira peso morto.</strong>",
    "tip": "<strong>Modelo mental:</strong> a energia vital é uma só e migra — da família para Gregor (antes), de Gregor para a família (agora)."
   },
   {
    "ic": "mask",
    "t": "Os Móveis e o Retrato",
    "b": "Mãe e Grete tentam esvaziar o quarto para Gregor rastejar — sem ver que arrancam dele os <strong>últimos vestígios do humano</strong>. Ele se lança sobre o retrato da dama de peles e o cobre com o corpo: não deixará que o levem.",
    "tip": "<strong>Símbolo:</strong> esvaziar o quarto = transformá-lo em jaula nua, apagar o homem que Gregor foi."
   },
   {
    "ic": "spark",
    "t": "A Maçã Encravada",
    "b": "O pai chega do trabalho, interpreta a cena como ataque e bombardeia Gregor com maçãs. Uma se crava nas costas com tal força que <strong>ali permanece, apodrecendo na carne</strong> — a ferida que nunca cicatriza e inicia o declínio.",
    "tip": "<strong>Leitura:</strong> a maçã = violência paterna petrificada + punição edípica + eco da maçã bíblica (pecado e queda)."
   }
  ]
 },
 "parte03-declinio-morte-e-renascimento": {
  "cards": [
   {
    "ic": "leaf",
    "t": "A Arte como Último Laço",
    "b": "Ao ouvir Grete tocar violino, Gregor é tomado de emoção e se arrasta para a sala, fascinado, sentindo que a música o chama de volta ao humano. <strong>A alma resiste no corpo de bicho</strong> — e é justamente isso que o condena.",
    "tip": "<strong>Símbolo:</strong> o violino é a ponte para a humanidade perdida; o momento de quase-redenção que precipita o fim."
   },
   {
    "ic": "triangle",
    "t": "Da Compaixão à Sentença",
    "b": "Grete, antes cuidadora, completa o arco de menina a mulher e a juíza: declara que <strong>aquela criatura já não é Gregor e tem de sumir</strong>. Gregor escuta cada palavra — e, sem revolta, lhe dá razão.",
    "tip": "<strong>Para refletir:</strong> a frase de Grete mata Gregor mais que a maçã; o afeto vira repúdio."
   },
   {
    "ic": "wave",
    "t": "A Morte como Alívio",
    "b": "Esvaziado, ferido e faminto, Gregor recolhe-se ao quarto e morre ao amanhecer, ainda pensando na família com ternura. A faxineira acha o corpo seco e o descarta. <strong>A reação dos Samsa não é luto, mas alívio.</strong>",
    "tip": "<strong>Leitura:</strong> a morte é a única saída do absurdo; Gregor a aceita — e nisso há uma estranha dignidade."
   },
   {
    "ic": "mountain",
    "t": "O Renascimento dos Vivos",
    "b": "Libertos, os Samsa despedem os hóspedes e saem num passeio de bonde ao campo. Ao sol, os pais notam que <strong>Grete desabrochou numa bela jovem</strong> em idade de casar. A vida segue, indiferente ao morto.",
    "tip": "<strong>Ironia final:</strong> a obra fecha não no luto, mas no futuro — Kafka nega a Gregor qualquer redenção dos vivos."
   }
  ]
 }
}
```
