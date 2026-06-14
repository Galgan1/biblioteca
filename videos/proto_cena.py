# -*- coding: utf-8 -*-
"""Protótipo de UMA cena premium: imagem IA de fundo + overlay + texto + Ken Burns
+ narração Iapetus + trilha. Para validar o visual antes de aplicar a tudo."""

import subprocess
from pathlib import Path
from PIL import Image, ImageDraw
import imageio_ffmpeg, tts_gcloud, gerar_video as gv
from mutagen.mp3 import MP3

FF = imageio_ffmpeg.get_ffmpeg_exe()
W, H = 1920, 1080
P = Path('_proto')

KICKER = '01 · A Estratégia Suprema'
TITLE = 'Vencer sem lutar'
ACCENT = gv.hex_rgb('#d8a64a')
BOOK = 'A ARTE DA GUERRA  ·  SUN TZU'
NAR = (
    'Para Sun Tzu, ganhar cem batalhas em cem combates não é o auge da excelência. '
    'A maior vitória é subjugar o inimigo sem lutar.'
)

# ── compor slide: imagem cobrindo 1920x1080 + escurecimento à esquerda ──
bg = Image.open(P / 'teste.png').convert('RGB')
s = max(W / bg.width, H / bg.height)
bg = bg.resize((int(bg.width * s), int(bg.height * s)), Image.LANCZOS)
x, y = (bg.width - W) // 2, (bg.height - H) // 2
img = bg.crop((x, y, x + W, y + H)).convert('RGBA')

ov = Image.new('RGBA', (W, H), (0, 0, 0, 0))
od = ImageDraw.Draw(ov)
for px in range(0, W, 2):  # gradiente: esquerda escura (texto) → direita revela imagem
    a = int(215 * (1 - px / W) ** 1.25) + 55
    od.rectangle([(px, 0), (px + 2, H)], fill=(5, 5, 8, min(235, a)))
img.alpha_composite(ov)

d = ImageDraw.Draw(img)
ax = 170
d.rectangle([(ax, 300), (ax + 56, 305)], fill=ACCENT)
gv.tracked(d, (ax, 336), KICKER.upper(), gv.F_UI_B(32), ACCENT, 4)
ft = gv.F_TITLE(108)
yy = 440
for ln in gv.wrap(d, TITLE, ft, W - 2 * ax):
    d.text((ax, yy), ln, font=ft, fill=(245, 245, 248))
    yy += int(ft.size * 1.12)
d.text((ax, H - 96), BOOK, font=gv.F_UI(28), fill=(205, 205, 215))
bx0, bx1, by = ax, W - ax, H - 60
d.rectangle([(bx0, by), (bx1, by + 3)], fill=(60, 60, 70))
d.rectangle([(bx0, by), (bx0 + int((bx1 - bx0) * 2 / 13), by + 3)], fill=ACCENT)
img.convert('RGB').save(P / 'slide.png', quality=95)
print('slide composto')

# ── narração + trilha ──
tts_gcloud.synth(NAR, 'pt-BR-Chirp3-HD-Iapetus', str(P / 'aud.mp3'), rate=0.96)
dur = MP3(P / 'aud.mp3').info.length + 0.8
gv.sintetiza_ambiente(dur + 1, P / 'mus.wav')

# ── Ken Burns + mix ──
nf = int(dur * 30)
fo = dur - 0.5
subprocess.run(
    [
        FF,
        '-y',
        '-loop',
        '1',
        '-i',
        str(P / 'slide.png'),
        '-i',
        str(P / 'aud.mp3'),
        '-i',
        str(P / 'mus.wav'),
        '-filter_complex',
        f"[0:v]scale=2304:1296,zoompan=z='min(zoom+0.0006,1.10)':d={nf}:"
        f"x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps=30,"
        f"fade=t=in:st=0:d=0.5,fade=t=out:st={fo:.2f}:d=0.5[v];"
        f"[2:a]volume=0.11[m];[1:a][m]amix=inputs=2:duration=first[a]",
        '-map',
        '[v]',
        '-map',
        '[a]',
        '-t',
        f'{dur:.2f}',
        '-c:v',
        'libx264',
        '-pix_fmt',
        'yuv420p',
        '-c:a',
        'aac',
        '-b:a',
        '192k',
        str(P / 'proto.mp4'),
    ],
    check=True,
    capture_output=True,
)
print(f'OK -> _proto/proto.mp4 ({dur:.1f}s)')
