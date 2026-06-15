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

# LIVRO PARA APROFUNDAR: Ponerologia Política — Andrzej Łobaczewski

**Subtítulo:** VISÃO GERAL · A CIÊNCIA DA GÊNESE DO MAL
**Ideia central:** Psiquiatra sob um regime totalitário, Łobaczewski propôs estudar o mal social como um fenômeno com causas observáveis — para que pessoas normais aprendessem a reconhecê-lo e resistir. É uma obra de diagnóstico e imunização: descreve como uma minoria patológica captura movimentos e Estados (ponerogênese), e como a maioria saudável pode interromper o processo. Lente defensiva, jamais um manual.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-ciencia-do-mal` — CAPÍTULO 1: A Ciência do Mal
- `ch02-psicopatia-essencial` — CAPÍTULO 2: A Psicopatia Essencial
- `ch03-caracteropatias` — CAPÍTULO 3: Caracteropatias e Esquizoidia
- `ch04-spellbinders-paramoralismos` — CAPÍTULO 4: Spellbinders e Paramoralismos
- `ch05-ponerogenese` — CAPÍTULO 5: Ponerogênese
- `ch06-associacoes-ponerogenicas` — CAPÍTULO 6: As Associações Ponerogênicas
- `ch07-mascara-ideologica` — CAPÍTULO 7: A Máscara Ideológica
- `ch08-pathocracia` — CAPÍTULO 8: A Pathocracia
- `ch09-ciclo-histeroidal` — CAPÍTULO 9: O Ciclo Histeroidal
- `ch10-defesa-imunizacao` — CAPÍTULO 10: A Defesa — Reconhecer e Resistir

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-ciencia-do-mal": {
  "cards": [
   {
    "ic": "eye",
    "t": "Ponerologia",
    "b": "O estudo interdisciplinar da <strong>gênese do mal</strong> macrossocial (psiquiatria + psicologia + sociologia + história). Pressuposto: se o mal se espalha por processos, eles podem ser descritos.",
    "tip": "<strong>Como aplicar:</strong> o que tem causa tem prevenção."
   },
   {
    "ic": "scale",
    "t": "Clínico, não moralista",
    "b": "Descrever o mecanismo sem se perder na indignação — porque só o entendimento frio permite a <strong>defesa eficaz</strong>.",
    "tip": "<strong>Modelo mental:</strong> indignar-se não basta; é preciso diagnosticar."
   },
   {
    "ic": "gap",
    "t": "Usar a lente para atacar",
    "b": "Rotular adversários de 'psicopatas' é <strong>abuso do conceito</strong> — a ponerologia é diagnóstico clínico, não xingamento político.",
    "tip": "<strong>Cuidado:</strong> personalizar o mal num único vilão ignora o processo que o produziu."
   }
  ]
 },
 "ch02-psicopatia-essencial": {
  "cards": [
   {
    "ic": "key",
    "t": "O núcleo sem freio moral",
    "b": "A <strong>psicopatia essencial</strong> (hereditária, na tese) — quem não experimenta culpa nem empatia e vê esses sentimentos nos outros como <strong>fraquezas a explorar</strong>.",
    "tip": "<strong>Como aplicar:</strong> poucos, mas catalisadores — agem onde a maioria hesita."
   },
   {
    "ic": "eye",
    "t": "A assimetria de compreensão",
    "b": "O normal <strong>não imagina</strong> uma mente sem consciência e projeta seus sentimentos sobre o psicopata, subestimando-o. O psicopata estuda o normal para manipulá-lo.",
    "tip": "<strong>Modelo mental:</strong> você projeta sua consciência onde ela não existe."
   },
   {
    "ic": "gap",
    "t": "Diagnóstico amador como arma",
    "b": "Rotular qualquer pessoa difícil de 'psicopata' <strong>banaliza</strong> o conceito e o torna injusto. É categoria clínica, não insulto.",
    "tip": "<strong>Cuidado:</strong> confundir frieza e ousadia com força de caráter — e segui-las."
   }
  ]
 },
 "ch03-caracteropatias": {
  "cards": [
   {
    "ic": "steps",
    "t": "Caracteropatia",
    "b": "Alteração de caráter de <strong>origem adquirida</strong> (lesão, trauma) que, numa posição formadora (educador, autoridade), <strong>transmite o padrão</strong> a muitos — o dano se propaga por gerações.",
    "tip": "<strong>Como aplicar:</strong> o desvio na cadeira certa contamina a sala inteira."
   },
   {
    "ic": "pivot",
    "t": "A posição amplifica o dano",
    "b": "O mesmo desvio é inofensivo num isolado e <strong>devastador</strong> num líder. Caracteropatas pavimentam o terreno que a psicopatia essencial explora.",
    "tip": "<strong>Modelo mental:</strong> o risco é proporcional à influência da posição."
   },
   {
    "ic": "gap",
    "t": "Doença não é maldade",
    "b": "Muitos caracteropatas são <strong>vítimas de dano</strong> — o foco é conter a influência com humanidade, não punir a condição.",
    "tip": "<strong>Cuidado:</strong> nem toda visão dura da natureza humana é patologia — evite o rótulo abusivo."
   }
  ]
 },
 "ch04-spellbinders-paramoralismos": {
  "cards": [
   {
    "ic": "mask",
    "t": "O spellbinder",
    "b": "O agitador carismático e patológico que <strong>hipnotiza</strong> com uma narrativa simples e total. Oferece certeza e um inimigo — e exige adesão, não exame.",
    "tip": "<strong>Como aplicar:</strong> quem te oferece certeza total cobra a tua capacidade de julgar."
   },
   {
    "ic": "fork",
    "t": "Paramoralismo",
    "b": "Um argumento que <strong>veste a roupa da moral</strong> para servir ao imoral ('é justo trair pela causa'). Soa virtuoso; opera ao contrário.",
    "tip": "<strong>Modelo mental:</strong> desconfie da virtude que pede crueldade."
   },
   {
    "ic": "gap",
    "t": "Carisma não é patologia",
    "b": "Nem todo líder carismático é spellbinder. O marcador é a <strong>exigência de adesão acrítica + a inversão moral</strong>, não o magnetismo.",
    "tip": "<strong>Cuidado:</strong> a força da convicção não mede a correção da ideia."
   }
  ]
 },
 "ch05-ponerogenese": {
  "cards": [
   {
    "ic": "spiral",
    "t": "A cadeia causal",
    "b": "Terreno preparado → spellbinder + ideia mobilizadora → adesão emocional → infiltração do núcleo → <strong>inversão dos valores</strong> → expulsão dos normais.",
    "tip": "<strong>Como aplicar:</strong> o mal social é processo, não interruptor — cada estágio é chance de interromper."
   },
   {
    "ic": "pivot",
    "t": "A seleção negativa",
    "b": "Os mais escrupulosos saem ou são afastados; os menos escrupulosos sobem. O grupo se <strong>destila no sentido errado</strong>.",
    "tip": "<strong>Modelo mental:</strong> quando os íntegros saem e os cínicos sobem, o grupo já virou."
   },
   {
    "ic": "gap",
    "t": "Normalizar o pequeno passo",
    "b": "Cada concessão 'pontual' ('só desta vez') é um <strong>degrau da cadeia</strong>. Quem só reage no fim perdeu os pontos baratos de interrupção.",
    "tip": "<strong>Cuidado:</strong> nem todo conflito é ponerogênese — o marcador é inversão de valores + seleção negativa."
   }
  ]
 },
 "ch06-associacoes-ponerogenicas": {
  "cards": [
   {
    "ic": "layers",
    "t": "A dupla estrutura",
    "b": "Por fora, a hierarquia oficial e o discurso nobre; por dentro, uma <strong>rede informal de patológicos</strong> que detém o poder real e usa a fachada como camuflagem.",
    "tip": "<strong>Como aplicar:</strong> olhe quem decide, não quem discursa."
   },
   {
    "ic": "link",
    "t": "Coesão por medo",
    "b": "O grupo se une não por ideais, mas por <strong>medo mútuo</strong> (todos sabem demais uns dos outros) e cumplicidade no que já foi feito.",
    "tip": "<strong>Modelo mental:</strong> coesão por cumplicidade é prisão, não lealdade."
   },
   {
    "ic": "eye",
    "t": "Os 'úteis'",
    "b": "Membros normais e idealistas mantidos como mão de obra e <strong>escudo moral</strong> — muitas vezes sem perceber a quem servem.",
    "tip": "<strong>Cuidado:</strong> sigilo e hierarquia não são, por si, ponerogênese."
   }
  ]
 },
 "ch07-mascara-ideologica": {
  "cards": [
   {
    "ic": "mask",
    "t": "A ideologia como máscara",
    "b": "Uma doutrina atraente é adotada como <strong>fachada</strong>; o núcleo a esvazia de sentido e a usa como camuflagem moral e ímã de idealistas.",
    "tip": "<strong>Como aplicar:</strong> o problema não é a ideia, é sua instrumentalização."
   },
   {
    "ic": "scale",
    "t": "A divergência crescente",
    "b": "Quanto mais o grupo age contra os próprios princípios, mais <strong>insiste</strong> na ideologia — o discurso fica mais puro à medida que a prática fica mais suja.",
    "tip": "<strong>Modelo mental:</strong> a pureza do discurso pode medir a sujeira da prática."
   },
   {
    "ic": "gap",
    "t": "Defender pela bandeira",
    "b": "'Mas a causa é justa' é exatamente o <strong>escudo</strong> que protege o núcleo. Atacar a ideia sincera dos 'úteis' valida o enquadramento.",
    "tip": "<strong>Cuidado:</strong> doutrinas podem ser sinceras — o marcador é a distância discurso × prática."
   }
  ]
 },
 "ch08-pathocracia": {
  "cards": [
   {
    "ic": "sword",
    "t": "O governo dos patológicos",
    "b": "A minoria com desvios ocupa o centro do poder e usa a maioria como recurso. Sustenta-se por <strong>terror, vigilância, cooptação</strong> e a paralisia dos normais.",
    "tip": "<strong>Como aplicar:</strong> durar não é ser apoiado; é controlar."
   },
   {
    "ic": "layers",
    "t": "A inversão institucional",
    "b": "Justiça, imprensa, ciência mantêm o <strong>nome</strong> e invertem a <strong>função</strong> — servem ao núcleo, não ao público. A forma persiste; o conteúdo se esvaziou.",
    "tip": "<strong>Modelo mental:</strong> a forma sobrevive ao conteúdo."
   },
   {
    "ic": "gap",
    "t": "Frágil por dentro",
    "b": "Como contraria a maioria, gasta enorme energia em controle e promove por <strong>cumplicidade</strong> (a mediocridade sobe) — estruturalmente insustentável.",
    "tip": "<strong>Cuidado:</strong> banalizar o termo (todo governo ruim = 'pathocracia') destrói seu valor."
   }
  ]
 },
 "ch09-ciclo-histeroidal": {
  "cards": [
   {
    "ic": "clock",
    "t": "A guarda cai no conforto",
    "b": "Épocas 'boas' geram complacência e <strong>perda de rigor</strong>; épocas difíceis reimpõem realismo. A vulnerabilidade máxima coincide com a sensação máxima de segurança.",
    "tip": "<strong>Como aplicar:</strong> é a bonança, não a crise, que prepara o terreno do mal."
   },
   {
    "ic": "wave",
    "t": "A memória do sofrimento",
    "b": "As gerações que não viveram a catástrofe <strong>não a temem</strong> — e repetem os erros, porque a lição não foi sentida na pele.",
    "tip": "<strong>Modelo mental:</strong> lição não sentida não protege."
   },
   {
    "ic": "gap",
    "t": "Silenciar o alerta",
    "b": "Tratar quem aponta riscos como 'estraga-prazeres' <strong>remove o anticorpo</strong>. Nos bons tempos, premia-se quem agrada, não quem alerta.",
    "tip": "<strong>Cuidado:</strong> o ciclo é tendência, não destino — consciência e instituições o amortecem."
   }
  ]
 },
 "ch10-defesa-imunizacao": {
  "cards": [
   {
    "ic": "bulb",
    "t": "O conhecimento como imunidade",
    "b": "A vantagem do núcleo vem da <strong>ignorância da maioria</strong> sobre como ele opera. Nomear os mecanismos (spellbinder, paramoralismo, máscara) <strong>quebra o feitiço</strong>.",
    "tip": "<strong>Como aplicar:</strong> a luz é o antídoto — o que se vê não enfeitiça."
   },
   {
    "ic": "constellation",
    "t": "A maioria saudável",
    "b": "Os normais são a esmagadora maioria; a fraqueza não é número, é <strong>desorganização e autoengano</strong>. Consciência e coesão revertem a assimetria.",
    "tip": "<strong>Modelo mental:</strong> resistência serena, não histérica — a histeria é o terreno do mal."
   },
   {
    "ic": "key",
    "t": "Imunizar, não perseguir",
    "b": "Usar a ponerologia para caçar e desumanizar adversários é <strong>cair no próprio processo</strong> (paramoralismo: 'é justo ser cruel com os cruéis').",
    "tip": "<strong>Cuidado:</strong> sociedade que expurga 'inimigos internos' reproduz a doença que dizia combater."
   }
  ]
 }
}
```
