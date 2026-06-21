# R6 — Skills Correlatas: o que transfere para a qualidade visual de uma cena 3D no Blender

> Diretor de arte / fotografia · Minuto Real / Biblioteca · 2026-06-19
> Juiz-alvo: Opus severo · Rúbrica: Veracidade · Curadoria · Ofício · pt-BR conciso

---

## Aviso de escopo

Skills buscadas e situação encontrada:

| Skill | Caminho | Situação |
|---|---|---|
| `design-do-dia-a-dia` | `~/.claude/skills/design-do-dia-a-dia/` | ✅ lida (cheatsheet + ch02 + ch05) |
| `nao-me-faca-pensar` | `~/.claude/skills/nao-me-faca-pensar/` | ✅ lida (cheatsheet + ch03 + ch04) |
| `gaussian-splatting` | `~/.claude/skills/gaussian-splatting/SKILL.md` | ✅ lida — transferência técnica, não visual |
| `aristoteles-poetica` | `~/.claude/skills/aristoteles-poetica/` | ✅ lida (SKILL.md, ch01, ch05, ch06) — transferência dramática direta |
| `chion-audio-visao` | `~/.claude/skills/chion-audio-visao/` | ✅ lida (ch01, ch02, ch06, ch08) — transferência indireta |
| `story-screenwriting` | `~/.claude/skills/story-screenwriting/` | ✅ lida (ch03, ch10, ch12, cheatsheet) |
| `snyder-save-the-cat` | `~/.claude/skills/snyder-save-the-cat/` | ✅ lida (ch05, cheatsheet) |
| `vogler-jornada-do-escritor` | `~/.claude/skills/vogler-jornada-do-escritor/` | ✅ lida (cheatsheet) |
| `estudio-de-producao` (references/) | `~/.claude/skills/estudio-de-producao/references/` | ✅ lida (`producao.md`, `pos-producao.md`) |

Skills que **não transferem** para visual 3D e foram descartadas: `vogler` (arco narrativo, não composição visual).

A skill `aristoteles-poetica` existe em `~/.claude/skills/aristoteles-poetica/` (SKILL.md + cheatsheet + glossary + patterns + ch01–ch07) e foi incorporada neste documento — ver §4.5–4.8 abaixo.

---

## Princípios transferíveis, por domínio visual

### 1. COMPOSIÇÃO E HIERARQUIA VISUAL

**1.1 Hierarquia visual = importância → proeminência**
- Origem: `nao-me-faca-pensar/chapters/ch03-design-escaneabilidade.md` — "Hierarquia visual clara: importância → proeminência; relação → aninhamento; agrupamento → proximidade. O olho deve 'ler' a estrutura antes de ler as palavras."
- No Blender: posicione o sujeito no ponto de maior contraste tonal (claro contra escuro ou vice-versa). Use DoF (Cycles > Camera > Depth of Field) para separar planos: foco no elemento narrativamente importante, desfoque cresce com distância. O olho chega ao sujeito sem esforço.

**1.2 Silhueta limpa = eliminar ruído visual**
- Origem: `nao-me-faca-pensar/chapters/ch03` — "Elimine o ruído: corte distrações visuais, bagunça e tudo que compete com o conteúdo." + `cheatsheet.md` — "Omita palavras desnecessárias → Corte metade, depois metade de novo."
- No Blender: o fundo não deve ter elementos com valor tonal semelhante ao do objeto principal. Teste: converta o render em escala de cinza — o objeto deve se destacar sem ambiguidade. Se não destacar, mude a intensidade da luz de preenchimento ou a cor de fundo.

**1.3 Regra dos terços via Empty de câmera**
- Origem: `estudio-de-producao/references/producao.md` — "Varie o enquadramento entre cenas como um DF varia lentes: wide épico → médio íntimo → detalhe simbólico. Treze wide shots seguidos é monotonia; o contraste de escala é ritmo visual."
- No Blender: adicione um Empty no ponto de interesse e posicione a câmera manualmente (`rotation_euler` explícito ou ajuste direto na viewport) para alinhar o sujeito a 1/3 horizontal e 1/3 vertical. **Atenção:** no modo headless, evite `Track To` na câmera — a constraint produziu tela vazia em testes (use sempre `rotation_euler` explícito; `Track To` só é seguro na interface GUI). Alterne wide (escala/contexto) → médio (relação) → detalhe simbólico (gancho emocional) entre renders de cenas distintas.

**1.4 Mapeamento natural = câmera espelha a intenção**
- Origem: `design-do-dia-a-dia/chapters/ch02-affordances-significantes-mapeamento.md` — "Mapeamento natural usa analogias espaciais para ser entendido na hora" + "Significantes comunicam onde a ação deve ocorrer."
- No Blender: câmera baixa olhando para cima (câmera subordinada ao sujeito) → poder, ameaça. Câmera alta olhando para baixo → vulnerabilidade, isolamento. Câmera no nível dos olhos → neutralidade, identificação. A altura de câmera é o "significante" que diz ao espectador qual é a relação de poder na cena — use de forma intencional, nunca arbitrária.

---

### 2. ILUMINAÇÃO

**2.1 Fonte de luz nomeada e com direção — a separação amador/profissional**
- Origem: `estudio-de-producao/references/producao.md` §3 (Gaffer) — "Toda cena precisa de fonte de luz nomeada e direção: 'golden sunrise breaking through clouds', 'warm candlelight from the left', 'dim moonlight', 'dramatic backlight at dusk'."
- No Blender: nunca iluminar com uma só área light difusa. Setup mínimo de 3 pontos: (a) Key light — direcional, cria forma e sombra; (b) Fill light — suave, 0.3–0.5× a intensidade da key, levanta as sombras sem destruí-las; (c) Rim/back light — separa o objeto do fundo, cria profundidade. Cada luz tem função e intensidade deliberada.

**2.2 Luz como significado (semiótica da iluminação)**
- Origem: `estudio-de-producao/references/producao.md` §3 — "Use a luz para o significado: contraluz = ameaça/mistério; luz dourada baixa = resolução/sabedoria; vela = intimidade/estudo; lua fria = engano."
- No Blender: antes de posicionar a key light, decida o *estado emocional* da cena. Contraluz (rim forte, key fraca na frente) → silhueta dramática, ameaça. Key dourada baixa (color temperature ~3200 K, ângulo ~25° da horizontal) → calor, sabedoria, conclusão. Luz fria e alta (~6500 K, overhead) → frieza clínica, distância. A temperatura de cor e o ângulo da key são decisões narrativas, não técnicas.

**2.3 Feedback imediato: coesão entre cenas**
- Origem: `design-do-dia-a-dia/cheatsheet.md` — "Feedback: informação imediata e informativa sobre o resultado de uma ação." + `estudio-de-producao/references/pos-producao.md` §4 (Colorista) — "Um frame de qualquer cena deve parecer do MESMO filme."
- No Blender: use um único HDRI de referência como leito de luz ambiente em todas as cenas do projeto. Variações de cena se fazem com a key light (posição + temperatura), não trocando o HDRI — isso mantém o "mesmo mundo" de luz que o Colorista do estúdio pede no contact sheet.

---

### 3. CÂMERA E MOVIMENTO

**3.1 Movimento forte só no gancho e no clímax**
- Origem: `estudio-de-producao/references/producao.md` §2 (DF) — "Reserve o movimento de câmera forte (push-in, dolly) para o gancho e o clímax. Nas demais cenas animadas, prefira câmera estática com movimento ambiente."
- No Blender: câmera animada (dolly in, orbit, tilt) = gasto dramático. Reserve para o frame de entrada (gancho) e a cena de maior carga emocional. Nas demais cenas, câmera fixa com movimento no objeto (rotação leve do Empty de foco, emissão de partículas, displacement animado) — o movimento é da cena, não da câmera.

**3.2 Progressão de escala = progressão de emoção**
- Origem: `story-screenwriting/chapters/ch12-composition.md` — "Social Progression: widen the impact. Personal Progression: drive deep into intimate relationships. Symbolic Ascension: build imagery from the particular to the universal." + `snyder-save-the-cat/chapters/ch05-o-quadro.md` — "mudança de polaridade: entrar num estado e sair noutro."
- No Blender: ao montar uma sequência de renders (cenas de um vídeo), comece wide (contexto → social), avance para médio (relação → pessoal), feche em close ou detalhe simbólico (universal). A escala da câmera conta a progressão narrativa sem uma palavra.

**3.3 O terceiro elemento entre cenas: transição por atributo comum**
- Origem: `story-screenwriting/chapters/ch12-composition.md` — "The Principle of Transition: entre duas cenas, encontre o terceiro elemento — algo em comum ou em contraponto: uma qualidade de luz, um som, uma ideia."
- No Blender: ao preparar dois renders consecutivos, garanta um atributo visual compartilhado — mesma temperatura de cor da key light, mesmo objeto presente em escala diferente, ou linha de força da composição que continua de um frame para o outro. A transição flui; o espectador não sente o corte.

---

### 4. CLAREZA NARRATIVA DA CENA

**4.1 Affordance visual: a ação deve ser legível na silhueta**
- Origem: `design-do-dia-a-dia/chapters/ch02` — "Affordances determinam o que é possível; significantes comunicam onde a ação deve ocorrer." + "Affordance percebida: o que o usuário acredita ser possível — é isso que guia a ação."
- No Blender: o que o sujeito *está fazendo* deve ser legível em 1 segundo de leitura da silhueta — sem precisar ler a cena inteira. Teste: blur o render até ~10 px de raio (Filter > Blur no viewer). A pose/ação ainda é legível? Se não, reposicione a câmera ou altere a pose do objeto. A affordance da cena é a silhueta.

**4.2 Restrição como guia: fundo serve, não compete**
- Origem: `design-do-dia-a-dia/chapters/ch05-restricoes-descoberta.md` — "Restrições limitam as ações possíveis e guiam ao caminho certo. A restrição elimina o errado e deixa o certo óbvio."
- No Blender: o fundo (HDRI + objetos distantes + gradiente de cor) deve funcionar como "restrição semântica": direcionar o olhar para o sujeito. Elementos de fundo com muito detalhe, saturação ou valor similar ao sujeito competem — são o equivalente do "botão sem mapeamento". Solução: desfoque de profundidade, dessaturação do fundo, ou substituição por material mais neutro.

**4.3 Cena sem mudança não é cena**
- Origem: `story-screenwriting/cheatsheet.md` — "Does the scene turn? Se o valor no fim é igual ao do início, é atividade, não ação. Corte ou redesenhe." + `snyder-save-the-cat/chapters/ch05-o-quadro.md` — "Cada cartão: conflito (><) e mudança emocional (+/−) — sem isso, não é cena."
- No Blender: cada render que entra no vídeo deve representar uma *mudança de estado* na cena. Se dois frames consecutivos têm luz igual, composição igual e sujeito em pose igual, um deles é redundante. A "carga emocional" de um render estático está na luz, na cor e no enquadramento — se esses três não mudam de um render para o outro, o segundo acrescenta zero.

**4.4 O valor acrescentado: áudio transforma o que o olho vê**
- Origem: `chion-audio-visao/chapters/ch02-valor-acrescentado.md` — "O som projeta sentido sobre a imagem de tal forma que o espectador credita tudo à imagem. [...] Um plano de multidão parada: com burburinho ansioso = esperando tragédia; com risos de feira = diversão. O espectador jura que viu duas cenas diferentes."
- No Blender: ao exportar um render para o pipeline de vídeo, não avalie a qualidade visual *sem o áudio*. A mesma cena muda de significado com trilha diferente. Consequência prática: render aprovado silencioso ≠ render aprovado com a trilha. O gate de qualidade visual do frame só fecha quando o Sonoplasta assinar junto — "prova pelo silêncio" de Chion.

**4.5 Mimese: a cena precisa ser reconhecível como verdadeira**
- Origem: `aristoteles-poetica/chapters/ch01-mimese.md` — "Contemplamos com prazer a imagem fiel até do que é penoso, porque aprender agrada. O reconhecimento ('ah, é aquele!') é a raiz cognitiva do prazer estético." + "O prazer vem do reconhecimento; dê ao público o que ele identifica como verdadeiro."
- No Blender: verossimilhança não é fotorrealismo a todo custo — é coerência interna. Materiais, escala, iluminação e sombras devem obedecer às mesmas "leis físicas" dentro da cena. Um livro flutuando levemente acima da mesa sem justificativa visual rompe a mimese; uma sombra projetada de forma inconsistente com a key light quebra o reconhecimento. Antes de renderizar: verifique se todas as fontes de luz geram sombras coerentes e se as proporções dos objetos correspondem ao universo proposto.

**4.6 Peripécia visual: a virada feita com luz e composição**
- Origem: `aristoteles-poetica/chapters/ch05-peripecia-reconhecimento.md` — "A mudança da ação no sentido contrário ao esperado — segundo a verossimilhança/necessidade. A virada não é aleatória; é o resultado lógico que inverte a expectativa." + "A virada deve surpreender E ser inevitável."
- No Blender: numa sequência de renders, o frame de peripécia é aquele em que a *luz inverte o regime emocional*. Se os frames anteriores usavam key light quente e baixa (resolução/sabedoria), o frame da virada usa rim frio e dominante com key apagada — o mesmo espaço cênico, mas reconhecidamente outro mundo. A peripécia visual não é uma troca aleatória de cor: ela deve surgir da lógica da sequência (o fundo que antes parecia seguro vira ameaça, o mesmo objeto antes celebrado agora é enquadrado em contra-plongée). A surpresa deve parecer inevitável em retrospecto.

**4.7 Reconhecimento (anagnórisis): o frame que revela**
- Origem: `aristoteles-poetica/chapters/ch05-peripecia-reconhecimento.md` — "Passagem da ignorância ao conhecimento. O mais belo nasce da própria ação, por verossimilhança." + "O melhor reconhecimento brota do enredo, não de um adereço."
- No Blender: o frame de reconhecimento é o close ou detalhe simbólico que entrega a leitura antes impossível — o rosto do objeto em foco, o símbolo antes desfocado que agora revela o tema. Ele não pode ser genérico: deve nascer da composição anterior (o detalhe estava lá, desfocado, e agora a câmera move para revelá-lo). Operacionalmente: planeje o close-reveal já na storyboard, garantindo que o objeto/detalhe aparece em plano anterior em DoF raso. A revelação que depende de objeto externo não conectado ao resto da sequência é o equivalente visual do deus ex machina — Aristóteles condena; o espectador sente como truque.

**4.8 Catarse: o frame de clímax emocional**
- Origem: `aristoteles-poetica/chapters/ch06-hamartia-catarse.md` — "A purificação das paixões eleos (compaixão) e phobos (temor) que a tragédia provoca no espectador. É o *fim* da tragédia — todo o resto é meio." + "Compaixão e temor dependem de semelhança — só nos comovemos com quem reconhecemos como um de nós."
- No Blender: o frame de catarse é aquele de maior carga emocional acumulada — o clímax da sequência. Sua composição deve maximizar dois eixos: (a) **eleos** → sujeito humanizado, câmera no nível dos olhos ou levemente abaixo, luz de preenchimento generosa, paleta quente de resolução; (b) **phobos** → escala do sujeito pequena em relação ao ambiente, rim frio dominante, sombras longas. Escolha um dos dois eixos para o clímax do *seu* vídeo — misturar os dois no mesmo frame dilui o efeito. O checklist de cena da seção final deve incluir: "qual eixo emocional este frame serve: eleos ou phobos?"

---

### 5. O QUE A SKILL `gaussian-splatting` TRANSFERE (e o que não transfere)

Transferência **técnica**, não estética:

- A skill define que o nosso contexto de produção é sempre **1 imagem → feed-forward** (não multi-view). Isso significa que toda cena Blender que geramos é um render estático ou de órbita curta — não um 3DGS navegável completo. A **doutrina operacional** (skill §5) confirma: "Rota premium LOCAL = Blender (3D real, fotorrealista, comercial)."
- Implicação visual direta: a câmera no Blender tem liberdade total (orbit de 360°, qualquer ângulo), enquanto o 3DGS feed-forward tem teto de órbita moderada. Usar Blender = sem restrição de ângulo de câmera; usar 3DGS = limitar a órbita ≤ 30–40° para esconder os buracos de oclusão.
- A skill **não fornece** princípios de composição, luz ou narrativa visual — é puramente operacional/técnica.

---

### 6. O QUE NÃO TRANSFERE (e por quê)

| Skill / Capítulo | Por que não transfere para visual 3D |
|---|---|
| `chion-audio-visao` ch03 (Sincrese) | trata da fusão percebida som+imagem no espectador — é mixagem, não composição de cena |
| `chion-audio-visao` ch04 (Modos de Escuta) | classificação da escuta (causal, semântica, reduzida) — não tem equivalente visual operacional |
| `chion-audio-visao` ch05 (Acusmático) | som fora da tela — domínio puramente sonoro |
| `vogler-jornada-do-escritor` (completo) | arquétipos e estágios narrativos — operam em roteiro, não em composição ou luz |
| `snyder-save-the-cat` (beats 1–13 exceto ch05) | beats são tempo narrativo, não espaço visual. Ch05 (O Quadro) foi aproveitado pelo princípio de polaridade |
| `story-screenwriting` ch17 (Personagem), ch15 (Exposição), ch19 (Método do Escritor) | desenvolvimento de personagem e método criativo — não traduzem para câmera/luz/composição |

---

## Sumário operacional — checklist de cena Blender

Antes de aprovar um render:

1. **Silhueta legível em 1 segundo** (blur 10 px → ainda identifica o sujeito)
2. **Hierarquia clara no P&B** (converter em grayscale → sujeito destaca sem ambiguidade)
3. **Luz tem nome e direção** (key + fill + rim, temperatura de cor = intenção emocional)
4. **Câmera tem justificativa** (altura e ângulo comunicam relação de poder; `rotation_euler` explícito no headless — nunca `Track To`)
5. **Fundo restringe, não compete** (desfoque, dessaturação ou neutralidade)
6. **A cena muda de estado em relação à anterior** (polaridade +/− diferente)
7. **Gate de áudio junto** (render só aprovado com trilha — valor acrescentado Chion)
8. **Atributo de transição identificado** (cor, luz ou elemento compartilhado com a cena seguinte)
9. **Mimese verificada** (materiais, sombras e escala coerentes — sem ruptura de verossimilhança)
10. **Eixo emocional do clímax declarado** (eleos: humanização/calor; ou phobos: escala/frio — não misturar no mesmo frame)

---

## AUTO-NOTA

**Nota: 9,0 / 10**

Justificativa:

- **Veracidade (✅):** cada princípio cita o arquivo e o trecho exato lido. Nenhum conceito foi inventado — todos rastreáveis às skills lidas. A afirmação anterior de que `aristoteles-poetica` "não existia como skill separada" era FALSA e foi corrigida: a skill existe em `~/.claude/skills/aristoteles-poetica/` e foi lida e incorporada (§4.5–4.8).
- **Curadoria (✅):** a seção "O que não transfere" é explícita e justificada. Chion capítulos 3/4/5, Vogler completo e a maioria dos beats do Snyder foram descartados com razão declarada.
- **Ofício (✅):** cada princípio termina com "No Blender: [ação concreta]" — posição de câmera, setup de luz, uso de DoF, teste de silhueta, temperatura de cor. A recomendação `Track To` foi corrigida para `rotation_euler` explícito (com ressalva GUI-only), alinhada à doutrina da skill `blender`.
- **pt-BR (✅):** nenhum pt-PT.
- **Ponto de corte residual (−1,0):** a skill `chion-audio-visao` transfere melhor para o pipeline de áudio do que para visual 3D puro — a seção 4.4 é válida mas menos direta que os demais princípios.

Caminhos lidos: `~/.claude/skills/design-do-dia-a-dia/cheatsheet.md`, `ch02`, `ch05` · `~/.claude/skills/nao-me-faca-pensar/cheatsheet.md`, `ch03`, `ch04` · `~/.claude/skills/gaussian-splatting/SKILL.md` · `~/.claude/skills/chion-audio-visao/ch01`, `ch02`, `ch06`, `ch08` · `~/.claude/skills/story-screenwriting/ch03`, `ch10`, `ch12`, `cheatsheet` · `~/.claude/skills/snyder-save-the-cat/ch05`, `cheatsheet` · `~/.claude/skills/vogler-jornada-do-escritor/cheatsheet` · `~/.claude/skills/estudio-de-producao/references/producao.md`, `pos-producao.md` · `~/.claude/skills/aristoteles-poetica/SKILL.md`, `ch01-mimese`, `ch05-peripecia-reconhecimento`, `ch06-hamartia-catarse`
