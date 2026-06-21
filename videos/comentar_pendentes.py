# -*- coding: utf-8 -*-
"""Posta o comentário de CTA nos Shorts agendados assim que ficarem públicos.
Idempotente: estado em _shorts/comentarios_state.json. Quando todos os pendentes
forem comentados, remove a própria tarefa agendada do Windows (MinutoReal_Comentarios).

Agendado via:  schtasks /Create /SC HOURLY /TN MinutoReal_Comentarios /TR "python <este arquivo>"
"""
import sys, json, subprocess
try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass
from pathlib import Path
from canal_guard import get_youtube

ROOT = Path(__file__).parent
STATE = ROOT / '_shorts' / 'comentarios_state.json'
ARTE, MAQ = 'https://youtu.be/zLqdMHJ-k8A', 'https://youtu.be/QIYk743VByU'
TXT = ('Se valeu seu tempo, o like ajuda o canal — e a inscrição garante o próximo livro. '
       'Toda semana, uma grande obra em minutos.\n\n📚 Resumo completo: {link}')
PENDENTES = {
    'fEVIgIFu8og': ARTE, 'sW8KKf3-CoA': ARTE, 'xtrshk9yadA': ARTE,
    'ODqa4x0uMTc': MAQ, 'gWa8BL1iZP8': MAQ, 'eUXaxESkSCo': MAQ,
}


def main():
    feitos = set(json.loads(STATE.read_text(encoding='utf-8'))) if STATE.exists() else set()
    falta = {v: l for v, l in PENDENTES.items() if v not in feitos}
    if not falta:
        subprocess.run(['schtasks', '/Delete', '/TN', 'MinutoReal_Comentarios', '/F'],
                       capture_output=True)
        print('todos comentados — tarefa removida')
        return
    yt = get_youtube()   # cliente JÁ verificado no Minuto Real
    r = yt.videos().list(part='status', id=','.join(falta)).execute()
    publicos = [it['id'] for it in r['items'] if it['status']['privacyStatus'] == 'public']
    for vid in publicos:
        try:
            yt.commentThreads().insert(part='snippet', body={'snippet': {
                'videoId': vid,
                'topLevelComment': {'snippet': {'textOriginal': TXT.format(link=falta[vid])}}}}).execute()
            feitos.add(vid)
            print(f'comentado: {vid}')
        except Exception as e:
            print(f'falhou {vid}: {str(e)[:100]}')
    STATE.write_text(json.dumps(sorted(feitos)), encoding='utf-8')
    print(f'estado: {len(feitos)}/{len(PENDENTES)} comentados')


if __name__ == '__main__':
    main()
