# -*- coding: utf-8 -*-
"""Strings CSS/JS do carrossel, extraídas de gerar_carrossel.py.

Exporta:
  CSS       — estilos do carrossel feed (1080x1350)
  _FIT_JS   — JavaScript de auto-fit (encolhe para caber, nunca trunca)
  STORY_CSS — estilos dos stories (1080x1920)
"""
import tokens  # fonte única de tokens (fontes + cores) — Diretor de Design

CSS = tokens.TOKENS + """
*{margin:0;padding:0;box-sizing:border-box}
body{background:#000;font-family:'Hanken Grotesk',system-ui,sans-serif;
  -webkit-font-smoothing:antialiased;text-rendering:geometricPrecision}

/* ---------- base do slide: profundidade em camadas ---------- */
.slide{width:1080px;height:1350px;color:var(--ink);padding:92px 90px 150px;
  display:flex;flex-direction:column;position:relative;overflow:hidden;
  background:
   radial-gradient(135% 95% at 102% 108%, oklch(24% 0.045 152 / .85) 0%, transparent 48%),
   radial-gradient(115% 72% at 50% -12%, oklch(27% 0.05 152) 0%, transparent 60%),
   radial-gradient(150% 125% at 50% 48%, transparent 52%, oklch(5% 0.012 152 / .6) 100%),
   linear-gradient(177deg, var(--bg) 0%, var(--bg2) 100%);}
/* textura: grade de pontos finos (fade do topo) */
.slide::before{content:'';position:absolute;inset:0;pointer-events:none;
  background-image:radial-gradient(oklch(78% 0.07 152 / .055) 1.1px, transparent 1.3px);
  background-size:36px 36px;background-position:center;
  -webkit-mask-image:radial-gradient(125% 105% at 50% -5%, #000 50%, transparent 100%);}
/* moldura tracejada (DNA cheat sheet), refinada + halo interno */
.slide::after{content:'';position:absolute;inset:38px;border:2px dashed var(--green);
  border-radius:32px;opacity:.38;pointer-events:none;
  box-shadow:inset 0 0 90px oklch(70% 0.13 152 / .05)}
/* numeral-fantasma de fundo (contido pela moldura p/ não virar artefato) */
.slide>*{position:relative;z-index:1}
.slide>.ghost{position:absolute;font-family:'Hanken Grotesk';font-weight:900;line-height:.74;
  color:transparent;-webkit-text-stroke:2px oklch(74% 0.09 152 / .10);
  pointer-events:none;letter-spacing:-.05em;z-index:0;-webkit-user-select:none;overflow:hidden;
  -webkit-mask-image:radial-gradient(120% 120% at 50% 50%, #000 60%, transparent 100%)}
/* indicador de progresso */
.dots{position:absolute;left:0;right:0;bottom:74px;display:flex;gap:13px;
  justify-content:center;align-items:center;z-index:2}
.dots i{width:11px;height:11px;border-radius:999px;background:var(--hair);
  display:block;transition:none}
.dots i.on{width:38px;background:var(--green);
  box-shadow:0 0 18px oklch(72% 0.14 152 / .55)}
.wm{position:absolute;left:0;right:0;bottom:40px;text-align:center;font-weight:800;
  letter-spacing:.26em;font-size:21px;color:var(--ink-dim);text-transform:uppercase;z-index:2}

/* ---------- topbar (slides de conceito) ---------- */
.topbar{display:flex;justify-content:space-between;align-items:center}
.brandmark{display:inline-flex;align-items:center;gap:12px;font-weight:900;
  letter-spacing:.03em;font-size:28px;color:var(--ink);text-transform:uppercase}
.brandmark .seal{width:46px;height:46px;border-radius:13px;display:flex;align-items:center;
  justify-content:center;background:var(--green);color:var(--on-green);flex:0 0 auto}
.brandmark .seal svg{width:28px;height:28px;color:var(--on-green)}
.brandmark b{color:var(--green);font-weight:900}

/* ---------- selo do ícone ---------- */
.card-icon{width:108px;height:108px;border-radius:26px;display:flex;align-items:center;
  justify-content:center;margin:46px 0 28px;
  background:linear-gradient(160deg, oklch(70% 0.14 152 / .16), oklch(70% 0.14 152 / .04));
  border:2px solid var(--hair);
  box-shadow:0 0 48px oklch(70% 0.14 152 / .14), inset 0 1px 0 oklch(90% 0.1 152 / .12)}
.card-icon svg{width:58px;height:58px;color:var(--green);
  filter:drop-shadow(0 0 12px oklch(72% 0.14 152 / .45))}
.warn .card-icon{background:linear-gradient(160deg, oklch(75% 0.16 30 / .16), oklch(75% 0.16 30 / .04));
  border-color:oklch(75% 0.16 30 / .42);box-shadow:0 0 48px oklch(75% 0.16 30 / .14)}
.warn .card-icon svg{color:var(--warn);filter:drop-shadow(0 0 12px oklch(75% 0.16 30 / .45))}

/* ---------- conceito ---------- */
.card-title{display:inline-block;background:var(--green);color:var(--on-green);
  font-weight:800;font-size:52px;line-height:1.12;padding:15px 30px;border-radius:16px;
  text-transform:uppercase;text-wrap:balance;align-self:flex-start;letter-spacing:.004em;
  box-shadow:0 14px 40px oklch(60% 0.14 152 / .3)}
.warn .card-title{background:var(--warn);color:var(--on-warn);
  box-shadow:0 14px 40px oklch(65% 0.16 30 / .3)}
.card-body{font-size:45px;line-height:1.4;color:var(--ink);margin-top:28px;
  font-weight:500;text-wrap:pretty}
.card-body strong{color:var(--green-soft);font-weight:800}
.warn .card-body strong{color:var(--warn)}
.card-tip{display:flex;gap:20px;align-items:flex-start;font-size:31px;line-height:1.36;
  color:var(--green-soft);margin-top:auto;margin-bottom:8px;border-top:2px dashed var(--green);
  padding-top:30px;font-weight:500;text-wrap:pretty}
.card-tip .tipic{flex:0 0 auto;width:42px;height:42px;margin-top:2px;color:var(--green)}
.card-tip .tipic svg{width:42px;height:42px}
.card-tip strong{color:var(--green);font-weight:800}
.warn .card-tip{color:var(--warn);border-color:oklch(75% 0.16 30 / .5)}
.warn .card-tip .tipic{color:var(--warn)} .warn .card-tip strong{color:var(--warn)}

/* ---------- conceito EDITORIAL (padrão quente W2) ---------- */
.ed{flex:1;display:flex;flex-direction:column;margin-top:30px}
.ed-head{display:flex;align-items:flex-end;gap:34px;margin-bottom:8px}
.ed-num{font-family:'Literata',Georgia,serif;font-weight:600;font-size:300px;line-height:.72;
  color:transparent;-webkit-text-stroke:2.5px oklch(74% 0.11 152 / .55);letter-spacing:-.04em;
  flex:0 0 auto;text-shadow:0 0 70px oklch(72% 0.14 152 / .12)}
.warn .ed-num{-webkit-text-stroke-color:oklch(75% 0.16 30 / .5)}
.ed-meta{flex:1;padding-bottom:22px}
.ed-kicker{font-weight:800;font-size:23px;letter-spacing:.26em;text-transform:uppercase;color:var(--green);margin-bottom:14px}
.warn .ed-kicker{color:var(--warn)}
.ed-rule{height:0;border-top:2px dashed var(--green);opacity:.7;margin-bottom:18px}
.warn .ed-rule{border-color:var(--warn)}
.ed-source{font-family:'Literata',Georgia,serif;font-style:italic;font-weight:400;font-size:27px;line-height:1.3;color:var(--muted)}
.ed-source b{color:var(--green-soft);font-style:normal;font-weight:600}
.ed-title{font-family:'Literata',Georgia,serif;font-weight:700;font-size:80px;line-height:1.04;color:var(--ink);letter-spacing:-.018em;text-wrap:balance;margin:18px 0 6px}
.ed-title em{font-style:italic;font-weight:600;color:var(--green)}
.warn .ed-title em{color:var(--warn)}
.ed-body{font-family:'Literata',Georgia,serif;font-weight:400;font-size:44px;line-height:1.5;color:var(--ink);text-wrap:pretty;margin-top:30px;padding-top:34px;border-top:2px solid var(--hair2);position:relative}
.ed-body::before{content:'';position:absolute;top:-1px;left:0;width:120px;height:0;border-top:3px solid var(--green)}
.warn .ed-body::before{border-color:var(--warn)}
.ed-body strong{font-weight:700;color:var(--green-soft)}
.warn .ed-body strong{color:var(--warn)}
.ed-body .dc{float:left;font-family:'Literata',Georgia,serif;font-weight:600;font-size:138px;line-height:.78;color:var(--green);margin:8px 22px -6px 0;text-shadow:0 0 44px oklch(72% 0.14 152 / .3)}
.warn .ed-body .dc{color:var(--warn)}
.ed-tip{margin-top:auto;display:flex;gap:26px;align-items:flex-start;background:linear-gradient(150deg, oklch(70% 0.14 152 / .14), oklch(70% 0.14 152 / .035));border:2px solid var(--hair);border-left:6px solid var(--green);border-radius:22px;padding:34px 38px;box-shadow:0 16px 44px oklch(8% 0.02 152 / .45), inset 0 1px 0 oklch(90% 0.1 152 / .08)}
.warn .ed-tip{border-left-color:var(--warn);background:linear-gradient(150deg, oklch(75% 0.16 30 / .14), oklch(75% 0.16 30 / .035))}
.ed-tip .tipic{flex:0 0 auto;width:60px;height:60px;border-radius:16px;display:flex;align-items:center;justify-content:center;background:var(--green);color:var(--on-green);box-shadow:0 8px 22px oklch(60% 0.14 152 / .4)}
.warn .ed-tip .tipic{background:var(--warn)}
.ed-tip .tipic svg{width:34px;height:34px;color:var(--on-green)}
.ed-tip .tiptext{flex:1}
.ed-tip .tiplabel{font-weight:900;font-size:20px;letter-spacing:.22em;text-transform:uppercase;color:var(--green);margin-bottom:9px}
.warn .ed-tip .tiplabel{color:var(--warn)}
.ed-tip .tipbody{font-size:31px;line-height:1.36;color:var(--green-soft);font-weight:500;text-wrap:pretty}
.ed-tip .tipbody strong{color:var(--green);font-weight:800}
.warn .ed-tip .tipbody{color:oklch(82% 0.08 38)} .warn .ed-tip .tipbody strong{color:var(--warn)}

/* ---------- capa ---------- */
.cover{justify-content:center;text-align:center;align-items:center}
/* wordmark = ASSINATURA forte do canal (a marca para o dedo) */
.cover .wordmark{position:absolute;top:74px;left:0;right:0;display:flex;
  align-items:center;justify-content:center;gap:16px;z-index:2}
.cover .wordmark .seal{width:62px;height:62px;border-radius:18px;display:flex;
  align-items:center;justify-content:center;background:var(--green);color:var(--on-green);
  box-shadow:0 10px 30px oklch(60% 0.14 152 / .4)}
.cover .wordmark .seal svg{width:38px;height:38px;color:var(--on-green)}
.cover .wordmark .name{font-weight:900;letter-spacing:.04em;font-size:40px;
  color:var(--ink);text-transform:uppercase;line-height:1}
.cover .wordmark .name b{color:var(--green)}
.cover .kicker{display:inline-block;font-size:21px;color:var(--green-soft);font-weight:800;
  letter-spacing:.2em;text-transform:uppercase;margin-top:0;max-width:680px;line-height:1.35;
  border:1.5px solid var(--hair);border-radius:999px;padding:11px 26px;
  background:oklch(70% 0.14 152 / .06)}
.cover h1{font-size:124px;line-height:.92;font-weight:900;text-transform:uppercase;
  margin:30px 0 0;text-wrap:balance;letter-spacing:-.022em}
.cover h1 .lt{color:var(--green);text-shadow:0 0 60px oklch(72% 0.14 152 / .4)}
.cover h1 .bd{color:var(--ink)}
.cover .author{font-size:34px;color:var(--muted);margin-top:30px;font-weight:700;letter-spacing:.01em}
.cover .hook{display:flex;align-items:center;justify-content:center;gap:28px;
  margin-top:58px;border-top:3px dashed var(--green);border-bottom:3px dashed var(--green);
  padding:32px 0;max-width:820px}
.cover .hook .num{font-size:128px;font-weight:900;line-height:.76;color:var(--gold);
  letter-spacing:-.04em;text-shadow:0 0 50px oklch(84% 0.12 83 / .35)}
.cover .hook .lbl{font-size:48px;font-weight:800;color:var(--ink);text-align:left;
  line-height:1.04;text-transform:uppercase;text-wrap:balance}
.cover .hook .lbl span{color:var(--green)}
/* swipe = affordance principal: pill verde, grande, perto do polegar */
.cover .swipe{position:absolute;bottom:120px;left:50%;transform:translateX(-50%);
  font-weight:800;letter-spacing:.16em;font-size:30px;color:var(--on-green);
  text-transform:uppercase;display:inline-flex;align-items:center;justify-content:center;
  gap:18px;z-index:2;background:var(--green);padding:20px 44px;border-radius:999px;
  box-shadow:0 16px 44px oklch(60% 0.14 152 / .42);white-space:nowrap}
.cover .swipe .arrow{display:inline-flex;width:38px;height:38px}
.cover .swipe .arrow svg{width:38px;height:38px;color:var(--on-green)}

/* ---------- cta ---------- */
.cta{justify-content:center;text-align:center;align-items:center;padding-top:110px}
.cta .big{font-size:90px;line-height:1.0;font-weight:900;text-transform:uppercase;text-wrap:balance;letter-spacing:-.015em}
.cta .big .lt{color:var(--green);text-shadow:0 0 56px oklch(72% 0.14 152 / .32)}
.cta .rows{display:flex;flex-direction:column;gap:0;margin-top:58px;width:100%;max-width:780px}
.cta .row{display:flex;align-items:center;gap:26px;padding:30px 4px;text-align:left}
.cta .row + .row{border-top:2px dashed var(--hair)}
.cta .row .rico{flex:0 0 auto;width:70px;height:70px;border-radius:18px;display:flex;
  align-items:center;justify-content:center;background:oklch(70% 0.14 152 / .12);
  border:2px solid var(--hair);color:var(--green)}
.cta .row .rico svg{width:40px;height:40px}
.cta .row p{font-size:38px;line-height:1.24;color:var(--ink);font-weight:600;text-wrap:pretty}
.cta .row p strong{color:var(--green-soft);font-weight:800}
.cta .save{margin-top:60px;display:inline-flex;align-items:center;gap:18px;background:var(--green);
  color:var(--on-green);font-weight:800;font-size:40px;padding:24px 52px;border-radius:20px;
  text-transform:uppercase;box-shadow:0 18px 50px oklch(60% 0.14 152 / .4)}
.cta .save svg{width:44px;height:44px;flex:0 0 auto}
.cta .handle{position:absolute;bottom:116px;left:0;right:0;font-weight:900;letter-spacing:.12em;
  font-size:30px;color:var(--green-soft);text-transform:uppercase;z-index:2}

/* ---------- lições do capítulo ---------- */
.lessons{justify-content:flex-start}
.lessons .ed-num{font-size:80px;width:80px;height:80px;display:flex;align-items:center;justify-content:center}
.lessons .ed-num svg{width:54px;height:54px;color:var(--green);filter:drop-shadow(0 0 12px oklch(72% 0.14 152 / .45))}
.lessons-list{list-style:none;padding:0;margin:20px 0 0;display:flex;flex-direction:column;flex:1}
.lessons-list li{display:flex;align-items:flex-start;gap:30px;padding:32px 0;font-family:'Literata',Georgia,serif;font-size:41px;font-weight:500;color:var(--ink);line-height:1.3;text-wrap:pretty}
.lessons-list li + li{border-top:2px dashed var(--hair)}
.lessons-list .lnum{font-family:'Hanken Grotesk',system-ui,sans-serif;font-size:62px;font-weight:900;color:var(--green);line-height:.82;flex:0 0 44px;text-shadow:0 0 36px oklch(72% 0.14 152 / .38)}
.lessons-list li strong{color:var(--green-soft);font-weight:700}

/* ---------- citação ---------- */
.quote{justify-content:center;align-items:flex-start;text-align:left;padding-top:120px}
.quote .qhead{position:absolute;top:80px;left:90px}
.quote .qmark{font-family:'Literata',Georgia,serif;font-style:italic;font-weight:600;
  font-size:280px;line-height:.62;color:var(--green);opacity:.92;height:150px;
  text-shadow:0 0 50px oklch(72% 0.14 152 / .3)}
.quote .qcount{position:absolute;top:104px;right:90px;z-index:2;
  font-weight:800;font-size:26px;letter-spacing:.04em;color:var(--green-soft);
  display:inline-flex;align-items:baseline;gap:4px}
.quote .qcount b{font-size:32px;color:var(--green)} .quote .qcount .sl{color:var(--hair)}
.quote .phrase{font-size:66px;line-height:1.2;font-weight:800;color:var(--ink);
  margin-top:8px;text-wrap:balance;letter-spacing:-.012em}
.quote .phrase em{color:var(--green);font-style:normal}
.quote .attr{margin-top:50px;padding-top:32px;border-top:3px dashed var(--green);
  font-size:34px;line-height:1.34;color:var(--green-soft);font-weight:800;letter-spacing:.01em}
.quote .attr .book{color:var(--muted);font-weight:600;font-style:italic}
.quote .foot{position:absolute;left:90px;right:90px;bottom:104px;display:flex;
  align-items:center;justify-content:space-between;z-index:2}
.quote .foot .handle{font-weight:900;letter-spacing:.08em;font-size:28px;color:var(--green-soft);text-transform:uppercase}
.quote .foot .cta-min{font-weight:800;letter-spacing:.02em;font-size:25px;color:var(--on-green);
  text-transform:uppercase;display:inline-flex;align-items:center;gap:12px;background:var(--green);
  padding:14px 26px;border-radius:999px;box-shadow:0 10px 30px oklch(60% 0.14 152 / .35)}
.quote .foot .cta-min svg{width:30px;height:30px;color:var(--on-green)}
"""


# Auto-fit do carrossel (FONTE ÚNICA). Encolhe-para-caber, nunca trunca:
#  (1) títulos gigantes por LARGURA (.cover/.st h1);
#  (2) QUALQUER slide (concept/quote/cta/story) por ALTURA — mede o elemento de
#      texto mais baixo contra a margem segura (= padding-bottom do slide) e reduz
#      o font-size dos blocos de texto até caber (piso 22px).
_FIT_JS = """() => {
  for (const el of document.querySelectorAll('.cover h1, .st h1')) {
    const box = el.parentElement, cs = getComputedStyle(box);
    const avail = box.clientWidth - parseFloat(cs.paddingLeft) - parseFloat(cs.paddingRight);
    let fs = parseFloat(getComputedStyle(el).fontSize), g = 0;
    while (el.getBoundingClientRect().width > avail && fs > 50 && g < 120) { fs -= 3; el.style.fontSize = fs + 'px'; g++; }
  }
  const SHRINK = '.ed-title,.ed-body,.ed-tip .tipbody,.phrase,.cta .big,.cta .row p,.cta .save,.card-title,.card-body,.card-tip';
  for (const slide of document.querySelectorAll('.slide, .story')) {
    const padB = parseFloat(getComputedStyle(slide).paddingBottom) || 110;
    const safe = slide.getBoundingClientRect().bottom - Math.max(padB, 40);
    const maxBottom = () => {
      let m = 0;
      for (const el of slide.querySelectorAll(SHRINK)) { const r = el.getBoundingClientRect(); if (r.height > 0) m = Math.max(m, r.bottom); }
      return m;
    };
    let g = 0;
    while (maxBottom() > safe && g < 300) {
      let changed = false;
      for (const el of slide.querySelectorAll(SHRINK)) {
        const fs = parseFloat(getComputedStyle(el).fontSize);
        if (fs > 22) { el.style.fontSize = (fs - 1) + 'px'; changed = true; }
      }
      if (!changed) break;
      g++;
    }
  }
}"""


# ---------- STORIES (9:16, 1080x1920) ----------
_STORY_CSS_AUX = """:root{
  --story-bg1: oklch(24% 0.045 152 / .85); --story-bg2: oklch(27% 0.05 152);
  --story-bg3: oklch(5% 0.012 152 / .62); --story-dots: oklch(78% 0.07 152 / .05);
  --story-ghost: oklch(74% 0.09 152 / .10); --story-seal-shadow: oklch(60% 0.14 152 / .4);
  --story-tap-shadow: oklch(60% 0.14 152 / .42); --story-glow-a42: oklch(72% 0.14 152 / .42);
  --story-glow-a38: oklch(84% 0.12 83 / .38); --story-glow-a35: oklch(72% 0.14 152 / .35);
  --story-glow-a34: oklch(72% 0.14 152 / .34); --story-rico-bg: oklch(70% 0.14 152 / .12);
}"""

STORY_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;500;600;700;800;900&family=Literata:ital,opsz,wght@1,7..72,500;1,7..72,600&display=swap');
""" + tokens.ROOT + "\n" + _STORY_CSS_AUX + """
*{margin:0;padding:0;box-sizing:border-box}
body{background:#000;font-family:'Hanken Grotesk',system-ui,sans-serif;-webkit-font-smoothing:antialiased}
/* zona segura de story: conteudo no miolo (topo/rodape ~290px livres p/ UI do IG) */
.story{width:1080px;height:1920px;color:var(--ink);padding:300px 100px;display:flex;
  flex-direction:column;align-items:center;justify-content:center;text-align:center;
  position:relative;overflow:hidden;
  background:
   radial-gradient(120% 50% at 100% 104%, var(--story-bg1) 0%, transparent 44%),
   radial-gradient(110% 42% at 50% -4%, var(--story-bg2) 0%, transparent 54%),
   radial-gradient(140% 120% at 50% 50%, transparent 50%, var(--story-bg3) 100%),
   linear-gradient(178deg, var(--bg) 0%, var(--bg2) 100%);}
.story::before{content:'';position:absolute;inset:0;pointer-events:none;
  background-image:radial-gradient(var(--story-dots) 1.1px, transparent 1.3px);
  background-size:38px 38px;background-position:center;
  -webkit-mask-image:radial-gradient(120% 88% at 50% 0%, #000 50%, transparent 100%);}
.story::after{content:'';position:absolute;inset:208px 60px;border:2px dashed var(--green);
  border-radius:40px;opacity:.32;pointer-events:none}
.story>*{position:relative;z-index:1}
.story>.ghost{position:absolute;font-family:'Hanken Grotesk';font-weight:900;line-height:.74;
  color:transparent;-webkit-text-stroke:2px var(--story-ghost);pointer-events:none;
  letter-spacing:-.05em;z-index:0;overflow:hidden;
  -webkit-mask-image:radial-gradient(120% 120% at 50% 50%, #000 60%, transparent 100%)}
/* wordmark de story = selo cheio + nome (assinatura forte do canal) */
.badge{position:absolute;top:280px;left:50%;transform:translateX(-50%);
  display:inline-flex;align-items:center;gap:16px;white-space:nowrap}
.badge .seal{width:58px;height:58px;border-radius:17px;display:flex;align-items:center;
  justify-content:center;background:var(--green);color:var(--on-green);flex:0 0 auto;
  box-shadow:0 10px 28px var(--story-seal-shadow)}
.badge .seal svg{width:36px;height:36px;color:var(--on-green)}
.badge .name{font-weight:900;letter-spacing:.03em;font-size:38px;color:var(--ink);text-transform:uppercase}
.badge .name b{color:var(--green)}
.foot{position:absolute;bottom:280px;left:80px;right:80px;text-align:center}
.foot .tap{display:inline-flex;align-items:center;gap:14px;font-weight:800;font-size:36px;
  letter-spacing:.02em;color:var(--on-green);background:var(--green);padding:24px 46px;border-radius:999px;
  text-transform:uppercase;box-shadow:0 18px 54px var(--story-tap-shadow)}
.foot .tap svg{width:40px;height:40px}
.foot .handle{display:block;margin-top:28px;font-weight:800;letter-spacing:.2em;font-size:25px;
  color:var(--muted);text-transform:uppercase}
/* teaser */
.eyebrow{font-size:31px;font-weight:800;letter-spacing:.2em;text-transform:uppercase;color:var(--muted)}
.st h1{font-size:158px;line-height:.9;font-weight:900;text-transform:uppercase;margin:34px 0 0;
  text-wrap:balance;letter-spacing:-.022em}
.st h1 .lt{color:var(--green);text-shadow:0 0 80px var(--story-glow-a42)}
.st h1 .bd{color:var(--ink)}
.st .hook{margin-top:60px;font-size:60px;font-weight:800;color:var(--ink);text-transform:uppercase;
  display:inline-flex;align-items:center;gap:26px;border-top:3px dashed var(--green);padding-top:46px}
.st .hook .num{font-size:140px;font-weight:900;color:var(--gold);line-height:.78;
  text-shadow:0 0 56px var(--story-glow-a38)}
/* quote */
.sq{align-items:flex-start;text-align:left}
.sq .qmark{font-family:'Literata',Georgia,serif;font-style:italic;font-weight:600;font-size:300px;
  line-height:.46;color:var(--green);height:150px;text-shadow:0 0 60px var(--story-glow-a35)}
.sq .phrase{font-size:88px;line-height:1.14;font-weight:800;color:var(--ink);margin-top:34px;
  text-wrap:balance;letter-spacing:-.014em}
.sq .phrase em{color:var(--green);font-style:normal}
.sq .attr{margin-top:60px;padding-top:38px;border-top:3px dashed var(--green);font-size:42px;
  color:var(--green-soft);font-weight:800}
.sq .attr .book{display:block;color:var(--muted);font-weight:600;font-style:italic;font-size:36px;margin-top:8px}
/* cta */
.sc .big{font-size:104px;line-height:.98;font-weight:900;text-transform:uppercase;letter-spacing:-.018em;text-wrap:balance}
.sc .big .lt{color:var(--green);text-shadow:0 0 60px var(--story-glow-a34)}
.sc .rows{display:flex;flex-direction:column;gap:0;margin-top:70px;width:100%}
.sc .row{display:flex;align-items:center;gap:32px;padding:38px 6px;text-align:left}
.sc .row + .row{border-top:2px dashed var(--hair)}
.sc .row .rico{flex:0 0 auto;width:92px;height:92px;border-radius:22px;display:flex;align-items:center;
  justify-content:center;background:var(--story-rico-bg);border:2px solid var(--hair);color:var(--green)}
.sc .row .rico svg{width:52px;height:52px}
.sc .row p{font-size:50px;font-weight:800;color:var(--ink);line-height:1.05}
.sc .row p span{display:block;font-size:33px;color:var(--muted);font-weight:600;margin-top:6px;text-transform:none;letter-spacing:0}
/* insights/lições */
.si{justify-content:flex-start;text-align:left;padding-top:340px}
.si .eyebrow{font-size:29px;font-weight:800;letter-spacing:.22em;text-transform:uppercase;color:var(--muted);margin-bottom:48px;display:block}
.si ul{list-style:none;padding:0;margin:0;display:flex;flex-direction:column;width:100%;flex:1}
.si li{padding:44px 0;display:flex;align-items:flex-start;gap:34px;font-size:52px;font-weight:800;color:var(--ink);line-height:1.18;text-align:left}
.si li + li{border-top:2px dashed var(--hair)}
.si li .num{font-size:86px;font-weight:900;color:var(--green);line-height:.78;flex:0 0 54px;text-shadow:0 0 48px var(--story-glow-a38)}
"""
