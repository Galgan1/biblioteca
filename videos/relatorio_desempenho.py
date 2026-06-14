# -*- coding: utf-8 -*-
"""Cientista de Dados — extrai lições acionáveis de datas_coletadas.json e grava
em analytics/aprendizados.json, que a Fase 1 do próximo vídeo lê automaticamente.

Fluxo de uso:
  python coletar_datas.py                  # coleta raw (YouTube + IG + site)
  python relatorio_desempenho.py           # extrai lições → analytics/aprendizados.json
  python relatorio_desempenho.py --print   # idem + imprime relatório legível

A Fase 1 do estúdio lê `analytics/aprendizados.json` antes do empacotamento.
"""
import sys, json
from pathlib import Path
from datetime import datetime, timezone, timedelta
try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

ROOT = Path(__file__).parent.parent          # biblioteca/
DATA_FILE = ROOT / 'datas_coletadas.json'
OUT_DIR = ROOT / 'analytics'
OUT_FILE = OUT_DIR / 'aprendizados.json'

# ── limiares (Cientista de Dados, dados-operacoes.md) ──────────────────────
CTR_BOM  = 4.0    # % — acima = empacotamento eficaz
CTR_OK   = 2.5    # % — abaixo = problema de empacotamento
RET_BOA  = 45.0   # % — acima = arco sustenta
RET_OK   = 35.0   # % — abaixo = estrutura precisa revisão
QUEDA_I  = 40.0   # % de queda inicial que sinaliza problema de gancho


def _slug_for_id(video_id, roteiros_dir):
    """Tenta mapear video_id → slug lendo os roteiros/ locais."""
    if not roteiros_dir.exists():
        return None
    for f in roteiros_dir.glob('*.json'):
        try:
            cfg = json.loads(f.read_text(encoding='utf-8'))
            yt = cfg.get('youtube', {})
            # checa IDs no roteiro ou no pipeline_state
            if cfg.get('slug') and video_id in str(cfg):
                return cfg['slug']
        except Exception:
            pass
    return None


def _tendencia(hist):
    """'crescendo'/'estavel'/'caindo' com base nos últimos 7 dias de snapshots."""
    if len(hist) < 2:
        return 'sem dados'
    recent = [h for h in hist[-8:] if 'views_total' in h]
    if len(recent) < 2:
        return 'sem dados'
    delta = recent[-1]['views_total'] - recent[0]['views_total']
    if delta > 100:
        return 'crescendo'
    if delta < -50:
        return 'caindo'
    return 'estavel'


def _diagnostico(ctr, retencao):
    """Retorna (notas[], alertas[], licoes_fase1[], licoes_producao[])."""
    notas, alertas, lic_f1, lic_prod = [], [], [], []

    if ctr is None and retencao is None:
        return ['sem dados de Analytics (rode coletar_datas.py --auth-analytics)'], [], [], []

    # CTR
    if ctr is not None:
        if ctr >= CTR_BOM:
            notas.append(f'CTR ✓ {ctr:.1f}% — empacotamento eficaz; replicar ângulo de título')
        elif ctr >= CTR_OK:
            notas.append(f'CTR ⚠ {ctr:.1f}% — dentro da faixa, mas há espaço para melhorar o título')
            lic_f1.append('Testar ângulo de tensão/paradoxo no título (CTR abaixo do teto)')
        else:
            alertas.append(f'CTR ✗ {ctr:.1f}% — abaixo de {CTR_OK}%: empacotamento fraco para o conteúdo')
            lic_f1.append('Priorizar ângulo de curiosidade ou benefício direto no próximo empacotamento')
            lic_f1.append('Revisar conceito de thumbnail — thumb e título devem gerar loop de curiosidade')

    # Retenção
    if retencao is not None:
        if retencao >= RET_BOA:
            notas.append(f'Retenção ✓ {retencao:.1f}% — arco dramático sustenta; padrão de clímax funcionou')
        elif retencao >= RET_OK:
            notas.append(f'Retenção ⚠ {retencao:.1f}% — aceitável, mas revisar densidade nas cenas do meio')
            lic_prod.append('Revisar loops de retenção a cada 15–30s nas cenas intermediárias')
        else:
            alertas.append(f'Retenção ✗ {retencao:.1f}% — abaixo de {RET_OK}%: estrutura precisa revisão')
            lic_prod.append('Reduzir duração das cenas conceituais; adicionar tensão/gap antes da resolução')
            lic_f1.append('Verificar se gancho entregou a promessa nos primeiros 30s')

    return notas, alertas, lic_f1, lic_prod


def gerar(verbose=False):
    if not DATA_FILE.exists():
        print(f'[!] {DATA_FILE} não encontrado. Rode: python coletar_datas.py')
        return

    raw = json.loads(DATA_FILE.read_text(encoding='utf-8'))
    yt  = raw.get('youtube', {})
    hist = raw.get('historico', [])
    roteiros_dir = ROOT / 'videos' / 'roteiros'

    publicos = {vid: v for vid, v in yt.items()
                if v.get('privacyStatus') == 'public' and 'erro' not in v}

    # ── Canal ──────────────────────────────────────────────────────────────
    total_views = sum(int(v.get('viewCount') or 0) for v in publicos.values())
    ctrs      = [v['ctr']      for v in publicos.values() if v.get('ctr')      is not None]
    retencoes = [v['retencao'] for v in publicos.values() if v.get('retencao') is not None]

    canal = {
        'total_views':          total_views,
        'videos_publicos':      len(publicos),
        'tendencia_7d':         _tendencia(hist),
        'ctr_medio_canal':      round(sum(ctrs) / len(ctrs), 1) if ctrs else None,
        'retencao_media_canal': round(sum(retencoes) / len(retencoes), 1) if retencoes else None,
        'coletado_em':          raw.get('coletado_em'),
    }

    # ── Por vídeo ──────────────────────────────────────────────────────────
    por_video = {}
    all_lic_f1, all_lic_prod = [], []

    for vid, v in sorted(publicos.items(), key=lambda x: int(x[1].get('viewCount') or 0), reverse=True):
        ctr      = v.get('ctr')
        retencao = v.get('retencao')
        notas, alertas, lic_f1, lic_prod = _diagnostico(ctr, retencao)
        slug = _slug_for_id(vid, roteiros_dir)
        por_video[vid] = {
            'slug':           slug,
            'titulo':         v.get('title', '')[:80],
            'views':          int(v.get('viewCount') or 0),
            'likes':          int(v.get('likeCount') or 0),
            'ctr':            ctr,
            'retencao':       retencao,
            'dur_media_s':    v.get('dur_media'),
            'impressoes':     v.get('impressoes'),
            'subs_ganhos':    v.get('subs'),
            'notas':          notas,
            'alertas':        alertas,
            'licoes_fase1':   lic_f1,
            'licoes_producao':lic_prod,
        }
        all_lic_f1.extend(lic_f1)
        all_lic_prod.extend(lic_prod)

    # ── Lições sistêmicas (recorrência em ≥2 vídeos) ──────────────────────
    from collections import Counter
    lic_count_f1   = Counter(all_lic_f1)
    lic_count_prod = Counter(all_lic_prod)
    sistemicas = {
        'fase1':   [l for l, n in lic_count_f1.items()   if n >= 2],
        'producao':[l for l, n in lic_count_prod.items() if n >= 2],
    }

    # ── proxima_fase1: resumo acionável para o Diretor de Ideação ─────────
    proxima = {
        'aviso':       (f'Canal com {len(publicos)} vídeo(s) — pouco dado para regras definitivas. '
                        'Trate como hipóteses.') if len(publicos) < 3 else None,
        'empacotamento': list(dict.fromkeys(
            [l for v in por_video.values() for l in v['licoes_fase1']]
        ))[:4],
        'producao': list(dict.fromkeys(
            [l for v in por_video.values() for l in v['licoes_producao']]
        ))[:4],
        'o_que_funcionou': [
            v['notas'][0] for v in por_video.values()
            if v['notas'] and '✓' in v['notas'][0]
        ][:3],
    }

    resultado = {
        '_doc':         'Lições acionáveis geradas por relatorio_desempenho.py. A Fase 1 do estúdio lê este arquivo antes do empacotamento.',
        'gerado_em':    datetime.now(timezone.utc).isoformat(),
        'canal':        canal,
        'por_video':    por_video,
        'sistemicas':   sistemicas,
        'proxima_fase1':proxima,
    }

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(json.dumps(resultado, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f'-> {OUT_FILE}  ({len(por_video)} vídeos analisados)')

    if verbose:
        _print_report(resultado)

    return resultado


def _print_report(r):
    c = r['canal']
    print(f"\n{'='*60}")
    print(f"RELATÓRIO DE DESEMPENHO · Canal Minuto Real")
    print(f"Coletado: {c.get('coletado_em', '')[:10]} | Tendência: {c['tendencia_7d']}")
    print(f"Views total: {c['total_views']:,} | CTR médio: {c['ctr_medio_canal']}% | Retenção média: {c['retencao_media_canal']}%")
    print(f"{'='*60}")
    for vid, v in r['por_video'].items():
        slug = v.get('slug') or vid
        print(f"\n  {slug}  ({v['views']:,} views)")
        for n in v['notas']:
            print(f"    • {n}")
        for a in v['alertas']:
            print(f"    ! {a}")
    p = r['proxima_fase1']
    if p.get('empacotamento') or p.get('producao'):
        print(f"\n{'─'*60}")
        print("LIÇÕES PARA O PRÓXIMO VÍDEO:")
        for l in p['empacotamento']:
            print(f"  [Fase 1] {l}")
        for l in p['producao']:
            print(f"  [Produção] {l}")
    if p.get('aviso'):
        print(f"\n  ⚠ {p['aviso']}")


if __name__ == '__main__':
    gerar(verbose='--print' in sys.argv)
