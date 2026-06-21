# -*- coding: utf-8 -*-
"""Gera um vídeo-resumo (~5 min) de um livro a partir de um roteiro JSON.
Estilo: minimalista escuro (slides sóbrios + narração neural pt-BR).
Pipeline 100% local: edge-tts (narração) + Pillow (slides) + ffmpeg (montagem).

Uso:  python gerar_video.py roteiros/arte-da-guerra.json
Saída: videos/<slug>.mp4
"""
import sys, json, subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import imageio_ffmpeg
from mutagen.mp3 import MP3

from _video_tts import _provedor_voz, _tts_eleven, _to_ssml, tts, _intonar
from _video_audio import sintetiza_ambiente

ROOT = Path(__file__).parent
import sys as _sys
if str(ROOT.parent) not in _sys.path:
    _sys.path.insert(0, str(ROOT.parent))
import marca  # fonte ÚNICA de tokens da marca (raiz do projeto)
WORK = ROOT / '_work'
FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
FONTS = Path('C:/Windows/Fonts')

W, H = 1920, 1080
MARGIN = 170
BG = marca.rgb('papel')        # fundo escuro da marca
WHITE = marca.rgb('tinta')     # texto claro
GRAY = marca.rgb('tinta-fraca')
TAIL = 0.7   # silêncio extra ao fim de cada narração (respiro)
FADE = 0.45  # fade in/out por cena (fade-to-black entre cenas)


def font(name, size):
    return ImageFont.truetype(str(FONTS / name), size)

# Tipografia da MARCA via marca.py: Hanken Grotesk (display) + Literata (serif)
F_TITLE = lambda s: marca.font('serif', s, 'Medium')       # serif editorial p/ títulos
F_TITLE_B = lambda s: marca.font('display', s, 'ExtraBold')
F_UI = lambda s: marca.font('display', s, 'Regular')
F_UI_B = lambda s: marca.font('display', s, 'SemiBold')
F_BLACK = lambda s: marca.font('display', s, 'Black')       # peso máximo p/ thumbnail


def hex_rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ''
    for w in words:
        test = (cur + ' ' + w).strip()
        if draw.textlength(test, font=fnt) <= max_w:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def tracked(draw, pos, text, fnt, fill, tracking):
    x, y = pos
    for ch in text:
        draw.text((x, y), ch, font=fnt, fill=fill)
        x += draw.textlength(ch, font=fnt) + tracking


def text_shadow(draw, pos, text, fnt, fill, halo=(4, 4, 7), r=4):
    """Desenha texto com contorno/halo escuro por glifo — protege o texto centrado
    sobre arte de miolo claro (mesma proteção do lower-third, que conta com o
    gradiente forte do darken_side). Anel de offsets + stroke do Pillow."""
    x, y = pos
    for dx in range(-r, r + 1, 2):
        for dy in range(-r, r + 1, 2):
            if dx or dy:
                draw.text((x + dx, y + dy), text, font=fnt, fill=halo)
    draw.text((x, y), text, font=fnt, fill=fill, stroke_width=2, stroke_fill=halo)


def radial_aura(img, color, cx, cy, radius, max_alpha):
    """Aura radial sutil de acento sobre o fundo escuro."""
    aura = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    ad = ImageDraw.Draw(aura)
    steps = 36
    for i in range(steps, 0, -1):
        r = int(radius * i / steps)
        a = int(max_alpha * (1 - i / steps) ** 1.6)
        ad.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color + (a,))
    img.alpha_composite(aura)


def radial_dark(img, cx, cy, rx, ry, max_alpha):
    """Vinheta escura elíptica centrada — garante contraste do texto sobre a foto."""
    ov = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(ov)
    steps = 44
    for i in range(steps, 0, -1):
        a = int(max_alpha * (1 - i / steps) ** 1.5)
        od.ellipse([cx - rx * i / steps, cy - ry * i / steps,
                    cx + rx * i / steps, cy + ry * i / steps], fill=(4, 4, 7, a))
    img.alpha_composite(ov)


def cover(bg_path):
    """Carrega a imagem e a recorta cobrindo 1920x1080 (centralizado)."""
    bg = Image.open(bg_path).convert('RGB')
    s = max(W / bg.width, H / bg.height)
    bg = bg.resize((max(W, int(bg.width * s)), max(H, int(bg.height * s))), Image.LANCZOS)
    x, y = (bg.width - W) // 2, (bg.height - H) // 2
    return bg.crop((x, y, x + W, y + H)).convert('RGBA')


def darken_side(img, side):
    """Escurece um lado (gradiente) p/ o texto, revelando a imagem do outro."""
    ov = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(ov)
    if side == 'left':
        for px in range(0, W, 2):
            a = min(238, int(215 * (1 - px / W) ** 1.25) + 55)
            od.rectangle([(px, 0), (px + 2, H)], fill=(5, 5, 8, a))
    elif side == 'right':
        for px in range(0, W, 2):
            a = min(238, int(215 * (px / W) ** 1.25) + 55)
            od.rectangle([(px, 0), (px + 2, H)], fill=(5, 5, 8, a))
    else:  # center
        od.rectangle([(0, 0), (W, H)], fill=(5, 5, 8, 110))
    # banda inferior: rodapé + barra de progresso sempre legíveis
    for py in range(H - 170, H, 2):
        a = int(150 * ((py - (H - 170)) / 170) ** 1.3)
        od.rectangle([(0, py), (W, py + 2)], fill=(5, 5, 8, a))
    img.alpha_composite(ov)
    if side == 'center':
        # scrim central reforçado: arte de miolo claro (pôr-do-sol) furava o AA-large
        radial_dark(img, W // 2, int(H * 0.48), 1080, 540, 205)


def tracked_width(draw, text, fnt, tracking):
    return sum(draw.textlength(c, font=fnt) + tracking for c in text) - (tracking if text else 0)


def make_slide(cena, accent, idx, total, book_label, out_png, bg_path=None, side='left'):
    accent = hex_rgb_safe(accent)
    has_bg = bool(bg_path)
    if has_bg:
        img = cover(bg_path)
        darken_side(img, side)
    else:
        img = Image.new('RGBA', (W, H), BG + (255,))
        radial_aura(img, accent, W // 2, int(H * 0.30), 720, 26)
    _draw_text(img, cena, accent, idx, total, book_label, side, has_bg)
    img.convert('RGB').save(out_png, quality=95)


def make_overlay(cena, accent, idx, total, book_label, out_png, side='left'):
    """Overlay transparente (gradiente de escurecimento + texto) p/ compor
    sobre um clipe de vídeo em movimento (Veo)."""
    accent = hex_rgb_safe(accent)
    img = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    darken_side(img, side)
    _draw_text(img, cena, accent, idx, total, book_label, side, has_bg=True)
    img.save(out_png)


def _draw_text(img, cena, accent, idx, total, book_label, side, has_bg):
    d = ImageDraw.Draw(img)
    tipo = cena.get('tipo', 'conceito')
    tfill = (245, 245, 248)

    if tipo in ('abertura', 'encerramento'):
        # Centralizado, monumental
        title = cena['titulo']
        ft = F_TITLE(132 if tipo == 'abertura' else 116)
        lines = wrap(d, title, ft, W - 2 * MARGIN)
        line_h = int(ft.size * 1.12)
        block_h = len(lines) * line_h
        y = (H - block_h) // 2 - 20
        for ln in lines:
            lw = d.textlength(ln, font=ft)
            text_shadow(d, ((W - lw) // 2, y), ln, ft, tfill)
            y += line_h
        sub = cena.get('subtitulo')
        if sub:
            fs = F_UI(44)
            sw = d.textlength(sub, font=fs)
            text_shadow(d, ((W - sw) // 2, y + 24), sub, fs,
                        (212, 212, 222) if has_bg else GRAY, r=3)
        d.rectangle([(W // 2 - 60, y + 110), (W // 2 + 60, y + 113)], fill=accent)
    else:
        # Editorial: alterna esquerda / direita p/ ritmo visual
        fk = F_UI_B(32)
        kicker = cena.get('kicker', '').upper()
        Y0, FLOOR = 440, H - 190   # bloco começa em y=440; não pode invadir a banda do rodapé (~910)
        sz = 108
        ft = F_TITLE(sz)
        lines = wrap(d, cena['titulo'], ft, W - 2 * MARGIN - 40)
        # Clamp título×rodapé: encolhe a fonte (re-wrap) até o bloco caber acima do rodapé
        while Y0 + len(lines) * int(ft.size * 1.12) > FLOOR and sz > 64:
            sz -= 8
            ft = F_TITLE(sz)
            lines = wrap(d, cena['titulo'], ft, W - 2 * MARGIN - 40)
        if side == 'right':
            kw = tracked_width(d, kicker, fk, 4)
            d.rectangle([(W - MARGIN - 56, 300), (W - MARGIN, 305)], fill=accent)
            tracked(d, (W - MARGIN - kw, 336), kicker, fk, accent, 4)
            y = Y0
            for ln in lines:
                lw = d.textlength(ln, font=ft)
                d.text((W - MARGIN - lw, y), ln, font=ft, fill=tfill)
                y += int(ft.size * 1.12)
        else:
            ax = MARGIN
            d.rectangle([(ax, 300), (ax + 56, 305)], fill=accent)
            tracked(d, (ax, 336), kicker, fk, accent, 4)
            y = Y0
            for ln in lines:
                d.text((ax, y), ln, font=ft, fill=tfill)
                y += int(ft.size * 1.12)

    # Rodapé + barra de progresso
    fr = F_UI(28)
    d.text((MARGIN, H - 96), book_label, font=fr, fill=(200, 200, 210) if has_bg else (110, 110, 125))
    bx0, bx1, by = MARGIN, W - MARGIN, H - 60
    d.rectangle([(bx0, by), (bx1, by + 3)], fill=(70, 70, 82) if has_bg else (40, 40, 50))
    prog = bx0 + int((bx1 - bx0) * (idx + 1) / total)
    d.rectangle([(bx0, by), (prog, by + 3)], fill=accent)


def hex_rgb_safe(h):
    return hex_rgb(h) if isinstance(h, str) else h


def make_clip(png, mp3, dur, out_mp4, ken_burns=False, kb=0):
    fo = max(0.1, dur - FADE)
    if ken_burns:
        nf = max(2, int(dur * 30))
        cx, cy = "iw/2-(iw/zoom/2)", "ih/2-(ih/zoom/2)"
        zin = "min(zoom+0.0006,1.12)"
        moves = [                                              # variação por cena
            f"z='{zin}':x='{cx}':y='{cy}'",                    # zoom centro
            f"z='{zin}':x='(iw-iw/zoom)*(on/{nf})':y='{cy}'",  # zoom + pan →
            f"z='{zin}':x='(iw-iw/zoom)*(1-on/{nf})':y='{cy}'",  # zoom + pan ←
            f"z='{zin}':x='{cx}':y='(ih-ih/zoom)*(1-on/{nf})'",  # zoom + pan ↑
        ]
        vf = (f"scale=2304:1296,zoompan={moves[kb % 4]}:d={nf}:s=1920x1080:fps=30,"
              f"fade=t=in:st=0:d={FADE},fade=t=out:st={fo:.3f}:d={FADE}")
        subprocess.run([FFMPEG, '-y', '-loop', '1', '-i', str(png), '-i', str(mp3),
                        '-t', f'{dur:.3f}', '-vf', vf,
                        '-c:v', 'libx264', '-pix_fmt', 'yuv420p',
                        '-c:a', 'aac', '-b:a', '192k', '-af', f'apad=pad_dur={TAIL}',
                        '-shortest', str(out_mp4)],
                       check=True, capture_output=True)
    else:
        subprocess.run([FFMPEG, '-y', '-loop', '1', '-i', str(png), '-i', str(mp3),
                        '-t', f'{dur:.3f}', '-r', '30',
                        '-vf', f'fade=t=in:st=0:d={FADE},fade=t=out:st={fo:.3f}:d={FADE}',
                        '-c:v', 'libx264', '-tune', 'stillimage', '-pix_fmt', 'yuv420p',
                        '-c:a', 'aac', '-b:a', '192k', '-af', f'apad=pad_dur={TAIL}',
                        '-shortest', str(out_mp4)],
                       check=True, capture_output=True)


def _clip_dur(path):
    import re
    r = subprocess.run([FFMPEG, '-i', str(path)], capture_output=True, text=True)
    m = re.search(r'Duration: (\d+):(\d+):([\d.]+)', r.stderr)
    return int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3)) if m else 8.0


def make_motion_clip(veo_mp4, overlay_png, mp3, dur, out_mp4, src_dur=None):
    """Clipe com fundo em movimento real (Veo/Kling): palíndromo (vai-e-volta sem
    corte) desacelerado p/ cobrir a narração + overlay de texto + fades."""
    if src_dur is None:
        src_dur = _clip_dur(veo_mp4)   # auto: Kling ~5s, Veo ~8s
    fo = max(0.1, dur - FADE)
    f = max(0.5, dur / (2 * src_dur))   # fator p/ o palíndromo (2x src) cobrir dur
    subprocess.run([FFMPEG, '-y', '-i', str(veo_mp4),
                    '-loop', '1', '-i', str(overlay_png), '-i', str(mp3),
                    '-filter_complex',
                    f"[0:v]split[a][b];[b]reverse[r];[a][r]concat=n=2:v=1,"
                    f"setpts={f:.4f}*PTS,scale=1920:1080:flags=lanczos,fps=30[bg];"
                    f"[bg][1:v]overlay=0:0:eof_action=repeat,"
                    f"fade=t=in:st=0:d={FADE},fade=t=out:st={fo:.3f}:d={FADE}[v];"
                    f"[2:a]apad=pad_dur={TAIL}[a]",
                    '-map', '[v]', '-map', '[a]', '-t', f'{dur:.3f}',
                    '-c:v', 'libx264', '-pix_fmt', 'yuv420p',
                    '-c:a', 'aac', '-b:a', '192k', str(out_mp4)],
                   check=True, capture_output=True)


def main(roteiro_path):
    cfg = json.loads(Path(roteiro_path).read_text(encoding='utf-8'))
    try:
        from contracts import load_roteiro
    except ImportError:
        pass  # pydantic/contracts.py ausente no ambiente — sem validação
    else:
        # Guarda dura: roteiro inválido aborta ANTES de qualquer chamada de API paga.
        load_roteiro(roteiro_path)
    slug = cfg['slug']
    import os as _os; _os.environ['PIPELINE_SLUG'] = slug
    accent = cfg.get('acento', marca.hex_of('ouro'))
    voice = cfg.get('voz', 'pt-BR-AntonioNeural')
    book_label = f"{cfg['titulo'].upper()}  ·  {cfg['autor'].upper()}"
    estilo = cfg.get('estilo_img', '')
    cenas = cfg['cenas']
    n = len(cenas)

    WORK.mkdir(exist_ok=True)
    IMGDIR = ROOT / '_img'
    IMGDIR.mkdir(exist_ok=True)
    MOTDIR = ROOT / '_motion'
    MOTDIR.mkdir(exist_ok=True)
    usa_img = any(c.get('img') for c in cenas)
    usa_mot = any(c.get('motion') for c in cenas)
    # Provedor de geração: "google" (Imagen+Veo) ou "fal" (Flux+Kling). Default google.
    provider = cfg.get('provider', 'google')
    img_gen = mot_gen = None
    if provider in ('base', 'none'):
        usa_img = usa_mot = False   # slides escuros + Ken Burns, sem geração paga (R$0)
    elif provider == 'fal':
        import falgen
        img_gen, mot_gen = falgen.gen, falgen.animate
    else:
        if usa_img:
            import imagen
            img_gen = imagen.gen
        if usa_mot:
            import veo
            mot_gen = veo.animate

    import cinegrafista                                  # Cinegrafista NORMAL (parallax grátis / fallback Ken Burns)
    import splatting                                      # Cinegrafista 3D (3D Gaussian Splatting na GPU local)
    clips = []
    durs = []   # duração on-screen de cada cena (p/ legendas/capítulos da lane YouTube)
    label = {'fal': 'Flux + Kling', 'google': 'Imagen + Veo'}.get(provider, provider)
    print(f"Gerando '{cfg['titulo']}' — {n} cenas"
          + (f" · imagens IA + movimento ({label})" if usa_img else ""))
    for i, cena in enumerate(cenas):
        mp3 = WORK / f'a{i:02d}.mp3'
        png = WORK / f's{i:02d}.png'
        clip = WORK / f'c{i:02d}.mp4'

        bg = None
        if cena.get('img') and img_gen:   # base/none: img_gen=None → slide escuro
            bg = IMGDIR / f'{slug}_{i:02d}.png'
            if not bg.exists():  # cache: não regenera (e não recobra) imagem já feita
                full = f"{cena['img']}, {estilo}" if estilo else cena['img']
                if not img_gen(full, str(bg), aspect='16:9'):
                    raise RuntimeError(f'Geração de imagem falhou na cena {i+1}')
                print(f"  imagem {i+1}/{n} gerada")

        mot = None
        if cena.get('motion') and bg and mot_gen:
            mot = MOTDIR / f'{slug}_{i:02d}.mp4'
            if not mot.exists():  # cache: clipe de movimento é pago — nunca regenera
                print(f"  animando cena {i+1}/{n}...")
                try:
                    if not mot_gen(str(bg), cena['motion'], str(mot)):
                        print(f"  [!] movimento falhou na cena {i+1} — usando Ken Burns")
                        mot = None
                except Exception as _me:
                    print(f"  [!] movimento falhou ({type(_me).__name__}: {str(_me)[:80]}) — usando Ken Burns")
                    mot = None

        # Cinegrafista 3D: imagem sem movimento pago → 3D Gaussian Splatting na GPU local
        # (cena 3D navegável, melhor profundidade). Dormente sem torch+CUDA + motor 3DGS.
        if not mot and bg and not mot_gen and splatting.gaussian_disponivel():
            gsp = MOTDIR / f'{slug}_{i:02d}_3dgs.mp4'
            if gsp.exists() or splatting.splat_clip(str(bg), str(gsp)):
                mot = gsp
                print(f"  cena {i+1}/{n}: 3D Gaussian Splatting (GPU local)")

        # Cinegrafista NORMAL: imagem grátis sem movimento pago → parallax 2.5D (DepthFlow);
        # rota de fuga = Ken Burns. Dormente enquanto DepthFlow não estiver instalado.
        if not mot and bg and not mot_gen and cinegrafista.depthflow_disponivel():
            dfp = MOTDIR / f'{slug}_{i:02d}_df.mp4'
            if dfp.exists() or cinegrafista.parallax(str(bg), str(dfp)):
                mot = dfp
                print(f"  cena {i+1}/{n}: parallax 2.5D (DepthFlow, grátis)")

        tipo = cena.get('tipo', 'conceito')
        side = 'center' if tipo in ('abertura', 'encerramento') else ('left' if i % 2 == 1 else 'right')

        tts(cena['narracao'], voice, mp3, rate=cfg.get('tts_rate', 1.0))
        dur = MP3(mp3).info.length + TAIL
        durs.append(dur)
        if mot:
            make_overlay(cena, accent, i, n, book_label, png, side=side)
            make_motion_clip(mot, png, mp3, dur, clip)
        else:
            make_slide(cena, accent, i, n, book_label, png, bg_path=bg, side=side)
            make_clip(png, mp3, dur, clip, ken_burns=bool(bg), kb=i)
        clips.append(clip)
        print(f"  cena {i+1}/{n}: {dur:.1f}s  · {cena['titulo'][:40]}"
              + ("  [movimento]" if mot else ""))

    # concat (vídeo + narração)
    listf = WORK / 'list.txt'
    listf.write_text(''.join(f"file '{c.as_posix()}'\n" for c in clips), encoding='utf-8')
    narr = WORK / '_narr.mp4'
    subprocess.run([FFMPEG, '-y', '-f', 'concat', '-safe', '0', '-i', str(listf),
                    '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k',
                    str(narr)], check=True, capture_output=True)

    # Pós-produção desacoplada: sintetiza a trilha, persiste os stems (D·M·E) e
    # roda o Mix & Master a partir deles — re-executável via `mixmaster.py <slug>`.
    import mixmaster
    mus = None
    if cfg.get('musica'):
        dur_total = sum(MP3(WORK / f'a{i:02d}.mp3').info.length + TAIL for i in range(n))
        mus = WORK / '_music.wav'
        energia = float(cfg.get('musica_energia', 0.65))   # ritmo/energia da trilha (0=contemplativo … 1=enérgico)
        sintetiza_ambiente(dur_total + 2, mus, energia=energia)
        print(f"  trilha ambiente sintetizada: {dur_total:.0f}s (energia={energia})")
    mixmaster.export_stems(slug, narr, mus)                 # _stems/<slug>/ (D·M·E + vídeo mudo)
    (ROOT / '_stems' / slug / 'timing.json').write_text(    # timing p/ legendas/capítulos (lane YouTube)
        json.dumps({'tail': TAIL, 'durs': durs}, ensure_ascii=False), encoding='utf-8')
    try:                                                    # Sonoplasta: batidas de transição em arco de comoção (Fibonacci)
        import efeitos_transicao
        efeitos_transicao.main(str(roteiro_path))           # escreve _stems/<slug>/efeitos.wav (antes do master)
    except (Exception, SystemExit) as e:                    # nunca aborta o build por causa da camada de batidas
        print(f"  [aviso] camada de batidas pulada: {e}")
    out = mixmaster.master(slug, ROOT / f'{slug}.mp4')      # Mix & Master a partir dos stems (já com efeitos.wav)
    print(f"\nOK -> {out}  ·  stems em _stems/{slug}/  ·  re-mix: python mixmaster.py {slug}")

    # Gate de QC: sinaliza e registra o veredicto — NÃO destrói a mídia cara em caso de reprovação.
    # A mídia fica; o que o gate barra é a PUBLICAÇÃO (consultar qc.aprovado(slug) antes de subir).
    import qc as _qc
    _falhas, _avisos = _qc.coletar(roteiro_path, out)
    _veredicto = _qc.montar_veredicto(_falhas, _avisos)
    _qc.salvar_veredicto(slug, _veredicto)
    print('=== QC — Gate 2 do estúdio ===')
    if _falhas:
        print(f'FALHAS ({len(_falhas)}):')
        for _f in _falhas:
            print('  [REPROVA]', _f)
    else:
        print('FALHAS: nenhuma')
    if _avisos:
        print(f'AVISOS ({len(_avisos)}):')
        for _a in _avisos:
            print('  [aviso]', _a)
    _status = 'APROVADO' if _veredicto['aprovado'] else 'REPROVADO'
    print(f"VEREDICTO: {_status}  ·  veredicto em _stems/{slug}/qc.json")


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else ROOT / 'roteiros' / 'arte-da-guerra.json')
