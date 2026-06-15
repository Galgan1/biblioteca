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

# LIVRO PARA APROFUNDAR: Amor Líquido — Zygmunt Bauman

**Subtítulo:** VISÃO GERAL · SOBRE A FRAGILIDADE DOS LAÇOS HUMANOS
**Ideia central:** Na modernidade líquida, o amor foi refeito à imagem do consumo: parceiros viram produtos, relacionamentos viraram conexões, e a saída fácil tornou-se o principal atrativo do vínculo. Bauman mostra como a mesma fragilidade que dissolve o casal opera em escala global — do mercado de afetos ao campo de refugiados.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-apaixonar-se-e-desapaixonar-se` — CAPÍTULO 1: Apaixonar-se e Desapaixonar-se
- `ch02-caixa-de-ferramentas-da-sociabilidade` — CAPÍTULO 2: A Caixa de Ferramentas da Sociabilidade
- `ch03-sobre-a-dificuldade-de-amar-o-proximo` — CAPÍTULO 3: Sobre a Dificuldade de Amar o Próximo
- `ch04-convivio-destruido` — CAPÍTULO 4: Convívio Destruído

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-apaixonar-se-e-desapaixonar-se": {
  "cards": [
   {
    "ic": "wave",
    "t": "Amor Líquido",
    "b": "Vínculo afetivo da modernidade líquida: <strong>frágil, fluido e de baixo compromisso</strong>. Começa intenso e se dissolve rápido. A cláusula tácita de toda relação líquida: <em>até segunda ordem</em> — revogável sem aviso.",
    "tip": "<strong>Como aplicar:</strong> trace o vínculo contra os 3 traços do consumo — aquisição fácil, satisfação imediata, descartabilidade."
   },
   {
    "ic": "mask",
    "t": "O Parceiro-Produto",
    "b": "Amar como comprar: o outro é avaliado pela 'relação custo-benefício'. O <strong>desejo</strong> (consumir o objeto) se disfarça de <strong>amor</strong> (cuidar do outro). Quando exige trabalho, descarta-se — e nunca se aprende a amar.",
    "tip": "<strong>Para refletir:</strong> aplicativo de relacionamento = cardápio, não laço; o botão de deletar já vem embutido."
   },
   {
    "ic": "gap",
    "t": "Conexão × Relação",
    "b": "A palavra mudou porque a coisa mudou. 'Conexão' promete <strong>ligar e desligar à vontade</strong>, sem dívida. O <em>laço</em> supõe obrigação e duração; a <em>conexão</em> é cabo reversível.",
    "tip": "<strong>Modelo mental:</strong> note o vocabulário — quem fala em 'conexões' e 'contatos' está pensando em rede, não em vínculo."
   },
   {
    "ic": "scale",
    "t": "Segurança × Liberdade",
    "b": "O dilema de todo laço: segurança e liberdade são <strong>inseparáveis e antagônicas</strong>. A 'semivida' — meia-relação a meio-gás — é a tentativa impossível de ter as duas sem pagar o preço de nenhuma.",
    "tip": "<strong>Para refletir:</strong> 'quero compromisso mas tenho medo de me prender' não é defeito pessoal — é o dilema estrutural do laço."
   }
  ]
 },
 "ch02-caixa-de-ferramentas-da-sociabilidade": {
  "cards": [
   {
    "ic": "link",
    "t": "Rede × Laço",
    "b": "O <strong>laço</strong> (bond) supõe obrigação mútua e duração. A <strong>rede</strong> (network) é matriz de conexões igualmente fáceis de fazer e desfazer. Pertencer a uma rede não é estar ligado; é estar 'no ar'.",
    "tip": "<strong>Como aplicar:</strong> conte as saídas — muitas saídas baratas = rede; saída custosa = laço."
   },
   {
    "ic": "eye",
    "t": "Proximidade Virtual × Física",
    "b": "A comunicação à distância, sempre disponível e com botão de desligar, <strong>desvaloriza o encontro presencial</strong> — lento, exigente, sem mute. O celular permite estar sempre conectado e nunca preso.",
    "tip": "<strong>Para refletir:</strong> 'estou sempre em contato' + sensação de solidão = conexão como anestésico, não como companhia."
   },
   {
    "ic": "bubble",
    "t": "Comunicar ≠ Estar Junto",
    "b": "Acumular conexões não preenche a solidão — <strong>adia sem curar</strong>. A rede atrofia o músculo do encontro real: fácil demais não exercita. Muita comunicação pode ser o disfarce mais eficiente da solidão.",
    "tip": "<strong>Modelo mental:</strong> pense na rede como cardápio de conexões — cada amizade é item que se pede ou cancela."
   }
  ]
 },
 "ch03-sobre-a-dificuldade-de-amar-o-proximo": {
  "cards": [
   {
    "ic": "person",
    "t": "Amar o Próximo",
    "b": "O preceito de Freud: é o mais antinatural dos mandamentos — exige amar quem não é igual nem útil. Por isso é o <strong>ato fundador da civilização</strong>: o salto que cria o laço onde o instinto não o criaria. Na cidade, o próximo é o estranho.",
    "tip": "<strong>Modelo mental:</strong> amar o próximo é decisão moral, não simpatia espontânea."
   },
   {
    "ic": "triangle",
    "t": "Mixofobia × Mixofilia",
    "b": "<strong>Mixofobia</strong>: medo de misturar-se; produz muros, condomínios, segregação. <strong>Mixofilia</strong>: prazer de conviver com a diferença. As duas pulsões coabitam em cada pessoa e em cada cidade.",
    "tip": "<strong>Regra:</strong> mais muros geram mais medo — a segregação realimenta a insegurança que diz combater."
   },
   {
    "ic": "mountain",
    "t": "O Ciclo Mixofóbico",
    "b": "O condomínio fechado promete paz e entrega <strong>medo crescente</strong> do que ficou de fora. Quanto mais alto o muro, mais assustador o estranho — a 'segurança' comprada é combustível da insegurança. A saída mixofílica: a praça, a rua misturada, a civilidade.",
    "tip": "<strong>Para refletir:</strong> o estranho se torna ameaça quando nunca se convive com ele — e só se convive sem muro."
   }
  ]
 },
 "ch04-convivio-destruido": {
  "cards": [
   {
    "ic": "layers",
    "t": "Humanos Refugados",
    "b": "A modernização produz pessoas 'a mais', sem lugar — <strong>subproduto regular, não exceção</strong>. O refugiado é o estranho radical: não pode ser assimilado nem expulso, fica 'estocado' no não-lugar. A descartabilidade do parceiro-produto aplicada a populações inteiras.",
    "tip": "<strong>Modelo mental:</strong> o refugiado como espelho ampliado do amor líquido — descarte em escala global."
   },
   {
    "ic": "pin",
    "t": "Transitoriedade Permanente",
    "b": "O campo de refugiados como '<strong>lugar-nenhum</strong>' (nowhereville): extraterritorial, fora do tempo, num 'estar de passagem' que nunca termina. Não é anomalia — é ensaio do padrão líquido que se generaliza: precariedade sem fim.",
    "tip": "<strong>Para refletir:</strong> 'é só passagem' que dura anos é a transitoriedade permanente como destino."
   },
   {
    "ic": "wave",
    "t": "Globalização Negativa",
    "b": "A integração de <strong>fluxos</strong> (capital, mercadorias, informação) <strong>sem a integração das responsabilidades</strong>. Gera vítimas globais sem proteção global. A saída — solidariedade e política da humanidade comum — exige o amor mais difícil numa era de desapego.",
    "tip": "<strong>Modelo mental:</strong> fluxos globalizados, responsabilidades locais — a fórmula que produz o convívio desmantelado."
   }
  ]
 }
}
```
