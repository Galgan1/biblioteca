# -*- coding: utf-8 -*-
"""Cinegrafista NORMAL — movimento sem custo de API.

Dá vida às imagens estáticas. Preferência na lane NORMAL: DepthFlow (parallax 2.5D
real, local/grátis) quando disponível; senão rota de fuga = Ken Burns (zoompan do
ffmpeg, que sempre existe). Mesmo padrão soberano do tts(): a produção nunca para
por falta de uma dependência pesada — degrada para o que está à mão.

DepthFlow precisa de torch + (idealmente) GPU (`pip install depthflow`). Enquanto
ausente, `depthflow_disponivel()` é False e o pipeline roda IDÊNTICO ao histórico
(Ken Burns). A CLI não fica no PATH — invocada via `python -m depthflow`.
Flags corretas (v1.0): input -i <img> main -o <out> -t <dur> -f <fps>
No Windows: NO_COLOR=1 + PYTHONIOENCODING=utf-8 evitam UnicodeError do Rich/dearlog.
"""
import importlib.util
import os
import subprocess
import sys
from pathlib import Path


def tratamento(modo, tem_imagem, motion_pago, depthflow_ok, gaussian_ok=False):
    """PURO: escolhe o tratamento de movimento da cena (do melhor ao mais simples).
      'motion'    — clipe de movimento pago já produzido (Veo/Kling)
      'gaussian'  — 3D Gaussian Splatting local na GPU (cena 3D navegável; melhor local)
      'parallax'  — DepthFlow 2.5D grátis (com imagem)
      'ken_burns' — zoompan do ffmpeg sobre a imagem (rota de fuga)
      'still'     — slide sem imagem (sem movimento)
    gaussian_ok default False → assinatura antiga (4 args) mantém o comportamento."""
    if motion_pago:
        return 'motion'
    if tem_imagem and gaussian_ok:
        return 'gaussian'                       # 3DGS é o melhor tratamento LOCAL quando há GPU/motor
    if tem_imagem and modo == 'normal' and depthflow_ok:
        return 'parallax'
    if tem_imagem:
        return 'ken_burns'
    return 'still'


def depthflow_disponivel():
    """True se o módulo depthflow for importável (CLI invocada via python -m depthflow)."""
    try:
        return importlib.util.find_spec('depthflow') is not None
    except Exception:
        return False


def _depthflow_cmd(src_png, out_mp4, dur, fps):
    """Comando DepthFlow via python -m depthflow (v1.0).
    Subcomandos em sequência: input -i <img>  main -o <out> -t <dur> -f <fps>
    -t = duração total (segundos); -f = fps (flag correta na v1.0, não --fps)."""
    return [sys.executable, '-m', 'depthflow',
            'input', '-i', str(src_png),
            'main', '-o', str(out_mp4), '-t', f'{dur:g}', '-f', str(fps)]


_CLIPE_MIN_BYTES = 1024   # abaixo disso o "clipe" é fantasma (vazio/quebrado), não sucesso


def parallax(src_png, out_mp4, dur=6.0, fps=30):
    """Renderiza um clipe parallax 2.5D (mudo) a partir de uma imagem. Devolve True
    em sucesso; False se DepthFlow indisponível ou se o render falhar (nunca levanta).
    O caller faz fallback para Ken Burns quando isto devolve False.

    NO_COLOR=1 + PYTHONIOENCODING=utf-8: evitam UnicodeError do Rich/dearlog no
    Windows (cp1252 não suporta os box-drawing chars usados pelo logger do DepthFlow).
    capture_output=True + sem text=True: bytes brutos, nenhum decode no processo-filho.

    Pilar 7 (erro COM contexto): em vez de engolir a falha muda, registra o MOTIVO
    em stderr antes de cair no Ken Burns — senão o debug fica às cegas. E aplica
    anti-fantasma: arquivo ausente/vazio NÃO conta como sucesso."""
    if not depthflow_disponivel():
        return False
    env = os.environ.copy()
    env.update({'NO_COLOR': '1', 'PYTHONIOENCODING': 'utf-8'})
    try:
        subprocess.run(_depthflow_cmd(src_png, out_mp4, dur, fps),
                       check=True, capture_output=True, env=env)
    except subprocess.CalledProcessError as e:
        _err = (e.stderr or b'')[-400:].decode('utf-8', 'replace').strip()
        print(f"[cinegrafista] DepthFlow rc={e.returncode} em {Path(src_png).name} "
              f"-> Ken Burns. detalhe: {_err or '(sem stderr)'}", file=sys.stderr)
        return False
    except Exception as e:
        print(f"[cinegrafista] DepthFlow {type(e).__name__}: {str(e)[:200]} "
              f"em {Path(src_png).name} -> Ken Burns", file=sys.stderr)
        return False
    out = Path(out_mp4)
    tam = out.stat().st_size if out.exists() else 0
    if tam < _CLIPE_MIN_BYTES:
        print(f"[cinegrafista] DepthFlow nao gerou clipe valido em {out.name} "
              f"(size={tam}) -> Ken Burns", file=sys.stderr)
        return False
    return True
