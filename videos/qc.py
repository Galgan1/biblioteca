# -*- coding: utf-8 -*-
"""QC — Gate 2 do estúdio (rúbrica de 4 estágios), executável (Akita: verde = exit code).

Roda ANTES de publicar. As avaliações são funções PURAS (testáveis sem render);
um coletor mede o arquivo real (resolução + loudness via ffmpeg) e agrega.

  Bloqueiam (exit 1): resolução < 1080p, true peak acima de -1 dBTP, pt-PT no roteiro,
                      link de afiliado que não seja de PRODUTO (/dp/, /gp/).
  Avisam (não derrubam): loudness fora do alvo, poucas composições, cena densa, sem CTA.

Uso:  python qc.py <roteiro.json> [video.mp4]
Read-only: não muta nada. Exit 0 = aprovado; 1 = reprovado.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

import compliance   # Conferente de direitos — fonte única das regras de direito

ROOT = Path(__file__).parent
LUFS_ALVO = -14.0
TP_MAX = -1.0
RES_MIN = 1080          # menor dimensão mínima (1920x1080 ou 1080x1920)
NARRACAO_MAX = 52       # palavras/cena de narração (convenção do projeto p/ caber no ritmo); slide usa 35

# Marcadores fortes de pt-PT (errados em pt-BR). Conservador p/ evitar falso positivo.
_PT_PT = [
    'utilizador', 'ecrã', 'telemóvel', 'autocarro', 'comboio', 'pequeno-almoço',
    'casa de banho', 'registo', 'facto', 'contacto', 'óptimo', 'óptima',
    'acção', 'direcção', 'colecção', 'actividade', 'sandes', 'autocarros',
]


def detectar_pt_pt(texto):
    """-> lista de marcadores pt-PT encontrados em *texto* (case-insensitive)."""
    t = (texto or '').lower()
    achados = []
    for m in _PT_PT:
        # fronteira de palavra (mas '-' e espaço de 'casa de banho'/'pequeno-almoço' contam)
        if re.search(r'(?<![\wáéíóúâêôãõàç])' + re.escape(m) + r'(?![\wáéíóúâêôãõàç])', t):
            achados.append(m)
    return achados


def avaliar_tecnico(largura, altura, lufs, true_peak):
    """-> (falhas, avisos). Resolução e clipping bloqueiam; loudness fora do alvo avisa."""
    falhas, avisos = [], []
    if largura and altura and min(largura, altura) < RES_MIN:
        falhas.append(f'resolução abaixo de 1080p ({largura}x{altura})')
    if true_peak is not None and true_peak > TP_MAX:
        falhas.append(f'true peak {true_peak:.1f} dBTP acima de {TP_MAX} (risco de clip)')
    if lufs is None:
        avisos.append('loudness não medido')
    elif abs(lufs - LUFS_ALVO) > 2.0:
        avisos.append(f'loudness {lufs:.1f} LUFS fora do alvo {LUFS_ALVO}')
    return falhas, avisos


def avaliar_producao(cenas):
    """-> avisos (heurística anti-slop, não bloqueia): >=4 composições distintas."""
    avisos = []
    if len(cenas or []) < 4:
        avisos.append(f'apenas {len(cenas or [])} cenas — pouca variação visual (alvo >=4)')
    return avisos


def avaliar_conteudo(cenas):
    """-> (falhas, avisos). pt-PT e ausência de gancho bloqueiam; CTA e densidade avisam."""
    falhas, avisos = [], []
    tipos = {c.get('tipo') for c in (cenas or [])}
    if 'abertura' not in tipos:
        falhas.append('sem cena de abertura (gancho dos primeiros segundos)')
    if 'encerramento' not in tipos:
        avisos.append('sem cena de encerramento (CTA)')
    try:
        from text_budget import excede
    except Exception:
        excede = None
    for i, c in enumerate(cenas or []):
        nar = c.get('narracao', '')
        pt = detectar_pt_pt(nar)
        if pt:
            falhas.append(f'cena {i+1}: pt-PT {pt}')
        if excede and excede(nar, NARRACAO_MAX):
            avisos.append(f'cena {i+1}: narração densa (>{NARRACAO_MAX} palavras)')
    return falhas, avisos


# As regras de direito vivem no Conferente (compliance.py) — fonte única. O qc
# reexporta o validador de link e delega a auditoria de links, sem duplicar a regra.
link_amazon_valido = compliance.link_amazon_valido


def avaliar_compliance(links):
    """-> falhas (BLOQUEANTE): todo link de afiliado tem de ser de produto. Delega ao Conferente."""
    return compliance.auditar_links(links)


def exit_code(falhas):
    return 1 if falhas else 0


def montar_veredicto(falhas, avisos):
    """PURA: converte (falhas, avisos) -> dict JSON-serializável do veredicto."""
    return {'aprovado': len(falhas) == 0, 'falhas': list(falhas), 'avisos': list(avisos)}


def salvar_veredicto(slug, veredicto, stems_root=None):
    """Persiste o veredicto em _stems/<slug>/qc.json. Sobrescreve se já existir."""
    raiz = (stems_root or ROOT) / '_stems' / slug
    raiz.mkdir(parents=True, exist_ok=True)
    (raiz / 'qc.json').write_text(
        json.dumps(veredicto, ensure_ascii=False, indent=2), encoding='utf-8'
    )


def aprovado(slug, stems_root=None):
    """Consulta de publicação: lê _stems/<slug>/qc.json e devolve bool.
    Devolve False se o arquivo não existir, estiver corrompido ou reprovar."""
    caminho = (stems_root or ROOT) / '_stems' / slug / 'qc.json'
    try:
        dados = json.loads(caminho.read_text(encoding='utf-8'))
        return bool(dados.get('aprovado', False))
    except Exception:
        return False


# --------------------------------------------------------------------------
# Coletor (I/O): mede o arquivo real e agrega os estágios
# --------------------------------------------------------------------------

def _parse_resolucao(stderr):
    """PURA: -> (largura, altura) da 1ª resolução WxH no stderr do ffmpeg; (None, None)."""
    m = re.search(r'(\d{3,4})x(\d{3,4})', stderr)
    return (int(m.group(1)), int(m.group(2))) if m else (None, None)


def _parse_loudness(stderr):
    """PURA: -> LUFS integrado do arquivo (campo input_i do loudnorm); None se ausente.

    Lê o bloco JSON final do loudnorm (uma medição do arquivo INTEIRO). NÃO casa com
    as linhas de progresso do ebur128, que começam no piso -70 LUFS no 1º frame — era
    daí que vinha o falso -70 (re.search pegava a 1ª, não a medição final)."""
    m = re.search(r'\{[^{}]*"input_i"[^{}]*\}', stderr, re.DOTALL)
    if not m:
        return None
    try:
        return float(json.loads(m.group(0))['input_i'])
    except (ValueError, KeyError):
        return None


def medir_arquivo(video_path):
    """-> (largura, altura, lufs, true_peak). Mede o ARQUIVO FINAL com ffmpeg:
    resolução + loudness integrado (loudnorm print_format=json). None se indisponível.
    true_peak segue não medido aqui (gate de clipping recebe None -> pula)."""
    try:
        import imageio_ffmpeg
        ff = imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        return None, None, None, None
    try:
        r = subprocess.run(
            [ff, '-i', str(video_path), '-af', 'loudnorm=print_format=json', '-f', 'null', '-'],
            capture_output=True, text=True)
    except Exception:
        return None, None, None, None
    w, h = _parse_resolucao(r.stderr)
    return w, h, _parse_loudness(r.stderr), None


def coletar(roteiro_path, video_path=None):
    """Roda os 4 estágios sobre o roteiro (+ vídeo, se houver). -> (falhas, avisos)."""
    cfg = json.loads(Path(roteiro_path).read_text(encoding='utf-8'))
    cenas = cfg.get('cenas', [])
    links = cfg.get('afiliado_links') or ([cfg['afiliado']] if cfg.get('afiliado') else [])
    falhas, avisos = [], []

    fc, ac = avaliar_conteudo(cenas)
    falhas += fc; avisos += ac
    avisos += avaliar_producao(cenas)
    falhas += avaliar_compliance(links)
    fcomp, acomp = compliance.auditar(cfg)   # Conferente: prompts de imagem (IP) + licença de trilha
    falhas += fcomp; avisos += acomp

    if video_path and Path(video_path).exists():
        w, h, lufs, tp = medir_arquivo(video_path)
        ft, at = avaliar_tecnico(w, h, lufs, tp)
        falhas += ft; avisos += at
    else:
        avisos.append('vídeo não fornecido — estágio técnico pulado')

    return falhas, avisos


def main():
    if len(sys.argv) < 2:
        sys.exit('uso: python qc.py <roteiro.json> [video.mp4]')
    roteiro = sys.argv[1]
    video = sys.argv[2] if len(sys.argv) > 2 else None
    falhas, avisos = coletar(roteiro, video)
    print('=== QC — Gate 2 do estúdio ===')
    print(f'FALHAS ({len(falhas)}):' if falhas else 'FALHAS: nenhuma')
    for x in falhas:
        print('  [REPROVA]', x)
    if avisos:
        print(f'AVISOS ({len(avisos)}):')
        for x in avisos:
            print('  [aviso]', x)
    code = exit_code(falhas)
    print(f"\nVEREDICTO: {'APROVADO' if code == 0 else 'REPROVADO'} (exit {code})")
    return code


if __name__ == '__main__':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.exit(main())
