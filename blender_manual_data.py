# -*- coding: utf-8 -*-
"""Conteúdo (pt-BR) do 'Blender Manual' (Blender Foundation) — CC-BY-SA 4.0.
Fonte: https://docs.blender.org/manual/ — cheat-sheet derivado, mesma licença."""

BOOK = {
 "title": "Blender Manual Oficial",
 "author": "Blender Foundation",
 "header_light": "BLENDER",
 "header_bold": "MANUAL",
 "subtitle": "VISÃO GERAL · A REFERÊNCIA DO 3D LIVRE",
 "intro": "O manual oficial do Blender é a referência canônica do software de 3D livre mais usado do mundo: modelagem, materiais físicos (Principled BSDF), iluminação, câmera, o motor Cycles e a API Python (bpy) para automação. Esta é uma referência rápida pt-BR, derivada do manual sob CC-BY-SA 4.0.",
 "description": "Referência rápida do Blender Manual oficial (CC-BY-SA): modelagem e modificadores, Principled BSDF, HDRI e luzes, câmera e profundidade de campo, Cycles/GPU OptiX, color management AgX e a API Python (bpy) para render headless. Conteúdo livre, com atribuição à Blender Foundation.",
 "tags": ["Blender", "3D", "Referência"],
 "progress": "4 Capítulos",
 "cover": "assets/blender-manual-cover.png",
 "overview_cards": [
   {"ic":"layers","t":"Tudo é Data-block","b":"O Blender organiza cena em <em>data-blocks</em>: um Objeto referencia uma Mesh, um Material, etc. <strong>Em produção headless você quase sempre importa geometria pronta e edita por script (bpy), não modela à mão.</strong>","tip":"<strong>Modelo mental:</strong> objeto = ponteiro; o dado (mesh/material) vive separado e é reaproveitável."},
   {"ic":"spark","t":"Principled BSDF: 1 shader p/ tudo","b":"Um único shader PBR cobre plástico, metal, vidro e papel. <strong>Os botões que importam: Base Color, Roughness, Metallic, Specular IOR Level e Coat (verniz).</strong> Capa fosca = rough alto; brilhante = rough baixo + Coat.","tip":"<strong>Regra:</strong> textura de cor = colorspace sRGB; normal/roughness = Non-Color."},
   {"ic":"eye","t":"Luz vem do mundo (HDRI)","b":"Iluminação realista = um HDRI no World (Environment Texture) + luzes de área. <strong>Sombra suave vem do TAMANHO da luz, não da potência.</strong> Truque de estúdio: a câmera vê fundo escuro, mas os reflexos usam o HDRI.","tip":"<strong>Fonte CC0 de HDRI:</strong> Poly Haven (uso comercial liberado).","wide":True},
   {"ic":"target","t":"Cycles + OptiX + AgX","b":"<strong>Cycles</strong> é o motor físico (path tracer); na GPU NVIDIA use <strong>OptiX</strong> (bem mais rápido) + <strong>denoiser</strong> p/ baixar samples. Cor sempre em <strong>AgX</strong> (Blender 4.x) para foto-realismo sem estouro.","tip":"<strong>Headless:</strong> ative a GPU no bpy na ordem certa, senão o render cai pra CPU.","warn":True},
 ],
}

CHAPTERS = [
 {"slug":"ch01-modelagem-modificadores","sub":"CAPÍTULO 1: Modelagem e Modificadores",
  "intro":"A base geométrica. Em produção, o segredo é não modelar do zero: importar e refinar com modificadores não-destrutivos.",
  "cards":[
    {"ic":"layers","t":"Object Mode × Edit Mode","emph":"TAB","b":"<strong>TAB</strong> alterna entre mover/escalar o objeto inteiro (Object) e editar vértices/arestas/faces (Edit). É a distinção mais fundamental do Blender — todo o fluxo gira em torno dela.","tip":"<strong>Em script:</strong> evite Edit Mode; opere a mesh por dados (bpy) sempre que possível."},
    {"ic":"spark","t":"Bevel mata o 'CG barato'","emph":"Bevel","b":"Arestas perfeitamente vivas denunciam render amador. <strong>O modificador Bevel (width ~0,0025, segments 3) arredonda de leve as arestas e captura um brilho fino</strong> — o detalhe que separa premium de plástico.","tip":"<strong>Não-destrutivo:</strong> o modificador fica no topo da pilha; edite a base e o Blender recalcula."},
    {"ic":"target","t":"Subdivision Surface","emph":"Subdivisão","b":"Subdivide a malha suavizando a forma sem você modelar curva por curva. <strong>Use levels 1 na viewport e 2 no render</strong> para leveza ao editar e qualidade ao entregar.","tip":"<strong>Modelo mental:</strong> você esculpe a gaiola simples; o modificador gera a superfície lisa."},
   ],
  "lessons_title":"Lições-Chave do Capítulo 1",
  "lessons":["Importe geometria pronta; refine com modificadores não-destrutivos.","TAB (Object↔Edit) organiza todo o fluxo de modelagem.","Bevel sutil nas arestas é o detalhe que eleva o realismo."]},

 {"slug":"ch02-materiais-principled-bsdf","sub":"CAPÍTULO 2: Materiais — Principled BSDF",
  "intro":"Um shader físico só, controlado por poucos parâmetros, faz qualquer superfície convincente.",
  "cards":[
    {"ic":"spark","t":"Roughness é o rei","emph":"Roughness","b":"De 0 (espelho) a 1 (fosco total), o <strong>Roughness define como a luz espalha</strong> — é o parâmetro que mais muda a leitura do material. Papel fosco ~0,7; verniz ~0,05.","tip":"<strong>Dica:</strong> quase nada no mundo real é 0 ou 1; fuja dos extremos."},
    {"ic":"bubble","t":"Metallic é binário","emph":"Metallic","b":"<strong>Metallic é 0 (dielétrico: plástico, papel, pele) ou 1 (metal puro) — raramente meio-termo.</strong> Em metal, a Base Color vira a cor do reflexo. Misturar valores intermediários costuma ser erro.","tip":"<strong>Regra PBR:</strong> decida primeiro 'é metal ou não?' e só então ajuste rugosidade."},
    {"ic":"book","t":"Textura por nó","emph":"Image Texture","b":"Conecte <strong>UV → Image Texture → Base Color → BSDF → Output</strong>. A imagem da capa vira a cor da superfície. <strong>Colorspace sRGB para cor; Non-Color para mapas técnicos</strong> (normal, roughness).","tip":"<strong>Alpha (recorte):</strong> ligue a saída Alpha do nó ao Alpha do BSDF — é assim que um billboard recortado funciona no Cycles."},
   ],
  "lessons_title":"Lições-Chave do Capítulo 2",
  "lessons":["Roughness é o parâmetro de maior impacto visual.","Metallic é praticamente binário (0 ou 1).","Texturas entram por nós; cuidado com o colorspace (sRGB × Non-Color)."]},

 {"slug":"ch03-luz-camera","sub":"CAPÍTULO 3: Iluminação e Câmera",
  "intro":"Render bom é 80% luz e enquadramento. HDRI para ambiente, luzes de área para controle, câmera de fotógrafo.",
  "cards":[
    {"ic":"eye","t":"HDRI + 3 pontos","emph":"Iluminação","b":"Um HDRI de estúdio ilumina e dá reflexos naturais; complemente com <strong>key + fill + rim</strong> (3 pontos) para controle. <strong>Luz maior = sombra mais suave.</strong> Proporção clássica Key:Fill ~ 3:1.","tip":"<strong>Estúdio limpo:</strong> esconda o HDRI da câmera (Light Path) e deixe-o só nos reflexos."},
    {"ic":"target","t":"Lente de produto: 85mm","emph":"85mm","b":"Distâncias focais longas (85–100mm) <strong>achatam a perspectiva e valorizam o objeto sem distorção</strong>. Grande-angular (<35mm) deforma produto. Sensor 36mm (full-frame).","tip":"<strong>Enquadramento:</strong> regra dos terços + leve inclinação dão tridimensionalidade."},
    {"ic":"mask","t":"Profundidade de Campo","emph":"DoF","b":"Ative DoF, aponte o <strong>focus_object</strong> ao herói e escolha o f-stop: <strong>f/5.6–8 deixa o produto inteiro nítido; f/2.8 cria bokeh</strong> e separa do fundo. f/1.4 em produto exagera e parece erro.","tip":"<strong>Premium:</strong> fundo desfocado + objeto nítido = leitura instantânea do herói."},
   ],
  "lessons_title":"Lições-Chave do Capítulo 3",
  "lessons":["HDRI para ambiente + 3 pontos para controle; tamanho da luz controla a sombra.","85mm + sensor full-frame é a lente de produto.","DoF com foco no herói e f-stop adequado separa o objeto do fundo."]},

 {"slug":"ch04-cycles-python-headless","sub":"CAPÍTULO 4: Cycles, Cor e Python (Headless)",
  "intro":"O motor físico + a API bpy permitem renderizar cenas inteiras por linha de comando, sem abrir a interface.",
  "cards":[
    {"ic":"target","t":"GPU OptiX na ordem certa","emph":"GPU","b":"No headless, ativar a GPU exige ordem: <strong>compute_device_type='OPTIX' → get_devices() → habilitar cada device</strong>. Fora dessa ordem, o Blender silenciosamente cai pra CPU.","tip":"<strong>OptiX</strong> usa os RT/Tensor cores: 40–80% mais rápido que CUDA + denoiser por IA.","warn":True},
    {"ic":"spark","t":"AgX: cor de cinema","emph":"AgX","b":"O <strong>AgX</strong> (padrão do Blender 4.x) comprime os altos como uma câmera real — sem estourar branco nem desbotar cores saturadas. <strong>Nunca entregue em 'Standard'.</strong>","tip":"<strong>Workflow:</strong> ajuste a EXPOSIÇÃO, não troque o look, para corrigir brilho."},
    {"ic":"book","t":"bpy + --background","emph":"Headless","b":"<strong>blender --background --python script.py</strong> renderiza sem GUI. O script cria cena, materiais, luz, câmera e dá render — perfeito para automação por livro.","tip":"<strong>Produção:</strong> renderize para sequência de imagens (PNG/EXR), nunca direto p/ .mp4 (um crash não perde tudo)."},
   ],
  "lessons_title":"Lições-Chave do Capítulo 4",
  "lessons":["Ativar GPU OptiX no bpy exige a ordem correta, senão cai pra CPU.","AgX é obrigatório para foto-realismo; ajuste exposição, não o look.","bpy + --background automatiza render de cenas inteiras."]},
]
