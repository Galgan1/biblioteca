# -*- coding: utf-8 -*-
"""Conteúdo (pt-BR) de 'Blender Fundamentals' (Blender Foundation) — CC-BY 4.0.
Fonte: https://studio.blender.org/training/blender-fundamentals-45-lts/ — cheat-sheet derivado."""

BOOK = {
 "title": "Blender Fundamentals",
 "author": "Blender Foundation",
 "header_light": "BLENDER",
 "header_bold": "FUNDAMENTALS",
 "subtitle": "VISÃO GERAL · O CURSO OFICIAL DE FUNDAMENTOS",
 "intro": "O curso gratuito de fundamentos da própria Blender Foundation: a forma 'certa' de aprender, dos atalhos essenciais ao workflow de produção (modelar → texturizar → iluminar → renderizar → compor). Cheat-sheet pt-BR derivado do material oficial sob CC-BY 4.0.",
 "description": "Resumo do curso oficial Blender Fundamentals (Blender Foundation, CC-BY 4.0): primeiros passos e atalhos, modelagem, shading com Principled BSDF, iluminação de três pontos, render Cycles × EEVEE e o workflow de produção recomendado. As boas práticas oficiais da casa.",
 "tags": ["Blender", "Curso", "Oficial"],
 "progress": "3 Capítulos",
 "cover": "assets/blender-fundamentals-cover.png",
 "overview_cards": [
   {"ic":"target","t":"O workflow de produção","b":"A ordem oficial: <strong>Modelagem → Texturização → Shading → Rigging → Animação → Iluminação → Render → Compositing.</strong> Cada Workspace do Blender corresponde a uma etapa — siga a esteira.","tip":"<strong>Modelo mental:</strong> produção é linha de montagem; pule etapa e retrabalha.","wide":True},
   {"ic":"spark","t":"F3 é a rota de fuga","b":"Não decore menus: <strong>aperte F3 e busque o comando pelo nome</strong> ('bevel', 'shade smooth'). É o atalho que destrava qualquer função quando você sabe o que quer, mas não onde fica.","tip":"<strong>Produtividade:</strong> F3 > caçar em submenu."},
   {"ic":"eye","t":"Cycles × EEVEE","b":"<strong>Cycles</strong> = path tracer físico (lento, foto-realista). <strong>EEVEE</strong> = tempo real (rápido, ótimo p/ preview e estilizado). O curso ensina os dois — escolha pela necessidade.","tip":"<strong>Regra:</strong> EEVEE p/ iterar/preview; Cycles p/ a entrega final."},
   {"ic":"mask","t":"Nunca renderize direto p/ .mp4","b":"A prática oficial: <strong>renderize a animação para uma SEQUÊNCIA de imagens (PNG/EXR), nunca direto para .mp4.</strong> Um crash no meio invalida o vídeo inteiro; a sequência preserva cada frame.","tip":"<strong>Depois:</strong> monte o filme no Video Sequencer (com áudio).","warn":True},
 ],
}

CHAPTERS = [
 {"slug":"ch01-primeiros-passos","sub":"CAPÍTULO 1: Primeiros Passos e Atalhos",
  "intro":"A base oficial: interface, navegação e os atalhos que fazem o Blender fluir.",
  "cards":[
    {"ic":"layers","t":"Os atalhos essenciais","emph":"G / R / S","b":"<strong>G mover, R rotacionar, S escalar — adicione X/Y/Z para travar no eixo.</strong> TAB troca de modo; A seleciona tudo; B/C são box/circle select. Esses poucos atalhos cobrem 80% do trabalho.","tip":"<strong>Confirme com Enter, cancele com Esc</strong> durante o transform."},
    {"ic":"eye","t":"Navegação e vistas","emph":"Numpad","b":"Scroll = zoom; <strong>Numpad 1/3/7 = frente/lado/topo; 5 = orto↔perspectiva; 0 = câmera ativa.</strong> O pie menu (~) dá acesso rápido às vistas e ao shading.","tip":"<strong>Vistas ortográficas</strong> são essenciais para modelar com precisão."},
    {"ic":"book","t":"Collections e Workspaces","emph":"Organização","b":"<strong>Use Collections (M) para agrupar objetos e Workspaces para cada etapa</strong> (Layout, Modeling, Shading, Render...). Nomeie tudo desde o início — cena organizada é cena que escala.","tip":"<strong>Hábito oficial:</strong> nada de 'Cube.001, Cube.002' largados na cena."},
   ],
  "lessons_title":"Lições-Chave do Capítulo 1",
  "lessons":["G/R/S (+X/Y/Z) e TAB cobrem a maior parte do trabalho.","Numpad para vistas ortográficas e câmera é essencial.","Collections + Workspaces mantêm a cena organizada e escalável."]},

 {"slug":"ch02-modelagem-shading","sub":"CAPÍTULO 2: Modelagem e Shading",
  "intro":"Construir a forma e dar superfície: as ferramentas de mesh e o shader padrão da casa.",
  "cards":[
    {"ic":"spark","t":"Ferramentas de mesh","emph":"E / Ctrl+R / Ctrl+B","b":"<strong>Extrude (E), Loop Cut (Ctrl+R), Bevel (Ctrl+B), Knife (K), Inset (I).</strong> Esse punhado de ferramentas resolve a maior parte da modelagem hard-surface que uma cena de produto precisa.","tip":"<strong>Topologia limpa</strong> desde o início evita dor no shading e na animação."},
    {"ic":"bubble","t":"Principled BSDF (oficial)","emph":"PBR","b":"O shader padrão combina <strong>albedo, roughness, metalness e normal</strong> num nó só (modelo OpenPBR). É o caminho oficial p/ materiais realistas — domine-o antes de partir p/ nós complexos.","tip":"<strong>Ordem:</strong> Base Color → Roughness → Metallic; o resto é refino."},
    {"ic":"book","t":"UV antes de texturizar","emph":"UV Unwrap","b":"O fluxo oficial: <strong>marcar seams logicamente → Unwrap → compactar ilhas p/ minimizar distorção → só então texturizar.</strong> Pular o UV é a causa nº1 de textura esticada.","tip":"<strong>Regra:</strong> UV é parte da modelagem, não um detalhe do fim."},
   ],
  "lessons_title":"Lições-Chave do Capítulo 2",
  "lessons":["Um punhado de ferramentas (E/Ctrl+R/Ctrl+B/K/I) cobre a modelagem.","Principled BSDF é o caminho oficial para materiais PBR.","Faça o UV unwrap ANTES de texturizar."]},

 {"slug":"ch03-luz-render-producao","sub":"CAPÍTULO 3: Luz, Render e Produção",
  "intro":"Fechar com qualidade: três pontos de luz, o motor certo e as práticas de produção da Blender Foundation.",
  "cards":[
    {"ic":"eye","t":"Iluminação de três pontos","emph":"Key/Fill/Rim","b":"A técnica-base oficial: <strong>key (principal), fill (preenche a sombra) e rim (separa do fundo).</strong> Tipos de luz: Point, Sun, Spot, Area — a Area dá a sombra suave de estúdio.","tip":"<strong>Comece pela key</strong>, depois alivie a sombra com o fill, por último separe com o rim."},
    {"ic":"target","t":"Render + Denoising","emph":"Cycles","b":"No Cycles, <strong>ative sempre o Denoising</strong> p/ obter imagem limpa com menos samples — economiza muito tempo. Defina resolução e formato no painel de Output.","tip":"<strong>Entrega:</strong> EXR 32-bit p/ compositing; PNG p/ frames finais."},
    {"ic":"mask","t":"Compositor + Sequencer","emph":"Pós-produção","b":"O Blender fecha o ciclo: <strong>o Compositor processa cada frame (cor, glare, grade) e o Video Sequencer monta o filme final com áudio</strong> — tudo sem sair do software.","tip":"<strong>Prática oficial:</strong> render → sequência de imagens → compositor → sequencer."},
   ],
  "lessons_title":"Lições-Chave do Capítulo 3",
  "lessons":["Iluminação de três pontos (key/fill/rim) é a base oficial.","Ative Denoising no Cycles para limpar com menos samples.","Compositor (por frame) + Video Sequencer (montagem) fecham a produção."]},
]
