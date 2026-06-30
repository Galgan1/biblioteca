# -*- coding: utf-8 -*-
"""Corta um Short vertical 9:16 (1080x1920) de UMA cena já renderizada.
Reaproveita o fundo limpo (_img/<slug>_NN.png) + a narração (_work/aNN.mp3).
Custo R$0 — só ffmpeg + Pillow, sem nenhuma API externa.

Uso:  python gerar_short.py <slug> <idx_cena>   (ex.: python gerar_short.py maquiavel-pedagogo 2)
Saída: _shorts/<slug>_NN.mp4  (1080x1920, ~20-45s)
"""
import sys, json, subprocess
from pathlib import Path
from PIL import Image, ImageDraw
import imageio_ffmpeg
from mutagen.mp3 import MP3
import gerar_video as gv
import _short_audio as sa

FF = imageio_ffmpeg.get_ffmpeg_exe()
ROOT = Path(__file__).parent
W, H = 1080, 1920
HANDLE = '@MinutoReal'


def _audio_filter(cover_s, lead_s):
    """Áudio do Short: voz (atrasada p/ após a capa+respiro) + leito de engajamento [4].
    amix normalize=0 mantém a voz CHEIA e o leito por baixo (VOZ SOBERANA); o alimiter
    trava o pico onde o acento de síncrese encontra a entrada da voz. O leito cobre 0→fim."""
    ms = int((cover_s + lead_s) * 1000)
    return (f"[2:a]adelay={ms}:all=1[vx];"
            f"[4:a][vx]amix=inputs=2:duration=first:normalize=0,alimiter=limit=0.97[a]")


def _reveal_offsets(cena, voice_start, voice_dur):
    """Offsets absolutos (s) dos ticks de revelação a partir do campo `reveal` da cena:
    True = meio da narração; número = segundos dentro dela; string = substring (estimativa
    por caractere). Synch point de CONTEÚDO (Chion) — pico sonoro no pico de informação.
    Ausente/False/não-encontrado = [] (backward-compatible)."""
    rev = cena.get('reveal')
    narr = cena.get('narracao', '') or ''
    if rev is None or rev is False:
        return []
    if rev is True:
        off = voice_dur / 2.0
    elif isinstance(rev, (int, float)):
        off = float(rev)
    elif isinstance(rev, str) and narr and rev in narr:
        off = narr.index(rev) / len(narr) * voice_dur
    else:
        return []
    return [voice_start + max(0.0, min(off, voice_dur))]


def cover(src):
    im = Image.open(src).convert('RGB')
    s = max(W / im.width, H / im.height)
    im = im.resize((max(W, int(im.width * s)), max(H, int(im.height * s))), Image.LANCZOS)
    x, y = (im.width - W) // 2, (im.height - H) // 2
    return im.crop((x, y, x + W, y + H))


def dark_bg(accent):
    """Fundo vertical escuro com aura suave — para Shorts de vídeos nível BASE (sem _img)."""
    ac = gv.hex_rgb(accent)
    img = Image.new('RGB', (W, H), gv.marca.rgb('papel'))
    ov = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(ov)
    cx, cy = W // 2, int(H * 0.40)
    for i in range(54, 0, -1):
        rr = int(820 * i / 54)
        a = int(34 * (1 - i / 54) ** 1.8)
        od.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], fill=ac + (a,))
    img.paste(Image.alpha_composite(img.convert('RGBA'), ov).convert('RGB'))
    return img


def make_overlay(cena, accent, hook, out_png):
    img = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    ac = gv.hex_rgb(accent)
    scrim = gv.marca.rgb('papel')   # fundo da marca p/ os degradês de escurecimento
    # escurecimento topo (gancho) e base (título + CTA)
    for py in range(0, 640, 2):
        a = int(205 * (1 - py / 640) ** 1.2)
        d.rectangle([(0, py), (W, py + 2)], fill=scrim + (a,))
    for py in range(H - 780, H, 2):
        a = int(225 * ((py - (H - 780)) / 780) ** 1.05)
        d.rectangle([(0, py), (W, py + 2)], fill=scrim + (a,))
    # GANCHO (topo)
    fh = gv.F_UI_B(56)
    yy = 150
    for ln in gv.wrap(d, hook.upper(), fh, W - 150):
        gv.tracked(d, (70, yy), ln, fh, ac, 2)
        yy += int(fh.size * 1.18)
    d.rectangle([(70, yy + 14), (70 + 96, yy + 22)], fill=ac)
    # TÍTULO grande (base)
    ft = gv.F_TITLE(94)
    lines = gv.wrap(d, cena['titulo'], ft, W - 140)
    ty = H - 470 - len(lines) * int(ft.size * 1.08)
    for ln in lines:
        d.text((70, ty), ln, font=ft, fill=gv.marca.rgb('tinta'))
        ty += int(ft.size * 1.08)
    # rodapé: marca + CTA (triângulo desenhado, sem depender de glifo da fonte)
    d.text((70, H - 168), HANDLE, font=gv.F_UI_B(44), fill=ac)
    cta = 'vídeo completo no canal'
    d.text((70, H - 108), cta, font=gv.F_UI(36), fill=gv.marca.rgb('tinta-fraca'))
    tx = 70 + d.textlength(cta, font=gv.F_UI(36)) + 22
    d.polygon([(tx, H - 100), (tx, H - 76), (tx + 20, H - 88)], fill=ac)
    img.save(out_png)


def make_cover(cena, accent, cfg, out_png, bg_src=None):
    """Frame de CAPA de marca p/ a VITRINE do Instagram (grid de Reels).
    Aberto no início do Reel e segurado ≥2s p/ o thumb_offset@1500ms SEMPRE cair
    nele (nunca no fade-in preto). Billboard-proof: legível no tamanho de unha.
    Fundo escuro da marca (papel) com a imagem do short escurecida ao estilo
    billboard, wordmark "MINUTO REAL" + fio de ouro, KICKER (topo) e TÍTULO
    (centro/baixo) em Hanken Black."""
    ac = gv.hex_rgb(accent)
    ouro = gv.marca.rgb('ouro')
    papel = gv.marca.rgb('papel')
    img = Image.new('RGB', (W, H), papel)
    # fundo billboard: a imagem do short bem escurecida (some graciosamente se não houver)
    if bg_src and Path(bg_src).exists():
        bg = cover(bg_src).convert('RGBA')
        veil = Image.new('RGBA', (W, H), papel + (215,))
        bg = Image.alpha_composite(bg, veil)
        img.paste(bg.convert('RGB'))
    d = ImageDraw.Draw(img)
    # WORDMARK (topo): "MINUTO REAL" tracked + fio de ouro
    # safe-zone 9:16: o bloco do topo começa em >=260 (IG cobre ~250px no player)
    fwm = gv.F_BLACK(48)
    gv.tracked(d, (70, 260), 'MINUTO REAL', fwm, gv.marca.rgb('tinta'), 6)
    d.rectangle([(70, 332), (70 + 150, 340)], fill=ouro)   # fio de ouro (acento, parcimônia)
    # KICKER (logo abaixo do wordmark)
    kicker = (cena.get('kicker', '') or '').strip()
    if kicker:
        fk = gv.F_UI_B(40)
        yy = 394
        for ln in gv.wrap(d, kicker.upper(), fk, W - 150):
            gv.tracked(d, (70, yy), ln, fk, ac, 2)
            yy += int(fk.size * 1.2)
    # TÍTULO grande (centro/baixo) em Hanken Black — o billboard
    titulo = cena.get('titulo') or cfg['titulo']
    ft = gv.F_BLACK(132)
    lines = gv.wrap(d, titulo, ft, W - 140)
    th = len(lines) * int(ft.size * 1.04)
    ty = int(H * 0.60) - th // 2
    for ln in lines:
        d.text((70, ty), ln, font=ft, fill=gv.marca.rgb('tinta'))
        ty += int(ft.size * 1.04)
    # rodapé: o livro + handle, ancorando a marca
    # safe-zone 9:16: o rodapé termina antes de ~y=1670 (IG cobre ~250px embaixo)
    # se o título central já É o do livro, o rótulo vira o AUTOR (info nova, sem repetir)
    rotulo = cfg['titulo']
    if titulo.upper() == cfg['titulo'].upper():
        rotulo = cfg.get('autor', '')
    if rotulo:
        d.text((70, H - 380), rotulo.upper(), font=gv.F_UI_B(40),
               fill=gv.marca.rgb('tinta-fraca'))
    d.text((70, H - 310), HANDLE, font=gv.F_UI_B(44), fill=ac)
    img.save(out_png)


def main(slug, idx, intro='gongo', out_name=None):
    cfg = json.loads((ROOT / 'roteiros' / f'{slug}.json').read_text(encoding='utf-8'))
    cena = cfg['cenas'][idx]
    accent = cfg.get('acento', gv.marca.hex_of('ouro'))
    SH = ROOT / '_shorts'
    SH.mkdir(exist_ok=True)

    bg_src = ROOT / '_img' / f'{slug}_{idx:02d}.png'   # existe só em vídeo cinema

    # re-sintetiza a narração com a MESMA voz do longo — incl. voz POR CENA (slogans em
    # voz feminina, p.ex.), p/ o short bater com o longo. Usa o mesmo gate que o gerar_video.
    voz, rate = gv._voz_cena(cena, cfg.get('voz', 'pt-BR-Chirp3-HD-Iapetus'), cfg.get('tts_rate', 1.0))
    mp3 = SH / f'{slug}_{idx:02d}_aud.mp3'
    if not mp3.exists():
        gv.tts(cena['narracao'], voz, mp3, rate=rate)

    COVER = 2.4    # capa de marca segurada na ABERTURA p/ a vitrine do IG (thumb_offset@1500ms cai aqui)
    LEAD = 0.45   # respiro de entrada: a 1ª palavra só entra DEPOIS do fade-in da cena
    voz_len = MP3(mp3).info.length
    dur = LEAD + voz_len + 0.6
    nf = max(2, int(dur * 30))
    fo = max(0.1, dur - 0.4)

    bg_png = SH / f'{slug}_{idx:02d}_bg.png'
    (cover(bg_src) if bg_src.exists() else dark_bg(accent)).save(bg_png)
    ov_png = SH / f'{slug}_{idx:02d}_ov.png'
    hook = (cena.get('kicker', '').split('·')[-1].strip()) or cfg['titulo']
    make_overlay(cena, accent, hook, ov_png)
    cv_png = SH / f'{slug}_{idx:02d}_cover.png'
    make_cover(cena, accent, cfg, cv_png, bg_src)

    # leito de engajamento (sonoplastia do Short): hook na capa + acento de síncrese
    # no corte + tensão sub-grave sob a voz (vetoriza). Forward-looking, soberano.
    bed_wav = SH / f'{slug}_{idx:02d}_bed.wav'
    sa.short_bed(COVER + dur, COVER, LEAD, bed_wav, seed=idx + 7,
                 energia=cfg.get('musica_energia', 0.6),
                 reveals=_reveal_offsets(cena, COVER + LEAD, voz_len), intro=intro)

    out = SH / (f'{out_name}.mp4' if out_name else f'{slug}_{idx:02d}.mp4')
    # [3] = frame de capa de marca, segurado COVER s na abertura (vitrine do IG),
    # depois concatena a cena animada. O áudio = voz (após a capa+respiro) + leito [4].
    vf = (f"[0:v]scale=1188:2112,zoompan=z='min(zoom+0.0008,1.12)':d={nf}:"
          f"x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920:fps=30[z];"
          f"[z][1:v]overlay=0:0,fade=t=in:st=0:d=0.4,fade=t=out:st={fo:.2f}:d=0.4[scene];"
          f"[3:v]scale=1080:1920,fps=30,trim=duration={COVER:.2f},setpts=PTS-STARTPTS,"
          f"fade=t=out:st={COVER-0.3:.2f}:d=0.3[cov];"
          f"[cov][scene]concat=n=2:v=1:a=0[v];"
          f"{_audio_filter(COVER, LEAD)}")
    subprocess.run([FF, '-y', '-loop', '1', '-i', str(bg_png), '-loop', '1', '-i', str(ov_png),
                    '-i', str(mp3), '-loop', '1', '-i', str(cv_png), '-i', str(bed_wav),
                    '-filter_complex', vf,
                    '-map', '[v]', '-map', '[a]', '-t', f'{COVER + dur:.2f}',
                    '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k', '-ar', '44100',
                    '-shortest', str(out)], check=True, capture_output=True)
    print(f'OK -> {out}  ({COVER + dur:.1f}s, 1080x1920, capa {COVER:.1f}s + leito de engajamento)')


if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]))
