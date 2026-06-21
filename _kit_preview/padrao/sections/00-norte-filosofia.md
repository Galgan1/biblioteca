## 00. Norte & Filosofia

> *A bíblia do padrão de imagem da rede Minuto Real / Biblioteca. Esta é a seção que abre o documento — o manifesto. As nove seções seguintes detalham o "como"; esta estabelece o "porquê" e a doutrina que governa todas as outras.*

---

### Por que este documento existe

Produzimos imagens para 92+ livros, em quatro frentes (feed e carrossel do Instagram, Stories, thumbnail do YouTube) e em ritmo de esteira. Sem uma regra única, cada peça vira uma decisão nova: outro verde, outra fonte, outro jeito de tratar o acento. O resultado seria um acervo que *parece* de marcas diferentes — e marca que não se reconhece não constrói equity.

A meta deste documento é uma só, e é mensurável: **uma peça nossa deve ser reconhecível em 0,5 segundo no feed**, antes de o olho ler uma palavra. O leitor passa o polegar, bate o olho, e *sabe* que é Minuto Real — pela cor, pela atmosfera, pelo acabamento. Essa coerência é o que separa um catálogo premium de uma pilha de posts.

A bíblia existe para tornar isso **automático e repetível**. Ela não é um moodboard inspiracional; é a fonte de verdade que alinha o gerador (`gerar_infografico.py`, `gerar_carrossel.py`), os tokens (`marca.py`) e o guardrail (`check_marca.py`). Quando a regra está escrita, a máquina executa e o humano só aprova.

---

### A alma que copiamos — e o arco-íris que não copiamos

A referência viva são os **infográficos densos de catálogo**: o "Guia rápido: fusíveis do carro", o "Tipos de fita e quando usar cada uma". O que admiramos neles não é o assunto — é a **densidade elegante**: muita informação organizada numa única imagem, sem virar bagunça. O DNA desse gênero é claro:

1. **Cabeçalho/título forte** que ancora a peça.
2. Uma **grade de itens**, cada um com um **objeto renderizado de verdade** (a "coisa", fotorrealista).
3. **Rótulo + descrição curta** por item.
4. Um bloco prático — **ícone + "USO:"**.
5. Um **rodapé de aviso** ("DICA" / "IMPORTANTE").
6. **Acabamento cinematográfico**: luz, profundidade, grão, vinheta.

Essa é a **alma**. Para nós, o "objeto" deixa de ser um fusível e passa a ser um **objeto-símbolo do livro**: coroa = poder, correntes = dependência, prisma = tática. Mas a estrutura — cabeçalho, grade, descrição, USO, rodapé, acabamento — é exatamente a que copiamos.

**O que NÃO copiamos é a paleta arco-íris.** As referências usam uma cor por categoria — vermelho, azul, amarelo, verde, tudo junto. Isso é morte para a marca: vira ruído, e nada se reconhece. Vestimos a mesma alma na **nossa** roupa:

> **Verde (hue 152) lidera. Um único ouro (hue 83, `#d8a64a`) é o acento. Mais nada.**

E a regra que sustenta isso: **a cor nunca é o único sinal.** Toda distinção vem acompanhada de ícone, forma ou rótulo — nunca só de matiz. É o que nos deixa monocromáticos *e* legíveis ao mesmo tempo (e acessíveis a quem não distingue cores).

---

### O modelo de 2 camadas — a espinha de toda a bíblia

Esta é a ideia central que organiza tudo o que vem depois. Toda peça da rede é construída em **duas camadas independentes**:

#### (A) PELE UNIVERSAL — o que toda peça veste

A **atmosfera comum**: a paleta (verde-mãe + ouro), a tipografia (Hanken Grotesk + Literata), o fundo escuro-papel (`#08080c`), a moldura tracejada verde, a grade de pontos, o número-fantasma e o acabamento cinematográfico (luz, profundidade, grão, vinheta).

A pele é o que faz **um carrossel e uma thumbnail parecerem irmãos**, mesmo tendo layouts completamente diferentes. É a camada do reconhecimento de 0,5 s. Ela é constante, governada por `marca.py`, e **não negociável** entre formatos. No código, ela vive no `BASE_CSS` compartilhado e nos tokens de marca.

#### (B) LAYOUT POR TIPO — a estrutura sob a pele

Por baixo da pele, cada formato tem sua **própria arquitetura**: a grade de itens da LISTA, a linha do tempo do FLUXO, as duas colunas do COMPARA, os números-herói do NUMEROS, os callouts da ANATOMIA — e, fora dos infográficos, o ritmo de slides do carrossel ou a hierarquia de uma thumbnail.

O layout é o **esqueleto que muda** conforme a informação a transmitir. No código, cada arquétipo é renderizado numa **página isolada** (`BASE_CSS` + só o CSS daquele tipo), de modo que **não há vazamento de estilo** entre formatos — a pele é compartilhada, o esqueleto é local.

#### Por que separar assim

A separação é o que nos dá **coerência e variedade ao mesmo tempo**. A pele garante que tudo pertença à mesma família; o layout garante que cada formato resolva bem seu trabalho. Trocar a cor-mãe é mexer em **uma** camada (a pele, em um arquivo) e propagar para 92 livros. Criar um formato novo é desenhar **um** esqueleto novo sob a pele que já existe. As seções desta bíblia mapeiam direto nessas duas camadas: 01–02 e 07–08 descrevem a **pele**; 03–06 descrevem os **layouts**; 00 e 09 são a doutrina e a governança que costuram as duas.

---

### Os princípios de marca

| Princípio | O que significa na prática |
|---|---|
| **Premium** | Nada de aparência "feita por IA" ou template genérico. Cada peça tem acabamento de catálogo editorial. |
| **Cinematográfico** | Luz, profundidade, grão e vinheta. A imagem tem *atmosfera*, não é flat design. |
| **Denso, mas legível** | Muita informação numa imagem — como as referências — sem nunca sacrificar a leitura. Densidade é a meta; ilegibilidade é o erro. |
| **Verde lidera** | O verde-mãe (hue 152) é a identidade. Domina a peça; o resto se subordina. |
| **Objeto > ícone** | O alvo é o **objeto fotorrealista** por conceito, não o ícone de linha. O ícone é a etapa intermediária; o objeto renderizado é a alma. |
| **Mono, não arco-íris** | Uma cor-mãe + um acento. Categorias se distinguem por ícone/forma/rótulo, jamais por uma paleta multicor. |
| **A cor nunca é o único sinal** | Acessibilidade e clareza: todo sinal de cor vem dobrado com forma, ícone ou texto. |
| **Gera-uma-vez + cache** | O objeto fotorrealista é caro de gerar. Gera-se uma vez por conceito, tinge-se na nossa cor e guarda-se. O custo é pago uma vez; o ativo se reusa. |

---

### A promessa visual da rede Minuto Real

Quando alguém vê uma peça nossa, a promessa entregue é:

- **"Isto é sério."** O acabamento premium sinaliza que o conteúdo por baixo também é cuidado — destilamos grandes livros com respeito.
- **"Isto é a Biblioteca."** O verde e o ouro são reconhecidos antes da leitura. A marca chega antes da palavra.
- **"Vou aprender algo aqui."** A densidade elegante promete substância, não enchimento — uma imagem que recompensa o tempo de leitura.

Toda decisão visual nesta bíblia serve a essas três promessas. Quando uma escolha não as serve, a escolha está errada.

---

### Os Mandamentos

1. **Verde lidera; ouro é o único acento.** Sem terceira cor de marca.
2. **A alma do catálogo, nunca o arco-íris.** Copiamos a densidade; rejeitamos a paleta multicor.
3. **A cor nunca é o único sinal.** Todo sinal de cor anda acompanhado de ícone, forma ou rótulo.
4. **Objeto fotorrealista vence ícone de linha.** O ícone é a ponte; o objeto-símbolo é o destino.
5. **Denso, mas sempre legível.** Densidade é virtude; ilegibilidade é falha.
6. **A pele é universal; o layout é por tipo.** Uma atmosfera para todos; um esqueleto para cada formato.
7. **`marca.py` é a fonte única de verdade.** Cor e fonte se leem dos tokens — nunca se hardcodam na peça.
8. **Gera uma vez, reusa sempre.** O objeto caro é cacheado; o pipeline é local e barato.
