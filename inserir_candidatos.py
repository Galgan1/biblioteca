# -*- coding: utf-8 -*-
"""Insere os livros CANDIDATOS (só card na estante, sem página/skill) na Biblioteca.

Cada candidato vira um card "Em breve": NÃO tem página de resumo (campo comingSoon),
o card não navega — só o chip "Comprar" (afiliado Amazon) leva à loja. A capa é a
ORIGINAL da edição brasileira, baixada pelo ASIN na CDN da Amazon (fallback Open Library).

O que faz (idempotente por id):
  1. Baixa a capa de cada livro -> assets/<slug>-cover.png  (valida imagem real)
  2. Acrescenta a entrada em books.json (sem duplicar; com comingSoon=True)
  3. Registra o ASIN em afiliados/afiliados.json (para gerar_links.py fazer link DIRETO /dp/)

Depois rode:  python afiliados/gerar_links.py   (espelha o campo "amazon" no books.json)

Uso:  python inserir_candidatos.py
"""

import io
import json
import os
import sys
import urllib.request

from PIL import Image

BASE = os.path.dirname(os.path.abspath(__file__))
BOOKS = os.path.join(BASE, "books.json")
AFIL = os.path.join(BASE, "afiliados", "afiliados.json")
ASSETS = os.path.join(BASE, "assets")
UA = {"User-Agent": "Mozilla/5.0 (biblioteca-cover/1.0; +andregalgani.com.br)"}
MIN_BYTES = 5000  # abaixo disso é placeholder/"imagem indisponível"

# (slug, title, author, asin, description, [tags])
CANDIDATOS = [
    (
        "psicologia-financeira",
        "A Psicologia Financeira",
        "Morgan Housel",
        "6555111100",
        "Lidar bem com dinheiro tem menos a ver com inteligência e mais com comportamento. Em 19 histórias curtas, Housel mostra como ego, ganância, medo e paciência decidem o destino financeiro — mais do que planilhas.",
        ["Dinheiro", "Comportamento", "Investimentos"],
    ),
    (
        "hora-da-estrela",
        "A Hora da Estrela",
        "Clarice Lispector",
        "853250812X",
        "O último romance de Clarice: a história de Macabéa, datilógrafa nordestina e quase invisível no Rio. Uma meditação cortante sobre pobreza, existência e o instante fatal, narrada por um escritor em crise.",
        ["Literatura", "Ficção", "Brasil"],
    ),
    (
        "habitos-atomicos",
        "Hábitos Atômicos",
        "James Clear",
        "8550807567",
        "Pequenas mudanças, resultados notáveis. Clear mostra que melhorar 1% ao dia se acumula, e dá as 4 leis da mudança de comportamento para criar bons hábitos e abandonar os ruins por sistema, não por força de vontade.",
        ["Hábitos", "Produtividade", "Autodesenvolvimento"],
    ),
    (
        "homem-mais-rico-babilonia",
        "O Homem Mais Rico da Babilônia",
        "George S. Clason",
        "8595081530",
        "Parábolas na antiga Babilônia que destilam regras atemporais da prosperidade: pague-se primeiro (guarde 1/10 do que ganha), faça o ouro trabalhar por você e proteja seu patrimônio da perda.",
        ["Finanças", "Riqueza", "Clássico"],
    ),
    (
        "noites-brancas",
        "Noites Brancas",
        "Fiódor Dostoiévski",
        "8582850743",
        "Em quatro noites de verão em São Petersburgo, um sonhador solitário encontra a jovem Nástienka. Uma novela breve e melancólica sobre amor não correspondido, ilusão e a beleza efêmera de um encontro.",
        ["Literatura", "Romance", "Rússia"],
    ),
    (
        "quatro-compromissos",
        "Os Quatro Compromissos",
        "Don Miguel Ruiz",
        "6557120956",
        "A sabedoria tolteca em quatro acordos para a liberdade pessoal: seja impecável com a palavra, não leve nada para o lado pessoal, não tire conclusões precipitadas e faça sempre o seu melhor.",
        ["Espiritualidade", "Sabedoria", "Autodesenvolvimento"],
    ),
    (
        "mais-esperto-que-o-diabo",
        "Mais Esperto que o Diabo",
        "Napoleon Hill",
        "8568014003",
        "Escrito em 1938 e mantido inédito por décadas: numa entrevista imaginária, Hill arranca do 'Diabo' o segredo do medo, da procrastinação e da deriva — o hábito de deixar a vida ser decidida pelas circunstâncias.",
        ["Sucesso", "Mentalidade", "Autodesenvolvimento"],
    ),
    (
        "quebrando-o-habito",
        "Quebrando o Hábito de Ser Você Mesmo",
        "Joe Dispenza",
        "8568014321",
        "Unindo neurociência, epigenética e meditação, Dispenza mostra como romper os padrões automáticos de pensamento e emoção que recriam o mesmo 'eu' todo dia — e reprogramar a mente para uma nova realidade.",
        ["Neurociência", "Mentalidade", "Autodesenvolvimento"],
    ),
    (
        "como-fazer-amigos",
        "Como Fazer Amigos e Influenciar Pessoas",
        "Dale Carnegie",
        "8504018024",
        "O manual clássico das relações humanas: princípios para agradar, conquistar pessoas para o seu modo de pensar e liderar sem gerar ressentimento — começando por nunca criticar e por se interessar de verdade pelo outro.",
        ["Relacionamentos", "Comunicação", "Clássico"],
    ),
    (
        "essencialismo",
        "Essencialismo",
        "Greg McKeown",
        "8543102146",
        "A busca disciplinada por menos. McKeown defende fazer só o essencial — menos, porém melhor — eliminando o trivial para investir energia no que de fato importa, em vez de dizer sim a tudo.",
        ["Produtividade", "Foco", "Carreira"],
    ),
    (
        "sutil-arte",
        "A Sutil Arte de Ligar o F*da-se",
        "Mark Manson",
        "855100249X",
        "Um contraponto irreverente à autoajuda positiva: você só tem energia para se importar com poucas coisas, então escolha bem. Manson defende valores melhores, aceitar limites e parar de fugir da dor inevitável.",
        ["Autodesenvolvimento", "Filosofia", "Comportamento"],
    ),
    (
        "mulheres-que-correm-com-os-lobos",
        "Mulheres que Correm com os Lobos",
        "Clarissa Pinkola Estés",
        "853252978X",
        "A psicanalista junguiana resgata o arquétipo da Mulher Selvagem por meio de mitos e contos, mapeando a recuperação da intuição, da criatividade e da força instintiva sufocadas pela cultura.",
        ["Psicologia", "Mitologia", "Feminino"],
    ),
    (
        "sociedade-do-cansaco",
        "Sociedade do Cansaço",
        "Byung-Chul Han",
        "8532649963",
        "Saímos da sociedade disciplinar (do dever) para a do desempenho (do poder): livres para nos explorarmos sozinhos. Han diagnostica o burnout e a depressão como doenças do excesso de positividade.",
        ["Filosofia", "Sociedade", "Trabalho"],
    ),
    (
        "assim-falou-zaratustra",
        "Assim Falou Zaratustra",
        "Friedrich Nietzsche",
        "8535930485",
        "O poema filosófico de Nietzsche: Zaratustra desce da montanha para anunciar a morte de Deus, o além-do-homem, a vontade de potência e o eterno retorno. Uma obra 'para todos e para ninguém'.",
        ["Filosofia", "Clássico", "Existência"],
    ),
    (
        "mundo-de-sofia",
        "O Mundo de Sofia",
        "Jostein Gaarder",
        "8535921893",
        "Um romance que é também um curso de filosofia: a jovem Sofia recebe cartas misteriosas que a conduzem dos pré-socráticos a Sartre — enquanto descobre que sua própria realidade pode não ser o que parece.",
        ["Filosofia", "Romance", "História das Ideias"],
    ),
    (
        "crime-e-castigo",
        "Crime e Castigo",
        "Fiódor Dostoiévski",
        "8573262087",
        "Raskólnikov, estudante miserável, assassina uma agiota para provar que está acima da moral comum. Dostoiévski disseca a culpa, a redenção e a teoria do 'homem extraordinário' num thriller psicológico monumental.",
        ["Literatura", "Psicologia", "Rússia"],
    ),
    (
        "irmaos-karamazov",
        "Os Irmãos Karamázov",
        "Fiódor Dostoiévski",
        "8573265388",
        "A obra-prima final de Dostoiévski: o assassinato de um pai e o julgamento dos filhos viram palco para as maiores questões humanas — fé e dúvida, livre-arbítrio e o problema do mal (o 'Grande Inquisidor').",
        ["Literatura", "Filosofia", "Rússia"],
    ),
    (
        "o-idiota",
        "O Idiota",
        "Fiódor Dostoiévski",
        "8573262559",
        "O príncipe Míchkin, bondoso a ponto de parecer 'idiota', volta à Rússia e é triturado pela ganância e pela vaidade da sociedade. Dostoiévski pergunta se um homem verdadeiramente bom pode sobreviver neste mundo.",
        ["Literatura", "Psicologia", "Rússia"],
    ),
    (
        "memorias-do-subsolo",
        "Memórias do Subsolo",
        "Fiódor Dostoiévski",
        "8573261854",
        "O monólogo amargo do 'homem do subsolo', funcionário ressentido que ataca a razão e o progresso. Considerado o primeiro romance existencialista: um mergulho na liberdade, no rancor e na autossabotagem.",
        ["Literatura", "Filosofia", "Existência"],
    ),
    (
        "o-principe",
        "O Príncipe",
        "Nicolau Maquiavel",
        "8563560034",
        "O tratado que separou a política da moral. Maquiavel ensina como conquistar e manter o poder no mundo como ele é — não como deveria ser: melhor ser temido que amado, e a razão de Estado acima de tudo.",
        ["Política", "Poder", "Clássico"],
    ),
    (
        "48-leis-do-poder",
        "As 48 Leis do Poder",
        "Robert Greene",
        "8532521665",
        "Um código amoral do poder destilado de 3 mil anos de história: 48 leis — de 'nunca ofusque o mestre' a 'mantenha os outros dependentes de você' — para dominar o jogo ou se defender de quem o joga.",
        ["Poder", "Estratégia", "Psicologia"],
    ),
    (
        "leis-da-natureza-humana",
        "As Leis da Natureza Humana",
        "Robert Greene",
        "6555353686",
        "Greene mapeia os impulsos profundos que governam o comportamento — narcisismo, inveja, irracionalidade, máscara social — para você ler as pessoas com clareza e dominar seus próprios padrões destrutivos.",
        ["Psicologia", "Comportamento", "Poder"],
    ),
    (
        "arte-da-seducao",
        "A Arte da Sedução",
        "Robert Greene",
        "6555322047",
        "A sedução como forma de poder. Greene anatomiza os nove tipos de sedutor, as vítimas e o processo em 24 fases — de criar tensão a render o alvo — aplicável ao amor, à política e à persuasão.",
        ["Sedução", "Psicologia", "Poder"],
    ),
    (
        "rapido-e-devagar",
        "Rápido e Devagar: Duas Formas de Pensar",
        "Daniel Kahneman",
        "853900383X",
        "O Nobel Kahneman revela os dois sistemas da mente: o Sistema 1 (rápido, intuitivo, emocional) e o Sistema 2 (lento, deliberado, lógico) — e o catálogo de vieses e ilusões que distorcem nossas decisões.",
        ["Psicologia", "Decisão", "Economia Comportamental"],
    ),
    (
        "jogos-da-vida",
        "Os Jogos da Vida",
        "Eric Berne",
        "8521308760",
        "O fundador da Análise Transacional revela os 'jogos' psicológicos — sequências de transações com ganho oculto — que estruturam nossas relações, e os papéis de Pai, Adulto e Criança que assumimos sem perceber.",
        ["Psicologia", "Relacionamentos", "Análise Transacional"],
    ),
    (
        "comunicacao-nao-violenta",
        "Comunicação Não-Violenta",
        "Marshall B. Rosenberg",
        "8571838267",
        "O método CNV de Rosenberg: comunicar-se a partir de observações, sentimentos, necessidades e pedidos — em vez de julgamentos e exigências — para resolver conflitos e criar conexão genuína.",
        ["Comunicação", "Empatia", "Relacionamentos"],
    ),
    (
        "coragem-de-nao-agradar",
        "A Coragem de Não Agradar",
        "Ichiro Kishimi & Fumitake Koga",
        "8543105692",
        "Num diálogo entre filósofo e jovem, os autores apresentam a psicologia de Alfred Adler: a felicidade exige separar suas tarefas das dos outros, abrir mão da aprovação alheia e escolher a liberdade de ser detestado.",
        ["Psicologia", "Filosofia", "Autodesenvolvimento"],
    ),
    (
        "armas-da-persuasao",
        "As Armas da Persuasão",
        "Robert B. Cialdini",
        "8575428098",
        "O clássico da influência. Cialdini revela os seis princípios que nos levam a dizer 'sim' quase no automático — reciprocidade, compromisso, prova social, afeição, autoridade e escassez — e como se defender deles.",
        ["Persuasão", "Psicologia", "Influência"],
    ),
    (
        "nunca-divida-a-diferenca",
        "Nunca Divida a Diferença",
        "Chris Voss",
        "8543108055",
        "As táticas de um ex-negociador de reféns do FBI: empatia tática, espelhamento, rotulagem de emoções e o poder do 'não' — para fechar acordos sem ceder pela metade. (Edição BR: 'Negocie como se sua vida dependesse disso'.)",
        ["Negociação", "Comunicação", "Persuasão"],
    ),
    (
        "conversas-cruciais",
        "Conversas Cruciais",
        "Kerry Patterson e outros",
        "8593585000",
        "Como dialogar quando as opiniões divergem, as emoções pegam fogo e há muito em jogo. Ferramentas para manter o diálogo seguro, falar o que precisa ser dito e transformar discussões tensas em resultados.",
        ["Comunicação", "Conflito", "Liderança"],
    ),
    (
        "escute",
        "Escute!",
        "Kate Murphy",
        "6555646292",
        "Perdemos a arte de ouvir. A jornalista Kate Murphy mostra por que escutar de verdade — não apenas esperar a vez de falar — aprofunda relações, gera ideias e é a habilidade social mais subestimada.",
        ["Comunicação", "Escuta", "Relacionamentos"],
    ),
    (
        "obrigado-pelo-feedback",
        "Obrigado pelo Feedback",
        "Douglas Stone & Sheila Heen",
        "8582850263",
        "Receber feedback bem é uma habilidade — e a mais difícil. Os autores de Harvard mostram por que reagimos mal a críticas e como extrair valor de qualquer retorno, mesmo o injusto ou mal dado.",
        ["Feedback", "Comunicação", "Carreira"],
    ),
    (
        "poder-dos-quietos",
        "O Poder dos Quietos",
        "Susan Cain",
        "8595080747",
        "Num mundo que não para de falar, Susan Cain reabilita os introvertidos: mostra como a quietude alimenta a criatividade e a liderança, e por que metade de nós pensa melhor longe do palco.",
        ["Psicologia", "Introversão", "Comportamento"],
    ),
    (
        "pai-rico-pai-pobre",
        "Pai Rico, Pai Pobre",
        "Robert T. Kiyosaki",
        "8550801488",
        "O best-seller que opõe dois 'pais' e suas filosofias de dinheiro. Kiyosaki defende comprar ativos que geram renda, entender a diferença entre ativo e passivo e buscar a educação financeira que a escola não dá.",
        ["Finanças", "Educação Financeira", "Riqueza"],
    ),
    (
        "segredos-da-mente-milionaria",
        "Os Segredos da Mente Milionária",
        "T. Harv Eker",
        "8575425927",
        "Seu 'modelo de dinheiro' interior determina sua renda. Eker mapeia os arquivos mentais que separam ricos de pobres e propõe declarações e hábitos para reprogramar a relação com a riqueza.",
        ["Finanças", "Mentalidade", "Riqueza"],
    ),
    (
        "investidor-inteligente",
        "O Investidor Inteligente",
        "Benjamin Graham",
        "8595080801",
        "A bíblia do investimento em valor, mestre de Warren Buffett. Graham ensina a diferença entre investir e especular, a margem de segurança e o 'Sr. Mercado' — disciplina contra a emoção das cotações.",
        ["Investimentos", "Finanças", "Clássico"],
    ),
    (
        "do-mil-ao-milhao",
        "Do Mil ao Milhão",
        "Thiago Nigro",
        "8595083274",
        "O Primo Rico destila seu método em três pilares — gastar bem, investir melhor e ganhar mais — para sair do zero e construir patrimônio, com foco na realidade do investidor brasileiro.",
        ["Finanças", "Investimentos", "Brasil"],
    ),
    (
        "quem-pensa-enriquece",
        "Quem Pensa, Enriquece",
        "Napoleon Hill",
        "6587885004",
        "Fruto de 20 anos estudando magnatas, o clássico de Hill destila 13 princípios da riqueza — do desejo ardente à fé, à persistência e à mente mestra — partindo da ideia de que o pensamento se materializa.",
        ["Sucesso", "Mentalidade", "Clássico"],
    ),
    (
        "psicopolitica",
        "Psicopolítica",
        "Byung-Chul Han",
        "8592649390",
        "O neoliberalismo não reprime: seduz. Han mostra como o poder migrou da biopolítica para a psicopolítica — Big Data, transparência e a ilusão de liberdade que nos faz explorar a nós mesmos com prazer.",
        ["Filosofia", "Tecnologia", "Poder"],
    ),
    (
        "realismo-capitalista",
        "Realismo Capitalista",
        "Mark Fisher",
        "6587233090",
        "'É mais fácil imaginar o fim do mundo do que o fim do capitalismo.' Fisher anatomiza a crença de que não há alternativa ao capitalismo e liga essa resignação ao adoecimento mental em massa.",
        ["Filosofia", "Política", "Cultura"],
    ),
    (
        "geracao-ansiosa",
        "A Geração Ansiosa",
        "Jonathan Haidt",
        "8535938532",
        "Haidt liga a epidemia de ansiedade e depressão juvenil à reconfiguração da infância: smartphones e redes sociais substituindo a brincadeira livre. Um alerta e um plano de ação para pais e escolas.",
        ["Psicologia", "Tecnologia", "Educação"],
    ),
    (
        "1984",
        "1984",
        "George Orwell",
        "8535914846",
        "A distopia definitiva: Winston Smith vive sob o Grande Irmão, a vigilância total e a 'novilíngua' que mata o pensamento. Orwell projeta o totalitarismo levado às últimas consequências.",
        ["Distopia", "Política", "Clássico"],
    ),
    (
        "admiravel-mundo-novo",
        "Admirável Mundo Novo",
        "Aldous Huxley",
        "8525056006",
        "Uma distopia oposta à de Orwell: aqui a opressão vem pelo prazer. Bebês produzidos em série, castas, sexo livre e a droga 'soma' garantem uma felicidade rasa — e a liberdade trocada por conforto.",
        ["Distopia", "Ficção Científica", "Clássico"],
    ),
    (
        "21-licoes",
        "21 Lições para o Século 21",
        "Yuval Noah Harari",
        "8535930914",
        "Depois de explorar o passado e o futuro, Harari encara o presente: IA, fake news, terrorismo, crise de sentido e religião — 21 ensaios sobre como navegar a confusão das próximas décadas.",
        ["Sociedade", "Tecnologia", "Futuro"],
    ),
    (
        "amor-liquido",
        "Amor Líquido",
        "Zygmunt Bauman",
        "8571107955",
        "Bauman diagnostica o amor na 'modernidade líquida': laços frágeis e descartáveis, relações 'até segunda ordem' e o medo de se comprometer num mundo de vínculos sob demanda.",
        ["Sociologia", "Relacionamentos", "Modernidade"],
    ),
    (
        "sete-saberes",
        "Os Sete Saberes Necessários à Educação do Futuro",
        "Edgar Morin",
        "8524917547",
        "Encomendado pela UNESCO, Morin propõe sete saberes que a educação ignora — do conhecimento do erro à compreensão humana e à ética do gênero humano — para formar mentes capazes de enfrentar a complexidade.",
        ["Educação", "Filosofia", "Complexidade"],
    ),
    (
        "cabeca-bem-feita",
        "A Cabeça Bem-Feita",
        "Edgar Morin",
        "852860764X",
        "Vale mais uma cabeça bem-feita que uma cabeça cheia. Morin critica a fragmentação do saber e defende uma reforma do pensamento que religue as disciplinas e ensine a contextualizar.",
        ["Educação", "Filosofia", "Complexidade"],
    ),
    (
        "pensamento-complexo",
        "Introdução ao Pensamento Complexo",
        "Edgar Morin",
        "8520505988",
        "O manifesto do pensamento complexo: contra a simplificação que isola e reduz, Morin propõe religar o que foi separado e conviver com a incerteza, a contradição e o todo que é mais que a soma das partes.",
        ["Filosofia", "Complexidade", "Epistemologia"],
    ),
    (
        "coisa-de-rico",
        "Coisa de Rico",
        "Michel Alcoforado",
        "6556928585",
        "O 'antropólogo do luxo' Michel Alcoforado decifra os códigos secretos dos ricos brasileiros: como se vestem, gastam, herdam e se distinguem. Uma etnografia bem-humorada das regras invisíveis da elite nacional.",
        ["Sociedade", "Antropologia", "Brasil"],
    ),
    (
        "insustentavel-leveza-do-ser",
        "A Insustentável Leveza do Ser",
        "Milan Kundera",
        "8535912517",
        "Em Praga, sob a invasão soviética de 1968, quatro amantes encarnam o peso e a leveza da existência. Kundera tece filosofia (o eterno retorno, o kitsch) e romance num clássico do século 20.",
        ["Literatura", "Filosofia", "Romance"],
    ),
]


def _get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def _try_save(data, slug):
    if not data or len(data) < MIN_BYTES:
        return False
    try:
        im = Image.open(io.BytesIO(data)).convert("RGB")
    except Exception:
        return False
    if im.width < 150 or im.height < 200:  # placeholder/ícone, não é capa
        return False
    if im.height > 900:
        im = im.resize((round(im.width * 900 / im.height), 900), Image.LANCZOS)
    out = os.path.join(ASSETS, f"{slug}-cover.png")
    os.makedirs(ASSETS, exist_ok=True)
    im.save(out, "PNG")
    return (im.width, im.height)


def baixar_capa(slug, asin):
    urls = [
        f"https://m.media-amazon.com/images/P/{asin}.01._SCLZZZZZZZ_.jpg",
        f"https://images-na.ssl-images-amazon.com/images/P/{asin}.01._SCLZZZZZZZ_.jpg",
        f"https://covers.openlibrary.org/b/isbn/{asin}-L.jpg?default=false",
    ]
    for url in urls:
        try:
            res = _try_save(_get(url), slug)
            if res:
                return res, url
        except Exception:
            continue
    return None, None


def main():
    books = json.loads(open(BOOKS, encoding="utf-8").read())
    existing = {b["id"] for b in books}
    afil = json.loads(open(AFIL, encoding="utf-8").read())
    afil.setdefault("asins", {})

    novos, faltou_capa = 0, []
    for slug, title, author, asin, desc, tags in CANDIDATOS:
        afil["asins"][slug] = asin  # link direto /dp/ no gerar_links.py

        if slug in existing:
            print(f"[=] já existe, pulando: {slug}")
            continue

        res, src = baixar_capa(slug, asin)
        if res:
            origem = "amazon" if "amazon" in src else "openlibrary"
            print(f"[OK] {slug}: capa {res[0]}x{res[1]} ({origem})")
        else:
            faltou_capa.append(slug)
            print(f"[!!] {slug}: SEM CAPA (asin {asin}) — verificar manualmente")

        books.append(
            {
                "id": slug,
                "title": title,
                "author": author,
                "coverUrl": f"assets/{slug}-cover.png",
                "description": desc,
                "tags": tags,
                "progress": "Em breve",
                "comingSoon": True,
            }
        )
        novos += 1

    open(BOOKS, "w", encoding="utf-8").write(json.dumps(books, ensure_ascii=False, indent=2))
    open(AFIL, "w", encoding="utf-8").write(json.dumps(afil, ensure_ascii=False, indent=2))

    print(f"\n{novos} card(s) novo(s) inserido(s). {len(afil['asins'])} ASIN(s) no afiliados.json.")
    if faltou_capa:
        print("CAPAS QUE FALHARAM (trocar ASIN ou baixar manual):", ", ".join(faltou_capa))
    print("\nAgora rode:  python afiliados/gerar_links.py")


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    main()
