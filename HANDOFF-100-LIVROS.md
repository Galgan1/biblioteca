# Handoff — Rumo aos 100 livros (27 novos)

**De:** lane Conversor Livro→Skill (Minuto Real)
**Para:** **Bibliotecário** (site/publicação) + **Diretor de Design** (consistência de marca)
**Data:** 2026-06-14

## Estado
- `books.json` hoje: **73** livros.
- Estes **27 livros novos** já têm **skill + `<slug>_data.py` + capa original (`assets/<slug>-cover.png`)** prontos e verificados (skill com links resolvendo, data.py com `ast.parse` OK, capa >4KB).
- **Falta só publicar** (gerar página + registrar no `books.json` + deploy). `73 + 27 = 100`. 🎯

## Bibliotecário — publicar + deploy (SÉRIE, não paralelo — evita corrida no `books.json`)
```bash
cd C:\Users\User\.gemini\antigravity\scratch\biblioteca
for s in 7-habitos poder-do-habito trabalho-focado a-unica-coisa comece-pelo-porque \
         de-zero-a-um startup-enxuta trabalhe-4-horas inteligencia-emocional mindset \
         garra flow corpo-guarda-as-marcas busca-de-sentido sapiens homo-deus gene-egoista \
         cisne-negro antifragil meditacoes axiomas-de-zurique milionario-mora-ao-lado \
         revolucao-dos-bichos pequeno-principe metamorfose o-alquimista dom-casmurro; do
  python publicar_livro.py "$s" --deploy
done
```
(ou rode `--check` antes de `--deploy` para validar cada um.)

## Diretor de Design — QC de marca nas 27 páginas novas
- Conferir tokens (verde h152, traço tracejado, ícones de linha) e a pílula `card-title` sem quebra feia.
- `theme-color` correto por skin; capa 2:3 sem distorção; grid `columns:2`.
- Rodar a varredura/`run-biblioteca` smoke nas novas + checar mobile/tablet.

## Os 27 (slug · arquivo de dados · nº de capítulos da skill)
| Slug | data.py | caps |
|---|---|---|
| 7-habitos | 7_habitos_data.py | 9 |
| poder-do-habito | poder_do_habito_data.py | 9 |
| trabalho-focado | trabalho_focado_data.py | 7 |
| a-unica-coisa | a_unica_coisa_data.py | 6 |
| comece-pelo-porque | comece_pelo_porque_data.py | 14 |
| de-zero-a-um | de_zero_a_um_data.py | 14 |
| startup-enxuta | startup_enxuta_data.py | 14 |
| trabalhe-4-horas | trabalhe_4_horas_data.py | 7 |
| inteligencia-emocional | inteligencia_emocional_data.py | 8 |
| mindset | mindset_data.py | 8 |
| garra | garra_data.py | 7 |
| flow | flow_data.py | 10 |
| corpo-guarda-as-marcas | corpo_guarda_as_marcas_data.py | 12 |
| busca-de-sentido | busca_de_sentido_data.py | 7 |
| sapiens | sapiens_data.py | 13 |
| homo-deus | homo_deus_data.py | 9 |
| gene-egoista | gene_egoista_data.py | 13 |
| cisne-negro | cisne_negro_data.py | 8 |
| antifragil | antifragil_data.py | 7 |
| meditacoes | meditacoes_data.py | 8 |
| axiomas-de-zurique | axiomas_de_zurique_data.py | 6 |
| milionario-mora-ao-lado | milionario_mora_ao_lado_data.py | 8 |
| revolucao-dos-bichos | revolucao_dos_bichos_data.py | 9 |
| pequeno-principe | pequeno_principe_data.py | 7 |
| metamorfose | metamorfose_data.py | 3 |
| o-alquimista | o_alquimista_data.py | 9 |
| dom-casmurro | dom_casmurro_data.py | 8 |

> Afiliados: depois do publicar, rodar `python afiliados/gerar_links.py` + `python afiliados/inserir_botao.py` para os 27 entrarem no botão de compra discreto (regra: só link de produto Amazon, nunca busca).
