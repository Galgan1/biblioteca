# -*- coding: utf-8 -*-
"""Conteúdo (pt-BR) de 'Blender 3D: Noob to Pro' (Wikibooks) — CC-BY-SA.
Fonte: https://en.wikibooks.org/wiki/Blender_3D:_Noob_to_Pro — cheat-sheet derivado, mesma licença."""

BOOK = {
 "title": "Blender 3D: Noob to Pro",
 "author": "Wikibooks (comunidade)",
 "header_light": "NOOB",
 "header_bold": "TO PRO",
 "subtitle": "VISÃO GERAL · A TRILHA DO INICIANTE AO INTERMEDIÁRIO",
 "intro": "O livro-trilha mais conhecido para aprender Blender do zero. Onde o manual é referência, o 'Noob to Pro' é caminho: ensina a ORDEM e o PORQUÊ — coordenadas, navegação, modelagem por projetos, materiais, UV e animação — sem pular degraus. Cheat-sheet pt-BR sob CC-BY-SA.",
 "description": "Trilha de aprendizado de Blender do Wikibooks (CC-BY-SA): fundamentos de 3D, navegação, Object/Edit Mode, extrusão e loop cut, normais e smooth shading, materiais × texturas, UV unwrap e animação por keyframes. O complemento didático do manual — a sequência e o 'porquê'.",
 "tags": ["Blender", "Aprendizado", "Tutorial"],
 "progress": "3 Capítulos",
 "cover": "assets/blender-noob-to-pro-cover.png",
 "overview_cards": [
   {"ic":"book","t":"Fundamentos antes do clique","b":"O livro insiste: <strong>entenda coordenadas XYZ, espaço local × global e projeção ortográfica × perspectiva ANTES de modelar.</strong> Sem o vocabulário mental, cada comando vira magia negra.","tip":"<strong>Metáfora do livro:</strong> não dá pra pilotar sem entender os instrumentos."},
   {"ic":"layers","t":"Aprenda na ORDEM certa","b":"Cada lição pressupõe a anterior: você não aprende UV antes de saber o que é uma face. <strong>É essa sequência por dependência que o manual (referência pura) não te dá.</strong>","tip":"<strong>Modelo mental:</strong> referência responde 'o quê'; trilha responde 'quando' e 'por quê'.","wide":True},
   {"ic":"spark","t":"Projetos concretos","b":"Casa, chapéu, taça, personagem com ossos. <strong>Cada conceito é ancorado num objeto real</strong> — não numa explicação abstrata de parâmetro. Você erra fazendo, e aprende.","tip":"<strong>Prática:</strong> termine cada mini-projeto antes de avançar."},
   {"ic":"mask","t":"Ressalva honesta de versão","b":"Por ser wiki comunitária, <strong>muitos tutoriais foram escritos p/ Blender 2.4–2.7</strong> (antes do redesign do 2.8+). Os conceitos valem; <strong>os atalhos e menus precisam de conferência na versão atual.</strong>","tip":"<strong>Regra:</strong> confie no conceito, valide o atalho no Blender que você usa.","warn":True},
 ],
}

CHAPTERS = [
 {"slug":"ch01-fundamentos-navegacao","sub":"CAPÍTULO 1: Fundamentos e Navegação",
  "intro":"Antes da geometria, o terreno mental: espaço 3D, vistas e o fluxo Object↔Edit que sustenta tudo.",
  "cards":[
    {"ic":"target","t":"Coordenadas e Espaços","emph":"XYZ","b":"<strong>X, Y, Z; espaço global × local; ortográfico × perspectiva.</strong> Um objeto rotacionado tem eixos locais diferentes dos globais — entender isso evita que mover/girar pareça aleatório.","tip":"<strong>Base:</strong> sem este vocabulário, nenhum transform faz sentido."},
    {"ic":"eye","t":"Navegar a viewport","emph":"Navegação","b":"Girar (botão do meio), pan (Shift+meio), zoom (scroll), Numpad p/ vistas fixas. <strong>Fluência aqui vale mais que qualquer ferramenta</strong> — sem ela, todo trabalho trava.","tip":"<strong>Prática:</strong> decore Numpad 1/3/7 (frente/lado/topo) e 5 (orto↔persp)."},
    {"ic":"layers","t":"TAB: Object × Edit","emph":"TAB","b":"Object Mode move o objeto inteiro; Edit Mode expõe vértices/arestas/faces. <strong>A troca (TAB) define o fluxo inteiro de modelagem.</strong> Os 3 modos de seleção (1/2/3) resolvem problemas diferentes.","tip":"<strong>Modelo mental:</strong> 'estou editando o objeto ou a geometria dele?'"},
   ],
  "lessons_title":"Lições-Chave do Capítulo 1",
  "lessons":["Domine coordenadas e espaços antes de modelar.","Navegação fluida da viewport é pré-requisito de tudo.","TAB (Object↔Edit) é a distinção mais fundamental do Blender."]},

 {"slug":"ch02-modelagem-materiais","sub":"CAPÍTULO 2: Modelagem e Materiais",
  "intro":"O verbo é extrudar. Aqui o iniciante constrói formas reais e aprende a diferença entre material e textura.",
  "cards":[
    {"ic":"spark","t":"Extrude é o verbo","emph":"Extrude (E)","b":"<strong>E</strong> cria geometria nova a partir da existente — é o movimento mais usado da modelagem (a casa, o telhado, tudo nasce dele). Combine com mesclar vértices p/ fechar formas.","tip":"<strong>Ciclo:</strong> selecionar → Edit → selecionar componente → agir (E, etc.)."},
    {"ic":"layers","t":"Normais + Smooth Shading","emph":"Normais","b":"<strong>Smooth Shading não adiciona geometria — interpola as normais</strong> p/ um cubo de poucos polígonos parecer liso. Normais invertidas causam sombra errada: <strong>Ctrl+N</strong> recalcula.","tip":"<strong>Ilusão-chave:</strong> low-poly + smooth shading = curva sem peso de geometria."},
    {"ic":"bubble","t":"Material × Textura","emph":"Material × Textura","b":"<strong>Material</strong> = propriedades da superfície (cor, brilho, reflexo). <strong>Textura</strong> = o detalhe que modifica o material (procedural ou imagem). Saber qual você está editando evita confusão clássica.","tip":"<strong>Regra:</strong> textura sem material não existe; ela é um modificador do material."},
   ],
  "lessons_title":"Lições-Chave do Capítulo 2",
  "lessons":["Extrude (E) é o movimento central da modelagem.","Smooth shading interpola normais — suaviza sem adicionar geometria.","Material define a superfície; textura é o detalhe que a modifica."]},

 {"slug":"ch03-uv-animacao","sub":"CAPÍTULO 3: UV, Animação e o Salto Pro",
  "intro":"Para texturas reais e movimento com alma: desdobrar o modelo e animar por keyframes com curvas.",
  "cards":[
    {"ic":"book","t":"UV Unwrap","emph":"UV","b":"Para colar uma foto numa superfície sem distorção, o modelo é <strong>'desdobrado' como uma caixa de papelão: marcar seams → Unwrap → ajustar as ilhas</strong> no UV Editor. É o passaporte para texturas reais.","tip":"<strong>Sem UV bom:</strong> imagens esticam e repetem feio."},
    {"ic":"target","t":"Keyframe + Graph Editor","emph":"Keyframe (I)","b":"<strong>I</strong> grava posição/rotação/escala num momento; o Blender interpola o resto. O <strong>Graph Editor (FCurves)</strong> ajusta a velocidade de entrada/saída — é o que troca o 'movimento robótico' linear por movimento orgânico.","tip":"<strong>Premium:</strong> curva suave (ease) > interpolação linear pura."},
    {"ic":"spark","t":"O salto para Pro","emph":"Nodes + Rigging","b":"O intermediário vira avançado com <strong>Node Editor</strong> (materiais/composição modulares), <strong>Cycles</strong> (luz física, GI grátis) e <strong>rigging</strong> (armature + weight paint). É a porta do pipeline profissional.","tip":"<strong>Trilha:</strong> nodes e rigging são o degrau Noob→Pro de verdade."},
   ],
  "lessons_title":"Lições-Chave do Capítulo 3",
  "lessons":["UV unwrap (seams→unwrap→ilhas) é pré-requisito de texturas reais.","Keyframe + Graph Editor dão movimento orgânico, não robótico.","Nodes, Cycles e rigging marcam o salto para o nível profissional."]},
]
