# -*- coding: utf-8 -*-
"""Gera um vídeo-resumo (~5 min) de um livro a partir de um roteiro JSON.
Estilo: minimalista escuro (slides sóbrios + narração neural pt-BR).
Pipeline 100% local: edge-tts (narração) + Pillow (slides) + ffmpeg (montagem).

Uso:  python gerar_video.py roteiros/arte-da-guerra.json
Saída: videos/<slug>.mp4
"""

import sys, json, subprocess, wave, struct
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import imageio_ffmpeg
import numpy as np
from mutagen.mp3 import MP3

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
BG = marca.rgb('papel')  # fundo escuro da marca
WHITE = marca.rgb('tinta')  # texto claro
GRAY = marca.rgb('tinta-fraca')
TAIL = 0.7  # silêncio extra ao fim de cada narração (respiro)
FADE = 0.45  # fade in/out por cena (fade-to-black entre cenas)


def font(name, size):
    return ImageFont.truetype(str(FONTS / name), size)


# Tipografia da MARCA via marca.py: Hanken Grotesk (display) + Literata (serif)
F_TITLE = lambda s: marca.font('serif', s, 'Medium')  # serif editorial p/ títulos
F_TITLE_B = lambda s: marca.font('display', s, 'ExtraBold')
F_UI = lambda s: marca.font('display', s, 'Regular')
F_UI_B = lambda s: marca.font('display', s, 'SemiBold')
F_BLACK = lambda s: marca.font('display', s, 'Black')  # peso máximo p/ thumbnail


def hex_rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i : i + 2], 16) for i in (0, 2, 4))


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
        od.ellipse(
            [cx - rx * i / steps, cy - ry * i / steps, cx + rx * i / steps, cy + ry * i / steps],
            fill=(4, 4, 7, a),
        )
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
        od.rectangle([(0, 0), (W, H)], fill=(5, 5, 8, 70))
    # banda inferior: rodapé + barra de progresso sempre legíveis
    for py in range(H - 170, H, 2):
        a = int(150 * ((py - (H - 170)) / 170) ** 1.3)
        od.rectangle([(0, py), (W, py + 2)], fill=(5, 5, 8, a))
    img.alpha_composite(ov)
    if side == 'center':
        radial_dark(img, W // 2, int(H * 0.48), 1000, 470, 150)


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
            d.text(((W - lw) // 2, y), ln, font=ft, fill=tfill)
            y += line_h
        sub = cena.get('subtitulo')
        if sub:
            fs = F_UI(44)
            sw = d.textlength(sub, font=fs)
            d.text(((W - sw) // 2, y + 24), sub, font=fs, fill=(212, 212, 222) if has_bg else GRAY)
        d.rectangle([(W // 2 - 60, y + 110), (W // 2 + 60, y + 113)], fill=accent)
    else:
        # Editorial: alterna esquerda / direita p/ ritmo visual
        fk = F_UI_B(32)
        kicker = cena.get('kicker', '').upper()
        ft = F_TITLE(108)
        lines = wrap(d, cena['titulo'], ft, W - 2 * MARGIN - 40)
        if side == 'right':
            kw = tracked_width(d, kicker, fk, 4)
            d.rectangle([(W - MARGIN - 56, 300), (W - MARGIN, 305)], fill=accent)
            tracked(d, (W - MARGIN - kw, 336), kicker, fk, accent, 4)
            y = 440
            for ln in lines:
                lw = d.textlength(ln, font=ft)
                d.text((W - MARGIN - lw, y), ln, font=ft, fill=tfill)
                y += int(ft.size * 1.12)
        else:
            ax = MARGIN
            d.rectangle([(ax, 300), (ax + 56, 305)], fill=accent)
            tracked(d, (ax, 336), kicker, fk, accent, 4)
            y = 440
            for ln in lines:
                d.text((ax, y), ln, font=ft, fill=tfill)
                y += int(ft.size * 1.12)

    # Rodapé + barra de progresso
    fr = F_UI(28)
    d.text(
        (MARGIN, H - 96), book_label, font=fr, fill=(200, 200, 210) if has_bg else (110, 110, 125)
    )
    bx0, bx1, by = MARGIN, W - MARGIN, H - 60
    d.rectangle([(bx0, by), (bx1, by + 3)], fill=(70, 70, 82) if has_bg else (40, 40, 50))
    prog = bx0 + int((bx1 - bx0) * (idx + 1) / total)
    d.rectangle([(bx0, by), (prog, by + 3)], fill=accent)


def hex_rgb_safe(h):
    return hex_rgb(h) if isinstance(h, str) else h


def sintetiza_ambiente(dur, out_wav, seed=7, energia=0.65):
    """Leito procedural livre de direitos em Ré menor — agora com PULSO RÍTMICO
    (parâmetro `energia` 0..1) para uma trilha mais dinâmica e enérgica, SEM perder a
    identidade do canal nem a voz soberana. Sonnenschein cap.5: ritmo/andamento → energia.
      energia=0   → pad contemplativo puro (comportamento antigo);
      energia~0.65 → leito pulsante + batida de coração grave (padrão do canal);
      energia=1.0 → mais movimento. Tunável por vídeo via cfg 'musica_energia'
    (livros contemplativos pedem menos; tática/ação/ofício pedem mais)."""
    sr = 44100
    rng = np.random.default_rng(seed)
    energia = max(0.0, min(1.0, energia))
    # Progressão modal contemplativa (Ré menor), graves + camada de oitava
    prog = [
        [146.83, 220.00, 293.66],  # Dm  (D3 A3 D4)
        [116.54, 174.61, 233.08],  # Bb  (Bb2 F3 Bb3)
        [174.61, 220.00, 261.63],  # F    (F3 A3 C4)
        [146.83, 196.00, 233.08],  # Gm  (D3 G3 Bb3)
    ]
    seg = 24.0 - 4.0 * energia  # mais enérgico = harmonia anda mais rápido (24s → 20s)
    xf = 6.0  # crossfade entre acordes
    n_total = int(dur * sr)
    out = np.zeros(n_total, dtype=np.float64)
    bpm = 60.0 + 18.0 * energia  # andamento do pulso (60 → 78 BPM)
    beat = 60.0 / bpm

    def voice(freqs, length, t0):
        t = np.arange(length) / sr
        sig = np.zeros(length)
        for f in freqs:
            for h, amp in [(1, 1.0), (2, 0.18), (3, 0.08)]:
                det = 0.18 * h
                sig += (
                    amp
                    * (
                        np.sin(2 * np.pi * (f * h + det) * t)
                        + np.sin(2 * np.pi * (f * h - det) * t)
                    )
                    * 0.5
                )
            sig += 0.10 * np.sin(2 * np.pi * f * 2 * t)  # shimmer de oitava
        # gate RÍTMICO (o pad pulsa no tempo) + resíduo de tremolo lento
        gate = 1 - (0.24 * energia) * (
            0.5 - 0.5 * np.cos(2 * np.pi * ((t + t0) / beat))
        )  # cheio no tempo, recua entre tempos
        slow = 0.88 + 0.12 * np.sin(2 * np.pi * 0.05 * t + rng.random() * 6.28)
        env = np.ones(length)
        nxf = int(xf * sr)
        env[:nxf] = np.sin(np.linspace(0, np.pi / 2, nxf)) ** 2
        env[-nxf:] = np.sin(np.linspace(np.pi / 2, 0, nxf)) ** 2
        return sig * gate * slow * env / max(1, len(freqs))

    pos, i = 0, 0
    step = int((seg - xf) * sr)
    while pos < n_total:
        length = int(seg * sr)
        v = voice(prog[i % len(prog)], length, pos / sr)
        end = min(pos + length, n_total)
        out[pos:end] += v[: end - pos]
        pos += step
        i += 1

    # batida de coração: pulso grave no tempo (raiz do acorde, oitava abaixo) — a energia
    if energia > 0:
        plen = int(0.5 * sr)
        tt = np.arange(plen) / sr
        penv = (1 - np.exp(-tt / 0.004)) * np.exp(-tt / 0.16)  # pluck: ataque rápido, decay curto
        for k in range(int(np.ceil(dur / beat))):
            tb = k * beat
            ic = int(tb / max(1e-9, (seg - xf))) % len(prog)  # acorde tocando em tb
            root = prog[ic][0] / 2.0  # oitava abaixo da fundamental
            accent = 1.0 if (k % 4 == 0) else 0.66  # acento no 1º tempo do compasso
            s = int(tb * sr)
            m = max(0, min(plen, n_total - s))
            if m > 0:
                out[s : s + m] += (
                    np.sin(2 * np.pi * root * tt) * penv * (0.42 * energia * accent)
                )[:m]

    # cadeia premium (espaço/calor/ar) — mão leve p/ não embolar sob a voz
    try:
        import dsp

        out = dsp.master(
            out, lowcut_fc=40, sat=1.3, air_db=2.0, rev=0.08, decay=1.0, dark=0.7, seed=31, peak=1.0
        )[:n_total]
    except Exception as _e:
        print(f"  [aviso] DSP da trilha pulado: {_e}")
    # normaliza + fade global
    out /= np.max(np.abs(out)) + 1e-9
    fi, fo = int(4 * sr), int(7 * sr)
    out[:fi] *= np.linspace(0, 1, fi)
    out[-fo:] *= np.linspace(1, 0, fo)
    out = (out * 0.9 * 32767).astype(np.int16)

    with wave.open(str(out_wav), 'w') as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(sr)
        w.writeframes(out.tobytes())


def _to_ssml(text):
    """Direção de prosódia PREMIUM (jun/2026): cadência VARIADA, não metronômica.
    O salto amador→premium é a MICRO-PAUSA DE VÍRGULA — sem ela a lista/oração 'corre'
    e soa robótica; com ela a frase respira e ganha fraseado humano. As pausas são
    diferenciadas por pontuação (cada sinal tem seu peso) e as reticências criam
    suspense. Chirp3-HD/Studio/Neural2 aceitam <break> via SSML.
    NB de orçamento: pausas custam tempo — manter narração ≤ ~52 palavras/cena para
    caber nos 30s/cena do QC (premium pede frase enxuta, não densa)."""
    import html as _html

    t = _html.escape(text, quote=False)  # & < > seguros no XML
    t = t.replace('... ', '…<break time="500ms"/> ')  # reticências → suspense
    t = t.replace('… ', '…<break time="500ms"/> ')
    t = t.replace('? ', '?<break time="560ms"/> ')  # pergunta pousa e respira
    t = t.replace('! ', '!<break time="440ms"/> ')
    t = t.replace('. ', '.<break time="400ms"/> ')  # ponto final: settle pleno
    t = t.replace('; ', ';<break time="300ms"/> ')  # ponto-e-vírgula
    t = t.replace(' — ', ' —<break time="330ms"/> ')  # travessão: pausa dramática
    t = t.replace(
        ', ', ',<break time="150ms"/> '
    )  # VÍRGULA: micro-pausa de fraseado (o salto premium)
    return f'<speak>{t}</speak>'


def tts(text, voice, out_mp3, rate=1.0):
    # Vozes Cloud TTS (Chirp3-HD / Studio / Neural2) → Google; senão edge-tts.
    # ROTA DE FUGA (jun/2026): se o Google cair (sem crédito/cota/503), tenta 2x e então
    # usa a voz GRÁTIS local (edge-tts) — a produção nunca para por falta de crédito externo.
    FUGA_VOZ = 'pt-BR-AntonioNeural'  # voz de fuga: masculina, sóbria (mais próxima do Iapetus)
    if any(t in voice for t in ('Chirp3', 'Studio', 'Neural2', 'Wavenet')):
        import time as _time

        for _tentativa in range(2):
            try:
                import tts_gcloud

                if tts_gcloud.synth(text, voice, str(out_mp3), rate=rate, ssml=_to_ssml(text)):
                    return
            except Exception as _e:
                print(f'  [aviso] Cloud TTS tentativa {_tentativa + 1}/2: {str(_e)[:100]}')
            _time.sleep(2)
        print(f'  [ROTA DE FUGA] Cloud TTS indisponível → voz grátis local edge-tts ({FUGA_VOZ})')
        voice = FUGA_VOZ
    subprocess.run(
        [
            sys.executable,
            '-m',
            'edge_tts',
            '--voice',
            voice,
            '--text',
            text,
            '--write-media',
            str(out_mp3),
        ],
        check=True,
        capture_output=True,
    )


def make_clip(png, mp3, dur, out_mp4, ken_burns=False, kb=0):
    fo = max(0.1, dur - FADE)
    if ken_burns:
        nf = max(2, int(dur * 30))
        cx, cy = "iw/2-(iw/zoom/2)", "ih/2-(ih/zoom/2)"
        zin = "min(zoom+0.0006,1.12)"
        moves = [  # variação por cena
            f"z='{zin}':x='{cx}':y='{cy}'",  # zoom centro
            f"z='{zin}':x='(iw-iw/zoom)*(on/{nf})':y='{cy}'",  # zoom + pan →
            f"z='{zin}':x='(iw-iw/zoom)*(1-on/{nf})':y='{cy}'",  # zoom + pan ←
            f"z='{zin}':x='{cx}':y='(ih-ih/zoom)*(1-on/{nf})'",  # zoom + pan ↑
        ]
        vf = (
            f"scale=2304:1296,zoompan={moves[kb % 4]}:d={nf}:s=1920x1080:fps=30,"
            f"fade=t=in:st=0:d={FADE},fade=t=out:st={fo:.3f}:d={FADE}"
        )
        subprocess.run(
            [
                FFMPEG,
                '-y',
                '-loop',
                '1',
                '-i',
                str(png),
                '-i',
                str(mp3),
                '-t',
                f'{dur:.3f}',
                '-vf',
                vf,
                '-c:v',
                'libx264',
                '-pix_fmt',
                'yuv420p',
                '-c:a',
                'aac',
                '-b:a',
                '192k',
                '-af',
                f'apad=pad_dur={TAIL}',
                '-shortest',
                str(out_mp4),
            ],
            check=True,
            capture_output=True,
        )
    else:
        subprocess.run(
            [
                FFMPEG,
                '-y',
                '-loop',
                '1',
                '-i',
                str(png),
                '-i',
                str(mp3),
                '-t',
                f'{dur:.3f}',
                '-r',
                '30',
                '-vf',
                f'fade=t=in:st=0:d={FADE},fade=t=out:st={fo:.3f}:d={FADE}',
                '-c:v',
                'libx264',
                '-tune',
                'stillimage',
                '-pix_fmt',
                'yuv420p',
                '-c:a',
                'aac',
                '-b:a',
                '192k',
                '-af',
                f'apad=pad_dur={TAIL}',
                '-shortest',
                str(out_mp4),
            ],
            check=True,
            capture_output=True,
        )


def _clip_dur(path):
    import re

    r = subprocess.run([FFMPEG, '-i', str(path)], capture_output=True, text=True)
    m = re.search(r'Duration: (\d+):(\d+):([\d.]+)', r.stderr)
    return int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3)) if m else 8.0


def make_motion_clip(veo_mp4, overlay_png, mp3, dur, out_mp4, src_dur=None):
    """Clipe com fundo em movimento real (Veo/Kling): palíndromo (vai-e-volta sem
    corte) desacelerado p/ cobrir a narração + overlay de texto + fades."""
    if src_dur is None:
        src_dur = _clip_dur(veo_mp4)  # auto: Kling ~5s, Veo ~8s
    fo = max(0.1, dur - FADE)
    f = max(0.5, dur / (2 * src_dur))  # fator p/ o palíndromo (2x src) cobrir dur
    subprocess.run(
        [
            FFMPEG,
            '-y',
            '-i',
            str(veo_mp4),
            '-loop',
            '1',
            '-i',
            str(overlay_png),
            '-i',
            str(mp3),
            '-filter_complex',
            f"[0:v]split[a][b];[b]reverse[r];[a][r]concat=n=2:v=1,"
            f"setpts={f:.4f}*PTS,scale=1920:1080:flags=lanczos,fps=30[bg];"
            f"[bg][1:v]overlay=0:0:eof_action=repeat,"
            f"fade=t=in:st=0:d={FADE},fade=t=out:st={fo:.3f}:d={FADE}[v];"
            f"[2:a]apad=pad_dur={TAIL}[a]",
            '-map',
            '[v]',
            '-map',
            '[a]',
            '-t',
            f'{dur:.3f}',
            '-c:v',
            'libx264',
            '-pix_fmt',
            'yuv420p',
            '-c:a',
            'aac',
            '-b:a',
            '192k',
            str(out_mp4),
        ],
        check=True,
        capture_output=True,
    )


def main(roteiro_path):
    cfg = json.loads(Path(roteiro_path).read_text(encoding='utf-8'))
    try:
        from contracts import load_roteiro

        _cfg_validated = load_roteiro(roteiro_path)
    except ImportError:
        pass  # contracts.py opcional
    except Exception as e:
        print(f'  [contracts] aviso: {e}')
    slug = cfg['slug']
    import os as _os

    _os.environ['PIPELINE_SLUG'] = slug
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
        usa_img = usa_mot = False  # slides escuros + Ken Burns, sem geração paga (R$0)
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

    clips = []
    durs = []  # duração on-screen de cada cena (p/ legendas/capítulos da lane YouTube)
    label = {'fal': 'Flux + Kling', 'google': 'Imagen + Veo'}.get(provider, provider)
    print(
        f"Gerando '{cfg['titulo']}' — {n} cenas"
        + (f" · imagens IA + movimento ({label})" if usa_img else "")
    )
    for i, cena in enumerate(cenas):
        mp3 = WORK / f'a{i:02d}.mp3'
        png = WORK / f's{i:02d}.png'
        clip = WORK / f'c{i:02d}.mp4'

        bg = None
        if cena.get('img') and img_gen:  # base/none: img_gen=None → slide escuro
            bg = IMGDIR / f'{slug}_{i:02d}.png'
            if not bg.exists():  # cache: não regenera (e não recobra) imagem já feita
                full = f"{cena['img']}, {estilo}" if estilo else cena['img']
                if not img_gen(full, str(bg), aspect='16:9'):
                    raise RuntimeError(f'Geração de imagem falhou na cena {i + 1}')
                print(f"  imagem {i + 1}/{n} gerada")

        mot = None
        if cena.get('motion') and bg and mot_gen:
            mot = MOTDIR / f'{slug}_{i:02d}.mp4'
            if not mot.exists():  # cache: clipe de movimento é pago — nunca regenera
                print(f"  animando cena {i + 1}/{n}...")
                try:
                    if not mot_gen(str(bg), cena['motion'], str(mot)):
                        print(f"  [!] movimento falhou na cena {i + 1} — usando Ken Burns")
                        mot = None
                except Exception as _me:
                    print(
                        f"  [!] movimento falhou ({type(_me).__name__}: {str(_me)[:80]}) — usando Ken Burns"
                    )
                    mot = None

        tipo = cena.get('tipo', 'conceito')
        side = (
            'center'
            if tipo in ('abertura', 'encerramento')
            else ('left' if i % 2 == 1 else 'right')
        )

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
        print(
            f"  cena {i + 1}/{n}: {dur:.1f}s  · {cena['titulo'][:40]}"
            + ("  [movimento]" if mot else "")
        )

    # concat (vídeo + narração)
    listf = WORK / 'list.txt'
    listf.write_text(''.join(f"file '{c.as_posix()}'\n" for c in clips), encoding='utf-8')
    narr = WORK / '_narr.mp4'
    subprocess.run(
        [
            FFMPEG,
            '-y',
            '-f',
            'concat',
            '-safe',
            '0',
            '-i',
            str(listf),
            '-c:v',
            'libx264',
            '-pix_fmt',
            'yuv420p',
            '-c:a',
            'aac',
            '-b:a',
            '192k',
            str(narr),
        ],
        check=True,
        capture_output=True,
    )

    # Pós-produção desacoplada: sintetiza a trilha, persiste os stems (D·M·E) e
    # roda o Mix & Master a partir deles — re-executável via `mixmaster.py <slug>`.
    import mixmaster

    mus = None
    if cfg.get('musica'):
        dur_total = sum(MP3(WORK / f'a{i:02d}.mp3').info.length + TAIL for i in range(n))
        mus = WORK / '_music.wav'
        energia = float(
            cfg.get('musica_energia', 0.65)
        )  # ritmo/energia da trilha (0=contemplativo … 1=enérgico)
        sintetiza_ambiente(dur_total + 2, mus, energia=energia)
        print(f"  trilha ambiente sintetizada: {dur_total:.0f}s (energia={energia})")
    mixmaster.export_stems(slug, narr, mus)  # _stems/<slug>/ (D·M·E + vídeo mudo)
    (
        ROOT / '_stems' / slug / 'timing.json'
    ).write_text(  # timing p/ legendas/capítulos (lane YouTube)
        json.dumps({'tail': TAIL, 'durs': durs}, ensure_ascii=False), encoding='utf-8'
    )
    try:  # Sonoplasta: batidas de transição em arco de comoção (Fibonacci)
        import efeitos_transicao

        efeitos_transicao.main(
            str(roteiro_path)
        )  # escreve _stems/<slug>/efeitos.wav (antes do master)
    except (Exception, SystemExit) as e:  # nunca aborta o build por causa da camada de batidas
        print(f"  [aviso] camada de batidas pulada: {e}")
    out = mixmaster.master(
        slug, ROOT / f'{slug}.mp4'
    )  # Mix & Master a partir dos stems (já com efeitos.wav)
    print(f"\nOK -> {out}  ·  stems em _stems/{slug}/  ·  re-mix: python mixmaster.py {slug}")


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else ROOT / 'roteiros' / 'arte-da-guerra.json')
