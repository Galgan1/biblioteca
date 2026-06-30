# -*- coding: utf-8 -*-
"""servir_publicar.py — SERVIÇO ISOLADO do botão 1-clique (T2).

Processo PRÓPRIO (vira um PM2 app na porta 8790) que NÃO toca nenhum dos apps de
produção da VPS (Akita pilar 8: os apps existentes não podem ser arriscados — este é
um processo novo e separado). HTTP em STDLIB pura (http.server) — SEM Flask, SEM deps
novas. O site da Biblioteca bate aqui; o nginx faz o proxy.

Contrato HTTP (fixo — o front depende disto):
  POST /publicar   header X-Admin-Token: <token>   body {"slug":"...","dry":bool}
    -> token ausente/errado: 401 JSON
    -> slug fora de ^[a-z0-9-]+$: 400 JSON
    -> ok: dispara publicar_tudo.py em BACKGROUND (Popen lista-de-args, nunca shell)
       e responde 200 {"ok":true,"job":"<slug>","dry":bool}
  GET /status?slug=<slug>  -> 200 com o state por superfície (ou {} se não começou)
  GET /livros  -> 200 {"livros":[{slug,titulo,autor}]} — lista pra UI escolher (sem decorar slug)
  GET /  -> página admin PREMIUM (escolhe livro na lista + Publicar tudo), atrás do auth_basic do nginx
  outra rota -> 404 JSON.  Erros -> JSON com contexto, nunca stack trace cru (pilar 7).
Bind: 127.0.0.1:8790 (o nginx termina TLS e faz proxy).
"""
import json
import re
import subprocess
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

ROOT = Path(__file__).parent
TOKEN_FILE = ROOT / '.secrets' / 'publicar_token.txt'
ESTADO_DIR = ROOT / '_shorts'
ORQUESTRADOR = ROOT / 'publicar_tudo.py'
SLUG_RE = re.compile(r'^[a-z0-9-]+$')
HOST, PORT = '127.0.0.1', 8790

# Tokens da marca = FONTE ÚNICA (marca.py, constituição pilar 4 — não inventar cor). O
# fallback abaixo é só insurance se marca.py não estiver no host; é cópia CITADA do
# css_root('dark') de marca.py (verde h152, ouro h83 = acento único, papel h152 escuro).
_BRAND_FALLBACK = """:root{
  --green: oklch(70% 0.13 152); --green-dark: oklch(76% 0.11 152); --green-light: oklch(28% 0.04 152);
  --gold: oklch(76% 0.105 83); --gold-soft: oklch(86% 0.075 83); --dislike: oklch(72% 0.16 30);
  --black: oklch(95% 0.01 152); --gray-dark: oklch(72% 0.01 152); --paper-bg: oklch(16% 0.01 152);
  --font-display: 'Hanken Grotesk', system-ui, sans-serif; --font-serif: 'Literata', Georgia, serif;
}"""


def _brand_css():
    """:root da marca a partir da fonte única marca.py; cai no fallback citado se ausente."""
    try:
        import marca
        return marca.css_root('dark')
    except Exception:
        return _BRAND_FALLBACK


_PAGE = """<!doctype html><html lang=pt-BR><head><meta charset=utf-8>
<meta name=viewport content="width=device-width,initial-scale=1"><title>Publicar · Minuto Real</title>
<link rel=preconnect href=https://fonts.googleapis.com><link rel=preconnect href=https://fonts.gstatic.com crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;500;600;700;800&family=Literata:ital@1&display=swap" rel=stylesheet>
<style>
__BRAND__
*{box-sizing:border-box}
body{background:var(--paper-bg);color:var(--black);font-family:var(--font-display);margin:0;line-height:1.5;
 background-image:radial-gradient(120% 70% at 50% -8%, color-mix(in oklab,var(--green) 12%,transparent), transparent 60%)}
.wrap{max-width:760px;margin:0 auto;padding:34px 20px 72px}
a{color:var(--gold)}
.marca{font-size:12px;letter-spacing:.22em;font-weight:700;color:var(--gold);display:flex;align-items:center;gap:9px;text-transform:uppercase}
.marca i{width:7px;height:7px;border-radius:50%;background:var(--gold);box-shadow:0 0 0 4px color-mix(in oklab,var(--gold) 22%,transparent)}
h1{font-size:clamp(28px,6vw,40px);font-weight:800;margin:16px 0 6px;letter-spacing:-.02em}
.sub{color:var(--gray-dark);max-width:56ch;margin:0 0 26px;font-size:15px}
.campo{display:flex;align-items:center;gap:10px;background:color-mix(in oklab,var(--black) 5%,transparent);
 border:1px solid color-mix(in oklab,var(--black) 14%,transparent);border-radius:14px;padding:0 14px}
.campo:focus-within{border-color:var(--green);box-shadow:0 0 0 4px color-mix(in oklab,var(--green) 16%,transparent)}
.campo svg{flex:none;opacity:.55}
#busca{flex:1;background:none;border:0;outline:0;color:var(--black);font:inherit;padding:14px 0}
#contagem{font-size:12px;color:var(--gray-dark);flex:none}
#lista{margin:14px 0 0;border:1px dashed color-mix(in oklab,var(--green) 42%,transparent);border-radius:16px;overflow:hidden;max-height:46vh;overflow-y:auto}
.item{display:flex;align-items:center;gap:14px;width:100%;text-align:left;background:none;color:inherit;font:inherit;cursor:pointer;
 border:0;border-bottom:1px solid color-mix(in oklab,var(--black) 8%,transparent);padding:13px 16px;transition:background .12s}
.item:last-child{border-bottom:0}
.item:hover{background:color-mix(in oklab,var(--green) 9%,transparent)}
.item.sel{background:color-mix(in oklab,var(--green) 16%,transparent);box-shadow:inset 3px 0 0 var(--gold)}
.item .ic{flex:none;color:var(--green)}
.item .meta{min-width:0}
.item b{display:block;font-weight:600;font-size:15px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.item i{display:block;font-family:var(--font-serif);font-style:italic;color:var(--gray-dark);font-size:13px}
.item .sg{margin-left:auto;font:11px/1 ui-monospace,monospace;color:color-mix(in oklab,var(--gray-dark) 75%,transparent);flex:none}
.vazio{padding:26px 16px;color:var(--gray-dark);text-align:center}
.sk{height:54px;border-bottom:1px solid color-mix(in oklab,var(--black) 8%,transparent);
 background:linear-gradient(90deg,transparent,color-mix(in oklab,var(--black) 8%,transparent),transparent);background-size:200% 100%;animation:sh 1.2s infinite}
@keyframes sh{0%{background-position:200% 0}100%{background-position:-200% 0}}
.acoes{display:flex;align-items:center;gap:18px;flex-wrap:wrap;margin-top:22px}
.switch{display:flex;align-items:center;gap:10px;cursor:pointer;user-select:none;font-size:14px;position:relative}
.switch input{position:absolute;opacity:0;width:0;height:0}
.track{width:44px;height:26px;border-radius:99px;background:color-mix(in oklab,var(--black) 22%,transparent);position:relative;transition:.15s;flex:none}
.track::after{content:"";position:absolute;top:3px;left:3px;width:20px;height:20px;border-radius:50%;background:var(--black);transition:.15s}
.switch input:checked + .track{background:var(--green)}
.switch input:checked + .track::after{transform:translateX(18px);background:var(--paper-bg)}
.switch small{color:var(--gray-dark)}
.switch.perigo .lbl{color:var(--dislike);font-weight:700}
.go{margin-left:auto;font:inherit;font-weight:700;font-size:15px;border:0;border-radius:13px;padding:14px 22px;cursor:pointer;background:var(--green);color:var(--paper-bg);transition:.15s}
.go:hover:not(:disabled){background:var(--green-dark)}
.go:disabled{opacity:.38;cursor:not-allowed}
.go.real{background:var(--gold)}
.aviso-real{flex-basis:100%;font-size:13px;color:var(--dislike);margin:2px 0 0}
#painel{margin-top:30px;display:none}
.painel-tit{font-weight:700;font-size:16px;margin:0 0 14px}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.card{border:1px solid color-mix(in oklab,var(--black) 12%,transparent);border-radius:14px;padding:14px 16px;background:color-mix(in oklab,var(--black) 4%,transparent)}
.card .k{font-size:13px;color:var(--gray-dark)}
.pill{margin-top:10px;display:inline-flex;align-items:center;gap:7px;font-size:13px;font-weight:600;padding:5px 11px;border-radius:99px;border:1px solid transparent}
.pill .led{width:7px;height:7px;border-radius:50%;background:currentColor}
.pill.wait{color:var(--gray-dark);border-color:color-mix(in oklab,var(--gray-dark) 40%,transparent)}
.pill.wait .led{animation:pulse 1s infinite}
@keyframes pulse{50%{opacity:.25}}
.pill.ok{color:var(--green);border-color:color-mix(in oklab,var(--green) 50%,transparent);background:color-mix(in oklab,var(--green) 12%,transparent)}
.pill.test{color:var(--gold);border-color:color-mix(in oklab,var(--gold) 50%,transparent);background:color-mix(in oklab,var(--gold) 12%,transparent)}
.pill.err{color:var(--dislike);border-color:color-mix(in oklab,var(--dislike) 50%,transparent);background:color-mix(in oklab,var(--dislike) 12%,transparent)}
.pill.skip{color:var(--gray-dark);border-color:color-mix(in oklab,var(--gray-dark) 30%,transparent)}
.card .det{margin-top:8px;font-size:11px;color:var(--gray-dark);word-break:break-all}
@media(max-width:560px){.grid{grid-template-columns:1fr}.go{margin-left:0;flex:1}}
</style></head><body>
<div class=wrap>
 <div class=marca><i></i> Minuto Real</div>
 <h1>Publicar tudo</h1>
 <p class=sub>Um clique e o livro vai pro YouTube (vídeo + Shorts), Instagram e Facebook — processado na VPS, com alerta no Telegram se algo falhar.</p>
 <label class=campo>
  <svg width=18 height=18 viewBox="0 0 24 24" fill=none stroke=currentColor stroke-width=2><circle cx=11 cy=11 r=7/><path d="m21 21-4.35-4.35"/></svg>
  <input id=busca placeholder="Buscar livro por título ou autor…" oninput=filtra() autocomplete=off>
  <span id=contagem></span>
 </label>
 <div id=lista><div class=sk></div><div class=sk></div><div class=sk></div></div>
 <div class=acoes>
  <label class=switch id=swt><input type=checkbox id=dry checked onchange=modo()><span class=track></span><span class=lbl>Modo teste</span><small>não publica</small></label>
  <button id=go class=go disabled onclick=pub()>Publicar tudo</button>
  <p class=aviso-real id=avisoReal hidden>Modo real ligado: ao confirmar, publica de verdade nas 3 redes.</p>
 </div>
 <section id=painel><p class=painel-tit id=painelTit></p><div class=grid id=grid></div></section>
</div>
<script>
var LIVROS=[], SLUG='';
var SURF=[['youtube_longo','YouTube · vídeo'],['youtube_shorts','YouTube · Shorts'],['instagram','Instagram · Reels'],['facebook','Facebook']];
function esc(s){var d=document.createElement('div');d.textContent=s==null?'':s;return d.innerHTML;}
function ico(){return '<svg class=ic width=20 height=20 viewBox="0 0 24 24" fill=none stroke=currentColor stroke-width=1.6><path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v15.5H6.5A2.5 2.5 0 0 0 4 21z"/><path d="M4 18.5A2.5 2.5 0 0 1 6.5 16H20"/></svg>';}
function render(arr){
 var L=document.getElementById('lista');
 document.getElementById('contagem').textContent=LIVROS.length?arr.length+'/'+LIVROS.length:'';
 if(!arr.length){L.innerHTML='<div class=vazio>nenhum livro encontrado.</div>';return;}
 L.innerHTML='';
 arr.forEach(function(b){
  var el=document.createElement('button'); el.type='button'; el.className='item';
  el.innerHTML=ico()+'<span class=meta><b>'+esc(b.titulo)+'</b><i>'+esc(b.autor||'—')+'</i></span><span class=sg>'+esc(b.slug)+'</span>';
  el.onclick=function(){
   SLUG=b.slug;
   [].forEach.call(document.querySelectorAll('.item'),function(x){x.classList.remove('sel');});
   el.classList.add('sel'); document.getElementById('go').disabled=false;
  };
  L.appendChild(el);
 });
}
function filtra(){var q=document.getElementById('busca').value.toLowerCase();
 render(LIVROS.filter(function(b){return (b.titulo+' '+b.slug+' '+(b.autor||'')).toLowerCase().indexOf(q)>=0;}));}
async function carrega(){
 try{var j=await (await fetch('livros')).json(); LIVROS=j.livros||[]; render(LIVROS);}
 catch(e){document.getElementById('lista').innerHTML='<div class=vazio>falha ao listar livros: '+esc(''+e)+'</div>';}
}
function modo(){
 var dry=document.getElementById('dry').checked, go=document.getElementById('go');
 document.getElementById('swt').classList.toggle('perigo',!dry);
 document.getElementById('avisoReal').hidden=dry;
 go.classList.toggle('real',!dry);
 go.textContent=dry?'Publicar tudo':'Publicar DE VERDADE';
}
function pill(v){
 if(v==null) return ['wait','aguardando'];
 if(/^ok/i.test(v)) return ['ok','no ar'];
 if(/^ERRO/i.test(v)) return ['err','falhou'];
 if(/dry-run/i.test(v)) return ['test','teste ok'];
 if(/pulado/i.test(v)) return ['skip','já no ar'];
 return ['wait',''+v];
}
function ytLink(v){var m=(''+v).match(/[A-Za-z0-9_-]{11}/);return m?'https://youtu.be/'+m[0]:'';}
function pinta(st){
 var g=document.getElementById('grid'); g.innerHTML='';
 SURF.forEach(function(s){
  var v=st[s[0]], p=pill(v);
  var link=(s[0]==='youtube_longo'&&/^ok/i.test(''+v))?ytLink(v):'';
  var det=(v==null)?'':esc((''+v).replace(/^ok:\\s*/i,'').slice(0,90));
  g.innerHTML+='<div class=card><div class=k>'+esc(s[1])+'</div>'+
   '<span class="pill '+p[0]+'"><span class=led></span>'+esc(p[1])+'</span>'+
   (link?'<div class=det><a href="'+link+'" target=_blank rel=noopener>'+link+'</a></div>':(det?'<div class=det>'+det+'</div>':''))+'</div>';
 });
}
async function pub(){
 var dry=document.getElementById('dry').checked, go=document.getElementById('go');
 if(!/^[a-z0-9-]+$/.test(SLUG)) return;
 if(!dry && !confirm('Publicar "'+SLUG+'" DE VERDADE em YouTube + Instagram + Facebook?')) return;
 go.disabled=true;
 document.getElementById('painel').style.display='block';
 document.getElementById('painelTit').textContent=(dry?'Modo teste · ':'Publicando · ')+SLUG;
 pinta({});
 try{
  var r=await fetch('publicar',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({slug:SLUG,dry:dry})});
  var j=await r.json();
  if(!j.ok){document.getElementById('painelTit').textContent='Erro ao disparar: '+(j.erro||('HTTP '+r.status));go.disabled=false;return;}
  for(var i=0;i<60;i++){
   await new Promise(function(x){setTimeout(x,3500);});
   var st=await (await fetch('status?slug='+encodeURIComponent(SLUG))).json();
   pinta(st);
   if(SURF.every(function(s){return st[s[0]]!=null;})){document.getElementById('painelTit').textContent=(dry?'Modo teste concluído · ':'Concluído · ')+SLUG;break;}
  }
 }catch(e){document.getElementById('painelTit').textContent='Falha: '+e;}
 go.disabled=false;
}
carrega(); modo();
</script></body></html>"""

_ADMIN_HTML = _PAGE.replace('__BRAND__', _brand_css())


# --- lógica pura (testável sem subir servidor) -----------------------------
def _autoriza(token):
    """True só se o header bate com o segredo em disco. Sem arquivo -> nega (não 'abre')."""
    try:
        esperado = TOKEN_FILE.read_text(encoding='utf-8').strip()
    except OSError:
        return False
    return bool(esperado) and token == esperado


def _slug_valido(slug):
    return bool(slug) and bool(SLUG_RE.match(slug))


def _dispara(slug, dry=False):
    """Anti-injeção: lista de args, NUNCA shell=True. Background. dry=True passa --dry
    (modo teste: roda a cadeia mas NÃO publica nem renderiza)."""
    args = [sys.executable, str(ORQUESTRADOR), slug]
    if dry:
        args.append('--dry')
    return subprocess.Popen(args, cwd=str(ROOT))


def _status(slug):
    """Estado por superfície do _shorts/<slug>_publicar_tudo.json (ou {} se não começou)."""
    p = ESTADO_DIR / f'{slug}_publicar_tudo.json'
    try:
        return json.loads(p.read_text(encoding='utf-8'))
    except OSError:
        return {}
    except json.JSONDecodeError:
        return {}


def _livros(diretorio=None):
    """Lista os roteiros PUBLICÁVEIS (slug + título + autor) p/ a UI não exigir slug de cor.
    Roteiro = JSON em ROOT (mesmo lugar que publicar_tudo lê <slug>.json) com 'titulo' e
    'cenas', nome-de-arquivo = slug válido. Ignora configs/estados sem forma de roteiro."""
    base = diretorio or ROOT
    out = []
    for f in sorted(base.glob('*.json')):
        if not _slug_valido(f.stem):
            continue
        try:
            cfg = json.loads(f.read_text(encoding='utf-8'))
        except (OSError, json.JSONDecodeError):
            continue
        if isinstance(cfg, dict) and cfg.get('titulo') and cfg.get('cenas'):
            out.append({'slug': f.stem, 'titulo': cfg['titulo'], 'autor': cfg.get('autor', '')})
    return out


# --- handler HTTP (casca fina sobre a lógica pura) -------------------------
class Handler(BaseHTTPRequestHandler):
    server_version = 'servir_publicar/1.0'

    def _json(self, code, payload):
        body = json.dumps(payload, ensure_ascii=False).encode('utf-8')
        self.send_response(code)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _html(self, code, body):
        b = body.encode('utf-8')
        self.send_response(code)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.send_header('Content-Length', str(len(b)))
        self.end_headers()
        self.wfile.write(b)

    def log_message(self, *_):
        pass  # silencia o log default (BaseHTTPRequestHandler escreve no stderr)

    def do_POST(self):
        if urlparse(self.path).path != '/publicar':
            return self._json(404, {'ok': False, 'erro': 'rota desconhecida'})
        if not _autoriza(self.headers.get('X-Admin-Token', '')):
            return self._json(401, {'ok': False, 'erro': 'token ausente ou invalido'})
        try:
            n = int(self.headers.get('Content-Length') or 0)
            corpo = json.loads(self.rfile.read(n) or b'{}')
            slug = (corpo or {}).get('slug', '')
        except (ValueError, json.JSONDecodeError) as e:
            return self._json(400, {'ok': False, 'erro': f'body JSON invalido: {e}'})
        if not _slug_valido(slug):
            return self._json(400, {'ok': False, 'erro': f'slug invalido (esperado ^[a-z0-9-]+$): {slug!r}'})
        dry = bool((corpo or {}).get('dry'))
        try:
            _dispara(slug, dry)
        except OSError as e:
            return self._json(500, {'ok': False, 'erro': f'falha ao disparar job: {e}'})
        return self._json(200, {'ok': True, 'job': slug, 'dry': dry})

    def do_GET(self):
        u = urlparse(self.path)
        if u.path in ('/', '/index.html'):
            return self._html(200, _ADMIN_HTML)
        if u.path == '/livros':
            return self._json(200, {'livros': _livros()})
        if u.path != '/status':
            return self._json(404, {'ok': False, 'erro': 'rota desconhecida'})
        slug = (parse_qs(u.query).get('slug') or [''])[0]
        if not _slug_valido(slug):
            return self._json(400, {'ok': False, 'erro': f'slug invalido (esperado ^[a-z0-9-]+$): {slug!r}'})
        return self._json(200, _status(slug))


def main():
    srv = ThreadingHTTPServer((HOST, PORT), Handler)
    print(f'servir_publicar ouvindo em http://{HOST}:{PORT}', flush=True)
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        srv.shutdown()
    return 0


if __name__ == '__main__':
    sys.exit(main())
