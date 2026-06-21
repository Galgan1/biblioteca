import json

def get_sapiens():
  return {
    "ch01-revolucao-cognitiva": {
      "cards": [
        {"ic": "spark", "t": "A Árvore do Conhecimento", "emph": "Conhecimento", "b": "O salto do Homo sapiens não foi a ferramenta, mas a linguagem. <strong>Pudemos fofocar, organizar grupos maiores e inventar coisas que não existem no mundo físico.</strong> Essa flexibilidade mental nos separou dos outros animais de forma definitiva.", "tip": "<strong>Modelo mental:</strong> a fofoca é a base da coesão social; a ficção é o motor da cooperação em massa."},
        {"ic": "layers", "t": "O Poder da Ficção", "emph": "Ficção", "b": "Animais cooperam apenas com parentes ou conhecidos. <strong>O sapiens coopera em escalas gigantescas porque compartilha a crença em mitos comuns: deuses, nações e empresas.</strong> A ficção é o adesivo invisível da humanidade.", "tip": "<strong>Como aplicar:</strong> para liderar milhares, você precisa de uma história crível, não apenas de lógica bruta."},
        {"ic": "target", "t": "A Invasão Fulminante", "emph": "Invasão", "b": "Armado com a linguagem e a cooperação, o sapiens saiu da África e dominou o globo. <strong>Em nosso caminho, extinguimos as outras espécies humanas e dizimamos ecossistemas inteiros.</strong> A revolução não foi pacífica, foi uma marcha de conquista.", "tip": "<strong>Sinal de alerta:</strong> o impacto ecológico letal da nossa espécie começou milhares de anos antes da indústria.", "warn": True}
      ]
    },
    "ch02-o-cacador-coletor": {
      "cards": [
        {"ic": "leaf", "t": "A Vida Ancestral", "emph": "Vida", "b": "Passamos a maior parte da nossa história na selva, não em cidades. <strong>O nosso cérebro atual ainda opera com a programação de caçadores que temiam a fome e buscavam o doce.</strong> Nossos instintos modernos são ecos do passado antigo.", "tip": "<strong>Prática:</strong> compreenda que o desejo por açúcar e status é um software primitivo tentando sobreviver."},
        {"ic": "scale", "t": "A Sociedade Opulenta", "emph": "Opulenta", "b": "Apesar do perigo, a dieta original era rica e o tempo de trabalho era curto. <strong>Os caçadores não sofriam de epidemias modernas nem de jornadas extenuantes no campo.</strong> Eles conheciam o ambiente com uma precisão que nós perdemos.", "tip": "<strong>Para refletir:</strong> o avanço tecnológico das eras posteriores sacrificou o bem-estar do indivíduo comum."}
      ]
    },
    "ch03-revolucao-agricola": {
      "cards": [
        {"ic": "layers", "t": "A Maior Fraude", "emph": "Fraude", "b": "A agricultura multiplicou a quantidade de humanos, mas piorou a qualidade de vida. <strong>Trocamos o lazer da selva pelo trabalho escravo no campo e pela dieta pobre do trigo.</strong> O luxo de uma minoria foi financiado pelo suor da maioria.", "tip": "<strong>Modelo mental:</strong> nem todo avanço coletivo significa uma melhoria na vida do trabalhador."},
        {"ic": "spiral", "t": "Quem Domesticou Quem", "emph": "Domesticou", "b": "O trigo era uma gramínea insignificante até usar o homem para se espalhar. <strong>Nós achamos que dominamos a terra, mas foi a planta que nos forçou a carregar água e limpar pedras.</strong> Medido pelo DNA, o trigo venceu.", "tip": "<strong>Para refletir:</strong> o sucesso de uma espécie pode ser a escravidão dos seus membros."},
        {"ic": "key", "t": "A Armadilha do Luxo", "emph": "Armadilha", "b": "O que era conveniência logo se transformou em necessidade pesada. <strong>As invenções criam novas obrigações que tomam ainda mais o nosso tempo.</strong> Promessas de alívio sempre geram rotinas novas.", "tip": "<strong>Sinal de alerta:</strong> cuidado ao adotar tecnologias que juram poupar tempo; elas exigirão atenção constante.", "warn": True}
      ]
    },
    "ch04-piramides-escrita-memoria": {
      "cards": [
        {"ic": "layers", "t": "A Ordem Antes da Pedra", "emph": "Ordem", "b": "Monumentos colossais exigem que milhares acreditem no faraó. <strong>O tijolo da pirâmide é a fé no mito compartilhado.</strong> A narrativa invisível ergue a estrutura física.", "tip": "<strong>Modelo mental:</strong> procure a história invisível que mantém qualquer grande projeto em pé."},
        {"ic": "book", "t": "A Escrita e o Fisco", "emph": "Escrita", "b": "Ninguém inventou letras para fazer poesia ou registrar amor. <strong>A escrita surgiu porque a burocracia do império não cabia no cérebro frágil do tesoureiro.</strong> O alfabeto nasceu das contas de impostos.", "tip": "<strong>Prática:</strong> o registro escrito é a ferramenta que supera a fronteira biológica da memória."},
        {"ic": "cards", "t": "A Burocracia", "emph": "Burocracia", "b": "A escrita forçou o homem a pensar por categorias e pastas. <strong>Essa organização fragmentou a percepção natural do mundo, criando gavetas rígidas para a realidade.</strong> O sistema dita como enxergamos a verdade.", "tip": "<strong>Para refletir:</strong> não confunda a etiqueta da pasta com a essência da coisa."}
      ]
    },
    "ch05-ordem-imaginada-hierarquias": {
      "cards": [
        {"ic": "scale", "t": "A Ordem Imaginada", "emph": "Ordem Imaginada", "b": "Castas, raças e classes são divisões inventadas e sustentadas pela força. <strong>A ordem social só sobrevive porque milhões acreditam nela simultaneamente.</strong> É uma ilusão coletiva que machuca quem fica em baixo.", "tip": "<strong>Modelo mental:</strong> o direito do rei e o direito natural são ambos frutos da imaginação humana."},
        {"ic": "eye", "t": "Os Três Truques", "emph": "Três Truques", "b": "Para a ficção durar, ela finge que é a ordem natural das coisas. <strong>Ela se veste de arquitetura sólida, molda nossos desejos e exige adesão da manada inteira.</strong> Alterar essa rede exige criar um mito ainda maior.", "tip": "<strong>Como aplicar:</strong> você não quebra um sistema apenas duvidando dele; você precisa da fé dos outros."},
        {"ic": "spiral", "t": "O Ciclo Vicioso", "emph": "Vicioso", "b": "Um evento histórico cria uma lei excludente. <strong>A exclusão gera desigualdade, e a desigualdade serve de prova para justificar novas leis opressoras.</strong> A injustiça se alimenta da própria sombra.", "tip": "<strong>Sinal de alerta:</strong> quando argumentarem que a hierarquia é natural, procure quem se beneficia disso.", "warn": True}
      ]
    },
    "ch06-dinheiro": {
      "cards": [
        {"ic": "key", "t": "A Confiança Suprema", "emph": "Confiança", "b": "O papel pintado só vale porque todos concordam em trocar bens por ele. <strong>O dinheiro é o sistema de confiança mais eficiente já inventado pela humanidade.</strong> Ele dispensa a honestidade, bastando crer no símbolo.", "tip": "<strong>Modelo mental:</strong> as moedas conectam rivais e reúnem estranhos num campo comum."},
        {"ic": "link", "t": "O Conversor Universal", "emph": "Conversor", "b": "O capital traduz qualquer esforço em números frios. <strong>A riqueza pode virar poder, saúde ou armas num instante.</strong> Ele é o solvente que mistura civilizações isoladas.", "tip": "<strong>Prática:</strong> o dinheiro não tem moral; ele é a ferramenta neutra da conversão total."},
        {"ic": "scale", "t": "O Lado Sombrio", "emph": "Sombrio", "b": "Ao transformar tudo em preços, a economia corrói os laços de comunidade e afeto. <strong>A solidariedade dá lugar aos contratos pagos; a vila vira um mercado anônimo.</strong> A eficiência tem o custo do isolamento.", "tip": "<strong>Para refletir:</strong> o que ganha etiqueta de venda perde o caráter de laço humano inestimável."}
      ]
    },
    "ch07-imperios": {
      "cards": [
        {"ic": "layers", "t": "O Motor Cultural", "emph": "Motor Cultural", "b": "Os grandes conquistadores trituram as diferenças sob a bota do exército. <strong>A imposição violenta da lei gera uma cultura sincrética que sobrevive aos reis e ditadores.</strong> A força brutal une os polos distantes.", "tip": "<strong>Modelo mental:</strong> os impérios são os grandes liquidificadores de idiomas e costumes do planeta."},
        {"ic": "link", "t": "A Herança Imperial", "emph": "Herança", "b": "As tribos vencidas usam os conceitos do invasor para exigir justiça depois da guerra. <strong>Direitos e ideias iluministas viajaram no rastro da pilhagem e da invasão territorial.</strong> A pureza cultural original está perdida para sempre.", "tip": "<strong>Para refletir:</strong> a cultura que temos hoje é filha bastarda do colonizador com o nativo."},
        {"ic": "target", "t": "Visão Universalista", "emph": "Universalista", "b": "Muitos líderes prometeram que a conquista levaria a paz e a ciência para os selvagens ignorantes. <strong>A retórica do benefício universal mascara o roubo, mas entrega pontes e estradas no final.</strong> O imperialismo tem saldo sangrento e avanço tecnológico.", "tip": "<strong>Sinal de alerta:</strong> a justificativa de levar a civilização é o escudo comum de quem quer roubar riquezas.", "warn": True}
      ]
    },
    "ch08-religioes": {
      "cards": [
        {"ic": "mountain", "t": "Ordem Sobre-Humana", "emph": "Sobre-Humana", "b": "A ordem civil é frágil se baseada só na vontade dos prefeitos e juízes da cidade. <strong>Ao amarrar as regras à fúria de deuses severos, o líder garante a obediência cega.</strong> A moral divina consolida as leis dos homens.", "tip": "<strong>Modelo mental:</strong> as crenças oferecem uma âncora fixa acima do caos das disputas políticas locais."},
        {"ic": "wave", "t": "O Rolo Compressor", "emph": "Rolo Compressor", "b": "Os cultos universais não respeitam divisas; eles exigem o mundo inteiro aos seus pés descalços. <strong>O zelo missionário atropela os costumes antigos e cria uma rede mental planetária e uniforme.</strong> Essa unificação substitui tribos isoladas.", "tip": "<strong>Como aplicar:</strong> a expansão vigorosa depende da crença íntima de que a sua verdade deve salvar o mundo."},
        {"ic": "person", "t": "As Religiões Modernas", "emph": "Religiões", "b": "A política e a economia assumiram os altares que antes pertenciam aos santos do deserto. <strong>O comunismo e o liberalismo exigem sacrifícios, possuem dogmas rígidos e castigam duramente as heresias internas.</strong> Mudam os nomes, o culto permanece.", "tip": "<strong>Para refletir:</strong> trate as ideologias seculares com o mesmo cuidado crítico que se dispensa a seitas antigas."}
      ]
    },
    "ch09-revolucao-cientifica": {
      "cards": [
        {"ic": "lens", "t": "O Salto da Dúvida", "emph": "Dúvida", "b": "Os antigos liam pergaminhos fechados certos de que o saber do mundo já fora registrado pela história. <strong>O salto científico ocorreu no exato momento em que o homem admitiu sua própria e abissal ignorância.</strong> A dúvida honesta derrotou o dogma cego.", "tip": "<strong>Modelo mental:</strong> o conhecimento avança quando a confissão do 'não sei' vira premissa de trabalho."},
        {"ic": "target", "t": "Os Três Pilares", "emph": "Três Pilares", "b": "Para dominar o globo, a ciência exigiu mais do que apenas a confissão crua do desconhecido na porta. <strong>Ela cobrou o uso dos números e cobrou resultados práticos que fizessem o mundo se dobrar às vontades humanas.</strong> O rigor matemático garante a entrega.", "tip": "<strong>Prática:</strong> uma hipótese bonita mas que não se traduz em resultado prático serve para poetas, não para engenheiros."},
        {"ic": "spark", "t": "A Forja do Poder", "emph": "Poder", "b": "A pesquisa moderna não almeja a verdade límpida; ela caça armamentos potentes e motores mais velozes para o império. <strong>O casamento da luneta com o canhão gerou um ciclo irrefreável de dominação tecnológica pelas nações ocidentais.</strong> A ciência é serva da expansão.", "tip": "<strong>Sinal de alerta:</strong> o financiamento de pesquisas sempre obedece ao interesse direto de quem quer mais lucros e terras.", "warn": True}
      ]
    },
    "ch10-ciencia-imperio-capital": {
      "cards": [
        {"ic": "link", "t": "O Triângulo de Ouro", "emph": "Triângulo", "b": "A expansão planetária exigiu a união visceral do soldado armado, do pesquisador frio e do banqueiro calculista da capital. <strong>O rei protege as rotas, o sábio aponta o rumo exato e o comerciante paga as dívidas dos dois.</strong> Separados, os três caem; unidos, dividem o mapa.", "tip": "<strong>Modelo mental:</strong> na economia real, não existe descoberta livre de interesses de quem paga a conta."},
        {"ic": "lens", "t": "A Busca pelo Vazio", "emph": "Vazio", "b": "A Europa conquistou mares distantes não por ter armas maiores na época, mas por sua fome agressiva e violenta. <strong>A cultura do mapa em branco incitou navegadores a cruzar os oceanos sem bússola e preencher o continente com bandeiras e cruzes.</strong> A obsessão expansionista fez a diferença.", "tip": "<strong>Para refletir:</strong> o apetite por espaço cria poder; o comodismo destrói vantagens acumuladas por séculos."},
        {"ic": "target", "t": "A Fatura Sangrenta", "emph": "Sangrenta", "b": "Os navios levaram botânicos nos mesmos porões em que carregavam grilhões pesados de aço escravo. <strong>O progresso intelectual custou genocídios colossais e saques históricos inegáveis na América inteira e nas planícies do continente africano.</strong> O conhecimento ocidental nasce manchado.", "tip": "<strong>Sinal de alerta:</strong> nenhum avanço imenso chega limpo; não se faz a glória do amanhã sem destroçar vidas alheias hoje.", "warn": True}
      ]
    },
    "ch11-capitalismo-credito": {
      "cards": [
        {"ic": "spiral", "t": "A Moeda do Futuro", "emph": "Futuro", "b": "O crédito financia estradas porque confia na expansão inevitável da riqueza na década seguinte. <strong>O dinheiro de plástico rompe a estagnação do presente pagando a conta baseada num crescimento ainda invisível.</strong> É uma profecia arriscada, mas funciona se todos crerem.", "tip": "<strong>Modelo mental:</strong> a base do mercado financeiro repousa na promessa psicológica forte de que o amanhã será gigantesco."},
        {"ic": "steps", "t": "O Vício do Crescimento", "emph": "Crescimento", "b": "A máquina exige que os lucros engordem a conta todo ano para manter a lona do circo bem armada e esticada. <strong>O empresário injeta os ganhos novos diretamente na fornalha da linha de montagem, ignorando o próprio desgaste do maquinário exausto.</strong> Parar é falir sem glória nenhuma.", "tip": "<strong>Como aplicar:</strong> o princípio capitalista não é acumular prata num baú, mas girar a fortuna até a quebra definitiva."},
        {"ic": "target", "t": "A Cegueira Ética", "emph": "Ética", "b": "A religião do lucro infinito destrói montanhas nativas e polui vales rasos sem pensar no futuro respirável de ninguém. <strong>O balanço contábil esconde o desastre da natureza, cobrando a dívida em tempestades que castigarão os filhos cegos dos acionistas felizes.</strong> A externalidade fica fora do papel.", "tip": "<strong>Sinal de alerta:</strong> o foco exclusivo no saldo bancário joga a conta do veneno para as gerações que nascerão amanhã.", "warn": True}
      ]
    },
    "ch12-felicidade": {
      "cards": [
        {"ic": "wave", "t": "O Ajuste Químico", "emph": "Químico", "b": "A euforia da casa nova desbota logo; a biologia ajusta as marés internas, puxando o homem de volta para o patamar original cinza. <strong>A natureza usa o prazer como isca passageira para garantir sobrevivência e apaga a luz logo depois para você correr novamente.</strong> O contentamento perene ofende a evolução.", "tip": "<strong>Modelo mental:</strong> entenda que a biologia condena qualquer conquista definitiva ao tédio iminente do mês seguinte."},
        {"ic": "scale", "t": "O Abismo da Expectativa", "emph": "Expectativa", "b": "A TV de plasma aumenta o peso dos desejos sem entregar a proporção idêntica de paz mental diária e sólida. <strong>O camponês feliz dormia satisfeito na terra dura, enquanto o executivo rico sofre praguejando no assento apertado de um voo atrasado no gelo.</strong> A barra de exigência engole a vida.", "tip": "<strong>Prática:</strong> gerencie os seus próprios anseios com mãos de ferro; a cobiça desvairada aniquila qualquer conforto material."},
        {"ic": "bulb", "t": "O Fim do Desejo", "emph": "Desejo", "b": "As antigas tradições avisam que a busca enlouquecida pela recompensa apenas escava poços mais profundos no peito. <strong>O silêncio do budismo e do estoicismo aponta que soltar as cordas da ansiedade pesa menos do que carregar pedras preciosas no ombro.</strong> A vitória mora na ausência do grito.", "tip": "<strong>Para refletir:</strong> a paz autêntica reside na quebra brusca do anseio de ter mais, não no acúmulo infinito de troféus vazios."}
      ]
    },
    "ch13-fim-do-homo-sapiens": {
      "cards": [
        {"ic": "spiral", "t": "O Salto Ciborgue", "emph": "Ciborgue", "b": "O roteiro da biologia natural fechou as cortinas; o homem pisa no palco usando tesouras genéticas e transistores de aço impiedoso. <strong>As máquinas assumem as lacunas da carne fraca e rasgam as velhas barreiras impostas por quatro bilhões de anos gelados e passivos.</strong> Nós desenhamos a próxima espécie.", "tip": "<strong>Modelo mental:</strong> o controle da nossa biologia é a passagem sem volta de macaco falante para força geológica independente."},
        {"ic": "layers", "t": "Mentes Imortais", "emph": "Imortais", "b": "A fusão do pulso elétrico frio com as células vivas úmidas aponta para cérebros fora de caixas finas cranianas e mortais. <strong>A mente liberta do peso de corpos perecíveis pode vagar nas redes e mudar de suporte na hora da pane fatal dos rins ou fígado.</strong> A imortalidade já ganha forma plástica.", "tip": "<strong>Como aplicar:</strong> compreenda que as restrições biológicas que moldam leis, éticas e mercados não resistirão por muito tempo."},
        {"ic": "fork", "t": "Deuses Confusos", "emph": "Confusos", "b": "Ganhamos motores interplanetários, mas nossa mente continua obcecada por status pífio, medo mesquinho e conforto morno de animal caçado. <strong>Ter o poder do céu nas mãos atadas de seres que ignoram o próprio desejo é a promessa do desastre maciço e surdo de proporções colossais.</strong> Ser deus sem propósito é a ruína.", "tip": "<strong>Sinal de alerta:</strong> o avanço técnico sem evolução de caráter forja armas pesadas demais para garotos temperamentais chorões.", "warn": True}
      ]
    }
  }

with open("gen_b8.json", "w", encoding="utf-8") as f:
    json.dump(get_sapiens(), f, ensure_ascii=False, indent=2)
