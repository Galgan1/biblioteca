import os

skill_dir = r"C:\Users\User\.gemini\config\skills\sun-tzu-arte-da-guerra\chapters"

chapters = {
    "ch04-posicoes-taticas.md": """# Chapter IV: Posições Táticas

## Core Idea
A invencibilidade depende de você; a derrota do inimigo depende dos erros dele. O perito torna-se invencível primeiro, depois espera a oportunidade de derrotar o inimigo. A vitória pode ser prevista, mas não forçada.

## Frameworks Introduced
- **Princípio da Invencibilidade**: ser invencível depende de si mesmo; derrotar o inimigo depende dos erros dele
  - When to use: para definir prioridades estratégicas — fortaleça-se antes de atacar
  - How: construa uma posição inabalável antes de buscar vulnerabilidades no adversário
- **Ataque vs Defesa**: quando não há chance de vitória, defenda; quando há, ataque
  - When to use: para decidir entre postura ofensiva ou defensiva
- **Cinco Elementos das Regras Militares**: análise do terreno → cálculo de recursos → capacidade logística → comparação de forças → previsão de vitória
  - When to use: como checklist de planejamento operacional sequencial

## Key Concepts
- **Invencibilidade**: estado que depende exclusivamente de suas próprias ações
- **Vitória previsível**: não excede o bom senso — o perito vence quando a vitória é facilmente previsível
- **Peso desproporcional**: exército vitorioso é 100kg contra gramas; derrotado é gramas contra centenas de kg
- **Águas represadas**: a força acumulada que se libera de 10.000 pés de altura

## Anti-patterns
- **Forçar a vitória**: a pessoa pode predizer uma vitória, mas não pode forçá-la
- **Lutar sem condições**: iniciar batalha esperando vitória depois, em vez de garantir condições antes

## Key Takeaways
1. Torne-se invencível primeiro, depois busque oportunidades
2. A vitória não deve ser forçada — ela surge da preparação
3. Siga os cinco elementos em sequência: terreno → recursos → logística → comparação → previsão
4. Acumule vantagens como águas represadas — libere-as no momento certo

## Connects To
- **Ch 01**: Os cinco fatores são a base dos cálculos aqui expandidos
- **Ch 05**: A vantagem estratégica como aplicação do princípio de força acumulada
""",
    "ch05-vantagens.md": """# Chapter V: Vantagens

## Core Idea
A arte da guerra se resume a combinar táticas frontais e de surpresa infinitamente, como as notas musicais que produzem melodias infinitas a partir de apenas cinco notas. O comandante habilidoso explora vantagem estratégica, não depende da bravura individual.

## Frameworks Introduced
- **Táticas Frontais + Surpresa**: as duas operações fundamentais cujas combinações são infinitas
  - When to use: em qualquer planejamento tático
  - How: use o frontal para fixar, o surpresa para destruir; alterne entre ambos continuamente
- **Princípio do Impulso**: torrente que faz saltar pedras (impulso) + falcão que destrói presa (oportunidade)
  - When to use: para cronometrar ações de alto impacto
  - How: acumule potencial como arco esticado, libere no momento preciso
- **Vantagem Estratégica**: pedra redonda rolando de montanha de 10.000 pés
  - When to use: para entender que vantagem vem da posição, não dos homens

## Key Concepts
- **Cinco notas, cores e sabores**: combinações simples geram resultados infinitos
- **Desordem da ordem**: a desordem nasce da ordem, covardia da coragem, fraqueza da força — tudo depende da organização
- **Seleção de homens**: o general seleciona os homens certos e explora situações favoráveis

## Key Takeaways
1. Combine frontal e surpresa infinitamente — como notas musicais
2. Acumule impulso e libere-o no momento preciso
3. Explore a posição estratégica, não dependa de bravura individual
4. Ofereça iscas ao inimigo, mas espere-o armado com toda a força

## Connects To
- **Ch 03**: Estratagemas como a base para as combinações táticas
- **Ch 06**: Exploração de pontos fracos como aplicação da surpresa
""",
    "ch06-pontos-fortes-fracos.md": """# Chapter VI: Pontos Fortes e Pontos Fracos

## Core Idea
O general competente move o inimigo e nunca é movido por ele. Chegue primeiro ao campo de batalha. Seja sutil a ponto de não deixar rastros; misterioso a ponto de ser inaudível. Ataque os pontos fracos, evite os fortes — como água corrente que flui para o terreno baixo.

## Frameworks Introduced
- **Domínio da Iniciativa**: quem chega primeiro descansa; quem chega depois se exaure
  - When to use: em qualquer situação competitiva — first-mover advantage
  - How: ocupe o campo de batalha (mercado/posição) antes do adversário
- **Princípio da Concentração**: concentre suas forças em um ponto enquanto o inimigo dispersa em dez — seremos 10 contra 1
  - When to use: quando precisa criar superioridade local em um cenário de recursos limitados
- **Água Corrente**: táticas são como água — evite terreno alto (forças), flua para o baixo (fraquezas)
  - When to use: como modelo mental permanente para adaptação tática
- **Precauções Múltiplas = Fraqueza**: quem toma precauções em todos os lugares será fraco em todos os lugares
  - When to use: para explorar adversários que dispersam recursos

## Key Concepts
- **Sutileza extrema**: tão sutil que ninguém ache rastro; tão misterioso que ninguém ouça informação
- **Determinando a situação**: escaramuças para revelar onde o inimigo é forte e fraco
- **Posições irrepetíveis**: vitórias não podem ser repetidas — cada circunstância é única

## Anti-patterns
- **Fortalecer todos os lugares**: se fortalece todos, será fraco em todos
- **Repetir táticas**: o modo de lutar nunca permanece constante

## Key Takeaways
1. Mova o inimigo — nunca seja movido por ele
2. Concentre suas forças onde o inimigo dispersa
3. Seja água: flua para os pontos fracos, evite os fortes
4. Cada vitória é única — nunca repita a mesma tática

## Connects To
- **Ch 03**: "Vencer sem lutar" começa com a identificação de pontos fracos
- **Ch 05**: Vantagem estratégica aplicada contra vulnerabilidades
""",
    "ch07-manobras.md": """# Chapter VII: Manobras

## Core Idea
A arte de manobrar está em transformar desvantagem em vantagem, caminhos tortuosos em retas. A manobra contém tanto oportunidades quanto perigos — mover todo o exército depressa sacrifica equipamentos; mover devagar perde a oportunidade. O moral é o fator decisivo.

## Frameworks Introduced
- **Caminho Tortuoso em Reto**: enganar o inimigo levando-o por rota tortuosa enquanto toma atalho direto
  - When to use: para obter posição favorável antes do adversário
- **Regra do Moral**: espírito agudo no início → relaxa no meio → fraco no final. Ataque quando o moral é baixo
  - When to use: para cronometrar engajamentos com base no estado psicológico do adversário
- **Regra da Administração de Exército Grande**: gongos/tambores/bandeiras unificam o exército — quando unificado, corajoso não avança só e covarde não recua sozinho
  - When to use: para entender a importância de sinais claros e comunicação
- **Cinco Qualidades de Movimento**: rápido como vento, estável como floresta, feroz como fogo, firme como montanha, inescrutável como nuvens
  - When to use: como framework para adaptar postura tática ao contexto

## Anti-patterns
- **Marcha forçada total**: correr 100 li sem parar = só 1/10 chega na hora; generais capturados
- **Ignorar terreno**: não conhecer montanhas, florestas e pântanos = incapaz de marchar
- **Atacar inimigo com moral alta**: nunca enfrente o inimigo quando seu espírito é agudo e irresistível

## Key Takeaways
1. Transforme desvantagem em vantagem — o caminho tortuoso pode ser tornado reto
2. Administre o moral como recurso — ataque quando o do inimigo estiver baixo
3. Nunca lance ataque sobre inimigo em terreno alto ou com colinas apoiando-o
4. Sempre deixe um caminho de saída para inimigo cercado — evite desespero

## Connects To
- **Ch 05**: As cinco qualidades de movimento como aplicação das combinações frontais/surpresa
- **Ch 09**: Regras detalhadas de posicionamento expandem o conhecimento de terreno
""",
    "ch08-contingencias.md": """# Chapter VIII: Contingências

## Core Idea
Um general deve compreender as variáveis táticas e as cinco regras que não devem ser violadas. Deve ponderar vantagens e desvantagens simultaneamente. Há cinco fraquezas fatais que podem destruir qualquer líder.

## Frameworks Introduced
- **Cinco Regras de Exceção**: algumas estradas não devem ser percorridas; inimigos não devem ser atacados; cidades não devem ser capturadas; territórios não devem ser contestados; ordens do soberano não devem ser obedecidas
  - When to use: para lembrar que nem toda oportunidade deve ser aproveitada
- **Cinco Fraquezas Fatais**: falhas de caráter que destroem generais
  - When to use: para autoavaliação de liderança e análise do adversário
  - How: identificar se você ou o oponente sofre de: valentia temerária, covardia, irascibilidade, excesso de honra, ou benevolência excessiva
- **Princípio da Prontidão**: nunca confie na probabilidade do inimigo não vir — dependa de estar preparado
  - When to use: sempre — é a base da postura defensiva

## Key Concepts
- **Ponderação dupla**: conhecer vantagens = sucesso nos planos; conhecer desvantagens = solucionar dificuldades
- **Regra da Nunca-Confiança**: dependa de sua preparação, não da inação do inimigo

## Anti-patterns
- **Valentia temerária**: ser valente e desprezar a vida → morto facilmente
- **Covardia**: hesitar na véspera → capturado facilmente
- **Irascibilidade**: temperamento explosivo → provocado facilmente
- **Excesso de honra**: suscetível demais → envergonhado facilmente
- **Benevolência excessiva**: preza demais as pessoas → hesitante e passivo

## Key Takeaways
1. Nem toda estrada deve ser seguida, nem toda batalha travada
2. Sempre pondere vantagens E desvantagens antes de agir
3. Nunca dependa da inação do inimigo — dependa da sua preparação
4. As cinco fraquezas fatais são os maiores riscos de qualquer líder

## Connects To
- **Ch 03**: As cinco fraquezas contrabalançam as cinco virtudes do comandante
- **Ch 10**: Terreno como fator de contingência operacional
""",
    "ch09-exercito-em-marcha.md": """# Chapter IX: O Exército em Marcha

## Core Idea
O posicionamento correto em diferentes terrenos (montanhas, rios, pântanos, planícies) é fundamental. Além disso, o general deve saber ler sinais — da natureza, das negociações, das formações inimigas e do comportamento dos soldados — para antecipar as intenções do inimigo.

## Frameworks Introduced
- **Quatro Leis de Posicionamento**: regras para montanhas, rios, pântanos salgados e terras planas
  - When to use: para decidir posicionamento em qualquer contexto geográfico/competitivo
  - How: sempre buscar terreno alto + ensolarado + com provisões + longe de perigos
- **Sistema de Sinais**: framework completo para ler as intenções do inimigo
  - When to use: para interpretar comportamento competitivo
  - How: observar posicionamento, indícios naturais, negociações, formações e comportamento
- **Regra da Civilidade + Disciplina**: comandar com humanidade para unir; com disciplina para manter na linha
  - When to use: para liderança equilibrada

## Key Concepts
- **Árvores se movendo**: inimigo avançando. **Pássaros levantando voo**: emboscada. **Pássaros reunidos no campo**: acampamento abandonado
- **Palavras moderadas + preparação**: inimigo vai avançar. **Palavras belicosas**: vai se retirar
- **Soldados apoiados em armas**: famintos e fatigados
- **Recompensas excessivas**: general com problemas. **Castigos excessivos**: angústia séria

## Key Takeaways
1. Sempre busque terreno alto, ensolarado e com linhas de provisão livres
2. Aprenda a ler sinais — da natureza, do comportamento e das negociações
3. Comande com civilidade e disciplina em equilíbrio
4. Quem faz planos e não menospreza o inimigo terá o apoio de seus homens

## Connects To
- **Ch 10**: Detalhamento dos seis tipos de terreno
- **Ch 13**: Espionagem como complemento à leitura de sinais
""",
    "ch10-terreno.md": """# Chapter X: O Terreno

## Core Idea
Existem seis tipos de terreno e seis situações que apontam a derrota. O terreno é o maior aliado do comandante. A fórmula completa: conheça o inimigo + conheça a si mesmo + conheça o terreno = vitória absoluta.

## Frameworks Introduced
- **Seis Tipos de Terreno**: acessível, traiçoeiro, duvidoso, estreito, acidentado, distante — cada um exige tática específica
  - When to use: para adaptar a estratégia ao ambiente competitivo
- **Seis Situações de Derrota**: fuga, negligência, deterioração, desmoronamento, desorganização, derrota — todas causadas por falhas de comando
  - When to use: para diagnóstico de problemas organizacionais
- **Fórmula Completa de Vitória**: conhecer inimigo + conhecer a si mesmo + conhecer o terreno = sem perigo
  - When to use: como extensão do framework de autoconhecimento do Ch 03

## Key Concepts
- **Terreno traiçoeiro**: fácil de entrar, difícil de sair — perigo de armadilha
- **Terreno duvidoso**: fingir retirada e golpear quando inimigo persegue
- **Pedra preciosa do Estado**: comandante que avança sem buscar fama e retrocede sem fugir da responsabilidade
- **Filhos amados**: tratar soldados como filhos gera lealdade até a morte — mas sem disciplina, são crianças mimadas

## Anti-patterns
- **Meias chances**: conhecer só o inimigo OU só suas tropas OU só o terreno = apenas 50% de chance
- **Desobedecer quando certo**: lutar mesmo quando o soberano ordena, se a situação aponta derrota

## Key Takeaways
1. Domine os seis tipos de terreno e suas táticas correspondentes
2. As seis situações de derrota são sempre culpa do comando, nunca da natureza
3. Conheça inimigo + si mesmo + terreno = vitória sem perigo
4. Trate soldados com amor E disciplina — nunca só um dos dois

## Connects To
- **Ch 01**: Terreno como um dos cinco fatores fundamentais
- **Ch 11**: As nove situações expandem a análise do terreno
""",
    "ch11-nove-situacoes.md": """# Chapter XI: As Nove Situações

## Core Idea
O terreno pode ser classificado em nove situações táticas, cada uma exigindo uma conduta específica. A psicologia dos soldados é moldada pela situação — em terreno desesperado, lutam até a morte sem precisar de ordens. A velocidade e a exploração de vulnerabilidades são a essência das operações.

## Frameworks Introduced
- **Nove Terrenos Táticos**: dispersivo, marginal, contencioso, aberto, convergente, crítico, difícil, cercado, desesperado
  - When to use: para classificar qualquer situação competitiva e escolher a conduta correta
- **Serpente de Monte Chang (Shuairan)**: se golpeia a cabeça, o rabo ataca; se golpeia o rabo, a cabeça ataca — coordenação instantânea
  - When to use: como modelo de organização adaptativa e responsiva
- **Princípio da Sem-Saída**: lance soldados onde não há retirada — eles lutarão até a morte
  - When to use: quando precisa de comprometimento total da equipe
- **Essência das Operações**: velocidade + explorar vulnerabilidades + caminhos inesperados + atacar onde não está preparado
  - When to use: como princípio operacional fundamental

## Key Concepts
- **Psicologia do desespero**: soldados sem saída resistem, lutam desesperadamente e seguem o general sem hesitação
- **Pureza da donzela → rapidez da lebre**: comece com aparência inocente, ataque com velocidade quando o inimigo abrir os portões
- **Capture o que ele preza**: faça o inimigo se curvar tomando algo valioso para ele

## Key Takeaways
1. Classifique o terreno em uma das nove situações e siga a conduta correspondente
2. Soldados em terreno desesperado lutam como nunca — use isso estrategicamente
3. Velocidade + exploração de vulnerabilidades = essência da operação militar
4. Seja serpente: coordenação instantânea em todas as partes

## Connects To
- **Ch 10**: Expansão dos seis terrenos em nove situações
- **Ch 02**: Provisões em território inimigo como necessidade de sobrevivência
""",
    "ch12-ataque-pelo-fogo.md": """# Chapter XII: O Ataque pelo Fogo

## Core Idea
O fogo é uma arma poderosa que requer timing preciso e condições favoráveis. Mas além da tática, este capítulo traz a lição mais profunda: nunca empreenda guerra por ira — um Estado destruído não pode ser reavivado, um morto não pode ser ressuscitado. O soberano iluminado age com prudência.

## Frameworks Introduced
- **Cinco Modos de Ataque pelo Fogo**: queimar tropas, provisões, equipamentos, arsenais, linhas de reabastecimento
  - When to use: como framework de ataque indireto — destruir a infraestrutura, não só a força
- **Princípio do Momento Oportuno**: atacar quando o tempo está seco, com ventos fortes — coordenar condições externas
  - When to use: para cronometrar ações destrutivas com condições ambientais favoráveis
- **Princípio da Prudência Suprema**: nunca aja por ira; nunca envie tropas por indignação; um Estado destruído nunca revive
  - When to use: como freio emocional em todas as decisões estratégicas

## Key Concepts
- **Fogo vs Água**: fogo pode destruir; água pode bloquear — mas água não priva o inimigo de provisões
- **Não consolidar**: ganhar batalha mas não consolidar é desperdício de tempo
- **Ira passageira**: homem enfurecido volta a ser feliz; Estado destruído nunca revive

## Anti-patterns
- **Guerra por emoção**: soberano que age por ira ou indignação arrisca destruição irreversível
- **Atacar contra o vento**: nunca ataque quando o vento sopra contra você
- **Não consolidar vitórias**: desperdício fatal de recursos e esforço

## Key Takeaways
1. Destrua a infraestrutura do inimigo, não apenas suas forças
2. Cronometre ações com condições externas favoráveis
3. Nunca aja por ira — decisões emocionais são irreversíveis
4. Consolide cada vitória antes de buscar a próxima

## Connects To
- **Ch 02**: Custos da guerra como contexto para prudência
- **Ch 08**: Cinco fraquezas fatais incluem irascibilidade
""",
    "ch13-uso-de-espioes.md": """# Chapter XIII: O Uso de Espiões

## Core Idea
A espionagem é o alicerce de todas as operações militares. Investir em inteligência custa infinitamente menos que manter um exército em campanha. O espião convertido é a peça central — através dele, todos os outros tipos de espionagem se tornam possíveis.

## Frameworks Introduced
- **Cinco Tipos de Espiões**: framework completo de inteligência
  - When to use: para estruturar qualquer operação de coleta de informações
  - How: 1) Nativos (locais do inimigo); 2) Internos (funcionários do inimigo); 3) Convertidos (espiões inimigos trabalhando para você); 4) Descartáveis (seus agentes com informação falsa); 5) Indispensáveis (agentes confiáveis entre os dois lados)
- **Princípio do Espião Convertido**: toda a base da espionagem repousa no convertido — por isso deve ser o mais recompensado
  - When to use: para priorizar investimentos em inteligência
- **Três Qualidades do Spymaster**: astúcia para empregar, humanidade e justiça para reter, atenção sutil para obter verdade
  - When to use: para avaliar capacidade de gestão de inteligência

## Worked Example
Cadeia de espionagem integrada: 1) Recrute espião CONVERTIDO (ex-agente do inimigo); 2) Através dele, obtenha informações para recrutar NATIVOS e INTERNOS; 3) Use DESCARTÁVEIS para desinformar o inimigo com dados falsos; 4) Envie INDISPENSÁVEIS para completar missões com base nas informações coletadas.

## Key Concepts
- **Custo-benefício**: mil barras de ouro por dia para exército vs. investimento mínimo em espiões
- **Conhecimento prévio**: não vem de fantasmas nem cálculos astronômicos — vem de pessoas que conhecem o inimigo
- **Segredo absoluto**: se plano secreto é divulgado prematuramente, espião e todos os contatos morrem

## Anti-patterns
- **Ignorar inteligência**: gastar anos sem conhecer o inimigo por economizar em espiões
- **Confiar em fontes não-humanas**: presságios, cálculos astrológicos e experiências passadas não substituem inteligência real

## Key Takeaways
1. Espionagem é o alicerce de todo movimento militar — invista generosamente
2. O espião convertido é a peça central de toda a rede de inteligência
3. Informação vem de pessoas, não de adivinhação ou analogias históricas
4. Segredo absoluto é vital — uma falha mata toda a rede

## Connects To
- **Ch 01**: Conhecimento prévio como base dos cálculos estratégicos
- **Ch 03**: Autoconhecimento + conhecimento do inimigo via espionagem
"""
}

for filename, content in chapters.items():
    filepath = os.path.join(skill_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Created: {filename}")

print("All chapters created!")
