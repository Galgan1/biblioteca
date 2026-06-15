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

# LIVRO PARA APROFUNDAR: Os 7 Hábitos das Pessoas Altamente Eficazes — Stephen R. Covey

**Subtítulo:** VISÃO GERAL · A EFETIVIDADE BASEADA EM CARÁTER
**Ideia central:** A efetividade verdadeira não vem de técnicas de imagem — vem do caráter, construído de dentro para fora sobre princípios. Mudamos antes os paradigmas (os mapas com que lemos o mundo); só então mudam os comportamentos. Os 7 hábitos movem a pessoa pelo continuum da maturidade: da dependência → à independência → à interdependência.

## Capítulos (contexto — mantenha estes slugs e títulos)
- `ch01-de-dentro-para-fora` — CAPÍTULO 1: De Dentro para Fora
- `ch02-visao-geral-dos-habitos` — CAPÍTULO 2: Visão Geral dos 7 Hábitos
- `ch03-habito1-ser-proativo` — CAPÍTULO 3: Hábito 1 — Ser Proativo
- `ch04-habito2-fim-em-mente` — CAPÍTULO 4: Hábito 2 — Começar com o Fim em Mente
- `ch05-habito3-primeiro-o-importante` — CAPÍTULO 5: Hábito 3 — Primeiro o Mais Importante
- `ch06-paradigmas-da-interdependencia` — CAPÍTULO 6: Paradigmas da Interdependência
- `ch07-habito4-ganha-ganha` — CAPÍTULO 7: Hábito 4 — Pensar Ganha-Ganha
- `ch08-habito5-compreender` — CAPÍTULO 8: Hábito 5 — Compreender, depois ser Compreendido
- `ch09-habito6-sinergia-e-habito7-renovacao` — CAPÍTULO 9: Hábitos 6 e 7 — Sinergia e Afinar o Instrumento

## ESQUELETO (aprofunde os corpos; devolva no FORMATO DE SAÍDA da skill)

```json
{
 "ch01-de-dentro-para-fora": {
  "cards": [
   {
    "ic": "leaf",
    "t": "Caráter × Personalidade",
    "b": "A <strong>ética do caráter</strong> (integridade, justiça, serviço) é o alicerce; a <strong>ética da personalidade</strong> (técnicas, atitude, imagem) é verniz que falha sozinho. Trabalhe a raiz (quem você é), não a folhagem.",
    "tip": "<strong>Como aplicar:</strong> quando 'consertos rápidos' não sustentam o resultado, suspeite que falta caráter, não técnica."
   },
   {
    "ic": "eye",
    "t": "Paradigmas",
    "b": "Um <strong>paradigma</strong> é o mapa mental com que você interpreta a realidade: 'vemos o mundo não como ele é, mas como nós somos'. A <strong>mudança de paradigma</strong> reorganiza todo o comportamento de uma vez.",
    "tip": "<strong>Modelo mental:</strong> trate o mapa como mapa, não como o território — se o resultado destoa, revise o paradigma."
   },
   {
    "ic": "mountain",
    "t": "Princípios e a Lei da Colheita",
    "b": "<strong>Princípios</strong> são leis naturais do comportamento (como a gravidade) — não mudam nem admitem atalho. A <strong>lei da colheita</strong>: colhe-se o que se planta; a fazenda não aceita 'encheção' de véspera.",
    "tip": "<strong>Para refletir:</strong> pare de buscar atalhos num sistema natural — caráter e confiança se cultivam, não se forçam."
   }
  ]
 },
 "ch02-visao-geral-dos-habitos": {
  "cards": [
   {
    "ic": "constellation",
    "t": "O que é um Hábito",
    "b": "Hábito é a interseção de <strong>conhecimento</strong> (o quê/porquê), <strong>habilidade</strong> (como) e <strong>desejo</strong> (querer). Falta qualquer um, não há hábito.",
    "tip": "<strong>Como aplicar:</strong> para instalar um hábito, supra os três; para diagnosticar a falha, descubra qual está faltando."
   },
   {
    "ic": "steps",
    "t": "Continuum da Maturidade",
    "b": "<strong>Dependência → independência → interdependência.</strong> Hábitos 1–3 = Vitória Privada (autodomínio); 4–6 = Vitória Pública (com os outros); o 7 renova o todo.",
    "tip": "<strong>Regra:</strong> a independência é etapa, não meta — a interdependência é a maturidade mais alta."
   },
   {
    "ic": "scale",
    "t": "P/CP — Efetividade Equilibrada",
    "b": "A fábula da galinha dos ovos de ouro: <strong>P</strong> é o resultado (o ovo), <strong>CP</strong> é a capacidade de produzir (a galinha). Matar a galinha por ganância acaba com os dois.",
    "tip": "<strong>Modelo mental:</strong> trate toda relação e todo recurso como 'galinha' — cuide do CP para não perder o P amanhã."
   }
  ]
 },
 "ch03-habito1-ser-proativo": {
  "cards": [
   {
    "ic": "gap",
    "t": "Espaço Estímulo → Resposta",
    "b": "Você não é determinado pelo que acontece, mas pela sua <strong>resposta</strong> a isso. Nesse espaço habitam os dons humanos: autoconsciência, imaginação, consciência moral e vontade independente.",
    "tip": "<strong>Modelo mental:</strong> você não controla o estímulo, controla a resposta — sempre há escolha."
   },
   {
    "ic": "target",
    "t": "Influência × Preocupação",
    "b": "O <strong>Círculo de Preocupação</strong> é tudo que te importa (inclusive o incontrolável); o <strong>Círculo de Influência</strong> é o que você pode afetar. Proativos focam o de Influência — e ele cresce.",
    "tip": "<strong>Como aplicar:</strong> classifique seu problema — está no Círculo de Influência (aja) ou só no de Preocupação (solte)?"
   },
   {
    "ic": "bubble",
    "t": "Linguagem Proativa",
    "b": "A linguagem revela e reforça o paradigma. Troque '<strong>não posso</strong>', '<strong>tenho que</strong>', 'ele me deixa furioso' por '<strong>escolho</strong>', '<strong>prefiro</strong>', 'controlo minha reação'.",
    "tip": "<strong>Para refletir:</strong> responsabilidade é 'response-ability' — a habilidade de escolher a resposta."
   }
  ]
 },
 "ch04-habito2-fim-em-mente": {
  "cards": [
   {
    "ic": "target",
    "t": "As Duas Criações",
    "b": "<strong>1ª criação</strong> = mental (visão, plano); <strong>2ª criação</strong> = física (execução). Se você não faz conscientemente a primeira, outros — ou as circunstâncias — a fazem por você.",
    "tip": "<strong>Modelo mental:</strong> antes de agir, projete o resultado final; sem destino, qualquer caminho serve e nenhum satisfaz."
   },
   {
    "ic": "book",
    "t": "Missão Pessoal & Liderança",
    "b": "<strong>Liderança</strong> ('subo a escada certa?') vem antes da <strong>gestão</strong> ('subo com eficiência?'). A <strong>declaração de missão pessoal</strong> é sua constituição: o que ser, o que fazer e os princípios que regem.",
    "tip": "<strong>Como aplicar:</strong> imagine o próprio funeral — o que quer que digam de você revela seus valores finais."
   },
   {
    "ic": "pin",
    "t": "Centros de Vida",
    "b": "Você organiza tudo em torno de um centro — cônjuge, trabalho, dinheiro, prazer, eu... Cada um distorce. O único estável é o <strong>centro em princípios</strong> (segurança, orientação, sabedoria e poder constantes).",
    "tip": "<strong>Para refletir:</strong> centros instáveis (aprovação, posses) fazem sua segurança oscilar com o que está fora do seu controle."
   }
  ]
 },
 "ch05-habito3-primeiro-o-importante": {
  "cards": [
   {
    "ic": "clock",
    "t": "Matriz do Tempo",
    "b": "Quatro quadrantes por urgente × importante: <strong>QI</strong> crises · <strong>QII</strong> importante & não urgente (prevenção, relações, planejar) · <strong>QIII</strong> urgente & não importante (interrupções) · <strong>QIV</strong> desperdício.",
    "tip": "<strong>Regra:</strong> more no Quadrante II — investir nele hoje encolhe as crises (QI) de amanhã."
   },
   {
    "ic": "mountain",
    "t": "As Pedras Grandes",
    "b": "Planeje a <strong>semana</strong> (não o dia) por <strong>papéis e metas</strong>: escolha 1–2 metas QII por papel e <strong>agende-as primeiro</strong>. Se você não puser as pedras grandes no balde, o trivial ocupa tudo.",
    "tip": "<strong>Como aplicar:</strong> ponha as prioridades primeiro; o cascalho e a areia se ajeitam nos vãos."
   },
   {
    "ic": "key",
    "t": "Dizer Não & Delegar",
    "b": "Priorizar o importante exige <strong>dizer não</strong> (com sorriso) ao urgente-não-importante. Delegue por <strong>resultados acordados</strong>, não por métodos — delegação por gestão multiplica P e CP.",
    "tip": "<strong>Para refletir:</strong> microgerenciar 'faça exatamente assim' mata iniciativa e sobrecarrega você."
   }
  ]
 },
 "ch06-paradigmas-da-interdependencia": {
  "cards": [
   {
    "ic": "scale",
    "t": "Conta Bancária Emocional",
    "b": "Metáfora do nível de confiança numa relação. <strong>Saldo alto</strong> = comunicação fácil e erros tolerados; <strong>saldo baixo</strong> = cada palavra vira atrito. Faça depósitos antes de precisar sacar.",
    "tip": "<strong>Como aplicar:</strong> antes de cobrar ou criticar (sacar), cheque o saldo — talvez falte depositar primeiro."
   },
   {
    "ic": "link",
    "t": "Os 6 Grandes Depósitos",
    "b": "<strong>Compreender o outro</strong> · atenção às <strong>pequenas coisas</strong> · <strong>cumprir compromissos</strong> · <strong>esclarecer expectativas</strong> · <strong>integridade</strong> (lealdade aos ausentes) · <strong>pedir desculpas</strong> sinceras.",
    "tip": "<strong>Modelo mental:</strong> pequenas grosserias são grandes saques; quebrar promessa é o maior saque de todos."
   },
   {
    "ic": "person",
    "t": "P/CP nas Relações",
    "b": "A confiança é o <strong>ativo (CP)</strong> que torna possível qualquer resultado conjunto (P). Numa relação humana, o 'rápido' é devagar — atalhos quebram a conta.",
    "tip": "<strong>Para refletir:</strong> construa a ponte antes de precisar atravessá-la; deposite confiança em tempos de paz."
   }
  ]
 },
 "ch07-habito4-ganha-ganha": {
  "cards": [
   {
    "ic": "fork",
    "t": "Os 6 Paradigmas",
    "b": "<strong>Ganha-ganha</strong> (ideal) · ganha-perde (competir) · perde-ganha (capacho) · perde-perde (vingança) · ganha (só eu) · <strong>ganha-ganha ou nada</strong> (sem acordo bom para ambos, concorda-se em não fechar).",
    "tip": "<strong>Como aplicar:</strong> ter 'ganha-ganha ou nada' como saída real tira a pressão de manipular."
   },
   {
    "ic": "leaf",
    "t": "Mentalidade de Abundância",
    "b": "A <strong>abundância</strong> vê o bolo como expansível e se alegra com o sucesso alheio; a <strong>escassez</strong> vê recurso fixo (o ganho do outro é minha perda). Ganha-ganha exige abundância.",
    "tip": "<strong>Modelo mental:</strong> o sucesso do outro não rouba o seu — pense no bolo como expansível."
   },
   {
    "ic": "scale",
    "t": "Maturidade & Acordos",
    "b": "<strong>Maturidade = coragem + consideração</strong>: dizer o que penso respeitando o outro. Sem coragem → perde-ganha; sem consideração → ganha-perde. E alinhe os <strong>sistemas</strong> para recompensar o ganha-ganha.",
    "tip": "<strong>Para refletir:</strong> ganha-ganha morre se o sistema de incentivos premia ganha-perde."
   }
  ]
 },
 "ch08-habito5-compreender": {
  "cards": [
   {
    "ic": "eye",
    "t": "Escuta Empática",
    "b": "Ouvir com a intenção de <strong>compreender</strong> (emocional e intelectualmente), entrando no quadro de referência do outro — não ouvir para concordar, refutar ou aconselhar. Reflita conteúdo <em>e</em> sentimento.",
    "tip": "<strong>Como aplicar:</strong> 'Você está frustrado porque...' — só ofereça solução depois do 'isso mesmo'."
   },
   {
    "ic": "lens",
    "t": "Diagnosticar antes de Prescrever",
    "b": "Como o bom médico ou o óptico, entenda o problema antes de oferecer sua receita. <strong>Prescrever sem diagnóstico destrói a confiança.</strong> Evite as 4 respostas autobiográficas.",
    "tip": "<strong>Modelo mental:</strong> os 4 vícios da escuta — avaliar, sondar, aconselhar, interpretar (tudo pelo seu ponto de vista)."
   },
   {
    "ic": "bubble",
    "t": "Ethos · Pathos · Logos",
    "b": "Para ser compreendido, nessa ordem: seu <strong>caráter</strong> (ethos), a <strong>empatia</strong> com o outro (pathos) e só então a <strong>lógica</strong> do argumento (logos).",
    "tip": "<strong>Para refletir:</strong> depois de ouvir, exponha suas ideias com clareza e coragem — pathos antes de logos."
   }
  ]
 },
 "ch09-habito6-sinergia-e-habito7-renovacao": {
  "cards": [
   {
    "ic": "constellation",
    "t": "Sinergia & 3ª Alternativa",
    "b": "O todo é maior que a soma: <strong>1+1 = 3</strong> ou mais. Diante de posições incompatíveis, valorize a diferença e busque a <strong>Terceira Alternativa</strong> — nem a sua, nem a do outro, mas uma melhor que ambas.",
    "tip": "<strong>Como aplicar:</strong> compromisso é 1+1 = 1,5 (ambos cedem); sinergia cria algo novo que satisfaz a todos."
   },
   {
    "ic": "spark",
    "t": "Valorizar as Diferenças",
    "b": "A essência da sinergia: 'se duas pessoas pensam igual, uma é desnecessária'. A diferença é a <strong>oportunidade</strong>, não a ameaça. A comunicação sobe de defensiva → respeitosa → <strong>sinérgica</strong>.",
    "tip": "<strong>Para refletir:</strong> pergunte 'topa procurar uma solução melhor que as nossas duas?' antes de transigir."
   },
   {
    "ic": "spiral",
    "t": "Afinar o Instrumento",
    "b": "Renovação nas <strong>4 dimensões</strong>: física, mental, espiritual e social/emocional. Como o lenhador que para para <strong>afiar o machado</strong>, é puro CP — e faz os 7 hábitos subirem numa <strong>espiral ascendente</strong>.",
    "tip": "<strong>Modelo mental:</strong> trate o Hábito 7 como atividade QII inegociável — sem renovação, os outros 6 se desgastam."
   }
  ]
 }
}
```
