# -*- coding: utf-8 -*-
"""Estágio de PÓS-PRODUÇÃO desacoplado — stems (D·M·E) + Mix & Master re-executável.

Separa as DECISÕES de áudio da MÍDIA cara (Imagen/Veo/TTS). O build (`gerar_video.py`)
renderiza a mídia uma vez e chama `export_stems`; daí o master é só um passe de
mixagem, que pode ser refeito quantas vezes quiser SEM re-renderizar nada.

Stems em `_stems/<slug>/`:
  - video_mudo.mp4   vídeo sem áudio
  - voz.wav          diálogo (narração, comprimento total)
  - trilha.wav       música (se houver)
  - efeitos.wav      efeitos/SFX (opcional — gancho da camada de sonoplastia)
  - mix.json         decisões de mix (níveis, loudness) — editável p/ pós-edição

Pós-edição: edite `_stems/<slug>/mix.json` (ex.: music_gain, loudnorm) e rode
`python mixmaster.py <slug>` → novo master em segundos.

CLI:  python mixmaster.py <slug>            # re-mixa o master a partir dos stems
      python mixmaster.py <slug> out.mp4    # master num caminho específico
"""

import sys, json, subprocess
from pathlib import Path
import imageio_ffmpeg

ROOT = Path(__file__).parent
FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
STEMS = ROOT / '_stems'

# Defaults de mix (iguais ao comportamento histórico: trilha ~-19 dB sob a voz)
DEFAULT_MIX = {"music_gain": 0.11, "sfx_gain": 1.0, "loudnorm": False, "lufs": -14, "tp": -1.0}


def _run(args):
    subprocess.run(args, check=True, capture_output=True)


def export_stems(slug, narr_mp4, music_wav=None, efeitos_wav=None):
    """Persiste os stems de um build em _stems/<slug>/. Não sobrescreve mix.json
    (preserva decisões de pós-edição entre rebuilds)."""
    d = STEMS / slug
    d.mkdir(parents=True, exist_ok=True)
    # vídeo mudo (faixa de vídeo, sem áudio)
    _run([FFMPEG, '-y', '-i', str(narr_mp4), '-an', '-c:v', 'copy', str(d / 'video_mudo.mp4')])
    # voz (diálogo) — extrai a faixa de áudio do _narr (voz limpa, já com pausas, sem trilha)
    _run([FFMPEG, '-y', '-i', str(narr_mp4), '-vn', '-c:a', 'pcm_s16le', str(d / 'voz.wav')])
    # trilha (música)
    trilha = d / 'trilha.wav'
    if music_wav and Path(music_wav).exists():
        _run([FFMPEG, '-y', '-i', str(music_wav), '-c:a', 'pcm_s16le', str(trilha)])
    elif trilha.exists():
        trilha.unlink()
    # efeitos (opcional — camada de SFX da sonoplastia, quando existir)
    efe = d / 'efeitos.wav'
    if efeitos_wav and Path(efeitos_wav).exists():
        _run([FFMPEG, '-y', '-i', str(efeitos_wav), '-c:a', 'pcm_s16le', str(efe)])
    elif efe.exists():
        efe.unlink()
    # mix.json default (preserva edições de pós existentes)
    mj = d / 'mix.json'
    if not mj.exists():
        mj.write_text(json.dumps(DEFAULT_MIX, ensure_ascii=False, indent=1), encoding='utf-8')
    return d


def master(slug, out=None):
    """Re-monta o master a partir dos stems + mix.json — segundos, sem re-render."""
    d = STEMS / slug
    video, voz, trilha, efe = (
        d / 'video_mudo.mp4',
        d / 'voz.wav',
        d / 'trilha.wav',
        d / 'efeitos.wav',
    )
    if not video.exists() or not voz.exists():
        sys.exit(f'[!] stems ausentes em {d} — rode o build (gerar_video.py) primeiro.')
    mix = {
        **DEFAULT_MIX,
        **(json.loads(mj.read_text(encoding='utf-8')) if (mj := d / 'mix.json').exists() else {}),
    }
    out = Path(out) if out else ROOT / f'{slug}.mp4'

    inp = ['-i', str(video), '-i', str(voz)]  # 0:v vídeo · 1:a voz
    parts, idx, cur = [], 2, '[1:a]'  # voz soberana
    if trilha.exists():
        inp += ['-i', str(trilha)]
        parts.append(f'[{idx}:a]volume={mix["music_gain"]}[m]')
        parts.append(f'{cur}[m]amix=inputs=2:duration=first:dropout_transition=2[vt]')
        cur = '[vt]'
        idx += 1
    if efe.exists():
        # SFX (sonoplastia) entra por uma 2ª soma SEM normalização (normalize=0): não
        # rebaixa voz/trilha. O knock cai no respiro entre cenas, onde a voz está em
        # silêncio — então o pico somado não clipa. (Só ativa se efeitos.wav existir.)
        inp += ['-i', str(efe)]
        parts.append(f'[{idx}:a]volume={mix["sfx_gain"]}[e]')
        parts.append(f'{cur}[e]amix=inputs=2:duration=first:normalize=0[ve]')
        cur = '[ve]'
        idx += 1
    if mix.get('loudnorm'):
        parts.append(f'{cur}loudnorm=I={mix["lufs"]}:TP={mix["tp"]}:LRA=11[a]')
        cur = '[a]'
    last = cur

    args = [FFMPEG, '-y', *inp]
    amap = '1:a'
    if parts:
        args += ['-filter_complex', ';'.join(parts)]
        amap = last
    args += ['-map', '0:v', '-map', amap, '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', str(out)]
    _run(args)
    extras = (
        (' +trilha' if trilha.exists() else '')
        + (' +SFX' if efe.exists() else '')
        + (' +loudnorm' if mix.get('loudnorm') else '')
    )
    print(f"OK master -> {out}  ({out.stat().st_size / 1e6:.1f} MB){extras}")
    return out


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit("uso: python mixmaster.py <slug> [saida.mp4]")
    master(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
