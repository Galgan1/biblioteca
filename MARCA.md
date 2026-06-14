# Marca — Minuto Real / Biblioteca

Brand book canônico da rede. **Fonte única de verdade técnica: [`marca.py`](marca.py).**
Toda peça (site, YouTube, Instagram, TikTok) lê os tokens daqui — nunca hardcoda cor ou fonte.
Guardrail: rode `python check_marca.py` (falha se algum gerador divergir).

## Decisão de marca (14/jun/2026)

- **Verde lidera** (cor-mãe, hue 152) — a identidade da Biblioteca.
- **UM ouro** é o único acento premium (hue 83, âmbar `#d8a64a`, com equity no YouTube). Usar **com parcimônia** (CTA, destaque, número-herói) — nunca como cor dominante.
- **Tipografia única**: **Hanken Grotesk** (display/UI/títulos-bomba) + **Literata** (serif editorial, títulos de vídeo e citações).
- **Um só alerta** (hue 30) — consolidou o vermelho-25 do site e o laranja-38 do IG.

## Paleta (OKLCH — claro / escuro)

| Token | Claro | Escuro | Hex (Pillow, canvas escuro) | Uso |
|---|---|---|---|---|
| `verde` | `52% 0.14 152` | `70% 0.13 152` | `#3faf76` | pílulas, bordas, ícones, realce |
| `verde-deep` | `40% 0.12 152` | `77% 0.11 152` | `#5cc28a` | títulos vivos |
| `verde-soft` | `86% 0.06 152` | `85% 0.10 152` | `#a9e6c4` | realce de texto sobre escuro |
| `ouro` | `60% 0.10 83` | `76% 0.105 83` | `#d8a64a` | **acento premium único** (parcimônia) |
| `ouro-soft` | `72% 0.09 83` | `86% 0.075 83` | `#ecca8c` | filete, kicker |
| `alerta` | `55% 0.17 30` | `72% 0.16 30` | `#e8744f` | perigo/atenção (um só hue) |
| `tinta` | `22% 0.01 152` | `95% 0.01 152` | `#f2f2f5` | texto |
| `papel` | `99% 0.002 152` | `16% 0.01 152` | `#08080c` | fundo |

## Tipografia

- **Display/UI/wordmark** — Hanken Grotesk (pesos 400 · 500 · 700 · 800 · **900/Black** p/ thumbnail).
- **Serif/editorial** — Literata (500 · 600), títulos de vídeo e citações.
- Fontes empacotadas em [`_fonts/`](_fonts) (OFL, variáveis). Pillow lê os pesos via `marca.font(role, size, peso)`.

## Regras de uso (lentes Norman + Krug — ver [doutrina](MARCA.md))

- **Ouro com parcimônia**: é tempero, não base. Verde é a estrutura.
- **Nunca informe só por cor** (acessibilidade): verde/ouro/alerta sempre acompanhados de ícone, forma ou rótulo (ex.: card `.warn` = cor + ícone de relógio + palavra).
- **Billboard**: thumbnail e capa de carrossel são lidos num relance — Hanken Black, contraste alto, foco único.
- **Omitir palavras**: corte metade, depois metade (≤52 palavras/cena no vídeo).

## Como consumir

```python
import marca
marca.css_root('dark')          # bloco :root{} p/ CSS (site claro/escuro, carrossel)
marca.rgb('ouro')               # (216,166,74) p/ Pillow
marca.font('display', 120, 'Black')   # Hanken Black p/ thumbnail
```

CSS (site/carrossel): tokens-chave (`--green`/`--gold`/`--warn`) batem com `marca.py`.
Pillow (vídeo/thumb/canal): `videos/gerar_video.py` importa `marca` e os demais herdam via `gv`.

## Saúde do sistema

`python check_marca.py` → checa drift (nenhum gerador pode hardcodar `#d8a64a`, Arial Black, ouro h92, alerta h38, verde L73) **e** reporta contraste WCAG dos pares-chave.
