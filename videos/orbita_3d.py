# -*- coding: utf-8 -*-
"""Cinegrafista — render de ÓRBITA 3D (DepthFlow, shader OpenGL na GPU local).

Movimento orbital circular forte a partir de UMA imagem: a câmera descreve um
círculo (offset cos/sin) com projeção isométrica → sensação 3D de "girar em volta"
da cena (o mais perto de um 360 que uma imagem única permite — não há o verso).

Uso:  python orbita_3d.py <imagem> <saida.mp4> [dur] [raio] [iso] [zoom]
"""
import math
import sys

from attrs import define
from depthflow.scene import DepthScene


@define
class Orbita(DepthScene):
    raio: float = 0.55      # amplitude da órbita (deslocamento lateral da câmera)
    iso: float = 0.55       # projeção isométrica (tilt 3D)
    zoomf: float = 0.68     # <1 = zoom-IN (corta as bordas reveladas pelo movimento)
    altura: float = 0.62    # height = separação de camadas (FORÇA do parallax/profundidade)
    firme: float = 0.12     # steady (âncora); baixo = mais movimento aparente

    def update(self) -> None:
        self.state.isometric = self.iso
        self.state.steady = self.firme
        self.state.height = self.altura          # parallax forte: fg/bg separam
        self.state.zoom = self.zoomf
        self.state.offset = (
            self.raio * math.cos(self.cycle),    # círculo completo no loop → órbita
            self.raio * math.sin(self.cycle),
        )


def render(img, out, dur=6.0, raio=0.55, iso=0.55, zoomf=0.68, altura=0.62, fps=30):
    scene = Orbita(backend="headless", raio=raio, iso=iso, zoomf=zoomf, altura=altura)
    scene.ffmpeg.h264(preset="veryfast")
    scene.input(image=img)
    scene.main(output=out, time=dur, fps=fps, ssaa=2.0)
    return out


if __name__ == "__main__":
    a = sys.argv
    render(a[1], a[2],
           dur=float(a[3]) if len(a) > 3 else 6.0,
           raio=float(a[4]) if len(a) > 4 else 0.55,
           iso=float(a[5]) if len(a) > 5 else 0.55,
           zoomf=float(a[6]) if len(a) > 6 else 0.68,
           altura=float(a[7]) if len(a) > 7 else 0.62)
    print("OK", a[2])
