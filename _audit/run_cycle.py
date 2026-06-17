# -*- coding: utf-8 -*-
"""Roda UM ciclo da varredura de bugs (loop-agente, pausado 1/5min, 30 ciclos).
Lê _audit/loop_state.json, executa o próximo ciclo, anexa achados em
_audit/findings.md, atualiza o estado e imprime se deve continuar.

Ciclos 1..25: ~4 livros ao vivo (overview HTTP 200 + manifest do kit) — espaçado, sem flood.
Ciclo  26: geração de asset do kit (ideia .png/.jpg) numa amostra.
Ciclo  27: endpoint de carrossel numa amostra.
Ciclo  28: gating dos endpoints admin (auth/me 401, options 401 s/ login).
Ciclo  29: integridade de dados (ícone inválido / emph fora do título / card sem corpo).
Ciclo  30: consolidação.
"""
import json, os, subprocess, sys, time, datetime, glob, importlib
sys.stdout.reconfigure(encoding='utf-8')
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(BASE)
AUD = os.path.join(BASE, '_audit')
STATE = os.path.join(AUD, 'loop_state.json')
FIND = os.path.join(AUD, 'findings.md')
SITE = 'https://andregalgani.com.br/biblioteca'

def now(): return datetime.datetime.now().strftime('%H:%M:%S')
def log(line): open(FIND, 'a', encoding='utf-8').write(line + '\n')

def http(path, timeout=25):
    """status code via curl (throttle-safe: retry + timeout). '000' = rede/throttle."""
    try:
        r = subprocess.run(['curl','-s','-o','/dev/null','-w','%{http_code}','--retry','2',
                            '--retry-delay','2','--connect-timeout','12','--max-time',str(timeout), path],
                           capture_output=True, text=True, timeout=timeout+15)
        return r.stdout.strip() or '000'
    except Exception:
        return '000'

def ids():
    return [b['id'] for b in json.load(open('books.json', encoding='utf-8'))]

def valid_icons():
    try:
        import gerar_livro, gerar_carrossel
        return set(gerar_livro.ICONS) | set(gerar_carrossel._EXTRA)
    except Exception:
        return set("arrow book bookmark bubble bulb cards clock constellation eye fork gap key "
                   "layers leaf lens link mask masks mountain person pin pivot play scale shelf "
                   "shield spark spiral steps sword target triangle wave wrench".split())

def cycle(n):
    bugs = []; checked = 0
    if n <= 25:
        chunk = ids()[(n-1)*4:n*4]
        for bid in chunk:
            if not os.path.exists(f'{bid}.html'):
                continue  # livro 'em breve' sem página — não é bug
            checked += 1
            c = http(f'{SITE}/{bid}.html')
            if c == '000':
                log(f'  [rede] {bid}.html (000 — throttle/rede, rechecar)')
            elif c != '200':
                bugs.append(f'{bid}.html → HTTP {c}')
            time.sleep(1.2)
            if os.path.isdir(os.path.join('assets','kit',bid)):
                cm = http(f'{SITE}/assets/kit/{bid}/manifest.json')
                if cm not in ('200','000'):
                    bugs.append(f'manifest do kit de {bid} → HTTP {cm}')
                time.sleep(0.8)
    elif n == 26:
        for bid in ['1984','sapiens','habitos-atomicos']:
            for fmt in ['ideia.png','ideia.jpg']:
                checked += 1
                c = http(f'{SITE}/pdf/asset/{bid}/{fmt}', timeout=60)
                if c not in ('200','000'): bugs.append(f'/pdf/asset/{bid}/{fmt} → {c}')
                time.sleep(2)
    elif n == 27:
        for bid in ['1984','sapiens']:
            checked += 1
            c = http(f'{SITE}/pdf/carrossel/{bid}/overview.json', timeout=90)
            if c not in ('200','000'): bugs.append(f'/pdf/carrossel/{bid}/overview.json → {c}')
            time.sleep(2)
    elif n == 28:
        checked += 2
        if http(f'{SITE}/pdf/auth/me') not in ('401','000'): bugs.append('auth/me NÃO retornou 401 sem login (gating!)')
        if http(f'{SITE}/pdf/admin/instagram/options?book=1984') not in ('401','000'): bugs.append('admin/options acessível SEM login (gating!)')
    elif n == 29:
        vic = valid_icons()
        for f in glob.glob('*_data.py'):
            slug = os.path.basename(f)[:-8]
            try:
                d = importlib.import_module(slug + '_data')
            except Exception as e:
                bugs.append(f'{f}: NÃO importa ({str(e)[:60]})'); continue
            for ch in getattr(d, 'CHAPTERS', []):
                for i, c in enumerate(ch.get('cards', []), 1):
                    checked += 1
                    loc = f"{slug}/{ch.get('slug','?')}#card{i}"
                    if c.get('ic') and c['ic'] not in vic: bugs.append(f'{loc}: ícone inválido "{c["ic"]}"')
                    if not c.get('t'): bugs.append(f'{loc}: sem título (t)')
                    if not c.get('b'): bugs.append(f'{loc}: sem corpo (b)')
                    if c.get('emph') and c['emph'] not in (c.get('t') or ''): bugs.append(f'{loc}: emph "{c["emph"]}" não está no título')
    return checked, bugs

def main():
    os.makedirs(AUD, exist_ok=True)
    st = json.load(open(STATE, encoding='utf-8')) if os.path.exists(STATE) else {'cycle':0,'max':30}
    n = st['cycle'] + 1
    mx = st['max']
    sd = bool(st.get('shutdown_on_done'))
    if n > mx:
        print(f'LOOP COMPLETO ({mx}/{mx}).'); print('continue: no')
        if sd: print('SHUTDOWN: yes')
        return
    checked, bugs = cycle(n)
    log(f'\n## Ciclo {n}/{mx} · {now()} · checados:{checked} · bugs:{len(bugs)}')
    for b in bugs: log(f'  [BUG] {b}')
    if not bugs: log('  PASS — nenhum bug.')
    st['cycle'] = n
    json.dump(st, open(STATE, 'w', encoding='utf-8'))
    print(f'CICLO {n}/{mx} | checados:{checked} | BUGS:{len(bugs)}')
    for b in bugs: print('   [BUG]', b)
    print('continue:', 'yes' if n < mx else 'no')
    if sd and n < mx:
        print('NOTE: desligar o PC ao fim (ciclo %d) — propague no prompt.' % mx)
    if sd and n == mx:
        print('SHUTDOWN: yes')

if __name__ == '__main__':
    main()
