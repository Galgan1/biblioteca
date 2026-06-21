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

# LIVRO PARA APROFUNDAR: Nação Dopamina — Anna Lembke

**Subtítulo:** VISÃO GERAL · PRAZER, DOR E O EQUILÍBRIO
**Ideia central:** A psiquiatra Anna Lembke explica por que, num mundo de prazer ilimitado, estamos mais infelizes. A chave é uma balança: prazer e dor moram no mesmo lugar do cérebro e buscam o equilíbrio — todo prazer é pago com dor depois. Do excesso nasce o déficit de dopamina; a cura passa por abstinência, autovínculo e, surpreendentemente, pela busca deliberada da dor.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-balanca-prazer-dor` — CAPÍTULO 1: A Balança Prazer-Dor
- `ch02-dopamina-moeda` — CAPÍTULO 2: Dopamina — A Moeda do Vício
- `ch03-deficit-dopamina` — CAPÍTULO 3: O Déficit de Dopamina
- `ch04-era-da-indulgencia` — CAPÍTULO 4: A Era da Indulgência
- `ch05-jejum-de-dopamina` — CAPÍTULO 5: O Jejum de Dopamina
- `ch06-autovinculo` — CAPÍTULO 6: O Autovínculo
- `ch07-busca-pela-dor` — CAPÍTULO 7: A Busca pela Dor
- `ch08-honestidade-radical` — CAPÍTULO 8: A Honestidade Radical
- `ch09-vergonha-equilibrio` — CAPÍTULO 9: Vergonha Prossocial e o Equilíbrio

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-balanca-prazer-dor": {
  "cards": [
   {
    "ic": "scale",
    "t": "A balança e a homeostase",
    "b": "Prazer de um lado, dor do outro, no <strong>mesmo circuito</strong>. Após um pico de prazer, o cérebro empurra a balança para a dor com a mesma força — e <strong>passa do ponto</strong>.",
    "tip": "<strong>Como aplicar:</strong> não há almoço grátis — todo prazer é empréstimo pago em dor."
   },
   {
    "ic": "wave",
    "t": "O baixo após o alto",
    "b": "O déficit que vem depois do prazer (o anticlímax, a fissura, a ressaca) é a balança compensando — e é ele que <strong>pede a próxima dose</strong>.",
    "tip": "<strong>Modelo mental:</strong> o que sobe desce, e passa do nível."
   },
   {
    "ic": "gap",
    "t": "Perseguir só o alto",
    "b": "Buscar o pico ignorando a dor garantida que vem na sequência afunda a balança. Tratar a fissura como <strong>falha moral</strong> só aumenta a culpa.",
    "tip": "<strong>Cuidado:</strong> repor o baixo com outra dose afunda a balança ainda mais."
   }
  ]
 },
 "ch02-dopamina-moeda": {
  "cards": [
   {
    "ic": "target",
    "t": "Querer, não gostar",
    "b": "A dopamina impulsiona a <strong>perseguição</strong> da recompensa (o desejo), distinta do prazer de consumi-la. O vício sequestra o <strong>querer</strong> mesmo quando o gostar já sumiu.",
    "tip": "<strong>Como aplicar:</strong> o vício é o querer que sobrevive à morte do gostar."
   },
   {
    "ic": "spark",
    "t": "Velocidade é veneno",
    "b": "Não é só quanto, mas <strong>quão rápido</strong> a dopamina sobe. Picos altos e instantâneos são os mais perigosos. A mesma régua vale para drogas e comportamentos (telas, jogo, compras).",
    "tip": "<strong>Modelo mental:</strong> o perigo está no pico rápido, não só na quantidade."
   },
   {
    "ic": "gap",
    "t": "Caçar dopamina direto",
    "b": "Buscar a dopamina diretamente é perseguir o <strong>querer</strong>, que nunca se sacia. Confundi-la com felicidade leva à corrida sem fim.",
    "tip": "<strong>Cuidado:</strong> achar que só drogas viciam ignora que telas disparam a mesma moeda."
   }
  ]
 },
 "ch03-deficit-dopamina": {
  "cards": [
   {
    "ic": "spiral",
    "t": "Tolerância e gremlins",
    "b": "O uso repetido faz o lado da dor responder mais forte (tolerância). Os <strong>gremlins</strong> se acumulam no lado da dor e a <strong>linha de base afunda</strong>.",
    "tip": "<strong>Como aplicar:</strong> a mesma dose entrega cada vez menos — a tolerância sempre ganha."
   },
   {
    "ic": "eye",
    "t": "Anedonia",
    "b": "No déficit, <strong>nada dá prazer</strong> — nem o vício. Consome-se já não para sentir o alto, mas para <strong>escapar do baixo</strong>.",
    "tip": "<strong>Modelo mental:</strong> tolerância é o brilho do mundo apagando."
   },
   {
    "ic": "gap",
    "t": "Aumentar a dose",
    "b": "Repor o déficit com mais estímulo <strong>afunda a balança ainda mais</strong> — a espiral do vício.",
    "tip": "<strong>Cuidado:</strong> 'nada me dá prazer' às vezes é a balança em déficit pedindo abstinência."
   }
  ]
 },
 "ch04-era-da-indulgencia": {
  "cards": [
   {
    "ic": "link",
    "t": "Incompatibilidade evolutiva",
    "b": "O aparato que nos fazia perseguir recompensas <strong>raras</strong> agora é bombardeado por recompensas <strong>infinitas</strong>. O design que era vantagem virou armadilha.",
    "tip": "<strong>Como aplicar:</strong> cérebro de escassez, mundo de fartura — o descompasso, não a fraqueza, explica o vício."
   },
   {
    "ic": "pin",
    "t": "O smartphone-agulha",
    "b": "Lembke chama o celular de <strong>agulha hipodérmica moderna</strong> — dopamina rápida e variável, a qualquer hora. A <strong>recompensa variável</strong> é o padrão mais viciante.",
    "tip": "<strong>Modelo mental:</strong> conveniência é a isca; acesso fácil afunda a balança."
   },
   {
    "ic": "gap",
    "t": "A doença da abundância",
    "b": "Depressão e anedonia crescem nos países mais ricos — <strong>por excesso, não por falta</strong>. Buscar a cura em mais consumo afunda a balança.",
    "tip": "<strong>Cuidado:</strong> culpar só a força de vontade ignora que os produtos são desenhados para vencê-la."
   }
  ]
 },
 "ch05-jejum-de-dopamina": {
  "cards": [
   {
    "ic": "clock",
    "t": "A regra dos ~30 dias",
    "b": "É o tempo que o sistema de recompensa leva para se reajustar. Os <strong>primeiros dias são os piores</strong> (a balança ainda na dor); a melhora vem na 2ª metade.",
    "tip": "<strong>Como aplicar:</strong> o objetivo é devolver a sensibilidade ao prazer simples, não zerar a dopamina."
   },
   {
    "ic": "steps",
    "t": "O acrônimo DOPAMINE",
    "b": "<strong>D</strong>ados · <strong>O</strong>bjetivos · <strong>P</strong>roblemas · <strong>A</strong>bstinência · <strong>M</strong>indfulness · <strong>I</strong>nsight · <strong>N</strong>ext (próximos passos) · <strong>E</strong>xperimento.",
    "tip": "<strong>Modelo mental:</strong> a fissura é uma onda — observe-a sem obedecer; ela passa."
   },
   {
    "ic": "gap",
    "t": "Desistir cedo",
    "b": "Abandonar nos primeiros dias é justo quando a balança está <strong>mais na dor</strong> — e confirma o vício. Tentar moderar antes de abstinir reacende o ciclo.",
    "tip": "<strong>Cuidado:</strong> a piora inicial é o reajuste, não uma recaída do problema."
   }
  ]
 },
 "ch06-autovinculo": {
  "cards": [
   {
    "ic": "key",
    "t": "Os 3 tipos",
    "b": "<strong>Físico</strong> (distância: app fora do celular, gatilho fora de casa); <strong>cronológico</strong> (janelas de tempo: 'só após as 18h'); <strong>categórico</strong> (abstinência total da categoria).",
    "tip": "<strong>Como aplicar:</strong> decida com a mente fria — erga o muro antes da fissura chegar."
   },
   {
    "ic": "link",
    "t": "Ulisses e o mastro",
    "b": "Amarrar-se ao mastro antes de ouvir as sereias: <strong>proteger o eu futuro</strong> das escolhas do eu impulsivo. Não é resistir — é não precisar resistir.",
    "tip": "<strong>Modelo mental:</strong> a vontade é fraca; mude o ambiente, não confie na vontade."
   },
   {
    "ic": "gap",
    "t": "Barreira fraca",
    "b": "Se contornar é fácil (o app a um toque), <strong>não é autovínculo</strong>. Manter o gatilho à mão 'para testar o autocontrole' é alimentá-lo.",
    "tip": "<strong>Cuidado:</strong> na hora da fissura, a força de vontade quase sempre perde."
   }
  ]
 },
 "ch07-busca-pela-dor": {
  "cards": [
   {
    "ic": "pivot",
    "t": "Hormese",
    "b": "Doses <strong>pequenas e controladas</strong> de um estressor (dor) ativam a recuperação do corpo, que <strong>passa do ponto para o prazer</strong> — o rebote. O bem-estar vem depois, e dura.",
    "tip": "<strong>Como aplicar:</strong> a dor é a porta dos fundos do prazer — sem ressaca."
   },
   {
    "ic": "steps",
    "t": "A 'dor boa'",
    "b": "Exercício, banho frio, jejum, sauna, trabalho difícil — desconfortos auto-impostos que rebatem em <strong>energia, foco e humor</strong> e elevam a linha de base.",
    "tip": "<strong>Modelo mental:</strong> desconforto voluntário é antídoto do excesso."
   },
   {
    "ic": "gap",
    "t": "Exagerar a dose",
    "b": "Hormese vira <strong>lesão</strong> se o estressor for grande demais. Buscar a dor pela dor (masoquismo) erra o alvo — o objetivo é o rebote saudável.",
    "tip": "<strong>Cuidado:</strong> o ganho vem no rebote; quem desiste durante a dor não colhe o depois."
   }
  ]
 },
 "ch08-honestidade-radical": {
  "cards": [
   {
    "ic": "eye",
    "t": "A verdade como reguladora",
    "b": "Relatar honestamente o que se fez (mesmo o vergonhoso) cria <strong>responsabilização</strong> e ativa circuitos de conexão — ajudando a equilibrar a balança.",
    "tip": "<strong>Como aplicar:</strong> a verdade dói na hora e cura depois; a mentira alivia na hora e adoece depois."
   },
   {
    "ic": "link",
    "t": "Autoria, não vítima",
    "b": "Contar a própria história com <strong>responsabilidade pelos próprios atos</strong> cura mais do que a narrativa de vítima passiva. A vulnerabilidade honesta restaura o vínculo.",
    "tip": "<strong>Modelo mental:</strong> esconder é estar sozinho — e o isolamento alimenta o vício."
   },
   {
    "ic": "gap",
    "t": "A narrativa de vítima",
    "b": "Terceirizar a culpa ('foi tudo culpa de X') mantém a <strong>passividade</strong> que impede a recuperação. Confessar para impressionar não cura.",
    "tip": "<strong>Cuidado:</strong> 'ser brutalmente honesto' com os outros não é desculpa para a crueldade."
   }
  ]
 },
 "ch09-vergonha-equilibrio": {
  "cards": [
   {
    "ic": "pivot",
    "t": "As duas vergonhas",
    "b": "A <strong>destrutiva</strong> diz 'eu sou ruim' → isola, esconde, usa mais. A <strong>prossocial</strong> diz 'fiz algo ruim, mas pertenço a um grupo que me ajuda' → repara e reconecta.",
    "tip": "<strong>Como aplicar:</strong> 'eu fiz algo ruim' cura; 'eu sou ruim' afunda."
   },
   {
    "ic": "scale",
    "t": "O equilíbrio",
    "b": "A meta final: buscar prazer com <strong>consciência da dor</strong> que ele cobra, e buscar dor com consciência do prazer que devolve. Não abstinência eterna — uma <strong>balança administrada</strong>.",
    "tip": "<strong>Modelo mental:</strong> o alvo é o nível, não o pico."
   },
   {
    "ic": "gap",
    "t": "Afogar a vergonha",
    "b": "A vergonha destrutiva <strong>pede o próprio veneno</strong> que a criou. Isolar-se na culpa torna a vergonha destrutiva por padrão.",
    "tip": "<strong>Cuidado:</strong> regras claras + comunidade transformam a vergonha em combustível de mudança."
   }
  ]
 }
}
```
